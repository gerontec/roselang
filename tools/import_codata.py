#!/usr/bin/env python3
"""Import the CODATA fundamental physical constants (NIST allascii.txt) into the rose_* tables.

Each constant becomes kind=const, ref const:codata.<slug>, with Rose source
    const <slug>: Real[<unit>] = <value> <unit>
and a test row holding value and standard uncertainty. NIST data: public domain.
"""
import re
import sys

import requests

import rose_db as R

URL = "https://physics.nist.gov/cuu/Constants/Table/allascii.txt"


def num(s: str):
    s = s.replace(" ", "").replace("...", "")
    return float(s) if s else None


def rose_unit(u: str) -> str:
    """'m s^-1' -> 'm*s^-1', '' -> '1'."""
    u = u.strip()
    return "*".join(u.split()) if u else "1"


def main():
    text = requests.get(URL, headers={"User-Agent": R.USER_AGENT}, timeout=60).text
    lines = text.splitlines()
    head = next(i for i, l in enumerate(lines) if l.lstrip().startswith("Quantity"))
    year = re.search(r"(\d{4}) CODATA", text)
    year = year.group(1) if year else "?"
    con = R.connect()
    cur = con.cursor()
    sid = R.ensure_source(cur, "codata", URL, "LicenseRef-NIST-public-domain", False,
                          f"CODATA {year} recommended values of the fundamental physical constants")
    n = 0
    for l in lines[head + 2:]:
        # columns are separated by two or more blanks; digit groups inside a value by one
        parts = re.split(r"\s{2,}", l.strip())
        if len(parts) < 3:
            continue
        name, val_s, unc_s = parts[0], parts[1], parts[2]
        unit = parts[3] if len(parts) > 3 else ""
        value = num(val_s)
        if not name or value is None:
            continue
        exact = unc_s == "(exact)"
        unc = 0.0 if exact else num(unc_s)
        s = R.slug(name, 70)
        ru = rose_unit(unit)
        unit_txt = f" {ru}" if ru != "1" else ""
        src = f"const {s}: Real[{ru}] = {value!r}{unit_txt}  # CODATA {year}{', exact' if exact else ''}"
        payload = {"value": value, "value_text": val_s, "uncertainty": unc, "exact": exact,
                   "unit": unit, "codata": year}
        uid = R.upsert_unit(cur, ref=f"const:codata.{s}", kind="const", name=name,
                            intent=f"{name} (CODATA {year} fundamental physical constant, unit {unit or 'dimensionless'})",
                            signature=f"Real[{ru}]", rose_src=src, payload=payload, source_id=sid,
                            source_url="https://physics.nist.gov/cuu/Constants/", level="tested")
        R.set_alias(cur, uid, "codata", name)
        R.replace_tests(cur, uid, [({}, {"value": value, "uncertainty": unc, "unit": unit}, None)], "source")
        n += 1
    R.mark_imported(cur, sid)
    con.commit()
    print(f"CODATA {year}: {n} constants")


if __name__ == "__main__":
    sys.exit(main())
