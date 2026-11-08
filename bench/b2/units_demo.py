"""tests/units_demo.rose written with the Python module (variant B2)."""
import rose
from rose import Q

heat_flow = rose.law("heat_flow", "P = mdot*cp*dT", P="W", mdot="kg/s", cp="J/(kg*K)", dT="K",
                     defaults={"cp": Q(4182, "J/(kg*K)")}, valid={"dT": (Q(0.5, "K"), Q(80, "K"))},
                     intent="thermal power carried by a water flow")


def required_flow(p, spread):
    """mass flow needed to carry power p at temperature spread"""
    return heat_flow.solve("mdot", P=p, dT=spread)


def spread_of(t_flow, t_return):
    """temperature spread between flow and return"""
    return t_flow - t_return


discharge_source = rose.table(
    "discharge_source", {"soc": ("%", 0, 100), "grid_ok": bool},
    [(">= 20 %", True, "battery"), ("< 20 %", True, "grid"),
     (">= 10 %", False, "battery"), ("< 10 %", False, "none")],
    intent="choose energy source by battery SOC and grid state")

assert rose.approx(required_flow(Q(9, "kW"), Q(5, "K")), Q(0.430, "kg/s"), rel=0.01)
assert rose.approx(spread_of(Q(35, "degC"), Q(30, "degC")), Q(5, "K"), abs_=Q(0.001, "K"))
assert discharge_source(soc=Q(15, "%"), grid_ok=False) == "battery"
assert discharge_source(soc=Q(5, "%"), grid_ok=True) == "grid"
print("4/4 tests passed")
