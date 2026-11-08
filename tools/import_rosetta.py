#!/usr/bin/env python3
"""Import Rosetta Code tasks and their Python solutions (kind algo, refs rc:<Task_name>).

robots.txt of rosettacode.org (Miraheze) disallows /w/ (the API) and every ?action= URL, so the
importer reads only the ordinary article pages /wiki/<Task> and the category pages, politely:
one network request every --delay seconds (default 2), every page cached under data/rosetta/.

Per task:   description (text before the first language section), number of languages,
            Python solutions (every python code block of the Python section, with the
            "Works with ... version" note in force), the first "Output:" blocks of that section.
Licence:    Rosetta Code content is GNU FDL 1.3 (share-alike) - stored with share_alike=1, so it
            never enters rose/std/; it is exported as a separate pack.
Level:      a solution that compiles as Python 3 (compile(), nothing is executed) -> parsed.
Usage: import_rosetta.py [--limit N] [--delay 2] [--dry-run] [--task "100 doors"]
"""
import argparse
import gzip
import hashlib
import html
import os
import re
import sys
import time
import urllib.parse

import requests

import rose_db as R

BASE = "https://rosettacode.org"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "rosetta")
CATEGORY = "/wiki/Category:Programming_Tasks"
LICENSE = "GFDL-1.3"
_last = [0.0]


def fetch(path, delay):
    os.makedirs(CACHE, exist_ok=True)
    f = os.path.join(CACHE, hashlib.sha1(path.encode()).hexdigest() + ".html.gz")
    if os.path.exists(f):
        with gzip.open(f, "rt", encoding="utf-8") as fh:
            return fh.read()
    if os.path.exists(f[:-3]):                      # uncompressed cache of an earlier run
        return open(f[:-3], encoding="utf-8").read()
    wait = delay - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    for attempt in range(4):
        r = requests.get(BASE + path, headers={"User-Agent": R.USER_AGENT}, timeout=60)
        _last[0] = time.time()
        if r.status_code == 200:
            break
        if r.status_code in (429, 503):
            time.sleep(30 * (attempt + 1))
            continue
        r.raise_for_status()
    r.raise_for_status()
    with gzip.open(f, "wt", encoding="utf-8") as fh:
        fh.write(r.text)
    return r.text


