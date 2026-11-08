"""Tokenizer for Rose. Newlines carry no meaning; '#' starts a comment."""
from dataclasses import dataclass

from .diag import RoseError

KEYWORDS = {
    "module", "target", "use", "as", "fn", "intent", "require", "ensure", "effect", "cost", "do", "end",
    "let", "if", "elif", "else", "for", "in", "while", "return", "test", "within", "const", "law", "var",
    "eq", "valid", "ref", "solve", "given", "and", "or", "not", "mod", "true", "false",
    "table", "hit", "rule", "check", "out", "machine", "ctrl", "model", "state", "on", "when", "param",
    "timer", "sample", "tune", "open",
}
OPS = ["..", "==", "!=", "<=", ">=", "->", "<", ">", "+", "-", "*", "/", "^", "=", "(", ")", "[", "]",
       "{", "}", ",", ":", ".", "%", "@"]


@dataclass
class Tok:
    kind: str   # ident, kw, num, str, op, eof
    text: str
    line: int
    col: int


def tokenize(src: str, file: str = "<src>") -> list:
    toks, i, line, col = [], 0, 1, 1
    n = len(src)

    def adv(k):
        nonlocal i, line, col
        for _ in range(k):
            if src[i] == "\n":
                line += 1; col = 1
            else:
                col += 1
            i += 1

    while i < n:
        c = src[i]
        if c in " \t\r\n":
            adv(1); continue
        if c == "#":
            while i < n and src[i] != "\n":
                adv(1)
            continue
        if c == '"':
            j = i + 1
            while j < n and src[j] != '"':
                if src[j] == "\n":
                    raise RoseError("E101", "unterminated string", file, line, col)
                j += 1
            if j >= n:
                raise RoseError("E101", "unterminated string", file, line, col)
            toks.append(Tok("str", src[i + 1:j], line, col)); adv(j + 1 - i); continue
        if c.isdigit() or (c == "." and i + 1 < n and src[i + 1].isdigit() and not src[i - 1:i] == "."):
            j = i
            while j < n and (src[j].isdigit() or src[j] == "_"):
                j += 1
            if j < n and src[j] == "." and j + 1 < n and src[j + 1].isdigit():
                j += 1
                while j < n and src[j].isdigit():
                    j += 1
            if j < n and src[j] in "eE" and j + 1 < n and (src[j + 1].isdigit() or src[j + 1] in "+-"):
                k = j + 1
                if src[k] in "+-":
                    k += 1
                if k < n and src[k].isdigit():
                    j = k
                    while j < n and src[j].isdigit():
                        j += 1
            toks.append(Tok("num", src[i:j].replace("_", ""), line, col)); adv(j - i); continue
        if c.isalpha() or c == "_" or c == "µ":
            j = i
            while j < n and (src[j].isalnum() or src[j] in "_µ"):
                j += 1
            w = src[i:j]
            toks.append(Tok("kw" if w in KEYWORDS else "ident", w, line, col)); adv(j - i); continue
        for op in OPS:
            if src.startswith(op, i):
                toks.append(Tok("op", op, line, col)); adv(len(op)); break
        else:
            raise RoseError("E101", f"unexpected character {c!r}", file, line, col)
    toks.append(Tok("eof", "", line, col))
    return toks
