# Unclassified / X

[Index](README.md) · 38 packages in this topic, by downloads.

### xxhash

Python binding for xxHash

`pip install xxhash` · installs (wheel) · licence: BSD-2-Clause · rank 204 · last release 2026-10-19 · [PyPI](https://pypi.org/project/xxhash/)

<details><summary>README extract</summary>

xxhash is a Python binding for the xxHash library by Yann Collet.

__ Cyan4973

Example:
```python
>>> import xxhash
>>> xxhash.VERSION
'4.0.2'
>>> xxhash.XXHASH_VERSION
'0.8.3'
```

Sections: python-xxhash, Prerequisites, Linking to libxxhash.so, Usage, Thread safety, Caveats, SEED OVERFLOW, ENDIANNESS, DONT USE XXHASH IN HMAC, v4.0.2 2026-10-19, v4.0.1 2026-08-17, v4.0.0 2026-08-12, v3.8.2 2026-10-18, v3.8.1 2026-07-06

</details>

### xlsxwriter

A Python module for creating Excel XLSX files.

`pip install xlsxwriter` · installs (wheel) · licence: BSD-2-Clause · rank 206 · last release 2026-10-28 · [PyPI](https://pypi.org/project/xlsxwriter/) · [docs](https://xlsxwriter.readthedocs.io) · [source](https://github.com/jmcnamara/XlsxWriter)

<details><summary>README extract</summary>

XlsxWriter is a Python module for writing files in the Excel 2007+ XLSX
file format.

XlsxWriter can be used to write text, numbers, formulas and hyperlinks to
multiple worksheets and it supports features such as formatting and many more,
including:

* 100% compatible Excel XLSX files.
* Full formatting.
* Merged cells.
* Defined names.
* Charts. ...

Example:
```python
import xlsxwriter

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook("demo.xlsx")
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column("A:A", 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({"bold": True})

# Write some simple text.
...
```

</details>

### xgboost

XGBoost Python Package

`pip install xgboost` · installs (wheel) · licence: Apache-2.0 · rank 629 · last release 2026-08-15 · [PyPI](https://pypi.org/project/xgboost/) · [docs](https://xgboost.readthedocs.io/en/stable/) · [source](https://github.com/dmlc/xgboost)

### xyzservices

Source of XYZ tiles providers

`pip install xyzservices` · installs (wheel) · licence: BSD-3-Clause · rank 1419 · last release 2026-09-04 · [PyPI](https://pypi.org/project/xyzservices/) · [source](https://github.com/geopandas/xyzservices)

<details><summary>README extract</summary>

`xyzservices` is a lightweight library providing a repository of available XYZ services
offering raster basemap tiles. The repository is provided via Python API and as a
compressed JSON file.

XYZ tiles can be used as background for your maps to provide necessary spatial context. ...

Example:
```python
>>> import xyzservices.providers as xyz
```

Sections: xyzservices - Source of XYZ tiles providers, Quick Start, Providers API, Providers JSON

</details>

### xgrammar

Efficient, Flexible and Portable Structured Generation

`pip install xgrammar` · installs (wheel) · licence: Apache Software License · rank 1814 · last release 2026-09-24 · [PyPI](https://pypi.org/project/xgrammar/) · [source](https://github.com/mlc-ai/xgrammar)

<details><summary>README extract</summary>

Efficient, Flexible and Portable Structured Generation

Get Started | Documentation | Blogpost | Technical Report

- [2026/5] XGrammar-2 has been released! Check out our blog for more information.
- [2025/12] XGrammar has been officially integrated into Mirai
- [2025/09] XGrammar has been officially integrated into OpenVINO GenAI ...

Features:
XGrammar is an open-source library for efficient, flexible, and portable structured generation.

It leverages constrained decoding to ensure 100% structural correctness of the output. ...

Example:
```python
import xgrammar as xgr
```

Sections: News, Overview, Get Started, Third-Party Bindings, Collaborators

</details>

### xmod

🌱 Turn any object into a module 🌱

`pip install xmod` · installs (wheel) · licence: MIT · rank 2050 · last release 2026-05-09 · [PyPI](https://pypi.org/project/xmod/) · [docs](https://rec.github.io/xmod) · [source](https://github.com/rec/xmod)

<details><summary>README extract</summary>

Callable modules! Indexable modules!?

Ever wanted to call a module directly, or index it? Or just sick of seeing
`from foo import foo` in your examples?

Give your module the awesome power of an object, or maybe just save a
little typing, with `xmod`. ...

Sections: 🌱 Turn any object into a module 🌱, Example: Make a module callable like a function!, Example: Make a module look like a list!?!, API Documentation

</details>

### xgboost-cpu

XGBoost Python Package

`pip install xgboost-cpu` · installs (wheel) · licence: Apache-2.0 · rank 3100 · last release 2026-08-15 · [PyPI](https://pypi.org/project/xgboost-cpu/) · [docs](https://xgboost.readthedocs.io/en/stable/) · [source](https://github.com/dmlc/xgboost)

<details><summary>README extract</summary>

The `xgboost-cpu` package provides for a minimal installation, with no support for the
GPU algorithms or federated learning. It is provided to allow XGBoost to be installed in a
space-constrained environment.

Note. `xgboost-cpu` package is only provided for x86_64 (amd64) Linux and Windows
platforms. ...

Sections: XGBoost Python Package (CPU only), From PyPI

</details>

### xarray-einstats

Stats, linear algebra and einops for xarray

`pip install xarray-einstats` · installs (wheel) · licence: Apache Software License · rank 3221 · last release 2026-07-20 · [PyPI](https://pypi.org/project/xarray-einstats/) · [docs](https://einstats.python.arviz.org) · [source](https://github.com/arviz-devs/xarray-einstats)

<details><summary>README extract</summary>

Stats, linear algebra and einops for xarray

Features:
As stated in their website:

> xarray makes working with multi-dimensional labeled arrays simple, efficient and fun!

The code is often more verbose, but it is generally because it is clearer and thus less error prone
and more intuitive. ...

Sections: xarray-einstats, Overview, Relevant links, Similar projects

</details>

### xopen

Open compressed files transparently

`pip install xopen` · installs (wheel) · licence: MIT · rank 4758 · last release 2026-06-03 · [PyPI](https://pypi.org/project/xopen/)

<details><summary>README extract</summary>

This Python module provides an `xopen` function that works like Python’s
built-in `open` function but also transparently deals with compressed files.
`xopen` selects the most efficient method for reading or writing a compressed file.

Supported compression formats are:

- gzip (`.gz`)
- bzip2 (`.bz2`)
- xz (`.xz`)
- Zstandard (`.zst`)

Example:
```python
from xopen import xopen

with xopen("file.txt.gz") as f:
    content = f.read()
```

Sections: xopen, Example usage, The `xopen` function, Parameters, Backends, Reproducibility, v2.1.0 (2026-06-03), v2.0.2 (2024-06-12), v2.0.1 (2024-03-28), v2.0.0 (2024-03-26), v1.9.0 (2024-01-31), v1.8.0 (2023-11-03), v1.7.0 (2022-11-03), v1.6.0 (2022-08-10)

</details>

### xatlas

Python bindings for xatlas

`pip install xatlas` · installs from source (sdist only) · licence: not stated · rank 5406 · last release 2025-07-04 · [PyPI](https://pypi.org/project/xatlas/)

<details><summary>README extract</summary>

(Unofficial) Python bindings for xatlas, a library that generates texture coordinates for triangle meshes.

Example:
```python
import trimesh
import xatlas

# We use trimesh ( to load a mesh but you can use any library.
mesh = trimesh.load_mesh("input.obj")

# The parametrization potentially duplicates vertices.
# `vmapping` contains the original vertex index for each new vertex (shape N, type uint32).
...
```

Sections: Python bindings for xatlas, From source, Using Pip, Usage, Parametrize a mesh and export it, Parametrize multiple meshes using one atlas, Repack multiple parametrized meshes into one atlas, Query the atlas, References

</details>

### xls2xlsx

Convert xls file to xlsx

`pip install xls2xlsx` · installs (wheel) · licence: MIT License · rank 5460 · last release 2023-01-06 · [PyPI](https://pypi.org/project/xls2xlsx/)

<details><summary>README extract</summary>

Convert xls file to xlsx

* Free software: MIT license

Features:
* Convert `.xls` files to `.xlsx` using xlrd and openpyxl.
* Convert `.htm` and `.mht` files containing tables or excel contents to `.xlsx` using beautifulsoup4 and openpyxl. ...

Example:
```python
from xls2xlsx import XLS2XLSX
x2x = XLS2XLSX("spreadsheet.xls")
x2x.to_xlsx("spreadsheet.xlsx")
```

Sections: xls2xlsx, Features, Usage, Dependencies, Implementation Notes, 0.2.0 (2023-01-05), 0.1.5 (2020-11-03), 0.1.4 (2020-11-02), 0.1.3 (2020-10-15), 0.1.0 (2020-09-13)

</details>

### xrootd

eXtended ROOT daemon

`pip install xrootd` · installs (wheel) · licence: LGPL-3.0-or-later · rank 5604 · last release 2026-10-29 · [PyPI](https://pypi.org/project/xrootd/)

_README extract left out: share-alike licence._

### xdg

Variables defined by the XDG Base Directory Specification

`pip install xdg` · installs (wheel) · licence: OSI Approved · rank 5901 · last release 2023-02-27 · [PyPI](https://pypi.org/project/xdg/) · [source](https://github.com/srstevenson/xdg-base-dirs)

<details><summary>README extract</summary>

`xdg` has been renamed to `xdg-base-dirs` due to an import collision with
`PyXDG`. Therefore the
`xdg` package is deprecated. Install
`xdg-base-dirs` instead.

</details>

### xdg-base-dirs

Variables defined by the XDG Base Directory Specification

`pip install xdg-base-dirs` · installs (wheel) · licence: ISC · rank 6040 · last release 2026-11-02 · [PyPI](https://pypi.org/project/xdg-base-dirs/) · [source](https://github.com/srstevenson/xdg-base-dirs)

<details><summary>README extract</summary>

xdg-base-dirs is a Python module that provides functions to return paths to the
directories defined by the XDG Base Directory Specification, to save you
from duplicating the same snippet of logic in every Python utility you write
that deals with user cache, configuration, or data files. ...

Example:
```python
from xdg_base_dirs import (
    xdg_cache_home,
    xdg_config_dirs,
    xdg_config_home,
    xdg_data_dirs,
    xdg_data_home,
    xdg_runtime_dir,
    xdg_state_home,
)
```

Sections: xdg-base-dirs, Usage, Copyright

</details>

### xmodem

XMODEM protocol implementation.

`pip install xmodem` · installs (wheel) · licence: MIT · rank 6046 · last release 2026-03-04 · [PyPI](https://pypi.org/project/xmodem/) · [source](https://github.com/tehmaze/xmodem)

<details><summary>README extract</summary>

Example:
```python
>>> import serial
>>> from xmodem import XMODEM
>>> ser = serial.Serial('/dev/ttyUSB0', timeout=0) # or whatever port you need
>>> def getc(size, timeout=1):
...     return ser.read(size) or None
...
>>> def putc(data, timeout=1):
...     return ser.write(data)  # note that this ignores the timeout
...
>>> modem = XMODEM(getc, putc)
```

Sections: Usage, Changes

</details>

### xdk

Python SDK for the X API

`pip install xdk` · installs (wheel) · licence: MIT License · rank 6357 · last release 2026-07-25 · [PyPI](https://pypi.org/project/xdk/) · [source](https://github.com/xdevplatform/xdk-python)

<details><summary>README extract</summary>

<!--
AUTO-GENERATED FILE - DO NOT EDIT
This file was automatically generated by the XDK build tool.

<!--
Auto-generated README for the X API Python SDK.

This file contains the documentation and usage examples
for the generated Python SDK package.

Generated automatically - do not edit manually.

A Python SDK for the X API.

Features:
- Full support for the X API v2
- Simple and intuitive interface
- Comprehensive documentation
- Type hints for better IDE support

Example:
```python
from xdk import Client

# Initialize the client
client = Client(
    api_key="your_api_key",
    api_secret="your_api_secret",
    access_token="your_access_token",
    access_token_secret="your_access_token_secret"
)

# Use the client to interact with the X API
# For example, to get posts:
...

</details>

### xacro

xacro is a macro language for XML

`pip install xacro` · installs (wheel) · licence: not stated · rank 6421 · last release 2025-08-28 · [PyPI](https://pypi.org/project/xacro/) · [docs](https://github.com/ros/xacro/wiki) · [source](https://github.com/ros/xacro)

<details><summary>README extract</summary>

Xacro is an XML macro language

With `xacro`, you can construct shorter and more readable XML files by using macros that expand to larger XML expressions.
Recent documentation can be found in the wiki. For older releases, have a look at the ROS wiki.

</details>

### xero-python

Official Python sdk for Xero API generated by OpenAPI spec for oAuth2

`pip install xero-python` · installs from source (sdist only) · licence: MIT License · rank 6554 · last release 2026-11-05 · [PyPI](https://pypi.org/project/xero-python/)

<details><summary>README extract</summary>

The xero-python SDK makes it easy for developers to access Xero's APIs in their python code, and build robust applications and software using small business & general ledger accounting data. ...

Example:
```python
# -*- coding: utf-8 -*-
import os
from functools import wraps
from io import BytesIO
from logging.config import dictConfig
from flask import Flask, session
from flask_oauthlib.contrib.client import OAuth, OAuth2Application
from flask_session import Session
from xero_python.accounting import AccountingApi
from xero_python.assets import AssetApi
...
```

</details>

### xonsh

Python-powered shell. Full-featured, cross-platform and AI-friendly.

`pip install xonsh` · installs (wheel) · licence: BSD 2-Clause License · rank 6809 · last release 2026-10-22 · [PyPI](https://pypi.org/project/xonsh/) · [docs](https://xon.sh/contents.html) · [source](https://github.com/xonsh/xonsh)

<details><summary>README extract</summary>

.. raw:: html

Xonsh (sounds like "consh") is a full-featured and cross-platform Python-based shell. The language is a superset of Python 3 with seamless integration of shell functionality and commands. It works on all major platforms, including Linux, macOS, Windows, BSD, Jupyter, Android, Raspberry Pi and Nix.

.. raw:: html

.. ...

</details>

### x402

x402 Payment Protocol SDK for Python

`pip install x402` · installs (wheel) · licence: Apache-2.0 · rank 6993 · last release 2026-11-04 · [PyPI](https://pypi.org/project/x402/) · [docs](https://x402.org) · [source](https://github.com/x402-foundation/x402)

<details><summary>README extract</summary>

Core implementation of the x402 payment protocol. Provides transport-agnostic client, server, and facilitator components with both async and sync variants.

Example:
```python
from x402 import x402Client
from x402.mechanisms.evm.exact import ExactEvmScheme

client = x402Client()
client.register("eip155:*", ExactEvmScheme(signer=my_signer))

# Create payment from 402 response
payload = await client.create_payment_payload(payment_required)
```

Sections: x402 Python SDK, Quick Start, Client (Async), Client (Sync), TVM Client (Async), Server (Async), Server (Sync), Facilitator (Async), Facilitator (Sync), Async vs Sync, Framework Pairing, Client Configuration, Spend controls, Policies

</details>

### x25519

A pure Python implemention of curve25519

`pip install x25519` · installs (wheel) · licence: Public Domain · rank 7822 · last release 2021-10-24 · [PyPI](https://pypi.org/project/x25519/)

<details><summary>README extract</summary>

A pure Python implemention of curve25519 like Go package x/crypto/curve25519:

Usage of this package:

Generally, other C implementions are much faster:

Example:
```python
# this code supports both python 2 and 3
from binascii import hexlify
import x25519

private_key = b'1' * 32
public_key = x25519.scalar_base_mult(private_key)
print(hexlify(public_key))

peer_public_key = b'2' * 32
shared_secret = x25519.scalar_mult(private_key, peer_public_key)
print(hexlify(shared_secret))

'''output:
...
```

</details>

### xds-protos

Generated Python code from envoyproxy/data-plane-api

`pip install xds-protos` · installs (wheel) · licence: Apache-2.0 · rank 7950 · last release 2026-10-30 · [PyPI](https://pypi.org/project/xds-protos/)

<details><summary>README extract</summary>

Package "xds-protos" is a collection of ProtoBuf generated Python files for xDS protos (or the data-plane-api). You can find the source code of this project in grpc/grpc. For any question or suggestion, please post to

Each generated Python file can be imported according to their proto package. ...

Example:
```python
# Import the message definitions
from envoy.service.status.v3 import csds_pb2
# Import the gRPC service and stub
from envoy.service.status.v3 import csds_pb2_grpc
```

</details>

### xkcdpass

Generate secure multiword passwords/passphrases, inspired by XKCD

`pip install xkcdpass` · installs (wheel) · licence: BSD-3-Clause · rank 8379 · last release 2026-01-12 · [PyPI](https://pypi.org/project/xkcdpass/) · [source](https://github.com/redacted/XKCD-password-generator.git)

<details><summary>README extract</summary>

A flexible and scriptable password generator which generates strong passphrases, inspired by XKCD 936:

Example:
```python
from xkcdpass import xkcd_password as xp

# create a wordlist from the default wordfile
# use words between 5 and 8 letters long
wordfile = xp.locate_wordfile()
mywords = xp.generate_wordlist(wordfile=wordfile, min_length=5, max_length=8)

# create a password with the acrostic "face"
print(xp.generate_xkcdpassword(mywords, acrostic="face"))
```

Sections: xkcdpass, Source, Requirements, Running `xkcdpass`, Word lists, Additional languages, Using xkcdpass as an imported module, Insecure random number generators

</details>

### xarray-spatial

xarray-based spatial analysis tools

`pip install xarray-spatial` · installs (wheel) · licence: MIT License · rank 8505 · last release 2026-10-27 · [PyPI](https://pypi.org/project/xarray-spatial/)

<details><summary>README extract</summary>

> [!IMPORTANT]
> xarray-spatial uses AI assistance. Before opening a PR, read the AI-Assisted Contribution Policy and run your changes through the project's approved AI review workflow (see the command suite in the xarray-spatial-skills repo). PRs that ignore the workflow are likely to be rejected.
> Feature freeze in effect. ...

Example:
```python
Compression codecs: Deflate, LZW (Numba JIT), ZSTD, PackBits, JPEG (Pillow, internal-only: requires `allow_internal_only_jpeg=True` and is not readable by GDAL), JPEG 2000 (glymur, experimental: requires `allow_experimental_codecs=True`), uncompressed

...
```

...

</details>

### xgboost-ray

A Ray backend for distributed XGBoost

`pip install xgboost-ray` · installs (wheel) · licence: Apache 2.0 · rank 8949 · last release 2023-09-20 · [PyPI](https://pypi.org/project/xgboost-ray/)

<details><summary>README extract</summary>

A distributed backend for XGBoost built on top of distributed computing framework Ray.

</details>

### xberg

High-performance document intelligence library

`pip install xberg` · installs (wheel) · licence: MIT · rank 9299 · last release 2026-10-13 · [PyPI](https://pypi.org/project/xberg/) · [source](https://github.com/xberg-io/xberg)

### xoto3

High level utilities for a subset of boto3 operations common for AWS serverless development in Python.

`pip install xoto3` · installs (wheel) · licence: not stated · rank 9413 · last release 2026-09-04 · [PyPI](https://pypi.org/project/xoto3/)

<details><summary>README extract</summary>

`xoto3` (pronounced zoto-three) is a layer of useful micro-utilities
for `boto3` (the AWS Python library) particularly suitable for
serverless development.

These come from years of experience developing a serverless platform
at XOi Technologies, and represent real production code.

Features:
Some of the features included:

- A more general purpose `boto3` client API paginator.

 - pure data transformation safeguards against various sorts of data
 that DynamoDB won't accept. ...

Sections: xoto3, Features, Other Utilities, Getting set up, Versioning, Writing tests

</details>

### xxtea

xxtea is a simple block cipher

`pip install xxtea` · installs (wheel) · licence: BSD-2-Clause · rank 9430 · last release 2026-10-20 · [PyPI](https://pypi.org/project/xxtea/)

<details><summary>README extract</summary>

XXTEA implemented as a Python extension module, licensed under 2-clause BSD.

The XXTEA algorithm takes a 128-bit key and operates on an array of 32-bit
integers (at least 2 integers), but it doesn't define the conversions between
bytes and array. Due to this reason, many XXTEA implementations out there are
not compatible with each other. ...

Example:
```python
>>> import os
>>> import xxtea
>>> import binascii
>>>
>>> key = os.urandom(16)  # Key must be a 16-byte string.
>>> s = b"xxtea is good"
>>>
>>> enc = xxtea.encrypt(s, key)
>>> dec = xxtea.decrypt(enc, key)
>>> s == dec
True
>>>
>>> hexenc = xxtea.encrypt_hex(s, key)
>>> s == xxtea.decrypt_hex(hexenc, key)
True
>>>
...
```

Sections: xxtea, Usage, XXTEA Type, Padding, Rounds, Catching Exceptions

</details>

### xdsl

xDSL

`pip install xdsl` · installs (wheel) · licence: Apache License v2.0 with LLVM Exceptions · rank 9442 · last release 2026-11-06 · [PyPI](https://pypi.org/project/xdsl/) · [source](https://github.com/xdslproject/xdsl)

<details><summary>README extract</summary>

<!-- markdownlint-disable-next-line MD041 -->

xDSL is a Python-native framework for
building compiler infrastructure. It provides *SSA-based intermediate
representations (IRs)*
and Pythonic APIs to define, assemble, and optimize custom IRs—all with seamless
compatibility with MLIR from the LLVM project. ...

Sections: xDSL: A Python-native SSA Compiler Framework, Subprojects With Extra Dependencies, Getting Started, Discussion

</details>

### xml-python

A library for making Python objects from XML.

`pip install xml-python` · installs (wheel) · licence: MPL · rank 10867 · last release 2021-01-07 · [PyPI](https://pypi.org/project/xml-python/)

### xlocal

execution locals: killing global state (including thread locals)

`pip install xlocal` · installs from source (sdist only) · licence: UNKNOWN · rank 10970 · last release 2012-11-16 · [PyPI](https://pypi.org/project/xlocal/)

<details><summary>README extract</summary>

This module provides execution locals aka "xlocal" objects which implement
a more restricted variant of "thread locals". An execution local allows to
manage attributes on a per-execution basis in a manner similar to how real
locals work:

- Invoked functions cannot change the binding for the invoking function ...

Example:
```python
xcurrent = xlocal()

def with_xlocal(func, **kwargs):
    with xcurrent(**kwargs):
        func()

def handle_request(request):
    func = gethandler(request)  # some user code
    spawn(with_xlocal(func, request=request))
```

Sections: Usage in frameworks and libraries invoking "handlers", Issues worth noting, Copyright / inspiration

</details>

### xarray-dataclass

xarray data creation by data classes

`pip install xarray-dataclass` · installs (wheel) · licence: MIT License · rank 11120 · last release 2025-07-30 · [PyPI](https://pypi.org/project/xarray-dataclass/) · [docs](https://xarray-contrib.github.io/xarray-dataclass/) · [source](https://github.com/xarray-contrib/xarray-dataclass/)

<details><summary>README extract</summary>

xarray data creation by data classes

This repository is adapted from here. We are grateful for the
work of the developer on this repo. Sadly, that repository is inactive. Thus, a fork was moved here in order to allow
for more visibility and community maintenance.

Features:
xarray-dataclass is a Python package that makes it easy to create [xarray]'s DataArray and Dataset objects that are "typed" (i.e. fixed dimensions, data type, coordinates, attributes, and name) using [the Python's dataclass]:

Example:
```python
from dataclasses import dataclass
from typing import Literal
from xarray_dataclass import AsDataArray, AsDataset
from xarray_dataclass import Attr, Coord, Data, Name

X = Literal["x"]
Y = Literal["y"]
```

...

</details>

### xrpl-py

A complete Python library for interacting with the XRP ledger

`pip install xrpl-py` · installs (wheel) · licence: OSI Approved · rank 12461 · last release 2026-09-16 · [PyPI](https://pypi.org/project/xrpl-py/) · [docs](https://xrpl-py.readthedocs.io) · [source](https://github.com/XRPLF/xrpl-py)

<details><summary>README extract</summary>

A pure Python implementation for interacting with the XRP Ledger.

The `xrpl-py` library simplifies the hardest parts of XRP Ledger interaction, like serialization and transaction signing. It also provides native Python methods and models for XRP Ledger transactions and core server API (`rippled`) objects. ...

Features:
Use `xrpl-py` to build Python applications that leverage the XRP Ledger. The library helps with all aspects of interacting with the XRP Ledger, including:

- Key and wallet management
- Serialization
- Transaction Signing

`xrpl-py` also provides: ...

Example:
```python
from xrpl.account import get_balance
from xrpl.clients import JsonRpcClient
from xrpl.models import Payment, Tx
from xrpl.transaction import submit_and_wait
from xrpl.wallet import generate_faucet_wallet

...

</details>

### xraydb

calculations with XrayDB: reference data for X-ray interactions with matter

`pip install xraydb` · installs (wheel) · licence: MIT · rank 12670 · last release 2025-07-18 · [PyPI](https://pypi.org/project/xraydb/) · [docs](https://xraypy.github.io/XrayDB/)

<details><summary>README extract</summary>

Python interface to XrayDB: X-ray Reference Data for the Elements

To install, use

License: MIT

</details>

### XMind

XMind是基于Python实现，提供了对XMind思维导图进行创建、解析、更新的一站式解决方案！

`pip install XMind` · installs (wheel) · licence: MIT License · rank 12795 · last release 2019-01-10 · [PyPI](https://pypi.org/project/XMind/)

<details><summary>README extract</summary>

XMind 是基于 Python 实现，提供了对 XMind思维导图进行创建、解析、更新的一站式解决方案！

Example:
```python
def gen_my_xmind_file():
    # 1、如果指定的XMind文件存在，则加载，否则创建一个新的
    workbook = xmind.load("my.xmind")

    # 2、获取第一个画布（Sheet），默认新建一个XMind文件时，自动创建一个空白的画布
    sheet1 = workbook.getPrimarySheet()
    # 对第一个画布进行设计完善，具体参照下一个函数
    design_sheet1(sheet1)

    # 3、创建第二个画布
    gen_sheet2(workbook, sheet1)

    # 4、保存（如果指定path参数，另存为该文件名）
...
```

Sections: XMind, 一、安装方式, 二、版本升级, 三、使用方式, 1、创建XMind文件, 2、解析XMind文件, (1) 将XMind文件转换为Dict数据 / JSON数据, （2）将画布转换为Dict数据, (3) 将主题转换为Dict数据, (4) 自定义解析, 3、更新保存XMind文件, （1）五种保存方法, （2）XMind文件结构, 四、工具支持功能

</details>

### xy

Experimental Python charting engine with a native Rust core, binary columnar transport, and a GPU render client

`pip install xy` · installs (wheel) · licence: Apache-2.0 · rank 13834 · last release 2026-11-05 · [PyPI](https://pypi.org/project/xy/) · [source](https://github.com/reflex-dev/xy)

<details><summary>README extract</summary>

XY is an extremely fast, interactive, customizable Python charting library for
the web, notebooks, and static exports.

Charts are composed declaratively or through matplotlib conventions. You can
fully customize them with Python, CSS, or Tailwind.

With small charts, every point is sent to the browser. ...

Example:
```python
import xy

chart = xy.line_chart(xy.line([1, 2, 3, 4, 5], [120, 180, 165, 240, 310]))
# chart.to_html("chart.html")
# chart.to_png("chart.png")
# chart.to_svg("chart.svg")
chart  # notebooks render it
```

Sections: Is XY right for me?, Getting started, Coming from Matplotlib, Customize every layer, Benchmarks, Embed XY in a Reflex app, Examples, How it works, Roadmap

</details>

### xorq-datafusion

(no summary)

`pip install xorq-datafusion` · installs (wheel) · licence: not stated · rank 14018 · last release 2026-11-06 · [PyPI](https://pypi.org/project/xorq-datafusion/)

### xacrodoc

Compile xacro files to URDF or MJCF from Python or the command line (no ROS required).

`pip install xacrodoc` · installs (wheel) · licence: MIT · rank 14534 · last release 2026-04-20 · [PyPI](https://pypi.org/project/xacrodoc/)

<details><summary>README extract</summary>

xacrodoc is a tool for compiling xacro files to
plain URDF files or Mujoco MJCF files from within
Python code or via the
command line. It is fully functional whether ROS is
installed on the system or not.

Features:
Compared to the regular xacro package, xacrodoc allows you to:

* Conveniently convert xacro files to URDF or Mujoco MJCF files without a ROS
 installation (this includes converting plain URDF to MJCF). ...

Example:
```python
import os
from xacrodoc import XacroDoc

doc = XacroDoc.from_file("robot.urdf.xacro")

# or relative to a ROS package
# e.g., for a file located at some_ros_package/urdf/robot.urdf.xacro:
doc = XacroDoc.from_package_file("some_ros_package", "urdf/robot.urdf.xacro")

# convert to a string of URDF
urdf_str = doc.to_urdf_string()

...
```

...

</details>

