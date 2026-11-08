"""Diagnostics: every message has a code, a location and optionally a fix (JSON-serialisable)."""
from dataclasses import asdict, dataclass, field

NAMES = {
    "E101": "syntax", "E199": "not-in-v1",
    "E201": "unit-mismatch", "E202": "missing-unit", "E203": "affine-temperature", "E204": "law-dimension",
    "E205": "type-mismatch", "E206": "unknown-name", "E207": "solve-failed", "E208": "bad-unit",
    "E301": "unknown-ref", "E302": "no-impl-for-target", "E303": "license-excluded", "E304": "self-reference",
    "E305": "open-problem", "E306": "ref-not-usable",
    "E410": "ctrl-without-sample-time", "E411": "unbounded-output",
    "E501": "nondeterministic", "E502": "unreachable-state", "E503": "deadlock",
    "E511": "table-incomplete", "E512": "table-overlap",
    "E601": "remote-blast", "E602": "unfiltered-nr-search", "E603": "charset-join",
    "R201": "known-solution", "R202": "lower-level-chosen", "R203": "local-data-available",
    "R204": "masked-residues", "R205": "share-alike-source", "R206": "corpus-offline",
}


@dataclass
class Diag:
    code: str
    message: str
    file: str = "<src>"
    line: int = 0
    col: int = 0
    fix: list = field(default_factory=list)

    @property
    def severity(self):
        return "error" if self.code.startswith("E") else "hint"

    def to_json(self):
        d = asdict(self)
        loc = {"file": d.pop("file"), "line": d.pop("line"), "col": d.pop("col")}
        return {"code": self.code, "name": NAMES.get(self.code, ""), "severity": self.severity,
                "at": loc, **{k: v for k, v in d.items() if k not in ("code",)}}

    def __str__(self):
        return f"{self.file}:{self.line}:{self.col}: {self.code} {NAMES.get(self.code, '')}: {self.message}"


class RoseError(Exception):
    def __init__(self, code, message, file="<src>", line=0, col=0, fix=None):
        super().__init__(message)
        self.diag = Diag(code, message, file, line, col, fix or [])
