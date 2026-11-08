# Unclassified / C

[Index](README.md) · 471 packages in this topic, by downloads.

### certifi

Python package for providing Mozilla's CA Bundle.

`pip install certifi` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 4 · last release 2026-10-23 · [PyPI](https://pypi.org/project/certifi/) · [source](https://github.com/certifi/python-certifi)

<details><summary>README extract</summary>

Certifi provides Mozilla's carefully curated collection of Root Certificates for
validating the trustworthiness of SSL certificates while verifying the identity
of TLS hosts. It has been extracted from the Requests project.

Example:
```python
>>> import certifi

>>> certifi.where()
'/usr/local/lib/python3.7/site-packages/certifi/cacert.pem'
```

Sections: Certifi: Python SSL Certificates, Usage, Addition/Removal of Certificates

</details>

### cffi

Foreign Function Interface for Python calling C code.

`pip install cffi` · installs (wheel) · licence: MIT-0 · rank 10 · last release 2026-08-03 · [PyPI](https://pypi.org/project/cffi/) · [docs](https://cffi.readthedocs.io/) · [source](https://github.com/python-cffi/cffi)

<details><summary>README extract</summary>

[][Documentation]

Foreign Function Interface for Python calling C code.

Please see the [Documentation] or uncompiled in the `doc/` subdirectory.

Download

Download page

Source Code

Source code is publicly available on
GitHub.

Contact

Mailing list

Testing/development tips ...

</details>

### click

Composable command line interface toolkit

`pip install click` · installs (wheel) · licence: BSD-3-Clause · rank 20 · last release 2026-11-06 · [PyPI](https://pypi.org/project/click/) · [docs](https://click.palletsprojects.com/) · [source](https://github.com/pallets/click/)

<details><summary>README extract</summary>

Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary. It's the "Command
Line Interface Creation Kit". It's highly configurable but comes with
sensible defaults out of the box. ...

Example:
```python
import click

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

if name == 'main':
...
```

Sections: Click, A Simple Example

</details>

### cycler

Composable style cycles

`pip install cycler` · installs (wheel) · licence: BSD License · rank 197 · last release 2023-10-07 · [PyPI](https://pypi.org/project/cycler/) · [source](https://github.com/matplotlib/cycler)

### cfgv

Validate configuration and produce human readable error messages.

`pip install cfgv` · installs (wheel) · licence: MIT · rank 213 · last release 2025-11-19 · [PyPI](https://pypi.org/project/cfgv/)

<details><summary>README extract</summary>

Validate configuration and produce human readable error messages.

Example:
```python
pre_commit.clientlib.InvalidConfigError:
==> File /home/asottile/workspace/pre-commit/.pre-commit-config.yaml
==> At Config()
==> At key: repos
==> At Repository(repo='
==> At key: hooks
==> At Hook(id='flake8')
==> At key: always_run
=====> Expected bool got str
```

Sections: cfgv, Sample error messages, API, `cfgv.validate(value, schema)`, `cfgv.apply_defaults(value, schema)`, `cfgv.remove_defaults(value, schema)`, Making a schema, writing your own schema container, `Map(object_name, id_key, *items)`, `Array(of, allow_empty=True)`, `KeyValueMap(object_name, key_check_fn, value_schema)`, Validator objects, writing your own validator, `Required(key, check_fn)`

</details>

### croniter

croniter provides iteration for datetime object with cron like format

`pip install croniter` · installs (wheel) · licence: MIT · rank 303 · last release 2026-07-10 · [PyPI](https://pypi.org/project/croniter/)

<details><summary>README extract</summary>

croniter provides iteration for the datetime object with a cron like format.

Website:

Example:
```python
>>> from croniter import croniter
>>> from datetime import datetime
>>> base = datetime(2010, 1, 25, 4, 46)
>>> iter = croniter('*/5 * * * *', base)  # every 5 minutes
>>> print(iter.get_next(datetime))   # 2010-01-25 04:50:00
>>> print(iter.get_next(datetime))   # 2010-01-25 04:55:00
>>> print(iter.get_next(datetime))   # 2010-01-25 05:00:00
>>>
...
```

Sections: Introduction, Usage, Strict validation, Last day of month (l), Nearest weekday (W), Day-of-month and day-of-week, Vixie cron bug compatibility, About DST, About second repeats, About year, Gaps between date matches, Iterating over a range using cron, Hashed expressions, Random expressions

</details>

### cyclopts

Intuitive, easy CLIs based on type hints.

`pip install cyclopts` · installs (wheel) · licence: Apache-2.0 · rank 341 · last release 2026-11-02 · [PyPI](https://pypi.org/project/cyclopts/) · [source](https://github.com/BrianPugh/cyclopts)

<details><summary>README extract</summary>

Documentation:

Source Code:

Cyclopts is a modern, easy-to-use command-line interface (CLI) framework that aims to provide an intuitive & efficient developer experience.

Features:
- Intuitive API: Quickly write CLI applications using a terse, intuitive syntax.

- Advanced Type Hinting: Full support of all builtin types and even user-specified (yes, including Pydantic, Dataclasses, and Attrs). ...

Example:
```python
from cyclopts import run

def foo(loops: int):
    for i in range(loops):
        print(f"Looping! {i}")

run(foo)
```

Sections: Why Cyclopts?, Quick Start, Compared to Typer

</details>

### cbor2

CBOR (de)serializer with extensive tag support

`pip install cbor2` · installs (wheel) · licence: MIT · rank 355 · last release 2026-11-07 · [PyPI](https://pypi.org/project/cbor2/) · [docs](https://cbor2.readthedocs.org/en/latest/) · [source](https://github.com/agronholm/cbor2)

<details><summary>README extract</summary>

This library provides encoding and decoding for the Concise Binary Object Representation (CBOR)
(RFC 8949) serialization format. The specification is fully compatible with the original RFC
7049. Read the docs to learn more.

It is implemented in Rust.

Features:
* Simple API like the `json` or `pickle` modules
* Support many CBOR tags with stdlib objects
* Generic tag decoding
* Shared value references including cyclic references
* String references compact encoding with repeated strings replaced with ...

Sections: About, Features, Build requirements, Usage, Command-line Usage

</details>

### comm

Jupyter Python Comm implementation, for usage in ipykernel, xeus-python etc.

`pip install comm` · installs (wheel) · licence: BSD License · rank 381 · last release 2025-07-25 · [PyPI](https://pypi.org/project/comm/)

<details><summary>README extract</summary>

It provides a way to register a Kernel Comm implementation, as per the Jupyter kernel protocol.
It also provides a base Comm implementation and a default CommManager that can be used.

We provide default implementations for usage in IPython:

This is typically what ipykernel and JupyterLite's pyolite kernel will do.

Example:
```python
import comm

class MyCustomComm(comm.base_comm.BaseComm):
    def publish_msg(self, msg_type, data=None, metadata=None, buffers=None, **keys):
        # TODO implement the logic for sending comm messages through the iopub channel
        pass

comm.create_comm = MyCustomComm
```

Sections: Comm, Register a comm implementation in the kernel, Comm users

</details>

### click-repl

REPL plugin for Click

`pip install click-repl` · installs (wheel) · licence: MIT · rank 455 · last release 2026-10-05 · [PyPI](https://pypi.org/project/click-repl/)

<details><summary>README extract</summary>

Example:
```python
import click
from click_repl import register_repl

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo("Hello world!")

register_repl(cli)
cli()
```

Sections: click-repl, Usage, Advanced Usage

</details>

### click-didyoumean

Enables git-like *did-you-mean* feature in click

`pip install click-didyoumean` · installs (wheel) · licence: MIT License · rank 459 · last release 2024-03-24 · [PyPI](https://pypi.org/project/click-didyoumean/) · [source](https://github.com/click-contrib/click-didyoumean)

<details><summary>README extract</summary>

Enable git-like *did-you-mean* feature in click.

It's as simple as this:

Example:
```python
import click
from click_didyoumean import DYMGroup

@click.group(cls=DYMGroup)
def cli():
    pass

@cli.command()
def foo():
    pass

@cli.command()
def bar():
    pass

@cli.command()
def barrr():
    pass

if name == "main":
    cli()
```

Sections: click-didyoumean, Usage, Change configuration, Examples

</details>

### cedarpy

(no summary)

`pip install cedarpy` · installs (wheel) · licence: not stated · rank 505 · last release 2026-10-14 · [PyPI](https://pypi.org/project/cedarpy/)

<details><summary>README extract</summary>

&nbsp;

`cedarpy` helps you use the (Rust) Cedar Policy library from Python. You can use `cedarpy` to:
* check whether a request is authorized by the Cedar Policy engine
* validate policies against a schema
* format policies ...

Example:
```python
from cedarpy import PolicySet, is_authorized, is_authorized_batch, Decision

policies: str = "// a string containing cedar policies"

# Parse once (e.g. at process/Lambda cold start). Parse errors raise ValueError here,
# rather than being folded into an authorization result.
policy_set = PolicySet.from_str(policies)

...
```

...

</details>

### crashtest

Manage Python errors with ease

`pip install crashtest` · installs (wheel) · licence: MIT License · rank 506 · last release 2022-11-02 · [PyPI](https://pypi.org/project/crashtest/) · [source](https://github.com/sdispater/crashtest)

<details><summary>README extract</summary>

Crashtest is a Python library that makes exceptions handling and inspection easier.

</details>

### cattrs

Composable complex class support for attrs and dataclasses.

`pip install cattrs` · installs (wheel) · licence: MIT License · rank 562 · last release 2026-09-26 · [PyPI](https://pypi.org/project/cattrs/) · [docs](https://catt.rs/en/stable/) · [source](https://github.com/python-attrs/cattrs)

<details><summary>README extract</summary>

*Because validation belongs to the edges.*

<!-- begin-teaser -->

cattrs is a Swiss Army knife for (un)structuring and validating data in Python.
In practice, that means it converts unstructured dictionaries into proper classes and back, while validating their contents.

<!-- end-teaser -->

Example:
```python
>>> from attrs import define
>>> from cattrs import structure, unstructure
>>> @define
... class C:
...     a: int
...     b: list[str]
>>> instance = structure({'a': 1, 'b': ['x', 'y']}, C)
>>> instance
C(a=1, b=['x', 'y'])
>>> unstructure(instance)
{'a': 1, 'b': ['x', 'y']}
```

Sections: cattrs*: Flexible Object Serialization and Validation, Example, Features, Recursive Unstructuring, Recursive Structuring, Batteries Included, Design Decisions

</details>

### claude-agent-sdk

Python SDK for Claude Code

`pip install claude-agent-sdk` · installs (wheel) · licence: MIT License · rank 601 · last release 2026-11-06 · [PyPI](https://pypi.org/project/claude-agent-sdk/) · [docs](https://docs.anthropic.com/en/docs/claude-code/sdk)

<details><summary>README extract</summary>

Python SDK for Claude Agent. See the Claude Agent SDK documentation for more information.

Example:
```python
import anyio
from claude_agent_sdk import query

async def main():
    async for message in query(prompt="What is 2 + 2?"):
        print(message)

anyio.run(main)
```

Sections: Claude Agent SDK for Python, Quick Start, Basic Usage: query(), Using Tools, Working Directory, System Prompt, ClaudeSDKClient, Custom Tools (as In-Process SDK MCP Servers), Creating a Simple Tool, Benefits Over External MCP Servers, Migration from External Servers, Hooks, Example, Types

</details>

### cuda-pathfinder

Pathfinder for CUDA components

`pip install cuda-pathfinder` · installs (wheel) · licence: Apache-2.0 · rank 606 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cuda-pathfinder/) · [docs](https://nvidia.github.io/cuda-python/) · [source](https://github.com/NVIDIA/cuda-python)

<details><summary>README extract</summary>

cuda.pathfinder
aims to be a one-stop solution for locating CUDA components. Currently
it supports locating and loading dynamic libraries (`.so`, `.dll`), and
locating CTK header directories. Support for other artifacts is in progress.

* Documentation
* Releases
* Repository
* Issue tracker (select component `cuda.pathfinder`) ...

</details>

### curl-cffi

libcurl ffi bindings for Python, with impersonation support.

`pip install curl-cffi` · installs (wheel) · licence: MIT · rank 607 · last release 2026-10-26 · [PyPI](https://pypi.org/project/curl-cffi/) · [source](https://github.com/lexiforest/curl_cffi)

<details><summary>README extract</summary>

Documentation

Python binding for curl-impersonate fork
via cffi. For commercial support, visit impersonate.pro.

`curl_cffi` is the most popular Python binding for `curl`. Unlike other pure
python http clients like `httpx` or `requests`, `curl_cffi` can impersonate
browsers' TLS/JA3 and HTTP/2 fingerprints. ...

Features:
- Supports JA3/TLS and http2 fingerprints impersonation, including recent browsers and custom fingerprints.
- Much faster than requests/httpx, on par with aiohttp/pycurl, see benchmarks.
- Mimics the requests API, no need to learn another one. ...

Example:
```python
import curl_cffi

# Notice the impersonate parameter
r = curl_cffi.get(" impersonate="chrome")

print(r.json())
# output: {..., "ja3n_hash": "aa56c057ad164ec4fdcb7a5a283be9fc", ...}
...

</details>

### clickhouse-connect

ClickHouse Database Core Driver for Python, Pandas, and Superset

`pip install clickhouse-connect` · installs (wheel) · licence: Apache-2.0 · rank 618 · last release 2026-11-03 · [PyPI](https://pypi.org/project/clickhouse-connect/)

<details><summary>README extract</summary>

A high performance core database driver for connecting ClickHouse to Python, Pandas, and Superset

* Pandas DataFrames (numpy and arrow-backed). Requires pandas 2.0 or later.
* Numpy Arrays
* PyArrow Tables
* Polars DataFrames
* Superset Connector
* SQLAlchemy Core (select, joins, lightweight deletes; limited feature set) ...

Sections: ClickHouse Connect, Upgrading from 0.x, Superset Connectivity, SQLAlchemy Implementation, Alembic Migrations, Complete Documentation

</details>

### cramjam

(no summary)

`pip install cramjam` · installs (wheel) · licence: MIT · rank 623 · last release 2026-10-13 · [PyPI](https://pypi.org/project/cramjam/) · [docs](https://docs.rs/cramjam/latest/cramjam) · [source](https://github.com/milesgranger/pyrus-cramjam)

<details><summary>README extract</summary>

API Documentation

Example:
```python
>>> import cramjam
>>> import numpy as np
>>> compressed = cramjam.snappy.compress(b"bytes here")
>>> decompressed = cramjam.snappy.decompress(compressed)
>>> decompressed
cramjam.Buffer(len=10)  # an object which implements the buffer protocol
>>> bytes(decompressed)
b"bytes here"
>>> np.frombuffer(decompressed, dtype=np.uint8)
...
```

Sections: cramjam, Pure-Rust backend, CLI, libcramjam, Benchmarks

</details>

### cuda-toolkit

CUDA Toolkit meta-package

`pip install cuda-toolkit` · installs (wheel) · licence: not stated · rank 701 · last release 2026-11-04 · [PyPI](https://pypi.org/project/cuda-toolkit/) · [docs](https://docs.nvidia.com/cuda/)

<details><summary>README extract</summary>

> The NVIDIA CUDA Toolkit provides a development environment for creating high-performance, GPU-accelerated applications. With it, you can develop, optimize, and deploy your applications on GPU-accelerated embedded systems, desktop workstations, enterprise data centers, cloud-based platforms, and supercomputers. ...

Sections: cuda-toolkit 13.5.0, NVIDIA CUDA Toolkit, `cuda-toolkit` package, Using the `cuda-toolkit` package, Available extras

</details>

### cloudpathlib

pathlib-style classes for cloud storage services.

`pip install cloudpathlib` · installs (wheel) · licence: MIT License · rank 719 · last release 2026-10-02 · [PyPI](https://pypi.org/project/cloudpathlib/) · [docs](https://cloudpathlib.drivendata.org/) · [source](https://github.com/drivendataorg/cloudpathlib)

<details><summary>README extract</summary>

> Our goal is to be the meringue of file management libraries: the subtle sweetness of `pathlib` working in harmony with the ethereal lightness of the cloud.

A Python library with classes that mimic `pathlib.Path`'s interface for URIs from different cloud storage services.

Features:
- Familiar: If you know how to interact with `Path`, you know how to interact with `CloudPath`. All of the cloud-relevant `Path` methods are implemented.
 - Supported clouds: AWS S3, Google Cloud Storage, and Azure Blob Storage are implemented. ...

Example:
```python
from cloudpathlib import CloudPath

# dispatches to S3Path based on prefix
root_dir = CloudPath("s3://drivendata-public-assets/")
root_dir
# > S3Path('s3://drivendata-public-assets/')

...

</details>

### cssselect

cssselect parses CSS3 Selectors and translates them to XPath 1.0

`pip install cssselect` · installs (wheel) · licence: BSD-3-Clause · rank 788 · last release 2026-10-09 · [PyPI](https://pypi.org/project/cssselect/)

<details><summary>README extract</summary>

cssselect is a BSD-licensed Python library to parse CSS3 selectors and
translate them to XPath 1.0 expressions.

XPath 1.0 expressions can be used in lxml or another XPath engine to find
the matching elements in an XML or HTML document.

Find the cssselect online documentation at

Quick facts: ...

</details>

### cached-property

A decorator for caching properties in classes.

`pip install cached-property` · installs (wheel) · licence: BSD License · rank 827 · last release 2024-10-25 · [PyPI](https://pypi.org/project/cached-property/)

<details><summary>README extract</summary>

A decorator for caching properties in classes.

Features:
* Makes caching of time or computational expensive properties quick and easy.
* Because I got tired of copy/pasting this code from non-web project to non-web project.
* I needed something really simple that worked in Python 2 and 3. ...

Example:
```python
class Monopoly:

    def init(self):
        self.boardwalk_price = 500

    @property
    def boardwalk(self):
        # In reality, this might represent a database call or time
        # intensive task like calling a third-party API.
        self.boardwalk_price += 50
        return self.boardwalk_price
```

...

</details>

### ConfigArgParse

A drop-in replacement for argparse that allows options to also be set via config files and/or environment variables.

`pip install ConfigArgParse` · installs (wheel) · licence: MIT License · rank 833 · last release 2026-10-27 · [PyPI](https://pypi.org/project/ConfigArgParse/)

<details><summary>README extract</summary>

Features:
Applications with more than a handful of user-settable options are best
configured through a combination of command line args, config files,
hard-coded defaults, and in some cases, environment variables. ...

Example:
```python
import configargparse

p = configargparse.ArgParser(default_config_files=['/etc/app/conf.d/*.conf', '~/.my_settings'])
p.add('-c', '--my-config', required=True, is_config_file=True, help='config file path')
p.add('--genome', required=True, help='path to genome file')  # this option can be set in a config file because it starts with '--'
...
```

...

</details>

### cobble

Create data objects

`pip install cobble` · installs (wheel) · licence: BSD License · rank 948 · last release 2024-06-01 · [PyPI](https://pypi.org/project/cobble/)

<details><summary>README extract</summary>

Cobble is a Python library that allows easy creation of data objects,
including implementations of common methods such as `eq and _repr__`.

Example:
```python
import cobble

@cobble.data
class Song(object):
    name = cobble.field()
    artist = cobble.field()
    album = cobble.field(default=None)

song = Song("MFEO", artist="Jack's Mannequin")

print(song) # Prints "Song(name='MFEO', artist="Jack's Mannequin", album=None)"
```

Sections: Cobble, Examples

</details>

### cfn-lint

Checks CloudFormation templates for practices and behaviour that could potentially be improved

`pip install cfn-lint` · installs (wheel) · licence: MIT-0 · rank 990 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cfn-lint/) · [docs](https://github.com/aws-cloudformation/cfn-lint) · [source](https://github.com/aws-cloudformation/cfn-lint)

<details><summary>README extract</summary>

Validate AWS CloudFormation yaml/json templates against the AWS CloudFormation resource provider schemas and additional checks. Includes checking valid values for resource properties and best practices.

This is an attempt to provide validation for AWS CloudFormation templates properties and
their values. ...

Sections: AWS CloudFormation Linter, Warning, Serverless Application Model, Pip, Optional dependencies, Homebrew (macOS), Docker, Editor Plugins, GitHub Action, Online demo, Basic Usage, Exit Codes, Configuring Exit Codes, Specifying the template as an input stream

</details>

### cdp-use

Type safe generator/client library for CDP

`pip install cdp-use` · installs (wheel) · licence: MIT License · rank 1077 · last release 2026-02-22 · [PyPI](https://pypi.org/project/cdp-use/) · [source](https://github.com/browser-use/cdp-use)

<details><summary>README extract</summary>

A type-safe Python client generator for the Chrome DevTools Protocol (CDP). This library automatically generates Python bindings with full TypeScript-like type safety from the official CDP protocol specifications.

- 🔒 Type Safety: Full type hints with `TypedDict` classes for all CDP commands, parameters, and return types ...

Example:
```python
import asyncio
from cdp_use.client import CDPClient

async def main():
    # Connect to Chrome DevTools
    async with CDPClient("ws://localhost:9222/devtools/browser/...") as cdp:
        # Get all browser targets with full type safety
        targets = await cdp.send.Target.getTargets()
...
```

...

</details>

### contextlib2

Backports and enhancements for the contextlib module

`pip install contextlib2` · installs (wheel) · licence: Apache Software License; Python Software Foundation License · rank 1194 · last release 2021-06-27 · [PyPI](https://pypi.org/project/contextlib2/)

<details><summary>README extract</summary>

contextlib2 is a backport of the standard library's contextlib
module to
earlier Python versions.

It also sometimes serves as a real world proving ground for possible future
enhancements to the standard library version. ...

Sections: Licensing, Updating to a new stdlib reference version

</details>

### colorful

Terminal string styling done right, in Python.

`pip install colorful` · installs (wheel) · licence: MIT License · rank 1223 · last release 2025-10-29 · [PyPI](https://pypi.org/project/colorful/)

<details><summary>README extract</summary>

Terminal string styling done right, in Python :tada:

Features:
* expressive and consistent API (docs)
* support for different color modes (8 ANSI, 256 ANSI, true colors) (docs)
* support for predefined awesome styles (solarized, ...) (docs)
* support for custom color palettes (docs)
* support nesting styles ...

Example:
```python
import colorful as cf

print(cf.italic_coral_on_beige('Hello World'))
print(cf.italic & cf.coral_on_beige | 'Hello World')
print('{c.italic_coral_on_beige}Hello World{c.reset}'.format(c=cf))
```

...

</details>

### cloud-sql-python-connector

Google Cloud SQL Python Connector library

`pip install cloud-sql-python-connector` · installs (wheel) · licence: Apache-2.0 · rank 1245 · last release 2026-10-15 · [PyPI](https://pypi.org/project/cloud-sql-python-connector/) · [source](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector.git)

<details><summary>README extract</summary>

[][colab-notebook]
[][ci-build]
[][pypi-docs]
[][pypi-docs]
[][pypi-docs]

The _Cloud SQL Python Connector is a Cloud SQL connector designed for use with the
Python language. Using a Cloud SQL connector provides a native alternative to the
Cloud SQL Auth Proxy while
providing the following benefits: ...

Example:
```python
from google.cloud.sql.connector import Connector
import sqlalchemy

# initialize Connector object
connector = Connector()

# initialize SQLAlchemy connection pool with Connector
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=lambda: connector.connect(
        "project:region:instance",
        "pymysql",
...
```

...

</details>

### coolname

Random name and slug generator

`pip install coolname` · installs (wheel) · licence: BSD-2-Clause · rank 1279 · last release 2026-04-23 · [PyPI](https://pypi.org/project/coolname/) · [docs](https://coolname.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Do you want random human-readable strings?

Features:
* Generate slugs, ready to use, Django-compatible.

 .. code-block:: python

 >>> from coolname import generate_slug
 >>> generate_slug()
 'qualified-agama-of-absolute-kindness'

* Generate names as sequences and do whatever you want with them.

 .. ...

Example:
```python
>>> from coolname import generate_slug
>>> generate_slug()
'tiny-optimal-crocodile-of-progress'
>>> generate_slug()
'cherubic-leopard-of-delightful-serendipity'
>>> generate_slug()
'wealthy-athletic-swift-of-tempest'
```

Sections: Random Name and Slug Generator, Features

</details>

### constructs

A programming model for software-defined state

`pip install constructs` · installs (wheel) · licence: OSI Approved · rank 1353 · last release 2026-08-03 · [PyPI](https://pypi.org/project/constructs/) · [source](https://github.com/aws/constructs.git)

<details><summary>README extract</summary>

> Software-defined persistent state

Constructs are classes which define a "piece of system state". Constructs can be composed together to form higher-level building blocks which represent more complex state.

Constructs are often used to represent the *desired state* of cloud applications. ...

Sections: Constructs, What are constructs?

</details>

### chromadb

Chroma.

`pip install chromadb` · installs (wheel) · licence: Apache Software License · rank 1390 · last release 2026-05-05 · [PyPI](https://pypi.org/project/chromadb/)

<details><summary>README extract</summary>

Chroma - the open-source data infrastructure for AI.



 Docs

 Homepage

Our hosted service, Chroma Cloud, powers serverless vector, hybrid, and full-text search. It's extremely fast, cost-effective, scalable and painless. Create a DB and try it out in under 30 seconds with $5 of free credits.

Get started with Chroma Cloud

Example:
```python
import chromadb
# setup Chroma in-memory, for easy prototyping. Can add persistence easily!
client = chromadb.Client()

# Create collection. get_collection, get_or_create_collection, delete_collection also available!
collection = client.create_collection("all-my-documents")

...
```

Sections: Chroma Cloud, API, Get involved

</details>

### cloudevents

CloudEvents Python SDK

`pip install cloudevents` · installs (wheel) · licence: Apache-2.0 · rank 1392 · last release 2026-06-11 · [PyPI](https://pypi.org/project/cloudevents/) · [docs](https://cloudevents.io) · [source](https://github.com/cloudevents/sdk-python)

<details><summary>README extract</summary>

Example:
```python
from cloudevents.core.v1.event import CloudEvent
from cloudevents.core.bindings.http import to_binary_event
import requests

# Create a CloudEvent
# - The CloudEvent "id" is generated if omitted. "specversion" defaults to "1.0".
attributes = {
  "type": "com.example.sampletype1",
  "source": "
}
data = {"message": "Hello World!"}
...
```

Sections: Python SDK v2 for CloudEvents, Python SDK, Sending CloudEvents, Binary HTTP CloudEvent, Structured HTTP CloudEvent, Receiving CloudEvents, SDK versioning, Additional SDK Resources, Maintenance

</details>

### cel-python

Pure Python implementation of Google Common Expression Language

`pip install cel-python` · installs (wheel) · licence: not stated · rank 1399 · last release 2026-01-31 · [PyPI](https://pypi.org/project/cel-python/)

<details><summary>README extract</summary>

Pure Python implementation of Google Common Expression Language,

 The Common Expression Language (CEL) implements common semantics for expression evaluation,
 enabling different applications to more easily interoperate.

 Key Applications ...

Example:
```python
>>> import celpy

# A list of type names and class bindings used to create an environment.
>>> types = []
>>> env = celpy.Environment(types)

# Parse the code to create the CEL AST.
>>> ast = env.compile("355. / 113.")

# Use the AST and any overriding functions to create an executable program.
>>> functions = {}
...
```

Sections: cel-python, re2, Command Line, Library, Notes, Example 2, Example 3

</details>

### configparser

Updated configparser from stdlib for earlier Pythons.

`pip install configparser` · installs (wheel) · licence: MIT · rank 1403 · last release 2026-10-22 · [PyPI](https://pypi.org/project/configparser/) · [source](https://github.com/jaraco/configparser)

<details><summary>README extract</summary>

This package is a backport of the refreshed and enhanced ConfigParser from
later Python versions. To use the backport instead of the built-in version,
simply import it explicitly as a backport:
For detailed documentation consult the vanilla version at ...

Example:
```python
from backports import configparser
```

Sections: Versioning, Maintenance, Conversion Process, For Enterprise

</details>

### click-default-group

click_default_group

`pip install click-default-group` · installs (wheel) · licence: Public Domain · rank 1458 · last release 2023-08-04 · [PyPI](https://pypi.org/project/click-default-group/) · [source](https://github.com/click-contrib/click-default-group)

<details><summary>README extract</summary>

`DefaultGroup` is a sub class of `click.Group`. But it invokes a default
subcommand instead of showing a help message when a subcommand is not passed.

Usage

Define a default subcommand by `default=NAME`:

Then you can invoke that without explicit subcommand name:

Compatibility

`click-default-group` is compatible with these Click versions: ...

Example:
```python
import click
from click_default_group import DefaultGroup

@click.group(cls=DefaultGroup, default='foo', default_if_no_args=True)
def cli():
    pass

@cli.command()
def foo():
    click.echo('foo')

@cli.command()
def bar():
    click.echo('bar')
```

</details>

### cachelib

A collection of cache libraries in the same API interface.

`pip install cachelib` · installs (wheel) · licence: BSD-3-Clause · rank 1546 · last release 2026-08-24 · [PyPI](https://pypi.org/project/cachelib/) · [docs](https://cachelib.readthedocs.io) · [source](https://github.com/pallets-eco/cachelib/)

<details><summary>README extract</summary>

A collection of cache libraries in the same API interface. Extracted from
Werkzeug.

Supported backends include:

- DynamoDbCache (DynamoDB)
- FileSystemCache (file based)
- MemcachedCache (Memcached)
- MongoDbCache (MongoDB)
- RedisCache (Redis)
- SimpleCache (in-memory, single-process)
- UWSGICache (uWSGI)
- ValkeyCache (Valkey) ...

Example:
```python
from cachelib import SimpleCache

# Create a cache instance
cache = SimpleCache()

# Set a value in the cache
cache.set("my_key", "my_value")

# Retrieve the value from the cache
value = cache.get("my_key")
print(value)  # Output: my_value

# Delete the value from the cache
cache.delete("my_key")

# Try to retrieve the deleted value
...
```

Sections: CacheLib, Pallets Ecosystem, A Minimal Example

</details>

### circuitbreaker

Python Circuit Breaker pattern implementation

`pip install circuitbreaker` · installs (wheel) · licence: BSD License · rank 1547 · last release 2025-03-31 · [PyPI](https://pypi.org/project/circuitbreaker/)

<details><summary>README extract</summary>

This is a Python implementation of the "Circuit Breaker" Pattern (
Inspired by Michael T. Nygard's highly recommendable book *Release It!* (

Example:
```python
from circuitbreaker import circuit

@circuit
def external_call():
    ...
```

Sections: CircuitBreaker, Usage, What does *failure* mean?, Get specific about the expected failure, Configuration, failure threshold, recovery timeout, expected exception, name, fallback function, Advanced Usage, Monitoring

</details>

### crc32c

A python package implementing the crc32c algorithm in hardware and software

`pip install crc32c` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 1607 · last release 2026-09-11 · [PyPI](https://pypi.org/project/crc32c/) · [source](https://github.com/ICRAR/crc32c)

_README extract left out: share-alike licence._

### ckzg

Python bindings for C-KZG-4844

`pip install ckzg` · installs (wheel) · licence: Apache-2.0 · rank 1704 · last release 2026-07-09 · [PyPI](https://pypi.org/project/ckzg/)

<details><summary>README extract</summary>

This directory contains Python bindings for the C-KZG-4844 library.

These bindings require `python3`, `PyYAML` and `make`.

Everything is consolidated into one command:

You should expect to see these messages at the bottom:

Sections: Python Bindings for the C-KZG Library, Prerequisites, Build & test

</details>

### codeowners

Codeowners parser for Python

`pip install codeowners` · installs (wheel) · licence: MIT · rank 1711 · last release 2026-06-28 · [PyPI](https://pypi.org/project/codeowners/) · [source](https://github.com/sbdchd/codeowners)

<details><summary>README extract</summary>

> Python codeowners parser based on softprops's Rust
> library and hmarr's Go
> library.

Features:
To allow Python users to parse codeowners
files
in Python.

Example:
```python
from codeowners import CodeOwners

example_file = """\
# owners for js files
*.js    @ghost
# python
*.py user@example.com
# misc
/build/logs/ @dmin
docs/*  docs@example.com
"""

owners = CodeOwners(example_file)
assert owners.of("test.js") ==  [('USERNAME', '@ghost')]
```

Sections: codeowners, Why?, Usage, Dev, Releasing a New Version

</details>

### cligj

Click params for commmand line interfaces to GeoJSON

`pip install cligj` · installs (wheel) · licence: BSD · rank 1754 · last release 2021-05-28 · [PyPI](https://pypi.org/project/cligj/)

<details><summary>README extract</summary>

Common arguments and options for GeoJSON processing commands, using Click.

`cligj` is for Python developers who create command line interfaces for geospatial data.
`cligj` allows you to quickly build consistent, well-tested and interoperable CLIs for handling GeoJSON.

`files_in_arg`
Multiple files ...

Features:
`sequence_opt`

`use_rs_opt`

Example:
```python
import click
import cligj
import json

def process_features(features):
    for feature in features:
        # TODO process feature here
        yield feature

@click.command()
@cligj.features_in_arg
@cligj.sequence_opt
@cligj.use_rs_opt
def pass_features(features, sequence, use_rs):
    if sequence:
...
```

...

</details>

### choreographer

Devtools Protocol implementation for chrome.

`pip install choreographer` · installs (wheel) · licence: MIT · rank 1788 · last release 2026-09-16 · [PyPI](https://pypi.org/project/choreographer/) · [source](https://github.com/plotly/choreographer)

<details><summary>README extract</summary>

choreographer allows remote control of browsers from Python.
It was created to support image generation from browser-based charting tools,
but can be used for other purposes as well.

choreographer is available PyPI and github.

Kaleido is a cross-platform library for generating static images of
plots. ...

Example:
```python
import asyncio
import choreographer as choreo

async def example():
    browser = await choreo.Browser(headless=False)
    tab = await browser.create_tab("
    await asyncio.sleep(3)
    await tab.send_command("Page.navigate", params={"url": "
    await asyncio.sleep(3)

if name == "main":
    asyncio.run(example())
```

...

</details>

### clarabel

Clarabel Conic Interior Point Solver for Rust / Python

`pip install clarabel` · installs (wheel) · licence: Apache-2.0 · rank 1819 · last release 2025-06-11 · [PyPI](https://pypi.org/project/clarabel/) · [source](https://github.com/oxfordcontrol/Clarabel.rs)

<details><summary>README extract</summary>

Features •
 Installation •
 License •
 Documentation

Clarabel.rs is a Rust implementation of an interior point numerical solver for convex optimization problems using a novel homogeneous embedding. Clarabel.rs solves the following problem: ...

Features:
* Versatile: Clarabel.rs solves linear programs (LPs), quadratic programs (QPs), second-order cone programs (SOCPs) and semidefinite programs (SDPs). It also solves problems with exponential, power cone and generalized power cone constraints. ...

Sections: Interior Point Conic Optimization for Rust and Python, Features, Citing

</details>

### cvxpy

A domain-specific language for modeling convex optimization problems in Python.

`pip install cvxpy` · installs (wheel) · licence: Apache-2.0 · rank 1834 · last release 2026-09-19 · [PyPI](https://pypi.org/project/cvxpy/)

<details><summary>README extract</summary>

The CVXPY documentation is at cvxpy.org.

*We are building a CVXPY community on Discord. Join the conversation! For issues and long-form discussions, use Github Issues and Github Discussions.*

Contents
- Installation
- Getting started
- Issues
- Community
- Contributing
- Team
- Citing ...

Example:
```python
import cvxpy as cp
import numpy

# Problem data.
m = 30
n = 20
numpy.random.seed(1)
A = numpy.random.randn(m, n)
b = numpy.random.randn(m)

# Construct the problem.
x = cp.Variable(n)
objective = cp.Minimize(cp.sum_squares(A @ x - b))
constraints = [0 <= x, x <= 1]
prob = cp.Problem(objective, constraints)

...
```

Sections: CVXPY, Getting started, Issues, Team, Citing

</details>

### channels-redis

Redis-backed ASGI channel layer implementation

`pip install channels-redis` · installs (wheel) · licence: BSD · rank 1881 · last release 2025-07-22 · [PyPI](https://pypi.org/project/channels-redis/)

<details><summary>README extract</summary>

Provides Django Channels channel layers that use Redis as a backing store.

There are two available implementations:

* `RedisChannelLayer` is the original layer, and implements channel and group
 handling itself.
* `RedisPubSubChannelLayer` is newer and leverages Redis Pub/Sub for message
 dispatch. ...

Example:
```python
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
            "channel_capacity": {
                "http.request": 200,
                "http.response!*": 10,
                re.compile(r"^websocket.send\!.+"): 20,
            },
...
```

...

</details>

### celery-types

Type stubs for Celery and its related packages

`pip install celery-types` · installs (wheel) · licence: Apache-2.0 · rank 1895 · last release 2026-03-12 · [PyPI](https://pypi.org/project/celery-types/) · [source](https://github.com/sbdchd/celery-types)

<details><summary>README extract</summary>

Type stubs for celery related projects:

- `celery`
- `django-celery-results`
- `amqp`
- `kombu`
- `billiard`
- `vine`
- `ephem`

Sections: celery-types, dev, initial setup, pre-commit, tooling, related

</details>

### cloudsplaining

AWS IAM Security Assessment tool that identifies violations of least privilege and generates a risk-prioritized HTML report

`pip install cloudsplaining` · installs (wheel) · licence: MIT · rank 1964 · last release 2026-06-14 · [PyPI](https://pypi.org/project/cloudsplaining/) · [docs](https://cloudsplaining.readthedocs.io/) · [source](https://github.com/salesforce/cloudsplaining)

<details><summary>README extract</summary>

Cloudsplaining

Cloudsplaining is an AWS IAM Security Assessment tool that identifies violations of least privilege and generates a risk-prioritized HTML report.

* Example report


For full documentation, please visit the project on ReadTheDocs.

* Installation
* Cheatsheet
* Example report

Features:
Cloudsplaining identifies violations of least privilege in AWS IAM policies and generates a pretty HTML report. It can scan all the policies in your AWS account, across multiple AWS accounts, or it can scan a single policy file. ...

...

</details>

### compressed-tensors

Library for utilization of compressed safetensors of neural network models

`pip install compressed-tensors` · installs (wheel) · licence: Apache 2.0 · rank 1992 · last release 2026-10-28 · [PyPI](https://pypi.org/project/compressed-tensors/)

<details><summary>README extract</summary>

The `compressed-tensors` library extends the safetensors format, providing a versatile and efficient way to store and manage compressed tensor data. This library supports various compression schemes, making it a unified format for handling models compressed with algorithms like GPTQ, AWQ, SmoothQuant, and SparseGPT, across formats like INT8, FP8, ...

Features:
As model compression becomes increasingly important for efficient deployment of LLMs, the landscape of quantization and compression techniques has become increasingly fragmented. ...

Example:
```python
import math

import torch
from transformers import AutoModelForCausalLM

from compressed_tensors.compressors import ModelCompressor
from compressed_tensors.offload import update_offload_parameter
...

</details>

### cssbeautifier

CSS unobfuscator and beautifier.

`pip install cssbeautifier` · installs (wheel) · licence: MIT · rank 2003 · last release 2026-06-30 · [PyPI](https://pypi.org/project/cssbeautifier/)

### check-jsonschema

A jsonschema CLI and pre-commit hook

`pip install check-jsonschema` · installs (wheel) · licence: Apache Software License · rank 2023 · last release 2026-10-26 · [PyPI](https://pypi.org/project/check-jsonschema/)

<details><summary>README extract</summary>

[][pypi]
[][pypi]

[][docs]

[][docs]

A JSON Schema CLI and pre-commit hook built on jsonschema.
The schema may be specified as a local or remote (HTTP or HTTPS) file.

Remote files are automatically downloaded and cached if possible.

Sections: check-jsonschema, Usage, Example pre-commit config, Project Information

</details>

### Cerberus

Lightweight, extensible schema and data validation tool for Pythondictionaries.

`pip install Cerberus` · installs (wheel) · licence: ISC License (ISCL) · rank 2056 · last release 2025-11-06 · [PyPI](https://pypi.org/project/Cerberus/) · [docs](http://docs.python-cerberus.org) · [source](https://github.com/pyeve/cerberus)

<details><summary>README extract</summary>

Cerberus is a lightweight and extensible data validation library for Python.

Features:
Cerberus provides type checking and other base functionality out of the box and
is designed to be non-blocking and easily and widely extensible, allowing for
custom validation. It has no dependencies, but has the potential to become
yours.

Example:
```python
>>> v = Validator({'name': {'type': 'string'}})
>>> v.validate({'name': 'john doe'})
True
```

Sections: Cerberus, Features, Documentation, Copyright

</details>

### commitizen

Python commitizen client tool

`pip install commitizen` · installs (wheel) · licence: MIT · rank 2136 · last release 2026-10-24 · [PyPI](https://pypi.org/project/commitizen/) · [docs](https://commitizen-tools.github.io/commitizen/) · [source](https://github.com/commitizen-tools/commitizen)

<details><summary>README extract</summary>

Commitizen Documentation Site

Commitizen is a powerful release management tool that helps teams maintain consistent and meaningful commit messages while automating version management.

By enforcing standardized commit conventions (defaulting to Conventional Commits), Commitizen helps teams:

- Write clear, structured commit messages ...

Features:
- Interactive CLI for standardized commits with default Conventional Commits support
- Intelligent version bumping using Semantic Versioning
- Automatic keep a changelog generation
- Built-in commit validation with pre-commit hooks ...

...

</details>

### capstone

Capstone disassembly engine

`pip install capstone` · installs (wheel) · licence: BSD License · rank 2153 · last release 2026-05-28 · [PyPI](https://pypi.org/project/capstone/)

<details><summary>README extract</summary>

To install Capstone, you should run `pip install capstone`.

If you would like to build Capstone with just the source distribution, without
pip, just run `python setup.py install` in the folder with setup.py in it.

In order to use this source distribution, you will need an environment that can
compile C code. ...

</details>

### clerk-backend-api

Python Client SDK for clerk.dev

`pip install clerk-backend-api` · installs (wheel) · licence: not stated · rank 2241 · last release 2026-11-02 · [PyPI](https://pypi.org/project/clerk-backend-api/) · [source](https://github.com/clerk/clerk-sdk-python.git)

<details><summary>README extract</summary>

The most comprehensive User Management Platform

Clerk Backend API: The Clerk REST Backend API, meant to be accessed by backend servers.

When the API changes in a way that isn't compatible with older versions, a new version is released.
Each version is identified by its release date, e.g. `2025-04-10`. ...

Example:
```python
# !/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
# "clerk-backend-api",
# ]
# ///

from clerk_backend_api import Clerk

sdk = Clerk(
  # SDK arguments
)

# Rest of script here...
```

Sections: Summary, Versions, uv, PIP, Poetry, Shell and script usage with `uv`, PyCharm, SDK Example Usage, Example, Authentication, Request Authentication, Authenticating Machine Tokens, Available Resources and Operations, ActorTokens

</details>

### click-aliases

Add (mutiple) aliases to a click group or command

`pip install click-aliases` · installs (wheel) · licence: MIT License · rank 2248 · last release 2026-07-09 · [PyPI](https://pypi.org/project/click-aliases/)

<details><summary>README extract</summary>

Add (multiple) aliases to a click group or command.

In your click app:

Will result in:

Example:
```python
import click
from click_aliases import ClickAliasedGroup

@click.group(cls=ClickAliasedGroup)
def cli():
    pass

@cli.command(aliases=['bar', 'baz', 'qux'])
def foo():
    """Run a command."""
    click.echo('foo')
```

</details>

### cadquery-ocp

Python wrapper for Open CASCADE Technology 3D geometry library based on the official CadQuery/OCP sources

`pip install cadquery-ocp` · installs (wheel) · licence: Apache Software License · rank 2355 · last release 2026-10-05 · [PyPI](https://pypi.org/project/cadquery-ocp/)

<details><summary>README extract</summary>

Python wrapper for OCCT generated using pywrap. Typing stubs available from pypi.

* Provide thin bindings to OCCT.
* Wrap all OCCT modules (if practical).
* React quickly to new OCCT releases.
* Cater primarily for the CadQuery project.

* Provide additional functionality not present in OCCT

Sections: cadquery-ocp (also known as OCP), Goals of OCP, Non-goals

</details>

### casbin

An authorization library that supports access control models like ACL, RBAC, ABAC in Python

`pip install casbin` · installs (wheel) · licence: Apache Software License · rank 2372 · last release 2025-05-10 · [PyPI](https://pypi.org/project/casbin/)

<details><summary>README extract</summary>

Sponsored by

 Build auth with fraud prevention, faster.
 Try Stytch for API-first authentication, user & org management, multi-tenant SSO, MFA, device fingerprinting, and more.

💖 Looking for an open-source identity and access management solution like Okta, Auth0, Keycloak ? Learn more about: Casdoor ...

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

### css-inline

High-performance library for inlining CSS into HTML 'style' attributes

`pip install css-inline` · installs (wheel) · licence: MIT License · rank 2436 · last release 2026-10-27 · [PyPI](https://pypi.org/project/css-inline/) · [source](https://github.com/Stranger6667/css-inline)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](

`css_inline` is a high-performance library for inlining CSS into HTML 'style' attributes.

Use it to prepare HTML emails or to embed HTML into third-party web pages.

It turns this HTML:

into:

- Uses components from Mozilla's Servo project ...

Example:
```python
import css_inline

HTML = """

    h1 { color:blue; }

# Big Text

"""

inlined = css_inline.inline(HTML)

# Big Text
```

Sections: css_inline, Playground, Usage, Configuration, Errors, XHTML compatibility, Performance, Comparison with other libraries, Further reading

</details>

### cadquery-ocp-proxy

Proxy package to track cadquery_ocp / cadquery_ocp_novtk version

`pip install cadquery-ocp-proxy` · installs (wheel) · licence: Apache Software License · rank 2454 · last release 2026-10-05 · [PyPI](https://pypi.org/project/cadquery-ocp-proxy/)

<details><summary>README extract</summary>

There is a proxy package `cadquery_ocp_proxy` with version `8.0.0.0` that does nothing, but have optional dependencies:

I built the following packages using the proxy package for testing on my local pypi server. ...

Example:
```python
try:
    import OCP
except ImportError:
    print("If you only want to use build123d, install 'build123d[novtk]'")
    print("When cadquery should also be installed, install 'build123d[vtk]'")
```

Sections: TEST SETUP, WORKFLOWS, Caveats, Forgetting `[vtk]` or `novtk`, Summary

</details>

### comfyui-workflow-templates

ComfyUI workflow templates package

`pip install comfyui-workflow-templates` · installs (wheel) · licence: MIT · rank 2473 · last release 2026-11-05 · [PyPI](https://pypi.org/project/comfyui-workflow-templates/)

<details><summary>README extract</summary>

This repo hosts the official ComfyUI workflow templates and subgraph blueprints.

Features:
| Content | Description | Location |

| Workflow Templates | Full standalone workflows for the template picker | `templates/`, `packages/` |
| Subgraph Blueprints | Reusable node components that appear in the node palette | `blueprints/`, ...

Sections: workflow_templates, Overview, Template Site (`site/`), Deployment Environments, Quick Start, Adding New Templates, 1 — Find Templates Folder, 2 — Obtain Workflow, 3 — Obtain Thumbnails, 4 — Choose Thumbnail Type, 5 — Compress Assets, 6 — Rename and Move Files, 7 — Assign Bundle & Sync Assets, 8 — Add Entry to `index.json`

</details>

### comfyui-workflow-templates-core

Core helpers for ComfyUI workflow templates

`pip install comfyui-workflow-templates-core` · installs (wheel) · licence: MIT · rank 2499 · last release 2026-11-05 · [PyPI](https://pypi.org/project/comfyui-workflow-templates-core/)

### comfyui-workflow-templates-json

Workflow template JSON definitions for ComfyUI

`pip install comfyui-workflow-templates-json` · installs (wheel) · licence: MIT · rank 2502 · last release 2026-11-05 · [PyPI](https://pypi.org/project/comfyui-workflow-templates-json/)

<details><summary>README extract</summary>

Workflow template JSON definitions for ComfyUI.

</details>

### commentjson

Add Python and JavaScript style comments in your JSON files.

`pip install commentjson` · installs from source (sdist only) · licence: not stated · rank 2527 · last release 2020-10-05 · [PyPI](https://pypi.org/project/commentjson/)

<details><summary>README extract</summary>

`commentjson` (Comment JSON) is a Python package that helps you create JSON
files with Python and JavaScript style inline comments. Its API is very similar
to the Python standard library's json module.

Example:
```python
>>> import commentjson
>>>
>>> json_string = """{
...     "name": "Vaidik Kapoor", # Person's name
...     "location": "Delhi, India", // Person's location
...
...     # Section contains info about
...     // person's appearance
...     "appearance": {
...         "hair_color": "black",
...         "eyes_color": "black",
...         "height": "6"
...
```

Sections: commentjson, Basic Usage, Documentation, Tests

</details>

### click-spinner

Spinner for Click

`pip install click-spinner` · installs (wheel) · licence: MIT · rank 2535 · last release 2026-06-23 · [PyPI](https://pypi.org/project/click-spinner/)

<details><summary>README extract</summary>

Sometimes you would just like to show the user some progress,
but a progress bar is not suitable because you don’t know how much longer it would take.
In these cases you might want to display a simple spinner using the `spinner()` function.

Example usage:

It looks like this:

Spinner class based on on a gist by @cevaris.

Introduced in PR #649.

Example:
```python
with click_spinner.spinner():
        do_something()
        do_something_else()
```

</details>

### comfyui-workflow-templates-media-assets-02

Media assets bundle 02 for ComfyUI workflow templates

`pip install comfyui-workflow-templates-media-assets-02` · installs (wheel) · licence: MIT · rank 2537 · last release 2026-11-05 · [PyPI](https://pypi.org/project/comfyui-workflow-templates-media-assets-02/)

<details><summary>README extract</summary>

Media assets bundle 02 for ComfyUI workflow templates.

</details>

### crewai

Cutting-edge framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

`pip install crewai` · does not install on CPython 3.14 · licence: not stated · rank 2551 · last release 2026-11-07 · [PyPI](https://pypi.org/project/crewai/) · [docs](https://docs.crewai.com) · [source](https://github.com/crewAIInc/crewAI)

<details><summary>README extract</summary>

Homepage
 Docs
 Start Cloud Trial
 Blog
 Forum

> CrewAI is a lean, lightning-fast Python framework built entirely from scratch—completely independent of LangChain or other agent frameworks.
> It empowers developers with both high-level simplicity and precise low-level control, ideal for creating autonomous AI agents tailored to any scenario. ...

Features:
CrewAI unlocks the true potential of multi-agent automation, delivering the best-in-class combination of speed, flexibility, and control with either Crews of AI Agents or Flows of Events: ...

Example:
```python
from crewai.flow.flow import Flow, listen, start, router, or
from crewai import Crew, Agent, Task, Process
from pydantic import BaseModel

# Define structured state for precise control
class MarketState(BaseModel):
...

</details>

### comfyui-frontend-package

(no summary)

`pip install comfyui-frontend-package` · installs (wheel) · licence: not stated · rank 2561 · last release 2026-11-05 · [PyPI](https://pypi.org/project/comfyui-frontend-package/)

### comfy-kitchen

Fast Kernel Library for ComfyUI with multiple compute backends

`pip install comfy-kitchen` · installs (wheel) · licence: Apache Software License · rank 2565 · last release 2026-11-05 · [PyPI](https://pypi.org/project/comfy-kitchen/)

<details><summary>README extract</summary>

Fast kernel library for Diffusion inference with multiple compute backends.

| Function | eager | cuda | triton | hip | ascend |

| `quantize_per_tensor_fp8` | ✓ | ✓ | ✓ | ✓ | |
| `dequantize_per_tensor_fp8` | ✓ | ✓ | ✓ | ✓ | |
| `stochastic_rounding_fp8` | ✓ | ✓ | | ✓ | |
| `quantize_nvfp4` | ✓ | ✓ | ✓ | | |
| `dequantize_nvfp4` | ✓ | ✓ | ✓ | | ...

Example:
```python
import comfy_kitchen as ck
import torch

# Automatic backend selection (hip -> cuda -> triton -> eager)
x = torch.randn(100, 100, device="cuda")
scale = torch.tensor([1.0], device="cuda")
result = ck.quantize_per_tensor_fp8(x, scale)

# Check which backends are available
print(ck.list_backends())

# Force a specific backend
...
```

...

</details>

### checkdigit

A check digit library for data validation

`pip install checkdigit` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 2600 · last release 2023-04-09 · [PyPI](https://pypi.org/project/checkdigit/) · [docs](https://checkdigit.rtfd.io) · [source](https://github.com/harens/checkdigit)

_README extract left out: share-alike licence._

### clickclick

Click utility functions

`pip install clickclick` · installs (wheel) · licence: Apache Software License · rank 2610 · last release 2020-10-03 · [PyPI](https://pypi.org/project/clickclick/)

<details><summary>README extract</summary>

Utility functions (Python 3 only) for the wonderful Click library.
Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary.

Example:
```python
from clickclick import Action, OutputFormat

with Action('Performing remote call..') as act:
    do_something()
    act.progress()
    do_something_else()

output_format = 'json' # default: "text"
with OutputFormat(output_format):
    print_table(['col1', 'col2'], rows)
```

Sections: Click Click, Usage, Working Example

</details>

### capi-param-builder-python

Parameter builder SDK for Conversion API events

`pip install capi-param-builder-python` · installs (wheel) · licence: LICENSE.txt · rank 2612 · last release 2026-09-16 · [PyPI](https://pypi.org/project/capi-param-builder-python/)

### columnar

A tool for printing data in a columnar format.

`pip install columnar` · installs (wheel) · licence: MIT License · rank 2740 · last release 2021-12-27 · [PyPI](https://pypi.org/project/columnar/)

<details><summary>README extract</summary>

A library for creating columnar output strings using data as input.

Example:
```python
from columnar import columnar
from click import style

data = [
    ['Strade Bianche', 'Saturday 9th March', 'Tuscany, Italy', "Men's - 176km / Women's - 103km. Both men's and women's "],
    ['Omloop Het Nieuwsblad', 'Saturday 2nd March', 'Gent, Belgium', "Men's - 200km / Women's - 130km"],
...
```

Sections: Columnar, Examples, Patterns, Selecting Columns, Dropping Columns, Column Sizing Algorithm, Text Wrapping, API, `columnar()` Arguments, `data`, `headers=None`, `patterns=[]`, `drop=[]`, `select=[]`

</details>

### clr_loader

Generic pure Python loader for .NET runtimes

`pip install clr_loader` · installs (wheel) · licence: not stated · rank 2827 · last release 2026-04-18 · [PyPI](https://pypi.org/project/clr_loader/) · [docs](https://pythonnet.github.io/clr-loader/)

<details><summary>README extract</summary>

Implements a generic interface for loading one of the CLR (.NET) runtime
implementations and calling simple functions on them.

Documentation is available at

</details>

### comfyui-embedded-docs

Embedded documentation for ComfyUI nodes

`pip install comfyui-embedded-docs` · installs (wheel) · licence: GPL-3.0 · rank 2881 · last release 2026-11-03 · [PyPI](https://pypi.org/project/comfyui-embedded-docs/) · [source](https://github.com/Comfy-Org/embedded-docs)

_README extract left out: share-alike licence._

### composio-client

The official Python library for the Composio API, generated from the v3.1 OpenAPI spec with hey-api

`pip install composio-client` · installs (wheel) · licence: Apache-2.0 · rank 2929 · last release 2026-11-05 · [PyPI](https://pypi.org/project/composio-client/) · [source](https://github.com/ComposioHQ/composio-client)

<details><summary>README extract</summary>

Sync and async clients for the Composio v3.1 API, with typed request fields and Pydantic responses.
Python 3.10 or newer is required.

Upgrading from Stainless 1.43 requires explicit authentication and the
other changes in the migration guide.

Example:
```python
from composio_client import Composio, ProjectAuth

client = Composio(auth=ProjectAuth("ak..."))

session = client.tool_router.session.create(user_id="user@example.com")
result = client.tool_router.session.execute(
    session.session_id,
    tool_slug="GITHUB_CREATE_ISSUE",
...
```

...

</details>

### composio

SDK for integrating Composio with your applications.

`pip install composio` · installs (wheel) · licence: Apache Software License · rank 3000 · last release 2026-11-03 · [PyPI](https://pypi.org/project/composio/)

<details><summary>README extract</summary>

Composio gives your AI agents 1000+ pre-authenticated toolkits, per-user sessions, authentication, triggers, and a sandbox. This package is the Python SDK.

- Documentation
- Quickstart
- Changelog
- Dashboard (grab your `COMPOSIO_API_KEY` from Settings)

Example:
```python
from composio import Composio

composio = Composio()  # reads COMPOSIO_API_KEY, or pass api_key=...

session = composio.create(user_id="user_123")
tools = session.tools()  # OpenAI-format tool definitions by default
```

Sections: Composio Python SDK, Quickstart, Use with an agent framework, MCP, Authentication, Triggers

</details>

### chroma-hnswlib

Chromas fork of hnswlib

`pip install chroma-hnswlib` · installs from source (sdist only) · licence: not stated · rank 3001 · last release 2024-07-22 · [PyPI](https://pypi.org/project/chroma-hnswlib/)

### copier

A library for rendering project templates.

`pip install copier` · installs (wheel) · licence: MIT License · rank 3026 · last release 2026-10-13 · [PyPI](https://pypi.org/project/copier/) · [source](https://github.com/copier-org/copier)

<details><summary>README extract</summary>

A library and CLI app for rendering project templates.

- Works with local paths and Git URLs.
- Your project can include any file and Copier can dynamically replace values in any
 kind of text file.
- It generates a beautiful output and takes care of not overwriting existing files
 unless instructed to do so.

Example:
```python
from copier import run_copy

# Create a project from a local path
run_copy("path/to/project/template", "path/to/destination")

# Or from a Git URL.
run_copy(" "path/to/destination")

# You can also use "gh:" as a shortcut of "
run_copy("gh:copier-org/copier.git", "path/to/destination")

# Or "gl:" as a shortcut of "
...
```

Sections: Homebrew formula, Quick start, Basic concepts, Browse or tag public templates

</details>

### crewai-core

Shared utilities for CrewAI — version, paths, user-data, telemetry, printer.

`pip install crewai-core` · does not install on CPython 3.14 · licence: not stated · rank 3045 · last release 2026-11-07 · [PyPI](https://pypi.org/project/crewai-core/) · [docs](https://docs.crewai.com) · [source](https://github.com/crewAIInc/crewAI)

<details><summary>README extract</summary>

Shared utilities used by both `crewai` and `crewai-cli`: version lookup, storage
paths, user-data helpers, telemetry, and the printer.

This package is a leaf — it has no dependency on the `crewai` framework — and is
pulled in transitively by `crewai` and `crewai-cli`. End users do not normally
install it directly.

</details>

### crewai-cli

CLI for CrewAI — scaffold, run, deploy and manage AI agent crews.

`pip install crewai-cli` · does not install on CPython 3.14 · licence: not stated · rank 3051 · last release 2026-11-07 · [PyPI](https://pypi.org/project/crewai-cli/) · [docs](https://docs.crewai.com) · [source](https://github.com/crewAIInc/crewAI)

<details><summary>README extract</summary>

CLI for CrewAI — scaffold, run, deploy and manage AI agent crews without
installing the full framework.

</details>

### comfy-aimdo

AI Model Dynamic Offloader for ComfyUI

`pip install comfy-aimdo` · installs (wheel) · licence: not stated · rank 3060 · last release 2026-10-21 · [PyPI](https://pypi.org/project/comfy-aimdo/) · [source](https://github.com/Comfy-Org/comfy-aimdo)

<details><summary>README extract</summary>

This project is a pytorch VRAM allocator that implements on-demand offloading of model weights when the primary pytorch VRAM allocator comes under pressure.

Sections: AI Model Dynamic Offloader, How it works, If the `fault()` is unsuccessful (offloaded weight), Priorities, Backend, Caveats

</details>

### cfn-flip

Convert AWS CloudFormation templates between JSON and YAML formats

`pip install cfn-flip` · installs (wheel) · licence: Apache2 · rank 3093 · last release 2021-10-07 · [PyPI](https://pypi.org/project/cfn-flip/)

<details><summary>README extract</summary>

AWS CloudFormation Template Flip is a tool that converts AWS CloudFormation templates between JSON and YAML formats, making use of the YAML format's short function syntax where possible.

The term "Flip" is inspired by the well-known Unix command-line tool flip which converts text files between Unix, Mac, and MS-DOS formats.

Example:
```python
from cfn_flip import flip, to_yaml, to_json

"""
All functions expect a string containing serialised data
and return a string containing serialised data
or raise an exception if there is a problem parsing the input
"""

# flip takes a best guess at the serialisation format
# and returns the opposite, converting json into yaml and vice versa
...
```

...

</details>

### crewai-tools

Set of tools for the crewAI framework

`pip install crewai-tools` · does not install on CPython 3.14 · licence: not stated · rank 3118 · last release 2026-11-07 · [PyPI](https://pypi.org/project/crewai-tools/) · [docs](https://docs.crewai.com) · [source](https://github.com/crewAIInc/crewAI)

<details><summary>README extract</summary>

Empower your CrewAI agents with powerful, customizable tools to elevate their capabilities and tackle sophisticated, real-world tasks.

CrewAI Tools provide the essential functionality to extend your agents, helping you rapidly enhance your automations with reliable, ready-to-use tools or custom-built solutions tailored precisely to your needs. ...

Features:
- Simplicity & Flexibility: Easy-to-use yet powerful enough for complex workflows.
- Rapid Integration: Seamlessly incorporate external services, APIs, and databases.
- Enterprise Ready: Built for stability, performance, and consistent results.

Example:
```python
from crewai.tools import BaseTool

class MyCustomTool(BaseTool):
    name: str = "Tool Name"
    description: str = "Detailed description here."

...

</details>

### coreforecast

Fast implementations of common forecasting routines

`pip install coreforecast` · installs (wheel) · licence: Apache Software License · rank 3139 · last release 2026-11-03 · [PyPI](https://pypi.org/project/coreforecast/) · [docs](https://nixtlaverse.nixtla.io/coreforecast) · [source](https://github.com/Nixtla/coreforecast)

<details><summary>README extract</summary>

At Nixtla we have implemented several libraries to deal with time series data. We often have to apply some transformation over all of the series, which can prove time consuming even for simple operations like performing some kind of scaling. ...

Example:
```python
import numpy as np
from coreforecast.grouped_array import GroupedArray

data = np.arange(10)
indptr = np.array([0, 3, 10])
ga = GroupedArray(data, indptr)
```

Sections: Motivation, PyPI, conda-forge, Minimal example, Multithreading, Single-array functions

</details>

### crossplane

Reliable and fast NGINX configuration file parser.

`pip install crossplane` · installs (wheel) · licence: Apache Software License · rank 3235 · last release 2022-09-22 · [PyPI](https://pypi.org/project/crossplane/)

<details><summary>README extract</summary>

- Install
 - Command Line Interface
 - crossplane parse
 - crossplane build
 - crossplane lex
 - crossplane format
 - crossplane minify
 - Python Module
 - crossplane.parse()
 - crossplane.build()
 - crossplane.lex()
 - Other Languages

Example:
```python
import crossplane
payload = crossplane.parse('/etc/nginx/nginx.conf')
```

Sections: crossplane, Command Line Interface, crossplane parse, Schema, Example, crossplane parse (advanced), crossplane build, crossplane lex, crossplane format, crossplane minify, Python Module, crossplane.parse(), crossplane.build()

</details>

### contree-sdk

SDK for ConTree container runtime with versioned filesystem state

`pip install contree-sdk` · installs (wheel) · licence: Apache Software License · rank 3272 · last release 2026-11-06 · [PyPI](https://pypi.org/project/contree-sdk/)

<details><summary>README extract</summary>

Use one sandbox session to run commands, read and write files, search contents,
and list directories. Save the filesystem as an image when you need to continue
later or try a different approach.

This checkout contains the breaking 0.5 development API. Install it locally:

Example:
```python
"""Use the five sandbox tools in one session."""

from contree_sdk import create_sandbox_session

def main() -> None:
    with create_sandbox_session(image="tag:alpine:latest") as sandbox_session:
        # Write a file in the sandbox.
        sandbox_session.write_file("/work/message.txt", b"Hello from ConTree!\n")

...
```

Sections: ConTree SDK, Use a sandbox session, Sync, Async, Follow a workflow

</details>

### Collectfasta

A Faster Collectstatic

`pip install Collectfasta` · installs (wheel) · licence: MIT License · rank 3274 · last release 2026-09-27 · [PyPI](https://pypi.org/project/Collectfasta/)

<details><summary>README extract</summary>

A faster collectstatic command. This is a fork of the archived collectfast by @antonagestam and a drop-in replacement - you must not have both installed at the same time.

Features

- Efficiently decide what files to upload using cached checksums ...

Sections: Collectfasta, Upload Strategies, Usage, Setting Up a Dedicated Cache Backend, Enable Parallel Uploads, Debugging, Versioning policy

</details>

### crontab

Parse and use crontab schedules in Python

`pip install crontab` · installs from source (sdist only) · licence: GNU Lesser General Public License v2 (LGPLv2); GNU Lesser General Public License · rank 3295 · last release 2025-07-09 · [PyPI](https://pypi.org/project/crontab/)

_README extract left out: share-alike licence._

### category-encoders

A package for encoding categorical variables for machine learning

`pip install category-encoders` · installs (wheel) · licence: Other/Proprietary License · rank 3299 · last release 2026-10-24 · [PyPI](https://pypi.org/project/category-encoders/)

<details><summary>README extract</summary>

A set of scikit-learn-style transformers for encoding categorical
variables into numeric by means of different techniques.

Important Links

Documentation:

Encoding Methods

Unsupervised:
 * Backward Difference Contrast 2
 * BaseN [6]
 * Binary [5]
 * Gray [14]
 * Count [10]
 * Hashing [1]
 * Helmert Contrast 2
 * Ordinal 2
 * One-Hot 2
 * ...

Example:
```python
from category_encoders import *
import pandas as pd

# prepare some data with categorical features
X = pd.DataFrame({
    'gender': ['male', 'female', 'female', 'male', 'female'],
    'country': ['US', 'UK', 'US', 'CA', 'UK'],
    'age': [25, 32, 47, 51, 38],
})

# use binary encoding to encode two categorical features
...
```

</details>

### comfyui-workflow-templates-media-assets-01

Media assets bundle 01 for ComfyUI workflow templates

`pip install comfyui-workflow-templates-media-assets-01` · installs (wheel) · licence: MIT · rank 3352 · last release 2026-09-23 · [PyPI](https://pypi.org/project/comfyui-workflow-templates-media-assets-01/)

<details><summary>README extract</summary>

Media assets bundle 01 for ComfyUI workflow templates.

</details>

### contree-client

Python client for the Contree API, generated from the OpenAPI specification

`pip install contree-client` · installs (wheel) · licence: Apache-2.0 · rank 3385 · last release 2026-11-02 · [PyPI](https://pypi.org/project/contree-client/) · [docs](https://docs.tokenfactory.nebius.com/sandboxes/overview)

<details><summary>README extract</summary>

Python client for the Contree API — sandboxed code execution
combining virtual machine isolation with container operational
efficiency.

Synchronous clients are named `ContreeClient`, asynchronous ones are
named `ContreeAsyncClient`; every backend shares the same interface:

| Backend | Extra | Import | ...

Example:
```python
from contree_client import models, testing

OP_UUID = "87654321-9abc-baba-deda-0123456789ab"
EVENTS = [
    models.OperationEvent.from_dict(event)
    for event in (
        {
            "id": 1,
            "ts": "2026-06-08T20:00:00Z",
            "spid": 1,
            "type": "stdout",
...
```

Sections: contree-client, Quick start, Use cases, Copyright

</details>

### cloudcruise

The official CloudCruise Python SDK

`pip install cloudcruise` · installs (wheel) · licence: MIT License · rank 3416 · last release 2026-10-22 · [PyPI](https://pypi.org/project/cloudcruise/) · [docs](https://docs.cloudcruise.com) · [source](https://github.com/CloudCruise/cloudcruise-python)

<details><summary>README extract</summary>

The official CloudCruise Python SDK for automated browser workflows, encrypted
credential management, realtime run monitoring, and webhook verification.

Example:
```python
from cloudcruise import CloudCruise, CloudCruiseParams, StartRunRequest

client = CloudCruise(
    CloudCruiseParams(
        api_key="<CLOUDCRUISE_API_KEY>",
        encryption_key="<CLOUDCRUISE_ENCRYPTION_KEY>",
    )
)
# Alternatively, set CLOUDCRUISE_API_KEY and CLOUDCRUISE_ENCRYPTION_KEY
...
```

Sections: cloudcruise-python, Quick Start, Clients, Documentation & Resources

</details>

### clickhouse-pool

a thread-safe connection pool for ClickHouse

`pip install clickhouse-pool` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 3420 · last release 2025-08-19 · [PyPI](https://pypi.org/project/clickhouse-pool/) · [source](https://github.com/ericmccarthy7/clickhouse-pool)

_README extract left out: share-alike licence._

### compact-json

A JSON formatter that produces compact but human-readable

`pip install compact-json` · installs (wheel) · licence: MIT License · rank 3423 · last release 2025-12-26 · [PyPI](https://pypi.org/project/compact-json/) · [docs](https://github.com/masaccio/compact-json/blob/main/README.md) · [source](https://github.com/masaccio/compact-json)

<details><summary>README extract</summary>

`compact-json` is a JSON formatter that produces configurably compact JSON that remains human-readable.

This package is now deprecated and you are strongly encouraged to migrate to fractured-json which tracks FracturedJson using that project's .NET assembly directly.

Any given container is formatted in one of three ways: ...

Example:
```python
import json
from compact_json import Formatter, EolStyle

formatter = Formatter()
formatter.indent_spaces = 2
formatter.max_inline_complexity = 10
formatter.json_eol_style = EolStyle.LF

# Format the JSON contents:
with open("input.json", "r") as f:
    obj = json.load(f)
    json_string = formatter.serialize(obj)
    print(json_string)

...
```

...

</details>

### cadquery-ocp-novtk

Python wrapper for Open CASCADE Technology 3D geometry library based on the official CadQuery/OCP sources (no VTK support)

`pip install cadquery-ocp-novtk` · installs (wheel) · licence: Apache Software License · rank 3466 · last release 2026-10-05 · [PyPI](https://pypi.org/project/cadquery-ocp-novtk/)

<details><summary>README extract</summary>

Python wrapper for OCCT generated using pywrap. Typing stubs available from pypi.
Note: VTK is not supported with cadquery-ocp-novtk.

* Provide thin bindings to OCCT.
* Wrap all OCCT modules (if practical).
* React quickly to new OCCT releases.
* Cater primarily for the CadQuery project.

* Provide additional functionality not present in OCCT

Sections: cadquery-ocp-novtk (also known as OCP), Goals of OCP, Non-goals

</details>

### camel-converter

Converts a string from snake case to camel case or camel case to snake case

`pip install camel-converter` · installs (wheel) · licence: MIT License · rank 3551 · last release 2026-10-10 · [PyPI](https://pypi.org/project/camel-converter/)

<details><summary>README extract</summary>

In JSON keys are frequently in camelCase format, while variable names in Python are typically
snake_case. The purpose of this package is to help convert between the two formats.

Example:
```python
from camel_converter import to_snake

snake = to_snake("myString")
```

Sections: Camel Converter, Usage, Optional Extras

</details>

### connectorx

(no summary)

`pip install connectorx` · installs (wheel) · licence: MIT · rank 3564 · last release 2026-09-17 · [PyPI](https://pypi.org/project/connectorx/) · [docs](https://sfu-db.github.io/connector-x/intro.html) · [source](https://github.com/sfu-db/connector-x)

<details><summary>README extract</summary>

Load data from to , the fastest way.

ConnectorX enables you to load data from databases into Python in the fastest and most memory efficient way.

What you need is one line of code:

Optionally, you can accelerate the data loading using parallelism by specifying a partition column. ...

Example:
```python
import connectorx as cx

cx.read_sql("postgresql://username:password@server:port/database", "SELECT * FROM lineitem")
```

Sections: Performance, Time chart, lower is better., Memory consumption chart, lower is better., How does ConnectorX download the data?, Sources, Destinations, Documentation, Next Plan, Historical Benchmark Results, Organizations and Projects using ConnectorX, Citing ConnectorX

</details>

### cowsay

The famous cowsay for GNU/Linux is now available for python

`pip install cowsay` · installs (wheel) · licence: GNU-GPL · rank 3595 · last release 2023-09-25 · [PyPI](https://pypi.org/project/cowsay/)

_README extract left out: share-alike licence._

### Crawl4AI

🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & scraper

`pip install Crawl4AI` · installs (wheel) · licence: Apache-2.0 · rank 3610 · last release 2026-10-14 · [PyPI](https://pypi.org/project/Crawl4AI/)

<details><summary>README extract</summary>

Latest: v0.9.5 (14 Oct 2026) · all releases →

Crawl4AI turns any website into clean, LLM-ready Markdown for RAG, AI agents and data pipelines. Run the open-source web crawler and scraper yourself, free forever, or use it hosted with one key: `/scrape` a page to Markdown, `/extract` it to JSON, `/search` the web, `/serp` for Google's results page ...

Example:
```python
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.content_filter_strategy import PruningContentFilterLXML
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

async def main():
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
...
```

...

</details>

### colorcet

Collection of perceptually uniform colormaps

`pip install colorcet` · installs (wheel) · licence: CC-BY-4.0 · rank 3693 · last release 2026-04-28 · [PyPI](https://pypi.org/project/colorcet/) · [docs](https://colorcet.holoviz.org) · [source](https://github.com/holoviz/colorcet)

<details><summary>README extract</summary>

| | |

| Latest release | |
| Python | |
| Build Status | |
| Coverage | |
| Latest dev release | |
| Documentation | |

Colorcet is a collection of
perceptually uniform colormaps for use with Python plotting programs like
bokeh,
matplotlib,
holoviews, and
datashader based on the
set of perceptually uniform colormaps created
by Peter Kovesi at the ...

Sections: Colorcet: Collection of perceptually uniform colormaps, What is it?, Learning more, Samples

</details>

### csvw

Python library to work with CSVW described tabular data

`pip install csvw` · installs (wheel) · licence: Apache Software License · rank 3716 · last release 2026-11-06 · [PyPI](https://pypi.org/project/csvw/)

<details><summary>README extract</summary>

This package provides
- a Python API to read and write relational, tabular data according to the CSV on the Web specification and
- commandline tools for reading and validating CSVW data.

> [!IMPORTANT]
> The Python API provided by `csvw` 4.x is not fully backwards compatible with `csvw` < 4.
> See CHANGES for more information.

Example:
```python
import json
from csvw import CSVW
data = CSVW('
print(json.dumps(data.to_json(minimal=True), indent=4))
[
    {
        "province": "Hello",
        "territory": "world",
        "precinct": "1"
    }
]
```

Sections: csvw, Links, CLI, `csvw2json`, `csvwvalidate`, `csvwdescribe`, Python API, Known limitations, CSVW conformance, Compatibility with Frictionless Data Specs, See also

</details>

### cmeel-boost

cmeel distribution for boost, which provides free peer-reviewed portable C++ source libraries.

`pip install cmeel-boost` · installs (wheel) · licence: BSL-1.0 · rank 3766 · last release 2026-05-20 · [PyPI](https://pypi.org/project/cmeel-boost/) · [source](https://github.com/cmake-wheel/cmeel-boost.git)

### cdk-nag

Check CDK v2 applications for best practices using a combination on available rule packs.

`pip install cdk-nag` · installs (wheel) · licence: OSI Approved · rank 3767 · last release 2026-08-04 · [PyPI](https://pypi.org/project/cdk-nag/) · [source](https://github.com/cdklabs/cdk-nag.git)

<details><summary>README extract</summary>

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: Apache-2.0

Check CDK applications or CloudFormation templates for best practices using a combination of available rule packs. Inspired by cfn_nag.

Check out this blog post for a guided overview! ...

Example:
```python
from aws_cdk import App, Validations
from cdk_nag import AwsSolutionsChecks, NIST80053R5Checks

# CdkTestStack: Any

app = App()
CdkTestStack(app, "CdkNagDemo")
# Simple rule informational messages using the AWS Solutions Rule pack
Validations.of(app).add_plugins(AwsSolutionsChecks(app))
# Multiple rule packs can be run against the same app
...
```

...

</details>

### creosote

Identify unused dependencies and avoid a bloated virtual environment.

`pip install creosote` · installs (wheel) · licence: MIT License · rank 3808 · last release 2026-03-28 · [PyPI](https://pypi.org/project/creosote/) · [source](https://github.com/fredrikaverpil/creosote)

<details><summary>README extract</summary>

Identify unused dependencies and avoid a bloated virtual environment.

Features:
Django dependencies are often added to the `INSTALLED_APPS` and `MIDDLEWARE`
lists in `settings.py` file as strings, without being directly imported in your
source code. ...

Sections: creosote, ⚡️ Quickstart, ⚙️ Configuration, Using commandline arguments, Required arguments, Optional arguments, Using `pyproject.toml`, 🤔 How this works, 🌶️ Features, 😤 Known limitations, 🤨 FAQ, Why are my Django dependencies reported as unused?, 📔 Notes on PEP-508 (`requirements.txt`), 📓 Notes on PEP-582 (`pypackages`)

</details>

### contextvars

PEP 567 Backport

`pip install contextvars` · installs from source (sdist only) · licence: Apache Software License · rank 3853 · last release 2019-04-01 · [PyPI](https://pypi.org/project/contextvars/)

<details><summary>README extract</summary>

This package implements a backport of Python 3.7 `contextvars`
module (see PEP 567) for Python 3.6.

Important: at this moment this package does not provide an
asyncio event loop with PEP 567 support yet. Stay tuned for updates.

This package replaces the old "contextvars" PyPI package which
repository is available here. ...

Example:
```python
import contextvars

my_var = contextvars.ContextVar('my_var')

# ...
```

Sections: PEP 567 Backport, Original "contextvars" Package, Documentation, Usage, Listing as a Dependency

</details>

### chargebee

Python wrapper for the Chargebee Subscription Billing API

`pip install chargebee` · installs (wheel) · licence: not stated · rank 3876 · last release 2026-11-02 · [PyPI](https://pypi.org/project/chargebee/)

<details><summary>README extract</summary>

> [!NOTE]
> We are trialing a Discord server for developers building with Chargebee. Limited spots are open on a first-come basis. Join here if interested.

This is the official Python library for integrating with Chargebee.
- 📘 For a complete reference of available APIs, check out our API Documentation. ...

Features:
- Automatic retries for specific HTTP status codes: Retries are automatically triggered for status codes `500`, `502`, `503`, and `504`.
- Exponential backoff: Retry delays increase exponentially to prevent overwhelming the server. ...

Example:
```python
from chargebee import Chargebee
from chargebee.retry_config import RetryConfig

retry_config = RetryConfig(enabled=True, max_retries=5, delay_ms=1000, retry_on=[500])
cb_client = Chargebee(api_key="api_key", site="site")
...

</details>

### codemagic-cli-tools

CLI tools used in Codemagic builds

`pip install codemagic-cli-tools` · installs (wheel) · licence: GPL-3.0-or-later · rank 3884 · last release 2026-10-29 · [PyPI](https://pypi.org/project/codemagic-cli-tools/) · [docs](https://github.com/codemagic-ci-cd/cli-tools/tree/master/docs#cli-tools) · [source](https://github.com/codemagic-ci-cd/cli-tools)

_README extract left out: share-alike licence._

### cython-lint

Lint Cython files

`pip install cython-lint` · installs (wheel) · licence: MIT License · rank 3890 · last release 2026-11-07 · [PyPI](https://pypi.org/project/cython-lint/)

<details><summary>README extract</summary>

Everything ``flake8`` used to do (by accident), plus much more.

A tool and pre-commit hook to lint Cython files.

Here's some major projects using ``cython-lint`` - is yours missing? Feel free to open a pull request!

- arrow-adbc
- ansible-pylibssh
- arrow
- CuPy
- dpctl
- frozenlist
- mkl_fft
- mkl-service
- NumPy
- open library
- pandas ...

Sections: cython-lint, Used by, Usage as a pre-commit hook, Command-line example, Configuration, Which checks are implemented?

</details>

### clandestined

rendezvous hashing implementation based on murmur3 hash

`pip install clandestined` · installs from source (sdist only) · licence: MIT · rank 3899 · last release 2023-06-01 · [PyPI](https://pypi.org/project/clandestined/)

### cmeel-assimp

cmeel distribution for assimp, Open-Asset-Importer-Library Repository

`pip install cmeel-assimp` · installs (wheel) · licence: BSD-3-Clause · rank 3903 · last release 2026-05-20 · [PyPI](https://pypi.org/project/cmeel-assimp/) · [source](https://github.com/cmake-wheel/cmeel-assimp.git)

### cmeel-zlib

cmeel distribution for zlib

`pip install cmeel-zlib` · installs (wheel) · licence: Zlib · rank 3971 · last release 2026-05-20 · [PyPI](https://pypi.org/project/cmeel-zlib/) · [source](https://github.com/cmake-wheel/cmeel-zlib.git)

### cmeel-octomap

cmeel distribution for OctoMap, An Efficient Probabilistic 3D Mapping Framework Based on Octrees

`pip install cmeel-octomap` · installs (wheel) · licence: not stated · rank 3984 · last release 2025-02-12 · [PyPI](https://pypi.org/project/cmeel-octomap/) · [source](https://github.com/cmake-wheel/cmeel-octomap.git)

### cmeel-qhull

cmeel distribution for qhull: Convex hull, Delaunay triangulation, Voronoi diagrams, Halfspace intersection

`pip install cmeel-qhull` · installs (wheel) · licence: not stated · rank 3986 · last release 2025-02-12 · [PyPI](https://pypi.org/project/cmeel-qhull/)

### comfyui-workflow-templates-media-video

Media bundle containing video workflow assets

`pip install comfyui-workflow-templates-media-video` · installs (wheel) · licence: MIT · rank 3992 · last release 2026-06-30 · [PyPI](https://pypi.org/project/comfyui-workflow-templates-media-video/)

<details><summary>README extract</summary>

Media bundle containing video workflow assets for ComfyUI.

</details>

### cog

Containers for machine learning

`pip install cog` · installs (wheel) · licence: not stated · rank 4007 · last release 2026-10-20 · [PyPI](https://pypi.org/project/cog/) · [source](https://github.com/replicate/cog)

<details><summary>README extract</summary>

Cog is an open-source tool that lets you package machine learning models in a standard, production-ready container.

You can deploy your packaged model to your own infrastructure, or to Replicate.

Features:
- 📦 Docker containers without the pain. Writing your own `Dockerfile` can be a bewildering process. With Cog, you define your environment with a simple configuration file and it generates a Docker image with all the best practices: Nvidia base ...

Example:
```python
from cog import BaseRunner, Input, Path
import torch

class Runner(BaseRunner):
    def setup(self):
        """Load the model into memory to make running multiple inferences efficient"""
        self.model = torch.load("./weights.pth")

    # The arguments and types the model takes as input
    def run(self,
...
```

...

</details>

### comfyui-workflow-templates-media-image

Media bundle containing image workflow assets

`pip install comfyui-workflow-templates-media-image` · installs (wheel) · licence: MIT · rank 4012 · last release 2026-06-30 · [PyPI](https://pypi.org/project/comfyui-workflow-templates-media-image/)

<details><summary>README extract</summary>

Media bundle containing image workflow assets for ComfyUI.

</details>

### comfyui-workflow-templates-media-other

Media bundle containing audio/3D/misc workflow assets

`pip install comfyui-workflow-templates-media-other` · installs (wheel) · licence: MIT · rank 4019 · last release 2026-06-30 · [PyPI](https://pypi.org/project/comfyui-workflow-templates-media-other/)

<details><summary>README extract</summary>

Media bundle containing audio, 3D, and other workflow assets for ComfyUI.

</details>

### comfyui-workflow-templates-media-api

Media bundle containing API-driven workflow assets

`pip install comfyui-workflow-templates-media-api` · installs (wheel) · licence: MIT · rank 4028 · last release 2026-06-30 · [PyPI](https://pypi.org/project/comfyui-workflow-templates-media-api/)

<details><summary>README extract</summary>

Media bundle containing API-driven workflow assets for ComfyUI.

</details>

### customerio

Customer.io Python bindings.

`pip install customerio` · installs (wheel) · licence: MIT · rank 4040 · last release 2026-07-24 · [PyPI](https://pypi.org/project/customerio/)

<details><summary>README extract</summary>

This module is tested with Python 3.10 through 3.14. If you're new to Customer.io, we recommend that you integrate with our Data Pipelines Python library instead.

Example:
```python
from customerio import CustomerIO, Regions

cio = CustomerIO(site_id, api_key, region=Regions.US)
cio.identify(id="5", email="customer@example.com", name="Bob", plan="premium")
cio.track(customer_id="5", name="purchased")
cio.track(customer_id="5", name="purchased", data={"price": 23.45})
```

...

</details>

### cliff

Command Line Interface Formulation Framework

`pip install cliff` · installs (wheel) · licence: Apache-2.0 · rank 4050 · last release 2026-10-22 · [PyPI](https://pypi.org/project/cliff/) · [source](https://opendev.org/openstack/cliff/)

<details><summary>README extract</summary>

cliff is a framework for building command line programs.
It uses entry points to provide subcommands, output formatters, and other
extensions.

* Free software: Apache license

Sections: Team and repository tags, cliff -- Command Line Interface Formulation Framework

</details>

### cmeel-urdfdom

cmeel distribution for urdfdom, URDF parser

`pip install cmeel-urdfdom` · installs (wheel) · licence: BSD-3-Clause · rank 4070 · last release 2026-05-21 · [PyPI](https://pypi.org/project/cmeel-urdfdom/)

<details><summary>README extract</summary>

The URDF (U-Robot Description Format) library provides core data structures and a simple XML parsers for populating the class data structures from an URDF file.

For now, the details of the URDF specifications reside on ...

Sections: urdfdom, Using with ROS, URDF Versioning, Version 1.0 (Default), Version 1.1, Version 1.2, Joint Limit Semantics By Version, Compatibility and Parsing Behavior

</details>

### cantools

CAN BUS tools.

`pip install cantools` · installs (wheel) · licence: MIT License · rank 4072 · last release 2026-10-29 · [PyPI](https://pypi.org/project/cantools/) · [docs](https://cantools.readthedocs.io/) · [source](https://github.com/cantools/cantools)

<details><summary>README extract</summary>

CAN BUS tools in Python 3.

- DBC, KCD, SYM, ARXML 3&4 and CDD file parsing.

- CAN message encoding and decoding.

- Simple and extended signal multiplexing.

- Diagnostic DID encoding and decoding.

- `candump` output decoder.

- Node tester.

- `C` source code generator.

- CAN bus monitor.

- Graphical plots of signals.

Project homepage: ...

Example:
```python
>>> import cantools
>>> from pprint import pprint
>>> db = cantools.database.load_file('tests/files/dbc/motohawk.dbc')
>>> db.messages
[message('ExampleMessage', 0x1f0, False, 8, {None: 'Example message used as template in MotoHawk models.'})]
>>> example_message = db.get_message_by_name('ExampleMessage')
>>> pprint(example_message.signals)
...
```

...

</details>

### curatorbin

install curator through pip and run it through python

`pip install curatorbin` · installs (wheel) · licence: SSPLv1 · rank 4091 · last release 2022-01-28 · [PyPI](https://pypi.org/project/curatorbin/)

### cmeel-console-bridge

cmeel distribution for console-bridge, A ROS-independent package for logging that seamlessly pipes into rosconsole/rosout for ROS-dependent packages.

`pip install cmeel-console-bridge` · installs (wheel) · licence: Zlib · rank 4107 · last release 2025-03-19 · [PyPI](https://pypi.org/project/cmeel-console-bridge/)

<details><summary>README extract</summary>

console-bridge distribution for cmeel packages.

</details>

### clamd

Clamd is a python interface to Clamd (Clamav daemon).

`pip install clamd` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 4141 · last release 2014-08-21 · [PyPI](https://pypi.org/project/clamd/)

_README extract left out: share-alike licence._

### coal

An extension of the Flexible Collision Library

`pip install coal` · installs (wheel) · licence: BSD-3-Clause · rank 4187 · last release 2026-05-21 · [PyPI](https://pypi.org/project/coal/)

<details><summary>README extract</summary>

FCL was forked in 2015, creating a new project called HPP-FCL.
Since then, a large part of the code has been rewritten or removed (unused and untested code), and new features have been introduced (see below).
Due to these major changes, it was decided in 2024 to rename the HPP-FCL project to Coal. ...

Example:
```python
import numpy as np
import coal
# Optional:
# The Pinocchio library is a rigid body algorithms library and has a handy SE3 module.
# It can be installed as simply as `conda -c conda-forge install pinocchio`.
# Installing pinocchio also installs coal.
import pinocchio as pin

def loadConvexMesh(file_name: str):
    loader = coal.MeshLoader()
...
```

...

</details>

### confuse

Painless YAML config files

`pip install confuse` · installs (wheel) · licence: MIT · rank 4199 · last release 2026-11-01 · [PyPI](https://pypi.org/project/confuse/) · [source](https://github.com/beetbox/confuse)

<details><summary>README extract</summary>

Confuse is a configuration library for Python that uses YAML. It takes care
of defaults, overrides, type checking, command-line integration, environment
variable support, human-readable errors, and standard OS-specific locations.

Features:
Here's what Confuse brings to the table:

- An utterly sensible API resembling dictionary-and-list structures but
 providing transparent validation without lots of boilerplate code. ...

Sections: Confuse: painless YAML config files, What It Does, Using Confuse

</details>

### comfy-angle

Redistributable ANGLE libraries

`pip install comfy-angle` · installs (wheel) · licence: BSD-3-Clause · rank 4276 · last release 2026-08-23 · [PyPI](https://pypi.org/project/comfy-angle/)

<details><summary>README extract</summary>

Redistributable ANGLE libraries packaged as Python wheels. Windows and macOS libraries are extracted from Electron releases. Linux libraries are built from the corresponding ANGLE revision without X11, Wayland, or GBM dependencies.

Provides `libEGL` and `libGLESv2` for Windows (x64, arm64), Linux (x64, arm64), and macOS (arm64).

Example:
```python
import comfy_angle

# Directory containing the shared libraries
comfy_angle.get_lib_dir()

# Full paths to individual libraries
comfy_angle.get_egl_path()
comfy_angle.get_glesv2_path()
```

Sections: comfy-angle, Usage, Building wheels from source

</details>

### cmeel-tinyxml2

cmeel distribution for TinyXML-2

`pip install cmeel-tinyxml2` · installs (wheel) · licence: Zlib · rank 4284 · last release 2026-05-21 · [PyPI](https://pypi.org/project/cmeel-tinyxml2/) · [source](https://github.com/cmake-wheel/cmeel-tinyxml2.git)

### chz

chz is a library for managing configuration

`pip install chz` · installs (wheel) · licence: not stated · rank 4358 · last release 2025-11-24 · [PyPI](https://pypi.org/project/chz/) · [source](https://github.com/openai/chz)

<details><summary>README extract</summary>

*(pronounced "चीज़")*

`chz` helps you manage configuration, particularly from the command line.

`chz` is available on PyPI.

To click the links below, please visit Github.

Overview:
- Quickstart
- Declarative object model
- Immutability
- Validation
- Type checking
- Command line parsing
- Discoverability
- Partial application ...

</details>

### curies

Idiomatic conversion between URIs and compact URIs (CURIEs)

`pip install curies` · installs (wheel) · licence: MIT · rank 4363 · last release 2026-11-02 · [PyPI](https://pypi.org/project/curies/) · [docs](https://curies.readthedocs.io) · [source](https://github.com/biopragmatics/curies.git)

<details><summary>README extract</summary>

Idiomatic conversion between URIs and compact URIs (CURIEs).

Full documentation is available at
curies.readthedocs.io.

Example:
```python
import curies

converter = curies.load_prefix_map({
    "CHEBI": "
    # ... and so on
})

>>> converter.compress("
'CHEBI:1'

>>> converter.expand("CHEBI:1")
'
```

Sections: CURIEs, CLI Usage, 🧑‍🤝‍🧑 Related, Users, 👋 Attribution, 🍪 Cookiecutter, Updating Package Boilerplate, 📖 Building the Documentation, Configuring ReadTheDocs, Configuring Zenodo, Registering with the Python Package Index (PyPI), Configuring your machine's connection to PyPI, Uploading to PyPI, Releasing on GitHub

</details>

### cashews

cache tools with async power

`pip install cashews` · installs (wheel) · licence: MIT License · rank 4372 · last release 2026-09-17 · [PyPI](https://pypi.org/project/cashews/)

<details><summary>README extract</summary>

Async cache framework with simple API to build fast and reliable applications

Features:
Cache plays a significant role in modern applications and everybody wants to use all the power of async programming and cache.
There are a few advanced techniques with cache and async programming that can help you build simple, fast,
scalable and ...

Example:
```python
from cashews import cache

cache.setup("mem://")  # configure as in-memory cache, but redis/diskcache is also supported

# use a decorator-based API
@cache(ttl="3h", key="user:{request.user.uid}")
async def long_running_function(request):
    ...

# or for fine-grained control, use it directly in a function
async def cache_using_function(request):
...
```

...

</details>

### cachetools-async

Provides decorators that are inspired by and work closely with cachetools' for caching asyncio functions and methods.

`pip install cachetools-async` · installs (wheel) · licence: MIT · rank 4397 · last release 2025-06-09 · [PyPI](https://pypi.org/project/cachetools-async/) · [source](https://github.com/imnotjames/cachetools-async.git)

<details><summary>README extract</summary>

This module provides decorators for Python asyncio coroutine functions
to support memoization. These are compatible, and can be considered extending
the functionality of `cachetools`.

This module supports the same definition of a cache as cachetools does - a mutable mapping of a fixed
maximum size. ...

Example:
```python
from cachetools import LRUCache, TTLCache
from cachetools_async import cached

# Dependencies for our examples
import aiohttp
import python_weather

# cache least recently used Python Enhancement Proposals
@cached(cache=LRUCache(maxsize=32))
async def get_pep(num: int):
    pep_url = ' % num
    async with aiohttp.ClientSession() as session:
...
```

Sections: cachetools_async, Poetry, Rye, Pip

</details>

### codewords-client

Python client for CodeWords with auto-configured FastAPI integration.

`pip install codewords-client` · installs (wheel) · licence: MIT · rank 4478 · last release 2026-09-01 · [PyPI](https://pypi.org/project/codewords-client/)

### cron-validator

Unix cron implementation by Python

`pip install cron-validator` · installs (wheel) · licence: MIT · rank 4493 · last release 2023-06-19 · [PyPI](https://pypi.org/project/cron-validator/)

<details><summary>README extract</summary>

Features:
- Validate unix cron expression
- Match unit cron expression with specific datetime
- Generate match datetime between two datetime
- Schedule tasks

Example:
```python
from cron_validator import CronValidator

assert CronValidator.parse('* * * * *') is not None # valid
assert CronValidator.parse('*/3 * * * *') is not None # valid
assert CronValidator.parse('*/61 * * * *') is None # invalid
```

Sections: Cron Validator, Features, Run Tests, Sample

</details>

### clevercsv

A Python package for handling messy CSV files

`pip install clevercsv` · installs (wheel) · licence: MIT License · rank 4496 · last release 2026-05-11 · [PyPI](https://pypi.org/project/clevercsv/) · [docs](https://clevercsv.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

*CleverCSV provides a drop-in replacement for the Python* ``csv`` *package
with improved dialect detection for messy CSV files. It also provides a handy
command line tool that can standardize a messy file or generate Python code to
import it.*

Useful links:

- CleverCSV on Github
- CleverCSV on PyPI
- Documentation on ReadTheDocs ...

Example:
```python
# Import the package
>>> import clevercsv

# Load the file as a list of rows
# This uses the imdb.csv file in the examples directory
>>> rows = clevercsv.read_table('./imdb.csv')

# Load the file as a Pandas Dataframe
# Note that df = pd.read_csv('./imdb.csv') would fail here
>>> df = clevercsv.read_dataframe('./imdb.csv')

...
```

...

</details>

### curated-transformers

A PyTorch library of transformer models and components

`pip install curated-transformers` · installs (wheel) · licence: MIT · rank 4604 · last release 2024-04-17 · [PyPI](https://pypi.org/project/curated-transformers/)

<details><summary>README extract</summary>

State-of-the-art transformers, brick by brick

Curated Transformers is a transformer library for PyTorch. It provides
state-of-the-art models that are composed from a set of reusable
components. The stand-out features of Curated Transformer are: ...

Sections: Curated Transformers, 🏃‍♀️ Usage Example, 📚 Documentation, 🗜️ Quantization

</details>

### c2pa-python

Python bindings for the C2PA Content Authenticity Initiative (CAI) library

`pip install c2pa-python` · does not install on CPython 3.14 · licence: MIT OR Apache-2.0 · rank 4651 · last release 2026-10-26 · [PyPI](https://pypi.org/project/c2pa-python/) · [source](https://github.com/contentauth/c2pa-python)

<details><summary>README extract</summary>

The c2pa-python repository provides a Python library that can:

- Read and validate C2PA manifest data from media files in supported formats.
- Create and sign manifest data, and attach it to media files in supported formats.

Features:

- Create and sign C2PA manifests using various signing algorithms. ...

Sections: C2PA Python library, Prerequisites, Building from local c2pa-rs sources, Using a virtual environment with local builds, Build steps, Note on targets for macOS, Examples, API reference documentation

</details>

### cem

Coarsened Exact Matching for Causal Inference

`pip install cem` · does not install on CPython 3.14 · licence: not stated · rank 4667 · last release 2023-10-12 · [PyPI](https://pypi.org/project/cem/)

<details><summary>README extract</summary>

cem is a lightweight library for Coarsened Exact Matching (CEM). CEM is a matching technique used to reduce covariate imbalance, which would otherwise lead to treatment effect estimates that are sensitive to model specification. ...

Example:
```python
from cem.match import match
from cem.coarsen import coarsen
from cem.imbalance import L1

import statsmodels.api as sm

boston = load_boston()

O = "MEDV"  # outcome variable
T = "CHAS"  # treatment variable

y = boston[O]
X = boston.drop(columns=O)
```

Sections: cem: Coarsened Exact Matching for Causal Inference, Usage, Load the data, Automatic Coarsening, Informed Coarsening, References

</details>

### cmaes

Lightweight Covariance Matrix Adaptation Evolution Strategy (CMA-ES) implementation for Python 3.

`pip install cmaes` · installs (wheel) · licence: MIT · rank 4674 · last release 2026-08-21 · [PyPI](https://pypi.org/project/cmaes/)

<details><summary>README extract</summary>

:whale: Paper is now available on arXiv!

*Simple* and *Practical* Python library for CMA-ES.
Please refer to the paper [Nomura et al. 2026] for detailed information, including the design philosophy and advanced examples.

Example:
```python
import numpy as np
from cmaes import CMA

def quadratic(x1, x2):
    return (x1 - 3)  2 + (10 * (x2 + 2))  2

if name == "main":
    optimizer = CMA(mean=np.zeros(2), sigma=1.3)

    for generation in range(50):
        solutions = []
        for _ in range(optimizer.population_size):
            x = optimizer.ask()
...
```

...

</details>

### cloup

Adds features to Click: option groups, constraints, subcommand sections and help themes.

`pip install cloup` · installs (wheel) · licence: BSD-3-Clause · rank 4692 · last release 2026-09-12 · [PyPI](https://pypi.org/project/cloup/)

<details><summary>README extract</summary>

Features:
Cloup — originally from "Cl\ick + option gr\ oup\s" — enriches
Click with several features that make it
more expressive and configurable:

- option groups ...

Example:
```python
from cloup import (
    HelpFormatter, HelpTheme, Style,
    command, option, option_group
)
from cloup.constraints import RequireAtLeast, mutually_exclusive

# Check the docs for all available arguments of HelpFormatter and HelpTheme.
formatter_settings = HelpFormatter.settings(
    theme=HelpTheme(
...
```

Sections: Overview, Does it replace Click?, A simple example, Links

</details>

### camelot-py

PDF Table Extraction for Humans.

`pip install camelot-py` · installs (wheel) · licence: MIT · rank 4708 · last release 2026-06-04 · [PyPI](https://pypi.org/project/camelot-py/) · [docs](https://camelot-py.readthedocs.io/) · [source](https://github.com/camelot-dev/camelot)

<details><summary>README extract</summary>

Camelot is a Python library that can help you extract tables from PDFs.

Features:
- 📊 Five parsers — `lattice` (ruled tables), `stream` (whitespace), the text-alignment `network` / `hybrid`, and the optional neural `ml` (Table Transformer) for hard borderless tables — plus `flavor="auto"` to pick one for you. ...

Example:
```python
>>> import camelot
>>> tables = camelot.read_pdf('foo.pdf')
>>> tables
<TableList n=1>
>>> tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
>>> tables[0]
<Table shape=(7, 7)>
>>> tables[0].parsing_report
{
    'accuracy': 99.02,
    'whitespace': 12.24,
    'order': 1,
    'page': 1
}
...
```

...

</details>

### cint

cint - make ctypes great again

`pip install cint` · installs (wheel) · licence: MIT License · rank 4748 · last release 2019-03-19 · [PyPI](https://pypi.org/project/cint/)

### colored-traceback

Automatically color uncaught exception tracebacks

`pip install colored-traceback` · installs (wheel) · licence: ISC License (ISCL) · rank 4757 · last release 2024-07-13 · [PyPI](https://pypi.org/project/colored-traceback/) · [source](https://www.github.com/staticshock/colored-traceback.py)

<details><summary>README extract</summary>

Automatically color Python's uncaught exception tracebacks.

This one's for anybody who's ever struggled to read python's stacktraces on the
terminal. Something about the two-lines-per-frame approach really just makes
them tough to scan visually.

Compare this:

To this:

Example:
```python
import colored_traceback
colored_traceback.add_hook()
```

Sections: Colored Traceback, Usage

</details>

### cfgrib

Python interface to map GRIB files to the NetCDF Common Data Model following the CF Convention using ecCodes.

`pip install cfgrib` · installs (wheel) · licence: Apache Software License · rank 4766 · last release 2025-09-30 · [PyPI](https://pypi.org/project/cfgrib/)

<details><summary>README extract</summary>

Python interface to map GRIB files to the
Unidata's Common Data Model v4
following the CF Conventions.
The high level API is designed to support a GRIB engine for xarray
and it is inspired by netCDF4-python
and h5netcdf.
Low level access and decoding is performed via the
ECMWF ecCodes library and
the eccodes python package. ...

Example:
```python
>>> import xarray as xr
>>> ds = xr.open_dataset('era5-levels-members.grib', engine='cfgrib')
>>> ds
<xarray.Dataset>
Dimensions:        (number: 10, time: 4, isobaricInhPa: 2, latitude: 61,
                    longitude: 120)
Coordinates:
* number         (number) int64 0 1 2 3 4 5 6 7 8 9
...
```

...

</details>

### catkin-pkg

catkin package library

`pip install catkin-pkg` · installs (wheel) · licence: BSD License · rank 4774 · last release 2026-09-09 · [PyPI](https://pypi.org/project/catkin-pkg/) · [source](https://github.com/ros-infrastructure/catkin_pkg)

<details><summary>README extract</summary>

Library for retrieving information about catkin packages.

</details>

### cmake-parser

Pure Python library to parse CMake scripts

`pip install cmake-parser` · installs (wheel) · licence: Apache Software License · rank 4788 · last release 2023-08-28 · [PyPI](https://pypi.org/project/cmake-parser/) · [docs](https://roehling.github.io/cmake_parser/) · [source](https://github.com/roehling/cmake_parser)

<details><summary>README extract</summary>

cmake_parser is a pure Python parser for CMake code. It is still work in progress,
but is reasonably usable. It provides the following features:

* AST representation of CMake code
* Correct handling of quoted and bracketed values
* Variable expansion
* Basic boolean expression evaluation

Notably missing but planned are: ...

</details>

### crc

Pure Python CRC library

`pip install crc` · installs (wheel) · licence: BSD-2-Clause · rank 4849 · last release 2026-08-29 · [PyPI](https://pypi.org/project/crc/) · [docs](https://nicoretti.github.io/crc/) · [source](https://github.com/Nicoretti/crc)

<details><summary>README extract</summary>

Calculate CRC checksums, verify CRC checksum, predefined CRC configurations, custom CRC configurations

For convenience various frequently used crc configurations ship with the library out of the box.

| CRC8 | CRC16 | CRC32 | CRC64 | ...

Example:
```python
from crc import Calculator, Crc8

calculator = Calculator(Crc8.CCITT)
```

Sections: CRC, Available CRC Configurations, Custom Configurations, Requirements, Examples, Create a Calculator, Pre defined configuration, Custom configuration, Calculate a checksum, Standard, Optimized for speed, Verify a checksum

</details>

### clikit

CliKit is a group of utilities to build beautiful and testable command line interfaces.

`pip install clikit` · installs (wheel) · licence: MIT License · rank 4856 · last release 2020-06-09 · [PyPI](https://pypi.org/project/clikit/) · [source](https://github.com/sdispater/clikit)

<details><summary>README extract</summary>

CliKit is a group of utilities to build beautiful and testable command line interfaces.

This is at the core of Cleo.

</details>

### coiled

Python client for coiled.io dask clusters

`pip install coiled` · installs (wheel) · licence: Elastic-2.0 · rank 4867 · last release 2026-10-09 · [PyPI](https://pypi.org/project/coiled/)

<details><summary>README extract</summary>

Coiled.io •
 Documentation •
 Community •
 Support

Coiled is a deployment-as-a-service library for scaling Python with Dask, a popular open source library for parallel analytics. Coiled manages cloud resources, networking, software environments, and everything you need to scale Python in the cloud robustly and easily. ...

</details>

### click-help-colors

Colorization of help messages in Click

`pip install click-help-colors` · installs (wheel) · licence: MIT · rank 4971 · last release 2023-11-18 · [PyPI](https://pypi.org/project/click-help-colors/)

<details><summary>README extract</summary>

Colorization of help messages in Click.

Example:
```python
import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand

@click.group(
    cls=HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='green'
)
def cli():
    pass

@cli.command()
@click.option('--count', default=1, help='Some number.')
def command1(count):
    click.echo('command 1')

@cli.command(
...
```

Sections: click-help-colors, Usage

</details>

### customtkinter

Create modern looking GUIs with Python

`pip install customtkinter` · installs (wheel) · licence: MIT License · rank 5018 · last release 2026-06-24 · [PyPI](https://pypi.org/project/customtkinter/)

<details><summary>README extract</summary>

A modern and customizable python UI-library based on Tkinter:

</details>

### cmakelang

Language tools for cmake (format, lint, etc)

`pip install cmakelang` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 5059 · last release 2020-08-19 · [PyPI](https://pypi.org/project/cmakelang/)

_README extract left out: share-alike licence._

### corner

Make some beautiful corner plots

`pip install corner` · installs (wheel) · licence: BSD License · rank 5102 · last release 2026-07-05 · [PyPI](https://pypi.org/project/corner/) · [source](https://github.com/dfm/corner.py)

<details><summary>README extract</summary>

If you make use of this code, please cite the JOSS paper:

Sections: corner.py, Read the documentation

</details>

### codecov-cli

Codecov Command Line Interface

`pip install codecov-cli` · installs (wheel) · licence: not stated · rank 5155 · last release 2026-10-28 · [PyPI](https://pypi.org/project/codecov-cli/) · [docs](https://docs.codecov.com)

<details><summary>README extract</summary>

CodecovCLI is a new way for users to interact with Codecov directly from the user’s terminal or CI platform. Many Codecov features that require the user’s interference can be done via the codecovCLI. It saves commits, creates reports, uploads coverage and has many more features.

- CodecovCLI ...

Example:
```python
curl  | gpg --no-default-keyring --keyring trustedkeys.gpg --import # One-time step
curl -Os
curl -Os
curl -Os

gpgv codecov.SHA256SUM.sig codecov.SHA256SUM

shasum -a 256 -c codecov.SHA256SUM
```

Sections: CodecovCLI, Using PIP, As a Binary, Integrity Checking the Binary, How to Upload to Codecov, How to Get an Upload Token, Usage, Codecov-cli Commands, create-commit, create-report, do-upload, pr-base-picking, send-notifications, empty-upload

</details>

### covdefaults

A coverage plugin to provide sensible default settings

`pip install covdefaults` · installs (wheel) · licence: MIT License · rank 5167 · last release 2023-03-05 · [PyPI](https://pypi.org/project/covdefaults/)

<details><summary>README extract</summary>

A coverage plugin to provide sensible default settings

Example:
```python
if sys.version_info >= (3, 9):  # pragma: >=3.9 cover
    print('3.9+')
else:  # pragma: <3.9 cover
    print('old')
```

Sections: covdefaults, usage, default settings, `[coverage:run]`, `[coverage:report]`, platform specific `# pragma: no cover`, version specific `# pragma: no cover`, overriding options, `run:omit`, `run:source`, `report:exclude_lines`, `report:fail_under`

</details>

### cos-python-sdk-v5

cos-python-sdk-v5

`pip install cos-python-sdk-v5` · installs (wheel) · licence: MIT · rank 5192 · last release 2026-05-29 · [PyPI](https://pypi.org/project/cos-python-sdk-v5/)

<details><summary>README extract</summary>

___

腾讯云COSV5Python SDK, 目前可以支持Python2.6与Python2.7以及Python3.x。

安装指南

使用pip安装:
手动安装:
使用方法

使用python sdk，参照

cos最新可用地域，参照

python sdk 快速入门，参照

python sdk 接口文档，参照

</details>

### casbin-sqlalchemy-adapter

SQLAlchemy Adapter for PyCasbin

`pip install casbin-sqlalchemy-adapter` · installs (wheel) · licence: Apache Software License · rank 5196 · last release 2024-07-08 · [PyPI](https://pypi.org/project/casbin-sqlalchemy-adapter/)

<details><summary>README extract</summary>

SQLAlchemy Adapter is the SQLAlchemy adapter for PyCasbin. With this library, Casbin can load policy from SQLAlchemy supported database or save policy to it.

Based on Officially Supported Databases, The current supported databases are:

- PostgreSQL
- MySQL
- SQLite
- Oracle
- Microsoft SQL Server
- Firebird
- Sybase

Example:
```python
import casbin_sqlalchemy_adapter
import casbin

adapter = casbin_sqlalchemy_adapter.Adapter('sqlite:///test.db')

e = casbin.Enforcer('path/to/model.conf', adapter)

sub = "alice"  # the user that wants to access a resource.
obj = "data1"  # the resource that is going to be accessed.
...
```

Sections: SQLAlchemy Adapter for PyCasbin, Simple Example, Soft Delete example, Getting Help

</details>

### change-wheel-version

Change the version of a wheel file

`pip install change-wheel-version` · installs (wheel) · licence: not stated · rank 5223 · last release 2024-09-12 · [PyPI](https://pypi.org/project/change-wheel-version/) · [source](https://github.com/hauntsaninja/change_wheel_version)

<details><summary>README extract</summary>

A script to change the version of a package inside a pre-existing wheel.

This is useful for e.g. adding a local version to a custom built wheel, without having to jury rig
its build process:

Note that this only affects the packaging metadata, not any version numbers in code.

</details>

### confusables

A python package providing functionality for matching words that can be confused for eachother, but contain different characters

`pip install confusables` · installs (wheel) · licence: MIT License · rank 5339 · last release 2021-03-24 · [PyPI](https://pypi.org/project/confusables/)

<details><summary>README extract</summary>

Confusables is a python package that provides functionality for analyzing and matching words that "appear"
to be the same or similar, but use different characters.

Confusables uses the unicode confusable characters list (
along with other methods of matching characters. ...

Example:
```python
from confusables import is_confusable

print(is_confusable('rover', 'Ʀỏ𝕍3ℛ'))
# prints True
```

Sections: Confusables, Usage, Updating to the latest Unicode confusables version, About confusables

</details>

### credstash

A utility for managing secrets in the cloud using AWS KMS and DynamoDB

`pip install credstash` · installs (wheel) · licence: Apache Software License · rank 5437 · last release 2020-04-11 · [PyPI](https://pypi.org/project/credstash/)

### contextily

Context geo-tiles in Python

`pip install contextily` · installs (wheel) · licence: BSD-3-Clause · rank 5464 · last release 2026-07-10 · [PyPI](https://pypi.org/project/contextily/) · [source](https://github.com/geopandas/contextily)

<details><summary>README extract</summary>

`contextily` is a small Python 3 (3.10 and above) package to retrieve tile maps from the
internet. It can add those tiles as basemap to matplotlib figures or write tile
maps to disk into geospatial raster files. Bounding boxes can be passed in both
WGS84 (`EPSG:4326`) and Spheric Mercator (`EPSG:3857`). ...

Sections: `contextily`: context geo tiles in Python, Dependencies

</details>

### chalkpy-rs

Native Rust extension package for chalkpy

`pip install chalkpy-rs` · installs (wheel) · licence: not stated · rank 5470 · last release 2026-10-16 · [PyPI](https://pypi.org/project/chalkpy-rs/) · [docs](https://docs.chalk.ai)

<details><summary>README extract</summary>

`chalkpy-rs` is the native Rust extension package used by `chalkpy`.

The Python distribution is named `chalkpy-rs`, but it provides the
top-level import module `chalk_rs`.

Supports CPython 3.11 through 3.15. Building from source requires Rust 1.97
or newer because the bundled Ruff parser supports Python 3.15 syntax.

</details>

### check-manifest

Check MANIFEST.in in a Python source package for completeness

`pip install check-manifest` · installs (wheel) · licence: MIT License · rank 5472 · last release 2025-10-15 · [PyPI](https://pypi.org/project/check-manifest/)

<details><summary>README extract</summary>

Are you a Python developer? Have you uploaded packages to the Python Package
Index? Have you accidentally uploaded *broken* packages with some files
missing? If so, check-manifest is for you.

Sections: check-manifest, Quick start, Command-line reference, Configuration, Version control integration, 0.51 (2025-10-15), 0.50 (2024-10-09), 0.49 (2022-12-05), 0.48 (2022-03-13), 0.47 (2021-09-22), 0.46 (2021-01-04), 0.45 (2020-10-31), 0.44 (2020-10-03), 0.43 (2020-09-21)

</details>

### CurrencyConverter

A currency converter using the European Central Bank data.

`pip install CurrencyConverter` · installs (wheel) · licence: not stated · rank 5481 · last release 2026-10-31 · [PyPI](https://pypi.org/project/CurrencyConverter/)

<details><summary>README extract</summary>

This is a currency converter that uses historical rates against a reference currency (Euro). It is compatible with Python3.9+.

The default source is the European Central Bank. This is the ECB historical rates for 42 currencies against the Euro since 1999.
It can be downloaded here: eurofxref-hist.zip. ...

Example:
```python
>>> from currency_converter import CurrencyConverter
>>> c = CurrencyConverter()
```

Sections: Currency data sources, Command line tool, Python API, Data, Fallbacks, Decimal, Other attributes

</details>

### condense-json

Python function for condensing JSON using replacement strings

`pip install condense-json` · installs (wheel) · licence: Apache-2.0 · rank 5498 · last release 2026-08-03 · [PyPI](https://pypi.org/project/condense-json/)

<details><summary>README extract</summary>

Python function for condensing JSON using replacement strings and values

Example:
```python
from condense_json import condense_json

input_json = {
    "foo": {
        "bar": {
            "string": "This is a string with foxes in it",
            "nested": {
                "more": ["Here is a string", "another with foxes in it too"]
            },
        }
    }
}

replacements = {"1": "with foxes in it"}

...
```

Sections: condense-json, Usage, Structural replacements for dicts and lists, Merge references: a base object plus a patch, Escaping of `$`, `$r` and `$raw` keys

</details>

### cdsapi

Climate Data Store API

`pip install cdsapi` · installs (wheel) · licence: Apache 2.0 · rank 5514 · last release 2025-09-30 · [PyPI](https://pypi.org/project/cdsapi/)

<details><summary>README extract</summary>

cdsapi

For a more detailed description on how to use the cdsapi, please visit:

Install

Install via `pip` with::

 $ pip install cdsapi

Configure

Get your Personal Access Token from your profile on the CDS portal at the address:
and write it into the configuration file, so it looks like:: ...

</details>

### claude-code-sdk

Python SDK for Claude Code

`pip install claude-code-sdk` · installs (wheel) · licence: MIT License · rank 5564 · last release 2025-09-29 · [PyPI](https://pypi.org/project/claude-code-sdk/) · [docs](https://docs.anthropic.com/en/docs/claude-code/sdk)

<details><summary>README extract</summary>

> ⚠️ DEPRECATED: This package has been deprecated and is no longer maintained. Please migrate to the Claude Agent SDK (`claude-agent-sdk`).

Python SDK for Claude Code. See the Claude Code SDK documentation for more information.

Example:
```python
import anyio
from claude_code_sdk import query

async def main():
    async for message in query(prompt="What is 2 + 2?"):
        print(message)

anyio.run(main)
```

Sections: Claude Code SDK for Python, Quick Start, Basic Usage: query(), Using Tools, Working Directory, ClaudeSDKClient, Custom Tools (as In-Process SDK MCP Servers), Creating a Simple Tool, Benefits Over External MCP Servers, Migration from External Servers, Hooks, Example, Types, Error Handling

</details>

### cut-cross-entropy

Code for cut cross entropy, a memory efficient implementation of linear-cross-entropy loss.

`pip install cut-cross-entropy` · installs (wheel) · licence: not stated · rank 5630 · last release 2025-01-07 · [PyPI](https://pypi.org/project/cut-cross-entropy/)

<details><summary>README extract</summary>

This software project accompanies the research paper:
Cut Your Losses in Large-Vocabulary Language Models,
*Erik Wijmans, Brody Huval, Alexander Hertzberg, Vladlen Koltun, and Philipp Krähenbühl*.

As language models grow ever larger, so do their vocabularies. ...

Example:
```python
from cut_cross_entropy import linear_cross_entropy

embeddings = model.compute_embedding(inputs)
classifier = model.get_classifier_weights()

loss = linear_cross_entropy(embeddings, classifier, labels)
```

Sections: Cut Your Losses in Large-Vocabulary Language Models, Getting started, Basic usage, Transformers Integration, Training and reproducing the benchmark results

</details>

### colorthief

A module for grabbing the color palette from an image.

`pip install colorthief` · installs (wheel) · licence: BSD License · rank 5699 · last release 2017-02-09 · [PyPI](https://pypi.org/project/colorthief/)

<details><summary>README extract</summary>

Color Thief

A module for grabbing the color palette from an image.

Links

</details>

### cursor

A small Python package to hide or show the terminal cursor

`pip install cursor` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 5808 · last release 2026-11-01 · [PyPI](https://pypi.org/project/cursor/)

_README extract left out: share-alike licence._

### cerberus-python-client

A python client for interacting with Cerberus

`pip install cerberus-python-client` · installs (wheel) · licence: Apache License, v2.0 · rank 5809 · last release 2022-10-06 · [PyPI](https://pypi.org/project/cerberus-python-client/)

### cvdupdate

ClamAV Private Database Mirror Updater Tool

`pip install cvdupdate` · installs (wheel) · licence: Apache Software License · rank 5847 · last release 2025-10-03 · [PyPI](https://pypi.org/project/cvdupdate/)

<details><summary>README extract</summary>

A tool to download and update clamav databases and database patch files
for the purposes of hosting your own database mirror.
Copyright (C) 2021-2025 Cisco Systems, Inc. and/or its affiliates. All rights reserved.

This tool downloads the latest ClamAV databases along with the latest database patch files. ...

Sections: About, Requirements, Basic Usage, Cron Example, Optional Functionality, Using a custom DNS server, Using a proxy, Files and directories created by CVD-Update, Additional Usage, Get familiar with the tool, Do an update, Add an additional database, Serve it up, Test out FreshClam, Use docker

</details>

### crick

High performance approximate and streaming algorithms

`pip install crick` · installs from source (sdist only) · licence: BSD-3-Clause · rank 5886 · last release 2024-12-23 · [PyPI](https://pypi.org/project/crick/) · [source](https://github.com/dask/crick)

<details><summary>README extract</summary>

Crick is a fast library of approximate and streaming algorithms. It is still a
work in progress, use at your own risk.

</details>

### cuequivariance

CUDA accelerated equivariant operations

`pip install cuequivariance` · installs (wheel) · licence: not stated · rank 5888 · last release 2026-10-15 · [PyPI](https://pypi.org/project/cuequivariance/)

<details><summary>README extract</summary>

cuEquivariance is an NVIDIA Python library designed to facilitate the construction of high-performance geometric neural networks using segmented polynomials and triangular operations. ...

Sections: cuEquivariance, Documentation, Disclaimer

</details>

### cvc5

Python bindings for cvc5 (BSD version)

`pip install cvc5` · installs (wheel) · licence: not stated · rank 5898 · last release 2026-10-08 · [PyPI](https://pypi.org/project/cvc5/) · [docs](https://cvc5.github.io/docs/) · [source](https://github.com/cvc5/cvc5)

### cw-rpa

The cw-rpa package provides reusable functions/common utilities for developing CW RPA bots.

`pip install cw-rpa` · installs (wheel) · licence: not stated · rank 6126 · last release 2025-10-13 · [PyPI](https://pypi.org/project/cw-rpa/)

<details><summary>README extract</summary>

RPA Library is a comprehensive Python library designed to empower partners
to efficiently development of Robotic Process Automation (RPA) solutions.
This library provides essential functionalities and utilities, simplifying the RPA development process. ...

Example:
```python
# Import the library.
from cw_rpa import Input

# Initialize the module.
input = Input()

# Calling the input method.
input.get_value("<variable name>")

E.g.
username = input.get_value("username")
```

Sections: Modules Overview, Input Module, Logger Module, HttpClient Module, Benefits for Partners, Getting Started, Example, Create O365 User Bot Sample Code, Additional Resources

</details>

### cf-xarray

A convenience wrapper for using CF attributes on xarray objects

`pip install cf-xarray` · installs (wheel) · licence: Apache Software License · rank 6162 · last release 2026-06-12 · [PyPI](https://pypi.org/project/cf-xarray/) · [docs](https://cf-xarray.readthedocs.io) · [source](https://github.com/xarray-contrib/cf-xarray.git)

<details><summary>README extract</summary>

A lightweight convenience wrapper for using CF attributes on xarray objects.

For example you can use `.cf.mean("latitude")` instead of `.mean("lat")` if appropriate attributes are set! This allows you to write code that does not require knowledge of specific dimension or coordinate names particular to a dataset. ...

</details>

### celery-singleton

Prevent duplicate celery tasks

`pip install celery-singleton` · installs (wheel) · licence: MIT License · rank 6195 · last release 2021-01-14 · [PyPI](https://pypi.org/project/celery-singleton/) · [source](https://github.com/steinitzu/celery-singleton)

### cdk-ecr-deployment

CDK construct to deploy docker image to Amazon ECR

`pip install cdk-ecr-deployment` · installs (wheel) · licence: OSI Approved · rank 6242 · last release 2026-11-03 · [PyPI](https://pypi.org/project/cdk-ecr-deployment/) · [source](https://github.com/cdklabs/cdk-ecr-deployment)

<details><summary>README extract</summary>

CDK construct to synchronize single docker image between docker registries.

> [!IMPORTANT]
> Please use the latest version of this package, which is `v4`.
> (Older versions are no longer supported).

Features:
* Copy image or multi-architecture image index from ECR/external registry to (another) ECR/external registry
* Copy an archive tarball image from s3 to ECR/external registry

Example:
```python
from aws_cdk.aws_ecr_assets import DockerImageAsset

image = DockerImageAsset(self, "CDKDockerImage",
    directory=path.join(__dirname, "docker")
)

# Copy from cdk docker image asset to another ECR.
ecrdeploy.ECRDeployment(self, "DeployDockerImage1",
    src=ecrdeploy.DockerImageName(image.image_uri),
...
```

Sections: cdk-ecr-deployment, Features, Usage, Examples: examples/, API

</details>

### compoundfiles

Library for parsing and reading OLE Compound Documents

`pip install compoundfiles` · installs from source (sdist only) · licence: MIT License · rank 6284 · last release 2014-09-01 · [PyPI](https://pypi.org/project/compoundfiles/)

<details><summary>README extract</summary>

This package provides a library for reading Microsoft's Compound File Binary
format (CFB), formerly known as OLE Compound Documents, the Advanced
Authoring Format (AAF), or just plain old Microsoft Office files (the non-XML
sort). ...

Sections: compoundfiles, Links

</details>

### clusterscope

Clusterscope is a CLI and python library to extract information from HPC Clusters and Jobs.

`pip install clusterscope` · installs (wheel) · licence: not stated · rank 6293 · last release 2026-01-16 · [PyPI](https://pypi.org/project/clusterscope/)

<details><summary>README extract</summary>

Clusterscope is a CLI and python library to extract information from HPC Clusters and Jobs.

Check out our Website for Getting Started and Documentation.

Sections: Clusterscope, Citing Clusterscope

</details>

### codefind

Find code objects and their referents

`pip install codefind` · installs (wheel) · licence: not stated · rank 6298 · last release 2024-09-08 · [PyPI](https://pypi.org/project/codefind/) · [source](https://github.com/breuleux/codefind)

<details><summary>README extract</summary>

* Find code objects from filename and qualname
* Find all functions that have a certain code
* Change the code of functions
* Used by jurigged

Example:
```python
from codefind import conform

def f(x):
    return x + x

def g(x):
    return x * x

print(f(5))  # 10
conform(f, g)
print(f(5))  # 25
```

Sections: Codefind, find_code, get_functions, conform, Simple usage, Updating all closures

</details>

### curtsies

Curses-like terminal wrapper, with colored strings!

`pip install curtsies` · installs (wheel) · licence: MIT License · rank 6309 · last release 2025-06-05 · [PyPI](https://pypi.org/project/curtsies/)

<details><summary>README extract</summary>

Curtsies is a Python 3.6+ compatible library for interacting with the terminal.
This is what using (nearly every feature of) curtsies looks like:

Paste it in a `something.py` file and try it out!

Installation: `pip install curtsies`

Documentation

Primer ...

Example:
```python
import random
import sys

from curtsies import FullscreenWindow, Input, FSArray
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow

print(yellow('this prints normally, not to the alternate screen'))

with FullscreenWindow() as window:
    a = FSArray(window.height, window.width)
...
```

</details>

### cdktf

Cloud Development Kit for Terraform

`pip install cdktf` · installs (wheel) · licence: OSI Approved · rank 6336 · last release 2025-06-04 · [PyPI](https://pypi.org/project/cdktf/) · [source](https://github.com/hashicorp/terraform-cdk.git)

<details><summary>README extract</summary>

cdktf is a framework for defining cloud infrastructure using Terraform providers and modules. It allows for
users to define infrastructure resources using higher-level programming languages.

Install dependencies

Build the package

Learn More

Sections: cdktf, Build

</details>

### case-conversion

Convert between different types of cases (unicode supported)

`pip install case-conversion` · installs (wheel) · licence: MIT · rank 6358 · last release 2025-08-27 · [PyPI](https://pypi.org/project/case-conversion/) · [source](https://github.com/AlejandroFrias/case-conversion)

<details><summary>README extract</summary>

This is a port of the Sublime Text 3 plugin CaseConversion, by Davis Clark, to a regular python package. I couldn't find any other python packages on PyPI at the time (Feb 2016) that could seamlessly convert from any case to any other case without having to specify from what type of case I was converting. ...

Features:
- Auto-detection of case *(no need to specify explicitly which case you are converting from!)*
- Acronym detection *(no funky splitting on every capital letter of an all caps acronym like `HTTPError`!)* ...

Example:
```python
>>> from case_conversion import Converter
>>> converter = Converter()
>>> converter.camel("FOO_BAR_STRING")
'fooBarString'
```

Sections: Case Conversion, Features, Usage, Converter Class, Convenience Functions

</details>

### colorhash

Generate color based on any object

`pip install colorhash` · installs (wheel) · licence: MIT License · rank 6401 · last release 2026-10-22 · [PyPI](https://pypi.org/project/colorhash/)

<details><summary>README extract</summary>

ColorHash is a lightweight Python library for generating deterministic colors from objects' string representations.

By calculating a color value based on an object's hash, it ensures consistent results: the same input will always yield the same color. ...

Example:
```python
>>> from colorhash import ColorHash
>>> c = ColorHash('Hello World')
>>> c.hsl
(131, 0.65, 0.5)
>>> c.rgb
(45, 210, 75)
>>> c.hex
'#2dd24b'
```

Sections: color-hash, Quick Start, Basic (intended) use, Advanced usage, Hue mapping change in version 3.0.0

</details>

### cloudconvert

Python REST API wrapper for cloud convert

`pip install cloudconvert` · installs (wheel) · licence: MIT License · rank 6402 · last release 2022-03-30 · [PyPI](https://pypi.org/project/cloudconvert/)

<details><summary>README extract</summary>

This is the official Python SDK for the CloudConvert API v2.

Example:
```python
 import cloudconvert

cloudconvert.configure(api_key='API_KEY', sandbox=False)
```

Sections: cloudconvert-python, Creating API Client, Creating Jobs, Downloading Files, Uploading Files, Webhook Signing, Signed URLs, Unit Tests, Integration Tests, Resources

</details>

### cognite-sdk

Cognite Python SDK

`pip install cognite-sdk` · installs (wheel) · licence: Apache-2.0 · rank 6405 · last release 2026-11-02 · [PyPI](https://pypi.org/project/cognite-sdk/) · [docs](https://cognite-sdk-python.readthedocs-hosted.com)

<details><summary>README extract</summary>

This is the Cognite Python SDK for developers and data scientists working with Cognite Data Fusion (CDF).
The package is tightly integrated with pandas, and helps you work easily and efficiently with data in Cognite Data Fusion (CDF).

The SDK v8 introduces full async support with the new `AsyncCogniteClient`. This enables: ...

Example:
```python
# Async client (new in v8!)
from cognite.client import AsyncCogniteClient

async def main():
    client = AsyncCogniteClient()
    tss = await client.time_series.list()

# Sync client (still supported)
from cognite.client import CogniteClient

client = CogniteClient()
tss = client.time_series.list()
```

...

</details>

### cement

Application Framework for Python

`pip install cement` · installs (wheel) · licence: BSD License · rank 6423 · last release 2026-07-13 · [PyPI](https://pypi.org/project/cement/) · [docs](https://docs.builtoncement.com) · [source](https://github.com/datafolklabs/cement)

<details><summary>README extract</summary>

Cement is an advanced Application Framework for Python, with a primary focus on Command Line Interfaces (CLI). Its goal is to introduce a standard and feature-full platform for both simple and complex command line applications as well as support rapid development needs without sacrificing quality. ...

Sections: Cement Framework, Core Features, Optional Extensions, More Information, Devbox / Process Compose, Docker, Running Tests and Compliance

</details>

### cdk8s

This is the core library of Cloud Development Kit (CDK) for Kubernetes (cdk8s). cdk8s apps synthesize into standard Kubernetes manifests which can be applied to any Kubernetes cluster.

`pip install cdk8s` · installs (wheel) · licence: OSI Approved · rank 6439 · last release 2026-11-03 · [PyPI](https://pypi.org/project/cdk8s/) · [source](https://github.com/cdk8s-team/cdk8s-core.git)

### cache-dit

Cache-DiT: A PyTorch-native Inference Engine with Cache, Parallelism, Quantization and CPU Offload for DiTs.

`pip install cache-dit` · installs (wheel) · licence: not stated · rank 6520 · last release 2026-10-15 · [PyPI](https://pypi.org/project/cache-dit/) · [source](https://github.com/vipshop/cache-dit)

<details><summary>README extract</summary>

Parallelism, Quantization and CPU Offload for DiTs

🤗Why Cache-DiT❓❓Cache-DiT is built on top of the 🤗Diffusers library and now supports nearly ALL DiTs from Diffusers. It provides hybrid cache acceleration (DBCache, TaylorSeer, SCM, etc.) and comprehensive parallelism optimizations, including Context Parallelism, Tensor Parallelism, hybrid 2D or ...

Sections: ⚡️🎉A PyTorch-native Inference Engine with Cache,, 🤖Agentic Workflows

</details>

### comet-ml

Supercharging Machine Learning

`pip install comet-ml` · installs (wheel) · licence: MIT License · rank 6548 · last release 2026-11-04 · [PyPI](https://pypi.org/project/comet-ml/)

<details><summary>README extract</summary>

Full documentation and additional training examples are available on

Example:
```python
from comet_ml import Experiment
experiment = Experiment(api_key="YOUR_API_KEY")

# Your code.
```

Sections: Comet, Documentation, Getting started: 30 seconds to Comet.ml

</details>

### cuequivariance-ops-cu13

cuequivariance-ops - GPU Accelerated Extensions for Equivariant Primitives

`pip install cuequivariance-ops-cu13` · installs (wheel) · licence: not stated · rank 6563 · last release 2026-10-15 · [PyPI](https://pypi.org/project/cuequivariance-ops-cu13/) · [docs](https://docs.nvidia.com/cuda/cuequivariance/)

<details><summary>README extract</summary>

`cuequivariance_ops` provides CUDA kernels for the
cuEquivariance.
This python module does not contain any python bindings.
When imported, it loads the shared library that contains the CUDA kernels.

Refer to
cuEquivariance.

Sections: cuequivariance-ops, Introduction, Documentation

</details>

### copilotkit

CopilotKit python SDK

`pip install copilotkit` · installs (wheel) · licence: MIT License · rank 6570 · last release 2026-08-26 · [PyPI](https://pypi.org/project/copilotkit/) · [source](https://github.com/CopilotKit/CopilotKit/tree/main/sdk-python)

<details><summary>README extract</summary>

The official Python SDK for CopilotKit - build AI copilots and agents into your applications.

Features:
- 🚀 Easy integration with LangGraph and LangChain
- 🔄 Built-in support for stateful conversations
- 🛠 Extensible agent framework
- 🔌 FastAPI-ready endpoints
- 🤝 Optional CrewAI integration

Example:
```python
from copilotkit import Copilot

# Initialize a copilot
copilot = Copilot()

# Add your tools and configure the copilot
copilot.add_tool(my_custom_tool)

# Run the copilot
response = copilot.run("Your task description here")
```

Sections: CopilotKit Python SDK, Features, Quick Start, Documentation

</details>

### compress-pickle

Standard pickle, wrapped with standard compression libraries

`pip install compress-pickle` · installs (wheel) · licence: MIT License · rank 6597 · last release 2021-09-21 · [PyPI](https://pypi.org/project/compress-pickle/)

<details><summary>README extract</summary>

The standard pickle package provides an excellent default tool for serializing arbitrary python objects and storing them to disk. Standard python also includes broad set of data compression packages. ...

</details>

### cmcrameri

Perceptually uniform colormaps by Fabio Crameri

`pip install cmcrameri` · installs (wheel) · licence: not stated · rank 6623 · last release 2026-08-04 · [PyPI](https://pypi.org/project/cmcrameri/) · [docs](https://github.com/callumrollo/cmcrameri) · [source](https://github.com/callumrollo/cmcrameri)

<details><summary>README extract</summary>

This is a Python wrapper around Fabio Crameri's perceptually uniform colormaps.


All credit for creating the colormaps to Fabio.
Any errors in the Python implementation of colormaps are my own.

This version is based on _Scientific colour maps version 8.0 (2023-06-14).

Example:
```python
import cmcrameri.cm as cmc
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)[np.newaxis, :]

plt.imshow(x, aspect='auto', cmap=cmc.batlow)
plt.axis('off')
plt.show()
```

Sections: cmcrameri, Usage example, Extra instructions, Usage

</details>

### coverage-threshold

Tools for coverage threshold limits

`pip install coverage-threshold` · installs (wheel) · licence: MIT · rank 6652 · last release 2025-05-25 · [PyPI](https://pypi.org/project/coverage-threshold/)

<details><summary>README extract</summary>

A command line tool for checking coverage reports against configurable coverage minimums.
Currently built for use around python's coverage

Sections: coverage threshold, Usage, Config

</details>

### Collectfast

A Faster Collectstatic

`pip install Collectfast` · installs (wheel) · licence: MIT License · rank 6669 · last release 2020-06-05 · [PyPI](https://pypi.org/project/Collectfast/)

<details><summary>README extract</summary>

A faster collectstatic command.

Features

- Efficiently decide what files to upload using cached checksums
- Parallel file uploads

Supported Storage Backends

- `storages.backends.s3boto3.S3Boto3Storage`
- `storages.backends.gcloud.GoogleCloudStorage`
- `django.core.files.storage.FileSystemStorage` ...

Sections: Collectfast, Upload Strategies, Usage, Setting Up a Dedicated Cache Backend, Enable Parallel Uploads, Debugging

</details>

### cloudsmith-api

Cloudsmith API (v1)

`pip install cloudsmith-api` · installs (wheel) · licence: Apache-2.0 · rank 6685 · last release 2026-10-26 · [PyPI](https://pypi.org/project/cloudsmith-api/)

### crhelper

crhelper simplifies authoring CloudFormation Custom Resources

`pip install crhelper` · installs (wheel) · licence: Apache Software License · rank 6687 · last release 2024-10-29 · [PyPI](https://pypi.org/project/crhelper/)

<details><summary>README extract</summary>

Simplify best practice Custom Resource creation, sending responses to CloudFormation and providing exception, timeout
trapping, and detailed configurable logging.

Features:
* Dead simple to use, reduces the complexity of writing a CloudFormation custom resource
* Guarantees that CloudFormation will get a response even if an exception is raised
* Returns meaningful errors to CloudFormation Stack events in the case of a ...

Example:
```python
from future import print_function
from crhelper import CfnResource
import logging

logger = logging.getLogger(name)
# Initialise the helper, all inputs are optional, this example shows the defaults
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL', sleep_on_delete=120, ssl_verify=None)

try:
...
```

...

</details>

### cpuset-py3

Fork of cpuset (https://github.com/lpechacek/cpuset) by Alex Tsariounov that works with python3

`pip install cpuset-py3` · installs (wheel) · licence: not stated · rank 6688 · last release 2020-12-01 · [PyPI](https://pypi.org/project/cpuset-py3/)

### chalice

Microframework

`pip install chalice` · installs (wheel) · licence: Apache Software License · rank 6712 · last release 2026-10-23 · [PyPI](https://pypi.org/project/chalice/)

<details><summary>README extract</summary>

Chalice is a framework for writing serverless apps in Python. It allows
you to quickly create and deploy applications that use AWS Lambda. It provides:

* A command line tool for creating, deploying, and managing your app
* A decorator based API for integrating with Amazon API Gateway, Amazon S3,
 Amazon SNS, Amazon SQS, and other AWS services. ...

Example:
```python
from chalice import Chalice

app = Chalice(app_name="helloworld")

@app.route("/")
def index():
    return {"hello": "world"}
```

Sections: AWS Chalice, Quickstart, Credentials, Creating Your Project, Deploying, Next Steps, Feedback

</details>

### composio-langchain

Use Composio to get an array of tools with your Langchain agent.

`pip install composio-langchain` · installs (wheel) · licence: Apache Software License · rank 6748 · last release 2026-11-03 · [PyPI](https://pypi.org/project/composio-langchain/)

<details><summary>README extract</summary>

Adapts Composio tools to LangChain's `StructuredTool` format so a LangChain agent can call 1000+ apps through a single Composio session.

Example:
```python
from composio import Composio
from composio_langchain import LangchainProvider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

composio = Composio(provider=LangchainProvider())
llm = ChatOpenAI(model="gpt-5.2")

# Each session is scoped to one of your users
session = composio.create(user_id="user_123")
...
```

Sections: composio-langchain, Quickstart, Error handling, Links

</details>

### cloud-accelerator-diagnostics

Monitor, debug and profile the jobs running on Cloud accelerators like TPUs and GPUs.

`pip install cloud-accelerator-diagnostics` · installs (wheel) · licence: not stated · rank 6957 · last release 2024-10-15 · [PyPI](https://pypi.org/project/cloud-accelerator-diagnostics/)

<details><summary>README extract</summary>

<!--
 Copyright 2023 Google LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at ...

Features:
Cloud Accelerator Diagnostics is a library to monitor, debug and profile the workloads running on Cloud accelerators like TPUs and GPUs. ...

Example:
```python
from cloud_accelerator_diagnostics import tensorboard

instance_id = tensorboard.create_instance(project="test-project",
                                          location="us-central1",
                                          tensorboard_name="test-instance")
print("Vertex AI Tensorboard created: ", instance_id)
```

...

</details>

### chia-rs

(no summary)

`pip install chia-rs` · installs (wheel) · licence: not stated · rank 6958 · last release 2026-10-26 · [PyPI](https://pypi.org/project/chia-rs/)

### cohere-compass-sdk

Cohere Compass SDK

`pip install cohere-compass-sdk` · installs (wheel) · licence: not stated · rank 6962 · last release 2026-10-06 · [PyPI](https://pypi.org/project/cohere-compass-sdk/)

<details><summary>README extract</summary>

The Compass SDK is a Python library that allows you to parse documents and insert them
into a Compass index.

In order to parse documents, the Compass SDK relies on the Compass Parser API, which is
a RESTful API that receives files and returns parsed documents. This requires a hosted
Compass server. ...

Example:
```python
result = compass_client.create_index(...)
if result.error:
    # do something about the error
```

Sections: Cohere Compass SDK, Getting Started, V2 Migration Guide, Create Python Virtual Environment, Running Tests Locally, VSCode Users, Pre-commit

</details>

### cppy

(no summary)

`pip install cppy` · installs (wheel) · licence: BSD License · rank 6994 · last release 2025-02-11 · [PyPI](https://pypi.org/project/cppy/) · [docs](https://cppy.readthedocs.io/en/latest/) · [source](https://github.com/nucleic/cppy)

<details><summary>README extract</summary>

A small C++ header library which makes it easier to write Python extension
modules. The primary feature is a PyObject smart pointer which automatically
handles reference counting and provides convenience methods for performing
common object operations.

</details>

### cybrid-api-id-python

Cybrid Identity API

`pip install cybrid-api-id-python` · installs (wheel) · licence: Apache-2.0 · rank 7041 · last release 2026-11-06 · [PyPI](https://pypi.org/project/cybrid-api-id-python/)

### cybrid-api-organization-python

Cybrid Organization API

`pip install cybrid-api-organization-python` · installs (wheel) · licence: Apache-2.0 · rank 7054 · last release 2026-11-06 · [PyPI](https://pypi.org/project/cybrid-api-organization-python/)

### cybrid-api-bank-python

Cybrid Bank API

`pip install cybrid-api-bank-python` · installs (wheel) · licence: Apache-2.0 · rank 7056 · last release 2026-11-06 · [PyPI](https://pypi.org/project/cybrid-api-bank-python/)

### chromadb-client

Chroma Client.

`pip install chromadb-client` · installs (wheel) · licence: Apache Software License · rank 7073 · last release 2026-05-05 · [PyPI](https://pypi.org/project/chromadb-client/)

<details><summary>README extract</summary>

Chroma - the open-source data infrastructure for AI.

 This package is for the Python HTTP client-only library for Chroma. This client connects to the Chroma Server. If that it not what you are looking for, you might want to check out the full library. ...

Example:
```python
import chromadb
# Example setup of the client to connect to your chroma server
client = chromadb.HttpClient(host="localhost", port=8000)

collection = client.create_collection("all-my-documents")

collection.add(
    documents=["This is document1", "This is document2"],
...
```

</details>

### cuequivariance-jax

CUDA accelerated equivariant operations

`pip install cuequivariance-jax` · installs (wheel) · licence: not stated · rank 7104 · last release 2026-10-15 · [PyPI](https://pypi.org/project/cuequivariance-jax/)

<details><summary>README extract</summary>

cuEquivariance is an NVIDIA Python library designed to facilitate the construction of high-performance geometric neural networks using segmented polynomials and triangular operations. ...

Sections: cuEquivariance, Documentation, Disclaimer

</details>

### cn2an

Convert Chinese numerals and Arabic numerals.

`pip install cn2an` · installs (wheel) · licence: MIT License · rank 7115 · last release 2026-04-22 · [PyPI](https://pypi.org/project/cn2an/)

<details><summary>README extract</summary>

📦 `cn2an` 是一个快速转化 `中文数字` 和 `阿拉伯数字` 的工具包！

> 🎈 `v0.5.24 update`: fix numeral parsing and transform edge cases
> 🎈 `en2an`: 「英文数字」和「阿拉伯数字」互转正在收集需求中！ 详情
> 🎈 `Cn2An.jl`: Julia 语言版本已经上线，正在丰富基础功能。详情

- 支持 `中文数字` => `阿拉伯数字`；
- 支持 `大写中文数字` => `阿拉伯数字`；
- 支持 `中文数字和阿拉伯数字` => `阿拉伯数字`；
- 支持 `中文数字` => `阿拉伯数字字符串` 的原样直译；

Example:
```python
# 在文件首部引入包
import cn2an

# 查看当前版本号
print(cn2an.version)
# 0.5.24
```

Sections: cn2an: Chinese Numerals To Arabic Numerals, 1 功能, 1.1 `中文数字` => `阿拉伯数字`, 1.2 `阿拉伯数字` => `中文数字`, 1.3 句子转化, 1.4 其他, 2 安装, 2.1 使用 pip 安装, 2.2 从代码库安装, 3 使用, 3.1 `中文数字` => `阿拉伯数字`, 3.2 `阿拉伯数字` => `中文数字`, 3.3 句子转化, 3.4 HTTP API

</details>

### client-signals

Privacy-safe client signals for CLI HTTP traffic.

`pip install client-signals` · installs (wheel) · licence: MIT · rank 7129 · last release 2026-10-26 · [PyPI](https://pypi.org/project/client-signals/)

<details><summary>README extract</summary>

Python implementation of the shared `client-signals` contract.

Example:
```python
import client_signals

signals = client_signals.detect_once()
headers = {}

client_signals.apply_headers(headers, signals)
headers["User-Agent"] = f"my-cli/1.0 {client_signals.user_agent_suffix(signals)}"
```

Sections: client-signals for Python, Usage, API

</details>

### Chameleon

Fast HTML/XML Template Compiler.

`pip install Chameleon` · installs (wheel) · licence: BSD-like (http://repoze.org/license.html) · rank 7187 · last release 2024-12-31 · [PyPI](https://pypi.org/project/Chameleon/) · [docs](https://chameleon.readthedocs.io)

<details><summary>README extract</summary>

Chameleon is an HTML/XML template engine for Python. It uses the *page templates* language.

You can use it in any Python application with just about any
version of Python (3.9+ and up, plus pypy 3).

Visit the documentation
for more information.

Example:
```python
In the example above, `name` is an identifier, while `value` and
`attrs` are Python expressions. However, `attrs` must evaluate
to a Python dictionary object (more concisely, the value must
implement the dictionary API-methods `update()` and `items()`).
```

Sections: Chameleon, Notes, Changes, 4.6.0 (2024-12-31), 4.5.4 (2024-04-08), 4.5.3 (2024-04-05), 4.5.2 (2024-01-29), 4.5.1 (2024-01-28), 4.5.0 (2024-01-18), 4.4.4 (2024-01-18), 4.4.3 (2023-12-30), 4.4.2 (2023-12-18), 4.4.1 (2023-12-18), 4.4.0 (2023-12-12)

</details>

### cuequivariance-ops-jax-cu13

cuequivariance-ops-jax - GPU Accelerated JAX Extensions for Equivariant Primitives

`pip install cuequivariance-ops-jax-cu13` · installs (wheel) · licence: not stated · rank 7197 · last release 2026-10-15 · [PyPI](https://pypi.org/project/cuequivariance-ops-jax-cu13/) · [docs](https://docs.nvidia.com/cuda/cuequivariance/)

<details><summary>README extract</summary>

`cuequivariance_ops_jax` provides CUDA kernels for the
cuEquivariance project's JAX
components. As such, it contains JAX bindings to optimized kernels that
cuEquivariance's operations map down to. In general, we advice that you access
those kernels through cuEquivariance, but you may also find them useful on
their own.

Example:
```python
import cuequivariance_ops_jax
```

Sections: cuequivariance-ops-jax, Introduction, Documentation, Usage

</details>

### chiavdf

Chia vdf verification (wraps C++)

`pip install chiavdf` · installs (wheel) · licence: Apache-2.0 · rank 7266 · last release 2026-10-29 · [PyPI](https://pypi.org/project/chiavdf/)

<details><summary>README extract</summary>

chiavdf implements the Verifiable Delay Function used by Chia's timelord. It
builds on Linux (x86_64 and arm64), macOS (Intel and Apple Silicon), and
Windows (x64), and produces:

- `vdf_client` - the CPU software timelord client.
- `vdf_bench` - a CPU benchmark for estimating iterations per second. ...

Sections: Chia VDF, What this repository provides, macOS, Windows, Linux, Run a timelord, Software timelord (CPU), Hardware timelord (Chia VDF ASIC), Building the Python wheel, Building Timelord and related binaries, Fuzzing, Historical background

</details>

### conventional-pre-commit

A pre-commit hook that checks commit messages for Conventional Commits formatting.

`pip install conventional-pre-commit` · installs (wheel) · licence: not stated · rank 7272 · last release 2026-10-29 · [PyPI](https://pypi.org/project/conventional-pre-commit/) · [source](https://github.com/compilerla/conventional-pre-commit)

<details><summary>README extract</summary>

A `pre-commit` hook to check commit messages for
Conventional Commits formatting.

Works with Python >= 3.8.

Sections: conventional-pre-commit, Usage, Passing `args`, Versioning

</details>

### color-matcher

Package enabling color transfer across images

`pip install color-matcher` · installs (wheel) · licence: GNU GPL V3.0 · rank 7331 · last release 2025-03-30 · [PyPI](https://pypi.org/project/color-matcher/)

_README extract left out: share-alike licence._

### cmake-format

Can format your listfiles so they don't look like crap

`pip install cmake-format` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 7350 · last release 2020-08-19 · [PyPI](https://pypi.org/project/cmake-format/)

_README extract left out: share-alike licence._

### clvm-tools-rs

tools for working with chialisp language; compiler, repl, python and wasm bindings

`pip install clvm-tools-rs` · installs (wheel) · licence: Apache-2.0 · rank 7351 · last release 2025-07-31 · [PyPI](https://pypi.org/project/clvm-tools-rs/) · [source](https://github.com/Chia-Network/clvm_tools_rs)

<details><summary>README extract</summary>

This repo can be installed via cargo

 cargo install clvm_tools_rs

or via pip

 pip install clvm_tools_rs@git+

Note: `pip` installs a subset of the tools installed by `cargo`, including `brun`, `run`, `opc` and `opd`.

The most current version of the language is in the nightly branch:

 nightly

To install from a specific branch: ...

Sections: clvm_tools_rs, Mac M1, Use with chia-blockchain

</details>

### cocotb-bus

(no summary)

`pip install cocotb-bus` · installs (wheel) · licence: not stated · rank 7354 · last release 2026-01-15 · [PyPI](https://pypi.org/project/cocotb-bus/)

<details><summary>README extract</summary>

cocotb-bus contains pre-packaged testbenching tools and
reusable bus interfaces for cocotb.

</details>

### clvm-rs

Implementation of `clvm` for Chia Network's cryptocurrency

`pip install clvm-rs` · installs (wheel) · licence: Apache-2.0 · rank 7367 · last release 2026-11-06 · [PyPI](https://pypi.org/project/clvm-rs/) · [source](https://github.com/Chia-Network/clvm_rs/)

<details><summary>README extract</summary>

Rust implementation of clvm.

The cargo workspace includes an rlib crate, for use with rust or other applications, and a python wheel.

The python wheel is in `wheel`. The npm package is in `wasm`.

In order to run the unit tests, run:

The fuzzing infrastructure for `clvm_rs` uses cargo-fuzz. ...

Sections: Tests, Fuzzing, Build Wheel, Bumping Version Number

</details>

### cwsandbox

A Python client library for CoreWeave Sandbox

`pip install cwsandbox` · installs (wheel) · licence: Apache-2.0 · rank 7386 · last release 2026-11-06 · [PyPI](https://pypi.org/project/cwsandbox/)

<details><summary>README extract</summary>

A Python client library for CWSandboxes.

See the documentation site for the full tutorial, guides, and API reference.

Example:
```python
from cwsandbox import Sandbox

# Quick one-liner with factory method (sync/async hybrid API)
sb = Sandbox.run("echo", "Hello, World!")
sb.stop().result()  # Block for completion

# Context manager for automatic cleanup
with Sandbox.run("sleep", "infinity", container_image="python:3.11") as sb:
...
```

Sections: cwsandbox-client, Documentation, Quick Start, Command-line interface, Sandbox data connections, Authentication, Embedding in a long-running host

</details>

### cuml-cu12

NVIDIA cuML: GPU-Accelerated Machine Learning

`pip install cuml-cu12` · installs (wheel) · licence: Apache-2.0 · rank 7444 · last release 2026-10-08 · [PyPI](https://pypi.org/project/cuml-cu12/) · [docs](https://docs.nvidia.com/cuml/latest/)

<details><summary>README extract</summary>

NVIDIA cuML is an open-source CUDA-X Data Science library for
GPU-accelerated machine learning. It provides two ways to run machine learning
workloads on NVIDIA GPUs:

- The `cuml` Python API provides GPU-native estimators with familiar
 scikit-learn-style APIs and direct control over machine learning workflows. ...

Example:
```python
from cuml.datasets import make_blobs
from cuml.cluster import DBSCAN

# Create sample data
X, y = make_blobs(n_samples=100, centers=3, n_features=2, random_state=42)

# Fit clustering model
dbscan = DBSCAN(eps=1.0, min_samples=5)
dbscan.fit(X)
print(dbscan.labels)
```

Sections: NVIDIA cuML: GPU-Accelerated Machine Learning, Use the GPU-native `cuml` API, Accelerate existing code with `cuml.accel`, Scale beyond one GPU, Scikit-learn compatibility

</details>

### cpe

CPE: Common Platform Enumeration for Python

`pip install cpe` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 7469 · last release 2024-10-02 · [PyPI](https://pypi.org/project/cpe/)

_README extract left out: share-alike licence._

### chiapos

Chia proof of space plotting, proving, and verifying (wraps C++)

`pip install chiapos` · installs (wheel) · licence: Apache-2.0 · rank 7500 · last release 2025-11-05 · [PyPI](https://pypi.org/project/chiapos/)

<details><summary>README extract</summary>

Chia's proof of space is written in C++. Includes a plotter, prover, and
verifier. It exclusively runs on 64 bit architectures. Read the
Proof of Space document to
learn about what proof of space is and how it works.

Sections: Chia Proof of Space, C++ Usage Instructions, Compile, Static Compilation With glibc, Statically compile ProofOfSpace, Run tests, CLI usage, Benchmark, Hellman Attacks usage, Python binding, Run python tests, Rust binding, ci Building

</details>

### cargo-zigbuild

(no summary)

`pip install cargo-zigbuild` · installs (wheel) · licence: not stated · rank 7633 · last release 2026-11-04 · [PyPI](https://pypi.org/project/cargo-zigbuild/)

### classify-imports

Utilities for refactoring imports in python-like syntax.

`pip install classify-imports` · installs (wheel) · licence: MIT · rank 7648 · last release 2026-07-10 · [PyPI](https://pypi.org/project/classify-imports/)

<details><summary>README extract</summary>

Utilities for refactoring imports in python-like syntax.

Example:
```python
>>> from classify_imports import import_obj_from_str
>>> obj = import_obj_from_str('import foo, bar, baz')
>>> [str(i) for i in obj.split()]
['import foo\n', 'import bar\n', 'import baz\n']
```

Sections: classify-imports, examples, splitting an import object, sorting import objects, classify a module

</details>

### cvxpy-base

A domain-specific language for modeling convex optimization problems in Python.

`pip install cvxpy-base` · installs (wheel) · licence: Apache-2.0 · rank 7653 · last release 2026-09-19 · [PyPI](https://pypi.org/project/cvxpy-base/)

<details><summary>README extract</summary>

The CVXPY documentation is at cvxpy.org.

*We are building a CVXPY community on Discord. Join the conversation! For issues and long-form discussions, use Github Issues and Github Discussions.*

Contents
- Installation
- Getting started
- Issues
- Community
- Contributing
- Team
- Citing ...

Example:
```python
import cvxpy as cp
import numpy

# Problem data.
m = 30
n = 20
numpy.random.seed(1)
A = numpy.random.randn(m, n)
b = numpy.random.randn(m)

# Construct the problem.
x = cp.Variable(n)
objective = cp.Minimize(cp.sum_squares(A @ x - b))
constraints = [0 <= x, x <= 1]
prob = cp.Problem(objective, constraints)

...
```

Sections: CVXPY, Getting started, Issues, Team, Citing

</details>

### chiabip158

Chia BIP158 (wraps C++)

`pip install chiabip158` · installs (wheel) · licence: Apache License · rank 7670 · last release 2025-11-06 · [PyPI](https://pypi.org/project/chiabip158/)

<details><summary>README extract</summary>

This implements the compact block filter construction in BIP 158. The code is
not used anywhere in the Bitcoin Core code base yet. The next step towards
BIP 157 support would be to create an indexing module similar to TxIndex that
constructs the basic and extended filters for each validated block.

Sections: Chia BIP158, Run python tests, ci Building

</details>

### casbin-async-sqlalchemy-adapter

Asynchronous SQLAlchemy Adapter for PyCasbin

`pip install casbin-async-sqlalchemy-adapter` · installs (wheel) · licence: Apache Software License · rank 7678 · last release 2025-12-10 · [PyPI](https://pypi.org/project/casbin-async-sqlalchemy-adapter/)

<details><summary>README extract</summary>

Asynchronous SQLAlchemy Adapter is the SQLAlchemy adapter for PyCasbin. With this library, Casbin can load policy from SQLAlchemy supported database or save policy to it.

Based on Officially Supported Databases, The current supported databases are:

- PostgreSQL
- MySQL
- MariaDB
- SQLite
- Oracle
- Microsoft SQL Server
- Firebird

Example:
```python
import casbin_async_sqlalchemy_adapter
import casbin

adapter = casbin_async_sqlalchemy_adapter.Adapter('sqlite+aiosqlite:///test.db')

# or mysql example
# adapter = casbin_async_sqlalchemy_adapter.Adapter('mysql+aiomysql://user:pwd@127.0.0.1:3306/exampledb')

e = casbin.AsyncEnforcer('path/to/model.conf', adapter)

...
```

...

</details>

### collate-sqllineage

Collate SQL Lineage for Analysis Tool powered by Python and sqlfluff based on sqllineage.

`pip install collate-sqllineage` · installs (wheel) · licence: MIT License · rank 7690 · last release 2026-11-05 · [PyPI](https://pypi.org/project/collate-sqllineage/)

<details><summary>README extract</summary>

SQL Lineage Analysis Tool powered by Python.

This is a fork authored by the OpenMetadata community, where we are adding `sqlfluff` as a parsing backend instead of `sqlparse`.

Never get the hang of a SQL parser? SQLLineage comes to the rescue. ...

Example:
```python
$ sqllineage -e "insert into db1.table1 select * from db2.table2"
Statements(#): 1
Source Tables:
    db2.table2
Target Tables:
    db1.table1
```

Sections: SQLLineage, Demo & Documentation, Quick Start, Advanced Usage, Multiple SQL Statements, Verbose Lineage Result, Dialect-Awareness Lineage, Column-Level Lineage, Lineage Visualization

</details>

### circus

Circus is a program that will let you run and watch multiple processes and sockets.

`pip install circus` · installs (wheel) · licence: Apache Software License · rank 7745 · last release 2025-02-13 · [PyPI](https://pypi.org/project/circus/) · [docs](https://circus.readthedocs.io) · [source](https://github.com/circus-tent/circus)

<details><summary>README extract</summary>

Circus is a program that runs and watches processes and sockets.
Circus can be used as a library or through the command line.

- Full Documentation
- How to Contribute
- IRC: Freenode, channel #mozilla-circus

Sections: Circus, Links

</details>

### cql2

Parse, validate, and convert Common Query Language (CQL2) text and JSON

`pip install cql2` · installs (wheel) · licence: MIT · rank 7770 · last release 2026-11-04 · [PyPI](https://pypi.org/project/cql2/)

<details><summary>README extract</summary>

Python library and command-line interface (CLI) for parsing and converting Common Query Language (CQL2), with Rust under the hood.

Example:
```python
from cql2 import Expr, parse_file

expr = Expr("landsat:scene_id = 'LC82030282019133LGN00'")
# or
expr = parse_file("examples/text/example01.txt")

s = expr.to_text()
d = expr.to_json()
sql = expr.to_sql()
print("cql2-text:", s)
print("cql2-json:", d)
print("SQL:", sql)
```

Sections: cql2, Usage, More information

</details>

### cachy

Cachy provides a simple yet effective caching library.

`pip install cachy` · installs (wheel) · licence: MIT License · rank 7771 · last release 2019-08-06 · [PyPI](https://pypi.org/project/cachy/) · [source](https://github.com/sdispater/cachy)

<details><summary>README extract</summary>

Cachy provides a simple yet effective caching library.

The full documentation is available here:

* Documentation
* Issue Tracker

Sections: Cachy, Resources

</details>

### cupti-python

NVIDIA CUPTI Python Library

`pip install cupti-python` · installs (wheel) · licence: Other/Proprietary License · rank 7783 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cupti-python/) · [docs](https://docs.nvidia.com/cupti-python/13.5.0/index.html)

<details><summary>README extract</summary>

CUPTI Python provides Python APIs for creation of profiling and tracing tools that target CUDA Python applications
This release of CUPTI Python supports a subset of CUPTI C Activity, Callback, PM Sampling, and Profiler Host APIs.
Refer the documentation for more details.

</details>

### clean-text

Functions to preprocess and normalize text.

`pip install clean-text` · installs (wheel) · licence: Apache Software License · rank 7838 · last release 2026-01-28 · [PyPI](https://pypi.org/project/clean-text/)

<details><summary>README extract</summary>

User-generated content on the Web and in social media is often dirty. Preprocess your scraped data with `clean-text` to create a normalized text representation. For instance, turn this corrupted input:

into this clean output:

`clean-text` uses ftfy, unidecode and numerous hand-crafted rules, i.e., RegEx.

Example:
```python
from cleantext import clean

clean("some input",
    fix_unicode=True,               # fix various unicode errors
    to_ascii=True,                  # transliterate to closest ASCII representation
    lower=True,                     # lowercase text
    no_line_breaks=False,           # fully strip line breaks as opposed to only normalizing them
...
```

...

</details>

### chatterbox-tts

Chatterbox: Open Source TTS and Voice Conversion by Resemble AI

`pip install chatterbox-tts` · installs (wheel) · licence: not stated · rank 7840 · last release 2026-03-26 · [PyPI](https://pypi.org/project/chatterbox-tts/) · [source](https://github.com/resemble-ai/chatterbox)

<details><summary>README extract</summary>

*Made with ♥️ by*

Chatterbox is a family of three state-of-the-art, open-source text-to-speech models by Resemble AI.

We are excited to introduce Chatterbox-Turbo, our most efficient model yet. Built on a streamlined 350M parameter architecture, Turbo delivers high-quality speech with less compute and VRAM than our previous models. ...

Example:
```python
import torchaudio as ta
import torch
from chatterbox.tts_turbo import ChatterboxTurboTTS

# Load the Turbo model
model = ChatterboxTurboTTS.from_pretrained(device="cuda")

# Generate with Paralinguistic Tags
text = "Hi there, Sarah here from MochaFone calling you back [chuckle], have you got one minute to chat about the billing issue?"

...
```

...

</details>

### cognitojwt

Decode and verify Amazon Cognito JWT tokens

`pip install cognitojwt` · installs (wheel) · licence: MIT License · rank 7845 · last release 2021-06-07 · [PyPI](https://pypi.org/project/cognitojwt/)

<details><summary>README extract</summary>

Example:
```python
import cognitojwt

id_token = '<YOUR_TOKEN_HERE>'
REGION = '-**-*'
USERPOOL_ID = 'eu-west-1***'
APP_CLIENT_ID = '1p3*****'

# Sync mode
verified_claims: dict = cognitojwt.decode(
    id_token,
    REGION,
    USERPOOL_ID,
    app_client_id=APP_CLIENT_ID,  # Optional
    testmode=True  # Disable token expiration check for testing purposes
)

...
```

Sections: Decode and verify Amazon Cognito JWT tokens, Usage

</details>

### civis

Civis API Python Client

`pip install civis` · installs (wheel) · licence: BSD-3-Clause · rank 7851 · last release 2026-10-06 · [PyPI](https://pypi.org/project/civis/) · [source](https://github.com/civisanalytics/civis-python)

<details><summary>README extract</summary>

The Civis API Python client is a Python package that helps analysts
and developers interact with Civis Platform programmatically. The package includes a set of
tools around common workflows as well as a convenient interface to make
requests directly to the Civis API.

Please see the
full documentation for more details. ...

Example:
```python
import civis
df = civis.io.read_civis(table="my_schema.my_table",
                         database="database",
                         return_as="pandas")
```

Sections: Civis API Python Client, API Keys, Linux / MacOS, Windows, Usage, Building Documentation, Command-line Interface (CLI)

</details>

### conda-package-streaming

An efficient library to read from new and old format .conda and .tar.bz2 conda packages.

`pip install conda-package-streaming` · installs (wheel) · licence: BSD License · rank 7973 · last release 2026-06-08 · [PyPI](https://pypi.org/project/conda-package-streaming/) · [docs](https://conda.github.io/conda-package-streaming/)

<details><summary>README extract</summary>

An efficient library to read from new and old format .conda and .tar.bz2 conda
packages.

Download conda metadata from packages without transferring entire file. Get
metadata from local `.tar.bz2` packages without reading entire files. ...

Example:
```python
from conda_package_streaming.url import stream_conda_info

# url = (ends with .conda or .tar.bz2)
for tar, member in stream_conda_info(url):
    if member.name == "info/index.json":
        index_json = json.load(tar.extractfile(member))
        break
```

Sections: conda-package-streaming, Quickstart, Package goals, Generating documentation

</details>

### click-completion

Fish, Bash, Zsh and PowerShell completion for Click

`pip install click-completion` · installs from source (sdist only) · licence: MIT · rank 7977 · last release 2019-10-15 · [PyPI](https://pypi.org/project/click-completion/)

### canonicaljson

Canonical JSON

`pip install canonicaljson` · installs (wheel) · licence: Apache Software License · rank 8020 · last release 2023-03-15 · [PyPI](https://pypi.org/project/canonicaljson/)

<details><summary>README extract</summary>

Features:
* Encodes objects and arrays as RFC 7159 JSON.
* Sorts object keys so that you get the same result each time.
* Has no insignificant whitespace to make the output as small as possible. ...

Example:
```python
import canonicaljson
assert canonicaljson.encode_canonical_json({}) == b'{}'
```

Sections: Canonical JSON, Features, Using

</details>

### census

A wrapper for the US Census Bureau's API

`pip install census` · installs (wheel) · licence: BSD License · rank 8045 · last release 2026-05-15 · [PyPI](https://pypi.org/project/census/)

<details><summary>README extract</summary>

A simple wrapper for the United States Census Bureau's API.

Provides access to ACS and SF1 data sets.

Example:
```python
from census import Census
from us import states

c = Census("MY_API_KEY")
c.acs5.get(('NAME', 'B25034_010E'),
          {'for': 'state:{}'.format(states.MD.fips)})
```

Sections: census, Usage, Datasets, Geographies, ACS5 Geographies, ACS1 Geographies, SF1 Geographies, PL Geographies, States, BYOS - Bring Your Own Session, Examples

</details>

### click-command-tree

click plugin to show the command tree of your CLI

`pip install click-command-tree` · installs (wheel) · licence: MIT License · rank 8064 · last release 2024-03-25 · [PyPI](https://pypi.org/project/click-command-tree/)

<details><summary>README extract</summary>

`click-command-tree` is a click plugin to show the command tree of your CLI

Installation

This is tested against Python versions 3.8 - 3.12 and (latest major release) click versions
5.x, 6.x, 7.x, 7.1.x, 8.0.x, and 8.1.x.

Example

Releasing:
1. update `version` variable, and in `setup.py`
1. git commit new version
1. make publish-dist

Example:
```python
from pkg_resources import iter_entry_points

import click
from click_plugins import with_plugins

@with_plugins(iter_entry_points('click_command_tree'))
@click.group()
def root():
    pass

@root.group()
def command_group():
    pass

@command_group.command()
def nested_command():
    pass

@root.command()
def standard_command():
    pass

...
```

</details>

### crochet

Use Twisted anywhere!

`pip install crochet` · installs (wheel) · licence: MIT License · rank 8166 · last release 2023-07-01 · [PyPI](https://pypi.org/project/crochet/)

<details><summary>README extract</summary>

Crochet is an MIT-licensed library that makes it easier to use Twisted from
regular blocking code. Some use cases include:

* Easily use Twisted from a blocking framework like Django or Flask.
* Write a library that provides a blocking API, but uses Twisted for its
 implementation. ...

Sections: Crochet: Use Twisted anywhere!, API and features, What's New, 2.1.0, 2.0.0, 1.12.0, 1.11.0, 1.10.0, 1.9.0, 1.8.0, 1.7.0, 1.6.0, 1.5.0, 1.4.0

</details>

### causal-learn

causal-learn Python Package

`pip install causal-learn` · installs (wheel) · licence: MIT License · rank 8178 · last release 2026-07-11 · [PyPI](https://pypi.org/project/causal-learn/)

<details><summary>README extract</summary>

Causal-learn (documentation, paper) is an open-source platform for causal learning with both classical and state-of-the-art causal discovery algorithms. It aims to recover causal structure from observational data, without requiring interventional experiments, while offering provable correctness guarantees.

The package is actively being developed. ...

Sections: News, Package Overview, Documentation, Running examples, Benchmarks, Running Tetrad in Python

</details>

### conjure-python-client

Conjure Python Library

`pip install conjure-python-client` · installs (wheel) · licence: Apache Software License · rank 8256 · last release 2026-10-14 · [PyPI](https://pypi.org/project/conjure-python-client/)

### can-ada

Ada is a fast spec-compliant url parser

`pip install can-ada` · installs (wheel) · licence: MIT · rank 8306 · last release 2026-01-28 · [PyPI](https://pypi.org/project/can-ada/)

<details><summary>README extract</summary>

[Fast] Python bindings for Ada, a fast and WHATWG spec-compliant URL parser.
This is the URL parser used in projects like Node.js.

Example:
```python
from can_ada import parse

url = parse("
print(url.protocol) # https:
print(url.host) # tkte.ch
print(url.pathname) # /search
print(url.search) # ?q=canada
```

Sections: can_ada, WHATWG URL compliance, Usage, Performance

</details>

### conditional

Conditionally enter a context manager

`pip install conditional` · installs (wheel) · licence: BSD-2-Clause · rank 8382 · last release 2026-07-04 · [PyPI](https://pypi.org/project/conditional/) · [docs](https://conditional.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

Features:
The `conditional` context manager comes handy when you always want to
execute a with-block but only conditionally want to apply its context
manager.

If you find yourself writing code like this:

Consider replacing it with:

Example:
```python
from conditional import conditional

with conditional(has_pager(cmd), ignoresignals()):
    os.system(cmd)
```

Sections: conditional, Conditionally enter a context manager, Overview, Async, Typing, Examples, Documentation, 2.2 - 2026-07-04, 2.1 - 2026-07-04, 2.0 - 2024-05-14, 1.5 - 2023-09-14, 1.4 - 2022-03-09, 1.3 - 2019-01-28, 1.2 - 2017-02-05

</details>

### click-config-file

Configuration file support for click applications.

`pip install click-config-file` · installs (wheel) · licence: MIT License · rank 8417 · last release 2020-04-29 · [PyPI](https://pypi.org/project/click-config-file/)

<details><summary>README extract</summary>

Easily add configuration file support to your
Click applications by adding a single
no-arguments decorator.

Features:
There are several existing implementations of config file support for
Click, however they seem to lack one or more of the following features:

- Sensible defaults
- Proper handling of resolution order ...

Example:
```python
@click.command()
@click.option('--name', default='World', help='Who to greet.')
@click_config_file.configuration_option()
def hello(name):
    click.echo('Hello {}!'.format(name))
```

Sections: Click config file, Basic usage, Options, Why?

</details>

### cloud-tpu-diagnostics

Monitor, debug and profile the jobs running on Cloud TPU.

`pip install cloud-tpu-diagnostics` · installs (wheel) · licence: not stated · rank 8426 · last release 2023-12-08 · [PyPI](https://pypi.org/project/cloud-tpu-diagnostics/)

<details><summary>README extract</summary>

This is a comprehensive library to monitor, debug and profile the jobs running on Cloud TPU.
To learn about Cloud TPU, refer to the full documentation.

Example:
```python
from cloud_tpu_diagnostics import diagnostic
from cloud_tpu_diagnostics.configuration import debug_configuration
from cloud_tpu_diagnostics.configuration import diagnostic_configuration
from cloud_tpu_diagnostics.configuration import stack_trace_configuration
```

Sections: Cloud TPU Diagnostics, Features, 1. Debugging, 1.1 Collect Stack Traces, Usage, Scenario 1: Do not collect stack traces on faults

</details>

### cisco-ai-mcp-scanner

A tool to scan MCP servers and tools for security findings

`pip install cisco-ai-mcp-scanner` · installs (wheel) · licence: not stated · rank 8642 · last release 2026-10-20 · [PyPI](https://pypi.org/project/cisco-ai-mcp-scanner/) · [docs](https://github.com/cisco-ai-defense/mcp-scanner#readme) · [source](https://github.com/cisco-ai-defense/mcp-scanner)

<details><summary>README extract</summary>

A Python tool for scanning MCP (Model Context Protocol) servers and tools for potential security findings. The MCP Scanner combines Cisco AI Defense inspect API, YARA rules and LLM-based analysis to detect malicious MCP tools.

Features:
The MCP Scanner provides a comprehensive solution for scanning MCP servers and tools for security findings. It leverages three powerful scanning engines (Yara, LLM-based analysis, Cisco AI Defense) that can be used together or independently. ...

Example:
```python
import asyncio
import os
from mcpscanner import Config, Scanner, set_log_level
from mcpscanner.core.models import AnalyzerEnum
import logging

async def main():
    # Suppress all mcpscanner logs below ERROR
    set_log_level(logging.ERROR)

    # Create configuration with your API keys
...

</details>

### crytic-compile

Util to facilitate smart contracts compilation.

`pip install crytic-compile` · installs (wheel) · licence: AGPL-3.0-only · rank 8701 · last release 2026-07-28 · [PyPI](https://pypi.org/project/crytic-compile/)

_README extract left out: share-alike licence._

### conllu

CoNLL-U Parser parses a CoNLL-U formatted string into a nested python dictionary

`pip install conllu` · installs (wheel) · licence: not stated · rank 8728 · last release 2024-10-13 · [PyPI](https://pypi.org/project/conllu/)

<details><summary>README extract</summary>

CoNLL-U Parser parses a CoNLL-U formatted string into a nested python dictionary. CoNLL-U is often the output of natural language processing tasks.

Features:
- It's simple. ~300 lines of code.
- It has no dependencies
- Full typing support so your editor can do autocompletion

- It has 100% test branch coverage (and has undergone mutation testing)
- It has

Example:
```python
>>> from conllu import parse
>>>
>>> data = """
... # text = The quick brown fox jumps over the lazy dog.
... 1   The     the    DET    DT   Definite=Def|PronType=Art   4   det     _   _
... 2   quick   quick  ADJ    JJ   Degree=Pos                  4   amod    _   _
... 3   brown   brown  ADJ    JJ   Degree=Pos                  4   amod    _   _
...
```

...

</details>

### clingo

CFFI-based bindings to the clingo solver.

`pip install clingo` · installs (wheel) · licence: MIT · rank 8732 · last release 2026-11-03 · [PyPI](https://pypi.org/project/clingo/)

<details><summary>README extract</summary>

This package provides CFFI-based bindings to the clingo solver.

Clingo is part of the Potassco project for *Answer Set
Programming* (ASP). ASP offers a simple and powerful modeling language to
describe combinatorial problems as *logic programs*. ...

</details>

### comfyui-manager

ComfyUI-Manager provides features to install and manage custom nodes for ComfyUI, as well as various functionalities to assist with ComfyUI.

`pip install comfyui-manager` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 8738 · last release 2026-09-18 · [PyPI](https://pypi.org/project/comfyui-manager/) · [source](https://github.com/ltdrdata/ComfyUI-Manager)

_README extract left out: share-alike licence._

### commented-configparser

A custom ConfigParser class that preserves comments and most formatting when writing loaded config out.

`pip install commented-configparser` · installs (wheel) · licence: MIT · rank 8740 · last release 2026-10-25 · [PyPI](https://pypi.org/project/commented-configparser/)

<details><summary>README extract</summary>

A custom ConfigParser class that preserves comments and most formatting when
writing loaded config out.

This library gives you a custom class of the standard library's
`configparser.ConfigParger` which will preserve the comments of a loaded config
file when writing that file back out.

Example:
```python
from commentedconfigparser import CommentedConfigParser

# Load the config like normal
config = CommentedConfigParser()
config.read("myconfig.ini")

# Use the config like normal
...

# Update the config like normal
...

# Save the config back to the file
with open("myconfig.ini", "w") as savefile:
    config.write(savefile)
```

Sections: commented-configparser, Example use, Results, Before, After

</details>

### celery-stubs

celery stubs

`pip install celery-stubs` · installs (wheel) · licence: MIT License · rank 8834 · last release 2023-02-10 · [PyPI](https://pypi.org/project/celery-stubs/)

### chargehound

Chargehound Python Bindings

`pip install chargehound` · installs from source (sdist only) · licence: MIT · rank 8896 · last release 2021-02-08 · [PyPI](https://pypi.org/project/chargehound/)

<details><summary>README extract</summary>

Example:
```python
import chargehound
chargehound.api_key = '{ YOUR_API_KEY }'
```

Sections: Chargehound python bindings, Usage, Requests, Response, Documentation, Deployment

</details>

### cargo-lambda

Cargo subcommand to work with AWS Lambda

`pip install cargo-lambda` · installs (wheel) · licence: MIT · rank 8971 · last release 2026-08-21 · [PyPI](https://pypi.org/project/cargo-lambda/) · [source](https://github.com/cargo-lambda/cargo-lambda)

<details><summary>README extract</summary>

cargo-lambda is a Cargo subcommand to help you work with AWS Lambda.

Get started by looking at the documentation.

</details>

### cli-ui

Build Nice User Interfaces In The Terminal

`pip install cli-ui` · installs (wheel) · licence: BSD License · rank 8975 · last release 2025-03-29 · [PyPI](https://pypi.org/project/cli-ui/)

<details><summary>README extract</summary>

Tools for nice user interfaces in the terminal.

This project was originally hosted on the TankerHQ organization, which was my employer from 2016
to 2021. They kindly agreed to give back ownership of this project to
me. Thanks!

See python-cli-ui documentation.

Example:
```python
import cli_ui

# coloring:
cli_ui.info(
  "This is",
  cli_ui.red, "red", cli_ui.reset,
  "and this is",
  cli_ui.bold, "bold"
)

# enumerating:
list_of_things = ["foo", "bar", "baz"]
for i, thing in enumerate(list_of_things):
    cli_ui.info_count(i, len(list_of_things), thing)

# progress indication:
cli_ui.info_progress("Done",  5, 20)
...
```

Sections: python-cli-ui, Note, Documentation, Demo, Usage, Uploading documentation

</details>

### cruft

Allows you to maintain all the necessary cruft for packaging and building projects separate from the code you intentionally write. Built on-top of CookieCutter.

`pip install cruft` · installs (wheel) · licence: MIT · rank 8984 · last release 2024-12-25 · [PyPI](https://pypi.org/project/cruft/)

<details><summary>README extract</summary>

_____

Features:
* Cookiecutter Compatible: cruft utilizes Cookiecutter as its template expansion engine. Meaning it retains full compatibility with all existing Cookiecutter templates. ...

Sections: Key Features, Creating a New Project, Updating a Project, Updating Values of Template Variables, Update Variables via the Command Line, Update Variables via a Cruft File, Checking a Project, Linking an Existing Project, Compute the diff, Automating updates with GitHub Actions, Why Create cruft?

</details>

### copernicusmarine

Command line interface and Python API for accessing Copernicus Marine data and related services.

`pip install copernicusmarine` · installs (wheel) · licence: not stated · rank 8990 · last release 2026-11-03 · [PyPI](https://pypi.org/project/copernicusmarine/)

<details><summary>README extract</summary>

Features:
The Copernicus Marine Toolbox offers capabilities through both Command Line Interface (CLI) and Python API:

- Metadata Information: List and retrieve metadata information on all products, datasets, variables. ...

Sections: Copernicus Marine Service Toolbox (CLI & Python), Features, Documentation, Mamba | Conda, Pip, Docker, Dependencies, Command Line Interface (CLI), The `--help` option, Python package (API), Version management, Future improvements & Roadmap

</details>

### customerio-cdp-analytics

Customer.io Data Pipelines (CDP) Python bindings.

`pip install customerio-cdp-analytics` · installs (wheel) · licence: MIT · rank 9114 · last release 2026-10-20 · [PyPI](https://pypi.org/project/customerio-cdp-analytics/)

<details><summary>README extract</summary>

﻿# Customer.io Data Pipelines analytics client for Python.

Example:
```python
from customerio import analytics

analytics.write_key = 'YOUR_WRITE_KEY'

analytics.track(user_id=4, event='order_complete')
```

Sections: Usage, Other Regions, Documentation

</details>

### composio-langgraph

Use Composio to get array of tools with LangGraph Agent Workflows.

`pip install composio-langgraph` · installs (wheel) · licence: Apache Software License · rank 9151 · last release 2026-11-03 · [PyPI](https://pypi.org/project/composio-langgraph/)

<details><summary>README extract</summary>

Adapts Composio tools to LangChain's `StructuredTool` format for use in LangGraph agents and graph workflows, giving them access to 1000+ apps through a single Composio session.

Example:
```python
from composio import Composio
from composio_langgraph import LanggraphProvider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

composio = Composio(provider=LanggraphProvider())
llm = ChatOpenAI(model="gpt-5.2")

# Each session is scoped to one of your users
session = composio.create(user_id="user_123")
...
```

Sections: composio-langgraph, Quickstart, Error handling, Links

</details>

### coralogix-opentelemetry

coralogix extentions for opentelemetry

`pip install coralogix-opentelemetry` · installs (wheel) · licence: not stated · rank 9241 · last release 2024-02-11 · [PyPI](https://pypi.org/project/coralogix-opentelemetry/)

<details><summary>README extract</summary>

coralogix opentelemetry contribution for python

</details>

### copychat

Easily copy code for LLM context

`pip install copychat` · installs (wheel) · licence: MIT · rank 9243 · last release 2025-06-19 · [PyPI](https://pypi.org/project/copychat/)

<details><summary>README extract</summary>

Simple code-to-context.

Copychat is a lightweight CLI tool that prepares your code for conversations with LLMs. It intelligently formats your source files into chat-ready context, handling everything from file selection to git diffs.

Features:
- 🎯 Smart file selection: Automatically identifies relevant source files while respecting `.gitignore`
- 🔍 Git-aware: Can include diffs and focus on changed files
- 📦 GitHub integration: Pull directly from repositories ...

Sections: Copychat 📋🐈‍⬛, Features, Running Copychat, Quick Start, MCP Server, Usage Guide, Basic Directory Scanning, Targeting Specific Files, Filtering by Language, Working with Git, Excluding Files, GitHub Integration, Reading GitHub Repositories, Reading GitHub Issues, PRs & Discussions

</details>

### cydifflib

Fast implementation of difflib's algorithms

`pip install cydifflib` · installs from source (sdist only) · licence: MIT · rank 9303 · last release 2025-04-11 · [PyPI](https://pypi.org/project/cydifflib/) · [source](https://github.com/rapidfuzz/CyDifflib.git)

<details><summary>README extract</summary>

The following benchmark compares the performance in the original difflib implementation, the library cdifflib and CyDifflib

Example:
```python
# from difflib import SequenceMatcher
from cydifflib import SequenceMatcher
```

Sections: CyDifflib, 🚀 Benchmarks, Source builds, 📖 Usage

</details>

### codex-app-server-sdk

Async Python client for Codex app-server over stdio and websocket.

`pip install codex-app-server-sdk` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 9305 · last release 2026-09-23 · [PyPI](https://pypi.org/project/codex-app-server-sdk/) · [docs](https://emsi.github.io/codex-app-server-sdk/) · [source](https://github.com/emsi/codex-app-server-sdk)

_README extract left out: share-alike licence._

### cssmin

A Python port of the YUI CSS compression algorithm.

`pip install cssmin` · installs from source (sdist only) · licence: UNKNOWN · rank 9348 · last release 2013-10-14 · [PyPI](https://pypi.org/project/cssmin/)

### crayons

TextUI colors for Python.

`pip install crayons` · installs (wheel) · licence: MIT License · rank 9349 · last release 2020-08-26 · [PyPI](https://pypi.org/project/crayons/)

<details><summary>README extract</summary>

This module is really simple, it gives you colored strings for terminal
usage. Included colors are `red`, `green`, `yellow`, `blue`, `black`, `magenta`, `cyan`, `white`, and
`normal` (as well as `clean` and `disable`). ...

Features:
- If you call `disable()`, all future calls to colors will be ignored.
- If you call `normal()`, color is reset to default foreground color
- If the current process is not in a TTY (e.g. being piped), no colors will be displayed. ...

Example:
```python
# red is red, white is white.
>>> print('{} white'.format(crayons.red('red')))
red white
```

Sections: Crayons: Text UI colors for Python., Features, Usage is simple

</details>

### class-resolver

Lookup and instantiate classes with style.

`pip install class-resolver` · installs (wheel) · licence: MIT · rank 9353 · last release 2026-09-29 · [PyPI](https://pypi.org/project/class-resolver/) · [docs](https://class_resolver.readthedocs.io) · [source](https://github.com/cthoyt/class-resolver.git)

<details><summary>README extract</summary>

Lookup and instantiate classes with style.

Example:
```python
from class_resolver import ClassResolver
from dataclasses import dataclass

class Base:
    pass

@dataclass
class A(Base):
    name: str

@dataclass
class B(Base):
    name: str

# Index
resolver = ClassResolver([A, B], base=Base)

# Lookup
assert A == resolver.lookup("A")

# Instantiate with a dictionary
...
```

Sections: Class Resolver, 💪 Getting Started, 👋 Attribution, 🍪 Cookiecutter, Pre-commit, 📖 Building the Documentation, Initial Configuration, Configuring ReadTheDocs, Configuring Archival on Zenodo, Registering with the Python Package Index (PyPI), Configuring your machine's connection to PyPI, Uploading to PyPI, Releasing on GitHub, Updating Package Boilerplate

</details>

### censusgeocode

Thin Python wrapper for the US Census Geocoder

`pip install censusgeocode` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 9406 · last release 2026-02-08 · [PyPI](https://pypi.org/project/censusgeocode/)

_README extract left out: share-alike licence._

### chialisp

(no summary)

`pip install chialisp` · installs (wheel) · licence: not stated · rank 9437 · last release 2026-10-15 · [PyPI](https://pypi.org/project/chialisp/)

### cambc

Cambridge Battlecode CLI

`pip install cambc` · installs (wheel) · licence: not stated · rank 9578 · last release 2026-11-04 · [PyPI](https://pypi.org/project/cambc/)

<details><summary>README extract</summary>

Portable Cambridge Battlecode command line tools.

</details>

### ceja

PySpark string and phonetic matching

`pip install ceja` · installs (wheel) · licence: not stated · rank 9631 · last release 2023-02-23 · [PyPI](https://pypi.org/project/ceja/)

### cuequivariance-torch

CUDA accelerated equivariant operations

`pip install cuequivariance-torch` · installs (wheel) · licence: not stated · rank 9748 · last release 2026-10-15 · [PyPI](https://pypi.org/project/cuequivariance-torch/)

<details><summary>README extract</summary>

cuEquivariance is an NVIDIA Python library designed to facilitate the construction of high-performance geometric neural networks using segmented polynomials and triangular operations. ...

Sections: cuEquivariance, Documentation, Disclaimer

</details>

### cmap

Scientific colormaps for python, without dependencies

`pip install cmap` · installs (wheel) · licence: BSD-3-Clause · rank 9772 · last release 2026-10-20 · [PyPI](https://pypi.org/project/cmap/) · [docs](https://cmap-docs.rtfd.io/) · [source](https://github.com/pyapp-kit/cmap)

<details><summary>README extract</summary>

Scientific colormaps for python, with no dependencies beyond numpy.

With `cmap`, you can use any of the colormaps from
matplotlib,
cmocean,
colorbrewer,
crameri,
seaborn, and a host
of other collections in your python code, without having to install matplotlib
or any other dependencies beyond numpy.

:book: See the complete
catalog ...

Example:
```python
from cmap import Color

red = Color("red")  # or a variety of other "color like" inputs
```

Sections: cmap, Usage, `cmap.Color`, `cmap.Colormap`, Alternatives, References and Further reading

</details>

### clamav-client

Python client library for the ClamAV antivirus.

`pip install clamav-client` · installs (wheel) · licence: GPL-2.0 · rank 9793 · last release 2026-03-05 · [PyPI](https://pypi.org/project/clamav-client/) · [docs](https://github.com/artefactual-labs/clamav-client/blob/main/README.md) · [source](https://github.com/artefactual-labs/clamav-client)

_README extract left out: share-alike licence._

### clean-fid

FID calculation in PyTorch with proper image resizing and quantization steps

`pip install clean-fid` · installs (wheel) · licence: BSD License · rank 9860 · last release 2022-12-18 · [PyPI](https://pypi.org/project/clean-fid/)

<details><summary>README extract</summary>

Project | Paper |
Colab-FID |
Colab-Resize |
Leaderboard Tables

Quick start: Calculate FID | Calculate KID

[New] Computing the FID using CLIP features [[Kynkäänniemi et al, 2022]]( is now supported. See here for more details.

The FID calculation involves many steps that can produce inconsistencies in the final metric. ...

Example:
```python
from cleanfid import fid
score = fid.compute_fid(fdir1, fdir2)
```

Sections: clean-fid for Evaluating Generative Models, Corresponding Manuscript, Quick Start, Computing FID, Computing CLIP-FID, Computing KID, Create Custom Dataset Statistics, Backwards Compatibility, Building clean-fid locally from source, CleanFID Leaderboard for common tasks, CIFAR-10 (few shot), CIFAR-100 (few shot), FFHQ, AFHQ (Few Shot Generation)

</details>

### cellpose

anatomical segmentation algorithm

`pip install cellpose` · installs (wheel) · licence: BSD License · rank 9918 · last release 2026-06-14 · [PyPI](https://pypi.org/project/cellpose/)

<details><summary>README extract</summary>

Cellpose-SAM: cell and nucleus segmentation with superhuman generalization. It can be optimized for your own data, applied in 3D, works on images with shot noise, (an)isotropic blur, undersampling, contrast inversions, regardless of channel order and object sizes.

To learn about Cellpose-SAM read the paper or watch the talk. ...

Sections: Cellpose, star2: v4.2+ update (June 2026) :star2, Old updates, v3.1+ update (Feb 2025), star2: v3 (Feb 2024) :star2, star2: v2.0 (April 2022) :star2, System requirements, Dependencies, GPU version (CUDA) on Windows or Linux, Run cellpose locally, Step-by-step demo, 3D segmentation, Download of pretrained models

</details>

### casttube

YouTube chromecast api

`pip install casttube` · installs (wheel) · licence: MIT · rank 9920 · last release 2020-04-08 · [PyPI](https://pypi.org/project/casttube/)

<details><summary>README extract</summary>

casttube provides a way to interact with the Youtube Chromecast api.

Install:

Features
* Play video
* Play a playlist
* Add video to the end of the play queue
* Play next
* Remove video
* Clear the entire queue

The library requires 2 things:
1. screen id
2. The Chromecast youtube app needs to be open ...

Example:
```python
from casttube import YouTubeSession
session = YouTubeSession(screen_id)

# YouTube video id is
session.play_video(video_id)
```

</details>

### cotyledon

Cotyledon provides a framework for defining long-running services.

`pip install cotyledon` · installs (wheel) · licence: Apache-2.0 · rank 9923 · last release 2025-12-23 · [PyPI](https://pypi.org/project/cotyledon/)

<details><summary>README extract</summary>

Cotyledon provides a framework for defining long-running services.

It provides handling of Unix signals, spawning of workers, supervision of
children processes, daemon reloading, sd-notify, rate limiting for worker
spawning, and more.

* Free software: Apache license

Features:
This library is mainly used in OpenStack Telemetry projects, in replacement of
*oslo.service*. However, as *oslo.service* depends on *eventlet*, a different
library was needed for project that do not need it. ...

Sections: Cotyledon, Why Cotyledon

</details>

### commitlint

commitlint is a pre-commit hook designed to lint your commit messages according to the Conventional Commits standard.

`pip install commitlint` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 9963 · last release 2026-07-29 · [PyPI](https://pypi.org/project/commitlint/) · [source](https://github.com/opensource-nepal/commitlint)

_README extract left out: share-alike licence._

### coinbase-advanced-py

Coinbase Advanced API Python SDK

`pip install coinbase-advanced-py` · installs (wheel) · licence: Apache Software License · rank 10017 · last release 2026-06-19 · [PyPI](https://pypi.org/project/coinbase-advanced-py/)

<details><summary>README extract</summary>

Welcome to the official Coinbase Advanced API Python SDK. This python project was created to allow coders to easily plug into the Coinbase Advanced API.
This SDK also supports easy connection to the Coinbase Advanced Trade WebSocket API. ...

Example:
```python
from coinbase.rest import RESTClient

client = RESTClient() # Uses environment variables for API key and secret
```

Sections: Coinbase Advanced API Python SDK, REST API Client, Using the REST Client, Custom Response Objects, Passing in additional parameters, Generic REST Calls, Rate Limit Response Headers, WebSocket API Client, WebSocket User API Client, Using the WebSocket Client, Automatic Reconnection to the WebSocket API, Catching WebSocket Exceptions, Async WebSocket Client, WebSocket Response Types

</details>

### cdp-sdk

CDP SDK

`pip install cdp-sdk` · installs (wheel) · licence: MIT · rank 10018 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cdp-sdk/)

<details><summary>README extract</summary>

Example:
```python
from cdp import CdpClient
import asyncio

async def main():
    async with CdpClient() as cdp:
        pass

asyncio.run(main())
```

Sections: CDP SDK, Documentation, API Keys, Usage, Initialization, Load client config from shell, Load client config from `.env` file, Pass the API Key and Wallet Secret to the client, Client Lifecycle, Creating EVM or Solana accounts, Create an EVM account as follows, Import an EVM account as follows, Create a Solana account as follows, Import a Solana account as follows

</details>

### capsolver

capsolver python libary

`pip install capsolver` · installs (wheel) · licence: MIT License · rank 10116 · last release 2023-07-20 · [PyPI](https://pypi.org/project/capsolver/)

<details><summary>README extract</summary>

Capsolver official python library

Example:
```python
from pathlib import Path
import os
import base64
import capsolver

# tokenTask
print("api host",capsolver.api_base)
print("api key",capsolver.api_key)
# capsolver.api_key = "..."
solution = capsolver.solve({
        "type":"ReCaptchaV2TaskProxyLess",
        "websiteKey":"6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
        "websiteURL":"
    })

...
```

Sections: Capsolver, Usage

</details>

### cloudsnorkel.cdk-github-runners

CDK construct to create GitHub Actions self-hosted runners. Creates ephemeral runners on demand. Easy to deploy and highly customizable.

`pip install cloudsnorkel.cdk-github-runners` · installs (wheel) · licence: OSI Approved · rank 10149 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cloudsnorkel.cdk-github-runners/) · [source](https://github.com/CloudSnorkel/cdk-github-runners.git)

<details><summary>README extract</summary>

Use this CDK construct to create ephemeral self-hosted GitHub runners on-demand inside your AWS account.

* 🧩 Easy to configure GitHub integration with a web-based interface
* 🧠 Customizable runners with decent defaults
* 🏃🏻 Multiple runner configurations controlled by labels
* 🔐 Everything fully hosted in your account
* 🔃 Automatically updated ...

Example:
```python
let vpc: ec2.Vpc;
let runnerSg: ec2.SecurityGroup;
let dbSg: ec2.SecurityGroup;
let bucket: s3.Bucket;

// create a custom CodeBuild provider
const myProvider = new CodeBuildRunnerProvider(this, 'codebuild runner', {
   labels: ['my-codebuild'],
   vpc: vpc,
   securityGroups: [runnerSg],
});
// grant some permissions to the provider
...
```

...

</details>

### composio-core

[DEPRECATED] Core package to act as a bridge between composio platform and other services. Please use 'composio' instead.

`pip install composio-core` · installs (wheel) · licence: Apache Software License · rank 10203 · last release 2026-10-22 · [PyPI](https://pypi.org/project/composio-core/)

<details><summary>README extract</summary>

`composio-core` is the legacy Composio Python SDK and no longer receives updates.
The current SDK requires Python 3.11 or newer.

Remove the legacy package before installing the current SDK. Both packages use
the `composio` import name and must not be installed together.

See the migration guide
to update an existing integration.

</details>

### clickhouse-connect-core

Compiled Rust native-format codec for clickhouse-connect

`pip install clickhouse-connect-core` · installs (wheel) · licence: Apache-2.0 · rank 10278 · last release 2026-10-16 · [PyPI](https://pypi.org/project/clickhouse-connect-core/) · [docs](https://clickhouse.com/docs/integrations/language-clients/python/rust-codec) · [source](https://github.com/ClickHouse/clickhouse-connect)

<details><summary>README extract</summary>

Compiled Rust codec for clickhouse-connect. This wheel provides the `_ch_core` extension module that decodes ClickHouse `FORMAT Native` query results and encodes inserts.

This package is not meant to be used directly. Install it through the `rust` extra of the main driver:

Then enable the codec on a client:

The codec is experimental and opt in. ...

Example:
```python
import clickhouse_connect

client = clickhouse_connect.get_client(host="localhost", native_codec="rust")
```

</details>

### cron-schedule-triggers

Cron Schedule Triggers ~ A library for determining Quartz Cron schedule trigger dates.

`pip install cron-schedule-triggers` · installs (wheel) · licence: MIT License · rank 10279 · last release 2019-11-08 · [PyPI](https://pypi.org/project/cron-schedule-triggers/)

<details><summary>README extract</summary>

Cron Schedule Triggers (CSTriggers) is a Python library enabling the ability to determine the next execution of a live schedule. Its syntax is that of Quartz Job Scheduler. This library is not a scheduling app or a task queue, there are plenty of those in the wild to choose from. ...

Example:
```python
from cstriggers.core.trigger import QuartzCron

schedule_string = "0 0 0 1 JAN-MAR ? 2010-2030"
start_date = "2019-10-13T00:00:00"
end_date = "2022-10-13T00:00:00"
cron_obj = QuartzCron(schedule_string=schedule_string, start_date=start_date, end_date=end_date)

print(cron_obj.next_trigger(isoformat=True))
```

Sections: This library is for those who, Example usage, Roadmap

</details>

### construct-classes

Parse your binary structs into dataclasses

`pip install construct-classes` · installs (wheel) · licence: MIT · rank 10285 · last release 2026-03-31 · [PyPI](https://pypi.org/project/construct-classes/) · [source](https://github.com/matejcik/construct-classes)

<details><summary>README extract</summary>

Parse your binary data into dataclasses. Pack your dataclasses into binary data.

construct-classes rely on construct for parsing and packing. The
programmer needs to manually write the Construct expressions. There is also no type
verification, so it is the programmer's responsibility that the dataclass and the
Construct expression match. ...

Example:
```python
import construct as c
from construct_classes import Struct, subcon

class BasicStruct(Struct):
    x: int
    y: int
    description: str

    SUBCON = c.Struct(
        "x" / c.Int32ul,
        "y" / c.Int32ul,
        "description" / c.PascalString(c.Int8ul, "utf8"),
    )

data = b"\x01\x00\x00\x00\x02\x00\x00\x00\x05hello"
...
```

Sections: construct-classes, Usage, Footer

</details>

### ccimport

a tiny package for fast python c++ binding build.

`pip install ccimport` · installs (wheel) · licence: MIT License · rank 10287 · last release 2024-10-15 · [PyPI](https://pypi.org/project/ccimport/)

<details><summary>README extract</summary>

a tiny package for fast python c++ binding build.

ccimport 0.2.x support python 3.5.
ccimport >= 0.3 support python 3.6-3.10.

Example:
```python
build_meta = ccimport.BuildMeta()
build_meta.add_global_includes(...)
build_meta.add_global_cflags(...)
build_meta.add_ldflags(...)

lib = ccimport([path1, path2], out_path, build_meta)
```

Sections: ccimport, Usage, Usage in setup.py

</details>

### causalml

Python Package for Uplift Modeling and Causal Inference with Machine Learning Algorithms

`pip install causalml` · installs from source (sdist only) · licence: Apache Software License · rank 10373 · last release 2026-10-12 · [PyPI](https://pypi.org/project/causalml/)

<details><summary>README extract</summary>

This project is stable and being incubated for long-term support. It may contain new experimental code, for which APIs are subject to change.

Causal ML is a Python package that provides a suite of uplift modeling and causal inference methods using machine learning algorithms based on recent
research [[1]](#Literature). ...

Sections: Disclaimer, Documentation, Quickstart, Example Notebooks, Benchmark Datasets and Leaderboard, Versioning, References, Workshops, Talks, and Publications, Literature, Related projects

</details>

### ci-info

Continuous Integration Information

`pip install ci-info` · installs (wheel) · licence: MIT License · rank 10396 · last release 2026-02-02 · [PyPI](https://pypi.org/project/ci-info/)

<details><summary>README extract</summary>

A Python implementation of watson/ci-info.
Get details about the current Continuous Integration environment.

Please open an issue
if your CI server isn't properly detected :)

Example:
```python
import ci_info
if ci_info.is_ci():
    print(ci_info.name())

"My CI Name"
```

Sections: ci-info, Usage, API, `ci_info.name()`, `ci_info.is_ci()`, `ci_info.is_pr()`, `ci_info.info()`

</details>

### causal-conv1d

Causal depthwise conv1d in CUDA, with a PyTorch interface

`pip install causal-conv1d` · installs from source (sdist only) · licence: BSD License · rank 10407 · last release 2026-08-20 · [PyPI](https://pypi.org/project/causal-conv1d/)

<details><summary>README extract</summary>

Features:
- Support fp32, fp16, bf16.
- Kernel size 2, 3, 4.

Example:
```python
from causal_conv1d import causal_conv1d_fn
```

Sections: Causal depthwise conv1d in CUDA with a PyTorch interface, How to use, Additional Prerequisites for AMD cards, Patching ROCm

</details>

### confluent-kafka-stubs

Stub files for confluent-kafka.

`pip install confluent-kafka-stubs` · installs (wheel) · licence: Apache Software License · rank 10444 · last release 2023-06-12 · [PyPI](https://pypi.org/project/confluent-kafka-stubs/) · [source](https://gitlab.com/theepic-dev/confluent-kafka-stubs)

<details><summary>README extract</summary>

This package only contains type hints for the `confluent-kafka` python package. It may be useful to add type checking for `mypy`, or autocompletion in your *language server*.

This package is not endorsed by Confluent.

Sections: confluent-kafka-stubs, Updating

</details>

### coverage_enable_subprocess

enable python coverage for subprocesses

`pip install coverage_enable_subprocess` · installs (wheel) · licence: MIT License · rank 10457 · last release 2016-05-11 · [PyPI](https://pypi.org/project/coverage_enable_subprocess/)

<details><summary>README extract</summary>

This package installs a pth file that enables the coveragepy process_startup
feature in this python prefix/virtualenv in subsequent runs.

See:

Demo::

 $ virtualenv tmpenv
 $ . ...

</details>

### chunkr-ai

Python client for Chunkr: open source document intelligence

`pip install chunkr-ai` · installs (wheel) · licence: not stated · rank 10498 · last release 2025-08-06 · [PyPI](https://pypi.org/project/chunkr-ai/)

<details><summary>README extract</summary>

This provides a simple interface to interact with the Chunkr API.

Example:
```python
from chunkr_ai import Chunkr

# Initialize client
chunkr = Chunkr()

# Upload a file and wait for processing
task = chunkr.upload("document.pdf")
print(task.task_id)

# Create task without waiting
task = chunkr.create_task("document.pdf")
result = task.poll()  # Check status when needed

# Clean up when done
chunkr.close()
```

Sections: Chunkr Python Client, Getting Started, Usage, Synchronous Usage, Asynchronous Usage, Concurrent Processing, Input Types, Configuration, Available Configuration Examples, Environment Setup, Resource Management

</details>

### compress-json

The missing Python utility to read and write large compressed JSONs.

`pip install compress-json` · installs from source (sdist only) · licence: MIT License · rank 10504 · last release 2024-10-26 · [PyPI](https://pypi.org/project/compress-json/)

<details><summary>README extract</summary>

The missing Python utility to read and write compressed JSONs.

The library is loosely based on the compress_pickle library.

Example:
```python
import compress_json

D = {
    "A": {
        "B": "C"
    }
}
compress_json.dump(D, "filepath.json.gz")   # for a gzip file
compress_json.dump(D, "filepath.json.bz")   # for a bz2 file
compress_json.dump(D, "filepath.json.lzma") # for a lzma file
compress_json.dump(D, "filepath.json.xz") # for a lzma file

...
```

Sections: compress_json, Available compression modes, Usage example, Some extra perks: local loading and dumping, Loading with RAM cache, Advanced usage

</details>

### connector-sdk-types

Generated types for the Lumos Connector SDK

`pip install connector-sdk-types` · installs (wheel) · licence: Apache-2.0 · rank 10536 · last release 2026-11-03 · [PyPI](https://pypi.org/project/connector-sdk-types/) · [docs](https://developers.lumos.com/reference/the-lumos-connector-api)

<details><summary>README extract</summary>

This package contains the generated types for the Lumos Connector SDK. These types are automatically generated from the TypeSpec definitions and provide type-safe interfaces for all connector operations.

Example:
```python
from connector_sdk_types import ListAccountsRequest, ListAccountsResponse
```

Sections: Connector SDK Types, Usage, Generated Types, Note

</details>

### cassidy

String case conversion, identification and parsing

`pip install cassidy` · installs (wheel) · licence: not stated · rank 10563 · last release 2021-10-29 · [PyPI](https://pypi.org/project/cassidy/)

### capstone6pwndbg

Capstone disassembly engine

`pip install capstone6pwndbg` · installs (wheel) · licence: BSD License · rank 10601 · last release 2026-08-27 · [PyPI](https://pypi.org/project/capstone6pwndbg/)

<details><summary>README extract</summary>

To install Capstone, you should run `pip install capstone`.

If you would like to build and install Capstone with just the source distribution,
just run `python -m pip install .`, considering you are in the folder with setup.py in it.

In order to use this source distribution, you will need an environment that can
compile C code. ...

</details>

### cody-special

High-precision error functions and normal distribution (Cody's algorithm)

`pip install cody-special` · installs (wheel) · licence: MIT License · rank 10630 · last release 2026-01-13 · [PyPI](https://pypi.org/project/cody-special/) · [source](https://github.com/vollib/cody-special)

<details><summary>README extract</summary>

High-precision error functions and normal distribution implementations based on W.J. Cody's rational Chebyshev approximations.

Example:
```python
from cody_special import erf_cody, erfc_cody, erfcx_cody
from cody_special import norm_pdf, norm_cdf, inverse_norm_cdf

# Error functions
erf_cody(1.0)      # ~ 0.8427
erfc_cody(1.0)     # ~ 0.1573
erfcx_cody(1.0)    # ~ 0.4276

# Normal distribution
norm_pdf(0.0)           # ~ 0.3989 (standard normal PDF)
...
```

Sections: cody-special, Usage, References

</details>

### cdk-certbot-dns-route53

Create Cron Job Via Lambda, to update certificate and put it to S3 Bucket.

`pip install cdk-certbot-dns-route53` · installs (wheel) · licence: OSI Approved · rank 10638 · last release 2026-08-22 · [PyPI](https://pypi.org/project/cdk-certbot-dns-route53/) · [source](https://github.com/neilkuan/cdk-certbot-dns-route53.git)

<details><summary>README extract</summary>

cdk-certbot-dns-route53 is a CDK construct library that allows you to create Certbot Lambda Function on AWS with CDK, and setting schedule cron job to renew certificate to store on S3 Bucket.

Sections: cdk-certbot-dns-route53, Example: Invoke Lambda Function log., Example: Renew certificate to store on S3 Bucket

</details>

### cyscale

Cython SCALE Codec Library

`pip install cyscale` · installs (wheel) · licence: Apache-2.0 · rank 10649 · last release 2026-08-09 · [PyPI](https://pypi.org/project/cyscale/) · [source](https://github.com/thewhaleking/cy-scale-codec)

<details><summary>README extract</summary>

Cython-accelerated SCALE codec library for Substrate-based blockchains (Polkadot, Kusama, Bittensor, etc.), with no external runtime dependencies.

Originally a drop-in replacement for py-scale-codec — same `scalecodec` module name, compiled with Cython — cyscale has since diverged and is no longer drop-in compatible: its decode paths produce ...

Sections: cyscale, Compatibility with py-scale-codec, Performance, Primitives and small types, Large payloads, batch_decode (cyscale-only API), Examples of different types

</details>

### codeflash

Client for codeflash.ai - automatic code performance optimization, powered by AI

`pip install codeflash` · installs (wheel) · licence: not stated · rank 10716 · last release 2026-05-30 · [PyPI](https://pypi.org/project/codeflash/)

<details><summary>README extract</summary>

Codeflash is a general purpose optimizer for Python that helps you improve the performance of your Python code while maintaining its correctness.
It uses advanced LLMs to generate multiple optimization ideas for your code, tests them to be correct and benchmarks them for performance. ...

Sections: Quick Start, Documentation, Demo

</details>

### configurator

A library for building a configuration store from one or more layered configuration sources

`pip install configurator` · installs (wheel) · licence: MIT License · rank 10725 · last release 2023-09-13 · [PyPI](https://pypi.org/project/configurator/)

<details><summary>README extract</summary>

This is a Python library for building a configuration store
from one or more layered configuration sources.
These are most commonly files, with YAML, TOML and JSON support included
and other formats easily added.
The sources don't have to be files, and support is included for both environment
variables and command line options. ...

Example:
```python
from configurator import Config

defaults = Config({
    'cache': {
        'location': '/tmp/my_app',
        'max_files': 100,
    },
    'banner': 'default banner',
    'threads': 1,
})
system = Config.from_path('/etc/my_app/config.yaml')
user = Config.from_path('~/.my_app.yaml', optional=True)
config = defaults + system + user
```

Sections: configurator, Quickstart

</details>

### cdk-gitlab-runner

Use AWS CDK to create a gitlab runner, and use gitlab runner to help you execute your Gitlab pipeline job.

`pip install cdk-gitlab-runner` · installs (wheel) · licence: OSI Approved · rank 10730 · last release 2026-06-16 · [PyPI](https://pypi.org/project/cdk-gitlab-runner/) · [source](https://github.com/neilkuan/cdk-gitlab-runner.git)

<details><summary>README extract</summary>

Use AWS CDK to create gitlab runner, and use gitlab runner to help you execute your Gitlab Pipeline Job.

> GitLab Runner is the open source project that is used to run your CI/CD jobs and send the results back to GitLab. (source repo)

Features:
Gitlab provides 400 minutes per month for each free user, hosted Gitlab Runner to execute your gitlab pipeline job.That's pretty good and users don't need to manage gitlab runner. If it is just a simple ci job for test 400, it may be enough. ...

Example:
```python
import { GitlabContainerRunner } from 'cdk-gitlab-runner';

// If want change instance type to t3.large .
new GitlabContainerRunner(this, 'runner-instance', { gitlabtoken: 'glrt-GITLABTOKEN', ec2type:'t3.large',gitlabRunnerVersion: '15.10' });
// OR
...

</details>

### cmocean

Colormaps for Oceanography

`pip install cmocean` · installs (wheel) · licence: not stated · rank 10797 · last release 2024-04-06 · [PyPI](https://pypi.org/project/cmocean/)

<details><summary>README extract</summary>

<!-- -->
<!-- -->

Documentation available:

We have a paper with guidelines to colormap selection for your application and a description of the `cmocean` colormaps:
Thyng, K. M., Greene, C. A., Hetland, R. D., Zimmerle, H. M., & DiMarco, S. F. (2016). True colors of oceanography. Oceanography, 29(3), 10.
link: ...

</details>

### cheap-repr

Better version of repr/reprlib for short, cheap string representations.

`pip install cheap-repr` · installs (wheel) · licence: MIT License · rank 10820 · last release 2024-08-10 · [PyPI](https://pypi.org/project/cheap-repr/)

<details><summary>README extract</summary>

This library provides short, fast, configurable string representations, and an easy API for registering your own. It's an improvement of the standard library module `reprlib` (`repr` in Python 2).

Just use the `cheap_repr` function instead of `repr`:

`cheap_repr` knows how to handle many different types out of the box. ...

Example:
```python
>>> from cheap_repr import cheap_repr
>>> cheap_repr(list(range(100)))
'[0, 1, 2, ..., 97, 98, 99]'
```

Sections: cheap_repr, Suppression of long reprs, Registering your own repr function, Exceptions in repr functions, Configuration, Configuration for specific functions, maxparts, pandas, level and max_level, Global configuration, Other miscellaneous functions

</details>

### colorspacious

A powerful, accurate, and easy-to-use Python library for doing colorspace conversions

`pip install colorspacious` · installs (wheel) · licence: MIT License · rank 10822 · last release 2018-04-08 · [PyPI](https://pypi.org/project/colorspacious/)

<details><summary>README extract</summary>

Colorspacious is a powerful, accurate, and easy-to-use library for
performing colorspace conversions.

In addition to the most common standard colorspaces (sRGB, XYZ, xyY,
CIELab, CIELCh), we also include: color vision deficiency ("color
blindness") simulations using the approach of Machado et al (2009); a
complete implementation of CIECAM02; and ...

Example:
```python
from colorspacious import cspace_convert

Jp, ap, bp = cspace_convert([64, 128, 255], "sRGB255", "CAM02-UCS")
```

</details>

### contentful_management

Contentful Management API Client

`pip install contentful_management` · installs (wheel) · licence: MIT · rank 10835 · last release 2026-08-18 · [PyPI](https://pypi.org/project/contentful_management/) · [docs](https://www.contentful.com/developers/docs/references/content-management-api/) · [source](https://github.com/contentful/contentful-management.py)

<details><summary>README extract</summary>

Contentful provides a content infrastructure for digital teams to power content in websites, apps, and devices. Unlike a CMS, Contentful was built to integrate with the modern software stack. ...

Example:
```python
# Optionally, you can pass the metric, start and end date filters
usage = client.organization_periodic_usages('organization_id').all()
# For example only CDA and CMA metrics from yesterday onwards
...
```

Sections: Contentful Management API SDK, Usage, Client, Spaces, Space Memberships, Organizations, Usage API, Organization Periodic Usages, Users, Environments, Assets, Entries, Tags, Content Types

</details>

### catalystwan

Cisco Catalyst WAN SDK for Python

`pip install catalystwan` · installs (wheel) · licence: not stated · rank 10846 · last release 2026-10-28 · [PyPI](https://pypi.org/project/catalystwan/) · [source](https://github.com/cisco-en-programmability/catalystwan-sdk)

<details><summary>README extract</summary>

Cisco Catalyst WAN SDK is a package for creating simple and parallel automatic requests via official SD-WAN Manager API. It is intended to serve as a multiple session handler (provider, provider as a tenant, tenant). The library is not dependent on environment which is being run in, you just need a connection to any SD-WAN Manager.

Example:
```python
devices = session.api.devices.get()
```

Sections: Not recommend to use in production environments., Manager Session, API usage examples, Note, Catching Exceptions

</details>

### cloudshell-pdu-core

QualiSystems PDU core package

`pip install cloudshell-pdu-core` · installs from source (sdist only) · licence: not stated · rank 10883 · last release 2016-10-09 · [PyPI](https://pypi.org/project/cloudshell-pdu-core/)

### cloudshell-pdu-raritan

QualiSystems Raritan PDU package

`pip install cloudshell-pdu-raritan` · installs from source (sdist only) · licence: not stated · rank 10884 · last release 2016-10-06 · [PyPI](https://pypi.org/project/cloudshell-pdu-raritan/)

### cdk-aurora-globaldatabase

cdk-aurora-globaldatabase is an AWS CDK construct library that provides Cross Region Create Global Aurora RDS Databases.

`pip install cdk-aurora-globaldatabase` · installs (wheel) · licence: OSI Approved · rank 10921 · last release 2026-06-16 · [PyPI](https://pypi.org/project/cdk-aurora-globaldatabase/) · [source](https://github.com/neilkuan/cdk-aurora-globaldatabase.git)

<details><summary>README extract</summary>

`cdk-aurora-globaldatabase` is an AWS CDK construct library that allows you to create Amazon Aurora Global Databases with AWS CDK in Typescript or Python.

Features:
Amazon Aurora Global Databases is designed for multi-regional Amazon Aurora Database clusters that span across different AWS regions. ...

Example:
```python
import { GlobalAuroraRDSMaster, InstanceTypeEnum, GlobalAuroraRDSSlaveInfra } from 'cdk-aurora-globaldatabase';
import { App, Stack, CfnOutput } from 'aws-cdk-lib';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
// new app .
const mockApp = new App();

// setting two region env config .
...
```

Sections: cdk-aurora-globaldatabase, Why, Now Try It !!!, Sample for Mysql, Sample for Postgres, To deploy, To destroy

</details>

### csv23

Python 2/3 unicode CSV compatibility layer

`pip install csv23` · installs (wheel) · licence: MIT License · rank 10987 · last release 2022-06-12 · [PyPI](https://pypi.org/project/csv23/) · [docs](https://csv23.readthedocs.io)

<details><summary>README extract</summary>

`csv23` provides the unicode-based API of the Python 3 `csv` module for
Python 2 and 3. Code that should run under both versions of Python can use it
to hide the `bytes` vs. `text` difference between 2 and 3 and stick to the
newer unicode-based interface.

It uses `utf-8` as default encoding everywhere. ...

Example:
```python
>>> import csv23

>>> with csv23.open_csv('spam.csv') as reader:  # doctest: +SKIP
...     for row in reader:
...         print(', '.join(row))
Spam!, Spam!, Spam!'
Spam!, Lovely Spam!, Lovely Spam!'
```

Sections: csv23, Improvements, Links, Extras, Python 3 Extras, See also

</details>

### cpi

Quickly adjust U.S. dollars for inflation using the Consumer Price Index (CPI)

`pip install cpi` · installs (wheel) · licence: MIT · rank 11011 · last release 2026-09-24 · [PyPI](https://pypi.org/project/cpi/) · [docs](https://palewi.re/docs/cpi/) · [source](https://github.com/palewire/cpi)

<details><summary>README extract</summary>

* Docs: palewi.re/docs/cpi/
* Code: github.com/palewire/cpi
* Issues: github.com/palewire/cpi/issues
* Packaging: pypi.python.org/pypi/cpi
* Testing: github.com/palewire/cpi/actions

</details>

### cua-computer

Computer-Use Interface (CUI) framework powering Cua

`pip install cua-computer` · does not install on CPython 3.14 · licence: not stated · rank 11028 · last release 2026-06-18 · [PyPI](https://pypi.org/project/cua-computer/)

<details><summary>README extract</summary>

Computer-Use Interface (CUI) framework for interacting with local macOS and Linux sandboxes.

Documentation - Installation, guides, and configuration.

</details>

### cufile-python

A basic Python wrapper for the NVidia cuFile API

`pip install cufile-python` · installs (wheel) · licence: MIT · rank 11032 · last release 2025-10-13 · [PyPI](https://pypi.org/project/cufile-python/)

<details><summary>README extract</summary>

A basic Python wrapper for the NVidia cuFile API

Example:
```python
from cufile import CuFile
import torch
import ctypes

# allocate an empty buffer in VRAM
t = torch.empty((1024, 1024, 16), dtype=torch.float32, device="cuda")
with CuFile("test.bin", "r") as f:
    f.read(ctypes.c_void_p(t.data_ptr()), t.nbytes)
```

Sections: cufile-python, Usage

</details>

### composio-openai

Use Composio to get an array of tools with your OpenAI Function Call.

`pip install composio-openai` · installs (wheel) · licence: Apache Software License · rank 11059 · last release 2026-11-03 · [PyPI](https://pypi.org/project/composio-openai/)

<details><summary>README extract</summary>

Adapts Composio tools to OpenAI function calling, for both the Responses API and the Chat Completions API.

Example:
```python
import json
from openai import OpenAI
from composio import Composio
from composio_openai import OpenAIResponsesProvider

composio = Composio(provider=OpenAIResponsesProvider())
client = OpenAI()

# Create a session for your user
session = composio.create(user_id="user_123")
tools = session.tools()

response = client.responses.create(
...
```

Sections: composio-openai, Quickstart, Chat Completions, Links

</details>

### csvinsight

Fast & simple summary for large CSV files

`pip install csvinsight` · installs (wheel) · licence: MIT License · rank 11155 · last release 2024-04-09 · [PyPI](https://pypi.org/project/csvinsight/)

<details><summary>README extract</summary>

Fast & simple summary for large CSV files

* Free software: MIT license

Features:
* Calculates basic stats for each column: max, min, mean length; number of non-empty values
* Calculates exact number of unique values and the top 20 most frequent values
* Supports non-orthogonal data (list fields)
* Works with very large files: ...

Sections: csvinsight, Features, Example Usage, 0.4.0 (2024-04-09), 0.3.3 (2020-12-02), 0.3.2 (2019-07-01), 0.3.1 (2019-06-26), 0.3.0 (2018-07-11), 0.2.3 (2017-12-09), 0.2.2 (2017-12-04), 0.2.1 (2017-11-27), 0.2.0 (2017-11-25), 0.1.0 (2017-10-29)

</details>

### colander

A simple schema-based serialization and deserialization library

`pip install colander` · installs (wheel) · licence: Repoze Public License · rank 11178 · last release 2023-01-03 · [PyPI](https://pypi.org/project/colander/) · [docs](https://docs.pylonsproject.org/projects/colander/en/latest/index.html)

<details><summary>README extract</summary>

An extensible package which can be used to:

- deserialize and validate a data structure composed of strings,
 mappings, and lists.

- serialize an arbitrary data structure to a data structure composed
 of strings, mappings, and lists.

It is tested on Python 3.7, 3.8, 3.9, 3.10, and 3.11, and PyPy 3.8.

Please see
for documentation. ...

Features:
- Add new exception `UnsupportedFields`. Used to pass to the caller a list
 of extra fields detected in a cstruct during deserialize.
 See

- Add `drop` functionality to `Sequence` type.
 See

Example:
```python
class What(colander.MappingSchema):
  thing = colander.SchemaNode(colander.String(), default=colander.drop)

result = What().serialize({}) # no "thing" in mapping
assert result == {}
```

...

</details>

### cudo-compute

A client for cudocompute.com

`pip install cudo-compute` · installs (wheel) · licence: MIT License · rank 11228 · last release 2025-01-08 · [PyPI](https://pypi.org/project/cudo-compute/)

<details><summary>README extract</summary>

To use this client install cudoctl and run ``./cudoctl init`` follow the steps to enter your API key and choose your project.

Then when you call cudo_api in python it will grab your API key from the yaml file created by cudoctl.

To use the api key and project set in cudoctl command line tool: ...

Example:
```python
vm_api = cudo_api.virtual_machines()
vms = vm_api.list_vms(cudo_api.project_id())
```

Sections: Cudo Compute, Documentation for API Endpoints, Documentation For Models

</details>

### cmeel-tinyxml

cmeel distribution for TinyXML, an obsolete thing.

`pip install cmeel-tinyxml` · installs (wheel) · licence: not stated · rank 11237 · last release 2023-11-29 · [PyPI](https://pypi.org/project/cmeel-tinyxml/)

### chemprop

Molecular Property Prediction with Message Passing Neural Networks

`pip install chemprop` · installs (wheel) · licence: MIT License · rank 11255 · last release 2026-08-04 · [PyPI](https://pypi.org/project/chemprop/) · [docs](https://chemprop.readthedocs.io/en/latest/) · [source](https://github.com/chemprop/chemprop)

<details><summary>README extract</summary>

Chemprop is a repository containing message passing neural networks for molecular property prediction.

Documentation can be found here.

There are tutorial notebooks in the `examples/` directory.

Chemprop recently underwent a ground-up rewrite and new major release (v2.0.0). A helpful transition guide from Chemprop v1 to v2 can be found here. ...

Sections: Chemprop, Version 1.x, v1 Documentation, v1 Tutorials and Examples, v1 Known Issues

</details>

### comrak

Python bindings for the Comrak Rust library, a fast CommonMark/GFM parser

`pip install comrak` · installs (wheel) · licence: MIT License · rank 11283 · last release 2026-07-27 · [PyPI](https://pypi.org/project/comrak/) · [source](https://github.com/lmmx/comrak.git)

<details><summary>README extract</summary>

Python bindings for the Comrak Rust library, a fast CommonMark/GFM parser.

Currently tracking comrak 0.54.

Example:
```python
>>> import comrak
>>> comrak.render_markdown("# Hello")
'
# Hello
\n'
```

Sections: comrak, Requirements, Usage, CommonMark output, Options, Not exposed, Benchmarks

</details>

### cle

CLE Loads Everything (at least, many binary formats!) and provides a pythonic interface to analyze what they are and what they would look like in memory.

`pip install cle` · installs (wheel) · licence: BSD-2-Clause · rank 11284 · last release 2026-10-22 · [PyPI](https://pypi.org/project/cle/) · [source](https://github.com/angr/cle)

<details><summary>README extract</summary>

CLE loads binaries and their associated libraries, resolves imports and
provides an abstraction of process memory the same way as if it was loader by
the OS's loader.

Project repository:

Documentation:

Example:
```python
>>> import cle
>>> ld = cle.Loader("/bin/ls")
>>> hex(ld.main_object.entry)
'0x4048d0'
>>> ld.shared_objects
{'ld-linux-x86-64.so.2': <ELF Object ld-2.21.so, maps [0x5000000:0x522312f]>,
 'libacl.so.1': <ELF Object libacl.so.1.1.0, maps [0x2000000:0x220829f]>,
 'libattr.so.1': <ELF Object libattr.so.1.1.0, maps [0x4000000:0x4204177]>,
...
```

Sections: CLE, Project Links, Usage example, Valid options, Loading Backends, Finding shared libraries

</details>

### chia-base

Common types and simple utilities used through chia code base

`pip install chia-base` · installs from source (sdist only) · licence: Apache-2.0 · rank 11286 · last release 2024-03-28 · [PyPI](https://pypi.org/project/chia-base/) · [source](https://github.com/richardkiss/chia_base.git)

<details><summary>README extract</summary>

chia_base: base data types for chia coins, spends and contract development

</details>

### cumulusci

Build and release tools for Salesforce developers

`pip install cumulusci` · does not install on CPython 3.14 · licence: BSD License · rank 11289 · last release 2026-10-30 · [PyPI](https://pypi.org/project/cumulusci/)

<details><summary>README extract</summary>

CumulusCI helps build great applications on the Salesforce platform by
automating org setup, testing, and deployment for everyone --- from
developers and admins to testers and product managers.

Best practices, proven at scale. ...

Sections: CumulusCI, Learn more, Questions?, v4.11.0 (2026-10-30), What's Changed, Critical Changes, Changes

</details>

### chialisp-puzzles

Some canonical puzzles deployed on chia-blockchain

`pip install chialisp-puzzles` · installs from source (sdist only) · licence: not stated · rank 11312 · last release 2023-11-10 · [PyPI](https://pypi.org/project/chialisp-puzzles/)

<details><summary>README extract</summary>

This project contains several standard and legacy puzzles commonly used on the chia network.

Note that it uses `enscons` to build, as the more commonly used `setuptools` does not easily allow fine-grained control of the contents of the `sdist` and `wheel` files. ...

Example:
```python
from chialisp_puzzles import load_puzzle

program = load_puzzle("p2_delegated_puzzle_or_hidden_puzzle")
```

Sections: chialisp_puzzles, Use

</details>

### certifi-linux

Certifi patch for using Linux cert trust stores

`pip install certifi-linux` · installs (wheel) · licence: MIT License · rank 11316 · last release 2025-05-27 · [PyPI](https://pypi.org/project/certifi-linux/) · [docs](https://github.com/m-birke/certifi-linux#readme) · [source](https://github.com/m-birke/certifi-linux)

<details><summary>README extract</summary>

Table of Contents

- About
- Installation
- Usage
- Compatibility
- Implementation
- Related Projects
- Credits
- License

WHAT: `certifi-linux` wraps certifi, but instead of distributing a certificate like `certifi` does, it uses the Linux system trust store.

WHY? The requests module depends on `certifi` and uses it for TLS. ...

Sections: certifi-linux, About, Usage, Compatibility, Implementation, Cert Path Candidates, Related Projects

</details>

### chialisp-loader

Provides `load_puzzle` which dynamic rebuilds if `chialisp_builder` is available.

`pip install chialisp-loader` · installs from source (sdist only) · licence: not stated · rank 11319 · last release 2023-11-10 · [PyPI](https://pypi.org/project/chialisp-loader/)

<details><summary>README extract</summary>

This tiny wheel exports `load_program`, which is used to load chialisp programs from resources included with python wheels.

Chialisp `.clsp` files are compiled into `.hex` output. Only `.hex` output files need to be included in binary wheels

When `load_program` is called, it tries to import `chialisp_builder`. ...

</details>

### chialisp-builder

Allow on-demand builds of chialisp with recursive dependency checking.

`pip install chialisp-builder` · installs from source (sdist only) · licence: not stated · rank 11325 · last release 2024-01-04 · [PyPI](https://pypi.org/project/chialisp-builder/)

<details><summary>README extract</summary>

Use this wheel in conjunction with `runtime_builder` to manage building of chialisp at build time or during development.

Add `chialisp_builder` as a buildtime dependency and a development-time dependency. Don't add it as a runtime dependency, as the clvm `.hex` files should be built and included with the wheel. The source does not need to be. ...

Sections: Chialisp Builder, Use, FAQ

</details>

### chialisp-stdlib

Chialisp `.clib` standard library files

`pip install chialisp-stdlib` · installs from source (sdist only) · licence: not stated · rank 11336 · last release 2023-11-10 · [PyPI](https://pypi.org/project/chialisp-stdlib/)

<details><summary>README extract</summary>

Use:

`pip install chialisp_stdlib`

To get the path to the include files, use

Note that `*_INCLUDE_DIRECTORY` is a `pathlib.Path` and not a `str`, so if your API expects `str`-based paths, use `str(path)` to convert.

And upgrade your API: see PEP519. C'mon, it's 2023 (as of this writing).

Example:
```python
from chialisp_stdlib import NIGHTLY_INCLUDE_DIRECTORY
from chialisp_stdlib import STABLE_INCLUDE_DIRECTORY
```

</details>

### chia-puzzles-py

A collection of the currently deployed ChiaLisp puzzles.

`pip install chia-puzzles-py` · installs (wheel) · licence: not stated · rank 11374 · last release 2025-10-14 · [PyPI](https://pypi.org/project/chia-puzzles-py/)

<details><summary>README extract</summary>

This is a collection of the standard Chia puzzles.
These are the puzzles which are deployed on chain and therefore cannot change.

This repository tracks the source code, the compiled hex, and a hash of the compiled hex to ensure continuity.

All puzzles are kept in the `puzzles` folder as both a `.clsp` and `.clsp.hex` file. ...

Sections: Chia Puzzles, Adding Bindings for a New Puzzle

</details>

### cfenv

Python wrapper for Cloud Foundry environments

`pip install cfenv` · installs (wheel) · licence: MIT License · rank 11453 · last release 2017-06-09 · [PyPI](https://pypi.org/project/cfenv/)

<details><summary>README extract</summary>

py-cfenv is a tiny utility that simplifies interactions with Cloud Foundry environment variables, modeled after node-cfenv.

Example:
```python
from cfenv import AppEnv

env = AppEnv()
env.name  # 'test-app'
env.port  # 5000

redis = env.get_service(label='redis')
redis.credentials  # {'uri': '...', 'password': '...'}
redis.get_url(host='hostname', password='password', port='port')  # redis://pass:host
```

Sections: py-cfenv, Quickstart

</details>

### cua-core

Core functionality for Cua including telemetry and shared utilities

`pip install cua-core` · does not install on CPython 3.14 · licence: MIT · rank 11473 · last release 2026-10-01 · [PyPI](https://pypi.org/project/cua-core/)

<details><summary>README extract</summary>

Cua Core provides essential shared functionality and utilities used across the Cua ecosystem:

- Privacy-focused telemetry system for transparent usage analytics
- Common helper functions and utilities used by other Cua packages
- Core infrastructure components shared between modules

</details>

### cuallee

Python library for data validation on DataFrame APIs including Snowflake/Snowpark, Apache/PySpark and Pandas/DataFrame.

`pip install cuallee` · installs (wheel) · licence: not stated · rank 11518 · last release 2025-10-07 · [PyPI](https://pypi.org/project/cuallee/)

<details><summary>README extract</summary>

Meaning `good` in Aztec (Nahuatl), _pronounced: QUAL-E

This library provides an intuitive `API` to describe data quality `checks` initially just for `PySpark` dataframes `v3.3.0`. And extended to `pandas`, `snowpark`, `duckdb`, `daft` and more.
It is a replacement written in pure `python` of the `pydeequ` framework. ...

Example:
```python
from cuallee import Check, CheckLevel # WARN:0, ERR: 1

# Nulls on column Id
check = Check(CheckLevel.WARNING, "Completeness")
(
    check
    .is_complete("id")
    .is_unique("id")
    .validate(df)
).show() # Returns a pyspark.sql.DataFrame
```

...

</details>

### cdktf-cdktf-provider-aws

Prebuilt aws Provider for Terraform CDK (cdktf)

`pip install cdktf-cdktf-provider-aws` · installs (wheel) · licence: OSI Approved · rank 11531 · last release 2025-12-10 · [PyPI](https://pypi.org/project/cdktf-cdktf-provider-aws/) · [source](https://github.com/cdktf/cdktf-provider-aws.git)

<details><summary>README extract</summary>

HashiCorp made the decision to stop publishing new versions of prebuilt Terraform aws provider bindings for CDK for Terraform on December 10, 2025. As such, this repository has been archived and is no longer supported in any way by HashiCorp. ...

Sections: Deprecated Packages, NPM, PyPI, Nuget, Maven, Go, Docs

</details>

### cutlet

Romaji converter

`pip install cutlet` · installs (wheel) · licence: MIT License · rank 11598 · last release 2026-07-01 · [PyPI](https://pypi.org/project/cutlet/)

<details><summary>README extract</summary>

Cutlet is a tool to convert Japanese to romaji. Check out the interactive demo! Also see the docs and the original blog post.

issueを英語で書く必要はありません。

Features:

- support for Modified Hepburn, Kunreisiki, Nihonsiki systems
- custom overrides for individual mappings
- custom overrides for specific words ...

Example:
```python
import cutlet
katsu = cutlet.Cutlet()
katsu.romaji("カツカレーは美味しい")
# => 'Cutlet curry wa oishii'

# you can print a slug suitable for urls
katsu.slug("カツカレーは美味しい")
# => 'cutlet-curry-wa-oishii'

# You can disable using foreign spelling too
katsu.use_foreign_spelling = False
katsu.romaji("カツカレーは美味しい")
# => 'Katsu karee wa oishii'

...
```

Sections: cutlet, Usage, Alternatives

</details>

### cozy-runtime

Cozy author surface and device executor

`pip install cozy-runtime` · installs (wheel) · licence: not stated · rank 11611 · last release 2026-11-06 · [PyPI](https://pypi.org/project/cozy-runtime/)

### cvat-sdk

Software Development Kit for CVAT

`pip install cvat-sdk` · installs (wheel) · licence: MIT · rank 11620 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cvat-sdk/)

<details><summary>README extract</summary>

This package provides a Python client library for CVAT server. It can be useful for
workflow automation and writing custom CVAT server clients.

The SDK API includes several layers:

- Server API wrappers (`ApiClient`). Located in at `cvat_sdk.api_client`.
- High-level tools (`Core`). Located at `cvat_sdk.core`.
- PyTorch adapter. ...

</details>

### composio-openai-agents

Use Composio to get array of strongly typed tools for OpenAI Agents

`pip install composio-openai-agents` · installs (wheel) · licence: Apache Software License · rank 11622 · last release 2026-11-03 · [PyPI](https://pypi.org/project/composio-openai-agents/)

<details><summary>README extract</summary>

Adapts Composio tools to the OpenAI Agents framework's native tool format, so your agents can take action across 1000+ apps.

Example:
```python
from composio import Composio
from composio_openai_agents import OpenAIAgentsProvider
from agents import Agent, Runner

composio = Composio(provider=OpenAIAgentsProvider())

# Each session is scoped to one of your users
session = composio.create(user_id="user_123")
tools = session.tools()

agent = Agent(
    name="Personal Assistant",
...
```

Sections: composio-openai-agents, Quickstart, Links

</details>

### cube_dbt

dbt integration for Cube

`pip install cube_dbt` · installs (wheel) · licence: MIT · rank 11628 · last release 2025-10-22 · [PyPI](https://pypi.org/project/cube_dbt/)

<details><summary>README extract</summary>

`cube_dbt` is the dbt integration for Cube that helps define the data model of the semantic layer on top of dbt models.

Example:
```python
manifest_url = '
dbt = (
  Dbt
  .from_url(manifest_url)
  .filter(
    paths=['marts/'],
    tags=['cube'],
    names=['my_table', 'my_table_2']
  )
)
print(dbt.models)

# For use in Jinja templates:
print(dbt.model('name').as_cube())
print(dbt.model('name').as_dimensions(skip=['id']))
print(dbt.model('name').column('name').as_dimension())
```

Sections: cube_dbt, Usage, Preprocessing the `manifest.json` file

</details>

### colbert-ai

Efficient and Effective Passage Search via Contextualized Late Interaction over BERT

`pip install colbert-ai` · installs (wheel) · licence: not stated · rank 11663 · last release 2025-08-11 · [PyPI](https://pypi.org/project/colbert-ai/)

<details><summary>README extract</summary>

[](

 Figure 1: ColBERT's late interaction, efficiently scoring the fine-grained similarity between a queries and a passage.

As Figure 1 illustrates, ColBERT relies on fine-grained contextual late interaction: it encodes each passage into a matrix of token-level embeddings (shown above in blue). ...

Features:
Using ColBERT on a dataset typically involves the following steps.

Step 0: Preprocess your collection. At its simplest, ColBERT works with tab-separated (TSV) files: a file (e.g., `collection.tsv`) will contain all passages and another (e.g., ...

Example:
```python
from colbert.infra import Run, RunConfig, ColBERTConfig
from colbert import Indexer

if name=='main':
    with Run().context(RunConfig(nranks=1, experiment="msmarco")):

        config = ColBERTConfig(
...

</details>

### cdk-events-notify

The Events Notify AWS Construct lib for AWS CDK

`pip install cdk-events-notify` · installs (wheel) · licence: OSI Approved · rank 11679 · last release 2026-06-16 · [PyPI](https://pypi.org/project/cdk-events-notify/) · [source](https://github.com/neilkuan/cdk-events-notify.git)

<details><summary>README extract</summary>

`cdk-events-notify` is an AWS CDK Construct Library that provides you know who login in your aws console.

Features:
It's just a small feature at the moment,
Provides you to trigger Lambda Function push notifications to Slack when you discover Console Login event or switch role event through Cloudtrail.

> Welcome to contribute another event notify case you want.

Example:
```python
import * as cdk from 'aws-cdk-lib';
import { EventNotify } from 'cdk-events-notify';

const app = new cdk.App();
const stack = new cdk.Stack(app, 'integ-stack', { env });
new EventNotify(stack, 'SlackEventNotify', {
  slack: {
    slackChannelName: 'your-channel-name',
    slackWebhookUrl: '
  },
});
```

...

</details>

### conda-inject

Helper functions for injecting a conda environment into the current python environment (by modifying sys.path, without actually changing the current python environment).

`pip install conda-inject` · installs (wheel) · licence: not stated · rank 11711 · last release 2024-05-27 · [PyPI](https://pypi.org/project/conda-inject/)

<details><summary>README extract</summary>

Helper functions for injecting a conda environment into the current python environment.
This happens by modifying sys.path, without actually changing the current python environment.

</details>

### cronex

This module provides an easy to use interface for cron-like task scheduling.

`pip install cronex` · installs from source (sdist only) · licence: MIT License · rank 11713 · last release 2018-11-04 · [PyPI](https://pypi.org/project/cronex/)

<details><summary>README extract</summary>

This module provides an easy to use interface for cron-like task
scheduling. The cron expression evaluation implemented by this library
is 100% Vixie Cron compatible and also supports Java
Quartz's
non-standard "L", "W" and "#" characters. ...

Example:
```python
>>> job = CronExpression("0 0 * * 1-5/2 find /var/log -delete")
>>> job.check_trigger((2010, 11, 17, 0, 0))
True
>>> job.check_trigger((2012, 12, 21, 0 , 0))
False
```

Sections: CronExpression, Examples, Standard Cron Fields, Periodic Trigger, Simple cron scheduler in less than ten lines, Expression Syntax, Ranges and Wild-cards, Steps, Repeaters, Special Symbols, Miscellaneous

</details>

### colorlover

Color scales for IPython notebook

`pip install colorlover` · installs (wheel) · licence: not stated · rank 11860 · last release 2019-01-19 · [PyPI](https://pypi.org/project/colorlover/)

### codeflash-benchmark

Pytest benchmarking plugin for codeflash.ai - automatic code performance optimization

`pip install codeflash-benchmark` · installs (wheel) · licence: not stated · rank 11864 · last release 2026-02-19 · [PyPI](https://pypi.org/project/codeflash-benchmark/) · [source](https://github.com/codeflash-ai/codeflash-benchmark)

<details><summary>README extract</summary>

A pytest benchmarking plugin for CodeFlash - automatic code performance optimization.

Sections: CodeFlash Benchmark, Usage

</details>

### checkout-sdk

Checkout.com Python SDK

`pip install checkout-sdk` · installs (wheel) · licence: MIT License · rank 11924 · last release 2026-11-06 · [PyPI](https://pypi.org/project/checkout-sdk/)

<details><summary>README extract</summary>

Example:
```python
from checkout_sdk.checkout_sdk import CheckoutSdk
from checkout_sdk.environment import Environment

def default():
    # public key is optional, only required for operations related with tokens
    checkout_api = CheckoutSdk
        .builder()
        .secret_key('secret_key')
...
```

Sections: Checkout.com Python SDK, Getting started, Requirements, book: Checkout our official documentation., How to use the SDK, Subdomain value, Default, Default OAuth, Previous, Logging, HttpClient, Exception handling, Building from source, Prerequisites

</details>

### cycode

Boost security in your dev lifecycle via SAST, SCA, Secrets & IaC scanning.

`pip install cycode` · installs (wheel) · licence: MIT · rank 11945 · last release 2026-11-01 · [PyPI](https://pypi.org/project/cycode/) · [source](https://github.com/cycodehq/cycode-cli)

<details><summary>README extract</summary>

The Cycode Command Line Interface (CLI) is an application you can install locally to scan your repositories for secrets, infrastructure as code misconfigurations, software composition analysis vulnerabilities, and static application security testing issues.

This guide walks you through both installation and usage.

Sections: Cycode CLI User Guide, Prerequisites, Using the Auth Command, Using the Configure Command, Add to Environment Variables, On Unix/Linux, On Windows, Cycode CLI Commands, Certificates and Proxies, MCP Command \[EXPERIMENT\], Starting the MCP Server, Available Options, MCP Tools, Usage Examples

</details>

### componentize-py

Tool to package Python applications as WebAssembly components

`pip install componentize-py` · installs (wheel) · licence: not stated · rank 12055 · last release 2026-09-12 · [PyPI](https://pypi.org/project/componentize-py/) · [source](https://github.com/bytecodealliance/componentize-py)

<details><summary>README extract</summary>

A Bytecode Alliance project

This is a tool to convert a Python application to a WebAssembly
component. It takes the
following as input:

- a WIT file or directory
- the name of a WIT world defined in the above file or directory
- the name of a Python module which targets said world ...

Example:
```python
import x

class Hello(hello.Hello):
    def hello(self) -> str:
        return x.y.foo()
```

Sections: componentize-py, Getting Started, Known Limitations, 23.

</details>

### case-convert

Cross library to convert case with permissive input

`pip install case-convert` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 12057 · last release 2020-09-10 · [PyPI](https://pypi.org/project/case-convert/)

_README extract left out: share-alike licence._

### clickhouse-toolset

(no summary)

`pip install clickhouse-toolset` · does not install on CPython 3.14 · licence: not stated · rank 12172 · last release 2025-04-28 · [PyPI](https://pypi.org/project/clickhouse-toolset/)

### cronitor

A lightweight Python client for Cronitor.

`pip install cronitor` · installs (wheel) · licence: MIT License · rank 12200 · last release 2025-10-08 · [PyPI](https://pypi.org/project/cronitor/)

<details><summary>README extract</summary>

Cronitor provides end-to-end monitoring for background jobs, websites, APIs, and anything else that can send or receive an HTTP request. This library provides convenient access to the Cronitor API from applications written in Python. See our API docs for detailed references on configuring monitors and sending telemetry pings.

In this guide: ...

Example:
```python
import cronitor.celery
from celery import Celery

app = Celery()
app.conf.beat_schedule = {
    'run-me-every-minute': {
        'task': 'tasks.every_minute_celery_task',
        'schedule': 60
    }
}

# Discover all of your celery tasks and automatically add monitoring.
cronitor.celery.initialize(app, api_key="apiKey123")

@app.task
...
```

...

</details>

### cardscan-client

Python CardScan API client

`pip install cardscan-client` · installs (wheel) · licence: Other/Proprietary License · rank 12229 · last release 2025-10-11 · [PyPI](https://pypi.org/project/cardscan-client/) · [source](https://github.com/CardScan-ai/api-clients.git)

<details><summary>README extract</summary>

The official python client for the CardScan API

Python 3.8+

Example:
```python
from cardscan_client.api_client import ApiClient
from cardscan_client.api.card_scan_api import CardScanApi
from cardscan_client.configuration import Configuration
from cardscan_client.exceptions import ApiException
from pprint import pprint

# Defining the host is optional and defaults to
...
```

Sections: cardscan-client, Requirements., Getting Started, Documentation for API Endpoints, Documentation For Models, bearerAuth

</details>

### cyclic

Handle cyclic relations

`pip install cyclic` · installs (wheel) · licence: BSD License · rank 12239 · last release 2018-09-26 · [PyPI](https://pypi.org/project/cyclic/)

<details><summary>README extract</summary>

Handle cyclic relation compared by value.

Example:
```python
from cyclic import Cyclic

cy = Cyclic()

# Let's say A is a prent of B
cy.add(B, A)

# B is a parent of C
cy.add(C, B)

# C is a parent of A (cyclic)
cy.add(A, C)

# let's see if C is in any kind of cyclic relation

print(cy.is_cyclic(C)) # True
```

</details>

### coqpit-config

Simple (maybe too simple), light-weight config management through python data-classes.

`pip install coqpit-config` · installs (wheel) · licence: MIT · rank 12259 · last release 2026-04-10 · [PyPI](https://pypi.org/project/coqpit-config/) · [source](https://github.com/idiap/coqui-ai-coqpit)

<details><summary>README extract</summary>

Simple, light-weight and no dependency config handling through python data
classes with to/from JSON serialization/deserialization.

Fork of the original, unmaintained repository. New PyPI package: coqpit-config

Currently it is being used by coqui-tts.

What I need from a ML configuration library...

1. ...

Example:
```python
import os
from dataclasses import asdict, dataclass, field
from typing import List, Union
from coqpit import MISSING, Coqpit, check_argument

@dataclass
class SimpleConfig(Coqpit):
    val_a: int = 10
    val_b: int = None
    val_d: float = 10.21
    val_c: str = "Coqpit is great!"
    # mandatory field
...
```

Sections: 👩‍✈️ Coqpit, ❔ Why I need this, 🚫 Limitations, 🔍 Examples, 👉 Simple Coqpit, 👉 Serialization, 👉 ```argparse``` handling and parsing.

</details>

### csvsort

Sort large CSV files on disk rather than in memory

`pip install csvsort` · installs from source (sdist only) · licence: lgpl · rank 12380 · last release 2020-06-17 · [PyPI](https://pypi.org/project/csvsort/)

_README extract left out: share-alike licence._

### certora-cli

Runner for the Certora Prover

`pip install certora-cli` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 12419 · last release 2026-10-26 · [PyPI](https://pypi.org/project/certora-cli/) · [docs](https://docs.certora.com/en/latest/) · [source](https://github.com/Certora/CertoraProver)

_README extract left out: share-alike licence._

### composio-anthropic

Use Composio to get an array of tools with your Anthropic LLMs.

`pip install composio-anthropic` · installs (wheel) · licence: Apache Software License · rank 12454 · last release 2026-11-03 · [PyPI](https://pypi.org/project/composio-anthropic/)

<details><summary>README extract</summary>

Adapts Composio tools to the Claude Messages API tool format and executes the tool calls Claude returns.

Example:
```python
import json
import anthropic
from composio import Composio
from composio_anthropic import AnthropicProvider

composio = Composio(provider=AnthropicProvider())
client = anthropic.Anthropic()

# Create a session for your user
session = composio.create(user_id="user_123")
tools = session.tools()

messages = [
...
```

Sections: composio-anthropic, Quickstart, Links

</details>

### channel-advisor-api-python

(no summary)

`pip install channel-advisor-api-python` · installs (wheel) · licence: not stated · rank 12488 · last release 2025-03-25 · [PyPI](https://pypi.org/project/channel-advisor-api-python/)

### cuequivariance-ops-torch-cu12

cuequivariance-ops-torch - GPU Accelerated Torch Extensions for Equivariant Primitives

`pip install cuequivariance-ops-torch-cu12` · installs (wheel) · licence: not stated · rank 12523 · last release 2026-10-15 · [PyPI](https://pypi.org/project/cuequivariance-ops-torch-cu12/) · [docs](https://docs.nvidia.com/cuda/cuequivariance/)

<details><summary>README extract</summary>

`cuequivariance_ops_torch` provides CUDA kernels for the
cuEquivariance project's PyTorch
components. As such, it contains pytorch bindings to optimized kernels that
cuEquivariance's operations map down to. In general, we advice that you access
those kernels through cuEquivariance, but you may also find them useful on
their own.

Example:
```python
import cuequivariance_ops_torch
```

Sections: cuequivariance-ops-torch, Introduction, Kernel Factory TriMul kernels, KF under `torch.compile`, Documentation, Pairformer inference primitives, Calling convention for declined cells, Usage

</details>

### cg

Clinical Genomics command center

`pip install cg` · does not install on CPython 3.14 · licence: not stated · rank 12533 · last release 2026-11-04 · [PyPI](https://pypi.org/project/cg/)

<details><summary>README extract</summary>

[][closed-issues-url]
[][ismaintained-resolve-url]
[][ismaintained-open-rate-url]
[][codefactor-url]
[][black-url]

`cg` stands for _Clinical Genomics; a clinical sequencing platform under SciLifeLab

In this context, `cg` provides the interface between these tools to facilitate automation and other necessary cross-talk. ...

</details>

### cbitstruct

Faster C implementation of bitstruct

`pip install cbitstruct` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 12585 · last release 2026-02-09 · [PyPI](https://pypi.org/project/cbitstruct/)

<details><summary>README extract</summary>

`cbitstruct` is a C implementation of the `bitstruct` library. Credits to Erik Moqvist for the original `bitstruct` library available on Github and pip.

The goal is to provide the same API an idealy to be able to interchange `import bitstruct` and `import cbitstruct as bitstruct`. ...

Sections: About, Documentation, Limitations, Performance, Comparing to `bitstruct`, The dict API

</details>

### cadgen

Deprecated alias of the text-to-cad library, still published: installs cad at the same release. Import cad.

`pip install cadgen` · installs (wheel) · licence: MIT · rank 12683 · last release 2026-11-08 · [PyPI](https://pypi.org/project/cadgen/)

<details><summary>README extract</summary>

Deprecated: install and import `cad`. `cadgen` is the deprecated alias of the text-to-cad
library, still published at every release for backwards compatibility. This distribution holds
nothing of its own: it installs `cad`, the library, at the same release. ...

</details>

### comma-deps-json11

json11 JSON parser library (static build)

`pip install comma-deps-json11` · installs (wheel) · licence: not stated · rank 12707 · last release 2026-11-08 · [PyPI](https://pypi.org/project/comma-deps-json11/)

### cronexpr

Python bindings for cronexpr using supertinycron

`pip install cronexpr` · installs from source (sdist only) · licence: Apache-2.0 · rank 12745 · last release 2024-09-11 · [PyPI](https://pypi.org/project/cronexpr/)

<details><summary>README extract</summary>

`cronexpr` is a Python library for parsing and evaluating cron expressions. It is a simple wrapper of the parser that powers supertinycron. This implementation was born out of a lack of cron libraries available for python that support all cron expression special characters including * / , - ? L W, # as well as 5, 6 (w/ seconds or year), or 7 (w/ ...

Example:
```python
import cronexpr

# At 21:00, on the first Tuesday of the month, every 2 months
cron = "0 0 21 ? 1/2 TUE#1 *"
# Output:
# Previous: 2024-09-03 21:00:00+00:00
# Next: 2024-11-05 21:00:00+00:00
print("Previous:", cronexpr.prev_fire(cron))
print("Next:", cronexpr.next_fire(cron))

# Output:
...
```

...

</details>

### chatlas

A simple and consistent interface for chatting with LLMs

`pip install chatlas` · installs (wheel) · licence: MIT · rank 12863 · last release 2026-09-04 · [PyPI](https://pypi.org/project/chatlas/) · [docs](https://posit-dev.github.io/chatlas) · [source](https://github.com/posit-dev/chatlas)

<details><summary>README extract</summary>

Your friendly guide to building LLM chat apps in Python with less effort and more clarity.

Example:
```python
from chatlas import ChatOpenAI

# Optional (but recommended) model and system_prompt
chat = ChatOpenAI(
    model="gpt-4.1-mini",
    system_prompt="You are a helpful assistant.",
)

# Optional tool registration
def get_current_weather(lat: float, lng: float):
    "Get the current weather for a given location."
    return "sunny"

...
```

Sections: chatlas, Quick start

</details>

### confocal

Multi-layer configuration management with source tracking

`pip install confocal` · installs (wheel) · licence: MIT · rank 12881 · last release 2026-10-22 · [PyPI](https://pypi.org/project/confocal/) · [source](https://github.com/joshuafcole/confocal)

<details><summary>README extract</summary>

A multi-layer configuration management library built on pydantic with source tracking and profile support.

Features:
- Hierarchical config file discovery (searches parent directories)
- Profile support for different environments
- Full source tracking to explain where each config value came from
- Built on pydantic for robust validation and type safety ...

Example:
```python
from confocal import BaseConfig
from pydantic import Field

class MyConfig(BaseConfig):
    database_url: str
    name: str = Field(default="Anonymous")
    debug: bool = False

# Load config from raiconfig.toml, environment variables, etc.
config = MyConfig.load()

# Show where config values came from
config.explain()
```

...

</details>

### ciscoisesdk

Cisco Identity Services Engine Platform SDK

`pip install ciscoisesdk` · installs (wheel) · licence: MIT License · rank 12905 · last release 2026-10-14 · [PyPI](https://pypi.org/project/ciscoisesdk/) · [source](https://github.com/CiscoISE/ciscoisesdk)

<details><summary>README extract</summary>

ciscoisesdk is a *community developed* Python library for working with the Identity Services Engine APIs.
Our goal is to make working with Cisco Identity Services Engine in Python a *native* and *natural* experience!

The quickest way to check that your credentials and API settings work is to ask ISE for
its version and patch level: ...

Example:
```python
from ciscoisesdk import IdentityServicesEngineAPI

api = IdentityServicesEngineAPI(username='admin',
                                password='C1sco12345',
                                uses_api_gateway=True,
                                base_url='
                                verify=True,
...
```

Sections: ciscoisesdk, Compatibility matrix, Documentation, Inspiration

</details>

### cqlsh

cqlsh is a Python-based command-line client for running CQL commands on a cassandra cluster.

`pip install cqlsh` · installs (wheel) · licence: Apache Software License · rank 12909 · last release 2026-04-16 · [PyPI](https://pypi.org/project/cqlsh/) · [docs](https://cassandra.apache.org/doc/latest/tools/cqlsh.html)

<details><summary>README extract</summary>

`cqlsh` is a Python-based command-line client for running `CQL` commands on a `cassandra` cluster.

Normally it's packaged as part of the full Apache Cassandra™ installation. This repo repackages it into a standalone Python package for lighter-weight installs.

Sections: `cqlsh`, Running, Documentation, 6.2.2 (April 16, 2026), 6.2.1 (August 6, 2025), 6.2.0 (September 16, 2024), 6.1.3 (Feburary 23, 2023), 6.1.2 (March 24, 2023), 6.1.1 (skipped due to a versioning issue), 6.1.0 (Jan 4, 2023), 6.0.1 (Jan 18, 2022), 6.0.0 (Aug 3, 2021), 6.0.0b4 (Mar 9, 2021), 5.0.5 (Mar 9, 2021)

</details>

### copybook

python copybook parser

`pip install copybook` · installs (wheel) · licence: MIT License · rank 12916 · last release 2022-09-15 · [PyPI](https://pypi.org/project/copybook/)

<details><summary>README extract</summary>

Copybook is a python module for parsing VSAM copybooks.

Features:
- integers
 - floats described with dot notation
 - floats described with V notation
 - leading SIGNED
 - trailing SIGNED
- Character PIC notations
- Groups
- OCCURS clauses
- REDEFINES clauses ...

Example:
```python
import copybook
text = """
       01  WORK-BOOK.
        10  TAX-RATE        PIC S9(13)V9(2)
                    SIGN LEADING SEPARATE.
"""
root = copybook.parse_string(text)
```

Sections: Copybook, Features, Usage, Using Copybook module to parse a fixed width line, Gratitude

</details>

### cryptojwt

Python implementation of JWT, JWE, JWS and JWK

`pip install cryptojwt` · installs (wheel) · licence: Apache-2.0 · rank 12937 · last release 2026-03-24 · [PyPI](https://pypi.org/project/cryptojwt/)

<details><summary>README extract</summary>

An implementation of the JSON cryptographic specs JWS, JWE, JWK, and JWA [RFC 7515-7518] and JSON Web Token (JWT) [RFC 7519]

Please read the Official Documentation for getting usage examples and further informations.

</details>

### cua-train

Cua Cloud Python client — control and data plane for Cua Cloud desktop VM pools

`pip install cua-train` · installs (wheel) · licence: MIT · rank 12987 · last release 2026-06-24 · [PyPI](https://pypi.org/project/cua-train/) · [source](https://github.com/trycua/cua)

<details><summary>README extract</summary>

Python client for the Cua Cloud API.

Example:
```python
from cua_train import TrainClient

client = TrainClient.from_key(
    client_id="ukey-...",      # from your Cua Cloud account
    client_secret="...",
)

# Control plane — claim a VM
http = client.get_async_httpx_client()
await http.post("/api/k8s/apis/osgym.cua.ai/v1alpha1/namespaces/my-pool/osgymsandboxclaims", json={...})

...
```

</details>

### craftax

An open-world environment for training RL agents

`pip install craftax` · installs (wheel) · licence: MIT License · rank 13000 · last release 2026-10-27 · [PyPI](https://pypi.org/project/craftax/)

<details><summary>README extract</summary>

Craftax is an RL environment written entirely in JAX. Craftax reimplements and significantly extends the game mechanics of Crafter, taking inspiration from roguelike games such as NetHack.
Craftax conforms to the gymnax interface, allowing easy integration with existing JAX-based frameworks like PureJaxRL and JaxUED.

Example:
```python
rng = jax.random.PRNGKey(0)
rng, _rng = jax.random.split(rng)
_rngs = jax.random.split(_rng, 3)

# Create environment
env = make_craftax_env_from_name("Craftax-Symbolic-v1", auto_reset=True)
env_params = env.default_params

# Get an initial state and observation
obs, state = env.reset(_rngs[0], env_params)

# Pick random action
...
```

...

</details>

### commonregex

Find all dates, times, emails, phone numbers, links, emails, ip addresses, prices, bitcoin address, and street addresses in a string.

`pip install commonregex` · does not install on CPython 3.14 · licence: MIT · rank 13005 · last release ? · [PyPI](https://pypi.org/project/commonregex/)

<details><summary>README extract</summary>

Find all times, dates, links, phone numbers, emails, ip addresses, and prices in a string.

Sections: CommonRegex, Usage, CommonRegex Ports

</details>

### comfy-cli

A CLI tool for installing and using ComfyUI.

`pip install comfy-cli` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 13017 · last release 2026-11-03 · [PyPI](https://pypi.org/project/comfy-cli/) · [source](https://github.com/Comfy-Org/comfy-cli.git)

_README extract left out: share-alike licence._

### cwltest

Common Workflow Language testing framework

`pip install cwltest` · installs (wheel) · licence: Apache Software License · rank 13059 · last release 2026-11-06 · [PyPI](https://pypi.org/project/cwltest/)

<details><summary>README extract</summary>

Example:
```python
setup(
  ...
  entry_points={"cwltest.fsaccess": ["fsaccess=my_cwl_runner.fsaccess:get_fsaccess"]}},
  ...
)
```

Sections: Run on the command line, Custom file access module

</details>

### cached_method

The equivalent of cached_property for methods

`pip install cached_method` · installs (wheel) · licence: MIT License · rank 13070 · last release 2021-10-31 · [PyPI](https://pypi.org/project/cached_method/)

<details><summary>README extract</summary>

The `@cached_method` decorator is the equivalent of
`functools.cached_property`
for methods. This means that each instance has its own cache, so that the caches get
garbage collected as soon as the owning objects are. The main advantages of
`cached_method` over applying `functools.lru_cache` directly to methods are
1. ...

Example:
```python
from cached_method import cached_method

class GPUVector:
    def init(self, data):
        # data is some smart tensor object as found in pytorch, tensorflow, etc.
        self.data = data

    # Only cache the 2 most-recently used norms
    @cached_method(maxsize=2)
    def norm(self, p=2):
        return (self.data  p).sum()  (1 / p)

...
```

</details>

### celery-prometheus

Celery with your own prometheus metrics

`pip install celery-prometheus` · installs (wheel) · licence: Other/Proprietary License · rank 13088 · last release 2023-12-20 · [PyPI](https://pypi.org/project/celery-prometheus/)

<details><summary>README extract</summary>

This module expose the Prometheus HTTP server to expose metrics of your Celery backends.

To install `celery-prometheus` with pip, use the command:

With Poetry:

Example:
```python
from celery import Celery
from celery_prometheus import add_prometheus_option

app = Celery()
add_prometheus_option(app)

# Rest of your code ...
```

Sections: Celery Prometheus, Usage

</details>

### cdk-common

Common AWS CDK librarys.

`pip install cdk-common` · installs (wheel) · licence: OSI Approved · rank 13101 · last release 2026-07-09 · [PyPI](https://pypi.org/project/cdk-common/) · [source](https://github.com/neilkuan/cdk-common.git)

<details><summary>README extract</summary>

This Constructs Library will collection of useful `function` and `class` for AWS CDK.

Example:
```python
import * as cdk from 'aws-cdk-lib';
import { AWSManagedPolicies } from 'cdk-common';
import { Construct } from 'constructs';
const app = new cdk.App();

const stack = new cdk.Stack(app, 'integ-default', { env });

export class IntegDefault extends Construct {
  constructor(scope: Construct, id: string ) {
    super(scope, id);

...
```

Sections: Welcome to `cdk-common`, AWS Managed Policies `enum`

</details>

### castellan

Generic Key Manager interface for OpenStack

`pip install castellan` · installs (wheel) · licence: Apache Software License · rank 13145 · last release 2026-07-10 · [PyPI](https://pypi.org/project/castellan/) · [source](https://opendev.org/openstack/castellan/)

<details><summary>README extract</summary>

Generic Key Manager interface for OpenStack.

* License: Apache License, Version 2.0

</details>

### comma-deps-raylib

raylib with CFFI and nanobind Python bindings (commaai fork)

`pip install comma-deps-raylib` · installs (wheel) · licence: not stated · rank 13185 · last release 2026-11-08 · [PyPI](https://pypi.org/project/comma-deps-raylib/)

### cdk-cloudformation-datadog-monitors-monitor

Datadog Monitor 4.12.0

`pip install cdk-cloudformation-datadog-monitors-monitor` · installs (wheel) · licence: OSI Approved · rank 13194 · last release 2026-09-21 · [PyPI](https://pypi.org/project/cdk-cloudformation-datadog-monitors-monitor/) · [source](https://github.com/cdklabs/cdk-cloudformation.git)

<details><summary>README extract</summary>

> AWS CDK L1 construct and data structures for the AWS CloudFormation Registry type `Datadog::Monitors::Monitor` v4.12.0.

Datadog Monitor 4.12.0

Sections: datadog-monitors-monitor, Description, Usage, Feedback

</details>

### clabe

Validate and generate the control digit of a CLABE in Mexico

`pip install clabe` · installs (wheel) · licence: MIT License · rank 13205 · last release 2026-08-05 · [PyPI](https://pypi.org/project/clabe/)

<details><summary>README extract</summary>

Librería para validar y calcular un número CLABE basado en

Python 3.8 o superior.

Se puede instalar desde Pypi usando

Example:
```python
from pydantic import BaseModel, ValidationError

from clabe import Clabe

class Account(BaseModel):
    id: str
    clabe: Clabe

account = Account(id='123', clabe='723010123456789019')
print(account)
"""
id='123' clabe='723010123456789019'
"""

try:
    account = Account(id='321', clabe='000000000000000011')
except ValidationError as exc:
...
```

...

</details>

### cloudcheck

Detailed database of cloud providers. Instantly look up a domain or IP address

`pip install cloudcheck` · installs (wheel) · licence: not stated · rank 13262 · last release 2026-10-30 · [PyPI](https://pypi.org/project/cloudcheck/)

<details><summary>README extract</summary>

> [!TIP]
> UPDATE 01-2026: Now supports REST API!

> [!NOTE]
> UPDATE 12-2025: Now supports government agencies (DoD, FBI, UK MoD, RU FSO)!

> [!IMPORTANT]
> UPDATE 12-2025: Now rewritten in Rust!

CloudCheck is a simple Rust tool to check whether an IP address or hostname belongs to a cloud provider. It includes:

- A Rust CLI
- A Rust library ...

Example:
```python
import asyncio
from cloudcheck import CloudCheck

async def main():
    cloudcheck = CloudCheck()
    results = await cloudcheck.lookup("8.8.8.8")
    print(results) # [{'name': 'Google', 'tags': ['cloud']}]

asyncio.run(main())
```

...

</details>

### cloudauthz

Implements means of authorization delegation on cloud-based resource providers.

`pip install cloudauthz` · installs (wheel) · licence: MIT · rank 13278 · last release 2019-06-30 · [PyPI](https://pypi.org/project/cloudauthz/)

<details><summary>README extract</summary>

Example:
```python
from cloudauthz import *

cloudauthz = CloudAuthz()
config = {
    "id_token": " ... ",
    "role_arn": " ... "
}
credentials = cloudauthz.authorize("aws", config)
```

Sections: CloudAuthz, Example

</details>

### coherent.licensed

License management tooling for Coherent System and skeleton projects

`pip install coherent.licensed` · installs (wheel) · licence: MIT · rank 13311 · last release 2025-06-02 · [PyPI](https://pypi.org/project/coherent.licensed/) · [source](https://github.com/coherent-oss/coherent.licensed)

<details><summary>README extract</summary>

This library was built for coherent.build and skeleton projects to inject a license file at build time to reflect the license declared in the License Expression.

</details>

### cuequivariance-ops-cu12

cuequivariance-ops - GPU Accelerated Extensions for Equivariant Primitives

`pip install cuequivariance-ops-cu12` · installs (wheel) · licence: not stated · rank 13317 · last release 2026-10-15 · [PyPI](https://pypi.org/project/cuequivariance-ops-cu12/) · [docs](https://docs.nvidia.com/cuda/cuequivariance/)

<details><summary>README extract</summary>

`cuequivariance_ops` provides CUDA kernels for the
cuEquivariance.
This python module does not contain any python bindings.
When imported, it loads the shared library that contains the CUDA kernels.

Refer to
cuEquivariance.

Sections: cuequivariance-ops, Introduction, Documentation

</details>

### cmeel-eigen

cmeel distribution for Eigen. Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.

`pip install cmeel-eigen` · installs (wheel) · licence: Apache-2.0 · rank 13329 · last release 2025-10-15 · [PyPI](https://pypi.org/project/cmeel-eigen/) · [source](https://github.com/cmake-wheel/cmeel-eigen.git)

### comma-deps-acados

acados solvers + Python interface, with a slimmed casadi vendored alongside

`pip install comma-deps-acados` · installs (wheel) · licence: not stated · rank 13331 · last release 2026-11-08 · [PyPI](https://pypi.org/project/comma-deps-acados/)

### clickhouse-migrations

Simple file-based migrations for clickhouse

`pip install clickhouse-migrations` · installs (wheel) · licence: MIT · rank 13333 · last release 2026-11-03 · [PyPI](https://pypi.org/project/clickhouse-migrations/) · [source](https://github.com/zifter/clickhouse-migrations)

<details><summary>README extract</summary>

Simple, file-based schema migrations for ClickHouse — the most actively maintained ClickHouse migration tool for Python. Write plain `.sql` files, apply them from the CLI, your code, CI, or Docker. Cluster-aware, with support for both the native `clickhouse-driver` and the official `clickhouse-connect` driver.

Features:
* Multi-statement migrations — more than one query per `.sql` file
* Cluster-aware — keeps migration state consistent across all cluster nodes
* Zero-config file format — `{VERSION}_{name}.sql`, applied in order
* Run anywhere — CLI, Python API, ...

Example:
```python
FILE                     LEVEL    CHECK         MESSAGE
003_add_users.sql:4      error    unterminated  string literal is never closed: the statement splitter reaches the end of the file inside it
...

</details>

### cplex

A Python interface to the CPLEX Callable Library, Community Edition.

`pip install cplex` · installs (wheel) · licence: Proprietary · rank 13362 · last release 2026-07-15 · [PyPI](https://pypi.org/project/cplex/)

<details><summary>README extract</summary>

A Python interface to the CPLEX Callable Library, Community Edition

The CPLEX Python API is a Python package named cplex that allows the Callable
Library to be accessed from the Python programming language. It is equally
suitable for interactive use through the Python interpreter or for writing
scripts or full-fledged applications. ...

</details>

### camel-ai

Communicative Agents for AI Society Study

`pip install camel-ai` · installs (wheel) · licence: Apache-2.0 · rank 13363 · last release 2026-03-22 · [PyPI](https://pypi.org/project/camel-ai/) · [docs](https://docs.camel-ai.org) · [source](https://github.com/camel-ai/camel)

<details><summary>README extract</summary>

[][docs-url]
[][discord-url]
[][x-url]
[][reddit-url]
[][wechat-url]
[][huggingface-url]
[][star-url]
[][package-license-url]
[][package-download-url]
[][join-us]

English |
简体中文 |
日本語

Features:
We are a community-driven research collective comprising over 100 researchers dedicated to advancing frontier research in Multi-Agent Systems. Researchers worldwide choose CAMEL for their studies based on the following reasons. ...

Example:
```python
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.agents import ChatAgent
from camel.toolkits import SearchToolkit

model = ModelFactory.create(
  model_platform=ModelPlatformType.OPENAI,
  model_type=ModelType.GPT_4O,
  model_config_dict={"temperature": 0.0},
)

...
```

...

</details>

### comma-deps-gcc-arm-none-eabi

ARM GCC toolchain for bare-metal targets

`pip install comma-deps-gcc-arm-none-eabi` · installs (wheel) · licence: not stated · rank 13400 · last release 2026-11-08 · [PyPI](https://pypi.org/project/comma-deps-gcc-arm-none-eabi/)

### cdktf-cdktf-provider-null

Prebuilt null Provider for Terraform CDK (cdktf)

`pip install cdktf-cdktf-provider-null` · installs (wheel) · licence: OSI Approved · rank 13405 · last release 2025-12-10 · [PyPI](https://pypi.org/project/cdktf-cdktf-provider-null/) · [source](https://github.com/cdktf/cdktf-provider-null.git)

<details><summary>README extract</summary>

HashiCorp made the decision to stop publishing new versions of prebuilt Terraform null provider bindings for CDK for Terraform on December 10, 2025. As such, this repository has been archived and is no longer supported in any way by HashiCorp. ...

Sections: Deprecated Packages, NPM, PyPI, Nuget, Maven, Go, Docs

</details>

### cdk-secret-manager-wrapper-layer

cdk-secret-manager-wrapper-layer

`pip install cdk-secret-manager-wrapper-layer` · installs (wheel) · licence: OSI Approved · rank 13435 · last release 2026-11-07 · [PyPI](https://pypi.org/project/cdk-secret-manager-wrapper-layer/) · [source](https://github.com/neilkuan/cdk-secret-manager-wrapper-layer.git)

<details><summary>README extract</summary>

that Lambda layer uses a wrapper script to fetch information from Secrets Manager and create environmental variables.

> idea from source

2025-03-02: v2.1.0

* Added architecture parameter support for Lambda Layer
* Updated Python runtime from 3.9 to 3.13
* Fixed handler name in example code
* Improved layer initialization and referencing ...

Example:
```python
import { App, Stack, CfnOutput, Duration } from 'aws-cdk-lib';
import { Effect, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { Function, Runtime, Code, FunctionUrlAuthType, Architecture } from 'aws-cdk-lib/aws-lambda';
import { CfnSecret } from 'aws-cdk-lib/aws-secretsmanager';
...
```

Sections: `cdk-secret-manager-wrapper-layer`, Updates, Example

</details>

### caido-sdk-client

Client SDK for interacting with a Caido instance

`pip install caido-sdk-client` · installs (wheel) · licence: MIT · rank 13444 · last release 2026-10-05 · [PyPI](https://pypi.org/project/caido-sdk-client/)

<details><summary>README extract</summary>

Github
 Documentation
 Discord

This is the Caido client SDK for Python.

The goal of this SDK is to allow scripts to access Caido instances. It handles authentication, GraphQL and REST.

We recommend you look at the examples to learn how to use it.

Example:
```python
import asyncio
from caido_sdk_client import AuthCacheFile, Client, PATAuthOptions

async def main():
    client = Client(
        "
        auth=PATAuthOptions(
            pat="caido_xxxxxx",
            cache=AuthCacheFile(file=".secrets.json"),
        ),
    )

    await client.connect()

    viewer = await client.user.viewer()
...
```

</details>

### comma-deps-capnproto

Cap'n Proto serialization library and compiler

`pip install comma-deps-capnproto` · installs (wheel) · licence: not stated · rank 13461 · last release 2026-11-08 · [PyPI](https://pypi.org/project/comma-deps-capnproto/)

### compliance-trestle

Tools to manage & autogenerate python objects representing the OSCAL layers/models

`pip install compliance-trestle` · installs (wheel) · licence: Apache-2.0 · rank 13469 · last release 2026-10-05 · [PyPI](https://pypi.org/project/compliance-trestle/) · [docs](https://oscal-compass.github.io/compliance-trestle) · [source](https://github.com/oscal-compass/compliance-trestle)

<details><summary>README extract</summary>

Trestle is an ensemble of tools that enable the creation, validation, and governance of documentation artifacts for compliance needs. It leverages NIST's OSCAL as a standard data format for interchange between tools and people, and provides an opinionated approach to OSCAL adoption. ...

Features:
Compliance suffers from being a complex topic that is hard to articulate simply. It involves complete and accurate execution of multiple procedures across many disciplines (e.g. ...

Sections: Compliance-trestle (also known as `trestle`), Why Trestle, Machine readable compliance format, Quick Start, Complete documentation and tutorials, Demos, v4: stable (maintenance mode), v3: stable (deprecated), v2: stable (deprecated)

</details>

### cosmos-xenna

A framework for building and running distributed, AI-powered data pipelines using Ray

`pip install cosmos-xenna` · installs (wheel) · licence: not stated · rank 13492 · last release 2026-11-02 · [PyPI](https://pypi.org/project/cosmos-xenna/)

<details><summary>README extract</summary>

> [!IMPORTANT]
> ## 🚀 Cosmos 3 Has Arrived
> Cosmos 3 is NVIDIA's next-generation foundation model platform for Physical AI. Compared with Cosmos-Xenna, Cosmos 3 unifies reasoning, world prediction, simulation, transfer, and action generation within a single model family and ecosystem. ...

Example:
```python
import cosmos_xenna.pipelines.v1 as pipelines_v1
import vllm
from transformers import AutoTokenizer
from cosmos_internal_data_utils.utils import model_utils

class LargeModelStage(pipelines_v1.Stage):
    def init(self, model_name: str, tensor_parallel_size: int):
        self._model_name = model_name
        self._tp_size = tensor_parallel_size

...
```

...

</details>

### comma-deps-ffmpeg

FFmpeg media tools and libraries (minimal build for openpilot)

`pip install comma-deps-ffmpeg` · installs (wheel) · licence: not stated · rank 13502 · last release 2026-11-08 · [PyPI](https://pypi.org/project/comma-deps-ffmpeg/)

### caido-server-auth

Authenticate with a Caido instance.

`pip install caido-server-auth` · installs (wheel) · licence: not stated · rank 13508 · last release 2026-10-05 · [PyPI](https://pypi.org/project/caido-server-auth/)

<details><summary>README extract</summary>

Github
 Documentation
 Discord

Authenticate with a Caido instance using device code flow.

Example:
```python
import asyncio
import os

from caido_server_auth import (
    AuthClient,
    AuthClientOptions,
    AuthenticationRequest,
    BrowserApprover,
)

def on_request(request: AuthenticationRequest) -> None:
    print(f"Visit: {request.verification_url}")
    print(f"Expires at: {request.expires_at.isoformat()}")

async def main() -> None:
...
```

Sections: 👋 Server Auth, Examples

</details>

### claripy

An abstraction layer for constraint solvers

`pip install claripy` · installs (wheel) · licence: BSD-2-Clause · rank 13518 · last release 2026-10-07 · [PyPI](https://pypi.org/project/claripy/)

<details><summary>README extract</summary>

Claripy is an abstracted constraint-solving wrapper.

Project repository:

Documentation:

Example:
```python
>>> import claripy
>>> a = claripy.BVV(3, 32)
>>> b = claripy.BVS('var_b', 32)
>>> s = claripy.Solver()
>>> s.add(b > a)
>>> print(s.eval(b, 1)[0])
```

Sections: claripy, Project Links, Usage

</details>

### comma-deps-zstd

Zstandard compression library (static build)

`pip install comma-deps-zstd` · installs (wheel) · licence: not stated · rank 13521 · last release 2026-11-08 · [PyPI](https://pypi.org/project/comma-deps-zstd/)

### comma-deps-eigen

Eigen C++ linear algebra headers

`pip install comma-deps-eigen` · installs (wheel) · licence: not stated · rank 13525 · last release 2026-11-08 · [PyPI](https://pypi.org/project/comma-deps-eigen/)

### cloudfoundry-client

A client library for CloudFoundry

`pip install cloudfoundry-client` · installs (wheel) · licence: not stated · rank 13538 · last release 2026-10-28 · [PyPI](https://pypi.org/project/cloudfoundry-client/) · [docs](https://pypi.org/project/cloudfoundry-client/) · [source](https://github.com/cloudfoundry-community/cf-python-client)

<details><summary>README extract</summary>

The cf-python-client repo contains a Python client library for Cloud Foundry.

Example:
```python
from cloudfoundry_client.client import CloudFoundryClient
target_endpoint = '
proxy = dict(http=os.environ.get('HTTP_PROXY', ''), https=os.environ.get('HTTPS_PROXY', ''))
client = CloudFoundryClient(target_endpoint, proxy=proxy, verify=False)
# init with user credentials
client.init_with_user_credentials('login', 'password')
...
```

Sections: Cloudfoundry python client, From pip, From sources, Run the client, Use the client in your code, Client, API V2, Entities, Available managers, API V3, Networking, policy server, Application logs

</details>

### comma-deps-imgui

Dear ImGui + ImPlot + GLFW 3.4 (static)

`pip install comma-deps-imgui` · installs (wheel) · licence: not stated · rank 13549 · last release 2026-11-08 · [PyPI](https://pypi.org/project/comma-deps-imgui/)

### comma-deps-ncurses

ncurses terminal library (static build)

`pip install comma-deps-ncurses` · installs (wheel) · licence: not stated · rank 13556 · last release 2026-11-08 · [PyPI](https://pypi.org/project/comma-deps-ncurses/)

### comma-deps-libusb

libusb USB device access library (static build)

`pip install comma-deps-libusb` · installs (wheel) · licence: not stated · rank 13560 · last release 2026-11-08 · [PyPI](https://pypi.org/project/comma-deps-libusb/)

### charmlibs-pathops

A pathlib-like interface for Juju K8s charms to interact with files in their workload container.

`pip install charmlibs-pathops` · installs (wheel) · licence: Apache-2.0 · rank 13571 · last release 2026-06-16 · [PyPI](https://pypi.org/project/charmlibs-pathops/) · [docs](https://documentation.ubuntu.com/charmlibs/reference/charmlibs/pathops/) · [source](https://github.com/canonical/charmlibs/tree/main/pathops)

<details><summary>README extract</summary>

`pathops` provides a `pathlib`-like interface for local filesystem and workload container paths for Juju Charms.

To install, add `charmlibs-pathops` to your requirements. Then in your Python code, import as:

Check out the reference docs on the charmlibs docsite.

Example:
```python
import ops
from charmlibs import pathops

class KubernetesCharm(ops.CharmBase):
    def init(self, framework: ops.Framework):
        super().init(framework)
        container = self.unit.get_container('container-name')
        self.root = pathops.ContainerPath('/', container=container)

# or

class MachineCharm(ops.CharmBase):
...
```

Sections: charmlibs-pathops, Getting started

</details>

### comma-deps-bootstrap-icons

Bootstrap Icons SVG sprite and TTF font

`pip install comma-deps-bootstrap-icons` · installs (wheel) · licence: not stated · rank 13606 · last release 2026-11-08 · [PyPI](https://pypi.org/project/comma-deps-bootstrap-icons/)

### content-core

Extract what matters from any media source. Available as Python Library, macOS Service, CLI and MCP Server

`pip install content-core` · installs (wheel) · licence: not stated · rank 13625 · last release 2026-11-08 · [PyPI](https://pypi.org/project/content-core/)

<details><summary>README extract</summary>

Extract, process, and summarize content from URLs, files, and text through a unified async Python API, CLI, or MCP server.

Example:
```python
import content_core

result = await content_core.extract_content(url="
print(result.content)
```

Sections: Content Core, Quick Start, CLI Usage, Extract, Summarize, MCP Server, Configuration, Python API, Extraction, Summarization, MCP Integration, Agent Skill (Claude Code & Codex), AI Providers

</details>

### comma-deps-zeromq

ZeroMQ messaging library (static build)

`pip install comma-deps-zeromq` · installs (wheel) · licence: not stated · rank 13631 · last release 2026-09-11 · [PyPI](https://pypi.org/project/comma-deps-zeromq/)

### crypto-cpp-py

This is a packaged crypto-cpp program

`pip install crypto-cpp-py` · installs (wheel) · licence: not stated · rank 13676 · last release 2026-04-03 · [PyPI](https://pypi.org/project/crypto-cpp-py/)

<details><summary>README extract</summary>

A python packaged crypto-cpp library, that can be used for hashing and signing messages in starknet.

- ecdsa,
- sympy,
- pywin32 (Windows only),
- cmake [optional, for building package from sdist; can be installed with `pip install crypto-cpp-py[build]`]


Sections: Crypto-cpp-py, Dependencies, Version 2.0.0 (2026-04-03), Version 1.4.5 (2024-11-20), Version 1.4.4 (2024-01-30), Version 1.4.0 (2023-05-12), Version 1.3.1 (2023-04-27), Version 1.3.0 (2023-04-20)

</details>

### codebleu

Unofficial CodeBLEU implementation that supports Linux, MacOS and Windows available on PyPI.

`pip install codebleu` · installs (wheel) · licence: MIT License · rank 13702 · last release 2024-05-30 · [PyPI](https://pypi.org/project/codebleu/)

<details><summary>README extract</summary>

This repository contains an unofficial `CodeBLEU` implementation that supports `Linux`, `MacOS` (incl. M-series) and `Windows`. It is available through `PyPI` and the `evaluate` library.

Available for: `Python`, `C`, `C#`, `C++`, `Java`, `JavaScript`, `PHP`, `Go`, `Ruby`, `Rust`. ...

Example:
```python
from codebleu import calc_codebleu

prediction = "def add ( a , b ) :\n return a + b"
reference = "def sum ( first , second ) :\n return second + first"

result = calc_codebleu([reference], [prediction], lang="python", weights=(0.25, 0.25, 0.25, 0.25), tokenizer=None)
print(result)
# {
# 'codebleu': 0.5537,
# 'ngram_match_score': 0.1041,
...
```

Sections: CodeBLEU, Metric Description, Usage

</details>

### celery-redis-cluster

A Redis Cluster backend for Celery

`pip install celery-redis-cluster` · installs (wheel) · licence: MIT License · rank 13723 · last release 2025-02-14 · [PyPI](https://pypi.org/project/celery-redis-cluster/)

<details><summary>README extract</summary>

A Redis Cluster backend implementation for Celery. This package extends Celery's Redis backend to work with Redis Cluster, providing better scalability and high availability through Redis Cluster's sharding and replication capabilities.

Example:
```python
from celery import Celery

from celery_redis_cluster_backend import install_redis_cluster_backend

app = Celery('your_app',
             broker='redis://localhost:6379/0',
             backend='redis+cluster://localhost:6379/0')
```

Sections: Celery Redis Cluster, Usage, Configuration, Requirements

</details>

### cdktf-cdktf-provider-google

Prebuilt google Provider for Terraform CDK (cdktf)

`pip install cdktf-cdktf-provider-google` · installs (wheel) · licence: OSI Approved · rank 13768 · last release 2025-12-10 · [PyPI](https://pypi.org/project/cdktf-cdktf-provider-google/) · [source](https://github.com/cdktf/cdktf-provider-google.git)

<details><summary>README extract</summary>

HashiCorp made the decision to stop publishing new versions of prebuilt Terraform google provider bindings for CDK for Terraform on December 10, 2025. As such, this repository has been archived and is no longer supported in any way by HashiCorp. ...

Sections: Deprecated Packages, NPM, PyPI, Nuget, Maven, Go, Docs

</details>

### charmlibs-interfaces-tls-certificates

The charmlibs.interfaces.tls_certificates package.

`pip install charmlibs-interfaces-tls-certificates` · installs (wheel) · licence: Apache Software License · rank 13771 · last release 2026-11-04 · [PyPI](https://pypi.org/project/charmlibs-interfaces-tls-certificates/) · [docs](https://canonical.com/juju/docs/charmlibs/reference/charmlibs/interfaces/tls-certificates) · [source](https://github.com/canonical/charmlibs/tree/main/interfaces/tls-certificates)

<details><summary>README extract</summary>

The `tls-certificates` interface library.

To install, add `charmlibs-interfaces-tls-certificates` to your Python dependencies. Then in your Python code, import as:

Read more:
- Tutorial
- Library reference
- How to configure certificate requests
- Explanation of the library design

Example:
```python
from charmlibs.interfaces import tls_certificates
```

</details>

### czifile

Read Carl Zeiss image files (CZI)

`pip install czifile` · installs (wheel) · licence: BSD-3-Clause · rank 13825 · last release 2026-10-14 · [PyPI](https://pypi.org/project/czifile/) · [docs](https://www.cgohlke.com/docs/czifile/) · [source](https://github.com/cgohlke/czifile)

<details><summary>README extract</summary>

Czifile is a Python library for reading image data and metadata from
Carl Zeiss Image (CZI) files, the native file format of ZEN by
Carl Zeiss Microscopy GmbH.

Czifile is a pure-Python library under the BSD-3-Clause license. ...

Sections: Read Carl Zeiss image files (CZI), Quickstart, Requirements, Revisions, Notes, Examples

</details>

### coscmd

simple command for cos

`pip install coscmd` · installs from source (sdist only) · licence: MIT · rank 13916 · last release 2025-05-13 · [PyPI](https://pypi.org/project/coscmd/)

<details><summary>README extract</summary>

___

腾讯云COS命令行工具, 最新版本支持Python3.x, 1.8.x版本支持Python2.6/Python2.7。

安装指南

使用pip安装:
手动安装:
使用方法

使用coscmd，参照

</details>

### cdktf-cdktf-provider-random

Prebuilt random Provider for Terraform CDK (cdktf)

`pip install cdktf-cdktf-provider-random` · installs (wheel) · licence: OSI Approved · rank 13935 · last release 2025-12-10 · [PyPI](https://pypi.org/project/cdktf-cdktf-provider-random/) · [source](https://github.com/cdktf/cdktf-provider-random.git)

<details><summary>README extract</summary>

HashiCorp made the decision to stop publishing new versions of prebuilt Terraform random provider bindings for CDK for Terraform on December 10, 2025. As such, this repository has been archived and is no longer supported in any way by HashiCorp. ...

Sections: Deprecated Packages, NPM, PyPI, Nuget, Maven, Go, Docs

</details>

### cursive

Cursive implements OpenStack-specific validation of digital signatures.

`pip install cursive` · installs (wheel) · licence: Apache-2.0 · rank 13966 · last release 2026-08-26 · [PyPI](https://pypi.org/project/cursive/) · [source](https://opendev.org/openstack/cursive)

<details><summary>README extract</summary>

Cursive implements OpenStack-specific validation of digital signatures.

As OpenStack continues to mature, robust security controls become increasingly
critical. The cursive project contains code extracted from various OpenStack
projects for verifying digital signatures. ...

Features:
* TODO

Sections: cursive, Features

</details>

### cc-transcript

Grep every Claude Code session you've ever run.

`pip install cc-transcript` · installs (wheel) · licence: PolyForm-Noncommercial-1.0.0 · rank 14001 · last release 2026-11-07 · [PyPI](https://pypi.org/project/cc-transcript/) · [docs](https://yasyf.github.io/cc-transcript/) · [source](https://github.com/yasyf/cc-transcript)

<details><summary>README extract</summary>

Grep every Claude Code session you've ever run. The lossless Rust parser reads Claude Code's on-disk JSONL at 169 MB/s; the compiled CLI greps it and renders one line per event, 25 ms cold.

Every session is already on disk under `~/.claude/projects`. `list` finds them newest first, and `stats` collapses one into a screenful: ...

Example:
```python
from cc_transcript import NOISE_SPEC, discover, parse

transcript = parse(discover()[0], drop=NOISE_SPEC)
print(len(transcript.events), "events after the noise drop")
```

Sections: Get started, Use cases, Ask Claude what you asked Claude yesterday, Find the session where you fixed that bug, Debug a token blowup from transcript evidence, Script it from Python, JSON output schema, More in the docs

</details>

### composio-gemini

Use Composio to get an array of tools with your Gemini agent.

`pip install composio-gemini` · installs (wheel) · licence: Apache Software License · rank 14010 · last release 2026-11-03 · [PyPI](https://pypi.org/project/composio-gemini/)

<details><summary>README extract</summary>

Adapts Composio tools to the `google-genai` SDK as Python callables compatible with Gemini's Automatic Function Calling.

Example:
```python
from composio import Composio
from composio_gemini import GeminiProvider
from google import genai
from google.genai import types

composio = Composio(provider=GeminiProvider())
client = genai.Client()

# Create a session for your user
session = composio.create(user_id="user_123")
tools = session.tools()

...
```

Sections: composio-gemini, Quickstart, composio-gemini vs composio-google, Links

</details>

### ctrader_open_api

A Python package for interacting with cTrader Open API

`pip install ctrader_open_api` · installs (wheel) · licence: MIT License · rank 14022 · last release 2024-06-26 · [PyPI](https://pypi.org/project/ctrader_open_api/) · [docs](https://spotware.github.io/OpenApiPy)

<details><summary>README extract</summary>

A Python package for interacting with cTrader Open API.

This package uses Twisted and it works asynchronously.

- Free software: MIT

Features:
* Works asynchronously by using Twisted

* Methods return Twisted deferreds

* It contains the Open API messages files so you don't have to do the compilation

* Makes handling request responses easy by using Twisted deferreds

Example:
```python
from ctrader_open_api import Client, Protobuf, TcpProtocol, Auth, EndPoints
from ctrader_open_api.messages.OpenApiCommonMessages_pb2 import *
from ctrader_open_api.messages.OpenApiCommonMessages_pb2 import *
from ctrader_open_api.messages.OpenApiMessages_pb2 import *
from ctrader_open_api.messages.OpenApiModelMessages_pb2 import *
...
```

Sections: OpenApiPy, Features, Insallation, Usage, Dependencies

</details>

### cylp

A Python interface for CLP, CBC, and CGL

`pip install cylp` · installs (wheel) · licence: EPL-2.0 · rank 14047 · last release 2026-10-28 · [PyPI](https://pypi.org/project/cylp/) · [docs](https://coin-or.github.io/CyLP)

<details><summary>README extract</summary>

CyLP is a Python interface to COIN-OR’s Linear and mixed-integer program solvers
(CLP, CBC, and CGL). CyLP’s unique feature is that you can use it to alter the
solution process of the solvers from within Python. For example, you may
define cut generators, branch-and-bound strategies, and primal/dual Simplex
pivot rules completely in Python. ...

Example:
```python
import numpy as np
from cylp.cy import CyClpSimplex
from cylp.py.modeling.CyLPModel import CyLPArray

s = CyClpSimplex()

# Add variables
x = s.addVariable('x', 3)
y = s.addVariable('y', 2)

# Create coefficients and bounds
A = np.matrix([[1., 2., 0],[1., 0, 1.]])
B = np.matrix([[1., 0, 0], [0, 0, 1.]])
D = np.matrix([[1., 2.],[0, 1]])
...
```

...

</details>

### compel

A prompting enhancement library for transformers-type text embedding systems.

`pip install compel` · installs (wheel) · licence: MIT License · rank 14062 · last release 2026-10-10 · [PyPI](https://pypi.org/project/compel/)

<details><summary>README extract</summary>

A text prompt weighting and blending library for transformers-type text embedding systems, by @damian0815.

With a flexible and intuitive syntax, you can re-weight different parts of a prompt string and thus re-weight the different parts of the embedding tensor produced from the string. ...

Example:
```python
from diffusers import StableDiffusionPipeline
from compel import CompelForSD

pipeline = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
compel = CompelForSD(pipeline)

# upweight "ball"
prompt = "a cat playing with a ball++ in the forest"
conditioning = compel(prompt)

# generate image
...
```

...

</details>

### cube-http-client

Pythonic HTTP client for Cube.js REST API (sync + async)

`pip install cube-http-client` · installs (wheel) · licence: MIT · rank 14077 · last release 2025-07-10 · [PyPI](https://pypi.org/project/cube-http-client/) · [docs](https://github.com/mharrisb1/cube-http-client) · [source](https://github.com/mharrisb1/cube-http-client)

<details><summary>README extract</summary>

<!--toc:start-->

- cube-http-client
 - Installation
 - Quickstart
 - Client Configuration
 - Using Custom HTTP Clients
 - Detailed Usage
 - Synchronous
 - Using Context Managers
 - Asynchronous
 - Working with Query Responses
 - Custom Response Models
 - SQL Query Compilation
 - Error Handling
 - Support Coverage
 <!--toc:end--> ...

Example:
```python
import cube_http

cube = cube_http.Client({"url": "...", "token": "..."})

# get metadata
meta = cube.v1.meta()

# load query results
results = cube.v1.load(
    {
        "query": {
            "measures": ["tasks.count"],
            "dimensions": ["tasks.status"],
        }
    }
)

# compile to SQL
compiled_sql_response = cube.v1.sql(
    {
...
```

...

</details>

### contrast-agent

Contrast Security's agent for Python web frameworks

`pip install contrast-agent` · installs (wheel) · licence: LicenseRef-ContrastSecurity-ContrastPlatformLicense · rank 14102 · last release 2026-10-29 · [PyPI](https://pypi.org/project/contrast-agent/)

<details><summary>README extract</summary>

The Contrast Python Agent provides interactive vulnerability discovery and
runtime protection for web applications. The agent is a WSGI-, ASGI-, and
framework-specific middleware that's compatible with the most popular web
application frameworks.

For the most up-to-date documentation please see
Contrast Docs

</details>

### chalk-sqlalchemy-redshift

Amazon Redshift Dialect for sqlalchemy (Chalk fork)

`pip install chalk-sqlalchemy-redshift` · installs (wheel) · licence: MIT License · rank 14155 · last release 2025-06-15 · [PyPI](https://pypi.org/project/chalk-sqlalchemy-redshift/)

<details><summary>README extract</summary>

Amazon Redshift dialect for SQLAlchemy.

Example:
```python
>>> import sqlalchemy as sa
>>> sa.create_engine('redshift+psycopg2://username@host.amazonaws.com:5439/database')
Engine(redshift+psycopg2://username@host.amazonaws.com:5439/database)
```

Sections: sqlalchemy-redshift, Usage, Running Tests, Continuous Integration (CI), Releasing, 0.8.14 (2023-04-07), 0.8.13 (2023-03-28), 0.8.12 (2022-12-08), 0.8.11 (2022-07-27), 0.8.10 (2022-07-21), 0.8.9 (2021-12-15), 0.8.8 (2021-11-03), 0.8.7 (2021-10-27), 0.8.6 (2021-09-22)

</details>

### cockroachdb

CockroachDB adapter for SQLAlchemy

`pip install cockroachdb` · installs (wheel) · licence: Apache Software License · rank 14157 · last release 2020-05-19 · [PyPI](https://pypi.org/project/cockroachdb/)

<details><summary>README extract</summary>

This package has changed names.

Please use sqlalchemy-cockroachdb.

</details>

### cyclonedds

Eclipse Cyclone DDS Python binding

`pip install cyclonedds` · installs from source (sdist only) · licence: EPL-2.0, BSD-3-Clause · rank 14169 · last release 2026-03-20 · [PyPI](https://pypi.org/project/cyclonedds/) · [docs](https://cyclonedds.io/docs) · [source](https://github.com/eclipse-cyclonedds/cyclonedds-python)

<details><summary>README extract</summary>

A Python binding for Eclipse Cyclone DDS.

Sections: Python binding for Eclipse Cyclone DDS, Getting Started, via PyPi, via git, Command line tooling, `cyclonedds ls`, `cyclonedds ps`, `cyclonedds typeof`, `cyclonedds subscribe`, `cyclonedds publish`, `cyclonedds performance`, Extra dependencies, PyOxidizer build

</details>

### crystal-toolkit

Crystal Toolkit is a web app framework from the Materials Project allowing Python

`pip install crystal-toolkit` · installs (wheel) · licence: not stated · rank 14181 · last release 2026-07-21 · [PyPI](https://pypi.org/project/crystal-toolkit/) · [docs](https://docs.crystaltoolkit.org)

<details><summary>README extract</summary>

Sections: Crystal Toolkit, Documentation, Example Apps, Future of This Repository, Contact

</details>

### cdktf-cdktf-provider-github

Prebuilt github Provider for Terraform CDK (cdktf)

`pip install cdktf-cdktf-provider-github` · installs (wheel) · licence: OSI Approved · rank 14184 · last release 2025-12-10 · [PyPI](https://pypi.org/project/cdktf-cdktf-provider-github/) · [source](https://github.com/cdktf/cdktf-provider-github.git)

<details><summary>README extract</summary>

HashiCorp made the decision to stop publishing new versions of prebuilt Terraform github provider bindings for CDK for Terraform on December 10, 2025. As such, this repository has been archived and is no longer supported in any way by HashiCorp. ...

Sections: Deprecated Packages, NPM, PyPI, Nuget, Maven, Go, Docs

</details>

### csv-diff

Python CLI tool and library for diffing CSV and JSON files

`pip install csv-diff` · installs (wheel) · licence: Apache Software License · rank 14198 · last release 2024-09-06 · [PyPI](https://pypi.org/project/csv-diff/)

<details><summary>README extract</summary>

Tool for viewing the difference between two CSV, TSV or JSON files. See Generating a commit log for San Francisco’s official list of trees (and the sf-tree-history repo commit log) for background information on this project.

Sections: csv-diff, Usage, JSON output, Adding templated extras, As a Python library, As a Docker container, Build the image, Run the container, Alternatives

</details>

### catt

Cast All The Things allows you to send videos from many, many online sources to your Chromecast.

`pip install catt` · installs (wheel) · licence: BSD License; Other/Proprietary License · rank 14206 · last release 2026-09-24 · [PyPI](https://pypi.org/project/catt/)

<details><summary>README extract</summary>

Cast All The Things allows you to send videos from many, many online
sources (YouTube, Vimeo, and a few hundred others) to your Chromecast.
It also allows you to cast local files or render websites.

Installation

You can run Cast All The Things with uv without installing:

 uvx catt

You can install Cast All The Things with pipx: ...

Sections: Cast All The Things, Configuration file

</details>

### chainladder

Chainladder Package - P&C Loss Reserving package

`pip install chainladder` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 14222 · last release 2026-09-15 · [PyPI](https://pypi.org/project/chainladder/) · [docs](https://chainladder-python.readthedocs.io/) · [source](https://github.com/casact/chainladder-python)

<details><summary>README extract</summary>

Welcome! The chainladder package was built to be able to handle all of your actuarial needs in python. It consists of popular actuarial tools, such as triangle data manipulation, link ratios calculation, and IBNR estimates with both deterministic and stochastic models. ...

Sections: chainladder (python), chainladder: Property and Casualty Loss Reserving in Python, Documentation Site

</details>

### cashaddress

Python tool for converty bitcoin cash legacy addresses

`pip install cashaddress` · installs from source (sdist only) · licence: not stated · rank 14274 · last release 2019-05-15 · [PyPI](https://pypi.org/project/cashaddress/)

### canvas

SDK to customize event-driven actions in your Canvas instance

`pip install canvas` · installs (wheel) · licence: MIT · rank 14299 · last release 2026-11-06 · [PyPI](https://pypi.org/project/canvas/)

<details><summary>README extract</summary>

Sections: Getting Started, Authentication, Migrating from `credentials.ini` to Canvas Platform, Instance API credentials, Canvas Platform, Which plugins go through Canvas Platform, Service accounts for CI/CD, Deploying from a monorepo, `canvas login`, `canvas logout`, `canvas whoami`, `canvas init`, `canvas deploy`, `canvas clone`

</details>

### chembl-structure-pipeline

ChEMBL Structure Pipeline

`pip install chembl-structure-pipeline` · installs (wheel) · licence: MIT · rank 14326 · last release 2025-11-24 · [PyPI](https://pypi.org/project/chembl-structure-pipeline/)

<details><summary>README extract</summary>

ChEMBL protocols used to standardise and salt strip molecules. First used in ChEMBL 26.

Check the wiki and paper[[1]](#1) for a detailed description of the different processes.

Example:
```python
from chembl_structure_pipeline import standardizer

o_molblock = """
  Mrv1810 07121910172D

  4  3  0  0  0  0            999 V2000
   -2.5038    0.4060    0.0000 C   0  0  3  0  0  0  0  0  0  0  0  0
   -2.5038    1.2310    0.0000 O   0  5  0  0  0  0  0  0  0  0  0  0
   -3.2182   -0.0065    0.0000 N   0  3  0  0  0  0  0  0  0  0  0  0
...
```

Sections: ChEMBL Structure Pipeline, Usage, Standardise a compound (info), Get the parent compound (info), Check a compound (info), References

</details>

### code-annotations

Extensible tools for parsing annotations in codebases

`pip install code-annotations` · installs (wheel) · licence: Apache Software License · rank 14337 · last release 2026-03-13 · [PyPI](https://pypi.org/project/code-annotations/)

<details><summary>README extract</summary>

Extensible tools for parsing annotations in codebases

Features:
This package provides configurable and extensible tools for parsing and
summarizing annotations in a wide range of codebases. Originally intended for
annotating code which stores personally identifiable information (PII), these
tools are optimized ...

Sections: code-annotations, Overview, Documentation, Getting Help, [2.3.2] - 2026-03-02, [2.2.0] - 2025-01-15, [2.1.0] - 2024-12-12, [2.0.0] - 2024-10-18, [1.8.1] - 2024-07-11, [1.8.0] - 2024-03-31, [1.6.0] - 2024-01-31, [1.5.0] - 2023-07-21, [1.4.0] - 2022-05-23, [1.3.0] - 2022-02-07

</details>

### cuequivariance-ops-torch-cu13

cuequivariance-ops-torch - GPU Accelerated Torch Extensions for Equivariant Primitives

`pip install cuequivariance-ops-torch-cu13` · installs (wheel) · licence: not stated · rank 14396 · last release 2026-10-15 · [PyPI](https://pypi.org/project/cuequivariance-ops-torch-cu13/) · [docs](https://docs.nvidia.com/cuda/cuequivariance/)

<details><summary>README extract</summary>

`cuequivariance_ops_torch` provides CUDA kernels for the
cuEquivariance project's PyTorch
components. As such, it contains pytorch bindings to optimized kernels that
cuEquivariance's operations map down to. In general, we advice that you access
those kernels through cuEquivariance, but you may also find them useful on
their own.

Example:
```python
import cuequivariance_ops_torch
```

Sections: cuequivariance-ops-torch, Introduction, Kernel Factory TriMul kernels, KF under `torch.compile`, Documentation, Pairformer inference primitives, Calling convention for declined cells, Usage

</details>

### criticality-score

Gives criticality score for an open source project - DEPRECATED

`pip install criticality-score` · installs (wheel) · licence: Apache Software License · rank 14411 · last release 2023-02-23 · [PyPI](https://pypi.org/project/criticality-score/)

<details><summary>README extract</summary>

The Python version of Criticality Score is deprecated and will no longer receive
updates.

A Go version exists and is under active development and should be used instead.
See for more details.

</details>

### cortex-code-agent-sdk

SDK for interacting with Cortex Code CLI programmatically

`pip install cortex-code-agent-sdk` · installs (wheel) · licence: LicenseRef-Snowflake-Proprietary · rank 14447 · last release 2026-07-31 · [PyPI](https://pypi.org/project/cortex-code-agent-sdk/)

### cowork-server

FastAPI backend for the MindsHub Cowork desktop app

`pip install cowork-server` · does not install on CPython 3.14 · licence: LicenseRef-Proprietary · rank 14480 · last release 2026-11-03 · [PyPI](https://pypi.org/project/cowork-server/) · [source](https://github.com/mindsdb/cowork-server)

<details><summary>README extract</summary>

FastAPI backend for MindsHub Cowork. Manages projects, conversations, files, scheduling, memory, and agent orchestration with a SQLite-backed data layer.

This repo is the Python backend. The frontend (Electron shell + React SPA) lives in a separate repo: `mindsdb/cowork`. They are developed and released independently. ...

Example:
```python
from cowork.api.v1.permissions import AuthenticatedInOrgMode, require

@router.get("/thing", dependencies=[Depends(require(AuthenticatedInOrgMode))])
```

Sections: Cowork Server, Quick Start, Dev setup helper, Nightly production read-only smoke, Logging, Releasing, Nightly staging integration, Architecture, Server modes and terms, Harness system, Streaming & scheduling, Data Layer, SQLite database, Filesystem storage

</details>

### cmeel-urdfdom-headers

cmeel distribution for urdfdom-headers, headers for URDF parsers

`pip install cmeel-urdfdom-headers` · installs (wheel) · licence: BSD-3-Clause · rank 14482 · last release 2026-05-21 · [PyPI](https://pypi.org/project/cmeel-urdfdom-headers/)

<details><summary>README extract</summary>

urdfdom-headers distribution for cmeel packages.

</details>

### code-sandboxes

(no summary)

`pip install code-sandboxes` · installs (wheel) · licence: BSD License · rank 14502 · last release 2026-11-02 · [PyPI](https://pypi.org/project/code-sandboxes/)

<details><summary>README extract</summary>

<!--
 ~ Copyright (c) 2025-2026 Datalayer, Inc.
 ~ BSD 3-Clause License

Code Sandboxes (`code_sandboxes`) is a Python package for running code in isolated sandbox variants through a unified API.

Canonical variant names:

- `cloudflare`
- `coreweave`
- `datalayer`
- `daytona`
- `docker`
- `e2b`
- `eval`
- `google-colab`
- `jupyter-server` ...

Example:
```python
from code_sandboxes import Sandbox

# Option 1: manage a local Jupyter server automatically
with Sandbox.create(variant="jupyter-server") as sandbox:
  print(sandbox.run_code("1 + 1").text)  # 2

# Option 2: connect to an existing Jupyter server
with Sandbox.create(
  variant="jupyter-server",
  server_url="
  token="MY_TOKEN",
) as sandbox:
...
```

...

</details>

### curio

Curio

`pip install curio` · installs from source (sdist only) · licence: BSD · rank 14590 · last release 2022-10-25 · [PyPI](https://pypi.org/project/curio/)

<details><summary>README extract</summary>

Curio is a coroutine-based library for concurrent systems programming. No longer
maintained as a PyPi project. Latest version is available on GitHub.

</details>

### craft-parts

Craft parts tooling

`pip install craft-parts` · installs (wheel) · licence: not stated · rank 14659 · last release 2026-10-08 · [PyPI](https://pypi.org/project/craft-parts/)

<details><summary>README extract</summary>

[][rtd-latest]
[][codecov-status]
[][ruff-site]

Craft Parts supports the _parts_ mechanism common to all craft applications. It
provides a declarative way to obtain, process, and organize data from different sources
before it is packaged into the final artifact.

This library is most useful for app developers in the Starcraft family. ...

Sections: Craft Parts, Documentation

</details>

### celery-redis-poll

A Redis Backend for Celery with polling instead of pub/sub

`pip install celery-redis-poll` · installs (wheel) · licence: MIT License · rank 14672 · last release 2025-02-14 · [PyPI](https://pypi.org/project/celery-redis-poll/)

<details><summary>README extract</summary>

A specialized Redis backend for Celery that replaces the default pub/sub mechanism for task result retrieval with a polling-based approach.

Features:
The default Celery Redis backend uses Redis pub/sub for real-time task result notifications. While pub/sub provides immediate updates, it can face challenges in certain scenarios: ...

Example:
```python
from celery import Celery

app = Celery('your_app',
             broker='redis://localhost:6379/0',
             backend='redis+poll://localhost:6379/0')
```

Sections: Celery Redis Poll Backend, Why Polling Instead of Pub/Sub?, Features, Usage, Requirements

</details>

### cdktf-cdktf-provider-docker

Prebuilt docker Provider for Terraform CDK (cdktf)

`pip install cdktf-cdktf-provider-docker` · installs (wheel) · licence: OSI Approved · rank 14728 · last release 2025-12-10 · [PyPI](https://pypi.org/project/cdktf-cdktf-provider-docker/) · [source](https://github.com/cdktf/cdktf-provider-docker.git)

<details><summary>README extract</summary>

HashiCorp made the decision to stop publishing new versions of prebuilt Terraform docker provider bindings for CDK for Terraform on December 10, 2025. As such, this repository has been archived and is no longer supported in any way by HashiCorp. ...

Sections: Deprecated Packages, NPM, PyPI, Nuget, Maven, Go, Docs

</details>

### cowsay-python

Very basic cowsay implementation

`pip install cowsay-python` · installs (wheel) · licence: MIT License · rank 14740 · last release 2024-08-17 · [PyPI](https://pypi.org/project/cowsay-python/) · [source](https://github.com/carderne/cowsay-python)

<details><summary>README extract</summary>

A very basic Python implementation of cowsay,
to be used in una monorepo demos.

Example:
```python
>>> from cowsay import say
>>> print(say("Hello!"))

┌───────┐
│Hello! │
└───────┘
      \
       \
         ^__^
         (oo)\___
         (__)\       )\/\
             ||----w |
             ||     ||
```

</details>

### cdk-fck-nat

A NAT Gateway instance construct built on the fck-nat AMI.

`pip install cdk-fck-nat` · installs (wheel) · licence: OSI Approved · rank 14751 · last release 2025-12-02 · [PyPI](https://pypi.org/project/cdk-fck-nat/) · [source](https://github.com/AndrewGuenther/cdk-fck-nat.git)

<details><summary>README extract</summary>

A CDK construct for deploying NAT Instances using fck-nat. The (f)easible (c)ost (k)onfigurable NAT!

* Overpaying for AWS Managed NAT Gateways? fck-nat.
* Want to use NAT instances and stay up-to-date with the latest security patches? fck-nat.
* Want to reuse your Bastion hosts as a NAT? fck-nat. ...

</details>

### crunch64

A library for handling common compression formats for N64 games

`pip install crunch64` · installs (wheel) · licence: not stated · rank 14776 · last release 2026-03-28 · [PyPI](https://pypi.org/project/crunch64/)

### cyrtranslit

Bi-directional Cyrillic transliteration. Transliterate Cyrillic script to Latin script and vice versa. Supports transliteration for Belarusian, Bulgarian, Greek, Montenegrin, Macedonian, Mongolian, Russian, Serbian, Tajik, and Ukrainian.

`pip install cyrtranslit` · installs (wheel) · licence: MIT License · rank 14779 · last release 2025-11-20 · [PyPI](https://pypi.org/project/cyrtranslit/)

<details><summary>README extract</summary>

A Python package for bi-directional transliteration of Cyrillic script to Latin script and vice versa.

By default, transliterates for the Serbian language. A language flag can be set in order to transliterate to and from Belarusian, Bulgarian, Greek, Montenegrin, Macedonian, Mongolian, Russian, Serbian, Tajik, and Ukrainian. ...

Example:
```python
>>> import cyrtranslit
>>> cyrtranslit.to_latin("ѝ је", "mk")
"i je"
>>> cyrtranslit.to_latin("нѐ сме", "mk")
"ne sme"
>>> cyrtranslit.to_cyrillic("i je", "mk")
"и је"
```

...

</details>

### covcheck

Code coverage validation

`pip install covcheck` · installs (wheel) · licence: Other/Proprietary License · rank 14815 · last release 2023-09-05 · [PyPI](https://pypi.org/project/covcheck/) · [source](https://github.com/HumeAI/covcheck)

<details><summary>README extract</summary>

Command-line tool for code coverage validation

`covcheck` is intended to be used in conjunction with coverage.py, which already has support for `pytest`, `unittest`, and `nosetest`. All you have to do is point `covcheck` to the `coverage.xml` file produced when running your tests. ...

Sections: covcheck, About

</details>

### chromedriver-py

chromedriver binaries for all platforms

`pip install chromedriver-py` · installs (wheel) · licence: Apache Software License · rank 14838 · last release 2026-11-04 · [PyPI](https://pypi.org/project/chromedriver-py/)

<details><summary>README extract</summary>

downloads and installs the latest chromedriver binary version for automated testing of webapps.
the installer supports linux, mac and windows operating systems.

this package is maintained by an automated update script on travis.
if a new chromedriver version is out, this package will automaticly get updated within a day.

Example:
```python
from selenium import webdriver
from chromedriver_py import binary_path # this will get you the path variable

svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)

# deprecated but works in older selenium versions
# driver = webdriver.Chrome(executable_path=binary_path)
driver.get("
...
```

Sections: chromedriver-py, usage, example

</details>

### codicodec

Encode and decode audio samples to/from continuous and discrete compressed representations!

`pip install codicodec` · installs (wheel) · licence: CC BY-NC 4.0 · rank 14865 · last release 2025-11-25 · [PyPI](https://pypi.org/project/codicodec/)

<details><summary>README extract</summary>

CoDiCodec is a generative neural audio Codec that highly compresses 44.1/48 kHz stereo audio into either Continuous or Discrete representations with SOTA reconstruction quality (as of Sep. 2025, see paper):
* Discrete tokens: at a bitrate of 2.38 kbit/s.
* Continuous latent vectors: at a ~11 Hz frame rate with 64 channels (128x compression). ...

Example:
```python
import librosa
import numpy as np
import IPython
from codicodec import EncoderDecoder

# Initialize the EncoderDecoder
encdec = EncoderDecoder()

# Load an example audio file (or use your own!)
audio_path = librosa.example('trumpet')
wv, sr = librosa.load(audio_path, sr=44100)  # Ensure 44.1kHz sample rate

# Encode the audio
...
```

...

</details>

### cryptocode

Python library used to encrypt and decrypt strings in the simplest possible way.

`pip install cryptocode` · installs (wheel) · licence: MIT License · rank 14903 · last release 2020-11-05 · [PyPI](https://pypi.org/project/cryptocode/)

<details><summary>README extract</summary>

Sections: Requirements, Basic usage, Example, Function to verify that the key is valid

</details>

### conda-lock

Lockfiles for conda

`pip install conda-lock` · installs (wheel) · licence: MIT · rank 14914 · last release 2026-11-03 · [PyPI](https://pypi.org/project/conda-lock/) · [docs](https://conda.github.io/conda-lock/) · [source](https://github.com/conda/conda-lock)

<details><summary>README extract</summary>

Conda lock is a lightweight library that can be used to generate fully reproducible lock files for conda
environments.

It does this by performing a conda solve for each platform you desire a lockfile for. ...

Features:
Conda `environment.yml` files are very useful for defining desired environments but there are times when we want to
be able to EXACTLY reproduce an environment by just installing and downloading the packages needed. ...

Sections: conda-lock, Why?, Basic usage, Pre 1.0 compatible usage (explicit per platform locks), Advanced usage, File naming, Compound specification, channel overrides, platform specification, default category, private pip repositories, --dev-dependencies/--no-dev-dependencies, --check-input-hash, --strip-auth, --auth and --auth-file

</details>

### checkmk-dev-tools

Checkmk DevOps tools

`pip install checkmk-dev-tools` · installs (wheel) · licence: not stated · rank 14915 · last release 2026-11-02 · [PyPI](https://pypi.org/project/checkmk-dev-tools/) · [source](https://github.com/Checkmk/checkmk-dev-tools)

<details><summary>README extract</summary>

Example:
```python
def buildData = [:];
params.each { paramKey, paramValue ->
    buildData[paramKey] = paramValue;
}

// === IMPORTANT ===
// use 'PROGRESS' at the begin of a job
// use 'currentBuild.result' at the closest possible end of a job
// buildData['build_status'] = 'PROGRESS';
// buildData['build_result'] = currentBuild.result;
// === IMPORTANT ===

...
```

Sections: Contained tools, General, Jenkins, InfluxDB, `ci-artifacts`, Usage, Await result, Download, Fetch, Info, Request, Validate, Todo, `job-resource-usage`

</details>

