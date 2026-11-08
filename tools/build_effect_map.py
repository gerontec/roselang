#!/usr/bin/env python3
"""Effect -> compound -> organism in MariaDB (tables rose_organism, rose_compound, rose_effect,
rose_compound_organism, rose_compound_effect, view rose_v_effect_compound_organism; DDL in
tools/sql/effect_map.sql). Built from the Rose corpus and rebuilt completely on every run:

  organisms         GRIN species cards (bio:taxon.*) and LOTUS organism cards (bio:lotusorg.*)
  compounds         drug cards (bio:drug.*, Wikidata/Orange Book) and LOTUS natural products (bio:lotus.*)
  compound-organism found_in of every compound card (LOTUS with one DOI per organism; Wikidata P703,
                    claims without a reference flagged sourced=0)
  effects           ATC groups of the drug cards (kind therapeutic_class, CC0) and measured effects on
                    human proteins from facts/targets/*.tsv (kind target; single facts, P12)

Example:
  SELECT DISTINCT organism FROM rose_v_effect_compound_organism WHERE effect='antimalarial';
Usage: build_effect_map.py
"""
import csv
import glob
import json
import os
import sys

import rose_db as R

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TABLES = ("rose_compound_effect", "rose_compound_organism", "rose_effect", "rose_compound", "rose_organism")


def ddl(cur):
    sql = open(os.path.join(ROOT, "tools", "sql", "effect_map.sql"), encoding="utf-8").read()
    for stmt in [s.strip() for s in sql.split(";\n") if s.strip()]:
        body = "\n".join(l for l in stmt.splitlines() if not l.strip().startswith("--")).strip()
        if body:
            cur.execute(body)


def norm_org(name):
    """Atropa bella-donna = Atropa belladonna: case and hyphens do not count."""
    return " ".join(name.lower().replace("-", "").split())


def first_doi(v):
    if isinstance(v, str):
        return v or None
    if isinstance(v, dict):
        return v.get("doi") or v.get("url")
    if isinstance(v, list) and v:
        return first_doi(v[0])
    return None


