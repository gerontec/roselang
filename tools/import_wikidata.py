#!/usr/bin/env python3
"""Import solved (and open) mathematics and physics from Wikidata into the rose_* tables.

Selection (one SPARQL query per class, union of item ids):
  - items with a defining formula (P2534), without individual numbers (primes etc.)
  - theorems (incl. subclasses), conjectures, physical laws, open problems, mathematical problems
  - items with "proved by" (P1318) and parts of problem lists such as the Millennium
    Prize Problems (Q727000)
Details per item come from the Wikidata API (wbgetentities), because SPARQL only
returns rendered MathML while the API returns the TeX source.

kind: open  = negative knowledge: unsolved problem / open conjecture, a hint for the LLM that
              no solution is known; never usable via `use` (compiler error E305)
      law   = physics (dimension or quantity symbols with dimensions, or physical law/quantity)
      const = mathematical or physical constant
      math  = everything else
payload.status: proved | open | defined (formula without a claim of proof)

Usage: import_wikidata.py [--limit N] [--dry-run]
"""
import argparse
import json
import re
import sys
import time

import requests

import rose_db as R

SPARQL = "https://query.wikidata.org/sparql"
API = "https://www.wikidata.org/w/api.php"

NUMBER_CLASSES = "wd:Q49008 wd:Q1989350 wd:Q9300316 wd:Q186875 wd:Q10338607 wd:Q16317911 wd:Q21199 wd:Q77358734"
BIO_FIELDS = ["Q128570", "Q7094", "Q7150", "Q7162", "Q7202", "Q128406", "Q133805", "Q171184", "Q177005",
              "Q214746", "Q222046", "Q323936", "Q471857", "Q815297", "Q840400", "Q908902", "Q31151",
              "Q883112", "Q904564"]
# Smith-Waterman, Needleman-Wunsch, sequence alignment, Michaelis-Menten, Hardy-Weinberg, Mendelian inheritance
BIO_CORE = ["Q1683352", "Q583546", "Q827246", "Q613955", "Q49974", "Q185055"]
SELECTIONS = {
    "formula": f"?i wdt:P2534 ?f . FILTER NOT EXISTS {{ ?i wdt:P31 ?x . VALUES ?x {{ {NUMBER_CLASSES} }} }}",
    "theorem": "?i wdt:P31/wdt:P279* wd:Q65943 .",
    "conjecture": "?i wdt:P31 wd:Q319141 .",
    "physical_law": "?i wdt:P31/wdt:P279* wd:Q214070 .",
    "open_problem": "?i wdt:P31 wd:Q1321906 .",
    "mathematical_problem": "?i wdt:P31 wd:Q1166625 .",
    "proved_by": "?i wdt:P1318 ?b .",
    "problem_list_member": "?i wdt:P361 ?l . VALUES ?l { wd:Q727000 } .",
    # biology: items linked to a biology field (ids verified by label on 2026-11-08) ...
    "bio_field": "?i wdt:P101|wdt:P361|wdt:P921|wdt:P2578|wdt:P1269 ?fld . VALUES ?fld { " + " ".join(
        "wd:" + q for q in BIO_FIELDS) + " } .",
    # ... plus core methods that Wikidata does not link to a field
    "bio_core": "VALUES ?i { " + " ".join("wd:" + q for q in BIO_CORE) + " } .",
}

Q_THEOREM, Q_CONJECTURE, Q_UNSOLVED = "Q65943", "Q319141", "Q1321906"  # theorem, conjecture, open problem
Q_PHYS = {"Q214070", "Q107715", "Q9357058", "Q71550118", "Q2994821"}  # physical law/quantity/theory, ISQ derived/base quantity
Q_CONST = {"Q173227", "Q186509"}  # physical constant, mathematical constant

session = requests.Session()
session.headers["User-Agent"] = R.USER_AGENT


def sparql_ids(where: str) -> list[str]:
    q = f"SELECT DISTINCT ?i WHERE {{ {where} }}"
    for attempt in range(4):
        r = session.get(SPARQL, params={"query": q, "format": "json"}, timeout=120)
        if r.status_code == 429:
            time.sleep(30 * (attempt + 1))
            continue
        r.raise_for_status()
        return [b["i"]["value"].rsplit("/", 1)[1] for b in r.json()["results"]["bindings"]]
    raise RuntimeError("SPARQL rate limited")


def get_entities(ids: list[str], props="labels|descriptions|claims", langs="en") -> dict:
    out = {}
    for k in range(0, len(ids), 50):
        chunk = ids[k:k + 50]
        for attempt in range(5):
            r = session.get(API, params={"action": "wbgetentities", "ids": "|".join(chunk), "props": props,
                                         "languages": langs, "format": "json", "maxlag": 5}, timeout=60)
            if r.status_code in (429, 503) or "error" in r.json() and r.json()["error"].get("code") == "maxlag":
                time.sleep(5 * (attempt + 1))
                continue
            r.raise_for_status()
            out.update(r.json().get("entities", {}))
            break
        time.sleep(0.3)
    return out


