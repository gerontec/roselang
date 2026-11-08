#!/usr/bin/env python3
"""Compiler self-test: positive files must compile and pass, negative files must raise the
diagnostic code in their file name (tests/neg/<code>[_suffix].rose). Runs offline."""
import glob
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
os.environ.setdefault("ROSE_OFFLINE", "1")
from rose.compiler import compile_source  # noqa: E402

fails = 0
for f in sorted(glob.glob(os.path.join(HERE, "neg", "*.rose"))):
    want = os.path.basename(f).split("_")[0].split(".")[0].upper()
    _, diags, _ = compile_source(open(f).read(), os.path.basename(f))
    got = [d.code for d in diags]
    ok = want in got
    fails += not ok
    print(f"{'ok  ' if ok else 'FAIL'} neg {os.path.basename(f):<22} want {want} got {got}")
for f in sorted(glob.glob(os.path.join(HERE, "*.rose"))):
    code, diags, _ = compile_source(open(f).read(), os.path.basename(f))
    if code is None:
        fails += 1
        print(f"FAIL pos {os.path.basename(f)}: " + "; ".join(map(str, diags)))
        continue
    r = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True, timeout=20)
    fails += r.returncode != 0
    print(f"{'ok  ' if r.returncode == 0 else 'FAIL'} pos {os.path.basename(f):<22} {r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-300:]}")
# the generated standard library must parse completely (every `use` of std parses its whole file)
sys.path.insert(0, os.path.dirname(HERE))
from rose.parser import parse  # noqa: E402
for f in sorted(glob.glob(os.path.join(HERE, "..", "rose", "std", "**", "*.rose"), recursive=True)):
    name = os.path.relpath(f, os.path.join(HERE, "..", "rose"))
    try:
        n = len(parse(open(f, encoding="utf-8").read(), name).items)
        print(f"ok   std {name:<26} {n} items")
    except Exception as e:
        fails += 1
        print(f"FAIL std {name:<26} {e}")
print("all ok" if not fails else f"{fails} failure(s)")
sys.exit(1 if fails else 0)
