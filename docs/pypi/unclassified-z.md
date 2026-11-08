# Unclassified / Z

[Index](README.md) · 43 packages in this topic, by downloads.

### zipp

Backport of pathlib-compatible object wrapper for zip files

`pip install zipp` · installs (wheel) · licence: MIT · rank 80 · last release 2026-10-21 · [PyPI](https://pypi.org/project/zipp/) · [source](https://github.com/jaraco/zipp)

<details><summary>README extract</summary>

A pathlib-compatible Zipfile object wrapper. Official backport of the standard library
Path object.

New features are introduced in this third-party library and later merged
into CPython. The following table indicates which versions of this library
were contributed to different versions in the standard library:

Sections: Compatibility, Usage, For Enterprise

</details>

### zstandard

Zstandard bindings for Python

`pip install zstandard` · installs (wheel) · licence: BSD-3-Clause · rank 173 · last release 2025-09-14 · [PyPI](https://pypi.org/project/zstandard/) · [docs](https://python-zstandard.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

ci-testci-wheelci-typingci-sdistci-anacondaci-sphinx|

This project provides Python bindings for interfacing with the
Zstandard compression library. A C extension
and CFFI interface are provided.

The primary goal of the project is to provide a rich interface to the
underlying C API through a Pythonic interface while not sacrificing
performance. ...

</details>

### zope.interface

Interfaces for Python

`pip install zope.interface` · installs (wheel) · licence: ZPL-2.1 · rank 427 · last release 2026-10-15 · [PyPI](https://pypi.org/project/zope.interface/) · [docs](https://zopeinterface.readthedocs.io) · [source](https://github.com/zopefoundation/zope.interface)

<details><summary>README extract</summary>

This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

This package provides an implementation of "object interfaces" for Python.
Interfaces are a mechanism for labeling objects as conforming to a given
API or contract. ...

Example:
```python
  class Foo:
      implements(IFoo)
      ...

can now also be written::

  @implementer(IFoo):
  class Foo:
      ...

There are 2to3 fixers available to do this change automatically in the
zope.fixers package.
```

Sections: `zope.interface`, 8.7 (2026-10-15), 8.6 (2026-08-20), 8.5 (2026-05-26), 8.4 (2026-04-25), 8.3 (2026-04-10), 8.2 (2026-01-09), 8.1.1 (2025-11-15), 8.1 (2025-11-10), 8.0.1 (2025-09-25), 8.0 (2025-09-12), 7.2 (2024-11-28), 7.1.1 (2024-10-23), 7.1.0 (2024-10-10)

</details>

### zeep

A Python SOAP client

`pip install zeep` · installs (wheel) · licence: MIT License · rank 631 · last release 2026-06-18 · [PyPI](https://pypi.org/project/zeep/) · [docs](https://docs.python-zeep.org) · [source](https://github.com/mvantellingen/python-zeep)

<details><summary>README extract</summary>

A Python SOAP client

Features:
- Compatible with Python 3.10, 3.11, 3.12, 3.13, 3.14 and PyPy3
- Built on top of lxml, requests, and httpx
- Support for Soap 1.1, Soap 1.2, and HTTP bindings
- Support for WS-Addressing headers
- Support for WSSE (UserNameToken / x.509 signing) ...

Example:
```python
from zeep import Client

client = Client('tests/wsdl_files/example.rst')
client.service.ping()
```

Sections: Zeep: Python SOAP client, Highlights, Usage

</details>

### zstd

ZSTD Bindings for Python

`pip install zstd` · installs (wheel) · licence: BSD · rank 1430 · last release 2025-06-23 · [PyPI](https://pypi.org/project/zstd/)

<details><summary>README extract</summary>

+----------------------+---------------------+
| wheels for:
+======================+=====================+
| cpython 2.7 x86 cpython27x86
+----------------------+---------------------+
| cpython 2.7 x64 cpython27x64
+----------------------+---------------------+
| cpython 2.7 armhf cpython27armhf
+----------------------+---------------------+
| ...

Sections: python-zstd, WARNING!!!, LINKS, Build from source

</details>

### zizmor

Static analysis for GitHub Actions

`pip install zizmor` · installs (wheel) · licence: MIT · rank 1520 · last release 2026-11-02 · [PyPI](https://pypi.org/project/zizmor/) · [docs](https://docs.zizmor.sh) · [source](https://github.com/zizmorcore/zizmor)

<details><summary>README extract</summary>

`zizmor` is a static analysis tool for CI/CD systems.

It can find and fix security issues in common CI/CD setups, including GitHub Actions,
Dependabot, and pre-commit. Some of the things `zizmor` finds: ...

Sections: 🌈 zizmor, The name?

</details>

### z3-solver

an efficient SMT solver library

`pip install z3-solver` · installs (wheel) · licence: MIT License · rank 1526 · last release 2026-10-29 · [PyPI](https://pypi.org/project/z3-solver/)

<details><summary>README extract</summary>

Z3 is a theorem prover from Microsoft Research with support for bitvectors, booleans, arrays, floating point numbers, strings, and other data types.

For documentation, please read

</details>

### zipstream-ng

A modern and easy to use streamable zip file generator

`pip install zipstream-ng` · installs (wheel) · licence: LGPL-3.0-only · rank 2027 · last release 2026-08-20 · [PyPI](https://pypi.org/project/zipstream-ng/) · [source](https://github.com/pR0Ps/zipstream-ng)

_README extract left out: share-alike licence._

### zict

Mutable mapping tools

`pip install zict` · installs (wheel) · licence: BSD License · rank 2111 · last release 2023-04-17 · [PyPI](https://pypi.org/project/zict/)

### zenpy

Python wrapper for the Zendesk API

`pip install zenpy` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 2691 · last release 2026-02-19 · [PyPI](https://pypi.org/project/zenpy/)

_README extract left out: share-alike licence._

### zope.deprecation

Zope Deprecation Infrastructure

`pip install zope.deprecation` · installs (wheel) · licence: Zope Public License · rank 2834 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.deprecation/)

<details><summary>README extract</summary>

This package provides a simple function called `deprecated(names, reason)`
to mark deprecated modules, classes, functions, methods and properties.

Please see for the documentation.

Sections: `zope.deprecation`, 6.0 (2025-09-12), 5.1 (2025-01-15), 5.0 (2023-03-29), 4.4.0 (2018-12-03), 4.3.0 (2017-08-07), 4.2.0 (2016-11-07), 4.1.2 (2015-01-13), 4.1.1 (2014-03-19), 4.1.0 (2013-12-20), 4.0.2 (2012-12-31), 4.0.1 (2012-11-21), 4.0.0 (2012-05-16), 3.5.1 (2012-03-15)

</details>

### zipcodes

Query U.S. state zipcodes without SQLite.

`pip install zipcodes` · installs (wheel) · licence: MIT · rank 3608 · last release 2026-11-02 · [PyPI](https://pypi.org/project/zipcodes/)

<details><summary>README extract</summary>

Python:

Rust: ) )

Zipcodes is a simple library for querying U.S. zipcodes. No SQLite, no
network, no runtime data files — the full dataset is embedded in the package.

Since 2.0, the library is implemented in Rust and published from a single
codebase as both the `zipcodes` Python package
and the `zipcodes` Rust crate. ...

Example:
```python
>>> from pprint import pprint
>>> import zipcodes

>>> # Simple zip-code matching.
>>> pprint(zipcodes.matching('77429'))
[{'acceptable_cities': [],
  'active': True,
  'area_codes': ['281', '346', '713', '832'],
  'city': 'Cypress',
  'country': 'US',
  'county': 'Harris County',
  'lat': '29.9766',
  'long': '-95.6358',
  'state': 'TX',
...
```

Sections: Zipcodes, Python, Rust, New in 2.0, Zipcode Data, Tests, Examples, Repository layout

</details>

### zthreading

A collection of wrapper classes for event broadcast and task management for python (Python Threads or Asyncio).

`pip install zthreading` · installs (wheel) · licence: LICENSE · rank 4297 · last release 2022-06-13 · [PyPI](https://pypi.org/project/zthreading/)

### zen-engine

Open-Source Business Rules Engine

`pip install zen-engine` · installs (wheel) · licence: not stated · rank 4519 · last release 2026-10-09 · [PyPI](https://pypi.org/project/zen-engine/) · [docs](https://docs.gorules.io/developers/sdks/python) · [source](https://github.com/gorules/zen)

<details><summary>README extract</summary>

Business logic humans can read and machines can run. One copy of your rules: the owner reads it, every system runs it.

ZEN Engine is a cross-platform, open-source Business Rules Engine (BRE) written in Rust with native Python bindings, alongside Node.js, Go, Java, Kotlin and .NET. ...

Example:
```python
import zen

with open("./jdm_graph.json", "r") as f:
    content = f.read()

engine = zen.ZenEngine()

decision = engine.create_decision(content)
result = decision.evaluate({"input": 15})
print(result)
```

Sections: Python Rules Engine, Rules that read like sentences, Rules as graphs, or as documents, What's new in 2.0, Quickstart, Loaders, Other platforms, The GoRules platform, AI that builds rules, and stays reviewable, Prove it before it ships

</details>

### zope.hookable

Zope hookable

`pip install zope.hookable` · installs (wheel) · licence: ZPL-2.1 · rank 5249 · last release 2026-10-16 · [PyPI](https://pypi.org/project/zope.hookable/) · [docs](https://zopehookable.readthedocs.io) · [source](https://github.com/zopefoundation/zope.hookable)

<details><summary>README extract</summary>

This package supports the efficient creation of "hookable" objects, which
are callable objects that are meant to be optionally replaced.

The idea is that you create a function that does some default thing and make it
hookable. Later, someone can modify what it does by calling its sethook method
and changing its implementation. ...

Sections: zope.hookable, 8.4 (2026-10-16), 8.3 (2026-08-20), 8.2 (2025-11-18), 8.1 (2025-10-28), 8.0 (2025-09-12), 7.0 (2024-09-17), 6.0 (2023-10-05), 5.4 (2022-11-17), 5.3 (2022-11-03), 5.2 (2022-09-13), 5.1.0 (2021-07-20), 5.0.1 (2020-03-10), 5.0.0 (2019-11-12)

</details>

### zmq

You are probably looking for pyzmq.

`pip install zmq` · installs from source (sdist only) · licence: BSD · rank 5717 · last release 2015-05-21 · [PyPI](https://pypi.org/project/zmq/)

### zss

Tree edit distance using the Zhang Shasha algorithm

`pip install zss` · installs from source (sdist only) · licence: not stated · rank 5953 · last release 2018-03-12 · [PyPI](https://pypi.org/project/zss/)

### zi-api-auth-client

A library that supports username-password and PKI authentication methods for enterprise-api

`pip install zi-api-auth-client` · installs (wheel) · licence: MIT License · rank 6658 · last release 2025-09-04 · [PyPI](https://pypi.org/project/zi-api-auth-client/)

<details><summary>README extract</summary>

This library supports 2 types of authentication methods. Both the methods return a JWT token which you can use to make
api calls for enterprise-api on production.

Usage:

1. import zi_api_auth_client

2. jwt_token = zi_api_auth_client.user_name_pwd_authentication("your_user_name", "your_password") ...

Sections: zi_api_auth_client, Username and password authentication, PKI authentication

</details>

### zigpy

Library implementing a Zigbee stack

`pip install zigpy` · installs (wheel) · licence: GPL-3.0 · rank 7346 · last release 2026-10-28 · [PyPI](https://pypi.org/project/zigpy/) · [source](https://github.com/zigpy/zigpy)

_README extract left out: share-alike licence._

### zope.proxy

Generic Transparent Proxies

`pip install zope.proxy` · installs (wheel) · licence: ZPL-2.1 · rank 7435 · last release 2026-08-20 · [PyPI](https://pypi.org/project/zope.proxy/) · [docs](https://zopeproxy.readthedocs.io) · [source](https://github.com/zopefoundation/zope.proxy)

<details><summary>README extract</summary>

Proxies are special objects which serve as mostly-transparent
wrappers around another object, intervening in the apparent behavior of
the wrapped object only when necessary to apply the policy (e.g., access
checking, location brokering, etc.) for which the proxy is responsible. ...

Sections: `zope.proxy, 7.3 (2026-08-20), 7.2 (2026-04-30), 7.1 (2025-11-18), 7.0 (2025-09-12), 6.1 (2024-10-02), 6.0 (2024-09-17), 5.3 (2024-08-07), 5.2 (2024-02-09), 5.1 (2023-10-05), 5.0.0 (2023-01-18), 4.6.1 (2022-11-16), 4.6.0 (2022-11-03), 4.5.1 (2022-09-15)

</details>

### zuvloop

A libuv event loop for asyncio, written in Zig.

`pip install zuvloop` · installs (wheel) · licence: MIT · rank 7626 · last release 2026-09-15 · [PyPI](https://pypi.org/project/zuvloop/) · [source](https://github.com/Kludex/zuvloop)

<details><summary>README extract</summary>

A fast, drop-in asyncio event loop, powered by libuv and written in Zig ⚡

Documentation:

Source Code:

zuvloop is a replacement for the built-in `asyncio` event loop.

Your code stays the same. The loop underneath gets faster. 🚀

The key features are: ...

Example:
```python
import asyncio

import zuvloop

async def main() -> None:
    reader, writer = await asyncio.open_connection("example.com", 80)
    writer.write(b"GET / HTTP/1.0\r\nHost: example.com\r\n\r\n")
    await writer.drain()
    print(await reader.read(64))
    writer.close()
    await writer.wait_closed()

zuvloop.run(main())
```

Sections: zuvloop, Performance, Requirements, Example, Observability, Compatibility

</details>

### zombie-imp

A copy of the `imp` module that was removed in Python 3.12

`pip install zombie-imp` · installs (wheel) · licence: Python Software Foundation License · rank 8350 · last release 2025-12-22 · [PyPI](https://pypi.org/project/zombie-imp/)

<details><summary>README extract</summary>

~~A particularly mischievous act of necromancy. That is,~~
A copy of the `imp` module that was removed in Python 3.12.

Don't use this, it'll probably trick and bite you.

Sections: zombie-imp, Usage

</details>

### zyte-api

Python interface to Zyte API

`pip install zyte-api` · installs (wheel) · licence: BSD License · rank 8507 · last release 2026-07-23 · [PyPI](https://pypi.org/project/zyte-api/) · [docs](https://python-zyte-api.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

Command-line client and Python client library for Zyte API.

Example:
```python
from zyte_api import ZyteAPI

client = ZyteAPI(api_key="YOUR_API_KEY")
response = client.get({"url": " "httpResponseBody": True})
```

Sections: python-zyte-api, Basic usage, Set your API key, Use the command-line client, Use the Python sync API, Use the Python async API

</details>

### zerobouncesdk

ZeroBounce Python API - https://www.zerobounce.net.

`pip install zerobouncesdk` · installs (wheel) · licence: MIT · rank 8627 · last release 2026-10-24 · [PyPI](https://pypi.org/project/zerobouncesdk/) · [docs](https://www.zerobounce.net/docs/)

<details><summary>README extract</summary>

This SDK contains methods for interacting easily with ZeroBounce API.
More information about ZeroBounce you can find in the official documentation.

Example:
```python
from zerobouncesdk import ZeroBounce
```

Sections: Zero Bounce Python SDK, USAGE, Examples, AI Scoring API, Validation options, Bulk email finder and domain search, List evaluator, Allowlist and blocklist filters, Amazon S3 and SFTP/FTP files, Inbox Placement Tester, Warmup API, Other hosts, Local setup, Lint and test

</details>

### ziafont

Convert TTF/OTF font glyphs to SVG paths

`pip install ziafont` · installs (wheel) · licence: MIT License · rank 8995 · last release 2025-11-27 · [PyPI](https://pypi.org/project/ziafont/) · [docs](https://ziafont.readthedocs.io) · [source](https://github.com/cdelker/ziafont)

<details><summary>README extract</summary>

Ziafont reads TrueType/OpenType font files and draws characters and strings as SVG <path> elements. Unlike the SVG <text> element, the output of Ziafont's SVG will render identically on any system, independent of whether the original font is available. ...

</details>

### zlib-state

Low-level interface to the zlib library that enables capturing the decoding state

`pip install zlib-state` · installs (wheel) · licence: MIT License · rank 9178 · last release 2026-10-15 · [PyPI](https://pypi.org/project/zlib-state/)

<details><summary>README extract</summary>

Low-level interface to the zlib library that enables capturing the decoding state.

Example:
```python
import zlib_state

TARGET_LINE = 5000 # pick back up after around the 5,000th line
# Specify keep_last_state=True to tell object to grab and keep the state and pos after each block
with zlib_state.GzipStateFile('testdata/frankenstein.txt.gz', keep_last_state=True) as f:
    for i, line in enumerate(f):
        if i == TARGET_LINE:
...
```

Sections: zlib-state, GzipStateFile, Decompressor

</details>

### zigpy-znp

A library for zigpy which communicates with TI ZNP radios

`pip install zigpy-znp` · installs (wheel) · licence: GPL-3.0 · rank 10223 · last release 2026-09-08 · [PyPI](https://pypi.org/project/zigpy-znp/) · [source](https://github.com/zigpy/zigpy-znp)

_README extract left out: share-alike licence._

### zipstream

Zipfile generator

`pip install zipstream` · installs from source (sdist only) · licence: UNKNOWN · rank 10326 · last release 2016-05-06 · [PyPI](https://pypi.org/project/zipstream/)

### zai-sdk

A SDK library for accessing big model apis from Z.ai

`pip install zai-sdk` · installs (wheel) · licence: not stated · rank 10392 · last release 2026-06-16 · [PyPI](https://pypi.org/project/zai-sdk/)

<details><summary>README extract</summary>

中文文档 | English

Z.ai Open Platform The official Python SDK for Z.ai's large model open interface, making it easier for developers to call Z.ai's open APIs.

- Standard Chat: Create chat completions with various models including `glm-5.2`
- Streaming Support: Real-time streaming responses for interactive applications ...

Example:
```python
from zai import ZaiClient, ZhipuAiClient

# For Overseas users, create the ZaiClient
client = ZaiClient(api_key="your-api-key")

# For Chinese users, create the ZhipuAiClient
client = ZhipuAiClient(api_key="your-api-key")

# Create chat completion
response = client.chat.completions.create(
    model="glm-5.2",
    messages=[
...
```

...

</details>

### zha-quirks

Library implementing Zigpy quirks for ZHA in Home Assistant

`pip install zha-quirks` · installs (wheel) · licence: Apache-2.0 · rank 10465 · last release 2026-11-04 · [PyPI](https://pypi.org/project/zha-quirks/) · [source](https://github.com/zigpy/zha-device-handlers)

<details><summary>README extract</summary>

ZHA Device Handlers are custom quirks implementations for Zigpy, the library that provides the Zigbee support for the ZHA component in Home Assistant.

ZHA device handlers bridge the functionality gap created when manufacturers deviate from the ZCL specification, handling deviations and exceptions by parsing custom messages to and from Zigbee ...

Example:
```python
class Plug(XiaomiCustomDevice):
    """lumi.plug.maus01 plug."""

    def init(self, *args, **kwargs):
        """Init."""
        self.voltage_bus = Bus()
        self.consumption_bus = Bus()
        self.power_bus = Bus()
        super().init(*args, **kwargs)

    signature = {
        MODELS_INFO: [(LUMI, "lumi.plug.maus01")],
...
```

...

</details>

### zigpy-deconz

A library which communicates with Deconz radios for zigpy

`pip install zigpy-deconz` · installs (wheel) · licence: GPL-3.0 · rank 10499 · last release 2026-10-28 · [PyPI](https://pypi.org/project/zigpy-deconz/) · [source](https://github.com/zigpy/zigpy-deconz)

_README extract left out: share-alike licence._

### zigpy-xbee

A library which communicates with XBee radios for zigpy

`pip install zigpy-xbee` · installs (wheel) · licence: GPL-3.0 · rank 10578 · last release 2026-08-25 · [PyPI](https://pypi.org/project/zigpy-xbee/) · [source](https://github.com/zigpy/zigpy-xbee)

_README extract left out: share-alike licence._

### zigpy-zigate

A library which communicates with ZiGate radios for zigpy

`pip install zigpy-zigate` · installs (wheel) · licence: GPL-3.0 · rank 10597 · last release 2026-04-20 · [PyPI](https://pypi.org/project/zigpy-zigate/) · [source](https://github.com/zigpy/zigpy-zigate)

_README extract left out: share-alike licence._

### zhinst-utils

Zurich Instruments utils for device control

`pip install zhinst-utils` · installs (wheel) · licence: MIT License · rank 11280 · last release 2026-04-27 · [PyPI](https://pypi.org/project/zhinst-utils/)

<details><summary>README extract</summary>

zhinst-utils provides a set of helper functions for the native LabOne Python API
called zhinst.core.

It offers higher level functions to ease the communication with
Zurich Instruments devices. It is not intended to be a
separate layer above ``zhinst.core`` but rather as an addition. ...

Example:
```python
import zhinst.utils.shfqa
import zhinst.utils.shfsg
import zhinst.utils.shfqc

help(zhinst.utils.shfqa)
help(zhinst.utils.shfsg)
help(zhinst.utils.shfqc)
```

Sections: Utils for Zurich Instruments LabOne API, Usage, About

</details>

### zhipuai

A SDK library for accessing big model apis from ZhipuAI

`pip install zhipuai` · installs (wheel) · licence: not stated · rank 11432 · last release 2025-08-25 · [PyPI](https://pypi.org/project/zhipuai/)

<details><summary>README extract</summary>

中文文档 | English

The official Python SDK for ZhipuAI's large model open interface, making it easier for developers to call ZhipuAI's open APIs.

- Type Safety: Complete type annotations for all interfaces
- Easy Integration: Simple initialization and intuitive method calls
- High Performance: Built-in connection pooling and request optimization ...

Example:
```python
from zhipuai import ZhipuAI

# Initialize client
client = ZhipuAI(api_key="your-api-key")

# Create chat completion
response = client.chat.completions.create(
    model="glm-4",
    messages=[
        {"role": "user", "content": "Hello, ZhipuAI!"}
    ]
)
print(response.choices[0].message.content)
```

...

</details>

### zip2tz

A simple timezone lookup by zip code

`pip install zip2tz` · installs (wheel) · licence: not stated · rank 11973 · last release 2026-04-19 · [PyPI](https://pypi.org/project/zip2tz/)

<details><summary>README extract</summary>

Fast, zero-dependency US zip code to timezone lookup for Python.

- 38,000+ zip codes mapped to IANA timezones
- Zero dependencies — pure Python, works everywhere
- O(1) lookup — instant hash table lookups, no database or file I/O
- Tiny footprint — ~100KB installed, loads in milliseconds
- Type-annotated — full type hints included

Features:
Most timezone lookup libraries require external databases, network calls, or heavy dependencies. `zip2tz` bakes the data directly into Python bytecode — just import and go.

| Feature | zip2tz | Other libraries | ...

Example:
```python
import zip2tz

# Get timezone for a zip code
tz = zip2tz.timezone("90210")
print(tz)  # America/Los_Angeles

tz = zip2tz.timezone("10001")
print(tz)  # America/New_York

# Works with integers too
...

</details>

### zh-sentence

Light-weight sentence tokenizer for Chinese languages.

`pip install zh-sentence` · installs (wheel) · licence: Apache Software License · rank 12275 · last release 2021-10-23 · [PyPI](https://pypi.org/project/zh-sentence/)

<details><summary>README extract</summary>

A light-weight sentence tokenizer for Chinese languages.

Sample Code:

from zh_sentence.tokenizer import tokenize

paragraph_str = "你好吗？你快乐吗？"

sentence_list = tokenize(paragraph_str)

for sentence in sentence_list:
 print(sentence)

</details>

### zuko

Normalizing flows in PyTorch

`pip install zuko` · installs (wheel) · licence: MIT · rank 12332 · last release 2026-03-10 · [PyPI](https://pypi.org/project/zuko/) · [docs](https://zuko.readthedocs.io) · [source](https://github.com/probabilists/zuko)

<details><summary>README extract</summary>

Zuko is a Python package that implements normalizing flows in PyTorch. It relies as much as possible on distributions and transformations already provided by PyTorch. Unfortunately, the `Distribution` and `Transform` classes of `torch` are not sub-classes of `torch.nn.Module`, which means you cannot send their internal tensors to GPU with ...

Example:
```python
import torch
import zuko

# Neural spline flow (NSF) with 3 sample features and 5 context features
flow = zuko.flows.NSF(3, 5, transforms=3, hidden_features=[128] * 3)

# Train to maximize the log-likelihood
optimizer = torch.optim.Adam(flow.parameters(), lr=1e-3)

for x, c in trainset:
    loss = -flow(c).log_prob(x)  # -log p(x | c)
...
```

Sections: Zuko - Normalizing flows in PyTorch, Getting started, Available flows

</details>

### zhinst-timing-models

Feedback Data Latency model for PQSC, SHF- and HDAWG systems.

`pip install zhinst-timing-models` · installs (wheel) · licence: MIT · rank 12639 · last release 2026-10-29 · [PyPI](https://pypi.org/project/zhinst-timing-models/)

<details><summary>README extract</summary>

Feedback Data Latency model for PQSC, SHF- and HDAWG systems.

Table of Contents

- Feedback Latency Model Parameters
 - Installation
 - Usage
 - License

Example:
```python
from zhinst.timing_models import (
    PQSCMode,
    QAType,
    QCCSFeedbackModel,
    SGType,
    TriggerSource,
    get_feedback_system_description,
)

model = QCCSFeedbackModel(
    description=get_feedback_system_description(
        generator_type=SGType.HDAWG,
        analyzer_type=QAType.SHFQA,
        pqsc_mode=PQSCMode.DECODER,
...
```

Sections: Feedback Latency Model Parameters, Usage

</details>

### zabbix-api

Zabbix API

`pip install zabbix-api` · installs from source (sdist only) · licence: GNU LGPL 2.1 · rank 12913 · last release 2023-05-04 · [PyPI](https://pypi.org/project/zabbix-api/)

_README extract left out: share-alike licence._

### zExceptions

zExceptions contains common exceptions used in Zope.

`pip install zExceptions` · installs (wheel) · licence: Zope Public License · rank 12988 · last release 2026-02-19 · [PyPI](https://pypi.org/project/zExceptions/)

<details><summary>README extract</summary>

Features:
zExceptions contains common exceptions and helper functions related to
exceptions as used in Zope.

Sections: Overview, 6.0 (2026-02-19), 5.0 (2023-06-28), 4.3 (2022-12-18), 4.2 (2021-10-22), 4.1 (2018-10-05), 4.0 (2018-01-27), 3.6.1 (2017-05-17), 3.6 (2017-02-05), 3.5 (2017-02-05), 3.4 (2016-09-08), 3.3 (2016-08-06), 3.2 (2016-07-22), 3.1 (2016-07-22)

</details>

### zope.globalrequest

Global way of retrieving the currently active request.

`pip install zope.globalrequest` · installs (wheel) · licence: Zope Public License · rank 13386 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.globalrequest/)

<details><summary>README extract</summary>

This package provides a contextless way to retrieve the currently active request object in a zope-based web framework.
To do so you simply need to do the following:
This package is mainly intended to be used with the Zope/Plone stack. ...

Example:
```python
from zope.globalrequest import getRequest
request = getRequest()
```

Sections: Introduction, 3.0 (2025-09-12), 2.1 (2025-09-04), 2.0 (2023-03-27), 1.6 (2022-10-18), 1.5 (2018-10-04), 1.4 (2017-05-29), 1.3 (2016-10-22), 1.2 (2016-06-07), 1.1 (2015-04-29), 1.0 (2010-08-07), 1.0a2 (2009-01-17), 1.0a1 (2009-01-15)

</details>

### zoo-kcl

(no summary)

`pip install zoo-kcl` · installs (wheel) · licence: not stated · rank 14795 · last release 2026-11-04 · [PyPI](https://pypi.org/project/zoo-kcl/)

