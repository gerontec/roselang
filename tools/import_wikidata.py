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
payload.status: proved | open | defined (formula without a claim of proof) | disputed (proposed
                without established empirical support: by hand with a source, or instance of pseudoscience)

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
# algorithm, method, theory, concept, phenomenon, mode of inheritance, ecological concept, equation,
# formula, physical law, theorem, scientific law, mathematical model (all verified by label 2026-11-08)
BIO_KNOWLEDGE_CLASSES = ["Q8366", "Q1799072", "Q17737", "Q151885", "Q483247", "Q1348351", "Q56575300",
                         "Q11345", "Q976981", "Q214070", "Q65943", "Q408891", "Q486902"]
# Smith-Waterman, Needleman-Wunsch, sequence alignment, Michaelis-Menten, Hardy-Weinberg, Mendelian inheritance
BIO_CORE = ["Q1683352", "Q583546", "Q827246", "Q613955", "Q49974", "Q185055"]
# core concepts of control, state machines and decision logic -> Rose kind (ids verified by label)
CORE_KIND = {
    "ctrl": {"Q716829", "Q818544", "Q230945", "Q334269", "Q48995591"},   # PID, observer, state space, transfer fn, loop
    "machine": {"Q176452", "Q1126309", "Q640119", "Q230885", "Q724168"},  # FSM, Mealy, Moore, state diagram, Petri net
    "table": {"Q747762", "Q24962978", "Q461528", "Q864155", "Q6667469"},  # decision table, DMN, Karnaugh, BDD, logic opt.
}
# radio technology (ids verified by label 2026-11-08): wireless network Q11375, modulation Q170474,
# multiplexing Q222903, channel access method Q1665191, spread spectrum Q958957, radio propagation
# model Q7281192, antenna Q131214, mobile phone network standard Q26763979, LPWAN Q20706829; fields
# telecommunications engineering Q1061219, radio-frequency engineering Q1363977, wireless communication
# Q249, radio Q872, radio propagation Q1474701
RADIO_CORE = ["Q199324", "Q1638779", "Q29643", "Q79703", "Q25021569", "Q135803", "Q19686539",   # Zigbee, BLE, Wi-Fi, LTE, NB-IoT, Z-Wave, LoRaWAN
              "Q477992", "Q601459", "Q1455719", "Q5680855", "Q1509342", "Q1474701",            # FSPL, Friis, Fresnel zone, Hata, link budget, propagation
              "Q1331892", "Q944633", "Q294502", "Q375889", "Q1074780", "Q1756194",             # SDR, CSMA/CA, ALOHAnet, OFDM, chirp spread spectrum, Shannon-Hartley
              "Q20706829", "Q222903", "Q1665191", "Q170474", "Q1363977", "Q249", "Q131214", "Q11375"]
# knowledge classes for the field selection: the BIO list plus technical standard, communication
# protocol, technique, computer network protocol, specification (verified by label 2026-11-08)
RADIO_KNOWLEDGE_CLASSES = BIO_KNOWLEDGE_CLASSES + ["Q317623", "Q132364", "Q2695280", "Q15836568", "Q2101564"]
# no people, organisations, businesses, manufactured products, or single installations and networks
# (anything with a country or coordinates)
NOT_KNOWLEDGE = ("FILTER NOT EXISTS { ?i wdt:P31 ?no . VALUES ?no { wd:Q5 wd:Q43229 wd:Q4830453 } } "
                 "FILTER NOT EXISTS { ?i wdt:P176|wdt:P17|wdt:P625 ?m }")
# social psychology and social dynamics (ids verified by label 2026-11-08): fields social psychology
# Q161272, crowd psychology Q1355183, mass psychology Q16622884, opinion dynamics Q101247857,
# sociology Q21201; classes social phenomenon Q602884 (instances only - its subclass tree is 14 000
# items of everything), cognitive bias Q1127759, threshold model Q7798106, voter model Q7942158
SOCIAL_CORE = ["Q110489961", "Q110489954", "Q16622884", "Q1355183", "Q101247857", "Q106283193",   # mass formation, m.f. psychosis, mass/crowd psychology, opinion dynamics, social contagion
               "Q7798106", "Q7942158", "Q5243912", "Q778684", "Q191474", "Q540742", "Q751414",     # threshold model, voter model, DeGroot learning, Asch, Milgram, spiral of silence, groupthink
               "Q6031027", "Q955199", "Q2914277", "Q4532199", "Q128135", "Q1307337", "Q221284", "Q161272"]  # cascade, bandwagon, moral panic, sociogenic illness, totalitarianism, influence, conformity
