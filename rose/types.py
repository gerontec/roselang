"""Static types of Rose v1."""
from dataclasses import dataclass, field

from . import units as U


@dataclass(frozen=True)
class Ty:
    base: str                    # Int Real Bool Text List Enum Range Fn Any Unit(=corpus unit object)
    dim: tuple = U.NONE          # Real only
    absolute: bool = False       # Real absolute temperature (degC scale)
    args: tuple = ()
    members: tuple = ()

    def __str__(self):
        if self.base == "Real":
            if self.dim == U.NONE and not self.absolute:
                return "Real"
            return f"Real[{'degC' if self.absolute else U.dim_str(self.dim)}]"
        if self.base in ("List", "Range") and self.args:
            return f"{self.base}[{self.args[0]}]"
        if self.base == "Enum":
            return "{" + ", ".join(self.members) + "}"
        return self.base

    @property
    def numeric(self):
        return self.base in ("Int", "Real")

    @property
    def dimensioned(self):
        return self.base == "Real" and (self.dim != U.NONE or self.absolute)


INT, REAL, BOOL, TEXT, ANY = Ty("Int"), Ty("Real"), Ty("Bool"), Ty("Text"), Ty("Any")


def real(dim=U.NONE, absolute=False):
    return Ty("Real", dim, absolute)


def list_of(t):
    return Ty("List", args=(t,))


def from_unit_text(text):
    u = U.parse_unit(text)
    return real(u.dim, u.absolute)


def compatible(expected: Ty, got: Ty) -> bool:
    if expected.base == "Any" or got.base == "Any":
        return True
    if expected.base == "Real" and got.base == "Int":
        return not expected.dimensioned
    if expected.base != got.base:
        return False
    if expected.base == "Real":
        return expected.dim == got.dim and expected.absolute == got.absolute
    if expected.base in ("List", "Range"):
        return not expected.args or not got.args or compatible(expected.args[0], got.args[0])
    if expected.base == "Enum":
        return set(got.members) <= set(expected.members)
    return True
