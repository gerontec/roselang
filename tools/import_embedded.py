#!/usr/bin/env python3
"""Pointer cards to public embedded-firmware building blocks (kind lib): what solves a microcontroller
task and where it is documented. Rose points only - no firmware is generated or shipped.

Each card names its project's licence (payload.license) and a `call` - how to get to the solution.
Usage: import_embedded.py   (needs the rose_unit DB, see local.env)
"""
import sys

import rose_db as R

# ref, name, intent, docs, call, licence of the project, rank of its PyPI package (ranking prior)
CARDS = [
    ("esphome:modbus_controller", "ESPHome modbus_controller (Modbus RTU master on ESP32/ESP8266)",
     "ESP32 or ESP8266 firmware written as YAML configuration: Modbus RTU master over RS485 on a UART. "
     "Several slave devices share one bus (multiplexing one UART by slave address): one `modbus` hub per "
     "UART with `flow_control_pin` for the RS485 DE/RE direction pin (half duplex, MAX485-style "
     "transceiver), one `modbus_controller` per slave `address`, polled in turn with `update_interval` "
     "and `max_cmd_retries`; a slave that does not answer does not stop the others. Sensors, binary "
     "sensors, switches and numbers map to holding registers, input registers and coils. Use instead of "
     "hand-written RS485 multiplexing, CRC16 and retry code on the microcontroller.",
     "https://esphome.io/components/modbus_controller/",
     "pip install esphome; YAML: uart + modbus (flow_control_pin) + one modbus_controller per address; "
     "esphome run <config>.yaml",
     "MIT AND GPL-3.0-only (C++ runtime)", 8018),
]


def main():
    con = R.connect()
    cur = con.cursor()
    sid = R.ensure_source(cur, "esphome", "https://github.com/esphome/esphome",
                          "MIT AND GPL-3.0-only", False,
                          "ESPHome: pointer cards written for Rose (own text, no ESPHome code or docs copied); "
                          "the project itself is MIT (Python) and GPL-3.0 (C++ runtime)")
    for ref, name, intent, docs, call, lic, rank in CARDS:
        R.upsert_unit(cur, ref=ref, kind="lib", name=name, intent=intent, signature=None, source_id=sid,
                      source_url=docs,
                      payload={"domain": "embedded", "status": "solved", "docs": docs, "call": call,
                               "license": lic, "rank": rank})
    R.mark_imported(cur, sid)
    con.commit()
    print(f"embedded cards: {len(CARDS)}")


if __name__ == "__main__":
    sys.exit(main())
