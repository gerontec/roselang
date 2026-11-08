"""Rose as a plain Python module (benchmark variant B2): the same knowledge and checks as the
language, but as a library - every check runs when Python executes the line, not before.

    import rose
    flow = rose.law("water_heat_flow", "P = mdot*cp*dT",
                    P="W", mdot="kg/s", cp="J/(kg*K)", dT="K", defaults={"cp": rose.Q(4182, "J/(kg*K)")})
    flow.solve("mdot", P=rose.Q(9, "kW"), dT=rose.Q(5, "K"))     # -> 0.4304 kg/s
    ke = rose.use("law:kinetic_energy")                           # from std/ (Wikidata)
    rose.use("open:goldbachs_conjecture")                         # raises OpenProblem (E305)
    rose.plan("count the prime numbers below n")

Same building blocks as rosec: rose/units.py (dimensions), std/ + std/catalog.jsonl (knowledge),
sympy (solve), the exhaustive table check. Error classes carry the Rose diagnostic code.
"""
import itertools
import os
import re
import warnings

from . import std
from . import units as U

__all__ = ["Q", "Task", "law", "use", "table", "plan", "search", "get", "lock", "approx",
           "RoseError", "UnitError", "LawError", "OpenProblem", "UnknownRef", "TableError", "ContractError"]


# ---------------------------------------------------------------- errors
class RoseError(Exception):
    code = "E000"

    def __init__(self, code, message):
        super().__init__(f"{code}: {message}")
        self.code = code


class UnitError(RoseError, TypeError):
    pass


class LawError(RoseError):
    pass


class OpenProblem(RoseError):
    pass


class UnknownRef(RoseError, LookupError):
    pass


class TableError(RoseError):
    pass


class ContractError(RoseError, ValueError):
    pass


# ---------------------------------------------------------------- quantities
class Q:
    """A physical quantity: SI value + dimension. Absolute temperatures (degC, degF, a K value
    marked absolute) are affine: abs - abs -> difference, abs + abs -> UnitError E203."""
    __slots__ = ("v", "dim", "absolute")

    def __init__(self, value, unit="1", *, _si=False, _dim=None, _abs=False):
        if _si:
            self.v, self.dim, self.absolute = float(value), _dim, _abs
            return
        u = U.parse_unit(unit)
        self.v, self.dim, self.absolute = U.to_si(float(value), u), u.dim, u.absolute

    @staticmethod
    def _si(v, dim, absolute=False):
        return Q(v, _si=True, _dim=dim, _abs=absolute)

    # conversion
    def to(self, unit):
        """Value as float in `unit` ('kg/s', 'degC', 'kWh')."""
        u = U.parse_unit(unit)
        if u.dim != self.dim:
            raise UnitError("E201", f"cannot express {self!r} in {unit} ({U.unit_name(u.dim)})")
        return (self.v - u.offset) / u.scale

    def __float__(self):
        if self.dim != U.NONE:
            raise UnitError("E202", f"{self!r} is not dimensionless; use .to('<unit>')")
        return self.v

    def __repr__(self):
        if self.absolute:
            return f"{self.v - 273.15:.6g} degC"
        return f"{self.v:.6g}" if self.dim == U.NONE else f"{self.v:.6g} {U.unit_name(self.dim)}"

    # arithmetic
    @staticmethod
    def _wrap(x, op):
        if isinstance(x, Q):
            return x
        if isinstance(x, (int, float)) and not isinstance(x, bool):
            return Q._si(x, U.NONE)
        raise UnitError("E201", f"cannot apply '{op}' to a quantity and {type(x).__name__}")

    def _same(self, o, op):
        if self.dim != o.dim:
            code = "E202" if U.NONE in (self.dim, o.dim) else "E201"
            raise UnitError(code, f"'{op}' needs equal dimensions: {U.unit_name(self.dim)} vs "
                                  f"{U.unit_name(o.dim)}" + (" (number without unit?)" if code == "E202" else ""))

    def __add__(self, o):
        o = self._wrap(o, "+"); self._same(o, "+")
        if self.absolute and o.absolute:
            raise UnitError("E203", "cannot add two absolute temperatures")
        return Q._si(self.v + o.v, self.dim, self.absolute or o.absolute)

    __radd__ = __add__

    def __sub__(self, o):
        o = self._wrap(o, "-"); self._same(o, "-")
        if o.absolute and not self.absolute:
            raise UnitError("E203", "cannot subtract an absolute temperature from a difference")
        return Q._si(self.v - o.v, self.dim, self.absolute and not o.absolute)

    def __rsub__(self, o):
        return self._wrap(o, "-").__sub__(self)

    def __neg__(self):
        if self.absolute:
            raise UnitError("E203", "cannot negate an absolute temperature")
        return Q._si(-self.v, self.dim)

    def __mul__(self, o):
        o = self._wrap(o, "*")
        return Q._si(self.v * o.v, U.dmul(self.dim, o.dim))

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = self._wrap(o, "/")
        return Q._si(self.v / o.v, U.ddiv(self.dim, o.dim))

    def __rtruediv__(self, o):
        return self._wrap(o, "/").__truediv__(self)

    def __pow__(self, n):
        return Q._si(self.v ** n, U.dpow(self.dim, n))

    def _cmp(self, o, op):
        o = self._wrap(o, op); self._same(o, op)
        return self.v, o.v

    def __lt__(self, o):
        a, b = self._cmp(o, "<"); return a < b

    def __le__(self, o):
        a, b = self._cmp(o, "<="); return a <= b

    def __gt__(self, o):
        a, b = self._cmp(o, ">"); return a > b

    def __ge__(self, o):
        a, b = self._cmp(o, ">="); return a >= b

    def __eq__(self, o):
        if not isinstance(o, (Q, int, float)):
            return NotImplemented
        a, b = self._cmp(o, "=="); return a == b

    def __hash__(self):
        return hash((self.v, self.dim))


