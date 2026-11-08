#!/usr/bin/env python3
"""Import solver functions of Python libraries as solver cards (kind algo, refs py:<public path>):
the answer to "is there a solution?" becomes a function that already exists, is tested and maintained.

  networkx  (BSD-3-Clause)  every public function/class of networkx.algorithms.*, by introspection
  scipy     (BSD-3-Clause)  public API (__all__) of the solver subpackages, by introspection
  ortools   (Apache-2.0)    curated entry points (SWIG modules cannot be introspected usefully)
  sympy     (BSD-3-Clause)  curated logic/equation solvers (SOPform, satisfiable, dsolve, ...)
  control   (BSD-3-Clause)  python-control: public top-level API (LTI systems, PID, LQR, Kalman, responses)
  automata  (MIT)           automata-lib: DFA/NFA/GNFA, pushdown automata, Turing machines, regex
  transitions (MIT)         state-machine classes (Machine, HierarchicalMachine, GraphMachine, ...)
  dd        (BSD-3-Clause)  binary/multi-valued decision diagrams (BDD, MDD)
  python    (PSF-2.0)       a few standard-library solvers (bisect, heapq, graphlib, difflib, ...)
Stored per card: public path, signature, first docstring paragraph, library version, docs URL.
Nothing is executed except importing the libraries. On the build host they are installed with
  python3 -m pip install --user --break-system-packages networkx scipy ortools control automata-lib transitions dd
(after checking with dpkg-query that dpkg does not hold the same library; numpy stays the .deb).
Usage: import_pylib.py [--dry-run]
"""
import argparse
import importlib
import inspect
import pkgutil
import re
import sys

import rose_db as R

SCIPY = ["scipy.optimize", "scipy.sparse.csgraph", "scipy.integrate", "scipy.interpolate", "scipy.linalg",
         "scipy.signal", "scipy.spatial", "scipy.cluster.vq", "scipy.cluster.hierarchy", "scipy.fft",
         "scipy.ndimage", "scipy.stats"]
SYMPY = {"sympy.logic.boolalg": ["SOPform", "POSform", "simplify_logic", "to_cnf", "to_dnf", "truth_table"],
         "sympy.logic.inference": ["satisfiable"], "sympy.solvers": ["solve", "nsolve", "dsolve", "linsolve", "nonlinsolve"],
         "sympy.integrals": ["integrate"], "sympy.series": ["series", "limit"]}
STDLIB = {"bisect": ["bisect_left", "bisect_right", "insort"], "heapq": ["heappush", "heappop", "nsmallest", "nlargest", "merge"],
          "graphlib": ["TopologicalSorter"], "difflib": ["SequenceMatcher", "get_close_matches", "unified_diff"],
          "itertools": ["permutations", "combinations", "product"], "statistics": ["median", "linear_regression", "correlation"],
          "math": ["gcd", "lcm", "comb", "perm", "isqrt", "factorial"], "fractions": ["Fraction"], "builtins": ["sorted"]}
ORTOOLS = [  # (public path, kind of problem, docs url)
    ("ortools.constraint_solver.pywrapcp.RoutingModel", "vehicle routing and travelling salesperson problems with capacities, time windows, pickups and deliveries (routing solver)",
     "https://developers.google.com/optimization/routing"),
    ("ortools.sat.python.cp_model.CpModel", "constraint programming and integer optimisation (CP-SAT): scheduling, job shop, assignment, packing, colouring",
     "https://developers.google.com/optimization/cp/cp_solver"),
    ("ortools.linear_solver.pywraplp.Solver", "linear programming and mixed-integer programming (MIP) solver wrapper",
     "https://developers.google.com/optimization/lp"),
    ("ortools.algorithms.python.knapsack_solver.KnapsackSolver", "knapsack problem solver (0-1, multi-dimensional)",
     "https://developers.google.com/optimization/pack/knapsack"),
    ("ortools.graph.python.max_flow.SimpleMaxFlow", "maximum flow in a network with capacities",
     "https://developers.google.com/optimization/flow/maxflow"),
    ("ortools.graph.python.min_cost_flow.SimpleMinCostFlow", "minimum cost flow",
     "https://developers.google.com/optimization/flow/mincostflow"),
    ("ortools.graph.python.linear_sum_assignment.SimpleLinearSumAssignment", "linear assignment problem (min cost one-to-one assignment)",
     "https://developers.google.com/optimization/assignment"),
]
LIBS = {"networkx": ("https://networkx.org", "BSD-3-Clause"), "scipy": ("https://scipy.org", "BSD-3-Clause"),
        "ortools": ("https://developers.google.com/optimization", "Apache-2.0"),
        "python": ("https://docs.python.org/3/library/", "PSF-2.0"), "sympy": ("https://www.sympy.org", "BSD-3-Clause"),
        "control": ("https://python-control.readthedocs.io", "BSD-3-Clause"),
        "automata": ("https://caleb531.github.io/automata/", "MIT"),
        "transitions": ("https://github.com/pytransitions/transitions", "MIT"),
        "dd": ("https://github.com/tulip-control/dd", "BSD-3-Clause")}
