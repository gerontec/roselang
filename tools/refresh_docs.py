#!/usr/bin/env python3
"""Count first, then renew the documentation.

1. tools/stats.py counts the shipped knowledge, the packs and the local corpus and writes
   docs/STATISTICS.md and docs/stats.json.
2. Every number in README.md, TODO.md and docs/*.md that is marked as
       <!--stat:KEY-->value<!--/stat-->
   is replaced by the current value of KEY (dotted path into stats.json, e.g. source.grin).
   GitHub does not show the markers. Unknown keys are reported and left as they are.

3. Size guard: warns about shipped or tracked files near the limits (PyPI 100 MB per file,
   GitHub 100 MB per file, warning at 50 MB): any file over 80 MB in rose/std, dist or a pack, and any
   git-tracked file over 50 MB.

Usage: refresh_docs.py [--check]    --check: only report what would change (exit 1 if anything is stale)
"""
import argparse
import glob
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
MARK = re.compile(r"<!--stat:([A-Za-z0-9_.-]+)-->(.*?)<!--/stat-->", re.S)


def lookup(S, key):
    v = S
    for part in key.split("."):
        if not isinstance(v, dict) or part not in v:
            raise KeyError(key)
        v = v[part]
    return v


def fmt(v):
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, int):
        return f"{v:,}".replace(",", " ")
    if isinstance(v, float):
        return f"{v:,.1f}".replace(",", " ")
    return str(v)


def size_warnings(limit_mb=80, git_mb=50):
    import subprocess
    out = []
    import zlib

    def packed(path):            # a wheel is a zip: what a file costs in it (deflate), streamed
        if path.endswith((".gz", ".whl", ".zip")):
            return os.path.getsize(path)
        z, n = zlib.compressobj(6), 0
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 22), b""):
                n += len(z.compress(chunk))
        return n + len(z.flush())
    # the wheels themselves, and the data files that go into them; former packs (now built-in sets) are skipped
    paths = glob.glob(os.path.join(ROOT, "dist", "*")) + glob.glob(os.path.join(ROOT, "packs", "*", "dist", "*"))
    paths += [p for p in glob.glob(os.path.join(ROOT, "rose", "std", "**", "*"), recursive=True) if os.path.isfile(p)]
    for p in glob.glob(os.path.join(ROOT, "packs", "*", "rose_*", "*")):
        name = os.path.basename(os.path.dirname(p))
        if not os.path.exists(os.path.join(ROOT, "rose", "std", "sets", name.replace("rose_", "", 1) + ".jsonl.gz")):
            paths.append(p)
    for path in paths:
        if os.path.isfile(path) and os.path.getsize(path) > 20e6 and packed(path) > limit_mb * 1e6:
            out.append(f"{os.path.relpath(path, ROOT)}: {packed(path) / 1e6:.0f} MB packed "
                       f"(> {limit_mb} MB; PyPI limit is 100 MB per file)")
    try:
        files = subprocess.run(["git", "-C", ROOT, "ls-files", "-z"], capture_output=True, check=True).stdout.split(b"\0")
        for f in files:
            path = os.path.join(ROOT, f.decode())
            if f and os.path.isfile(path) and os.path.getsize(path) > git_mb * 1e6:
                out.append(f"{f.decode()} is tracked in git with {os.path.getsize(path) / 1e6:.0f} MB "
                           f"(GitHub warns at 50 MB, rejects 100 MB)")
    except (OSError, subprocess.CalledProcessError):
        pass
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    import stats
    S = stats.main()
    files = [os.path.join(ROOT, f) for f in ("README.md", "TODO.md")] + sorted(glob.glob(os.path.join(ROOT, "docs", "*.md")))
    stale, unknown = 0, []
    for path in files:
        text = open(path, encoding="utf-8").read()

        def sub(m):
            nonlocal stale
            key, old = m.group(1), m.group(2)
            try:
                new = fmt(lookup(S, key))
            except KeyError:
                unknown.append(f"{os.path.relpath(path, ROOT)}: {key}")
                return m.group(0)
            if new != old:
                stale += 1
                print(f"{os.path.relpath(path, ROOT)}: {key}: {old} -> {new}")
            return f"<!--stat:{key}-->{new}<!--/stat-->"
        new_text = MARK.sub(sub, text)
        if new_text != text and not a.check:
            open(path, "w", encoding="utf-8").write(new_text)
    for w in size_warnings():
        print("SIZE:", w, file=sys.stderr)
    for u in unknown:
        print("unknown key:", u, file=sys.stderr)
    print(f"{stale} value(s) {'stale' if a.check else 'updated'}; STATISTICS.md and stats.json regenerated")
    return 1 if (a.check and stale) else 0


if __name__ == "__main__":
    sys.exit(main())
