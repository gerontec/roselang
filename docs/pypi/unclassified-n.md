# Unclassified / N

[Index](README.md) · 181 packages in this topic, by downloads.

### narwhals

Extremely lightweight compatibility layer between dataframe libraries

`pip install narwhals` · installs (wheel) · licence: MIT · rank 235 · last release 2026-10-27 · [PyPI](https://pypi.org/project/narwhals/) · [docs](https://narwhals-dev.github.io/narwhals/) · [source](https://github.com/narwhals-dev/narwhals)

<details><summary>README extract</summary>

Extremely lightweight and extensible compatibility layer between dataframe libraries!

- Full API support: cuDF, Modin, pandas, Polars, PyArrow.
- Lazy-only support: Dask, DuckDB, Ibis, PySpark, SQLFrame, Daft via the
 narwhals-daft plugin, and Apache DataFusion via the
 narwhals-datafusion plugin. ...

Features:
Coz they are so awesome.

Thanks to Olha Urdeichuk for the illustration!

Example:
```python
import narwhals as nw
from narwhals.typing import IntoDataFrameT, IntoLazyFrameT

def agnostic_function(
    df_native: IntoDataFrameT | IntoLazyFrameT,
) -> IntoDataFrameT | IntoLazyFrameT:
    return (
        nw.from_native(df_native)
        .with_columns(
            category=nw.when(nw.col("animal").str.contains("whale"))
...
```

...

</details>

### nbformat

The Jupyter Notebook format

`pip install nbformat` · installs (wheel) · licence: BSD License · rank 302 · last release 2026-08-17 · [PyPI](https://pypi.org/project/nbformat/) · [docs](https://nbformat.readthedocs.io/) · [source](https://github.com/jupyter/nbformat.git)

<details><summary>README extract</summary>

This package contains the base implementation of the Jupyter Notebook format,
and Python APIs for working with notebooks.

</details>

### nest-asyncio

Patch asyncio to allow nested event loops

`pip install nest-asyncio` · installs (wheel) · licence: BSD License · rank 309 · last release 2024-01-21 · [PyPI](https://pypi.org/project/nest-asyncio/)

<details><summary>README extract</summary>

By design asyncio does not allow
its event loop to be nested. This presents a practical problem:
When in an environment where the event loop is
already running it's impossible to run tasks and wait
for the result. Trying to do so will give the error
"`RuntimeError: This event loop is already running`". ...

Example:
```python
import nest_asyncio
nest_asyncio.apply()
```

Sections: Introduction, Usage

</details>

### nbclient

A client library for executing notebooks. Formerly nbconvert's ExecutePreprocessor.

`pip install nbclient` · installs (wheel) · licence: BSD License · rank 405 · last release 2026-06-05 · [PyPI](https://pypi.org/project/nbclient/) · [docs](https://nbclient.readthedocs.io) · [source](https://github.com/jupyter/nbclient)

<details><summary>README extract</summary>

NBClient lets you execute notebooks.

A client library for programmatic notebook execution, NBClient is a tool for running Jupyter Notebooks in
different execution contexts, including the command line.

To demo NBClient interactively, click this Binder badge to start the demo:

Sections: nbclient, Interactive Demo, Documentation, Origins, Relationship to JupyterClient, Our Copyright Policy

</details>

### nbconvert

Convert Jupyter Notebooks (.ipynb files) to other formats.

`pip install nbconvert` · installs (wheel) · licence: BSD License · rank 409 · last release 2026-10-12 · [PyPI](https://pypi.org/project/nbconvert/)

<details><summary>README extract</summary>

The nbconvert tool, `jupyter nbconvert`, converts notebooks to various other
formats via [Jinja] templates. The nbconvert tool allows you to convert an
`.ipynb` notebook file into various static formats including:

- HTML
- LaTeX
- PDF
- Reveal JS
- Markdown (md)
- ReStructured Text (rst)
- executable script

Sections: nbconvert, Jupyter Notebook Conversion, Usage, Example: Convert a notebook to HTML, Documentation, Jupyter Resources, Our Copyright Policy

</details>

### nexus-rpc

Nexus Python SDK

`pip install nexus-rpc` · installs (wheel) · licence: MIT · rank 538 · last release 2026-10-28 · [PyPI](https://pypi.org/project/nexus-rpc/)

<details><summary>README extract</summary>

⚠️ This SDK is currently at an experimental release stage. Backwards-incompatible changes are anticipated until a stable release is announced. ⚠️

Nexus is a synchronous RPC protocol. Arbitrary duration operations are modeled on top of
a set of pre-defined synchronous RPCs.

A Nexus caller calls a handler. ...

Example:
```python
from dataclasses import dataclass

import nexusrpc

@dataclass
class MyInput:
    name: str

@dataclass
class MyOutput:
    message: str

@nexusrpc.service
class MyNexusService:
    my_sync_operation: nexusrpc.Operation[MyInput, MyOutput]

@nexusrpc.handler.service_handler(service=MyNexusService)
class MyNexusServiceHandler:
...
```

Sections: Nexus Python SDK, What is Nexus?, Usage, Defining Nexus services and operations

</details>

### nest-asyncio2

Patch asyncio to allow nested event loops

`pip install nest-asyncio2` · installs (wheel) · licence: BSD License · rank 556 · last release 2026-10-07 · [PyPI](https://pypi.org/project/nest-asyncio2/)

<details><summary>README extract</summary>

By design asyncio does not allow
its event loop to be nested. This presents a practical problem:
When in an environment where the event loop is
already running it's impossible to run tasks and wait
for the result. Trying to do so will give the error
"`RuntimeError: This event loop is already running`". ...

Example:
```python
import nest_asyncio2
nest_asyncio2.apply()
```

Sections: nest-asyncio2, Introduction, Usage, Examples, aiohttp, Known issues, Leaked event loop, Comparison with `nest_asyncio`

</details>

### notebook

Jupyter Notebook - A web-based notebook environment for interactive computing

`pip install notebook` · installs (wheel) · licence: BSD License · rank 630 · last release 2026-11-06 · [PyPI](https://pypi.org/project/notebook/) · [docs](https://jupyter-notebook.readthedocs.io/) · [source](https://github.com/jupyter/notebook)

<details><summary>README extract</summary>

The Jupyter notebook is a web-based notebook environment for interactive
computing.

We maintain the two most recently released major versions of Jupyter Notebook,
Classic Notebook v6 and Notebook v7. Notebook v5 is no longer maintained.
All Notebook v5 users are strongly advised to upgrade to Classic Notebook v6 as soon as possible. ...

Sections: Jupyter Notebook, Maintained versions, Notebook v7, Classic Notebook v6, Usage - Running Jupyter notebook, Resources, Our Copyright Policy

</details>

### notebook-shim

A shim layer for notebook traits and config

`pip install notebook-shim` · installs (wheel) · licence: BSD License · rank 632 · last release 2024-02-14 · [PyPI](https://pypi.org/project/notebook-shim/)

<details><summary>README extract</summary>

This project provides a way for JupyterLab and other frontends to switch to Jupyter Server for their Python Web application backend.

Example:
```python
from notebook.notebookapp import NotebookApp

class MyApplication(NotebookApp):
```

Sections: Notebook Shim, Basic Usage, Usage

</details>

### nodejs-wheel-binaries

unoffical Node.js package

`pip install nodejs-wheel-binaries` · installs (wheel) · licence: MIT License · rank 822 · last release 2026-08-19 · [PyPI](https://pypi.org/project/nodejs-wheel-binaries/) · [source](https://github.com/njzjz/nodejs-wheel)

<details><summary>README extract</summary>

`nodejs-wheel` is an unofficial repository to distribute Node.js prebuilt wheels through PyPI using

*New in v20.13.0*: If you don't need command line interface (CLI), install only `nodejs-wheel-binaries`, which is a direct dependency of `nodejs-wheel`.

The package requires Python 3.7 and above. ...

Example:
```python
from nodejs_wheel import (
    node,
    npm,
    npx,
    # corepack: New in v22.13.1
    corepack,
)

return_code0 = node(["--version"])
return_code1 = npm(["--version"])
return_code2 = npx(["--version"])
# corepack: New in v22.13.1
return_code3 = corepack(["--version"])
```

Sections: Unofficial Node.js wheels, Available Builds, Usage, Command line, Run library module as a script, Python API, Other projects

</details>

### nemo-relay

Python bindings for the NeMo Relay agent runtime.

`pip install nemo-relay` · installs (wheel) · licence: Apache-2.0 · rank 1174 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nemo-relay/) · [docs](https://nvidia-nemo-relay.docs.buildwithfern.com/nemo-relay) · [source](https://github.com/NVIDIA/NeMo-Relay)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

`nemo-relay` is the NeMo Relay package for Python applications. ...

Features:
Use the Python binding for the following tasks:

- Own execution context in Python: Group agent, tool, and LLM work into
 one scope tree from Python application code. ...

Example:
```python
import nemo_relay

def on_event(event) -> None:
    print(f"{event.kind} {event.name}")

nemo_relay.subscribers.register("printer", on_event)

with nemo_relay.scope.scope("demo-agent", nemo_relay.ScopeType.Agent) as handle:
    nemo_relay.scope.event("initialized", handle=handle, data={"binding": "python"})

nemo_relay.subscribers.flush()
...
```

...

</details>

### nats-py

NATS client for Python

`pip install nats-py` · installs (wheel) · licence: Apache-2.0 · rank 1626 · last release 2026-09-16 · [PyPI](https://pypi.org/project/nats-py/)

<details><summary>README extract</summary>

An asyncio Python client for the NATS messaging system.

Example:
```python
import asyncio
import nats
from nats.errors import ConnectionClosedError, TimeoutError, NoServersError

async def main():
    # It is very likely that the demo server will see traffic from clients other than yours.
    # To avoid this, start your own locally and modify the example to use it.
    nc = await nats.connect("nats://demo.nats.io:4222")

...
```

Sections: NATS - Python3 Client for Asyncio, Getting started, JetStream, TLS, NKEYS and JWT User Credentials

</details>

### nvidia-cutlass-dsl-libs-base

NVIDIA CUTLASS Python DSL

`pip install nvidia-cutlass-dsl-libs-base` · installs (wheel) · licence: Other/Proprietary License · rank 1760 · last release 2026-10-16 · [PyPI](https://pypi.org/project/nvidia-cutlass-dsl-libs-base/) · [docs](https://github.com/NVIDIA/cutlass) · [source](https://github.com/NVIDIA/cutlass)

<details><summary>README extract</summary>

CUTLASS 4.x provides a Python native interfaces for writing high-performance CUDA kernels based on core CUTLASS and CuTe concepts without any performance compromises. This allows for a much smoother learning curve, orders of magnitude faster compile times, native integration with DL frameworks without writing glue code, and much more intuitive ...

</details>

### namex

A simple utility to separate the implementation of your Python package and its public API surface.

`pip install namex` · installs (wheel) · licence: not stated · rank 1793 · last release 2025-05-26 · [PyPI](https://pypi.org/project/namex/)

### nvidia-cutlass-dsl

NVIDIA CUTLASS Python DSL

`pip install nvidia-cutlass-dsl` · installs (wheel) · licence: Other/Proprietary License · rank 1870 · last release 2026-10-16 · [PyPI](https://pypi.org/project/nvidia-cutlass-dsl/) · [docs](https://github.com/NVIDIA/cutlass) · [source](https://github.com/NVIDIA/cutlass)

<details><summary>README extract</summary>

CUTLASS 4.x provides a Python native interfaces for writing high-performance CUDA kernels based on core CUTLASS and CuTe concepts without any performance compromises. This allows for a much smoother learning curve, orders of magnitude faster compile times, native integration with DL frameworks without writing glue code, and much more intuitive ...

</details>

### notion-client

Python client for the official Notion API

`pip install notion-client` · installs (wheel) · licence: MIT License · rank 2086 · last release 2026-05-12 · [PyPI](https://pypi.org/project/notion-client/)

<details><summary>README extract</summary>

**_notion-sdk-py is a simple and easy to use client library for the official
Notion API.**

It is meant to be a Python version of the reference JavaScript SDK,
so usage should be very similar between both. 😊 (If not, please open an issue
or PR!)

Example:
```python
import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])
```

Sections: Usage, Handling errors, Logging, Client options, Automatic retries, Constants, Full API responses, Utility functions, `iterate_paginated_api(function, **kwargs)`, `collect_paginated_api(function, **kwargs)`, Custom requests, Requirements and compatibility, Getting help

</details>

### nvidia-cutlass-dsl-libs-cu12

NVIDIA CUTLASS Python DSL

`pip install nvidia-cutlass-dsl-libs-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 2104 · last release 2026-10-16 · [PyPI](https://pypi.org/project/nvidia-cutlass-dsl-libs-cu12/) · [docs](https://github.com/NVIDIA/cutlass) · [source](https://github.com/NVIDIA/cutlass)

<details><summary>README extract</summary>

CUTLASS 4.x provides a Python native interfaces for writing high-performance CUDA kernels based on core CUTLASS and CuTe concepts without any performance compromises. This allows for a much smoother learning curve, orders of magnitude faster compile times, native integration with DL frameworks without writing glue code, and much more intuitive ...

</details>

### nvidia-cutlass-dsl-libs-cu13

NVIDIA CUTLASS Python DSL

`pip install nvidia-cutlass-dsl-libs-cu13` · installs (wheel) · licence: Other/Proprietary License · rank 2160 · last release 2026-10-16 · [PyPI](https://pypi.org/project/nvidia-cutlass-dsl-libs-cu13/) · [docs](https://github.com/NVIDIA/cutlass) · [source](https://github.com/NVIDIA/cutlass)

<details><summary>README extract</summary>

CUTLASS 4.x provides a Python native interfaces for writing high-performance CUDA kernels based on core CUTLASS and CuTe concepts without any performance compromises. This allows for a much smoother learning curve, orders of magnitude faster compile times, native integration with DL frameworks without writing glue code, and much more intuitive ...

</details>

### numpy-typing-compat

Static typing compatibility layer for older versions of NumPy

`pip install numpy-typing-compat` · installs (wheel) · licence: BSD-3-Clause · rank 2164 · last release 2026-06-02 · [PyPI](https://pypi.org/project/numpy-typing-compat/) · [source](https://github.com/jorenham/numpy-typing-compat)

<details><summary>README extract</summary>

[][RELEASES]
[][CF]

[][NP]

Features:
This package provides version-specific boolean constants that allow library authors to
write NumPy-version-dependent static type annotations. ...

Sections: `numpy-typing-compat`, Overview, Reference, `StringDType`, `ABCPolyBase`, `LiteralTrue` and `LiteralFalse`, Version constants

</details>

### nvidia-cutlass-dsl-libs-core

NVIDIA CUTLASS Python DSL

`pip install nvidia-cutlass-dsl-libs-core` · installs (wheel) · licence: Other/Proprietary License · rank 2172 · last release 2026-10-16 · [PyPI](https://pypi.org/project/nvidia-cutlass-dsl-libs-core/) · [docs](https://github.com/NVIDIA/cutlass) · [source](https://github.com/NVIDIA/cutlass)

<details><summary>README extract</summary>

CUTLASS 4.x provides a Python native interfaces for writing high-performance CUDA kernels based on core CUTLASS and CuTe concepts without any performance compromises. This allows for a much smoother learning curve, orders of magnitude faster compile times, native integration with DL frameworks without writing glue code, and much more intuitive ...

</details>

### ndindex

A Python library for manipulating indices of ndarrays.

`pip install ndindex` · installs (wheel) · licence: MIT · rank 2428 · last release 2025-11-19 · [PyPI](https://pypi.org/project/ndindex/)

<details><summary>README extract</summary>

A Python library for manipulating indices of ndarrays.

The documentation for ndindex can be found at

ndindex is a library that allows representing and manipulating objects that
can be valid indices to numpy arrays, i.e., slices, integers, ellipses,
None, integer and boolean arrays, and tuples thereof. The goals of the library
are ...

Example:
```python
>>> from ndindex import *
>>> Slice(-2, 10, 3).reduce()
Slice(-2, 10, 2)
>>> Slice(-2, 10, 3).reduce(5)
Slice(3, 4, 1)
```

Sections: ndindex, Examples

</details>

### nab-index

PyPI Simple-API client and on-disk cache for nab

`pip install nab-index` · installs (wheel) · licence: MIT · rank 2857 · last release 2026-11-08 · [PyPI](https://pypi.org/project/nab-index/) · [docs](https://nab.readthedocs.io/) · [source](https://github.com/notatallshaw/nab)

<details><summary>README extract</summary>

Fetch package listings and metadata from Python package indexes. This package implements the PyPI
Simple API and caches responses on disk for `nab-project`
and `nab`.

It provides:

- An asynchronous HTTP interface with `urllib3` by default and optional `httpx` and `httpx2`
 backends.
- A Simple-API client with JSON and HTML decoders. ...

Sections: nab-index, When to use it

</details>

### nab-resolver

Generic PubGrub dependency-resolver core

`pip install nab-resolver` · installs (wheel) · licence: MIT · rank 2860 · last release 2026-11-08 · [PyPI](https://pypi.org/project/nab-resolver/) · [docs](https://nab.readthedocs.io/) · [source](https://github.com/notatallshaw/nab)

<details><summary>README extract</summary>

Find a combination of package versions that satisfies their dependency constraints, using the
PubGrub algorithm. A `ResolverProvider` supplies the package rules, so the solver needs no
Python-specific knowledge. The Python provider lives in
`nab-provider` and the user-facing CLI in
`nab`. ...

Example:
```python
trial = Resolver(make_provider())
pins = trial.try_resolve_preferred(requirements, preferred, constraints)
if pins is None:
    pins = Resolver(make_provider()).resolve(requirements, constraints)
```

Sections: nab-resolver, When to use it, The public API, Checking preferred versions

</details>

### nab-provider

IO-free resolution core for nab

`pip install nab-provider` · installs (wheel) · licence: MIT · rank 2898 · last release 2026-11-08 · [PyPI](https://pypi.org/project/nab-provider/) · [docs](https://nab.readthedocs.io/) · [source](https://github.com/notatallshaw/nab)

<details><summary>README extract</summary>

Apply Python packaging rules during dependency resolution. This package supplies candidate versions
and their dependency constraints to `nab-resolver`,
including environment markers and build, distribution, and VCS policies.

It performs no networking, file access, or subprocess calls. ...

Example:
```python
from nab_provider.tags import PlatformSpec
from nab_provider.value import replace

platform = PlatformSpec("linux_x86_64")
platform = replace(platform, runs_on_libc=(2, 28))
```

Sections: nab-provider, When to use it, Wheel tags, Value records

</details>

### nab-project

Index-backed provider, lockfile emitter, and downloader for nab

`pip install nab-project` · installs (wheel) · licence: MIT · rank 2899 · last release 2026-11-08 · [PyPI](https://pypi.org/project/nab-project/) · [docs](https://nab.readthedocs.io/) · [source](https://github.com/notatallshaw/nab)

<details><summary>README extract</summary>

`nab-project` connects `nab-provider` to networking and
files. It supplies the provider's I/O through `nab-index`,
and adds the resolve orchestration, workspace discovery, the PEP 517 build path, the lockfile
emitter and the downloader. ...

Sections: nab-project, When to use it

</details>

### nab-markersets

PEP 508 marker algebra: markers as sets of environments

`pip install nab-markersets` · installs (wheel) · licence: MIT · rank 2927 · last release 2026-11-08 · [PyPI](https://pypi.org/project/nab-markersets/) · [docs](https://nab.readthedocs.io/) · [source](https://github.com/notatallshaw/nab)

<details><summary>README extract</summary>

A dependency marker is a condition such as `python_version < "3.11"` that controls when a
requirement applies. This package compares PEP 508 markers as sets of environments. `packaging`
evaluates a marker against one environment. `nab-markersets` checks whether markers overlap, whether
one implies another, and whether a marker is contradictory. ...

Example:
```python
>>> from nab_markersets.markersets import MarkerSet
>>> old = MarkerSet.from_marker('python_version < "3.11"')
>>> new = MarkerSet.from_marker('python_version >= "3.12"')
>>> old.is_disjoint(new)
True
```

Sections: nab-markersets, When to use it, The public API

</details>

### nab

PubGrub-based dependency resolver for Python packages

`pip install nab` · installs (wheel) · licence: MIT · rank 2968 · last release 2026-11-08 · [PyPI](https://pypi.org/project/nab/) · [docs](https://nab.readthedocs.io/en/stable/) · [source](https://github.com/notatallshaw/nab)

<details><summary>README extract</summary>

nab generates universal lockfiles for Python projects. Declare your target Python versions and
platforms in `pyproject.toml`, then write one PEP 751 `pylock.toml` covering them. An installer such
as pip installs the dependencies selected for its environment from that file.

nab is written in Python and is experimental. ...

Sections: nab, Example project, Safer defaults, Soundness, More features, Policy overrides, Allow a reviewed update during a cooldown, Use an index without upload times, Performance, Universal lock benchmark, Libraries

</details>

### nbclassic

Jupyter Notebook as a Jupyter Server extension.

`pip install nbclassic` · installs (wheel) · licence: BSD License · rank 3199 · last release 2025-09-16 · [PyPI](https://pypi.org/project/nbclassic/)

<details><summary>README extract</summary>

*Read the full [NbClassic User Manual here]!*

The Jupyter Notebook is [evolving to bring you big new features], but it
will also break backwards compatibility with many classic Jupyter Notebook
extensions and customizations. ...

Sections: The Classic Jupyter Notebook as a Jupyter Server Extension, How does it work?, Basic Usage

</details>

### nebius

Nebius Python SDK

`pip install nebius` · installs (wheel) · licence: not stated · rank 3364 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nebius/)

<details><summary>README extract</summary>

The Nebius Python® SDK is a client library for
Nebius AI Cloud services. It uses gRPC and supports all
APIs in the Nebius API repository. Use the SDK
to authenticate, manage resources, and communicate with Nebius services. ...

Example:
```python
def report_loop_exception(loop, context):
    record_redacted_fields(context)
    loop.default_exception_handler(context)

sdk = SDK(loop_exception_handler=report_loop_exception)
```

Sections: Nebius Python® SDK, Full documentation and reference, Migration from 0.4.x to 0.5.x, Runtime ownership and shutdown, Custom extensions and data, RPC and stream behavior, Cross-loop handles, Migration from 0.3.x to 0.4.x, Migration from 0.2.x to 0.3.x, Example, How-to, Initialize, Initialize with an IAM token, Initialize using CLI config

</details>

### ndjson

JsonDecoder for ndjson

`pip install ndjson` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 3503 · last release 2020-02-25 · [PyPI](https://pypi.org/project/ndjson/)

_README extract left out: share-alike licence._

### node-semver

port of node-semver

`pip install node-semver` · installs (wheel) · licence: mit · rank 3871 · last release 2026-06-23 · [PyPI](https://pypi.org/project/node-semver/)

<details><summary>README extract</summary>

python version of node-semver

Example:
```python
from nodesemver import max_satisfying

versions = ['1.2.3', '1.2.4', '1.2.5', '1.2.6', '2.0.1']
range = '~1.2.3'
assert max_satisfying(versions, range, loose=False) == '1.2.6'

versions = ['1.1.0', '1.2.0', '1.2.1', '1.3.0', '2.0.0b1', '2.0.0b2', '2.0.0b3', '2.0.0', '2.1.0']
range = '~2.0.0'
...
```

Sections: node-semver, examples

</details>

### nvshmem4py-cu13

Python bindings for NVSHMEM

`pip install nvshmem4py-cu13` · installs (wheel) · licence: not stated · rank 4123 · last release 2026-10-15 · [PyPI](https://pypi.org/project/nvshmem4py-cu13/)

<details><summary>README extract</summary>

NVSHMEM4Py exposes NVSHMEM host, device, and on-stream interfaces to Python, with interoperability
for CUDA Python, Numba, PyTorch, CuPy, and CuTe DSL.

Sections: NVSHMEM4Py, Quick Start, Building Wheels, Examples

</details>

### ntc-templates

TextFSM Templates for Network Devices, and Python wrapper for TextFSM's CliTable.

`pip install ntc-templates` · installs (wheel) · licence: Apache Software License · rank 4127 · last release 2026-09-14 · [PyPI](https://pypi.org/project/ntc-templates/) · [docs](https://ntc-templates.readthedocs.io) · [source](https://github.com/networktocode/ntc-templates)

<details><summary>README extract</summary>

Features:
Repository of TextFSM Templates for Network Devices, and Python wrapper for TextFSM's CliTable. TextFSM is a tool to help make parsing cli commands more manageable.

Sections: NTC Templates, Overview, Documentation, Questions, Additional Automation Resources

</details>

### netmiko

Multi-vendor library to simplify legacy CLI connections to network devices

`pip install netmiko` · installs (wheel) · licence: MIT · rank 4329 · last release 2026-09-21 · [PyPI](https://pypi.org/project/netmiko/) · [source](https://github.com/ktbyers/netmiko)

<details><summary>README extract</summary>

Multi-vendor library to simplify CLI connections to network devices

Features:
Network automation to screen-scraping devices is primarily concerned with gathering output from show commands and with making configuration changes. ...

Example:
```python
from netmiko import ConnectHandler

cisco_881 = {
    "device_type": "cisco_ios",
    "host": "10.10.10.10",
    "username": "test",
    "password": "password",
    "port": 8022,  # optional, defaults to 22
    "secret": "secret",  # optional, defaults to ''
}
```

Sections: Netmiko, Why Netmiko?, Getting Started, Examples, API-Documentation, Common Issues/FAQ, Tutorials, Create a dictionary representing the device., Execute show commands., Questions/Discussion, #

</details>

### nkeys

A public-key signature system based on Ed25519 for the NATS ecosystem.

`pip install nkeys` · installs from source (sdist only) · licence: Apache Software License · rank 4506 · last release 2024-09-11 · [PyPI](https://pypi.org/project/nkeys/)

<details><summary>README extract</summary>

A public-key signature system based on Ed25519 for the NATS ecosystem.

The NATS ecosystem will be moving to Ed25519 keys for identity, authentication and authorization for entities such as Accounts, Users, Servers and Clusters.

Ed25519 is fast and resistant to side channel attacks. ...

Example:
```python
import nkeys
import os

# Create an NKEYS KeyPair from a seed file.
user = None
with open("user.nkey", 'rb', buffering=0) as f:

  # We compute the size of the file to allocate the required
  # bytearray size in order to have control over the memory
  # and be able to wipe it once the keys are not needed anymore.
...
```

Sections: NKEYS for Python3, About, Basic API Usage

</details>

### numpyro

Probabilistic programming with NumPy powered by JAX for autograd and JIT compilation to GPU/TPU/CPU.

`pip install numpyro` · installs (wheel) · licence: Apache Software License · rank 4590 · last release 2026-09-18 · [PyPI](https://pypi.org/project/numpyro/)

<details><summary>README extract</summary>

Installation •
Documentation and Tutorials •
Forum

NumPyro is a lightweight probabilistic programming library that provides a NumPy backend for Pyro. We rely on JAX for automatic differentiation and JIT compilation to GPU / CPU. NumPyro is under active development, so beware of brittleness, bugs, and changes to the API as the design evolves. ...

Features:
We provide an overview of most of the inference algorithms supported by NumPyro and offer some guidelines about which inference algorithms may be appropriate for different classes of models.

Example:
```python
>>> import numpy as np

>>> J = 8
>>> y = np.array([28.0, 8.0, -3.0, 7.0, -1.0, 1.0, 18.0, 12.0])
>>> sigma = np.array([15.0, 10.0, 16.0, 11.0, 9.0, 11.0, 10.0, 18.0])
```

...

</details>

### ntlm-auth

Creates NTLM authentication structures

`pip install ntlm-auth` · installs (wheel) · licence: MIT License · rank 4591 · last release 2020-06-16 · [PyPI](https://pypi.org/project/ntlm-auth/)

<details><summary>README extract</summary>

\ \

This library handles the low-level details of NTLM authentication for
use in authenticating with a service that uses NTLM. It will create and
parse the 3 different message types in the order required and produce a
base64 encoded value that can be attached to the HTTP header. ...

Features:
- LM, NTLM and NTLMv2 authentication
- NTLM1 and NTLM2 extended session security
- Set the The NTLM Compatibility level when sending messages
- Channel Binding Tokens support, need to pass in the SHA256 hash of
 the certificate for it to work ...

Example:
```python
import socket

from ntlm_auth.ntlm import NtlmContext

username = 'User'
password = 'Password'
domain = 'Domain' # Can be blank if you are not in a domain
...

</details>

### number-parser

parse numbers written in natural language

`pip install number-parser` · installs (wheel) · licence: BSD License · rank 4716 · last release 2023-03-28 · [PyPI](https://pypi.org/project/number-parser/)

<details><summary>README extract</summary>

`number-parser` is a simple library that allows you to convert numbers written in the natural
language to it's equivalent numeric forms. It currently supports cardinal numbers in the following
languages - English, Hindi, Spanish, Ukrainian and Russian and ordinal numbers in English.

Sections: number-parser, Usage, Converting numbers in-place, Parsing a number, Parsing an ordinal, Parsing a fraction, Changes, 0.3.2 (2023-03-28), 0.3.1 (2023-03-22), 0.3.0 (2022-10-20), 0.2.1 (2020-08-25), 0.2.0 (2020-08-18), 0.1.0 (2020-07-30)

</details>

### nixl-cu13

NIXL Python API

`pip install nixl-cu13` · installs (wheel) · licence: MIT AND Apache-2.0 · rank 5206 · last release 2026-10-29 · [PyPI](https://pypi.org/project/nixl-cu13/)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

NVIDIA Inference Xfer Library (NIXL) is targeted for accelerating point to point communications in AI inference frameworks such as NVIDIA Dynamo, while providing an abstraction over various types of memory ...

Sections: NVIDIA Inference Xfer Library (NIXL), Documentation and Resources, Pre-build Distributions, PyPI Wheel, Prerequisites for source build (Linux), Ubuntu, Fedora, Python, UCX, ETCD (Optional), ETCD Server and Client, ETCD CPP API, Additional plugins, Getting started

</details>

### names

Generate random names

`pip install names` · installs from source (sdist only) · licence: MIT License · rank 5480 · last release 2013-05-14 · [PyPI](https://pypi.org/project/names/)

<details><summary>README extract</summary>

Random name generator

Example:
```python
>>> import names
>>> names.get_full_name()
u'Patricia Halford'
>>> names.get_full_name(gender='male')
u'Patrick Keating'
>>> names.get_first_name()
'Bernard'
>>> names.get_first_name(gender='female')
'Christina'
>>> names.get_last_name()
'Szczepanek'
```

Sections: names, Usage, Command Line Usage, Python Package Usage, Changes, 0.3.0 (2013-05-14), 0.2 (2013-02-17), Hacking and Pull Requests, Running the tests

</details>

### nixl

NIXL Python API meta package for CUDA variants

`pip install nixl` · installs (wheel) · licence: MIT AND Apache-2.0 · rank 5526 · last release 2026-10-29 · [PyPI](https://pypi.org/project/nixl/)

<details><summary>README extract</summary>

This is a *meta package*. The PyPI distribution installs both the CUDA 12
and CUDA 13 backends, and the correct one is selected automatically at
runtime based on the CUDA version reported by PyTorch. Source builds install
a single backend unless built with `-Drelease_wheel=true`. ...

</details>

### nemoguardrails

NeMo Guardrails is an open-source toolkit for easily adding programmable guardrails to LLM-based conversational systems.

`pip install nemoguardrails` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 5570 · last release 2026-09-16 · [PyPI](https://pypi.org/project/nemoguardrails/) · [docs](https://docs.nvidia.com/nemo/guardrails/) · [source](https://github.com/NVIDIA-NeMo/Guardrails)

<details><summary>README extract</summary>

> LATEST RELEASE / DEVELOPMENT VERSION: The develop branch tracks the latest top of tree development. The latest released version is 0.24.1.

✨✨✨

📌 The official NeMo Guardrails library documentation is available at docs.nvidia.com/nemo/guardrails.

✨✨✨ ...

Features:
The NeMo Guardrails library enables developers building LLM-based applications to add programmable guardrails between the application code and the LLM.

Key benefits of adding *programmable guardrails* include: ...

Example:
```python
from nemoguardrails import LLMRails, RailsConfig

# Load a guardrails configuration from the specified path.
config = RailsConfig.from_path("PATH/TO/CONFIG")
rails = LLMRails(config)

completion = rails.generate(
    messages=[{"role": "user", "content": "Hello world!"}]
)
```

...

</details>

### nplusone

Detecting the n+1 queries problem in Python

`pip install nplusone` · installs (wheel) · licence: Copyright 2016 Joshua Carp · rank 5590 · last release 2018-05-21 · [PyPI](https://pypi.org/project/nplusone/)

<details><summary>README extract</summary>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit ...

</details>

### nbmake

Pytest plugin for testing notebooks

`pip install nbmake` · installs (wheel) · licence: Apache-2.0 · rank 5722 · last release 2024-12-23 · [PyPI](https://pypi.org/project/nbmake/)

<details><summary>README extract</summary>

What? Pytest plugin for testing and releasing notebook documentation

Why? To raise the quality of scientific material through better automation

Who is this for? Research/Machine Learning Software Engineers who maintain packages/teaching materials with documentation written in notebooks.

1. ...

Sections: nbmake, Functionality, Quick Start, Configure Cell Timeouts, Allow Errors For a Whole Notebook, Allow a Cell to Throw an Exception, Ignore a Code Cell, Add Missing Jupyter Kernel to Your CI Environment, Parallelisation, Build Jupyter Books Faster, Find missing imports in a directory of failing notebooks, Run test logic after a cell executes, Advice on Usage, Pre-commit

</details>

### nothing

a simple package that does nothing

`pip install nothing` · installs (wheel) · licence: MIT License · rank 5735 · last release 2015-12-25 · [PyPI](https://pypi.org/project/nothing/)

### nixl-cu12

NIXL Python API

`pip install nixl-cu12` · installs (wheel) · licence: MIT AND Apache-2.0 · rank 5754 · last release 2026-10-29 · [PyPI](https://pypi.org/project/nixl-cu12/)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

NVIDIA Inference Xfer Library (NIXL) is targeted for accelerating point to point communications in AI inference frameworks such as NVIDIA Dynamo, while providing an abstraction over various types of memory ...

Sections: NVIDIA Inference Xfer Library (NIXL), Documentation and Resources, Pre-build Distributions, PyPI Wheel, Prerequisites for source build (Linux), Ubuntu, Fedora, Python, UCX, ETCD (Optional), ETCD Server and Client, ETCD CPP API, Additional plugins, Getting started

</details>

### nylas

Python bindings for the Nylas API platform.

`pip install nylas` · installs (wheel) · licence: MIT · rank 5923 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nylas/) · [source](https://github.com/nylas/nylas-python)

<details><summary>README extract</summary>

The official Python SDK for Nylas — the infrastructure that powers communications

 📖 SDK Guide ·
 📚 API Reference ·
 🚀 Sign up ·
 💡 Samples ·
 💬 Forum

The official Python SDK for Nylas — the infrastructure that powers communications. Integrate with Gmail, Microsoft, IMAP, Zoom, and 250+ email, calendar, and meeting providers in 5 minutes. ...

Example:
```python
import os
from nylas import Client

nylas = Client(
    api_key=os.environ["NYLAS_API_KEY"],
    api_uri=os.environ.get("NYLAS_API_URI", "
    timeout=30,  # optional, in seconds
)
```

Sections: Nylas Python SDK, Get started, ⚡️ Usage, Error handling, Debugging, 💡 Examples, 🤖 AI agents, 📚 Reference, ✨ Upgrading, 🔗 Other Nylas SDKs

</details>

### newton-usd-schemas

OpenUSD schema definitions for the Newton physics engine

`pip install newton-usd-schemas` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 5927 · last release 2026-10-15 · [PyPI](https://pypi.org/project/newton-usd-schemas/) · [source](https://github.com/newton-physics/newton-usd-schemas)

<details><summary>README extract</summary>

Features:
Newton USD schemas provide extensions to OpenUSD's UsdPhysics specification, allowing USD layers to configure the Newton runtime data model. ...

Example:
```python
import newton_usd_schemas  # this registers the schema
from pxr import Usd, UsdPhysics

stage: Usd.Stage = Usd.Stage.CreateInMemory()

# create a UsdPhysics.Scene and set gravity
scene: UsdPhysics.Scene = UsdPhysics.Scene.Define(stage, "/scene")
scene.GetGravityMagnitudeAttr().Set(9.81)

# apply a Newton schema and set some of its attributes
...
```

Sections: newton-usd-schemas, Overview, Get Started, Design Principles, References

</details>

### nodejs-wheel

unoffical Node.js package

`pip install nodejs-wheel` · installs (wheel) · licence: not stated · rank 5968 · last release 2026-10-29 · [PyPI](https://pypi.org/project/nodejs-wheel/) · [source](https://github.com/njzjz/nodejs-wheel)

<details><summary>README extract</summary>

`nodejs-wheel` is an unofficial repository to distribute Node.js prebuilt wheels through PyPI using

*New in v20.13.0*: If you don't need command line interface (CLI), install only `nodejs-wheel-binaries`, which is a direct dependency of `nodejs-wheel`.

The package requires Python 3.7 and above. ...

Example:
```python
from nodejs_wheel import (
    node,
    npm,
    npx,
    # corepack: New in v22.13.1
    corepack,
)

return_code0 = node(["--version"])
return_code1 = npm(["--version"])
return_code2 = npx(["--version"])
# corepack: New in v22.13.1
return_code3 = corepack(["--version"])
```

Sections: Unofficial Node.js wheels, Available Builds, Usage, Command line, Run library module as a script, Python API, Other projects

</details>

### newspaper3k

Simplified python article discovery & extraction.

`pip install newspaper3k` · installs (wheel) · licence: MIT · rank 6043 · last release 2018-09-28 · [PyPI](https://pypi.org/project/newspaper3k/)

<details><summary>README extract</summary>

Inspired by requests for its simplicity and powered by lxml for its speed:

 "Newspaper is an amazing python library for extracting & curating articles."
 -- tweeted by Kenneth Reitz, Author of requests

 "Newspaper delivers Instapaper style article extraction." -- The Changelog ...

Features:
- Multi-threaded article download framework
- News url identification
- Text extraction from html
- Top image extraction from html
- All image extraction from html
- Keyword extraction from text
- Summary extraction from text ...

Example:
```python
>>> from newspaper import Article

>>> url = '
>>> article = Article(url)
```

Sections: Newspaper3k: Article scraping & curation, A Glance, Documentation, Features, Get it now, Demo

</details>

### numba-cuda

CUDA target for Numba

`pip install numba-cuda` · installs (wheel) · licence: BSD-2-Clause · rank 6197 · last release 2026-07-03 · [PyPI](https://pypi.org/project/numba-cuda/) · [docs](https://nvidia.github.io/numba-cuda/) · [source](https://github.com/NVIDIA/numba-cuda)

<details><summary>README extract</summary>

The CUDA target for Numba. Please visit the official
documentation to get started!

Numba-CUDA is in maintenance mode. Moving forward, we intend to support only
security issues and critical bug fixes through the lifetime of CUDA 13. ...

Example:
```python
python -c "from numba import cuda; print(cuda.file)"
```

Sections: Numba CUDA Target, Maintenance notice, Running tests

</details>

### nova-act

A Python SDK for Amazon Nova Act.

`pip install nova-act` · installs (wheel) · licence: Apache-2.0 · rank 6333 · last release 2026-04-30 · [PyPI](https://pypi.org/project/nova-act/)

<details><summary>README extract</summary>

A Python SDK for Amazon Nova Act.

Amazon Nova Act is available as a new AWS service to build and manage fleets of reliable AI agents for automating production UI workflows at scale. Nova Act completes repetitive UI workflows in the browser and escalates to a human supervisor when appropriate. ...

Example:
```python
from nova_act import NovaAct

with NovaAct(starting_page=" as nova:
    nova.act("Find flights from Boston to Wolf on Feb 22nd")
```

Sections: Nova Act SDK, Pre-requisites, Set Up, Quick Set Up with IDE Extension, Authentication, API Key Authentication, IAM-based Authentication, Quick Start, Script mode, Interactive mode, Async mode, Samples, How to prompt act(), Workflows

</details>

### nested-lookup

Python functions for working with deeply nested documents (lists and dicts)

`pip install nested-lookup` · installs from source (sdist only) · licence: Public Domain · rank 6420 · last release 2022-07-06 · [PyPI](https://pypi.org/project/nested-lookup/)

<details><summary>README extract</summary>

Make working with JSON, YAML, and XML document responses fun again!

The `nested_lookup` package provides many Python functions for working with deeply nested documents.
A document in this case is a a mixture of Python dictionary and list objects typically derived from YAML or JSON. ...

Example:
```python
>>> document = [ { 'taco' : 42 } , { 'salsa' : [ { 'burrito' : { 'taco' : 69 } } ] } ]
```

Sections: nested_lookup, quick tutorial, longer tutorial, nested_alter tutorial, misc

</details>

### nncf

Neural Networks Compression Framework

`pip install nncf` · installs (wheel) · licence: Apache-2.0 · rank 6504 · last release 2026-09-17 · [PyPI](https://pypi.org/project/nncf/)

<details><summary>README extract</summary>

Neural Network Compression Framework (NNCF) provides a suite of post-training and training-time algorithms for
optimizing inference of neural networks in OpenVINO™ with a minimal accuracy drop.

NNCF is designed to work with models from PyTorch,
TorchFX,
ONNX and OpenVINO™. ...

Sections: Neural Network Compression Framework (NNCF), Key Features, Post-Training Compression Algorithms, Training-Time Compression Algorithms, Third-party Repository Integration, Used by, NNCF Compressed Model Zoo, Citing, Telemetry

</details>

### nvidia-riva-client

Python implementation of the Riva Client API

`pip install nvidia-riva-client` · installs (wheel) · licence: MIT · rank 6638 · last release 2026-11-06 · [PyPI](https://pypi.org/project/nvidia-riva-client/)

<details><summary>README extract</summary>

NVIDIA Riva is a GPU-accelerated SDK for building Speech AI applications that are customized for your use
case and deliver real-time performance. This repo provides performant client example command-line clients.

- `riva.client.ASRService` is a class for speech recognition,
- `riva.client.TTSService` is a class for speech synthesis, ...

Sections: NVIDIA Riva Clients, Main API, CLI interface, Before using microphone and audio output devices on Unix, Usage, Server, CLI, ASR, NLP, TTS, API, Documentation

</details>

### ngcsdk

NVIDIA GPU Cloud SDK

`pip install ngcsdk` · installs (wheel) · licence: Apache-2.0 · rank 6678 · last release 2026-10-01 · [PyPI](https://pypi.org/project/ngcsdk/) · [docs](https://docs.ngc.nvidia.com/sdk/)

<details><summary>README extract</summary>

The NVIDIA NGC software development kit to interact and develop Python utilities and applications to integrate with the NVIDIA GPU Cloud.

 Python version >= 3.9

Example:
```python
from ngcsdk import Client

clt = Client()

clt.configure(api_key='****NkMQ', org_name='nvidia', team_name='no-team')
Validating configuration...
Successfully validated configuration.

clt.current_config()
[{'key': 'apikey', 'value': '****NkMQ', 'source': 'user settings'},
 {'key': 'format_type', 'value': 'ascii', 'source': 'user settings'},
...
```

Sections: NGC-SDK, Prerequisites, Extras, Creating and configuring NGC SDK client, Debugging, Output

</details>

### neo4j-graphrag

Python package to allow easy integration to Neo4j's GraphRAG features

`pip install neo4j-graphrag` · installs (wheel) · licence: Apache License, Version 2.0 · rank 6905 · last release 2026-10-28 · [PyPI](https://pypi.org/project/neo4j-graphrag/) · [source](https://github.com/neo4j/neo4j-graphrag-python)

<details><summary>README extract</summary>

The official Neo4j GraphRAG package for Python enables developers to build graph retrieval augmented generation (GraphRAG) applications using the power of Neo4j and Python.
As a first-party library, it offers a robust, feature-rich, and high-performance solution, with the added assurance of long-term support and maintenance directly from Neo4j. ...

Example:
```python
import asyncio

from neo4j import GraphDatabase
from neo4j_graphrag.embeddings import OpenAIEmbeddings
from neo4j_graphrag.experimental.pipeline.kg_builder import SimpleKGPipeline
from neo4j_graphrag.llm import OpenAILLM

NEO4J_URI = "neo4j://localhost:7687"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "password"

# Connect to the Neo4j database
...
```

...

</details>

### notifiers

The easy way to send notifications

`pip install notifiers` · installs (wheel) · licence: MIT · rank 7061 · last release 2026-10-10 · [PyPI](https://pypi.org/project/notifiers/) · [docs](https://notifiers.readthedocs.io/en/latest/) · [source](https://github.com/liiight/notifiers)

<details><summary>README extract</summary>

See changelog for recent changes

Got an app or service, and you want to enable your users to use notifications with their provider of choice? Working on a script and you want to receive notification based on its output? You don't need to implement a solution yourself, or use individual provider libs. ...

Example:
```python
>>> from notifiers import get_notifier
>>> p = get_notifier('pushover')
>>> p.required
{'required': ['user', 'message', 'token']}
>>> p.notify(user='foo', token='bar', message='test')
<Response,provider=Pushover,status=Success, errors=None>
```

Sections: Advantages, Basic Usage, From CLI, As a logger, Mentions, Road map

</details>

### notify_py

Cross-platform desktop notification library for Python

`pip install notify_py` · installs (wheel) · licence: MIT License · rank 7224 · last release 2024-06-05 · [PyPI](https://pypi.org/project/notify_py/) · [docs](https://github.com/ms7m/notify-py) · [source](https://github.com/ms7m/notify-py)

<details><summary>README extract</summary>

Cross platform desktop notifications for Python scripts and applications.

You can read the docs on this Git's Wiki, or here

Example:
```python
from notifypy import Notify

notification = Notify()
notification.title = "Cool Title"
notification.message = "Even cooler message."
notification.send()
```

Sections: notify.py, Docs, Usage, CLI, Important Caveats, Windows Specific., Inspiration and Special Thanks, Setting Up Environment

</details>

### nequix

Nequix source code

`pip install nequix` · installs (wheel) · licence: not stated · rank 7274 · last release 2026-03-17 · [PyPI](https://pypi.org/project/nequix/) · [source](https://github.com/atomicarchitects/nequix)

<details><summary>README extract</summary>

Source code and model weights for the Nequix foundation model, and Phonon fine-tuning (PFT).

Model | Dataset | Theory | Reference

`nequix-mp-1`| MPtrj | DFT (PBE+U) | Nequix
`nequix-mp-1-pft`| MPtrj, MDR Phonon | DFT (PBE+U) |PFT
`nequix-omat-1`| OMat24 | DFT (PBE+U, VASP 54) | PFT
`nequix-oam-1`| OMat24, sAlex, MPtrj | DFT (PBE+U) | ...

Example:
```python
from nequix.calculator import NequixCalculator

atoms = ...
atoms.calc = NequixCalculator("nequix-mp-1", backend="jax")
```

Sections: Nequix, Usage, ASE calculator, NequixCalculator, Training, Phonon fine-tuning (PFT), Phonon calculations, Training OMat/OAM base models

</details>

### nanoarrow

Python bindings to the nanoarrow C library

`pip install nanoarrow` · installs (wheel) · licence: Apache-2.0 · rank 7397 · last release 2026-08-04 · [PyPI](https://pypi.org/project/nanoarrow/) · [source](https://github.com/apache/arrow-nanoarrow)

<details><summary>README extract</summary>

<!---
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements. See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership. ...

Example:
```python
na.int32()
```

Sections: nanoarrow for Python, Data types, arrays, and array streams, Low-level C library bindings, Schemas, Arrays, Array streams

</details>

### nvidia-libnvcomp-cu12

NVIDIA nvcomp for CUDA 12

`pip install nvidia-libnvcomp-cu12` · installs (wheel) · licence: LICENSE AGREEMENT FOR NVIDIA SOFTWARE DEVELOPMENT KITS · rank 7480 · last release 2026-10-13 · [PyPI](https://pypi.org/project/nvidia-libnvcomp-cu12/)

<details><summary>README extract</summary>

The nvCOMP library provides fast lossless data compression and decompression using a GPU.
It features generic compression interfaces to enable developers to use high-performance GPU compressors in their applications.

</details>

### normality

Micro-library to normalize text strings

`pip install normality` · installs (wheel) · licence: MIT License · rank 7493 · last release 2026-03-08 · [PyPI](https://pypi.org/project/normality/) · [docs](https://github.com/pudo/normality) · [source](https://github.com/pudo/normality.git)

<details><summary>README extract</summary>

Normality is a Python micro-package that contains a small set of text normalization functions for easier re-use. These functions accept a snippet of unicode or utf-8 encoded text and remove various classes of characters, such as diacritics, punctuation etc. This is useful as a preparation to further text analysis. ...

Example:
```python
# coding: utf-8
from normality import normalize, slugify, collapse_spaces, ascii_text, latinize_text

text = normalize('Nie wieder "Grüne Süppchen" kochen!')
assert text == 'nie wieder grune suppchen kochen'

slug = slugify('My first blog post!')
assert slug == 'my-first-blog-post'

text = 'this \n\n\r\nhas\tlots of \nodd spacing.'
...
```

Sections: normality, Example

</details>

### ngboost

Library for probabilistic predictions via gradient boosting.

`pip install ngboost` · installs (wheel) · licence: Apache Software License · rank 7625 · last release 2026-11-07 · [PyPI](https://pypi.org/project/ngboost/) · [docs](https://stanfordmlgroup.github.io/ngboost/intro) · [source](https://github.com/stanfordmlgroup/ngboost)

<details><summary>README extract</summary>

ngboost is a Python library that implements Natural Gradient Boosting, as described in "NGBoost: Natural Gradient Boosting for Probabilistic Prediction". It is built on top of Scikit-Learn, and is designed to be scalable and modular with respect to choice of proper scoring rule, distribution, and base learner. ...

Example:
```python
from ngboost import NGBRegressor

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load California housing dataset
cal = fetch_california_housing()
X, Y = cal.data, cal.target

...
```

Sections: Usage, Reference

</details>

### netutils

Common helper functions useful in network automation.

`pip install netutils` · installs (wheel) · licence: Apache Software License · rank 7793 · last release 2026-09-23 · [PyPI](https://pypi.org/project/netutils/) · [docs](https://netutils.readthedocs.io) · [source](https://github.com/networktocode/netutils)

<details><summary>README extract</summary>

Features:
A Python library that is a collection of functions that are used in the common network automation tasks. Tasks such as converting a BGP ASN to and from dotted format, normalizing an interface name, or "type 5" encrypting a password. ...

Sections: Netutils, Overview, Documentation, Questions

</details>

### nvdlfw-inspect

Facilitates debugging convergence issues and testing new algorithms/recipes for training LLMs using Nvidia libraries.

`pip install nvdlfw-inspect` · installs (wheel) · licence: Apache2 · rank 7798 · last release 2025-12-03 · [PyPI](https://pypi.org/project/nvdlfw-inspect/)

<details><summary>README extract</summary>

This tool facilitates debugging convergence issues and testing new algorithms/recipes for training LLMs using Nvidia libraries: Transformer Engine, Megatron-LM, and NeMo. It is compatible with any PyTorch model and/or any combination of our libraries (e.g., Megatron-LM/NeMo + Transformer Engine or Transformer Engine/Megatron/Nemo standalone). ...

Example:
```python
debug_api.log_tensor_stats(layer_name, tensor=weight, tensor_name="weight")
```

Sections: Nvidia-DL-Framework-Inspect, Getting Started, Initialization, Configuration Files, Loading Specific Features, Available Features, API Usage, Documentation

</details>

### names-dataset

The python library to handle names

`pip install names-dataset` · installs (wheel) · licence: MIT · rank 7825 · last release 2025-04-08 · [PyPI](https://pypi.org/project/names-dataset/)

<details><summary>README extract</summary>

To download the raw CSV data for your analysis, browse here.

This Python library provides information about names:
- Popularity (rank)
- Country (105 countries are supported)
- Gender
- Fuzzy search (search with an erroneous name, `ISABLE -> ISABEL`)
- Auto-complete search (realtime, for example all names starting with `ISA*`.) ...

Example:
```python
from names_dataset import NameDataset, NameWrapper

# The library takes time to initialize because the database is massive. A tip is to include its initialization in your app's startup process.
nd = NameDataset()

print(NameWrapper(nd.search('Philippe')).describe)
# Male, France

print(NameWrapper(nd.search('Zoe')).describe)
...
```

Sections: First and Last Names Database, Composition, Usage, API, Full dataset, Ports, Countries

</details>

### nfoursid

Implementation of N4SID, Kalman filtering and state-space models

`pip install nfoursid` · installs (wheel) · licence: MIT License · rank 7881 · last release 2025-07-24 · [PyPI](https://pypi.org/project/nfoursid/)

<details><summary>README extract</summary>

Implementation of the N4SID algorithm for subspace identification [1], together with Kalman filtering and state-space
models.

State-space models are versatile models for representing multi-dimensional timeseries. ...

Sections: NFourSID, Documentation and code example, References

</details>

### ntgcalls

A Native Implementation of Telegram Calls in a seamless way.

`pip install ntgcalls` · installs (wheel) · licence: not stated · rank 7948 · last release 2026-11-03 · [PyPI](https://pypi.org/project/ntgcalls/) · [docs](https://pytgcalls.github.io/NTgCalls) · [source](https://github.com/pytgcalls/ntgcalls.git)

<details><summary>README extract</summary>

A Native Implementation of Telegram Calls in a seamless way.

 Examples


 Documentation


 PyPi


 npm


 crates.io


 Maven Central


 Releases


 Channel


 Chat

NTgCalls is a lightweight open-source library for media streaming in Telegram calls. ...

Features:
- Pre-built binaries for macOS (arm64-v8a), Linux (x86_64, arm64-v8a), Windows (x86_64), and Android (x86, 86_64, arm64-v8a, armv7)
- Call flexibility: Group and private call support
- Media controls: pause/resume and mute/unmute ...

Sections: NTgCalls, Features, Building from source, Special Thanks

</details>

### nv-one-logger-core

Extensions to onelogger library to use Open telemetry (OTEL) as a backend.

`pip install nv-one-logger-core` · installs (wheel) · licence: Apache Software License · rank 8084 · last release 2025-10-29 · [PyPI](https://pypi.org/project/nv-one-logger-core/)

<details><summary>README extract</summary>

This Python project contains the API and libraries for OneLogger: A library for collecting telemetry information from jobs.

The following are the dependency rules for various packages (which we will enforce by creating separate python projects in the end state):

- core: Classes representing core concepts such as span, event, attributes. ...

Example:
```python
from nv_one_logger.api.timed_span import configure_one_logger, get_recorder, timed_span

def main():
    # One-time initialization of the library
    config = OneLoggerConfig(....) # You can use a factory that takes a json or other representation of the configs and creates a OneLoggerConfig object.
...
```

...

</details>

### nv-one-logger-training-telemetry

Training job telemetry using OneLogger library.

`pip install nv-one-logger-training-telemetry` · installs (wheel) · licence: Apache Software License · rank 8087 · last release 2025-10-29 · [PyPI](https://pypi.org/project/nv-one-logger-training-telemetry/)

<details><summary>README extract</summary>

One Logger Training Telemetry is built on top of one-logger-core using the latter to collect telemetry data on training jobs. It includes

- Predefined spans, events, and attributes for a typical training job.
- Easy integration with several trainng frameworks. ...

Example:
```python
@application() # < ---- telemetry context manager
def main() -> None:

    ....

    with training_loop(train_iterations_start=0): # < ---- telemetry context manager
        ...

        for epoch in range(num_epochs):
            for batch_idx, (inputs, targets) in enumerate(dataloader):
...
```

...

</details>

### nv-one-logger-pytorch-lightning-integration

Wrappers that facilitate enabling training job telemetry for a set of supported training frameworks.

`pip install nv-one-logger-pytorch-lightning-integration` · does not install on CPython 3.14 · licence: Apache Software License · rank 8128 · last release 2025-10-29 · [PyPI](https://pypi.org/project/nv-one-logger-pytorch-lightning-integration/)

<details><summary>README extract</summary>

`one_logger_pytorch_lightning_integration` library provides an easy way to add telemetry to applications that use Pytorch Lightning for training.
The integration works by using Lightning's callback mechanism. ...

Example:
```python
import os
import torch
from pytorch_lightning import LightningModule, Trainer
from nv_one_logger.training_telemetry.api.training_telemetry_provider import TrainingTelemetryProvider
from nv_one_logger.training_telemetry.integration.pytorch_lightning import hook_trainer_cls

class SimpleModel(LightningModule):
    def init(self, learning_rate=1e-3):
...
```

Sections: Pytorch Lightning Integration, Minmum Requirements, Explicit vs Implicit Telemetry Collection, Full Example

</details>

### nbdime

Diff and merge of Jupyter Notebooks

`pip install nbdime` · installs (wheel) · licence: BSD License · rank 8176 · last release 2026-02-10 · [PyPI](https://pypi.org/project/nbdime/) · [source](https://github.com/jupyter/nbdime)

<details><summary>README extract</summary>

Installation |
Documentation |
Contributing |
Development Install |
Testing |
License |
Getting help

`nbdime` provides tools for diffing and merging of Jupyter Notebooks.

- `nbdiff` compare notebooks in a terminal-friendly way
- `nbmerge` three-way merge of notebooks with automatic conflict resolution ...

Sections: nbdime Jupyter Notebook Diff and Merge tools, Documentation, Getting help, Resources

</details>

### nptyping

Type hints for NumPy.

`pip install nptyping` · installs (wheel) · licence: MIT License · rank 8183 · last release 2023-02-20 · [PyPI](https://pypi.org/project/nptyping/)

<details><summary>README extract</summary>

🧊 *Type hints for `NumPy`*

🐼 *Type hints for `pandas.DataFrame`*

💡 *Extensive dynamic type checks for dtypes shapes and structures*

🚀 *Jump to the Quickstart*

Example of a hinted `numpy.ndarray`:

Example of a hinted `pandas.DataFrame`:

Example:
```python
def plan_route(
        locations: NDArray[Shape["[from, to], [x, y]"], Float]
) -> NDArray[Shape["* stops, [x, y]"], Float]:
    ...
```

Sections: Instance checking, NumPy Structured arrays, NumPy Record arrays, Pandas DataFrames, More examples, Documentation

</details>

### nvidia-nat-core

Core library for NVIDIA NeMo Agent Toolkit

`pip install nvidia-nat-core` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 8209 · last release 2026-09-10 · [PyPI](https://pypi.org/project/nvidia-nat-core/) · [docs](https://docs.nvidia.com/nemo/agent-toolkit/latest/) · [source](https://github.com/NVIDIA/NeMo-Agent-Toolkit)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2024-2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at ...

Features:
- Framework Agnostic: Works with any agentic framework, so you can use your current technology stack without replatforming.
- Reusability: Every agent, tool, or workflow can be combined and repurposed, allowing developers to leverage existing work ...

Sections: NVIDIA NeMo Agent Toolkit, Key Features, Links, First time user?, Feedback

</details>

### nvidia-nat-langchain

Subpackage for LangChain/LangGraph integration in NeMo Agent Toolkit

`pip install nvidia-nat-langchain` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 8244 · last release 2026-09-10 · [PyPI](https://pypi.org/project/nvidia-nat-langchain/) · [docs](https://docs.nvidia.com/nemo/agent-toolkit/latest/) · [source](https://github.com/NVIDIA/NeMo-Agent-Toolkit)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2025-2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at ...

</details>

### nvidia-nat-opentelemetry

Subpackage for OpenTelemetry integration in NeMo Agent Toolkit

`pip install nvidia-nat-opentelemetry` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 8247 · last release 2026-09-10 · [PyPI](https://pypi.org/project/nvidia-nat-opentelemetry/) · [docs](https://docs.nvidia.com/nemo/agent-toolkit/latest/) · [source](https://github.com/NVIDIA/NeMo-Agent-Toolkit)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2025-2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at ...

</details>

### notion-to-md-py

A package to convert Notion content into Markdown format

`pip install notion-to-md-py` · installs (wheel) · licence: MIT License · rank 8281 · last release 2026-05-11 · [PyPI](https://pypi.org/project/notion-to-md-py/) · [source](https://github.com/SwordAndTea/notion-to-md-py)

<details><summary>README extract</summary>

This is the Python implementation of nodejs version of notion-to-md,
a tool that converts Notion pages into Markdown files.

Example:
```python
from notion_client import Client
from notion_to_md import NotionToMarkdown

notion = Client(auth="your-auth-token")

n2m = NotionToMarkdown(notion)

# Export a page as a markdown blocks
md_blocks = n2m.page_to_markdown("page-id")

# Convert markdown blocks to string
md_str = n2m.to_markdown_string(md_blocks).get('parent')

# Write to a file
...
```

Sections: notion-to-md (Python Version), Usage, Sync Version, Async Version, Authentication with Notion API, Requirements, Limitations

</details>

### neon-api

An API Client for the Neon API.

`pip install neon-api` · installs (wheel) · licence: Apache Software License · rank 8361 · last release 2025-01-16 · [PyPI](https://pypi.org/project/neon-api/)

<details><summary>README extract</summary>

`neon_api` is a Python wrapper designed to simplify interactions with the Neon API. It provides a convenient way for developers to integrate their Python applications with the Neon platform, offering methods to manage API keys, projects, branches, databases, endpoints, roles, and operations programmatically. ...

Example:
```python
from neon_api import NeonAPI

# Initialize the client.
neon = NeonAPI(api_key='your_api_key')
```

Sections: `neon_api`: Python API wrapper for the Neon API., Usage, Methods of the `NeonAPI` class, Updating the schema

</details>

### nominal-api

(no summary)

`pip install nominal-api` · installs (wheel) · licence: not stated · rank 8380 · last release 2026-11-06 · [PyPI](https://pypi.org/project/nominal-api/)

### nvidia-nat-eval

Subpackage for evaluation in NVIDIA NeMo Agent Toolkit

`pip install nvidia-nat-eval` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 8392 · last release 2026-09-10 · [PyPI](https://pypi.org/project/nvidia-nat-eval/) · [docs](https://docs.nvidia.com/nemo/agent-toolkit/latest/) · [source](https://github.com/NVIDIA/NeMo-Agent-Toolkit)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at ...

</details>

### nutter

A databricks notebook testing library

`pip install nutter` · installs (wheel) · licence: MIT License · rank 8437 · last release 2022-12-16 · [PyPI](https://pypi.org/project/nutter/)

### nvidia-nat-atif

Subpackage for ATIF schema models in NVIDIA NeMo Agent Toolkit

`pip install nvidia-nat-atif` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 8488 · last release 2026-09-10 · [PyPI](https://pypi.org/project/nvidia-nat-atif/) · [docs](https://docs.nvidia.com/nemo/agent-toolkit/latest/) · [source](https://github.com/NVIDIA/NeMo-Agent-Toolkit)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at ...

</details>

### ncompress

LZW compression and decompression

`pip install ncompress` · installs (wheel) · licence: The Unlicense (Unlicense) · rank 8527 · last release 2024-01-30 · [PyPI](https://pypi.org/project/ncompress/) · [source](https://github.com/valgur/ncompress)

<details><summary>README extract</summary>

LZW compression and decompression in Python and C++.

Ported with minimal changes from the (N)compress CLI tool.

Sections: ncompress, Usage

</details>

### nessus-file-reader

LimberDuck NFR (nessus file reader) is a CLI tool and python module created to quickly parse nessus files containing the results of scans performed by Tenable Nessus and Tenable Security Center.

`pip install nessus-file-reader` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 8593 · last release 2026-10-23 · [PyPI](https://pypi.org/project/nessus-file-reader/)

_README extract left out: share-alike licence._

### nano-vectordb

A simple, easy-to-hack Vector Database implementation

`pip install nano-vectordb` · installs (wheel) · licence: MIT License · rank 8719 · last release 2024-11-11 · [PyPI](https://pypi.org/project/nano-vectordb/)

<details><summary>README extract</summary>

A simple, easy-to-hack Vector Database

 =3.9.11-blue">

🌬️ A vector database implementation with single-dependency (`numpy`).

🎁 It can handle a query from `100,000` vectors and return in 100 milliseconds.

🏃 It's okay for your prototypes, maybe even more.

🏃 Support naive multi-tenancy.

Example:
```python
from nano_vectordb import NanoVectorDB
import numpy as np

data_len = 100_000
fake_dim = 1024
fake_embeds = np.random.rand(data_len, fake_dim)

fakes_data = [{"vector": fake_embeds[i], **ANYFIELDS} for i in range(data_len)]
```

Sections: nano-VectorDB, Quick Start, Init a DB, Upsert, Query, Conditional filter, Save, Get, Delete, Additional Data, Multi-Tenancy, Benchmark

</details>

### nemo-fabric-runtime

Python SDK and native bindings for NeMo Fabric

`pip install nemo-fabric-runtime` · installs (wheel) · licence: Apache-2.0 · rank 8739 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nemo-fabric-runtime/) · [docs](https://docs.nvidia.com/nemo/fabric) · [source](https://github.com/NVIDIA/NeMo-Fabric)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

`nemo-fabric-runtime` provides the Python SDK and native Rust bindings for
NVIDIA NeMo Fabric, a runtime execution layer for agents.

Typically this is installed using the `nemo-fabric` meta package. ...

</details>

### neuralforecast

Time series forecasting suite using deep learning models

`pip install neuralforecast` · installs (wheel) · licence: Apache Software License · rank 8857 · last release 2026-10-07 · [PyPI](https://pypi.org/project/neuralforecast/) · [docs](https://nixtlaverse.nixtla.io/neuralforecast/)

<details><summary>README extract</summary>

NeuralForecast offers a large collection of neural forecasting models focusing on their performance, usability, and robustness. The models range from classic networks like RNNs to the latest transformers: `MLP`, `LSTM`, `GRU`, `RNN`, `TCN`, `TimesNet`, `BiTCN`, `DeepAR`, `NBEATS`, `NBEATSx`, `NHITS`, `TiDE`, `DeepNPTS`, `TSMixer`, `TSMixerx`, ...

Features:
There is a shared belief in Neural forecasting methods' capacity to improve forecasting pipeline's accuracy and efficiency.

Unfortunately, available implementations and published research are yet to realize neural networks' potential. ...

Example:
```python
from neuralforecast import NeuralForecast
from neuralforecast.models import NBEATS
from neuralforecast.utils import AirPassengersDF

nf = NeuralForecast(
...

</details>

### netapp-ontap

A library for working with ONTAP's REST APIs simply in Python

`pip install netapp-ontap` · installs (wheel) · licence: BSD License · rank 8958 · last release 2026-08-12 · [PyPI](https://pypi.org/project/netapp-ontap/) · [docs](https://library.netapp.com/ecmdocs/ECMLP3383665/html/index.html)

<details><summary>README extract</summary>

The Python client library is a package you can use when writing scripts to access the
ONTAP REST API. It provides support for several underlying services, including connection
management, asynchronous request processing, and exception handling. ...

Example:
```python
from netapp_ontap.resources import Volume

# Example 1 - keyword arguments
volume = Volume(name='vol1', svm={'name': 'vs1'}, aggregates=[{'name': 'aggr1'}])

# Example 2 - dict as keyword arguments
data = {
    'name': 'vol1',
    'svm': {'name': 'vs1'},
    'aggregates': [{'name': 'aggr1'}],
}
volume = Volume(**data)

...
```

...

</details>

### nameof

Get the name of a variable or attribute, as in C#

`pip install nameof` · installs from source (sdist only) · licence: MIT License · rank 9016 · last release 2020-02-01 · [PyPI](https://pypi.org/project/nameof/)

### nominal-api-protos

(no summary)

`pip install nominal-api-protos` · installs (wheel) · licence: not stated · rank 9059 · last release 2026-11-06 · [PyPI](https://pypi.org/project/nominal-api-protos/)

### npmai

npmai is a lightweight Python package designed to bridge the gap between users and open-source LLMs. Connect with Ollama and 45+ other powerful models instantly— no installation, no login, and no API keys required, and help in development of RAG Agents without installing anything locally or on cloud and it is free without sigin or signup or any type of limit.

`pip install npmai` · does not install on CPython 3.14 · licence: MIT · rank 9074 · last release 2026-05-16 · [PyPI](https://pypi.org/project/npmai/) · [source](https://github.com/sonuramashishnpm/npmai)

<details><summary>README extract</summary>

By Sonu Kumar (Viral Boy)

`npmai` is a lightweight Python package designed to bridge the gap between users and open-source LLMs.

Connect with Ollama and 45+ other powerful models instantly—no installation, no login, and no API keys required, and help in development of RAG Agents without installing anything locally or on cloud and it is free ...

Sections: 🚀 npmai, ✨ Features, Achievment for npmai:-, Workflow:-, npmai, Rag, npmai Ecosystem:-, Important Update in NPMAI RAG:-, 🚀 NPMAI Update: Advanced RAG & Refine Architecture, 🔍 1. Dynamic K-Context Retrieval (70% Coverage), 🔄 2. Sliding Window Batch-Refinement (3-Chunk Window), Thankyou Statement:-

</details>

### nanodjango

Run Django models and views from a single file, and convert it to a full project.

`pip install nanodjango` · installs (wheel) · licence: BSD License · rank 9131 · last release 2026-10-24 · [PyPI](https://pypi.org/project/nanodjango/) · [docs](https://nanodjango.readthedocs.io/en/latest/) · [source](https://github.com/radiac/nanodjango)

<details><summary>README extract</summary>

- Write a Django site in a single file, using views, models and admin
- Run it locally or in production, or share it as a standalone script
- Automatically convert it to a full Django project when you're ready for it to grow
- Try it out in your browser at the nanodjango playground ...

Example:
```python
from django.db import models
from nanodjango import Django

app = Django()

@app.admin
class CountLog(models.Model):
    # Standard Django model, registered with the admin site
    timestamp = models.DateTimeField(auto_now_add=True)

@app.route("/")
def count(request):
    # Standard Django function view, or class-based view
...
```

Sections: nanodjango, Quickstart, Convert it to a full site, Share an app, Run management commands, Run in production, Further reading

</details>

### nautilus_ibapi

Python IB API

`pip install nautilus_ibapi` · installs (wheel) · licence: Other/Proprietary License · rank 9375 · last release 2026-04-23 · [PyPI](https://pypi.org/project/nautilus_ibapi/) · [source](https://interactivebrokers.github.io/tws-api)

<details><summary>README extract</summary>

Installation Guide for TWS API Library

This guide provides step-by-step instructions for setting up the TWS API library, including creating virtual environments using both Anaconda and standard Python, building distributions, and testing the installation. ...

Example:
```python
import ibapi

print("TWS API version:", ibapi.version)
```

</details>

### nodejs-bin

Node.js is an open-source, cross-platform, back-end JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser.

`pip install nodejs-bin` · installs (wheel) · licence: MIT License · rank 9439 · last release 2022-07-06 · [PyPI](https://pypi.org/project/nodejs-bin/)

<details><summary>README extract</summary>

Node.js is an open-source, cross-platform, back-end JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser.

The nodejs-bin Python package redistributes Node.js so that it can be used as a dependency of Python projects. ...

Example:
```python
from nodejs import node, npm, npx

# Run Node.js and return the exit code.
node.call(['script.js', 'arg1', ...], **kwargs)

# Run npm and return the exit code.
npm.call(['command', 'arg1', ...], **kwargs)

# Run npx and return the exit code.
npx.call(['command', 'arg1', ...], **kwargs)
```

</details>

### nutpie

Sample Stan or PyMC models

`pip install nutpie` · installs (wheel) · licence: MIT · rank 9456 · last release 2026-06-30 · [PyPI](https://pypi.org/project/nutpie/) · [source](https://github.com/pymc-devs/nutpie)

<details><summary>README extract</summary>

The `nutpie` package provides a fast NUTS sampler for PyMC and Stan models.

See the documentation for more details.

Example:
```python
import pymc as pm
import numpy as np
import nutpie
import pandas as pd
import seaborn as sns

# Load the radon dataset
data = pd.read_csv(pm.get_data("radon.csv"))
data["log_radon"] = data["log_radon"].astype(np.float64)
county_idx, counties = pd.factorize(data.county)
coords = {"county": counties, "obs_id": np.arange(len(county_idx))}

...
```

Sections: nutpie: A fast sampler for Bayesian posteriors, Usage with PyMC, Usage with Stan, Advantages

</details>

### nemo-fabric-adapters-common

Shared Python helpers for NeMo Fabric adapters

`pip install nemo-fabric-adapters-common` · installs (wheel) · licence: Apache-2.0 · rank 9534 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nemo-fabric-adapters-common/) · [docs](https://docs.nvidia.com/nemo/fabric) · [source](https://github.com/NVIDIA/NeMo-Fabric)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

`nemo-fabric-adapters-common` provides shared helper methods for NeMo Fabric
adapter implementations. Adapter packages typically declare this package as a
dependency.

</details>

### nominal

Automate Nominal workflows in Python

`pip install nominal` · installs (wheel) · licence: Apache-2.0 · rank 9542 · last release 2026-11-03 · [PyPI](https://pypi.org/project/nominal/) · [docs](https://docs.nominal.io) · [source](https://github.com/nominal-io/nominal-client)

<details><summary>README extract</summary>

Nominal Python Client for test data, storage, and compute.

View on docs.nominal.io.

Sections: ⟢ Nominal, 📖 Docs, Usage

</details>

### nemo-fabric-adapter-contract

Typed Python contract for NeMo Fabric adapters

`pip install nemo-fabric-adapter-contract` · installs (wheel) · licence: Apache-2.0 · rank 9557 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nemo-fabric-adapter-contract/) · [docs](https://docs.nvidia.com/nemo/fabric) · [source](https://github.com/NVIDIA/NeMo-Fabric)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

`nemo-fabric-adapter-contract` provides the typed Python configuration and
execution contract implemented by NeMo Fabric adapters. ...

Example:
```python
from nemo_fabric_adapter_contract.models import AgentConfig
```

</details>

### nemo-fabric

Python SDK distribution for NeMo Fabric

`pip install nemo-fabric` · installs (wheel) · licence: Apache-2.0 · rank 9711 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nemo-fabric/) · [docs](https://docs.nvidia.com/nemo/fabric) · [source](https://github.com/NVIDIA/NeMo-Fabric)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

NeMo Fabric gives users one configurable, observable way to run applications
across agent harnesses and custom agents. ...

Sections: NVIDIA NeMo Fabric, Integrations, Harbor Integration, NeMo Relay Integration, Learn More

</details>

### nvidia-cutlass

CUTLASS

`pip install nvidia-cutlass` · installs (wheel) · licence: BSD License · rank 9712 · last release 2025-09-19 · [PyPI](https://pypi.org/project/nvidia-cutlass/)

<details><summary>README extract</summary>

Sections: Overview, CUTLASS 4.2.0, What's New in CUTLASS 4.2, CuTe DSL, CUTLASS C++, Performance, CuTe, Compatibility, Operating Systems, Hardware, Target Architecture, Documentation, Resources, Building CUTLASS

</details>

### neoteroi-mkdocs

Plugins for MkDocs and Python Markdown

`pip install neoteroi-mkdocs` · installs (wheel) · licence: MIT License · rank 9797 · last release 2025-11-23 · [PyPI](https://pypi.org/project/neoteroi-mkdocs/)

<details><summary>README extract</summary>

This package includes the following plugins and extensions:

| Name | Description |

| `mkdocsoad` | Generates documentation from OpenAPI specification files. |
| `cards` | Component to display cards. |
| `timeline` | Component to display chronological information with style. |
| `gantt` | Component to display Gantt diagrams. ...

Sections: Plugins for MkDocs and Python Markdown, Documentation, Preview, Cards extension, Gantt extension, Timeline extension, OpenAPI Documentation extension

</details>

### nbtlib

A python package to read and edit nbt data

`pip install nbtlib` · installs (wheel) · licence: MIT License · rank 9838 · last release 2021-11-25 · [PyPI](https://pypi.org/project/nbtlib/) · [docs](https://github.com/vberlier/nbtlib) · [source](https://github.com/vberlier/nbtlib)

<details><summary>README extract</summary>

> A python library to read and edit nbt data. Requires
> python 3.8.

Features

- Create, read and edit nbt files
- Supports gzipped and uncompressed files
- Supports big-endian and little-endian files
- Parse and serialize raw nbt data
- Define tag schemas that automatically enforce predefined tag types ...

Example:
```python
import nbtlib

nbt_file = nbtlib.load('bigtest.nbt')
assert nbt_file['intTest'] == 2147483647
```

Sections: nbtlib, Basic usage, Reading files, Editing files, Using schemas, Nbt literals, Nbt paths, Command-line interface, Read nbt data, Write nbt data, Merge nbt data, Compression and byte order

</details>

### nuscenes-devkit

The official devkit of the nuScenes dataset (www.nuscenes.org).

`pip install nuscenes-devkit` · installs (wheel) · licence: Free for non-commercial use · rank 9875 · last release 2025-08-28 · [PyPI](https://pypi.org/project/nuscenes-devkit/)

<details><summary>README extract</summary>

Welcome to the Motionalᵀᴹ nuTonomy® downloadable driverless vehicle software page. Click on the green box above labeled "Code" to download a copy of the software described below.

Features:
- Changelog
- Devkit setup
- nuImages
 - nuImages setup
 - Getting started with nuImages
- nuScenes
 - nuScenes setup
 - Panoptic nuScenes
 - nuScenes-lidarseg
 - Prediction challenge
 - CAN bus expansion
 - Map expansion
 - Map versions
 - Getting ...

Sections: nuScenes™ devkit, Overview, Devkit setup, nuImages, nuImages setup, Getting started with nuImages, nuScenes, nuScenes setup, Panoptic nuScenes, nuScenes-lidarseg, Prediction challenge, CAN bus expansion, Map expansion, Map versions

</details>

### nanotime

nanotime python implementation

`pip install nanotime` · installs from source (sdist only) · licence: MIT License · rank 9893 · last release 2011-09-22 · [PyPI](https://pypi.org/project/nanotime/)

### nemo-fabric-adapters-deepagents

LangChain Deep Agents adapter for NeMo Fabric

`pip install nemo-fabric-adapters-deepagents` · installs (wheel) · licence: Apache-2.0 · rank 9902 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nemo-fabric-adapters-deepagents/) · [docs](https://docs.nvidia.com/nemo/fabric) · [source](https://github.com/NVIDIA/NeMo-Fabric)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

`nemo-fabric-adapters-deepagents` provides a NeMo Fabric adapter for use with LangChain Deep Agents.

</details>

### neurokit2

The Python Toolbox for Neurophysiological Signal Processing.

`pip install neurokit2` · installs (wheel) · licence: MIT License · rank 9910 · last release 2026-11-01 · [PyPI](https://pypi.org/project/neurokit2/) · [docs](https://neuropsychology.github.io/NeuroKit/) · [source](https://github.com/neuropsychology/NeuroKit)

<details><summary>README extract</summary>

The Python Toolbox for Neurophysiological Signal Processing

NeuroKit2 is a user-friendly package providing easy access to advanced biosignal processing routines.
Researchers and clinicians without extensive knowledge of programming or biomedical signal processing
can analyze physiological data with only two lines of code.

Example:
```python
import neurokit2 as nk

# Download example data
data = nk.data("bio_eventrelated_100hz")

# Preprocess the data (filter, find peaks, etc.)
processed_data, info = nk.bio_process(ecg=data["ECG"], rsp=data["RSP"], eda=data["EDA"], sampling_rate=100)

# Compute relevant features
results = nk.bio_analyze(processed_data, sampling_rate=100)
```

...

</details>

### nr-stream

(no summary)

`pip install nr-stream` · installs (wheel) · licence: MIT License · rank 9930 · last release 2023-02-14 · [PyPI](https://pypi.org/project/nr-stream/)

<details><summary>README extract</summary>

This package provides utilities for writing functional-style code in Python. The package originally contained only
the `Stream` class, hence the name, but since we've adopted the terminology for letting us *streamline* large chunks
of our code.

Represents an optional value, i.e. one that either has a valid value or is `None`. ...

Example:
```python
import os
from nr.stream import Optional

opt = Optional(os.getenv("SOMEVAR"))
value = opt.or_else_get(lambda: do_something_else())
value = opt.or_else_raise(lambda: Exception("SOMEVAR not set"))
opt = opt.map(lambda value: value + " another value")
len(opt.stream().count())  # 0 or 1
```

Sections: nr-stream, API, Optional objects, Refreshable objects, Stream objects, Supplier objects

</details>

### nemo-fabric-adapters-claude

Claude adapter for NeMo Fabric

`pip install nemo-fabric-adapters-claude` · installs (wheel) · licence: Apache-2.0 · rank 9991 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nemo-fabric-adapters-claude/) · [docs](https://docs.nvidia.com/nemo/fabric) · [source](https://github.com/NVIDIA/NeMo-Fabric)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

`nemo-fabric-adapters-claude` provides a NeMo Fabric adapter for Claude Code.

</details>

### nemo-fabric-adapters-codex

Codex adapter for NeMo Fabric

`pip install nemo-fabric-adapters-codex` · installs (wheel) · licence: Apache-2.0 · rank 9996 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nemo-fabric-adapters-codex/) · [docs](https://docs.nvidia.com/nemo/fabric) · [source](https://github.com/NVIDIA/NeMo-Fabric)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

`nemo-fabric-adapters-codex` provides a NeMo Fabric adapter for use with Codex.

</details>

### nr-date

(no summary)

`pip install nr-date` · installs (wheel) · licence: MIT License · rank 10002 · last release 2023-08-16 · [PyPI](https://pypi.org/project/nr-date/)

<details><summary>README extract</summary>

A fast, regex-based date parsing library in pure Python.

</details>

### notifications-python-client

Python API client for GOV.UK Notify.

`pip install notifications-python-client` · installs (wheel) · licence: MIT License · rank 10020 · last release 2026-10-23 · [PyPI](https://pypi.org/project/notifications-python-client/)

<details><summary>README extract</summary>

Python API client for GOV.UK Notify - see for more information.

For usage and documentation see

</details>

### nominal-streaming

Python bindings for the Nominal Rust streaming client

`pip install nominal-streaming` · installs (wheel) · licence: MIT License · rank 10064 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nominal-streaming/) · [source](https://github.com/nominal-io/nominal-streaming)

<details><summary>README extract</summary>

`nominal-streaming` is a thin python wrapper around the existing nominal-streaming rust crate.
Usage semantics remain largely the same, but with some slight alterations to allow for a more pythonic interface.

Requires Python 3.11 or newer.

The library aims to balance three concerns:

1. ...

Example:
```python
import pathlib
import time

from nominal.core import NominalClient
from nominal_streaming import NominalDatasetStream, PyNominalStreamOpts

if name == "main":
    num_points = 100_000
    stream = (
        NominalDatasetStream(
            auth_header="<api key>",
            opts=PyNominalStreamOpts(),
        )
...
```

Sections: nominal-streaming Python Bindings, Runtime metrics, NumPy batches, Measuring enqueue performance, Log streams

</details>

### numpyencoder

Python JSON encoder for handling Numpy data types.

`pip install numpyencoder` · installs (wheel) · licence: MIT · rank 10132 · last release 2025-07-15 · [PyPI](https://pypi.org/project/numpyencoder/)

<details><summary>README extract</summary>

Custom Python JSON encoder for handling Numpy data types.

Example Use:

Example:
```python
from numpyencoder import NumpyEncoder

numpy_data = np.array([0, 1, 2, 3])

with open(json_file, 'w') as file:
    json.dump(
        numpy_data,
        file,
        indent=4,
        sort_keys=True,
        separators=(', ', ': '),
        ensure_ascii=False,
        cls=NumpyEncoder
    )
```

</details>

### notion2md

Notion Markdown Exporter with Python Cli

`pip install notion2md` · installs (wheel) · licence: MIT License · rank 10141 · last release 2024-01-10 · [PyPI](https://pypi.org/project/notion2md/)

<details><summary>README extract</summary>

- Notion Markdown Exporter using official notion api by notion-sdk-py

- Check out Notion2Medium that publishes a Medium post from Notion using Notion2Md.

- Before getting started, create an integration and find the token. → Learn more about authorization.

- Then save your api key(token) as your os environment variable ...

Example:
```python
from notion2md.exporter.block import MarkdownExporter, StringExporter

# MarkdownExporter will make markdown file on your output path
MarkdownExporter(block_id='...',output_path='...',download=True).export()

# StringExporter will return output as String type
md = StringExporter(block_id='...',output_path='...').export()
```

Sections: About Notion2Md, Notion2Medium, API Key(Token), Usage: Shell Command, Usage: Python, To-do

</details>

### nemo-fabric-collector

Standalone collector for NVIDIA NeMo Fabric

`pip install nemo-fabric-collector` · installs (wheel) · licence: Apache-2.0 · rank 10283 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nemo-fabric-collector/)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Standalone service for collecting and routing NVIDIA NeMo Relay records to
NVIDIA NeMo Fabric runtimes.

Adding the collector to an asynchronous Python application can be done as follows.

Example:
```python
from nemo_fabric_collector import serve_collector

async with serve_collector(host="127.0.0.1", port=0) as base_url:
    print(base_url)
```

</details>

### Nasdaq-Data-Link

Package for Nasdaq Data Link API access

`pip install Nasdaq-Data-Link` · installs (wheel) · licence: MIT License · rank 10345 · last release 2022-08-29 · [PyPI](https://pypi.org/project/Nasdaq-Data-Link/)

<details><summary>README extract</summary>

A Python library for Nasdaq Data Link's RESTful API.

You can install this package by using the pip tool and installing:

 $ pip install nasdaq-data-link

Sections: Official Nasdaq Data Link API Client for Python, Setup

</details>

### nemo-fabric-adapters-hermes

Hermes Agent adapter for NeMo Fabric

`pip install nemo-fabric-adapters-hermes` · installs (wheel) · licence: Apache-2.0 · rank 10349 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nemo-fabric-adapters-hermes/) · [docs](https://docs.nvidia.com/nemo/fabric) · [source](https://github.com/NVIDIA/NeMo-Fabric)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

`nemo-fabric-adapters-hermes` provides a NeMo Fabric adapter for use with Hermes Agent.

</details>

### nr-util

General purpose Python utility library.

`pip install nr-util` · installs (wheel) · licence: MIT License · rank 10378 · last release 2022-06-20 · [PyPI](https://pypi.org/project/nr-util/)

<details><summary>README extract</summary>

General purpose Python utility library.

Compatible with Python 3.7 and higher.

</details>

### npe2

napari plugin engine v2

`pip install npe2` · installs (wheel) · licence: BSD License · rank 10495 · last release 2026-11-04 · [PyPI](https://pypi.org/project/npe2/) · [source](https://github.com/napari/npe2)

<details><summary>README extract</summary>

The napari plugin engine version 2, npe2 extends the functionality of
napari's core.
The plugin ecosystem offers user additional functionality for napari as well
as specific support for different scientific domains.

This repo contains all source code and documentation required for defining, validating and managing plugins for napari.

Sections: npe2 - napari plugin engine version 2, Project description, Getting started, Plugin users, Using pip, Using conda, Usage, Examples, Contact us

</details>

### nmslib

Non-Metric Space Library (NMSLIB)

`pip install nmslib` · installs (wheel) · licence: not stated · rank 10693 · last release 2025-12-01 · [PyPI](https://pypi.org/project/nmslib/)

<details><summary>README extract</summary>

Non-Metric Space Library (NMSLIB) is an efficient cross-platform
 similarity search library and a toolkit for evaluation of similarity search methods.
 The goal of the project is to create an effective and comprehensive toolkit for searching
 in generic and non-metric spaces. ...

</details>

### nvidia-nat-config-optimizer

Workflow config and prompt optimizer for NVIDIA NeMo Agent Toolkit

`pip install nvidia-nat-config-optimizer` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 10755 · last release 2026-09-10 · [PyPI](https://pypi.org/project/nvidia-nat-config-optimizer/) · [docs](https://docs.nvidia.com/nemo/agent-toolkit/latest/) · [source](https://github.com/NVIDIA/NeMo-Agent-Toolkit)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2025-2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at ...

</details>

### nemo-anonymizer

NeMo Anonymizer

`pip install nemo-anonymizer` · installs (wheel) · licence: Apache-2.0 · rank 10758 · last release 2026-10-28 · [PyPI](https://pypi.org/project/nemo-anonymizer/)

<details><summary>README extract</summary>

Detect and replace sensitive entities in text using LLM-powered workflows.

- Detect entities using GLiNER-PII and LLM-based augmentation and validation
- Replace with 4 strategies — LLM-generated substitute, redact, annotate, or hash (deterministic, local)
- Preview results before full runs with `display_record()` visualization

Example:
```python
from anonymizer import Anonymizer, AnonymizerConfig, AnonymizerInput, Redact
DATA_URL = "

# Uses Anonymizer's bundled model providers (see src/anonymizer/config/default_model_configs/providers.yaml)
anonymizer = Anonymizer()

config = AnonymizerConfig(replace=Redact())

preview = anonymizer.preview(
    config=config,
...
```

...

</details>

### nvidia-nat

NVIDIA NeMo Agent Toolkit

`pip install nvidia-nat` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 10868 · last release 2026-09-10 · [PyPI](https://pypi.org/project/nvidia-nat/) · [docs](https://docs.nvidia.com/nemo/agent-toolkit/latest/) · [source](https://github.com/NVIDIA/NeMo-Agent-Toolkit)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2024-2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at ...

Features:
- Framework Agnostic: Works with any agentic framework, so you can use your current technology stack without replatforming.
- Reusability: Every agent, tool, or workflow can be combined and repurposed, allowing developers to leverage existing work ...

Sections: NVIDIA NeMo Agent Toolkit, Key Features, Links, First time user?, Feedback

</details>

### nvdlib

A simple wrapper for the National Vulnerability CVE/CPE API

`pip install nvdlib` · installs (wheel) · licence: MIT · rank 10916 · last release 2026-09-27 · [PyPI](https://pypi.org/project/nvdlib/) · [docs](https://nvdlib.com)

<details><summary>README extract</summary>

NVDlib is a Python library that allows you to interface with the NIST National Vulnerability Database (NVD), pull vulnerabilities (CVEs), and Common Platform Enumeration (CPEs) into easily accessible objects.

Features:
- Search the NVD for CVEs using all parameters allowed by the NVD API version 2. Including search criteria such as CVE publish and modification date, keywords, CVSS V2/V3/V4 severity or metrics, CPE name, CVE tags, and KEV catalog dates. ...

Example:
```python
>>> import nvdlib
>>> r = nvdlib.searchCVE(cveId='CVE-2021-26855')[0]
>>> print(r.v31severity + ' - ' + str(r.v31score))
CRITICAL - 9.1
>>> print(r.descriptions[0].value)
Microsoft Exchange Server Remote Code Execution Vulnerability This CVE ID is unique from CVE-2021-26412,
...
```

...

</details>

### nb-clean

Clean Jupyter notebooks for versioning

`pip install nb-clean` · installs (wheel) · licence: ISC · rank 11167 · last release 2026-11-02 · [PyPI](https://pypi.org/project/nb-clean/) · [source](https://github.com/srstevenson/nb-clean)

<details><summary>README extract</summary>

nb-clean cleans Jupyter notebooks for version control. It removes cell metadata,
execution counts, outputs, and the notebook's language version. It can check
notebooks in CI, clean files in place, or run as a Git filter or pre-commit
hook.

Sections: Checking and cleaning, Options, Git filter, Pre-commit, Jujutsu, Migrating from nb-clean 5, Migrating from nb-clean 4, Copyright

</details>

### ntropy-sdk

SDK for the Ntropy API

`pip install ntropy-sdk` · installs (wheel) · licence: MIT License · rank 11183 · last release 2026-10-07 · [PyPI](https://pypi.org/project/ntropy-sdk/)

<details><summary>README extract</summary>

This repository hosts the SDK for the Ntropy API. It provides transaction enrichment and categorization, account ledger
and metrics. The full documentation is available at the developer portal.

To obtain an API key, you can follow this guide.

Example:
```python
from ntropy_sdk import SDK

sdk = SDK("YOUR-API-KEY")
r = sdk.transactions.create(
    id="4yp49x3tbj9mD8DB4fM8DDY6Yxbx8YP14g565Xketw3tFmn",
    description="AMAZON WEB SERVICES",
    entry_type="outgoing",
    amount=12042.37,
    currency="USD",
    date="2021-11-01",
    location=dict(
        country="US"
    ),
)
print(r)
```

Sections: Ntropy SDK, Quick Start, Documentation

</details>

### njsscan

njsscan is a SAST tool that can find insecure code patterns in your Node.js applications.

`pip install njsscan` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 11245 · last release 2026-10-27 · [PyPI](https://pypi.org/project/njsscan/)

_README extract left out: share-alike licence._

### nemo-fabric-adapters-remote-agent

Remote agent adapter for NeMo Fabric

`pip install nemo-fabric-adapters-remote-agent` · installs (wheel) · licence: Apache-2.0 · rank 11288 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nemo-fabric-adapters-remote-agent/) · [docs](https://docs.nvidia.com/nemo/fabric) · [source](https://github.com/NVIDIA/NeMo-Fabric)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

`nemo-fabric-adapters-remote-agent` provides the `nvidia.fabric.remote-agent`
adapter for remote agents with OpenAI Responses, OpenAI Chat Completions, or
Anthropic Messages HTTP APIs. ...

</details>

### nvgpu

NVIDIA GPU tools

`pip install nvgpu` · installs from source (sdist only) · licence: MIT License · rank 11412 · last release 2023-03-30 · [PyPI](https://pypi.org/project/nvgpu/)

<details><summary>README extract</summary>

It provides information about GPUs and their availability for computation.

Often we want to train a ML model on one of GPUs installed on a multi-GPU
machine. Since TensorFlow allocates all memory, only one such process can
use the GPU at a time. Unfortunately `nvidia-smi` provides only a text
interface with information about GPUs. ...

Example:
```python
import nvgpu

nvgpu.available_gpus()
# ['0', '2']

nvgpu.gpu_info()
[{'index': '0',
  'mem_total': 8119,
  'mem_used': 7881,
  'mem_used_percent': 97.06860450794433,
  'type': 'GeForce GTX 1070',
  'uuid': 'GPU-3aa99ee6-4a9f-470e-3798-70aaed942689'},
 {'index': '1',
  'mem_total': 11178,
  'mem_used': 10795,
...
```

Sections: `nvgpu` - NVIDIA GPU tools, Usage examples, Web application with agents, Agent, Master, TODO

</details>

### numerize

Convert large numbers into readable numbers for humans.

`pip install numerize` · installs from source (sdist only) · licence: MIT · rank 11418 · last release 2018-08-14 · [PyPI](https://pypi.org/project/numerize/)

<details><summary>README extract</summary>

Numerize is a Python (2 and 3) library for converting large numbers into readable strings.
Similar to what Twitter and Instagram use for large follower counts.

| Number | Numerized | ...

Example:
```python
>>> from numerize import numerize
>>> numerize(1234567.12)
'1.23M'
>>> numerize(12134.123, 3)
'12.134K'
```

Sections: Numerize, Usage, Requirements

</details>

### netsuite

Make async requests to NetSuite SuiteTalk SOAP/REST Web Services and Restlets

`pip install netsuite` · installs (wheel) · licence: MIT License · rank 11565 · last release 2024-03-04 · [PyPI](https://pypi.org/project/netsuite/) · [docs](https://jacobsvante.github.io/netsuite/) · [source](https://github.com/jacobsvante/netsuite)

<details><summary>README extract</summary>

Make async requests to NetSuite SuiteTalk SOAP, REST Web Services, and Restlets. Detailed documentation available here.

Sections: netsuite, Documentation

</details>

### nlpaug

Natural language processing augmentation library for deep neural networks

`pip install nlpaug` · installs (wheel) · licence: MIT · rank 11693 · last release 2022-07-07 · [PyPI](https://pypi.org/project/nlpaug/)

<details><summary>README extract</summary>

This python library helps you with augmenting nlp for your machine learning projects. Visit this introduction to understand about Data Augmentation in NLP. `Augmenter` is the basic element of augmentation while `Flow` is a pipeline to orchestra multi augmenter together.

Features:
* Generate synthetic data for improving model performance without manual effort
* Simple, easy-to-use and lightweight library. Augment data in 3 lines of code
* Plug and play to any machine leanring/ neural network frameworks (e.g. ...

Sections: nlpaug, Features, Textual Data Augmentation Example, Acoustic Data Augmentation Example, Quick Demo, Augmenter, Flow, Recent Changes, 1.1.11 Jul 6, 2022, Extension Reading, Reference

</details>

### noto-cjk-sans-otc

Noto Sans CJK OpenType Collection (Regular)

`pip install noto-cjk-sans-otc` · installs (wheel) · licence: OFL-1.1 · rank 11697 · last release 2026-08-14 · [PyPI](https://pypi.org/project/noto-cjk-sans-otc/) · [docs](https://github.com/bowenliang123/py-noto-cjk)

<details><summary>README extract</summary>

Noto Sans CJK OpenType Collection (Regular).

This package only carries the font file. Use the
`noto-cjk` meta-package for a Python API
and to discover all available fonts:

 pip install noto-cjk[sans]

Fonts are licensed under the SIL Open Font License, Version 1.1.

</details>

### NREL-PySAM

National Laboratory of the Rockies' System Advisor Model Python Wrapper

`pip install NREL-PySAM` · does not install on CPython 3.14 · licence: BSD 3-Clause · rank 11732 · last release 2026-04-28 · [PyPI](https://pypi.org/project/NREL-PySAM/)

### nnaudio

A fast GPU audio processing toolbox with 1D convolutional neural network

`pip install nnaudio` · installs (wheel) · licence: MIT License · rank 11779 · last release 2025-12-07 · [PyPI](https://pypi.org/project/nnaudio/)

<details><summary>README extract</summary>

Please refer to the nnAudio homepage
Github-flavored Markdown

</details>

### ntstatus

Python enum for NTSTATUS from WinAPI, supporting comparision to both signed and unsigned integers

`pip install ntstatus` · installs (wheel) · licence: MIT · rank 11789 · last release 2025-06-11 · [PyPI](https://pypi.org/project/ntstatus/)

<details><summary>README extract</summary>

Example:
```python
>>> from ntstatus import NtStatus
```

Sections: Usage examples, List of values, Licensing

</details>

### nitypes

Data types for NI Python APIs

`pip install nitypes` · installs (wheel) · licence: MIT License · rank 11808 · last release 2026-06-16 · [PyPI](https://pypi.org/project/nitypes/) · [docs](https://nitypes.readthedocs.io/) · [source](https://github.com/ni/nitypes-python)

<details><summary>README extract</summary>

| Info | Data types for NI Python APIs |

| Author | National Instruments |

Sections: About, Documentation, Waveforms, Analog Waveforms, Complex Waveforms, Digital Waveforms, Frequency Spectrums, Complex Numbers, Complex Integers, Complex Number Conversion, Time, Time Conversion, Binary Time, Scalar Values

</details>

### neutron-lib

Neutron shared routines and utilities

`pip install neutron-lib` · installs (wheel) · licence: Apache-2.0 · rank 11983 · last release 2026-08-24 · [PyPI](https://pypi.org/project/neutron-lib/) · [docs](https://docs.openstack.org/neutron-lib) · [source](https://opendev.org/openstack/neutron-lib)

<details><summary>README extract</summary>

Neutron shared routines and utilities.

* Free software: Apache license

</details>

### novu-py

Python Client SDK Generated by Speakeasy.

`pip install novu-py` · installs (wheel) · licence: not stated · rank 12021 · last release 2026-08-07 · [PyPI](https://pypi.org/project/novu-py/) · [source](https://github.com/novuhq/novu-py.git)

<details><summary>README extract</summary>

The notification platform that turns complex multi-channel delivery into a single component. Built for developers, designed for growth, powered by open source.

The Python Novu SDK and package provides a fluent and expressive interface for interacting with Novu's API and managing notifications.

Novu API: Novu REST API. ...

Example:
```python
# !/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
# "novu-py",
# ]
# ///

from novu_py import Novu

sdk = Novu(
  # SDK arguments
)

# Rest of script here...
```

...

</details>

### nudenet

Lightweight Nudity Detection

`pip install nudenet` · installs (wheel) · licence: MIT License · rank 12078 · last release 2024-07-03 · [PyPI](https://pypi.org/project/nudenet/)

<details><summary>README extract</summary>

Looking for contributors/ maintainers for this repo:
I have become busy with other stuff in the last years, still trying to maintain this repo as it is the current best OSS option for nudity detection,
Looking for interested mainttainer, who can add/ work on more features for this repo (with my help of course) ...

Example:
```python
from nudenet import NudeDetector
detector = NudeDetector()
# the 320n model included with the package will be used

detector.detect('image.jpg') # Returns list of detections

detector.detect_batch(['image_1.jpg', 'image_2.jpg']) # Returns list of [list of detections]
```

Sections: NudeNet: lightweight Nudity detection, Available models, Docker, Some interesting projects based on NudeNet

</details>

### neonize

Neonize is a Python library designed to streamline the automation of tasks on WhatsApp

`pip install neonize` · installs (wheel) · licence: not stated · rank 12125 · last release 2026-11-03 · [PyPI](https://pypi.org/project/neonize/)

<details><summary>README extract</summary>

A Python library for WhatsApp automation. A native Go core built on
whatsmeow is compiled into a shared
library and exposed to Python through a zero-copy FFI layer.

Getting Started | Features | Examples | Documentation | Contributing

Features:
| | |

| Go core performance | The WhatsApp multidevice protocol runs in Go, called directly through ctypes. No subprocesses, no HTTP bridges. |
| Python native | Fully typed, idiomatic API. Sync and async clients with identical surfaces. ...

Example:
```python
from neonize.client import NewClient
from neonize.events import ConnectedEv, MessageEv

client = NewClient("session.db")

@client.event(ConnectedEv)
def on_connected(client: NewClient, _: ConnectedEv) -> None:
    print("Connected")

@client.event(MessageEv)
...

</details>

### nemo-fabric-adapters-nooa

NOOA adapters for NeMo Fabric

`pip install nemo-fabric-adapters-nooa` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 12153 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nemo-fabric-adapters-nooa/) · [docs](https://docs.nvidia.com/nemo/fabric) · [source](https://github.com/NVIDIA/NeMo-Fabric)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

`nemo-fabric-adapters-nooa` provides NVIDIA NeMo Fabric adapters for
NVIDIA-labs Object Oriented Agents
(NOOA) `InteractiveAgent` targets and `nooa_bench.BenchAgent` evaluations.

</details>

### nemo-fabric-adapters-mini-swe-agent

mini-SWE-agent adapter for NeMo Fabric

`pip install nemo-fabric-adapters-mini-swe-agent` · installs (wheel) · licence: Apache-2.0 · rank 12383 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nemo-fabric-adapters-mini-swe-agent/) · [docs](https://docs.nvidia.com/nemo/fabric) · [source](https://github.com/NVIDIA/NeMo-Fabric)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

`nemo-fabric-adapters-mini-swe-agent` translates the NVIDIA NeMo Fabric
adapter contract into mini-SWE-agent's native shell-only execution loop.

</details>

### nbdev-stdlib

nbdev docs lookup for the python standard library

`pip install nbdev-stdlib` · installs (wheel) · licence: Apache Software License · rank 12528 · last release 2026-02-09 · [PyPI](https://pypi.org/project/nbdev-stdlib/)

<details><summary>README extract</summary>

nbdev docs lookup for the python standard library, scipy, pandas, numpy, django, pytorch, sphinx, and APL.

</details>

### nanobot-ai

A lightweight personal AI assistant framework

`pip install nanobot-ai` · installs (wheel) · licence: MIT License · rank 12634 · last release 2026-11-06 · [PyPI](https://pypi.org/project/nanobot-ai/)

<details><summary>README extract</summary>

English |
 简体中文 |
 繁體中文 |
 Español |
 Français |
 Bahasa Indonesia |
 日本語 |
 한국어 |
 Русский |
 Tiếng Việt

 Discord ·
 X ·
 WeChat 微信交流群 ·
 Feishu

🐈 nanobot is an ultra-lightweight, open-source, self-hosted personal AI agent framework written in Python. ...

Sections: nanobot, Start Here, What can nanobot do?, 💡 Why nanobot, 🚀 Quick Start, ☁️ Deploy, 🌐 WebUI, Keep related work side by side, Inspect the work and its context, Bring your tools into the conversation, Let recurring work run on a schedule, Architecture, Docs, Recent Updates

</details>

### ndcube

A package for multi-dimensional contiguous and non-contiguous coordinate aware arrays.

`pip install ndcube` · installs (wheel) · licence: not stated · rank 12675 · last release 2026-10-27 · [PyPI](https://pypi.org/project/ndcube/) · [docs](https://docs.sunpy.org/projects/ndcube) · [source](https://github.com/sunpy/ndcube)

<details><summary>README extract</summary>

`ndcube` is an open-source SunPy affiliated package for manipulating, inspecting and visualizing multi-dimensional contiguous and non-contiguous coordinate-aware data arrays.

It combines data, uncertainties, units, metadata, masking, and coordinate transformations into classes with unified slicing and generic coordinate transformations and ...

Sections: ndcube, Usage of Generative AI, Getting Help

</details>

### nbdev-numpy

nbdev docs lookup for numpy

`pip install nbdev-numpy` · installs (wheel) · licence: Apache Software License · rank 12728 · last release 2026-02-09 · [PyPI](https://pypi.org/project/nbdev-numpy/)

<details><summary>README extract</summary>

nbdev docs lookup for the python standard library, scipy, pandas, numpy, django, pytorch, sphinx, and APL.

</details>

### nixtla

Python SDK for Nixtla API (TimeGPT)

`pip install nixtla` · installs (wheel) · licence: Apache Software License · rank 12788 · last release 2026-09-21 · [PyPI](https://pypi.org/project/nixtla/) · [docs](https://nixtlaverse.nixtla.io/) · [source](https://github.com/Nixtla/nixtla/)

<details><summary>README extract</summary>

TimeGPT is a production ready, generative pretrained transformer for time series. It's capable of accurately predicting various domains such as retail, electricity, finance, and IoT with just a few lines of code 🚀.

Example:
```python
import pandas as pd
from nixtla import NixtlaClient
```

Sections: Nixtla, TimeGPT-2.1, Foundation model for forecasting and anomaly detection, 🚀 Quick Start, Import libraries and load data, Forecast using TimeGPT in 3 easy steps, Anomaly detection using TimeGPT in 3 easy steps, ❄️ Snowflake Deployment, 🔥 Features and Capabilities, 📚 Documentation with examples and use cases, ⚙️ TimeGPT's Architecture, ⚡️ Zero-shot Results, Accuracy, Ease of use

</details>

### nvidia-resiliency-ext

NVIDIA Resiliency Package

`pip install nvidia-resiliency-ext` · installs (wheel) · licence: Other/Proprietary License · rank 12897 · last release 2026-09-16 · [PyPI](https://pypi.org/project/nvidia-resiliency-ext/) · [source](https://github.com/NVIDIA/nvidia-resiliency-ext)

<details><summary>README extract</summary>

The NVIDIA Resiliency Extension (NVRx) integrates multiple resiliency-focused solutions for PyTorch-based workloads. Users can modularly integrate NVRx capabilities into their own infrastructure to maximize AI training productivity at scale. ...

Sections: NVIDIA Resiliency Extension, Core Components and Capabilities, From sources, From PyPI wheel

</details>

### nox-poetry

nox-poetry

`pip install nox-poetry` · installs (wheel) · licence: MIT License · rank 12927 · last release 2025-02-25 · [PyPI](https://pypi.org/project/nox-poetry/) · [docs](https://nox-poetry.readthedocs.io) · [source](https://github.com/cjolowicz/nox-poetry)

<details><summary>README extract</summary>

[][pypi]
[][python version]
[][license]

[][read the docs]
[][tests]
[][codecov]

Use [Poetry] inside [Nox] sessions

This package provides a drop-in replacement for the `nox.session` decorator,
and for the `nox.Session` object passed to user-defined session functions. ...

Features:
Let's look at an example:

This session performs the following steps:

- Build a wheel from the local package.
- Install the wheel as well as the `pytest` package.
- Invoke `pytest` to run the test suite against the installation. ...

Example:
```python
from nox_poetry import session

@session(python=["3.10", "3.9"])
def tests(session):
    session.install("pytest", ".")
    session.run("pytest")
```

Sections: nox-poetry, Requirements, Usage, Why?, Issues

</details>

### nvidia-physicsnemo

A deep learning framework for AI-driven multi-physics systems

`pip install nvidia-physicsnemo` · installs (wheel) · licence: Apache-2.0 · rank 13012 · last release 2026-09-11 · [PyPI](https://pypi.org/project/nvidia-physicsnemo/) · [docs](https://docs.nvidia.com/physicsnemo/index.html#core)

<details><summary>README extract</summary>

📝 NVIDIA PhysicsNeMo is undergoing an update to v2.0 - all the features, with easier installation and integration to external packages. See the migration guide for more details!

NVIDIA PhysicsNeMo
| Documentation
| Install Guide
| Getting Started
| Contributing Guidelines
| Dev blog ...

Features:
Here are some of the key benefits of PhysicsNeMo for SciML model development:

 | |

|SciML Benchmarking and Validation|Ease of Using Generalized SciML Recipes with Heterogeneous Datasets |Out-of-the-Box Performance and Scalability
|PhysicsNeMo ...

Example:
```python
>>> import torch
>>> from physicsnemo.models.mlp.fully_connected import FullyConnected
>>> model = FullyConnected(in_features=32, out_features=64)
>>> input = torch.randn(128, 32)
>>> output = model(input)
>>> output.shape
...

</details>

### nbdev-scipy

nbdev docs lookup for scipy

`pip install nbdev-scipy` · installs (wheel) · licence: Apache Software License · rank 13188 · last release 2026-02-09 · [PyPI](https://pypi.org/project/nbdev-scipy/)

<details><summary>README extract</summary>

nbdev docs lookup for the python standard library, scipy, pandas, numpy, django, pytorch, sphinx, and APL.

</details>

### nbdev-django

nbdev docs lookup for django

`pip install nbdev-django` · installs (wheel) · licence: Apache Software License · rank 13359 · last release 2026-02-09 · [PyPI](https://pypi.org/project/nbdev-django/)

<details><summary>README extract</summary>

nbdev docs lookup for the python standard library, scipy, pandas, numpy, django, pytorch, sphinx, and APL.

</details>

### numba-cuda-mlir

numba-cuda-mlir Python Compiler

`pip install numba-cuda-mlir` · installs (wheel) · licence: Apache-2.0 · rank 13459 · last release 2026-10-19 · [PyPI](https://pypi.org/project/numba-cuda-mlir/) · [source](https://github.com/NVIDIA/numba-cuda-mlir)

<details><summary>README extract</summary>

Numba-CUDA-MLIR provides a programming model similar to CUDA C++ in Python. It
is evolved from Numba-CUDA, and is
intended to be compatible with Numba-CUDA kernels.

Numba-CUDA-MLIR aims to interoperate well with existing programming models
whilst also allowing experts sufficient control over code generation.

Example:
```python
import numpy as np
from numba_cuda_mlir import cuda

@cuda.jit
def vector_add(a, b, out):
    i = cuda.grid(1)
    if i < out.shape[0]:
        out[i] = a[i] + b[i]

n = 1_000_000
a = np.ones(n, dtype=np.float32)
b = np.ones(n, dtype=np.float32)
out = np.zeros(n, dtype=np.float32)

threads_per_block = 256
...
```

Sections: Numba-CUDA-MLIR, Quick Start, Migration from Numba / Numba-CUDA, Benchmarks, Licensing

</details>

### nbdev-sphinx

nbdev docs lookup for sphinx

`pip install nbdev-sphinx` · installs (wheel) · licence: Apache Software License · rank 13476 · last release 2026-02-09 · [PyPI](https://pypi.org/project/nbdev-sphinx/)

<details><summary>README extract</summary>

nbdev docs lookup for the python standard library, scipy, pandas, numpy, django, pytorch, sphinx, and APL.

</details>

### nominal-compute

Core functionality for composing compute queries

`pip install nominal-compute` · installs (wheel) · licence: Apache-2.0 · rank 13498 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nominal-compute/)

### nbdev

Create delightful software with Jupyter Notebooks

`pip install nbdev` · installs (wheel) · licence: Apache-2.0 · rank 13517 · last release 2026-11-02 · [PyPI](https://pypi.org/project/nbdev/) · [docs](https://nbdev.fast.ai/) · [source](https://github.com/AnswerDotAI/nbdev)

<details><summary>README extract</summary>

Example:
```python
import some_module
some_module.something()
```

Sections: Getting Started, 🛑Jan 2026 Major Version Update – Breaking Change🛑, How to use nbdev, FAQ, Copyright

</details>

### nbdev-pandas

nbdev docs lookup for pandas

`pip install nbdev-pandas` · installs (wheel) · licence: Apache Software License · rank 13541 · last release 2026-02-09 · [PyPI](https://pypi.org/project/nbdev-pandas/)

<details><summary>README extract</summary>

nbdev docs lookup for the python standard library, scipy, pandas, numpy, django, pytorch, sphinx, and APL.

</details>

### nbdev-pytorch

nbdev docs lookup for PyTorch

`pip install nbdev-pytorch` · installs (wheel) · licence: Apache Software License · rank 13611 · last release 2026-02-09 · [PyPI](https://pypi.org/project/nbdev-pytorch/)

<details><summary>README extract</summary>

nbdev docs lookup for the python standard library, scipy, pandas, numpy, django, pytorch, sphinx, and APL.

</details>

### nvidia-nvimgcodec-cu12

NVIDIA nvimgcodec for CUDA 12.

`pip install nvidia-nvimgcodec-cu12` · installs (wheel) · licence: Apache License 2.0 · rank 13642 · last release 2026-11-03 · [PyPI](https://pypi.org/project/nvidia-nvimgcodec-cu12/)

<details><summary>README extract</summary>

nvImageCodec is a library of accelerated codec with unified interface. It is designed as a framework for extension modules which delivers codec plugins.

You can install the following optional extras:

 - nvjpeg: Includes nvjpeg package dependency, needed to run the nvjpeg extension. ...

</details>

### netgen-mesher

Netgen mesh generator

`pip install netgen-mesher` · installs (wheel) · licence: LGPL-2.1-only · rank 13667 · last release 2026-10-01 · [PyPI](https://pypi.org/project/netgen-mesher/)

_README extract left out: share-alike licence._

### nornir

Pluggable multi-threaded framework with inventory management to help operate collections of devices

`pip install nornir` · installs (wheel) · licence: Apache-2.0 · rank 13764 · last release 2026-10-30 · [PyPI](https://pypi.org/project/nornir/) · [source](https://github.com/nornir-automation/nornir)

<details><summary>README extract</summary>

Nornir is a pure Python automation framework intented to be used directly from Python. While most automation frameworks use their own Domain Specific Language (DSL) which you use to describe what you want to have done, Nornir lets you control everything from Python. ...

Sections: Nornir, Plugins, Documentation, External Resources, Bugs & New features

</details>

### nemo-fabric-adapter-catalog

Metadata-only catalog of bundled NVIDIA NeMo Fabric adapter descriptors

`pip install nemo-fabric-adapter-catalog` · installs (wheel) · licence: Apache-2.0 · rank 13864 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nemo-fabric-adapter-catalog/) · [source](https://github.com/NVIDIA/NeMo-Fabric)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

`nemo-fabric-adapter-catalog` provides release snapshots of the bundled Python and TypeScript adapter descriptors and their registered targets. ...

Sections: NVIDIA NeMo Fabric Adapter Catalog, Metadata Is Not Execution

</details>

### nbdev-apl

nbdev docs lookup for Dyalog APL

`pip install nbdev-apl` · installs (wheel) · licence: Apache Software License · rank 13885 · last release 2026-02-09 · [PyPI](https://pypi.org/project/nbdev-apl/)

<details><summary>README extract</summary>

nbdev docs lookup for the python standard library, scipy, pandas, numpy, django, pytorch, sphinx, and APL.

</details>

### nemo-relay-cli-bin

Prebuilt NeMo Relay command-line interface.

`pip install nemo-relay-cli-bin` · installs (wheel) · licence: Apache-2.0 · rank 13889 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nemo-relay-cli-bin/) · [source](https://github.com/NVIDIA/NeMo-Relay)

<details><summary>README extract</summary>

This platform wheel installs the prebuilt `nemo-relay` command-line interface.

</details>

### nautobot

Source of truth and network automation platform.

`pip install nautobot` · installs (wheel) · licence: Apache-2.0 · rank 13961 · last release 2026-10-27 · [PyPI](https://pypi.org/project/nautobot/) · [docs](https://docs.nautobot.com) · [source](https://github.com/nautobot/nautobot)

<details><summary>README extract</summary>

Nautobot is the open source Network Source of Truth and Network Automation Platform for enterprises operating complex networks at scale.

Network to Code is the sponsor and official steward of Nautobot. ...

Sections: Nautobot, What Nautobot Is, Network Source of Truth, Network Automation Platform, Nautobot Apps and Editions, Screenshots, Nautobot Apps and Extensibility, App Screenshots, Golden Config, Device Lifecycle Management, ChatOps, Application Stack, Providing Feedback, Related projects

</details>

### neovim

Transition packgage for pynvim

`pip install neovim` · installs from source (sdist only) · licence: Apache · rank 13985 · last release 2018-11-17 · [PyPI](https://pypi.org/project/neovim/)

### nebula3-python

Python client for NebulaGraph v3

`pip install nebula3-python` · installs (wheel) · licence: Apache 2.0 · rank 14007 · last release 2024-10-22 · [PyPI](https://pypi.org/project/nebula3-python/)

<details><summary>README extract</summary>

Example:
```python
from nebula3.gclient.net import ConnectionPool
from nebula3.Config import Config

# define a config
config = Config()
config.max_connection_pool_size = 10
# init connection pool
connection_pool = ConnectionPool()
# if the given servers are ok, return true, else return false
ok = connection_pool.init([('127.0.0.1', 9669)], config)

...
```

Sections: NebulaGraph Python Client, Getting Started, Accessing NebulaGraph, Handling Query Results, Jupyter Notebook Integration, Obtaining nebula3-python, Quick Example: Connecting to GraphD Using Graph Client, Using the Session Pool: A Guide, Example: Server-Side Evaluated Parameters, Example: Retrieve Primitive Typed Results, Example: Fetching Query Results into a Pandas DataFrame, Compatibility Matrix, Directory Structure Overview

</details>

### napari-resources

Resources for the napari project.

`pip install napari-resources` · installs (wheel) · licence: BSD License · rank 14043 · last release 2026-09-01 · [PyPI](https://pypi.org/project/napari-resources/) · [source](https://github.com/napari/napari-resources)

<details><summary>README extract</summary>

Graphics and copy resources for the napari project.

For a quick download link to the up-to-date logos, see the dowload section of the latest release.

Example:
```python
from napari_resources import logo_path

svg = logo_path("gradient-plain-dark.svg")
svg.read_bytes()  # the raw SVG
```

Sections: resources, Permissions and usage guidelines, Usage guidelines, logos, Usage, Rasterizing a logo (making an image / PNG), Adding or editing logos, fonts

</details>

### notebooklm-mcp-cli

Unified CLI and MCP server for Google NotebookLM

`pip install notebooklm-mcp-cli` · installs (wheel) · licence: MIT · rank 14055 · last release 2026-11-06 · [PyPI](https://pypi.org/project/notebooklm-mcp-cli/) · [source](https://github.com/jacob-bd/gemini-notebook-mcp-cli)

<details><summary>README extract</summary>

Programmatic access to Gemini Notebook — via command-line interface (CLI) or Model Context Protocol (MCP) server.

> 🚨 New: Protected login storage (recommended)
> Your saved Google login can now be encrypted, with its key kept in your computer's keychain instead of a plain file. ...

Features:
| Capability | CLI Command | MCP Tool |

| List notebooks | `nlm notebook list` | `notebook_list` |
| Create notebook | `nlm notebook create` | `notebook_create` |
| Add Sources (URL, Text, Drive, File) | `nlm source add` | `source_add` |
| Query ...

...

</details>

### NLPPlus

Python extension for the NLP++ text analysis engine

`pip install NLPPlus` · installs from source (sdist only) · licence: MIT License · rank 14229 · last release 2026-11-06 · [PyPI](https://pypi.org/project/NLPPlus/) · [source](https://github.com/VisualText/py-package-nlpengine)

<details><summary>README extract</summary>

NLP++ lets you build fully customized text analyzers using the NLP++ VSCode language extension, giving you 100% visibility into — and complete control over — every rule and decision your analyzer makes. ...

Example:
```python
import NLPPlus
# from a Python object
NLPPlus.put_json_object("myanalyzer", {"company": {"name": "Acme"}}, "company")
# or from an existing JSON file
NLPPlus.put_json_file("myanalyzer", "data/company.json")
# then analyze — the json2kbb pass builds company.kbb into the KB first
NLPPlus.analyze("some text", "myanalyzer")
```

...

</details>

### nvidia-ncore

A unified data format and library for AV / robotics

`pip install nvidia-ncore` · installs (wheel) · licence: Apache-2.0 · rank 14342 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-ncore/)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

A unified data format and library for autonomous vehicle and robotics sensor data.

Features:
- Neural Reconstruction - Designed for data-driven neural 3D reconstruction and simulation applications
- Data Format - Canonical and extensible component-based data format optimized for efficient training ...

Sections: nvidia-ncore, Features, Documentation

</details>

### nd2

Yet another nd2 (Nikon NIS Elements) file reader

`pip install nd2` · installs (wheel) · licence: BSD License · rank 14444 · last release 2026-09-29 · [PyPI](https://pypi.org/project/nd2/) · [docs](https://tlambert03.github.io/nd2/) · [source](https://github.com/tlambert03/nd2)

<details><summary>README extract</summary>

`.nd2` (Nikon NIS Elements) file reader.

This reader provides a pure python implementation of the Nikon ND2 SDK.

> It _used_ to wrap the official SDK with Cython, but has since been completely
> rewritten to be pure python (for performance, ease of distribution, and
> maintenance) while retaining complete API parity with the official SDK. ...

Example:
```python
import nd2
import numpy as np

my_array = nd2.imread('some_file.nd2')                          # read to numpy array
my_array = nd2.imread('some_file.nd2', dask=True)               # read to dask array
my_array = nd2.imread('some_file.nd2', xarray=True)             # read to xarray
...
```

Sections: nd2, book: Documentation, Faster XML parsing, Usage and API, Metadata structures, alternatives

</details>

### nostr-sdk

Nostr protocol implementation, Relay, RelayPool, high-level client library, NWC client and more.

`pip install nostr-sdk` · installs (wheel) · licence: not stated · rank 14472 · last release 2026-08-19 · [PyPI](https://pypi.org/project/nostr-sdk/) · [docs](https://nostrdevkit.org) · [source](https://github.com/nostrdevkit/nostr-sdk-ffi)

<details><summary>README extract</summary>

Nostr protocol implementation, Relay, RelayPool, high-level client library, NWC client and more.

Learn more about at <

Sections: Nostr SDK, Description, Documentation, State

</details>

### nonecap

Official Python client for NoneCap, the hCaptcha solver API.

`pip install nonecap` · installs (wheel) · licence: MIT · rank 14638 · last release 2026-10-31 · [PyPI](https://pypi.org/project/nonecap/) · [docs](https://nonecap.com/api-reference) · [source](https://github.com/nonecap/nonecap-py)

<details><summary>README extract</summary>

Official Python client for the NoneCap hCaptcha solver API.

Submit a captcha, get back a token. The client handles the polling, the timeouts, and the error cases so you don't write the request loop yourself. Sync and async, fully typed.

Example:
```python
from nonecap import NoneCap

nc = NoneCap(api_key="nc_live...")

solve = nc.solve(
    type="hcaptcha",
    sitekey="10000000-ffff-ffff-ffff-000000000001",
    url="
)

print(solve.token)  # the hCaptcha token, ready to submit
print(solve.resp_key)  # hcaptcha.getRespKey() equivalent, for sites that verify the pair
...
```

...

</details>

### netapp-lib

netapp-lib is required for Ansible deployments to interact with NetApp storage systems.

`pip install netapp-lib` · installs (wheel) · licence: Apache License, Version 2.0 · rank 14645 · last release 2021-08-03 · [PyPI](https://pypi.org/project/netapp-lib/)

### newick

A python module to read and write the Newick format

`pip install newick` · installs (wheel) · licence: Apache Software License · rank 14690 · last release 2026-01-14 · [PyPI](https://pypi.org/project/newick/)

<details><summary>README extract</summary>

python package to read and write the
Newick format.

Since Newick specifies a format for a set of trees, all functions to read Newick return
a `list` of `newick.Node` objects.

Example:
```python
>>> from newick import loads
>>> trees = loads('(A,B,(C,D)E)F;')
>>> trees[0].name
'F'
>>> [n.name for n in trees[0].descendants]
['A', 'B', 'E']
```

Sections: python-newick, Reading Newick, Quoted node labels, Additional information in comments

</details>

### neuralprophet

NeuralProphet is an easy to learn framework for interpretable time series forecasting.

`pip install neuralprophet` · does not install on CPython 3.14 · licence: MIT License · rank 14716 · last release 2024-06-21 · [PyPI](https://pypi.org/project/neuralprophet/)

<details><summary>README extract</summary>

Please note that the project is still in beta phase. Please report any issues you encounter or suggestions you have. We will do our best to address them quickly. Contributions are very welcome!

NeuralProphet is an easy to learn framework for interpretable time series forecasting. ...

Example:
```python
from neuralprophet import NeuralProphet
```

Sections: NeuralProphet: human-centered forecasting, Documentation, Discussion and Help, Slack Chat, Tutorials, Minimal example, Features, Model components, Framework features, Coming soon:tm, About

</details>

### nvforest-cu12

nvForest

`pip install nvforest-cu12` · installs (wheel) · licence: Apache-2.0 · rank 14799 · last release 2026-10-08 · [PyPI](https://pypi.org/project/nvforest-cu12/) · [docs](https://docs.rapids.ai/api/nvforest/stable/)

### nvidia-nat-mcp

Subpackage for MCP client integration in NeMo Agent Toolkit

`pip install nvidia-nat-mcp` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 14936 · last release 2026-09-10 · [PyPI](https://pypi.org/project/nvidia-nat-mcp/) · [docs](https://docs.nvidia.com/nemo/agent-toolkit/latest/) · [source](https://github.com/NVIDIA/NeMo-Agent-Toolkit)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2025-2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at ...

Features:
- Connect to MCP servers via streamable-http, SSE, or stdio transports
- Wrap individual MCP tools as NeMo Agent Toolkit functions
- Connect to MCP servers and dynamically discover available tools ...

Sections: NVIDIA NeMo Agent Toolkit MCP Subpackage, Features

</details>

