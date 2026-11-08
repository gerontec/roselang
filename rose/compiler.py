"""Rose v1 checker + Python code generator (one pass: every expression yields (code, type)).

Supported in v1: module, target, use (law/math/const/oeis/open from the corpus), const, fn,
law + solve (sympy), table (hit unique/first, exhaustive check), test.
machine/ctrl/model are recognised and skipped with R199 (planned for M5/M6).
"""
import itertools
import json
import math

from . import types as Ty
from . import units as U
from .diag import Diag, RoseError
from .nodes import *  # noqa: F401,F403
from .parser import parse

VERSION = "0.1.0"
BUILTIN_DIMLESS = {"exp": "math.exp", "ln": "math.log", "log10": "math.log10", "sin": "math.sin",
                   "cos": "math.cos", "tan": "math.tan", "asin": "math.asin", "acos": "math.acos",
                   "atan": "math.atan", "sinh": "math.sinh", "cosh": "math.cosh", "tanh": "math.tanh"}

PRELUDE = '''import math


class RoseContractError(AssertionError):
    pass


def _require(ok, what):
    if not ok:
        raise RoseContractError("require failed: " + what)


def _ensure(ok, what):
    if not ok:
        raise RoseContractError("ensure failed: " + what)


def _valid(x, lo, hi, what):
    if not (lo <= x <= hi):
        raise RoseContractError(f"outside validity range: {what} = {x!r} not in [{lo!r}, {hi!r}]")
    return x


def _is_sorted(xs):
    return all(a <= b for a, b in zip(xs, xs[1:]))


def _pick(cands, what):
    real = []
    for c in cands:
        c = complex(c)
        if abs(c.imag) <= 1e-12 * max(1.0, abs(c.real)):
            real.append(c.real)
    pos = [c for c in real if c >= 0]
    if len(pos) == 1:
        return pos[0]
    if len(real) == 1:
        return real[0]
    raise RoseContractError(f"solve {what}: {len(real)} real solutions {real}, cannot pick one")


class OeisSequence:
    """Leading terms of an OEIS sequence (offset = index of the first term)."""
    def __init__(self, anum, terms, offset=0):
        self.anum, self.terms, self.offset = anum, [int(t) for t in terms], offset
        self._set = set(self.terms)

    def __call__(self, n):
        return self.terms[n - self.offset]

    def contains(self, x):
        # beyond the stored terms membership is unknown: do not fail a contract on missing data
        if self.terms and x > max(self.terms):
            return True
        return x in self._set


def _close(a, b, rel=1e-9, abs_=0.0):
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        return len(a) == len(b) and all(_close(x, y, rel, abs_) for x, y in zip(a, b))
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.isclose(a, b, rel_tol=rel, abs_tol=abs_)
    return a == b
'''


class Sig:
    def __init__(self, name, params, ret, pyname=None):
        self.name, self.params, self.ret, self.pyname = name, params, ret, pyname or name


class LawInfo:
    def __init__(self, node, ref=None, source_note=None):
        self.node, self.ref, self.source_note = node, ref, source_note
        self.vars = {}       # name -> Ty
        self.defaults = {}   # name -> (code, Ty)


