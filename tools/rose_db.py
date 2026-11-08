"""Shared helpers for the Rose corpus importers (MariaDB, tables rose_*).

Connection: ~/.my.cnf section $ROSE_DB_GROUP (default "rose"), database $ROSE_DB_NAME (default "rose").
"""
import hashlib
import json
import os
import re
import unicodedata

import pymysql

DB_GROUP = os.environ.get("ROSE_DB_GROUP", "rose")   # section in ~/.my.cnf (host, user, password)
DB_NAME = os.environ.get("ROSE_DB_NAME", "rose")
USER_AGENT = "roselang-import/0.1 (https://github.com/gerontec/roselang)"


def connect():
    return pymysql.connect(
        read_default_file=os.path.expanduser("~/.my.cnf"),
        read_default_group=DB_GROUP,
        database=DB_NAME,
        charset="utf8mb4",
        autocommit=False,
    )


def slug(text: str, maxlen: int = 80) -> str:
    """ASCII identifier: 'Ohm's law' -> 'ohms_law'."""
    t = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode()
    t = re.sub(r"['’`]", "", t.lower())
    t = re.sub(r"[^a-z0-9]+", "_", t).strip("_")
    if not t:
        t = "unnamed"
    if t[0].isdigit():
        t = "n" + t
    return t[:maxlen].rstrip("_")


def sha256(text: str) -> bytes:
    return hashlib.sha256(text.encode("utf-8")).digest()


def ensure_source(cur, name, url, license, share_alike, note=None) -> int:
    cur.execute(
        "INSERT INTO rose_source (name, url, license, share_alike, note) VALUES (%s,%s,%s,%s,%s) "
        "ON DUPLICATE KEY UPDATE url=VALUES(url), license=VALUES(license), "
        "share_alike=VALUES(share_alike), note=VALUES(note), source_id=LAST_INSERT_ID(source_id)",
        (name, url, license, share_alike, note),
    )
    return cur.lastrowid


def mark_imported(cur, source_id):
    cur.execute("UPDATE rose_source SET imported_at=NOW() WHERE source_id=%s", (source_id,))


def unit_by_alias(cur, scheme, value):
    cur.execute(
        "SELECT u.unit_id, u.ref FROM rose_alias a JOIN rose_unit u USING (unit_id) "
        "WHERE a.scheme=%s AND a.value=%s",
        (scheme, value),
    )
    return cur.fetchone()


def free_ref(cur, ref, own_unit_id=None):
    """Return ref, or ref with a numeric suffix if another unit already holds it."""
    cand, n = ref, 2
    while True:
        cur.execute("SELECT unit_id FROM rose_unit WHERE ref=%s", (cand,))
        row = cur.fetchone()
        if row is None or row[0] == own_unit_id:
            return cand
        cand = f"{ref}_{n}"
        n += 1


UNIT_COLS = ("ref", "kind", "name", "intent", "signature", "rose_src", "payload",
             "level", "source_id", "source_url")

UPSERT_SQL = (
    "INSERT INTO rose_unit (" + ",".join(UNIT_COLS) + ") VALUES (" + ",".join(["%s"] * len(UNIT_COLS)) + ") "
    "ON DUPLICATE KEY UPDATE kind=VALUES(kind), name=VALUES(name), intent=VALUES(intent), "
    "signature=COALESCE(VALUES(signature), signature), rose_src=COALESCE(VALUES(rose_src), rose_src), "
    "payload=VALUES(payload), source_id=VALUES(source_id), source_url=VALUES(source_url), "
    # a changed payload invalidates earlier verification
    "level=IF(payload <=> VALUES(payload), level, VALUES(level)), "
    "unit_id=LAST_INSERT_ID(unit_id)"
)


def unit_row(ref, kind, name, intent, source_id, source_url=None, signature=None,
             rose_src=None, payload=None, level="imported"):
    return (ref, kind, name[:255], intent, signature, rose_src,
            json.dumps(payload, ensure_ascii=False, sort_keys=True) if payload is not None else None,
            level, source_id, source_url)


def upsert_unit(cur, **kw) -> int:
    cur.execute(UPSERT_SQL, unit_row(**kw))
    return cur.lastrowid


def upsert_units_many(cur, rows):
    cur.executemany(UPSERT_SQL, rows)


def set_alias(cur, unit_id, scheme, value):
    cur.execute(
        "INSERT INTO rose_alias (scheme, value, unit_id) VALUES (%s,%s,%s) "
        "ON DUPLICATE KEY UPDATE unit_id=VALUES(unit_id)",
        (scheme, str(value)[:255], unit_id),
    )


def replace_law_vars(cur, unit_id, rows):
    """rows: (symbol, quantity, unit, dim, role)"""
    cur.execute("DELETE FROM rose_law_var WHERE unit_id=%s", (unit_id,))
    seen = set()
    for sym, qty, unit, dim, role in rows:
        sym = (sym or "")[:32]
        if not sym or sym in seen:
            continue
        seen.add(sym)
        cur.execute(
            "INSERT INTO rose_law_var (unit_id, symbol, quantity, unit, dim, role) VALUES (%s,%s,%s,%s,%s,%s)",
            (unit_id, sym, (qty or "")[:64] or None, (unit or "")[:32], (dim or "")[:64], role),
        )


def replace_tests(cur, unit_id, tests, origin):
    """tests: list of (input_obj, expected_obj, tolerance)"""
    cur.execute("DELETE FROM rose_test WHERE unit_id=%s AND origin=%s", (unit_id, origin))
    for inp, exp, tol in tests:
        cur.execute(
            "INSERT INTO rose_test (unit_id, input, expected, tolerance, origin) VALUES (%s,%s,%s,%s,%s)",
            (unit_id, json.dumps(inp), json.dumps(exp), tol, origin),
        )
