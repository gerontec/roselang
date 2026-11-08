#!/usr/bin/env python3
"""Import the Gene Ontology (go-basic.obo) as bio knowledge cards (kind=bio).

Gene Ontology Consortium, CC BY 4.0 (attribution, not share-alike): every term of the three
namespaces biological_process, molecular_function, cellular_component, without obsolete terms.
  ref     bio:go.0006310
  intent  "<name> - <definition> [synonyms: ...] (GO biological_process)"  - synonyms make the
          term findable under other names (e.g. a process known under several names)
  alias   go:GO:0006310
  payload go id, namespace, definition, synonyms by scope, is_a / part_of parents, release
Usage: import_go.py [--obo FILE] [--dry-run]
"""
import argparse
import os
import re
import sys

import requests

import rose_db as R

OBO_URL = "https://purl.obolibrary.org/obo/go/go-basic.obo"


def parse_obo(text):
    release, term = None, None
    for line in text.splitlines():
        if line.startswith("data-version:"):
            release = line.split(":", 1)[1].strip()
        if line == "[Term]":
            if term:
                yield release, term
            term = {"synonyms": {}, "is_a": [], "part_of": []}
            continue
        if line.startswith("[") and line.endswith("]"):
            if term:
                yield release, term
            term = None
            continue
        if term is None or ": " not in line:
            continue
        k, v = line.split(": ", 1)
        if k in ("id", "name", "namespace"):
            term[k] = v
        elif k == "def":
            m = re.match(r'"((?:[^"\\]|\\.)*)"', v)
            term["def"] = (m.group(1) if m else v).replace('\\"', '"')
        elif k == "synonym":
            m = re.match(r'"((?:[^"\\]|\\.)*)"\s+(EXACT|NARROW|BROAD|RELATED)', v)
            if m:
                term["synonyms"].setdefault(m.group(2).lower(), []).append(m.group(1))
        elif k == "is_a":
            term["is_a"].append(v.split(" ! ")[0])
        elif k == "relationship" and v.startswith("part_of "):
            term["part_of"].append(v.split()[1])
        elif k == "is_obsolete" and v == "true":
            term["obsolete"] = True
    if term:
        yield release, term


def units(text):
    for release, t in parse_obo(text):
        if t.get("obsolete") or not t.get("id", "").startswith("GO:"):
            continue
        syn = [s for scope in ("exact", "narrow", "related", "broad") for s in t["synonyms"].get(scope, [])]
        intent = f"{t['name']} - {t.get('def', '')}".strip()
        if syn:
            intent += " [synonyms: " + "; ".join(syn[:12]) + "]"
        intent += f" (GO {t['namespace']})"
        num = t["id"][3:]
        yield {"ref": f"bio:go.{num}", "name": t["name"], "intent": intent[:2000],
               "url": f"https://amigo.geneontology.org/amigo/term/{t['id']}",
               "go": t["id"],
               "payload": {"go": t["id"], "namespace": t["namespace"], "definition": t.get("def"),
                           "synonyms": t["synonyms"], "is_a": t["is_a"], "part_of": t["part_of"],
                           "release": release, "domain": "biology", "status": "defined"}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--obo")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if a.obo:
        text = open(a.obo, encoding="utf-8").read()
    else:
        r = requests.get(OBO_URL, headers={"User-Agent": R.USER_AGENT}, timeout=300)
        r.raise_for_status()
        text = r.text
    us = list(units(text))
    print(f"go terms: {len(us)}  release {us[0]['payload']['release'] if us else '-'}", flush=True)
    if a.dry_run:
        for u in us[:3] + [u for u in us if "recombination" in u["name"]][:8]:
            print(u["ref"], "|", u["intent"][:160])
        return 0
    con = R.connect()
    cur = con.cursor()
    sid = R.ensure_source(cur, "gene_ontology", "https://geneontology.org", "CC-BY-4.0", False,
                          "Gene Ontology Consortium, go-basic.obo; attribution required")
    for k in range(0, len(us), 1000):
        chunk = us[k:k + 1000]
        R.upsert_units_many(cur, [R.unit_row(ref=u["ref"], kind="bio", name=u["name"], intent=u["intent"],
                                             source_id=sid, source_url=u["url"], payload=u["payload"])
                                  for u in chunk])
        cur.execute("SELECT unit_id, ref FROM rose_unit WHERE ref IN (" + ",".join(["%s"] * len(chunk)) + ")",
                    [u["ref"] for u in chunk])
        ids = dict((ref, uid) for uid, ref in cur.fetchall())
        cur.executemany("INSERT INTO rose_alias (scheme, value, unit_id) VALUES ('go',%s,%s) "
                        "ON DUPLICATE KEY UPDATE unit_id=VALUES(unit_id)",
                        [(u["go"], ids[u["ref"]]) for u in chunk if u["ref"] in ids])
        con.commit()
    R.mark_imported(cur, sid)
    con.commit()
    print("done", flush=True)


if __name__ == "__main__":
    sys.exit(main())
