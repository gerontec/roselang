# Unclassified / P (part 2 of 3)

[Index](README.md) · 979 packages in this topic, by downloads.

[part 1](unclassified-p.md) · part 2 · [part 3](unclassified-p-3.md)

### pytest-html-merger

Pytest HTML reports merging utility

`pip install pytest-html-merger` · installs (wheel) · licence: not stated · rank 7564 · last release 2024-07-12 · [PyPI](https://pypi.org/project/pytest-html-merger/)

### pulumi-pulumiservice

A native Pulumi package for creating and managing Pulumi Cloud constructs.

`pip install pulumi-pulumiservice` · installs (wheel) · licence: Apache-2.0 · rank 7608 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pulumi-pulumiservice/) · [source](https://github.com/pulumi/pulumi-pulumiservice)

### portal

Fast and reliable distributed systems in Python

`pip install portal` · installs (wheel) · licence: MIT · rank 7623 · last release 2026-10-25 · [PyPI](https://pypi.org/project/portal/)

<details><summary>README extract</summary>

Fast and reliable distributed systems in Python.

Features:
- 📡 Communication: Portal lets you bind functions to a `Server` and call
 them from one or more `Client`s. Wait on results via `Future` objects.
 Clients can automatically restore broken connections. ...

Example:
```python
def server():
  import portal
  server = portal.Server(2222)
  server.bind('add', lambda x, y: x + y)
  server.bind('greet', lambda msg: print('Message from client:', msg))
  server.start()

def client():
  import portal
  client = portal.Client('localhost:2222')
  future = client.add(12, 42)
  result = future.result()
  print(result)  # 54
...
```

Sections: 🌀 Portal, Features, Example, Questions

</details>

### python-dynamodb-lock

Python library that emulates the java-based dynamo-db-client from awslabs

`pip install python-dynamodb-lock` · installs (wheel) · licence: Apache Software License · rank 7635 · last release 2018-10-28 · [PyPI](https://pypi.org/project/python-dynamodb-lock/)

<details><summary>README extract</summary>

This is a general purpose distributed locking library built on top of DynamoDB. It is heavily
"inspired" by the java-based AmazonDynamoDBLockClient
library, and supports both coarse-grained and fine-grained locking.

* Free software: Apache Software License 2.0

Features:
* Acquire named locks - with configurable retry semantics
* Periodic heartbeat/update for the locks to keep them alive
* Auto-release the locks if there is no heartbeat for a configurable lease-duration
* Notify an app-callback function if the lock ...

Sections: Python DynamoDB Lock, Features, Consistency Notes, 0.9.0 (2018-10-28)

</details>

### pulumi-policy

Pulumi's Policy Python SDK

`pip install pulumi-policy` · installs (wheel) · licence: Apache 2.0 · rank 7647 · last release 2026-05-20 · [PyPI](https://pypi.org/project/pulumi-policy/)

<details><summary>README extract</summary>

Features:
Define and manage policy for cloud resources deployed through Pulumi.

Policy rules run during `pulumi preview` and `pulumi up`, asserting that cloud resource definitions
comply with the policy immediately before they are created or updated. ...

Sections: Pulumi Policy SDK, Overview, Getting Started, Documentation, Examples, Languages

</details>

### proxsuite

Quadratic Programming Solver for Robotics and beyond.

`pip install proxsuite` · installs (wheel) · licence: BSD-2-Clause · rank 7666 · last release 2026-10-29 · [PyPI](https://pypi.org/project/proxsuite/) · [source](https://github.com/cmake-wheel/proxsuite.git)

<details><summary>README extract</summary>

ProxSuite is a collection of open-source, numerically robust, precise, and efficient numerical solvers (e.g., LPs, QPs, etc.) rooted in revisited primal-dual proximal algorithms.
Through ProxSuite, we aim to offer the community scalable optimizers that deal with dense, sparse, or matrix-free problems. ...

Sections: ProxSuite, ProxSuite main features, Documentation, Getting started, Alternative approaches, Compiling a first example program, Using ProxSuite with CMake, ProxQP, Citing ProxQP, Numerical benchmarks, QPLayer, Citing QPLayer, Core-dev team

</details>

### pgspecial

Meta-commands handler for Postgres Database.

`pip install pgspecial` · installs (wheel) · licence: BSD · rank 7675 · last release 2025-04-28 · [PyPI](https://pypi.org/project/pgspecial/)

<details><summary>README extract</summary>

This package provides an API to execute meta-commands (AKA "special", or
"backslash commands") on PostgreSQL.

Example:
```python
from pgspecial.main import PGSpecial
from pgspecial.namedqueries import NamedQueries
```

Sections: Meta-commands for Postgres, Quick Start, Usage, Projects using it

</details>

### py-clob-client-v2

Python client for the Polymarket CLOBV2

`pip install py-clob-client-v2` · installs (wheel) · licence: MIT License · rank 7677 · last release 2026-10-15 · [PyPI](https://pypi.org/project/py-clob-client-v2/)

<details><summary>README extract</summary>

> [!WARNING]
> This package is deprecated. Please migrate to the unified Polymarket SDK. Follow the migration guide to get started.

Python client for the Polymarket CLOB (v2)

Example:
```python
# pip install py_clob_client_v2

import os
from py_clob_client_v2 import ApiCreds, ClobClient, OrderArgs, OrderType, PartialCreateOrderOptions, Side

host = "<polymarket-clob-host>"
chain_id = 137  # or 80002 for Amoy testnet

# Step 1: obtain API credentials using your wallet (L1 auth)
...
```

Sections: PY Polymarket CLOB Client V2, Usage, Market Orders, Authentication

</details>

### pyodide-py

A Python package providing core interpreter functionality for Pyodide

`pip install pyodide-py` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 7684 · last release 2026-09-14 · [PyPI](https://pypi.org/project/pyodide-py/) · [docs](https://pyodide.org/en/stable/)

<details><summary>README extract</summary>

A Python package providing core interpreter functionality for Pyodide.

This package is an integral part of the Pyodide runtime which cannot start
without it. Install in a native Python for type checking or testing purposes. ...

</details>

### PyKMIP

KMIP library

`pip install PyKMIP` · installs (wheel) · licence: Apache Software License · rank 7695 · last release 2026-09-09 · [PyPI](https://pypi.org/project/PyKMIP/)

<details><summary>README extract</summary>

PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP), an OASIS communication standard for the management of
objects stored and maintained by key management systems. KMIP defines how key
management operations and operation data should be encoded and communicated
between client and server applications. ...

</details>

### pydantic-partial

Create partial models from your pydantic models. Partial models may allow None for certain or all fields.

`pip install pydantic-partial` · installs (wheel) · licence: MIT · rank 7730 · last release 2026-06-26 · [PyPI](https://pypi.org/project/pydantic-partial/) · [source](https://github.com/team23/pydantic-partial)

<details><summary>README extract</summary>

Example:
```python
import pydantic
from pydantic_partial import PartialModelMixin

# Something model, then can be used as a partial, too:
class Something(PartialModelMixin, pydantic.BaseModel):
    name: str
    age: int

# Create a full partial model
FullSomethingPartial = Something.model_as_partial()
...
```

Sections: pydantic-partial, About, Usage example, Without using the mixin, Only changing some fields to being optional, Recursive partials, Known limitations

</details>

### pykrx

KRX data scraping

`pip install pykrx` · installs (wheel) · licence: MIT License · rank 7734 · last release 2026-09-19 · [PyPI](https://pypi.org/project/pykrx/)

<details><summary>README extract</summary>

한국 증권시장(KRX, Naver)에서 주식·채권 데이터를 스크래핑하는 Python 라이브러리입니다.

프로젝트가 도움이 되셨다면 개발자를 응원해주세요!

* 본 라이브러리는 KRX(한국거래소) 및 Naver의 데이터를 스크래핑하며, 데이터의 저작권은 각 제공처에 있습니다.
* 도의적으로 무분별한 API 호출을 자제해 주시기 바랍니다.
* 제공되는 데이터는 공식 데이터와 차이가 있을 수 있으며, 참고용으로만 사용해야 합니다.
* 투자 손실이나 법적 책임은 사용자에게 있으며, 상업적 용도 사용 시 데이터 제공처의 약관을 준수해야 합니다. ...

Example:
```python
tickers = stock.get_market_ticker_list("20190225")
print(tickers)
```

Sections: PyKrx, ☕ 후원하기, ⚠️ 면책 및 주의사항, 1 환경설정, 1.3 환경변수 설정 (Required Environment Variables), 지원 Python 버전, 2. API 설명, 2.1.1 MarketData API, 2.1.1.1 Ticker 조회, 2.1.1.2 일자별 OHLCV 조회, 2.1.1.3 전체 종목 시세 조회, 2.1.1.4 모든 종목의 가격 변동 조회, 2.1.1.5 종목별 DIV/BPS/PER/EPS 조회, 2.1.1.6 일자별 DIV/BPS/PER/EPS 조회

</details>

### pyvex

A Python interface to libVEX and VEX IR

`pip install pyvex` · installs (wheel) · licence: BSD-2-Clause AND GPL-2.0-or-later · rank 7747 · last release 2026-10-22 · [PyPI](https://pypi.org/project/pyvex/) · [source](https://github.com/angr/pyvex)

_README extract left out: share-alike licence._

### pyiosbackup

A python parser for iOS backups

`pip install pyiosbackup` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 7754 · last release 2026-02-02 · [PyPI](https://pypi.org/project/pyiosbackup/)

_README extract left out: share-alike licence._

### pycocoevalcap

MS-COCO Caption Evaluation for Python 3

`pip install pycocoevalcap` · installs (wheel) · licence: not stated · rank 7761 · last release 2020-11-18 · [PyPI](https://pypi.org/project/pycocoevalcap/)

<details><summary>README extract</summary>

Evaluation codes for MS COCO caption generation.

This repository provides Python 3 support for the caption evaluation metrics used for the MS COCO dataset.

The code is derived from the original repository that supports Python 2.7:
Caption evaluation depends on the COCO API that natively supports Python 3.

- Java 1.8.0
- Python 3

Sections: Microsoft COCO Caption Evaluation, Description, Requirements, Usage, Files, Setup, References

</details>

### pismosendlogs

A library to send logs

`pip install pismosendlogs` · installs from source (sdist only) · licence: BSD 2-clause · rank 7766 · last release 2024-03-05 · [PyPI](https://pypi.org/project/pismosendlogs/)

### polylith-cli

Python tooling support for the Polylith Architecture

`pip install polylith-cli` · installs (wheel) · licence: MIT License · rank 7805 · last release 2026-10-04 · [PyPI](https://pypi.org/project/polylith-cli/) · [source](https://github.com/davidvujic/python-polylith)

<details><summary>README extract</summary>

A command line interface that adds tooling support for the Polylith Architecture in Python.

Have a look at the documentation.
You will find installation, setup, usage guides and more.

Sections: Python tooling for Polylith, Documentation, Quick start, Setup for Hatch users, Ready for coding!, Setup for PDM users, Add a workspace hook, Add the polylith-cli, Setup for Rye users, Setup for uv users, Rye and uv users: edit the configuration, Rye and uv users: ready for coding!

</details>

### pyston

A JIT for Python

`pip install pyston` · does not install on CPython 3.14 · licence: not stated · rank 7836 · last release 2022-10-28 · [PyPI](https://pypi.org/project/pyston/)

<details><summary>README extract</summary>

This is the package for Pyston "lite", the JIT part of Pyston,
a faster implementation of Python. Pyston lite does not contain all of the
optimizations of full Pyston, but it is still 10-25% faster on many workloads.

Pyston lite is currently only available for Python 3.7-3.10

</details>

### python-neutronclient

CLI and Client Library for OpenStack Networking

`pip install python-neutronclient` · installs (wheel) · licence: Apache Software License · rank 7850 · last release 2026-08-26 · [PyPI](https://pypi.org/project/python-neutronclient/)

<details><summary>README extract</summary>

This is a client library for Neutron built on the Neutron API. It
provides a Python API (the `neutronclient` module).

* License: Apache License, Version 2.0
* PyPi - package installation
* Online Documentation
* Launchpad project - release management
* Blueprints - feature specifications
* Bugs - issue tracking
* Source
* Developer's Guide

Sections: Team and repository tags, Python bindings to the Neutron API

</details>

### portforward

Easy Kubernetes Port-Forward For Python

`pip install portforward` · installs (wheel) · licence: MIT License · rank 7852 · last release 2026-01-29 · [PyPI](https://pypi.org/project/portforward/) · [docs](https://portforward.readthedocs.io) · [source](https://github.com/pytogo/portforward.git)

<details><summary>README extract</summary>

Easy Kubernetes Port-Forward For Python

* Free software: MIT license

Features:
* Native Kubernetes port-forwarding with the `.kube/config` from the home dir
 or any other path to config.
* Portforward for pods and services - the lib will first look for a pod with matching name then for
 a service
* Waiting for a pod to become ...

Example:
```python
import requests

import portforward

def main():
    namespace = "test"
    pod_name = "web"  # You can also use a service name instead
    local_port = 9000  # from port
    pod_port = 80  # to port

    # No path to kube config provided - will use default from $HOME/.kube/config
...
```

Sections: portforward, Quickstart, Features

</details>

### pyston-autoload

Automatically loads and enables pyston

`pip install pyston-autoload` · does not install on CPython 3.14 · licence: not stated · rank 7869 · last release 2022-10-28 · [PyPI](https://pypi.org/project/pyston-autoload/)

<details><summary>README extract</summary>

pyston_autoload is a small package that simply imports and enables
pyston on python startup. It is possible
to use pyston without this autoload package, but it is generally
recommended to install the autoloader to automatically get the performance
benefits

</details>

### pytest-insta

A practical snapshot testing plugin for pytest

`pip install pytest-insta` · installs (wheel) · licence: not stated · rank 7873 · last release 2025-11-22 · [PyPI](https://pypi.org/project/pytest-insta/)

<details><summary>README extract</summary>

> A practical snapshot testing plugin for pytest.

Snapshot testing makes it easy to monitor and approve changes by comparing the result of an operation against a previous reference value.

This project borrows from a lot of other implementations to provide a pythonic, batteries included snapshot testing solution. ...

Features:
- Expressive and familiar assertion syntax
- Can format text, binary, hexdump, json and pickle snapshots out-of-the-box
- Can be extended with custom snapshot formats
- Interactive review tool for inspecting and approving changes

Example:
```python
def test_hello_world(snapshot):
    assert snapshot() == "hello"
```

Sections: pytest-insta, Introduction, Features, Getting Started, Snapshot Formats, Command-line Options, Caveats

</details>

### pdftext

Extract structured text from pdfs quickly

`pip install pdftext` · installs (wheel) · licence: Apache Software License · rank 7879 · last release 2026-07-08 · [PyPI](https://pypi.org/project/pdftext/) · [source](https://github.com/VikParuchuri/pdftext)

<details><summary>README extract</summary>

Text extraction like PyMuPDF, but without the AGPL license. PDFText extracts plain text or structured blocks and lines. It's built on pypdfium2, so it's fast, accurate, and Apache licensed.

Example:
```python
from pdftext.extraction import plain_text_output

text = plain_text_output(PDF_PATH, sort=False, hyphens=False, page_range=[1,2,3]) # Optional arguments explained above
```

Sections: PDFText, Usage, Plain text, JSON, Programmatic usage, Concurrency, Benchmarks, Methodology, Running benchmarks, How it works

</details>

### pdfservices-sdk

Adobe PDFServices Client Library

`pip install pdfservices-sdk` · installs (wheel) · licence: Apache Software License · rank 7912 · last release 2026-08-10 · [PyPI](https://pypi.org/project/pdfservices-sdk/)

<details><summary>README extract</summary>

Adobe PDF Services SDK allows you to access RESTful APIs to create, convert, and manipulate PDFs within your applications. Adobe PDF Services API provides access to over 15 different services including:
- Document Generation: Build PDF and Word documents from Word templates and your own data
- Tag PDF files to make them more accessible. ...

</details>

### pemja

PemJa

`pip install pemja` · installs from source (sdist only) · licence: Apache Software License · rank 7914 · last release 2026-10-17 · [PyPI](https://pypi.org/project/pemja/)

<details><summary>README extract</summary>

PemJa is an open source cross language call framework based on FFI. It aims to provide a high-performance

framework of calling between different languages.

Python binary installers for the latest released version are available at the Python package index

Java Maven Dependency

Sections: PemJa, What is it?, Where to get it, Usage, Documentation

</details>

### packaging-legacy

Core utilities for legacy Python packages

`pip install packaging-legacy` · installs (wheel) · licence: Apache Software License; BSD License · rank 7920 · last release 2023-11-28 · [PyPI](https://pypi.org/project/packaging-legacy/) · [source](https://github.com/di/packaging_legacy)

<details><summary>README extract</summary>

This library provides support for "legacy" Python Packaging functionality
removed from

Sections: Legacy Packaging, `LegacyVersion`

</details>

### python-dxf

Package for accessing a Docker v2 registry

`pip install python-dxf` · installs (wheel) · licence: MIT · rank 7956 · last release 2025-05-05 · [PyPI](https://pypi.org/project/python-dxf/)

<details><summary>README extract</summary>

Python module and command-line tool for storing and retrieving data in a
Docker registry.

- Store arbitrary data (blob-store)
- Content addressable
- Set up named aliases to blobs
- Supports Docker registry schema v2
- Works on Python 3.8+ ...

Example:
```python
from dxf import DXF

def auth(dxf, response):
    dxf.authenticate('fred', 'somepassword', response=response)

dxf = DXF('registry-1.docker.io', 'fred/datalogger', auth)

dgst = dxf.push_blob('logger.dat')
dxf.set_alias('may15-readings', dgst)

assert dxf.get_alias('may15-readings') == [dgst]

for chunk in dxf.pull_blob(dgst):
...
```

Sections: Usage, Certificates, Authentication tokens, Docker Cloud authentication

</details>

### pulumi-esc-sdk

ESC (Environments, Secrets, Config) API

`pip install pulumi-esc-sdk` · installs (wheel) · licence: Apache 2.0 · rank 7968 · last release 2026-06-15 · [PyPI](https://pypi.org/project/pulumi-esc-sdk/)

<details><summary>README extract</summary>

Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.

</details>

### python-registry

Read access to Windows Registry files.

`pip install python-registry` · installs (wheel) · licence: Apache Software License · rank 7969 · last release 2019-05-08 · [PyPI](https://pypi.org/project/python-registry/)

### pytest-integration

Organizing pytests by integration or not

`pip install pytest-integration` · installs (wheel) · licence: MIT License · rank 7981 · last release 2022-11-17 · [PyPI](https://pypi.org/project/pytest-integration/) · [source](https://github.com/jbwdevries/pytest-integration)

<details><summary>README extract</summary>

Overview

Plugin for pytest to mark tests as
integration or slow integration.

Integration tests are run after normal tests (unit tests) and
slow integration tests are run after (quick) integration tests.

If a unit test fails, (quick) integration and slow integration tests are not run. ...

</details>

### placebo

Make boto3 calls that look real but have no effect

`pip install placebo` · installs from source (sdist only) · licence: Apache Software License · rank 7984 · last release 2021-09-28 · [PyPI](https://pypi.org/project/placebo/)

<details><summary>README extract</summary>

Placebo allows you to mock boto3 calls that look just like normal calls but
actually have no effect at all. It does this by allowing you to record a set
of calls and save them to a data file and then replay those calls later
(e.g. in a unit test) without ever hitting the AWS endpoints.

Installation

~~~
$ pip install placebo
~~~

Quickstart ...

Example:
```python
pill = pill = placebo.attach(session, record_format="pickle")
```

Sections: placebo, ... more lambda calls ..., ... mocked response will be returned, Attaching to the default session, Now make Boto3 calls using the default session., Using pickle, Manual Mocking, Usage as a decorator

</details>

### python-magic-standalone

File type identification using libmagic

`pip install python-magic-standalone` · installs (wheel) · licence: MIT License · rank 8010 · last release 2026-10-29 · [PyPI](https://pypi.org/project/python-magic-standalone/)

<details><summary>README extract</summary>

This package `python-magic-standalone` is an unofficial distribution of python-magic.
It is built directly from @ddelange’s `abi3-wheels` branch, which is the subject of open PR #294. It provides prebuilt wheels with libmagic bundled for Windows, macOS, and Linux. ...

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

...

</details>

### prodigyopt

An Adam-like optimizer for neural networks with adaptive estimation of learning rate

`pip install prodigyopt` · installs (wheel) · licence: MIT License · rank 8012 · last release 2025-01-16 · [PyPI](https://pypi.org/project/prodigyopt/)

<details><summary>README extract</summary>

This is the official repository used to run the experiments in the paper that proposed the Prodigy optimizer. The optimizer is implemented in PyTorch.
There is also a JAX version of Prodigy in Optax, which currently does not have the `slice_p` argument.

Prodigy: An Expeditiously Adaptive Parameter-Free Learner
*K. Mishchenko, A. Defazio*
Paper:

Example:
```python
We do not recommend using restarts in cosine annealing, so we suggest setting `T_max=total_steps`, where
`total_steps` should be the number of times `scheduler.step()` is called. If you do use restarts, we highly
recommend setting `safeguard_warmup=True`.

Extra care should be taken if you use linear warm-up at the beginning:
...
```

...

</details>

### python-glanceclient

OpenStack Image API Client Library

`pip install python-glanceclient` · installs (wheel) · licence: Apache Software License · rank 8029 · last release 2026-08-27 · [PyPI](https://pypi.org/project/python-glanceclient/)

<details><summary>README extract</summary>

This is a client library for Glance built on the OpenStack Images API. It provides a Python API (the `glanceclient` module) and a command-line tool (`glance`). This library fully supports the v1 Images API, while support for the v2 API is in progress.

Development takes place via the usual OpenStack processes as outlined in the developer guide. ...

Sections: Team and repository tags, Python bindings to the OpenStack Images API

</details>

### pymagnitude-light

Magnitude fork that only supports Word2Vec, GloVe and fastText embeddings

`pip install pymagnitude-light` · installs (wheel) · licence: MIT · rank 8037 · last release 2020-11-13 · [PyPI](https://pypi.org/project/pymagnitude-light/)

### poselib

RANSAC + collection of minimal solvers for camera pose estimation.

`pip install poselib` · installs (wheel) · licence: not stated · rank 8046 · last release 2025-08-27 · [PyPI](https://pypi.org/project/poselib/)

<details><summary>README extract</summary>

This library provides a collection of minimal solvers for camera pose estimation. The focus is on calibrated absolute pose estimation problems from different types of correspondences (e.g. point-point, point-line, line-point, line-line). ...

Example:
```python
camera = {'model': 'SIMPLE_PINHOLE', 'width': 1200, 'height': 800, 'params': [960, 600, 400]}

pose, info = poselib.estimate_absolute_pose(p2d, p3d, camera, {'max_reproj_error': 16.0}, {})
```

Sections: PoseLib, Robust Estimation and Non-linear Refinement, Camera models, Python bindings, Storing poses and estimated camera parameters, Benchmarking the robust estimators, Minimal Solvers, Naming convention, Calling conventions, Generalized Cameras, Upright Solvers, Implemented solvers, Absolute Pose, Relative Pose

</details>

### pyevtk

Export data as binary VTK files

`pip install pyevtk` · installs (wheel) · licence: MIT · rank 8053 · last release 2026-05-28 · [PyPI](https://pypi.org/project/pyevtk/)

<details><summary>README extract</summary>

This package in its entirety belongs to Paulo Herrera and its currently hosted under:

I've misappropriated, well forked and repackaged really, this package in order to host it on PyPI and allow for its easy distribution and installation as I use it a lot. I take no credit whatsoever for it.

My fork is hosted under: ...

Sections: PREAMBLE, INTRODUCTION, DOCUMENTATION, DESIGN GUIDELINES, REQUIREMENTS

</details>

### pick

Pick an option in the terminal with a simple GUI

`pip install pick` · installs (wheel) · licence: MIT License · rank 8072 · last release 2026-02-28 · [PyPI](https://pypi.org/project/pick/)

<details><summary>README extract</summary>

pick is a small python library to help you create interactive
selection list in the terminal.

| Basic | Multiselect |

| | |

Sections: pick, Optional: `blessed` backend, Usage, Options

</details>

### pydomo

The official Python3 Domo API SDK - Domo, Inc.

`pip install pydomo` · installs (wheel) · licence: MIT · rank 8102 · last release 2025-11-12 · [PyPI](https://pypi.org/project/pydomo/)

### pycaw

Python Core Audio Windows Library

`pip install pycaw` · installs (wheel) · licence: MIT · rank 8104 · last release 2026-09-26 · [PyPI](https://pypi.org/project/pycaw/) · [docs](https://andremiras.github.io/pycaw/) · [source](https://github.com/AndreMiras/pycaw.git)

<details><summary>README extract</summary>

Pycaw is a Python library designed exclusively for controlling audio devices on Windows systems.
It allows programmatic access to audio sessions, volume control, and sound device management on the Windows platform.

> Note: Pycaw does not support macOS or Linux.
> It is built specifically for Windows using Core Audio APIs. ...

Example:
```python
from pycaw.pycaw import AudioUtilities
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
print(f"Audio output: {device.FriendlyName}")
print(f"- Muted: {bool(volume.GetMute())}")
print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
...
```

Sections: Pycaw (Python Core Audio Windows), Usage, Tests

</details>

### promb

promb: protein mutation burden

`pip install promb` · installs (wheel) · licence: MIT · rank 8122 · last release 2025-05-17 · [PyPI](https://pypi.org/project/promb/)

<details><summary>README extract</summary>

Python library for computing protein humanness (or mouse-ness, dog-ness, cow-ness, ...) based on average number of mutations
to nearest peptide in a reference proteome (Human SwissProt, human antibody repertoires in OAS, or a custom reference DB).

Example:
```python
from promb import init_db
# Use pre-defined Human reference proteome (UP000005640)
db = init_db('human-reference', 9)
# Use pre-defined Human SwissProt DB
db = init_db('human-swissprot', 9)
# Use pre-defined Human OAS DB (antibody peptides found in >=10% of subjects)
db = init_db('human-oas')
# Use custom path with gzipped fasta file
...
```

Sections: promb: protein humanness evaluation toolkit, How does this work? What is protein humanness?, Usage, Command-line interface, Python library

</details>

### py-tgcalls

Async client API for the Telegram Calls.

`pip install py-tgcalls` · installs (wheel) · licence: not stated · rank 8151 · last release 2026-09-25 · [PyPI](https://pypi.org/project/py-tgcalls/) · [docs](https://pytgcalls.github.io/PyTgCalls) · [source](https://github.com/pytgcalls/pytgcalls.git)

<details><summary>README extract</summary>

A simple and elegant client that allows you to make group voice calls quickly and easily.

 Examples


 Documentation


 PyPi


 Channel


 Chat

This project allows making Telegram call using MtProto and WebRTC, this is possible thanks to the power of [NTgCalls] library and [@evgeny-nadymov]

Features:
- Prebuilt wheels for macOS, Linux and Windows.
- Supporting all type of MTProto libraries: Pyrogram, Telethon and Hydrogram.
- Work with voice chats in channels and chats.
- Join as channels or chats. ...

Example:
```python
from pytgcalls import PyTgCalls
from pytgcalls import idle

...
chat_id = -1001185324811
app = PyTgCalls(client)
app.start()
app.play(
    chat_id,
    '
)
idle()
```

Sections: PyTgCalls, Example Usage, Features, Requirements, Special Thanks

</details>

### pytest-tinybird

A pytest plugin to report test results to tinybird

`pip install pytest-tinybird` · installs (wheel) · licence: MIT · rank 8167 · last release 2025-05-07 · [PyPI](https://pypi.org/project/pytest-tinybird/)

<details><summary>README extract</summary>

A pytest plugin to report test results to Tinybird. At the end of every run, this plugin posts results using the Tinybird Events API.

Requirements

- Python >=3.8
- pytest 3.8 or newer (previous versions might be compatible)
- Tinybird account and a token with append permissions

Installation

pypi install package: ...

</details>

### PyExecJS

Run JavaScript code from Python

`pip install PyExecJS` · installs from source (sdist only) · licence: MIT License · rank 8172 · last release 2018-01-18 · [PyPI](https://pypi.org/project/PyExecJS/)

<details><summary>README extract</summary>

This library is no longer maintananced. Bugs are not be fixed (even if
they are trivial or essential).

We suggest to use other library or to make a fork.

Run JavaScript code from Python.

PyExecJS is a porting of ExecJS from Ruby. PyExecJS automatically
picks the best runtime available to evaluate your JavaScript program.

A short example:

Example:
```python
>>> import execjs
>>> execjs.eval("'red yellow blue'.split(' ')")
['red', 'yellow', 'blue']
>>> ctx = execjs.compile("""
...     function add(x, y) {
...         return x + y;
...     }
... """)
>>> ctx.call("add", 1, 2)
3
```

Sections: PyExecJS (EOL), End of life, Details, 1.5.0, 1.4.1, 1.4.0, 1.3.1, 1.3.0, 1.2.0, 1.1.0, 1.0.5, 1.0.4, 1.0.3, 1.0.2

</details>

### pretty-errors

Prettifies Python exception output to make it legible.

`pip install pretty-errors` · installs (wheel) · licence: MIT License · rank 8191 · last release 2021-11-24 · [PyPI](https://pypi.org/project/pretty-errors/)

<details><summary>README extract</summary>

Prettifies Python exception output to make it legible. Install it with

If you want `pretty_errors` to be used whenever you run a python script you must add it to your python startup procedure. ...

Example:
```python
import pretty_errors
```

Sections: pretty-errors, Scraping STDERR, Whitelist / Blacklist, Pathed Configurations, Environment Variables, Configuration settings, Further customization

</details>

### pyhelm3

Python library for managing Helm releases using Helm 3 and later (i.e. Tiller-less Helm).

`pip install pyhelm3` · installs (wheel) · licence: Apache-2.0 · rank 8211 · last release 2026-10-19 · [PyPI](https://pypi.org/project/pyhelm3/)

<details><summary>README extract</summary>

Python library for managing Helm releases using Helm 3 and later (i.e. Tiller-less Helm).

Example:
```python
from pyhelm3 import Client

# This will use the Kubernetes configuration from the environment
client = Client()
# Specify the kubeconfig file to use
client = Client(kubeconfig = "/path/to/kubeconfig")
# Specify the kubecontext to use
client = Client(kubecontext = "kubecontext")
...
```

Sections: pyhelm3, Usage

</details>

### pycadf

CADF Library

`pip install pycadf` · installs (wheel) · licence: Apache Software License · rank 8216 · last release 2026-07-09 · [PyPI](https://pypi.org/project/pycadf/) · [source](https://opendev.org/openstack/pycadf)

<details><summary>README extract</summary>

This library provides an auditing data model based on the Cloud Auditing Data
Federation specification, primarily for
use by OpenStack. The goal is to establish strict expectations about what
auditors can expect from audit notifications. ...

</details>

### polygraphy

Polygraphy: A Deep Learning Inference Prototyping and Debugging Toolkit

`pip install polygraphy` · installs (wheel) · licence: Apache 2.0 · rank 8235 · last release 2026-09-22 · [PyPI](https://pypi.org/project/polygraphy/)

<details><summary>README extract</summary>

Sections: Introduction, Building From Source, Using Make Targets (Linux), Using Powershell Script (Windows), Building Manually, Command-line Toolkit, Python API, Examples, How-To Guides

</details>

### p-tqdm

Parallel processing with progress bars

`pip install p-tqdm` · installs from source (sdist only) · licence: MIT License · rank 8239 · last release 2024-08-08 · [PyPI](https://pypi.org/project/p-tqdm/)

<details><summary>README extract</summary>

`p_tqdm` makes parallel processing with progress bars easy.

`p_tqdm` is a wrapper around pathos.multiprocessing and tqdm. Unlike Python's default multiprocessing library, pathos provides a more flexible parallel map which can apply almost any type of function, including lambda functions, nested functions, and class methods, and can easily handle ...

Sections: p_tqdm, added == ['1a', '2b', '3c'], added = ['1a', '2b', '3c'], added is an array with '1a', '2b', '3c' in any order, added == ['1a!', '2b!', '3c!']

</details>

### pinecone-text

Text utilities library by Pinecone.io

`pip install pinecone-text` · installs (wheel) · licence: not stated · rank 8258 · last release 2025-08-11 · [PyPI](https://pypi.org/project/pinecone-text/)

<details><summary>README extract</summary>

Pinecone Text Client

The Pinecone Text Client is a Python package that provides text utilities designed for seamless integration with Pinecone's sparse-dense (hybrid) semantic search.

> _⚠️ Warning
> This is a public preview ("Beta") version.
> For any issues or requests, please reach out to our support team.

Example:
```python
from pinecone_text.sparse import BM25Encoder

corpus = ["The quick brown fox jumps over the lazy dog",
          "The lazy dog is brown",
          "The fox is brown"]

# Initialize BM25 and fit the corpus
bm25 = BM25Encoder()
bm25.fit(corpus)

# Encode a new document (for upsert to Pinecone index)
...
```

...

</details>

### pyclothoids

A library for clothoid curves in Python

`pip install pyclothoids` · installs from source (sdist only) · licence: not stated · rank 8264 · last release 2025-05-11 · [PyPI](https://pypi.org/project/pyclothoids/)

<details><summary>README extract</summary>

A Python library for clothoid curves

Read the Documentation!

Clothoid curves have some remarkable mathematical properties that make them desirable for use in many areas of physics and engineering. Not only is a clothoid parameterized by arc length, but it has closed form expressions for its tangent angle and curvature. ...

</details>

### py-expression-eval

Python Mathematical Expression Evaluator

`pip install py-expression-eval` · installs (wheel) · licence: MIT · rank 8270 · last release 2021-08-26 · [PyPI](https://pypi.org/project/py-expression-eval/)

<details><summary>README extract</summary>

Based on js-expression-eval, by Matthew Crumley (email@matthewcrumley.com,

Ported to Python and modified by @cansadadeserfeliz.

You are free to use and modify this code in anyway you find useful. Please leave this comment in the code
to acknowledge its original source. ...

Example:
```python
from py_expression_eval import Parser

parser = Parser()
parser.parse('2 * 3').evaluate({})  # 6
parser.parse('2 ^ x').evaluate({'x': 3})  # 8.0
parser.parse('2 * x + 1').evaluate({'x': 3})  # 7
parser.parse('2 + 3 * x').evaluate({'x': 4})  # 14
parser.parse('(2 + 3) * x').evaluate({'x': 4}) # 20
parser.parse('2-3^x').evaluate({'x': 4})  # -79.0
...
```

...

</details>

### pyheck

Python bindings for heck, the Rust case conversion library

`pip install pyheck` · installs (wheel) · licence: not stated · rank 8296 · last release 2022-07-18 · [PyPI](https://pypi.org/project/pyheck/) · [docs](https://kevinheavey.github.io/pyheck/) · [source](https://github.com/kevinheavey/pyheck)

<details><summary>README extract</summary>

PyHeck is a case conversion library (for converting strings to snake_case, camelCase etc). It is a thin wrapper around the Rust library heck.

Read the documentation.

Example:
```python
>>> from pyheck import snake
>>> snake("We carry a new world here, in our hearts.")
'we_carry_a_new_world_here_in_our_hearts'
```

Sections: pyheck, Example, Setup

</details>

### pyramid-tm

A package which allows Pyramid requests to join the active transaction

`pip install pyramid-tm` · installs (wheel) · licence: Repoze Public License · rank 8303 · last release 2024-11-14 · [PyPI](https://pypi.org/project/pyramid-tm/) · [docs](https://docs.pylonsproject.org/projects/pyramid-tm/en/latest/index.html)

<details><summary>README extract</summary>

`pyramid_tm` is a package which allows Pyramid requests to join
the active transaction as provided by the transaction package.

See
or `docs/index.rst` in this distribution for detailed
documentation.

- Drop support for Python 3.7, and 3.8.

- Add support for Python 3.11, 3.12, and 3.13.

- rename "master" to "main" ...

Features:
- The transaction manager has been converted to a Pyramid 1.2 "tween"
 (instead of an event subscriber). It will be slotted directly "below" the
 exception view handler, meaning it will have a chance to handle exceptions
 before they are turned into ...

Example:
```python
def bwcompat_commit_veto_wrapper(request, response):
    return my_custom_commit_veto(request.environ, response.status,
                                 response.headerlist)
```

...

</details>

### pg0-embedded

Python API for pg0 - embedded PostgreSQL

`pip install pg0-embedded` · installs (wheel) · licence: MIT · rank 8327 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pg0-embedded/) · [source](https://github.com/vectorize-io/pg0)

<details><summary>README extract</summary>

Zero-config PostgreSQL with pgvector. No installation, no Docker, no configuration.

Example:
```python
from pg0 import Pg0

# Basic usage
with Pg0() as pg:
    print(pg.uri)  # postgresql://postgres:postgres@127.0.0.1:5432/postgres
    pg.execute("CREATE EXTENSION IF NOT EXISTS vector")
    pg.execute("SELECT version()")

# Custom configuration
pg = Pg0(
    name="myapp",
    port=5433,
    username="myuser",
    password="mypass",
...
```

Sections: pg0 - PostgreSQL for Python, Usage, API, Pg0 Class, Module Functions, Getting Connection URI, Runtime paths, Links

</details>

### pysnyk

A Python client for the Snyk API

`pip install pysnyk` · installs (wheel) · licence: MIT License · rank 8330 · last release 2024-01-13 · [PyPI](https://pypi.org/project/pysnyk/) · [source](https://github.com/snyk-labs/pysnyk)

<details><summary>README extract</summary>

A Python client for the Snyk API.

Using the client requires you to provide your Snyk API token.

By default the client will connect to the public Snyk service. If you are using a local installation then you can provide the API url as the second argument.

By default the `User-Agent` string for the API requests will be `pysnyk/<version>`. ...

Example:
```python
import snyk
client = snyk.SnykClient("<your-api-token>")
```

Sections: pysnyk, Client, Organizations, A note on Managers, Projects, Importing new projects, Inviting new users, Low-level client, Experimental rest low-level client

</details>

### preliz

Exploring and eliciting probability distributions.

`pip install preliz` · installs (wheel) · licence: Apache Software License · rank 8334 · last release 2026-09-07 · [PyPI](https://pypi.org/project/preliz/) · [docs](https://preliz.readthedocs.io) · [source](https://github.com/arviz-devs/preliz)

<details><summary>README extract</summary>

Exploring and eliciting probability distributions

Features:
Prior elicitation refers to the process of transforming the knowledge of a particular domain into well-defined probability distributions. Specifying useful priors is a central aspect of Bayesian statistics. ...

Sections: Overview, The Zen of PreliZ, Documentation

</details>

### python-libsbml

LibSBML Python API

`pip install python-libsbml` · installs (wheel) · licence: LGPL · rank 8348 · last release 2026-09-17 · [PyPI](https://pypi.org/project/python-libsbml/)

_README extract left out: share-alike licence._

### pandavro

The interface between Avro and pandas DataFrame

`pip install pandavro` · installs (wheel) · licence: MIT · rank 8359 · last release 2025-08-27 · [PyPI](https://pypi.org/project/pandavro/)

<details><summary>README extract</summary>

The interface between Apache Avro and pandas DataFrame.

Example:
```python
import os
import numpy as np
import pandas as pd
import pandavro as pdx

OUTPUT_PATH='{}/example.avro'.format(os.path.dirname(file))

def main():
    df = pd.DataFrame({
        "Boolean": [True, False, True, False],
        "pdBoolean": pd.Series([True, None, True, False], dtype=pd.BooleanDtype()),
        "Float64": np.random.randn(4),
...
```

Sections: pandavro, Description, What can and can't pandavro do?, Loading Pandas nullable datatypes, Example

</details>

### powerfx

Power Fx python bridge to invoke c# implementation.

`pip install powerfx` · installs (wheel) · licence: MIT · rank 8366 · last release 2025-12-22 · [PyPI](https://pypi.org/project/powerfx/)

### PyMySQLLock

MySQL Backed Locking Primitive

`pip install PyMySQLLock` · installs (wheel) · licence: MIT License · rank 8388 · last release 2020-09-13 · [PyPI](https://pypi.org/project/PyMySQLLock/)

<details><summary>README extract</summary>

py-mysql-lock provides locking primitive based on MySQL's GET_LOCK

Though there are mature locking primitives provided by systems like Zookeeper and etcd, when you have an application which is primarily dependent on MySQL for its uptime and health, added resiliency provided by systems just mentioned doesn't add much benefit. ...

Example:
```python
from PyMySQLLock import Locker

locker = Locker(host="localhost", user="root",
                password="password", database="db")
lock = locker.lock("lock_name")

lock.acquire()  # returns True if lock is acquired

# do something

lock.release()
```

...

</details>

### polymarket-client

Official Python client for Polymarket

`pip install polymarket-client` · installs (wheel) · licence: MIT License · rank 8390 · last release 2026-11-05 · [PyPI](https://pypi.org/project/polymarket-client/) · [docs](https://docs.polymarket.com) · [source](https://github.com/Polymarket/py-sdk)

<details><summary>README extract</summary>

Official Python SDK for Polymarket.

The SDK gives Python developers one coherent, workflow-oriented interface for building on Polymarket across public data, authenticated account, trading, builder attribution, and wallet workflows.

Example:
```python
from polymarket import Market, PublicClient

with PublicClient() as client:
    market: Market = client.get_market(url="
```

Sections: Polymarket Python SDK, Usage, API Compatibility, API Design

</details>

### pyfinite

Finite field operations and erasure correction codes.

`pip install pyfinite` · installs from source (sdist only) · licence: MIT · rank 8391 · last release 2022-11-02 · [PyPI](https://pypi.org/project/pyfinite/)

<details><summary>README extract</summary>

The `pyfinite` package is a python package for dealing with finite
fields and related mathematical operations. Also included is a generic
matrix package for doing matrix operations over generic fields. As an
illustration a Reed-Solomon erasure correcting code implementation is
provided using these tools. ...

Example:
```python
>>> from pyfinite import ffield
>>> help(ffield.FField)
```

Sections: Introduction, Usage, Future work

</details>

### pdiff

Pretty side-by-side diff

`pip install pdiff` · installs (wheel) · licence: MIT · rank 8395 · last release 2025-06-15 · [PyPI](https://pypi.org/project/pdiff/)

<details><summary>README extract</summary>

Pretty side-by-side diff.

Inspired by `ydiff` and
`icdiff`.

Sections: pdiff, Example, Usage, Git

</details>

### pySigma-backend-elasticsearch

pySigma Elasticsearch backend supporting Lucene, ES|QL (with correlations) and EQL queries

`pip install pySigma-backend-elasticsearch` · installs (wheel) · licence: LGPL-3.0-only · rank 8415 · last release 2026-08-10 · [PyPI](https://pypi.org/project/pySigma-backend-elasticsearch/)

_README extract left out: share-alike licence._

### pulumiverse-vercel

(no summary)

`pip install pulumiverse-vercel` · installs (wheel) · licence: Apache-2.0 · rank 8416 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pulumiverse-vercel/) · [source](https://github.com/pulumiverse/pulumi-vercel)

<details><summary>README extract</summary>

The Vercel Resource Provider lets you manage Vercel resources.

The Pulumi `Vercel` provider is available as a package in all Pulumi languages:

- JavaScript/TypeScript: `@pulumiverse/vercel`
- Python: `pulumiverse-vercel`
- Go: `github.com/pulumiverse/pulumi-vercel/sdk`
- .NET: `Pulumiverse.vercel`

Sections: Vercel Resource Provider, Node.js (JavaScript/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### percy-appium-app

Python client for visual testing with Percy for mobile apps

`pip install percy-appium-app` · installs (wheel) · licence: MIT License · rank 8422 · last release 2026-06-25 · [PyPI](https://pypi.org/project/percy-appium-app/)

<details><summary>README extract</summary>

Percy visual testing for Python Appium.

Example:
```python
from appium import webdriver
from percy import percy_screenshot

driver = webdriver.Remote(" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)

# take a screenshot
percy_screenshot(driver, 'here is some name')
```

Sections: percy-appium-python, Usage, Configuration, Running with Hybrid Apps, Running Percy on Automate, Creating Percy on automate build, Migrating Config

</details>

### pytest-playwright-asyncio

A pytest wrapper with async fixtures for Playwright to automate web browsers

`pip install pytest-playwright-asyncio` · installs (wheel) · licence: Apache Software License · rank 8431 · last release 2026-10-08 · [PyPI](https://pypi.org/project/pytest-playwright-asyncio/)

<details><summary>README extract</summary>

Write end-to-end tests for your web apps with Playwright and pytest.

- Support for all modern browsers including Chromium, WebKit and Firefox.
- Support for headless and headed execution.
- Built-in fixtures that provide browser primitives to test functions.

See on playwright.dev for examples and more detailed information.

Sections: Pytest plugin for Playwright, Documentation

</details>

### pulumi-hcloud

A Pulumi package for creating and managing hcloud cloud resources.

`pip install pulumi-hcloud` · installs (wheel) · licence: Apache-2.0 · rank 8467 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pulumi-hcloud/) · [source](https://github.com/pulumi/pulumi-hcloud)

<details><summary>README extract</summary>

The HCloud resource provider for Pulumi lets you use Hetzner Cloud resources in your infrastructure
programs. To use this package, please install the Pulumi CLI first.

Sections: HCloud provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### parquet

Python support for Parquet file format

`pip install parquet` · installs (wheel) · licence: Apache Software License · rank 8468 · last release 2020-04-30 · [PyPI](https://pypi.org/project/parquet/)

<details><summary>README extract</summary>

parquet-python is a pure-python implementation (currently with only
read-support) of the parquet
format. It comes with a
script for reading parquet files and outputting the data to stdout as
JSON or TSV (without the overhead of JVM startup). Performance has not
yet been optimized, but it's useful for debugging and quick viewing of
data in files. ...

Example:
```python
import parquet
import json

# assuming parquet file with two rows and three columns:
# foo bar baz
# 1   2   3
# 4   5   6

with open("test.parquet") as fo:
   # prints:
   # {"foo": 1, "bar": 2}
   # {"foo": 4, "bar": 5}
   for row in parquet.DictReader(fo, columns=['foo', 'bar']):
       print(json.dumps(row))

with open("test.parquet") as fo:
...
```

Sections: parquet-python, requirements, getting started, Example, Todos

</details>

### pyautogen

A programming framework for agentic AI. Proxy package for autogen-agentchat.

`pip install pyautogen` · installs (wheel) · licence: MIT License · rank 8472 · last release 2025-07-15 · [PyPI](https://pypi.org/project/pyautogen/)

<details><summary>README extract</summary>

> NOTE: This is a proxy package for the latest version of `autogen-agentchat`. If you are looking for the 0.2.x version, please pin to `pyautogen~=0.2.0`.
> To migrate from 0.2.x to the latest version, please refer to the migration guide.
> Read our previous clarification regarding to forks.
> We have regained admin access to this package. ...

</details>

### pyodide-cli

"The command line interface for the Pyodide project"

`pip install pyodide-cli` · installs (wheel) · licence: MPL-2.0 · rank 8484 · last release 2026-01-28 · [PyPI](https://pypi.org/project/pyodide-cli/) · [docs](https://pyodide.org/en/stable/)

<details><summary>README extract</summary>

The command line interface for the Pyodide project.

In most cases, you do not need to install this package directly, and it would be installed as
a dependency of other packages in the ecosystem (e.g., pyodide-build, pyodide-pack, auditwheel-emscripten, etc.)

Sections: pyodide-cli, Usage

</details>

### private-attribute-cpp

A Python package that provides a way to define private attributes in C++ implementation.

`pip install private-attribute-cpp` · installs (wheel) · licence: MIT · rank 8485 · last release 2026-11-08 · [PyPI](https://pypi.org/project/private-attribute-cpp/)

<details><summary>README extract</summary>

True C++-style private attributes for Python, enforced at the C level.

A C++ extension module (`private_attribute`) that lets you declare attributes
that are only accessible from *inside* the class that owns them — genuinely
hidden from the outside world, from subclasses, and from `hasattr()`, `dir()`,
and `obj.dict`. ...

Features:
Python gives you a *convention* (`_private`) and a *name-mangling trick*
(`name` → `_ClassNamename`), but neither is an actual access barrier. Any
code that knows (or can guess) the mangled name can still read and mutate your
"private" state. ...

Example:
```python
from private_attribute import PrivateAttrBase

class BankAccount(PrivateAttrBase):
    private_attrs = ["_balance"]

    def init(self, balance):
        self._balance = balance

...

</details>

### pydantic-settings-yaml

Yaml support for Pydantic settings

`pip install pydantic-settings-yaml` · installs (wheel) · licence: not stated · rank 8497 · last release 2023-07-20 · [PyPI](https://pypi.org/project/pydantic-settings-yaml/)

<details><summary>README extract</summary>

*Note: 2.x needs Pydantic>2.0,<3.0. Install 1.x if you still need Pydantic 1.x.*

Yaml support for Pydantic settings. Load a yaml config file
as nested Pydantic models.

Allows to use <file:xxxx> placeholders in the yaml config file
for secrets. A placeholder is replaced with the contents of the
file. ...

Example:
```python
from pydantic import BaseModel
from pydantic_settings_yaml import YamlBaseSettings
from pydantic_settings import SettingsConfigDict

class Database(BaseModel):
    username: str
    password: str

class Settings(YamlBaseSettings):
    database: Database

    # configure paths to secrets directory and YAML config file
...
```

Sections: pydantic-settings-yaml, Usage

</details>

### pyunpack

unpack archive files

`pip install pyunpack` · installs (wheel) · licence: BSD License · rank 8498 · last release 2022-06-06 · [PyPI](https://pypi.org/project/pyunpack/)

### pytest_tagging

a pytest plugin to tag tests

`pip install pytest_tagging` · installs (wheel) · licence: MIT License · rank 8514 · last release 2024-11-08 · [PyPI](https://pypi.org/project/pytest_tagging/) · [source](https://github.com/scastlara/pytest-tagging)

<details><summary>README extract</summary>

pytest plugin that allows tagging tests using arbitrary strings.

It supports selecting only tests with a specific tag, and displays a counter of how many tests failed
for each specific tag. ...

Example:
```python
@pytest.mark.tags("JIRA-XX", "integration", constants.COMPONENT_X)
def test_foo():
    assert False
```

Sections: pytest-tagging, Usage, Combining tags, Excluding tags, Extra

</details>

### paradime-io

Paradime - Python SDK

`pip install paradime-io` · installs (wheel) · licence: not stated · rank 8530 · last release 2026-11-02 · [PyPI](https://pypi.org/project/paradime-io/)

<details><summary>README extract</summary>

Example:
```python
from paradime import Paradime

paradime = Paradime(
    api_endpoint="API_ENDPOINT",
    api_secret="API_TOKEN",  # e.g. prdm_wsp... or prdm_cmp...
    # workspace_uid="WORKSPACE_UID",  # required when using a company-level (prdm_cmp) token
)

# Use the paradime client to interact with the API
```

Sections: Paradime - Python SDK, SDK Usage, CLI Usage, Examples, Telemetry

</details>

### pyudorandom

Generate pseudorandom numbers by using algebra

`pip install pyudorandom` · installs from source (sdist only) · licence: UNKNOWN · rank 8548 · last release 2016-07-18 · [PyPI](https://pypi.org/project/pyudorandom/)

### pytest-codeblocks

Test code blocks in your READMEs

`pip install pytest-codeblocks` · installs (wheel) · licence: MIT License · rank 8586 · last release 2026-06-15 · [PyPI](https://pypi.org/project/pytest-codeblocks/)

<details><summary>README extract</summary>

Test code blocks in your READMEs.

This is pytest-codeblocks, a pytest plugin for testing code
blocks from README files. It supports Python and shell code.

Install with

and run pytest with

pytest-codeblocks will only pick up code blocks with `python` and `sh`/`bash`/`zsh`
syntax highlighting.

Sections: Marking code blocks, Merging code blocks, this would otherwise fail since `a` is not defined, Expected output

</details>

### prometheus-async

Async helpers for prometheus_client.

`pip install prometheus-async` · installs (wheel) · licence: Apache-2.0 · rank 8615 · last release 2026-03-24 · [PyPI](https://pypi.org/project/prometheus-async/) · [docs](https://prometheus-async.readthedocs.io/) · [source](https://github.com/hynek/prometheus-async/)

<details><summary>README extract</summary>

*prometheus-async* adds support for asynchronous frameworks to the official Python client for the Prometheus metrics and monitoring system.

Currently *asyncio* and Twisted are supported.

It works by wrapping the metrics from the official client: ...

Example:
```python
import asyncio

from aiohttp import web
from prometheus_client import Histogram
from prometheus_async.aio import time

REQ_TIME = Histogram("req_time_seconds", "time spent in requests")

@time(REQ_TIME)
async def req(request):
      await asyncio.sleep(1)
      return web.Response(body=b"hello")
```

Sections: prometheus-async, prometheus-async* for Enterprise

</details>

### pytest-astropy-header

pytest plugin to add diagnostic information to the header of the test output

`pip install pytest-astropy-header` · installs (wheel) · licence: BSD License · rank 8665 · last release 2022-09-06 · [PyPI](https://pypi.org/project/pytest-astropy-header/)

<details><summary>README extract</summary>

This plugin package provides a way to include information about the system,
Python installation, and select dependencies in the header of the output when
running pytest. It can be used with packages that are not affiliated with the
Astropy project, but is optimized for use with Astropy-related projects.

Example:
```python
def pytest_configure(config):
    config.option.astropy_header = True
```

Sections: pytest-astropy-header, User guide

</details>

### pycoingecko

Python wrapper around the CoinGecko API

`pip install pycoingecko` · installs (wheel) · licence: MIT License · rank 8712 · last release 2024-11-13 · [PyPI](https://pypi.org/project/pycoingecko/)

<details><summary>README extract</summary>

Python3 wrapper around the CoinGecko API (V3) 🦎
 Supports both Public and Pro API:
 * Public API v3.0.1
 * Pro API v3.1.1

Example:
```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

Sections: CoinGecko API wrapper, Usage, Examples, API documentation, 📡 Endpoints included, Test

</details>

### pytest-mypy-plugins

pytest plugin for writing tests for mypy plugins

`pip install pytest-mypy-plugins` · installs (wheel) · licence: MIT License · rank 8713 · last release 2026-10-23 · [PyPI](https://pypi.org/project/pytest-mypy-plugins/)

<details><summary>README extract</summary>

Example:
```python
mypy-tests:
  --mypy-testing-base=MYPY_TESTING_BASE
                        Base directory for tests to use
  --mypy-pyproject-toml-file=MYPY_PYPROJECT_TOML_FILE
                        Which `pyproject.toml` file to use
                        as a default config for tests.
                        Incompatible with `--mypy-ini-file`
...
```

Sections: Usage, Running, Asserting types, Paths, What is a test case?, Example, 1. Inline type expectations, 2. `@parametrized`, 3. Longer type expectations, 4. Regular expressions in expectations, 5. Regular expressions specific lines of output., 6. Markers, Options, Further reading

</details>

### pgtask

PostgreSQL-native durable tasks and workflows

`pip install pgtask` · installs (wheel) · licence: MIT · rank 8727 · last release 2026-10-07 · [PyPI](https://pypi.org/project/pgtask/)

<details><summary>README extract</summary>

Durable tasks and workflows that live entirely in PostgreSQL.

There is no broker, no coordinator, and no extension to install. If your database is up, your queue is up.

> [!WARNING]
> `pgtask` is under active development. It is not ready for production use.

Example:
```python
from future import annotations

import asyncio
import os

from pgtask import Client, Task, TaskRegistry, Worker

tasks = TaskRegistry(queue_name="reports")

@tasks.task("reports.render")
async def render(task: Task, payload: dict) -> dict:
    return {"report_id": payload["report_id"], "attempt": task.attempt}

async def main() -> None:
...
```

Sections: pgtask, Define a task and run a worker, Enqueue a task, Enqueue inside your transaction, Documentation

</details>

### python-manilaclient

Client library for OpenStack Shared File System Storage

`pip install python-manilaclient` · installs (wheel) · licence: Apache Software License · rank 8733 · last release 2026-08-28 · [PyPI](https://pypi.org/project/python-manilaclient/) · [source](https://opendev.org/openstack/python-manilaclient/)

<details><summary>README extract</summary>

This is a client for the OpenStack Manila API. There's a Python API (the
`manilaclient` module), and a command-line script (`manila`). Each
implements 100% of the OpenStack Manila API.

See the OpenStack CLI guide for information on how to use the `manila`
command-line tool. You may also want to look at the
OpenStack API documentation. ...

Example:
```python
# use v3 auth with
>>> from manilaclient.v2 import client
>>> nt = client.Client("2", USER, PASS, PROJECT, AUTH_URL, service_type="share")
>>> nt.shares.list()
[...]
```

Sections: Team and repository tags, Python bindings to the OpenStack Manila API, Command-line API, Python API

</details>

### pytensor-distributions

PyTensor powered distributions.

`pip install pytensor-distributions` · installs (wheel) · licence: Apache Software License · rank 8761 · last release 2026-10-06 · [PyPI](https://pypi.org/project/pytensor-distributions/) · [docs](https://pytensor-distributions.readthedocs.io) · [source](https://github.com/pymc-devs/pytensor-distributions)

<details><summary>README extract</summary>

PyTensor-powered distributions

Features:
PyTensor-distributions provides a collection of core probability expressions implemented in PyTensor.

The goal of this package is to work as a unified, well-tested, and performant source for core probability expressions. ...

Sections: PyTensor-distributions, Overview

</details>

### pykube-ng

Python client library for Kubernetes

`pip install pykube-ng` · installs (wheel) · licence: Apache Software License; Other/Proprietary License · rank 8768 · last release 2023-06-16 · [PyPI](https://pypi.org/project/pykube-ng/)

<details><summary>README extract</summary>

Pykube (pykube-ng) is a lightweight Python 3.6+ client library for Kubernetes.

This is a fork of kelproject/pykube which is no longer maintained (archived). Here the original text of the pykube README:

 Kel is an open source Platform as a Service (PaaS) from Eldarion, Inc. ...

Features:
* HTTP interface using requests using kubeconfig for authentication
* Python native querying of Kubernetes API objects

Example:
```python
import operator
import pykube

api = pykube.HTTPClient(pykube.KubeConfig.from_file())
pods = pykube.Pod.objects(api).filter(namespace="gondor-system")
ready_pods = filter(operator.attrgetter("ready"), pods)
```

Sections: pykube-ng, Features, Interactive Console, Usage, Requirements

</details>

### pytest-custom-report

Configure the symbols displayed for test outcomes

`pip install pytest-custom-report` · installs (wheel) · licence: MIT · rank 8802 · last release 2019-01-30 · [PyPI](https://pypi.org/project/pytest-custom-report/)

<details><summary>README extract</summary>

A plugin for defining your own characters to be used when displaying test outcomes in pytest (passed, failed, skipped etc).

For example, if you wanted to see a PILE OF POO (U+1F4A9) glyph displayed in the terminal report for each failing test:

To persist your custom characters, add a section like this in the configuration file (i.e. ...

Sections: pytest-custom-report, Configuration, Example config file

</details>

### PlexAPI

Python bindings for the Plex API.

`pip install PlexAPI` · installs (wheel) · licence: BSD-3-Clause · rank 8810 · last release 2026-09-28 · [PyPI](https://pypi.org/project/PlexAPI/) · [docs](https://python-plexapi.readthedocs.io)

<details><summary>README extract</summary>

Features:
Unofficial Python bindings for the Plex API. Our goal is to match all capabilities of the official
Plex Web Client. A few of the many features we currently support are:

* Navigate local or remote shared libraries. ...

Example:
```python
# Example 1: List all unwatched movies.
movies = plex.library.section('Movies')
for video in movies.search(unwatched=True):
    print(video.title)
```

Sections: Python-PlexAPI, Overview, Getting a PlexServer Instance, Usage Examples, Controlling Sonos speakers, Running tests over PlexAPI, Common Questions

</details>

### pulumi-azure

A Pulumi package for creating and managing Microsoft Azure cloud resources, based on the Terraform azurerm provider. We recommend using the [Azure Native provider](https://github.com/pulumi/pulumi-azure-native) to provision Azure infrastructure. Azure Native provides complete coverage of Azure resources and same-day access to new resources and resource updates.

`pip install pulumi-azure` · installs (wheel) · licence: Apache-2.0 · rank 8832 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pulumi-azure/) · [source](https://github.com/pulumi/pulumi-azure)

<details><summary>README extract</summary>

> _NOTE:_ We recommend using the Azure Native provider to provision Azure infrastructure. Azure Native provides complete coverage of Azure resources and same-day access to new resources and resource updates because it’s built and automatically from the Azure Resource Manager API.
> Azure Classic is based on the Terraform azurerm provider. ...

Sections: Microsoft Azure Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Concepts, Configuring credentials, Reference

</details>

### python-redis-cache

Basic Redis caching for functions

`pip install python-redis-cache` · installs (wheel) · licence: MIT · rank 8833 · last release 2025-03-25 · [PyPI](https://pypi.org/project/python-redis-cache/)

<details><summary>README extract</summary>

Simple redis cache for Python functions

- Redis 5+
- Python 3.8+ (should work in Python 3.6+, but not tested)

Example:
```python
from redis import StrictRedis
from redis_cache import RedisCache

client = StrictRedis(host="redis", decode_responses=True)
cache = RedisCache(redis_client=client)

@cache.cache()
def my_func(arg1, arg2):
    return some_expensive_operation()

# Use the function
my_func(1, 2)

# Call it again with the same arguments and it will use cache
...
```

Sections: python-redis-cache, Requirements, How to use, API, Limitations and things to know, Redis key names, Specifying `namespace` - The name of the cache function, Instance/Class methods

</details>

### py-evm

Python implementation of the Ethereum Virtual Machine

`pip install py-evm` · installs (wheel) · licence: MIT License · rank 8840 · last release 2025-05-14 · [PyPI](https://pypi.org/project/py-evm/)

### pytorch-wavelets

A port of the DTCWT toolbox to run on pytorch

`pip install pytorch-wavelets` · installs (wheel) · licence: Free To Use But Restricted · rank 8847 · last release 2023-04-13 · [PyPI](https://pypi.org/project/pytorch-wavelets/)

<details><summary>README extract</summary>

The full documentation is also available here.


This package provides support for computing the 2D discrete wavelet and
the 2d dual-tree complex wavelet transforms, their inverses, and passing
gradients through both using pytorch.

The implementation is designed to be used with batches of multichannel images. ...

Example:
```python
import torch
from pytorch_wavelets import DWTForward, DWTInverse
xfm = DWTForward(J=3, wave='db3', mode='zero')
X = torch.randn(10,5,64,64)
Yl, Yh = xfm(X)
print(Yl.shape)
>>> torch.Size([10, 5, 12, 12])
print(Yh[0].shape)
>>> torch.Size([10, 5, 3, 34, 34])
print(Yh[1].shape)
>>> torch.Size([10, 5, 3, 19, 19])
print(Yh[2].shape)
...
```

...

</details>

### pygwalker

pygwalker: turn your data into an interactive UI for data exploration and visualization

`pip install pygwalker` · installs (wheel) · licence: Apache Software License · rank 8860 · last release 2026-04-04 · [PyPI](https://pypi.org/project/pygwalker/) · [source](https://github.com/Kanaries/pygwalker)

<details><summary>README extract</summary>

English | Español | Français | Deutsch | 中文 | Türkçe | 日本語 | 한국어 | Русский

PyGWalker can simplify your Jupyter Notebook data analysis and data visualization workflow, by turning your pandas dataframe into an interactive user interface for visual exploration. ...

Features:
PyGWalker is a Python library that simplifies data analysis and visualization workflows by turning pandas DataFrames into interactive visual interfaces.
It offers a variety of features that make it a powerful tool for data exploration: ...

Example:
```python
import pandas as pd
import pygwalker as pyg
```

...

</details>

### pyformance

Performance metrics, based on Coda Hale's Yammer metrics

`pip install pyformance` · installs from source (sdist only) · licence: Apache 2.0 · rank 8864 · last release 2017-10-08 · [PyPI](https://pypi.org/project/pyformance/)

### pytest-antilru

Bust functools.lru_cache when running pytest to avoid test pollution

`pip install pytest-antilru` · installs (wheel) · licence: MIT · rank 8904 · last release 2026-10-01 · [PyPI](https://pypi.org/project/pytest-antilru/) · [source](https://github.com/ipwnponies/pytest-antilru)

<details><summary>README extract</summary>

<details>
 <summary>More badges</summary>

</details>

Caching expensive function calls with `functools.lru_cache` is simple and great performance optimization.
It works so well that it'll even speed up your unit test runs!
Too bad it violated test isolation and caches the wrong values under test conditions, introducing test pollution
(persisted ...

Example:
```python
def expensive_network_call() -> int:
    # Pretend this is an expensive network call.
    # You want to cache this for performance but you want to run tests with different responses as well.
    return 1

@lru_cache()
def cache_me() -> int:
    return expensive_network_call()
```

...

</details>

### paracelsus

Visualize SQLAlchemy Databases using Mermaid or Dot Diagrams.

`pip install paracelsus` · installs (wheel) · licence: not stated · rank 8909 · last release 2026-01-04 · [PyPI](https://pypi.org/project/paracelsus/)

<details><summary>README extract</summary>

Paracelsus generates Entity Relationship Diagrams by reading your SQLAlchemy models.

- Paracelsus
 - Features
 - Usage
 - Installation
 - Basic CLI Usage
 - Importing Models
 - Include or Exclude tables
 - Specify Column Sort Order
 - Omit Comments
 - Type Parameter Delimiter
 - Generate Mermaid Diagrams
 - Inject Mermaid Diagrams
 - Creating ...

Features:
- ERDs can be injected into documentation as Mermaid Diagrams.
- Paracelsus can be run in CICD to check that databases are up to date.
- ERDs can be created as files in either Dot or Mermaid format. ...

Example:
```python
from example_app.models import *
```

...

</details>

### python-redlines

Open-source DOCX comparison tool to generate native Word tracked changes (redlines) in Python without MS Word dependencies.

`pip install python-redlines` · installs (wheel) · licence: MIT · rank 8915 · last release 2026-10-24 · [PyPI](https://pypi.org/project/python-redlines/) · [docs](https://jsv4.github.io/Python-Redlines/) · [source](https://github.com/JSv4/Python-Redlines)

<details><summary>README extract</summary>

Generate tracked-change "redline" `.docx` documents by comparing two Word files.

`python-redlines` is the pure-Python core. The comparison engines themselves are
compiled .NET binaries shipped in separate, optional companion packages — install
the one(s) you need as extras: ...

Example:
```python
from python_redlines import DocxodusEngine

engine = DocxodusEngine()
redline_bytes, stdout, stderr = engine.run_redline(
    "Author Name",
    original=open("original.docx", "rb").read(),
    modified=open("modified.docx", "rb").read(),
)
```

Sections: python-redlines, Usage

</details>

### pyliblzfse

Python bindings for the LZFSE reference implementation

`pip install pyliblzfse` · installs from source (sdist only) · licence: MIT · rank 8923 · last release 2025-05-03 · [PyPI](https://pypi.org/project/pyliblzfse/)

<details><summary>README extract</summary>

<pre> _ _ _ _ ___
 | (_) | | | / __)
 __ _ _| |_| | _ | |_| | _ __
| _ \| | | | | | || \| (_ ) )___)/ _ )
| | | | |_| | | | |_) ) |/ /| | |_ ( (/ /
| ||_/ \ |_|_|/|_(_)_| (_/ \____)
|_| (____/

Features:
pyliblzfse is a Python ( module that provides LZFSE
and LZVN compression and decompression through the reference implementation
provided by Apple (

Sections: Overview, Building, Usage, Notes

</details>

### py-rattler

A blazing fast library to work with the conda ecosystem

`pip install py-rattler` · installs (wheel) · licence: BSD-3-Clause · rank 8950 · last release 2026-10-29 · [PyPI](https://pypi.org/project/py-rattler/) · [docs](https://conda.github.io/rattler/py-rattler/) · [source](https://github.com/conda/rattler)

<details><summary>README extract</summary>

[][build]
[][chat-url]
[][pixi-url]
[][docs-main]
[][py-docs-main]

Rattler is a library that provides common functionality used within the conda ecosystem (what is conda & conda-forge?).
The goal of the library is to enable programs and other libraries to easily interact with the conda ecosystem without being dependent on Python. ...

Example:
```python
import asyncio
import tempfile

from rattler import solve, install, VirtualPackage

async def main() -> None:
    # Start by solving the environment.
    #
    # Solving is the process of going from specifications of package and their
    # version requirements to a list of concrete packages.
    print("started solving the environment")
...
```

...

</details>

### pscript

Python to JavaScript compiler.

`pip install pscript` · installs (wheel) · licence: not stated · rank 8957 · last release 2026-03-31 · [PyPI](https://pypi.org/project/pscript/) · [docs](http://pscript.readthedocs.io) · [source](https://github.com/flexxui/pscript)

<details><summary>README extract</summary>

PScript is a Python to JavaScript compiler, and is also the name of the subset
of Python that this compiler supports. It was originally developed as a part of
Flexx and is now a project on its own.

Installation

PScript is pure Python and requires Python 3.6+ (including Pypy).
It has no further dependencies.

Short example

Gives: ...

Example:
```python
from pscript import py2js

def foo(a, b=2):
   print(a - b)

print(py2js(foo))
```

</details>

### pyccolo

Declarative instrumentation for Python

`pip install pyccolo` · installs (wheel) · licence: BSD License · rank 8964 · last release 2026-10-09 · [PyPI](https://pypi.org/project/pyccolo/)

<details><summary>README extract</summary>

Pyccolo (pronounced like the instrument "piccolo") is a library for declarative
instrumentation in Python; i.e., it lets you specify the *what* of the
instrumentation you wish to perform, and takes care of the *how* for you.

Pyccolo brings metaprogramming to everybody via general, event-emitting AST
transformations, and aims to be: ...

Example:
```python
from decimal import Decimal

import pyccolo as pyc

class ExactFloats(pyc.BaseTracer):
    @pyc.after_float
    def to_decimal(self, ret, *_, **__):
        return Decimal(str(ret))

with ExactFloats:
    pyc.exec("print(0.1 + 0.2)")  # -> 0.3   (not 0.30000000000000004)
```

...

</details>

### purify

Pythonic object-mutator transforms as pure functions

`pip install purify` · installs (wheel) · licence: not stated · rank 8977 · last release 2026-03-26 · [PyPI](https://pypi.org/project/purify/)

<details><summary>README extract</summary>

Pythonic object-mutator transforms as pure functions.

This solves a longstanding complaint that I have about Python -
there's no Pythonic way to write a pure function that is supposed to
return a transformed version of an input instance of a class. ...

Example:
```python
def rename_tree(name: str, tree: Tree) -> Tree:
    tree.name = name
    return tree
```

Sections: purify, Rationale, Shallow copy vs deepcopy, How to visually parse shallowly pure functions, Advanced Usage, Argument name, Deepcopy

</details>

### perf-analyzer

Triton Performance Analyzer

`pip install perf-analyzer` · installs (wheel) · licence: not stated · rank 8985 · last release 2026-04-28 · [PyPI](https://pypi.org/project/perf-analyzer/)

<details><summary>README extract</summary>

Triton Performance Analyzer is CLI tool which can help you optimize the
inference performance of models running on Triton Inference Server by measuring
changes in performance as you experiment with different optimization strategies.

> ⚠️ Warning: genai-perf is being deprecated. Please migrate to AIPerf for continued support and enhanced features.

Sections: Triton Performance Analyzer, Features, Inference Load Modes, Performance Measurement Modes, Other Features, Quick Start, Step 1: Start Triton Container, Step 2: Download `simple` Model, Step 3: Start Triton Server, Step 4: Start Triton SDK Container, Step 5: Run Perf Analyzer, Documentation, Reporting problems, asking questions

</details>

### pwinput

A cross-platform Python module that displays **** for password input. Works on Windows, unlike getpass. Formerly called stdiomask.

`pip install pwinput` · installs from source (sdist only) · licence: MIT License · rank 9002 · last release 2023-02-16 · [PyPI](https://pypi.org/project/pwinput/)

<details><summary>README extract</summary>

A cross-platform Python module that displays **** for password input. Formerly called stdiomask.

Installation

To install with pip, run:

 pip install pwinput

Quickstart Guide

The `getpass.getpass()` function in the Python Standard Library won't display "mask" characters as you type; it only displays nothing as you type. ...

</details>

### pysigma-backend-splunk

pySigma Splunk backend

`pip install pysigma-backend-splunk` · installs (wheel) · licence: OSI Approved · rank 9008 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pysigma-backend-splunk/) · [source](https://github.com/SigmaHQ/pySigma-backend-splunk)

<details><summary>README extract</summary>

This is the Splunk backend for pySigma. It provides the package `sigma.backends.splunk` with the `SplunkBackend` class.
Further, it contains the following processing pipelines in `sigma.pipelines.splunk`: ...

Sections: pySigma Splunk Backend, Data model (tstats) query settings

</details>

### pyseto

A Python implementation of PASETO/PASERK.

`pip install pyseto` · installs (wheel) · licence: MIT · rank 9030 · last release 2026-07-19 · [PyPI](https://pypi.org/project/pyseto/) · [source](https://github.com/dajiaji/pyseto)

<details><summary>README extract</summary>

PySETO is a PASETO (Platform-Agnostic SEcurity TOkens)/PASERK (Platform-Agnostic Serialized Keys) implementation written in Python
which supports all of the versions (v1,
v2,
v3 and
v4) and purposes (`public` and `local`)
and has passed all of the official tests.

You can install PySETO with pip: ...

Example:
```python
import pyseto
from pyseto import Key

private_key_pem = b"-----BEGIN PRIVATE KEY-----\nMC4CAQAwBQYDK2VwBCIEILTL+0PfTOIQcn2VPkpxMwf6Gbt9n4UEFDjZ4RuUKjd0\n-----END PRIVATE KEY-----"
public_key_pem = b"-----BEGIN PUBLIC KEY-----\nMCowBQYDK2VwAyEAHrnbu7wEfAP9cGBOAHHwmH4Wsot1ciXBHwBBXQ4gsaI=\n-----END PUBLIC KEY-----"

...
```

...

</details>

### python-path

A clean way to import scripts on other folders via a context manager.

`pip install python-path` · installs from source (sdist only) · licence: MIT · rank 9041 · last release 2018-04-09 · [PyPI](https://pypi.org/project/python-path/)

<details><summary>README extract</summary>

`python_path` is a simple utility that lets you cleanly add routes to your `PYTHON_PATH`. Its very useful to safely load scripts from other folders.

Example:
```python
# my_project/main.py

from python_path import PythonPath

with PythonPath("some_folder"):
    import other
```

Sections: Python Path, Usage

</details>

### PyWinCtl

Cross-Platform toolkit to get info on and control windows on screen

`pip install PyWinCtl` · installs (wheel) · licence: BSD License · rank 9042 · last release 2024-09-23 · [PyPI](https://pypi.org/project/PyWinCtl/)

<details><summary>README extract</summary>

Cross-Platform module to get info on and control windows on screen.

With PyWinCtl you can retrieve info or control windows from other open applications, as well as use it as a cross-platform toolkit to manipulate your own application windows. ...

Sections: PyWinCtl, Window Features, Window Change Notifications, Menu Features, Using this code, Test

</details>

### PyMonCtl

Cross-Platform toolkit to get info on and control monitors connected

`pip install PyMonCtl` · installs (wheel) · licence: BSD License · rank 9047 · last release 2024-04-22 · [PyPI](https://pypi.org/project/PyMonCtl/)

<details><summary>README extract</summary>

Cross-Platform module which provides a set of features to get info on and control monitors.

Additional tools/extensions/APIs used:

 - Xlib's randr extension
 - xrandr command-line tool
 - xset command-line tool

 - VCP MCCS API interface

 - pmset command-line tool ...

Sections: PyMonCtl, General Features, Monitor Class, Important OS-dependent behaviors and limitations, Keep track of Monitor(s) changes, Keep Monitors info updated, Get notified on Monitors changes, USING THIS CODE, TEST

</details>

### python-redlines-docxodus

Docxodus redline engine binary for python-redlines.

`pip install python-redlines-docxodus` · installs (wheel) · licence: MIT · rank 9064 · last release 2026-10-24 · [PyPI](https://pypi.org/project/python-redlines-docxodus/) · [source](https://github.com/JSv4/Python-Redlines)

<details><summary>README extract</summary>

Compiled Docxodus redline engine binary for
`python-redlines`.

Version 2.0.0 bundles the engine built from Docxodus v14.1.0.

This package only contains the platform-specific engine binary. Install it via
the `python-redlines` extra rather than directly:

</details>

### pyaml-env

Provides yaml file parsing with environment variable resolution

`pip install pyaml-env` · installs (wheel) · licence: MIT License · rank 9071 · last release 2025-01-13 · [PyPI](https://pypi.org/project/pyaml-env/)

<details><summary>README extract</summary>

A very small library that parses a yaml configuration file and it resolves the environment variables,
so that no secrets are kept in text.

Example:
```python
from pyaml_env import parse_config
config = parse_config('path/to/config.yaml')

print(config)
# outputs the following, with the environment variables resolved
{
    'database': {
        'name': 'test_db',
        'username': 'super_secret_user',
        'password': 'extra_super_secret_password',
        'url': '
    }
}
```

Sections: TL;DR, How to use, Basic Usage: Environment variable parsing, Attribute Access using `BaseConfig`, Default Values with `:`, Datatype parsing with yaml's tag:yaml.org,2002, If nothing matches: `N/A` as `default_value`, Using a different loader, Useful links

</details>

### PyWinBox

Cross-Platform and multi-monitor toolkit to handle rectangular areas and windows box

`pip install PyWinBox` · installs (wheel) · licence: BSD License · rank 9073 · last release 2024-04-17 · [PyPI](https://pypi.org/project/PyWinBox/)

<details><summary>README extract</summary>

Cross-Platform and multi-monitor module which allows to manage window areas (position and
size) and all their properties, as well as any rectangular area.

You just need to instantiate the PyWinBox class, passing custom callbacks to be called when any property is
queried (onQuery) or set (onSet). ...

Sections: PyWinBox, Rectangular areas, Window areas, Class Properties, Data Structs, USING THIS CODE, TEST

</details>

### pytorch

(no summary)

`pip install pytorch` · installs from source (sdist only) · licence: not stated · rank 9115 · last release 2019-04-24 · [PyPI](https://pypi.org/project/pytorch/)

<details><summary>README extract</summary>

You tried to install "pytorch". The package named for PyTorch is "torch"

</details>

### pyhidra

Native CPython for Ghidra

`pip install pyhidra` · installs (wheel) · licence: MIT License · rank 9160 · last release 2024-10-04 · [PyPI](https://pypi.org/project/pyhidra/)

<details><summary>README extract</summary>

Pyhidra has been integrated into Ghidra under the name "PyGhidra". Pyhidra will continue to support up to Ghidra 11.3/12.0 whichever comes first.

Pyhidra is a Python library that provides direct access to the Ghidra API within a native CPython interpreter using jpype. ...

Example:
```python
import pyhidra
pyhidra.start()

import ghidra
from ghidra.app.util.headless import HeadlessAnalyzer
from ghidra.program.flatapi import FlatProgramAPI
from ghidra.base.project import GhidraProject
from java.lang import String

# do things
```

...

</details>

### poyo

A lightweight YAML Parser for Python. 🐓

`pip install poyo` · installs (wheel) · licence: MIT License · rank 9173 · last release 2019-07-26 · [PyPI](https://pypi.org/project/poyo/) · [source](https://github.com/hackebrot/poyo)

<details><summary>README extract</summary>

A lightweight YAML Parser for Python. 🐓

poyo does not allow deserialization of arbitrary Python objects. Supported
types are `str`, `bool`, `int`, `float`, `NoneType` as well as `dict` and
`list` values.

⚠️ Please note that poyo supports only a chosen subset of the YAML format
that is required to parse cookiecutter user configuration
files. ...

Example:
```python
import codecs
import logging

from poyo import parse_string, PoyoException

logging.basicConfig(level=logging.DEBUG)

with codecs.open("tests/foobar.yml", encoding="utf-8") as ymlfile:
    ymlstring = ymlfile.read()

try:
    config = parse_string(ymlstring)
except PoyoException as exc:
    logging.error(exc)
else:
    logging.debug(config)
```

...

</details>

### pdftotext

Simple PDF text extraction

`pip install pdftotext` · installs from source (sdist only) · licence: MIT · rank 9239 · last release 2026-06-26 · [PyPI](https://pypi.org/project/pdftotext/)

<details><summary>README extract</summary>

Simple PDF text extraction

Features:
I needed to index a lot of PDF documents with Python. Existing solutions were
slow, complicated, or both. That might not be true anymore!

Example:
```python
import pdftotext

# Load your PDF
with open("lorem_ipsum.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# If it's password-protected
with open("secure.pdf", "rb") as f:
    pdf = pdftotext.PDF(f, "secret")

# How many pages?
print(len(pdf))

# Iterate over all the pages
for page in pdf:
    print(page)

# Read some individual pages
print(pdf[0])
...
```

Sections: pdftotext, Why, Dependencies, Debian, Ubuntu, and friends, Fedora, Red Hat, and friends, macOS

</details>

### pytrilogy

Declarative, typed query language that compiles to SQL.

`pip install pytrilogy` · installs from source (sdist only) · licence: not stated · rank 9252 · last release 2026-11-08 · [PyPI](https://pypi.org/project/pytrilogy/)

<details><summary>README extract</summary>

Trilogy is a batteries-included data-productivity toolkit that accelerates SQL-based analytics with a typed, expressive language. It's great for humans - and even better for agents. ...

Features:
SQL is the best way to work with data with but shows strain at scale and as it ages. Can we have the pros without the cons? We believe you can. ...

Example:
```python
from trilogy import Environment, Dialects
from trilogy.ai import Provider, text_to_query
import os

executor = Dialects.DUCK_DB.default_executor(
    environment=Environment(working_path=Path(file).parent)
)

api_key = os.environ.get(OPENAI_API_KEY)
if not api_key:
    raise ValueError("OPENAI_API_KEY required for gpt generation")
# load a model
...
```

...

</details>

### pynvim

Python client for Neovim

`pip install pynvim` · installs (wheel) · licence: Apache · rank 9253 · last release 2025-09-07 · [PyPI](https://pypi.org/project/pynvim/)

### python-barbicanclient

Client Library for OpenStack Barbican Key Management API

`pip install python-barbicanclient` · installs (wheel) · licence: Apache Software License · rank 9270 · last release 2026-08-28 · [PyPI](https://pypi.org/project/python-barbicanclient/)

<details><summary>README extract</summary>

This is a client for the Barbican
Key Management API. There is a Python library for accessing the API
(`barbicanclient` module), and a command-line script (`barbican`).

Example:
```python
>>> from keystoneclient.auth import identity
>>> from keystoneauth1 import session
>>> from barbicanclient import client

>>> # We'll use Keystone API v3 for authentication
>>> auth = identity.v3.Password(auth_url='
...                             username='admin_user',
...                             user_domain_name='Default',
...
```

Sections: python-barbicanclient, barbicanclient - Python Library, barbican - Command Line Client

</details>

### python-jsonschema-objects

An object wrapper for JSON Schema definitions

`pip install python-jsonschema-objects` · installs (wheel) · licence: MIT License · rank 9282 · last release 2024-11-13 · [PyPI](https://pypi.org/project/python-jsonschema-objects/)

### paper-xlsx

A drop-in openpyxl fork for safe inspection and editing of existing Excel files

`pip install paper-xlsx` · installs (wheel) · licence: MIT License · rank 9298 · last release 2026-09-23 · [PyPI](https://pypi.org/project/paper-xlsx/) · [source](https://github.com/paper-instruments/paper-xlsx)

<details><summary>README extract</summary>

An import-compatible, agent-safe fork of openpyxl for creating and editing Excel workbooks without silent data loss.

`paper-xlsx` is an import-compatible hard fork of openpyxl for creating and editing Excel (`.xlsx`) workbooks. It keeps the `openpyxl` import name and upstream object model. ...

Example:
```python
from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws["A1"], ws["B1"] = "Growth rate", 0.05
ws["A2"], ws["B2"] = "Revenue", 1000
ws["B3"] = "=B2 * (1 + B1)"
wb.save("model.xlsx")

wb = load_workbook("model.xlsx")
wb.active["B1"] = 0.07
receipt = wb.save("model-v2.xlsx", receipt=True)
...
```

Sections: paper-xlsx, Quick start, Documentation

</details>

### protoletariat

Python protocol buffers for the rest of us

`pip install protoletariat` · installs (wheel) · licence: Apache Software License · rank 9318 · last release 2025-03-19 · [PyPI](https://pypi.org/project/protoletariat/) · [source](https://github.com/cpcloud/protoletariat)

<details><summary>README extract</summary>

Sections: Motivation, Usage, Example, How it works, Subcommands, Help

</details>

### pytest-markdown-docs

Run markdown code fences through pytest

`pip install pytest-markdown-docs` · installs (wheel) · licence: MIT · rank 9329 · last release 2026-03-23 · [PyPI](https://pypi.org/project/pytest-markdown-docs/) · [source](https://github.com/modal-labs/pytest-markdown-docs)

<details><summary>README extract</summary>

A plugin for pytest that uses markdown code snippets from markdown files and docstrings as tests.

Detects Python code fences (triple backtick escaped blocks) in markdown files as
well as inline Python docstrings (similar to doctests) and runs them as tests.

Python file example: ...

Example:
```python
def pytest_markdown_docs_globals():
    import math
    return {"math": math, "myvar": "hello"}
```

Sections: Pytest Markdown Docs, Usage, Detection conditions, Skipping tests, Code block dependencies, Injecting global/local variables, Fixtures, Async Fixtures (pytest-asyncio), Depending on previous snippets, Retrying Flaky Tests, Compatibility with Material for MkDocs, Customizing your own custom MarkdownIt parser, Known issues

</details>

### pip-autoremove

Remove a package and its unused dependencies

`pip install pip-autoremove` · installs (wheel) · licence: Apache Software License · rank 9358 · last release 2021-09-17 · [PyPI](https://pypi.org/project/pip-autoremove/)

<details><summary>README extract</summary>

Remove a package and its unused dependencies.

Sections: pip-autoremove, Quickstart, Usage

</details>

### pangres

Postgres insert update with pandas DataFrames.

`pip install pangres` · installs from source (sdist only) · licence: Public Domain · rank 9407 · last release 2023-11-05 · [PyPI](https://pypi.org/project/pangres/)

<details><summary>README extract</summary>

_Thanks to freesvg.org for the logo assets

Upsert with pandas DataFrames (<code>ON CONFLICT DO NOTHING</code> or <code>ON CONFLICT DO UPDATE</code>) for PostgreSQL, MySQL, SQlite and potentially other databases behaving like SQlite (untested) with some additional optional features (see features). ...

Features:
1. <i>(optional)</i> Automatical column creation (when a column exists in the DataFrame but not in the SQL table)
2. <i>(optional)</i> Automatical column type alteration for columns that are empty in the SQL table (except for SQlite where alteration ...

Sections: pangres, Features, Requirements, Requirements for sqlalchemy>=2.0, Requirements for asynchronous engines, Gotchas and caveats, All flavors, Postgres, SQlite, MySQL, Notes, Usage, Pytest, flake8

</details>

### pytransitions

A lightweight, object-oriented Python state machine implementation with many extensions.

`pip install pytransitions` · installs (wheel) · licence: MIT License · rank 9443 · last release 2024-12-10 · [PyPI](https://pypi.org/project/pytransitions/)

<details><summary>README extract</summary>

A lightweight, object-oriented state machine implementation in Python with many extensions. Compatible with Python 2.7+ and 3.0+.

Example:
```python
from transitions import Machine
import random

class NarcolepticSuperhero(object):

    # Define some states. Most of the time, narcoleptic superheroes are just like
    # everyone else. Except for...
    states = ['asleep', 'hanging out', 'hungry', 'sweaty', 'saving the world']

    def init(self, name):

...
```

Sections: transitions, Quickstart, The non-quickstart, Some key concepts, Basic initialization, States, Callbacks, Checking state, Enumerations, Transitions, Triggering a transition, Triggering invalid transitions, Automatic transitions for all states, Transitioning from multiple states

</details>

### PyNiteFEA

A simple 3D structural finite element library for Python.

`pip install PyNiteFEA` · installs (wheel) · licence: MIT · rank 9464 · last release 2026-10-29 · [PyPI](https://pypi.org/project/PyNiteFEA/)

<details><summary>README extract</summary>

An easy to use elastic 3D structural engineering finite element analysis library for Python.

Sections: Simple Finite Element Analysis in Python, Current Capabilities, Project Objectives, Example Projects, What's New?

</details>

### pulumi-automation

Pulumi Automation Wrapper

`pip install pulumi-automation` · installs (wheel) · licence: Apache Software License · rank 9485 · last release 2022-01-22 · [PyPI](https://pypi.org/project/pulumi-automation/)

### py-healthcheck

Adds healthcheck endpoints to Flask or Tornado apps

`pip install py-healthcheck` · installs (wheel) · licence: MIT · rank 9609 · last release 2022-06-11 · [PyPI](https://pypi.org/project/py-healthcheck/)

<details><summary>README extract</summary>

Healthcheck is a library to write simple healthcheck functions that can
be used to monitor your application. It is possible to use in a `Flask`
app or `Tornado` app. It's useful for asserting that your dependencies
are up and running and your application can respond to HTTP requests. ...

Example:
```python
from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump

app = Flask(name)

health = HealthCheck()
envdump = EnvironmentDump()

# add your own check function to the healthcheck
def redis_available():
    client = _redis_client()
    info = client.info()
    return True, "redis ok"

health.add_check(redis_available)

...
```

...

</details>

### pyBigWig

A package for accessing bigWig files using libBigWig

`pip install pyBigWig` · installs from source (sdist only) · licence: OSI Approved · rank 9649 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyBigWig/)

<details><summary>README extract</summary>

A python extension, written in C, for quick access to bigBed files and access to and creation of bigWig files. This extension uses libBigWig for local and remote file access.

Sections: pyBigWig, Requirements, Usage, Load the extension, Open a bigWig or bigBed file, Determining the file type, Access the list of chromosomes and their lengths, Print the header, Compute summary information on a range, A note on statistics and zoom levels, Retrieve values for individual bases in a range, Retrieve all intervals in a range, Retrieving bigBed entries, Add a header to a bigWig file

</details>

### poetry-plugin-shell

Poetry plugin to run subshell with virtual environment activated

`pip install poetry-plugin-shell` · installs (wheel) · licence: MIT License · rank 9667 · last release 2025-01-05 · [PyPI](https://pypi.org/project/poetry-plugin-shell/) · [source](https://github.com/python-poetry/poetry-plugin-shell)

<details><summary>README extract</summary>

> [!NOTE]
> We are looking for maintainers, see the issue.

This package is a plugin that runs a subshell with virtual environment activated.

This plugin replaces the same feature as the `shell` command previously available in Poetry.

Sections: Poetry Plugin: Shell, Usage

</details>

### py-crunchbase-api

A python client for Crunchbase's REST API

`pip install py-crunchbase-api` · installs (wheel) · licence: MIT License · rank 9705 · last release 2023-03-04 · [PyPI](https://pypi.org/project/py-crunchbase-api/) · [source](https://github.com/FahadNoor/py_crunchbase)

<details><summary>README extract</summary>

PyCrunchbase is a python client for Crunchbase's REST API.
Crunchbase provides 4 types of APIs:-

1. Search API
2. Autocomplete API
3. Deleted Entities API
4. Entities API

PyCrunchbase supports all of these through a very simple interface.

Example:
```python
from py_crunchbase import PyCrunchbase

# API key can be set as the env variable PY_CRUNCHBASE_API_KEY
pycb = PyCrunchbase()

# OR passed as an argument
pycb = PyCrunchbase('api_key')

# If both are provided, the latter will take preference
```

...

</details>

### pegasus-cli

CLI for Django and SaaS Pegasus

`pip install pegasus-cli` · installs (wheel) · licence: Apache Software License · rank 9715 · last release 2026-08-04 · [PyPI](https://pypi.org/project/pegasus-cli/)

<details><summary>README extract</summary>

Features:
The Pegasus CLI is the command-line companion to SaaS Pegasus:
manage your Pegasus projects without leaving the terminal.

With it you can: ...

Sections: pegasus-cli, Overview, Usage, Managing your Pegasus projects, Setup, Listing projects, Configuring projects, Pushing to GitHub, Custom server URL, Creating Django apps, Configuration, Migrating pg- CSS classes

</details>

### PyQt6-WebEngine-Qt6

The subset of a Qt installation needed by PyQt6-WebEngine.

`pip install PyQt6-WebEngine-Qt6` · installs (wheel) · licence: LGPL v3 · rank 9749 · last release 2026-11-02 · [PyPI](https://pypi.org/project/PyQt6-WebEngine-Qt6/)

_README extract left out: share-alike licence._

### plyer

Platform-independent wrapper for platform-dependent APIs

`pip install plyer` · installs (wheel) · licence: MIT License · rank 9759 · last release 2022-11-12 · [PyPI](https://pypi.org/project/plyer/)

<details><summary>README extract</summary>

Plyer is a platform-independent api to use features commonly found on various
platforms, notably mobile ones, in Python.

Plyer tries not to reinvent the wheel, and will call for external libraries to
implement the api in the easiest way, depending on the current platform.

- On Android(python-for-android), pyjnius is used ...

Sections: Plyer, How plyer works?, Backers, 2.1.0 (2022-11-12), 2.0.0 (2020-11-09), 1.4.3 (2020-03-27), 1.4.2 (2019-09-05), 1.4.1 (2019-09-05), 1.4.0 (2018-12-31), 1.3.2 (2018-11-16), 1.3.1 (2018-10-14), 1.3.0 (2017-03-23), v1.2.4 (2015-06-01), 1.2.3 (2015-01-27)

</details>

### pipfile

(no summary)

`pip install pipfile` · installs from source (sdist only) · licence: Apache Software License; BSD License · rank 9760 · last release 2017-03-11 · [PyPI](https://pypi.org/project/pipfile/)

<details><summary>README extract</summary>

`Pipfile` and its sister `Pipfile.lock` are a replacement for the existing standard pip's `requirements.txt` file.

 WARNING: This project is under active design and development. Nothing is set in stone at this point of time. ...

Sections: Pipfile, The Concept, Examples, `Pipfile`, `Pipfile.lock`, Pip Integration (eventual), Useful Links, Inspirations, Documentation, Discussion, 16.0 - master

</details>

### pupil-apriltags

Python bindings for apriltags v3

`pip install pupil-apriltags` · installs from source (sdist only) · licence: MIT License · rank 9815 · last release 2025-04-22 · [PyPI](https://pypi.org/project/pupil-apriltags/) · [docs](https://pupil-apriltags.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

These are Python bindings for the
Apriltags3 library
developed by AprilRobotics,
specifically adjusted to work with the pupil-labs software. The original
bindings were provided by
duckietown and were
inspired by the Apriltags2
bindings by Matt
Zucker.

Example:
```python
from pupil_apriltags import Detector

at_detector = Detector(
   families="tag36h11",
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)

at_detector.detect(img)
```

Sections: pupil-apriltags: Python bindings for the apriltags3 library, Usage

</details>

### python-squarelet

Python library that handles token authentication for MuckRock and DocumentCloud

`pip install python-squarelet` · does not install on CPython 3.14 · licence: MIT License · rank 9871 · last release 2026-09-03 · [PyPI](https://pypi.org/project/python-squarelet/)

<details><summary>README extract</summary>

A Python wrapper for Squarelet, allowing for authentication with MuckRock systems like MuckRock Requests and DocumentCloud.

Features:
- Token-based Authentication: Easily authenticate with MuckRock services using username/password or refresh tokens.
- Rate Limiting: Automatically applies rate limiting to prevent exceeding API request limits. ...

Example:
```python
# If you intend on accessing MuckRock requests, the base_uri would be  or
base_uri="
from squarelet import SquareletClient
# Authenticating with Squarelet using your credentials
client = SquareletClient(base_uri=base_uri, username="your_username", password="your_password")
# Example API call that gets data about your DocumentCloud account.
...
```

Sections: python-squarelet, Features, Usage, Running tests

</details>

### python-heatclient

OpenStack Orchestration API Client Library

`pip install python-heatclient` · installs (wheel) · licence: Apache-2.0 · rank 9879 · last release 2026-08-25 · [PyPI](https://pypi.org/project/python-heatclient/) · [source](https://opendev.org/openstack/python-heatclient)

<details><summary>README extract</summary>

OpenStack Orchestration API Client Library

This is a client library for Heat built on the Heat orchestration API. It
provides a Python API (the `heatclient` module) and a command-line tool
(`heat`). ...

</details>

### pyhs2

Python Hive Server 2 Client Driver

`pip install pyhs2` · installs from source (sdist only) · licence: LICENSE.txt · rank 9881 · last release 2014-11-20 · [PyPI](https://pypi.org/project/pyhs2/)

<details><summary>README extract</summary>

pyHS2 is a python client driver for connecting to hive server 2.

See example.py for an example of how to use it.

Please log all issues/new feature requests under the issues tab and I will respond ASAP.

Contact @bradruderman or bradruderman@gmail.com with questions.

Enjoy

</details>

### pyorc

Python module for reading and writing Apache ORC file format.

`pip install pyorc` · installs (wheel) · licence: Apache-2.0 · rank 9886 · last release 2026-10-20 · [PyPI](https://pypi.org/project/pyorc/) · [docs](https://pyorc.readthedocs.io) · [source](https://github.com/noirello/pyorc.git)

<details><summary>README extract</summary>

Python module for reading and writing Apache ORC file format. It uses the Apache ORC's Core C++ API
under the hood, and provides a similar interface as the csv module in the Python standard library.

Supports Python 3.11 or newer and ORC 1.8 or newer library version.

Features:
- Reading ORC files.
- Writing ORC files.
- While using Python's stream/file-like object IO interface.

That sums up quite well the purpose of this project.

Example:
```python
import pyorc

with open("./data.orc", "rb") as data:
    reader = pyorc.Reader(data)
    for row in reader:
        print(row)
```

Sections: PyORC, Features, Example

</details>

### pytest-operator

Fixtures for Charmed Operators

`pip install pytest-operator` · installs (wheel) · licence: Apache Software License · rank 9897 · last release 2025-10-04 · [PyPI](https://pypi.org/project/pytest-operator/)

<details><summary>README extract</summary>

PyTest plugin to make it easy to create integration tests for Operator Charms.

Example:
```python
import pytest

@pytest.mark.abort_on_fail
async def test_build_and_deploy(ops_test):
    my_charm = await ops_test.build_charm(".")
    await ops_test.model.deploy(my_charm)
    await ops_test.model.wait_for_idle()

async def test_status(ops_test):
    assert ops_test.model.applications["my-charm"].units[0].workload_status == "active"
```

Sections: pytest-operator, Usage, Building/Downloading Charm Resources, Reference

</details>

### pylibyear

A simple measure of software dependency freshness.

`pip install pylibyear` · installs (wheel) · licence: MIT License · rank 9913 · last release 2026-06-27 · [PyPI](https://pypi.org/project/pylibyear/) · [docs](https://github.com/sam-atkins/pylibyear#readme) · [source](https://github.com/sam-atkins/pylibyear)

<details><summary>README extract</summary>

This is a fork of libyear as it appears to no longer be maintained.

A simple measure of software dependency freshness. It is a single number telling you how up-to-date your dependencies are.

Sections: [py]libyear, Usage, Example output, Example 1, Simpler is Better, Example 2, A Healthy App, Etymology, References, Dev

</details>

### PyGEL3D

PyGEL 3D (Python Bindings for GEL) contains tools for polygonal mesh based geometry processing

`pip install PyGEL3D` · installs (wheel) · licence: MIT · rank 9926 · last release 2026-09-02 · [PyPI](https://pypi.org/project/PyGEL3D/) · [source](https://github.com/janba/GEL)

<details><summary>README extract</summary>

GEL is a C++ library of geometry processing tools mostly intended for computer graphics applications. Python bindings for GEL are found in the included PyGEL library which is also available from PyPI under the package name PyGEL3D.

GEL contains ...

Sections: GEL, PyGEL, DOCUMENTATION, Building with CMake, Using GEL from CMake, Compilation of Demos and Tests, Practical Issues

</details>

### pypsexec

Run commands on a remote Windows host using SMB/RPC

`pip install pypsexec` · installs (wheel) · licence: MIT License · rank 9947 · last release 2021-10-21 · [PyPI](https://pypi.org/project/pypsexec/)

<details><summary>README extract</summary>

This library can run commands on a remote Windows host through Python. This
means that it can be run on any host with Python and does not require any
binaries to be present or a specific OS. It uses SMB/RPC to executable commands
in a similar fashion to the popular PsExec tool. More details on this tool
can be read on
this blog post. ...

Features:
With pypsexec you can run commands of a remote Windows host like you would with
PsExec. Current you can use pypsexec to do the following; ...

Example:
```python
from pypsexec.client import Client

# creates an encrypted connection to the host with the username and password
c = Client("hostname", username="username", password="password")

# set encrypt=False for Windows 7, Server 2008
...

</details>

### poppler-utils

Precompiled command-line utilities (based on Poppler) for manipulating PDF files and converting them to other formats.

`pip install poppler-utils` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 9966 · last release 2020-10-06 · [PyPI](https://pypi.org/project/poppler-utils/)

_README extract left out: share-alike licence._

### pylhasa

Cross-platform Python wrapper for liblhasa (LHA/LZH archives)

`pip install pylhasa` · installs from source (sdist only) · licence: MIT License · rank 9978 · last release 2026-01-24 · [PyPI](https://pypi.org/project/pylhasa/) · [source](https://github.com/bwhitn/pylhasa)

<details><summary>README extract</summary>

`pylhasa` is a cross-platform Python wrapper for the LHA/LZH archive format. It vendors the liblhasa C sources and builds a CPython extension, producing wheels for Linux, macOS, and Windows.

Example:
```python
import pylhasa

archive = pylhasa.open("example.lha")
for entry in archive:
    print(entry.raw_path, entry.size)

# Read bytes directly (loads full file into memory)
payload = archive.read("hello.txt")

# Stream contents (incremental reads, avoids large memory usage)
entry = next(iter(archive))
with entry.open() as stream:
...
```

Sections: pylhasa, Usage, API overview, Examples, In-memory / streaming, Safety notes, Exceptions, Header metadata

</details>

### python-binary-memcached

A pure python module to access memcached via its binary protocol with SASL auth support

`pip install python-binary-memcached` · installs (wheel) · licence: MIT License · rank 10015 · last release 2026-10-12 · [PyPI](https://pypi.org/project/python-binary-memcached/) · [docs](https://python-binary-memcached.readthedocs.org) · [source](https://github.com/jaysonsantos/python-binary-memcached)

<details><summary>README extract</summary>

A pure python module (thread safe) to access memcached via it's binary with SASL auth support.

The main purpose of this module it to be able to communicate with memcached using binary protocol and support authentication, so it can work with Heroku for example.

Latest compiled docs on Read The Docs here.

Example:
```python
import bmemcached
client = bmemcached.Client(('127.0.0.1:11211', ), 'user',
                            'password')
client.set('key', 'value')
print(client.get('key'))
```

Sections: Introduction to bmemcached, Using, Using with Django, v0.33.0 (2026-10-12), Feat, Fix, v0.32.0 (2026-04-28), Docs, v0.31.2 (2022-12-14), v0.31.1 (2021-12-29), v0.31.0 (2021-12-28), Refactor

</details>

### polar-sdk

Polar SDK — A billing platform for the intelligence era

`pip install polar-sdk` · installs (wheel) · licence: MIT · rank 10019 · last release 2026-10-02 · [PyPI](https://pypi.org/project/polar-sdk/) · [source](https://github.com/polarsource/polar/tree/main/sdk/python)

<details><summary>README extract</summary>

The official Python client for the Polar API.

Example:
```python
from polar.v2026_10 import Polar

polar = Polar("polar_oat_xxx")

customer_state = polar.customers.get_state_external("customer_external_id")
print(customer_state)
```

Sections: Polar Python SDK, Quick Start, Async Client, Context Managers, Request Timeouts, Organizations, Deserializing Data, Webhooks

</details>

### pymilvus.model

Model components for PyMilvus, the Python SDK for Milvus

`pip install pymilvus.model` · installs (wheel) · licence: Apache Software License · rank 10069 · last release 2026-09-23 · [PyPI](https://pypi.org/project/pymilvus.model/) · [source](https://github.com/milvus-io/milvus-model)

<details><summary>README extract</summary>

The `milvus-model` library provides the integration with common embedding and reranker models for Milvus, a high performance open-source vector database built for AI applications. `milvus-model` lib is included as a dependency in `pymilvus`, the Python SDK of Milvus. ...

</details>

### pyconify

iconify for python. Universal icon framework

`pip install pyconify` · installs (wheel) · licence: BSD-3-Clause · rank 10082 · last release 2026-10-26 · [PyPI](https://pypi.org/project/pyconify/) · [source](https://github.com/pyapp-kit/pyconify)

<details><summary>README extract</summary>

Python wrapper for the Iconify API.

Iconify is a versatile icon framework that includes 100+ icon sets with more
than 100,000 icons from FontAwesome, Material Design Icons, DashIcons, Feather
Icons, EmojiOne, Noto Emoji and many other open source icon sets.

Search for icons at:

Example:
```python
import pyconify

# Info on available collections
collections = pyconify.collections()

# Info on specific collection(s)
details = pyconify.collection("fa", "fa-brands")

# Search for icons
hits = pyconify.search("python")

# Get icon data
data = pyconify.icon_data("fa-brands", "python")

# Get SVG
svg = pyconify.svg("fa-brands", "python")

...
```

Sections: pyconify, Usage, cache, freedesktop themes

</details>

### ppk2-api

API for Nordic Semiconductor's Power Profiler Kit II (PPK 2).

`pip install ppk2-api` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 10108 · last release 2023-06-09 · [PyPI](https://pypi.org/project/ppk2-api/)

_README extract left out: share-alike licence._

### pillow-jxl-plugin

Pillow plugin for JPEG-XL, using Rust for bindings.

`pip install pillow-jxl-plugin` · installs (wheel) · licence: not stated · rank 10118 · last release 2026-07-17 · [PyPI](https://pypi.org/project/pillow-jxl-plugin/)

<details><summary>README extract</summary>

Pillow plugin for JPEG-XL, using Rust for bindings.

Features:
- JPEG-XL Plugin for Pillow
- Encoder/Decoder to work with JPEG-XL using safe wrapper
- Support EXIF metadata encoding

Example:
```python
from io import BytesIO

import pillow_jxl
from PIL import Image

# Lossless encode a png image
with Image.open("example.png") as img:
    img.save("example.jxl",lossless=True)

# Encode image with JPEG-Style quality
with Image.open("example.png") as img:
    img.save("example.jxl", quality=98)

# Lossless construct from a jpeg image
...
```

Sections: pillow-jpegxl-plugin, Features, Build from source, Plugin Usage, Example

</details>

### PyQt6-WebEngine

Python bindings for the Qt WebEngine framework

`pip install PyQt6-WebEngine` · installs (wheel) · licence: GPL-3.0-only · rank 10133 · last release 2026-11-02 · [PyPI](https://pypi.org/project/PyQt6-WebEngine/)

_README extract left out: share-alike licence._

### pulumi-std

Standard library functions

`pip install pulumi-std` · installs (wheel) · licence: not stated · rank 10153 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pulumi-std/) · [source](https://github.com/pulumi/pulumi-std)

<details><summary>README extract</summary>

Standard library functions implemented as a native Pulumi provider.

Sections: pulumi-std, Function List, Build, Test, Generate inferred schema

</details>

### pagefind-bin-extended

Pagefind is a library for performant, low-bandwidth, fully static search.

`pip install pagefind-bin-extended` · installs (wheel) · licence: MIT License · rank 10155 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pagefind-bin-extended/) · [source](https://github.com/pagefind/pagefind/)

<details><summary>README extract</summary>

<!-- Note: this is a template file that is used for both the `pagefind_bin_extended` and
`pagefind_bin_extended_extended` python packages. All occurrences of `pagefind_bin_extended` will
be replaced with the actual package name. -->

A python wrapper for the `pagefind` executable.

Example:
```python
# !/usr/bin/env python3
from pagefind_bin_extended import get_executable
print(get_executable()) # yields absolute path to the executable
```

Sections: `pagefind_bin_extended`, Usage

</details>

### pyproject-toml

Project intend to implement PEP 517, 518, 621, 631 and so on.

`pip install pyproject-toml` · does not install on CPython 3.14 · licence: MIT License · rank 10174 · last release 2024-11-12 · [PyPI](https://pypi.org/project/pyproject-toml/)

<details><summary>README extract</summary>

Project intend to implement PEP 517, 518, 621, 631 and so on.

</details>

### prometheus-remote-writer

A Python package to send data using Prometheus remote write protocol.

`pip install prometheus-remote-writer` · installs (wheel) · licence: Apache Software License · rank 10178 · last release 2026-01-25 · [PyPI](https://pypi.org/project/prometheus-remote-writer/)

<details><summary>README extract</summary>

`prometheus-remote-writer` is a Python library designed to simplify the process of writing data to a database using
the Prometheus Remote Write
protocol. This library is platform-independent and aims to provide developers with an intuitive way to send time-series
data to Prometheus-compatible storage.

Features:
- Easily write data to Prometheus-compatible storage backends.
- Supports custom HTTP headers and authentication methods.
- Provides a simple and easy-to-use API.
- Supports batch data sending to improve transmission efficiency.

Example:
```python
from prometheus_remote_writer import RemoteWriter

# Create a RemoteWriter instance
writer = RemoteWriter(
    url='
    headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
)

# Prepare the data to send
data = [
    {
...

</details>

### pyfaup-rs

Python bindings for faup-rs Rust library

`pip install pyfaup-rs` · installs (wheel) · licence: GPL-3.0 · rank 10196 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pyfaup-rs/) · [source](https://github.com/ail-project/faup-rs)

_README extract left out: share-alike licence._

### PyPrind

Python Progress Bar and Percent Indicator Utility

`pip install PyPrind` · installs (wheel) · licence: BSD License · rank 10197 · last release 2021-04-18 · [PyPI](https://pypi.org/project/PyPrind/)

<details><summary>README extract</summary>

The PyPrind (Python Progress Indicator) module provides a progress
bar and a percentage indicator
object that let you track the progress of a loop structure or
other iterative computation.
Typical applications include the processing of
large data sets to provide an intuitive estimate
at runtime about the progress of the computation. ...

</details>

### python-printr

printr

`pip install python-printr` · installs from source (sdist only) · licence: not stated · rank 10209 · last release 2026-04-15 · [PyPI](https://pypi.org/project/python-printr/)

<details><summary>README extract</summary>

Python print functions to beautify output

Installation:
`pip install python-printr`

Usage:

Output:

Example:
```python
from printr import logger

logger = logger(filename='test.log')
log, current_time = logger.log, logger.current_time

log('Here') # Prints to terminal and saves message to test.log
```

</details>

### python-timeout

Random timeout between minimum and maximum values

`pip install python-timeout` · installs from source (sdist only) · licence: not stated · rank 10210 · last release 2026-06-30 · [PyPI](https://pypi.org/project/python-timeout/)

<details><summary>README extract</summary>

Random timeout between minimum and maximum values

Installation:
`pip install python-timeout`

Usage:

Example:
```python
from timeout import random_timeout, sleep

random_timeout(10, 20) # Random timeout between 10 and 20 seconds
random_timeout(from_minutes=1, to_minutes=2) # Random timeout between one and two minutes
random_timeout(from_hours=1, to_hours=2) # Random timeout between one and two hours
...
```

</details>

### python-kasa

Python API for TP-Link Kasa and Tapo devices

`pip install python-kasa` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 10214 · last release 2026-10-25 · [PyPI](https://pypi.org/project/python-kasa/) · [docs](https://python-kasa.readthedocs.io) · [source](https://github.com/python-kasa/python-kasa)

_README extract left out: share-alike licence._

### PyQtWebEngine

Python bindings for the Qt WebEngine framework

`pip install PyQtWebEngine` · installs (wheel) · licence: GPL v3 · rank 10216 · last release 2024-07-19 · [PyPI](https://pypi.org/project/PyQtWebEngine/)

_README extract left out: share-alike licence._

### ploomber-core

(no summary)

`pip install ploomber-core` · installs (wheel) · licence: Apache Software License · rank 10248 · last release 2025-07-21 · [PyPI](https://pypi.org/project/ploomber-core/)

### persisting-theory

Registries that can autodiscover values accross your project apps

`pip install persisting-theory` · installs (wheel) · licence: BSD License · rank 10257 · last release 2022-05-06 · [PyPI](https://pypi.org/project/persisting-theory/)

<details><summary>README extract</summary>

Persisting-theory is a small python utility designed to automate data discovering and access inside a list of packages. Use case: you are building an application that will have pluggable components. You want to allow these components to register data so it can be accessed by any other component of your app. ...

Example:
```python
from django.contrib import admin
admin.autodiscover()
```

Sections: Introduction, Quickstart, Setup, API, Registry.register(), Registry.validate(), Registry.prepare_data(), Registry.prepare_name(), Going meta, What the hell is that name ?

</details>

### prince

Factor analysis in Python: PCA, CA, MCA, MFA, FAMD, GPA, PGA

`pip install prince` · installs (wheel) · licence: MIT · rank 10268 · last release 2026-10-28 · [PyPI](https://pypi.org/project/prince/)

<details><summary>README extract</summary>

Prince is a Python library for multivariate exploratory data analysis in Python. It includes a variety of methods for summarizing tabular data, including principal component analysis (PCA) and correspondence analysis (CA). Prince provides efficient implementations, using a scikit-learn API.

I made Prince when I was at university, back in 2016. ...

Example:
```python
>>> import prince

>>> dataset = prince.datasets.load_decathlon()
>>> decastar = dataset.query('competition == "Decastar"')

>>> pca = prince.PCA(n_components=5)
>>> pca = pca.fit(decastar, supplementary_columns=['rank', 'points'])
>>> pca.eigenvalues_summary
          eigenvalue % of variance % of variance (cumulative)
component
...
```

...

</details>

### pytest-boorst

Guarded Rust-powered acceleration for pytest

`pip install pytest-boorst` · installs (wheel) · licence: MIT · rank 10270 · last release 2026-10-10 · [PyPI](https://pypi.org/project/pytest-boorst/) · [source](https://github.com/dnikolayev/pytest-boorst)

<details><summary>README extract</summary>

Guarded Rust-powered acceleration for pytest, targeting large batches of
duplicate ASCII parameter IDs and many explicit sibling test-file arguments.
On supported CPython 3.14 environments, it also batches assertion-location updates
during test-file rewriting. ...

Sections: pytest-boorst, Compatibility boundary, Experimental duration scheduling, Inspect a run, Experimental batched profiling, Performance evidence

</details>

### pccm

Python C++ Code Manager.

`pip install pccm` · installs (wheel) · licence: MIT License · rank 10277 · last release 2024-09-06 · [PyPI](https://pypi.org/project/pccm/)

<details><summary>README extract</summary>

Python C++ Code Manager

Only pccm 0.1.x support python 3.5, pccm >= 0.2.0 require python >= 3.6.

see introduction ppt or pdf

Sections: PCCM, Docs

</details>

### pulumi-cloudinit

A Pulumi package for creating and managing cloudinit cloud resources.

`pip install pulumi-cloudinit` · installs (wheel) · licence: Apache-2.0 · rank 10284 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pulumi-cloudinit/) · [source](https://github.com/pulumi/pulumi-cloudinit)

<details><summary>README extract</summary>

Provider for rendering cloud-init configurations.

Sections: CloudInit Provider, Node.js (Java/TypeScript), Python 3, Go, .NET, Reference

</details>

### py-ocsf-models

This is a Python implementation of the OCSF models. The models are used to represent the data of the OCSF Schema defined in https://schema.ocsf.io/.

`pip install py-ocsf-models` · installs (wheel) · licence: Apache Software License · rank 10291 · last release 2026-07-13 · [PyPI](https://pypi.org/project/py-ocsf-models/) · [docs](https://docs.prowler.cloud)

<details><summary>README extract</summary>

The `py-ocsf-models` package offers a Python implementation of the Open Cybersecurity Schema Framework (OCSF) models, facilitating the manipulation and understanding of cybersecurity data within Python applications. ...

Features:
- Comprehensive OCSF Schema Implementation: Includes models for events, findings, objects, and profiles, covering the entire OCSF Schema.
- Easy Data Manipulation: Easily create, modify, and interact with cybersecurity data structures. ...

Sections: py-ocsf-models, Features, OCSF Coverage, Usage Examples

</details>

### pptree

Pretty print trees

`pip install pptree` · installs from source (sdist only) · licence: not stated · rank 10298 · last release 2020-04-15 · [PyPI](https://pypi.org/project/pptree/)

### py-bip39-bindings

Python bindings for tiny-bip39 RUST crate

`pip install py-bip39-bindings` · installs (wheel) · licence: Apache Software License · rank 10306 · last release 2025-09-03 · [PyPI](https://pypi.org/project/py-bip39-bindings/) · [source](https://github.com/polkascan/py-bip39-bindings)

<details><summary>README extract</summary>

Python bindings for the tiny-bip39 library:

Reference to Reference to for the initial work

Example:
```python
import binascii
from bip39 import bip39_to_mini_secret, bip39_generate, bip39_validate

mnemonic = bip39_generate(12)
bip39_validate(mnemonic)

seed_array = bip39_to_mini_secret(mnemonic, "")
seed_hex = binascii.hexlify(bytearray(seed_array)).decode("ascii")
```

Sections: py-bip39-bindings, Documentation, Build wheels, Examples

</details>

### polyscope

Polyscope: A viewer and user interface for 3D data.

`pip install polyscope` · installs (wheel) · licence: MIT License · rank 10322 · last release 2026-02-26 · [PyPI](https://pypi.org/project/polyscope/) · [docs](https://polyscope.run)

<details><summary>README extract</summary>

Python bindings for Polyscope.

This library is a python wrapper and deployment system. The core library lives at See documentation at

To contribute, check out the instructions here.

Sections: polyscope-py, Deploy a new version

</details>

### paddle-python-sdk

Paddle's Python SDK for Paddle Billing

`pip install paddle-python-sdk` · installs (wheel) · licence: MIT License · rank 10328 · last release 2026-11-05 · [PyPI](https://pypi.org/project/paddle-python-sdk/)

<details><summary>README extract</summary>

Paddle Billing is the developer-first merchant of record, designed for modern SaaS, AI, mobile app, and digital product businesses. We take care of payments, tax, subscriptions, and metrics with one unified API that does it all.

This is a Python SDK that you can use to integrate Paddle Billing with applications written in Python. ...

Example:
```python
from paddle_billing import Client

paddle = Client('PADDLE_API_SECRET_KEY')
```

Sections: paddle-python-sdk, Requirements, Usage, Examples, List entities, Get an entity, Create an entity, Update an entity, Delete an entity, Error Handling, Resources, Webhook signature verification, Learn more

</details>

### pgvecto-rs

Python binding for pgvecto.rs

`pip install pgvecto-rs` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 10351 · last release 2024-10-08 · [PyPI](https://pypi.org/project/pgvecto-rs/)

<details><summary>README extract</summary>

Example:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

URL = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"
engine = create_engine(URL)
with Session(engine) as session:
    pass
```

Sections: Usage, Requirements, SQLAlchemy, Psycopg3, Django, SDK, Test

</details>

### pypcap

pypcap -- Python interface to pcap a packet capture library

`pip install pypcap` · installs from source (sdist only) · licence: not stated · rank 10355 · last release 2022-09-12 · [PyPI](https://pypi.org/project/pypcap/)

### pypi-attestations

A library to convert between Sigstore Bundles and PEP-740 Attestation objects

`pip install pypi-attestations` · installs (wheel) · licence: Apache-2.0 · rank 10362 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pypi-attestations/) · [docs](https://pypi.github.io/pypi-attestations/) · [source](https://github.com/pypi/pypi-attestations)

<details><summary>README extract</summary>

<!--- BADGES: START --->

<!--- BADGES: END --->

A library to generate and convert between Sigstore Bundles and [PEP 740]
Attestation objects.

> [!IMPORTANT]
> This library is an implementation detail within the reference implementation
> of [PEP 740]. ...

Example:
```python
from pathlib import Path

from pypi_attestations import Attestation, Distribution
from sigstore.oidc import Issuer
from sigstore.models import ClientTrustConfig
from sigstore.sign import SigningContext
from sigstore.verify import Verifier, policy

dist = Distribution.from_file(Path("test_package-0.0.1-py3-none-any.whl"))

# Sign a Python artifact
...
```

...

</details>

### papyrus-newsroom

Papyrus newsroom Python tools and CLI.

`pip install papyrus-newsroom` · does not install on CPython 3.14 · licence: MIT · rank 10370 · last release 2026-11-07 · [PyPI](https://pypi.org/project/papyrus-newsroom/) · [source](https://github.com/AnthusAI/Papyrus)

<details><summary>README extract</summary>

Papyrus is an open-source engine for a continuous, steerable feed of insight about a subject. It watches sources, decides what is relevant from an editor's include and exclude decisions, has editor agents research, write and check up to the publication's policies, and publishes the result for people and agents. ...

Sections: Papyrus, How it relates to the other repositories, Where it runs, What exists today, Quick start, How a change reaches production, Start a new Papyrus site, Where to read next

</details>

### pynamodb-mypy

mypy plugin for PynamoDB

`pip install pynamodb-mypy` · installs (wheel) · licence: not stated · rank 10400 · last release 2022-10-21 · [PyPI](https://pypi.org/project/pynamodb-mypy/)

<details><summary>README extract</summary>

A plugin for mypy which gives it deeper understanding of PynamoDB (beyond what's possible through type stubs).

Example:
```python
from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model

class MyModel(Model):
  my_key = UnicodeAttribute()
  my_value = UnicodeAttribute(null=True)

...
my_model = MyModel.get('key')
if my_model.my_value.lower() == 'foo':  # error: Item "None" of "Optional[str]" has no attribute "lower"
   print("Value is foo")
```

Sections: pynamodb-mypy, Usage, Nullable attributes, Typed model initializers

</details>

### plotbin

PlotBin: Plotting Binned Maps and Other Utilities

`pip install plotbin` · installs (wheel) · licence: Other/Proprietary License · rank 10401 · last release 2026-07-10 · [PyPI](https://pypi.org/project/plotbin/)

<details><summary>README extract</summary>

The PlotBin package contains utilities to plot binned maps and various
other general plotting utilities for two-dimensional maps.

Sections: The PlotBin Package, Documentation

</details>

### py-ed25519-zebra-bindings

Python bindings for the ed25519-zebra RUST crate

`pip install py-ed25519-zebra-bindings` · installs (wheel) · licence: Apache Software License · rank 10413 · last release 2025-09-03 · [PyPI](https://pypi.org/project/py-ed25519-zebra-bindings/) · [source](https://github.com/polkascan/py-ed25519-zebra-bindings)

<details><summary>README extract</summary>

Python bindings for the ed25519-zebra RUST crate

Example:
```python
import bip39
import ed25519_zebra

message = b"test"

# Get private and public key from seed
seed = bip39.bip39_to_mini_secret('daughter song common combine misery cotton audit morning stuff weasel flee field','')
private_key, public_key = ed25519_zebra.ed_from_seed(bytes(seed))

# Generate signature
...
```

Sections: py-ed25519-zebra-bindings, Documentation, Build wheels, Usage

</details>

### PyAVM

Simple pure-python AVM meta-data handling

`pip install PyAVM` · installs (wheel) · licence: MIT License · rank 10416 · last release 2026-03-12 · [PyPI](https://pypi.org/project/PyAVM/) · [docs](http://astrofrog.github.io/pyavm/) · [source](https://github.com/astrofrog/pyavm)

<details><summary>README extract</summary>

PyAVM is a module to represent, read, and write metadata following the
*Astronomy Visualization
Metadata* (AVM)
standard.

PyAVM supports Python 3.8 and later. No other dependencies are needed
simply to read and embed AVM meta-data.

However, the following optional dependencies are needed for more
advanced functionality:

- Numpy 1.10 or later ...

Example:
```python
>>> from pyavm import AVM
```

Sections: About, Requirements, Using PyAVM, Importing, Parsing files, Accessing and setting the meta-data, Creating an AVM object from scratch, Converting to a WCS object, Initializing from a FITS header, Initializing from a WCS object, Tagging images with AVM meta-data

</details>

### py_svg_hush

(no summary)

`pip install py_svg_hush` · installs (wheel) · licence: not stated · rank 10448 · last release 2026-02-13 · [PyPI](https://pypi.org/project/py_svg_hush/) · [docs](https://github.com/jams2/py-svg-hush) · [source](https://github.com/jams2/py-svg-hush)

### pysnow

ServiceNow HTTP client library

`pip install pysnow` · installs (wheel) · licence: MIT License · rank 10471 · last release 2021-03-06 · [PyPI](https://pypi.org/project/pysnow/)

<details><summary>README extract</summary>

Documentation

The documentation is available at

Development status

The development status of pysnow is stable; maintenence will be performed, but no new features added.

New features goes into rbw/aiosnow: a modern, asynchronous library for interacting with ServiceNow.

Author

Robert Wikman \<rbw@vault13.org\>

Credits ...

</details>

### pycookiecheat

Borrow cookies from your browser's authenticated session for use in Python scripts.

`pip install pycookiecheat` · installs (wheel) · licence: MIT · rank 10478 · last release 2024-11-03 · [PyPI](https://pypi.org/project/pycookiecheat/)

<details><summary>README extract</summary>

Borrow cookies from your browser's authenticated session for use in Python
scripts.

- Free software: MIT
- Documentation

Features:
- Returns decrypted cookies from Google Chrome, Brave, or Slack, on MacOS or
 Linux.
- Optionally outputs cookies to file (thanks to Muntashir Al-Islam!)

Example:
```python
from pycookiecheat import BrowserType, get_cookies
import requests

url = '

# Uses Chrome's default cookies filepath by default
cookies = get_cookies(url)
r = requests.get(url, cookies=cookies)

# Using an alternate browser
cookies = get_cookies(url, browser=BrowserType.CHROMIUM)
```

...

</details>

### python-digitalocean

digitalocean.com API to manage Droplets and Images

`pip install python-digitalocean` · installs (wheel) · licence: LGPL v3 · rank 10490 · last release 2021-10-02 · [PyPI](https://pypi.org/project/python-digitalocean/)

_README extract left out: share-alike licence._

### py-ulid

Python library that provides an implementation of the ULID Specification

`pip install py-ulid` · installs from source (sdist only) · licence: MIT License · rank 10491 · last release 2019-07-14 · [PyPI](https://pypi.org/project/py-ulid/)

<details><summary>README extract</summary>

The py-ulid library is a minimal and self-contained implementation of the ULID (Universally Unique Lexicographically Sortable Identifier) specification in Python.
For more information, please refer to the official specification.

UUID can be suboptimal for many uses-cases because: ...

Example:
```python
from ulid import ULID

# Instantiate the ULID class
ulid = ULID()
ulid.generate()  #01BX5ZZKBKACTAV9WEVGEMMVRZ
```

Sections: py-ulid - A ULID Implementation in Python, How to use, Seeding Time, Monotonic ULIDs, Prior Art

</details>

### python-incidentio-client

Python client for Incident.io

`pip install python-incidentio-client` · installs (wheel) · licence: MIT License · rank 10497 · last release 2025-08-15 · [PyPI](https://pypi.org/project/python-incidentio-client/) · [source](https://github.com/expobrain/python-incidentio-client)

<details><summary>README extract</summary>

A client library for accessing incident.io.

Example:
```python
from incident_io_client import Client

client = Client(base_url="
```

Sections: python-incident-io-client, Usage, Generate code

</details>

### pagefind-bin

Pagefind is a library for performant, low-bandwidth, fully static search.

`pip install pagefind-bin` · installs (wheel) · licence: MIT License · rank 10500 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pagefind-bin/) · [source](https://github.com/pagefind/pagefind/)

<details><summary>README extract</summary>

<!-- Note: this is a template file that is used for both the `pagefind_bin` and
`pagefind_bin_extended` python packages. All occurrences of `pagefind_bin` will
be replaced with the actual package name. -->

A python wrapper for the `pagefind` executable.

Example:
```python
# !/usr/bin/env python3
from pagefind_bin import get_executable
print(get_executable()) # yields absolute path to the executable
```

Sections: `pagefind_bin`, Usage

</details>

### py-multibase

Multibase implementation for Python

`pip install py-multibase` · installs (wheel) · licence: MIT License · rank 10521 · last release 2025-12-18 · [PyPI](https://pypi.org/project/py-multibase/)

<details><summary>README extract</summary>

Multibase implementation for Python

Multibase is a protocol for distinguishing base encodings and other simple string encodings, and for ensuring full compatibility with program interfaces.

It answers the question: Given data d encoded into string s, how can I tell what base d is encoded with? ...

Example:
```python
>>> # encoding a buffer
>>> from multibase import encode, decode
>>> encode('base58btc', 'hello world')
b'zStV1DL6CwTryKyV'
>>> encode('base64', 'hello world')
b'mGhlbGxvIHdvcmxk'
>>> # decoding a multibase
>>> decode('mGhlbGxvIHdvcmxk')
b'hello world'
>>> decode(b'zStV1DL6CwTryKyV')
b'hello world'
>>> decode(encode('base2', b'hello world'))
...
```

Sections: py-multibase, Sample Usage

</details>

### pylerc

Limited Error Raster Compression

`pip install pylerc` · installs (wheel) · licence: Apache Software License · rank 10550 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pylerc/)

<details><summary>README extract</summary>

LERC is an open-source raster format which supports rapid encoding and decoding for any pixel type, with user-set maximum compression error per pixel.

Lerc 4.2 adds stricter size limits for improved safety:
- Input data to encode is limited to 2 GB per band.
- Compressed Lerc blob size is limited to 2 GB per band. ...

Sections: `pylerc` is the LERC Python package, What's new in Lerc 4.2?, What's new in Lerc 4.0?, Option 1, uses numpy masked array, Option 2, uses regular numpy arrays for data and mask, General remarks

</details>

### pyobvector

A python SDK for OceanBase Vector Store, based on SQLAlchemy, compatible with Milvus API.

`pip install pyobvector` · installs (wheel) · licence: Apache-2.0 · rank 10551 · last release 2026-07-29 · [PyPI](https://pypi.org/project/pyobvector/) · [source](https://github.com/oceanbase/pyobvector.git)

<details><summary>README extract</summary>

A python SDK for OceanBase Multimodal Store (Vector Store / Full Text Search / JSON Table), based on SQLAlchemy, compatible with Milvus API.

Example:
```python
from pyobvector import *

client = MilvusLikeClient(uri="127.0.0.1:2881", user="test@test")
```

Sections: pyobvector, Build Doc, Usage, Milvus compatible mode, SQLAlchemy hybrid mode, ann_search Parameters, Embedded SeekDB mode, Hybrid Search Mode, Get SQL Query, SQL-level Hybrid Search (OceanBase >= 4.6.0), DSL Reference, Restrictions

</details>

### pdf417gen

PDF417 2D barcode generator for Python

`pip install pdf417gen` · installs (wheel) · licence: MIT License · rank 10592 · last release 2025-01-23 · [PyPI](https://pypi.org/project/pdf417gen/)

<details><summary>README extract</summary>

Easily encode your data into a 2D barcode using the PDF417 format.

Licensed under the MIT License, see LICENSE.

Example:
```python
from pdf417gen import encode, render_image, render_svg

# Some data to encode
text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

# Convert to code words
codes = encode(text)

# Generate barcode as image
image = render_image(codes)  # Pillow Image object
...
```

Sections: PDF417 barcode generator for Python, CLI, Usage, Encoding data, Columns, Render image, Render SVG, See also

</details>

### python-ironicclient

OpenStack Bare Metal Provisioning API Client Library

`pip install python-ironicclient` · installs (wheel) · licence: Apache-2.0 · rank 10608 · last release 2026-08-26 · [PyPI](https://pypi.org/project/python-ironicclient/) · [source](https://opendev.org/openstack/python-ironicclient/)

<details><summary>README extract</summary>

Features:
This is a client for the OpenStack Bare Metal API. It provides:

* a Python API: the `ironicclient` module, and
* a command-line interfaces: `openstack baremetal` ...

Example:
```python
>>> from ironicclient import client
>>>
>>> kwargs = {'os_auth_token': '3bcc3d3a03f44e3d8377f9247b0ad155',
>>>           'ironic_url': '
>>> ironic = client.get_client(1, **kwargs)
```

Sections: Python bindings for the Ironic API, Team and repository tags, Overview, Project resources, Python API, `openstack baremetal` CLI

</details>

### pagerduty-mcp

PagerDuty's official local MCP (Model Context Protocol) server which provides tools to interact with your PagerDuty account directly from your MCP-enabled client.

`pip install pagerduty-mcp` · does not install on CPython 3.14 · licence: not stated · rank 10612 · last release 2026-07-07 · [PyPI](https://pypi.org/project/pagerduty-mcp/)

<details><summary>README extract</summary>

<!-- mcp-name: io.github.PagerDuty/pagerduty-mcp -->

PagerDuty's local MCP (Model Context Protocol) server which provides tools to interact with your PagerDuty account, allowing you to manage incidents, services, schedules, event orchestrations, and more directly from your MCP-enabled client.

Sections: PagerDuty's official MCP Server, 1. Incident Command Center 🚨, 2. On-Call Manager 📅, 3. On-Call Compensation Report 💰, 4. Service Dependency Graph 🕸️, 5. Onboarding Wizard 🧙, Prerequisites, Using with MCP Clients, Cursor Integration, VS Code Integration, Trying it in VS Code Chat (Agent), Claude Desktop Integration, Running with Docker

</details>

### pocket-tts

Kyutai's pocket-sized text-to-speech!

`pip install pocket-tts` · installs (wheel) · licence: not stated · rank 10625 · last release 2026-10-21 · [PyPI](https://pypi.org/project/pocket-tts/)

<details><summary>README extract</summary>

A lightweight text-to-speech (TTS) application designed to run efficiently on CPUs.
Forget about the hassle of using GPUs and web APIs serving TTS models. With Kyutai's Pocket TTS, generating audio is just a pip install and a function call away.

Supports Python 3.10, 3.11, 3.12, 3.13 and 3.14. Requires PyTorch 2.5+. ...

Example:
```python
tts_model = TTSModel.load_model()
tts_model.to("cuda")
...
audio = tts_model.generate_audio(voice_state, "Hello world, this is a test.")
# generate_audio() returns a tensor on the same device as the model, so on GPU you need
# to move it back to CPU before calling .numpy():
...
```

...

</details>

### piecewise-rational

Shape-preserving piecewise rational cubic interpolation (Delbourgo-Gregory algorithm)

`pip install piecewise-rational` · installs (wheel) · licence: MIT License · rank 10631 · last release 2026-01-13 · [PyPI](https://pypi.org/project/piecewise-rational/) · [source](https://github.com/vollib/piecewise-rational)

<details><summary>README extract</summary>

Shape-preserving piecewise rational cubic interpolation using the Delbourgo-Gregory algorithm.

Features:
- Shape-preserving interpolation (maintains monotonicity and convexity)
- Control parameters for fitting second derivatives
- High numerical precision

Example:
```python
from piecewise_rational import rational_cubic_interpolation

# Interpolate at x=0.5 given endpoints and derivatives
x_l, x_r = 0.0, 1.0      # interval
y_l, y_r = 0.0, 1.0      # values at endpoints
d_l, d_r = 1.0, 1.0      # derivatives at endpoints
r = 0.0                   # control parameter

...
```

Sections: piecewise-rational, Usage, Features, References

</details>

### pydantic-string-url

Pydantic URL types that are based on the str class.

`pip install pydantic-string-url` · installs (wheel) · licence: MIT License · rank 10702 · last release 2024-09-15 · [PyPI](https://pypi.org/project/pydantic-string-url/) · [docs](https://github.com/patrsc/pydantic-string-url) · [source](https://github.com/patrsc/pydantic-string-url)

<details><summary>README extract</summary>

Pydantic URL types that are based on the `str` class.

Since Pydantic v2 the types realated to
URLs are not based on the
standard Python `str` class any more.

This decision comes with some issues:
* URLs cannot be directly passed to library packages that expect `str`, you must use `str(url)`
 instead
* some internal normalization is done, so the ...

Example:
```python
"""Example."""

from pydantic import BaseModel, TypeAdapter, ValidationError

from pydantic_string_url import HttpUrl

# Use inside BaseModel
class User(BaseModel):
    """A user."""

    name: str
    age: int
    homepage: HttpUrl

user = {"name": "John Doe", "age": 33, "homepage": "

...
```

Sections: pydantic-string-url, Introduction, Usage

</details>

### PyStaticConfiguration

A python library for loading static configuration

`pip install PyStaticConfiguration` · installs (wheel) · licence: Apache Software License · rank 10770 · last release 2022-10-22 · [PyPI](https://pypi.org/project/PyStaticConfiguration/)

### pyprctl

An interface to Linux's prctl() syscall written in pure Python using ctypes.

`pip install pyprctl` · installs (wheel) · licence: MIT License · rank 10780 · last release 2021-10-26 · [PyPI](https://pypi.org/project/pyprctl/) · [docs](https://pyprctl.readthedocs.io/en/latest)

<details><summary>README extract</summary>

An interface to Linux's prctl() system call (and Linux capabilities in general) written in pure Python using ctypes.

Documentation

</details>

### pydantic-mongo

Document object mapper for pydantic and pymongo

`pip install pydantic-mongo` · installs (wheel) · licence: MIT License · rank 10781 · last release 2025-04-18 · [PyPI](https://pypi.org/project/pydantic-mongo/)

<details><summary>README extract</summary>

A Python library that offers an easy-to-use Repository pattern for MongoDB, supporting both synchronous and asynchronous operations. It simplifies working with databases by providing a clear interface for CRUD (Create, Read, Update, Delete) operations using Pydantic models. ...

Features:
* Asynchronous and Synchronous support
* Pydantic models integration
* Type-safe MongoDB operations
* Cursor-based pagination

Example:
```python
from bson import ObjectId
from pydantic import BaseModel
from pydantic_mongo import AbstractRepository, PydanticObjectId
from pymongo import MongoClient
from typing import Optional, List

# Define your models
class Foo(BaseModel):
   count: int
   size: float = None

class Bar(BaseModel):
   apple: str = 'x'
   banana: str = 'y'

...
```

...

</details>

### pickle-mixin

Makes un-pickle-able objects pick-able.

`pip install pickle-mixin` · installs from source (sdist only) · licence: MIT License · rank 10798 · last release 2017-04-09 · [PyPI](https://pypi.org/project/pickle-mixin/)

<details><summary>README extract</summary>

Makes un-pickle-able objects pick-able.

Example:
```python
python -c "import pickle_mixin; pickle_mixin.test()"
```

Sections: pickle-mixin, Running the tests, Usage, Pickle by initialisation, Mixing classes with and without slots

</details>

### panns-inference

panns_inference: audio tagging and sound event detection inference toolbox

`pip install panns-inference` · installs (wheel) · licence: MIT License · rank 10803 · last release 2023-03-26 · [PyPI](https://pypi.org/project/panns-inference/)

<details><summary>README extract</summary>

panns_inference provides an easy to use Python interface for audio tagging and sound event detection. The audio tagging and sound event detection models are trained from PANNs: Large-Scale Pretrained Audio Neural Networks for Audio Pattern Recognition:

Example:
```python
import librosa
import panns_inference
from panns_inference import AudioTagging, SoundEventDetection, labels

audio_path = 'examples/R9_ZSCveAHg_7s.wav'
(audio, _) = librosa.core.load(audio_path, sr=32000, mono=True)
audio = audio[None, :]  # (batch_size, segment_samples)

print('------ Audio tagging ------')
...
```

Sections: PANNs inferece, Usage, Results

</details>

### pynautobot

Nautobot API client library

`pip install pynautobot` · installs (wheel) · licence: Apache Software License · rank 10814 · last release 2026-09-21 · [PyPI](https://pypi.org/project/pynautobot/) · [docs](https://docs.nautobot.com/projects/pynautobot/) · [source](https://github.com/nautobot/pynautobot)

<details><summary>README extract</summary>

Python API client library for Nautobot.

> pynautobot was initially developed as a fork of pynetbox.
> pynetbox was originally developed by Zach Moody at DigitalOcean and the NetBox Community.

The complete documentation for pynautobot can be found on our docs page.

Questions? Comments? Join us in the #nautobot Slack channel on Network to Code!

Example:
```python
import pynautobot

nautobot = pynautobot.api(
    url="
    token="d6f4e314a5b5fefd164995169f28ae32d987704f",
)
```

Sections: pynautobot, Using pip, Using poetry, Quick Start, Jobs, Queries, Threading, Versioning, Retry logic, Related projects

</details>

### PyQtWebEngine-Qt5

The subset of a Qt installation needed by PyQtWebEngine.

`pip install PyQtWebEngine-Qt5` · installs (wheel) · licence: LGPL v3 · rank 10821 · last release 2026-05-21 · [PyPI](https://pypi.org/project/PyQtWebEngine-Qt5/)

_README extract left out: share-alike licence._

### pyqir

(no summary)

`pip install pyqir` · installs (wheel) · licence: MIT License · rank 10836 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyqir/)

<details><summary>README extract</summary>

The `pyqir` package provides the ability to generate
QIR as well as an easy way to
parse and analyze QIR.

QIR generation is intended to be used by code automating translation processes
enabling the conversion in some format to QIR via Python; i.e., this is a
low-level API intended to be used as a bridge to existing Python frameworks
enabling the ...

Example:
```python
from pyqir import BasicQisBuilder, SimpleModule

module = SimpleModule("Bell", num_qubits=2, num_results=2)
qis = BasicQisBuilder(module.builder)

qis.h(module.qubits[0])
qis.cx(module.qubits[0], module.qubits[1])

qis.mz(module.qubits[0], module.results[0])
qis.mz(module.qubits[1], module.results[1])

print(module.ir())
```

Sections: PyQIR, Examples, Generation, LLVM Opaque Pointers

</details>

### pyLDAvis

Interactive topic model visualization. Port of the R package.

`pip install pyLDAvis` · installs (wheel) · licence: BSD License · rank 10857 · last release 2023-04-23 · [PyPI](https://pypi.org/project/pyLDAvis/)

<details><summary>README extract</summary>

Python library for interactive topic model visualization.
This is a port of the fabulous R package by Carson Sievert and Kenny Shirley.

pyLDAvis is designed to help users interpret the topics in a topic model that has been fit to a corpus of text data. ...

Sections: pyLDAvis, Usage, Video demos, More documentation

</details>

### pycytominer

Python package for processing image-based profiling data

`pip install pycytominer` · installs (wheel) · licence: BSD-3-Clause · rank 10864 · last release 2026-08-13 · [PyPI](https://pypi.org/project/pycytominer/) · [source](https://github.com/cytomining/pycytominer)

<details><summary>README extract</summary>

Pycytominer is a toolkit for processing high dimensional readouts from high-throughput image-based profiling experiments.
The tool is most often used for processing data through the following pipeline:

> Figure 1. The standard image-based profiling experiment and the role of Pycytominer. ...

Example:
```python
# Real world example
import pandas as pd
import pycytominer

commit = "da8ae6a3bc103346095d61b4ee02f08fc85a5d98"
url = f"

df = pd.read_csv(url)

normalized_df = pycytominer.normalize(
    profiles=df,
    method="standardize",
    samples="Metadata_broad_sample == 'DMSO'"
)
```

...

</details>

### pyModbusTCP

A simple Modbus/TCP library for Python

`pip install pyModbusTCP` · installs (wheel) · licence: MIT · rank 10894 · last release 2026-09-30 · [PyPI](https://pypi.org/project/pyModbusTCP/)

<details><summary>README extract</summary>

A simple Modbus/TCP client library for Python.
pyModbusTCP is pure Python code without any extension or external module dependency.

Since version 0.1.0, a server is also available.

The module is currently test on Python 3.10, 3.11, 3.12, 3.13 and 3.14.

For Linux, Mac OS and Windows.

Documentation of the last release is available online at

Example:
```python
from pyModbusTCP.client import ModbusClient
```

Sections: pyModbusTCP, Tests, Documentation, Setup, Usage example, include (for all samples), module init (TCP always open), module init (TCP open/close for each request), Read 2x 16 bits registers at modbus address 0, Write value 44 and 55 to registers at modbus address 10

</details>

### pythena

A simple athena wrapper leveraging boto3 to execute queries and return results while only requiring a database and a query string.

`pip install pythena` · installs (wheel) · licence: Mozilla Public License Version 2.0 · rank 10899 · last release 2020-09-15 · [PyPI](https://pypi.org/project/pythena/)

<details><summary>README extract</summary>

This is a simple python module that will allow you to query athena the same way the AWS Athena console would. It only requires a database name and query string.

Example:
```python
import pythena

athena_client = pythena.Athena("mydatabase")

# Returns results as a pandas dataframe
df = athena_client.execute("select * from mytable")

print(df.sample(n=2)) # Prints 2 rows from your dataframe
```

Sections: pythena, Setup, Simple Usage, Connect to Database, athena_client.execute(), Full Usage Examples, Note

</details>

### pivot

High-performance Python pipeline tool with automatic code change detection

`pip install pivot` · does not install on CPython 3.14 · licence: MIT · rank 10910 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pivot/) · [docs](https://sjawhar.github.io/pivot/) · [source](https://github.com/sjawhar/pivot)

<details><summary>README extract</summary>

Change your code. Pivot knows what to run.

Pivot is a Python pipeline tool with automatic code change detection. Stages are plain
Python functions; you wire them together by calling them inside a `Pipeline` block, and
Pivot works out what needs to re-run.

- Automatic code change detection using Python introspection ...

Example:
```python
# pipeline.py
import pandas as pd

from pivot import Pipeline, StageParams, stage

class CleanParams(StageParams):
    min_value: int = 0

@stage
def clean(records: pd.DataFrame, params: CleanParams) -> pd.DataFrame:
    kept = records.dropna()
    return kept[kept["value"] >= params.min_value]

@stage
def summarize(rows: pd.DataFrame) -> dict:
...
```

Sections: Pivot: High-Performance Python Pipeline Tool, Quick Start, Learn More

</details>

### parquet-tools

Easy install parquet-tools

`pip install parquet-tools` · installs (wheel) · licence: MIT License · rank 10937 · last release 2024-03-19 · [PyPI](https://pypi.org/project/parquet-tools/) · [source](https://github.com/ktrueda/parquet-tools)

<details><summary>README extract</summary>

This is a pip installable parquet-tools.
In other words, parquet-tools is a CLI tools of Apache Arrow.
You can show parquet file content/schema on local disk or on Amazon S3.
It is incompatible with original parquet-tools.

Features:
- Read Parquet data (local file or file on S3)
- Read Parquet metadata/schema (local file or file on S3)

Example:
```python
# ###### file meta data
created_by: parquet-cpp version 1.5.1-SNAPSHOT
num_columns: 3
num_rows: 3
num_row_groups: 1
format_version: 1.0
serialized_size: 2226

# ###### Columns
one
two
three

# ###### Column(one)
name: one
path: one
max_definition_level: 1
max_repetition_level: 0
physical_type: DOUBLE
logical_type: None
...
```

...

</details>

### pulumi-google-native

A native Pulumi package for creating and managing Google Cloud resources.

`pip install pulumi-google-native` · installs (wheel) · licence: Apache-2.0 · rank 10960 · last release 2023-11-29 · [PyPI](https://pypi.org/project/pulumi-google-native/) · [source](https://github.com/pulumi/pulumi-google-native)

<details><summary>README extract</summary>

Sections: Node.js (JavaScript/TypeScript), Python, Go, .NET, Concepts, Configuring credentials, Building, Dependencies, Building locally, Running an example

</details>

### python-octaviaclient

Octavia client for OpenStack Load Balancing

`pip install python-octaviaclient` · installs (wheel) · licence: Apache Software License · rank 10973 · last release 2026-08-27 · [PyPI](https://pypi.org/project/python-octaviaclient/)

<details><summary>README extract</summary>

Octavia client for OpenStack Load Balancing

This is an OpenStack Client (OSC) plugin for Octavia, an OpenStack
Load Balancing project.

For more information about Octavia see:

For more information about the OpenStack Client see:

* Free software: Apache license

Sections: python-octaviaclient, Getting Started

</details>

### periodiq

Simple Scheduler for Dramatiq Task Queue

`pip install periodiq` · installs (wheel) · licence: LGPL-3.0-or-later · rank 10981 · last release 2026-04-16 · [PyPI](https://pypi.org/project/periodiq/)

_README extract left out: share-alike licence._

### python-calendarific

Official Python library for the Calendarific Global Holiday API - https://calendarific.com

`pip install python-calendarific` · installs from source (sdist only) · licence: MIT · rank 10990 · last release 2019-02-22 · [PyPI](https://pypi.org/project/python-calendarific/)

### py-multicodec

Multicodec implementation in Python

`pip install py-multicodec` · installs (wheel) · licence: MIT License · rank 10994 · last release 2025-12-18 · [PyPI](https://pypi.org/project/py-multicodec/)

<details><summary>README extract</summary>

Multicodec implementation in Python

`multicodec` *is a self-describing multiformat*, it wraps other formats with a tiny bit of self-description.

A multicodec identifier is both a varint and the code identifying the following data, this means that the most
significant bit of every multicodec code is reserved to signal the continuation. ...

Example:
```python
>>> from multicodec import add_prefix, remove_prefix, get_codec
>>> # adding a prefix to existing data
>>> add_prefix('sha2-256', b'EiC5TSe5k00')
b'\x12EiC5TSe5k00'
>>> # removing prefix from prefixed data
>>> remove_prefix(b'\x12EiC5TSe5k00')
EiC5TSe5k00
>>> # get codec used to prefix the prefixed data
>>> get_codec(b'\x12EiC5TSe5k00')
'sha2-256'
```

Sections: py-multicodec, Sample Usage, Code Management, Updating the lookup table

</details>

### parfive

A HTTP and FTP parallel file downloader.

`pip install parfive` · installs (wheel) · licence: not stated · rank 11055 · last release 2026-01-27 · [PyPI](https://pypi.org/project/parfive/) · [source](https://parfive.readthedocs.io/)

<details><summary>README extract</summary>

A parallel file downloader using asyncio. parfive can handle downloading
multiple files in parallel as well as downloading each file in a number of
chunks.

Example:
```python
from parfive import Downloader
dl = Downloader()
dl.enqueue_file(" path="./")
files = dl.download()
```

Sections: Parfive, Usage, Results, Handling Errors, Requirements

</details>

### pyvista-zstd

VTK zstandard compression library.

`pip install pyvista-zstd` · installs (wheel) · licence: MIT · rank 11060 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pyvista-zstd/)

<details><summary>README extract</summary>

Seamlessly compress VTK datasets using Zstandard.

Install `pyvista-zstd[network]` to read an individual field array from a remote
container. The producer exports a small sidecar with `build_range_index`. Serve
the container with HTTP byte-range support and the sidecar's matching ETag. ...

Example:
```python
import pyvista_zstd

# create and write out
ds = pv.Sphere()
pyvista_zstd.write(ds, "dataset.pv")

# read in and show these are identical
ds_in = pyvista_zstd.read("dataset.pv")
assert ds == ds_in
```

Sections: pyvista-zstd, Partial reads over HTTPS, Usage, PyVista Integration, The C library, Rational, VTK Compression with Zstandard: pyvista-zstd, Additional Information

</details>

### pythonping

A simple way to ping in Python

`pip install pythonping` · installs (wheel) · licence: MIT · rank 11071 · last release 2022-10-25 · [PyPI](https://pypi.org/project/pythonping/)

<details><summary>README extract</summary>

PythonPing is simple way to ping in Python. With it, you can send ICMP Probes to remote devices like
you would do from the terminal. PythonPing is modular, so that you can run it in a script as a
standalone function, or integrate its components in a fully-fledged application.

Features:
All operating systems allow programs to create TCP or UDP sockets without requiring particular
permissions. However, ping runs in ICMP (which is neither TCP or UDP). ...

Example:
```python
from pythonping import ping

ping('127.0.0.1', verbose=True)
```

Sections: pythonping, Basic Usage, FAQ, Do I need privileged mode or root?, Why do I need to be root to use pythonping?, Advanced Usage, Code Structure, Top Level Directory Layout, Utils, Network, Payload Provider, ICMP, Executor, Init

</details>

### prisma-sase

Python3 SDK for the Prisma SASE AppFabric

`pip install prisma-sase` · installs from source (sdist only) · licence: MIT License · rank 11084 · last release 2026-07-22 · [PyPI](https://pypi.org/project/prisma-sase/)

<details><summary>README extract</summary>

Python3 SDK for the Prisma SASE AppFabric

Intended to be a small, lightweight SDK wrapper around the Prisma SASE API for easy use.
Initial version requires knowledge of JSON/Dict objects for POST/PUT/PATCH operations.

* Active Prisma SASE Account
* Python >= 3.7

 * Requests - <
 * Websockets >= 8.1 - <
 * urllib3 >= 2.0.0 - <

Example:
```python
# Import the Prisma SASE SDK API constructor and JSON response pretty printer
from prisma_sase import API, jd

# Instantiate the Prisma SASEx API constructor
sdk = API()

# Call Prisma SASE API login using the Interactive helpers (Handle SAML2.0 login and MSP functions too!).
...
```

Sections: Palo Alto Networks Prisma SASE Python SDK v6.8.1b1, Synopsis, Requirements, Code Example, Version, For more info

</details>

### packvers

Core utilities for Python packages. Fork to support LegacyVersion

`pip install packvers` · installs (wheel) · licence: Apache Software License; BSD License · rank 11104 · last release 2022-12-22 · [PyPI](https://pypi.org/project/packvers/)

<details><summary>README extract</summary>

packvers is friendly fork of packaging to work around the drop for
LegacyVersion support. See

Reusable core utilities for various Python Packaging
interoperability specifications. ...

Sections: packvers, Documentation, Discussion, 21.5 - 2022-12-22, 21.4 - 2022-12-22, 21.3 - 2021-11-17, 21.2 - 2021-10-29, 21.1 - 2021-10-29, 21.0 - 2021-07-03, 20.9 - 2021-01-29, 20.8 - 2020-12-11, 20.7 - 2020-11-28, 20.6 - 2020-11-28, 20.5 - 2020-11-27

</details>

### prowler

Prowler is an Open Source security tool to perform AWS, GCP and Azure security best practices assessments, audits, incident response, continuous monitoring, hardening and forensics readiness. It contains hundreds of controls covering CIS, NIST 800, NIST CSF, CISA, RBI, FedRAMP, PCI-DSS, GDPR, HIPAA, FFIEC, SOC2, GXP, AWS Well-Architected Framework Security Pillar, AWS Foundational Technical Review (FTR), ENS (Spanish National Security Scheme) and your custom security frameworks.

`pip install prowler` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 11106 · last release 2026-11-06 · [PyPI](https://pypi.org/project/prowler/) · [docs](https://docs.prowler.com)

<details><summary>README extract</summary>

Prowler is the Open Cloud Security Platform trusted by thousands to automate security and compliance in any cloud environment. With thousands of ready-to-use checks and compliance frameworks, Prowler delivers real-time, customizable monitoring and seamless integrations, making cloud security simple, scalable, and cost-effective for organizations ...

Sections: Description, Prowler Cloud & Prowler Local Server, Prowler CLI, Prowler Local Dashboard, Attack Paths, Neo4j sink, Neptune sink, Prowler at a Glance, Prowler Local Server, Docker Compose, Requirements, Commands, From GitHub

</details>

### phone-iso3166

Phonenumber to Country (ISO 3166-1) mapping

`pip install phone-iso3166` · installs (wheel) · licence: MIT License · rank 11124 · last release 2022-08-18 · [PyPI](https://pypi.org/project/phone-iso3166/)

<details><summary>README extract</summary>

Small project to map an E.164 (international) phone number to the
ISO-3166-1 alpha 2 (two letter) country code, associated with that number.

Also provides mapping for E.212 (mobile network codes, mcc+mnc) to the country.

The package has no dependencies, and works on Python 3.6+ and PyPy 3.6+.

Example:
```python
>>> from phone_iso3166.country import *
>>> phone_country(45)
'DK'
>>> phone_country('+1 202-456-1111')
'US'
>>> phone_country(14412921234)
'BM'
>>> network_country(238, 1)
'DK'
```

Sections: Phone-ISO3166, Simple Usage, Network names and codes, More information

</details>

### piano-transcription-inference

Piano transcription inference toolbox

`pip install piano-transcription-inference` · installs (wheel) · licence: MIT License · rank 11125 · last release 2025-01-26 · [PyPI](https://pypi.org/project/piano-transcription-inference/)

<details><summary>README extract</summary>

This toolbox is a piano transcription inference package that can be easily installed. Users can transcribe their favorite piano recordings to MIDI files after installation. To see how the piano transcription system is trained, please visit:

Here is a demo of our piano transcription system:

Example:
```python
import librosa
from piano_transcription_inference import PianoTranscription, sample_rate

# Load audio
audio, _ = librosa.load(path=audio_path, sr=sample_rate, mono=True)

# Transcriptor
transcriptor = PianoTranscription(device='cuda', checkpoint_path=None)  # device: 'cuda' | 'cpu'

# Transcribe and write out to MIDI file
...
```

Sections: Piano transcription inference, Demos, Usage, Visualization of piano transcription, FAQs, Applications

</details>

### py3-validate-email

Email validator with regex, blacklisted domains and SMTP checking.

`pip install py3-validate-email` · installs (wheel) · licence: LGPL · rank 11174 · last release 2024-06-01 · [PyPI](https://pypi.org/project/py3-validate-email/)

_README extract left out: share-alike licence._

### pcodec

Good compression for numerical sequences

`pip install pcodec` · installs (wheel) · licence: not stated · rank 11198 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pcodec/) · [source](https://github.com/pcodec/pcodec)

<details><summary>README extract</summary>

[][pypi-url]

Pcodec is a codec for numerical sequences. Example usage:

For pcodec's uses, design, and benchmarks, see the main repo.

Documentation is served
on readthedocs.
It is sometimes incomplete; the types and functions largely mirror those of the
more thoroughly documented Rust API.

Example:
```python
>>> from pcodec import standalone, ChunkConfig
>>> import numpy as np
>>>
>>> np.random.seed(0)
>>> nums = np.random.normal(size=1000000)
>>>
>>> # compress
>>> compressed = standalone.simple_compress(nums, ChunkConfig())
>>> print(f'compressed to {len(compressed)} bytes')
compressed to 6946280 bytes
>>>
>>> # decompress
...
```

</details>

### pandas_access

A tiny, subprocess-based tool for reading a MS Access database(.rdb) as a Pandas DataFrame.

`pip install pandas_access` · installs from source (sdist only) · licence: License :: OSI Approved :: MIT License · rank 11202 · last release 2016-06-07 · [PyPI](https://pypi.org/project/pandas_access/)

<details><summary>README extract</summary>

A tiny, `subprocess`-based tool for reading a
MS Access
database (`.rdb`) as a Pandas
DataFrame.

Example:
```python
import pandas_access as mdb

# Listing the tables.
for tbl in mdb.list_tables("my.mdb"):
    print(tbl)

# Read a small table.
df = pandas_access.read_table("my.mdb", "MyTable")

# Read a huge table.
accumulator = []
for chunk in pandas_access.read_table("my.mdb", "MyTable", chunksize=10000):
    accumulator.append(f(chunk))
```

Sections: What is this?, Usage

</details>

### pytest-helpers-namespace

Pytest Helpers Namespace Plugin

`pip install pytest-helpers-namespace` · installs (wheel) · licence: Apache Software License · rank 11233 · last release 2021-12-29 · [PyPI](https://pypi.org/project/pytest-helpers-namespace/) · [docs](https://pytest-helpers-namespace.readthedocs.io) · [source](https://github.com/saltstack/pytest-helpers-namespace)

<details><summary>README extract</summary>

This plugin does not provide any helpers to pytest, it does, however,
provide a helpers namespace in pytest which enables you to register helper
functions in your `conftest.py` to be used within your tests without having
to import them.

Features:
* Provides a `helpers` pytest namespace which can be used to register
 helper functions without requiring you to import them on your actual tests to
 use them.

Example:
```python
import pytest

@pytest.helpers.register
def foo(bar):
    """
    this dumb helper function will just return what you pass to it
    """
    return bar
```

Sections: Pytest Helpers Namespace, Features, Requirements, Usage, Documentation

</details>

### pan-python

Multi-tool set for Palo Alto Networks PAN-OS, Panorama, WildFire and AutoFocus

`pip install pan-python` · installs (wheel) · licence: ISC · rank 11235 · last release 2026-06-18 · [PyPI](https://pypi.org/project/pan-python/)

<details><summary>README extract</summary>

`pan-python` is a Python package for Palo Alto Networks
Next-Generation Firewalls, WildFire and AutoFocus. It provides
several components:

- Python and command line interface to the PAN-OS and Panorama XML API
- Command line program for managing PAN-OS XML configurations
- Python and command line interface to the WildFire API ...

Sections: pan-python, Documentation

</details>

### polars-ols

Polars Least Squares Extension

`pip install polars-ols` · installs (wheel) · licence: not stated · rank 11252 · last release 2024-08-25 · [PyPI](https://pypi.org/project/polars-ols/)

<details><summary>README extract</summary>

Supports linear model estimation in Polars.

This package provides efficient rust implementations of common linear
regression variants (OLS, WLS, Ridge, Elastic Net, Non-negative least squares, Recursive least squares) and exposes
them as simple polars expressions which can easily be integrated into your workflow.

Features:
1. High Performance: implementations are written in rust and make use of optimized rust linear-algebra crates & LAPACK routines. See benchmark section.
2. ...

Example:
```python
import polars as pl
import polars_ols as pls  # registers 'least_squares' namespace

df = pl.DataFrame({"y": [1.16, -2.16, -1.57, 0.21, 0.22, 1.6, -2.11, -2.92, -0.86, 0.47],
                   "x1": [0.72, -2.43, -0.63, 0.05, -0.07, 0.65, -0.02, -1.64, -0.92, -0.27],
...
```

...

</details>

### pymaven-patch

Python access to maven. nexB advanced patch.

`pip install pymaven-patch` · installs (wheel) · licence: Apache-2 · rank 11278 · last release 2024-03-21 · [PyPI](https://pypi.org/project/pymaven-patch/)

<details><summary>README extract</summary>

Features:
Pymaven is a Python library for interfacing with the maven build system. There
are two major interfaces:

* pymaven.client provides a basic maven repository client
* pymaven.pom provides a Pom object that can provide progromatic access to
 a maven ...

Sections: Pymaven, Overview

</details>

### piper-sdk

A sdk to control Agilex piper arm

`pip install piper-sdk` · installs (wheel) · licence: MIT License · rank 11290 · last release 2026-07-31 · [PyPI](https://pypi.org/project/piper-sdk/) · [source](https://github.com/agilexrobotics/piper_sdk)

<details><summary>README extract</summary>

|Ubuntu |STATE|

|||
|||
|||

Test:

|PYTHON |STATE|

|||
|||
|||

Sections: Piper SDK, Notes, Contact Us

</details>

### percentify

Data Exploratory stats and Quality diagnostics for pandas and Polars DataFrames. One easy call each.

`pip install percentify` · installs (wheel) · licence: Apache Software License · rank 11307 · last release 2026-07-13 · [PyPI](https://pypi.org/project/percentify/)

<details><summary>README extract</summary>

80% of the checks you run on every dataset. 20% of the code.

Exploratory stats and data-quality diagnostics for pandas and Polars DataFrames. One call each.

> [!TIP]
> ⚡ Polars is first-class, not an afterthought. Pass a Polars DataFrame or Series and get the same kind straight back, with no flag and no manual conversion. ...

Example:
```python
import pandas as pd
from percentify import missing

df = pd.DataFrame({
    "salary": [50000, None, 60000, None],
    "age":    [25, 30, None, 40],
    "city":   ["NY", "LA", "SF", "LA"],
})

missing(df)
# column  missing_pct
# 0  salary         50.0
# 1     age         25.0
# 2    city          0.0
```

Sections: ⭐ The flagship: `profiler`, 📖 Documentation, Quick example, What's inside, 🛟 Friendly by design

</details>

### pydlt

A pyre-python library to handle AUTOSAR DLT.

`pip install pydlt` · installs (wheel) · licence: MIT License · rank 11321 · last release 2025-03-07 · [PyPI](https://pypi.org/project/pydlt/) · [source](https://github.com/mikiepure/pydlt)

<details><summary>README extract</summary>

A pyre-python library to handle AUTOSAR DLT protocol, which is based on
AUTOSAR Specification of Diagnostic Log and Trace V1.2.0 R4.0 Rev3, Section 7.7 Protocol Specification.

Example:
```python
from pydlt import (
    ArgumentString,
    DltFileWriter,
    DltMessage,
    MessageLogInfo,
    MessageType,
    StorageHeader,
)

# Create DLT message
msg1 = DltMessage.create_verbose_message(
    [ArgumentString("hello, pydlt!")],
    MessageType.DLT_TYPE_LOG,
    MessageLogInfo.DLT_LOG_INFO,
    "App",
    "Ctx",
    message_counter=0,
...
```

Sections: PyDLT, Quick Start, Write messages to DLT file, Read messages from DLT file, Limitation

</details>

### pytest-jira-xray

pytest plugin to integrate tests with JIRA XRAY

`pip install pytest-jira-xray` · installs (wheel) · licence: Apache-2.0 · rank 11332 · last release 2026-04-24 · [PyPI](https://pypi.org/project/pytest-jira-xray/)

<details><summary>README extract</summary>

pytest-jira-xray is a plugin for pytest that uploads test results to JIRA XRAY.

Example:
```python
# -- FILE: test_example.py

import pytest

@pytest.mark.xray('JIRA-1')
def test_foo():
    assert True

@pytest.mark.xray(['JIRA-2', 'JIRA-3'])
def test_bar():
    assert True
```

Sections: pytest-jira-xray, Usage, Upload results, Jira authentication, Attach test evidences, Hooks, IntelliJ integration, Troubleshooting, `Error message from server: fixVersions: fixVersions`, References

</details>

### parameter-expansion-patched

Shell parameter expansion in Python. Patched by co-maintainer for a PyPI release.

`pip install parameter-expansion-patched` · installs (wheel) · licence: Apache Software License · rank 11333 · last release 2022-05-04 · [PyPI](https://pypi.org/project/parameter-expansion-patched/)

<details><summary>README extract</summary>

This is an experimental Python library to enable
POSIX parameter expansion in a string.
It supports also a subset of Bash parameter expansion.

Note that this is a fork from upstream to support proper release on PyPI.

This repo is released at
 on PyPI.

Upstream is less active lately at

Features:
One reason is that it may be security risk. Another reason is to
support lightweight analysis or evaluation of shell parameters with
few system dependencies and outside of a running shell. ...

Example:
```python
>>> from parameter_expansion import expand
>>> foo = 'abc/123-def.ghi'
>>> # Bland Expansion
>>> expand('abc $foo abc')
'abc abc/123-def.ghi abc'
>>> expand('abc${foo}abc')
'abcabc/123-def.ghiabc'
>>>
>>> # Default Value Expansion
>>> expand('-${foo:-bar}-')
'-abc/123-def.ghi-'
...

</details>

### py-cid

Self-describing content-addressed identifiers for distributed systems

`pip install py-cid` · installs (wheel) · licence: MIT · rank 11358 · last release 2026-02-13 · [PyPI](https://pypi.org/project/py-cid/) · [docs](https://py-cid.readthedocs.io) · [source](https://github.com/ipld/py-cid)

<details><summary>README extract</summary>

CID is a format for referencing content in distributed information systems,
like IPFS.
It leverages content addressing,
cryptographic hashing, and
self-describing formats.

It is the core identifier used by IPFS and IPLD.

CID is a self-describing content-addressed identifier.

It uses cryptographic hashes to achieve content addressing. ...

Example:
```python
>>> from cid import make_cid
>>> make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
CIDv0(version=0, codec=dag-pb, multihash=b"\x12 \xb9M'\xb9\x93M>\x08\xa5.R\xd7\xda}\xab\xfa\xc4\x84..")

>>> cid = make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
>>> print(cid.version, cid.codec, cid.multihash)

>>> print(cid.encode())
...
```

Sections: CID (Content IDentifier), What is CID ?, Sample Usage, Other info

</details>

### py-horned-owl

(no summary)

`pip install py-horned-owl` · installs (wheel) · licence: LGPL-3.0-or-later · rank 11361 · last release 2026-09-23 · [PyPI](https://pypi.org/project/py-horned-owl/)

_README extract left out: share-alike licence._

### pulumi-twingate

A Pulumi package for creating and managing Twingate cloud resources.

`pip install pulumi-twingate` · installs from source (sdist only) · licence: Apache-2.0 · rank 11377 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pulumi-twingate/) · [source](https://github.com/Twingate/pulumi-twingate)

<details><summary>README extract</summary>

The Twingate Resource Provider lets you manage Twingate resources.

Sections: Twingate Resource Provider, Node.js (JavaScript/TypeScript), Python, Go, .NET, Configuration, Reference, Building the Provider Locally, Prerequisites, Build Steps, Common Errors, Run workflows locally

</details>

### pycowsay

(no summary)

`pip install pycowsay` · installs (wheel) · licence: License :: OSI Approved :: MIT License · rank 11385 · last release 2023-10-18 · [PyPI](https://pypi.org/project/pycowsay/)

<details><summary>README extract</summary>

A talking cow!

Use pipx to run without permanently installing

Sections: pycowsay, Run

</details>

### protobuf-decoder

Decode protobuf without proto file

`pip install protobuf-decoder` · installs (wheel) · licence: MIT License · rank 11421 · last release 2024-02-25 · [PyPI](https://pypi.org/project/protobuf-decoder/)

<details><summary>README extract</summary>

Simple protobuf decoder for python

The goal of this project is decode protobuf binary without proto files

Example:
```python
"""
# proto
message Test1 {
  string a = 1;
}

# message
{
  "a": "테스트"
}

# binary
0A 09 ED 85 8C EC 8A A4 ED 8A B8
"""
from protobuf_decoder.protobuf_decoder import Parser

test_target = "0A 09 ED 85 8C EC 8A A4 ED 8A B8"
parsed_data = Parser().parse(test_target)
...
```

Sections: Protobuf Decoder, Motivation, Simple Examples, Nested Protobuf Detection Logic, Current Logic, Extensibility, Remain Bytes, Reference

</details>

### pyrootutils

Simple package for easy project root setup

`pip install pyrootutils` · installs (wheel) · licence: MIT · rank 11426 · last release 2022-06-09 · [PyPI](https://pypi.org/project/pyrootutils/)

<details><summary>README extract</summary>

A simple python package to solve all your problems with pythonpath, working directory, file paths, module imports and environment variables.

Features:
Problem: I would like to be able to:

- Run my python scripts from anywhere
- Always import python modules relatively to the project root directory ...

Example:
```python
import pyrootutils

# find absolute root path (searches for directory containing .project-root file)
# search starts from current file and recursively goes over parent directories
# returns pathlib object
path = pyrootutils.find_root(search_from=file, indicator=".project-root")

...
```

Sections: pyrootutils, Why pyrootutils?, Setup, Usage, Inspirations

</details>

### pydantic-zarr

Pydantic models for the Zarr file format

`pip install pydantic-zarr` · installs (wheel) · licence: MIT · rank 11468 · last release 2026-04-23 · [PyPI](https://pypi.org/project/pydantic-zarr/) · [docs](https://pydantic-zarr.readthedocs.io/) · [source](https://github.com/zarr-developers/pydantic-zarr)

<details><summary>README extract</summary>

Pydantic models for Zarr.

Example:
```python
import zarr
from pydantic_zarr import GroupSpec

group = zarr.group(path='foo')
array = zarr.create(store = group.store, path='foo/bar', shape=10, dtype='uint8')
array.attrs.put({'metadata': 'hello'})

# this is a pydantic model
spec = GroupSpec.from_zarr(group)
print(spec.model_dump())
"""
{
    'zarr_format': 2,
    'attributes': {},
...
```

Sections: pydantic-zarr, Getting help, Example

</details>

### python-odata

A simple library for read/write access to OData services.

`pip install python-odata` · installs (wheel) · licence: MIT · rank 11483 · last release 2026-08-04 · [PyPI](https://pypi.org/project/python-odata/)

<details><summary>README extract</summary>

A simple library for read/write access to OData services.

- Supports OData version 4.0
- Requires JSON format support from the service
- Should work on both Python 2.x and 3.x

Available on readthedocs.org

- requests >= 2.0
- python-dateutil
- rich >= 13.3.1

Example:
```python
import requests
from datetime import datetime

# you can only import this on the second run, the first run will create the package
# import generated
from odata import ODataService
session = requests.Session()

url = '
service = ODataService(
    url="
    session=session,
    base=generated.northwind.ReflectionBase,
    reflect_entities=True,
...
```

Sections: python-odata, Documentation, Dependencies, Demo, Northwind ODATA service, TripPin ODATA service (v4)

</details>

### pytorch-seed

RNG seeding and context management for pytorch

`pip install pytorch-seed` · installs (wheel) · licence: MIT License · rank 11491 · last release 2023-02-15 · [PyPI](https://pypi.org/project/pytorch-seed/) · [source](https://github.com/UM-ARM-Lab/pytorch_seed)

<details><summary>README extract</summary>

- PyTorch (1.0+)
- python 3

Example:
```python
import pytorch_seed
pytorch_seed.seed(123)
```

Sections: Requirements, Usage

</details>

### pinject

A pythonic dependency injection library

`pip install pinject` · installs (wheel) · licence: Apache License 2.0 · rank 11500 · last release 2019-05-25 · [PyPI](https://pypi.org/project/pinject/)

<details><summary>README extract</summary>

Pinject is a dependency injection library for python.

The primary goal of Pinject is to help you assemble objects into graphs in an
easy, maintainable way.

If you are already familiar with other dependency injection libraries, you may
want to read the condensed summary section at the end, so that you get an idea
of what Pinject is like and how ...

Features:
If you're wondering why to use a dependency injection library at all: if
you're writing a lot of object-oriented code in python, then it will make your
life easier. See, for instance: ...

Example:
```python
>>> class OuterClass(object):
...     def init(self, inner_class):
...         self.inner_class = inner_class
...
>>> class InnerClass(object):
...     def init(self):
...         self.forty_two = 42
...
...

</details>

### padelpy

A Python wrapper for PaDEL-Descriptor software

`pip install padelpy` · installs (wheel) · licence: MIT License · rank 11513 · last release 2026-07-22 · [PyPI](https://pypi.org/project/padelpy/)

<details><summary>README extract</summary>

PaDELPy provides a Python wrapper for the
PaDEL-Descriptor molecular
descriptor calculation software. It exposes the PaDEL-Descriptor command-line
interface to Python for computing descriptors and fingerprints from SMILES,
MDL MolFiles, and SDF files.

Example:
```python
from padelpy import from_smiles

# molecular descriptors for propane
descriptors = from_smiles("CCC")

# propane and butane
descriptors = from_smiles(["CCC", "CCCC"])

# descriptors plus PubChem fingerprints
desc_fp = from_smiles("CCC", fingerprints=True)

# fingerprints only
fingerprints = from_smiles("CCC", fingerprints=True, descriptors=False)

...
```

...

</details>

### picklescan

Security scanner detecting Python Pickle files performing suspicious actions

`pip install picklescan` · installs (wheel) · licence: MIT License · rank 11532 · last release 2026-07-01 · [PyPI](https://pypi.org/project/picklescan/)

<details><summary>README extract</summary>

Security scanner detecting Python Pickle files performing suspicious actions.

Sections: Getting started, Usage, Exit codes, Filtering files and directories, References

</details>

### pybammsolvers

Python interface for the IDAKLU solver

`pip install pybammsolvers` · installs (wheel) · licence: not stated · rank 11553 · last release 2026-10-14 · [PyPI](https://pypi.org/project/pybammsolvers/)

<details><summary>README extract</summary>

Standalone repository for the C/C++ solvers used in PyBaMM

Sections: IDAKLU solver, Solvers, Local builds, Nox (Recommended), MacOS, Linux, Custom SUNDIALS / SuiteSparse paths, Building a wheel or sdist, Unit Tests, Benchmarks

</details>

### psdtags

Read and write layered TIFF ImageSourceData and ImageResources tags

`pip install psdtags` · installs (wheel) · licence: BSD-3-Clause · rank 11561 · last release 2026-11-01 · [PyPI](https://pypi.org/project/psdtags/) · [docs](https://www.cgohlke.com/docs/psdtags/) · [source](https://github.com/cgohlke/psdtags)

<details><summary>README extract</summary>

Psdtags is a Python library to read and write the Adobe Photoshop(r) specific
ImageResources (#34377) and ImageSourceData (#37724) TIFF tags, which contain
image resource blocks, layer and mask information found in a typical layered
TIFF file created by Photoshop. ...

Sections: Quickstart, Requirements, Revisions, Notes, Examples

</details>

### pytorch-frame

Tabular Deep Learning Library for PyTorch

`pip install pytorch-frame` · installs (wheel) · licence: MIT · rank 11568 · last release 2025-11-02 · [PyPI](https://pypi.org/project/pytorch-frame/) · [docs](https://pytorch-frame.readthedocs.io) · [source](https://github.com/pyg-team/pytorch-frame.git)

<details><summary>README extract</summary>

A modular deep learning framework for building neural network models on heterogeneous tabular data.

______________

[][arxiv-url]

[][pypi-url]
[][testing-url]
[][docs-url]
[][contributing-url]
[][slack-url]

Documentation | Paper ...

Example:
```python
from torch import Tensor
from torch.nn import Linear, Module, ModuleList

from torch_frame import TensorFrame, stype
from torch_frame.nn.conv import TabTransformerConv
from torch_frame.nn.encoder import (
    EmbeddingEncoder,
    LinearEncoder,
    StypeWiseFeatureEncoder,
)

class ExampleTransformer(Module):
    def init(
        self,
...
```

Sections: Library Highlights, Architecture Overview, Quick Tour, Build and train your own deep tabular model, Implemented Deep Tabular Models, Benchmark

</details>

### pydantic-spark

Converting pydantic classes to spark schemas

`pip install pydantic-spark` · installs (wheel) · licence: MIT License · rank 11588 · last release 2023-11-24 · [PyPI](https://pypi.org/project/pydantic-spark/) · [source](https://github.com/godatadriven/pydantic-spark)

<details><summary>README extract</summary>

This library can convert a pydantic class to a spark schema or generate python code from a spark schema.

Example:
```python
import json
from typing import Optional

from pydantic_spark.base import SparkBase

class TestModel(SparkBase):
    key1: str
    key2: int
    key2: Optional[str]

schema_dict: dict = TestModel.spark_schema()
print(json.dumps(schema_dict))
```

Sections: pydantic-spark, Pydantic class to spark schema, Coerce type, Run unit tests, Run linting

</details>

### pyvi

Python Vietnamese Toolkit

`pip install pyvi` · installs (wheel) · licence: MIT License · rank 11596 · last release 2021-06-30 · [PyPI](https://pypi.org/project/pyvi/)

<details><summary>README extract</summary>

- Retrain a new tokenization model on a much bigger dataset. F1 score =0.985

- Add training data and training code

- Better integration to spacy.io (removing redundant spaces between tokens after tokenization. Eg. Việt Nam , 12 / 22 / 2020 => Việt Nam, 12/22/2020]

- Tokenization

- POS tagging

- Accents removal

- Accents adding ...

Example:
```python
from pyvi import ViTokenizer, ViPosTagger

ViTokenizer.tokenize(u"Trường đại học bách khoa hà nội")

ViPosTagger.postagging(ViTokenizer.tokenize(u"Trường đại học Bách Khoa Hà Nội")

from pyvi import ViUtils
ViUtils.remove_accents(u"Trường đại học bách khoa hà nội")

from pyvi import ViUtils
ViUtils.add_accents(u'truong dai hoc bach khoa ha noi')
```

Sections: Python Vietnamese Toolkit, What's New (0.1), Functionality, Usage

</details>

### pulumi-onepassword

Use the 1Password Pulumi provider to access and manage items in your 1Password vaults.

`pip install pulumi-onepassword` · installs from source (sdist only) · licence: Apache-2.0 · rank 11654 · last release 2026-10-22 · [PyPI](https://pypi.org/project/pulumi-onepassword/) · [source](https://github.com/1Password/pulumi-onepassword)

<details><summary>README extract</summary>

Use the 1Password Pulumi provider to access and manage items in your 1Password vaults.

*This project is licensed under Apache-2.0. Use of the 1Password APIs and services accessed through these tools is governed by the 1Password API Terms of Service.*

Sections: 1Password Pulumi provider, Node.js (JavaScript/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pyvim

Pure Python Vi Implementation

`pip install pyvim` · installs (wheel) · licence: BSD License · rank 11658 · last release 2022-05-16 · [PyPI](https://pypi.org/project/pyvim/)

<details><summary>README extract</summary>

*An implementation of Vim in Python*

Issues, questions, wishes, comments, feedback, remarks? Please create a GitHub
issue, I appreciate it.

Features:
There are several reasons.

The main reason is maybe because it was a small step after I created the Python
`prompt-toolkit` library. ...

Sections: pyvim, The good things, Some more screenshots, Configuring pyvim, Limitations, Roadmap, Why did I create Pyvim?, Alternatives, Q & A, Thanks

</details>

### pytest-suite-timeout

A pytest plugin for ensuring max suite time

`pip install pytest-suite-timeout` · installs (wheel) · licence: MIT License · rank 11667 · last release 2024-01-26 · [PyPI](https://pypi.org/project/pytest-suite-timeout/)

<details><summary>README extract</summary>

A pytest plugin for ensuring max suite time.

Really though, it's: if the timeout expires, no new tests are started.

Works great in conjunction with pytest-repeat.

Say your debugging a flaky test and just want to run it a bunch of times, but not longer than say 10 minutes (600 seconds). ...

Sections: pytest-suite-timeout, A use case, Usage, Defaults to no timeout, Timeout behavior, Issues

</details>

### promptlayer

PromptLayer is a platform for prompt engineering and tracks your LLM requests.

`pip install promptlayer` · installs (wheel) · licence: Apache Software License · rank 11674 · last release 2026-10-29 · [PyPI](https://pypi.org/project/promptlayer/) · [docs](https://docs.promptlayer.com/sdks/python) · [source](https://github.com/MagnivOrg/prompt-layer-library)

<details><summary>README extract</summary>

Version, test, and monitor every prompt and agent with robust evals, tracing, and regression sets.

This library provides convenient access to the PromptLayer API from applications written in python.

Install PromptLayer skill files and the Docs MCP server into your coding agents: ...

Example:
```python
from promptlayer import PromptLayer

pl = PromptLayer(api_key="pl_xxxxx")

prompt = pl.templates.get(
    "support-reply",
    {
        "input_variables": {
            "customer_name": "Ada",
            "question": "How do I reset my password?",
        }
    },
)

print(prompt["prompt_template"])
```

...

</details>

### paramtools

Library for parameter processing and validation with a focus on computational modeling projects

`pip install paramtools` · installs (wheel) · licence: MIT License · rank 11699 · last release 2025-05-15 · [PyPI](https://pypi.org/project/paramtools/)

<details><summary>README extract</summary>

Define, update, and validate your model's parameters.

Install using pip:

Install using conda:

Example:
```python
import paramtools

class Params(paramtools.Parameters):
    defaults = {
        "schema": {
            "labels": {
                "date": {
                    "type": "date",
                    "validators": {
                        "range": {
                            "min": "2020-01-01",
                            "max": "2021-01-01",
...
```

Sections: ParamTools, Usage, Access parameter values, Adjust and validate parameter values, Extend parameter values using label definitions, NumPy integration, Documentation

</details>

### pylibfdt

Python binding for libfdt

`pip install pylibfdt` · installs from source (sdist only) · licence: not stated · rank 11705 · last release 2026-09-01 · [PyPI](https://pypi.org/project/pylibfdt/)

<details><summary>README extract</summary>

This tree contains a copy of libfdt from the upstream dtc project for the
purposes of pypi.org packaging. Other than changes to the packaging files,
changes should be made upstream. The upstream sources are here:

git://git.kernel.org/pub/scm/utils/dtc/dtc.git

To install this you will need to install swig and Python development files. ...

</details>

### pure-pcapy3

Pure Python reimplementation of pcapy. This package is API compatible and a drop-in replacement.

`pip install pure-pcapy3` · installs from source (sdist only) · licence: Simplified BSD · rank 11709 · last release 2017-02-27 · [PyPI](https://pypi.org/project/pure-pcapy3/)

<details><summary>README extract</summary>

This package provides an API-compatible replacement for the popular pcapy package. Since it is a pure-Python package, it cannot access some elements like live traffic capture directly. Only file operations are allowed right now. Any operation which is available in pcapy and could not be implemented here will throw NotImplementedError. ...

</details>

### projen

CDK for software projects

`pip install projen` · installs (wheel) · licence: OSI Approved · rank 11717 · last release 2026-11-06 · [PyPI](https://pypi.org/project/projen/) · [source](https://github.com/projen/projen.git)

<details><summary>README extract</summary>

Define and maintain complex project configuration through code.

 Documentation ·
 Changelog ·
 Project types ·
 Join the community

*projen* synthesizes project configuration files such as `package.json`,
`tsconfig.json`, `.gitignore`, GitHub Workflows, eslint, jest, etc. from a
well-typed definition written in JavaScript. ...

Features:
Some examples of features built-in to project types:

* Fully synthesize `package.json`
* Standard npm scripts like `compile`, `build`, `test`, `package`
* eslint
* Jest
* jsii: compile, package, api compatibility checks, API.md
* Bump & release ...

...

</details>

### py-tlsh

TLSH (C++ Python extension)

`pip install py-tlsh` · installs from source (sdist only) · licence: Apache or BSD · rank 11726 · last release 2026-05-08 · [PyPI](https://pypi.org/project/py-tlsh/)

<details><summary>README extract</summary>

TLSH (Trend Micro Locality Sensitive Hash) is a fuzzy matching library.
Given a byte stream with a minimum length of 50 bytes
TLSH generates a hash value which can be used for similarity comparisons.
Similar objects will have similar hash values which allows for
the detection of similar objects by comparing their hash values. ...

Example:
```python
import tlsh

tlsh.hash(data)
```

Sections: TLSH - C++ extension for Python, What's new in py-tlsh 5.0.0, Usage, Example, Extra Options, Backwards Compatibility Options

</details>

### py-lets-be-rational

Pure python implementation of Peter Jaeckel's LetsBeRational.

`pip install py-lets-be-rational` · installs (wheel) · licence: MIT License · rank 11750 · last release 2026-05-30 · [PyPI](https://pypi.org/project/py-lets-be-rational/) · [source](https://github.com/vollib/py_lets_be_rational)

<details><summary>README extract</summary>

Features:
`lets_be_rational` is the canonical package for Peter Jaeckel's LetsBeRational algorithm.
It provides a pure Python implementation and keeps the historical `py_lets_be_rational`
import path available for compatibility.

Sections: Overview, Execution Speed, Numba Dependency, About "Let's be Rational"

</details>

### pylcs

super fast cpp implementation of longest common subsequence

`pip install pylcs` · installs from source (sdist only) · licence: Apache 2.0 · rank 11752 · last release 2023-10-25 · [PyPI](https://pypi.org/project/pylcs/)

<details><summary>README extract</summary>

The original repository stop maintenance. This is a transfer version

pylcs is a super fast c++ library which adopts dynamic programming(DP) algorithm to solve two classic LCS problems as below . ...

Example:
```python
import pylcs

# finding the longest common subsequence length of string A and string B
A = 'We are shannonai'
B = 'We like shannonai'
pylcs.lcs_sequence_length(A, B)
"""
>>> pylcs.lcs_sequence_length(A, B)
14
"""

# finding alignment from string A to B
A = 'We are shannonai'
B = 'We like shannonai'
res = pylcs.lcs_sequence_idx(A, B)
...
```

</details>

### pytest-xfiles

Pytest fixtures providing data read from function, module or package related (x)files.

`pip install pytest-xfiles` · installs (wheel) · licence: not stated · rank 11858 · last release 2018-02-27 · [PyPI](https://pypi.org/project/pytest-xfiles/)

<details><summary>README extract</summary>

Each test function deserves a companion - a small or large (YAML, JSON or other) file sitting beside.

Providing such data can be as simple as:

Run the test:

Where are the files?

and one more (for the whole package `tests.shakespeare`):

Example:
```python
"""Test Romeo y Julieta by Shakespeare.
"""

def test_romeo(function_yaml):
    print(function_yaml)

def test_julieta(function_yaml):
    print(function_yaml)

def test_play(module_yaml):
    print(module_yaml)

def test_author(package_yaml):
    print(package_yaml)
```

...

</details>

### pulumi-coreweave

A Pulumi package for creating and managing CoreWeave cloud resources.

`pip install pulumi-coreweave` · installs (wheel) · licence: Apache-2.0 · rank 11863 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pulumi-coreweave/) · [source](https://github.com/pulumi/pulumi-coreweave)

<details><summary>README extract</summary>

Pulumi provider that lets you manage CoreWeave resources. Based on the terraform-provider-coreweave Terraform provider under the hood.

Example:
```python
import pulumi_coreweave as coreweave

provider = coreweave.Provider("coreweave",
    token="CW-SECRET-XXXXXXXXXXXXX",
)
```

Sections: Pulumi provider for CoreWeave, Node.js (JavaScript/TypeScript), Python, Go, .NET, Configuration, Setting configuration values, Example usage

</details>

### pipcl

Python packaging operations, including PEP-517 support, for use by a setup.py script.

`pip install pipcl` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 11866 · last release 2026-09-01 · [PyPI](https://pypi.org/project/pipcl/)

_README extract left out: share-alike licence._

### pytorch-kinematics

Robot kinematics implemented in pytorch

`pip install pytorch-kinematics` · installs (wheel) · licence: MIT License · rank 11867 · last release 2026-04-15 · [PyPI](https://pypi.org/project/pytorch-kinematics/) · [source](https://github.com/UM-ARM-Lab/pytorch_kinematics)

<details><summary>README extract</summary>

- Parallel and differentiable forward kinematics (FK), Jacobian calculation, and damped least squares inverse kinematics (IK)
- Load robot description from URDF, SDF, and MJCF formats
- SDF queries batched across configurations and points via pytorch-volumetric

Example:
```python
import pytorch_kinematics as pk

urdf = "widowx/wx250s.urdf"
# there are multiple natural end effector links so it's not a serial chain
chain = pk.build_chain_from_urdf(open(urdf, mode="rb").read())
# visualize the frames (the string is also returned)
chain.print_tree()
"""
base_link
└── shoulder_link
    └── upper_arm_link
...
```

Sections: PyTorch Robot Kinematics, Reference, Usage, Loading Robots, Forward Kinematics (FK), Jacobian calculation, Inverse Kinematics (IK), Compiled IK, SDF Queries

</details>

### pysigma-pipeline-windows

pySigma Windows processing pipelines

`pip install pysigma-pipeline-windows` · installs (wheel) · licence: OSI Approved · rank 11910 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pysigma-pipeline-windows/) · [source](https://github.com/SigmaHQ/pySigma-pipeline-windows)

<details><summary>README extract</summary>

This is the windows service processing pipeline for pySigma. It provides the package `sigma.pipeline.windows` with the `windows_pipeline` function that returns a ProcessingPipeline object.

Currently the pipeline adds support for the following event types (Sigma logsource service and category to Channel mapping): ...

</details>

### py-multihash

Multihash implementation in Python

`pip install py-multihash` · installs (wheel) · licence: MIT · rank 11928 · last release 2025-12-17 · [PyPI](https://pypi.org/project/py-multihash/)

<details><summary>README extract</summary>

Multihash implementation in Python

* Free software: MIT license

* Python versions: Python 3.10, 3.11, 3.12, 3.13, 3.14

Features:
* Cryptographic hashes: SHA-1, SHA-2 (224/256/384/512), SHA-3, BLAKE2b, BLAKE2s, BLAKE3
 * Variable-length hashes: SHAKE-128, SHAKE-256
 * Non-cryptographic hashes: MurmurHash3 (32-bit and 128-bit)
 * Specialized hashes: Double-SHA-256 (Bitcoin), ...

Example:
```python
from multihash import digest, sum, Func

# Using modern hash functions
mh = digest(b"hello world", "blake3")

# Using MurmurHash3 for fast, non-cryptographic hashing
mh = digest(b"data", "murmur3-128")

# Using BLAKE2b with custom digest size
mh = digest(b"data", "blake2b-256")

# Go-compatible API
mh = sum(b"hello world", Func.sha2_256)
...
```

Sections: py-multihash, Features, Quick Start

</details>

### py-trello

Python wrapper around the Trello API

`pip install py-trello` · installs (wheel) · licence: BSD License · rank 11951 · last release 2024-06-11 · [PyPI](https://pypi.org/project/py-trello/)

<details><summary>README extract</summary>

A wrapper around the Trello API written in Python. Each Trello object is
represented by a corresponding Python object. The attributes of these objects
are cached, but the child objects are not. ...

Example:
```python
from trello import TrelloClient

client = TrelloClient(
    api_key='your-key',
    api_secret='your-secret',
    token='your-oauth-token-key',
    token_secret='your-oauth-token-secret'
)
```

Sections: Usage, Working with boards, working with board lists and cards, Getting your Trello OAuth Token, Required Python modules, Tests

</details>

### pysigma-pipeline-sysmon

pySigma Sysmon processing pipelines

`pip install pysigma-pipeline-sysmon` · installs (wheel) · licence: OSI Approved · rank 11952 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pysigma-pipeline-sysmon/) · [source](https://github.com/SigmaHQ/pySigma-pipeline-sysmon/)

<details><summary>README extract</summary>

This is the Sysmon processing pipeline for pySigma. It provides the package `sigma.pipeline.sysmon` with the `sysmon_pipeline` function that returns a ProcessingPipeline object.

Currently the pipeline adds support for the following event types (Sigma logsource category to EventID mapping): ...

</details>

### polars-ds

(no summary)

`pip install polars-ds` · installs (wheel) · licence: MIT License · rank 11961 · last release 2026-10-30 · [PyPI](https://pypi.org/project/polars-ds/)

<details><summary>README extract</summary>

Discord
 Documentation
 User Guide
 Want to Contribute?

 pip install polars-ds

PDS is a modern data science package that

1. is fast and furious
2. is small and lean, with minimal dependencies
3. has an intuitive and concise API (if you know Polars already)
4. has dataframe friendly design
5. ...

Example:
```python
import polars_ds as pds
```

Sections: Polars for Data Science, PDS (polars_ds), Parallel ML Metrics Calculation, Quick and simple modeling on the fly (non-persistent), Distances, In-dataframe statistical tests, Making Polars More Convenient, Nearest Neighbors Related Queries, Compatibility, Other, Getting Started, How Fast is it?, Road Map, Build From Source

</details>

### pytorch-ranger

Ranger - a synergistic optimizer using RAdam (Rectified Adam) and LookAhead in one codebase

`pip install pytorch-ranger` · installs (wheel) · licence: MIT License · rank 11965 · last release 2020-03-30 · [PyPI](https://pypi.org/project/pytorch-ranger/)

### powerbot-client

PowerBot Asyncio Client

`pip install powerbot-client` · installs (wheel) · licence: not stated · rank 11984 · last release 2026-10-21 · [PyPI](https://pypi.org/project/powerbot-client/)

### pkscreener

A Python-based stock screener for NSE, India with alerts to Telegram Channel (pkscreener)

`pip install pkscreener` · installs from source (sdist only) · licence: MIT License · rank 12026 · last release 2026-06-15 · [PyPI](https://pypi.org/project/pkscreener/)

<details><summary>README extract</summary>

Example:
```python
 0 > Full Screening (Shows Technical Parameters without any criterion)
 1 > Probable Breakouts/Breakdowns       2 > Today's Breakouts/Breakdowns
 3 > Consolidating stocks                4 > Lowest Volume in last N-days (Early Breakout Detection)
 5 > RSI screening                       6 > Reversal Signals
...
```

Sections: 🚀 What is PKScreener?, ✨ Key Features at a Glance, 💹 Trading Signals & Analysis, 📈 Comprehensive Market Coverage, 🏆 Why Choose PKScreener?, Receiving Scheduled Scan results, Receiving On-Demand Scan results, Scanners, Running Piped Scanners, Running Intraday analysis of Piped Scanners, How to use on your own local Windows/Linux/Macbook laptop?, Using docker, running within docker container, Building from source repo, Running the executables

</details>

### petastorm

Petastorm is a library enabling the use of Parquet storage from Tensorflow, Pytorch, and other Python-based ML training frameworks.

`pip install petastorm` · installs (wheel) · licence: Apache Software License · rank 12035 · last release 2026-01-02 · [PyPI](https://pypi.org/project/petastorm/)

<details><summary>README extract</summary>

Petastorm is an open source data access library developed at Uber ATG. This library enables single machine or
distributed training and evaluation of deep learning models directly from datasets in Apache Parquet
format. Petastorm supports popular Python-based machine learning (ML) frameworks such as
Tensorflow, PyTorch, and
PySpark. ...

Example:
```python
import numpy as np
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType

from petastorm.codecs import ScalarCodec, CompressedImageCodec, NdarrayCodec
from petastorm.etl.dataset_metadata import materialize_dataset
from petastorm.unischema import dict_to_spark_row, Unischema, UnischemaField

...
```

...

</details>

### pypcode

Machine code disassembly and IR translation library

`pip install pypcode` · installs (wheel) · licence: BSD-2-Clause AND Apache-2.0 AND Zlib · rank 12039 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pypcode/) · [source](https://github.com/angr/pypcode)

<details><summary>README extract</summary>

Machine code disassembly and IR translation library for Python using the
excellent SLEIGH library from the Ghidra framework.

This library was created primarily for use with angr, which
provides analyses and symbolic execution of p-code.

Documentation covering how to install and use pypcode is
available here.

</details>

### pyzk

an unofficial library of zksoftware fingerprint device

`pip install pyzk` · installs from source (sdist only) · licence: LICENSE.txt · rank 12086 · last release 2019-08-13 · [PyPI](https://pypi.org/project/pyzk/)

### pydemumble

A Python wrapper library for demumble; demumble is a tool to demangle C++, Rust, and Swift symbol names.

`pip install pydemumble` · installs (wheel) · licence: BSD License · rank 12139 · last release 2026-07-21 · [PyPI](https://pypi.org/project/pydemumble/)

### pypinyin-dict

使用 pinyin-data 和 phrase-pinyin-data 中的拼音数据文件覆盖 pypinyin 中的自带拼音数据，实现只使用某个或某些拼音数据文件中的拼音数据的需求

`pip install pypinyin-dict` · installs (wheel) · licence: MIT License · rank 12155 · last release 2025-01-12 · [PyPI](https://pypi.org/project/pypinyin-dict/)

<details><summary>README extract</summary>

使用 pinyin-data 和 phrase-pinyin-data 中的拼音数据文件覆盖 pypinyin 中的内置拼音数据，
实现只使用某个或某些拼音数据文件中的拼音数据的需求。

Example:
```python
>>> from pypinyin import pinyin
>>> pinyin('枯萎')
[['kū'], ['wēi']]

# 使用 phrase-pinyin-data 项目中 cc_cedict.txt 文件中的拼音数据优化结果
>>> from pypinyin_dict.phrase_pinyin_data import cc_cedict
>>> cc_cedict.load()

>>> pinyin('枯萎')
[['kū'], ['wěi']]

>>> pinyin('扔', heteronym=True)
[['rēng', 'rèng']]

# 使用 pinyin-data 项目中 kXHC1983.txt 文件中的拼音数据优化结果
...
```

Sections: pypinyin-dict, 安装, 使用示例, 模块介绍, 生成文件

</details>

### pulumi-xyz

A test provider used by Pulumi CI to exercise provider tooling. It manages no real cloud resources and is not intended for use in Pulumi programs.

`pip install pulumi-xyz` · installs (wheel) · licence: Apache-2.0 · rank 12174 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pulumi-xyz/) · [source](https://github.com/pulumi/pulumi-xyz)

<details><summary>README extract</summary>

The xyz Resource Provider is a test provider used by Pulumi CI to exercise
provider tooling. It manages no real cloud resources and is not intended for
use in Pulumi programs.

The install instructions below exist so that CI can exercise the published
SDKs. They are not a recommendation to depend on this package.

Sections: XYZ Resource Provider, Node.js (JavaScript/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pytest-pyodide

Pytest plugin for testing applications that use Pyodide

`pip install pytest-pyodide` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 12179 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pytest-pyodide/) · [source](https://github.com/pyodide/pytest-pyodide)

<details><summary>README extract</summary>

Pytest plugin for testing applications that use Pyodide

Example:
```python
def test_a(selenium):
    selenium.run("assert 1+1 == 2")   # run Python with Pyodide
```

Sections: pytest-pyodide, Github Reusable workflow, Usage, `run_in_pyodide`, Copying files to Pyodide, Running non-pyodide tests in Pyodide, Specifying a browser, Running tests with Playwright (optional), Custom test marks, Examples, Compatible Pyodide versions

</details>

### pyGeoTile

Python package to handle tiles and points of different projections, in particular WGS 84 (Latitude, Longitude), Spherical Mercator (Meters), Pixel Pyramid and Tiles (TMS, Google, QuadTree)

`pip install pyGeoTile` · installs from source (sdist only) · licence: MIT · rank 12193 · last release 2018-03-08 · [PyPI](https://pypi.org/project/pyGeoTile/)

<details><summary>README extract</summary>

Example:
```python
from pygeotile.point import Point

meter_x, meter_y, zoom = -9757148.442088600, 5138517.444985110, 19  # meters in Spherical Mercator EPSG:900913

point = Point.from_meters(meter_x=meter_x, meter_y=meter_y)

print('Pixels: ', point.pixels(zoom=zoom))  # Pixels:  (34430592, 49899136)
...
```

Sections: Usage, Point, Tile, Notes

</details>

### pyinvoke

(no summary)

`pip install pyinvoke` · installs from source (sdist only) · licence: MIT · rank 12195 · last release 2018-09-20 · [PyPI](https://pypi.org/project/pyinvoke/)

<details><summary>README extract</summary>

`pyinvoke` is a simple module that is used to invoked Python applications
using a full function specifier, similar to distlib entrypoints.

The key advantage is that the Python application you want to run will be
loaded as its proper module instead of as the `main` module. `pyinvoke`
will be the `main` module for this operation. ...

Example:
```python
argv = getattr(sys, 'argv', sys.argv)
```

</details>

### pulumi-keycloak

A Pulumi package for creating and managing keycloak cloud resources.

`pip install pulumi-keycloak` · installs (wheel) · licence: Apache-2.0 · rank 12198 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pulumi-keycloak/) · [source](https://github.com/pulumi/pulumi-keycloak)

<details><summary>README extract</summary>

The Keycloak resource provider for Pulumi lets you manage Keycloak resources in your cloud programs. To use
this package, please install the Pulumi CLI first.

Sections: Keycloak Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pyriemann

Machine learning for multivariate data with Riemannian geometry

`pip install pyriemann` · installs (wheel) · licence: BSD (3-clause) · rank 12212 · last release 2026-07-01 · [PyPI](https://pypi.org/project/pyriemann/) · [docs](https://pyriemann.readthedocs.io) · [source](https://github.com/pyRiemann/pyRiemann)

<details><summary>README extract</summary>

pyRiemann is a Python machine learning package based on scikit-learn API.
It provides a high-level interface for processing and classification of real (*resp*. complex)-valued multivariate data
through the Riemannian geometry of symmetric (*resp*. Hermitian)
positive definite (SPD) (*resp*. HPD) matrices.

The documentation is available on ...

Example:
```python
import pyriemann
from sklearn.model_selection import cross_val_score

# load your data
X = ... # EEG data, in format n_epochs x n_channels x n_times
y = ... # labels

# estimate covariance matrices
cov = pyriemann.estimation.Covariances().fit_transform(X)

# build your classifier
mdm = pyriemann.classification.MDM()

# cross validation
...
```

...

</details>

### pygments-ansi-color

(no summary)

`pip install pygments-ansi-color` · installs (wheel) · licence: Apache Software License · rank 12222 · last release 2023-05-18 · [PyPI](https://pypi.org/project/pygments-ansi-color/)

### Persistence

Persistent ExtensionClass

`pip install Persistence` · installs (wheel) · licence: ZPL-2.1 · rank 12236 · last release 2026-08-20 · [PyPI](https://pypi.org/project/Persistence/) · [source](https://github.com/zopefoundation/Persistence)

<details><summary>README extract</summary>

Features:
This package provides a variant of the persistent base class that's an
ExtensionClass. Unless you need ExtensionClass semantics, you probably want to
use `persistent.Persistent` from the persistent distribution (formerly in ZODB3).

Sections: Overview, 5.5 (2026-08-20), 5.4 (2025-11-16), 5.3 (2025-11-15), 5.2 (2025-11-06), 5.1 (2024-09-17), 5.0 (2024-05-30), 4.1 (2023-10-05), 4.0.post1 (2023-03-24), 4.0 (2023-03-24), 3.6 (2022-11-17), 3.5 (2022-11-03), 3.4 (2022-10-11), 3.3 (2022-03-10)

</details>

### pytabkit

ML models + benchmark for tabular data classification and regression

`pip install pytabkit` · installs (wheel) · licence: Apache-2.0 · rank 12240 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pytabkit/) · [docs](https://github.com/dholzmueller/pytabkit#readme) · [source](https://github.com/dholzmueller/pytabkit)

<details><summary>README extract</summary>

Paper | Documentation | RealMLP-TD-S standalone implementation | Grinsztajn et al. benchmark code | Data archive |

PyTabKit provides scikit-learn interfaces for modern tabular classification and regression methods
benchmarked in our paper, see below.
It also contains the code we used for benchmarking these methods
on our benchmarks. ...

Example:
```python
from pytabkit import RealMLP_TD_Classifier

model = RealMLP_TD_Classifier()  # or TabR_S_D_Classifier, CatBoost_TD_Classifier, etc.
model.fit(X_train, y_train)
model.predict(X_test)
```

Sections: PyTabKit: Tabular ML models and benchmarking (NeurIPS 2024), When (not) to use pytabkit, Using the ML models, Available ML models, Post-hoc calibration and refinement stopping, Benchmarking code, Preprocessing code

</details>

### pymetastore

A Python client for the Thrift interface to Hive Metastore

`pip install pymetastore` · installs (wheel) · licence: MIT · rank 12241 · last release 2025-11-04 · [PyPI](https://pypi.org/project/pymetastore/) · [source](https://github.com/recap-build/pymetastore)

<details><summary>README extract</summary>

`pymetastore` is a Python client for Hive Metastore.

Features:
* Python-friendly interface for Hive Metastore
* Comprehensive support for metadata operations
* Fully compatible with the Hive metastore service over Thrift protocol

Example:
```python
from pymetastore.metastore import HMS

with HMS.create(host="localhost", port=9083) as hms:
    databases = hms.list_databases()
    database = hms.get_database(name="test_db")
    tables = hms.list_tables(database_name=database.name)
    table = hms.get_table(
        database_name=database.name,
        table_name=tables[0],
    )
...
```

Sections: pymetastore 🐝 🐍, Features, Quick Start

</details>

### pySigma-backend-kusto

pySigma Kusto backend

`pip install pySigma-backend-kusto` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 12243 · last release 2025-11-28 · [PyPI](https://pypi.org/project/pySigma-backend-kusto/) · [source](https://github.com/AttackIQ/pySigma-backend-kusto)

_README extract left out: share-alike licence._

### python-bitcoinrpc

Enhanced version of python-jsonrpc for use with Bitcoin

`pip install python-bitcoinrpc` · installs from source (sdist only) · licence: GNU Library or Lesser General Public License (LGPL) · rank 12246 · last release 2016-08-24 · [PyPI](https://pypi.org/project/python-bitcoinrpc/)

_README extract left out: share-alike licence._

### pyserial-labgrid

Python Serial Port Extension (with labgrid RFC2217 fixes)

`pip install pyserial-labgrid` · installs (wheel) · licence: BSD · rank 12253 · last release 2023-04-26 · [PyPI](https://pypi.org/project/pyserial-labgrid/)

<details><summary>README extract</summary>

Features:
This module encapsulates the access for the serial port. It provides backends
for Python running on Windows, OSX, Linux, BSD (possibly any POSIX compliant
system) and IronPython. ...

Sections: pySerial (labgrid fork), Overview, Documentation, Examples

</details>

### pytest-reverse

Pytest plugin to reverse test order.

`pip install pytest-reverse` · installs (wheel) · licence: MIT · rank 12254 · last release 2025-09-09 · [PyPI](https://pypi.org/project/pytest-reverse/) · [source](https://github.com/adamchainz/pytest-reverse)

<details><summary>README extract</summary>

Pytest plugin to reverse test order.

Testing a Django project?
Check out my book Speed Up Your Django Tests which covers loads of recommendations to write faster, more accurate tests.
I created pytest-reverse whilst working on the book!

Sections: pytest-reverse, Usage

</details>

### py-solc-x

Python wrapper and version management tool for the solc Solidity compiler.

`pip install py-solc-x` · installs (wheel) · licence: MIT · rank 12281 · last release 2026-10-30 · [PyPI](https://pypi.org/project/py-solc-x/) · [docs](https://solcx.readthedocs.io/en/latest/) · [source](https://github.com/ApeWorX/py-solc-x)

<details><summary>README extract</summary>

Python wrapper and version management tool for the `solc` Solidity compiler.

Forked from `py-solc`.

Features:
- Full support for Solidity `>=0.4.11`
- Install Solidity on Linux, OSX and Windows
- Compile Solidity from source on Linux and OSX

Sections: py-solc-x, Features, Dependencies, via `pip`, from source, Documentation

</details>

### python3-nmap

Python3-nmap converts Nmap commands into python3 methods making it very easy to use nmap in any of your python pentesting projects

`pip install python3-nmap` · installs (wheel) · licence: not stated · rank 12293 · last release 2024-09-15 · [PyPI](https://pypi.org/project/python3-nmap/) · [docs](https://nmap.readthedocs.io/en/latest/) · [source](https://github.com/nmmapper/python3-nmap)

<details><summary>README extract</summary>

A python 3 library which helps in using nmap port scanner. The way this tools works is by defining each nmap command into a python function making it very easy to use sophisticated nmap commands in other python scripts. ...

Example:
```python
import nmap3
nmap = nmap3.Nmap()
os_results = nmap.nmap_os_detection("192.168.178.2") # MOST BE ROOT
```

Sections: python3-nmap, How to use python3-nmap, How to use the script to identify OS, Class components of python3-nmap, Identifying service version, Nmap commands available, Nmap Scanning Techniques, Using custom nmap command line arguments., Cross-Selling, Stargazers over time

</details>

### pyffx

pure Python format preserving encryption

`pip install pyffx` · installs from source (sdist only) · licence: MIT License · rank 12311 · last release 2019-05-12 · [PyPI](https://pypi.org/project/pyffx/)

<details><summary>README extract</summary>

pyffx is a pure Python implementation of *Format-preserving, Feistel-based encryption* (FFX).

* The FFX Mode of Operation for Format-Preserving Encryption
* Addendum to “The FFX Mode of Operation for Format-Preserving Encryption”

Only method 2 is implemented.

See also libffx

Example:
```python
>>> import pyffx
>>> e = pyffx.Integer(b'secret-key', length=4)
>>> e.encrypt(1234)
6103
>>> e.decrypt(6103)
1234
>>> e = pyffx.String(b'secret-key', alphabet='abc', length=6)
>>> e.encrypt('aaabbb')
'acbacc'
>>> e.decrypt('acbacc')
'aaabbb'
```

Sections: pyffx, Usage

</details>

### pypyodbc

A Pure Python ctypes ODBC module

`pip install pypyodbc` · installs from source (sdist only) · licence: MIT License · rank 12312 · last release 2021-12-23 · [PyPI](https://pypi.org/project/pypyodbc/)

<details><summary>README extract</summary>

A Pure Python ctypes ODBC module compatible with PyPy and almost totally same usage as pyodbc

</details>

### pygrok

A Python library to parse strings and extract information from structured/unstructured data

`pip install pygrok` · installs from source (sdist only) · licence: MIT · rank 12327 · last release 2016-09-24 · [PyPI](https://pypi.org/project/pygrok/)

<details><summary>README extract</summary>

|Join the chat at

A Python library to parse strings and extract information from
structured/unstructured data

- parsing and matching patterns in a string(log, message etc.)
- relieving from complex regular expressions.
- extracting information from structured/unstructured data

Example:
```python
from pygrok import Grok
text = 'gary is male, 25 years old and weighs 68.5 kilograms'
pattern = '%{WORD:name} is %{WORD:gender}, %{NUMBER:age} years old and weighs %{NUMBER:weight} kilograms'
grok = Grok(pattern)
print grok.match(text)

# {'gender': 'male', 'age': '25', 'name': 'gary', 'weight': '68.5'}
```

Sections: pygrok, What can I use Grok for?, Getting Started, More details, Get Help

</details>

### pypura

Python package for interacting with Pura smart fragrance diffusers over the cloud

`pip install pypura` · installs (wheel) · licence: MIT · rank 12361 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pypura/)

<details><summary>README extract</summary>

A Python package for interacting with Pura smart fragrance diffusers over the cloud. Used in the Pura for Home Assistant integration.

</details>

### pydub-stubs

Stub-only package containing type information for pydub

`pip install pydub-stubs` · installs (wheel) · licence: OSI Approved; ISC License (ISCL) · rank 12362 · last release 2025-04-11 · [PyPI](https://pypi.org/project/pydub-stubs/) · [source](https://github.com/clo4/pydub-stubs)

<details><summary>README extract</summary>

Pydub version: 0.25.1

`pydub-stubs` provides type information for [Pydub].
 Only the public
interface is guaranteed to be typed, however there are type definitions for some
private and undocumented functions.

These are legacy types that have been replaced by the `channels`, `frame_rate`,
and `sample_rate` keyword arguments.

Sections: pydub-stubs, Anticipated Questions, Q: What is `_Metadata` and `_PartialMetadata`?, Version 0.25.1.6, Version 0.25.1.5, Version 0.25.1.4, Version 0.25.1.3, Version 0.25.1.2, Version 0.25.1.1, Version 0.25.1.0, Version 0.24.1.9, Version 0.24.1.8, Version 0.24.1.7, Version 0.24.1.6

</details>

### python-jsonrpc-server

JSON RPC 2.0 server library

`pip install python-jsonrpc-server` · installs (wheel) · licence: not stated · rank 12364 · last release 2020-09-08 · [PyPI](https://pypi.org/project/python-jsonrpc-server/)

<details><summary>README extract</summary>

A Python 2.7 and 3.4+ server implementation of the JSON RPC 2.0 protocol. This library has been pulled
out of the Python Language Server project.

Asynchronous request handling is supported using Python 3's `concurrent.futures` module and the Python 2 concurrent.futures backport.

Sections: Python JSON RPC Server, Examples

</details>

### pdf2zh-next

PDF Translator based on BabelDOC

`pip install pdf2zh-next` · does not install on CPython 3.14 · licence: AGPL-3.0 · rank 12365 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pdf2zh-next/)

_README extract left out: share-alike licence._

### ppdeep

Pure-Python library for computing fuzzy hashes (ssdeep)

`pip install ppdeep` · installs (wheel) · licence: Apache Software License · rank 12373 · last release 2026-02-21 · [PyPI](https://pypi.org/project/ppdeep/)

<details><summary>README extract</summary>

This is a pure-Python library for computing context triggered piecewise hashes
(CTPH), also called fuzzy hashes, or often ssdeep after the name of a popular
tool. At a very high level, fuzzy hashing is a way to determine whether two
inputs are similar, rather than identical. ...

Example:
```python
>>> import ppdeep
>>> h1 = ppdeep.hash('The equivalence of mass and energy translates into the well-known E = mc²')
>>> h1
'3:RC0qYX4LBFA0dxEq4z2LRK+oCKI9VnXn:RvqpLB60dx8ilK+owX'
>>> h2 = ppdeep.hash('The equivalence of mass and energy translates into the well-known E = MC2')
>>> h2
'3:RC0qYX4LBFA0dxEq4z2LRK+oCKI99:RvqpLB60dx8ilK+oA'
```

</details>

### prometheus-mcp-server

MCP server for Prometheus integration

`pip install prometheus-mcp-server` · installs (wheel) · licence: not stated · rank 12378 · last release 2026-08-03 · [PyPI](https://pypi.org/project/prometheus-mcp-server/)

<details><summary>README extract</summary>

Give AI assistants the power to query your Prometheus metrics.

A Model Context Protocol (MCP) server that provides access to your Prometheus metrics and queries through standardized MCP interfaces, allowing AI assistants to execute PromQL queries and analyze your metrics data.

Features:
- Execute PromQL queries against Prometheus
- Discover and explore metrics
 - List available metrics
 - Get metadata for specific metrics
 - Search metric metadata by name or description in a single call
 - View instant query results
 - View range ...

Sections: Prometheus MCP Server, Getting Started, Prerequisites, Configuration Options, Available Tools, Features

</details>

### patroni

PostgreSQL High-Available orchestrator and CLI

`pip install patroni` · installs (wheel) · licence: The MIT License · rank 12379 · last release 2026-08-12 · [PyPI](https://pypi.org/project/patroni/)

<details><summary>README extract</summary>

You can find a searchable version of this documentation at
patroni.readthedocs.io.

Patroni is a Python template for building PostgreSQL high availability (HA) clusters.
It supports several distributed configuration stores, including ZooKeeper,
etcd, Consul, and Kubernetes.

Supported PostgreSQL versions: 9.3 to 18. ...

Sections: How Patroni Works, Pre-requirements for macOS, Psycopg choices, Running and Configuring, Memory issue on Python 3.11+, Recommended solution, Additional recommendations (Linux, glibc), Configuration References, YAML configuration, Environment configuration, Replication choices, Application connections

</details>

### pyrosetta-installer

Download PyRosetta wheel package from PyRosetta.org and install it

`pip install pyrosetta-installer` · installs (wheel) · licence: Rosetta Software License · rank 12392 · last release 2024-10-22 · [PyPI](https://pypi.org/project/pyrosetta-installer/)

### pye57

Python .e57 files reader/writer

`pip install pye57` · installs (wheel) · licence: MIT License · rank 12444 · last release 2025-11-26 · [PyPI](https://pypi.org/project/pye57/)

<details><summary>README extract</summary>

Python wrapper of LibE57Format to read and write .e57 point cloud files

Example:
```python
import numpy as np
import pye57

e57 = pye57.E57("e57_file.e57")

# read scan at index 0
data = e57.read_scan(0)

# 'data' is a dictionary with the point types as keys
assert isinstance(data["cartesianX"], np.ndarray)
assert isinstance(data["cartesianY"], np.ndarray)
assert isinstance(data["cartesianZ"], np.ndarray)

...
```

Sections: pye57, Example usage, Cloning the repository with required submodule, Dependencies on Linux, Dependencies on Windows, Dependencies on MacOS

</details>

### pyheif

Python 3.6+ interface to libheif library

`pip install pyheif` · installs from source (sdist only) · licence: Apache Software License · rank 12449 · last release 2024-09-01 · [PyPI](https://pypi.org/project/pyheif/)

<details><summary>README extract</summary>

Python 3.6+ interface to libheif library using CFFI

*Note*: currently only reading is supported.

Example:
```python
import pyheif

# Using a file path:
heif_file = pyheif.read("IMG_7424.HEIC")
# Or using bytes directly:
heif_file = pyheif.read(open("IMG_7424.HEIC", "rb").read())
```

Sections: pyheif, Usage, Read the primary image of a HEIF encoded file, Converting to a Pillow Image object, Read the entire container within the HEIF file, Objects, The HeifImage object, The UndecodedHeifImage object, The HeifContainer object, The HeifTopLevelImage object, The HeifDepthImage object, The HeifAuxiliaryImage object

</details>

### pymammotion

(no summary)

`pip install pymammotion` · installs (wheel) · licence: GPL-3.0 · rank 12466 · last release 2026-11-08 · [PyPI](https://pypi.org/project/pymammotion/)

_README extract left out: share-alike licence._

### portablemc

Cross platform command line utility for launching Minecraft quickly and reliably with included support for Mojang versions and popular mod loaders.

`pip install portablemc` · installs (wheel) · licence: Apache-2.0 · rank 12469 · last release 2026-10-18 · [PyPI](https://pypi.org/project/portablemc/) · [source](https://github.com/theorzr/portablemc)

<details><summary>README extract</summary>

Cross platform command line utility for launching Minecraft quickly and reliably with
included support for Mojang versions and popular mod loaders. It is also available as
a Rust crate for developers ~~and bindings for C and Python~~ (yet to come).

Features:
- Install and launch a version in 1 command.
- Supports Mojang versions, and many mod loaders which are installed seamlessly: Forge, NeoForge, Fabric, Quilt, LegacyFabric and Babric. ...

Sections: PortableMC, Features, Binaries, Cargo, PyPI, Linux packages, Arch Linux, NixOS, Usage, Repositories, Releasing

</details>

### pdqhash

"Python bindings for Facebook's PDQ hash"

`pip install pdqhash` · installs from source (sdist only) · licence: MIT · rank 12472 · last release 2025-05-28 · [PyPI](https://pypi.org/project/pdqhash/)

<details><summary>README extract</summary>

These are Python bindings to the PDQ perceptual hash released by Facebook. Note that the bindings are provided under the MIT license but the PDQ source code is licensed separately under its own license (see the `ThreatExchange/hashing/pdq` folder).

Example:
```python
import pdqhash

image = cv2.imread(os.path.join('tests', 'images', image_name))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hash_vector, quality = pdqhash.compute(image)

# Get all the rotations and flips in one pass.
# hash_vectors is a list of vectors in the following order
# - Original
# - Rotated 90 degrees
# - Rotated 180 degrees
...
```

Sections: pdqhash-python, Usage

</details>

### parquet-metadata

A tool to show metadata about a Parquet file

`pip install parquet-metadata` · installs (wheel) · licence: Apache Software License · rank 12506 · last release 2018-09-15 · [PyPI](https://pypi.org/project/parquet-metadata/)

<details><summary>README extract</summary>

Dump metadata about a Parquet file. You may also be interested in csv2parquet.

Sample output:

</details>

### Pymem

python memory access made easy

`pip install Pymem` · installs (wheel) · licence: MIT License · rank 12511 · last release 2024-10-27 · [PyPI](https://pypi.org/project/Pymem/) · [docs](https://pymem.readthedocs.io/en/latest/) · [source](https://github.com/srounet/Pymem)

<details><summary>README extract</summary>

A python library to manipulate Windows processes (32 and 64 bits).
With pymem you can hack into windows process and manipulate memory (read / write).

You can find pymem documentation on readthedoc there:

Sections: Pymem, Documentation, Examples

</details>

### pyscreenshot

python screenshot

`pip install pyscreenshot` · installs (wheel) · licence: BSD License · rank 12518 · last release 2023-03-12 · [PyPI](https://pypi.org/project/pyscreenshot/)

<details><summary>README extract</summary>

The pyscreenshot module is obsolete in most cases.
It was created because PIL ImageGrab module worked on Windows only,
but now Linux and macOS are also supported.
There are some features in pyscreenshot which can be useful in special cases:
flexible backends, Wayland support, sometimes better performance, optional subprocessing. ...

</details>

### pip-install-test

A minimal stub package to test success of pip install

`pip install pip-install-test` · installs (wheel) · licence: MIT · rank 12520 · last release 2019-03-28 · [PyPI](https://pypi.org/project/pip-install-test/)

<details><summary>README extract</summary>

Example:
```python
>>> import pip_install_test
```

Sections: Introduction, Usage

</details>

### pylint-exit

Exit code handler for pylint command line utility.

`pip install pylint-exit` · installs (wheel) · licence: MIT License · rank 12584 · last release 2020-07-15 · [PyPI](https://pypi.org/project/pylint-exit/)

<details><summary>README extract</summary>

Utility to handle pylint exit codes on Linux in a scripting-friendly way.

Pylint uses bit-encoded exit codes to convey the results of the pylint review,
which means it will return with a non-zero return code even when the
pylint scoring was successful. ...

Sections: pylint-exit, Usage, Return codes, Examples, Exiting gracefully on non-severe messages, Exiting with an error on severe messages, Treating errors and warnings as severe

</details>

### pyddq

Python API for Drunken Data Quality

`pip install pyddq` · installs from source (sdist only) · licence: Apache License Version 2.0 · rank 12597 · last release 2020-02-28 · [PyPI](https://pypi.org/project/pyddq/)

<details><summary>README extract</summary>

Python API of Drunken Data Quality.

DDQ is a small library for checking constraints on Spark data structures.
It can be used to assure a certain data quality, especially when continuous imports happen.

This project has been set up using PyScaffold 2.5.6. For details and usage
information on PyScaffold see

Sections: pyddq, Description, Note

</details>

### pyxlsb2

Excel 2007+ Binary Workbook (xlsb) parser

`pip install pyxlsb2` · installs (wheel) · licence: Apache Software License · rank 12629 · last release 2022-05-09 · [PyPI](https://pypi.org/project/pyxlsb2/)

<details><summary>README extract</summary>

`pyxlsb2` (a variant of pyxlsb - is an Excel 2007+ Binary Workbook (xlsb) parser written in Python.

`pyxslb2` offers the following improvements/changes in comparison to pyxlsb:

1. By default, keeps all data in memory instead of creating temporary files. ...

Example:
```python
from pyxlsb2 import open_workbook
with open_workbook('Book1.xlsb') as wb:
    # Do stuff with wb
```

Sections: pyxlsb2, Usage, Example, Limitations

</details>

### pymbar

Python implementation of the multistate Bennett acceptance ratio (MBAR) method

`pip install pymbar` · installs (wheel) · licence: MIT License · rank 12642 · last release 2024-03-21 · [PyPI](https://pypi.org/project/pymbar/)

<details><summary>README extract</summary>

Pymbar ( is a library
that provides tools for optimally combining simulations
from multiple thermodynamic states using maximum likelihood
methods to compute free energies (normalization constants)
and expectation values from all of the samples simultaneously.

</details>

### pan-os-python

Framework for interacting with Palo Alto Networks devices via API

`pip install pan-os-python` · installs (wheel) · licence: OSI Approved; ISC License (ISCL) · rank 12653 · last release 2026-07-22 · [PyPI](https://pypi.org/project/pan-os-python/) · [docs](https://pan-os-python.readthedocs.io) · [source](https://github.com/PaloAltoNetworks/pan-os-python)

<details><summary>README extract</summary>

The PAN-OS SDK for Python (pan-os-python) is a package to help interact with
Palo Alto Networks devices (including physical and virtualized Next-generation
Firewalls and Panorama). The pan-os-python SDK is object oriented and mimics
the traditional interaction with the device via the GUI or CLI/API.

Features ...

Example:
```python
import panos
```

</details>

### presidio-structured

Presidio structured package - analyzes and anonymizes structured and semi-structured data.

`pip install presidio-structured` · installs (wheel) · licence: MIT · rank 12669 · last release 2026-10-27 · [PyPI](https://pypi.org/project/presidio-structured/)

<details><summary>README extract</summary>

The Presidio structured package is a flexible and customizable framework designed to identify and protect structured sensitive data. This tool extends the capabilities of Presidio, focusing on structured data formats such as tabular formats and semi-structured formats (JSON). ...

Example:
```python
import pandas as pd
from presidio_structured import StructuredEngine, PandasAnalysisBuilder
from presidio_anonymizer.entities import OperatorConfig
from faker import Faker # optionally using faker as an example

# Initialize the engine with a Pandas data processor (default)
pandas_engine = StructuredEngine()

# Create a sample DataFrame
...
```

Sections: Presidio structured, Description, As a python package, Getting started, More information

</details>

### pytorch-wpe

A pytorch implementation of Weighted Prediction Error

`pip install pytorch-wpe` · installs (wheel) · licence: not stated · rank 12695 · last release 2021-03-05 · [PyPI](https://pypi.org/project/pytorch-wpe/)

### python-didl-lite

DIDL-Lite (Digital Item Declaration Language) tools for Python

`pip install python-didl-lite` · installs (wheel) · licence: Apache-2.0 · rank 12706 · last release 2026-10-21 · [PyPI](https://pypi.org/project/python-didl-lite/)

<details><summary>README extract</summary>

DIDL-Lite tools for Python to read and write DIDL-Lite-xml.

Sections: Usage, Resources / documents, Releasing

</details>

### pgembed

Self-contained postgres server for your python applications

`pip install pgembed` · installs (wheel) · licence: not stated · rank 12750 · last release 2026-03-18 · [PyPI](https://pypi.org/project/pgembed/) · [source](https://github.com/Ladybug-Memory/pgembed)

<details><summary>README extract</summary>

-green)

pgembed makes it easy to add a full-featured PostgreSQL database to your Python application—no server setup required. Your users simply run `pip install yourapp`, and PostgreSQL comes bundled automatically.

Think of it like SQLite, but with the power of PostgreSQL. ...

Example:
```python
import pgembed

# Initialize and start the server
pgembed.get_server("/path/to/my/data/dir")

# Connect and use like any PostgreSQL database
# ... your database code here
# Look in examples/*.py for more complete examples that could be run via uv
```

Sections: pgembed: Embedded PostgreSQL for Agents, What pgembed gives you, Quick start, Extensions, Checking available extensions, Building specific extensions

</details>

### pdbufr

Pandas reader for the BUFR format using ecCodes.

`pip install pdbufr` · installs (wheel) · licence: Apache Software License · rank 12756 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pdbufr/) · [docs](https://pdbufr.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Quick Start
 Installation
 Documentation

> \[!IMPORTANT\]
> This software is Incubating and subject to ECMWF's guidelines on Software Maturity.

pdbufr is a Python package implementing a Pandas reader for the BUFR format using ecCodes.

Example:
```python
import urllib.request
from pathlib import Path
import pdbufr

# get a radiosonde BUFR file
url = "
if not Path("temp.bufr").exists():
    urllib.request.urlretrieve(url, "temp.bufr")

# extract the station id, datetime, pressure and air temperature for two stations
# for all the available pressure levels into a pandas dataframe
...
```

</details>

### pytorch-fid

Package for calculating Frechet Inception Distance (FID) using PyTorch

`pip install pytorch-fid` · installs (wheel) · licence: Apache Software License · rank 12757 · last release 2023-01-05 · [PyPI](https://pypi.org/project/pytorch-fid/)

<details><summary>README extract</summary>

This is a port of the official implementation of Fréchet Inception Distance to PyTorch.
See for the original implementation using Tensorflow.

FID is a measure of similarity between two datasets of images. ...

Sections: FID score for PyTorch, Usage, Using different layers for feature maps, Generating a compatible `.npz` archive from a dataset, Citing

</details>

### pulumi-vault

A Pulumi package for creating and managing HashiCorp Vault cloud resources.

`pip install pulumi-vault` · installs (wheel) · licence: Apache-2.0 · rank 12769 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pulumi-vault/) · [source](https://github.com/pulumi/pulumi-vault)

<details><summary>README extract</summary>

The Vault resource provider for Pulumi lets you manage Vault resources in your cloud programs. To use
this package, please install the Pulumi CLI first.

Sections: Hashicorp Vault Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### piecewise-regression

piecewise (segmented) regression in python

`pip install piecewise-regression` · installs (wheel) · licence: MIT License · rank 12786 · last release 2023-12-18 · [PyPI](https://pypi.org/project/piecewise-regression/)

<details><summary>README extract</summary>

piecewise-regression provides tools for fitting continuous straight line models to data with breakpoint(s) where the gradient changes. For docs and more information, visit the Github repo at

</details>

### pulumi-argocd

A Pulumi package for creating and managing Argo CD resources.

`pip install pulumi-argocd` · installs (wheel) · licence: Apache-2.0 · rank 12797 · last release 2026-06-27 · [PyPI](https://pypi.org/project/pulumi-argocd/) · [source](https://github.com/Three141/pulumi-argocd)

<details><summary>README extract</summary>

The Argo CD Resource Provider lets you manage Argo CD resources.

Sections: Argo CD Resource Provider, Node.js (JavaScript/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pyceres

Factor graph optimization with Ceres, in Python

`pip install pyceres` · installs (wheel) · licence: Apache Software License · rank 12799 · last release 2025-11-05 · [PyPI](https://pypi.org/project/pyceres/) · [source](https://github.com/cvg/pyceres)

<details><summary>README extract</summary>

This repository provides minimal Python bindings for the Ceres Solver and the implementation of factor graphs for bundle adjustment and pose graph optimization.

Sections: pyceres, Factor graph optimization

</details>

### pytest-aioboto3

Aioboto3 Pytest with Moto

`pip install pytest-aioboto3` · installs (wheel) · licence: Other/Proprietary License; Public Domain · rank 12806 · last release 2025-01-17 · [PyPI](https://pypi.org/project/pytest-aioboto3/) · [source](https://github.com/phillipuniverse/pytest-aioboto3)

<details><summary>README extract</summary>

This is a Pytest plugin that sets up a Moto background service and patch the aioboto3 session to forward all calls to it. This is designed to work against any calls that create an `aiobotocore3.Session()` or `botocore3.Session()` automatically. ...

Example:
```python
async def test_aio_aws_bucket_access(aioboto3_s3_client: S3Client) -> None:
    resp = await aioboto3_s3_client.list_buckets()
    ...
```

Sections: aioboto3 mocking with Pytest and Moto, Running the example test, Usage

</details>

### pytdx

A Python Interface to TDX protocol

`pip install pytdx` · installs from source (sdist only) · licence: not stated · rank 12815 · last release 2019-08-26 · [PyPI](https://pypi.org/project/pytdx/)

<details><summary>README extract</summary>

用户文档会逐步转移到gitbook上，您可以在

阅读使用该api接口的详细文档。

Pytdx 是一款纯Python语言开发的类似TradeX的行情数据接口的实现。

Sections: Pytdx - Python tdx数据接口, 文档, 概述, 特点, 安装, 接口实现, 标准行情 pytdx.hq, 扩展行情 pytdx.exhq, 数据文件读取 pytdx.reader, 历史专业财务数据的爬取和解析, 交易相关 (使用TdxTradeServer(wrapper of trade.dll)), pytdx.pool (试验性质), 命令行, 缘起

</details>

### pigpio

Raspberry Pi GPIO module

`pip install pigpio` · installs (wheel) · licence: unlicense.org · rank 12820 · last release 2020-09-29 · [PyPI](https://pypi.org/project/pigpio/)

<details><summary>README extract</summary>

Raspberry Pi Python module to access the pigpio daemon

</details>

### python-consul2

Python client for Consul (http://www.consul.io/)

`pip install python-consul2` · installs (wheel) · licence: MIT License · rank 12837 · last release 2020-10-20 · [PyPI](https://pypi.org/project/python-consul2/)

<details><summary>README extract</summary>

Features:
* forked from cablehead/python-consul
* Fix `Consul.ACL` support

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

Sections: Python client for Consul.io, Example, Mailing List, Issue Labels, PRs, . All current tests pass, including flake8, . To add tests for your new features, if reasonable, 0.0.1, Features, 0.0.4, 0.0.5, 0.0.8

</details>

### phono3py

This is the phono3py module.

`pip install phono3py` · installs (wheel) · licence: BSD-3-Clause · rank 12842 · last release 2026-11-06 · [PyPI](https://pypi.org/project/phono3py/) · [source](https://github.com/phonopy/phono3py)

<details><summary>README extract</summary>

A simulation package of phonon-phonon interaction related properties mainly
written in python. Phono3py user documentation is found at

Usual phono3py questions should be sent to phonopy mailing list

See `pyproject.toml`.

Sections: phono3py, Mailing list for questions, Dependency, Documentation, How to run tests

</details>

### py-iam-expand

This is a Python package to expand and deobfuscate IAM policies.

`pip install py-iam-expand` · installs (wheel) · licence: Apache Software License · rank 12891 · last release 2026-02-24 · [PyPI](https://pypi.org/project/py-iam-expand/) · [docs](https://docs.prowler.cloud)

<details><summary>README extract</summary>

`py-iam-expand` is a Python tool to expand and deobfuscate AWS IAM actions.

This can help you to understand and analyze AWS IAM policies more effectively.

Features:
* Expand IAM actions with wildcards (`*`, `?`).
* Invert IAM action sets to find actions *not* matching specified patterns.
* Process IAM policies in JSON format.
* Command-line interface for easy use. ...

Example:
```python
usage: py-iam-expand [-h] [--version] [-i] [--invalid-action {raise,remove,keep}]
                     [--invalid-notaction {raise,remove,keep}]
                     [ACTION_PATTERN ...]

Expand AWS IAM action patterns provided as arguments/stdin lines OR expand actions within an IAM Policy JSON provided
via stdin.

positional arguments:
...
```

...

</details>

### python-language-server

Python Language Server for the Language Server Protocol

`pip install python-language-server` · installs (wheel) · licence: not stated · rank 12923 · last release 2020-12-11 · [PyPI](https://pypi.org/project/python-language-server/)

<details><summary>README extract</summary>

A Python 2.7 and 3.5+ implementation of the Language Server Protocol.

Sections: Python Language Server, 3rd Party Plugins, Configuration, Language Server Features

</details>

### pypsa

Python for Power Systems Analysis

`pip install pypsa` · installs (wheel) · licence: MIT License · rank 12925 · last release 2026-10-09 · [PyPI](https://pypi.org/project/pypsa/) · [docs](https://docs.pypsa.org) · [source](https://github.com/PyPSA/PyPSA)

<details><summary>README extract</summary>

PyPSA stands for Python for Power System Analysis. It is pronounced
pipes-ah.

PyPSA is an open-source Python framework for optimising and simulating modern
power and energy systems that include features such as conventional generators
with unit commitment, variable wind and solar generation, hydro-electricity,
inter-temporal storage, coupling to ...

Features:
- Economic Dispatch (ED): Models short-term market-based dispatch including
unit commitment, renewable availability, short-duration and seasonal storage
including hydro reservoirs with inflow and spillage dynamics, elastic demands,
load shedding and ...

Example:
```python
import pypsa

# create a new network
n = pypsa.Network()
n.add("Bus", "mybus")
n.add("Load", "myload", bus="mybus", p_set=100)
...

</details>

### pyspark-stubs

A collection of the Apache Spark stub files

`pip install pyspark-stubs` · installs (wheel) · licence: Apache Software License · rank 12940 · last release 2022-01-05 · [PyPI](https://pypi.org/project/pyspark-stubs/)

<details><summary>README extract</summary>

A collection of the Apache Spark stub
files. These
files were generated by
stubgen
and manually edited to include accurate type hints.

Tests and configuration files have been originally contributed to the
Typeshed project. Please refer
to its contributors
list and
license for
details. ...

Sections: PySpark Stubs, Important, Motivation, PySpark Version Compatibility, See also, Disclaimer, Footnotes

</details>

### python_arptable

Python simple arp table reader

`pip install python_arptable` · installs from source (sdist only) · licence: BSD License · rank 12946 · last release 2018-04-05 · [PyPI](https://pypi.org/project/python_arptable/)

<details><summary>README extract</summary>

Python simple arp table reader

* Free software: BSD license

Features:
* Export ARP Table on linux as a dictionary.

Example:
```python
>>> from arp_table import ARPTABLE
>>> print(ARPTABLE)

[{'Device': 'eth0',
  'Flags': '0x2',
  'HW address': '00:12:79:d2:b9:67',
  'HW type': '0x1',
  'IP address': '10.3.0.1',
  'Mask': '*'}]

>>> from arp_table import get_arp_table
>>> print(get_arp_table())

[{'Device': 'eth0',
  'Flags': '0x2',
  'HW address': '00:12:79:d2:b9:67',
...
```

Sections: Python simple arp table reader, Features, Usage, Disclaimer, 0.0.1 (2015-06-14)

</details>

### pygeomag

A python port of the World Magnetic Model (WMM)

`pip install pygeomag` · installs (wheel) · licence: MIT License · rank 12971 · last release 2024-12-21 · [PyPI](https://pypi.org/project/pygeomag/)

<details><summary>README extract</summary>

What is declination?

Declination is the angle that adjusts a compass reading from Magnetic North to True North. Many
maps will show it in the legend, so you can adjust your compass (either physically or mentally).

Why do you need this?

In Washington State, the declination angle is between 14° and 16° West depending on your location. ...

Example:
```python
>>> from pygeomag import GeoMag
>>> geo_mag = GeoMag(coefficients_file="wmm/WMM_2025.COF")
>>> result = geo_mag.calculate(glat=47.6205, glon=-122.3493, alt=0, time=2025.25)
>>> print(result.d)
15.065629638512593
```

Sections: Welcome to pyGeoMag's documentation!, High Resolution, Example, Validation, Notes, Documentation

</details>

### pid

Pidfile featuring stale detection and file-locking, can also be used as context-manager or decorator

`pip install pid` · installs (wheel) · licence: Apache Software License · rank 12982 · last release 2020-07-18 · [PyPI](https://pypi.org/project/pid/)

<details><summary>README extract</summary>

PidFile class featuring:

 - stale detection
 - pidfile locking (fcntl)
 - chmod (default is 0o644)
 - chown
 - custom exceptions

PidFile can be used as a context manager:

Logging to file is also possible when using PidFile with a daemon context manager
(e.g. python-daemon). ...

Example:
```python
from pid import PidFile
import os

with PidFile('foo') as p:
  print(p.pidname) # -> 'foo'
  print(p.piddir) # -> '/var/run' But you can modify it when initialize PidFile.
  print(os.listdir('/var/run')) # -> ['foo.pid']

# pid file will delete after 'with' literal.
```

Sections: pid, Context Manager, Daemons and Logging, Decorator, Exception Order, Behaviour

</details>

### python-irodsclient

A Python API for iRODS

`pip install python-irodsclient` · installs (wheel) · licence: BSD-3-Clause · rank 12984 · last release 2026-03-18 · [PyPI](https://pypi.org/project/python-irodsclient/) · [source](https://github.com/irods/python-irodsclient)

<details><summary>README extract</summary>

iRODS is an open source distributed data management system. This is a client API implemented in Python.

Currently supported:

- Python 3.9 or later
- Establish a (secure) connection to iRODS
- Authenticate via password, GSI, PAM
- GenQuery and Specific Queries
- GenQuery2 ...

Example:
```python
>>> from irods.session import iRODSSession
>>> with iRODSSession(host='localhost', port=1247, user='bob', password='1234', zone='tempZone') as session:
...      # workload
...
>>>
```

</details>

### PySideSix-Frameless-Window

A cross-platform frameless window based on pyside6, support Win32, Linux and macOS.

`pip install PySideSix-Frameless-Window` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 12991 · last release 2026-08-02 · [PyPI](https://pypi.org/project/PySideSix-Frameless-Window/)

_README extract left out: share-alike licence._

### python-mistralclient

Mistral Client Library

`pip install python-mistralclient` · installs (wheel) · licence: Apache Software License · rank 13003 · last release 2026-08-27 · [PyPI](https://pypi.org/project/python-mistralclient/)

<details><summary>README extract</summary>

Mistral is a workflow service. Most business processes consist of multiple
distinct interconnected steps that need to be executed in a particular
order in a distributed environment. A user can describe such a process as a set
of tasks and their transitions. ...

Sections: Mistral, Mistral client, Running Mistral client, Useful Links

</details>

### panda3d-simplepbr

A straight-forward, easy-to-use, drop-in, PBR replacement for Panda3D's builtin auto shader

`pip install panda3d-simplepbr` · installs (wheel) · licence: BSD License · rank 13010 · last release 2025-03-30 · [PyPI](https://pypi.org/project/panda3d-simplepbr/)

<details><summary>README extract</summary>

A straight-forward, easy-to-use PBR render pipeline for Panda3D.
This project aims to be a drop-in replacement for Panda3D's auto-shader.
The PBR shader is heavily inspired by the Khronos glTF Sample Viewer.
*Note:* this project does not make an attempt to match a reference renderer.

Features:
* Supports running on a wide range of hardware with an easy OpenGL 2.1+ requirement
* Forward rendered metal-rough PBR
* All Panda3D light types (point, directional, spot, and ambient)
* Filmic tonemapping
* Normal maps
* Emission maps
* Occlusion ...

Example:
```python
from direct.showbase.ShowBase import ShowBase

import simplepbr

class App(ShowBase):
    def init(self):
        super().init()

        simplepbr.init()
```

...

</details>

### pydantic-compat

Compatibility layer for pydantic v1/v2

`pip install pydantic-compat` · installs (wheel) · licence: BSD License · rank 13014 · last release 2023-10-24 · [PyPI](https://pypi.org/project/pydantic-compat/) · [source](https://github.com/pyapp-kit/pydantic-compat)

<details><summary>README extract</summary>

Pydantic 2 was a major release that completely changed the pydantic API.

For applications, this is not a big deal, as they can pin to whatever version of
pydantic they need. But for libraries that want to exist in a broader
environment, pinning to a specific version of pydantic is not always an option
(as it limits the ability to co-exist with ...

Example:
```python
from pydantic import BaseModel
from pydantic_compat import PydanticCompatMixin
from pydantic_compat import field_validator  # or 'validator'
from pydantic_compat import model_validator  # or 'root_validator'

class MyModel(PydanticCompatMixin, BaseModel):
    x: int
    y: int = 2

    # prefer v2 dict, but v1 class Config is supported
...
```

...

</details>

### pulsar-galaxy-lib

Distributed job execution application built for Galaxy (http://galaxyproject.org/).

`pip install pulsar-galaxy-lib` · installs (wheel) · licence: Apache License 2.0 · rank 13019 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pulsar-galaxy-lib/)

<details><summary>README extract</summary>

This project is a Python server application that allows a Galaxy server to run jobs on remote systems (including
Windows) without requiring a shared mounted file system. Unlike traditional
Galaxy job runners - input files, scripts, and config files may be transferred
to the remote system, the job is executed, and the results are transferred ...

Sections: Configuring Galaxy, Quickstart, 0.16.0 (2026-10-11), 0.15.16 (2026-10-08), 0.15.15 (2026-07-13), 0.15.14 (2025-01-20), 0.15.13 (2026-01-12), 0.15.12 (2025-11-28), 0.15.11 (2025-09-30), 0.15.10 (2025-09-04), 0.15.9 (2025-07-17), 0.15.8 (2025-06-09), 0.15.7 (2025-03-13), 0.15.6 (2024-01-15)

</details>

### pyshortcuts

Create desktop and Start Menu shortcuts for python scripts

`pip install pyshortcuts` · installs (wheel) · licence: MIT · rank 13033 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pyshortcuts/) · [docs](https://github.com/newville/pyshortcuts/README.md)

<details><summary>README extract</summary>

Install `pyshortcuts` with

Full documentation is at: Pyshortcuts Documentation

Example:
```python
from pyshortcuts import make_shortcut

make_shortcut('/home/user/bin/myapp.py', name='MyApp', icon='/home/user/icons/myicon.ico')
```

Sections: Pyshortcuts Overview, Usage from Python, `pyshortcut` command-line program, Making a shortcut for single python command, `pyshortcut` GUI

</details>

### pykd

python windbg extension

`pip install pykd` · does not install on CPython 3.14 · licence: not stated · rank 13036 · last release 2020-10-21 · [PyPI](https://pypi.org/project/pykd/)

### pipecatcloud

Cloud hosting for Pipecat AI applications

`pip install pipecatcloud` · installs (wheel) · licence: BSD 2-Clause License · rank 13042 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pipecatcloud/)

<details><summary>README extract</summary>

Python module and CLI for interacting with Pipecat Cloud.

- Python 3.11+
- Docker and a Docker repository (e.g. Docker Hub)
- Active Pipecat Cloud
 account

Documentation for Pipecat Cloud is available here.

Example:
```python
from pipecatcloud.session import Session
from pipecatcloud.exception import AgentStartError
import asyncio

async def main():
    session = Session(
        agent_name="your-agent-name",
        api_key="pk...",
    )

    try:
        await session.start()
    except AgentStartError as e:
        print(e)
    except Exception as e:
...
```

Sections: Pipecat Cloud, Requirements, Documentation, Usage, Seeing your secret keys, Usage in Python scripts, Troubleshooting, SSL certificate errors on macOS, Setup Steps, Running tests

</details>

### panda3d-gltf

glTF utilities for Panda3D

`pip install panda3d-gltf` · installs (wheel) · licence: BSD License · rank 13054 · last release 2025-03-16 · [PyPI](https://pypi.org/project/panda3d-gltf/)

<details><summary>README extract</summary>

This project adds glTF loading capabilities to Panda3D.
One long-term goal for this project is to be used as a reference for adding a builtin, C++ glTF loader to Panda3D.
If and when Panda3D gets builtin support for glTF, this module will go into maintenance mode and be used to backport glTF support to older versions of Panda3D.

Features:
* Adds support for native loading of glTF files
* Supports glTF 2.0
* Supports binary glTF

 * KHR_lights (deprecated in favor of KHR_lights_punctual)
 * KHR_lights_punctual
 * BLENDER_physics
* Ships with a `gltf2bam` cli-tool for converting glTF ...

Sections: panda3d-gltf, Features, Usage, Configuration, Native loading, Command Line, Viewer, Running Tests, Building Wheels

</details>

### py-lib3mf

Python bindings for Lib3MF

`pip install py-lib3mf` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 13072 · last release 2026-05-04 · [PyPI](https://pypi.org/project/py-lib3mf/)

<details><summary>README extract</summary>

Minimal files required to use lib3mf in python. Provides a pip-installable package for the python API that wraps Lib3MF API available here: The repository that is used to prepare the PyPI release is here

</details>

### python-troveclient

Client library for OpenStack DBaaS API

`pip install python-troveclient` · installs (wheel) · licence: Apache Software License · rank 13083 · last release 2026-08-28 · [PyPI](https://pypi.org/project/python-troveclient/)

<details><summary>README extract</summary>

This is a client for the OpenStack Trove API. There's a Python API (the
`troveclient` module), and a command-line script (`trove`). Each
implements 100% of the OpenStack Trove API.

See the Trove CLI Guide for information on how to use the `trove`
command-line tool. You may also want to look at the
OpenStack API documentation. ...

</details>

### plum-py

Pack/Unpack Memory.

`pip install plum-py` · installs (wheel) · licence: MIT License · rank 13091 · last release 2024-05-12 · [PyPI](https://pypi.org/project/plum-py/)

<details><summary>README extract</summary>

The plum-py Python package provides classes and utility functions to
transform byte sequences into Python objects and back. While similar in
purpose to Python's standard library `struct` module, this package
provides a larger set of format specifiers and is extensible, allowing
you to easily create complex ones of your own.

</details>

### pixeloe

Detail-Oriented Pixelization based on Contrast-Aware Outline Expansion.

`pip install pixeloe` · installs (wheel) · licence: Apache-2.0 · rank 13093 · last release 2026-09-24 · [PyPI](https://pypi.org/project/pixeloe/) · [source](https://github.com/KohakuBlueleaf/PixelOE)

<details><summary>README extract</summary>

Create stunning pixel art from high-resolution images without AI or complex networks.

PixelOE is a Python library that generates high-quality pixel art from standard images using a novel, contrast-aware approach. ...

Example:
```python
import cv2
from pixeloe.pixelize import pixelize

img = cv2.imread("img/test.webp")
img = pixelize(img, target_size=256, patch_size=8)
cv2.imwrite("img/test2.webp", img)
```

Sections: Usage, ComfyUI, Command Line Interface (CLI), Gradio, Python API, Example, Outline Expansion, Pixelization, Use outline expansion to improve existing method, Algorithms Implemented in This Project, How It Works, 1. Contrast-Aware Outline Expansion, 2. Contrast-Based Downsampling, Optional Enhancements

</details>

### percy-selenium

Python client for visual testing with Percy

`pip install percy-selenium` · installs (wheel) · licence: MIT License · rank 13154 · last release 2026-07-13 · [PyPI](https://pypi.org/project/percy-selenium/)

<details><summary>README extract</summary>

Percy visual testing for Python Selenium.

Example:
```python
from percy import percy_snapshot

browser = webdriver.Firefox()
browser.get('
​
# take a snapshot
percy_snapshot(browser, 'Python example')
```

Sections: percy-selenium-python, Usage, Configuration, Migrating Config, Percy on Automate, Example Usage for regions, Creating Percy on automate build, Robot Keywords, Percy Snapshot, Percy Screenshot (Automate), Create Percy Region, Percy Is Running

</details>

### pytest-asyncio-cooperative

Run all your asynchronous tests cooperatively.

`pip install pytest-asyncio-cooperative` · installs (wheel) · licence: MIT License · rank 13163 · last release 2025-06-24 · [PyPI](https://pypi.org/project/pytest-asyncio-cooperative/)

### pyrit

The Python Risk Identification Tool for LLMs (PyRIT) is a library used to assess the robustness of LLMs

`pip install pyrit` · installs (wheel) · licence: MIT · rank 13170 · last release 2026-09-04 · [PyPI](https://pypi.org/project/pyrit/)

<details><summary>README extract</summary>

The Python Risk Identification Tool for generative AI (PyRIT) is an open source
framework built to empower security professionals and engineers to proactively
identify risks in generative AI systems.

- Check out our website for more information
 about how to use, install, or contribute to PyRIT. ...

</details>

### petri-bloom

Framework for generating behavioral evaluations of frontier AI models.

`pip install petri-bloom` · installs (wheel) · licence: MIT License · rank 13174 · last release 2026-06-08 · [PyPI](https://pypi.org/project/petri-bloom/) · [source](https://github.com/meridianlabs-ai/petri_bloom)

<details><summary>README extract</summary>

Welcome to Petri Bloom, an implementation of the Bloom automated evaluation tool using the Petri auditor/target framework.

Bloom generates evaluation suites that probe LLMs for specific behaviors (sycophancy, self-preservation, political bias, etc.). ...

</details>

### pyreadline

A python implmementation of GNU readline.

`pip install pyreadline` · installs from source (sdist only) · licence: BSD License · rank 13176 · last release 2015-09-16 · [PyPI](https://pypi.org/project/pyreadline/)

<details><summary>README extract</summary>

The pyreadline package is a python implementation of GNU readline functionality
it is based on the ctypes based UNC readline package by Gary Bishop.
It is not complete. It has been tested for use with windows 2000 and windows xp.

* pyreadline 2.1 <2015-09-16>

 This is a bugfix release to make pyreadline work with python 3.5. ...

</details>

### pySigma-backend-opensearch

pySigma OpenSearch backend

`pip install pySigma-backend-opensearch` · installs (wheel) · licence: LGPL-3.0-only · rank 13177 · last release 2026-05-20 · [PyPI](https://pypi.org/project/pySigma-backend-opensearch/)

_README extract left out: share-alike licence._

### pulumi-oci

A Pulumi package for creating and managing Oracle Cloud Infrastructure resources.

`pip install pulumi-oci` · installs (wheel) · licence: Apache-2.0 · rank 13182 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pulumi-oci/) · [source](https://github.com/pulumi/pulumi-oci)

<details><summary>README extract</summary>

The Oracle Cloud Infrastructure (OCI) Resource Provider lets you manage OCI resources.

Sections: Oracle Cloud Infrastructure Resource Provider, Node.js (JavaScript/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pytest-archon

Rule your architecture like a real developer

`pip install pytest-archon` · installs (wheel) · licence: Apache Software License · rank 13183 · last release 2025-09-19 · [PyPI](https://pypi.org/project/pytest-archon/) · [source](https://github.com/jwbargsten/pytest-archon)

<details><summary>README extract</summary>

`pytest-archon` is a little tool that helps you structure (large) Python projects. This
tool allows you to define architectural boundaries in your code, also known as
_forbidden dependencies.

Explicitly defined architectural boundaries helps you keep your code in shape. It avoids
the creation of circular dependencies. ...

Example:
```python
from pytest_archon import archrule

def test_rule_basic():
    (
        archrule("name", comment="some comment")
        .match("pytest_archon.col*")
        .exclude("pytest_archon.colgate")
        .should_not_import("pytest_archon.import_finder")
        .should_import("pytest_archon.core*")
        .check("pytest_archon")
    )
```

...

</details>

### pyghidra

Native CPython for Ghidra

`pip install pyghidra` · installs (wheel) · licence: Apache Software License · rank 13187 · last release 2026-10-22 · [PyPI](https://pypi.org/project/pyghidra/) · [source](https://github.com/NationalSecurityAgency/ghidra)

<details><summary>README extract</summary>

The PyGhidra Python library, originally developed by the
Department of Defense Cyber Crime Center (DC3) under the name "Pyhidra", is a
Python library that provides direct access to the Ghidra API within a native CPython 3 interpreter
using JPype. ...

Example:
```python
import os, jpype, pyghidra
pyghidra.start()

# Open/create a project
with pyghidra.open_project(os.environ["GHIDRA_PROJECT_DIR"], "ExampleProject", create=True) as project:

    # Walk a Ghidra release zip file, load every decompiler binary, and save them to the project
...
```

...

</details>

### pykaos

(no summary)

`pip install pykaos` · installs (wheel) · licence: not stated · rank 13214 · last release 2026-04-02 · [PyPI](https://pypi.org/project/pykaos/)

<details><summary>README extract</summary>

PyKAOS is a lightweight Python library providing an abstraction layer for agents to interact with operating systems. File operations and command executions via KAOS can be easily switched between local environment and remote systems over SSH.

</details>

### pydantic-tes

Pydantic Models for the GA4GH Task Execution Service

`pip install pydantic-tes` · installs (wheel) · licence: MIT License · rank 13220 · last release 2026-04-13 · [PyPI](https://pypi.org/project/pydantic-tes/) · [source](https://github.com/jmchilton/pydantic-tes/issues)

<details><summary>README extract</summary>

A collection of pydantic models for GA4GH Task Execution Service.

In addition to the models, this package contains a lightweight client for TES based
on them using requests and utilities for working and testing it against Funnel -
a the TES implementation.

This Python project can be installed from PyPI using `pip`. ...

Sections: pydantic-tes, 0.4.0 (2026-04-13), 0.3.0 (2026-03-03), 0.2.0 (2025-04-10), 0.1.5 (2022-10-06), 0.1.4 (2022-10-06), 0.1.3 (2022-10-05), 0.1.2 (2022-10-05), 0.1.1 (2022-09-29), 0.1.0 (2022-09-29)

</details>

### property-cached

A decorator for caching properties in classes (forked from cached-property).

`pip install property-cached` · installs (wheel) · licence: BSD License · rank 13255 · last release 2020-03-06 · [PyPI](https://pypi.org/project/property-cached/)

<details><summary>README extract</summary>

A decorator for caching properties in classes (forked from `cached-property`).

This library was forked from the upstream library `cached-property` since its
developer does not seem to be maintaining it anymore. ...

Features:
* Makes caching of time or computational expensive properties quick and easy.
* Because I got tired of copy/pasting this code from non-web project to non-web project.

Example:
```python
class Monopoly(object):

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

### piqp

A Proximal Interior Point Quadratic Programming solver

`pip install piqp` · installs (wheel) · licence: not stated · rank 13267 · last release 2026-11-05 · [PyPI](https://pypi.org/project/piqp/)

<details><summary>README extract</summary>

-90e3dc.svg)

PIQP is a Proximal Interior Point Quadratic Programming solver, which can solve dense and sparse quadratic programs of the form

\begin{aligned}
\min{x} \quad & \frac{1}{2} x^\top P x + c^\top x \\
\text {s.t.}\quad & Ax=b, \\
& h_l \leq Gx \leq h_u, \\
& x_l \leq x \leq x_u,
\end{aligned} ...

Features:
* PIQP is written in header only C++ 14 leveraging the Eigen library for vectorized linear algebra.
* Dense and sparse problem formulations are supported. ...

Sections: PIQP, Features, Interfaces, Citing our Work

</details>

### pickle5

Backport of the pickle 5 protocol (PEP 574) and other pickle changes

`pip install pickle5` · does not install on CPython 3.14 · licence: Python Software Foundation License · rank 13275 · last release 2021-11-20 · [PyPI](https://pypi.org/project/pickle5/)

### pytorch-minimize

Newton and Quasi-Newton optimization with PyTorch

`pip install pytorch-minimize` · installs (wheel) · licence: MIT License · rank 13323 · last release 2026-01-23 · [PyPI](https://pypi.org/project/pytorch-minimize/) · [docs](https://pytorch-minimize.readthedocs.io)

<details><summary>README extract</summary>

For the most up-to-date information on pytorch-minimize, see the docs site: pytorch-minimize.readthedocs.io

Pytorch-minimize represents a collection of utilities for minimizing multivariate functions in PyTorch.
It is inspired heavily by SciPy's `optimize` module and MATLAB's Optimization Toolbox. ...

Example:
```python
import torch
from torchmin import minimize

def rosen(x):
    return torch.sum(100*(x[..., 1:] - x[..., :-1]2)2
                     + (1 - x[..., :-1])**2)

# initial point
x0 = torch.tensor([1., 8.])

# Select from the following methods:
# ['bfgs', 'l-bfgs', 'cg', 'newton-cg', 'newton-exact',
...
```

...

</details>

### pbxproj

XCode Project manipulation library for Python

`pip install pbxproj` · installs (wheel) · licence: MIT · rank 13351 · last release 2026-02-04 · [PyPI](https://pypi.org/project/pbxproj/)

### pycdfpp

A modern C++ header only cdf library

`pip install pycdfpp` · installs (wheel) · licence: MIT License · rank 13353 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pycdfpp/) · [docs](https://pycdfpp.readthedocs.io/en/latest/) · [source](https://github.com/SciQLop/CDFpp)

<details><summary>README extract</summary>

A modern, from-scratch C++20 implementation of NASA's CDF (Common Data Format) with full Python bindings.

📖 Documentation: quickstart, guides for reading and for producing ISTP-compliant files, cookbook, and C++ guide. The examples run live in your browser. ...

Features:
- C++20 library, mostly headers — see the C++ guide for the compiler flags
- Complete read/write support — CDF versions 2.2 through 3.x, row and column major, compressed files and variables (GZip, RLE) ...

Example:
```python
import pycdfpp

cdf = pycdfpp.load("my_data.cdf")

# Variables expose numpy arrays (zero-copy when possible)
data = cdf["variable_name"].values

# Global attributes
print(cdf.attributes"Project")

# Variable attributes
print(cdf["variable_name"].attributes["UNITS"].value)

...

</details>

### plato-sdk

Plato SDK

`pip install plato-sdk` · does not install on CPython 3.14 · licence: not stated · rank 13395 · last release 2026-10-30 · [PyPI](https://pypi.org/project/plato-sdk/)

<details><summary>README extract</summary>

Example:
```python
import asyncio
import os
from plato import Plato, PlatoTask
from plato.examples.doordash_tasks import all_tasks as doordash_tasks

base_prompt = """
You are a helpful assistant that can help me buy food from doordash.
start by going to {start_url}. Do not navigate to other websites.
...
```

Sections: Plato SDK, Usage, State mutations

</details>

### prophecy-libs

Helper library for prophecy generated code

`pip install prophecy-libs` · installs (wheel) · licence: GPL-3.0 · rank 13401 · last release 2026-09-14 · [PyPI](https://pypi.org/project/prophecy-libs/)

_README extract left out: share-alike licence._

### plugp100

Controller for TP-Link Tapo P100 and other devices

`pip install plugp100` · installs (wheel) · licence: GPL-3.0-only · rank 13403 · last release 2026-10-19 · [PyPI](https://pypi.org/project/plugp100/) · [source](https://github.com/petretiandrea/plugp100)

_README extract left out: share-alike licence._

### pytdigest

Python package for *fast* TDigest calculation.

`pip install pytdigest` · installs from source (sdist only) · licence: Apache Software License · rank 13409 · last release 2023-02-03 · [PyPI](https://pypi.org/project/pytdigest/) · [docs](https://protivinsky.github.io/pytdigest)

<details><summary>README extract</summary>

Python package for fast TDigest calculation.

- C implementation and thin Python wrapper
- suitable for big data and streaming and distributed settings
- developed for smooth compatibility with Pandas and numpy

Based on previous work of Ted Dunning and Andrew Werner.

Example:
```python
from pytdigest import TDigest
import numpy as np
import pandas as pd

rng = np.random.default_rng(12354)
n = 100_000
x = rng.normal(loc=0, scale=10, size=n)
w = rng.exponential(scale=1, size=n)

# estimation from data is simple:
td = TDigest.compute(x, w, compression=1_000)
...
```

Sections: Basic example, Performance, Similar packages, Future plans, Documentation, Legal stuff

</details>

### pyg-nightly

Graph Neural Network Library for PyTorch

`pip install pyg-nightly` · installs (wheel) · licence: MIT · rank 13437 · last release 2026-11-08 · [PyPI](https://pypi.org/project/pyg-nightly/) · [docs](https://pytorch-geometric.readthedocs.io) · [source](https://github.com/pyg-team/pytorch_geometric.git)

<details><summary>README extract</summary>

______________

[][pypi-url]
[][pypi-download-url]
[][slack-url]
[][contributing-url]

Documentation |
PyG 1.0 Paper |
PyG 2.0 Paper |
Colab Notebooks |
External Resources |
OGB Examples ...

Example:
```python
import torch
from torch import Tensor
from torch_geometric.nn import GCNConv
from torch_geometric.datasets import Planetoid

dataset = Planetoid(root='.', name='Cora')

class GCN(torch.nn.Module):
    def init(self, in_channels, hidden_channels, out_channels):
        super().init()
        self.conv1 = GCNConv(in_channels, hidden_channels)
...
```

...

</details>

### pyspeex-noise

Noise suppression and automatic gain with speex

`pip install pyspeex-noise` · installs (wheel) · licence: MIT · rank 13452 · last release 2026-06-04 · [PyPI](https://pypi.org/project/pyspeex-noise/)

<details><summary>README extract</summary>

Noise suppression and automatic gain control using speex.

Example:
```python
from pyspeex_noise import AudioProcessor

auto_gain = 4000
noise_suppression = -30
audio_processor = AudioProcessor(auto_gain, noise_suppression)

# Process 10ms chunks of 16-bit mono PCM @16Khz
while audio := get_10ms_of_audio():  # you define this
    assert len(audio) == 160 * 2  # 160 samples
...
```

</details>

### pytest-rng

Fixtures for seeding tests and making randomness reproducible

`pip install pytest-rng` · installs (wheel) · licence: MIT License · rank 13454 · last release 2019-08-08 · [PyPI](https://pypi.org/project/pytest-rng/)

<details><summary>README extract</summary>

`pytest-rng` provides fixtures for
ensuring "randomness" in your tests is reproducible
from one run to the next.
It also allows the seed for all tests to be changed if requested,
to help ensure that test successes are not dependent on
particular random number seeds. ...

Example:
```python
import numpy as np

def test_rectification(rng, seed):
    print(rng.uniform(-1, 1, size=3))
    print(seed)
```

Sections: pytest-rng, Seed generation, salt, 1.0.0 (August 8, 2019)

</details>

### pytest-sentry

A pytest plugin to send testrun information to Sentry.io

`pip install pytest-sentry` · installs (wheel) · licence: BSD-2-Clause · rank 13466 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pytest-sentry/) · [source](https://github.com/getsentry/pytest-sentry)

<details><summary>README extract</summary>

`pytest-sentry` is a pytest plugin that uses Sentry to store and aggregate information about your testruns.

> [!IMPORTANT]
> This is not an official Sentry product.

This is what a test run will look like in Sentry.

Example:
```python
import random
import pytest

from sentry_sdk import Scope
from pytest_sentry import Client

@pytest.mark.sentry_client(None)
def test_no_sentry():
    # Even though flaky, this test never gets reported to sentry
    assert random.random() > 0.5

@pytest.mark.sentry_client("MY NEW DSN")
def test_custom_dsn():
...
```

Sections: pytest-sentry, Quickstart, Prerequisites, Configuration, Running, Tracking flaky tests as errors, Tracking the performance of your testsuite, Advanced Options, Accessing the used Sentry client, Always reporting test failures

</details>

### PraisonAI

Open-source Python AI agent framework that runs on your own computers, even fully offline.

`pip install PraisonAI` · installs (wheel) · licence: MIT · rank 13467 · last release 2026-11-05 · [PyPI](https://pypi.org/project/PraisonAI/) · [source](https://github.com/mervinpraison/PraisonAI)

<details><summary>README extract</summary>

Private AI that earns trust one task at a time.

PraisonAI runs AI agents on your own computers, even fully offline, so private data never has to leave the building.

- For highly regulated teams (early access): each task moves to your own AI only after it passes a test. ...

Features:
- Agents and multi-agent teams: Agents · Handoffs · Workflows
- Memory: Memory · Knowledge and RAG · Sessions
- Tools and MCP: Tools · MCP
- Guardrails and approval: Guardrails · Human approval · Policy engine ...

Example:
```python
from praisonaiagents import Agent

agent = Agent(instructions="You are a helpful assistant.")
print(agent.start("In two sentences, why do some companies keep their data on their own computers?"))
```

...

</details>

### pyspark-dist-explore

Create histogram and density plots from PySpark Dataframes

`pip install pyspark-dist-explore` · installs (wheel) · licence: MIT License · rank 13473 · last release 2019-08-20 · [PyPI](https://pypi.org/project/pyspark-dist-explore/)

### pyexiv2

Read and write image metadata, including EXIF, IPTC, XMP, ICC Profile.

`pip install pyexiv2` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 13491 · last release 2026-08-02 · [PyPI](https://pypi.org/project/pyexiv2/)

_README extract left out: share-alike licence._

### presidio-image-redactor

Presidio image redactor package

`pip install presidio-image-redactor` · installs (wheel) · licence: MIT · rank 13495 · last release 2026-10-27 · [PyPI](https://pypi.org/project/presidio-image-redactor/)

<details><summary>README extract</summary>

The Presidio Image Redactor is a Python based module for detecting and redacting PII text entities in images.

Use the following button to deploy presidio image redactor to your Azure subscription.

Process for standard images:

Process for DICOM files:

Example:
```python
from PIL import Image
from presidio_image_redactor import ImageRedactorEngine

# Get the image to redact using PIL lib (pillow)
image = Image.open("presidio-image-redactor/tests/integration/resources/ocr_test.png")

# Initialize the engine
engine = ImageRedactorEngine()

# Redact the image with pink color
...
```

...

</details>

### promptflow-tracing

Prompt flow tracing

`pip install promptflow-tracing` · installs (wheel) · licence: MIT License · rank 13505 · last release 2026-05-01 · [PyPI](https://pypi.org/project/promptflow-tracing/) · [source](https://github.com/microsoft/promptflow)

<details><summary>README extract</summary>

The `promptflow-tracing` package offers tracing capabilities to capture and illustrate the internal execution processes of both DAG flow and Flex flow. It is designed to be compatible with OpenTelemetry. ...

Sections: Prompt flow tracing, Introduction

</details>

### pyxbe

Library to work with XBE files

`pip install pyxbe` · installs (wheel) · licence: MIT · rank 13535 · last release 2026-06-08 · [PyPI](https://pypi.org/project/pyxbe/) · [source](https://github.com/mborgerson/pyxbe)

<details><summary>README extract</summary>

Pure Python 3.12+ library to work with `.xbe` files, the executable file format for the original Xbox game console.

Documentation covering how to install and use pyxbe is available here.

</details>

### promptflow-core

Prompt flow core

`pip install promptflow-core` · installs (wheel) · licence: MIT License · rank 13552 · last release 2026-05-01 · [PyPI](https://pypi.org/project/promptflow-core/) · [source](https://github.com/microsoft/promptflow)

<details><summary>README extract</summary>

The `promptflow-core` package provides the essential features needed to execute a `flow` in prompt flow.

For those seeking a minimal dependency to execute a flow in serving or cloud run scenarios, installing this package alone will suffice. ...

Sections: Prompt flow core, Introduction

</details>

### pyxlsx

(no summary)

`pip install pyxlsx` · installs (wheel) · licence: MIT License · rank 13566 · last release 2020-07-21 · [PyPI](https://pypi.org/project/pyxlsx/)

<details><summary>README extract</summary>

A package to read/write xlsx worksheet like dictionary, based on openpyxl.

Example:
```python
from pyxlsx import new_xlsx

with new_xlsx(filename) as wb:
    ws = wb.create_sheet('sheet1')
    # some operations

# or
wb = new_xlsx()
ws = wb.creat_sheet('sheet1')  # create a new sheet with name 'sheet1'
# some operations
wb.save(filename)
```

Sections: Introduction, Usage

</details>

### pyramid-session-redis

High performance and actively maintained server-side session framework for Pyramid and Redis.

`pip install pyramid-session-redis` · installs from source (sdist only) · licence: BSD · rank 13579 · last release 2025-10-27 · [PyPI](https://pypi.org/project/pyramid-session-redis/)

<details><summary>README extract</summary>

Features:
`pyramid_session_redis` is a mature, stable and actively maintained Server-Side
Sessions plugin for the Pyramid web framework. ...

Sections: Overview, Key Concepts, Key Differences From pyramid_redis_sessions, Configuration, Initialization, Timeout Notes, Warning: Session Locking and Race Conditions, Feature - Timeout Triggers, Feature - set_redis_ttl_readheavy, Invalid Logging, Uncaught Errors, FAQ, Examples, Further Reading

</details>

### pyjson

Compare the similarities between two JSONs.

`pip install pyjson` · installs (wheel) · licence: MIT License · rank 13618 · last release 2023-09-21 · [PyPI](https://pypi.org/project/pyjson/)

### pymicro-vad

Self-contained voice activity detector

`pip install pymicro-vad` · installs (wheel) · licence: Apache · rank 13619 · last release 2026-06-29 · [PyPI](https://pypi.org/project/pymicro-vad/)

<details><summary>README extract</summary>

Self-contained voice activity detector (VAD) that uses the machine learning architecture from microWakeWord.

Example:
```python
from pymicro_vad import MicroVad

vad = MicroVad()
threshold = 0.5

# Process 10ms chunks of 16-bit mono PCM @16Khz
while audio := get_10ms_of_audio():  # you define this
    assert len(audio) == 160 * 2  # 160 samples
    speech_prob = vad.process_10ms(audio)
    if speech_prob < 0:
        print("Need more audio")
...
```

Sections: microVAD, Usage, Building

</details>

### palmerpenguins

A python package for the palmer penguins dataset

`pip install palmerpenguins` · installs (wheel) · licence: MIT · rank 13620 · last release 2026-02-01 · [PyPI](https://pypi.org/project/palmerpenguins/)

<details><summary>README extract</summary>

The Palmer penguins dataset by Allison Horst, Alison Hill, and Kristen Gorman was first made publicly available as an R package. The goal of the Palmer Penguins dataset is to replace the highly overused Iris dataset for data exploration & visualization.
Using this python package you can easily load the Palmer penguins into your python environment.

Features:
Size measurements, clutch observations, and blood isotope ratios for 344 adult foraging Adelie, Chinstrap, and Gentoo penguins observed on islands in the Palmer Archipelago near Palmer Station, Antarctica. ...

Sections: palmerpenguins, Overview, Examples, Bibliography, See also

</details>

### pyros-genmsg

Standalone Python library for generating ROS message and service data structures for various languages.

`pip install pyros-genmsg` · installs (wheel) · licence: BSD · rank 13623 · last release 2019-04-18 · [PyPI](https://pypi.org/project/pyros-genmsg/)

### pyvat

VAT validation for Python

`pip install pyvat` · installs from source (sdist only) · licence: Apache Software License · rank 13635 · last release 2024-01-25 · [PyPI](https://pypi.org/project/pyvat/)

<details><summary>README extract</summary>

With EU VAT handling rules becoming ever more ridiculous and complicated, businesses within the EU are faced with the complexity of having to validate VAT numbers. `pyvat` was built for Iconfinder's marketplace to handle just this problem. ...

Sections: pyvat -- VAT validation and calculation for Python, Usage

</details>

### prettydiff

Pretty JSON data diffs

`pip install prettydiff` · installs (wheel) · licence: MIT License · rank 13650 · last release 2021-01-22 · [PyPI](https://pypi.org/project/prettydiff/)

<details><summary>README extract</summary>

prettydiff - diff parsed JSON objects and pretty-print it

> `$ python3 -m pip install prettydiff`

- Custom output format example (HTML)

Example:
```python
from prettydiff import print_diff

a = {"a": "hello", "b": True, "c": [1, 3], "d": {"e": {"f": 1}}}
b = {"a": "world", "b": False, "c": [1, 2, 3]}

# to enable colors: $ python3 -m pip install prettydiff[terminal]
print_diff(a, b)
```

Sections: prettydiff, terminal

</details>

### pulumi-archive

A Pulumi package for creating and managing Archive cloud resources.

`pip install pulumi-archive` · installs (wheel) · licence: Apache-2.0 · rank 13681 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pulumi-archive/) · [source](https://github.com/pulumi/pulumi-archive)

<details><summary>README extract</summary>

This provider is mainly used for ease of converting terraform programs to Pulumi.
For standard use in Pulumi programs, please use your programming language's filesystem library.

The Archive resource provider for Pulumi lets you use Archive resources in your cloud programs.
To use this package, please install the Pulumi CLI first.

Sections: Archive Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pnnx

pnnx is an open standard for PyTorch model interoperability.

`pip install pnnx` · installs (wheel) · licence: BSD License · rank 13682 · last release 2026-10-20 · [PyPI](https://pypi.org/project/pnnx/)

<details><summary>README extract</summary>

python wrapper of pnnx, only support python 3.7+ now.

Example:
```python
import torch
import torchvision.models as models
import pnnx

net = models.resnet18(pretrained=True)
x = torch.rand(1, 3, 224, 224)

# You could try disabling checking when torch tracing raises error
# opt_net = pnnx.export(net, "resnet18.pt", x, check_trace=False)
opt_net = pnnx.export(net, "resnet18.pt", x)
```

Sections: pnnx, Prerequisites, Tests, Usage, API Reference

</details>

### pytestify

Automatically convert unittests to pytest

`pip install pytestify` · installs (wheel) · licence: MIT License · rank 13688 · last release 2023-06-04 · [PyPI](https://pypi.org/project/pytestify/)

<details><summary>README extract</summary>

A tool to automatically change unittest to pytest. Similar to
unittest2pytest,
but with a few more features and written using AST and tokenize, rather
than lib2to3.

Big thanks to pyupgrade, which
this project has learned from.

Example:
```python
class TestThing(unittest.TestCase):  # class TestThing:
class TestThing(TestCase, ClassB):   # class TestThing(ClassB):
class ThingTest(unittest.TestCase):  # class TestThing:
class Thing(unittest.TestCase):      # class TestThing:
```

Sections: pytestify, Usage, Implemented features, Test class names, Setup / teardowns, Asserts, Multi-line asserts, camelCase to snake_case, assertCountEqual, Exceptions, Skipping / Expecting failure

</details>

### pyxdia

Extract useful program information from PDB files

`pip install pyxdia` · installs (wheel) · licence: not stated · rank 13696 · last release 2026-06-16 · [PyPI](https://pypi.org/project/pyxdia/)

<details><summary>README extract</summary>

pyxdia is a Python library for extracting useful program information from a PDB file. pyxdia runs on Windows, macOS, Linux, and other platforms.

pyxdia depends on xdia, a native Windows executable. For cross-platform support, a thin loader and compatibility layer (xdialdr) and emulator (Blink) are used to run xdia. ...

Example:
```python
In [1]: from pyxdia import PDB

In [2]: pdb = PDB("./hello-wdm.pdb")

In [3]: pdb.globals[0]
Out[3]:
{'addressOffset': 48,
 'addressSection': 1,
 'name': '_guard_dispatch_icall_nop',
 'relativeVirtualAddress': 4144,
 'symTag': 'Function',
 'undecoratedName': '_guard_dispatch_icall_nop'}
```

Sections: pyxdia, Dependencies, Usage

</details>

### pytoshop

A Python-based library to write Photoshop PSD files

`pip install pytoshop` · installs from source (sdist only) · licence: BSD License · rank 13701 · last release 2018-11-30 · [PyPI](https://pypi.org/project/pytoshop/)

<details><summary>README extract</summary>

A Python-based library to read and write Photoshop PSD and PSB files.

Based on the specification from Adobe,
but also with the help of the psd-tools source code.

* Free software: BSD license

Features:
- Parsing of the most important tags. This is not complete, but the
 infrastructure is in place to add support for more quite easily.

- Loading of complex nested layer structures, and the ability to edit
 them and write them back out.

Sections: pytoshop, Features, 0.4.1 (2017-06-05), 0.4.0 (2017-05-12), 0.3.0 (2017-01-09)

</details>

### pipreqs-fivetran

Pip requirements.txt generator based on imports in project

`pip install pipreqs-fivetran` · installs (wheel) · licence: Apache Software License · rank 13721 · last release 2026-02-02 · [PyPI](https://pypi.org/project/pipreqs-fivetran/)

<details><summary>README extract</summary>

Features:
- `pip freeze` only saves the packages that are installed with `pip install` in your environment.
- `pip freeze` saves all packages in the environment including those that you don't use in your current project (if you don't have `virtualenv`). ...

Sections: Usage, Example, Why not pip freeze?

</details>

### python-bcb

Interface Python para APIs de dados abertos do Banco Central do Brasil.

`pip install python-bcb` · installs (wheel) · licence: not stated · rank 13726 · last release 2026-10-23 · [PyPI](https://pypi.org/project/python-bcb/)

<details><summary>README extract</summary>

python-bcb é uma interface em Python estruturada para obter informações
da API de dados abertos do Banco Central do Brasil.

O projeto de Dados Abertos do Banco Central do Brasil
disponibiliza diversas APIs provendo acesso direto a dados de: ...

Example:
```python
from bcb import sgs

# Buscar taxa Selic (código 1)
df = sgs.get(1, start="2023-01-01", end="2024-12-31")
```

Sections: python-bcb, Instalação, APIs, SGS - Sistema Gerenciador de Séries Temporais, Conversor de Moedas, OData - APIs Estruturadas, Qual Módulo Devo Usar?, Início Rápido, Séries Temporais com SGS, Taxas de Câmbio com Currency, Expectativas de Mercado com OData, Perguntas Frequentes, P: Qual é a diferença entre dados de moedas do SGS e PTAX?, P: Quão longe no tempo os dados históricos vão?

</details>

### pep562

Backport of PEP 562.

`pip install pep562` · installs (wheel) · licence: MIT License · rank 13738 · last release 2021-05-21 · [PyPI](https://pypi.org/project/pep562/)

<details><summary>README extract</summary>

[][donate-link]
[][discord-link]
[][github-ci-link]
[][codecov-link]
[][pypi-link]
[][pypi-link]

Features:
A backport of PEP 562. Allows controlling a module's `dir` and `getattr`. Useful for deprecating attributes.
Works for Python 2.7+. And while it works on Python 3.7, it is recommended to use the official Python 3.7 implementation
where applicable. ...

Example:
```python
from pep562 import pep562
import warnings

version = (1, 0, 0)
all = ("version",)
deprecated = {
    "version": ("version", version)
}

PY37 = sys.version_info >= (3, 7)

def getattr(name):
    """Get attribute."""

    deprecated = deprecated.get(name)
    if deprecated:
        stacklevel = 3 if PY37 else 4
        warnings.warn(
...
```

Sections: PEP 562, Overview, Vendoring, Usage

</details>

### parakeet-mlx

An implementation of the Nvidia's Parakeet models for Apple Silicon using MLX.

`pip install parakeet-mlx` · installs (wheel) · licence: Apache-2.0 · rank 13741 · last release 2026-11-04 · [PyPI](https://pypi.org/project/parakeet-mlx/) · [source](https://github.com/senstella/parakeet-mlx.git)

<details><summary>README extract</summary>

An implementation of the Parakeet models - Nvidia's ASR(Automatic Speech Recognition) models - for Apple Silicon using MLX.

Example:
```python
from parakeet_mlx import from_pretrained

model = from_pretrained("mlx-community/parakeet-tdt-0.6b-v3")

result = model.transcribe("audio_file.wav")

print(result.text)
```

Sections: Parakeet MLX, CLI Quick Start, Arguments, Options, Examples, Python API Quick Start, from_pretrained, Timestamp Result, Boosting, Streaming Transcription, Streaming Parameters, Low-Level API, Todo

</details>

### pytorch_revgrad

A pytorch module (and function) to reverse gradients.

`pip install pytorch_revgrad` · installs (wheel) · licence: MIT License · rank 13750 · last release 2021-01-09 · [PyPI](https://pypi.org/project/pytorch_revgrad/)

<details><summary>README extract</summary>

This package implements a gradient reversal layer for pytorch modules.

Example:
```python
import torch

from pytorch_revgrad import RevGrad

model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.Linear(5, 2),
    RevGrad()
)
```

Sections: `pytorch-revgrad`, Example usage

</details>

### pyarrowfs-adlgen2

Use pyarrow with Azure Data Lake gen2

`pip install pyarrowfs-adlgen2` · installs (wheel) · licence: MIT License · rank 13759 · last release 2024-06-27 · [PyPI](https://pypi.org/project/pyarrowfs-adlgen2/)

<details><summary>README extract</summary>

pyarrowfs-adlgen2 is an implementation of a pyarrow filesystem for Azure Data Lake Gen2.

It allows you to use pyarrow and pandas to read parquet datasets directly from Azure without
the need to copy files to local storage first. ...

Example:
```python
import azure.identity
import pandas as pd
import pyarrow.fs
import pyarrowfs_adlgen2

handler = pyarrowfs_adlgen2.AccountHandler.from_account_name(
    'YOUR_ACCOUNT_NAME', azure.identity.DefaultAzureCredential())
fs = pyarrow.fs.PyFileSystem(handler)
df = pd.read_parquet('container/dataset.parq', filesystem=fs)
```

Sections: pyarrowfs-adlgen2, Reading datasets, Configuring timeouts, Writing datasets, Accessing only a single container/file-system, Set http headers for files for pyarrow >= 5, Running tests, Performance

</details>

### pydssp

A simplified implementation of DSSP algorithm for PyTorch and NumPy

`pip install pydssp` · installs (wheel) · licence: MIT License · rank 13761 · last release 2025-02-24 · [PyPI](https://pypi.org/project/pydssp/)

<details><summary>README extract</summary>

A simplified implementation of DSSP algorithm for PyTorch and NumPy

DSSP (Dictionary of Secondary Structure of Protein) is a popular algorithm for assigning secondary structure of protein backbone structure. ...

Example:
```python
# Import
import torch
import pydssp

# Sample coordinates
batch, length, atoms, xyz = 10, 100, 4, 3
# atoms should be 4 (N, CA, C, O) or 5 (N, CA, C, O, H)
coord = torch.randn([batch, length, atom, xyz]) # batch-dim is optional
```

Sections: PyDSSP, What's this?, General Info, How to use, To use pydssp script, To use as python module, Import & test coordinates, To get hydrogen-bond matrix: ```pydssp.get_hbond_map()```, Differences from the original DSSP, Reference

</details>

### pocketbase

PocketBase SDK for python.

`pip install pocketbase` · installs (wheel) · licence: MIT · rank 13765 · last release 2026-05-20 · [PyPI](https://pypi.org/project/pocketbase/)

<details><summary>README extract</summary>

Python client SDK for the PocketBase backend.

This is in early development, and at first is just a translation of the javascript lib using HTTPX.

Example:
```python
from pocketbase import PocketBase  # Client also works the same
from pocketbase.client import FileUpload

client = PocketBase('

# authenticate as regular user
user_data = client.collection("users").auth_with_password(
    "user@example.com", "0123456789")
# check if user token is valid
user_data.is_valid

# or as admin
...
```

Sections: PocketBase Python SDK, Usage, Tests

</details>

### pysimstring

Easy to install clone of simstring

`pip install pysimstring` · installs from source (sdist only) · licence: not stated · rank 13767 · last release 2025-04-06 · [PyPI](https://pypi.org/project/pysimstring/)

<details><summary>README extract</summary>

Orginal version by chokkan and QuickUMLS.

This version removes the libiconv dependency
which required a conda installation before installing the simstring package on Windows.

</details>

### parsedmarc

A Python package and CLI for parsing aggregate, failure, and SMTP TLS DMARC reports

`pip install parsedmarc` · installs (wheel) · licence: Apache-2.0 · rank 13785 · last release 2026-11-01 · [PyPI](https://pypi.org/project/parsedmarc/)

<details><summary>README extract</summary>

`parsedmarc` is a Python module and CLI utility for parsing DMARC
reports. When used with Elasticsearch and Kibana (or Splunk), or with
OpenSearch and Grafana, it works as a self-hosted open-source
alternative to commercial DMARC report processing services such as
Agari Brand Protection, Dmarcian, OnDMARC, ProofPoint Email Fraud
Defense, and ...

Features:
- Parses aggregate/rua DMARC reports: the legacy draft and 1.0 schemas
 (RFC 7489) and the new RFC 9990 schema for the final DMARC standard
 (RFC 9989)
- Parses failure/ruf DMARC reports (RFC 6591 and RFC 9991; formerly called
 forensic reports) ...

Sections: parsedmarc, Features, Python Compatibility

</details>

### public

replace __all__ with @public.add decorator

`pip install public` · installs from source (sdist only) · licence: Public Domain · rank 13835 · last release 2020-12-03 · [PyPI](https://pypi.org/project/public/)

<details><summary>README extract</summary>

Features:
+ replace `all` with `@public.add` decorator

before

after

Example:
```python
>>> import public
>>> @public.add
    def func(): pass

>>> @public.add
    class Cls: pass

>>> all
['Cls','func']

>>> public.add("name")
>>> public.add(*["name1","name2"])

>>> all
['Cls','func','name','name1','name2']
```

Sections: Features, Examples, Links

</details>

### pylife

General Fatigue library

`pip install pylife` · installs (wheel) · licence: Apache Software License · rank 13840 · last release 2026-04-28 · [PyPI](https://pypi.org/project/pylife/) · [docs](https://pylife.readthedocs.io) · [source](https://github.com/boschresearch/pylife/)

<details><summary>README extract</summary>

pyLife is an Open Source Python library for state of the art algorithms used in
lifetime assessment of mechanical components subjected to fatigue.

This library was originally compiled at Bosch
Research to collect algorithms needed by
different in house software projects, that deal with lifetime prediction and
material fatigue on a component ...

Sections: pyLife – a general library for fatigue and reliability, Purpose of the project

</details>

### pulumi-mongodbatlas

A Pulumi package for creating and managing mongodbatlas cloud resources.

`pip install pulumi-mongodbatlas` · installs (wheel) · licence: Apache-2.0 · rank 13863 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pulumi-mongodbatlas/) · [source](https://github.com/pulumi/pulumi-mongodbatlas)

<details><summary>README extract</summary>

The MongoDB Atlas resource provider for Pulumi lets you interact with MongoDB Atlas in your infrastructure
programs. To use this package, please install the Pulumi CLI first.

Sections: MongoDB Atlas provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### postal-codes-tools

Library that help working with different postal codes.

`pip install postal-codes-tools` · installs (wheel) · licence: MIT · rank 13890 · last release 2023-01-10 · [PyPI](https://pypi.org/project/postal-codes-tools/)

<details><summary>README extract</summary>

Library that helps working with different postal codes. Purpose of this library is to validate string
if it matches the postal code format.

Postal code format checking is based on European Central Bank - List of postal code formatting rules and regular
expressions per country
spreadsheet version 1.1. ...

Sections: Postal Codes Tools, Usage

</details>

### pulumiverse-sentry

A Pulumi package for creating and managing Sentry resources.

`pip install pulumiverse-sentry` · installs (wheel) · licence: Apache-2.0 · rank 13899 · last release 2024-11-15 · [PyPI](https://pypi.org/project/pulumiverse-sentry/) · [source](https://github.com/pulumiverse/pulumi-sentry)

<details><summary>README extract</summary>

This plugin requires pulumi cli v3.35.3 or later

The Sentry Resource Provider lets you manage Sentry resources.

It is based on the sentry terraform provider

Sections: Sentry Resource Provider, Node.js (JavaScript/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### parametrize-from-file

Parametrize test functions with values read from config files.

`pip install parametrize-from-file` · installs (wheel) · licence: MIT License · rank 13924 · last release 2026-05-01 · [PyPI](https://pypi.org/project/parametrize-from-file/) · [docs](https://parametrize-from-file.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Parametrize From File is a library for reading unit test parameters from config
files. It works with the pytest framework. Below is the basic workflow that
this package enables:

- Write test cases in a JSON, YAML, TOML, or NestedText file:

 .. code-block:: yaml

 # test_camelot.yml
 test_str_find:
 - str: sir lancelot
 sub: lance
 loc: 4 ...

</details>

### python-magnumclient

Client library for Magnum API

`pip install python-magnumclient` · installs (wheel) · licence: Apache-2.0 · rank 13928 · last release 2026-08-28 · [PyPI](https://pypi.org/project/python-magnumclient/) · [source](https://opendev.org/openstack/python-magnumclient)

<details><summary>README extract</summary>

This is a client library for Magnum built on the Magnum API. It
provides a Python API (the `magnumclient` module) and a command-line
tool (`magnum`).

Development takes place via the usual OpenStack processes as outlined
in the developer guide. ...

</details>

### pytest-ignore-test-results

A pytest plugin to ignore test results.

`pip install pytest-ignore-test-results` · installs (wheel) · licence: Apache Software License · rank 13929 · last release 2025-02-03 · [PyPI](https://pypi.org/project/pytest-ignore-test-results/) · [source](https://github.com/espressif/pytest-ignore-test-results.git)

<details><summary>README extract</summary>

A pytest plugin that enables selective test result ignoring while maintaining test execution.

Features:
- Ignore specific test case results using exact names or patterns
- Load ignore patterns from files
- Custom exit codes for different failure scenarios
- Support for child test cases
- Option to ignore "no tests collected" errors

Example:
```python
def pytest_custom_test_case_name(item):
    """
    Args:
        item: pytest item

    Returns:
        str: Custom name for the test case
    """
    return f"custom_name::{item.name}"
```

Sections: pytest-ignore-test-results, Features, Usage, Ignore Test Results by Case Name or Pattern, Control Exit Codes, Custom Test Case Names

</details>

### python-mollusc

Python clamd client (fork of python-clamd)

`pip install python-mollusc` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 13931 · last release 2021-06-17 · [PyPI](https://pypi.org/project/python-mollusc/)

_README extract left out: share-alike licence._

### pystardog

Python client for Stardog Platform Endpoints and Stardog Cloud

`pip install pystardog` · installs (wheel) · licence: Apache Software License · rank 13933 · last release 2026-08-31 · [PyPI](https://pypi.org/project/pystardog/) · [source](https://github.com/stardog-union/pystardog)

<details><summary>README extract</summary>

Python client for Stardog servers and Stardog Cloud.

Requirements: Python 3.9+

Sections: pystardog, Quick Start, Documentation, Interactive Tutorial, Voicebox Demo

</details>

### pyyml

Use python in yaml

`pip install pyyml` · installs (wheel) · licence: MIT · rank 13942 · last release 2019-04-09 · [PyPI](https://pypi.org/project/pyyml/)

<details><summary>README extract</summary>

Use python in yaml

在python中使用：
在yaml中 `${...}` 中的内容将会被python执行：

yaml内容
实际解析内容
通过在文件开头第一行注释来导入所需的包：

通过 [包名]:[别名] 取别名导入包

`'os.path:path' 等同于 python 中的 from os import path`

例如yaml文件内容

Example:
```python
from pyyml import load

with open('conf.yml') as f:
    raw_conf = f.read()
config = load(raw_conf)
print(config)
```

Sections: pyyml, 基本使用

</details>

### pins

Publish data sets, models, and other python objects, making it easy to share them across projects and with your colleagues.

`pip install pins` · installs (wheel) · licence: MIT License · rank 13949 · last release 2026-10-13 · [PyPI](https://pypi.org/project/pins/) · [docs](https://rstudio.github.io/pins-python)

<details><summary>README extract</summary>

The pins package publishes data, models, and other Python objects,
making it easy to share them across projects and with your colleagues.
You can pin objects to a variety of pin *boards*, including folders (to
share on a networked drive or with services like DropBox), Posit
Connect, Amazon S3, and Google Cloud Storage. ...

Example:
```python
import pins
from pins.data import mtcars

board = pins.board_temp()
```

Sections: pins, Usage

</details>

### PyRuSH

PyRuSH is the python implementation of RuSH (Rule-based sentence Segmenter using Hashing), which is originally developed using Java. RuSH is an efficient, reliable, and easy adaptable rule-based sentence segmentation solution. It is specifically designed to handle the telegraphic written text in clinical note. It leverages a nested hash table to execute simultaneous rule processing, which reduces the impact of the rule-base growth on execution time and eliminates the effect of rule order on accuracy.

`pip install PyRuSH` · installs from source (sdist only) · licence: MIT · rank 13974 · last release 2026-03-28 · [PyPI](https://pypi.org/project/PyRuSH/) · [source](https://github.com/jianlins/PyRuSH)

<details><summary>README extract</summary>

PyRuSH is the python implementation of RuSH (Ru le-based sentence S egmenter using H ashing), which is originally developed using Java. RuSH is an efficient, reliable, and easy adaptable rule-based sentence segmentation solution. It is specifically designed to handle the telegraphic written text in clinical note. ...

Sections: PyRuSH, How to use, Spacy Componentized PyRuSH, A Colab Notebook Demo

</details>

### praatio

A library for working with praat, textgrids, time aligned audio transcripts, and audio files.

`pip install praatio` · installs (wheel) · licence: not stated · rank 13990 · last release 2026-01-16 · [PyPI](https://pypi.org/project/praatio/)

<details><summary>README extract</summary>

*Questions? Comments? Feedback? *

A library for working with praat, time aligned audio transcripts, and audio files *that comes with batteries included*.

Praat uses a file format called textgrids, which are time aligned speech transcripts. ...

Example:
```python
from praatio import textgrid
tg = textgrid.openTextgrid(r"C:\Users\tim\Documents\transcript.TextGrid", False)
```

Sections: praatIO, Documentation, Tutorials, Requirements, Upgrading, Usage, Common Use Cases, Output types, Citing praatIO

</details>

### pyFUME

A Python package for fuzzy model estimation

`pip install pyFUME` · installs (wheel) · licence: GNU General Public License (GPL) · rank 13994 · last release 2024-05-03 · [PyPI](https://pypi.org/project/pyFUME/)

_README extract left out: share-alike licence._

### pycsep

Python tools from the Collaboratory for the Study of Earthquake Predictability

`pip install pycsep` · installs (wheel) · licence: not stated · rank 13998 · last release 2026-01-30 · [PyPI](https://pypi.org/project/pycsep/)

<details><summary>README extract</summary>

The pyCSEP Toolkit helps earthquake forecast model developers evaluate their forecasts with the goal of understanding
earthquake predictability.

pyCSEP should:
1. Help modelers become familiar with formats, procedures, and evaluations used in CSEP Testing Centers.
2. Provide vetted software for model developers to use in their research.
3. ...

Sections: Description, Usage

</details>

### poseidon-py

Python implementation of Poseidon hash

`pip install poseidon-py` · installs (wheel) · licence: not stated · rank 14014 · last release 2026-03-26 · [PyPI](https://pypi.org/project/poseidon-py/)

<details><summary>README extract</summary>

Poseidon hash Python library with Hades permutation implemented in C.

Currently, the parameters for poseidon hash are set to define the permutation used in Starknet.

They can be found in *poseidon_params.txt*.


Sections: poseidon-py, Version 0.2.0 (2026-03-26), Version 0.1.5 (2024-08-08), Version 0.1.4 (2024-02-12), Version 0.1.3 (2023-04-27), Version 0.1.2 (2023-04-13), Version 0.1.1 (2023-04-07)

</details>

### pytsk3

Python bindings for the SleuthKit

`pip install pytsk3` · installs (wheel) · licence: Apache-2.0 · rank 14015 · last release 2026-07-15 · [PyPI](https://pypi.org/project/pytsk3/) · [docs](https://raw.githubusercontent.com/py4n6/pytsk/refs/heads/main/README) · [source](https://github.com/py4n6/pytsk)

<details><summary>README extract</summary>

pytsk is a Python binding for the SleuthKit.

This is a Python binding against the libtsk (SleuthKit library). The aim is
to make the binding reflect the TSK API as much as possible in capabilities,
while at the same time having a nice Pythonic OO interface:

4.15.0: ...

</details>

### poetry-multiproject-plugin

A Poetry plugin that makes it possible to use relative package includes.

`pip install poetry-multiproject-plugin` · installs (wheel) · licence: MIT · rank 14016 · last release 2026-09-05 · [PyPI](https://pypi.org/project/poetry-multiproject-plugin/) · [source](https://github.com/davidvujic/poetry-multiproject-plugin)

<details><summary>README extract</summary>

This is a Python `Poetry` plugin, adding the `build-project` and `check-project` commands.

The `build-project` command will make it possible to use relative package includes.
This feature is very useful for monorepos and when sharing code between projects. ...

Example:
```python
from my_package import my_function
```

Sections: Poetry Multiproject Plugin, Use cases, Microservices and apps, A basic building block for the Polylith Architecture, Libraries?, Usage, Available command options, Custom temp path, Usage for libraries, The build output, Default(no flag), Namespace(`--with-top-namespace=my_namespace`)

</details>

### polarion

Polarion client for Python

`pip install polarion` · installs (wheel) · licence: MIT License · rank 14017 · last release 2024-05-23 · [PyPI](https://pypi.org/project/polarion/) · [docs](https://python-polarion.readthedocs.io/)

<details><summary>README extract</summary>

This package allows the user to access many Polarion items like workitems, test run, plans and documents.

Features:
This package can, among others, read, modify and create:
- Workitems
- Test runs from templates
- Plans
- Documents

Work with attachments in workitems and test runs.
Work with custom field in workitems and documents.

Example:
```python
from polarion import polarion
client = polarion.Polarion(' 'user', 'password')
project = client.getProject('Python')
workitem = project.getWorkitem('PYTH-510')
run = project.getTestRun('SWQ-0001')
plan = project.getPlan('00002')
```

Sections: Python-polarion, Feature overview, Getting started, How does it work?, Dependencies, Known issues or missing features

</details>

### pyjokes

One line jokes for programmers (jokes as a service)

`pip install pyjokes` · installs (wheel) · licence: BSD License · rank 14023 · last release 2024-08-10 · [PyPI](https://pypi.org/project/pyjokes/)

<details><summary>README extract</summary>

One line jokes for programmers (jokes as a service)

Example:
```python
>>> import pyjokes
>>> print(pyjokes.get_joke())
Why do programmers confuse Halloween with Christmas? Because OCT 31 == DEC 25.
```

Sections: pyjokes, Usage, Command line, Python, Website and documentation, The story of pyjokes, PyJokes logo

</details>

### pydevicetree

A library for parsing Devicetree Source v1

`pip install pydevicetree` · installs (wheel) · licence: Apache Software License · rank 14039 · last release 2023-07-21 · [PyPI](https://pypi.org/project/pydevicetree/)

<details><summary>README extract</summary>

This is a Python 3 library for parsing, querying, and modifying Devicetree Source v1 files as
described in the Devicetree Specification v0.2.

Example:
```python
>>> from pydevicetree import Devicetree
>>> tree = Devicetree.parseFile("design.dts")
>>> tree
<Devicetree my,design>
```

Sections: pydevicetree, Tutorial, The Devicetree, Parsing the Tree, Querying the Tree, By `compatible` string, By path, Getting `Node` properties, Getting `chosen` properties, Converting back to Devicetree

</details>

### PypeR

A python interface to R lanugage

`pip install PypeR` · installs from source (sdist only) · licence: GPL · rank 14045 · last release 2014-03-26 · [PyPI](https://pypi.org/project/PypeR/)

_README extract left out: share-alike licence._

### phrase-api

Phrase Strings API Reference

`pip install phrase-api` · installs (wheel) · licence: MIT · rank 14064 · last release 2026-10-23 · [PyPI](https://pypi.org/project/phrase-api/)

<details><summary>README extract</summary>

Phrase Strings is a translation management platform for software projects. You can collaborate on language file translation with your team or order translations through our platform. ...

</details>

### play-scraper

Google Play Store application scraper

`pip install play-scraper` · installs (wheel) · licence: MIT License · rank 14074 · last release 2019-09-15 · [PyPI](https://pypi.org/project/play-scraper/)

<details><summary>README extract</summary>

Scrapes and parses application data from the Google Play Store.

Example:
```python
>>> import play_scraper
>>> print(play_scraper.details('com.android.chrome'))
{
    'app_id': 'com.android.chrome',
    'category': ['COMMUNICATION'],
    'content_rating': ['Everyone'],
    'current_version': 'Varies with device',
...
```

Sections: Play Store Scraper, Usage, details, collection, suggestions, search, similar, categories, Tests

</details>

### pyinstxtractor-ng

PyInstaller Extractor Next Generation

`pip install pyinstxtractor-ng` · installs (wheel) · licence: GPL-3.0-only · rank 14085 · last release 2026-07-03 · [PyPI](https://pypi.org/project/pyinstxtractor-ng/)

_README extract left out: share-alike licence._

### pydoll-python

Pydoll is a library for automating chromium-based browsers without a WebDriver, offering realistic interactions.

`pip install pydoll-python` · installs (wheel) · licence: not stated · rank 14089 · last release 2026-09-29 · [PyPI](https://pypi.org/project/pydoll-python/)

<details><summary>README extract</summary>

Browser automation for Python over raw CDP.
No WebDriver, no driver process, sync or async, and your Playwright scripts run on it with one import.

 = 3.10">

 Documentation ·
 Quick start ·
 Playwright ·
 Features ·
 Support

> [!NOTE]
> Pydoll 3 is here. ...

Features:
- Nothing to patch: a direct CDP connection over WebSocket. No driver binary, no `navigator.webdriver` flag, no version-matching, and no stealth fork to keep up to date. ...

Example:
```python
import asyncio

from pydoll import Chrome, Key

async def google_search(query: str):
    async with Chrome() as browser:
        tab = await browser.start()
        await browser.set_window_maximized()
        await tab.go_to('

        search_box = await tab.find(tag_name='textarea', name='q')
...
```

...

</details>

### pytest-playwright-visual

A pytest fixture for visual testing with Playwright

`pip install pytest-playwright-visual` · installs (wheel) · licence: Apache Software License · rank 14093 · last release 2022-04-28 · [PyPI](https://pypi.org/project/pytest-playwright-visual/)

<details><summary>README extract</summary>

Example:
```python
def test_myapp(page, assert_snapshot):
    page.goto("
    assert_snapshot(page.screenshot())
```

Sections: Main Features, Usage, Folder Structure Example, API

</details>

### pyvsc

pyvsc (Verification Stimulus and Coverage) is a Python package for generating randomized stimulus and defining and collecting functional coverage.

`pip install pyvsc` · installs (wheel) · licence: Apache-2.0 · rank 14127 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyvsc/) · [docs](https://dvkit.org/fvutils/pyvsc/) · [source](https://github.com/fvutils/pyvsc)

<details><summary>README extract</summary>

Python package providing a library for Verification Stimulus and Coverage

Documentation: dvkit.org/fvutils/pyvsc

Join the chat on Gitter

</details>

### praisonaiagents

Open-source Python AI agent framework that runs on your own computers, even fully offline.

`pip install praisonaiagents` · installs (wheel) · licence: not stated · rank 14130 · last release 2026-11-05 · [PyPI](https://pypi.org/project/praisonaiagents/)

<details><summary>README extract</summary>

Private AI that earns trust one task at a time.

PraisonAI runs AI agents on your own computers, even fully offline, so private data never has to leave the building.

- For highly regulated teams (early access): each task moves to your own AI only after it passes a test. ...

Features:
- Agents and multi-agent teams: Agents · Handoffs · Workflows
- Memory: Memory · Knowledge and RAG · Sessions
- Tools and MCP: Tools · MCP
- Guardrails and approval: Guardrails · Human approval · Policy engine ...

Example:
```python
from praisonaiagents import Agent

agent = Agent(instructions="You are a helpful assistant.")
print(agent.start("In two sentences, why do some companies keep their data on their own computers?"))
```

...

</details>

### PyFastNER

PyFastNER is the python implementation of FastNER, which is orginally developed using Java. It uses hash function to process multiple rules at the same time. Similar to FastNER, PyFastNER supports token-based rules (FastNER--under developing) and character-based rules (FastCNER). It is licensed under the MIT License.

`pip install PyFastNER` · installs (wheel) · licence: MIT License · rank 14163 · last release 2023-12-13 · [PyPI](https://pypi.org/project/PyFastNER/) · [source](https://github.com/jianlins/PyFastNER)

<details><summary>README extract</summary>

PyFastNER is the python implementation of FastNER, which is orginally developed
using Java. It uses hash function to process multiple rules at the same time. Similar to FastNER, PyFastNER
supports token-based rules (FastNER--under developing) and character-based rules
 (FastCNER). It is licensed under the
 Apache License, Version 2.0.

Example:
```python
from PyFastNER import FastCNER
# initiate fastner using external rule file
fastner = FastCNER('conf/crule_test.tsv')
# process an input string
res = fastner.processString('Pt came with fever, T 102.0F.')
# display processed results
for type in res.keys():
    for span in res[type]:
        print(span)
```

Sections: PyFastNER, Examples

</details>

### pysen

Python linting made easy. Also a casual yet honorific way to address individuals who have entered an organization prior to you.

`pip install pysen` · installs (wheel) · licence: MIT · rank 14176 · last release 2026-07-21 · [PyPI](https://pypi.org/project/pysen/) · [source](https://github.com/pfnet/pysen.git)

<details><summary>README extract</summary>

Example:
```python
:cex system("pysen run_files lint --error-format gnu ".expand('%:p'))
```

Sections: pysen, PyPI, Quickstart: Set up linters using pysen, Frequently Asked Questions, What is pysen?, What isn't pysen?, How it works: Settings file directory, Tips: IDE / Text editor integration, vim, Emacs, VSCode, Configure pysen, Configuration model, Create a plugin to customize pysen

</details>

### pymitter

Python port of the extended Node.js EventEmitter 2 approach providing namespaces, wildcards and TTL.

`pip install pymitter` · installs (wheel) · licence: BSD-3-Clause · rank 14182 · last release 2025-07-11 · [PyPI](https://pypi.org/project/pymitter/) · [docs](https://pymitter.readthedocs.io) · [source](https://github.com/riga/pymitter.git)

<details><summary>README extract</summary>

Python port of the extended Node.js EventEmitter 2 approach of providing namespaces, wildcards and TTL.

Original source hosted at GitHub.

Features:
- Namespaces with wildcards
- Times to listen (TTL)
- Usage via decorators or callbacks
- Coroutine support
- Lightweight implementation, good performance

Example:
```python
from pymitter import EventEmitter

ee = EventEmitter()

# decorator usage
@ee.on("my_event")
def handler1(arg):
    print("handler1 called with", arg)

# callback usage
def handler2(arg):
    print("handler2 called with", arg)

ee.on("my_other_event", handler2)

# support for coroutine functions
@ee.on("my_third_event")
async def handler3(arg):
...
```

Sections: Features, Examples, Basic usage, Coroutines, TTL (times to listen), Wildcards, API

</details>

### pycpfcnpj

Python module for brazilian register numbers for persons (CPF) and companies (CNPJ).

`pip install pycpfcnpj` · installs (wheel) · licence: MIT · rank 14185 · last release 2026-01-25 · [PyPI](https://pypi.org/project/pycpfcnpj/)

<details><summary>README extract</summary>

Description

Python module for brazilian register numbers for persons (CPF) and companies (CNPJ). If want this validation in your web application, please check my tiny web component that does exactly that. ;) ...

Example:
```python
from pycpfcnpj import cpfcnpj
cpf_number = '11144477735'
masked_cpf_number = '111.444.777-35'
cnpj_number = '11444777000161'
masked_cnpj_number = '11.444.777/0001-61'
alphanumeric_cnpj = '12ABC34501DE35'

print(cpfcnpj.validate(cpf_number))
print(cpfcnpj.validate(masked_cpf_number))
print(cpfcnpj.validate(cnpj_number))
...
```

Sections: Pycpfcnpj, Related projects, Quick Start, Como instalar, Projetos relacionados, Como usar

</details>

### pydantic-ai-absurd

Durable execution of Pydantic AI agents on Postgres via Absurd.

`pip install pydantic-ai-absurd` · installs (wheel) · licence: MIT · rank 14191 · last release 2026-08-20 · [PyPI](https://pypi.org/project/pydantic-ai-absurd/)

<details><summary>README extract</summary>

Durable execution for Pydantic AI agents, on Postgres alone.

Agents run for a while, a model call, a tool call, another model call. When the worker dies in the middle of that, the run is usually lost: you restart from zero and pay for every token again.

Pydantic AI Absurd fixes that. ...

Example:
```python
import asyncio

from absurd_sdk import AsyncAbsurd
from pydantic_ai import Agent
from pydantic_ai_absurd import AbsurdDurability

absurd = AsyncAbsurd("postgresql://localhost/absurd", queue_name="agents")
agent = Agent("openai:gpt-5.2", name="analyst", capabilities=[AbsurdDurability()])

@absurd.register_task(name="analyse")
...
```

Sections: Pydantic AI Absurd, Example, Documentation

</details>

### pr-agent

PR-Agent aims to help efficiently review and handle pull requests, by providing AI feedback and suggestions.

`pip install pr-agent` · installs (wheel) · licence: not stated · rank 14201 · last release 2026-10-25 · [PyPI](https://pypi.org/project/pr-agent/) · [docs](https://docs.pr-agent.ai/) · [source](https://github.com/the-pr-agent/pr-agent)

<details><summary>README extract</summary>

The Original Open-Source PR Reviewer

 This repository contains the open-source PR Agent Project.
 It is not the Qodo offering for open-source projects.

PR-Agent is an open-source, AI-powered code review agent and a community-maintained legacy project of Qodo. ...

Sections: Getting Started, 🚀 Quick Start for PR-Agent, 1. GitHub Action (Recommended), 3. Other Platforms, News and Updates, Why Use PR-Agent?, Features, See It in Action, /describe, /review, /improve, Usage Examples, How It Works, Data Privacy

</details>

### pyaga8

Python package for calculating gas properties using the AGA8 equations GERG-2008 and DETAIL

`pip install pyaga8` · installs (wheel) · licence: not stated · rank 14209 · last release 2026-06-24 · [PyPI](https://pypi.org/project/pyaga8/)

<details><summary>README extract</summary>

Python bindings for the AGA8 GERG-2008 and DETAIL gas property equations, built on the Rust `aga8` port of NIST's AGA8 code.

GitHub:

`pyaga8` is a low-level Python interface to the AGA8 calculations. It exposes the underlying GERG-2008 and DETAIL state objects and methods directly, with Rust used for performance via `pyo3`. ...

Example:
```python
import pyaga8

detail = pyaga8.Detail()
comp = pyaga8.Composition()
comp.methane = 0.9
comp.nitrogen = 0.1

detail.set_composition(comp)
detail.temperature = 400.0
detail.pressure = 50_000.0
detail.calc_density()

print(detail.d)
```

Sections: pyaga8, Description, Minimal usage, Error handling

</details>

### pytelegraf

Telegraf client

`pip install pytelegraf` · installs from source (sdist only) · licence: MIT License · rank 14237 · last release 2018-04-13 · [PyPI](https://pypi.org/project/pytelegraf/)

### pkcs7

extension class for argparse with json configuration

`pip install pkcs7` · installs from source (sdist only) · licence: MIT · rank 14254 · last release 2017-03-23 · [PyPI](https://pypi.org/project/pkcs7/)

### pysr

Simple and efficient symbolic regression

`pip install pysr` · installs (wheel) · licence: Apache Software License · rank 14257 · last release 2026-10-19 · [PyPI](https://pypi.org/project/pysr/)

<details><summary>README extract</summary>

Symbolic Regression in Python and Julia
Docs × Examples × API × Forum × Agents

If you find PySR useful, please cite the paper arXiv:2305.01582.
If you've finished a project with PySR, please submit a PR to showcase your work on the research showcase page!

Contents:

- Why PySR?
- Installation
- Quickstart
- → Documentation
- Contributors

Features:
PySR is an open-source tool for *Symbolic Regression*: a machine learning
task where the goal is to find an interpretable symbolic expression that optimizes some objective. ...

Example:
```python
import numpy as np

X = 2 * np.random.randn(100, 5)
y = 2.5382 * np.cos(X[:, 3]) + X[:, 0] ** 2 - 0.5
```

Sections: PySR, Why PySR?, AI Agent Skill, Docker, Apptainer, Troubleshooting, Quickstart, Detailed Example

</details>

### pylxd

Python library for interacting with the LXD REST API

`pip install pylxd` · installs (wheel) · licence: Apache-2.0 · rank 14266 · last release 2026-08-18 · [PyPI](https://pypi.org/project/pylxd/) · [docs](https://pylxd.readthedocs.io/en/latest/) · [source](https://github.com/canonical/pylxd)

<details><summary>README extract</summary>

A Python library for interacting with the LXD REST API.

Sections: pylxd, Bug reports

</details>

### probmetrics

Probabilistic metrics and calibration methods

`pip install probmetrics` · installs (wheel) · licence: Apache-2.0 · rank 14273 · last release 2026-05-27 · [PyPI](https://pypi.org/project/probmetrics/) · [docs](https://github.com/dholzmueller/probmetrics#readme) · [source](https://github.com/dholzmueller/probmetrics)

<details><summary>README extract</summary>

This package (PyTorch-based) currently contains

 - a fast and accurate temperature scaling implementation described in [1]
 - an implementation of structured matrix scaling (SMS), a regularized version of matrix scaling introduced in [2]
 - implementations for all the post-hoc calibration methods in the CalArena benchmark [4] ...

Example:
```python
import numpy as np

probas = np.asarray([[0.1, 0.9]])  # shape = (n_samples, n_classes)
labels = np.asarray([1])  # shape = (n_samples,)

calib.fit(probas, labels)
calibrated_probas = calib.predict_proba(probas) # shape = (n_samples, n_classes)
```

...

</details>

### pure25519

pure-python curve25519/ed25519 routines

`pip install pure25519` · installs from source (sdist only) · licence: MIT · rank 14293 · last release 2018-01-17 · [PyPI](https://pypi.org/project/pure25519/)

### pyone

Python Bindings for OpenNebula XML-RPC API

`pip install pyone` · installs (wheel) · licence: Apache-2.0 · rank 14294 · last release 2026-07-13 · [PyPI](https://pypi.org/project/pyone/)

<details><summary>README extract</summary>

Apache License
Version 2.0, January 2004

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction,
and distribution as defined by Sections 1 through 9 of this document. ...

</details>

### pulumi-okta

A Pulumi package for creating and managing okta resources.

`pip install pulumi-okta` · installs (wheel) · licence: Apache-2.0 · rank 14312 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pulumi-okta/) · [source](https://github.com/pulumi/pulumi-okta)

<details><summary>README extract</summary>

The Okta resource provider for Pulumi lets you manage Okta resources in your cloud programs. To use
this package, please install the Pulumi CLI first.

Sections: Okta Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pypgstac

Schema, functions and a python library for storing and accessing STAC collections and items in PostgreSQL

`pip install pypgstac` · installs (wheel) · licence: MIT · rank 14324 · last release 2026-10-01 · [PyPI](https://pypi.org/project/pypgstac/) · [docs](https://stac-utils.github.io/pgstac/) · [source](https://github.com/stac-utils/pgstac)

### pixelflux

A performant web native pixel delivery pipeline for diverse sources, blending VNC-inspired parallel processing of pixel buffers with flexible modern encoding formats.

`pip install pixelflux` · installs (wheel) · licence: MPL-2.0 · rank 14376 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pixelflux/)

<details><summary>README extract</summary>

Part of

A performant pixel delivery pipeline for diverse sources, blending flexible and high-performance modern encoding formats.

This module provides a Python interface to a high-performance capture library supporting both X11 and Wayland environments. It captures pixel data, detects changes, and encodes modified stripes into JPEG or H.264. ...

Features:
* X11: zero-copy capture through NvFBC on the NVIDIA X driver or through DRI3 on any server whose screen lives on the GPU, else XShm capture via pure-Rust XCB with XFixes cursor and watermark compositing. ...

Example:
```python
from pixelflux import CaptureSettings, ScreenCapture

settings = CaptureSettings()

# --- Core Capture ---
settings.capture_width = 1920
settings.capture_height = 1080
settings.capture_x = 0
...

</details>

### pypushdeer

PushDeer for Python

`pip install pypushdeer` · installs (wheel) · licence: MIT License · rank 14394 · last release 2022-02-13 · [PyPI](https://pypi.org/project/pypushdeer/)

<details><summary>README extract</summary>

PushDeer SDK for Python.

Example:
```python
from pypushdeer import PushDeer

pushdeer = PushDeer(pushkey="your_push_key")
pushdeer.send_text("hello world", desp="optional description")
pushdeer.send_markdown("# hello world", desp="optional description in markdown")
pushdeer.send_image("
pushdeer.send_image(
...
```

Sections: pypushdeer, Usage, 1. Use pushdeer default server, 2. Use self-hosted server, 3. Use unique configuration for each message, TODO

</details>

### pyntcloud

Python library for working with 3D point clouds.

`pip install pyntcloud` · installs (wheel) · licence: MIT License · rank 14413 · last release 2022-07-31 · [PyPI](https://pypi.org/project/pyntcloud/)

<details><summary>README extract</summary>

pyntcloud is a Python 3 library for working with 3D point clouds leveraging the power of the Python scientific stack.

- Examples (We encourage you to try out the examples by launching Binder.)
- Documentation

Example:
```python
from pyntcloud import PyntCloud

cloud = PyntCloud.from_file("some_file.ply")

cloud.add_scalar_field("hsv")

voxelgrid_id = cloud.add_structure("voxelgrid", n_x=32, n_y=32, n_z=32)

new_cloud = cloud.get_sample("voxelgrid_nearest", voxelgrid_id=voxelgrid_id, as_PyntCloud=True)

new_cloud.to_file("out_file.npz")
```

Sections: Making point clouds fun again, Quick Overview, Integration with other libraries

</details>

### PyPowerStore

Python Library for Dell PowerStore

`pip install PyPowerStore` · installs (wheel) · licence: Apache Software License · rank 14434 · last release 2026-09-29 · [PyPI](https://pypi.org/project/PyPowerStore/)

### promptflow-devkit

Prompt flow devkit

`pip install promptflow-devkit` · installs (wheel) · licence: MIT License · rank 14435 · last release 2026-05-01 · [PyPI](https://pypi.org/project/promptflow-devkit/) · [source](https://github.com/microsoft/promptflow)

<details><summary>README extract</summary>

> Welcome to join us to make prompt flow better by
> participating discussions,
> opening issues,
> submitting PRs.

The `promptflow-devkit` is a subpackage of `promptflow`. It contains features like :

- Create and iteratively develop flow
 - Debug and iterate your flows, especially the interaction with LLMs with ease. ...

Sections: Prompt flow devkit, Introduction

</details>

### poetry-polylith-plugin

A Poetry plugin that adds tooling support for the Polylith Architecture

`pip install poetry-polylith-plugin` · installs (wheel) · licence: MIT License · rank 14442 · last release 2026-10-04 · [PyPI](https://pypi.org/project/poetry-polylith-plugin/) · [source](https://github.com/davidvujic/python-polylith)

<details><summary>README extract</summary>

This is a Python `Poetry` plugin, adding CLI support for the Polylith Architecture.

Have a look at the documentation.
You will find installation, setup, usage guides and more.

Sections: Poetry Polylith Plugin, Documentation, Quick start

</details>

### pygaul

Easy access to administrative boundary defined by FAO GAUL from Python scripts

`pip install pygaul` · installs (wheel) · licence: MIT License · rank 14449 · last release 2026-01-14 · [PyPI](https://pypi.org/project/pygaul/)

<details><summary>README extract</summary>

Features:
Easy access to administrative boundary defined by FAO GAUL 2015 from Python scripts.

This lib provides access to FAO GAUL 2015 datasets from a Python script. it is the best boundary dataset available for GEE at this point. ...

Example:
```python
import pygaul

fc = pygaul.Items(name="Singapore", content_level=1)
```

Sections: pyGAUL, Overview, Note

</details>

### prefect-coiled

Prefect integrations for interacting with Coiled.

`pip install prefect-coiled` · installs (wheel) · licence: Apache License 2.0 · rank 14451 · last release 2025-01-10 · [PyPI](https://pypi.org/project/prefect-coiled/)

<details><summary>README extract</summary>

Prefect worker for running deployments and flows on Coiled.

The worker polls a Prefect Cloud work pool for pending flows to be run and then uses Coiled to run the flow in the cloud.

To get started, see this example.

</details>

### pythonmonkey

Seamless interop between Python and JavaScript.

`pip install pythonmonkey` · installs (wheel) · licence: MIT License · rank 14452 · last release 2026-10-16 · [PyPI](https://pypi.org/project/pythonmonkey/) · [docs](https://docs.pythonmonkey.io/) · [source](https://github.com/Distributive-Network/PythonMonkey)

<details><summary>README extract</summary>

PythonMonkey is a Mozilla SpiderMonkey JavaScript engine embedded into the Python Runtime,
using the Python engine to provide the Javascript host environment.

We feature JavaScript Array and Object methods implemented on Python List and Dictionaries using the cPython C API, and the inverse using the Mozilla Firefox Spidermonkey JavaScript C++ ...

Example:
```python
from pythonmonkey import eval as js_eval

js_eval("console.log")('hello, world')
```

Sections: PythonMonkey, About, tl;dr, Goals, Data Interchange, Roadmap, Build Instructions, Running tests, Using the library, Use local version, Debugging Steps, Examples, Official API, eval(code, options)

</details>

### pytest-bazel

A pytest runner with bazel support

`pip install pytest-bazel` · installs (wheel) · licence: Apache 2.0 · rank 14454 · last release 2025-10-31 · [PyPI](https://pypi.org/project/pytest-bazel/) · [docs](https://github.com/aignas/pytest-bazel) · [source](https://github.com/aignas/pytest-bazel.git)

<details><summary>README extract</summary>

[Documentation] [Changelog] [Contributing]

Special thanks to [rules_python_pytest] and [rules_py] projects that had some
great ideas how to integrate with `pytest`. This attempts to [unify] all of the
approaches.

Sections: pytest-bazel, Thanks

</details>

### pulumi-pagerduty

A Pulumi package for creating and managing pagerduty cloud resources.

`pip install pulumi-pagerduty` · installs (wheel) · licence: Apache-2.0 · rank 14459 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pulumi-pagerduty/) · [source](https://github.com/pulumi/pulumi-pagerduty)

<details><summary>README extract</summary>

The PagerDuty Resource Provider lets you manage PagerDuty resources.

Sections: PagerDuty Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pulumi-fastly

A Pulumi package for creating and managing fastly cloud resources.

`pip install pulumi-fastly` · installs (wheel) · licence: Apache-2.0 · rank 14460 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pulumi-fastly/) · [source](https://github.com/pulumi/pulumi-fastly)

<details><summary>README extract</summary>

The Fastly resource provider for Pulumi lets you manage Fastly resources in your cloud programs. To use
this package, please install the Pulumi CLI first.

Sections: Fastly Resource Provider, Node.js (Java/TypeScript), Python, Go, .NET, Configuration, Reference

</details>

### pulumi-rs-yaml

Python bindings for the Rust Pulumi YAML engine

`pip install pulumi-rs-yaml` · installs (wheel) · licence: AGPL-3.0-or-later · rank 14466 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pulumi-rs-yaml/)

_README extract left out: share-alike licence._

### pyinstrument-cext

A CPython extension supporting pyinstrument

`pip install pyinstrument-cext` · installs from source (sdist only) · licence: not stated · rank 14473 · last release 2021-02-12 · [PyPI](https://pypi.org/project/pyinstrument-cext/)

### python-lambda-local

Run lambda function in python on local machine.

`pip install python-lambda-local` · installs (wheel) · licence: MIT License · rank 14486 · last release 2022-06-02 · [PyPI](https://pypi.org/project/python-lambda-local/)

<details><summary>README extract</summary>

|Join the chat at Actions statusPyPI version|

Run lambda function on local machine

Example:
```python
from future import print_function
from rx import Observable

def handler(event, context):
    xs = Observable.from(range(event['answer']))
    ys = xs.to_blocking()
    zs = (x*x for x in ys if x % 7 == 0)
    for x in zs:
        print(x)
```

Sections: python-lambda-local, Usage as a shell command, Project directory structure, Content of `test.py`, Content of `event.json`, Run the lambda function, Usage as a library, API signature, Sample

</details>

### pytest-databases

Reusable database fixtures for any and all databases.

`pip install pytest-databases` · installs (wheel) · licence: MIT · rank 14511 · last release 2026-05-23 · [PyPI](https://pypi.org/project/pytest-databases/) · [docs](https://github.com/litestar-org/pytest-databases#readme) · [source](https://github.com/litestar-org/pytest-databases)

<details><summary>README extract</summary>

| Project | | Status |
| --------- | :-- | ...

Features:
- 🚀 Easy-to-use database fixtures
- 🔄 Support for multiple database types
- 🐳 Docker integration for isolated testing environments
- ⚡ Fast and efficient test execution
- 🔧 Highly configurable ...

Example:
```python
from pytest_databases.docker.postgres import PostgresService
import psycopg

def test_one(postgres_service: PostgresService) -> None:
    with psycopg.connect(
        f"postgresql://{postgres_service.user}:{postgres_service.password}@{postgres_service.host}:{postgres_service.port}/{postgres_service.database}",
        autocommit=True,
...
```

Sections: Pytest Databases, Features, Quick Start, Documentation

</details>

### pyuseragents

A Python module which does one thing: giving you a random User-Agent Header

`pip install pyuseragents` · installs (wheel) · licence: MIT License · rank 14519 · last release 2021-03-21 · [PyPI](https://pypi.org/project/pyuseragents/)

<details><summary>README extract</summary>

*Do not worry about sticking with a single user-agent for you HTTP requests ever again!*

Example:
```python
>>> import pyuseragents
>>> headers = {
    "User-Agent": pyuseragents.random(),
    "Content-Type": "application/json",
    "and so on..."
}
>>> pyuseragents.random()
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
```

Sections: `useragents`, Getting Started, Prerequisites, List of User-Agents, Usage, Deployment, Built With

</details>

### pynisher

A library to limit the resources used by functions using subprocesses

`pip install pynisher` · installs from source (sdist only) · licence: BSD License · rank 14572 · last release 2023-11-13 · [PyPI](https://pypi.org/project/pynisher/)

<details><summary>README extract</summary>

Pynisher is a library to limit resources of a function call in a synchronous manner.
You can use this to ensure that your function doesn't use up more resources than it
should.

Features:
To check if a feature is supported on your system:

Currently we mainly support Linux with partial support for Mac and Windows: ...

Example:
```python
import pynisher

def sleepy(x: int) -> int:
    time.sleep(x)
    return x

# You can also use `cpu_time` instead
with pynisher.limit(sleepy, wall_time=7) as limited_sleep:
    x = limited_sleep(10)  # Will raise a TimeoutException
```

Sections: Usage, Details, Features, Parameters, Exceptions, Changes from v0.6.0, Controlling namespace pollution, Pynisher and Multithreading, Nested Pynisher and Multiprocessing contexts, Project origin

</details>

### pysigma-backend-crowdstrike

pySigma CrowdStrike Logscale backend and processing pipelines for the Falcon data model.

`pip install pysigma-backend-crowdstrike` · installs (wheel) · licence: OSI Approved · rank 14602 · last release 2025-11-30 · [PyPI](https://pypi.org/project/pysigma-backend-crowdstrike/) · [source](https://github.com/SigmaHQ/pySigma-backend-crowdstrike)

<details><summary>README extract</summary>

This is the CrowdStrike backend for pySigma. It provides the package `sigma.backends.crowdstrike` with the `LogScaleBackend` class.

Further it contains the following processing pipelines under `sigma.pipelines.crowdstrike`: ...

Sections: pySigma CrowdStrike Backend, Falcon Pipeline, Limitations and caveats, References

</details>

