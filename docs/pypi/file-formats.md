# File Formats

[Index](README.md) · 12 packages in this topic, 3 more listed under another topic, by downloads.

### msgpack

MessagePack serializer

`pip install msgpack` · installs (wheel) · licence: Apache-2.0 · rank 145 · last release 2026-10-26 · [PyPI](https://pypi.org/project/msgpack/) · [docs](https://msgpack-python.readthedocs.io/) · [source](https://github.com/msgpack/msgpack-python/)

<details><summary>README extract</summary>

MessagePack is an efficient binary serialization format.
It lets you exchange data among multiple languages like JSON.
But it's faster and smaller.
This package provides CPython bindings for reading and writing MessagePack data.

Example:
```python
>>> import msgpack
>>> msgpack.packb([1, 2, 3])
'\x93\x01\x02\x03'
>>> msgpack.unpackb(_)
[1, 2, 3]
```

Sections: MessagePack for Python, What is this?, Pure Python implementation, Windows, How to use, One-shot pack & unpack, Streaming unpacking, Packing/unpacking of custom data types, Extended types, Advanced unpacking control, Notes, String and binary types in the old MessagePack spec, ext type, Performance tips

</details>

### pyelftools

Library for analyzing ELF files and DWARF debugging information

`pip install pyelftools` · installs (wheel) · licence: Public Domain · rank 1103 · last release 2026-05-29 · [PyPI](https://pypi.org/project/pyelftools/) · [source](https://github.com/eliben/pyelftools.git)

### protobuf-py

Idiomatic Protocol Buffers for Python.

`pip install protobuf-py` · installs (wheel) · licence: Apache-2.0 · rank 1613 · last release 2026-10-22 · [PyPI](https://pypi.org/project/protobuf-py/) · [docs](https://protobufpy.com/) · [source](https://github.com/bufbuild/protobuf-py)

<details><summary>README extract</summary>

`protobuf-py` is an ergonomic and modern Protobuf library for Python.

Well-typed, generated code you can read. High-performance encoder/decoder written in Rust. 100% conformance.

Zero third-party dependencies or tooling required.

Getting started •
Examples •
New to Protobuf?

Protobuf is the easiest way to build APIs. ...

Example:
```python
from gen.user_pb import User

# Messages are plain Python objects: pass fields as keyword args, or set them later.
user = User(id="123", first_name="Alice")
user.last_name = "Smith"

# Serialize to the Protobuf wire format, then parse it back.
data = user.to_binary()
user = User.from_binary(data)

print(user.first_name)  # Alice
...
```

...

</details>

### stringzilla

Search, hash, sort, and process strings faster via SWAR and SIMD

`pip install stringzilla` · installs (wheel) · licence: Apache-2.0 · rank 2879 · last release 2026-10-25 · [PyPI](https://pypi.org/project/stringzilla/)

<details><summary>README extract</summary>

Strings are the first fundamental data type every programming language implements in software rather than hardware — the closest CPUs come to a "find substring" instruction is x86's `PCMPISTRI`, which is too slow and too narrow to build a library on, and nothing ships a "compute string hash" instruction at all. ...

Features:
There are several other excellent libraries with overlapping subsets of operations and somewhat different design philosophies.
LibC obviously provides a good baseline for basic memory operations, but its APIs vary widely in quality, and its Arm ...

Example:
```python
                           Standard                  StringZilla
─────────────────────────────────────────────────────────────────────────────────
Python
...

</details>

### pyjpegls

JPEG-LS for Python via CharLS C++ Library

`pip install pyjpegls` · installs from source (sdist only) · licence: MIT License · rank 4237 · last release 2024-10-28 · [PyPI](https://pypi.org/project/pyjpegls/) · [docs](https://pydicom.github.io/pydicom) · [source](https://github.com/pydicom/pyjpegls)

<details><summary>README extract</summary>

> Note
> This is a fork of the original CharPyLS repository created
> to be able to add fixes and adaptions, as that repo is not maintained anymore. The rest
> of this file is unchanged from the original readme. ...

Sections: pyjpegls, JPEG-LS for Python via CharLS C++ Library, About JPEG-LS, Dependencies

</details>

### symusic

A high performance MIDI file parser with comprehensible interface.

`pip install symusic` · installs (wheel) · licence: MIT License · rank 5670 · last release 2026-04-08 · [PyPI](https://pypi.org/project/symusic/) · [source](https://github.com/Yikai-Liao/symusic.git)

<details><summary>README extract</summary>

ISMIR 2024 LBD Demo Video: YouTube Bilibili

Symusic ("Symbolic Music") is a cross-platform symbolic music toolkit for note-level
MIDI and ABC workflows. The core is written in C++20 and exposed to Python through nanobind, which
keeps common parsing and transformation workloads hundreds of times faster than the pure-Python
stacks many MIR ...

Features:
- Load MIDI and ABC files with `Score("path.mid")` or `Score("path.abc", fmt="abc")`.
- Convert scores between `tick`, `quarter`, and `second` time units.
- Export back to MIDI or ABC with `dump_midi`, `dump_abc`, and `dumps_abc`. ...

Sections: symusic, Documentation, Features, Use pre-built wheels, Build from source, Python compatibility and CI coverage, Benchmark

</details>

### rdata

Read R datasets from Python.

`pip install rdata` · installs (wheel) · licence: MIT · rank 7890 · last release 2026-06-11 · [PyPI](https://pypi.org/project/rdata/) · [docs](https://rdata.readthedocs.io) · [source](https://github.com/vnmabus/rdata)

<details><summary>README extract</summary>

A Python library for R datasets.

The package rdata offers a lightweight way in Python to import and export R datasets/objects stored
in the ".rda" and ".rds" formats.
Its main advantages are:

- It is a pure Python implementation, with no dependencies on the R language or
 related libraries. ...

Example:
```python
import rdata

converted = rdata.read_rds(rdata.TESTDATA_PATH / "test_dataframe.rds")
print(converted)
```

Sections: rdata, Documentation, Examples, Citing rdata, Usage, Read an R dataset, . First, the file is parsed using the function, Write an R dataset, Additional examples

</details>

### protoc-gen-py

(no summary)

`pip install protoc-gen-py` · installs (wheel) · licence: Apache-2.0 · rank 7961 · last release 2026-10-22 · [PyPI](https://pypi.org/project/protoc-gen-py/) · [docs](https://protobufpy.com/) · [source](https://github.com/bufbuild/protobuf-py)

<details><summary>README extract</summary>

Sections: Generating code, With buf, Plugin options, `init_files`

</details>

### cwl-utils

(no summary)

`pip install cwl-utils` · installs (wheel) · licence: Apache Software License · rank 9237 · last release 2026-11-06 · [PyPI](https://pypi.org/project/cwl-utils/) · [docs](https://cwl-utils.readthedocs.io/) · [source](https://github.com/common-workflow-language/cwl-utils)

<details><summary>README extract</summary>

Python Utilities and Autogenerated Classes for loading and parsing CWL
v1.0,
CWL
v1.1,
and CWL
v1.2
documents.

Requires Python 3.8+

Example:
```python
from pathlib import Path
from ruamel import yaml
import sys

from cwl_utils.parser import load_document_by_uri, save

# File Input - This is the only thing you will need to adjust or take in as an input to your function:
cwl_file = Path("testdata/md5sum.cwl")  # or a plain string works as well

# Import CWL Object
...
```

...

</details>

### cwl-upgrader

Upgrade a CWL tool or workflow document from one version to another

`pip install cwl-upgrader` · installs (wheel) · licence: Apache Software License · rank 9517 · last release 2026-03-31 · [PyPI](https://pypi.org/project/cwl-upgrader/) · [source](https://github.com/common-workflow-language/cwl-upgrader)

<details><summary>README extract</summary>

This is a standalone upgrader for Common Workflow Language documents from
version `draft-3`, `v1.0`, and `v1.1` to `v1.2`.

See for upgrading from `sbg:draft-2`.

It does not check for correctness of the input document, for that one can use
the CWL reference implementation (`cwltool --validate`).

This is written and tested for 3.10 through 3.14.

Sections: Common workflow language standalone document upgrader, Run on the command line

</details>

### PyPDFForm

The Python library & CLI for PDF forms.

`pip install PyPDFForm` · installs (wheel) · licence: MIT · rank 10541 · last release 2026-11-08 · [PyPI](https://pypi.org/project/PyPDFForm/) · [docs](https://chinapandaman.github.io/PyPDFForm/)

<details><summary>README extract</summary>

PDF Form Automation Simplified - Create, Inspect, Style, and Fill Forms in Python or from the Command Line.

PyPDFForm is a Python library and command line tool for working with PDF forms. It provides Python APIs and CLI commands for creating, inspecting, updating, and filling forms, plus common PDF utilities.

With PyPDFForm, you can: ...

Example:
```python
from PyPDFForm import PdfWrapper

filled = PdfWrapper("sample_template.pdf", need_appearances=True).fill(
    {
        "test": "test_1",
        "check": True,
        "test_2": "test_2",
        "check_2": False,
        "test_3": "test_3",
        "check_3": True,
    },
)

filled.write("output.pdf")
```

Sections: Introduction, Quick Example, Documentation, Other Resources

</details>

### tsv2py

High-performance parser and generator for PostgreSQL-compatible tab-separated values (TSV)

`pip install tsv2py` · installs (wheel) · licence: MIT · rank 13051 · last release 2026-06-26 · [PyPI](https://pypi.org/project/tsv2py/)

<details><summary>README extract</summary>

Tab-separated values (TSV) is a simple and popular format for data storage, data transfer, exporting data from and importing data to relational databases. For example, PostgreSQL COPY moves data between PostgreSQL tables and standard file-system files or in-memory stores, and its `text` format (a text file with one line per table row) is a generic ...

Example:
```python
from tsv.helper import Parser

# specify the column structure
parser = Parser(fields=(bytes, date, datetime, float, int, str, UUID, bool))

# read and parse an entire file
with open(tsv_path, "rb") as f:
    py_records = parser.parse_file(f)

# read and parse a file line by line
with open(tsv_path, "rb") as f:
    for line in f:
...
```

...

</details>

## Also in this topic

- [python-oxmsg](communications-email.md#python-oxmsg) - Extract attachments from Outlook .msg files.
- [borb](artistic-software.md#borb) - borb is a library for reading, creating and manipulating PDF files in python.
- [vortex-data](database.md#vortex-data) - Python bindings for Vortex, an Apache Arrow-compatible toolkit for working with compressed array data.
