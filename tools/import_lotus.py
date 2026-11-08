#!/usr/bin/env python3
"""All natural products of LOTUS with the organisms they are recorded in - the full compound <->
organism mapping (the core has only the ~420 compounds with an ATC code, bio:drug.*).

Input: data/lotus/<date>_frozen_metadata.csv.gz from the LOTUS frozen dump on Zenodo (record
19360665, v11 of 2026-04-13, CC BY 4.0; the triplets themselves live in Wikidata, CC0). One row per
structure-organism-reference triplet. Cards bio:lotus.<qid> with the name (LOTUS 'traditional' name,
else IUPAC), formula, NPClassifier class, all organisms (found_in) and for each organism the first
reference DOI (found_in_refs). Compounds that also have a bio:drug card (same Wikidata item) keep their
LOTUS card with drug_ref -> the drug card; the index and the effect map put their organisms on the drug.
Organism names are compared normalised (lower case, hyphens removed: Atropa bella-donna = belladonna). Shipped as the separate pack rose_lotus (export_pack.py lotus).

Names: the English Wikidata label (psilocybin, piperine) when data/lotus/compound_labels.jsonl exists
(tools/wikidata_labels.py), the LOTUS name and Wikidata aliases as synonyms. Organisms without a GRIN
card get a card bio:lotusorg.<name> with kingdom, family and English common names (Wikidata P1843,
data/lotus/organism_labels.jsonl), so that 'liberty cap' finds Psilocybe semilanceata. NCBI taxonomy
(names.dmp / nodes.dmp of the taxdump, public domain; --taxdump) adds common names, scientific synonyms
(Agaricus semilanceatus) and the family or kingdom where LOTUS has none.
Usage: import_lotus.py [--file data/lotus/260413_frozen_metadata.csv.gz] [--dry-run]
"""
import argparse
import csv
import glob
import gzip
import json
import os
import re
import sys

import rose_db as R

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SHOWN = 15


def labels(path):
    out = {}
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                r = json.loads(line)
                out[r["q"]] = r
    return out


def common_names(lab):
    """English common names: P1843 first, else aliases that do not look like a scientific name."""
    seen, out = set(), []
    pool = lab.get("common") or [x for x in lab.get("aliases", []) if not re.match(r"^[A-Z][a-z]+ [a-z-]+", x)]
    for x in pool:
        if x.lower() not in seen:
            seen.add(x.lower())
            out.append(x)
    return out[:5]


def ncbi(taxdump, wanted):
    """NCBI taxdump -> {scientific name: {"common": [...], "synonyms": [...], "family": f, "kingdom": k}}."""
    names, nodes = os.path.join(taxdump, "names.dmp"), os.path.join(taxdump, "nodes.dmp")
    if not os.path.exists(names):
        return {}
    sci, common, syn, sci_of = {}, {}, {}, {}
    with open(names, encoding="utf-8") as fh:
        for line in fh:
            f = [x.strip() for x in line.split("|")]
            tid, name, kind = f[0], f[1], f[3]
            if kind == "scientific name":
                sci_of[tid] = name
                if name in wanted:
                    sci[name] = tid
            elif kind in ("common name", "genbank common name"):
                common.setdefault(tid, []).append(name)
            elif kind in ("synonym", "equivalent name"):
                syn.setdefault(tid, []).append(name)
    parent, rank = {}, {}
    if os.path.exists(nodes):
        with open(nodes, encoding="utf-8") as fh:
            for line in fh:
                f = [x.strip() for x in line.split("|")]
                parent[f[0]], rank[f[0]] = f[1], f[2]

    def up(tid, want):
        for _ in range(60):
            if rank.get(tid) in want:
                return sci_of.get(tid)
            if parent.get(tid) in (None, tid):
                return None
            tid = parent[tid]
        return None
    out = {}
    for name, tid in sci.items():
        out[name] = {"taxid": tid, "common": common.get(tid, []), "synonyms": syn.get(tid, [])[:10],
                     "family": up(tid, ("family",)), "kingdom": up(tid, ("kingdom", "superkingdom", "domain"))}
    return out