def approx(a, b, rel=1e-9, abs_=None):
    """a == b within a relative tolerance (or an absolute one given as Q)."""
    a, b = Q._wrap(a, "=="), Q._wrap(b, "==")
    a._same(b, "==")
    if abs_ is not None:
        return abs(a.v - b.v) <= Q._wrap(abs_, "within").v
    return abs(a.v - b.v) <= rel * max(abs(a.v), abs(b.v))


# ---------------------------------------------------------------- laws
_LOCK = []


def _sym_dim(e, dims):
    """Dimension of a sympy expression; None if unknown (pure numbers -> dimensionless)."""
    import sympy as sp
    if e.is_Number or e in (sp.pi, sp.E):
        return U.NONE
    if e.is_Symbol:
        return dims.get(str(e))
    if e.is_Add:
        ds = [_sym_dim(a, dims) for a in e.args]
        known = [d for d in ds if d is not None]
        if any(d != known[0] for d in known):
            raise ValueError("cannot add " + " and ".join(U.unit_name(d) for d in dict.fromkeys(known)))
        return known[0] if known else None
    if e.is_Mul:
        d = U.NONE
        for a in e.args:
            x = _sym_dim(a, dims)
            if x is None:
                return None
            d = U.dmul(d, x)
        return d
    if e.is_Pow:
        b, n = e.args
        db = _sym_dim(b, dims)
        if db is None or not n.is_Number:
            return None if db != U.NONE else U.NONE
        return U.dpow(db, n)
    if isinstance(e, sp.Function):
        return U.NONE
    return None


