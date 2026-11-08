"""Translate an imported TeX formula into a Rose `law` (knowledge moves from the corpus into the language).

The symbol table of the source (Wikidata P7235: TeX of each symbol + quantity + dimension) drives the
tokenizer: symbol token sequences are matched longest first, the remaining TeX structure (\\frac,
powers, roots, functions, implicit multiplication) becomes a Rose expression. Formulas with
derivatives, integrals, sums, limits, vectors or relations other than '=' are rejected with a reason.
"""
import re

from . import units as U
from .lexer import KEYWORDS

REJECT = {r"\int": "integral", r"\oint": "integral", r"\sum": "sum", r"\prod": "product", r"\lim": "limit",
          r"\partial": "partial derivative", r"\nabla": "vector operator", r"\mathrm{d}": "derivative",
          r"\operatorname{d}": "derivative", r"\approx": "approximation", r"\propto": "proportionality",
          r"\leq": "inequality", r"\geq": "inequality", r"\le": "inequality", r"\ge": "inequality",
          r"\neq": "inequality", r"\equiv": "congruence", r"\to": "limit/map", r"\rightarrow": "limit/map",
          r"\in": "set relation", r"\langle": "expectation value", r"\vec": "vector", r"\cdots": "series",
          r"\ldots": "series", r"\dots": "series", r"\otimes": "tensor product", r"\times\mathbf": "cross product",
          r"\begin": "matrix/array", r"\mathbf": "vector or matrix", r"\boldsymbol": "vector or matrix",
          r"\dot": "time derivative", r"\ddot": "time derivative", r"\bar": "mean value", r"\hat": "operator",
          r"\binom": "binomial", r"!": "factorial", r"\|": "norm", r"|": "absolute value/norm"}
FUNCS = {r"\sin": "sin", r"\cos": "cos", r"\tan": "tan", r"\exp": "exp", r"\ln": "ln", r"\log": "ln",
         r"\sinh": "sinh", r"\cosh": "cosh", r"\tanh": "tanh", r"\arcsin": "asin", r"\arccos": "acos",
         r"\arctan": "atan"}
DROP = {r"\left", r"\right", r"\,", r"\;", r"\!", r"\:", r"\quad", r"\qquad", r"\displaystyle", r"\textstyle",
        r"\big", r"\Big", r"\bigg", r"\Bigg", "~"}
MULT = {r"\cdot", r"\times", "*", r"\ast"}


class TexError(ValueError):
    pass


def tokens(tex: str):
    out, i = [], 0
    while i < len(tex):
        c = tex[i]
        if c.isspace():
            i += 1
            continue
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", tex[i:])
            out.append("\\" + m.group(1))
            i += len(m.group(0))
            continue
        if c.isdigit() or (c == "." and i + 1 < len(tex) and tex[i + 1].isdigit()):
            m = re.match(r"\d*\.?\d+", tex[i:])
            out.append(m.group(0))
            i += len(m.group(0))
            continue
        out.append(c)
        i += 1
    return out


def norm_symbol_tokens(tex):
    """Symbol TeX as token tuple, with \\mathrm/\\mathit wrappers removed for robust matching."""
    t = [x for x in tokens(tex) if x not in DROP]
    return tuple(t)


def strip_wrappers(toks):
    """\\mathrm{v} -> v, \\text{x} -> x, \\operatorname{...} kept as a name later."""
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        if t in (r"\mathrm", r"\mathit", r"\text", r"\textrm", r"\mathsf", r"\rm", r"\it") and i + 1 < len(toks) and toks[i + 1] == "{":
            depth, j = 0, i + 1
            while j < len(toks):
                depth += toks[j] == "{"
                depth -= toks[j] == "}"
                if depth == 0:
                    break
                j += 1
            inner = toks[i + 2:j]
            if inner == ["d"]:
                raise TexError("derivative")
            out += inner if len(inner) > 1 else inner  # keep letters, they are matched against symbols
            i = j + 1
            continue
        out.append(t)
        i += 1
    return out


def safe_ident(name, used):
    n = re.sub(r"[^A-Za-z0-9_]", "_", name).strip("_") or "x"
    if n[0].isdigit():
        n = "v" + n
    if n in KEYWORDS or n in ("pi", "result", "sqrt", "exp", "ln", "sin", "cos", "tan"):
        n = n + "_"
    base, k = n, 2
    while n in used:
        n = f"{base}{k}"
        k += 1
    return n