def text_of(fragment):
    t = re.sub(r"<(script|style)\b.*?</\1>", " ", fragment, flags=re.S)
    t = re.sub(r"<br\s*/?>|</p>|</li>|</dd>|</h[1-6]>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t).strip()


def task_list(delay):
    tasks, path = [], CATEGORY
    while path:
        page = fetch(path, delay)
        m = re.search(r'<div id="mw-pages">(.*?)<div class="printfooter"', page, re.S) or \
            re.search(r'<div id="mw-pages">(.*)', page, re.S)
        block = m.group(1) if m else ""
        for href, title in re.findall(r'<li><a href="(/wiki/[^"#]+)" title="([^"]+)"', block):
            tasks.append((html.unescape(title), href))
        nxt = re.search(r'<a href="([^"]*pagefrom=[^"#]+)[^"]*"[^>]*>next page</a>', page)
        path = None
        if nxt:
            q = urllib.parse.parse_qs(urllib.parse.urlparse(html.unescape(nxt.group(1))).query)
            path = CATEGORY + "?pagefrom=" + urllib.parse.quote_plus(q["pagefrom"][0])  # article path, not /w/
    return list(dict.fromkeys(tasks))


H2 = re.compile(r'<div class="mw-heading mw-heading2"><h2 id="([^"]+)"')


def parse_task(page):
    body = page.split('class="mw-content-ltr mw-parser-output"', 1)[-1].split(">", 1)[-1]
    heads = [(m.start(), html.unescape(m.group(1))) for m in H2.finditer(body)]
    first = heads[0][0] if heads else len(body)
    intro = re.sub(r'<div class="infobox".*?</div>', "", body[:first], count=1, flags=re.S)
    intro = re.sub(r'<div id="toc".*', "", intro, flags=re.S)
    desc = text_of(intro)
    langs = [h for _, h in heads]
    py = None
    for k, (pos, hid) in enumerate(heads):
        if hid == "Python":
            end = heads[k + 1][0] if k + 1 < len(heads) else len(body)
            py = body[pos:end]
            break
    solutions, outputs = [], []
    if py:
        version = None
        for m in re.finditer(r'<div class="examplemeta workswith">(.*?)</div>|'
                             r'<div class="mw-highlight mw-highlight-lang-(python[0-9]*)[^"]*"[^>]*><pre>(.*?)</pre></div>|'
                             r'<dt>Output:</dt></dl></div>\s*<pre>(.*?)</pre>', py, re.S):
            if m.group(1) is not None:
                v = re.search(r"version\s+([0-9][^<\s]*)", text_of(m.group(1)))
                version = v.group(1) if v else None
            elif m.group(3) is not None:
                code = html.unescape(re.sub(r"<[^>]+>", "", m.group(3))).replace("\xa0", " ")
                solutions.append({"code": code, "works_with": version})
            elif m.group(4) is not None and len(outputs) < 3:
                outputs.append(html.unescape(re.sub(r"<[^>]+>", "", m.group(4)))[:2000])
    return desc, langs, solutions, outputs


def py3_ok(code):
    try:
        compile(code, "<rosetta>", "exec")
        return True
    except (SyntaxError, ValueError):
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--delay", type=float, default=2.0)
    ap.add_argument("--task")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    tasks = [(a.task, "/wiki/" + urllib.parse.quote(a.task.replace(" ", "_")))] if a.task else task_list(a.delay)
    print(f"tasks: {len(tasks)}", flush=True)
    if a.limit:
        tasks = tasks[:a.limit]
    con = cur = sid = None
    if not a.dry_run:
        con = R.connect()
        cur = con.cursor()
        sid = R.ensure_source(cur, "rosettacode", BASE, LICENSE, True,
                              "Rosetta Code tasks and Python solutions, article pages only (robots.txt)")
        con.commit()
    stats = {"tasks": 0, "with_python": 0, "solutions": 0, "py3": 0}
    for n, (title, href) in enumerate(tasks, 1):
        try:
            page = fetch(href, a.delay)
        except requests.RequestException as e:
            print(f"  skip {title}: {e}", file=sys.stderr)
            continue
        desc, langs, sols, outs = parse_task(page)
        for s in sols:
            s["py3"] = py3_ok(s["code"])
        stats["tasks"] += 1
        stats["with_python"] += bool(sols)
        stats["solutions"] += len(sols)
        stats["py3"] += sum(s["py3"] for s in sols)
        ref = "rc:" + title.replace(" ", "_")
        url = BASE + href
        intent = f"{title} - {desc[:600]}" if desc else title
        payload = {"task": title, "description": desc[:4000], "languages": len(langs),
                   "python_solutions": len(sols), "python3_solutions": sum(s["py3"] for s in sols),
                   "outputs": outs, "domain": "algorithm", "status": "solved" if sols else "no_python"}
        if a.dry_run:
            print(f"{ref}: {len(langs)} languages, {len(sols)} python ({payload['python3_solutions']} py3) | {desc[:100]}")
            continue
        uid = R.upsert_unit(cur, ref=ref, kind="algo", name=title, intent=intent, source_id=sid, source_url=url,
                            payload=payload, level="parsed" if payload["python3_solutions"] else "imported")
        cur.execute("SELECT unit_id FROM rose_unit WHERE ref=%s", (ref,))
        uid = cur.fetchone()[0]
        cur.execute("DELETE FROM rose_impl WHERE unit_id=%s AND lang='python'", (uid,))
        for s in sols:
            code = s["code"]
            cur.execute("INSERT IGNORE INTO rose_impl (unit_id, lang, code, code_sha, license, source_url, level) "
                        "VALUES (%s,'python',%s,%s,%s,%s,%s)",
                        (uid, code, R.sha256(code), LICENSE, url + "#Python", "parsed" if s["py3"] else "imported"))
        if n % 25 == 0:
            con.commit()
            print(f"  {n}/{len(tasks)} {stats}", flush=True)
    if con:
        R.mark_imported(cur, sid)
        con.commit()
    print("done", stats, flush=True)


if __name__ == "__main__":
    sys.exit(main())
