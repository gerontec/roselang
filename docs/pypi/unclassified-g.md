# Unclassified / G

[Index](README.md) · 195 packages in this topic, by downloads.

### grpcio

HTTP/2-based RPC framework

`pip install grpcio` · installs (wheel) · licence: Apache-2.0 · rank 92 · last release 2026-10-30 · [PyPI](https://pypi.org/project/grpcio/) · [docs](https://grpc.github.io/grpc/python) · [source](https://github.com/grpc/grpc)

<details><summary>README extract</summary>

Package for gRPC Python.

Sections: gRPC Python, Troubleshooting, Versioning

</details>

### grpcio-status

Status proto mapping for gRPC

`pip install grpcio-status` · installs (wheel) · licence: Apache-2.0 · rank 96 · last release 2026-10-30 · [PyPI](https://pypi.org/project/grpcio-status/) · [docs](https://grpc.github.io/grpc/python/grpc_status.html)

### google-crc32c

A python wrapper of the C library 'Google CRC32C'

`pip install google-crc32c` · installs (wheel) · licence: Apache-2.0 · rank 195 · last release 2026-09-24 · [PyPI](https://pypi.org/project/google-crc32c/)

<details><summary>README extract</summary>

[](

This package wraps the `google/crc32c`
hardware-based implementation of the CRC32C hashing algorithm. Multiple wheels
are distributed as well as source. If a wheel is not published for the python
version and platform you are using, you will need to compile crc32c using a
C toolchain. ...

Sections: `google-crc32c`, Currently Published Wheels, Linux, Mac OS, Windows

</details>

### grpcio-tools

Protobuf code generator for gRPC

`pip install grpcio-tools` · installs (wheel) · licence: Apache-2.0 · rank 210 · last release 2026-10-30 · [PyPI](https://pypi.org/project/grpcio-tools/) · [source](https://github.com/grpc/grpc/tree/master/tools/distrib/python/grpcio_tools)

<details><summary>README extract</summary>

Package for gRPC Python tools.

Example:
```python
setuptools.setup(
  # ...
  cmdclass={
    'build_proto_modules': grpc_tools.command.BuildPackageProtos,
  }
  # ...
)
```

Sections: gRPC Python Tools, Troubleshooting, Usage

</details>

### GitPython

GitPython is a Python library used to interact with Git repositories

`pip install GitPython` · installs (wheel) · licence: BSD-3-Clause · rank 220 · last release 2026-10-14 · [PyPI](https://pypi.org/project/GitPython/) · [docs](https://gitpython.readthedocs.io/en/stable/) · [source](https://github.com/gitpython-developers/GitPython)

<details><summary>README extract</summary>

I started working on GitPython in 2009, back in the days when Python was 'my thing' and I had great plans with it.
Of course, back in the days, I didn't really know what I was doing and this shows in many places. Somewhat similar to
Python this happens to be 'good enough', but at the same time is deeply flawed and broken beyond repair. ...

Sections: Gitoxide: A peek into the future…, GitPython, REQUIREMENTS, From PyPI, From downloaded source code, By cloning the source code repository, Limitations, Leakage of System Resources, RUNNING TESTS, Test commands, CI (and tox), Configuration files, INFRASTRUCTURE, Projects using GitPython

</details>

### gitdb

Git Object Database

`pip install gitdb` · installs (wheel) · licence: BSD License · rank 237 · last release 2025-01-02 · [PyPI](https://pypi.org/project/gitdb/)

### graphql-core

GraphQL-core is a Python port of GraphQL.js, the JavaScript reference implementation for GraphQL.

`pip install graphql-core` · installs (wheel) · licence: MIT · rank 356 · last release 2026-11-06 · [PyPI](https://pypi.org/project/graphql-core/) · [docs](https://graphql-core-3.readthedocs.io/) · [source](https://github.com/graphql-python/graphql-core)

<details><summary>README extract</summary>

GraphQL-core 3 is a Python 3.10+ port of GraphQL.js,
the JavaScript reference implementation for GraphQL,
a query language for APIs created by Facebook.

An extensive test suite with over 3000 unit tests and 100% coverage replicates the
complete test suite of GraphQL.js, ensuring that this port is reliable and compatible
with GraphQL.js. ...

Example:
```python
from graphql import (
    GraphQLSchema, GraphQLObjectType, GraphQLField, GraphQLString)

schema = GraphQLSchema(
    query=GraphQLObjectType(
        name='RootQueryType',
        fields={
            'hello': GraphQLField(
                GraphQLString,
                resolve=lambda obj, info: 'world')
        }))
```

...

</details>

### google-cloud-audit-log

Google Cloud Audit Protos

`pip install google-cloud-audit-log` · installs (wheel) · licence: Apache Software License · rank 594 · last release 2026-10-22 · [PyPI](https://pypi.org/project/google-cloud-audit-log/)

<details><summary>README extract</summary>

|preview| |pypi| |versions|

`Audit Log`_:

- `Client Library Documentation`_
- `Product Documentation`_

.. |preview| image::
 :target:
.. |pypi| image::
 :target:
.. |versions| image::
 :target:
.. _Audit Log:
.. _Client Library Documentation:
.. _Product Documentation:

Quick Start ...

</details>

### gcsfs

Convenient Filesystem interface over GCS

`pip install gcsfs` · installs (wheel) · licence: BSD-3-Clause · rank 653 · last release 2026-10-16 · [PyPI](https://pypi.org/project/gcsfs/) · [docs](https://gcsfs.readthedocs.io) · [source](https://github.com/fsspec/gcsfs)

<details><summary>README extract</summary>

|Build Status|
|Docs|

GCSFS is a Python library that provides a familiar, file-system-like interface to Google Cloud Storage (GCS). Built on top of fsspec, it allows you to interact with cloud buckets as if they were local directories, making it a favorite for data scientists and engineers.

Example:
```python
import gcsfs

# Initialize the filesystem
fs = gcsfs.GCSFileSystem(project='my-google-project')

# List files in a bucket
files = fs.ls('my-bucket')

# Read a file directly into a string/bytes
with fs.open('my-bucket/data.txt', 'rb') as f:
    content = f.read()
```

Sections: gcsfs, Getting Started, Basic Usage, 1\. Hierarchical Namespace (HNS), 2\. Rapid Buckets (Zonal Storage), Integration & Auth, Authentication Modes

</details>

### ghapi

A python client for the GitHub API

`pip install ghapi` · installs (wheel) · licence: Apache-2.0 · rank 802 · last release 2026-10-27 · [PyPI](https://pypi.org/project/ghapi/) · [docs](https://ghapi.fast.ai/) · [source](https://github.com/fastai/ghapi)

<details><summary>README extract</summary>

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

> ghapi v2 (July 2026) is now async by default. Every API call is now awaited: `res = await api.repos.get()`. Top-level `await` works directly in Jupyter and modern REPLs; in scripts, use `asyncio.run`. For sync code (which should be largely compatible with v1), use `GhApi(sync=True)`. ...

Example:
```python
from ghapi.all import GhApi
```

Sections: ghapi, How to use - Python, Beyond the endpoints, GraphQL, How to use - command line

</details>

### grpcio-health-checking

Standard Health Checking Service for gRPC

`pip install grpcio-health-checking` · installs (wheel) · licence: Apache-2.0 · rank 807 · last release 2026-10-30 · [PyPI](https://pypi.org/project/grpcio-health-checking/) · [docs](https://grpc.github.io/grpc/python/grpc_health_checking.html)

<details><summary>README extract</summary>

Reference package for GRPC Python health checking.

Depends on the `grpcio` package, available from PyPI via `pip install grpcio`.

Sections: gRPC Python Health Checking, Dependencies

</details>

### google-re2

RE2 Python bindings

`pip install google-re2` · installs (wheel) · licence: BSD License · rank 823 · last release 2025-11-05 · [PyPI](https://pypi.org/project/google-re2/)

<details><summary>README extract</summary>

A drop-in replacement for the re module.

It uses RE2 under the hood, of course, so various PCRE features
(e.g. backreferences, look-around assertions) are not supported.
See for the canonical
reference, but known syntactic "gotchas" relative to Python are:

 * PCRE supports \Z and \z; RE2 supports \z; Python supports \z,
 but calls it \Z. ...

</details>

### google-pasta

pasta is an AST-based Python refactoring library

`pip install google-pasta` · installs (wheel) · licence: Apache Software License · rank 870 · last release 2020-03-13 · [PyPI](https://pypi.org/project/google-pasta/)

### ghp-import

Copy your docs directly to the gh-pages branch.

`pip install ghp-import` · installs (wheel) · licence: Apache Software License · rank 929 · last release 2022-05-02 · [PyPI](https://pypi.org/project/ghp-import/)

<details><summary>README extract</summary>

As part of gunicorn, Benoit Chesneau and Paul Davis
were looking at how to host documentation. There's the obvious method of
using GitHub's post-receive hook to trigger doc builds and rsync
to a webserver, but we ended up wanting to try out github's hosting to make the
whole interface a bit more robust. ...

Example:
```python
Usage: ghp-import [OPTIONS] DIRECTORY

Options:
  -n, --no-jekyll       Include a .nojekyll file in the branch.
  -c CNAME, --cname=CNAME
                        Write a CNAME file with the given CNAME.
  -m MESG, --message=MESG
                        The commit message to use on the target branch.
...
```

</details>

### grpc-interceptor

Simplifies gRPC interceptors

`pip install grpc-interceptor` · installs (wheel) · licence: MIT License · rank 947 · last release 2023-11-16 · [PyPI](https://pypi.org/project/grpc-interceptor/) · [docs](https://grpc-interceptor.readthedocs.io) · [source](https://github.com/d5h-foss/grpc-interceptor)

<details><summary>README extract</summary>

Simplified Python gRPC interceptors.

The Python `grpc` package provides service interceptors, but they're a bit hard to
use because of their flexibility. The `grpc` interceptors don't have direct access
to the request and response objects, or the service context. ...

Example:
```python
from grpc_interceptor import ServerInterceptor
from grpc_interceptor.exceptions import GrpcException

class ExceptionToStatusInterceptor(ServerInterceptor):
    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        context: grpc.ServicerContext,
        method_name: str,
    ) -> Any:
...
```

Sections: Summary, Usage, Server Interceptor, Client Interceptor, Documentation

</details>

### google-ads

Client library for the Google Ads API

`pip install google-ads` · installs (wheel) · licence: not stated · rank 1057 · last release 2026-10-29 · [PyPI](https://pypi.org/project/google-ads/) · [source](https://github.com/googleads/google-ads-python)

<details><summary>README extract</summary>

This project hosts the Python client library for the Google Ads API.

Features:
* Distributed via PyPI.
* Easy management of credentials.
* Easy creation of Google Ads API service clients.

Sections: Google Ads API Client Library for Python, Requirements, Features, Documentation, Miscellaneous

</details>

### gast

Python AST that abstracts the underlying Python version

`pip install gast` · installs (wheel) · licence: BSD License · rank 1078 · last release 2025-11-29 · [PyPI](https://pypi.org/project/gast/)

<details><summary>README extract</summary>

A generic AST to represent Python2 and Python3's Abstract Syntax Tree(AST).

GAST provides a compatibility layer between the AST of various Python versions,
as produced by ``ast.parse`` from the standard ``ast`` module.

</details>

### gremlinpython

Gremlin-Python for Apache TinkerPop

`pip install gremlinpython` · does not install on CPython 3.14 · licence: Apache Software License · rank 1082 · last release 2026-09-08 · [PyPI](https://pypi.org/project/gremlinpython/)

<details><summary>README extract</summary>

Apache TinkerPop™
is a graph computing framework for both graph databases (OLTP) and
graph analytic systems (OLAP). Gremlin
is the graph traversal language of
TinkerPop. It can be described as a functional, data-flow language that enables users to succinctly express complex
traversals on (or queries of) their application's property graph. ...

Example:
```python
from gremlin_python.process.traversal import T
from gremlin_python.process.traversal import Cardinality

id = T.id
single = Cardinality.single

def create_vertex(self, vid, vlabel):
    # default database cardinality is used when Cardinality argument is not specified
    g.add_v(vlabel).property(id, vid). \
...
```

Sections: Apache TinkerPop - Gremlin Python, Sample Traversals, Create Vertex, Find Vertices, Update Vertex

</details>

### gepa

A framework for optimizing textual system components (AI prompts, code snippets, etc.) using LLM-based reflection and Pareto-efficient evolutionary search.

`pip install gepa` · installs (wheel) · licence: MIT · rank 1262 · last release 2026-07-15 · [PyPI](https://pypi.org/project/gepa/)

<details><summary>README extract</summary>

Optimize any text parameter — prompts, code, agent architectures, configurations — using LLM-based reflection and Pareto-efficient evolutionary search.

 Website  |
 Quick Start  |
 Paper  |
 Blog  |
 Discord

GEPA (Genetic-Pareto) is a framework for optimizing any system with textual parameters against any evaluation metric. ...

Example:
```python
import gepa

trainset, valset, _ = gepa.examples.aime.init_dataset()

seed_prompt = {
    "system_prompt": "You are a helpful assistant. Answer the question. "
                     "Put your final answer in the format '### '"
}

result = gepa.optimize(
    seed_candidate=seed_prompt,
    trainset=trainset,
    valset=valset,
...
```

...

</details>

### giturlparse

A Git URL parsing module (supports parsing and rewriting)

`pip install giturlparse` · installs (wheel) · licence: Apache Software License · rank 1264 · last release 2026-10-13 · [PyPI](https://pypi.org/project/giturlparse/)

<details><summary>README extract</summary>

Parse & rewrite git urls (supports GitHub, Bitbucket, FriendCode, Assembla, Gitlab ...)

This is a fork of giturlparse.py with updated parsers.

Original project can be found at

Features:
- Allow rewriting repo and owner (#0)

Example:
```python
from giturlparse import parse

p = parse('git@bitbucket.org:AaronO/some-repo.git')

p.host, p.owner, p.repo

# => ('bitbucket.org', 'AaronO', 'some-repo')
```

Sections: giturlparse, Examples, Exposed attributes, Parse, Rewrite, URLS, Validate, Tests, 0.16.0 (2026-10-13), Bugfixes, 0.15.0 (2026-06-16), 0.14.0 (2025-10-22), Features

</details>

### grpcio-reflection

Standard Protobuf Reflection Service for gRPC

`pip install grpcio-reflection` · installs (wheel) · licence: Apache-2.0 · rank 1518 · last release 2026-10-30 · [PyPI](https://pypi.org/project/grpcio-reflection/) · [docs](https://grpc.github.io/grpc/python/grpc_reflection.html)

<details><summary>README extract</summary>

Reference package for reflection in GRPC Python.

Depends on the `grpcio` package, available from PyPI via `pip install grpcio`.

Sections: gRPC Python Reflection package, Dependencies

</details>

### grpcio-gcp

gRPC extensions for Google Cloud Platform

`pip install grpcio-gcp` · installs (wheel) · licence: Apache Software License · rank 1577 · last release 2018-09-10 · [PyPI](https://pypi.org/project/grpcio-gcp/)

<details><summary>README extract</summary>

Package for gRPC-GCP Python.

Example:
```python
import google.protobuf.text_format

config = grpc_gcp.api_config_from_text_pb(
    pkg_resources.resource_string(name, 'spanner.grpc.config'))
```

Sections: gRPC-GCP Python, From PyPI, Usage

</details>

### github3.py

Python wrapper for the GitHub API(http://developer.github.com/v3)

`pip install github3.py` · installs (wheel) · licence: OSI Approved; BSD License · rank 1734 · last release 2023-04-26 · [PyPI](https://pypi.org/project/github3.py/) · [docs](https://github3.readthedocs.io) · [source](https://github.com/sigmavirus24/github3.py)

<details><summary>README extract</summary>

github3.py is a comprehensive, actively developed, and extraordinarily stable
wrapper around the GitHub API (v3).

Note: This library currently works with Python 3.7+ or pypy3. For older versions, please use version 1.3.0.

Sections: Dependencies, Examples, Contact Options

</details>

### gguf

Read and write ML models in GGUF for GGML

`pip install gguf` · installs (wheel) · licence: MIT License · rank 1830 · last release 2026-05-06 · [PyPI](https://pypi.org/project/gguf/) · [source](https://github.com/ggml-org/llama.cpp)

<details><summary>README extract</summary>

This is a Python package for writing binary files in the GGUF
(GGML Universal File) format.

See convert_hf_to_gguf.py
as an example for its usage.

Sections: gguf, API Examples/Simple Tools, Automatic publishing with CI, Manual publishing, Run Unit Tests, TODO

</details>

### groovy

A small Python library created to help developers protect their applications from Server Side Request Forgery (SSRF) attacks.

`pip install groovy` · installs (wheel) · licence: MIT License · rank 1955 · last release 2025-02-28 · [PyPI](https://pypi.org/project/groovy/) · [source](https://github.com/gradio-app/groovy)

<details><summary>README extract</summary>

Groovy is a Python-to-JavaScript transpiler, meaning that it converts Python functions to their JavaScript equivalents. It is used in the Gradio library, so that developers can write functions in Python and have them run as fast as client-side JavaScript ⚡. ...

Example:
```python
from groovy import transpile

def sum_range(n: int):
    total = 0
    for i in range(n):
        total = total + i
    return total

js_code = transpile(sum)
print(js_code)
```

Sections: 🚀 Features, 🔧 Usage, 🤔 Ambiguity

</details>

### grpc-stubs

Mypy stubs for gRPC

`pip install grpc-stubs` · installs (wheel) · licence: MIT License · rank 2005 · last release 2025-04-28 · [PyPI](https://pypi.org/project/grpc-stubs/)

<details><summary>README extract</summary>

> [!WARNING]
> 2025-04-28: The end of the line for `grpc-stubs`.
> My involvement with grpc ceased around 2019, and my knowledge of the minutiae faded
> with each passing year. As a consequence, this this project has been archived, but
> development will continue at
> typeshed. Thank you to
> the folks who helped prepare the code for
> merging. ...

</details>

### google-api-python-client-stubs

Type stubs for google-api-python-client

`pip install google-api-python-client-stubs` · installs (wheel) · licence: Apache-2.0 · rank 2283 · last release 2026-08-22 · [PyPI](https://pypi.org/project/google-api-python-client-stubs/)

<details><summary>README extract</summary>

This package provides type stubs for the google-api-python-client library.
It allows you to type check usage of the library with e.g. mypy and will also improve autocomplete in many editors.

This is in no way affiliated with Google. ...

Sections: Type stubs for google-api-python-client, Caveats, Explicit annotations, Performance, Recursive types, Stubs for non-API-specific parts

</details>

### gherkin-official

Gherkin parser (official, by Cucumber team)

`pip install gherkin-official` · installs (wheel) · licence: MIT · rank 2334 · last release 2026-08-05 · [PyPI](https://pypi.org/project/gherkin-official/) · [source](https://github.com/cucumber/gherkin.git)

<details><summary>README extract</summary>

Gherkin parser/compiler for Python. Please see Gherkin for details.

</details>

### greenback

Reenter an async event loop from synchronous code

`pip install greenback` · installs (wheel) · licence: Apache Software License; MIT License · rank 2335 · last release 2025-12-23 · [PyPI](https://pypi.org/project/greenback/)

<details><summary>README extract</summary>

Python 3.5 introduced `async`/`await` syntax for defining
functions that can run concurrently in a cooperative multitasking
framework such as `asyncio` or Trio. Such frameworks have a number of advantages
over previous approaches to concurrency: they scale better than threads and are
clearer about control flow
than the implicit cooperative ...

Example:
```python
import subprocess

def main():
    print_fact(10)

def print_fact(n, mult=1):
    """Print the value of *n* factorial times *mult*."""
    if n <= 1:
        print_value(mult)
    else:
        print_fact(n - 1, mult * n)

def print_value(n):
    """Print the value *n* in an unreasonably convoluted way."""
    assert isinstance(n, int)
...
```

Sections: Quickstart, Example

</details>

### gotrue

Python Client Library for Supabase Auth

`pip install gotrue` · installs (wheel) · licence: MIT License · rank 2456 · last release 2025-08-08 · [PyPI](https://pypi.org/project/gotrue/) · [docs](https://github.com/supabase/auth-py) · [source](https://github.com/supabase/auth-py)

<details><summary>README extract</summary>

The `gotrue` package name is deprecated and is not going to receive any more updates. Please, use `supabase_auth` instead.

1. Use `uv add supabase_auth` instead of `uv add gotrue`.
2. Replace `gotrue` with `supabase_auth` in your `requirements.txt`, `pyproject.toml`, `setup.py`, etc.
3. ...

Sections: ⚠️⚠️⚠️ Deprecation notice ⚠️⚠️⚠️, How to switch, Reasoning

</details>

### grandalf

Graph and drawing algorithms framework

`pip install grandalf` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 2570 · last release 2023-01-26 · [PyPI](https://pypi.org/project/grandalf/)

_README extract left out: share-alike licence._

### growthbook

Powerful Feature flagging and A/B testing for Python apps

`pip install growthbook` · installs (wheel) · licence: MIT License · rank 3044 · last release 2026-11-02 · [PyPI](https://pypi.org/project/growthbook/)

<details><summary>README extract</summary>

Features:
Powerful Feature flagging and A/B testing for Python apps.

- Lightweight and fast
- Local evaluation, no network requests required
- Flexible targeting
- Use your existing event tracking (GA, Segment, Mixpanel, custom) ...

Example:
```python
from growthbook import GrowthBook

# User attributes for targeting and experimentation
attributes = {
  "id": "123",
  "customUserAttribute": "foo"
}

# The parameter names matter: the SDK invokes this callback
# with keyword arguments (experiment=, result=, user_context=)
def on_experiment_viewed(experiment, result, user_context):
...
```

...

</details>

### graphifyy

AI coding assistant skill (Claude Code, CodeBuddy, Codex, OpenCode, Kilo Code, Cursor, Gemini CLI, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro, Pi, Devin CLI, Google Antigravity) - turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`pip install graphifyy` · installs (wheel) · licence: Apache-2.0 · rank 3165 · last release 2026-11-08 · [PyPI](https://pypi.org/project/graphifyy/) · [docs](https://docs.graphify.com) · [source](https://github.com/Graphify-Labs/graphify)

<details><summary>README extract</summary>

Read this in other languages

English | 简体中文 | 日本語 | 한국어 | Deutsch | Français | Español | हिन्दी | Português | Русский | العربية | فارسی | Italiano | Polski | Nederlands | Türkçe | Українська | Tiếng Việt | Bahasa Indonesia | Svenska | Ελληνικά | Română | Čeština | Suomi | Dansk | Norsk | Magyar | ภาษาไทย | Oʻzbekcha | 繁體中文 | Filipino | עברית ...

Features:
What you get out of the box:

| Capability | What you get |

| God nodes | The most-connected concepts, so you see what everything flows through |
| Communities | The graph split into subsystems (Leiden), with LLM-free labels |
| Cross-file links | ...

...

</details>

### github-copilot-sdk

Python SDK for GitHub Copilot CLI

`pip install github-copilot-sdk` · installs (wheel) · licence: MIT · rank 3220 · last release 2026-11-06 · [PyPI](https://pypi.org/project/github-copilot-sdk/) · [source](https://github.com/github/copilot-sdk)

<details><summary>README extract</summary>

Python SDK for programmatic control of GitHub Copilot CLI via JSON-RPC.

To use the SDK, you'll need:

- Python 3.11+

Features:
- ✅ Full JSON-RPC protocol support
- ✅ stdio, TCP, and in-process (FFI) transports
- ✅ Real-time streaming events
- ✅ Session history with `get_events()`
- ✅ Type hints throughout
- ✅ Async/await native ...

Example:
```python
import asyncio

from copilot import CopilotClient
from copilot.session_events import (
    AssistantMessageData,
    SessionAutopilotStoppedData,
    SessionIdleData,
    SessionMode,
)
from copilot.session import PermissionHandler

async def main():
    # Client automatically starts on enter and cleans up on exit
...
```

...

</details>

### gto

Version and deploy your models following GitOps principles

`pip install gto` · installs (wheel) · licence: Apache License 2.0 · rank 3372 · last release 2026-07-09 · [PyPI](https://pypi.org/project/gto/) · [source](https://github.com/iterative/gto)

<details><summary>README extract</summary>

Git Tag Ops. Turn your Git repository into an Artifact Registry:

- Registry: Track new artifacts and their versions for releases and significant
 changes.
- Lifecycle Management: Create actionable stages for versions marking status of
 artifact or it's readiness to be consumed by a specific environment. ...

Sections: GTO, Getting started, Copyright

</details>

### graphemeu

Unicode grapheme helpers

`pip install graphemeu` · installs (wheel) · licence: MIT · rank 3399 · last release 2026-09-22 · [PyPI](https://pypi.org/project/graphemeu/) · [docs](https://graphemeu.readthedocs.io/)

<details><summary>README extract</summary>

A Python package for working with user perceived characters. More specifically,
string manipulation and calculation functions for working with grapheme cluster
groups (graphemes) as defined by the Unicode Standard Annex #29.

documentation

Or similar.

The currently supported version of Unicode: 18.0.0. ...

Example:
```python
>>> string = 'u̲n̲d̲e̲r̲l̲i̲n̲e̲d̲'
>>> len(string)
20
>>> grapheme.length(string)
10
>>> string[:3]
'u̲n'
>>> grapheme.slice(string, 0, 3)
'u̲n̲d̲'
```

Sections: grapheme, What? Why?, Documentation, Performance, Examples of grapheme cluster groups, Unicode version upgrade

</details>

### grapheme

Unicode grapheme helpers

`pip install grapheme` · installs from source (sdist only) · licence: MIT · rank 3601 · last release 2020-03-07 · [PyPI](https://pypi.org/project/grapheme/)

<details><summary>README extract</summary>

A Python package for working with user perceived characters. More specifically,
string manipulation and calculation functions for working with grapheme cluster
groups (graphemes) as defined by the Unicode Standard Annex #29.

documentation

The currently supported version of Unicode: 13.0.0. ...

Example:
```python
>>> string = 'u̲n̲d̲e̲r̲l̲i̲n̲e̲d̲'
>>> len(string)
20
>>> grapheme.length(string)
10
>>> string[:3]
'u̲n'
>>> grapheme.substr(string, 0, 3)
'u̲n̲d̲'
```

Sections: grapheme, What? Why?, Documentation, Performance, Examples of grapheme cluster groups, Unicode version upgrade

</details>

### grain

Grain: A library for loading and transforming data for ML training.

`pip install grain` · installs (wheel) · licence: not stated · rank 3859 · last release 2026-06-17 · [PyPI](https://pypi.org/project/grain/)

<details><summary>README extract</summary>

Installation
| Quickstart
| Reference docs
| Change logs

Grain is a Python library for reading and processing data for training and
evaluating JAX models. It is flexible, fast and deterministic.

Grain allows to define data processing steps in a simple declarative way: ...

Example:
```python
import grain

dataset = (
    grain.MapDataset.source([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    .shuffle(seed=42)  # Shuffles elements globally.
    .map(lambda x: x+1)  # Maps each element.
    .batch(batch_size=2)  # Batches consecutive elements.
)

for batch in dataset:
  # Training step.
```

Sections: Grain - Feeding JAX Models, Quickstart, Citing Grain, Existing users

</details>

### git-filter-repo

Quickly rewrite git repository history

`pip install git-filter-repo` · installs (wheel) · licence: MIT License · rank 3887 · last release 2024-12-04 · [PyPI](https://pypi.org/project/git-filter-repo/) · [source](https://github.com/newren/git-filter-repo)

<details><summary>README extract</summary>

git filter-repo is a versatile tool for rewriting history, which includes
capabilities I have not found anywhere
else. It roughly falls into the
same space of tool as git
filter-branch but without the
capitulation-inducing poor
performance,
with far more capabilities, and with a design that scales usability-wise
beyond trivial rewriting cases. ...

Features:
This was covered in more detail in a Git Rev News article on
filter-repo,
but some highlights for the main competitors:

...

</details>

### geohash2

(Geohash fixed for python3) Module to decode/encode Geohashes to/from latitude and longitude. See http://en.wikipedia.org/wiki/Geohash

`pip install geohash2` · installs from source (sdist only) · licence: not stated · rank 3933 · last release 2017-07-06 · [PyPI](https://pypi.org/project/geohash2/)

<details><summary>README extract</summary>

This module provides functions to decode and encode Geohashes to and from latitude and longitude coordinates.

</details>

### googlesearch-python

A Python library for scraping the Google search engine.

`pip install googlesearch-python` · installs (wheel) · licence: MIT License · rank 3947 · last release 2025-01-21 · [PyPI](https://pypi.org/project/googlesearch-python/)

<details><summary>README extract</summary>

googlesearch is a Python library for searching Google, easily. googlesearch uses requests and BeautifulSoup4 to scrape Google.

Example:
```python
from googlesearch import search
search("Google")
```

Sections: googlesearch, Usage, Additional options

</details>

### googleads

Google Ads Python Client Library

`pip install googleads` · installs from source (sdist only) · licence: Apache Software License · rank 4018 · last release 2026-08-24 · [PyPI](https://pypi.org/project/googleads/)

<details><summary>README extract</summary>

The googleads Python Client Libraries support the following products:

* Google Ad Manager API

You can find more information about the Google Ads Python Client Libraries
here.

Sections: The googleads Python Client Libraries, Examples, Contact Us

</details>

### gym

Gym: A universal API for reinforcement learning environments

`pip install gym` · installs from source (sdist only) · licence: MIT · rank 4221 · last release 2022-10-04 · [PyPI](https://pypi.org/project/gym/)

### gidgethub

An async GitHub API library

`pip install gidgethub` · installs (wheel) · licence: Apache-2.0 AND MIT · rank 4239 · last release 2026-09-25 · [PyPI](https://pypi.org/project/gidgethub/) · [docs](https://gidgethub.readthedocs.io) · [source](https://github.com/gidgethub/gidgethub)

<details><summary>README extract</summary>

An asynchronous GitHub API library.

Sections: gidgethub, Goals, Alternative libraries, Aside*: what's with the name?

</details>

### grep-ast

A tool to grep through the AST of a source file

`pip install grep-ast` · installs (wheel) · licence: Apache Software License · rank 4373 · last release 2025-05-08 · [PyPI](https://pypi.org/project/grep-ast/)

<details><summary>README extract</summary>

Grep source code files and see matching lines with
useful context that show how they fit into the code.
See the loops, functions, methods, classes, etc
that contain all the matching lines.
Get a sense of what's inside a matched class or function definition. ...

Sections: grep-ast, Usage, Examples

</details>

### google-auth-stubs

Type stubs for google-auth

`pip install google-auth-stubs` · installs (wheel) · licence: Apache Software License · rank 4411 · last release 2024-08-26 · [PyPI](https://pypi.org/project/google-auth-stubs/) · [source](https://github.com/henribru/google-auth-stubs)

<details><summary>README extract</summary>

This package provides type stubs for the google-auth package.

This is in no way affiliated with Google.

The stubs were largely created automatically by stubgen.

</details>

### GPUtil

GPUtil is a Python module for getting the GPU status from NVIDA GPUs using nvidia-smi.

`pip install GPUtil` · installs from source (sdist only) · licence: MIT · rank 4465 · last release 2018-12-18 · [PyPI](https://pypi.org/project/GPUtil/)

### GitHubKit

GitHub SDK for Python

`pip install GitHubKit` · installs (wheel) · licence: MIT · rank 4524 · last release 2026-11-06 · [PyPI](https://pypi.org/project/GitHubKit/) · [docs](https://github.com/yanyongyu/githubkit) · [source](https://github.com/yanyongyu/githubkit)

<details><summary>README extract</summary>

_✨ The modern, all-batteries-included GitHub SDK for Python ✨_

_✨ Support both sync and async calls, fully typed ✨_

_✨ Always up to date, like octokit ✨_

 Documentation |
 Report Bug |
 GitHub Docs

githubkit aims to be an easy-to-use, fully typed, and always up-to-date GitHub SDK for Python. It is inspired by octokit. ...

Example:
```python
from githubkit import GitHub

github = GitHub("")
```

Sections: Getting Started, Usage

</details>

### gpytorch

An implementation of Gaussian Processes in Pytorch

`pip install gpytorch` · installs (wheel) · licence: MIT · rank 4533 · last release 2026-02-28 · [PyPI](https://pypi.org/project/gpytorch/) · [docs](https://gpytorch.readthedocs.io) · [source](https://github.com/cornellius-gp/gpytorch/)

<details><summary>README extract</summary>

GPyTorch is a Gaussian process library implemented using PyTorch. GPyTorch is designed for creating scalable, flexible, and modular Gaussian process models with ease.

Internally, GPyTorch differs from many existing approaches to GP inference by performing most inference operations using numerical linear algebra techniques like preconditioned ...

Sections: GPyTorch, Examples, Tutorials, and Documentation, Latest (Unstable) Version, ArchLinux Package, Citing Us, The Team

</details>

### gurobipy

Python interface to Gurobi

`pip install gurobipy` · installs (wheel) · licence: Proprietary · rank 4593 · last release 2026-08-25 · [PyPI](https://pypi.org/project/gurobipy/) · [docs](https://docs.gurobi.com)

<details><summary>README extract</summary>

The Gurobi Optimizer is a mathematical optimization software library for solving mixed-integer linear and quadratic optimization problems.

This package comes with a trial license that allows you to solve problems of limited size. As a student or staff member of an academic institution, you qualify for a free, full product license. ...

Example:
```python
# Solve the following MIP:
# maximize
# x +   y + 2 z
# subject to
# x + 2 y + 3 z <= 4
# x +   y       >= 1
# x, y, z binary

import gurobipy as gp

# Create a new model
m = gp.Model()

# Create variables
x = m.addVar(vtype='B', name="x")
y = m.addVar(vtype='B', name="y")
z = m.addVar(vtype='B', name="z")

# Set objective function
...
```

Sections: A simple example, Licensing information

</details>

### graphiti-core

A temporal graph building library

`pip install graphiti-core` · installs (wheel) · licence: Apache-2.0 · rank 4622 · last release 2026-10-20 · [PyPI](https://pypi.org/project/graphiti-core/) · [source](https://github.com/getzep/graphiti)

<details><summary>README extract</summary>

> [!NOTE]
> We're Hiring! Build context graphs that power reliable, personalized, fast production AI agents.
> Come build with us — we're hiring Engineers and Developer Relations folks. View open roles.

⭐ *Help us reach more developers and grow the Graphiti community. Star this repo!* ...

Features:
Traditional RAG approaches often rely on batch processing and static data summarization, making them inefficient for
frequently changing data. Graphiti addresses these challenges by providing: ...

Example:
```python
from openai import AsyncOpenAI
from graphiti_core import Graphiti
from graphiti_core.llm_client.azure_openai_client import AzureOpenAILLMClient
from graphiti_core.llm_client.config import LLMConfig
from graphiti_core.embedder.azure_openai import AzureOpenAIEmbedderClient

...

</details>

### gym-notices

Notices for gym

`pip install gym-notices` · installs (wheel) · licence: MIT License · rank 4715 · last release 2025-07-27 · [PyPI](https://pypi.org/project/gym-notices/)

<details><summary>README extract</summary>

This repository hosts notices for Gym that may be displayed on import on internet connected systems, in order to give notices if versions have major reproducibility issues, are very old and need to be upgraded (e.g. there's been issues with researchers using 4 year old versions of Gym for no reason), or other similar issues. ...

</details>

### gender-guesser

Get the gender from first name.

`pip install gender-guesser` · installs (wheel) · licence: GPLv3 · rank 4739 · last release 2016-12-05 · [PyPI](https://pypi.org/project/gender-guesser/)

_README extract left out: share-alike licence._

### google-cloud-alloydb-connector

A Python client library for connecting securely to your Google Cloud AlloyDB instances.

`pip install google-cloud-alloydb-connector` · installs (wheel) · licence: Apache-2.0 · rank 4811 · last release 2026-10-14 · [PyPI](https://pypi.org/project/google-cloud-alloydb-connector/) · [source](https://github.com/GoogleCloudPlatform/alloydb-python-connector.git)

<details><summary>README extract</summary>

[][ci-build]
[][pypi-docs]
[][pypi-docs]
[][pypi-docs]

The AlloyDB Python Connector is the recommended way to connect to AlloyDB from
Python applications. It provides:

- Secure connections — TLS 1.3 encryption and identity verification,
 independent of the database protocol ...

Example:
```python
import sqlalchemy
from google.cloud.alloydbconnector import Connector

INSTANCE_URI = "projects/MY_PROJECT/locations/MY_REGION/clusters/MY_CLUSTER/instances/MY_INSTANCE"

with Connector() as connector:
    pool = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=lambda: connector.connect(
            INSTANCE_URI,
...
```

...

</details>

### gevent-websocket

Websocket handler for the gevent pywsgi server, a Python network library

`pip install gevent-websocket` · installs (wheel) · licence: Copyright 2011-2017 Jeffrey Gelens <jeffrey@noppo.pro> · rank 4857 · last release 2017-03-12 · [PyPI](https://pypi.org/project/gevent-websocket/)

<details><summary>README extract</summary>

Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY ...

</details>

### gliner

Generalist model for NER (Extract any entity types from texts)

`pip install gliner` · installs (wheel) · licence: Apache-2.0 · rank 4864 · last release 2026-10-31 · [PyPI](https://pypi.org/project/gliner/)

<details><summary>README extract</summary>

Zero-shot NER | Streaming NER | Relation Extraction | PII Detection | Information Extraction | Token Classification

GLiNER is a framework for training and deploying small Named Entity Recognition (NER) models with zero-shot capabilities. ...

Features:
Zero-shot Recognition
Extract any entity type — no labeled data or task-specific training required

Runs Anywhere
CPU, INT8 quantization, torch.compile, ONNX export — deploy on any hardware ...

Example:
```python
from gliner import GLiNER

model = GLiNER.from_pretrained("gliner-community/gliner_small-v2.5")

text = """
Cristiano Ronaldo dos Santos Aveiro (born 5 February 1985) is a Portuguese
professional footballer who plays as a forward for and captains both Saudi Pro
League club Al Nassr and the Portugal national team.
"""

...
```

...

</details>

### google-python-cloud-debugger

Python Cloud Debugger

`pip install google-python-cloud-debugger` · does not install on CPython 3.14 · licence: Apache License, Version 2.0 · rank 5007 · last release 2023-06-06 · [PyPI](https://pypi.org/project/google-python-cloud-debugger/)

<details><summary>README extract</summary>

The Cloud Debugger lets you inspect the state of an application at any
code location without stopping or slowing it down. The debugger makes it
easier to view the application state without adding logging statements.

For more details please see

</details>

### gilknocker

(no summary)

`pip install gilknocker` · installs (wheel) · licence: not stated · rank 5073 · last release 2026-01-07 · [PyPI](https://pypi.org/project/gilknocker/) · [source](https://github.com/milesgranger/gilknocker)

### garminconnect

Python 3 API wrapper for Garmin Connect

`pip install garminconnect` · installs (wheel) · licence: MIT License · rank 5131 · last release 2026-10-23 · [PyPI](https://pypi.org/project/garminconnect/)

<details><summary>README extract</summary>

[][releases]
[][commits]
[](LICENSE)

The Garmin Connect API library comes with two examples:

- `example.py` - Simple getting-started example showing authentication, token storage, and basic API calls
- `demo.py` - Comprehensive demo providing access to 270 API methods organized into 15 categories for easy navigation

Example:
```python
import os
from getpass import getpass
from datetime import date
from garminconnect import Garmin

# First run: logs in and saves tokens to ~/.garminconnect
# Subsequent runs: loads saved tokens and auto-refreshes
client = Garmin(
    os.getenv("GARMIN_EMAIL"),
    getpass("Garmin password: "),
    prompt_mfa=lambda: input("MFA code: "),
)
...
```

...

</details>

### google-cloud-jupyter-config

Jupyter configuration utilities using gcloud

`pip install google-cloud-jupyter-config` · installs (wheel) · licence: Apache License 2.0 · rank 5188 · last release 2026-09-28 · [PyPI](https://pypi.org/project/google-cloud-jupyter-config/)

<details><summary>README extract</summary>

This package provides Python classes that can be used in the Jupyter config file
(e.g. `~/.jupyter/jupyter_lab_config.py`) in order to fill in some configuration
using the Google Cloud SDK's `gcloud` tool. ...

Example:
```python
import google.cloud.jupyter_config
google.cloud.jupyter_config.configure_gateway_client(c)
```

Sections: Notebook server configuration using the Google Cloud SDK, Included features, Prerequisites, Setup

</details>

### g2p-en

A Simple Python Module for English Grapheme To Phoneme Conversion

`pip install g2p-en` · installs (wheel) · licence: Apache Software License · rank 5362 · last release 2019-12-31 · [PyPI](https://pypi.org/project/g2p-en/)

<details><summary>README extract</summary>

[Update] * We removed TensorFlow from the dependencies. After all, it changes its APIs quite often, and we don't expect you to have a GPU. Instead, NumPy is used for inference.

This module is designed to convert English graphemes (spelling) to
phonemes (pronunciation). It is considered essential in several tasks
such as speech synthesis. ...

Example:
```python
from g2p_en import G2p

texts = ["I have $250 in my pocket.", # number -> spell-out
         "popular pets, e.g. cats and dogs", # e.g. -> for example
         "I refuse to collect the refuse around here.", # homograph
         "I'm an activationist."] # newly coined word
g2p = G2p()
for text in texts:
    out = g2p(text)
    print(out)
...
```

Sections: Algorithm, Environment, Dependencies, Usage

</details>

### gpxpy

GPX file parser and GPS track manipulation library

`pip install gpxpy` · installs (wheel) · licence: Apache License, Version 2.0 · rank 5435 · last release 2023-11-29 · [PyPI](https://pypi.org/project/gpxpy/)

<details><summary>README extract</summary>

This is a simple Python library for parsing and manipulating GPX files. GPX is an XML based format for GPS tracks.

You can see it in action on my online GPS track editor and organizer.

There is also a Golang port of gpxpy: gpxgo.

See also srtm.py if your track lacks elevation data.

Example:
```python
import gpxpy
import gpxpy.gpx

# Parsing an existing file:
# -------------------------

gpx_file = open('test_files/cerknicko-jezero.gpx', 'r')

gpx = gpxpy.parse(gpx_file)

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
...
```

Sections: gpxpy -- GPX file parser, Usage, GPX version, GPX extensions, XML parsing, GPX max speed, Pull requests, GPX tools

</details>

### grpcio-testing

Testing utilities for gRPC Python

`pip install grpcio-testing` · installs (wheel) · licence: Apache-2.0 · rank 5533 · last release 2026-10-30 · [PyPI](https://pypi.org/project/grpcio-testing/) · [docs](https://grpc.github.io/grpc/python/grpc_testing.html)

### google-antigravity

Google Antigravity SDK for building AI agents

`pip install google-antigravity` · installs (wheel) · licence: Apache Software License · rank 5538 · last release 2026-10-28 · [PyPI](https://pypi.org/project/google-antigravity/)

<details><summary>README extract</summary>

The Google Antigravity SDK is a Python SDK for building AI agents powered by
Antigravity and Gemini. It provides a secure, scalable, and stateful
infrastructure layer that abstracts the agentic loop, letting you focus on what
your agent *does* rather than how it runs.

Example:
```python
import asyncio
from google.antigravity.connections.local import LocalConnectionStrategy
from google.antigravity.conversation.conversation import Conversation
from google.antigravity.tools.tool_runner import ToolRunner

async def main():
    tool_runner = ToolRunner()
    strategy = LocalConnectionStrategy(
        tool_runner=tool_runner,
    )

...
```

...

</details>

### gpiod

Python bindings for libgpiod

`pip install gpiod` · installs (wheel) · licence: LGPL-2.1-or-later · rank 5596 · last release 2026-11-04 · [PyPI](https://pypi.org/project/gpiod/)

_README extract left out: share-alike licence._

### GitHubKit-schemas-2026-03-10

GitHub Schemas for GitHubKit

`pip install GitHubKit-schemas-2026-03-10` · installs (wheel) · licence: MIT · rank 5605 · last release 2026-11-05 · [PyPI](https://pypi.org/project/GitHubKit-schemas-2026-03-10/) · [docs](https://github.com/yanyongyu/githubkit) · [source](https://github.com/yanyongyu/githubkit)

<details><summary>README extract</summary>

_✨ The modern, all-batteries-included GitHub SDK for Python ✨_

_✨ Support both sync and async calls, fully typed ✨_

_✨ Always up to date, like octokit ✨_

 Documentation |
 Report Bug |
 GitHub Docs

This package provides the models and GitHub schemas for GitHubKit.

When GitHub schemas are updated, this package will be updated accordingly. ...

</details>

### GitHubKit-schemas

GitHub Schemas for GitHubKit

`pip install GitHubKit-schemas` · installs (wheel) · licence: MIT · rank 5609 · last release 2026-11-05 · [PyPI](https://pypi.org/project/GitHubKit-schemas/) · [docs](https://github.com/yanyongyu/githubkit) · [source](https://github.com/yanyongyu/githubkit)

<details><summary>README extract</summary>

_✨ The modern, all-batteries-included GitHub SDK for Python ✨_

_✨ Support both sync and async calls, fully typed ✨_

_✨ Always up to date, like octokit ✨_

 Documentation |
 Report Bug |
 GitHub Docs

This package provides the models and GitHub schemas for GitHubKit. ...

</details>

### gitdb2

A mirror package for gitdb

`pip install gitdb2` · installs (wheel) · licence: not stated · rank 5783 · last release 2020-02-23 · [PyPI](https://pypi.org/project/gitdb2/)

<details><summary>README extract</summary>

This is a mirror package for `gitdb < Consider installing it directly instead.

</details>

### google-cloud-profiler

Google Cloud Profiler Python Agent

`pip install google-cloud-profiler` · installs from source (sdist only) · licence: Apache Software License · rank 5934 · last release 2023-08-16 · [PyPI](https://pypi.org/project/google-cloud-profiler/)

<details><summary>README extract</summary>

Python profiling agent for
Google Cloud Profiler.

See
Google Cloud Profiler profiling Python code
for detailed documentation.

Sections: Google Cloud Python profiling agent, Troubleshooting, Resource temporarily unavailable errors with Python

</details>

### genagent

Python utilities for generative agent tasks, including LLM interactions and agent memory.

`pip install genagent` · installs (wheel) · licence: not stated · rank 6140 · last release 2025-12-17 · [PyPI](https://pypi.org/project/genagent/)

<details><summary>README extract</summary>

A Python package providing utilities for generative agent tasks, including:
- Interacting with LLM providers (OpenAI, Anthropic).
- Helper functions for prompt engineering and structured output.
- Basic agent memory and chat session management.

(See `genagent/init.py` for the current version)

Example:
```python
from genagent import gen, Agent, ChatSession, mod_gen, modular_instructions

# --- Basic text generation ---
response = gen("Tell me a concise joke.")
print(f"Joke: {response}")

# --- Agent memory example ---
my_agent = Agent(name="MyTestAgent")
my_agent.add_memory("The capital of France is Paris.")
...
```

Sections: GenAgent Utilities, Configuration, Usage, What's New in 0.2.1, What's New in 0.2.0

</details>

### g711

A small library for A-Law and u-Law audio coding

`pip install g711` · installs from source (sdist only) · licence: MIT License · rank 6179 · last release 2021-03-08 · [PyPI](https://pypi.org/project/g711/)

<details><summary>README extract</summary>

The library is written as an extension for python3 and allows to work simply with G711 encoded audio.

1. Python 3.5+
2. Numpy (will be installed anyway before the building procedure)
3. Tools for building C/C++ applications (GCC/Clang/VS build tools)

The library is written in pure C and relies exclusively on a python build system. ...

Sections: G711 A-Law / u-Law audio-coding library, Requirements, Implementation details, Functions

</details>

### gocardless-pro

A client library for the GoCardless API.

`pip install gocardless-pro` · installs (wheel) · licence: MIT · rank 6307 · last release 2026-11-05 · [PyPI](https://pypi.org/project/gocardless-pro/)

<details><summary>README extract</summary>

A Python client for interacting with the GoCardless API.

Tested against Python 3.9, 3.10, 3.11 and 3.12.

- "Getting Started" guide with copy and paste Python code samples
- API reference

Install from PyPI:

Example:
```python
import gocardless_pro
token = os.environ['ACCESS_TOKEN']
client = gocardless_pro.Client(access_token=token, environment='live')
```

Sections: GoCardless Python client library, Usage, Handling webhooks, Accessing the webhook ID, Available resources, Balances, Bank account details, Bank account holder verifications, Bank details lookups, Billing requests, Billing request flows, Billing request templates, Billing request with actions, Blocks

</details>

### github-action-utils

Python helpers for GitHub Actions workflow commands

`pip install github-action-utils` · installs (wheel) · licence: MIT · rank 6351 · last release 2026-10-20 · [PyPI](https://pypi.org/project/github-action-utils/)

<details><summary>README extract</summary>

Use GitHub Actions workflow commands from Python: annotate logs, share values
between steps, read inputs, and write job summaries.

Python 3.11+ · Linux, Windows, macOS · No runtime dependencies · Typed

> [!NOTE]
> See the changelog for breaking changes and upgrade instructions.

Contents ...

Example:
```python
gha.echo("Starting build")
gha.debug("Checking dependencies")
gha.warning("Unused variable", title="Lint", file="src/app.py", line=12, col=5)
gha.notice("Review this block", file="src/app.py", line=20, end_line=24)
```

...

</details>

### glum

High performance Python GLMs with all the features!

`pip install glum` · installs (wheel) · licence: BSD · rank 6446 · last release 2026-05-06 · [PyPI](https://pypi.org/project/glum/)

<details><summary>README extract</summary>

Documentation

Generalized linear models (GLM) are a core statistical tool that include many common methods like least-squares regression, Poisson regression, and logistic regression as special cases. At QuantCo, we have used GLMs in e-commerce pricing, insurance claims prediction, and more. ...

Example:
```python
>>> import pandas as pd
>>> from glum import GeneralizedLinearRegressor
>>>
>>> # This dataset contains house sale prices for King County, which includes
>>> # Seattle. It includes homes sold between May 2014 and May 2015.
>>> # To download, use: sklearn.datasets.fetch_openml(name="house_sales", version=3)
...
```

Sections: glum, A classic example predicting housing prices, Performance

</details>

### google-cloud-spark-connect

Managed Spark client library for Spark Connect

`pip install google-cloud-spark-connect` · installs (wheel) · licence: Apache 2.0 · rank 6456 · last release 2026-11-04 · [PyPI](https://pypi.org/project/google-cloud-spark-connect/)

<details><summary>README extract</summary>

A wrapper of the Apache Spark Connect
client with additional functionalities that allow applications to communicate
with a remote Managed Spark Session using the Spark Connect protocol without
requiring additional steps.

Example:
```python
from google.cloud.managed_spark_connect import ManagedSparkSession
spark = ManagedSparkSession.builder.getOrCreate()
```

Sections: Managed Spark Connect Client, Python versions, Setup, Usage, Builder Configuration, Configuration (environment variables), Reusing Named Sessions Across Notebooks, Instrumentation (opt-in), Interactive Extras, Opting out, Bundled Magics, `%dpip`, `%%sparksql`, Migrating from dataproc-spark-connect

</details>

### grpcio-observability

gRPC Python observability package

`pip install grpcio-observability` · installs (wheel) · licence: Apache-2.0 · rank 6576 · last release 2026-10-30 · [PyPI](https://pypi.org/project/grpcio-observability/) · [docs](https://grpc.github.io/grpc/python/grpc_observability.html) · [source](https://github.com/grpc/grpc/tree/master/src/python/grpcio_observability)

<details><summary>README extract</summary>

Package for gRPC Python Observability.

More details can be found in OpenTelemetry Metrics gRFC.

gRPC Python is a wrapper layer built upon the gRPC Core (written in C/C++). Most of telemetry data
is collected at core layer and then exported to Python layer. ...

Sections: gRPC Python Observability, How gRPC Python Observability Works, Dependencies, Usage

</details>

### genanki

Generate Anki decks programmatically

`pip install genanki` · installs (wheel) · licence: MIT · rank 6624 · last release 2023-11-12 · [PyPI](https://pypi.org/project/genanki/)

<details><summary>README extract</summary>

`genanki` allows you to programatically generate decks in Python 3 for Anki, a popular spaced-repetition flashcard
program. Please see below for concepts and usage.

*This library and its author(s) are not affiliated/associated with the main Anki project in any way.*

The basic unit in Anki is the `Note`, which contains a fact to memorize. ...

Example:
```python
my_note = genanki.Note(
  model=my_model,
  fields=['Capital of Argentina', 'Buenos Aires'])
```

Sections: genanki: A Library for Generating Anki Decks, Notes, Models, Generating a Deck/Package, Media Files, Note GUIDs, sort_field, YAML for Templates (and Fields), Using genanki inside an Anki addon, CLOZE_MODEL DeprecationWarning, FAQ, My field data is getting garbled, Publishing to PyPI

</details>

### gladiaio-sdk

Gladia SDK for Python

`pip install gladiaio-sdk` · installs (wheel) · licence: not stated · rank 6635 · last release 2026-10-23 · [PyPI](https://pypi.org/project/gladiaio-sdk/)

<details><summary>README extract</summary>

A Python SDK for the Gladia API.

You need Python 3.10+ for this package.

Example:
```python
from gladiaio_sdk import GladiaClient

gladia_client = GladiaClient(api_key="your-api-key")
```

Sections: Gladia Python SDK, Requirements, Usage, Sync client, Pre-recorded transcription, Async pre-recorded, Live transcription, Async live, Documentation

</details>

### google-cloud-mldiagnostics

diagnostic packages for profiling and ML experiment management

`pip install google-cloud-mldiagnostics` · installs (wheel) · licence: Apache-2.0 · rank 6681 · last release 2026-11-05 · [PyPI](https://pypi.org/project/google-cloud-mldiagnostics/) · [source](https://github.com/AI-Hypercomputer/google-cloud-mldiagnostics)

<details><summary>README extract</summary>

<!--
 Copyright 2025 Google LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at ...

Features:
Release Notes

Note: Google Cloud ML Diagnostics supports JAX, PyTorch, vLLM, and RL (Maxtext + Tunix + Pathways) on Google Cloud TPUs and GPUs today. ...

Example:
```python
import logging
import google.cloud.logging

# Instantiate a Cloud Logging client
logging_client = google.cloud.logging.Client()

# Attaches the Cloud Logging handler to the Python root logger
logging_client.setup_logging()

# Now, standard logging calls will go to Cloud Logging
...
```

...

</details>

### git-python

combination and simplification of some useful git commands

`pip install git-python` · does not install on CPython 3.14 · licence: not stated · rank 6794 · last release 2020-01-04 · [PyPI](https://pypi.org/project/git-python/)

<details><summary>README extract</summary>

git-python
^^^^^^^^^^

combination and simplification of some useful git commands

Usage

1. add and commit

 gp addc -m <message>

2. push as tag

 gp pushc addt -t <tag>

 gp pushc addr -t <tag> -n <name> -r <remote>

 gp pushc pusht -t <tag>

</details>

### googlenewsdecoder

A Python package to decode Google News URLs to their original sources.

`pip install googlenewsdecoder` · installs (wheel) · licence: MIT · rank 6868 · last release 2026-10-18 · [PyPI](https://pypi.org/project/googlenewsdecoder/) · [docs](https://github.com/SSujitX/google-news-url-decoder#readme) · [source](https://github.com/SSujitX/google-news-url-decoder)

<details><summary>README extract</summary>

=3.11">

Google News Decoder is a Python package that can decode Google News links or Google News URLs to their original URLs. It is a simple tool that saves you time and effort. If you find it useful, please support the package by hitting the star on GitHub. Your support helps keep the project going! ...

Example:
```python
from googlenewsdecoder import gnewsdecoder

def main():
    interval_time = 1  # optional; None means no wait
    timeout = 15.0
    # Optional. Examples:
    #   proxy = "
    #   proxy = "
    #   proxy = "socks5://user:pass@host:port"
    proxy = None

    source_url = "

    try:
        result = gnewsdecoder(
            source_url,
...
```

...

</details>

### gdsfactory

python library to generate GDS layouts

`pip install gdsfactory` · installs (wheel) · licence: not stated · rank 6915 · last release 2026-09-14 · [PyPI](https://pypi.org/project/gdsfactory/)

<details><summary>README extract</summary>

GDSFactory is a Python library for designing chips (Photonics, Analog, Quantum, MEMS), PCBs, and 3D-printable objects. We aim to make hardware design accessible, intuitive, and fun—empowering everyone to build the future.

As input you write python code, as an output GDSFactory creates CAD files (GDS, OASIS, STL, GERBER).

Features:
- Fast, extensible, and easy to use – designed for efficiency and flexibility.
- Free and open-source – no licensing fees, giving you the freedom to modify and extend it. ...

Example:
```python
import gdsfactory as gf

# Activate the built-in generic process design kit
gf.gpdk.PDK.activate()

# Create a new component
c = gf.Component()

# Add a rectangle
r = gf.components.rectangle(size=(10, 10), layer=(1, 0))
rect = c.add_ref(r)

# Add text elements
...

</details>

### gspread-asyncio

asyncio wrapper for burnash's Google Spreadsheet API library, gspread

`pip install gspread-asyncio` · installs (wheel) · licence: MIT License · rank 7027 · last release 2026-08-30 · [PyPI](https://pypi.org/project/gspread-asyncio/) · [docs](https://gspread-asyncio.readthedocs.io/en/latest/) · [source](https://github.com/dgilman/gspread_asyncio)

<details><summary>README extract</summary>

An asyncio wrapper for burnash's excellent Google Spreadsheet API library. `gspread_asyncio` isn't just a plain asyncio wrapper around the `gspread` API, it implements several useful and helpful features on top of those APIs. It's useful for long-running processes and one-off scripts.

Requires Python >= 3.11.

Features:
* Complete async wrapping of the `gspread` API. All `gspread` API calls are run off the main thread in a threadpool executor.
* Internal caching and reuse of `gspread` `Client`/`Spreadsheet`/`Worksheet` objects. ...

Example:
```python
import asyncio

import gspread_asyncio

# from google-auth package
from google.oauth2.service_account import Credentials

# First, set up a callback function that fetches our credentials off the disk.
...

</details>

### geoarrow-types

(no summary)

`pip install geoarrow-types` · installs (wheel) · licence: Apache-2.0 · rank 7173 · last release 2026-09-28 · [PyPI](https://pypi.org/project/geoarrow-types/) · [source](https://github.com/geoarrow/geoarrow-python)

### greenery

Greenery allows manipulation of regular expressions

`pip install greenery` · installs (wheel) · licence: MIT License · rank 7205 · last release 2026-10-24 · [PyPI](https://pypi.org/project/greenery/)

### graphlib-backport

Backport of the Python 3.9 graphlib module for Python 3.6+

`pip install graphlib-backport` · installs (wheel) · licence: Python Software Foundation License; Other/Proprietary License · rank 7255 · last release 2024-03-05 · [PyPI](https://pypi.org/project/graphlib-backport/) · [docs](https://github.com/mariushelf/graphlib_backport) · [source](https://github.com/mariushelf/graphlib_backport)

<details><summary>README extract</summary>

Backport of the Python 3.9
graphlib
module for older Python versions.

Github:

Sections: graphlib backport, Usage, Dev requirements, Running tests, Publishing a new version, Thanks

</details>

### goodvibes

A python program to compute corrections to thermochemical data from frequency calculations

`pip install goodvibes` · installs (wheel) · licence: MIT · rank 7292 · last release 2026-09-19 · [PyPI](https://pypi.org/project/goodvibes/)

<details><summary>README extract</summary>

===

GoodVibes computes quasi-harmonic thermochemical corrections from electronic structure calculations (Gaussian, ORCA, NWChem, QChem, xTB, ASE). It corrects the poor description of low-frequency vibrations by the rigid-rotor harmonic oscillator (RRHO) treatment using the approaches of Grimme and Truhlar.

Features:
- Grimme quasi-RRHO (mRRHO) and Truhlar quasi-harmonic entropy corrections
- Head-Gordon quasi-harmonic enthalpy correction
- Variable temperature and concentration thermochemistry ...

...

</details>

### gitingest

CLI tool to analyze and create text dumps of codebases for LLMs

`pip install gitingest` · installs (wheel) · licence: MIT License · rank 7359 · last release 2025-07-31 · [PyPI](https://pypi.org/project/gitingest/) · [source](https://github.com/coderamp-labs/gitingest)

<details><summary>README extract</summary>

Turn any Git repository into a prompt-friendly text ingest for LLMs.

You can also replace `hub` with `ingest` in any GitHub URL to access the corresponding digest.

gitingest.com · Chrome Extension · Firefox Add-on

Deutsch |
Español |
Français |
日本語 |
한국어 |
Português |
Русский | ...

Example:
```python
# Synchronous usage
from gitingest import ingest

summary, tree, content = ingest("path/to/directory")

# or from URL
summary, tree, content = ingest("

# or from a specific subdirectory
summary, tree, content = ingest("
```

Sections: Gitingest, 🚀 Features, 📚 Requirements, 🧩 Browser Extension Usage, 💡 Command line usage, 🐍 Python package usage, Jupyter notebook usage, 🐳 Self-host, Using Docker, Environment Variables, Using Docker Compose, Compose File Structure, Services, Usage Examples

</details>

### gliner2

GLiNER2: Unified Schema-Based Information Extraction and Text Classification

`pip install gliner2` · installs (wheel) · licence: Apache-2.0 · rank 7384 · last release 2026-10-09 · [PyPI](https://pypi.org/project/gliner2/) · [source](https://github.com/fastino-ai/GLiNER2)

<details><summary>README extract</summary>

> *Schema-driven information extraction and classification — entities, labels, records, relations, and span attributes in one local model.*

GLiNER2 is a schema-conditioned encoder family for Named Entity Recognition, Text Classification, Structured Data Extraction, Relation Extraction, and span attributes. ...

Example:
```python
from gliner2 import AutoExtractor
from gliner2.training.data import InputExample
from gliner2.training.trainer import ExtractorTrainer, TrainingConfig

# GLiNER2Trainer is a backward-compatible alias for ExtractorTrainer

# 1. Prepare training data
examples = [
    InputExample(
        text="John works at Google in California.",
...
```

...

</details>

### gethwp

Get text from HWP/HWPX file

`pip install gethwp` · installs (wheel) · licence: MIT · rank 7636 · last release 2024-02-11 · [PyPI](https://pypi.org/project/gethwp/)

<details><summary>README extract</summary>

HWP 파일 내 텍스트를 문자열 형태로 추출해주는 파이썬 라이브러리입니다. (HWPX 내 문자열 치환도 지원)

Example:
```python
import gethwp
hwp = gethwp.read_hwp('test.hwp')
print(hwp)
```

Sections: Description, Thanks to, 사용법, HWP 파일, HWPX 파일, HWPX 파일 내 텍스트 치환

</details>

### geoarrow-c

Python bindings to the geoarrow C and C++ implementation

`pip install geoarrow-c` · installs (wheel) · licence: Apache-2.0 · rank 7702 · last release 2026-09-29 · [PyPI](https://pypi.org/project/geoarrow-c/) · [source](https://github.com/geoarrow/geoarrow-c)

<details><summary>README extract</summary>

The geoarrow-c Python package provides bindings to the geoarrow-c implementation of the GeoArrow specification. Its primary purpose is to serve as a dependency to geoarrow-python where needed.

Example:
```python
import geoarrow.pyarrow as ga
from geoarrow.c import AggregateFunction, ScalarFunction

input_pyarrow = ga.array(["POINT (0 1)"])
format_wkt = ScalarFunction("format_wkt", precision=3)
formatted = format_wkt(input_pyarrow)

box_agg = AggregateFunction("box_agg")
result = box_agg(input_pyarrow)
```

Sections: geoarrow-c for Python, Example, Type specification integration, Building

</details>

### geoarrow-pyarrow

(no summary)

`pip install geoarrow-pyarrow` · installs (wheel) · licence: Apache-2.0 · rank 7939 · last release 2026-09-28 · [PyPI](https://pypi.org/project/geoarrow-pyarrow/) · [source](https://github.com/geoarrow/geoarrow-python)

### globmatch

Matching paths against globs

`pip install globmatch` · installs (wheel) · licence: BSD License · rank 8356 · last release 2021-01-07 · [PyPI](https://pypi.org/project/globmatch/)

<details><summary>README extract</summary>

Installation |
Usage |
Testing |
License

`globmatch` provides functions for matching a path against one ore more glob patterns in Python.
This differs from the `glob` module of the standard library, which matches a glob against the
file-tree on your system. `globmatch` does not interact with the filesystem at all, but relies on
generic matching. ...

Example:
```python
from globmatch import glob_match

# Some paths that match (returns True):
glob_match('.git/gitconfig/', ['.git'])
glob_match('foo/config', ['**/config'])
glob_match('foo/config/bar', ['**/config'])
glob_match('.git/gitconfig/', ['.git', '**/config'])
glob_match('foo/config/bar', ['.git', '**/config'])
glob_match('/.git/gitconfig/', ['**/.git'])

...
```

Sections: globmatch - Matching paths against globs, Usage, Resources

</details>

### grpc-gateway-protoc-gen-openapiv2

Provides the missing pieces for gRPC Gateway.

`pip install grpc-gateway-protoc-gen-openapiv2` · installs (wheel) · licence: BSD License · rank 8519 · last release 2021-05-09 · [PyPI](https://pypi.org/project/grpc-gateway-protoc-gen-openapiv2/)

### gecosistema_lite

A simple python package

`pip install gecosistema_lite` · installs from source (sdist only) · licence: MIT · rank 8543 · last release 2021-03-03 · [PyPI](https://pypi.org/project/gecosistema_lite/)

### gh-md-to-html

Feature-rich Github-flavored Markdown to html python and command line interface.

`pip install gh-md-to-html` · installs (wheel) · licence: LICENSE.txt · rank 8550 · last release 2024-06-17 · [PyPI](https://pypi.org/project/gh-md-to-html/)

<details><summary>README extract</summary>

A user-friendly python-module and command-line frontend to convert markdown to html. It uses
GitHubs online Markdown-to-html-API by default (which requires
internet connection), but comes with an option for offline conversion (which closely imitates GitHubs behavior), and any other python- or commandline tool can be plugged into it as well. ...

Example:
```python
import gh_md_to_html
```

Sections: Usage, Documentation, More detail on image caching paths, Feedback, Further reading, Attribution

</details>

### google-cloud-agentplatform

Google Cloud Agent Platform Client Library

`pip install google-cloud-agentplatform` · installs (wheel) · licence: Apache Software License · rank 8558 · last release 2026-10-28 · [PyPI](https://pypi.org/project/google-cloud-agentplatform/)

<details><summary>README extract</summary>

Gemini Enterprise Agent Platform Client Library.

</details>

### grpcio-channelz

Channel Level Live Debug Information Service for gRPC

`pip install grpcio-channelz` · installs (wheel) · licence: Apache-2.0 · rank 8643 · last release 2026-10-30 · [PyPI](https://pypi.org/project/grpcio-channelz/) · [docs](https://grpc.github.io/grpc/python/grpc_channelz.html)

<details><summary>README extract</summary>

Channelz is a live debug tool in gRPC Python.

Depends on the `grpcio` package, available from PyPI via `pip install grpcio`.

Sections: gRPC Python Channelz package, Dependencies

</details>

### gpsoauth

A python client library for Google Play Services OAuth.

`pip install gpsoauth` · installs (wheel) · licence: MIT License · rank 8682 · last release 2026-11-05 · [PyPI](https://pypi.org/project/gpsoauth/) · [source](https://github.com/simon-weber/gpsoauth)

<details><summary>README extract</summary>

Python client library for Google Play Services OAuth.

`gpsoauth` allows python code to use the "master token" flow that KB Sriram described at

This can be useful when writing code that poses as a Google app, like
gmusicapi does here.

Many thanks to Dima Kovalenko for reverse engineering the EncryptedPasswd signature in ...

Example:
```python
import gpsoauth

email = 'example@gmail.com'
password = 'my-password'
android_id = '0123456789abcdef'

master_response = gpsoauth.perform_master_login(email, password, android_id)
master_token = master_response['Token']

auth_response = gpsoauth.perform_oauth(
    email, master_token, android_id,
    service='sj', app='com.google.android.music',
...
```

Sections: gpsoauth, Alternative flow, Using another HTTP client, Ports

</details>

### geoip2-tools

Automatic updates and administration of MaxMind GeoIP2 databases.

`pip install geoip2-tools` · installs (wheel) · licence: MIT License · rank 9026 · last release 2020-10-29 · [PyPI](https://pypi.org/project/geoip2-tools/)

<details><summary>README extract</summary>

Automatic updates and administration of MaxMind GeoIP2 databases.

To install geoip2-tools, run this command in your terminal:

This is the preferred method to install geoip2-tools, as it will always install the most recent stable release.

Example:
```python
from geoip2_tools.manager import Geoip2DataBaseManager

geoip2_manager = Geoip2DataBaseManager('<license key>')

print(geoip2_manager['country'].reader.country('1.1.1.1').country.name)  # Australia
```

Sections: geoip2-tools, Usage

</details>

### gtsam

Georgia Tech Smoothing And Mapping library

`pip install gtsam` · installs (wheel) · licence: BSD License · rank 9086 · last release 2026-09-19 · [PyPI](https://pypi.org/project/gtsam/)

<details><summary>README extract</summary>

Development branch

The `develop` branch contains changes intended for the next GTSAM release and
may include API changes. For production use, choose the latest stable version
from the GTSAM releases. Current
development builds require C++17; Boost support is optional and controlled by
CMake options. ...

Sections: GTSAM: Georgia Tech Smoothing and Mapping Library, What is GTSAM?, Documentation, Quickstart, GTSAM 4 Compatibility, Wrappers, The Preintegrated IMU Factor, Additional Information

</details>

### globus-sdk

Globus SDK for Python

`pip install globus-sdk` · installs (wheel) · licence: Apache Software License · rank 9126 · last release 2026-10-22 · [PyPI](https://pypi.org/project/globus-sdk/)

<details><summary>README extract</summary>

This SDK provides a convenient Pythonic interface to
Globus APIs.

Example:
```python
from globus_sdk import LocalGlobusConnectPersonal

# None if Globus Connect Personal is not installed
endpoint_id = LocalGlobusConnectPersonal().endpoint_id
```

Sections: Globus SDK for Python, Basic Usage, Links

</details>

### gem-llm

A Gym for Generalist LLMs.

`pip install gem-llm` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 9127 · last release 2025-10-05 · [PyPI](https://pypi.org/project/gem-llm/) · [docs](https://axon-rl.github.io/gem/) · [source](https://github.com/axon-rl/gem)

<details><summary>README extract</summary>

Features:
We’re entering the era of experience, where large language models (LLMs) learn not just from static datasets, but from *interactive experience* gathered in complex, expressive environments. ...

Example:
```python
import gem

# List all supported environments
gem.print_envs()

# Initialize the environment
env = gem.make("game:GuessTheNumber-v0")

# Reset the environment to generate the first observation
observation, info = env.reset()

# Start the agent-environment loop
while True:
    action = env.sample_random_action() # insert policy here, e.g.,
...
```

Sections: 🌍 GEM: A Gym for Agentic LLMs, Overview, Links, Interface, Features

</details>

### graphql-utils

Useful function when interacting with GraphQL APIs

`pip install graphql-utils` · installs (wheel) · licence: Apache Software License · rank 9149 · last release 2021-12-06 · [PyPI](https://pypi.org/project/graphql-utils/)

<details><summary>README extract</summary>

The `graphql-utils` Python package is a collection of utilities function for
interacting with GraphQL libraries. It is meant to be library agnostic so it
should work with whatever library or protocol you want.

Example:
```python
import requests

from graphql_utils import multi

def requests_api(query):
    return requests.post(" json=query)

userlist = (
    {"login": "jd"},
    {"login": "sileht"},
    {"login": "foo"},
    {"login": "bar"},
)

result_iterator = multi.multi_query("""
    user(login: "{login}") {{
      pets(first: 100{after}) {{
        nodes {{
...
```

Sections: GraphQL Utils for Python, Usage, Multi-requests

</details>

### ghidra-bridge

RPC bridge from Python to Ghidra Jython

`pip install ghidra-bridge` · installs (wheel) · licence: MIT License · rank 9204 · last release 2023-01-30 · [PyPI](https://pypi.org/project/ghidra-bridge/)

<details><summary>README extract</summary>

Ghidra is great, and I like scripting as much of my RE as possible. But Ghidra's Python scripting is based on Jython, which isn't in a great state these days. Installing new packages is a hassle, if they can even run in a Jython environment, and it's only going to get worse as Python 2 slowly gets turned off. ...

Example:
```python
$ghidraRoot/support/analyzeHeadless <path to directory to store project> <name for project> -import <path to file to import>  -scriptPath <install directory for the server scripts> -postscript ghidra_bridge_server.py
```

...

</details>

### gw-dsl-parser

gw_dsl_parser: Convert your graphic-walker workflow to sql

`pip install gw-dsl-parser` · installs (wheel) · licence: Apache Software License · rank 9223 · last release 2024-07-31 · [PyPI](https://pypi.org/project/gw-dsl-parser/) · [source](https://github.com/Kanaries/gw-dsl-parser-py)

<details><summary>README extract</summary>

Example:
```python
from gw_dsl_parser import get_sql_from_payload

payload = {"workflow": [{"type": "view", "query": [{"op": "aggregate", "groupBy": [], "measures": [{"field": "*", "agg": "count", "asFieldKey": "count"}]}]}]}
table_name = "test_table"
sql = get_sql_from_payload(table_name, payload)
```

Sections: gw-dsl-parser-py, Example

</details>

### GvGen

Generate clear Graphviz Graphs which can be edited manually later on.

`pip install GvGen` · installs (wheel) · licence: MIT License · rank 9285 · last release 2020-02-12 · [PyPI](https://pypi.org/project/GvGen/)

### gigachat

GigaChat. Python-library for GigaChat API

`pip install gigachat` · installs (wheel) · licence: MIT · rank 9387 · last release 2026-10-30 · [PyPI](https://pypi.org/project/gigachat/) · [source](https://github.com/ai-forever/gigachat)

<details><summary>README extract</summary>

Python SDK for the GigaChat REST API — a large language model.

This library is part of GigaChain and powers langchain-gigachat, the official LangChain integration for GigaChat.

Features:
- ✅ Chat completions — synchronous and asynchronous
- ✅ Streaming responses — real-time token generation
- ✅ Embeddings — text vectorization
- ✅ Function calling — tool use for building agents
- ✅ Vision — image understanding (multimodal) ...

Example:
```python
from gigachat import GigaChat

with GigaChat(credentials="<your_authorization_key>", model="GigaChat-2") as client:
    response = client.chat.create("Hello, GigaChat!")
    print(response.messages[0].content[0].text)
```

...

</details>

### garmin-fit-sdk

Garmin FIT Python SDK

`pip install garmin-fit-sdk` · installs (wheel) · licence: LicenseRef-FIT-Protocol-License-Agreement · rank 9521 · last release 2026-11-03 · [PyPI](https://pypi.org/project/garmin-fit-sdk/) · [docs](https://developer.garmin.com/fit/overview/) · [source](https://github.com/garmin/fit-python-sdk)

<details><summary>README extract</summary>

The FIT SDK documentation is available at

Example:
```python
from garmin_fit_sdk import Decoder, Stream

stream = Stream.from_file("Activity.fit")
decoder = Decoder(stream)
messages, errors = decoder.read()

print(errors)
print(messages)
```

Sections: Garmin - FIT Python SDK, FIT SDK Documentation, FIT Python SDK Requirements, Usage, Decoder, Constructor, is_fit Method, check_integrity Method, Read Method, mesg_listener, apply_scale_and_offset: true | false, enable_crc_check: true | false, expand_sub_fields: true | false, expand_components: true | false

</details>

### gohighlevel-api-client

GoHighLevel Python SDK - Official API client for GoHighLevel platform

`pip install gohighlevel-api-client` · installs (wheel) · licence: MIT · rank 9558 · last release 2026-06-25 · [PyPI](https://pypi.org/project/gohighlevel-api-client/) · [docs](https://marketplace.gohighlevel.com/docs/) · [source](https://github.com/GoHighLevel/highlevel-api-python)

<details><summary>README extract</summary>

Official Python SDK for the GoHighLevel API. This library provides a convenient way to interact with GoHighLevel's APIs from applications written in Python.

Features:
- Automatic Token Management: Handles `INSTALL` and `UNINSTALL` webhooks automatically
- Token Storage: Generates and stores access tokens on `INSTALL`, removes them on `UNINSTALL` ...

Example:
```python
from highlevel import HighLevel

# Initialize with OAuth credentials
client = HighLevel(
    client_id="your_client_id",
    client_secret="your_client_secret"
)
```

Sections: GoHighLevel Python SDK, Quick Start, Basic Usage, OAuth Flow Example, Storage, MongoDB Storage, Webhook Integration, Features, Webhook Handler Setup, Webhook Signature Verification, Documentation

</details>

### googleauthentication

A meta package to be connected to Google services

`pip install googleauthentication` · installs from source (sdist only) · licence: MIT License · rank 9582 · last release 2024-10-09 · [PyPI](https://pypi.org/project/googleauthentication/)

### grpcio-csds

xDS configuration dump library

`pip install grpcio-csds` · installs (wheel) · licence: Apache-2.0 · rank 9769 · last release 2026-10-30 · [PyPI](https://pypi.org/project/grpcio-csds/) · [docs](https://grpc.github.io/grpc/python/grpc_csds.html)

### grpcio-admin

a collection of admin services

`pip install grpcio-admin` · installs (wheel) · licence: Apache-2.0 · rank 9807 · last release 2026-10-30 · [PyPI](https://pypi.org/project/grpcio-admin/) · [docs](https://grpc.github.io/grpc/python/grpc_admin.html)

<details><summary>README extract</summary>

Debugging gRPC library can be a complex task. There are many configurations and
internal states, which will affect the behavior of the library. This Python
package will be the collection of admin services that are exposing debug
information. Currently, it includes: ...

</details>

### gemma

Gemma open-weight LLM library from Google DeepMind.

`pip install gemma` · installs (wheel) · licence: Apache Software License · rank 9858 · last release 2026-05-20 · [PyPI](https://pypi.org/project/gemma/) · [source](https://github.com/google-deepmind/gemma)

<details><summary>README extract</summary>

Gemma is a family of open-weights Large Language
Model (LLM) by Google DeepMind, based on Gemini
research and technology.

This repository contains the implementation of the
`gemma` PyPI package. A
JAX library to use and fine-tune Gemma.

For examples and use cases, see our
documentation. Please
report issues and feedback in
our GitHub.

Example:
```python
from gemma import gm

# Model and parameters (Gemma 4)
model = gm.nn.Gemma4_E4B()
params = gm.ckpts.load_params(gm.ckpts.CheckpointPath.GEMMA4_E4B_IT)

# Example of multi-turn conversation
sampler = gm.text.ChatSampler(
    model=model,
    params=params,
    multi_turn=True,
)

prompt = """Which of the 2 images do you prefer ?

Image 1: <|image|>
...
```

...

</details>

### gdrive-fsspec

File system on GDrive

`pip install gdrive-fsspec` · installs (wheel) · licence: BSD License · rank 9878 · last release 2026-06-11 · [PyPI](https://pypi.org/project/gdrive-fsspec/) · [source](http://github.com/fsspec/gdrive-fsspec)

<details><summary>README extract</summary>

This is an implementation of the fsspec interface for Google Drive.

This software is in beta stage and should not be relied upon in production settings.

Example:
```python
from gdrive_fsspec import GoogleDriveFileSystem
fs = GoogleDriveFileSystem(creds=service_account_credentials,
                           token="service_account")
```

Sections: Google Drive fsspec implementation, Usage, Authentication, 1. Service account credentials, 2. OAuth with user credentials, 3. Anonymous (read-only) access, Running tests, Style, Other implementations

</details>

### gfpgan

GFPGAN aims at developing Practical Algorithms for Real-world Face Restoration

`pip install gfpgan` · installs (wheel) · licence: Apache Software License · rank 9908 · last release 2022-09-16 · [PyPI](https://pypi.org/project/gfpgan/)

<details><summary>README extract</summary>

1. :boom: Updated online demo: . Here is the backup.
1. :boom: Updated online demo:
1. Colab Demo for GFPGAN ; (Another Colab Demo for the original paper model)

> :rocket: Thanks for your interest in our work. You may also want to check our new updates on the *tiny models* for *anime images and videos* in Real-ESRGAN :blush: ...

Sections: English | 简体中文, zap: Quick Inference, european_castle: Model Zoo, computer: Training, BibTeX, e-mail: Contact

</details>

### geonames

Geonames data parser into Shapefile/KML

`pip install geonames` · installs (wheel) · licence: UNKNOWN · rank 9948 · last release 2015-07-29 · [PyPI](https://pypi.org/project/geonames/)

<details><summary>README extract</summary>

The Geonames library parses Geonames.org datasets into clean & simple OGR shapefile format.

Sections: Geonames, How to Use, Documentation

</details>

### googleapis-common-protos-stubs

Type stubs for googleapis-common-protos

`pip install googleapis-common-protos-stubs` · installs (wheel) · licence: Apache Software License · rank 10050 · last release 2024-01-28 · [PyPI](https://pypi.org/project/googleapis-common-protos-stubs/) · [source](https://github.com/henribru/googleapis-common-protos-stubs)

<details><summary>README extract</summary>

This package provides type stubs for the googleapis-common-protos package.

This is in no way affiliated with Google.

The stubs were created automatically by mypy-protobuf.

Note that if you're using Mypy you need to use the `--namespace-packages` option as `google` and some of its subpackages are namespace packages.

</details>

### gmssl

Pure-Python SM2/SM3/SM4 implementation

`pip install gmssl` · installs (wheel) · licence: BSD · rank 10077 · last release 2023-02-23 · [PyPI](https://pypi.org/project/gmssl/)

<details><summary>README extract</summary>

GmSSL是一个开源的加密包的python实现，支持SM2/SM3/SM4等国密(国家商用密码)算法、项目采用对商业应用友好的类BSD开源许可证，开源且可以用于闭源的商业应用。

RSA算法的危机在于其存在亚指数算法，对ECC算法而言一般没有亚指数攻击算法
SM2椭圆曲线公钥密码算法：我国自主知识产权的商用密码算法，是ECC（Elliptic Curve Cryptosystem）算法的一种，基于椭圆曲线离散对数问题，计算复杂度是指数级，求解难度较大，同等安全程度要求下，椭圆曲线密码较其他公钥算法所需密钥长度小很多。

gmssl是包含国密SM2算法的Python实现， 提供了 `encrypt`、 `decrypt`等函数用于加密解密， 用法如下：

Example:
```python
import base64
import binascii
from gmssl import sm2, func
# 16进制的公钥和私钥
private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
sm2_crypt = sm2.CryptSM2(
...
```

...

</details>

### getname

Get popular cat/dog/superhero/supervillain names

`pip install getname` · installs from source (sdist only) · licence: MIT License · rank 10173 · last release 2015-08-23 · [PyPI](https://pypi.org/project/getname/)

<details><summary>README extract</summary>

Get cat/dog/superhero/supervillain names.

I just combine @sindresorhus's
four staffs into this one.

- cat-names
- dog-names
- superheroes
- supervillains

Example:
```python
>>> from getname import random_name
>>> random_name('cat')
u'Angel'
>>> random_name('dog', gender='female')
u'Maggie'
>>> random_name('superhero', showall=True)
[u'3-D Man', u'A-Bomb', u'A.I.M.', ...]
```

Sections: GetName, Usage, API, CLI, Tests

</details>

### gwcs

Generalized World Coordinate System

`pip install gwcs` · installs (wheel) · licence: not stated · rank 10217 · last release 2026-02-12 · [PyPI](https://pypi.org/project/gwcs/) · [docs](https://gwcs.readthedocs.io/en/stable/) · [source](https://github.com/spacetelescope/jwst)

<details><summary>README extract</summary>

Generalized World Coordinate System (GWCS) is an Astropy affiliated package providing tools for managing the World Coordinate System of astronomical data.

GWCS takes a general approach to the problem of expressing transformations between pixel and world coordinates. ...

Sections: GWCS - Generalized World Coordinate System, Citing GWCS

</details>

### gritql

Python bindings for GritQL

`pip install gritql` · installs (wheel) · licence: MIT License · rank 10294 · last release 2025-06-24 · [PyPI](https://pypi.org/project/gritql/)

<details><summary>README extract</summary>

GritQL is a declarative query language for searching and modifying source code.

- 📖 Start simply without learning AST details: any code snippet is a valid GritQL query
- ⚡️ Use Rust and query optimization to scale up to 10M+ line repositories
- 📦 Use Grit's built-in module system to reuse 200+ standard patterns or share your own ...

</details>

### google-agents-cli

Agents CLI — Agent Development Lifecycle toolchain for ADK

`pip install google-agents-cli` · installs (wheel) · licence: Apache-2.0 · rank 10376 · last release 2026-11-04 · [PyPI](https://pypi.org/project/google-agents-cli/) · [docs](https://google.github.io/agents-cli/)

<details><summary>README extract</summary>

The CLI and skills for building agents on Gemini platform.

 Get Started |
 Skills |
 Commands |
 PyPI |
 Issues |
 Docs |
 Release Notes |
 Star us

Turn your favorite coding assistant into an expert at building and deploying agents on Google Cloud. ...

Sections: agents-cli, Get Started, 2. Open your coding agent, 3. Build your first agent, Agent Skills, CLI Commands, How it works, Architecture, FAQ, Feedback, Telemetry, Terms of Service

</details>

### graphene-django-optimizer

Optimize database access inside graphene queries.

`pip install graphene-django-optimizer` · installs (wheel) · licence: MIT License · rank 10524 · last release 2023-08-05 · [PyPI](https://pypi.org/project/graphene-django-optimizer/)

<details><summary>README extract</summary>

Optimize queries executed by graphene-django automatically, using `select_related`, `prefetch_related` and `only` methods of Django QuerySet.

Example:
```python
# cookbook/ingredients/schema.py
import graphene

from graphene_django.types import DjangoObjectType
import graphene_django_optimizer as gql_optimizer

from cookbook.ingredients.models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class IngredientType(DjangoObjectType):
    class Meta:
...
```

Sections: graphene-django-optimizer, Usage, Advanced usage, Optimize with non model fields

</details>

### graphyte

Python 3 compatible library to send data to a Graphite metrics server (Carbon)

`pip install graphyte` · installs from source (sdist only) · licence: MIT License · rank 10537 · last release 2022-01-23 · [PyPI](https://pypi.org/project/graphyte/)

<details><summary>README extract</summary>

graphyte is a small Python library that sends data to a Graphite metrics
server (Carbon). We wrote it because the existing graphitesend library
didn’t support Python 3, and it also required gevent for asyncronous use.
graphyte is tested on Python 3.5+ as well as Python 2.7, and uses the
standard library’s `threading` module for asynchronous use. ...

Example:
```python
import graphyte
graphyte.init('graphite.example.com', prefix='system.sync')
graphyte.send('foo.bar', 42)
```

</details>

### ghstack

Stack diff support for GitHub

`pip install ghstack` · installs (wheel) · licence: MIT · rank 10562 · last release 2026-09-11 · [PyPI](https://pypi.org/project/ghstack/) · [source](https://github.com/ezyang/ghstack)

<details><summary>README extract</summary>

Conveniently submit stacks of diffs to GitHub as separate pull requests.

ghstack is tested with
several different Python versions.
It requires at least Python 3.9.1.

Go to github.com `Settings→Developer Settings→Personal Access Tokens` and
generate a token with `public_repo` access only.
Create a `~/.ghstackrc` as shown below: ...

Sections: ghstack, How to setup, How to use, Structure of submitted pull requests, Design constraints, Ripley Cupboard

</details>

### guardrails-hub-types

Guardrails Hub Types.

`pip install guardrails-hub-types` · installs (wheel) · licence: not stated · rank 10677 · last release 2024-08-12 · [PyPI](https://pypi.org/project/guardrails-hub-types/)

<details><summary>README extract</summary>

Internal data structures for the Guardrails Hub.

Sections: Guardrails Hub Types, Documentation For Models

</details>

### git-credentials

Simple library to interact with Git Credentials

`pip install git-credentials` · installs (wheel) · licence: MIT License · rank 10701 · last release 2022-01-31 · [PyPI](https://pypi.org/project/git-credentials/)

<details><summary>README extract</summary>

Simple small library to provide an interface around the `git credential` Git command.
No dependencies but `git` must in the PATH.

Example:
```python
from git_credentials import GitCredentials, GitCredentialDescription, GitCredentialError, GitCredentialNotStoredError

def test_creds(user, pw):
    ...

def ask_for_creds():
    ...

cred = GitCredentials("/path/to/repo")

try:
    response = cred.fill(GitCredentialDescription(
        protocol="https",
        host="example.com",
...
```

Sections: Git Credentials, Example

</details>

### gron

Python library to grep JSON.

`pip install gron` · installs (wheel) · licence: MIT License · rank 10737 · last release 2024-08-24 · [PyPI](https://pypi.org/project/gron/) · [docs](https://gron.readthedocs.io/) · [source](https://github.com/venthur/python-gron)

<details><summary>README extract</summary>

Make JSON grep-able, a Python implementation of
gron.

Sections: python-gron, Documentation, Usage

</details>

### glean-api-client

Python Client SDK Generated by Speakeasy.

`pip install glean-api-client` · installs (wheel) · licence: not stated · rank 10773 · last release 2026-10-22 · [PyPI](https://pypi.org/project/glean-api-client/) · [source](https://github.com/gleanwork/api-client-python.git)

<details><summary>README extract</summary>

The Glean Python SDK provides convenient access to the Glean REST API from any Python 3.8+ application. It includes type hints for all request parameters and response fields, and supports both synchronous and asynchronous usage via httpx.
<!-- No Summary [summary] --> ...

Example:
```python
# !/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
# "glean-api-client",
# ]
# ///

from glean.api_client import Glean

sdk = Glean(
  # SDK arguments
)

# Rest of script here...
```

Sections: Glean Python API Client, Unified SDK Architecture, PIP, Poetry, Shell and script usage with `uv`, PyCharm, SDK Example Usage, Example 1, Example 2, Authentication, Authentication Methods, Client Namespace, Indexing Namespace, Available Resources and Operations

</details>

### giteapy

Python SDK for Gitea - A painless, self-hosted Git service

`pip install giteapy` · installs from source (sdist only) · licence: not stated · rank 10774 · last release 2020-01-14 · [PyPI](https://pypi.org/project/giteapy/)

<details><summary>README extract</summary>

This documentation describes the Gitea API.

This Python package is automatically generated by the Swagger Codegen project:

- API version: 1.1.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

Python 2.7 and 3.4+

Example:
```python
from future import print_function
import time
import giteapy
from giteapy.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = giteapy.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
...
```

...

</details>

### gs-quant

Goldman Sachs Quant

`pip install gs-quant` · installs (wheel) · licence: Apache Software License · rank 10786 · last release 2026-11-06 · [PyPI](https://pypi.org/project/gs-quant/)

<details><summary>README extract</summary>

GS Quant is a Python toolkit for quantitative finance, created on top of one of the world’s most powerful risk transfer platforms. Designed to accelerate development of quantitative trading strategies and risk management solutions, crafted over 25 years of experience navigating global markets. ...

Sections: GS Quant, Requirements, Examples, Help

</details>

### google-gax

Google API Extensions

`pip install google-gax` · installs (wheel) · licence: BSD License · rank 10813 · last release 2018-02-28 · [PyPI](https://pypi.org/project/google-gax/)

<details><summary>README extract</summary>

This project has been deprecated and will no longer be developed. It has
been wholly replaced by google-api-core.

Google API Extensions for Python (gax-python) is a set of modules which aids the
development of APIs for clients and servers based on gRPC and Google API
conventions. ...

Sections: DEPRECATED, Google API Extensions for Python, Python Versions, Versioning, Details

</details>

### geoarrow-pandas

(no summary)

`pip install geoarrow-pandas` · installs (wheel) · licence: Apache-2.0 · rank 10830 · last release 2026-09-28 · [PyPI](https://pypi.org/project/geoarrow-pandas/) · [source](https://github.com/geoarrow/geoarrow-python)

### genesis-world

A universal and generative physics engine

`pip install genesis-world` · does not install on CPython 3.14 · licence: not stated · rank 10930 · last release 2026-10-22 · [PyPI](https://pypi.org/project/genesis-world/)

<details><summary>README extract</summary>

Genesis World is a simulation platform for physical AI developments. It combines a unified multi-physics engine, a photo-realistic renderer (Nyx), and a cross-platform compiler (Quadrants) behind a Pythonic simulation interface. ...

Sections: Genesis World, What is Genesis World?, Documentation, Catalogue, Physics, Rendering, Simulation Interface, Using pip, Optional extras, Using uv

</details>

### gptcache

GPTCache, a powerful caching library that can be used to speed up and lower the cost of chat applications that rely on the LLM service. GPTCache works as a memcache for AIGC applications, similar to how Redis works for traditional applications.

`pip install gptcache` · installs (wheel) · licence: https://opensource.org/license/mit/ · rank 10949 · last release 2024-08-01 · [PyPI](https://pypi.org/project/gptcache/)

<details><summary>README extract</summary>

Slash Your LLM API Costs by 10x 💰, Boost Speed by 100x ⚡

🎉 GPTCache has been fully integrated with 🦜️🔗LangChain ! Here are detailed usage instructions.

🐳 The GPTCache server docker image has been released, which means that any language will be able to use GPTCache! ...

Example:
```python
import os
import time

import openai

def response_text(openai_resp):
    return openai_resp'choices''message'

question = 'what‘s chatgpt'

# OpenAI API original usage
openai.api_key = os.getenv("OPENAI_API_KEY")
start_time = time.time()
response = openai.ChatCompletion.create(
  model='gpt-3.5-turbo',
  messages=[
    {
        'role': 'user',
...
```

...

</details>

### graphql_client

A GraphQL Client

`pip install graphql_client` · installs from source (sdist only) · licence: Apache-2.0 · rank 11075 · last release 2018-07-30 · [PyPI](https://pypi.org/project/graphql_client/)

<details><summary>README extract</summary>

Example:
```python
client = GraphQLClient('

result = client.query('''
query ($id: String!) {
    hn2 {
        nodeFromHnId(id: $id, isUserId: true) {
            id
        }
    }
}
''', {'id': 'clayallsopp'})
```

Sections: GraphQL Client, Getting Started, Tests

</details>

### guardrails-ai

Adding guardrails to large language models.

`pip install guardrails-ai` · does not install on CPython 3.14 · licence: Apache Software License · rank 11109 · last release 2026-08-14 · [PyPI](https://pypi.org/project/guardrails-ai/)

<details><summary>README extract</summary>

- [Feb 12, 2025] We just launched Guardrails Index -- the first of its kind benchmark comparing the performance and latency of 24 guardrails across 6 most common categories! Check out the index at index.guardrailsai.com

Guardrails is a Python framework that helps build reliable AI applications by performing two key functions:
1. ...

Example:
```python
from guardrails import Guard, OnFailAction
from guardrails_ai.regex_match import RegexMatch

guard = Guard().use(
    RegexMatch, regex="\(?\d{3}\)?-? *\d{3}-? *-?\d{4}", on_fail=OnFailAction.EXCEPTION
)

guard.validate("123-456-7890")  # Guardrail passes

try:
    guard.validate("1234-789-0000")  # Guardrail fails
except Exception as e:
...
```

...

</details>

### getdaft

getdaft is now daft

`pip install getdaft` · installs (wheel) · licence: not stated · rank 11189 · last release 2025-08-01 · [PyPI](https://pypi.org/project/getdaft/)

<details><summary>README extract</summary>

This package has been renamed. Use `pip install daft` instead.

New package:

</details>

### gcp-storage-emulator

A stub emulator for the Google Cloud Storage API

`pip install gcp-storage-emulator` · installs (wheel) · licence: BSD License · rank 11236 · last release 2026-07-19 · [PyPI](https://pypi.org/project/gcp-storage-emulator/)

<details><summary>README extract</summary>

Google doesn't (yet) ship an emulator for the Cloud Storage API like they do for
Cloud Datastore.

This is a stub emulator so you can run your tests and do local development without
having to connect to the production Storage APIs.

THIS IS A WORK IN PROGRESS AND ONLY SUPPORTS A LIMITED SUBSET OF THE API

Example:
```python
import os

from google.cloud import storage
from gcp_storage_emulator.server import create_server

HOST = "localhost"
PORT = 9023
BUCKET = "test-bucket"

# default_bucket parameter creates the bucket automatically
server = create_server(HOST, PORT, in_memory=True, default_bucket=BUCKET)
server.start()

os.environ["STORAGE_EMULATOR_HOST"] = f"
...
```

...

</details>

### guardpycfn

Python bindings for AWS CloudFormation Guard via pyo3

`pip install guardpycfn` · installs (wheel) · licence: MIT-0 · rank 11239 · last release 2025-10-15 · [PyPI](https://pypi.org/project/guardpycfn/)

### graphitesend

A simple interface for sending metrics to Graphite

`pip install graphitesend` · installs from source (sdist only) · licence: not stated · rank 11274 · last release 2017-03-25 · [PyPI](https://pypi.org/project/graphitesend/)

### graphqlclient

Simple GraphQL client for Python 2.7+

`pip install graphqlclient` · installs from source (sdist only) · licence: MIT · rank 11329 · last release 2018-07-12 · [PyPI](https://pypi.org/project/graphqlclient/)

<details><summary>README extract</summary>

Simple GraphQL client for Python 2.7+

Example:
```python
from graphqlclient import GraphQLClient

client = GraphQLClient('

result = client.execute('''
{
  allFilms {
    films {
      title
    }
  }
}
''')

print(result)
```

Sections: python-graphql-client, Usage

</details>

### geobuf

Geobuf is a compact binary geospatial format for lossless compression of GeoJSON.

`pip install geobuf` · installs (wheel) · licence: MIT · rank 11383 · last release 2026-01-20 · [PyPI](https://pypi.org/project/geobuf/)

<details><summary>README extract</summary>

Geobuf is a compact binary geospatial format for _lossless_ compression of GeoJSON.

Note well: this project has been transferred by Mapbox to the new pygeobuf organization.

Advantages over using GeoJSON directly (in this revised version):

- Very compact: typically makes GeoJSON 6-8 times smaller. ...

Example:
```python
import geobuf

pbf = geobuf.encode(my_json) # GeoJSON -> Geobuf string
my_json = geobuf.decode(pbf) # Geobuf string -> GeoJSON
```

Sections: Geobuf, pygeobuf, Sample compression sizes, Usage, Tests, Generating from geobuf.proto

</details>

### gpuhunt

A catalog of GPU pricing for different cloud providers

`pip install gpuhunt` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 11386 · last release 2026-10-29 · [PyPI](https://pypi.org/project/gpuhunt/) · [source](https://github.com/dstackai/gpuhunt)

<details><summary>README extract</summary>

Easy access to GPU pricing data for major cloud providers: AWS, Azure, GCP, etc.
The catalog includes details about prices, locations, CPUs, RAM, GPUs, and spots (interruptible instances).

Example:
```python
import gpuhunt

items = gpuhunt.query(
    min_memory=16,
    min_cpu=8,
    min_gpu_count=1,
    max_price=1.0,
)

print(*items, sep="\n")
```

Sections: Usage, Advanced usage, See also

</details>

### global-land-mask

Check whether a lat/lon point in on land or on sea

`pip install global-land-mask` · installs (wheel) · licence: MIT License · rank 11621 · last release 2020-10-05 · [PyPI](https://pypi.org/project/global-land-mask/)

<details><summary>README extract</summary>

Check whether a lat/lon point is on land for any point on earth.

Example:
```python
from global_land_mask import globe
import numpy as np

# Check if a point is on land:
lat = 40
lon = -120
is_on_land = globe.is_land(lat, lon)

print('lat={}, lon={} is on land: {}'.format(lat,lon,is_on_land))
# lat=40, lon=-120 is on land: True

# Check if several points are in the ocean
lat = 40
lon = np.linspace(-150,-110,3)
...
```

Sections: global-land-mask, Description, Simple example, Speed test, Example of map over US

</details>

### guardrails-ai-types

Offical Guardrails AI Types

`pip install guardrails-ai-types` · installs (wheel) · licence: not stated · rank 11630 · last release 2026-07-10 · [PyPI](https://pypi.org/project/guardrails-ai-types/) · [docs](https://guardrails-ai.github.io/guardrails-ai/autoapi/guardrails_ai/types/index.html) · [source](https://github.com/guardrails-ai/guardrails-ai/tree/main/types/py)

<details><summary>README extract</summary>

A thin REST client for the guardrails-api.

Example:
```python
from guardrails_ai.sdk import GuardrailsAI, Guard, ValidationOutcome

# Init the GuardrailsAI client
client = GuardrailsAI(api_key="xxx")

# Fetch a Guard from the server
guard: Guard = await client.guards.retrieve(name="my-guard")

print(guard)

# Run a Guard to validate content
...
```

Sections: guardrails-client, Quickstart

</details>

### gliclass

Generalist and Lightweight Model for Text Classification

`pip install gliclass` · installs (wheel) · licence: Apache-2.0 · rank 11683 · last release 2026-10-31 · [PyPI](https://pypi.org/project/gliclass/)

<details><summary>README extract</summary>

GLiClass is an efficient, zero-shot sequence classification model inspired by the GLiNER framework. It achieves comparable performance to traditional cross-encoder models while being significantly more computationally efficient, offering classification results approximately 10 times faster by performing classification in a single forward pass. ...

Example:
```python
from gliclass import GLiClassModel, ZeroShotClassificationPipeline
from transformers import AutoTokenizer

model = GLiClassModel.from_pretrained("knowledgator/gliclass-small-v1.0")
tokenizer = AutoTokenizer.from_pretrained("knowledgator/gliclass-small-v1.0")

pipeline = ZeroShotClassificationPipeline(
...
```

...

</details>

### guarddog

GuardDog is a CLI tool for identifying malicious open source packages

`pip install guarddog` · installs (wheel) · licence: Apache Software License · rank 11704 · last release 2026-08-12 · [PyPI](https://pypi.org/project/guarddog/) · [source](https://github.com/DataDog/guarddog)

<details><summary>README extract</summary>

GuardDog is a CLI tool that identifies malicious PyPI and npm packages, Go modules, Rust crates, RubyGems, GitHub actions, or VSCode extensions. It runs static analysis on package source code (through YARA rules) and analyzes package metadata to detect supply chain attacks. ...

Features:
Traditional SAST tools flag every suspicious pattern independently, leading to alert fatigue. GuardDog understands that:

- Capability alone isn't malicious (network libraries should make HTTP requests) ...

Sections: GuardDog, How GuardDog Works, Why This Approach?, Risk Scoring, Getting started, Sample usage, Sandboxed Scanning, Scanning packages from S3, Rules, Running GuardDog in a GitHub Action, Running a local version of GuardDog, Unit tests, Benchmarking, Code quality checks

</details>

### groundingdino-py

open-set object detector

`pip install groundingdino-py` · installs from source (sdist only) · licence: not stated · rank 11759 · last release 2023-05-23 · [PyPI](https://pypi.org/project/groundingdino-py/)

<details><summary>README extract</summary>

Official PyTorch implementation of "Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection": the SoTA open-set object detector.

Example:
```python
from groundingdino.util.inference import load_model, load_image, predict, annotate
import cv2

model = load_model("groundingdino/config/GroundingDINO_SwinT_OGC.py", "weights/groundingdino_swint_ogc.pth")
IMAGE_PATH = "weights/dog-3.jpeg"
TEXT_PROMPT = "chair . person . dog ."
BOX_TRESHOLD = 0.35
TEXT_TRESHOLD = 0.25

...
```

Sections: sauropod: Grounding DINO, sun_with_face: Helpful Tutorial, sparkles: Highlight Projects, bulb: Highlight, fire: News, label: TODO, arrow_forward: Demo, luggage: Checkpoints, medal_military: Results, sauropod: Model: Grounding DINO

</details>

### gllm-inference-binary

A library containing components related to model inferences in Gen AI applications.

`pip install gllm-inference-binary` · does not install on CPython 3.14 · licence: not stated · rank 11806 · last release 2026-11-05 · [PyPI](https://pypi.org/project/gllm-inference-binary/)

<details><summary>README extract</summary>

A library containing components related to model inferences in Gen AI applications.

Sections: GLLM Inference, Description, Prerequisites, 1. Clone Repository, 2. Setup Authentication, 3. Quick Setup, 4. Activate Virtual Environment, Update Dependencies, Run Tests

</details>

### glean-parser

Parser tools for Mozilla's Glean telemetry

`pip install glean-parser` · installs (wheel) · licence: not stated · rank 11839 · last release 2026-10-20 · [PyPI](https://pypi.org/project/glean-parser/) · [source](https://github.com/mozilla/glean_parser)

<details><summary>README extract</summary>

Parser tools for Mozilla's Glean telemetry.

Features:
Contains various utilities for handling `metrics.yaml` and `pings.yaml` for the
Glean SDKs. This includes producing generated
code for various integrations and linting.

Sections: Glean Parser, Features, Documentation, Requirements, Usage

</details>

### gribberish

(no summary)

`pip install gribberish` · installs (wheel) · licence: not stated · rank 11944 · last release 2026-10-22 · [PyPI](https://pypi.org/project/gribberish/)

### getanyapi

Official typed Python SDK for AnyAPI: any API, one wallet, USD, no subscriptions.

`pip install getanyapi` · installs (wheel) · licence: MIT · rank 12002 · last release 2026-11-06 · [PyPI](https://pypi.org/project/getanyapi/) · [docs](https://getanyapi.com/docs) · [source](https://github.com/getanyapi-com/sdks)

<details><summary>README extract</summary>

Official typed Python SDK for AnyAPI: any API, one wallet, USD, no
subscriptions. Reach hundreds of scraping and data APIs through one interface and one key; pay
per request in real US dollars. httpx + pydantic v2, Python 3.10+, sync and async clients.

Example:
```python
from getanyapi import AnyAPI

client = AnyAPI()  # reads ANYAPI_API_KEY from the environment
res = client.reddit.search(query="mechanical keyboard")
if res.output.found:
    for post in res.output.data.posts:
        print(post.title, post.score)
print("charged", res.cost_usd, "USD")
```

Sections: getanyapi, Quickstart, Inputs vs outputs (naming asymmetry), Not found vs error, Discovery, Pagination, Request options (context-cost savers), Errors and retries, Waiting out a run that is still in flight, Agent signup, Docs

</details>

### geckordp

A client implementation of Firefox DevTools over remote debug protocol.

`pip install geckordp` · installs (wheel) · licence: MIT License · rank 12234 · last release 2024-09-03 · [PyPI](https://pypi.org/project/geckordp/) · [docs](https://jpramosi.github.io/geckordp) · [source](https://github.com/jpramosi/geckordp.git)

<details><summary>README extract</summary>

This is a client implementation of Firefox DevTools over remote debug protocol in python.

It essentially exposes the raw api to interact with the debug server and has some similarities with a common webdriver. See also Documentation.

*What's possible with geckordp?*

Geckordp is meant to be used as a low level library to build tools on top. ...

Example:
```python
import json

from geckordp.actors.root import RootActor
from geckordp.firefox import Firefox
from geckordp.profile import ProfileManager
from geckordp.rdp_client import RDPClient

""" Uncomment to enable debug output
"""
# from geckordp.settings import GECKORDP
# GECKORDP.DEBUG = 1
# GECKORDP.DEBUG_REQUEST = 1
# GECKORDP.DEBUG_RESPONSE = 1

...
```

...

</details>

### grpc-google-pubsub-v1

GRPC library for the google-pubsub-v1 service

`pip install grpc-google-pubsub-v1` · installs from source (sdist only) · licence: Apache Software License · rank 12316 · last release 2016-09-30 · [PyPI](https://pypi.org/project/grpc-google-pubsub-v1/)

<details><summary>README extract</summary>

gRPC library for google-pubsub-v1

grpc-google-pubsub-v1 is the IDL-derived library for the google-pubsub (v1) service in the googleapis repository.

.. _`googleapis`:

</details>

### garth

Garmin SSO auth + Connect client

`pip install garth` · installs (wheel) · licence: MIT License · rank 12350 · last release 2026-03-28 · [PyPI](https://pypi.org/project/garth/) · [docs](https://garth.readthedocs.io) · [source](https://github.com/matin/garth)

<details><summary>README extract</summary>

> Garth is deprecated and no longer maintained. Garmin changed their auth
> flow, breaking the mobile auth approach that Garth depends on. I'm not in a
> position to dedicate the time to adapt to these changes. See the
> announcement for details.
> Anyone is welcome to fork Garth as a starting point for a new library. ...

Sections: Garth, About, For existing users, Documentation

</details>

### gooddata-api-client

OpenAPI definition

`pip install gooddata-api-client` · installs (wheel) · licence: MIT · rank 12504 · last release 2026-11-04 · [PyPI](https://pypi.org/project/gooddata-api-client/)

<details><summary>README extract</summary>

No description provided (generated by Openapi Generator

This Python package is automatically generated by the OpenAPI Generator project:

- API version: v0
- Package version: 1.79.1
- Build package: org.openapitools.codegen.languages.PythonPriorClientCodegen

Python >=3.6

Example:
```python
import time
import gooddata_api_client
from pprint import pprint
from gooddata_api_client.api import ai_lake_api
from gooddata_api_client.model.add_database_data_source_request import AddDatabaseDataSourceRequest
from gooddata_api_client.model.add_database_data_source_response import AddDatabaseDataSourceResponse
...
```

Sections: gooddata-api-client, Requirements., Setuptools, Getting Started, Documentation for API Endpoints, Documentation For Models, Notes for Large OpenAPI documents

</details>

### grpc-google-logging-v2

GRPC library for the google-logging-v2 service

`pip install grpc-google-logging-v2` · installs from source (sdist only) · licence: Apache Software License · rank 12569 · last release 2016-09-30 · [PyPI](https://pypi.org/project/grpc-google-logging-v2/)

<details><summary>README extract</summary>

gRPC library for google-logging-v2

grpc-google-logging-v2 is the IDL-derived library for the google-logging (v2) service in the googleapis repository.

.. _`googleapis`:

</details>

### gcp-pilot

Google Cloud Platform Friendly Pilot

`pip install gcp-pilot` · installs (wheel) · licence: not stated · rank 12643 · last release 2026-03-11 · [PyPI](https://pypi.org/project/gcp-pilot/)

<details><summary>README extract</summary>

Google Cloud Pilot (gcp-pilot) is a Python library that simplifies interaction with Google Cloud Platform services. It provides a high-level, user-friendly interface to various GCP APIs, handling authentication, error management, and parameter fallback automatically.

Full documentation is available at gcp-pilot.flamingo.codes

Features:
- Parameter Fallback: Automatically detects project_id and location based on your credentials
- Friendly Errors: Converts generic HttpExceptions into more specific exceptions like NotFound, AlreadyExists, etc. ...

Example:
```python
from gcp_pilot.resource import ResourceManager

grm = ResourceManager()
```

Sections: Google Cloud Pilot, Documentation, Basic Usage, Key Features, Firestore ORM

</details>

### gruut

A tokenizer, text cleaner, and phonemizer for many human languages.

`pip install gruut` · installs from source (sdist only) · licence: MIT License · rank 12711 · last release 2024-07-03 · [PyPI](https://pypi.org/project/gruut/)

<details><summary>README extract</summary>

A tokenizer, text cleaner, and IPA phonemizer for several human languages that supports SSML.

which outputs:

Note that "wound" and "read" have different pronunciations when used in different (grammatical) contexts.

A subset of SSML is also supported:

with the output:

See the documentation for more details.

Example:
```python
from gruut import sentences

text = 'He wound it around the wound, saying "I read it was $10 to read."'

for sent in sentences(text, lang="en-us"):
    for word in sent:
        if word.phonemes:
            print(word.text, *word.phonemes)
```

Sections: Gruut, Dependencies, Numbers, Dates, and More, Command-Line Usage, Plain Text, SSML, Word Roles, Inline Lexicons, Intended Audience

</details>

### google-re2-stubs

Typestubs for google-re2

`pip install google-re2-stubs` · installs (wheel) · licence: MIT License · rank 12767 · last release 2024-10-21 · [PyPI](https://pypi.org/project/google-re2-stubs/)

### gtsam-develop

Georgia Tech Smoothing And Mapping library

`pip install gtsam-develop` · installs (wheel) · licence: BSD License · rank 12834 · last release 2026-11-08 · [PyPI](https://pypi.org/project/gtsam-develop/)

<details><summary>README extract</summary>

Development branch

The `develop` branch contains changes intended for the next GTSAM release and
may include API changes. For production use, choose the latest stable version
from the GTSAM releases. Current
development builds require C++17; Boost support is optional and controlled by
CMake options. ...

Sections: GTSAM: Georgia Tech Smoothing and Mapping Library, What is GTSAM?, Documentation, Quickstart, GTSAM 4 Compatibility, Wrappers, The Preintegrated IMU Factor, Additional Information

</details>

### geometric

Geometry optimization for quantum chemistry

`pip install geometric` · installs from source (sdist only) · licence: not stated · rank 12908 · last release 2026-05-18 · [PyPI](https://pypi.org/project/geometric/)

<details><summary>README extract</summary>

This is a geometry optimization code for molecular structures.
The code works by calling external software for the energy and
gradient through wrapper functions. Q-Chem, TeraChem, Psi4,
Molpro, Gaussian 09/16, CFOUR, QUICK, BAGEL are supported quantum chemistry
codes through the command line interface. ...

</details>

### GitHubKit-schemas-2022-11-28

GitHub Schemas for GitHubKit

`pip install GitHubKit-schemas-2022-11-28` · installs (wheel) · licence: MIT · rank 12965 · last release 2026-11-05 · [PyPI](https://pypi.org/project/GitHubKit-schemas-2022-11-28/) · [docs](https://github.com/yanyongyu/githubkit) · [source](https://github.com/yanyongyu/githubkit)

<details><summary>README extract</summary>

_✨ The modern, all-batteries-included GitHub SDK for Python ✨_

_✨ Support both sync and async calls, fully typed ✨_

_✨ Always up to date, like octokit ✨_

 Documentation |
 Report Bug |
 GitHub Docs

This package provides the models and GitHub schemas for GitHubKit.

When GitHub schemas are updated, this package will be updated accordingly. ...

</details>

### g4f

The official gpt4free repository | various collection of powerful language models

`pip install g4f` · installs (wheel) · licence: not stated · rank 12973 · last release 2026-11-02 · [PyPI](https://pypi.org/project/g4f/) · [source](https://github.com/xtekky/gpt4free)

<details><summary>README extract</summary>

[](

 Created by @xtekky,
 maintained by @hlohaus

Support the project on

 GitHub Sponsors


GPT4Free (g4f) is a community-driven project that aggregates multiple accessible providers and interfaces to make working with modern LLMs and media-generation models easier and more flexible. ...

Example:
```python
from g4f.gui import run_gui
run_gui()
```

Sections: GPT4Free (g4f), What’s included, Quick links, Related projects, Requirements & compatibility, Docker (recommended), Slim Docker image (x64 & arm64), Sandbox desktop (Docker), Standalone launcher (no checkout), Running the app, GUI (web client), FastAPI / Inference API, CLI, MCP Server

</details>

### gruut-lang-en

English language files for gruut tokenizer/phonemizer

`pip install gruut-lang-en` · installs from source (sdist only) · licence: MIT License · rank 12983 · last release 2024-07-03 · [PyPI](https://pypi.org/project/gruut-lang-en/)

<details><summary>README extract</summary>

Language-specific files for English (en) in gruut

</details>

### gruut-ipa

Library for manipulating pronunciations using the International Phonetic Alphabet (IPA)

`pip install gruut-ipa` · installs from source (sdist only) · licence: MIT License · rank 12996 · last release 2022-03-11 · [PyPI](https://pypi.org/project/gruut-ipa/)

<details><summary>README extract</summary>

Library for manipulating International Phonetic Alphabet (IPA) pronunciations.

Features include:

* Getting the category and details of a phone, e.g. "open front unrounded vowel" for ɶ

 * Phones (`/ˈt͡ʃuːz/` to `ˈt͡ʃ uː z` )
 * Phonemes (`/kˈaʊ/` to `k ˈaʊ` for U.S. English)

 * IPA
 * espeak
 * sampa

Supported Languages: ...

Sections: Gruut IPA, Dependencies, Phones and Phonemes, Phonemes, Usage, Alternative Phoneme Sets, Scripts, Phones

</details>

### gdsfactoryplus

Adds powerful features such as foundry PDKs, simulations, and verification tools like DRC and LVS.

`pip install gdsfactoryplus` · does not install on CPython 3.14 · licence: LicenseRef-Proprietary · rank 13206 · last release 2026-11-07 · [PyPI](https://pypi.org/project/gdsfactoryplus/) · [docs](https://gdsfactory.com/plus/)

<details><summary>README extract</summary>

Adds powerful features such as foundry PDKs, simulations, and verification tools like
DRC and LVS.

- Documentation is publicly hosted at gdsfactory.com/plus

Sections: GDSFactory+ 2.3, Documentation

</details>

### grafana-django-saml2-auth

Deprecated compatibility package. Install django-saml2-auth-community instead.

`pip install grafana-django-saml2-auth` · installs (wheel) · licence: Apache-2.0 · rank 13249 · last release 2026-04-11 · [PyPI](https://pypi.org/project/grafana-django-saml2-auth/)

<details><summary>README extract</summary>

This package name is deprecated and kept only as a compatibility shim.
Please install:
`grafana-django-saml2-auth==3.21.0` depends on `django-saml2-auth-community==3.21.0`.

</details>

### gravity

Command-line utilities to assist in managing Galaxy servers

`pip install gravity` · installs (wheel) · licence: MIT · rank 13256 · last release 2026-08-26 · [PyPI](https://pypi.org/project/gravity/)

<details><summary>README extract</summary>

Process management for Galaxy servers.

* License: MIT

Features:
Modern Galaxy servers run multiple disparate processes: gunicorn for serving the web application, celery for
asynchronous tasks, tusd for fault-tolerant uploads, standalone Galaxy processes for job handling, and more. ...

Sections: Overview, Quick Start, Usage, 1.2.4, 1.2.3, 1.2.2, 1.2.1, 1.2.0, Breaking Changes, Major Changes, Other Changes, 1.1.1, 1.1.0, 1.0.8

</details>

### getstream

GetStream Python SDK - Build scalable activity feeds, chat, and video calling applications

`pip install getstream` · installs (wheel) · licence: not stated · rank 13308 · last release 2026-11-04 · [PyPI](https://pypi.org/project/getstream/)

<details><summary>README extract</summary>

Check out our:

- ⭐ Chat API
- 📱 Video API
- 🔔 Activity Feeds

Features:
- Video call creation and management
- Chat session creation and management
- Token generation for user authentication

Example:
```python
from getstream import Stream

client = Stream(api_key="your_api_key", api_secret="your_api_secret")
```

Sections: Official Python SDK for Stream, Features, Migrating from stream-chat?, Usage, Users and Authentication, Video API - Calls, Getting Response Data, Reusing the client and connection pooling, Logging, Retries, Sending null, App configuration, Chat API - Channels, 🚀 Quick Start

</details>

### gogo-python

Python package for gogoproto

`pip install gogo-python` · installs (wheel) · licence: MIT License · rank 13384 · last release 2020-12-05 · [PyPI](https://pypi.org/project/gogo-python/)

<details><summary>README extract</summary>

Python package for gogoproto(

Example:
```python
from github.com.gogo.protobuf.gogoproto import gogo_pb2
```

</details>

### glean-sdk

Mozilla's Glean Telemetry SDK: The Machine that Goes 'Ping!'

`pip install glean-sdk` · installs (wheel) · licence: not stated · rank 13465 · last release 2026-10-22 · [PyPI](https://pypi.org/project/glean-sdk/) · [source](https://github.com/mozilla/glean)

<details><summary>README extract</summary>

[][book]

All documentation is available online:

Features:
Refer to the documentation for using and developing the Glean SDK.

For an overview of Glean beyond just the SDK, see the section in the Firefox data docs.

The code in this repository is organized as follows: ...

Sections: Glean SDK, Documentation, The Glean SDK Book, Overview, Contact

</details>

### Geode-Explicit

Geode-solutions OpenGeode module for building explicit models

`pip install Geode-Explicit` · installs (wheel) · licence: Proprietary · rank 13647 · last release 2026-11-08 · [PyPI](https://pypi.org/project/Geode-Explicit/)

### gnews

Provide an API to search for articles on Google News and returns a usable JSON response.

`pip install gnews` · installs (wheel) · licence: MIT License · rank 13711 · last release 2026-10-09 · [PyPI](https://pypi.org/project/gnews/) · [docs](https://github.com/ranahaani/GNews/blob/master/README.md) · [source](https://github.com/ranahaani/GNews/)

<details><summary>README extract</summary>

[][contributors-url]
[][forks-url]
[][stars-url]
[][issues-url]
[][license-url]
[][download-url]
[][linkedin-url]
[][docs-url]

Sponsored by SearchApi

 A Happy and lightweight Python Package that Provides an API to search for articles on Google News and returns a usable JSON response! 🚀 ...

Example:
```python
from gnews import GNews

google_news = GNews()
pakistan_news = google_news.get_news('Pakistan')
print(pakistan_news[0])
```

Sections: GNews 📰, About GNews, Demo, Getting Started, Option 1: Setup with Docker, Example usage, 📘 Interactive Tutorial, Get top news, Get news by keyword, Get news by major topic, Get news by geo location, Get news by site, Results specification, Example Initialization

</details>

### gruut-lang-es

Spanish language files for gruut tokenizer/phonemizer

`pip install gruut-lang-es` · installs from source (sdist only) · licence: MIT License · rank 13773 · last release 2024-07-03 · [PyPI](https://pypi.org/project/gruut-lang-es/)

<details><summary>README extract</summary>

Language-specific files for Spanish (es) in gruut

</details>

### Geode-Conversion

Conversion module for Geode-solutions OpenGeode modules

`pip install Geode-Conversion` · installs (wheel) · licence: Proprietary · rank 13812 · last release 2026-11-08 · [PyPI](https://pypi.org/project/Geode-Conversion/)

<details><summary>README extract</summary>

Copyright (c) 2019 - 2026, Geode-solutions

Sections: Geode-Conversionby Geode-solutions, Conversion OpenGeode module

</details>

### gruut-lang-de

German language files for gruut tokenizer/phonemizer

`pip install gruut-lang-de` · installs from source (sdist only) · licence: MIT License · rank 13819 · last release 2024-07-03 · [PyPI](https://pypi.org/project/gruut-lang-de/)

### gazetteer-matcher

Constraint-driven gazetteer matcher for Home Assistant intents

`pip install gazetteer-matcher` · installs (wheel) · licence: Apache-2.0 · rank 13852 · last release 2026-09-11 · [PyPI](https://pypi.org/project/gazetteer-matcher/)

<details><summary>README extract</summary>

An English-language, constraint-driven intent recognizer for Home Assistant
voice commands. It complements Home Assistant's built-in sentence grammars by
handling home-specific names, fuzzy wording, compound requests, and explicit
conversation references while rejecting interpretations that do not fit the
upstream intent schema.

Features:
- Flexible and fuzzy target matching for entities, areas, floors, domains,
 and actions: `turn on the bedrom lamp` resolves to `Bedroom Lamp`. ...

Example:
```python
from gazetteer_matcher import GazetteerMatcher

matcher = GazetteerMatcher(
    home={
        "areas": {
            "kitchen": {"name": "Kitchen", "floor": "ground"},
        },
        "floors": {
            "ground": {"name": "Ground Floor"},
        },
        "entities": {},
    }
)
...

</details>

### gruut-lang-fr

French language files for gruut tokenizer/phonemizer

`pip install gruut-lang-fr` · installs from source (sdist only) · licence: MIT License · rank 13930 · last release 2022-05-11 · [PyPI](https://pypi.org/project/gruut-lang-fr/)

### gsplat

Python package for differentiable rasterization of gaussians

`pip install gsplat` · installs (wheel) · licence: not stated · rank 13950 · last release 2025-07-04 · [PyPI](https://pypi.org/project/gsplat/)

### graylint

Run linters and show only new errors compared to an older commit

`pip install graylint` · installs (wheel) · licence: BSD · rank 13958 · last release 2024-07-31 · [PyPI](https://pypi.org/project/graylint/) · [source](https://github.com/akaihola/graylint)

<details><summary>README extract</summary>

This utility runs linters on Python source code files.
However, when run in a Git repository, it runs the linters both in an old and a newer
revision of the source tree. It then only reports those linting messages which appeared
after the modifications to the source code files between those revisions. ...

Features:
You want to lint your code with more or less strict linter rules.
Your code base is known to violate some of those linter rules.

When running the linters, you only want to see the new violations which have appeared
e.g. ...

Example:
```python
first_name = input("Enter your first name: ")
if first_name == "Guido":
    print("I know you")
else:
    print("Nice to meet you")
```

...

</details>

### gmft

Lightweight, performant, deep table extraction

`pip install gmft` · installs (wheel) · licence: MIT License · rank 14026 · last release 2026-07-24 · [PyPI](https://pypi.org/project/gmft/)

<details><summary>README extract</summary>

There are many pdfs out there, and many of those pdfs have tables. But despite a plethora of table extraction options, there is still no definitive extraction method.

gmft converts pdf tables to many formats. It is lightweight, modular, and performant. Batteries included: it just works, offering strong performance with the default settings. ...

Features:
Fast, lightweight, and performant, gmft is a great choice for extracting tables from pdfs.

The extraction quality is superb: check out the bulk extract notebook for approximate quality. ...

Example:
```python
# new in v0.3: gmft.auto
from gmft.auto import CroppedTable, TableDetector, AutoTableFormatter, AutoTableDetector
from gmft.pdf_bindings import PyPDFium2Document

detector = AutoTableDetector()
formatter = AutoTableFormatter()

...

</details>

### granite-tsfm

Public notebooks and utilities for TSFM

`pip install granite-tsfm` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 14048 · last release 2026-10-29 · [PyPI](https://pypi.org/project/granite-tsfm/) · [source](https://github.com/ibm-granite/granite-tsfm)

<details><summary>README extract</summary>

Public notebooks, utilities, and serving components for working with Time Series Foundation Models (TSFM).

The core TSFM time series models have been made available on Hugging Face -- check out the granite time series collection here. Additional details can be found in our
wiki. Information on the services component can be found here. ...

Sections: TSFM: Time Series Foundation Models, Python Version, Initial Setup, 🔗 Links to the notebooks, 📗 Google Colab Tutorials, 🪲 Issues, 🌏 Wiki, Notice

</details>

### gower

Python implementation of Gowers distance, pairwise between records in two data sets

`pip install gower` · installs (wheel) · licence: MIT License · rank 14088 · last release 2022-11-13 · [PyPI](https://pypi.org/project/gower/)

<details><summary>README extract</summary>

<!-- badges: start -->

<!-- badges: end -->

Gower's distance calculation in Python. Gower Distance is a distance measure that can be used to calculate distance between two entity whose attribute has a mixed of categorical and numerical values. Gower (1971) A general coefficient of similarity and some of its properties. Biometrics 27 857–874. ...

Example:
```python
import numpy as np
import pandas as pd
import gower

Xd=pd.DataFrame({'age':[21,21,19, 30,21,21,19,30,None],
'gender':['M','M','N','M','F','F','F','F',None],
'civil_status':['MARRIED','SINGLE','SINGLE','SINGLE','MARRIED','SINGLE','WIDOW','DIVORCED',None],
'salary':[3000.0,1200.0 ,32000.0,1800.0 ,2900.0 ,1100.0 ,10000.0,1500.0,None],
...
```

...

</details>

### Geode-Common

Common module for licensed Geode-solutions modules

`pip install Geode-Common` · installs (wheel) · licence: Proprietary · rank 14313 · last release 2026-11-08 · [PyPI](https://pypi.org/project/Geode-Common/)

<details><summary>README extract</summary>

Sections: Geode-Commonby Geode-solutions, Common module for proprietary Geode-solutions modules

</details>

### graphene-directives

Schema Directives implementation for graphene

`pip install graphene-directives` · installs (wheel) · licence: MIT License · rank 14402 · last release 2026-07-29 · [PyPI](https://pypi.org/project/graphene-directives/) · [docs](https://github.com/strollby/graphene-directives) · [source](https://github.com/strollby/graphene-directives)

<details><summary>README extract</summary>

Schema Directives implementation for graphene

[][pypi-url]
[][pypi-version-url]
[][pypi-downloads-url]
[][tests-url]
[][coveralls-url]

Example:
```python
import graphene
from graphql import GraphQLArgument, GraphQLInt, GraphQLNonNull, GraphQLString

from graphene_directives import (
    CustomDirective,
    DirectiveLocation,
    build_schema,
    directive,
)

CacheDirective = CustomDirective(
    name="cache",
    locations=[DirectiveLocation.FIELD_DEFINITION, DirectiveLocation.OBJECT],
...
```

Sections: Graphene Directives, Example, Using `@directive`, Using `directive_decorator`, Custom Input Validation, Complex Use Cases

</details>

### Geode-Background

Geode-solutions OpenGeode module for building background meshes

`pip install Geode-Background` · installs (wheel) · licence: Proprietary · rank 14463 · last release 2026-11-08 · [PyPI](https://pypi.org/project/Geode-Background/)

### gate-api

Gate API

`pip install gate-api` · installs (wheel) · licence: Apache Software License · rank 14478 · last release 2026-11-03 · [PyPI](https://pypi.org/project/gate-api/)

<details><summary>README extract</summary>

Welcome to Gate API
APIv4 provides operations related to spot, margin, and contract trading, including public interfaces for querying market data and authenticated private interfaces for implementing API-based automated trading.

This Python package is automatically generated by the OpenAPI Generator project:

- API version: v4.106.179 ...

Example:
```python
from future import print_function

import gate_api
from gate_api.exceptions import ApiException, GateApiException

# Defining the host is optional and defaults to
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
...
```

...

</details>

### Geode-Implicit

Licensed framework for working with implicit modeling

`pip install Geode-Implicit` · installs (wheel) · licence: Proprietary · rank 14591 · last release 2026-11-02 · [PyPI](https://pypi.org/project/Geode-Implicit/)

<details><summary>README extract</summary>

Geode-Implicit is an [OpenGeode] module for working with implicit modeling, from the construction of an implicit model using data points to its explicitation in a topologically valid meshed model.

Copyright (c) 2019 - 2026, Geode-solutions

Sections: Geode-Implicitby Geode-solutions, Module for working with implicit modeling., Introduction

</details>

### gnocchiclient

Python client library for Gnocchi

`pip install gnocchiclient` · installs (wheel) · licence: Apache Software License · rank 14894 · last release 2025-03-24 · [PyPI](https://pypi.org/project/gnocchiclient/)

<details><summary>README extract</summary>

Python bindings to the Gnocchi API

This is a client for Gnocchi API. There's a Python API (the `gnocchiclient`
module), and a `command-line script` (installed as `gnocchi`). Each
implements the entire Gnocchi API.

* Free software: Apache license

</details>

### G722

This is a package for G.722 module

`pip install G722` · installs (wheel) · licence: Public-Domain · rank 14899 · last release 2026-06-29 · [PyPI](https://pypi.org/project/G722/)

<details><summary>README extract</summary>

The G.722 module is a bit-exact implementation of the ITU G.722 specification
for all three specified bit rates: 64,000 bps, 56,000 bps and 48,000 bps. It
passes the ITU tests.

To allow fast and flexible interworking with narrowband telephony, the
encoder and decoder support an option for the linear audio to be an 8 kHz
stream. ...

Sections: libg722, Introduction, macOS and Linux, iOS, Python Build Options, Python API, Pull Library Into Your Docker Container

</details>

### geemap

A Python package for interactive mapping using Google Earth Engine and ipyleaflet

`pip install geemap` · installs (wheel) · licence: MIT License · rank 14904 · last release 2026-10-01 · [PyPI](https://pypi.org/project/geemap/)

<details><summary>README extract</summary>

A Python package for interactive geospatial analysis and visualization with Google Earth Engine

- GitHub repo: <
- Documentation: <
- PyPI: <
- Conda-forge: <
- 360+ GEE notebook examples: <
- GEE Tutorials on YouTube: <
- Free software: MIT license

Join our Discord server 👇 ...

Features:
Below is a partial list of features available for the geemap package. Please check the examples page for notebook examples, GIF animations, and video tutorials.

- Convert Earth Engine JavaScripts to Python scripts and Jupyter notebooks. ...

Sections: geemap, Announcement, Introduction, Key Features

</details>

### genicam

The official Python Binding for the GenICam GenApi & the GenTL Producers

`pip install genicam` · installs (wheel) · licence: LicenseRef-GenICam-1.6 · rank 14969 · last release 2026-09-01 · [PyPI](https://pypi.org/project/genicam/)

<details><summary>README extract</summary>

The `genicam` module is the official Python binding of GenICam that is developed and maintained by the GenICam committee.

The `genicam` module consists of two sub-modules. The one is `genapi` and the other is `gentl`. The `genapi` module gives you a way to control GenICam features of the target device supports. ...

Example:
```python
from genicam.genapi import NodeMap

node_map = NodeMap()
```

Sections: About the genicam module, Using the genicam module, The genapi module, Creating a node map object, Changing a feature value, The gentl module, Links, Harvester, EMVA

</details>

