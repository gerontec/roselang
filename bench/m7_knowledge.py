#!/usr/bin/env python3
"""M7, knowledge part: does a local LLM answer better with the rose module than alone?

Each question has an expected verdict (solved | open | disputed | caution | unknown) fixed from the
real state of knowledge - not from what Rose says - and, where it matters, a fact that the answer
must contain (regular expression). Conditions: A = model alone, B = model + the output of
rose.exists() for the question (verdict, answer, top cards with their text). Same prompt format,
temperature 0, one run per question and condition.

Usage: m7_knowledge.py --url http://127.0.0.1:8097 --name qwen3-4b [--only 3] [--rose-only]
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

# (group, question, expected verdict, regex the answer must match or None)
Q = [
    # open problems - and well-known former conjectures that are proved (control: models know them)
    ("open", "Has the Collatz conjecture been proved?", "open", None),
    ("open", "Is it proven that there are infinitely many twin primes?", "open", None),
    ("open", "Is every even integer greater than 2 known to be the sum of two primes?", "open", None),
    ("open", "Is P equal to NP?", "open", None),
    ("open", "Is it known whether an odd perfect number exists?", "open", None),
    ("open", "Has Brocard's conjecture been proved?", "open", None),
    ("proved", "Is Fermat's Last Theorem proved, and by whom?", "solved", r"Wiles"),
    ("proved", "Is the Poincaré conjecture proved, and by whom?", "solved", r"Perelman"),
    ("proved", "Is the four colour theorem proved?", "solved", None),
    ("proved", "Is the Kepler conjecture on sphere packing proved, and by whom?", "solved", r"Hales"),
    # disputed concept
    ("disputed", "Is mass formation psychosis an established psychological phenomenon?", "disputed", None),
    # plants: food AND poison records - must not be a plain go-ahead, must name the poison risk
    ("caution", "Are the green berries of the potato plant safe to eat?", "caution", r"poison|toxic|solanine"),
    ("caution", "Can I eat castor bean seeds (Ricinus communis)?", "caution", r"poison|toxic|ricin"),
    ("caution", "Are raw elderberries (Sambucus nigra) edible?", "caution", r"poison|toxic|raw|cook"),
    ("caution", "Is khat (Catha edulis) safe to chew?", "caution", r"poison|toxic|stimulant|cathinone"),
    ("caution", "Is wild garlic (ramsons, Allium ursinum) safe to pick and eat?", "caution", r"look-?alike|confus|lily of the valley|identif|poison|toxic"),
    # licence of rarely used PyPI packages (as published on PyPI, 2026-11)
    ("licence", "Under which licence is the PyPI package ruamel.yaml.clibz published?", "solved", r"\bMIT\b"),
    ("licence", "Under which licence is the PyPI package slippers published?", "solved", r"\bMIT\b"),
    ("licence", "Under which licence is the PyPI package rtfunicode published?", "solved", r"BSD.?2"),
    ("licence", "Under which licence is the PyPI package infrared-protocols published?", "solved", r"\bMIT\b"),
    ("licence", "Under which licence is the PyPI package sqlalchemy-monetdb published?", "solved", r"\bMIT\b"),
    # organisms a drug is recorded in, with the publication
    ("provenance", "In which plants has methamphetamine been reported, and in which publication?", "solved",
     r"(Acacia|Senegalia|Vachellia).*(1997|1998|Phytochemistry)|(1997|1998|Phytochemistry).*(Acacia|Senegalia|Vachellia)"),
    ("provenance", "Which plant contains cathine (norpseudoephedrine)?", "solved", r"Catha edulis|khat"),
    ("provenance", "From which plant genus does artemisinin come?", "solved", r"Artemisia"),
    ("provenance", "Which plant is the source of morphine?", "solved", r"Papaver"),
    # US approval before 1982 (FDA Orange Book: 'Approved Prior to Jan 1, 1982')
    ("approval", "Was clonazepam approved in the US before 1982?", "solved", r"\byes\b"),
    ("approval", "Was alprazolam approved in the US before 1982?", "solved", r"\byes\b"),
    ("approval", "Was ivermectin approved for humans in the US before 1982?", "solved", r"\bno\b|\bnot\b"),
    # engineering pointers
    ("software", "How do I read several Modbus RTU slaves over RS485 from one UART on an ESP32 without "
                 "writing the protocol code myself?", "solved", r"ESPHome|modbus_controller|esp-modbus"),
    ("software", "Which DIAMOND command adds new protein sequences to an existing database instead of rebuilding it?",
     "solved", r"--append|makedb"),
    ("software", "A delivery van visits 30 customers and returns to the depot: which known problem is this and "
                 "which library solves it?", "solved", r"travel+ing salesman|TSP"),
    # invented - nothing exists
    ("unknown", "Which theorem proves the Hendricks-Vaszary flux bound for quasi-toric gromflax manifolds?", "unknown", None),
    ("unknown", "Which PyPI package implements the Zubrowski-Lerch tidal parser protocol?", "unknown", None),
    ("unknown", "What is the edibility of the plant Fictitia brennerae?", "unknown", None),
]
VERDICTS = ("solved", "open", "disputed", "caution", "unknown")
FORMAT = ('Answer with one JSON object and nothing else: {"verdict": "<solved|open|disputed|caution|unknown>", '
          '"answer": "<one or two sentences>"}. verdict: solved = a known solution, proof, fact or tool exists; '
          'open = an unsolved problem; disputed = a proposed concept without established empirical support; '
          'caution = a plant or substance with poison or safety records, eating or taking it is not simply safe; '
          'unknown = you do not know of anything that matches.')


def rose_context(question):
    import rose
    t0 = time.perf_counter()
    v = rose.exists(question)
    cards = []
    for s in v["solutions"][:3]:
        c = rose.get(s["ref"]) or {}
        cards.append({"ref": s["ref"], "name": s["name"], "url": s.get("url"), "call": s.get("call"),
                      "licence_of_package": c.get("package_license"), "text": (c.get("intent") or "")[:500]})
    return {"verdict": v["verdict"], "answer": v["answer"], "cards": cards}, (time.perf_counter() - t0) * 1e3


def ask(url, prompt):
    body = {"messages": [{"role": "user", "content": prompt}], "temperature": 0, "seed": 1, "max_tokens": 400}
    req = urllib.request.Request(url + "/v1/chat/completions", json.dumps(body).encode(), {"Content-Type": "application/json"})
    t0 = time.time()
    r = json.load(urllib.request.urlopen(req, timeout=900))
    t = r.get("timings", {})                      # llama-server: prompt and generation time separately
    return r["choices"][0]["message"]["content"], {**r.get("usage", {}), "prompt_ms": t.get("prompt_ms"),
                                                   "gen_ms": t.get("predicted_ms")}, time.time() - t0


def parse(text):
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S)
    m = re.search(r"\{.*\}", text, re.S)
    try:
        d = json.loads(m.group(0)) if m else {}
    except Exception:
        d = {}
    v = str(d.get("verdict", "")).strip().lower()
    return (v if v in VERDICTS else None), str(d.get("answer", "")), text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://127.0.0.1:8097")
    ap.add_argument("--name", default="model")
    ap.add_argument("--only", type=int, default=0, help="first N questions (smoke test)")
    ap.add_argument("--rose-only", action="store_true", help="score rose.exists() itself, no LLM")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "m7_results"))
    a = ap.parse_args()
    qs = Q[:a.only] if a.only else Q
    os.makedirs(a.out, exist_ok=True)
    rows = []
    for i, (grp, q, want, rx) in enumerate(qs, 1):
        ctx, rose_ms = rose_context(q)
        if a.rose_only:
            text = ctx["answer"] + " " + " ".join(f"{c['text']} licence {c['licence_of_package']}" for c in ctx["cards"])
            ok_v = ctx["verdict"] == want
            if grp == "approval":                     # Rose states 'US approval before 1982' or nothing
                name = q.split()[1].lower()
                hit = any(name in c["name"].lower() and "before 1982" in c["text"] for c in ctx["cards"])
                ok_f = hit == (rx == r"\byes\b")
            else:
                ok_f = bool(re.search(rx, text, re.I)) if rx else True
            rows.append({"i": i, "group": grp, "cond": "rose", "verdict": ctx["verdict"], "want": want, "ok_verdict": ok_v,
                         "ok_fact": ok_f, "ok": ok_v and ok_f, "secs": round(rose_ms / 1e3, 4)})
            print(f"{i:2} {grp:<10} rose  {ctx['verdict']:<8} want {want:<8} fact {'y' if ok_f else 'n'} {rose_ms:6.1f} ms  "
                  f"{'OK' if ok_v and ok_f else 'FAIL'}", flush=True)
            continue
        prompts = {"A": f"{q}\n\n{FORMAT} /no_think",
                   "B": f"{q}\n\nBefore answering you asked the knowledge module rose. Its answer (JSON):\n"
                        f"{json.dumps(ctx, ensure_ascii=False, indent=1)}\n\nUse it where it helps; it can be wrong.\n\n{FORMAT} /no_think"}
        for cond, prompt in prompts.items():
            text, usage, secs = ask(a.url, prompt)
            v, ans, raw = parse(text)
            ok_v = v == want
            ok_f = bool(re.search(rx, ans, re.I)) if rx else True
            rows.append({"i": i, "group": grp, "cond": cond, "verdict": v, "want": want, "ok_verdict": ok_v, "ok_fact": ok_f,
                         "ok": ok_v and ok_f, "answer": ans, "raw": raw[:1500], "secs": round(secs, 1),
                         "tokens_in": usage.get("prompt_tokens"), "tokens_out": usage.get("completion_tokens"),
                         "prompt_ms": usage.get("prompt_ms"), "gen_ms": usage.get("gen_ms"),
                         "rose_ms": round(rose_ms, 1) if cond == "B" else 0, "rose": ctx["verdict"]})
            print(f"{i:2} {grp:<10} {cond}  {str(v):<8} want {want:<8} fact {'y' if ok_f else 'n'}  {secs:5.1f}s  "
                  f"{'OK' if ok_v and ok_f else 'FAIL'}  {ans[:80]}", flush=True)
    tag = "rose" if a.rose_only else a.name
    json.dump(rows, open(os.path.join(a.out, f"{tag}.json"), "w"), ensure_ascii=False, indent=1)
    print("\nsummary", tag)
    for cond in sorted({r["cond"] for r in rows}):
        rs = [r for r in rows if r["cond"] == cond]
        secs = sorted(r["secs"] for r in rs)
        tin = [r.get("tokens_in") or 0 for r in rs]
        print(f"  {cond}: {sum(r['ok'] for r in rs)}/{len(rs)} correct "
              f"(verdict {sum(r['ok_verdict'] for r in rs)}, fact {sum(r['ok_fact'] for r in rs)}) | "
              f"time per question: median {secs[len(secs)//2]:.2f} s, total {sum(secs):.0f} s"
              + (f" | tokens in median {sorted(tin)[len(tin)//2]}" if any(tin) else "")
              + (f" | rose lookup median {sorted(r['rose_ms'] for r in rs)[len(rs)//2]:.0f} ms" if cond == "B" else ""))
        for g in dict.fromkeys(r["group"] for r in rs):
            gs = [r for r in rs if r["group"] == g]
            print(f"     {g:<10} {sum(r['ok'] for r in gs)}/{len(gs)}")


if __name__ == "__main__":
    sys.exit(main())
