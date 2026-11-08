# Unclassified / H

[Index](README.md) · 119 packages in this topic, by downloads.

### httptools

A collection of framework independent HTTP protocol utils.

`pip install httptools` · installs (wheel) · licence: MIT · rank 124 · last release 2026-10-09 · [PyPI](https://pypi.org/project/httptools/)

<details><summary>README extract</summary>

httptools is a Python binding for the nodejs HTTP parser.

The package is available on PyPI: `pip install httptools`.

httptools contains two classes `httptools.HttpRequestParser`,
`httptools.HttpResponseParser` (fulfilled through
llhttp) and a function for
parsing URLs `httptools.parse_url` (through
http-parse for now).
See unittests for examples.

Example:
```python
class HttpRequestParser:

    def init(self, protocol):
        """HttpRequestParser

        protocol -- a Python object with the following methods
        (all optional):

          - on_message_begin()
          - on_url(url: bytes)
          - on_header(name: bytes, value: bytes)
          - on_headers_complete()
...
```

</details>

### httpx-sse

Consume Server-Sent Event (SSE) messages with HTTPX.

`pip install httpx-sse` · installs (wheel) · licence: MIT · rank 168 · last release 2025-10-10 · [PyPI](https://pypi.org/project/httpx-sse/)

<details><summary>README extract</summary>

Consume Server-Sent Event (SSE) messages with HTTPX.

Table of contents

- Installation
- Quickstart
- How-To
- API Reference

Example:
```python
import httpx
from httpx_sse import connect_sse

with httpx.Client() as client:
    with connect_sse(client, "GET", " as event_source:
        for sse in event_source.iter_sse():
            print(sse.event, sse.data, sse.id, sse.retry)
```

Sections: httpx-sse, Quickstart, How-To, Calling into Python web apps, Handling reconnections, API Reference, `connect_sse`, `aconnect_sse`, `EventSource`, `response`, `iter_sse`, `aiter_sse`, `ServerSentEvent`, `SSEError`

</details>

### h2

Pure-Python HTTP/2 protocol implementation

`pip install h2` · installs (wheel) · licence: MIT · rank 177 · last release 2026-08-03 · [PyPI](https://pypi.org/project/h2/) · [docs](https://python-hyper.org/) · [source](https://github.com/python-hyper/h2/)

### hpack

Pure-Python HPACK header encoding

`pip install hpack` · installs (wheel) · licence: MIT · rank 179 · last release 2026-06-23 · [PyPI](https://pypi.org/project/hpack/) · [docs](https://python-hyper.org/) · [source](https://github.com/python-hyper/hpack/)

<details><summary>README extract</summary>

This module contains a pure-Python HTTP/2 header encoding (HPACK) logic for use
in Python programs that implement HTTP/2.

Documentation is available at .

Quickstart:

Example:
```python
from hpack import Encoder, Decoder

headers = [
    (':method', 'GET'),
    (':path', '/jimiscool/'),
    ('X-Some-Header', 'some_value'),
]

e = Encoder()
encoded_bytes = e.encode(headers)

d = Decoder()
decoded_headers = d.decode(encoded_bytes)
```

Sections: hpack: HTTP/2 Header Encoding for Python, Documentation

</details>

### hyperframe

Pure-Python HTTP/2 framing

`pip install hyperframe` · installs (wheel) · licence: MIT License · rank 182 · last release 2025-01-22 · [PyPI](https://pypi.org/project/hyperframe/) · [docs](https://python-hyper.org/) · [source](https://github.com/python-hyper/hyperframe/)

<details><summary>README extract</summary>

This library contains the HTTP/2 framing code used in the hyper project. It
provides a pure-Python codebase that is capable of decoding a binary stream
into HTTP/2 frames.

This library is used directly by hyper and a number of other projects to
provide HTTP/2 frame decoding logic.

</details>

### hvac

HashiCorp Vault API client

`pip install hvac` · installs (wheel) · licence: Apache Software License · rank 779 · last release 2025-10-30 · [PyPI](https://pypi.org/project/hvac/) · [docs](https://hvac.readthedocs.io/en/stable/overview.html) · [source](https://github.com/hvac/hvac)

<details><summary>README extract</summary>

HashiCorp Vault API client for Python 3.x

Tested against the latest release, HEAD ref, and 3 previous minor versions (counting back from the latest release) of Vault.
Current official support covers Vault v1.4.7 or later.

> NOTE: Support for EOL Python versions will be dropped at the end of 2022. ...

Sections: hvac, Documentation

</details>

### hatch-vcs

Hatch plugin for versioning with your preferred VCS

`pip install hatch-vcs` · installs (wheel) · licence: MIT · rank 892 · last release 2025-05-27 · [PyPI](https://pypi.org/project/hatch-vcs/) · [source](https://github.com/ofek/hatch-vcs)

<details><summary>README extract</summary>

| | |

| CI/CD | |
| Package | |
| Meta | |

This provides a plugin for Hatch that uses your preferred version control system (like Git) to determine project versions.

Table of Contents

- Global dependency
- Version source
 - Version source options
 - Version source environment variables
- Build hook
 - Build hook options
 - Editable installs ...

Sections: hatch-vcs, Global dependency, Version source, Version source options, Version source environment variables, Build hook, Build hook options, Metadata hook, Metadata hook options, URLs, Example, Migration tips, Display version, Write version to file

</details>

### hydra-core

A framework for elegantly configuring complex applications

`pip install hydra-core` · installs (wheel) · licence: MIT License · rank 932 · last release 2026-10-25 · [PyPI](https://pypi.org/project/hydra-core/)

<details><summary>README extract</summary>

A framework for elegantly configuring complex applications.

 Check the website for more information,

 or click the thumbnail below for a one-minute video introduction to Hydra.

Sections: Stable, Hydra Ecosystem, Citing Hydra

</details>

### html2text

Turn HTML into equivalent Markdown-structured text.

`pip install html2text` · installs (wheel) · licence: GPL-3.0-or-later · rank 1090 · last release 2025-04-15 · [PyPI](https://pypi.org/project/html2text/)

_README extract left out: share-alike licence._

### http-ece

Encrypted Content Encoding for HTTP

`pip install http-ece` · installs from source (sdist only) · licence: MIT License · rank 1352 · last release 2024-08-08 · [PyPI](https://pypi.org/project/http-ece/)

### hexbytes

hexbytes: Python `bytes` subclass that decodes hex, with a readable console output

`pip install hexbytes` · installs (wheel) · licence: MIT · rank 1582 · last release 2026-08-21 · [PyPI](https://pypi.org/project/hexbytes/) · [docs](https://hexbytes.readthedocs.io/) · [source](https://github.com/ApeWorX/hexbytes.git)

<details><summary>README extract</summary>

Python `bytes` subclass that decodes hex, with a readable console output

Read the documentation.

View the change log.

</details>

### harbor

A framework for evaluating and optimizing agents and models using sandboxed environments.

`pip install harbor` · installs (wheel) · licence: Apache-2.0 · rank 1608 · last release 2026-10-25 · [PyPI](https://pypi.org/project/harbor/)

<details><summary>README extract</summary>

Harbor is a framework from the creators of Terminal-Bench for evaluating and optimizing agents and language models. You can use Harbor to:

- Evaluate arbitrary agents like Claude Code, OpenHands, Codex CLI, and more.
- Build and share your own benchmarks and environments. ...

Sections: Harbor, Example: Running Terminal-Bench-2.0

</details>

### highspy

A thin set of pybind11 wrappers to HiGHS

`pip install highspy` · installs (wheel) · licence: MIT · rank 1615 · last release 2026-07-02 · [PyPI](https://pypi.org/project/highspy/) · [source](https://github.com/ERGO-Code/HiGHS)

<details><summary>README extract</summary>

[][fast_build_link]
[][linux_build_link]
[][macos_build_link]
[][windows_build_link]



- About HiGHS
- Documentation
- Installation
 - Build from source using CMake
 - Build with Meson*
 - Build with Nix*
 - Precompiled binaries
- Running HiGHS
- Interfaces
 - Python
 - CSharp
 - Fortran
- Reference ...

Sections: HiGHS - Linear optimization software, About HiGHS, Documentation, Build from source using CMake, Build with Meson, Build with Nix, Precompiled binaries, Running HiGHS, Command line options, Interfaces, Python, C, CSharp, Fortran

</details>

### httpx-aiohttp

Aiohttp transport for HTTPX

`pip install httpx-aiohttp` · installs (wheel) · licence: not stated · rank 1813 · last release 2026-07-25 · [PyPI](https://pypi.org/project/httpx-aiohttp/) · [source](https://github.com/karpetrosyan/httpx-aiohttp)

<details><summary>README extract</summary>

httpx-aiohttp - provides transports for httpx to work on top of aiohttp, handling all high-level features like authentication, retries, and cookies through httpx, while delegating low-level socket-level HTTP messaging to aiohttp

</details>

### hubspot-api-client

HubSpot API client

`pip install hubspot-api-client` · installs (wheel) · licence: Apache-2.0 · rank 1899 · last release 2026-11-02 · [PyPI](https://pypi.org/project/hubspot-api-client/)

<details><summary>README extract</summary>

Python HubSpot API v3 SDK(Client) files and sample apps

Sample Applications can be found in Sample apps

See the API docs.

Example:
```python
import hubspot

from dateutil import parser
from pprint import pprint
from hubspot.crm.contacts import PublicObjectSearchRequest, ApiException

api_client = hubspot.Client.create(access_token="YOUR_ACCESS_TOKEN")

# timestamp in milliseconds
date = str(int(parser.isoparse("XXXX-XX-XXTXX:XX:XX.XXXZ").timestamp() * 1000))
...
```

Sections: hubspot-api-python, Documentation, Requirements, Quickstart, Configuring HubSpot client, OAuth API, Obtain OAuth2 access token, CRM API, Create contact, Get contact by id, Get custom objects page, Get all, Search, Example Search by date

</details>

### hdfs

HdfsCLI: API and command line interface for HDFS.

`pip install hdfs` · installs from source (sdist only) · licence: MIT License · rank 2139 · last release 2023-10-13 · [PyPI](https://pypi.org/project/hdfs/)

<details><summary>README extract</summary>

API and command line interface for HDFS.

Features:
* Python 3 bindings for the WebHDFS (and HttpFS) API,
 supporting both secure and insecure clusters.
* Command line interface to transfer files and start an interactive client
 shell, with aliases for convenient namenode URL caching. ...

Example:
```python
$ hdfscli --alias=dev

Welcome to the interactive HDFS python shell.
The HDFS client is available as `CLIENT`.

In [1]: CLIENT.list('models/')
Out[1]: ['1.json', '2.json']

In [2]: CLIENT.status('models/2.json')
Out[2]: {
  'accessTime': 1439743128690,
  'blockSize': 134217728,
  'childrenNum': 0,
  'fileId': 16389,
  'group': 'supergroup',
...
```

Sections: HdfsCLI, Features, Getting started

</details>

### hf-transfer

Speed up file transfers with the Hugging Face Hub.

`pip install hf-transfer` · installs (wheel) · licence: not stated · rank 2141 · last release 2025-01-07 · [PyPI](https://pypi.org/project/hf-transfer/) · [source](https://github.com/huggingface/hf_transfer.git)

<details><summary>README extract</summary>

Speed up file transfers with the Hub.

This library is a power user tool, to go beyond `~500MB/s` on very high bandwidth
network, where Python cannot cap out the available bandwidth.

This is *not* meant to be a general usability tool.
It purposefully lacks progressbars and comes generally as-is. ...

Example:
```python
import os

# os.environ["HF_ENDPOINT"] = "
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

from huggingface_hub import HfApi, logging

logging.set_verbosity_debug()
hf = HfApi()
hf.upload_file(path_or_fileobj="/path/to/my/repo/some_file", path_in_repo="some_file", repo_id="my/repo", repo_type="model")
```

Sections: HF Transfer, DISCLAIMER, `huggingface_hub`

</details>

### honcho

Honcho: a Python clone of Foreman. For managing Procfile-based applications.

`pip install honcho` · installs (wheel) · licence: MIT License · rank 2185 · last release 2024-10-06 · [PyPI](https://pypi.org/project/honcho/) · [source](https://github.com/nickstenning/honcho)

<details><summary>README extract</summary>

Honcho is a Python port of Foreman, a tool for managing Procfile-based applications.

Why a port?

</details>

### hf-gradio

An extension of the Hugging Face CLI for interacting with Gradio Spaces and Apps.

`pip install hf-gradio` · installs (wheel) · licence: MIT · rank 2278 · last release 2026-04-22 · [PyPI](https://pypi.org/project/hf-gradio/)

### hijri-converter

[DEPRECATED] Use 'hijridate' package instead

`pip install hijri-converter` · installs (wheel) · licence: MIT · rank 2459 · last release 2025-07-27 · [PyPI](https://pypi.org/project/hijri-converter/)

<details><summary>README extract</summary>

This package is deprecated and will not receive future updates.

Install the HijriDate package:

Update your imports:

The API is identical - only the package name changes.

Features:
The HijriDate package is the actively maintained successor with the same functionality and accuracy.

Example:
```python
# Old (deprecated)
from hijri_converter import Hijri, Gregorian

# New (recommended)
from hijridate import Hijri, Gregorian
```

Sections: hijri-converter, ⚠️ DEPRECATED - Use HijriDate instead, Migration Required, Why the change?

</details>

### hashids

Implements the hashids algorithm in python. For more information, visit http://hashids.org/

`pip install hashids` · installs (wheel) · licence: MIT License · rank 2661 · last release 2020-07-26 · [PyPI](https://pypi.org/project/hashids/)

<details><summary>README extract</summary>

A python port of the JavaScript *hashids* implementation. It generates YouTube-like hashes from one or many numbers. Use hashids when you do not want to expose your database ids to the user. Website:

hashids is tested with python 2.7 and 3.5–3.8. PyPy and PyPy 3 work as well. ...

Example:
```python
from hashids import Hashids
hashids = Hashids()
```

Sections: hashids for Python 2.7 & 3, Compatibility, Compatibility with the JavaScript implementation, Run the tests, Usage, Basic Usage, Using A Custom Salt, Controlling Hash Length, Using A Custom Alphabet, Randomness, Repeating numbers, Curses! #$%@

</details>

### html-to-markdown

High-performance HTML to Markdown converter

`pip install html-to-markdown` · installs (wheel) · licence: MIT · rank 2752 · last release 2026-11-07 · [PyPI](https://pypi.org/project/html-to-markdown/) · [source](https://github.com/xberg-io/html-to-markdown)

### hupper

Integrated process monitor for developing and reloading daemons.

`pip install hupper` · installs (wheel) · licence: MIT License · rank 2798 · last release 2024-01-26 · [PyPI](https://pypi.org/project/hupper/) · [docs](https://docs.pylonsproject.org/projects/hupper/en/latest/)

<details><summary>README extract</summary>

`hupper` is an integrated process monitor that will track changes to
any imported Python files in `sys.modules` as well as custom paths. When
files are changed the process is restarted.

Example:
```python
# myapp/scripts/serve.py

import sys
import hupper
import waitress

def wsgi_app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield b'hello'

def main(args=sys.argv[1:]):
    if '--reload' in args:
        # start_reloader will only return in a monitored subprocess
...
```

Sections: hupper, Command-line Usage, API Usage

</details>

### hatchet-sdk

This is the official Python SDK for Hatchet, a distributed, fault-tolerant task queue. The SDK allows you to easily integrate Hatchet's task scheduling and workflow orchestration capabilities into your Python applications.

`pip install hatchet-sdk` · installs (wheel) · licence: MIT · rank 3074 · last release 2026-11-05 · [PyPI](https://pypi.org/project/hatchet-sdk/)

<details><summary>README extract</summary>

This is the official Python SDK for Hatchet, a distributed, fault-tolerant task queue. The SDK allows you to easily integrate Hatchet's task scheduling and workflow orchestration capabilities into your Python applications.

The linked pages serve plain markdown for tools and agents. Full docs index:

Setup and local development:

Core concepts: ...

Features:
- 🔄 Workflow Orchestration: Define complex workflows with dependencies and parallel execution
- 🔁 Automatic Retries: Configure retry policies for handling transient failures
- 📊 Observability: Track workflow progress and monitor execution metrics ...

Sections: Hatchet Python SDK, Documentation for agents, Quick Start, Features, Documentation

</details>

### hogql-parser

HogQL parser for internal PostHog use

`pip install hogql-parser` · installs (wheel) · licence: MIT · rank 3389 · last release 2026-09-17 · [PyPI](https://pypi.org/project/hogql-parser/)

<details><summary>README extract</summary>

ANTLR4-based parser for HogQL and Hog,
available as both a Python C++ extension and a WebAssembly module for JavaScript/TypeScript.

| Package | Runtime | Registry |

| `hogql_parser` | CPython (native C++ extension) | PyPI |
| `@posthog/hogql-parser` | Any JS environment (WebAssembly) | npm | ...

Sections: HogQL Parser, Packages, npm package (`@posthog/hogql-parser`), Usage, API, Python package (`hogql_parser`), Building from source, Python, WebAssembly

</details>

### hogql-parser-rs

Hand-rolled Rust HogQL parser with C++-parity AST output

`pip install hogql-parser-rs` · installs (wheel) · licence: MIT · rank 3445 · last release 2026-09-17 · [PyPI](https://pypi.org/project/hogql-parser-rs/) · [source](https://github.com/PostHog/posthog)

<details><summary>README extract</summary>

Hand-rolled Rust HogQL parser. Pratt + recursive descent. Same JSON AST
shape as the C++ ANTLR parser so the
two can be cross-validated query-by-query. Ships as a Python extension
via `maturin` and is selected as the `rust-json` backend in
`posthog/hogql/parser.py`. ...

Example:
```python
from posthog.hogql.constants import HogQLParserBackend
parse_expr(src, backend=HogQLParserBackend.CPP_WITH_RUST_SHADOW)
```

...

</details>

### html-text

Extract text from HTML

`pip install html-text` · installs (wheel) · licence: MIT · rank 3680 · last release 2025-10-06 · [PyPI](https://pypi.org/project/html-text/)

<details><summary>README extract</summary>

Extract text from HTML

* Free software: MIT license

How is html_text different from `.xpath('//text()')` from LXML
or `.get_text()` from Beautiful Soup?

* Text extracted with `html_text` does not contain inline styles,
 javascript, comments and other text that is not normally visible to users;
* `html_text` normalizes whitespace, but in a way ...

Example:
```python
>>> import html_text
>>> html_text.extract_text('
# Hello
 world!')
'Hello\n\nworld!'

>>> html_text.extract_text('
# Hello
 world!', guess_layout=False)
'Hello world!'
```

Sections: HTML to Text, Usage, Hello, Hello.foo{}!

</details>

### HyperPyYAML

Extensions to YAML syntax for better python interaction

`pip install HyperPyYAML` · installs (wheel) · licence: Apache Software License · rank 3701 · last release 2026-01-01 · [PyPI](https://pypi.org/project/HyperPyYAML/)

<details><summary>README extract</summary>

Introduction

A crucial element of systems for data-analysis is laying out all the
hyperparameters of that system so they can be easily examined and modified.
We add a few useful extensions to a popular human-readable data-serialization
language known as YAML (YAML Ain't Markup Language). ...

Example:
```python
>>> loaded_yaml = load_hyperpyyaml("add: !name:operator.add")
>>> loaded_yaml"add"
6
```

Sections: Objects, Aliases, Tuples

</details>

### hdijupyterutils

HdiJupyterUtils: Utils for Jupyter projects from HDInsight team

`pip install hdijupyterutils` · installs (wheel) · licence: BSD License · rank 4248 · last release 2025-07-07 · [PyPI](https://pypi.org/project/hdijupyterutils/)

### hindsight-client

Python client for Hindsight - Semantic memory system with personality-driven thinking

`pip install hindsight-client` · installs (wheel) · licence: MIT · rank 4263 · last release 2026-11-03 · [PyPI](https://pypi.org/project/hindsight-client/)

### halo

Beautiful terminal spinners in Python

`pip install halo` · installs from source (sdist only) · licence: MIT · rank 4321 · last release 2020-11-10 · [PyPI](https://pypi.org/project/halo/)

<details><summary>README extract</summary>

halo

> Beautiful spinners for terminal, IPython and Jupyter

Example:
```python
from halo import Halo

spinner = Halo(text='Loading', spinner='dots')
spinner.start()

# Run time consuming work here
# You can also change properties for spinner as and when you want

spinner.stop()
```

Sections: Usage, API, `text`, `text_color`, `spinner`, `animation`, `placement`, `color`, `interval`, `stream`, `enabled`, Methods, `spinner.start([text])`, `spinner.stop()`

</details>

### hidapi

A Cython interface to the hidapi from https://github.com/libusb/hidapi

`pip install hidapi` · installs (wheel) · licence: BSD License; GNU General Public License v3 (GPLv3) · rank 4337 · last release 2025-12-09 · [PyPI](https://pypi.org/project/hidapi/)

_README extract left out: share-alike licence._

### httpx-oauth

Async OAuth client using HTTPX

`pip install httpx-oauth` · installs (wheel) · licence: MIT License · rank 4367 · last release 2026-05-13 · [PyPI](https://pypi.org/project/httpx-oauth/) · [docs](https://frankie567.github.io/httpx-oauth/) · [source](https://github.com/frankie567/httpx-oauth)

<details><summary>README extract</summary>

Async OAuth client using HTTPX

Documentation:

Source Code:

Sections: HTTPX OAuth, Setup environment, Run unit tests, Format the code, Publish a new version, Serve the documentation

</details>

### hbreader

Honey Badger reader - a generic file/url/string open and read tool

`pip install hbreader` · installs (wheel) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication · rank 4548 · last release 2021-02-25 · [PyPI](https://pypi.org/project/hbreader/)

### httpxthrottlecache

Rate Limiting and Caching HTTPX Client

`pip install httpxthrottlecache` · installs (wheel) · licence: not stated · rank 4632 · last release 2026-10-11 · [PyPI](https://pypi.org/project/httpxthrottlecache/) · [source](https://github.com/paultiq/httpxthrottlecache)

<details><summary>README extract</summary>

HTTPX Wrapper with Rate Limiting and Caching Transports.

Example:
```python
from httpxthrottlecache import HttpxThrottleCache

url = "

with HttpxThrottleCache(
    cache_mode="Hishel-File",
    cache_dir="_cache",
    rate_limiter_enabled=True,
    request_per_sec_limit=10,
    user_agent="your user agent",
) as manager:
    # Single synchronous request
    with manager.http_client() as client:
...
```

Sections: Introduction, Caching, Misc Settings, Usage: Synchronous Requests, Usage: Batch Requests, Usage: Retrieve many files and write to files, Usage: Asynchronous, Usage: primp backend, FileCache, Rate Limiting

</details>

### htmldocx

Convert html to docx

`pip install htmldocx` · installs (wheel) · licence: MIT License · rank 4722 · last release 2021-08-25 · [PyPI](https://pypi.org/project/htmldocx/)

<details><summary>README extract</summary>

Convert html to docx

Dependencies: `python-docx` & `bs4`

Example:
```python
from docx import Document
from htmldocx import HtmlToDocx

document = Document()
new_parser = HtmlToDocx()
# do stuff to document

html = '
# Hello world
'
new_parser.add_html_to_document(html, document)

# do more stuff to document
document.save('your_file_name')
```

Sections: htmldocx, Usage

</details>

### hnswlib

hnswlib

`pip install hnswlib` · installs from source (sdist only) · licence: not stated · rank 5041 · last release 2023-12-03 · [PyPI](https://pypi.org/project/hnswlib/)

### httpstan

HTTP-based interface to Stan, a package for Bayesian inference.

`pip install httpstan` · installs (wheel) · licence: OSI Approved; ISC License (ISCL) · rank 5307 · last release 2026-07-29 · [PyPI](https://pypi.org/project/httpstan/) · [docs](https://httpstan.readthedocs.io) · [source](https://github.com/stan-dev/httpstan)

<details><summary>README extract</summary>

HTTP-based REST interface to Stan, a package for Bayesian inference.

An HTTP 1.1 interface to the Stan C++ package, httpstan is a shim that
allows users to interact with the Stan C++ library using a REST API. The
package is intended for use as a universal backend for frontends which know how
to make HTTP requests. ...

Example:
```python
curl -H "Content-Type: application/json" \
    --data '{"program_code":"parameters {real y;} model {y ~ normal(0,1);}"}' \
```

Sections: httpstan, Requirements, Background, Usage

</details>

### hdrhistogram

High Dynamic Range histogram in native python

`pip install hdrhistogram` · installs (wheel) · licence: Apache Software License · rank 5446 · last release 2026-10-12 · [PyPI](https://pypi.org/project/hdrhistogram/)

<details><summary>README extract</summary>

Features:
High Dynamic Range Histogram python implementation

This repository contains a port to python of most of the original Java HDR Histogram
library: ...

Example:
```python
histogram = HdrHistogram(1, 60 * 60 * 1000, 2)
```

Sections: Overview, Python API, Aggregation of Distributed Histograms, Histogram wire encoding and size, Performance, Limitations, Caveats and Known Issues, Dependencies, Licensing, Links

</details>

### human-eval

(no summary)

`pip install human-eval` · installs (wheel) · licence: not stated · rank 6129 · last release 2023-07-24 · [PyPI](https://pypi.org/project/human-eval/)

### hyperbrowser

Python SDK for hyperbrowser

`pip install hyperbrowser` · installs (wheel) · licence: MIT License · rank 6156 · last release 2026-10-28 · [PyPI](https://pypi.org/project/hyperbrowser/) · [source](https://github.com/hyperbrowserai/python-sdk)

<details><summary>README extract</summary>

Checkout the full documentation here

Example:
```python
from hyperbrowser import Hyperbrowser

client = Hyperbrowser(api_key="test-key")

# Preferred in 1.0: autocomplete works directly in the dictionary.
session = client.sessions.create(
    {
        "use_stealth": True,
        "screen": {"width": 1920, "height": 1080},
    }
)
```

Sections: Hyperbrowser Python SDK, Configuration, API Key, WebMCP page tools, Web Bot Auth, Proxy routes, Fill credentials into browser sessions, Fill from 1Password, Use with LLM SDKs, Tools for LLM function calling, Usage, Async, Sync, Sandboxes

</details>

### helion

A Python-embedded DSL that makes it easy to write ML kernels

`pip install helion` · installs (wheel) · licence: not stated · rank 6362 · last release 2026-11-01 · [PyPI](https://pypi.org/project/helion/)

<details><summary>README extract</summary>

📚 View Documentation 📚 |
🎥 Watch Talk 🎥 |
🚀 Try In Colab 🚀 |
Try In AMD DevCloud

Helion is a Python-embedded domain-specific language (DSL) for
authoring machine learning kernels, designed to compile down to [Triton],
a performant backend for programming GPUs and other devices. ...

Example:
```python
import torch, helion, helion.language as hl

@helion.kernel()
def matmul(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    m, k = x.size()
    k, n = y.size()
    out = torch.empty([m, n], dtype=x.dtype, device=x.device)

    for tile_m, tile_n in hl.tile([m, n]):
        acc = hl.zeros([tile_m, tile_n], dtype=torch.float32)
...
```

...

</details>

### hcloud

Official Hetzner Cloud python library

`pip install hcloud` · installs (wheel) · licence: MIT · rank 6425 · last release 2026-10-05 · [PyPI](https://pypi.org/project/hcloud/) · [docs](https://hcloud-python.readthedocs.io/en/stable/) · [source](https://github.com/hetznercloud/hcloud-python)

<details><summary>README extract</summary>

Official Hetzner Cloud python library.

The library's documentation is available at hcloud-python.readthedocs.io, the public API documentation is available at docs.hetzner.cloud. ...

Example:
```python
from hcloud import Client
from hcloud.images import Image
from hcloud.server_types import ServerType

client = Client(
    token="{YOUR_API_TOKEN}", # Please paste your API token here
    application_name="my-app",
    application_version="v1.0.0",
)

# Create a server named my-server
response = client.servers.create(
    name="my-server",
...
```

Sections: Hetzner Cloud Python, Usage, Experimental features, Deprecations implementation, Releasing experimental features

</details>

### httpagentparser

Extracts OS Browser etc information from http user agent string

`pip install httpagentparser` · installs (wheel) · licence: not stated · rank 6454 · last release 2026-03-08 · [PyPI](https://pypi.org/project/httpagentparser/)

<details><summary>README extract</summary>

Features:
- Fast
- Detects OS and Browser. Does not aim to be a full featured agent parser
- Will not turn into django-httpagentparser ;)

Example:
```python
>>> import httpagentparser
>>> s = "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.9 (KHTML, like Gecko) \
        Chrome/5.0.307.11 Safari/532.9"
>>> print(httpagentparser.simple_detect(s))
('Linux', 'Chrome 5.0.307.11')
>>> print(httpagentparser.detect(s))
{'os': {'name': 'Linux'},
...
```

Sections: Features, Usage

</details>

### html-tag-names

List of known HTML tag names

`pip install html-tag-names` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6632 · last release 2022-03-09 · [PyPI](https://pypi.org/project/html-tag-names/) · [source](https://github.com/Riverside-Healthcare/html-tag-names)

_README extract left out: share-alike licence._

### html-void-elements

List of HTML void tag names.

`pip install html-void-elements` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6636 · last release 2022-03-09 · [PyPI](https://pypi.org/project/html-void-elements/) · [source](https://github.com/Riverside-Healthcare/html-void-elements)

_README extract left out: share-alike licence._

### hermes-agent

The self-improving AI agent — creates skills from experience, improves them during use, and runs anywhere

`pip install hermes-agent` · does not install on CPython 3.14 · licence: MIT · rank 6729 · last release 2026-07-20 · [PyPI](https://pypi.org/project/hermes-agent/)

<details><summary>README extract</summary>

Hermes Agent | Hermes Desktop

The self-improving AI agent built by Nous Research. It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. ...

Sections: Hermes Agent ☤, Linux, macOS, WSL2, Termux, Windows (native, PowerShell), Troubleshooting, Windows Defender or antivirus flags `uv.exe` as malware, Getting Started, Skip the API-key collection — Nous Portal, CLI vs Messaging Quick Reference, Documentation, Migrating from OpenClaw

</details>

### hiPhive

High-order force constants for the masses

`pip install hiPhive` · installs (wheel) · licence: not stated · rank 7037 · last release 2025-07-28 · [PyPI](https://pypi.org/project/hiPhive/) · [docs](https://hiphive.materialsmodeling.org) · [source](https://gitlab.com/materials-modeling/hiphive/)

<details><summary>README extract</summary>

hiPhive is a tool for efficiently extracting high-order force constants from atomistic simulations, most commonly density functional theory calculations.
A detailed description of the functionality provided as well as an extensive tutorial can be found in the user guide. ...

Example:
```python
cs = ClusterSpace(primitive_cell, cutoffs)
sc = StructureContainer(cs, list_of_training_structure)
opt = Optimizer(sc.get_fit_data())
opt.train()
fcp = ForceConstantPotential(cs, opt.parameters)
```

</details>

### hatch-polylith-bricks

Hatch build hook plugin for Polylith

`pip install hatch-polylith-bricks` · installs (wheel) · licence: MIT License · rank 7304 · last release 2026-07-03 · [PyPI](https://pypi.org/project/hatch-polylith-bricks/) · [source](https://github.com/davidvujic/python-polylith)

<details><summary>README extract</summary>

A plugin for Hatch and the Polylith Architecture.

This build hook will look for Polylith `bricks` in `pyproject.toml` and optionally re-write the imports made in the source code.

Features:
Building libraries is supported in the Python tools for the Polylith Architecture,
but you will need to consider that code will share the same top namespace with any other library built from the same monorepo. ...

Example:
```python
from my_namespace.my_package import my_function
```

Sections: Hatch Build Hook for Polylith, Polylith documentation, Why re-write code?, How is this done?, What's the output from this plugin?, With a Top Namespace configuration, Usage

</details>

### harness-featureflags

Feature flag server SDK for python

`pip install harness-featureflags` · installs (wheel) · licence: Apache Software License · rank 7339 · last release 2026-11-03 · [PyPI](https://pypi.org/project/harness-featureflags/)

<details><summary>README extract</summary>

Example:
```python
from featureflags.client import CfClient
from featureflags.config import *
from featureflags.evaluations.auth_target import Target
from featureflags.util import log
import os
import time

# API Key
apiKey = os.getenv('FF_API_KEY', "changeme")

# Flag Name
flagName = os.getenv('FF_FLAG_NAME', "harnessappdemodarkmode")

def main():
...
```

Sections: Python SDK For Harness Feature Flags, Intro, Requirements, Quickstart, - Created a server SDK key and made a copy of it, Code Sample, Running the example, Running the example with Docker, Additional Reading

</details>

### hydraters

Hydrate Python dictionaries with Rust.

`pip install hydraters` · installs (wheel) · licence: not stated · rank 7618 · last release 2026-05-27 · [PyPI](https://pypi.org/project/hydraters/) · [source](https://github.com/developmentseed/hydraters)

<details><summary>README extract</summary>

Hydrate Python dictionaries with Rust.
A general-purpose algorithm, used in pgstac to reduce the size of the `items` table.

If you want to clean out any lingering ``DO_NOT_MERGE_MARKER`` entries after
hydration, pass ``strip_unmatched_markers=True``. ...

Example:
```python
import hydraters

base = {"a": "first", "b": "second", "c": {"d": "third"}}
item = {"c": {"e": "fourth", "f": "fifth"}}
result = hydraters.hydrate(base, item)
assert result == {
    "a": "first",
    "b": "second",
    "c": {"d": "third", "e": "fourth", "f": "fifth"},
}
```

Sections: hydraters, Background

</details>

### hierarchicalforecast

Hierarchical Methods Time Series Forecasting

`pip install hierarchicalforecast` · installs (wheel) · licence: Apache Software License · rank 7641 · last release 2026-09-24 · [PyPI](https://pypi.org/project/hierarchicalforecast/) · [docs](https://nixtlaverse.nixtla.io/hierarchicalforecast/) · [source](https://github.com/Nixtla/hierarchicalforecast/)

<details><summary>README extract</summary>

HierarchicalForecast offers a collection of cross-sectional and temporal reconciliation methods, including `BottomUp`, `TopDown`, `MiddleOut`, `MinTrace` and `ERM`, as well as probabilistic coherent prediction methods such as `Normality`, `Bootstrap`, and `PERMBU`.

Example:
```python
# !pip install -U numba statsforecast datasetsforecast
import numpy as np
import pandas as pd

# obtain hierarchical dataset
from datasetsforecast.hierarchical import HierarchicalData

# compute base forecast no coherent
from statsforecast.core import StatsForecast
from statsforecast.models import AutoARIMA, Naive

...
```

Sections: Nixtla, Hierarchical Forecast 👑, 📚 Intro, 🎊 Features, 📖 Why?, 🧬 How to use, Evaluation, 📖 Documentation, 🏟 HTS projects

</details>

### http-sf

Parse and serialise HTTP Structured Fields

`pip install http-sf` · installs (wheel) · licence: MIT · rank 7801 · last release 2026-10-23 · [PyPI](https://pypi.org/project/http-sf/)

<details><summary>README extract</summary>

This is a Python 3 library implementing parsing and serialisation of RFC 9651.

Textual HTTP headers can be parsed by calling `parse`; the return value is a data structure that represents the field value. ...

Sections: HTTP Structured Fields in Python, Python API, Parsing, Indicating Top-Level Type, Error Handling, Duplicate Keys, Types, Parameters, Serialisation, Migrating from `http_sfv`, Before, After, Command Line Use

</details>

### hammock

rest like a boss

`pip install hammock` · installs from source (sdist only) · licence: UNKNOWN · rank 7963 · last release 2013-04-21 · [PyPI](https://pypi.org/project/hammock/)

<details><summary>README extract</summary>

_ _
 | | | |
 | | _ _ ____| | _
 | _ \(__ | \| \ / _ \ / _) |_/ )
 | | | / _ | | | | | | | |_| ( (_| _ (
 |_| |_\_|_|_|_|_|_|_|\_/ \__)_| \_)

Hammock is a fun module lets you deal with rest APIs by converting them into dead simple programmatic APIs.
It uses popular ``requests`` module in backyard to provide full-fledged rest experience.

Proof ...

</details>

### HTMLParser

Backport of HTMLParser from python 2.7

`pip install HTMLParser` · installs from source (sdist only) · licence: BSD License · rank 8117 · last release 2013-03-01 · [PyPI](https://pypi.org/project/HTMLParser/)

<details><summary>README extract</summary>

A copy of HTMLParser from python2.7 for use in python2.6

</details>

### html-testRunner

A Test Runner in python, for Human Readable HTML Reports

`pip install html-testRunner` · installs (wheel) · licence: MIT License · rank 8158 · last release 2019-09-09 · [PyPI](https://pypi.org/project/html-testRunner/)

<details><summary>README extract</summary>

HtmlTest runner is a unittest test runner that save test results
in Html files, for human readable presentation of results.

This Package was inspired in `unittest-xml-reporting` and
`HtmlTestRunner by tungwaiyip`.

Example:
```python
import HtmlTestRunner
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_error(self):
        """ This test should be marked as error one. """
        raise ValueError

    def test_fail(self):
        """ This test should fail. """
...
```

Sections: HtmlTestRunner, Usage, Links

</details>

### hydra-colorlog

Enables colorlog for Hydra apps

`pip install hydra-colorlog` · installs (wheel) · licence: MIT License · rank 8337 · last release 2022-05-17 · [PyPI](https://pypi.org/project/hydra-colorlog/)

<details><summary>README extract</summary>

Adds colorlog colored logs for `hydra/job_logging` and `hydra/hydra_logging`.

See website for more information

</details>

### hive-metastore-client

A client for connecting and running DDLs on Hive Metastore with Thrift protocol

`pip install hive-metastore-client` · installs (wheel) · licence: Copyright · rank 8477 · last release 2021-08-23 · [PyPI](https://pypi.org/project/hive-metastore-client/)

<details><summary>README extract</summary>

_A client for connecting and running DDLs on Hive Metastore using Thrift protocol._


| Source | Downloads | Page | Installation Command |

| PyPi | | Link | `pip install hive-metastore-client ` |

</details>

### httpbin

HTTP Request and Response Service

`pip install httpbin` · installs (wheel) · licence: ISC License (ISCL); MIT License · rank 8518 · last release 2026-06-16 · [PyPI](https://pypi.org/project/httpbin/) · [source](https://github.com/psf/httpbin)

<details><summary>README extract</summary>

This is a fork of the original httpbin project, which is located at

Why fork? we were unable to get ahold of the folks at postmanlabs to maintain the original project, and httpbin is used for other packages within the python ecosystem, such as pytest-httpbin which is in turn used by packages such as requests so we have forked this package. ...

Sections: httpbin(1): HTTP Request & Response Service, Downloading and Running, Using `httpbin` as a Library, Manually Building the Latest Docker Image, Maintenance, "Extra" Dependencies, Officially Deployed (but out of date) at, SEE ALSO

</details>

### httpx-ntlm

This package allows for HTTP NTLM authentication using the HTTPX library.

`pip install httpx-ntlm` · installs (wheel) · licence: ISC License (ISCL) · rank 8785 · last release 2023-11-03 · [PyPI](https://pypi.org/project/httpx-ntlm/)

<details><summary>README extract</summary>

This package allows for HTTP NTLM authentication using the HTTPX library. It is an
adaptation of

Example:
```python
import httpx
from httpx_ntlm import HttpNtlmAuth

httpx.get("
```

Sections: httpx-ntlm, Usage, Requirements

</details>

### hierarchical-conf

A tool for loading settings from files hierarchically

`pip install hierarchical-conf` · installs (wheel) · licence: not stated · rank 9052 · last release 2025-08-20 · [PyPI](https://pypi.org/project/hierarchical-conf/)

<details><summary>README extract</summary>

_A library for loading configurations (or other metadata) hierarchically based on the current environment


| Source | Downloads | Page | Installation Command |

| PyPi | | Link | `pip install hierarchical-conf ` |

Example:
```python
from hierarchical_conf.hierarchical_conf import HierarchicalConf

hierarchical_conf = HierarchicalConf(searched_paths=[PROJECT_ROOT])
my_config = hierarchical_conf.get_config("my_config_key")
```

Sections: Hierarchical Conf, How to use, Short, Long

</details>

### hud-sdk

Hud runtime code sensor for Python

`pip install hud-sdk` · installs (wheel) · licence: SEE LICENSE FILE · rank 9053 · last release 2026-10-30 · [PyPI](https://pypi.org/project/hud-sdk/) · [docs](https://docs.hud.io)

<details><summary>README extract</summary>

Hud is a Runtime Code Sensor that understands your code's behavior in production, helping engineers and coding agents build production-safe code.

Features:
`hud-sdk` is a lightweight, low-overhead runtime sensor for production code. Installed in under a minute, it captures real-time behavior of every function in your service - including performance characteristics, error behavior, and execution ...

Sections: Hud Python SDK, Why Hud, Core Benefits & Features, Learn More

</details>

### hyperlight-sandbox-backend-wasm

Wasm backend implementation for hyperlight-sandbox

`pip install hyperlight-sandbox-backend-wasm` · installs (wheel) · licence: Apache-2.0 · rank 9062 · last release 2026-11-06 · [PyPI](https://pypi.org/project/hyperlight-sandbox-backend-wasm/)

<details><summary>README extract</summary>

Native Wasm backend package for the `hyperlight-sandbox` Python API.

</details>

### hyperlight-sandbox-python-guest

Packaged Hyperlight Wasm Python guest exposed as python_guest.path

`pip install hyperlight-sandbox-python-guest` · installs (wheel) · licence: Apache-2.0 · rank 9106 · last release 2026-11-06 · [PyPI](https://pypi.org/project/hyperlight-sandbox-python-guest/)

<details><summary>README extract</summary>

Packaged Python guest for the `hyperlight-sandbox` Wasm backend.

After installation, use `module="python_guest.path"` or
`module_path="python_guest.path"` in the public API package.

</details>

### hatch-jupyter-builder

A hatch plugin to help build Jupyter packages

`pip install hatch-jupyter-builder` · installs (wheel) · licence: BSD License · rank 9129 · last release 2026-09-18 · [PyPI](https://pypi.org/project/hatch-jupyter-builder/) · [docs](https://github.com/jupyterlab/hatch-jupyter-builder#readme) · [source](https://github.com/jupyterlab/hatch-jupyter-builder)

<details><summary>README extract</summary>

______________

This provides a build hook plugin for Hatch that adds a build step for use with Jupyter packages.

Table of Contents

- Documentation
- Installation
- License
- Usage and Configuration
- Local Development

The full documentation is available on Read The Docs.

Sections: hatch-jupyter-builder, Documentation, Skipping the Build, Migration

</details>

### hyperlight-sandbox

Python API for running code in isolated Hyperlight sandboxes with swappable backends

`pip install hyperlight-sandbox` · installs (wheel) · licence: Apache-2.0 · rank 9171 · last release 2026-11-06 · [PyPI](https://pypi.org/project/hyperlight-sandbox/) · [source](https://github.com/hyperlight-dev/hyperlight-wasm)

<details><summary>README extract</summary>

Python API package for running code inside Hyperlight sandboxes with separately
installable backends and packaged guest packages.

Example:
```python
from hyperlight_sandbox import Sandbox

sandbox = Sandbox(backend="wasm", module="python_guest.path")
sandbox.register_tool("add", lambda a=0, b=0: a + b)

result = sandbox.run("""
result = call_tool('add', a=3, b=4)
print(result)
""")
print(result.stdout)  # "7\n"
```

Sections: hyperlight-sandbox, Quick Start, Snapshot Semantics, Build

</details>

### hyundai-kia-connect-api

Python API for Hyundai, Kia, and Genesis car infotainment systems

`pip install hyundai-kia-connect-api` · installs (wheel) · licence: MIT License · rank 9261 · last release 2026-11-08 · [PyPI](https://pypi.org/project/hyundai-kia-connect-api/)

<details><summary>README extract</summary>

Example:
```python
# login

login(self)

# OTP Details

# Sent OTP
send_otp(self, method)

# Verify OTP
verify_otp(self, otp_code)

# Checks the token is still valid and updates it if not.  Should be called before anything else if the code has been running for any length of time.
check_and_refresh_token(self)

...
```

Sections: Introduction, API Usage, China (Hyundai Bluelink / Kia UVO CN), MQTT push (Europe CCI/GSPA), CLI Usage

</details>

### home-assistant-frontend

The Home Assistant frontend

`pip install home-assistant-frontend` · installs (wheel) · licence: Apache-2.0 · rank 9278 · last release 2026-11-06 · [PyPI](https://pypi.org/project/home-assistant-frontend/)

<details><summary>README extract</summary>

This is the repository for the official Home Assistant frontend.

- View demo of Home Assistant
- More information about Home Assistant
- Frontend development instructions

Sections: Home Assistant Frontend, Classic environment

</details>

### hyperon-das

Query Engine API for Distributed AtomSpace

`pip install hyperon-das` · installs (wheel) · licence: not stated · rank 9513 · last release 2025-04-09 · [PyPI](https://pypi.org/project/hyperon-das/)

<details><summary>README extract</summary>

A data manipulation API for Distributed Atomspace (DAS). It allows queries with pattern matching capabilities and traversal of the Atomspace hypergraph.

</details>

### htbuilder

A purely-functional HTML builder for Python. Think JSX rather than templates.

`pip install htbuilder` · installs from source (sdist only) · licence: Apache Software License · rank 9550 · last release 2025-01-09 · [PyPI](https://pypi.org/project/htbuilder/)

<details><summary>README extract</summary>

htbuilder lets you build HTML strings using a purely functional syntax in Python.
Why use templating languages when you can just use functions?

(PS: If you like this, check out jsbuilder which
lets you build JavaScript strings by simply annotating Python functions!)

Example:
```python
# Import any tag you want from htbuilder, and it just works!
from htbuilder import div

dom = div('Hello world!')
```

Sections: htbuilder — tiny HTML string builder for Python, Usage, Multiple children, Programmatically add children, Conditionally add elements, Modify elements imperatively, Styling, Underscores are magic, Use underscores instead of dashes, Prefix with underscore to avoid reserved words

</details>

### hdrpy

HDR histogram implementation based on numpy

`pip install hdrpy` · installs (wheel) · licence: Apache Software License · rank 9553 · last release 2018-08-06 · [PyPI](https://pypi.org/project/hdrpy/)

### html-to-json

Convert html to json.

`pip install html-to-json` · installs (wheel) · licence: MIT License · rank 9606 · last release 2026-05-13 · [PyPI](https://pypi.org/project/html-to-json/) · [docs](https://github.com/fhightower/html-to-json) · [source](https://github.com/fhightower/html-to-json)

<details><summary>README extract</summary>

Convert HTML and/or HTML tables to JSON.

If this library is useful to you or if you're using this library for a business - please consider sponsoring me. Even a small sponsorship allows me to prioritize work on this library and ongoing maintainance. Thanks!

Example:
```python
import html_to_json

html_string = """

        #
        Malware
        MD5
        Date Added

        25548
        DarkComet
        034a37b2a2307f876adc9538986d7b86
        July 9, 2018, 6:25 a.m.

        25547
        DarkComet
        706eeefbac3de4d58b27d964173999c3
        July 7, 2018, 6:25 a.m.
    """
...
```

Sections: HTML to JSON, Usage, Example, HTML Tables to JSON, Preserving nested tags in table cells

</details>

### heroku3

Heroku API Wrapper.

`pip install heroku3` · installs (wheel) · licence: MIT License · rank 9808 · last release 2023-04-17 · [PyPI](https://pypi.org/project/heroku3/)

<details><summary>README extract</summary>

This is the updated Python wrapper for the Heroku API V3.
The Heroku REST API allows Heroku users to manage their accounts, applications, addons, and
other aspects related to Heroku. It allows you to easily utilize the Heroku
platform from your applications.

First instantiate a heroku_conn as above:
Interact with your applications:

Example:
```python
heroku_conn.apps(order_by='name')
```

Sections: Heroku3.py, Introduction, General notes on Debugging, Ratelimit Remaining, Last Request Id, General notes about list Objects, Examples, General Notes on Objects, Switching Accounts Mid Flow, Legacy API Calls, Object API, Account, SSH Keys, Account Features (Heroku Labs)

</details>

### hyper

HTTP/2 Client for Python

`pip install hyper` · installs (wheel) · licence: MIT License · rank 10005 · last release 2016-09-27 · [PyPI](https://pypi.org/project/hyper/)

<details><summary>README extract</summary>

HTTP is changing under our feet. HTTP/1.1, our old friend, is being
supplemented by the brand new HTTP/2 standard. HTTP/2 provides many benefits:
improved speed, lower bandwidth usage, better connection management, and more.

`hyper` provides these benefits to your Python code. How? Like this:
Simple.

Example:
```python
from hyper import HTTPConnection

conn = HTTPConnection('http2bin.org:443')
conn.request('GET', '/get')
resp = conn.get_response()

print(resp.read())
```

Sections: Hyper: HTTP/2 Client for Python, Caveat Emptor!, Versions, Compatibility, Documentation, v0.7.0 (2016-09-27), 0.6.2 (2016-06-13), 0.6.1 (2016-06-13), 0.6.0 (2016-05-06), 0.5.0 (2015-10-11), 0.4.0 (2015-06-21), 0.3.1 (2015-04-03), 0.3.0 (2015-04-03), 0.2.2 (2015-04-03)

</details>

### hkdf

HMAC-based Extract-and-Expand Key Derivation Function (HKDF)

`pip install hkdf` · installs from source (sdist only) · licence: BSD License · rank 10227 · last release 2015-06-16 · [PyPI](https://pypi.org/project/hkdf/)

<details><summary>README extract</summary>

This module implements the HMAC Key Derivation function, defined at

There are two interfaces: a functional interface, with separate extract
and expand functions as defined in the draft RFC, and a wrapper class for
these functions. ...

Example:
```python
from binascii import unhexlify
prk = hkdf_extract(unhexlify(b"8e94ef805b93e683ff18"), b"asecretpassword")
key = hkdf_expand(prk, b"context1", 16)
```

Sections: HKDF - HMAC Key Derivation Function, Functional interface, `Hkdf` wrapper class

</details>

### hightime

Hightime Python API

`pip install hightime` · installs (wheel) · licence: MIT License · rank 10380 · last release 2025-10-02 · [PyPI](https://pypi.org/project/hightime/) · [docs](https://hightime.readthedocs.io) · [source](https://github.com/ni/hightime)

<details><summary>README extract</summary>

Features:
Hightime allows for up to yoctosecond precision replacements for the datetime datetime
and timedelta types.

Example:
```python
>>> from hightime import datetime
>>> from hightime import timedelta

>>> high_noon = datetime(
...   year=1952,
...   month=7,
...   day=24,
...   hour=12,
...   minute=0,
...   second=30,
...   microsecond=0,
... )

>>> print(high_noon)
1952-07-24 12:00:30

>>> hesitation = timedelta(microseconds=10, femtoseconds=203456)

>>> print(hesitation)
...
```

Sections: Hightime, Overview, Examples

</details>

### hpp-fcl

An extension of the Flexible Collision Library

`pip install hpp-fcl` · installs from source (sdist only) · licence: not stated · rank 10389 · last release 2024-03-12 · [PyPI](https://pypi.org/project/hpp-fcl/)

<details><summary>README extract</summary>

FCL was forked in 2015. Since then, a large part of the code has been rewritten or removed (for the unused and untested part).
The broad phase was reintroduced by J. Carpentier in 2022 based on the FCL version 0.7.0.

Compared to the original FCL library, the main new features are: ...

Sections: HPP-FCL — An extension of the Flexible Collision Library, New features, A high-performance library

</details>

### hatch-nodejs-version

Hatch plugin for versioning from a package.json file

`pip install hatch-nodejs-version` · installs (wheel) · licence: MIT · rank 10484 · last release 2025-07-24 · [PyPI](https://pypi.org/project/hatch-nodejs-version/) · [source](https://github.com/agoose77/hatch-nodejs-version)

<details><summary>README extract</summary>

This package provides two Hatch plugins:

- version source plugin that reads/writes the package version
 from the `version` field of the Node.js `package.json` file.
- metadata hook plugin that reads PEP 621 metadata from the
 Node.js `package.json` file.

Table of Contents

- Global dependency
- Version source
- Metadata hook
- License ...

Sections: hatch-nodejs-version, Global dependency, Version source, Semver, Version source options, Metadata hook, Metadata hook options

</details>

### higgsfield-client

Higgsfield API Python SDK

`pip install higgsfield-client` · installs (wheel) · licence: Apache-2.0 · rank 10655 · last release 2026-09-17 · [PyPI](https://pypi.org/project/higgsfield-client/) · [source](https://github.com/higgsfield-ai/higgsfield-client)

<details><summary>README extract</summary>

The official Python SDK for Higgsfield AI. Supports both synchronous and asynchronous usage.

Example:
```python
import higgsfield_client

# Submit and wait for result
result = higgsfield_client.subscribe(
    'bytedance/seedream/v4/text-to-image',
    arguments={
        'prompt': 'A serene lake at sunset with mountains',
        'resolution': '2K',
        'aspect_ratio': '16:9',
        'camera_fixed': False
    }
)

print(result'images'['url'])
```

Sections: Higgsfield Python Client, Authentication, Quick Start, Usage Patterns, Pattern 1: Simple Submit and Wait, Pattern 2: Submit and Track Progress, Pattern 3: Submit with Callbacks, Pattern 4: Manage Existing Requests, File Uploads, Upload bytes, Upload by path, Upload PIL Images, Async Uploads, Agent API

</details>

### HiYaPyCo

Hierarchical Yaml Python Config

`pip install HiYaPyCo` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 10668 · last release 2024-10-20 · [PyPI](https://pypi.org/project/HiYaPyCo/)

_README extract left out: share-alike licence._

### hello-world

UNKNOWN

`pip install hello-world` · installs from source (sdist only) · licence: UNKNOWN · rank 10763 · last release 2013-12-24 · [PyPI](https://pypi.org/project/hello-world/)

### hellosign-python-sdk

A Python wrapper for the HelloSign API (http://www.hellosign.com/api)

`pip install hellosign-python-sdk` · installs (wheel) · licence: MIT License · rank 10906 · last release 2020-04-01 · [PyPI](https://pypi.org/project/hellosign-python-sdk/)

<details><summary>README extract</summary>

Hellosign Python SDK

A Python wrapper for the HelloSign API

Sections: Configuration, Usage, Account, Get current account information, Update your account information, Create a new HelloSign account, Signature Request, Get a Signature Request, Get a list of your Signature Requests, Send a Signature Request, Send a Signature Request with Template, Embedded, Embedded signing, Embedded requesting

</details>

### http_client

Fast and robust HTTP client based on PyCurl

`pip install http_client` · installs from source (sdist only) · licence: MIT · rank 10975 · last release 2017-08-28 · [PyPI](https://pypi.org/project/http_client/)

### hsms

Hardware security module simulator for chia bls12_381 signatures

`pip install hsms` · installs (wheel) · licence: not stated · rank 11311 · last release 2025-11-20 · [PyPI](https://pypi.org/project/hsms/)

<details><summary>README extract</summary>

HSMS: hardware security module software/simulator

This project is intended to run on an air-gapped computer to sign chia spends using bls12_381 keys.

Install

`$ pip install -e .`

If on windows, you need one extra package:

`$ pip install pyreadline`

Tools

Command-line tools installed include: ...

</details>

### historydict

A persistent dictionary with history backed by sqlite

`pip install historydict` · installs (wheel) · licence: not stated · rank 11349 · last release 2023-08-05 · [PyPI](https://pypi.org/project/historydict/)

### hatch_build_scripts

Dependency injection without the boilerplate.

`pip install hatch_build_scripts` · installs (wheel) · licence: not stated · rank 11720 · last release 2025-05-29 · [PyPI](https://pypi.org/project/hatch_build_scripts/) · [source](https://github.com/rmorshea/hatch-build-scripts)

<details><summary>README extract</summary>

A plugin for Hatch that allows you to run arbitrary
build scripts and include their artifacts in your package distributions.

Sections: Hatch Build Scripts, Usage

</details>

### hangul-romanize

Rominize Hangul strings.

`pip install hangul-romanize` · installs (wheel) · licence: not stated · rank 11763 · last release 2020-04-07 · [PyPI](https://pypi.org/project/hangul-romanize/)

<details><summary>README extract</summary>

You can install the package from PyPI

 $ pip install hangul-romanize

Example:
```python
>>> from hangul_romanize import Transliter
>>> from hangul_romanize.rule import academic
>>>
>>> transliter = Transliter(academic)
>>> print(transliter.translit(u'안녕하세요'))
annyeonghase-yo
```

Sections: Hangul romanization tool, Example

</details>

### hydra-submitit-launcher

Submitit Launcher for Hydra apps

`pip install hydra-submitit-launcher` · installs (wheel) · licence: MIT License · rank 11833 · last release 2022-05-17 · [PyPI](https://pypi.org/project/hydra-submitit-launcher/)

<details><summary>README extract</summary>

Provides a `Submitit` based Hydra Launcher supporting SLURM .

See website for more information

</details>

### hf

CLI extracted from the huggingface_hub library to interact with the Hugging Face Hub

`pip install hf` · installs (wheel) · licence: Apache · rank 11883 · last release 2026-10-29 · [PyPI](https://pypi.org/project/hf/)

<details><summary>README extract</summary>

The official Python client for the Huggingface Hub.

CLI Documentation:

Source Code:

> [!TIP]
> This package provides a clean CLI interface via `uvx hf`. It is not meant to be used as a package in scripts. Use `huggingface_hub` instead.

Sections: Usage, Note

</details>

### hindsight-api-slim

Hindsight: Agent Memory That Learns

`pip install hindsight-api-slim` · installs (wheel) · licence: MIT · rank 11969 · last release 2026-11-03 · [PyPI](https://pypi.org/project/hindsight-api-slim/)

<details><summary>README extract</summary>

Memory System for AI Agents — Temporal + Semantic + Entity Memory Architecture using PostgreSQL with pgvector.

Hindsight gives AI agents persistent memory that works like human memory: it stores facts, tracks entities and relationships, handles temporal reasoning ("what happened last spring?"), and forms opinions based on configurable disposition ...

Features:
- Multi-Strategy Retrieval (TEMPR) — Semantic, keyword, graph, and temporal search combined with RRF fusion
- Entity Graph — Automatic entity extraction and relationship tracking
- Temporal Reasoning — Native support for time-based queries ...

Example:
```python
from hindsight_api import MemoryEngine

# Create and initialize the memory engine
memory = MemoryEngine()
await memory.initialize()

# Create a memory bank for your agent
...

</details>

### h5grove

Core utilities to serve HDF5 file contents

`pip install h5grove` · installs (wheel) · licence: not stated · rank 12007 · last release 2026-04-14 · [PyPI](https://pypi.org/project/h5grove/) · [docs](https://silx-kit.github.io/h5grove/) · [source](https://github.com/silx-kit/h5grove)

### hindsight-embed

Hindsight embedded CLI - local memory operations without a server

`pip install hindsight-embed` · installs (wheel) · licence: MIT · rank 12062 · last release 2026-11-03 · [PyPI](https://pypi.org/project/hindsight-embed/)

<details><summary>README extract</summary>

Hindsight embedded CLI - local memory operations with automatic daemon management.

This package provides a simple CLI for storing and recalling memories using Hindsight's memory engine. It automatically manages a background daemon for fast operations - no manual server setup required. ...

Sections: hindsight-embed, How It Works, Quick Start, Commands, configure, memory retain, memory recall, memory reflect, bank list, profile, daemon, Configuration, Interactive Setup, Environment Variables

</details>

### h3-pyspark

PySpark bindings for H3, a hierarchical hexagonal geospatial indexing system

`pip install h3-pyspark` · installs (wheel) · licence: MIT License · rank 12089 · last release 2022-03-10 · [PyPI](https://pypi.org/project/h3-pyspark/)

<details><summary>README extract</summary>

PySpark bindings for the H3 core library.

For available functions, please see the vanilla Python binding documentation at:

- uber.github.io/h3-py

Example:
```python
>>> from pyspark.sql import SparkSession, functions as F
>>> import h3_pyspark
>>>
>>> spark = SparkSession.builder.getOrCreate()
>>> df = spark.createDataFrame([{"lat": 37.769377, "lng": -122.388903, 'resolution': 9}])
>>>
>>> df = df.withColumn('h3_9', h3_pyspark.geo_to_h3('lat', 'lng', 'resolution'))
>>> df.show()

...
```

Sections: Usage, Extension Functions, Assumptions, Indexing, `index_shape(geometry: Column, resolution: Column)`, Buffers, `k_ring_distinct(cells: Column, distance: Column)`, Spatial Joins, Publishing New Versions

</details>

### hacking

OpenStack Hacking Guideline Enforcement

`pip install hacking` · installs (wheel) · licence: Apache-2.0 · rank 12116 · last release 2026-06-11 · [PyPI](https://pypi.org/project/hacking/) · [source](https://opendev.org/openstack/hacking)

<details><summary>README extract</summary>

hacking is a set of flake8 plugins that test and enforce the
OpenStack StyleGuide

Hacking pins its dependencies, as a new release of some dependency can break
hacking based gating jobs. This is because new versions of dependencies can
introduce new rules, or make existing rules stricter.

Example:
```python
from hacking import core
...
@core.flake8ext
def import_no_db_in_virt(logical_line, filename):
    ...

class CheckForStrUnicodeExc(BaseASTChecker):
   name = "check_for_str_unicode_exc"
   version = "1.0"
   ...
```

Sections: Introduction, Origin, Versioning, Enabling off-by-default checks, Local Checks

</details>

### h2ogpte

Client library for Enterprise h2oGPTe

`pip install h2ogpte` · installs (wheel) · licence: not stated · rank 12252 · last release 2026-10-01 · [PyPI](https://pypi.org/project/h2ogpte/) · [docs](https://h2oai.github.io/h2ogpte/) · [source](https://github.com/h2oai/h2ogpte)

<details><summary>README extract</summary>

- RAG Benchmarks: latest results and how to reproduce

We recommend installing the client with the same version as the software:

Example:
```python
from h2ogpte import H2OGPTE

client = H2OGPTE(
    address='
    api_key='sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
)

# Create a new collection
collection_id = client.create_collection(
    name='Contracts',
    description='Paper clip supply contracts',
)

# Create documents
...
```

Sections: Python Client and Documentation, API Keys and Python Client Examples, Global API keys, Collection-specific API keys, OpenAI-compatible API

</details>

### hatch-regex-commit

Hatch plugin to create a commit and tag when bumping version

`pip install hatch-regex-commit` · installs (wheel) · licence: MIT · rank 12278 · last release 2025-09-29 · [PyPI](https://pypi.org/project/hatch-regex-commit/) · [docs](https://github.com/frankie567/hatch-regex-commit#readme) · [source](https://github.com/frankie567/hatch-regex-commit)

<details><summary>README extract</summary>

This provides a plugin for Hatch that automatically creates a Git commit and tag after version bumping.

Ensure `hatch-regex-commit` is defined within the `build-system.requires` field in your `pyproject.toml` file.

The version source plugin name is `regex_commit`.

- *pyproject.toml*

- *hatch.toml*

Sections: hatch-regex-commit, Global dependency, Version source, Version source options, Examples, Basic, Custom commit message, Edit commit message in the editor before proceeding, Disable Git tag

</details>

### hampel

Python implementation of the Hampel Filter

`pip install hampel` · installs from source (sdist only) · licence: MIT License · rank 12869 · last release 2023-09-19 · [PyPI](https://pypi.org/project/hampel/)

<details><summary>README extract</summary>

> Warning: Starting from version 1.0.1, there are breaking changes in this library. Please review the Usage section for details and update your code accordingly.

The Hampel filter is generally used to detect anomalies in data with a timeseries structure.
It basically consists of a sliding window of a parameterizable size. ...

Example:
```python
import pandas as pd
from hampel import hampel

# Sample data as a pandas.Series
data = pd.Series([1.0, 2.0, 3.0, 100.0, 4.0, 5.0, 6.0])

# Apply the Hampel filter
result = hampel(data, window_size=3, n_sigma=3.0)

print(result.filtered_data)
```

Sections: Hampel, Usage, Parameters, Related Links

</details>

### hana-ml

Python Machine Learning Client for SAP HANA

`pip install hana-ml` · installs (wheel) · licence: SAP DEVELOPER LICENSE AGREEMENT · rank 13046 · last release 2026-09-22 · [PyPI](https://pypi.org/project/hana-ml/) · [docs](https://help.sap.com/doc/cd94b08fe2e041c2ba778374572ddba9/latest/en-US/hana_ml.html)

<details><summary>README extract</summary>

Introduction

Welcome to Python machine learning client for SAP HANA (hana-ml)!

This package enables Python data scientists to access SAP HANA data and build various machine learning models using the data directly in SAP HANA. This page provides an overview of hana-ml.

Overview ...

Sections: Establish a connection to SAP HANA, Create a SAP HANA DataFrame from select statement, Convert a SAP HANA DataFrame to be a pandas DataFrame, Convert a pandas DataFrame to be a SAP HANA DataFrame, An Classification Example

</details>

### honeycomb-beeline

Honeycomb library for easy instrumentation

`pip install honeycomb-beeline` · installs (wheel) · licence: Apache Software License · rank 13078 · last release 2024-03-07 · [PyPI](https://pypi.org/project/honeycomb-beeline/) · [source](https://github.com/honeycombio/beeline-python)

<details><summary>README extract</summary>

⚠️Note: Beelines are Honeycomb's legacy instrumentation libraries. We embrace OpenTelemetry as the effective way to instrument applications. For any new observability efforts, we recommend instrumenting with OpenTelemetry. ...

Sections: Honeycomb Beeline for Python, Compatible with, Updating to 3.3.0

</details>

### hopsworks-apigen

(no summary)

`pip install hopsworks-apigen` · installs (wheel) · licence: not stated · rank 13120 · last release 2026-03-20 · [PyPI](https://pypi.org/project/hopsworks-apigen/)

### hadolint-coatl

Python wrapper around invoking hadolint (https://github.com/hadolint/hadolint)

`pip install hadolint-coatl` · installs (wheel) · licence: MIT · rank 13178 · last release 2026-08-01 · [PyPI](https://pypi.org/project/hadolint-coatl/) · [source](https://github.com/coatl-dev/hadolint-coatl)

<details><summary>README extract</summary>

A python wrapper to provide a pip-installable [hadolint] binary. Inspired by
[shellcheck-py].

Internally this package provides a convenient way to download the pre-built
hadolint binary for your particular platform.

Sections: hadolint-coatl, Usage, As a pre-commit hook

</details>

### hyperleaup

Create and publish Tableau Hyper files from Apache Spark DataFrames and Spark SQL.

`pip install hyperleaup` · installs (wheel) · licence: Apache Software License · rank 13253 · last release 2023-09-06 · [PyPI](https://pypi.org/project/hyperleaup/)

<details><summary>README extract</summary>

Pronounced "hyper-loop". Create and publish Tableau Hyper files from Apache Spark DataFrames or Spark SQL.

Features:
Tableau Data Extracts can take hours to create and publish to a Tableau Server.
Sometimes this means waiting around most of the day for the data extract to complete. ...

Example:
```python
from hyperleaup import HyperFile

# Step 1: Create a Hyper File from Spark SQL
query = """
select *
  from transaction_history
 where action_date > '2015-01-01'
"""

hf = HyperFile(name="transaction_history", sql=query, is_dbfs_enabled=True)

# Step 2: Publish Hyper File to a Tableau Server
hf.publish(tableau_server_url,
           username,
...
```

...

</details>

### hsslms

Leighton-Micali Hash-Based Signatures

`pip install hsslms` · installs (wheel) · licence: MIT License · rank 13280 · last release 2024-04-11 · [PyPI](https://pypi.org/project/hsslms/) · [docs](https://pmvr.github.io/python-hsslms/) · [source](https://github.com/pypa/sampleproject/)

<details><summary>README extract</summary>

This is an implementation of Leighton-Micali Hash-Based Signatures in Python according to `RFC 8554 < The one time signature keys are generated by using pseudo random generator, which saves a lot of memory to store the private keys in ram and on harddisk.

The implementation is meant as a reference and for educational purposes. ...

</details>

### holehe

holehe allows you to check if the mail is used on different sites like twitter, instagram , snapchat and will retrieve information on sites with the forgotten password function.

`pip install holehe` · installs from source (sdist only) · licence: GNU General Public License v3 (GPLv3) · rank 13408 · last release 2022-07-21 · [PyPI](https://pypi.org/project/holehe/)

_README extract left out: share-alike licence._

### hadolint-py

Python wrapper around invoking hadolint (https://github.com/hadolint/hadolint)

`pip install hadolint-py` · installs (wheel) · licence: MIT · rank 13529 · last release 2026-10-29 · [PyPI](https://pypi.org/project/hadolint-py/)

<details><summary>README extract</summary>

A pre-commit hook for hadolint that automatically downloads and installs the hadolint binary — no manual installation required.

The official `hadolint/hadolint` repository provides a pre-commit hook configuration, but it does not auto-install the `hadolint` binary. Users who add it to their `.pre-commit-config.yaml` are met with: ...

Sections: hadolint-pre-commit, Background, Usage, Passing arguments, Using a configuration file, How it works, Comparison with alternatives, Versioning

</details>

### harlequin

The SQL IDE for Your Terminal.

`pip install harlequin` · installs (wheel) · licence: MIT · rank 13586 · last release 2026-10-26 · [PyPI](https://pypi.org/project/harlequin/) · [docs](https://harlequin.sh/docs/getting-started/index) · [source](https://github.com/tconbeer/harlequin)

<details><summary>README extract</summary>

The SQL IDE for Your Terminal.

> [!TIP]
> This README contains a small subset of the docs available at
> harlequin.sh.

Sections: Harlequin, Running Harlequin, Using Harlequin with DuckDB, Using Harlequin with SQLite and Other Adapters, Configuring Harlequin, Using Harlequin with Agents or in Scripts, Using Harlequin with Django, Keep Reading at harlequin.sh, Getting Help

</details>

### harness-python-sdk

harness python sdk package

`pip install harness-python-sdk` · installs (wheel) · licence: MIT License · rank 13728 · last release 2025-06-13 · [PyPI](https://pypi.org/project/harness-python-sdk/)

<details><summary>README extract</summary>

This repo is generated by Harness official swagger.json file, please follow up their site for getting newest updates,the copyright of the document and source code belongs to Harness Company.And the code has published to pypi site:
you can use below command to install:
you can find from below docs for more details

Example:
```python
from future import print_function
import time
import harness_python_sdk
from harness_python_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = harness_python_sdk.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
...
```

...

</details>

### html2pdf4doc

Python client for HTML2PDF4Doc JavaScript library.

`pip install html2pdf4doc` · installs (wheel) · licence: Apache Software License · rank 13743 · last release 2026-09-13 · [PyPI](https://pypi.org/project/html2pdf4doc/) · [source](https://github.com/mettta/html2pdf_python/)

<details><summary>README extract</summary>

html2pdf4doc_python is the Python wrapper/CLI for the
html2pdf4doc JavaScript
library that prints HTML pages into PDFs using Chrome/Chromedriver.

This repository focuses strictly on the Python-side automation layer. The
rendering logic remains in the JS core.

Sections: html2pdf4doc_python, Usage, Disable SSL (corporate environments), Pin a specific Chrome binary, Getting started

</details>

### hotglue-etl-exceptions

Exception classes for Hotglue ETL

`pip install hotglue-etl-exceptions` · installs (wheel) · licence: not stated · rank 13751 · last release 2026-01-08 · [PyPI](https://pypi.org/project/hotglue-etl-exceptions/)

<details><summary>README extract</summary>

Python module providing exception classes for Hotglue ETL operations.

Example:
```python
from hotglue_etl_exceptions import InvalidCredentialsError, InvalidPayloadError

# Raise InvalidCredentialsError exception
raise InvalidCredentialsError("Invalid username or password")

# Raise InvalidPayloadError exception
raise InvalidPayloadError("Payload validation failed")
```

Sections: hotglue-etl-exceptions, Usage, Exported Classes

</details>

### hydra-optuna-sweeper

Hydra Optuna Sweeper plugin

`pip install hydra-optuna-sweeper` · installs (wheel) · licence: MIT License · rank 14036 · last release 2026-09-14 · [PyPI](https://pypi.org/project/hydra-optuna-sweeper/)

<details><summary>README extract</summary>

Provides an Optuna based Hydra Sweeper.

See website for more information.

</details>

### honeybee-energy

Energy simulation library for honeybee.

`pip install honeybee-energy` · installs (wheel) · licence: AGPL-3.0 · rank 14118 · last release 2026-11-06 · [PyPI](https://pypi.org/project/honeybee-energy/)

_README extract left out: share-alike licence._

### hoimin

Mutation Testing CLI, Designed for AI Agents

`pip install hoimin` · installs (wheel) · licence: Elastic-2.0 · rank 14323 · last release 2026-11-06 · [PyPI](https://pypi.org/project/hoimin/) · [source](https://github.com/HayaoSuzuki/hoimin)

<details><summary>README extract</summary>

hoimin is a mutation testing CLI for Python, designed for AI agents to improve tests locally within explicit resource budgets.
It makes small changes to copies of your source and runs your tests to find behavior they do not check.

An agent investigates selected survivors, adds tests grounded in the intended behavior, and verifies the improvement. ...

Sections: hoimin, Quick start, Startup cleanup reports

</details>

### hyperloglog

HyperLogLog cardinality counter

`pip install hyperloglog` · installs (wheel) · licence: LGPL 2.1 or later · rank 14455 · last release 2026-07-08 · [PyPI](https://pypi.org/project/hyperloglog/)

_README extract left out: share-alike licence._

### hadolint-bin

A thin wrapper to distribute https://github.com/hadolint/hadolint via pip.

`pip install hadolint-bin` · installs (wheel) · licence: GPL-3.0 · rank 14722 · last release 2026-08-03 · [PyPI](https://pypi.org/project/hadolint-bin/) · [source](https://github.com/justin-yan/pybin)

_README extract left out: share-alike licence._

### hf-doc-builder

Doc building utility

`pip install hf-doc-builder` · installs (wheel) · licence: Apache Software License · rank 14857 · last release 2026-11-06 · [PyPI](https://pypi.org/project/hf-doc-builder/) · [source](https://github.com/huggingface/doc-builder)

<details><summary>README extract</summary>

This is the package we use to build the documentation of our Hugging Face repos.

Example:
```python
from pathlib import Path

from doc_builder.testing import DocIntegrationTest

class MyPageDocIntegrationTest(DocIntegrationTest):
    doc_path = Path(file).resolve().parents[2] / "docs" / "source" / "en" / "my_page.md"
```

Sections: doc-builder, Previewing, Doc building, Specifying a version, Page-level HTML build cache, Notebook conversion, Runnable code blocks, Doc styling, Using the pre-commit hook, Writing in notebooks, Templates for GitHub Actions, Enabling multilingual documentation, Machine-translated documentation, Redirects

</details>

### harvesters

Image Acquisition Library for GenICam-based Machine Vision System

`pip install harvesters` · installs (wheel) · licence: Apache Software License · rank 14927 · last release 2024-05-16 · [PyPI](https://pypi.org/project/harvesters/)

<details><summary>README extract</summary>

Harvester is a Python library that aims to make the image acquisition process in your computer vision application breathtakingly easy. Like the peasants/harvesters in the above drawing, it gathers the image data as its harvest and fills up your bucket/buffer. ...

Example:
```python
(genicam) kznr@Kazunaris-MacBook:~% ipython
Python 3.6.6 |Anaconda, Inc.| (default, Jun 28 2018, 11:07:29)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from harvesters.core import Harvester

In [2]: import numpy as np  # This is just for a demonstration.

...
```

...

</details>

### html-table-parser-python3

A small and simple HTML table parser not requiring any external dependency.

`pip install html-table-parser-python3` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 14942 · last release 2022-12-06 · [PyPI](https://pypi.org/project/html-table-parser-python3/)

_README extract left out: share-alike licence._

### hid

ctypes bindings for hidapi

`pip install hid` · installs (wheel) · licence: MIT License · rank 14949 · last release 2026-02-05 · [PyPI](https://pypi.org/project/hid/)

<details><summary>README extract</summary>

Example:
```python
import hid

vid = 0x046d    # Change it for your device
pid = 0xc534    # Change it for your device

with hid.Device(vid, pid) as h:
    print(f'Device manufacturer: {h.manufacturer}')
    print(f'Product: {h.product}')
    print(f'Serial Number: {h.serial}')
```

Sections: Linux, Arch Linux, CentOS/RHEL, Fedora, Ubuntu/Debian, Others, Windows, OSX, FreeBSD, Sample usage code

</details>

### hud-python

The HUD SDK was renamed to 'hud'. Install that instead.

`pip install hud-python` · installs from source (sdist only) · licence: MIT · rank 14953 · last release 2026-07-15 · [PyPI](https://pypi.org/project/hud-python/) · [docs](https://docs.hud.ai)

<details><summary>README extract</summary>

The HUD SDK was renamed on PyPI: `hud-python`
is now `hud`. To migrate:

Uninstalling both names first is safe in every state, including a broken or
half-migrated install:

Then replace `hud-python` with `hud` in requirements files, `pyproject.toml`,
Dockerfiles, and CI configs. The import name (`import hud`) and the CLI
(`hud`) are unchanged. ...

</details>