class Law:
    """An acausal equation set; solve(unknown, **given) returns a Q."""

    def __init__(self, name, eqs, units, defaults=None, valid=None, ref=None, intent=""):
        import sympy as sp
        self.name, self.ref, self.intent = name, ref, intent
        self.syms = {n: sp.Symbol(n, real=True) for n in units}
        self.units = {n: U.parse_unit(u) for n, u in units.items()}
        self.dims = {n: u.dim for n, u in self.units.items()}
        self.eqs = eqs
        self.defaults = dict(defaults or {})
        self.valid = dict(valid or {})
        self._cache = {}
        for lhs, rhs in eqs:
            try:
                a, b = _sym_dim(lhs, self.dims), _sym_dim(rhs, self.dims)
            except ValueError as e:
                raise LawError("E204", f"law '{name}' is dimensionally inconsistent: {e}")
            if a is not None and b is not None and a != b:
                raise LawError("E204", f"law '{name}' is dimensionally inconsistent: left side is "
                                       f"{U.unit_name(a)}, right side is {U.unit_name(b)}")

    def __repr__(self):
        return f"<law {self.name}: " + ", ".join(f"{l} = {r}" for l, r in self.eqs) + ">"

    def solve(self, unknown, **given):
        import sympy as sp
        if unknown not in self.syms:
            raise LawError("E207", f"law '{self.name}' has no variable '{unknown}' (has: {', '.join(self.syms)})")
        vals = {}
        for n, x in given.items():
            if n not in self.syms:
                raise LawError("E207", f"law '{self.name}' has no variable '{n}'")
            x = Q._wrap(x, f"given {n}")
            if x.dim != self.dims[n]:
                code = "E202" if x.dim == U.NONE else "E201"
                raise UnitError(code, f"given {n}: expected {U.unit_name(self.dims[n])}, got {U.unit_name(x.dim)}")
            vals[n] = x
        for n, x in self.defaults.items():
            if n not in vals and n != unknown:
                vals[n] = Q._wrap(x, n)
        for n, (lo, hi) in self.valid.items():
            if n in vals and not (lo <= vals[n] <= hi):
                raise ContractError("E400", f"outside validity range: {n} = {vals[n]!r} not in [{lo!r}, {hi!r}]")
        missing = [n for n in self.syms if n not in vals and n != unknown]
        unknowns = [unknown] + (missing if len(self.eqs) > 1 else [])
        if missing and len(self.eqs) == 1:
            raise LawError("E207", f"solve {self.name} for {unknown}: no value for {', '.join(missing)}")
        key = (tuple(unknowns), tuple(sorted(vals)))
        if key not in self._cache:
            eqs = [sp.Eq(l, r) for l, r in self.eqs]
            sols = sp.solve(eqs, [self.syms[u] for u in unknowns], dict=True)
            cands = [s[self.syms[unknown]] for s in sols if self.syms[unknown] in s]
            if not cands:
                raise LawError("E207", f"no closed-form solution of {self.name} for {unknown}")
            args = [self.syms[n] for n in sorted(vals)]
            self._cache[key] = [sp.lambdify(args, c, "math") for c in cands]
        xs = []
        for f in self._cache[key]:
            try:
                c = complex(f(*[vals[n].v for n in sorted(vals)]))
            except (ValueError, ZeroDivisionError):
                continue
            if abs(c.imag) <= 1e-12 * max(1.0, abs(c.real)):
                xs.append(c.real)
        pos = [x for x in xs if x >= 0]
        if len(pos) == 1 or (len(xs) == 1):
            x = pos[0] if len(pos) == 1 else xs[0]
        else:
            raise LawError("E207", f"{self.name}.{unknown}: {len(xs)} real solutions {xs}, cannot choose")
        out = Q._si(x, self.dims[unknown])
        if unknown in self.valid:
            lo, hi = self.valid[unknown]
            if not (lo <= out <= hi):
                raise ContractError("E400", f"result {unknown} = {out!r} outside [{lo!r}, {hi!r}]")
        return out


def law(name, *equations, defaults=None, valid=None, intent="", **units):
    """Define a law: law("ohm", "U = R*I", U="V", R="Ohm", I="A"). Checked for dimensions now."""
    import sympy as sp
    syms = {n: sp.Symbol(n, real=True) for n in units}
    eqs = []
    for text in equations:
        if text.count("=") != 1:
            raise LawError("E101", f"equation must contain exactly one '=': {text!r}")
        lhs, rhs = text.split("=")
        loc = dict(syms, pi=sp.pi)
        eqs.append((sp.sympify(lhs.replace("^", "**"), locals=loc), sp.sympify(rhs.replace("^", "**"), locals=loc)))
        free = {str(s) for l, r in eqs[-1:] for s in (l.free_symbols | r.free_symbols)}
        unknown = free - set(units)
        if unknown:
            raise LawError("E206", f"law '{name}': no unit given for {', '.join(sorted(unknown))}")
    return Law(name, eqs, units, defaults, valid, intent=intent)


