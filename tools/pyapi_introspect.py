#!/usr/bin/env python3
"""Runs INSIDE the sandbox container (no network, read-only, non-root): import one installed
distribution and list its public API - path, object kind, signature, first docstring paragraph.
Nothing is called except imports. Output: one JSON document on stdout.
  python pyapi_introspect.py <distribution> <site dir>"""
import importlib
import inspect
import json
import os
import pkgutil
import re
import sys
import warnings

MAX_OBJECTS = 1500
MAX_MODULES = 300


def top_levels(dist, site):
    """Top-level import names of a distribution from its RECORD (not its dependencies)."""
    norm = re.sub(r"[-_.]+", "_", dist).lower()
    for d in os.listdir(site):
        if d.endswith(".dist-info") and re.sub(r"[-_.]+", "_", d[:-10].rsplit("-", 1)[0]).lower() == norm:
            tops = set()
            for line in open(os.path.join(site, d, "RECORD"), encoding="utf-8"):
                p = line.split(",")[0]
                head = p.split("/")[0]
                if head.endswith((".dist-info", ".data")) or head.startswith(("_", "..")) or head == "bin":
                    continue
                if "/" in p:
                    tops.add(head)
                elif p.endswith(".py"):
                    tops.add(p[:-3])
            return sorted(t for t in tops if t.isidentifier()), d
    return [], None


def summary(obj):
    doc = inspect.getdoc(obj) or ""
    paras = [p for p in doc.strip().split("\n\n") if p.strip()]
    name = getattr(obj, "__name__", "")
    if len(paras) > 1 and name and re.match(rf"\s*{re.escape(name)}\s*\(", paras[0]):
        paras = paras[1:]
    return " ".join(paras[0].split())[:500] if paras else ""


def sig(obj):
    try:
        return str(inspect.signature(obj))[:400]
    except (TypeError, ValueError):
        return None


def public(name, obj, top):
    if name.startswith("_") or not callable(obj):
        return False
    if inspect.isclass(obj) and issubclass(obj, (BaseException, Warning)):
        return False
    mod = getattr(obj, "__module__", None) or ""
    return mod == top or mod.startswith(top + ".")


def walk(top):
    out, seen, errors = [], set(), []
    try:
        root = importlib.import_module(top)
    except BaseException as e:                   # SystemExit included: foreign code
        return [], [f"{top}: {type(e).__name__}: {str(e)[:120]}"]
    mods = [root]
    if hasattr(root, "__path__"):
        for mi in pkgutil.walk_packages(root.__path__, top + "."):
            if len(mods) >= MAX_MODULES:
                break
            if any(p.startswith("_") or p in ("tests", "test", "testing", "conftest", "examples", "benchmarks")
                   for p in mi.name.split(".")[1:]):
                continue
            try:
                mods.append(importlib.import_module(mi.name))
            except BaseException as e:
                errors.append(f"{mi.name}: {type(e).__name__}")
    for mod in mods:
        names = getattr(mod, "__all__", None)
        if not isinstance(names, (list, tuple)):
            names = [n for n in dir(mod) if not n.startswith("_")]
        for name in names:
            if len(out) >= MAX_OBJECTS:
                return out, errors + ["truncated"]
            try:
                obj = getattr(mod, name, None)
            except BaseException:
                continue
            if obj is None or not isinstance(name, str) or not public(name, obj, top) or id(obj) in seen:
                continue
            seen.add(id(obj))
            canon = getattr(obj, "__name__", name)
            path = f"{obj.__module__}.{canon}" if isinstance(canon, str) and canon.isidentifier() else f"{mod.__name__}.{name}"
            out.append({"path": path, "public": f"{mod.__name__}.{name}",
                        "object": "class" if inspect.isclass(obj) else "function",
                        "signature": sig(obj), "doc": summary(obj)})
    return out, errors


def main():
    dist, site = sys.argv[1], sys.argv[2]
    sys.path.insert(0, site)
    warnings.simplefilter("ignore")
    tops, info = top_levels(dist, site)
    version = info[:-10].rsplit("-", 1)[1] if info else None
    objs, errs = [], []
    for t in tops:
        o, e = walk(t)
        objs += o
        errs += e
    json.dump({"dist": dist, "version": version, "tops": tops, "objects": objs, "errors": errs[:50]},
              sys.stdout, ensure_ascii=False)


if __name__ == "__main__":
    main()
