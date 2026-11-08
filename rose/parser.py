"""Recursive-descent parser for Rose v1 (see spec/grammar.ebnf)."""
from . import units as U
from .diag import RoseError
from .lexer import tokenize
from .nodes import *  # noqa: F401,F403

SCHEMES = {"rc", "oeis", "math", "law", "const", "model", "ctrl", "machine", "table", "bio", "wikidata",
           "local", "open", "codata"}
CMP = {"==", "!=", "<", "<=", ">", ">="}
UNSUPPORTED_V1 = {"machine", "ctrl", "model"}


class Parser:
    def __init__(self, src, file="<src>"):
        self.t = tokenize(src, file)
        self.i = 0
        self.file = file

    # ---- token helpers ----
    @property
    def cur(self):
        return self.t[self.i]

    def peek(self, k=1):
        return self.t[min(self.i + k, len(self.t) - 1)]

    def pos(self, tok=None):
        tok = tok or self.cur
        return Pos(tok.line, tok.col)

    def err(self, msg, tok=None, code="E101", fix=None):
        tok = tok or self.cur
        return RoseError(code, msg, self.file, tok.line, tok.col, fix)

    def at(self, text, kind=None):
        c = self.cur
        return c.text == text and (kind is None or c.kind == kind) and c.kind in ("kw", "op", kind or "kw")

    def is_(self, text):
        return self.cur.kind in ("kw", "op") and self.cur.text == text

    def accept(self, text):
        if self.is_(text):
            self.i += 1
            return True
        return False

    def expect(self, text):
        if not self.is_(text):
            got = self.cur.text or "end of file"
            raise self.err(f"expected '{text}', got '{got}'")
        tok = self.cur
        self.i += 1
        return tok

    def ident(self, what="name"):
        if self.cur.kind != "ident":
            raise self.err(f"expected {what}, got '{self.cur.text or 'end of file'}'")
        tok = self.cur
        self.i += 1
        return tok.text

    def qname(self):
        parts = [self.ident()]
        while self.is_(".") and self.peek().kind == "ident":
            self.i += 1
            parts.append(self.ident())
        return ".".join(parts)

    # ---- module ----
    def module(self):
        self.expect("module")
        name = self.qname()
        targets, uses, items = [], [], []
        while not self.cur.kind == "eof":
            if self.accept("target"):
                targets.append(self.ident("target"))
                while self.accept(","):
                    targets.append(self.ident("target"))
            elif self.is_("use"):
                uses.append(self.use())
            elif self.is_("fn"):
                items.append(self.fn())
            elif self.is_("const"):
                items.append(self.const())
            elif self.is_("law"):
                items.append(self.law())
            elif self.is_("table"):
                items.append(self.table())
            elif self.is_("test"):
                items.append(self.test())
            elif self.cur.text in UNSUPPORTED_V1 and self.cur.kind == "kw":
                items.append(self.skip_block())
            else:
                raise self.err(f"unexpected '{self.cur.text}' at top level "
                               "(expected use, fn, const, law, table, test, machine, ctrl, model)")
        return Module(name, targets, uses, items, self.file)

    def skip_block(self):
        """machine/ctrl/model are parsed in v2; v1 skips to the 'end' in the same column."""
        tok = self.cur
        self.i += 1
        name = self.cur.text
        while self.cur.kind != "eof" and not (self.cur.text == "end" and self.cur.col == tok.col):
            self.i += 1
        if self.cur.kind == "eof":
            raise self.err(f"'{tok.text} {name}' has no matching 'end' in column {tok.col}", tok)
        self.i += 1
        return Unsupported(tok.text, name, self.pos(tok))

    def ref_name(self):
        if self.cur.kind == "str":
            s = self.cur.text
            self.i += 1
            return s.replace(" ", "_")
        parts = [self.cur.text]
        if self.cur.kind not in ("ident", "kw", "num"):
            raise self.err("expected reference name")
        self.i += 1
        while self.is_(".") and self.peek().kind in ("ident", "kw", "num"):
            self.i += 1
            parts.append(self.cur.text)
            self.i += 1
        return ".".join(parts)

    def use(self):
        p = self.pos()
        self.expect("use")
        scheme = self.cur.text
        if self.cur.kind not in ("ident", "kw"):
            raise self.err("expected scheme, e.g. law:, oeis:, rc:")
        self.i += 1
        self.expect(":")
        name = self.ref_name()
        version = None
        if self.accept("@"):
            version = self.ref_name()
        alias = self.ident("alias") if self.accept("as") else None
        if scheme not in SCHEMES:
            raise RoseError("E301", f"unknown scheme '{scheme}'", self.file, p.line, p.col,
                            [{"why": "known schemes", "with": sorted(SCHEMES)}])
        return Use(scheme, name, alias, version, p)

    # ---- types ----
    def type(self):
        p = self.pos()
        if self.is_("{"):
            self.i += 1
            members = [self.ident("enum member")]
            while self.accept(","):
                members.append(self.ident("enum member"))
            self.expect("}")
            return TypeRef("Enum", members=members, pos=p)
        base = self.qname()
        t = TypeRef(base, pos=p)
        if self.is_("["):
            open_tok = self.cur
            self.i += 1
            if base == "Real":
                t.unit = self.unit_text_until("]")
            else:
                t.args.append(self.type())
                while self.accept(","):
                    t.args.append(self.type())
                self.expect("]")
            del open_tok
        if self.is_("{"):
            self.i += 1
            if self.cur.text in CMP:
                op = self.cur.text
                self.i += 1
                t.refine = ("cmp", op, self.expr())
            else:
                lo = self.or_expr()
                self.expect("..")
                t.refine = ("range", lo, self.or_expr())
            self.expect("}")
        return t

    def unit_text_until(self, closer):
        depth, parts, start = 0, [], self.cur
        while not (self.cur.text == closer and depth == 0):
            if self.cur.kind == "eof":
                raise self.err(f"unterminated unit, expected '{closer}'", start)
            if self.cur.text == "(":
                depth += 1
            elif self.cur.text == ")":
                depth -= 1
            parts.append(self.cur.text)
            self.i += 1
        self.i += 1
        text = "".join(parts) or "1"
        self.check_unit(text, start)
        return text

    def check_unit(self, text, tok):
        try:
            U.parse_unit(text)
        except ValueError as e:
            raise self.err(str(e), tok, "E208")

    def unit_after_number(self):
        """Collect a unit following a number literal: 9 kW, 0.43 kg/s, 4182 J/(kg*K), 20 %."""
        start, parts, i = self.cur, [], self.i

        def atom_at(j):
            tk = self.t[j]
            if tk.kind == "ident" and U.is_unit_name(tk.text):
                return j + 1
            if tk.kind == "op" and tk.text == "%":
                return j + 1
            if tk.kind == "op" and tk.text == "(":
                k, depth = j, 0
                while True:
                    if self.t[k].kind == "eof":
                        return None
                    if self.t[k].text == "(":
                        depth += 1
                    elif self.t[k].text == ")":
                        depth -= 1
                        if depth == 0:
                            break
                    elif not (self.t[k].kind == "ident" and U.is_unit_name(self.t[k].text)) and \
                            self.t[k].text not in "*/^-%" and self.t[k].kind != "num":
                        return None
                    k += 1
                return k + 1
            return None

        j = atom_at(i)
        if j is None:
            return None
        while True:
            if self.t[j].text == "^" and self.t[j].kind == "op":
                k = j + 1
                if self.t[k].text == "-":
                    k += 1
                if self.t[k].kind == "num":
                    j = k + 1
            if self.t[j].kind == "op" and self.t[j].text in ("*", "/"):
                k = atom_at(j + 1)
                if k is not None:
                    j = k
                    continue
            break
        parts = [self.t[k].text for k in range(i, j)]
        self.i = j
        text = "".join(parts)
        self.check_unit(text, start)
        return text

    # ---- items ----
    def params(self):
        ps = []
        self.expect("(")
        if not self.is_(")"):
            while True:
                p = self.pos()
                name = self.ident("parameter")
                self.expect(":")
                ps.append(Param(name, self.type(), p))
                if not self.accept(","):
                    break
        self.expect(")")
        return ps

    def fn(self):
        p = self.pos()
        self.expect("fn")
        name = self.ident("function name")
        params = self.params()
        self.expect("->")
        ret = self.type()
        intent, req, ens, eff, cost = None, [], [], [], None
        while True:
            if self.accept("intent"):
                if self.cur.kind != "str":
                    raise self.err("intent needs a string")
                intent = self.cur.text
                self.i += 1
            elif self.accept("require"):
                req.append(self.expr())
            elif self.accept("ensure"):
                ens.append(self.expr())
            elif self.accept("effect"):
                eff.append(self.ident("effect"))
                while self.accept(","):
                    eff.append(self.ident("effect"))
            elif self.accept("cost"):
                tok = self.cur
                buf, depth = [], 0
                while True:
                    buf.append(self.cur.text)
                    if self.cur.text == "(":
                        depth += 1
                    elif self.cur.text == ")":
                        depth -= 1
                        if depth == 0:
                            self.i += 1
                            break
                    if self.cur.kind == "eof":
                        raise self.err("unterminated cost", tok)
                    self.i += 1
                cost = " ".join(buf).replace("( ", "(").replace(" )", ")")
            else:
                break
        if intent is None:
            raise self.err(f"fn '{name}' needs an intent \"...\" (the intent is the search key)", code="E101",
                           fix=[{"insert": 'intent "<what this function does>"', "why": "principle P4"}])
        if self.accept("="):
            body = self.expr()
        else:
            self.expect("do")
            body = self.block()
            self.expect("end")
        return Fn(name, params, ret, intent, req, ens, eff, cost, body, p)

    def const(self):
        p = self.pos()
        self.expect("const")
        name = self.ident()
        self.expect(":")
        t = self.type()
        self.expect("=")
        return Const(name, t, self.expr(), p)

    def law(self):
        p = self.pos()
        self.expect("law")
        name = self.ident("law name")
        self.expect("intent")
        intent = self.cur.text
        self.i += 1
        vars_, eqs, valid, refs = [], [], [], []
        while not self.is_("end"):
            if self.accept("var"):
                vp = self.pos()
                vn = self.ident("variable")
                self.expect(":")
                vt = self.type()
                default = self.expr() if self.accept("=") else None
                vars_.append(LawVar(vn, vt, default, vp))
            elif self.accept("eq"):
                lhs = self.or_expr()
                self.expect("=")
                eqs.append((lhs, self.or_expr()))
            elif self.accept("valid"):
                vn = self.ident()
                self.expect("in")
                lo = self.or_expr()
                self.expect("..")
                valid.append((vn, lo, self.or_expr()))
            elif self.accept("ref"):
                scheme = self.cur.text
                self.i += 1
                self.expect(":")
                refs.append(f"{scheme}:{self.ref_name()}")
            else:
                raise self.err(f"unexpected '{self.cur.text}' in law (expected var, eq, valid, ref, end)")
        self.expect("end")
        if not eqs:
            raise self.err(f"law '{name}' has no eq", code="E101")
        return Law(name, intent, vars_, eqs, valid, refs, p)

    def table(self):
        p = self.pos()
        self.expect("table")
        name = self.ident()
        self.expect("intent")
        intent = self.cur.text
        self.i += 1
        self.expect("hit")
        hit = self.ident("hit policy") if self.cur.kind == "ident" else self.cur.text
        if self.cur.kind != "ident":
            self.i += 1
        ins, outs, rules, checks = [], [], [], []
        while not self.is_("end"):
            if self.is_("in") or self.is_("out"):
                which = ins if self.cur.text == "in" else outs
                self.i += 1
                while True:
                    pp = self.pos()
                    n = self.ident()
                    self.expect(":")
                    which.append(Param(n, self.type(), pp))
                    if not self.accept(","):
                        break
            elif self.is_("rule"):
                rp = self.pos()
                self.i += 1
                cells = [self.cell()]
                while self.accept(","):
                    cells.append(self.cell())
                self.expect("->")
                res = [self.or_expr()]
                while self.accept(","):
                    res.append(self.or_expr())
                rules.append((cells, res, rp))
            elif self.accept("check"):
                checks.append(self.ident())
                while self.accept(","):
                    checks.append(self.ident())
            else:
                raise self.err(f"unexpected '{self.cur.text}' in table")
        self.expect("end")
        return Table(name, intent, hit, ins, outs, rules, checks, p)

    def cell(self):
        if self.accept("-"):
            return ("any",)
        if self.cur.text in CMP and self.cur.kind == "op":
            op = self.cur.text
            self.i += 1
            return ("cmp", op, self.add_expr())
        e = self.add_expr()
        if self.accept(".."):
            return ("range", e, self.add_expr())
        return ("eq", e)

    def test(self):
        p = self.pos()
        self.expect("test")
        e = self.expr()
        within = self.expr() if self.accept("within") else None
        return Test(e, within, p)

    # ---- statements ----
    def block(self):
        stmts = []
        while not (self.is_("end") or self.is_("elif") or self.is_("else")):
            if self.cur.kind == "eof":
                raise self.err("missing 'end'")
            stmts.append(self.stmt())
        return stmts

    def stmt(self):
        p = self.pos()
        if self.accept("let"):
            n = self.ident()
            t = self.type() if self.accept(":") else None
            self.expect("=")
            return Let(n, t, self.expr(), p)
        if self.accept("return"):
            return Return(self.expr(), p)
        if self.accept("if"):
            branches = [(self.expr(), None)]
            self.expect("do")
            branches[0] = (branches[0][0], self.block())
            orelse = []
            while True:
                if self.accept("elif"):
                    c = self.expr()
                    self.expect("do")
                    branches.append((c, self.block()))
                elif self.accept("else"):
                    orelse = self.block()
                else:
                    break
            self.expect("end")
            return If(branches, orelse, p)
        if self.accept("for"):
            v = self.ident()
            self.expect("in")
            it = self.expr()
            self.expect("do")
            body = self.block()
            self.expect("end")
            return For(v, it, body, p)
        if self.accept("while"):
            c = self.expr()
            self.expect("do")
            body = self.block()
            self.expect("end")
            return While(c, body, p)
        if self.cur.kind == "ident" and self.peek().text == "=" and self.peek().kind == "op":
            n = self.ident()
            self.expect("=")
            return Assign(n, self.expr(), p)
        return ExprStmt(self.expr(), p)

    # ---- expressions ----
    def expr(self):
        if self.is_("solve"):
            return self.solve()
        e = self.or_expr()
        if self.is_(".."):
            p = self.pos()
            self.i += 1
            return Range(e, self.or_expr(), p)
        return e

    def solve(self):
        p = self.pos()
        self.expect("solve")
        law = self.qname()
        self.expect("for")
        unknown = self.ident("unknown")
        givens = []
        if self.accept("given"):
            while True:
                n = self.ident("given variable")
                self.expect("=")
                givens.append((n, self.or_expr()))
                if not self.accept(","):
                    break
        return Solve(law, unknown, givens, p)

    def or_expr(self):
        e = self.and_expr()
        while self.is_("or"):
            p = self.pos(); self.i += 1
            e = BinOp("or", e, self.and_expr(), p)
        return e

    def and_expr(self):
        e = self.not_expr()
        while self.is_("and"):
            p = self.pos(); self.i += 1
            e = BinOp("and", e, self.not_expr(), p)
        return e

    def not_expr(self):
        if self.is_("not"):
            p = self.pos(); self.i += 1
            return Unary("not", self.not_expr(), p)
        return self.cmp_expr()

    def cmp_expr(self):
        e = self.add_expr()
        if self.cur.kind == "op" and self.cur.text in CMP:
            p = self.pos()
            op = self.cur.text
            self.i += 1
            e = BinOp(op, e, self.add_expr(), p)
        return e

    def add_expr(self):
        e = self.mul_expr()
        while self.cur.kind == "op" and self.cur.text in ("+", "-"):
            p = self.pos(); op = self.cur.text; self.i += 1
            e = BinOp(op, e, self.mul_expr(), p)
        return e

    def mul_expr(self):
        e = self.pow_expr()
        while (self.cur.kind == "op" and self.cur.text in ("*", "/")) or self.is_("mod"):
            p = self.pos(); op = self.cur.text; self.i += 1
            e = BinOp(op, e, self.pow_expr(), p)
        return e

    def pow_expr(self):
        e = self.unary()
        if self.is_("^"):
            p = self.pos(); self.i += 1
            e = BinOp("^", e, self.unary(), p)
        return e

    def unary(self):
        if self.is_("-"):
            p = self.pos(); self.i += 1
            return Unary("-", self.unary(), p)
        return self.postfix(self.primary())

    def postfix(self, e):
        while True:
            if self.is_("("):
                e = self.call(e)
            elif self.is_(".") and self.peek().kind == "ident":
                p = self.pos(); self.i += 1
                e = Attr(e, self.ident(), p)
            else:
                return e

    def call(self, func):
        p = self.pos()
        self.expect("(")
        args = []
        if not self.is_(")"):
            while True:
                if self.cur.kind == "ident" and self.peek().text == "=" and self.peek().kind == "op":
                    k = self.ident(); self.expect("=")
                    args.append((k, self.expr()))
                else:
                    args.append((None, self.expr()))
                if not self.accept(","):
                    break
        self.expect(")")
        return Call(func, args, p)

    def primary(self):
        tok = self.cur
        p = self.pos()
        if tok.kind == "num":
            self.i += 1
            unit = self.unit_after_number()
            return Quantity(tok.text, unit, p) if unit else Num(tok.text, p)
        if tok.kind == "str":
            self.i += 1
            return Str(tok.text, p)
        if self.is_("true") or self.is_("false"):
            self.i += 1
            return Bool(tok.text == "true", p)
        if self.is_("("):
            self.i += 1
            e = self.expr()
            self.expect(")")
            return e
        if self.is_("["):
            self.i += 1
            items = []
            if not self.is_("]"):
                items.append(self.expr())
                while self.accept(","):
                    items.append(self.expr())
            self.expect("]")
            return ListLit(items, p)
        if tok.kind == "ident" or (tok.kind == "kw" and tok.text in ("const", "law", "table")):
            if tok.text in SCHEMES and self.peek().text == ":" and self.peek().kind == "op":
                self.i += 2
                return Ref(tok.text, self.ref_name(), p)
            self.i += 1
            return Name([tok.text], p)
        raise self.err(f"unexpected '{tok.text or 'end of file'}' in expression")


def parse(src: str, file: str = "<src>") -> Module:
    return Parser(src, file).module()