# ---------------------------------------------------------------- knowledge
_K = None


def _knowledge():
    global _K
    if _K is None:
        from .knowledge import Knowledge
        _K = Knowledge()
    return _K


def _q_from_rose(e):
    from .nodes import BinOp, Num, Quantity, Unary
    if isinstance(e, Quantity):
        return Q(float(e.value), e.unit)
    if isinstance(e, Num):
        return Q._si(float(e.text), U.NONE)
    if isinstance(e, Unary):
        return -_q_from_rose(e.expr)
    if isinstance(e, BinOp) and e.op in "*/":
        a, b = _q_from_rose(e.left), _q_from_rose(e.right)
        return a * b if e.op == "*" else a / b
    raise RoseError("E306", f"cannot evaluate constant expression {type(e).__name__}")


class Task:
    """A solved programming task from a pack (Rosetta Code): description and solutions as source text.
    .code is the first solution that compiles as Python 3; nothing is executed."""

    def __init__(self, card, impls):
        self.ref, self.name, self.url = card["ref"], card["name"], card.get("url")
        self.license, self.description = card["license"], card.get("description") or card.get("intent", "")
        self.solutions = [i for i in impls if i.get("lang") == "python"]
        self.outputs = card.get("outputs", [])

    @property
    def python3(self):
        return [s["code"] for s in self.solutions if s.get("level") in ("parsed", "tested", "cross_checked", "proven")]

    @property
    def code(self):
        p3 = self.python3
        if not p3:
            raise UnknownRef("E302", f"'{self.ref}' has no Python 3 solution ({len(self.solutions)} Python solutions "
                                     "in total, none compiles as Python 3)")
        return p3[0]

    def __repr__(self):
        return f"<task {self.ref}: {len(self.solutions)} python solutions ({len(self.python3)} py3), {self.license}>"


def use(ref):
    """Bind a unit of the built-in knowledge: law -> Law, const -> Q, Rosetta task -> Task;
    open problem -> OpenProblem."""
    from .compiler import to_sympy
    from .nodes import Const, Law as LawNode, Open
    hit = std.lookup(ref)
    if hit is None:
        card = _knowledge().get(ref)
        if card is None:
            sim = _knowledge().similar_refs(ref)
            raise UnknownRef("E301", f"unknown ref '{ref}'" + (f"; did you mean {', '.join(sim[:3])}?" if sim else ""))
        if card["kind"] == "open":
            raise OpenProblem("E305", f"'{card['name']}' is an open problem - no known solution (negative knowledge)")
        if card.get("_pack"):
            impls = _knowledge().implementations(card["ref"])
            _LOCK.append({"ref": card["ref"], "level": card["level"], "license": card["license"],
                          "source": "pack " + os.path.basename(card["_pack"]), "url": card.get("url"),
                          "share_alike": bool(card.get("share_alike"))})
            if card.get("share_alike"):
                warnings.warn(f"R205: '{card['ref']}' is {card['license']} (share-alike); code that embeds it "
                              "inherits that licence", stacklevel=2)
            return Task(card, impls)
        raise UnknownRef("E306", f"'{ref}' ({card['kind']}, {card['level']}) has no machine-readable source yet"
                         + (f"; TeX: {card['tex'][:80]}" if card.get("tex") else ""))
    item, meta = hit
    _LOCK.append({"ref": ref, "level": meta.get("level"), "license": meta.get("license"),
                  "source": "std/" + meta["file"], "url": meta.get("url")})
    if isinstance(item, Open):
        raise OpenProblem("E305", f"'{item.intent.split(' - ')[0]}' is an open problem - no known solution "
                                  "(negative knowledge); solve a bounded sub-question instead")
    if isinstance(item, Const):
        return _q_from_rose(item.expr)
    if isinstance(item, LawNode):
        import sympy as sp
        units = {v.name: (v.type.unit or "1") for v in item.vars}
        syms = {n: sp.Symbol(n, real=True) for n in units}
        eqs = [(to_sympy(l, syms), to_sympy(r, syms)) for l, r in item.eqs]
        defaults = {v.name: _q_from_rose(v.default) for v in item.vars if v.default is not None}
        valid = {n: (_q_from_rose(lo), _q_from_rose(hi)) for n, lo, hi in item.valid}
        return Law(item.name, eqs, units, defaults, valid, ref=ref, intent=item.intent)
    raise RoseError("E302", f"'{ref}' has no python binding")


