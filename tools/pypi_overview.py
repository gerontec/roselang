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

PART_BYTES = 350_000
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
        if f.endswith(".md") and f != "DATASET.md":           # DATASET.md is written by hand
            os.remove(os.path.join(a.out, f))
    # split big topics into parts (GitHub stops rendering very large Markdown files); remember each
    # package's file so that cross-references point to the right part
    parts, home_file = {}, {}
    for t in set(pages) | set(refs):
        own = sorted(pages.get(t, []), key=lambda x: x[0])
        chunks, cur, size = [], [], 0
        for rank, r in own:
            e = entry(r, rank)
            if cur and size + len(e) > PART_BYTES:
                chunks.append(cur)
                cur, size = [], 0
            cur.append((rank, r, e))
            size += len(e)
        chunks.append(cur)
        names = [slug(t) + (f"-{i + 1}" if i else "") + ".md" for i in range(len(chunks))]
        parts[t] = list(zip(names, chunks))
        for fn, ch in parts[t]:
            for _, r, _ in ch:
                home_file[r["name"]] = fn
    index = collections.defaultdict(list)
    for t in sorted(parts):
        other = sorted(refs.get(t, []), key=lambda x: x[0])
        n_own = sum(len(ch) for _, ch in parts[t])
        for i, (fn, ch) in enumerate(parts[t]):
            nav = " · ".join(f"[part {j + 1}]({x})" if j != i else f"part {j + 1}" for j, (x, _) in enumerate(parts[t])) \
                if len(parts[t]) > 1 else ""
            with open(os.path.join(a.out, fn), "w", encoding="utf-8") as f:
                f.write(f"# {t}" + (f" (part {i + 1} of {len(parts[t])})" if len(parts[t]) > 1 else "") +
                        f"\n\n[Index](README.md) · {n_own} packages in this topic"
                        + (f", {len(other)} more listed under another topic" if other else "") + ", by downloads."
                        + (f"\n\n{nav}" if nav else "") + "\n\n")
                for _, _, e in ch:
                    f.write(e + "\n")
                if other and i == len(parts[t]) - 1:
                    f.write("## Also in this topic\n\n")
                    for rank, r, home in other:
                        f.write(f"- [{r['name']}]({home_file.get(r['name'], slug(home) + '.md')}#{anchor(r['name'])})"
                                f" - {r.get('summary') or ''}\n")
        index[t.split(" / ")[0]].append((t, parts[t][0][0], n_own + len(other)))
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
                "- generated by `tools/pypi_overview.py`; machine-readable in `rose/std/catalog.jsonl.gz` "
                "(cards `pypi:<name>`, kind `lib`) and via `rose.exists()`\n"
                "- all ~900 000 PyPI projects in the same form: [DATASET.md](DATASET.md) (release assets)\n\n")
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
