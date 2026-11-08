#!/usr/bin/env python3
"""Acceptance test of `rosec plan` (needs the corpus): category, expected unit in the top 5,
negative-knowledge warnings. Expectations in plan_cases.json were written before the first run."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from rose.corpus import Corpus  # noqa: E402

c = Corpus()
if not c.online:
    sys.exit(f"corpus offline: {c.error}")
cases = json.load(open(os.path.join(HERE, "plan_cases.json")))
passed = 0
for case in cases:
    r = c.plan(case["task"], k=5)
    refs = [p["ref"].lower() for p in r["paths"]]
    warn = " ".join(r["warnings"]).lower()
    checks = []
    if "category" in case:
        checks.append(("category", (r["category"] or "").startswith(case["category"])))
    if "ref_any" in case:
        checks.append(("top5", any(s in ref for s in case["ref_any"] for ref in refs)))
    if "warning" in case:
        checks.append(("warning", case["warning"] in warn))
    if case.get("no_warning"):
        checks.append(("no warning", not r["warnings"]))
    ok = all(v for _, v in checks)
    passed += ok
    print(f"{'ok  ' if ok else 'FAIL'} {case['task'][:70]}")
    print(f"     category {r['category']} (margin {r['confidence']:.2f})  top: {', '.join(refs[:3])}")
    if r["warnings"]:
        print(f"     warning: {r['warnings'][0][:110]}")
    if not ok:
        print("     failed: " + ", ".join(n for n, v in checks if not v))
print(f"{passed}/{len(cases)} plan cases passed")