SOCIAL_KNOWLEDGE_CLASSES = BIO_KNOWLEDGE_CLASSES + ["Q602884", "Q3249551"]   # + social phenomenon, process
# social procedures and algorithms (ids verified by label 2026-11-08): electoral system Q182985, fair division
# problem Q1511081, solution concept Q780008, agent-based model Q392811, compartmental models in epidemiology
# Q2572354, epidemiological modeling Q990044; fields game theory Q44455, opinion dynamics Q101247857, social
# network analysis Q7551269
SOCIAL_ALGO_CLASSES = ["Q182985", "Q1511081", "Q780008", "Q392811", "Q2572354", "Q990044"]
SOCIAL_ALGO_FIELDS = ["Q44455", "Q101247857", "Q7551269"]
# constituencies and single elections are instances of electoral-system classes too: they have a place
# (P131 located in, P625 coordinates, P276 location) or a date (P585 point in time) - procedures have neither
# ... and by class (ids verified by label 2026-11-08): constituency of the House of Commons Q27971968, single-member
# district Q1052894, constituencies of the Parliament / Legislative Assembly of Singapore Q5163953 / Q136093601,
# public election Q40231
NOT_PLACE_OR_EVENT = ("FILTER NOT EXISTS { ?i wdt:P131|wdt:P625|wdt:P276|wdt:P585 ?pe . } "
                      "FILTER NOT EXISTS { ?i wdt:P31 ?ce . VALUES ?ce { wd:Q27971968 wd:Q1052894 wd:Q5163953 "
                      "wd:Q136093601 } } FILTER NOT EXISTS { ?i wdt:P31/wdt:P279* wd:Q40231 . } ")
NOT_KNOWLEDGE_SOCIAL = ("FILTER NOT EXISTS { ?i wdt:P31 ?no . VALUES ?no { wd:Q5 wd:Q43229 wd:Q4830453 wd:Q13442814 wd:Q571 } } "
                        "FILTER NOT EXISTS { ?i wdt:P176|wdt:P17|wdt:P625 ?m }")    # + scholarly articles, books
