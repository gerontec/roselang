#!/usr/bin/env python3
"""Import solver functions of Python libraries as solver cards (kind algo, refs py:<public path>):
the answer to "is there a solution?" becomes a function that already exists, is tested and maintained.

  networkx  (BSD-3-Clause)  every public function/class of networkx.algorithms.*, by introspection
  scipy     (BSD-3-Clause)  public API (__all__) of the solver subpackages, by introspection
  ortools   (Apache-2.0)    curated entry points (SWIG modules cannot be introspected usefully)
  python    (PSF-2.0)       a few standard-library solvers (bisect, heapq, graphlib, difflib, ...)
Stored per card: public path, signature, first docstring paragraph, library version, docs URL.
Nothing is executed except importing the libraries. Run with the interpreter that has them, e.g.
  ~/roselang/.venv-libs/bin/python tools/import_pylib.py [--dry-run]
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
        "python": ("https://docs.python.org/3/library/", "PSF-2.0")}


def summary(obj):
    doc = inspect.getdoc(obj) or ""
    para = doc.strip().split("\n\n")[0]
    return " ".join(para.split())[:600]


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
    return inspect.isfunction(obj) or inspect.isclass(obj) or type(obj).__name__ in ("ufunc", "builtin_function_or_method")


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
    units = networkx_units() + scipy_units() + ortools_units() + stdlib_units()
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
            if u["path"].endswith(("traveling_salesman_problem", "linear_sum_assignment", "RoutingModel", "TopologicalSorter")):
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
