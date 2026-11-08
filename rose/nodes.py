"""Syntax tree of Rose v1."""
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class Pos:
    line: int = 0
    col: int = 0


# ---- types ----
@dataclass
class TypeRef:
    base: str                       # Int, Real, Bool, Text, List, Map, Opt, Enum, or a qualified opaque name
    unit: Optional[str] = None      # Real[<unit>]
    args: list = field(default_factory=list)
    refine: Any = None              # ("cmp", op, expr) | ("range", lo, hi)
    members: list = field(default_factory=list)  # Enum
    pos: Pos = field(default_factory=Pos)


# ---- expressions ----
@dataclass
class Num:
    text: str
    pos: Pos = field(default_factory=Pos)

    @property
    def is_int(self):
        return all(c.isdigit() for c in self.text)


@dataclass
class Quantity:
    value: str
    unit: str
    pos: Pos = field(default_factory=Pos)


@dataclass
class Str:
    value: str
    pos: Pos = field(default_factory=Pos)


@dataclass
class Bool:
    value: bool
    pos: Pos = field(default_factory=Pos)


@dataclass
class Name:
    parts: list
    pos: Pos = field(default_factory=Pos)

    @property
    def text(self):
        return ".".join(self.parts)


@dataclass
class Ref:
    scheme: str
    name: str
    pos: Pos = field(default_factory=Pos)


@dataclass
class Call:
    func: Any
    args: list          # [(keyword or None, expr)]
    pos: Pos = field(default_factory=Pos)


@dataclass
class Attr:
    obj: Any
    name: str
    pos: Pos = field(default_factory=Pos)


@dataclass
class BinOp:
    op: str
    left: Any
    right: Any
    pos: Pos = field(default_factory=Pos)


@dataclass
class Unary:
    op: str
    expr: Any
    pos: Pos = field(default_factory=Pos)


@dataclass
class ListLit:
    items: list
    pos: Pos = field(default_factory=Pos)


@dataclass
class Range:
    lo: Any
    hi: Any
    pos: Pos = field(default_factory=Pos)


@dataclass
class Solve:
    law: str
    unknown: str
    givens: list        # [(name, expr)]
    pos: Pos = field(default_factory=Pos)


# ---- statements ----
@dataclass
class Let:
    name: str
    type: Optional[TypeRef]
    expr: Any
    pos: Pos = field(default_factory=Pos)


@dataclass
class Assign:
    name: str
    expr: Any
    pos: Pos = field(default_factory=Pos)


@dataclass
class If:
    branches: list      # [(cond, body)]
    orelse: list
    pos: Pos = field(default_factory=Pos)


@dataclass
class For:
    var: str
    iter: Any
    body: list
    pos: Pos = field(default_factory=Pos)


@dataclass
class While:
    cond: Any
    body: list
    pos: Pos = field(default_factory=Pos)


@dataclass
class Return:
    expr: Any
    pos: Pos = field(default_factory=Pos)


@dataclass
class ExprStmt:
    expr: Any
    pos: Pos = field(default_factory=Pos)


# ---- items ----
@dataclass
class Use:
    scheme: str
    name: str
    alias: Optional[str]
    version: Optional[str]
    pos: Pos = field(default_factory=Pos)

    @property
    def ref(self):
        return f"{self.scheme}:{self.name}"

    @property
    def local(self):
        return self.alias or self.name.split(".")[-1]


@dataclass
class Param:
    name: str
    type: TypeRef
    pos: Pos = field(default_factory=Pos)


@dataclass
class Fn:
    name: str
    params: list
    ret: TypeRef
    intent: str
    requires: list
    ensures: list
    effects: list
    cost: Optional[str]
    body: Any           # list of statements, or a single expression
    pos: Pos = field(default_factory=Pos)


@dataclass
class Const:
    name: str
    type: TypeRef
    expr: Any
    pos: Pos = field(default_factory=Pos)


@dataclass
class LawVar:
    name: str
    type: TypeRef
    default: Any
    pos: Pos = field(default_factory=Pos)


@dataclass
class Law:
    name: str
    intent: str
    vars: list
    eqs: list           # [(lhs, rhs)]
    valid: list         # [(name, lo, hi)]
    refs: list
    pos: Pos = field(default_factory=Pos)


@dataclass
class Table:
    name: str
    intent: str
    hit: str
    ins: list
    outs: list
    rules: list         # [(cells, outputs, pos)]
    checks: list
    pos: Pos = field(default_factory=Pos)


@dataclass
class Open:
    """Negative knowledge: a problem without known solution. Never usable as a building block."""
    name: str
    intent: str
    refs: list
    pos: Pos = field(default_factory=Pos)


@dataclass
class Test:
    expr: Any
    within: Any
    pos: Pos = field(default_factory=Pos)


@dataclass
class Unsupported:
    kind: str
    name: str
    pos: Pos = field(default_factory=Pos)


@dataclass
class Module:
    name: str
    targets: list
    uses: list
    items: list
    file: str = "<src>"
