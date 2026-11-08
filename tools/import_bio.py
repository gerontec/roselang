#!/usr/bin/env python3
"""Import solved bioinformatics problems from the public Rosalind problem list (kind=bio).

Only title + URL are stored (reference cards): the problem texts are copyrighted.
robots.txt is respected (no ?page= URLs). Bio methods and laws from Wikidata come from
import_wikidata.py (biology fields and core methods).
Usage: import_bio.py [--dry-run]
"""
import argparse
import re
import sys

import requests

import rose_db as R

ROSALIND = ["https://rosalind.info/problems/list-view/", "https://rosalind.info/problems/tree-view/"]


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
    ros = list(rosalind_units())
    print(f"rosalind: {len(ros)}")
    if a.dry_run:
        for u in ros[:5]:
            print(u["ref"], "|", u["intent"][:120])
        return 0
    con = R.connect()
    cur = con.cursor()
    sid = R.ensure_source(cur, "rosalind", "https://rosalind.info", "LicenseRef-reference-only", False,
                          "Rosalind problem titles and links only")
    for u in ros:
        R.upsert_unit(cur, ref=u["ref"], kind="bio", name=u["name"], intent=u["intent"], source_id=sid,
                      source_url=u["url"], payload=u["payload"])
    R.mark_imported(cur, sid)
    con.commit()
    print("done")


if __name__ == "__main__":
    sys.exit(main())
