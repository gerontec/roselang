#!/usr/bin/env python3
"""Protein similarity computed with DIAMOND, as pointer cards: which proteins of one organism resemble
proteins of another (e.g. long pepper vs human). Our own computation on NCBI nr sequences (public
domain), cards under MIT; every card records the method (DIAMOND version, mode, E-value cut-off, nr
release hash) so that the result can be reproduced and judged.

Input: a TSV with a header line and the columns
  qacc qtitle sacc stitle [sorg] pident length evalue bitscore qcov
(DIAMOND outfmt 6 with the titles joined from the nr metadata). Similarity is not function: a hit
says the sequences resemble each other, not that the proteins do the same in both organisms.

Cards: bio:homolog.<query taxon>.<qacc> (one per query protein with hits, best hits first) and the
overview bio:homolog.<query taxon>.<subject taxon> (how many query proteins have hits, the best of each).
Usage: import_diamond.py result.tsv --query-taxon "Piper longum" --subject-taxon "Homo sapiens"
       --method "DIAMOND 2.2.8 blastp --more-sensitive -e 1e-5, nr dmnd_hash ..." [--top 5] [--dry-run]
"""
import argparse
import collections
import csv
import sys

import rose_db as R

NCBI = "https://www.ncbi.nlm.nih.gov/protein/{}"


def taxon_title(cur, taxon):
    """'Piper longum' -> 'Piper longum (Indian long pepper)' from the GRIN species card, if any."""
    hit = R.unit_by_alias(cur, "taxon", taxon)
    if not hit:
        return taxon
    cur.execute("SELECT name FROM rose_unit WHERE unit_id=%s", (hit[0],))
    return cur.fetchone()[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tsv")
    ap.add_argument("--query-taxon", required=True)
    ap.add_argument("--subject-taxon", required=True)
    ap.add_argument("--subject-common", help="common name of the subject taxon, e.g. human")
    ap.add_argument("--method", required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--note", default="", help="interpretation for the overview card, e.g. what the hits do not show")
    ap.add_argument("--n-query", type=int, help="number of query proteins searched (for the overview card)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    hits = collections.defaultdict(list)
    qtitle = {}
    with open(a.tsv, encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            qtitle[r["qacc"]] = r["qtitle"]
            hits[r["qacc"]].append({"acc": r["sacc"], "title": r["stitle"], "organism": r.get("sorg") or a.subject_taxon,
                                    "identity": float(r["pident"]),
                                    "length": int(r["length"]), "evalue": float(r["evalue"]),
                                    "bitscore": float(r["bitscore"]), "qcov": float(r["qcov"])})
    con = R.connect()
    cur = con.cursor()
    sid = R.ensure_source(cur, "rose-diamond", "https://github.com/gerontec/roselang", "MIT", False,
                          "protein similarity computed with DIAMOND on NCBI nr sequences (public domain)")
    n = 0
    qname = taxon_title(cur, a.query_taxon)
    sname = f"{a.subject_taxon} ({a.subject_common})" if a.subject_common else a.subject_taxon
    overview = []
    for q, hs in sorted(hits.items()):
        best = {}
        for h in sorted(hs, key=lambda h: (-h["bitscore"], h["evalue"])):
            best.setdefault(h["acc"], h)          # one HSP per subject: the best
        hs = list(best.values())[:a.top]
        shown = "; ".join(f"{h['title']} ({h['acc']}" + (f", {h['organism']}" if h["organism"] != a.subject_taxon else "")
                          + f", identity {h['identity']:.0f} %, coverage {h['qcov']:.0f} %, "
                          f"E-value {h['evalue']:.1e})" for h in hs)
        ref = f"bio:homolog.{R.slug(a.query_taxon)}.{R.slug(q)}"
        overview.append((hs[0]["bitscore"], f"{qtitle[q]} ~ {hs[0]['title']} ({hs[0]['identity']:.0f} %)"))
        name = f"{a.query_taxon} {qtitle[q]} ({q}) ~ {sname}"
        intent = (f"Protein {qtitle[q]} ({q}) of {qname} is similar in sequence to {sname} proteins: "
                  f"{shown}. [similarity, not proof of the same function; computed {a.date}: {a.method}]")
        payload = {"domain": "biology", "status": "defined", "query": {"acc": q, "title": qtitle[q],
                   "taxon": a.query_taxon}, "subject_taxon": a.subject_taxon, "hits": hs, "method": a.method,
                   "computed": a.date}
        if a.dry_run:
            print(ref, "|", intent[:300])
            continue
        uid = R.upsert_unit(cur, ref=ref, kind="bio", name=name, intent=intent, source_id=sid,
                            source_url=NCBI.format(q), payload=payload)
        R.set_alias(cur, uid, "protein", q)
        n += 1
    if hits:
        ov = "; ".join(t for _, t in sorted(overview, reverse=True))
        total = f" of the {a.n_query} searched" if a.n_query else ""
        ref = f"bio:homolog.{R.slug(a.query_taxon)}.{R.slug(a.subject_taxon)}"
        intent = (f"{sname} proteins similar to proteins of {qname}: {len(hits)}{total} {a.query_taxon} "
                  f"proteins have significant hits, the best by score: {ov}. One card per protein "
                  f"(bio:homolog.{R.slug(a.query_taxon)}.<accession>). " + (a.note + " " if a.note else "") + f"[similarity, not proof of the same function; "
                  f"computed {a.date}: {a.method}]")
        if a.dry_run:
            print(ref, "|", intent[:400])
        else:
            R.upsert_unit(cur, ref=ref, kind="bio", name=f"{qname} proteins similar to {sname} proteins",
                          intent=intent, source_id=sid, source_url=None,
                          payload={"domain": "biology", "status": "defined", "query_taxon": a.query_taxon,
                                   "subject_taxon": a.subject_taxon, "n_query": a.n_query, "n_with_hits": len(hits),
                                   "method": a.method, "computed": a.date, "note": a.note})
            n += 1
    if a.dry_run:
        con.rollback()
    else:
        R.mark_imported(cur, sid)
        con.commit()
    print("homolog cards:", n)


if __name__ == "__main__":
    sys.exit(main())
