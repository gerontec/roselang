"""Built-in knowledge of the compiler: std/catalog.jsonl, generated from the corpus, shipped with rosec.

No database, no server: `rosec plan/search/get` and `use` resolution work offline.
  search: BM25 over name, intent and aliases (always available)
          + cosine similarity on std/catalog.vec when that file and an embedding endpoint
            (ROSE_EMBED_URL) are available - then similarity is the cosine, as in the corpus DB
  get:    card by ref, alias (wikidata:Q..., codata:...) or slug across kinds; Rose source from std/
The full corpus (OEIS, share-alike) stays in the database; Knowledge(fallback=Corpus()) asks it for
refs the catalog does not contain.

Packs: optional knowledge under another licence, installed separately (share-alike sources such as
Rosetta Code, GFDL). A pack is a directory with catalog.jsonl and optionally impl.jsonl
(ref -> implementations); found as an installed module (PACK_MODULES) or listed in $ROSE_PACKS.
"""
import json
import math
import os
import re
from collections import Counter

from . import std

CATALOG = os.path.join(std.STD, "catalog.jsonl")
VECTORS = os.path.join(std.STD, "catalog.vec")
EMBED_URL = os.environ.get("ROSE_EMBED_URL", "http://127.0.0.1:8084/v1/embeddings")
DIM = 1024
PACK_MODULES = ("rose_rosetta",)


def pack_dirs():
    import importlib.util
    dirs = []
    for m in PACK_MODULES:
        try:
            spec = importlib.util.find_spec(m)
        except (ImportError, ValueError):
            spec = None
        if spec and spec.submodule_search_locations:
            dirs.append(list(spec.submodule_search_locations)[0])
    dirs += [d for d in os.environ.get("ROSE_PACKS", "").split(os.pathsep) if d]
    return [d for d in dict.fromkeys(dirs) if os.path.exists(os.path.join(d, "catalog.jsonl"))]

STOP = set("""a an the of in on at to for from by with without and or not no is are be been was were it its this
that these those as into than then there here what which who whom how why when where do does did can could should
would will shall may might must i me my we our you your he she they them his her their give gives given get find
finds compute calculate determine write make let lets show prove please need needed using use used want all any
some every each one two below above over under between about is if so such via per""".split())


def stem(w):
    for suf in ("ations", "ation", "ings", "ing", "ies", "es", "s", "ed", "ly"):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            return w[:-len(suf)] + ("y" if suf == "ies" else "")
    return w


def tokens(text):
    out = []
    t = re.sub(r"\bnon[- ]", "non", (text or "").lower().replace("'s", ""))  # non-homologous != homologous
    for w in re.findall(r"[a-z][a-z0-9]*", t):
        if w in STOP or len(w) < 2:
            continue
        out.append(stem(w))
    return out


