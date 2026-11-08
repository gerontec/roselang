#!/usr/bin/env python3
"""Browsable overview of the top PyPI packages for GitHub: docs/pypi/README.md (index) and one
Markdown page per topic (Trove classifier, two levels) - name, what it is for, licence, whether it
installs on CPython 3.14, install line, cleaned README extract. A package's full entry is on the page
of its first topic; its other topics list it in one line. Packages without a topic: pages by letter.
Source: the cache of import_pypi.py fetch (data/pypi). Usage: pypi_overview.py [--out docs/pypi]"""
import argparse
import collections
import datetime as dt
import gzip
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import import_pypi as P          # noqa: E402
import pypi_dataset as D         # noqa: E402

INSTALL = {"wheel": "installs (wheel)", "sdist": "installs from source (sdist only)", None: "does not install on CPython 3.14"}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "other"


def anchor(heading):
    """GitHub heading anchor: lower case, punctuation except - and _ dropped, spaces -> -."""
    return re.sub(r"[^a-z0-9 _-]", "", heading.lower()).replace(" ", "-")


def topic_key(t):
    parts = t.split(" / ")
    return " / ".join(parts[:2])


def entry(r, rank):
    lines = [f"### {r['name']}", "",
             f"{r.get('summary') or '(no summary)'}", "",
             f"`pip install {r['name']}` · {INSTALL[r.get('install_cp314')]} · licence: {r.get('license') or 'not stated'}"
             f" · rank {rank} · last release {r.get('last_release') or '?'} · [PyPI]({r['url']})"
             + (f" · [docs]({r['docs']})" if r.get("docs") else "")
             + (f" · [source]({r['source']})" if r.get("source") else ""), ""]
    if r.get("readme"):
        body = r["readme"]
        # keep the extract readable inside the page: no top-level headings, fenced code untouched
        lines += ["<details><summary>README extract</summary>", "", body, "", "</details>", ""]
    elif r.get("share_alike"):
        lines += ["_README extract left out: share-alike licence._", ""]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "pypi"))
    a = ap.parse_args()
    rows = P.top_list()["rows"]
    recs = []
    for rank, row in enumerate(rows, 1):
        path = os.path.join(P.CACHE, P.norm(row["project"]) + ".json.gz")
        if os.path.exists(path):
            recs.append((rank, D.record(json.load(gzip.open(path)))))
    pages, refs = collections.defaultdict(list), collections.defaultdict(list)
    for rank, r in recs:
        tps = list(dict.fromkeys(topic_key(t) for t in (r.get("topics") or [])))
        if tps:
            pages[tps[0]].append((rank, r))
            for t in tps[1:]:
                refs[t].append((rank, r, tps[0]))
        else:
            c = P.norm(r["name"])[0]
            pages["Unclassified / " + (c.upper() if c.isalpha() else "0-9")].append((rank, r))
    os.makedirs(a.out, exist_ok=True)
    for f in os.listdir(a.out):
        if f.endswith(".md"):
            os.remove(os.path.join(a.out, f))
    index = collections.defaultdict(list)
    for t in sorted(set(pages) | set(refs)):
        own = sorted(pages.get(t, []), key=lambda x: x[0])
        other = sorted(refs.get(t, []), key=lambda x: x[0])
        name = slug(t) + ".md"
        with open(os.path.join(a.out, name), "w", encoding="utf-8") as f:
            f.write(f"# {t}\n\n[Index](README.md) · {len(own)} packages on this page"
                    + (f", {len(other)} more listed under another topic" if other else "") + ", by downloads.\n\n")
            for rank, r in own:
                f.write(entry(r, rank) + "\n")
            if other:
                f.write("## Also in this topic\n\n")
                for rank, r, home in other:
                    f.write(f"- [{r['name']}]({slug(home)}.md#{anchor(r['name'])}) - {r.get('summary') or ''}\n")
        index[t.split(" / ")[0]].append((t, name, len(own) + len(other)))
    n_ok = sum(1 for _, r in recs if r.get("install_cp314"))
    n_rd = sum(1 for _, r in recs if r.get("readme"))
    with open(os.path.join(a.out, "README.md"), "w", encoding="utf-8") as f:
        f.write("# What the top PyPI packages are for\n\n"
                f"The {len(recs):,} most-downloaded Python packages (last 30 days, "
                f"[hugovk/top-pypi-packages](https://hugovk.dev/top-pypi-packages/), built {dt.date.today().isoformat()}), "
                "grouped by their Trove topics: what each package is for, its licence, whether it installs on "
                "CPython 3.14 (Linux x86_64), and a short README extract cleaned for reading by people and LLMs "
                "(badges, images, HTML and link targets removed; intro, features, one example, section names).\n\n"
                f"- installable on CPython 3.14: {n_ok:,} · with README extract: {n_rd:,}\n"
                "- metadata as each project published it on PyPI; a README extract is the project's own text "
                "under its licence, and is left out for share-alike licences\n"
                "- generated by `tools/pypi_overview.py`; machine-readable in `rose/std/catalog.jsonl` "
                "(cards `pypi:<name>`, kind `lib`) and via `rose.exists()`\n\n")
        for top in sorted(index):
            f.write(f"## {top}\n\n")
            for t, name, n in sorted(index[top]):
                f.write(f"- [{t}]({name}) ({n})\n")
            f.write("\n")
    sizes = sorted((os.path.getsize(os.path.join(a.out, x)), x) for x in os.listdir(a.out))
    print(f"{len(recs)} packages, {len(sizes)} pages, largest {sizes[-1][0] / 1e3:.0f} KB ({sizes[-1][1]}), "
          f"total {sum(s for s, _ in sizes) / 1e6:.1f} MB")


if __name__ == "__main__":
    sys.exit(main())