class Compiler:
    def __init__(self, corpus=None, file="<src>"):
        self.corpus = corpus
        self.file = file
        self.diags = []
        self.out = []          # generated top-level code blocks
        self.helpers = []
        self.consts = {}       # name -> (pyname, Ty)
        self.fns = {}          # name -> Sig
        self.laws = {}         # local name -> LawInfo
        self.objects = {}      # alias -> ("oeis", pyname) | ("const", pyname, Ty)
        self.enum_members = {}
        self.lock = []         # pinned corpus units
        self.solve_n = 0
        self.tests = []

    # ---- diagnostics ----
    def d(self, code, msg, node=None, fix=None):
        p = getattr(node, "pos", None) or Pos()
        self.diags.append(Diag(code, msg, self.file, p.line, p.col, fix or []))

    @property
    def errors(self):
        return [x for x in self.diags if x.severity == "error"]

    # ---- types from syntax ----
    def ty(self, t: TypeRef):
        if t is None:
            return Ty.ANY
        if t.base == "Real":
            if t.unit:
                try:
                    return Ty.from_unit_text(t.unit)
                except ValueError as e:
                    self.d("E208", str(e), t)
                    return Ty.ANY
            return Ty.REAL
        if t.base in ("Int", "Bool", "Text"):
            return Ty.Ty(t.base)
        if t.base in ("List", "Opt"):
            return Ty.Ty("List", args=(self.ty(t.args[0]) if t.args else Ty.ANY,))
        if t.base == "Enum":
            for m in t.members:
                self.enum_members[m] = t
            return Ty.Ty("Enum", members=tuple(t.members))
        return Ty.ANY  # opaque (e.g. Fasta, bio.Hit) in v1

    # ---- module ----
    def compile_module(self, mod: Module):
        if not mod.targets:
            mod.targets = ["python"]
        for t in mod.targets:
            if t not in ("python", "c", "st", "esphome"):
                self.d("E302", f"unknown target '{t}'")
        for u in mod.uses:
            self.bind_use(u)
        # declare first so that order of items does not matter
        for it in mod.items:
            if isinstance(it, Fn):
                params = [(p.name, self.ty(p.type)) for p in it.params]
                self.fns[it.name] = Sig(it.name, params, self.ty(it.ret))
            elif isinstance(it, Table):
                self.declare_table(it)
            elif isinstance(it, Law):
                self.laws[it.name] = LawInfo(it)
        for it in mod.items:
            if isinstance(it, Const):
                self.compile_const(it)
        for it in mod.items:
            if isinstance(it, Law):
                self.compile_law(self.laws[it.name])
            elif isinstance(it, Fn):
                self.compile_fn(it)
            elif isinstance(it, Table):
                self.compile_table(it)
            elif isinstance(it, Test):
                self.compile_test(it)
            elif isinstance(it, Unsupported):
                self.d("R199", f"'{it.kind} {it.name}' is planned for a later milestone "
                               f"({'M5' if it.kind == 'machine' else 'M6'}); skipped in v1", it)
        for t in mod.targets:
            if t != "python":
                self.d("R199", f"target '{t}' is planned (M5/M6); v1 generates python only")
        return self.render(mod)

    # ---- use ----
    def bind_use(self, u: Use):
        if self.corpus is None or not self.corpus.online:
            self.d("E301", f"cannot resolve '{u.ref}': corpus offline"
                           + (f" ({self.corpus.error})" if self.corpus else ""), u)
            return
        unit = self.corpus.get(u.ref)
        if unit is None:
            sim = self.corpus.similar_refs(u.ref)
            hint = " - this source is not imported yet (Rosetta Code = milestone M1)" if u.scheme == "rc" else ""
            self.d("E301", f"unknown ref '{u.ref}'{hint}", u,
                   [{"did_you_mean": sim}] if sim else [])
            return
        self.lock.append({"ref": unit["ref"], "level": unit["level"], "license": unit["license"],
                          "source": unit["source"], "url": unit["source_url"]})
        if unit["share_alike"]:
            self.d("R205", f"'{unit['ref']}' comes from a share-alike source ({unit['license']}); "
                           "generated code that embeds it inherits that licence", u)
        if unit["kind"] == "open":
            self.d("E305", f"'{unit['name']}' is an open problem - no known solution exists (negative "
                           "knowledge). It cannot be used as a building block.", u,
                   [{"why": "solve a bounded or numerical sub-question instead, or state it as an assumption"}])
            return
        if unit["kind"] in ("law", "math") and not unit["ref"].startswith("oeis:"):
            if not unit["rose_src"]:
                self.d("E306", f"'{unit['ref']}' has no machine-readable equation yet (only TeX: "
                               f"{(unit['payload'].get('tex') or ['-'])[0][:80]}); level {unit['level']}", u)
                return
            try:
                law_mod = parse(unit["rose_src"], unit["ref"])
            except RoseError as e:
                self.d("E306", f"corpus source of '{unit['ref']}' does not parse: {e.diag.message}", u)
                return
            law = next(i for i in law_mod.items if isinstance(i, Law))
            info = LawInfo(law, unit["ref"])
            self.laws[u.local] = info
            self.laws.setdefault(law.name, info)
            self.compile_law(info)
            return
        if unit["ref"].startswith("oeis:"):
            py = f"_oeis_{unit['ref'][5:]}"
            terms = unit["payload"].get("terms", [])
            self.helpers.append(f"{py} = OeisSequence({unit['ref'][5:]!r}, {terms!r})")
            self.objects[u.local] = ("oeis", py)
            return
        if unit["kind"] == "const":
            if not unit["rose_src"]:
                self.d("E306", f"constant '{unit['ref']}' has no Rose source", u)
                return
            c = next(i for i in parse("module c\n" + unit["rose_src"], unit["ref"]).items)
            code, t = self.expr(c.expr, {})
            py = "_c_" + unit["ref"].split(".")[-1]
            self.helpers.append(f"{py} = {code}  # {unit['ref']}")
            self.objects[u.local] = ("const", py, self.ty(c.type))
            return
        self.d("E302", f"'{unit['ref']}' (kind {unit['kind']}) has no python implementation in v1", u)

    # ---- const ----
    def compile_const(self, c: Const):
        want = self.ty(c.type)
        code, got = self.expr(c.expr, {})
        self.assignable(want, got, c.expr, f"const {c.name}")
        self.consts[c.name] = (c.name, want if want.base != "Any" else got)
        self.out.append(f"{c.name} = {code}")

    # ---- laws ----
    def law_dim(self, e, vars_):
        """Dimension of an expression inside a law; None if not determinable."""
        if isinstance(e, Num):
            return U.NONE
        if isinstance(e, Quantity):
            return U.parse_unit(e.unit).dim
        if isinstance(e, Name):
            t = vars_.get(e.text)
            return t.dim if t is not None and t.base in ("Real", "Int") else None
        if isinstance(e, Unary):
            return self.law_dim(e.expr, vars_)
        if isinstance(e, BinOp):
            a, b = self.law_dim(e.left, vars_), self.law_dim(e.right, vars_)
            if e.op in ("+", "-"):
                if a is not None and b is not None and a != b:
                    raise ValueError(f"cannot add {U.dim_str(a)} and {U.dim_str(b)}")
                return a if a is not None else b
            if e.op == "*":
                return None if a is None or b is None else U.dmul(a, b)
            if e.op == "/":
                return None if a is None or b is None else U.ddiv(a, b)
            if e.op == "^":
                if b not in (None, U.NONE):
                    raise ValueError("exponent must be dimensionless")
                n = const_number(e.right)
                if a == U.NONE:
                    return U.NONE
                if n is None or a is None:
                    return None
                return U.dpow(a, n)
        if isinstance(e, Call) and isinstance(e.func, Name):
            f = e.func.text
            args = [self.law_dim(x, vars_) for _, x in e.args]
            if f == "sqrt" and args:
                return None if args[0] is None else U.dpow(args[0], 0.5)
            if f in ("abs",) and args:
                return args[0]
            if f in BUILTIN_DIMLESS:
                if args and args[0] not in (None, U.NONE):
                    raise ValueError(f"{f}() needs a dimensionless argument, got {U.dim_str(args[0])}")
                return U.NONE
        return None

    def compile_law(self, info: LawInfo):
        law = info.node
        if info.vars:
            return
        for v in law.vars:
            t = self.ty(v.type)
            info.vars[v.name] = t
            if v.default is not None:
                info.defaults[v.name] = self.expr(v.default, {})
        for lhs, rhs in law.eqs:
            try:
                a, b = self.law_dim(lhs, info.vars), self.law_dim(rhs, info.vars)
                if a is not None and b is not None and a != b:
                    raise ValueError(f"left side is {U.dim_str(a)}, right side is {U.dim_str(b)}")
            except ValueError as e:
                self.d("E204", f"law '{law.name}' is dimensionally inconsistent: {e}", lhs)

    def solve(self, e: Solve, env):
        info = self.laws.get(e.law)
        if info is None:
            self.d("E206", f"unknown law '{e.law}' (declare it with `law` or `use law:...`)", e)
            return "None", Ty.ANY
        law = info.node
        if e.unknown not in info.vars:
            self.d("E207", f"law '{law.name}' has no variable '{e.unknown}' (has: {', '.join(info.vars)})", e)
            return "None", Ty.ANY
        try:
            import sympy as sp
        except ImportError:
            self.d("E207", "sympy is required for solve", e)
            return "None", Ty.ANY
        syms = {n: sp.Symbol(n, real=True) for n in info.vars}
        given_codes, given_names = [], []
        for n, ex in e.givens:
            if n not in info.vars:
                self.d("E207", f"law '{law.name}' has no variable '{n}'", ex)
                continue
            code, t = self.expr(ex, env)
            self.assignable(info.vars[n], t, ex, f"given {n}")
            given_codes.append(code)
            given_names.append(n)
        eqs = [sp.Eq(to_sympy(l, syms), to_sympy(r, syms)) for l, r in law.eqs]
        unknowns = {e.unknown}
        missing = [n for n in info.vars if n not in given_names and n != e.unknown and n not in info.defaults]
        if len(eqs) > 1:
            # system: the other free variables are eliminated as additional unknowns
            unknowns |= set(missing)
            missing = []
        if missing:
            self.d("E207", f"solve {law.name} for {e.unknown}: no value for {', '.join(missing)} "
                           "(add them to `given` or give the law var a default)", e)
            return "None", Ty.ANY
        try:
            sols = sp.solve(eqs, [syms[u] for u in sorted(unknowns)], dict=True)
        except Exception as ex:
            self.d("E207", f"sympy could not solve {law.name} for {e.unknown}: {ex}", e)
            return "None", Ty.ANY
        cands = [s[syms[e.unknown]] for s in sols if syms[e.unknown] in s]
        if not cands:
            self.d("E207", f"no closed-form solution of {law.name} for {e.unknown}", e)
            return "None", Ty.ANY
        self.solve_n += 1
        fname = f"_solve_{law.name}_{e.unknown}_{self.solve_n}"
        args = given_names + [n for n in info.defaults if n not in given_names and n != e.unknown]
        body = [f"def {fname}({', '.join(args)}):",
                f'    """solve {law.name} for {e.unknown}{" (" + info.ref + ")" if info.ref else ""}: '
                f'{", ".join(str(c) for c in cands)}"""']
        for vn, lo, hi in law.valid:
            if vn in args:
                lc, _ = self.expr(lo, {}); hc, _ = self.expr(hi, {})
                body.append(f"    _valid({vn}, {lc}, {hc}, {vn!r})")
        pys = [sp.pycode(c, fully_qualified_modules=True) for c in cands]
        if len(pys) == 1:
            body.append(f"    x = {pys[0]}")
        else:
            body.append(f"    x = _pick([{', '.join(pys)}], {law.name + '.' + e.unknown!r})")
        for vn, lo, hi in law.valid:
            if vn == e.unknown:
                lc, _ = self.expr(lo, {}); hc, _ = self.expr(hi, {})
                body.append(f"    _valid(x, {lc}, {hc}, {vn!r})")
        body.append("    return x")
        self.helpers.append("\n".join(body))
        call_args = given_codes + [info.defaults[n][0] for n in info.defaults if n not in given_names and n != e.unknown]
        return f"{fname}({', '.join(call_args)})", info.vars[e.unknown]

    # ---- fn ----
    def compile_fn(self, f: Fn):
        sig = self.fns[f.name]
        env = {n: t for n, t in sig.params}
        lines = [f"def {f.name}({', '.join(n for n, _ in sig.params)}):", f'    """{f.intent}"""']
        for p in f.params:
            for chk in self.refinement_checks(p.name, p.type, env):
                lines.append(f"    _require({chk}, {chk!r})")
        for r in f.requires:
            code, t = self.expr(r, env)
            self.expect_bool(t, r, "require")
            lines.append(f"    _require({code}, {code!r})")
        if isinstance(f.body, list):
            inner = [f"    def _body({', '.join(n for n, _ in sig.params)}):"]
            inner += self.block(f.body, dict(env), 2, sig.ret)
            if not ends_with_return(f.body):
                inner.append("        return None")
            lines += inner
            lines.append(f"    result = _body({', '.join(n for n, _ in sig.params)})")
        else:
            code, t = self.expr(f.body, env)
            self.assignable(sig.ret, t, f.body, f"return value of {f.name}")
            lines.append(f"    result = {code}")
        env_r = dict(env, result=sig.ret)
        for chk in self.refinement_checks("result", f.ret, env_r):
            lines.append(f"    _ensure({chk}, {chk!r})")
        for en in f.ensures:
            code, t = self.expr(en, env_r)
            self.expect_bool(t, en, "ensure")
            lines.append(f"    _ensure({code}, {code!r})")
        lines.append("    return result")
        self.out.append("\n".join(lines))

    def refinement_checks(self, name, t: TypeRef, env):
        if t is None or t.refine is None:
            return []
        if t.refine[0] == "cmp":
            code, _ = self.expr(t.refine[2], env)
            return [f"{name} {t.refine[1]} {code}"]
        lo, _ = self.expr(t.refine[1], env)
        hi, _ = self.expr(t.refine[2], env)
        return [f"{lo} <= {name} <= {hi}"]

    def block(self, stmts, env, depth, ret):
        ind = "    " * depth
        out = []
        for s in stmts:
            if isinstance(s, Let):
                code, t = self.expr(s.expr, env)
                if s.type is not None:
                    want = self.ty(s.type)
                    self.assignable(want, t, s.expr, f"let {s.name}")
                    t = want
                env[s.name] = t
                out.append(f"{ind}{s.name} = {code}")
            elif isinstance(s, Assign):
                code, t = self.expr(s.expr, env)
                if s.name not in env:
                    self.d("E206", f"assignment to undeclared '{s.name}' (use let)", s)
                else:
                    self.assignable(env[s.name], t, s.expr, s.name)
                out.append(f"{ind}{s.name} = {code}")
            elif isinstance(s, Return):
                code, t = self.expr(s.expr, env)
                self.assignable(ret, t, s.expr, "return value")
                out.append(f"{ind}return {code}")
            elif isinstance(s, If):
                for k, (c, body) in enumerate(s.branches):
                    code, t = self.expr(c, env)
                    self.expect_bool(t, c, "if")
                    out.append(f"{ind}{'if' if k == 0 else 'elif'} {code}:")
                    out += self.block(body, dict(env), depth + 1, ret) or [f"{ind}    pass"]
                if s.orelse:
                    out.append(f"{ind}else:")
                    out += self.block(s.orelse, dict(env), depth + 1, ret)
            elif isinstance(s, For):
                code, t = self.expr(s.iter, env)
                inner = dict(env)
                inner[s.var] = t.args[0] if t.args else Ty.ANY
                out.append(f"{ind}for {s.var} in {code}:")
                out += self.block(s.body, inner, depth + 1, ret) or [f"{ind}    pass"]
            elif isinstance(s, While):
                code, t = self.expr(s.cond, env)
                self.expect_bool(t, s.cond, "while")
                out.append(f"{ind}while {code}:")
                out += self.block(s.body, dict(env), depth + 1, ret) or [f"{ind}    pass"]
            elif isinstance(s, ExprStmt):
                code, _ = self.expr(s.expr, env)
                out.append(f"{ind}{code}")
        return out

    # ---- tables ----
    def declare_table(self, t: Table):
        params = [(p.name, self.ty(p.type)) for p in t.ins]
        outs = [self.ty(p.type) for p in t.outs]
        self.fns[t.name] = Sig(t.name, params, outs[0] if len(outs) == 1 else Ty.ANY)

    def compile_table(self, t: Table):
        env = {p.name: self.ty(p.type) for p in t.ins}
        axes = []
        for k, p in enumerate(t.ins):
            pt = env[p.name]
            if pt.base == "Bool":
                axes.append([True, False])
            elif pt.base == "Enum":
                axes.append(list(pt.members))
            elif pt.numeric:
                lo = hi = None
                if p.type.refine and p.type.refine[0] == "range":
                    lo = const_value(p.type.refine[1]); hi = const_value(p.type.refine[2])
                pts = set()
                for cells, _, _ in t.rules:
                    c = cells[k] if k < len(cells) else ("any",)
                    for ex in c[1:] if c[0] in ("cmp", "eq", "range") else ():
                        v = const_value(ex)
                        if v is not None:
                            pts.add(v)
                pts |= {x for x in (lo, hi) if x is not None}
                pts = sorted(pts)
                samples = list(pts)
                for a, b in zip(pts, pts[1:]):
                    samples.append((a + b) / 2)
                if pts:
                    if lo is None:
                        samples.append(pts[0] - 1)
                    if hi is None:
                        samples.append(pts[-1] + 1)
                else:
                    samples = [0.0]
                axes.append(sorted(x for x in samples if (lo is None or x >= lo) and (hi is None or x <= hi)))
            else:
                axes.append([None])
        conds = []
        for cells, res, rp in t.rules:
            if len(cells) != len(t.ins):
                self.d("E101", f"rule has {len(cells)} cells, table has {len(t.ins)} inputs", Pos(*[rp.line, rp.col]) and rp)
            parts = []
            for k, c in enumerate(cells[:len(t.ins)]):
                nm = t.ins[k].name
                if c[0] == "any":
                    continue
                code, ct = self.expr(c[-1] if c[0] != "range" else c[1], env)
                if c[0] == "cmp":
                    self.same_dims(env[nm], ct, c[2], c[1])
                    parts.append(f"{nm} {c[1]} {code}")
                elif c[0] == "range":
                    hc, _ = self.expr(c[2], env)
                    parts.append(f"{code} <= {nm} <= {hc}")
                else:
                    parts.append(f"{nm} == {code}")
            outs = [self.expr(r, env)[0] for r in res]
            conds.append((" and ".join(parts) or "True", outs[0] if len(outs) == 1 else "(" + ", ".join(outs) + ")"))
        # exhaustive check over all sample points
        names = [p.name for p in t.ins]
        if t.hit in ("unique", "first"):
            for point in itertools.product(*axes):
                scope = dict(zip(names, point))
                matched = [i for i, (cond, _) in enumerate(conds) if eval_cond(cond, scope)]
                shown = ", ".join(f"{n} = {fmt_point(v, env[n])}" for n, v in scope.items())
                if not matched and ("complete" in t.checks or not t.checks):
                    self.d("E511", f"table '{t.name}' has no rule for {shown}", t)
                    break
                if len(matched) > 1 and t.hit == "unique" and ("no_overlap" in t.checks or not t.checks):
                    self.d("E512", f"table '{t.name}': rules {', '.join(str(i + 1) for i in matched)} "
                                   f"all match {shown} (hit unique)", t)
                    break
        lines = [f"def {t.name}({', '.join(names)}):", f'    """{t.intent} (decision table, hit {t.hit})"""']
        for cond, out in conds:
            lines.append(f"    if {cond}:")
            lines.append(f"        return {out}")
        lines.append(f"    raise RoseContractError('table {t.name}: no rule matches')")
        self.out.append("\n".join(lines))

    # ---- tests ----
    def compile_test(self, t: Test):
        e = t.expr
        if isinstance(e, BinOp) and e.op == "==" and (t.within is not None or True):
            a, ta = self.expr(e.left, {})
            b, tb = self.expr(e.right, {})
            self.same_dims(ta, tb, e, "==")
            if t.within is not None:
                w, tw = self.expr(t.within, {})
                rel = isinstance(t.within, Quantity) and t.within.unit == "%" or (tw.numeric and not tw.dimensioned)
                cond = f"_close({a}, {b}, rel={w})" if rel else f"_close({a}, {b}, rel=0.0, abs_={w})"
            else:
                cond = f"_close({a}, {b})"
            shown = f"({a}, {b})"
        else:
            cond, tt = self.expr(e, {})
            self.expect_bool(tt, e, "test")
            shown = "None"
        self.tests.append((t.pos.line, cond, shown, src_of(e)))

    # ---- expressions ----
    def expr(self, e, env):
        if isinstance(e, Num):
            return (e.text, Ty.INT) if e.is_int else (repr(float(e.text)), Ty.REAL)
        if isinstance(e, Quantity):
            try:
                u = U.parse_unit(e.unit)
            except ValueError as ex:
                self.d("E208", str(ex), e)
                return "None", Ty.ANY
            v = U.to_si(float(e.value), u)
            return repr(v), Ty.real(u.dim, u.absolute)
        if isinstance(e, Str):
            return repr(e.value), Ty.TEXT
        if isinstance(e, Bool):
            return repr(e.value), Ty.BOOL
        if isinstance(e, ListLit):
            items = [self.expr(x, env) for x in e.items]
            et = items[0][1] if items else Ty.ANY
            return "[" + ", ".join(c for c, _ in items) + "]", Ty.list_of(et)
        if isinstance(e, Range):
            lo, tl = self.expr(e.lo, env)
            hi, th = self.expr(e.hi, env)
            self.same_dims(tl, th, e, "..")
            return f"({lo}, {hi})", Ty.Ty("Range", args=(tl,))
        if isinstance(e, Name):
            return self.name(e, env)
        if isinstance(e, Ref):
            fake = Use(e.scheme, e.name, "_ref_" + e.name.replace(".", "_"), None, e.pos)
            self.bind_use(fake)
            obj = self.objects.get(fake.local)
            if obj and obj[0] == "const":
                return obj[1], obj[2]
            return "None", Ty.ANY
        if isinstance(e, Attr):
            if isinstance(e.obj, Name) and e.obj.text in self.objects:
                obj = self.objects[e.obj.text]
                if obj[0] == "oeis" and e.name == "contains":
                    return f"{obj[1]}.contains", Ty.Ty("Fn", args=(Ty.INT,))
            code, _ = self.expr(e.obj, env)
            return f"{code}.{e.name}", Ty.ANY
        if isinstance(e, Unary):
            code, t = self.expr(e.expr, env)
            if e.op == "not":
                self.expect_bool(t, e, "not")
                return f"(not {code})", Ty.BOOL
            return f"(-{code})", t
        if isinstance(e, BinOp):
            return self.binop(e, env)
        if isinstance(e, Call):
            return self.call(e, env)
        if isinstance(e, Solve):
            return self.solve(e, env)
        self.d("E101", f"unsupported expression {type(e).__name__}", e)
        return "None", Ty.ANY

    def name(self, e: Name, env):
        n = e.text
        if n in env:
            return n, env[n]
        if n in self.consts:
            return self.consts[n]
        if n in self.objects:
            o = self.objects[n]
            return (o[1], o[2]) if o[0] == "const" else (o[1], Ty.ANY)
        if n in self.fns:
            return n, Ty.Ty("Fn")
        if n in self.enum_members:
            return repr(n), Ty.Ty("Enum", members=(n,))
        if n == "pi":
            return "math.pi", Ty.REAL
        self.d("E206", f"unknown name '{n}'", e)
        return n, Ty.ANY

    def binop(self, e: BinOp, env):
        a, ta = self.expr(e.left, env)
        b, tb = self.expr(e.right, env)
        op = e.op
        if op in ("and", "or"):
            self.expect_bool(ta, e.left, op); self.expect_bool(tb, e.right, op)
            return f"({a} {op} {b})", Ty.BOOL
        if op in ("==", "!=", "<", "<=", ">", ">="):
            self.same_dims(ta, tb, e, op)
            return f"({a} {op} {b})", Ty.BOOL
        if ta.base == "Any" or tb.base == "Any":
            return f"({a} {pyop(op)} {b})", Ty.ANY
        if not (ta.numeric and tb.numeric):
            if op == "+" and ta.base == tb.base and ta.base in ("Text", "List"):
                return f"({a} + {b})", ta
            self.d("E205", f"operator '{op}' needs numbers, got {ta} and {tb}", e)
            return f"({a} {pyop(op)} {b})", Ty.ANY
        if op in ("+", "-"):
            if ta.absolute and tb.absolute:
                if op == "-":
                    return f"({a} - {b})", Ty.real(U.TH)
                self.d("E203", "cannot add two absolute temperatures (degC + degC)", e,
                       [{"why": "one of them is probably a temperature difference: write it in K"}])
                return f"({a} + {b})", ta
            if ta.absolute or tb.absolute:
                other = tb if ta.absolute else ta
                if other.dim != U.TH:
                    self.unit_mismatch(ta, tb, e, op)
                return f"({a} {op} {b})", (ta if ta.absolute else tb) if op == "+" or ta.absolute else ta
            self.same_dims(ta, tb, e, op)
            res = ta if ta.dimensioned or ta.base == "Real" else tb
            if ta.base == "Int" and tb.base == "Int":
                res = Ty.INT
            return f"({a} {op} {b})", res
        if op == "*":
            return f"({a} * {b})", self.mul_ty(ta, tb, U.dmul)
        if op == "/":
            return f"({a} / {b})", self.mul_ty(ta, tb, U.ddiv, div=True)
        if op == "mod":
            return f"({a} % {b})", ta
        if op == "^":
            if tb.dimensioned:
                self.d("E201", "exponent must be dimensionless", e.right)
            n = const_number(e.right)
            if ta.dimensioned:
                if n is None:
                    self.d("E201", "a quantity can only be raised to a constant exponent", e.right)
                    return f"({a} ** {b})", Ty.ANY
                try:
                    return f"({a} ** {b})", Ty.real(U.dpow(ta.dim, n))
                except ValueError:
                    self.d("E201", f"{ta} ^ {n} gives a fractional dimension", e)
                    return f"({a} ** {b})", Ty.ANY
            return f"({a} ** {b})", Ty.INT if ta.base == "Int" and tb.base == "Int" else Ty.REAL
        return f"({a} {pyop(op)} {b})", Ty.ANY

    def mul_ty(self, ta, tb, f, div=False):
        if ta.base == "Int" and tb.base == "Int" and not div:
            return Ty.INT
        return Ty.real(f(ta.dim, tb.dim))

    def call(self, e: Call, env):
        if isinstance(e.func, Name):
            n = e.func.text
            args = [(k, self.expr(x, env), x) for k, x in e.args]
            if n in self.fns:
                return self.call_sig(self.fns[n], args, e)
            if n in self.objects and self.objects[n][0] == "oeis":
                return f"{self.objects[n][1]}({', '.join(c for _, (c, _), _ in args)})", Ty.INT
            return self.builtin(n, args, e)
        code, t = self.expr(e.func, env)
        args = [self.expr(x, env)[0] for _, x in e.args]
        return f"{code}({', '.join(args)})", Ty.BOOL if t.base == "Fn" and t.args else Ty.ANY

    def call_sig(self, sig: Sig, args, e):
        pos = [a for a in args if a[0] is None]
        kws = {a[0]: a for a in args if a[0] is not None}
        if len(pos) > len(sig.params):
            self.d("E205", f"{sig.name}() takes {len(sig.params)} arguments, got {len(args)}", e)
        codes = []
        for i, (pn, pt) in enumerate(sig.params):
            if i < len(pos):
                a = pos[i]
            elif pn in kws:
                a = kws.pop(pn)
            else:
                self.d("E205", f"{sig.name}() missing argument '{pn}'", e)
                codes.append("None")
                continue
            _, (code, t), node = a
            self.assignable(pt, t, node, f"argument '{pn}' of {sig.name}")
            codes.append(code)
        for k in kws:
            self.d("E205", f"{sig.name}() has no parameter '{k}'", e)
        return f"{sig.pyname}({', '.join(codes)})", sig.ret

    def builtin(self, n, args, e):
        codes = [c for _, (c, _), _ in args]
        tys = [t for _, (_, t), _ in args]
        if n == "sqrt":
            t = tys[0] if tys else Ty.ANY
            if t.dimensioned:
                try:
                    return f"math.sqrt({codes[0]})", Ty.real(U.dpow(t.dim, 0.5))
                except ValueError:
                    self.d("E201", f"sqrt of {t} gives a fractional dimension", e)
            return f"math.sqrt({codes[0]})", Ty.REAL
        if n in BUILTIN_DIMLESS:
            if tys and tys[0].dimensioned:
                self.d("E201", f"{n}() needs a dimensionless argument, got {tys[0]}", e)
            return f"{BUILTIN_DIMLESS[n]}({codes[0]})", Ty.REAL
        if n == "abs":
            return f"abs({codes[0]})", tys[0]
        if n in ("min", "max"):
            for t in tys[1:]:
                self.same_dims(tys[0], t, e, n)
            return f"{n}({', '.join(codes)})", tys[0] if tys else Ty.ANY
        if n == "len":
            return f"len({codes[0]})", Ty.INT
        if n == "sum":
            t = tys[0].args[0] if tys and tys[0].args else Ty.ANY
            return f"sum({codes[0]})", t
        if n == "sorted":   # predicate in Rose; sort() returns the sorted list
            return f"_is_sorted({codes[0]})", Ty.BOOL
        if n == "sort":
            return f"sorted({codes[0]})", tys[0]
        if n in ("all", "any"):
            if len(codes) == 2:
                return f"{n}({codes[1]}(x) for x in {codes[0]})", Ty.BOOL
            return f"{n}({codes[0]})", Ty.BOOL
        if n == "range":
            return f"list(range({', '.join(codes)}))", Ty.list_of(Ty.INT)
        if n in ("floor", "ceil"):
            return f"math.{n}({codes[0]})", Ty.INT
        if n == "round":
            return f"round({', '.join(codes)})", Ty.REAL if len(codes) > 1 else Ty.INT
        self.d("E206", f"unknown function '{n}'", e)
        return f"{n}({', '.join(codes)})", Ty.ANY

    # ---- type helpers ----
    def expect_bool(self, t, node, where):
        if t.base not in ("Bool", "Any"):
            self.d("E205", f"{where} needs Bool, got {t}", node)

    def unit_mismatch(self, ta, tb, node, op):
        self.d("E201", f"cannot combine {ta} and {tb} with '{op}'", node)

    def same_dims(self, ta, tb, node, op):
        if ta.base == "Any" or tb.base == "Any":
            return
        if ta.numeric and tb.numeric:
            if ta.dimensioned != tb.dimensioned:
                bare = node.right if isinstance(node, BinOp) and not tb.dimensioned else \
                       (node.left if isinstance(node, BinOp) else node)
                if is_zero(bare):
                    return
                want = ta if ta.dimensioned else tb
                self.d("E202", f"number without unit where {want} is expected (operator '{op}')", bare,
                       [{"with": f"<value> {unit_hint(want)}"}])
            elif ta.dim != tb.dim or ta.absolute != tb.absolute:
                if not (ta.absolute or tb.absolute) or ta.dim != tb.dim:
                    self.unit_mismatch(ta, tb, node, op)
            return
        if ta.base != tb.base and not (ta.base == "Enum" and tb.base == "Enum"):
            self.d("E205", f"cannot compare {ta} with {tb}", node)

    def assignable(self, want, got, node, what):
        if want.base == "Any" or got.base == "Any":
            return
        if want.dimensioned and got.numeric and not got.dimensioned:
            if not is_zero(node):
                self.d("E202", f"{what}: number without unit, expected {want}", node,
                       [{"with": f"<value> {unit_hint(want)}"}])
            return
        if not Ty.compatible(want, got):
            code = "E201" if want.numeric and got.numeric else "E205"
            self.d(code, f"{what}: expected {want}, got {got}", node)

    # ---- output ----
    def render(self, mod: Module):
        parts = [f"# generated by rosec {VERSION} from {mod.file} (module {mod.name}) - do not edit",
                 "# runtime values are SI floats; absolute temperatures are in kelvin", PRELUDE]
        if self.helpers:
            parts.append("\n\n".join(self.helpers))
        parts += self.out
        tl = ["def _rose_tests():", "    results = []"]
        for line, cond, shown, src in self.tests:
            tl.append("    try:")
            tl.append(f"        results.append(({line}, bool({cond}), {src!r}, repr({shown})))")
            tl.append("    except Exception as ex:")
            tl.append(f"        results.append(({line}, False, {src!r}, repr(ex)))")
        tl.append("    return results")
        parts.append("\n".join(tl))
        parts.append('''if __name__ == "__main__":
    import sys
    res = _rose_tests()
    for line, ok, src, detail in res:
        print(("ok  " if ok else "FAIL") + f" line {line}: {src}" + ("" if ok else f"   got {detail}"))
    print(f"{sum(r[1] for r in res)}/{len(res)} tests passed")
    sys.exit(0 if all(r[1] for r in res) else 1)''')
        return "\n\n\n".join(parts) + "\n"


