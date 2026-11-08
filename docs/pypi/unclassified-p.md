# Unclassified / P (part 1 of 3)

[Index](README.md) · 979 packages in this topic, by downloads.

part 1 · [part 2](unclassified-p-2.md) · [part 3](unclassified-p-3.md)

### packaging

Core utilities for Python packages

`pip install packaging` · installs (wheel) · licence: Apache-2.0 OR BSD-2-Clause · rank 2 · last release 2026-08-04 · [PyPI](https://pypi.org/project/packaging/) · [docs](https://packaging.pypa.io/) · [source](https://github.com/pypa/packaging)

<details><summary>README extract</summary>

Reusable core utilities for various Python Packaging
interoperability specifications.

This library provides utilities that implement the interoperability
specifications which have clearly one correct behaviour (eg: 440)
or benefit greatly from having a single shared implementation (eg: 425). ...

Sections: packaging, Documentation, Discussion

</details>

### pycparser

C parser in Python

`pip install pycparser` · installs (wheel) · licence: BSD-3-Clause · rank 13 · last release 2026-10-22 · [PyPI](https://pypi.org/project/pycparser/)

<details><summary>README extract</summary>

pycparser is a parser for the C language, written in pure Python. It is a
module designed to be easily integrated into applications that need to parse
C source code.

Example:
```python
from pycparser import CParser, parse_file

ast = parse_file(
    "example.c",
    use_cpp=True,
    cpp_args=["-std=c23"],
    parser=CParser(dialect="c23"),
)
```

Sections: pycparser, Introduction, What is pycparser?, What is it good for?, What grammar does pycparser follow?, Contact details, Prerequisites, Using, Interaction with the C preprocessor, What about the standard C library headers?, Basic usage, Advanced usage, Modifying

</details>

### pydantic_core

Core functionality for Pydantic validation and serialization

`pip install pydantic_core` · installs (wheel) · licence: MIT · rank 19 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pydantic_core/) · [source](https://github.com/pydantic/pydantic/tree/main/pydantic-core)

<details><summary>README extract</summary>

This package provides the core functionality for pydantic validation and serialization.

Pydantic-core is currently around 17x faster than pydantic V1.
See `tests/benchmarks/` for details.

Example:
```python
from pydantic_core import SchemaValidator, ValidationError

v = SchemaValidator(
    {
        'type': 'typed-dict',
        'fields': {
            'name': {
                'type': 'typed-dict-field',
                'schema': {
                    'type': 'str',
                },
            },
            'age': {
...
```

Sections: pydantic-core, Example of direct usage, Getting Started, Prerequisites, Quick Start, Useful Resources, Profiling, Releasing

</details>

### protobuf

(no summary)

`pip install protobuf` · installs (wheel) · licence: 3-Clause BSD License · rank 34 · last release 2026-09-17 · [PyPI](https://pypi.org/project/protobuf/)

### pyarrow

Python library for Apache Arrow

`pip install pyarrow` · installs (wheel) · licence: Apache-2.0 · rank 78 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyarrow/) · [docs](https://arrow.apache.org/docs/python) · [source](https://github.com/apache/arrow)

<details><summary>README extract</summary>

<!---
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements. See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership. ...

Sections: Python library for Apache Arrow, Building the documentation

</details>

### PyNaCl

Python binding to the Networking and Cryptography (NaCl) library

`pip install PyNaCl` · installs (wheel) · licence: Apache Software License · rank 184 · last release 2026-01-01 · [PyPI](https://pypi.org/project/PyNaCl/) · [docs](https://pynacl.readthedocs.io)

<details><summary>README extract</summary>

PyNaCl is a Python binding to libsodium, which is a fork of the
Networking and Cryptography library. These libraries have a stated goal of
improving usability, security and speed. It supports Python 3.8+ as well as
PyPy 3.

Features:
* Digital signatures
* Secret-key encryption
* Public-key encryption
* Hashing and message authentication
* Password based key derivation and password hashing

Sections: PyNaCl: Python binding to the libsodium library, Features, Faster wheel build, Linux source build, 1.6.2 (2026-01-01), 1.6.1 (2025-11-10), 1.6.0 (2025-09-11), 1.5.0 (2022-01-07), 1.4.0 (2020-05-25), 1.3.0 2018-09-26, 1.2.1 - 2017-12-04, 1.2.0 - 2017-11-01, 1.1.2 - 2017-03-31, 1.1.1 - 2017-03-15

</details>

### pre-commit

A framework for managing and maintaining multi-language pre-commit hooks.

`pip install pre-commit` · installs (wheel) · licence: MIT · rank 211 · last release 2026-10-12 · [PyPI](https://pypi.org/project/pre-commit/)

<details><summary>README extract</summary>

A framework for managing and maintaining multi-language pre-commit hooks.

For more information see:

</details>

### pytest-json-ctrf

Pytest plugin to generate json report in CTRF (Common Test Report Format)

`pip install pytest-json-ctrf` · installs (wheel) · licence: MIT · rank 249 · last release 2026-10-04 · [PyPI](https://pypi.org/project/pytest-json-ctrf/)

<details><summary>README extract</summary>

Pytest implementation of Common Test Report Format (CTRF) for test results.
Test report will be generated in JSON format.
Test report can be used to prettify the report in GitHub Actions with github-actions-ctrf.
Do not worry if report in GitHub does not appear immediately. It takes some time to process the report.

Features:
- Generates JSON report
- Tested to work correctly with and without pytest-xdist
- Tested to get browser name from pytest-playwright
- Reruns from pytest-rerunfailures are reported as `retries`, `retryAttempts` and `flaky` ...

Sections: CTRF for pytest, Features, Usage, JSON example, Report Example, Technical details, Roadmap

</details>

### pyproject-hooks

Wrappers to call pyproject.toml-based build backend hooks.

`pip install pyproject-hooks` · installs (wheel) · licence: MIT · rank 284 · last release 2026-09-16 · [PyPI](https://pypi.org/project/pyproject-hooks/) · [docs](https://pyproject-hooks.readthedocs.io/) · [source](https://github.com/pypa/pyproject-hooks)

<details><summary>README extract</summary>

This is a low-level library for calling build-backends in `pyproject.toml`-based project. It provides the basic functionality to help write tooling that generates distribution files from Python projects.

If you want a tool that builds Python packages, you'll want to use instead. ...

</details>

### pure-eval

Safely evaluate AST nodes without side effects

`pip install pure-eval` · installs (wheel) · licence: MIT License · rank 287 · last release 2026-09-10 · [PyPI](https://pypi.org/project/pure-eval/)

<details><summary>README extract</summary>

This is a Python package that lets you safely evaluate certain AST nodes without triggering arbitrary code that may have unwanted side effects.

It can be installed from PyPI:

 pip install pure_eval

To demonstrate usage, suppose we have an object defined as follows: ...

Example:
```python
class Rectangle:
    def init(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        print("Calculating area...")
        return self.width * self.height

rect = Rectangle(3, 5)
```

</details>

### pytokens

A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons.

`pip install pytokens` · installs (wheel) · licence: MIT License · rank 325 · last release 2026-01-30 · [PyPI](https://pypi.org/project/pytokens/)

<details><summary>README extract</summary>

A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons.

Sections: pytokens, Usage, Type Checking, Compilation with mypyc, Create and upload a package to PyPI

</details>

### pyperclip

A cross-platform clipboard module for Python. (Only handles plain text for now.)

`pip install pyperclip` · installs (wheel) · licence: BSD License · rank 343 · last release 2025-09-26 · [PyPI](https://pypi.org/project/pyperclip/)

<details><summary>README extract</summary>

Pyperclip is a cross-platform Python module for copy and paste clipboard functions. It works with Python 2 and 3.

Install on Windows: `pip install pyperclip`

Install on Linux/macOS: `pip3 install pyperclip`

Al Sweigart al@inventwithpython.com
BSD License

</details>

### python-slugify

A Python slugify application that also handles Unicode

`pip install python-slugify` · installs (wheel) · licence: MIT · rank 346 · last release 2026-10-07 · [PyPI](https://pypi.org/project/python-slugify/)

<details><summary>README extract</summary>

Unicode-aware slug generation for Python, with explicit transliteration choices.

Example:
```python
from slugify import slugify

# Use the modern algorithm for the latest rules.
assert slugify("C'est déjà l'été.", algorithm='modern') == 'c-est-deja-l-ete'
assert slugify('影師嗎', backend='text-unidecode', algorithm='modern') == 'ying-shi-ma'
assert slugify('影師嗎', allow_unicode=True, algorithm='modern') == '影師嗎'

...
```

Sections: Python Slugify, Quickstart, API options, Recipes and boundaries, Command line, Licensing

</details>

### py-key-value-aio

Async Key-Value Store - A pluggable interface for KV Stores

`pip install py-key-value-aio` · installs (wheel) · licence: Apache-2.0 · rank 371 · last release 2026-09-18 · [PyPI](https://pypi.org/project/py-key-value-aio/)

<details><summary>README extract</summary>

This monorepo contains:

- `py-key-value-aio`: Async key-value store library (primary and supported).
- `py-key-value-sync`: Sync version (no longer planned; async-only focus).

- Full Documentation
- Getting Started Guide
- Stores Guide
- Wrappers Guide
- Adapters Guide
- API Reference ...

Features:
- Multiple backends: Aerospike, Azure Tables, chDB, DuckDB, DynamoDB,
 Elasticsearch, FileTree, Firestore, Keyring, Memcached, MongoDB, OpenSearch,
 PostgreSQL, Redis, RocksDB, S3, Valkey, Vault, Windows Registry, and
 In-memory, Disk, etc. ...

Example:
```python
from key_value.aio.protocols.key_value import AsyncKeyValue

class YourFramework:
    def init(self, cache: AsyncKeyValue):
        self.cache = cache
```

...

</details>

### pendulum

Python datetimes made easy

`pip install pendulum` · installs (wheel) · licence: MIT License · rank 422 · last release 2026-10-12 · [PyPI](https://pypi.org/project/pendulum/) · [docs](https://pendulum.eustace.io/docs) · [source](https://github.com/sdispater/pendulum)

<details><summary>README extract</summary>

Python datetimes made easy.

Supports Python 3.10 and newer.

Features:
Native `datetime` instances are enough for basic cases but when you face more complex use-cases
they often show limitations and are not so intuitive to work with. ...

Example:
```python
>>> import pendulum

>>> now_in_paris = pendulum.now('Europe/Paris')
>>> now_in_paris
'2016-07-04T00:49:58.502116+02:00'

# Seamless timezone switching
>>> now_in_paris.in_timezone('UTC')
'2016-07-03T22:49:58.502116+00:00'

>>> tomorrow = pendulum.now().add(days=1)
>>> last_week = pendulum.now().subtract(weeks=1)

...
```

Sections: Pendulum, Resources, Why Pendulum?, Limitations, Getting started, Localization

</details>

### pdfplumber

Plumb a PDF for detailed information about each char, rectangle, and line.

`pip install pdfplumber` · installs (wheel) · licence: MIT License · rank 435 · last release 2026-06-15 · [PyPI](https://pypi.org/project/pdfplumber/)

<details><summary>README extract</summary>

Plumb a PDF for detailed information about each text character, rectangle, and line. Plus: Table extraction and visual debugging.

Works best on machine-generated, rather than scanned, PDFs. Built on `pdfminer.six`.

Currently tested on Python 3.10, 3.11, 3.12, 3.13, 3.14. ...

Example:
```python
import pdfplumber

with pdfplumber.open("path/to/file.pdf") as pdf:
    first_page = pdf.pages[0]
    print(first_page.chars[0])
```

Sections: pdfplumber, Command line interface, Basic example, Options, Python library, Loading a PDF, The `pdfplumber.PDF` class, The `pdfplumber.Page` class, Objects, `char` properties, `line` properties, `rect` properties, `curve` properties

</details>

### pyspark

Apache Spark Python API

`pip install pyspark` · installs from source (sdist only) · licence: Apache-2.0 · rank 453 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyspark/)

<details><summary>README extract</summary>

Spark is a unified analytics engine for large-scale data processing. It provides
high-level APIs in Scala, Java, Python, and R, and an optimized engine that
supports general computation graphs for data analysis. ...

Sections: Apache Spark, Online Documentation, Python Packaging, Python Requirements

</details>

### posthog

Integrate PostHog into any python application.

`pip install posthog` · installs (wheel) · licence: MIT · rank 472 · last release 2026-11-06 · [PyPI](https://pypi.org/project/posthog/) · [source](https://github.com/posthog/posthog-python)

<details><summary>README extract</summary>

Please see the main PostHog docs.

SDK usage examples and code snippets live in the official documentation so they stay up to date.

Sections: PostHog Python, Documentation, Releasing

</details>

### PySocks

A Python SOCKS client module. See https://github.com/Anorov/PySocks for more information.

`pip install PySocks` · installs (wheel) · licence: BSD · rank 479 · last release 2019-09-20 · [PyPI](https://pypi.org/project/PySocks/)

<details><summary>README extract</summary>

PySocks lets you send traffic through SOCKS and HTTP proxy servers. It is a modern fork of SocksiPy with bug fixes and extra features.

Acts as a drop-in replacement to the socket module. Seamlessly configure SOCKS proxies for any socket object by calling `socket_object.set_proxy()`.

Features:
* SOCKS proxy client for Python 2.7 and 3.4+
* TCP supported
* UDP mostly supported (issues may occur in some edge cases)
* HTTP proxy client included but not supported or recommended (you should use urllib2's or requests' own HTTP proxy ...

Sections: PySocks, Features, Usage, socks.socksocket, Monkeypatching, urllib2 Handler

</details>

### pgvector

pgvector support for Python

`pip install pgvector` · installs (wheel) · licence: MIT · rank 545 · last release 2026-10-09 · [PyPI](https://pypi.org/project/pgvector/)

<details><summary>README extract</summary>

pgvector support for Python

Supports Django, SQLAlchemy, SQLModel, Psycopg 3, Psycopg 2, asyncpg, pg8000, and Peewee

Example:
```python
from pgvector.django import VectorExtension

class Migration(migrations.Migration):
    operations = [
        VectorExtension()
    ]
```

Sections: pgvector-python, Django, Half-Precision Indexing, SQLAlchemy, Binary Quantization, Arrays, SQLModel, Psycopg 3, Psycopg 2, asyncpg, pg8000, Peewee, Reference

</details>

### pydyf

A low-level PDF generator.

`pip install pydyf` · installs (wheel) · licence: BSD License · rank 553 · last release 2026-10-14 · [PyPI](https://pypi.org/project/pydyf/) · [docs](https://doc.courtbouillon.org/pydyf/) · [source](https://github.com/CourtBouillon/pydyf)

<details><summary>README extract</summary>

pydyf is a low-level PDF generator written in Python.

* Free software: BSD license
* For Python 3.11+, tested on CPython and PyPy

Copyrights are retained by their contributors, no copyright assignment is
required to contribute to pydyf. ...

</details>

### pip-api

An unofficial, importable pip API

`pip install pip-api` · installs (wheel) · licence: Apache Software License · rank 569 · last release 2026-09-08 · [PyPI](https://pypi.org/project/pip-api/) · [source](https://github.com/di/pip-api)

<details><summary>README extract</summary>

<!--- BADGES: START --->
[][#github-license]
[][#pypi-package]
[][#pypi-package]
[][#conda-forge-package]
[][#conda-forge-package]
[][#conda-forge-feedstock]

<!--- BADGES: END --->

Since `pip` is a command-line-tool, it does not have
an official, supported, _importable_
API. ...

Sections: Goal, Scope, Available with all `pip` versions, Use cases

</details>

### pbs-installer

Installer for Python Build Standalone

`pip install pbs-installer` · installs (wheel) · licence: MIT · rank 579 · last release 2026-10-25 · [PyPI](https://pypi.org/project/pbs-installer/) · [docs](http://pbs-installer.readthedocs.io) · [source](https://github.com/frostming/pbs-installer)

### passlib

comprehensive password hashing framework supporting over 30 schemes

`pip install passlib` · installs (wheel) · licence: BSD · rank 598 · last release 2020-10-08 · [PyPI](https://pypi.org/project/passlib/)

<details><summary>README extract</summary>

Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 30 password hashing algorithms, as well
as a framework for managing existing password hashes. ...

</details>

### pyroaring

Library for handling efficiently sorted integer sets.

`pip install pyroaring` · installs (wheel) · licence: MIT License · rank 613 · last release 2026-10-03 · [PyPI](https://pypi.org/project/pyroaring/)

<details><summary>README extract</summary>

An efficient and light-weight ordered set of integers.
This is a Python wrapper for the C library CRoaring.

Example:
```python
from pyroaring import BitMap
bm1 = BitMap()
bm1.add(3)
bm1.add(18)
print("has 3:", 3 in bm1)
print("has 4:", 4 in bm1)
bm2 = BitMap([3, 27, 42])
print("bm1       = %s" % bm1)
print("bm2       = %s" % bm2)
print("bm1 & bm2 = %s" % (bm1&bm2))
print("bm1 | bm2 = %s" % (bm1|bm2))
```

Sections: Example, Optimizing the builds for your machine (x64), Updating CRoaring, Tracking Package and CRoaring versions, Benchmark

</details>

### pymupdf4llm

(no summary)

`pip install pymupdf4llm` · installs (wheel) · licence: not stated · rank 620 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pymupdf4llm/)

<details><summary>README extract</summary>

This is an empty package that is required by pymupdf-2.x, in order to avoid
a pip bug that can result in a broken installation when upgrading from
pymupdf-1.x to pymupdf-2.x.

[The pymupdf-2.x package now contains the 4llm code that used to be in
pymupdf4llm-1.x.]

To install pymupdf please do `pip install pymupdf`. ...

</details>

### postgrest

PostgREST client for Python. This library provides an ORM interface to PostgREST.

`pip install postgrest` · installs (wheel) · licence: MIT · rank 640 · last release 2026-11-06 · [PyPI](https://pypi.org/project/postgrest/) · [docs](https://postgrest-py.rtfd.io) · [source](https://github.com/supabase/supabase-py)

<details><summary>README extract</summary>

PostgREST client for Python. This library provides an "ORM-like" interface to PostgREST.

Example:
```python
import asyncio
from postgrest import AsyncPostgrestClient

async def main():
    async with AsyncPostgrestClient(" as client:
        r = await client.from("countries").select("*").execute()
        countries = r.data

asyncio.run(main())
```

Sections: postgrest-py, Requirements, Local PostgREST server, Instructions, With uv (recommended), With Pip, Supabase Service Compatibility, USAGE, Getting started, Create, Read, Update, Delete, General filters

</details>

### pytest-runner

Invoke py.test as distutils command with dependency resolution

`pip install pytest-runner` · installs (wheel) · licence: MIT License · rank 648 · last release 2023-12-04 · [PyPI](https://pypi.org/project/pytest-runner/)

<details><summary>README extract</summary>

Setup scripts can use pytest-runner to add setup.py test support for pytest
runner.

pytest-runner depends on deprecated features of setuptools and relies on features that break security
mechanisms in pip. For example 'setup_requires' and 'tests_require' bypass `pip --require-hashes`.
See also pypa/setuptools#1684.

It is recommended that you: ...

Example:
```python
setup(
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
```

Sections: Deprecation Notice, Usage, Example, Standalone Example, Considerations, Conditional Requirement, For Enterprise

</details>

### partd

Appendable key-value storage

`pip install partd` · installs (wheel) · licence: BSD · rank 663 · last release 2024-05-06 · [PyPI](https://pypi.org/project/partd/)

<details><summary>README extract</summary>

Key-value byte store with appendable values

 Partd stores key-value pairs.
 Values are raw bytes.
 We append on old values.

Partd excels at shuffling operations.

PartD has two main operations, `append` and `get`.

Example:
```python
>>> import partd
>>> p = partd.File('/path/to/new/dataset/')
```

Sections: PartD, Operations, Example, Implementations, Encodings and Compression, Composition

</details>

### ply

Python Lex & Yacc

`pip install ply` · installs (wheel) · licence: BSD · rank 666 · last release 2018-02-15 · [PyPI](https://pypi.org/project/ply/)

<details><summary>README extract</summary>

PLY is yet another implementation of lex and yacc for Python. Some notable
features include the fact that its implemented entirely in Python and it
uses LALR(1) parsing which is efficient and well suited for larger grammars. ...

</details>

### pymupdf-layout

(no summary)

`pip install pymupdf-layout` · installs (wheel) · licence: not stated · rank 668 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pymupdf-layout/)

<details><summary>README extract</summary>

This is an empty package that is required by pymupdf-2.x, in order to avoid
a pip bug that can result in a broken installation when upgrading from
pymupdf-1.x to pymupdf-2.x.

[The pymupdf-2.x package now contains the layout code that used to be in
pymupdf_layout-1.x.]

To install pymupdf please do `pip install pymupdf`. ...

</details>

### python-engineio

Engine.IO server and client for Python

`pip install python-engineio` · installs (wheel) · licence: MIT · rank 702 · last release 2026-10-28 · [PyPI](https://pypi.org/project/python-engineio/) · [docs](https://python-engineio.readthedocs.io/) · [source](https://code.miguelgrinberg.com/miguelgrinberg/python-engineio)

<details><summary>README extract</summary>

Python implementation of the `Engine.IO` realtime client and server.

Resources

- git
- Change Log
- Documentation
- PyPI
- Contributor's guide
- Security policy

Sponsor this project

This project relies on contributions from its users. ...

</details>

### python-socketio

Socket.IO server and client for Python

`pip install python-socketio` · installs (wheel) · licence: MIT · rank 706 · last release 2026-11-03 · [PyPI](https://pypi.org/project/python-socketio/) · [docs](https://python-socketio.readthedocs.io/) · [source](https://code.miguelgrinberg.com/miguelgrinberg/python-socketio)

<details><summary>README extract</summary>

Python implementation of the `Socket.IO` realtime client and server.

Version compatibility

The Socket.IO protocol has been through a number of revisions, and some of these
introduced backward incompatible changes, which means that the client and the
server must use compatible versions for everything to work. ...

</details>

### pyiceberg

Apache Iceberg is an open table format for huge analytic datasets

`pip install pyiceberg` · installs (wheel) · licence: Apache-2.0 · rank 715 · last release 2026-09-01 · [PyPI](https://pypi.org/project/pyiceberg/) · [source](https://github.com/apache/iceberg-python)

<details><summary>README extract</summary>

<!--
 - Licensed to the Apache Software Foundation (ASF) under one or more
 - contributor license agreements. See the NOTICE file distributed with
 - this work for additional information regarding copyright ownership. ...

Sections: Iceberg Python, Get in Touch

</details>

### python-magic

File type identification using libmagic

`pip install python-magic` · installs (wheel) · licence: MIT License · rank 735 · last release 2022-06-07 · [PyPI](https://pypi.org/project/python-magic/)

<details><summary>README extract</summary>

python-magic is a Python interface to the libmagic file type
identification library. libmagic identifies file types by checking
their headers according to a predefined list of file types. This
functionality is exposed to the command line by the Unix command
`file`.

Example:
```python
>>> import magic
>>> magic.from_file("testdata/test.pdf")
'PDF document, version 1.2'
# recommend using at least the first 2048 bytes, as less can produce incorrect identification
>>> magic.from_buffer(open("testdata/test.pdf", "rb").read(2048))
'PDF document, version 1.2'
>>> magic.from_file("testdata/test.pdf", mime=True)
'application/pdf'
```

Sections: python-magic, Usage, Debian/Ubuntu, Windows, OSX, Troubleshooting, Bug Reports, Running the tests, libmagic python API compatibility, Versioning

</details>

### pyrsistent

Persistent/Functional/Immutable data structures

`pip install pyrsistent` · installs (wheel) · licence: MIT License · rank 753 · last release 2023-10-25 · [PyPI](https://pypi.org/project/pyrsistent/)

<details><summary>README extract</summary>

Pyrsistent is a number of persistent collections (by some referred to as functional data structures). Persistent in
the sense that they are immutable.

All methods on a data structure that would normally mutate it instead return a new copy of the structure containing the
requested updates. The original structure is left untouched. ...

Example:
```python
>>> from pyrsistent import v, pvector

# No mutation of vectors once created, instead they
# are "evolved" leaving the original untouched
>>> v1 = v(1, 2, 3)
>>> v2 = v1.append(4)
>>> v3 = v2.set(1, 5)
>>> v1
pvector([1, 2, 3])
>>> v2
pvector([1, 2, 3, 4])
>>> v3
pvector([1, 5, 3, 4])

# Random access and slicing
>>> v3[1]
5
>>> v3[1:3]
...
```

...

</details>

### python-http-client

HTTP REST client, simplified for Python

`pip install python-http-client` · installs (wheel) · licence: MIT · rank 764 · last release 2022-03-09 · [PyPI](https://pypi.org/project/python-http-client/)

<details><summary>README extract</summary>

The default branch name for this repository has been changed to `main` as of 07/27/2020.

Quickly and easily access any RESTful or RESTful-like API.

If you are looking for the Twilio SendGrid API client library, please see this repo.

Example:
```python
import python_http_client

global_headers = {"Authorization": "Bearer XXXXXXX"}
client = Client(host='base_url', request_headers=global_headers)
client.your.api._(param).call.get()
print(response.status_code)
print(response.headers)
print(response.body)
```

Sections: Prerequisites, API Key, Quick Start, Usage, Local Setup of the Project, Troubleshooting, Announcements, Thanks, About

</details>

### pyarrow-hotfix

(no summary)

`pip install pyarrow-hotfix` · installs (wheel) · licence: Apache License, Version 2.0 · rank 768 · last release 2025-04-25 · [PyPI](https://pypi.org/project/pyarrow-hotfix/) · [docs](https://github.com/pitrou/pyarrow-hotfix#readme) · [source](https://github.com/pitrou/pyarrow-hotfix)

<details><summary>README extract</summary>

This is a hotfix for the PyArrow security vulnerability
CVE-2023-47248.

We generally recommend upgrading to PyArrow 14.0.1 or later, but if you
cannot upgrade, this package disables the vulnerability on older versions.

Example:
```python
import pyarrow_hotfix
```

Sections: PyArrow Hotfix, Description, Usage, Dependencies, Example

</details>

### papermill

Parameterize and run Jupyter and nteract Notebooks

`pip install papermill` · installs (wheel) · licence: BSD License · rank 828 · last release 2026-02-27 · [PyPI](https://pypi.org/project/papermill/) · [docs](https://papermill.readthedocs.io) · [source](https://github.com/nteract/papermill/)

<details><summary>README extract</summary>

papermill is a tool for parameterizing, executing, and analyzing
Jupyter Notebooks.

Papermill lets you:

- parameterize notebooks
- execute notebooks

This opens up new opportunities for how notebooks can be used. For
example: ...

Sections: Usage, Parameterizing a Notebook, Executing a Notebook, Execute via the Python API, Execute via CLI, Documentation

</details>

### pytesseract

Python-tesseract is a python wrapper for Google's Tesseract-OCR

`pip install pytesseract` · installs (wheel) · licence: Apache Software License · rank 836 · last release 2024-08-16 · [PyPI](https://pypi.org/project/pytesseract/)

<details><summary>README extract</summary>

Python-tesseract is an optical character recognition (OCR) tool for python.
That is, it will recognize and "read" the text embedded in images.

Python-tesseract is a wrapper for Google's Tesseract-OCR Engine. ...

Example:
```python
from PIL import Image

import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
...
```

Sections: Python Tesseract, USAGE

</details>

### python-utils

Python Utils is a module with some convenient utilities not included with the standard Python install

`pip install python-utils` · installs (wheel) · licence: BSD-3-Clause · rank 848 · last release 2026-11-05 · [PyPI](https://pypi.org/project/python-utils/) · [docs](https://python-utils.readthedocs.io/) · [source](https://github.com/WoLpH/python-utils)

<details><summary>README extract</summary>

The fast, fully-typed stdlib helpers you keep rewriting — in one tiny, dependency-light package.

Typed: mypy, pyright and pyrefly

Documentation ·
PyPI ·
Source ·
Issues

Python Utils is a collection of small, battle-tested functions and classes that
make everyday Python patterns shorter, safer and faster. ...

Example:
```python
import python_utils

# Pull a number out of any messy string
python_utils.to_int('listening on port=8080', regexp=True)   # 8080

# Human-readable sizes: (value, power-of-1024)
python_utils.scale_1024(1536, 2)                             # (1.5, 1)  -> 1.5 KiB

# Remap a value between ranges (46% volume -> dB on an AVR)
...
```

...

</details>

### pbr

Python Build Reasonableness

`pip install pbr` · installs (wheel) · licence: Apache-2.0 · rank 863 · last release 2026-10-07 · [PyPI](https://pypi.org/project/pbr/) · [docs](https://docs.openstack.org/pbr/) · [source](https://opendev.org/openstack/pbr)

<details><summary>README extract</summary>

PBR is a library that injects some useful and sensible default behaviors
into your setuptools run. It started off life as the chunks of code that
were copied between all of the OpenStack projects. ...

</details>

### pdf2image

A wrapper around the pdftoppm and pdftocairo command line tools to convert PDF to a PIL Image list.

`pip install pdf2image` · installs (wheel) · licence: MIT License · rank 865 · last release 2024-01-07 · [PyPI](https://pypi.org/project/pdf2image/)

<details><summary>README extract</summary>

A python (3.7+) module that wraps pdftoppm and pdftocairo to convert PDF to a PIL Image object

Example:
```python
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
```

Sections: pdf2image, Windows, Mac, Linux, Platform-independant (Using `conda`), How does it work?, What's new?, Performance tips, Limitations / known issues

</details>

### pywin32

Python for Windows Extensions

`pip install pywin32` · does not install on CPython 3.14 · licence: Python Software Foundation License · rank 898 · last release 2026-06-04 · [PyPI](https://pypi.org/project/pywin32/) · [docs](https://mhammond.github.io/pywin32/)

<details><summary>README extract</summary>

This is the readme for the Python for Win32 (pywin32) extensions, which provides access to many of the Windows APIs from Python, including COM support.

See CHANGES.md for recent notable changes.

adodbapi's documentation can be found in: adodbapi/readme.txt

isapi's documentation can be found in: isapi/README.txt ...

Sections: pywin32, Docs, Binaries, Running as a Windows Service, Troubleshooting, Building from source, Versioning

</details>

### pycares

Python interface for c-ares

`pip install pycares` · installs (wheel) · licence: MIT · rank 919 · last release 2026-10-20 · [PyPI](https://pypi.org/project/pycares/)

<details><summary>README extract</summary>

pycares is a Python module which provides an interface to c-ares.
c-ares is a C library that performs
DNS requests and name resolutions asynchronously.

pycares currently bundles c-ares as a submodule for ease of building. Using the system
provided c-ares is possible if the `PYCARES_USE_SYSTEM_LIB` environment variable is
set to `1` when building. ...

Sections: pycares: Python interface for c-ares, Documentation, Bundled c-ares, Running the test suite, Using it from the cli, a la dig

</details>

### pathlib-abc

Backport of pathlib ABCs

`pip install pathlib-abc` · installs (wheel) · licence: Python Software Foundation License · rank 960 · last release 2025-10-10 · [PyPI](https://pypi.org/project/pathlib-abc/)

<details><summary>README extract</summary>

Base classes for `pathlib.Path`-ish objects. Requires Python 3.9+.

This package is a preview of `pathlib` functionality planned for a future
release of Python; specifically, it provides three ABCs that can be used to
implement path classes for non-local filesystems, such as archive files and
storage servers: ...

</details>

### pyspnego

Windows Negotiate Authentication Client and Server

`pip install pyspnego` · installs (wheel) · licence: MIT · rank 1006 · last release 2026-10-06 · [PyPI](https://pypi.org/project/pyspnego/)

<details><summary>README extract</summary>

Library to handle SPNEGO (Negotiate, NTLM, Kerberos) and CredSSP authentication. Also includes a packet parser that can
be used to decode raw NTLM/SPNEGO/Kerberos tokens into a human readable format.

See How to Install for more details

* CPython 3.9+
* cryptography
* sspilib - Windows only ...

Sections: Python SPNEGO Library, Requirements, Optional Requirements, Kerberos Authentication, How to Use, CredSSP Authentication, Backlog

</details>

### prometheus-fastapi-instrumentator

Instrument your FastAPI app with Prometheus metrics

`pip install prometheus-fastapi-instrumentator` · installs (wheel) · licence: OSI Approved · rank 1010 · last release 2026-07-26 · [PyPI](https://pypi.org/project/prometheus-fastapi-instrumentator/)

<details><summary>README extract</summary>

Features:
Beyond the fast track, this instrumentator is highly configurable and it is
very easy to customize and adapt to your specific use case. Here is a list of
some of these options you may opt-in to:

- Regex patterns to ignore certain routes. ...

Example:
```python
from prometheus_fastapi_instrumentator import Instrumentator, metrics

instrumentator = Instrumentator(
    should_group_status_codes=False,
    should_ignore_untemplated=True,
    should_respect_env_var=True,
    should_instrument_requests_inprogress=True,
    excluded_handlers=[".*admin.*", "/metrics"],
    env_var_name="ENABLE_METRICS",
...
```

...

</details>

### poetry-plugin-export

Poetry plugin to export the dependencies to various formats

`pip install poetry-plugin-export` · installs (wheel) · licence: MIT · rank 1023 · last release 2026-09-19 · [PyPI](https://pypi.org/project/poetry-plugin-export/) · [source](https://github.com/python-poetry/poetry-plugin-export)

<details><summary>README extract</summary>

This package is a plugin that allows the export of locked packages to various formats.

Note: For now, only the `constraints.txt` and `requirements.txt` formats are available.

This plugin provides the same features as the existing `export` command of Poetry which it will eventually replace.

Sections: Poetry Plugin: Export, Usage, Available options

</details>

### python-gitlab

The python wrapper for the GitLab REST and GraphQL APIs.

`pip install python-gitlab` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 1051 · last release 2026-09-28 · [PyPI](https://pypi.org/project/python-gitlab/) · [docs](https://python-gitlab.readthedocs.io) · [source](https://github.com/python-gitlab/python-gitlab)

_README extract left out: share-alike licence._

### parameterized

Parameterized testing with any Python test framework

`pip install parameterized` · installs (wheel) · licence: BSD License · rank 1061 · last release 2023-03-27 · [PyPI](https://pypi.org/project/parameterized/)

<details><summary>README extract</summary>

Example:
```python
from parameterized import parameterized, param

# A list of tuples
@parameterized([
    (2, 3, 5),
    (3, 5, 8),
])
def test_add(a, b, expected):
    assert_equal(a + b, expected)

# A list of params
@parameterized([
    param("10", 10),
    param("10", 16, base=16),
])
def test_int(str_val, expected, base=10):
...
```

Sections: Compatibility, Dependencies, Exhaustive Usage Examples, Migrating from `nose-parameterized` to `parameterized`, FAQ

</details>

### pydeequ

PyDeequ - Unit Tests for Data

`pip install pydeequ` · installs (wheel) · licence: Apache Software License · rank 1109 · last release 2026-09-14 · [PyPI](https://pypi.org/project/pydeequ/) · [docs](https://pydeequ.readthedocs.io) · [source](https://github.com/awslabs/python-deequ)

<details><summary>README extract</summary>

PyDeequ is a Python API for Deequ, a library built on top of Apache Spark for defining "unit tests for data", which measure data quality in large datasets. PyDeequ is written to support usage of Deequ in Python.

There are 4 main components of Deequ, and they are:

 - `Profiles` leverages Analyzers to analyze each column of a dataset. ...

Example:
```python
import os

os.environ["SPARK_VERSION"] = "4.1"
```

Sections: PyDeequ, Quickstart, Select your Spark version, Set up a PySpark session, Analyzers, Profile, Constraint Suggestions, Constraint Verification, Row-Level Results, DQDL Rules, Repository, Wrapping up, Setup SDKMAN, Setup Java

</details>

### pydocket

A distributed background task system for Python functions

`pip install pydocket` · installs (wheel) · licence: MIT · rank 1119 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pydocket/) · [docs](https://docket.lol/en/latest/) · [source](https://github.com/chrisguidry/docket)

<details><summary>README extract</summary>

Docket is a distributed background task system for Python functions with a focus
on the scheduling of future work as seamlessly and efficiently as immediate work.

Check out our docs for more details,
examples, and the API
reference.

Features:
⚡️ Snappy one-way background task processing without any bloat

📅 Schedule immediate or future work seamlessly with the same interface

⏭️ Skip problematic tasks or parameters without redeploying

🌊 Purpose-built for Redis streams ...

Example:
```python
from datetime import datetime, timedelta, timezone

from docket import Docket

async def greet(name: str, greeting="Hello") -> None:
    print(f"{greeting}, {name} at {datetime.now()}!")

async with Docket() as docket:
    await docket.add(greet)("Jane")

    now = datetime.now(timezone.utc)
...

</details>

### pytest-playwright

A pytest wrapper with fixtures for Playwright to automate web browsers

`pip install pytest-playwright` · installs (wheel) · licence: Apache Software License · rank 1147 · last release 2026-10-08 · [PyPI](https://pypi.org/project/pytest-playwright/)

<details><summary>README extract</summary>

Write end-to-end tests for your web apps with Playwright and pytest.

- Support for all modern browsers including Chromium, WebKit and Firefox.
- Support for headless and headed execution.
- Built-in fixtures that provide browser primitives to test functions. ...

Sections: Pytest plugin for Playwright, Documentation

</details>

### pysftp

A friendly face on SFTP

`pip install pysftp` · installs from source (sdist only) · licence: BSD License · rank 1148 · last release 2016-07-06 · [PyPI](https://pypi.org/project/pysftp/)

<details><summary>README extract</summary>

A simple interface to SFTP. The module offers high level abstractions and
task based routines to handle your SFTP needs. Checkout the Cook Book, in the
docs, to see what pysftp can do for you.

Example:
```python
import pysftp

with pysftp.Connection('hostname', username='me', password='secret') as sftp:
    with sftp.cd('public'):             # temporarily chdir to public
        sftp.put('/my/local/filename')  # upload file to public/ on remote
        sftp.get('remote_file')         # get a remote file
```

Sections: pysftp, Example

</details>

### pytest-randomly

Pytest plugin to randomly order tests and control random.seed.

`pip install pytest-randomly` · installs (wheel) · licence: MIT · rank 1149 · last release 2026-09-01 · [PyPI](https://pypi.org/project/pytest-randomly/) · [source](https://github.com/pytest-dev/pytest-randomly)

<details><summary>README extract</summary>

Pytest plugin to randomly order tests and control `random.seed`.

Testing a Django project?
Check out my book Speed Up Your Django Tests which covers loads of ways to write faster, more accurate tests.

Features:
All of these features are on by default but can be disabled with flags.

* Randomly shuffles the order of test items. This is done first at the level of
 modules, then at the level of test classes (if you have them), then at the
 order of functions. ...

Sections: pytest-randomly, Features, About, Usage, Avoid reordering some tests, Entry Point, References

</details>

### python-Levenshtein

Python extension for computing string edit distances and similarities.

`pip install python-Levenshtein` · installs (wheel) · licence: GPL-2.0-or-later · rank 1208 · last release 2026-09-12 · [PyPI](https://pypi.org/project/python-Levenshtein/) · [docs](https://rapidfuzz.github.io/Levenshtein/) · [source](https://github.com/rapidfuzz/python-Levenshtein.git)

_README extract left out: share-alike licence._

### python-frontmatter

Parse and manage posts with YAML (or other) frontmatter

`pip install python-frontmatter` · installs (wheel) · licence: MIT · rank 1220 · last release 2026-05-20 · [PyPI](https://pypi.org/project/python-frontmatter/) · [docs](http://python-frontmatter.rtfd.io) · [source](https://github.com/eyeseast/python-frontmatter)

<details><summary>README extract</summary>

Front matter offers a useful way to add arbitrary, structured metadata to text documents, regardless of type.

This is a small package to load and parse files (or just text) with YAML (or JSON, TOML or other) front matter.

Documentation

Example:
```python
>>> import frontmatter
```

Sections: Python Frontmatter, Usage

</details>

### pyxlsb

Excel 2007-2010 Binary Workbook (xlsb) parser

`pip install pyxlsb` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 1274 · last release 2022-10-14 · [PyPI](https://pypi.org/project/pyxlsb/)

_README extract left out: share-alike licence._

### python-calamine

Python binding for Rust's library for reading excel and odf file - calamine

`pip install python-calamine` · installs (wheel) · licence: MIT · rank 1291 · last release 2026-11-03 · [PyPI](https://pypi.org/project/python-calamine/) · [source](https://github.com/dimastbk/python-calamine)

<details><summary>README extract</summary>

Python binding for beautiful Rust's library for reading excel and odf file - calamine.

* calamine
* pyo3
* maturin

Example:
```python
from python_calamine import CalamineWorkbook

workbook = CalamineWorkbook.from_path("file.xlsx")
workbook.sheet_names
# ["Sheet1", "Sheet2"]

workbook.get_sheet_by_name("Sheet1").to_python()
# [
# ["1",  "2",  "3",  "4",  "5",  "6",  "7"],
# ["1",  "2",  "3",  "4",  "5",  "6",  "7"],
# ["1",  "2",  "3",  "4",  "5",  "6",  "7"],
# ]
```

Sections: python-calamine, Is used, Example

</details>

### pytest-json-report

A pytest plugin to report test results as JSON files

`pip install pytest-json-report` · installs (wheel) · licence: MIT · rank 1312 · last release 2022-03-15 · [PyPI](https://pypi.org/project/pytest-json-report/)

<details><summary>README extract</summary>

This pytest plugin creates test reports as JSON. This makes it easy to process test results in other applications.

It can report a summary, test details, captured output, logs, exception tracebacks and more. Additionally, you can use the available fixtures and hooks to add metadata and customize the report as you like.

Example:
```python
{
    "duration": 0.00018835067749023438,
    "outcome": "failed",
    "crash": {
        "path": "/path/to/tests/test_foo.py",
        "lineno": 54,
        "message": "TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'"
    },
    "traceback": [
        {
            "path": "test_foo.py",
            "lineno": 65,
...
```

...

</details>

### pyproject-metadata

PEP 621 metadata parsing

`pip install pyproject-metadata` · installs (wheel) · licence: MIT · rank 1323 · last release 2026-07-04 · [PyPI](https://pypi.org/project/pyproject-metadata/) · [docs](https://pep621.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

[][pre-commit-link]
[][gha-checks-link]
[][gha-tests-link]
[][codecov-link]
[][rtd-link]
[][pypi-link]

> Dataclass for pyproject.toml `[project]` metadata with support for \[core >
> metadata\] generation

This project does not implement the parsing of `pyproject.toml` containing
pyproject.toml `[project]` metadata. ...

Example:
```python
from pyproject_metadata import StandardMetadata

parsed_pyproject = {...}  # you can use parsers like `tomli` to obtain this dict
metadata = StandardMetadata.from_pyproject(parsed_pyproject, allow_extra_keys=False)
# Same fields as defined in pyproject.toml [project] metadata
print(metadata.entrypoints)

pkg_info = metadata.as_rfc822()
...
```

...

</details>

### pickleshare

Tiny 'shelve'-like database with concurrency support

`pip install pickleshare` · installs (wheel) · licence: MIT License · rank 1324 · last release 2018-09-25 · [PyPI](https://pypi.org/project/pickleshare/)

<details><summary>README extract</summary>

PickleShare - a small 'shelve' like datastore with concurrency support

Like shelve, a PickleShareDB object acts like a normal dictionary. Unlike shelve,
many processes can access the database simultaneously. Changing a value in
database is immediately visible to other processes accessing the same database. ...

</details>

### pkgutil_resolve_name

Resolve a name to an object.

`pip install pkgutil_resolve_name` · installs (wheel) · licence: MIT License · rank 1347 · last release 2021-07-21 · [PyPI](https://pypi.org/project/pkgutil_resolve_name/)

<details><summary>README extract</summary>

A backport of Python 3.9's `pkgutil.resolve_name`.
See the Python 3.9 documentation.

</details>

### partial-json-parser

Parse partial JSON generated by LLM

`pip install partial-json-parser` · installs (wheel) · licence: MIT · rank 1358 · last release 2025-11-17 · [PyPI](https://pypi.org/project/partial-json-parser/) · [source](https://github.com/promplate/partial-json-parser)

<details><summary>README extract</summary>

Sometimes we need LLM (Large Language Models) to produce structural information instead of natural language. The easiest way is to use JSON.

But before receiving the last token of response, the JSON is broken, which means you can't use `JSON.parse` to decode it. But we still want to stream the data to the user. ...

Example:
```python
from partial_json_parser import loads

>>> loads('{"key": "v')  # {'key': 'v'}
```

Sections: Partial JSON Parser, Usage, Detailed Usage, Parsing complete / partial JSON strings, Handling malformed JSON, API Reference, loads(json_string, [allow_partial], [parser]), ensure_json(json_string, [allow_partial]), fix(json_string, [allow_partial]), Allow

</details>

### python-crontab

Python Crontab API

`pip install python-crontab` · installs (wheel) · licence: LGPLv3 · rank 1370 · last release 2026-08-29 · [PyPI](https://pypi.org/project/python-crontab/)

_README extract left out: share-alike licence._

### publication

Publication helps you maintain public-api-friendly modules by preventing unintentional access to private implementation details via introspection.

`pip install publication` · installs (wheel) · licence: MIT License · rank 1375 · last release 2019-01-15 · [PyPI](https://pypi.org/project/publication/)

<details><summary>README extract</summary>

Setting expectations around what APIs you can rely on in a Python
library is very difficult.

Publication makes it easy.

As Hyrum's Law somewhat grimly states,

 | With a sufficient number of users of an API,
 | it does not matter what you promise in the contract:
 | all observable behaviors of your system
 | will be depended on by somebody. ...

Example:
```python
# sprocket_zorfer.py
from sprocket import sprocket_with_name
from zorf import zorfable_thing

def zorf_sprocket_internal(sprocket, zorfulations):
    ...
def compute_zorfulations():
    ...

def zorf_sprocket_named(sprocket_name, how_much):
    sprocket = sprocket_with_name(sprocket_name)
    zorfulations = compute_zorfulations(how_much)
...
```

...

</details>

### pep517

Wrappers to build Python packages using PEP 517 hooks

`pip install pep517` · installs (wheel) · licence: MIT License · rank 1421 · last release 2023-11-08 · [PyPI](https://pypi.org/project/pep517/)

<details><summary>README extract</summary>

PEP 517 specifies a standard
API for systems which build Python packages.

PEP 660 extends it with a build
mode that leads to editable installs.

This package contains wrappers around the hooks specified by PEP 517 and
PEP 660. It provides:

- A mechanism to call the hooks in a subprocess, so they are isolated from
 the current process. ...

Example:
```python
import os
import tomli
from pep517.wrappers import Pep517HookCaller

src = 'path/to/source'  # Folder containing 'pyproject.toml'
with open(os.path.join(src, 'pyproject.toml'), 'rb') as f:
    build_sys = tomli.load(f)['build-system']

print(build_sys['requires'])  # List of static requirements
...
```

Sections: API to call PEP 517 hooks, Deprecated high-level

</details>

### priority

A pure-Python implementation of the HTTP/2 priority tree

`pip install priority` · installs (wheel) · licence: MIT License · rank 1424 · last release 2021-06-27 · [PyPI](https://pypi.org/project/priority/) · [docs](https://python-hyper.org/projects/priority/) · [source](https://github.com/python-hyper/priority/)

<details><summary>README extract</summary>

Priority is a pure-Python implementation of the priority logic for HTTP/2, set
out in RFC 7540 Section 5.3 (Stream Priority). This logic allows for clients
to express a preference for how the server allocates its (limited) resources to
the many outstanding HTTP requests that may be running over a single HTTP/2
connection. ...

Example:
```python
>>> p = priority.PriorityTree()
>>> p.insert_stream(stream_id=1)
>>> p.insert_stream(stream_id=3)
>>> p.insert_stream(stream_id=5, depends_on=1)
>>> p.insert_stream(stream_id=7, weight=32)
>>> p.insert_stream(stream_id=9, depends_on=7, weight=8)
>>> p.insert_stream(stream_id=11, depends_on=7, exclusive=True)
```

Sections: Priority: A HTTP/2 Priority Implementation, Using Priority, Iterating The Tree, Updating The Tree, Removing Streams

</details>

### pywin32-ctypes

A (partial) reimplementation of pywin32 using ctypes/cffi

`pip install pywin32-ctypes` · installs (wheel) · licence: BSD-3-Clause · rank 1429 · last release 2024-08-14 · [PyPI](https://pypi.org/project/pywin32-ctypes/)

<details><summary>README extract</summary>

A reimplementation of pywin32 that is pure python. The default
behaviour will try to use cffi (>= 1.3.0), if available, and fall back
to using ctypes. Please note that there is no need to have a compiler
available on installation or at runtime.

Example:
```python
# Equivalent to 'import win32api' from pywin32.
from win32ctypes.pywin32 import win32api

win32api.LoadLibraryEx(sys.executable, 0, win32api.LOAD_LIBRARY_AS_DATAFILE)
```

Sections: Usage, Version 0.2.3, Version 0.2.2, Version 0.2.1, Version 0.2.0, Version 0.1.2, Version 0.1.1, Version 0.1.0, Version 0.0.1

</details>

### python3-saml

Saml Python Toolkit. Add SAML support to your Python software using this library

`pip install python3-saml` · installs (wheel) · licence: MIT · rank 1516 · last release 2023-10-09 · [PyPI](https://pypi.org/project/python3-saml/)

### pastel

Bring colors to your terminal.

`pip install pastel` · installs (wheel) · licence: MIT License · rank 1529 · last release 2020-09-16 · [PyPI](https://pypi.org/project/pastel/) · [source](https://github.com/sdispater/pastel)

<details><summary>README extract</summary>

Pastel is a simple library to help you colorize strings in your terminal.

It comes bundled with predefined styles:

* `info`: green
* `comment`: yellow
* `question`: black on cyan
* `error`: white on red

Features:
* Use predefined styles or add you own.
* Disable colors all together by calling `with_colors(False)`.
* Automatically disables colors if the output is not a TTY.
* Used in cleo.
* Supports Python 2.7+, 3.5+ and PyPy.

Example:
```python
>>> import pastel
>>> print(pastel.colorize('<info>Information</info>'))
'Information'  # Green string by default
>>> print(pastel.colorize('<fg=red;options=bold>This is bold red</>'))
'This is bold red'
```

Sections: Pastel: Bring colors to your terminal, Features, Usage

</details>

### pipenv

Python Development Workflow for Humans.

`pip install pipenv` · installs (wheel) · licence: MIT License · rank 1531 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pipenv/) · [docs](https://pipenv.pypa.io/en/latest/) · [source](https://github.com/pypa/pipenv.git)

<details><summary>README extract</summary>

Sections: Basic Concepts, Shell Completion, Locate the project, Locate the virtualenv, Locate the Python interpreter, Show a dependency graph, Generate a lockfile, Use the shell, PURPOSE AND ADVANTAGES OF PIPENV

</details>

### pulumi

Pulumi's Python SDK

`pip install pulumi` · installs (wheel) · licence: Apache-2.0 · rank 1541 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pulumi/) · [docs](https://www.pulumi.com) · [source](https://github.com/pulumi/pulumi)

<details><summary>README extract</summary>

The Pulumi Python SDK (pulumi) is the core package used when writing Pulumi programs in Python. It contains everything that you’ll need in order to interact with Pulumi resource providers and express infrastructure using Python code. ...

Sections: Pulumi Python SDK, Getting Started, Pulumi Programming Model, The Pulumi Python Resource Model

</details>

### py-rust-stemmers

Fast and parallel snowball stemmer

`pip install py-rust-stemmers` · installs (wheel) · licence: not stated · rank 1568 · last release 2026-05-22 · [PyPI](https://pypi.org/project/py-rust-stemmers/)

<details><summary>README extract</summary>

py-rust-stemmers is a high-performance Python wrapper around the rust-stemmers library, utilizing the Snowball stemming algorithm. This library allows for efficient stemming of words with support for parallel processing, making it a powerful tool for text processing tasks. ...

Features:
* Snowball Stemmer: Uses the well-known Snowball stemming algorithms for efficient word stemming in multiple languages.
* Parallelism Support: Offers parallel processing for batch stemming, providing significant speedup for larger text sequences. ...

Example:
```python
s.stem_word("running")  # Output: "run"
```

Sections: py-rust-stemmers, Features, Initialize the stemmer for the English language, Input text, Example usage of the methods, Stem a list of words, Stem words in parallel, Build from source

</details>

### protobuf-py-ext

Native extension for protobuf-py

`pip install protobuf-py-ext` · installs (wheel) · licence: Apache-2.0 · rank 1601 · last release 2026-10-22 · [PyPI](https://pypi.org/project/protobuf-py-ext/) · [docs](https://protobufpy.com/) · [source](https://github.com/bufbuild/protobuf-py)

### parver

Parse and manipulate version numbers.

`pip install parver` · installs (wheel) · licence: MIT · rank 1625 · last release 2026-07-30 · [PyPI](https://pypi.org/project/parver/) · [docs](https://parver.readthedocs.io) · [source](https://github.com/RazerM/parver)

<details><summary>README extract</summary>

parver allows parsing and manipulation of PEP 440 version numbers.

Example:
```python
>>> Version.parse('1.3').bump_dev()

>>> v = Version.parse('v1.2.alpha-3')
>>> v.is_alpha
True
>>> v.pre
3
>>> v

>>> v.normalize()
```

Sections: parver, Example

</details>

### pyiceberg-core

(no summary)

`pip install pyiceberg-core` · installs (wheel) · licence: Apache Software License · rank 1696 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyiceberg-core/)

<details><summary>README extract</summary>

<!--
 ~ Licensed to the Apache Software Foundation (ASF) under one
 ~ or more contributor license agreements. See the NOTICE file
 ~ distributed with this work for additional information
 ~ regarding copyright ownership. ...

</details>

### presidio-analyzer

Presidio Analyzer package

`pip install presidio-analyzer` · installs (wheel) · licence: MIT · rank 1742 · last release 2026-10-27 · [PyPI](https://pypi.org/project/presidio-analyzer/)

<details><summary>README extract</summary>

The Presidio analyzer is a Python based service for detecting PII entities in text.

During analysis, it runs a set of different _PII Recognizers,
each one in charge of detecting one or more PII entities using different mechanisms. ...

Example:
```python
from presidio_analyzer.predefined_recognizers import BasicLangExtractRecognizer
recognizer = BasicLangExtractRecognizer()  # Uses default config
```

Sections: Presidio analyzer, Description, Language Model-based PII/PHI Detection, Quick Usage, Deploy Presidio analyzer to Azure, Simple usage example, GPU Acceleration, Documentation

</details>

### proglog

Log and progress bar manager for console, notebooks, web...

`pip install proglog` · installs (wheel) · licence: MIT · rank 1749 · last release 2025-05-09 · [PyPI](https://pypi.org/project/proglog/)

<details><summary>README extract</summary>

Proglog is a progress logging system for Python. It allows to build complex
libraries while giving the user control on the management of logs, callbacks and progress bars.

PIP installation:

Github Page: <

License: MIT

Copyright 2017 Edinburgh Genome Foundry, University of Edinburgh

Sections: Proglog, Infos

</details>

### pipdeptree

Command line utility to show dependency tree of packages.

`pip install pipdeptree` · installs (wheel) · licence: MIT · rank 1769 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pipdeptree/) · [docs](https://pipdeptree.readthedocs.io) · [source](https://github.com/tox-dev/pipdeptree)

<details><summary>README extract</summary>

pipdeptree displays installed Python packages as a dependency tree.
`pip freeze` shows a flat list; `pipdeptree` adds parent-child
relationships and reports dependency conflicts or cycles.

Sections: pipdeptree, Quick start

</details>

### pytest-dotenv

A py.test plugin that parses environment files before running tests

`pip install pytest-dotenv` · installs (wheel) · licence: MIT License · rank 1770 · last release 2020-06-16 · [PyPI](https://pypi.org/project/pytest-dotenv/)

<details><summary>README extract</summary>

This little plugin uses `python-dotenv` to load any environment variables from a `.env` file. Extra configuration can be defined in any `pytest` config files, such as `pytest.ini`, `tox.ini` and so on.

Sections: pytest-dotenv, Basic Usage, Non-default configuration, Custom Environment Variable Files, Overriding Existing Values, Alternative: Specify the file at the command line

</details>

### pyhumps

🐫 Convert strings (and dictionary keys) between snake case, camel case and pascal case in Python. Inspired by Humps for Node

`pip install pyhumps` · installs (wheel) · licence: MIT License · rank 1802 · last release 2022-10-21 · [PyPI](https://pypi.org/project/pyhumps/)

<details><summary>README extract</summary>

Convert strings (and dictionary keys) between snake case, camel case and pascal case in Python. Inspired by Humps for Node.

Example:
```python
import humps

humps.camelize("jack_in_the_box")  # jackInTheBox
humps.decamelize("rubyTuesdays")  # ruby_tuesdays
humps.pascalize("red_robin")  # RedRobin
humps.kebabize("white_castle")  # white-castle
```

Sections: Usage, Converting strings, Converting dictionary keys, Checking character casing, Cookbook, Pythonic Boto3 API Wrapper

</details>

### python-tds

Python DBAPI driver for MSSQL using pure Python TDS (Tabular Data Stream) protocol implementation

`pip install python-tds` · installs (wheel) · licence: MIT · rank 1815 · last release 2025-09-13 · [PyPI](https://pypi.org/project/python-tds/)

### pulumi-aws

A Pulumi package for creating and managing Amazon Web Services (AWS) cloud resources.

`pip install pulumi-aws` · installs (wheel) · licence: Apache-2.0 · rank 1863 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pulumi-aws/) · [source](https://github.com/pulumi/pulumi-aws)

<details><summary>README extract</summary>

The Amazon Web Services (AWS) resource provider for Pulumi lets you use AWS resources in your cloud programs. To use
this package, install the Pulumi CLI. For a streamlined Pulumi walkthrough, including language runtime installation and AWS configuration, select "Get Started" below.

Sections: Amazon Web Services (AWS) provider, Node.js (Java/TypeScript), Python, Go, .NET, Concepts, Serverless Functions, Configuration, Reference, Pulumi roadmap

</details>

### polyleven

A fast C-implemented library for Levenshtein distance

`pip install polyleven` · installs (wheel) · licence: not stated · rank 1882 · last release 2026-10-15 · [PyPI](https://pypi.org/project/polyleven/) · [source](https://github.com/fujimotos/polyleven)

<details><summary>README extract</summary>

:License: MIT License

polyleven is a Pythonic Levenshtein distance library that:

- Is fast regardless of input types, and hence can be applied to
 both short (like English words) and long inputs (like DNA sequences).

- Is stand-alone with no external dependencies. ...

Sections: Polyleven -- Fast Pythonic Levenshtein Library, 1. Introduction, 3. How to use, 4. Benchmark, 4.1 English Words, 4.2. Longer Inputs, 4.3. List of Libraries

</details>

### pyarrow-stubs

Type annotations for pyarrow

`pip install pyarrow-stubs` · installs (wheel) · licence: BSD-2-Clause · rank 1898 · last release 2026-08-19 · [PyPI](https://pypi.org/project/pyarrow-stubs/) · [source](https://github.com/zen-xu/pyarrow-stubs.git)

### python-on-whales

A Docker client for Python, designed to be fun and intuitive!

`pip install python-on-whales` · installs (wheel) · licence: not stated · rank 1935 · last release 2026-03-09 · [PyPI](https://pypi.org/project/python-on-whales/) · [docs](https://gabrieldemarmiesse.github.io/python-on-whales/) · [source](https://github.com/gabrieldemarmiesse/python-on-whales)

<details><summary>README extract</summary>

A Docker client for Python, designed to be fun and intuitive!

Works on Linux, macOS and Windows, for Python 3.8 and above.

* Documentation
* Github repository

Features:
In a sense this project is built on top of Docker-py
because the implementation, the organisation and the API is inspired from the project, but the codebases
could not be the same.

Two major differences do not permit that: ...

Example:
```python
from python_on_whales import docker
```

Sections: Some cool examples, Some more `docker.run()` advanced examples with postgres, Main features, Why another project? Why not build on Docker-py?, Should I use Docker-py or Python on Whales?, Alternatives to Docker: Podman, nerdctl...

</details>

### policy-sentry

Generate locked-down AWS IAM Policies

`pip install policy-sentry` · installs (wheel) · licence: MIT · rank 1947 · last release 2026-04-14 · [PyPI](https://pypi.org/project/policy-sentry/) · [docs](https://policy-sentry.readthedocs.io/) · [source](https://github.com/salesforce/policy_sentry/)

<details><summary>README extract</summary>

IAM Least Privilege Policy Generator.

- Tutorial
 * Installation
 + Package managers
 + Shell completion
 * Step 1: Create the Template
 * Step 2: Copy/paste ARNs
 * Step 3: Write-policy command
- Cheat sheets
 * Policy Writing cheat sheet
 * IAM Database Query Cheat Sheet
 * Local Initialization (Optional) ...

Features:
Writing security-conscious IAM Policies by hand can be very tedious and inefficient. Many Infrastructure as Code developers have experienced something like this: ...

Example:
```python
from policy_sentry.querying.actions import get_actions_for_service

def example():
    actions = get_actions_for_service('cloud9')  # Then you can leverage any method that requires access to the database.
    for action in actions:
        print(action)

if name == 'main':
    example()
...

</details>

### pycep-parser

A Python based Bicep parser

`pip install pycep-parser` · installs (wheel) · licence: Apache-2.0 · rank 1966 · last release 2026-08-09 · [PyPI](https://pypi.org/project/pycep-parser/) · [source](https://github.com/gruebel/pycep)

<details><summary>README extract</summary>

A parser for Azure Bicep files leveraging Lark.

Sections: pycep, Getting Started, Requirements, Current capabilities, Next milestones, Custom data types, Functions, Operators, Considering, Out-of-scope

</details>

### pydocstyle

Python docstring style checker

`pip install pydocstyle` · installs (wheel) · licence: MIT License · rank 2073 · last release 2023-01-17 · [PyPI](https://pypi.org/project/pydocstyle/) · [docs](https://www.pydocstyle.org/en/stable/) · [source](https://github.com/PyCQA/pydocstyle)

<details><summary>README extract</summary>

pydocstyle is a static analysis tool for checking compliance with Python
docstring conventions.

pydocstyle supports most of
PEP 257 out of the box, but it
should not be considered a reference implementation.

pydocstyle supports Python 3.6+.

Sections: pydocstyle - docstring style checker, Quick Start, Run, Links

</details>

### prophet

Automatic Forecasting Procedure

`pip install prophet` · installs (wheel) · licence: MIT · rank 2090 · last release 2026-10-05 · [PyPI](https://pypi.org/project/prophet/) · [docs](https://facebook.github.io/prophet/) · [source](https://github.com/facebook/prophet)

<details><summary>README extract</summary>

Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. ...

Example:
```python
>>> from prophet import Prophet
>>> m = Prophet()
>>> m.fit(df)  # df is a pandas.DataFrame with 'y' and 'ds' columns
>>> future = m.make_future_dataframe(periods=365)
>>> m.predict(future)
```

Sections: Prophet: Automatic Forecasting Procedure, Important links, Other forecasting packages, Example usage

</details>

### python-rapidjson

Python wrapper around rapidjson

`pip install python-rapidjson` · installs (wheel) · licence: MIT License · rank 2100 · last release 2026-11-01 · [PyPI](https://pypi.org/project/python-rapidjson/)

<details><summary>README extract</summary>

:Authors: Ken Robbins <ken@kenrobbins.com>; Lele Gaifax <lele@metapensiero.it>
:License: MIT License
:Status:


RapidJSON is an extremely fast C++ JSON parser and serialization library: this module
wraps it into a Python 3 extension, exposing its serialization/deserialization (to/from
either `bytes`, `str` or *file-like* instances) and JSON Schema ...

Example:
```python
>>> import rapidjson
>>> data = {'foo': 100, 'bar': 'baz'}
>>> rapidjson.dumps(data)
'{"foo":100,"bar":"baz"}'
>>> rapidjson.loads('{"bar":"baz","foo":100}')
{'bar': 'baz', 'foo': 100}
>>>
>>> class Stream:
...   def write(self, data):
...      print("Chunk:", data)
...
>>> rapidjson.dump(data, Stream(), chunk_size=5)
Chunk: b'{"foo'
...
```

...

</details>

### py-key-value-shared

Shared Key-Value

`pip install py-key-value-shared` · installs (wheel) · licence: Apache Software License · rank 2119 · last release 2025-11-17 · [PyPI](https://pypi.org/project/py-key-value-shared/)

<details><summary>README extract</summary>

Shared code between key-value-aio and key-value-sync

</details>

### pipx

Install and Run Python Applications in Isolated Environments

`pip install pipx` · installs (wheel) · licence: MIT · rank 2120 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pipx/) · [docs](https://pipx.pypa.io) · [source](https://github.com/pypa/pipx)

<details><summary>README extract</summary>

Features:
pipx installs and runs end-user applications written in Python. It's roughly similar to macOS's brew,
JavaScript's npx, and Linux's
apt.

It's closely related to pip. ...

Sections: Overview: What is `pipx`?, Features, On macOS, On Linux, On Windows, Quick Start

</details>

### pycomposefile

Structured deserialization of Docker Compose files.

`pip install pycomposefile` · installs (wheel) · licence: MIT · rank 2123 · last release 2025-07-29 · [PyPI](https://pypi.org/project/pycomposefile/)

### portkey-ai

Python client library for the Portkey API

`pip install portkey-ai` · installs (wheel) · licence: MIT License · rank 2166 · last release 2026-07-23 · [PyPI](https://pypi.org/project/portkey-ai/)

<details><summary>README extract</summary>

Features:
The Portkey SDK is built on top of the OpenAI SDK, allowing you to seamlessly integrate Portkey's advanced features while retaining full compatibility with OpenAI methods. ...

Example:
```python
import asyncio
from portkey_ai import AsyncPortkey

portkey = AsyncPortkey(
    api_key="PORTKEY_API_KEY",
    virtual_key="VIRTUAL_KEY"
)

async def main():
    chat_completion = await portkey.chat.completions.create(
        messages=[{'role': 'user', 'content': 'Say this is a test'}],
        model='gpt-4'
    )

    print(chat_completion)

...
```

...

</details>

### PyMatting

Python package for alpha matting.

`pip install PyMatting` · installs (wheel) · licence: MIT License · rank 2167 · last release 2026-09-08 · [PyPI](https://pypi.org/project/PyMatting/) · [source](https://github.com/pymatting/pymatting)

<details><summary>README extract</summary>

We introduce the PyMatting package for Python, which implements various methods to solve the alpha matting problem.

Given an input image and a hand-drawn trimap (top row), alpha matting estimates the alpha channel of a foreground object which can then be composed onto a different background (bottom row).

PyMatting provides: ...

Example:
```python
# First import will take a minute due to compilation
from pymatting import cutout

cutout(
    # input image path
    "data/lemur/lemur.png",
    # input trimap path
    "data/lemur/lemur_trimap.png",
    # output cutout path
    "lemur_cutout.png")
```

...

</details>

### pycocotools

Official APIs for the MS-COCO dataset

`pip install pycocotools` · installs (wheel) · licence: FreeBSD · rank 2245 · last release 2025-12-15 · [PyPI](https://pypi.org/project/pycocotools/)

<details><summary>README extract</summary>

This is a fork of the original cocoapi, with bug fixes and packaging improvements.

This is also the "official" source of the pypi package `pycocotools`, available for download at pypi. ...

</details>

### prime-pydantic-config

Pydantic-driven CLI with TOML/YAML config file support for ML

`pip install prime-pydantic-config` · installs (wheel) · licence: not stated · rank 2258 · last release 2026-08-18 · [PyPI](https://pypi.org/project/prime-pydantic-config/) · [source](https://github.com/PrimeIntellect-ai/pydantic-config)

<details><summary>README extract</summary>

A Pydantic-driven CLI with TOML / YAML / JSON config file support.

Features:
Every example below uses `examples/train.py`, a dummy
training config that exercises the patterns common in `prime-rl`-style
training scripts.

Example:
```python
from pydantic_config import cli, BaseConfig

class Config(BaseConfig):
    lr: float = 1e-4
    batch_size: int = 32

config = cli(Config)
```

Sections: Pydantic Config, Features, Help output, Config files via `@`, Required fields, Nested config groups, Bool flags and `--no-` negation, Lists, Dicts, Optional sub-configs, Disabling an optional sub-config, Discriminated unions, Validation aliases, Single-dash short flags

</details>

### pinecone-plugin-interface

Plugin interface for the Pinecone python client

`pip install pinecone-plugin-interface` · installs (wheel) · licence: Apache Software License · rank 2262 · last release 2024-06-05 · [PyPI](https://pypi.org/project/pinecone-plugin-interface/) · [docs](https://pinecone.io/docs) · [source](https://github.com/pinecone-io/python-plugin-interface)

<details><summary>README extract</summary>

This small package is used to distribute a few classes and utilities used to build and consume plugins for the Pinecone Python SDK.

At present this package is experimental and intended for internal use by Pinecone engineers iterating on new features. It should not be used by end-users or partners.

</details>

### pymilvus

Python SDK for Milvus

`pip install pymilvus` · installs (wheel) · licence: Apache Software License · rank 2267 · last release 2026-09-18 · [PyPI](https://pypi.org/project/pymilvus/) · [source](https://github.com/milvus-io/pymilvus)

<details><summary>README extract</summary>

Python SDK for Milvus. To contribute code to this project, please read our contribution guidelines first. If you have some ideas or encounter a problem, you can find us in the Slack channel #py-milvus.

The following collection shows Milvus versions and recommended PyMilvus versions:

|Milvus version| Recommended PyMilvus version | ...

Sections: Milvus Python SDK, Compatibility, FAQ, Documentation

</details>

### prison

Rison encoder/decoder

`pip install prison` · installs (wheel) · licence: MIT License · rank 2275 · last release 2021-08-26 · [PyPI](https://pypi.org/project/prison/)

### procrastinate

Postgres-based distributed task processing library

`pip install procrastinate` · installs (wheel) · licence: MIT License · rank 2284 · last release 2026-09-23 · [PyPI](https://pypi.org/project/procrastinate/) · [docs](https://procrastinate.readthedocs.io/) · [source](https://github.com/procrastinate-org/procrastinate/)

<details><summary>README extract</summary>

Procrastinate is looking for additional maintainers!

Procrastinate is an open-source Python 3.10+ distributed task processing
library, leveraging PostgreSQL 13+ to store task definitions, manage locks and
dispatch tasks. It can be used within both sync and async code,
has [Django] integration, and is easy to use with ASGI frameworks. ...

Example:
```python
# mycode.py
import procrastinate

# Make an app in your code
app = procrastinate.App(connector=procrastinate.SyncPsycopgConnector())

# Then define tasks
@app.task(queue="sums")
def sum(a, b):
    with open("myfile", "w") as f:
        f.write(str(a + b))

with app.open():
    # Launch a job
    sum.defer(a=3, b=5)

...
```

Sections: Procrastinate: PostgreSQL-based Task Queue for Python, Where to go from here

</details>

### pydantic-monty-runtime

The monty CLI binary — spawned as worker subprocesses by pydantic-monty

`pip install pydantic-monty-runtime` · installs (wheel) · licence: MIT License · rank 2297 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pydantic-monty-runtime/) · [source](https://github.com/pydantic/monty)

<details><summary>README extract</summary>

The `monty` command-line binary for the
Monty sandbox.

Installing the wheel puts the compiled binary in the environment's scripts directory.

You normally don't install this directly — the
`pydantic-monty` metapackage pulls
it in alongside the Python bindings, which need it to spawn worker
subprocesses. ...

Sections: pydantic-monty-runtime, Usage, Worker mode

</details>

### presidio-anonymizer

Presidio Anonymizer package - replaces analyzed text with desired values.

`pip install presidio-anonymizer` · installs (wheel) · licence: MIT · rank 2302 · last release 2026-10-27 · [PyPI](https://pypi.org/project/presidio-anonymizer/)

<details><summary>README extract</summary>

The Presidio anonymizer is a Python based module for anonymizing detected PII text
entities with desired values.

Use the following button to deploy presidio anonymizer to your Azure subscription.

The Presidio-Anonymizer package contains both Anonymizers and Deanonymizers. ...

Example:
```python
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

# Initialize the engine with logger.
engine = AnonymizerEngine()

# Invoke the anonymize function with the text,
# analyzer results (potentially coming from presidio-analyzer) and
# Operators to get the anonymization output:
...
```

...

</details>

### pyglet

pyglet is a cross-platform games and multimedia package.

`pip install pyglet` · installs (wheel) · licence: not stated · rank 2337 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pyglet/)

<details><summary>README extract</summary>

*pyglet* is a cross-platform windowing and multimedia library for Python, intended for developing games
and other visually rich applications. It supports Windowing, input event handling, Controllers & Joysticks,
OpenGL graphics, loading images and videos, and playing sounds and music. *pyglet* works on Windows, OS X and Linux. ...

Sections: pyglet, Requirements, Building Docs, Contact

</details>

### pulumi-command

The Pulumi Command Provider enables you to execute commands and scripts either locally or remotely as part of the Pulumi resource model.

`pip install pulumi-command` · installs (wheel) · licence: Apache-2.0 · rank 2347 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pulumi-command/) · [source](https://github.com/pulumi/pulumi-command)

<details><summary>README extract</summary>

The Pulumi Command Provider enables you to execute commands and scripts either locally or remotely as part of the Pulumi resource model. Resources in the command package support running scripts on `create` and `destroy` operations, supporting stateful local and remote command execution. ...

Sections: Pulumi Command Provider, Examples, A simple local resource (random), Remote provisioning of an EC2 instance, Invoking a Lambda during Pulumi deployment, Using `local.Command `with CURL to manage external REST API, Graceful cleanup of workloads in a Kubernetes cluster, Working with Assets and Paths, Asset Paths Example, Building, Dependencies, Building locally, Running an example

</details>

### playwright-stealth

Make your playwright instance stealthy

`pip install playwright-stealth` · installs (wheel) · licence: MIT · rank 2360 · last release 2026-04-04 · [PyPI](https://pypi.org/project/playwright-stealth/)

<details><summary>README extract</summary>

Fork of AtuboDad's port
of puppeteer-extra-plugin-stealth,
with some improvements. Don't expect this to bypass anything but the simplest of bot detection methods. Consider this a
proof-of-concept starting point.

I've merged some of the outstanding PRs, added some features, and cleaned up the API surface. See
the changelog. ...

Example:
```python
import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

async def main():
    # This is the recommended usage. All pages created will have stealth applied:
    async with Stealth().use_async(async_playwright()) as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
...
```

...

</details>

### psygnal

Fast python callback/event system modeled after Qt Signals

`pip install psygnal` · installs (wheel) · licence: BSD License · rank 2361 · last release 2026-09-11 · [PyPI](https://pypi.org/project/psygnal/) · [docs](https://psygnal.readthedocs.io) · [source](https://github.com/pyapp-kit/psygnal)

<details><summary>README extract</summary>

Psygnal (pronounced "signal") is a pure python implementation of the observer
pattern, with the API of
Qt-style Signals with (optional)
signature and type checking, and support for threading. It has no dependencies.

> This library does *not* require or use Qt in any way, It simply implements
> a similar observer pattern API.

Example:
```python
from psygnal import Signal

class MyObject:
    # define one or more signals as class attributes
    value_changed = Signal(str)

# create an instance
my_obj = MyObject()

# You (or others) can connect callbacks to your signals
@my_obj.value_changed.connect
def on_change(new_value: str):
    print(f"The value changed to {new_value}!")

...
```

...

</details>

### pycrdt

Python bindings for Yrs

`pip install pycrdt` · installs (wheel) · licence: MIT License · rank 2396 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pycrdt/)

<details><summary>README extract</summary>

CRDTs based on Yrs.

Documentation is available here.

</details>

### puccinialin

Install rust into a temporary directory for boostrapping a rust-based build backend

`pip install puccinialin` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 2411 · last release 2026-07-21 · [PyPI](https://pypi.org/project/puccinialin/) · [source](https://github.com/konstin/puccinialin)

<details><summary>README extract</summary>

Install rust into a temporary directory to support rust-based builds.

Cargo and rustc are installed into a cache directory, to avoid modifying the host's environment, and activated using a
set of environment variables. ...

Example:
```python
import os
from subprocess import check_call

from puccinialin import setup_rust

extra_env = setup_rust("path/to/installation/dir")
check_call(["cargo", "build"], env={os.environ, extra_env})
```

Sections: puccinialin, Usage: Python, Usage: CLI, Implementation

</details>

### pycairo

Python interface for cairo

`pip install pycairo` · installs from source (sdist only) · licence: LGPL-2.1-only OR MPL-1.1 · rank 2438 · last release 2026-10-04 · [PyPI](https://pypi.org/project/pycairo/) · [source](https://github.com/pygobject/pycairo)

_README extract left out: share-alike licence._

### pulumi-tls

A Pulumi package to create TLS resources in Pulumi programs.

`pip install pulumi-tls` · installs (wheel) · licence: Apache-2.0 · rank 2449 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pulumi-tls/) · [source](https://github.com/pulumi/pulumi-tls)

<details><summary>README extract</summary>

The TLS resource provider for Pulumi lets you create TLS keys and certificates in your cloud programs. To use
this package, please install the Pulumi CLI first.

Sections: TLS Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Concepts, Reference

</details>

### pynamodb

A Pythonic Interface to DynamoDB

`pip install pynamodb` · installs (wheel) · licence: MIT License · rank 2455 · last release 2025-06-02 · [PyPI](https://pypi.org/project/pynamodb/) · [source](https://github.com/pynamodb/PynamoDB)

<details><summary>README extract</summary>

A Pythonic interface for Amazon's DynamoDB.

DynamoDB is a great NoSQL service provided by Amazon, but the API is verbose.
PynamoDB presents you with a simple, elegant API.

Useful links:

* See the full documentation at
* Ask questions in the GitHub issues
* See release notes at

Features:
* Python >= 3.7 support
* An ORM-like interface with query and scan filters
* Compatible with DynamoDB Local
* Supports the entire DynamoDB API
* Support for Unicode, Binary, JSON, Number, Set, and UTC Datetime attributes
* Support for Global and ...

Example:
```python
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class UserModel(Model):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = "dynamodb-user"
    email = UnicodeAttribute(null=True)
...

</details>

### pyod

A Python library for anomaly detection across tabular, time series, graph, text, image, and audio data. 61 detectors, benchmark-backed ADEngine orchestration, and an agentic workflow for AI agents.

`pip install pyod` · installs (wheel) · licence: BSD-2-Clause · rank 2483 · last release 2026-10-12 · [PyPI](https://pypi.org/project/pyod/) · [docs](https://pyod.readthedocs.io) · [source](https://github.com/yzhao062/pyod)

<details><summary>README extract</summary>

PyOD 3: Agentic Anomaly Detection At Scale

 PyOD is agent-ready. Claude Code and Codex can use the `od-expert` skill to drive ADEngine investigations, while MCP-compatible agents can query PyOD's detector knowledge and planning tools. The classic `fit`/`predict` API stays unchanged. ...

Example:
```python
Zhao, Y., Nasrullah, Z. and Li, Z., 2019. PyOD: A Python Toolbox for Scalable Outlier Detection. Journal of machine learning research (JMLR), 20(96), pp.1-7.
```

Sections: Python Outlier Detection (PyOD) 3, About PyOD, API Cheatsheet & Reference, Benchmarks, Additional Topics, Implemented Algorithms, Quick Start for Outlier Detection, . See a sample output & visualization., Reference

</details>

### pdpyras

PagerDuty Python REST API Sessions.

`pip install pdpyras` · installs (wheel) · licence: MIT · rank 2484 · last release 2025-06-03 · [PyPI](https://pypi.org/project/pdpyras/)

<details><summary>README extract</summary>

A basic REST API client for PagerDuty based on Requests' Session class

</details>

### pystac

Python library for working with the SpatioTemporal Asset Catalog (STAC) specification

`pip install pystac` · installs (wheel) · licence: Apache Software License · rank 2512 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC is a library for working with the SpatioTemporal Asset Catalog specification in Python 3.

Sections: PySTAC, Versioning, Documentation, Running the quickstart and tutorials

</details>

### portpicker

A library to choose unique available network ports.

`pip install portpicker` · installs (wheel) · licence: Apache Software License · rank 2543 · last release 2023-08-15 · [PyPI](https://pypi.org/project/portpicker/)

<details><summary>README extract</summary>

Portpicker provides an API to find and return an available
network port for an application to bind to. Ideally suited for use from
unittests or for test harnesses that launch local servers. ...

</details>

### py-ecc

py-ecc: Elliptic curve crypto in python including secp256k1, alt_bn128, and bls12_381

`pip install py-ecc` · installs (wheel) · licence: MIT License · rank 2556 · last release 2025-04-14 · [PyPI](https://pypi.org/project/py-ecc/)

<details><summary>README extract</summary>

Elliptic curve crypto in python including secp256k1, alt_bn128, and bls12_381.

> Warning: This library contains some experimental code and has NOT been audited.

Read the documentation.

View the change log.

</details>

### pykwalify

Python lib/cli for JSON/YAML schema validation

`pip install pykwalify` · installs (wheel) · licence: MIT License · rank 2597 · last release 2020-12-30 · [PyPI](https://pypi.org/project/pykwalify/)

<details><summary>README extract</summary>

YAML/JSON validation library

This framework is a port with a lot of added functionality of the Java version of the framework kwalify that can be found at

The original source code can be found at ...

Sections: pyKwalify, Usage, Examples, YAML parser, UTF-8 and data encoding, Project details

</details>

### pycron

Simple cron-like parser, which determines if current datetime matches conditions.

`pip install pycron` · installs (wheel) · licence: MIT · rank 2622 · last release 2026-09-17 · [PyPI](https://pypi.org/project/pycron/) · [source](https://github.com/kipe/pycron)

<details><summary>README extract</summary>

Simple cron-like parser for Python, which determines if current datetime matches conditions.

Example:
```python
import pycron
pycron.is_now('*/5 * * * *')  # True every 5 minutes
pycron.is_now('0 * * * *')    # True every hour, on minute 0
```

Sections: pycron, Usage, Help, Notes

</details>

### PyAutoGUI

PyAutoGUI lets Python control the mouse and keyboard, and other GUI automation tasks. For Windows, macOS, and Linux, on Python 3 and 2.

`pip install PyAutoGUI` · installs from source (sdist only) · licence: BSD License · rank 2657 · last release 2023-05-24 · [PyPI](https://pypi.org/project/PyAutoGUI/)

<details><summary>README extract</summary>

PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.

`pip install pyautogui`

Full documentation available at

Simplified Chinese documentation available at

Source code available at

If you need help installing Python, visit

PyAutoGUI supports Python 2 and 3. ...

Example:
```python
>>> import pyautogui
>>> screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
>>> currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
...
```

Sections: PyAutoGUI, Dependencies, Example Usage, How Does PyAutoGUI Work?

</details>

### pytweening

A collection of tweening (aka easing) functions.

`pip install pytweening` · installs from source (sdist only) · licence: MIT License · rank 2663 · last release 2024-02-20 · [PyPI](https://pypi.org/project/pytweening/)

<details><summary>README extract</summary>

A collection of tweening (aka easing) functions implemented in Python. You can learn more about it in this blog post: and in the Nordic Game Jam talk by Martin Jonasson and Petri Purho at

Sections: PyTweening, Example Usage, Tweens

</details>

### pygls

A pythonic generic language server (pronounced like 'pie glass')

`pip install pygls` · installs (wheel) · licence: Apache-2.0 · rank 2666 · last release 2026-03-25 · [PyPI](https://pypi.org/project/pygls/)

<details><summary>README extract</summary>

_pygls_ (pronounced like "pie glass") is a pythonic generic implementation of the Language Server Protocol for use as a foundation for writing your own Language Servers in just a few lines of code.

Example:
```python
from pygls.lsp.server import LanguageServer
from lsprotocol import types

server = LanguageServer("example-server", "v0.1")

@server.feature(types.TEXT_DOCUMENT_COMPLETION)
def completions(params: types.CompletionParams):
    items = []
    document = server.workspace.get_text_document(params.text_document.uri)
...
```

Sections: pygls: The Generic Language Server Framework, Quickstart, Docs and Tutorial, Projects based on _pygls_, Alternatives, Tests

</details>

### PyGetWindow

A simple, cross-platform module for obtaining GUI information on application's windows.

`pip install PyGetWindow` · installs from source (sdist only) · licence: BSD License · rank 2673 · last release 2020-10-04 · [PyPI](https://pypi.org/project/PyGetWindow/)

<details><summary>README extract</summary>

A simple, cross-platform module for obtaining GUI information on and controlling application's windows.

Still under development. Currently only the Windows platform is implemented. If you want to help contribute, please contact al@inventwithpython.com!

Install

 pip install pygetwindow

Examples ...

</details>

### pytest-lazy-fixtures

Allows you to use fixtures in @pytest.mark.parametrize.

`pip install pytest-lazy-fixtures` · installs (wheel) · licence: MIT · rank 2692 · last release 2026-08-12 · [PyPI](https://pypi.org/project/pytest-lazy-fixtures/) · [source](https://github.com/dev-petrov/pytest-lazy-fixtures)

<details><summary>README extract</summary>

Use your fixtures in `@pytest.mark.parametrize`.

This project was inspired by pytest-lazy-fixture.

Improvements that have been made in this project:

1. You can use fixtures in any data structures
2. You can access the attributes of fixtures
3. You can use functions in fixtures
4. It is compatible with pytest-deadfixtures

Example:
```python
import pytest
from pytest_lazy_fixtures import lf

@pytest.fixture()
def one():
    return 1

@pytest.mark.parametrize('arg1,arg2', [('val1', lf('one'))])
def test_func(arg1, arg2):
    assert arg2 == 1
```

Sections: pytest-lazy-fixtures, Usage, Injecting fixtures from a callable signature, Issues

</details>

### PyMsgBox

A simple, cross-platform, pure Python module for JavaScript-like message boxes.

`pip install PyMsgBox` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 2701 · last release 2025-09-09 · [PyPI](https://pypi.org/project/PyMsgBox/) · [docs](https://github.com/asweigart/pymsgbox) · [source](https://github.com/asweigart/pymsgbox)

_README extract left out: share-alike licence._

### PyScreeze

A simple, cross-platform screenshot module for Python 2 and 3.

`pip install PyScreeze` · installs from source (sdist only) · licence: MIT License · rank 2705 · last release 2024-08-20 · [PyPI](https://pypi.org/project/PyScreeze/)

<details><summary>README extract</summary>

PyScreeze is a simple, cross-platform screenshot module for Python 3.

PyScreeze can take screenshots, save them to files, and locates images within the screen. This is useful if you have a small image of, say, a button that needs to be clicked and want to locate it on the screen. ...

Sections: PyScreeze, About, Special Notes About Ubuntu, The screenshot() Function, The Locate Functions, Grayscale Matching, Pixel Matching

</details>

### PyRect

PyRect is a simple module with a Rect class for Pygame-like rectangular areas.

`pip install PyRect` · installs from source (sdist only) · licence: BSD License · rank 2708 · last release 2022-03-16 · [PyPI](https://pypi.org/project/PyRect/)

<details><summary>README extract</summary>

PyRect is a simple module with a Rect class for Pygame-like rectangular areas.

This module is like a stand-alone version of Pygame's Rect class. It is similar to the Rect module by Simon Wittber, but compatible with both Python 2 and 3.

Currently under development, though the basic features work.

Sections: PyRect, Quickstart Guide, Rect Attributes

</details>

### pre-commit-hooks

Some out-of-the-box hooks for pre-commit.

`pip install pre-commit-hooks` · installs (wheel) · licence: MIT · rank 2727 · last release 2025-08-09 · [PyPI](https://pypi.org/project/pre-commit-hooks/)

<details><summary>README extract</summary>

Some out-of-the-box hooks for pre-commit.

See also:

Add this to your `.pre-commit-config.yaml`

Sections: pre-commit-hooks, Using pre-commit-hooks with pre-commit, Hooks available, `check-added-large-files`, `check-ast`, `check-builtin-literals`, `check-case-conflict`, `check-docstring-first`, `check-executables-have-shebangs`, `check-illegal-windows-names`, `check-json`, `check-merge-conflict`, `check-shebang-scripts-are-executable`, `check-symlinks`

</details>

### pycasbin

An authorization library that supports access control models like ACL, RBAC, ABAC in Python

`pip install pycasbin` · installs (wheel) · licence: Apache Software License · rank 2755 · last release 2026-02-02 · [PyPI](https://pypi.org/project/pycasbin/)

<details><summary>README extract</summary>

News: 🔥 How to use it with `Django` ? Try Django Authorization, an authorization library for `Django` framework.

News: Async is now supported by Pycasbin >= 1.23.0!

News: still worry about how to write the correct Casbin policy? ``Casbin online editor`` is coming to help! Try it at: ...

Features:
What Casbin does:

1. enforce the policy in the classic ``{subject, object, action}`` form or a customized form as you defined, both allow and deny authorizations are supported.
2. handle the storage of the access control model and its policy.
3. ...

Example:
```python
import casbin
e = casbin.Enforcer("path/to/model.conf", "path/to/policy.csv")
```

...

</details>

### py-deviceid

A simple library to get or create a unique device id for a device in Python.

`pip install py-deviceid` · installs (wheel) · licence: MIT License · rank 2761 · last release 2025-03-07 · [PyPI](https://pypi.org/project/py-deviceid/) · [source](https://github.com/microsoft/py-deviceid)

<details><summary>README extract</summary>

`deviceid` provides a device ID for a given system, based on the `DevDeviceId` specification.

Example:
```python
from deviceid import get_device_id

device_id: str = get_device_id()

print(f'Device ID is: {deviceid}')
```

Sections: Device ID for Python, Usage, Trademarks

</details>

### pkce

PKCE Pyhton generator.

`pip install pkce` · installs (wheel) · licence: MIT License · rank 2784 · last release 2021-02-08 · [PyPI](https://pypi.org/project/pkce/)

<details><summary>README extract</summary>

Simple Python module to generate PKCE code verifier and code challenge.

Example:
```python
>>> import pkce
>>> code_verifier, code_challenge = pkce.generate_pkce_pair()
```

Sections: pkce (Proof Key for Code Exchange), Usage, Additional information

</details>

### protovalidate

Protocol Buffer Validation for Python

`pip install protovalidate` · installs (wheel) · licence: Apache-2.0 · rank 2794 · last release 2026-10-23 · [PyPI](https://pypi.org/project/protovalidate/) · [docs](https://protovalidate.com) · [source](https://github.com/bufbuild/protovalidate-py)

<details><summary>README extract</summary>

[][buf]

Protovalidate is the semantic validation library for Protobuf. It provides standard annotations to validate common rules on messages and fields, as well as the ability to use CEL to write custom rules. It's the next generation of protoc-gen-validate. ...

Example:
```python
try:
    protovalidate.validate(message)
except protovalidate.ValidationError as e:
    # Handle failure.
```

Sections: protovalidate-py, Documentation, Additional languages and repositories, Benchmarks, Legal

</details>

### pytest-retry

Adds the ability to retry flaky tests in CI environments

`pip install pytest-retry` · installs (wheel) · licence: MIT License · rank 2796 · last release 2025-01-19 · [PyPI](https://pypi.org/project/pytest-retry/)

<details><summary>README extract</summary>

pytest-retry is a plugin for Pytest which adds the ability to retry flaky tests,
thereby improving the consistency of the test suite results.

pytest-retry is designed for the latest versions of Python and Pytest. Python 3.9+
and pytest 7.0.0+ are required.

Example:
```python
def pytest_set_excluded_exceptions():
    """
    All tests will be retried unless they fail due to an AssertionError or CustomError
    """
    return [AssertionError, CustomError]
```

Sections: pytest-retry, Requirements, Usage, 1. Global settings, Advanced Options, 2. Pytest flaky mark, Things to consider, Reporting

</details>

### pythonnet

.NET and Mono integration for Python

`pip install pythonnet` · installs (wheel) · licence: MIT · rank 2807 · last release 2026-10-08 · [PyPI](https://pypi.org/project/pythonnet/)

<details><summary>README extract</summary>

|Join the chat at shield|

Python.NET is a package that gives Python programmers nearly
seamless integration with the .NET Common Language Runtime (CLR) and
provides a powerful application scripting tool for .NET developers. It
allows Python code to interact with the CLR, and may also be used to
embed Python into a .NET application. ...

Example:
```python
import clr
from System import String
from System.Collections import *
```

Sections: pythonnet - Python.NET, Calling .NET code from Python, .NET Core, Embedding Python in .NET, Example, Resources, .NET Foundation

</details>

### python-chess

A chess library with move generation, move validation, and support for common formats.

`pip install python-chess` · installs (wheel) · licence: GPL-3.0+ · rank 2824 · last release 2020-10-26 · [PyPI](https://pypi.org/project/python-chess/) · [docs](https://python-chess.readthedocs.io)

_README extract left out: share-alike licence._

### pyupgrade

A tool to automatically upgrade syntax for newer versions.

`pip install pyupgrade` · installs (wheel) · licence: MIT · rank 2829 · last release 2026-10-09 · [PyPI](https://pypi.org/project/pyupgrade/)

<details><summary>README extract</summary>

A tool (and pre-commit hook) to automatically upgrade syntax for newer
versions of the language.

Sections: pyupgrade, As a pre-commit hook, Implemented features, Set literals, Dictionary comprehensions, Format Specifiers, printf-style string formatting, Unicode literals, Invalid escape sequences, `is` / `is not` comparison to constant literals, `.encode()` to bytes literals, extraneous parens in `print(...)`, constant fold `isinstance` / `issubclass` / `except`, unittest deprecated aliases

</details>

### pulumi-random

A Pulumi package to safely use randomness in Pulumi programs.

`pip install pulumi-random` · installs (wheel) · licence: Apache-2.0 · rank 2853 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pulumi-random/) · [source](https://github.com/pulumi/pulumi-random)

<details><summary>README extract</summary>

The random provider allows the safe use of randomness in a Pulumi program. This allows you to generate resource
properties, such as names, that contain randomness in a way that works with Pulumi's goal state oriented approach. ...

Sections: Random Provider, Node.js (Java/TypeScript), Python, Go, .NET, Example, Reference

</details>

### pgserver

Self-contained postgres server for your python applications

`pip install pgserver` · does not install on CPython 3.14 · licence: not stated · rank 2858 · last release 2024-06-08 · [PyPI](https://pypi.org/project/pgserver/) · [source](https://github.com/orm011/pgserver)

<details><summary>README extract</summary>

Example:
```python
# Example 1: postgres backed application
import pgserver

db = pgserver.get_server(MYPGDATA)
# server ready for connection.

print(db.psql('create extension vector'))
db_uri = db.get_uri()
# use uri with sqlalchemy / psycopg, etc, see colab.

# if no other process is using this server, it will be shutdown at exit,
...
```

</details>

### pydata-sphinx-theme

Bootstrap-based Sphinx theme from the PyData community

`pip install pydata-sphinx-theme` · installs (wheel) · licence: BSD License · rank 2865 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pydata-sphinx-theme/) · [source](https://github.com/pydata/pydata-sphinx-theme)

<details><summary>README extract</summary>

A clean, three-column, Bootstrap-based Sphinx theme by and for the PyData community.

- :books: Documentation:
- :bulb: Examples:
- :raised_hands: Contribute:
- :globe_with_meridians: Translate:

</details>

### python-debian

Modules to read and manipulate many file formats related to Debian packages and repositories

`pip install python-debian` · installs (wheel) · licence: GPL-2.0-or-later · rank 2887 · last release 2026-06-07 · [PyPI](https://pypi.org/project/python-debian/)

_README extract left out: share-alike licence._

### py-walk

Filter filesystem paths based on gitignore-like patterns

`pip install py-walk` · installs (wheel) · licence: MIT License · rank 2891 · last release 2024-10-26 · [PyPI](https://pypi.org/project/py-walk/)

<details><summary>README extract</summary>

_Python library to filter filesystem paths based on gitignore-like patterns._

Example:

py-walk can be useful for applications or tools that work with paths and aim to
offer a `.gitignore` type file to their users. ...

Example:
```python
from py_walk import walk
from py_walk import get_parser_from_text

patterns = """
    **/data/*.bin
    !**/data/foo.bin

    # python files
    pycache/
    *.py[cod]
"""

# you can get the filtered paths from a directory
for path in walk("some/directory", ignore=patterns):
    do_something(path)

# ...or check paths against the patterns manually
...
```

Sections: py-walk, Usage, walk, get_parser_from, base_dir

</details>

### pystac-core

Core functionality for PySTAC without extensions. Most users will want to use pystac, not this package

`pip install pystac-core` · installs (wheel) · licence: Apache Software License · rank 2902 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-core/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

### pystac-ext-file

File extension for PySTAC

`pip install pystac-ext-file` · installs (wheel) · licence: Apache Software License · rank 2904 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-file/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the File Info Extension.
This extension provides fields for describing file details such as byte order, checksum, header size, and data type for assets.

Sections: pystac-ext-file, Versioning

</details>

### pystac-ext-mgrs

MGRS extension for PySTAC

`pip install pystac-ext-mgrs` · installs (wheel) · licence: Apache Software License · rank 2905 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-mgrs/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the MGRS Extension.
This extension provides fields for describing data using the Military Grid Reference System (MGRS), including UTM zone, latitude band, and grid square identifiers.

Sections: pystac-ext-mgrs, Versioning

</details>

### pystac-ext-timestamps

Timestamps extension for PySTAC

`pip install pystac-ext-timestamps` · installs (wheel) · licence: Apache Software License · rank 2906 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-timestamps/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Timestamps Extension.
This extension provides fields for additional temporal metadata beyond the core datetime, including published, expires, and unpublished timestamps.

Sections: pystac-ext-timestamps, Versioning

</details>

### pystac-ext-grid

Grid extension for PySTAC

`pip install pystac-ext-grid` · installs (wheel) · licence: Apache Software License · rank 2907 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-grid/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Grid Extension.
This extension describes gridded data products by specifying the grid code (e.g. MGRS, MODIS, or other tiling schemes) that the data corresponds to.

Sections: pystac-ext-grid, Versioning

</details>

### pystac-ext-xarray-assets

Xarray Assets extension for PySTAC

`pip install pystac-ext-xarray-assets` · installs (wheel) · licence: Apache Software License · rank 2908 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-xarray-assets/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Xarray Assets Extension.
This extension provides fields for describing how assets can be opened with xarray, including storage options, open parameters, and engine configuration.

Sections: pystac-ext-xarray-assets, Versioning

</details>

### pystac-ext-raster

Raster extension for PySTAC

`pip install pystac-ext-raster` · installs (wheel) · licence: Apache Software License · rank 2909 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-raster/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Raster Extension.
This extension provides fields for describing raster band metadata, including data type, statistics, histograms, spatial resolution, nodata values, and units.

Sections: pystac-ext-raster, Versioning

</details>

### pystac-ext-item-assets

Item Assets extension for PySTAC

`pip install pystac-ext-item-assets` · installs (wheel) · licence: Apache Software License · rank 2910 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-item-assets/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Item Assets Definition Extension.
This extension allows collections to define common asset properties that are shared across all items in the collection, providing a template for expected assets.

Sections: pystac-ext-item-assets, Versioning

</details>

### pystac-ext-version

Version extension for PySTAC

`pip install pystac-ext-version` · installs (wheel) · licence: Apache Software License · rank 2911 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-version/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Versioning Indicators Extension.
This extension provides fields for tracking version information and deprecation status of STAC items and collections, including links to predecessor and successor versions.

Sections: pystac-ext-version, Versioning

</details>

### pystac-ext-storage

Storage extension for PySTAC

`pip install pystac-ext-storage` · installs (wheel) · licence: Apache Software License · rank 2912 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-storage/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Storage Extension.
This extension provides fields for describing cloud storage attributes of assets, including storage platform, region, tier, and requester-pays configuration.

Sections: pystac-ext-storage, Versioning

</details>

### pystac-ext-label

Label extension for PySTAC

`pip install pystac-ext-label` · installs (wheel) · licence: Apache Software License · rank 2913 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-label/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Label Extension.
This extension provides fields for describing labeled training data for machine learning, including label types, classes, tasks, methods, and overviews of label distributions.

Sections: pystac-ext-label, Versioning

</details>

### pystac-ext-view

View extension for PySTAC

`pip install pystac-ext-view` · installs (wheel) · licence: Apache Software License · rank 2914 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-view/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the View Geometry Extension.
This extension provides fields for describing the angle of observation for geospatial data, including off-nadir angle, incidence angle, azimuth, and sun geometry.

Sections: pystac-ext-view, Versioning

</details>

### pystac-ext-mlm

Machine Learning Model extension for PySTAC

`pip install pystac-ext-mlm` · installs (wheel) · licence: Apache Software License · rank 2915 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-mlm/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Machine Learning Model Extension.
This extension provides fields for describing machine learning models, including model architecture, framework, input/output structure, training details, and runtime information.

Sections: pystac-ext-mlm, Versioning

</details>

### pystac-ext-classification

Classification extension for PySTAC

`pip install pystac-ext-classification` · installs (wheel) · licence: Apache Software License · rank 2916 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-classification/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Classification Extension.
This extension provides a way to describe categorical data and classification schemes for raster and vector data, including class names, descriptions, color hints, and regional mappings.

Sections: pystac-ext-classification, Versioning

</details>

### pystac-ext-table

Table extension for PySTAC

`pip install pystac-ext-table` · installs (wheel) · licence: Apache Software License · rank 2917 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-table/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Table Extension.
This extension provides fields for describing tabular data assets, including column definitions, row counts, primary/foreign keys, and storage formats.

Sections: pystac-ext-table, Versioning

</details>

### pystac-ext-eo

Electro-Optical extension for PySTAC

`pip install pystac-ext-eo` · installs (wheel) · licence: Apache Software License · rank 2918 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-eo/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Electro-Optical Extension.
This extension provides fields for describing electro-optical sensor data, including spectral band information, cloud cover, and snow cover.

Sections: pystac-ext-eo, Versioning

</details>

### pystac-ext-scientific

Scientific extension for PySTAC

`pip install pystac-ext-scientific` · installs (wheel) · licence: Apache Software License · rank 2919 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-scientific/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Scientific Citation Extension.
This extension provides fields for linking STAC items and collections to scientific publications, including DOIs and bibliographic citations.

Sections: pystac-ext-scientific, Versioning

</details>

### pystac-ext-sar

SAR extension for PySTAC

`pip install pystac-ext-sar` · installs (wheel) · licence: Apache Software License · rank 2920 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-sar/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the SAR Extension.
This extension provides fields for describing Synthetic-Aperture Radar (SAR) data, including instrument mode, frequency band, polarizations, product type, and observation direction.

Sections: pystac-ext-sar, Versioning

</details>

### pystac-ext-projection

Projection extension for PySTAC

`pip install pystac-ext-projection` · installs (wheel) · licence: Apache Software License · rank 2921 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-projection/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Projection Extension.
This extension provides fields for describing the geospatial projection of data, including EPSG code, WKT2, PROJJSON, geometry, bounding box, centroid, shape, and transform.

Sections: pystac-ext-projection, Versioning

</details>

### pystac-ext-pointcloud

Point Cloud extension for PySTAC

`pip install pystac-ext-pointcloud` · installs (wheel) · licence: Apache Software License · rank 2922 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-pointcloud/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Point Cloud Extension.
This extension provides fields for describing point cloud data, including point count, encoding, density, schemas, and statistics.

Sections: pystac-ext-pointcloud, Versioning

</details>

### pystac-ext-sat

Satellite extension for PySTAC

`pip install pystac-ext-sat` · installs (wheel) · licence: Apache Software License · rank 2923 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-sat/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Satellite Extension.
This extension provides fields for describing satellite-specific metadata, including orbit state vectors, relative orbit numbers, and platform-specific identifiers.

Sections: pystac-ext-sat, Versioning

</details>

### pystac-ext-datacube

Datacube extension for PySTAC

`pip install pystac-ext-datacube` · installs (wheel) · licence: Apache Software License · rank 2925 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-datacube/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Datacube Extension.
This extension describes datasets that are organized as multi-dimensional datacubes, including dimension types, extents, values, and reference systems.

Sections: pystac-ext-datacube, Versioning

</details>

### pystac-ext-render

Render extension for PySTAC

`pip install pystac-ext-render` · installs (wheel) · licence: Apache Software License · rank 2926 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pystac-ext-render/) · [docs](https://pystac.readthedocs.io) · [source](https://github.com/stac-utils/pystac)

<details><summary>README extract</summary>

PySTAC extension package for the Render Extension.
This extension provides fields for describing visualization parameters for assets, including rescaling, color maps, expressions, and tile matrix set configurations.

Sections: pystac-ext-render, Versioning

</details>

### protoc-gen-openapiv2

Provides the missing pieces for gRPC Gateway.

`pip install protoc-gen-openapiv2` · installs (wheel) · licence: BSD License · rank 2928 · last release 2022-12-02 · [PyPI](https://pypi.org/project/protoc-gen-openapiv2/)

### pympp

Python SDK for the Machine Payments Protocol (MPP)

`pip install pympp` · installs (wheel) · licence: Apache Software License; MIT License · rank 2945 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pympp/) · [docs](https://github.com/tempoxyz/pympp#readme)

<details><summary>README extract</summary>

Python SDK for the Machine Payments Protocol

Full documentation, API reference, and guides are available at mpp.dev/sdk/python.

Example:
```python
from mpp.methods.stripe import server as stripe

server = Mpp(methods=stripe.charge(secret_key="sk...", network_id="bn...", currency="usd"))
```

Sections: pympp, Documentation, Quick Start, Server, Serve x402 clients, Client, Pay x402 servers, Examples, Restrict automatic payment origins, Hosted fee-payer services, Payment request context

</details>

### pymediainfo

A Python wrapper for the MediaInfo library.

`pip install pymediainfo` · installs (wheel) · licence: MIT License · rank 2954 · last release 2025-02-12 · [PyPI](https://pypi.org/project/pymediainfo/) · [docs](https://pymediainfo.readthedocs.io/)

<details><summary>README extract</summary>

pymediainfo is a wrapper for the MediaInfo library. It makes it easy to
extract detailed information from multimedia files.

pymediainfo is compatible with the following:

* Platforms: Linux, macOS and Windows.
* Python Versions: Tested with Python 3.9 (the minimum required version) to 3.13, as well as PyPy3.

Example:
```python
from pymediainfo import MediaInfo

media_info = MediaInfo.parse("/home/user/image.jpg")
# Tracks can be accessed using the 'tracks' attribute or through shorthands
# such as 'image_tracks', 'audio_tracks', 'video_tracks', etc.
general_track = media_info.general_tracks[0]
image_track = media_info.image_tracks[0]
print(
...
```

...

</details>

### pandasql

sqldf for pandas

`pip install pandasql` · installs from source (sdist only) · licence: not stated · rank 2962 · last release 2016-04-20 · [PyPI](https://pypi.org/project/pandasql/)

<details><summary>README extract</summary>

`pandasql` allows you to query `pandas` DataFrames using SQL syntax.
It works similarly to `sqldf` in R. `pandasql` seeks to provide a
more familiar way of manipulating and cleaning data for people new to
Python or `pandas`.

Example:
```python
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())
```

Sections: pandasql, Basics, Querying

</details>

### pygltflib

Python library for reading, writing and managing 3D objects in the Khronos Group gltf and gltf2 formats.

`pip install pygltflib` · installs (wheel) · licence: MIT License · rank 2977 · last release 2025-07-24 · [PyPI](https://pypi.org/project/pygltflib/)

<details><summary>README extract</summary>

This is a library for reading, writing and handling GLTF v2 files. It works for Python3.6 and above.

It supports the entire specification, including materials and animations. Main features are:
* GLB and GLTF support
* Buffer data conversion
* Extensions
* All attributes are type-hinted

Example:
```python
from pygltflib import GLTF2

gltf = GLTF2()
```

Sections: pygltflib, Quickstart, How do I..., Create an empty GLTF2 object?, Add a scene?, Load a file?, Load a binary GLB file?, Load a binary file with an unusual extension?, Load A B3DM file?, Create a mesh?, Convert buffers to glb binary buffers?, Convert buffer to data uri (embedded) buffer?, Convert buffers to binary file (external) buffers?, Convert a glb to a gltf file?

</details>

### pulumi-gcp

A Pulumi package for creating and managing Google Cloud Platform resources.

`pip install pulumi-gcp` · installs (wheel) · licence: Apache-2.0 · rank 2987 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pulumi-gcp/) · [source](https://github.com/pulumi/pulumi-gcp)

<details><summary>README extract</summary>

The Google Cloud Platform (GCP) resource provider for Pulumi lets you use GCP resources in your cloud programs. To use
this package, install the Pulumi CLI. For a streamlined Pulumi walkthrough, including language runtime installation and GCP configuration, select "Get Started" below.

Sections: Google Cloud Platform Resource Provider, Node.js (JavaScript/TypeScript), Python, Go, .NET, Reference

</details>

### pytz-deprecation-shim

Shims to make deprecation of pytz easier

`pip install pytz-deprecation-shim` · installs (wheel) · licence: Apache Software License · rank 3039 · last release 2020-06-17 · [PyPI](https://pypi.org/project/pytz-deprecation-shim/) · [docs](https://pytz-deprecation-shim.readthedocs.io) · [source](https://github.com/pganssle/pytz-deprecation-shim)

<details><summary>README extract</summary>

`pytz` has served the Python community well for many years, but it is no
longer the best option for providing time zones. `pytz` has a non-standard
interface that is very easy to misuse; this
interface was necessary when `pytz` was created, because `datetime` had no
way to represent ambiguous datetimes, but this was solved in in Python 3.6,
which ...

Example:
```python
>>> import pytz_deprecation_shim as pds
>>> from datetime import datetime, timedelta
>>> LA = pds.timezone("America/Los_Angeles")

>>> dt = datetime(2020, 10, 31, 12, tzinfo=LA)
>>> print(dt)
2020-10-31 12:00:00-07:00

>>> dt.tzname()
'PDT'
```

Sections: pytz_deprecation_shim: Shims to help you safely remove pytz, Usage

</details>

### python-pam

(no summary)

`pip install python-pam` · installs (wheel) · licence: not stated · rank 3084 · last release 2026-10-28 · [PyPI](https://pypi.org/project/python-pam/)

<details><summary>README extract</summary>

Python pam module supporting py3 for Linux type systems (!windows)

Example:
```python
>>> import pam
>>> pam.authenticate('david', 'correctpassword')
True
>>> p = pam.pam()
>>> p.authenticate('david', 'correctpassword')
True
>>> p.authenticate('david', 'badpassword')
False
>>> p.authenticate('david', 'correctpassword', service='login')
True
>>> p.authenticate('david', 'correctpassword', service='unknownservice')
False
...
```

Sections: python-pam, Threading and concurrency, Credentials (`resetcreds`), Examples, Authentication and privileges

</details>

### plaster-pastedeploy

A loader implementing the PasteDeploy syntax to be used by plaster.

`pip install plaster-pastedeploy` · installs (wheel) · licence: MIT License · rank 3088 · last release 2022-11-07 · [PyPI](https://pypi.org/project/plaster-pastedeploy/)

<details><summary>README extract</summary>

`plaster_pastedeploy` is a plaster plugin that provides a `plaster.Loader`
that can parse ini files according to the standard set by PasteDeploy. It
supports the `wsgi` plaster protocol, implementing the
`plaster.protocols.IWSGIProtocol` interface.

Example:
```python
import plaster

loader = plaster.get_loader('development.ini', protocols=['wsgi'])
# to get any section out of the config file
settings = loader.get_settings('app:main')

# to get settings for a WSGI app
app_config = loader.get_wsgi_app_settings()  # defaults to main

# to get an actual WSGI app
app = loader.get_wsgi_app()  # defaults to main

...
```

...

</details>

### plaster

A loader interface around multiple config file formats.

`pip install plaster` · installs (wheel) · licence: MIT License · rank 3089 · last release 2022-11-21 · [PyPI](https://pypi.org/project/plaster/)

<details><summary>README extract</summary>

`plaster` is a loader interface around multiple config file formats. It
exists to define a common API for applications to use when they wish to load
configuration. The library itself does not aim to handle anything except
a basic API that applications may use to find and load configuration settings. ...

Sections: plaster, 1.1.2 (2022-11-20), 1.1.1 (2022-11-20), 1.1 (2022-10-06), 1.0 (2017-10-11), 0.5 (2017-06-02), 0.4 (2017-03-30), 0.3 (2017-03-27), 0.2 (2016-06-15), 0.1 (2016-06-12)

</details>

### PyQt5

Python bindings for the Qt cross platform application toolkit

`pip install PyQt5` · installs (wheel) · licence: GPL v3 · rank 3090 · last release 2024-07-19 · [PyPI](https://pypi.org/project/PyQt5/)

_README extract left out: share-alike licence._

### progress

Easy to use progress bars

`pip install progress` · installs (wheel) · licence: ISC · rank 3094 · last release 2025-07-01 · [PyPI](https://pypi.org/project/progress/) · [source](https://github.com/verigak/progress.git)

<details><summary>README extract</summary>

There are 7 progress bars to choose from:

- `Bar`
- `ChargingBar`
- `FillingSquaresBar`
- `FillingCirclesBar`
- `IncrementalBar`
- `PixelBar`
- `ShadyBar`

To use them, just call `next` to advance and `finish` to finish:

or use any bar of this class as a context manager: ...

Example:
```python
from progress.bar import Bar

bar = Bar('Processing', max=20)
for i in range(20):
    # Do some work
    bar.next()
bar.finish()
```

Sections: Easy progress reporting for Python, Bars, Spinners, Other

</details>

### perfetto

Python APIs and bindings for Perfetto (perfetto.dev)

`pip install perfetto` · installs (wheel) · licence: apache-2.0 · rank 3096 · last release 2026-10-26 · [PyPI](https://pypi.org/project/perfetto/)

### python-jsonpath

JSONPath, JSON Pointer and JSON Patch for Python.

`pip install python-jsonpath` · installs (wheel) · licence: MIT · rank 3117 · last release 2026-10-17 · [PyPI](https://pypi.org/project/python-jsonpath/) · [docs](https://jg-rp.github.io/python-jsonpath/) · [source](https://github.com/jg-rp/python-jsonpath)

<details><summary>README extract</summary>

A flexible JSONPath engine for Python.

We follow RFC 9535 and test against the JSONPath Compliance Test Suite.

Table of Contents

- Install
- Links
- Related projects
- Examples
- License

Example:
```python
import jsonpath

data = {
    "users": [
        {"name": "Sue", "score": 100},
        {"name": "John", "score": 86},
        {"name": "Sally", "score": 84},
        {"name": "Jane", "score": 55},
    ]
}

user_names = jsonpath.findall("$.users[?@.score < 100].name", data)
print(user_names) # ['John', 'Sally', 'Jane']
```

Sections: Python JSONPath, Links, Related projects, Examples, JSONPath, JSON Pointer, JSON Patch

</details>

### PyQt5-sip

The sip module support for PyQt5

`pip install PyQt5-sip` · installs (wheel) · licence: BSD-2-Clause · rank 3135 · last release 2026-10-10 · [PyPI](https://pypi.org/project/PyQt5-sip/)

<details><summary>README extract</summary>

The sip extension module provides support for the PyQt5 package.

</details>

### pulumi-kubernetes

A Pulumi package for creating and managing Kubernetes resources.

`pip install pulumi-kubernetes` · installs (wheel) · licence: Apache-2.0 · rank 3154 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pulumi-kubernetes/) · [source](https://github.com/pulumi/pulumi-kubernetes)

<details><summary>README extract</summary>

The Kubernetes resource provider for Pulumi lets you create, deploy, and manage Kubernetes API resources and workloads in a running cluster. For a streamlined Pulumi walkthrough, including language runtime installation and Kubernetes configuration, select "Get Started" below. ...

Sections: Pulumi Kubernetes Resource Provider, Introduction, References, Prerequisites, Quick Examples, Deploying a YAML Manifest, Deploying a Helm Chart, Deploying a Workload using the Resource API

</details>

### pycollada

python library for reading and writing collada documents

`pip install pycollada` · installs (wheel) · licence: BSD · rank 3157 · last release 2026-01-24 · [PyPI](https://pypi.org/project/pycollada/)

<details><summary>README extract</summary>

pycollada is a python module for creating, editing and loading
COLLADA, which is a COLLAborative Design Activity
for establishing an interchange file format for interactive 3D applications.

The library allows you to load a COLLADA file and interact with it as a python
object. ...

Sections: pycollada, Projects using pycollada

</details>

### pytest-alembic

A pytest plugin for verifying alembic migrations.

`pip install pytest-alembic` · installs (wheel) · licence: MIT · rank 3160 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pytest-alembic/) · [source](https://github.com/schireson/pytest-alembic)

<details><summary>README extract</summary>

See the full documentation here.

A pytest plugin to test alembic migrations (with default tests) and
which enables you to write tests specific to your migrations.

Runs on Python 3.10 – 3.15 with alembic 1.9+ and SQLAlchemy 1.4+, on Linux, macOS and
Windows.

Example:
```python
from sqlalchemy import text

def test_gnarly_migration_xyz123(alembic_engine, alembic_runner):
    # Migrate up to, but not including this new migration
    alembic_runner.migrate_up_before('xyz123')

    # Perform some very specific data setup, because this migration is sooooo complex.
    # ...
...
```

Sections: Introduction, The pitch, Built-in Tests, Custom Tests

</details>

### pinecone-plugin-assistant

Assistant plugin for Pinecone SDK

`pip install pinecone-plugin-assistant` · installs (wheel) · licence: Apache Software License · rank 3171 · last release 2026-03-27 · [PyPI](https://pypi.org/project/pinecone-plugin-assistant/) · [docs](https://pinecone.io/docs)

<details><summary>README extract</summary>

Interact with Pinecone's Assistant APIs, e.g. create, manage, and chat with assistants (currently in beta). Pinecone Assistant is also available in the console.

Example:
```python
from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message

pc = Pinecone(api_key='<<PINECONE_API_KEY>>')

# Create an assistant (in this case we'll store documents about planets)
space_assistant = pc.assistant.create_assistant(assistant_name="space")

# Upload information to your assistant
...
```

Sections: Assistant, Quickstart, Assistants API, Create Assistant, Describe Assistant, Update Assistant, List Assistants, Delete Assistant, Assistants Model API, Upload File to Assistant, Describe File to Assistant, List Files, Delete file from assistant, Chat

</details>

### pydantic-avro

Converting pydantic classes to avro schemas

`pip install pydantic-avro` · installs (wheel) · licence: MIT License · rank 3176 · last release 2026-09-05 · [PyPI](https://pypi.org/project/pydantic-avro/) · [source](https://github.com/godatadriven/pydantic-avro)

<details><summary>README extract</summary>

This library can convert a pydantic class to a avro schema or generate python code from a avro schema.

Example:
```python
import json
from typing import Optional

from pydantic_avro.base import AvroBase

class TestModel(AvroBase):
    key1: str
    key2: int
    key2: Optional[str]

schema_dict: dict = TestModel.avro_schema()
print(json.dumps(schema_dict))
```

Sections: pydantic-avro, Pydantic class to avro schema, Avro schema to pydantic, Specify expected Avro type, Run unit tests, Run linting

</details>

### PyQt5-Qt5

The subset of a Qt installation needed by PyQt5.

`pip install PyQt5-Qt5` · installs (wheel) · licence: LGPL v3 · rank 3205 · last release 2026-05-21 · [PyPI](https://pypi.org/project/PyQt5-Qt5/)

_README extract left out: share-alike licence._

### pyreadline3

A python implementation of GNU readline.

`pip install pyreadline3` · installs (wheel) · licence: BSD License · rank 3214 · last release 2026-05-14 · [PyPI](https://pypi.org/project/pyreadline3/) · [docs](https://github.com/pyreadline3/pyreadline3) · [source](https://github.com/pyreadline3/pyreadline3.git)

<details><summary>README extract</summary>

The `pyreadline3` package is based on the stale package `pyreadline` located
here.
The original `pyreadline` package is a Python implementation of GNU `readline`
functionality.
It is based on the `ctypes` based UNC `readline` package by Gary Bishop.
It is not complete.
It has been tested for use with Windows 10. ...

Features:
- keyboard text selection and copy/paste
- Shift-arrowkeys for text selection
- Control-c can be used for copy activate with allow_ctrl_c(True) in config file
- Double tapping ctrl-c will raise a KeyboardInterrupt, use ctrl_c_tap_time_interval(x) ...

Sections: pyreadline3, Features, Build The Virtual Environment, Setup, Debugging

</details>

### proxy_tools

Proxy Implementation

`pip install proxy_tools` · installs from source (sdist only) · licence: MIT License · rank 3224 · last release 2014-05-05 · [PyPI](https://pypi.org/project/proxy_tools/)

<details><summary>README extract</summary>

I'm just a proxy

Loveingly extracted from werkzeug. A very useful proxy implementation, that I found to be useful outside
the web context -- hence the extraction.

Example:
```python
from proxy_tools import Proxy
p = Proxy()

def get_current_user():
    return User.find_by_id(request['user_id'])

current_user = p(get_current_user)

# Or alternatively

from proxy_tools import module_property

@module_property
def current_user():
    return User.find_by_id(request['user_id'])

# Then
print(current_user.name)
```

Sections: proxy_tools, Basic Usage, Questions / Issues, Thank you

</details>

### pyvis

A Python network graph visualization library

`pip install pyvis` · installs (wheel) · licence: BSD · rank 3252 · last release 2023-02-24 · [PyPI](https://pypi.org/project/pyvis/)

<details><summary>README extract</summary>

Pyvis is built around visjs, a JavaScript visualization library.

Pyvis' full documentation can be found at

Example:
```python
from pyvis.network import Network

g = Network()
g.add_node(0)
g.add_node(1)
g.add_edge(0, 1)
g.show("basic.html")
```

Sections: Pyvis - a Python library for visualizing networks, Description, Documentation, Dependencies, Test Dependencies, Quick Start, Interactive Notebook playground with examples

</details>

### pygeohash

Python module for interacting with geohashes

`pip install pygeohash` · installs (wheel) · licence: MIT License · rank 3262 · last release 2026-09-06 · [PyPI](https://pypi.org/project/pygeohash/)

<details><summary>README extract</summary>

A simple, lightweight, and dependency-free Python library for working with geohashes.

Full docs at pygeohash.mcginniscommawill.com

PyGeoHash is a Python module that provides functions for encoding and decoding geohashes to and from latitude and longitude coordinates, along with utilities for performing calculations and approximations with them. ...

Features:
- Zero Dependencies: Works with just the Python standard library
- Simple API: Clean, intuitive functions that are easy to understand
- Lightweight: Minimal overhead for your projects
- Python 3 Support: Fully compatible with modern Python ...

Example:
```python
import pygeohash as pgh

# Encode coordinates to geohash
geohash = pgh.encode(latitude=42.6, longitude=-5.6)
print(geohash)  # 'ezs42e44yx96'

# Control precision
...

</details>

### pdbr

Pdb with Rich library.

`pip install pdbr` · installs (wheel) · licence: not stated · rank 3263 · last release 2026-07-15 · [PyPI](https://pypi.org/project/pdbr/) · [source](https://github.com/cansarigol/pdbr)

<details><summary>README extract</summary>

`pdbr` is intended to make the PDB results more colorful. it uses Rich library to carry out that.

Example:
```python
import os

os.environ["PYTHONBREAKPOINT"] = "pdbr.set_trace"
```

Sections: pdbr, Breakpoint, What `import pdbr` does at load time, New commands, (i)nspect / inspectall | ia, search | src, sql, (syn)tax, (v)ars, varstree | vt, log, IPython integration, whereami

</details>

### patito

A dataframe modelling library built on top of polars and pydantic.

`pip install patito` · installs (wheel) · licence: MIT · rank 3283 · last release 2026-02-04 · [PyPI](https://pypi.org/project/patito/) · [docs](https://patito.readthedocs.io) · [source](https://github.com/JakobGM/patito)

<details><summary>README extract</summary>

Patito combines pydantic and polars in order to write modern, type-annotated data frame logic.

Patito offers a simple way to declare pydantic data models which double as schema for your polars data frames.
These schema can be used for: ...

Example:
```python
# models.py
from typing import Literal

import patito as pt

class Product(pt.Model):
    product_id: int = pt.Field(unique=True)
    temperature_zone: Literal["dry", "cold", "frozen"]
    is_for_sale: bool
```

Sections: Patito, Documentation, 👮 Data validation, 🧪 Synthesize valid test data, 🖼️ A model-aware data frame class, 🐍 Representing rows as classes

</details>

### python-liquid

A Python engine for the Liquid template language.

`pip install python-liquid` · installs (wheel) · licence: MIT · rank 3286 · last release 2026-10-25 · [PyPI](https://pypi.org/project/python-liquid/) · [docs](https://jg-rp.github.io/liquid/) · [source](https://github.com/jg-rp/liquid)

<details><summary>README extract</summary>

Python Liquid is a Python engine for Liquid, the safe, customer-facing template language.

We follow Shopify/Liquid closely and test against the Golden Liquid test suite.

Table of Contents

- Install
- Links
- Related Projects
- Quick Start
- Contributing

Example:
```python
from liquid import render

print(render("Hello, {{ you }}!", you="World"))
# Hello, World!
```

Sections: Python Liquid, Links, Related Projects, Quick Start, `render()`, `parse()`, Configure

</details>

### price-parser

Extract price and currency from a raw string

`pip install price-parser` · installs (wheel) · licence: BSD-3-Clause · rank 3287 · last release 2026-03-19 · [PyPI](https://pypi.org/project/price-parser/) · [source](https://github.com/scrapinghub/price-parser)

<details><summary>README extract</summary>

`price-parser` is a small library for extracting price and currency from
raw text strings.

Features:

* robust price amount and currency symbol extraction
* zero-effort handling of thousand and decimal separators

The main use case is parsing prices extracted from web pages. ...

Sections: price-parser, Usage, Basic usage, Currency hints, Decimal separator

</details>

### polling

Powerful polling utility with many configurable options

`pip install polling` · installs from source (sdist only) · licence: MIT · rank 3289 · last release 2021-05-22 · [PyPI](https://pypi.org/project/polling/)

### prefect-cloud

Package for easily deploying to Prefect Cloud.

`pip install prefect-cloud` · installs (wheel) · licence: not stated · rank 3306 · last release 2026-10-27 · [PyPI](https://pypi.org/project/prefect-cloud/)

<details><summary>README extract</summary>

:zap: Deploy your code to Prefect Cloud in seconds! :zap:

Deploy and run your Python functions on Prefect Cloud with a single command.

Example:
```python
#

def hello_world():
    print("Hello, World!")
```

Sections: prefect-cloud, Login to Prefect Cloud, Deploy your workflow, Deploy to Prefect Cloud, Run it with, Schedule it with, Additional Options

</details>

### pynvvideocodec

pynvvideocodec (PyNvVideoCodec) is NVIDIA's Python library for hardware-accelerated video encode/decode on NVIDIA GPUs.

`pip install pynvvideocodec` · installs (wheel) · licence: MIT License · rank 3316 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pynvvideocodec/) · [docs](https://docs.nvidia.com/video-technologies/pynvvideocodec/index.html) · [source](https://catalog.ngc.nvidia.com/orgs/nvidia/resources/pynvvideocodec)

<details><summary>README extract</summary>

PyNvVideoCodec is NVIDIA's Python-based library that provides simple yet powerful Python APIs for hardware-accelerated video encoding and decoding on NVIDIA GPUs.

PyNvVideoCodec is built on top of the Video Codec SDK and offers encode, decode, and transcode performance on par with it. ...

Features:
PyNvVideoCodec supports following features:

Example:
```python
import site; print(site.getsitepackages())
```

Sections: PyNvVideoCodec, Features, Decode Features, Encode Features, Transcode Features, What's New, v 2.2.4 (Latest), v 2.2.3, v 2.2, Distribution, Sample Applications and Documents

</details>

### PyQt6-Qt6

The subset of a Qt installation needed by PyQt6.

`pip install PyQt6-Qt6` · installs (wheel) · licence: LGPL v3 · rank 3326 · last release 2026-10-28 · [PyPI](https://pypi.org/project/PyQt6-Qt6/)

_README extract left out: share-alike licence._

### pyramid-mako

Mako template bindings for the Pyramid web framework

`pip install pyramid-mako` · installs (wheel) · licence: Repoze Public License · rank 3327 · last release 2019-08-18 · [PyPI](https://pypi.org/project/pyramid-mako/) · [docs](https://docs.pylonsproject.org/projects/pyramid_mako/en/latest/)

<details><summary>README extract</summary>

These are bindings for the Mako templating system for the Pyramid web framework.

Documentation for pyramid_mako.

- Add support for Python 3.5, 3.6, 3.7.

- Require `mako >= 1.1.0`.

- Add a config option for `preprocessor_wants_settings`. ...

Sections: Mako bindings for Pyramid, 1.1.0 (2019-08-18), 1.0.2 (2014-04-22), 1.0.1 (2014-04-16), 1.0 (2014-04-15), 0.3.1 (2013-10-22), 0.3 (2013-10-20), 0.2 (2013-09-07), 0.1 (2012-03-12)

</details>

### pyvers

A Python library for managing multiple versions of dependencies

`pip install pyvers` · installs (wheel) · licence: MIT License · rank 3344 · last release 2026-07-09 · [PyPI](https://pypi.org/project/pyvers/)

<details><summary>README extract</summary>

A Python library for dynamic dispatch based on module versions and backends.

- 🔄 Handle breaking changes between different versions of a library without cluttering your code
- 🔀 Switch seamlessly between different backend implementations (e.g., CPU vs GPU) ...

Example:
```python
from pyvers import implement_for, register_backend, get_backend, set_backend

# Register numpy backend - you could register more than one backend!
register_backend(group="numpy", backends={"numpy": "numpy"})

# Define the function with @implement_for, then register version-specific implementations
@implement_for("numpy")
def create_mask(arr):
...
```

...

</details>

### prefixdate

Parse and process date string of varied precision as prefixes in Python.

`pip install prefixdate` · installs (wheel) · licence: MIT · rank 3348 · last release 2026-08-08 · [PyPI](https://pypi.org/project/prefixdate/) · [source](https://github.com/pudo/prefixdate.git)

<details><summary>README extract</summary>

This is a helper class to parse dates with varied degrees of precision. For
example, a data source might state a date as `2001`, `2001-4` or `2001-04-02`,
with the implication that only the year, month or day is known. This library
will process such partial dates into a structured format and allow their
validation and re-formatting (e.g. ...

Example:
```python
from prefixdate import parse, normalize_date, Precision

# Parse returns a `DatePrefix` object:
date = parse('2001-3')
assert date.text == '2001-03'
date = parse(2001)
assert date.text == '2001'
assert date.precision == Precision.YEAR

date = parse(None)
assert date.text is None
assert date.precision == Precision.EMPTY
...
```

Sections: Prefix date parser, Usage, Format strings, Two-digit years, Inspecting format strings, Caveats

</details>

### PyQt6-sip

The sip module support for PyQt6

`pip install PyQt6-sip` · installs (wheel) · licence: BSD-2-Clause · rank 3350 · last release 2026-10-10 · [PyPI](https://pypi.org/project/PyQt6-sip/)

<details><summary>README extract</summary>

The sip extension module provides support for the PyQt6 package.

</details>

### posthoganalytics

Integrate PostHog into any python application.

`pip install posthoganalytics` · installs (wheel) · licence: MIT · rank 3363 · last release 2026-11-06 · [PyPI](https://pypi.org/project/posthoganalytics/) · [source](https://github.com/posthog/posthog-python)

<details><summary>README extract</summary>

> Do not use this package. Use `posthog` instead.

This package exists solely for internal use by posthog/posthog to avoid import conflicts with the local `posthog` package in that repository. It is an automatically generated mirror of `posthog` — same code, same versions, just published under a different name. ...

</details>

### PyVirtualDisplay

python wrapper for Xvfb, Xephyr and Xvnc

`pip install PyVirtualDisplay` · installs (wheel) · licence: BSD License · rank 3376 · last release 2022-02-13 · [PyPI](https://pypi.org/project/PyVirtualDisplay/)

<details><summary>README extract</summary>

pyvirtualdisplay is a python wrapper for Xvfb, Xephyr and Xvnc

Documentation:

</details>

### pyramid-jinja2

Jinja2 template bindings for the Pyramid web framework

`pip install pyramid-jinja2` · installs (wheel) · licence: Repoze Public License · rank 3379 · last release 2024-02-08 · [PyPI](https://pypi.org/project/pyramid-jinja2/) · [docs](https://docs.pylonsproject.org/projects/pyramid_jinja2/en/latest/)

<details><summary>README extract</summary>

These are bindings for the Jinja2 templating system
for the Pyramid web framework.

See for
documentation or `index.rst` in the `docs` sub-directory of the source
distribution.

- Rename "master" git branch to "main"

- Add Python 3.11 and 3.12 support.

- Replace usage of private Pyramid APIs.

- Add `jinja2.i18n_extension` configuration setting. ...

Features:
- Add `model_url` and `route_url` filter implementations (and
 documented).

Example:
```python
  ValueError: As of pyramid_jinja2 2.3, the use of the
  "pyramid_jinja2.renderer_factory" requires that pyramid_jinja2 be
  configured via config.include("pyramid_jinja2") or the equivalent
  "pyramid.includes" setting.

The fix is to include `pyramid_jinja2`::

  config.include("pyramid_jinja2")
```

...

</details>

### pydruid

A Python connector for Druid.

`pip install pydruid` · installs from source (sdist only) · licence: Apache Software License · rank 3386 · last release 2024-05-16 · [PyPI](https://pypi.org/project/pydruid/) · [docs](https://pythonhosted.org/pydruid/) · [source](https://github.com/druid-io/pydruid)

<details><summary>README extract</summary>

pydruid exposes a simple API to create, execute, and analyze Druid queries. pydruid can parse query results into Pandas DataFrame objects for subsequent data analysis -- this offers a tight integration between Druid, the SciPy stack (for scientific computing) and scikit-learn (for machine learning). ...

Example:
```python
from pydruid.client import *
from pylab import plt

query = PyDruid(druid_url_goes_here, 'druid/v2')

ts = query.timeseries(
    datasource='twitterstream',
    granularity='day',
    intervals='2014-02-02/p4w',
    aggregations={'length': doublesum('tweet_length'), 'count': doublesum('count')},
...
```

Sections: pydruid, examples, timeseries, topN, groupby, asynchronous client, engine = create_engine('druid+

</details>

### pyroscope-otel

A library providing profiling functionalities related to OpenTelemetry

`pip install pyroscope-otel` · installs (wheel) · licence: not stated · rank 3415 · last release 2026-06-30 · [PyPI](https://pypi.org/project/pyroscope-otel/)

<details><summary>README extract</summary>

Example:
```python
from pyroscope import configure as pyroscope_configure

# Local setup (default)
pyroscope_configure(
    app_name="my-app",
    server_address="
    sample_rate=100,
)

# Grafana Cloud setup (uncomment and update with your credentials)
# pyroscope_configure(
# app_name="my-app",
# server_address="
# auth_token="<your-grafana-cloud-token>",
...
```

Sections: Prerequisites, Pyroscope Configuration (Required), How It Works & Span Attributes, Manual Instrumentation, Automatic Instrumentation, Grafana Cloud OpenTelemetry Exporter (Optional), Integration Checklist, Troubleshooting, References

</details>

### phonemizer

Simple text to phones converter for multiple languages

`pip install phonemizer` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 3430 · last release 2026-11-02 · [PyPI](https://pypi.org/project/phonemizer/) · [docs](https://bootphon.github.io/phonemizer/) · [source](https://github.com/bootphon/phonemizer)

_README extract left out: share-alike licence._

### pybase62

Python module for base62 encoding

`pip install pybase62` · installs (wheel) · licence: not stated · rank 3431 · last release 2023-05-29 · [PyPI](https://pypi.org/project/pybase62/)

<details><summary>README extract</summary>

A Python module for `base62` encoding. Ported from PHP code that I wrote
in mid-2000, which can be found
here.

When writing a web application, often times we would like to keep the URLs
short.

This certainly gives a more concise look than the following. ...

Example:
```python
>>> import base62

>>> base62.encode(34441886726)
'base62'

>>> base62.decode('base62')
34441886726
```

Sections: base62, Rationale, Usage, Tests, Deployment

</details>

### PyQt6

Python bindings for the Qt cross platform application toolkit

`pip install PyQt6` · installs (wheel) · licence: GPL-3.0-only · rank 3441 · last release 2026-10-28 · [PyPI](https://pypi.org/project/PyQt6/)

_README extract left out: share-alike licence._

### pixelhog

Rust-accelerated pixelmatch and SSIM for PNG bytes

`pip install pixelhog` · installs (wheel) · licence: MIT License · rank 3452 · last release 2026-09-16 · [PyPI](https://pypi.org/project/pixelhog/) · [source](https://github.com/PostHog/pixelhog)

<details><summary>README extract</summary>

Fast visual regression primitives for Python, implemented in Rust.

`pixelhog` compares screenshots in two complementary ways:
- `diff`: exact pixel-level differences (with anti-alias handling), optional diff image output
- `ssim`: perceptual similarity score in `[0.0, 1.0]` ...

Example:
```python
from pixelhog import Comparison, thumbnail

cmp = Comparison(baseline_png, current_png)

count = cmp.diff_count()                     # pixel mismatch count
score = cmp.ssim()                           # perceptual similarity
png   = cmp.diff_image()                     # diff visualization (PNG bytes)
...
```

Sections: pixelhog, Quickstart, API at a glance, Comparison, Utilities and batch, Row alignment (vertical shifts), Behavior, Correctness and tests, Benchmarks

</details>

### plum-dispatch

Multiple dispatch in Python

`pip install plum-dispatch` · installs (wheel) · licence: MIT License · rank 3478 · last release 2026-09-07 · [PyPI](https://pypi.org/project/plum-dispatch/) · [docs](https://beartype.github.io/plum) · [source](https://github.com/beartype/plum)

<details><summary>README extract</summary>

Everybody likes multiple dispatch, just like everybody likes plums.

The design philosophy of Plum is to provide an implementation of multiple dispatch that is Pythonic, yet close to how Julia does it.
See here for a comparison between Plum, `multipledispatch`, and `multimethod`. ...

Example:
```python
from numbers import Number

from plum import dispatch

@dispatch
def f(x: str):
    return "This is a string!"

@dispatch
def f(x: int):
    return "This is an integer!"

@dispatch
def f(x: Number):
    return "This is a number, but I don't know which type."
```

Sections: Plum: Multiple Dispatch in Python, Documentation, What's This?, Projects Using Plum

</details>

### pyannote-core

Advanced data structures for handling temporal segments with attached labels

`pip install pyannote-core` · installs (wheel) · licence: not stated · rank 3488 · last release 2026-10-15 · [PyPI](https://pypi.org/project/pyannote-core/)

<details><summary>README extract</summary>

> advanced data structures for handling and visualizing temporal segments with attached labels.

</details>

### pathlib-mate

An extended and more powerful pathlib.

`pip install pathlib-mate` · installs (wheel) · licence: MIT License · rank 3510 · last release 2024-01-22 · [PyPI](https://pypi.org/project/pathlib-mate/)

<details><summary>README extract</summary>

pathlib is an awesome library handling path in different OS. And it's been added into standard library since Python3.4. `pathlib_mate` gives extensive methods and attributes, makes `pathlib` more powerful and user-friendly.

Features:

Convenient Attribute Accessor:

Powerful Path Search:

Eazy to use File / Dir Operation:

Atomic Write Support: ...

Example:
```python
>>> p = Path("/Users/username/test.py").

>>> p.abspath
/Users/username/test.py

>>> p.basename
test.py

>>> p.fname
test

>>> p.ext
.py

>>> p.dirname
username

>>> p.dirpath
/Users/username

>>> p.size
1500

>>> p.size_in_text
1.46 KB

>>> p.create_datetime
datetime(2018, 1, 15, 8, 30, 15)

>>> p.md5
415f12f07a7e01486cc82856621e05bf

...
```

</details>

### pdf2docx

Open source Python library converting pdf to docx.

`pip install pdf2docx` · installs (wheel) · licence: MIT · rank 3512 · last release 2026-05-01 · [PyPI](https://pypi.org/project/pdf2docx/)

### pyannote-database

Interface to multimedia databases and experimental protocols

`pip install pyannote-database` · installs (wheel) · licence: not stated · rank 3513 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pyannote-database/)

<details><summary>README extract</summary>

Reproducible experimental protocols for multimedia (audio, video, text) database.

- pyannote-database
 - Definitions
 - Configuration file
 - Data loaders
 - Preprocessors
 - `FileFinder`
 - Tasks
 - Collections
 - Segmentation
 - Speaker diarization
 - Speaker verification
 - Versioning
 - Meta-protocols and requirements
 - Plugins
 - API
 - ...

Example:
```python
from pyannote.database import registry

registry.load_database("/path/to/database.yml")
```

Sections: pyannote-database, Definitions, Configuration file, Data loaders, Preprocessors, `FileFinder`, Tasks, Collections, Segmentation, Speaker diarization, Speaker verification, Versioning, Plugins, API

</details>

### pyannote-metrics

A toolkit for reproducible evaluation, diagnostic, and error analysis of speaker diarization systems

`pip install pyannote-metrics` · installs (wheel) · licence: not stated · rank 3518 · last release 2026-10-16 · [PyPI](https://pypi.org/project/pyannote-metrics/)

<details><summary>README extract</summary>

> a toolkit for reproducible evaluation, diagnostic, and error analysis of speaker diarization systems

An overview of `pyannote.metrics` is available as an InterSpeech 2017 paper: it is recommended to read it first, to quickly get an idea whether this tool is for you.

</details>

### python-semantic-release

Automatic Semantic Versioning for Python projects

`pip install python-semantic-release` · installs (wheel) · licence: MIT · rank 3531 · last release 2026-09-22 · [PyPI](https://pypi.org/project/python-semantic-release/) · [docs](https://python-semantic-release.readthedocs.io) · [source](http://github.com/python-semantic-release/python-semantic-release.git)

### polling2

Updated polling utility with many configurable options

`pip install polling2` · installs (wheel) · licence: MIT License · rank 3536 · last release 2021-07-19 · [PyPI](https://pypi.org/project/polling2/)

<details><summary>README extract</summary>

_Never write another polling function again!_

Documentation available at Read the Docs

You can install the package from Pypi

Polling2 is a powerful python utility used to wait for a function to return a certain expected condition.

Some possible uses cases include:

- Wait for API response to return with code 200 ...

Example:
```python
# This call will wait until the file exists, checking every 0.1 seconds and stopping after 3 seconds have elapsed
file_handle = polling2.poll(
    lambda: open('/tmp/myfile.txt'),
    ignore_exceptions=(IOError,),
    timeout=3,
    step=0.1)

# Polling will return the value of your polling function, so you can now interact with it
...
```

Sections: polling2, Example, API and user guide at Read the Docs

</details>

### python-monkey-business

Utility functions for monkey-patching python code

`pip install python-monkey-business` · installs (wheel) · licence: BSD License · rank 3538 · last release 2024-07-11 · [PyPI](https://pypi.org/project/python-monkey-business/)

<details><summary>README extract</summary>

About

python-monkey-business is a package that provides a decorator for
monkey-patching python functions at runtime.

Installation

Using pip::

 pip install python-monkey-business

Or, to install from source::

 pip install -e git+

If the source is already checked out, use setuptools::

 python setup.py develop

Usage ...

</details>

### python-lsp-jsonrpc

JSON RPC 2.0 server library

`pip install python-lsp-jsonrpc` · installs (wheel) · licence: MIT License · rank 3546 · last release 2023-09-23 · [PyPI](https://pypi.org/project/python-lsp-jsonrpc/)

<details><summary>README extract</summary>

A Python 3.8+ server implementation of the JSON RPC 2.0 protocol. This library has been pulled out of the Python LSP Server project.

Sections: Python JSON RPC Server, Examples

</details>

### polyline

A Python implementation of Google's Encoded Polyline Algorithm Format.

`pip install polyline` · installs (wheel) · licence: not stated · rank 3547 · last release 2025-12-02 · [PyPI](https://pypi.org/project/polyline/) · [source](https://github.com/frederickjansen/polyline)

<details><summary>README extract</summary>

`polyline` is a Python implementation of Google's Encoded Polyline Algorithm
Format. It is essentially a port of Mapbox polyline with some additional features.

Example:
```python
import polyline
polyline.encode([(38.5, -120.2), (40.7, -120.9), (43.2, -126.4)], 5)
```

Sections: polyline, API Documentation, Encoding, Decoding, Documentation, Versioning, Publishing

</details>

### primePy

This module contains several useful functions to work with prime numbers. from primePy import primes

`pip install primePy` · installs (wheel) · licence: MIT License · rank 3549 · last release 2018-05-29 · [PyPI](https://pypi.org/project/primePy/)

<details><summary>README extract</summary>

This module contains several useful functions to work with prime numbers. For example, extracting all the prime factors (with multiplicity) of a positive integer reasonably fast. Following the list of all functions and their running time.

Example:
```python
>>>pip install primePy
```

Sections: primes from module primePy, Getting started, Available methods, Demonstration, Small numbers, A little bigger numbers, Suggestions

</details>

### pagerduty

Clients for PagerDuty's Public APIs

`pip install pagerduty` · installs (wheel) · licence: not stated · rank 3554 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pagerduty/) · [docs](https://pagerduty.github.io/python-pagerduty) · [source](https://github.com/PagerDuty/python-pagerduty)

### python3-xlib

Python3 X Library

`pip install python3-xlib` · installs from source (sdist only) · licence: GPLv2 · rank 3562 · last release 2014-05-31 · [PyPI](https://pypi.org/project/python3-xlib/)

_README extract left out: share-alike licence._

### python-consul

Python client for Consul (http://www.consul.io/)

`pip install python-consul` · installs (wheel) · licence: MIT License · rank 3578 · last release 2018-07-09 · [PyPI](https://pypi.org/project/python-consul/)

<details><summary>README extract</summary>

Read the Docs

Features:
* Add Operator endpoint (thanks @bantonj!)

Example:
```python
import consul

c = consul.Consul()

# poll a key for updates
index = None
while True:
    index, data = c.kv.get('foo', index=index)
    print data['Value']

# in another process
c.kv.put('foo', 'bar')
```

Sections: Python client for Consul.io, Documentation, Example, Mailing List, Issue Labels, PRs, . All current tests pass, including flake8, . To add tests for your new features, if reasonable, 1.1.0, 1.0.1, 0.7.2, 0.7.1, 0.7.0, Features

</details>

### ptpython

Python REPL build on top of prompt_toolkit

`pip install ptpython` · installs (wheel) · licence: BSD License · rank 3615 · last release 2025-11-20 · [PyPI](https://pypi.org/project/ptpython/) · [source](https://github.com/prompt-toolkit/ptpython)

<details><summary>README extract</summary>

*A better Python REPL*

Ptpython is an advanced Python REPL. It should work on all
Python versions from 2.6 up to 3.11 and work cross platform (Linux,
BSD, OS X and Windows).

Note: this version of ptpython requires at least Python 3.6. Install ptpython
2.0.5 for older Python versions.

Features:
- Syntax highlighting.
- Multiline editing (the up arrow works).
- Autocompletion.
- Mouse support. [1]
- Support for color schemes.
- Support for bracketed paste [2].
- Both Vi and Emacs key bindings. ...

Example:
```python
from ptpython.utils import ptrepr_to_repr
from prompt_toolkit.formatted_text import HTML

@ptrepr_to_repr
class MyClass:
    def pt_repr(self):
        return HTML('<yellow>Hello world!</yellow>')
```

...

</details>

### pytest-watch

Local continuous test runner with pytest and watchdog.

`pip install pytest-watch` · installs from source (sdist only) · licence: MIT · rank 3625 · last release 2018-05-20 · [PyPI](https://pypi.org/project/pytest-watch/)

<details><summary>README extract</summary>

Current version on PyPI
Say Thanks!

pytest-watch a zero-config CLI tool that runs
pytest, and re-runs it when a file in your
project changes. It beeps on failures and can run arbitrary commands on
each passing and failing test run. ...

Example:
```python
# custom_pytest_runner.py

import sys
import pytest

print('py.test exited with code:', pytest.main(sys.argv[1:]))
```

Sections: pytest-watch – Continuous pytest runner, Motivation, Usage, Configuration, Alternatives

</details>

### pyrage

(no summary)

`pip install pyrage` · installs (wheel) · licence: not stated · rank 3629 · last release 2026-08-23 · [PyPI](https://pypi.org/project/pyrage/)

<details><summary>README extract</summary>

Python bindings for the Rust implementation of `age`.

* Installation
* Usage
* Development
* Licensing

Example:
```python
from pyrage import x25519

ident = x25519.Identity.generate()

# returns the public key
ident.to_public()

# returns the private key
str(ident)
```

Sections: pyrage, Index, Usage, Identity generation (x25519 only), Identity-based encryption and decryption, Passphrase encryption and decryption, Licensing

</details>

### pyannote-pipeline

Tunable pipelines

`pip install pyannote-pipeline` · installs (wheel) · licence: not stated · rank 3654 · last release 2026-10-14 · [PyPI](https://pypi.org/project/pyannote-pipeline/)

<details><summary>README extract</summary>

Example:
```python
>>> # shamelessly stolen from
...
... import numpy as np
>>> from sklearn import datasets
...
>>> np.random.seed(0)
...
>>> n_samples = 1500
>>> noisy_circles = datasets.make_circles(n_samples=n_samples, factor=.5,
...                                       noise=.05)
>>> noisy_moons = datasets.make_moons(n_samples=n_samples, noise=.05)
...
```

Sections: Tutorial, Multi-objective optimization, Documentation

</details>

### perplexityai

(no summary)

`pip install perplexityai` · installs (wheel) · licence: Apache Software License · rank 3676 · last release 2026-10-23 · [PyPI](https://pypi.org/project/perplexityai/) · [source](https://github.com/perplexityai/perplexity-py)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Perplexity Python library provides convenient access to the Perplexity REST API from any Python 3.10+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx. ...

Example:
```python
import os
import asyncio
from perplexity import AsyncPerplexity

client = AsyncPerplexity(
    api_key=os.environ.get("PERPLEXITY_API_KEY"),  # This is the default and can be omitted
)

async def main() -> None:
    stream_chunk = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
...
```

...

</details>

### python-sat

A Python library for prototyping with SAT oracles

`pip install python-sat` · installs (wheel) · licence: MIT · rank 3728 · last release 2026-11-05 · [PyPI](https://pypi.org/project/python-sat/)

<details><summary>README extract</summary>

A Python library providing a simple interface to a number of state-of-art
Boolean satisfiability (SAT) solvers and a few types of cardinality and
pseudo-Boolean encodings. The purpose of PySAT is to enable researchers
working on SAT and its applications and generalizations to easily prototype
with SAT oracles in Python while exploiting ...

</details>

### prawcore

Low-level communication layer for PRAW 4+.

`pip install prawcore` · installs (wheel) · licence: BSD License · rank 3752 · last release 2026-06-13 · [PyPI](https://pypi.org/project/prawcore/) · [docs](https://prawcore.readthedocs.io/) · [source](https://github.com/praw-dev/prawcore)

<details><summary>README extract</summary>

prawcore is a low-level communication layer used by PRAW 4+.

Example:
```python
# !/usr/bin/env python
import os
import pprint
import prawcore

authenticator = prawcore.TrustedAuthenticator(
    client_id=os.environ["PRAWCORE_CLIENT_ID"],
    client_secret=os.environ["PRAWCORE_CLIENT_SECRET"],
    requestor=prawcore.Requestor(user_agent="YOUR_VALID_USER_AGENT"),
)
...
```

Sections: prawcore, Execution Example, Documentation, Depending on prawcore, setup.py, requirements.txt

</details>

### pytest-freezer

Pytest plugin providing a fixture interface for spulec/freezegun

`pip install pytest-freezer` · installs (wheel) · licence: MIT License · rank 3757 · last release 2024-12-12 · [PyPI](https://pypi.org/project/pytest-freezer/)

<details><summary>README extract</summary>

Pytest plugin providing a fixture interface for freezegun.

Example:
```python
def test_frozen_date(freezer):
    now = datetime.now()
    time.sleep(1)
    later = datetime.now()
    assert now == later
```

Sections: pytest-freezer, Usage

</details>

### pyquery

A jquery-like library for python

`pip install pyquery` · installs (wheel) · licence: BSD · rank 3762 · last release 2026-07-27 · [PyPI](https://pypi.org/project/pyquery/)

<details><summary>README extract</summary>

pyquery allows you to make jquery queries on xml documents.
The API is as much as possible similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

This is not (or at least not yet) a library to produce or interact with
javascript code. ...

Example:
```python
>>> from pyquery import PyQuery as pq
>>> from lxml import etree
>>> import urllib
>>> d = pq("")
>>> d = pq(etree.fromstring(""))
>>> d = pq(url=your_url)
>>> d = pq(url=your_url,
...        opener=lambda url, **kw: urlopen(url).read())
>>> d = pq(filename=path_to_html_file)
```

...

</details>

### python-lsp-server

Python Language Server for the Language Server Protocol

`pip install python-lsp-server` · installs (wheel) · licence: MIT · rank 3769 · last release 2026-07-27 · [PyPI](https://pypi.org/project/python-lsp-server/)

<details><summary>README extract</summary>

A Python 3.9+ implementation of the Language Server Protocol.

Sections: Python LSP Server, 3rd Party Plugins, Configuration, LSP Server Features

</details>

### pybacklogpy

A library for backlog api

`pip install pybacklogpy` · installs (wheel) · licence: Apache Software License · rank 3785 · last release 2021-09-18 · [PyPI](https://pypi.org/project/pybacklogpy/)

<details><summary>README extract</summary>

BacklogAPI を Python から簡単に呼べるようにラップしたものです。

- `Python 3.5` 以上
 - `typing` モジュールを使用しているため
 - 開発およびテスト環境は `Python 3.7.3` を使用

Example:
```python
from pybacklogpy.BacklogConfigure import BacklogComConfigure
from pybacklogpy.Issue import Issue

# Configure クラスのインスタンスを生成
config = BacklogComConfigure(space_key='kitadakyou',
                             api_key='qwertyuiopasdfghjklzxcvbnmqazwsxedcrfvtgbyhnujmikolp')

issue_api = Issue(config)  # API を呼ぶクラスのコンストラクタ引数として Configure クラスのインスタンスは使用可能
...
```

Sections: PyBacklogPy, これは何？, 必須環境, 使い方, インストール, ドメインおよびシークレットキーの登録, プログラム上で設定する場合, 設定ファイルで指定する場合, モジュールを読み込み、インスタンス生成, API を呼ぶ, 返り値を見る, ファイルの取得, バグを見つけたら, おまけ: なんでこんな名前なの？

</details>

### paypal-checkout-serversdk

Deprecated

`pip install paypal-checkout-serversdk` · installs (wheel) · licence: Apache Software License · rank 3809 · last release 2023-10-24 · [PyPI](https://pypi.org/project/paypal-checkout-serversdk/)

### proxy-protocol

PROXY protocol library with asyncio server implementation

`pip install proxy-protocol` · installs (wheel) · licence: MIT License · rank 3817 · last release 2024-04-27 · [PyPI](https://pypi.org/project/proxy-protocol/)

<details><summary>README extract</summary>

Sections: Specification, API Reference, Docker Image, Server Usage, Echo Server, Proxy Server, Type Hinting

</details>

### pyannote-audio

State-of-the-art speaker diarization toolkit

`pip install pyannote-audio` · installs (wheel) · licence: not stated · rank 3832 · last release 2026-06-30 · [PyPI](https://pypi.org/project/pyannote-audio/)

<details><summary>README extract</summary>

`pyannote.audio` is an open-source toolkit written in Python for speaker diarization. Based on PyTorch machine learning framework, it comes with state-of-the-art pretrained models and pipelines, that can be further finetuned to your own data for even better performance.

Features:
- :exploding_head: state-of-the-art performance (see Benchmark)
- :hugs: pretrained pipelines (and models) on :hugs: model hub
- :rocket: built-in support for pyannoteAI premium speaker diarization
- :snake: Python-first API ...

Example:
```python
from pyannote.audio import Pipeline

# Precision-2 premium speaker diarization service
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-precision-2", token="PYANNOTEAI_API_KEY")

output = pipeline("audio.wav")  # runs on pyannoteAI servers

...

</details>

### pixelmatch

A pixel-level image comparison library.

`pip install pixelmatch` · installs (wheel) · licence: OSI Approved · rank 3834 · last release 2026-03-07 · [PyPI](https://pypi.org/project/pixelmatch/) · [source](https://github.com/whtsky/pixelmatch-py)

<details><summary>README extract</summary>

A fast pixel-level image comparison library, originally created to compare screenshots in tests.
Now with additional support of PIL.Image instances
Python port of

Features accurate anti-aliased pixels detection
and perceptual color difference metrics.

Implements ideas from the following papers: ...

Example:
```python
from pixelmatch import pixelmatch

num_diff_pixels = pixelmatch(img1, img2, 800, 600, diff, threshold=0.1)
```

Sections: pixelmatch-py, Example usage, PIL.Image comparison, Raw Image Data Comparison, API, contrib.PIL.pixelmatch, Example output, v0.4.0, v0.3.1, v0.3.0, v0.2.4, v0.2.3, v0.2.2, v0.2.1

</details>

### pytest-anyio

The pytest anyio plugin is built into anyio. You don't need this package.

`pip install pytest-anyio` · installs (wheel) · licence: MIT License · rank 3868 · last release 2021-06-29 · [PyPI](https://pypi.org/project/pytest-anyio/)

### pyspark-client

Python Spark Connect client for Apache Spark

`pip install pyspark-client` · installs from source (sdist only) · licence: Apache-2.0 · rank 3873 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyspark-client/)

<details><summary>README extract</summary>

Spark is a unified analytics engine for large-scale data processing. It provides
high-level APIs in Scala, Java, Python, and R, and an optimized engine that
supports general computation graphs for data analysis. ...

Sections: Apache Spark, Online Documentation, Python Packaging, Python Requirements

</details>

### pyicumessageformat

An unopinionated parser for ICU MessageFormat.

`pip install pyicumessageformat` · installs (wheel) · licence: MIT License · rank 3891 · last release 2021-09-22 · [PyPI](https://pypi.org/project/pyicumessageformat/)

<details><summary>README extract</summary>

An unopinionated library for parsing ICU MessageFormat messages into both
ASTs and, optionally, token lists.

This library is mainly a re-implementation of the JavaScript library
format-message-parse
with a few extra configuration flags.

format-message-parse
and `pyicumessageformat` are both licensed MIT.

Example:
```python
from pyicumessageformat import Parser

# The following are the default values for the various available
# settings for the Parser.
parser = Parser({
    # Whether or not to include indices on placeholder objects.
    'include_indices': False,

    # Maximum depth limits the nesting depth of sub-messages. This is
...
```

Sections: pyicumessageformat, Parser Options, Require Other, Tags, Parsing, `parse(input: str, tokens?: list) -> AST`, AST Format

</details>

### pytest-messenger

Pytest to Slack reporting plugin

`pip install pytest-messenger` · installs (wheel) · licence: MIT License · rank 3896 · last release 2022-11-24 · [PyPI](https://pypi.org/project/pytest-messenger/)

<details><summary>README extract</summary>

ex pytest-slack

Pytest to IM reporting plugin

Supported messengers and links to the usage:

* Slack
* Ding Talk
* Telegram - soon

* Requests
* Python >= 3.6

Sections: pytest-messenger, Requirements, Issues, 1.0.1 (2019-04-18), 2.1.2 (2020-02-10)

</details>

### pathy

pathlib.Path subclasses for local and cloud bucket storage

`pip install pathy` · installs (wheel) · licence: Apache-2.0 · rank 3905 · last release 2026-04-11 · [PyPI](https://pypi.org/project/pathy/)

<details><summary>README extract</summary>

Pathy is a practical Python package with type annotations tailored for managing Cloud Bucket storage through a Path-like interface. It has an intuitive API and supports your favorite cloud providers, facilitating file transfers between local systems and remote buckets. ...

Example:
```python
from pathy import Pathy, use_fs

# Use the local file-system for quicker development
use_fs()

# Create a bucket
Pathy("gs://my_bucket").mkdir(exist_ok=True)

# An excellent blob
greeting = Pathy(f"gs://my_bucket/greeting.txt")

# But it doesn't exist yet
assert not greeting.exists()

# Create it by writing some text
...
```

Sections: Pathy, 🚀 Quickstart, 🔐 Setup Credentials, Google Cloud Storage, Amazon S3, Azure, ♻️ Semantic Versioning, 📖 API, exists, fluid, from_bucket, glob, is_dir

</details>

### py3dbp

3D Bin Packing

`pip install py3dbp` · installs from source (sdist only) · licence: MIT License · rank 3924 · last release 2020-07-04 · [PyPI](https://pypi.org/project/py3dbp/)

<details><summary>README extract</summary>

3D Bin Packing implementation based on this paper. The code is based on gedex implementation in Go.

Features:
1. Sorting Bins and Items:

Example:
```python
from py3dbp import Packer, Bin, Item

packer = Packer()

packer.add_bin(Bin('small-envelope', 11.5, 6.125, 0.25, 10))
packer.add_bin(Bin('large-envelope', 15.0, 12.0, 0.75, 15))
packer.add_bin(Bin('small-box', 8.625, 5.375, 1.625, 70.0))
packer.add_bin(Bin('medium-box', 11.0, 8.5, 5.5, 70.0))
...
```

Sections: 3D Bin Packing, Features, Basic Explanation, Usage, Versioning, Credit

</details>

### pytoolconfig

Python tool configuration

`pip install pytoolconfig` · installs (wheel) · licence: LGPL-3.0-or-later · rank 3927 · last release 2024-01-11 · [PyPI](https://pypi.org/project/pytoolconfig/)

_README extract left out: share-alike licence._

### python-qpid-proton

An AMQP based messaging library.

`pip install python-qpid-proton` · installs from source (sdist only) · licence: Apache-2.0 · rank 3950 · last release 2026-10-27 · [PyPI](https://pypi.org/project/python-qpid-proton/)

<details><summary>README extract</summary>

This module provides a Python binding to the Proton AMQP messaging toolkit.

Qpid Proton is a high-performance, lightweight messaging library. It
can be used in the widest range of messaging applications, including
brokers, client libraries, routers, bridges, proxies, and more. ...

</details>

### py-money

Money module for python

`pip install py-money` · installs (wheel) · licence: MIT License · rank 3954 · last release 2020-01-29 · [PyPI](https://pypi.org/project/py-money/)

<details><summary>README extract</summary>

Money class for Python 3. Unlike other Python money classes, this class enforces that all monetary amounts are represented with the correct number of decimal places for the currency. For example, 3.678 USD is invalid, as is 5.5 JPY.

Example:
```python
>>> from money.money import Money
>>> from money.currency import Currency
>>> m = Money('9.95', Currency.GBP)
>>> m
GBP 9.95
```

Sections: py-money, Usage, Is this the money library for me?, Future improvements

</details>

### pin

A fast and flexible implementation of Rigid Body Dynamics algorithms and their analytical derivatives

`pip install pin` · installs (wheel) · licence: BSD-3-Clause · rank 3964 · last release 2026-07-08 · [PyPI](https://pypi.org/project/pin/)

<details><summary>README extract</summary>

Pinocchio is open-source software actively developed by the Willow team at Inria in the lovely city of Paris.
Pinocchio instantiates state-of-the-art Rigid Body Algorithms for poly-articulated systems, building upon and revisiting the foundational algorithms introduced by Roy Featherstone. ...

Sections: Pinocchio main features, Documentation, Examples, Tutorials, Pinocchio continuous integrations, Performances, Conda, Docker, ROS, Visualization, Citing Pinocchio, Questions and Issues, Core-dev team, Open-source projects relying on Pinocchio

</details>

### panzi-json-logic

Pure Python 3 JsonLogic and CertLogic implementation.

`pip install panzi-json-logic` · installs (wheel) · licence: MIT License · rank 3980 · last release 2021-09-12 · [PyPI](https://pypi.org/project/panzi-json-logic/)

<details><summary>README extract</summary>

Pure Python 3 JsonLogic and
CertLogic
implementation.

The JsonLogic format is designed to allow you to share rules (logic) between
front-end and back-end code (regardless of language difference), even to store
logic along with a record in a database. ...

Example:
```python
from json_logic import jsonLogic
jsonLogic( { "==" : [1, 1] } )
# True
```

Sections: panzi-json-logic, Simple, Compound, Data-Driven, Always and Never, CertLogic, `now`, `parseTime`, `timeSince`, `hours`, `days`, `combinations`, `zip`

</details>

### paddlepaddle

Parallel Distributed Deep Learning

`pip install paddlepaddle` · does not install on CPython 3.14 · licence: Apache Software License · rank 4020 · last release 2026-03-26 · [PyPI](https://pypi.org/project/paddlepaddle/)

<details><summary>README extract</summary>

Welcome to the PaddlePaddle GitHub.

PaddlePaddle, as the only independent R&D deep learning platform in China, has been officially open-sourced to professional communities since 2016. ...

Sections: PREQUISTIES, On Windows, On Linux, On macOS, cpu, gpu, specific version cuda, FOUR LEADING TECHNOLOGIES, Documentation, Communication

</details>

### pystray

Provides systray integration

`pip install pystray` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 4031 · last release 2023-09-17 · [PyPI](https://pypi.org/project/pystray/)

_README extract left out: share-alike licence._

### py-grpc-prometheus

Python gRPC Prometheus Interceptors

`pip install py-grpc-prometheus` · installs (wheel) · licence: not stated · rank 4039 · last release 2024-02-29 · [PyPI](https://pypi.org/project/py-grpc-prometheus/)

<details><summary>README extract</summary>

Instrument library to provide prometheus metrics similar to:

Example:
```python
import grpc
from py_grpc_prometheus.prometheus_client_interceptor import PromClientInterceptor

channel = grpc.intercept_channel(grpc.insecure_channel('server:6565'),
                                         PromClientInterceptor())
# Start an end point to expose metrics.
start_http_server(metrics_port)
```

Sections: py-grpc-prometheus, Server side, Client side, How to use, Histograms, Server Side, Client Side, Legacy metrics, server side, client side, How to run and test, TODO

</details>

### pyleak

Detect leaked asyncio tasks, threads, and event loop blocking in Python. Inspired by Go's goleak

`pip install pyleak` · installs (wheel) · licence: not stated · rank 4081 · last release 2026-01-29 · [PyPI](https://pypi.org/project/pyleak/) · [source](https://github.com/deepankarm/pyleak)

<details><summary>README extract</summary>

Detect leaked asyncio tasks, threads, and event loop blocking in Python. Inspired by Go's goleak.

Features:
AsyncIO Tasks: Leaked tasks can cause memory leaks, prevent graceful shutdown, and make debugging difficult.

Threads: Leaked threads consume system resources and can prevent proper application termination. ...

Example:
```python
import asyncio
from pyleak import no_task_leaks, no_thread_leaks, no_event_loop_blocking

# Detect leaked asyncio tasks
async def main():
    async with no_task_leaks():
        asyncio.create_task(asyncio.sleep(10))  # This will be detected
        await asyncio.sleep(0.1)

# Detect leaked threads
def sync_main():
    with no_thread_leaks():
...
```

...

</details>

### pystoi

Computes Short Term Objective Intelligibility measure

`pip install pystoi` · installs (wheel) · licence: MIT License · rank 4084 · last release 2023-12-29 · [PyPI](https://pypi.org/project/pystoi/)

<details><summary>README extract</summary>

Implementation of the classical and extended Short Term Objective Intelligibility measures

Intelligibility measure which is highly correlated with the intelligibility of degraded speech signals, e.g., due to additive noise, single/multi-channel noise reduction, binary masking and vocoded speech as in CI simulations. ...

Example:
```python
import soundfile as sf
from pystoi import stoi

clean, fs = sf.read('path/to/clean/audio')
denoised, fs = sf.read('path/to/denoised/audio')

# Clean and den should have the same length, and be 1D
d = stoi(clean, denoised, fs, extended=False)
```

Sections: Python implementation of STOI, Usage, Running the Octave tests, References

</details>

### pydoclint

A Python docstring linter that checks arguments, returns, yields, and raises sections

`pip install pydoclint` · installs (wheel) · licence: MIT License · rank 4106 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pydoclint/)

<details><summary>README extract</summary>

_pydoclint_ is the go-to linter for making sure Python docstrings match the
code they describe, with

monthly downloads.

It checks arguments, return values, yields, raises, class attributes, and type
hints in numpy,
Google,
and
Sphinx
styles, with a few
minor deviations.

Full documentation:
jsh9.github.io/pydoclint.

<!--TOC-->

______________ ...

Sections: pydoclint, 1. Why _pydoclint_?, 1.1. Docstrings that stay true to the code, 1.2. Built for the age of AI-assisted coding, 1.3. Highly configurable, 1.4. _pydoclint_ vs Ruff's `DOC` rules, 1.5. How to adopt _pydoclint_?, 3. Usage, 3.1. As a native command line tool, 3.2. As a _flake8_ plugin, 3.3. Native vs _flake8_, 3.4. As a pre-commit hook, 3.4.1. Native mode, 3.4.2. As a _flake8_ plugin

</details>

### python-quickbooks

A Python library for accessing the QuickBooks API.

`pip install python-quickbooks` · installs (wheel) · licence: MIT License · rank 4111 · last release 2025-04-16 · [PyPI](https://pypi.org/project/python-quickbooks/)

<details><summary>README extract</summary>

A Python 3 library for accessing the Quickbooks API. Complete rework of
quickbooks-python.

These instructions were written for a Django application. Make sure to
change it to whatever framework/method you're using.
You can find additional examples of usage in Integration tests folder. ...

</details>

### pulumi-docker

A Pulumi package for interacting with Docker in Pulumi programs

`pip install pulumi-docker` · installs (wheel) · licence: Apache-2.0 · rank 4128 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pulumi-docker/) · [source](https://github.com/pulumi/pulumi-docker)

<details><summary>README extract</summary>

The Docker resource provider for Pulumi lets you manage Docker resources in your cloud programs. To use
this package, please install the Pulumi CLI first.

Sections: Docker Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Reference

</details>

### pylink-square

Python interface for SEGGER J-Link.

`pip install pylink-square` · installs (wheel) · licence: Apache 2.0 · rank 4135 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pylink-square/)

<details><summary>README extract</summary>

Python interface for the SEGGER J-Link.

- Python >= 3.7
- GNU ARM Embedded
 Toolchain (for functional
 tests)
- SEGGER J-Link Tools >=
 6.0b

Example:
```python
import pylink

if name == 'main':
   serial_no = '123456789'
   jlink = pylink.JLink()

   # Open a connection to your J-Link.
   jlink.open(serial_no)

   # Connect to the target device.
   jlink.connect('device', verbose=True)

   # Do whatever you want from here on in.
   jlink.flash(firmware, 0x0)
   jlink.reset()
```

Sections: pylink, Requirements, External Dependencies, On Mac, On Windows, On Linux, Usage, Troubleshooting, Documentation, Coverage

</details>

### pulumi-datadog

A Pulumi package for creating and managing Datadog resources.

`pip install pulumi-datadog` · installs (wheel) · licence: Apache-2.0 · rank 4138 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pulumi-datadog/) · [source](https://github.com/pulumi/pulumi-datadog)

<details><summary>README extract</summary>

The Datadog resource provider for Pulumi lets you configure Datadog resources in your cloud programs. To use
this package, please install the Pulumi CLI first.

Sections: Datadog Provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pytrends

Pseudo API for Google Trends

`pip install pytrends` · installs (wheel) · licence: Apache Software License · rank 4151 · last release 2023-04-13 · [PyPI](https://pypi.org/project/pytrends/)

<details><summary>README extract</summary>

Unofficial API for Google Trends

Allows simple interface for automating downloading of reports from Google Trends.
Only good until Google changes their backend again :-P. When that happens feel free to contribute!

Looking for maintainers! Please open an issue with a method of contacting you if you're interested.

Sections: pytrends, Introduction, Requirements, API, Connect to Google, Build Payload, API Methods, Common API parameters, Interest Over Time, Multirange Interest Over Time, Historical Hourly Interest, Interest by Region, Related Topics, Related Queries

</details>

### pulumi-docker-build

A Pulumi provider for building modern Docker images with buildx and BuildKit.

`pip install pulumi-docker-build` · installs (wheel) · licence: Apache-2.0 · rank 4184 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pulumi-docker-build/) · [source](https://github.com/pulumi/pulumi-docker-build)

<details><summary>README extract</summary>

A Pulumi provider for building modern Docker images with buildx and BuildKit.

Not to be confused with the earlier
Docker provider, which is still
appropriate for managing resources unrelated to building images.

| Provider | Use cases |

| `@pulumi/docker-build` | Anything related to building images with `docker build`. ...

Sections: Docker-Build Resource Provider, Reference

</details>

### pyawscron

An AWS Cron Parser

`pip install pyawscron` · installs (wheel) · licence: BSD License · rank 4189 · last release 2024-08-14 · [PyPI](https://pypi.org/project/pyawscron/)

<details><summary>README extract</summary>

Main Branch Status

Develop Branch Status

A python port from a typescript project.

Example:
```python
from_dt = datetime.datetime(2021, 8, 7, 8, 30, 57, tzinfo=datetime.timezone.utc)
to_date = datetime.datetime(2021, 8, 7, 11, 30, 57, tzinfo=datetime.timezone.utc)

AWSCron.get_all_schedule_bw_dates(from_dt, to_date, '0/23 * * * ? *')

# Resulting list
[datetime.datetime(2021, 8, 7, 8, 46, tzinfo=datetime.timezone.utc),
...
```

Sections: pyawscron, AWS Cron Expressions, cron(fields), Wildcards, Iterative Use, Helper Methods, get_all_schedule_bw_dates, get_next_n_schedule, get_prev_n_schedule

</details>

### pretty-html-table

Make pandas dataframe looking pretty again

`pip install pretty-html-table` · installs (wheel) · licence: MIT License · rank 4214 · last release 2022-04-25 · [PyPI](https://pypi.org/project/pretty-html-table/)

<details><summary>README extract</summary>

`pretty_html_table` exists to convert a pandas DataFrame into a pretty html table for use in email. The intended target audience is anyone who needs to send reports via email and would like to make their tables look more attractive.

12 different color themes are available. ...

Features:
Output is ready to be sent via any Python package used to send emails. Insert the result of this package to the body of the email and voila.

Example:
```python
from O365 import Account

# Never hard code credentials or store them in a repo
# Use environmental variables instead

credentials = (o365credid, o365credpwd)
account = Account(credentials)

def send_email(account, to, subject, start, body, end):
    m = account.new_message()
    m.to.add(to)
    m.subject = subject
...

</details>

### PyMeta3

Pattern-matching language based on OMeta for Python 3 and 2

`pip install PyMeta3` · installs from source (sdist only) · licence: MIT License · rank 4281 · last release 2015-02-22 · [PyPI](https://pypi.org/project/PyMeta3/)

<details><summary>README extract</summary>

This is a fork of PyMeta 0.5.0 that supports Python 2 and 3.

Sections: PyMeta3, A Pattern-Matching Language Based on Python, Summary, How It Works, Basic syntax, Interface, Example Usage

</details>

### pygdbmi

Parse gdb machine interface output with Python

`pip install pygdbmi` · installs (wheel) · licence: MIT License · rank 4298 · last release 2023-01-29 · [PyPI](https://pypi.org/project/pygdbmi/)

<details><summary>README extract</summary>

Documentation

Source Code

Python (py) gdb machine interface (mi)

> GDB/MI is a line based machine oriented text interface to GDB and is activated by specifying using the --interpreter command line option (see Mode Options). ...

Example:
```python
from pygdbmi import gdbmiparser
from pprint import pprint
response = gdbmiparser.parse_response('^done,bkpt={number="1",type="breakpoint",disp="keep", enabled="y",addr="0x08048564",func="main",file="myprog.c",fullname="/home/myprog.c",line="68",thread-groups=["i1"],times="0"')
pprint(response)
pprint(response)
# Prints:
# {'message': 'done',
...
```

Sections: What's in the box?, Compatibility, Operating Systems, gdb versions, Examples, Programmatic Control Over gdb, Parsed Output Format, Similar projects, Projects Using pygdbmi

</details>

### pyserde

Yet another serialization library on top of dataclasses

`pip install pyserde` · installs (wheel) · licence: MIT License · rank 4307 · last release 2026-11-08 · [PyPI](https://pypi.org/project/pyserde/) · [source](https://github.com/yukinarit/pyserde)

<details><summary>README extract</summary>

Yet another serialization library on top of dataclasses, inspired by serde-rs.

 Guide🇬🇧 | ガイド🇯🇵 | API Reference | Examples

Features:
`pyserde` is a simple yet powerful serialization library on top of dataclasses. It allows you to convert Python objects to and from JSON, YAML, and other formats easily and efficiently. ...

Example:
```python
>>> to_json(Foo(i=10, s='foo', f=100.0, b=True))
'{"i":10,"s":"foo","f":100.0,"b":true}'
```

Sections: pyserde, Overview, Features, Extensions

</details>

### py-asciimath

A simple converter from ASCIIMath/MathML to LaTeX/MathML

`pip install py-asciimath` · installs (wheel) · licence: MIT License · rank 4314 · last release 2020-04-22 · [PyPI](https://pypi.org/project/py-asciimath/)

<details><summary>README extract</summary>

py_asciimath is a simple yet powerful Python module that:

* converts an ASCIIMath ex to LaTeX or MathML
* converts a LaTeX mathematical expression to ASCIIMath (soon also to MathML)
* converts a MathML string to LaTeX (the conversion is done thank to the XSLT MathML Library. ...

Example:
```python
from py_asciimath.translator.translator import (
    ASCIIMath2MathML,
    ASCIIMath2Tex,
    MathML2Tex,
    Tex2ASCIIMath
)

if name == "main":
    print("ASCIIMath to MathML")
    asciimath2mathml = ASCIIMath2MathML(log=False, inplace=True)
    parsed = asciimath2mathml.translate(
        r"e^x > 0 forall x in RR",
        displaystyle=True,
...
```

...

</details>

### phonemizer-fork

Simple text to phones converter for multiple languages

`pip install phonemizer-fork` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 4339 · last release 2025-01-30 · [PyPI](https://pypi.org/project/phonemizer-fork/) · [docs](https://bootphon.github.io/phonemizer/) · [source](https://github.com/bootphon/phonemizer)

_README extract left out: share-alike licence._

### pyshark

Python wrapper for tshark, allowing python packet parsing using wireshark dissectors

`pip install pyshark` · installs (wheel) · licence: MIT License · rank 4343 · last release 2023-04-26 · [PyPI](https://pypi.org/project/pyshark/)

<details><summary>README extract</summary>

Python wrapper for tshark, allowing python packet parsing using wireshark dissectors.

See for documentation.

</details>

### pyfarmhash

Google FarmHash Bindings for Python

`pip install pyfarmhash` · installs from source (sdist only) · licence: MIT License · rank 4366 · last release 2026-08-26 · [PyPI](https://pypi.org/project/pyfarmhash/)

### pulumi-cloudflare

A Pulumi package for creating and managing Cloudflare cloud resources.

`pip install pulumi-cloudflare` · installs (wheel) · licence: Apache-2.0 · rank 4374 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pulumi-cloudflare/) · [source](https://github.com/pulumi/pulumi-cloudflare)

<details><summary>README extract</summary>

The Cloudflare resource provider for Pulumi lets you use Cloudflare resources
in your cloud programs. To use this package, please install the Pulumi CLI
first.

Sections: Cloudflare Provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### python-pcapng

Library to read/write the pcap-ng format used by various packet sniffers.

`pip install python-pcapng` · installs (wheel) · licence: Apache Software License · rank 4386 · last release 2022-08-23 · [PyPI](https://pypi.org/project/python-pcapng/)

<details><summary>README extract</summary>

Python library to parse the pcap-ng format used by newer versions
of dumpcap & similar tools (wireshark, winpcap, ...).

If you prefer the RTD theme, or want documentation for any version
other than the latest, head here:

If you prefer the more comfortable, page-wide, default sphinx theme,
a documentation mirror is hosted on GitHub pages:

Features:
- I need to decently extract some information from a bunch of pcap-ng
 files, but apparently tcpdump has some problems reading those files,

 I couldn't find other nice tools nor Python bindings to a library
 able to parse this format, so.. ...

Example:
```python
from pcapng import FileScanner

with open('/tmp/mycapture.pcap', 'rb') as fp:
    scanner = FileScanner(fp)
    for block in scanner:
        pass  # do something with the block...
...

</details>

### Parsley

Parsing and pattern matching made easy.

`pip install Parsley` · installs (wheel) · licence: MIT License · rank 4392 · last release 2015-09-09 · [PyPI](https://pypi.org/project/Parsley/)

<details><summary>README extract</summary>

You can read further docs at:

Parsley is a parsing library for people who find parsers scary or
annoying. I wrote it because I wanted to parse a programming language,
and tools like PLY or ANTLR or Bison were very hard to understand and
integrate into my Python code. ...

Example:
```python
from parsley import makeGrammar
exampleGrammar = """
ones = '1' '1' -> 1
twos = '2' '2' -> 2
stuff = (ones | twos)+
"""
Example = makeGrammar(exampleGrammar, {})
g = Example("11221111")
result = g.stuff()
print result
```

Sections: Summary, How It Works, Basic syntax, Interface, Example Usage

</details>

### pycrdt-websocket

WebSocket connector for pycrdt

`pip install pycrdt-websocket` · installs (wheel) · licence: MIT License · rank 4393 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pycrdt-websocket/) · [source](https://github.com/y-crdt/pycrdt-websocket)

<details><summary>README extract</summary>

Pycrdt-websocket is an async WebSocket connector for pycrdt.

Documentation:

Source Code:

Pycrdt-websocket is a Python library for building WebSocket servers and clients that connect and synchronize shared documents.
It can be used to create collaborative web applications.

The following diagram illustrates a typical architecture. ...

</details>

### PyByteBuffer

A bytes manipulation library inspired by Java ByteBuffer

`pip install PyByteBuffer` · installs (wheel) · licence: GPL 3.0 · rank 4396 · last release 2020-12-28 · [PyPI](https://pypi.org/project/PyByteBuffer/)

_README extract left out: share-alike licence._

### pylev

A pure Python Levenshtein implementation that's not freaking GPL'd.

`pip install pylev` · installs (wheel) · licence: BSD License · rank 4398 · last release 2021-05-30 · [PyPI](https://pypi.org/project/pylev/)

<details><summary>README extract</summary>

A pure Python Levenshtein implementation that's not freaking GPL'd.

Based off the Wikipedia code samples at

* Python 2.7.X, Python 3.3+ or PyPy 1.6.0+

Example:
```python
import pylev
distance = pylev.levenshtein('kitten', 'sitting')
assert distance == 3
```

Sections: pylev, Requirements, Usage, Tests

</details>

### pulsar-client

Apache Pulsar Python client library

`pip install pulsar-client` · installs (wheel) · licence: Apache License v2.0 · rank 4412 · last release 2026-07-02 · [PyPI](https://pypi.org/project/pulsar-client/)

### prometheus-api-client

A small python api to collect data from prometheus

`pip install prometheus-api-client` · installs (wheel) · licence: MIT License · rank 4415 · last release 2026-04-13 · [PyPI](https://pypi.org/project/prometheus-api-client/)

<details><summary>README extract</summary>

A Python wrapper for the Prometheus http api and some tools for metrics processing.

Example:
```python
from prometheus_api_client import PrometheusConnect
prom = PrometheusConnect(url ="", disable_ssl=True)

# Get the list of all the metrics that the Prometheus host scrapes
prom.all_metrics()
```

Sections: prometheus-api-client, Links, Getting Started, Usage, Connecting and Collecting Metrics from a Prometheus host, Understanding the Metrics Data Fetched, Additional Metric Functions, Adding Metrics, Equating Metrics, Plotting Metric Objects, Getting Metrics Data as pandas DataFrames, Running tests, Code Styling and Linting

</details>

### pyspark-huggingface

A DataSource for reading and writing HuggingFace Datasets in Spark

`pip install pyspark-huggingface` · installs (wheel) · licence: Apache License 2.0 · rank 4485 · last release 2026-04-14 · [PyPI](https://pypi.org/project/pyspark-huggingface/)

<details><summary>README extract</summary>

A Spark Data Source for accessing 🤗 Hugging Face Datasets and 🤗 Storage Bucket:

- Stream datasets from Hugging Face as Spark DataFrames
- Select subsets and splits, apply projection and predicate filters
- Save Spark DataFrames as Parquet files to Hugging Face
- Fast deduped uploads
- Fully distributed ...

Example:
```python
import pyspark_huggingface
df = spark.read.format("huggingface").load("stanfordnlp/imdb")
```

Sections: Spark Data Source for Hugging Face Datasets, Usage with dataset repositories, Usage with storage buckets, Advanced, Fast deduped uploads, Backport

</details>

### pyrdfa3

pyRdfa distiller/parser library

`pip install pyrdfa3` · installs (wheel) · licence: W3C License · rank 4490 · last release 2026-01-17 · [PyPI](https://pypi.org/project/pyrdfa3/)

<details><summary>README extract</summary>

> Note: since I retired a few months ago I do not really maintain this package any more. I would be more than happy if an interested party was interested to take over. In the meantime, I have "archived" the repository to clearly signal that there is no maintenance. I would be happy to unarchive it and transfer ownership if someone is interested. ...

</details>

### pycdlib

Pure python ISO manipulation library

`pip install pycdlib` · installs (wheel) · licence: LGPL-2.1-only · rank 4502 · last release 2026-10-09 · [PyPI](https://pypi.org/project/pycdlib/)

_README extract left out: share-alike licence._

### pulumi-awsx

Pulumi Amazon Web Services (AWS) AWSX Components.

`pip install pulumi-awsx` · installs (wheel) · licence: Apache-2.0 · rank 4504 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pulumi-awsx/) · [source](https://github.com/pulumi/pulumi-awsx)

<details><summary>README extract</summary>

Pulumi's framework for Amazon Web Services (AWS) infrastructure.

To use this package, install the Pulumi CLI. For a streamlined Pulumi walkthrough, including language runtime installation and AWS configuration, see the AWS Guides. ...

Example:
```python
import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx

awsp = aws.Provider("awsp", opts=pulumi.ResourceOptions(version="6.36.0"))
lb = awsx.lb.ApplicationLoadBalancer("lb", opts=pulumi.ResourceOptions(providers={"aws": awsp}))
```

Sections: Pulumi AWS Infrastructure Components, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Node.js compatibility warnings, Custom AWS Provider Versions, Migration from 0.x to 1.0, Notable changes, References

</details>

### pydantic-collections

Collections of pydantic models

`pip install pydantic-collections` · installs (wheel) · licence: Apache 2 · rank 4531 · last release 2024-07-09 · [PyPI](https://pypi.org/project/pydantic-collections/)

<details><summary>README extract</summary>

The `pydantic-collections` package provides `BaseCollectionModel` class that allows you
to manipulate collections of pydantic models
(and any other types supported by pydantic).

- Python>=3.7
- pydantic>=1.8.2,<3.0

Example:
```python
from datetime import datetime

from pydantic import BaseModel
from pydantic_collections import BaseCollectionModel

class User(BaseModel):
    id: int
    name: str
    birth_date: datetime

class UserCollection(BaseCollectionModel[User]):
    pass

 user_data = [
        {'id': 1, 'name': 'Bender', 'birth_date': '2010-04-01T12:59:59'},
...
```

Sections: pydantic-collections, Requirements, Usage, Basic usage, Strict assignment validation, Using as a model field

</details>

### pyTelegramBotAPI

Python Telegram bot API.

`pip install pyTelegramBotAPI` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 4532 · last release 2026-10-17 · [PyPI](https://pypi.org/project/pyTelegramBotAPI/) · [docs](https://pytba.readthedocs.org) · [source](https://github.com/eternnoir/pyTelegramBotAPI)

_README extract left out: share-alike licence._

### pandas-flavor

The easy way to write your own Pandas flavor

`pip install pandas-flavor` · installs (wheel) · licence: MIT License · rank 4551 · last release 2025-11-22 · [PyPI](https://pypi.org/project/pandas-flavor/) · [source](https://github.com/pyjanitor-devs/pandas_flavor)

<details><summary>README extract</summary>

The easy way to write your own flavor of Pandas

Pandas 0.23 added a (simple) API for registering accessors with Pandas objects.

Pandas-flavor extends Pandas' extension API by:
1. adding support for registering methods as well.
2. making each of these functions backwards compatible with older versions of Pandas.

*What does this mean?* ...

Example:
```python
# my_flavor.py

import pandas_flavor as pf

@pf.register_dataframe_accessor('my_flavor')
class MyFlavor(object):

  def init(self, data):
    self._data = data

  def row_by_value(self, col, value):
    """Slice out row from DataFrame by a value."""
    return self._data[self._data[col] == value].squeeze()
```

Sections: Pandas Flavor, Register accessors, Register methods, Registered methods tracing, Available Methods, TL;DR

</details>

### pulumi-azure-native

A native Pulumi package for creating and managing Azure resources.

`pip install pulumi-azure-native` · installs (wheel) · licence: Apache-2.0 · rank 4580 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pulumi-azure-native/) · [source](https://github.com/pulumi/pulumi-azure-native)

<details><summary>README extract</summary>

The Azure Native provider for Pulumi lets you use Azure resources in your cloud programs.
This provider uses the Azure Resource Manager REST API directly and therefore provides full access to the ARM API.

The Azure Native provider is the recommended provider for projects targeting Azure.

To use this package, install the Pulumi CLI.

Sections: Native Azure Pulumi Provider, Node.js (JavaScript/TypeScript), Python, Go, .NET, Concepts, Configuring credentials, Building, Reference

</details>

### pybind11-stubgen

PEP 561 type stubs generator for pybind11 modules

`pip install pybind11-stubgen` · installs (wheel) · licence: BSD-3-Clause · rank 4595 · last release 2026-09-25 · [PyPI](https://pypi.org/project/pybind11-stubgen/) · [source](https://github.com/pybind/pybind11-stubgen)

<details><summary>README extract</summary>

About

Static analysis tools and IDE usually struggle to understand python binary extensions.
`pybind11-stubgen` generates stubs for python extensions to make them less opaque.

While the CLI tool includes tweaks to target modules compiled specifically
with pybind11 but it should work well with modules built with other libraries.

Usage ...

</details>

### pywhispercpp

Python bindings for whisper.cpp

`pip install pywhispercpp` · installs (wheel) · licence: MIT · rank 4641 · last release 2026-08-22 · [PyPI](https://pypi.org/project/pywhispercpp/) · [docs](https://absadiki.github.io/pywhispercpp/) · [source](https://github.com/absadiki/pywhispercpp)

<details><summary>README extract</summary>

Python bindings for whisper.cpp with a simple Pythonic API on top of it.

Example:
```python
from pywhispercpp.model import Model

model = Model('base.en')
segments = model.transcribe('file.wav')
for segment in segments:
    print(segment.text)
```

Sections: pywhispercpp, From source, Pre-built wheels, Quick start, Examples, CLI, GUI, Assistant, Advanced usage

</details>

### pyjwt-key-fetcher

Async library to fetch JWKs for JWT tokens

`pip install pyjwt-key-fetcher` · installs (wheel) · licence: BSD License · rank 4663 · last release 2024-08-07 · [PyPI](https://pypi.org/project/pyjwt-key-fetcher/) · [source](https://github.com/ioxiocom/pyjwt-key-fetcher)

<details><summary>README extract</summary>

Async library to fetch JWKs for JWT tokens.

This library is intended to be used together with
PyJWT to automatically verify keys signed by
for example OpenID Connect providers. ...

Example:
```python
import asyncio

import jwt

from pyjwt_key_fetcher import AsyncKeyFetcher

async def main():
    fetcher = AsyncKeyFetcher()
    # Token and options copied from
    #
...
```

Sections: pyjwt-key-fetcher, Usage, Example, Options, Limiting issuers, Adjusting caching, Loading configuration from a custom path, Using static configuration, Using your own HTTP Client

</details>

### pyannoteai-sdk

Official pyannoteAI Python SDK

`pip install pyannoteai-sdk` · installs (wheel) · licence: not stated · rank 4665 · last release 2026-01-14 · [PyPI](https://pypi.org/project/pyannoteai-sdk/)

<details><summary>README extract</summary>

Example:
```python
# instantiate client
from pyannoteai.sdk import Client
client = Client("your-api-key")

# upload conversation file
media_url = client.upload('/path/to/conversation.wav')

# submit a diarization job
job_id = client.diarize(media_url)

# retrieve diarization
diarization = client.retrieve(job_id)
# diarization'output' contains diarization output
```

Sections: Official pyannoteAI Python SDK, Speaker diarization, STT orchestration, Speaker identification

</details>

### psmpy

Propensity score matching for python and graphical plots

`pip install psmpy` · installs (wheel) · licence: MIT License · rank 4668 · last release 2025-11-12 · [PyPI](https://pypi.org/project/psmpy/) · [docs](https://pypi.org/project/psmpy)

<details><summary>README extract</summary>

Matching techniques for epidemiological observational studies as carried out in Python. Propensity score matching is a statistical matching technique used with observational data that attempts to ascertain the validity of concluding there is a potential causal link between a treatment or intervention and an outcome(s) of interest. ...

Example:
```python
# import relevant libraries
from psmpy import PsmPy
from psmpy.functions import cohenD
from psmpy.plotting import *
sns.set(rc={'figure.figsize':(10,8)}, font_scale = 1.3)
```

...

</details>

### pytest-httpx2

A pytest plugin for mocking out httpx2 using respx.

`pip install pytest-httpx2` · installs (wheel) · licence: BSD-3-Clause · rank 4676 · last release 2026-05-20 · [PyPI](https://pypi.org/project/pytest-httpx2/) · [source](https://github.com/lundberg/pytest-httpx2)

<details><summary>README extract</summary>

A `pytest` plugin for mocking out `httpx2` using `respx`.

See `respx` documentation for more
configuration options and api.

Example:
```python
import httpx2

def test_foobar(httpx2_mock: respx.Router) -> None:
    httpx2_mock.post("
    response = httpx2.post("
    assert response.status_code == 201
```

Sections: pytest-httpx2, Configure using marker

</details>

### python-keystoneclient

Client Library for OpenStack Identity

`pip install python-keystoneclient` · installs (wheel) · licence: Apache Software License · rank 4684 · last release 2026-08-28 · [PyPI](https://pypi.org/project/python-keystoneclient/)

<details><summary>README extract</summary>

This is a client for the OpenStack Identity API, implemented by the Keystone
team; it contains a Python API (the `keystoneclient` module) for
OpenStack's Identity Service. For command line interface support, use
OpenStackClient. ...

Example:
```python
>>> from keystoneauth1.identity import v3
>>> from keystoneauth1 import session
>>> from keystoneclient.v3 import client
>>> auth = v3.Password(auth_url=" username="admin",
...                     password="password", project_name="admin",
...                     user_domain_id="default", project_domain_id="default")
...
```

Sections: Team and repository tags, Python bindings to the OpenStack Identity API (Keystone), Python API

</details>

### plato-sdk-v2

Python SDK for the Plato API

`pip install plato-sdk-v2` · does not install on CPython 3.14 · licence: MIT · rank 4696 · last release 2026-10-30 · [PyPI](https://pypi.org/project/plato-sdk-v2/)

<details><summary>README extract</summary>

Python SDK for the Plato platform.

Example:
```python
import asyncio
from plato.v2 import AsyncPlato, Env

async def main():
    plato = AsyncPlato()

    # Create session with one or more environments
    # (heartbeat starts automatically to keep session alive)
    session = await plato.sessions.create(
        envs=[
            Env.simulator("gitea", dataset="blank", alias="gitea"),
...
```

Sections: Plato Python SDK, Configuration, Agents, CLI Usage, Sessions & Environments, Flow 1: Create Session from Environments, Flow 2: Create Session from Test Case, Environment Configuration, Per-Environment Operations, Sync Client, Documentation

</details>

### publish-event-sns

Publish message into SNS Topic with attributes

`pip install publish-event-sns` · installs (wheel) · licence: MIT License · rank 4706 · last release 2020-05-22 · [PyPI](https://pypi.org/project/publish-event-sns/)

<details><summary>README extract</summary>

This package helps you to publish a dict object as JSON into SNS Topic, including fields as attributes

This code will transform DICT into JSON and publish into SNS Topic with `foo` as attribute as `bar` value.

> `publish` function will automaticaly exclude from attributes non primitive values (dict, object, etc)

Example:
```python
from publish_event_sns import publish

my_dict = {
    "foo": "bar"
}

response = publish("topic_name", my_dict)
```

Sections: Publish Data Event to SNS Topic, Parameters

</details>

### pymeshlab

A Python interface to MeshLab

`pip install pymeshlab` · installs (wheel) · licence: GPL3 · rank 4717 · last release 2026-01-30 · [PyPI](https://pypi.org/project/pymeshlab/)

_README extract left out: share-alike licence._

### pystow

Easily pick a place to store data for your Python code

`pip install pystow` · installs (wheel) · licence: MIT · rank 4724 · last release 2026-10-17 · [PyPI](https://pypi.org/project/pystow/) · [docs](https://pystow.readthedocs.io) · [source](https://github.com/cthoyt/pystow.git)

<details><summary>README extract</summary>

👜 Easily pick a place to store data for your Python code

Example:
```python
import pystow

# Get a directory (as a pathlib.Path) for ~/.data/pykeen
pykeen_directory = pystow.join("pykeen")

# Get a subdirectory (as a pathlib.Path) for ~/.data/pykeen/experiments
pykeen_experiments_directory = pystow.join("pykeen", "experiments")

# You can go as deep as you want
...
```

Sections: PyStow, 💪 Getting Started, ⚙️️ Configuration, X Desktop Group (XDG) Compatibility, 👋 Attribution, 🍪 Cookiecutter, Updating Package Boilerplate, 📖 Building the Documentation, Configuring ReadTheDocs, Configuring Zenodo, Registering with the Python Package Index (PyPI), Configuring your machine's connection to PyPI, Uploading to PyPI, Releasing on GitHub

</details>

### pyandoc

Python wrapper for Pandoc - the universal document converter

`pip install pyandoc` · installs from source (sdist only) · licence: MIT License · rank 4727 · last release 2016-02-04 · [PyPI](https://pypi.org/project/pyandoc/)

<details><summary>README extract</summary>

Pyandoc is a simple Python wrapper for the excellent pandoc utility. It allows you to convert the format of text documents by interacting with a `Document` object's attributes. Each supported format is available as a property, and can either read from or written to.

* Pandoc

Example:
```python
import pandoc
```

Sections: Pyandoc: a simple Pandoc wrapper for Python, Requirements, Usage, v0.0.2 (02-04-2016), v0.0.1 (01-02-2010)

</details>

### patch

Library to parse and apply unified diffs

`pip install patch` · installs from source (sdist only) · licence: MIT License · rank 4728 · last release 2016-02-13 · [PyPI](https://pypi.org/project/patch/)

<details><summary>README extract</summary>

Features

 * Python 2 and 3 compatible
 * Automatic correction of
 * Linefeeds according to patched file
 * Diffs broken by stripping trailing whitespace
 * a/ and b/ prefixes
 * Single file, which is a command line tool and a library
 * No dependencies outside Python stdlib
 * Patch format detection (SVN, HG, GIT)
 * Nice diffstat histogram
 * ...

</details>

### pypsrp

PowerShell Remoting Protocol and WinRM for Python

`pip install pypsrp` · installs (wheel) · licence: MIT · rank 4738 · last release 2026-03-16 · [PyPI](https://pypi.org/project/pypsrp/)

<details><summary>README extract</summary>

Example:
```python
from pypsrp.client import Client

# this takes in the same kwargs as the WSMan object
with Client("server", username="user", password="password") as client:

    # execute a cmd command
    stdout, stderr, rc = client.execute_cmd("dir")

    stdout, stderr, rc = client.execute_cmd("powershell.exe gci $pwd")
...
```

Sections: Requirements, Optional Requirements, Kerberos Authentication, CredSSP Authentication, How to Use, Connection, Shell, Process, Examples, Logging, Backlog

</details>

### pyatlan

Atlan Python Client

`pip install pyatlan` · installs (wheel) · licence: Apache Software License · rank 4745 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyatlan/) · [docs](https://github.com/atlanhq/atlan-python) · [source](https://github.com/atlanhq/atlan-python)

<details><summary>README extract</summary>

The official Python SDK for the Atlan 💙

📖 Documentation •
🐳 Docker •
🤝 Contributing

- 🐍 Python Versions: 3.9, 3.10, 3.11, 3.12, 3.13
- 📦 Package Size: Optimized for fast installation
- 🚀 Performance: Built with modern async/await support
- 🔧 Dependencies: Minimal, modern stack
- 📈 Stability: Production-ready

Sections: 📊 Project Stats, Production Use, Dependency Groups, 🐳 Docker, Pre-built Images (Harbor), Usage, Run Snyk locally (dependencies), Unit Tests, Integration Tests, Quality Assurance, Making Changes, Guidelines, 🛠️ SDK Generator, App Builders Generator

</details>

### pypiwin32

(no summary)

`pip install pypiwin32` · installs (wheel) · licence: not stated · rank 4751 · last release 2018-02-26 · [PyPI](https://pypi.org/project/pypiwin32/)

### propelauth-py

A python authentication library

`pip install propelauth-py` · installs (wheel) · licence: MIT · rank 4752 · last release 2026-04-21 · [PyPI](https://pypi.org/project/propelauth-py/)

<details><summary>README extract</summary>

A python library for managing authentication, backed by PropelAuth.

PropelAuth makes it easy to add authentication and authorization to your B2B/multi-tenant application.

Your frontend gets a beautiful, safe, and customizable login screen. Your backend gets easy authorization with just a few lines of code. ...

Example:
```python
from propelauth_py import init_base_auth

auth = init_base_auth("YOUR_AUTH_URL", "YOUR_API_KEY")
```

Sections: PropelAuth Python SDK, Documentation, Initialize, Protect API Routes, Check Org Membership, Check Org Membership and Role, Check Org Membership and Permission, Calling Backend APIs, Logging Configuration, Questions?

</details>

### petname

Generate human-readable, random object names

`pip install petname` · installs (wheel) · licence: Apache2 · rank 4777 · last release 2026-02-15 · [PyPI](https://pypi.org/project/petname/)

<details><summary>README extract</summary>

petname − an RFC1178 implementation to generate pronounceable, sometimes even memorable, "pet names", consisting of a random combination of adverbs, an adjective, and an animal name

Example:
```python
# !/usr/bin/python
import argparse
import petname
import sys

parser = argparse.ArgumentParser(description='Generate human readable random names')
parser.add_argument('-w', '--words', help='Number of words in name, default=2', default=2)
parser.add_argument('-l', '--letters', help='Maximum number of letters per word, default=6', default=6)
...
```

Sections: petname, Name, Synopsis, Options, Description, Examples, Code, Golang Example, Python Example

</details>

### py-mini-racer

Minimal, modern embedded V8 for Python.

`pip install py-mini-racer` · installs (wheel) · licence: ISC License (ISCL) · rank 4834 · last release 2021-04-22 · [PyPI](https://pypi.org/project/py-mini-racer/)

<details><summary>README extract</summary>

Minimal, modern embedded V8 for Python.

Features:
* Latest ECMAScript support
* Web Assembly support
* Unicode support
* Thread safe
* Re-usable contexts

MiniRacer can be easily used by Django or Flask projects to minify assets, run
babel or WASM modules.

Example:
```python
>>> from py_mini_racer import MiniRacer
>>> ctx = MiniRacer()
>>> ctx.eval("1+1")
2
>>> ctx.eval("var x = {company: 'Sqreen'}; x.company")
'Sqreen'
>>> print(ctx.eval("'\N{HEAVY BLACK HEART}'"))
❤
>>> ctx.eval("var fun = () => ({ foo: 1 });")
```

Sections: Features, Examples, Compatibility, Build, Notes for building on macOS, Tests, 0.6.0 (2020-04-20), 0.5.0 (2020-02-25), 0.4.0 (2020-09-22), 0.3.0 (2020-06-29), 0.2.0 (2020-03-11), 0.2.0b1 (2020-01-09), 0.1.18 (2019-01-04), 0.1.17 (2018-19-12)

</details>

### py-openapi-schema-to-json-schema

Convert OpenAPI Schemas to JSON Schemas

`pip install py-openapi-schema-to-json-schema` · installs (wheel) · licence: MIT License · rank 4850 · last release 2020-07-25 · [PyPI](https://pypi.org/project/py-openapi-schema-to-json-schema/)

<details><summary>README extract</summary>

Overview

**This is a straight Python port of the MIT-licensed
mikunn/openapi-schema-to-json-schema
(v2.1.0)**.
This port is similarly MIT-licensed.

It converts from OpenAPI 3.0 to
JSON Schema Draft 4.

Features:
OpenAPI 3 Schemas and JSON Schemas are mostly similar. However, JSON Schema
validators are unaware of the differences between the two formats. ...

Example:
```python
import json
from openapi_schema_to_json_schema import to_json_schema

openapi_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "nullable": True,
        }
    },
    "x-patternProperties": {
        "^[a-z]+$": {
            "type": "number",
        }
    }
}

...
```

...

</details>

### pytest-opentelemetry

A pytest plugin for instrumenting test runs via OpenTelemetry

`pip install pytest-opentelemetry` · installs (wheel) · licence: MIT License · rank 4862 · last release 2025-04-25 · [PyPI](https://pypi.org/project/pytest-opentelemetry/)

<details><summary>README extract</summary>

Instruments your pytest runs, exporting the spans and timing via OpenTelemetry.

Features:
As projects grow larger, perhaps with many contributors, test suite runtime can be
a significant limiting factor to how fast you and your team can deliver changes. ...

Sections: pytest-opentelemetry, Why instrument my test suite?, Visualizing test traces

</details>

### py-markdown-table

Package that generates markdown tables from a list of dicts

`pip install py-markdown-table` · installs (wheel) · licence: MIT · rank 4878 · last release 2026-10-20 · [PyPI](https://pypi.org/project/py-markdown-table/)

<details><summary>README extract</summary>

Tiny python library with zero dependencies which generates formatted multiline tables in `markdown`.

Example:
```python
from py_markdown_table.markdown_table import markdown_table
data = [
    {
        "Product": "Smartphone",
        "Brand": "Apple",
        "Price": 999.99
    },
    {
        "Product": "Laptop",
        "Brand": "Dell",
        "Price": 1299.99
    }
]
markdown = markdown_table(data).get_markdown()
print(markdown)
```

Sections: py-markdown-table, Basic Use, Advanced Use, Type hints, Utils, Further Examples, Row separatation, Padding, padding weight and padding char, Per-column padding and padding weight, Compact output, Multiline and emoji, Benchmarks

</details>

### pycrdt-store

Persistent storage for pycrdt

`pip install pycrdt-store` · installs (wheel) · licence: MIT License · rank 4899 · last release 2026-06-11 · [PyPI](https://pypi.org/project/pycrdt-store/) · [source](https://github.com/y-crdt/pycrdt-store)

### pyro-ppl

A Python library for probabilistic modeling and inference

`pip install pyro-ppl` · installs (wheel) · licence: Apache-2.0 · rank 4900 · last release 2026-10-03 · [PyPI](https://pypi.org/project/pyro-ppl/) · [docs](https://docs.pyro.ai) · [source](https://github.com/pyro-ppl/pyro)

<details><summary>README extract</summary>

Getting Started |
Documentation |
Community |
Contributing

Pyro is a flexible, scalable deep probabilistic programming library built on PyTorch. Notably, it was designed with these principles in mind:

- Universal: Pyro is a universal PPL - it can represent any computable probability distribution. ...

</details>

### pytest-reportportal

Agent for Reporting results of tests to the Report Portal

`pip install pytest-reportportal` · installs (wheel) · licence: Apache 2.0 · rank 4942 · last release 2026-10-26 · [PyPI](https://pypi.org/project/pytest-reportportal/)

<details><summary>README extract</summary>

Pytest plugin for reporting test results of the Pytest to the ReportPortal.

> DISCLAIMER: We use Google Analytics for sending anonymous usage information such as agent's and client's names,
> and their versions after a successful launch start. This information might help us to improve both ReportPortal
> backend and client sides. ...

Example:
```python
import logging

import pytest

from reportportal_client import RPLogger

@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger
```

Sections: ReportPortal integration for pytest framework, Configuration, Examples, Launching, Copyright Notice

</details>

### promql-parser

(no summary)

`pip install promql-parser` · installs (wheel) · licence: not stated · rank 4952 · last release 2026-11-06 · [PyPI](https://pypi.org/project/promql-parser/) · [source](https://github.com/messense/py-promql-parser)

<details><summary>README extract</summary>

Python bindings for promql-parser, a PromQL parser written in Rust.

`promql-parser` parses Prometheus query expressions into a Python-accessible AST that can be inspected, walked, transformed, and formatted back to PromQL.

Example:
```python
import promql_parser

ast = promql_parser.parse('prometheus_http_requests_total{code="200", job="prometheus"}')
print(ast)
print(ast.prettify())
```

Sections: py-promql-parser, Quick start, Inspecting the AST, Walking expressions, Transforming expressions, Duration helpers, Custom functions

</details>

### pyjsparser

Fast javascript parser (based on esprima.js)

`pip install pyjsparser` · installs from source (sdist only) · licence: MIT · rank 4959 · last release 2019-04-21 · [PyPI](https://pypi.org/project/pyjsparser/)

### PureCloudPlatformClientV2

PureCloud Platform API SDK

`pip install PureCloudPlatformClientV2` · installs (wheel) · licence: MIT · rank 4978 · last release 2026-10-08 · [PyPI](https://pypi.org/project/PureCloudPlatformClientV2/)

<details><summary>README extract</summary>

Documentation can be found at

Documentation version PureCloudPlatformClientV2 269.0.0

Warning: Preview APIs are included in this SDK. These resources are subject to both breaking and non-breaking changes at any time without notice. ...

Example:
```python
import PureCloudPlatformClientV2
```

Sections: Platform API Client SDK - Python, Preview APIs, Using the Library, Referencing the Library, Authenticating, Client Credentials Grant, OAuth2 SAML2 Bearer Grant, PKCE Grant, Setting the Environment, Setting the gateway, Connect to a Proxy Server, SDK Logging, Configuration file, Making Requests

</details>

### phik

Phi_K correlation analyzer library

`pip install phik` · installs (wheel) · licence: MIT License · rank 4990 · last release 2025-10-10 · [PyPI](https://pypi.org/project/phik/)

<details><summary>README extract</summary>

* Version: 0.12.5. Released: Jul 2025

* Publication: [offical] [arxiv pre-print]

Phi_K is a practical correlation constant that works consistently between categorical, ordinal and interval variables.
It is based on several refinements to Pearson's hypothesis test of independence of two variables. ...

Example:
```python
import phik
```

Sections: Phi_K Correlation Constant, Example notebooks, Documentation, Check it out, Quick run

</details>

### pyro-api

Generic API for dispatch to Pyro backends.

`pip install pyro-api` · installs (wheel) · licence: Apache Software License · rank 5008 · last release 2020-05-15 · [PyPI](https://pypi.org/project/pyro-api/)

<details><summary>README extract</summary>

Generic API for modeling and inference for dispatch to different Pyro backends.

</details>

### prefab-ui

The generative UI framework that even humans can use.

`pip install prefab-ui` · installs (wheel) · licence: Apache-2.0 · rank 5054 · last release 2026-10-26 · [PyPI](https://pypi.org/project/prefab-ui/) · [docs](https://prefab.prefect.io) · [source](https://github.com/PrefectHQ/prefab)

<details><summary>README extract</summary>

The generative UI framework that even humans can use.

🚧 *Don't panic. Prefab is under very active development.* 🚧

Docs · Playground · GitHub

Prefab is a UI framework for building rich, interactive interfaces in Python. Create MCP Apps, data dashboards, interactive tools, and more with 100+ prebuilt components. ...

Features:
Python developers building tools, APIs, and servers regularly need to ship interactive interfaces alongside their logic: dashboards, data tables, forms, charts. ...

Example:
```python
from prefab_ui.components import *
from prefab_ui.rx import Rx

name = Rx("name").default("world")

with Card():
    with CardContent():
        with Column(gap=3):
            H3(f"Hello, {name}!")
            Muted("Type below and watch this update in real time.")
...

</details>

### pulumi-postgresql

A Pulumi package for creating and managing postgresql cloud resources.

`pip install pulumi-postgresql` · installs (wheel) · licence: Apache-2.0 · rank 5095 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pulumi-postgresql/) · [source](https://github.com/pulumi/pulumi-postgresql)

<details><summary>README extract</summary>

The postgresql resource provider for Pulumi lets you manage postgresql resources in your cloud programs. To use
this package, please install the Pulumi CLI first.

Sections: postgresql Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### python-fasthtml

The fastest way to create an HTML app

`pip install python-fasthtml` · installs (wheel) · licence: Apache-2.0 · rank 5103 · last release 2026-11-05 · [PyPI](https://pypi.org/project/python-fasthtml/) · [docs](https://www.fastht.ml/docs/) · [source](https://github.com/AnswerDotAI/fasthtml)

<details><summary>README extract</summary>

Welcome to the official FastHTML documentation.

FastHTML is a new next-generation web framework for fast, scalable web applications with minimal, compact code. It’s designed to be:

- Powerful and expressive enough to build the most advanced, interactive web apps you can imagine. ...

Example:
```python
from fasthtml.common import *

app,rt = fast_app()

@rt('/')
def get(): return Div(P('Hello World!'), hx_get="/change")

serve()
```

Sections: FastHTML, Usage, Getting help from AI, Next Steps, Other languages and related projects

</details>

### pystan

Python interface to Stan, a package for Bayesian inference

`pip install pystan` · installs (wheel) · licence: OSI Approved; ISC License (ISCL) · rank 5112 · last release 2026-09-11 · [PyPI](https://pypi.org/project/pystan/) · [docs](https://pystan.readthedocs.io) · [source](https://github.com/stan-dev/pystan)

<details><summary>README extract</summary>

PyStan is a Python interface to Stan, a package for Bayesian inference.

Stan® is a state-of-the-art platform for statistical modeling and
high-performance statistical computation. Thousands of users rely on Stan for
statistical modeling, data analysis, and prediction in the social, biological,
and physical sciences, engineering, and business. ...

Example:
```python
import stan

schools_code = """
data {
  int<lower=0> J;         // number of schools
  array[J] real y;              // estimated treatment effects
  array[J] real<lower=0> sigma; // standard error of effect estimates
}
parameters {
  real mu;                // population treatment effect
...
```

Sections: PyStan, Getting started

</details>

### pysimdjson

Add your description here

`pip install pysimdjson` · installs from source (sdist only) · licence: not stated · rank 5113 · last release 2025-06-28 · [PyPI](https://pypi.org/project/pysimdjson/)

<details><summary>README extract</summary>

Python bindings for the simdjson project, a SIMD-accelerated JSON parser.
If SIMD instructions are unavailable a fallback parser is used, making
pysimdjson safe to use anywhere.

Bindings are currently tested on OS X, Linux, and Windows for Python version
3.9 to 3.12.

The latest documentation can be found at ...

Sections: pysimdjson, 📝 Documentation, 📈 Benchmarks

</details>

### pydantic-to-typescript

Convert pydantic models to typescript interfaces

`pip install pydantic-to-typescript` · installs (wheel) · licence: MIT License · rank 5129 · last release 2024-11-22 · [PyPI](https://pypi.org/project/pydantic-to-typescript/) · [source](https://github.com/phillipdupuis/pydantic-to-typescript)

<details><summary>README extract</summary>

A simple CLI tool for converting pydantic models into typescript interfaces. Useful for any scenario in which python and javascript applications are interacting, since it allows you to have a single source of truth for type definitions.

This tool requires that you have the lovely json2ts CLI utility installed. Instructions can be found here:

Example:
```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

api = FastAPI()

class LoginCredentials(BaseModel):
    username: str
    password: str

class Profile(BaseModel):
    username: str
    age: Optional[int]
    hobbies: List[str]

class LoginResponseData(BaseModel):
    token: str
    profile: Profile

...
```

Sections: pydantic-to-typescript, CLI, Usage

</details>

### postgres-mcp

PostgreSQL Tuning and Analysis Tool

`pip install postgres-mcp` · installs (wheel) · licence: MIT · rank 5138 · last release 2025-05-16 · [PyPI](https://pypi.org/project/postgres-mcp/)

<details><summary>README extract</summary>

Overview •
 Demo •
 Quick Start •
 Technical Notes •
 MCP API •
 Related Projects •
 FAQ

Features:
Postgres MCP Pro is an open source Model Context Protocol (MCP) server built to support you and your AI agents throughout the entire development process—from initial coding, through testing and deployment, and to production tuning and maintenance. ...

Sections: Overview, Demo, Quick Start, Prerequisites, Access Credentials, Docker or Python, Option 1: Using Docker, Option 2: Using Python, Configure Your AI Assistant, Claude Desktop Configuration, If you are using Docker, If you are using `pipx`, If you are using `uv`, Connection URI

</details>

### pyppeteer

Headless chrome/chromium automation library (unofficial port of puppeteer)

`pip install pyppeteer` · installs (wheel) · licence: MIT License · rank 5141 · last release 2024-02-18 · [PyPI](https://pypi.org/project/pyppeteer/) · [source](https://github.com/pyppeteer/pyppeteer)

<details><summary>README extract</summary>

If you would like to overhaul this code to bring it up to date, please contact me

_Note: this is a continuation of the pyppeteer project

Unofficial Python port of puppeteer JavaScript (headless) chrome/chromium browser automation library.

* Free software: MIT license (including the work distributed under the Apache 2.0 license)

Example:
```python
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
```

Sections: pyppeteer, Usage, Examples, Differences between puppeteer and pyppeteer, Keyword arguments for options, Element selector method names, Roadmap

</details>

### portend

TCP port monitoring and discovery

`pip install portend` · installs (wheel) · licence: MIT · rank 5181 · last release 2025-05-29 · [PyPI](https://pypi.org/project/portend/) · [source](https://github.com/jaraco/portend)

<details><summary>README extract</summary>

por·tend
pôrˈtend/
verb

 be a sign or warning that (something, especially something momentous or calamitous) is likely to happen.

Example:
```python
portend.occupied('www.google.com', 80, timeout=3)
```

Sections: Usage, For Enterprise

</details>

### pybars3

Handlebars.js templating for Python 3 and 2

`pip install pybars3` · installs from source (sdist only) · licence: GNU Library or Lesser General Public License (LGPL) · rank 5202 · last release 2019-11-05 · [PyPI](https://pypi.org/project/pybars3/)

_README extract left out: share-alike licence._

### poly-eip712-structs

A python library for EIP712 objects

`pip install poly-eip712-structs` · installs (wheel) · licence: MIT License · rank 5226 · last release 2024-07-18 · [PyPI](https://pypi.org/project/poly-eip712-structs/)

<details><summary>README extract</summary>

A python interface for simple EIP-712 struct construction.

In this module, a "struct" is structured data as defined in the standard.
It is not the same as the Python Standard Library's struct (e.g., `import struct`).

Read the proposal:

Example:
```python
# Make a unique domain
from eip712_structs import make_domain
domain = make_domain(name='Some name', version='1.0.0')  # Make a Domain Separator

# Define your struct type
from eip712_structs import EIP712Struct, String, Uint
class MyStruct(EIP712Struct):
    some_string = String()
    some_number = Uint(256)

# Create an instance with some data
...
```

Sections: EIP-712 Structs, Usage, Quickstart, Dynamic construction, The domain separator, Setting a default domain, Member Types, Basic types, Struct references, Arrays, Shameless Plug

</details>

### py-order-utils

Python utilities used to generate and sign orders from Polymarket's Exchange

`pip install py-order-utils` · installs (wheel) · licence: MIT License · rank 5229 · last release 2024-07-29 · [PyPI](https://pypi.org/project/py-order-utils/)

<details><summary>README extract</summary>

Python utilities used to generate and sign orders from Polymarket's Exchange

Example:
```python
from py_order_utils.builders import OrderBuilder
from py_order_utils.signer import Signer
from pprint import pprint

def main():
    exchange_address = "0x...."
    chain_id = 80002
    signer = Signer("0x....")
    builder = OrderBuilder(exchange_address, chain_id, signer)

    # Create and sign the order
    order = builder.build_signed_order(
...
```

Sections: Polymarket CLOB Python order-utils, Usage

</details>

### python-geohash

Fast, accurate python geohashing library

`pip install python-geohash` · installs (wheel) · licence: not stated · rank 5265 · last release 2026-06-02 · [PyPI](https://pypi.org/project/python-geohash/)

<details><summary>README extract</summary>

python-geohash is a fast, accurate Python geohashing library.

</details>

### pulumi-aws-native

A native Pulumi package for creating and managing Amazon Web Services (AWS) resources.

`pip install pulumi-aws-native` · installs (wheel) · licence: Apache-2.0 · rank 5303 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pulumi-aws-native/) · [source](https://github.com/pulumi/pulumi-aws-native)

<details><summary>README extract</summary>

The Pulumi AWS Cloud Control Provider enables you to build, deploy, and manage any AWS resource that's supported by the AWS Cloud Control API.
With Pulumi's native provider for AWS Cloud Control, you get same-day access to all new AWS resources and all new properties on existing resources supported by the Cloud Control API. ...

Sections: Pulumi AWS Cloud Control Provider, Configuring credentials, Building, Dependencies, Building locally, Running tests, Running an example, Additional Build Targets, Debugging / Logging

</details>

### pipreqs

Pip requirements.txt generator based on imports in project

`pip install pipreqs` · does not install on CPython 3.14 · licence: Apache Software License · rank 5327 · last release 2024-02-18 · [PyPI](https://pypi.org/project/pipreqs/) · [source](https://github.com/bndr/pipreqs)

<details><summary>README extract</summary>

Features:
- `pip freeze` only saves the packages that are installed with `pip install` in your environment.
- `pip freeze` saves all packages in the environment including those that you don't use in your current project (if you don't have `virtualenv`). ...

Sections: Usage, Example, Why not pip freeze?, 0.4.11 (2020-03-29), 0.4.8 (2017-06-30), 0.4.7 (2017-04-20), 0.4.5 (2016-12-13), 0.4.4 (2016-07-14), 0.4.2 (2016-02-10), 0.4.1 (2016-02-05), 0.4.0 (2016-01-28), 0.3.9 (2016-01-20), 0.3.8 (2016-01-12), 0.3.1 (2015-10-20)

</details>

### pyttsx3

Text to Speech (TTS) library for Python 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.

`pip install pyttsx3` · installs (wheel) · licence: MPL-2.0 · rank 5330 · last release 2025-07-08 · [PyPI](https://pypi.org/project/pyttsx3/)

<details><summary>README extract</summary>

`pyttsx3` is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline.

Buy me a coffee 😇

Features:
- ✨Fully OFFLINE text to speech conversion
- 🎈 Choose among different voices installed in your system
- 🎛 Control speed/rate of speech
- 🎚 Tweak Volume
- 📀 Save the speech audio as a file
- ❤️ Simple, powerful, & intuitive API

Example:
```python
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I will speak this text")
engine.runAndWait()
```

...

</details>

### pymsalruntime

The MSALRuntime Python Interop Package

`pip install pymsalruntime` · installs (wheel) · licence: MIT License · rank 5334 · last release 2026-10-24 · [PyPI](https://pypi.org/project/pymsalruntime/)

### poetry-plugin-pypi-mirror

Poetry plugin that adds support for pypi.org mirrors and pull-through caches

`pip install poetry-plugin-pypi-mirror` · installs (wheel) · licence: BSD License · rank 5347 · last release 2026-09-22 · [PyPI](https://pypi.org/project/poetry-plugin-pypi-mirror/) · [source](https://github.com/arcesium/poetry-plugin-pypi-mirror)

<details><summary>README extract</summary>

*poetry-plugin-pypi-mirror* is a
plugin for
poetry, the Python packaging and dependency
manager. It enables poetry to substitute connections to pypi.org with
connections to a pypi.org mirror or pull-through cache **without requiring
project configuration changes**. ...

Example:
```python
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

...
```

...

</details>

### pypika-tortoise

Forked from pypika and streamline just for tortoise-orm

`pip install pypika-tortoise` · installs (wheel) · licence: Apache-2.0 · rank 5361 · last release 2026-03-13 · [PyPI](https://pypi.org/project/pypika-tortoise/) · [docs](https://github.com/tortoise/pypika-tortoise) · [source](https://github.com/tortoise/pypika-tortoise.git)

<details><summary>README extract</summary>

Forked from pypika and adapted just for tortoise-orm.

Features:
The original repository includes many databases that Tortoise ORM doesn’t require. It aims to be a comprehensive SQL builder with broad compatibility, but that’s not the goal for Tortoise ORM. ...

Sections: pypika-tortoise, Why forked?, What changed?, ThanksTo

</details>

### prettyprinter

Syntax-highlighting, declarative and composable pretty printer for Python 3.5+

`pip install prettyprinter` · installs (wheel) · licence: MIT License · rank 5379 · last release 2019-06-22 · [PyPI](https://pypi.org/project/prettyprinter/)

<details><summary>README extract</summary>

Documentation

Syntax-highlighting, declarative and composable pretty printer for Python 3.5+

- Drop in replacement for the standard library `pprint`: just rename `pprint` to `prettyprinter` in your imports.
- Uses a modified Wadler-Leijen layout algorithm for optimal formatting ...

Example:
```python
>>> from datetime import datetime
>>> from prettyprinter import pprint
>>> pprint({'beautiful output': datetime.now()})
{
    'beautiful output': datetime.datetime(
        year=2017,
        month=12,
        day=12,
        hour=0,
        minute=43,
        second=4,
        microsecond=752094
    )
}
```

...

</details>

### pylint-gitlab

This project provides pylint formatters for a nice integration with GitLab CI.

`pip install pylint-gitlab` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 5419 · last release 2025-11-23 · [PyPI](https://pypi.org/project/pylint-gitlab/) · [docs](https://gitlab.com/smueller18/pylint-gitlab) · [source](https://gitlab.com/smueller18/pylint-gitlab)

_README extract left out: share-alike licence._

### pyromark

Blazingly fast CommonMark-compliant Markdown pull parser

`pip install pyromark` · installs (wheel) · licence: not stated · rank 5427 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pyromark/) · [docs](https://monosans.github.io/pyromark) · [source](https://github.com/monosans/pyromark)

<details><summary>README extract</summary>

pyromark (stands for Python Rust Optimized Markdown) is a blazingly fast CommonMark-compliant Markdown parser for Python, built on the pulldown-cmark Rust crate.

Example:
```python
import pyromark

html = pyromark.html("# Hello world")
assert html == "
# Hello world
\n"
```

Sections: pyromark, Documentation, Examples, Convert Markdown to HTML, Iterate over Markdown elements, Enable extensions and highlight code, Command line, Performance

</details>

### python3-logstash

Python logging handler for Logstash.

`pip install python3-logstash` · installs (wheel) · licence: MIT · rank 5448 · last release 2018-07-12 · [PyPI](https://pypi.org/project/python3-logstash/)

<details><summary>README extract</summary>

This is a copy of python-logstash: <
That has been update to work with python 3.

Example:
```python
import logging
import logstash
import sys

host = 'localhost'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5959, version=1))
# test_logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))

...
```

Sections: python-logstash, Python logging handler for Logstash., Notes, Usage, For example, Using with Django, Using with Gunicorn, Sample logstash configuration

</details>

### phonopy

This is the phonopy module.

`pip install phonopy` · installs (wheel) · licence: BSD-3-Clause · rank 5493 · last release 2026-11-06 · [PyPI](https://pypi.org/project/phonopy/) · [source](https://github.com/phonopy/phonopy)

<details><summary>README extract</summary>

Phonon code mainly written in Python, with the compute-intensive parts handled
by the Rust backend (phonors). Phonopy user documentation is found at

Sections: Phonopy, Mailing list for questions, Formatting, pre-commit, VSCode setting, Documentation, How to run tests

</details>

### pyocse

Python Organic Crystal Simulation Environment

`pip install pyocse` · installs (wheel) · licence: MIT License · rank 5503 · last release 2026-09-28 · [PyPI](https://pypi.org/project/pyocse/)

<details><summary>README extract</summary>

This is a public repository that aims to automate the simulation of organic crystals with a primary emphasis on the mechanical properties of organic crystals. Currently, we focus on two components:

1. Automate the geneation of structural model and force field (through `ambertools` or `openff`)
2. ...

Example:
```python
# Find your structure from
tag = {
       "csd_code": 'ACSALA',
       "ccdc_number": 1101020,
       "smiles": "CC(=O)OC1=CC=CC=C1C(O)=O",
}

# Load the pyxtal structure
from pyxtal import pyxtal
xtal = pyxtal(molecular=True)
xtal.from_seed(str(tag['ccdc_number'])+'.cif',
               molecules=[str(tag['smiles'])+'.smi'])
xtal.tag = tag
...
```

...

</details>

### pyxtal

Python code for generation of crystal structures based on symmetry constraints.

`pip install pyxtal` · installs (wheel) · licence: MIT License · rank 5508 · last release 2026-09-09 · [PyPI](https://pypi.org/project/pyxtal/)

<details><summary>README extract</summary>

- Introduction
- Quick Start
- Current Features
- Installation
- Citation
- How to contribute?

PyXtal is an open source Python package which was initiated by Qiang Zhu and Scott Fredericks. The goal of PyXtal is to develop a fundamental library to allow one to design the material structure with a certain symmetry constraint. ...

Sections: Table of content, Introduction, Quick Start, Current Features, General PyXtal, Site Symmetry Representation, Symmetry relation, Organic crystal packing motif

</details>

### pyseccomp

An interface to libseccomp using ctypes. API compatible with libseccomp's Python bindings.

`pip install pyseccomp` · installs (wheel) · licence: MIT License · rank 5516 · last release 2021-01-02 · [PyPI](https://pypi.org/project/pyseccomp/)

<details><summary>README extract</summary>

An interface to libseccomp using ctypes.

This library is API compatible with libseccomp's Python bindings, but it's available on PyPI and it's written in pure Python.

This is the intended use case:

Example:
```python
try:
    import seccomp
except ImportError:
    import pyseccomp as seccomp
```

</details>

### pmtiles

Library and utilities to write and read PMTiles archives - cloud-optimized archives of map tiles.

`pip install pmtiles` · installs (wheel) · licence: BSD License · rank 5530 · last release 2026-09-16 · [PyPI](https://pypi.org/project/pmtiles/)

<details><summary>README extract</summary>

Sections: pmtiles, Running Tests, Uploading build

</details>

### polygon-api-client

Official Polygon.io REST and Websocket client.

`pip install polygon-api-client` · installs (wheel) · licence: MIT License · rank 5565 · last release 2025-10-30 · [PyPI](https://pypi.org/project/polygon-api-client/) · [docs](https://polygon.io/docs) · [source](https://github.com/polygon-io/client-python)

### pyvespa

Python API for vespa.ai

`pip install pyvespa` · installs (wheel) · licence: Apache Software License · rank 5568 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyvespa/) · [source](https://github.com/vespa-engine/pyvespa)

<details><summary>README extract</summary>

pyvespa site / documentation

Vespa is the scalable open-sourced serving engine that enables users to store,
compute and rank big data at user serving time.
`pyvespa` provides a python API to Vespa.
It allows users to create, modify, deploy and interact with running Vespa instances. ...

Sections: pyvespa, vespacli

</details>

### proto-schema-parser

A Pure Python Protobuf .proto Parser

`pip install proto-schema-parser` · installs (wheel) · licence: MIT · rank 5644 · last release 2025-11-05 · [PyPI](https://pypi.org/project/proto-schema-parser/)

<details><summary>README extract</summary>

Protobuf Schema Parser is a pure-Python library that parses and writes Protobuf schemas to and from an abstract syntax tree (AST).

The library uses `proto_schema_parser.parser.Parser` to parse the CST into an AST. The `proto_schema_parser.generator.Generator` class converts the AST back into a CST (a Protobuf schema string). ...

Features:
- ✅ proto2 and proto3 support
- ✅ protobuf editions support (edition 2023, edition 2024)
- ✅ message, field, enum, optional, required, repeated
- ✅ import, package, oneof, map, and option
- ✅ group and extend (in proto2) ...

Example:
```python
from proto_schema_parser.parser import Parser

text = """
syntax = "proto3";

message SearchRequest {
  string query = 1;
  int32 page_number = 2;
  int32 result_per_page = 3;
}
"""

...

</details>

### python-jwt

Module for generating and verifying JSON Web Tokens

`pip install python-jwt` · installs (wheel) · licence: MIT · rank 5655 · last release 2023-11-13 · [PyPI](https://pypi.org/project/python-jwt/)

<details><summary>README extract</summary>

Module for generating and verifying JSON Web Tokens.

*All versions of python-jwt are now DEPRECATED. I don't have the time to maintain this module.*

- Note: Versions 3.3.4 and later fix a vulnerability (CVE-2022-39227) in JSON Web Token verification which lets an attacker with a valid token re-use its signature with modified claims. ...

Example:
```python
import python_jwt as jwt, jwcrypto.jwk as jwk, datetime
key = jwk.JWK.generate(kty='RSA', size=2048)
priv_pem = key.export_to_pem(private_key=True, password=None)
pub_pem = key.export_to_pem()
payload = { 'foo': 'bar', 'wup': 90 };
priv_key = jwk.JWK.from_pem(priv_pem)
pub_key = jwk.JWK.from_pem(pub_pem)
...
```

Sections: python-jwt&nbsp;&nbsp;&nbsp;, Another Example, Tests, Lint, Code Coverage, Benchmarks

</details>

### propelauth-fastapi

A FastAPI library for managing authentication, backed by PropelAuth

`pip install propelauth-fastapi` · installs (wheel) · licence: MIT · rank 5675 · last release 2026-04-23 · [PyPI](https://pypi.org/project/propelauth-fastapi/)

<details><summary>README extract</summary>

A FastAPI library for managing authentication, backed by PropelAuth.

PropelAuth makes it easy to add authentication and authorization to your B2B/multi-tenant application.

Your frontend gets a beautiful, safe, and customizable login screen. Your backend gets easy authorization with just a few lines of code. ...

Example:
```python
from propelauth_fastapi import init_auth

auth = init_auth("YOUR_AUTH_URL", "YOUR_API_KEY")
```

Sections: PropelAuth FastAPI SDK, Documentation, Initialize, Protect API Routes, require_user, optional_user, Check Org Membership, Check Org Membership and Role, Check Org Membership and Permission, Calling Backend APIs, Questions?

</details>

### pulumi-github

A Pulumi package for creating and managing github cloud resources.

`pip install pulumi-github` · installs (wheel) · licence: Apache-2.0 · rank 5696 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pulumi-github/) · [source](https://github.com/pulumi/pulumi-github)

<details><summary>README extract</summary>

The GitHub resource provider for Pulumi lets you use GitHub resources in your infrastructure programs.
To use this package, please install the Pulumi CLI first.

Sections: GitHub provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pytest-coverage

(no summary)

`pip install pytest-coverage` · does not install on CPython 3.14 · licence: not stated · rank 5707 · last release ? · [PyPI](https://pypi.org/project/pytest-coverage/)

### pulumi-azuread

A Pulumi package for creating and managing Azure Active Directory (Azure AD) cloud resources.

`pip install pulumi-azuread` · installs (wheel) · licence: Apache-2.0 · rank 5729 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pulumi-azuread/) · [source](https://github.com/pulumi/pulumi-azuread)

<details><summary>README extract</summary>

The Microsoft Azure AD resource provider for Pulumi lets you use Azure Active Directory resources in your cloud programs. To use
this package, please install the Pulumi CLI first. For a streamlined Pulumi walkthrough, including language runtime installation and Azure configuration, click "Get Started" below.

Sections: Microsoft Azure Active Directory Resource Provider, Node.js (Java/TypeScript), Python 3, Go, .NET, Configuration, Reference

</details>

### PyDrive2

Google Drive API made easy. Maintained fork of PyDrive.

`pip install PyDrive2` · installs (wheel) · licence: Apache License 2.0 · rank 5751 · last release 2024-11-29 · [PyPI](https://pypi.org/project/PyDrive2/) · [docs](https://docs.iterative.ai/PyDrive2)

<details><summary>README extract</summary>

*PyDrive2* is a wrapper library of
google-api-python-client
that simplifies many common Google Drive API V2 tasks. It is an actively
maintained fork of
By the authors and maintainers of the Git for Data - DVC
project.

- Running tests

Features:
- Simplifies OAuth2.0 into just few lines with flexible settings.
- Wraps Google Drive API V2 into
 classes of each resource to make your program more object-oriented. ...

Example:
```python
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
```

Sections: PyDrive2, Project Info, Features of PyDrive2, OAuth made easy, File management made easy, File listing pagination made easy, Fsspec filesystem, Concurrent access made easy

</details>

### paramiko-expect

An expect-like extension for the Paramiko SSH library

`pip install paramiko-expect` · installs from source (sdist only) · licence: MIT License · rank 5823 · last release 2026-11-02 · [PyPI](https://pypi.org/project/paramiko-expect/)

<details><summary>README extract</summary>

Artwork courtesy of Open Clip Art
Library

This project originally started as a POC while I was automating some tasks on Cisco CDS devices
in my operations role. While the library worked well, I didn't actually get to use it much myself
as I moved onto an engineering role soon after. ...

Example:
```python
# Connect to the host
client.connect(hostname=hostname, username=username, password=password)

# Create a client interaction class which will interact with the host
interact = SSHClientInteraction(client, timeout=10, display=True)
interact.expect(prompt)

# Run the first command and capture the cleaned output, if you want the output
...
```

Sections: Paramiko Expect, Repository Archived, Introduction, Quick Start, Tests

</details>

### protoc-gen-validate

PGV for python via just-in-time code generation

`pip install protoc-gen-validate` · installs (wheel) · licence: not stated · rank 5825 · last release 2026-02-18 · [PyPI](https://pypi.org/project/protoc-gen-validate/)

<details><summary>README extract</summary>

Example:
```python
from entities_pb2 import Person
from protoc_gen_validate.validator import validate, ValidationFailed, validate_all

p = Person(name="Foo")
try:
    validate(p)
except ValidationFailed as err:
    print(err)  # p.id is not greater than 999

try:
    validate_all(p)
except ValidationFailed as err:
    print(err)
    # p.id is not greater than 999
...
```

</details>

### pylint-celery

pylint-celery is a Pylint plugin to aid Pylint in recognising and understandingerrors caused when using the Celery library

`pip install pylint-celery` · installs from source (sdist only) · licence: GPLv2 · rank 5836 · last release 2014-09-25 · [PyPI](https://pypi.org/project/pylint-celery/)

_README extract left out: share-alike licence._

### pinotdb

Python DB-API and SQLAlchemy dialect for Pinot.

`pip install pinotdb` · installs (wheel) · licence: MIT License · rank 5837 · last release 2026-10-12 · [PyPI](https://pypi.org/project/pinotdb/)

<details><summary>README extract</summary>

This module allows accessing Pinot via its SQL API.

Current supported Pinot version: `1.1.0`.

Example:
```python
Sending SQL to Pinot: SELECT * FROM baseballStats LIMIT 5
[0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 'NL', 11, 11, 'aardsda01', 'David Allan', 1, 0, 0, 0, 0, 0, 0, 'SFN', 0, 2004]
[2, 45, 0, 0, 0, 0, 0, 0, 0, 0, 'NL', 45, 43, 'aardsda01', 'David Allan', 1, 0, 0, 0, 1, 0, 0, 'CHN', 0, 2006]
...
```

Sections: Python DB-API and SQLAlchemy dialect for Pinot, Usage, Using the DB API to query Pinot Broker directly, Native query results (9.2+), Pass the Pinot database context, Using SQLAlchemy, Examples with Pinot Quickstart, Examples with existing pinot.live demo cluster

</details>

### pyct

Python package common tasks for users (e.g. copy examples, fetch data, ...)

`pip install pyct` · installs (wheel) · licence: BSD-3-Clause · rank 5839 · last release 2025-09-26 · [PyPI](https://pypi.org/project/pyct/) · [source](https://github.com/holoviz-dev/pyct)

<details><summary>README extract</summary>

A utility package that includes:

 1. pyct.cmd: Makes various commands available to other
 packages. (Currently no sophisticated plugin system, just a try
 import/except in the other packages.) The same commands are
 available from within python. ...

Sections: pyct, pyct.cmd, pyct.build, pyct report

</details>

### pybuildkite

Python wrapper for the Buildkite API

`pip install pybuildkite` · installs (wheel) · licence: not stated · rank 5875 · last release 2025-07-31 · [PyPI](https://pypi.org/project/pybuildkite/) · [source](https://github.com/pyasi/pybuildkite.git)

<details><summary>README extract</summary>

A Python library and client for the Buildkite API.

Example:
```python
from pybuildkite.buildkite import Buildkite, BuildState

buildkite = Buildkite()
buildkite.set_access_token('YOUR_API_ACCESS_TOKEN_HERE')

# Get all info about particular org
org = buildkite.organizations().get_org('my-org')

# Get all running and scheduled builds for a particular pipeline
...
```

Sections: PyBuildkite, Usage, Per-Page Configuration, Pagination, Artifacts

</details>

### python-lsp-ruff

Ruff linting plugin for pylsp

`pip install python-lsp-ruff` · installs (wheel) · licence: MIT · rank 5876 · last release 2026-09-08 · [PyPI](https://pypi.org/project/python-lsp-ruff/)

<details><summary>README extract</summary>

`python-lsp-ruff` is a plugin for `python-lsp-server` that adds linting, code actions and formatting capabilities that are provided by ruff,
an extremely fast Python linter and formatter written in Rust.

Note that `ruff>0.4.5` ships with a built-in LSP server (and `ruff-lsp` before that), which allows linting, formatting and code actions. ...

Sections: python-lsp-ruff, When using ruff before version 0.1.0, Usage, Configuration, Custom severities, Code formatting, Code actions, Debugging

</details>

### patchy

Patch the inner source of python functions at runtime.

`pip install patchy` · installs (wheel) · licence: MIT · rank 5882 · last release 2026-08-21 · [PyPI](https://pypi.org/project/patchy/) · [source](https://github.com/adamchainz/patchy)

<details><summary>README extract</summary>

Patch the inner source of python functions at runtime.

A quick example, making a function that returns 1 instead return 9001:

Patchy works by replacing the code attribute of the function, leaving the
function object itself the same. ...

Features:
If you’re monkey-patching an external library to add or fix some functionality,
you will probably forget to check the monkey patch when you upgrade it. ...

Example:
```python
>>> def sample():
...     return 1
...
>>> patchy.patch(
...     sample,
...     """\
...     @@ -1,2 +1,2 @@
...      def sample():
...     -    return 1
...     +    return 9001
...     """,
... )
>>> sample()
9001
```

...

</details>

### pymobiledevice3

Pure python3 implementation for working with iDevices (iPhone, etc...)

`pip install pymobiledevice3` · installs (wheel) · licence: GPL-3.0-or-later · rank 5906 · last release 2026-11-08 · [PyPI](https://pypi.org/project/pymobiledevice3/)

_README extract left out: share-alike licence._

### python-swiftclient

OpenStack Object Storage API Client Library

`pip install python-swiftclient` · installs (wheel) · licence: Apache Software License · rank 5908 · last release 2026-08-28 · [PyPI](https://pypi.org/project/python-swiftclient/) · [docs](https://docs.openstack.org/python-swiftclient/latest/) · [source](https://opendev.org/openstack/python-swiftclient)

<details><summary>README extract</summary>

This is a python client for the Swift API. There's a Python API (the
`swiftclient` module), and a command-line script (`swift`).

Development takes place via the usual OpenStack processes as outlined
in the OpenStack wiki.


This code is based on the original client previously included with
OpenStack's Swift. ...

</details>

### python-bitcoinlib

The Swiss Army Knife of the Bitcoin protocol.

`pip install python-bitcoinlib` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 5914 · last release 2023-06-03 · [PyPI](https://pypi.org/project/python-bitcoinlib/)

_README extract left out: share-alike licence._

### py-machineid

Get the unique machine ID of any host (without admin privileges)

`pip install py-machineid` · installs (wheel) · licence: MIT License · rank 5918 · last release 2025-12-02 · [PyPI](https://pypi.org/project/py-machineid/)

<details><summary>README extract</summary>

Get the unique machine ID of any host (without admin privileges).

Sponsored by:

_A fair source software licensing and distribution API._

Example:
```python
import machineid

print(machineid.id())
```

Sections: py-machineid, Usage, Building, Publishing, Thanks

</details>

### pymeshfix

Repair triangular meshes using MeshFix

`pip install pymeshfix` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 5931 · last release 2026-04-23 · [PyPI](https://pypi.org/project/pymeshfix/) · [docs](https://pymeshfix.pyvista.org/) · [source](https://github.com/pyvista/pymeshfix)

_README extract left out: share-alike licence._

### python-json-config

This library allows to load json configs and access the values like members (i.e., via dots), validate config field types and values and transform config fields.

`pip install python-json-config` · installs (wheel) · licence: MIT License · rank 5945 · last release 2019-11-21 · [PyPI](https://pypi.org/project/python-json-config/)

<details><summary>README extract</summary>

Features:
This library allows to load json configs and access the values like members (i.e., `config.server.port`
instead of `config'server'`), validate the data types of fields and transform the values of fields.

Example:
```python
from python_json_config import ConfigBuilder

# create config parser
builder = ConfigBuilder()

# parse config
config = builder.parse_config('path/to/config.json')

# access elements
host = config.server.host
port = config.server.port
myfield = config.myfield
```

Sections: Overview, Usage, Validate field types, Validate field values, Transform field values, Define field access settings, Access config values, Change config values, Overwrite fields with environment variables, Serialization

</details>

### python-fcl

Python bindings for the Flexible Collision Library

`pip install python-fcl` · installs (wheel) · licence: BSD License · rank 5959 · last release 2026-04-08 · [PyPI](https://pypi.org/project/python-fcl/)

<details><summary>README extract</summary>

Python-FCL is an (unofficial) Python interface for the Flexible Collision Library (FCL),
an excellent C++ library for performing proximity and collision queries on pairs of geometric models.
Currently, this package is targeted for FCL 0.7.0. ...

Example:
```python
import numpy as np
import fcl

v1 = np.array([1.0, 2.0, 3.0])
v2 = np.array([2.0, 1.0, 3.0])
v3 = np.array([3.0, 2.0, 1.0])
x, y, z = 1, 2, 3
rad, lz = 1.0, 3.0
n = np.array([1.0, 0.0, 0.0])
d = 5.0

t = fcl.TriangleP(v1, v2, v3) # Triangle defined by three points
b = fcl.Box(x, y, z)          # Axis-aligned box with given side lengths
...
```

...

</details>

### polars-hash

Stable non-cryptographic and cryptographic hashing functions for Polars

`pip install polars-hash` · installs (wheel) · licence: not stated · rank 5964 · last release 2026-09-08 · [PyPI](https://pypi.org/project/polars-hash/)

<details><summary>README extract</summary>

This plugin provides stable hashing functionality across different polars versions.

📖 Documentation — every expression,
its input and output types, and its arguments.

Example:
```python
import polars as pl
import polars_hash as plh

df = pl.DataFrame({
    "foo":["hello_world"]
})

result = df.select(plh.col('foo').chash.sha256())

print(result)

┌──────────────────────────────────────────────────────────────────┐
│ foo                                                              │
...
```

Sections: Examples, Cryptographic Hashers, Non-cryptographic Hashers, Geo Hashers, H3 Spatial Index, Time Hasher, Create hash from multiple columns, Hash a whole row

</details>

### pysnc

Python SNC (REST) API

`pip install pysnc` · installs (wheel) · licence: MIT License · rank 5995 · last release 2026-02-11 · [PyPI](https://pypi.org/project/pysnc/) · [docs](https://servicenow.github.io/PySNC/) · [source](https://github.com/ServiceNow/PySNC)

<details><summary>README extract</summary>

What:
PySnc is a python interface for the ServiceNow and the Table API. It is designed to mimic the familiar GlideRecord interface you know with pythonic support where applicable.

Why:
Spawned from the desire to interact with ServiceNow data in a familiar and consistent manner

Features:
* GlideAggregate support (`/api/now/stats/{tableName}`)

And we want to:

* Improve documentation

Example:
```python
from pysnc import ServiceNowClient

client = ServiceNowClient(' ('integration.user', password))

gr = client.GlideRecord('sys_user')
gr.add_query('user_name', 'admin')
gr.query()
for r in gr:
    print(r.sys_id)
```

Sections: ServiceNow Python API, Quick Start, Documentation, Feature Wants and TODO

</details>

### pulumi-tailscale

A Pulumi package for creating and managing Tailscale cloud resources.

`pip install pulumi-tailscale` · installs (wheel) · licence: Apache-2.0 · rank 6003 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pulumi-tailscale/) · [source](https://github.com/pulumi/pulumi-tailscale)

<details><summary>README extract</summary>

The Tailscale Resource Provider lets you manage Tailscale resources.

Sections: Tailscale Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pyspark-test

Check that left and right spark DataFrame are equal.

`pip install pyspark-test` · installs (wheel) · licence: Apache Software License (Apache 2.0) · rank 6017 · last release 2021-10-31 · [PyPI](https://pypi.org/project/pyspark-test/)

<details><summary>README extract</summary>

Check that left and right spark DataFrame are equal.

This function is intended to compare two spark DataFrames and output any differences. It is inspired from pandas testing module but for pyspark, and for use in unit tests. Additional parameters allow varying the strictness of the equality checks performed.

Example:
```python
assert_pyspark_df_equal(left_df, actual_df)
```

Sections: pyspark-test, Usage, Additional Arguments, Example

</details>

### protobuf_to_pydantic

Generate the `pydantic.BaseModel` class (and the corresponding source code) with parameter verification function through the Protobuf file

`pip install protobuf_to_pydantic` · installs (wheel) · licence: Other/Proprietary License · rank 6027 · last release 2025-06-07 · [PyPI](https://pypi.org/project/protobuf_to_pydantic/) · [source](https://github.com/so1n/protobuf_to_pydantic)

<details><summary>README extract</summary>

Generate Pydantic Model or source code with parameter verification function based on Protobuf file (Proto3).

中文文档

Features:
Feature：
- [x] Generate source code through `Protobuf` plugin。
- [x] Generate `Pydantic Model` or source code by parsing `Protobuf Message` in `Python` runtime.
- [x] Compatible with `V1` and `V2` versions of `Pydantic`。 ...

Example:
```python
import logging
from typing import List, Type

from google.protobuf.any_pb2 import Any  # type: ignore
from pydantic import confloat, conint
from pydantic.fields import FieldInfo

from protobuf_to_pydantic.template import Template

# Configure the log output format and log level of the plugin, which is very useful when debugging
...
```

...

</details>

### pyang

A YANG (RFC 6020/7950) validator and converter

`pip install pyang` · installs (wheel) · licence: BSD License · rank 6031 · last release 2025-08-29 · [PyPI](https://pypi.org/project/pyang/)

<details><summary>README extract</summary>

An extensible YANG (RFC 6020/7950) validator. Provides a framework for plugins that can convert YANG modulesto other formats.

</details>

### pyprojroot

Project-oriented workflow in Python

`pip install pyprojroot` · installs (wheel) · licence: MIT License · rank 6041 · last release 2023-03-13 · [PyPI](https://pypi.org/project/pyprojroot/)

<details><summary>README extract</summary>

Finding project directories in Python (data science) projects.

This library aims to provide both
the programmatic functionality from the R `rprojroot` package
and the interactive functionality from the R `here` package. ...

Example:
```python
from pyprojroot.here import here

here()
```

Sections: Project-oriented workflow in Python, Motivation, pip, conda, Example Usage, Interactive, Programmatic, Demonstration

</details>

### psycopg2-pool

Proper pooling of psycopg2 connections

`pip install psycopg2-pool` · installs (wheel) · licence: LGPL3 · rank 6051 · last release 2024-01-15 · [PyPI](https://pypi.org/project/psycopg2-pool/)

_README extract left out: share-alike licence._

### pytest-structlog

Structured logging assertions

`pip install pytest-structlog` · installs (wheel) · licence: MIT · rank 6064 · last release 2025-09-10 · [PyPI](https://pypi.org/project/pytest-structlog/)

<details><summary>README extract</summary>

Structured logging assertions.
pytest + structlog = `pytest-structlog`.

Example:
```python
# your_lib.py
from structlog import get_logger

logger = get_logger()

def spline_reticulator():
    logger.info("reticulating splines")
    for i in range(3):
        logger.debug("processing", spline=i)
    logger.info("reticulated splines", n_splines=3)
```

Sections: pytest-structlog, Usage, Advanced configuration

</details>

### pyfmodex

Python bindings to the Fmod Ex library.

`pip install pyfmodex` · installs (wheel) · licence: MIT License · rank 6080 · last release 2024-03-08 · [PyPI](https://pypi.org/project/pyfmodex/)

<details><summary>README extract</summary>

This is pyfmodex, an FMOD Engine Python binding using ctypes.

Installation

To install, first make sure that you have the FMOD Engine library for you platform somewhere in your path, so Python will be able to find it.
On Linux, libraries are searched for in `LD_LIBRARY_PATH`. ...

Example:
```python
import pyfmodex
```

</details>

### pyhpke

A Python implementation of HPKE.

`pip install pyhpke` · installs (wheel) · licence: MIT · rank 6105 · last release 2026-07-16 · [PyPI](https://pypi.org/project/pyhpke/) · [source](https://github.com/dajiaji/pyhpke)

<details><summary>README extract</summary>

PyHPKE is a HPKE (Hybrid Public Key Encryption) implementation written in Python.

You can install PyHPKE with pip:

And then, you can use it as follows:

Example:
```python
from pyhpke import AEADId, CipherSuite, KDFId, KEMId, KEMKey

# The sender side:
suite_s = CipherSuite.new(
    KEMId.DHKEM_P256_HKDF_SHA256, KDFId.HKDF_SHA256, AEADId.AES128_GCM
)
pkr = KEMKey.from_jwk(
    {
        "kid": "01",
        "kty": "EC",
        "crv": "P-256",
        "x": "Ze2loSV3wrroKUN_4zhwGhCqo3Xhu1td4QjeQ5wIVR0",
...
```

Sections: PyHPKE - A Python implementation of HPKE, Index, Warnings and Restrictions, Usage, API Reference, Test, Dependency updates, Scanning

</details>

### py-builder-signing-sdk

Python builder signing sdk

`pip install py-builder-signing-sdk` · installs (wheel) · licence: MIT License · rank 6124 · last release 2025-10-20 · [PyPI](https://pypi.org/project/py-builder-signing-sdk/)

<details><summary>README extract</summary>

Python SDK for Polymarket builder authentication and signing.

Example:
```python
from py_builder_signing_sdk import BuilderConfig, BuilderApiKeyCreds, RemoteBuilderConfig

# Local signing
creds = BuilderApiKeyCreds(
    key="your-api-key",
    secret="your-secret",
    passphrase="your-passphrase"
)
config = BuilderConfig(local_builder_creds=creds)

# Remote signing
remote_config = RemoteBuilderConfig(
    url="
...
```

Sections: py-builder-signing-sdk, Usage

</details>

### pyapacheatlas

A package to simplify working with the Apache Atlas REST APIs for Atlas and Azure Purview.

`pip install pyapacheatlas` · installs (wheel) · licence: MIT License · rank 6134 · last release 2023-12-23 · [PyPI](https://pypi.org/project/pyapacheatlas/)

<details><summary>README extract</summary>

PyApacheAtlas lets you work with the Azure Purview and Apache Atlas APIs in a Pythonic way. Supporting bulk loading, custom lineage, custom type definition and more from an SDK and Excel templates / integration.

The package supports programmatic interaction and an Excel template for low-code uploads.

* Bulk upload entities. ...

Sections: Using Excel to Accelerate Metadata Uploads, Using the Pythonic SDK for Purview and Atlas

</details>

### PyTurboJPEG

A Python wrapper of libjpeg-turbo for decoding and encoding JPEG image.

`pip install PyTurboJPEG` · installs (wheel) · licence: MIT · rank 6155 · last release 2026-10-24 · [PyPI](https://pypi.org/project/PyTurboJPEG/)

<details><summary>README extract</summary>

A Python wrapper for libjpeg-turbo that enables efficient JPEG image decoding and encoding.

- libjpeg-turbo 3.0 or later (required for PyTurboJPEG 2.0+)
- numpy
- Python 3.8 or later

Important: PyTurboJPEG 2.0+ requires libjpeg-turbo 3.0 or later as it uses the new function-based TurboJPEG 3 API. ...

Example:
```python
from turbojpeg import TurboJPEG

# Use the default library installation
jpeg = TurboJPEG()

# Or specify the library path explicitly
# jpeg = TurboJPEG(r'D:\turbojpeg.dll')  # Windows
# jpeg = TurboJPEG('/usr/lib64/libturbojpeg.so')  # Linux
# jpeg = TurboJPEG('/usr/local/lib/libturbojpeg.dylib')  # macOS
```

...

</details>

### piccolo-api

Utilities for using the Piccolo ORM in ASGI apps, plus essential ASGI middleware such as authentication and rate limiting.

`pip install piccolo-api` · installs (wheel) · licence: MIT License · rank 6166 · last release 2026-08-07 · [PyPI](https://pypi.org/project/piccolo-api/)

<details><summary>README extract</summary>

Utilities for easily exposing Piccolo tables as REST endpoints in ASGI apps, such as Starlette and FastAPI.

Includes a bunch of useful ASGI middleware:

- Session Auth
- Token Auth
- Rate Limiting
- CSRF
- Content Security Policy (CSP)
- And more ...

</details>

### pydeseq2

A python implementation of DESeq2.

`pip install pydeseq2` · installs (wheel) · licence: not stated · rank 6174 · last release 2026-01-23 · [PyPI](https://pypi.org/project/pydeseq2/) · [docs](https://pydeseq2.readthedocs.io/) · [source](https://github.com/owkin/PyDESeq2)

<details><summary>README extract</summary>

PyDESeq2 is a python implementation of the DESeq2
method [1] for differential expression analysis (DEA) with bulk RNA-seq data, originally in R.
It aims to facilitate DEA experiments for python users.

As PyDESeq2 is a re-implementation of DESeq2 from
scratch, you may experience some differences in terms of retrieved values or available features. ...

Sections: PyPI, Bioconda, Requirements, Getting started, Documentation, Data, 1 - Download the repository, 2 - Create a uv environment, Citing this work, References

</details>

### pandapower

An easy to use open source tool for power system modeling, analysis and optimization with a high degree of automation.

`pip install pandapower` · installs (wheel) · licence: BSD License · rank 6196 · last release 2026-10-07 · [PyPI](https://pypi.org/project/pandapower/) · [docs](https://pandapower.readthedocs.io) · [source](https://www.github.com/e2nIEE/pandapower.git)

<details><summary>README extract</summary>

pandapower is an easy to use network calculation program aimed to automate the analysis and optimization of power
systems. It uses the data analysis library pandas and is compatible with the commonly
used MATPOWER / PYPOWER case format. ...

</details>

### python-openstackclient

OpenStack Command-line Client

`pip install python-openstackclient` · installs (wheel) · licence: Apache-2.0 · rank 6215 · last release 2026-10-22 · [PyPI](https://pypi.org/project/python-openstackclient/) · [source](https://opendev.org/openstack/python-openstackclient/)

<details><summary>README extract</summary>

OpenStackClient (OSC) is a command-line client for OpenStack that brings
the command set for Compute, Identity, Image, Network, Object Store and Block
Storage APIs together in a single shell with a uniform command structure.
Support for additional service APIs is provided via plugins. ...

Sections: OpenStackClient, Getting Started, Configuration, Links

</details>

### pytest-pep8

pytest plugin to check PEP8 requirements

`pip install pytest-pep8` · installs from source (sdist only) · licence: MIT license · rank 6224 · last release 2014-04-27 · [PyPI](https://pypi.org/project/pytest-pep8/)

<details><summary>README extract</summary>

Example:
```python
# content of myfile.py

somefunc( 123,456)
```

Sections: py.test plugin for efficiently checking PEP8 compliance, Usage, A little example, Configuring PEP8 options per project and file, Running PEP8 checks and no other tests, Notes

</details>

### pyworld

PyWorld: a Python wrapper for WORLD vocoder

`pip install pyworld` · does not install on CPython 3.14 · licence: not stated · rank 6229 · last release 2026-08-20 · [PyPI](https://pypi.org/project/pyworld/)

<details><summary>README extract</summary>

| `Linux` | `Windows` |

| | |

WORLD Vocoder is a fast and high-quality vocoder
which parameterizes speech into three components:

 1. `f0`: Pitch contour
 2. `sp`: Harmonic spectral envelope
 3. `ap`: Aperiodic spectral envelope (relative to the harmonic spectral envelope) ...

Example:
```python
import pyworld as pw
_f0, t = pw.dio(x, fs)    # raw pitch extractor
f0 = pw.stonemask(x, _f0, t, fs)  # pitch refinement
sp = pw.cheaptrick(x, f0, t, fs)  # extract smoothed spectrogram
ap = pw.d4c(x, f0, t, fs)         # extract aperiodicity

y = pw.synthesize(f0, sp, ap, fs) # synthesize an utterance using the parameters
```

...

</details>

### py-clob-client

Python client for the Polymarket CLOB

`pip install py-clob-client` · installs (wheel) · licence: MIT License · rank 6231 · last release 2026-02-19 · [PyPI](https://pypi.org/project/py-clob-client/)

<details><summary>README extract</summary>

Python client for the Polymarket Central Limit Order Book (CLOB).

Example:
```python
from py_clob_client.client import ClobClient

client = ClobClient("  # Level 0 (no auth)

ok = client.get_ok()
time = client.get_server_time()
print(ok, time)
```

Sections: Polymarket Python CLOB Client, Documentation, Usage, Quickstart (read‑only), Start trading (EOA), Start trading (proxy wallet), Funder Address, Signature Types, Find markets, prices, and orderbooks, Place a market order (buy by $ amount), Place a limit order (shares at a price), Manage orders, Markets (read‑only), User trades (requires auth)

</details>

### pytest-timestamper

Pytest plugin to add a timestamp prefix to the pytest output

`pip install pytest-timestamper` · installs (wheel) · licence: not stated · rank 6268 · last release 2024-03-27 · [PyPI](https://pypi.org/project/pytest-timestamper/)

<details><summary>README extract</summary>

Pytest plugin to add a timestamp prefix to the pytest output.

Sections: pytest-timestamper, Motivation, Usage

</details>

### pytest-pylint

pytest plugin to check source code with pylint

`pip install pytest-pylint` · installs (wheel) · licence: MIT License · rank 6292 · last release 2023-10-06 · [PyPI](https://pypi.org/project/pytest-pylint/)

<details><summary>README extract</summary>

Run pylint with pytest and have configurable rule types
(i.e. Convention, Warn, and Error) fail the build. You can also
specify a pylintrc file.

Sections: pytest pylint, Sample Usage, 0.21.0, 0.20.0, 0.19.0, 0.18.0, 0.17.0, 0.16.1, 0.16.0, 0.15.1, 0.15.0, 0.14.1, 0.14.0, 0.13.0

</details>

### piq

Measures and metrics for image2image tasks. PyTorch.

`pip install piq` · installs (wheel) · licence: Apache Software License · rank 6342 · last release 2023-07-04 · [PyPI](https://pypi.org/project/piq/)

<details><summary>README extract</summary>

PyTorch Image Quality (PIQ) is a collection of measures and metrics for
image quality assessment. PIQ helps you to concentrate on your experiments without the boilerplate code.
The library contains a set of measures and metrics that is continually getting extended. ...

Example:
```python
import torch
from piq import ssim, SSIMLoss

x = torch.rand(4, 3, 256, 256, requires_grad=True)
y = torch.rand(4, 3, 256, 256)

ssim_index: torch.Tensor = ssim(x, y, data_range=1.)

loss = SSIMLoss(data_range=1.)
output: torch.Tensor = loss(x, y)
output.backward()
```

...

</details>

### pycolmap

COLMAP bindings

`pip install pycolmap` · installs (wheel) · licence: BSD License · rank 6353 · last release 2026-09-29 · [PyPI](https://pypi.org/project/pycolmap/) · [source](https://github.com/colmap/colmap)

<details><summary>README extract</summary>

PyCOLMAP exposes to Python most capabilities of the COLMAP Structure-from-Motion (SfM) and Multi-View Stereo (MVS) pipeline.

Example:
```python
output_path: pathlib.Path
image_dir: pathlib.Path

output_path.mkdir()
mvs_path = output_path / "mvs"
database_path = output_path / "database.db"

pycolmap.extract_features(database_path, image_dir)
pycolmap.match_exhaustive(database_path)
maps = pycolmap.incremental_mapping(database_path, image_dir, output_path)
maps[0].write(output_path)

...
```

...

</details>

### python-certifi-win32

Add windows certificate store to certifi cacerts.

`pip install python-certifi-win32` · installs (wheel) · licence: BSD · rank 6377 · last release 2022-07-02 · [PyPI](https://pypi.org/project/python-certifi-win32/)

<details><summary>README extract</summary>

NOTE : This package has been replaced by
pip-system-certs and is generally unmaintained.

This package patches certifi at runtime to also include certificates from the windows certificate store. ...

</details>

### PyExcelerate

Accelerated Excel XLSX Writing Library for Python 2/3

`pip install PyExcelerate` · installs (wheel) · licence: BSD License · rank 6387 · last release 2025-05-23 · [PyPI](https://pypi.org/project/PyExcelerate/)

<details><summary>README extract</summary>

Accelerated Excel XLSX writing library for Python

master: dev: test coverage:

- Authors: Kevin Wang and Kevin
 Zhang
- Copyright 2015 Kevin Wang, Kevin Zhang. Portions copyright Google,
 Inc.
- License: Simplified BSD License
- Source repository
- PyPI page ...

Example:
```python
from pyexcelerate import Workbook

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # data is a 2D array

wb = Workbook()
wb.new_sheet("sheet name", data=data)
wb.save("output.xlsx")
```

Sections: PyExcelerate, Description, Benchmarks, Usage, Writing bulk data, Fastest, Writing bulk data to a range, Writing cell data, Faster, Fast, Selecting cells by name, Merging cells, Styling cells

</details>

### pyspark-pandas

Tools and algorithms for pandas Dataframes distributed on pyspark. Please consider the SparklingPandas project before this one

`pip install pyspark-pandas` · installs from source (sdist only) · licence: UNKNOWN · rank 6395 · last release 2014-10-14 · [PyPI](https://pypi.org/project/pyspark-pandas/)

### pycountry-convert

Extension of Python package pycountry providing conversion functions.

`pip install pycountry-convert` · installs (wheel) · licence: MIT License · rank 6430 · last release 2018-02-18 · [PyPI](https://pypi.org/project/pycountry-convert/)

<details><summary>README extract</summary>

Extension of Python package pycountry providing conversion functions.

Sections: pycountry-convert, Architecture, Functions, Parameter: cn_name_format, Parameter: cn_extras, Dependencies, 0.7.2 (2018-02-16), 0.7.1 (2018-02-15), 0.6.7 (2018-02-15), 0.6.6 (2018-01-25), 0.6.2 (2017-12-09), 0.5.4 (2017-12-07), 0.5.0 (2017-11-30), 0.3.0 (2017-11-27)

</details>

### phpserialize

a port of the serialize and unserialize functions of php to python.

`pip install phpserialize` · installs from source (sdist only) · licence: BSD License · rank 6438 · last release 2012-01-22 · [PyPI](https://pypi.org/project/phpserialize/)

<details><summary>README extract</summary>

a port of the `serialize` and `unserialize` functions of
php to python. This module implements the python serialization
interface (eg: provides `dumps`, `loads` and similar functions).

Example:
```python
class WP_UserBase {
    protected $username;

    public function __construct($username) {
        $this->username = $username;
    }
}

class WP_User extends WP_UserBase {
    private $password;
    public $flag;

    public function __construct($username, $password) {
        parent::__construct($username);
        $this->password = $password;
...
```

Sections: phpserialize, Usage, Array Serialization, Object Serialization, PHP's Object System, Python 3 Notes

</details>

### pytest-mock-resources

A pytest plugin for easily instantiating reproducible mock resources.

`pip install pytest-mock-resources` · installs (wheel) · licence: MIT · rank 6458 · last release 2026-10-01 · [PyPI](https://pypi.org/project/pytest-mock-resources/) · [source](https://github.com/schireson/pytest-mock-resources)

<details><summary>README extract</summary>

Code which depends on external resources such a databases (postgres, redshift, etc) can be difficult
to write automated tests for. Conventional wisdom might be to mock or stub out the actual database
calls and assert that the code works correctly before/after the calls.

However take the following, _simple_ example: ...

Features:
General features include:

- Support for "actions" which pre-populate the resource you're mocking before the test
- Async fixtures
- Custom configuration for container/resource startup

Example:
```python
def serialize(users):
    return [
        {
            'user': user.serialize(),
            'address': user.address.serialize(),
            'purchases': [p.serialize() for p in user.purchases],
        }
        for user in users
    ]

...

</details>

### pytdc

Therapeutics Commons

`pip install pytdc` · installs from source (sdist only) · licence: MIT · rank 6462 · last release 2025-03-31 · [PyPI](https://pypi.org/project/pytdc/)

<details><summary>README extract</summary>

Website | NeurIPS 2024 AIDrugX Paper | Nature Chemical Biology 2022 Paper | NeurIPS 2021 Paper | Long Paper | Slack | TDC Mailing List | TDC Documentation | Contribution Guidelines | [\[PyTDC Webpage\]]( ...

Example:
```python
from tdc.single_pred import ADME
data = ADME(name = 'HIA_Hou')
# split into train/val/test with scaffold split methods
split = data.get_split(method = 'scaffold')
# get the entire data in the various formats
data.get_data(format = 'df')
```

...

</details>

### pathwaysutils

Package of Pathways-on-Cloud utilities.

`pip install pathwaysutils` · installs (wheel) · licence: Apache Software License · rank 6463 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pathwaysutils/) · [source](https://github.com/AI-Hypercomputer/pathways-utils)

<details><summary>README extract</summary>

Pathways is a compute orchestration runtime for single-controller ML workloads
across multiple Cloud TPU slices. A single Python controller orchestrates
computation across hundreds or thousands of TPU chips, unlocking slice-level
training resiliency, fast cross-slice data movement, and interactive
multi-slice development. ...

Sections: APIs to get started with using Pathways on Cloud, Core Modules, Further Reading

</details>

### pykdebugparser

Python parser for kdebug events

`pip install pykdebugparser` · installs (wheel) · licence: not stated · rank 6464 · last release 2026-10-20 · [PyPI](https://pypi.org/project/pykdebugparser/) · [source](https://github.com/matan1008/pykdebugparser)

<details><summary>README extract</summary>

- Description
- Installation
- Usage
 * CLI
 * Python
 * Example

`pykdebugparser` is a utility created in order to parse Darwin's (iOS and OSX) kdebug events.

The main difference between `pykdebugparser` and other utilities like fs_usage and ktrace is the traces parsing and
formatting.

Example:
```python
...
2489180732445653 MACH_vm_page_release (0x130049c)                          DBG_FUNC_NONE  Error: tid 19699133        b'\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
...
```

Sections: Description, Usage, CLI, Python, Example

</details>

### pyvrl

Exposes Vector VRL to Python

`pip install pyvrl` · installs from source (sdist only) · licence: MIT License · rank 6478 · last release 2024-05-16 · [PyPI](https://pypi.org/project/pyvrl/)

<details><summary>README extract</summary>

Exposes Vector VRL to Python for fast, simple & unified transforms

Example:
```python
>>> from pyvrl import Transform
>>> data: dict = {"x": "foo"}
>>> vrl_program = '''
... .y = "bar"
... .x = upcase!(.x)
... .z = uuid_v7()
... .
... '''
>>> transform = Transform(vrl_program)
>>> output = transform.remap(data)
>>> print(output)
{'x': 'FOO', 'y': 'bar', 'z': '018f79d0-812b-7f90-bc74-85042e23db44'}
```

Sections: pyVRL, Use

</details>

### pytest-plugin-utils

Reusable configuration and artifact utilities for building pytest plugins

`pip install pytest-plugin-utils` · installs (wheel) · licence: not stated · rank 6486 · last release 2026-05-04 · [PyPI](https://pypi.org/project/pytest-plugin-utils/) · [source](https://github.com/iloveitaly/pytest-plugin-utils)

<details><summary>README extract</summary>

Building pytest plugins means dealing with the same problems repeatedly: managing configuration options with proper precedence (CLI vs INI vs defaults), creating per-test artifact directories, and sanitizing test names for filesystem paths. This package extracts those common patterns into reusable utilities. ...

Features:
* Centralized option registry with runtime, CLI, and INI support
* Automatic INI type inference from Python type hints (bool, str, list[str], list[Path])
* Smart value casting with fallback precedence handling
* Filesystem-safe test name ...

Example:
```python
set_pytest_option(
    package,
    "playwright_kwargs",
    default={},
    available=None,  # Runtime only
    type_hint=dict,
)
```

...

</details>

### pytest-playwright-visual-snapshot

Easy pytest visual regression testing using playwright

`pip install pytest-playwright-visual-snapshot` · installs (wheel) · licence: not stated · rank 6490 · last release 2026-02-05 · [PyPI](https://pypi.org/project/pytest-playwright-visual-snapshot/) · [source](https://github.com/iloveitaly/pytest-playwright-visual-snapshot)

<details><summary>README extract</summary>

Example:
```python
def test_myapp(page, assert_snapshot: AssertSnapshot):
    page.goto("
    assert_snapshot(page)
```

Sections: Usage, Configuration, Masking Elements, Handling Size Differences, Disabling Visual Snapshots Locally, GitHub Actions Script, API, Fixture Parameters, Command Line Options, Alternatives

</details>

### pulumi-snowflake

A Pulumi package for creating and managing snowflake cloud resources.

`pip install pulumi-snowflake` · installs (wheel) · licence: Apache-2.0 · rank 6494 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pulumi-snowflake/) · [source](https://github.com/pulumi/pulumi-snowflake)

<details><summary>README extract</summary>

The Snowflake Resource Provider lets you manage Snowflake resources.

Sections: Snowflake Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pytest-skip-slow

A pytest plugin to skip `@pytest.mark.slow` tests by default.

`pip install pytest-skip-slow` · installs (wheel) · licence: MIT · rank 6510 · last release 2026-05-27 · [PyPI](https://pypi.org/project/pytest-skip-slow/)

<details><summary>README extract</summary>

A pytest plugin to skip tests marked as `@pytest.mark.slow` or `@pytest.mark.hugemem` by default.
Include the slow tests with `--slow/--run-slow`, or memory-intensive tests with `--hugemem/--run-hugemem`.

Example:
```python
import pytest

def test_normal():
    pass

@pytest.mark.slow
def test_slow():
    pass
```

Sections: pytest-skip-slow, Usage

</details>

### PyDrive

Google Drive API made easy.

`pip install PyDrive` · installs from source (sdist only) · licence: LICENSE · rank 6518 · last release 2016-10-24 · [PyPI](https://pypi.org/project/PyDrive/)

<details><summary>README extract</summary>

*PyDrive* is a wrapper library of
google-api-python-client
that simplifies many common Google Drive API tasks.

- Documentation: Official documentation on GitHub pages

Features:
- Simplifies OAuth2.0 into just few lines with flexible settings.
- Wraps Google Drive API into
 classes of each resource to make your program more object-oriented. ...

Example:
```python
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
```

Sections: PyDrive, Project Info, Features of PyDrive, OAuth made easy, File management made easy, File listing pagination made easy, Create httplib.Http() object., Create file object to upload.

</details>

### python-cinderclient

OpenStack Block Storage API Client Library

`pip install python-cinderclient` · installs (wheel) · licence: Apache Software License · rank 6552 · last release 2026-09-01 · [PyPI](https://pypi.org/project/python-cinderclient/) · [source](https://opendev.org/openstack/python-cinderclient)

<details><summary>README extract</summary>

This is a client for the OpenStack Cinder API. There's a Python API (the
`cinderclient` module), and a command-line script (`cinder`). Each
implements 100% of the OpenStack Cinder API.

See the OpenStack CLI Reference for information on how to use the `cinder`
command-line tool. You may also want to look at the
OpenStack API documentation. ...

Example:
```python
usage: cinder [--version] [-d] [--os-auth-system <auth-system>]
              [--service-type <service-type>] [--service-name <service-name>]
              [--volume-service-name <volume-service-name>]
              [--os-endpoint-type <os-endpoint-type>]
              [--endpoint-type <endpoint-type>]
...
```

Sections: Python bindings to the OpenStack Cinder API, Command-line API, Python API

</details>

### python-louvain

Louvain algorithm for community detection

`pip install python-louvain` · installs from source (sdist only) · licence: BSD License · rank 6555 · last release 2022-01-29 · [PyPI](https://pypi.org/project/python-louvain/)

### pytun-pmd3

python-pytun fork with darwin and windows support (IPv6-ONLY)

`pip install pytun-pmd3` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6578 · last release 2026-01-27 · [PyPI](https://pypi.org/project/pytun-pmd3/)

_README extract left out: share-alike licence._

### packmol

Packmol - Creates Initial Configurations for Molecular Dynamics Simulations

`pip install packmol` · installs (wheel) · licence: MIT License · rank 6594 · last release 2026-05-27 · [PyPI](https://pypi.org/project/packmol/) · [source](https://github.com/m3g/packmol)

<details><summary>README extract</summary>

Packmol - Creates Initial Configurations for Molecular Dynamics Simulations

Packmol creates an initial point for molecular dynamics simulations by packing molecules in defined regions of space. The packing guarantees that short range repulsive interactions do not disrupt the simulations. ...

Sections: Packmol, What is Packmol, Usage, Multi-platform package provider with Julia, Manual compilation, Using `make`, Using the Fortran Package Manager (`fpm`), References

</details>

### python_speech_features

Python Speech Feature extraction

`pip install python_speech_features` · installs from source (sdist only) · licence: MIT · rank 6603 · last release 2017-08-16 · [PyPI](https://pypi.org/project/python_speech_features/)

### pygnuutils

A python implementation for GNU utils

`pip install pygnuutils` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6606 · last release 2023-05-12 · [PyPI](https://pypi.org/project/pygnuutils/)

_README extract left out: share-alike licence._

### pycrashreport

Pure python3 for parsing Apple's crash reports

`pip install pycrashreport` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6611 · last release 2026-03-30 · [PyPI](https://pypi.org/project/pycrashreport/)

_README extract left out: share-alike licence._

### PIMS

Python Image Sequence

`pip install PIMS` · installs from source (sdist only) · licence: BSD-3-clause · rank 6648 · last release 2024-06-10 · [PyPI](https://pypi.org/project/PIMS/)

<details><summary>README extract</summary>

What Problem Does PIMS Solve?

Scientific video can be packaged in various ways: familiar video formats like
.AVI and .MOV, folders full of numbered images, or "stacks" of TIFF images. Each
of these requires a separate Python module. ...

</details>

### python-amazon-sp-api

Python wrapper for the Amazon Selling-Partner API

`pip install python-amazon-sp-api` · installs (wheel) · licence: MIT · rank 6654 · last release 2026-11-07 · [PyPI](https://pypi.org/project/python-amazon-sp-api/)

<details><summary>README extract</summary>

A wrapper to access Amazon's Selling Partner API with an easy-to-use interface.

Example:
```python
from sp_api.api import Orders
from sp_api.api import Reports
from sp_api.api import DataKiosk
from sp_api.api import Feeds
from sp_api.base import SellingApiException
from sp_api.base.reportTypes import ReportType
from datetime import datetime, timedelta, timezone

# DATA KIOSK API
client = DataKiosk()

...
```

Sections: PYTHON-AMAZON-SP-API, Amazon Selling-Partner API, New Features, 🌟 Thank you for using python-amazon-sp-api! 🌟, Documentation, Q & A, Usage, Async Usage, New endpoints, ADVERTISING API, DISCLAIMER, Base Client

</details>

### paragraphs

Incorporate long strings painlessly, beautifully into Python code.

`pip install paragraphs` · installs (wheel) · licence: MIT · rank 6659 · last release 2026-10-28 · [PyPI](https://pypi.org/project/paragraphs/)

<details><summary>README extract</summary>

Incorporate long strings painlessly, beautifully into Python code.

Features:
Joins lines. Removes indentation and leading whitespace.

Ignores one leading newline.

Separates paragraphs with double newline (`"\n\n"`).

Retains one trailing newline (if present).

Example:
```python
from paragraphs import par

class SuddenDeathError(Exception):
    def init(self, cause: str) -> None:
        self.cause = cause

    def str(self) -> str:
        return par(
            f"""
            Y - e - e - e - es, Lord love you! Why should she die of
            {self.cause}? She come through diphtheria right enough the year
...
```

Sections: paragraphs, Examples, Use, Features, Notes

</details>

### py-consul

Python client for Consul (http://www.consul.io/)

`pip install py-consul` · installs (wheel) · licence: MIT License · rank 6660 · last release 2026-10-26 · [PyPI](https://pypi.org/project/py-consul/)

<details><summary>README extract</summary>

Status

This project is maintained and actively developed by Criteo.
We aim at converging towards a full compatibility with the official Consul API.

We're currently supporting consul 1.20 up to 1.22. Due to quite a few changes
since our development started (see section "A bit of history"), some endpoints are
still partially handled. ...

Example:
```python
import consul

c = consul.Consul()

# poll a key for updates
index = None
while True:
    index, data = c.kv.get('foo', index=index)
    print data['Value']

# in another process
c.kv.put('foo', 'bar')
```

Sections: py-consul, 1.5.5, 1.5.4, 1.5.3, 1.5.2, 1.5.1, 1.5.0, 1.4.1, 1.3.0, 1.2.4, 1.2.3, 1.2.2, 1.2.1, 1.2.0

</details>

### pybars4

Handlebars.js templating for Python 3

`pip install pybars4` · installs from source (sdist only) · licence: GNU Library or Lesser General Public License (LGPL) · rank 6677 · last release 2021-04-04 · [PyPI](https://pypi.org/project/pybars4/)

_README extract left out: share-alike licence._

### pyclang

A python clang-tidy runner

`pip install pyclang` · installs (wheel) · licence: MIT License · rank 6694 · last release 2026-07-13 · [PyPI](https://pypi.org/project/pyclang/)

<details><summary>README extract</summary>

Example:
```python
import os

from pyclang import Runner

# all the dirs you want to run clang-tidy in, will use this value to pass to all chained methods automatically
runner = Runner([os.path.join(os.environ['IDF_PATH'], 'examples', 'get-started', 'hello_world')])
runner.idf_reconfigure().normalize()  # each function is a step, all these steps are chainable
...
```

Sections: Clang Tidy Runner, Examples, Use as a script

</details>

### pksuid

Python package for generating prefixed ksuids.

`pip install pksuid` · installs (wheel) · licence: MIT License · rank 6696 · last release 2022-05-07 · [PyPI](https://pypi.org/project/pksuid/) · [source](https://github.com/sashahilton00/python-pksuid)

<details><summary>README extract</summary>

This library provides an enhancement to the KSUID identifier
first proposed and used by Segment.io, whose reference implementation
exists here:

This library extends the KSUID specification as the `PKSUID` specification
with a prefix, inspired by the Stripe prefixed IDs, such as `txn_1032HU2eZvKYlo2CEPtcnUvl`. ...

Example:
```python
from pksuid import PKSUID

# generate a new unique identifier with the prefix usr
uid = PKSUID('usr')

# returns 'usr_24OnhzwMpa4sh0NQmTmICTYuFaD'
print(uid)

# returns: usr
print(uid.get_prefix())

# returns: 1643510623
print(uid.get_timestamp())

# returns: 2022-01-30 02:43:43
print(uid.get_datetime())

...
```

Sections: Python-PKSUID, (Prefixed K-Sortable Unique IDentifier), Usage

</details>

### py-sr25519-bindings

Python bindings for schnorrkel RUST crate

`pip install py-sr25519-bindings` · installs (wheel) · licence: Apache Software License · rank 6697 · last release 2026-06-15 · [PyPI](https://pypi.org/project/py-sr25519-bindings/) · [source](https://github.com/polkascan/py-sr25519-bindings)

<details><summary>README extract</summary>

Python bindings for sr25519 library:

Reference to and for the initial work

Example:
```python
import bip39
import sr25519

message = b"test"

# Get private and public key from seed
seed = bip39.bip39_to_mini_secret('daughter song common combine misery cotton audit morning stuff weasel flee field','')

public_key, private_key = sr25519.pair_from_seed(bytes(seed))

# Generate signature
signature = sr25519.sign(
    (public_key, private_key),
...
```

Sections: py-sr25519-bindings, Documentation, Build wheels, Usage

</details>

### pytest-shared-session-scope

Pytest session-scoped fixture that works with xdist

`pip install pytest-shared-session-scope` · installs (wheel) · licence: not stated · rank 6711 · last release 2025-10-31 · [PyPI](https://pypi.org/project/pytest-shared-session-scope/)

<details><summary>README extract</summary>

Session scoped fixture that is shared between all workers in a pytest-xdist run.

<!--- doctest:main --->

It differs from normal fixtures in two ways:
- If it yields it must yield twice - once to optionally calculate the value, once to yield the value to the test
- If it yields, a `SetupToken` or calculated data is send back in the first yield. ...

Features:
This helps avoid one of the most classic pytest pitfalls: session-scoped fixtures are run in each xdist worker.
This is a special case of the more general pytest pitfall of thinking that if something works, it will also work with xdist.

Example:
```python
from pytest_shared_session_scope import shared_session_scope_json, CleanupToken, SetupToken

def expensive_calculation():
  return 123

def clean_up(data):
...

</details>

### pipupgrade

UPGRADE ALL THE PIP PACKAGES!

`pip install pipupgrade` · installs (wheel) · licence: MIT License · rank 6725 · last release 2022-02-16 · [PyPI](https://pypi.org/project/pipupgrade/)

<details><summary>README extract</summary>

Features:
* Updates system packages and local packages.
* Discovers packages present within multiple Python Environments.
* Updates packages mentioned within a `requirements.txt` file (Also pins up-to-date versions if mentioned). ...

Example:
```python
$ pipupgrade --help
usage: pipupgrade [--pip-path PIP_PATH] [-y] [-c]
                  [--upgrade-type {major,minor,patch} [{major,minor,patch} ...]]
                  [-l] [-f {table,tree,json,yaml}] [-a] [--pip] [-s]
                  [-r REQUIREMENTS] [--pipfile PIPFILE] [-i] [-p PROJECT]
...
```

Sections: pipupgrade, The missing command for pip, Features, Quick Start, Usage, Basic Usage, Docker, Similar Packages, Known Issues

</details>

### pyspark-hnsw

(no summary)

`pip install pyspark-hnsw` · installs (wheel) · licence: not stated · rank 6730 · last release 2022-12-30 · [PyPI](https://pypi.org/project/pyspark-hnsw/)

### pysubtypes

Provides subclasses for common python types with additional functionality and convenience methods.

`pip install pysubtypes` · installs (wheel) · licence: MIT · rank 6733 · last release 2021-02-01 · [PyPI](https://pypi.org/project/pysubtypes/)

<details><summary>README extract</summary>

This library is currently still under development. The API will likely undergo significant changes that may break any code you write with it.
The documentation will fall out of sync with the updates regularly until development slows down. Use it at your own risk.

Features:
Provides subclasses for certain python builtins (str, list, dict) and common complex types (datetime, Enum, DataFrame, BeautifulSoup) which add functionality and
convenience methods/properties. ...

Sections: PLEASE NOTE, Overview, Usage

</details>

### pymiscutils

Provides a wide range of useful classes and functions.

`pip install pymiscutils` · installs (wheel) · licence: MIT · rank 6739 · last release 2021-02-01 · [PyPI](https://pypi.org/project/pymiscutils/)

<details><summary>README extract</summary>

This library is currently still under development. The API will likely undergo significant changes that may break any code you write with it.
The documentation will fall out of sync with the updates regularly until development slows down. Use it at your own risk.

Features:
Provides a wide range of useful classes and functions:

The `NestedParser` class

* Parse a string by user-specified opening/closing tokens, recursively
* Can ignore tokens between specific tags (for example, within string quotation marks)
* Return ...

Sections: PLEASE NOTE, Overview, Usage

</details>

### pathmagic

Provides ORM path classes (File and Dir), which automatically emit file system IO operations upon having their attributes modified. File objects allow for easy content manipulation of many forms of files.

`pip install pathmagic` · installs (wheel) · licence: MIT · rank 6741 · last release 2021-02-01 · [PyPI](https://pypi.org/project/pathmagic/)

<details><summary>README extract</summary>

This library is currently still under development. The API will likely undergo significant changes that may break any code you write with it.
The documentation will fall out of sync with the updates regularly until development slows down. Use it at your own risk.

Features:
Pathmagic implements two classes, `File` and `Dir`, to represent mapped file system obects in a manner similar to database ORMs like sqlalchemy. ...

Sections: PLEASE NOTE, Overview, Usage

</details>

### pyiotools

Provides several utilities for handling I/O

`pip install pyiotools` · installs (wheel) · licence: MIT · rank 6742 · last release 2021-02-01 · [PyPI](https://pypi.org/project/pyiotools/)

<details><summary>README extract</summary>

This library is currently still under development. The API will likely undergo significant changes that may break any code you write with it.
The documentation will fall out of sync with the updates regularly until development slows down. Use it at your own risk.

Features:
Provides several utilities for handling I/O:

The `IOHandler` class

* Api similar to `argparse.ArgumentParser()`. Must be used as a context manager, and while in scope the `Argument.add()` method will act equivalent to ...

Sections: PLEASE NOTE, Overview, Usage

</details>

### pdfid

PDFID simple tool to analyze PDF malicious files by DidierStevens. Customized by Matteo Lodi to be used as a library.

`pip install pdfid` · installs (wheel) · licence: MIT License · rank 6782 · last release 2023-06-06 · [PyPI](https://pypi.org/project/pdfid/)

<details><summary>README extract</summary>

This is a clone of Didier Steven's tool created to publish it into Pypi and make it usable as a library.

See `test.py` for an example of usage

</details>

### python-ffmpeg

A python binding for FFmpeg which provides sync and async APIs

`pip install python-ffmpeg` · installs (wheel) · licence: MIT License · rank 6791 · last release 2024-04-15 · [PyPI](https://pypi.org/project/python-ffmpeg/)

<details><summary>README extract</summary>

A python binding for FFmpeg which provides sync and async APIs

See documentation for more details.

Example:
```python
from ffmpeg import FFmpeg

def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("input.mp4")
        .output(
            "output.mp4",
            {"codec:v": "libx264"},
            vf="scale=1280:-1",
            preset="veryslow",
            crf=24,
        )
    )

    ffmpeg.execute()

if name == "main":
    main()
```

Sections: python-ffmpeg, Help, Examples, Transcoding, Synchronous API, Asynchronous API, Recording

</details>

### pipelinewise-singer-python

Singer.io utility library - PipelineWise compatible

`pip install pipelinewise-singer-python` · does not install on CPython 3.14 · licence: Apache Software License · rank 6811 · last release 2026-04-22 · [PyPI](https://pypi.org/project/pipelinewise-singer-python/)

<details><summary>README extract</summary>

Writes the Singer format from Python.

This is a fork of Singer's singer-python made for PipelineWise.

Usage

This library depends on python3. We recommend using a `virtualenv` like this:

Example:
```python
import singer

singer.write_schema('my_table',
                {'properties':{'id': {'type': 'string', 'key': True}}},
            ['id'])
singer.write_records('my_table',
                     [{'id': 'b'}, {'id':'d'}])
singer.write_state({'my_table': 'd'})
```

Sections: pipelinewise-singer-python, Setup environment, Usage example, Logging configuration

</details>

### pyroma

Test your project's packaging friendliness

`pip install pyroma` · installs (wheel) · licence: MIT License · rank 6821 · last release 2025-12-09 · [PyPI](https://pypi.org/project/pyroma/) · [source](https://github.com/regebro/pyroma)

<details><summary>README extract</summary>

Pyroma rhymes with aroma, and is a product aimed at giving a rating of how well
a Python project complies with the best practices of the Python packaging
ecosystem, primarily PyPI, pip, Distribute etc, as well as a list of issues that
could be improved. ...

Sections: pyroma, Tests, Version control integration, 5.0.1 (2025-12-09), 5.0 (2025-07-15), 5.0b2 (2025-07-10), 5.0b1 (2025-07-04), 5.0a1 (2025-07-02), 4.3.3 (2025-07-03), 4.3.2 (2025-07-02), 4.3.1 (2025-07-01), 4.3 (2025-07-01), 4.2 (2023-02-25), 4.1 (2022-11-24)

</details>

### pulumi-databricks

A Pulumi package for creating and managing databricks cloud resources.

`pip install pulumi-databricks` · installs (wheel) · licence: Apache-2.0 · rank 6861 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pulumi-databricks/) · [source](https://github.com/pulumi/pulumi-databricks)

<details><summary>README extract</summary>

The Databricks Resource Provider lets you manage Databricks resources.

Sections: Databricks Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pytorch-msssim

Fast and differentiable MS-SSIM and SSIM for pytorch.

`pip install pytorch-msssim` · installs (wheel) · licence: MIT License · rank 6876 · last release 2023-05-25 · [PyPI](https://pypi.org/project/pytorch-msssim/)

<details><summary>README extract</summary>

Fast and differentiable MS-SSIM and SSIM for pytorch.

Features:
Gaussian kernels used in SSIM & MS-SSIM are seperable. A separable filter in image processing can be written as product of two more simple filters. Typically a 2-dimensional convolution operation is separated into two 1-dimensional filters. ...

Example:
```python
from pytorch_msssim import ssim, ms_ssim, SSIM, MS_SSIM
# X: (N,3,H,W) a batch of non-negative RGB images (0~255)
# Y: (N,3,H,W)

# calculate ssim & ms-ssim for each image
ssim_val = ssim( X, Y, data_range=255, size_average=False) # return (N,)
ms_ssim_val = ms_ssim( X, Y, data_range=255, size_average=False ) #(N,)

...
```

...

</details>

### python-novaclient

Client library for OpenStack Compute API

`pip install python-novaclient` · installs (wheel) · licence: Apache Software License · rank 6877 · last release 2026-08-28 · [PyPI](https://pypi.org/project/python-novaclient/)

<details><summary>README extract</summary>

This is a client for the OpenStack Compute API. It provides a Python API (the
`novaclient` module) and a deprecated command-line script (`nova`). The
Python API implements 100% of the OpenStack Compute API. ...

Sections: Team and repository tags, Python bindings to the OpenStack Compute API

</details>

### pulumiverse-time

A Pulumi package for creating and managing Time resources

`pip install pulumiverse-time` · installs from source (sdist only) · licence: Apache-2.0 · rank 6890 · last release 2024-12-29 · [PyPI](https://pypi.org/project/pulumiverse-time/) · [source](https://github.com/pulumiverse/pulumi-time)

<details><summary>README extract</summary>

The Time Resource Provider lets you manage time resources.

Sections: Time Resource Provider, Node.js (JavaScript/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pulumi-eks

Pulumi Amazon Web Services (AWS) EKS Components.

`pip install pulumi-eks` · installs (wheel) · licence: Apache-2.0 · rank 6909 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pulumi-eks/) · [source](https://github.com/pulumi/pulumi-eks)

<details><summary>README extract</summary>

The Pulumi EKS library provides a Pulumi component that creates and manages the resources necessary to run an EKS Kubernetes cluster in AWS. This component exposes the Crosswalk for AWS functionality documented in the Pulumi Elastic Kubernetes Service guide as a package available in all Pulumi languages.

This includes: ...

Sections: Pulumi Amazon Web Services (AWS) EKS Components, Node.js (JavaScript/TypeScript), Python, Go, .NET, Node.js compatibility warnings, References

</details>

### policyuniverse

Parse and Process AWS IAM Policies, Statements, ARNs, and wildcards.

`pip install policyuniverse` · installs (wheel) · licence: Apache Software License · rank 6912 · last release 2023-11-30 · [PyPI](https://pypi.org/project/policyuniverse/)

<details><summary>README extract</summary>

This package provides classes to parse AWS IAM and Resource Policies.

Additionally, this package can expand wildcards in AWS Policies using permissions obtained from the AWS Policy Generator.

See the Service and Permissions data.

_This package can also minify an AWS policy to help you stay under policy size limits. ...

Example:
```python
from policyuniverse.arn import ARN
arn = ARN('arn:aws:iam::012345678910:role/SomeTestRoleForTesting')
assert arn.error == False
assert arn.tech == 'iam'
assert arn.region == ''  # IAM is universal/global
assert arn.account_number == '012345678910'
assert arn.name == 'role/SomeTestRoleForTesting'
assert arn.partition == 'aws'
...
```

...

</details>

### python-tss-sdk

The Delinea Secret Server Python SDK

`pip install python-tss-sdk` · installs (wheel) · licence: Apache Software License · rank 6919 · last release 2025-11-03 · [PyPI](https://pypi.org/project/python-tss-sdk/)

<details><summary>README extract</summary>

The Delinea Secret Server Python SDK contains classes that interact with Secret Server via their REST APIs.

Example:
```python
from delinea.secrets.server import PasswordGrantAuthorizer

authorizer = PasswordGrantAuthorizer(" os.getenv("myusername"), os.getenv("password"))
```

Sections: The Delinea Secret Server Python SDK, Secret Server Authentication, Usage, With Secret Server, With Platform, Secret Server Cloud, Useage, Initializing SecretServer

</details>

### pip-hello-world

Hello World testing setuptools

`pip install pip-hello-world` · installs from source (sdist only) · licence: BSD · rank 6928 · last release 2017-03-23 · [PyPI](https://pypi.org/project/pip-hello-world/)

### pylzss

A Python library for decoding/encoding LZSS-compressed data.

`pip install pylzss` · installs (wheel) · licence: LGPL-3.0-only · rank 6948 · last release 2026-10-17 · [PyPI](https://pypi.org/project/pylzss/) · [source](https://github.com/m1stadev/pylzss)

_README extract left out: share-alike licence._

### pptx2md

This package converts pptx to markdown

`pip install pptx2md` · installs (wheel) · licence: Other/Proprietary License · rank 6964 · last release 2024-12-03 · [PyPI](https://pypi.org/project/pptx2md/) · [source](https://github.com/ssine/pptx2md)

### python-datauri

A li'l class for data URI manipulation in Python

`pip install python-datauri` · installs (wheel) · licence: The Unlicense (Unlicense) · rank 7003 · last release 2025-01-03 · [PyPI](https://pypi.org/project/python-datauri/)

<details><summary>README extract</summary>

Data URI manipulation made easy.

This isn't very robust, and will reject a number of valid data URIs. However, it meets the most useful case: a mimetype, a charset, and the base64 flag.

Example:
```python
>>> from datauri import DataURI
>>> uri = DataURI('data:text/plain;charset=utf-8;base64,VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2cu')
>>> uri.mimetype
'text/plain'
>>> uri.charset
'utf-8'
>>> uri.is_base64
True
>>> uri.data
b'The quick brown fox jumped over the lazy dog.'
```

Sections: DataURI, Parsing, Creating from a string, Creating from a file, Serializing

</details>

### pylibmc

Quick and small memcached client for Python

`pip install pylibmc` · installs from source (sdist only) · licence: 3-clause BSD <https://opensource.org/licenses/bsd-license.php> · rank 7009 · last release 2022-08-30 · [PyPI](https://pypi.org/project/pylibmc/) · [source](https://github.com/lericson/pylibmc)

<details><summary>README extract</summary>

`pylibmc` is a Python client for memcached written in C.

See the documentation at sendapatch.se/projects/pylibmc/_ for more information.


Though no major feature overhauls have taken place, this release is partially
incompatible with 1.5.0. ...

Sections: New in version 1.6.0, New in version 1.5.0, New in version 1.4.0

</details>

### pwlf

fit piecewise linear functions to data

`pip install pwlf` · installs (wheel) · licence: MIT License · rank 7021 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pwlf/)

<details><summary>README extract</summary>

A library for fitting continuous piecewise linear functions to data. Just specify the number of line segments you desire and provide the data.

Check out the documentation!

Read the blog post.

Now you can perform segmented constant fitting and piecewise polynomials!

Features:
For a specified number of line segments, you can determine (and predict from) the optimal continuous piecewise linear function f(x). See this example. ...

Sections: About, Features, Python Package Index (PyPI), Conda, From source, How it works, Requirements

</details>

### python-ripgrep

A Python wrapper for ripgrep

`pip install python-ripgrep` · does not install on CPython 3.14 · licence: MIT License · rank 7031 · last release 2025-07-30 · [PyPI](https://pypi.org/project/python-ripgrep/)

### pandas-read-xml

A tool to read XML files as pandas dataframes.

`pip install pandas-read-xml` · installs (wheel) · licence: MIT License · rank 7032 · last release 2021-04-08 · [PyPI](https://pypi.org/project/pandas-read-xml/)

<details><summary>README extract</summary>

A tool to help read XML files as pandas dataframes.

See example in Google Colab here

Isn't it annoying working with data in XML format? I think so. Take a look at this simple example.

I wish there was a simple `df = pd.read_xml('some_file.xml')` like `pd.read_csv()` and `pd.read_json()` that we all love. ...

Example:
```python
import pandas_read_xml as pdx
```

Sections: Pandas Read XML, Import package, Read XML as pandas dataframe, Auto Flatten

</details>

### pulumiverse-grafana

A Pulumi package for creating and managing grafana.

`pip install pulumiverse-grafana` · installs (wheel) · licence: Apache-2.0 · rank 7047 · last release 2026-10-21 · [PyPI](https://pypi.org/project/pulumiverse-grafana/) · [source](https://github.com/pulumiverse/pulumi-grafana)

<details><summary>README extract</summary>

The grafana resource provider for Pulumi lets you creating resources in grafana. To use
this package, please install the Pulumi CLI first.

Sections: grafana Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Reference

</details>

### pyreqwest

Powerful and fast Rust based HTTP client

`pip install pyreqwest` · installs (wheel) · licence: not stated · rank 7085 · last release 2026-10-23 · [PyPI](https://pypi.org/project/pyreqwest/) · [source](https://github.com/MarkusSintonen/pyreqwest)

<details><summary>README extract</summary>

pyreqwest - Powerful and fast Rust based HTTP client. Built on top of and inspired by reqwest.

Features:
- No reinvention of the wheel - built on top of widely used reqwest and other Rust HTTP crates
- Secure and fast - no C-extension code, no Python code/dependencies, no `unsafe` code ...

Example:
```python
# uv add pyreqwest

from pyreqwest.client import ClientBuilder, SyncClientBuilder

async def example_async():
    async with ClientBuilder().error_for_status(True).build() as client:
        response = await client.get(" "val"}).build().send()
        print(await response.json())

def example_sync():
...
```

Sections: Why, Features, Standard HTTP features you would expect, Quickstart, Mocking in pytest, Simple request interface, Documentation, Compatibility with other libraries

</details>

### planetary-computer

Planetary Computer SDK for Python

`pip install planetary-computer` · installs (wheel) · licence: not stated · rank 7086 · last release 2023-07-05 · [PyPI](https://pypi.org/project/planetary-computer/)

<details><summary>README extract</summary>

Python library for interacting with the Microsoft Planetary Computer.

For general questions or discussions about the Planetary Computer, use the microsoft/PlanetaryComputer repository.

Example:
```python
import planetary_computer
import pystac_client

from pystac_client import Client
import planetary_computer, requests
api = Client.open(
   '
   modifier=planetary_computer.sign_inplace,
)
```

Sections: Planetary Computer SDK for Python, Usage, Automatic signing, Manual signing, Convenience methods, Trademarks

</details>

### pyzipcode

query zip codes and location data

`pip install pyzipcode` · installs from source (sdist only) · licence: MIT License · rank 7127 · last release 2021-03-03 · [PyPI](https://pypi.org/project/pyzipcode/)

<details><summary>README extract</summary>

This package will allow you to get zip code information. The data used in this
package can be retrieved from

`pyzipcode` uses a local sqlite database to run. You can replace it with your
own other storage mechanism with a little effort.

Here is some basic usage...

Search zip codes... ...

Example:
```python
>>> from pyzipcode import ZipCodeDatabase
>>> zcdb = ZipCodeDatabase()

>>> zcdb[54115]
ZipCode(zip='54115', city='De Pere', state='WI', longitude=-88.07896, latitude=44.42042, timezone=-6, dst=1)
>>> zcdb[210]
ZipCode(zip='00210', city='Portsmouth', state='NH', longitude=-71.013202, latitude=43.005895, timezone=-5, dst=1)
```

Sections: Introduction, The Data, 3.0.0 (2021-03-03), 2.0.2 (2021-02-28), 2.0.1 (2021-02-25), 2.0.0 (2020-04-07), 0.3, 0.2, 0.1

</details>

### pqdm

PQDM is a TQDM and concurrent futures wrapper to allow enjoyable paralellization of progress bars.

`pip install pqdm` · installs (wheel) · licence: MIT License · rank 7181 · last release 2022-02-14 · [PyPI](https://pypi.org/project/pqdm/)

<details><summary>README extract</summary>

PQDM is a TQDM and concurrent futures wrapper to allow enjoyable paralellization of
iterating through an Iterable with a progress bar.

* Free software: MIT license

Features:
* parellize your tqdm runs using processes or threads thanks to concurrent.futures,
* just import `pqdm` from `pqdm.threads` or `pqdm.processes` to start,
* automatic usage of `tqdm.notebook` when iPython/Jupyter notebook environment detected, ...

Sections: Parallel TQDM, Features, 0.2.0 (2022-02-14), 0.1.0 (2020-03-07), 0.0.1 (2020-03-05)

</details>

### pydefect

Integrated environment for first-principles point-defect calculations

`pip install pydefect` · installs (wheel) · licence: MIT License · rank 7196 · last release 2026-05-25 · [PyPI](https://pypi.org/project/pydefect/)

### pytest-csv

CSV output for pytest.

`pip install pytest-csv` · installs (wheel) · licence: GNU General Public License (GPL) · rank 7199 · last release 2021-04-22 · [PyPI](https://pypi.org/project/pytest-csv/)

_README extract left out: share-alike licence._

### proces

text preprocess.

`pip install proces` · installs (wheel) · licence: MIT License · rank 7215 · last release 2023-09-09 · [PyPI](https://pypi.org/project/proces/)

<details><summary>README extract</summary>

🐨 文本预处理。

> ⚠️ 注意：
> 1. 本地安装仅支持 Python 的 3.6 以上版本；
> 2. 尽可能使用 `proces` 的最新版本。

Example:
```python
from proces import preprocess

# 默认会按照顺序执行，处理空白字符、大写转小写、繁体转简体、全角转半角
result = preprocess("Today, 你 幹 什 麼 ！")
# result: today,你干什么!

# 配置 pipeline，比如只去除空白字符
result = preprocess("Today, 你 幹 什 麼 ！", pipelines=["handle_blank_character"])
# result: Today,你幹什麼！

# 单独使用子方法
from proces import filter_unusual_characters, filter
...
```

Sections: Proces, 1 安装, 使用 pip 安装, 从代码库安装, 2 使用, 3 TODO, 4 许可

</details>

### pinecone-plugin-inference

Embeddings plugin for Pinecone SDK

`pip install pinecone-plugin-inference` · installs (wheel) · licence: Apache Software License · rank 7239 · last release 2024-12-10 · [PyPI](https://pypi.org/project/pinecone-plugin-inference/) · [docs](https://pinecone.io/docs)

<details><summary>README extract</summary>

Example:
```python
from pinecone import Pinecone

pc = Pinecone(api_key="<<PINECONE_API_KEY>>")
model = "multilingual-e5-large"

# Embed documents
text = [
    "Turkey is a classic meat to eat at American Thanksgiving.",
    "Many people enjoy the beautiful mosques in Turkey.",
]
text_embeddings = pc.inference.embed(
    model=model,
    inputs=text,
...
```

Sections: Inference API plugin for python SDK, Usage, Generate embeddings

</details>

### pydynamodb

Python DB API 2.0 (PEP 249) client for Amazon DynamoDB

`pip install pydynamodb` · installs (wheel) · licence: MIT License · rank 7242 · last release 2026-04-04 · [PyPI](https://pypi.org/project/pydynamodb/) · [docs](https://github.com/passren/PyDynamoDB/wiki) · [source](https://github.com/passren/PyDynamoDB)

<details><summary>README extract</summary>

PyDynamoDB is a Python DB API 2.0 (PEP 249) client for Amazon DynamoDB.
SQLAlchemy dialect supported as well.

PyDynamoDB implement the DB API 2.0 interfaces based on PartiQL supported by AWS DynamoDB. \
Although PartiQL can only support DML operations (INSERT, UPDATE, DELETE, SELECT), PyDynamoDB \
extended the capabilities to support DDL as well. ...

Features:
* Compatible with DB API 2.0 Specification
* PartiQL for DML operations (INSERT, UPDATE, DELETE, SELECT)
* Limit supported in SELECT statement
* Extra type conversion and string functions supported in SELECT statement
* Column alias supported in ...

Example:
```python
from pydynamodb import connect

cursor = connect(aws_access_key_id="aws_access_key_id",
                aws_secret_access_key="aws_secret_access_key",
...

</details>

### pyap

Pyap is an MIT Licensed text processing library, written in Python, for detecting and parsing addresses. Currently it supports USA, Canadian and British addresses.

`pip install pyap` · installs (wheel) · licence: MIT License · rank 7256 · last release 2020-09-30 · [PyPI](https://pypi.org/project/pyap/) · [docs](https://github.com/vladimarius/pyap)

<details><summary>README extract</summary>

Pyap is an MIT Licensed text processing library, written in Python, for
detecting and parsing addresses. Currently it supports US 🇺🇸, Canadian 🇨🇦 and British 🇬🇧 addresses.

Example:
```python
>>> import pyap
>>> test_address = """
    Lorem ipsum
    225 E. John Carpenter Freeway,
    Suite 1500 Irving, Texas 75062
    Dorem sit amet
    """
>>> addresses = pyap.parse(test_address, country='US')
>>> for address in addresses:
        # shows found address
        print(address)
        # shows address parts
...
```

Sections: Pyap: Python address parser, About, Future work, Typical workflow, Limitations

</details>

### pesq

Python Wrapper for PESQ Score (narrow band and wide band)

`pip install pesq` · installs from source (sdist only) · licence: MIT License · rank 7260 · last release 2022-05-17 · [PyPI](https://pypi.org/project/pesq/)

<details><summary>README extract</summary>

PESQ (Perceptual Evaluation of Speech Quality) Wrapper for Python Users

This code is designed for numpy array specially.

 C compiler
 numpy
 cython

Example:
```python
def pesq(fs, ref, deg, mode='wb', on_error=PesqError.RAISE_EXCEPTION):
    """
    Args:
        ref: numpy 1D array, reference audio signal
        deg: numpy 1D array, degraded audio signal
        fs:  integer, sampling rate
        mode: 'wb' (wide-band) or 'nb' (narrow-band)
...
```

Sections: pesq, Requirements, Usage for narrowband and wideband Modes, Usage for `multiprocessing` feature, Correctness, Note, Who is using `pesq`

</details>

### pymsym

libmsym python binding

`pip install pymsym` · installs (wheel) · licence: MIT License · rank 7282 · last release 2026-05-25 · [PyPI](https://pypi.org/project/pymsym/)

<details><summary>README extract</summary>

libmsym is a C library dealing with point group symmetry in molecules. pymsym is its python interface.

this library was originally developed by Marcus Johansson. the original library can be found here and seems unmaintained - after reaching out to the initial authors, i've decided to fork this so i can maintain it. ...

Example:
```python
import pymsym

# water
atomic_numbers = [8, 1, 1]
positions = [
  [0.007544053252786398, 0.39774343371391296, 0.0],
  [-0.7671031355857849, -0.18439316749572754, 0.0],
  [0.7595590949058533, -0.21335026621818542, 0.0]
 ]

pymsym.get_point_group(atomic_numbers, positions) # returns C2v
...
```

Sections: pymsym, about, api, point groups

</details>

### plotly-resampler

Visualizing large time series with plotly

`pip install plotly-resampler` · installs (wheel) · licence: MIT License · rank 7295 · last release 2026-10-04 · [PyPI](https://pypi.org/project/plotly-resampler/) · [docs](https://predict-idlab.github.io/plotly-resampler/latest) · [source](https://github.com/predict-idlab/plotly-resampler)

<details><summary>README extract</summary>

> `plotly_resampler`: visualize large sequential data by adding resampling functionality to Plotly figures

`plotly-resampler` makes one Plotly trace fast (i.e., line trace). `flexviz` applies the same principle (never ship the raw data to the browser) to a whole dashboard: linked cross-filtering, 10 trace types (lines, histograms, bars, pies, box ...

Example:
```python
import plotly.graph_objects as go; import numpy as np
from plotly_resampler import register_plotly_resampler

# Call the register function once and all Figures/FigureWidgets will be wrapped
# according to the register_plotly_resampler its `mode` argument
register_plotly_resampler(mode='auto')

x = np.arange(1_000_000)
...
```

...

</details>

### pulumi-confluentcloud

A Pulumi package for creating and managing Confluent cloud resources.

`pip install pulumi-confluentcloud` · installs (wheel) · licence: Apache-2.0 · rank 7306 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pulumi-confluentcloud/) · [source](https://github.com/pulumi/pulumi-confluentcloud)

<details><summary>README extract</summary>

The Confluent Resource Provider lets you manage Confluent resources.

Please Note:
This provider is built from the ConfluentInc official Terraform Provider -

Sections: Confluent Cloud Resource Provider, Node.js (JavaScript/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pylightxl

A light weight excel read/writer for python27 and python3 with no dependencies

`pip install pylightxl` · installs from source (sdist only) · licence: MIT License · rank 7307 · last release 2023-01-01 · [PyPI](https://pypi.org/project/pylightxl/)

<details><summary>README extract</summary>

pylightxl - A Light Weight Excel Reader/Writer

 Documentation

 A light weight, zero dependency (only standard libs used), to the point (no bells and whistles)
 Microsoft Excel reader/writer python 2.7.18 - 3+ library.

**Please help us spread the word about pylightxl to the community by voting for pylightxl to be added
to python-awesome list. ...

Features:
- Zero non-standard library dependencies!

 - No compatibility/version control issues.

- Python2.7.18 to Python3+ support for life!

 - Don't worry about which python version you are using, pylightxl will support it for life ...

Sections: High-Level Feature Summary, Limitations, Why pylightxl over pandas/openpyxl/xlrd, Setup

</details>

### Pinterest-Generated-Client

Pinterest REST API

`pip install Pinterest-Generated-Client` · installs (wheel) · licence: MIT · rank 7321 · last release 2026-08-27 · [PyPI](https://pypi.org/project/Pinterest-Generated-Client/)

<details><summary>README extract</summary>

Pinterest's REST API

This Python package is automatically generated by the OpenAPI Generator project:

- API version: 5.14.0
- Package version: 0.1.12
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit

Python >=3.6

Example:
```python
import time
import openapi_generated.pinterest_client
from pprint import pprint
from openapi_generated.pinterest_client.api import ad_accounts_api
from openapi_generated.pinterest_client.model.ad_account import AdAccount
from openapi_generated.pinterest_client.model.ad_account_analytics_response import AdAccountAnalyticsResponse
...
```

...

</details>

### point-cloud-utils

A Python library for common tasks on 3D point clouds and meshes

`pip install point-cloud-utils` · installs from source (sdist only) · licence: MIT License · rank 7326 · last release 2025-04-14 · [PyPI](https://pypi.org/project/point-cloud-utils/)

<details><summary>README extract</summary>

Author: Francis Williams

If Point Cloud Utils contributes to an academic publication, cite it as:

Point Cloud Utils (pcu) is a utility library providing the following functionality for 3D processing point clouds and triangle meshes. ...

Example:
```python
import point_cloud_utils as pcu

# Load vertices and faces for a mesh
v, f = pcu.load_mesh_vf("path/to/mesh")

# Load vertices and per-vertex normals
v, n = pcu.load_mesh_vn("path/to/mesh")

# Load vertices, per-vertex normals, and per-vertex-colors
v, n, c = pcu.load_mesh_vnc("path/to/mesh")

# Load vertices, faces, and per-vertex normals
...
```

...

</details>

### pinterest-api-sdk

Pinterest API SDK

`pip install pinterest-api-sdk` · installs (wheel) · licence: Apache License 2.0 · rank 7333 · last release 2026-09-02 · [PyPI](https://pypi.org/project/pinterest-api-sdk/)

<details><summary>README extract</summary>

The Pinterest SDK currently offers a Python library that supports campaign management and simplifies authentication and error handling. We will be adding functionality supporting organic Pins, shopping, analytics, and more over time. If you have specific feedback about the SDK or requests for additional functionality, please let us know. ...

Example:
```python
from pinterest.ads.campaigns import Campaign
from pinterest.ads.ad_groups import AdGroup
from pinterest.ads.ads import Ad

# Create a new Ad
new_ad = Ad.create(
    ad_account_id="123456789",
    ad_group_id="999999999",
    creative_type="REGULAR",
    pin_id="111111111",
    name="SDK Example Ad",
    status="ACTIVE",
    is_pin_deleted=False,
...
```

...

</details>

### python-tools-scripts

Python Tools Scripts

`pip install python-tools-scripts` · installs (wheel) · licence: Apache Software License · rank 7357 · last release 2024-02-29 · [PyPI](https://pypi.org/project/python-tools-scripts/) · [docs](https://python-tools-scripts.readthedocs.io) · [source](https://github.com/s0undt3ch/python-tools-scripts)

<details><summary>README extract</summary>

This is a tool, similar to invoke.
It's more recent and uses argparse under the hood
and some additional magic to define the CLI arguments.

To use it, you must have a `tools` package in your repository root.
On your `tools/init.py` import your scripts and *Python Tools Scripts* will add them to it's CLI.

Example:
```python
"""
These commands are used to create/destroy VMs, sync the local checkout
to the VM and to run commands on the VM.
"""

from ptscripts import Context, command_group

# Define the command group
vm = command_group(name="vm", help="VM Related Commands", description=doc)

@vm.command(
    arguments={
        "name": {
...
```

Sections: Python Tools Scripts, An Example Script `tools/vm.py`

</details>

### pyproject-flake8

pyproject-flake8 (`pflake8`), a monkey patching wrapper to connect flake8 with pyproject.toml configuration

`pip install pyproject-flake8` · installs (wheel) · licence: not stated · rank 7363 · last release 2024-04-09 · [PyPI](https://pypi.org/project/pyproject-flake8/)

<details><summary>README extract</summary>

A monkey patching wrapper to connect flake8 with `pyproject.toml` configuration.

pyproject-flake8 so far came without explicit pinning of a flake8 version. Since a recent update broke compatibility – not unexpectedly – the issue arose, how to handle incompatible versions of flake8 and pyproject-flake8. ...

Sections: pyproject-flake8 (`pflake8`), Update concerning versioning, Rationale, From github, From PyPI, Building packages, Usage, See also, Caveat

</details>

### PyMatching

A package for decoding quantum error correcting codes using minimum-weight perfect matching.

`pip install PyMatching` · installs (wheel) · licence: Apache 2 · rank 7410 · last release 2026-05-22 · [PyPI](https://pypi.org/project/PyMatching/)

<details><summary>README extract</summary>

PyMatching is a fast Python/C++ library for decoding quantum error correcting (QEC) codes using the Minimum Weight
Perfect Matching (MWPM) decoder.
Given the syndrome measurements from a quantum error correction circuit, the MWPM decoder finds the most probable set
of errors, given the assumption that error mechanisms are _independent_, as well as ...

Example:
```python
import numpy as np
import stim
import pymatching
circuit = stim.Circuit.generated(
    "surface_code:rotated_memory_x",
    distance=5,
    rounds=5,
    after_clifford_depolarization=0.005
)
```

Sections: PyMatching 2, The new >100x faster implementation for Version 2, Correlated matching, Usage, Decoding Stim circuits, Loading from a parity check matrix, Attribution

</details>

### pytapo

Python library for communication with Tapo Cameras

`pip install pytapo` · installs (wheel) · licence: MIT License · rank 7423 · last release 2026-10-23 · [PyPI](https://pypi.org/project/pytapo/)

<details><summary>README extract</summary>

Python library for communication with Tapo Cameras.

Used inside Home Assistant Integration HomeAssistant-Tapo-Control.

- Python3.13
- PIP modules installed

Example:
```python
from pytapo import Tapo

user = "" # user you set in Advanced Settings -> Camera Account
password = "" # password you set in Advanced Settings -> Camera Account
host = "" # ip of the camera, example: 192.168.1.52

tapo = Tapo(host, user, password)

print(tapo.getBasicInfo())
```

Sections: PyTapo, Pre-Requirements, Usage examples, Initiate library, Nightlight, Authentication, Downloading Recordings, Performance notes, Test instructions, Thank you, FAQ, Disclaimer

</details>

### pytorch-ignite

A lightweight library to help with training neural networks in PyTorch.

`pip install pytorch-ignite` · installs (wheel) · licence: BSD-3-Clause · rank 7433 · last release 2026-07-22 · [PyPI](https://pypi.org/project/pytorch-ignite/) · [source](https://github.com/pytorch/ignite)

<details><summary>README extract</summary>

| |

| ・ ・ |
| |
| |
| |

Ignite is a high-level library to help with training and evaluating neural networks in PyTorch flexibly and transparently.

_Click on the image to see complete code

Features:
- Less code than pure PyTorch
 while ensuring maximum control and simplicity

- Library approach and no program's control inversion - _Use ignite where and when you need

- Extensible API for metrics, experiment managers, and other components

Example:
```python
from ignite.engine import Engine, Events, create_supervised_evaluator
from ignite.metrics import Accuracy

# Setup training engine:
def train_step(engine, batch):
    # Users can do whatever they need on a single iteration
    # Eg. forward/backward pass for any number of models, optimizers, etc
    # ...

...

</details>

### pylibraft-cu12

RAFT: Reusable Algorithms Functions and other Tools

`pip install pylibraft-cu12` · installs (wheel) · licence: Apache-2.0 · rank 7462 · last release 2026-10-08 · [PyPI](https://pypi.org/project/pylibraft-cu12/) · [docs](https://docs.rapids.ai/api/raft/stable/)

<details><summary>README extract</summary>

Example:
```python
import cupy as cp

from cuvs.distance import pairwise_distance

n_samples = 5000
n_features = 50

in1 = cp.random.random_sample((n_samples, n_features), dtype=cp.float32)
in2 = cp.random.random_sample((n_samples, n_features), dtype=cp.float32)

output = pairwise_distance(in1, in2, metric="euclidean")
```

Sections: RAFT: Reusable Accelerated Functions and Tools, Useful Resources, What is RAFT?, #, Is RAFT right for me?, Getting started, RAPIDS Memory Manager (RMM), Multi-dimensional Arrays, C++ Example, Python Example, References

</details>

### parameter-decorators

Handy decorators for converting parameters

`pip install parameter-decorators` · installs (wheel) · licence: not stated · rank 7475 · last release 2023-01-31 · [PyPI](https://pypi.org/project/parameter-decorators/) · [source](https://github.com/matan1008/parameter-decorators)

<details><summary>README extract</summary>

Handy decorators for converting parameters

Example:
```python
from parameter_decorators import str_to_path

@str_to_path('input_file')
def get_parent(input_file):
    return input_file.parent

# Will print "/usr/bin"
print(get_parent('/usr/bin/python'))
```

Sections: parameter-decorators, Usage

</details>

### pyghmi

Python General Hardware Management Initiative (IPMI and others)

`pip install pyghmi` · installs (wheel) · licence: Apache Software License · rank 7523 · last release 2026-07-13 · [PyPI](https://pypi.org/project/pyghmi/)

<details><summary>README extract</summary>

This is a pure python implementation of IPMI protocol.

pyghmicons and pyghmiutil are example scripts to show how one may incorporate
this library into python code

</details>