def main():
    con = R.connect()
    cur = con.cursor()
    ddl(cur)
    for t in TABLES:
        cur.execute(f"DELETE FROM {t}")
    con.commit()
    # ---- organisms
    org_id = {}
    cur.execute("SELECT u.ref, u.payload, a.value FROM rose_unit u JOIN rose_alias a USING (unit_id) "
                "WHERE a.scheme='taxon' AND (u.ref LIKE 'bio:taxon.%' OR u.ref LIKE 'bio:lotusorg.%')")
    rows = []
    for ref, payload, name in cur.fetchall():
        p = json.loads(payload or "{}")
        cn = (p.get("common_names") or [None])[0]
        rows.append((name[:255], cn[:255] if cn else None, p.get("kingdom") or ("Plantae" if ref.startswith("bio:taxon.") else None),
                     p.get("family"), p.get("ncbi_taxid"), p.get("wikidata"), ref))
    cur.executemany("INSERT IGNORE INTO rose_organism (name, common_name, kingdom, family, ncbi_taxid, wikidata, ref) "
                    "VALUES (%s,%s,%s,%s,%s,%s,%s)", rows)
    cur.execute("SELECT name, organism_id FROM rose_organism")
    org_id = {norm_org(k): v for k, v in cur.fetchall()}
    print("organisms with a card:", len(org_id), flush=True)
    # ---- compounds
    cur.execute("SELECT ref, name, payload FROM rose_unit WHERE ref LIKE 'bio:drug.%' OR ref LIKE 'bio:lotus.%'")
    comps = cur.fetchall()
    drug_refs = {ref for ref, _, _ in comps if ref.startswith("bio:drug.")}
    owner = {}                                   # a LOTUS card of a drug counts as the drug (its organisms, InChIKey)
    inchikey = {}
    for ref, name, payload in comps:
        p = json.loads(payload or "{}")
        d = p.get("drug_ref")
        owner[ref] = d if d in drug_refs else ref
        if p.get("inchikey"):
            inchikey.setdefault(owner[ref], p["inchikey"])
    cur.executemany("INSERT INTO rose_compound (name, wikidata, inchikey, atc, ref) VALUES (%s,%s,%s,%s,%s)",
                    [(name[:255], (p := json.loads(payload or "{}")).get("wikidata"), inchikey.get(ref),
                      ",".join(p.get("atc") or []) or None, ref) for ref, name, payload in comps if owner[ref] == ref])
    cur.execute("SELECT ref, compound_id FROM rose_compound")
    comp_id = dict(cur.fetchall())
    print("compounds:", len(comp_id), flush=True)
    # ---- compound <-> organism (organisms named only in found_in get a row without a card)
    pairs, effects_class = [], []
    for ref, name, payload in comps:
        p = json.loads(payload or "{}")
        refs = p.get("found_in_refs") or {}
        src = "lotus" if ref.startswith("bio:lotus.") else "wikidata"
        for key, sourced in (("found_in", 1), ("found_in_unsourced", 0)):
            for o in p.get(key) or []:
                pairs.append((comp_id[owner[ref]], o[:255], first_doi(refs.get(o)), sourced, src))
        for g in p.get("atc_groups") or []:
            code, _, label = g.partition(" ")
            effects_class.append((comp_id[owner[ref]], code, label or code))
    missing = sorted({norm_org(o): o for _, o, _, _, _ in pairs if norm_org(o) not in org_id}.values())
    cur.executemany("INSERT IGNORE INTO rose_organism (name) VALUES (%s)", [(o,) for o in missing])
    cur.execute("SELECT name, organism_id FROM rose_organism")
    org_id = {norm_org(k): v for k, v in cur.fetchall()}
    rows = [(c, org_id[norm_org(o)], d, s, src) for c, o, d, s, src in pairs if norm_org(o) in org_id]
    for i in range(0, len(rows), 20000):
        cur.executemany("INSERT IGNORE INTO rose_compound_organism (compound_id, organism_id, reference_doi, sourced, source) "
                        "VALUES (%s,%s,%s,%s,%s)", rows[i:i + 20000])
    print("compound-organism pairs:", len(rows), "(organisms without a card:", len(missing), ")", flush=True)
    # ---- effects: ATC groups
    cur.executemany("INSERT IGNORE INTO rose_effect (kind, name, code) VALUES ('therapeutic_class', %s, %s)",
                    sorted({(label, code) for _, code, label in effects_class}))
    cur.execute("SELECT name, effect_id FROM rose_effect WHERE kind='therapeutic_class'")
    eff = dict(cur.fetchall())
    cur.executemany("INSERT IGNORE INTO rose_compound_effect (compound_id, effect_id, relation, evidence, reference, source) "
                    "VALUES (%s,%s,'class','regulatory',%s,'atc')",
                    [(c, eff[label], f"ATC {code}") for c, code, label in effects_class])
    print("ATC class links:", len(effects_class), flush=True)
    # ---- effects: measured targets (facts/targets/*.tsv)
    n = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "facts", "targets", "*.tsv"))):
        with open(path, encoding="utf-8") as fh:
            lines = [l for l in fh if l.strip() and not l.startswith("#")]
        for f in csv.reader(lines, delimiter="\t"):
            comp, target, code, chembl, relation, measure, vmin, vmax, system, evidence, reference = (x.strip() for x in f)
            cur.execute("SELECT compound_id FROM rose_compound WHERE LOWER(name)=LOWER(%s) ORDER BY ref LIMIT 1", (comp,))
            hit = cur.fetchone()
            if not hit:
                print(f"{path}: compound '{comp}' not found - skipped", file=sys.stderr)
                continue
            cur.execute("INSERT INTO rose_effect (kind, name, code, chembl_target) VALUES ('target',%s,%s,%s) "
                        "ON DUPLICATE KEY UPDATE effect_id=LAST_INSERT_ID(effect_id)", (target, code or None, chembl or None))
            cur.execute("INSERT IGNORE INTO rose_compound_effect (compound_id, effect_id, relation, measure, value_um_min, "
                        "value_um_max, test_system, evidence, reference, source) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,'rose-facts')",
                        (hit[0], cur.lastrowid, relation, measure or None, float(vmin) if vmin else None,
                         float(vmax) if vmax else None, system or None, evidence or None, reference))
            n += 1
    print("measured target links:", n, flush=True)
    con.commit()


if __name__ == "__main__":
    sys.exit(main())
