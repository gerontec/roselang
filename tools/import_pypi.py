#!/usr/bin/env python3
"""Import the most-downloaded PyPI packages as pointer cards (kind lib, refs pypi:<name>):
"a maintained package for this exists - pip install <name>". Metadata only: nothing is installed or run.

  selection  the top 15 000 projects by downloads in the last 30 days (hugovk/top-pypi-packages,
             a list of names and counts), not all ~935 000 PyPI projects: most of those are empty,
             abandoned, squatted or malicious names a weak model must not be pointed to
  filter     the latest release must install on THIS interpreter: requires_python admits it and a
             wheel matches its tags (packaging.tags.sys_tags) - or, marked as such, only an sdist exists
  card       summary, keywords, Topic classifiers, licence, requires_python, wheel/sdist, monthly
             downloads and rank, project and documentation links

  fetch   import_pypi.py fetch [--top 15000]    PyPI JSON API -> data/pypi/<name>.json.gz (cache, polite)
  import  import_pypi.py import [--dry-run]     cache -> rose_unit (source 'pypi')
"""
import argparse
import concurrent.futures as cf
import gzip
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

import rose_db as R

TOP_URL = "https://hugovk.dev/top-pypi-packages/top-pypi-packages.min.json"
UA = "roselang-importer/0.1 (+https://github.com/gerontec/roselang)"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "pypi")


def norm(name):
    return re.sub(r"[-_.]+", "-", name).lower()


def get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def top_list():
    path = os.path.join(CACHE, "_top.json")
    if not os.path.exists(path):
        os.makedirs(CACHE, exist_ok=True)
        open(path, "wb").write(get(TOP_URL))
    return json.load(open(path))


def fetch_one(name):
    path = os.path.join(CACHE, norm(name) + ".json.gz")
    if os.path.exists(path):
        return "cached"
    for attempt in range(3):
        try:
            data = get(f"https://pypi.org/pypi/{name}/json")
            with gzip.open(path, "wb") as f:
                f.write(data)
            time.sleep(0.15)
            return "ok"
        except urllib.error.HTTPError as e:
            if e.code == 404:                       # removed or quarantined by PyPI
                open(path[:-8] + ".404", "w").close()
                return "404"
            time.sleep(2 + 5 * attempt)
        except Exception:
            time.sleep(2 + 5 * attempt)
    return "failed"


def fetch(top):
    rows = top_list()["rows"][:top]
    stats = {}
    with cf.ThreadPoolExecutor(4) as ex:
        for i, res in enumerate(ex.map(fetch_one, [r["project"] for r in rows]), 1):
            stats[res] = stats.get(res, 0) + 1
            if i % 1000 == 0:
                print(i, stats, flush=True)
    print("fetched", stats, flush=True)


def installable(info, files):
    """'wheel' / 'sdist' / None for the running interpreter."""
    from packaging.specifiers import InvalidSpecifier, SpecifierSet
    from packaging.tags import sys_tags
    from packaging.utils import InvalidWheelFilename, parse_wheel_filename
    rp = info.get("requires_python")
    if rp:
        try:
            if not SpecifierSet(rp).contains(".".join(map(str, sys.version_info[:3]))):
                return None
        except InvalidSpecifier:
            pass
    here = set(sys_tags())
    live = [f for f in files if not f.get("yanked")]
    for f in live:
        if f["packagetype"] == "bdist_wheel":
            try:
                if here & set(parse_wheel_filename(f["filename"])[3]):
                    return "wheel"
            except InvalidWheelFilename:
                continue
    return "sdist" if any(f["packagetype"] == "sdist" for f in live) else None


def licence(info):
    if info.get("license_expression"):
        return info["license_expression"][:80]
    cl = [c.split(" :: ")[-1] for c in info.get("classifiers") or [] if c.startswith("License ::")]
    if cl:
        return "; ".join(cl)[:80]
    lic = (info.get("license") or "").strip()
    return lic[:80] if lic and "\n" not in lic and len(lic) < 80 else None


def topics(info):
    out = []
    for c in info.get("classifiers") or []:
        if c.startswith("Topic ::"):
            out.append(" / ".join(c.split(" :: ")[1:]))
    return out


def card(row, rank, d):
    info = d["info"]
    inst = installable(info, d.get("urls") or [])
    if inst is None:
        return None, "not installable here"
    summary = " ".join((info.get("summary") or "").split())
    if not summary:
        return None, "no summary"
    name = info["name"]
    kw = info.get("keywords") or ""
    kw = ", ".join(x.strip() for x in re.split(r"[,;]|\s{2,}", kw) if x.strip())[:300] if "," in kw or ";" in kw \
        else " ".join(kw.split())[:300]
    tp = topics(info)
    urls = info.get("project_urls") or {}
    docs = next((v for k, v in urls.items() if k.lower() in ("documentation", "docs", "homepage", "home")), None) \
        or info.get("home_page") or None
    intent = f"{name} - {summary}"
    if kw:
        intent += f" [keywords: {kw}]"
    if tp:
        intent += " [topics: " + "; ".join(tp[:8]) + "]"
    intent += f" [install: pip install {name}]"
    payload = {"package": name, "version": info.get("version"), "license": licence(info),
               "requires_python": info.get("requires_python"), "install": inst,
               "downloads_30d": row["download_count"], "rank": rank, "docs": docs, "topics": tp,
               "status": "solved", "domain": "software"}
    return {"ref": "pypi:" + norm(name), "name": name, "intent": intent[:2000],
            "url": f"https://pypi.org/project/{name}/", "payload": payload}, inst


def do_import(dry):
    rows = top_list()["rows"]
    cards, stats = [], {}
    for rank, row in enumerate(rows, 1):
        path = os.path.join(CACHE, norm(row["project"]) + ".json.gz")
        if not os.path.exists(path):
            stats["not fetched"] = stats.get("not fetched", 0) + 1
            continue
        c, why = card(row, rank, json.load(gzip.open(path)))
        stats[why] = stats.get(why, 0) + 1
        if c:
            cards.append(c)
    print(f"{len(cards)} cards from {len(rows)} projects: {stats}", flush=True)
    if dry:
        for c in cards:
            if c["name"].lower() in ("networkx", "python-control", "control", "pulp", "simpy", "transitions", "pint"):
                print(c["ref"], "|", c["intent"][:200], "|", c["payload"]["install"], c["payload"]["license"])
        return 0
    con = R.connect()
    cur = con.cursor()
    sid = R.ensure_source(cur, "pypi", "https://pypi.org", "LicenseRef-PyPI-metadata", False,
                          "top PyPI packages by downloads (hugovk/top-pypi-packages): name, summary, keywords, "
                          "classifiers, licence, links - metadata as published by each project on PyPI")
    urows = [R.unit_row(ref=c["ref"], kind="lib", name=c["name"], intent=c["intent"], source_id=sid,
                        source_url=c["url"], payload=c["payload"]) for c in cards]
    for k in range(0, len(urows), 1000):
        R.upsert_units_many(cur, urows[k:k + 1000])
    R.mark_imported(cur, sid)
    con.commit()
    print("done", len(urows), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("step", choices=["fetch", "import"])
    ap.add_argument("--top", type=int, default=15000)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if a.step == "fetch":
        fetch(a.top)
    else:
        return do_import(a.dry_run)


if __name__ == "__main__":
    sys.exit(main())