# disputed: proposed concepts without empirical support - status 'disputed', the verdict says so.
# Set by hand with a source, or by Wikidata 'instance of pseudoscience' (Q483677).
DISPUTED = {
    "Q110489954": "not a diagnosis (not in the DSM); experts asked by Reuters (2022) found no evidence for it; "
                  "social psychologist Steve Reicher: 'more metaphor than science, more ideology than fact' "
                  "(source: https://en.wikipedia.org/wiki/Robert_W._Malone); popularised on a podcast in "
                  "December 2021; linked in public debate to Mattias Desmet's mass formation theory",
}
Q_PSEUDOSCIENCE = "Q483677"
# notes added to a card's intent (facts with a source, not a judgement of the concept)
NOTES = {
    "Q110489961": "classical concept of crowd psychology (Le Bon, Freud); its application to the COVID-19 "
                  "pandemic by the Belgian psychologist Mattias Desmet (The Psychology of Totalitarianism, 2022) "
                  "is disputed - see mass formation psychosis",
}
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
    # only knowledge classes (whitelist): projects, trials, journals, people, genes etc. stay out
    "bio_field": "?i wdt:P101|wdt:P361|wdt:P921|wdt:P2578|wdt:P1269 ?fld . VALUES ?fld { " + " ".join(
        "wd:" + q for q in BIO_FIELDS) + " } . ?i wdt:P31 ?k . VALUES ?k { " + " ".join(
        "wd:" + q for q in BIO_KNOWLEDGE_CLASSES) + " } .",
    # ... plus core methods that Wikidata does not link to a field
    "bio_core": "VALUES ?i { " + " ".join("wd:" + q for q in BIO_CORE) + " } .",
    # algorithms and computational problems (ids verified by label 2026-11-08): algorithm Q8366,
    # computational problem Q3435924, optimization problem Q984063 - e.g. travelling salesperson
    "algorithm": "?i wdt:P31/wdt:P279* wd:Q8366 .",
    "computational_problem": "?i wdt:P31/wdt:P279* wd:Q3435924 .",
    "optimization_problem": "?i wdt:P31/wdt:P279* wd:Q984063 .",
    # control engineering, automata, decision logic (ids verified by label 2026-11-08): fields control
    # theory Q6501221 and automata theory Q214526 (knowledge classes only), models of computation
    # Q2651576, finite-state machine family Q176452, plus core concepts by id
    "ctrl_field": "?i wdt:P101|wdt:P361|wdt:P921|wdt:P2578|wdt:P2579 wd:Q6501221 . ?i wdt:P31 ?k . VALUES ?k { "
                  + " ".join("wd:" + q for q in BIO_KNOWLEDGE_CLASSES) + " } .",
    "machine_field": "?i wdt:P101|wdt:P361|wdt:P921|wdt:P2578|wdt:P2579 wd:Q214526 . ?i wdt:P31 ?k . VALUES ?k { "
                     + " ".join("wd:" + q for q in BIO_KNOWLEDGE_CLASSES) + " } .",
    "machine_model": "{ ?i wdt:P31/wdt:P279* wd:Q2651576 . } UNION { ?i wdt:P279* wd:Q176452 . }",
    "radio_class": "{ ?i wdt:P279+ wd:Q11375 . } UNION "
                   "{ ?i wdt:P279+ wd:Q170474 . } UNION { ?i wdt:P279+ wd:Q222903 . } UNION { ?i wdt:P279+ wd:Q1665191 . } "
                   "UNION { ?i wdt:P31 wd:Q1665191 . } UNION { ?i wdt:P279* wd:Q958957 . } UNION "
                   "{ ?i wdt:P31/wdt:P279* wd:Q7281192 . } UNION { ?i wdt:P279+ wd:Q7281192 . } UNION "
                   "{ ?i wdt:P279+ wd:Q131214 . } UNION { ?i wdt:P31/wdt:P279* wd:Q26763979 . } UNION "
                   "{ ?i wdt:P279+ wd:Q20706829 . } UNION { ?i wdt:P31 wd:Q20706829 . } " + NOT_KNOWLEDGE,
    "radio_field": "?i wdt:P101|wdt:P361|wdt:P921|wdt:P2578|wdt:P2579 ?fld . VALUES ?fld { wd:Q1061219 wd:Q1363977 "
                   "wd:Q249 wd:Q872 wd:Q1474701 } . ?i wdt:P31 ?k . VALUES ?k { " + " ".join(
                       "wd:" + q for q in RADIO_KNOWLEDGE_CLASSES) + " } . " + NOT_KNOWLEDGE,
    "radio_core": "VALUES ?i { " + " ".join("wd:" + q for q in RADIO_CORE) + " } .",
    "social_field": "?i wdt:P101|wdt:P361|wdt:P921|wdt:P2578|wdt:P2579|wdt:P279 ?fld . VALUES ?fld { wd:Q161272 "
                    "wd:Q1355183 wd:Q16622884 wd:Q101247857 } . ?i wdt:P31 ?k . VALUES ?k { " + " ".join(
                        "wd:" + q for q in SOCIAL_KNOWLEDGE_CLASSES) + " } . " + NOT_KNOWLEDGE_SOCIAL,
    "social_sociology": "?i wdt:P101|wdt:P2579 wd:Q21201 . ?i wdt:P31 ?k . VALUES ?k { " + " ".join(
                        "wd:" + q for q in SOCIAL_KNOWLEDGE_CLASSES) + " } . " + NOT_KNOWLEDGE_SOCIAL,
    "social_class": "{ ?i wdt:P279+ ?f . VALUES ?f { wd:Q161272 wd:Q1355183 } } UNION { ?i wdt:P31 wd:Q602884 . } UNION "
                    "{ ?i wdt:P31 wd:Q1127759 . } UNION { ?i wdt:P279* wd:Q7798106 . } UNION { ?i wdt:P279* wd:Q7942158 . } "
                    "UNION { ?i wdt:P361|wdt:P2579 wd:Q101247857 . } " + NOT_KNOWLEDGE_SOCIAL,
    "social_core": "VALUES ?i { " + " ".join("wd:" + q for q in SOCIAL_CORE) + " } .",
    "socalg_class": " UNION ".join("{ ?i wdt:P31/wdt:P279* wd:%s . } UNION { ?i wdt:P279+ wd:%s . }" % (q, q)
                                   for q in SOCIAL_ALGO_CLASSES) + " " + NOT_KNOWLEDGE_SOCIAL + NOT_PLACE_OR_EVENT,
    "socalg_field": "?i wdt:P101|wdt:P361|wdt:P921|wdt:P2578|wdt:P2579 ?fld . VALUES ?fld { " + " ".join(
                    "wd:" + q for q in SOCIAL_ALGO_FIELDS) + " } . ?i wdt:P31 ?k . VALUES ?k { " + " ".join(
                    "wd:" + q for q in BIO_KNOWLEDGE_CLASSES) + " } . " + NOT_KNOWLEDGE_SOCIAL,
    "core_concepts": "VALUES ?i { " + " ".join("wd:" + q for q in sorted(set().union(*CORE_KIND.values()))) + " } .",
}
SOCIAL_SELECTIONS = {"social_field", "social_sociology", "social_class", "social_core"}
SOCIAL_ALGO_SELECTIONS = {"socalg_class", "socalg_field"}     # procedures: kind algo, domain social science
RADIO_SELECTIONS = {"radio_class", "radio_field", "radio_core"}
ALGO_SELECTIONS = {"algorithm", "computational_problem", "optimization_problem"}
Q_HARD = {"Q1137554": "NP-hard", "Q215206": "NP-complete"}   # complexity classes (verified by label)

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