# ---- free helpers ----
def pyop(op):
    return {"^": "**", "mod": "%"}.get(op, op)


def is_zero(node):
    return isinstance(node, Num) and float(node.text) == 0.0


def unit_hint(t):
    return "degC" if t.absolute else U.dim_str(t.dim)


def const_number(e):
    if isinstance(e, Num):
        return float(e.text) if not e.is_int else int(e.text)
    if isinstance(e, Unary) and e.op == "-":
        v = const_number(e.expr)
        return -v if v is not None else None
    if isinstance(e, BinOp) and e.op == "/":
        a, b = const_number(e.left), const_number(e.right)
        if a is not None and b:
            from fractions import Fraction
            return Fraction(a) / Fraction(b)
    return None


def const_value(e):
    """SI value of a constant cell expression (number or quantity)."""
    if isinstance(e, Num):
        return float(e.text)
    if isinstance(e, Quantity):
        return U.to_si(float(e.value), U.parse_unit(e.unit))
    if isinstance(e, Unary) and e.op == "-":
        v = const_value(e.expr)
        return None if v is None else -v
    return None


def eval_cond(cond, scope):
    return bool(eval(cond, {"__builtins__": {}}, dict(scope)))  # cond is generated code over literals


def fmt_point(v, t):
    if isinstance(v, float) and t.dimensioned:
        return f"{v:g} (SI)"
    return repr(v)


