# Software Development / Libraries (part 3 of 5)

[Index](README.md) · 1884 packages in this topic, 1694 more listed under another topic, by downloads.

[part 1](software-development-libraries.md) · [part 2](software-development-libraries-2.md) · part 3 · [part 4](software-development-libraries-4.md) · [part 5](software-development-libraries-5.md)

### label-studio-sdk

(no summary)

`pip install label-studio-sdk` · installs (wheel) · licence: not stated · rank 6716 · last release 2026-11-05 · [PyPI](https://pypi.org/project/label-studio-sdk/) · [source](https://github.com/HumanSignal/label-studio-sdk)

<details><summary>README extract</summary>

The Label Studio Python Library provides convenient access to the Label Studio API from applications written in Python.
<!-- End Title -->

<!-- Outline -->

Explore the Label Studio API documentation here.

Example:
```python
from label_studio_sdk import LabelStudio

client = LabelStudio(
    base_url='YOUR_LABEL_STUDIO_URL',
    api_key="YOUR_API_KEY",
)
```

Sections: Label Studio Python Library, Documentation, Usage, CLI, Running the CLI with uv, Interface CLI, Versions, SDK 2.0.0, Enhancements, Breaking changes, SDK 1.0+, SDK <1, Example: Create a new project with tasks

</details>

### DateTimeRange

DateTimeRange is a Python library to handle a time range. e.g. check whether a time is within the time range, get the intersection of time ranges, truncate a time range, iterate through a time range, and so forth.

`pip install DateTimeRange` · installs (wheel) · licence: MIT License · rank 6717 · last release 2025-11-14 · [PyPI](https://pypi.org/project/DateTimeRange/) · [docs](https://datetimerange.rtfd.io/) · [source](https://github.com/thombashi/DateTimeRange)

<details><summary>README extract</summary>

DateTimeRange is a Python library to handle a time range. e.g. check whether a time is within the time range, get the intersection of time ranges, truncate a time range, iterate through a time range, and so forth.

Features:
Features of `DateTimeRange` class include:

 - Equation
 - Addition
 - Subtraction
 - Intersection
 - Union
 - Contains
 - Truncate
 - Split
 - Iteration
- Timezone support
- Daylight saving time support

...

</details>

### Redis-Sentinel-Url

A factory for redis connection that supports using Redis Sentinel

`pip install Redis-Sentinel-Url` · installs (wheel) · licence: Apache Software License · rank 6722 · last release 2017-04-05 · [PyPI](https://pypi.org/project/Redis-Sentinel-Url/)

<details><summary>README extract</summary>

Redis-Sentinel-Url provides parser and connection factory for `redis://` and `redis+sentinel://` URLs (the latter
being defined by this package).

* Supports Python 2.7 and 3.3+
* Licensed using Apache License 2.0

Example:
```python
import redis_sentinel_url

sentinel, client = redis_sentinel_url.connect('redis://localhost/0')
# None, StrictRedis(...)

sentinel, client = redis_sentinel_url.connect('rediss://localhost/0')
# None, StrictRedis(...)

sentinel, client = redis_sentinel_url.connect('unix://[:password]@/path/to/socket.sock?db=0')
# None, StrictRedis(...)

...
```

Sections: Redis-Sentinel-Url, URL scheme for connecting via Sentinel, Basic usage

</details>

### django-autoslug

An automated slug field for Django.

`pip install django-autoslug` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 6728 · last release 2023-04-03 · [PyPI](https://pypi.org/project/django-autoslug/)

_README extract left out: share-alike licence._

### xmhuffman

Cython bindings for Microsoft xVelocity/Vertipaq canonical-Huffman string decoding

`pip install xmhuffman` · installs (wheel) · licence: MIT License · rank 6731 · last release 2026-10-15 · [PyPI](https://pypi.org/project/xmhuffman/)

<details><summary>README extract</summary>

A small, fast Cython extension that decodes the canonical-Huffman string
dictionary pages used by xVelocity / Vertipaq column stores — the storage
format inside Power BI `.pbix` files (the `DataModel` part) and Excel
Power Pivot workbooks (`xl/model/item.data`).

Provides a tight C kernel for what would otherwise be a per-symbol Python
loop. ...

Example:
```python
import xmhuffman

# All inputs come straight from the Vertipaq dictionary page metadata:
# bitstream  — compressed_string_buffer (bytes)
# encode_array_128 — 128-byte nibble-packed code-length array
# offsets    — per-string start bit offsets (sequence of u32)
# total_bits — store_total_bits (end of last string)
...
```

...

</details>

### single-source

Access to the project version in Python code for PEP 621-style projects

`pip install single-source` · installs (wheel) · licence: MIT License · rank 6738 · last release 2024-06-11 · [PyPI](https://pypi.org/project/single-source/) · [source](https://github.com/rabbit72/single-source.git)

<details><summary>README extract</summary>

> `single-source` helps to reduce the entropy in your Python project by keeping
> single source of truth.

The targets of this library are modern Python projects which want to have
one source of truth for version, name and etc.

At the moment, the library provides the single point for a package version.

It supports Python 3.8+.

Example:
```python
# root_package/init.py
from pathlib import Path
from single_source import get_version

version = get_version(name, Path(file).parent.parent)
```

Sections: Single-source: There is only one truth, Quick start, Root of the problem, Advanced usage, Changing default value, Raising an exception, Not only pyproject.toml

</details>

### aiobreaker

Python implementation of the Circuit Breaker pattern.

`pip install aiobreaker` · installs (wheel) · licence: BSD License · rank 6744 · last release 2021-05-17 · [PyPI](https://pypi.org/project/aiobreaker/)

<details><summary>README extract</summary>

aiobreaker is a Python implementation of the Circuit Breaker pattern,
described in Michael T. Nygard's book `Release It!`_.

Circuit breakers exist to allow one subsystem to fail without destroying
the entire system. ...

</details>

### flake8-use-fstring

Flake8 plugin for string formatting style.

`pip install flake8-use-fstring` · installs from source (sdist only) · licence: MIT License · rank 6755 · last release 2022-07-27 · [PyPI](https://pypi.org/project/flake8-use-fstring/)

### jsonschema-pydantic-converter

Convert JSON Schema definitions to Pydantic models dynamically at runtime

`pip install jsonschema-pydantic-converter` · installs (wheel) · licence: Apache Software License · rank 6756 · last release 2026-08-31 · [PyPI](https://pypi.org/project/jsonschema-pydantic-converter/) · [source](https://github.com/akshaylive/jsonschema-pydantic-converter)

<details><summary>README extract</summary>

Convert JSON Schema definitions to Pydantic models dynamically at runtime.

Features:
`jsonschema-pydantic-converter` is a Python library that transforms JSON Schema dictionaries into Pydantic v2 models. This is useful when you need to work with dynamic schemas, validate data against JSON Schema specifications, or bridge JSON ...

Example:
```python
from jsonschema_pydantic_converter import transform

# Define a JSON Schema
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "description": "User's name"},
        "age": {"type": "integer", "description": "User's age"},
        "email": {"type": "string"}
    },
    "required": ["name", "age"]
}

...
```

...

</details>

### textile

Textile processing for python.

`pip install textile` · installs (wheel) · licence: BSD License · rank 6759 · last release 2026-05-10 · [PyPI](https://pypi.org/project/textile/) · [source](https://github.com/textile/python-textile.git)

<details><summary>README extract</summary>

python-textile is a Python port of Textile, Dean Allen’s humane web text generator.

Example:
```python
import textile
>>> s = """
... _This_ is a *test.*
...
... * One
... * Two
... * Three
...
... Link to "Slashdot":
... """
>>> html = textile.textile(s)
>>> print html
<p><em>This</em> is a <strong>test.</strong></p>

<ul>
    <li>One</li>
    <li>Two</li>
    <li>Three</li>
</ul>

<p>Link to <a href="
>>>
```

Sections: python-textile, Usage, Notes, Running Tests

</details>

### pytest-spark

pytest plugin to run the tests with support of pyspark.

`pip install pytest-spark` · installs (wheel) · licence: MIT License · rank 6766 · last release 2025-05-21 · [PyPI](https://pypi.org/project/pytest-spark/)

<details><summary>README extract</summary>

pytest plugin to run the tests with support of pyspark (Apache Spark).

This plugin will allow to specify `SPARK_HOME` directory in `pytest.ini`
and thus to make "pyspark" importable in your tests which are executed
by pytest. ...

Example:
```python
def test_my_case(spark_context):
    test_rdd = spark_context.parallelize([1, 2, 3, 4])
    # ...
```

Sections: pytest-spark, Usage, Set Spark location, Customize spark_options, Using the `spark_context` fixture, Using the `spark_session` fixture (Spark 2.0 and above), Using `spark_session` fixture with Spark Connect, Tests

</details>

### qualname

__qualname__ emulation for older Python versions

`pip install qualname` · installs from source (sdist only) · licence: BSD License · rank 6772 · last release 2015-04-11 · [PyPI](https://pypi.org/project/qualname/)

<details><summary>README extract</summary>

Python module to emulate the `qualname` attribute for classes and methods
(Python 3.3+) in older Python versions. See PEP 3155_ for details.


Example:
```python
class C:
    def f():
        pass

    class D:
        def g():
            pass
```

Sections: qualname, Usage, How does it work?, Feedback? Issues?

</details>

### fissix

Monkeypatches to override default behavior of lib2to3.

`pip install fissix` · installs (wheel) · licence: Python Software Foundation License · rank 6788 · last release 2026-10-30 · [PyPI](https://pypi.org/project/fissix/) · [source](https://github.com/amyreese/fissix)

<details><summary>README extract</summary>

Backport of latest lib2to3, with enhancements.

Installation

`pip3 install fissix` or `pip install fissix`, depending on the
operating system's Python policy. On Debian ≥11 and derivatives such
as Ubuntu 21.04, `sudo apt install python3-fissix`.

License

fissix is licensed under the Python Software Foundation License Version 2. ...

</details>

### ghostscript

Interface to the Ghostscript C-API, both high- and low-level, based on ctypes

`pip install ghostscript` · installs (wheel) · licence: GPL-3.0-or-later · rank 6789 · last release 2025-05-28 · [PyPI](https://pypi.org/project/ghostscript/)

_README extract left out: share-alike licence._

### local-crontab

Convert local crontabs to UTC crontabs

`pip install local-crontab` · installs (wheel) · licence: MIT License · rank 6796 · last release 2021-07-09 · [PyPI](https://pypi.org/project/local-crontab/)

<details><summary>README extract</summary>

local-crontab is a Python wheel and command line utility to convert a crontab, in a local timezone, into a set of UTC crontabs.
It creates multiple UTC crontabs because of Daylight Saving Time.

This project is based to local-crontab by UnitedIncome with some bug fixes. ...

Example:
```python
from local_crontab import Converter
Converter('0 10 * * *', 'America/New_York').to_utc_crons()
# returns
['0 15 * 1-2,12 *',
 '0 15 1-10 3 *',
 '0 14 11-31 3 *',
 '0 14 * 4-10 *',
 '0 14 1-3 11 *',
 '0 15 4-31 11 *']
```

Sections: Use it online!, Use as a script, Use as a library, Project info

</details>

### podman

Bindings for Podman RESTful API

`pip install podman` · installs (wheel) · licence: Apache Software License · rank 6804 · last release 2026-03-25 · [PyPI](https://pypi.org/project/podman/)

<details><summary>README extract</summary>

This python package is a library of bindings to use the RESTful API of Podman.
It is currently under development and contributors are welcome!

Example:
```python
"""Demonstrate PodmanClient."""
import json
from podman import PodmanClient

# Provide a URI path for the libpod service.  In libpod, the URI can be a unix
# domain socket(UDS) or TCP.  The TCP connection has not been implemented in this
# package yet.

uri = "unix:///run/user/1000/podman/podman.sock"

with PodmanClient(base_url=uri) as client:
...
```

Sections: podman-py, Dependencies, Example usage

</details>

### prefect-ray

Prefect integrations with the Ray execution framework.

`pip install prefect-ray` · installs (wheel) · licence: Apache Software License · rank 6806 · last release 2026-10-19 · [PyPI](https://pypi.org/project/prefect-ray/)

### ssh2-python

Bindings for libssh2 C library

`pip install ssh2-python` · installs (wheel) · licence: LGPL-2.1-only · rank 6826 · last release 2025-10-12 · [PyPI](https://pypi.org/project/ssh2-python/)

_README extract left out: share-alike licence._

### koheesio

The steps-based Koheesio framework

`pip install koheesio` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 6834 · last release 2026-10-16 · [PyPI](https://pypi.org/project/koheesio/) · [docs](https://github.com/Nike-Inc/koheesio#readme) · [source](https://github.com/Nike-Inc/koheesio)

<details><summary>README extract</summary>

| | |

| CI/CD | |
| Package | |
| Meta | |

Koheesio - the Finnish word for cohesion - is a robust Python framework designed to build efficient data pipelines. It
encourages modularity and collaboration, allowing the creation of complex pipelines from simple, reusable components. ...

Sections: Koheesio, Koheesio: A Python Framework for Efficient Data Pipelines, What is Koheesio?, What Koheesio is Not, The Strength of Koheesio, Promoting Collaboration and Innovation, Comparison to other libraries, ML frameworks, Orchestration tools, Others, Koheesio Core Components, Using Pip, Using Hatch, Using Poetry

</details>

### mozlog

Robust log handling specialized for logging in the Mozilla universe

`pip install mozlog` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 6839 · last release 2026-03-23 · [PyPI](https://pypi.org/project/mozlog/)

### extend-ai

Official Python SDK for Extend (extend.ai) — the document processing API. Parse, extract, classify, split, and edit PDFs and 35+ file types

`pip install extend-ai` · installs (wheel) · licence: MIT License · rank 6857 · last release 2026-11-03 · [PyPI](https://pypi.org/project/extend-ai/) · [source](https://github.com/extend-hq/extend-python-sdk)

<details><summary>README extract</summary>

Official Python SDK for Extend (extend.ai) — the document processing API. Parse, extract, classify, split, and edit PDFs and 35+ file types via PyPI (`extend-ai`).

The Extend Python library provides convenient, typed access to the Extend API — enabling you to parse, extract, classify, split, and edit documents with a few lines of code.

Example:
```python
from extend_ai import Extend

client = Extend(token="YOUR_API_KEY")

result = client.parse(file={"url": "

for chunk in result.output.chunks:
    print(chunk.content)
```

...

</details>

### pycel

A library for compiling excel spreadsheets to python code & visualizing them as a graph

`pip install pycel` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 6863 · last release 2021-10-13 · [PyPI](https://pypi.org/project/pycel/)

_README extract left out: share-alike licence._

### miniopy-async

Asynchronous MinIO Client SDK for Python

`pip install miniopy-async` · installs (wheel) · licence: Apache Software License · rank 6865 · last release 2026-10-26 · [PyPI](https://pypi.org/project/miniopy-async/) · [docs](https://hlf20010508.github.io/miniopy-async/) · [source](https://github.com/hlf20010508/miniopy-async)

<details><summary>README extract</summary>

Asynchronous MinIO Client SDK for Python

Example:
```python
from miniopy_async import Minio
import asyncio

async def main():
    async with Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        secure=True,  # http for False, https for True
    ) as client:
...
```

Sections: miniopy-async, Build from Source, Quick Start

</details>

### xpress8

Python bindings for the Microsoft Xpress8 (ESE) compression library

`pip install xpress8` · installs (wheel) · licence: MIT License · rank 6883 · last release 2026-09-14 · [PyPI](https://pypi.org/project/xpress8/) · [source](https://github.com/Hugoberry/xpress8-python)

<details><summary>README extract</summary>

Cython bindings for Microsoft's Xpress8 compression library, as shipped in
the Extensible Storage Engine (ESE)
source tree. Released under the MIT License.

This is a sibling of xpress9-python.
Xpress8 is the variant used by Power BI's `.pbix` file format and by various
Windows-internal data stores; it is *not* wire-compatible with Xpress9.

Example:
```python
from xpress8 import Xpress8

x = Xpress8()                       # max_original_size=65536, level=9

# Single-buffer round trip
compressed = x.compress(b"hello world " * 64)
restored   = x.decompress(compressed, len(b"hello world " * 64))

# PBIX-style chunked stream: each chunk has a 4-byte LE header
...
```

Sections: xpress8-python, Usage, Layout

</details>

### inertia-django

Django adapter for the InertiaJS framework

`pip install inertia-django` · installs (wheel) · licence: MIT · rank 6884 · last release 2026-08-16 · [PyPI](https://pypi.org/project/inertia-django/) · [source](https://github.com/inertiajs/inertia-django)

<details><summary>README extract</summary>

Official Docs and installation instructions are available here

Example:
```python
from inertia import render
from .models import Event

def index(request):
  return render(request, 'Event/Index', props={
    'events': Event.objects.all()
  })
```

Sections: Inertia.js Django Adapter, Backend, Frontend, CSRF, Upgrading to Inertia v3, Usage, Responses, Shared Data, Prop Serialization, InertiaJsonEncoder, InertiaMeta, External Redirects, Optional Props, Deferred Props

</details>

### watchgod

Simple, modern file watching and code reload in python.

`pip install watchgod` · installs (wheel) · licence: MIT License · rank 6900 · last release 2022-04-01 · [PyPI](https://pypi.org/project/watchgod/)

<details><summary>README extract</summary>

Simple, modern file watching and code reload in python.

Please note: This package (watchgod) has been renamed to watchfiles.
Please replace `watchgod` with `watchfiles`, see the migration guide
for help and instructions on switching. ...

Features:
*watchgod* (for now) uses file polling rather than the OS's built in file change notifications.

This is not an oversight, it's a decision with the following rationale:

1. ...

Example:
```python
from watchgod import watch

for changes in watch('./path/to/dir'):
    print(changes)
```

Sections: watchgod, NOTICE - Package Renamed to `watchfiles`, Usage, Asynchronous Methods, Custom Watchers, CLI

</details>

### pamela

PAM interface using ctypes

`pip install pamela` · installs (wheel) · licence: MIT License · rank 6914 · last release 2024-08-09 · [PyPI](https://pypi.org/project/pamela/)

<details><summary>README extract</summary>

There seems to be a glut of Python wrappers for PAM that have since been abandoned.
This repo merges two separate efforts:

- gnosek/python-pam
 - adds wrappers for a few more calls, e.g. opening sessions
 - raises PamError on failure instead of returning False, with informative error messages ...

Features:
Both projects appear to be abandoned, with no response to issues or pull requests in at least a year, and I need it for JupyterHub.

Sections: Pamela: yet another Python wrapper for PAM, Why?, Use it

</details>

### matrice

Common server utilities for Matrice.ai services

`pip install matrice` · installs (wheel) · licence: MIT · rank 6922 · last release 2026-07-29 · [PyPI](https://pypi.org/project/matrice/)

<details><summary>README extract</summary>

Purpose: Python SDK for creating projects and inference pipelines using the Matrice packages. This document is a precise, scannable reference for modules, files, functions, and testing/use-case mapping.

| Item | Description | ...

Sections: py_matrice SDK — Comprehensive Reference, 1. Overview, 2. Repository Layout, 3. Build and Setup, 4. Module and Function Reference, 4.1 `init.py`, 4.2 `projects.py` — Projects, 4.3 `dataset.py` — Datasets, 4.4 `models.py` — Trained Models, 4.5 `model_store.py` — Model Store & BYOM, 4.6 `exported_model.py` — Exported Models, 4.7 `annotation.py` — Annotations, 4.8 `action.py` — Actions, 4.9 `application.py` & `app_store.py`

</details>

### HeapDict

a heap with decrease-key and increase-key operations

`pip install HeapDict` · installs (wheel) · licence: BSD License · rank 6933 · last release 2019-09-09 · [PyPI](https://pypi.org/project/HeapDict/)

<details><summary>README extract</summary>

heapdict implements the MutableMapping ABC, meaning it works pretty
much like a regular Python dict. It's designed to be used as a
priority queue, where items are added and consumed as follows:

Compared to an ordinary dict, a heapdict has the following differences: ...

Example:
```python
hd = heapdict()
hd[obj1] = priority1
hd[obj2] = priority2
# ...
(obj, priority) = hd.popitem()
```

</details>

### lia-web

This package has been renamed to cross-web. Install cross-web instead.

`pip install lia-web` · installs (wheel) · licence: MIT License · rank 6941 · last release 2025-12-25 · [PyPI](https://pypi.org/project/lia-web/)

<details><summary>README extract</summary>

This package has been renamed to cross-web.

Please update your dependencies to use `cross-web` instead:

And update your imports from:

to:

This package (`lia-web`) now depends on `cross-web` and re-exports all its symbols under the `lia` namespace for backwards compatibility. However, we recommend updating your imports to use `cross` directly.

Example:
```python
from lia import Response
```

Sections: lia-web has been renamed to cross-web, Backwards Compatibility

</details>

### mercadopago

Mercadopago SDK module for Payments integration

`pip install mercadopago` · installs (wheel) · licence: MIT License · rank 6943 · last release 2026-09-10 · [PyPI](https://pypi.org/project/mercadopago/) · [source](https://github.com/mercadopago/sdk-python)

<details><summary>README extract</summary>

This library provides developers with a simple set of bindings to help you integrate Mercado Pago API to a website and start receiving payments.

Python 3.9 or higher.

Example:
```python
import mercadopago

sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")

request_options = mercadopago.config.RequestOptions()
request_options.custom_headers = {
    'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
}

order_data = {
    "type": "online",
    "total_amount": "100.00",
    "external_reference": "ext_ref_1234",
    "transactions": {
...
```

Sections: Mercado Pago SDK for Python, 💡 Requirements, 🌟 Getting Started, Simple usage — Orders API, Typed request classes (optional), Creating a payment (legacy Payments API), Per-request configuration, 📚 Documentation

</details>

### prefect-sqlalchemy

Prefect integrations for working with databases

`pip install prefect-sqlalchemy` · installs (wheel) · licence: Apache Software License · rank 6946 · last release 2026-02-12 · [PyPI](https://pypi.org/project/prefect-sqlalchemy/)

### snapshottest

Snapshot testing for pytest, unittest, Django, and Nose

`pip install snapshottest` · installs (wheel) · licence: MIT · rank 6947 · last release 2020-09-29 · [PyPI](https://pypi.org/project/snapshottest/)

<details><summary>README extract</summary>

Snapshot testing is a way to test your APIs without writing actual test cases.

1. A snapshot is a single state of your API, saved in a file.
2. You have a set of snapshots for your API endpoints.
3. Once you add a new feature, you can generate *automatically* new snapshots for the updated API.

Example:
```python
from snapshottest import TestCase

class APITestCase(TestCase):
    def test_api_me(self):
        """Testing the API for /me"""
        my_api_response = api.client.get('/me')
        self.assertMatchSnapshot(my_api_response)

        # Set custom snapshot name: `gpg_response`
        my_gpg_response = api.client.get('/me?gpg_key')
...
```

...

</details>

### probatio

A modern Python data validation library

`pip install probatio` · installs (wheel) · licence: MIT · rank 6980 · last release 2026-10-02 · [PyPI](https://pypi.org/project/probatio/) · [docs](https://probatio.frenck.dev) · [source](https://github.com/frenck/probatio)

<details><summary>README extract</summary>

[][releases]
[][pypi]

[](

[][build]
[][codecov]
[][codspeed]
[][scorecard]

Put your data to the proof.

Probatio is a modern, maintained data validation library for Python. The model
is simple: a schema is data, and data describes data. ...

Features:
It is a config-loading library, so the real question is whether you would feed it
untrusted input. The evidence, not the adjectives:

- voluptuous 0.16.0 test suite: runs against Probatio, with every divergence
 a deliberate, documented deviation. ...

Example:
```python
from probatio import Schema, Required, Optional

schema = Schema(
    {
        Required("name"): str,
        Optional("port", default=8080): int,
    }
)

schema({"name": "app"})
# {'name': 'app', 'port': 8080}
```

...

</details>

### prefect-dbt

Prefect integrations for working with dbt

`pip install prefect-dbt` · installs (wheel) · licence: Apache Software License · rank 6981 · last release 2026-06-05 · [PyPI](https://pypi.org/project/prefect-dbt/)

### cassandra-sigv4

Implements a sigv4 authentication plugin for the open-source Datastax Python Driver for Apache Cassandra

`pip install cassandra-sigv4` · installs (wheel) · licence: Apache Software License · rank 6984 · last release 2020-10-30 · [PyPI](https://pypi.org/project/cassandra-sigv4/) · [source](https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin/)

<details><summary>README extract</summary>

The current version is 4.0.2. Please see the changelog for details on version history.

This package implements an authentication plugin for the open-source Datastax Python Driver for Apache Cassandra.
The driver enables you to add authentication information to your API requests using the AWS Signature Version 4 Process (SigV4). ...

Example:
```python
ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.load_verify_locations('./AmazonRootCA1.pem')
ssl_context.verify_mode = CERT_REQUIRED
boto_session = boto3.Session(aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
                             aws_secret_access_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
...
```

...

</details>

### python-hwpx

한글 없이 HWPX 문서를 열고, 편집하고, 생성하고, 검증하는 Python 문서 라이브러리

`pip install python-hwpx` · installs (wheel) · licence: Apache-2.0 · rank 7001 · last release 2026-11-02 · [PyPI](https://pypi.org/project/python-hwpx/) · [docs](https://airmang.github.io/python-hwpx/)

<details><summary>README extract</summary>

한컴오피스 없이 한/글 문서(HWPX·HWP)를 읽고 고치고 만드는 파이썬 라이브러리

한국어 | English

HWPX는 ZIP 안에 XML(OWPML)을 담은 형식이라, 한컴오피스가 없어도 파이썬만으로 다룰 수 있습니다.
python-hwpx는 Windows·macOS·Linux·CI 어디서나 돌고 의존성은 `lxml` 하나입니다. HWP 5.0(`.hwp`)도 같은
API로 열고 저장합니다.

만든 문서는 한컴오피스 2024에서 직접 열어 보고 그 결과를 날짜와 함께
아래에 적어 둡니다.

스타일은 이름으로 고릅니다. 없는 이름을 쓰면 그 줄에서 바로 오류가 납니다. ...

Example:
```python
from hwpx import HwpxDocument

doc = HwpxDocument.new()
doc.add_heading("2026 운영계획", level=1)
doc.add_paragraph("추진 배경", style="개요 2")  # 한/글이 "가." 번호를 붙인다
doc.save_to_path("계획.hwpx")
```

Sections: python-hwpx, 시작하기, 할 수 있는 것, 양식 채우기 예, 한/글과 얼마나 같은가, 어디서 쓰나, 비교, 알려진 제약, 기여하기, 감사의 말

</details>

### runwayml

The official Python library for the runwayml API

`pip install runwayml` · installs (wheel) · licence: Apache Software License · rank 7006 · last release 2026-10-23 · [PyPI](https://pypi.org/project/runwayml/) · [source](https://github.com/runwayml/sdk-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The RunwayML Python library provides convenient access to the RunwayML REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from runwayml import RunwayML

client = RunwayML(
    api_key=os.environ.get("RUNWAYML_API_SECRET"),  # This is the default and can be omitted
)

image_to_video = client.image_to_video.create(
    model="gen4_turbo",
    prompt_image="
    ratio="1280:720",
    prompt_text="The bunny is eating a carrot",
)
print(image_to_video.id)
```

...

</details>

### pytest-spec

Library pytest-spec is a pytest plugin to display test execution output like a SPECIFICATION.

`pip install pytest-spec` · installs (wheel) · licence: GPL-2.0-or-later · rank 7015 · last release 2026-05-17 · [PyPI](https://pypi.org/project/pytest-spec/) · [docs](https://pchomik.ovh/docs/pytest-spec/about) · [source](https://github.com/pchomik/pytest-spec)

_README extract left out: share-alike licence._

### pyjwkest

Python implementation of JWT, JWE, JWS and JWK

`pip install pyjwkest` · installs (wheel) · licence: Apache Software License · rank 7024 · last release 2025-10-04 · [PyPI](https://pypi.org/project/pyjwkest/)

<details><summary>README extract</summary>

NOTE!! This library is NOT actively maintained anymore.

If someone wants to take over the responsibility of maintaining it,
contact me (

Implementation of JWT, JWS, JWE and JWK as defined in:

</details>

### arcadepy

The official Python library for the Arcade API

`pip install arcadepy` · installs (wheel) · licence: MIT License · rank 7034 · last release 2025-11-06 · [PyPI](https://pypi.org/project/arcadepy/) · [source](https://github.com/ArcadeAI/arcade-py)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Arcade Python library provides convenient access to the Arcade REST API from any Python 3.8+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from arcadepy import Arcade

client = Arcade(
    api_key=os.environ.get("ARCADE_API_KEY"),  # This is the default and can be omitted
)

execute_tool_response = client.tools.execute(
    tool_name="Google.ListEmails",
    input={"n_emails": 10},
    user_id="user@example.com",
)
print(execute_tool_response.id)
```

...

</details>

### requests-sse

server-sent events python client library based on requests

`pip install requests-sse` · installs (wheel) · licence: Apache Software License · rank 7044 · last release 2026-03-11 · [PyPI](https://pypi.org/project/requests-sse/) · [docs](https://github.com/overcat/requests-sse) · [source](https://github.com/overcat/requests-sse)

<details><summary>README extract</summary>

A Server-Sent Events python client based on requests, provides a simple interface to process Server-Sent Events.

Example:
```python
import requests
from requests_sse import EventSource, InvalidStatusCodeError, InvalidContentTypeError

with EventSource(" timeout=30) as event_source:
    try:
        for event in event_source:
            print(event)
    except InvalidStatusCodeError:
        pass
    except InvalidContentTypeError:
        pass
...
```

Sections: requests-sse, Usage

</details>

### mdformat-footnote

An mdformat plugin for parsing/validating footnotes

`pip install mdformat-footnote` · installs (wheel) · licence: MIT License · rank 7049 · last release 2026-01-30 · [PyPI](https://pypi.org/project/mdformat-footnote/)

<details><summary>README extract</summary>

[][ci-link]
[][cov-link]
[][pypi-link]

Footnote format addition for mdformat.

Sections: mdformat-footnote, Publish to PyPi

</details>

### instagrapi

Fast and effective Instagram Private API wrapper

`pip install instagrapi` · installs (wheel) · licence: MIT · rank 7051 · last release 2026-11-07 · [PyPI](https://pypi.org/project/instagrapi/) · [docs](https://subzeroid.github.io/instagrapi/) · [source](https://github.com/subzeroid/instagrapi)

<details><summary>README extract</summary>

> ⚠️ Telegram support group moved to aiograpi_support — the previous `@instagrapi` group has been restricted by Meta and is no longer maintained.

Fast and effective unofficial Instagram API wrapper for Python. ...

Features:
* Uses Web API and Mobile API flows where available
* Supports login by password, 2FA, 8-digit backup codes, `sessionid`, and Bloks 2FA fallback/helpers for newer verification flows
* Includes email/SMS-based challenge resolver hooks
* Uploads and ...

Example:
```python
from instagrapi import Client

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
medias = cl.user_medias(user_id, 20)
```

...

</details>

### pydantic-ai-shields

Guardrail capabilities for Pydantic AI — cost tracking, tool permissions, input/output guards

`pip install pydantic-ai-shields` · installs (wheel) · licence: MIT · rank 7060 · last release 2026-06-01 · [PyPI](https://pypi.org/project/pydantic-ai-shields/) · [docs](https://vstorm-co.github.io/pydantic-ai-shields/) · [source](https://github.com/vstorm-co/pydantic-ai-shields)

<details><summary>README extract</summary>

Guardrail Capabilities for Pydantic AI Agents

 Cost Tracking
 Prompt Injection
 PII Detection
 Secret Redaction
 Tool Permissions
 Async Guardrails

Pydantic AI Shields provides ready-to-use guardrail capabilities for Pydantic AI agents. ...

Example:
```python
from pydantic_ai import Agent
from pydantic_ai_shields import CostTracking, ToolGuard, InputGuard

agent = Agent(
    "openai:gpt-4.1",
    capabilities=[
        CostTracking(budget_usd=5.0),
        ToolGuard(blocked=["execute"], require_approval=["write_file"]),
...
```

Sections: Pydantic AI Shields, Quick Start, Available Shields, CostTracking, ToolGuard, InputGuard, OutputGuard, AsyncGuardrail, Built-in Content Shields, PromptInjection, PiiDetector, SecretRedaction, BlockedKeywords, NoRefusals

</details>

### hurry.filesize

A simple Python library for human readable file sizes (or anything sized in bytes).

`pip install hurry.filesize` · installs from source (sdist only) · licence: ZPL 2.1 · rank 7068 · last release 2009-03-11 · [PyPI](https://pypi.org/project/hurry.filesize/)

<details><summary>README extract</summary>

hurry.filesize a simple Python library that can take a number of bytes and
returns a human-readable string with the size in it, in kilobytes (K),
megabytes (M), etc.

The default system it uses is "traditional", where multipliers of 1024
increase the unit size:
An alternative, slightly more verbose system:
A verbose system:
You can also use the SI ...

Example:
```python
>>> from hurry.filesize import size
>>> size(1024)
'1K'
```

Sections: hurry.filesize, Changes, 0.9 (2009-03-11), Download

</details>

### pyexcel-xlsx

A wrapper library to read, manipulate and write data in xlsx and xlsmformat

`pip install pyexcel-xlsx` · installs (wheel) · licence: New BSD · rank 7075 · last release 2025-03-05 · [PyPI](https://pypi.org/project/pyexcel-xlsx/)

<details><summary>README extract</summary>

pyexcel-xlsx is a tiny wrapper library to read, manipulate and write data in xlsx and xlsm format using `read_only` mode reader, `write_only` mode writer from openpyxl. You are likely to use it with pyexcel.

Please note:

1. `auto_detect_int` flag will not take effect because openpyxl detect integer in python 3 by default.
2. ...

Example:
```python
>>> from pyexcel_xlsx import save_data
>>> data = OrderedDict() # from collections import OrderedDict
>>> data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
>>> data.update({"Sheet 2": [["row 1", "row 2", "row 3"]]})
>>> save_data("your_file.xlsx", data)
```

...

</details>

### stqdm

Easy progress bar for streamlit based on the awesome streamlit.progress and tqdm

`pip install stqdm` · installs (wheel) · licence: Apache Software License · rank 7080 · last release 2026-06-14 · [PyPI](https://pypi.org/project/stqdm/) · [source](https://github.com/Wirg/stqdm)

<details><summary>README extract</summary>

stqdm is the simplest way to handle a progress bar in streamlit app.

Example:
```python
from time import sleep
from stqdm import stqdm

for _ in stqdm(range(50)):
    sleep(0.5)
```

Sections: stqdm, How to use, Use stqdm in main, Use stqdm in sidebar, Customize the bar with tqdm parameters, Setting Default Configuration, Scoped Configuration, Going further with configuration management

</details>

### concurrencytest

Run unittest test suites concurrently

`pip install concurrencytest` · installs (wheel) · licence: GPL-2.0-or-later · rank 7087 · last release 2026-11-06 · [PyPI](https://pypi.org/project/concurrencytest/) · [source](https://github.com/cgoldberg/concurrencytest)

_README extract left out: share-alike licence._

### summarization-pydantic-ai

Automatic Conversation Summarization and History Management for Pydantic AI

`pip install summarization-pydantic-ai` · installs (wheel) · licence: MIT · rank 7091 · last release 2026-07-24 · [PyPI](https://pypi.org/project/summarization-pydantic-ai/) · [source](https://github.com/vstorm-co/summarization-pydantic-ai)

<details><summary>README extract</summary>

Unlimited context for long-running agents.

 Auto-summarize or slide the window — never hit the context wall.

 Docs ·
 PyPI ·
 Install ·
 Ecosystem ·
 Deep Agents

 LLM summarization • Zero-cost sliding window • Auto token tracking • Limit warnings • Safe tool-pair cutoff ...

Features:
| Feature | Description |

| Two Strategies | Intelligent summarization or fast sliding window |
| Flexible Triggers | Message count, token count, or fraction-based |
| Safe Cutoff | Never breaks tool call/response pairs |
| Auto max_tokens | ...

Example:
```python
from pydantic_ai import Agent
from pydantic_ai_summarization import ContextManagerCapability

agent = Agent(
    "anthropic:claude-sonnet-4-6",
    capabilities=[ContextManagerCapability(max_tokens=100_000)],
)

...

</details>

### pathtools

File system general utilities

`pip install pathtools` · installs from source (sdist only) · licence: MIT License · rank 7092 · last release 2011-08-25 · [PyPI](https://pypi.org/project/pathtools/)

<details><summary>README extract</summary>

Pattern matching and various utilities for file systems paths.

</details>

### pytoml

A parser for TOML-0.4.0

`pip install pytoml` · installs (wheel) · licence: MIT License · rank 7093 · last release 2019-07-21 · [PyPI](https://pypi.org/project/pytoml/)

<details><summary>README extract</summary>

The pytoml project is no longer being actively maintained. Consider using the
toml package instead.

This project aims at being a specs-conforming and strict parser and writer for TOML files.
The library currently supports version 0.4.0 of the specs and runs with Python 2.7+ and 3.5+.

Install:

 pip install pytoml ...

Sections: Deprecated, pytoml, tests

</details>

### dockerpty

Python library to use the pseudo-tty of a docker container

`pip install dockerpty` · installs from source (sdist only) · licence: Apache Software License · rank 7094 · last release 2016-02-04 · [PyPI](https://pypi.org/project/dockerpty/)

<details><summary>README extract</summary>

Provides the functionality needed to operate the pseudo-tty (PTY) allocated to
a docker container, using the Python client.


Example:
```python
import docker
import dockerpty

client = docker.Client()
container = client.create_container(
    image='busybox:latest',
    stdin_open=True,
    tty=True,
    command='/bin/sh',
)

dockerpty.start(client, container)
```

Sections: Docker PTY, Usage, Tests, How it works, Copyright & Licensing

</details>

### ibmcloudant

Python client library for IBM Cloudant

`pip install ibmcloudant` · installs (wheel) · licence: Apache Software License · rank 7095 · last release 2026-11-03 · [PyPI](https://pypi.org/project/ibmcloudant/)

<details><summary>README extract</summary>

IBM Cloudant Python SDK is a client library that interacts with the
IBM Cloudant APIs.

Disclaimer: This library is still a 0.x release. We do consider this
library production-ready and capable, but there are still some
limitations we’re working to resolve, and refinements we want to
deliver. ...

Features:
The IBM Cloudant Python SDK allows developers to programmatically
interact with IBM Cloudant
with the help of the `ibmcloudant` package.

Example:
```python
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_all_dbs().get_result()

print(response)
```

...

</details>

### kiwipiepy-model

Model for kiwipiepy

`pip install kiwipiepy-model` · installs from source (sdist only) · licence: Apache-2.0 · rank 7105 · last release 2026-09-25 · [PyPI](https://pypi.org/project/kiwipiepy-model/)

<details><summary>README extract</summary>

kiwipiepy is a python version package of Kiwi(Korean Intelligent Word Identifier) which is a morphological analyzer for Korean.

</details>

### matrice-inference

Common server utilities for Matrice.ai services

`pip install matrice-inference` · installs (wheel) · licence: MIT · rank 7107 · last release 2026-07-29 · [PyPI](https://pypi.org/project/matrice-inference/)

### pygelf

Logging handlers with GELF support

`pip install pygelf` · installs (wheel) · licence: MIT License · rank 7125 · last release 2025-06-14 · [PyPI](https://pypi.org/project/pygelf/)

<details><summary>README extract</summary>

Python logging handlers with GELF (Graylog Extended Log Format) support.

Currently TCP, UDP, TLS (encrypted TCP) and HTTP logging handlers are supported.

Example:
```python
from pygelf import GelfTcpHandler, GelfUdpHandler, GelfTlsHandler, GelfHttpHandler, GelfHttpsHandler
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.addHandler(GelfTcpHandler(host='127.0.0.1', port=9401))
logger.addHandler(GelfUdpHandler(host='127.0.0.1', port=9402))
...
```

Sections: pygelf, Get pygelf, Usage, Message structure, Configuration, Static fields, Dynamic fields, Defining fields from environment

</details>

### blosc

Blosc data compressor

`pip install blosc` · installs (wheel) · licence: BSD License · rank 7132 · last release 2026-01-17 · [PyPI](https://pypi.org/project/blosc/)

<details><summary>README extract</summary>

:Author: The Blosc development team
:Contact: blosc@blosc.org
:Github:
:URL:
:PyPi:
:Anaconda:
:Gitter:
:Code of Conduct:

Features:
Note: There is a more modern version of this package called Python-Blosc2
which supports many more features and is more actively maintained. Visit it at:

Blosc ( is a high performance compressor optimized for
binary data. ...

Example:
```python
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
python-blosc version: 1.5.1.dev0
Blosc version: 1.11.2 ($Date:: 2017-01-27 #$)
Compressors available: ['blosclz', 'lz4', 'lz4hc', 'snappy', 'zlib', 'zstd']
Compressor library versions:
  BloscLZ: 1.0.5
  LZ4: 1.7.5
  Snappy: 1.1.1
  Zlib: 1.2.7
  Zstd: 1.1.2
...
```

...

</details>

### matrice-common

Common server utilities for Matrice.ai services

`pip install matrice-common` · installs (wheel) · licence: MIT · rank 7139 · last release 2026-07-29 · [PyPI](https://pypi.org/project/matrice-common/)

<details><summary>README extract</summary>

matrice_common is a high-performance Python package providing reusable utilities for Matrice.ai services. It offers production-ready components for authentication, API communication, streaming, and more.

Example:
```python
from matrice_common.rpc import RPC
from matrice_common.session import create_session

# Initialize RPC client
rpc = RPC(
    access_key="your_access_key",
    secret_key="your_secret_key"  # pragma: allowlist secret
)

# Make API requests
response = rpc.get("/v1/endpoint")
data = rpc.post("/v1/resource", payload={"key": "value"})

...
```

...

</details>

### matrice-streaming

Common server utilities for Matrice.ai services

`pip install matrice-streaming` · installs (wheel) · licence: MIT · rank 7141 · last release 2026-08-26 · [PyPI](https://pypi.org/project/matrice-streaming/)

<details><summary>README extract</summary>

matrice\_streaming is a high-performance, Cython-compiled Python package providing streaming, client, and deployment utilities for Matrice.ai services.
It offers ready-to-use streaming gateways, client management, camera handling, and deployment orchestration with complete type stubs for IDEs.

Features:
* Cython Compiled – Optimized performance via C extensions.
* Streaming Gateway – Real-time streaming and inference processing.
* Client Management – Deploy clients with streaming capabilities. ...

Example:
```python
from matrice_streaming import StreamingGateway, AutoStreaming
from matrice_streaming import CameraManager, Deployment

# Example: Create streaming gateway
gateway = StreamingGateway(
    model_input_type="video",
    input_config=input_config,
    output_config=output_config
...

</details>

### gibberish-detector

Detects gibberish strings.

`pip install gibberish-detector` · installs (wheel) · licence: MIT License · rank 7147 · last release 2021-03-04 · [PyPI](https://pypi.org/project/gibberish-detector/)

<details><summary>README extract</summary>

This is based off and adapted so that it is a
Python3 module.

Example:
```python
>>> from gibberish_detector import detector
>>> Detector = detector.create_from_model('big.model')
>>> print(Detector.is_gibberish('ertrjiloifdfyyoiu'))
True
```

Sections: Gibberish Detector, Examples, Usage

</details>

### azure-iot-device

Microsoft Azure IoT Device Library

`pip install azure-iot-device` · installs (wheel) · licence: MIT License · rank 7161 · last release 2024-07-17 · [PyPI](https://pypi.org/project/azure-iot-device/)

<details><summary>README extract</summary>

The Azure IoT Device SDK for Python enables Python developers to easily create IoT device solutions that seamlessly connect to the Azure IoT Hub ecosystem.

* *If you're looking for the azure-iot-hub library, it is now located in the azure-iot-hub-python repository* ...

Features:
:heavy_check_mark: feature available :heavy_multiplication_x: feature planned but not yet supported :heavy_minus_sign: no support planned*

*Features that are not planned may be prioritized in a future release, but are not currently planned ...

Sections: azure-iot-device, Using the library, Features, IoTHub Device Client, IoTHub Module Client, Provisioning Device Client, Critical Upcoming Changes Notice, Certificates

</details>

### awscliv2

Wrapper for AWS CLI v2

`pip install awscliv2` · installs (wheel) · licence: MIT License · rank 7167 · last release 2024-09-04 · [PyPI](https://pypi.org/project/awscliv2/) · [docs](https://awscliv2.readthedocs.io/en/latest/) · [source](https://github.com/youtype/awscliv2)

<details><summary>README extract</summary>

Wrapper for AWS CLI v2.

- AWS CLI v2 for Python
 - Features
 - Before you start
 - Installation
 - Usage
 - From command line
 - Docker fallback
 - Extra commands
 - As a Python module
 - Development
 - How to help
 - Versioning
 - Latest changes

Features:
- No dependency hell, like with original awscli
- Can install and update `awscliv2` binaries
- Provides access to all AWS services
- Has Python interface `awscliv2.api.AWSAPI`

Example:
```python
from awscliv2.api import AWSAPI
from awscliv2.exceptions import AWSCLIError

aws_api = AWSAPI()

try:
    output = aws_api.execute(["s3", "ls"])
except AWSCLIError as e:
    print(f"Something went wrong: {e}")
else:
    print(output)
```

...

</details>

### python-intercom

(no summary)

`pip install python-intercom` · installs (wheel) · licence: not stated · rank 7172 · last release 2026-01-30 · [PyPI](https://pypi.org/project/python-intercom/) · [source](https://github.com/intercom/python-intercom)

<details><summary>README extract</summary>

The Intercom Python library provides convenient access to the Intercom APIs from Python.

Example:
```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.ai_content.create_content_import_source(
    url="
)
```

Sections: Intercom Python Library, Reference, Usage, Async Client, Exception Handling, Pagination, Advanced, Access Raw Response Data, Retries, Timeouts, Custom Client

</details>

### genbadge

Generate badges for tools that do not provide one.

`pip install genbadge` · installs (wheel) · licence: BSD License · rank 7174 · last release 2025-11-24 · [PyPI](https://pypi.org/project/genbadge/)

### authcaptureproxy

A Python project to create a proxy to capture authentication information from a webpage. This is useful to capture oauth login details without access to a third-party oauth.

`pip install authcaptureproxy` · installs (wheel) · licence: Apache-2.0 · rank 7184 · last release 2026-11-08 · [PyPI](https://pypi.org/project/authcaptureproxy/) · [docs](https://auth_capture_proxy.readthedocs.io) · [source](https://github.com/alandtse/auth_capture_proxy)

<details><summary>README extract</summary>

A Python project to create a proxy to capture authentication information from a webpage. This is useful to capture oauth login details without access to a third-party oauth.

Sections: Auth_capture_proxy, Using

</details>

### newspaper4k

Simplified python article discovery & extraction.

`pip install newspaper4k` · installs (wheel) · licence: MIT · rank 7212 · last release 2026-11-01 · [PyPI](https://pypi.org/project/newspaper4k/)

<details><summary>README extract</summary>

Newspaper4k Project grew from a fork of the well known newspaper3k by codelucas which was not updated since September 2020. The initial goal of this fork was to keep the project alive and to add new features and fix bugs. ...

Features:
- Multi-threaded article download framework
- Newspaper website category structure detection
- News url identification
- Google News integration
- Text extraction from html
- Top image extraction from html
- All image extraction from html ...

Example:
```python
import newspaper

article = newspaper.article('

print(article.authors)
# ['Hannah Brewitt']

print(article.publish_date)
# 2023-10-29 09:00:15.717000+00:00

print(article.text)
# New England Patriots head coach Bill Belichick, right, embraces Buffalo Bills head coach Sean McDermott ...

...

</details>

### prefect-slack

Prefect integrations with Slack

`pip install prefect-slack` · installs (wheel) · licence: Apache Software License · rank 7213 · last release 2026-08-04 · [PyPI](https://pypi.org/project/prefect-slack/)

<details><summary>README extract</summary>

`prefect-slack` is a collection of prebuilt Prefect tasks and blocks that can be used to quickly send Slack messages in your Prefect flows.

Example:
```python
from prefect import flow
from prefect.context import get_run_context
from prefect_slack import SlackCredentials
from prefect_slack.messages import send_chat_message

@flow
def example_send_message_flow():
   context = get_run_context()

   # Run other tasks and subflows here

   token = "xoxb-your-bot-token-here"
   send_chat_message(
...
```

Sections: prefect-slack, Welcome!, Getting Started, Python setup, Slack setup, Write and run a flow

</details>

### django-admin-tools

A collection of tools for the django administration interface

`pip install django-admin-tools` · installs (wheel) · licence: MIT License · rank 7214 · last release 2026-11-04 · [PyPI](https://pypi.org/project/django-admin-tools/)

<details><summary>README extract</summary>

Features:
django-admin-tools is a collection of extensions/tools for the default django
administration interface, it includes:

* a full featured and customizable dashboard;
* a customizable menu bar;
* tools to make admin theming easier. ...

Sections: django-admin-tools, Overview, Requirements, Documentation, Translations, Screenshots, Version 0.9.4, 4 November 2026, Version 0.9.3, 10 August 2023, Version 0.9.2, 12 December 2021, Version 0.9.1, 12 January 2021, Version 0.9.0, 19 January 2020, Version 0.8.1, 30 May 2017, Version 0.8.0, 12 August 2016, Version 0.7.2, 14 January 2016

</details>

### stellar-sdk

The Python Stellar SDK library provides APIs to build transactions and connect to Horizon and Stellar RPC server.

`pip install stellar-sdk` · installs (wheel) · licence: Apache-2.0 · rank 7227 · last release 2026-10-30 · [PyPI](https://pypi.org/project/stellar-sdk/) · [docs](https://stellar-sdk.readthedocs.io/) · [source](https://github.com/StellarCN/py-stellar-base)

<details><summary>README extract</summary>

py-stellar-base is a Python library for communicating with
a Stellar Horizon server and Stellar RPC server. It is used for building Stellar apps on Python. It supports Python 3.10+ as
well as PyPy 3.11.

It provides:

- a networking layer API for Horizon endpoints.
- a networking layer API for Stellar RPC server methods. ...

Example:
```python
# Alice pay 10.25 XLM to Bob
from stellar_sdk import Asset, Server, Keypair, TransactionBuilder, Network

alice_keypair = Keypair.from_secret("SBFZCHU5645DOKRWYBXVOXY2ELGJKFRX6VGGPRYUWHQ7PMXXJNDZFMKD")
bob_address = "GA7YNBW5CBTJZ3ZZOWX3ZNBKD6OE7A7IHUQVWMY62W2ZBG2SGZVOOPVH"

server = Server("
...
```

Sections: Stellar Python SDK, Documentation, A Simple Example, stellar-contract-bindings, stellar-model, Links

</details>

### django-braces

Reusable, generic mixins for Django

`pip install django-braces` · installs (wheel) · licence: BSD License · rank 7230 · last release 2025-03-18 · [PyPI](https://pypi.org/project/django-braces/)

<details><summary>README extract</summary>

Mixins to add easy functionality to Django class-based views, forms, and models.

</details>

### getmac

Get MAC addresses of remote hosts and local interfaces

`pip install getmac` · installs (wheel) · licence: MIT License · rank 7231 · last release 2026-10-03 · [PyPI](https://pypi.org/project/getmac/) · [source](https://github.com/GhostofGoes/getmac)

<details><summary>README extract</summary>

Pure-Python package to get the MAC address of network interfaces and hosts on the local network.

It provides a platform-independent interface to get the MAC addresses of:

- System network interfaces (by interface name)
- Remote hosts on the local network (by IPv4/IPv6 address or hostname)

It provides one function: `get_mac_address()` ...

Features:
- Pure-Python (no compiled C-extensions required!)
- Python 2.7 and 3.4+
- Lightweight, with no dependencies and a small package size
- Can be dropped into a project as a standalone .py file ...

Example:
```python
from getmac import get_mac_address
eth_mac = get_mac_address(interface="eth0")
win_mac = get_mac_address(interface="Ethernet 3")
ip_mac = get_mac_address(ip="192.168.0.1")
ip6_mac = get_mac_address(ip6="::1")
...

</details>

### matrice-analytics

Post-processing analytics for Matrice.ai inference pipelines

`pip install matrice-analytics` · installs (wheel) · licence: LicenseRef-Matrice-Proprietary · rank 7233 · last release 2026-10-23 · [PyPI](https://pypi.org/project/matrice-analytics/)

### pycobertura

"A Cobertura coverage parser that can diff reports and show coverage progress."

`pip install pycobertura` · installs (wheel) · licence: MIT License · rank 7237 · last release 2025-09-23 · [PyPI](https://pypi.org/project/pycobertura/)

<details><summary>README extract</summary>

A code coverage diff tool for Cobertura reports.

- About
- Install
- CLI usage
- Library usage
- How to contribute?
- FAQ

pycobertura is a generic Cobertura
report parser. It was also designed to help prevent code coverage from
decreasing with the `pycobertura diff` command: any line changed should be
tested and uncovered changes should be ...

Features:
Because we would have to support N version control systems (VCS). It is easy
enough to generate a directory that contains the source code at a given commit
or branch name that it's not a top priority for pycobertura to be VCS-aware: ...

Example:
```python
from pycobertura import Cobertura
cobertura = Cobertura('coverage.xml')

cobertura.version == '4.0.2'
cobertura.line_rate() == 1.0  # 100%
cobertura.files() == [
...

</details>

### squareup

(no summary)

`pip install squareup` · installs (wheel) · licence: MIT License · rank 7244 · last release 2026-09-15 · [PyPI](https://pypi.org/project/squareup/) · [source](https://github.com/square/square-python-sdk)

<details><summary>README extract</summary>

The Square Python library provides convenient access to the Square API from Python.

Example:
```python
from square import Square

client = Square(
    # This is the default and can be omitted.
    token=os.environ.get("SQUARE_TOKEN"),
)
client.payments.create(
    source_id="ccof:GaJGNaZa8x4OgDJn4GB",
    idempotency_key="7b0f3ec5-086a-4871-8f13-3c81b3875218",
    amount_money={
        "amount": 1000,
        "currency": "USD"
    },
...
```

Sections: Square Python Library, Requirements, Usage, Async Client, Legacy SDK, Versioning, Automatic Pagination, File Uploads, Exception Handling, Webhook Signature Verification, Reporting API, Advanced, Retries, Timeouts

</details>

### intel-cmplr-lib-rt

Intel® oneAPI Runtime COMMON LIBRARIES

`pip install intel-cmplr-lib-rt` · installs (wheel) · licence: Other/Proprietary License · rank 7249 · last release 2026-10-16 · [PyPI](https://pypi.org/project/intel-cmplr-lib-rt/)

<details><summary>README extract</summary>

This Intel® oneAPI Runtime COMMON LIBRARIES package contains shared common libraries needed to deploy executables to hosts without the Intel® oneAPI development Toolkits. This COMMON Libraries package should be downloaded and installed along with the COMMON LICENSING package and one or more of the Compiler-Specific runtimes.

</details>

### detect-delimiter

Detects the delimiter used in CSV, TSV and other ad hoc file formats.

`pip install detect-delimiter` · installs (wheel) · licence: Apache Software License · rank 7252 · last release 2018-07-29 · [PyPI](https://pypi.org/project/detect-delimiter/)

<details><summary>README extract</summary>

Detects the delimiter used in CSV, TSV and other ad hoc file formats.

Sections: detect_delimiter, About, Usage

</details>

### proclimits

Resource limits that actually apply to the running process, from cgroups or Windows job objects

`pip install proclimits` · installs (wheel) · licence: Apache-2.0 · rank 7259 · last release 2026-09-17 · [PyPI](https://pypi.org/project/proclimits/) · [source](https://github.com/apify/proclimits)

<details><summary>README extract</summary>

Reports the CPU and memory limits that actually apply to the running process. It reads cgroups on Linux and job objects on Windows.

Features:
Inside a container the usual answers describe the machine, not the process. `psutil.virtual_memory().total` reports the memory of the node, `os.cpu_count()` reports every core of it. ...

Example:
```python
import psutil

import proclimits

def memory_budget() -> tuple[int, int]:
    """The total and the used memory, in bytes.

    For a consumer that sizes a budget from the pair rather than from `MemoryBudget.available`.
    """
    budget = proclimits.get_memory_budget()
    if budget is not None:
        return budget.limit, budget.used

...
```

...

</details>

### jupyter-book

Create computational narratives that are reusable, reproducible, and interactive.

`pip install jupyter-book` · installs (wheel) · licence: BSD License · rank 7261 · last release 2026-09-23 · [PyPI](https://pypi.org/project/jupyter-book/)

<details><summary>README extract</summary>

Jupyter Book is an open-source tool for building publication-quality books and documents from computational material.

Jupyter Book allows users to

- write their content in Markdown files or Jupyter notebooks,
- include computational elements (e.g., code cells) in either type, ...

Sections: Jupyter Book, Governance of This Project

</details>

### multiping

Pure python library to send and receive ICMPecho request (ping) to monitor IP addresses

`pip install multiping` · installs (wheel) · licence: Apache Software License · rank 7265 · last release 2018-05-24 · [PyPI](https://pypi.org/project/multiping/)

<details><summary>README extract</summary>

MultiPing is a Python library to monitor one or many IP addresses via ICMP echo
(ping) requests. Features:

* It works for Python 2 and 3.
* Supports timeouts and retries.
* Supports IPv4 as well as IPv6.
* Small and compact and does not rely on any 3rd party packages, aside from
 what's included in Python. ...

</details>

### xdrlib3

A forked version of `xdrlib`, a module for encoding and decoding XDR (External Data Representation) data in Python.

`pip install xdrlib3` · installs (wheel) · licence: Apache Software License · rank 7278 · last release 2023-05-06 · [PyPI](https://pypi.org/project/xdrlib3/) · [docs](https://github.com/overcat/xdrlib3) · [source](https://github.com/overcat/xdrlib3)

<details><summary>README extract</summary>

A forked version of `xdrlib`, a module for encoding and decoding XDR (External Data Representation) data in Python. `xdrlib` is planned to be removed in Python 3.13 and later versions, therefore this fork has been created to add type hints and maintain compatibility with future versions of Python.

Example:
```python
import xdrlib3

packer = xdrlib3.Packer()
packer.pack_int(16)
packed_data = packer.get_buffer()

unpacker = xdrlib3.Unpacker(packed_data)
unpacked_data = unpacker.unpack_int()
```

Sections: xdrlib3, Usage

</details>

### scrapingbee

ScrapingBee Python SDK

`pip install scrapingbee` · installs (wheel) · licence: MIT License · rank 7324 · last release 2026-09-01 · [PyPI](https://pypi.org/project/scrapingbee/)

<details><summary>README extract</summary>

ScrapingBee is a web scraping API that handles headless browsers and rotates proxies for you. The Python SDK makes it easier to interact with ScrapingBee's API.

Example:
```python
response = client.usage()
print(response.json())
# {
# "max_api_credit": 8000000,
# "used_api_credit": 1000023,
# "max_concurrency": 200,
# "current_concurrency": 1,
# "renewal_subscription_date": "2026-09-01T04:57:13.580067"
# }
```

Sections: ScrapingBee Python SDK, Usage, Authentication, Common parameters, HTML API, Basic Request, Making a POST request, Auto-Mode, HTML API Parameters, Google Search API, Google Search Parameters, Fast Search API, Fast Search Parameters, Amazon API

</details>

### chromedriver-autoinstaller

Automatically install chromedriver that supports the currently installed version of chrome.

`pip install chromedriver-autoinstaller` · installs (wheel) · licence: MIT License · rank 7335 · last release 2024-01-28 · [PyPI](https://pypi.org/project/chromedriver-autoinstaller/)

<details><summary>README extract</summary>

Example:
```python
from selenium import webdriver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()
...
```

Sections: Usage, Example

</details>

### asyncio-gevent

asyncio & gevent in harmony

`pip install asyncio-gevent` · installs (wheel) · licence: MIT License · rank 7343 · last release 2025-07-14 · [PyPI](https://pypi.org/project/asyncio-gevent/) · [docs](https://github.com/gfmio/asyncio-gevent) · [source](https://github.com/gfmio/asyncio-gevent)

<details><summary>README extract</summary>

asyncio-gevent makes asyncio and gevent compatible. It provides utilities for

- running asyncio on gevent (by using gevent as asyncio's event loop)
- running gevent on asyncio (by using asyncio as gevent's event loop, still work in progress)
- converting greenlets to asyncio futures
- converting futures to asyncio greenlets ...

Example:
```python
import gevent.monkey

gevent.monkey.patch_all()

import asyncio
import threading

import gevent

import asyncio_gevent

asyncio.set_event_loop_policy(asyncio_gevent.EventLoopPolicy())

async def f():
    print("f", 1)
    await asyncio.sleep(1)
    print("f", 2)

def g():
    print("g", 1)
    gevent.sleep(2)
    print("g", 2)

async def main():
...
```

...

</details>

### pytest-loguru

Pytest Loguru

`pip install pytest-loguru` · installs (wheel) · licence: MIT License · rank 7345 · last release 2026-05-16 · [PyPI](https://pypi.org/project/pytest-loguru/)

<details><summary>README extract</summary>

A pytest plugin to add support for loguru to pytest's caplog fixture.

You can install it from pypi with:

and from conda-forge with:

Note that coverage is 100% but the coverage tool is confused by the fixture decorator.

Sections: pytest-loguru, Environment, Pre-commit, Packages, Project

</details>

### pytest-xprocess

A pytest plugin for managing processes across test runs.

`pip install pytest-xprocess` · installs (wheel) · licence: MIT License · rank 7358 · last release 2024-05-19 · [PyPI](https://pypi.org/project/pytest-xprocess/)

<details><summary>README extract</summary>

A pytest plugin for managing external processes across test runs.

Sections: pytest-xprocess, Useful Links

</details>

### pygrib

Python module for reading/writing GRIB files

`pip install pygrib` · installs (wheel) · licence: MIT AND (Apache-2.0 OR BSD-2-Clause) · rank 7360 · last release 2025-10-26 · [PyPI](https://pypi.org/project/pygrib/) · [docs](https://jswhit.github.io/pygrib/) · [source](https://github.com/jswhit/pygrib)

<details><summary>README extract</summary>

Provides a high-level interface to the ECWMF ECCODES C library for reading GRIB files.
There are limited capabilities for writing GRIB files (you can modify the contents of an existing file, but you can't create one from scratch). See the online docs for
example usage.

</details>

### xinference-client

Client for Xinference

`pip install xinference-client` · installs (wheel) · licence: Apache License 2.0 · rank 7366 · last release 2026-11-08 · [PyPI](https://pypi.org/project/xinference-client/)

<details><summary>README extract</summary>

Xinference provides a restful client for managing and accessing models programmatically.

Example:
```python
from xinference_client import RESTfulClient as Client

client = Client("
model_uid = client.launch_model(model_name="chatglm2")
model = client.get_model(model_uid)

chat_history = []
prompt = "What is the largest animal?"
model.chat(
    prompt,
    chat_history=chat_history,
    generate_config={"max_tokens": 1024}
)
```

Sections: Xinference Restful Client, Usage

</details>

### fcm-django

Send push notifications to mobile devices and browsers through FCM in Django.

`pip install fcm-django` · installs (wheel) · licence: MIT · rank 7368 · last release 2026-11-02 · [PyPI](https://pypi.org/project/fcm-django/) · [docs](https://github.com/xtrinch/fcm-django#readme) · [source](https://github.com/xtrinch/fcm-django)

<details><summary>README extract</summary>

Django app for Firebase Cloud Messaging. Used as an unified platform for sending push notifications to mobile devices & browsers (android / ios / chrome / firefox / ...).

Supports Firebase Cloud Messaging HTTP v1 API. If you're looking for the legacy API, use `fcm-django<1`! ...

Example:
```python
from firebase_admin import initialize_app

INSTALLED_APPS = (
    ...
    "fcm_django"
    ...
)

# Optional ONLY IF you have initialized a firebase app already:
# Visit
# for more options for the following:
# Store an environment variable called GOOGLE_APPLICATION_CREDENTIALS
# which is a path that point to a json file with your credentials.
...
```

...

</details>

### baostock

A tool for obtaining historical data of China stock market

`pip install baostock` · installs (wheel) · licence: BSD License · rank 7369 · last release 2026-09-21 · [PyPI](https://pypi.org/project/baostock/)

<details><summary>README extract</summary>

Example:
```python
import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取历史K线数据
# 详细指标参数，参见“历史行情指标参数”章节
rs = bs.query_history_k_data_plus("sh.600000",
...
```

Sections: Target Users, Upgrade, Quick Start

</details>

### chroma-mcp

Chroma MCP Server - Vector Database Integration for LLM Applications

`pip install chroma-mcp` · installs (wheel) · licence: Apache-2.0 · rank 7404 · last release 2025-08-14 · [PyPI](https://pypi.org/project/chroma-mcp/) · [docs](https://github.com/chroma-core/chroma-mcp#readme)

<details><summary>README extract</summary>

Chroma - the open-source embedding database.

 The fastest way to build Python or JavaScript LLM apps with memory!



 Docs

 Homepage

The Model Context Protocol (MCP) is an open protocol designed for effortless integration between LLM applications and external data sources or tools, offering a standardized framework to seamlessly provide LLMs ...

Features:
- Flexible Client Types
 - Ephemeral (in-memory) for testing and development
 - Persistent for file-based storage
 - HTTP client for self-hosted Chroma instances
 - Cloud client for Chroma Cloud integration (automatically connects to ...

Sections: Chroma MCP Server, Features, Embedding Functions, Usage with Claude Desktop, Demos, Using Environment Variables, Embedding Function Environment Variables

</details>

### rhino3dm

Python library based on OpenNURBS with a RhinoCommon style

`pip install rhino3dm` · installs (wheel) · licence: MIT License · rank 7406 · last release 2026-09-15 · [PyPI](https://pypi.org/project/rhino3dm/)

<details><summary>README extract</summary>

CPython package based on OpenNURBS with a RhinoCommon style

Example:
```python
from rhino3dm import *
import requests  # pip install requests

req = requests.get(" Logo.3dm")
model = File3dm.FromByteArray(req.content)
for obj in model.Objects:
    geometry = obj.Geometry
    bbox = geometry.GetBoundingBox()
    print("{}, {}".format(bbox.Min, bbox.Max))
```

Sections: rhino3dm.py, Test

</details>

### govuk-bank-holidays

Tool to load UK bank holidays from GOV.UK

`pip install govuk-bank-holidays` · installs (wheel) · licence: MIT License · rank 7407 · last release 2026-02-25 · [PyPI](https://pypi.org/project/govuk-bank-holidays/)

<details><summary>README extract</summary>

This library loads the official list of bank holidays in the United Kingdom as supplied by GOV.UK.
GOV.UK tend to provide this list for only a year or two into the future.

A cached backup list of known bank holidays is stored in this package though it is not updated often. ...

Example:
```python
from govuk_bank_holidays.bank_holidays import BankHolidays

bank_holidays = BankHolidays()
for bank_holiday in bank_holidays.get_holidays():
    print(bank_holiday['title'], 'is on', bank_holiday['date'])
print(bank_holidays.get_next_holiday())

# see govuk_bank_holidays/bank_holidays.py source file for more methods and argument details…

...
```

Sections: GOV.UK Bank Holidays, Usage, Copyright

</details>

### xmlrunner

PyUnit-based test runner with JUnit like XML reporting.

`pip install xmlrunner` · installs from source (sdist only) · licence: GNU Library or Lesser General Public License (LGPL) · rank 7412 · last release 2014-11-10 · [PyPI](https://pypi.org/project/xmlrunner/)

_README extract left out: share-alike licence._

### pylru

A least recently used (LRU) cache implementation

`pip install pylru` · installs (wheel) · licence: MIT · rank 7437 · last release 2026-10-25 · [PyPI](https://pypi.org/project/pylru/) · [source](https://github.com/jlhutch/pylru.git)

<details><summary>README extract</summary>

A least recently used (LRU) cache for Python.

Pylru implements a true LRU cache along with several support classes. The cache is efficient and written in pure Python. Python 3.3+ is supported. Basic operations (lookup, insert, delete) all run in a constant amount of time. Pylru provides a cache class with a simple dict interface. ...

Example:
```python
import pylru

size = 100          # Size of the cache. The maximum number of key/value
                    # pairs you want the cache to hold.

cache = pylru.lrucache(size)
                    # Create a cache object.

value = cache[key]  # Lookup a value given its key.
cache[key] = value  # Insert a key/value pair.
...
```

...

</details>

### pyrad

RADIUS tools

`pip install pyrad` · installs (wheel) · licence: BSD-3-Clause · rank 7438 · last release 2026-10-18 · [PyPI](https://pypi.org/project/pyrad/) · [docs](https://pyradius-pyrad.readthedocs.io) · [source](https://github.com/pyradius/pyrad)

<details><summary>README extract</summary>

pyrad is an implementation of a RADIUS client/server as described in RFC 2865
and related RFCs: accounting, CoA and Disconnect, tunnel attributes,
Status-Server and EAP-MD5. It takes care of all the details like building
RADIUS packets, sending them and decoding responses.

Here is an example of doing an authentication request: ...

Example:
```python
from pyrad.client import Client
from pyrad.dictionary import Dictionary
import pyrad.packet

srv = Client(
    server="localhost",
    secret=b"Kah3choteereethiejeimaeziecumi",
    dict=Dictionary("dictionary"),
)

# create request
req = srv.CreateAuthPacket(
    code=pyrad.packet.AccessRequest, User_Name="wichert", NAS_Identifier="localhost"
)
...
```

Sections: Introduction, BlastRADIUS, Related Projects & Forks

</details>

### bravado-core

Library for adding Swagger support to clients and servers

`pip install bravado-core` · installs (wheel) · licence: BSD License · rank 7441 · last release 2026-05-12 · [PyPI](https://pypi.org/project/bravado-core/)

<details><summary>README extract</summary>

bravado-core is a Python library that adds client-side and server-side support
for the OpenAPI Specification v2.0.

Features:
* OpenAPI Specification schema validation
* Marshaling, transformation, and validation of requests and responses
* Models as Python classes or dicts
* Custom formats for type conversion

Sections: bravado-core, About, Features, Documentation, Related Projects, Setup

</details>

### python-gflags

Obsolete. Please migrate to absl-py instead.

`pip install python-gflags` · installs from source (sdist only) · licence: BSD License · rank 7443 · last release 2017-10-27 · [PyPI](https://pypi.org/project/python-gflags/)

### pybit

Python3 Bybit HTTP/WebSocket API Connector

`pip install pybit` · installs (wheel) · licence: MIT License · rank 7446 · last release 2026-07-14 · [PyPI](https://pypi.org/project/pybit/)

<details><summary>README extract</summary>

Official Python3 API connector for Bybit's HTTP and WebSockets APIs.

Example:
```python
from pybit.unified_trading import HTTP
```

Sections: pybit, About, Usage, Contact

</details>

### gnureadline

The standard Python readline extension statically linked against the GNU readline library.

`pip install gnureadline` · installs (wheel) · licence: GPL-3.0-or-later · rank 7448 · last release 2026-01-06 · [PyPI](https://pypi.org/project/gnureadline/)

_README extract left out: share-alike licence._

### aioping

Asyncio ping implementation

`pip install aioping` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 7470 · last release 2023-07-12 · [PyPI](https://pypi.org/project/aioping/)

_README extract left out: share-alike licence._

### backports.cached-property

cached_property() - computed once per instance, cached as attribute

`pip install backports.cached-property` · installs (wheel) · licence: MIT License · rank 7479 · last release 2022-06-14 · [PyPI](https://pypi.org/project/backports.cached-property/)

<details><summary>README extract</summary>

Python 3.8 adds great descriptor to functools: cached_property.
Technically all required APIs was available since python 3.6,
but it is what it is.

This package is a backport of this functionality for python 3.6 and 3.7.

Example:
```python
from backports.cached_property import cached_property
```

Sections: backports.cached_property, What, How to use

</details>

### bz2file

Read and write bzip2-compressed files.

`pip install bz2file` · installs from source (sdist only) · licence: Apache Software License · rank 7507 · last release 2014-01-19 · [PyPI](https://pypi.org/project/bz2file/)

<details><summary>README extract</summary>

Bz2file is a Python library for reading and writing bzip2-compressed files.

It contains a drop-in replacement for the file interface in the standard
library's ``bz2`` module, including features from the latest development
version of CPython that are not available in older releases. ...

</details>

### sphinx-data-viewer

"Sphinx extension to show data in an interactive list view.

`pip install sphinx-data-viewer` · installs (wheel) · licence: MIT License · rank 7508 · last release 2024-08-28 · [PyPI](https://pypi.org/project/sphinx-data-viewer/) · [docs](https://sphinx-data-viewer.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Adds an interactive data viewer for data objects to Sphinx.

Use it to document:

* JSON data
* JSON files
* Python objects

Complete documentation and examples:

The Javascript part is based on the wonderful work of

</details>

### sdnotify

A pure Python implementation of systemd's service notification protocol (sd_notify)

`pip install sdnotify` · installs from source (sdist only) · licence: MIT License · rank 7517 · last release 2017-08-02 · [PyPI](https://pypi.org/project/sdnotify/)

<details><summary>README extract</summary>

systemd Service Notification

This is a pure Python implementation of the systemd sd_notify protocol. This protocol can be used to inform systemd about service start-up completion, watchdog events, and other service status changes. Thus, this package can be used to write system services in Python that play nicely with systemd. ...

</details>

### purl

An immutable URL class for easy URL-building and manipulation

`pip install purl` · installs (wheel) · licence: MIT License · rank 7518 · last release 2021-05-15 · [PyPI](https://pypi.org/project/purl/)

<details><summary>README extract</summary>

A simple, immutable URL class with a clean API for interrogation and
manipulation. Supports Pythons 2.7, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8 and pypy.

Also supports template URLs as per RFC 6570

Contents:

Example:
```python
>>> from purl import URL

# String constructor
>>> from_str = URL('

# Keyword constructor
>>> from_kwargs = URL(scheme='https', host='www.google.com', path='/search', query='q=testing')

# Combine
>>> from_combo = URL(' 'testing')
```

Sections: purl - A simple Python URL class, Docs, Use, v1.6 - 2021-05-15, v1.5 - 2019-03-10, v1.4 - 2018-03-11, v1.3.1, v1.3, v1.2, v1.1, v1.0.3, v1.0.2, v1.0.1, v1.0

</details>

### password-strength

Password strength and validation

`pip install password-strength` · installs (wheel) · licence: BSD · rank 7522 · last release 2019-01-04 · [PyPI](https://pypi.org/project/password-strength/)

<details><summary>README extract</summary>

Password strength and validation.

Example:
```python
from password_strength import PasswordPolicy

policy = PasswordPolicy.from_names(
    length=8,  # min length: 8
    uppercase=2,  # need min. 2 uppercase letters
    numbers=2,  # need min. 2 digits
    special=2,  # need min. 2 special characters
    nonletters=2,  # need min. 2 non-letter characters (digits, specials, anything)
)
```

Sections: Password Strength, Tutorial, Uppercase, Numbers, Special Characters, So-Called Entropy Bits, Complexity, PasswordPolicy, tests.EntropyBits(bits), tests.Length(length), tests.NonLetters(count), tests.NonLettersLc(count), tests.Numbers(count), tests.Special(count), tests.Strength(strength, weak_bits=30), tests.Uppercase(count)

</details>

### ssh-python

libssh C library bindings for Python.

`pip install ssh-python` · installs (wheel) · licence: LGPL-2.1-only · rank 7526 · last release 2025-10-12 · [PyPI](https://pypi.org/project/ssh-python/)

_README extract left out: share-alike licence._

### parallel-ssh

Asynchronous parallel SSH library

`pip install parallel-ssh` · installs (wheel) · licence: LGPL-2.1-only · rank 7538 · last release 2025-10-14 · [PyPI](https://pypi.org/project/parallel-ssh/)

_README extract left out: share-alike licence._

### simplefix

Simple FIX Protocol implementation for Python

`pip install simplefix` · installs (wheel) · licence: MIT License · rank 7548 · last release 2023-09-12 · [PyPI](https://pypi.org/project/simplefix/)

<details><summary>README extract</summary>

Build StatusDocsCoveragePython|
PyPIPePY DownloadsPePY Monthly|

FIX
(Financial Information eXchange) Protocol is a widely-used,
text-based protocol for interaction between parties in financial
trading. Banks, brokers, clearing firms, exchanges, and other general
market participants use FIX protocol for all phases of electronic
trading. ...

Example:
```python
msg = simplefix.FixMessage()
```

Sections: simplefix, Introduction, Basic Usage, Creating Messages, Parsing Messages

</details>

### rasa-sdk

Open source machine learning framework to automate text- and voice-based conversations: NLU, dialogue management, connect to Slack, Facebook, and more - Create chatbots and voice assistants

`pip install rasa-sdk` · installs (wheel) · licence: Apache Software License · rank 7550 · last release 2026-10-28 · [PyPI](https://pypi.org/project/rasa-sdk/) · [docs](https://rasa.com/docs) · [source](https://github.com/rasahq/rasa-sdk)

<details><summary>README extract</summary>

Python SDK for the development of custom actions for Rasa.

<hr />

💡 We're migrating issues to Jira 💡

Starting January 2023, issues for Rasa Open Source are located in
this Jira board. You can browse issues without being logged in;
if you want to create issues, you'll need to create a Jira account.

<hr />

Sections: Rasa Python-SDK, Compatibility, Usage, Docker, Custom Dependencies, Building from source, Code Style

</details>

### pydantic-to-pyarrow

Conversion from pydantic models to pyarrow schemas

`pip install pydantic-to-pyarrow` · installs (wheel) · licence: MIT License · rank 7575 · last release 2025-01-31 · [PyPI](https://pypi.org/project/pydantic-to-pyarrow/) · [source](https://github.com/simw/pydantic-to-pyarrow)

<details><summary>README extract</summary>

pydantic-to-pyarrow is a library for Python to help with conversion
of pydantic models to pyarrow schemas.

(Please note that this project is not affiliated in any way with the
great teams at pydantic or
pyarrow.)

pydantic is a Python library
for data validation, applying type hints / annotations. ...

Example:
```python
from typing import Dict, List, Optional

from pydantic import BaseModel, Field
from pydantic_to_pyarrow import get_pyarrow_schema

class NestedModel(BaseModel):
    str_field: str

class MyModel(BaseModel):
    int_field: int
    opt_str_field: Optional[str]
    py310_opt_str_field: str | None
    nested: List[NestedModel]
...
```

Sections: pydantic-to-pyarrow, Conversion Table, Settings, An Example

</details>

### cchecksum

An ~18x faster drop-in replacement for eth_utils.to_checksum_address. Raises the exact same Exceptions. Implemented in C.

`pip install cchecksum` · installs (wheel) · licence: MIT · rank 7585 · last release 2026-10-26 · [PyPI](https://pypi.org/project/cchecksum/)

<details><summary>README extract</summary>

CChecksum is an ~18x faster drop-in replacement for `eth_utils.to_checksum_address`, with the most cpu-intensive part implemented in C.

It keeps the exact same API as the existing implementation, exceptions and all.

Just `pip install cchecksum`, drop it in, and run your script with a substantial speed improvement. ...

</details>

### nagisa

A Japanese tokenizer based on recurrent neural networks

`pip install nagisa` · installs (wheel) · licence: MIT · rank 7604 · last release 2026-11-03 · [PyPI](https://pypi.org/project/nagisa/) · [docs](https://nagisa.readthedocs.io/en/latest/) · [source](https://github.com/taishi-i/nagisa)

<details><summary>README extract</summary>

Nagisa is a python module for Japanese word segmentation/POS-tagging.

It is designed to be a simple and easy-to-use tool.

This tool has the following features.
- Based on recurrent neural networks.
- The word segmentation model uses character- and word-level features [[池田+]](
- The POS-tagging model uses tag dictionary information [[Inoue+]]( ...

Example:
```python
import nagisa

text = 'Pythonで簡単に使えるツールです'
words = nagisa.tagging(text)
print(words)
# => Python/名詞 で/助詞 簡単/形状詞 に/助動詞 使える/動詞 ツール/名詞 です/助動詞

# Get a list of words
print(words.words)
# => ['Python', 'で', '簡単', 'に', '使える', 'ツール', 'です']

# Get a list of POS-tags
print(words.postags)
# => ['名詞', '助詞', '形状詞', '助動詞', '動詞', '名詞', '助動詞']
```

Sections: Basic usage, Post-processing functions, Train a model

</details>

### dom-toml

Dom's tools for Tom's Obvious, Minimal Language.

`pip install dom-toml` · installs (wheel) · licence: MIT License · rank 7616 · last release 2026-01-22 · [PyPI](https://pypi.org/project/dom-toml/) · [docs](https://dom-toml.readthedocs.io/en/latest) · [source](https://github.com/domdfcoding/dom_toml)

### ibmmq

Python Extension for IBM MQ

`pip install ibmmq` · installs (wheel) · licence: Python-2.0 · rank 7622 · last release 2026-10-13 · [PyPI](https://pypi.org/project/ibmmq/)

<details><summary>README extract</summary>

The "ibmmq" package is an open-source Python extension for IBM MQ.

It gives a full-featured implementation of the MQI programming interface, with additional
helper functions to assist with system monitoring and management.

To put a message on a queue:

To read the message back from the queue: ...

Example:
```python
import ibmmq

queue_manager = ibmmq.connect('QM1', 'DEV.APP.SVRCONN', '192.168.1.121(1414)')

q = ibmmq.Queue(queue_manager, 'DEV.QUEUE.1')
q.put('Hello from Python!')
```

Sections: Python library for IBM MQ, Sample code

</details>

### rpaframework

A collection of tools and libraries for RPA

`pip install rpaframework` · installs (wheel) · licence: Apache Software License · rank 7637 · last release 2026-11-02 · [PyPI](https://pypi.org/project/rpaframework/) · [docs](https://rpaframework.org/) · [source](https://github.com/robocorp/rpaframework)

<details><summary>README extract</summary>

`RPA Framework` is a collection of open-source libraries and tools for
Robotic Process Automation (RPA), and it is designed to be used with both
Robot Framework and Python. The goal is to offer well-documented and
actively maintained core libraries for Software Robot Developers.

Learn more about RPA at Robocorp Documentation.

The project is: ...

Example:
```python
from RPA.Browser.Selenium import Selenium

lib = Selenium()

lib.open_available_browser("
lib.input_text("id:user-name", username)
lib.input_text("id:password", password)
```

Sections: RPA Framework, Introduction, Links, Packages, Libraries, Example, . `uv run python -m robot <ROBOT_ARGS> <TARGET_ROBOT_FILE>`, . `uv run python <TARGET_PYTHON_FILE>`, . git commit changes, . git push changes to remote

</details>

### setoptconf-tmp

A module for retrieving program settings from various sources in a consistant method.

`pip install setoptconf-tmp` · installs (wheel) · licence: MIT License · rank 7638 · last release 2021-09-08 · [PyPI](https://pypi.org/project/setoptconf-tmp/)

<details><summary>README extract</summary>

This is a fork of setoptconf .
It is a temporary solution to fix prospector
being unable to install due to setoptconf not working with setuptools >= 58 -
see the issue here.

This package is only meant as a temporary solution to fix CI builds using prosector
until setoptconf can be removed from there. ...

Example:
```python
import setoptconf as soc
```

Sections: IMPORTANT!, setoptconf-tmp

</details>

### oslash

Functional library for Functors, Applicatives, and Monads in Python 3.12+

`pip install oslash` · installs (wheel) · licence: MIT License · rank 7640 · last release 2025-11-17 · [PyPI](https://pypi.org/project/oslash/) · [source](https://github.com/dbrattli/oslash)

<details><summary>README extract</summary>

OSlash (Ø) is a library for learning and understanding functional programming in Python 3.12+. It re-implements
concepts from Learn You a Haskell for Great Good! using Python with modern type annotations. OSlash unifies
functional and object-oriented paradigms by grouping related functions within classes. ...

Example:
```python
>>> Just(2).map(lambda x: x+3)
Just 5

>>> (lambda x: x+3) % Just(2)
Just 5
```

Sections: Functors, Applicatives, And Monads in Python, ✨ What's New in 1.0, Abstract Base Classes, And Some Monads, Monadic functions, Utility functions, But why?, Examples, Tutorials

</details>

### flake8-commas

Flake8 lint for trailing commas.

`pip install flake8-commas` · installs (wheel) · licence: MIT License · rank 7654 · last release 2024-05-16 · [PyPI](https://pypi.org/project/flake8-commas/)

<details><summary>README extract</summary>

Example:
```python
lookup_table = {
    'key1': 'value',
    'key2': 'something'  # <-- missing a trailing comma
}

json_data = json.dumps({
    "key": "value",
}),                      # <-- incorrect trailing comma. json_data is now a tuple. Likely by accident.
```

Sections: Flake8 Extension to enforce better comma placement., Usage, Errors, Examples, Related tools, 4.0.0 (2024-05-16), 3.0.0 (2024-03-12), 2.0.0 (2018-03-19), 1.0.0 (2018-01-04), 0.5.1 (2018-01-02), 0.5.0 (2018-01-02), 0.4.3 (2017-04-25), 0.4.2 (2017-04-18), 0.4.1 (2017-01-18)

</details>

### pyre2

Python wrapper for Google RE2 library using Cython

`pip install pyre2` · installs (wheel) · licence: BSD-3-Clause · rank 7658 · last release 2026-09-25 · [PyPI](https://pypi.org/project/pyre2/)

<details><summary>README extract</summary>

pyre2 is a Python extension that wraps
Google's RE2 regular expression library.
The RE2 engine compiles (strictly) regular expressions to
deterministic finite automata, which guarantees linear-time behavior.

Intended as a drop-in replacement for `re`. ...

Example:
```python
try:
    import re2 as re
except ImportError:
    import re
```

Sections: Summary, Compiling from source, Platform-agnostic building with conda, Documentation, Backwards Compatibility, Performance, Tests

</details>

### retry-requests

Make requests's sessions auto-retry on failure.

`pip install retry-requests` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 7659 · last release 2023-05-28 · [PyPI](https://pypi.org/project/retry-requests/) · [docs](https://github.com/bustawin/retry-requests) · [source](https://github.com/bustawin/retry-requests)

_README extract left out: share-alike licence._

### django-seal

Allows ORM constructs to be sealed to prevent them from executing queries on attribute accesses.

`pip install django-seal` · installs (wheel) · licence: MIT License · rank 7660 · last release 2025-07-10 · [PyPI](https://pypi.org/project/django-seal/)

<details><summary>README extract</summary>

Django application providing queryset sealing capability to force appropriate usage of `only()`/`defer()` and
`select_related()`/`prefetch_related()`.

Example:
```python
# models.py
from django.db import models
from seal.models import SealableModel

class Location(SealableModel):
    latitude = models.FloatField()
    longitude = models.FloatField()

class SeaLion(SealableModel):
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
...
```

Sections: django-seal, Usage

</details>

### mmhash3

Python wrapper for MurmurHash (MurmurHash3), a set of fast and robust hash functions.

`pip install mmhash3` · installs from source (sdist only) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication · rank 7664 · last release 2022-10-29 · [PyPI](https://pypi.org/project/mmhash3/)

<details><summary>README extract</summary>

Fork of the original mmh3 library since it is unmaintained.

mmhash3 is a Python wrapper for MurmurHash (MurmurHash3), a set of fast and robust non-cryptographic hash functions invented by Austin Appleby. ...

Sections: mmhash3, How to use, 3.0.0 (2021-02-23), 2.5.1 (2017-10-31), 2.5 (2017-10-28), 2.4 (2017-05-27), 2.3.2 (2017-05-26), 2.3.1 (2015-06-07), 2.3 (2013-12-08), 2.2 (2013-03-03), 2.1 (2013-02-25), Known Issues, Unexpected results when given non 32-bit seeds, See also

</details>

### otel-extensions

Python extensions for OpenTelemetry

`pip install otel-extensions` · installs (wheel) · licence: Apache Software License · rank 7683 · last release 2024-10-21 · [PyPI](https://pypi.org/project/otel-extensions/) · [source](https://github.com/s4v4g3/otel-extensions-python)

<details><summary>README extract</summary>

OpenTelemetry Extensions for Python is a collection of helper classes, functions, and decorators to facilitate the use of the
OpenTelemetry Python API & SDK packages

Example:
```python
from otel_extensions import init_telemetry_provider, TelemetryOptions

# Provide options for telemetry provider
# Alternatively, any of the following options can be specified through
# environment variables with the equivalent name
options = TelemetryOptions(
    # OTLP receiver endpoint
    OTEL_EXPORTER_OTLP_ENDPOINT="
...
```

Sections: otel-extensions-python: OpenTelemetry Extensions for Python, Setuptools, Features, Tracer Provider Initialization, Instrumentation Decorator, Conditional span creation, Trace Context helper class, Log messages as events

</details>

### pdb-attach

A python debugger that can attach to running processes.

`pip install pdb-attach` · installs (wheel) · licence: BSD License · rank 7687 · last release 2023-09-23 · [PyPI](https://pypi.org/project/pdb-attach/) · [docs](https://github.com/smitchell556/pdb-attach) · [source](https://github.com/smitchell556/pdb-attach)

<details><summary>README extract</summary>

A python debugger that can attach to running processes.

> :exclamation: pdb-attach does not work on processes where it hasn't been imported and set up. If you just discovered this package and hope to use it on an already running process, you will need to restart the program with pdb-attach listening. ...

Example:
```python
import pdb_attach
pdb_attach.listen(50000)  # Listen on port 50000.

def do_stuff():
    ...

if name == 'main:
    do_stuff()
```

Sections: pdb-attach, Requirements, OS, Python versions, Usage

</details>

### trycourier

The official Python library for the Courier API

`pip install trycourier` · installs (wheel) · licence: Apache Software License · rank 7718 · last release 2026-10-29 · [PyPI](https://pypi.org/project/trycourier/) · [source](https://github.com/trycourier/courier-python)

<details><summary>README extract</summary>

The Courier Python SDK provides typed access to the Courier REST API from Python applications. Use it to send notifications, manage user profiles, check message status, issue JWT tokens for client-side SDKs, and more.

Example:
```python
import os
from courier import Courier

client = Courier(
    api_key=os.environ.get("COURIER_API_KEY"),  # the default, can be omitted
)

response = client.send.message(
    message={
        "to": {"user_id": "your_user_id"},
        "template": "your_template_id",
        "data": {"foo": "bar"},
    },
)
print(response.request_id)
```

Sections: Courier Python SDK, Quick Start, Documentation

</details>

### zep-cloud

The Python SDK for Zep, the context layer for AI agents.

`pip install zep-cloud` · installs (wheel) · licence: not stated · rank 7722 · last release 2026-11-02 · [PyPI](https://pypi.org/project/zep-cloud/) · [source](https://github.com/getzep/zep-python)

<details><summary>README extract</summary>

The Zep Python library provides convenient access to the Zep APIs from Python.

Example:
```python
from zep_cloud import Zep

client = Zep(
    api_key="<value>",
)

client.agent.create(
    agent_id="payments-agent",
    name="Refund a duplicate charge",
    security_domain="customer:support",
)
```

Sections: Zep Python Library, What is Zep? 💬, How Zep works, Reference, Usage, Environments, Async Client, Exception Handling, Streaming, Pagination, Advanced, Access Raw Response Data, Retries, Timeouts

</details>

### pockets

A collection of helpful Python tools!

`pip install pockets` · installs (wheel) · licence: BSD License · rank 7733 · last release 2019-11-02 · [PyPI](https://pypi.org/project/pockets/)

<details><summary>README extract</summary>

The Pockets library pulls together many of the Python helper functions I've
found useful over the years.

If you've worked on a project that exports an API and accesses a data store,
you've probably seen some code that looks like this:
There's an impedance mismatch any time you work with two different frameworks;
especially when you want to update ...

Example:
```python
# Receive a data type with underscores from some API
data_type = 'user_preference'

# Convert underscored data type to CamelCase to match the data model
model_name = camel(data_type)

# Resolve the model name into a model class
model_class = resolve(model_name, modules=["webapp.model.admin",
...
```

Sections: Pockets full of useful Python tools!, Let me check my pockets..., Downloads and Docs

</details>

### inquirer3

Collection of common interactive command line user interfaces, based on Inquirer.js

`pip install inquirer3` · installs (wheel) · licence: MIT License · rank 7735 · last release 2024-07-02 · [PyPI](https://pypi.org/project/inquirer3/) · [docs](https://python-inquirer3.readthedocs.io/en/latest/) · [source](https://github.com/guysalt/python-inquirer3)

<details><summary>README extract</summary>

[][pypi status]
[][pypi downloads]
[][read the docs]

[][tests]
[][codecov]
[][pypi status]
[][license]
[][black]

This is a fork of [magmax/python-inquirer]. This one is hopefully more responsive (Issues/PRs/...).

Collection of common interactive command line user interfaces, based on [magmax/python-inquirer]. ...

Example:
```python
import re

import inquirer3

questions = [
    inquirer3.Text('name', message="What's your name"),
    inquirer3.Text('surname', message="What's your surname"),
    inquirer3.Text('phone', message="What's your phone number",
                   validate=lambda _, x: re.match('\+?\d[\d ]+\d', x),
                   )
]
...
```

Sections: python-inquirer3, Goal and Philosophy, Documentation, Text, Editor, List, Checkbox, Path

</details>

### rpaframework-core

Core utilities used by RPA Framework

`pip install rpaframework-core` · installs (wheel) · licence: Apache Software License · rank 7738 · last release 2026-11-01 · [PyPI](https://pypi.org/project/rpaframework-core/) · [docs](https://rpaframework.org/) · [source](https://github.com/robocorp/rpaframework)

<details><summary>README extract</summary>

This package is a set of core functionality and utilities used
by RPA Framework. It is not intended to be installed directly, but
as a dependency to other projects.

</details>

### junos-eznc

Junos 'EZ' automation for non-programmers

`pip install junos-eznc` · installs (wheel) · licence: Apache Software License · rank 7743 · last release 2026-11-03 · [PyPI](https://pypi.org/project/junos-eznc/)

### django-bootstrap4

Bootstrap 4 for Django

`pip install django-bootstrap4` · installs (wheel) · licence: BSD-3-Clause · rank 7753 · last release 2026-10-11 · [PyPI](https://pypi.org/project/django-bootstrap4/) · [docs](https://django-bootstrap4.readthedocs.io/) · [source](https://github.com/zostera/django-bootstrap4)

<details><summary>README extract</summary>

Bootstrap 4 for Django.

The goal of this project is to seamlessly blend Django and Bootstrap 4.

Bootstrap 4 has been superseded by Bootstrap 5. As a result, this package is now in maintenance mode and will only receive bug fixes and security updates. No new features or enhancements will be added. ...

Sections: django-bootstrap4, Goal, Maintenance Mode, Requirements, Documentation, Example template, Example app, Bugs and suggestions

</details>

### http-message-signatures

An implementation of the IETF HTTP Message Signatures draft standard

`pip install http-message-signatures` · installs (wheel) · licence: Apache Software License · rank 7757 · last release 2026-10-26 · [PyPI](https://pypi.org/project/http-message-signatures/)

<details><summary>README extract</summary>

*http-message-signatures* is an implementation of the IETF
RFC 9421 HTTP Message Signatures standard in
Python.

Example:
```python
import requests
from http_message_signatures import HTTPMessageSigner, HTTPMessageVerifier, HTTPSignatureKeyResolver, algorithms

class MyHTTPSignatureKeyResolver(HTTPSignatureKeyResolver):
    keys = {"my-key": b"top-secret-key"}

    def resolve_public_key(self, key_id: str):
        return self.keys[key_id]

...
```

Sections: Synopsis, Integrations, Requests, HTTPX2 integration, Signing only or verification only, aiohttp integration, aiohttp servers, Remote and asynchronous signing, Structured Field serialization, Binary wrapping and Set-Cookie, URL components, Multiple signatures, Error handling, Links

</details>

### steel-sdk

The official Python library for the steel API

`pip install steel-sdk` · installs (wheel) · licence: Apache Software License · rank 7767 · last release 2026-11-07 · [PyPI](https://pypi.org/project/steel-sdk/) · [source](https://github.com/steel-dev/sdk)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Steel Python library provides convenient access to the Steel REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

The REST API documentation can be found on docs.steel.dev. ...

Example:
```python
import os
from steel import Steel

client = Steel(
    steel_api_key=os.environ.get("STEEL_API_KEY"),  # This is the default and can be omitted
)

session = client.sessions.create(
    api_timeout=20000,
    use_proxy=True,
)
print(session.id)
```

...

</details>

### django-bootstrap3

Bootstrap 3 for Django

`pip install django-bootstrap3` · installs (wheel) · licence: BSD-3-Clause · rank 7772 · last release 2026-10-11 · [PyPI](https://pypi.org/project/django-bootstrap3/) · [docs](https://django-bootstrap3.readthedocs.io/) · [source](https://github.com/zostera/django-bootstrap3)

<details><summary>README extract</summary>

Bootstrap 3 for Django.

The goal of this project is to seamlessly blend Django and Bootstrap 3.

Bootstrap 3 has been superseded by Bootstrap 4, which has since been superseded by Bootstrap 5. As a result, this package is now in maintenance mode and will only receive bug fixes and security updates. No new features or enhancements will be added. ...

Sections: django-bootstrap3, Goal, Maintenance Mode, Requirements, Documentation, Example template, Example app, Bugs and suggestions

</details>

### mongodb-migrations

A database migration tool for MongoDB

`pip install mongodb-migrations` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 7786 · last release 2024-05-13 · [PyPI](https://pypi.org/project/mongodb-migrations/)

_README extract left out: share-alike licence._

### pytest-ruff

pytest plugin to check ruff requirements.

`pip install pytest-ruff` · installs (wheel) · licence: not stated · rank 7791 · last release 2025-06-19 · [PyPI](https://pypi.org/project/pytest-ruff/)

<details><summary>README extract</summary>

A pytest plugin to run ruff.

Sections: pytest-ruff, Usage, Configuration

</details>

### nacos-sdk-python

Python client for Nacos.

`pip install nacos-sdk-python` · installs (wheel) · licence: Apache License 2.0 · rank 7823 · last release 2026-04-27 · [PyPI](https://pypi.org/project/nacos-sdk-python/) · [docs](https://github.com/nacos-group/nacos-sdk-python) · [source](https://github.com/nacos-group/nacos-sdk-python)

<details><summary>README extract</summary>

English | 简体中文

A Python implementation of Nacos OpenAPI.

see:

Example:
```python
from v2.nacos import NacosNamingService, NacosConfigService, NacosAIService, ClientConfigBuilder, GRPCConfig, \
    Instance, SubscribeServiceParam, RegisterInstanceParam, DeregisterInstanceParam, \
    BatchRegisterInstanceParam, GetServiceParam, ListServiceParam, ListInstanceParam, ConfigParam
...
```

Sections: nacos-sdk-python v3, Client Configuration, Config Client, config client common parameters, Get Config, Add Listener, Remove Listener, Publish Config, Remove Config, Stop Config Client, Naming Client, Register Instance, Batch Register Instance, Deregister Instance

</details>

### azure-iot-hub

Microsoft Azure IoTHub Service Library

`pip install azure-iot-hub` · installs (wheel) · licence: MIT License · rank 7835 · last release 2025-08-06 · [PyPI](https://pypi.org/project/azure-iot-hub/)

<details><summary>README extract</summary>

The Azure IoTHub Service SDK for Python provides functionality for communicating with the Azure IoT Hub.

Features:
The SDK provides the following clients:

* ### IoT Hub Registry Manager

 * Provides CRUD operations for device on IoTHub
 * Get statistics about the IoTHub service and devices

Example:
```python
>>> from azure.iot.hub import IoTHubRegistryManager
>>> help(IoTHubRegistryManager)
```

Sections: Azure IoTHub Service SDK, Features, IoTHub Samples, Getting help and finding API docs

</details>

### wemake-python-styleguide

The strictest and most opinionated python linter ever

`pip install wemake-python-styleguide` · installs (wheel) · licence: MIT License · rank 7839 · last release 2026-09-12 · [PyPI](https://pypi.org/project/wemake-python-styleguide/) · [source](https://github.com/wemake-services/wemake-python-styleguide)

<details><summary>README extract</summary>

Welcome to the strictest and most opinionated Python linter ever.

*The best tool to teach your LLM how to write idiomatic and simple Python code!*

`wemake-python-styleguide` is actually a flake8
plugin, the only one you will need as your ruff companion.

Fully compatible with ALL rules and format conventions from `ruff`.

Sections: wemake-python-styleguide, Quickstart, AI Features, Running, Strict is the new cool, What we are about, What we are not, Show your style :sunglasses, Markdown, Restructured text

</details>

### yamlloader

Ordered YAML loader and dumper for PyYAML.

`pip install yamlloader` · installs (wheel) · licence: MIT License · rank 7843 · last release 2025-11-10 · [PyPI](https://pypi.org/project/yamlloader/) · [docs](https://yamlloader.readthedocs.io/)

<details><summary>README extract</summary>

This module provides loaders and dumpers for PyYAML. Currently, an OrderedDict loader/dumper is
implemented, allowing to keep items order
when loading resp. dumping a file from/to an OrderedDict (Python 3.8+: Also regular dicts are supported and are the default items to be loaded to. ...

Example:
```python
import yaml
import yamlloader

with open('myfile.yml') as yaml_file:
    data = yaml.load(yaml_file,
                     Loader=yamlloader.ordereddict.CLoader)
                     # CLoader is faster than Loader
```

Sections: yamlloader, But does [your special case here] also work?, C vs non-C version, Usage examples, Loader usage, Dumper usage, FAQ, C version not working

</details>

### implicit

Collaborative Filtering for Implicit Feedback Datasets

`pip install implicit` · installs (wheel) · licence: MIT · rank 7847 · last release 2026-05-14 · [PyPI](https://pypi.org/project/implicit/)

<details><summary>README extract</summary>

Fast Python Collaborative Filtering for Implicit Datasets.

This project provides fast Python implementations of several different popular recommendation algorithms for
implicit feedback datasets: ...

Example:
```python
import implicit

# initialize a model
model = implicit.als.AlternatingLeastSquares(factors=50)

# train the model on a sparse matrix of user/item/confidence weights
model.fit(user_item_data)

# recommend items for a user
recommendations = model.recommend(userid, user_item_data[userid])

# find related items
related = model.similar_items(itemid)
```

Sections: Implicit, Basic Usage, Articles about Implicit, Requirements, Benchmarks, Optimal Configuration

</details>

### attr

Simple decorator to set attributes of target function or class in a DRY way.

`pip install attr` · installs (wheel) · licence: MIT License · rank 7849 · last release 2022-07-13 · [PyPI](https://pypi.org/project/attr/)

<details><summary>README extract</summary>

Usage example::

 # Django proposes:
 def my_calculated_field(...
 my_calculated_field.short_description = 'Field'
 my_calculated_field.admin_order_field = 'real_field'

 # DRY:
 @attr(short_description='Field', admin_order_field='real_field')
 def my_calculated_field(...

Get it::

 sudo pip install attr
 from attr import attr ...

</details>

### nemo-switchyard

Typed, composable LLM routing with request/response translation and multi-backend orchestration

`pip install nemo-switchyard` · installs (wheel) · licence: Apache-2.0 · rank 7861 · last release 2026-09-22 · [PyPI](https://pypi.org/project/nemo-switchyard/) · [source](https://github.com/NVIDIA-NeMo/Switchyard)

<details><summary>README extract</summary>

Switchyard routes each LLM call to the cheapest model that can still do the job. Without changing a line of your agent.

Get started →

_\*Total cost based on average ISP token cost

Switchyard picks which model serves each LLM call.

Switchyard runs inside gateways you may already have.

- NeMo Relay — a native plugin. ...

Example:
```python
from switchyard.libsy import LlmResponse, Step
from switchyard.libsy.algorithms import stage_router

algorithm = stage_router(picker="efficient_first", confidence_threshold=0.5)
```

...

</details>

### zuban

Zuban - The Zuban Language Server

`pip install zuban` · installs (wheel) · licence: AGPL-3.0-only · rank 7864 · last release 2026-10-29 · [PyPI](https://pypi.org/project/zuban/) · [docs](https://docs.zubanls.com) · [source](https://github.com/zubanls/zubanls-python)

_README extract left out: share-alike licence._

### rpaframework-pdf

PDF library of RPA Framework

`pip install rpaframework-pdf` · installs (wheel) · licence: Apache Software License · rank 7894 · last release 2026-11-01 · [PyPI](https://pypi.org/project/rpaframework-pdf/) · [docs](https://rpaframework.org/) · [source](https://github.com/robocorp/rpaframework)

<details><summary>README extract</summary>

This library enables various PDF features with RPA Framework
libraries, such as locating text by label.

</details>

### prefect-snowflake

Prefect integrations for interacting with Snowflake

`pip install prefect-snowflake` · installs (wheel) · licence: Apache Software License · rank 7900 · last release 2026-09-08 · [PyPI](https://pypi.org/project/prefect-snowflake/)

### PyRTF3

PyRTF - Rich Text Format Document Generation

`pip install PyRTF3` · installs (wheel) · licence: GNU General Public License (GPL) · rank 7902 · last release 2017-05-19 · [PyPI](https://pypi.org/project/PyRTF3/)

_README extract left out: share-alike licence._

### pytest-redis

Redis fixtures and fixture factories for Pytest.

`pip install pytest-redis` · installs (wheel) · licence: LGPL-3.0-or-later · rank 7916 · last release 2026-10-07 · [PyPI](https://pypi.org/project/pytest-redis/) · [source](https://github.com/dbfixtures/pytest-redis)

_README extract left out: share-alike licence._

### mozprocess

Mozilla-authored process handling

`pip install mozprocess` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 7919 · last release 2024-08-19 · [PyPI](https://pypi.org/project/mozprocess/)

### odfdo

Python library for OpenDocument Format

`pip install odfdo` · installs (wheel) · licence: Apache-2.0 · rank 7927 · last release 2026-10-24 · [PyPI](https://pypi.org/project/odfdo/) · [docs](https://jdum.github.io/odfdo/) · [source](https://github.com/jdum/odfdo)

<details><summary>README extract</summary>

OpenDocument Format (ODF, ISO/IEC 26300) library for Python

`odfdo` is a Python library for programmatically creating, parsing, and editing OpenDocument Format (ODF) files. It provides an interface for interacting with `.odt`, `.ods`, `.odp`, and other ODF file types. ...

Example:
```python
from odfdo import Document, Paragraph

doc = Document("text")
doc.body.append(Paragraph("Hello world!"))

doc.save("hello.odt")
```

Sections: odfdo, Dependencies, Usage Overview, Creating a "Hello world" Text Document, Modifying a Spreadsheet, Utilities, tl;dr, Documentation, About styles, Related project, Former lpod-python library

</details>

### pyobjc-framework-CoreAudio

Wrappers for the framework CoreAudio on macOS

`pip install pyobjc-framework-CoreAudio` · installs from source (sdist only) · licence: MIT · rank 7970 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreAudio/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreAudio" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### apify

Apify SDK for Python

`pip install apify` · installs (wheel) · licence: Apache-2.0 · rank 7974 · last release 2026-11-05 · [PyPI](https://pypi.org/project/apify/) · [docs](https://docs.apify.com/sdk/python/docs/overview) · [source](https://github.com/apify/apify-sdk-python)

<details><summary>README extract</summary>

The official Python SDK for building Apify Actors.

`apify` is the official SDK for building Apify Actors in Python. It handles the Actor lifecycle, storage access, platform events, Apify Proxy, pay-per-event charging, and more. ...

Features:
- Run the full Actor lifecycle inside `async with Actor:`, covering init, exit, failures, status messages, and reboots (Actor lifecycle).
- Read Actor input validated against your input schema with `Actor.get_input()` (Actor input). ...

Example:
```python
from apify import Actor

async def main() -> None:
    async with Actor:
        actor_input = await Actor.get_input()
        Actor.log.info('Actor input: %s', actor_input)
        await Actor.set_value('OUTPUT', 'Hello, world!')
```

...

</details>

### daal

Intel® oneAPI Data Analytics Library

`pip install daal` · installs (wheel) · licence: Other/Proprietary License · rank 7975 · last release 2026-10-16 · [PyPI](https://pypi.org/project/daal/)

<details><summary>README extract</summary>

Intel® oneAPI Data Analytics Library (Intel® oneDAL) is the library of Intel® architecture optimized building blocks covering all stages of data analytics: data acquisition from a data source, preprocessing, transformation, data mining, modeling, validation, and decision making.

</details>

### spectree

Generate OpenAPI document and validate request & response with Python annotations.

`pip install spectree` · installs (wheel) · licence: Apache-2.0 · rank 7985 · last release 2026-09-10 · [PyPI](https://pypi.org/project/spectree/) · [docs](https://0b01001001.github.io/spectree/) · [source](https://github.com/0b01001001/spectree)

<details><summary>README extract</summary>

[][documentation]

Yet another library to generate OpenAPI documents and validate requests & responses with Python annotations.

If all you need is a framework-agnostic library that can generate OpenAPI document, check defspec.

Features:
* Less boilerplate code, only annotations, no need for YAML :sparkles:
* Generate API document with Redoc UI, Scalar UI or Swagger UI :yum:
* Validate query, JSON data, and response data with supported model backends :wink:
 * pydantic
 * msgspec
 * ...

Example:
```python
Response(HTTP_200=None, HTTP_403=ForbidModel)
Response('HTTP_200') # equals to Response(HTTP_200=None)
# with custom code description
Response(HTTP_403=(ForbidModel, "custom code description"))
```

...

</details>

### drf-pydantic

Use pydantic with the Django REST framework

`pip install drf-pydantic` · installs (wheel) · licence: MIT · rank 8000 · last release 2026-10-31 · [PyPI](https://pypi.org/project/drf-pydantic/) · [source](https://github.com/georgebv/drf-pydantic)

<details><summary>README extract</summary>

Use pydantic with Django REST framework

- Introduction
 - Performance
- Installation
- Usage
 - General
 - Pydantic Validation
 - Updating Field Values
 - Validation Errors
 - Accessing the Validated Pydantic Instance
 - Existing Models
 - Nested Models
 - Manual Serializer Configuration
 - Per-Field Configuration
 - Custom Serializer ...

Example:
```python
from drf_pydantic import BaseModel

class MyModel(BaseModel):
    name: str
    addresses: list[str]
```

Sections: Introduction, Performance, Usage, General, Pydantic Validation, Updating Field Values, Validation Errors, Accessing the Validated Pydantic Instance, Existing Models, Nested Models, Manual Serializer Configuration, Per-Field Configuration, Custom Serializer, Additional Properties

</details>

### smpclient

Simple Management Protocol (SMP) Client for remotely managing MCU firmware

`pip install smpclient` · installs (wheel) · licence: Apache-2.0 · rank 8014 · last release 2026-07-06 · [PyPI](https://pypi.org/project/smpclient/) · [docs](https://intercreate.github.io/smpclient) · [source](https://github.com/intercreate/smpclient.git)

<details><summary>README extract</summary>

Sections: User Documentation, Server Buffers & SMP Serial Fragmentation, The SMP serial frame, Terminology (mcuboot vs. Zephyr), How smpclient targets these, Create the venv, Verify Your Setup, Enable the githooks

</details>

### iso-week-date

Toolkit to work with str representing ISO Week date format

`pip install iso-week-date` · installs (wheel) · licence: MIT · rank 8015 · last release 2026-04-01 · [PyPI](https://pypi.org/project/iso-week-date/) · [docs](https://fbruzzesi.github.io/iso-week-date/) · [source](https://github.com/fbruzzesi/iso-week-date)

<details><summary>README extract</summary>

iso-week-date is a toolkit to work with strings representing ISO Week date
in two formats, namely:

* Week format YYYY-WNN (date format %Y-W%V)
* Week date format YYYY-WNN-D (date format %Y-W%V-%u)

where _YYYY_ represents the year, _W_ is a string literal, _NN_ represents the week number, and _D_ represents the day
of the week. ...

Sections: ISO Week Date, Dependencies, Getting Started, Available features, Quickstart, Custom offset

</details>

### path.py

A module wrapper for os.path

`pip install path.py` · installs (wheel) · licence: MIT License · rank 8035 · last release 2020-07-27 · [PyPI](https://pypi.org/project/path.py/)

### walrus

a set of utilities for working with redis

`pip install walrus` · installs (wheel) · licence: not stated · rank 8040 · last release 2026-01-15 · [PyPI](https://pypi.org/project/walrus/) · [docs](https://walrus.readthedocs.io/) · [source](https://github.com/coleifer/walrus)

<details><summary>README extract</summary>

Lightweight Python utilities for working with Redis.

The purpose of walrus is to make working
with Redis in Python a little easier. Rather than ask you to learn a new
library, walrus subclasses and extends the popular `redis-py` client, allowing
it to be used as a drop-in replacement. ...

Sections: Walrus, Models, Found a bug?

</details>

### neotime

Nanosecond resolution temporal types

`pip install neotime` · installs from source (sdist only) · licence: Apache Software License · rank 8049 · last release 2018-12-04 · [PyPI](https://pypi.org/project/neotime/)

<details><summary>README extract</summary>

The `neotime` module defines classes for working with temporal data to nanosecond precision.
These classes comprise a similar set to that provided by the standard library `datetime` module.
Inspiration has also been drawn from ISO-8601.

Features:
The classes are listed below:

* Duration
* Date
* Time
* DateTime
* TODO

Sections: Neotime, Overview, More Information

</details>

### sodapy

Python library for the Socrata Open Data API

`pip install sodapy` · installs (wheel) · licence: MIT License · rank 8052 · last release 2022-08-31 · [PyPI](https://pypi.org/project/sodapy/)

<details><summary>README extract</summary>

:rotating_light: NOTICE: sodapy still works well, but is unmaintained as of Aug 31, 2022. No new features or bugfixes will be added. Use at your own risk.

sodapy is a python client for the Socrata Open Data API.

Example:
```python
files = (
    {'file': ("gtfs2", open('myfile.zip', 'rb'))}
)
```

Sections: sodapy - UNMAINTAINED, Requirements, Documentation, Examples, Interface, client, datasets(limit=0, offset=0), get(dataset_identifier, content_type="json", **kwargs), get_all(dataset_identifier, content_type="json", **kwargs), get_metadata(dataset_identifier, content_type="json"), create(name, **kwargs), publish(dataset_identifier, content_type="json"), upsert(dataset_identifier, payload, content_type="json"), replace(dataset_identifier, payload, content_type="json")

</details>

### solace-pubsubplus

Solace Messaging API for Python.

`pip install solace-pubsubplus` · installs (wheel) · licence: Apache Software License · rank 8063 · last release 2026-11-05 · [PyPI](https://pypi.org/project/solace-pubsubplus/)

<details><summary>README extract</summary>

This package contains the Solace Messaging API for Python.

The Solace Messaging API for Python is developed and supported by the Solace Corporation.

The API provides access to Solace Messaging Service, supporting a variety of Message Exchange Patterns.

Sections: Dependencies, Documentation, Introduction, MessagingService, MessageReceiver, Samples, multiprocessing

</details>

### dearpygui

DearPyGui: A simple Python GUI Toolkit

`pip install dearpygui` · installs (wheel) · licence: MIT License · rank 8066 · last release 2026-05-01 · [PyPI](https://pypi.org/project/dearpygui/)

<details><summary>README extract</summary>

Features •
 Installation •
 How To Use •
 Demo •
 Resources •
 Support •
 Tech stack •
 Credits •
 License •
 Gallery

Features:
- Modern look — Complete theme and style control
- Great performance — GPU-based rendering and efficient C/C++ code
- Stable operation — Asynchronous function support
- Fast graphs — Display over 1 million datapoints at 60 fps, zoom and pan ...

Example:
```python
import dearpygui.dearpygui as dpg

def save_callback():
    print("Save Clicked")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="Example Window"):
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string")
...
```

...

</details>

### PyArtifactory

Typed interactions with the Jfrog Artifactory REST API

`pip install PyArtifactory` · installs (wheel) · licence: MIT License · rank 8083 · last release 2025-09-23 · [PyPI](https://pypi.org/project/PyArtifactory/) · [docs](https://github.com/anancarv/python-artifactory) · [source](https://github.com/anancarv/python-artifactory)

<details><summary>README extract</summary>

`pyartifactory` is a Python library to access the Artifactory REST API.

This library enables you to manage Artifactory resources such as users, groups, permissions, repositories, artifacts and access tokens in your applications. Based on Python 3.8+ type hints.

<!-- toc -->

- Requirements
- Install ...

Example:
```python
from pyartifactory import Artifactory
art = Artifactory(url="ARTIFACTORY_URL", auth=('USERNAME','PASSWORD_OR_API_KEY'), api_version=1)
```

Sections: PyArtifactory, Requirements, Usage, Authentication, Basic authentication, Authentication with access token, SSL Cert Verification Options, Timeout option, Admin objects, User, Group, Repository, Permission, Artifactory lower than 6.6.0

</details>

### pyobjc-framework-CoreBluetooth

Wrappers for the framework CoreBluetooth on macOS

`pip install pyobjc-framework-CoreBluetooth` · installs from source (sdist only) · licence: MIT · rank 8085 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreBluetooth/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreBluetooth" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### warlock

Python object model built on JSON schema and JSON patch.

`pip install warlock` · installs (wheel) · licence: Apache-2.0 · rank 8093 · last release 2025-05-30 · [PyPI](https://pypi.org/project/warlock/) · [source](http://github.com/bcwaldon/warlock)

<details><summary>README extract</summary>

Create self-validating Python objects using JSON schema.

[][warlock]
[][warlock]
[][pypistats]

[][ci-builds]
[][coveralls]

[][poetry]

Example:
```python
>>> schema = {
    'name': 'Country',
    'properties': {
        'name': {'type': 'string'},
        'abbreviation': {'type': 'string'},
        'population': {'type': 'integer'},
    },
    'additionalProperties': False,
}
```

Sections: Warlock 🧙‍♀️, Usage

</details>

### bravado

Library for accessing Swagger-enabled API's

`pip install bravado` · installs from source (sdist only) · licence: BSD License · rank 8103 · last release 2025-05-07 · [PyPI](https://pypi.org/project/bravado/)

<details><summary>README extract</summary>

Bravado is a Yelp maintained fork of digium/swagger-py
for use with OpenAPI Specification version 2.0 (previously
known as Swagger).

From the OpenAPI Specification project:

 The goal of The OpenAPI Specification is to define a standard,
 language-agnostic interface to REST APIs which allows both humans and
 computers to discover and understand ...

Example:
```python
from bravado.client import SwaggerClient
client = SwaggerClient.from_url('
pet = client.pet.getPetById(petId=1).response().result
```

Sections: Bravado, About, Example Usage, Example with Basic Authentication, Example with Header Authentication, Example with Fido Client (Async Http Client), Documentation, Setup, Releasing a new version (Yelpers only)

</details>

### pyobjc-framework-libdispatch

Wrappers for libdispatch on macOS

`pip install pyobjc-framework-libdispatch` · installs from source (sdist only) · licence: MIT · rank 8105 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-libdispatch/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "dispatch" library on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### django-eagle

Prevent Django ORM Unused Eager Loads

`pip install django-eagle` · installs (wheel) · licence: MIT · rank 8120 · last release 2026-06-17 · [PyPI](https://pypi.org/project/django-eagle/) · [source](https://github.com/xelixdev/django-eagle)

<details><summary>README extract</summary>

Catch wasted eager loads in your Django ORM queries.

When you `select_related(...)` or `prefetch_related(...)` a relation but never actually read it during a request, you've paid for a join or extra query for nothing. `django-eagle` watches relation access per request and warns you about eager loads that were never used.

Example:
```python
# views.py
def eagle_detail(request, pk):
    # select_related("location") joins the location table...
    eagle = Eagle.objects.select_related("location").get(pk=pk)

    # ...but the response only reads eagle.name — location is never touched.
    return JsonResponse({"name": eagle.name})
```

...

</details>

### mo-dots

More Dots! Dot-access to Python dicts like Javascript

`pip install mo-dots` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 8144 · last release 2026-11-07 · [PyPI](https://pypi.org/project/mo-dots/)

<details><summary>README extract</summary>

Features:
Box your JSON-like data in a `Data` object to get null-safe dot access. This library is a replacement for `dict` that is more consistent and easier to use.

> See full documentation for all the features of `mo-dots` ...

Sections: More Dots!, Overview, Create instances, Dot Access, Path Access, Null-Safe Access, Path assignment, Path accumulation, Serializing to JSON, Using with Claude Code, Summary

</details>

### oic

Python implementation of OAuth2 and OpenID Connect

`pip install oic` · installs (wheel) · licence: Apache Software License · rank 8147 · last release 2024-04-25 · [PyPI](https://pypi.org/project/oic/)

<details><summary>README extract</summary>

This is a complete implementation of OpenID Connect as specified in the OpenID
Connect Core specification. And as a side effect, a complete implementation
of OAuth2.0 too.

Please see the CHANGELOG.md to review the latest changes.

The documentation is graciously hosted by Read the Docs. ...

Sections: A Python OpenID Connect implementation, Documentation, Examples, Windows

</details>

### graphql-query

Complete Domain Specific Language (DSL) for GraphQL query in Python.

`pip install graphql-query` · installs (wheel) · licence: MIT License · rank 8148 · last release 2024-07-31 · [PyPI](https://pypi.org/project/graphql-query/) · [docs](https://denisart.github.io/graphql-query/) · [source](https://github.com/denisart/graphql-query)

<details><summary>README extract</summary>

graphql_query is a complete Domain Specific Language (DSL) for GraphQL query in Python. With this package
you can to

- generate a correct GraphQL query string from a python classes;
- use and share similar Arguments, Variables and e.t.c between different queries;
- easily add new fields to your query;
- add Fragments and Directives to queries; ...

Example:
```python
from graphql_query import Operation, Query

hero = Query(name="hero", fields=["name"])
operation = Operation(type="query", queries=[hero])

print(operation.render())
"""
query {
  hero {
    name
  }
}
"""
```

Sections: graphql-query, Quickstart, Simple query, Arguments, Variables and Directives

</details>

### looptime

Fast-forward asyncio event loop time (in tests)

`pip install looptime` · installs (wheel) · licence: MIT · rank 8160 · last release 2026-10-14 · [PyPI](https://pypi.org/project/looptime/) · [docs](https://github.com/nolar/looptime) · [source](https://github.com/nolar/looptime)

<details><summary>README extract</summary>

Fake the flow of time in asyncio event loops.
The effects of time removal can be seen from both sides:

* From the event loop's (i.e. your tests') point of view,
 all external activities, such as synchronous executor calls (thread pools)
 and i/o with sockets, servers, files, happen in zero amount of the loop time —
 even if it takes some real ...

Example:
```python
import asyncio
import pytest

@pytest.mark.asyncio
async def test_me():
    await asyncio.sleep(100)
    assert asyncio.get_running_loop().time() == 100
```

Sections: Fast-forward asyncio event loop time (in tests), What is this?, What is it not?, Examples, Documentation

</details>

### fawltydeps

Find undeclared and unused 3rd-party dependencies in your Python project.

`pip install fawltydeps` · installs (wheel) · licence: not stated · rank 8162 · last release 2025-06-05 · [PyPI](https://pypi.org/project/fawltydeps/) · [docs](https://tweag.github.io/FawltyDeps/) · [source](https://github.com/tweag/FawltyDeps)

<details><summary>README extract</summary>

FawltyDeps is a dependency checker for Python that finds _undeclared_ and/or
_unused_ 3rd-party dependencies in your Python project.
The name is inspired by the Monty Python-adjacent
Fawlty Towers sitcom.

📝 Full documentation available at: tweag.github.io/FawltyDeps ...

Sections: FawltyDeps, Key Concepts, Usage

</details>

### sdbus

Modern Python D-Bus library. Based on sd-bus from libsystemd.

`pip install sdbus` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 8163 · last release 2026-08-20 · [PyPI](https://pypi.org/project/sdbus/) · [docs](https://python-sdbus.readthedocs.io/en/latest/) · [source](https://github.com/python-sdbus/python-sdbus/)

_README extract left out: share-alike licence._

### rasa

Open source machine learning framework to automate text- and voice-based conversations: NLU, dialogue management, connect to Slack, Facebook, and more - Create chatbots and voice assistants

`pip install rasa` · does not install on CPython 3.14 · licence: Apache Software License · rank 8165 · last release 2025-01-14 · [PyPI](https://pypi.org/project/rasa/) · [docs](https://rasa.com/docs) · [source](https://github.com/rasahq/rasa)

<details><summary>README extract</summary>

💡 We're migrating issues to Jira 💡

Starting January 2023, issues for Rasa Open Source are located in
this Jira board. You can browse issues without being logged in;
if you want to create issues, you'll need to create a Jira account.

Rasa is an open source machine learning framework to automate text and voice-based conversations. ...

Sections: Rasa Open Source, Where to get help, Managing environments, Building from source, Running and changing the documentation, Running the Tests, Running the Integration Tests, Resolving merge conflicts, Build a Docker image locally, Code Style, Formatting, Type Checking, Deploying documentation updates, Maintenance Policy

</details>

### pydo

The official client for interacting with the DigitalOcean API

`pip install pydo` · installs (wheel) · licence: Apache Software License · rank 8173 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pydo/) · [docs](https://pydo.readthedocs.io/) · [source](https://github.com/digitalocean/pydo)

<details><summary>README extract</summary>

`pydo` is the official Python client library that allows
Python developers to interact with and manage their DigitalOcean
resources through a Python abstraction layer on top of the raw
DigitalOcean API HTTP Interface.

A top priority of this project is to ensure the client abides by the API
contract. ...

Example:
```python
import os
from pydo import Client

client = Client(token=os.getenv("DIGITALOCEAN_TOKEN"))
```

Sections: PyDo, Getting Started With the Client, Prerequisites, `pydo` Quickstart, Example of Using `pydo` to Access DO Resources, AI & Inference, Chat completions (streaming), Image generation, List available models, Pagination Example, Async Usage, Retries and Backoff, Tests, Mocked Tests: `tests/mocked/`

</details>

### utils

A grab-bag of utility functions and objects

`pip install utils` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 8198 · last release 2024-01-06 · [PyPI](https://pypi.org/project/utils/)

_README extract left out: share-alike licence._

### lunar-python

lunar is a calendar library for Solar and Chinese Lunar.

`pip install lunar-python` · installs from source (sdist only) · licence: MIT License · rank 8203 · last release 2026-11-05 · [PyPI](https://pypi.org/project/lunar-python/) · [docs](https://6tail.cn/calendar/api.html) · [source](https://github.com/6tail/lunar-python)

<details><summary>README extract</summary>

lunar is a calendar library for Solar and Chinese Lunar.

> Python2 not supported since v1.2.23.

简体中文

Sections: lunar, Example, Documentation

</details>

### pyclibrary

C binding automation

`pip install pyclibrary` · installs (wheel) · licence: MIT License · rank 8204 · last release 2025-09-03 · [PyPI](https://pypi.org/project/pyclibrary/) · [docs](https://pyclibrary.readthedocs.io/en/latest/) · [source](https://github.com/MatthieuDartiailh/pyclibrary)

<details><summary>README extract</summary>

C parser and bindings automation for Python.

Fork of

PyCLibrary includes 1) a pure-python C parser and 2) an automation library
that uses C header file definitions to simplify the use of c bindings. ...

</details>

### sttable

Parser of string representation tables

`pip install sttable` · installs (wheel) · licence: MIT License · rank 8215 · last release 2019-11-23 · [PyPI](https://pypi.org/project/sttable/)

<details><summary>README extract</summary>

Parser of string representation tables, input example:
Parsed information can be accessed by rows:
As well as by columns:
Fields:

</details>

### beautysh

A Bash beautifier for the masses.

`pip install beautysh` · installs (wheel) · licence: MIT License · rank 8227 · last release 2026-03-12 · [PyPI](https://pypi.org/project/beautysh/) · [source](https://github.com/lovesegfault/beautysh)

<details><summary>README extract</summary>

This program takes upon itself the hard task of beautifying Bash scripts
(yeesh). Processing Bash scripts is not trivial, they aren't like C or Java
programs — they have a lot of ambiguous syntax, and (shudder) you can use
keywords as variables. Years ago, while testing the first version of this
program, I encountered this example: ...

Example:
```python
  --indent-size INDENT_SIZE, -i INDENT_SIZE
                        Sets the number of spaces to be used in indentation.
  --backup, -b          Beautysh will create a backup file in the same path as
                        the original.
  --check, -c           Beautysh will just check the files without doing any
...
```

...

</details>

### kafka

Pure Python client for Apache Kafka

`pip install kafka` · installs (wheel) · licence: Apache Software License · rank 8230 · last release 2017-10-07 · [PyPI](https://pypi.org/project/kafka/)

<details><summary>README extract</summary>

Python client for the Apache Kafka distributed stream processing system.
kafka-python is designed to function much like the official java client, with a
sprinkling of pythonic interfaces (e.g., consumer iterators).

kafka-python is best used with newer brokers (0.9+), but is backwards-compatible with
older versions (to 0.8.0). ...

Sections: Kafka Python client, KafkaConsumer, KafkaProducer, Thread safety, Compression, Low-level

</details>

### ome-zarr

Implementation of images in Zarr files.

`pip install ome-zarr` · installs (wheel) · licence: BSD-2-Clause · rank 8238 · last release 2026-10-07 · [PyPI](https://pypi.org/project/ome-zarr/) · [docs](https://ome-zarr.readthedocs.io) · [source](https://github.com/ome/ome-zarr-py)

<details><summary>README extract</summary>

Tools for multi-resolution images stored in Zarr filesets, according to the OME NGFF spec.

See Documentation for usage information.

Documentation will be automatically built with `readthedocs`.

It can be built locally with:
Or, if you prefer using pip:

 $ pip install .[docs]
 $ sphinx-build -b html docs/source/ docs/build/

Sections: ome-zarr-py, Documentation, Tests

</details>

### lorem

Generator for random text that looks like Latin.

`pip install lorem` · installs (wheel) · licence: MIT License · rank 8245 · last release 2016-06-18 · [PyPI](https://pypi.org/project/lorem/)

<details><summary>README extract</summary>

Generator for random text that looks like Latin.

Example:
```python
import lorem

s = lorem.sentence()  # 'Eius dolorem dolorem labore neque.'
p = lorem.paragraph()
t = lorem.text()
```

Sections: Python Lorem Package, Summary, Simple Example, Complex Example, 0.1.1 (2016-06-18), 0.1.0 (2016-06-17), 0.0.1 (2016-06-14)

</details>

### wreq

An ergonomic, privacy-aware Python HTTP Client

`pip install wreq` · installs (wheel) · licence: Apache-2.0 · rank 8257 · last release 2026-10-05 · [PyPI](https://pypi.org/project/wreq/) · [docs](https://python.wreq.org) · [source](https://github.com/0x676e67/wreq-python)

<details><summary>README extract</summary>

[][discord-url]

> 🚀 Help me work seamlessly with open source sharing by sponsoring me on GitHub

An ergonomic and modular Python HTTP Client for high-fidelity protocol matching, featuring customizable TLS, JA3/JA4, and HTTP/2 signature capabilities, powered by wreq.

Features:
- Async and Blocking `Client`s
- Plain bodies, JSON, urlencoded, multipart
- HTTP Trailer
- Cookie Store
- Redirect Policy
- Original Header
- Rotating Proxies
- Connection Pooling
- Streaming Transfers
- Zero-Copy Transfers
- WebSocket Upgrade ...

Example:
```python
import asyncio
from wreq import Client, Emulation

async def main():
    async with Client(emulation=Emulation.Chrome154) as c:
        async with c.get(" as r:
            r.raise_for_status()
            print(await r.text())

if name == "main":
...

</details>

### aiodogstatsd

An asyncio-based client for sending metrics to StatsD with support of DogStatsD extension

`pip install aiodogstatsd` · installs (wheel) · licence: MIT License · rank 8265 · last release 2021-12-12 · [PyPI](https://pypi.org/project/aiodogstatsd/) · [docs](https://gr1n.github.io/aiodogstatsd) · [source](https://github.com/Gr1N/aiodogstatsd)

<details><summary>README extract</summary>

An asyncio-based client for sending metrics to StatsD with support of DogStatsD extension.

Library fully tested with statsd_exporter and supports `gauge`, `counter`, `histogram`, `distribution` and `timing` types.

`aiodogstatsd` client by default uses _9125_ port. ...

Example:
```python
import asyncio

import aiodogstatsd

async def main():
    async with aiodogstatsd.Client() as client:
        client.increment("users.online")

asyncio.run(main())
```

Sections: aiodogstatsd, At a glance

</details>

### mda-xdrlib

Stand-alone XDRLIB module (from cpython 3.10.8)

`pip install mda-xdrlib` · installs (wheel) · licence: Python Software Foundation License · rank 8267 · last release 2023-08-28 · [PyPI](https://pypi.org/project/mda-xdrlib/)

<details><summary>README extract</summary>

A stand-alone XDRLIB module extracted from cpython 3.10.8

Features:
The xdrlib package has historically been a feature of the core python library.
However, as of Python 3.11, the module was deemed to no longer be widely used
and has been deprecated, with a target removal version of Python 3.13. ...

Sections: mda_xdrlib, Why does this package exist?, Changes from the cpython implementation

</details>

### vapi-server-sdk

(no summary)

`pip install vapi-server-sdk` · installs (wheel) · licence: not stated · rank 8268 · last release 2026-10-12 · [PyPI](https://pypi.org/project/vapi-server-sdk/) · [source](https://github.com/VapiAI/server-sdk-python)

<details><summary>README extract</summary>

The Vapi Python library provides convenient access to the Vapi API from Python.

Example:
```python
import os

from vapi import Vapi

client = Vapi(token=os.environ["VAPI_API_KEY"])
assistants = client.assistants.list(limit=10)
for assistant in assistants:
    print(assistant.id)
```

Sections: Vapi Python Library, Upgrade to 3.0.0, Reference, Usage, Async Client, Exception Handling, List Resources, Advanced, Retries, Timeouts, Custom Client

</details>

### gotenberg-client

A Python client for interfacing with the Gotenberg API

`pip install gotenberg-client` · installs (wheel) · licence: MPL-2.0 · rank 8269 · last release 2026-11-05 · [PyPI](https://pypi.org/project/gotenberg-client/) · [docs](https://stumpylog.github.io/gotenberg-client/) · [source](https://github.com/stumpylog/gotenberg-client/)

<details><summary>README extract</summary>

A modern, fully-typed Python client for the Gotenberg PDF generation API, with sync and async support.

Features:
Gotenberg is a powerful, Docker-based API for PDF generation and manipulation using
Chromium and LibreOffice under the hood. This client gives you a clean, Pythonic interface to all of its
capabilities, so you can skip the multipart form-data ...

Example:
```python
from gotenberg_client import GotenbergClient
from pathlib import Path

with GotenbergClient(" as client:
    with client.chromium.html_to_pdf() as route:
        response = route.index(Path("my-index.html")).run()
        response.to_file(Path("my-index.pdf"))
```

...

</details>

### mdformat-mkdocs

An mdformat plugin for mkdocs and Material for MkDocs

`pip install mdformat-mkdocs` · installs (wheel) · licence: MIT · rank 8278 · last release 2026-08-02 · [PyPI](https://pypi.org/project/mdformat-mkdocs/)

<details><summary>README extract</summary>

[][ci-link] [][pypi-link]

An mdformat plugin for mkdocs and packages commonly used with MkDocs (mkdocs-material, mkdocstrings, and python-markdown)

In addition, mdformat-mkdocs will intentionally provide support for Zensical, which is working towards feature parity with mkdocs (as of mid-2026) and may add features ahead of mkdocs.

Supports: ...

Features:
The following MkDocs/Material/PyMdown syntax passes through mdformat-mkdocs unchanged — it is not modified or corrupted, but it is also not actively normalized:

- PyMdown Keys — `++ctrl+alt+del++` (not a markdown construct, preserved as-is) ...

Example:
```python
from markdown_it import MarkdownIt

from mdformat_mkdocs.mdit_plugins import (
    material_admon_plugin,
    material_content_tabs_plugin,
...

</details>

### IP2Location

This is an IP geolocation library that enables the user to find the country, region, city, latitude and longitude, ZIP code, time zone, ISP, domain name, area code, weather info, mobile info, elevation, usage type, address type and IAB category from an IP address. It supports both IPv4 and IPv6 lookup.

`pip install IP2Location` · installs (wheel) · licence: MIT License · rank 8280 · last release 2025-09-04 · [PyPI](https://pypi.org/project/IP2Location/)

<details><summary>README extract</summary>

This is a IP2Location Python library that enables the user to find the country, region or state, city, latitude and longitude, ZIP code, time zone, Internet Service Provider (ISP) or company name, domain name, net speed, area code, weather station code, weather station name, mobile country code (MCC), mobile network code (MNC) and carrier brand, ...

Sections: IP2Location Python Library, IP2Location BIN Databases, IPv4 versus IPv6 BIN Database, SDK or Library for Other Programming Languages

</details>

### cohere-melody

Templating rendering and generation parsing for Cohere models

`pip install cohere-melody` · installs (wheel) · licence: MIT · rank 8283 · last release 2026-10-20 · [PyPI](https://pypi.org/project/cohere-melody/) · [source](https://github.com/cohere-ai/melody)

<details><summary>README extract</summary>

Templating rendering and generation parsing for Cohere models.

1. Install Rust from rustup.rs.
2. Install rust-analyzer for IDE support.
3. `make rust-test` && `make rust-lint` to ensure everything is working.

Sections: melody, Dev Setup, Examples, Usage, Parsing, Parsing vision generations (unary), Templating, Releasing, Building Python Bindings, Prerequisites (from pyo3), Debugging

</details>

### ibm-vpc

Python client library for IBM Cloud ibm-vpc Services

`pip install ibm-vpc` · installs (wheel) · licence: Apache Software License · rank 8288 · last release 2026-10-30 · [PyPI](https://pypi.org/project/ibm-vpc/) · [docs](https://github.com/IBM/vpc-python-sdk/blob/master/README.md) · [source](https://github.com/IBM/vpc-python-sdk)

<details><summary>README extract</summary>

Python client library to interact with various IBM Cloud Virtual Private Cloud (VPC) Service APIs.

This SDK uses Semantic Versioning, and as such there may be backward-incompatible changes for any new `0.y.z` version.

Features:
The IBM Cloud Virtual Private Cloud (VPC) Python SDK allows developers to programmatically interact with the following
IBM Cloud services:

Service Name | Imported Class Name

VPC | VpcV1

Example:
```python
from ibm_vpc import VpcV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException

authenticator = IAMAuthenticator("YOUR_IBMCLOUD_API_KEY")
service = VpcV1(authenticator=authenticator)

# to change the service URL to the United Kingdom region
...
```

...

</details>

### salesforce-api

Salesforce API wrapper

`pip install salesforce-api` · installs from source (sdist only) · licence: MIT License · rank 8295 · last release 2026-01-05 · [PyPI](https://pypi.org/project/salesforce-api/)

<details><summary>README extract</summary>

This project aims to provide an easy to use, highly flexible and testable solution for communicating with Salesforce
through its REST and SOAP api.

Content

- Simple Usage
- Authentication
- Record management
 - Insert
 - Upsert
 - Update
 - Get
 - Delete
- Quering SObjects
- Bulk
- Tooling
- Deploying
- Retrieving
- Additional features ...

Example:
```python
from salesforce_api import Salesforce
client = Salesforce(
    username='test@example.com',
    password='my-password',
    security_token='password-token'
)
```

Sections: Python Salesforce API, Insert, Get, Update, Upsert, Delete, Metadata, Describe, Bulk Insert, Bulk Upsert, Bulk Update, Bulk Delete, Failed requests

</details>

### cloudant

Cloudant / CouchDB Client Library

`pip install cloudant` · installs (wheel) · licence: Apache Software License · rank 8301 · last release 2021-08-26 · [PyPI](https://pypi.org/project/cloudant/)

<details><summary>README extract</summary>

This library is now deprecated and will be end-of-life on Dec 31 2021.

The library remains supported until the end-of-life date,
but will receive only _critical_ maintenance updates.

Please see the Migration Guide for advice
about migrating to our replacement library
cloudant-python-sdk. ...

Sections: DEPRECATED, Cloudant Python Client, Getting started, API Reference, Related Documentation, Using in other projects, Examples in open source projects, Issues, Migrating to `cloudant-python-sdk` library

</details>

### readline

The standard Python readline extension statically linked against the GNU readline library.

`pip install readline` · does not install on CPython 3.14 · licence: GNU General Public License v3 (GPLv3) · rank 8302 · last release 2022-10-12 · [PyPI](https://pypi.org/project/readline/)

_README extract left out: share-alike licence._

### mo-future

More future! Make Python 2/3 compatibility a bit easier

`pip install mo-future` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 8304 · last release 2026-11-07 · [PyPI](https://pypi.org/project/mo-future/)

<details><summary>README extract</summary>

For old code written against Python2, plus some tiny useful functions

December 2022 - No longer points to Python2 modules.

Example:
```python
from future.utils import text
```

Sections: More Future!, Recent Changes, Description, Problem, Solution, Flat namespace, Simpler imports

</details>

### ibm-secrets-manager-sdk

IBM Cloud Secrets Manager Python SDK

`pip install ibm-secrets-manager-sdk` · installs (wheel) · licence: Apache Software License · rank 8315 · last release 2026-03-17 · [PyPI](https://pypi.org/project/ibm-secrets-manager-sdk/) · [docs](https://cloud.ibm.com/apidocs/secrets-manager) · [source](https://github.com/IBM/secrets-manager-python-sdk)

<details><summary>README extract</summary>

A Python client library to interact with the IBM Cloud® Secrets Manager APIs.

<details>
<summary>Table of Contents</summary>

* Overview
* Prerequisites
* Installation
* Authentication
* Using the SDK
* Questions
* Issues
* Contributing
* License

</details>

Features:
The IBM Cloud Secrets Manager Python SDK allows developers to programmatically interact with the following IBM Cloud services:

| Service name | Imported class name |

| Secrets Manager | SecretsManagerV2 |

Example:
```python
from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator
from ibm_secrets_manager_sdk.secrets_manager_v2 import *

secretsManager = SecretsManagerV2(
    authenticator=IAMAuthenticator(apikey='<IBM_CLOUD_API_KEY>')
)

secretsManager.set_service_url('<SERVICE_URL>')

...

</details>

### INITools

Tools for parsing and using INI-style files

`pip install INITools` · installs from source (sdist only) · licence: MIT License · rank 8325 · last release 2010-03-31 · [PyPI](https://pypi.org/project/INITools/)

<details><summary>README extract</summary>

A set of tools for parsing and using ``.ini``-style files, including
an abstract parser and several tools built on that parser.

Repository available at `
< or `download a tarball
of the development version
using ``easy_install INITools==dev``

</details>

### sendblue

The official Python library for the sendblue-api API

`pip install sendblue` · installs (wheel) · licence: Apache Software License · rank 8332 · last release 2026-10-30 · [PyPI](https://pypi.org/project/sendblue/) · [source](https://github.com/sendblue-api/sendblue-py)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Sendblue API Python library provides convenient access to the Sendblue API REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from sendblue_api import SendblueAPI

client = SendblueAPI(
    api_key=os.environ.get("SENDBLUE_API_API_KEY"),  # This is the default and can be omitted
    api_secret=os.environ.get("SENDBLUE_API_API_SECRET"),  # This is the default and can be omitted
)

message_response = client.messages.send(
    number="REPLACE_ME",
...
```

...

</details>

### mo-imports

More Imports! - Delayed importing

`pip install mo-imports` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 8338 · last release 2026-11-07 · [PyPI](https://pypi.org/project/mo-imports/)

<details><summary>README extract</summary>

A few methods to make late importing cleaner

|Branch |Status |

|master | |
|dev | |

Splitting code into modules is nice, but it can result in cyclic dependencies.

foos.py

bars.py

> We are not concerned with the infinite recursion; this is only for demonstrating cyclic dependencies.

Example:
```python
from bars import bar

def foo():
    bar()
```

Sections: More Imports! - Delayed importing, Problem, More Imports!, Solution #1: Use `expect`/`export` pattern, Solution #2: Use `delay_import`, Other solutions, Bad Solution: Keep in single file, Bad Solution: Use end-of-file imports, Bad Solution: Inline import, Bad Solution: Use the `_late_import()` pattern, More on importing, Ordering imports

</details>

### pydantic-numpy

Pydantic Model integration of the NumPy array

`pip install pydantic-numpy` · installs (wheel) · licence: BSD-3-Clause · rank 8344 · last release 2026-10-18 · [PyPI](https://pypi.org/project/pydantic-numpy/)

<details><summary>README extract</summary>

Example:
```python
import numpy as np
from pydantic import BaseModel

import pydantic_numpy.typing as pnd
from pydantic_numpy import np_array_pydantic_annotated_typing
from pydantic_numpy.model import NumpyModel, MultiArrayNumpyFile

class MyBaseModelDerivedModel(BaseModel):
    any_array_dtype_and_dimension: pnd.NpNDArray

    # Must be numpy float32 as dtype
...
```

Sections: pydantic-numpy, Usage, Examples, JSON Serialization, Custom type, Custom serialization

</details>

### rst2ansi

A rst converter to ansi-decorated console output

`pip install rst2ansi` · installs (wheel) · licence: MIT License · rank 8346 · last release 2016-05-24 · [PyPI](https://pypi.org/project/rst2ansi/)

<details><summary>README extract</summary>

A python module dedicated to rendering RST (reStructuredText) documents
to ansi-escaped strings suitable for display in a terminal.

Example:
```python
from rst2ansi import rst2ansi

print(rst2ansi('I love reStructuredText!'))
```

Sections: rst2ansi, Requirements, PyPi package, Usage, As a CLI utility, As a python module

</details>

### smolmachines

Embed isolated microVM sandboxes directly in your Python code — local (embedded) or smolfleet cloud.

`pip install smolmachines` · installs (wheel) · licence: Apache Software License · rank 8352 · last release 2026-10-28 · [PyPI](https://pypi.org/project/smolmachines/) · [source](https://github.com/smol-machines/smol)

<details><summary>README extract</summary>

Use a published guest port with any TCP client, locally or in smol cloud:

Install `smolmachines[tunnel]` for cloud tunnels. Cloud authentication stays in
the transport, not in the endpoint URL. Leaving the context closes the listener
and its connections. ...

Example:
```python
async with machine.tunnel(22222) as endpoint:
    reader, writer = await asyncio.open_connection(endpoint.host, endpoint.port)
    # Exchange bytes with the guest service.
    writer.close()
    await writer.wait_closed()
```

...

</details>

### types-pika

PEP-484 stubs for Pika

`pip install types-pika` · installs (wheel) · licence: MIT License · rank 8354 · last release 2022-01-18 · [PyPI](https://pypi.org/project/types-pika/)

<details><summary>README extract</summary>

This package contains type stubs to provide more precise static types and type inference for pika, the RabbitMQ client library.

</details>

### python-ipmi

Pure python IPMI library

`pip install python-ipmi` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 8367 · last release 2026-10-08 · [PyPI](https://pypi.org/project/python-ipmi/)

_README extract left out: share-alike licence._

### tailer

Python tail is a simple implementation of GNU tail and head.

`pip install tailer` · installs from source (sdist only) · licence: MIT License · rank 8374 · last release 2015-12-09 · [PyPI](https://pypi.org/project/tailer/)

<details><summary>README extract</summary>

Python tail is a simple implementation of GNU tail and head.

It provides 3 main functions that can be performed on any file-like object that supports `seek()` and `tell()`.

* `tail` - read lines from the end of a file
* `head` - read lines from the top of a file
* `follow` - read lines as a file grows ...

Example:
```python
import tailer
f = open('test.txt', 'w')
for i in range(11):
    f.write('Line %d\\n' % (i + 1))
f.close()
```

Sections: Tailer, Examples, Tail, Head, Follow, Running Tests

</details>

### pyobjc-framework-CoreMedia

Wrappers for the framework CoreMedia on macOS

`pip install pyobjc-framework-CoreMedia` · installs from source (sdist only) · licence: MIT · rank 8381 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreMedia/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreMedia" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### Sift

Python bindings for Sift Science's API

`pip install Sift` · installs (wheel) · licence: MIT License · rank 8383 · last release 2026-09-30 · [PyPI](https://pypi.org/project/Sift/) · [source](https://github.com/SiftScience/sift-python)

<details><summary>README extract</summary>

Bindings for Sift's APIs -- including the
Events
except sift.client.ApiException:
 # request failed
 pass
else:
 if response.is_ok():
 score_response = response.body["score_response"]
 print(score_response)

try:
 response = client.track("$transaction", properties, include_warnings=True)
 # ... ...

Sections: Sift Python Bindings, `track()` method, set it by the `include_warnings` param, Request a score for the user with user_id 23056, Remove a label from a user with user_id 23056, Get the latest decisions for a user, Get the latest decisions for an order, Get the latest decisions for a session, Get the latest decisions for a piece of content

</details>

### expects

Expressive and extensible TDD/BDD assertion library for Python

`pip install expects` · installs from source (sdist only) · licence: Apache Software License · rank 8384 · last release 2018-10-25 · [PyPI](https://pypi.org/project/expects/)

<details><summary>README extract</summary>

Expects is an *expressive* and *extensible* TDD/BDD assertion library for Python. Expects can be *extended* by defining new matchers.

Example:
```python
from expects import *

expect([]).to(be_empty)

expect(False).not_to(be_true)

expect({
    'name': 'Jack',
    'email': 'jack@example.com'
}).to(have_key('name', match('\w+')))

expect(str).to(have_property('split') & be_callable)

expect(lambda: foo).to(raise_error(NameError))

expect('Foo').to(equal('Bar') | equal('Foo'))
```

Sections: Expects, Usage, Specs, Changes, 3rd Party Matchers

</details>

### pypi-simple

PyPI Simple Repository API client library

`pip install pypi-simple` · installs (wheel) · licence: MIT · rank 8403 · last release 2025-09-03 · [PyPI](https://pypi.org/project/pypi-simple/) · [source](https://github.com/jwodder/pypi-simple)

<details><summary>README extract</summary>

GitHub
| PyPI
| Documentation
| Issues
| Changelog

`pypi-simple` is a client library for the Python Simple Repository API as
specified in 503 and updated by 592, 629, 658,
691, 700, 708, 714, 740, and 792. ...

Example:
```python
from pypi_simple import PyPISimple, tqdm_progress_factory

with PyPISimple() as client:
    page = client.get_project_page("pypi-simple")
    pkg = page.packages[-1]
    client.download_package(
        pkg, path=pkg.filename, progress=tqdm_progress_factory(),
    )
```

</details>

### easypost

EasyPost Shipping API Client Library for Python

`pip install easypost` · installs (wheel) · licence: MIT License · rank 8407 · last release 2026-10-27 · [PyPI](https://pypi.org/project/easypost/) · [docs](https://docs.easypost.com) · [source](https://github.com/EasyPost/easypost-python)

<details><summary>README extract</summary>

EasyPost, the simple shipping solution. You can sign up for an account at <

Example:
```python
import os
import easypost

client = easypost.EasyPostClient(os.getenv('EASYPOST_API_KEY'))

shipment = client.shipment.create(
    from_address = {
        "name": "EasyPost",
        "street1": "118 2nd Street",
        "street2": "4th Floor",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94105",
        "country": "US",
...
```

Sections: EasyPost Python Client Library, Usage, HTTP Hooks, Documentation, Unit Test API Keys, Google Cloud SDK

</details>

### PyPyDispatcher

Multi-producer-multi-consumer signal dispatching mechanism

`pip install PyPyDispatcher` · installs from source (sdist only) · licence: BSD License · rank 8408 · last release 2017-07-03 · [PyPI](https://pypi.org/project/PyPyDispatcher/)

<details><summary>README extract</summary>

Dispatcher mechanism for creating event models

PyDispatcher is an enhanced version of Patrick K. O'Brien's
original dispatcher.py module. It provides the Python
programmer with a robust mechanism for event routing within
various application contexts. ...

</details>

### fuzzyset2

A simple python fuzzyset implementation.

`pip install fuzzyset2` · installs from source (sdist only) · licence: BSD License · rank 8494 · last release 2024-10-21 · [PyPI](https://pypi.org/project/fuzzyset2/)

<details><summary>README extract</summary>

This is a maintained fork of the unfortunately no longer maintained fuzzyset package package by
 Mike Axiak. This fork is available on PyPi as fuzzyset2.

fuzzyset is a data structure that performs something akin to fulltext search
against data to determine likely misspellings and approximate string matching.

Example:
```python
>>> a = fuzzyset.FuzzySet()
>>> a.add("michael axiak")
>>> a.get("micael asiak")
[(0.8461538461538461, u'michael axiak')]
```

Sections: fuzzyset - A fuzzy string set for python., Note, Usage, Construction Arguments, Theory of operation, Adding to the data structure, Retrieving

</details>

### qasync

Python library for using asyncio in Qt-based applications

`pip install qasync` · installs (wheel) · licence: BSD-2-Clause · rank 8496 · last release 2025-08-28 · [PyPI](https://pypi.org/project/qasync/) · [source](https://github.com/CabbageDevelopment/qasync)

<details><summary>README extract</summary>

`qasync` allows coroutines to be used in PyQt/PySide applications by providing an implementation of the `PEP 3156` event loop.

With `qasync`, you can use `asyncio` functionalities directly inside Qt app's event loop, in the main thread. ...

Example:
```python
import asyncio
import sys

from PySide6.QtWidgets import QVBoxLayout, QWidget

from qasync import QApplication, QEventLoop

class MainWindow(QWidget):
    def init(self):
        super().init()

        self.setLayout(QVBoxLayout())
        self.lbl_status = QLabel("Idle", self)
        self.layout().addWidget(self.lbl_status)

    @asyncClose
...
```

Sections: qasync, Introduction, Basic Example, The Future of `qasync`, Requirements

</details>

### mixer

Mixer -- Is a fixtures replacement. Supported Django ORM, SqlAlchemy ORM, Mongoengine ODM and custom python objects.

`pip install mixer` · installs (wheel) · licence: BSD License · rank 8499 · last release 2022-03-23 · [PyPI](https://pypi.org/project/mixer/) · [docs](https://mixer.readthedocs.org) · [source](https://github.com/klen/mixer)

<details><summary>README extract</summary>

The Mixer is a helper to generate instances of Django or SQLAlchemy models.
It's useful for testing and fixture replacement. Fast and convenient test-data
generation.

Mixer supports:

* Django;
* SQLAlchemy;
* Flask-SQLAlchemy;
* Peewee;
* Pony;
* Mongoengine;
* Marshmallow;
* Custom schemes; ...

Example:
```python
from mixer.main import mixer

class Test:
    one = int
    two = int
    name = str

class Scheme:
    name = str
    money = int
    male = bool
    prop = Test

scheme = mixer.blend(Scheme, prop__one=1)
```

Sections: Requirements, Usage, Django workflow, Flask, Flask-SQLAlchemy, SQLAlchemy workflow, Mongoengine workflow, Marshmallow workflow, Common usage, DB commits, Custom fields, Middlewares, Locales, Bug tracker

</details>

### flake8-debugger

ipdb/pdb statement checker plugin for flake8

`pip install flake8-debugger` · installs (wheel) · licence: MIT License · rank 8501 · last release 2022-04-30 · [PyPI](https://pypi.org/project/flake8-debugger/) · [source](https://github.com/jbkahn/flake8-debugger)

<details><summary>README extract</summary>

Check for pdb;idbp imports and set traces, as well as `from IPython.terminal.embed import InteractiveShellEmbed` and `InteractiveShellEmbed()()`.

This module provides a plugin for ``flake8``, the Python code checker.

Installation

You can install or upgrade ``flake8-debugger`` with these commands:: ...

Sections: Flake8 debugger plugin, 4.1.2 - 2022-04-30, 4.1.1 - 2022-04-30, 4.1.0 - 2022-04-30, 4.0.0 - 2020-11-29, 3.2.1 - 2019-10-31, 3.2.0 - 2019-10-15, 3.1.1 - 2019-10-12, 3.1.0 - 2018-02-11, 3.0.0 - 2017-05-11, 2.0.0 - 2016-09-19, 1.4.0 - 2015-05-18, 1.3.2 - 2014-11-04, 1.3.1 - 2014-11-04

</details>

### pyobjc-framework-FSEvents

Wrappers for the framework FSEvents on macOS

`pip install pyobjc-framework-FSEvents` · installs from source (sdist only) · licence: MIT · rank 8506 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-FSEvents/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "FSEvents" API in macOS. The functions in this framework
allow you to reliably observe changes to the filesystem, even when your
program is not running al the time. ...

</details>

### openunmix

PyTorch-based music source separation toolkit

`pip install openunmix` · installs (wheel) · licence: MIT License · rank 8532 · last release 2024-04-16 · [PyPI](https://pypi.org/project/openunmix/)

<details><summary>README extract</summary>

This repository contains the PyTorch (1.8+) implementation of Open-Unmix, a deep neural network reference implementation for music source separation, applicable for researchers, audio engineers and artists. ...

Example:
```python
separator = torch.hub.load('sigsep/open-unmix-pytorch', 'umxl, device=device)
```

Sections: _Open-Unmix for PyTorch, ⭐️ News, 🧠 The Model (for one source), Input Stage, Dimensionality reduction, Bidirectional-LSTM, Output Stage, 🤹‍♀️ Putting source models together: the `Separator`, 🏁 Getting started, Using Docker, Pre-trained models, Using pre-trained models from within python, torch.hub, Performing separation

</details>

### peewee-migrate

Support for migrations in Peewee ORM

`pip install peewee-migrate` · installs (wheel) · licence: MIT · rank 8535 · last release 2026-08-24 · [PyPI](https://pypi.org/project/peewee-migrate/) · [source](https://github.com/klen/peewee_migrate)

<details><summary>README extract</summary>

Peewee Migrate -- A simple migration engine for Peewee ORM

- peewee >= 4.4

- For `Peewee<3.0` please use `Peewee-Migrate==0.14.0`
- For `Python 3.0-3.6` please use `Peewee-Migrate==1.1.6`
- For `Python 3.7` please use `Peewee-Migrate==1.6.6`
- For `Python 3.8, 3.9` please use `Peewee-Migrate>=1.13.0` ...

Example:
```python
from peewee_migrate import Router
from peewee import SqliteDatabase

router = Router(SqliteDatabase('test.db'))

# Create migration
router.create('migration_name')

# Run migration/migrations
router.run('migration_name')

# Run all unapplied migrations
router.run()
```

Sections: Peewee Migrate, Requirements, Dependency Note, Usage, From shell, From python, Migration files, Bug tracker

</details>

### django-webtest

Instant integration of Ian Bicking's WebTest (http://docs.pylonsproject.org/projects/webtest/) with Django's testing framework.

`pip install django-webtest` · installs (wheel) · licence: MIT License · rank 8538 · last release 2026-10-10 · [PyPI](https://pypi.org/project/django-webtest/) · [source](https://github.com/django-webtest/django-webtest)

<details><summary>README extract</summary>

django-webtest is an app for instant integration of Ian Bicking's
WebTest ( with Django's
testing framework.

Features:
While django.test.client.Client is fine for its purposes, it is not
well-suited for functional or integration testing. From Django's test client
docstring: ...

Example:
```python
from django_webtest import WebTest

class MyTestCase(WebTest):

    # optional: we want some initial data to be able to login
    fixtures = ['users', 'blog_posts']

    # optional: default extra_environ for this TestCase
    extra_environ = {'HTTP_ACCEPT_LANGUAGE': 'ru'}

    def testBlog(self):
...
```

...

</details>

### dbt-artifacts-parser

A dbt artifacts parser in python

`pip install dbt-artifacts-parser` · installs (wheel) · licence: Apache Software License · rank 8552 · last release 2026-08-10 · [PyPI](https://pypi.org/project/dbt-artifacts-parser/)

<details><summary>README extract</summary>

This is a dbt artifacts parser in python.
It enables us to deal with `catalog.json`, `manifest.json`, `run-results.json` and `sources.json` as python objects.

This package is primarily designed for dbt-core, enabling seamless interaction with dbt artifacts as Python objects. ...

Example:
```python
import json

# parse any version of catalog.json
from dbt_artifacts_parser.parser import parse_catalog

with open("path/to/catalog.json", "r") as fp:
    catalog_dict = json.load(fp)
    catalog_obj = parse_catalog(catalog=catalog_dict)

# parse catalog.json v1
from dbt_artifacts_parser.parser import parse_catalog_v1

...
```

...

</details>

### hier-config

A network configuration query and comparison library, used to build remediation configurations.

`pip install hier-config` · installs (wheel) · licence: MIT License · rank 8590 · last release 2026-09-20 · [PyPI](https://pypi.org/project/hier-config/)

### scale-gp-beta

The official Python library for the Scale GP API

`pip install scale-gp-beta` · installs (wheel) · licence: Apache Software License · rank 8600 · last release 2026-09-29 · [PyPI](https://pypi.org/project/scale-gp-beta/) · [source](https://github.com/scaleapi/sgp-python-beta)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Scale GP Python library provides convenient access to the Scale GP REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from scale_gp_beta import SGPClient

client = SGPClient(
    account_id="My Account ID",
    api_key=os.environ.get("SGP_API_KEY"),  # This is the default and can be omitted
    # or 'production' | 'staging' | 'development' | 'local'; defaults to "production".
    environment="production-multitenant",
)

...
```

...

</details>

### cfnresponse

Send a response object to a custom resource by way of an Amazon S3 presigned URL

`pip install cfnresponse` · installs (wheel) · licence: Apache Software License · rank 8609 · last release 2024-08-03 · [PyPI](https://pypi.org/project/cfnresponse/) · [source](https://github.com/gene1wood/cfnresponse)

<details><summary>README extract</summary>

This package contains the Amazon Web Services (AWS) cfnresponse module which is
available in Python AWS Lambda environments.

The code for this module can be found in the AWS documentation
and in the awslabs GitHub repo

You can compare the code in `awslabs` with this pypi package with this command ...

</details>

### progressbar33

Text progress bar library for Python.

`pip install progressbar33` · installs from source (sdist only) · licence: BSD License; GNU Library or Lesser General Public License (LGPL) · rank 8614 · last release 2014-08-29 · [PyPI](https://pypi.org/project/progressbar33/)

_README extract left out: share-alike licence._

### sarge

A wrapper for subprocess which provides command pipeline functionality.

`pip install sarge` · installs (wheel) · licence: BSD-3-Clause · rank 8619 · last release 2026-01-20 · [PyPI](https://pypi.org/project/sarge/) · [docs](https://sarge.readthedocs.io/) · [source](https://github.com/vsajip/sarge)

<details><summary>README extract</summary>

The sarge package provides a wrapper for subprocess which provides
command pipeline functionality.

This package leverages subprocess to provide easy-to-use cross-platform command
pipelines with a POSIX flavour: you can have chains of commands using ``;``, ``&``,
pipes using ``|`` and ``|&``, and redirection.

</details>

### pydifact

Pydifact is a library that aims to provide complete support for reading and writing EDIFACT files. These file format, despite being old, is still a standard in many business cases. In Austria e.g., it is used for the transfer of medical reports between medical doctors.

`pip install pydifact` · installs (wheel) · licence: MIT · rank 8621 · last release 2026-04-10 · [PyPI](https://pypi.org/project/pydifact/) · [docs](https://pydifact.readthedocs.io) · [source](https://github.com/nerdocs/pydifact)

<details><summary>README extract</summary>

A Python library to parse and serialize UN/EDIFACT interchanges.

This is a port of metroplex-systems/edifact to Python. Thanks here at the start to Craig Duncan for this cool piece of software. Porting was like a breeze due to the high code quality there. ...

Features:
Because I did not find a decent UN/EDIFACT library for Python, so I decided to port one of the available good PHP libraries to Python. Here is the result.

ATM this is a Work In Progress, the API is not stable yet.
Feel free to help.

Example:
```python
from pydifact.segmentcollection import Interchange

interchange = Interchange.from_file("./tests/data/wikipedia.edi")
interchange = Interchange.from_str(
    "UNA:+,? '"
    "UNB+UNOC:1+1234+3333+200102:2212+42'"
    "UNH+42z42+PAORES:93:1:IA'"
    "MSG+1:45'"
...

</details>

### py-yaml12

A modern YAML 1.2 parser and emitter for Python, written in Rust.

`pip install py-yaml12` · installs (wheel) · licence: MIT License · rank 8638 · last release 2026-08-25 · [PyPI](https://pypi.org/project/py-yaml12/) · [docs](https://posit-dev.github.io/py-yaml12/) · [source](https://github.com/posit-dev/py-yaml12)

<details><summary>README extract</summary>

A YAML 1.2 parser/formatter for Python, implemented in Rust for speed
and correctness. Built on the excellent
`saphyr` crate.

Compared with YAML 1.1's type library, YAML 1.2's recommended core
schema uses more conservative type inference for unquoted values. The
YAML 1.1 versus 1.2 quick
reference
summarizes the differences. ...

Example:
```python
from yaml12 import parse_yaml, format_yaml, Yaml

yaml_text = """
title: A modern YAML parser and emitter written in Rust
properties: [fast, correct, safe, simple]
features:
  tags: preserve
  streams: multi
"""

doc = parse_yaml(yaml_text)

assert doc == {
    "title": "A modern YAML parser and emitter written in Rust",
...
```

...

</details>

### scholarly

Simple access to Google Scholar authors and citations

`pip install scholarly` · installs (wheel) · licence: Unlicense · rank 8649 · last release 2023-01-16 · [PyPI](https://pypi.org/project/scholarly/)

<details><summary>README extract</summary>

scholarly is a module that allows you to retrieve author and publication information from Google Scholar in a friendly, Pythonic way without having to solve CAPTCHAs.

Example:
```python
from scholarly import scholarly

# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results
search_query = scholarly.search_author('Steven A Cholewiak')
# Retrieve the first result from the iterator
first_author_result = next(search_query)
scholarly.pprint(first_author_result)

...
```

Sections: scholarly, Optional dependencies, Tests, Documentation, Examples, Disclaimer

</details>

### unrar-cffi

Read RAR file from python -- cffi edition

`pip install unrar-cffi` · installs from source (sdist only) · licence: Apache Software License · rank 8650 · last release 2021-09-26 · [PyPI](https://pypi.org/project/unrar-cffi/)

<details><summary>README extract</summary>

unrar-cffi is a python extension that exposes unrar library
functionality through a `zipfile`-like interface.

Features:
The package implements the following `RarFile` functions:

 * `namelist()`
 * `infolist()`
 * `getinfo()`
 * `read()`
 * `open()`
 * `testrar()`
 * `rarfile.is_rar_file()`

Example:
```python
from unrar.cffi import rarfile

rar = rarfile.RarFile('sample.rar')

assert rar.testrar() == None

for filename in rar.namelist():
    info = rar.getinfo(filename)
    print("Reading {}, {}, {} bytes ({} bytes compressed)".format(info.filename, info.date_time, info.file_size, info.compress_size))
    data = rar.read(filename)
...
```

Sections: unrar-cffi -- Work with RAR files., Description, Features, Usage, Build, Requirements, Compile and test

</details>

### pyobjc-framework-AVFoundation

Wrappers for the framework AVFoundation on macOS

`pip install pyobjc-framework-AVFoundation` · installs from source (sdist only) · licence: MIT · rank 8652 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-AVFoundation/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "AVFoundation" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### onemkl-license

Intel® oneAPI Math Kernel Library

`pip install onemkl-license` · does not install on CPython 3.14 · licence: Other/Proprietary License · rank 8657 · last release 2026-10-16 · [PyPI](https://pypi.org/project/onemkl-license/)

<details><summary>README extract</summary>

Intel® oneAPI Math Kernel Library (Intel® oneMKL) is a computing math library of highly optimized, extensively threaded routines for applications that require maximum performance. This package provides C and Data Parallel C++ (DPC++) programming language interfaces. ...

</details>

### pydantic-deep

Batteries-included agent harness for Python — tool-calling, sandboxed execution, multi-agent teams, and unlimited context on Pydantic AI

`pip install pydantic-deep` · installs (wheel) · licence: MIT · rank 8662 · last release 2026-10-06 · [PyPI](https://pypi.org/project/pydantic-deep/) · [docs](https://vstorm-co.github.io/pydantic-deepagents/) · [source](https://github.com/vstorm-co/pydantic-deepagents)

<details><summary>README extract</summary>

From the team behind this repo: AgenticOS, the Sovereign Agentic AI Layer. AI agents your whole team can use and improve: open source (Apache-2.0), self-hosted, built on Pydantic AI.

 Open-source Claude Code — that you can also build on.

 A self-hosted terminal AI assistant and the Python framework behind it. ...

Example:
```python
from pydantic_deep import create_deep_agent

agent = create_deep_agent(model="anthropic:claude-sonnet-4-6")
result = await agent.run("Build a REST API for auth")
```

...

</details>

### config-formatter

An automatic formatter for .ini and .cfg configuration files

`pip install config-formatter` · installs (wheel) · licence: MIT License · rank 8677 · last release 2023-11-18 · [PyPI](https://pypi.org/project/config-formatter/)

<details><summary>README extract</summary>

An automatic formatter for .ini and .cfg configuration files.

Example:
```python
from config_formatter import ConfigFormatter

with open("config.ini", "r") as file:
    formatter = ConfigFormatter()
    formatted = formatter.prettify(file.read())
    print(formatted)
```

Sections: config-formatter, Usage, Example

</details>

### sail

Python SDK for the Sail sandbox platform

`pip install sail` · installs (wheel) · licence: Apache-2.0 · rank 8685 · last release 2026-10-29 · [PyPI](https://pypi.org/project/sail/) · [docs](https://docs.sailresearch.com) · [source](https://github.com/sailresearchco/sail)

<details><summary>README extract</summary>

Python client library for Sail, the most cost-efficient infrastructure provider
for long-horizon agents.

- Sail documentation: quickstarts, guides, and examples.
- Sailbox Python guide and
 Python API reference.
- Other languages: TypeScript,
 Rust.

Sections: Sail SDK, Documentation, What's inside

</details>

### Pypubsub

Python Publish-Subscribe Package

`pip install Pypubsub` · installs (wheel) · licence: BSD-2-Clause · rank 8699 · last release 2025-12-08 · [PyPI](https://pypi.org/project/Pypubsub/) · [docs](http://pypubsub.readthedocs.io) · [source](https://github.com/schollii/pypubsub)

<details><summary>README extract</summary>

- December 2025: pypubsub 4.0.7 released! (update to latest packaging system, testing, docs).
- ... (has it really been this long since I cleaned this up?!)...
- January 2019: pypubsub 4.0.3 released! (for those -- and only those -- who use Python >= 3).
- March 2019: pypubsub 3.4.2 released (for those -- and only those -- who use Python 2.7.x).

Features:
Provides a publish-subscribe API to facilitate event-based or message-based
architecture in a single-process application. It is pure Python and works on
Python 3.7+ (tested through 3.14). ...

Sections: News, Overview, Versioning and tags, wxPython on Ubuntu 22+, Docs

</details>

### sap-ai-sdk-core

SAP Cloud SDK for AI (Python): Core SDK

`pip install sap-ai-sdk-core` · installs (wheel) · licence: Apache-2.0 · rank 8708 · last release 2026-10-02 · [PyPI](https://pypi.org/project/sap-ai-sdk-core/)

<details><summary>README extract</summary>

The SDK formerly known as *AI Core SDK* was rebranded.

The class names have not changed i.e., you can continue to use existing code.

The SAP AI Core SDK can be used to interact with SAP AI Core.
It provides access to all public lifecycle and administration APIs.

For example: ...

Example:
```python
from ai_core_sdk.ai_core_v2_client import AICoreV2Client
```

Sections: SAP Cloud SDK for AI (Python): Core SDK, Example Usage, Import Definitions, Create Client, Create New Resource Group, Create Object Store Secret, List Scenarios, Client Configuration, Tracking, Modify Metrics

</details>

### blkinfo

blkinfo is a python package to list information about all available or the specified block devices.

`pip install blkinfo` · installs from source (sdist only) · licence: GPLv3 · rank 8709 · last release 2021-10-06 · [PyPI](https://pypi.org/project/blkinfo/)

_README extract left out: share-alike licence._

### flake8-noqa

Flake8 noqa comment validation

`pip install flake8-noqa` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 8720 · last release 2026-02-07 · [PyPI](https://pypi.org/project/flake8-noqa/)

_README extract left out: share-alike licence._

### picobox

Dependency injection framework designed with Python in mind.

`pip install picobox` · installs (wheel) · licence: MIT License · rank 8723 · last release 2023-11-20 · [PyPI](https://pypi.org/project/picobox/) · [docs](https://picobox.readthedocs.io) · [source](https://github.com/ikalnytskyi/picobox)

<details><summary>README extract</summary>

Picobox is opinionated dependency injection framework designed to be clean,
pragmatic and with Python in mind. No complex graphs, no implicit injections,
no type bindings – just picoboxes, and explicit demands!

Features:
Because we usually want to decouple our code and Python lack of clean and
pragmatic solutions (even third parties).

Example:
```python
import picobox
import requests

@picobox.pass("conf")
@picobox.pass("requests", as="session")
def get_resource(uri, session, conf):
    return session.get(conf["base_uri"] + uri)

box = picobox.Box()
box.put("conf", {"base_uri": "
box.put("requests", factory=requests.Session, scope=picobox.threadlocal)

with picobox.push(box):
...
```

Sections: Picobox, Why?, Features, Quickstart, Links

</details>

### sap-ai-sdk-base

SAP Cloud SDK for AI (Python): Base Client

`pip install sap-ai-sdk-base` · installs (wheel) · licence: Other/Proprietary License · rank 8769 · last release 2026-03-30 · [PyPI](https://pypi.org/project/sap-ai-sdk-base/)

<details><summary>README extract</summary>

The SDK formerly known as *AI API Client SDK* was rebranded.

The class names have not changed i.e., you can continue to use existing code.

The Base Client for AI API is a Python-based SDK that enables you to access the AI API using Python methods and data
structures.

The Base SDK can be used with any implementation of AI API. ...

Example:
```python
from ai_api_client_sdk.ai_api_v2_client import AIAPIV2Client

# Instantiate the client
client = AIAPIV2Client(base_url=AI_API_URL,
    auth_url=AUTH_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET, resource_group=RESOURCE_GROUP)

# Make some queries, e.g.
scenarios = client.scenario.query()

for scenario in scenarios.resources:
...
```

Sections: SAP Cloud SDK for AI (Python): Base Client for AI API, Example Usage

</details>

### django-viewflow

Reusable library to build business applications fast

`pip install django-viewflow` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 8774 · last release 2026-07-30 · [PyPI](https://pypi.org/project/django-viewflow/)

_README extract left out: share-alike licence._

### sap-ai-sdk-gen

SAP Cloud SDK for AI (Python): generative AI SDK

`pip install sap-ai-sdk-gen` · installs (wheel) · licence: Apache-2.0 · rank 8786 · last release 2026-09-23 · [PyPI](https://pypi.org/project/sap-ai-sdk-gen/)

<details><summary>README extract</summary>

With this SDK you can leverage the power of generative models available in the generative AI Hub of SAP AI Core.
The SDK provides model access by wrapping the native SDKs of the model providers (OpenAI, Amazon, Google), through langchain, or through the orchestration service.

Sections: SAP Cloud SDK for AI (Python) - generative, Configuration, Usage

</details>

### linode-api4

The official Python SDK for Linode API v4

`pip install linode-api4` · installs (wheel) · licence: BSD License · rank 8789 · last release 2026-10-27 · [PyPI](https://pypi.org/project/linode-api4/) · [docs](https://linode-api4.readthedocs.io/) · [source](https://github.com/linode/linode_api4-python.git)

<details><summary>README extract</summary>

The official python library for the Linode API v4 in python.

Example:
```python
from linode_api4 import LinodeClient, Instance

# Create a Linode API client
client = LinodeClient("MY_PERSONAL_ACCESS_TOKEN")

# Create a new Linode
new_linode, root_pass = client.linode.instance_create(
    ltype="g6-nanode-1",
    region="us-southeast",
    image="linode/ubuntu22.04",
    label="my-ubuntu-linode"
)

...
```

Sections: linode_api4, Building from Source, Usage, Quick Start, Examples, Tests, Integration Tests, Pre-requisite, Running the tests, Documentation

</details>

### pyobjc-framework-CoreServices

Wrappers for the framework CoreServices on macOS

`pip install pyobjc-framework-CoreServices` · installs from source (sdist only) · licence: MIT · rank 8792 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreServices/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreServices" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### json-diff

Generates diff between two JSON files

`pip install json-diff` · installs from source (sdist only) · licence: MIT License · rank 8812 · last release 2019-08-25 · [PyPI](https://pypi.org/project/json-diff/)

<details><summary>README extract</summary>

Compares two JSON files ( and generates a new JSON file
with the result. Allows exclusion of some keys from the comparison, or
in other way to include only some keys.

The project’s website is at
Patches and pull requests are welcome, but please keep the script compatible
with python 2.4.

Released under MIT/X11 license.

</details>

### reka-api

Reka Python SDK

`pip install reka-api` · installs (wheel) · licence: MIT License · rank 8823 · last release 2024-09-30 · [PyPI](https://pypi.org/project/reka-api/)

<details><summary>README extract</summary>

The Reka Python Library provides convenient access to the Reka API from
applications written in Python.

The library includes type definitions for all
request and response fields, and offers both synchronous and asynchronous clients powered by httpx.

Example:
```python
from reka import ChatMessage
from reka.client import Reka

client = Reka(
    api_key="YOUR_API_KEY",
) # or just client = Reka() if set via env

client.chat.create(
    messages=[
        ChatMessage(
            content="What is the fifth prime number?",
            role="user",
        )
    ],
    model="reka-core-20240501",
)
```

Sections: Reka Python Library, Usage, Typing, V2 SDK, Async Client, Streaming, Exception Handling, Advanced, Timeouts, Retries, Custom HTTP client

</details>

### ascii-colors

A Python library for rich terminal output with advanced logging features.

`pip install ascii-colors` · installs (wheel) · licence: Apache-2.0 · rank 8848 · last release 2026-10-23 · [PyPI](https://pypi.org/project/ascii-colors/) · [docs](https://parisneo.github.io/ascii_colors/) · [source](https://github.com/ParisNeo/ascii_colors)

<details><summary>README extract</summary>

> One library. Colors. Logging. Progress. Menus. Prompts. Panels. Tables. Done.

Stop wrestling with multiple CLI libraries. ASCIIColors unifies everything you need for modern terminal applications into a single, elegant toolkit — from quick colored output to production-grade logging, interactive menus, smart prompts, and rich UI components. ...

Features:
| Concern | How it's handled |

| Logger created *before* `basicConfig`? | Falls back to a default console handler; picks up the configured handlers on the next emit. No crash. ...

Example:
```python
from ascii_colors import ASCIIColors

# Simple color methods — print immediately to terminal
ASCIIColors.red("Error: Connection failed")
ASCIIColors.green("✓ Success!")
...

</details>

### iniparse

Accessing and Modifying INI files

`pip install iniparse` · installs (wheel) · licence: MIT License; Python Software Foundation License · rank 8854 · last release 2026-11-03 · [PyPI](https://pypi.org/project/iniparse/)

<details><summary>README extract</summary>

iniparse is an INI parser for Python which is API compatible
with the standard library's ConfigParser, preserves structure of INI
files (order of sections & options, indentation, comments, and blank
lines are preserved when data is updated), and is more convenient to
use.

</details>

### python-lokalise-api

Official Python interface for the Lokalise API v2

`pip install python-lokalise-api` · installs (wheel) · licence: BSD-3-Clause · rank 8902 · last release 2026-10-26 · [PyPI](https://pypi.org/project/python-lokalise-api/) · [docs](https://python-lokalise-api.readthedocs.io/) · [source](https://github.com/lokalise/python-lokalise-api)

<details><summary>README extract</summary>

Official Python 3 interface for the Lokalise APIv2 that represents returned data as Python objects.

Example:
```python
import lokalise

client = lokalise.Client('YOUR_API_TOKEN')

project = client.project('123.abc')
print(project.name)

client.upload_file(project.project_id, {
    "data": 'ZnI6DQogIHRlc3Q6IHRyYW5zbGF0aW9u',
    "filename": 'python_upload.yml',
    "lang_iso": 'en'
})

translation_keys = client.keys(project.project_id, {"page": 2,
    "limit": 3,
...
```

Sections: Lokalise API v2 official Python interface, Quick start, Documentation

</details>

### reducto

Alias package — installs the official reductoai SDK. Prefer `pip install reductoai`.

`pip install reducto` · installs (wheel) · licence: Apache Software License · rank 8908 · last release 2026-11-04 · [PyPI](https://pypi.org/project/reducto/) · [source](https://github.com/reductoai/reducto-python-sdk)

<details><summary>README extract</summary>

This directory builds the `reducto` package on PyPI, which is an alias for `reductoai` — the official Reducto Python SDK.

`pip install reducto` installs `reductoai` as a dependency. The import name is `reducto` either way:

Example:
```python
import reducto
```

Sections: reducto (PyPI alias), How this builds

</details>

### sphinx_external_toc

A sphinx extension that allows the site-map to be defined in a single YAML file.

`pip install sphinx_external_toc` · installs (wheel) · licence: MIT License · rank 8921 · last release 2026-01-16 · [PyPI](https://pypi.org/project/sphinx_external_toc/) · [docs](https://sphinx-external-toc.readthedocs.io)

<details><summary>README extract</summary>

Example:
```python
import yaml
from sphinx_external_toc.parsing import parse_toc_yaml
path = "path/to/_toc.yml"
site_map = parse_toc_yaml(path)
yaml.dump(site_map.as_json())
```

Sections: User Guide, Sphinx Configuration, Jupyterbook configuration, Basic Structure, File and URL titles, Using different key-mappings, Command-line, API

</details>

### whop-sdk

(no summary)

`pip install whop-sdk` · installs (wheel) · licence: Apache-2.0 · rank 8941 · last release 2026-10-28 · [PyPI](https://pypi.org/project/whop-sdk/) · [source](https://github.com/whopio/whopsdk-python)

<details><summary>README extract</summary>

The Whop SDK gives you typed access to the Whop API. Pass your API key to the client explicitly — the SDK reads no environment variables, so a client built without a key sends unauthenticated requests and the API answers 401.

Example:
```python
from whop_sdk import Whop

client = Whop(
    token="<token>",
)

client.access_tokens.create()
```

Sections: Whop Python Library, Documentation, Reference, Usage, Migrating from 0.0.41 and earlier, There is no environment-variable fallback, A first request, Environments, Async Client, Using aiohttp, Exception Handling, Pagination, Verifying user tokens, Advanced

</details>

### persist-queue

A thread-safe disk based persistent queue in Python.

`pip install persist-queue` · installs (wheel) · licence: BSD License · rank 8942 · last release 2025-10-25 · [PyPI](https://pypi.org/project/persist-queue/)

<details><summary>README extract</summary>

Features:
`persist-queue` implements file-based and SQLite3-based persistent queues for Python.
It provides thread-safe, disk-based queue implementations that survive process crashes
and restarts. ...

Example:
```python
from persistqueue import Queue

# Create a queue
q = Queue("my_queue_path")

# Add items
q.put("item1")
q.put("item2")

# Get items
item = q.get()
print(item)  # "item1"

# Mark as done
q.task_done()
```

Sections: persist-queue - A thread-safe, disk-based queue for Python, Overview, Key Features, With Extra Features, From Source, Requirements, Quick Start, Basic File Queue, SQLite Queue, MySQL Queue, Async Queue (v1.1.0+), Examples, File-based Queue, SQLite3-based Queue

</details>

### aiocron

Crontabs for asyncio

`pip install aiocron` · installs (wheel) · licence: MIT License · rank 8952 · last release 2025-02-14 · [PyPI](https://pypi.org/project/aiocron/)

<details><summary>README extract</summary>

Example:
```python
>>> import aiocron
>>> import asyncio
>>>
>>> @aiocron.crontab('*/30 * * * *')
... async def attime():
...     print('run')
...
>>> asyncio.get_event_loop().run_forever()
```

Sections: aiocron - Crontabs for asyncio, Usage

</details>

### zenml

ZenML: MLOps for Reliable AI: from Classical AI to Agents.

`pip install zenml` · installs (wheel) · licence: Apache-2.0 · rank 8965 · last release 2026-11-03 · [PyPI](https://pypi.org/project/zenml/) · [docs](https://docs.zenml.io) · [source](https://github.com/zenml-io/zenml)

<details><summary>README extract</summary>

[][pypi-url]
 [][pypi-url]
 [][downloads-url]
 [][contributors-url]
 [][license-url]

 Projects •
 Roadmap •
 Changelog •
 Report Bug •
 Sign up for ZenML Pro •
 Blog •
 Docs

 🎉 For the latest release, see the changelog.

ZenML is built for ML or AI Engineers working on traditional ML use-cases, LLM workflows, or agents, in a company setting. ...

Sections: One AI Platform From Pipelines to Agents, 🚀 Get Started (5 minutes), 🏗️ Architecture Overview, 🎮 Demo, 🖼️ Resources, 🗣️ Chat With Your Pipelines: ZenML MCP Server, 🤖 Kitaru: Replay-Based Evals for AI Agents, 🎓 Books & Resources, 🤝 Join ML Engineers Building the Future of AI, ❓ FAQs from ML Engineers Like You, 🛠 VS Code / Cursor Extension

</details>

### classproperties

property for class methods

`pip install classproperties` · installs from source (sdist only) · licence: MIT License · rank 8992 · last release 2019-01-24 · [PyPI](https://pypi.org/project/classproperties/)

### graphlib

Graph API

`pip install graphlib` · installs from source (sdist only) · licence: BSD License · rank 9001 · last release 2014-06-12 · [PyPI](https://pypi.org/project/graphlib/)

### lazy-import

A module for lazy loading of Python modules

`pip install lazy-import` · installs from source (sdist only) · licence: GNU General Public License v3 or later (GPLv3+) · rank 9007 · last release 2018-01-22 · [PyPI](https://pypi.org/project/lazy-import/)

_README extract left out: share-alike licence._

### wechatpy

WeChat SDK for Python

`pip install wechatpy` · installs (wheel) · licence: MIT License · rank 9019 · last release 2021-11-11 · [PyPI](https://pypi.org/project/wechatpy/)

<details><summary>README extract</summary>

_ _ __ _ _ __ _ __ _ _
 |\ \ |\ \|\ _ \ |\ \|\ \|\ \|\ \|\_ _\\ __ \|\ \ / /|
 \ \ \ \ \ \ \ /|\ \ \_|\ \ \\\ \ \ \|\ \|___ \ \_\ \ \|\ \ \ \/ / /
 \ \ \ \ \ \ \ \_|/_\ \ \ \ \ \ \ \ \ \ \ \ \ __\ \ / /
 \ \ \|\\_\ \ \ \_|\ \ \ \\ \ \ \ \ \ \ \ \ \ \ \ \ \ \_|\/ / /
 \ \__\ \_\ \_\ \\ \\ \\ \\ \ \\ \ \\ / / /
 \|__|\|_|\|_|\||\||\||\|| \|| \|||\_/ ...

Sections: 功能特性, 安装, 使用示例, 贡献代码, 问题反馈

</details>

### libscrc

Library for calculating CRC3/CRC4/CRC8/CRC16/CRC24/CRC32/CRC64/CRC82

`pip install libscrc` · installs from source (sdist only) · licence: GNU General Public License v3 or later (GPLv3+) · rank 9022 · last release 2024-08-21 · [PyPI](https://pypi.org/project/libscrc/)

_README extract left out: share-alike licence._

### sarvamai

(no summary)

`pip install sarvamai` · installs (wheel) · licence: not stated · rank 9039 · last release 2026-11-07 · [PyPI](https://pypi.org/project/sarvamai/) · [source](https://github.com/sarvamai/sarvam-python-sdk)

<details><summary>README extract</summary>

The Sarvam Python library provides convenient access to the Sarvam API from Python.

API reference documentation is available here.

Example:
```python
from sarvamai import SarvamAI

client = SarvamAI(
    api_subscription_key="YOUR_API_SUBSCRIPTION_KEY",
)
client.text.translate(
    input="input",
    source_language_code="auto",
    target_language_code="bn-IN",
)
```

Sections: Sarvam Python Library, Documentation, Reference, Usage, Async Client, Exception Handling, Advanced, Retries, Timeouts, Custom Client, References, Text, 📝 Description, Newly added languages

</details>

### mailchimp3

A python client for v3 of MailChimp API

`pip install mailchimp3` · installs (wheel) · licence: MIT License · rank 9040 · last release 2023-06-13 · [PyPI](https://pypi.org/project/mailchimp3/)

<details><summary>README extract</summary>

|mailchimp3 v3.0.21 on PyPiMIT licenseStable|

A straightforward python client for v3 of MailChimp API using requests
>= 2.7.0.

Example:
```python
# returns all the lists (only name and id)
client.lists.all(get_all=True, fields="lists.name,lists.id")

# returns all members inside list '123456'
client.lists.members.all('123456', get_all=True)

# return the first 100 member's email addresses for the list with id 123456
...
```

Sections: python-mailchimp-api, Getting Started, Upgrading from v2.x, Upgrading from v1.x, Initialization, Pagination, Fields, Examples, API Structure, API Endpoints, Root, Automations

</details>

### robocorp-log

Automatic trace logging for Python

`pip install robocorp-log` · installs (wheel) · licence: Apache Software License · rank 9043 · last release 2026-11-01 · [PyPI](https://pypi.org/project/robocorp-log/) · [source](https://github.com/robocorp/robocorp/)

<details><summary>README extract</summary>

`robocorp-log` is a library which provides comprehensible logging for Python with a focus on Python automation, where detailed information on what happened and why a failure occurs is of vital importance.

> Note: The format of the log is not a part of the API and should not be relied upon as it can change even between minor versions.

Features:
Although Python logging is flexible it may be hard to analyze the logging afterwards and visualize it. Also, the format may end up using a big amount of disk space and it may be tedious to add logging calls to all places of interest.

Sections: robocorp-log, Why, How, Usage, Configuring with pyproject.toml, Caveats, Guides, API Reference

</details>

### gersemi

A formatter to make your CMake code the real treasure

`pip install gersemi` · installs (wheel) · licence: MPL-2.0 · rank 9051 · last release 2026-10-01 · [PyPI](https://pypi.org/project/gersemi/)

<details><summary>README extract</summary>

A formatter to make your CMake code the real treasure.

Sections: gersemi, Usage, pre-commit hook, Extensions in pre-commit hook, Formatting, Style, Default style `favour-inlining`, Example, Alternative style `favour-expansion`, Let's make a deal, `gersemi: ignore`, `gersemi: hints`, `gersemi: block_end`

</details>

### aiven-client

Aiven.io client library / command-line client

`pip install aiven-client` · installs (wheel) · licence: Apache Software License · rank 9054 · last release 2026-09-01 · [PyPI](https://pypi.org/project/aiven-client/) · [docs](https://docs.aiven.io/docs/tools/cli)

<details><summary>README extract</summary>

Aiven is a next-generation managed cloud services platform. Its focus is in
ease of adoption, high fault resilience, customer's peace of mind and
advanced features at competitive price points. See for
more information about the backend service.

aiven-client (`avn`) is the official command-line client for Aiven.

Sections: Aiven Client, Getting Started, Build an RPM Package, Log In, Usage, Authenticate: Logins and Tokens, Choose your Cloud, Working with Projects, Working with Application Users, Working with Permissions, Explore Existing Services, Launch Services, Managing service users, Service Integrations

</details>

### emval

emval is a blazingly fast email validator

`pip install emval` · installs (wheel) · licence: MIT License · rank 9065 · last release 2026-08-13 · [PyPI](https://pypi.org/project/emval/)

<details><summary>README extract</summary>

`emval` is a blazingly fast email validator written in Rust with Python bindings, offering performance improvements of 100-1000x over traditional validators.

Features:
- Drop-in replacement for popular email validators like `python-email-validator`, `verify-email`, and `pyIsEmail`.
- 100-1000x faster than python-email-validator.
- Validates email address syntax according to RFC 5322 and RFC 6531. ...

Example:
```python
from emval import validate_email, EmailValidator

email = "example@domain.com"

try:
    # Check if the email is valid.
    val_email = validate_email(email)
    # Utilize the normalized form for storage.
    normalized_email = val_email.normalized
except Exception as e:
...
```

...

</details>

### config-parser

Configuration library wrappers

`pip install config-parser` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 9066 · last release 2019-01-21 · [PyPI](https://pypi.org/project/config-parser/)

_README extract left out: share-alike licence._

### esphome-glyphsets

A lightweight version of glyphsets for ESPHome

`pip install esphome-glyphsets` · installs (wheel) · licence: Apache Software License 2.0 · rank 9085 · last release 2026-11-03 · [PyPI](https://pypi.org/project/esphome-glyphsets/) · [source](https://github.com/esphome-libs/esphome-glyphsets)

<details><summary>README extract</summary>

Source Code:

A lightweight version of glyphsets for ESPHome

Example:
```python
import esphome_glyphsets
```

Sections: esphome-glyphsets, Usage

</details>

### fastapi-profiler

A FastAPI Middleware of pyinstrument to check your service performance.

`pip install fastapi-profiler` · installs (wheel) · licence: MIT License · rank 9090 · last release 2026-03-24 · [PyPI](https://pypi.org/project/fastapi-profiler/)

### optionaldict

A dict-like object that ignore NoneType values for Python

`pip install optionaldict` · installs (wheel) · licence: MIT License · rank 9092 · last release 2021-01-15 · [PyPI](https://pypi.org/project/optionaldict/)

<details><summary>README extract</summary>

``optionaldict`` is a dict-like object that ignore NoneType values for Python which is pickable and JSON serializable.

Example:
```python
from optionaldict import optionaldict
```

Sections: optionaldict, Usage

</details>

### pyasn

Offline IP address to Autonomous System Number lookup module.

`pip install pyasn` · installs from source (sdist only) · licence: MIT License · rank 9104 · last release 2023-09-01 · [PyPI](https://pypi.org/project/pyasn/)

<details><summary>README extract</summary>

pyasn is a Python extension module that enables very fast IP address to Autonomous System Number lookups.
Current state and Historical lookups can be done, based on the MRT/RIB BGP archive used as input.

*pyasn* is different from other ASN lookup tools in that it provides offline and historical lookups. ...

Example:
```python
import pyasn

# Initialize module and load IP to ASN database
# the sample database can be downloaded or built - see below
asndb = pyasn.pyasn('ipasn_20140513.dat')

asndb.lookup('8.8.8.8')
# should return: (15169, '8.8.8.0/24'), the origin AS, and the BGP prefix it matches

asndb.get_as_prefixes(1128)
...
```

Sections: pyasn, Usage, IPASN Data Files, Performance Tip, Package Structure

</details>

### mailtrap

Official mailtrap.io API client

`pip install mailtrap` · installs (wheel) · licence: MIT License · rank 9108 · last release 2026-10-30 · [PyPI](https://pypi.org/project/mailtrap/) · [docs](https://github.com/mailtrap/mailtrap-python) · [source](https://github.com/mailtrap/mailtrap-python.git)

<details><summary>README extract</summary>

This Python package offers integration with the official API for Mailtrap.

Add email sending functionality to your Python application quickly with Mailtrap.

Example:
```python
import mailtrap as mt

API_TOKEN = ""  # your API key here

client = mt.MailtrapClient(token=API_TOKEN)

# Create mail object
mail = mt.Mail(
    sender=mt.Address(email="sender@example.com", name="John Smith"),
    to=[mt.Address(email="recipient@example.com")],
    subject="You are awesome!",
...
```

...

</details>

### aioprocessing

A Python 3.5+ library that integrates the multiprocessing module with asyncio.

`pip install aioprocessing` · installs (wheel) · licence: BSD License · rank 9153 · last release 2022-09-15 · [PyPI](https://pypi.org/project/aioprocessing/)

<details><summary>README extract</summary>

`aioprocessing` provides asynchronous, `asyncio` compatible, coroutine
versions of many blocking instance methods on objects in the `multiprocessing`
library. To use `dill` for universal pickling, install using `pip install aioprocessing[dill]`. Here's an example demonstrating the `aioprocessing` versions of
`Event`, `Queue`, and `Lock`: ...

Example:
```python
import time
import asyncio
import aioprocessing

def func(queue, event, lock, items):
    """ Demo worker function.

    This worker function runs in its own process, and uses
    normal blocking calls to aioprocessing objects, exactly
    the way you would use oridinary multiprocessing objects.

    """
    with lock:
        event.set()
...
```

</details>

### bloomfilter-py

Yet another bloomfilter implementation in Python

`pip install bloomfilter-py` · installs (wheel) · licence: MIT License · rank 9207 · last release 2026-10-26 · [PyPI](https://pypi.org/project/bloomfilter-py/) · [docs](https://github.com/OldPanda/bloomfilter-py/blob/master/README.md) · [source](https://github.com/OldPanda/bloomfilter-py.git)

<details><summary>README extract</summary>

Features:
Yet another Bloomfilter implementation in Python, compatible with Java's Guava library.

Compatibility targets Guava's compact `BloomFilter.writeTo` / `readFrom` format. ...

Example:
```python
>>> from bloomfilter import BloomFilter
>>> bloom_filter = BloomFilter(expected_insertions=500, err_rate=0.01)
>>> for i in range(100):
...     bloom_filter.put(i)
...
>>> 1 in bloom_filter
True
>>> 100 in bloom_filter
False
>>>
```

Sections: bloomfilter-py, Overview, Requirements, Backends and migration from 1.3, Bit storage and custom strategies, Usage Examples, Basic Usage, Guava Funnel Compatibility, Serialize Bloomfilter, Deserialize Bloomfilter, Stream I/O, Copies, Merging, and Statistics, Reproducible backend benchmarks, Auditing compatibility against an earlier checkout

</details>

### redislite

Redis built into a python package

`pip install redislite` · installs from source (sdist only) · licence: BSD License · rank 9227 · last release 2023-12-01 · [PyPI](https://pypi.org/project/redislite/) · [docs](https://redislite.readthedocs.io/en/latest/) · [source](https://github.com/yahoo/redislite)

<details><summary>README extract</summary>

Redislite is a self contained Python interface to the Redis key-value store.

It provides enhanced versions of the Redis-Py Python bindings for Redis. That provide the following added functionality:

* Easy to use - It provides a built in Redis server that is automatically installed, configured and managed when the Redis bindings are used. ...

Example:
```python
>>> from redislite import Redis
>>> redis_connection = Redis('/tmp/redis.db')
>>> redis_connection.keys()
[]
>>> redis_connection.set('key', 'value')
True
>>> redis_connection.get('key')
'value'
```

Sections: Redislite, Description, Requirements, Getting Started, Examples, Setting a value, Persistence, Compatibility, Running and using Multiple servers, More Information

</details>

### json-tricks

Extra features for Python's JSON: comments, order, numpy, pandas, datetimes, and many more! Simple but customizable.

`pip install json-tricks` · installs (wheel) · licence: BSD License · rank 9238 · last release 2023-08-19 · [PyPI](https://pypi.org/project/json-tricks/)

<details><summary>README extract</summary>

The [pyjson-tricks] package brings several pieces of
functionality to python handling of json files:

1. Store and load numpy arrays in human-readable format.
2. Store and load class instances both generic and customized.
3. Store and load date/times as a dictionary (including timezone).
4. Preserve map order `{}` using `OrderedDict`.
5. ...

Example:
```python
arr = arange(0, 10, 1, dtype=uint8).reshape((2, 5))
print(dumps({'mydata': arr}))
```

Sections: JSON tricks (python), Features, Numpy arrays, Class instances, Date, time, datetime and timedelta, Order, Comments, Other features, Preserve type vs use primitive, Tests

</details>

### language_tool_python

Checks grammar using LanguageTool.

`pip install language_tool_python` · installs (wheel) · licence: GPL-3.0-only · rank 9242 · last release 2026-05-14 · [PyPI](https://pypi.org/project/language_tool_python/) · [docs](https://language-tool-python.readthedocs.io/en/latest/) · [source](https://github.com/jxmorris12/language_tool_python.git)

_README extract left out: share-alike licence._

### json2xml

Simple Python Library to convert JSON to XML

`pip install json2xml` · installs (wheel) · licence: Apache Software License · rank 9249 · last release 2026-10-12 · [PyPI](https://pypi.org/project/json2xml/)

<details><summary>README extract</summary>

json2xml is a Python library and CLI for converting JSON data into XML. It is designed for teams that need predictable XML output, Python-first ergonomics, and a faster native path when conversion speed matters.

Documentation:

The library was initially dependent on the `dict2xml` project, but it has now been integrated into json2xml itself. ...

Features:
Use json2xml when you need:

* A Python library for turning dictionaries, strings, files, or API responses into XML
* A command-line tool for quick JSON-to-XML conversion from scripts and terminals
* Optional Rust acceleration with automatic ...

Example:
```python
from json2xml import json2xml
from json2xml.utils import readfromstring

data = readfromstring('{"name": "Ada", "language": "Python"}')
...

</details>

### timecode

SMPTE Time Code Manipulation Library

`pip install timecode` · installs from source (sdist only) · licence: MIT · rank 9271 · last release 2026-01-27 · [PyPI](https://pypi.org/project/timecode/) · [source](https://github.com/eoyilmaz/timecode)

<details><summary>README extract</summary>

About

Python module for manipulating SMPTE timecode. Supports all formats in the ST12
standard, as well as any arbitrary integer frame rates and some default str
values of 23.976, 23.98, 24, 25, 29.97, 30, 50, 59.94, 60 frame rates and
milliseconds (1000 fps) and fractional frame rates like "30000/1001". ...

Example:
```python
from timecode import Timecode

tc1 = Timecode('29.97', '00:00:00;00')
tc2 = Timecode(24, '00:00:00:10')
tc3 = tc1 + tc2
assert tc3.framerate == '29.97'
assert tc3.frames == 12
assert tc3 == '00:00:00:11'
```

</details>

### ansimarkup

Produce colored terminal text with an xml-like markup

`pip install ansimarkup` · installs (wheel) · licence: BSD License · rank 9272 · last release 2026-02-04 · [PyPI](https://pypi.org/project/ansimarkup/)

<details><summary>README extract</summary>

Ansimarkup is an XML-like markup for producing colored terminal text.

Example:
```python
from ansimarkup import ansiprint as print

print("bold text"))
print("red text", "red text on a green background")
print("orange text")
```

Sections: Ansimarkup, Usage, Basic, Colors and styles, User-defined tags, Alignment and length, Escaping raw strings, Other features, Command-line, Logging formatter, Windows, Performance, Limitations, Todo

</details>

### flake8-requirements

Package requirements checker, plugin for flake8

`pip install flake8-requirements` · installs (wheel) · licence: MIT License · rank 9274 · last release 2025-08-23 · [PyPI](https://pypi.org/project/flake8-requirements/)

<details><summary>README extract</summary>

This module provides a plug-in for flake8, which checks/validates
package import requirements. It reports missing and/or not used project direct dependencies.

This plug-in adds new flake8 warnings:

- `I900`: Package is not listed as a requirement.
- `I901`: Package is required but not used. (not implemented yet) ...

Sections: Package requirements checker, Important notice, Customization, FAQ

</details>

### openlayer

The official Python library for the openlayer API

`pip install openlayer` · installs (wheel) · licence: Apache Software License · rank 9283 · last release 2026-10-06 · [PyPI](https://pypi.org/project/openlayer/) · [source](https://github.com/openlayer-ai/openlayer-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Openlayer Python library provides convenient access to the Openlayer REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from openlayer import Openlayer

client = Openlayer(
    api_key=os.environ.get("OPENLAYER_API_KEY"),  # This is the default and can be omitted
)

response = client.inference_pipelines.data.stream(
    inference_pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    config={
        "input_variable_names": ["user_query"],
...
```

...

</details>

### django-db-connection-pool

Database connection pool component library for Django

`pip install django-db-connection-pool` · installs (wheel) · licence: MIT License · rank 9293 · last release 2025-05-05 · [PyPI](https://pypi.org/project/django-db-connection-pool/) · [source](https://github.com/altairbow/django-db-connection-pool)

<details><summary>README extract</summary>

:star: If this project is helpful to you, please light up the star, Thank you:smile:

MySQL & Oracle & PostgreSQL & JDBC (Oracle, OceanBase) connection pool components for Django,
Be based on SQLAlchemy.
Works fine in multiprocessing and multithreading django project.

* 中文版

Example:
```python
import dj_db_conn_pool

dj_db_conn_pool.setup(pool_size=100, max_overflow=50)
```

Sections: django-db-connection-pool, Quickstart, Update settings.DATABASES, MySQL, Oracle, PostgreSQL, Pool options(optional), multiprocessing environment, JDBC, Usage, Set Java runtime environment, OceanBase

</details>

### django-admin-extra-buttons

Django mixin to easily add buttons to any ModelAdmin

`pip install django-admin-extra-buttons` · installs (wheel) · licence: BSD License · rank 9297 · last release 2026-05-19 · [PyPI](https://pypi.org/project/django-admin-extra-buttons/) · [docs](https://saxix.github.io/django-admin-extra-buttons/)

<details><summary>README extract</summary>

This is a full rewriting of the original `django-admin-extra-url`. It
provides decorators to easily add custom buttons to Django Admin pages and/or add views to any ModelAdmin

It allows easy creation of wizards, actions and/or links to external resources
as well as api only views.

Four decorators are available: ...

Sections: django-admin-extra-buttons, Project Links

</details>

### empty-files

Serves empty files of many types

`pip install empty-files` · installs (wheel) · licence: Apache Software License · rank 9310 · last release 2023-07-30 · [PyPI](https://pypi.org/project/empty-files/)

<details><summary>README extract</summary>

TL;DR Null Object pattern for files.

Example:
```python
from empty_files.empty_files import create_empty_file
create_empty_file("temp/empty.jpg")
```

Sections: EmptyFiles.Python, Setup, Usage, Null Object Pattern, Attributions

</details>

### pytest-mysql

MySQL process and client fixtures for pytest

`pip install pytest-mysql` · installs (wheel) · licence: LGPL-3.0-or-later · rank 9312 · last release 2026-10-08 · [PyPI](https://pypi.org/project/pytest-mysql/) · [source](https://github.com/dbfixtures/pytest-mysql)

_README extract left out: share-alike licence._

### prosemirror

Python implementation of core ProseMirror modules for collaborative editing

`pip install prosemirror` · installs (wheel) · licence: BSD License · rank 9316 · last release 2026-02-21 · [PyPI](https://pypi.org/project/prosemirror/) · [source](https://github.com/fellowapp/prosemirror-py)

<details><summary>README extract</summary>

This package provides Python implementations of the following
ProseMirror packages:

- `prosemirror-model` version 1.25.4
- `prosemirror-transform` version 1.11.0
- `prosemirror-test-builder` version 1.1.1
- `prosemirror-schema-basic` version 1.2.4 ...

Features:
ProseMirror provides a powerful toolkit for building rich-text editors, but it's
JavaScript-only. Until now, the only option for manipulating and working with
ProseMirror documents from Python was to embed a JS runtime. ...

Example:
```python
from prosemirror.transform import Transform
from prosemirror.schema.basic import schema

# Create a document containing a single paragraph with the text "Hello, world!"
doc = schema.node(
    "doc", {}, [schema.node("paragraph", {}, [schema.text("Hello, world!")])]
)

...

</details>

### rolo

A Python framework for building HTTP-based server applications

`pip install rolo` · installs (wheel) · licence: Apache Software License · rank 9346 · last release 2026-10-14 · [PyPI](https://pypi.org/project/rolo/)

### objectpath

The agile query language for semi-structured data. #JSON

`pip install objectpath` · installs (wheel) · licence: MIT License · rank 9347 · last release 2018-11-27 · [PyPI](https://pypi.org/project/objectpath/)

<details><summary>README extract</summary>

#Python #NoSQL #Javascript #JSON #nested-array-object

ObjectPath is a query language similar to XPath or JSONPath, but much
more powerful thanks to embedded arithmetic calculations, comparison
mechanisms and built-in functions. ...

Sections: ObjectPath, The agile NoSQL query language for semi-structured data, Documentation, Command line usage, Python usage, Download

</details>

### letta-client

The official Python library for the letta API

`pip install letta-client` · installs (wheel) · licence: Apache Software License · rank 9352 · last release 2026-06-02 · [PyPI](https://pypi.org/project/letta-client/) · [source](https://github.com/letta-ai/letta-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Letta Python library provides convenient access to the Letta REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from letta_client import Letta

client = Letta(
    api_key=os.environ.get("LETTA_API_KEY"),  # This is the default and can be omitted
    # defaults to "cloud".
    environment="local",
)

archive = client.archives.create(
    name="name",
)
print(archive.id)
```

...

</details>

### arthur-client

Arthur Python API Client Library

`pip install arthur-client` · installs (wheel) · licence: MIT License · rank 9361 · last release 2026-11-07 · [PyPI](https://pypi.org/project/arthur-client/) · [docs](https://docs.arthur.ai)

<details><summary>README extract</summary>

Arthur is the platform for centralized monitoring of production models.
We help data scientists, product owners, and business leaders accelerate model operations to optimize
for accuracy, explainability, and fairness. ...

</details>

### scale-gp

The official Python library for the SGPClient API

`pip install scale-gp` · installs (wheel) · licence: Apache Software License · rank 9363 · last release 2026-05-14 · [PyPI](https://pypi.org/project/scale-gp/) · [source](https://github.com/scaleapi/sgp-python)

<details><summary>README extract</summary>

> ⚠️ This is the legacy v4 API SDK. For the latest v5 SDK, please use sgp-python-beta.

<!-- prettier-ignore -->

The SGP Client Python library provides convenient access to the SGP Client REST API from any Python 3.9+
application. ...

Example:
```python
import os
from scale_gp import SGPClient

client = SGPClient(
    api_key=os.environ.get("SGP_API_KEY"),  # This is the default and can be omitted
    # defaults to "production".
    environment="development",
)

create_knowledge_base_response = client.knowledge_bases.create(
    embedding_config={
...
```

Sections: SGP Client Python API library, Documentation, Usage, Async usage, With aiohttp, Streaming responses, Using types, Pagination, Nested params, Handling errors, Retries, Timeouts, Advanced, Logging

</details>

### newsapi-python

An unofficial Python client for the News API

`pip install newsapi-python` · installs (wheel) · licence: MIT License · rank 9367 · last release 2023-03-02 · [PyPI](https://pypi.org/project/newsapi-python/)

### phonic

(no summary)

`pip install phonic` · installs (wheel) · licence: MIT License · rank 9372 · last release 2026-11-05 · [PyPI](https://pypi.org/project/phonic/) · [source](https://github.com/Phonic-Co/phonic-python)

<details><summary>README extract</summary>

The Phonic Python library provides convenient access to the Phonic APIs from Python.

Example:
```python
from phonic import Phonic, CreateAgentRequestTemplateVariablesValue, CreateAgentRequestPronunciationDictionaryItem, CreateAgentRequestConfigurationEndpoint

client = Phonic(
    api_key="<token>",
)

client.agents.create(
    project="main",
    name="support-agent",
    phone_number="assign-automatically",
    timezone="America/Los_Angeles",
...
```

Sections: Phonic Python Library, Reference, Usage, Async Client, Exception Handling, Websockets, Advanced, Access Raw Response Data, Retries, Timeouts, Custom Client

</details>

### opentelemetry-instrumentation-absurd

OpenTelemetry instrumentation for the Absurd durable-task SDK

`pip install opentelemetry-instrumentation-absurd` · installs (wheel) · licence: MIT · rank 9376 · last release 2026-07-30 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-absurd/) · [source](https://github.com/jirikuncar/opentelemetry-instrumentation-absurd)

<details><summary>README extract</summary>

OpenTelemetry instrumentation for the Absurd
durable-task SDK (`absurd-sdk`).

Absurd (`absurd_sdk.AsyncAbsurd`) is a Postgres-backed durable task queue: a producer
`spawn()`s a task and a worker `work_batch()` claims and runs the registered handler, possibly
in a different process. ...

Example:
```python
from opentelemetry.instrumentation.absurd import AbsurdInstrumentor

AbsurdInstrumentor().instrument()
```

Sections: opentelemetry-instrumentation-absurd, Usage, Producer / consumer example, Span attributes, How it works, Compatibility, AI disclaimer

</details>

### pysmbc

Python bindings for libsmbclient

`pip install pysmbc` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 9377 · last release 2023-01-10 · [PyPI](https://pypi.org/project/pysmbc/)

_README extract left out: share-alike licence._

### mkl-include

Intel® oneAPI Math Kernel Library

`pip install mkl-include` · installs (wheel) · licence: Other/Proprietary License · rank 9379 · last release 2026-10-16 · [PyPI](https://pypi.org/project/mkl-include/)

<details><summary>README extract</summary>

Intel® oneAPI Math Kernel Library (Intel® oneMKL) is a computing math library of highly optimized, extensively threaded routines for applications that require maximum performance. This package provides C and Data Parallel C++ (DPC++) programming language interfaces. ...

</details>

### click-compose

Composable Click callback utilities for building flexible CLI applications.

`pip install click-compose` · installs (wheel) · licence: MIT · rank 9390 · last release 2026-09-16 · [PyPI](https://pypi.org/project/click-compose/) · [source](https://github.com/adamtheturtle/click-compose)

<details><summary>README extract</summary>

Composable Click callback utilities for building flexible CLI applications.

Example:
```python
"""Example of using multi_callback to combine validators."""

import click

from click_compose import multi_callback

def validate_positive(
    _ctx: click.Context | None,
    _param: click.Parameter | None,
    value: int,
) -> int:
    """Validate that value is positive."""
    if value <= 0:
        msg = "Must be positive"
...
```

Sections: click-compose, Quick Start, multi_callback, sequence_validator, deduplicate, Documentation

</details>

### uv-secure

Deprecated dependency scanner for uv projects; use uv audit instead

`pip install uv-secure` · installs (wheel) · licence: MIT · rank 9402 · last release 2026-04-18 · [PyPI](https://pypi.org/project/uv-secure/) · [docs](https://github.com/owenlamont/uv-secure#readme) · [source](https://github.com/owenlamont/uv-secure)

<details><summary>README extract</summary>

Deprecated dependency scanner for uv projects. Prefer `uv audit` for new use.

I created uv-secure to resolve some pain points I had with getting pip-audit to work
with uv.lock files. Since
`uv audit` was announced though I
now use that for my repos and am deprecating uv-secure in favour of the `uv audit`
command. ...

Sections: uv-secure, Deprecation Notice, Scope and Limitations, Disclaimer, Optional Dependencies, Usage, Configuration, uv-secure.toml / .uv-secure.toml, pyproject.toml, File Caching, Cache Performance on Windows, Configuration discovery, Vulnerability Severity Data, Pre-commit Usage

</details>

### pytest-print

pytest-print adds the printer fixture you can use to print messages to the user (directly to the pytest runner, not stdout)

`pip install pytest-print` · installs (wheel) · licence: MIT · rank 9429 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pytest-print/) · [source](https://github.com/pytest-dev/pytest-print)

<details><summary>README extract</summary>

Allows to print extra content onto the PyTest reporting. This can be used for example to report sub-steps for long
running tests, or to print debug information in your tests when you cannot debug the code (so that the end user does not
need to wonder if the test froze/dead locked or not).

Changelog · Contributing.

<!--ts-->

- Install ...

Example:
```python
from future import annotations

from typing import TYPE_CHECKING, Iterator

import pytest

if TYPE_CHECKING:
    from pytest_print import Printer

@pytest.fixture(scope="session")
def _expensive_setup(printer_session: Printer) -> Iterator[None]:
    printer_session("setup")
    yield
    printer_session("teardown")

...
```

...

</details>

### artifactory

A Python to Artifactory interface

`pip install artifactory` · installs from source (sdist only) · licence: MIT License · rank 9431 · last release 2016-03-12 · [PyPI](https://pypi.org/project/artifactory/)

<details><summary>README extract</summary>

This module is intended to serve as a logical descendant of
pathlib, a Python 3
module for object-oriented path manipulations. As such, it implements
everything as closely as possible to the origin with few exceptions,
such as stat().

Example:
```python
from artifactory import ArtifactoryPath
path = ArtifactoryPath(
    "
for p in path:
    print p
```

Sections: Python interface library for Jfrog Artifactory, Usage Examples, Walking Directory Tree, Downloading Artifacts, Uploading Artifacts, Authentication, SSL Cert Verification Options, Global Configuration File

</details>

### pytoniq-core-fork

TON Blockchain SDK

`pip install pytoniq-core-fork` · installs (wheel) · licence: not stated · rank 9450 · last release 2026-02-27 · [PyPI](https://pypi.org/project/pytoniq-core-fork/)

<details><summary>README extract</summary>

This is a fork of pytoniq-core. It extends compatibility to Python 3.7, 3.8, and 3.9, as the original package strictly requires Python >= 3.10.

Sections: pytoniq-core, Examples, Structure, boc, crypto, proof, tl, tl-b

</details>

### regipy

Python Registry Parser

`pip install regipy` · installs (wheel) · licence: MIT License · rank 9454 · last release 2026-10-12 · [PyPI](https://pypi.org/project/regipy/) · [source](https://github.com/mkorman90/regipy/)

<details><summary>README extract</summary>

Regipy is a python library for parsing offline registry hives!

Requires Python 3.9 or higher.

Features:

* Use as a library
* Recurse over the registry hive, from root or a given path and get all subkeys and values
* Read specific subkeys and values
* Apply transaction logs on a registry hive ...

Example:
```python
from regipy.registry import RegistryHive
reg = RegistryHive('/Users/martinkorman/Documents/TestEvidence/Registry/Vibranium-NTUSER.DAT')

# Iterate over a registry hive recursively:
for entry in reg.recurse_subkeys(as_json=True):
    print(entry)

# Iterate over a key and get all subkeys and their modification time:
...
```

Sections: regipy, Using as a library, Rust-accelerated backend (alpha), Plugin Validation, Available Plugins

</details>

### gmqtt

Client for MQTT protocol

`pip install gmqtt` · installs (wheel) · licence: MIT License · rank 9462 · last release 2026-10-08 · [PyPI](https://pypi.org/project/gmqtt/)

<details><summary>README extract</summary>

Example:
```python
import asyncio
import os
import signal
import time

from gmqtt import Client as MQTTClient

# gmqtt also compatibility with uvloop
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

STOP = asyncio.Event()

def on_connect(client, flags, rc, properties):
    print('Connected')
    client.subscribe('TEST/#', qos=0)

...
```

Sections: gmqtt: Python async MQTT client implementation., Usage, Getting Started, MQTT Version 5.0, Version setup, Properties, Connect properties, Publish properties, Subscribe properties, Reconnects, Asynchronous on_message callback, Other examples

</details>

### approvaltests

Assertion/verification library to aid testing

`pip install approvaltests` · installs (wheel) · licence: Apache-2.0 · rank 9474 · last release 2026-10-25 · [PyPI](https://pypi.org/project/approvaltests/)

<details><summary>README extract</summary>

Features:
Approvals work by comparing the test results to a golden master. If no golden master exists you can create a snapshot
of the current test results and use that as the golden master. The reporter helps you manage the golden master. ...

Example:
```python
from approvaltests.approvals import verify

def test_simple() -> None:
    result = "Hello ApprovalTests"
    verify(result)
```

Sections: ApprovalTests.Python, What can I use ApprovalTests for?, Getting Started, What Are Approvals, New Projects, Minimal Example Tutorial, Adding to Existing Projects, Overview, Example using pytest, Example using unittest, Example using CLI, Usage, Argument Definitions, Reporters

</details>

### prefect-dask

Prefect integrations with the Dask execution framework.

`pip install prefect-dask` · installs (wheel) · licence: Apache Software License · rank 9482 · last release 2026-06-05 · [PyPI](https://pypi.org/project/prefect-dask/)

### pydocumentdb

Azure DocumentDB Python SDK

`pip install pydocumentdb` · installs (wheel) · licence: MIT License · rank 9509 · last release 2019-10-01 · [PyPI](https://pypi.org/project/pydocumentdb/)

<details><summary>README extract</summary>

🚨🚨🚨 The pydocumentdb package for versions 1.x and 2.x of the Azure Cosmos DB Python SDK for SQL API will be retired August 20, 2020.
See the release and retirement documentation for more information.

Please use the latest version of the Python SDK with new package name, azure-cosmos.🚨🚨🚨

- Updated README regarding package deprecation ...

Sections: Changes in 2.3.5, Changes in 2.3.3, Changes in 2.3.2, Changes in 2.3.1, Changes in 2.3.0, Changes in 2.2.1, Changes in 2.2.0, Changes in 2.1.0, Changes in 2.0.1, Changes in 2.0.0, Changes in 1.9.0, Changes in 1.8.0, Changes in 1.7.0, Changes in 1.6.1

</details>

### pydivert

Python binding to WinDivert (Windows) and eBPFDivert (Linux) for packet capture, filtering and injection

`pip install pydivert` · installs (wheel) · licence: LGPL-3.0-or-later OR GPL-2.0-or-later · rank 9525 · last release 2026-10-25 · [PyPI](https://pypi.org/project/pydivert/) · [source](https://github.com/ffalcinelli/pydivert.git)

_README extract left out: share-alike licence._

### fastcrud

FastCRUD is a Python package for FastAPI, offering robust async CRUD operations and flexible endpoint creation utilities.

`pip install fastcrud` · installs (wheel) · licence: MIT · rank 9541 · last release 2026-10-12 · [PyPI](https://pypi.org/project/fastcrud/) · [source](https://github.com/benavlabs/fastcrud)

<details><summary>README extract</summary>

Powerful CRUD methods and automatic endpoint creation for FastAPI.

FastCRUD is a Python package for FastAPI, offering robust async CRUD operations and flexible endpoint creation utilities, streamlined through advanced features like auto-detected join conditions, dynamic sorting, and offset and cursor pagination. ...

Features:
- ⚡️ Fully Async: Leverages Python's async capabilities for non-blocking database operations.
- 📚 SQLAlchemy 2.0: Works with the latest SQLAlchemy version for robust database interactions. ...

Example:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Item(Base):
    tablename = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
...

</details>

### jsonable

An abstract class that supports jsonserialization/deserialization.

`pip install jsonable` · installs (wheel) · licence: MIT License · rank 9549 · last release 2015-10-01 · [PyPI](https://pypi.org/project/jsonable/)

<details><summary>README extract</summary>

This library provides and abstract base class `JSONable` which enables easy definition of trivially JSON-able python objects.

* Installation: `pip install jsonable`

:Example:

 >>> import jsonable
 >>>
 >>>
 >>> class Fruit(jsonable.Type):
 ... slots = ('type', 'weight')
 ...
 ... def initialize(self, type, weight):
 ... ...

</details>

### none

An extensive library providing additional facilities to the Python Standard Library.

`pip install none` · installs (wheel) · licence: MIT License · rank 9551 · last release 2022-08-08 · [PyPI](https://pypi.org/project/none/) · [source](https://github.com/spack971/none)

<details><summary>README extract</summary>

In the beginning there was none, and then bang a bunch of extra batteries
started to fill the Python universe.

*None* is an extensive Python library offering a range of extra facilities not
found in the Python Standard Library.

This software project is provided under the licensing terms of the
MIT License stated in the file `LICENSE.rst`. ...

Sections: none, Licensing

</details>

### tronpy

TRON Python client library

`pip install tronpy` · installs (wheel) · licence: MIT · rank 9560 · last release 2026-11-06 · [PyPI](https://pypi.org/project/tronpy/) · [docs](https://tronpy.bitcart.ai) · [source](https://github.com/bitcart/tronpy)

<details><summary>README extract</summary>

TRON Python Client Library. Documentation

> Note: in case you want to use cryptocurrency functions in an universal way or e.g. reliably calculate transaction fees for BTC, ETH, Tron and many others, check out the Bitcart project

Example:
```python
from tronpy import Tron
from tronpy.keys import PrivateKey

client = Tron(network="nile")
# Private key of TJzXt1sZautjqXnpjQT4xSCBHNSYgBkDr3
priv_key = PrivateKey(bytes.fromhex("8888888888888888888888888888888888888888888888888888888888888888"))

txn = (
...
```

Sections: tronpy, How to use, Async Client

</details>

### paid-python

(no summary)

`pip install paid-python` · does not install on CPython 3.14 · licence: not stated · rank 9576 · last release 2026-10-27 · [PyPI](https://pypi.org/project/paid-python/) · [source](https://github.com/paid-ai/paid-python)

<details><summary>README extract</summary>

Paid is the all-in-one, drop-in Business Engine for AI Agents that handles your pricing, subscriptions, margins, billing, and renewals with just 5 lines of code.
The Paid Python library provides convenient access to the Paid API from Python applications.

See the full API docs here

Example:
```python
from paid import Paid

client = Paid(token="API_KEY")

client.customers.create_customer(
    name="name"
)
```

Sections: Documentation, Usage, Request And Response Types, Exception Handling, Logging, Environment Variables, `PAID_API_KEY`, `PAID_ENABLED`, `PAID_LOG_LEVEL`, `PAID_OTEL_COLLECTOR_ENDPOINT`, Cost Tracking via OTEL tracing, Simple Decorator and Context Manager Methods, As a Decorator, As a Context Manager

</details>

### prefect-redis

Prefect integrations with Redis.

`pip install prefect-redis` · installs (wheel) · licence: Apache Software License · rank 9585 · last release 2026-10-07 · [PyPI](https://pypi.org/project/prefect-redis/)

<details><summary>README extract</summary>

For more information about how to use Prefect, please refer to the Prefect documentation.

</details>

### nipyapi

A rich Apache NiFi Python Client SDK

`pip install nipyapi` · installs (wheel) · licence: Apache-2.0 · rank 9589 · last release 2026-10-24 · [PyPI](https://pypi.org/project/nipyapi/) · [docs](https://nipyapi.readthedocs.io/en/latest/) · [source](https://github.com/Chaffelson/nipyapi.git)

<details><summary>README extract</summary>

Nifi-Python-Api: A rich Apache NiFi Python Client SDK

Features:
Multiple interfaces for working with Apache NiFi:
 - Command-Line Interface: Shell access for scripting and CI/CD pipelines (`pip install nipyapi[cli]`)
 - Mid-level Client SDK: Python functions for typical complex tasks
 - Low-level Client SDKs: ...

Example:
```python
# Clone the repository (includes Docker profiles and Makefile)
git clone
cd nipyapi

# Install NiPyAPI in development mode
pip install -e ".[dev]"

# Start complete NiFi environment (this may take a few minutes)
make certs && make up NIPYAPI_PROFILE=single-user && make wait-ready NIPYAPI_PROFILE=single-user

# Test the connection
python3 -c "
...
```

Sections: NiPyApi, Features, Quick Start, Background and Documentation

</details>

### PyChromecast

Python module to talk to Google Chromecast.

`pip install PyChromecast` · installs (wheel) · licence: MIT License · rank 9590 · last release 2026-11-03 · [PyPI](https://pypi.org/project/PyChromecast/)

<details><summary>README extract</summary>

Library for Python 3.11+ to communicate with the Google Chromecast. It
currently supports:

- Auto discovering connected Chromecasts on the network
- Start the default media receiver and play any online media
- Control playback of current playing media
- Implement Google Chromecast api v2
- Communicate with apps via channels ...

Example:
```python
>> import time
>> import pychromecast
>> import zeroconf

>> # Create a browser which prints the friendly name of found chromecast devices
>> zconf = zeroconf.Zeroconf()
>> browser = pychromecast.CastBrowser(pychromecast.SimpleCastListener(lambda uuid, service: print(browser.devices[uuid].friendly_name)), zconf)
>> browser.start_discovery()
...
```

...

</details>

### pytest-faker

Faker integration with the pytest framework.

`pip install pytest-faker` · installs from source (sdist only) · licence: MIT License · rank 9615 · last release 2016-12-19 · [PyPI](https://pypi.org/project/pytest-faker/)

<details><summary>README extract</summary>

Faker integration with the pytest test runner

pytest-faker adds Faker fixtures for easy use of Faker for your tests under pytest runner.

Example:
```python
from faker.generator import Generator

def test_faker(faker):
    """Faker factory is a fixture."""
    assert isinstance(faker, Generator)
    assert isinstance(faker.name(), str)
```

Sections: Example, 2.0.0, 1.1.0, 1.0.0

</details>

### todoist_api_python

Official Python SDK for the Todoist API.

`pip install todoist_api_python` · installs (wheel) · licence: MIT · rank 9660 · last release 2026-11-03 · [PyPI](https://pypi.org/project/todoist_api_python/) · [docs](https://doist.github.io/todoist-api-python) · [source](https://github.com/Doist/todoist-api-python)

<details><summary>README extract</summary>

This is the official Python SDK for the Todoist API.

Example:
```python
from todoist_api_python.api import TodoistAPI

api = TodoistAPI("YOUR_API_TOKEN")

task = api.get_task("6X4Vw2Hfmg73Q2XR")
print(f"Task: {task.content}")

comments_iter = api.get_comments(task_id=task.id)
for comments in comments_iter:
    for comment in comments:
        print(f"Comment: {comment.content}")
```

Sections: Todoist API Python Client, Usage, Async usage, Documentation, Migrating from 3.x, Feedback

</details>

### mr-proper

Static Python code analyzer, that tries to check if functions in code are pure or not and why.

`pip install mr-proper` · installs (wheel) · licence: MIT · rank 9690 · last release 2021-10-27 · [PyPI](https://pypi.org/project/mr-proper/)

<details><summary>README extract</summary>

Static Python code analyzer, that tries to check if functions in code are
pure or not and why.

*DISCLAIMER*: this library is very experimental and has a lot of edge cases.
Functions that mr. Proper marks as pure can be not pure, but they are
usually cleaner than other functions.

Example:
```python
# test.py
def add_one(n: int) -> int:
    return n + 1

def print_amount_of_users(users_qs: QuerySet) -> None:
    print(f'Current amount of users is {users_qs.count()}')
```

Sections: mr. Proper, What mr. Proper check, Example, Parameters, Code prerequisites

</details>

### fugue-sql-antlr

Fugue SQL Antlr Parser

`pip install fugue-sql-antlr` · installs from source (sdist only) · licence: Apache Software License · rank 9700 · last release 2026-02-19 · [PyPI](https://pypi.org/project/fugue-sql-antlr/)

<details><summary>README extract</summary>

Chat with us on slack!

This is the dedicated package for the Fugue SQL parser built on Antlr4. It consists of two packages: fugue-sql-antlr and fugue-sql-antlr-cpp.

fugue-sql-antlr is the main package. It contains the python parser of Fugue SQL and the vistor for the parser tree.

fugue-sql-antlr-cpp is the C++ implementation of the parser. ...

Sections: Fugue SQL Antlr Parser

</details>

### approval-utilities

Utilities for your production code that work well with approvaltests

`pip install approval-utilities` · installs (wheel) · licence: Apache-2.0 · rank 9706 · last release 2026-10-25 · [PyPI](https://pypi.org/project/approval-utilities/)

### semanticscholar

Unofficial Python client library for Semantic Scholar APIs.

`pip install semanticscholar` · installs (wheel) · licence: MIT License · rank 9719 · last release 2026-03-29 · [PyPI](https://pypi.org/project/semanticscholar/)

<details><summary>README extract</summary>

Unofficial Python client library for Semantic Scholar APIs.

- Simplified access to the Semantic Scholar APIs
- Support for the Academic Graph, Recommendations, and Datasets APIs
- Typed responses
- Streamlined navigation of paginated responses
- Support for asynchronous requests

Example:
```python
# First, import the client from semanticscholar module
from semanticscholar import SemanticScholar

# You'll need an instance of the client to request data from the API
sch = SemanticScholar()

# Get a paper by its ID
paper = sch.get_paper('10.1093/mind/lix.236.433')

# Print the paper title
print(paper.title)
```

Sections: semanticscholar, Main features, Quickstart, Usage, What next?, Semantic Scholar API official docs

</details>

### landingai-ade

The official Python library for the landingai-ade API

`pip install landingai-ade` · installs (wheel) · licence: Apache Software License · rank 9739 · last release 2026-09-17 · [PyPI](https://pypi.org/project/landingai-ade/) · [source](https://github.com/landing-ai/ade-python)

<details><summary>README extract</summary>

Docs · Playground · LandingAI

The official Python library for the LandingAI Agentic Document Extraction (ADE) API. Parse PDFs and images into structured, grounded Markdown, then extract typed fields with a JSON Schema or Pydantic model.

- Fully typed requests and Pydantic response models
- Sync and async clients with identical surfaces ...

Example:
```python
from pathlib import Path
from pydantic import BaseModel, Field
from landingai_ade import LandingAIADE

class Invoice(BaseModel):
    invoice_number: str = Field(description="The invoice number")
    total: str = Field(description="Invoice grand total")

client = LandingAIADE()  # reads VISION_AGENT_API_KEY

...
```

...

</details>

### scrapli

Fast, flexible, sync/async, Python 3.10+ screen scraping client specifically for network devices

`pip install scrapli` · installs (wheel) · licence: MIT · rank 9740 · last release 2026-10-14 · [PyPI](https://pypi.org/project/scrapli/) · [docs](https://carlmontanari.github.io/scrapli/)

<details><summary>README extract</summary>

scrapli -- scrap(e c)li -- is a python 3.10+ library focused on connecting to devices, specifically network devices
 (routers/switches/firewalls/etc.) via Telnet, SSH or NETCONF.

</details>

### sentinel

Create sentinel objects, akin to None, NotImplemented, Ellipsis

`pip install sentinel` · installs (wheel) · licence: MIT License · rank 9742 · last release 2022-07-23 · [PyPI](https://pypi.org/project/sentinel/) · [source](https://github.com/eddieantonio/sentinel.git)

<details><summary>README extract</summary>

Creates simple sentinel objects.

Features:
- sentinels are unique
- sentinels are singletons — the only instance of their own anonymous class
- sentinels can be used with `is` comparisons
- sentinels can be used with `pickle`
- sentinels can be used with `copy.deepcopy ...

Example:
```python
import sentinel

MySentinel = sentinel.create()

print(MySentinel)  # prints `MySentinel`
```

Sections: sentinel — create sentinel and singleton objects, What is a sentinel?, Features, Usage, Example, Adding extra methods and class attributes

</details>

### safe-init

Safe Init is a Python library that enhances AWS Lambda functions with advanced error handling, logging, monitoring, and resilience features, providing comprehensive observability and reliability for serverless applications.

`pip install safe-init` · does not install on CPython 3.14 · licence: MIT · rank 9756 · last release 2026-10-19 · [PyPI](https://pypi.org/project/safe-init/) · [docs](https://safe-init.readthedocs.io/en/latest/) · [source](https://github.com/kalepa/safe-init)

<details><summary>README extract</summary>

Safe Init is a Python library that provides a comprehensive set of tools for initializing AWS Lambda functions safely and handling errors and exceptions gracefully. It is designed to make your Lambda functions more robust, easier to debug, and less prone to unexpected failures. ...

Example:
```python
from contextvars import ContextVar
from typing import Callable

import logging

def custom_logger():
    return logging.getLogger("my_custom_logger")

safe_init_logger_getter: ContextVar[Callable] = ContextVar("safe_init_logger_getter")
safe_init_logger_getter.set(custom_logger)
```

...

</details>

### pytest-shutil

A goodie-bag of unix shell and environment tools for py.test

`pip install pytest-shutil` · installs (wheel) · licence: MIT License · rank 9773 · last release 2024-11-29 · [PyPI](https://pypi.org/project/pytest-shutil/)

<details><summary>README extract</summary>

This library is a goodie-bag of Unix shell and environment management tools for automated tests.
A summary of the available functions is below, look at the source for the full listing.

Example:
```python
# Enable the fixture explicitly in your tests or conftest.py (not required when using setuptools entry points)
pytest_plugins = ['pytest_shutil']

def test_something(workspace):
    # Workspaces contain a handle to the path `path` object (see
    path = workspace.workspace
    script = path / 'hello.sh'
...
```

...

</details>

### tower

Tower CLI and runtime environment for Tower.

`pip install tower` · installs (wheel) · licence: MIT License · rank 9777 · last release 2026-09-21 · [PyPI](https://pypi.org/project/tower/)

<details><summary>README extract</summary>

The CLI and Python runtime for Tower - deploy your AI and hand-written Python code to production in minutes.

> Bridge the last mile from code to production.

Code-first platform for deploying Python data apps, pipelines, and AI agents, with built-in orchestration, analytical storage, and multi-tenant APIs. ...

Features:
Are you shipping your Python code to prod but struggling to:

- Turn scripts into production services
- Expose APIs for users and customers/tenants
- Store and query analytical data
- Run reliably across environments

Tower gives you: ...

Sections: Tower CLI, What is Tower?, Why Tower?, Quick Start, Add Tower to Claude, Add Tower to Cursor, Add Tower to other AI Assistants, Features, Demo, Use Cases, Comparison, How It Works, Roadmap, Not For

</details>

### snakebite-py3

Pure Python HDFS client

`pip install snakebite-py3` · installs (wheel) · licence: Apache License 2.0 · rank 9792 · last release 2025-02-18 · [PyPI](https://pypi.org/project/snakebite-py3/)

<details><summary>README extract</summary>

🐍 About This Fork🍴

This is a fork of via
 We maintain it enough
to work for our needs at the Internet Archive. We use the library with our CDH5
cluster and have not tested it with any other versions of hadoop. Please help
us improve this! Or make your own fork. No hard feelings. ...

</details>

### vmware-vapi-runtime

VMware vAPI Runtime

`pip install vmware-vapi-runtime` · installs (wheel) · licence: Apache Software License · rank 9800 · last release 2026-09-03 · [PyPI](https://pypi.org/project/vmware-vapi-runtime/)

<details><summary>README extract</summary>

VMware vAPI Runtime is a client library which facilitates invocations of the VCF SDK APIs from a Python application. It contains HTTP client, API messages serializers, and API input/output validators and converters to native Python types. ...

Sections: VMware vAPI Runtime, Getting started, Prerequisites

</details>

### multiprocessing-logging

Logger for multiprocessing applications

`pip install multiprocessing-logging` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 9817 · last release 2026-08-19 · [PyPI](https://pypi.org/project/multiprocessing-logging/)

_README extract left out: share-alike licence._

### notebooklm-py

Unofficial Python library for automating Google NotebookLM

`pip install notebooklm-py` · installs (wheel) · licence: MIT License · rank 9826 · last release 2026-10-29 · [PyPI](https://pypi.org/project/notebooklm-py/) · [docs](https://github.com/teng-lin/notebooklm-py#readme) · [source](https://github.com/teng-lin/notebooklm-py)

<details><summary>README extract</summary>

A Comprehensive Google Gemini Notebook Skill & Unofficial Python API. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw.

> Note (July 2026): Google rebranded NotebookLM to Gemini Notebook. ...

Example:
```python
import asyncio
from notebooklm import NotebookLMClient, MindMapKind

async def main():
    async with NotebookLMClient.from_storage() as client:
        # Create notebook and add sources
        nb = await client.notebooks.create("Research")
        await client.sources.add_url(nb.id, " wait=True)

        # Chat with your sources
...
```

...

</details>

### mastercard-oauth1-signer

Mastercard OAuth1 Signer.

`pip install mastercard-oauth1-signer` · does not install on CPython 3.14 · licence: MIT · rank 9854 · last release 2026-11-03 · [PyPI](https://pypi.org/project/mastercard-oauth1-signer/)

<details><summary>README extract</summary>

Python library for generating a Mastercard API compliant OAuth signature.

</details>

### vmware-vapi-common-client

VMware vAPI Common Services Client Bindings

`pip install vmware-vapi-common-client` · installs (wheel) · licence: Apache Software License · rank 9859 · last release 2026-09-03 · [PyPI](https://pypi.org/project/vmware-vapi-common-client/)

<details><summary>README extract</summary>

VMware vAPI Common Client is a client library which contains Python language bindings for core APIs like Session, Tasks and API Metadata.

Sections: VMware vAPI Common Client, Getting started, Prerequisites

</details>

### flake8-pyi

A plugin for flake8 to enable linting .pyi stub files.

`pip install flake8-pyi` · installs (wheel) · licence: MIT · rank 9863 · last release 2026-05-11 · [PyPI](https://pypi.org/project/flake8-pyi/) · [source](https://github.com/PyCQA/flake8-pyi)

<details><summary>README extract</summary>

A plugin for Flake8 that provides specializations for
type hinting stub files,
especially interesting for linting
typeshed.

Refer to this documentation for more
details on stub files.

1. Adds the `.pyi` extension to the default value of the `--filename`
 command-line argument to Flake8. ...

Sections: flake8-pyi, Functionality, Lints provided, See also

</details>

### pygtail

Reads log file lines that have not been read.

`pip install pygtail` · installs (wheel) · licence: GNU General Public License (GPL) · rank 9865 · last release 2022-11-06 · [PyPI](https://pypi.org/project/pygtail/)

_README extract left out: share-alike licence._

### BeautifulSoup

Screen-scraping library

`pip install BeautifulSoup` · installs from source (sdist only) · licence: Python Software Foundation License · rank 9869 · last release 2019-10-05 · [PyPI](https://pypi.org/project/BeautifulSoup/)

<details><summary>README extract</summary>

Beautiful Soup is a library that makes it easy to scrape information
from web pages. It sits atop an HTML or XML parser, providing Pythonic
idioms for iterating, searching, and modifying the parse tree.

You should use the 'beautifulsoup4' package instead of this package. ...

</details>

### gofeatureflag-python-provider

GO Feature Flag provider for OpenFeature

`pip install gofeatureflag-python-provider` · installs (wheel) · licence: Apache-2.0 · rank 9870 · last release 2026-09-01 · [PyPI](https://pypi.org/project/gofeatureflag-python-provider/) · [docs](https://github.com/thomaspoignant/go-feature-flag/tree/main/openfeature/providers/python-provider) · [source](https://github.com/thomaspoignant/go-feature-flag/tree/main/openfeature/providers/python-provider)

<details><summary>README extract</summary>

GO Feature Flag provider allows you to connect to your GO Feature Flag instance.

GO Feature Flag believes in simplicity and offers a simple and lightweight solution to use feature flags.
Our focus is to avoid any complex infrastructure work to use GO Feature Flag. ...

Example:
```python
from gofeatureflag_python_provider.provider import GoFeatureFlagProvider
from gofeatureflag_python_provider.options import GoFeatureFlagOptions, EvaluationType
from openfeature import api
from openfeature.evaluation_context import EvaluationContext

goff_provider = GoFeatureFlagProvider(
    options=GoFeatureFlagOptions(
        endpoint="
...
```

...

</details>

### biip

Biip interprets the data in barcodes.

`pip install biip` · installs (wheel) · licence: Apache-2.0 · rank 9882 · last release 2026-10-25 · [PyPI](https://pypi.org/project/biip/) · [docs](https://biip.readthedocs.io) · [source](https://github.com/jodal/biip)

<details><summary>README extract</summary>

_Biip interprets the data in barcodes._

Biip is a Python library for making sense of the data in barcodes.

The library can interpret the following formats:

- GTIN-8, GTIN-12, GTIN-13, and GTIN-14 numbers,
 commonly found in EAN-8, EAN-13, and ITF-14 barcodes.

- GS1 AI element strings,
 commonly found in GS1-128 barcodes. ...

Example:
```python
>>> from rich import print
>>> import biip
>>> print(biip.parse("]E09781492053743"))
ParseResult(
    value=']E09781492053743',
    symbology_identifier=SymbologyIdentifier(
        value=']E0',
        iso_symbology=ISOSymbology.EAN_UPC,
        modifiers='0',
        gs1_symbology=GS1Symbology.EAN_13
    ),
    gtin=Gtin(
...
```

Sections: &#x1F4E6; Biip, Example, Project resources

</details>

### pymupdf-stubs

Type stubs for PyMuPDF (fitz), automatically generated

`pip install pymupdf-stubs` · installs (wheel) · licence: Apache Software License · rank 9904 · last release 2026-08-10 · [PyPI](https://pypi.org/project/pymupdf-stubs/) · [source](https://github.com/elohmeier/pymupdf-stubs)

<details><summary>README extract</summary>

Type stubs for PyMuPDF (`pymupdf` / `fitz`), published as a PEP 561 stub-only package.

Example:
```python
import pymupdf
import fitz

doc = pymupdf.Document()
page = doc[0]
drawings = page.get_drawings()
```

Sections: pymupdf-stubs, Usage, Type Checking, Compatibility Notes

</details>

### theine

high performance in-memory cache

`pip install theine` · installs (wheel) · licence: BSD-3-Clause · rank 9906 · last release 2025-08-17 · [PyPI](https://pypi.org/project/theine/)

<details><summary>README extract</summary>

High performance in-memory cache inspired by Caffeine.

- High performance Rust core
- High hit ratio with adaptive W-TinyLFU eviction policy
- Expired data are removed automatically using hierarchical timer wheel
- Fully typed
- Thread-safe with Free-Threading support (tested on Python 3.13.6t)
- Django cache backend ...

Example:
```python
cache = Cache("tlfu", 10000)

@Memoize(Cache("tlfu", 10000), timedelta(seconds=100))
...
```

Sections: Theine, Theine V2 Migration Guide, Cache Class and Memoize Decorator, Renaming `timeout` to `ttl`, Thread Safety by Default, Single Expiration Handling Thread for All Cache Instances, Improved Adaptive Cache Eviction Policy, Requirements, Design, API, Cache Client, Cache Decorator, Django Cache Backend, Core Metadata Memory Overhead

</details>

### throttled-py

🔧 High-performance Python rate limiting library with multiple algorithms (Fixed Window, Sliding Window, Token Bucket, Leaky Bucket & GCRA) and storage backends (Redis, In-Memory).

`pip install throttled-py` · installs (wheel) · licence: MIT License · rank 9928 · last release 2026-08-30 · [PyPI](https://pypi.org/project/throttled-py/) · [docs](https://throttled-py.readthedocs.io) · [source](https://github.com/ZhuoZhuoCrayon/throttled-py)

<details><summary>README extract</summary>

🔧 High-performance Python rate limiting library with multiple algorithms (Fixed Window, Sliding Window, Token Bucket, Leaky Bucket & GCRA) and storage backends (Redis, In-Memory).

简体中文 | English

🔰 Installation | 🎨 Quick Start | 📝 Usage | ⚙️ Data Models | 📊 Benchmarks | 🍃 Inspiration | 📚 Version History | 📄 License

Example:
```python
from throttled import RateLimiterType, Throttled, utils

throttle = Throttled(
    # 📈 Use Token Bucket algorithm
    using=RateLimiterType.TOKEN_BUCKET.value,
    # 🪣 Set quota: 1,000 tokens per second (limit), bucket size 1,000 (burst)
    quota="1000/s burst 1000",
    # 📁 By default, global MemoryStore is used as the storage backend.
)

...
```

...

</details>

### b2

Command Line Tool for Backblaze B2

`pip install b2` · installs (wheel) · licence: MIT License · rank 9969 · last release 2026-10-23 · [PyPI](https://pypi.org/project/b2/)

<details><summary>README extract</summary>

&nbsp;&nbsp;&nbsp;&nbsp;

The command-line tool that gives easy access to all of the capabilities of B2 Cloud Storage.

This program provides command-line access to the B2 service.

The latest documentation is available on Read the Docs.

Sections: B2 Command Line Tool, Documentation, Homebrew, Binaries, Python Package Index, Docker, Usage, Docker image, Downloading and uploading, ApiVer CLI versions (`b2` vs `b2v3`, `b2v4`, `b2v5`, etc.), Contrib, Detailed logs

</details>

### lightrag-hku

LightRAG: Simple and Fast Retrieval-Augmented Generation

`pip install lightrag-hku` · installs (wheel) · licence: MIT License · rank 9972 · last release 2026-09-02 · [PyPI](https://pypi.org/project/lightrag-hku/) · [docs](https://github.com/HKUDS/LightRAG) · [source](https://github.com/HKUDS/LightRAG)

<details><summary>README extract</summary>

- [2026.07]🎯[New Feature]: Add Smart Heading recognition feature for word documents.
- [2026.05]🎯[New Feature]: Merge RagAnything into LightRAG🎉. Multimodal content parsing and extraction via MinerU / Docling services.
- [2026.05]🎯[New Feature]: Introducing four selectable text chunking strategies: `Fix`, `Recursive`, `Vector`, and `Paragraph`. ...

Features:
- Deep Contextual Understanding: Through graph-structured indexing, LightRAG captures complex semantic dependencies between entities, overcoming the fragmented context limitations typical of traditional chunk-based retrieval methods. ...

...

</details>

### aiomoto

Moto-style AWS service mocks for aiobotocore

`pip install aiomoto` · installs (wheel) · licence: MIT · rank 9983 · last release 2026-10-30 · [PyPI](https://pypi.org/project/aiomoto/) · [source](https://github.com/owenlamont/aiomoto)

<details><summary>README extract</summary>

`aiomoto` is Moto for aiobotocore (while staying compatible with classic
botocore / boto3). It adapts Moto's stubber so async and sync clients share the same
in-memory backend: you can write to a mock S3 bucket with boto3 and read it back via
aiobotocore in the same process.

📖 Full documentation: <

Example:
```python
import boto3
from aiobotocore.session import AioSession
from aiomoto import mock_aws

async def demo() -> None:
    async with mock_aws():
        # Write with a synchronous boto3 client.
        boto3.client("s3", region_name="us-east-1").create_bucket(Bucket="example")

        # Read it back with an async aiobotocore client.
...
```

Sections: aiomoto, Usage, Motivation, Limitations

</details>

### graphql-server

A library setting up a GraphQL server in a variety of frameworks

`pip install graphql-server` · installs (wheel) · licence: MIT License · rank 9990 · last release 2025-08-17 · [PyPI](https://pypi.org/project/graphql-server/) · [source](https://github.com/graphql-python/graphql-server)

<details><summary>README extract</summary>

GraphQL-Server is a base library that serves as a helper
for building GraphQL servers or integrations into existing web frameworks using
GraphQL-Core.
* ✅ It passes all the GraphQL spec tests
* Supports 💾 `Upload`s, 🔁 Sync, 🔀 Async views and 🔄 Subscriptions through WebSockets.
* 🚀 It integrates seamlessly with all HTTP/Websocket Python servers ...

Sections: Integrations built with GraphQL-Server, Documentation, Licensing

</details>

### pylibiio

Analog Devices python interfaces for hardware with Industrial I/O drivers

`pip install pylibiio` · installs (wheel) · licence: LGPL-2.1-or-later · rank 9992 · last release 2026-10-07 · [PyPI](https://pypi.org/project/pylibiio/) · [docs](https://analogdevicesinc.github.io/libiio/) · [source](https://github.com/analogdevicesinc/libiio)

_README extract left out: share-alike licence._

### ASGIMiddlewareStaticFile

ASGI Middleware for serving Static File.

`pip install ASGIMiddlewareStaticFile` · installs (wheel) · licence: not stated · rank 9997 · last release 2025-12-18 · [PyPI](https://pypi.org/project/ASGIMiddlewareStaticFile/) · [docs](https://github.com/rexzhang/asgi-middleware-static-file/blob/main/README.md) · [source](https://github.com/rexzhang/asgi-middleware-static-file)

<details><summary>README extract</summary>

ASGI Middleware for serving static file.

Features:
> ASGIMiddlewareStaticFile is a solution when we need to distribute the whole project with static files in Docker; or
> when the deployment environment has very limited resources; or Internal network(Unable to reach CDN).

Example:
```python
static_root_paths = [ "/path/a", "path/b" ]
application = ASGIMiddlewareStaticFile(
    application,
    static_url=settings.STATIC_URL,
    static_root_paths=static_root_paths,
)
```

Sections: ASGIMiddlewareStaticFile, Why?, Features, Usage, Common, Prepare, Test with wget, Pure ASGI, Code, Start Server, Django 3.0+, Collect static file

</details>

### supermemory

The official Python library for the Supermemory API

`pip install supermemory` · installs (wheel) · licence: Apache-2.0 · rank 10012 · last release 2026-10-26 · [PyPI](https://pypi.org/project/supermemory/) · [docs](https://docs.supermemory.ai) · [source](https://github.com/supermemoryai/python-sdk)

<details><summary>README extract</summary>

The official Python library for the Supermemory v5 API, with sync and async clients built on httpx.

> Upgrading from 3.x? v5 moves to the namespace-first v5 API. See MIGRATION.md.

Example:
```python
from supermemory import Supermemory

client = Supermemory()  # reads SUPERMEMORY_API_KEY; or Supermemory(api_key="...")

client.add("user_alex", content="Alex prefers morning meetings.", id="pref-1")

response = client.search("user_alex", query="when does alex like to meet?", limit=5)
for result in response.results:
    print(result)
```

Sections: Supermemory Python SDK, Usage, Async, API surface, Filtering, Listing, File uploads, Errors, Retries, timeouts, and per-request options, Raw responses

</details>

### python-anvil

Anvil API Client

`pip install python-anvil` · installs (wheel) · licence: MIT · rank 10014 · last release 2026-10-29 · [PyPI](https://pypi.org/project/python-anvil/) · [docs](https://github.com/anvilco/python-anvil#readme) · [source](https://github.com/anvilco/python-anvil)

<details><summary>README extract</summary>

This library will allow you to interact with the Anvil API in Python.

Anvil provides easy APIs for all things paperwork.

1. PDF filling API - fill out a PDF template with a web request and structured JSON data.
2. PDF generation API - send markdown or HTML and Anvil will render it to a PDF.
3. ...

Example:
```python
from python_anvil import Anvil

# The ID of the PDF template to fill
pdf_template_id = "kA6Da9CuGqUtc6QiBDRR"
# Your API key from your Anvil organization settings
api_key = "7j2JuUWmN4fGjBxsCltWaybHOEy3UEtt"

# JSON data to fill the PDF
example_data = {
    "title": "My PDF Title",
    "fontSize": 10,
    "textColor": "#CC0000",
    "data": {
...
```

...

</details>

### webfinger

Simple Python implementation of WebFinger client protocol

`pip install webfinger` · installs from source (sdist only) · licence: BSD License · rank 10024 · last release 2013-11-02 · [PyPI](https://pypi.org/project/webfinger/)

<details><summary>README extract</summary>

A simple Python client implementation of WebFinger RFC 7033.

WebFinger is a discovery protocol that allows you to find information about people or things in a standardized way. See the spec or webfinger.net for more information.

Example:
```python
>>> from webfinger import finger
>>> wf = finger('acct:eric@konklone.com')
>>> wf.subject
acct:eric@konklone.com
>>> wf.avatar

>>> wf.profile

>>> wf.properties.get('
Eric Mill
```

Sections: webfinger, finger, WebFinger Client, WebFinger Response, Properties, Methods, Relation Properties, Unofficial Endpoints, Dependencies

</details>

### django-soft-delete

Soft delete models, managers, queryset for Django

`pip install django-soft-delete` · installs (wheel) · licence: MIT · rank 10029 · last release 2026-02-21 · [PyPI](https://pypi.org/project/django-soft-delete/)

<details><summary>README extract</summary>

This is a set of small classes to make soft deletion of objects.
Use the abstract model `SoftDeleteModel` for adding two new fields:
- `is_deleted` - is a boolean field, shows weather of a deletion state of object
- `deleted_at` - is a DateTimeField, serves a timestamp of deletion. ...

Example:
```python
# For regular model
from django.db import models
from django_softdelete.models import SoftDeleteModel

class Article(SoftDeleteModel):
    title = models.CharField(max_length=100)

    # Following fields will be added automatically
    # is_deleted
    # deleted_at

    # Following managers will be added automatically
...
```

...

</details>

### unicode-segmentation-rs

Unicode segmentation and width for Python using Rust

`pip install unicode-segmentation-rs` · installs (wheel) · licence: not stated · rank 10030 · last release 2026-10-30 · [PyPI](https://pypi.org/project/unicode-segmentation-rs/) · [docs](https://docs.weblate.org/) · [source](https://github.com/WeblateOrg/unicode-segmentation-rs)

<details><summary>README extract</summary>

Python bindings for the Rust unicode-segmentation, unicode-linebreak, and unicode-width crates, providing Unicode text segmentation and width calculation according to Unicode standards.

Maintained by Weblate — a privacy-respecting localization platform built on open-source foundations.

Features:
- Grapheme Cluster Segmentation: Split text into user-perceived characters
- Word Segmentation: Split text into words according to Unicode rules
- Sentence Segmentation: Split text into sentences ...

Example:
```python
import unicode_segmentation_rs

# Grapheme clusters (user-perceived characters)
text = "Hello 👨‍👩‍👧‍👦 World"
clusters = unicode_segmentation_rs.graphemes(text, is_extended=True)
print(
    clusters
)  # ['H', 'e', 'l', 'l', 'o', ' ', '👨‍👩‍👧‍👦', ' ', 'W', 'o', 'r', 'l', 'd']

...

</details>

### pyzotero

Python wrapper for the Zotero API

`pip install pyzotero` · installs (wheel) · licence: BlueOak-1.0.0 · rank 10044 · last release 2026-10-13 · [PyPI](https://pypi.org/project/pyzotero/) · [docs](https://pyzotero.readthedocs.org) · [source](https://github.com/urschrei/pyzotero)

<details><summary>README extract</summary>

Example:
```python
from pyzotero import Zotero

zot = Zotero(
    library_id, library_type, api_key
)  # local=True to use a running Zotero instead of the web API
items = zot.top(limit=5)
# we've retrieved the latest five top-level items in our library
# we can print each item's item type and ID
for item in items:
    print(f"Item: {item'data'} | Key: {item'data'}")
```

Sections: Pyzotero: An API Client for the Zotero API, Quickstart, Documentation, Local Zotero API, Command-Line Interface, MCP Server, Issues, Pull Requests, Versioning

</details>

### flake8-rst-docstrings

Python docstring reStructuredText (RST) validator for flake8

`pip install flake8-rst-docstrings` · installs (wheel) · licence: MIT License · rank 10045 · last release 2025-10-06 · [PyPI](https://pypi.org/project/flake8-rst-docstrings/) · [docs](https://github.com/peterjc/flake8-rst-docstrings/blob/master/README.rst) · [source](https://github.com/peterjc/flake8-rst-docstrings/)

<details><summary>README extract</summary>

This is an MIT licensed flake8 plugin for validating Python docstrings markup
as reStructuredText (RST) using the Python library `docutils`. It is
available to install from the Python Package Index (PyPI).

This is based heavily off `pydocstyle` (which is also MIT licensed), which
has a flake8 plugin called `flake8-docstrings`, see: ...

Sections: flake8-rst-docstrings, Introduction, Flake8 Validation codes, Configuration

</details>

### connection_pool

thread safe connection pool

`pip install connection_pool` · installs from source (sdist only) · licence: MIT License · rank 10052 · last release 2020-09-17 · [PyPI](https://pypi.org/project/connection_pool/)

<details><summary>README extract</summary>

Thread-safe connection pool for python

Example:
```python
import memcache
from connection_pool import ConnectionPool

# via create function
def create_memcache_client():
    return memcache.Client(['127.0.0.1:11211'])

pool = ConnectionPool(create=create_memcache_client,
                      max_size=10, max_usage=10000, idle=60, ttl=120)

# via lambda
...
```

Sections: ConnectionPool, Examples, Create a pool

</details>

### flake8-no-implicit-concat

Flake8 plugin that forbids implicit str/bytes literal concatenations

`pip install flake8-no-implicit-concat` · installs (wheel) · licence: MIT License · rank 10057 · last release 2024-11-05 · [PyPI](https://pypi.org/project/flake8-no-implicit-concat/)

<details><summary>README extract</summary>

Flake8 plugin that forbids implicit str/bytes literal concatenations.

 # Not Allowed
 print('foo' 'bar', 'baz')
 a = ["aaa",
 "bbb"
 "ccc"]
 b = b'abc' b'def'

 # OK
 print('foobar', 'baz')
 a = ["aaa",
 "bbb"
 + "ccc"]
 b = b'abcdef'

Installation

Install via pip:

 pip install flake8-no-implicit-concat

Violation Codes ...

</details>

### zope.testing

Zope testing helpers

`pip install zope.testing` · installs (wheel) · licence: ZPL-2.1 · rank 10059 · last release 2026-07-03 · [PyPI](https://pypi.org/project/zope.testing/) · [source](https://github.com/zopefoundation/zope.testing)

<details><summary>README extract</summary>

Features:
- Add support for Python 3.11.

Example:
```python
  class MYTests(unittest.TestCase):
      ...
      test_foo = doctestcase.doctestfile('foo.txt')

You can use::

  @doctestcase.doctestfiles('foo.txt', 'bar.txt', ...)
  class MYTests(unittest.TestCase):
      ...
```

Sections: Changes, 6.2 (2026-07-03), 6.1 (2025-12-17), 6.0 (2025-09-12), 5.1 (2025-02-14), 5.0.1 (2022-12-20), 5.0 (2022-12-20), Backwards incompatible changes, Features, 4.10 (2022-03-07), 4.9 (2021-01-08), 4.8 (2021-01-04), 4.7 (2018-10-04), 4.6.2 (2017-06-12)

</details>

### lark-js

An extension to Lark that generates a Javascript standalone

`pip install lark-js` · installs (wheel) · licence: MIT License · rank 10081 · last release 2022-05-16 · [PyPI](https://pypi.org/project/lark-js/) · [docs](https://lark.readthedocs.io/en/latest/) · [source](https://github.com/lark-parser/lark.js)

<details><summary>README extract</summary>

Generate LALR(1) parsers in Javascript

Lark is a popular parsing toolkit for Python.

This project is a live port of the Lark standalone parser to Javascript.

Lark.js takes a `.lark` grammar, and from it generates a standalone Javascript parser. ...

Features:
- LALR(1) parser - Fast and light
 - EBNF grammar
 - Builds a parse-tree (AST) automagically, based on the structure of the grammar
 - Usable in the browser and in Node.js
 - Interactive parsing (step-by-step)
 - Error handling
 - Tree utilities ...

Sections: Lark.js, Lark grammars, "Hello World" Grammar, Quick links, Generate a Javascript LALR(1) parser, Features, Syntax Highlighting, Live Port

</details>

### mozrunner

Reliable start/stop/configuration of Mozilla Applications (Firefox, Thunderbird, etc.)

`pip install mozrunner` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 10089 · last release 2026-03-26 · [PyPI](https://pypi.org/project/mozrunner/)

### QDarkStyle

The most complete dark/light style sheet for C++/Python and Qt applications

`pip install QDarkStyle` · installs (wheel) · licence: MIT License · rank 10090 · last release 2023-11-28 · [PyPI](https://pypi.org/project/QDarkStyle/) · [docs](https://qdarkstylesheet.readthedocs.io/en/stable)

<details><summary>README extract</summary>

The most complete dark/light style sheet for Qt applications (Qt4, Qt5,
PySide, PySide2, PyQt4, PySide6, PyQt5, PyQt6, QtPy, PyQtGraph, Qt.Py) for
Python 2/3 and C++.

Python 2, as well as Qt4 (PyQt4 and PySide), will not be supported anymore.
They are still there as it is, but no back-compatibility, fixes, nor features
will be implemented. ...

Example:
```python
import qdarkstyle
```

</details>

### aes-pkcs5

Implementation of AES with CBC/ECB mode and padding scheme PKCS5

`pip install aes-pkcs5` · installs (wheel) · licence: BSD-2-Clause · rank 10095 · last release 2025-04-26 · [PyPI](https://pypi.org/project/aes-pkcs5/) · [docs](https://aes-pkcs5.readthedocs.io) · [source](https://github.com/Laerte/aes_pkcs5)

<details><summary>README extract</summary>

Python implementation of AES with CBC/ECB mode and padding scheme PKCS5.

* Python 3.9+

Sections: AESPKCS5, Requirements, Documentation

</details>

### aws-sso-lib

Library to make AWS SSO easier

`pip install aws-sso-lib` · installs (wheel) · licence: Apache Software License · rank 10107 · last release 2023-01-27 · [PyPI](https://pypi.org/project/aws-sso-lib/) · [source](https://github.com/benkehoe/aws-sso-util)

<details><summary>README extract</summary>

`aws-sso-lib` allows you to programmatically interact with AWS IAM Identity Center (formerly AWS SSO).

The primary functions that will be of interest are available at the package level:
* `get_boto3_session`: Get a boto3 session for a specific account and role. ...

Example:
```python
get_boto3_session(start_url, sso_region, account_id, role_name, *, region,
    login=False,
    sso_cache=None,
    credential_cache=None)
```

Sections: `aws-sso-lib`, `get_boto3_session`, `login`, `list_available_accounts` and `list_available_roles`, `list_assignments`

</details>

### robocorp-tasks

The automation framework for Python

`pip install robocorp-tasks` · installs (wheel) · licence: Apache Software License · rank 10126 · last release 2026-03-13 · [PyPI](https://pypi.org/project/robocorp-tasks/) · [source](https://github.com/robocorp/robocorp/)

<details><summary>README extract</summary>

`robocorp-tasks` is a Python framework designed to simplify the development of Python automations.

Features:
While Python is widely used in the automation world, many solutions end up being ad-hoc, making it difficult to navigate different projects and keep up with the features required for analysing the results of such automations afterwards.

Example:
```python
from robocorp.tasks import task

@task
def my_task():
    ...
```

Sections: robocorp-tasks, Why, How, Getting started, Guides, API Reference

</details>

### version-utils

Library for parsing system package strings and comparing package versions

`pip install version-utils` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 10139 · last release 2022-05-06 · [PyPI](https://pypi.org/project/version-utils/)

_README extract left out: share-alike licence._

### pkg-about

Unified access to Python package metadata at runtime.

`pip install pkg-about` · installs (wheel) · licence: Zlib · rank 10160 · last release 2026-10-16 · [PyPI](https://pypi.org/project/pkg-about/) · [docs](https://karpierz.github.io/pkg_about/) · [source](https://github.com/karpierz/pkg_about)

<details><summary>README extract</summary>

Unified access to Python package metadata at runtime.

Features:
Provides a unified way to retrieve Python package metadata at runtime,
regardless of the build backend or project structure.

| about(package: str) - retrieves metadata for the given package
| about() - retrieves metadata for the current package
| ...

Example:
```python
>>> import pkg_about
>>> pkg_about.about("pip")
>>> uri == "
True
```

Sections: pkg_about, Overview, Usage

</details>

### vineyard

An in-memory immutable data manager

`pip install vineyard` · does not install on CPython 3.14 · licence: Apache Software License · rank 10163 · last release 2024-08-29 · [PyPI](https://pypi.org/project/vineyard/) · [docs](https://v6d.io) · [source](https://github.com/v6d-io/v6d)

<details><summary>README extract</summary>

|crates.ioDocker HUBArtifact HUBACM DL|

Vineyard (v6d) is an innovative in-memory immutable data manager that offers **out-of-the-box
high-level abstractions and zero-copy in-memory** sharing for distributed data in various
big data tasks, such as graph analytics (e.g., GraphScope), numerical computing
(e.g., Mars), and machine learning. ...

Sections: vineyard: an in-memory immutable data manager, What is vineyard, Features, Efficient In-Memory Immutable Data Sharing, Out-of-the-Box High-Level Data Abstractions, Stream Pipelining for Enhanced Performance, Versatile Drivers for Common Tasks, Try Vineyard, Deploying on Kubernetes, FAQ, Get Involved, Publications

</details>

### maya

Datetimes for Humans.

`pip install maya` · installs (wheel) · licence: MIT License · rank 10167 · last release 2019-01-06 · [PyPI](https://pypi.org/project/maya/)

<details><summary>README extract</summary>

Datetimes are very frustrating to work with in Python, especially when dealing
with different locales on different systems. This library exists to make the
simple things much easier, while admitting that time is an illusion
(timezones doubly so).

Datetimes should be interacted with via an API written for humans. ...

Example:
```python
>>> now = maya.now()
<MayaDT epoch=1481850660.9>

>>> tomorrow = maya.when('tomorrow')
<MayaDT epoch=1481919067.23>

>>> tomorrow.slang_date()
'tomorrow'

>>> tomorrow.slang_time()
'23 hours from now'

# Also: MayaDT.from_iso8601(...)
>>> tomorrow.iso8601()
'2017-02-10T22:17:01.445418Z'

# Also: MayaDT.from_rfc2822(...)
>>> tomorrow.rfc2822()
...
```

...

</details>

### pynput-robocorp-fork

Monitor and control user input devices

`pip install pynput-robocorp-fork` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 10170 · last release 2022-12-29 · [PyPI](https://pypi.org/project/pynput-robocorp-fork/)

_README extract left out: share-alike licence._

### flask-swagger

Extract swagger specs from your flask project

`pip install flask-swagger` · installs from source (sdist only) · licence: MIT · rank 10181 · last release 2019-03-26 · [PyPI](https://pypi.org/project/flask-swagger/)

<details><summary>README extract</summary>

A Swagger 2.0 spec extractor for Flask

Install:

Flask-swagger provides a method (swagger) that inspects the Flask app
for endpoints that contain YAML docstrings with Swagger 2.0
Operation
objects.

Flask-swagger supports docstrings in methods of MethodView classes and
regular Flask view functions. ...

Example:
```python
class UserAPI(MethodView):

    def post(self):
        """
        Create a new user

        tags:
          - users
        definitions:

              id: Group
              properties:
                name:
                 type: string
                 description: the group's name
        parameters:
          - in: body
...
```

</details>

### linkpreview

Get link (URL) preview

`pip install linkpreview` · installs (wheel) · licence: MIT License · rank 10186 · last release 2026-10-14 · [PyPI](https://pypi.org/project/linkpreview/)

<details><summary>README extract</summary>

Get link preview in python

Gathering data from:

1. OpenGraph meta tags
2. TwitterCard meta tags
3. Microdata meta tags
4. JSON-LD meta tags
5. HTML Generic tags (`h1`, `p`, `img`)
6. URL readable parts

Example:
```python
from linkpreview import link_preview

url = "
content = """
<!DOCTYPE html>

    a title

"""
preview = link_preview(url, content)
print("title:", preview.title)
print("description:", preview.description)
print("image:", preview.image)
print("force_title:", preview.force_title)
print("absolute_image:", preview.absolute_image)
...
```

Sections: linkpreview, Usage, Basic, Automatic fetch link content, `lxml` as XML parser, Advanced

</details>

### flake8-literal

Flake8 string literal validation

`pip install flake8-literal` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 10190 · last release 2025-06-28 · [PyPI](https://pypi.org/project/flake8-literal/)

_README extract left out: share-alike licence._

### objectgraph

A basic graph library

`pip install objectgraph` · installs (wheel) · licence: MIT License · rank 10199 · last release 2025-11-21 · [PyPI](https://pypi.org/project/objectgraph/) · [docs](https://objectgraph.readthedocs.io/) · [source](https://github.com/ronaldoussoren/objectgraph/)

<details><summary>README extract</summary>

Objectgraph is a library that provides a class representing
basic graphs with nodes and edges between nodes.

Nodes can be arbitrary objects with an "identifier" attribute
(which should be hashable). Edges can have arbitrary attributes. ...

</details>

### django-templated-email

A Django oriented templated / transaction email abstraction

`pip install django-templated-email` · installs (wheel) · licence: MIT License · rank 10202 · last release 2025-08-21 · [PyPI](https://pypi.org/project/django-templated-email/)

<details><summary>README extract</summary>

:Info: A Django oriented templated email sending class
:Original Author: Bradley Whittington (
:Maintained by: Vinta Software:
:Tests:

Features:
django-templated-email is oriented towards sending templated emails.
The library supports template inheritance, adding cc'd and bcc'd recipients,
configurable template naming and location. ...

Example:
```python
from templated_email import send_templated_mail
send_templated_mail(
        template_name='welcome',
        from_email='from@example.com',
        recipient_list=['to@example.com'],
        context={
            'username':request.user.username,
            'full_name':request.user.get_full_name(),
...
```

...

</details>

### fastapi-injectable

Use FastAPI's Depends() anywhere — in CLI tools, Celery tasks, background workers, and more. No refactoring needed.

`pip install fastapi-injectable` · installs (wheel) · licence: MIT · rank 10207 · last release 2026-10-28 · [PyPI](https://pypi.org/project/fastapi-injectable/) · [docs](https://fastapi-injectable.readthedocs.io) · [source](https://github.com/JasperSui/fastapi-injectable)

<details><summary>README extract</summary>

Use FastAPI's Depends() anywhere — in CLI tools, background workers, scheduled jobs, and more.

 Stop rewriting your dependency logic. Start reusing it.

Installation: `pip install fastapi-injectable` ...

Features:
If you use FastAPI, you've built your app around `Depends()`. But the moment you need those same dependencies in a CLI command, background worker, Celery task, or scheduled job — you're stuck. You end up: ...

Example:
```python
from typing import Annotated

from fastapi import Depends
from fastapi_injectable import injectable

class Database:
    def query(self) -> str:
        return "data"

def get_db() -> Database:
    return Database()

@injectable
def process_data(db: Annotated[Database, Depends(get_db)]) -> str:
    return db.query()

# Use it anywhere!
...
```

...

</details>

### threaded

Decorators for running functions in Thread/ThreadPool/IOLoop

`pip install threaded` · installs (wheel) · licence: Apache Software License · rank 10220 · last release 2023-11-22 · [PyPI](https://pypi.org/project/threaded/) · [docs](https://threaded.readthedocs.io/) · [source](https://github.com/python-useful-helpers/threaded)

<details><summary>README extract</summary>

threaded is a set of decorators, which wrap functions in:

 * `concurrent.futures.ThreadPool`
 * `threading.Thread`
 * `asyncio.Task` in Python 3.

Why? Because copy-paste of `loop.create_task`, `threading.Thread` and `thread_pool.submit` is boring,
especially if target functions is used by this way only.

Pros:

* Free software: Apache license ...

Example:
```python
threaded.ThreadPooled.configure(max_workers=3)
```

Sections: threaded, Usage, ThreadPooled, Threaded, AsyncIOTask, CI systems, CD system

</details>

### django-map-widgets

Configurable and user-friendly map widgets for GeoDjango fields

`pip install django-map-widgets` · installs (wheel) · licence: MIT License · rank 10221 · last release 2026-07-19 · [PyPI](https://pypi.org/project/django-map-widgets/) · [docs](https://django-map-widgets.readthedocs.io/) · [source](https://github.com/erdem/django-map-widgets)

<details><summary>README extract</summary>

Django Map Widgets is a package that provides highly configurable, pluggable, and user-friendly map widgets for
GeoDjango form fields. It simplifies the integration of interactive maps into GeoDjango applications, enhancing the
overall development experience. ...

Example:
```python
from django.contrib.gis.db import models
import mapwidgets

class CityAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": mapwidgets.GoogleMapPointFieldWidget}
    }
```

Sections: Django Map Widgets, Usage, Settings, JQuery Requirement, Screenshots, MapBox Interactive Point Field Widget, MapBox Static Point Field Widget, Leaflet Interactive Point Field Widget, Leaflet Interactive Polygon Field Widget, GoogleMap Interactive Point Field Widget

</details>

### mkl-static

Intel® oneAPI Math Kernel Library

`pip install mkl-static` · installs (wheel) · licence: Other/Proprietary License · rank 10228 · last release 2026-10-16 · [PyPI](https://pypi.org/project/mkl-static/)

<details><summary>README extract</summary>

Intel® oneAPI Math Kernel Library (Intel® oneMKL) is a computing math library of highly optimized, extensively threaded routines for applications that require maximum performance. This package provides C and Data Parallel C++ (DPC++) programming language interfaces. ...

</details>

### micawber

a small library for extracting rich content from urls

`pip install micawber` · installs (wheel) · licence: not stated · rank 10230 · last release 2026-09-03 · [PyPI](https://pypi.org/project/micawber/) · [docs](https://micawber.readthedocs.io/) · [source](https://github.com/coleifer/micawber)

<details><summary>README extract</summary>

A small library for extracting rich content from urls.

micawber supplies a few methods for retrieving rich metadata about a variety of
links, such as links to youtube videos. micawber also provides functions for
parsing blocks of text and html and replacing links to videos with rich embedded
content.

Example:
```python
import micawber

# load up rules for some default providers, such as youtube and flickr
providers = micawber.bootstrap_basic()

providers.request(' maxwidth=640)

# returns the following dictionary:
{
    'author_name': 'Pascal Brax',
    'author_url': '
    'height': 480,
    'html': '',
    'provider_name': 'YouTube',
    'provider_url': '
...
```

Sections: what does it do?, examples

</details>

### pyadi-iio

Analog Devices python interfaces for hardware with Industrial I/O drivers

`pip install pyadi-iio` · installs (wheel) · licence: ADI BSD · rank 10233 · last release 2026-05-26 · [PyPI](https://pypi.org/project/pyadi-iio/) · [docs](https://analogdevicesinc.github.io/pyadi-iio/) · [source](https://github.com/analogdevicesinc/pyadi-iio)

<details><summary>README extract</summary>

pyadi-iio is a python abstraction module for ADI hardware with IIO drivers to make them easier to use. The libIIO interface although extremely flexible can be cumbersome to use due to the amount of boilerplate code required for even simple examples, especially when interfacing with buffers. ...

Example:
```python
import adi

# Create device from specific uri address
sdr = adi.ad9361(uri="ip:192.168.2.1")
# Get data from transceiver
data = sdr.rx()
```

Sections: Dependencies, Building doc

</details>

### pyobjc-framework-CoreLocation

Wrappers for the framework CoreLocation on macOS

`pip install pyobjc-framework-CoreLocation` · installs from source (sdist only) · licence: MIT · rank 10241 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreLocation/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for framework 'CoreLocation' on macOS 10.6. This framework provides
an interface for dealing with the physical location of a machine, which allows
for geo-aware applications. ...

</details>

### aws-kinesis-agg

Python module to assist in taking advantage of the Kinesis message aggregation format for both aggregation and deaggregation.

`pip install aws-kinesis-agg` · installs (wheel) · licence: Apache Software License · rank 10243 · last release 2022-06-10 · [PyPI](https://pypi.org/project/aws-kinesis-agg/)

<details><summary>README extract</summary>

The Kinesis Aggregation/Deaggregation Modules for Python provide the ability to do in-memory aggregation and deaggregation of standard Kinesis user records using the Kinesis Aggregated Record Format to allow for more efficient transmission of records.

Example:
```python
import boto3
import aws_kinesis_agg.aggregator

kinesis_client = None

def send_record(agg_record):
    global kinesis_client
    pk, ehk, data = agg_record.get_contents()
    kinesis_client.put_record(StreamName='MyKinesisStreamName',
                                  Data=data,
                                  PartitionKey=pk,
...
```

...

</details>

### prefect-azure

Prefect integrations with Microsoft Azure services

`pip install prefect-azure` · installs (wheel) · licence: Apache Software License · rank 10245 · last release 2026-09-08 · [PyPI](https://pypi.org/project/prefect-azure/)

<details><summary>README extract</summary>

`prefect-azure` is a collection of Prefect integrations for orchestration workflows with Azure.

Example:
```python
from prefect import flow

from prefect_azure import AzureBlobStorageCredentials
from prefect_azure.blob_storage import blob_storage_download

@flow
def example_blob_storage_download_flow():
    connection_string = "connection_string"
    blob_storage_credentials = AzureBlobStorageCredentials(
        connection_string=connection_string,
    )
...
```

Sections: prefect-azure, Getting Started, Examples, Download a blob, Azure Container Instance Worker

</details>

### pyobjc-framework-Contacts

Wrappers for the framework Contacts on macOS

`pip install pyobjc-framework-Contacts` · installs from source (sdist only) · licence: MIT · rank 10261 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Contacts/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Contacts" framework on macOS 10.11.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### flake8-import-rules

(no summary)

`pip install flake8-import-rules` · installs (wheel) · licence: MIT License · rank 10264 · last release 2023-04-24 · [PyPI](https://pypi.org/project/flake8-import-rules/)

<details><summary>README extract</summary>

Helps to prevent import of certain modules from certain modules.

It's useful if you have many modules in your project and want to keep them kind of
isolated.

After installing just add `import-rules` option to your `setup.cfg` file.

Rules are checking top-down. The Order Matters. ...

Example:
```python
[flake8]
...
import-rules=
    # yaml format here
    - module_one: [
        module_two allow,
        any deny
    ]
    - module_two: [
        module_one.sub.submodule deny
    ]
    - module_two.sumbodule: module_one deny
    - module_three: any allow

    # many section for the same module are allowed
    # for example
    - module_two: [
...
```

</details>

### sqlalchemy-celery-beat

A Scheduler Based SQLalchemy For Celery

`pip install sqlalchemy-celery-beat` · installs (wheel) · licence: MIT License · rank 10282 · last release 2026-10-06 · [PyPI](https://pypi.org/project/sqlalchemy-celery-beat/)

<details><summary>README extract</summary>

A Scheduler Based Sqlalchemy for Celery.

> NOTE: This project was originally developed by AngelLiang to use sqlalchemy as the database scheduler for Flask or FastAPI, like django-celery-beat for django. I am trying to continue on his work and maintain a working solution.

- Python 3
- celery >= 5.0
- sqlalchemy >= 1.4 ...

Example:
```python
>>> from sqlalchemy_celery_beat.models import PeriodicTask, IntervalSchedule, Period
>>> from sqlalchemy_celery_beat.session import SessionManager
>>> from celeryconfig import beat_dburi
>>> session_manager = SessionManager()
>>> session = session_manager.session_factory(beat_dburi)

# executes every 10 seconds.
...
```

...

</details>

### python-hmac-auth

Python client for jersey-hmac-auth (https://github.com/bazaarvoice/jersey-hmac-auth)

`pip install python-hmac-auth` · installs (wheel) · licence: Apache Software License · rank 10297 · last release 2014-08-22 · [PyPI](https://pypi.org/project/python-hmac-auth/)

<details><summary>README extract</summary>

HMAC authentication for Python client libraries.

This library makes it easy to add support for HMAC authentication in Python clients that:

1. Interface with a REST API that uses
jersey-hmac-auth to implement HMAC authentication, and
2. Use the Python Requests library to make API calls. ...

Example:
```python
import requests
from python_hmac_auth import HmacAuth

response = requests.get(' auth=HmacAuth('your_api_key', 'your_secret_key'))
```

Sections: python-hmac-auth, Getting Started, User Guide

</details>

### workdays

Workday date utility functions to extend python's datetime

`pip install workdays` · installs from source (sdist only) · licence: BSD License · rank 10299 · last release 2014-08-26 · [PyPI](https://pypi.org/project/workdays/)

<details><summary>README extract</summary>

Extend python datetime with excel-like workday addition/subtraction
 functionality:

 NETWORKDAYS(start_date,end_date,holidays)

 Returns the number of whole working days between start_date and
 end_date (inclusive of both start_date and end_date). Working days
 exclude weekends and any dates identified in holidays. ...

</details>

### streamlit-image-coordinates

Streamlit component that displays an image and returns the coordinates when you click on it

`pip install streamlit-image-coordinates` · installs (wheel) · licence: MIT License · rank 10311 · last release 2026-08-14 · [PyPI](https://pypi.org/project/streamlit-image-coordinates/)

<details><summary>README extract</summary>

Author: @blackary

Code:

Streamlit component that displays an image and returns the coordinates when you click on it.
Also returns click event time in unix format.

Example:
```python
import streamlit as st

from streamlit_image_coordinates import streamlit_image_coordinates

value = streamlit_image_coordinates("

st.write(value)
```

Sections: Streamlit-Image-Coordinates, Usage instructions

</details>

### mdformat_myst

Mdformat plugin for MyST compatibility.

`pip install mdformat_myst` · installs (wheel) · licence: MIT License · rank 10316 · last release 2025-11-27 · [PyPI](https://pypi.org/project/mdformat_myst/)

<details><summary>README extract</summary>

[][ci-link]
[][codecov-link]
[][pypi-link]

> Mdformat plugin for MyST compatibility

Mdformat is a formatter for
CommonMark
compliant Markdown.

Mdformat-myst is an mdformat plugin that changes the target specification to
MyST,
making the tool able to format the following syntax extensions:

- tables
- directives
- roles ...

Sections: mdformat-myst, Description, Usage

</details>

### ai-api-client-sdk

[DEPRECATED] AI API Client SDK

`pip install ai-api-client-sdk` · installs (wheel) · licence: Other/Proprietary License · rank 10317 · last release 2025-05-14 · [PyPI](https://pypi.org/project/ai-api-client-sdk/)

<details><summary>README extract</summary>

This package is no longer maintained.

Please use sap-ai-sdk-base instead.

The AI API client SDK is a Python-based SDK that enables you to access the AI API using Python methods and data structures. You can use the Client SDK to test AI API.

The client SDK can be used with any implementation of AI API. ...

Example:
```python
from ai_api_client_sdk.ai_api_v2_client import AIAPIV2Client

# Instantiate the client
client = AIAPIV2Client(base_url=AI_API_URL,
    auth_url=AUTH_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET, resource_group=RESOURCE_GROUP)

# Make some queries, e.g.
scenarios = client.scenario.query()

for scenario in scenarios.resources:
...
```

Sections: [DEPRECATED] SAP AI API Client SDK, Example Usage

</details>

### ASGIWebDAV

An asynchronous WebDAV server implementation, support multi-provider.

`pip install ASGIWebDAV` · installs (wheel) · licence: not stated · rank 10325 · last release 2026-11-04 · [PyPI](https://pypi.org/project/ASGIWebDAV/) · [docs](https://rexzhang.github.io/asgi-webdav/) · [source](https://github.com/rexzhang/asgi-webdav)

<details><summary>README extract</summary>

An asynchronous WebDAV server implementation, Support multi-provider, multi-account and permission control.

Features:
- ASGI standard
- WebDAV standard: RFC4918
- Support multi-provider: FileSystemProvider, MemoryProvider, WebHDFSProvider
- Support multi-account and permission control
- Support optional anonymous user
- Support optional home directory ...

Sections: ASGI WebDAV Server, Features, Quickstart, Default Account, View in Browser, Documentation, Related Projects

</details>

### pybaseball

Retrieve baseball data in Python

`pip install pybaseball` · installs (wheel) · licence: MIT License · rank 10327 · last release 2023-09-08 · [PyPI](https://pypi.org/project/pybaseball/)

<details><summary>README extract</summary>

Baseball data scraping and analysis tools in python

Features:
`pybaseball` is a Python package for baseball data analysis. This package scrapes Baseball Reference, Baseball Savant, and FanGraphs so you don't have to. ...

Example:
```python
>>> from pybaseball import statcast
>>> statcast(start_dt="2019-06-24", end_dt="2019-06-25").columns
Index(['pitch_type', 'game_date', 'release_speed', 'release_pos_x',
       'release_pos_z', 'player_name', 'batter', 'pitcher', 'events',
       'description', 'spin_dir', 'spin_rate_deprecated',
...
```

Sections: pybaseball, Overview, Documentation, Player-Specific Queries, A note on Statcast data, Aggregate Statistics, Game-by-Game Results and Schedule, Caching, FAQ, Stale Cache, Multiprocessing, Credit

</details>

### waiter

Delayed iteration for polling and retries.

`pip install waiter` · installs (wheel) · licence: Apache-2.0 · rank 10337 · last release 2026-07-26 · [PyPI](https://pypi.org/project/waiter/) · [docs](https://coady.github.io/waiter)

<details><summary>README extract</summary>

Does Python need yet another retry / poll library? It needs at least one that isn't coupled to decorators and functions. Decorators prevent the caller from customizing delay options, and organizing the code around functions hinders any custom handling of failures. ...

Example:
```python
from waiter import wait

wait(1)  # 1, 1, 1, 1, ...
wait([1] * 3)  # 1, 1, 1
wait([0.5, 0.5, 60])  # circuit breaker
```

Sections: Usage, creation, iteration, functions, async, statistics, Tests

</details>

### deprecat

Python @deprecat decorator to deprecate old python classes, functions or methods.

`pip install deprecat` · installs (wheel) · licence: MIT License · rank 10339 · last release 2024-07-24 · [PyPI](https://pypi.org/project/deprecat/)

### standard-distutils

Standard library distutils redistribution. "dead battery".

`pip install standard-distutils` · installs (wheel) · licence: Python Software Foundation License · rank 10342 · last release 2024-10-30 · [PyPI](https://pypi.org/project/standard-distutils/)

<details><summary>README extract</summary>

Python is moving forward! Python finally started to remove dead batteries.
For more information, see PEP 594.

If your project depends on a module that has been removed from the standard,
here is the redistribution of the dead batteries.

</details>

### pyobjc-framework-SystemConfiguration

Wrappers for the framework SystemConfiguration on macOS

`pip install pyobjc-framework-SystemConfiguration` · installs from source (sdist only) · licence: MIT · rank 10353 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SystemConfiguration/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for framework 'SystemConfiguration'.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pysequoia

Provides OpenPGP facilities using Sequoia-PGP library

`pip install pysequoia` · installs (wheel) · licence: Apache-2.0 · rank 10358 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pysequoia/) · [source](https://github.com/wiktor-k/pysequoia)

<details><summary>README extract</summary>

This library provides OpenPGP facilities in Python through the
Sequoia PGP library. If you need to work with encryption and
digital signatures using an IETF standardized protocol, this
package is for you!

Note: This is a work in progress. The API is not stable!

Example:
```python
from pysequoia import Cert, Sig, Tsk
```

Sections: PySequoia, Building, Functions, sign, sign_file, verify, encrypt, encrypt_file, decrypt, decrypt_file, Certificates, Parsing, generate, Cipher suites

</details>

### ai-core-sdk

[DEPRECATED] SAP AI Core SDK

`pip install ai-core-sdk` · installs (wheel) · licence: Other/Proprietary License · rank 10361 · last release 2025-05-14 · [PyPI](https://pypi.org/project/ai-core-sdk/)

<details><summary>README extract</summary>

This package is no longer maintained.

Please use sap-ai-sdk-core instead.

**Note: This is the last version supporting AICore Content Packages.
This capability will be removed in _sap-ai-sdk-core.**

The SAP AI Core SDK is a Python-based SDK that lets you access SAP AI Core using Python methods and data structures. ...

Example:
```python
from ai_core_sdk.ai_core_v2_client import AICoreV2Client
```

Sections: [DEPRECATED] SAP AI Core SDK, Example Usage, Import Definitions, Create Client, Create New Resource Group, Create Object Store Secret, List Scenarios, Client Configuration, AICore Content Packages, Discover Content Packages and their Content, User's workflow configuration, Create Docker images, Create AI Core Templates, Create Execution Templates

</details>

### django-fsm-log

Transition's persistence for django-fsm

`pip install django-fsm-log` · installs (wheel) · licence: MIT · rank 10367 · last release 2026-01-27 · [PyPI](https://pypi.org/project/django-fsm-log/) · [docs](https://django-fsm-log.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Provides persistence of the transitions of your fsm's models. Backed by the excellent Django FSM
package.

Logs can be accessed before a transition occurs and before they are persisted to the database
by enabling a cached backend. See Advanced Usage

Example:
```python
from django_fsm_log.models import StateLog
StateLog.objects.all()
# ...all recorded logs...
```

Sections: Django Finite State Machine Log, 5.0.2 ( 2026-01-27 ), 5.0.1 ( :x: ), 5.0.0 ( :x: ), 4.0.5 ( :x: ), 4.0.4 ( :x: ), 4.0.3 ( :x: ), 4.0.2 ( :x: ), 4.0.1 (2025-01-07), 4.0.0 (2025-01-07), 3.1.0 (2023-03-23), 3.0.0 (2022-01-14), 2.0.1 (2020-03-26), 1.6.2 (2019-01-06)

</details>

### pypi-json

PyPI JSON API client library

`pip install pypi-json` · installs (wheel) · licence: MIT License · rank 10374 · last release 2026-02-19 · [PyPI](https://pypi.org/project/pypi-json/) · [docs](https://pypi-json.readthedocs.io/en/latest) · [source](https://github.com/repo-helper/pypi-json)

### llist

Linked list data structures for Python

`pip install llist` · installs from source (sdist only) · licence: MIT License · rank 10383 · last release 2021-04-26 · [PyPI](https://pypi.org/project/llist/)

<details><summary>README extract</summary>

llist is an extension module for CPython providing basic linked list
data structures.
Collections implemented in the llist module perform well in problems
which rely on fast insertions and/or deletions of elements in
the middle of a sequence. ...

</details>

### python-libmaas

A client API library specially for MAAS.

`pip install python-libmaas` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 10387 · last release 2022-08-17 · [PyPI](https://pypi.org/project/python-libmaas/)

_README extract left out: share-alike licence._

### intel-opencl-rt

Intel® oneAPI OpenCL* Runtime

`pip install intel-opencl-rt` · installs (wheel) · licence: Other/Proprietary License · rank 10414 · last release 2026-10-16 · [PyPI](https://pypi.org/project/intel-opencl-rt/)

<details><summary>README extract</summary>

This COMPILER-SPECIFIC Intel® oneAPI OpenCL* Runtime package contains the compiler-specific shared libraries needed to deploy executables to hosts without the Intel® oneAPI development Toolkits. In addition to this package you will need both the COMMON LIBRARIES and COMMON LICENSING packages.

</details>

### flake8-mutable

mutable defaults flake8 extension

`pip install flake8-mutable` · installs from source (sdist only) · licence: MIT License · rank 10421 · last release 2017-04-24 · [PyPI](https://pypi.org/project/flake8-mutable/)

<details><summary>README extract</summary>

flake8-mutable

Python's default arguments are evaluated at definition as opposed to when the function is invoked. This leads to unexpected behavior, as mutations persist between calls. For a more detailed explanation, see The Hitchhiker's Guide to Python.

Example:
```python
def fnc(a, b={}):
    pass

foo.py:2:14: M511 - mutable default arg of type Dict
```

Sections: Motivation, Example, Changes, [1.1.0] 2016-11-26, [1.0.6] 2016-11-26

</details>

### typecats

Structure unstructured data for the purpose of static type checking

`pip install typecats` · installs (wheel) · licence: MIT · rank 10437 · last release 2026-04-24 · [PyPI](https://pypi.org/project/typecats/) · [source](https://github.com/xoeye/typecats)

<details><summary>README extract</summary>

Structure unstructured data for the purpose of static type
checking. An opinionated wrapper for `attrs` and `cattrs`.

In many web services it is common to consume or generate JSON or some
JSON-like representation of data. JSON translates quite nicely to core
Python objects such as dicts and lists. ...

Features:
1. ### Built-in `struc` and `unstruc`.

 Static class function `struc` and object method `unstruc` added to
 every class type defined as a Cat, which pass directly through to
 their underlying `structure` and `unstructure` implementations in ...

Example:
```python
@Cat
class TestCat:
   name: str
   age: int

try:
   TestCat.struc(dict(name='Tom', age=9)) == TestCat(name='Tom', age=9)

   TestCat.struc(dict(name='Tom', age=9)).unstruc() == dict(name='Tom', age=9)
...

</details>

### writer-sdk

The official Python library for the writer API

`pip install writer-sdk` · installs (wheel) · licence: Apache Software License · rank 10443 · last release 2026-06-02 · [PyPI](https://pypi.org/project/writer-sdk/) · [source](https://github.com/writer/writer-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Writer Python library provides access to the Writer REST API from any Python 3.9+
application. It includes a set of tools and utilities that make it easy to integrate the capabilities
of Writer into your projects.

It is generated with Stainless. ...

Example:
```python
from writerai import Writer

client = Writer()

chat_completion = client.chat.chat(
    messages=[
        {
            "content": "Write a haiku about programming",
            "role": "user",
        }
    ],
    model="palmyra-x5",
)
print(chat_completion.choices[0].message.content)
```

...

</details>

### spandrel-extra-arches

Implements extra model architectures for spandrel

`pip install spandrel-extra-arches` · installs (wheel) · licence: MIT License · rank 10459 · last release 2024-09-16 · [PyPI](https://pypi.org/project/spandrel-extra-arches/)

<details><summary>README extract</summary>

This library implements various PyTorch architectures with restrictive licenses for spandrel.

If you are working on a private project or non-commercial open-source project, you are free to use this library. ...

Example:
```python
import spandrel
import spandrel_extra_arches

# add extra architectures before `ModelLoader` is used
spandrel_extra_arches.install()

# load a model from disk
model = spandrel.ModelLoader().load_from_file(r"path/to/model.pth")

... # use model
```

Sections: Spandrel extra architectures, Basic usage

</details>

### Adafruit-PlatformDetect

Platform detection for use by libraries like Adafruit-Blinka.

`pip install Adafruit-PlatformDetect` · installs (wheel) · licence: MIT License · rank 10470 · last release 2026-10-28 · [PyPI](https://pypi.org/project/Adafruit-PlatformDetect/)

<details><summary>README extract</summary>

This library provides best-guess platform detection for a range of single-board
computers and (potentially) other platforms. It was written primarily for use
in Adafruit_Blinka, but may be
useful in other contexts.

Platform detection is divided into "chip" and "board" detection, with the latter
generally dependent on the former. ...

Example:
```python
from adafruit_platformdetect import Detector
detector = Detector()
print("Chip id: ", detector.chip.id)
print("Board id: ", detector.board.id)

# Check for specific board models:
print("Pi 3B+? ", detector.board.RASPBERRY_PI_3B_PLUS)
print("BBB? ", detector.board.BEAGLEBONE_BLACK)
print("Orange Pi PC? ", detector.board.ORANGE_PI_PC)
...
```

...

</details>

### pypaperless

Little api client for paperless(-ngx).

`pip install pypaperless` · installs (wheel) · licence: MIT License · rank 10477 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pypaperless/) · [source](https://github.com/tb1337/pypaperless)

<details><summary>README extract</summary>

[][release-url]
[][python-url]
[][license-url]

[][tests-url]
[][codecov-url]
[][linting-url]
[][typing-url]

pypaperless is a modern, fully async Python client library for the Paperless-ngx REST API.

- Features
- Quick example
- Installation
- Documentation
- Compatibility matrix
- Authors \& contributors

Features:
| Feature | Details |

| Fully async | Built on `asyncio` + `httpx.AsyncClient`; drop-in for any async framework |
| Type-safe models | All resources are validated Pydantic models |
| Complete resource coverage | Documents, Correspondents, Tags, ...

Example:
```python
import asyncio
from pypaperless import PaperlessClient

async def main():
    async with PaperlessClient("localhost:8000", "your-api-token") as paperless:
...

</details>

### pyobjc-framework-Metal

Wrappers for the framework Metal on macOS

`pip install pyobjc-framework-Metal` · installs from source (sdist only) · licence: MIT · rank 10479 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Metal/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Metal" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### ayafileio

Cross-platform async file API for Python. Blazing fast like Shameimaru Aya.

`pip install ayafileio` · installs (wheel) · licence: MIT License · rank 10486 · last release 2026-11-03 · [PyPI](https://pypi.org/project/ayafileio/) · [source](https://github.com/SaigyoujYuyuko/ayafileio.git)

<details><summary>README extract</summary>

English | 简体中文

> "The fastest file I/O in Gensokyo, swift as the Wind God Maiden."
> — Aya Shameimaru

Async file I/O on real kernel backends: IOCP on Windows, io_uring on Linux
(5.1+), Dispatch I/O on macOS. No thread pools pretending to be async;
`ayafileio.open()` picks the backend for you.

Features:
- Kernel backends avoid Python executor offloading
- Kernel-level completion: IOCP / io_uring / Dispatch I/O
- Cache-hit inline fast paths: hot small reads complete on the calling thread (IOCP sync-completion / io_uring COOP_TASKRUN / macOS mincore ...

Example:
```python
import asyncio
import ayafileio

async def main():
    # Write to a file — fast as the wind
    async with ayafileio.open("example.txt", "w") as f:
        await f.write("Hello, async world!\n")

...

</details>

### dishka-faststream

Integration package for Dishka DI and FastStream framework

`pip install dishka-faststream` · installs (wheel) · licence: Apache-2.0 · rank 10494 · last release 2026-06-04 · [PyPI](https://pypi.org/project/dishka-faststream/) · [source](https://github.com/faststream-community/dishka-faststream)

<details><summary>README extract</summary>

Though it is not required, you can use *dishka-faststream* integration. It features:

* automatic *REQUEST* scope management using middleware
* passing `StreamMessage` and `ContextRepo` object as a context data to providers
* automatic injection of dependencies into message handler.

You can use auto-injection for `FastStream` 0.5.0 and higher. ...

Example:
```python
from dishka_faststream import (
    FromDishka,
    inject,
    setup_dishka,
    FastStreamProvider,
)
from dishka import make_async_container, Provider, provide, Scope
```

Sections: FastStream integration for Dishka, How to use, FastStream - Litestar/FastAPI - dishka integration, Example of usage FastStream + FastAPI

</details>

### cocoindex

With CocoIndex, users declare the transformation, CocoIndex creates & maintains an index, and keeps the derived index up to date based on source update, with minimal computation and changes.

`pip install cocoindex` · installs (wheel) · licence: Apache Software License · rank 10505 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cocoindex/)

<details><summary>README extract</summary>

Star us ❤️ → ·

CocoIndex turns codebases, meeting notes, inboxes, Slack, PDFs, and videos into live, continuously fresh context for your AI agents and LLM apps to reason over effectively — with minimal incremental processing. ...

Features:
Your agents are only as good as the data they see.
Batch pipelines drift stale. CocoIndex stays live — and only runs the Δ.

Example:
```python
import cocoindex as coco
from cocoindex.connectors import localfs, postgres
from cocoindex.ops.text import RecursiveSplitter

@coco.fn(memo=True)                          # ← cached by hash(input) + hash(code)
async def index_file(file, table):
    for chunk in RecursiveSplitter().split(await file.read_text()):
...
```

...

</details>

### vineyard-bdist

An in-memory immutable data manager

`pip install vineyard-bdist` · installs (wheel) · licence: Apache Software License · rank 10511 · last release 2024-08-29 · [PyPI](https://pypi.org/project/vineyard-bdist/) · [docs](https://v6d.io) · [source](https://github.com/v6d-io/v6d)

<details><summary>README extract</summary>

|crates.ioDocker HUBArtifact HUBACM DL|

Vineyard (v6d) is an innovative in-memory immutable data manager that offers **out-of-the-box
high-level abstractions and zero-copy in-memory** sharing for distributed data in various
big data tasks, such as graph analytics (e.g., GraphScope), numerical computing
(e.g., Mars), and machine learning. ...

Sections: vineyard: an in-memory immutable data manager, What is vineyard, Features, Efficient In-Memory Immutable Data Sharing, Out-of-the-Box High-Level Data Abstractions, Stream Pipelining for Enhanced Performance, Versatile Drivers for Common Tasks, Try Vineyard, Deploying on Kubernetes, FAQ, Get Involved, Publications

</details>

### wireup

Python Dependency Injection Library

`pip install wireup` · installs (wheel) · licence: MIT License · rank 10512 · last release 2026-11-03 · [PyPI](https://pypi.org/project/wireup/) · [docs](https://maldoinc.github.io/wireup/) · [source](https://github.com/maldoinc/wireup)

<details><summary>README extract</summary>

Type-driven dependency injection for Python. Wireup is battle-tested in production, thread-safe, no-GIL (PEP 703) ready, and fail-fast by design: if the container starts, it works.

 Quick Start ·
 Docs ·
 Benchmarks ·
 Migrate to Wireup

Example:
```python
import fastapi
import wireup
import wireup.integration.fastapi
from wireup import Injected, injectable

@injectable
class Database:
    def query(self, sql: str) -> list[str]: ...

@injectable
class UserService:
    def init(self, db: Database) -> None:
        self.db = db

    def get_users(self) -> list[str]:
...
```

...

</details>

### haikunator

Heroku-like random name generator for python.

`pip install haikunator` · installs (wheel) · licence: BSD License · rank 10531 · last release 2016-09-20 · [PyPI](https://pypi.org/project/haikunator/)

### indexed-bzip2

Fast random access to bzip2 files

`pip install indexed-bzip2` · installs from source (sdist only) · licence: Apache Software License; MIT License · rank 10534 · last release 2025-07-21 · [PyPI](https://pypi.org/project/indexed-bzip2/)

<details><summary>README extract</summary>

This module provides an IndexedBzip2File class, which can be used to seek inside bzip2 files without having to decompress them first.
Alternatively, you can use this simply as a parallelized bzip2 decoder as a replacement for Python's builtin `bz2` module in order to fully utilize all your cores. ...

Example:
```python
import bz2
import os
import time

fileSize = os.stat(bz2FilePath).st_size

with bz2.open(bz2FilePath) as file:
    t0 = time.time()
    while file.read(512*1024):
        pass
    bz2Duration = time.time() - t0
    print(f"Decoded file in {bz2Duration:.0f}s, bandwidth: {fileSize / bz2Duration / 1e6:.1f} MB/s")
```

...

</details>

### pyjnius

A Python library for accessing access Java classes as using the Java Native Interface (JNI).

`pip install pyjnius` · installs (wheel) · licence: MIT License · rank 10538 · last release 2026-10-10 · [PyPI](https://pypi.org/project/pyjnius/) · [docs](https://pyjnius.readthedocs.io) · [source](https://github.com/kivy/pyjnius)

<details><summary>README extract</summary>

PyJNIus is a Python library for accessing
Java classes using the
Java Native Interface
(JNI).

PyJNIus is managed by the Kivy Team and can be
used with python-for-android.

It can also be used independently of Kivy, on desktop and mobile platforms.

> [!WARNING]
> The PyPI package name is now
pyjnius instead of `jnius`.

/badge.svg)

Installation ...

Example:
```python
>>> from jnius import autoclass
>>> autoclass('java.lang.System').out.println('Hello world')
Hello world

>>> Stack = autoclass('java.util.Stack')
>>> stack = Stack()
>>> stack.push('hello')
>>> stack.push('world')
>>> print(stack.pop())
world
>>> print(stack.pop())
hello
```

Sections: PyJNIus, Documentation, Backers

</details>

### mdformat-front-matters

An mdformat plugin to format YAML, TOML, or JSON front matter

`pip install mdformat-front-matters` · installs (wheel) · licence: MIT · rank 10549 · last release 2025-12-04 · [PyPI](https://pypi.org/project/mdformat-front-matters/)

<details><summary>README extract</summary>

[][ci-link] [][pypi-link]

An mdformat plugin for normalizing YAML, TOML, and JSON front matter in CommonMark documents.

> [!NOTE]
> `mdformat-frontmatter` has additional duplicate key detection, but did not support mdformat v1 (butler54/mdformat-frontmatter #37) nor TOML and JSON at the time (
> Along with the 's', the extra dash is intentional ...

Features:
- Multi-format support: Handles YAML (`---`), TOML (`+++`), and JSON (`{...}`) front matter
- Automatic normalization: Formats front matter consistently (preserves key order by default, standardized indentation) ...

Example:
```python
from markdown_it import MarkdownIt

from mdformat_front_matters.mdit_plugins import front_matters_plugin

md = MarkdownIt()
md.use(front_matters_plugin)

text = """
+++
title = "Example"
...

</details>

### intbitset

C-based extension implementing fast integer bit sets.

`pip install intbitset` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 10554 · last release 2026-04-28 · [PyPI](https://pypi.org/project/intbitset/)

_README extract left out: share-alike licence._

### siphashc

Python module (in c) for siphash-2-4

`pip install siphashc` · installs (wheel) · licence: ISC · rank 10565 · last release 2026-10-23 · [PyPI](https://pypi.org/project/siphashc/) · [source](https://github.com/WeblateOrg/siphashc)

<details><summary>README extract</summary>

siphashc is a Python C extension implementing SipHash-2-4.

Maintained by Weblate — a privacy-respecting localization platform built on open-source foundations.

Example:
```python
>>> from siphashc import siphash
>>> siphash("sixteencharstrng", "i need a hash of this")
10796923698683394048
```

Sections: siphashc, Introduction, Usage

</details>

### pyobjc-framework-AppleScriptKit

Wrappers for the framework AppleScriptKit on macOS

`pip install pyobjc-framework-AppleScriptKit` · installs (wheel) · licence: MIT · rank 10579 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-AppleScriptKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for framework 'AppleScriptKit'.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### statsd-tags

A simple statsd client with DogTag-compatible tag support.

`pip install statsd-tags` · installs (wheel) · licence: MIT License · rank 10590 · last release 2016-12-24 · [PyPI](https://pypi.org/project/statsd-tags/)

### hickle

Hickle - an HDF5 based version of pickle

`pip install hickle` · installs (wheel) · licence: OSI Approved · rank 10593 · last release 2024-03-30 · [PyPI](https://pypi.org/project/hickle/)

<details><summary>README extract</summary>

Hickle is an HDF5 based clone of `pickle`, with a twist: instead of serializing to a pickle file,
Hickle dumps to an HDF5 file (Hierarchical Data Format). It is designed to be a "drop-in" replacement for pickle (for common data objects), but is
really an amalgam of `h5py` and `pickle` with extended functionality. ...

Example:
```python
import os
import hickle as hkl
import numpy as np

# Create a numpy array of data
array_obj = np.ones(32768, dtype='float32')

# Dump to file
hkl.dump(array_obj, 'test.hkl', mode='w')

# Dump data, with compression
hkl.dump(array_obj, 'test_gzip.hkl', mode='w', compression='gzip')

# Compare filesizes
...
```

Sections: Hickle, HDF5 compression options, Note: storing complex objects in HDF5 file, Easy method, Optional requirements

</details>

### pyobjc-framework-Photos

Wrappers for the framework Photos on macOS

`pip install pyobjc-framework-Photos` · installs from source (sdist only) · licence: MIT · rank 10606 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Photos/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Photos" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### luaparser

A lua parser in Python

`pip install luaparser` · installs (wheel) · licence: MIT · rank 10613 · last release 2026-08-29 · [PyPI](https://pypi.org/project/luaparser/)

<details><summary>README extract</summary>

A Lua parser and AST builder written in Python.

It's both a development library and a command line tool.

Example:
```python
from luaparser import ast

src = """
    local function sayHello()
      print('hello world !')
    end
    sayHello()
    """

tree = ast.parse(src)
print(ast.to_pretty_str(tree))
```

Sections: py-lua-parser, Compatibility with Lua grammar, Options, Quickstart, Node structure, Working on AST tree, Rendering lua code, Command line

</details>

### pypi

PyPI is the Python Package Index at http://pypi.org/

`pip install pypi` · installs from source (sdist only) · licence: BSD License · rank 10619 · last release 2018-03-24 · [PyPI](https://pypi.org/project/pypi/)

<details><summary>README extract</summary>

PyPI has a new home at < Users should need not need to change
anything, as the old "www" address should still work. Use of the new
address in preference is encouraged.

Developers interested in how PyPI works, or in contributing to the project,
should visit

</details>

### hiddenlayer-sdk

The official Python library for the hiddenlayer API

`pip install hiddenlayer-sdk` · installs (wheel) · licence: Apache Software License · rank 10620 · last release 2026-09-10 · [PyPI](https://pypi.org/project/hiddenlayer-sdk/) · [source](https://github.com/hiddenlayerai/hiddenlayer-sdk-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The HiddenLayer Python library provides convenient access to the HiddenLayer REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
from hiddenlayer import HiddenLayer

client = HiddenLayer(
    # defaults to "prod-us".
    environment="prod-eu",
)

response = client.interactions.analyze(
    metadata={
        "model": "REPLACE_ME",
        "requester_id": "REPLACE_ME",
    },
    input={
        "messages": [
            {
                "role": "user",
...
```

...

</details>

### pyobjc-framework-EventKit

Wrappers for the framework Accounts on macOS

`pip install pyobjc-framework-EventKit` · installs (wheel) · licence: MIT · rank 10633 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-EventKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "EventKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### domaintools-api

DomainTools Official Python API

`pip install domaintools-api` · installs (wheel) · licence: MIT License · rank 10634 · last release 2026-09-08 · [PyPI](https://pypi.org/project/domaintools-api/)

<details><summary>README extract</summary>

===================

DomainTools Official Python API

The DomainTools Python API Wrapper provides an interface to work with our cybersecurity and related data tools provided by our Iris Investigate™, Iris Enrich™, and Iris Detect™ products. It is actively maintained and may be downloaded via GitHub or PyPI. ...

Example:
```python
from domaintools import API

api = API(USER_NAME, KEY)
```

Sections: Using the API, IrisQL, Using the API Asynchronously, Interacting with the API via the command line client, Authentication, Real-Time Threat Feeds, Feed parameters, Session Management Parameters, Filter Parameters, Result formatting parameters, Download-only parameters, Handling iterative response from RTTF endpoints, Running E2E Tests Locally, Preparation

</details>

### cloudshell-shell-core

Core package for all CloudShell Shells. This package contains the basic driver interfaces and metadata definitions as well as utilities and helpers created specifically for Shells

`pip install cloudshell-shell-core` · installs (wheel) · licence: Apache Software License · rank 10646 · last release 2026-08-24 · [PyPI](https://pypi.org/project/cloudshell-shell-core/)

<details><summary>README extract</summary>

Core package for all CloudShell Shells. This package contains the basic driver interfaces and metadata definitions as well as utilities and helpers created specifically for Shells

</details>

### azure-containerapps-sandbox

Azure Container Apps Sandbox SDK for Python — data plane + sandbox group management. Community preview.

`pip install azure-containerapps-sandbox` · installs (wheel) · licence: MIT License · rank 10654 · last release 2026-07-17 · [PyPI](https://pypi.org/project/azure-containerapps-sandbox/) · [source](https://github.com/microsoft/azure-container-apps)

<details><summary>README extract</summary>

> ⚠️ Preview — This SDK is in preview. The API surface may change without notice.

Data-plane and control-plane SDK for Azure Container Apps sandboxes.

Secure, isolated compute environments with sub-second startup.

- Hardware-isolated microVM boundary — fully separated from host, platform, and other sandboxes ...

Example:
```python
import uuid
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.containerapps.sandbox import (
    SandboxGroupManagementClient,
    SandboxGroupClient,
    endpoint_for_region,
)

...
```

...

</details>

### aioretry

Asyncio retry utility for Python 3.7+

`pip install aioretry` · installs (wheel) · licence: MIT License · rank 10657 · last release 2025-02-20 · [PyPI](https://pypi.org/project/aioretry/)

<details><summary>README extract</summary>

Asyncio retry utility for Python 3.7+

- Upgrade guide

Example:
```python
import asyncio

from aioretry import (
    retry,
    # Tuple[bool, Union[int, float]]
    RetryPolicyStrategy,
    RetryInfo
)

# This example shows the usage with python typings
def retry_policy(info: RetryInfo) -> RetryPolicyStrategy:
    """
    - It will always retry until succeeded: abandon = False
...
```

Sections: aioretry, Usage, Use as class instance method decorator, Use instance method as retry policy, Register an `before_retry` callback, Only retry for certain types of exceptions, APIs, retry(retry_policy, before_retry)(fn), RetryPolicy, Python typings, Upgrade guide, 2.x -> 5.x, 3.x -> 5.x, 4.x -> 5.x

</details>

### omnimarket

OmniMarket - Portable ONEX workflow package registry

`pip install omnimarket` · installs (wheel) · licence: MIT · rank 10658 · last release 2026-10-29 · [PyPI](https://pypi.org/project/omnimarket/) · [source](https://github.com/OmniNode-ai/omnimarket)

<details><summary>README extract</summary>

OmniMarket provides portable ONEX workflow packages and contract-driven automation.
Documentation: public knowledge base.

</details>

### grizzled-python

The Grizzled Python Utility Library

`pip install grizzled-python` · installs (wheel) · licence: BSD License · rank 10663 · last release 2019-03-12 · [PyPI](https://pypi.org/project/grizzled-python/)

<details><summary>README extract</summary>

The Grizzled Utility Library is a general-purpose Python library with
a variety of different modules and packages. It's roughly organized into
subpackages that group different kinds of utility functions and classes.

</details>

### flake8-picky-parentheses

flake8 plugin to nitpick about parenthesis, brackets, and braces

`pip install flake8-picky-parentheses` · installs (wheel) · licence: Apache Software License · rank 10675 · last release 2026-01-10 · [PyPI](https://pypi.org/project/flake8-picky-parentheses/) · [source](https://github.com/robsdedude/flake8-picky-parentheses)

<details><summary>README extract</summary>

Picky Parentheses is a flake8 plugin that
nitpicks all things parentheses, brackets and braces.
The plugin has two components:
 1. A checker that warns about redundant parentheses (with some exceptions).
 2. A checker for parentheses, brackets, and braces alignment. ...

Example:
```python
# BAD
answer = func((
    1, 2, 3, 4, 5,
    )
)

# GOOD
answer = func((
    1, 2, 3, 4, 5,
))
```

Sections: Picky Parentheses, Error Codes, `PAR0xx`, `PAR001`, `PAR002`, `PAR1xx`, `PAR101`, `PAR102`, `PAR103`, `PAR104`, Details and Exceptions, Footnotes, Additional Notes

</details>

### intel-sycl-rt

Intel® oneAPI DPC++/C++ SYCL Compiler Runtime package

`pip install intel-sycl-rt` · installs (wheel) · licence: Other/Proprietary License · rank 10682 · last release 2026-10-16 · [PyPI](https://pypi.org/project/intel-sycl-rt/)

<details><summary>README extract</summary>

This COMPILER-SPECIFIC Intel® oneAPI DPC++/C++ SYCL Compiler Runtime package uses the SYCL framework and combines it with compilers, APIs, libraries, tools, and code samples that delivers a rich catalog of SYCL and oneAPI fully enabled applications with the achievable vision of ubiquitous multiarchitecture and multivendor computing. ...

</details>

### vdf

Library for working with Valve's VDF text format

`pip install vdf` · installs (wheel) · licence: MIT License · rank 10685 · last release 2021-05-22 · [PyPI](https://pypi.org/project/vdf/)

<details><summary>README extract</summary>

pypilicensecoveragemaster_build|
sonar_maintainabilitysonar_reliabilitysonar_security|

Pure python module for (de)serialization to and from VDF that works just like `json`.

Tested and works on `py2.7`, `py3.3+`, `pypy` and `pypy3`.

VDF is Valve's KeyValue text file format

| Supported versions: `kv1`
| Unsupported: `kv2` and `kv3`

Example:
```python
import vdf

# parsing vdf from file or string
d = vdf.load(open('file.txt'))
d = vdf.loads(vdf_text)
d = vdf.parse(open('file.txt'))
d = vdf.parse(vdf_text)

# dumping dict as vdf to string
vdf_text = vdf.dumps(d)
indented_vdf = vdf.dumps(d, pretty=True)

# dumping dict as vdf to file
vdf.dump(d, open('file2.txt','w'), pretty=True)
```

Sections: Problems & solutions, Example usage

</details>

### finch-api

The official Python library for the Finch API

`pip install finch-api` · installs (wheel) · licence: Apache Software License · rank 10707 · last release 2026-11-04 · [PyPI](https://pypi.org/project/finch-api/) · [source](https://github.com/Finch-API/finch-api-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Finch Python library provides convenient access to the Finch REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
from finch import Finch

client = Finch(
    access_token="My Access Token",
)

page = client.hris.directory.list()
print(page.individuals)
```

Sections: Finch Python API library, MCP Server, Documentation, Usage, Async usage, With aiohttp, Using types, Pagination, Webhook Verification, Handling errors, Retries, Timeouts, Default Headers, Advanced

</details>

### ruff-lsp

A Language Server Protocol implementation for Ruff.

`pip install ruff-lsp` · installs (wheel) · licence: MIT · rank 10715 · last release 2025-02-10 · [PyPI](https://pypi.org/project/ruff-lsp/) · [source](https://github.com/astral-sh/ruff-lsp)

### text2ql

Natural language to any query language, starting with GraphQL

`pip install text2ql` · installs (wheel) · licence: Apache-2.0 · rank 10717 · last release 2026-08-27 · [PyPI](https://pypi.org/project/text2ql/) · [source](https://github.com/riteshakumar/text2ql)

<details><summary>README extract</summary>

Natural-language to query-language toolkit for GraphQL and SQL.

`text2ql` is built for practical usage: deterministic generation, LLM-assisted generation, schema/mapping normalization, evaluation utilities, and benchmark adapters (Spider/BIRD). ...

Features:
- Fast path from text -> query for GraphQL and SQL.
- Three generation modes: `deterministic`, `llm`, `function_calling`.
- Schema + mapping aware generation with validation and confidence scoring. ...

Example:
```python
from text2ql import Text2QL

service = Text2QL()
result = service.generate(
    text="list active customers",
    target="graphql",
    schema={"entities": ["customers"], "fields": {"customers": ["id", "status", "email"]}},
...

</details>

### tbb-devel

Intel® oneAPI Threading Building Blocks

`pip install tbb-devel` · installs (wheel) · licence: Other/Proprietary License · rank 10718 · last release 2026-10-16 · [PyPI](https://pypi.org/project/tbb-devel/)

<details><summary>README extract</summary>

Intel® oneAPI Threading Building Blocks (oneTBB) header files, x86_64 dynamic and import libraries for Windows*. Intel® oneAPI Threading Building Blocks (oneTBB) is a flexible performance library that supports scalable parallel programming using C++ code compliant with ISO C++ standard.

</details>

### cot

Common OVF Tool

`pip install cot` · installs (wheel) · licence: MIT License · rank 10723 · last release 2019-12-04 · [PyPI](https://pypi.org/project/cot/)

<details><summary>README extract</summary>

COT (the Common OVF Tool) is a tool for editing Open Virtualization Format
(`.ovf`, `.ova`) virtual appliances, with a focus on virtualized network
appliances such as the Cisco CSR 1000V and Cisco IOS XRv platforms.

COT's capabilities include: ...

</details>

### stringparser

Easy to use pattern matching and information extraction

`pip install stringparser` · installs (wheel) · licence: BSD License · rank 10727 · last release 2023-11-16 · [PyPI](https://pypi.org/project/stringparser/)

<details><summary>README extract</summary>

The `stringparser` module provides a simple way to match patterns and
extract information within strings. As patterns are given using the
familiar format string specification 3101., writing them is much easier than writing regular
expressions (albeit less powerful).

Just install it using:

Example:
```python
>>> from stringparser import Parser
>>> parser = Parser('The answer is {:d}')
>>> parser('The answer is 42')
42
>>> parser('The answer is 54')
54
```

Sections: Motivation, Examples, Limitations

</details>

### Adafruit-PureIO

Pure python (i.e. no native extensions) access to Linux IO including I2C and SPI. Drop in replacement for smbus and spidev modules.

`pip install Adafruit-PureIO` · installs (wheel) · licence: MIT License · rank 10731 · last release 2026-09-24 · [PyPI](https://pypi.org/project/Adafruit-PureIO/)

<details><summary>README extract</summary>

Pure python (i.e. no native extensions) access to Linux IO including I2C and SPI. Drop in replacement for smbus and spidev modules.

This driver depends on:

* Python 3.5 or higher

Sections: Introduction, Dependencies, Documentation

</details>

### anomalo

Python bindings for the Anomalo API

`pip install anomalo` · installs (wheel) · licence: Apache-2.0 · rank 10735 · last release 2026-11-05 · [PyPI](https://pypi.org/project/anomalo/)

<details><summary>README extract</summary>

A basic REST API client and command line client for Anomalo

</details>

### cloudshell-core

Core package for CloudShell Python orchestration and automation. This package contains commoncode for CloudShell packages, including logging, basic interfaces and other utilities

`pip install cloudshell-core` · installs from source (sdist only) · licence: Apache Software License · rank 10736 · last release 2017-08-09 · [PyPI](https://pypi.org/project/cloudshell-core/)

### candidhealth

(no summary)

`pip install candidhealth` · installs (wheel) · licence: Apache Software License · rank 10739 · last release 2026-10-31 · [PyPI](https://pypi.org/project/candidhealth/) · [source](https://github.com/candidhealth/candid-python)

<details><summary>README extract</summary>

The Candid Python library provides convenient access to the Candid APIs from Python.

Example:
```python
from candid import CandidApiClient
from candid.resources.pre_encounter.resources.coverages.resources.v_1 import (
    MemberInfo,
)
from candid.resources.pre_encounter.resources.eligibility_checks.resources.v_1 import (
    EligibilityRequest,
    IndividualProvider,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
...
```

Sections: Candid Python Library, Reference, Usage, Async Client, Exception Handling, Oauth Token Override, Advanced, Access Raw Response Data, Retries, Timeouts, Custom Client

</details>

