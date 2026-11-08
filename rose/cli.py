"""rosec - the Rose compiler command line.

  rosec plan "<task text>" [--json] [-k 8]     classify a new task, list the best solution paths
  rosec search "<query>" [--kind law] [--json]
  rosec check FILE.rose [--json]
  rosec compile FILE.rose [-o OUT.py] [--json]  writes OUT.py and OUT.lock.json
  rosec test FILE.rose                          compile and run the tests
  rosec get REF [--json]                        show one unit
plan/search/get use the built-in knowledge (std/catalog.jsonl); --db uses the corpus database.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

from .compiler import VERSION, compile_source
from .corpus import Corpus
from .knowledge import Knowledge


def knowledge(db=False):
    """The compiler's built-in knowledge (std/catalog). The corpus database is optional: with --db
    search/plan use it, and with ROSE_DB_NAME set it resolves refs the catalog lacks (oeis:...)."""
    if db:
        return Corpus()
    return Knowledge(fallback=Corpus() if os.environ.get("ROSE_DB_NAME") else None)


def _diags(diags, as_json):
    if as_json:
        return [d.to_json() for d in diags]
    for d in diags:
        print(str(d), file=sys.stderr)
        for f in d.fix:
            print(f"    fix: {json.dumps(f, ensure_ascii=False)}", file=sys.stderr)


def cmd_compile(a, write=True):
    src = open(a.file, encoding="utf-8").read()
    code, diags, lock = compile_source(src, os.path.basename(a.file), knowledge())
    out = a.out or os.path.splitext(a.file)[0] + ".py"
    if a.json:
        print(json.dumps({"ok": code is not None, "output": out if code and write else None,
                          "diagnostics": _diags(diags, True), "lock": lock}, ensure_ascii=False, indent=1))
    else:
        _diags(diags, False)
    if code is None:
        return 1, None
    if write:
        with open(out, "w", encoding="utf-8") as f:
            f.write(code)
        with open(os.path.splitext(out)[0] + ".lock.json", "w", encoding="utf-8") as f:
            json.dump({"rosec": VERSION, "source": a.file, "units": lock}, f, indent=1, ensure_ascii=False)
        if not a.json:
            print(f"wrote {out} ({len(lock)} corpus units pinned)")
    return 0, code


def main(argv=None):
    ap = argparse.ArgumentParser(prog="rosec", description=f"Rose compiler {VERSION}")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan"); p.add_argument("task"); p.add_argument("--json", action="store_true")
    p.add_argument("-k", type=int, default=8)
    p = sub.add_parser("search"); p.add_argument("query"); p.add_argument("--kind")
    p.add_argument("--json", action="store_true"); p.add_argument("-k", type=int, default=10)
    for name in ("check", "compile", "test"):
        p = sub.add_parser(name); p.add_argument("file"); p.add_argument("-o", "--out")
        p.add_argument("--json", action="store_true")
    p = sub.add_parser("get"); p.add_argument("ref"); p.add_argument("--json", action="store_true")
    for name in ("plan", "search", "get"):
        sub.choices[name].add_argument("--db", action="store_true", help="use the corpus database")
    a = ap.parse_args(argv)

    if a.cmd in ("plan", "search", "get"):
        corpus = knowledge(a.db)
        if not corpus.online:
            print(f"knowledge unavailable: {corpus.error}", file=sys.stderr)
            return 2
        if a.cmd == "get":
            u = corpus.get(a.ref)
            if not u:
                print(f"unknown ref {a.ref}", file=sys.stderr)
                return 1
            print(json.dumps(u, ensure_ascii=False, indent=1, default=str))
            return 0
        if a.cmd == "search":
            hits, notes = corpus.search(a.query, k=a.k, kind=a.kind)
            if a.json:
                print(json.dumps({"hits": hits, "notes": notes}, ensure_ascii=False, indent=1))
            else:
                for n in notes:
                    print("note:", n, file=sys.stderr)
                for h in hits:
                    print(f"{h['similarity']:.3f}  {h['kind']:<7} {h['level']:<9} {h['ref']:<55} {h['name'][:60]}")
            return 0
        r = corpus.plan(a.task, k=a.k)
        if a.json:
            print(json.dumps(r, ensure_ascii=False, indent=1))
            return 0
        print(f"task:      {r['task']}")
        print(f"category:  {r['category']}  (margin {r['confidence']:.2f} over the next category)")
        print("           best similarity per category: " + ", ".join(f"{c} {w:.2f}" for c, w in r["distribution"].items()))
        q = r.get("quantities") or {}
        if q.get("given") or q.get("wanted"):
            print(f"quantities: given {', '.join(q['given']) or '-'}; wanted {', '.join(q['wanted']) or '-'}")
        for w in r["warnings"]:
            print(f"WARNING:   {w}")
        print("best solution paths:")
        for i, h in enumerate(r["paths"], 1):
            extra = f", proved by {', '.join(h['proved_by'])}" if h.get("proved_by") else ""
            print(f" {i}. {h['ref']}  [{h['kind']}, {h['level']}{extra}, {h['license']}]  sim {h['similarity']:.2f}")
            print(f"    {h['name'][:100]}")
            print(f"    -> {h['how']}")
        for n in r["notes"]:
            print("note:", n)
        return 0

    if a.cmd == "check":
        src = open(a.file, encoding="utf-8").read()
        code, diags, lock = compile_source(src, os.path.basename(a.file), knowledge())
        if a.json:
            print(json.dumps({"ok": code is not None, "diagnostics": _diags(diags, True)}, ensure_ascii=False,
                             indent=1))
        else:
            _diags(diags, False)
            print("ok" if code is not None else f"{sum(d.severity == 'error' for d in diags)} error(s)")
        return 0 if code is not None else 1
    if a.cmd == "compile":
        return cmd_compile(a)[0]
    if a.cmd == "test":
        rc, code = cmd_compile(a, write=False)
        if code is None:
            return rc
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(code)
        try:
            return subprocess.run([sys.executable, "-I", f.name], timeout=20).returncode
        finally:
            os.unlink(f.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
