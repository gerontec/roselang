"""Rose. `import rose` gives the Python module (rose/lib.py, benchmark variant B2);
the compiler is `python3 -m rose` / `rosec` (rose/cli.py)."""

_API = {"Q", "law", "use", "table", "plan", "search", "get", "lock", "approx", "RoseError", "UnitError",
        "LawError", "OpenProblem", "UnknownRef", "TableError", "ContractError"}


def __getattr__(name):
    if name not in _API:          # submodules (rose.types, ...) must not trigger the library import
        raise AttributeError(name)
    from . import lib
    return getattr(lib, name)
