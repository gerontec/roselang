# Unclassified / V

[Index](README.md) · 93 packages in this topic, by downloads.

### vcs-versioning

the blessed package to manage your versions by vcs metadata

`pip install vcs-versioning` · installs (wheel) · licence: MIT · rank 345 · last release 2026-10-06 · [PyPI](https://pypi.org/project/vcs-versioning/) · [docs](https://github.com/pypa/setuptools-scm#readme) · [source](https://github.com/pypa/setuptools-scm)

### vine

Python promises.

`pip install vine` · installs (wheel) · licence: BSD License · rank 461 · last release 2023-11-05 · [PyPI](https://pypi.org/project/vine/)

<details><summary>README extract</summary>

:Version: 5.1.0
:Web:
:Download:
:Source:
:Keywords: promise, async, future

This is a special implementation of promises in that it can be used both
for promise of a value and lazy evaluation. The biggest upside for this
is that everything in a promise can also be a promise, e.g. filters,
callbacks and errbacks can all be promises.

Sections: vine - Python Promises, About

</details>

### valkey

Python client for Valkey forked from redis-py

`pip install valkey` · installs (wheel) · licence: MIT License · rank 1667 · last release 2026-10-12 · [PyPI](https://pypi.org/project/valkey/) · [docs](https://valkey-py.readthedocs.io/en/latest/) · [source](https://github.com/valkey-io/valkey-py)

<details><summary>README extract</summary>

The Python interface to the Valkey key-value store.

Installation | Usage | Documentation | Advanced Topics | Contributing

Example:
```python
import valkey
r = valkey.Valkey(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
# True
r.get('foo')
# b'bar'
```

Sections: valkey-py, Usage, Basic Example, Migration from redis-py, Connection Pools, Valkey Commands, Documentation, Advanced Topics, Pipelines, PubSub

</details>

### voluptuous

Python data validation library

`pip install voluptuous` · installs (wheel) · licence: BSD License · rank 1709 · last release 2025-12-18 · [PyPI](https://pypi.org/project/voluptuous/)

<details><summary>README extract</summary>

Features:
Validators are simple callables:
No need to subclass anything, just use a function.

Errors are simple exceptions:
A validator can just `raise Invalid(msg)` and expect the user to get
useful messages. ...

Example:
```python
>>> from voluptuous import Schema
>>> schema = Schema({
...   'q': str,
...   'per_page': int,
...   'page': int,
... })
```

Sections: Voluptuous is a Python data validation library, Contact, Documentation, Why use Voluptuous over another validation library?, Show me an example, Defining schemas, Literals, Types, URLs, Lists, Sets and frozensets, Validation functions, Dictionaries, Extra dictionary keys

</details>

### voyageai

(no summary)

`pip install voyageai` · installs (wheel) · licence: MIT License · rank 1812 · last release 2026-07-10 · [PyPI](https://pypi.org/project/voyageai/)

<details><summary>README extract</summary>

Voyage AI provides cutting-edge embedding and rerankers.

Embedding models are neural net models (e.g., transformers) that convert unstructured and complex data, such as documents, images, audios, videos, or tabular data, into dense numerical vectors (i.e. embeddings) that capture their semantic meanings. ...

Example:
```python
import voyageai

vo = voyageai.Client()  # no API key needed for local models
result = vo.embed(["Hello, world!"], model="voyage-4-nano", input_type="document")
print(result.embeddings[0])
```

Sections: Voyage Python Library, Local models (`voyage-4-nano`), Voyage AI Official Documentation

</details>

### vercel-oidc

OIDC helpers for Vercel Python applications

`pip install vercel-oidc` · installs (wheel) · licence: MIT · rank 2207 · last release 2026-11-03 · [PyPI](https://pypi.org/project/vercel-oidc/)

<details><summary>README extract</summary>

`vercel.oidc` retrieves and decodes Vercel OIDC tokens.

Token lookup prefers the `x-vercel-oidc-token` request header registered with
`vercel.headers.set_headers()`, then `VERCEL_OIDC_TOKEN`. The compatibility
alias `vercel.oidc.set_headers()` updates the same header context. In local development,
you can load a short-lived token dynamically: ...

Example:
```python
from vercel.oidc import decode_oidc_payload
from vercel.headers import set_headers
from vercel.oidc.aio import get_vercel_oidc_token

async def main() -> None:
    token = await get_vercel_oidc_token()
    payload = decode_oidc_payload(token)
    project_id = payload.get("project_id")
```

Sections: OIDC, Async Token Lookup, Verification, Token Identity

</details>

### vercel-headers

Request header helpers for Vercel Python applications

`pip install vercel-headers` · installs (wheel) · licence: MIT · rank 2227 · last release 2026-09-08 · [PyPI](https://pypi.org/project/vercel-headers/)

<details><summary>README extract</summary>

`vercel.headers` stores request headers for Vercel Function helpers and exposes
IP address and geolocation helpers.

Register request headers once per request:

OIDC and cache helpers read the same registered header context.

Example:
```python
from vercel.headers import set_headers

set_headers(request.headers)
```

</details>

### vercel

Python SDK for Vercel

`pip install vercel` · installs (wheel) · licence: MIT · rank 2327 · last release 2026-11-03 · [PyPI](https://pypi.org/project/vercel/)

<details><summary>README extract</summary>

This package exposes small public modules for Vercel APIs and Vercel Function
helpers.

- `vercel.cache` - Runtime Cache clients and invalidation helpers
- `vercel.cron` - cron decorators and schedule helpers
- `vercel.deployments` - deployment creation and deployment file upload helpers ...

Sections: vercel Package Map, Public Modules, Internals

</details>

### vercel-cache

Runtime cache helpers for Vercel Python applications

`pip install vercel-cache` · installs (wheel) · licence: MIT · rank 2496 · last release 2026-11-03 · [PyPI](https://pypi.org/project/vercel-cache/)

<details><summary>README extract</summary>

`vercel.cache` exposes runtime cache helpers for Vercel Python applications.

Use `get_cache()` for synchronous code and `vercel.cache.aio.get_cache()` for
async code. When runtime cache environment variables are unavailable, cache
operations fall back to an in-memory cache.

</details>

### vercel-internal-telemetry

Internal telemetry helpers for Vercel Python packages

`pip install vercel-internal-telemetry` · installs (wheel) · licence: MIT · rank 2503 · last release 2026-11-03 · [PyPI](https://pypi.org/project/vercel-internal-telemetry/)

<details><summary>README extract</summary>

`vercel.internal.telemetry` provides shared internal telemetry helpers for
Vercel Python packages.

</details>

### versioneer

Easy VCS-based management of project version strings

`pip install versioneer` · installs (wheel) · licence: The Unlicense (Unlicense) · rank 2590 · last release 2023-07-07 · [PyPI](https://pypi.org/project/versioneer/)

<details><summary>README extract</summary>

* like a rocketeer, but for versions!

* Brian Warner
* License: Public Domain (Unlicense)
* Compatible with: Python 3.7, 3.8, 3.9, 3.10, 3.11 and pypy3
* [][pypi-url]
* [][travis-url]

This is a tool for managing a recorded version number in setuptools-based
python projects. ...

Sections: The Versioneer, Vendored mode, Build-time dependency mode, Version Identifiers, Theory of Operation, Version-String Flavors, Styles, Debugging, Known Limitations, Subprojects, Updating Versioneer, Future Directions, Similar projects

</details>

### venusian

A library for deferring decorator actions

`pip install venusian` · installs (wheel) · licence: Repoze Public License · rank 2706 · last release 2024-12-02 · [PyPI](https://pypi.org/project/venusian/)

<details><summary>README extract</summary>

Venusian is a library which allows framework authors to defer
decorator actions. Instead of taking actions when a function (or
class) decorator is executed at import time, you can defer the action
usually taken by the decorator until a separate "scan" phase.

See the "docs" directory of the package or the online documentation at ...

Example:
```python
  # in a module named "one"

  from two import anotheradecoratedthing
  @adecorator
  def adecoratedthing(): pass

  # and scanning both modules
  scan('one')
  scan('two')

In this case you'd wind up with two repeated registrations for
"anotherdecoratedthing", which isn't what anyone expects.
```

...

</details>

### vercel-workers

Python SDK for Vercel Workers

`pip install vercel-workers` · installs (wheel) · licence: MIT · rank 2840 · last release 2026-06-20 · [PyPI](https://pypi.org/project/vercel-workers/)

<details><summary>README extract</summary>

Python SDK for Vercel Queues and Vercel Worker Services.

It includes:

- `send()` and `@subscribe` primitives for publishing and consuming queue messages
- adapters for Celery, Dramatiq, and Django tasks

Sections: vercel-workers, Worker Service deployment shape, Examples

</details>

### vl-convert-python

Convert Vega-Lite chart specifications to SVG, PNG, or Vega

`pip install vl-convert-python` · installs (wheel) · licence: BSD-3-Clause · rank 2974 · last release 2026-01-21 · [PyPI](https://pypi.org/project/vl-convert-python/)

<details><summary>README extract</summary>

Features:
`vl-convert-python` is a dependency-free Python package for converting Vega-Lite chart specifications into static images (SVG or PNG) or Vega chart specifications. ...

Example:
```python
import vl_convert as vlc
import json

vl_spec = r"""
{
  "$schema": "
  "data": {"url": "
  "mark": "circle",
  "encoding": {
    "x": {
      "bin": {"maxbins": 10},
      "field": "IMDB Rating"
    },
    "y": {
      "bin": {"maxbins": 10},
      "field": "Rotten Tomatoes Rating"
    },
    "size": {"aggregate": "count"}
  }
}
"""

...
```

Sections: Overview, Usage, Convert Vega-Lite to SVG, PNG, and Vega, Convert Altair Chart to SVG, PNG, and Vega, How it works

</details>

### vercel-internal-core

Shared internal runtime for Vercel Python packages

`pip install vercel-internal-core` · installs (wheel) · licence: MIT · rank 3772 · last release 2026-10-15 · [PyPI](https://pypi.org/project/vercel-internal-core/)

<details><summary>README extract</summary>

`vercel._internal.core` provides the shared runtime used by Vercel Python service
packages. It is installed as their dependency and is not intended for direct
installation or direct end-user imports.

The distribution contributes service-neutral namespace portions. ...

Example:
```python
from vercel.api import session
from vercel.errors import VercelError
```

Sections: Internal Core, Legacy HTTPX client migration

</details>

### verspec

Flexible version handling

`pip install verspec` · installs (wheel) · licence: BSD-3-Clause OR Apache-2.0 · rank 3883 · last release 2026-10-15 · [PyPI](https://pypi.org/project/verspec/)

<details><summary>README extract</summary>

verspec has been renamed to inversion. This package is
retained as an alias only to smooth the migration process.

</details>

### vhacdx

Python bindings for VHACD

`pip install vhacdx` · installs (wheel) · licence: not stated · rank 3908 · last release 2026-10-23 · [PyPI](https://pypi.org/project/vhacdx/)

<details><summary>README extract</summary>

Python bindings for V-HACD

A very simple and raw python binding for V-HACD that is forked from thomwolf/pyVHACD which generates an approximate convex decomposition of a triangle mesh.

Contains a single method: `output = compute_vhacd(points, faces)` which take as inputs: ...

</details>

### viser

3D visualization + Python

`pip install viser` · installs (wheel) · licence: MIT License · rank 3909 · last release 2026-09-15 · [PyPI](https://pypi.org/project/viser/) · [source](https://github.com/viser-project/viser)

<details><summary>README extract</summary>

Viser is a 3D visualization library for computer vision and robotics in Python.

Features include:

- API for visualizing 3D primitives.
- GUI building blocks: buttons, checkboxes, text inputs, sliders, etc.
- Scene interaction tools (clicks, selection, transform gizmos).
- Programmatic camera control and rendering. ...

</details>

### vaderSentiment

VADER Sentiment Analysis. VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media, and works well on texts from other domains.

`pip install vaderSentiment` · installs (wheel) · licence: MIT License · rank 4052 · last release 2020-05-22 · [PyPI](https://pypi.org/project/vaderSentiment/)

<details><summary>README extract</summary>

VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is *specifically attuned to sentiments expressed in social media*. It is fully open-sourced under the `[MIT License] < (we sincerely appreciate all attributions and readily accept most contributions, but please don't hold us liable). ...

</details>

### validate_email

Validate_email verify if an email address is valid and really exists.

`pip install validate_email` · installs from source (sdist only) · licence: LGPL · rank 4224 · last release 2015-03-23 · [PyPI](https://pypi.org/project/validate_email/)

_README extract left out: share-alike licence._

### vercel-queue

Vercel Queue client for Python

`pip install vercel-queue` · installs (wheel) · licence: MIT · rank 4266 · last release 2026-11-03 · [PyPI](https://pypi.org/project/vercel-queue/)

<details><summary>README extract</summary>

A Python client library for interacting with the Vercel Queues API,
designed for seamless integration with Vercel deployments.

Features:
- Simple API: `send`, `subscribe`, and `poll` cover standard workflows.
- Automatic Triggering on Vercel: Vercel invokes your function when messages are ready. ...

Example:
```python
from vercel.queue import send

message_id = await send("my-topic", {"message": "Hello world"})
```

Sections: Vercel Queues, Features, Quick Start, Publishing Messages, Receiving and Handling Messages, Auto-scaled push-mode on Vercel, Automatic Polling Loop, Manual Polling, Region Considerations when Polling, Retry and Backoff, Custom Client Configuration, Type-safe Message Passing and Streaming, Error Handling, Environment Variables

</details>

### virtualenv-clone

script to clone virtualenvs.

`pip install virtualenv-clone` · installs (wheel) · licence: MIT License · rank 4293 · last release 2021-09-07 · [PyPI](https://pypi.org/project/virtualenv-clone/)

<details><summary>README extract</summary>

virtualenv cloning script.

A script for cloning a non-relocatable virtualenv.

Virtualenv provides a way to make virtualenv's relocatable which could then be
copied as we wanted. ...

</details>

### vercel-sandbox

Python SDK for Vercel Sandbox

`pip install vercel-sandbox` · installs (wheel) · licence: MIT · rank 4353 · last release 2026-11-03 · [PyPI](https://pypi.org/project/vercel-sandbox/)

<details><summary>README extract</summary>

Create and manage Vercel Sandboxes with synchronous and asynchronous APIs.

The package can be installed independently with `pip install vercel-sandbox`.

Use `run_command()` to run a command to completion and `create_command()` to
start one and return a `Command` handle (`SyncCommand` synchronously).
`run_command()` returns a `CompletedCommand`. ...

Example:
```python
import subprocess

from vercel import sandbox
from vercel.api import session

async with session():
    async with sandbox.create_sandbox() as instance:
        process = await instance.run_command("echo", ["hello"], capture_output=True)
        print(process.stdout)

...
```

...

</details>

### vertexai

Please run pip install vertexai to use the Vertex SDK.

`pip install vertexai` · installs (wheel) · licence: Apache 2.0 · rank 4491 · last release 2024-10-31 · [PyPI](https://pypi.org/project/vertexai/) · [source](https://github.com/googleapis/python-aiplatform.git)

<details><summary>README extract</summary>

To use the Vertex GAPIC clients, please install the `google-cloud-aiplatform` PyPi package by running `pip install google-cloud-aiplatform`.

To use the Vertex AI SDK, please install the `vertexai` PyPi package by running `pip install vertexai`.

</details>

### vtracer

Python bindings for the Rust Vtracer raster-to-vector library

`pip install vtracer` · installs (wheel) · licence: MIT · rank 4618 · last release 2026-03-23 · [PyPI](https://pypi.org/project/vtracer/)

<details><summary>README extract</summary>

Raster to Vector Graphics Converter built on top of visioncortex

 Demo
 Download

Built with 🦀 by The Vision Cortex Research Group

visioncortex VTracer is an open source software to convert raster images (like jpg & png) into vector graphics (svg). It can vectorize graphics and photographs and trace the curves to output compact vector files. ...

Example:
```python
import vtracer

input_path = "/path/to/some_file.jpg"
output_path = "/path/to/some_file.vtracer.jpg"

# Minimal example: use all default values, generate a multicolor SVG
vtracer.convert_image_to_svg_py(inp, out)

# Single-color example. Good for line art, and much faster than full color:
...
```

Sections: VTracer: Python Binding, Article, Introduction, Usage (Python), Rust Library

</details>

### visions

Visions

`pip install visions` · installs (wheel) · licence: BSD-4-Clause · rank 4657 · last release 2026-05-26 · [PyPI](https://pypi.org/project/visions/) · [docs](https://dylan-profiler.github.io/visions) · [source](https://github.com/dylan-profiler/visions)

<details><summary>README extract</summary>

And these visions of data types, they kept us up past the dawn.

``Visions`` provides a set of tools for defining and using *semantic* data types.

- [x] Semantic type detection &
 inference on sequence data.

- [x] Automated data processing

- [x] Completely customizable. ...

Example:
```python
import pandas as pd

df = pd.read_csv("
df.head(2)
```

Sections: The Semantic Data Library, Quick Start Guide

</details>

### visitor

A tiny pythonic visitor implementation.

`pip install visitor` · installs from source (sdist only) · licence: MIT · rank 5184 · last release 2016-05-18 · [PyPI](https://pypi.org/project/visitor/)

<details><summary>README extract</summary>

A tiny library to facilitate visitor implementation in Python
(which are slightly peculiar due to dynamic typing). In fact, it is so small,
you may just be better off copy & pasting the source straight into your
project...

Example:
```python
from visitor import Visitor

class JSONEncoder(Visitor):
    def init(self):
        self.indent = 0

    def escape_str(self, s):
        # note: this is not a good escape function, do not use this in
        # production!
        s = s.replace('\\', '\\\\')
        s = s.replace('"', '\\"')
        return '"' + s + '"'

...
```

Sections: visitor, Example use

</details>

### vercel-workflow

Python SDK for Vercel Workflows

`pip install vercel-workflow` · installs (wheel) · licence: MIT · rank 5298 · last release 2026-11-03 · [PyPI](https://pypi.org/project/vercel-workflow/)

<details><summary>README extract</summary>

`vercel.workflow` provides Vercel Workflows primitives: `Workflows`, workflow
registration, step registration, durable sleeps, hooks, and `start`.

`wf.workflow` registers async workflow functions. `wf.step` registers async
steps that can be called only from inside a workflow. `sleep()` creates a
durable wait in a workflow run.

Example:
```python
from vercel.workflow import Workflows, sleep, start

wf = Workflows()

@wf.step
async def charge_customer(customer_id: str) -> None:
    ...

@wf.workflow
async def renew_subscription(customer_id: str) -> None:
    await sleep("1h")
    await charge_customer(customer_id)

async def main() -> None:
...
```

...

</details>

### volcengine-python-sdk

Volcengine SDK for Python (all services)

`pip install volcengine-python-sdk` · installs (wheel) · licence: Apache License 2.0 · rank 5367 · last release 2026-11-05 · [PyPI](https://pypi.org/project/volcengine-python-sdk/)

<details><summary>README extract</summary>

中文 | English

* Requirements
* Install
* Usage
* FAQ

Example:
```python
import volcenginesdkautoscaling
import volcenginesdkcore

configuration = volcenginesdkcore.Configuration()
configuration.client_side_validation = True  # 客户端是否进行参数校验
configuration.scheme = "https"  # https or http
configuration.debug = False  # 是否开启调试
configuration.logger_file = "sdk.log"

volcenginesdkcore.Configuration.set_default(configuration)
```

Sections: Volcengine SDK for Python, 目录, Requirements, Usage, 详细使用文档, Configuration Usage, Endpoint 设置, 完整示例, FAQ

</details>

### vasprun-xml

A python package for quick analysis of vasp calculation

`pip install vasprun-xml` · installs (wheel) · licence: MIT License · rank 5505 · last release 2022-02-14 · [PyPI](https://pypi.org/project/vasprun-xml/)

<details><summary>README extract</summary>

vasprun-xml is used for quick analysis of vasp calculation solely from vasprun.xml. It has the following features:

- band gap calculation
- dos plot (total dos / orbital partial dos / atomic partial dos)
- band structure plot (with color map enhancement)
- incar/potcar/poscar generation
- force analysys
- KS orbital eigenvalue analysys ...

</details>

### vale

Install and use Vale (grammar & style check tool) in python environments.

`pip install vale` · installs (wheel) · licence: MIT License · rank 6607 · last release 2026-11-02 · [PyPI](https://pypi.org/project/vale/)

<details><summary>README extract</summary>

> ⚠️ Vale is a software developed by errata.ai and a community of open-source
> contributors. This repository just makes that software available to Python
> users. The author is not affiliated nor endorsed by errata.ai.

Vale is a command-line tool that can enforce an editorial
style guide onto your text. It's written in Go. ...

</details>

### voluptuous-serialize

Convert voluptuous schemas to dictionaries

`pip install voluptuous-serialize` · installs (wheel) · licence: Apache-2.0 · rank 6631 · last release 2025-08-17 · [PyPI](https://pypi.org/project/voluptuous-serialize/) · [source](https://github.com/home-assistant-libs/voluptuous-serialize)

<details><summary>README extract</summary>

Convert Voluptuous schemas to json serializable objects.

becomes

_(dictionaries become lists to guarantee order of properties)_

See the tests for more examples.

Example:
```python
import voluptuous as vol
from voluptuous_serialize import convert

schema = vol.Schema(
    {
        vol.Required("name"): vol.All(str, vol.Length(min=5)),
        vol.Required("age"): vol.All(vol.Coerce(int), vol.Range(min=18)),
        vol.Optional("hobby", default="not specified"): str,
    }
)
result = convert(schema)
```

Sections: Voluptuous Serialize, Custom serializer

</details>

### vk-api

Python модуль для создания скриптов для социальной сети Вконтакте (vk.ru API wrapper)

`pip install vk-api` · installs (wheel) · licence: Apache-2.0 · rank 6737 · last release 2026-07-17 · [PyPI](https://pypi.org/project/vk-api/)

<details><summary>README extract</summary>

vk_api – Python модуль для создания скриптов для ВКонтакте (vk.ru API wrapper)

* Документация
* Примеры
* Чат в Telegram
* Документация по методам API
* Альтернативы vk_api (асинхронность; боты)

Example:
```python
import vk_api

vk_session = vk_api.VkApi('+71234567890', 'mypassword')
vk_session.auth()

vk = vk_session.get_api()

print(vk.wall.post(message='Hello world!'))
```

</details>

### voluptuous-openapi

Convert voluptuous schemas to OpenAPI Schema object

`pip install voluptuous-openapi` · installs (wheel) · licence: Apache-2.0 · rank 6758 · last release 2026-06-26 · [PyPI](https://pypi.org/project/voluptuous-openapi/) · [source](https://github.com/home-assistant-libs/voluptuous-openapi)

<details><summary>README extract</summary>

Convert Voluptuous schemas to OpenAPI Schema object.

becomes

See the tests for more examples.

Example:
```python
schema = {}
schema[vol.Required('name')] = vol.All(str, vol.Length(min=5))
schema[vol.Required('age', description='Age in full years')] = vol.All(vol.Coerce(int), vol.Range(min=18))
schema[vol.Optional('hobby', default='not specified')] = str
schema = vol.Schema(schema)
```

Sections: Voluptuous OpenAPI, Custom serializer

</details>

### vercel-blob

Python SDK for Vercel Blob

`pip install vercel-blob` · installs (wheel) · licence: MIT · rank 6862 · last release 2026-11-03 · [PyPI](https://pypi.org/project/vercel-blob/)

<details><summary>README extract</summary>

`vercel-blob` provides async object operations through `vercel.blob` and matching
sync operations through `vercel.blob.sync`.

Set `BLOB_READ_WRITE_TOKEN` to a read-write token for your store. On Vercel, you
can instead use OIDC credentials with `BLOB_STORE_ID`.

Use `access="public"` for a public store or `access="private"` for a private store. ...

Example:
```python
from vercel import blob

async def round_trip() -> None:
    uploaded = await blob.put_blob("hello.txt", b"hello, Blob!", access="public")
    try:
        result = await blob.get_blob(uploaded.url, access="public")
        print(result.metadata.content_type)
        print(result.body)
...
```

...

</details>

### vmodal

Thin Python SDK for the VMX external API

`pip install vmodal` · installs (wheel) · licence: MIT · rank 6869 · last release 2026-07-12 · [PyPI](https://pypi.org/project/vmodal/) · [docs](https://github.com/v-modal/vmodal_sdk/tree/main/sdk_python/docs/docs_ref) · [source](https://github.com/v-modal/vmodal_sdk)

<details><summary>README extract</summary>

Async-first Python SDK for the VMX external API. The SDK is published on
PyPI under the MIT License.

Example:
```python
from vmodal import SyncClient

client = SyncClient.from_env()
print(client.auth())
print(client.health())
```

Sections: vmodal Python SDK, Configure authentication, Verify authentication, Simple usage examples, More examples, Async usage, CLI

</details>

### vonage

Python Server SDK for using Vonage APIs

`pip install vonage` · installs (wheel) · licence: Apache Software License · rank 6978 · last release 2026-10-21 · [PyPI](https://pypi.org/project/vonage/)

<details><summary>README extract</summary>

The Vonage Python SDK Package `vonage` provides a streamlined interface for using Vonage APIs in Python projects. This package includes the `Vonage` class, which simplifies API interactions.

The Vonage class in this package serves as the main entry point for using Vonage APIs. ...

Example:
```python
from vonage import Vonage, Auth, HttpClientOptions

# Create an Auth instance
auth = Auth(api_key='your_api_key', api_secret='your_api_secret')

# Create HttpClientOptions instance
# (not required unless you want to change options from the defaults)
options = HttpClientOptions(api_host='api.nexmo.com', timeout=30)

# Create a Vonage instance
...
```

Sections: Vonage Python SDK, Usage

</details>

### vocos

Fourier-based neural vocoder for high-quality audio synthesis

`pip install vocos` · installs (wheel) · licence: not stated · rank 6982 · last release 2023-10-14 · [PyPI](https://pypi.org/project/vocos/)

<details><summary>README extract</summary>

Audio samples |
Paper [[abs]]( [[pdf]](

Vocos is a fast neural vocoder designed to synthesize audio waveforms from acoustic features. Trained using a Generative
Adversarial Network (GAN) objective, Vocos can generate waveforms in a single forward pass. Unlike other typical
GAN-based vocoders, Vocos does not model audio samples in the time domain. ...

Example:
```python
import torch

from vocos import Vocos

vocos = Vocos.from_pretrained("charactr/vocos-mel-24khz")

mel = torch.randn(1, 100, 256)  # B, C, T
audio = vocos.decode(mel)
```

Sections: Usage, Reconstruct audio from mel-spectrogram, Reconstruct audio from EnCodec tokens, Integrate with 🐶 Bark text-to-audio model, Pre-trained models, Training

</details>

### vonage-jwt

Tooling for working with JWTs for Vonage APIs in Python.

`pip install vonage-jwt` · installs (wheel) · licence: Apache Software License · rank 7038 · last release 2024-11-29 · [PyPI](https://pypi.org/project/vonage-jwt/)

<details><summary>README extract</summary>

This package (`vonage-jwt`) provides functionality to generate a JWT in Python code.

It is used by the Vonage Python SDK, specifically by the `vonage-http-client` package, to generate JWTs for authentication. Thus, it doesn't require manual installation or configuration unless you're using this package independently of an SDK. ...

Example:
```python
from vonage_jwt import JwtClient
```

Sections: Vonage JWT Generator for Python, Generating JWTs, Import the `JwtClient` object, Create a `JwtClient` object, Verifying a JWT signature

</details>

### vise

Package for handling io of vasp package in kumagai group at IMR, Tohoku university

`pip install vise` · installs (wheel) · licence: MIT License · rank 7195 · last release 2026-09-28 · [PyPI](https://pypi.org/project/vise/)

<details><summary>README extract</summary>

VASP Integrated Supporting Environment (vise) is a collection of tools that
supports VASP users to prepare input files for the VASP calculations, handle its calculation errors, and analyze its results.

Note1: Only ensure VASP ver5.4.4 or later so far. ...

Sections: vise, Bugs, requests and questions, Tests

</details>

### vonage-utils

Utils package containing objects for use with Vonage APIs

`pip install vonage-utils` · installs (wheel) · licence: Apache Software License · rank 7209 · last release 2024-10-21 · [PyPI](https://pypi.org/project/vonage-utils/)

<details><summary>README extract</summary>

This package contains utility code that is used by the Vonage Python SDK and other related packages.

The utils module provides two utility functions: `format_phone_number` and `remove_none_values`. It also exposes the `VonageError` type that other exceptions related to Vonage SDK inherit from. ...

Example:
```python
from utils import format_phone_number, remove_none_values

# Use format_phone_number
try:
    formatted_number = format_phone_number('123-456-7890')
    print(formatted_number)
except (InvalidPhoneNumberError, InvalidPhoneNumberTypeError) as e:
    print(e)

...
```

Sections: Vonage Utils Package, Usage

</details>

### vonage-messages

Vonage messages package

`pip install vonage-messages` · installs (wheel) · licence: Apache Software License · rank 7298 · last release 2026-10-21 · [PyPI](https://pypi.org/project/vonage-messages/)

<details><summary>README extract</summary>

This package contains the code to use Vonage's Messages API in Python.

Example:
```python
from vonage_messages import Sms

message = Sms(
    from='Vonage APIs',
    to='1234567890',
    text='This is a test message sent from the Vonage Python SDK',
)
```

Sections: Vonage Messages Package, Usage, How to Construct a Message, Send a message, Mark a WhatsApp Message as Read, Revoke an RCS Message, Message Models

</details>

### vonage-video

Vonage video package

`pip install vonage-video` · installs (wheel) · licence: Apache Software License · rank 7311 · last release 2026-10-21 · [PyPI](https://pypi.org/project/vonage-video/)

<details><summary>README extract</summary>

This package contains the code to use Vonage's Video API in Python. This package includes methods for working with video sessions, streams, signals, and more.

Example:
```python
from vonage_video import TokenOptions

token_options = TokenOptions(session_id='your_session_id', role='publisher')
client_token = vonage_client.video.generate_client_token(token_options)
```

Sections: Vonage Video API, Usage, Generate a Client Token, Create a Session, List Streams, Get a Stream, Change Stream Layout, Send a Signal, Disconnect a Client, Mute a Stream, Mute All Streams, Disable Mute All Streams, Start Captions, Stop Captions

</details>

### vonage-http-client

An HTTP client for making requests to Vonage APIs.

`pip install vonage-http-client` · installs (wheel) · licence: Apache Software License · rank 7352 · last release 2026-04-22 · [PyPI](https://pypi.org/project/vonage-http-client/)

<details><summary>README extract</summary>

This Python package provides a synchronous HTTP client for sending authenticated requests to Vonage APIs.

This package (`vonage-http-client`) is used by the `vonage` Python package and SDK so doesn't require manual installation or config unless you're using this package independently of a SDK. ...

Example:
```python
from vonage_http_client import HttpClient, HttpClientOptions
from vonage_http_client.auth import Auth

# Create an Auth instance
auth = Auth(api_key='your_api_key', api_secret='your_api_secret')

# Create HttpClientOptions instance
options = HttpClientOptions(api_host='api.nexmo.com', timeout=30)

# Create a HttpClient instance
...
```

...

</details>

### vonage-voice

Vonage voice package

`pip install vonage-voice` · installs (wheel) · licence: Apache Software License · rank 7364 · last release 2026-07-20 · [PyPI](https://pypi.org/project/vonage-voice/)

<details><summary>README extract</summary>

This package contains the code to use Vonage's Voice API in Python. This package includes methods for working with the Voice API. It also contains an NCCO (Call Control Object) builder to help you to control call flow.

There is a `Voice` class which contains the methods used to call Vonage APIs. ...

Example:
```python
from vonage import Vonage, Auth

vonage_client = Vonage(Auth('MY_AUTH_INFO'))
```

Sections: Vonage Voice Package, Structure, Usage, Create a Call, List Calls, Get Information About a Specific Call, Transfer a Call to a New NCCO, Transfer a Call to a New Answer URL, Hang Up a Call, Mute/Unmute a Participant, Earmuff/Unearmuff a UUID, Play Audio Into a Call, Stop Playing Audio Into a Call, Play TTS Into a Call

</details>

### vonage-sms

Vonage SMS package

`pip install vonage-sms` · installs (wheel) · licence: Apache Software License · rank 7371 · last release 2026-04-22 · [PyPI](https://pypi.org/project/vonage-sms/)

<details><summary>README extract</summary>

This package contains the code to use Vonage's SMS API in Python.

It includes a method for sending SMS messages and returns an `SmsResponse` class to handle the response.

Example:
```python
from vonage_sms import SmsMessage, SmsResponse

message = SmsMessage(to='1234567890', from='Acme Inc.', text='Hello, World!')
response: SmsResponse = vonage_client.sms.send(message)

print(response.model_dump(exclude_unset=True))
```

Sections: Vonage SMS Package, Usage, Send an SMS

</details>

### vonage-users

Vonage Users package

`pip install vonage-users` · installs (wheel) · licence: Apache Software License · rank 7375 · last release 2026-04-22 · [PyPI](https://pypi.org/project/vonage-users/)

<details><summary>README extract</summary>

This package contains the code to use Vonage's Users API in Python.

It includes methods for managing users.

Example:
```python
from vonage_users import ListUsersRequest

users, _ = vonage_client.users.list_users()

# With options
params = ListUsersRequest(
    page_size=10,
    cursor=my_cursor,
    order='desc',
)
users, next_cursor = vonage_client.users.list_users(params)
```

Sections: Vonage Users Package, Usage, List Users, Create a New User, Get a User, Update a User, Delete a User

</details>

### vonage-verify

Vonage verify package

`pip install vonage-verify` · installs (wheel) · licence: Apache Software License · rank 7376 · last release 2026-04-22 · [PyPI](https://pypi.org/project/vonage-verify/)

<details><summary>README extract</summary>

This package contains the code to use Vonage's Verify API in Python. This package includes methods for working with 2-factor authentication (2FA) messages sent via SMS, Voice, WhatsApp and Email. You can also make Silent Authentication requests with Verify to give your end user a more seamless experience.

Example:
```python
from vonage_verify import VerifyRequest, SmsChannel
# All channels have associated models
sms_channel = SmsChannel(to='1234567890')
params = {
    'brand': 'Vonage',
    'workflow': [sms_channel],
}
verify_request = VerifyRequest(**params)

response = vonage_client.verify.start_verification(verify_request)
```

Sections: Vonage Verify Package, Usage, Make a Verify Request, Check a Verification Code, Cancel a Verification, Trigger the Next Workflow Event

</details>

### vonage-application

Vonage Application API package

`pip install vonage-application` · installs (wheel) · licence: Apache Software License · rank 7379 · last release 2026-04-22 · [PyPI](https://pypi.org/project/vonage-application/)

<details><summary>README extract</summary>

This package contains the code to use Vonage's Application API in Python.

It includes methods for managing applications.

Example:
```python
from vonage_application import ListApplicationsFilter, ApplicationData

applications, next_page = vonage_client.application.list_applications()

# With options
options = ListApplicationsFilter(page_size=3, page=2)
applications, next_page = vonage_client.application.list_applications(options)
```

Sections: Vonage Application API Package, Usage, List Applications, Create a New Application, Get an Application, Update an Application, Delete an Application

</details>

### vonage-account

Vonage Account API package

`pip install vonage-account` · installs (wheel) · licence: Apache Software License · rank 7381 · last release 2026-04-22 · [PyPI](https://pypi.org/project/vonage-account/)

<details><summary>README extract</summary>

This package contains the code to use Vonage's Account API in Python.

It includes methods for managing Vonage accounts, managing account secrets and querying country pricing.

Example:
```python
balance = vonage_client.account.get_balance()
print(balance)
```

Sections: Vonage Account Package, Usage, Get Account Balance, Top-Up Account, Get Service Pricing for a Specific Country, Get Service Pricing for All Countries, Get Service Pricing by Dialing Prefix, Update the Default SMS Webhook, List Secrets Associated with the Account, Create a New Account Secret, Get Information About One Secret, Revoke a Secret

</details>

### vonage-verify-legacy

Vonage legacy verify package

`pip install vonage-verify-legacy` · installs (wheel) · licence: Apache Software License · rank 7383 · last release 2026-04-22 · [PyPI](https://pypi.org/project/vonage-verify-legacy/)

<details><summary>README extract</summary>

This package contains the code to use Vonage's legacy Verify API in Python. This package includes methods for working with 2-factor authentication (2FA) messages sent via SMS or TTS.

Note: There is a more current package available: Vonage's Verify API, which is recommended for most use cases. ...

Example:
```python
from vonage_verify_legacy import VerifyRequest
params = {'number': '1234567890', 'brand': 'Acme Inc.'}
request = VerifyRequest(**params)
response = vonage_client.verify_legacy.start_verification(request)
```

Sections: Vonage Legacy Verify Package, Usage, Make a Verify Request, Make a PSD2 (Payment Services Directive v2) Request, Check a Verification Code, Search Verification Requests, Cancel a Verification, Trigger the Next Workflow Event, Request a Network Unblock

</details>

### vonage-numbers

Vonage Numbers package

`pip install vonage-numbers` · installs (wheel) · licence: Apache Software License · rank 7387 · last release 2025-10-09 · [PyPI](https://pypi.org/project/vonage-numbers/)

<details><summary>README extract</summary>

This package contains the code to use Vonage's Numbers API in Python.

It includes methods for managing and buying numbers.

Example:
```python
numbers, count, next_page = vonage_client.numbers.list_owned_numbers()
print(numbers)
print(count)
print(next_page)

# With filtering
from vonage_numbers import ListOwnedNumbersFilter
numbers, count, next_page = vonage_client.numbers.list_owned_numbers(
    ListOwnedNumbersFilter(country='GB', size=3, index=2)
)

...
```

Sections: Vonage Numbers Package, Usage, List Numbers You Own, Search for Available Numbers, Buy a Number, Cancel a number, Update a Number

</details>

### vonage-number-insight

Vonage Number Insight package

`pip install vonage-number-insight` · installs (wheel) · licence: Apache Software License · rank 7393 · last release 2025-05-09 · [PyPI](https://pypi.org/project/vonage-number-insight/)

<details><summary>README extract</summary>

This package contains the code to use Vonage's Number Insight API in Python. This package includes methods to get information about phone numbers. It has 3 levels of insight: basic, standard, and advanced.

The advanced insight can be obtained synchronously or asynchronously. An async approach is recommended to avoid timeouts. ...

Example:
```python
from vonage_number_insight import BasicInsightRequest

response = vonage_client.number_insight.basic_number_insight(
    BasicInsightRequest(number='12345678900')
)

print(response.model_dump(exclude_none=True))
```

Sections: Vonage Number Insight Package, Usage, Make a Basic Number Insight Request, Make a Standard Number Insight Request, Make an Asynchronous Advanced Number Insight Request, Make a Synchronous Advanced Number Insight Request

</details>

### vonage-network-auth

Package for working with Network APIs that require Oauth2 in Python.

`pip install vonage-network-auth` · installs (wheel) · licence: Apache Software License · rank 7395 · last release 2024-11-29 · [PyPI](https://pypi.org/project/vonage-network-auth/)

<details><summary>README extract</summary>

This package (`vonage-network-auth`) provides a client for authenticating Network APIs that require Oauth2 authentication. Using it, it is possible to generate authenticated JWTs for use with Vonage Network APIs, e.g. Sim Swap, Number Verification. ...

Example:
```python
from vonage_network_auth import NetworkAuth
from vonage_http_client import HttpClient, Auth

network_auth = NetworkAuth(HttpClient(Auth(application_id='application-id', private_key='private-key')))
```

Sections: Vonage Network API Authentication Client, Usage, Create a `NetworkAuth` Object

</details>

### vonage-subaccounts

Vonage Subaccounts API package

`pip install vonage-subaccounts` · installs (wheel) · licence: Apache Software License · rank 7398 · last release 2024-11-06 · [PyPI](https://pypi.org/project/vonage-subaccounts/)

<details><summary>README extract</summary>

This package contains the code to use Vonage's Subaccount API in Python.

It includes methods for creating and modifying Vonage subaccounts and transferring credit, balances and numbers between subaccounts.

Example:
```python
response = vonage_client.subaccounts.list_subaccounts()
print(response.model_dump)
```

Sections: Vonage Subaccount Package, Usage, List Subaccounts, Create Subaccount, Modify a Subaccount, List Balance Transfers, Transfer Balance Between Subaccounts, List Credit Transfers, Transfer Credit Between Subaccounts, Transfer a Phone Number Between Subaccounts

</details>

### vonage-network-sim-swap

Package for working with the Vonage Sim Swap Network API.

`pip install vonage-network-sim-swap` · installs (wheel) · licence: Apache Software License · rank 7399 · last release 2024-11-29 · [PyPI](https://pypi.org/project/vonage-network-sim-swap/)

<details><summary>README extract</summary>

This package (`vonage-network-sim-swap`) allows you to check whether a SIM card has been swapped, and the last swap date.

This package is not intended to be used directly, instead being accessed from an enclosing SDK package. Thus, it doesn't require manual installation or configuration unless you're using this package independently of an SDK. ...

Example:
```python
from vonage_network_sim_swap import SwapStatus
swap_status: SwapStatus = vonage_client.sim_swap.check(phone_number='MY_NUMBER')
print(swap_status.swapped)
```

Sections: Vonage Sim Swap Network API Client, Registering to Use the Sim Swap API, Usage, Check if a SIM Has Been Swapped, Get the Date of the Last SIM Swap

</details>

### vonage-network-number-verification

Package for working with the Vonage Number Verification Network API.

`pip install vonage-network-number-verification` · installs (wheel) · licence: Apache Software License · rank 7400 · last release 2024-11-29 · [PyPI](https://pypi.org/project/vonage-network-number-verification/)

<details><summary>README extract</summary>

This package (`vonage-network-number-verification`) allows you to verify a mobile device. It verifies the phone number linked to the SIM card in a device which is connected to a mobile data network, without any user input.

This package is not intended to be used directly, instead being accessed from an enclosing SDK package. ...

Example:
```python
from vonage_network_number_verification import CreateOidcUrl

url_options = CreateOidcUrl(
    redirect_uri='
    state='c9896ee6-4ff8-464c-b393-d56d6e638f88',
    login_hint='+990123456',
)

url = number_verification.get_oidc_url(url_options)
print(url)
```

Sections: Vonage Number Verification Network API Client, Registering to Use the Network Number Verification API, Usage, Get an OIDC URL, Make a Number Verification Request

</details>

### varname

Dark magics about variable names in python.

`pip install varname` · installs (wheel) · licence: MIT · rank 7494 · last release 2026-04-16 · [PyPI](https://pypi.org/project/varname/) · [source](https://github.com/pwwang/python-varname)

<details><summary>README extract</summary>

[][4] [][6] [][4]
[][15] [][13] [][13]

Dark magics about variable names in python

CHANGELOG | API | Playground | :fire: StackOverflow answer

Features:
- Retrieving names of variables a function/class call is assigned to from inside it, using `varname`.
 - Detecting next immediate attribute name, using `will`
 - Fetching argument names/sources passed to a function using `argname` ...

Example:
```python
from varname import varname
def function():
    return varname()

func = function()  # func == 'func'
```

...

</details>

### vt-py

The official Python client library for VirusTotal

`pip install vt-py` · installs (wheel) · licence: Apache Software License · rank 7551 · last release 2025-10-28 · [PyPI](https://pypi.org/project/vt-py/)

<details><summary>README extract</summary>

This is the official Python client library for VirusTotal. With this library
you can interact with the VirusTotal REST API v3
and automate your workflow quickly and efficiently. ...

Sections: vt-py, Things you can do with vt-py

</details>

### volcengine

The Volcengine SDK for Python

`pip install volcengine` · installs (wheel) · licence: MIT License · rank 7906 · last release 2026-10-15 · [PyPI](https://pypi.org/project/volcengine/)

### vsdx

vsdx - A python library for processing .vsdx files

`pip install vsdx` · installs (wheel) · licence: BSD License · rank 7937 · last release 2026-01-04 · [PyPI](https://pypi.org/project/vsdx/) · [docs](https://vsdx.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

__.vsdx files can be processed in two ways, directly via python code as in
example 1 below, or indirectly using a jinja template as in example 2__

For quick start documentation please see

Example 1 code to find a shape with specific text, remove it, and
then save the updated .vsdx file: ...

Example:
```python
from vsdx import VisioFile

filename = 'my_file.vsdx'
# open a visio file
with VisioFile(filename) as vis:
  # find shape by its text on first page
  shape = vis.pages[0].find_shape_by_text('Shape to remove')
  # remove the shape if found
  if shape:
    shape.remove()
    # save a new copy
    vis.save_vsdx('shape_removed.vsdx')
```

</details>

### validate-docbr

Validate brazilian documents.

`pip install validate-docbr` · installs (wheel) · licence: MIT · rank 8589 · last release 2026-10-01 · [PyPI](https://pypi.org/project/validate-docbr/) · [docs](https://alvarofpp.github.io/validate-docbr) · [source](https://github.com/alvarofpp/validate-docbr)

<details><summary>README extract</summary>

Pacote Python para validação de documentos brasileiros.

Para instalar o pacote:

Ou com uv:

A documentação pode ser acessada
clicando aqui.

Documentos que estão no pacote:

- CPF: Cadastro de Pessoas Físicas;
- CNH: Carteira Nacional de Habilitação;
- CNPJ: Cadastro Nacional da Pessoa
 Jurídica (numérico e alfanumérico); ...

Example:
```python
from validate_docbr import CPF

cpf = CPF()

# Validar CPF
cpf.validate("012.345.678-90")  # True
cpf.validate("012.345.678-91")  # False
```

Sections: validate-docbr, Documentos, Métodos, validate, validate_list, validate_docs, generate, generate_list, mask, Testes

</details>

### vodozemac

Python bindings for vodozemac

`pip install vodozemac` · installs (wheel) · licence: not stated · rank 8796 · last release 2026-07-23 · [PyPI](https://pypi.org/project/vodozemac/) · [source](https://github.com/matrix-nio/vodozemac-python)

### vonage-identity-insights

Vonage Identity Insights package

`pip install vonage-identity-insights` · installs (wheel) · licence: Apache Software License · rank 8951 · last release 2026-04-22 · [PyPI](https://pypi.org/project/vonage-identity-insights/)

<details><summary>README extract</summary>

This package contains the code to use the Vonage Identity Insights API in Python. The API provides real-time access to a broad range of attributes related to the carrier, subscriber, or device associated with a phone number. To use it you will need a Vonage account. Sign up for free at vonage.com.

Example:
```python
from vonage import Vonage, Auth, HttpClientOptions
from vonage_identity_insights import (
    IdentityInsightsRequest,
    InsightsRequest,
    EmptyInsight,
    SimSwapInsight,
)

options = HttpClientOptions(api_host="api-eu.vonage.com", timeout=30)

client = Vonage(auth=auth, http_client_options=options)

request = IdentityInsightsRequest(
...
```

Sections: Vonage Identity Insights Package, Usage, Make a Standard Identity Insights Request

</details>

### vanna

Generate SQL queries from natural language

`pip install vanna` · installs (wheel) · licence: MIT License · rank 9024 · last release 2026-02-02 · [PyPI](https://pypi.org/project/vanna/)

<details><summary>README extract</summary>

Natural language → SQL → Answers. Now with enterprise security and user-aware permissions.

🔐 User-Aware at Every Layer — Queries automatically filtered per user permissions

🎨 Modern Web Interface — Beautiful pre-built `<vanna-chat>` component

⚡ Streaming Responses — Real-time tables, charts, and progress updates ...

Example:
```python
from fastapi import FastAPI
from vanna import Agent
from vanna.servers.fastapi.routes import register_chat_routes
from vanna.servers.base import ChatHandler
from vanna.core.user import UserResolver, User, RequestContext
from vanna.integrations.anthropic import AnthropicLlmService
from vanna.tools import RunSqlTool
...
```

...

</details>

### verovio

A library and toolkit for engraving MEI music notation into SVG

`pip install verovio` · installs (wheel) · licence: LGPL-3.0-only · rank 9477 · last release 2026-11-03 · [PyPI](https://pypi.org/project/verovio/) · [source](https://github.com/rism-digital/verovio)

_README extract left out: share-alike licence._

### vibium-linux-x64

Vibium binary for Linux x64

`pip install vibium-linux-x64` · installs (wheel) · licence: Apache-2.0 · rank 9618 · last release 2026-08-22 · [PyPI](https://pypi.org/project/vibium-linux-x64/) · [source](https://github.com/VibiumDev/vibium)

<details><summary>README extract</summary>

Vibium binary for Linux x64.

This package is automatically installed as a dependency of the main `vibium` package on Linux x64 systems.

Sections: vibium-linux-x64, Usage

</details>

### vibium

Browser automation for AI agents and humans

`pip install vibium` · installs (wheel) · licence: Apache-2.0 · rank 9630 · last release 2026-08-22 · [PyPI](https://pypi.org/project/vibium/) · [source](https://github.com/VibiumDev/vibium)

<details><summary>README extract</summary>

Browser automation for AI agents and humans.

Example:
```python
from vibium import browser

bro = browser.start()
vibe = bro.page()
vibe.go("

# Take a screenshot
png = vibe.screenshot()
with open("screenshot.png", "wb") as f:
    f.write(png)

# Find and click a link
link = vibe.find("a")
print(link.text())
link.click()

bro.stop()
```

Sections: Vibium, Quick Start, Async API, CLI, Requirements, Links

</details>

### vastai

CLI and SDK for Vast.ai GPU Cloud Service

`pip install vastai` · installs (wheel) · licence: MIT License · rank 9967 · last release 2026-11-04 · [PyPI](https://pypi.org/project/vastai/) · [source](https://github.com/vast-ai/vast-cli)

<details><summary>README extract</summary>

Provides both the CLI and SDK for managing Vast.ai GPU cloud resources, plus a serverless client for endpoint inference.

Example:
```python
from vastai import VastAI

vast = VastAI()  # uses VAST_API_KEY env var, or pass api_key="..."

vast.search_offers(query='gpu_name=RTX_4090 num_gpus>=4')
vast.show_instances()
vast.start_instance(id=12345)
vast.stop_instance(id=12345)
```

Sections: Vast.ai Python SDK & CLI, Quickstart, CLI Usage, SDK Usage, Using the Serverless Client, AI Agents

</details>

### vininfo

Extracts useful information from Vehicle Identification Number (VIN)

`pip install vininfo` · installs (wheel) · licence: BSD-3-Clause · rank 9981 · last release 2026-05-02 · [PyPI](https://pypi.org/project/vininfo/)

<details><summary>README extract</summary>

*Extracts useful information from Vehicle Identification Number (VIN)*

* Can be used as a standalone console application (CLI).
* One can also use import it as any other package in your Python code.
* Gives basic and detailed info (is available) about VIN.
* Allows VIN checksum verification.

Additional info available for many vehicles from: ...

Sections: vininfo, Description, Requirements, Usage, CLI, Python, Quickstart

</details>

### validations-engine

Engine for creating and running validation suites for general purposes

`pip install validations-engine` · installs (wheel) · licence: not stated · rank 10053 · last release 2023-11-16 · [PyPI](https://pypi.org/project/validations-engine/)

<details><summary>README extract</summary>

_Engine for creating and running validations for general purposes._


| Source | Downloads | Page | Installation Command |

| PyPi | | Link | `pip install validations-engine ` |

Sections: Validations Engine, Purpose, Structure and the engine core concepts

</details>

### voila

Voilà turns Jupyter notebooks into standalone web applications

`pip install voila` · installs (wheel) · licence: BSD License · rank 10788 · last release 2026-09-04 · [PyPI](https://pypi.org/project/voila/)

<details><summary>README extract</summary>

Rendering of live Jupyter notebooks with interactive widgets.

Voilà turns Jupyter notebooks into standalone web applications.

Unlike the usual HTML-converted notebooks, each user connecting to the Voilà
tornado application gets a dedicated Jupyter kernel which can execute the
callbacks to changes in Jupyter interactive widgets. ...

Sections: Introduction, JupyterLab preview extension, Usage, As a standalone tornado application, As a server extension to `notebook` or `jupyter_server`, Documentation, Examples, Showing the source code for a Voilà notebook, Voilà dashboards with other language kernels\*\, The Voilà Gallery, Related projects

</details>

### virtualenvwrapper

(no summary)

`pip install virtualenvwrapper` · installs (wheel) · licence: MIT License · rank 10902 · last release 2024-10-13 · [PyPI](https://pypi.org/project/virtualenvwrapper/) · [source](https://github.com/python-virtualenvwrapper/virtualenvwrapper)

<details><summary>README extract</summary>

.. -*- mode: rst -*-

virtualenvwrapper

virtualenvwrapper is a set of extensions to Ian Bicking's `virtualenv
< tool. The extensions include
wrappers for creating and deleting virtual environments and otherwise
managing your development workflow, making it easier to work on more
than one project at a time without introducing conflicts in ...

Features:
1. Organizes all of your virtual environments in one place.

2. Wrappers for creating, copying and deleting environments, including
 user-configurable hooks.

3. Use a single command to switch between environments.

4. ...

Sections: #, Features, Python Versions, Shell Aliases

</details>

### vyper

Vyper: the Pythonic Programming Language for the EVM

`pip install vyper` · installs (wheel) · licence: Apache Software License · rank 10992 · last release 2025-06-18 · [PyPI](https://pypi.org/project/vyper/)

<details><summary>README extract</summary>

Sections: Getting Started, Compiling a contract

</details>

### vega-datasets

A Python package for offline access to Vega datasets

`pip install vega-datasets` · installs (wheel) · licence: MIT License · rank 11091 · last release 2020-11-26 · [PyPI](https://pypi.org/project/vega-datasets/) · [source](https://github.com/altair-viz/vega_datasets)

<details><summary>README extract</summary>

A Python package for offline access to vega datasets.

This package has several goals:

- Provide straightforward access in Python to the datasets made available at vega-datasets.
- return the results in the form of a Pandas dataframe. ...

Example:
```python
>>> from vega_datasets import data
```

Sections: vega_datasets, Usage, Available Datasets, Dataset Information

</details>

### vmecpp

Proxima Fusion's reimplementation of the Variational Moments Equilibrium Code (VMEC), a free-boundary ideal-MHD equilibrium solver for stellarators and Tokamaks.

`pip install vmecpp` · installs (wheel) · licence: MIT · rank 12008 · last release 2026-11-06 · [PyPI](https://pypi.org/project/vmecpp/) · [docs](https://github.com/proximafusion/vmecpp#readme) · [source](https://github.com/proximafusion/vmecpp)

<details><summary>README extract</summary>

VMEC++ is a Python-friendly, from-scratch reimplementation in C++ of the Variational Moments Equilibrium Code (VMEC),
a free-boundary ideal-MHD equilibrium solver for stellarators and tokamaks.

The original version was written by Steven P. Hirshman and colleagues in the 1980s and 1990s. ...

Example:
```python
import vmecpp

vmec_input = vmecpp.VmecInput.from_file("examples/data/w7x.json")

# Base run
vmec_output = vmecpp.run(vmec_input)

# Now let's perturb the plasma boundary a little bit...
ntor = vmec_input.ntor
vmec_input.rbc[0, ntor+0] *= 1.0 + 1.0e-6 # m=0, n=0
vmec_input.rbc[1, ntor+0] *= 1.0 - 1.0e-6 # m=1, n=0
...
```

...

</details>

### vention-sim-grpc-py-sdk

Generated Python gRPC clients for the Vention simulation protos

`pip install vention-sim-grpc-py-sdk` · installs (wheel) · licence: Proprietary · rank 12134 · last release 2026-11-06 · [PyPI](https://pypi.org/project/vention-sim-grpc-py-sdk/) · [source](https://github.com/VentionCo/simulation)

<details><summary>README extract</summary>

Generated Python gRPC clients for the Vention simulation protos (`physics/**` and
`vention/simulation/**` under `libs/proto/`), published from this repo.

Example:
```python
import grpc

from vention.robots.v1.joint_trajectory_point_pb2 import JointTrajectoryPoint
from vention_sim import SIMULATION_SHA, VENTION_PROTOS_SHA, version
from vention_sim.simulation.v1.sim_robot_driver_commands_pb2 import StartTrajectoryRequest
...
```

Sections: vention-sim-grpc-py-sdk, Use, Import root, One package per proto source, Versions

</details>

### visualdl

Visualize Deep Learning

`pip install visualdl` · installs (wheel) · licence: Apache License · rank 12189 · last release 2023-06-05 · [PyPI](https://pypi.org/project/visualdl/)

<details><summary>README extract</summary>

VisualDL, a visualization analysis tool of PaddlePaddle, provides a variety of charts to show the trends of parameters, and visualizes model structures, data samples, histograms of tensors, PR curves , ROC curves and high-dimensional data distributions. ...

Example:
```python
from visualdl import LogWriter

# create a log file under `./log/scalar_test/train`
with LogWriter(logdir="./log/scalar_test/train") as writer:
    # use `add_scalar` to record scalar values
    writer.add_scalar(tag="acc", step=1, value=0.5678)
    writer.add_scalar(tag="acc", step=2, value=0.6878)
...
```

...

</details>

### voxcpm

VoxCPM: Tokenizer-Free TTS for Context-Aware Speech Generation and True-to-Life Voice Cloning

`pip install voxcpm` · installs (wheel) · licence: Apache-2.0 · rank 12227 · last release 2026-05-11 · [PyPI](https://pypi.org/project/voxcpm/) · [docs](https://github.com/OpenBMB/VoxCPM#readme) · [source](https://github.com/OpenBMB/VoxCPM.git)

<details><summary>README extract</summary>

English | 中文

 👋 Join our community for discussion and support!

 Feishu


 Discord

VoxCPM is a tokenizer-free Text-to-Speech system that directly generates continuous speech representations via an end-to-end diffusion autoregressive architecture, bypassing discrete tokenization to achieve highly natural and expressive synthesis. ...

Example:
```python
from voxcpm import VoxCPM
import soundfile as sf

model = VoxCPM.from_pretrained(
  "openbmb/VoxCPM2",
  load_denoiser=False,
)

wav = model.generate(
    text="VoxCPM2 is the current recommended release for realistic multilingual speech synthesis.",
    cfg_value=2.0,
    inference_timesteps=10,
)
...
```

...

</details>

### vat-utils

(no summary)

`pip install vat-utils` · installs (wheel) · licence: not stated · rank 12426 · last release 2023-10-10 · [PyPI](https://pypi.org/project/vat-utils/)

### versioneer-518

Just the vendored file

`pip install versioneer-518` · installs (wheel) · licence: public domain · rank 12647 · last release 2021-04-01 · [PyPI](https://pypi.org/project/versioneer-518/)

### volue-insight-timeseries

Volue Data & Forecasts API python library

`pip install volue-insight-timeseries` · installs (wheel) · licence: MIT · rank 12734 · last release 2026-11-05 · [PyPI](https://pypi.org/project/volue-insight-timeseries/) · [docs](https://docs.volue.com/data-and-forecasts/volue-insight-timeseries/) · [source](https://github.com/Volue-Public/volue-insight-timeseries)

<details><summary>README extract</summary>

Python library for the Volue Data & Forecasts Timeseries API. You need a Volue Data & Forecasts account. Documentation:

</details>

### velocity-profile

Module for calculating velocity profile

`pip install velocity-profile` · installs (wheel) · licence: Apache Software License · rank 12948 · last release 2024-06-13 · [PyPI](https://pypi.org/project/velocity-profile/) · [source](https://github.com/DiamondLightSource/velocity-profile)

<details><summary>README extract</summary>

Module for calculating velocity profile

Source | <

PyPI | `pip install velocity-profile`
Releases | <

</details>

### virustotal3

Python 3 implementation of the VirusTotal v3 API

`pip install virustotal3` · installs from source (sdist only) · licence: not stated · rank 13020 · last release 2020-08-17 · [PyPI](https://pypi.org/project/virustotal3/)

<details><summary>README extract</summary>

virustotal3 provides an easy way to use VirusTotal version 3 REST endpoints, including those exclusive to VirusTotal Enterprise such as Live Hunt, Retro Hunt and Zip Files that were not available in version 2.

Example:
```python
import os
import virustotal3.enterprise

API_KEY = os.environ['VT_API']

livehunt = virustotal3.enterprise.Livehunt(API_KEY)

rulesets = livehunt.get_rulesets()

print(rulesets)
```

Sections: virustotal3, 1.0.8, Documentation, Usage example

</details>

### vastai-sdk

DEPRECATED — use 'pip install vastai' instead. This package is a compatibility wrapper that installs vastai.

`pip install vastai-sdk` · installs (wheel) · licence: not stated · rank 13108 · last release 2026-11-04 · [PyPI](https://pypi.org/project/vastai-sdk/) · [source](https://github.com/vast-ai/vast-cli)

<details><summary>README extract</summary>

> This package is deprecated. It has been merged into vast-ai/vast-cli. `pip install vastai` now installs both the SDK and CLI in a single package. `pip install vastai-sdk` still works and installs the same package. For issues and PRs, go to vast-ai/vast-cli.

Example:
```python
from vastai_sdk import VastAI
vast = VastAI(api_key="YOUR_API_KEY")
```

Sections: Vast.ai Python SDK, Quickstart, SDK Usage, Using the Serverless Client

</details>

### vismatch

Easily test and apply pairwise image matching models

`pip install vismatch` · installs (wheel) · licence: BSD License · rank 13236 · last release 2026-10-15 · [PyPI](https://pypi.org/project/vismatch/) · [source](https://github.com/gmberton/vismatch)

<details><summary>README extract</summary>

Vis(ion)Match(ers) is a unified API for quickly and easily trying 50+ (and growing!) image matching models.

Jump to: Install | Use | Models | Add a Model / Contributing | Acknowledgements | Cite | Download Stats | Documentation

Example:
```python
from vismatch import get_matcher
from vismatch.viz import plot_matches, plot_keypoints

# Choose any of the 50+ matchers listed below
matcher = get_matcher("superpoint-lightglue", device="cuda")
img_size = 512  # optional

img0 = matcher.load_image("vismatch/assets/example_pairs/outdoor/montmartre_close.jpg", resize=img_size)
...
```

...

</details>

### volatility3

Memory forensics framework

`pip install volatility3` · installs (wheel) · licence: VSL · rank 13340 · last release 2026-09-17 · [PyPI](https://pypi.org/project/volatility3/) · [docs](https://volatility3.readthedocs.io/) · [source](https://github.com/volatilityfoundation/volatility3)

<details><summary>README extract</summary>

Volatility is the world's most widely used framework for extracting digital
artifacts from volatile memory (RAM) samples. The extraction techniques are
performed completely independent of the system being investigated but offer
visibility into the runtime state of the system. ...

Sections: Volatility 3: The volatile memory extraction framework, Quick Start, Symbol Tables, Documentation, Licensing and Copyright, Contact

</details>

### vcdvcd

Python Verilog value change dump (VCD) parser library + the nifty vcdcat VCD command line viewer

`pip install vcdvcd` · installs (wheel) · licence: not stated · rank 14056 · last release 2025-10-19 · [PyPI](https://pypi.org/project/vcdvcd/)

<details><summary>README extract</summary>

= vcdvcd
:idprefix:
:idseparator: -
:sectanchors:
:sectlinks:
:sectnumlevels: 6
:sectnums:
:toc: macro
:toclevels: 6
:toc-title:

Python Verilog value change dump (VCD) parser library + the nifty <<vcdcat>> VCD command line pretty printer.

toc::[]

== Installation

Since Ubuntu 23.04 you to use pipx] as:

....
pipx install vcdvcd
.... ...

Sections: 0 1 2 3 4 5, 0 1 2, Do the parsing., List all human readable signal names., View all signal data., Get a signal by human readable name., tv is a list of Time/Value delta pairs for this signal., Random access value of the signal at a given time., Note how it works for times between deltas as well.

</details>

### vecs

pgvector client

`pip install vecs` · installs from source (sdist only) · licence: MIT · rank 14199 · last release 2024-12-13 · [PyPI](https://pypi.org/project/vecs/)

<details><summary>README extract</summary>

Documentation:

Source Code:

`vecs` is a python client for managing and querying vector stores in PostgreSQL with the pgvector extension. This guide will help you get started with using vecs.

If you don't have a Postgres database with the pgvector ready, see hosting for easy options.

Example:
```python
import vecs

DB_CONNECTION = "postgresql://:@:/"

# create vector store client
vx = vecs.create_client(DB_CONNECTION)

# create a collection of vectors with 3 dimensions
docs = vx.get_or_create_collection(name="docs", dimension=3)

# add records to the *docs* collection
docs.upsert(
    records=[
        (
...
```

Sections: vecs, Usage

</details>

### vsa

Video Sparse Attention Kernel Used in FastVideo

`pip install vsa` · does not install on CPython 3.14 · licence: Apache Software License · rank 14343 · last release 2025-11-13 · [PyPI](https://pypi.org/project/vsa/)

### vulture-rs

Rust reimplementation of vulture (dead code finder) - output-identical to vulture 2.13

`pip install vulture-rs` · installs (wheel) · licence: MIT License · rank 14880 · last release 2026-07-15 · [PyPI](https://pypi.org/project/vulture-rs/)

<details><summary>README extract</summary>

A Rust reimplementation of
vulture (the Python
dead-code finder), built on the
ruff parser for performance.
Versioned independently; the upstream parity target (currently
vulture 2.13) is stated here, in the package description, and in
the `CHANGELOG` (a dated entry per release, enforced at release
time). ...

Sections: vulture-rs, Results, Parity, Build & test, Usage

</details>

### vercel-celery

Celery integration for Vercel Queue and Runtime Cache

`pip install vercel-celery` · installs (wheel) · licence: MIT · rank 14897 · last release 2026-11-03 · [PyPI](https://pypi.org/project/vercel-celery/)

<details><summary>README extract</summary>

Celery integration for Vercel Queue Service and Vercel Runtime Cache.

This package provides a Celery broker transport backed by Vercel Queue Service
and a Celery result backend backed by Vercel Runtime Cache.

By default, named Celery apps publish to app-prefixed Vercel Queue topics. ...

Example:
```python
from vercel.integrations.celery import install_vercel_celery_integration

install_vercel_celery_integration()
```

</details>

### valyu

Deepsearch API for AI.

`pip install valyu` · installs (wheel) · licence: MIT License · rank 14952 · last release 2026-10-31 · [PyPI](https://pypi.org/project/valyu/)

<details><summary>README extract</summary>

Search and research APIs built for AI agents. Access web and proprietary data sources through Search, extract content from URLs, generate grounded answers, and run multi-step research with DeepResearch - all through a single SDK.

Documentation | API Reference | Platform

Example:
```python
from valyu import Valyu

valyu = Valyu()  # uses VALYU_API_KEY env var

response = valyu.search(
    "latest advances in transformer architectures",
    max_num_results=5,
    search_type="all",
)

for result in response.results:
    print(result.title, result.url)
```

Sections: Valyu Python SDK, Quick Start, APIs, Search, Answer, DeepResearch, Batch, Workflows, Data Sources, Authentication, Type Safety, Error Handling, Rate limits, Integrations

</details>