# control engineering, automata and decision diagrams: modules whose public classes/functions are pointers
AUTOMATA = ["automata.fa.dfa", "automata.fa.nfa", "automata.fa.gnfa", "automata.pda.dpda", "automata.pda.npda",
            "automata.tm.dtm", "automata.tm.ntm", "automata.tm.mntm", "automata.regex.regex"]
TRANSITIONS = ["transitions.core", "transitions.extensions.nesting", "transitions.extensions.diagrams",
               "transitions.extensions.locking", "transitions.extensions.asyncio", "transitions.extensions.markup"]
DD = ["dd.autoref", "dd.bdd", "dd.mdd"]


def summary(obj):
    doc = inspect.getdoc(obj) or ""
    paras = [p for p in doc.strip().split("\n\n") if p.strip()]
    name = getattr(obj, "__name__", "")
    if len(paras) > 1 and name and re.match(rf"\s*{re.escape(name)}\s*\(", paras[0]):
        paras = paras[1:]                      # python-control: first paragraph is the call signature
    return " ".join(paras[0].split())[:600] if paras else ""


def sig(obj):
    try:
        return str(inspect.signature(obj))[:500]
    except (TypeError, ValueError):
        return None


def is_solver(name, obj):
    if name.startswith("_") or not callable(obj):
        return False
    if inspect.isclass(obj) and issubclass(obj, (BaseException, Warning)):
        return False
    return inspect.isfunction(obj) or inspect.isclass(obj) or type(obj).__name__ in ("ufunc", "builtin_function_or_method",
                                                                         "cython_function_or_method", "fused_cython_function")


def networkx_units():
    import networkx as nx
    seen = {}
    for mi in pkgutil.walk_packages(nx.algorithms.__path__, "networkx.algorithms."):
        if ".tests" in mi.name:
            continue
        try:
            mod = importlib.import_module(mi.name)
        except Exception:
            continue
        for name in getattr(mod, "__all__", []):
            obj = getattr(mod, name, None)
            if obj is None or not is_solver(name, obj) or not getattr(obj, "__module__", "").startswith("networkx"):
                continue
            canon = f"{obj.__module__}.{name}"
            if canon in seen:
                continue
            short = f"networkx.{name}" if getattr(nx, name, None) is obj else canon
            seen[canon] = {"path": canon, "public": short, "obj": obj, "lib": "networkx", "version": nx.__version__,
                           "url": f"https://networkx.org/documentation/stable/reference/generated/{canon}.html"}
    return list(seen.values())


def scipy_units():
    import scipy
    out, seen = [], set()
    for modname in SCIPY:
        mod = importlib.import_module(modname)
        for name in getattr(mod, "__all__", []):
            obj = getattr(mod, name, None)
            if obj is None or not is_solver(name, obj) or id(obj) in seen:
                continue
            if modname == "scipy.stats" and type(obj).__name__.endswith("_gen"):
                continue              # the ~100 distribution objects are not solvers
            seen.add(id(obj))
            path = f"{modname}.{name}"
            out.append({"path": path, "public": path, "obj": obj, "lib": "scipy", "version": scipy.__version__,
                        "url": f"https://docs.scipy.org/doc/scipy/reference/generated/{path}.html"})
    return out


def ortools_units():
    import ortools
    out = []
    for path, what, url in ORTOOLS:
        mod, name = path.rsplit(".", 1)
        try:
            obj = getattr(importlib.import_module(mod), name)
        except Exception as e:
            print(f"  ortools: {path} not importable: {e}", file=sys.stderr)
            continue
        out.append({"path": path, "public": path, "obj": obj, "lib": "ortools", "version": ortools.__version__,
                    "url": url, "what": what})
    return out


def sympy_units():
    import sympy
    out = []
    for mod, names in SYMPY.items():
        m = importlib.import_module(mod)
        for name in names:
            obj = getattr(m, name, None)
            if obj is None:
                continue
            path = f"{mod}.{name}"
            out.append({"path": path, "public": f"sympy.{name}" if getattr(sympy, name, None) is obj else path,
                        "obj": obj, "lib": "sympy", "version": sympy.__version__,
                        "url": f"https://docs.sympy.org/latest/search.html?q={name}"})
    return out


