# Software Development / Embedded Systems

[Index](README.md) · 19 packages in this topic, 29 more listed under another topic, by downloads.

### python-can

Controller Area Network interface module for Python

`pip install python-can` · installs (wheel) · licence: LGPL-3.0-only · rank 2330 · last release 2025-08-12 · [PyPI](https://pypi.org/project/python-can/) · [docs](https://python-can.readthedocs.io) · [source](https://github.com/hardbyte/python-can)

_README extract left out: share-alike licence._

### esptool

A serial utility for flashing, provisioning, and interacting with Espressif SoCs.

`pip install esptool` · installs from source (sdist only) · licence: GPL-2.0-or-later · rank 3055 · last release 2026-10-15 · [PyPI](https://pypi.org/project/esptool/) · [docs](https://docs.espressif.com/projects/esptool/) · [source](https://github.com/espressif/esptool/)

_README extract left out: share-alike licence._

### esp-pylib

Python library for logging, utils and constants for Espressif Systems' Python projects

`pip install esp-pylib` · installs (wheel) · licence: Apache-2.0 · rank 3667 · last release 2026-11-02 · [PyPI](https://pypi.org/project/esp-pylib/) · [source](https://github.com/espressif/esp-pylib)

<details><summary>README extract</summary>

Python library for logging, utils and constants for Espressif Systems' Python projects.

Example:
```python
from esp_pylib.logger import log

log.print('Plain output to stdout')
log.note('Informational note')
log.hint('Actionable hint on how to proceed')
log.warn('Something looks off')  # stderr
log.err('Something failed')  # stderr
log.debug('Only shown in verbose mode')  # stdout, verbose only
```

Sections: esp-pylib, Quick start, Modules, IDE integration (WebSocket), Environment variables, Uncaught exceptions, Progress bars, Collapsible stages, Redirecting informational output, Custom logger, Migration Skill for AI Coding Agents, Common migration pitfalls, Use it from Cursor, Use it from Other AI Coding Agents

</details>

### esp-idf-kconfig

Kconfig tooling for esp-idf

`pip install esp-idf-kconfig` · installs (wheel) · licence: Apache Software License · rank 4731 · last release 2026-10-12 · [PyPI](https://pypi.org/project/esp-idf-kconfig/)

<details><summary>README extract</summary>

The ```esp-idf-kconfig``` package is part of the ESP-IDF SDK for Espressif products and is automatically installed.

It is responsible for enabling project configuration using the ```kconfig``` language, providing IDE support for configuration and configuration documentation generation. ...

Sections: esp-idf-kconfig, Reporting issues

</details>

### esp-idf-size

Firmware size analysis for ESP-IDF

`pip install esp-idf-size` · installs (wheel) · licence: Apache Software License · rank 5099 · last release 2026-10-01 · [PyPI](https://pypi.org/project/esp-idf-size/)

<details><summary>README extract</summary>

In the field of IoT development, memory constraints are a common challenge,
often requiring developers to optimize their application size. Whether it
involves ensuring the firmware fits within available flash memory or analyzing
impact of code changes on the final binary size, effective firmware size
management is essential for resource ...

</details>

### esp-coredump

Generate core dumps on unrecoverable software errors

`pip install esp-coredump` · installs (wheel) · licence: Apache-2.0 · rank 5111 · last release 2026-11-02 · [PyPI](https://pypi.org/project/esp-coredump/)

<details><summary>README extract</summary>

A Python-based utility that helps users to retrieve and analyse core dumps. This tool provides two commands for core dumps analysis:

- `info_corefile` - prints crashed task’s registers, callstack, list of available tasks in the system, memory regions and contents of memory stored in core dump (TCBs and stacks) ...

Example:
```python
from esp_coredump import CoreDump

# Instantiate the coredump object
coredump = CoreDump(chip='esp32', core='./tests/esp32/coredump.b64', print_mem=True, core_format='b64', prog='./test_apps/build/test_core_dump.elf')
coredump.info_corefile()  #  print the info of the test app corefile
...
```

Sections: esp-coredump, Examples, Documentation, Code Style & Static Analysis, Pre-commit checks, Conventional Commits

</details>

### canmatrix

Automotive Communication Matrix

`pip install canmatrix` · installs (wheel) · licence: BSD License · rank 5322 · last release 2026-10-21 · [PyPI](https://pypi.org/project/canmatrix/) · [docs](https://canmatrix.readthedocs.io) · [source](https://github.com/ebroecker/canmatrix)

<details><summary>README extract</summary>

*Canmatrix* implements a "Python Can Matrix Object" which describes the can-communication and the needed objects (Boardunits, Frames, Signals, Values, ...)
*Canmatrix* also includes two Tools (canconvert and cancompare) for converting and comparing CAN databases.

- Multiple formats automotive related communication matrix file parsing. ...

</details>

### esp-idf-nvs-partition-gen

ESP-IDF NVS partition generation tool

`pip install esp-idf-nvs-partition-gen` · installs (wheel) · licence: Apache Software License · rank 6361 · last release 2026-07-21 · [PyPI](https://pypi.org/project/esp-idf-nvs-partition-gen/)

<details><summary>README extract</summary>

The utility `esp-idf-nvs-partition-gen/nvs_partition_gen.py` creates a binary file, compatible with the NVS architecture defined in Non-Volatile Storage Library, based on the key-value pairs provided in a CSV file. ...

Sections: NVS Partition Generator Utility, Introduction, Documentation

</details>

### esp-idf-monitor

Serial monitor for esp-idf

`pip install esp-idf-monitor` · installs (wheel) · licence: Apache-2.0 · rank 6431 · last release 2026-09-03 · [PyPI](https://pypi.org/project/esp-idf-monitor/)

<details><summary>README extract</summary>

The `esp-idf-monitor` is a Python-based, open-source package that is part of the ESP-IDF SDK or can be used as a standalond tool for monitoring of Espressif microcontrollers.

The main responsibility of the IDF Monitor is serial communication input and output in ESP-IDF projects. ...

Sections: Espressif IDF Monitor, Documentation, Usage, Non-Interactive (Scripting) Mode, Commands, Examples, Configuration File, File Location, Configuration Options, Custom Reset Sequences, Share Configuration Across Tools, Syntax, Embedded Command Execution, How It Works

</details>

### esp-idf-panic-decoder

ESP-IDF panic decoder

`pip install esp-idf-panic-decoder` · installs (wheel) · licence: Apache Software License · rank 6437 · last release 2026-04-13 · [PyPI](https://pypi.org/project/esp-idf-panic-decoder/)

<details><summary>README extract</summary>

The ```esp-idf-panic-decoder``` is a Python-based, open-source package that is part of the ESP-IDF SDK for Espressif products.

The main part is a script that parses ESP-IDF panic handler output (registers & stack dump), and then acts as a GDB server over stdin/stdout, presenting the information from the panic handler to GDB. ...

Sections: ESP IDF panic decoder, Code Style & Static Analysis, Pre-commit checks, Conventional Commits

</details>

### lpc-checksum

Python script to calculate LPC firmware checksums

`pip install lpc-checksum` · installs (wheel) · licence: MIT License · rank 6706 · last release 2022-11-13 · [PyPI](https://pypi.org/project/lpc-checksum/) · [source](https://github.com/basilfx/lpc_checksum)

<details><summary>README extract</summary>

Python script to calculate LPC firmware checksums, based on the C version by
Roel Verdult. It can be used as a standalone application, or as a Python module
that integrates directly in a build environment (e.g. SCons). It does not need
to be compiled.

The only requirement is Python 3.9 or newer.

Example:
```python
import lpc_checksum

checksum = lpc_checksum.checksum(input_file, [read_only=True])
```

Sections: lpc_checksum, Requirements, Usage, Standalone, As a module, Tests

</details>

### esp-idf-diag

Diagnostic tool for ESP-IDF

`pip install esp-idf-diag` · installs (wheel) · licence: Apache Software License · rank 6822 · last release 2025-06-13 · [PyPI](https://pypi.org/project/esp-idf-diag/)

<details><summary>README extract</summary>

The esp-idf-diag tool gathers information about the ESP-IDF environment, the
system information, and the ESP-IDF project into a report directory to help
with troubleshooting problems.

Sections: ESP-IDF Diag Tool (esp-idf-diag), Creating report directory, Creating a zipped archive of the report directory, Recipes, Redacting sensitive data

</details>

### adafruit-circuitpython-requests

A requests-like library for web interfacing

`pip install adafruit-circuitpython-requests` · installs (wheel) · licence: MIT · rank 10874 · last release 2026-10-30 · [PyPI](https://pypi.org/project/adafruit-circuitpython-requests/)

<details><summary>README extract</summary>

A requests-like library for HTTP commands.

This driver depends on:

* Adafruit CircuitPython
* Adafruit CircuitPython ConnectionManager

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
the Adafruit library and driver bundle.

Sections: Introduction, Dependencies, Usage Example, Documentation

</details>

### adafruit-circuitpython-typing

Types needed for type annotation that are not in `typing`

`pip install adafruit-circuitpython-typing` · installs (wheel) · licence: MIT · rank 10887 · last release 2026-10-20 · [PyPI](https://pypi.org/project/adafruit-circuitpython-typing/)

<details><summary>README extract</summary>

Definitions not in the standard `typing` module that are
needed for type annotation of CircuitPython code.

This library is not needed at runtime for CircuitPython code, and does not need to be in the bundle.

Sections: Introduction, Dependencies, Documentation

</details>

### uModbus

Implementation of the Modbus protocol in pure Python.

`pip install uModbus` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 10898 · last release 2020-08-27 · [PyPI](https://pypi.org/project/uModbus/)

<details><summary>README extract</summary>

uModbus or (μModbus) is a pure Python implementation of the Modbus protocol as
described in the MODBUS Application Protocol Specification V1.1b3. uModbus
implements both a Modbus client (both TCP and RTU) and a Modbus server (both
TCP and RTU). The "u" or "μ" in the name comes from the the SI prefix "micro-".
uModbus is very small and lightweight. ...

Features:
The following functions have been implemented for Modbus TCP and Modbus RTU:

* 01: Read Coils
* 02: Read Discrete Inputs
* 03: Read Holding Registers
* 04: Read Input Registers
* 05: Write Single Coil
* 06: Write Single Register
* 15: Write ...

Example:
```python
# !/usr/bin/env python
# scripts/examples/simple_tcp_server.py
import logging
from socketserver import TCPServer
from collections import defaultdict

...

</details>

### adafruit-circuitpython-busdevice

CircuitPython bus device classes to manage bus sharing.

`pip install adafruit-circuitpython-busdevice` · installs (wheel) · licence: MIT · rank 10905 · last release 2026-04-23 · [PyPI](https://pypi.org/project/adafruit-circuitpython-busdevice/)

<details><summary>README extract</summary>

The `I2CDevice` and `SPIDevice` helper classes make managing transaction state
on a bus easy. For example, they manage locking the bus to prevent other
concurrent access. For SPI devices, it manages the chip select and protocol
changes such as mode. For I2C, it manages the device address. ...

Sections: Adafruit CircuitPython BusDevice, Usage Example, Documentation

</details>

### inputs

Cross-platform Python support for keyboards, mice and gamepads.

`pip install inputs` · installs (wheel) · licence: BSD License · rank 10913 · last release 2018-10-05 · [PyPI](https://pypi.org/project/inputs/)

<details><summary>README extract</summary>

.. image::

Inputs aims to provide cross-platform Python support for keyboards, mice and gamepads.

Example:
```python
from inputs import devices
```

Sections: Inputs, About

</details>

### adafruit-circuitpython-connectionmanager

A urllib3.poolmanager/urllib3.connectionpool-like library for managing sockets and connections

`pip install adafruit-circuitpython-connectionmanager` · installs (wheel) · licence: MIT · rank 11115 · last release 2026-04-23 · [PyPI](https://pypi.org/project/adafruit-circuitpython-connectionmanager/)

<details><summary>README extract</summary>

A urllib3.poolmanager/urllib3.connectionpool-like library for managing sockets and connections

This driver depends on:

* Adafruit CircuitPython

Please ensure all dependencies are available on the CircuitPython filesystem. ...

Sections: Introduction, Dependencies, Usage Example, Documentation

</details>

### mpremote

Tool for interacting remotely with MicroPython devices

`pip install mpremote` · installs (wheel) · licence: MIT License · rank 13850 · last release 2026-08-24 · [PyPI](https://pypi.org/project/mpremote/)

<details><summary>README extract</summary>

This CLI tool provides an integrated set of utilities to remotely interact with
and automate a MicroPython device over a serial connection.

The simplest way to use this tool is:

 mpremote

This will automatically connect to a USB serial port and provide an interactive REPL.

The full list of supported commands are: ...

</details>

## Also in this topic

- [pyquaternion](scientific-engineering-mathematics.md#pyquaternion) - A fully featured, pythonic library for representing and using quaternions.
- [crccheck](scientific-engineering.md#crccheck) - Calculation library for CRCs and checksums
- [pwntools](security.md#pwntools) - Pwntools CTF framework and exploit development library.
- [pyocd](software-development.md#pyocd) - Cortex-M debugger for Python
- [cmsis-pack-manager](software-development.md#cmsis-pack-manager) - Python manager for CMSIS-Pack index and cache with fast Rust backend
- [btsocket](education.md#btsocket) - Python library for BlueZ Bluetooth Management API
- [dbus-next](desktop-environment-gnome.md#dbus-next) - A zero-dependency DBus library for Python with asyncio support
- [littlefs-python](scientific-engineering.md#littlefs-python) - A python wrapper for littlefs
- [phidget22](scientific-engineering.md#phidget22) - Phidget22 Python Library
- [fatfs-ng](scientific-engineering.md#fatfs-ng) - Enhanced Python wrapper around ChaN's FatFS library - Fork of fatfs-python with extended features.
- [pylibftdi](scientific-engineering.md#pylibftdi) - Pythonic interface to FTDI devices using libftdi.
- [spsdk](scientific-engineering.md#spsdk) - Open Source Secure Provisioning SDK for NXP MCU/MPU
- [libusbsio](scientific-engineering.md#libusbsio) - Python wrapper around NXP LIBUSBSIO library
- [speedict](database.md#speedict) - Speedb Python Binding
- [prophy](scientific-engineering-interface-engine-protocol-translator.md#prophy) - prophy: fast serialization protocol
- [bytesparse](scientific-engineering-interface-engine-protocol-translator.md#bytesparse) - Library to handle sparse bytes within a virtual memory space
- [hexrec](scientific-engineering-interface-engine-protocol-translator.md#hexrec) - Library to handle hexadecimal record files
- [niche-elf](software-development-debuggers.md#niche-elf) - A small library that optimizes some niche operations commonly used by debugger extensions.
- [labjack-ljm](software-development.md#labjack-ljm) - LJM library Python wrapper for LabJack T4, T7 and T8.
- [fdt](scientific-engineering-2.md#fdt) - Flattened Device Tree Python Module
- [pyjoulescope-driver](scientific-engineering-2.md#pyjoulescope-driver) - Joulescope™ driver
- [tapo](home-automation.md#tapo) - Unofficial Tapo API Client. Works with TP-Link Tapo smart devices. Tested with light bulbs (L430C, L430P, L510, L520, L530, L535, L610, L630), light strips (L900, L920, L930), plugs (P100, P105, P110, P110M, P115, P125, P125M, TP10), power strips (P300, P304M, P306, P316M), hubs (H100, H110, H200, H500), switches (S200B, S200D, S210), sensors (KE100, T100, T110, T300, T310, T315) and cameras (C120, C210, C220, C225, C325WB, C520WS, TC40, TC70).
- [qctrl-client](internet-www-http-2.md#qctrl-client) - Q-CTRL Client
- [pypemicro](scientific-engineering-2.md#pypemicro) - Python tool to control PEMicro Debug probes
- [pyocd-pemicro](scientific-engineering-2.md#pyocd-pemicro) - PyOCD debug probe plugin for PEMicro debug probes
- [pydsdl](scientific-engineering-2.md#pydsdl) - Cyphal DSDL processing frontend
- [nunavut](scientific-engineering-2.md#nunavut) - Generate code from DSDL using Jinja2 templates.
- [saleae](scientific-engineering-2.md#saleae) - Library to control a Saleae
- [membrowse](software-development-build-tools.md#membrowse) - Memory footprint analysis tools for embedded firmware
