#!/usr/bin/env python3
"""Move formula knowledge from the corpus into Rose: convert every imported TeX formula with a
symbol table into a Rose `law`, check it with the compiler and store the result.

  converted + dimensions known + compiler finds no error -> level tested, rose_src set
  converted, some dimensions unknown (pure mathematics)  -> level parsed, rose_src set
  converted but dimensionally inconsistent (E204)        -> level imported, payload.verify.error
  not convertible (derivative, integral, ...)            -> level imported, payload.verify.reason
Usage: verify_laws.py [--limit N] [--ref law:...]
"""
import argparse
import json
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import rose_db as R  # noqa: E402
from rose.compiler import compile_source  # noqa: E402
from rose.tex import TexError, tex_to_law  # noqa: E402


def law_name(ref):
    n = ref.split(":", 1)[1].replace(".", "_")
    return n if not n[0].isdigit() else "l_" + n


def constant_defaults(cur):
    """Wikidata quantity id -> 'value unit' of the CODATA constant it denotes (e.g. the speed of light
    behind the symbol c): matched by name, Wikidata label == CODATA name or its prefix."""
    cur.execute("SELECT u.name, u.rose_src FROM rose_unit u JOIN rose_source s USING (source_id) "
                "WHERE s.name='codata' AND u.rose_src IS NOT NULL")
    codata = {}
    for name, src in cur.fetchall():
        m = re.match(r"\s*const\s+\w+\s*:\s*Real(?:\[[^\]]*\])?\s*=\s*(.+?)\s*(?:#.*)?$", src)
        if m and "uncertainty" not in name.lower():
            codata[name.lower()] = m.group(1)
    cur.execute("SELECT a.value, u.name FROM rose_alias a JOIN rose_unit u USING (unit_id) "
                "WHERE a.scheme='wikidata' AND u.kind='const'")
    out = {}
    for qid, name in cur.fetchall():
        n = name.lower()
        hit = codata.get(n) or next((v for k, v in sorted(codata.items()) if k.startswith(n + " ")), None)
        if hit:
            out[qid] = hit
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--ref")
    a = ap.parse_args()
    con = R.connect()
    cur = con.cursor()
    q = ("SELECT u.unit_id, u.ref, u.name, u.intent, u.payload FROM rose_unit u JOIN rose_source s USING (source_id) "
         "WHERE s.name='wikidata' AND u.kind IN ('law','math','const','bio') "
         "AND JSON_LENGTH(u.payload, '$.tex') > 0 AND JSON_LENGTH(u.payload, '$.symbols') > 0")
    args = []
    if a.ref:
        q += " AND u.ref=%s"
        args.append(a.ref)
    if a.limit:
        q += f" LIMIT {int(a.limit)}"
    cur.execute(q, args)
    rows = cur.fetchall()
    consts = constant_defaults(cur)
    print(f"constants usable as defaults: {len(consts)}")
    stats, reasons = Counter(), Counter()
    for uid, ref, name, intent, payload in rows:
        p = json.loads(payload)
        for sym in p["symbols"]:
            if sym.get("quantity") in consts:
                sym["default"] = consts[sym["quantity"]]
        result = None
        last = None
        for tex in p["tex"]:
            try:
                src, typed = tex_to_law(law_name(ref), p.get("label") or name, tex, p["symbols"],
                                        f"wikidata:{p['wikidata']}")
            except TexError as e:
                last = ("reason", str(e))
                continue
            code, diags, _ = compile_source("module verify\n" + src, ref)
            errs = [d for d in diags if d.severity == "error"]
            if errs:
                last = ("error", f"{errs[0].code}: {errs[0].message}")
                continue
            result = (src, "tested" if typed else "parsed", tex)
            break
        if result:
            src, level, tex = result
            p["verify"] = {"status": level, "tex": tex}
            cur.execute("UPDATE rose_unit SET rose_src=%s, level=%s, payload=%s WHERE unit_id=%s",
                        (src, level, json.dumps(p, ensure_ascii=False, sort_keys=True), uid))
            stats[level] += 1
        else:
            kind, msg = last or ("reason", "no formula")
            p["verify"] = {"status": "rejected", kind: msg}
            cur.execute("UPDATE rose_unit SET rose_src=NULL, level='imported', payload=%s WHERE unit_id=%s",
                        (json.dumps(p, ensure_ascii=False, sort_keys=True), uid))
            stats["inconsistent" if kind == "error" else "not_convertible"] += 1
            reasons[msg.split(":")[0] if kind == "error" else msg] += 1
        if sum(stats.values()) % 500 == 0:
            con.commit()
    con.commit()
    print(f"formulas: {len(rows)}  {dict(stats)}")
    print("top reasons:", reasons.most_common(12))


if __name__ == "__main__":
    sys.exit(main())
