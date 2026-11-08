# Scientific/Engineering / Instrument Drivers

[Index](README.md) · 1 packages in this topic, 1 more listed under another topic, by downloads.

### RsInstrument

VISA or Socket Communication Module for Rohde & Schwarz Instruments

`pip install RsInstrument` · installs (wheel) · licence: MIT · rank 12560 · last release 2026-08-17 · [PyPI](https://pypi.org/project/RsInstrument/) · [docs](https://rsinstrument.readthedocs.io/) · [source](https://github.com/Rohde-Schwarz/RsInstrument)

<details><summary>README extract</summary>

RsInstrument module provides convenient way of communicating with R&S instruments.

Basic Hello-World code:

Check out the full documentation on ReadTheDocs.

Our public Rohde&Schwarz Github repository hosts many examples using this library. ...

Example:
```python
from RsInstrument import *

instr = RsInstrument('TCPIP::192.168.56.101::hislip0', id_query=True, reset=True)
idn = instr.query_str('*IDN?')
print('Hello, I am: ' + idn)
```

</details>

## Also in this topic

- [phidget22](scientific-engineering.md#phidget22) - Phidget22 Python Library
