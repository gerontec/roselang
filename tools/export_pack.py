#!/usr/bin/env python3
"""Export a share-alike source as a separate knowledge pack (installable, own licence).

  rosetta: Rosetta Code (GFDL 1.3) -> packs/rosetta/rose_rosetta/{catalog.jsonl, impl.jsonl}
           installable as `pip install ./packs/rosetta` (distribution roselang-rosetta, module rose_rosetta);
           rose/knowledge.py finds it automatically.
Usage: export_pack.py rosetta [--out ../packs/rosetta]
"""
import argparse
import json
import os
import sys

import rose_db as R

PACKS = {"rosetta": ("rosettacode", "rose_rosetta")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pack", choices=sorted(PACKS))
    ap.add_argument("--out")
    a = ap.parse_args()
    source, module = PACKS[a.pack]
    out = os.path.abspath(a.out or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "packs", a.pack))
    d = os.path.join(out, module)
    os.makedirs(d, exist_ok=True)
    con = R.connect()
    cur = con.cursor()
    cur.execute("SELECT u.unit_id, u.ref, u.kind, u.name, u.intent, u.level, u.payload, u.source_url, s.license "
                "FROM rose_unit u JOIN rose_source s USING (source_id) WHERE s.name=%s ORDER BY u.ref", (source,))
    units = cur.fetchall()
    impls = {}
    cur.execute("SELECT i.unit_id, i.lang, i.code, i.level FROM rose_impl i JOIN rose_unit u USING (unit_id) "
                "JOIN rose_source s USING (source_id) WHERE s.name=%s ORDER BY i.impl_id", (source,))
    for uid, lang, code, level in cur.fetchall():
        impls.setdefault(uid, []).append({"lang": lang, "code": code, "level": level})
    stats = {"tasks": 0, "with_python": 0, "with_python3": 0, "solutions": 0}
    with open(os.path.join(d, "catalog.jsonl"), "w", encoding="utf-8") as fc, \
            open(os.path.join(d, "impl.jsonl"), "w", encoding="utf-8") as fi:
        for uid, ref, kind, name, intent, level, payload, url, lic in units:
            p = json.loads(payload) if payload else {}
            card = {"ref": ref, "kind": kind, "name": name, "intent": intent, "level": level, "source": source,
                    "license": lic, "url": url, "share_alike": True, "std": False,
                    "description": p.get("description"), "outputs": p.get("outputs", []),
                    "languages": p.get("languages"), "python_solutions": p.get("python_solutions", 0),
                    "python3_solutions": p.get("python3_solutions", 0), "status": p.get("status")}
            fc.write(json.dumps(card, ensure_ascii=False, sort_keys=True) + "\n")
            if uid in impls:
                fi.write(json.dumps({"ref": ref, "impl": impls[uid]}, ensure_ascii=False) + "\n")
            stats["tasks"] += 1
            stats["with_python"] += bool(p.get("python_solutions"))
            stats["with_python3"] += bool(p.get("python3_solutions"))
            stats["solutions"] += len(impls.get(uid, []))
    print(out, stats)


if __name__ == "__main__":
    sys.exit(main())
