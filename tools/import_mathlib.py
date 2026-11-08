#!/usr/bin/env python3
"""Import the theorems of Lean mathlib4 (Apache-2.0) as math units with level `proven`.

Reads the .lean sources of a local clone (git clone --depth 1 .../mathlib4), no Lean needed:
every top-level `theorem`/`lemma` that is not `private`, with
  ref        mathlib:<full name>          (namespace + declared name, `_root_.` respected)
  name       full Lean name
  intent     "<named result from the docstring, e.g. Four squares theorem> - <docstring> -
              <words of the name> : <statement>"   (the search key)
  payload    lean name, statement (text up to `:=`), docstring, file, line, commit, named
  level      proven: mathlib is checked by Lean in CI at this commit
The proof itself is not stored.
Usage: import_mathlib.py --repo ../data/mathlib4 [--limit N] [--dry-run]
"""
import argparse
import os
import re
import subprocess
import sys

import rose_db as R

DECL = re.compile(r"^((?:@\[[^\]]*\]\s*)*)((?:(?:private|protected|nonrec|noncomputable|scoped)\s+)*)"
                  r"(theorem|lemma)\s+([^\s(:{\[]+)")
NS = re.compile(r"^(namespace|section|noncomputable\s+section)\b\s*([^\s]*)")
END = re.compile(r"^end\b\s*([^\s]*)")
BOLD = re.compile(r"\*\*(.+?)\*\*")


def statement(lines, i, first_rest):
    """Text from after the name up to the first top-level `:=` (or `|` pattern / `where`)."""
    buf, depth, text = [], 0, first_rest
    j = i
    while True:
        k = 0
        while k < len(text):
            ch = text[k]
            if ch in "([{⟨":
                depth += 1
            elif ch in ")]}⟩":
                depth -= 1
            elif depth <= 0 and text.startswith(":=", k):
                buf.append(text[:k])
                return " ".join(" ".join(buf).split())
            k += 1
        buf.append(text)
        j += 1
        if j >= len(lines) or j - i > 40:
            return " ".join(" ".join(buf).split())
        text = lines[j]
        if depth <= 0 and (text.startswith("  | ") or re.match(r"^\s*where\b", text)):
            return " ".join(" ".join(buf).split())


def docstring_before(lines, i):
    j = i - 1
    while j >= 0 and lines[j].strip().startswith("@["):
        j -= 1
    if j < 0 or not lines[j].rstrip().endswith("-/"):
        return None
    end = j
    while j >= 0 and "/--" not in lines[j]:
        j -= 1
    if j < 0:
        return None
    doc = " ".join(l.strip() for l in lines[j:end + 1])
    doc = doc.split("/--", 1)[1].rsplit("-/", 1)[0]
    return " ".join(doc.split())


def humanize(name):
    words = re.split(r"[._]", name)
    return " ".join(w for w in words if w and w not in ("_root_",))


def parse_file(path, rel):
    lines = open(path, encoding="utf-8").read().split("\n")
    stack = []                          # [(kind, name)]
    in_comment = 0
    for i, line in enumerate(lines):
        s = line.strip()
        # block comments (non-doc) can contain the word theorem
        if in_comment:
            in_comment += line.count("/-") - line.count("-/")
            continue
        if s.startswith("/-") and not s.startswith("/--"):
            in_comment = line.count("/-") - line.count("-/")
            continue
        m = NS.match(line)
        if m:
            stack.append((m.group(1).split()[-1], m.group(2)))
            continue
        m = END.match(line)
        if m:
            if stack:
                stack.pop()
            continue
        m = DECL.match(line)
        if not m:
            continue
        mods, kw, short = m.group(2), m.group(3), m.group(4)
        if "private" in mods:
            continue
        if short.startswith("_root_."):
            full = short[len("_root_."):]
        else:
            ns = ".".join(n for k, n in stack if k == "namespace" and n)
            full = f"{ns}.{short}" if ns else short
        st = statement(lines, i, line[m.end():])
        doc = docstring_before(lines, i)
        named = BOLD.findall(doc or "")
        yield {"name": full, "statement": st[:2000], "doc": doc, "named": named, "file": rel, "line": i + 1,
               "attrs": m.group(1).strip() or None}


def units(repo):
    commit = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    base = os.path.join(repo, "Mathlib")
    for dp, _, fs in os.walk(base):
        for f in sorted(fs):
            if not f.endswith(".lean"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, repo)
            for d in parse_file(p, rel):
                parts = []
                if d["named"]:
                    parts.append("; ".join(d["named"]))
                if d["doc"]:
                    parts.append(d["doc"][:500])
                parts.append(humanize(d["name"]) + " : " + d["statement"].lstrip(": ")[:600])
                yield {"ref": "mathlib:" + d["name"], "name": d["name"][:255], "intent": " - ".join(parts),
                       "url": f"https://github.com/leanprover-community/mathlib4/blob/{commit}/{rel}#L{d['line']}",
                       "payload": {"lean": d["name"], "statement": d["statement"], "doc": d["doc"],
                                   "named": d["named"], "file": rel, "line": d["line"], "commit": commit,
                                   "attrs": d["attrs"], "status": "proved", "domain": "math"}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "mathlib4"))
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    seen, rows, n = set(), [], 0
    con = cur = sid = None
    if not a.dry_run:
        con = R.connect()
        cur = con.cursor()
        sid = R.ensure_source(cur, "mathlib", "https://github.com/leanprover-community/mathlib4", "Apache-2.0", False,
                              "Lean mathlib4 theorem statements (no proofs), checked by Lean at the recorded commit")
        con.commit()
    named = 0
    for u in units(a.repo):
        if u["ref"] in seen:
            continue
        seen.add(u["ref"])
        n += 1
        named += bool(u["payload"]["named"])
        if a.dry_run:
            if n <= 5 or (u["payload"]["named"] and named <= 8):
                print(u["ref"], "|", u["intent"][:160])
        else:
            rows.append(R.unit_row(ref=u["ref"], kind="math", name=u["name"], intent=u["intent"], source_id=sid,
                                   source_url=u["url"], payload=u["payload"], level="proven"))
            if len(rows) >= 2000:
                R.upsert_units_many(cur, rows)
                con.commit()
                rows = []
                print(f"  {n}", flush=True)
        if a.limit and n >= a.limit:
            break
    if rows:
        R.upsert_units_many(cur, rows)
    if con:
        R.mark_imported(cur, sid)
        con.commit()
    print(f"done theorems: {n}, with a named result in the docstring: {named}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
