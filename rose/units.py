"""Physical units and dimensions for the Rose checker.

A dimension is a 7-tuple of integer exponents over the SI base dimensions
(L, M, T, I, Th, N, J). A unit is (scale to SI, dimension, offset, absolute).
Runtime values are always SI floats; absolute temperatures are stored in kelvin,
so `45 degC` becomes 318.15 and `degC - degC` yields a temperature difference in K.
"""
from dataclasses import dataclass
from fractions import Fraction

BASE = ("L", "M", "T", "I", "Th", "N", "J")
NONE = (0, 0, 0, 0, 0, 0, 0)


def dim(**kw) -> tuple:
    return tuple(int(kw.get(b, 0)) for b in BASE)


def dmul(a, b):
    return tuple(x + y for x, y in zip(a, b))


def ddiv(a, b):
    return tuple(x - y for x, y in zip(a, b))


def dpow(a, n):
    r = tuple(Fraction(x) * Fraction(n) for x in a)
    if any(x.denominator != 1 for x in r):
        raise ValueError("fractional dimension")
    return tuple(int(x) for x in r)


def dim_str(d) -> str:
    """(1,0,-1,...) -> 'L1 T-1'; dimensionless -> '1' (same format as rose_law_var.dim)."""
    s = " ".join(f"{b}{e}" for b, e in zip(BASE, d) if e)
    return s or "1"


def parse_dim_str(s: str):
    if not s or s == "1":
        return NONE if s == "1" else None
    acc = dict.fromkeys(BASE, 0)
    for part in s.split():
        for b in sorted(BASE, key=len, reverse=True):
            if part.startswith(b):
                try:
                    acc[b] += int(part[len(b):])
                except ValueError:
                    return None
                break
        else:
            return None
    return tuple(acc[b] for b in BASE)


@dataclass(frozen=True)
class Unit:
    scale: float
    dim: tuple
    offset: float = 0.0       # only degC/degF
    absolute: bool = False    # affine absolute temperature scale

    def __mul__(self, o):
        return Unit(self.scale * o.scale, dmul(self.dim, o.dim))

    def __truediv__(self, o):
        return Unit(self.scale / o.scale, ddiv(self.dim, o.dim))

    def __pow__(self, n):
        return Unit(self.scale ** n, dpow(self.dim, n))


L, M, T, I, TH, N, J = (dim(**{b: 1}) for b in BASE)

_U = {
    "1": Unit(1, NONE), "%": Unit(0.01, NONE), "ppm": Unit(1e-6, NONE),
    "rad": Unit(1, NONE), "sr": Unit(1, NONE),
    "m": Unit(1, L), "g": Unit(1e-3, M), "s": Unit(1, T), "A": Unit(1, I), "K": Unit(1, TH),
    "mol": Unit(1, N), "cd": Unit(1, J),
    "min": Unit(60, T), "h": Unit(3600, T), "d": Unit(86400, T),
    "Hz": Unit(1, dim(T=-1)), "N": Unit(1, dim(L=1, M=1, T=-2)), "Pa": Unit(1, dim(L=-1, M=1, T=-2)),
    "bar": Unit(1e5, dim(L=-1, M=1, T=-2)), "J": Unit(1, dim(L=2, M=1, T=-2)),
    "Wh": Unit(3600, dim(L=2, M=1, T=-2)), "eV": Unit(1.602176634e-19, dim(L=2, M=1, T=-2)),
    "W": Unit(1, dim(L=2, M=1, T=-3)), "C": Unit(1, dim(T=1, I=1)),
    "V": Unit(1, dim(L=2, M=1, T=-3, I=-1)), "F": Unit(1, dim(L=-2, M=-1, T=4, I=2)),
    "Ohm": Unit(1, dim(L=2, M=1, T=-3, I=-2)), "ohm": Unit(1, dim(L=2, M=1, T=-3, I=-2)),
    "S": Unit(1, dim(L=-2, M=-1, T=3, I=2)), "Wb": Unit(1, dim(L=2, M=1, T=-2, I=-1)),
    "T": Unit(1, dim(M=1, T=-2, I=-1)), "H": Unit(1, dim(L=2, M=1, T=-2, I=-2)),
    "lm": Unit(1, J), "lx": Unit(1, dim(L=-2, J=1)), "Bq": Unit(1, dim(T=-1)),
    "Gy": Unit(1, dim(L=2, T=-2)), "Sv": Unit(1, dim(L=2, T=-2)), "kat": Unit(1, dim(T=-1, N=1)),
    "L": Unit(1e-3, dim(L=3)), "l": Unit(1e-3, dim(L=3)), "t": Unit(1e3, M),
    "degC": Unit(1, TH, offset=273.15, absolute=True),
    # atomic-scale units used by CODATA (values CODATA 2022; c exact)
    "u": Unit(1.66053906892e-27, M), "Da": Unit(1.66053906892e-27, M),
    "E_h": Unit(4.3597447222060e-18, dim(L=2, M=1, T=-2)),
    "c": Unit(299792458, dim(L=1, T=-1)),
}
PREFIX = {"Y": 1e24, "Z": 1e21, "E": 1e18, "P": 1e15, "T": 1e12, "G": 1e9, "M": 1e6, "k": 1e3, "h": 1e2,
          "da": 1e1, "d": 1e-1, "c": 1e-2, "m": 1e-3, "u": 1e-6, "µ": 1e-6, "n": 1e-9, "p": 1e-12,
          "f": 1e-15, "a": 1e-18}