class Knowledge:
    def __init__(self, fallback=None):
        self.fallback = fallback
        self.error = None
        self.cards, self.by_ref, self.by_alias = [], {}, {}
        try:
            self._load(CATALOG, None)
        except FileNotFoundError:
            self.error = f"{CATALOG} missing - run tools/export_std.py"
        self.n_core = len(self.cards)           # catalog.vec covers the core catalog only
        self.packs = []
        for d in pack_dirs():
            self._load(os.path.join(d, "catalog.jsonl"), d)
            self.packs.append(d)
        self._impl = {}
        self._index = None
        self._vec = None

    def _load(self, path, pack):
        with open(path, encoding="utf-8") as f:
            for line in f:
                c = json.loads(line)
                if pack:
                    c["_pack"] = pack
                if c["ref"] in self.by_ref:
                    continue
                self.by_ref[c["ref"]] = len(self.cards)
                for a in c.get("aliases", []):
                    self.by_alias.setdefault(a, len(self.cards))
                self.cards.append(c)

    def implementations(self, ref):
        """Implementations of a pack unit: [{"lang", "code", "level", "works_with"}]."""
        i = self.by_ref.get(ref)
        pack = self.cards[i].get("_pack") if i is not None else None
        if not pack:
            return []
        if pack not in self._impl:
            self._impl[pack] = {}
            f = os.path.join(pack, "impl.jsonl")
            if os.path.exists(f):
                with open(f, encoding="utf-8") as fh:
                    for line in fh:
                        r = json.loads(line)
                        self._impl[pack][r["ref"]] = r["impl"]
        return self._impl[pack].get(ref, [])

    @property
    def online(self):
        return bool(self.cards) or bool(self.fallback and self.fallback.online)

    @property
    def mode(self):
        return "semantic+lexical" if self._vectors() is not None and self._embed_ok() else "lexical"

    # ---- get ----
    def get(self, ref):
        i = self.by_ref.get(ref)
        if i is None:
            i = self.by_alias.get(ref)
        if i is None and ":" in ref:
            scheme, value = ref.split(":", 1)
            for k in ("law", "math", "const", "open"):
                if scheme in ("law", "math", "const", "open") and f"{k}:{value}" in self.by_ref:
                    i = self.by_ref[f"{k}:{value}"]
                    break
        if i is None:
            return self.fallback.get(ref) if self.fallback and self.fallback.online else None
        c = dict(self.cards[i])
        c["rose_src"] = None   # Rose source of std units is bound from std/ by the compiler (bind_std)
        c["source_url"] = c.get("url")
        c["share_alike"] = bool(c.get("share_alike"))
        c["payload"] = {"tex": [c["tex"]]} if c.get("tex") else {}
        return c

    def similar_refs(self, ref, k=5):
        name = ref.split(":", 1)[-1].split(".")[-1].replace("_", " ")
        hits, _ = self.search(name, k=k, semantic=False)
        return [h["ref"] for h in hits]

    # ---- lexical index ----
    def _build(self):
        df, docs = Counter(), []
        for c in self.cards:
            name = tokens(c["name"] + " " + c["ref"].split(":", 1)[1].replace("_", " ").replace(".", " "))
            body = tokens(c.get("intent", ""))
            tf = Counter(body)
            for t in name:
                tf[t] += 3          # the name says what the unit is
            docs.append((tf, sum(tf.values()), set(name)))
            df.update(tf.keys())
        n = len(docs)
        idf = {t: math.log(1 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}
        avg = sum(L for _, L, _ in docs) / max(n, 1)
        post = {}
        for i, (tf, _, _) in enumerate(docs):
            for t in tf:
                post.setdefault(t, []).append(i)
        self._index = (docs, idf, avg, post, math.log(1 + (n + 0.5) / 0.5))

    def _lexical(self, query, pool):
        if self._index is None:
            self._build()
        docs, idf, avg, post, idf_max = self._index
        q = list(dict.fromkeys(tokens(query)))
        if not q:
            return {}, {}
        w = {t: idf.get(t, idf_max) for t in q}     # an unknown word is as specific as a word can be
        total = sum(w.values())
        scores, cover = Counter(), Counter()
        for t in q:
            for i in post.get(t, ()):
                tf, L, _ = docs[i]
                f = tf[t]
                scores[i] += w[t] * f * 2.2 / (f + 1.2 * (0.25 + 0.75 * L / avg))
                cover[i] += w[t]
        qs = set(q)
        for i in list(scores):
            if docs[i][2] == qs:            # the task names exactly this unit: it outranks its relatives
                scores[i] *= 1.5
        top = scores.most_common(pool)
        return {i: s for i, s in top}, {i: cover[i] / total for i, _ in top}

    # ---- semantic ----
    def _vectors(self):
        if self._vec is None:
            self._vec = False
            try:
                import numpy as np
                m = np.fromfile(VECTORS, dtype=np.int8)
                if m.size == self.n_core * DIM:
                    self._vec = m.reshape(self.n_core, DIM).astype(np.float32) / 127.0
            except Exception:
                pass
        return self._vec if self._vec is not False else None

    def _embed_ok(self):
        return not os.environ.get("ROSE_NO_EMBED")

    def _embed(self, text):
        import requests
        r = requests.post(EMBED_URL, json={"input": [text], "model": "bge-m3-FP16"}, timeout=10)
        r.raise_for_status()
        return r.json()["data"][0]["embedding"]

    # ---- search ----
    def search(self, query, k=10, kind=None, pool=60, semantic=True):
        notes = []
        bm, cover = self._lexical(query, pool)
        sims = None
        m = self._vectors() if semantic and self._embed_ok() else None
        if m is not None:
            try:
                import numpy as np
                v = np.array(self._embed(query), dtype=np.float32)
                v /= np.linalg.norm(v) or 1.0
                sims = m @ v
            except Exception as e:
                notes.append(f"semantic search unavailable ({type(e).__name__}), lexical only")
        if sims is not None:
            import numpy as np
            cand = set(int(i) for i in np.argpartition(-sims, pool)[:pool]) | set(bm)
            score = {i: float(sims[i]) + (0.03 if i in bm else 0.0) for i in cand}
            sim = {i: float(sims[i]) for i in cand}
            measure = "cosine"
        else:
            top = max(bm.values(), default=1.0)
            score = {i: s / top for i, s in bm.items()}
            sim = cover
            measure = "coverage"
        out = []
        for i in sorted(score, key=lambda i: -score[i]):
            c = self.cards[i]
            if kind and c["kind"] != kind:
                continue
            out.append({"ref": c["ref"], "kind": c["kind"], "name": c["name"], "level": c["level"],
                        "signature": c.get("signature"), "status": c.get("status"), "domain": c.get("domain"),
                        "usable": bool(c.get("std")) and c["kind"] != "open", "license": c["license"],
                        "share_alike": bool(c.get("share_alike")), "similarity": round(sim.get(i, 0.0), 3),
                        "score": round(score[i], 4), "measure": measure, "proved_by": c.get("proved_by")})
            if len(out) >= k:
                break
        return out, notes

    def plan(self, task, k=8):
        from .corpus import make_plan
        hits, notes = self.search(task, k=30)
        semantic = bool(hits) and hits[0]["measure"] == "cosine"
        return make_plan(task, hits, notes, k, semantic)
