"""Specification matching (Zaremski & Wing): recognise a known problem class from the STRUCTURE of a
task - what is given, what is wanted, what is optimised, which constraints hold - not from its name.

A task text is mapped onto a controlled vocabulary of facets (rose/std/problems.json, "facets":
regular expressions, English and German). A problem class requires groups of facets (each group:
any one of its facets), may forbid facets (one vehicle vs. a fleet: TSP vs. VRP) and lists optional
facets as tie-breakers. score = share of required groups present, halved by a forbidden facet.

    match("plan a tour for a delivery van that visits 30 customers and returns to the depot ...")
    -> travelling_salesperson 1.0 (locations, tour, return, visit_all, minimise)
"""
import json
import os
import re

from . import std

PROBLEMS = os.path.join(std.STD, "problems.json")
_data = None


def data():
    global _data
    if _data is None:
        with open(PROBLEMS, encoding="utf-8") as f:
            d = json.load(f)
        d["_re"] = {k: re.compile(v, re.I) for k, v in d["facets"].items()}
        _data = d
    return _data


def facets(text):
    """Facets present in a task text, with the matched words as evidence."""
    out = {}
    for name, rx in data()["_re"].items():
        m = rx.search(text)
        if m:
            out[name] = m.group(0)
    return out


def match(text, k=5):
    found = facets(text)
    res = []
    for p in data()["problems"]:
        req = p["requires"]
        sat = [g for g in req if any(f in found for f in g)]
        score = len(sat) / len(req) if req else 0.0
        bad = [f for f in p.get("forbids", []) if f in found]
        if bad:
            score *= 0.5
        score += 0.02 * sum(f in found for f in p.get("optional", []))
        if score > 0:
            res.append({"id": p["id"], "ref": "problem:" + p["id"], "score": round(score, 3),
                        "matched": sorted({f for g in sat for f in g if f in found}), "forbidden": bad,
                        "missing": [g for g in req if g not in sat]})
    res.sort(key=lambda r: -r["score"])
    return res[:k], found


def cards():
    """Problem classes as knowledge cards (kind algo, source rose-core, MIT)."""
    for p in data()["problems"]:
        solvers = "; ".join(f"{s['name']} ({s['use']})" for s in p.get("solvers", []))
        intent = f"{p['name']} - {p['description']}"
        if p.get("aliases"):
            intent += " [also: " + "; ".join(p["aliases"]) + "]"
        intent += f" [{p['complexity']}] [solved by: {solvers}]"
        yield {"ref": "problem:" + p["id"], "kind": p.get("kind", "algo"), "name": p["name"], "intent": intent,
               "level": "imported", "source": "rose-core", "license": "MIT", "url": None, "std": False,
               "complexity": p["complexity"], "solvers": p.get("solvers", []), "see": p.get("see", []),
               "requires": p["requires"], "status": "defined", "domain": "computer science"}