def values(claims, prop):
    res = []
    for st in claims.get(prop, []):
        ms = st.get("mainsnak", {})
        if ms.get("snaktype") != "value":
            continue
        res.append((ms["datavalue"]["value"], st.get("qualifiers", {}), st.get("rank")))
    return res


def item_ids(claims, prop):
    return [v["id"] for v, _, rank in values(claims, prop) if isinstance(v, dict) and "id" in v and rank != "deprecated"]


def label(e, lang="en"):
    return (e.get("labels", {}).get(lang) or {}).get("value")


def descr(e, lang="en"):
    return (e.get("descriptions", {}).get(lang) or {}).get("value")


GREEK = {"alpha", "beta", "gamma", "delta", "epsilon", "varepsilon", "zeta", "eta", "theta", "vartheta", "iota",
         "kappa", "lambda", "mu", "nu", "xi", "pi", "rho", "sigma", "tau", "upsilon", "phi", "varphi", "chi",
         "psi", "omega", "Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi", "Sigma", "Phi", "Psi", "Omega"}


def tex_ident(tex: str) -> str:
    """'I_{\\mathrm{v}}' -> 'I_v', '\\Phi_{\\mathrm{v}}' -> 'Phi_v'."""
    t = re.sub(r"\\(mathrm|mathit|mathbf|boldsymbol|vec|mathsf|operatorname|text|bar|hat|tilde|dot)\s*", "", tex)
    t = re.sub(r"\\([A-Za-z]+)", lambda m: m.group(1) if m.group(1) in GREEK else m.group(1), t)
    t = t.replace("'", "_prime").replace("\\prime", "_prime")
    t = re.sub(r"[{}\s\\]", "", t)
    t = re.sub(r"[^A-Za-z0-9_]", "_", t)
    t = re.sub(r"_+", "_", t).strip("_")
    return t or "x"


DIM_MAP = {"L": "L", "M": "M", "T": "T", "I": "I", "Theta": "Th", "Θ": "Th", "N": "N", "J": "J"}


def tex_dim(tex: str) -> str:
    """'\\mathsf{L} \\mathsf{T}^{-1}' -> 'L1 T-1'; '1' -> '1'; unknown -> ''."""
    if not tex:
        return ""
    s = tex.replace("\\,", " ").replace("\\cdot", " ")
    terms = re.findall(r"\\mathsf\{\s*\\?([A-Za-zΘ]+)\s*\}\s*(?:\^\s*\{?\s*([-−]?\d+(?:/\d+)?)\s*\}?)?", s)
    if not terms:
        return "1" if re.fullmatch(r"\s*(1|\\mathsf\{1\})\s*", s) else ""
    acc = {}
    for base, exp in terms:
        b = DIM_MAP.get(base)
        if b is None:
            return ""
        acc[b] = acc.get(b, 0) + int((exp or "1").replace("−", "-").split("/")[0])
    order = ["L", "M", "T", "I", "Th", "N", "J"]
    return " ".join(f"{b}{acc[b]}" for b in order if acc.get(b)) or "1"


