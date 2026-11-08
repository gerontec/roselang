#!/usr/bin/env python3
"""Import already solved biology problems into wagodb.rose_* (kind=bio).

Sources:
  own      - the user's own solved bio problems on the dell: scripts of the DIAMOND/nr pipeline
             (gerontec/blastDiamond), reports, AmyloDeep, ivermectin simulation. Module docstring
             -> intent, path + role in payload. Reference cards: the code stays where it is.
  rosalind - the public Rosalind problem list (title + URL only; problem texts are copyrighted,
             robots.txt is respected: no ?page= URLs).
Run on the dell (reads local files). Usage: import_bio.py [--dry-run]
"""
import argparse
import ast
import glob
import os
import re
import sys

import requests

import rose_db as R

HOME = os.path.expanduser("~")
REPO = os.path.join(HOME, "src/blastDiamond")
OWN_GLOBS = [
    f"{REPO}/pipeline/*.py", f"{REPO}/examples/*.py", f"{REPO}/amyloid/*.py",
    f"{HOME}/python/rep_new*.py", f"{HOME}/python/blast_*.py", f"{HOME}/python/dmnd_*.py",
    f"{HOME}/python/nr_*.py", f"{HOME}/python/amylo*.py", f"{HOME}/python/ace2*.py",
    f"{HOME}/iver_sim/ol_amyloid/*.py", f"{HOME}/iver_sim/*.py",
]
# scripts that answer a question (as opposed to keeping the infrastructure running)
SOLUTION = re.compile(r"(^rep_|spike_|amylo_gpu|nr_seq\.py|dmnd_getseq|dmnd_preselect|blast_api_worker|"
                      r"nr_seqhash|blast_compare|ace2|iver|sim)")
ROSALIND = ["https://rosalind.info/problems/list-view/", "https://rosalind.info/problems/tree-view/"]


def docstring(path):
    try:
        return ast.get_docstring(ast.parse(open(path, encoding="utf-8", errors="replace").read())) or ""
    except SyntaxError:
        return ""


def own_units():
    seen = {}
    for g in OWN_GLOBS:
        for p in sorted(glob.glob(g)):
            base = os.path.basename(p)
            # the public repo copy wins over the working copy in ~/python
            if base in seen and not p.startswith(REPO):
                continue
            seen[base] = p
    for base, p in sorted(seen.items()):
        doc = docstring(p).strip()
        if not doc:
            continue
        first = doc.split("\n\n")[0].replace("\n", " ").strip()
        role = "solution" if SOLUTION.search(base) else "infrastructure"
        public = p.startswith(REPO)
        url = ("https://github.com/gerontec/blastDiamond/blob/main/" + os.path.relpath(p, REPO)) if public else None
        yield {
            "ref": f"bio:own.{R.slug(os.path.splitext(base)[0])}",
            "name": f"{base}: {first[:200]}",
            "intent": f"[own {role}] {first[:900]}",
            "url": url,
            "payload": {"host": "dell", "path": p, "role": role, "public_repo": public,
                        "doc": doc[:4000], "domain": "biology"},
        }


def rosalind_units():
    seen = {}
    for url in ROSALIND:
        try:
            html = requests.get(url, headers={"User-Agent": R.USER_AGENT}, timeout=30).text
        except requests.RequestException as e:
            print(f"rosalind {url}: {e}", file=sys.stderr)
            continue
        for pid, title in re.findall(r'href="/problems/([a-z0-9]+)/"[^>]*>([^<]+)<', html):
            title = title.strip().strip("“”\"")
            if pid in ("topics", "list", "tree") or not title or len(title) < 4:
                continue
            seen.setdefault(pid, title)
    for pid, title in sorted(seen.items()):
        yield {
            "ref": f"bio:rosalind.{pid}",
            "name": f"Rosalind {pid.upper()}: {title}",
            "intent": f"{title} (classic bioinformatics problem, Rosalind {pid.upper()}; solved, known algorithm)",
            "url": f"https://rosalind.info/problems/{pid}/",
            "payload": {"rosalind": pid, "title": title, "status": "proved", "domain": "biology",
                        "note": "reference only: problem text is copyrighted"},
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    own, ros = list(own_units()), list(rosalind_units())
    print(f"own: {len(own)} ({sum(u['payload']['role'] == 'solution' for u in own)} solutions)  rosalind: {len(ros)}")
    if a.dry_run:
        for u in own[:5] + ros[:3]:
            print(u["ref"], "|", u["intent"][:120])
        return 0
    con = R.connect()
    cur = con.cursor()
    s_own = R.ensure_source(cur, "gerontec-bio", "https://github.com/gerontec/blastDiamond", "LicenseRef-own", False,
                            "own solved bio problems on the dell (DIAMOND nr pipeline, reports, AmyloDeep)")
    s_ros = R.ensure_source(cur, "rosalind", "https://rosalind.info", "LicenseRef-reference-only", False,
                            "Rosalind problem titles and links only")
    for u in own:
        R.upsert_unit(cur, ref=u["ref"], kind="bio", name=u["name"], intent=u["intent"], source_id=s_own,
                      source_url=u["url"], payload=u["payload"])
    for u in ros:
        R.upsert_unit(cur, ref=u["ref"], kind="bio", name=u["name"], intent=u["intent"], source_id=s_ros,
                      source_url=u["url"], payload=u["payload"])
    R.mark_imported(cur, s_own)
    R.mark_imported(cur, s_ros)
    con.commit()
    print("done")


if __name__ == "__main__":
    sys.exit(main())