def norm_org(name):
    return " ".join(name.lower().replace("-", "").split())


def read(path):
    comp, orgs = {}, {}
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            q = r["structure_wikidata"].rsplit("/", 1)[-1]
            org = r["organism_name"].strip()
            if not q.startswith("Q") or not org:
                continue
            if org not in orgs:
                orgs[org] = {"q": r["organism_wikidata"].rsplit("/", 1)[-1], "kingdom": r["organism_taxonomy_02kingdom"],
                             "family": r["organism_taxonomy_06family"], "n": 0}
            orgs[org]["n"] += 1
            c = comp.get(q)
            if c is None:
                name = (r["structure_nameTraditional"] or r["structure_nameIupac"] or q).strip()
                c = comp[q] = {"name": name, "formula": r["structure_molecular_formula"], "inchikey": r["structure_inchikey"],
                               "npclass": [x for x in (r["structure_taxonomy_npclassifier_01pathway"],
                                                       r["structure_taxonomy_npclassifier_02superclass"],
                                                       r["structure_taxonomy_npclassifier_03class"]) if x],
                               "orgs": {}}
            doi = r["reference_doi"].strip()
            if org not in c["orgs"] or (doi and not c["orgs"][org]):
                c["orgs"][org] = doi
    return comp, orgs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default=(sorted(glob.glob(os.path.join(ROOT, "data", "lotus", "*_frozen_metadata.csv.gz"))) or [None])[-1])
    ap.add_argument("--taxdump", default=os.environ.get("NCBI_TAXDUMP", os.path.expanduser("~/diamond/taxdump")))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    comp, orgs = read(a.file)
    clab = labels(os.path.join(os.path.dirname(a.file), "compound_labels.jsonl"))
    olab = labels(os.path.join(os.path.dirname(a.file), "organism_labels.jsonl"))
    print(f"labels: {len(clab)} compounds, {len(olab)} organisms", flush=True)
    tax = ncbi(a.taxdump, set(orgs))
    print(f"NCBI taxonomy: {len(tax)} of {len(orgs)} organisms", flush=True)
    print(f"LOTUS: {len(comp)} compounds, {sum(len(c['orgs']) for c in comp.values())} compound-organism pairs", flush=True)
    con = R.connect()
    cur = con.cursor()
    cur.execute("SELECT a.value, u.ref FROM rose_alias a JOIN rose_unit u USING (unit_id) "
                "WHERE a.scheme='wikidata' AND u.ref LIKE 'bio:drug.%'")
    drugs = dict(cur.fetchall())
    sid = R.ensure_source(cur, "lotus", "https://doi.org/10.5281/zenodo.19360665", "CC-BY-4.0", False,
                          "LOTUS initiative, frozen dataset union Wikidata (Rutz et al., eLife 2022, "
                          "doi:10.7554/eLife.70780); triplets from Wikidata (CC0)")
    rows, aliases, skipped = [], [], 0
    for q, c in comp.items():
        found = sorted(c["orgs"])
        lab = clab.get(q, {})
        name = lab.get("label") or c["name"]
        syn = [x for x in dict.fromkeys([c["name"]] + lab.get("aliases", [])) if x and x.lower() != name.lower()][:10]
        cls = " / ".join(c["npclass"]) or "natural product"
        intent = (f"{name} - natural product ({cls}; {c['formula']})"
                  + (" [also: " + "; ".join(syn[:5]) + "]" if syn else "")
                  + f", recorded in LOTUS as found in {len(found)} organism(s): " + "; ".join(found[:SHOWN])
                  + (" ..." if len(found) > SHOWN else "")
                  + " [a found-in record can be a trace detection; references per organism on the card]")
        orgs_ = found
        if q in drugs:
            skipped += 1
        payload = {"domain": "chemistry", "status": "defined", "wikidata": q, "formula": c["formula"], "synonyms": syn,
                   "drug_ref": drugs.get(q),
                   "inchikey": c["inchikey"], "npclass": c["npclass"], "found_in": orgs_,
                   "found_in_refs": {o: d for o, d in c["orgs"].items() if d}}
        ref = f"bio:lotus.{q.lower()}"   # not "np": the token would drown "P vs NP"
        rows.append(R.unit_row(ref=ref, kind="bio", name=name, intent=intent, source_id=sid,
                               source_url=f"https://www.wikidata.org/wiki/{q}", payload=payload))
        aliases.append((ref, q, c["inchikey"], None))
    print(f"cards: {len(rows)} ({skipped} of them linked to a bio:drug card)", flush=True)
    # organisms without a GRIN species card
    cur.execute("SELECT value FROM rose_alias WHERE scheme='taxon' AND unit_id NOT IN "
                "(SELECT unit_id FROM rose_unit WHERE source_id=%s)", (sid,))
    grin = {norm_org(v) for (v,) in cur.fetchall()}
    by_org = {}
    for q, c in comp.items():
        for o in c["orgs"]:
            by_org.setdefault(o, []).append(clab.get(q, {}).get("label") or c["name"])
    n_org = 0
    for o, info in sorted(orgs.items()):
        if norm_org(o) in grin:
            continue
        t = tax.get(o, {})
        cn = list(dict((x.lower(), x) for x in reversed(common_names(olab.get(info["q"], {})) + t.get("common", []))).values())[::-1][:6]
        syn = [x for x in t.get("synonyms", []) if x != o]
        info["family"] = info["family"] or t.get("family")
        info["kingdom"] = info["kingdom"] or t.get("kingdom")
        title = o + (f" ({cn[0]})" if cn else "")
        names = sorted(by_org.get(o, []), key=len)[:10]
        intent = (f"{o} - organism ({info['kingdom'] or '?'}; family {info['family'] or '?'})"
                  + (" [common names: " + "; ".join(cn) + "]" if cn else "")
                  + (" [synonyms: " + "; ".join(syn[:5]) + "]" if syn else "")
                  + f"; LOTUS records {len(by_org.get(o, []))} compound(s) in it, e.g. " + "; ".join(names))
        ref = f"bio:lotusorg.{R.slug(o)}"
        rows.append(R.unit_row(ref=ref, kind="bio", name=title, intent=intent, source_id=sid,
                               source_url=f"https://www.wikidata.org/wiki/{info['q']}",
                               payload={"domain": "biology", "status": "defined", "wikidata": info["q"],
                                        "kingdom": info["kingdom"], "family": info["family"], "common_names": cn,
                                        "synonyms": syn, "ncbi_taxid": t.get("taxid"),
                                        "n_compounds": len(by_org.get(o, []))}))
        aliases.append((ref, None, None, o))
        n_org += 1
    print(f"organism cards: {n_org} (not in GRIN)", flush=True)
    if a.dry_run:
        for r in rows[:3]:
            print(r[0], "|", r[3][:300])
        con.rollback()
        return
    for i in range(0, len(rows), 2000):
        R.upsert_units_many(cur, rows[i:i + 2000])
    cur.execute("SELECT ref, unit_id FROM rose_unit WHERE source_id=%s", (sid,))
    uid = dict(cur.fetchall())
    arows = [(s, v, uid[ref]) for ref, q, ik, taxon in aliases
             for s, v in (("wikidata", q), ("inchikey", ik), ("taxon", taxon)) if v]
    for i in range(0, len(arows), 5000):
        cur.executemany("INSERT INTO rose_alias (scheme, value, unit_id) VALUES (%s,%s,%s) "
                        "ON DUPLICATE KEY UPDATE unit_id=VALUES(unit_id)", arows[i:i + 5000])
    R.mark_imported(cur, sid)
    con.commit()
    print("lotus imported:", len(rows), "aliases:", len(arows))


if __name__ == "__main__":
    sys.exit(main())
