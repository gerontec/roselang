#!/usr/bin/env python3
"""Export a large source as a built-in knowledge set of the core: rose/std/sets/<pack>.jsonl.gz
(+ <pack>.impl.jsonl.gz with implementations). Every card carries the SPDX id of its source; the
licences are listed in rose/std/LICENSES.md. --out DIR writes a third-party pack directory instead.

Former separate packs (kept for reference):

  rosetta: Rosetta Code (GFDL 1.3) -> packs/rosetta/rose_rosetta/{catalog.jsonl, impl.jsonl}
           installable as `pip install ./packs/rosetta` (distribution roselang-rosetta, module rose_rosetta)
  mathlib: Lean mathlib4 theorem statements (Apache-2.0) -> packs/mathlib/rose_mathlib/catalog.jsonl
           (distribution roselang-mathlib; a pack because of its size, not its licence)
rose/knowledge.py finds installed packs automatically.
Usage: export_pack.py rosetta|mathlib [--out ../packs/<pack>]
"""
import argparse
import json
import os
import sys

import rose_db as R

# pack -> (corpus source, module, share-alike, payload fields copied into the card)
PACKS = {"rosetta": ("rosettacode", "rose_rosetta", True,
                     ("description", "outputs", "languages", "python_solutions", "python3_solutions", "status")),
         "mathlib": ("mathlib", "rose_mathlib", False, ("statement", "doc", "named", "file", "line", "status")),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pack", choices=sorted(PACKS))
    ap.add_argument("--out")
    a = ap.parse_args()
    source, module, share_alike, fields = PACKS[a.pack]
    import gzip
    if a.out:
        d = os.path.join(os.path.abspath(a.out), module)
        os.makedirs(d, exist_ok=True)
        cat_path, impl_file = os.path.join(d, "catalog.jsonl"), os.path.join(d, "impl.jsonl")
        opener = open
    else:
        d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "rose", "std", "sets")
        os.makedirs(d, exist_ok=True)
        cat_path, impl_file = os.path.join(d, a.pack + ".jsonl.gz"), os.path.join(d, a.pack + ".impl.jsonl.gz")
        opener = lambda p, m, encoding: gzip.open(p, m + "t", encoding=encoding, compresslevel=9)  # noqa: E731
    out = cat_path
    con = R.connect()
    cur = con.cursor()
    cur.execute("SELECT u.unit_id, u.ref, u.kind, u.name, u.intent, u.level, u.payload, u.source_url, s.license "
                "FROM rose_unit u JOIN rose_source s USING (source_id) WHERE s.name=%s ORDER BY u.ref", (source,))
    units = cur.fetchall()
    aliases = {}
    cur.execute("SELECT a.unit_id, a.scheme, a.value FROM rose_alias a JOIN rose_unit u USING (unit_id) "
                "JOIN rose_source s USING (source_id) WHERE s.name=%s", (source,))
    for uid_, scheme, value in cur.fetchall():
        aliases.setdefault(uid_, []).append(f"{scheme}:{value}")
    impls = {}
    cur.execute("SELECT i.unit_id, i.lang, i.code, i.level FROM rose_impl i JOIN rose_unit u USING (unit_id) "
                "JOIN rose_source s USING (source_id) WHERE s.name=%s ORDER BY i.impl_id", (source,))
    for uid, lang, code, level in cur.fetchall():
        impls.setdefault(uid, []).append({"lang": lang, "code": code, "level": level})
    stats = {"units": 0, "with_python": 0, "with_python3": 0, "solutions": 0}
    with opener(cat_path, "w", encoding="utf-8") as fc, opener(impl_file, "w", encoding="utf-8") as fi:
        for uid, ref, kind, name, intent, level, payload, url, lic in units:
            p = json.loads(payload) if payload else {}
            card = {"ref": ref, "kind": kind, "name": name, "intent": intent, "level": level, "source": source,
                    "license": lic, "url": url, "share_alike": share_alike, "std": False}
            card.update({f: p[f] for f in fields if p.get(f) not in (None, [], "")})
            if uid in aliases:
                card["aliases"] = sorted(aliases[uid])
            fc.write(json.dumps(card, ensure_ascii=False, sort_keys=True) + "\n")
            if uid in impls:
                fi.write(json.dumps({"ref": ref, "impl": impls[uid]}, ensure_ascii=False) + "\n")
            stats["units"] += 1
            stats["with_python"] += bool(p.get("python_solutions"))
            stats["with_python3"] += bool(p.get("python3_solutions"))
            stats["solutions"] += len(impls.get(uid, []))
    print(out, stats)


if __name__ == "__main__":
    sys.exit(main())
