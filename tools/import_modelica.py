#!/usr/bin/env python3
"""Import the class index of the Modelica Standard Library (BSD-3-Clause) as pointer cards:
"a model for this already exists". Only the class path, its kind, its description string and a source
link are stored - no equations, nothing is simulated.

  refs     msl:Modelica.Thermal.HeatTransfer.Components.HeatCapacitor
  kind     machine (StateGraph), ctrl (Blocks.Continuous, Blocks.Discrete), table (Blocks.Logical,
           Blocks.Tables), algo (functions), model (everything else)
  skipped  partial classes, Icons, Internal, Obsolete, test and conversion libraries
Usage: import_modelica.py [--repo ../data/ModelicaStandardLibrary] [--dry-run]
"""
import argparse
import os
import re
import subprocess
import sys

import rose_db as R

CLS = re.compile(r'^\s*(?:(?:encapsulated|replaceable|final|redeclare|inner|outer|expandable|impure|pure|operator)\s+)*'
                 r'(partial\s+)?(model|block|connector|record|function|package|type)\s+([A-Za-z_][A-Za-z0-9_]*)'
                 r'\s*(?:"([^"]*)")?')
END = re.compile(r"^\s*end\s+([A-Za-z_][A-Za-z0-9_]*)\s*;")
WITHIN = re.compile(r"^\s*within\s+([A-Za-z0-9_.]*)\s*;")
SKIP = (".Icons", ".Internal", "Obsolete", ".UsersGuide", "ModelicaTest", "ModelicaReference")
KIND_PREFIX = [("Modelica.StateGraph", "machine"), ("Modelica.Clocked.ClockSignals", "machine"),
               ("Modelica.Blocks.Continuous", "ctrl"), ("Modelica.Blocks.Discrete", "ctrl"),
               ("Modelica.Blocks.Logical", "table"), ("Modelica.Blocks.Tables", "table")]


def kind_of(path, cls):
    if cls == "function":
        return "algo"
    for prefix, k in KIND_PREFIX:
        if path.startswith(prefix):
            return k
    return "model"


def classes(repo):
    base = os.path.join(repo, "Modelica")
    for dp, _, fs in os.walk(base):
        for f in sorted(fs):
            if not f.endswith(".mo"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, repo)
            within, stack = "", []
            for i, line in enumerate(open(p, encoding="utf-8", errors="replace")):
                m = WITHIN.match(line)
                if m:
                    within = m.group(1)
                    continue
                m = CLS.match(line)
                if m and not line.strip().startswith(("extends", "import")) and "=" not in line.split('"')[0]:
                    partial, cls, name, desc = m.groups()
                    stack.append(name)
                    path = ".".join(x for x in [within] + stack if x)
                    yield {"path": path, "cls": cls, "partial": bool(partial), "desc": desc or "", "file": rel,
                           "line": i + 1}
                    continue
                m = END.match(line)
                if m and stack and stack[-1] == m.group(1):
                    stack.pop()


def words(path):
    last = path.split(".")[-1]
    return re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", last).replace("_", " ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data",
                                                   "ModelicaStandardLibrary"))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    commit = subprocess.run(["git", "-C", a.repo, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    pkg = open(os.path.join(a.repo, "Modelica", "package.mo"), encoding="utf-8", errors="replace").read()
    ver = (re.search(r'version\s*=\s*"([^"]+)"', pkg) or [None, "?"])[1]
    seen, units, stats = set(), [], {}
    for c in classes(a.repo):
        if c["partial"] or c["cls"] in ("package", "type", "connector") or any(s in c["path"] for s in SKIP):
            continue
        if c["path"] in seen or not c["path"].startswith("Modelica."):
            continue
        seen.add(c["path"])
        k = kind_of(c["path"], c["cls"])
        stats[k] = stats.get(k, 0) + 1
        area = " ".join(c["path"].split(".")[1:-1])
        example = ".Examples." in c["path"] + "."
        intent = f"{words(c['path'])} - {c['desc'] or c['cls']} [Modelica {c['cls']}: {area}]" + \
                 (" [example model]" if example else "")
        units.append({"ref": "msl:" + c["path"], "kind": k, "name": c["path"], "intent": intent[:2000],
                      "url": f"https://github.com/modelica/ModelicaStandardLibrary/blob/{commit}/{c['file']}#L{c['line']}",
                      "payload": {"class": c["cls"], "path": c["path"], "description": c["desc"], "file": c["file"],
                                  "line": c["line"], "msl_version": ver, "commit": commit, "example": example,
                                  "status": "solved", "domain": "engineering"}})
    print(f"MSL {ver} @ {commit[:10]}: {len(units)} classes {stats}", flush=True)
    if a.dry_run:
        for u in units:
            if u["name"].endswith(("HeatCapacitor", "LimPID", "StepWithTransition", "CombiTable1Ds")):
                print(u["ref"], u["kind"], "|", u["intent"][:150])
        return 0
    con = R.connect()
    cur = con.cursor()
    sid = R.ensure_source(cur, "modelica", "https://github.com/modelica/ModelicaStandardLibrary", "BSD-3-Clause",
                          False, "Modelica Standard Library class index (path, description, source link)")
    rows = [R.unit_row(ref=u["ref"], kind=u["kind"], name=u["name"][:255], intent=u["intent"], source_id=sid,
                       source_url=u["url"], payload=u["payload"]) for u in units]
    for k in range(0, len(rows), 1000):
        R.upsert_units_many(cur, rows[k:k + 1000])
    R.mark_imported(cur, sid)
    con.commit()
    print("done", len(rows), flush=True)


if __name__ == "__main__":
    sys.exit(main())