def plan(task, k=8):
    return _knowledge().plan(task, k=k)


def search(query, k=10, kind=None):
    return _knowledge().search(query, k=k, kind=kind)[0]


def get(ref):
    return _knowledge().get(ref)


def lock():
    """Provenance and licence of every unit bound with use() in this process."""
    return list(_LOCK)


# ---------------------------------------------------------------- decision tables
_CELL = re.compile(r"^\s*(>=|<=|>|<|==)\s*([-+0-9.eE]+)\s*(.*)$")


def _cell(c, spec):
    """Parse one rule cell into (predicate, threshold or None). '-' or None matches anything."""
    if c is None or c == "-":
        return (lambda x: True), None
    if spec is bool or isinstance(spec, (set, list)):
        return (lambda x, c=c: x == c), None
    m = _CELL.match(c) if isinstance(c, str) else None
    if not m:
        raise TableError("E101", f"cannot read rule cell {c!r} (expected e.g. '>= 20 %')")
    op, num, unit = m.groups()
    want = U.parse_unit(spec[0]).dim
    t = Q(float(num), unit or "1")
    if t.dim != want:
        raise UnitError("E202" if t.dim == U.NONE else "E201",
                        f"rule cell {c!r}: expected {U.unit_name(want)}, got {U.unit_name(t.dim)}")
    f = {">=": lambda x: x >= t, "<=": lambda x: x <= t, ">": lambda x: x > t, "<": lambda x: x < t,
         "==": lambda x: x == t}[op]
    return f, t


def table(name, inputs, rules, hit="unique", intent=""):
    """Decision table, checked exhaustively when it is defined.
    inputs: {"soc": ("%", 0, 100), "grid_ok": bool, "mode": ["eco", "boost"]}
    rules:  [(">= 20 %", True, "battery"), ...] - one cell per input, then the output."""
    names = list(inputs)
    parsed = []
    for r in rules:
        if len(r) != len(names) + 1:
            raise TableError("E101", f"rule {r!r} has {len(r) - 1} cells, table has {len(names)} inputs")
        cells = [_cell(c, inputs[n]) for c, n in zip(r[:-1], names)]
        parsed.append(([f for f, _ in cells], [t for _, t in cells], r[-1]))
    axes = []
    for k, n in enumerate(names):
        spec = inputs[n]
        if spec is bool:
            axes.append([True, False])
        elif isinstance(spec, (set, list)):
            axes.append(list(spec))
        else:
            unit, lo, hi = spec
            lo, hi = Q(lo, unit), Q(hi, unit)
            pts = sorted({t.v for _, ts, _ in parsed for t in [ts[k]] if t is not None} | {lo.v, hi.v})
            samples = pts + [(a + b) / 2 for a, b in zip(pts, pts[1:])]
            d = lo.dim
            axes.append([Q._si(x, d) for x in sorted(samples) if lo.v <= x <= hi.v])
    for point in itertools.product(*axes):
        matched = [i for i, (fs, _, _) in enumerate(parsed) if all(f(x) for f, x in zip(fs, point))]
        shown = ", ".join(f"{n} = {v!r}" for n, v in zip(names, point))
        if not matched:
            raise TableError("E511", f"table '{name}' has no rule for {shown}")
        if len(matched) > 1 and hit == "unique":
            raise TableError("E512", f"table '{name}': rules {', '.join(str(i + 1) for i in matched)} "
                                     f"all match {shown} (hit unique)")

    def decide(**kw):
        point = [kw[n] for n in names]
        for fs, _, out in parsed:
            if all(f(x) for f, x in zip(fs, point)):
                return out
        raise ContractError("E511", f"table {name}: no rule matches")
    decide.__name__, decide.__doc__ = name, f"{intent} (decision table, hit {hit})"
    return decide
