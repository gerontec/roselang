# Software Development / Libraries (part 5 of 5)

[Index](README.md) · 1884 packages in this topic, 1694 more listed under another topic, by downloads.

[part 1](software-development-libraries.md) · [part 2](software-development-libraries-2.md) · [part 3](software-development-libraries-3.md) · [part 4](software-development-libraries-4.md) · part 5

### python-amazon-paapi

Amazon Creators API wrapper for Python

`pip install python-amazon-paapi` · installs (wheel) · licence: MIT · rank 14160 · last release 2026-09-16 · [PyPI](https://pypi.org/project/python-amazon-paapi/) · [source](https://github.com/sergioteula/python-amazon-paapi)

<details><summary>README extract</summary>

A Python wrapper for the Amazon Creators API.

Features:
- 🎯 Simple object-oriented interface for easy integration
- ⚡ Async/await support for high-performance applications
- 🔍 Product search by keywords, categories, or browse nodes
- 📦 Product details via ASIN or Amazon URL ...

Example:
```python
from amazon_creatorsapi import AmazonCreatorsApi, Country

# Initialize with your Creators API credentials
api = AmazonCreatorsApi(
    credential_id="your_credential_id",
    credential_secret="your_credential_secret",
    version="2.2",
    tag="your-affiliate-tag",
    country=Country.US,
)

# Get product information by ASIN
...
```

...

</details>

### jsonsubschema

A tool to check whether a JSON schema is subset/subschema of another JSON schema

`pip install jsonsubschema` · installs (wheel) · licence: Apache-2.0 · rank 14178 · last release 2026-06-12 · [PyPI](https://pypi.org/project/jsonsubschema/) · [source](https://github.com/IBM/jsonsubschema)

<details><summary>README extract</summary>

jsonsubschema checks if one JSON schema is a subschema (subtype) of another.

For any two JSON schemas s1 and s2, s1 <: s2 (reads s1 is subschema/subtype of s2)
if every JSON document instance that validates against s1 also validates against s2. ...

Example:
```python
from jsonsubschema import isSubschema

def main():
    s1 = {'type': "integer"}
    s2 = {'type': ["integer", "string"]}

    print(f'LHS <: RHS {isSubschema(s1, s2)}')

if name == "main":
    main()
```

Sections: jsonsubschema #, I) Obtaining the tool, Requirements, II) Running subschema, A) CLI interface, B) python API

</details>

### tracebackturbo3

Patched version of traceback, also dumps local and global scope vars.

`pip install tracebackturbo3` · installs (wheel) · licence: Python Software Foundation License · rank 14186 · last release 2018-12-18 · [PyPI](https://pypi.org/project/tracebackturbo3/)

### mcp-use

Full Stack MCP framework for python, build MCP agents, clients, and servers.

`pip install mcp-use` · installs (wheel) · licence: MIT License · rank 14193 · last release 2026-09-10 · [PyPI](https://pypi.org/project/mcp-use/)

<details><summary>README extract</summary>

> 📦 Part of the mcp-use Monorepo - This is the Python implementation. Also available in TypeScript.

🌐 mcp-use for Python is the complete way to connect any LLM to any MCP server and build custom MCP agents with tool access. ...

Features:
Feature
 Description

 🔄 Ease of use
 Create your first MCP capable agent you need only 6 lines of code

 🤖 LLM Flexibility
 Works with any langchain supported LLM that supports tool calling (OpenAI, Anthropic, Groq, LLama etc.) ...

Example:
```python
async for chunk in agent.stream("Find the best restaurant in San Francisco"):
    print(chunk["messages"], end="", flush=True)
```

...

</details>

### Flask-Injector

Adds Injector, a Dependency Injection framework, support to Flask.

`pip install Flask-Injector` · installs (wheel) · licence: MIT License · rank 14194 · last release 2023-07-27 · [PyPI](https://pypi.org/project/Flask-Injector/)

<details><summary>README extract</summary>

Adds Injector support to Flask,
this way there's no need to use global Flask objects, which makes testing simpler.

Injector is a dependency-injection framework for Python, inspired by Guice. You
can find Injector on PyPI and Injector
documentation on Read the Docs.

`Flask-Injector` is compatible with CPython 3.7+. ...

Features:
Flask-Injector lets you inject dependencies into:

* views (functions and class-based)
* `before_request` handlers
* `after_request` handlers
* `teardown_request` handlers
* template context processors
* error handlers
* Jinja environment globals ...

Example:
```python
import sqlite3
from flask import Flask, Config
from flask.views import View
from flask_injector import FlaskInjector
from injector import inject

app = Flask(name)

...

</details>

### r2pipe

Pipe interface for radare2

`pip install r2pipe` · installs (wheel) · licence: MIT License · rank 14202 · last release 2026-10-19 · [PyPI](https://pypi.org/project/r2pipe/)

<details><summary>README extract</summary>

Interact with radare2 using the #!pipe command or in standalone scripts
that communicate with local or remote r2 via pipe, tcp or http.

Example:
```python
import r2pipe

r2 = r2pipe.open("/bin/ls")
r2.cmd('aa')
print(r2.cmd("afl"))
print(r2.cmdj("aflj"))            # evaluates JSONs and returns an object
print(r2.cmdj("ij")"core")  # shows file format
r2.quit()
```

Sections: r2pipe for Python, Usage example, Structured commands (r2pipe2), Asyncio

</details>

### simple-ascii-tables

Simple, minimal, dependency-free ASCII tables for Python.

`pip install simple-ascii-tables` · installs (wheel) · licence: GNU General Public License (GPL); MIT License · rank 14223 · last release 2025-01-23 · [PyPI](https://pypi.org/project/simple-ascii-tables/) · [source](https://github.com/g-battaglia/simple-ascii-tables)

_README extract left out: share-alike licence._

### dotted-notation

Dotted notation for safe nested data traversal with optional chaining, pattern matching, and transforms

`pip install dotted-notation` · installs (wheel) · licence: MIT · rank 14228 · last release 2026-11-04 · [PyPI](https://pypi.org/project/dotted-notation/) · [source](https://github.com/freywaid/dotted)

<details><summary>README extract</summary>

Sometimes you want to fetch data from a deeply nested data structure. Dotted notation
helps you do that.

Features:
Several Python libraries handle nested data access. Here's how dotted compares:

| Feature | dotted | glom | jmespath | pydash | ...

Sections: Dotted, Safe Traversal (Optional Chaining), Why Dotted?, Breaking Changes, v0.55.0, v0.53.0, v0.50.0, v0.49.0, v0.47.0, v0.44.0, v0.43.4, v0.40.0, v0.39.0, v0.38.0

</details>

### collate-dbt-artifacts-parser

A dbt artifacts parser in python

`pip install collate-dbt-artifacts-parser` · installs (wheel) · licence: Apache Software License · rank 14238 · last release 2025-11-24 · [PyPI](https://pypi.org/project/collate-dbt-artifacts-parser/)

<details><summary>README extract</summary>

This is a dbt artifacts parse in python.
It enables us to deal with `catalog.json`, `manifest.json`, `run-results.json` and `sources.json` as python objects.

This package is primarily designed for dbt-core, enabling seamless interaction with dbt artifacts as Python objects. ...

Example:
```python
import json

# parse any version of catalog.json
from collate_dbt_artifacts_parser.parser import parse_catalog

with open("path/to/catalog.json", "r") as fp:
    catalog_dict = json.load(fp)
    catalog_obj = parse_catalog(catalog=catalog_dict)

# parse catalog.json v1
from collate_dbt_artifacts_parser.parser import parse_catalog_v1

...
```

...

</details>

### carbone-sdk

Carbone API Python SDK to generate documents (PDF DOCX XLSX PPTX CSV XML HTML ODS ODT and more) from a JSON and a template.

`pip install carbone-sdk` · installs (wheel) · licence: Apache-2.0 · rank 14261 · last release 2025-05-04 · [PyPI](https://pypi.org/project/carbone-sdk/)

<details><summary>README extract</summary>

Generate Documents in Python: Seamless Integration with Carbone API.

Carbone is a document generator that utilizes Templates and JSON data to create a wide range of file formats, including PDF, DOCX, XLSX, ODT, PPTX, ODS, XML, CSV, and more. ...

Example:
```python
import carbone_sdk

# SDK constructor
# The access token can be passed as an argument to the constructor CarboneSDK
# Or by the environment variable "CARBONE_TOKEN", use the command "export CARBONE_TOKEN=secret-token"
csdk = carbone_sdk.CarboneSDK("secret-token")
# Set API version (default : 5)
csdk.set_api_version("5")
...
```

Sections: Carbone Python SDK, About Carbone, Usage, Documentation, Tests, Tests - Run with Makefile, Tests - Run manually

</details>

### xcffib

xcffib is the XCB binding for python

`pip install xcffib` · installs from source (sdist only) · licence: Apache Software License · rank 14265 · last release 2026-10-18 · [PyPI](https://pypi.org/project/xcffib/)

<details><summary>README extract</summary>

`xcffib` is the XCB binding for Python.

Sections: xcffib, Hacking, Hacking on new xcbproto versions, Hacking on new xcb-types versions

</details>

### aiobmsble

Asynchronous Python library to query battery management systems via Bluetooth Low Energy.

`pip install aiobmsble` · installs (wheel) · licence: Apache-2.0 · rank 14277 · last release 2026-11-06 · [PyPI](https://pypi.org/project/aiobmsble/) · [docs](https://patman15.github.io/aiobmsble/) · [source](https://github.com/patman15/aiobmsble.git)

<details><summary>README extract</summary>

[](
[](
[](LICENSE)

Requires Python 3 and uses asyncio and Bleak

This library is intended to query data from battery management systems that use Bluetooth LE. Stand-alone usage is possible in any Python environment (with necessary dependencies installed). ...

Features:
- Support for autodetecting compatible BLE BMSs
- 50+ different protocol variants
- Automatic detection of compatible BLE write mode
- Asynchronous operation using asyncio
- Any number of batteries in parallel ...

Example:
```python
"""Example of using the aiobmsble library to find a BLE device by name and print its sensor data.

Project: aiobmsble,
License: Apache-2.0,
"""

import asyncio
import logging
from typing import Final

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
...

</details>

### vendoring

A command line tool, to simplify vendoring pure Python dependencies.

`pip install vendoring` · installs (wheel) · licence: MIT License · rank 14304 · last release 2026-05-19 · [PyPI](https://pypi.org/project/vendoring/) · [source](https://github.com/pradyunsg/vendoring)

<details><summary>README extract</summary>

A command line tool, to simplify vendoring pure Python dependencies.

Features:
pip had a "home-grown" setup for vendoring dependencies. The `invoke` task grew in complexity to over 500 lines and, at some point, became extremely difficult to improve and maintain. ...

Sections: vendoring, Why does this exist?, Should I use it?

</details>

### python-dbusmock

Mock D-Bus objects

`pip install python-dbusmock` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 14332 · last release 2026-01-30 · [PyPI](https://pypi.org/project/python-dbusmock/)

_README extract left out: share-alike licence._

### SQLAlchemy-History

History tracking extension for SQLAlchemy.

`pip install SQLAlchemy-History` · installs (wheel) · licence: Apache-2.0 AND BSD-3-Clause · rank 14353 · last release 2026-10-23 · [PyPI](https://pypi.org/project/SQLAlchemy-History/) · [docs](https://corridor.github.io/sqlalchemy-history/) · [source](https://github.com/corridor/sqlalchemy-history)

<details><summary>README extract</summary>

Features:
- Supports SQLAlchemy 2+ and Python 3.10+
- Tracks history for inserts, deletes, and updates
- Does not store updates which don't change anything
- Supports Alembic migrations ...

Example:
```python
>>> from sqlalchemy_history import make_versioned
>>> make_versioned(user_cls=None)
>>> class Article(Base):
...    versioned = {}
...    tablename = 'article'
...    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
...    name = sa.Column(sa.Unicode(255))
...    content = sa.Column(sa.UnicodeText)
...
```

Sections: Features, Quickstart, Resources, More information, Comparison

</details>

### async-typer

Typer with first-class async support: unified sync/async commands, callbacks, and lifecycle event handlers.

`pip install async-typer` · installs (wheel) · licence: MIT License · rank 14365 · last release 2026-09-04 · [PyPI](https://pypi.org/project/async-typer/) · [source](https://github.com/byunjuneseok/async-typer)

<details><summary>README extract</summary>

Typer with first-class async support:
`async def` commands and callbacks work alongside regular sync ones via the
same `@app.command()` decorator — no second API to remember — plus lifecycle
event handlers for setting up and tearing down async resources.

Features:
- One decorator, sync or async — `@app.command()` and `@app.callback()`
 accept both regular and `async def` functions. The wrapper is transparent;
 Typer's `--help`, option parsing, and type conversion all work as normal. ...

Example:
```python
from async_typer import AsyncTyper

app = AsyncTyper()

@app.command()
def sync_hello(name: str = "world") -> None:
    print(f"hi {name}")

@app.command()
async def async_hello(name: str = "world") -> None:
    # await anything you need here
    print(f"hello {name}")

...

</details>

### django-db-geventpool

Add a DB connection pool using gevent to django

`pip install django-db-geventpool` · installs (wheel) · licence: Apache-2.0 · rank 14385 · last release 2025-02-23 · [PyPI](https://pypi.org/project/django-db-geventpool/)

<details><summary>README extract</summary>

Another DB pool using gevent for PostgreSQL DB.

psycopg3

Django, since 4.2, supports psycopg3. One of the advantages is that gevent is supported without needing extra patches, just install the package

psycopg2

If gevent is not installed, the pool will use eventlet as fallback. ...

</details>

### spaceforge

A Python framework for building Spacelift plugins

`pip install spaceforge` · installs (wheel) · licence: MIT · rank 14388 · last release 2026-10-21 · [PyPI](https://pypi.org/project/spaceforge/) · [docs](https://github.com/spacelift-io/plugins#readme) · [source](https://github.com/spacelift-io/plugins)

<details><summary>README extract</summary>

Spaceforge is a Python framework for building powerful Spacelift plugins using a declarative, hook-based approach. Define your plugin logic in Python, and Spaceforge automatically generates the plugin manifest for Spacelift.

Sections: Spaceforge - Build Spacelift Plugins in Python, Usage

</details>

### isbnlib

Extract, clean, transform, hyphenate and metadata for ISBNs (International Standard Book Number).

`pip install isbnlib` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 14398 · last release 2023-04-26 · [PyPI](https://pypi.org/project/isbnlib/)

_README extract left out: share-alike licence._

### django-sendfile2

Abstraction to offload file uploads to web-server (e.g. Apache with mod_xsendfile) once Django has checked permissions etc.

`pip install django-sendfile2` · installs (wheel) · licence: BSD License · rank 14417 · last release 2025-04-06 · [PyPI](https://pypi.org/project/django-sendfile2/)

<details><summary>README extract</summary>

This is a wrapper around web-server specific methods for sending files to web
clients. This is useful when Django needs to check permissions associated
files, but does not want to serve the actual bytes of the file itself. i.e. as
serving large files is not what Django is made for.

Note this should not be used for regular file serving (e.g. ...

Sections: Django Sendfile 2, Fork

</details>

### nucliadb-models

(no summary)

`pip install nucliadb-models` · installs (wheel) · licence: Apache-2.0 · rank 14422 · last release 2026-11-06 · [PyPI](https://pypi.org/project/nucliadb-models/) · [source](https://github.com/nuclia/nucliadb)

### nucliadb-utils

NucliaDB util library

`pip install nucliadb-utils` · installs (wheel) · licence: Apache-2.0 · rank 14426 · last release 2026-11-06 · [PyPI](https://pypi.org/project/nucliadb-utils/) · [source](https://github.com/nuclia/nucliadb)

### django-middleware-global-request

Django middleware that keep request instance for every thread.

`pip install django-middleware-global-request` · installs (wheel) · licence: MIT License · rank 14437 · last release 2025-10-22 · [PyPI](https://pypi.org/project/django-middleware-global-request/)

<details><summary>README extract</summary>

Django middleware that keep request instance for every thread.

Example:
```python
from django.db import models
from django.conf import settings
from django_middleware_global_request import get_request

class Book(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def str(self):
        return self.name

...
```

Sections: django-middleware-global-request, Note, Usage, Test Passed, v0.1.0, v0.1.1, v0.1.2, v0.2.0, v0.3.0, v0.3.1, v0.3.2, v0.3.3, v0.3.4, v0.3.5

</details>

### yolk3k

Command-line tool for querying PyPI and Python packages installed on your system.

`pip install yolk3k` · installs from source (sdist only) · licence: BSD License · rank 14445 · last release 2016-06-19 · [PyPI](https://pypi.org/project/yolk3k/)

<details><summary>README extract</summary>

Example:
```python
$ yolk --upgrade
    Upgrade all packages

$ yolk --upgrade --user
    Upgrade user packages

$ yolk -l
    List all installed Python packages

$ yolk -a
    List only the activated packages installed (Activated packages are
    normal packages on sys.path you can import)

$ yolk -n
...
```

Sections: yolk, Summary, Useful tips

</details>

### tika-client

A modern REST client for Apache Tika server

`pip install tika-client` · installs (wheel) · licence: MPL-2.0 · rank 14469 · last release 2026-10-28 · [PyPI](https://pypi.org/project/tika-client/) · [docs](https://github.com/stumpylog/tika-client#readme) · [source](https://github.com/stumpylog/tika-client)

<details><summary>README extract</summary>

A simple, fully-typed Python client for extracting text, HTML, and metadata from documents via the Apache Tika server REST API.

Features:
- Synchronous and asynchronous client support
- Pluggable HTTP backend (httpx, httpx2, niquests, or requests)
- `metadata.from_file()` and `rmeta.*.from_file()` stream files to the server via HTTP multipart/form-data (no full file reads into ...

Example:
```python
from pathlib import Path
from tika_client import TikaClient

with TikaClient(" as client:
    metadata = client.metadata.from_file(Path("sample.docx"))
    print(metadata.title)
    print(metadata.created)
```

...

</details>

### pyexcel-ods3

A wrapper library to read, manipulate and write data in ods format

`pip install pyexcel-ods3` · installs (wheel) · licence: BSD License · rank 14470 · last release 2022-01-30 · [PyPI](https://pypi.org/project/pyexcel-ods3/)

<details><summary>README extract</summary>

pyexcel-ods3 is a tiny wrapper library to read, manipulate and write data in ods
format. You are likely to use pyexcel together
with this library. pyexcel-ods is a sister
library that depends on GPL licensed odfpy.
pyexcel-odsr is the other sister library
that has no external dependency but do ods reading only

Example:
```python
>>> from pyexcel_ods3 import save_data
>>> data = OrderedDict() # from collections import OrderedDict
>>> data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
>>> data.update({"Sheet 2": [["row 1", "row 2", "row 3"]]})
>>> save_data("your_file.ods", data)
```

...

</details>

### zipencrypt

Encryption for zipfile

`pip install zipencrypt` · installs from source (sdist only) · licence: not stated · rank 14483 · last release 2018-11-08 · [PyPI](https://pypi.org/project/zipencrypt/)

<details><summary>README extract</summary>

zipencrypt is a Python module to provide *weak* password-based
encryption for zipfiles. It is meant as a drop-in replacement for
zipfile from the standard lib and provides the counterpart to the
decryption implemented there.

It is implemented in pure python and does not rely on any 3rd party libraries.

Compatible to python 2.7 and 3.4+

Example:
```python
from zipencrypt import ZipFile

with ZipFile("file.zip", mode="w") as f:
    f.writestr("file1.txt", "plaintext", pwd=b"password")
```

Sections: zipencrypt, The code, Do not use this!

</details>

### pytest-flask-sqlalchemy

A pytest plugin for preserving test isolation in Flask-SQlAlchemy using database transactions.

`pip install pytest-flask-sqlalchemy` · installs (wheel) · licence: MIT License · rank 14505 · last release 2022-04-30 · [PyPI](https://pypi.org/project/pytest-flask-sqlalchemy/)

<details><summary>README extract</summary>

A pytest plugin providing fixtures for running tests in
transactions using Flask-SQLAlchemy.

Example:
```python
def test_a_transaction(db_session):
   row = db_session.query(Table).get(1)
   row.name = 'testing'

   db_session.add(row)
   db_session.commit()

def test_transaction_doesnt_persist(db_session):
   row = db_session.query(Table).get(1)
   assert row.name != 'testing'
```

Sections: pytest-flask-sqlalchemy, Motivation, Quick examples, Usage, From PyPi, Configuration, Conftest setup, Test configuration, `mocked-engines`, `mocked-sessions`, `mocked-sessionmakers`, Writing transactional tests, Fixtures, `db_session`

</details>

### retrie

Efficient Trie-based regex unions for blacklist/whitelist filtering and one-pass mapping-based string replacing

`pip install retrie` · installs (wheel) · licence: MIT License · rank 14507 · last release 2024-02-22 · [PyPI](https://pypi.org/project/retrie/)

<details><summary>README extract</summary>

retrie offers fast methods to match and replace (sequences of) strings based on efficient Trie-based regex unions.

Instead of matching against a simple regex union, which becomes slow for large sets of words, a more efficient regex pattern can be compiled using a Trie structure: ...

Example:
```python
from retrie.trie import Trie

trie = Trie()

trie.add("abc", "foo", "abs")
assert trie.pattern() == "(?:ab[cs]|foo)"  # equivalent to but faster than "(?:abc|abs|foo)"

trie.add("absolute")
assert trie.pattern() == "(?:ab(?:c|s(?:olute)?)|foo)"

trie.add("abx")
assert trie.pattern() == "(?:ab(?:[cx]|s(?:olute)?)|foo)"

trie.add("abxy")
...
```

Sections: retrie, Trie, Usage, Blacklist, Whitelist, Replacer

</details>

### valohai-yaml

Valohai.yaml validation and parsing

`pip install valohai-yaml` · installs (wheel) · licence: MIT · rank 14525 · last release 2026-09-14 · [PyPI](https://pypi.org/project/valohai-yaml/)

<details><summary>README extract</summary>

Parses and validates `valohai.yaml` files.

Valohai YAML files are used to define how your machine learning project workloads and pipelines are ran on the Valohai ecosystem. Refer to Valohai Documentation to learn how to write the actual YAML files and for more in-depth usage examples.

Example:
```python
from valohai_yaml import validate, ValidationErrors

try:
    with open("path/to/valohai.yaml") as f:
        validate(f)
except ValidationErrors as errors:
    print("oh no!")
    for err in errors:
        print(err)
```

Sections: valohai-yaml, Usage, Validation, Parsing, Snapshots

</details>

### xlib

Python X Library

`pip install xlib` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 14528 · last release 2018-01-02 · [PyPI](https://pypi.org/project/xlib/)

_README extract left out: share-alike licence._

### xoscar

Python actor framework for heterogeneous computing.

`pip install xoscar` · installs (wheel) · licence: Apache License 2.0 · rank 14529 · last release 2026-10-27 · [PyPI](https://pypi.org/project/xoscar/)

<details><summary>README extract</summary>

Writing parallel and distributed programs is often challenging and requires a lot of time to deal with concurrency
issues. Actor model provides a high-level, scalable and robust abstraction for building distributed applications.
It provides several benefits:
- Scalability: Actors easily scale across nodes. ...

Features:
Xoscar implements the actor model in Python and provides user-friendly APIs that offer significant benefits for building
applications on heterogeneous hardware: ...

Example:
```python
import xoscar as xo

# stateful actor, for stateless actor, inherit from xo.StatelessActor
class MyActor(xo.Actor):
    def init(self, *args, **kwargs):
        pass

    async def post_create(self):
        # called after created
        pass

    async def pre_destroy(self):
...

</details>

### PySquashfsImage

Squashfs image parser

`pip install PySquashfsImage` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 14548 · last release 2023-07-02 · [PyPI](https://pypi.org/project/PySquashfsImage/)

_README extract left out: share-alike licence._

### pycsvschema

PyCSVSchema is an implementation of CSV Schema in Python.

`pip install pycsvschema` · installs (wheel) · licence: MIT License · rank 14550 · last release 2019-10-09 · [PyPI](https://pypi.org/project/pycsvschema/)

<details><summary>README extract</summary>

PyPI Page:

Github Page:

PyCSVSchema is an implementation of CSV Schema in Python.

This project is under heavy development.

Example:
```python
>>> from pycsvschema.checker import Validator
>>>
>>> # demo.csv:
... # id,name,value
... # 1,Ann,"5"
... # 2,Ben,"10"
... # 3,Tom,"14"
...
>>>
>>> schema = {
...     'fields': [
...         {
...             'name': 'value',
...             'type': 'number',
...             'multipleOf': 5
...         }
...     ]
... }
>>>
...
```

Sections: PyCSVSchema, Introduction

</details>

### prompt

Library for prompting input on the command line.

`pip install prompt` · installs (wheel) · licence: MIT License · rank 14551 · last release 2017-06-05 · [PyPI](https://pypi.org/project/prompt/)

<details><summary>README extract</summary>

| Prompt and verify user input on the command line.
| Python 3.3+ and Wheels are supported.

The project was initiated by Stefan Fischer.

- Documentation is
 available on PythonHosted.
- Questions can be asked via e-mail.
- Changes
 between releases are documented.
- Source code is
 tracked on GitHub.
- Bugs can be
 reported on the issue tracker.

Example:
```python
import prompt

email = prompt.email()

# modify default prompt
integer = prompt.integer(prompt="Please enter a number: ")

# allow empty response
real = prompt.real(empty=True)

# require a two digit number using a regular expression
regex = prompt.regex("^\d\d$")
```

Sections: Python Prompt Package, Use, Added, Changed, Deprecated, Fixed, Removed, 0.4.1 - 2017-06-05, 0.4.0 - 2016-03-22, 0.3.2 - 2016-03-22, 0.3.1 - 2015-10-10

</details>

### pytest-django-queries

Generate performance reports from your django database performance tests.

`pip install pytest-django-queries` · installs (wheel) · licence: MIT · rank 14553 · last release 2026-03-01 · [PyPI](https://pypi.org/project/pytest-django-queries/) · [docs](https://pytest-django-queries.readthedocs.io/) · [source](https://github.com/NyanKiyoshi/pytest-django-queries/)

<details><summary>README extract</summary>

Generate performance reports from your django database performance tests
 (inspired by coverage.py).

Example:
```python
import pytest

@pytest.mark.count_queries
def test_query_performances():
    Model.objects.all()

# Or...
def test_another_query_performances(count_queries):
    Model.objects.all()
```

Sections: pytest-django-queries, Usage, Recommendation when Using Fixtures, Using pytest-django alongside of pytest-django-queries, Integrating with GitHub, Visualising Results, Exporting the Results (HTML), Comparing Results

</details>

### python-mpd2

A Python MPD client library

`pip install python-mpd2` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 14563 · last release 2024-01-13 · [PyPI](https://pypi.org/project/python-mpd2/)

_README extract left out: share-alike licence._

### infi.exceptools

a mechanism for chaining exceptions, compatible with Python 2.x

`pip install infi.exceptools` · installs from source (sdist only) · licence: BSD License · rank 14585 · last release 2019-02-18 · [PyPI](https://pypi.org/project/infi.exceptools/)

<details><summary>README extract</summary>

Python 3.x has such mechanism, which was not ported to Python 2.x, this is an alternative

</details>

### infi.instruct

declarative structure marshalling

`pip install infi.instruct` · installs from source (sdist only) · licence: BSD License · rank 14594 · last release 2018-12-20 · [PyPI](https://pypi.org/project/infi.instruct/)

### oci-openai

OCI authentication and authorization utilities for OpenAI python SDK

`pip install oci-openai` · installs (wheel) · licence: UPL-1.0 · rank 14595 · last release 2026-02-03 · [PyPI](https://pypi.org/project/oci-openai/) · [docs](https://github.com/oracle-samples/oci-openai#readme) · [source](https://github.com/oracle-samples/oci-openai)

<details><summary>README extract</summary>

The OCI OpenAI Python library provides secure and convenient access to the OpenAI-compatible REST API hosted by OCI Generative AI Service and OCI Data Science Model Deployment Service.

Example:
```python
from openai import OpenAI
import os

API_KEY=os.getenv("OPENAI_API_KEY")

print(API_KEY)

client = OpenAI(
    api_key=API_KEY,
    base_url="
)

# Responses API
response = client.responses.create(
    model="openai.gpt-oss-120b",
    # model="xai.grok-3",
    # meta models are not supported with the Responses API
...
```

Sections: oci-openai, Before you start, Examples, OCI Generative AI, Using the OCI OpenAI Synchronous Client, Using the OCI OpenAI Asynchronous Client, Using the Native OpenAI Client, Using with langchain-openai, OCI Data Science Model Deployment, Signers

</details>

### vyper-config

Python configuration with (more) fangs

`pip install vyper-config` · installs (wheel) · licence: MIT License · rank 14597 · last release 2023-10-04 · [PyPI](https://pypi.org/project/vyper-config/)

<details><summary>README extract</summary>

Python configuration with (more) fangs! Python port of the very awesome Viper for Go.

The package changed name on pypi from `vyper` to `vyper-config` on August 20th 2018.
The `vyper` name is now used by the following project.
The `vyper-config` package is available on PyPI. ...

Features:
When building a modern application, you don’t want to worry about
configuration file formats; you want to focus on building awesome software.
Vyper is here to help with that.

Vyper does the following for you:

1. ...

Example:
```python
v.set_env_prefix('spf')  # will be uppercased automatically
v.bind_env('id')

os.environ['SPF_ID'] = '13'  # typically done outside of the app

id = v.get('id')  # 13
```

...

</details>

### mementos

Memoizing metaclass. Drop-dead simple way to create cached objects

`pip install mementos` · installs (wheel) · licence: Apache Software License · rank 14598 · last release 2018-06-03 · [PyPI](https://pypi.org/project/mementos/)

<details><summary>README extract</summary>

travisciversionversionsimplswheelcoveragebr-coverage|

A quick way to make Python classes automatically memoize (a.k.a. cache) their
instances based on the arguments with which they are instantiated (i.e. args to
their `init`). ...

Example:
```python
from mementos import mementos

class Thing(mementos):

    def init(self, name):
        self.name = name

    ...
```

Sections: Usage, Under the Hood, Python 2 vs. Python 3, Careful with Call Signatures, Partial Signatures, Visiting the Factory, Notes

</details>

### street-address

Street address parser and formatter

`pip install street-address` · installs from source (sdist only) · licence: MIT License · rank 14601 · last release 2018-10-06 · [PyPI](https://pypi.org/project/street-address/)

<details><summary>README extract</summary>

Street address parser and formatter

Sections: street-address, Usage

</details>

### django-image-cropping

A reusable app for cropping images easily and non-destructively in Django

`pip install django-image-cropping` · installs (wheel) · licence: BSD License · rank 14611 · last release 2022-02-08 · [PyPI](https://pypi.org/project/django-image-cropping/)

<details><summary>README extract</summary>

django-image-cropping is an app for cropping uploaded images via Django's admin backend using Jcrop.

Screenshot:

django-image-cropping is perfect when you need images with a specific size for your templates but want your
users or editors to upload images of any dimension. ...

Example:
```python
from django.db import models
from image_cropping import ImageRatioField

class MyModel(models.Model):
    image = models.ImageField(blank=True, upload_to='uploaded_images')
    # size is "width x height"
    cropping = ImageRatioField('image', '430x360')
```

Sections: django-image-cropping, Configuration, Admin Integration, Backends, Frontend, easy_thumbnails, ModelForm, Multiple formats, Foreign Keys, Free cropping, Disabling cropping, Settings, Thumbnail size, Size warning

</details>

### fusionauth-client

A client library for FusionAuth

`pip install fusionauth-client` · installs (wheel) · licence: Apache Software License · rank 14614 · last release 2026-10-28 · [PyPI](https://pypi.org/project/fusionauth-client/)

<details><summary>README extract</summary>

<!--
tag::forDocSite[]

If you're integrating FusionAuth with a Python 3 application, this library will speed up your development time. Please also make sure to check our SDK Usage Suggestions page.

For additional information and documentation on FusionAuth refer to

Example:
```python
from fusionauth.fusionauth_client import FusionAuthClient
```

Sections: FusionAuth Python Client, Intro, Examples, Set Up, Create the Client, Error Handling, Create an Application, Adding Roles to an Existing Application, Retrieve Application Details, Delete an Application, Lock a User, Registering a User, Upgrade Policy

</details>

### markdown-it-pyrs

A Python interface for markdown-it.rs, using Rust for blazingly fast Markdown parsing ⚡️

`pip install markdown-it-pyrs` · installs from source (sdist only) · licence: Apache Software License · rank 14627 · last release 2024-10-22 · [PyPI](https://pypi.org/project/markdown-it-pyrs/)

<details><summary>README extract</summary>

[][pypi-link]

Currently in Beta, feedback welcome!

A Python interface for markdown-it.rs (and plugins), using Rust for blazingly fast Markdown parsing ⚡️

The goal of this project is to provide a fast, safe, extensible, and easy-to-use Markdown parser for Python. ...

Example:
```python
from markdown_it_pyrs import MarkdownIt

md = MarkdownIt("commonmark").enable("table")
md.render("# Hello, world!")
# '
# Hello, world!
\n'
```

Sections: markdown-it-pyrs, Usage, Command Line Interface, Initial Configuration, Plugins, TODO

</details>

### open-mock-file

Smart object for mocking open file calls, depends on file path

`pip install open-mock-file` · installs (wheel) · licence: MIT License · rank 14631 · last release 2018-01-28 · [PyPI](https://pypi.org/project/open-mock-file/)

<details><summary>README extract</summary>

This library contains object, which can be used during mocking files in
tests. Features:

- You can register different actions (provide different objects) for
 different paths
- You can add text, which will be returned on read
- You can select behavior for paths, which are not registered.
 Supported behaviors: ...

Example:
```python
from unittest.mock import patch
from open_file_mock import MockOpen

class FileObject:
    def init(self, data):
        self.data = data

    def read(self, *args, **kwargs):
        return self.data

    def write(self, data, *args, **kwargs):
        self.data = data

    def enter(self):
        return self

...
```

Sections: Open File Mock, Description, Usage, Examples, Object methods

</details>

### flake8-django

Plugin to catch bad style specific to Django Projects.

`pip install flake8-django` · installs from source (sdist only) · licence: GNU General Public License v3 or later (GPLv3+) · rank 14639 · last release 2023-07-31 · [PyPI](https://pypi.org/project/flake8-django/) · [source](https://github.com/rocioar/flake8-django)

_README extract left out: share-alike licence._

### cappa

Declarative CLI argument parser.

`pip install cappa` · installs (wheel) · licence: not stated · rank 14655 · last release 2026-10-09 · [PyPI](https://pypi.org/project/cappa/) · [source](https://github.com/dancardin/cappa)

<details><summary>README extract</summary>

- Full Documentation
- Comparison vs click/typer/argparse/etc
- Annotations Inference Docs
- "invoke" API Docs
- Class Compatibility (dataclasses/pydantic/etc)

Cappa is a declarative command line parsing library, which uses runtime type inspection
to infer (default) CLI argument behavior, and provide automatic help text
generation and dynamic ...

Example:
```python
from future import annotations
from dataclasses import dataclass, field
from typing import Literal
from typing_extensions import Annotated
import cappa

@dataclass
class Example:
    # Normal types are by default inferred as positional arguments
    positional: str = "optional"

    # Except boolean types, which are inferred as flags
...
```

...

</details>

### bleak-esphome

Bleak backend of ESPHome

`pip install bleak-esphome` · installs (wheel) · licence: MIT License · rank 14657 · last release 2026-08-30 · [PyPI](https://pypi.org/project/bleak-esphome/) · [docs](https://bleak-esphome.readthedocs.io) · [source](https://github.com/bluetooth-devices/bleak-esphome)

<details><summary>README extract</summary>

Documentation:

Source Code:

A Bleak backend that proxies Bluetooth Low Energy
through an ESP32 running ESPHome with the
Bluetooth Proxy component.
It lets any Python application — Home Assistant, an add-on, or a stand-alone
script — discover and connect to BLE peripherals using a remote ESP32 as the
adapter. ...

</details>

### increase

The official Python library for the increase API

`pip install increase` · installs (wheel) · licence: Apache Software License · rank 14661 · last release 2026-11-04 · [PyPI](https://pypi.org/project/increase/) · [source](https://github.com/Increase/increase-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Increase Python library provides convenient access to the Increase REST API from any Python 3.10+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx. ...

Example:
```python
import os
from increase import Increase

client = Increase(
    api_key=os.environ.get("INCREASE_API_KEY"),  # This is the default and can be omitted
    # defaults to "production".
    environment="sandbox",
)

account = client.accounts.create(
    name="New Account!",
    entity_id="entity_n8y8tnk2p9339ti393yi",
...
```

...

</details>

### mouse

Hook and simulate mouse events on Windows and Linux

`pip install mouse` · installs (wheel) · licence: MIT License · rank 14667 · last release 2020-01-01 · [PyPI](https://pypi.org/project/mouse/)

<details><summary>README extract</summary>

Take full control of your mouse with this small Python library. Hook global events, register hotkeys, simulate mouse movement and clicks, and much more.

_Huge thanks to Kirill Pavlov for donating the package name. If you are looking for the Cheddargetter.com client implementation, `pip install mouse==0.5.0`._

Features:
- Global event hook on all mice devices (captures events regardless of focus).
- Listen and sends mouse events.
- Works with Windows and Linux (requires sudo).
- Pure Python, no C modules to be compiled.
- Zero dependencies. ...

Sections: mouse, Features, Usage, Known limitations

</details>

### idpyoidc

Python implementation of everything OAuth2 and OpenID Connect

`pip install idpyoidc` · installs (wheel) · licence: Apache Software License · rank 14676 · last release 2024-09-15 · [PyPI](https://pypi.org/project/idpyoidc/)

<details><summary>README extract</summary>

This project is a Python implementation of everything OpenID Connect and OAuth2.

idpyoidc is the 2nd layer in the JwtConnect stack (cryptojwt, idpyoidc).
As OIDC OP Idpy implements the following standards: ...

Sections: idpyoidc, Introduction, Usage, Certifications

</details>

### trame-dataclass

Dataclass for trame UI binding

`pip install trame-dataclass` · installs (wheel) · licence: Apache Software License · rank 14689 · last release 2026-10-16 · [PyPI](https://pypi.org/project/trame-dataclass/)

<details><summary>README extract</summary>

`trame-dataclass` lets you define typed Python classes whose fields sync
automatically between the server and the browser. Each field is declared
with a descriptor (`Sync`, `ServerOnly`, or `ClientOnly`) that controls
the sync direction. ...

Example:
```python
from typing import Any

from trame.app import TrameApp
from trame.app.dataclass import ClientOnly, ServerOnly, StateDataModel, Sync, watch
from trame.ui.html import DivLayout
from trame.widgets import dataclass, html

class SimpleStructure(StateDataModel):
    name = Sync(str, "John Doe")        # server <=> client
...
```

Sections: trame-dataclass, Field descriptors, Reactivity, Exposing instances to the UI, Composed dataclasses, Deep reactivity, Embedded GUI, Usage example, More examples, Commit message convention

</details>

### strawberry-sqlalchemy-mapper

A library for autogenerating Strawberry GraphQL types from SQLAlchemy models.

`pip install strawberry-sqlalchemy-mapper` · installs (wheel) · licence: MIT License · rank 14692 · last release 2026-08-31 · [PyPI](https://pypi.org/project/strawberry-sqlalchemy-mapper/) · [docs](https://strawberry.rocks/) · [source](https://github.com/strawberry-graphql/strawberry-sqlalchemy)

<details><summary>README extract</summary>

[][pypi-url]

[][downloads-url]
[][coverage-url]
[][ci-url]

[][discord-url]

The simplest way to implement autogenerated Strawberry types for columns and relationships in SQLAlchemy models. ...

Example:
```python
# models.py
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Employee(Base):
    tablename = "employee"
    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
...
```

Sections: Strawberry SQLAlchemy Mapper, Getting Started, Basic Usage, Type Inheritance, Relay connections, BigInt Columns, Limitations, Association Proxies, Polymorphic Hierarchies, Prerequisites, Test

</details>

### mdformat_simple_breaks

An mdformat plugin for simple line breaks like in GitHub Flavored Markdown.

`pip install mdformat_simple_breaks` · installs (wheel) · licence: MIT License · rank 14731 · last release 2025-10-28 · [PyPI](https://pypi.org/project/mdformat_simple_breaks/)

<details><summary>README extract</summary>

[][ci-link]
[][cov-link]
[][pypi-link]

An mdformat plugin to render *thematic breaks* using three dashes

instead of 70 underscores

Sections: mdformat-simple-breaks, Usage as a pre-commit hook, Plugin rationale

</details>

### opensandbox-code-interpreter

OpenSandbox Code Interpreter Python SDK - Advanced code execution with persistent contexts

`pip install opensandbox-code-interpreter` · installs (wheel) · licence: Apache Software License · rank 14734 · last release 2026-10-27 · [PyPI](https://pypi.org/project/opensandbox-code-interpreter/) · [docs](https://open-sandbox.ai) · [source](https://github.com/opensandbox-group/OpenSandbox)

<details><summary>README extract</summary>

A Python SDK for executing code in secure, isolated sandboxes. It provides a high-level API for running Python, Java, Go, TypeScript, and other languages safely, with support for code execution contexts.

This SDK requires a Docker image containing the Code Interpreter runtime environment. ...

Example:
```python
import asyncio
from datetime import timedelta

from code_interpreter import CodeInterpreter, SupportedLanguage
from opensandbox import Sandbox
from opensandbox.config import ConnectionConfig

async def main() -> None:
    # 1. Configure connection
    config = ConnectionConfig(
        domain="api.opensandbox.io",
        api_key="your-api-key",
...
```

...

</details>

### django-ebhealthcheck

Django app to add an instance's public IP to ALLOWED_HOSTS for Elastic Beanstalk's health check system

`pip install django-ebhealthcheck` · installs (wheel) · licence: BSD License · rank 14738 · last release 2022-08-22 · [PyPI](https://pypi.org/project/django-ebhealthcheck/)

<details><summary>README extract</summary>

By default, Elastic Beanstalk's health check system uses the public IP of each
load balanced instance as the request's host header when making a request.
Unless added to `ALLOWED_HOSTS`, this causes Django to return a `400 Bad
Request` and a failed health check. ...

</details>

### ymodem

Ymodem Python implementation

`pip install ymodem` · installs (wheel) · licence: MIT License · rank 14765 · last release 2025-12-18 · [PyPI](https://pypi.org/project/ymodem/) · [source](https://github.com/alexwoo1900/ymodem)

<details><summary>README extract</summary>

The YMODEM project is based on XMODEM implementation written by tehmaze. It is also compatible with XMODEM mode.

README: ENGLISH | 简体中文

- Installation
- Usage
 - CLI TOOL
 - Sending a batch of files
 - Receive a file
 - Source Code
 - API
 - Create MODEM Object
 - Send files
 - Receive files
- Debug
- Changelog
- License

Example:
```python
from ymodem.Socket import ModemSocket

# define read
def read(size, timeout = 3):
    # implementation

# define write
def write(data, timeout = 3):
    # implementation

# create socket
cli = ModemSocket(read, write)

# send multi files
cli.send([file_path1, file_path2, file_path3 ...])

# receive multi files
cli.recv(folder_path)
```

...

</details>

### fillmore

Sentry event scrubber and utilities library

`pip install fillmore` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 14768 · last release 2025-10-09 · [PyPI](https://pypi.org/project/fillmore/) · [docs](https://fillmore.readthedocs.io/) · [source](https://github.com/mozilla-services/fillmore/)

<details><summary>README extract</summary>

Status 2025-10-09: This project is deprecated.

The Python sentry-sdk has a before_send hook that lets you scrub Sentry events
before they're sent. Fillmore makes it easier to set up a before_send scrubber
and test it.

:Code:
:Issues:
:License: MPL v2
:Documentation:

Goals of Fillmore:

1. ...

Features:
Other libraries:

* Have an awkward API that is hard to reason about.

 I'm not scrubbing Sentry events for fun. I need to be able to write scrubbing
 configuration that is exceptionally clear about what it is and isn't doing. ...

Example:
```python
# examples/myapp/myapp/app.py
import logging
import logging.config

from fillmore.libsentry import set_up_sentry
from fillmore.scrubber import Scrubber, Rule, build_scrub_query_string

# Set up logging to capture fillmore error messages
...

</details>

### mdformat_deflist

An mdformat plugin for markdown-it-deflist.

`pip install mdformat_deflist` · installs (wheel) · licence: MIT License · rank 14770 · last release 2025-10-19 · [PyPI](https://pypi.org/project/mdformat_deflist/)

<details><summary>README extract</summary>

[][ci-link]
[][cov-link]
[][pypi-link]

An mdformat plugin for markdown-it-deflist.

Sections: mdformat-deflist, Publish to PyPi

</details>

### python-roborock

A package to control Roborock vacuums.

`pip install python-roborock` · installs (wheel) · licence: Apache-2.0 · rank 14772 · last release 2026-11-08 · [PyPI](https://pypi.org/project/python-roborock/) · [docs](https://python-roborock.readthedocs.io/) · [source](https://github.com/python-roborock/python-roborock)

<details><summary>README extract</summary>

Roborock library for online and offline control of your vacuums.

Example:
```python
import asyncio

from roborock.web_api import RoborockApiClient
from roborock.devices.device_manager import create_device_manager, UserParams

async def main():
    email_address = "youremailhere@example.com"
    web_api = RoborockApiClient(username=email_address)
    # Send a login code to the above email address
    await web_api.request_code()
...
```

Sections: Roborock, Example Usage, Functionality

</details>

### pypugjs

PugJS syntax template adapter for Django, Jinja2, Mako and Tornado templates

`pip install pypugjs` · installs (wheel) · licence: MIT License · rank 14774 · last release 2026-07-16 · [PyPI](https://pypi.org/project/pypugjs/)

<details><summary>README extract</summary>

PyPugJS is a fork of PyJade
with the name Jade changed to PugJS.

Additional disclaimer: Since the original pypugjs died i took the liberty to keep it alive, because
since starting to work with the jade compiler for node I hate writing HTML and want to continue using it in my Django projects. ...

Example:
```python
import pypugjs

@pypugjs.register_filter('capitalize')
def capitalize(text, ast):
  return text.capitalize()
```

Sections: PyPugJS, UTILITIES, Syntax, Example, Register filters, Notable Features, TODOs and BUGS, 5.8.1, 5.8.0, 5.7.2, 5.7.1, 5.7.0, 5.6.1, 5.6.0

</details>

### django-registration-redux

An extensible user-registration application for Django

`pip install django-registration-redux` · installs (wheel) · licence: BSD License · rank 14775 · last release 2023-10-27 · [PyPI](https://pypi.org/project/django-registration-redux/)

<details><summary>README extract</summary>

:Description: Django-registration provides user registration functionality for Django websites.
:maintainers: Macropin, DiCato, and joshblum
:contributors: list of contributors

If you have issues with the "django-registration-redux" package then please raise them here. ...

</details>

### django-admin-action-forms

Extension for the Django admin panel that allows passing additional parameters to actions by creating intermediate pages with forms.

`pip install django-admin-action-forms` · installs (wheel) · licence: not stated · rank 14804 · last release 2026-08-06 · [PyPI](https://pypi.org/project/django-admin-action-forms/) · [source](https://github.com/michalpokusa/django-admin-action-forms)

<details><summary>README extract</summary>

Extension for the Django admin panel that allows passing additional parameters to actions by creating intermediate pages with forms.

- 🚀 Overview
- 🎉 Features
- 🔌 Installation
- ✏️ Examples
 - Simple confirm form
 - Action with parameters
 - Customizing action form layout
 - Inlines
 - Testing action forms
- 📄 Reference ...

Example:
```python
from django.contrib import admin
from django.contrib.auth.models import User

from django_admin_action_forms import AdminActionFormsMixin, AdminActionForm, action_with_form

class ResetUsersPasswordActionForm(AdminActionForm):
    # No fields needed

    class Meta:
        list_objects = True
...
```

...

</details>

### django-syzygy

Deployment aware tooling for Django migrations.

`pip install django-syzygy` · installs (wheel) · licence: MIT License · rank 14822 · last release 2026-03-13 · [PyPI](https://pypi.org/project/django-syzygy/)

<details><summary>README extract</summary>

Django application providing database migration tooling to automate their deployment.

Inspired by a 2015 post from Ludwig Hähne and experience dealing with migration at Zapier.

Currently only tested against PostgreSQL, SQLite, and MySQL. ...

Example:
```python
class Migration(migrations.Migration):
    operations = [
        AddField('model', 'field', models.IntegerField(null=True))
    ]
```

Sections: django-syzygy, Usage, Concept, What it does and doesn't do, It does, It doesn't, Specialized operations, Field addition, Field removal, Checks, Third-party migrations, Reverts, CI Integration, Migration quorum

</details>

### actions-python-core

Actions core lib

`pip install actions-python-core` · installs (wheel) · licence: MIT License · rank 14823 · last release 2023-10-08 · [PyPI](https://pypi.org/project/actions-python-core/)

<details><summary>README extract</summary>

> Core functions for setting results, logging, registering secrets and exporting variables across actions

Example:
```python
from actions import core
```

Sections: `actions-python-core`, Usage, Import the package, Inputs/Outputs, TBD

</details>

### tini

Read simple .ini/configuration files.

`pip install tini` · installs (wheel) · licence: MIT License · rank 14824 · last release 2024-12-04 · [PyPI](https://pypi.org/project/tini/)

<details><summary>README extract</summary>

A simple module for loading `.ini`-style configuration files.

Based on ConfigParser and works in Python 2 and Python 3.

Or, with `tox` (test with multiple Python versions):

Example:
```python
import os
import sys

from tini import Tini

filenames = [
    './foobar.ini',
    os.path.join(os.path.expanduser('~'), '.foobar.ini'),
    os.path.join(os.path.expanduser('~'), '.config', '.foobar.ini'),
]

defaults = {
    'foobar': {
        'baz': 'a string',
        'buzz': True,
        'bizz': 123,
    }
}

...
```

Sections: tini, Running tests, Example, settings.py, foobar.ini, test.py

</details>

### pytest-splinter

Splinter plugin for pytest testing framework

`pip install pytest-splinter` · installs (wheel) · licence: MIT License · rank 14827 · last release 2022-09-09 · [PyPI](https://pypi.org/project/pytest-splinter/) · [docs](https://github.com/pytest-dev/pytest-splinter/blob/master/README.rst) · [source](https://github.com/pytest-dev/pytest-splinter)

<details><summary>README extract</summary>

Features:
The plugin provides a set of fixtures to use splinter
for browser testing with pytest

Example:
```python
def test_some_browser_stuff(browser):
    """Test using real browser."""
    url = "
    browser.visit(url)
    browser.fill('q', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    button = browser.find_by_name('btnK')
    # Interact with elements
    button.click()
...
```

Sections: Splinter plugin for the pytest runner, Features, Fixtures, Command-line options, Browser fixture, Automatic screenshots on test failure, Example, Contact, 3.3.2, 3.3.1, 3.3.0, 3.2.0, 3.1.0, 3.0.0

</details>

### mozInstall

package for installing and uninstalling Mozilla applications

`pip install mozInstall` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 14829 · last release 2023-07-28 · [PyPI](https://pypi.org/project/mozInstall/)

### matrx-connect

FastAPI middleware, auth, streaming infrastructure, and context management for the Matrx ecosystem

`pip install matrx-connect` · installs (wheel) · licence: MIT License · rank 14837 · last release 2026-10-30 · [PyPI](https://pypi.org/project/matrx-connect/) · [source](https://github.com/AI-Matrix-Engine/aidream-current)

<details><summary>README extract</summary>

FastAPI connectivity layer for the Matrx ecosystem: auth middleware, streaming-response infrastructure, request-scoped `AppContext`, and the `Emitter` protocol. Despite the name, "connect" is about connecting a FastAPI app to the Matrx streaming + auth contract — not database connectivity.

Example:
```python
from fastapi import APIRouter, Depends
from matrx_connect import AppContext, context_dep
from matrx_connect.streaming import create_streaming_response

router = APIRouter()

@router.post("/topics/{topic_id}/search")
async def trigger_search(topic_id: str, ctx: AppContext = Depends(context_dep)):
    return create_streaming_response(
...
```

Sections: matrx-connect, What's in the box, The streaming endpoint pattern, Wiring the auth middleware, Standalone-friendliness

</details>

### net-mesh

High-performance, schema-agnostic event bus for AI runtime workloads

`pip install net-mesh` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 14844 · last release 2026-10-31 · [PyPI](https://pypi.org/project/net-mesh/) · [source](https://github.com/ai-2070/net)

<details><summary>README extract</summary>

The PyO3 extension for the Net mesh — a latency-first encrypted mesh where
services and agents announce capabilities, discover each other, and invoke work
over typed RPC.

**Most people want `net-mesh-sdk`
instead.** That's the Pythonic wrapper — context managers, generators, typed
channels, dataclass and Pydantic support — and it depends on this ...

Example:
```python
from net import Net

with Net(num_shards=4) as bus:
    bus.ingest_raw('{"sensor": "lidar", "range_m": 12.5}')
    bus.ingest({"sensor": "radar", "range_m": 45.0})

    # Cursor-paginated. None starts from the earliest buffered event.
    resp = bus.poll(100)
    for event in resp.events:
        print("event", event)
...
```

...

</details>

### aiousbwatcher

Watch for USB devices to be plugged and unplugged

`pip install aiousbwatcher` · installs (wheel) · licence: MIT · rank 14846 · last release 2026-04-21 · [PyPI](https://pypi.org/project/aiousbwatcher/) · [docs](https://aiousbwatcher.readthedocs.io) · [source](https://github.com/bluetooth-devices/aiousbwatcher)

<details><summary>README extract</summary>

Documentation:

Source Code:

Watch for USB devices to be plugged and unplugged

</details>

### asyncgui

A minimalistic async library that focuses on fast responsiveness

`pip install asyncgui` · installs (wheel) · licence: MIT · rank 14848 · last release 2026-10-18 · [PyPI](https://pypi.org/project/asyncgui/) · [docs](https://asyncgui.github.io/asyncgui/) · [source](https://github.com/asyncgui/asyncgui)

<details><summary>README extract</summary>

...is a minimalistic async library that:

- does not provide features involving system calls, such as I/O.
- has no external dependencies.
- does not own a main loop, but is designed to integrate with an existing one.
- avoids global state.
- focuses on fast responsiveness, allowing immediate task start and resumption. ...

Sections: AsyncGui, Tested on, Dependants

</details>

### Spark

An easy to use actor model framework in Python

`pip install Spark` · installs (wheel) · licence: MIT License · rank 14850 · last release 2026-05-16 · [PyPI](https://pypi.org/project/Spark/) · [source](https://github.com/wensheng/spark)

<details><summary>README extract</summary>

Spark is an async-first actor framework for Python. The core API is small:
start a `Syndicate`, create actors, and send messages with `tell(message,
target)` or `ask(message, target)`.

Workflow routing lives in the explicit `spark.workflow` package. ...

Example:
```python
from spark import Actor, Syndicate
from spark.core.message import Message

class Echo(Actor):
    async def process(self, message: Message) -> str:
        return f"echo:{message.content}"

async with Syndicate("app") as system:
    echo = await system.create_actor(Echo)
    print(await system.ask("hello", echo, timeout=1.0))
```

Sections: Spark, Quick Start, Core Capabilities, Workflow Layer, Networking, Examples, Documentation

</details>

### pytest-rabbitmq

RabbitMQ process and client fixtures for pytest

`pip install pytest-rabbitmq` · installs (wheel) · licence: LGPL-3.0-or-later · rank 14851 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pytest-rabbitmq/) · [source](https://github.com/dbfixtures/pytest-rabbitmq)

_README extract left out: share-alike licence._

### qpd

Query Pandas Using SQL

`pip install qpd` · installs (wheel) · licence: Apache Software License · rank 14861 · last release 2023-07-12 · [PyPI](https://pypi.org/project/qpd/)

<details><summary>README extract</summary>

QPD let you run the same SQL (`SELECT` for now) statements on different computing frameworks with pandas-like interfaces.
Currently, it support Pandas, Dask and Ray
(via Modin on Ray). ...

Example:
```python
from qpd_pandas import run_sql_on_pandas
import pandas as pd

df = pd.DataFrame([[0,1],[2,3],[0,5]], columns=["a","b"])
res = run_sql_on_pandas("SELECT a, SUM(b) AS b, COUNT(*) AS c FROM df GROUP BY a", {"df": df})
print(res)
```

Sections: Query Pandas-like Dataframes Using SQL, Using QPD, On Pandas, On Dask, On Ray, Ignoring Case in SQL, Things to clarify, QPD on Spark (Koalas)?

</details>

### textual-fspicker

A simple Textual filesystem picker dialog library.

`pip install textual-fspicker` · installs (wheel) · licence: MIT · rank 14877 · last release 2026-05-20 · [PyPI](https://pypi.org/project/textual-fspicker/) · [docs](https://textual-fspicker.davep.dev/) · [source](https://github.com/davep/textual-fspicker)

<details><summary>README extract</summary>

This library provides a simple set of filesystem navigation and picking
dialogs. The aim is to provide "ready to go" dialogs that should also be
fairly easy to tailor to your own applications.

Sections: textual-fspicker, Introduction, Using the library, TODO

</details>

### django-drf-filepond

Filepond server app for Django REST Framework

`pip install django-drf-filepond` · installs (wheel) · licence: BSD License · rank 14882 · last release 2026-01-15 · [PyPI](https://pypi.org/project/django-drf-filepond/)

<details><summary>README extract</summary>

django-drf-filepond is a Django app that provides a filepond server-side implementation for Django/Django REST Framework projects. The app can be easily added to your Django projects to provide a server-side API for the filepond file upload library.

django-drf-filepond supports remote storage of uploads via *django-storages* ...

Example:
```python
import os
...
DJANGO_DRF_FILEPOND_UPLOAD_TMP = os.path.join(BASE_DIR, 'filepond-temp-uploads')
...
```

...

</details>

### python-librsync

Python ctypes wrapper for librsync.

`pip install python-librsync` · installs from source (sdist only) · licence: MIT · rank 14886 · last release 2013-06-04 · [PyPI](https://pypi.org/project/python-librsync/)

<details><summary>README extract</summary>

A SmartFile Open Source project. Read more about how SmartFile
uses and contributes to Open Source software.

A ctypes wrapper for librsync. Provides `signature()`, `delta()`, and
`patch()` functions.

There are three steps necessary to synchronize a file. Two steps are performed
on the source file and one on the destination.

1. ...

Example:
```python
import librsync

# The destination file.
dst = file('Resume-v1.0.pdf', 'rb')

# The source file.
src = file('Resume-v1.2.pdf', 'rb')

# Where we will write the synchronized copy.
synced = file('Resume-latest.pdf', 'wb')

# Step 1: prepare signature of the destination file
signature = librsync.signature(dst)

...
```

Sections: Introduction, Extending

</details>

### pysdl2-dll

Pre-built SDL2 binaries for PySDL2

`pip install pysdl2-dll` · installs (wheel) · licence: MPL-2.0 · rank 14893 · last release 2026-05-26 · [PyPI](https://pypi.org/project/pysdl2-dll/)

<details><summary>README extract</summary>

pysdl2-dll is a Python package that bundles the SDL2 binaries in pip-installable form for macOS and Windows, making it easier to create and run scripts/packages that use the PySDL2 library. ...

Sections: pysdl2-dll, Requirements, Linux Requirements, Usage

</details>

### sqlalchemy-declarative-extensions

Library to declare additional kinds of objects not natively supported by SQLAlchemy/Alembic.

`pip install sqlalchemy-declarative-extensions` · installs (wheel) · licence: not stated · rank 14920 · last release 2026-11-05 · [PyPI](https://pypi.org/project/sqlalchemy-declarative-extensions/) · [docs](https://sqlalchemy-declarative-extensions.readthedocs.io/en/latest/) · [source](https://github.com/dancardin/sqlalchemy-declarative-extensions)

<details><summary>README extract</summary>

See the full documentation
here.

Adds extensions to SQLAlchemy (and/or Alembic) which allows declaratively
stating the existence of additional kinds of objects about your database not
natively supported by SQLAlchemy/Alembic.

The primary function(s) of this library include: ...

Example:
```python
from sqlalchemy import Column, types, select
from sqlalchemy.orm import as_declarative
from sqlalchemy_declarative_extensions import (
    declarative_database, Schemas, Roles, Row, View, view,
)
from sqlalchemy_declarative_extensions.dialects.postgresql import (
    DefaultGrant, Function, Trigger, Role
)
...
```

...

</details>

### prefect-email

Prefect integrations for interacting with email.

`pip install prefect-email` · installs (wheel) · licence: Apache Software License · rank 14923 · last release 2026-09-08 · [PyPI](https://pypi.org/project/prefect-email/)

### i2

The middleware toolbox: signatures as data, decorators, wrappers and multi-object composition

`pip install i2` · installs (wheel) · licence: Apache-2.0 · rank 14939 · last release 2026-10-20 · [PyPI](https://pypi.org/project/i2/) · [docs](https://i2mint.github.io/i2) · [source](https://github.com/i2mint/i2)

<details><summary>README extract</summary>

Core tools for minting code.

For human readers: Documentation here.

<!-- epythet:agentic-readme:start -->

`i2` ships tooling for coding agents. If you are one, start here.

Skills (Agent Skills format), for any agent host.

| Skill | Use it to | ...

Example:
```python
from i2.castgraph import TransformationGraph

graph = TransformationGraph()

# Register transformations between types
@graph.register_edge(str, float)
def str_to_float(s, ctx):
    return float(s)

@graph.register_edge(float, int)
def float_to_int(f, ctx):
    return int(f)

# Automatically routes str -> float -> int
...
```

...

</details>

### read-version

Extract your project's __version__ variable

`pip install read-version` · installs (wheel) · licence: MIT License · rank 14964 · last release 2021-07-25 · [PyPI](https://pypi.org/project/read-version/) · [source](https://github.com/jwodder/read_version)

<details><summary>README extract</summary>

GitHub
| PyPI
| Issues
| Changelog

Note: As of the release of setuptools 46.4.0, setuptools natively supports
using the `attr:` directive in `setup.cfg` to set the project version based
on static analysis of the project source. This makes the bulk of
`read_version`'s use cases obsolete, and so it will not receive further
development. ...

Example:
```python
with open(join(dirname(file), 'package_name', 'init.py')) as fp:
    for line in fp:
        m = re.search(r'^\s*version\s*=\s*([\'"])([^\'"]+)\1\s*$', line)
        if m:
            version = m.group(2)
            break
    else:
        raise RuntimeError('Unable to find own version string')

setup(
    version = version,
    ...
)
```

Sections: Usage, The Functional Way, The Declarative Way, API, Restrictions

</details>

### coverage-conditional-plugin

Conditional coverage based on any rules you define!

`pip install coverage-conditional-plugin` · installs (wheel) · licence: MIT License · rank 14972 · last release 2023-06-02 · [PyPI](https://pypi.org/project/coverage-conditional-plugin/) · [source](https://github.com/wemake-services/coverage-conditional-plugin)

<details><summary>README extract</summary>

Conditional coverage based on any rules you define!

Some projects have different parts that relies on different environments:

- Python version, some code is only executed on specific versions and ignored on others
- OS version, some code might be Windows, Mac, or Linux only ...

Example:
```python
try:  # pragma: has-django
    import django
except ImportError:  # pragma: has-no-django
    django = None

def run_if_django_is_installed():
    if django is not None:  # pragma: has-django
        ...
```

Sections: coverage-conditional-plugin, Example, Writing pragma rules, Writing omits

</details>

### requests-http-signature

A Requests auth module for HTTP Message Signatures

`pip install requests-http-signature` · installs (wheel) · licence: Apache Software License · rank 14989 · last release 2026-10-26 · [PyPI](https://pypi.org/project/requests-http-signature/)

<details><summary>README extract</summary>

requests-http-signature is a Requests authentication plugin (`requests.auth.AuthBase` subclass) implementing
the
IETF RFC 9421 HTTP Message Signatures standard.

Example:
```python
import requests
from http_message_signatures import HTTPSignatureKeyResolver
from requests_http_signature import HTTPSignatureAuth, algorithms

preshared_key_id = 'squirrel'
preshared_secret = b'monorail_cat'
url = '

auth = HTTPSignatureAuth(key=preshared_secret,
                         key_id=preshared_key_id,
...
```

Sections: Usage, Verifying responses, Asymmetric key algorithms, Digest algorithms, Request bodies and streams, Component identifiers, External signing, Signature selection and verification policies, Redirects, Links, Bugs

</details>

### lyft-dataset-sdk

SDK for Lyft dataset.

`pip install lyft-dataset-sdk` · installs (wheel) · licence: Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) · rank 14995 · last release 2019-09-24 · [PyPI](https://pypi.org/project/lyft-dataset-sdk/)

<details><summary>README extract</summary>

Welcome to the devkit for the Lyft Level 5 AV dataset! This devkit shall help you to visualise and explore our dataset.

Sections: Lyft Dataset SDK, Getting Started, Dataset Download, Tutorial and Reference Model, Dataset structure, Data Exploration Tutorial

</details>

### pyexcel-ods

A wrapper library to read, manipulate and write data in ods format

`pip install pyexcel-ods` · installs (wheel) · licence: New BSD · rank 14997 · last release 2020-10-08 · [PyPI](https://pypi.org/project/pyexcel-ods/)

<details><summary>README extract</summary>

pyexcel-ods is a tiny wrapper library to read, manipulate and write data in
ods format using python 2.6 and python 2.7. You are likely to use it with
pyexcel.
pyexcel-ods3 is a sister library that
depends on ezodf and lxml. pyexcel-odsr
is the other sister library that has no external dependency but do ods reading only

Example:
```python
>>> from pyexcel_ods import save_data
>>> data = OrderedDict() # from collections import OrderedDict
>>> data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
>>> data.update({"Sheet 2": [["row 1", "row 2", "row 3"]]})
>>> save_data("your_file.ods", data)
```

...

</details>

### asynckivy

Async library for Kivy

`pip install asynckivy` · installs (wheel) · licence: MIT · rank 15000 · last release 2026-10-23 · [PyPI](https://pypi.org/project/asynckivy/) · [docs](https://asyncgui.github.io/asynckivy/) · [source](https://github.com/asyncgui/asynckivy)

<details><summary>README extract</summary>

Youtube
日本語doc

`asynckivy` is an async library that saves you from ugly callback-style code,
like most of async libraries do.
Let's say you want to do:

1. `print('A')`
1. wait for 1sec
1. `print('B')`
1. wait for a button to be pressed
1. `print('C')`

in that order.
Your code would look like this:

It's not easy to understand. ...

Example:
```python
import asynckivy as ak

async def some_task(button):
    # waits for 2 seconds to elapse
    dt = await ak.sleep(2)
    print(f'{dt} seconds have elapsed')

    # waits for a button to be pressed
    await ak.event(button, 'on_press')

    # waits for the value of 'button.x' to change
    __, x = await ak.event(button, 'x')
...
```

Sections: AsyncKivy, Usage, Tested on

</details>

## Also in this topic

- [idna](internet-name-service-dns.md#idna) - Internationalized Domain Names in Applications (IDNA)
- [urllib3](internet-www-http.md#urllib3) - HTTP library with thread-safe connection pooling, file post, and more.
- [requests](internet-www-http.md#requests) - Python HTTP for Humans.
- [pydantic](internet.md#pydantic) - Data validation using Python type hints
- [yarl](internet-www-http.md#yarl) - Yet another URL library
- [propcache](internet-www-http.md#propcache) - Accelerated property cache
- [annotated-doc](internet.md#annotated-doc) - Document parameters, class attributes, return types, and variables inline, with Annotated.
- [fastapi](internet.md#fastapi) - FastAPI framework, high performance, easy to learn, fast to code, ready for production
- [tqdm](desktop-environment.md#tqdm) - Fast, Extensible Progress Meter
- [pyasn1](communications.md#pyasn1) - Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208)
- [pydantic-settings](internet.md#pydantic-settings) - Settings management using Pydantic
- [pyasn1-modules](communications.md#pyasn1-modules) - A collection of ASN.1-based protocols modules
- [hatchling](software-development-build-tools.md#hatchling) - Modern, extensible Python build backend
- [regex](scientific-engineering-information-analysis.md#regex) - Alternative regular expression module, to replace re.
- [scipy](scientific-engineering.md#scipy) - Fundamental algorithms for scientific computing in Python
- [soupsieve](internet-www-http.md#soupsieve) - A modern CSS selector implementation for Beautiful Soup.
- [typer](software-development.md#typer) - Typer, build great CLIs. Easy to code. Based on Python type hints.
- [proto-plus](software-development-code-generators.md#proto-plus) - Beautiful, Pythonic protocol buffers
- [wcwidth](software-development-internationalization.md#wcwidth) - Measures the displayed width of unicode strings in a terminal
- [dnspython](internet-name-service-dns.md#dnspython) - DNS toolkit
- [docstring-parser](documentation-sphinx.md#docstring-parser) - Parse Python docstrings in reST, Google and Numpydoc format
- [Werkzeug](internet-www-http.md#werkzeug) - The comprehensive WSGI web application library.
- [networkx](scientific-engineering-bio-informatics.md#networkx) - Python package for creating and manipulating graphs and networks
- [psycopg2-binary](database.md#psycopg2-binary) - psycopg2 - Python-PostgreSQL Database Adapter
- [cloudpickle](scientific-engineering.md#cloudpickle) - Pickler class to extend the standard pickle.Pickler functionality
- [isodate](internet.md#isodate) - An ISO 8601 date/time/duration parser and formatter
- [Flask](internet-www-http.md#flask) - A simple framework for building complex web applications.
- [pyOpenSSL](security-cryptography.md#pyopenssl) - Python wrapper module around the OpenSSL library
- [joblib](scientific-engineering.md#joblib) - Lightweight pipelining with Python functions
- [psycopg](database.md#psycopg) - PostgreSQL database adapter for Python
- [websocket-client](internet.md#websocket-client) - WebSocket client for Python with low level API options
- [psycopg-binary](database.md#psycopg-binary) - PostgreSQL database adapter for Python -- C optimisation distribution
- [langchain](scientific-engineering-artificial-intelligence.md#langchain) - Building applications with LLMs through composability
- [google-genai](internet.md#google-genai) - GenAI Python SDK
- [langchain-core](scientific-engineering-artificial-intelligence.md#langchain-core) - Building applications with LLMs through composability
- [mpmath](scientific-engineering-mathematics.md#mpmath) - Python library for arbitrary-precision floating-point arithmetic
- [SecretStorage](security.md#secretstorage) - Python bindings to FreeDesktop.org Secret Service API
- [backoff](internet-www-http.md#backoff) - Function decoration for backoff and retry
- [pexpect](software-development.md#pexpect) - Pexpect allows easy control of interactive console applications.
- [httplib2](internet-www-http.md#httplib2) - A comprehensive HTTP client library.
- [python-docx](office-business-office-suites.md#python-docx) - Create, read, and update Microsoft Word .docx files.
- [babel](software-development-internationalization.md#babel) - Internationalization utilities
- [pymupdf](multimedia-graphics.md#pymupdf) - A high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents.
- [gunicorn](internet.md#gunicorn) - WSGI HTTP Server for UNIX
- [Markdown](communications-email.md#markdown) - Python implementation of John Gruber's Markdown.
- [python-pptx](office-business-office-suites.md#python-pptx) - Create, read, and update PowerPoint 2007+ (.pptx) files.
- [snowflake-connector-python](database.md#snowflake-connector-python) - Snowflake DB driver for Python
- [asttokens](software-development-code-generators.md#asttokens) - Annotate AST trees with source code positions
- [onnxruntime](scientific-engineering.md#onnxruntime) - ONNX Runtime is a runtime accelerator for Machine Learning models
- [google-cloud-aiplatform](internet.md#google-cloud-aiplatform) - Vertex AI API client library
- [poetry-core](software-development-build-tools.md#poetry-core) - Poetry PEP 517 Build Backend
- [Cython](software-development-code-generators.md#cython) - The Cython compiler for writing C extensions in the Python language.
- [pypdfium2](multimedia-graphics.md#pypdfium2) - Python bindings to PDFium
- [beartype](software-development-code-generators.md#beartype) - Unbearably fast near-real-time pure-Python runtime-static type-checker.
- [xlrd](database.md#xlrd) - Library for developers to extract data from Microsoft Excel (tm) .xls spreadsheet files
- [argon2-cffi-bindings](security.md#argon2-cffi-bindings) - Low-level CFFI bindings for Argon2
- [invoke](software-development.md#invoke) - Pythonic task execution
- [psycopg2](database.md#psycopg2) - psycopg2 - Python-PostgreSQL Database Adapter
- [argcomplete](software-development.md#argcomplete) - Bash tab completion for argparse
- [caio](software-development.md#caio) - Asynchronous file IO for Linux MacOS or Windows.
- [torch](scientific-engineering.md#torch) - Tensors and Dynamic neural networks in Python with strong GPU acceleration
- [pydantic-extra-types](internet.md#pydantic-extra-types) - Extra Pydantic types.
- [openapi-pydantic](software-development.md#openapi-pydantic) - Modern, type-safe OpenAPI schemas in Python using Pydantic 1.8+ and 2.x
- [langchain-protocol](scientific-engineering-artificial-intelligence.md#langchain-protocol) - Python bindings for the LangChain agent streaming protocol
- [psycopg-pool](database.md#psycopg-pool) - Connection Pool for Psycopg
- [grpclib](internet-www-http.md#grpclib) - Pure-Python gRPC implementation for asyncio
- [kombu](communications.md#kombu) - Messaging library for Python.
- [humanfriendly](communications.md#humanfriendly) - Human friendly output for text interfaces using Python
- [Django](internet-www-http.md#django) - A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [fastapi-cli](software-development.md#fastapi-cli) - Run and manage FastAPI apps from the command line with FastAPI CLI. 🚀
- [pg8000](database-front-ends.md#pg8000) - PostgreSQL interface library
- [redshift-connector](database-front-ends.md#redshift-connector) - Redshift interface library
- [av](multimedia-sound-audio.md#av) - Pythonic bindings for FFmpeg's libraries.
- [boolean.py](scientific-engineering-mathematics.md#booleanpy) - Define boolean algebras, create and parse boolean expressions and create custom boolean DSL.
- [poetry](software-development-build-tools.md#poetry) - Python dependency management and packaging made easy.
- [cleo](software-development.md#cleo) - Cleo allows you to create beautiful and testable command-line interfaces.
- [peewee](database.md#peewee) - a little orm
- [langchain-text-splitters](scientific-engineering-artificial-intelligence.md#langchain-text-splitters) - LangChain text splitting utilities
- [coloredlogs](communications.md#coloredlogs) - Colored terminal output for Python's logging module
- [strands-agents](scientific-engineering-artificial-intelligence.md#strands-agents) - A model-driven approach to building AI agents in just a few lines of code
- [pymssql](database.md#pymssql) - DB-API interface to Microsoft SQL Server for Python. (new Cython-based version)
- [fastapi-cloud-cli](software-development.md#fastapi-cloud-cli) - Deploy and manage FastAPI Cloud apps from the command line 🚀
- [PyOTP](software-development.md#pyotp) - Python One Time Password Library
- [qrcode](multimedia-graphics.md#qrcode) - QR Code image generator
- [gspread](office-business-financial.md#gspread) - Google Spreadsheets Python API
- [fastavro](scientific-engineering-information-analysis.md#fastavro) - Fast read/write of AVRO files
- [h5py](database.md#h5py) - Read and write HDF5 files from Python
- [genai-prices](internet.md#genai-prices) - Calculate prices for calling LLM inference APIs.
- [pydantic-ai-slim](internet.md#pydantic-ai-slim) - AI Agent Framework, the Pydantic way, slim package
- [pydantic-graph](internet.md#pydantic-graph) - Graph and state machine library
- [holidays](file-formats-json.md#holidays) - Open World Holidays Framework
- [nvidia-nccl-cu12](scientific-engineering.md#nvidia-nccl-cu12) - NVIDIA Collective Communication Library (NCCL) Runtime
- [pillow-heif](multimedia-graphics.md#pillow-heif) - Python interface for libheif library
- [nvidia-nccl-cu13](scientific-engineering.md#nvidia-nccl-cu13) - NVIDIA Collective Communication Library (NCCL) Runtime
- [mysql-connector-python](database.md#mysql-connector-python) - A self-contained Python driver for communicating with MySQL servers, using an API that is compliant with the Python Database API Specification v2.0 (PEP 249).
- [nvidia-cudnn-cu13](scientific-engineering.md#nvidia-cudnn-cu13) - cuDNN runtime libraries
- [gevent](internet.md#gevent) - Coroutine-based network library
- [scikit-image](scientific-engineering.md#scikit-image) - Image processing in Python
- [nvidia-cublas](scientific-engineering.md#nvidia-cublas) - CUBLAS native runtime libraries
- [mlflow-skinny](scientific-engineering-artificial-intelligence.md#mlflow-skinny) - MLflow is an open source platform for the complete machine learning lifecycle
- [nvidia-nvjitlink](scientific-engineering.md#nvidia-nvjitlink) - Nvidia JIT LTO Library
- [nvidia-nvshmem-cu13](scientific-engineering.md#nvidia-nvshmem-cu13) - NVSHMEM creates a global address space that provides efficient and scalable communication for NVIDIA GPU clusters.
- [nvidia-cuda-nvrtc](scientific-engineering.md#nvidia-cuda-nvrtc) - NVRTC native runtime libraries
- [nvidia-cufft](scientific-engineering.md#nvidia-cufft) - CUFFT native runtime libraries
- [nvidia-cusolver](scientific-engineering.md#nvidia-cusolver) - CUDA solver native runtime libraries
- [nvidia-cusparse](scientific-engineering.md#nvidia-cusparse) - CUSPARSE native runtime libraries
- [nvidia-cuda-runtime](scientific-engineering.md#nvidia-cuda-runtime) - CUDA Runtime native Libraries
- [pyproj](scientific-engineering.md#pyproj) - Python interface to PROJ (cartographic projections and coordinate transformations library)
- [nvidia-cuda-cupti](scientific-engineering.md#nvidia-cuda-cupti) - CUDA profiling tools runtime libs.
- [nvidia-cufile](scientific-engineering.md#nvidia-cufile) - cuFile GPUDirect libraries
- [nvidia-nvtx](scientific-engineering.md#nvidia-nvtx) - NVIDIA Tools Extension
- [snowflake-sqlalchemy](database.md#snowflake-sqlalchemy) - Snowflake SQLAlchemy Dialect
- [nvidia-curand](scientific-engineering.md#nvidia-curand) - CURAND native runtime libraries
- [streamlit](database-front-ends.md#streamlit) - A faster way to build and share data apps
- [requirements-parser](software-development.md#requirements-parser) - This is a small Python module for parsing Pip requirement files.
- [twilio](communications-telephony.md#twilio) - Twilio API client and TwiML generator
- [pymdown-extensions](internet-www-http.md#pymdown-extensions) - Extension pack for Python Markdown.
- [agate](scientific-engineering-information-analysis.md#agate) - A data analysis library that is optimized for humans instead of machines.
- [jsonconversion](internet-www-http.md#jsonconversion) - This python module helps converting arbitrary Python objects into JSON strings and back.
- [leather](multimedia-graphics.md#leather) - Python charting for 80% of humans.
- [ua-parser](internet-www-http.md#ua-parser) - Python port of Browserscope's user agent parser
- [mlflow](scientific-engineering-artificial-intelligence.md#mlflow) - MLflow is an open source platform for the complete machine learning lifecycle
- [emoji](internet-www-http.md#emoji) - Emoji for Python
- [fpdf2](multimedia-graphics.md#fpdf2) - Simple & fast PDF generation for Python
- [nvidia-cudnn-cu12](scientific-engineering.md#nvidia-cudnn-cu12) - cuDNN runtime libraries
- [ua-parser-builtins](internet-www-http.md#ua-parser-builtins) - Precompiled rules for User Agent Parser
- [nvidia-cublas-cu12](scientific-engineering.md#nvidia-cublas-cu12) - CUBLAS native runtime libraries
- [pydot](scientific-engineering-visualization.md#pydot) - Python interface to Graphviz's Dot
- [jira](internet-www-http.md#jira) - Python library for interacting with JIRA via REST APIs.
- [wandb](scientific-engineering-artificial-intelligence.md#wandb) - A CLI and library for interacting with the Weights & Biases API.
- [service-identity](security-cryptography.md#service-identity) - Service identity verification for pyOpenSSL & cryptography.
- [tensorboard](scientific-engineering-mathematics.md#tensorboard) - TensorBoard lets you watch Tensors Flow
- [jwcrypto](security.md#jwcrypto) - Implementation of JOSE Web standards
- [progressbar2](desktop-environment.md#progressbar2) - A Python Progressbar library to provide visual (yet text based) progress to long running operations.
- [logfire](internet.md#logfire) - Pydantic Logfire Python SDK and command-line interface
- [nvidia-cuda-nvrtc-cu12](scientific-engineering.md#nvidia-cuda-nvrtc-cu12) - NVRTC native runtime libraries
- [pydub](multimedia-sound-audio.md#pydub) - Manipulate audio with an simple and easy high level interface
- [Flask-Login](internet-www-http.md#flask-login) - User authentication and session management for Flask.
- [nvidia-cufft-cu12](scientific-engineering.md#nvidia-cufft-cu12) - CUFFT native runtime libraries
- [nvidia-cusparse-cu12](scientific-engineering.md#nvidia-cusparse-cu12) - CUSPARSE native runtime libraries
- [nvidia-cusolver-cu12](scientific-engineering.md#nvidia-cusolver-cu12) - CUDA solver native runtime libraries
- [pooch](scientific-engineering.md#pooch) - A friend to fetch your data files
- [genson](file-formats-json.md#genson) - GenSON is a powerful, user-friendly JSON Schema generator.
- [nvidia-nvjitlink-cu12](scientific-engineering.md#nvidia-nvjitlink-cu12) - Nvidia JIT LTO Library
- [nvidia-cuda-runtime-cu12](scientific-engineering.md#nvidia-cuda-runtime-cu12) - CUDA Runtime native Libraries
- [nvidia-curand-cu12](scientific-engineering.md#nvidia-curand-cu12) - CURAND native runtime libraries
- [yfinance](office-business-financial.md#yfinance) - Download market data from Yahoo! Finance API
- [nvidia-cuda-cupti-cu12](scientific-engineering.md#nvidia-cuda-cupti-cu12) - CUDA profiling tools runtime libs.
- [SQLAlchemy-Utils](internet-www-http.md#sqlalchemy-utils) - Various utility functions for SQLAlchemy.
- [langchain-classic](scientific-engineering-artificial-intelligence.md#langchain-classic) - Building applications with LLMs through composability
- [typer-slim](software-development.md#typer-slim) - Typer, build great CLIs. Easy to code. Based on Python type hints.
- [parse](software-development-code-generators.md#parse) - parse() is the opposite of format()
- [pfzy](software-development.md#pfzy) - Python port of the fzy fuzzy string matching algorithm
- [mlflow-tracing](scientific-engineering-artificial-intelligence.md#mlflow-tracing) - MLflow Tracing SDK is an open-source, lightweight Python package that only includes the minimum set of dependencies and functionality to instrument your code/models/agents with MLflow Tracing.
- [nvidia-nvtx-cu12](scientific-engineering.md#nvidia-nvtx-cu12) - NVIDIA Tools Extension
- [inquirerpy](software-development.md#inquirerpy) - Python port of Inquirer.js (A collection of common interactive command-line user interfaces)
- [jsonlines](internet-log-analysis.md#jsonlines) - Library with helpers for the jsonlines file format
- [pyserial](communications.md#pyserial) - Python Serial Port Extension
- [watchtower](software-development.md#watchtower) - Python CloudWatch Logging
- [asyncssh](internet.md#asyncssh) - AsyncSSH: Asynchronous SSHv2 client and server library
- [mkdocs-material-extensions](internet-www-http.md#mkdocs-material-extensions) - Extension pack for Python Markdown and MkDocs Material.
- [optuna](scientific-engineering.md#optuna) - A hyperparameter optimization framework
- [tensorflow](scientific-engineering.md#tensorflow) - TensorFlow is an open source machine learning framework for everyone.
- [tensorboard-data-server](scientific-engineering-mathematics.md#tensorboard-data-server) - Fast data loading for TensorBoard
- [pyclipper](multimedia-graphics.md#pyclipper) - Cython wrapper for the C++ translation of the Angus Johnson's Clipper library (ver. 6.4.2)
- [pika](communications.md#pika) - Pika Python AMQP Client Library
- [geographiclib](scientific-engineering-gis.md#geographiclib) - The geodesic routines from GeographicLib
- [aiosmtplib](communications.md#aiosmtplib) - asyncio SMTP client
- [geopy](scientific-engineering-gis.md#geopy) - Python Geocoding Toolbox
- [polyfactory](software-development.md#polyfactory) - Mock data generation factories
- [rq](internet.md#rq) - RQ is a simple, lightweight, library for creating background jobs, and processing them.
- [snowflake-snowpark-python](database.md#snowflake-snowpark-python) - Snowflake Snowpark for Python
- [pikepdf](multimedia-graphics.md#pikepdf) - Read, write, repair, and transform PDFs in Python, powered by qpdf
- [clickhouse-driver](database.md#clickhouse-driver) - Python driver with native interface for ClickHouse
- [kfp](scientific-engineering.md#kfp) - Kubeflow Pipelines SDK
- [timm](scientific-engineering.md#timm) - PyTorch Image Models
- [svix](software-development.md#svix) - Svix webhooks API client and webhook verification library
- [aiohttp-cors](internet-www-http.md#aiohttp-cors) - CORS support for aiohttp
- [python-snappy](internet.md#python-snappy) - Python library for the snappy compression library from Google
- [launchdarkly-eventsource](software-development.md#launchdarkly-eventsource) - LaunchDarkly SSE Client
- [launchdarkly-server-sdk](software-development.md#launchdarkly-server-sdk) - LaunchDarkly SDK for Python
- [user-agents](internet-www-http.md#user-agents) - A library to identify devices (phones, tablets) and their capabilities by parsing browser user agent strings.
- [oletools](security.md#oletools) - Python tools to analyze security characteristics of MS Office and OLE files (also called Structured Storage, Compound File Binary Format or Compound Document File Format), for Malware Analysis and Incident Response #DFIR
- [office365-rest-python-client](internet-www-http.md#office365-rest-python-client) - Microsoft 365 & Microsoft Graph Library for Python
- [primp](internet-www-http.md#primp) - HTTP client that can impersonate web browsers
- [altgraph](scientific-engineering-mathematics.md#altgraph) - Python graph (network) package
- [cytoolz](scientific-engineering.md#cytoolz) - Cython implementation of Toolz: High performance functional utilities
- [dependency-injector](software-development.md#dependency-injector) - Dependency injection framework for Python
- [pyinstaller](software-development.md#pyinstaller) - PyInstaller bundles a Python application and all its dependencies into a single package.
- [JayDeBeApi](database.md#jaydebeapi) - Use JDBC database drivers from Python 2/3 or Jython with a DB-API.
- [Protego](internet-www-http.md#protego) - Pure-Python robots.txt parser with support for modern conventions
- [pyrate-limiter](software-development-documentation.md#pyrate-limiter) - Python rate limiter with pluggable algorithms and backends
- [pydantic-evals](internet.md#pydantic-evals) - Framework for evaluating stochastic code execution, especially code making use of LLMs
- [fetch-use](internet-www-http.md#fetch-use) - Python client for Browser-Use Fetch HTTP service
- [num2words](software-development-internationalization.md#num2words) - Modules to convert numbers to words. Easily extensible.
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [tritonclient](scientific-engineering.md#tritonclient) - Python client library and utilities for communicating with Triton Inference Server
- [PyPika](scientific-engineering-information-analysis.md#pypika) - A SQL query builder API for Python
- [autobahn](communications.md#autobahn) - WebSocket client & server library, WAMP real-time framework
- [Flask-WTF](internet-www-http.md#flask-wtf) - Form rendering, validation, and CSRF protection for Flask with WTForms.
- [dj-database-url](internet-www-http.md#dj-database-url) - Use Database URLs in your Django Application.
- [segno](multimedia-graphics.md#segno) - QR Code and Micro QR Code generator for Python
- [nvidia-cufile-cu12](scientific-engineering.md#nvidia-cufile-cu12) - cuFile GPUDirect libraries
- [parsimonious](scientific-engineering-information-analysis.md#parsimonious) - (Soon to be) the fastest pure-Python PEG parser I could muster
- [PGPy](security.md#pgpy) - Pretty Good Privacy for Python
- [bottle](internet-www-http.md#bottle) - Fast and simple WSGI-framework for small web-applications.
- [typesafe-sdk](scientific-engineering-artificial-intelligence.md#typesafe-sdk) - Python SDK for TypeSafe AI API.
- [atlassian-python-api](internet.md#atlassian-python-api) - Python Atlassian REST API Wrapper
- [cssutils](internet.md#cssutils) - A CSS Cascading Style Sheets library for Python
- [markdown2](software-development-documentation.md#markdown2) - A fast and complete Python implementation of Markdown
- [standardwebhooks](software-development.md#standardwebhooks) - Standard Webhooks
- [SpeechRecognition](multimedia-sound-audio.md#speechrecognition) - Library for performing speech recognition, with support for several engines and APIs, online and offline.
- [xlwt](database.md#xlwt) - Library to create spreadsheet files compatible with MS Excel 97/2000/XP/2003 XLS files, on any platform, with Python 2.6, 2.7, 3.3+
- [dash](database-front-ends.md#dash) - A Python framework for building reactive web-apps. Developed by Plotly.
- [fabric](software-development.md#fabric) - High level SSH command execution
- [deepagents](scientific-engineering-artificial-intelligence.md#deepagents) - Production-ready, extensible agent harness with a built-in filesystem and context management, sub-agent delegation, skills, and long-term memory.
- [python-telegram-bot](communications-chat.md#python-telegram-bot) - We have made you a wrapper you can't refuse
- [w3lib](internet-www-http.md#w3lib) - Library of web-related functions
- [Hypercorn](internet-www-http.md#hypercorn) - A ASGI Server based on Hyper libraries and inspired by Gunicorn
- [ortools](office-business-scheduling.md#ortools) - Google OR-Tools python libraries and modules
- [Pint](scientific-engineering.md#pint) - Physical quantities module
- [python-crfsuite](scientific-engineering.md#python-crfsuite) - Python binding for CRFsuite
- [PyOpenGL](multimedia-graphics.md#pyopengl) - Standard OpenGL bindings for Python
- [pypng](multimedia-graphics.md#pypng) - Pure Python library for saving and loading PNG images
- [poethepoet](software-development-build-tools.md#poethepoet) - A task runner that works well with poetry and uv.
- [parse-type](software-development-code-generators.md#parse-type) - Simplifies to build parse types based on the parse module
- [fake-useragent](internet-www-http.md#fake-useragent) - Up-to-date simple useragent faker with real world database
- [python3-openid](internet-www-http.md#python3-openid) - OpenID support for modern servers and consumers.
- [aiormq](internet.md#aiormq) - Pure python AMQP asynchronous client library
- [aio-pika](internet.md#aio-pika) - Wrapper around the aiormq for asyncio and humans
- [catboost](scientific-engineering-artificial-intelligence.md#catboost) - CatBoost Python Package
- [django-celery-beat](communications.md#django-celery-beat) - Database-backed Periodic Tasks.
- [sh](software-development-build-tools.md#sh) - Python subprocess replacement
- [ddgs](internet-www-http.md#ddgs) - Dux Distributed Global Search. A metasearch library that aggregates results from diverse web search services.
- [bedrock-agentcore](scientific-engineering-artificial-intelligence.md#bedrock-agentcore) - An SDK for using Bedrock AgentCore
- [tensorflow-estimator](scientific-engineering.md#tensorflow-estimator) - TensorFlow Estimator.
- [pydantic-ai](internet.md#pydantic-ai) - AI Agent Framework, the Pydantic way
- [mando](software-development.md#mando) - Create Python CLI apps with little to no effort at all!
- [radon](software-development.md#radon) - Code Metrics in Python
- [django-allauth](internet.md#django-allauth) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- [latex2mathml](scientific-engineering-mathematics.md#latex2mathml) - Pure Python library for LaTeX to MathML conversion
- [protobuf-py](file-formats.md#protobuf-py) - Idiomatic Protocol Buffers for Python.
- [probableparsing](scientific-engineering.md#probableparsing) - Common methods for propbable parsers
- [usaddress](scientific-engineering.md#usaddress) - Parse US addresses using conditional random fields
- [llama-index-core](scientific-engineering-artificial-intelligence.md#llama-index-core) - Interface between LLMs and your data
- [python-stdnum](office-business-financial.md#python-stdnum) - Python module to handle standardized numbers and codes
- [flask-babel](internet-www-http.md#flask-babel) - Adds i18n/l10n support for Flask applications.
- [selectolax](internet.md#selectolax) - A fast HTML5 parser with CSS selectors, written in Cython, using the Lexbor engine.
- [python-oxmsg](communications-email.md#python-oxmsg) - Extract attachments from Outlook .msg files.
- [imbalanced-learn](scientific-engineering.md#imbalanced-learn) - Toolbox for imbalanced dataset in machine learning
- [biopython](scientific-engineering.md#biopython) - Freely available tools for computational molecular biology.
- [connectrpc](internet-www-http.md#connectrpc) - Server and client runtime library for Connect RPC
- [svglib](documentation.md#svglib) - A pure-Python library for reading and converting SVG
- [construct](software-development-build-tools.md#construct) - A powerful declarative symmetric parser/builder for binary data
- [discord.py](internet.md#discordpy) - A Python wrapper for the Discord API
- [pydicom](scientific-engineering-medical-science-apps.md#pydicom) - A pure Python package for reading and writing DICOM data
- [firecrawl-py](internet.md#firecrawl-py) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [pyHanko](security-cryptography.md#pyhanko) - Tools for stamping and signing PDF files
- [asgi-correlation-id](internet-www-http.md#asgi-correlation-id) - Middleware correlating project logs to individual requests
- [python-box](software-development.md#python-box) - Advanced Python dictionaries with dot notation access
- [docling-core](database.md#docling-core) - A python library to define and validate data types in Docling.
- [arxiv](scientific-engineering.md#arxiv) - Python wrapper for the arXiv API
- [polib](software-development-internationalization.md#polib) - A library to manipulate gettext files (po and mo files).
- [PySide6-Essentials](database.md#pyside6-essentials) - Python bindings for the Qt cross-platform application and UI framework (Essentials)
- [pyshp](scientific-engineering-gis.md#pyshp) - Pure Python read/write support for ESRI Shapefile format
- [python-ipware](internet-www-http.md#python-ipware) - A Python package to retrieve a client's real IP address.
- [fastapi-mcp](internet-www-http.md#fastapi-mcp) - Automatic MCP server generator for FastAPI applications - converts FastAPI endpoints to MCP tools for LLM integration
- [odfpy](office-business.md#odfpy) - Python API and tools to manipulate OpenDocument files
- [Scrapy](internet-www-http.md#scrapy) - A high-level Web Crawling and Web Scraping framework
- [premailer](communications.md#premailer) - Turns CSS blocks into style attributes
- [vtk](multimedia-graphics.md#vtk) - VTK is an open-source toolkit for 3D computer graphics, image processing, and visualization
- [pyaml](software-development.md#pyaml) - PyYAML-based module to produce a bit more pretty and readable YAML-serialized data
- [cuda-python](education.md#cuda-python) - CUDA Python: Performance meets Productivity
- [pi-heif](multimedia-graphics.md#pi-heif) - Python interface for libheif library
- [intervaltree](scientific-engineering-artificial-intelligence.md#intervaltree) - Editable interval tree data structure for Python 2 and 3
- [ndg-httpsclient](internet.md#ndg-httpsclient) - Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
- [cuda-core](education.md#cuda-core) - cuda.core: pythonic CUDA module
- [spdx-tools](software-development-documentation.md#spdx-tools) - SPDX parser and tools.
- [nvidia-nvshmem-cu12](scientific-engineering.md#nvidia-nvshmem-cu12) - NVSHMEM creates a global address space that provides efficient and scalable communication for NVIDIA GPU clusters.
- [django-otp](security.md#django-otp) - A pluggable framework for adding two-factor authentication to Django using one-time passwords.
- [shiboken6](database.md#shiboken6) - Python/C++ bindings helper module
- [mpire](software-development.md#mpire) - A Python package for easy multiprocessing, but faster than multiprocessing
- [sqlparams](database.md#sqlparams) - Convert between various DB API 2.0 parameter styles.
- [Flask-Session](internet-www-http.md#flask-session) - Server-side session support for Flask
- [yaspin](software-development.md#yaspin) - Yet Another Terminal Spinner
- [pymsteams](internet.md#pymsteams) - Format messages and post to Microsoft Teams.
- [django-ninja](internet.md#django-ninja) - Django Ninja - Fast Django REST framework
- [zxcvbn](security.md#zxcvbn) - 
- [arq](internet.md#arq) - Job queues in python with asyncio and redis
- [semchunk](scientific-engineering-artificial-intelligence.md#semchunk) - A Python library for splitting text into smaller chunks while preserving as much local semantic context as possible.
- [Wikipedia-API](communications-email.md#wikipedia-api) - Python Wrapper for Wikipedia
- [tensorflow-text](scientific-engineering.md#tensorflow-text) - TF.Text is a TensorFlow library of text related ops, modules, and subgraphs.
- [xai-sdk](internet-www-http.md#xai-sdk) - The official Python SDK for the xAI API
- [django-celery-results](communications.md#django-celery-results) - Celery result backends for Django.
- [tensorflow-serving-api](scientific-engineering.md#tensorflow-serving-api) - TensorFlow Serving Python API.
- [lingua-language-detector](scientific-engineering-information-analysis.md#lingua-language-detector) - An accurate natural language detection library, suitable for short text and mixed-language text
- [prance](internet-www-http.md#prance) - Resolving Swagger/OpenAPI 2.0 and 3.0.0 Parser
- [pysbd](scientific-engineering.md#pysbd) - pysbd (Python Sentence Boundary Disambiguation) is a rule-based sentence boundary detection that works out-of-the-box across many languages.
- [pydantic-monty](internet.md#pydantic-monty) - Monty, the Python sandbox: bindings plus the worker binary
- [PySide6-Addons](database.md#pyside6-addons) - Python bindings for the Qt cross-platform application and UI framework (Addons)
- [tom-swe](scientific-engineering-artificial-intelligence.md#tom-swe) - Theory of Mind modeling for Software Engineering assistants
- [nvidia-cuda-cccl](scientific-engineering.md#nvidia-cuda-cccl) - CUDA CCCL
- [pinecone](database.md#pinecone) - Pinecone Python SDK
- [snowflake.core](database.md#snowflakecore) - Snowflake Python API for Resource Management
- [vercel-runtime](internet-www-http.md#vercel-runtime) - 
- [nvidia-cudnn-frontend](scientific-engineering-artificial-intelligence.md#nvidia-cudnn-frontend) - NVIDIA cuDNN Frontend — Python and C++ Graph API with SOTA attention (SDPA / Flash Attention), MoE grouped GEMM fusions, and FP8/MXFP8 kernels for Hopper, Blackwell, and Rubin GPUs.
- [pyusb](scientific-engineering-interface-engine-protocol-translator.md#pyusb) - Easy USB access for Python
- [PySide6](database.md#pyside6) - Python bindings for the Qt cross-platform application and UI framework
- [optax](scientific-engineering-artificial-intelligence.md#optax) - A gradient processing and optimization library in JAX.
- [dbos](database.md#dbos) - Ultra-lightweight durable execution in Python
- [svgwrite](multimedia-graphics.md#svgwrite) - A Python library to create SVG drawings.
- [cadwyn](internet.md#cadwyn) - Production-ready community-driven modern Stripe-like API versioning in FastAPI
- [pdfrw](multimedia-graphics.md#pdfrw) - PDF file reader/writer library
- [duckduckgo-search](internet-www-http.md#duckduckgo-search) - Search for words, documents, images, news, maps and text translation using the DuckDuckGo.com search engine.
- [fido2](internet.md#fido2) - FIDO2/WebAuthn library for implementing clients and servers.
- [formulas](scientific-engineering.md#formulas) - Parse and compile Excel formulas and workbooks in python code.
- [schedula](scientific-engineering.md#schedula) - Produce a plan that dispatches calls based on a graph of functions, satisfying data dependencies.
- [chess](games-entertainment-board-games.md#chess) - A chess library with move generation and validation, Polyglot opening book probing, PGN reading and writing, Gaviota tablebase probing, Syzygy tablebase probing, and XBoard/UCI engine communication.
- [shtab](desktop-environment.md#shtab) - Automagic shell tab completion for Python CLI applications
- [rembg](scientific-engineering.md#rembg) - Remove image background
- [igraph](scientific-engineering.md#igraph) - High performance graph data structures and algorithms
- [dm-tree](scientific-engineering-mathematics.md#dm-tree) - Tree is a library for working with nested data structures.
- [django-anymail](communications-email.md#django-anymail) - Django email backends and webhooks for Amazon SES, Brevo, MailerSend, Mailgun, Mailjet, Mailtrap, Mandrill, Postal, Postmark, Resend, Scaleway TEM, SendGrid, SparkPost, and Unisender Go (EmailBackend, transactional email tracking and inbound email signals)
- [connexion](internet.md#connexion) - Connexion - API first applications with OpenAPI/Swagger
- [pysmb](communications-file-sharing.md#pysmb) - pysmb is an experimental SMB/CIFS library written in Python to support file sharing between Windows and Linux machines
- [pyunormalize](software-development-internationalization.md#pyunormalize) - A library for Unicode normalization (NFC, NFD, NFKC, NFKD) independent of Python's core Unicode database.
- [txtorcon](internet.md#txtorcon) - Twisted-based Tor controller client, with state-tracking and configuration abstractions. https://txtorcon.readthedocs.org https://github.com/meejah/txtorcon
- [yq](software-development.md#yq) - Command-line YAML/XML processor - jq wrapper for YAML/XML documents
- [recurring-ical-events](office-business-scheduling.md#recurring-ical-events) - Calculate recurrence times of events, todos, alarms and journals based on icalendar RFC5545.
- [signxml](software-development.md#signxml) - Python XML Signature and XAdES library
- [chdb](database.md#chdb) - chDB is an in-process OLAP SQL Engine powered by ClickHouse
- [tensorflow-io-gcs-filesystem](scientific-engineering.md#tensorflow-io-gcs-filesystem) - TensorFlow IO
- [connect-python](internet-www-http.md#connect-python) - Server and client runtime library for Connect RPC
- [scrapy-playwright](internet-www-http.md#scrapy-playwright) - Playwright integration for Scrapy
- [rjsmin](internet-www-http.md#rjsmin) - Javascript Minifier
- [assemblyai](scientific-engineering-artificial-intelligence.md#assemblyai) - AssemblyAI Python SDK
- [mdformat](documentation.md#mdformat) - CommonMark compliant Markdown formatter
- [devtools](internet.md#devtools) - Python's missing debug print command, and more.
- [Quart](internet-www-http.md#quart) - A Python ASGI web framework with the same API as Flask
- [Flask-Compress](internet-www-http.md#flask-compress) - Compress responses in your Flask app with gzip, deflate, brotli or zstandard.
- [influxdb-client](database.md#influxdb-client) - InfluxDB 2.0 Python client library
- [marisa-trie](scientific-engineering-information-analysis.md#marisa-trie) - Static memory-efficient and fast Trie-like structures for Python.
- [dirty-equals](internet.md#dirty-equals) - Doing dirty (but extremely useful) things with equals.
- [tzfpy](scientific-engineering-gis.md#tzfpy) - Probably the fastest Python package to convert longitude/latitude to timezone name
- [python-ldap](database.md#python-ldap) - Python modules for implementing LDAP clients
- [gspread-dataframe](office-business-financial.md#gspread-dataframe) - Read/write gspread worksheets using pandas DataFrames
- [pydantic-monty-client](internet.md#pydantic-monty-client) - Python client for the Monty sandbox
- [chdb-core](database.md#chdb-core) - chDB is an in-process OLAP SQL Engine powered by ClickHouse
- [aiogram](communications-chat.md#aiogram) - Modern and fully asynchronous framework for Telegram Bot API
- [rcssmin](internet-www-http.md#rcssmin) - CSS Minifier
- [cloudscraper](internet-www-http.md#cloudscraper) - A Python module to bypass Cloudflare's anti-bot page.
- [pip-system-certs](security-cryptography.md#pip-system-certs) - Automatically configures Python to use system certificates via truststore
- [tuspy](communications-file-sharing.md#tuspy) - A Python client for the tus resumable upload protocol -> http://tus.io
- [javaproperties](software-development.md#javaproperties) - Read & write Java .properties files
- [commonmark](documentation.md#commonmark) - Python parser for the CommonMark Markdown spec
- [dotty-dict](software-development.md#dotty-dict) - Dictionary wrapper for quick access to deeply nested keys.
- [nvidia-nvvm](scientific-engineering.md#nvidia-nvvm) - NVVM Libraries
- [nvidia-cuda-nvcc](scientific-engineering.md#nvidia-cuda-nvcc) - CUDA nvcc
- [nvidia-cuda-crt](scientific-engineering.md#nvidia-cuda-crt) - CUDA C Runtime
- [cloudinary](internet-www-http.md#cloudinary) - Upload, transform, optimize, and manage images and videos with Cloudinary from Python or Django.
- [jwt](internet-www-http.md#jwt) - JSON Web Token library for Python 3.
- [itemloaders](internet-www-http.md#itemloaders) - Base library for scrapy's ItemLoader
- [html-for-docx](software-development-build-tools.md#html-for-docx) - Convert HTML to DOCX easily and quickly
- [itemadapter](internet-www-http.md#itemadapter) - Common interface for data container classes
- [django-polymorphic](database.md#django-polymorphic) - Seamless polymorphic inheritance for Django models.
- [tables](database.md#tables) - Hierarchical datasets for Python
- [word2number](documentation-sphinx.md#word2number) - Convert number words eg. three hundred and forty two to numbers (342).
- [coloraide](internet-www-http.md#coloraide) - A color library for Python.
- [azure-cognitiveservices-speech](scientific-engineering.md#azure-cognitiveservices-speech) - Microsoft Cognitive Services Speech SDK for Python
- [mss](multimedia-graphics.md#mss) - An ultra fast cross-platform multiple screenshots module in pure python using ctypes.
- [coincurve](security-cryptography.md#coincurve) - Safest and fastest Python library for secp256k1 elliptic curve operations
- [loky](scientific-engineering.md#loky) - A robust implementation of concurrent.futures.ProcessPoolExecutor
- [kornia](scientific-engineering-artificial-intelligence.md#kornia) - Open Source Differentiable Computer Vision Library for PyTorch
- [munch](software-development.md#munch) - A dot-accessible dictionary (a la JavaScript objects)
- [mediapipe](scientific-engineering.md#mediapipe) - MediaPipe is the simplest way for researchers and developers to build world-class ML solutions and applications for mobile, edge, cloud and the web. See the privacy notice at https://goo.gle/mediapipe-privacy.
- [albumentations](scientific-engineering.md#albumentations) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volumes, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows.
- [onnxruntime-gpu](scientific-engineering.md#onnxruntime-gpu) - ONNX Runtime is a runtime accelerator for Machine Learning models
- [kgb](software-development.md#kgb) - Utilities for spying on function calls in unit tests.
- [hdbcli](database.md#hdbcli) - SAP HANA Python Client
- [strands-agents-tools](scientific-engineering-artificial-intelligence.md#strands-agents-tools) - A collection of specialized tools for Strands Agents
- [django-js-asset](internet-www-http.md#django-js-asset) - script tag with additional attributes for django.forms.Media
- [uncertainties](education.md#uncertainties) - calculations with values with uncertainties, error propagation
- [python-barcode](multimedia-graphics.md#python-barcode) - Create standard barcodes with Python. No external modules needed. (optional Pillow support included).
- [PasteDeploy](internet-www-http.md#pastedeploy) - Load, configure, and compose WSGI applications and servers
- [pytablewriter](software-development-code-generators.md#pytablewriter) - pytablewriter is a Python library to write a table in various formats: AsciiDoc / CSV / Elasticsearch / HTML / JavaScript / JSON / LaTeX / LDJSON / LTSV / Markdown / MediaWiki / NumPy / Excel / Pandas / Python / reStructuredText / SQLite / TOML / TSV / YAML.
- [djangorestframework-dataclasses](internet-www-http.md#djangorestframework-dataclasses) - A dataclasses serializer for Django REST Framework
- [django-crispy-forms](internet-www-http.md#django-crispy-forms) - Best way to have Django DRY forms
- [chex](scientific-engineering-artificial-intelligence.md#chex) - Chex: Testing made fun, in JAX!
- [llama-index](scientific-engineering-artificial-intelligence.md#llama-index) - Interface between LLMs and your data
- [browserforge](internet-www-http.md#browserforge) - Intelligent browser header & fingerprint generator
- [CoolProp](scientific-engineering.md#coolprop) - Open-source thermodynamic and transport properties database
- [nvidia-cuda-nvdisasm](scientific-engineering.md#nvidia-cuda-nvdisasm) - CUDA nvdisasm
- [ml-collections](scientific-engineering.md#ml-collections) - ML Collections is a library of Python collections designed for ML usecases.
- [clickhouse-sqlalchemy](database.md#clickhouse-sqlalchemy) - Simple ClickHouse SQLAlchemy Dialect
- [nccl4py](education.md#nccl4py) - NCCL4Py: Python bindings for NCCL
- [Arpeggio](software-development-compilers.md#arpeggio) - Packrat parser interpreter
- [asynch](database.md#asynch) - An asyncio driver for ClickHouse with native TCP support
- [django-admin-sortable2](internet-www-http.md#django-admin-sortable2) - Generic drag-and-drop sorting for the List, the Stacked- and the Tabular-Inlines Views in the Django Admin
- [verifiers](scientific-engineering-artificial-intelligence.md#verifiers) - Verifiers: Environments for LLM Reinforcement Learning
- [cadquery](internet.md#cadquery) - CadQuery is a parametric scripting language for creating and traversing CAD models
- [eventlet](internet.md#eventlet) - Highly concurrent networking library
- [PubChemPy](database-front-ends.md#pubchempy) - A simple Python wrapper around the PubChem PUG REST API.
- [open3d](education.md#open3d) - Open3D: A Modern Library for 3D Data Processing.
- [pytube](internet.md#pytube) - Python 3 library for downloading YouTube Videos.
- [crowdstrike-falconpy](security.md#crowdstrike-falconpy) - The CrowdStrike Falcon SDK for Python
- [open-clip-torch](scientific-engineering.md#open-clip-torch) - Open reproduction of contrastive language-image pretraining (CLIP) and related.
- [albucore](scientific-engineering-artificial-intelligence.md#albucore) - High-performance image processing functions for deep learning and computer vision.
- [scim2-filter-parser](internet.md#scim2-filter-parser) - A customizable parser/transpiler for SCIM2.0 filters.
- [stone](software-development-code-generators.md#stone) - Stone is an interface description language (IDL) for APIs.
- [snowflake.-legacy](database.md#snowflake-legacy) - You should switch to the snowflake-uuid package
- [snowflake](database.md#snowflake) - Snowflake Python API
- [translationstring](software-development-internationalization.md#translationstring) - Utility library for i18n relied on by various Repoze and Pyramid packages
- [DBUtils](database.md#dbutils) - Database connections for multi-threaded environments.
- [PyMuPDFb](multimedia-graphics.md#pymupdfb) - MuPDF shared libraries for PyMuPDF.
- [fast-depends](software-development.md#fast-depends) - FastDepends - extracted and cleared from HTTP domain logic FastAPI Dependency Injection System. Async and sync are both supported.
- [configcat-client](software-development.md#configcat-client) - ConfigCat SDK for Python. https://configcat.com
- [dkimpy](communications-email.md#dkimpy) - DKIM (DomainKeys Identified Mail), ARC (Authenticated Receive Chain), and TLSRPT (TLS Report) email signing and verification
- [django-cacheops](internet-www-http.md#django-cacheops) - A slick ORM cache with automatic granular event-driven invalidation for Django.
- [tf-keras](scientific-engineering.md#tf-keras) - Deep learning for humans.
- [python-nvd3](multimedia-graphics.md#python-nvd3) - Python NVD3 - Chart Library for d3.js
- [geocoder](internet.md#geocoder) - Geocoder is a simple and consistent geocoding library.
- [mistral-vibe](software-development.md#mistral-vibe) - Minimal CLI coding agent by Mistral
- [python-statemachine](home-automation.md#python-statemachine) - Python Finite State Machines made easy.
- [fpdf](multimedia-graphics.md#fpdf) - Simple PDF generation for Python
- [django-scim2](internet.md#django-scim2) - A partial implementation of the SCIM 2.0 provider specification for use with Django.
- [svgelements](multimedia-graphics.md#svgelements) - Svg Elements Parsing
- [ariadne](internet-www-http.md#ariadne) - Ariadne is a Python library for implementing GraphQL servers.
- [stagehand](internet-www-http.md#stagehand) - Browserbase's SDK for building browser agents
- [sphinx-autobuild](documentation.md#sphinx-autobuild) - Rebuild Sphinx documentation on changes, with hot reloading in the browser.
- [scrubadub](scientific-engineering-information-analysis.md#scrubadub) - Clean personally identifiable information from dirty dirty text.
- [stockfish](games-entertainment-board-games.md#stockfish) - Wraps the open-source Stockfish chess engine for easy integration into python.
- [Pysher](internet.md#pysher) - Pusher websocket client for python, based on Erik Kulyk's PythonPusherClient
- [pyquaternion](scientific-engineering-mathematics.md#pyquaternion) - A fully featured, pythonic library for representing and using quaternions.
- [django-admin-inline-paginator](internet-www-http.md#django-admin-inline-paginator) - The "Django Admin Inline Paginator" is simple way to paginate your inline in django admin
- [beanie](database.md#beanie) - Asynchronous Python ODM for MongoDB
- [pytest-pretty](internet.md#pytest-pretty) - pytest plugin for printing summary data as I want it
- [PySide6-WebEngine](database.md#pyside6-webengine) - Python bindings for the Qt cross-platform application and UI framework (WebEngine)
- [dominate](internet-www-http.md#dominate) - Dominate is a Python library for creating and manipulating HTML documents using an elegant DOM API.
- [whatthepatch](software-development.md#whatthepatch) - A patch parsing and application library.
- [gnupg](security-cryptography.md#gnupg) - A Python wrapper for GnuPG
- [macholib](software-development-build-tools.md#macholib) - Mach-O header analysis and editing
- [PySide6-Pdf](database.md#pyside6-pdf) - Python bindings for the Qt cross-platform application and UI framework (Pdf)
- [gemmi](scientific-engineering-bio-informatics.md#gemmi) - library for structural biology
- [lazy-imports](software-development.md#lazy-imports) - Tool to support lazy imports
- [svgpathtools](multimedia-graphics.md#svgpathtools) - A collection of tools for manipulating and analyzing SVG Path objects and Bezier curves.
- [pygsheets](office-business-financial.md#pygsheets) - Google Spreadsheets Python API v4
- [litestar](internet.md#litestar) - Litestar - A production-ready, highly performant, extensible ASGI API Framework
- [tensorflow-metadata](scientific-engineering-artificial-intelligence.md#tensorflow-metadata) - Library and standards for schema and statistics.
- [seleniumbase](internet.md#seleniumbase) - SeleniumBase is a framework for web crawling, scraping, and testing. Supports pytest. CDP Mode adds stealth. Includes many tools.
- [faststream](software-development.md#faststream) - A thin, typed Python client for Kafka, RabbitMQ, NATS, Redis and MQTT — with AsyncAPI docs and in-memory testing.
- [stpyv8](internet.md#stpyv8) - Python Wrapper for Google V8 Engine
- [litestar-htmx](internet.md#litestar-htmx) - HTMX Integration for Litestar
- [mongoengine](database.md#mongoengine) - MongoEngine is a Python Object-Document Mapper for working with MongoDB.
- [pyslang](scientific-engineering-electronic-design-automation-eda.md#pyslang) - Python bindings for slang, a library for compiling SystemVerilog
- [circular-dict](software-development-debuggers.md#circular-dict) - CircularDict is a high-performance Python data structure that blends the functionality of dictionaries and circular buffers. Inheriting the usage of traditional dictionaries, it allows you to define constraints on size and memory usage. This way, the CircularDict will be always up-to-date with the last N added elements, ensuring that neither the maximum length nor the memory usage limit is exceeded. It is ideal for caching large data structures while maintaining control over memory footprint.
- [aioredis](software-development.md#aioredis) - asyncio (PEP 3156) Redis support
- [swagger-ui-bundle](internet.md#swagger-ui-bundle) - Swagger UI bundled for usage with Python
- [mido](multimedia-sound-audio.md#mido) - MIDI Objects for Python
- [djangorestframework-role-filters](internet-www-http.md#djangorestframework-role-filters) - django-rest-framework-role-filters
- [model2vec](scientific-engineering-artificial-intelligence.md#model2vec) - Fast State-of-the-Art Static Embeddings
- [psycopg-c](database.md#psycopg-c) - PostgreSQL database adapter for Python -- C optimisation distribution
- [cuid](internet-www-http.md#cuid) - Fast, scalable unique ID generation
- [py-moneyed](office-business-financial.md#py-moneyed) - Provides Currency and Money classes for use in your Python code.
- [urllib3-future](internet-www-http.md#urllib3-future) - urllib3.future is a powerful HTTP 1.1, 2, and 3 client with both sync and async interfaces
- [tensorflow-cpu](scientific-engineering.md#tensorflow-cpu) - TensorFlow is an open source machine learning framework for everyone.
- [falcon](internet-www-http.md#falcon) - The ultra-reliable, fast ASGI+WSGI framework for building data plane APIs at scale.
- [nvidia-cublas-cu11](scientific-engineering.md#nvidia-cublas-cu11) - CUBLAS native runtime libraries
- [interrogate](software-development-documentation.md#interrogate) - Interrogate a codebase for docstring coverage.
- [jh2](internet-www-http.md#jh2) - HTTP/2 State-Machine based protocol implementation
- [mleap](communications-chat.md#mleap) - MLeap Python API
- [param](scientific-engineering.md#param) - Declarative parameters for robust Python classes and a rich API for reactive programming
- [wassima](internet-www-http.md#wassima) - Access your OS root certificates with utmost ease
- [ct3](internet-www-http.md#ct3) - Cheetah is a template engine and code generation tool
- [srt](multimedia-video.md#srt) - A tiny library for parsing, modifying, and composing SRT files.
- [nvidia-cudnn-cu11](scientific-engineering.md#nvidia-cudnn-cu11) - cuDNN runtime libraries
- [niquests](internet-www-http.md#niquests) - Niquests is a simple, yet elegant, HTTP library. It is a drop-in replacement for Requests, which is under feature freeze.
- [vertica-python](database.md#vertica-python) - Official native Python client for the Vertica database.
- [gTTS](multimedia-sound-audio.md#gtts) - gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate text-to-speech API
- [rpyc](internet.md#rpyc) - Remote Python Call (RPyC) is a transparent and symmetric distributed computing library
- [pinecone-client](database.md#pinecone-client) - Pinecone client (DEPRECATED)
- [construct-typing](software-development-build-tools.md#construct-typing) - Extension for the python package 'construct' that adds typing features
- [nvidia-cuda-nvcc-cu12](scientific-engineering.md#nvidia-cuda-nvcc-cu12) - CUDA nvcc
- [smartsheet-python-sdk](office-business-financial.md#smartsheet-python-sdk) - Library that uses Python to connect to Smartsheet services (using API 2.0).
- [rtoml](internet.md#rtoml) - A TOML library for python implemented in rust.
- [uptime-kuma-api](internet-www-http.md#uptime-kuma-api) - A python wrapper for the Uptime Kuma WebSocket API
- [IMAPClient](communications-email.md#imapclient) - Easy-to-use, Pythonic and complete IMAP client library
- [pysnmp](communications.md#pysnmp) - A Python library for SNMP
- [docstring-parser-fork](documentation-sphinx.md#docstring-parser-fork) - Parse Python docstrings in reST, Google and Numpydoc format
- [pyvista-validation](scientific-engineering.md#pyvista-validation) - Validate and standardize array-like input.
- [gssapi](security.md#gssapi) - Python GSSAPI Wrapper
- [instanttensor](scientific-engineering.md#instanttensor) - An ultra-fast, distributed Safetensors loader
- [pylibjpeg](scientific-engineering-medical-science-apps.md#pylibjpeg) - A Python framework for decoding JPEG and decoding/encoding DICOM RLE data, with a focus on supporting pydicom
- [panel](office-business.md#panel) - The powerful data exploration & web app framework for Python.
- [nicegui](internet-www-http.md#nicegui) - Create web-based user interfaces with Python. The nice way.
- [esprima](software-development-code-generators.md#esprima) - ECMAScript parsing infrastructure for multipurpose analysis in Python
- [xenon](internet-www-http.md#xenon) - Monitor code metrics for Python on your CI server
- [OpenCC](scientific-engineering.md#opencc) - Conversion between Traditional and Simplified Chinese
- [pylibjpeg-openjpeg](scientific-engineering-medical-science-apps.md#pylibjpeg-openjpeg) - A Python wrapper for openjpeg, with a focus on use as a plugin for for pylibjpeg
- [webdavclient3](internet.md#webdavclient3) - WebDAV client, based on original package https://github.com/designerror/webdav-client-python but uses requests instead of PyCURL
- [pyngrok](internet-proxy-servers.md#pyngrok) - The complete ngrok agent for Python: programmatic tunnels for ingress, inspection, webhooks, demos, and APIs
- [langchain-litellm](scientific-engineering-artificial-intelligence.md#langchain-litellm) - An integration package connecting LiteLLM and LangChain
- [nvidia-cuda-runtime-cu11](scientific-engineering.md#nvidia-cuda-runtime-cu11) - CUDA Runtime native Libraries
- [enum-tools](documentation.md#enum-tools) - Tools to expand Python's enum module.
- [rauth](internet-www-http.md#rauth) - A Python library for OAuth 1.0/a, 2.0, and Ofly.
- [pyswisseph](religion.md#pyswisseph) - Python extension to the Swiss Ephemeris
- [yattag](internet-www-http.md#yattag) - Generate HTML or XML in a pythonic way. Pure python alternative to web template engines.Can fill HTML forms with default values and error messages.
- [ocp-gordon](scientific-engineering-mathematics.md#ocp-gordon) - A Python library for Gordon Surface interpolation using B-splines.
- [auditwheel](software-development.md#auditwheel) - Cross-distribution Linux wheels
- [nvidia-cuda-nvrtc-cu11](scientific-engineering.md#nvidia-cuda-nvrtc-cu11) - NVRTC native runtime libraries
- [databento](office-business-financial.md#databento) - Official Python client library for Databento
- [types-confluent-kafka](software-development.md#types-confluent-kafka) - Types for Confluent Kafka
- [autocommand](software-development.md#autocommand) - A library to create a command-line program from a function
- [fredapi](internet-www-http.md#fredapi) - Python API for Federal Reserve Economic Data (FRED) from St. Louis Fed
- [upstash-redis](database.md#upstash-redis) - Serverless Redis SDK from Upstash
- [pylibjpeg-libjpeg](scientific-engineering-medical-science-apps.md#pylibjpeg-libjpeg) - A Python wrapper for libjpeg, with a focus on use as a plugin for for pylibjpeg
- [requests-oauth](internet-www-http.md#requests-oauth) - Hook for adding Open Authentication support to Python-requests HTTP library.
- [prisma](database-database-engines-servers.md#prisma) - Prisma Client Python is an auto-generated and fully type-safe database client
- [ocspresponder](security.md#ocspresponder) - RFC 6960 compliant OCSP Responder framework written in Python 3.5+.
- [pyomo](scientific-engineering-mathematics.md#pyomo) - The Pyomo optimization modeling framework
- [gspread-formatting](office-business-financial.md#gspread-formatting) - Complete Google Sheets formatting support for gspread worksheets
- [asynciolimiter](internet.md#asynciolimiter) - Rate limiter for Async IO
- [scrapling](internet-www-http.md#scrapling) - Scrapling is an undetectable, powerful, flexible, high-performance Python framework that makes Web Scraping easy and effortless as it should be!
- [mysql-connector](database.md#mysql-connector) - MySQL driver written in Python
- [camoufox](internet-www-http.md#camoufox) - Wrapper around Playwright to help launch Camoufox
- [IPy](communications.md#ipy) - Class and tools for handling of IPv4 and IPv6 addresses and networks
- [token-bucket](internet-www-http.md#token-bucket) - Very fast implementation of the token bucket algorithm.
- [tensorflow-hub](scientific-engineering.md#tensorflow-hub) - TensorFlow Hub is a library to foster the publication, discovery, and consumption of reusable parts of machine learning models.
- [Flask-Bcrypt](internet-www-http.md#flask-bcrypt) - Brcrypt hashing for Flask.
- [psd-tools](multimedia-graphics.md#psd-tools) - Python package for working with Adobe Photoshop PSD files
- [pyviz-comms](scientific-engineering.md#pyviz-comms) - A JupyterLab extension for rendering HoloViz content.
- [starlette-compress](internet-www-http.md#starlette-compress) - Compression middleware for Starlette - supporting ZStd, Brotli, and GZip
- [django-tables2](internet-www-http.md#django-tables2) - Table/data-grid framework for Django
- [shyaml](software-development.md#shyaml) - YAML for command line
- [pyjpegls](file-formats.md#pyjpegls) - JPEG-LS for Python via CharLS C++ Library
- [PyVISA](scientific-engineering-interface-engine-protocol-translator.md#pyvisa) - Python VISA bindings for GPIB, RS232, TCPIP and USB instruments
- [paddlex](scientific-engineering.md#paddlex) - Low-code development tool based on PaddlePaddle.
- [tensorflow-addons](scientific-engineering-mathematics.md#tensorflow-addons) - TensorFlow Addons.
- [collections-extended](software-development.md#collections-extended) - Extra Python Collections - bags (multisets) and setlists (ordered sets)
- [pyftpdlib](internet-file-transfer-protocol-ftp.md#pyftpdlib) - Very fast asynchronous FTP server library
- [aqtinstall](software-development.md#aqtinstall) - Another unofficial Qt installer
- [traceback-with-variables](software-development-debuggers.md#traceback-with-variables) - Adds variables to python traceback. Simple, lightweight, controllable. Debug reasons of exceptions by logging or pretty printing colorful variable contexts for each frame in a stacktrace, showing every value. Dump locals environments after errors to console, files, and loggers. Works with Jupyter and IPython.
- [django-guardian](security.md#django-guardian) - Per object permissions for Django
- [stanza](scientific-engineering.md#stanza) - A Python NLP Library for Many Human Languages, by the Stanford NLP Group
- [neptune-api](scientific-engineering-artificial-intelligence.md#neptune-api) - A client library for accessing Neptune API
- [simpleitk](scientific-engineering.md#simpleitk) - SimpleITK is a simplified interface to the Insight Toolkit (ITK) for image registration and segmentation
- [proxy.py](internet.md#proxypy) - \u26a1 Fast \u2022 \U0001fab6 Lightweight \u2022 \U0001f51f Dependency \u2022 \U0001f50c Pluggable \u2022 \U0001f608 TLS interception \u2022 \U0001f512 DNS-over-HTTPS \u2022 \U0001f525 Poor Mans VPN \u2022 \u23ea Reverse & \u23e9 Forward \u2022 \U0001f46e\U0001f3ff Proxy Server framework \u2022 \U0001f310 Web Server framework \u2022 \u27b5 \u27b6 \u27b7 \u27a0 PubSub framework \u2022 \U0001f477 Work acceptor & executor framework.
- [neptune-fetcher](scientific-engineering-artificial-intelligence.md#neptune-fetcher) - Neptune Fetcher (DEPRECATED - use neptune-query instead)
- [countryinfo](scientific-engineering-gis.md#countryinfo) - A Python module for returning data about countries, ISO info, and states/provinces within them.
- [pyqtgraph](scientific-engineering-visualization.md#pyqtgraph) - Scientific Graphics and GUI Library for Python
- [tensorflow-probability](scientific-engineering.md#tensorflow-probability) - Probabilistic modeling and statistical inference in TensorFlow
- [htmltools](internet-www-http.md#htmltools) - Tools for HTML generation and output.
- [libpass](security-cryptography.md#libpass) - Fork of passlib, a comprehensive password hashing framework supporting over 30 schemes
- [crispy-bootstrap5](internet-www-http.md#crispy-bootstrap5) - Bootstrap5 template pack for django-crispy-forms
- [rioxarray](scientific-engineering-gis.md#rioxarray) - geospatial xarray extension powered by rasterio
- [python-memcached](internet.md#python-memcached) - Pure python memcached client
- [sigfig](education.md#sigfig) - Python library for rounding numbers (with expected results)
- [nccl-extensions](scientific-engineering.md#nccl-extensions) - Python bindings for the nccl-extensions communication libraries (nccl_ep, nccl_m2n)
- [fastapi-utils](internet.md#fastapi-utils) - Reusable utilities for FastAPI
- [plantuml-markdown](software-development-documentation.md#plantuml-markdown) - A PlantUML plugin for Markdown
- [emails](communications.md#emails) - Modern python library for emails.
- [pylibjpeg-rle](scientific-engineering-medical-science-apps.md#pylibjpeg-rle) - Python bindings for a fast RLE decoder/encoder, with a focus on use as a plugin for pylibjpeg
- [prime-traces](scientific-engineering-artificial-intelligence.md#prime-traces) - Prime Intellect Traces SDK - Upload, query and export traces
- [django-rq](internet.md#django-rq) - An app that provides django integration for RQ (Redis Queue)
- [flyteidl](scientific-engineering.md#flyteidl) - IDL for Flyte Platform
- [prime-runs](scientific-engineering-artificial-intelligence.md#prime-runs) - Prime Intellect Runs SDK - Track eval and training runs on the Prime platform
- [nvidia-mathdx](scientific-engineering.md#nvidia-mathdx) - MathDx Device libraries
- [authres](communications-email.md#authres) - authres - Authentication Results Header Module
- [pysmi](communications.md#pysmi) - A pure-Python implementation of SNMP/SMI MIB parsing and conversion library.
- [fnvhash](internet.md#fnvhash) - Pure Python FNV hash implementation.
- [logfire-sdk](internet.md#logfire-sdk) - The best Python observability tool! 🪵🔥
- [cel-expr-python](software-development-interpreters.md#cel-expr-python) - The CEL Python runtime
- [coacd](education.md#coacd) - Approximate Convex Decomposition for 3D Meshes with Collision-Aware Concavity and Tree Search
- [sentencex](software-development.md#sentencex) - Sentence segmenter that supports ~300 languages
- [optuna-integration](scientific-engineering.md#optuna-integration) - Integration libraries of Optuna.
- [Paste](internet-www-http.md#paste) - Tools for using a Web Server Gateway Interface stack
- [sec-api](office-business-financial.md#sec-api) - SEC EDGAR Filings API
- [jpholiday](other-nonlisted-topic.md#jpholiday) - Pure-Python Japan Public Holiday Generate
- [weave](database-front-ends.md#weave) - A toolkit for building composable interactive data driven applications.
- [holoviews](scientific-engineering.md#holoviews) - A high-level plotting API for the PyData ecosystem built on HoloViews.
- [pymatgen](scientific-engineering-chemistry.md#pymatgen) - Python Materials Genomics is a robust materials analysis code that defines core object representations for structures and molecules with support for many electronic structure codes. It is currently the core analysis code powering the Materials Project (https://materialsproject.org).
- [music21](artistic-software.md#music21) - A Toolkit for Computer-Aided Musical Analysis and Computational Musicology.
- [python-logging-loki](internet-www-http.md#python-logging-loki) - Python logging handler for Grafana Loki.
- [pwntools](security.md#pwntools) - Pwntools CTF framework and exploit development library.
- [draftjs_exporter](internet-www-http.md#draftjs_exporter) - Library to convert rich text from Draft.js raw ContentState to HTML
- [indic-numtowords](scientific-engineering-artificial-intelligence.md#indic-numtowords) - A module to convert numbers to words for Indian languages and English.
- [scrapy-stealth](internet-www-http.md#scrapy-stealth) - Stealthy Crawling. Maximum Results. A pluggable anti-bot and stealth framework for Scrapy.
- [panel-material-ui](scientific-engineering.md#panel-material-ui) - An extension to bring MaterialUI components to Panel.
- [python-fsutil](desktop-environment-file-managers.md#python-fsutil) - high-level file-system operations for lazy devs.
- [frida](software-development-debuggers.md#frida) - Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers
- [spark-nlp](scientific-engineering.md#spark-nlp) - John Snow Labs Spark NLP is a natural language processing library built on top of Apache Spark ML. It provides simple, performant & accurate NLP annotations for machine learning pipelines, that scale easily in a distributed environment.
- [PyVISA-py](scientific-engineering-interface-engine-protocol-translator.md#pyvisa-py) - Pure Python implementation of a VISA library.
- [jsonasobj](internet.md#jsonasobj) - JSON as python objects
- [descript-audiotools](artistic-software.md#descript-audiotools) - Utilities for handling audio.
- [pyactiveresource](software-development.md#pyactiveresource) - ActiveResource for Python
- [bedrock-agentcore-starter-toolkit](scientific-engineering-artificial-intelligence.md#bedrock-agentcore-starter-toolkit) - A starter toolkit for using Bedrock AgentCore
- [purgatory](internet-www-http.md#purgatory) - A circuit breaker implementation for asyncio
- [firecrawl](internet.md#firecrawl) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [tensorboard-plugin-profile](scientific-engineering-mathematics.md#tensorboard-plugin-profile) - XProf Profiler Plugin
- [pygame-ce](games-entertainment.md#pygame-ce) - Python Game Development
- [nvidia-cusparse-cu11](scientific-engineering.md#nvidia-cusparse-cu11) - CUSPARSE native runtime libraries
- [xmljson](software-development.md#xmljson) - Converts XML into JSON/Python dicts/arrays and vice-versa.
- [nvidia-cufft-cu11](scientific-engineering.md#nvidia-cufft-cu11) - CUFFT native runtime libraries
- [ShopifyAPI](software-development.md#shopifyapi) - Shopify API for Python
- [nvidia-cusolver-cu11](scientific-engineering.md#nvidia-cusolver-cu11) - CUDA solver native runtime libraries
- [unitycatalog-client](scientific-engineering.md#unitycatalog-client) - Official Python SDK for Unity Catalog
- [SQLAlchemy-Continuum](internet-www-http.md#sqlalchemy-continuum) - Versioning and auditing extension for SQLAlchemy.
- [empy](software-development-interpreters.md#empy) - A templating system for Python.
- [aspose-words](office-business.md#aspose-words) - Aspose.Words for Python is a Document Processing library that allows developers to work with documents in many popular formats without needing Office Automation.
- [nvidia-curand-cu11](scientific-engineering.md#nvidia-curand-cu11) - CURAND native runtime libraries
- [cpsat-logutils](scientific-engineering-mathematics.md#cpsat-logutils) - Parse CP-SAT (OR-Tools) solver logs into line-anchored, JSON-serializable pydantic models.
- [caldav](office-business-scheduling.md#caldav) - CalDAV (RFC4791) client library
- [orloge](software-development.md#orloge) - OR log extractor
- [airbyte-cdk](scientific-engineering.md#airbyte-cdk) - A framework for writing Airbyte Connectors.
- [pysqlite3-binary](database-database-engines-servers.md#pysqlite3-binary) - DB-API 2.0 interface for Sqlite 3.x
- [django-autocomplete-light](internet-www-http.md#django-autocomplete-light) - Fresh autocompletes for Django
- [python-logstash](internet-www-http.md#python-logstash) - Python logging handler for Logstash.
- [nvidia-cuda-cupti-cu11](scientific-engineering.md#nvidia-cuda-cupti-cu11) - CUDA profiling tools runtime libs.
- [extension-helpers](software-development-build-tools.md#extension-helpers) - Utilities for building and installing packages with compiled extensions
- [kaldialign](scientific-engineering-artificial-intelligence.md#kaldialign) - Kaldi alignment methods wrapped into Python
- [xprof](scientific-engineering-mathematics.md#xprof) - XProf Profiler Plugin
- [nvidia-nvtx-cu11](scientific-engineering.md#nvidia-nvtx-cu11) - NVIDIA Tools Extension
- [hexdump](software-development.md#hexdump) - dump binary data to hex format and restore from there
- [Flask-Testing](internet-www-http.md#flask-testing) - Unit testing for Flask
- [nvidia-nccl-cu11](scientific-engineering.md#nvidia-nccl-cu11) - NVIDIA Collective Communication Library (NCCL) Runtime
- [demjson3](internet-www-http.md#demjson3) - encoder, decoder, and lint/validator for JSON (JavaScript Object Notation) compliant with RFC 7159
- [rawpy](multimedia-graphics.md#rawpy) - RAW image processing for Python, a wrapper for libraw
- [pdbp](scientific-engineering.md#pdbp) - pdbp (Pdb+): A drop-in replacement for pdb and pdbpp.
- [Flask-OpenID](internet-www-http.md#flask-openid) - OpenID support for Flask
- [pyoxigraph](database-database-engines-servers.md#pyoxigraph) - Python bindings of Oxigraph, a SPARQL database and RDF toolkit
- [llama-index-legacy](scientific-engineering-artificial-intelligence.md#llama-index-legacy) - Interface between LLMs and your data
- [tabcompleter](scientific-engineering.md#tabcompleter) - tabcompleter --- Autocompletion in the Python console.
- [hl7](communications.md#hl7) - Python library parsing HL7 v2.x messages
- [wandb-workspaces](scientific-engineering-artificial-intelligence.md#wandb-workspaces) - A library for programatically working with the Weights & Biases UI.
- [feu](scientific-engineering.md#feu) - A lightweight Python library for managing packages and versions across different Python environments
- [sqlean.py](database-database-engines-servers.md#sqleanpy) - sqlite3 with extensions
- [tls-client](internet-www-http.md#tls-client) - Advanced Python HTTP Client.
- [simplekml](scientific-engineering-gis.md#simplekml) - A Simple KML creator
- [ipaddr](internet.md#ipaddr) - Google's IP address manipulation library
- [pymatgen-io-validation](scientific-engineering.md#pymatgen-io-validation) - A comprehensive I/O validator for electronic structure calculations
- [praat-parselmouth](scientific-engineering.md#praat-parselmouth) - Praat in Python, the Pythonic way
- [hass-nabucasa](internet-proxy-servers.md#hass-nabucasa) - Home Assistant cloud integration by Nabu Casa, Inc.
- [ibm-watsonx-ai](internet.md#ibm-watsonx-ai) - IBM watsonx.ai API Client
- [great-tables](internet-www-http.md#great-tables) - Easily generate information-rich, publication-quality tables from Python.
- [Flask-Bootstrap](internet-www-http.md#flask-bootstrap) - An extension that includes Bootstrap in your project, without any boilerplate code.
- [pyserial-asyncio](communications.md#pyserial-asyncio) - Python Serial Port Extension - Asynchronous I/O support
- [django-q2](internet-www-http.md#django-q2) - A multiprocessing distributed task queue for Django
- [pony](database.md#pony) - Pony Object-Relational Mapper
- [google-cloud-pipeline-components](scientific-engineering.md#google-cloud-pipeline-components) - This SDK enables a set of First Party (Google owned) pipeline components that allow users to take their experience from Vertex AI SDK and other Google Cloud services and create a corresponding pipeline using KFP or Managed Pipelines.
- [mpi4py](scientific-engineering.md#mpi4py) - Python bindings for MPI
- [seekpath](scientific-engineering-chemistry.md#seekpath) - A module to obtain and visualize k-vector coefficients and obtain band paths in the Brillouin zone of crystal structures
- [PyRIC](security.md#pyric) - Python Wireless Library
- [flytekit](scientific-engineering.md#flytekit) - Flyte SDK for Python
- [arize](scientific-engineering-artificial-intelligence.md#arize) - A helper library to interact with Arize AI APIs
- [snitun](internet-proxy-servers.md#snitun) - SNI proxy with TCP multiplexer
- [codetiming](education.md#codetiming) - A flexible, customizable timer for your Python code.
- [pygraphviz](scientific-engineering-information-analysis.md#pygraphviz) - Python interface to Graphviz
- [cityhash](scientific-engineering-information-analysis.md#cityhash) - Python bindings for CityHash and FarmHash
- [monai](scientific-engineering.md#monai) - AI Toolkit for Healthcare Imaging
- [tortoise-orm](database.md#tortoise-orm) - Easy async ORM for python, built with relations in mind
- [nicknames](scientific-engineering-information-analysis.md#nicknames) - Hand-curated dataset of English names and nicknames.
- [unitycatalog-ai](scientific-engineering.md#unitycatalog-ai) - Official Python library for Unity Catalog AI support
- [pymorphy3-dicts-ru](scientific-engineering-information-analysis.md#pymorphy3-dicts-ru) - Russian dictionaries for pymorphy2
- [pymorphy3](scientific-engineering-information-analysis.md#pymorphy3) - Morphological analyzer (POS tagger + inflection engine) for Russian language.
- [nautilus-trader](office-business-financial.md#nautilus-trader) - Production-grade Rust-native trading engine with deterministic event-driven architecture
- [CherryPy](internet-www-http.md#cherrypy) - Object-Oriented HTTP framework
- [dj-stripe](office-business-financial.md#dj-stripe) - Django + Stripe made easy
- [django-mathfilters](internet-www-http.md#django-mathfilters) - A set of simple math filters for Django
- [tool](internet-www-http.md#tool) - A compact modular conf/web/console framework.
- [fastapi-azure-auth](software-development.md#fastapi-azure-auth) - Easy and secure implementation of Azure Entra ID for your FastAPI APIs
- [django-admin-autocomplete-filter](internet-www-http.md#django-admin-autocomplete-filter) - A simple Django app to render list filters in django admin using autocomplete widget
- [cacheout](database.md#cacheout) - A caching library for Python
- [dash-cytoscape](database-front-ends.md#dash-cytoscape) - A Component Library for Dash aimed at facilitating network visualization in Python, wrapped around Cytoscape.js
- [django-test-migrations](internet-www-http.md#django-test-migrations) - Test django schema and data migrations, including ordering
- [earthengine-api](multimedia-graphics.md#earthengine-api) - Earth Engine Python API
- [pystac-client](scientific-engineering-gis.md#pystac-client) - Python library for searching SpatioTemporal Asset Catalog (STAC) APIs.
- [pgqueuer](database.md#pgqueuer) - PostgreSQL-backed background job and task queue for Python.
- [gmpy2](scientific-engineering-mathematics.md#gmpy2) - gmpy2 interface to GMP, MPFR, and MPC for Python
- [djangosaml2](internet-www-http.md#djangosaml2) - pysaml2 integration for Django
- [DAWG2-Python](scientific-engineering-information-analysis.md#dawg2-python) - Pure-python reader for DAWGs (DAFSAs) created by dawgdic C++ library or DAWG Python extension.
- [python-igraph](scientific-engineering.md#python-igraph) - High performance graph data structures and algorithms (legacy package)
- [sbvirtualdisplay](internet.md#sbvirtualdisplay) - A customized pyvirtualdisplay for SeleniumBase.
- [hatchling-autoextras-hook](scientific-engineering.md#hatchling-autoextras-hook) - Hatchling metadata hook to generate all extras
- [munkres](scientific-engineering-mathematics.md#munkres) - The Munkres (Hungarian) algorithm for the assignment problem: fast, typed, dependency-free.
- [python-mimeparse](internet-www-http.md#python-mimeparse) - A module provides basic functions for parsing mime-type names and matching them against a list of media-ranges.
- [apeye](internet-www-http.md#apeye) - Handy tools for working with URLs and APIs.
- [fiddle](scientific-engineering.md#fiddle) - Fiddle: A Python-first configuration library
- [UnityPy](games-entertainment.md#unitypy) - A Unity extraction and patching package
- [traits](scientific-engineering.md#traits) - Observable typed attributes for Python classes
- [mycdp](internet.md#mycdp) - Autogenerated CDP utilities for Python
- [pymatgen-core](scientific-engineering-chemistry.md#pymatgen-core) - Python Materials Genomics is a robust materials analysis code that defines core object representations for structures and molecules with support for many electronic structure codes. It is currently the core analysis code powering the Materials Project (https://materialsproject.org). This repository is for pymatgen-core, which implements the core data structures and algorithms.
- [chainlit](communications-chat.md#chainlit) - Build Conversational AI.
- [urwid-readline](desktop-environment.md#urwid-readline) - A textbox edit widget for urwid that supports readline shortcuts
- [docx2pdf](office-business-office-suites.md#docx2pdf) - Convert docx to pdf on Windows or macOS directly using Microsoft Word (must be installed).
- [descript-audio-codec](artistic-software.md#descript-audio-codec) - A high-quality general neural audio codec.
- [pytorch-tokenizers](scientific-engineering.md#pytorch-tokenizers) - A package with common tokenizers in Python and C++
- [PyLD](internet.md#pyld) - Python implementation of the JSON-LD API
- [gcs-oauth2-boto-plugin](internet-www-http.md#gcs-oauth2-boto-plugin) - Auth plugin allowing use the use of OAuth 2.0 credentials for Google Cloud Storage in the Boto library.
- [deal](software-development.md#deal) - **Deal** is a Python library for [design by contract][wiki] (DbC) programming.
- [cloakbrowser](internet-www-http.md#cloakbrowser) - Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches.
- [aiosonic](internet-www-http.md#aiosonic) - Async HTTP/WebSocket client
- [mock-open](software-development.md#mock-open) - A better mock for file I/O
- [flask-oidc](internet-www-http.md#flask-oidc) - OpenID Connect extension for Flask
- [serpapi](internet-www-http.md#serpapi) - The official Python client for SerpApi.com.
- [coralogix-logger](internet-log-analysis.md#coralogix-logger) - Coralogix Python SDK
- [python-markdown-math](scientific-engineering-mathematics.md#python-markdown-math) - Math extension for Python-Markdown
- [runloop_api_client](scientific-engineering-artificial-intelligence.md#runloop_api_client) - Official Python SDK for Runloop — secure Linux sandboxes (Devboxes) where AI agents run code, edit files, and expose ports
- [django-split-settings](internet-www-http.md#django-split-settings) - Organize Django settings into multiple files and directories. Easily override and modify settings. Use wildcards and optional settings files.
- [django-user-agents](internet-www-http.md#django-user-agents) - A django package that allows easy identification of visitors' browser, operating system and device information (mobile phone, tablet or has touch capabilities).
- [TgCrypto](communications.md#tgcrypto) - Fast and Portable Cryptography Extension Library for Pyrogram
- [headroom-ai](scientific-engineering-artificial-intelligence.md#headroom-ai) - Compress tool outputs, logs, JSON and chat history before each LLM call. Fewer input tokens, same answers; in-process, no API key. Library, proxy and MCP server.
- [authy](security.md#authy) - Authy API Client
- [transaction](database.md#transaction) - Transaction management for Python
- [stirrup](scientific-engineering-artificial-intelligence.md#stirrup) - The lightweight foundation for building agents
- [selenium-stealth](internet.md#selenium-stealth) - Trying to make python selenium more stealthy.
- [nemo-toolkit](scientific-engineering.md#nemo-toolkit) - NeMo - a toolkit for Conversational AI
- [python-backoff](internet-www-http.md#python-backoff) - Function decoration for backoff and retry
- [pydotplus](scientific-engineering-visualization.md#pydotplus) - Python interface to Graphviz's Dot language
- [texture2ddecoder](multimedia-graphics.md#texture2ddecoder) - a python wrapper for Perfare's Texture2DDecoder
- [nvidia-cuda-tileiras](scientific-engineering.md#nvidia-cuda-tileiras) - TileIR Assembler Package
- [verboselogs](software-development.md#verboselogs) - Verbose logging level for Python's logging module
- [2captcha-python](scientific-engineering-image-recognition.md#2captcha-python) - Python module for easy integration with 2Captcha API
- [ftputil](internet-file-transfer-protocol-ftp.md#ftputil) - High-level FTP client library (virtual file system and more)
- [stream-chat](software-development.md#stream-chat) - Client for Stream Chat.
- [twofish](security-cryptography.md#twofish) - Bindings for the Twofish implementation by Niels Ferguson
- [tfp-nightly](scientific-engineering.md#tfp-nightly) - Probabilistic modeling and statistical inference in TensorFlow
- [authheaders](communications-email.md#authheaders) - A library wrapping email authentication header verification and generation.
- [megatron-core](scientific-engineering.md#megatron-core) - Megatron Core - a library for efficient and scalable training of transformer based models
- [Routes](internet-www-http.md#routes) - Routing Recognition and Generation Tools
- [flufl.bounce](communications-email.md#fluflbounce) - Email bounce detectors
- [pymupdfpro](multimedia-graphics.md#pymupdfpro) - Commercial extensions for PyMuPDF; enables Office document handling, including doc, docx, hwp, hwpx, ppt, pptx, xls, xls, and others. Supports text and table extraction, document conversion and more.
- [ai-edge-litert](scientific-engineering.md#ai-edge-litert) - LiteRT is for mobile and embedded devices.
- [frida-tools](software-development-debuggers.md#frida-tools) - Frida CLI tools
- [httpr](internet-www-http.md#httpr) - Fast HTTP client for Python
- [etcpak](multimedia-graphics.md#etcpak) - python wrapper for etcpak
- [textsearch](software-development.md#textsearch) - Find strings/words in text; convenience and C speed
- [astc-encoder-py](multimedia-graphics.md#astc-encoder-py) - a python wrapper for astc-encoder
- [Flask-BasicAuth](internet-www-http.md#flask-basicauth) - HTTP basic access authentication for Flask.
- [gin-config](scientific-engineering.md#gin-config) - Gin-Config: A lightweight configuration library for Python
- [Flask-Pydantic](internet-www-http.md#flask-pydantic) - Flask extension for integration with Pydantic library.
- [spider-client](internet.md#spider-client) - Python SDK for Spider Cloud API
- [nvidia-cuda-cccl-cu12](scientific-engineering.md#nvidia-cuda-cccl-cu12) - CUDA CCCL
- [veracode-api-signing](internet-www-http.md#veracode-api-signing) - Easily sign any request destined for the Veracode API Gateway
- [planarity](scientific-engineering.md#planarity) - Python Wrapper for the Edge Addition Planarity Suite and Graph Library
- [django-ninja-extra](internet.md#django-ninja-extra) - Django Ninja Extra - Class Based Utility and more for Django Ninja(Fast Django REST framework)
- [sqlcipher3](database.md#sqlcipher3) - DB-API 2.0 interface for SQLCipher 4.x
- [coola](scientific-engineering.md#coola) - Library to check equality between two complex/nested objects
- [couchbase](database.md#couchbase) - Python Client for Couchbase
- [airbyte-protocol-models-dataclasses](scientific-engineering.md#airbyte-protocol-models-dataclasses) - Declares the Airbyte Protocol using Python Dataclasses. Dataclasses in Python have less performance overhead compared to Pydantic models, making them a more efficient choice for scenarios where speed and memory usage are critical
- [contractions](software-development.md#contractions) - Fixes contractions such as `you're` to you `are`
- [quart-cors](internet-www-http.md#quart-cors) - A Quart extension to provide Cross Origin Resource Sharing, access control, support
- [plantuml](internet-www-http.md#plantuml) - 
- [fmod-toolkit](games-entertainment.md#fmod-toolkit) - 
- [django-jazzmin](internet-www-http.md#django-jazzmin) - Drop-in theme for django admin, that utilises AdminLTE 3 & Bootstrap 5 to make yo' admin look jazzy
- [datashader](scientific-engineering.md#datashader) - Data visualization toolchain based on aggregating into a grid
- [py-cord](internet.md#py-cord) - A Python wrapper for the Discord API
- [littlefs-python](scientific-engineering.md#littlefs-python) - A python wrapper for littlefs
- [aioimaplib](communications-email.md#aioimaplib) - Python asyncio IMAP4rev1 client library
- [flake8-bandit](security.md#flake8-bandit) - Automated security testing with bandit and flake8.
- [cognitive-complexity](software-development-documentation.md#cognitive-complexity) - Library to calculate Python functions cognitive complexity via code
- [delocate](software-development-build-tools.md#delocate) - Move macOS dynamic libraries into package
- [pysnmpcrypto](communications.md#pysnmpcrypto) - Strong cryptography support for PySNMP (SNMP library for Python)
- [django-auth-ldap](internet-www-http.md#django-auth-ldap) - Django LDAP authentication backend
- [crispy-bootstrap4](internet-www-http.md#crispy-bootstrap4) - Bootstrap4 template pack for django-crispy-forms
- [plyvel](database.md#plyvel) - Plyvel, a fast and feature-rich Python interface to LevelDB
- [lapx](education.md#lapx) - Linear assignment problem solvers, including single and batch solvers.
- [tombi](software-development-build-tools.md#tombi) - 🦅 TOML Toolkit 🦅
- [stem](security.md#stem) - Stem is a Python controller library that allows applications to interact with Tor (https://www.torproject.org/).
- [Pyrogram](communications.md#pyrogram) - Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots
- [postgres](database-front-ends.md#postgres) - postgres is a high-value abstraction over psycopg2.
- [pynetdicom](scientific-engineering-medical-science-apps.md#pynetdicom) - A Python implementation of the DICOM networking protocol
- [effdet](scientific-engineering.md#effdet) - EfficientDet for PyTorch
- [hvplot](scientific-engineering.md#hvplot) - A high-level plotting API for the PyData ecosystem built on HoloViews.
- [typer-config](software-development.md#typer-config) - Utilities for working with configuration files in typer CLIs.
- [phidget22](scientific-engineering.md#phidget22) - Phidget22 Python Library
- [queries](database.md#queries) - Simplified PostgreSQL client built upon Psycopg2
- [flufl.i18n](software-development-internationalization.md#flufli18n) - A high level API for internationalizing Python libraries and applications
- [clickhouse-cityhash](internet.md#clickhouse-cityhash) - Python-bindings for CityHash, a fast non-cryptographic hash algorithm
- [cli-helpers](software-development.md#cli-helpers) - Helpers for building command-line apps
- [mrcfile](scientific-engineering-bio-informatics.md#mrcfile) - MRC file I/O library
- [pyTenable](software-development.md#pytenable) - Python library to interface into Tenable's products and applications
- [sphinx-toolbox](documentation.md#sphinx-toolbox) - Box of handy tools for Sphinx 🧰 📔
- [segtok](scientific-engineering-information-analysis.md#segtok) - sentence segmentation and word tokenization tools
- [tika](database-front-ends.md#tika) - Apache Tika Python library
- [pyx12](office-business.md#pyx12) - HIPAA X12 validator, parser and converter
- [pywikibot](internet-www-http.md#pywikibot) - Python MediaWiki Bot Framework
- [licensecheck](security.md#licensecheck) - Output the licenses used by dependencies and check if these are compatible with the project license
- [sqlalchemy-hana](database.md#sqlalchemy-hana) - SQLAlchemy dialect for SAP HANA
- [wiremock](internet-www-http.md#wiremock) - Wiremock Admin API Client
- [qstash](database.md#qstash) - Python SDK for Upstash QStash
- [pytools](scientific-engineering.md#pytools) - A collection of tools for Python
- [sqlalchemy-cloudflare-d1](database.md#sqlalchemy-cloudflare-d1) - A SQLAlchemy dialect for Cloudflare's D1 Serverless SQLite Database
- [common-expression-language](software-development-interpreters.md#common-expression-language) - Python bindings for the Common Expression Language (CEL)
- [django-crum](internet-www-http.md#django-crum) - Django middleware to capture current request and user.
- [arize-otel](scientific-engineering-artificial-intelligence.md#arize-otel) - OpenTelemetry tracing helpers for Arize
- [Flask-Principal](internet-www-http.md#flask-principal) - Identity management for flask
- [pook](software-development.md#pook) - HTTP traffic mocking and expectations made easy
- [flyteidl2](scientific-engineering.md#flyteidl2) - IDL for Flyte
- [libipld](software-development.md#libipld) - Python binding to the Rust IPLD library
- [pixeltable-pgserver](database.md#pixeltable-pgserver) - Embedded Postgres Server for Pixeltable
- [pysqlite3](database.md#pysqlite3) - DB-API 2.0 interface for Sqlite 3.x
- [pyglove](scientific-engineering-artificial-intelligence.md#pyglove) - PyGlove: A library for manipulating Python objects.
- [quantstats](office-business-financial.md#quantstats) - Portfolio analytics for quants
- [funasr](multimedia-sound-audio.md#funasr) - OpenAI-compatible speech recognition toolkit with WebSocket streaming, vLLM acceleration, and llama.cpp/GGUF edge runtime.
- [pylogbeat](internet-www-http.md#pylogbeat) - Simple, incomplete implementation of the Beats protocol used by Elastic Beats and Logstash.
- [pbixray](scientific-engineering-information-analysis.md#pbixray) - A Python library to parse and analyze PBIX files used with Microsoft Power BI and Excel PowerPivot.
- [validator-collection](internet-www-http.md#validator-collection) - Collection of 60+ Python functions for validating data
- [simplification](scientific-engineering-gis.md#simplification) - Fast linestring simplification using RDP or Visvalingam-Whyatt
- [eralchemy](database.md#eralchemy) - Simple entity relation (ER) diagrams generation
- [AMQPStorm](communications.md#amqpstorm) - Thread-safe Python3 RabbitMQ Client & Management library.
- [jmp](scientific-engineering-mathematics.md#jmp) - JMP is a Mixed Precision library for JAX.
- [RESTFly](internet-www-http.md#restfly) - Write your own API Client libraries quickly.
- [lhotse](multimedia-sound-audio.md#lhotse) - Data preparation for speech processing models training.
- [xdis](software-development-debuggers.md#xdis) - Python cross-version byte-code disassembler and marshal routines
- [ics](office-business-scheduling.md#ics) - Python icalendar (rfc5545) parser
- [ha-mcp](home-automation.md#ha-mcp) - Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants.
- [pyspf](communications-email.md#pyspf) - SPF (Sender Policy Framework) implemented in Python.
- [supertokens-python](internet-www-http.md#supertokens-python) - SuperTokens SDK for Python
- [numpy-rms](multimedia-sound-audio.md#numpy-rms) - A fast python library for calculating the RMS of a NumPy array
- [numpy-minmax](multimedia-sound-audio.md#numpy-minmax) - A fast python library for finding both min and max value in a NumPy array
- [check-wheel-contents](software-development-build-tools.md#check-wheel-contents) - Check your wheels have the right contents
- [django-celery-email](communications.md#django-celery-email) - An async Django email backend using celery
- [i18nice](software-development-internationalization.md#i18nice) - Translation library for Python
- [Flask-Script](internet-www-http.md#flask-script) - Scripting support for Flask
- [opuslib](multimedia-sound-audio.md#opuslib) - Python bindings to the libopus, IETF low-delay audio codec
- [plivo](communications-telephony.md#plivo) - A Python SDK to make voice calls & send SMS using Plivo and to generate Plivo XML
- [fpgen](internet-www-http.md#fpgen) - A fast & comprehensive browser fingerprint generator
- [zernio-sdk](internet-www-http.md#zernio-sdk) - The official Python library for the Zernio API
- [python-logstash-async](internet-www-http.md#python-logstash-async) - Asynchronous Python logging handler for Logstash.
- [pyvo](database.md#pyvo) - Astropy affiliated package for accessing Virtual Observatory data and services
- [rq-dashboard](internet.md#rq-dashboard) - rq-dashboard is a general purpose, lightweight, web interface to monitor your RQ queues, jobs, and workers in realtime.
- [pydantic-ai-todo](scientific-engineering-artificial-intelligence.md#pydantic-ai-todo) - Todo/task planning toolset for pydantic-ai agents
- [args](internet-www-http.md#args) - Command Arguments for Humans.
- [sec-edgar-downloader](office-business-financial.md#sec-edgar-downloader) - Download SEC filings from the EDGAR database using Python
- [PyGreSQL](database.md#pygresql) - Python PostgreSQL interfaces
- [py-trees](scientific-engineering-artificial-intelligence.md#py-trees) - pythonic implementation of behaviour trees
- [starlette-prometheus](internet-www-http.md#starlette-prometheus) - Prometheus integration for Starlette
- [MultiPyVu](scientific-engineering-chemistry.md#multipyvu) - Control MultiVu using Python
- [vicinity](scientific-engineering-artificial-intelligence.md#vicinity) - Lightweight Nearest Neighbors with Flexible Backends
- [saq](internet.md#saq) - Distributed Python job queue with asyncio and redis
- [scrapy-ingest](database.md#scrapy-ingest) - One pipeline. Full crawl observability in SQL or Elasticsearch.
- [django-revproxy](internet-proxy-servers.md#django-revproxy) - Yet another Django reverse proxy application
- [yellowbrick](scientific-engineering-visualization.md#yellowbrick) - A suite of visual analysis and diagnostic tools for machine learning.
- [atproto](software-development.md#atproto) - The AT Protocol SDK
- [pymunk](games-entertainment.md#pymunk) - Pymunk is a easy-to-use pythonic 2D physics library
- [imgaug](scientific-engineering-artificial-intelligence.md#imgaug) - Image augmentation library for deep neural networks
- [subagents-pydantic-ai](scientific-engineering-artificial-intelligence.md#subagents-pydantic-ai) - Subagent toolset for pydantic-ai with dual-mode execution and dynamic agent creation
- [pyglm](multimedia-graphics.md#pyglm) - OpenGL Mathematics library for Python
- [python-etcd](database-front-ends.md#python-etcd) - A python client for etcd
- [astroquery](database.md#astroquery) - Functions and classes to access online astronomical data resources
- [chalkpy](scientific-engineering-artificial-intelligence.md#chalkpy) - Python SDK for Chalk
- [energyquantified](office-business-financial.md#energyquantified) - Energy Quantified Time series API client.
- [tflite-runtime](scientific-engineering.md#tflite-runtime) - TensorFlow Lite is for mobile and embedded devices.
- [pycti](security.md#pycti) - Python API client for OpenCTI.
- [fastapi-debug-toolbar](internet.md#fastapi-debug-toolbar) - A debug toolbar for FastAPI.
- [yake](scientific-engineering-information-analysis.md#yake) - Keyword extraction Python package
- [pdfrw2](multimedia-graphics.md#pdfrw2) - PDF file reader/writer library
- [jraph](scientific-engineering-artificial-intelligence.md#jraph) - Jraph: A library for Graph Neural Networks in Jax
- [onnx-asr](multimedia-sound-audio.md#onnx-asr) - A lightweight Python package for Automatic Speech Recognition using ONNX models
- [pyteomics](education.md#pyteomics) - A framework for proteomics data analysis.
- [tb-nightly](scientific-engineering-mathematics.md#tb-nightly) - TensorBoard lets you watch Tensors Flow
- [delvewheel](software-development.md#delvewheel) - Self-contained wheels for Windows
- [Flask-Security-Too](internet-www-http.md#flask-security-too) - Quickly add security features to your Flask application.
- [stackone-defender](security.md#stackone-defender) - Indirect prompt injection defense for AI agents using tool calls
- [numpy-groupies](scientific-engineering.md#numpy-groupies) - Optimised tools for group-indexing operations: aggregated sum and more.
- [grequests](internet-www-http.md#grequests) - Requests + Gevent
- [PyOpenGL-accelerate](multimedia-graphics.md#pyopengl-accelerate) - Cython-coded accelerators for PyOpenGL
- [airbyte-protocol-models-pdv2](scientific-engineering.md#airbyte-protocol-models-pdv2) - Declares the Airbyte Protocol.
- [gseapy](scientific-engineering-bio-informatics.md#gseapy) - Gene Set Enrichment Analysis in Python
- [toml-fmt-common](internet.md#toml-fmt-common) - Common logic to the TOML formatter.
- [bitmath](communications-file-sharing.md#bitmath) - Pythonic module for representing and manipulating file sizes with different prefix notations (file size unit conversion)
- [scrapfly-sdk](internet.md#scrapfly-sdk) - Scrapfly SDK for Scrapfly
- [stream-python](software-development.md#stream-python) - Client for getstream.io. Build scalable newsfeeds & activity streams in a few hours instead of weeks.
- [pybloom-live](database-database-engines-servers.md#pybloom-live) - Bloom filter: A Probabilistic data structure
- [verlib2](software-development-build-tools.md#verlib2) - A standalone bundle of "distutils.version" and "packaging.version", without anything else.
- [doped](scientific-engineering-chemistry.md#doped) - Python package to setup, process and analyse solid-state defect calculations with VASP
- [M2Crypto](security-cryptography.md#m2crypto) - A Python crypto and SSL toolkit
- [neptune-query](scientific-engineering-artificial-intelligence.md#neptune-query) - Neptune Query is a Python library for retrieving data from Neptune.
- [cirq-core](scientific-engineering-quantum-computing.md#cirq-core) - A framework for creating, editing, and invoking Noisy Intermediate Scale Quantum (NISQ) circuits.
- [mcpforunityserver](games-entertainment.md#mcpforunityserver) - MCP for Unity Server: A Unity package for Unity Editor integration via the Model Context Protocol (MCP).
- [pypd](software-development.md#pypd) - A python client for PagerDuty API
- [pysubs2](multimedia-video.md#pysubs2) - A library for editing subtitle files
- [django-classy-tags](internet-www-http.md#django-classy-tags) - Class based template tags for Django
- [aiohomematic](home-automation.md#aiohomematic) - Async Python library for Homematic(IP) devices via OpenCCU, CCU3, CUxD and CCU-Jack.
- [pytubefix](internet.md#pytubefix) - Python3 library for downloading YouTube Videos.
- [grafana-api](internet.md#grafana-api) - Yet another Python library for Grafana API
- [aerich](database.md#aerich) - A database migrations tool for Tortoise ORM.
- [nflreadpy](scientific-engineering-information-analysis.md#nflreadpy) - A Python package for downloading NFL data from nflverse repositories
- [python-jobspy](internet-www-http.md#python-jobspy) - JobSpy: job scraper for LinkedIn, Indeed, Glassdoor, ZipRecruiter, Bayt, Naukri, BDJobs & HelloWork
- [nvidia-npp-cu12](scientific-engineering.md#nvidia-npp-cu12) - NPP native runtime libraries
- [workspace-mcp](communications-chat.md#workspace-mcp) - Comprehensive, highly performant Google Workspace Streamable HTTP & SSE MCP Server for Calendar, Gmail, Docs, Sheets, Slides & Drive
- [fatfs-ng](scientific-engineering.md#fatfs-ng) - Enhanced Python wrapper around ChaN's FatFS library - Fork of fatfs-python with extended features.
- [pyAgrum-nightly](scientific-engineering-artificial-intelligence.md#pyagrum-nightly) - Bayesian networks and other Probabilistic Graphical Models.
- [jsonrpcserver](internet.md#jsonrpcserver) - Process incoming JSON-RPC 2.0 requests in Python
- [tslearn](scientific-engineering-artificial-intelligence.md#tslearn) - A machine learning toolkit dedicated to time-series data
- [flake8-cognitive-complexity](software-development-documentation.md#flake8-cognitive-complexity) - An extension for flake8 that validates cognitive functions complexity
- [pykcs11](security-cryptography.md#pykcs11) - A Full PKCS#11 wrapper for Python
- [quotequail](communications-email.md#quotequail) - A library that identifies quoted text in plain text and HTML email messages.
- [jose](security.md#jose) - An implementation of the JOSE draft
- [django-graphql-jwt](internet.md#django-graphql-jwt) - JSON Web Token for Django GraphQL.
- [p4python](software-development.md#p4python) - P4Python - Python interface to Perforce API
- [Sanic-Cors](internet-www-http.md#sanic-cors) - A Sanic extension adding a decorator for CORS support. Based on flask-cors by Cory Dolphin.
- [envparse](internet-www-http.md#envparse) - Simple environment variable parsing
- [pynmeagps](scientific-engineering-gis.md#pynmeagps) - NMEA protocol parser and generator
- [fhconfparser](security.md#fhconfparser) - Provides a config language independent way to read a config file.
- [Cheetah3](internet-www-http.md#cheetah3) - Cheetah is a template engine and code generation tool
- [citeurl](internet-www-http.md#citeurl) - an extensible tool to process legal citations in text
- [snowflake-telemetry-python](database.md#snowflake-telemetry-python) - Snowflake Telemetry for Python
- [pyrealsense2](multimedia-video.md#pyrealsense2) - Python Wrapper for Realsense SDK 2.0.
- [cerbos](security.md#cerbos) - SDK for working with Cerbos: an open core, language-agnostic, scalable authorization solution
- [dj-email-url](internet-www-http.md#dj-email-url) - Use an URL to configure email backend settings in your Django Application.
- [mistralai-workflows](scientific-engineering-artificial-intelligence.md#mistralai-workflows) - Mistral Workflows - Build reliable AI workflows with Python
- [late-sdk](internet-www-http.md#late-sdk) - The official Python library for the Zernio API
- [django-fast-update](database.md#django-fast-update) - Faster db updates for Django using UPDATE FROM VALUES sql variants.
- [speechmatics-rt](multimedia-sound-audio.md#speechmatics-rt) - Speechmatics Real-Time API Client
- [python-docx-ml6](office-business-office-suites.md#python-docx-ml6) - Create, read, and update Microsoft Word .docx files. This is a fork from the original library that includes feature requests that have been provided by the open source community but have not yet been merged in the original package.
- [mxnet](scientific-engineering.md#mxnet) - Apache MXNet is an ultra-scalable deep learning framework. This version uses openblas and MKLDNN.
- [textX](software-development-compilers.md#textx) - Meta-language for DSL implementation inspired by Xtext
- [markdown-include](internet-www-http.md#markdown-include) - A Python-Markdown extension which provides an 'include' function
- [ezodf](office-business-office-suites.md#ezodf) - A Python package to create/manipulate OpenDocumentFormat files.
- [pgcli](database.md#pgcli) - CLI for Postgres Database. With auto-completion and syntax highlighting.
- [pysrt](multimedia-video.md#pysrt) - SubRip (.srt) subtitle parser and writer
- [semhash](scientific-engineering-artificial-intelligence.md#semhash) - Fast Multimodal Semantic Deduplication & Filtering
- [yagmail](communications-email.md#yagmail) - Yet Another GMAIL client
- [wsgidav](internet-www-http.md#wsgidav) - Generic and extendable WebDAV server based on WSGI
- [OpenImageIO](multimedia-graphics.md#openimageio) - Reading, writing, and processing images in a wide variety of file formats, using a format-agnostic API, aimed at VFX applications.
- [npmai-agents](office-business-scheduling.md#npmai-agents) - Production-grade autonomous AI agent framework with 1,371 tools across 100 classes and a 5-role LLM pipeline — built on the NPMAI ECOSYSTEM.
- [openccu-data](home-automation.md#openccu-data) - Extract and distribute Homematic CCU/OpenCCU configuration metadata (translations, easymodes, link profiles).
- [Flask-OAuthlib](internet-www-http.md#flask-oauthlib) - OAuthlib for Flask
- [django-sekizai](internet-www-http.md#django-sekizai) - Django Sekizai
- [agate-sql](scientific-engineering-information-analysis.md#agate-sql) - agate-sql adds SQL read/write support to agate.
- [agate-excel](scientific-engineering-information-analysis.md#agate-excel) - agate-excel adds read support for Excel files (xls and xlsx) to agate.
- [webexpythonsdk](communications.md#webexpythonsdk) - Work with the Webex APIs in native Python!
- [fastkml](scientific-engineering-gis.md#fastkml) - Fast KML processing in python
- [iapws](scientific-engineering.md#iapws) - Python implementation of standards from The InternationalAssociation for the Properties of Water and Steam
- [carelytics](scientific-engineering-information-analysis.md#carelytics) - A Python library for Healthcare Data Analytics and Revenue Cycle Management.
- [hachoir](multimedia.md#hachoir) - Package of Hachoir parsers used to open binary files
- [agate-dbf](scientific-engineering-information-analysis.md#agate-dbf) - agate-dbf adds read support for dbf files to agate.
- [rdata](file-formats.md#rdata) - Read R datasets from Python.
- [csvkit](scientific-engineering-information-analysis.md#csvkit) - A suite of command-line tools for working with CSV, the king of tabular file formats.
- [zenrows](internet-www-http.md#zenrows) - Zenrows Python SDK: Fetch, Extract (structured data), Batch and Crawl APIs
- [rax](scientific-engineering-artificial-intelligence.md#rax) - Learning-to-Rank using JAX.
- [pytracking2](communications-email.md#pytracking2) - Email open and click tracking
- [pyvalid](software-development-debuggers.md#pyvalid) - The module, which allows easily validate function's input/output values.
- [django-pipeline](internet-www-http.md#django-pipeline) - Pipeline is an asset packaging library for Django.
- [http-sfv](internet-www-http.md#http-sfv) - Parse and serialise HTTP Structured Field Values
- [geoip2fast](internet.md#geoip2fast) - GeoIP2Fast is the fastest GeoIP2 country/city/asn lookup library that supports IPv4 and IPv6. A search takes less than 0.00003 seconds. It has its own data file updated twice a week with Maxmind-Geolite2-CSV, supports IPv4/IPv6 and is Pure Python!
- [onnxruntime-openvino](scientific-engineering.md#onnxruntime-openvino) - ONNX Runtime is a runtime accelerator for Machine Learning models
- [poutyne](scientific-engineering.md#poutyne) - A simplified framework and utilities for PyTorch.
- [django-weasyprint](internet-www-http.md#django-weasyprint) - Django WeasyPrint integration
- [ironcalc](office-business-financial.md#ironcalc) - Create, edit and evaluate Excel spreadsheets
- [odc-geo](scientific-engineering-gis.md#odc-geo) - Geometry Classes and Operations (opendatacube)
- [fastapi-utilities](internet-www-http.md#fastapi-utilities) - Reusable utilities for FastAPI
- [django-ninja-jwt](internet.md#django-ninja-jwt) - Django Ninja JWT - JSON Web Token for Django-Ninja
- [deepparse](scientific-engineering.md#deepparse) - A library for parsing multinational street addresses using deep learning.
- [flake8-variables-names](software-development-documentation.md#flake8-variables-names) - A flake8 extension that helps to make more readable variables names
- [snowflake-ml-python](database.md#snowflake-ml-python) - The machine learning client library that is used for interacting with Snowflake to build machine learning solutions.
- [Panda3D](games-entertainment.md#panda3d) - Panda3D is a framework for 3D rendering and game development for Python and C++ programs.
- [ofxtools](office-business.md#ofxtools) - Library for working with Open Financial Exchange (OFX) data
- [pubnub](internet-www-http.md#pubnub) - PubNub Real-time push service in the cloud
- [tf-keras-nightly](scientific-engineering.md#tf-keras-nightly) - Deep learning for humans.
- [modulegraph](software-development-build-tools.md#modulegraph) - Python module dependency analysis tool
- [pynini](scientific-engineering-artificial-intelligence.md#pynini) - Finite-state grammar compilation
- [persistent](database.md#persistent) - Translucent persistent objects
- [torch-tb-profiler](scientific-engineering.md#torch-tb-profiler) - PyTorch Profiler TensorBoard Plugin
- [django-render-block](internet.md#django-render-block) - Render a particular block from a template to a string.
- [launchdarkly-openfeature-server](software-development.md#launchdarkly-openfeature-server) - An OpenFeature provider for the LaunchDarkly Python server SDK
- [pyfcm](communications.md#pyfcm) - Python client for FCM - Firebase Cloud Messaging (Android, iOS and Web)
- [OpenTimelineIO](multimedia-graphics.md#opentimelineio) - Editorial interchange format and API
- [WTForms-JSON](internet-www-http.md#wtforms-json) - Adds smart json support for WTForms. Useful for when using WTForms with RESTful APIs.
- [t61codec](communications.md#t61codec) - Python Codec for ITU T.61 Strings
- [modelcontextprotocol](software-development-code-generators.md#modelcontextprotocol) - CLI tool and utilities for scaffolding Model Context Protocol (MCP) projects with enhanced logging
- [starlette-admin](internet-www-http.md#starlette-admin) - Fast, beautiful and extensible administrative interface framework for FastAPI & Starlette applications
- [plotly-stubs](scientific-engineering.md#plotly-stubs) - Type stubs for plotly.
- [unicon](software-development-build-tools.md#unicon) - Unicon Connection Library
- [probablepeople](scientific-engineering.md#probablepeople) - Parse romanized names & companies using advanced NLP methods
- [arcp](internet.md#arcp) - arcp (Archive and Package) URI parser and generator
- [fastobo](scientific-engineering-bio-informatics.md#fastobo) - Faultless AST for Open Biomedical Ontologies in Python.
- [scrypt](security-cryptography.md#scrypt) - Bindings for the scrypt key derivation function library
- [fastapi-restful](internet.md#fastapi-restful) - Quicker FastApi developing tools
- [buildpg](internet.md#buildpg) - Query building for the postgresql prepared statements and asyncpg.
- [djangorestframework-jsonapi](internet-www-http.md#djangorestframework-jsonapi) - A Django REST framework API adapter for the JSON:API spec.
- [baron](software-development.md#baron) - Full Syntax Tree for python to make writing refactoring code a realist task
- [MDAnalysis](scientific-engineering.md#mdanalysis) - An object-oriented toolkit to analyze molecular dynamics trajectories.
- [fasta2a](internet.md#fasta2a) - Convert an AI Agent into a A2A server! ✨
- [BTrees](database.md#btrees) - Scalable persistent object containers
- [django-guid](internet-www-http.md#django-guid) - Middleware that enables single request-response cycle tracing by injecting a unique ID into project logs
- [webassets](internet-www-http.md#webassets) - Media asset management for Python, with glue code for various web frameworks
- [redbaron](software-development.md#redbaron) - Abstraction on top of baron, a FST for python to make writing refactoring code a realistic task
- [skrub](scientific-engineering.md#skrub) - Machine learning with dataframes
- [docstr-coverage](documentation.md#docstr-coverage) - Utility for examining python source files to ensure proper documentation. Lists missing docstrings, and calculates overall docstring coverage percentage rating.
- [kreuzberg](office-business.md#kreuzberg) - High-performance document intelligence library for Python. Extract text, metadata, and structured data from PDFs, Office documents, images, and 88+ formats. Powered by Rust core for 10-50x speed improvements.
- [spark-parser](software-development-code-generators.md#spark-parser) - An Earley-Algorithm Context-free grammar Parser Toolkit
- [kiteconnect](office-business-financial.md#kiteconnect) - The official Python client for the Kite Connect trading API
- [distrax](scientific-engineering-artificial-intelligence.md#distrax) - Distrax: Probability distributions in JAX.
- [rocrate](internet.md#rocrate) - RO-Crate metadata generator/parser
- [sqlcipher3-binary](database-database-engines-servers.md#sqlcipher3-binary) - DB-API 2.0 interface for SQLCipher 3.x
- [py2neo-history](database.md#py2neo-history) - Python client library and toolkit for Neo4j
- [pyodata](internet-www-http.md#pyodata) - Enterprise ready Python OData client
- [solcast](internet.md#solcast) - a simple Python SDK for the Solcast API
- [drake](scientific-engineering.md#drake) - Model-based design and verification for robotics
- [rake-nltk](software-development-build-tools.md#rake-nltk) - RAKE short for Rapid Automatic Keyword Extraction algorithm, is a domain independent keyword extraction algorithm which tries to determine key phrases in a body of text by analyzing the frequency of word appearance and its co-occurance with other words in the text.
- [ropwr](scientific-engineering-mathematics.md#ropwr) - RoPWR: Robust Piecewise Regression
- [x690](communications.md#x690) - Pure-Python ASN.1 BER encoder and decoder with typed values, light on memory for large documents
- [unicon.plugins](software-development-build-tools.md#uniconplugins) - Unicon Connection Library Plugins
- [pyamg](education.md#pyamg) - PyAMG: Algebraic Multigrid Solvers in Python
- [GridDataFormats](scientific-engineering.md#griddataformats) - Reading and writing of data on regular grids in Python
- [mac-alias](desktop-environment.md#mac-alias) - Generate/parse macOS Alias records from Python
- [optbinning](scientific-engineering-mathematics.md#optbinning) - OptBinning: The Python Optimal Binning library
- [tf-nightly](scientific-engineering.md#tf-nightly) - TensorFlow is an open source machine learning framework for everyone.
- [ds-store](desktop-environment.md#ds-store) - Manipulate Finder .DS_Store files from Python
- [ws4py](communications.md#ws4py) - WebSocket client and server library for Python 2 and 3 as well as PyPy
- [bagit](communications-file-sharing.md#bagit) - Create and validate BagIt packages
- [pyats](software-development-build-tools.md#pyats) - pyATS - Python Automation Test System
- [quart-schema](internet-www-http.md#quart-schema) - A Quart extension to provide schema validation
- [questdb](database-front-ends.md#questdb) - QuestDB client library for Python
- [APIFlask](internet-www-http.md#apiflask) - A lightweight web API framework based on Flask.
- [tlslite-ng](security-cryptography.md#tlslite-ng) - Pure python implementation of SSL and TLS.
- [ansible-pylibssh](security.md#ansible-pylibssh) - Python bindings for libssh client specific to Ansible use case
- [scrapegraph-py](internet-www-http.md#scrapegraph-py) - Official Python SDK for ScrapeGraph AI API
- [mechanize](internet.md#mechanize) - Stateful, programmatic web browsing
- [CouchDB](database-front-ends.md#couchdb) - Python library for working with CouchDB
- [fastapi-decorators](internet.md#fastapi-decorators) - Create decorators for your endpoints using FastAPI dependencies.
- [joblibspark](scientific-engineering.md#joblibspark) - Joblib Apache Spark Backend
- [tableschema](internet-www-http.md#tableschema) - A utility library for working with Table Schema in Python
- [pyats.datastructures](software-development-build-tools.md#pyatsdatastructures) - pyATS Datastructures: Extended Datastructures for Grownups
- [pyats.easypy](software-development-build-tools.md#pyatseasypy) - pyATS Easypy: launcher and runtime environment
- [tf2onnx](scientific-engineering.md#tf2onnx) - Tensorflow to ONNX converter
- [pyats.topology](software-development-build-tools.md#pyatstopology) - pyATS Topology: Topology Objects and Testbed YAMLs
- [pyats.aetest](software-development-build-tools.md#pyatsaetest) - pyATS AEtest: Testscript Engine
- [pyats.utils](software-development-build-tools.md#pyatsutils) - pyATS Utils: Utilities Module
- [abx-dl](internet-www-http.md#abx-dl) - All-in-one CLI tool to download and extract content from URLs
- [foundry-local-sdk](scientific-engineering.md#foundry-local-sdk) - Foundry Local Python SDK (v2): in-process Python bindings for the Foundry Local native runtime.
- [pyats.reporter](software-development-build-tools.md#pyatsreporter) - pyATS Reporter: Result Collection and Reporting
- [pyats.connections](software-development-build-tools.md#pyatsconnections) - pyATS Connection: Device Connection Handling & Base Classes
- [pyats.aereport](software-development-build-tools.md#pyatsaereport) - pyATS AEreport: Result Collection and Reporting
- [pyats.tcl](software-development-build-tools.md#pyatstcl) - pyATS Tcl: Tcl Integration and Objects
- [pyats.log](software-development-build-tools.md#pyatslog) - pyATS Log: Logging Format and Utilities
- [pyats.kleenex](software-development-build-tools.md#pyatskleenex) - pyATS Kleenex: Testbed Preparation, Clean & Finalization
- [pdf-oxide](scientific-engineering-information-analysis.md#pdf-oxide) - The fastest Python PDF library — 0.8ms mean, 5× faster than the industry leaders, 100% pass rate on 3,830 real-world PDFs. Text extraction, Markdown/HTML conversion, PDF creation and editing.
- [zope.sqlalchemy](database.md#zopesqlalchemy) - Minimal Zope/SQLAlchemy transaction integration
- [pyats.results](software-development-build-tools.md#pyatsresults) - pyATS Results: Representing Results using Objects
- [cyksuid](scientific-engineering.md#cyksuid) - Cython implementation of ksuid
- [pyats.async](software-development-build-tools.md#pyatsasync) - pyATS Async: Asynchronous Execution of Codes
- [pronto](scientific-engineering-bio-informatics.md#pronto) - Python frontend to ontologies.
- [device-detector](internet-www-http.md#device-detector) - Python3 port of matomo's Device Detector
- [colormath](scientific-engineering-mathematics.md#colormath) - Color math and conversion library.
- [citeproc-py](documentation.md#citeproc-py) - Citations and bibliography formatter
- [bentoml](scientific-engineering-artificial-intelligence.md#bentoml) - BentoML: The easiest way to serve AI apps and models
- [pgparse](database.md#pgparse) - Python wrapper for libpg_query
- [pytricia](internet-log-analysis.md#pytricia) - An efficient IP address storage and lookup module for Python.
- [pypcd4](scientific-engineering.md#pypcd4) - Read and write PCL .pcd files in python
- [databend-driver](database.md#databend-driver) - Databend Driver Python Binding
- [objectory](scientific-engineering.md#objectory) - A light library for general purpose object factories
- [Frozen-Flask](internet-www-http.md#frozen-flask) - Freezes a Flask application into a set of static files.
- [tensorflow-io](scientific-engineering.md#tensorflow-io) - TensorFlow IO
- [django-enum](internet-www-http.md#django-enum) - Full and natural support for enumerations as Django model fields.
- [flake8-functions](software-development-documentation.md#flake8-functions) - A flake8 extension that checks functions
- [django-markdownx](internet-www-http.md#django-markdownx) - A comprehensive Markdown editor built for Django.
- [websocket](internet.md#websocket) - Websocket implementation for gevent
- [turbohtml](internet.md#turbohtml) - A fast, fully typed HTML toolkit for Python, powered by a C-accelerated core.
- [matrx-ai](scientific-engineering-artificial-intelligence.md#matrx-ai) - Unified multi-provider AI client, orchestration, and tool system
- [uncompyle6](software-development-debuggers.md#uncompyle6) - Python cross-version byte-code decompiler
- [ag2](software-development.md#ag2) - A programming framework for agentic AI
- [dataflows-tabulator](internet-www-http.md#dataflows-tabulator) - Consistent interface for stream reading and writing tabular data (csv/xls/json/etc)
- [genie](software-development-build-tools.md#genie) - Genie: THE standard pyATS Library System
- [python-openid](internet-www-http.md#python-openid) - OpenID support for servers and consumers.
- [ical](office-business-scheduling.md#ical) - Python iCalendar implementation (rfc 5545) with built-in recurring event support
- [pytorch-forecasting](scientific-engineering.md#pytorch-forecasting) - Forecasting timeseries with PyTorch - dataloaders, normalizers, metrics and models
- [webapp2](internet-www-http.md#webapp2) - Taking Google App Engine's webapp to the next level!
- [wecom-aibot-python-sdk](communications-chat.md#wecom-aibot-python-sdk) - 企业微信智能机器人 Python SDK —— 基于 WebSocket 长连接通道，提供消息收发、流式回复、模板卡片、事件回调、文件下载解密等核心能力。
- [http-exceptions](software-development-build-tools.md#http-exceptions) - Raisable HTTP Exceptions
- [sopsy](security-cryptography.md#sopsy) - SOPS Python wrapper library
- [Kivy](artistic-software.md#kivy) - An open-source Python framework for developing GUI apps that work cross-platform, including desktop, mobile and embedded platforms.
- [PGPy13](security.md#pgpy13) - Pretty Good Privacy for Python (temporary fork for py3.13 compatability)
- [crispy-tailwind](internet-www-http.md#crispy-tailwind) - Tailwind CSS for Django Crispy Forms
- [aspose-slides](multimedia-graphics.md#aspose-slides) - Aspose.Slides for Python via .NET is a presentation file formats processing library for working with Microsoft PowerPoint files without using Microsoft PowerPoint.
- [intervals](internet-www-http.md#intervals) - Python tools for handling intervals (ranges of comparable objects).
- [jina](database-database-engines-servers.md#jina) - Multimodal AI services & pipelines with cloud-native stack: gRPC, Kubernetes, Docker, OpenTelemetry, Prometheus, Jaeger, etc.
- [pyventus](software-development.md#pyventus) - A Python library for event-driven and reactive programming.
- [libmagic](security.md#libmagic) - libmagic bindings
- [fastapi-health](software-development-build-tools.md#fastapi-health) - Heath check on FastAPI applications.
- [sqlalchemy-filters](database.md#sqlalchemy-filters) - A library to filter SQLAlchemy queries.
- [vbuild](software-development-build-tools.md#vbuild) - A simple module to extract html/script/style from a vuejs '.vue' file (can minimize/es2015 compliant js) ... just py2 or py3, NO nodejs !
- [thetadata](office-business-financial.md#thetadata) - Python client library for ThetaData market data APIs
- [Genshi](internet-www-http.md#genshi) - A toolkit for generation of output for the web
- [prophy](scientific-engineering-interface-engine-protocol-translator.md#prophy) - prophy: fast serialization protocol
- [loki-mode-sdk](software-development-build-tools.md#loki-mode-sdk) - Python SDK for Loki Mode - autonomous multi-agent development platform
- [flake8-class-attributes-order](software-development-documentation.md#flake8-class-attributes-order) - A flake8 extension that checks classes attributes order
- [universal-startfile](desktop-environment-file-managers.md#universal-startfile) - A cross-platform version of 'os.startfile' from the standard library.
- [pyaxmlparser](software-development-build-tools.md#pyaxmlparser) - Python3 Parser for Android XML file and get Application Name without using Androguard
- [py-automapper](software-development-build-tools.md#py-automapper) - Library for automatically mapping one object to another
- [google-i18n-address](software-development-internationalization.md#google-i18n-address) - Address validation helpers for Google's i18n address database
- [cwl-utils](file-formats.md#cwl-utils) - 
- [openTSNE](scientific-engineering.md#opentsne) - Extensible, parallel implementations of t-SNE
- [WSDiscovery](communications.md#wsdiscovery) - WS-Discovery implementation for python
- [sqlalchemy-views](database.md#sqlalchemy-views) - Adds CreateView and DropView constructs to SQLAlchemy
- [centrifuge-python](internet.md#centrifuge-python) - WebSocket SDK for Centrifugo (and any Centrifuge-based server) on top of Python asyncio library
- [dmgbuild](desktop-environment.md#dmgbuild) - macOS command line utility to build disk images
- [2captcha-python-async](scientific-engineering-image-recognition.md#2captcha-python-async) - Python module for easy integration with 2Captcha API
- [aspose-email-foss](communications-email.md#aspose-email-foss) - Pure Python CFB and Outlook MSG toolkit for reading, projecting, and writing message data.
- [lbox-clients](scientific-engineering-artificial-intelligence.md#lbox-clients) - This module contains client sdk uses to conntect to the Labelbox API and backends
- [pykeepass](security.md#pykeepass) - Python library to interact with keepass databases (supports KDBX3 and KDBX4)
- [wolfxl](office-business-financial.md#wolfxl) - Openpyxl-compatible Excel library with a Rust backend: speed up openpyxl code with one import change and edit .xlsx templates without losing formatting, conditional formatting, or data validation. WolfXL 2.0.21 measured 6.7-12.0x faster than openpyxl 3.1.5 on the committed read/write benchmark (small-file gains vary). MIT.
- [pySmartDL](internet-www-http.md#pysmartdl) - A Smart Download Manager for Python
- [tfx-bsl](scientific-engineering.md#tfx-bsl) - tfx_bsl (TFX Basic Shared Libraries) contains libraries shared by many TFX (TensorFlow eXtended) libraries and components.
- [truthound](scientific-engineering.md#truthound) - Zero-Configuration Data Quality Framework Powered by Polars
- [python-rtmidi](multimedia-sound-audio.md#python-rtmidi) - A Python binding for the RtMidi C++ library implemented using Cython.
- [mendeleev](scientific-engineering-chemistry.md#mendeleev) - Pythonic periodic table of elements
- [genie.libs.parser](software-development-build-tools.md#genielibsparser) - Genie libs Parser: Genie Parser Libraries
- [slixmpp](internet-xmpp.md#slixmpp) - Slixmpp is an elegant Python library for XMPP (aka Jabber).
- [paper-pptx](office-business-office-suites.md#paper-pptx) - Create, read, and update PowerPoint 2007+ (.pptx) files.
- [ovstage](scientific-engineering.md#ovstage) - NVIDIA OVStage Data Plane Python API
- [genie.libs.sdk](software-development-build-tools.md#genielibssdk) - Genie libs sdk: Libraries containing all Triggers and Verifications
- [fish-audio-sdk](multimedia-sound-audio.md#fish-audio-sdk) - The official Python library for the Fish Audio API
- [genie.libs.ops](software-development-build-tools.md#genielibsops) - Genie libs Ops: Libraries to retrieve operational state of the topology
- [genie.libs.clean](software-development-build-tools.md#genielibsclean) - Genie Library for device clean support
- [apache-superset-core](database.md#apache-superset-core) - Core Python package for building Apache Superset backend extensions and integrations
- [genie.libs.conf](software-development-build-tools.md#genielibsconf) - Genie libs Conf: Libraries to configures topology through Python object attributes
- [PyLTI1p3](internet-www-http.md#pylti1p3) - LTI 1.3 Advantage Tool implementation in Python
- [genie.libs.filetransferutils](software-development-build-tools.md#genielibsfiletransferutils) - Genie libs FileTransferUtils: Genie FileTransferUtils Libraries
- [genie.libs.health](software-development-build-tools.md#genielibshealth) - pyATS Health Check for monitoring device health status
- [aiopenapi3](internet.md#aiopenapi3) - client and validator for OpenAPI3 3.0, OpenAPI 3.1, OpenAPI 3.2, Swagger 2.0
- [cwl-upgrader](file-formats.md#cwl-upgrader) - Upgrade a CWL tool or workflow document from one version to another
- [pybedtools](scientific-engineering-bio-informatics.md#pybedtools) - Wrapper around BEDTools for bioinformatics work
- [mwxml](scientific-engineering.md#mwxml) - A set of utilities for processing MediaWiki XML dump data.
- [py3rijndael](security-cryptography.md#py3rijndael) - Rijndael algorithm library for Python3.
- [mwtypes](scientific-engineering.md#mwtypes) - A set of types for processing MediaWiki data.
- [rest.connector](software-development-build-tools.md#restconnector) - pyATS REST connection package
- [para](scientific-engineering.md#para) - a set utilities that ake advantage of python's 'multiprocessing' module to distribute CPU-intensive tasks
- [mwcli](scientific-engineering.md#mwcli) - Utilities for processing MediaWiki on the command line.
- [WTForms-SQLAlchemy](internet-www-http.md#wtforms-sqlalchemy) - SQLAlchemy tools for WTForms
- [flake8-expression-complexity](software-development-documentation.md#flake8-expression-complexity) - A flake8 extension that checks expressions complexity
- [django-parler](internet-www-http.md#django-parler) - Simple Django model translations without nasty hacks, featuring nice admin integration.
- [cachier](other-nonlisted-topic.md#cachier) - Persistent, stale-free, local and cross-machine caching for Python functions.
- [ha-mcp-dev](home-automation.md#ha-mcp-dev) - Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants.
- [pywa](communications-chat.md#pywa) - 🚀 Build WhatsApp Bots in Python • Fast, Effortless, Powerful
- [segyio](scientific-engineering.md#segyio) - Simple & fast IO for SEG-Y files
- [pysmi-lextudio](communications.md#pysmi-lextudio) - A pure-Python implementation of SNMP/SMI MIB parsing and conversion library.
- [spider-browser](internet-www-http.md#spider-browser) - Browser automation client for Spider's pre-warmed browser fleet with smart retry and browser switching
- [speechmatics-voice](multimedia-sound-audio.md#speechmatics-voice) - Speechmatics Voice Agent Python client for Real-Time API
- [YORM](database.md#yorm) - Automatic object-YAML mapping for Python.
- [property-manager](documentation-sphinx.md#property-manager) - Useful property variants for Python programming (required properties, writable properties, cached properties, etc)
- [mysql-connector-python-rf](database.md#mysql-connector-python-rf) - MySQL driver written in Python
- [google-vizier](scientific-engineering-mathematics.md#google-vizier) - Open Source Vizier: Distributed service framework for blackbox optimization and research.
- [pysnmp-lextudio](communications.md#pysnmp-lextudio) - A deprecated package. Please use 'pysnmp' instead.
- [paper-docx](office-business-office-suites.md#paper-docx) - Create, read, and update Microsoft Word .docx files.
- [torchreid](education.md#torchreid) - Torchreid-Pip: Deep learning person re-identification in PyTorch.
- [falkordblite](database.md#falkordblite) - FalkorDB embedded in a Python package
- [sgfmill](games-entertainment-board-games.md#sgfmill) - Library for reading and writing files using Smart Game Format (SGF).
- [airspeed-ext](internet-www-http.md#airspeed-ext) - Airspeed is a powerful and easy-to-use templating engine for Python that aims for a high level of compatibility with Velocity templates in AWS cloud services.
- [liac-arff](scientific-engineering-artificial-intelligence.md#liac-arff) - A module for read and write ARFF files in Python.
- [python-status](internet.md#python-status) - HTTP Status for Humans
- [SLH-DSA](security.md#slh-dsa) - Pure Python implementation of the SLH-DSA algorithm (based on FIPS 205).
- [django-typer](internet-www-http.md#django-typer) - Use Typer to define the CLI for your Django management commands.
- [h2o-wave](communications-chat.md#h2o-wave) - Python driver for H2O Wave Realtime Apps
- [taxjar](office-business.md#taxjar) - Sales tax API client for Python
- [galois](scientific-engineering-mathematics.md#galois) - A performant NumPy extension for Galois fields and their applications
- [python-evtx](security.md#python-evtx) - Pure Python parser for Windows event log files (.evtx).
- [grafana-client](communications.md#grafana-client) - A client library for accessing the Grafana HTTP API, written in Python
- [zodbpickle](database.md#zodbpickle) - Fork of Python 3 pickle module
- [aiohomematic-config](home-automation.md#aiohomematic-config) - Presentation-layer library for Homematic device configuration UI.
- [sahi](scientific-engineering-artificial-intelligence.md#sahi) - A vision library for performing sliced inference on large images/small objects
- [graph-retriever](scientific-engineering-artificial-intelligence.md#graph-retriever) - Retriever combining unstructured similarity and structured document traversal.
- [langchain-graph-retriever](scientific-engineering-artificial-intelligence.md#langchain-graph-retriever) - LangChain retriever for traversing document graphs on top of vector-based similarity search.
- [flake8-annotations-complexity](software-development-documentation.md#flake8-annotations-complexity) - A flake8 extension that checks for type annotations complexity
- [DAWG-Python](scientific-engineering-information-analysis.md#dawg-python) - Pure-python reader for DAWGs (DAFSAs) created by dawgdic C++ library or DAWG Python extension.
- [backoff-utils](internet-www-http.md#backoff-utils) - Python functions and decorators for various backoff/retry strategies
- [eutils](scientific-engineering-bio-informatics.md#eutils) - Python interface to NCBI's eutilities API
- [openbabel-wheel](scientific-engineering-bio-informatics.md#openbabel-wheel) - An unofficial repository to distribute OpenBabel prebuilt wheels through Pypi..
- [pymongosql](database.md#pymongosql) - Python DB API 2.0 (PEP 249) client for MongoDB
- [mlOpus](scientific-engineering-artificial-intelligence.md#mlopus) - MLOps tools for research and development.
- [tensorflowjs](scientific-engineering.md#tensorflowjs) - 
- [musicbrainzngs](database-front-ends.md#musicbrainzngs) - Python bindings for the MusicBrainz NGS and the Cover Art Archive webservices
- [minimalmodbus](communications.md#minimalmodbus) - Easy-to-use Modbus RTU and Modbus ASCII implementation for Python
- [pyserial-asyncio-fast](communications.md#pyserial-asyncio-fast) - Python Serial Port Extension - Asynchronous I/O support
- [ete3](scientific-engineering-bio-informatics.md#ete3) - A Python Environment for (phylogenetic) Tree Exploration
- [aioaws](internet.md#aioaws) - Asyncio SDK for some AWS services.
- [mistralai-workflows-plugins-mistralai](scientific-engineering-artificial-intelligence.md#mistralai-workflows-plugins-mistralai) - Mistral AI plugin for Mistral Workflows - Provides native Mistral AI integration
- [cx-Freeze](software-development-build-tools.md#cx-freeze) - Create standalone executables from Python scripts
- [arcgis](internet-www-http.md#arcgis) - ArcGIS API for Python
- [Flask-PyMongo](internet-www-http.md#flask-pymongo) - PyMongo support for Flask applications
- [traceml](scientific-engineering-artificial-intelligence.md#traceml) - Engine for ML/Data tracking, visualization, dashboards, and model UI for Polyaxon.
- [infinity](internet-www-http.md#infinity) - All-in-one infinity value for Python. Can be compared to any object.
- [pymorphy2-dicts-ru](scientific-engineering-information-analysis.md#pymorphy2-dicts-ru) - Russian dictionaries for pymorphy2
- [fhirpy](internet-www-http.md#fhirpy) - FHIR client for python
- [executor](internet.md#executor) - Programmer friendly subprocess wrapper
- [albumentationsx](scientific-engineering.md#albumentationsx) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volume data, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows. Available under AGPL-3.0-only or a commercial license with agreed coverage for your team, products, and deployments.
- [kitchen](software-development-internationalization.md#kitchen) - Kitchen contains a cornucopia of useful code
- [Flask-Assets](internet-www-http.md#flask-assets) - Asset management for Flask, to compress and merge CSS and Javascript files.
- [surrealdb](database.md#surrealdb) - SurrealDB python client
- [wn](scientific-engineering-information-analysis.md#wn) - Wordnet interface library
- [sqlcipher3-wheels](database-database-engines-servers.md#sqlcipher3-wheels) - DB-API 2.0 interface for SQLCipher 3.x
- [pytest-beartype](software-development-code-generators.md#pytest-beartype) - Pytest plugin type-checking tests, fixtures, and/or your codebase with beartype: the unbearably fast near-real-time pure-Python runtime-static type-checker.
- [fastapi-csrf-protect](internet-www-http.md#fastapi-csrf-protect) - Stateless implementation of Cross-Site Request Forgery (XSRF) Protection by using Double Submit Cookie mitigation pattern
- [aiomisc](internet.md#aiomisc) - aiomisc - miscellaneous utils for asyncio
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
- [pynmea2](scientific-engineering-gis.md#pynmea2) - Python library for the NMEA 0183 protcol
- [bittensor-wallet](scientific-engineering.md#bittensor-wallet) - 
- [user-agent](internet-www-http.md#user-agent) - Library to build content for User-Agent HTTP header
- [modulegraph2](software-development-build-tools.md#modulegraph2) - A module import dependency graph for Python projects.
- [setupmeta](software-development-build-tools.md#setupmeta) - Simplify your setup.py
- [labelbox](scientific-engineering-artificial-intelligence.md#labelbox) - Labelbox Python API
- [fastapi-cors](internet.md#fastapi-cors) - Simple env support of CORS settings for Fastapi applications
- [xclienttransaction](software-development-build-tools.md#xclienttransaction) - Twitter X-Client-Transaction-Id generator written in python.
- [Bootstrap-Flask](internet-www-http.md#bootstrap-flask) - Bootstrap 4 & 5 helper for your Flask projects.
- [flask-paginate](internet-www-http.md#flask-paginate) - Simple paginate support for flask
- [pyaaf2](multimedia-graphics.md#pyaaf2) - A python module for reading and writing advanced authoring format files
- [ogx-client](scientific-engineering-artificial-intelligence.md#ogx-client) - OpenAPI-generated Python client for OGX
- [arize-phoenix-sqlean](database-database-engines-servers.md#arize-phoenix-sqlean) - sqlite3 with extensions
- [sqlalchemy-diff](database.md#sqlalchemy-diff) - A tool for comparing database schemas using SQLAlchemy
- [uniplot](scientific-engineering.md#uniplot) - Lightweight plotting to the terminal. 4x resolution via Unicode.
- [nemo-text-processing](scientific-engineering.md#nemo-text-processing) - NeMo text processing for ASR and TTS
- [django-summernote](internet-www-http.md#django-summernote) - Summernote plugin for Django
- [py-pglite](database.md#py-pglite) - Python testing library for PGlite - in-memory PostgreSQL for tests
- [agentenv-framework-protocol](scientific-engineering-artificial-intelligence.md#agentenv-framework-protocol) - Open data-plane protocol and server SDK for agent environments.
- [cu2qu](multimedia-graphics.md#cu2qu) - Cubic-to-quadratic bezier curve conversion
- [ai-edge-litert-nightly](scientific-engineering.md#ai-edge-litert-nightly) - LiteRT is for mobile and embedded devices.
- [rst2pdf](documentation.md#rst2pdf) - Convert reStructured Text to PDF via ReportLab.
- [onnxruntime-directml](scientific-engineering.md#onnxruntime-directml) - ONNX Runtime is a runtime accelerator for Machine Learning models
- [py-vollib-vectorized](office-business-financial.md#py-vollib-vectorized) - A fast, vectorized approach to calculating Implied Volatility and Greeks using the Black, Black-Scholes and Black-Scholes-Merton pricing.
- [dm-haiku](scientific-engineering-mathematics.md#dm-haiku) - Haiku is a library for building neural networks in JAX.
- [fullbleed](office-business.md#fullbleed) - Deterministic Python PDF engine for reports, invoices, accessible documents, print-ready output, and compiled VDP
- [httpcloak](internet-www-http.md#httpcloak) - Browser fingerprint emulation HTTP client with HTTP/1.1, HTTP/2, and HTTP/3 support
- [upstash-vector](database.md#upstash-vector) - Serverless Vector SDK from Upstash
- [tendo](internet-www-http.md#tendo) - A Python library that extends some core functionality
- [odc-stac](scientific-engineering-gis.md#odc-stac) - Tooling for converting STAC metadata to ODC data model
- [aiosql](database.md#aiosql) - Simple SQL in Python
- [PyPDFForm](file-formats.md#pypdfform) - The Python library & CLI for PDF forms.
- [pymorphy2](scientific-engineering-information-analysis.md#pymorphy2) - Morphological analyzer (POS tagger + inflection engine) for Russian language.
- [speechmatics-agent-stt](multimedia-sound-audio.md#speechmatics-agent-stt) - Speechmatics Agent STT Python client for agent transcription
- [zaproxy](security.md#zaproxy) - ZAP API Client
- [sapien](education.md#sapien) - ['SAPIEN: A SimulAted Parted based Interactive ENvironment']
- [django-qr-code](internet-www-http.md#django-qr-code) - An application that provides tools for displaying QR codes on your Django site.
- [django-admin-inline-paginator-plus](internet-www-http.md#django-admin-inline-paginator-plus) - The 'Django Admin Inline Paginator Plus' is simple way to paginate your inlines in Django admin
- [jupyter_bokeh](scientific-engineering.md#jupyter_bokeh) - A Jupyter extension for rendering Bokeh content.
- [bx-python](scientific-engineering-bio-informatics.md#bx-python) - Tools for manipulating biological data, particularly multiple sequence alignments
- [aimmspy](scientific-engineering-mathematics.md#aimmspy) - Python bindings for the AIMMS optimization platform, built with pybind11 for seamless C++ integration. Enables efficient data exchange and interaction with AIMMS projects using pandas, polars, and pyarrow. Ideal for advanced optimization workflows requiring high-performance native code.
- [jedi-language-server](software-development-code-generators.md#jedi-language-server) - A language server for Jedi!
- [jcodemunch-mcp](software-development.md#jcodemunch-mcp) - MCP server that gives AI coding agents the exact function or class they asked for, not the whole file. Runs on your machine, 70+ languages. Free for non-commercial use; commercial use needs a one-time license.
- [django-graphiql-debug-toolbar](internet.md#django-graphiql-debug-toolbar) - Django Debug Toolbar for GraphiQL IDE.
- [pdfreader](software-development.md#pdfreader) - Pythonic API for parsing PDF files
- [urlpath](internet-www-http.md#urlpath) - Object-oriented URL from urllib.parse and pathlib
- [jsonrpcclient](internet.md#jsonrpcclient) - Create JSON-RPC 2.0 requests and parse responses in Python
- [ovs](database-front-ends.md#ovs) - Open vSwitch library
- [fastdigest](scientific-engineering.md#fastdigest) - A fast t-digest library for Python built on Rust.
- [torchax](scientific-engineering.md#torchax) - torchax is a library for running Jax and PyTorch together
- [iden](scientific-engineering.md#iden) - simple library to manage a dataset of shards to train machine learning models
- [epicscorelibs](scientific-engineering.md#epicscorelibs) - The EPICS Core libraries for use by python modules
- [django-auth-adfs](internet-www-http.md#django-auth-adfs) - A Django authentication backend for Microsoft ADFS and AzureAD
- [osm2geojson](scientific-engineering-gis.md#osm2geojson) - Parse OSM and Overpass JSON
- [fastapi-etag](internet-www-http.md#fastapi-etag) - Convenience library for working with etags in fastapi
- [base58check](internet-www-http.md#base58check) - Base58check encoding and decoding of binary data
- [python-redmine](internet-www-http.md#python-redmine) - Library for communicating with a Redmine project management application
- [pymediawiki](internet.md#pymediawiki) - Wikipedia and MediaWiki API wrapper for Python
- [ffprobe-python](multimedia-video.md#ffprobe-python) - A wrapper around ffprobe command to extract metadata from media files.
- [napari-plugin-engine](scientific-engineering.md#napari-plugin-engine) - napari plugin engine, fork of pluggy
- [ecologits](internet.md#ecologits) - EcoLogits tracks and estimates the energy consumption and environmental impacts of using generative AI models through APIs.
- [translate-toolkit](software-development-internationalization.md#translate-toolkit) - Tools and API for translation and localization engineering.
- [ZODB](database.md#zodb) - ZODB, a Python object-oriented database
- [pytorch_optimizer](scientific-engineering.md#pytorch_optimizer) - optimizer & lr scheduler & objective function collections in PyTorch
- [networkit](scientific-engineering-bio-informatics.md#networkit) - NetworKit is a toolbox for high-performance network analysis
- [solidpython2](scientific-engineering-mathematics.md#solidpython2) - Python interface to the OpenSCAD declarative geometry language
- [neomodel](database.md#neomodel) - An object mapper for the neo4j graph database.
- [crispy-bootstrap3](internet-www-http.md#crispy-bootstrap3) - Bootstrap3 template pack for django-crispy-forms
- [pycomm3](scientific-engineering-human-machine-interfaces.md#pycomm3) - A Python Ethernet/IP library for communicating with Allen-Bradley PLCs.
- [tensorflow-decision-forests](scientific-engineering.md#tensorflow-decision-forests) - Collection of training and inference decision forest algorithms.
- [pecan](internet-www-http.md#pecan) - A WSGI object-dispatching web framework, designed to be lean and fast, with few dependencies.
- [pvxslibs](scientific-engineering.md#pvxslibs) - PVXS libraries packaged for python
- [py3dns](internet-name-service-dns.md#py3dns) - Python 3 DNS library
- [PyVISA-sim](scientific-engineering-interface-engine-protocol-translator.md#pyvisa-sim) - Simulated backend for PyVISA implementing TCPIP, GPIB, RS232, and USB resources
- [vesin](scientific-engineering.md#vesin) - Computing neighbor lists for atomistic system
- [alchemlyb](scientific-engineering-2.md#alchemlyb) - the simple alchemistry library
- [depgather](security.md#depgather) - Get a list of deps given a pyproject.toml, uv.lock, requirements.txt etc
- [p4p](scientific-engineering-2.md#p4p) - Python interface to PVAccess protocol client
- [adafruit-circuitpython-requests](software-development-embedded-systems.md#adafruit-circuitpython-requests) - A requests-like library for web interfacing
- [django-filer](internet-www-http.md#django-filer) - A file management application for django that makes handling of files and images a breeze.
- [adafruit-circuitpython-typing](software-development-embedded-systems.md#adafruit-circuitpython-typing) - Types needed for type annotation that are not in `typing`
- [agent_governance_toolkit](scientific-engineering-artificial-intelligence.md#agent_governance_toolkit) - Public Preview — Unified installer and runtime policy enforcement for the Agent Governance Toolkit
- [adaptix](internet.md#adaptix) - An extremely flexible and configurable data model conversion library
- [django-robots](internet-www-http.md#django-robots) - Robots exclusion application for Django, complementing Sitemaps.
- [PySide2](database.md#pyside2) - Python bindings for the Qt cross-platform application and UI framework
- [adafruit-circuitpython-busdevice](software-development-embedded-systems.md#adafruit-circuitpython-busdevice) - CircuitPython bus device classes to manage bus sharing.
- [inputs](software-development-embedded-systems.md#inputs) - Cross-platform Python support for keyboards, mice and gamepads.
- [cidr-trie](internet.md#cidr-trie) - Store/search CIDR prefixes in a trie structure.
- [owlready2](scientific-engineering-artificial-intelligence.md#owlready2) - A package for ontology-oriented programming in Python: load OWL 2.0 ontologies as Python objects, modify them, save them, and perform reasoning via HermiT. Includes an optimized RDF quadstore.
- [dhooks-lite](communications-chat.md#dhooks-lite) - A wrapper for sending messages to Discord webhooks.
- [snowflake-id](software-development.md#snowflake-id) - The Snowflake generator done right
- [textcase](software-development.md#textcase) - Python library for text case conversions.
- [windows-curses](software-development.md#windows-curses) - Support for the standard curses module on Windows
- [rainflow](scientific-engineering-2.md#rainflow) - Implementation of ASTM E1049-85 rainflow cycle counting algorithm
- [flask-redis](internet-www-http.md#flask-redis) - A nice way to use Redis in your Flask app
- [python3-dtls](security-cryptography.md#python3-dtls) - Python Datagram Transport Layer Security
- [google-compute-engine](internet.md#google-compute-engine) - Google Compute Engine
- [litert-converter](scientific-engineering-2.md#litert-converter) - LiteRT is for mobile and embedded devices.
- [django-more-admin-filters](internet-www-http.md#django-more-admin-filters) - Additional filters for django-admin.
- [odc-loader](scientific-engineering-gis.md#odc-loader) - Tooling for constructing xarray objects from parsed metadata
- [django-slowtests](internet-www-http.md#django-slowtests) - locate your slowest tests
- [cerbos-sqlalchemy](security.md#cerbos-sqlalchemy) - SQLAlchemy adapter for generating queries with Cerbos: an open core, language-agnostic, scalable authorization solution
- [pyshorteners](internet-www-http.md#pyshorteners) - A Python lib to wrap and consume the most used shorteners APIs
- [django-defender](internet-www-http.md#django-defender) - redis based Django app that locks out users after too many failed login attempts.
- [adafruit-circuitpython-connectionmanager](software-development-embedded-systems.md#adafruit-circuitpython-connectionmanager) - A urllib3.poolmanager/urllib3.connectionpool-like library for managing sockets and connections
- [pkginfo2](software-development.md#pkginfo2) - Query metadata from sdists / bdists / installed packages. Safer fork of pkginfo to avoid doing arbitrary imports and eval.
- [quadrilateral-fitter](scientific-engineering-artificial-intelligence.md#quadrilateral-fitter) - QuadrilateralFitter is an efficient and easy-to-use Python library for fitting irregular quadrilaterals from irregular polygons or any noisy data.
- [earthaccess](software-development.md#earthaccess) - Client library for NASA Earthdata APIs
- [itk-core](scientific-engineering-2.md#itk-core) - ITK is an open-source toolkit for multidimensional image analysis
- [google-cloud-documentai-toolbox](internet.md#google-cloud-documentai-toolbox) - 
- [redis-data-structures](database.md#redis-data-structures) - Redis-backed data structures for building scalable and resilient applications
- [ydb-sqlglot-plugin](database.md#ydb-sqlglot-plugin) - YDB dialect plugin for sqlglot
- [codecarbon](scientific-engineering-artificial-intelligence.md#codecarbon) - Track and reduce the CO2 emissions of your computing
- [islpy](scientific-engineering-2.md#islpy) - Wrapper around isl, an integer set library
- [pylakekeeper](database.md#pylakekeeper) - Official Lakekeeper client — generic-tables API and OAuth2 auth (static token / client_credentials with refresh)
- [puhu](multimedia-graphics.md#puhu) - A modern, high-performance image processing library for Python, powered by Rust.
- [apiclient](internet-www-http-2.md#apiclient) - Framework for making good API client libraries using urllib3.
- [tensorflow-data-validation](scientific-engineering-2.md#tensorflow-data-validation) - A library for exploring and validating machine learning data.
- [itk-filtering](scientific-engineering-2.md#itk-filtering) - ITK is an open-source toolkit for multidimensional image analysis
- [bittensor-drand](scientific-engineering-2.md#bittensor-drand) - Rust-backed Python library for generating timelock-encrypted weight commitments for Bittensor's commit-reveal mechanism using drand randomness.
- [CMRESHandler](internet-log-analysis.md#cmreshandler) - Elasticsearch Log handler for the logging library
- [itk-numerics](scientific-engineering-2.md#itk-numerics) - ITK is an open-source toolkit for multidimensional image analysis
- [discord-protos](internet.md#discord-protos) - Discord user settings protobufs.
- [freeze-core](software-development-build-tools.md#freeze-core) - Core dependency for cx_Freeze
- [censys](documentation-sphinx.md#censys) - An easy-to-use and lightweight API wrapper for Censys APIs (censys.io).
- [click-extra](documentation-sphinx.md#click-extra) - 🌈 Drop-in replacement for Click to make user-friendly and colorful CLI
- [kubeflow](scientific-engineering-2.md#kubeflow) - Kubeflow Python SDK to manage ML workloads and to interact with Kubeflow APIs.
- [landlock](security.md#landlock) - Python interface to the Landlock Linux Security Module.
- [pyspelling](internet-www-http-2.md#pyspelling) - Spell checker.
- [scikit-bio](scientific-engineering-2.md#scikit-bio) - Data structures, algorithms and educational resources for bioinformatics.
- [pymorphy3-dicts-uk](scientific-engineering-information-analysis.md#pymorphy3-dicts-uk) - Ukrainian dictionaries for pymorphy3
- [igwn-ligolw](scientific-engineering-2.md#igwn-ligolw) - Python LIGO Light-Weight XML I/O Library
- [pipe](software-development.md#pipe) - Module enabling a sh like infix syntax (using pipes)
- [dipy](scientific-engineering-2.md#dipy) - Diffusion MRI Imaging in Python
- [backports.ssl](internet-www-http-2.md#backportsssl) - The Python 3.4 standard `ssl` module API implemented on top of pyOpenSSL
- [zhinst-core](scientific-engineering-2.md#zhinst-core) - Python API for Zurich Instruments Devices
- [django-post_office](communications-email.md#django-post_office) - A Django app to monitor and send mail asynchronously, complete with template support.
- [biom-format](scientific-engineering-bio-informatics.md#biom-format) - Biological Observation Matrix (BIOM) format
- [atif](scientific-engineering-artificial-intelligence.md#atif) - Pydantic models for the Agent Trajectory Interchange Format (ATIF v1.8).
- [lightly](scientific-engineering-2.md#lightly) - A deep learning package for self-supervised learning and world models
- [docplex](other-nonlisted-topic.md#docplex) - The IBM Decision Optimization CPLEX Modeling for Python
- [novita-sandbox](scientific-engineering-artificial-intelligence.md#novita-sandbox) - Novita Agent Sandbox SDK - Python library for Novita Agent Sandbox
- [datrie](scientific-engineering-information-analysis.md#datrie) - Super-fast, efficiently stored Trie for Python.
- [aiocoap](internet.md#aiocoap) - Python CoAP library
- [genie.telemetry](software-development-build-tools.md#genietelemetry) - Genie libs Telemetry: Genie Telemetry Libraries
- [vici](security.md#vici) - Native Python interface for strongSwan's VICI protocol
- [gs-madrona](multimedia-graphics.md#gs-madrona) - A fork from the official Madrona. The fork will be used for Genesis's own Madrona integration.
- [microsoft-agents-a365-runtime](scientific-engineering-artificial-intelligence.md#microsoft-agents-a365-runtime) - Telemetry, tracing, and monitoring components for AI agents
- [python-twitter](communications-chat.md#python-twitter) - A Python wrapper around the Twitter API
- [opensearch-logger](internet-log-analysis.md#opensearch-logger) - OpenSearch logging handler
- [pyblock-builder](software-development-documentation.md#pyblock-builder) - A lightweight Python library with a declarative syntax for simplifying building apps using Slack's Block Kit UI framework
- [microsoft-agents-a365-observability-core](scientific-engineering-artificial-intelligence.md#microsoft-agents-a365-observability-core) - Telemetry, tracing, and monitoring components for AI agents
- [genie.libs.robot](software-development-build-tools.md#genielibsrobot) - Genie libs Robot: RobotFramework libraries to interact with Genie
- [glpk](scientific-engineering-mathematics.md#glpk) - PyGLPK, a Python module encapsulating GLPK.
- [genie.trafficgen](software-development-build-tools.md#genietrafficgen) - Genie Library for traffic generator connection support
- [pyats.contrib](software-development-build-tools.md#pyatscontrib) - Open source package for pyATS framework extensions.
- [pyats.robot](software-development-build-tools.md#pyatsrobot) - pyATS Robot: Robot Module
- [ouster-sdk](scientific-engineering-2.md#ouster-sdk) - Ouster Sensor SDK
- [rtdl_num_embeddings](scientific-engineering-artificial-intelligence.md#rtdl_num_embeddings) - On Embeddings for Numerical Features in Tabular Deep Learning.
- [openvino-tokenizers](scientific-engineering-artificial-intelligence.md#openvino-tokenizers) - Convert tokenizers into OpenVINO models
- [coqui-tts](multimedia.md#coqui-tts) - Deep learning for Text to Speech.
- [rubric](education.md#rubric) - rubric
- [tensorflow-intel](scientific-engineering-2.md#tensorflow-intel) - TensorFlow is an open source machine learning framework for everyone.
- [pypresence](communications-chat.md#pypresence) - Discord RPC client written in Python
- [ydf](scientific-engineering-2.md#ydf) - YDF (short for Yggdrasil Decision Forests) is a library for training, serving, evaluating and analyzing decision forest models such as Random Forest and Gradient Boosted Trees.
- [fhirpathpy](internet-www-http-2.md#fhirpathpy) - FHIRPath implementation in Python
- [flytekitplugins-ray](scientific-engineering-2.md#flytekitplugins-ray) - This package holds the Ray plugins for flytekit
- [monotonic-alignment-search](multimedia-sound-audio.md#monotonic-alignment-search) - Monotonically align text and speech
- [lithops](scientific-engineering-2.md#lithops) - Run unmodified Python code at massive scale on any cloud, with no servers to manage
- [itk](scientific-engineering-2.md#itk) - ITK is an open-source toolkit for multidimensional image analysis
- [sharepoint-to-text](communications-email.md#sharepoint-to-text) - Text extraction library for typical file formats found in SharePoint repositories
- [dj-static](internet-www-http-2.md#dj-static) - Serve production static files with Django.
- [pypptx-with-oxml](office-business-office-suites.md#pypptx-with-oxml) - Create, read, and update PowerPoint 2007+ (.pptx) files.
- [whoisdomain](internet.md#whoisdomain) - Python package for retrieving WHOIS information of domains.
- [nvidia-matmul-heuristics](scientific-engineering-2.md#nvidia-matmul-heuristics) - NVIDIA Matmul Heuristics
- [streamlit-pdf](multimedia-graphics.md#streamlit-pdf) - A Streamlit component for viewing PDF files
- [notify2](desktop-environment.md#notify2) - Python interface to DBus notifications
- [itk-io](scientific-engineering-2.md#itk-io) - ITK is an open-source toolkit for multidimensional image analysis
- [twitter-ads](internet.md#twitter-ads) - A Twitter supported and maintained Ads API SDK for Python.
- [Pint-Pandas](scientific-engineering-2.md#pint-pandas) - Extend Pandas Dataframe with Physical quantities module
- [open-spiel](games-entertainment.md#open-spiel) - A Framework for Reinforcement Learning in Games
- [uniception](scientific-engineering-artificial-intelligence.md#uniception) - Generalizable Perception Stack for 3D, 4D, spatial AI and scene understanding
- [kerykeion](religion.md#kerykeion) - A Python library for astrological calculations, including natal charts, houses, planetary aspects, and SVG chart generation.
- [Flask-SSLify](internet-www-http-2.md#flask-sslify) - Force SSL on your Flask app.
- [coqui-tts-trainer](scientific-engineering-artificial-intelligence.md#coqui-tts-trainer) - General purpose model trainer for PyTorch that is more flexible than it should be, by 🐸Coqui.
- [nbtoolbelt](education.md#nbtoolbelt) - Tools to work with Jupyter notebooks
- [fabio](scientific-engineering-bio-informatics.md#fabio) - FabIO is an I/O library for images produced by 2D X-ray detectors and written in Python
- [babelfish](software-development-internationalization.md#babelfish) - A module to work with countries and languages
- [suitesparse-graphblas](scientific-engineering-2.md#suitesparse-graphblas) - SuiteSparse:GraphBLAS Python bindings.
- [ai](internet.md#ai) - AI Agent Framework for Python
- [guessit](multimedia.md#guessit) - GuessIt - a library for guessing information from video filenames.
- [websockets-proxy](internet-proxy-servers.md#websockets-proxy) - Connect to websockets through a proxy server.
- [skorch](scientific-engineering-2.md#skorch) - scikit-learn compatible neural network library for pytorch
- [decompyle3](software-development-debuggers.md#decompyle3) - Python cross-version byte-code decompiler
- [docarray](database-database-engines-servers.md#docarray) - The data structure for multimodal data
- [Flask-Cognito](internet-www-http-2.md#flask-cognito) - Authenticate users to Cognito user pool via JWT.
- [an](multimedia-graphics.md#an) - AI-driven structured animation in Python: scene.md to rendered video.
- [eyeD3](multimedia-sound-audio.md#eyed3) - Python audio data toolkit (ID3 and MP3)
- [django-admin-csvexport](internet-www-http-2.md#django-admin-csvexport) - Django-admin-action to export items as csv-formatted data.
- [pypolyline](scientific-engineering-gis.md#pypolyline) - Fast Google Polyline encoding and decoding using Rust
- [django-modeltree](internet-www-http-2.md#django-modeltree) - TODO
- [itk-segmentation](scientific-engineering-2.md#itk-segmentation) - ITK is an open-source toolkit for multidimensional image analysis
- [lightly-utils](scientific-engineering-2.md#lightly-utils) - A utility package for lightly
- [cirq-ionq](scientific-engineering-quantum-computing.md#cirq-ionq) - A Cirq package to simulate and connect to IonQ quantum computers
- [cpm-kernels](scientific-engineering-artificial-intelligence.md#cpm-kernels) - CPM CUDA kernels
- [django-cms](internet-www-http-2.md#django-cms) - Lean enterprise content management powered by Django.
- [nvidia-nvfatbin-cu12](scientific-engineering-2.md#nvidia-nvfatbin-cu12) - NVIDIA compiler library for fatbin interaction
- [pyIsEmail](communications-email.md#pyisemail) - Simple, robust email validation
- [pyap2](scientific-engineering-information-analysis.md#pyap2) - Pyap2 is a maintained fork of pyap, a regex-based library for parsing US, CA, and UK addresses. The fork adds typing support, handles more address formats and edge cases.
- [cirq](scientific-engineering-quantum-computing.md#cirq) - A framework for creating, editing, and invoking Noisy Intermediate Scale Quantum (NISQ) circuits.
- [pyrig](software-development-build-tools.md#pyrig) - A Python project setup and management tool built on infrastructure as code and convention over configuration.
- [strands-agents-builder](scientific-engineering-artificial-intelligence.md#strands-agents-builder) - An example Strands agent demonstrating streaming, tool use, and interactivity from your terminal. This agent builder can help you to build your own agents and tools.
- [custodian](scientific-engineering-chemistry.md#custodian) - A simple JIT job management framework in Python.
- [agentenv-framework](scientific-engineering-artificial-intelligence.md#agentenv-framework) - SDK and CLI for building, deploying and running agent environments and the tasks that grade agents in them.
- [tensorflow-recommenders](scientific-engineering-2.md#tensorflow-recommenders) - Tensorflow Recommenders, a TensorFlow library for recommender systems.
- [aspose-cad](office-business.md#aspose-cad) - Aspose.CAD for Python is a CAD and BIM drawings Processing library that allows developers to modify, convert and publish various drawing and image formats without need to have any other CAD software.
- [blendmodes](multimedia-graphics.md#blendmodes) - Use this module to apply a number of blending modes to a background and foreground image
- [mailgun2](communications-email.md#mailgun2) - A python client for Mailgun API v2
- [chematic](scientific-engineering-artificial-intelligence.md#chematic) - Pure-Rust cheminformatics — SMILES, fingerprints, 190+ descriptors, pKa, ADMET
- [pyroots](scientific-engineering-2.md#pyroots) - Pure python single variable function solvers
- [langfun](scientific-engineering-artificial-intelligence.md#langfun) - Langfun: Language as Functions.
- [skylos](security.md#skylos) - Python dead code, security and secrets scanner with a pull-request gate; narrower checks for TypeScript, Java and more.
- [tradingview-screener](software-development.md#tradingview-screener) - A package for creating stock screeners with the TradingView API
- [itk-registration](scientific-engineering-2.md#itk-registration) - ITK is an open-source toolkit for multidimensional image analysis
- [sec-parser](office-business-financial.md#sec-parser) - Parse SEC EDGAR HTML documents into a tree of elements that correspond to the visual structure of the document.
- [ha-ffmpeg](scientific-engineering-atmospheric-science.md#ha-ffmpeg) - A library that handling with ffmpeg for home-assistant
- [django-secured-fields](security-cryptography.md#django-secured-fields) - Django encrypted fields with search enabled.
- [matrx-scraper](internet-www-http-2.md#matrx-scraper) - Web scraping engine, HTML parsing, and search integration for the Matrx ecosystem
- [neptune](scientific-engineering-artificial-intelligence.md#neptune) - Neptune Client
- [rust-store-py](database.md#rust-store-py) - Python binding (PyO3) for the rust-store multi-backend data engine: GQL parsing, permissions, computed columns and SQL dialect translation for MongoDB, MySQL, SQLite and PostgreSQL
- [pyDOE3](education.md#pydoe3) - Design of experiments for Python
- [tensorflow-cpu-aws](scientific-engineering-2.md#tensorflow-cpu-aws) - TensorFlow is an open source machine learning framework for everyone.
- [interchange](software-development.md#interchange) - Data types and interchange formats
- [cent](internet-www-http-2.md#cent) - Python SDK for Centrifugo's HTTP server API: API client, tokens, proxy handlers
- [pgpq](software-development.md#pgpq) - Arrow -> PostgreSQL encoder
- [pansi](software-development.md#pansi) - Text mode rendering library
- [bagit-profile](communications-file-sharing.md#bagit-profile) - This module can be used to validate BagitProfiles.
- [cirq-google](scientific-engineering-quantum-computing.md#cirq-google) - The Cirq module that provides tools and access to the Google Quantum Computing Service
- [flytekitplugins-spark](scientific-engineering-2.md#flytekitplugins-spark) - Spark 3 plugin for flytekit
- [pydantic-factories](software-development.md#pydantic-factories) - Mock data generation for pydantic based models and python dataclasses
- [smartapi-python](office-business-financial.md#smartapi-python) - Angel Broking openApi integration
- [mcstatus](games-entertainment.md#mcstatus) - A library to query Minecraft Servers for their status and capabilities.
- [faiss-gpu](scientific-engineering-artificial-intelligence.md#faiss-gpu) - A library for efficient similarity search and clustering of dense vectors (GPU support).
- [st-theme](database-front-ends.md#st-theme) - A component that returns the active theme of the Streamlit app.
- [markdown-gfm-admonition](software-development-documentation.md#markdown-gfm-admonition) - GFM admonition syntax for Python Markdown
- [semble](scientific-engineering-artificial-intelligence.md#semble) - Fast and Accurate Code Search for Agents
- [basemap-data](scientific-engineering-visualization.md#basemap-data) - Data assets for matplotlib basemap
- [cloudml-hypertune](internet.md#cloudml-hypertune) - A library to report Google CloudML Engine HyperTune metrics.
- [wecom-aibot-sdk](communications-chat.md#wecom-aibot-sdk) - 企业微信智能机器人 Python SDK —— 基于 WebSocket 长连接通道
- [soco](home-automation.md#soco) - SoCo (Sonos Controller) is a simple library to control Sonos speakers.
- [django-citext](database.md#django-citext) - PostgreSQL CIText integration for Django.
- [xlcalculator](office-business-financial.md#xlcalculator) - Converts MS Excel formulas to Python and evaluates them.
- [pyrtcm](scientific-engineering-gis.md#pyrtcm) - RTCM3 protocol parser
- [desktop-notifier](communications.md#desktop-notifier) - Python library for cross-platform desktop notifications
- [zapros](internet-www-http-2.md#zapros) - Modern and extensible HTTP client for Python.
- [drf-api-logger](internet-www-http-2.md#drf-api-logger) - The production standard for DRF API observability: request/response logging, profiling, masking, and admin analytics.
- [recipe-scrapers](internet-www-http-2.md#recipe-scrapers) - Python package, scraping recipes from all over the internet
- [silx](scientific-engineering-physics.md#silx) - Silx tool-kit: collection of Python packages to support the development of data assessment, reduction and analysis applications at synchrotron radiation facilities
- [chalk-remote-call-python](scientific-engineering-artificial-intelligence.md#chalk-remote-call-python) - Chalk remote call Python runtime interface client
- [pykml](multimedia-graphics.md#pykml) - Python KML library
- [roc-validator](scientific-engineering-2.md#roc-validator) - A Python package to validate RO-Crates
- [pysentry-rs](security.md#pysentry-rs) - Security vulnerability auditing tool for Python packages
- [pydot-ng](scientific-engineering-visualization.md#pydot-ng) - Python interface to Graphviz's Dot
- [convertbng](scientific-engineering-gis.md#convertbng) - Fast lon, lat to and from ETRS89 and BNG (OSGB36) using the OS OSTN15 transform
- [netron](scientific-engineering-2.md#netron) - Viewer for neural network, deep learning and machine learning models.
- [flup](internet-www-http-2.md#flup) - Random assortment of WSGI servers (py3)
- [uwsgidecorators](internet-www-http-2.md#uwsgidecorators) - uwsgidecorators standalone package
- [tabulator](internet-www-http-2.md#tabulator) - Consistent interface for stream reading and writing tabular data (csv/xls/json/etc)
- [Hydrogram](communications.md#hydrogram) - Sleek, advanced, and asynchronous Telegram MTProto API framework in Python, designed for fluid user and bot interactions.
- [pyScss](software-development-code-generators.md#pyscss) - pyScss, a Scss compiler for Python
- [otio-fcp-adapter](multimedia-graphics.md#otio-fcp-adapter) - OpenTimelineIO FCP XML Adapter
- [djangocms-admin-style](internet-www-http-2.md#djangocms-admin-style) - Adds pretty CSS styles for the django CMS admin interface.
- [torch-npu](scientific-engineering-2.md#torch-npu) - NPU bridge for PyTorch
- [django-analytical](internet-www-http-2.md#django-analytical) - Analytics service integration for Django projects
- [geolib](scientific-engineering-gis.md#geolib) - A library for geohash encoding, decoding and associated functions
- [dash-auth](database-front-ends.md#dash-auth) - Dash Authorization Package.
- [pyhdb](database.md#pyhdb) - SAP HANA Database Client for Python
- [basemap](scientific-engineering-visualization.md#basemap) - Plot data on map projections with matplotlib
- [blacksheep](internet-www-http-2.md#blacksheep) - Fast web framework for Python asyncio
- [highcharts-core](internet-www-http-2.md#highcharts-core) - High-end Data Visualization for the Python Ecosystem. Official wrapper for Highcharts Core (JS).
- [ko-speech-tools](multimedia-sound-audio.md#ko-speech-tools) - Korean speech/NLP tools
- [python-xmp-toolkit](multimedia.md#python-xmp-toolkit) - XMP I/O wrapping Exempi
- [pymobiledetect](internet-www-http-2.md#pymobiledetect) - Detect mobile and tablet browsers
- [createsend](communications.md#createsend) - A library which implements the complete functionality of the Campaign Monitor API.
- [doppler-dsp](scientific-engineering-2.md#doppler-dsp) - Practical, portable, performant digital signal processing.
- [python-escpos](office-business-financial.md#python-escpos) - Python library to manipulate ESC/POS Printers
- [python-msilib](software-development-build-tools.md#python-msilib) - Read and write Microsoft Installer files
- [py3-wget](communications-file-sharing.md#py3-wget) - A tool to download files. It supports progress bar, cksum, timeout, retry failed download.
- [py2neo](database.md#py2neo) - Python client library and toolkit for Neo4j
- [ovrtx](multimedia-graphics.md#ovrtx) - Omniverse RTX
- [essentia](multimedia-sound-audio.md#essentia) - Library for audio and music analysis, description and synthesis
- [pylast](internet.md#pylast) - A Python interface to Last.fm and Libre.fm
- [socid-extractor](internet-www-http-2.md#socid-extractor) - Extract accounts' identifiers and metadata from personal pages on various platforms.
- [dns-lexicon](internet-name-service-dns.md#dns-lexicon) - Manipulate DNS records on various DNS providers in a standardized/agnostic way
- [neptune-scale](scientific-engineering-artificial-intelligence.md#neptune-scale) - A minimal client library
- [convex](database-front-ends.md#convex) - Python client for the reactive backend-as-a-service Convex.
- [anastruct](scientific-engineering-2.md#anastruct) - Finite element analysis of 2D structures
- [twython](communications-chat.md#twython) - Actively maintained, pure Python wrapper for the Twitter API. Supports both normal and streaming Twitter APIs
- [tensorflow-transform](scientific-engineering-2.md#tensorflow-transform) - A library for data preprocessing with TensorFlow
- [bitcoinlib](office-business-financial.md#bitcoinlib) - Bitcoin cryptocurrency Library
- [onetimepass](internet-www-http-2.md#onetimepass) - Module for generating and validating HOTP and TOTP tokens
- [pipestat](scientific-engineering-bio-informatics.md#pipestat) - A pipeline results reporter
- [Zope](internet-www-http-2.md#zope) - Zope application server / web framework
- [aiothreads](software-development.md#aiothreads) - glue between async and thread worlds
- [piper](scientific-engineering-bio-informatics.md#piper) - A lightweight python toolkit for gluing together restartable, robust command line pipelines
- [godot-ai](games-entertainment.md#godot-ai) - Production-grade MCP server and AI tools for the Godot engine
- [fortifyapi](software-development.md#fortifyapi) - Python library for Fortify Software Security Center (SSC) RESTFul API
- [PasteScript](internet-www-http-2.md#pastescript) - A pluggable command-line frontend, including commands to setup package file layouts
- [arxiv-mcp-server](scientific-engineering-2.md#arxiv-mcp-server) - A flexible arXiv search and analysis service with MCP protocol support
- [stravalib](scientific-engineering-2.md#stravalib) - A Python package that makes it easy to access and download data from the Strava V3 REST API.
- [deepfilternet](multimedia-sound-audio.md#deepfilternet) - Noise supression using deep filtering
- [simple-ddl-parser](software-development.md#simple-ddl-parser) - Simple DDL Parser to parse SQL & dialects like HQL, TSQL (MSSQL), Oracle, AWS Redshift, Snowflake, MySQL, PostgreSQL, etc ddl files to json/python dict with full information about columns: types, defaults, primary keys, etc.; sequences, alters, custom types & other entities from ddl.
- [lazydocs](documentation.md#lazydocs) - Generate markdown API documentation for Google-style Python docstring.
- [pytextrank](scientific-engineering-artificial-intelligence.md#pytextrank) - Python implementation of TextRank as a spaCy pipeline extension, for graph-based natural language work plus related knowledge graph practices; used for for phrase extraction of text documents.
- [linuxdoc](software-development-documentation.md#linuxdoc) - Sphinx-doc extensions & tools to extract documentation from C/C++ source file comments.
- [archivebox](internet-www-http-2.md#archivebox) - Self-hosted internet archiving solution.
- [Flask-Security](internet-www-http-2.md#flask-security) - Quickly add security features to your Flask application.
- [mmdr](multimedia-graphics.md#mmdr) - Fast native Mermaid diagram rendering (Rust-based, no browser required) with two backends: mermaid-rs-renderer and merman
- [featrixsphere](internet-www-http-2.md#featrixsphere) - Transform any CSV into a production-ready ML model in minutes, not months.
- [excelrd](office-business.md#excelrd) - Library for developers to extract data from Microsoft Excel (tm) spreadsheet files
- [WTForms-Components](internet-www-http-2.md#wtforms-components) - Additional fields, validators and widgets for WTForms.
- [xbbg](office-business-financial.md#xbbg) - Independent client for Bloomberg-connected data workflows
- [python-coveralls](internet-www-http-2.md#python-coveralls) - Python interface to coveralls.io API
- [pymatreader](scientific-engineering-2.md#pymatreader) - Convenient reader for Matlab mat files
- [mpyq](games-entertainment-real-time-strategy.md#mpyq) - A Python library for extracting MPQ (MoPaQ) files.
- [formualizer](office-business-financial.md#formualizer) - Embeddable spreadsheet engine — parse, evaluate & mutate Excel workbooks at native speed
- [pyan3](software-development.md#pyan3) - Generate approximate call graphs for Python programs
- [mplib](education.md#mplib) - A lightweight motion planning library
- [PyCifRW](scientific-engineering-bio-informatics.md#pycifrw) - CIF/STAR file support for Python
- [pyrabbit2](internet-www-http-2.md#pyrabbit2) - A Pythonic interface to the RabbitMQ Management HTTP API
- [pyatv](home-automation.md#pyatv) - A client library for Apple TV and AirPlay devices
- [defcon](multimedia-graphics.md#defcon) - A set of flexible objects for representing UFO data.
- [ufo2ft](multimedia-graphics.md#ufo2ft) - A bridge between UFOs and FontTools.
- [shinyswatch](internet-www-http-2.md#shinyswatch) - Bootswatch + Bootstrap 5 themes for Shiny.
- [nemo-gym](scientific-engineering-2.md#nemo-gym) - NeMo Gym is a library for building reinforcement learning environments
- [sqlalchemy-file](database.md#sqlalchemy-file) - SQLAlchemy-file is a SQLAlchemy extension for attaching files to SQLAlchemy model and uploading them to various storage.
- [toxiproxy-python](software-development.md#toxiproxy-python) - Python library for Toxiproxy
- [shioaji](office-business-financial.md#shioaji) - Shioaji — cross-language, cross-platform universal trading API. Native Python bindings, HTTP API with SSE streaming, standalone CLI, and a visual dashboard.
- [guacamole](software-development.md#guacamole) - Guacamole is an command line tool library for Python
- [genpy](scientific-engineering-2.md#genpy) - AST-based generation of Python source code
- [libpci](software-development.md#libpci) - Pure-Python, high-level bindings to libpci
- [persista](scientific-engineering-2.md#persista) - library for persisting and caching data
- [clize](software-development.md#clize) - Turn functions into command-line interfaces
- [starlette-graphene3](internet-www-http-2.md#starlette-graphene3) - Use Graphene v3 on Starlette
- [crowdypy](games-entertainment.md#crowdypy) - Official Python SDK for Crowded Kingdoms: typed GraphQL clients and a native UDP replication core
- [scann](scientific-engineering-mathematics.md#scann) - Scalable Nearest Neighbor search library
- [flwr](scientific-engineering-2.md#flwr) - Flower: A Friendly Federated AI Framework
- [roboto-mcap-codec](scientific-engineering-2.md#roboto-mcap-codec) - Decodes one channel of an MCAP file (ROS, DDS/IDL, JSON or MessagePack messages) into Apache Arrow, and single messages into Python objects.
- [TikTokLive](communications-chat.md#tiktoklive) - Unofficial TikTok LIVE API for Python: real-time chat, gift, like, follow and viewer events from any TikTok livestream.
- [trendspy](internet.md#trendspy) - A Python library for accessing Google Trends data
- [pyversity](scientific-engineering-artificial-intelligence.md#pyversity) - Fast Diversification for Search & Retrieval
- [shiboken2](database.md#shiboken2) - Python / C++ bindings helper module
- [Kurigram](communications.md#kurigram) - Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots
- [pysqlsync](database-database-engines-servers.md#pysqlsync) - Synchronize schema and large volumes of data
- [discord.py-self](internet.md#discordpy-self) - A Python wrapper for the Discord user API
- [xtgeo](scientific-engineering-2.md#xtgeo) - XTGeo is a Python library for 3D grids, surfaces, wells, etc
- [sweetviz](scientific-engineering-visualization.md#sweetviz) - A pandas-based library to visualize and compare datasets.
- [basicauth](internet-www-http-2.md#basicauth) - An incredibly simple HTTP basic auth implementation.
- [pygerduty](software-development.md#pygerduty) - Python Client Library for PagerDuty's REST API
- [meeko](scientific-engineering-bio-informatics.md#meeko) - Python package for preparing small molecule for docking
- [fabric2](software-development.md#fabric2) - High level SSH command execution
- [mistralai-agents](scientific-engineering-artificial-intelligence.md#mistralai-agents) - Mistral Agents SDK - build and serve agents in Python
- [qiskit-connector](scientific-engineering-2.md#qiskit-connector) - Quantum Computing Qiskit Connector For Quantum Backend Use In Realtime
- [pyaedt](scientific-engineering-electronic-design-automation-eda.md#pyaedt) - High-level Python API for Ansys Electronics Desktop Framework
- [flask-weasyprint](internet-www-http-2.md#flask-weasyprint) - Make PDF in your Flask app with WeasyPrint
- [speechmatics-batch](multimedia-sound-audio.md#speechmatics-batch) - Speechmatics Batch API Client
- [pyPEG2](software-development-compilers.md#pypeg2) - An intrinsic PEG Parser-Interpreter for Python
- [pybboxes](education.md#pybboxes) - Light Weight Toolkit for Bounding Boxes
- [dnsdb2](internet-name-service-dns.md#dnsdb2) - Client for DNSDB API version 2 with Flexible Search
- [django-request-id](software-development.md#django-request-id) - Augment each request with unique id for logging purposes
- [tensorflow-gpu](scientific-engineering-2.md#tensorflow-gpu) - Removed: please install "tensorflow" instead.
- [fastapi-slim](internet.md#fastapi-slim) - FastAPI framework, high performance, easy to learn, fast to code, ready for production
- [tilt-mcp](software-development-build-tools.md#tilt-mcp) - Model Context Protocol server for Tilt - interact with Tilt resources through MCP
- [pymgclient](database.md#pymgclient) - Memgraph database adapter for Python language
- [postmark-python](communications-email.md#postmark-python) - The Official Postmark Python SDK.
- [yubico-client](security.md#yubico-client) - Library for verifying Yubikey One Time Passwords (OTPs)
- [pyubx2](scientific-engineering-gis.md#pyubx2) - UBX protocol parser and generator
- [flask-prometheus-metrics](internet.md#flask-prometheus-metrics) - Prometheus Metrics for Flask Web App
- [docculus](scientific-engineering-2.md#docculus) - Library for LangChain documents
- [Flask-BabelEx](internet-www-http-2.md#flask-babelex) - Adds i18n/l10n support to Flask applications
- [postal](internet-www-http-2.md#postal) - Python bindings to libpostal for fast international address parsing/normalization
- [fastapi-distributed-websocket](software-development.md#fastapi-distributed-websocket) - Large scale WebSocket with FastAPI
- [dbt-vertica](database.md#dbt-vertica) - Official vertica adapter plugin for dbt (data build tool)
- [wren-core-py](database.md#wren-core-py) - Python bindings for Wren Engine semantic layer (wren-core)
- [sphinxcontrib-typer](documentation.md#sphinxcontrib-typer) - Auto generate docs for typer commands.
- [rlax](scientific-engineering-artificial-intelligence.md#rlax) - A library of reinforcement learning building blocks in JAX.
- [otio-cmx3600-adapter](multimedia-graphics.md#otio-cmx3600-adapter) - OpenTimelineIO CMX 3600 EDL Adapter
- [executorch](scientific-engineering-2.md#executorch) - On-device AI across mobile, embedded and edge for PyTorch
- [aspose-diagram-python](multimedia-graphics.md#aspose-diagram-python) - Aspose.Diagram for Python via .NET is a scalable and feature-rich API to process visio files using Python. API offers Visio file creation, manipulation, conversion and rendering. Developers can format pages to the most granular level, create and manipulate shape, render pages, shapes to PDF and images, and much more - all without any dependency on Microsoft Office or Visio application.
- [cirq-web](scientific-engineering-quantum-computing.md#cirq-web) - Web-based 3D visualization tools for Cirq.
- [cirq-pasqal](scientific-engineering-quantum-computing.md#cirq-pasqal) - A Cirq package to simulate and connect to Pasqal quantum computers
- [booleanOperations](multimedia-graphics.md#booleanoperations) - Boolean operations on paths.
- [cirq-aqt](scientific-engineering-quantum-computing.md#cirq-aqt) - A Cirq package to simulate and connect to Alpine Quantum Technologies quantum computers
- [django-pgware](database.md#django-pgware) - PostgreSQL utilities for Django: advisory locks, GUC management, and logging suppression
- [aioauth](internet.md#aioauth) - Asynchronous OAuth 2.0 framework for Python 3.
- [fastapi-redis-sdk](database.md#fastapi-redis-sdk) - The official Redis integration with FastAPI
- [matrx-rag](scientific-engineering-information-analysis.md#matrx-rag) - Multi-tenant RAG: hybrid retrieval, chunking, embeddings, ingestion, PDF + image + repo pipelines, agent-extraction indexing, priority-aware ranking.
- [hdf5storage](database.md#hdf5storage) - Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files.
- [supertonic](multimedia-sound-audio.md#supertonic) - High-quality Text-to-Speech synthesis with ONNX Runtime
- [pyexcel-webio](internet-www-http-2.md#pyexcel-webio) - A generic request and response interface for pyexcel web extensions.
- [pyocclient](internet-www-http-2.md#pyocclient) - Python client library for ownCloud
- [galileo-core](scientific-engineering-artificial-intelligence.md#galileo-core) - 
- [lytekit](scientific-engineering-2.md#lytekit) - Latch fork of Flyte SDK for Python
- [django-session-security](internet-www-http-2.md#django-session-security) - Client and server side session timeout with warnings
- [commit-check](software-development-build-tools.md#commit-check) - Commit policy as code for teams and AI agents: check commit messages, branch names, authors, tags, files and AI attribution.
- [ha-garmin](internet-www-http-2.md#ha-garmin) - Python client for Garmin Connect API
- [requests-async](internet-www-http-2.md#requests-async) - Simple async HTTP client with requests-like interface, powered by httpx
- [django-tenant-users](internet-www-http-2.md#django-tenant-users) - A Django app to extend django-tenants to incorporate global multi-tenant users
- [generic-connection-pool](database.md#generic-connection-pool) - generic connection pool
- [django-private-storage](internet-www-http-2.md#django-private-storage) - Private media file storage for Django projects
- [httplib2shim](internet.md#httplib2shim) - A wrapper over urllib3 that matches httplib2's interface
- [djust](internet-www-http-2.md#djust) - Phoenix LiveView-style reactive components for Django with Rust-powered performance. Real-time UI updates over WebSocket, no JavaScript build step required.
- [cpex](scientific-engineering-artificial-intelligence.md#cpex) - CPEX - ContextForge Plugin Extensibility Framework
- [pywidevine](multimedia-video.md#pywidevine) - Widevine CDM (Content Decryption Module) implementation in Python.
- [feedgenerator](internet-www-http-2.md#feedgenerator) - Standalone version of django.utils.feedgenerator
- [autogen](software-development.md#autogen) - A programming framework for agentic AI
- [fingerprint-pro-server-api-sdk](security.md#fingerprint-pro-server-api-sdk) - This version of SDK is marked as deprecated. Please follow our [migration guide](https://dev.fingerprint.com/reference/migrating-from-server-api-v3-to-v4) to migrate. Fingerprint Server API allows you to search, update, and delete identification events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.
- [slack-blocks-markdown](communications-chat.md#slack-blocks-markdown) - Convert Markdown to Slack Block Kit blocks using mistletoe
- [yandex-cli](office-business.md#yandex-cli) - Interact with Yandex 360 services (Wiki, Tracker, Forms, …) from a CLI, an MCP server, or a Python SDK.
- [pydsdl](scientific-engineering-2.md#pydsdl) - Cyphal DSDL processing frontend
- [uptime-kuma-api-v2](internet-www-http-2.md#uptime-kuma-api-v2) - A python wrapper for the Uptime Kuma WebSocket API
- [lytekitplugins-pods](scientific-engineering-2.md#lytekitplugins-pods) - Flytekit plugin to support K8s Pod tasks
- [pyexcel-ezodf](office-business.md#pyexcel-ezodf) - A Python package to create/manipulate OpenDocumentFormat files
- [microsandbox](security.md#microsandbox) - Python SDK for microsandbox — secure, fast microVM-based sandboxing.
- [PyLink](internet.md#pylink) - Universal communication interface using File-Like API
- [zhinst-comms](scientific-engineering-2.md#zhinst-comms) - Zurich Instruments internal python bindings for Capnp
- [btclib-secp256k1](scientific-engineering-2.md#btclib-secp256k1) - Simple python bindings to libsecp256k1
- [endesive](communications-email.md#endesive) - Digital signatures for PDF, S/MIME, XML (XAdES), and CMS in Python.
- [axioms-fastapi](security.md#axioms-fastapi) - OAuth2/OIDC authentication and authorization for FastAPI APIs
- [otio-aaf-adapter](multimedia-video.md#otio-aaf-adapter) - OpenTimelineIO AAF Adapter
- [pulsar-relay-client](internet-www-http-2.md#pulsar-relay-client) - Client library for the pulsar-relay HTTP wire contract (auth, transport, device flow, topic management)
- [bourbaki.application](software-development-code-generators.md#bourbakiapplication) - CLIs derived directly from type signatures and docstrings years before typer existed
- [nunavut](scientific-engineering-2.md#nunavut) - Generate code from DSDL using Jinja2 templates.
- [hexor](internet-www-http-2.md#hexor) - Coloring texts and their backgrounds in command line interface (cli), with rgb or hex types.
- [uiprotect](software-development-build-tools.md#uiprotect) - Python API for Unifi Protect (Unofficial)
- [django-invitations](internet.md#django-invitations) - Generic invitations app with support for django-allauth
- [fontMath](multimedia-graphics.md#fontmath) - A set of objects for performing math operations on font data.
- [histomicstk](scientific-engineering-artificial-intelligence.md#histomicstk) - A Python toolkit for Histopathology Image Analysis
- [mistralai-otel-observability](scientific-engineering-artificial-intelligence.md#mistralai-otel-observability) - OTLP-first Mistral AI observability SDK
- [otio-fcpx-xml-adapter](multimedia-graphics.md#otio-fcpx-xml-adapter) - OpenTimelineIO FCP X XML Adapter
- [Fabric3](software-development.md#fabric3) - Fabric is a simple, Pythonic tool for remote execution and deployment (py2.7/py3.4+ compatible fork).
- [bourbaki.introspection](software-development-code-generators.md#bourbakiintrospection) - Introspection utilities for Python: types, signatures, objects, docstrings, and more
- [Flask-SeaSurf](internet-www-http-2.md#flask-seasurf) - An updated CSRF extension for Flask.
- [drf-recaptcha](internet-www-http-2.md#drf-recaptcha) - Django rest framework recaptcha field serializer
- [stftpitchshift](artistic-software.md#stftpitchshift) - STFT based pitch and timbre shifting
- [pyrabbit](internet-www-http-2.md#pyrabbit) - A Pythonic interface to the RabbitMQ Management HTTP API
- [openvino-genai](scientific-engineering-artificial-intelligence.md#openvino-genai) - Library of the most popular Generative AI model pipelines, optimized execution methods, and samples
- [pyturso](database.md#pyturso) - Turso is an in-process SQL database written in Rust, compatible with SQLite.
- [rfc3161ng](communications.md#rfc3161ng) - Python implementation of the RFC3161 specification, using pyasn1
- [wrapper-tls-requests](internet-www-http-2.md#wrapper-tls-requests) - A powerful and lightweight Python library for making secure and reliable HTTP/TLS fingerprint requests.
- [sphinxcontrib-django](internet-www-http-2.md#sphinxcontrib-django) - Improve the Sphinx autodoc for Django classes.
- [django-prose-editor](internet-www-http-2.md#django-prose-editor) - Prose editor for the Django admin based on ProseMirror
- [cosmpy](software-development.md#cosmpy) - A library for interacting with the cosmos networks
- [djangocms-text-ckeditor](internet-www-http-2.md#djangocms-text-ckeditor) - Text Plugin for django CMS with CKEditor support
- [supervisely](scientific-engineering-artificial-intelligence.md#supervisely) - Supervisely Python SDK.
- [easydev](scientific-engineering-bio-informatics.md#easydev) - Common utilities to ease development of Python packages
- [sqlalchemy-searchable](internet-www-http-2.md#sqlalchemy-searchable) - Provides fulltext search capabilities for declarative SQLAlchemy models.
- [jumpssh](software-development.md#jumpssh) - Python library for remote ssh calls through a gateway.
- [WSME](internet-www-http-2.md#wsme) - Simplify the writing of REST APIs, and extend them with additional protocols.
- [flup-py3](internet-www-http-2.md#flup-py3) - Random assortment of WSGI servers
- [djangocms-attributes-field](internet-www-http-2.md#djangocms-attributes-field) - Adds attributes to Django models.
- [tsdb](scientific-engineering-artificial-intelligence.md#tsdb) - TSDB (Time Series Data Beans): a Python toolbox helping load 172 open-source time-series datasets
- [python-vxi11](scientific-engineering-interface-engine-protocol-translator.md#python-vxi11) - Python VXI-11 driver for controlling instruments over Ethernet
- [flask-mongoengine](internet-www-http-2.md#flask-mongoengine) - Flask-MongoEngine is a Flask extension that provides integration with MongoEngine and WTF model forms.
- [PyCampbellCR1000](internet.md#pycampbellcr1000) - Communication tools for Campbell CR1000-type Dataloggers
- [cachekit](database-database-engines-servers.md#cachekit) - Backend-agnostic caching for Python — intent-based decorators with circuit breaker, distributed locking, Prometheus metrics, and optional zero-knowledge AES-256-GCM encryption, on a Rust-powered core. Zero-config L1 in-memory; scales to Redis, Memcached, File, or CachekitIO.
- [tastytrade](internet-www-http-2.md#tastytrade) - An unofficial, typed, asynchronous Python SDK for Tastytrade!
- [instana](internet-www-http-2.md#instana) - Python Distributed Tracing & Metrics Sensor for Instana.
- [tinyhtml](internet-www-http-2.md#tinyhtml) - A tiny library to safely render compact HTML5 from Python expressions.
- [open3d-cpu](education.md#open3d-cpu) - Open3D: A Modern Library for 3D Data Processing.
- [specutils](scientific-engineering-astronomy.md#specutils) - Package for spectroscopic astronomical data
- [distconfig3](internet.md#distconfig3) - Library to manage configuration using Zookeeper, Etcd, Consul
- [Flask-JSON](internet-www-http-2.md#flask-json) - Better JSON support for Flask
- [django-crequest](software-development.md#django-crequest) - Middleware that makes the current request available from anywhere.
- [Flask-QRcode](internet-www-http-2.md#flask-qrcode) - A concise Flask extension to render QR codes on Jinja2 templates using python-qrcode
- [dcor](scientific-engineering-mathematics.md#dcor) - dcor: distance correlation and energy statistics in Python.
- [odmantic](database.md#odmantic) - ODMantic, an AsyncIO MongoDB Object Document Mapper for Python using type hints
- [pilgram](multimedia-graphics.md#pilgram) - library for instagram filters
- [metatensor-core](scientific-engineering-2.md#metatensor-core) - Python bindings for metatensor
- [SpiffWorkflow](other-nonlisted-topic.md#spiffworkflow) - A workflow framework and BPMN/DMN Processor
- [WTForms-Alchemy](internet-www-http-2.md#wtforms-alchemy) - Generates WTForms forms from SQLAlchemy models.
- [tablescope](scientific-engineering-information-analysis.md#tablescope) - A lazy table viewer with narwhals-backed query pushdown, for Marimo or Juptyer
- [fastapi-guard](internet-www-http-2.md#fastapi-guard) - Production-ready security middleware for FastAPI — IP filtering, rate limiting, penetration detection, and 20+ per-route security decorators.
- [django-multiupload](internet-www-http-2.md#django-multiupload) - Dead simple drop-in multi file upload field for django forms using HTML5's multiple attribute.
- [pytango](scientific-engineering-2.md#pytango) - Python bindings for the cppTango library; part of the Tango Distributed Control System toolkit
- [pymetis](multimedia-graphics.md#pymetis) - A graph partitioning package
- [torch-xla](scientific-engineering-artificial-intelligence.md#torch-xla) - XLA bridge for PyTorch
- [pyvirtualcam](multimedia-video.md#pyvirtualcam) - Send frames to a virtual camera
- [Scweet](internet-www-http-2.md#scweet) - Scrape tweets, profiles, followers and more from Twitter/X — no API key needed
- [vulkan](multimedia-graphics.md#vulkan) - Ultimate Python binding for Vulkan API
- [dcc-mcp-core](multimedia-graphics.md#dcc-mcp-core) - Foundational library for the DCC Model Context Protocol (MCP) ecosystem
- [FastAPI-SQLAlchemy](internet-www-http-2.md#fastapi-sqlalchemy) - Adds simple SQLAlchemy support to FastAPI
- [enzyme](multimedia-video.md#enzyme) - Video metadata parser
- [pytracking](communications-email.md#pytracking) - Email open and click tracking
- [tensorflow-io-nightly](scientific-engineering-2.md#tensorflow-io-nightly) - TensorFlow IO
- [launchdarkly-server-sdk-otel](software-development.md#launchdarkly-server-sdk-otel) - LaunchDarkly SDK OpenTelemetry integration
- [mnn](scientific-engineering-2.md#mnn) - C methods for MNN Package
- [returnn](scientific-engineering-2.md#returnn) - The RWTH extensible training framework for universal recurrent neural networks
