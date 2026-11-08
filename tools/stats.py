#!/usr/bin/env python3
"""What can be found through Rose: counts of distinct cards and facts in the shipped knowledge
(rose/std: catalog.jsonl, sets/*.jsonl.gz, problems.json, *.rose) plus per-card details from the
corpus database (plant uses, drug-organism records, synonyms). Writes docs/STATISTICS.md.
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


def n(x):
    return f"{x:,}".replace(",", " ")


def gz_lines(name):
    path = os.path.join(STD, "sets", name)
    return [json.loads(l) for l in gzip.open(path, "rt", encoding="utf-8")] if os.path.exists(path) else []


def main():
    cards = [json.loads(l) for l in open(os.path.join(STD, "catalog.jsonl"), encoding="utf-8")]
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
            t = "Botany: plant species with recorded uses or poisons (USDA GRIN, WCVP)"
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
    except Exception as e:                                 # no database: catalog counts only
        detail = {"(detail counts need the corpus database)": type(e).__name__}

    with_tex = sum(1 for c in cards if c.get("tex"))
    with_sig = sum(1 for c in cards if c.get("signature"))
    n_alias = sum(len(c.get("aliases") or []) for c in cards)
    total = len(cards) + len(mathlib) + len(rc)
    out = [f"# What can be found through Rose\n\nCounted in the shipped knowledge (`rose/std/`, build "
           f"{dt.date.today().isoformat()}); generated by `tools/stats.py`. Every count is a distinct card: one "
           "theorem, one plant species, one drug, one package. `rose.exists()` searches all of them.\n",
           f"**{n(total)} searchable cards**: {n(len(cards))} in the catalog, {n(len(mathlib))} mathlib statements, "
           f"{n(len(rc))} Rosetta Code tasks (with {n(n_impl)} Python solutions). In addition {n(n_problems)} "
           f"problem classes recognised by the structure of a task, and {n(sum(rose_src.values()))} units with Rose "
           "source (laws, formulas, constants, open problems) usable in `rosec` programs.\n",
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
    out += ["\n## Not in the package\n",
            "- all ~907 000 PyPI projects: release asset `pypi-2026-11` ([DATASET.md](pypi/DATASET.md))",
            "- OEIS (> 400 000 sequences, CC BY-SA): corpus database only",
            "- the local NCBI nr for homology search: built by the user ([NR_BACKEND.md](bio/NR_BACKEND.md))",
            "\nSources and licences: [`rose/std/LICENSES.md`](../rose/std/LICENSES.md); background: "
            "[CONCEPT.md §6](CONCEPT.md).\n"]
    open(os.path.join(ROOT, "docs", "STATISTICS.md"), "w", encoding="utf-8").write("\n".join(out))
    print("\n".join(out))


if __name__ == "__main__":
    sys.exit(main())
