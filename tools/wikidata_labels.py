#!/usr/bin/env python3
"""English label, aliases and taxon common names (P1843) of many Wikidata items, cached as JSONL.

Used for the LOTUS pack: compound names ('psilocybin' instead of the IUPAC name) and common names of
organisms without a GRIN card ('liberty cap'). Wikidata is CC0. Resumable: items already in the
output file are skipped.
Usage: wikidata_labels.py QIDS.txt OUT.jsonl [--batch 400] [--pause 1.0]
"""
import argparse
import json
import os
import sys
import time

import requests

import rose_db as R

URL = "https://query.wikidata.org/sparql"
Q = """SELECT ?item ?label (GROUP_CONCAT(DISTINCT ?alt; separator="\\u001f") AS ?alts)
       (GROUP_CONCAT(DISTINCT ?cn; separator="\\u001f") AS ?cns) WHERE {
  VALUES ?item { %s }
  OPTIONAL { ?item rdfs:label ?label FILTER(LANG(?label) = "en") }
  OPTIONAL { ?item skos:altLabel ?alt FILTER(LANG(?alt) = "en") }
  OPTIONAL { ?item wdt:P1843 ?cn FILTER(LANG(?cn) = "en") }
} GROUP BY ?item ?label"""


def fetch(s, qids):
    for attempt in range(6):
        try:
            r = s.post(URL, data={"query": Q % " ".join("wd:" + q for q in qids)},
                       headers={"Accept": "application/sparql-results+json"}, timeout=120)
            if r.status_code in (429, 500, 502, 503, 504):
                wait = int(r.headers.get("Retry-After", 0) or 0) or 10 * 2 ** attempt
                print(f"HTTP {r.status_code}, waiting {wait} s", file=sys.stderr, flush=True)
                time.sleep(wait)
                continue
            r.raise_for_status()
            return r.json()["results"]["bindings"]
        except requests.RequestException as e:
            print(f"error {e}, retry", file=sys.stderr, flush=True)
            time.sleep(10 * 2 ** attempt)
    raise SystemExit("giving up after 6 attempts")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("qids")
    ap.add_argument("out")
    ap.add_argument("--batch", type=int, default=400)
    ap.add_argument("--pause", type=float, default=1.0)
    a = ap.parse_args()
    want = [l.strip() for l in open(a.qids) if l.strip().startswith("Q")]
    done = set()
    if os.path.exists(a.out):
        with open(a.out, encoding="utf-8") as fh:
            done = {json.loads(l)["q"] for l in fh if l.strip()}
    todo = [q for q in dict.fromkeys(want) if q not in done]
    print(f"{len(want)} items, {len(done)} cached, {len(todo)} to fetch", file=sys.stderr, flush=True)
    s = requests.Session()
    s.headers["User-Agent"] = R.USER_AGENT
    t0 = time.time()
    with open(a.out, "a", encoding="utf-8") as fh:
        for i in range(0, len(todo), a.batch):
            part = todo[i:i + a.batch]
            got = {}
            for b in fetch(s, part):
                q = b["item"]["value"].rsplit("/", 1)[-1]
                split = lambda k: [x for x in b.get(k, {}).get("value", "").split("\x1f") if x]  # noqa: E731
                got[q] = {"q": q, "label": b.get("label", {}).get("value"), "aliases": split("alts"), "common": split("cns")}
            for q in part:                      # items without any English text are cached too
                fh.write(json.dumps(got.get(q, {"q": q, "label": None, "aliases": [], "common": []}), ensure_ascii=False) + "\n")
            fh.flush()
            n = i + len(part)
            print(f"{n}/{len(todo)} ({time.time() - t0:.0f} s)", file=sys.stderr, flush=True)
            time.sleep(a.pause)
    print("done", file=sys.stderr, flush=True)


if __name__ == "__main__":
    sys.exit(main())
