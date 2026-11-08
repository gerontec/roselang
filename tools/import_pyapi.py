#!/usr/bin/env python3
"""Function-level pointer cards for a curated set of technical PyPI packages, read in a sandbox.

  select      from the PyPI cache (import_pypi.py fetch): packages with a Topic classifier in
              science/engineering/mathematics/hardware/automation, a wheel for this interpreter,
              wheel <= 150 MB, not already covered by import_pylib.py; the top N by downloads
  install     docker, python:3.14-slim: pip install --only-binary :all: --target site/<dist>
              (wheels are unpacked, no setup.py runs)
  introspect  docker with --network none, read-only root, non-root user, no capabilities, 2 GB,
              120 s: pyapi_introspect.py imports the package and lists its public API
  import      out/*.json -> rose_unit (kind algo, refs py:<path>, source py-<dist>, level tested:
              covered by the project's own tests, not run by Rose); GPL-family licences are marked
              share-alike and therefore stay out of the shipped catalog

  import_pyapi.py select [--n 200] | install | introspect | import [--dry-run]
"""
import argparse
import gzip
import json
import os
import re
import subprocess
import sys

import rose_db as R

HERE = os.path.dirname(os.path.abspath(__file__))
PYPI = os.path.join(HERE, "..", "data", "pypi")
BASE = os.path.abspath(os.path.join(HERE, "..", "data", "pyapi"))
IMAGE = "python:3.14-slim"
TECH = ("Scientific/Engineering", "Mathematics", "System / Hardware", "Home Automation", "Embedded")
DONE = {"networkx", "scipy", "sympy", "ortools", "control", "automata-lib", "transitions", "dd"}
SHARE_ALIKE = re.compile(r"\b(A?GPL|LGPL|GNU (Affero |Lesser )?General Public|CC[- ]BY[- ]SA|EUPL|MPL)", re.I)
UID = f"{os.getuid()}:{os.getgid()}"


def norm(name):
    return re.sub(r"[-_.]+", "-", name).lower()


def meta(name):
    p = os.path.join(PYPI, norm(name) + ".json.gz")
    return json.load(gzip.open(p)) if os.path.exists(p) else None


def select(n):
    sys.path.insert(0, HERE)
    import import_pypi as P
    from packaging.tags import sys_tags
    from packaging.utils import parse_wheel_filename
    here = set(sys_tags())
    rows = P.top_list()["rows"]
    out = []
    for rank, row in enumerate(rows, 1):
        d = meta(row["project"])
        if not d or norm(d["info"]["name"]) in DONE:
            continue
        info = d["info"]
        tp = P.topics(info)
        if not any(t.startswith(TECH) or any(x in t for x in TECH) for t in tp):
            continue
        if P.installable(info, d.get("urls") or []) != "wheel":
            continue
        sizes = [f["size"] for f in d["urls"] if f["packagetype"] == "bdist_wheel"
                 and here & set(parse_wheel_filename(f["filename"])[3])]
        if not sizes or min(sizes) > 150e6:
            continue
        out.append({"dist": info["name"], "version": info["version"], "rank": rank, "license": P.licence(info),
                    "docs": P.card(row, rank, d)[0]["payload"]["docs"] if P.card(row, rank, d)[0] else None,
                    "topics": tp[:6]})
        if len(out) >= n:
            break
    os.makedirs(BASE, exist_ok=True)
    json.dump(out, open(os.path.join(BASE, "selection.json"), "w"), indent=1)
    print(f"selected {len(out)}; last rank {out[-1]['rank'] if out else '-'}")


def selection():
    return json.load(open(os.path.join(BASE, "selection.json")))


def install():
    site = os.path.join(BASE, "site")
    os.makedirs(site, exist_ok=True)
    stats = {}
    for s in selection():
        target = os.path.join(site, norm(s["dist"]))
        if os.path.exists(os.path.join(target, ".ok")):
            stats["cached"] = stats.get("cached", 0) + 1
            continue
        cmd = ["docker", "run", "--rm", "--user", UID, "-e", "HOME=/tmp", "-v", f"{site}:/site", IMAGE,
               "pip", "install", "-q", "--no-cache-dir", "--disable-pip-version-check", "--only-binary", ":all:",
               "--target", f"/site/{norm(s['dist'])}", f"{s['dist']}=={s['version']}"]
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
            ok = p.returncode == 0
        except subprocess.TimeoutExpired:
            ok, p = False, None
        if ok:
            open(os.path.join(target, ".ok"), "w").close()
        else:
            err = (p.stderr.strip().splitlines() or ["?"])[-1][:160] if p else "timeout"
            print(f"  install failed {s['dist']}: {err}", flush=True)
        stats["ok" if ok else "failed"] = stats.get("ok" if ok else "failed", 0) + 1
    print("install", stats, flush=True)


