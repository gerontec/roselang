#!/usr/bin/env python3
"""Embed rose_unit name+intent with bge-m3 (llama-server :8084) into rose_embedding.

Idempotent: a unit is re-embedded only when the sha256 of its text changed.
Usage: embed.py [--kind law] [--source oeis] [--limit N] [--batch 64]
"""
import argparse
import json
import os
import sys
import time

import requests

import rose_db as R

URL = os.environ.get("ROSE_EMBED_URL", "http://127.0.0.1:8084/v1/embeddings")
MODEL = "bge-m3-FP16"
DIM = 1024


def embed_text(name, intent):
    return f"{name}\n{intent}"[:2000]


def embed(texts):
    r = requests.post(URL, json={"input": texts, "model": MODEL}, timeout=300)
    r.raise_for_status()
    data = sorted(r.json()["data"], key=lambda d: d["index"])
    return [d["embedding"] for d in data]


def model_id(cur):
    cur.execute("INSERT INTO rose_embed_model (name, dim, endpoint) VALUES (%s,%s,%s) "
                "ON DUPLICATE KEY UPDATE endpoint=VALUES(endpoint), model_id=LAST_INSERT_ID(model_id)",
                (MODEL, DIM, URL))
    return cur.lastrowid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kind")
    ap.add_argument("--source")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--batch", type=int, default=64)
    a = ap.parse_args()
    con = R.connect()
    cur = con.cursor()
    mid = model_id(cur)
    con.commit()
    where, args = ["1=1"], []
    if a.kind:
        where.append("u.kind=%s"); args.append(a.kind)
    if a.source:
        where.append("s.name=%s"); args.append(a.source)
    cur.execute("SELECT u.unit_id, u.name, u.intent, e.text_sha FROM rose_unit u "
                "JOIN rose_source s USING (source_id) LEFT JOIN rose_embedding e USING (unit_id) "
                f"WHERE {' AND '.join(where)} ORDER BY u.unit_id", args)
    todo = []
    for uid, name, intent, old in cur.fetchall():
        t = embed_text(name, intent)
        h = R.sha256(t)
        if old != h:
            todo.append((uid, t, h))
    if a.limit:
        todo = todo[:a.limit]
    print(f"to embed: {len(todo)}", flush=True)
    t0, done = time.time(), 0
    for k in range(0, len(todo), a.batch):
        chunk = todo[k:k + a.batch]
        vecs = embed([t for _, t, _ in chunk])
        cur.executemany(
            "INSERT INTO rose_embedding (unit_id, model_id, text_sha, v) VALUES (%s,%s,%s,VEC_FromText(%s)) "
            "ON DUPLICATE KEY UPDATE model_id=VALUES(model_id), text_sha=VALUES(text_sha), v=VALUES(v)",
            [(uid, mid, h, json.dumps(v)) for (uid, _, h), v in zip(chunk, vecs)])
        con.commit()
        done += len(chunk)
        if done % (a.batch * 50) < a.batch:
            print(f"  {done}/{len(todo)}  {done / (time.time() - t0):.0f}/s", flush=True)
    print(f"embedded {done} in {time.time() - t0:.0f} s", flush=True)


if __name__ == "__main__":
    sys.exit(main())
