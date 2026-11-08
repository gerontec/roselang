#!/usr/bin/env python3
"""Consistency of the curated problem classes (rose/std/problems.json): facets defined, every ref
exists in the knowledge, every class reachable. Offline:  python3 tests/test_spec.py"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rose import spec  # noqa: E402
from rose.knowledge import Knowledge  # noqa: E402


class ProblemClasses(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = spec.data()
        cls.k = Knowledge()

    def test_facets_defined(self):
        names = set(self.d["facets"])
        for p in self.d["problems"]:
            used = {f for g in p["requires"] for f in g} | set(p.get("optional", [])) | set(p.get("forbids", []))
            self.assertFalse(used - names, f"{p['id']}: undefined facets {used - names}")

    def test_refs_exist(self):
        for p in self.d["problems"]:
            for ref in p.get("see", []) + [s["ref"] for s in p.get("solvers", []) if s.get("ref")]:
                self.assertIsNotNone(self.k.get(ref), f"{p['id']}: unknown ref {ref}")

    def test_cards_indexed(self):
        for p in self.d["problems"]:
            self.assertIsNotNone(self.k.get("problem:" + p["id"]), p["id"])

    def test_unique_ids(self):
        ids = [p["id"] for p in self.d["problems"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_tsp_vs_vrp(self):
        top = spec.match("one van visits all 20 customers and returns to the depot, shortest total distance")[0][0]
        self.assertEqual(top["id"], "travelling_salesperson")
        top = spec.match("four trucks visit all 20 customers from the depot, shortest total distance")[0][0]
        self.assertEqual(top["id"], "vehicle_routing")


if __name__ == "__main__":
    unittest.main(verbosity=1)