def introspect():
    out = os.path.join(BASE, "out")
    os.makedirs(out, exist_ok=True)
    stats = {}
    for s in selection():
        d = norm(s["dist"])
        site = os.path.join(BASE, "site", d)
        dest = os.path.join(out, d + ".json")
        if not os.path.exists(os.path.join(site, ".ok")) or os.path.exists(dest):
            continue
        cmd = ["docker", "run", "--rm", "--network", "none", "--read-only", "--tmpfs", "/tmp:size=256m",
               "--memory", "2g", "--pids-limit", "256", "--cpus", "2", "--cap-drop", "ALL",
               "--security-opt", "no-new-privileges", "--user", UID, "-e", "HOME=/tmp", "-e", "MPLBACKEND=Agg",
               "-v", f"{site}:/site:ro", "-v", f"{os.path.join(HERE, 'pyapi_introspect.py')}:/i.py:ro",
               IMAGE, "timeout", "120", "python", "-I", "/i.py", s["dist"], "/site"]
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
            res = json.loads(p.stdout) if p.returncode == 0 and p.stdout.strip() else None
        except (subprocess.TimeoutExpired, json.JSONDecodeError):
            res = None
        if res is None:
            stats["failed"] = stats.get("failed", 0) + 1
            print(f"  introspect failed {s['dist']}", flush=True)
            continue
        json.dump(res, open(dest, "w"), ensure_ascii=False)
        stats["ok"] = stats.get("ok", 0) + 1
        print(f"  {s['dist']}: {len(res['objects'])} objects, tops {res['tops']}", flush=True)
    print("introspect", stats, flush=True)


def words(path):
    last = path.split(".")[-1]
    return re.sub(r"([a-z])([A-Z])", r"\1 \2", last).replace("_", " ")


def do_import(dry):
    sel = {norm(s["dist"]): s for s in selection()}
    cards, per = [], {}
    for f in sorted(os.listdir(os.path.join(BASE, "out"))):
        res = json.load(open(os.path.join(BASE, "out", f)))
        s = sel.get(norm(res["dist"]))
        if not s:
            continue
        seen = set()
        for o in res["objects"]:
            ref = "py:" + o["path"]
            if ref.lower() in seen:             # refs are case-insensitive in the factory DB
                continue
            seen.add(ref.lower())
            mods = " ".join(p.replace("_", " ") for p in o["path"].split(".")[1:-1])
            intent = f"{words(o['path'])} - {o['doc'] or o['object']}" + (f" [{mods}]" if mods else "") + \
                     f" [call: {o['public']}{o['signature'] or '()'}] [package: {s['dist']}]"
            cards.append((s, o, ref, intent[:2000]))
        per[s["dist"]] = len(seen)
    print(f"{len(cards)} objects from {len(per)} packages", flush=True)
    if dry:
        for s, o, ref, intent in cards[:: max(1, len(cards) // 12)]:
            print(" ", ref, "|", intent[:170])
        return 0
    con = R.connect()
    cur = con.cursor()
    sids = {}
    for s in sel.values():
        if s["dist"] not in per:
            continue
        lic = s["license"] or "LicenseRef-unknown"
        sids[s["dist"]] = R.ensure_source(cur, f"py-{norm(s['dist'])}", f"https://pypi.org/project/{s['dist']}/", lic[:64],
                                          bool(SHARE_ALIKE.search(lic)),
                                          f"public API of {s['dist']} {s.get('version')} read in a sandbox "
                                          "(path, signature, first docstring paragraph)")
    rows = [R.unit_row(ref=ref, kind="algo", name=o["public"][:255], intent=intent, source_id=sids[s["dist"]],
                       source_url=s.get("docs") or f"https://pypi.org/project/{s['dist']}/", signature=o["signature"],
                       payload={"path": o["path"], "public": o["public"], "library": s["dist"], "version": s["version"],
                                "signature": o["signature"], "doc": o["doc"], "status": "solved",
                                "domain": "computer science", "kind_of_object": o["object"]}, level="tested")
            for s, o, ref, intent in cards]
    for k in range(0, len(rows), 1000):
        R.upsert_units_many(cur, rows[k:k + 1000])
    for sid in sids.values():
        R.mark_imported(cur, sid)
    con.commit()
    print("done", len(rows), "share-alike packages:",
          sorted(s for s, x in sel.items() if x["dist"] in per and SHARE_ALIKE.search(x["license"] or "")), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("step", choices=["select", "install", "introspect", "import"])
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if a.step == "select":
        select(a.n)
    elif a.step == "install":
        install()
    elif a.step == "introspect":
        introspect()
    else:
        return do_import(a.dry_run)


if __name__ == "__main__":
    sys.exit(main())
