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


INDEX_VERSION = 1


def cache_dir():
    d = os.environ.get("ROSE_CACHE") or os.path.join(
        os.environ.get("XDG_CACHE_HOME") or os.path.join(os.path.expanduser("~"), ".cache"), "roselang")
    os.makedirs(d, exist_ok=True)
    return d


class Knowledge:
    """Cards of the core catalog and all installed packs, behind one SQLite file (FTS5 full-text
    index) that is built once per set of catalog files and cached (~/.cache/roselang, $ROSE_CACHE)."""

    def __init__(self, fallback=None):
        import hashlib
        import sqlite3
        self.fallback = fallback
        self.error = None
        self.packs = pack_dirs()
        sources = [(CATALOG, None)] + [(os.path.join(d, "catalog.jsonl"), d) for d in self.packs]
        if not os.path.exists(CATALOG):
            self.error = f"{CATALOG} missing - run tools/export_std.py"
            sources = sources[1:]
        h = hashlib.sha1(str(INDEX_VERSION).encode())
        for path, _ in sources:
            st = os.stat(path)
            h.update(f"{os.path.abspath(path)}|{st.st_size}|{st.st_mtime_ns}".encode())
        self.db_path = os.path.join(cache_dir(), f"knowledge-{h.hexdigest()[:16]}.sqlite")
        if not os.path.exists(self.db_path):
            self._build(sources)
        self.db = sqlite3.connect(self.db_path, check_same_thread=False)
        meta = dict(self.db.execute("SELECT key, value FROM meta"))
        self.n_core, self.n = int(meta["n_core"]), int(meta["n"])
        self._impl = {}
        self._vec = None
        self._idf_max = math.log(1 + (self.n + 0.5) / 0.5)

    def _build(self, sources):
        import sqlite3
        import sys
        print(f"rose: building the knowledge index once ({len(sources)} catalog file(s)) ...", file=sys.stderr)
        tmp = self.db_path + f".tmp{os.getpid()}"
        db = sqlite3.connect(tmp)
        db.executescript("""
            CREATE TABLE cards (id INTEGER PRIMARY KEY, ref TEXT UNIQUE, kind TEXT, pack TEXT, json TEXT);
            CREATE TABLE alias (alias TEXT PRIMARY KEY, id INTEGER);
            CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);
            CREATE VIRTUAL TABLE fts USING fts5(ntok, btok, tokenize = 'unicode61');
            CREATE VIRTUAL TABLE vocab USING fts5vocab(fts, 'row');
        """)
        n, n_core, seen = 0, 0, set()
        for path, pack in sources:
            rows, frows, arows = [], [], []
            with open(path, encoding="utf-8") as f:
                for line in f:
                    c = json.loads(line)
                    if c["ref"] in seen:
                        continue
                    seen.add(c["ref"])
                    n += 1
                    rows.append((n, c["ref"], c["kind"], pack, line))
                    name = tokens(c["name"] + " " + c["ref"].split(":", 1)[1].replace("_", " ").replace(".", " "))
                    frows.append((n, " ".join(name), " ".join(tokens(c.get("intent", "")))))
                    arows += [(a, n) for a in c.get("aliases", [])]
            db.executemany("INSERT INTO cards VALUES (?,?,?,?,?)", rows)
            db.executemany("INSERT INTO fts (rowid, ntok, btok) VALUES (?,?,?)", frows)
            db.executemany("INSERT OR IGNORE INTO alias VALUES (?,?)", arows)
            if pack is None:
                n_core = n                      # catalog.vec covers the core catalog only, ids 1..n_core
        db.executemany("INSERT INTO meta VALUES (?,?)", [("n", n), ("n_core", n_core)])
        db.commit()
        db.close()
        os.replace(tmp, self.db_path)
        # keep the three most recent indexes (other pack sets), drop older ones
        old = sorted((f for f in os.listdir(cache_dir()) if f.startswith("knowledge-") and f.endswith(".sqlite")),
                     key=lambda f: -os.path.getmtime(os.path.join(cache_dir(), f)))[3:]
        for f in old:
            try:
                os.unlink(os.path.join(cache_dir(), f))
            except OSError:
                pass

    def _card(self, i):
        r = self.db.execute("SELECT json, pack FROM cards WHERE id=?", (i,)).fetchone()
        c = json.loads(r[0])
        if r[1]:
            c["_pack"] = r[1]
        return c

    def _id(self, ref):
        r = self.db.execute("SELECT id FROM cards WHERE ref=?", (ref,)).fetchone() or \
            self.db.execute("SELECT id FROM alias WHERE alias=?", (ref,)).fetchone()
        return r[0] if r else None

    def implementations(self, ref):
        """Implementations of a pack unit: [{"lang", "code", "level"}]."""
        i = self._id(ref)
        pack = self._card(i).get("_pack") if i is not None else None
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
        return self.n > 0 or bool(self.fallback and self.fallback.online)

    @property
    def mode(self):
        return "semantic+lexical" if self._vectors() is not None and self._embed_ok() else "lexical"

    # ---- get ----
    def get(self, ref):
        i = self._id(ref)
        if i is None and ":" in ref:
            scheme, value = ref.split(":", 1)
            if scheme in ("law", "math", "const", "open"):
                for k in ("law", "math", "const", "open"):
                    i = self._id(f"{k}:{value}")
                    if i is not None:
                        break
        if i is None:
            return self.fallback.get(ref) if self.fallback and self.fallback.online else None
        c = self._card(i)
        c["rose_src"] = None   # Rose source of std units is bound from std/ by the compiler (bind_std)
        c["source_url"] = c.get("url")
        c["share_alike"] = bool(c.get("share_alike"))
        c["payload"] = {"tex": [c["tex"]]} if c.get("tex") else {}
        return c

    def similar_refs(self, ref, k=5):
        name = ref.split(":", 1)[-1].split(".")[-1].replace("_", " ")
        hits, _ = self.search(name, k=k, semantic=False)
        return [h["ref"] for h in hits]

    # ---- lexical ----
    def _lexical(self, query, pool):
        """BM25 (FTS5, name column weighted 3x) for ranking; similarity = idf-weighted share of the
        task's words that a unit contains. Returns ({id: score}, {id: coverage})."""
        q = list(dict.fromkeys(tokens(query)))
        if not q:
            return {}, {}
        ph = ",".join("?" * len(q))
        df = dict(self.db.execute(f"SELECT term, doc FROM vocab WHERE term IN ({ph})", q))
        w = {t: (math.log(1 + (self.n - df[t] + 0.5) / (df[t] + 0.5)) if t in df else self._idf_max) for t in q}
        known = [t for t in q if t in df]
        if not known:
            return {}, {}
        match = " OR ".join(f'"{t}"' for t in known)
        rows = self.db.execute("SELECT rowid, -bm25(fts, 3.0, 1.0), ntok, btok FROM fts WHERE fts MATCH ? "
                               "ORDER BY bm25(fts, 3.0, 1.0) LIMIT ?", (match, pool * 4)).fetchall()
        total = sum(w.values())
        qs = set(q)
        scores, cover = {}, {}
        for i, sc, ntok, btok in rows:
            nt = set(ntok.split())
            have = nt | set(btok.split())
            cover[i] = sum(w[t] for t in q if t in have) / total
            scores[i] = sc * (1.5 if nt == qs else 1.0)   # the task names exactly this unit
        top = sorted(scores, key=lambda i: -scores[i])[:pool]
        return {i: scores[i] for i in top}, {i: cover[i] for i in top}

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
            # vector row r is card id r + 1; pack cards (ids > n_core) have no vector: lexical score only
            cand = set(int(r) + 1 for r in np.argpartition(-sims, pool)[:pool]) | set(bm)
            score = {i: (float(sims[i - 1]) if i <= self.n_core else 0.0) + (0.03 if i in bm else 0.0) for i in cand}
            sim = {i: (float(sims[i - 1]) if i <= self.n_core else cover.get(i, 0.0)) for i in cand}
            measure = "cosine"
        else:
            top = max(bm.values(), default=1.0)
            score = {i: s / top for i, s in bm.items()}
            sim = cover
            measure = "coverage"
        out = []
        for i in sorted(score, key=lambda i: -score[i]):
            c = self._card(i)
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
