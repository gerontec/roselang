#!/usr/bin/env python3
"""Test suite of the Python module `rose` (rose/lib.py). Offline, standard library only:
    python3 -m unittest tests.test_lib      or      python3 tests/test_lib.py
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import rose  # noqa: E402
from rose import Q  # noqa: E402


class Code:
    """assertRaises with the Rose diagnostic code."""

    def __init__(self, tc, code, cls=rose.RoseError):
        self.tc, self.code, self.cls = tc, code, cls

    def __enter__(self):
        return self

    def __exit__(self, et, ev, tb):
        self.tc.assertIsNotNone(et, f"expected {self.code}, nothing raised")
        self.tc.assertTrue(issubclass(et, self.cls), f"expected {self.cls.__name__}, got {et.__name__}: {ev}")
        self.tc.assertEqual(ev.code, self.code, str(ev))
        self.exc = ev
        return True


class Quantities(unittest.TestCase):
    def test_si_and_conversion(self):
        self.assertEqual(Q(9, "kW").v, 9000)
        self.assertAlmostEqual(Q(1, "kWh").to("J"), 3.6e6)
        self.assertAlmostEqual(Q(36, "km/h").to("m/s"), 10)
        self.assertAlmostEqual(Q(1, "J/(kg*K)").to("J/(kg*K)"), 1)

    def test_arithmetic_combines_dimensions(self):
        p = Q(2, "kg/s") * Q(4182, "J/(kg*K)") * Q(5, "K")
        self.assertAlmostEqual(p.to("W"), 41820)
        self.assertAlmostEqual((Q(10, "m") / Q(2, "s")).to("m/s"), 5)
        self.assertAlmostEqual((Q(3, "m") ** 2).to("m^2"), 9)
        self.assertAlmostEqual((2 * Q(3, "W")).to("W"), 6)

    def test_comparison(self):
        self.assertTrue(Q(1, "kW") > Q(999, "W"))
        self.assertTrue(Q(1000, "W") == Q(1, "kW"))
        self.assertTrue(rose.approx(Q(0.4304, "kg/s"), Q(0.430, "kg/s"), rel=0.01))
        self.assertFalse(rose.approx(Q(0.45, "kg/s"), Q(0.430, "kg/s"), rel=0.01))

    def test_dimensionless_numbers_mix(self):
        self.assertAlmostEqual(float(Q(50, "%") + 0.5), 1.0)

    def test_E201_unequal_dimensions(self):
        with Code(self, "E201", rose.UnitError):
            Q(1, "W") + Q(1, "kWh")
        with Code(self, "E201"):
            Q(1, "W").to("kg")

    def test_E202_bare_number(self):
        with Code(self, "E202"):
            Q(1, "W") > 9
        with Code(self, "E202"):
            float(Q(1, "W"))

    def test_unknown_unit(self):
        with self.assertRaises(ValueError):
            Q(1, "furlong")


class Temperatures(unittest.TestCase):
    def test_absolute_minus_absolute_is_difference(self):
        d = Q(35, "degC") - Q(30, "degC")
        self.assertFalse(d.absolute)
        self.assertAlmostEqual(d.to("K"), 5)

    def test_absolute_plus_difference_is_absolute(self):
        t = Q(20, "degC") + Q(5, "K")
        self.assertTrue(t.absolute)
        self.assertAlmostEqual(t.to("degC"), 25)
        self.assertAlmostEqual(t.to("K"), 298.15)

    def test_E203(self):
        with Code(self, "E203"):
            Q(1, "degC") + Q(2, "degC")
        with Code(self, "E203"):
            Q(5, "K") - Q(1, "degC")
        with Code(self, "E203"):
            -Q(1, "degC")


class Laws(unittest.TestCase):
    def setUp(self):
        self.flow = rose.law("water_heat_flow", "P = mdot*cp*dT", P="W", mdot="kg/s", cp="J/(kg*K)", dT="K",
                             defaults={"cp": Q(4182, "J/(kg*K)")}, valid={"dT": (Q(0.5, "K"), Q(80, "K"))})

    def test_solve_every_variable(self):
        self.assertTrue(rose.approx(self.flow.solve("mdot", P=Q(9, "kW"), dT=Q(5, "K")), Q(0.4304, "kg/s"), 1e-3))
        self.assertTrue(rose.approx(self.flow.solve("P", mdot=Q(0.5, "kg/s"), dT=Q(5, "K")), Q(10455, "W")))
        self.assertTrue(rose.approx(self.flow.solve("dT", P=Q(9, "kW"), mdot=Q(0.5, "kg/s")), Q(4.3042, "K"), 1e-4))

    def test_default_can_be_overridden(self):
        r = self.flow.solve("P", mdot=Q(1, "kg/s"), dT=Q(1, "K"), cp=Q(1000, "J/(kg*K)"))
        self.assertAlmostEqual(r.to("W"), 1000)

    def test_validity_range(self):
        with Code(self, "E400", rose.ContractError):
            self.flow.solve("mdot", P=Q(9, "kW"), dT=Q(100, "K"))

    def test_E204_inconsistent_law(self):
        with Code(self, "E204", rose.LawError):
            rose.law("wrong", "P = mdot*dT", P="W", mdot="kg/s", dT="K")

    def test_E206_symbol_without_unit(self):
        with Code(self, "E206"):
            rose.law("x", "P = mdot*cp", P="W", mdot="kg/s")

    def test_E207(self):
        with Code(self, "E207"):
            self.flow.solve("nope", P=Q(1, "W"))
        with Code(self, "E207"):
            self.flow.solve("mdot", P=Q(1, "W"))                 # dT missing

    def test_given_with_wrong_unit(self):
        with Code(self, "E201"):
            self.flow.solve("mdot", P=Q(9, "kWh"), dT=Q(5, "K"))
        with Code(self, "E202"):
            self.flow.solve("mdot", P=9000, dT=Q(5, "K"))

    def test_positive_root_is_chosen(self):
        area = rose.law("square", "A = a^2", A="m^2", a="m")
        self.assertAlmostEqual(area.solve("a", A=Q(9, "m^2")).to("m"), 3)

    def test_equation_syntax(self):
        with Code(self, "E101"):
            rose.law("x", "P == mdot", P="W", mdot="W")


class Knowledge(unittest.TestCase):
    def test_use_std_law(self):
        ke = rose.use("law:kinetic_energy")
        self.assertTrue(rose.approx(ke.solve("v", T=Q(200, "kJ"), m=Q(1000, "kg")), Q(20, "m/s")))
        self.assertTrue(rose.approx(ke.solve("T", m=Q(2, "kg"), v=Q(3, "m/s")), Q(9, "J")))

    def test_use_codata_constant(self):
        c = rose.use("const:codata.speed_of_light_in_vacuum")
        self.assertEqual(c.to("m/s"), 299792458)
        self.assertTrue(rose.approx(rose.use("const:codata.electron_mass_in_u"), Q(9.1093837139e-31, "kg"), rel=1e-9))  # unit u

    def test_lock_records_provenance(self):
        rose.use("law:kinetic_energy")
        refs = {e["ref"]: e for e in rose.lock()}
        self.assertIn("law:kinetic_energy", refs)
        self.assertEqual(refs["law:kinetic_energy"]["license"], "CC0-1.0")

    def test_E305_open_problem(self):
        with Code(self, "E305", rose.OpenProblem):
            rose.use("open:goldbachs_conjecture")
        with Code(self, "E305", rose.OpenProblem):
            rose.use("open:riemann_hypothesis")

    def test_E301_unknown_ref_with_suggestion(self):
        with Code(self, "E301", rose.UnknownRef) as c:
            rose.use("law:water_heat_flow")
        self.assertIn("did you mean", str(c.exc))

    def test_E306_card_without_source(self):
        with Code(self, "E306", rose.UnknownRef):
            rose.use("bio:go.0035825")                            # homologous recombination: a card, no code

    def test_get_card(self):
        card = rose.get("bio:go.0035825")
        self.assertEqual(card["name"], "homologous recombination")
        self.assertEqual(card["license"], "CC-BY-4.0")

    def test_search(self):
        refs = [h["ref"] for h in rose.search("speed of light in vacuum", k=3)]
        self.assertIn("const:codata.speed_of_light_in_vacuum", refs)

    def test_plan_negative_knowledge(self):
        r = rose.plan("prove that every even integer greater than 2 is the sum of two primes")
        self.assertTrue(any("Goldbach" in w for w in r["warnings"]))

    def test_plan_category(self):
        self.assertEqual(rose.plan("speed of light in vacuum in metres per second")["category"], "physics/constant")


def _has_rosetta():
    from rose.knowledge import pack_dirs
    return any(os.path.basename(d) == "rose_rosetta" for d in pack_dirs())


@unittest.skipUnless(_has_rosetta(), "Rosetta Code pack not installed (pip install roselang-rosetta)")
class RosettaPack(unittest.TestCase):
    def test_task_with_python3_solution(self):
        import warnings
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            t = rose.use("rc:100_doors")
        self.assertTrue(any("R205" in str(x.message) for x in w))
        self.assertIn("100 doors", t.description)
        compile(t.code, "<rc>", "exec")
        self.assertTrue(rose.lock()[-1]["share_alike"])

    def test_search_finds_task(self):
        self.assertEqual(rose.search("100 doors toggle", k=1)[0]["ref"], "rc:100_doors")


class Exists(unittest.TestCase):
    def test_solved_points_to_solution(self):
        v = rose.exists("plan a tour for a delivery van that visits 30 customers and returns to the depot "
                        "with the shortest total distance")
        self.assertEqual(v["verdict"], "solved")
        self.assertEqual(v["solutions"][0]["ref"], "problem:travelling_salesperson")
        self.assertTrue(v["solutions"][0]["url"])

    def test_open_problem(self):
        v = rose.exists("prove that every even integer greater than 2 is the sum of two primes")
        self.assertEqual(v["verdict"], "open")
        self.assertIn("Goldbach", v["answer"])

    def test_unknown(self):
        self.assertEqual(rose.exists("qwxz frobnicate the blorf")["verdict"], "unknown")


class Tables(unittest.TestCase):
    INPUTS = {"soc": ("%", 0, 100), "grid_ok": bool}
    RULES = [(">= 20 %", True, "battery"), ("< 20 %", True, "grid"),
             (">= 10 %", False, "battery"), ("< 10 %", False, "none")]

    def test_decide(self):
        t = rose.table("src", self.INPUTS, self.RULES)
        self.assertEqual(t(soc=Q(15, "%"), grid_ok=False), "battery")
        self.assertEqual(t(soc=Q(5, "%"), grid_ok=True), "grid")
        self.assertEqual(t(soc=Q(5, "%"), grid_ok=False), "none")
        self.assertEqual(t(soc=Q(100, "%"), grid_ok=True), "battery")

    def test_E511_incomplete(self):
        with Code(self, "E511", rose.TableError):
            rose.table("src", self.INPUTS, self.RULES[:3])

    def test_E512_overlap(self):
        with Code(self, "E512", rose.TableError):
            rose.table("src", {"soc": ("%", 0, 100)}, [(">= 10 %", "battery"), ("< 20 %", "grid")])

    def test_hit_first_allows_overlap(self):
        t = rose.table("src", {"soc": ("%", 0, 100)}, [(">= 10 %", "battery"), ("< 20 %", "grid")], hit="first")
        self.assertEqual(t(soc=Q(15, "%")), "battery")

    def test_enum_and_wildcard(self):
        t = rose.table("mode", {"mode": ["eco", "boost"], "t": ("degC", -20, 60)},
                       [("eco", "-", "low"), ("boost", ">= 40 degC", "off"), ("boost", "< 40 degC", "high")])
        self.assertEqual(t(mode="boost", t=Q(30, "degC")), "high")
        self.assertEqual(t(mode="eco", t=Q(50, "degC")), "low")

    def test_cell_unit_mismatch(self):
        with Code(self, "E201"):
            rose.table("x", {"soc": ("%", 0, 100)}, [(">= 20 kW", "a"), ("< 20 kW", "b")])

    def test_cell_syntax_and_arity(self):
        with Code(self, "E101"):
            rose.table("x", {"soc": ("%", 0, 100)}, [("about 20", "a")])
        with Code(self, "E101"):
            rose.table("x", {"soc": ("%", 0, 100)}, [(">= 20 %", True, "a")])


if __name__ == "__main__":
    unittest.main(verbosity=1)
