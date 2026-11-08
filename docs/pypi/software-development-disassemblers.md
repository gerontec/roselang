# Software Development / Disassemblers

[Index](README.md) · 2 packages in this topic, 7 more listed under another topic, by downloads.

### idapro

IDA Library Python module

`pip install idapro` · installs (wheel) · licence: MIT License · rank 11733 · last release 2026-10-22 · [PyPI](https://pypi.org/project/idapro/)

<details><summary>README extract</summary>

The IDA Library Python module enables running IDA Pro as an independent Python package outside the IDA UI environment, allowing for programmatic binary analysis and reverse engineering tasks.

The `idapro` Python module needs to know where IDA Pro is installed. ...

Example:
```python
# !/usr/bin/env python3
"""
IDA Pro Python Library Usage Example
This example demonstrates how to analyze a binary file using IDA Pro Python library.
"""

import argparse
import importlib.metadata

# You need to import first idapro module
import idapro

# After idapro module was loaded, you can simply import IDA Python modules
import ida_entry
...
```

Sections: IDA Library Python Module, Prerequisites, Usage Example, Type Hints, Troubleshooting, Common Issues, API Reference, Advanced Usage

</details>

### json-source-map

Calculate the source map for a JSON document.

`pip install json-source-map` · installs (wheel) · licence: Apache Software License · rank 11972 · last release 2022-12-20 · [PyPI](https://pypi.org/project/json-source-map/) · [docs](https://github.com/open-alchemy/json-source-map/wiki) · [source](https://github.com/open-alchemy/json-source-map)

<details><summary>README extract</summary>

Calculate JSON Pointers to each value within a JSON document along with the
line, column and character position for the start and end of that value. For
more information see: <

For example:

The above prints:

Where:

- each key in the dictionary is a JSON path to an item, ...

Example:
```python
from json_source_map import calculate

print(calculate('{"foo": "bar"}'))
```

</details>

## Also in this topic

- [pyelftools](file-formats.md#pyelftools) - Library for analyzing ELF files and DWARF debugging information
- [pcodedmp](security.md#pcodedmp) - A VBA p-code disassembler
- [pwntools](security.md#pwntools) - Pwntools CTF framework and exploit development library.
- [hachoir](multimedia.md#hachoir) - Package of Hachoir parsers used to open binary files
- [CppHeaderParser](software-development.md#cppheaderparser) - Parse C++ header files and generate a data structure representing the class
- [smda](security.md#smda) - A recursive disassembler optimized for CFG recovery from memory dumps. Based on capstone.
- [python-flirt](security.md#python-flirt) - A Python library for parsing, compiling, and matching Fast Library Identification and Recognition Technology (FLIRT) signatures.
