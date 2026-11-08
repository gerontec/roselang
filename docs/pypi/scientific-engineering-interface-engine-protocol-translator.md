# Scientific/Engineering / Interface Engine/Protocol Translator

[Index](README.md) · 11 packages in this topic, 9 more listed under another topic, by downloads.

### pyusb

Easy USB access for Python

`pip install pyusb` · installs (wheel) · licence: BSD License · rank 2064 · last release 2025-01-08 · [PyPI](https://pypi.org/project/pyusb/) · [source](https://github.com/pyusb/pyusb)

<details><summary>README extract</summary>

PyUSB offers easy USB devices communication in Python.
It should work without additional code in any environment with
Python >= 3.9, ctypes and a pre-built USB backend library
(currently: libusb 1.x, libusb 0.1.x or OpenUSB).

</details>

### PyVISA

Python VISA bindings for GPIB, RS232, TCPIP and USB instruments

`pip install PyVISA` · installs (wheel) · licence: MIT License · rank 4247 · last release 2026-02-27 · [PyPI](https://pypi.org/project/PyVISA/) · [docs](https://pyvisa.readthedocs.io/en/latest/) · [source](https://github.com/pyvisa/pyvisa)

<details><summary>README extract</summary>

A Python package for support of the "Virtual Instrument Software
Architecture" (VISA), in order to control measurement devices and
test equipment via GPIB, RS232, Ethernet or USB.

The programming of measurement instruments can be real pain. There are many
different protocols, sent over many different interfaces and bus systems
(GPIB, RS232, USB). ...

Sections: PyVISA, Description, VISA and Python, Requirements, Documentation, Citing

</details>

### PyVISA-py

Pure Python implementation of a VISA library.

`pip install PyVISA-py` · installs (wheel) · licence: MIT License · rank 4822 · last release 2025-09-04 · [PyPI](https://pypi.org/project/PyVISA-py/) · [docs](https://pyvisa-py.readthedocs.io/en/latest/) · [source](https://github.com/pyvisa/pyvisa-py)

<details><summary>README extract</summary>

A PyVISA backend that implements a large part of the "Virtual Instrument Software
Architecture" (VISA) in pure Python (with the help of some nice cross platform
libraries python packages!).

PyVISA started as wrapper for the IVI-VISA library and therefore you need to install
a VISA library in your system (National Instruments, Keysight, etc). ...

Sections: PyVISA-py, Description, VISA and Python, Requirements, Documentation

</details>

### libretranslatepy

Python bindings for LibreTranslate API

`pip install libretranslatepy` · installs (wheel) · licence: MIT License · rank 6282 · last release 2024-04-16 · [PyPI](https://pypi.org/project/libretranslatepy/) · [source](https://github.com/argosopentech/LibreTranslate-py/)

### can-isotp

Module enabling the IsoTP protocol defined by ISO-15765

`pip install can-isotp` · installs (wheel) · licence: MIT License · rank 8286 · last release 2025-05-14 · [PyPI](https://pypi.org/project/can-isotp/)

<details><summary>README extract</summary>

This project is a Python package meant to provide support for IsoTP (ISO-15765) protocol written in Python 3. The code is published under MIT license on GitHub (pylessard/python-can-isotp).

This package contains a Python implementation of the protocol that works in the user space that may or may not be coupled with python-can. ...

Sections: python-can-isotp, Documentation, Requirements

</details>

### prophy

prophy: fast serialization protocol

`pip install prophy` · installs (wheel) · licence: MIT License · rank 9185 · last release 2022-09-01 · [PyPI](https://pypi.org/project/prophy/)

<details><summary>README extract</summary>

Prophy is a statically typed, binary, tag-free, unpacked serialization protocol.

You can define message schema:
generate codecs for chosen languages:
and serialize data in Python:
in C++:
again in C++ (half hand-rolled, compiler-dependent, but fastest option):
Documentation:

Issues:

Example:
```python
>>> import test
>>> msg = test.MyMsg()
>>> msg.x[:] = [1, 2, 3]
>>> msg.encode('<')
'\x03\x00\x00\x00\x01\x00\x02\x00\x03\x00\x00\x00'
>>> print msg
x: 1
x: 2
x: 3
```

</details>

### udsoncan

Implementation of the Unified Diagnostic Service (UDS) protocol (ISO-14229) used in the automotive industry.

`pip install udsoncan` · installs (wheel) · licence: MIT License · rank 9259 · last release 2026-06-25 · [PyPI](https://pypi.org/project/udsoncan/)

<details><summary>README extract</summary>

This project is an implementation of the Unified Diagnostic Services (UDS) protocol defined by ISO-14229 written in Python 3. The code is published under MIT license on GitHub (pylessard/python-udsoncan).

The documentation is available here :

 - Python 3.7+

Example:
```python
import SomeLib.SomeCar.SomeModel as MyCar

import udsoncan
import isotp
from udsoncan.connections import IsoTPSocketConnection
from udsoncan.client import Client
from udsoncan.exceptions import *
from udsoncan.services import *

udsoncan.setup_logging()

...
```

Sections: python-udsoncan, Documentation, Requirements, Example

</details>

### bytesparse

Library to handle sparse bytes within a virtual memory space

`pip install bytesparse` · installs (wheel) · licence: BSD-2-Clause · rank 9853 · last release 2025-07-04 · [PyPI](https://pypi.org/project/bytesparse/) · [docs](https://bytesparse.readthedocs.io) · [source](https://github.com/TexZK/bytesparse)

<details><summary>README extract</summary>

Features:
Library to handle sparse bytes within a virtual memory space.

* Free software: BSD 2-Clause License

Sections: Overview, Objectives, Python implementation, Cython implementation, Examples, Background, Documentation

</details>

### hexrec

Library to handle hexadecimal record files

`pip install hexrec` · installs (wheel) · licence: BSD-2-Clause · rank 9873 · last release 2025-07-25 · [PyPI](https://pypi.org/project/hexrec/) · [docs](https://hexrec.readthedocs.io/en/latest/) · [source](https://github.com/TexZK/hexrec/)

<details><summary>README extract</summary>

Features:
Library to handle hexadecimal record files

* Free software: BSD 2-Clause License

Example:
```python
from hexrec import convert

convert('data.hex', 'data.srec')
```

Sections: Overview, Introduction, Documentation, Architecture, Examples, Convert format, Merge files, Dataset generator, Write a CRC, Trim for bootloader, Export ELF sections

</details>

### PyVISA-sim

Simulated backend for PyVISA implementing TCPIP, GPIB, RS232, and USB resources

`pip install PyVISA-sim` · installs (wheel) · licence: MIT License · rank 10815 · last release 2025-09-04 · [PyPI](https://pypi.org/project/PyVISA-sim/) · [docs](https://pyvisa-sim.readthedocs.io/en/latest/) · [source](https://github.com/pyvisa/pyvisa-sim)

<details><summary>README extract</summary>

PyVISA-sim is a PyVISA backend that simulates a large part of the
"Virtual Instrument Software Architecture" (VISA).

PyVISA started as a wrapper for the NI-VISA library and therefore you
need to install the National Instruments VISA library in your system.
This works most of the time, for most people. ...

Sections: PyVISA-sim, Description, VISA and Python, Requirements, Documentation

</details>

### python-vxi11

Python VXI-11 driver for controlling instruments over Ethernet

`pip install python-vxi11` · installs from source (sdist only) · licence: MIT License · rank 14636 · last release 2017-01-18 · [PyPI](https://pypi.org/project/python-vxi11/)

<details><summary>README extract</summary>

This Python package supports the VXI-11 Ethernet
instrument control protocol for controlling VXI11 and LXI compatible instruments.

</details>

## Also in this topic

- [jsonconversion](internet-www-http.md#jsonconversion) - This python module helps converting arbitrary Python objects into JSON strings and back.
- [yfinance](office-business-financial.md#yfinance) - Download market data from Yahoo! Finance API
- [crcmod](communications.md#crcmod) - CRC Generator
- [crcmod-plus](communications.md#crcmod-plus) - CRC generator - modernized
- [crate](database.md#crate) - CrateDB Python Client
- [grafana-client](communications.md#grafana-client) - A client library for accessing the Grafana HTTP API, written in Python
- [pycomm3](scientific-engineering-human-machine-interfaces.md#pycomm3) - A Python Ethernet/IP library for communicating with Allen-Bradley PLCs.
- [morph-kgc](database.md#morph-kgc) - Powerful [R2]RML engine to create RDF knowledge graphs from heterogeneous data sources.
- [covalent](adaptive-technologies.md#covalent) - Covalent Workflow Tool
