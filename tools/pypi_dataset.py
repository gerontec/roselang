#!/usr/bin/env python3
"""A public overview of ALL PyPI projects (not shipped in the package): one compact, LLM-readable
record per project - what it is for, licence, whether its latest release installs on CPython 3.14
(Linux x86_64), when it was last released, links and a cleaned README extract. Metadata only:
nothing is installed or run.

  fetch   pypi_dataset.py fetch      all names from the PyPI simple index -> data/pypi_all/records.jsonl
                                     (append-only, resumable; reuses data/pypi/*.json.gz of import_pypi.py)
  build   pypi_dataset.py build      records.jsonl -> data/pypi_all/dataset/pypi-<a..z,0-9,_>.jsonl.gz + STATS.md
"""
import argparse
import collections
import concurrent.futures as cf
import datetime as dt
import gzip
import json
import os
import sys
import threading
import time
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import import_pypi as P          # noqa: E402  (fetch helpers, licence, topics, installable)
import readme_clean               # noqa: E402

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "pypi_all")
RECORDS = os.path.join(BASE, "records.jsonl")
SIMPLE = "https://pypi.org/simple/"


def names():
    path = os.path.join(BASE, "_simple.json")
    if not os.path.exists(path):
        os.makedirs(BASE, exist_ok=True)
        import urllib.request
        req = urllib.request.Request(SIMPLE, headers={"User-Agent": P.UA, "Accept": "application/vnd.pypi.simple.v1+json"})
        open(path, "wb").write(urllib.request.urlopen(req, timeout=120).read())
    return [p["name"] for p in json.load(open(path))["projects"]]


def record(d):
    info = d["info"]
    files = d.get("urls") or []
    lic = P.licence(info)
    sa = bool(P.SHARE_ALIKE.search(lic or ""))
    up = [f.get("upload_time_iso_8601") or f.get("upload_time") for f in files if f.get("upload_time_iso_8601") or f.get("upload_time")]
    urls = info.get("project_urls") or {}
    pick = lambda *keys: next((v for k, v in urls.items() if k.lower() in keys), None)  # noqa: E731
    try:
        inst = P.installable(info, files)
    except Exception:
        inst = None
    return {"name": info["name"], "version": info.get("version"),
            "summary": " ".join((info.get("summary") or "").split()) or None,
            "keywords": " ".join((info.get("keywords") or "").split())[:300] or None,
            "topics": P.topics(info) or None, "license": lic, "share_alike": sa or None,
            "requires_python": info.get("requires_python") or None, "install_cp314": inst,
            "last_release": max(up)[:10] if up else None, "yanked": info.get("yanked") or None,
            "docs": pick("documentation", "docs"), "homepage": pick("homepage", "home") or info.get("home_page") or None,
            "source": pick("source", "source code", "repository", "github", "code"),
            "url": f"https://pypi.org/project/{info['name']}/",
            "readme": None if sa else (readme_clean.extract(info.get("description") or "",
                                                            info.get("description_content_type")) or None)}


class Brake:
    """Shared back-off: a 429 or 5xx from PyPI stops every thread for a while (doubling up to
    5 minutes while it repeats); each success shortens the next pause again."""
    def __init__(self):
        self.lock, self.until, self.delay, self.hits, self.bytes = threading.Lock(), 0.0, 5.0, 0, 0

    def wait(self):
        t = self.until - time.time()
        if t > 0:
            time.sleep(t)

    def hit(self):
        with self.lock:
            self.hits += 1
            self.until = max(self.until, time.time() + self.delay)
            self.delay = min(self.delay * 2, 300.0)

    def ok(self, n):
        with self.lock:
            self.bytes += n
            self.delay = max(5.0, self.delay * 0.99)


BRAKE = Brake()


def fetch_one(name):
    cached = os.path.join(P.CACHE, P.norm(name) + ".json.gz")
    try:
        if os.path.exists(cached):
            d = json.load(gzip.open(cached))
        else:
            for attempt in range(6):
                BRAKE.wait()
                try:
                    raw = P.get(f"https://pypi.org/pypi/{name}/json")
                    BRAKE.ok(len(raw))
                    d = json.loads(raw)
                    break
                except urllib.error.HTTPError as e:
                    if e.code == 404:
                        return {"name": name, "missing": True}
                    if e.code == 429 or e.code >= 500:
                        BRAKE.hit()
                    else:
                        time.sleep(1 + attempt)
                except Exception:
                    time.sleep(1 + 2 * attempt)
            else:
                return None                        # retried later on resume
        r = {k: v for k, v in record(d).items() if v is not None}
        r["key"] = P.norm(name)
        return r
    except Exception as e:                         # broken metadata: keep the name, note the error
        return {"name": name, "key": P.norm(name), "error": type(e).__name__}


