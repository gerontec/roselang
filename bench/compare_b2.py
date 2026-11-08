#!/usr/bin/env python3
"""Language (Rose, variant C) vs. Python module (`import rose`, variant B2): WHEN is an error found?

Every case is the same faulty program twice. Phases:
  Rose:   check  - by `rosec` before anything runs
          run    - only when the compiled program runs its tests
  Python: define - when the module code is executed (law/table/use at import time)
          call   - only when the faulty line is executed by the test call
          never  - the test call passes, the error stays in the program
This measures the checks, not the LLM. The LLM benchmark (pass@1, tokens, rounds) is M7.
Usage: python3 bench/compare_b2.py [--json]
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from rose.compiler import compile_source  # noqa: E402
from rose.knowledge import Knowledge  # noqa: E402

PRE = "import rose\nfrom rose import Q\n"

CASES = [
    {"id": "add_power_energy", "code": "E201", "what": "power + energy",
     "rose": 'fn f(p: Real[W], e: Real[kW*h]) -> Real[W]\n  intent "x"\n= p + e\ntest f(1 W, 1 kW*h) == 1 W',
     "py_def": "def f(p, e):\n    return p + e\n",
     "py_call": "f(Q(1, 'W'), Q(1, 'kWh'))"},
    {"id": "add_in_rare_branch", "code": "E201", "what": "power + energy in a branch the test does not take",
     "rose": 'fn f(p: Real[W], e: Real[kW*h], x: Bool) -> Real[W]\n  intent "x"\ndo\n  if x do\n    return p + e\n'
             '  end\n  return p\nend\ntest f(1 W, 1 kW*h, false) == 1 W',
     "py_def": "def f(p, e, x):\n    if x:\n        return p + e\n    return p\n",
     "py_call": "assert f(Q(1, 'W'), Q(1, 'kWh'), False) == Q(1, 'W')"},
    {"id": "bare_number", "code": "E202", "what": "power compared with a bare number",
     "rose": 'fn f(p: Real[W]) -> Bool\n  intent "x"\n= p > 9\ntest f(10 W) == true',
     "py_def": "def f(p):\n    return p > 9\n",
     "py_call": "f(Q(10, 'W'))"},
    {"id": "plain_floats", "code": "E202", "what": "caller passes plain numbers instead of quantities",
     "rose": 'fn f(p: Real[W], e: Real[kW*h]) -> Real[W]\n  intent "x"\n= p\ntest f(1, 2) == 1 W',
     "py_def": "def f(p, e):\n    return p\n",
     "py_call": "f(1, 2)"},
    {"id": "add_abs_temperatures", "code": "E203", "what": "degC + degC",
     "rose": 'fn f(a: Real[degC], b: Real[degC]) -> Real[degC]\n  intent "x"\n= a + b\ntest f(1 degC, 2 degC) == 3 degC',
     "py_def": "def f(a, b):\n    return a + b\n",
     "py_call": "f(Q(1, 'degC'), Q(2, 'degC'))"},
    {"id": "law_inconsistent", "code": "E204", "what": "law without cp: W = kg/s * K",
     "rose": 'law wrong\n  intent "x"\n  var P: Real[W]\n  var mdot: Real[kg/s]\n  var dT: Real[K]\n  eq P = mdot * dT\nend',
     "py_def": "wrong = rose.law('wrong', 'P = mdot*dT', P='W', mdot='kg/s', dT='K')\n",
     "py_call": "pass"},
    {"id": "use_open_problem", "code": "E305", "what": "open problem used as a building block",
     "rose": 'use open:goldbachs_conjecture\nfn f(n: Int) -> Int\n  intent "x"\n= n',
     "py_def": "g = rose.use('open:goldbachs_conjecture')\n",
     "py_call": "pass"},
    {"id": "table_incomplete", "code": "E511", "what": "decision table misses soc < 10 % without grid",
     "rose": 'table src\n  intent "x"\n  hit unique\n  in soc: Real[%]{0 .. 100}, grid_ok: Bool\n  out s: {battery, grid, none}\n'
             '  rule soc >= 20 %, true -> battery\n  rule soc < 20 %, true -> grid\n  rule soc >= 10 %, false -> battery\n'
             '  check complete, no_overlap\nend',
     "py_def": "src = rose.table('src', {'soc': ('%', 0, 100), 'grid_ok': bool}, [('>= 20 %', True, 'battery'), "
               "('< 20 %', True, 'grid'), ('>= 10 %', False, 'battery')])\n",
     "py_call": "pass"},
    {"id": "table_overlap", "code": "E512", "what": "two rules overlap between 10 and 20 %",
     "rose": 'table src\n  intent "x"\n  hit unique\n  in soc: Real[%]{0 .. 100}\n  out s: {battery, grid}\n'
             '  rule soc >= 10 % -> battery\n  rule soc < 20 % -> grid\n  check complete, no_overlap\nend',
     "py_def": "src = rose.table('src', {'soc': ('%', 0, 100)}, [('>= 10 %', 'battery'), ('< 20 %', 'grid')])\n",
     "py_call": "pass"},
    {"id": "solve_wrong_given", "code": "E201", "what": "solve given a temperature where a power is expected",
     "rose": 'use law:kinetic_energy\nfn f(t: Real[K], m: Real[kg]) -> Real[m/s]\n  intent "x"\n'
             '= solve kinetic_energy for v given T = t, m = m\ntest f(1 K, 1 kg) == 1 m/s',
     "py_def": "ke = rose.use('law:kinetic_energy')\ndef f(t, m):\n    return ke.solve('v', T=t, m=m)\n",
     "py_call": "f(Q(1, 'K'), Q(1, 'kg'))"},
]


def rose_phase(case, kb):
    code, diags, _ = compile_source("module bench\n" + case["rose"], case["id"] + ".rose", kb)
    got = [d.code for d in diags if d.severity == "error"]
    if case["code"] in got:
        return "check", got
    if code is None:
        return "check(other)", got
    r = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True, timeout=30)
    return ("run" if r.returncode else "never"), got


def py_run(src):
    r = subprocess.run([sys.executable, "-c", src], capture_output=True, text=True, timeout=60,
                       cwd=ROOT, env=dict(os.environ, PYTHONPATH=ROOT))
    return r.returncode, r.stderr


def py_phase(case):
    rc, err = py_run(PRE + case["py_def"])
    if rc:
        return "define", err.strip().splitlines()[-1][:90]
    rc, err = py_run(PRE + case["py_def"] + case["py_call"] + "\n")
    if rc:
        return "call", err.strip().splitlines()[-1][:90]
    return "never", ""


def main():
    kb = Knowledge()
    rows = []
    for c in CASES:
        rp, got = rose_phase(c, kb)
        pp, msg = py_phase(c)
        rows.append({"id": c["id"], "code": c["code"], "what": c["what"], "rose": rp, "python": pp,
                     "python_error": msg, "rose_codes": got})
    if "--json" in sys.argv:
        print(json.dumps(rows, indent=1))
        return
    print(f"{'case':<22} {'want':<5} {'Rose':<13} {'Python module':<14} what")
    for r in rows:
        print(f"{r['id']:<22} {r['code']:<5} {r['rose']:<13} {r['python']:<14} {r['what']}")
    static = sum(r["rose"] == "check" for r in rows)
    early = sum(r["python"] == "define" for r in rows)
    never = sum(r["python"] == "never" for r in rows)
    print(f"\nRose finds {static}/{len(rows)} before running. Python module: {early} at definition, "
          f"{sum(r['python'] == 'call' for r in rows)} only when the faulty line runs, {never} never.")


if __name__ == "__main__":
    main()
