"""Access to the Rose corpus in MariaDB (tables rose_*): resolve refs, search, plan.

Connection: ~/.my.cnf section $ROSE_DB_GROUP, database $ROSE_DB_NAME (default "rose" for both). Embeddings: bge-m3 at ROSE_EMBED_URL
(default http://127.0.0.1:8084/v1/embeddings). ROSE_OFFLINE=1 disables the corpus.
"""
import json
import os
from collections import Counter

# Measured 2026-11-08 (bge-m3): right units 0.50-0.71, noise up to 0.55 - similarity alone cannot
# separate "known" from "unknown"; below MIN the corpus surely has no match, below LOW it is a guess.
MIN_SIMILARITY = float(os.environ.get("ROSE_MIN_SIMILARITY", "0.45"))
LOW_CONFIDENCE = float(os.environ.get("ROSE_LOW_CONFIDENCE", "0.60"))
# lexical mode (built-in catalog without vectors): similarity = idf-weighted share of the task's words
LEX_MIN = float(os.environ.get("ROSE_LEX_MIN", "0.35"))
LEX_LOW = float(os.environ.get("ROSE_LEX_LOW", "0.70"))
OPEN_MIN = 0.6  # lexical: an open problem must cover most of the task to warn
LEVELS = ["imported", "parsed", "tested", "cross_checked", "proven"]
EMBED_URL = os.environ.get("ROSE_EMBED_URL", "http://127.0.0.1:8084/v1/embeddings")


