#!/usr/bin/env python3
"""Coverage check against an independent fixed list: Karp's 21 NP-complete problems (1972).
For every name: does rose.exists() answer 'solved' and point to that problem (top 1 / top 3)?"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import rose  # noqa: E402

KARP = {  # name as in the list -> words the right card must contain
    "satisfiability problem": ["satisfiab"], "0-1 integer programming": ["integer", "programming"],
    "clique problem": ["clique"], "set packing": ["set packing"], "vertex cover problem": ["vertex cover"],
    "set cover problem": ["set cover"], "feedback vertex set": ["feedback vertex"],
    "feedback arc set": ["feedback arc"], "directed Hamiltonian cycle": ["hamiltonian"],
    "Hamiltonian cycle problem": ["hamiltonian"], "3-satisfiability": ["satisfiab", "3-sat", "3sat"],
    "graph coloring": ["colo"], "clique cover": ["clique cover"], "exact cover": ["exact cover"],
    "hitting set": ["hitting set"], "Steiner tree problem": ["steiner tree"],
    "3-dimensional matching": ["3-dimensional matching", "three-dimensional matching", "3dimensional"],
    "knapsack problem": ["knapsack"], "job sequencing": ["sequencing", "scheduling"],
    "partition problem": ["partition"], "maximum cut": ["maximum cut", "max cut", "max-cut"],
}
top1 = top3 = 0
for name, words in KARP.items():
    v = rose.exists(name)
    sols = v["solutions"]
    hit = [any(w in (s["name"] + " " + s["ref"]).lower().replace("_", " ") for w in words) for s in sols]
    t1, t3 = bool(hit[:1] and hit[0]), any(hit[:3])
    top1 += t1
    top3 += t3
    first = sols[0] if sols else {}
    print(f"{'ok ' if t1 else 'top3' if t3 else 'MISS'} {name:<28} {v['verdict']:<8} {first.get('name', '-')[:45]}")
print(f"\nKarp's 21: top-1 {top1}/21, top-3 {top3}/21")