def get_entities(ids: list[str], props="labels|descriptions|aliases|claims", langs="en") -> dict:
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


def status_of(claims, types, qid=None):
    if qid in DISPUTED or Q_PSEUDOSCIENCE in types:
        return "disputed"
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
    ap.add_argument("--only", help="comma-separated selection name prefixes, e.g. radio (cards of other "
                                   "selections stay as they are)")
    a = ap.parse_args()

    selected: dict[str, set] = {}
    for name, where in SELECTIONS.items():
        if a.only and not name.startswith(tuple(a.only.split(","))):
            continue
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
    stats = {"disputed": 0, "law": 0, "math": 0, "const": 0, "open": 0, "bio": 0, "algo": 0, "ctrl": 0, "machine": 0, "table": 0, "proved": 0, "open_status": 0, "defined": 0, "skipped": 0}
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
        if a.only:      # partial run: keep what the other selections chose this card for
            hit = R.unit_by_alias(cur, "wikidata", q)
            if hit:
                cur.execute("SELECT JSON_EXTRACT(payload, '$.selected_by') FROM rose_unit WHERE unit_id=%s", (hit[0],))
                selected[q] |= set(json.loads(cur.fetchone()[0] or "[]"))
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
        status = status_of(c, types, q)
        if status == "open":
            kind = "open"
        elif types & Q_CONST:
            kind = "const"
        elif dim or types & Q_PHYS or any(s["dim"] for s in symbols):
            kind = "law"
        else:
            kind = "math"
        domain = "physics" if (dim or types & Q_PHYS or any(s["dim"] for s in symbols)) else "math"
        complexity = None
        if selected[q] & ALGO_SELECTIONS and not tex and kind == "math":
            kind = "algo"
            domain = "computer science"
            complexity = next((Q_HARD[t] for t in types if t in Q_HARD), None) or next(
                (h for h in ("NP-hard", "NP-complete") if h.lower() in (descr(e, "en") or "").lower()), None)
        core_kind = next((kd for kd, ids in CORE_KIND.items() if q in ids), None)
        if not tex and kind in ("math", "algo") and (core_kind or selected[q] & {"ctrl_field", "machine_field", "machine_model"}):
            kind = core_kind or ("ctrl" if "ctrl_field" in selected[q] else "machine")
            domain = "engineering" if kind == "ctrl" else "computer science"
        if selected[q] & RADIO_SELECTIONS and domain == "math":
            domain = "radio engineering"
        if selected[q] & SOCIAL_SELECTIONS and domain == "math":
            domain = "social science"
        if selected[q] & SOCIAL_ALGO_SELECTIONS and not tex and kind in ("math", "algo"):
            kind, domain = "algo", "social science"
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
                   "part_of": part_of, "selected_by": sorted(selected[q]), "complexity": complexity,
                   "aliases": [x["value"] for x in e.get("aliases", {}).get("en", [])][:10]}
        name = en
        intent_parts = [p for p in (en, descr(e, "en")) if p]
        intent = " - ".join(intent_parts)
        if payload["aliases"]:
            intent += " [also: " + "; ".join(payload["aliases"]) + "]"
        if complexity:
            intent += (f" [{complexity}: no polynomial-time exact algorithm is known - use an exact solver "
                       "for small instances, otherwise heuristics or approximation algorithms]")
        if q in NOTES:
            intent += f" [note: {NOTES[q]}]"
        if status == "disputed":
            intent += (" [DISPUTED - a proposed concept without established empirical support, not known knowledge"
                       + (f": {DISPUTED[q]}" if q in DISPUTED else "") + "]")
        if status == "open":
            intent += " [OPEN PROBLEM - no known solution, do not claim or search for a general one]"
        elif provers:
            intent += " [proved by " + ", ".join(p["label"] or p["id"] for p in provers) + "]"
        stats[kind] += 1
        stats["open_status" if status == "open" else status] += 1   # status: proved | open | defined | disputed
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