def status_of(claims, types):
    if item_ids(claims, "P1318"):
        return "proved"
    if Q_THEOREM in types:
        return "proved"
    for v, q, rank in values(claims, "P31"):
        if isinstance(v, dict) and v.get("id") in (Q_CONJECTURE, Q_UNSOLVED) and "P582" not in q:
            return "open"
    return "defined"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    selected: dict[str, set] = {}
    for name, where in SELECTIONS.items():
        ids = sparql_ids(where)
        print(f"select {name}: {len(ids)}", flush=True)
        for q in ids:
            selected.setdefault(q, set()).add(name)
        time.sleep(2)
    qids = sorted(selected, key=lambda q: int(q[1:]))
    if a.limit:
        qids = qids[:a.limit]
    print(f"items: {len(qids)}", flush=True)

    ents = get_entities(qids)
    print(f"fetched: {len(ents)}", flush=True)

    # referenced items: quantities behind symbols, provers, problem lists, recommended units
    ref_ids = set()
    for e in ents.values():
        c = e.get("claims", {})
        for _, q, _ in values(c, "P7235"):
            for s in q.get("P9758", []):
                if s.get("snaktype") == "value":
                    ref_ids.add(s["datavalue"]["value"]["id"])
        ref_ids.update(item_ids(c, "P1318"))
        ref_ids.update(item_ids(c, "P361"))
        ref_ids.update(item_ids(c, "P8111"))
    ref_ids -= set(ents)
    print(f"referenced items: {len(ref_ids)}", flush=True)
    refs = get_entities(sorted(ref_ids), props="labels|claims", langs="en")
    allents = {**refs, **ents}

    def unit_symbol(qid):
        e = allents.get(qid)
        if not e:
            return ""
        for v, _, _ in values(e.get("claims", {}), "P5061"):
            if isinstance(v, dict) and v.get("text"):
                return v["text"]
        return label(e) or ""

    con = R.connect()
    cur = con.cursor()
    sid = R.ensure_source(cur, "wikidata", "https://www.wikidata.org", "CC0-1.0", False,
                          "defining formulas, theorems, conjectures, physical laws, unsolved problems")
    stats = {"law": 0, "math": 0, "const": 0, "open": 0, "bio": 0, "proved": 0, "open_status": 0, "defined": 0, "skipped": 0}
    for n, q in enumerate(qids, 1):
        e = ents.get(q)
        if not e or "missing" in e:
            stats["skipped"] += 1
            continue
        c = e.get("claims", {})
        en = label(e, "en")
        if not en:  # English only
            stats["skipped"] += 1
            continue
        types = set(item_ids(c, "P31"))
        tex = [v for v, _, rank in values(c, "P2534") if isinstance(v, str) and rank != "deprecated"]
        dim = next((tex_dim(v) for v, _, _ in values(c, "P4020") if isinstance(v, str)), "")
        symbols = []
        for v, qual, rank in values(c, "P7235"):
            if not isinstance(v, str):
                continue
            qty = next((s["datavalue"]["value"]["id"] for s in qual.get("P9758", []) if s.get("snaktype") == "value"), None)
            qe = allents.get(qty, {}) if qty else {}
            qdim = next((tex_dim(x) for x, _, _ in values(qe.get("claims", {}), "P4020") if isinstance(x, str)), "")
            qunit = next((unit_symbol(u) for u in item_ids(qe.get("claims", {}), "P8111")), "")
            symbols.append({"tex": v, "symbol": tex_ident(v), "quantity": qty,
                            "quantity_label": label(qe) if qe else None, "dim": qdim, "unit": qunit})
        status = status_of(c, types)
        if status == "open":
            kind = "open"
        elif types & Q_CONST:
            kind = "const"
        elif dim or types & Q_PHYS or any(s["dim"] for s in symbols):
            kind = "law"
        else:
            kind = "math"
        domain = "physics" if (dim or types & Q_PHYS or any(s["dim"] for s in symbols)) else "math"
        if selected[q] & {"bio_field", "bio_core"}:
            domain = "biology"
            if kind == "math" and not tex:
                kind = "bio"  # a method or concept without equation: reference card
        provers = [{"id": p, "label": label(allents.get(p, {}))} for p in item_ids(c, "P1318")]
        proved_when = None
        for v, qual, _ in values(c, "P1318"):
            for t in qual.get("P585", []):
                if t.get("snaktype") == "value":
                    proved_when = t["datavalue"]["value"]["time"][1:5]
        part_of = [{"id": p, "label": label(allents.get(p, {}))} for p in item_ids(c, "P361")]
        payload = {"wikidata": q, "label": en, "description": descr(e, "en"),
                   "tex": tex, "dim": dim, "symbols": symbols, "types": sorted(types),
                   "status": status, "domain": domain, "proved_by": provers, "proved_year": proved_when,
                   "part_of": part_of, "selected_by": sorted(selected[q])}
        name = en
        intent_parts = [p for p in (en, descr(e, "en")) if p]
        intent = " - ".join(intent_parts)
        if status == "open":
            intent += " [OPEN PROBLEM - no known solution, do not claim or search for a general one]"
        elif provers:
            intent += " [proved by " + ", ".join(p["label"] or p["id"] for p in provers) + "]"
        stats[kind] += 1
        stats["open_status" if status == "open" else status] += 1
        if a.dry_run:
            if n <= 5 or q == "Q203586":
                print(json.dumps({"ref": f"{kind}:{R.slug(name)}", "intent": intent, "payload": payload},
                                 ensure_ascii=False)[:600])
            continue
        hit = R.unit_by_alias(cur, "wikidata", q)
        own = hit[0] if hit else None
        if hit and hit[1].startswith(kind + ":"):
            ref = hit[1]
        else:
            ref = R.free_ref(cur, f"{kind}:{R.slug(name)}", own)
            if own:  # kind changed (e.g. open -> proved): rename the existing unit instead of duplicating it
                cur.execute("UPDATE rose_unit SET ref=%s WHERE unit_id=%s", (ref, own))
        uid = R.upsert_unit(cur, ref=ref, kind=kind, name=name, intent=intent, source_id=sid,
                            source_url=f"https://www.wikidata.org/wiki/{q}", payload=payload)
        R.set_alias(cur, uid, "wikidata", q)
        if symbols:
            R.replace_law_vars(cur, uid, [(s["symbol"], s["quantity_label"], s["unit"], s["dim"], "var")
                                          for s in symbols])
        if n % 500 == 0:
            con.commit()
            print(f"  {n}/{len(qids)} {stats}", flush=True)
    if not a.dry_run:
        R.mark_imported(cur, sid)
        con.commit()
    print("done", stats, flush=True)


if __name__ == "__main__":
    sys.exit(main())
