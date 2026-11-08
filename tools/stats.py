#!/usr/bin/env python3
"""What can be found through Rose: counts of distinct cards and facts in the shipped knowledge
(rose/std: catalog.jsonl.gz, sets/*.jsonl.gz, problems.json, *.rose) and in the optional packs (packs/*/rose_*/
catalog.jsonl, e.g. LOTUS), plus per-card details from the corpus database (plant uses, drug-organism records,
synonyms) and the local-only effect map (rose_compound_effect). Writes docs/STATISTICS.md.
All numbers also go to docs/stats.json; tools/refresh_docs.py puts them into the other docs.
Usage: stats.py   (needs the rose_unit DB for the detail counts, see local.env)"""
import collections
import datetime as dt
import gzip
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
STD = os.path.join(ROOT, "rose", "std")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, ROOT)


def n(x):
    return f"{x:,}".replace(",", " ")


def gz_lines(name):
    path = os.path.join(STD, "sets", name)
    return [json.loads(l) for l in gzip.open(path, "rt", encoding="utf-8")] if os.path.exists(path) else []


def main():
    cards = [json.loads(l) for l in gzip.open(os.path.join(STD, "catalog.jsonl.gz"), "rt", encoding="utf-8")]
    mathlib = gz_lines("mathlib.jsonl.gz")
    rc = gz_lines("rosetta.jsonl.gz")
    rc_impl = gz_lines("rosetta.impl.jsonl.gz")
    problems = json.load(open(os.path.join(STD, "problems.json"), encoding="utf-8"))
    n_problems = len(problems["problems"]) if isinstance(problems, dict) else len(problems)
    rose_src = {f: len(re.findall(r"^\s*(law|const|open|math|fn)\b", open(os.path.join(STD, f), encoding="utf-8").read(), re.M))
                for f in ("law.rose", "math.rose", "open.rose", os.path.join("const", "codata.rose"))
                if os.path.exists(os.path.join(STD, f))}

    by = collections.Counter()
    status = collections.Counter()
    for c in cards:
        ref, src, dom = c["ref"], c["source"], c.get("domain")
        if ref.startswith("bio:taxon."):
            t = "Botany: plant species with recorded economic uses, poisons or protection status (USDA GRIN, WCVP)"
        elif ref.startswith("bio:fact."):
            t = "Facts restated in our own words, with cited sources and evidence level"
        elif ref.startswith("bio:homolog."):
            t = "Biology: protein similarity computed with DIAMOND on NCBI nr"
        elif ref.startswith("bio:drug."):
            t = "Pharmacology: drugs (found in organisms; known before 1982)"
        elif src == "gene_ontology":
            t = "Biology: Gene Ontology terms"
        elif src == "rosalind":
            t = "Biology: Rosalind problems"
        elif c["kind"] == "bio":
            t = "Biology: methods, laws, local nr backend"
        elif src == "pypi" or src == "esphome":
            t = "Software: Python packages (PyPI top 15 000) and firmware building blocks"
        elif src.startswith("py-"):
            t = "Software: solver functions of maintained Python libraries"
        elif src == "modelica":
            t = "Engineering: Modelica Standard Library classes"
        elif c["kind"] in ("ctrl", "machine", "table", "model") or src == "rose-core":
            t = "Engineering: controllers, state machines, decision tables, plant models"
        elif dom == "radio engineering":
            t = "Radio technology"
        elif dom == "social science":
            t = "Social psychology and social dynamics"
        elif c["kind"] == "open":
            t = "Open problems (negative knowledge)"
        elif c["kind"] == "const":
            t = "Physics: constants (CODATA 2022, Wikidata)"
        elif c["kind"] == "law" or dom == "physics":
            t = "Physics: laws and formulas"
        elif c["kind"] == "algo":
            t = "Computer science: algorithms and computational problems"
        else:
            t = "Mathematics: definitions, formulas, theorems (Wikidata)"
        by[t] += 1
        status[c.get("status") or "-"] += 1
    by["Mathematics: proved statements from Lean mathlib4"] += len(mathlib)
    by["Computer science: Rosetta Code tasks"] += len(rc)
    n_impl = sum(len(x.get("impl", [])) for x in rc_impl)
    evidence = collections.Counter(c.get("evidence") for c in cards if c["ref"].startswith("bio:fact."))
    # optional packs
    packs = {}
    for path in sorted(__import__("glob").glob(os.path.join(ROOT, "packs", "*", "rose_*", "catalog.jsonl"))):
        name = os.path.basename(os.path.dirname(path))
        if os.path.exists(os.path.join(STD, "sets", name.replace("rose_", "", 1) + ".jsonl.gz")):
            continue                  # former pack, now a built-in set (already counted above)
        k = collections.Counter()
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                c = json.loads(line)
                k["cards"] += 1
                if c["ref"].startswith("bio:lotus."):
                    k["natural products"] += 1
                    k["compound-organism records"] += len(c.get("found_in") or [])
                    k["records with a reference DOI"] += len(c.get("found_in_refs") or {})
                    k["natural products with synonyms"] += bool(c.get("synonyms"))
                elif c["ref"].startswith("bio:lotusorg."):
                    k["organisms without a GRIN card (fungi, bacteria, animals, plants)"] += 1
                    k["organisms with an English common name"] += bool(c.get("common_names"))
        packs[name] = k

    # detail facts from the corpus database (the catalog keeps only the text of these)
    detail = {}
    try:
        import rose_db as R
        cur = R.connect().cursor()
        cur.execute("SELECT u.ref, u.payload FROM rose_unit u WHERE u.ref LIKE 'bio:taxon.%' OR u.ref LIKE 'bio:drug.%'")
        uses, food, poison, both, syn, cn, pairs, refd, unsourced, old, atc1 = (collections.Counter() for _ in range(11))
        for ref, p in cur.fetchall():
            p = json.loads(p or "{}")
            if ref.startswith("bio:taxon."):
                u = p.get("uses") or {}
                uses["records"] += sum(len(v) for v in u.values())
                food["n"] += "human food" in u
                poison["n"] += "poison" in u
                both["n"] += "human food" in u and "poison" in u
                syn["n"] += len(p.get("synonyms") or [])
                cn["n"] += len(p.get("common_names") or [])
            else:
                pairs["n"] += len(p.get("found_in") or [])
                unsourced["n"] += len(p.get("found_in_unsourced") or [])
                refd["n"] += len(p.get("found_in_refs") or {})
                old["n"] += bool(p.get("approved_us_before_1982"))
                for code in {a[0] for a in p.get("atc") or []}:
                    atc1[code] += 1
        detail = {"plant use records": uses["records"], "plant species recorded as human food": food["n"],
                  "plant species recorded as poisonous": poison["n"], "plant species recorded as both": both["n"],
                  "plant synonyms (WCVP)": syn["n"], "plant common names (English)": cn["n"],
                  "drug-organism records with a reference": pairs["n"],
                  "drug-organism records without a reference (shown as unconfirmed)": unsourced["n"],
                  "drugs with US approval before 1982": old["n"],
                  "ATC main groups covered": len(atc1)}
        cur.execute("SELECT payload FROM rose_unit WHERE ref LIKE 'bio:taxon.%'")
        prot = collections.Counter()
        for (p,) in cur.fetchall():
            for x in json.loads(p or "{}").get("protection") or []:
                prot[x] += 1
        detail.update({f"plant species with protection status {k}": v for k, v in sorted(prot.items())})
        effect = []
        try:
            cur.execute("SELECT e.kind, ce.source, COUNT(DISTINCT e.effect_id), COUNT(*), COUNT(DISTINCT ce.compound_id) "
                        "FROM rose_compound_effect ce JOIN rose_effect e USING (effect_id) GROUP BY e.kind, ce.source "
                        "ORDER BY e.kind, ce.source")
            effect = cur.fetchall()
            cur.execute("SELECT (SELECT COUNT(*) FROM rose_organism), (SELECT COUNT(*) FROM rose_compound), "
                        "(SELECT COUNT(*) FROM rose_compound_organism)")
            effect_tot = cur.fetchone()
        except Exception:
            effect_tot = None
    except Exception as e:                                 # no database: catalog counts only
        detail = {"(detail counts need the corpus database)": type(e).__name__}
        effect, effect_tot = [], None

    with_tex = sum(1 for c in cards if c.get("tex"))
    with_sig = sum(1 for c in cards if c.get("signature"))
    n_alias = sum(len(c.get("aliases") or []) for c in cards)
    total = len(cards) + len(mathlib) + len(rc)
    n_pack = sum(k["cards"] for k in packs.values())
    src = collections.Counter(c["source"] for c in cards)
    drugs = [c for c in cards if c["ref"].startswith("bio:drug.")]
    S = {"date": dt.date.today().isoformat(), "total_cards": total, "catalog_cards": len(cards),
         "mathlib_cards": len(mathlib), "rosetta_tasks": len(rc), "rosetta_solutions": n_impl,
         "problem_classes": n_problems, "rose_source_units": sum(rose_src.values()), "pack_cards": n_pack,
         "total_with_packs": total + n_pack, "aliases": n_alias,
         "source": dict(src), "py_library_functions": sum(v for k, v in src.items() if k.startswith("py-")),
         "drugs_found_in": None, "drugs_only_unsourced": None,     # from the corpus database below
         "radio_cards": sum(1 for c in cards if c.get("domain") == "radio engineering" and c["source"] == "wikidata"),
         "social_cards": sum(1 for c in cards if c.get("domain") == "social science" and c["source"] == "wikidata"),
         "social_concepts": sum(1 for c in cards if c.get("domain") == "social science" and c["source"] == "wikidata"
                                and c["kind"] != "algo"),
         "social_procedures": sum(1 for c in cards if c.get("domain") == "social science" and c["source"] == "wikidata"
                                  and c["kind"] == "algo"),
         "social_solvers": sum(1 for c in cards if c.get("domain") == "social science" and c["source"].startswith("py-")),
         "detail": {k: v for k, v in detail.items() if isinstance(v, int)},
         "packs": {k: dict(v) for k, v in packs.items()}, "by_topic": dict(by), "status": dict(status)}
    S["wikidata_radio_social"] = S["radio_cards"] + S["social_cards"]
    S["wikidata_knowledge"] = src.get("wikidata", 0) - S["wikidata_radio_social"] - sum(
        1 for c in drugs if c["source"] == "wikidata")
    S["rose_core"] = src.get("rose-core", 0) + n_problems
    S["grin_species"] = src.get("grin", 0)
    for k, key in (("plant species recorded as human food", "grin_food"), ("plant species recorded as poisonous", "grin_poison"),
                   ("plant species recorded as both", "grin_both")):
        S[key] = detail.get(k)

    S["total_cards_round"] = round(total, -3)
    m7 = os.path.join(ROOT, "bench", "m7_results", "rose.json")
    if os.path.exists(m7):
        r = json.load(open(m7, encoding="utf-8"))
        S["m7_rose"] = f"{sum(1 for x in r if x.get('ok'))}/{len(r)}"
    try:
        cur.execute("SELECT COUNT(*) FROM rose_unit")
        S["corpus_units"] = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM rose_unit u JOIN rose_source s USING (source_id) WHERE s.name='oeis'")
        S["oeis_sequences"] = cur.fetchone()[0]
        cur.execute("SELECT s.name, COUNT(*) FROM rose_unit u JOIN rose_source s USING (source_id) GROUP BY s.name")
        S["db_source"] = {k: int(v) for k, v in cur.fetchall()}
        cur.execute("SELECT SUM(ref LIKE 'bio:lotus.%%'), SUM(ref LIKE 'bio:lotusorg.%%') FROM rose_unit")
        S["lotus_compounds"], S["lotus_organisms"] = (int(x or 0) for x in cur.fetchone())
        cur.execute("SELECT payload FROM rose_unit WHERE ref LIKE 'bio:drug.%%'")
        fi = [json.loads(p or "{}") for (p,) in cur.fetchall()]
        S["drugs_found_in"] = sum(1 for p in fi if p.get("found_in") or p.get("found_in_unsourced"))
        S["drugs_only_unsourced"] = sum(1 for p in fi if p.get("found_in_unsourced") and not p.get("found_in"))
        S["corpus_units_round"] = round(S["corpus_units"], -3)
    except Exception:
        pass
    from rose import knowledge as K                         # index size: the unpacked core index, if built
    try:
        key = open(K.PREBUILT_KEY).read().strip()
        idx = os.path.join(K.cache_dir(), f"knowledge-{key}.sqlite")
        if os.path.exists(idx):
            S["index_mb"] = round(os.path.getsize(idx) / 1e6)
    except OSError:
        pass
    S["effect_map"] = {"organisms": effect_tot[0], "compounds": effect_tot[1], "compound_organism": effect_tot[2],
                       "effects": [list(map(lambda x: x if isinstance(x, (int, str)) else int(x), r)) for r in effect]} \
        if effect_tot else None
    out = [f"# What can be found through Rose\n\nCounted in the shipped knowledge (`rose/std/`, build "
           f"{dt.date.today().isoformat()}); generated by `tools/stats.py`. Every count is a distinct card: one "
           "theorem, one plant species, one drug, one package. `rose.exists()` searches all of them.\n",
           f"**{n(total)} searchable cards**: {n(len(cards))} in the catalog, {n(len(mathlib))} mathlib statements, "
           f"{n(len(rc))} Rosetta Code tasks (with {n(n_impl)} Python solutions). In addition {n(n_problems)} "
           f"problem classes recognised by the structure of a task, and {n(sum(rose_src.values()))} units with Rose "
           "source (laws, formulas, constants, open problems) usable in `rosec` programs."
           + "\n",
           "## By topic\n\n| Topic | Cards |\n|---|---:|"]
    out += [f"| {t} | {n(v)} |" for t, v in sorted(by.items(), key=lambda x: -x[1])]
    out += ["\n## By what the verdict can say\n",
            "| Status of the card | Cards | Verdict when it is the best match |\n|---|---:|---|"]
    verdict = {"solved": "solved (a maintained solution or package exists)", "proved": "solved (theorem with proof)",
               "defined": "solved (definition, formula, method)", "open": "**open** – no known solution",
               "caution": "**caution** – food or poison records, never a confirmation of safety",
               "disputed": "**disputed** – proposed, without established empirical support", "-": "solved (reference)"}
    out += [f"| {s} | {n(v)} | {verdict.get(s, s)} |" for s, v in sorted(status.items(), key=lambda x: -x[1])]
    out += ["\nNothing found → verdict **unknown**.\n", "## Distinct facts\n\n| Fact | Count |\n|---|---:|",
            f"| cards with a formula (TeX) | {n(with_tex)} |", f"| cards with a signature | {n(with_sig)} |",
            f"| aliases in the catalog (Wikidata ids, synonyms) | {n(n_alias)} |"]
    out += [f"| {k} | {n(v) if isinstance(v, int) else v} |" for k, v in detail.items()]
    out += [f"| fact cards with evidence '{k}' | {n(v)} |" for k, v in sorted(evidence.items(), key=lambda x: str(x[0]))]
    if effect_tot:
        out += ["\n## Local only: effect → compound → organism (MariaDB)\n",
                "Not part of the Python module. Built by `tools/build_effect_map.py` from the corpus (LOTUS, GRIN, "
                "drug cards) and `tools/import_chembl_effects.py` from a local ChEMBL copy, next to the DIAMOND "
                "tables (`blast_*`), "
                "into the tables `rose_effect`, `rose_compound`, `rose_organism`, `rose_compound_effect`, "
                "`rose_compound_organism` and the view `rose_v_effect_compound_organism`. Not shipped: rows from "
                "share-alike sources (ChEMBL) stay in the local database (CONCEPT.md P12).\n",
                f"{n(effect_tot[0])} organisms, {n(effect_tot[1])} compounds, {n(effect_tot[2])} compound-organism records.\n",
                "| Effect kind | Source | Effects | Links | Compounds |\n|---|---|---:|---:|---:|"]
        out += [f"| {kind} | {src} | {n(a)} | {n(b)} | {n(c)} |" for kind, src, a, b, c in effect]
    out += ["\n## Not in the package\n",
            "- all ~907 000 PyPI projects: release asset `pypi-2026-11` ([DATASET.md](pypi/DATASET.md))",
            "- OEIS (> 400 000 sequences, CC BY-SA): corpus database only",
            "- LOTUS natural products (CC BY 4.0): corpus database and the local effect map only",
            "- ChEMBL (CC BY-SA): local MariaDB only, never exported",
            "- the local NCBI nr for homology search: built by the user ([NR_BACKEND.md](bio/NR_BACKEND.md))",
            "\nSources and licences: [`rose/std/LICENSES.md`](../rose/std/LICENSES.md); background: "
            "[CONCEPT.md §6](CONCEPT.md).\n"]
    open(os.path.join(ROOT, "docs", "STATISTICS.md"), "w", encoding="utf-8").write("\n".join(out))
    with open(os.path.join(ROOT, "docs", "stats.json"), "w", encoding="utf-8") as fh:
        json.dump(S, fh, ensure_ascii=False, indent=1, sort_keys=True, default=int)
    return S


if __name__ == "__main__":
    main()