NO_PREFIX = {"1", "%", "ppm", "degC", "min", "h", "d", "rad", "sr", "t"}


def lookup(name: str):
    """Unit atom by name, with SI prefixes ('kW', 'mm', 'kWh'); None if unknown."""
    if name in _U:
        return _U[name]
    for p in sorted(PREFIX, key=len, reverse=True):
        if name.startswith(p) and name[len(p):] in _U and name[len(p):] not in NO_PREFIX:
            u = _U[name[len(p):]]
            return Unit(u.scale * PREFIX[p], u.dim)
    return None


def is_unit_name(name: str) -> bool:
    return lookup(name) is not None


def parse_unit(text: str) -> Unit:
    """Parse 'J/(kg*K)', 'm*s^-1', 'm s^-1', 'kg/s', '%'. Raises ValueError."""
    toks, i, s = [], 0, text.replace("·", "*").replace("⋅", "*")
    while i < len(s):
        c = s[i]
        if c.isspace():
            i += 1
            if toks and toks[-1] not in "*/(^" and i < len(s) and s[i] not in "*/)^":
                toks.append("*")
            continue
        if c in "*/()^":
            toks.append(c); i += 1; continue
        if c == "-" or c.isdigit():
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            toks.append(s[i:j]); i = j; continue
        j = i
        while j < len(s) and (s[j].isalpha() or s[j] in "%µ" or (s[j] == "_" and j > i)):
            j += 1
        if j == i:
            raise ValueError(f"bad character {c!r} in unit {text!r}")
        toks.append(s[i:j]); i = j
    pos = 0

    def atom():
        nonlocal pos
        t = toks[pos] if pos < len(toks) else None
        if t == "(":
            pos += 1
            u = expr()
            if pos >= len(toks) or toks[pos] != ")":
                raise ValueError(f"missing ')' in unit {text!r}")
            pos += 1
        elif t == "1":
            pos += 1
            u = _U["1"]
        elif t and (t[0].isalpha() or t[0] in "%µ"):
            pos += 1
            u = lookup(t)
            if u is None:
                raise ValueError(f"unknown unit {t!r}")
        else:
            raise ValueError(f"unexpected {t!r} in unit {text!r}")
        if pos < len(toks) and toks[pos] == "^":
            pos += 1
            u = u ** int(toks[pos]); pos += 1
        return u

    def expr():
        nonlocal pos
        u = atom()
        while pos < len(toks) and toks[pos] in "*/":
            op = toks[pos]; pos += 1
            v = atom()
            if u.absolute or v.absolute:
                u, v = (Unit(1, TH) if x.absolute else x for x in (u, v))
            u = u * v if op == "*" else u / v
        return u

    u = expr()
    if pos != len(toks):
        raise ValueError(f"trailing {toks[pos]!r} in unit {text!r}")
    return u


def to_si(value: float, u: Unit) -> float:
    return value * u.scale + u.offset


_NAMED = ["W", "J", "N", "Pa", "V", "C", "F", "Ohm", "S", "Wb", "T", "H", "Hz", "lx"]
_BASE_SYM = ["m", "kg", "s", "A", "K", "mol", "cd"]


def unit_name(d) -> str:
    """Readable SI unit for a dimension: (2,1,-3,0,0,0,0) -> 'W', (0,1,-1,...) -> 'kg/s'."""
    if d == NONE:
        return "1"
    for n in _NAMED:
        if _U[n].dim == d:
            return n
    num = [f"{s}^{e}" if e != 1 else s for s, e in zip(_BASE_SYM, d) if e > 0]
    den = [f"{s}^{-e}" if e != -1 else s for s, e in zip(_BASE_SYM, d) if e < 0]
    top = "*".join(num) or "1"
    if not den:
        return top
    return f"{top}/{den[0]}" if len(den) == 1 else f"{top}/({'*'.join(den)})"