def record_files():
    return sorted(os.path.join(BASE, f) for f in os.listdir(BASE) if f.startswith("records") and f.endswith(".jsonl"))


def fetch(threads, shard="0/1"):
    """Shard k/N fetches every N-th name starting at k into records-<k>.jsonl, so that N processes
    can run side by side (one Python process is limited by its interpreter lock, not by the line)."""
    k, n = map(int, shard.split("/"))
    all_names = names()
    done = set()
    for path in record_files() if os.path.isdir(BASE) else []:
        for ln in open(path, encoding="utf-8"):
            try:
                done.add(P.norm(json.loads(ln)["name"]))
            except Exception:
                pass
    todo = [x for i, x in enumerate(all_names) if i % n == k and P.norm(x) not in done]
    print(f"{len(all_names)} projects, {len(done)} done, shard {shard}: {len(todo)} to fetch", flush=True)
    stats, t0 = collections.Counter(), time.time()
    out_path = RECORDS if n == 1 else os.path.join(BASE, f"records-{k}.jsonl")
    with open(out_path, "a", encoding="utf-8") as out, cf.ThreadPoolExecutor(threads) as ex:
        for c in range(0, len(todo), 2000):                     # bounded: one chunk in flight at a time
            for r in ex.map(fetch_one, todo[c:c + 2000]):
                if r is None:
                    stats["retry later"] += 1
                    continue
                stats["missing" if r.get("missing") else "error" if r.get("error") else "ok"] += 1
                out.write(json.dumps(r, ensure_ascii=False) + "\n")
            out.flush()
            i, dt_ = min(c + 2000, len(todo)), time.time() - t0
            rate = i / dt_
            print(f"{i}/{len(todo)} {dict(stats)} {rate:.0f}/s, {BRAKE.bytes * 8 / dt_ / 1e6:.0f} Mbit/s, "
                  f"throttled {BRAKE.hits}x, eta {(len(todo) - i) / rate / 3600:.1f} h", flush=True)
    print("fetched", dict(stats), flush=True)


def build():
    out_dir = os.path.join(BASE, "dataset")
    os.makedirs(out_dir, exist_ok=True)
    shards, seen, st = collections.defaultdict(list), set(), collections.Counter()
    years = collections.Counter()
    for ln in (x for path in record_files() for x in open(path, encoding="utf-8")):
        try:
            r = json.loads(ln)
        except json.JSONDecodeError:               # a line cut off by an interrupted fetch
            continue
        k = P.norm(r["name"])
        if k in seen or r.get("missing"):
            st["missing"] += bool(r.get("missing"))
            continue
        seen.add(k)
        st["projects"] += 1
        st["installable_wheel"] += r.get("install_cp314") == "wheel"
        st["installable_sdist"] += r.get("install_cp314") == "sdist"
        st["with_readme_extract"] += bool(r.get("readme"))
        st["with_summary"] += bool(r.get("summary"))
        st["share_alike"] += bool(r.get("share_alike"))
        if r.get("last_release"):
            years[r["last_release"][:4]] += 1
        c = k[0] if k[0].isalnum() else "_"
        r.pop("key", None)
        shards[c].append(r)
    for c, rows in sorted(shards.items()):
        rows.sort(key=lambda r: P.norm(r["name"]))
        with gzip.open(os.path.join(out_dir, f"pypi-{c}.jsonl.gz"), "wt", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
    with open(os.path.join(out_dir, "STATS.md"), "w") as f:
        f.write(f"# PyPI overview - build {dt.date.today().isoformat()}\n\n")
        for k, v in st.items():
            f.write(f"- {k}: {v}\n")
        f.write("\nLatest release by year:\n\n" + "".join(f"- {y}: {n}\n" for y, n in sorted(years.items())))
    print(dict(st), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("step", choices=["fetch", "build"])
    ap.add_argument("--threads", type=int, default=16)
    ap.add_argument("--shard", default="0/1", help="k/N: this process takes every N-th name, starting at k")
    a = ap.parse_args()
    fetch(a.threads, a.shard) if a.step == "fetch" else build()


if __name__ == "__main__":
    sys.exit(main())