def ends_with_return(stmts):
    return bool(stmts) and isinstance(stmts[-1], Return)


def src_of(e):
    if isinstance(e, BinOp):
        return f"{src_of(e.left)} {e.op} {src_of(e.right)}"
    if isinstance(e, Num):
        return e.text
    if isinstance(e, Quantity):
        return f"{e.value} {e.unit}"
    if isinstance(e, Name):
        return e.text
    if isinstance(e, Call):
        return f"{src_of(e.func)}(" + ", ".join((k + " = " if k else "") + src_of(x) for k, x in e.args) + ")"
    if isinstance(e, ListLit):
        return "[" + ", ".join(src_of(x) for x in e.items) + "]"
    if isinstance(e, Attr):
        return f"{src_of(e.obj)}.{e.name}"
    if isinstance(e, Str):
        return repr(e.value)
    if isinstance(e, Unary):
        return f"{e.op}{' ' if e.op == 'not' else ''}{src_of(e.expr)}"
    return type(e).__name__


def to_sympy(e, syms):
    import sympy as sp
    if isinstance(e, Num):
        return sp.Integer(int(e.text)) if e.is_int else sp.Float(e.text)
    if isinstance(e, Quantity):
        return sp.Float(U.to_si(float(e.value), U.parse_unit(e.unit)))
    if isinstance(e, Name):
        if e.text in syms:
            return syms[e.text]
        if e.text == "pi":
            return sp.pi
        raise RoseError("E206", f"unknown symbol '{e.text}' in law")
    if isinstance(e, Unary):
        return -to_sympy(e.expr, syms)
    if isinstance(e, BinOp):
        a, b = to_sympy(e.left, syms), to_sympy(e.right, syms)
        return {"+": lambda: a + b, "-": lambda: a - b, "*": lambda: a * b, "/": lambda: a / b,
                "^": lambda: a ** b}[e.op]()
    if isinstance(e, Call) and isinstance(e.func, Name):
        f = {"sqrt": sp.sqrt, "exp": sp.exp, "ln": sp.log, "log10": lambda x: sp.log(x, 10), "sin": sp.sin,
             "cos": sp.cos, "tan": sp.tan, "abs": sp.Abs, "sinh": sp.sinh, "cosh": sp.cosh, "tanh": sp.tanh,
             "asin": sp.asin, "acos": sp.acos, "atan": sp.atan}.get(e.func.text)
        if f:
            return f(*[to_sympy(x, syms) for _, x in e.args])
    raise RoseError("E207", f"cannot use {type(e).__name__} in a law equation")


def compile_source(src, file="<src>", corpus=None):
    """Returns (python_code or None, diagnostics, lock)."""
    try:
        mod = parse(src, file)
    except RoseError as e:
        return None, [e.diag], []
    c = Compiler(corpus, file)
    try:
        code = c.compile_module(mod)
    except RoseError as e:
        c.diags.append(e.diag)
        code = None
    return (code if not c.errors else None), c.diags, c.lock
