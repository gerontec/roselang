#!/usr/bin/env python3
"""Facts restated in our own words, with the sources cited (facts/*.tsv).

The first column is a taxon (plants.tsv) or a compound (compounds.tsv); cards bio:fact.<subject>.<topic>.

A fact (a measured content, a recorded property) is not protected by copyright; the wording of a
text and a database as a whole are. So a fact may come from any source - also share-alike,
non-commercial or proprietary ones - as long as we write it ourselves, cite the source and take
single facts, not a substantial part of a database. The cards carry our licence (MIT), the cited
sources and how well the fact is backed (evidence).

Cards: bio:fact.<taxon>.<topic>, alias fact:<taxon>/<topic>. Rows starting with '#' are comments.
Usage: import_facts.py [facts/plants.tsv ...] [--dry-run]
"""
import argparse
import glob
import os
import sys

import rose_db as R

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EVIDENCE = ("handbook", "single_study", "several_studies", "review", "regulatory")


def rows(path):
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.startswith("#"):
                continue
            f = line.split("\t")
            if len(f) != 7:
                sys.exit(f"{path}:{n}: expected 7 tab-separated columns, got {len(f)}")
            taxon, part, topic, fact, cites, evidence, checked = (x.strip() for x in f)
            if evidence not in EVIDENCE:
                sys.exit(f"{path}:{n}: evidence must be one of {EVIDENCE}")
            yield {"taxon": taxon, "part": part, "topic": topic, "fact": fact,
                   "cites": [c.strip() for c in cites.split(";") if c.strip()], "evidence": evidence, "checked": checked}


def taxon_title(cur, taxon):
    """'Juniperus communis' -> 'Juniperus communis (common juniper)' from the GRIN species card."""
    hit = R.unit_by_alias(cur, "taxon", taxon)
    if not hit:
        return taxon
    cur.execute("SELECT name FROM rose_unit WHERE unit_id=%s", (hit[0],))
    return cur.fetchone()[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    files = a.files or sorted(glob.glob(os.path.join(ROOT, "facts", "*.tsv")))
    con = R.connect()
    cur = con.cursor()
    sid = R.ensure_source(cur, "rose-facts", "https://github.com/gerontec/roselang/tree/main/facts", "MIT", False,
                          "facts restated in our own words with the sources cited (facts are not copyrighted)")
    n = 0
    for path in files:
        for r in rows(path):
            ref = f"bio:fact.{R.slug(r['taxon'])}.{R.slug(r['topic'])}"
            plant = taxon_title(cur, r["taxon"])     # with the common name of the species card, if any
            name = f"{plant}, {r['part']}: {r['topic']}"
            intent = (f"{plant}, {r['part']} - {r['topic']}: {r['fact']} "
                      f"[evidence: {r['evidence'].replace('_', ' ')}; checked {r['checked']}]")
            payload = {"domain": "botany", "status": "defined", "taxon": r["taxon"], "part": r["part"],
                       "topic": r["topic"], "cites": r["cites"], "evidence": r["evidence"], "checked": r["checked"]}
            if a.dry_run:
                print(ref, "|", intent)
                continue
            uid = R.upsert_unit(cur, ref=ref, kind="bio", name=name, intent=intent, source_id=sid,
                                source_url=r["cites"][0] if r["cites"] else None, payload=payload)
            R.set_alias(cur, uid, "fact", f"{r['taxon']}/{r['topic']}")
            n += 1
    if a.dry_run:
        con.rollback()
    else:
        R.mark_imported(cur, sid)
        con.commit()
    print("facts:", n)


if __name__ == "__main__":
    sys.exit(main())
