"""Quantities in a task text: what is given (numbers with units) and what is wanted (a quantity
word without a number). The basis of the dimension search in `rosec plan`: a law fits a task when
its variables carry exactly the dimensions of the given and the wanted quantities - independent
of the words (and the language) the task uses.

    extract("mass flow of water for 9 kW at 5 K spread")
    -> given [9 kW (power), 5 K (temperature)], wanted [mass flow kg/s]
"""
import re

from . import units as U

NUM = r"(?<![\w.\-])([-+]?\d+(?:[.,]\d+)?(?:[eE][-+]?\d+)?)"
# unit words -> unit symbols (English; German where a task text commonly uses it)
UNIT_WORDS = {
    "degrees celsius": "degC", "degree celsius": "degC", "°c": "degC", "grad celsius": "degC", "grad": "degC",
    "celsius": "degC", "kelvin": "K", "seconds": "s", "second": "s", "sekunden": "s", "minutes": "min",
    "minute": "min", "minuten": "min", "hours": "h", "hour": "h", "stunden": "h", "metres": "m", "meters": "m",
    "metre": "m", "meter": "m", "kilometres": "km", "kilometers": "km", "kilograms": "kg", "kilogram": "kg",
    "grams": "g", "watts": "W", "watt": "W", "kilowatts": "kW", "kilowatt": "kW", "volts": "V", "volt": "V",
    "amperes": "A", "ampere": "A", "amps": "A", "ohms": "Ohm", "ohm": "Ohm", "ω": "Ohm", "joules": "J",
    "joule": "J", "newtons": "N", "newton": "N", "pascals": "Pa", "hertz": "Hz", "litres": "L", "liters": "L",
    "liter": "L", "percent": "%", "prozent": "%", "km/h": "km/h", "metres per second": "m/s",
    "meters per second": "m/s",
}
# quantity words -> unit of the dimension (longest phrase first)
QUANTITY_WORDS = [
    ("mass flow rate", "kg/s"), ("mass flow", "kg/s"), ("massenstrom", "kg/s"), ("volume flow", "m^3/s"),
    ("volumenstrom", "m^3/s"), ("kinetic energy", "J"), ("kinetische energie", "J"), ("potential energy", "J"),
    ("energy", "J"), ("energie", "J"), ("arbeit", "J"), ("work", "J"),
    ("how fast", "m/s"), ("wie schnell", "m/s"), ("how far", "m"), ("wie weit", "m"), ("how heavy", "kg"),
    ("wie schwer", "kg"), ("how long does", "s"), ("wie lange", "s"),
    ("power", "W"), ("leistung", "W"), ("force", "N"), ("kraft", "N"), ("pressure", "Pa"), ("druck", "Pa"),
    ("velocity", "m/s"), ("speed", "m/s"), ("geschwindigkeit", "m/s"), ("acceleration", "m/s^2"),
    ("beschleunigung", "m/s^2"), ("period", "s"), ("periode", "s"), ("schwingungsdauer", "s"), ("duration", "s"),
    ("dauer", "s"), ("frequency", "Hz"), ("frequenz", "Hz"), ("wavelength", "m"), ("wellenlänge", "m"),
    ("length", "m"), ("länge", "m"), ("distance", "m"), ("abstand", "m"), ("height", "m"), ("höhe", "m"),
    ("radius", "m"), ("area", "m^2"), ("fläche", "m^2"), ("volume", "m^3"), ("volumen", "m^3"),
    ("density", "kg/m^3"), ("dichte", "kg/m^3"), ("momentum", "kg*m/s"), ("impuls", "kg*m/s"),
    ("mass", "kg"), ("masse", "kg"), ("temperature", "K"), ("temperatur", "K"), ("voltage", "V"),
    ("spannung", "V"), ("current", "A"), ("strom", "A"), ("resistance", "Ohm"), ("widerstand", "Ohm"),
    ("charge", "C"), ("ladung", "C"), ("capacitance", "F"), ("kapazität", "F"), ("torque", "N*m"),
    ("drehmoment", "N*m"),
]


def _unit_at(text, pos):
    """Longest unit starting at pos: a unit word/phrase or a unit expression like kW, m/s, J/(kg*K)."""
    rest = text[pos:]
    low = rest.lower()
    for w in sorted(UNIT_WORDS, key=len, reverse=True):
        if low.startswith(w) and (len(low) == len(w) or not low[len(w)].isalpha()):
            return UNIT_WORDS[w], len(w)
    m = re.match(r"[A-Za-z%µΩ°][A-Za-z0-9%µΩ°/^*()·_]*", rest)
    if not m:
        return None, 0
    cand = m.group(0)
    while cand:
        c = cand.rstrip(".,;:?!)")
        if c.count("(") < c.count(")"):
            c = c[:-1]
        if len(c) < len(rest) and rest[len(c)].isalpha():     # "2 spike" is not "2 s"
            cand = cand[:-1]
            continue
        try:
            U.parse_unit(c)
            return c, len(c)
        except ValueError:
            cand = cand[:-1]
    return None, 0


def given(text):
    """[(value, unit, Unit, start, end)] for every number followed by a parseable unit."""
    out = []
    for m in re.finditer(NUM, text):
        j = m.end()
        while j < len(text) and text[j] == " ":
            j += 1
        unit, n = _unit_at(text, j)
        if not unit:
            continue
        u = U.parse_unit(unit)
        out.append((float(m.group(1).replace(",", ".")), unit, u, m.start(), j + n))
    return out


def wanted(text, gv=None):
    """[(word, unit, Unit)] quantity words of the task that are not followed by their own value."""
    gv = given(text) if gv is None else gv
    low, taken, out = text.lower(), [], []
    for word, unit in QUANTITY_WORDS:
        for m in re.finditer(r"\b" + re.escape(word) + r"\b", low):
            if any(a <= m.start() < b for a, b in taken):
                continue
            taken.append((m.start(), m.end()))
            u = U.parse_unit(unit)
            # "length 1 m", "of 1000 kg": a value of the same dimension right after the word labels a given
            after = [g for g in gv if 0 <= g[3] - m.end() <= 12 and g[2].dim == u.dim]
            if after:
                continue
            if any(g[2].dim == u.dim for g in gv) and word not in ("temperature", "temperatur"):
                continue
            if all(o[2].dim != u.dim for o in out):
                out.append((word, unit, u))
    return out


def extract(text):
    gv = given(text)
    return {"given": [{"value": v, "unit": un, "dim": u.dim, "si": U.to_si(v, u), "absolute": u.absolute,
                       "text": text[a:b]} for v, un, u, a, b in gv if u.dim != U.NONE],
            "wanted": [{"word": w, "unit": un, "dim": u.dim} for w, un, u in wanted(text, gv)]}
