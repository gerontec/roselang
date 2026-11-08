"""Access to the Rose corpus in MariaDB (tables rose_*): resolve refs, search, plan.

Connection: ~/.my.cnf section $ROSE_DB_GROUP, database $ROSE_DB_NAME (default "rose" for both). Embeddings: bge-m3 at ROSE_EMBED_URL
(default http://127.0.0.1:8084/v1/embeddings). ROSE_OFFLINE=1 disables the corpus.
"""
import json
import os
from collections import Counter

MIN_SIMILARITY = float(os.environ.get("ROSE_MIN_SIMILARITY", "0.55"))  # below: corpus does not know the task
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
        """Hybrid search: HNSW vector top-N + FULLTEXT top-N, fused by reciprocal rank (RRF)."""
        cur = self.con.cursor()
        ranks, sims, notes = {}, {}, []
        try:
            v = json.dumps(self.embed(query))
            cur.execute("SELECT unit_id, VEC_DISTANCE_COSINE(v, VEC_FromText(%s)) d FROM rose_embedding "
                        "ORDER BY d LIMIT %s", (v, pool))
            for i, (uid, d) in enumerate(cur.fetchall()):
                ranks.setdefault(uid, 0.0)
                ranks[uid] += 1.0 / (60 + i)
                sims[uid] = 1 - float(d)
        except Exception as e:
            notes.append(f"vector search unavailable: {e}")
        cur.execute("SELECT unit_id, MATCH(name, intent) AGAINST (%s) s FROM rose_unit "
                    "WHERE MATCH(name, intent) AGAINST (%s) ORDER BY s DESC LIMIT %s", (query, query, pool))
        for i, (uid, s) in enumerate(cur.fetchall()):
            ranks.setdefault(uid, 0.0)
            ranks[uid] += 1.0 / (60 + i)
        if not ranks:
            return [], notes
        ids = list(ranks)
        cur.execute("SELECT u.unit_id, u.ref, u.kind, u.name, u.level, u.signature, u.payload, s.license, "
                    "s.share_alike, u.rose_src IS NOT NULL FROM rose_unit u JOIN rose_source s USING (source_id) "
                    f"WHERE u.unit_id IN ({','.join(['%s'] * len(ids))})", ids)
        out = []
        for uid, ref, kd, name, level, sig, payload, lic, sa, has_src in cur.fetchall():
            if kind and kd != kind:
                continue
            p = json.loads(payload) if payload else {}
            out.append({"ref": ref, "kind": kd, "name": name, "level": level, "signature": sig,
                        "status": p.get("status"), "domain": p.get("domain"),
                        "usable": bool(has_src) and kd != "open", "license": lic, "share_alike": bool(sa),
                        "similarity": round(sims.get(uid, 0.0), 3), "score": ranks[uid],
                        "proved_by": [x.get("label") for x in p.get("proved_by", [])] or None})
        out.sort(key=lambda r: (-r["score"], -LEVELS.index(r["level"])))
        return out[:k], notes

    def plan(self, task, k=8):
        """Classify a new task by the solved problems it resembles and list the best solution paths."""
        hits, notes = self.search(task, k=30)
        weights = Counter()
        for i, h in enumerate(hits[:15]):
            cat = category(h)
            weights[cat] += 1.0 / (1 + i)
        best_sim = max((h["similarity"] for h in hits[:10]), default=0.0)
        if best_sim < MIN_SIMILARITY:
            return {"task": task, "category": "unknown", "confidence": 0.0, "distribution": {},
                    "paths": [], "notes": notes,
                    "warnings": [f"CORPUS GAP: no solved problem in the corpus resembles this task "
                                 f"(best similarity {best_sim:.2f} < {MIN_SIMILARITY}). Do not pretend to "
                                 "reuse a known solution; write and test it, then submit it."]}
        total = sum(weights.values()) or 1.0
        dist = {c: round(w / total, 2) for c, w in weights.most_common()}
        cat = next(iter(dist), None)
        warnings = []
        for h in hits[:5]:
            if h["kind"] == "open":
                warnings.append(f"NEGATIVE KNOWLEDGE: '{h['name']}' is an open problem - no known solution. "
                                "Do not claim or search for a general solution; solve a bounded or numerical "
                                "sub-question instead.")
        paths = []
        for h in hits:
            if h["kind"] == "open":
                continue
            h = dict(h)
            h["how"] = how_to_use(h)
            paths.append(h)
            if len(paths) >= k:
                break
        return {"task": task, "category": cat, "confidence": dist.get(cat, 0.0), "distribution": dist,
                "paths": paths, "warnings": warnings, "notes": notes}


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
    if h["kind"] in ("law", "math") and h["usable"]:
        return f"use {h['ref']}  then  solve <name> for <unknown> given ..."
    if h["kind"] == "const" and h["usable"]:
        return f"use {h['ref']} as <alias>"
    if h["ref"].startswith("oeis:"):
        return f"use {h['ref']} as <alias>   (terms as test oracle, alias.contains(x))"
    if h["kind"] == "bio":
        return f"use {h['ref']}   (local DIAMOND nr, two-stage, never online BLAST)"
    return f"reference only ({h['level']}): no machine-readable Rose source yet"