class Conv:
    def __init__(self, toks, symtab):
        self.t, self.i, self.sym = toks, 0, symtab   # symtab: list of (token tuple, ident), longest first
        self.used = set()

    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else None

    def take(self):
        t = self.peek()
        self.i += 1
        return t

    def group(self):
        """{...} or a single token/symbol as an operand."""
        if self.peek() == "{":
            self.take()
            e = self.expr(stop="}")
            if self.take() != "}":
                raise TexError("unbalanced braces")
            return e
        return self.atom()

    def match_symbol(self):
        for seq, ident in self.sym:
            n = len(seq)
            if tuple(self.t[self.i:self.i + n]) == seq:
                # avoid matching 'm' inside a longer symbol chain such as m_e when m_e is also a symbol: longest first
                self.i += n
                self.used.add(ident)
                return ident
        return None

    def atom(self):
        s = self.match_symbol()
        if s:
            return s
        t = self.peek()
        if t is None:
            raise TexError("unexpected end of formula")
        if re.fullmatch(r"\d*\.?\d+", t):
            self.take()
            return t
        if t == r"\pi":
            self.take()
            return "pi"
        if t == r"\frac" or t == r"\dfrac" or t == r"\tfrac":
            self.take()
            a = self.group()
            b = self.group()
            return f"{par(a)} / {par(b)}"
        if t == r"\sqrt":
            self.take()
            if self.peek() == "[":
                raise TexError("n-th root")
            return f"sqrt({self.group()})"
        if t in FUNCS:
            self.take()
            if self.peek() == "^":
                raise TexError("power of a function")
            if self.peek() == "{":
                arg = self.group()
            elif self.peek() == "(":
                self.take()
                arg = self.expr(stop=")")
                self.take()
            else:
                arg = self.factor()
            return f"{FUNCS[t]}({arg})"
        if t == "(" or t == "[":
            close = ")" if t == "(" else "]"
            self.take()
            e = self.expr(stop=close)
            if self.take() != close:
                raise TexError("unbalanced parentheses")
            return f"({e})"
        if t == "{":
            return self.group()
        if t == "e" and self.i + 1 < len(self.t) and self.t[self.i + 1] == "^":
            self.take()
            return "exp(1)"
        raise TexError(f"unknown token {t!r} (not in the symbol table)")

    def postfix(self, base):
        while self.peek() == "^":
            self.take()
            exp = self.group()
            base = f"{par(base)} ^ {par(exp)}"
            if base.startswith("exp(1)"):
                base = f"exp({exp})"
        if self.peek() == "_":
            raise TexError("subscript not covered by a symbol")
        return base

    def unary(self):
        if self.peek() == "-":
            self.take()
            return f"-{self.factor()}"
        if self.peek() == "+":
            self.take()
        return self.factor()

    def factor(self):
        return self.postfix(self.atom())

    def term(self, stop):
        parts = [self.unary()]
        while True:
            t = self.peek()
            if t is None or t == stop or t in ("+", "-", "=", "}", ")", "]"):
                break
            if t in MULT:
                self.take()
                parts.append("*")
                parts.append(self.unary())
            elif t == "/":
                self.take()
                parts.append("/")
                parts.append(self.unary())
            else:  # implicit multiplication
                parts.append("*")
                parts.append(self.factor())
        return " ".join(parts)

    def expr(self, stop=None):
        out = self.term(stop)
        while self.peek() in ("+", "-"):
            op = self.take()
            out += f" {op} " + self.term(stop)
        return out


def tex_to_law(name, intent, tex, symbols, ref=None):
    """Returns (rose_src, typed) or raises TexError. typed = every used symbol has a dimension."""
    for k, why in REJECT.items():
        if k in tex:
            raise TexError(why)
    toks = [t for t in tokens(tex.replace(":=", "=")) if t not in DROP]
    while toks and toks[-1] in (".", ",", ";"):
        toks.pop()
    toks = strip_wrappers(toks)
    if toks.count("=") != 1:
        raise TexError("not a single equation" if toks.count("=") == 0 else "chained equation")
    used_idents = set()
    symtab, dims = [], {}
    for s in symbols:
        seq = tuple(strip_wrappers(list(norm_symbol_tokens(s["tex"]))))
        if not seq:
            continue
        ident = safe_ident(s.get("symbol") or "x", used_idents)
        used_idents.add(ident)
        symtab.append((seq, ident))
        dims[ident] = s.get("dim") or ""
    symtab.sort(key=lambda x: -len(x[0]))
    c = Conv(toks, symtab)
    lhs = c.expr(stop="=")
    if c.take() != "=":
        raise TexError("cannot split at '='")
    rhs = c.expr()
    if c.peek() is not None:
        raise TexError(f"unparsed rest {''.join(toks[c.i:c.i + 5])!r}")
    if not c.used:
        raise TexError("no symbol of the symbol table occurs")
    typed = all(dims.get(v) for v in c.used)
    lines = [f"law {name}", f"  intent {intent_str(intent)}"]
    for v in sorted(c.used):
        d = U.parse_dim_str(dims.get(v, "")) if typed else None
        unit = U.unit_name(d) if d is not None else None
        lines.append(f"  var {v}: Real" + (f"[{unit}]" if unit and unit != "1" else ""))
    lines.append(f"  eq  {lhs} = {rhs}")
    if ref:
        lines.append(f"  ref {ref}")
    lines.append("end")
    return "\n".join(lines) + "\n", typed


def par(x):
    """Parenthesise unless x is a single name, number or call."""
    if re.fullmatch(r"-?[A-Za-z_][A-Za-z0-9_]*(\(.*\))?|\d*\.?\d+|\(.*\)", x) and x.count("(") == x.count(")"):
        if not x.startswith("(") or _balanced_outer(x):
            return x
    return f"({x})"


def _balanced_outer(x):
    depth = 0
    for i, c in enumerate(x):
        depth += c == "("
        depth -= c == ")"
        if depth == 0 and i < len(x) - 1:
            return False
    return True


def intent_str(s):
    return '"' + s.replace('"', "'").replace("\n", " ")[:400] + '"'
