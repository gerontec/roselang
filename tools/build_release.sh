#!/bin/sh
# Release build - runs on the build host (dell), never on a notebook.
#   1. built-in sets from the corpus   2. prebuilt knowledge index   3. self-test   4. wheel + sdist
set -e
cd "$(dirname "$0")/.."
[ -f local.env ] && set -a && . ./local.env && set +a
python3 tools/export_pack.py mathlib
python3 tools/export_pack.py rosetta
python3 -c 'from rose.knowledge import build_prebuilt; print("prebuilt index", build_prebuilt())'
python3 tests/run_tests.py
ROSE_NO_EMBED=1 python3 tests/run_plan.py | tail -1
rm -rf dist build *.egg-info
python3 -m build
ls -la dist