class Corpus:
    def __init__(self):
        self.con = None
        self.error = None
        self._cache = {}
        if os.environ.get("ROSE_OFFLINE"):
            self.error = "ROSE_OFFLINE set"
            return
        try:
            import pymysql
            self.con = pymysql.connect(read_default_file=os.path.expanduser("~/.my.cnf"),
                                       read_default_group=os.environ.get("ROSE_DB_GROUP", "rose"),
                                       database=os.environ.get("ROSE_DB_NAME", "rose"), charset="utf8mb4",
                                       connect_timeout=5)
        except Exception as e:  # corpus is optional for local-only programs
            self.error = str(e)

    @property
    def online(self):
        return self.con is not None

    def _row(self, where, args):
        cur = self.con.cursor()
        cur.execute("SELECT u.unit_id, u.ref, u.kind, u.name, u.intent, u.signature, u.rose_src, u.payload, "
                    "u.level, s.name, s.license, s.share_alike, u.source_url "
                    "FROM rose_unit u JOIN rose_source s USING (source_id) WHERE " + where, args)
        r = cur.fetchone()
        if not r:
            return None
        keys = ("unit_id", "ref", "kind", "name", "intent", "signature", "rose_src", "payload", "level",
                "source", "license", "share_alike", "source_url")
        d = dict(zip(keys, r))
        d["payload"] = json.loads(d["payload"]) if d["payload"] else {}
        return d

    def get(self, ref: str):
        """ref like 'law:ohms_law', 'oeis:A000040', 'const:codata.boltzmann_constant', 'wikidata:Q11382'."""
        if not self.online:
            return None
        if ref in self._cache:
            return self._cache[ref]
        d = self._row("u.ref=%s", (ref,))
        if d is None and ":" in ref:
            scheme, value = ref.split(":", 1)
            d = self._row("u.unit_id=(SELECT unit_id FROM rose_alias WHERE scheme=%s AND value=%s)",
                          (scheme, value))
            if d is None and scheme in ("law", "math", "const", "open"):
                # a law may have been filed under another kind; look up by slug across kinds
                d = self._row("u.ref IN (%s,%s,%s,%s)", tuple(f"{k}:{value}" for k in ("law", "math", "const", "open")))
        self._cache[ref] = d
        return d

    def similar_refs(self, ref, k=5):
        if not self.online or ":" not in ref:
            return []
        name = ref.split(":", 1)[1].split(".")[-1].replace("_", " ")
        cur = self.con.cursor()
        cur.execute("SELECT ref FROM rose_unit WHERE MATCH(name, intent) AGAINST (%s) LIMIT %s", (name, k))
        return [r[0] for r in cur.fetchall()]

    # ---- search / plan ----
    def embed(self, text):
        import requests
        r = requests.post(EMBED_URL, json={"input": [text], "model": "bge-m3-FP16"}, timeout=30)
        r.raise_for_status()
        return r.json()["data"][0]["embedding"]

    def search(self, query, k=10, kind=None, pool=60):
        """Hybrid search. Candidates: HNSW vector top-N + FULLTEXT top-N. Rank: exact cosine similarity
        of every candidate, plus a small bonus for a FULLTEXT hit (semantics first, words second)."""
        cur = self.con.cursor()
        cand, ft, notes, v = set(), set(), [], None
        try:
            v = json.dumps(self.embed(query))
            # the distance expression must be repeated in ORDER BY: ordering by its alias returned wrong
            # neighbours on MariaDB 11.8 (measured 2026-11-08)
            cur.execute("SELECT unit_id FROM rose_embedding ORDER BY VEC_DISTANCE_COSINE(v, VEC_FromText(%s)) "
                        "LIMIT %s", (v, pool))
            cand |= {r[0] for r in cur.fetchall()}
        except Exception as e:
            notes.append(f"vector search unavailable: {e}")
        cur.execute("SELECT unit_id FROM rose_unit WHERE MATCH(name, intent) AGAINST (%s) "
                    "ORDER BY MATCH(name, intent) AGAINST (%s) DESC LIMIT %s", (query, query, pool // 2))
        ft = {r[0] for r in cur.fetchall()}
        cand |= ft
        if not cand:
            return [], notes
        ids = list(cand)
        ph = ",".join(["%s"] * len(ids))
        sims = {}
        if v is not None:
            cur.execute(f"SELECT unit_id, 1 - VEC_DISTANCE_COSINE(v, VEC_FromText(%s)) FROM rose_embedding "
                        f"WHERE unit_id IN ({ph})", [v] + ids)
            sims = {uid: float(s) for uid, s in cur.fetchall()}
        cur.execute("SELECT u.unit_id, u.ref, u.kind, u.name, u.level, u.signature, u.payload, s.license, "
                    "s.share_alike, u.rose_src IS NOT NULL FROM rose_unit u JOIN rose_source s USING (source_id) "
                    f"WHERE u.unit_id IN ({ph})", ids)
        out = []
        for uid, ref, kd, name, level, sig, payload, lic, sa, has_src in cur.fetchall():
            if kind and kd != kind:
                continue
            p = json.loads(payload) if payload else {}
            sim = sims.get(uid, 0.0)
            out.append({"ref": ref, "kind": kd, "name": name, "level": level, "signature": sig,
                        "status": p.get("status"), "domain": p.get("domain"),
                        "usable": bool(has_src) and kd != "open", "license": lic, "share_alike": bool(sa),
                        "similarity": round(sim, 3), "score": sim + (0.03 if uid in ft else 0.0),
                        "proved_by": [x.get("label") for x in p.get("proved_by", [])] or None})
        out.sort(key=lambda r: (-r["score"], -LEVELS.index(r["level"])))
        return out[:k], notes

    def plan(self, task, k=8):
        hits, notes = self.search(task, k=30)
        return make_plan(task, hits, notes, k, semantic=True)


def make_plan(task, hits, notes, k=8, semantic=True):
    """Classify a new task by the solved problems it resembles and list the best solution paths.
    Category = category of the best evidence (highest score per category), not of the most numerous
    source - otherwise 400 000 OEIS sequences outvote one matching law.
    semantic: similarity is a cosine (thresholds MIN/LOW); else it is the idf-weighted share of the
    task's words a unit contains (thresholds LEX_MIN/LEX_LOW)."""
    lo, low = (MIN_SIMILARITY, LOW_CONFIDENCE) if semantic else (LEX_MIN, LEX_LOW)
    warnings = []
    # negative knowledge is checked first and always
    best_known = max((h["score"] for h in hits[:10] if h["kind"] != "open"), default=0.0)
    for h in hits[:10]:
        # an open problem warns when it resembles the task and is not outranked by a solved unit
        # (a proof of the Poincare conjecture must not warn because its generalisation is open)
        if h["kind"] == "open" and h["similarity"] >= max(lo, OPEN_MIN if not semantic else 0) \
                and h["score"] >= 0.95 * best_known:
            warnings.append(f"NEGATIVE KNOWLEDGE: '{h['name']}' is an open problem - no known solution. "
                            "Do not claim or search for a general solution; solve a bounded or numerical "
                            "sub-question instead.")
    best_sim = max((h["similarity"] for h in hits[:10]), default=0.0)
    if best_sim < lo:
        warnings.append(f"CORPUS GAP: no solved problem resembles this task (best similarity {best_sim:.2f} "
                        f"< {lo}). Do not pretend to reuse a known solution; write and test it, then submit it.")
        return {"task": task, "category": "unknown", "confidence": 0.0, "distribution": {},
                "paths": [], "warnings": warnings, "notes": notes}
    best = {}
    for h in hits:
        c = category(h)
        best[c] = max(best.get(c, 0.0), h["score"])
    ranked = sorted(best.items(), key=lambda x: -x[1])
    cat = ranked[0][0]
    margin = ranked[0][1] - (ranked[1][1] if len(ranked) > 1 else 0.0)
    if best_sim < low:
        notes.append(f"low confidence: best similarity {best_sim:.2f} < {low}")
    paths = []
    for h in hits:
        if h["kind"] == "open":
            continue
        h = dict(h)
        h["how"] = how_to_use(h)
        paths.append(h)
        if len(paths) >= k:
            break
    return {"task": task, "category": cat, "confidence": round(margin, 3),
            "distribution": {c: round(v, 3) for c, v in ranked}, "paths": paths,
            "warnings": warnings, "notes": notes}


def category(h):
    k = h["kind"]
    if k == "law":
        return "physics/law"
    if k == "const":
        return "physics/constant" if h.get("domain") == "physics" or str(h["ref"]).startswith("const:codata") \
            else "math/constant"
    if k == "math":
        return "math/sequence" if str(h["ref"]).startswith("oeis:") else "math/" + (h.get("status") or "formula")
    return k


def how_to_use(h):
    if h["ref"].startswith("problem:"):
        sol = "; ".join(f"{x['name']} [{x['ref'] or '-'}]: {x['use']}" for x in h.get("solvers", []))
        return f"problem class ({h.get('complexity')}): {sol}"
    d = h.get("dimensions")
    if d and d.get("solve_for"):
        givens = ", ".join(f"{v} = {t}" for v, t in d["given"].items())
        more = f"  (also needs {', '.join(d['unknowns'])})" if d["unknowns"] else ""
        return f"use {h['ref']}  then  solve {d['law']} for {d['solve_for']} given {givens}{more}"
    if h["kind"] in ("law", "math") and h["usable"]:
        return f"use {h['ref']}  then  solve <name> for <unknown> given ..."
    if h["kind"] == "const" and h["usable"]:
        return f"use {h['ref']} as <alias>"
    if h["ref"].startswith("oeis:"):
        return f"use {h['ref']} as <alias>   (terms as test oracle, alias.contains(x))"
    if h["kind"] == "bio":
        return f"use {h['ref']}   (local DIAMOND nr, two-stage, never online BLAST)"
    if h["ref"].startswith("rc:"):
        return (f"python: rose.use({h['ref']!r}).code  (Rosetta Code solution, GFDL share-alike); "
                "Rose: reference only, no signature yet")
    return f"reference only ({h['level']}): no machine-readable Rose source yet"
