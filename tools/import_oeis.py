#!/usr/bin/env python3
"""Import the OEIS (names.gz + stripped.gz) into wagodb.rose_*.

Each sequence becomes kind=math, ref oeis:Annnnnn, name = OEIS name,
payload.terms = the leading terms (as strings, they exceed 64 bit).
Licence: CC BY-SA 4.0 (share-alike), recorded in rose_source.
"""
import gzip
import io
import json
import sys

import requests

import rose_db as R

NAMES = "https://oeis.org/names.gz"
STRIPPED = "https://oeis.org/stripped.gz"
BATCH = 5000


def fetch(url):
    r = requests.get(url, headers={"User-Agent": R.USER_AGENT}, timeout=300)
    r.raise_for_status()
    return gzip.GzipFile(fileobj=io.BytesIO(r.content)).read().decode("utf-8", "replace").splitlines()


def main():
    names = {}
    for l in fetch(NAMES):
        if l and not l.startswith("#"):
            a, _, name = l.partition(" ")
            names[a] = name.strip()
    terms = {}
    for l in fetch(STRIPPED):
        if l and not l.startswith("#"):
            a, _, t = l.partition(" ")
            terms[a] = [x for x in t.strip().strip(",").split(",") if x][:40]
    print(f"names: {len(names)}  stripped: {len(terms)}", flush=True)
    con = R.connect()
    cur = con.cursor()
    sid = R.ensure_source(cur, "oeis", "https://oeis.org", "CC-BY-SA-4.0", True,
                          "On-Line Encyclopedia of Integer Sequences")
    rows, n = [], 0
    for a in sorted(names):
        t = terms.get(a, [])
        rows.append(R.unit_row(ref=f"oeis:{a}", kind="math", name=names[a] or a,
                               intent=f"{names[a]} (integer sequence {a})", source_id=sid,
                               source_url=f"https://oeis.org/{a}", signature="(n: Int) -> Int",
                               payload={"oeis": a, "terms": t}))
        if len(rows) >= BATCH:
            R.upsert_units_many(cur, rows)
            con.commit()
            n += len(rows)
            rows = []
            print(f"  {n}", flush=True)
    if rows:
        R.upsert_units_many(cur, rows)
        n += len(rows)
    R.mark_imported(cur, sid)
    con.commit()
    print(f"OEIS: {n} sequences", flush=True)


if __name__ == "__main__":
    sys.exit(main())