def control_units():
    """python-control: every public callable of the top-level namespace defined inside the package."""
    import control
    out, seen = [], set()
    for name in sorted(dir(control)):
        obj = getattr(control, name)
        if not is_solver(name, obj) or not getattr(obj, "__module__", "").startswith("control") or id(obj) in seen:
            continue
        seen.add(id(obj))
        out.append({"path": f"{obj.__module__}.{name}", "public": f"control.{name}", "obj": obj, "lib": "control",
                    "version": control.__version__,
                    "url": f"https://python-control.readthedocs.io/en/latest/generated/control.{name}.html"})
    return out


def module_units(lib, mods, url, version):
    """Public classes/functions defined in the given modules (no re-exports, no private names)."""
    out, seen = [], set()
    for modname in mods:
        try:
            mod = importlib.import_module(modname)
        except Exception as e:
            print(f"  {lib}: {modname} not importable: {e}", file=sys.stderr)
            continue
        names = getattr(mod, "__all__", None) or dir(mod)
        for name in names:
            obj = getattr(mod, name, None)
            if obj is None or not is_solver(name, obj) or getattr(obj, "__module__", "") != modname or id(obj) in seen:
                continue
            seen.add(id(obj))
            out.append({"path": f"{modname}.{name}", "public": f"{modname}.{name}", "obj": obj, "lib": lib,
                        "version": version, "url": url})
    return out


def automata_units():
    from importlib.metadata import version
    return module_units("automata", AUTOMATA, "https://caleb531.github.io/automata/api/", version("automata-lib"))


def transitions_units():
    import transitions
    return module_units("transitions", TRANSITIONS, "https://github.com/pytransitions/transitions#readme",
                        transitions.__version__)


def dd_units():
    import dd
    from importlib.metadata import version
    return module_units("dd", DD, "https://github.com/tulip-control/dd/blob/main/doc.md", version("dd"))


def stdlib_units():
    out = []
    v = ".".join(map(str, sys.version_info[:3]))
    for mod, names in STDLIB.items():
        m = importlib.import_module(mod)
        for name in names:
            obj = getattr(m, name)
            path = f"{mod}.{name}"
            out.append({"path": path, "public": name if mod == "builtins" else path, "obj": obj, "lib": "python",
                        "version": v, "url": f"https://docs.python.org/3/library/{'functions' if mod == 'builtins' else mod}.html"})
    return out


def words(path):
    last = path.split(".")[-1]
    parts = re.sub(r"([a-z])([A-Z])", r"\1 \2", last).replace("_", " ")
    mods = " ".join(p.replace("_", " ") for p in path.split(".")[1:-1] if p not in ("algorithms", "python"))
    return parts, mods


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    units = (networkx_units() + scipy_units() + ortools_units() + sympy_units() + control_units() + automata_units()
             + transitions_units() + dd_units() + stdlib_units())
    by_lib = {}
    for u in units:
        by_lib[u["lib"]] = by_lib.get(u["lib"], 0) + 1
    print("solvers:", by_lib, flush=True)
    rows = []
    con = cur = None
    sids = {}
    if not a.dry_run:
        con = R.connect()
        cur = con.cursor()
        for lib, (url, lic) in LIBS.items():
            sids[lib] = R.ensure_source(cur, f"py-{lib}", url, lic, False,
                                        f"public solver functions of {lib} (path, signature, first docstring paragraph)")
    for u in units:
        obj = u["obj"]
        doc = u.get("what") or summary(obj)
        name_words, mod_words = words(u["path"])
        s = sig(obj)
        intent = f"{name_words} - {doc}" + (f" [{mod_words}]" if mod_words else "") + f" [call: {u['public']}{s or '()'}]"
        payload = {"path": u["path"], "public": u["public"], "library": u["lib"], "version": u["version"],
                   "signature": s, "doc": doc, "status": "solved", "domain": "computer science",
                   "kind_of_object": "class" if inspect.isclass(obj) else "function"}
        if a.dry_run:
            if u["path"].endswith(("traveling_salesman_problem", "linear_sum_assignment", "RoutingModel", "TopologicalSorter",
                                   "control.pid_designer", ".lqr", "fa.dfa.DFA", "core.Machine", "autoref.BDD")):
                print(u["path"], "|", intent[:220])
            continue
        rows.append(R.unit_row(ref="py:" + u["path"], kind="algo", name=u["public"], intent=intent,
                               source_id=sids[u["lib"]], source_url=u["url"], signature=s, payload=payload,
                               level="tested"))
    if rows:
        for k in range(0, len(rows), 1000):
            R.upsert_units_many(cur, rows[k:k + 1000])
        for lib in sids.values():
            R.mark_imported(cur, lib)
        con.commit()
    print("done", len(units), flush=True)


if __name__ == "__main__":
    sys.exit(main())
