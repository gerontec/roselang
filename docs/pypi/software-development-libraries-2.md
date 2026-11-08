# Software Development / Libraries (part 2 of 5)

[Index](README.md) · 1884 packages in this topic, 1694 more listed under another topic, by downloads.

[part 1](software-development-libraries.md) · part 2 · [part 3](software-development-libraries-3.md) · [part 4](software-development-libraries-4.md) · [part 5](software-development-libraries-5.md)

### comtypes

Pure Python COM package

`pip install comtypes` · installs (wheel) · licence: MIT · rank 3029 · last release 2026-09-21 · [PyPI](https://pypi.org/project/comtypes/) · [source](https://github.com/enthought/comtypes)

<details><summary>README extract</summary>

`comtypes` is a lightweight pure Python COM package based on the `ctypes` foreign function interface library.

`comtypes` allows you to define, call, and implement custom and dispatch-based COM interfaces in pure Python.

`comtypes` requires Windows and Python 3.9 or later. ...

Sections: comtypes, Dependencies, For Enterprise, Frequently Asked Questions, Documentation

</details>

### cucumber-expressions

Cucumber Expressions - a simpler alternative to Regular Expressions

`pip install cucumber-expressions` · installs (wheel) · licence: MIT · rank 3040 · last release 2026-08-05 · [PyPI](https://pypi.org/project/cucumber-expressions/) · [source](https://github.com/cucumber/cucumber-expressions.git)

### html5rdf

HTML parser based on the WHATWG HTML specification

`pip install html5rdf` · installs (wheel) · licence: MIT License · rank 3042 · last release 2024-10-30 · [PyPI](https://pypi.org/project/html5rdf/)

<details><summary>README extract</summary>

html5rdf is a pure-python library for parsing HTML to DOMFragment objects for the use in RDFLib.
html5rdf is a fork of html5lib-python. See below for the html5lib README.

It is designed to conform to the WHATWG HTML specification, as is implemented by all major
web browsers. ...

Example:
```python
import html5rdf
with open("mydocument.html", "rb") as f:
    document = html5rdf.parse(f)
```

Sections: html5rdf, Usage, Optional Dependencies, Bugs, Tests, Patches and suggestions, HTML5Lib-modern

</details>

### pyvmomi

VMware vSphere Python SDK

`pip install pyvmomi` · installs (wheel) · licence: Apache Software License · rank 3054 · last release 2026-09-03 · [PyPI](https://pypi.org/project/pyvmomi/)

<details><summary>README extract</summary>

pyVmomi is the Python SDK for the VMware vSphere Management API that allows you to rapidly build solutions integrated with VMware ESXi and vCenter Server.
For accessing features from the vSphere Automation APIs
(REST), please refer to the VMware vSphere Automation SDK for Python.

Sections: pyvmomi, Getting Started, Documentation, Versioning, Compatibility Policy, Related Projects

</details>

### aiohttp-fast-zlib

Use the fastest installed zlib compatible library with aiohttp

`pip install aiohttp-fast-zlib` · installs (wheel) · licence: Apache Software License · rank 3070 · last release 2025-06-07 · [PyPI](https://pypi.org/project/aiohttp-fast-zlib/) · [source](https://github.com/bluetooth-devices/aiohttp-fast-zlib)

<details><summary>README extract</summary>

Source Code:

Use the fastest installed zlib compatible library with aiohttp

zlib is be a bottleneck for aiohttp, especially for websocket connections. `aiohttp-fast-zlib` replaces usage of `zlib` in `aiohttp` with `isal` or `zlib-ng` which is a drop-in faster replacement in most cases. ...

Example:
```python
import aiohttp_zlib_fast

# isal is preferred over zlib_ng if it is available
aiohttp_zlib_fast.enable()
aiohttp_zlib_fast.enable()
```

Sections: aiohttp-fast-zlib, Usage

</details>

### triad

A collection of python utils for Fugue projects

`pip install triad` · installs (wheel) · licence: Apache-2.0 · rank 3097 · last release 2026-11-06 · [PyPI](https://pypi.org/project/triad/)

<details><summary>README extract</summary>

A collection of python utility functions for Fugue projects

Sections: Triad, 1.0.4, 1.0.3, 1.0.2, 1.0.1, 1.0.0, 0.9.8, 0.9.7, 0.9.6, 0.9.5, 0.9.4, 0.9.3, 0.9.2, 0.9.1

</details>

### flask-talisman

HTTP security headers for Flask.

`pip install flask-talisman` · installs (wheel) · licence: Apache Software License · rank 3107 · last release 2023-08-03 · [PyPI](https://pypi.org/project/flask-talisman/)

<details><summary>README extract</summary>

Features:
Note: Feature Policy has largely been renamed Permissions Policy
in the latest draft and some features are likely to move to Document Policy.
At this writing, most browsers support the `Feature-Policy` HTTP Header name. ...

Example:
```python
csp = {
    'default-src': '\'self\'',
    'object-src': '\'none\'',
}
talisman = Talisman(app, content_security_policy=csp)
```

Sections: Options, Per-view options, Example 1, Example 2, Example 3, Example 4, Example 5, Example 6, Example 7, Feature Policy, Geolocation Example, Permissions Policy, Geolocation and Microphone Example, Document Policy

</details>

### trame-components

Core components for trame widgets

`pip install trame-components` · installs (wheel) · licence: Apache Software License · rank 3124 · last release 2025-05-30 · [PyPI](https://pypi.org/project/trame-components/)

<details><summary>README extract</summary>

trame-components extend trame widgets with helper components that are core to trame widgets.

This package is not supposed to be used by itself but rather should come as a dependency of trame.
For any specificity, please refer to the trame documentation.

Sections: trame-components: vue.js utility widgets, Usage, Enjoying trame?, JavaScript dependency

</details>

### pynput

Monitor and control user input devices

`pip install pynput` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 3126 · last release 2026-05-12 · [PyPI](https://pypi.org/project/pynput/)

_README extract left out: share-alike licence._

### fugue

An abstraction layer for distributed computing

`pip install fugue` · installs (wheel) · licence: Apache-2.0 · rank 3132 · last release 2026-11-06 · [PyPI](https://pypi.org/project/fugue/) · [source](http://github.com/fugue-project/fugue)

<details><summary>README extract</summary>

| Tutorials | API Documentation | Chat with us on slack! |

| | | |

Fugue is a unified interface for distributed computing that lets users execute Python, Pandas, and SQL code on Spark, Dask, and Ray with minimal rewrites.

Fugue is most commonly used for: ...

Example:
```python
import pandas as pd
from typing import Dict

input_df = pd.DataFrame({"id":[0,1,2], "value": (["A", "B", "C"])})
map_dict = {"A": "Apple", "B": "Banana", "C": "Carrot"}

def map_letter_to_food(df: pd.DataFrame, mapping: Dict[str, str]) -> pd.DataFrame:
    df["value"] = df["value"].map(mapping)
    return df
```

Sections: Fugue API, FugueSQL, Getting Started, Using binder, Using Docker, Jupyter Notebook Extension, Ecosystem, Case Studies, Mentioned Uses, Further Resources, Blogs, Conferences

</details>

### scylla-driver

Scylla Driver for Apache Cassandra

`pip install scylla-driver` · installs (wheel) · licence: Apache-2.0 · rank 3140 · last release 2026-11-02 · [PyPI](https://pypi.org/project/scylla-driver/) · [docs](https://scylladb.github.io/python-driver/) · [source](https://github.com/scylladb/python-driver/)

<details><summary>README extract</summary>

A modern, feature-rich and highly-tunable Python client library for Scylla Open Source (2.1+) and Apache Cassandra (2.1+) and
Scylla Enterprise (2018.1.x+) using exclusively Cassandra's binary protocol and Cassandra Query Language v3.

The driver supports Python versions 3.10-3.15.

Features:
* Synchronous and Asynchronous APIs
* Simple, Prepared, and Batch statements
* Asynchronous IO, parallel execution, request pipelining
* Connection pooling
* Automatic node discovery
* Automatic reconnection
* Configurable load balancing and retry ...

Sections: Scylla Python Driver, Features, Documentation, Training, Object Mapper, Error Handling, Reporting Problems, Getting Help

</details>

### coredis

Fast, async, fully-typed Redis client with support for cluster and sentinel

`pip install coredis` · installs (wheel) · licence: MIT · rank 3147 · last release 2026-08-31 · [PyPI](https://pypi.org/project/coredis/) · [docs](https://coredis.readthedocs.org) · [source](https://github.com/alisaifee/coredis)

<details><summary>README extract</summary>

> [!IMPORTANT]
> To learn about breaking changes and migration steps for version 6 please see
> Migrating from 5.x to 6.0.
> If you are looking for the 5.x implementation, please
> refer to the 5.x branch.

Fast, async, fully-typed Redis client with support for cluster and sentinel

Features:
- Fully typed, even when using pipelines, Lua scripts, and libraries
- Redis Cluster and Sentinel support
- Built with structured concurrency on `anyio`, supports both `asyncio` and `trio` ...

Example:
```python
import anyio
import coredis

async def main() -> None:
    client = coredis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
    # or cluster
    # client = coredis.RedisCluster(startup_nodes=[coredis.connection.TCPLocation("127.0.0.1", 6379)], decode_responses=True)
...

</details>

### adagio

The Dag IO Framework for Fugue projects

`pip install adagio` · installs (wheel) · licence: Apache Software License · rank 3149 · last release 2024-08-14 · [PyPI](https://pypi.org/project/adagio/)

<details><summary>README extract</summary>

Join Fugue-Project on Slack

A Dag IO framework for Fugue projects

</details>

### funcsigs

Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+

`pip install funcsigs` · installs (wheel) · licence: Apache Software License · rank 3161 · last release 2016-04-25 · [PyPI](https://pypi.org/project/funcsigs/)

<details><summary>README extract</summary>

`funcsigs` is a backport of the PEP 362 function signature features from
Python 3.3's inspect module. The backport is compatible with Python 2.6, 2.7
as well as 3.3 and up. 3.2 was supported by version 0.4, but with setuptools and
pip no longer supporting 3.2, we cannot make any statement about 3.2
compatibility. ...

Example:
```python
>>> from funcsigs import signature
>>> def foo(a, b=None, *args, **kwargs):
...     pass
...
>>> sig = signature(foo)
>>> sig
<funcsigs.Signature object at 0x...>
>>> sig.parameters
OrderedDict([('a', <Parameter at 0x... 'a'>), ('b', <Parameter at 0x... 'b'>), ('args', <Parameter at 0x... 'args'>), ('kwargs', <Parameter at 0x... 'kwargs'>)])
...
```

...

</details>

### pytest-profiling

Profiling plugin for py.test

`pip install pytest-profiling` · installs (wheel) · licence: MIT License · rank 3162 · last release 2024-11-29 · [PyPI](https://pypi.org/project/pytest-profiling/)

<details><summary>README extract</summary>

Profiling plugin for pytest, with tabular and heat graph output.

Tests are profiled with cProfile and analysed with pstats; heat graphs are
generated using gprof2dot and dot.

Sections: Pytest Profiling Plugin, Usage, 1.8.1 (2024-11-29), 1.8.0 (2024-10-17), 1.7.1 (2019-05-28), 1.7.0 (2019-02-21), 1.6.2 (2019-02-21), 1.6.1 (2019-02-12), 1.6.0 (2019-02-12), 1.5.1 (2019-01-24), 1.5.0 (2019-01-23), 1.4.1 (2019-01-18), 1.4.0 (2019-01-15), 1.3.1 (2018-06-28)

</details>

### google-apitools

client libraries for humans

`pip install google-apitools` · installs (wheel) · licence: Apache Software License · rank 3185 · last release 2025-09-24 · [PyPI](https://pypi.org/project/google-apitools/)

<details><summary>README extract</summary>

DEPRECATED - Please see alternatives below

`google-apitools` is a collection of utilities to make it easier to build
client-side tools, especially those that talk to Google APIs.

NOTE: This library is deprecated and unsupported. Please read below for suggested alternatives. ...

Sections: google-apitools, Alternatives to apitools, Running the tests

</details>

### Rx

Reactive Extensions (Rx) for Python

`pip install Rx` · installs (wheel) · licence: MIT License · rank 3198 · last release 2021-04-25 · [PyPI](https://pypi.org/project/Rx/)

<details><summary>README extract</summary>

*A library for composing asynchronous and event-based programs using observable collections and
query operator functions in Python*

For v1.X please go to the v1 branch.

RxPY v3.x runs on Python 3.6 or above. To install
RxPY: ...

Example:
```python
import rx
from rx import operators as ops

source = rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

composed = source.pipe(
    ops.map(lambda s: len(s)),
    ops.filter(lambda i: i >= 5)
)
composed.subscribe(lambda value: print("Received {0}".format(value)))
```

Sections: The Reactive Extensions for Python (RxPY), RxPY v3.0, About ReactiveX, Learning RxPY, Differences from .NET and RxJS

</details>

### jschema-to-python

Generate source code for Python classes from a JSON schema.

`pip install jschema-to-python` · installs (wheel) · licence: MIT License · rank 3200 · last release 2019-10-05 · [PyPI](https://pypi.org/project/jschema-to-python/)

<details><summary>README extract</summary>

Generate Python classes from a JSON schema.

Sections: jschema-to-python, Usage

</details>

### gzip-stream

Compress stream by GZIP on the fly.

`pip install gzip-stream` · installs from source (sdist only) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication · rank 3201 · last release 2021-12-08 · [PyPI](https://pypi.org/project/gzip-stream/)

<details><summary>README extract</summary>

`gzip-stream` is a super-tiny library that will help you compress by GZIP
on-the-fly.

`GZIPCompressedStream` class instance acting like an any other stream (in fact,
`GZIPCompressedStream` inherits io.RawIOBase),
but wraps another stream and compress it on-the-fly. ...

Example:
```python
from gzip_stream import GZIPCompressedStream
from my_upload_lib import MyUploadClient

upload_client = MyUploadClient()
with open('my_very_big_1tb_file.txt') as file_to_upload:
    compressed_stream = GZIPCompressedStream(
        file_to_upload,
        compression_level=7
    )
    upload_client.upload_fileobj(compressed_stream)
```

</details>

### pywebview

Build GUI for your Python program with JavaScript, HTML, and CSS

`pip install pywebview` · installs (wheel) · licence: BSD License · rank 3204 · last release 2026-04-15 · [PyPI](https://pypi.org/project/pywebview/) · [source](https://github.com/r0x0r/pywebview)

### ulid-py

Universally Unique Lexicographically Sortable Identifier

`pip install ulid-py` · installs (wheel) · licence: Apache Software License · rank 3209 · last release 2020-09-15 · [PyPI](https://pypi.org/project/ulid-py/)

<details><summary>README extract</summary>

Universally Unique Lexicographically Sortable Identifier in Python 3.

Features:
UUID can be suboptimal for many uses-cases because:

* It isn't the most character efficient way of encoding 128 bits of randomness
* UUID v1/v2 is impractical in many environments, as it requires access to a unique, stable MAC address
* UUID v3/v5 ...

Example:
```python
>>> import ulid
>>> ulid.new()
<ULID('01BJQE4QTHMFP0S5J153XCFSP9')>
```

Sections: ulid, Usage, Future Items, Goals, Why not UUID?, Specification, Components, Sorting, Encoding, Binary Layout and Byte Order, String Representation, Links

</details>

### tinker

The official Python SDK for the tinker API

`pip install tinker` · installs (wheel) · licence: Apache Software License · rank 3240 · last release 2026-11-07 · [PyPI](https://pypi.org/project/tinker/) · [docs](https://tinker-docs.thinkingmachines.ai/) · [source](https://github.com/thinking-machines-lab/tinker)

<details><summary>README extract</summary>

Documentation:
 tinker-docs.thinkingmachines.ai

</details>

### secure

A lightweight package that adds security headers for Python web frameworks.

`pip install secure` · installs (wheel) · licence: MIT · rank 3243 · last release 2026-04-22 · [PyPI](https://pypi.org/project/secure/) · [docs](https://github.com/TypeError/secure/tree/main/docs) · [source](https://github.com/TypeError/secure)

<details><summary>README extract</summary>

HTTP security headers for Python web applications, centered on one object: `Secure`.

`secure` exists to keep header policy out of ad hoc view code. Instead of copying header strings into routes, middleware, and framework-specific hooks, you configure one `Secure` instance and apply it consistently.

Hand-written header code tends to drift. ...

Example:
```python
from secure import Secure

class Response:
    def init(self):
        self.headers = {}

response = Response()
Secure.with_default_headers().set_headers(response)
```

Sections: secure, Quick start, Presets, Middleware, WSGI, ASGI, Advanced usage, Custom policy, Optional validation, Framework examples, FastAPI, Flask, Starlette, Links

</details>

### immutables

Immutable Collections

`pip install immutables` · installs from source (sdist only) · licence: Apache Software License · rank 3250 · last release 2024-10-10 · [PyPI](https://pypi.org/project/immutables/) · [source](https://github.com/MagicStack/immutables)

<details><summary>README extract</summary>

An immutable mapping type for Python.

The underlying datastructure is a Hash Array Mapped Trie (HAMT)
used in Clojure, Scala, Haskell, and other functional languages.
This implementation is used in CPython 3.7 in the `contextvars`
module (see PEP 550 and
PEP 567 for more details). ...

Example:
```python
import immutables

map = immutables.Map(a=1, b=2)

print(map['a'])
# will print '1'

print(map.get('z', 100))
# will print '100'

print('z' in map)
# will print 'False'
```

Sections: immutables, API

</details>

### django-ses

A Django email backend for Amazon's Simple Email Service (SES)

`pip install django-ses` · installs (wheel) · licence: MIT License · rank 3258 · last release 2026-10-29 · [PyPI](https://pypi.org/project/django-ses/) · [docs](https://github.com/django-ses/django-ses/blob/main/README.rst) · [source](https://github.com/django-ses/django-ses)

<details><summary>README extract</summary>

:Info: A Django email backend for Amazon's Simple Email Service
:Author: Harry Marr (
:Collaborators: Paul Craciunoiu (

Django-SES is a drop-in mail backend for Django. Instead of sending emails
through a traditional SMTP mail server, Django-SES routes email through
Amazon Web Services' excellent Simple Email Service (SES). ...

Features:
Configuring, maintaining, and dealing with some complicated edge cases can be
time-consuming. Sending emails with Django-SES might be attractive to you if:

* You don't want to maintain mail servers. ...

Example:
```python
from django_ses.signals import bounce_received
from django.dispatch import receiver

@receiver(bounce_received)
def bounce_handler(sender, mail_obj, bounce_obj, raw_message, *args, **kwargs):
...

</details>

### django-waffle

A feature flipper for Django.

`pip install django-waffle` · installs (wheel) · licence: BSD License · rank 3271 · last release 2025-06-12 · [PyPI](https://pypi.org/project/django-waffle/)

<details><summary>README extract</summary>

Django Waffle is (yet another) feature flipper for Django. You can
define the conditions for which a flag should be active, and use it in
a number of ways.

:Code:
:License: BSD; see LICENSE file
:Issues:
:Documentation:

</details>

### descope

Descope Python SDK

`pip install descope` · installs (wheel) · licence: MIT · rank 3285 · last release 2026-11-05 · [PyPI](https://pypi.org/project/descope/) · [docs](https://docs.descope.com) · [source](https://github.com/descope/python-sdk)

<details><summary>README extract</summary>

The Descope SDK for python provides convenient access to the Descope user management and authentication API
for a backend written in python. You can read more on the Descope Website.

The SDK supports Python 3.9 and above.

Example:
```python
from descope import DescopeClient

# Initialized after setting the DESCOPE_PROJECT_ID and DESCOPE_AUTH_MANAGEMENT_KEY env vars
descope_client = DescopeClient()

#  Or directly (w/ optional base URL)
descope_client = DescopeClient(
    project_id="<Project ID>",
    auth_management_key="<Descope Project Management Key>,
...
```

...

</details>

### together

The official Python library for the together API

`pip install together` · installs (wheel) · licence: Apache Software License · rank 3291 · last release 2026-11-04 · [PyPI](https://pypi.org/project/together/) · [docs](https://docs.together.ai/) · [source](https://github.com/togethercomputer/together-py)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Together Python library provides convenient access to the Together REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from together import Together

client = Together(
    api_key=os.environ.get("TOGETHER_API_KEY"),  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test!",
        }
    ],
...
```

...

</details>

### pep8-naming

Check PEP-8 naming conventions, plugin for flake8

`pip install pep8-naming` · installs (wheel) · licence: MIT License · rank 3302 · last release 2025-05-05 · [PyPI](https://pypi.org/project/pep8-naming/) · [source](https://github.com/PyCQA/pep8-naming)

<details><summary>README extract</summary>

Check your code against PEP 8
naming conventions.

This module provides a plugin for `flake8`, the Python code checker.

(It replaces the plugin `flint-naming` for the `flint` checker.)

Sections: PEP 8 Naming Conventions, Plugin for Flake8, Error Codes, Options, FAQ

</details>

### ably

Python REST and Realtime client library SDK for Ably realtime messaging service

`pip install ably` · installs (wheel) · licence: Apache Software License · rank 3305 · last release 2026-09-23 · [PyPI](https://pypi.org/project/ably/) · [source](https://github.com/ably/ably-pubsub-python)

<details><summary>README extract</summary>

A Python client library for Ably Realtime messaging.

You can install this package by using the pip tool and installing:

 pip install ably

- Sign up for Ably at
- Get usage examples at
- Visit for a complete API reference and more examples

Sections: Official Ably Bindings for Python, Setup, Using Ably for Python

</details>

### Keras-Preprocessing

Easy data preprocessing and data augmentation for deep learning models

`pip install Keras-Preprocessing` · installs (wheel) · licence: MIT License · rank 3312 · last release 2020-05-14 · [PyPI](https://pypi.org/project/Keras-Preprocessing/)

<details><summary>README extract</summary>

Keras Preprocessing is the data preprocessing
and data augmentation module of the Keras deep learning library.
It provides utilities for working with image data, text data,
and sequence data.

Read the documentation at:

Keras Preprocessing may be imported directly
from an up-to-date installation of Keras: ...

Example:
```python
from keras import preprocessing
```

</details>

### SPARQLWrapper

SPARQL Endpoint interface to Python

`pip install SPARQLWrapper` · installs (wheel) · licence: W3C License · rank 3328 · last release 2022-03-13 · [PyPI](https://pypi.org/project/SPARQLWrapper/) · [docs](https://sparqlwrapper.readthedocs.io) · [source](https://github.com/RDFLib/sparqlwrapper)

<details><summary>README extract</summary>

This is a wrapper around a SPARQL service. It helps in creating the query URI and, possibly, convert the result into a more manageable format.

</details>

### skypilot

SkyPilot: Manage all your AI compute.

`pip install skypilot` · installs (wheel) · licence: Apache Software License · rank 3333 · last release 2026-10-28 · [PyPI](https://pypi.org/project/skypilot/) · [docs](https://docs.skypilot.co/)

<details><summary>README extract</summary>

SkyPilot is a system to run, manage, and scale AI workloads on any AI infrastructure.

SkyPilot gives AI teams a simple interface to run jobs on any infra.
Infra teams get a unified control plane to manage any AI compute — with advanced scheduling, scaling, and orchestration.

:fire: *News* :fire: ...

Features:
SkyPilot is easy to use for AI users:
- Quickly spin up compute on your own infra
- Environment and job as code — simple and portable
- Easy job management: queue, run, and auto-recover many jobs ...

Sections: Manage all your AI compute, Overview, Getting started, Benefits of SkyPilot on Kubernetes, SkyPilot in 1 minute, Runnable examples, Learn more, Questions and feedback

</details>

### pyobjc-core

Python<->ObjC Interoperability Module

`pip install pyobjc-core` · installs from source (sdist only) · licence: MIT · rank 3337 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-core/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

PyObjC is a bridge between Python and Objective-C. It allows full
featured Cocoa applications to be written in pure Python. It is also
easy to use other frameworks containing Objective-C class libraries
from Python and to mix in Objective-C, C and C++ source.

Python is a highly dynamic programming language with a shallow learning
curve. ...

</details>

### tink

A multi-language, cross-platform library that provides cryptographic APIs that are secure, easy to use correctly, and hard(er) to misuse.

`pip install tink` · installs (wheel) · licence: Apache 2.0 · rank 3351 · last release 2026-08-13 · [PyPI](https://pypi.org/project/tink/)

<details><summary>README extract</summary>

<!-- GCP Ubuntu --->

<!-- GCP Ubuntu (aarch64) --->

<!-- GCP Windows --->

<!-- MacOS --->

Test | GCP Ubuntu | GCP Ubuntu (aarch64) | MacOS | GCP Windows

Bazel | [](#) | N/A | [](#) | [](#)
Bazel (with KMS) | [](#) | N/A | [](#) | N/A
Pip | [](#) | N/A | [](#) | [](#)
Pip (with KMS) | [](#) | N/A | [](#) | N/A
Bdist (Create + Test) | [](#) | ...

Sections: Tink Python, Contact and mailing list

</details>

### logging-azure-rest

A python threadded logging handler and service extension for Azure Log Workspace OMS REST API.

`pip install logging-azure-rest` · installs from source (sdist only) · licence: MIT License · rank 3355 · last release 2021-06-14 · [PyPI](https://pypi.org/project/logging-azure-rest/)

<details><summary>README extract</summary>

This package provides an asynchronous solution for uploading application logs to an Azure Log Workspace using their
provided REST API, all supplied as a handler and service extension for python builtin `logging` module. ...

Sections: Python Logging Azure Workspace OMS Extension, Usage, Package Configuration, Logging Configuration, Recommendations, Set an appropriate log level minimum, Set a clear formatter for messages, Useful links, Package requirements

</details>

### kopf

Kubernetes Operator Pythonic Framework (Kopf)

`pip install kopf` · installs (wheel) · licence: MIT · rank 3358 · last release 2026-10-23 · [PyPI](https://pypi.org/project/kopf/) · [docs](https://docs.kopf.dev/) · [source](https://github.com/nolar/kopf)

<details><summary>README extract</summary>

Kopf — Kubernetes Operator Pythonic Framework — is a framework and a library
to make Kubernetes operator development easier, in just a few lines of Python code.

The main goal is to bring the Domain-Driven Design to the infrastructure level,
with Kubernetes being an orchestrator/database of the domain objects (custom resources),
and the operators ...

Features:
* A full-featured operator in just 2 files: a `Dockerfile` + a Python file (*).
 * Handling functions registered via decorators with a declarative approach.
 * No infrastructure boilerplate code for K8s API communication. ...

Example:
```python
import kopf

@kopf.on.create('kopfexamples')
def create_fn(spec, name, meta, status, **kwargs):
    print(f"And here we are! Created {name} with spec: {spec}")
```

...

</details>

### pyobjc-framework-Cocoa

Wrappers for the Cocoa frameworks on macOS

`pip install pyobjc-framework-Cocoa` · installs from source (sdist only) · licence: MIT · rank 3369 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Cocoa/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the core Cocoa frameworks: CoreFoundation, Foundation and
AppKit.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use these frameworks and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation ...

</details>

### mutf8

Fast MUTF-8 encoder & decoder

`pip install mutf8` · installs (wheel) · licence: MIT · rank 3393 · last release 2026-07-11 · [PyPI](https://pypi.org/project/mutf8/) · [source](https://github.com/TkTech/mutf8)

<details><summary>README extract</summary>

This package contains simple pure-python as well as C encoders and decoders for
the MUTF-8 character encoding.

These days, you'll most likely encounter MUTF-8 when working on files or
protocols related to the JVM. ...

Example:
```python
from mutf8 import encode_modified_utf8, decode_modified_utf8

unicode = decode_modified_utf8(byte_like_object)
bytes = encode_modified_utf8(unicode)
```

Sections: mutf-8, Usage, Benchmarks, MUTF-8 Decoding, MUTF-8 Encoding, C Extension

</details>

### treelib

A Python implementation of tree structure.

`pip install treelib` · installs (wheel) · licence: Apache Software License · rank 3397 · last release 2025-06-29 · [PyPI](https://pypi.org/project/treelib/) · [source](https://github.com/caesar0301/treelib)

<details><summary>README extract</summary>

Tree implementation in python: simple for you to use.

Sections: treelib, Quick Start, Documentation

</details>

### typed-settings

Typed settings based on attrs classes

`pip install typed-settings` · installs (wheel) · licence: MIT · rank 3409 · last release 2026-11-05 · [PyPI](https://pypi.org/project/typed-settings/) · [docs](https://typed-settings.readthedocs.io) · [source](https://gitlab.com/sscherfke/typed-settings)

<details><summary>README extract</summary>

Load and merge settings from multiple different sources and present them in a structured, typed, and validated way!

Features:
There are many different config file formats and libraries.
Many of them have a narrow scope, don't integrate well with other libs, or lack in typing support. ...

Example:
```python
# example.py
import attrs
import typed_settings as ts

@attrs.frozen
class Settings:
    option: str

settings = ts.load(cls=Settings, appname="example")
print(settings)
```

Sections: Typed Settings, Why?, What can it be used for?, What does it do?, Examples, Hello, World!, with env. vars., Nested classes and config files, Configurable settings loaders, Command Line Interfaces, Argparse, Click, Project Links

</details>

### py-ubjson

Universal Binary JSON encoder/decoder

`pip install py-ubjson` · installs from source (sdist only) · licence: Apache Software License · rank 3414 · last release 2020-04-18 · [PyPI](https://pypi.org/project/py-ubjson/)

<details><summary>README extract</summary>

Features:
This is a Python v3.2+ (and 2.7+) Universal Binary JSON encoder/decoder based on the draft-12 specification.

Example:
```python
import ubjson

encoded = ubjson.dumpb({u'a': 1})

decoded = ubjson.loadb(encoded)
```

Sections: Overview, Usage, Documentation, Command-line utility, Tests, Static, Unit, Limitations, Why?

</details>

### python-editor

Programmatically open an editor, capture the result.

`pip install python-editor` · installs (wheel) · licence: Apache Software License · rank 3417 · last release 2019-02-01 · [PyPI](https://pypi.org/project/python-editor/)

<details><summary>README extract</summary>

`python-editor` is a library that provides the `editor` module for programmatically
interfacing with your system's $EDITOR.

Examples

Opens an editor, prefilled with the contents, `# Enter commit message here`.
When the editor is closed, returns the contents (bytes) in variable `commit_msg`. ...

Example:
```python
import editor
commit_msg = editor.edit(contents=b"# Enter commit message here")
```

</details>

### ajsonrpc

Async JSON-RPC 2.0 protocol + server powered by asyncio

`pip install ajsonrpc` · installs (wheel) · licence: MIT License · rank 3425 · last release 2021-07-21 · [PyPI](https://pypi.org/project/ajsonrpc/) · [docs](https://ajsonrpc.readthedocs.io) · [source](https://github.com/pavlov99/ajsonrpc)

<details><summary>README extract</summary>

Example:
```python
# init
d = Dispatcher({"sum": lambda a, b: a + b})

# set item
d["max"] = lambda a, b: max(a, b)

# function decorator
@d.add_function
def add(x, y):
    return x + y

# Add class or object
class Math:
    def sum(self, a, b):
        return a + b

    def diff(self, a, b):
        return a - b

d.add_class(Math)
d.add_object(Math())
...
```

Sections: Quick Start, Core Module, Dispatcher, Manager, Vanilla Server (Demo), Backends

</details>

### lithic

The official Python library for the lithic API

`pip install lithic` · installs (wheel) · licence: Apache Software License · rank 3434 · last release 2026-10-29 · [PyPI](https://pypi.org/project/lithic/) · [source](https://github.com/lithic-com/lithic-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Lithic Python library provides convenient access to the Lithic REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx. ...

Example:
```python
import os
from lithic import Lithic

client = Lithic(
    api_key=os.environ.get("LITHIC_API_KEY"),  # This is the default and can be omitted
    # defaults to "production".
    environment="sandbox",
)

card = client.cards.create(
    type="SINGLE_USE",
)
print(card.token)
```

...

</details>

### django-adminplus

Add new pages to the Django admin.

`pip install django-adminplus` · installs (wheel) · licence: BSD License · rank 3438 · last release 2023-12-05 · [PyPI](https://pypi.org/project/django-adminplus/)

<details><summary>README extract</summary>

AdminPlus aims to be the smallest possible extension to the excellent
Django admin component that lets you add admin views that are not tied to
models.

There are packages out there, like Nexus
and django-admin-tools that
replace the entire admin. ...

Example:
```python
# someapp/admin.py
# Assuming you've replaced django.contrib.admin.site as above.
from django.contrib import admin

def my_view(request, *args, **kwargs):
    pass
admin.site.register_view('somepath', view=my_view)

# And of course, this still works:
from someapp.models import MyModel
admin.site.register(MyModel)
```

Sections: Django AdminPlus, Using AdminPlus

</details>

### statshog

A simple statsd client.

`pip install statshog` · installs (wheel) · licence: MIT License · rank 3439 · last release 2021-05-07 · [PyPI](https://pypi.org/project/statshog/)

<details><summary>README extract</summary>

A python client for Etsy's
StatsD server and
InfluxDB's
Telegraf StatsD server.

Code: <

License: MIT; see LICENSE file

Issues: <

Documentation: <

Example:
```python
import statshog
statsd = statshog.StatsClient(host='localhost', port=8125)
statsd.incr('foo')  # Increment the 'foo' counter.
statsd.timing('stats.timed', 320)  # Record a 320ms 'stats.timed'
```

Sections: A Python statsd client, Usage, Quick usage, Using with telegraf/influxdb, Usage with django

</details>

### path

A module wrapper for os.path

`pip install path` · installs (wheel) · licence: MIT · rank 3443 · last release 2025-07-27 · [PyPI](https://pypi.org/project/path/) · [source](https://github.com/jaraco/path)

<details><summary>README extract</summary>

`path` (aka path pie, formerly `path.py`) implements path
objects as first-class entities, allowing common operations on
files to be invoked on those path objects directly. For example:

Path pie is hosted at Github.

Find the documentation here.

Example:
```python
from path import Path

d = Path("/home/guido/bin")
for f in d.files("*.py"):
    f.chmod(0o755)

# Globbing
for f in d.files("*.py"):
    f.chmod("u+rwx")

# Changing the working directory:
with Path("somewhere"):
    # cwd in now `somewhere`
    ...

# Concatenate paths with /
foo_txt = Path("bar") / "foo.txt"
```

Sections: Guides and Testimonials, Advantages, Origins, For Enterprise

</details>

### posthog-hogland

Python client for hogland — Firecracker-backed sandboxes (hogboxes)

`pip install posthog-hogland` · installs (wheel) · licence: MIT License · rank 3455 · last release 2026-10-16 · [PyPI](https://pypi.org/project/posthog-hogland/) · [source](https://github.com/PostHog/hogland)

<details><summary>README extract</summary>

Python client for hogland's
Firecracker-backed sandboxes (hogboxes).

The SDK exposes the user-facing slice of the hogplane API
(`/v1/hogboxes/*`, `/v1/limits`, `/v1/me`, plus snapshots and devboxes)
as a small, typed surface designed to be a viable backend for PostHog's
internal `SandboxBase` interface — see `examples/sandbox_base_adapter.py`.

Example:
```python
from hogland import Hogland

client = Hogland()  # reads HOG_TOKEN + HOG_HOST from env (same vars as the CLI)

# No ssh_public_key given → the box defaults to access_type="none":
# everything below goes through the exec/files/proxy API. Pass
# ssh_public_key=... (+ access_type="ssh-public") if you want a shell too.
...
```

...

</details>

### evdev

Bindings to the Linux input handling subsystem

`pip install evdev` · installs from source (sdist only) · licence: BSD-3-Clause · rank 3479 · last release 2026-08-23 · [PyPI](https://pypi.org/project/evdev/)

<details><summary>README extract</summary>

This package provides bindings to the generic input event interface in Linux.
The *evdev* interface serves the purpose of passing events generated in the
kernel directly to userspace through character devices that are typically
located in `/dev/input/`.

This package also comes with bindings to *uinput*, the userspace input
subsystem. ...

</details>

### splunk-sdk

Splunk Software Development Kit for Python

`pip install splunk-sdk` · installs (wheel) · licence: Apache-2.0 · rank 3491 · last release 2026-09-09 · [PyPI](https://pypi.org/project/splunk-sdk/) · [docs](https://docs.splunk.com/Documentation/PythonSDK) · [source](https://github.com/splunk/splunk-sdk-python.git)

<details><summary>README extract</summary>

The Splunk Enterprise Software Development Kit (SDK) for Python is intended to be the primary way for developers to communicate with the Splunk platform's REST API.

You may be asking:

- What are Splunk Apps?
- What can Splunk Apps do?
- How do I write Splunk Apps?
- Where does the SDK fit in all this? ...

Example:
```python
sys.path.insert(0, os.path.join(os.path.dirname(file), "lib"))
```

Sections: Splunk Enterprise SDK for Python, Getting started, Requirements, Including external dependencies in your App, Packaging your App, Using SDK in Splunk Apps, Using AI in Splunk Apps, Connecting to a Splunk Enterprise instance, Using a username/password combo, Using a bearer token, Using a session key, Creating Custom Search Commands, Accessing instance metadata in CSCs, Field retention in CSC

</details>

### colour

converts and manipulates various color representation (HSL, RVB, web, X11, ...)

`pip install colour` · installs (wheel) · licence: BSD License · rank 3505 · last release 2017-11-19 · [PyPI](https://pypi.org/project/colour/)

<details><summary>README extract</summary>

Converts and manipulates common color representation (RGB, HSL, web, ...)

Features:
- Damn simple and pythonic way to manipulate color representation (see
 examples below)

- Full conversion between RGB, HSL, 6-digit hex, 3-digit hex, human color ...

Example:
```python
>>> foo = object()
>>> bar = object()

>>> Color(pick_for=foo)  # doctest: +ELLIPSIS
<Color ...>
>>> Color(pick_for=foo) == Color(pick_for=foo)
True
>>> Color(pick_for=foo) == Color(pick_for=bar)
False
```

Sections: Colour, Feature, Usage, Instantiation, Reading values, Modifying color objects, Ranges of colors, Color comparison, Sane default, Customization, Equality to non-Colour objects, Picking arbitrary color for a python object, Basic Usage, Advanced Usage

</details>

### cli-exit-tools

functions to exit an cli application properly

`pip install cli-exit-tools` · installs (wheel) · licence: MIT License · rank 3508 · last release 2024-10-02 · [PyPI](https://pypi.org/project/cli-exit-tools/) · [docs](https://github.com/bitranox/cli_exit_tools/blob/master/README.rst) · [source](https://github.com/bitranox/cli_exit_tools.git)

<details><summary>README extract</summary>

Version v1.2.7 as of 2024-10-02 see Changelog

small toolset to properly exit a cli application:

- print the traceback information (can be set with commandline option)
- get a proper exit code from the Exception
- flush the streams, to make sure output is written in proper order
- demo how to integrate into Your cli module (see usage) ...

Example:
```python
# STDLIB
import platform
import signal
import sys
from typing import Any
from typing import Callable
from typing import Optional
from typing import Union
from types import FrameType

# EXT
import click

# CONSTANTS
CLICK_CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

try:
    from . import initconf_
    from . import cli_exit_tools
...
```

...

</details>

### warcio

Streaming WARC (and ARC) IO library

`pip install warcio` · installs (wheel) · licence: Apache Software License · rank 3524 · last release 2026-10-28 · [PyPI](https://pypi.org/project/warcio/)

<details><summary>README extract</summary>

This library provides a fast, standalone way to read and write WARC
Format commonly used in
web archives. Python 3.7+ (minimally only needing
six as an external dependency)

warcio supports reading and writing of WARC files compliant with both the WARC 1.0
and WARC 1.1 ISO standards. ...

Example:
```python
from warcio.capture_http import capture_http
import requests  # requests must be imported after capture_http

with capture_http('example.warc.gz'):
    requests.get('
```

...

</details>

### pydantic-ai-skills

Remote skill registries and bundled-file execution for Pydantic AI Agent Skills

`pip install pydantic-ai-skills` · installs (wheel) · licence: MIT · rank 3553 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pydantic-ai-skills/) · [source](https://github.com/dougtrajano/pydantic-ai-skills)

<details><summary>README extract</summary>

Remote skill registries and bundled-file execution for Agent Skills
in Pydantic AI.

Agent Skills are modular packages of instructions, resources, and scripts that teach an agent to
handle a specialized task. ...

Example:
```python
from pydantic_ai import Agent
from pydantic_ai_skills import SkillsCapability

agent = Agent(
    model='gateway/openai:gpt-5.2',
    instructions='You are a helpful research assistant.',
    capabilities=[SkillsCapability('./skills')],
)

result = await agent.run('What are the last 3 papers on arXiv about machine learning?')
print(result.output)
```

Sections: pydantic-ai-skills, How This Relates to `pydantic-ai-harness`, Quick Start, Anatomy of a Skill, Beyond the Filesystem, Related Resources

</details>

### flask-restx

Fully featured framework for fast, easy and documented API development with Flask

`pip install flask-restx` · installs (wheel) · licence: BSD License · rank 3557 · last release 2025-09-23 · [PyPI](https://pypi.org/project/flask-restx/)

<details><summary>README extract</summary>

Flask-RESTX is a community driven fork of Flask-RESTPlus.

Flask-RESTX is an extension for Flask that adds support for quickly building REST APIs.
Flask-RESTX encourages best practices with minimal setup.
If you are familiar with Flask, Flask-RESTX should be easy to pick up. ...

Example:
```python
from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(name)
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
...
```

Sections: Flask RESTX, Compatibility, On Flask Compatibility, Quick start, Documentation

</details>

### complexipy

An extremely fast Python library to calculate the cognitive complexity of Python files, written in Rust.

`pip install complexipy` · installs (wheel) · licence: MIT · rank 3568 · last release 2026-10-27 · [PyPI](https://pypi.org/project/complexipy/) · [docs](https://complexipy.com/) · [source](https://github.com/rohaquinlop/complexipy)

<details><summary>README extract</summary>

Blazingly fast cognitive complexity analysis for Python, written in Rust.

 Installation •
 Quick Start •
 Integrations •
 Learn More •
 Documentation •
 Changelog •
 Complexipy Teams

> Cognitive complexity measures how hard code is to understand by humans, not machines. ...

Example:
```python
from complexipy import file_complexity

# Analyze a file
result = file_complexity("app.py", check_script=True)
print(f"File complexity: {result.complexity}")

for func in result.functions:
    print(f"{func.name}: {func.complexity}")
```

Sections: complexipy, What is Cognitive Complexity?, Common Questions, Quick Start, Command Line, Python API, Integrations, Learn More

</details>

### fireworks-ai

The official Python library for the fireworks API

`pip install fireworks-ai` · installs (wheel) · licence: Apache Software License · rank 3569 · last release 2026-11-05 · [PyPI](https://pypi.org/project/fireworks-ai/) · [source](https://github.com/fw-ai-external/python-sdk)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Fireworks AI Python SDK library provides convenient access to the Fireworks REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients. ...

Example:
```python
import os
from fireworks import Fireworks

client = Fireworks(
    api_key=os.environ.get("FIREWORKS_API_KEY"),  # This is the default and can be omitted
)

completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How do LLMs work?",
        }
    ],
...
```

...

</details>

### backports-datetime-fromisoformat

Backport of Python 3.11's datetime.fromisoformat

`pip install backports-datetime-fromisoformat` · installs from source (sdist only) · licence: MIT License · rank 3571 · last release 2024-12-28 · [PyPI](https://pypi.org/project/backports-datetime-fromisoformat/) · [docs](https://github.com/movermeyer/backports.datetime_fromisoformat) · [source](https://github.com/movermeyer/backports.datetime_fromisoformat)

<details><summary>README extract</summary>

A backport of Python 3.11's `datetime.fromisoformat` methods to earlier versions of Python 3.
Tested against Python 3.6, 3.7, 3.8, 3.9, 3.10 and 3.11

Example:
```python
>>> from datetime import date, datetime, time
>>> from backports.datetime_fromisoformat import MonkeyPatch
>>> MonkeyPatch.patch_fromisoformat()

>>> datetime.fromisoformat("2014-01-09T21:48:00-05:30")
datetime.datetime(2014, 1, 9, 21, 48, tzinfo=-05:30)

>>> date.fromisoformat("2014-01-09")
datetime.date(2014, 1, 9)

...
```

Sections: backports.datetime_fromisoformat, Version 2 changes, Quick Start, Explanation, Usage in Python 3.11+, Goal / Project Scope

</details>

### ansible-runner

"Consistent Ansible Python API and CLI with container and process isolation runtime capabilities"

`pip install ansible-runner` · installs (wheel) · licence: Apache Software License · rank 3575 · last release 2026-03-16 · [PyPI](https://pypi.org/project/ansible-runner/) · [source](https://github.com/ansible/ansible-runner)

<details><summary>README extract</summary>

Ansible Runner is a tool and Python library that helps when interfacing with Ansible directly or as part of another system. Ansible Runner works as a standalone tool, a container image interface, or a Python module that can be imported. The goal is to provide a stable and consistent interface abstraction to Ansible. ...

</details>

### decopatch

Create decorators easily in python.

`pip install decopatch` · installs (wheel) · licence: BSD License · rank 3591 · last release 2022-03-01 · [PyPI](https://pypi.org/project/decopatch/)

<details><summary>README extract</summary>

*python decorators made easy.*

The documentation for users is available here:

A readme for developers is available here:

</details>

### spandrel

Give your project support for a variety of PyTorch model architectures, including auto-detecting model architecture from just .pth files. spandrel gives you arch support.

`pip install spandrel` · installs (wheel) · licence: MIT License · rank 3594 · last release 2026-02-21 · [PyPI](https://pypi.org/project/spandrel/)

<details><summary>README extract</summary>

Spandrel is a library for loading and running pre-trained PyTorch models. It automatically detects the model architecture and hyperparameters from model files, and provides a unified interface for running models. ...

Example:
```python
from spandrel import ImageModelDescriptor, ModelLoader
import torch

# load a model from disk
model = ModelLoader().load_from_file(r"path/to/model.pth")

# make sure it's an image to image model
assert isinstance(model, ImageModelDescriptor)

# send it to the GPU and put it in inference mode
model.cuda().eval()

# use the model
...
```

Sections: Spandrel, Basic Usage, More architectures, Single Image Super Resolution, Face Restoration, Inpainting, Denoising, DeJPEG, Colorization, Dehazing, Low-light Enhancement, Used By

</details>

### legacy-api-wrap

Legacy API wrapper.

`pip install legacy-api-wrap` · installs (wheel) · licence: MPL-2.0 · rank 3602 · last release 2025-11-03 · [PyPI](https://pypi.org/project/legacy-api-wrap/) · [source](https://github.com/flying-sheep/legacy-api-wrap)

<details><summary>README extract</summary>

This module defines a decorator to wrap legacy APIs.
The primary use case is APIs defined before keyword-only parameters existed.

>>> from legacy_api_wrap import legacy_api

We have a function with many positional parameters lying around:

>>> def fn(a, b=None, d=1, c=2):
... return c, d, e ...

</details>

### argh

Plain Python functions as CLI commands without boilerplate

`pip install argh` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 3604 · last release 2024-07-13 · [PyPI](https://pypi.org/project/argh/) · [docs](https://argh.readthedocs.io/en/latest)

_README extract left out: share-alike licence._

### stdlib-list

A list of Python Standard Libraries (2.7 through 3.14).

`pip install stdlib-list` · installs (wheel) · licence: MIT License · rank 3616 · last release 2025-10-24 · [PyPI](https://pypi.org/project/stdlib-list/) · [docs](https://pypi.github.io/stdlib-list/) · [source](https://github.com/pypi/stdlib-list)

<details><summary>README extract</summary>

This package includes lists of all of the standard libraries for Python 2.6
through 3.14.

IMPORTANT: If you're on Python 3.10 or newer, you probably don't need this library.
See `sys.stdlib_module_names`
and `sys.builtin_module_names`
for similar functionality.

Example:
```python
>>> from stdlib_list import stdlib_list
>>> libraries = stdlib_list("2.7")
>>> libraries[:10]
['AL', 'BaseHTTPServer', 'Bastion', 'CGIHTTPServer', 'ColorPicker', 'ConfigParser', 'Cookie', 'DEVICE', 'DocXMLRPCServer', 'EasyDialogs']
```

Sections: stdlib-list, Usage

</details>

### cmd2

cmd2 - quickly build feature-rich and user-friendly interactive command line applications in Python

`pip install cmd2` · installs (wheel) · licence: MIT · rank 3623 · last release 2026-11-03 · [PyPI](https://pypi.org/project/cmd2/)

<details><summary>README extract</summary>

Quick start •
 Why cmd2? •
 Installation •
 Documentation •
 Projects using cmd2

`cmd2` makes it quick to build powerful, polished command-line applications and REPLs in Python. ...

Example:
```python
from typing import Annotated

import cmd2
from cmd2.annotated import Argument, Option

class App(cmd2.Cmd):
    """A small interactive application."""

    @cmd2.with_annotated
    def do_greet(
        self,
        name: Annotated[str, Argument(help_text="person to greet")],
...
```

Sections: cmd2: build feature-rich command-line apps in Python, Quick start, Why cmd2?, Build more with less code, Give users a capable interface from day one, Grow from exploration to automation, Documentation, Tutorials, Found a bug?, Projects using cmd2

</details>

### django-widget-tweaks

Tweak the form field rendering in templates, not in python-level form definitions.

`pip install django-widget-tweaks` · installs (wheel) · licence: MIT License · rank 3624 · last release 2026-01-02 · [PyPI](https://pypi.org/project/django-widget-tweaks/)

<details><summary>README extract</summary>

Tweak the form field rendering in templates, not in python-level
form definitions. Altering CSS classes and HTML attributes is supported.

That should be enough for designers to customize field presentation (using
CSS and unobtrusive javascript) without touching python code.

License is MIT.

Sections: django-widget-tweaks, Usage, render_field, attr, add_class, set_data, append_attr, remove_attr, add_label_class, add_error_class, add_error_attr, add_required_class, field_type and widget_type, Fields with multiple widgets

</details>

### orb-billing

The official Python library for the orb API

`pip install orb-billing` · installs (wheel) · licence: Apache Software License · rank 3636 · last release 2026-11-07 · [PyPI](https://pypi.org/project/orb-billing/) · [source](https://github.com/orbcorp/orb-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Orb Python library provides convenient access to the Orb REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

The REST API documentation can be found on docs.withorb.com. ...

Example:
```python
import os
from orb import Orb

client = Orb(
    api_key=os.environ.get("ORB_API_KEY"),  # This is the default and can be omitted
)

customer = client.customers.create(
    email="example-customer@withorb.com",
    name="My Customer",
)
print(customer.id)
```

...

</details>

### wrapt-timeout-decorator

The better timout decorator

`pip install wrapt-timeout-decorator` · installs (wheel) · licence: MIT License · rank 3641 · last release 2024-02-28 · [PyPI](https://pypi.org/project/wrapt-timeout-decorator/) · [docs](https://github.com/bitranox/wrapt_timeout_decorator/blob/master/README.rst) · [source](https://github.com/bitranox/wrapt_timeout_decorator.git)

<details><summary>README extract</summary>

Version v1.5.1 as of 2024-02-28 see Changelog

There are several timeout decorators available, but the one mentioned here
focuses on ensuring correctness when used with classes, methods, class methods,
static methods, etc. It also preserves traceback information for PyCharm debugging. ...

Features:
Subprocesses ares utilized by default to implement timeout functionality. This involves forking or spawning subprocesses, each with its own set of
considerations and caveats.

Example:
```python
import time
from wrapt_timeout_decorator import *

@timeout(5)
def mytest(message):
    # this example does NOT work on windows, please check the section
    # "use with Windows" in the README.rst
    print(message)
    for i in range(1,10):
        time.sleep(1)
...

</details>

### sshconf

Lightweight SSH config library.

`pip install sshconf` · installs (wheel) · licence: MIT License · rank 3644 · last release 2024-06-29 · [PyPI](https://pypi.org/project/sshconf/)

<details><summary>README extract</summary>

Sshconf is a library for reading and modifying your ssh/config file in a non-intrusive way, meaning
your file should look more or less the same after modifications. Idea is to keep it simple,
so you can modify it for your needs.

Read more about ssh config files here: Create SSH config file on Linux

Installation and usage ...

Example:
```python
from sshconf import read_ssh_config, empty_ssh_config_file
from os.path import expanduser

c = read_ssh_config(expanduser("~/.ssh/config"))
print("hosts", c.hosts())

# assuming you have a host "svu"
print("svu host", c.host("svu"))  # print the settings
c.set("svu", Hostname="ssh.svu.local", Port=1234)
print("svu host now", c.host("svu"))
...
```

</details>

### standard-sunau

Standard library sunau redistribution. "dead battery".

`pip install standard-sunau` · installs (wheel) · licence: Python Software Foundation License · rank 3656 · last release 2024-10-30 · [PyPI](https://pypi.org/project/standard-sunau/)

<details><summary>README extract</summary>

Python is moving forward! Python finally started to remove dead batteries.
For more information, see PEP 594.

If your project depends on a module that has been removed from the standard,
here is the redistribution of the dead batteries.

</details>

### glob2

Version of the glob module that can capture patterns and supports recursive wildcards

`pip install glob2` · installs from source (sdist only) · licence: BSD License · rank 3659 · last release 2019-06-10 · [PyPI](https://pypi.org/project/glob2/)

### pytest-flask

A set of py.test fixtures to test Flask applications.

`pip install pytest-flask` · installs (wheel) · licence: MIT License · rank 3663 · last release 2023-10-23 · [PyPI](https://pypi.org/project/pytest-flask/) · [source](https://github.com/pytest-dev/pytest-flask)

<details><summary>README extract</summary>

An extension of pytest test runner which
provides a set of useful tools to simplify testing and development
of the Flask extensions and applications.

To view a more detailed list of extension features and examples go to
the PyPI overview page or
package documentation. ...

Example:
```python
from flask import Flask

def create_app():
   # create a minimal app
   app = Flask(name)

   # simple hello world view
   @app.route('/hello')
   def hello():
      return 'Hello, World!'

   return app
```

Sections: pytest-flask, How to start?, 1.3.0 (2023-10-23), 1.2.1, 1.2.0 (2021-02-26), 1.1.0 (2020-11-08), 1.0.0 (2020-03-03), 0.15.1 (2020-02-03), 0.15.0 (2019-05-13), 0.14.0 (2018-10-15), 0.13.0 (2018-09-29), 0.12.0 (2018-09-06), 0.11.0 (compared to 0.10.0), 0.10.0 (compared to 0.9.0)

</details>

### zhon

Zhon provides constants used in Chinese text processing.

`pip install zhon` · installs (wheel) · licence: MIT License · rank 3688 · last release 2024-11-20 · [PyPI](https://pypi.org/project/zhon/) · [docs](https://tsroten.github.io/zhon) · [source](https://github.com/tsroten/zhon)

<details><summary>README extract</summary>

Zhon is a Python library that provides constants commonly used in Chinese text
processing.

* Free software: MIT license

Zhon's constants can be used in Chinese text processing, for example:

 .. code:: python

 >>> re.findall('[{}]'.format(zhon.hanzi.characters), 'I broke a plate: 我打破了一个盘子.')
 ['我', '打', '破', '了', '一', '个', '盘', '子']

 .. ...

Features:
Zhon includes the following commonly-used constants:

* CJK characters and radicals
* Chinese punctuation marks
* Chinese sentence regular expression pattern
* Pinyin vowels, consonants, lowercase, uppercase, and punctuation
* Pinyin syllable, word, ...

Sections: Zhon, About, Features, Getting Started

</details>

### kafka-python-ng

Pure Python client for Apache Kafka

`pip install kafka-python-ng` · installs (wheel) · licence: Apache Software License · rank 3691 · last release 2024-10-02 · [PyPI](https://pypi.org/project/kafka-python-ng/)

<details><summary>README extract</summary>

DUE TO ISSUES WITH RELEASES, IT IS SUGGESTED TO USE FOR THE TIME BEING

Python client for the Apache Kafka distributed stream processing system.
kafka-python-ng is designed to function much like the official java client, with a
sprinkling of pythonic interfaces (e.g., consumer iterators). ...

Example:
```python
# join a consumer group for dynamic partition assignment and offset commits
from kafka import KafkaConsumer
consumer = KafkaConsumer('my_favorite_topic', group_id='my_favorite_group')
# or as a static member with a fixed group member name
# consumer = KafkaConsumer('my_favorite_topic', group_id='my_favorite_group',
...
```

Sections: Kafka Python client, KafkaConsumer, KafkaProducer, Thread safety, Compression, Optimized CRC32 Validation

</details>

### davey

A Discord Audio & Video End-to-End Encryption (DAVE) Protocol implementation

`pip install davey` · installs (wheel) · licence: MIT License · rank 3700 · last release 2026-11-02 · [PyPI](https://pypi.org/project/davey/) · [source](https://github.com/Snazzah/davey)

<details><summary>README extract</summary>

A Discord Audio & Video End-to-End Encryption (DAVE) Protocol implementation using OpenMLS.

> Proper usage documentation does not exist yet.

</details>

### lief

Library to instrument executable formats

`pip install lief` · installs (wheel) · licence: Apache License 2.0 · rank 3711 · last release 2026-07-12 · [PyPI](https://pypi.org/project/lief/) · [docs](https://lief-project.github.io/doc/latest/) · [source](https://github.com/lief-project/LIEF)

<details><summary>README extract</summary>

The purpose of this project is to provide a cross platform library that can parse, modify and
abstract ELF, PE and MachO formats.

Main features:

 * Parsing: LIEF can parse ELF, PE, MachO, OAT, DEX, VDEX, ART and provides an user-friendly API to access to format internals. ...

Example:
```python
import lief

elf = lief.ELF.parse("/bin/ls")
for section in elf.sections:
    print(section.name, len(section.content))

pe = lief.PE.parse("cmd.exe")
for imp in pe.imports:
    print(imp.name)

fat = lief.MachO.parse("/bin/dyld")
for macho in fat:
    for sym in macho.symbols:
        print(sym)
```

Sections: About, Getting Started, Documentation, Contact

</details>

### omnibase_core

ONEX Core Framework - Base classes and essential implementations

`pip install omnibase_core` · installs (wheel) · licence: MIT · rank 3724 · last release 2026-11-08 · [PyPI](https://pypi.org/project/omnibase_core/) · [docs](https://github.com/OmniNode-ai/knowledge_base) · [source](https://github.com/OmniNode-ai/omnibase_core)

<details><summary>README extract</summary>

omnibase_core provides the contracts, models, validation and execution primitives for the ONEX framework.
Documentation: knowledge_base.

Sections: omnibase_core, v0.47.69 (2026-11-07), Included Since v0.47.67, v0.47.67 (2026-11-05), Included Since v0.47.66, v0.47.66 (2026-11-04), Included Since v0.47.62, v0.47.62 (2026-11-02), Included Since v0.47.61, v0.47.61 (2026-11-01), Included Since v0.47.60, v0.47.60 (2026-10-31), Included Since v0.47.59, v0.47.59 (2026-10-30)

</details>

### numpy-stl

Library to make reading, writing and modifying both binary and ascii STL files easy.

`pip install numpy-stl` · installs (wheel) · licence: BSD-3-Clause · rank 3726 · last release 2026-10-28 · [PyPI](https://pypi.org/project/numpy-stl/)

<details><summary>README extract</summary>

A fast library for reading, writing, and modifying STL files, powered
by NumPy. Every mesh operation uses vectorized array math for speed.

*Stanford Dragon — 871,414 triangles loaded in 0.63s, rendered with matplotlib*

Features:
- Read and write binary and ASCII STL files
- Read PLY and 3MF files (3MF is experimental, read-only)
- Mesh operations: rotate, translate, transform (4x4 matrix)
- Properties: surface area, volume, center of gravity, inertia
 tensor, convexity ...

Example:
```python
from stl import mesh

# Load an STL file (auto-detects binary/ASCII)
your_mesh = mesh.Mesh.from_file('model.stl')

# Inspect
print(f'{len(your_mesh)} triangles')
print(f'Bounding box: {your_mesh.min} to {your_mesh.max}')

# Save
your_mesh.save('output.stl')
```

...

</details>

### icecream

Never use print() to debug again: inspect variables, expressions, and program execution with a single, simple function call.

`pip install icecream` · installs (wheel) · licence: MIT License · rank 3732 · last release 2026-04-03 · [PyPI](https://pypi.org/project/icecream/)

### cwevals

The official Python library for the CoreWeave Evaluations API

`pip install cwevals` · installs (wheel) · licence: Apache Software License · rank 3738 · last release 2026-10-28 · [PyPI](https://pypi.org/project/cwevals/) · [source](https://github.com/wandb/core)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Core Weave Evaluations Python library provides convenient access to the Core Weave Evaluations REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx. ...

Example:
```python
from coreweave_evaluations import Client

client = Client()

service = client.service.get()
print(service.message)
```

Sections: Core Weave Evaluations Python API library, Documentation, Usage, Async usage, With aiohttp, Using types, Nested params, Handling errors, Retries, Timeouts, Advanced, Logging, How to tell whether `None` means `null` or missing, Accessing raw response data (e.g. headers)

</details>

### singer-sdk

A framework for building Singer taps and targets

`pip install singer-sdk` · installs (wheel) · licence: Apache-2.0 · rank 3749 · last release 2026-10-19 · [PyPI](https://pypi.org/project/singer-sdk/) · [docs](https://sdk.meltano.com/en/latest/) · [source](https://github.com/meltano/sdk)

<details><summary>README extract</summary>

Taps and targets built on the SDK are automatically compliant with the
Singer Spec, the
de-facto open source standard for extract and load pipelines.

______________

______________

On average, developers tell us that they write about 70% less code by using the SDK, which
makes learning the SDK a great investment. ...

Sections: Meltano Singer SDK, Future-proof extractors and loaders, with less code, Meltano, Documentation

</details>

### flatdict

Python module for interacting with nested dicts as a single level dict with delimited keys.

`pip install flatdict` · installs (wheel) · licence: BSD-3-Clause · rank 3764 · last release 2026-02-15 · [PyPI](https://pypi.org/project/flatdict/) · [docs](https://flatdict.readthedocs.io)

<details><summary>README extract</summary>

`FlatDict` and `FlatterDict` are dict classes that allow for single level,
delimited key/value pair mapping of nested dictionaries. You can interact with
`FlatDict` and `FlatterDict` like a normal dictionary and access child
dictionaries as you normally would or with the composite key.

*For example:*

*would be the same as:* ...

Example:
```python
value = flatdict.FlatDict({'foo': {'bar': 'baz', 'qux': 'corge'}})
```

Sections: FlatDict, API, Versioning

</details>

### paypalrestsdk

Deprecated

`pip install paypalrestsdk` · installs (wheel) · licence: PayPal SDK License · rank 3770 · last release 2023-11-01 · [PyPI](https://pypi.org/project/paypalrestsdk/)

### dohq-artifactory

A Python interface to Artifactory

`pip install dohq-artifactory` · installs (wheel) · licence: MIT License · rank 3771 · last release 2026-08-19 · [PyPI](https://pypi.org/project/dohq-artifactory/)

### hanzidentifier

Python module that identifies Chinese text as Simplified or Traditional.

`pip install hanzidentifier` · installs (wheel) · licence: MIT License · rank 3773 · last release 2024-11-20 · [PyPI](https://pypi.org/project/hanzidentifier/) · [source](https://github.com/tsroten/hanzidentifier)

<details><summary>README extract</summary>

Hanzi Identifier is a simple Python module that identifies a string of text as
having Simplified or Traditional characters.

* Free software: MIT license

Easy-to-use helper functions for identifying strings:

Here it is without the helper functions:

`hanzidentifier.identify` has five possible return values: ...

Example:
```python
>>> import hanzidentifier
>>> hanzidentifier.has_chinese('Hello my name is John.')
False
>>> hanzidentifier.is_simplified('John说：你好！')
True
>>> hanzidentifier.is_traditional('John說：你好！')
True
>>> hanzidentifier.has_chinese('Country in Simplified: 国家. Country in Traditional: 國家.')
True
```

Sections: Hanzi Identifier, About, Getting Started

</details>

### ldaptor

A Pure-Python Twisted library for LDAP

`pip install ldaptor` · installs (wheel) · licence: MIT License · rank 3776 · last release 2021-02-28 · [PyPI](https://pypi.org/project/ldaptor/)

<details><summary>README extract</summary>

Ldaptor is a pure-Python library that implements:

- LDAP client logic
- separately-accessible LDAP and BER protocol message generation/parsing
- ASCII-format LDAP filter generation and parsing
- LDIF format data generation
- Samba password changing logic

Also included is a set of LDAP utilities for use from the command line. ...

Example:
```python
from twisted.internet import reactor, defer
from ldaptor.protocols.ldap import ldapclient, ldapsyntax, ldapconnector

@defer.inlineCallbacks
def example():
    # The following arguments may be also specified as unicode strings
    # but it is recommended to use byte strings for ldaptor objects
    serverip = b'192.168.128.21'
...
```

Sections: Ldaptor, Quick Usage Example

</details>

### pep8

Python style guide checker

`pip install pep8` · installs (wheel) · licence: MIT License · rank 3789 · last release 2017-10-24 · [PyPI](https://pypi.org/project/pep8/)

<details><summary>README extract</summary>

pep8 is a tool to check your Python code against some of the style
conventions in PEP 8.

Features:
* Plugin architecture: Adding new checks is easy.

* Parseable output: Jump to error location in your editor.

* Small: Just one Python file, requires only stdlib. You can use just
 the pep8.py file for this purpose. ...

Example:
```python
$ pep8 --first optparse.py
optparse.py:69:11: E401 multiple imports on one line
optparse.py:77:1: E302 expected 2 blank lines, found 1
optparse.py:88:5: E301 expected 1 blank line, found 0
optparse.py:222:34: W602 deprecated form of raising exception
optparse.py:347:31: E211 whitespace before '('
optparse.py:357:17: E201 whitespace after '{'
...
```

...

</details>

### paypalhttp

(no summary)

`pip install paypalhttp` · installs (wheel) · licence: MIT · rank 3790 · last release 2021-09-14 · [PyPI](https://pypi.org/project/paypalhttp/)

<details><summary>README extract</summary>

PayPalHttp is a generic http client designed to be used with code-generated projects.

</details>

### deepl

Python library for the DeepL API.

`pip install deepl` · installs (wheel) · licence: MIT License · rank 3791 · last release 2026-11-02 · [PyPI](https://pypi.org/project/deepl/) · [docs](https://www.deepl.com/docs-api/) · [source](https://github.com/DeepLcom/deepl-python)

<details><summary>README extract</summary>

The DeepL API is a language AI API that allows other computer programs
to send texts and documents to DeepL's servers and receive high-quality
translations and improvements to the text. ...

Example:
```python
import deepl

auth_key = "f63c02c5-f056-..."  # Replace with your key
deepl_client = deepl.DeepLClient(auth_key)

result = deepl_client.translate_text("Hello, world!", target_lang="FR")
print(result.text)  # "Bonjour, le monde !"
```

...

</details>

### Flask-Admin

Simple and extensible admin interface framework for Flask

`pip install Flask-Admin` · installs (wheel) · licence: BSD License · rank 3792 · last release 2026-09-21 · [PyPI](https://pypi.org/project/Flask-Admin/) · [docs](https://flask-admin.readthedocs.io) · [source](https://github.com/pallets-eco/flask-admin/)

<details><summary>README extract</summary>

Flask-Admin is now part of Pallets-Eco, an open source organization managed by the
Pallets team to facilitate community maintenance of Flask extensions. Please update
your references to `

Sections: Flask-Admin, Introduction, Examples, How to run an example, Documentation, Tests, 3rd Party Stuff, As a translator who's updated some `.po`/`.mo` files

</details>

### langchain-tests

Standard tests for LangChain implementations

`pip install langchain-tests` · installs (wheel) · licence: MIT License · rank 3795 · last release 2026-05-21 · [PyPI](https://pypi.org/project/langchain-tests/) · [docs](https://docs.langchain.com/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Example:
```python
"""Standard LangChain interface tests"""

from typing import Type

import pytest
from langchain_core.language_models import BaseChatModel
from langchain_tests.unit_tests import ChatModelUnitTests

from langchain_parrot_chain import ChatParrotChain

class TestParrotChainStandard(ChatModelUnitTests):
    @pytest.fixture
...
```

Sections: 🦜️🔗 langchain-tests, 🤔 What is this?, 📖 Documentation, Usage, Reference

</details>

### returns

Make your functions return something meaningful, typed, and safe!

`pip install returns` · installs (wheel) · licence: BSD License · rank 3797 · last release 2026-10-27 · [PyPI](https://pypi.org/project/returns/) · [source](https://github.com/dry-python/returns)

<details><summary>README extract</summary>

Make your functions return something meaningful, typed, and safe!

Features:
- Brings functional programming to Python land
- Provides a bunch of primitives to write declarative business logic
- Enforces better architecture
- Fully typed with annotations and checked with `mypy`, PEP561 compatible ...

Example:
```python
import requests
from returns.result import Result, safe
from returns.pipeline import flow
from returns.pointfree import bind

def fetch_user_profile(user_id: int) -> Result['UserProfile', Exception]:
    """Fetches `UserProfile` TypedDict from foreign API."""
    return flow(
        user_id,
        _make_request,
        bind(_parse_json),
    )
...
```

...

</details>

### Whoosh

Fast, pure-Python full text indexing, search, and spell checking library.

`pip install Whoosh` · installs (wheel) · licence: BSD License · rank 3799 · last release 2016-04-04 · [PyPI](https://pypi.org/project/Whoosh/)

<details><summary>README extract</summary>

Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how Whoosh
works can be extended or replaced to meet your needs exactly.

Some of Whoosh's features include:

* Pythonic API.
* Pure-Python. ...

Sections: About Whoosh, Learning more, Getting the source

</details>

### Pebble

Threading and multiprocessing eye-candy.

`pip install Pebble` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 3802 · last release 2026-10-04 · [PyPI](https://pypi.org/project/Pebble/)

_README extract left out: share-alike licence._

### dishka

Cute DI framework with scopes and agreeable API

`pip install dishka` · installs (wheel) · licence: Apache-2.0 · rank 3803 · last release 2026-04-25 · [PyPI](https://pypi.org/project/dishka/) · [docs](https://dishka.readthedocs.io/en/stable/) · [source](https://github.com/reagento/dishka)

<details><summary>README extract</summary>

Cute DI framework with scopes and an agreeable API.

📚 Documentation

This library provides an IoC container that's genuinely useful.
If you're exhausted from endlessly passing objects to create other objects, only to have those objects create even
more — you're not alone, and ``dishka`` is a solution. ...

Features:
* Scopes. Any object can have a lifespan for the entire app, a single request, or even more fractionally. Many
 frameworks either lack scopes completely or offer only two. With ``dishka``, you can define as many scopes as needed.
* Finalization. ...

Example:
```python
from sqlite3 import Connection
from typing import Protocol

class APIClient:
    ...

class UserDAO(Protocol):
    ...

class SQLiteUserDAO(UserDAO):
    def init(self, connection: Connection):
        ...

...

</details>

### django-treebeard

Efficient tree implementations for Django

`pip install django-treebeard` · installs (wheel) · licence: Apache-2.0 · rank 3826 · last release 2026-10-21 · [PyPI](https://pypi.org/project/django-treebeard/) · [docs](http://django-treebeard.readthedocs.io/) · [source](https://github.com/django-treebeard/django-treebeard)

<details><summary>README extract</summary>

django-treebeard is a library that implements efficient tree implementations for the Django Web Framework.

It was written by Gustavo Picón and licensed under the Apache License 2.0.

Features:
django-treebeard is:

- Flexible: Includes 3 different tree implementations with the
 same API:
 1. Adjacency List
 2. Materialized Path
 3. Nested Sets
 4. PostgreSQL ltree (experimental)
- Fast: Optimized non-naive tree operations ...

Sections: django-treebeard, Features, System requirements

</details>

### jsoncomparison

json compare utility

`pip install jsoncomparison` · installs (wheel) · licence: MIT License · rank 3831 · last release 2021-05-17 · [PyPI](https://pypi.org/project/jsoncomparison/) · [docs](https://github.com/rugleb/JsonCompare/blob/master/README.md) · [source](https://github.com/rugleb/JsonCompare)

<details><summary>README extract</summary>

This package is designed to compare two objects with a JSON-like structure and data types.

Example:
```python
from jsoncomparison import Compare, NO_DIFF

expected = {
    "project": {
        "name": "jsoncomparison",
        "version": "0.1",
        "license": "MIT",
        "language": {
            "name": "python",
            "versions": [
                3.5,
                3.6
            ]
        }
    },
    "os": "linux"
}

actual = {
...
```

Sections: The JSON Comparison package, Usage, Configuration, Output, Ignore rules, Links

</details>

### pyinotify

Linux filesystem events monitoring

`pip install pyinotify` · installs from source (sdist only) · licence: MIT License · rank 3838 · last release 2015-06-04 · [PyPI](https://pypi.org/project/pyinotify/)

<details><summary>README extract</summary>

* License : MIT

* Linux ≥ 2.6.13
* Python ≥ 2.4 (including Python 3.x)

Sections: Pyinotify, Dependencies, Watch a directory

</details>

### airtable

Python client library for AirTable

`pip install airtable` · installs (wheel) · licence: The MIT License (MIT) · rank 3845 · last release 2021-02-05 · [PyPI](https://pypi.org/project/airtable/)

<details><summary>README extract</summary>

Python interface to the Airtable's REST API - -

For javascript enthusiasts:

Example:
```python
from airtable import airtable
at = airtable.Airtable('BASE_ID', 'API_KEY')
at.get('TABLE_NAME')
```

Sections: Airtable.py: Python API wrapper for Airtable, Getting started, API Reference, Get, Iterate, Create, Update, Update All, Delete

</details>

### pyobjc-framework-Quartz

Wrappers for the Quartz frameworks on macOS

`pip install pyobjc-framework-Quartz` · installs from source (sdist only) · licence: MIT · rank 3856 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Quartz/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Quartz" related frameworks on macOS. These frameworks
provide a number of graphics related API's.

The frameworks wrapped by this package are:

 * CoreGraphics - 2D Graphics, based on the PDF model

 * ImageIO - Reading and writing images

 * QuartzComposer - Working with "Quartz Composer" compositions ...

Sections: NEWS, 2.4, Project links

</details>

### textfsm

Python module for parsing semi-structured text into python tables.

`pip install textfsm` · installs (wheel) · licence: Apache Software License · rank 3862 · last release 2025-04-17 · [PyPI](https://pypi.org/project/textfsm/)

<details><summary>README extract</summary>

Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI) of networking
devices. ...

</details>

### crawlee

Crawlee for Python

`pip install crawlee` · installs (wheel) · licence: Apache-2.0 · rank 3874 · last release 2026-11-05 · [PyPI](https://pypi.org/project/crawlee/) · [docs](https://crawlee.dev/python/docs/quick-start) · [source](https://github.com/apify/crawlee-python)

<details><summary>README extract</summary>

A web scraping and browser automation library

Crawlee covers your crawling and scraping end-to-end and helps you build reliable scrapers. Fast.

Your crawlers will appear almost human-like and fly under the radar of modern bot protections even with the default configuration. ...

Features:
Why Crawlee is the preferred choice for web scraping and crawling?

Example:
```python
import asyncio

from crawlee.crawlers import BeautifulSoupCrawler, BeautifulSoupCrawlingContext

async def main() -> None:
    crawler = BeautifulSoupCrawler(
        # Limit the crawl to max requests. Remove or increase it for crawling all links.
        max_requests_per_crawl=10,
    )

...
```

...

</details>

### geonamescache

Geonames data for continents, cities and US states.

`pip install geonamescache` · installs (wheel) · licence: MIT · rank 3885 · last release 2026-07-28 · [PyPI](https://pypi.org/project/geonamescache/) · [docs](https://github.com/yaph/geonamescache#readme) · [source](https://github.com/yaph/geonamescache)

<details><summary>README extract</summary>

A Python library that provides functions to retrieve names, ISO and FIPS codes of continents, countries as well as US states and counties as Python dictionaries. The country and city datasets also include population and geographic data.

Geonames data is obtained from GeoNames.

Sections: GeonamesCache, Usage, Settings, Cities dataset, Methods, Mappers

</details>

### flake8-import-order

Flake8 and pylama plugin that checks the ordering of import statements.

`pip install flake8-import-order` · installs (wheel) · licence: LGPLv3 · rank 3894 · last release 2025-06-24 · [PyPI](https://pypi.org/project/flake8-import-order/)

_README extract left out: share-alike licence._

### apache-airflow-microsoft-fabric-plugin

A plugin for Apache Airflow to interact with Microsoft Fabric items

`pip install apache-airflow-microsoft-fabric-plugin` · installs (wheel) · licence: not stated · rank 3897 · last release 2024-09-09 · [PyPI](https://pypi.org/project/apache-airflow-microsoft-fabric-plugin/)

<details><summary>README extract</summary>

A Python package that helps Data and Analytics engineers trigger run on demand job items of Microsoft Fabric in Apache Airflow DAGs.

Microsoft Fabric is an end-to-end analytics and data platform designed for enterprises that require a unified solution. ...

Features:
Refresh token rotation is a security mechanism that involves replacing the refresh token each time it is used to obtain a new access token.
 This process enhances security by reducing the risk of stolen tokens being reused indefinitely. ...

Example:
```python
from future import annotations

from airflow import DAG
from apache_airflow_microsoft_fabric_plugin.operators.fabric import FabricRunItemOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
}

...

</details>

### apache-airflow-providers-microsoft-fabric

A plugin for Apache Airflow to interact with Microsoft Fabric items

`pip install apache-airflow-providers-microsoft-fabric` · installs (wheel) · licence: not stated · rank 3901 · last release 2026-04-25 · [PyPI](https://pypi.org/project/apache-airflow-providers-microsoft-fabric/)

<details><summary>README extract</summary>

An Apache Airflow provider package for Microsoft Fabric. It enables Data and Analytics engineers to trigger, monitor, and orchestrate Microsoft Fabric items from Airflow DAGs.

Microsoft Fabric is an end-to-end analytics and data platform designed for enterprises that require a unified solution. ...

Features:
Connections in Microsoft Fabric are identified by GUIDs, not by the
human-readable names Airflow normally uses. When a DAG references a Fabric
connection (e.g. ...

Example:
```python
from airflow.providers.microsoft.fabric.operators.run_item import MSFabricRunJobOperator

run_notebook = MSFabricRunJobOperator(
    task_id="run_fabric_notebook",
    workspace_id="<workspace_id>",
    item_id="<item_id>",
    fabric_conn_id="fabric_conn_id",
    job_type="RunNotebook",
...

</details>

### Naked

A command line application framework

`pip install Naked` · installs (wheel) · licence: MIT License · rank 3906 · last release 2022-11-06 · [PyPI](https://pypi.org/project/Naked/)

### lunardate

A Chinese Calendar Library in Pure Python

`pip install lunardate` · installs (wheel) · licence: GPL-3.0-or-later · rank 3913 · last release 2026-07-07 · [PyPI](https://pypi.org/project/lunardate/)

_README extract left out: share-alike licence._

### aiohttp-client-cache

Persistent cache for aiohttp requests

`pip install aiohttp-client-cache` · installs (wheel) · licence: MIT License · rank 3917 · last release 2026-10-07 · [PyPI](https://pypi.org/project/aiohttp-client-cache/) · [docs](https://aiohttp-client-cache.readthedocs.io) · [source](https://github.com/requests-cache/aiohttp-client-cache)

<details><summary>README extract</summary>

aiohttp-client-cache is an async persistent cache for aiohttp
client requests, based on requests-cache.

Features:
- Ease of use: Use as a drop-in replacement
 for `aiohttp.ClientSession`
- Customization: Works out of the box with little to no config, but with plenty of options
 available for customizing cache
 expiration
 and other behavior ...

Example:
```python
from aiohttp import ClientSession

async with ClientSession() as session:
    await session.get('
```

Sections: aiohttp-client-cache, Features, Quickstart, Basic Usage, Configuration, More Info, Feedback

</details>

### reporters-db

Database of Court Reporters

`pip install reporters-db` · installs (wheel) · licence: BSD-2-Clause · rank 3937 · last release 2026-10-15 · [PyPI](https://pypi.org/project/reporters-db/) · [source](https://github.com/freelawproject/reporters-db)

<details><summary>README extract</summary>

+---------------+---------------------+-------------------+
Lint Badge Version Badge
+---------------+---------------------+-------------------+

A long, long time ago near a courthouse not too far away, people started
keeping books of every important opinion that was ever written. ...

Example:
```python
from reporters_db import REPORTERS
```

Sections: Background of the Free Law Reporters Database, Data Sourcing, API, CSV, Known Implementations, Some Notes on the Data, The "regexes" field and regexes.json placeholders, `state_abbreviations` and `case_name_abbreviations` files, Notes on Specific Data Point and References, Tests

</details>

### xattr

Python wrapper for extended filesystem attributes

`pip install xattr` · installs (wheel) · licence: MIT · rank 3945 · last release 2025-10-13 · [PyPI](https://pypi.org/project/xattr/) · [source](https://github.com/xattr/xattr)

<details><summary>README extract</summary>

xattr is a Python wrapper for extended filesystem attributes.

xattr also ships with an `xattr` command line tool for viewing and
editing extended filesystem attributes. On platforms that support or
ship with the attr package, you may prefer to use the `getfattr`
and `setfattr` command line tools from the attr package. ...

</details>

### json-stream

Streaming JSON encoder and decoder

`pip install json-stream` · installs (wheel) · licence: MIT License · rank 3948 · last release 2026-04-27 · [PyPI](https://pypi.org/project/json-stream/) · [source](https://github.com/daggaz/json-stream)

<details><summary>README extract</summary>

Simple streaming JSON parser and encoder.

When reading JSON data, `json-stream` can decode JSON data in
a streaming manner, providing a pythonic dict/list-like interface, or a
visitor-based interface. It can stream from files, URLs
or iterators. ...

Example:
```python
import json_stream

with open("events.ndjson", "rb") as f:  # NDJSON: one JSON object per line
    for item in json_stream.load_many(f):
        # each item is the top-level item in each JSON text
        handle(item)
```

Sections: json-stream, Reading, Usage, `json_stream.load()`, Transient mode (default), Persistent mode, Mixed mode, visitor pattern, Multiple JSON documents: `load_many()` and `visit_many()`, Examples, Stream a URL, urllib, requests, httpx

</details>

### box-sdk-gen

Official Box Python Generated SDK

`pip install box-sdk-gen` · installs (wheel) · licence: Apache Software License · rank 3974 · last release 2025-09-05 · [PyPI](https://pypi.org/project/box-sdk-gen/)

<details><summary>README extract</summary>

We are excited to introduce the stable release of the latest generation of Box Python SDK, designed to elevate the developer experience and streamline your integration with the Box Content Cloud.

With this SDK, you’ll have access to:

1. ...

Example:
```python
from box_sdk_gen import BoxClient, BoxDeveloperTokenAuth

def main(token: str):
    auth: BoxDeveloperTokenAuth = BoxDeveloperTokenAuth(token=token)
    client: BoxClient = BoxClient(auth=auth)
    for item in client.folders.get_folder_items('0').entries:
        print(item.name)

if name == 'main':
    main('INSERT YOUR DEVELOPER TOKEN HERE')
```

...

</details>

### courts-db

Database of Courts

`pip install courts-db` · installs (wheel) · licence: BSD-2-Clause · rank 3988 · last release 2026-03-25 · [PyPI](https://pypi.org/project/courts-db/) · [source](https://github.com/freelawproject/courts-db)

<details><summary>README extract</summary>

Courts-DB is an open source repository to organize a database of all courts current and historical.
It was built for use in CourtListener.com.

Its main goal is to interface with CourtListener to identify historical and current courts
by string. It includes mechanisms to filter results based on dates and/or whether it is a bankruptcy court. ...

Example:
```python
from courts_db import find_court, find_court_by_id

find_court_by_id("mass")

returns:
[{
    "regex": [
        "${sjc} ${ma}?",
        "${ma} ${sjc}",
        "Supreme Court Of ${ma}",
        "State Of ${ma} Supreme Court"
    ],
    "name_abbreviation": "Mass. Sup. Jud. Ct.",
    "dates": [
        {
            "start": "1692-01-01",
...
```

...

</details>

### synapseml

Synapse Machine Learning

`pip install synapseml` · installs (wheel) · licence: MIT License · rank 3989 · last release 2026-04-07 · [PyPI](https://pypi.org/project/synapseml/)

<details><summary>README extract</summary>

SynapseML contains Microsoft's open source contributions to the Apache Spark ecosystem

</details>

### eyecite

Tool for extracting legal citations from text strings.

`pip install eyecite` · installs (wheel) · licence: BSD-2-Clause · rank 3999 · last release 2026-07-01 · [PyPI](https://pypi.org/project/eyecite/) · [source](https://github.com/freelawproject/eyecite)

<details><summary>README extract</summary>

Example:
```python
from eyecite import get_citations

text = """
    Mass. Gen. Laws ch. 1, § 2 (West 1999) (barring ...).
    Foo v. Bar, 1 U.S. 2, 3-4 (1999) (overruling ...).
    Id. at 3.
    Foo, supra, at 5.
"""

get_citations(text)

# returns:
[
    FullLawCitation(
        'Mass. Gen. Laws ch. 1, § 2',
...
```

Sections: Functionality, API, Quickstart, Tutorial, Documentation, Cleaning Input Text, Wrapping HTML Tags, Customizing Annotation, Tokenizers, AhocorasickTokenizer (default), HyperscanTokenizer, Debugging, Deployment

</details>

### pykerberos

High-level interface to Kerberos

`pip install pykerberos` · installs from source (sdist only) · licence: Apache Software License · rank 4003 · last release 2022-03-09 · [PyPI](https://pypi.org/project/pykerberos/)

<details><summary>README extract</summary>

This Python package is a high-level wrapper for Kerberos (GSSAPI) operations.
The goal is to avoid having to build a module that wraps the entire Kerberos.framework,
and instead offer a limited set of functions that do what is needed for client/server
Kerberos authentication based on <

</details>

### PyQRCode

A QR code generator written purely in Python with SVG, EPS, PNG and terminal output.

`pip install PyQRCode` · installs from source (sdist only) · licence: BSD License · rank 4004 · last release 2016-06-20 · [PyPI](https://pypi.org/project/PyQRCode/)

<details><summary>README extract</summary>

The pyqrcode module is a QR code generator that is simple to use and written
in pure python. The module can automates most of the building process for
creating QR codes. Most codes can be created using only two lines of code!

Unlike other generators, all of the helpers can be controlled manually. ...

Example:
```python
>>> import pyqrcode
>>> url = pyqrcode.create('
>>> url.svg('uca-url.svg', scale=8)
>>> url.eps('uca-url.eps', scale=2)
>>> print(url.terminal(quiet_zone=1))
```

Sections: PyQRCode, Requirements, Usage

</details>

### habluetooth

High availability Bluetooth

`pip install habluetooth` · installs (wheel) · licence: Apache-2.0 · rank 4006 · last release 2026-09-22 · [PyPI](https://pypi.org/project/habluetooth/) · [docs](https://habluetooth.readthedocs.io) · [source](https://github.com/bluetooth-devices/habluetooth)

<details><summary>README extract</summary>

Documentation:

Source Code:

High availability Bluetooth

</details>

### omnibase_spi

ONEX Service Provider Interface - Protocol definitions

`pip install omnibase_spi` · installs (wheel) · licence: MIT License · rank 4010 · last release 2026-11-05 · [PyPI](https://pypi.org/project/omnibase_spi/) · [docs](https://github.com/OmniNode-ai/knowledge_base) · [source](https://github.com/OmniNode-ai/omnibase_spi)

<details><summary>README extract</summary>

omnibase_spi defines ONEX service-provider protocols and wire contracts with namespace isolation between interfaces and implementations.
Documentation: knowledge_base.

</details>

### django-picklefield

Pickled object field for Django

`pip install django-picklefield` · installs (wheel) · licence: MIT License · rank 4013 · last release 2025-11-27 · [PyPI](https://pypi.org/project/django-picklefield/)

<details><summary>README extract</summary>

django-picklefield provides an implementation of a pickled object field.
Such fields can contain any picklable objects.

The implementation is taken and adopted from Django snippet #1694 by Taavi
Taijala, which is in turn based on Django snippet #513 by Oliver Beattie.

django-picklefield is available under the MIT license.

Example:
```python
>>> from picklefield.fields import PickledObjectField
... class SomeObject(models.Model):
...     args = PickledObjectField()
```

Sections: django-picklefield, About, Usage, Notes, Running tests, Original notes, Changes, Changes in version 3.4.0, Changes in version 3.3.0, Changes in version 3.2.0, Changes in version 3.1.0, Changes in version 3.0.1, Changes in version 3.0.0, Changes in version 2.1.0

</details>

### opentracing

OpenTracing API for Python. See documentation at http://opentracing.io

`pip install opentracing` · installs from source (sdist only) · licence: Apache Software License · rank 4014 · last release 2020-11-19 · [PyPI](https://pypi.org/project/opentracing/)

<details><summary>README extract</summary>

This library is a Python platform API for OpenTracing.

In order to understand the Python platform API, one must first be familiar with
the OpenTracing project and
terminology more
specifically.

Example:
```python
def handle_request(request):
    span = before_request(request, opentracing.global_tracer())
    # store span in some request-local storage using Tracer.scope_manager,
    # using the returned `Scope` as Context Manager to ensure
    # `Span` will be cleared and (in this case) `Span.finish()` be called.
...
```

Sections: OpenTracing API for Python, Required Reading, Usage, Inbound request, Outbound request, Scope and within-process propagation, Scope managers

</details>

### spacy-language-detection

Fully customizable language detection for spaCy pipeline

`pip install spacy-language-detection` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 4027 · last release 2021-09-08 · [PyPI](https://pypi.org/project/spacy-language-detection/)

_README extract left out: share-alike licence._

### django-tenants

Tenant support for Django using PostgreSQL schemas.

`pip install django-tenants` · installs (wheel) · licence: MIT · rank 4045 · last release 2026-10-23 · [PyPI](https://pypi.org/project/django-tenants/)

<details><summary>README extract</summary>

This application enables django powered websites to have multiple
tenants via PostgreSQL schemas. A vital feature for every
Software-as-a-Service (SaaS) website.

 Read the full documentation here: django-tenants.readthedocs.org ...

Features:
There are typically three solutions for solving the multitenancy
problem.

1. Isolated Approach: Separate Databases. Each tenant has its own
 database.

2. Semi Isolated Approach: Shared Database, Separate Schemas. ...

Example:
```python
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

class Domain(DomainMixin):
...

</details>

### EbookLib

Ebook library which can handle EPUB2/EPUB3 format

`pip install EbookLib` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 4063 · last release 2026-11-01 · [PyPI](https://pypi.org/project/EbookLib/) · [docs](https://ebooklib.readthedocs.io) · [source](https://github.com/aerkalov/ebooklib)

_README extract left out: share-alike licence._

### flake8-quotes

Flake8 lint for quotes.

`pip install flake8-quotes` · installs from source (sdist only) · licence: MIT License · rank 4065 · last release 2024-02-10 · [PyPI](https://pypi.org/project/flake8-quotes/)

<details><summary>README extract</summary>

We automatically encourage avoiding escaping quotes as per PEP 8. To disable this, use `--no-avoid-escape` (can be used in configuration file via `avoid-escape`).

To anticipate multiline support, we are renaming `--quotes` to `--inline-quotes`. Please adjust your configurations appropriately.

Sections: Flake8 Extension to lint for quotes., Major update in 2.0.0, Deprecation notice in 0.3.0, Usage, Warnings, Configuration, Caveats

</details>

### vosk

Offline open source speech recognition API based on Kaldi and Vosk

`pip install vosk` · installs (wheel) · licence: Apache Software License · rank 4077 · last release 2022-12-14 · [PyPI](https://pypi.org/project/vosk/)

<details><summary>README extract</summary>

This is a Python module for Vosk.

Vosk is an offline open source speech recognition toolkit. It enables
speech recognition for 20+ languages and dialects - English, Indian
English, German, French, Spanish, Portuguese, Chinese, Russian, Turkish,
Vietnamese, Italian, Dutch, Catalan, Arabic, Greek, Farsi, Filipino,
Ukrainian, Kazakh, Swedish, ...

</details>

### testtools

Extensions to the Python standard library unit testing framework

`pip install testtools` · installs (wheel) · licence: MIT License · rank 4090 · last release 2026-04-24 · [PyPI](https://pypi.org/project/testtools/)

<details><summary>README extract</summary>

Example:
```python
def test_response_has_bold(self):
   # The response has bold text.
   response = self.server.getResponse()
   self.assertThat(response, HTMLContains(Tag('bold', 'b')))
```

Sections: Why use testtools?, Matchers: better than assertion methods, More debugging info, when you need it, Extend unittest, but stay compatible and re-usable, Cross-Python compatibility

</details>

### pyexcel-io

A python library to read and write structured data in csv, zipped csvformat and to/from databases

`pip install pyexcel-io` · installs (wheel) · licence: BSD License · rank 4095 · last release 2026-06-28 · [PyPI](https://pypi.org/project/pyexcel-io/)

<details><summary>README extract</summary>

Sections: pyexcel-io - Let you focus on data, instead of file formats, Known constraints, Introduction, Plugin shopping guide, . git clone, . cd pyexcel-io, Before you commit, Before you raise pull request, 0.6.8 - 28.06.2026, . #56: fix regex error, 0.6.7 - 09.11.2024, . #115: Pathnames with ., . #117: fix a typo in, 0.6.6 - 31.1.2022

</details>

### geckodriver-autoinstaller

Automatically install geckodriver that supports the currently installed version of chrome.

`pip install geckodriver-autoinstaller` · installs (wheel) · licence: MIT License · rank 4108 · last release 2020-02-14 · [PyPI](https://pypi.org/project/geckodriver-autoinstaller/)

<details><summary>README extract</summary>

Example:
```python
from selenium import webdriver
import geckodriver_autoinstaller

geckodriver_autoinstaller.install()  # Check if the current version of geckodriver exists
                                     # and if it doesn't exist, download it automatically,
                                     # then add geckodriver to path

driver = webdriver.Firefox()
...
```

Sections: Usage, Example

</details>

### fastcrc

A hyper-fast Python module for computing CRC(8, 16, 32, 64) checksum

`pip install fastcrc` · installs (wheel) · licence: MIT License · rank 4109 · last release 2026-09-16 · [PyPI](https://pypi.org/project/fastcrc/) · [docs](https://fastcrc.readthedocs.io) · [source](https://github.com/overcat/fastcrc)

<details><summary>README extract</summary>

A hyper-fast Python module for computing CRC(8, 16, 32, 64) checksum.

Example:
```python
from fastcrc import crc8, crc16, crc32, crc64

data = b"123456789"
print(f"crc8 checksum with cdma2000 algorithm: {crc8.cdma2000(data)}")
print(f"crc16 checksum with xmodem algorithm: {crc16.xmodem(data)}")
print(f"crc32 checksum with aixm algorithm: {crc32.aixm(data)}")
print(f"crc64 checksum with ecma_182 algorithm: {crc64.ecma_182(data)}")
...
```

Sections: fastcrc, Usage, Notes, Performance, Documentation, Thanks

</details>

### mergepythonclient

(no summary)

`pip install mergepythonclient` · installs (wheel) · licence: not stated · rank 4120 · last release 2026-10-05 · [PyPI](https://pypi.org/project/mergepythonclient/) · [source](https://github.com/merge-api/merge-python-client)

<details><summary>README extract</summary>

The Merge Python library provides convenient access to the Merge APIs from Python.

Example:
```python
from merge import Merge

client = Merge(
    api_key="<token>",
)

client.ats.account_token.regenerate_create()
```

Sections: Merge Python Library, Documentation, Reference, Usage, Instantiation, Categories, Async Client, Exception Handling, Advanced, Access Raw Response Data, Retries, Timeouts, Custom Client, File Download

</details>

### pyasyncore

Make asyncore available for Python 3.12 onwards

`pip install pyasyncore` · installs (wheel) · licence: Python Software Foundation License · rank 4125 · last release 2026-01-05 · [PyPI](https://pypi.org/project/pyasyncore/)

<details><summary>README extract</summary>

This package contains the asyncore module as found in Python versions prior to 3.12.
It is provided so that existing code relying on `import asyncore` is able to continue being used without significant refactoring.

The module's source code is taken directly from the Python standard library<sup id="a1">[[1]](#f1)</sup>. ...

Example:
```python
import asyncore
```

Sections: Purpose, Usage, Maintenance, Footnotes

</details>

### cerebras-cloud-sdk

The official Python library for the cerebras API

`pip install cerebras-cloud-sdk` · installs (wheel) · licence: Apache Software License · rank 4129 · last release 2026-07-16 · [PyPI](https://pypi.org/project/cerebras-cloud-sdk/) · [source](https://github.com/Cerebras/cerebras-cloud-sdk-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Cerebras Python library provides convenient access to the Cerebras REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
import asyncio
from cerebras.cloud.sdk import AsyncCerebras

client = AsyncCerebras(
    api_key=os.environ.get("CEREBRAS_API_KEY"),  # This is the default and can be omitted
)

async def main() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
...
```

...

</details>

### autopage

A library to provide automatic paging for console output

`pip install autopage` · installs (wheel) · licence: OSI Approved; Apache Software License · rank 4131 · last release 2026-01-30 · [PyPI](https://pypi.org/project/autopage/)

<details><summary>README extract</summary>

Autopage is a Python library to
automatically display terminal output from a program in a pager (like `less`)
whenever you need it, and never when you don't. And it only takes one line of
code. ...

Example:
```python
import sys
import autopage

with autopage.AutoPager() as out:
    for l in sys.stdin:
        out.write(l)
```

Sections: autopage, On Fedora and CentOS/RHEL, On Ubuntu and Debian, On Gentoo, Basic Use, Paging help output, Environment, Line buffering, Terminal reset, Exit code, Complete Example

</details>

### prefect-gcp

Prefect integrations for interacting with Google Cloud Platform.

`pip install prefect-gcp` · installs (wheel) · licence: Apache Software License · rank 4136 · last release 2026-09-08 · [PyPI](https://pypi.org/project/prefect-gcp/)

<details><summary>README extract</summary>

`prefect-gcp` makes it easy to leverage the capabilities of Google Cloud Platform (GCP) in your flows, featuring support for Vertex AI, Cloud Run, BigQuery, Cloud Storage, and Secret Manager.

Visit the full docs here.

</details>

### graphene-django

Graphene Django integration

`pip install graphene-django` · installs (wheel) · licence: MIT · rank 4143 · last release 2025-03-13 · [PyPI](https://pypi.org/project/graphene-django/)

<details><summary>README extract</summary>

[][build-url]
[][pypi-url]
[][conda-url]
[][coveralls-url]

Graphene-Django is an open-source library that provides seamless integration between Django, a high-level Python web framework, and Graphene, a library for building GraphQL APIs. ...

Features:
* Seamless integration with Django models
* Automatic generation of GraphQL schema
* Integration with Django's authentication and permission system
* Easy querying and filtering of data
* Support for Django's pagination system
* Compatible with ...

Example:
```python
import graphene
from graphene_django import DjangoObjectType
from .models import MyModel

class MyModelType(DjangoObjectType):
    class Meta:
        model = MyModel

class Query(graphene.ObjectType):
    mymodels = graphene.List(MyModelType)

...

</details>

### lml

Load me later. A lazy plugin management system.

`pip install lml` · installs (wheel) · licence: New BSD · rank 4144 · last release 2025-03-16 · [PyPI](https://pypi.org/project/lml/)

<details><summary>README extract</summary>

lml seamlessly finds the lml based plugins from your current python
environment but loads your plugins on demand. It is designed to support
plugins that have external dependencies, especially bulky and/or
memory hungry ones. lml provides the plugin management system only and the
plugin interface is on your shoulder. ...

Example:
```python
from lml.plugin import PluginInfo, PluginManager

@PluginInfo("cuisine", tags=["Portable Battery"])
class Boost(object):
    def make(self, food=None, **keywords):
        print("I can cook %s for robots" % food)

class CuisineManager(PluginManager):
    def init(self):
        PluginManager.init(self, "cuisine")

...
```

...

</details>

### cua-driver

Rust-backed Cua Driver SDK and bundled executable for client applications

`pip install cua-driver` · installs (wheel) · licence: MIT License · rank 4154 · last release 2026-11-08 · [PyPI](https://pypi.org/project/cua-driver/) · [docs](https://github.com/trycua/cua/tree/main/libs/cua-driver) · [source](https://github.com/trycua/cua)

<details><summary>README extract</summary>

Rust-backed Python SDK and bundled executable for
Cua Driver.

This package is for client applications importing Cua Driver as an SDK:

It does not contain a Python MCP protocol implementation. Agents already have
runtime-neutral MCP clients and should configure the bundled server directly: ...

Example:
```python
import asyncio

from cua_driver import (
    CuaDriver,
    CursorReducedMotion,
    EndSessionInput,
    GetDesktopStateInput,
    SetAgentCursorThemeInput,
    StartSessionInput,
)

async def main() -> None:
    driver = CuaDriver.create()
    await driver.start_session(
...
```

Sections: cua-driver Python SDK, Product boundary, SDK example, Typed native-window migration, Daemon-backed MCP host, Binary wrapper

</details>

### gviz-api

Python API for Google Visualization

`pip install gviz-api` · installs (wheel) · licence: Apache Software License · rank 4158 · last release 2021-10-14 · [PyPI](https://pypi.org/project/gviz-api/)

<details><summary>README extract</summary>

Google Visualization API

This project is a helper python library for providers who want to implement a
data source for visualizations built on the
`Google Visualization API <

- Documentation - See the `API documentation
 for details about how to use this library.
- Installation - ``pip install gviz_api`` ...

</details>

### standard-imghdr

Standard library imghdr redistribution. "dead battery".

`pip install standard-imghdr` · installs (wheel) · licence: Python Software Foundation License · rank 4169 · last release 2024-10-30 · [PyPI](https://pypi.org/project/standard-imghdr/)

<details><summary>README extract</summary>

Python is moving forward! Python finally started to remove dead batteries.
For more information, see PEP 594.

If your project depends on a module that has been removed from the standard,
here is the redistribution of the dead batteries.

</details>

### pyudev

A libudev binding

`pip install pyudev` · installs (wheel) · licence: LGPL-2.1-or-later · rank 4197 · last release 2026-09-28 · [PyPI](https://pypi.org/project/pyudev/)

_README extract left out: share-alike licence._

### asyncinotify

'A simple optionally-async python inotify library, focused on simplicity of use and operation, and leveraging modern Python features

`pip install asyncinotify` · installs (wheel) · licence: MPL-2.0 · rank 4215 · last release 2026-04-13 · [PyPI](https://pypi.org/project/asyncinotify/) · [docs](https://asyncinotify.readthedocs.io/) · [source](https://github.com/ProCern/asyncinotify/)

<details><summary>README extract</summary>

An async python inotify package. Kept as simple and easy-to-understand as
possible, while still being flexible and powerful. This is built on no external
dependencies, and works through ctypes in a very obvious fashion.

This works without any other external dependencies. ...

Example:
```python
from pathlib import Path
from asyncinotify import Inotify, Mask
import asyncio

async def main():
    # Context manager to close the inotify handle after use
    with Inotify() as inotify:
        # Adding the watch can also be done outside of the context manager.
        # enter doesn't actually do anything except return self.
...
```

Sections: asyncinotify, Usage, Motivation

</details>

### telnyx

The official Python library for the telnyx API

`pip install telnyx` · installs (wheel) · licence: MIT License · rank 4225 · last release 2026-10-28 · [PyPI](https://pypi.org/project/telnyx/) · [source](https://github.com/team-telnyx/telnyx-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Telnyx Python library provides convenient access to the Telnyx REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),  # This is the default and can be omitted
)

response = client.calls.dial(
    connection_id="conn12345",
    from="+15557654321",
    to="+15551234567",
    webhook_url="
)
print(response.data)
```

...

</details>

### find-libpython

Finds the libpython associated with your environment, wherever it may be hiding

`pip install find-libpython` · installs (wheel) · licence: MIT · rank 4226 · last release 2026-02-11 · [PyPI](https://pypi.org/project/find-libpython/)

<details><summary>README extract</summary>

A pypi project version of this gist, which also appears
within the PyCall library.

The library is designed to find the path to the libpython dynamic library for the current Python environment.
It should work with many types of installations, whether it be conda-managed, system-managed, or otherwise. ...

Example:
```python
>>> from find_libpython import find_libpython
>>> find_libpython()
'/home/kaleb/miniconda3/envs/test/lib/libpython3.8.so.1.0'
```

Sections: find_libpython, Usage

</details>

### mdformat-frontmatter

An mdformat plugin for parsing / ignoring frontmatter.

`pip install mdformat-frontmatter` · installs (wheel) · licence: MIT · rank 4242 · last release 2026-10-27 · [PyPI](https://pypi.org/project/mdformat-frontmatter/) · [source](https://github.com/butler54/mdformat-frontmatter)

<details><summary>README extract</summary>

[][ci-link]
[][cov-link]
[][pypi-link]
[][scorecard-link]

An mdformat plugin for ensuring that yaml `front-matter` is respected.
Many tools (such as jekyll) use yaml front matter for automation purposes.
`mdformat-frontmatter` only supports yaml. For example:

Frontmatter can only be at the first line or two of the code. ...

Sections: mdformat-frontmatter, Requirements

</details>

### petl

A Python package for extracting, transforming and loading tables of data.

`pip install petl` · installs (wheel) · licence: MIT License · rank 4249 · last release 2026-10-29 · [PyPI](https://pypi.org/project/petl/)

<details><summary>README extract</summary>

`petl` is a general purpose Python package for extracting, transforming and
loading tables of data.

Please feel free to ask questions via the mailing list
(python-etl@googlegroups.com).

To report installation problems, bugs or any other issues please email
python-etl@googlegroups.com or raise an issue on GitHub.

Sections: petl - Extract, Transform and Load, Resources, Getting Help

</details>

### jsonpath

An XPath for JSON

`pip install jsonpath` · installs from source (sdist only) · licence: MIT License · rank 4262 · last release 2023-08-24 · [PyPI](https://pypi.org/project/jsonpath/)

<details><summary>README extract</summary>

A port of the Perl, and JavaScript versions of JSONPath
see

Based on on JavaScript version by Stefan Goessner at:

and Perl version by Kay Rhodes at:

Python3 compatibily by Per J. Sandstrom

</details>

### urlextract

Collects and extracts URLs from given text.

`pip install urlextract` · installs (wheel) · licence: MIT License · rank 4277 · last release 2026-10-02 · [PyPI](https://pypi.org/project/urlextract/) · [docs](https://urlextract.readthedocs.io/en/latest/) · [source](https://github.com/lipoja/URLExtract)

<details><summary>README extract</summary>

URLExtract is python class for collecting (extracting) URLs from given
text based on locating TLD.

It tries to find any occurrence of TLD in given text. If TLD is found it
starts from that position to expand boundaries to both sides searching
for "stop character" (usually whitespace, comma, single or double
quote). ...

Example:
```python
from urlextract import URLExtract

extractor = URLExtract()
urls = extractor.find_urls("Text with URLs. Let's have URL janlipovsky.cz as an example.")
print(urls) # prints: ['janlipovsky.cz']
```

Sections: URLExtract, How does it work, Documentation, Requirements, Run tox, Example, Known issues

</details>

### flashinfer-cubin

Pre-compiled cubins for FlashInfer

`pip install flashinfer-cubin` · installs (wheel) · licence: Apache Software License · rank 4278 · last release 2026-06-25 · [PyPI](https://pypi.org/project/flashinfer-cubin/) · [docs](https://github.com/flashinfer-ai/flashinfer) · [source](https://github.com/flashinfer-ai/flashinfer)

<details><summary>README extract</summary>

This package contains pre-compiled CUDA kernels (cubins) for FlashInfer. It provides all necessary cubin files downloaded from the FlashInfer artifactory.

</details>

### opensandbox

OpenSandbox Python SDK - Secure, isolated execution environments

`pip install opensandbox` · installs (wheel) · licence: Apache Software License · rank 4279 · last release 2026-10-27 · [PyPI](https://pypi.org/project/opensandbox/) · [docs](https://open-sandbox.ai) · [source](https://github.com/opensandbox-group/OpenSandbox)

<details><summary>README extract</summary>

A Python SDK for low-level interaction with OpenSandbox. It provides capabilities to create, manage, and interact with secure sandbox environments, including executing shell commands, managing files, and monitoring resources.

Example:
```python
import asyncio
from opensandbox.sandbox import Sandbox
from opensandbox.config import ConnectionConfig
from opensandbox.exceptions import SandboxException

async def main():
    # 1. Configure connection
    config = ConnectionConfig(
        domain="api.opensandbox.io",
        api_key="your-api-key"
    )

    # 2. Create a Sandbox
    try:
...
```

...

</details>

### xdoctest

A rewrite of the builtin doctest module

`pip install xdoctest` · installs (wheel) · licence: Apache 2 · rank 4286 · last release 2026-03-27 · [PyPI](https://pypi.org/project/xdoctest/)

<details><summary>README extract</summary>

Xdoctest - Execute doctests. A Python package for executing tests in
documentation strings!

What is a doctest?
It is example code you write in a docstring!
What is a docstring?
Its a string you use as a comment! They get attached to Python functions and
classes as metadata. They are often used to auto-generate documentation. ...

Example:
```python
def func():
    """
    # Old way
    >>> def func():
    ...     print('The old regex-based parser required specific formatting')
    >>> func()
    The old regex-based parser required specific formatting

    # New way
    >>> def func():
    >>>     print('The new ast-based parser lets you prefix all lines with >>>')
    >>> func()
...
```

...

</details>

### delta-sharing

Python Connector for Delta Sharing

`pip install delta-sharing` · installs (wheel) · licence: Apache Software License · rank 4295 · last release 2026-10-29 · [PyPI](https://pypi.org/project/delta-sharing/) · [docs](https://github.com/delta-io/delta-sharing) · [source](https://github.com/delta-io/delta-sharing)

<details><summary>README extract</summary>

Delta Sharing is an open protocol for secure real-time exchange of large datasets, which enables secure data sharing across different computing platforms. It lets organizations share access to existing Delta Lake and Apache Parquet tables with other organizations, who can then directly read the table in Pandas, Apache Spark, or any other software ...

Sections: Delta Sharing, Documentation

</details>

### pipedream

(no summary)

`pip install pipedream` · installs (wheel) · licence: not stated · rank 4305 · last release 2026-10-21 · [PyPI](https://pypi.org/project/pipedream/) · [source](https://github.com/PipedreamHQ/pipedream-sdk-python)

<details><summary>README extract</summary>

The Pipedream Python library provides convenient access to the Pipedream APIs from Python.

Example:
```python
from pipedream import Pipedream

client = Pipedream(
    client_id="<clientId>",
    client_secret="<clientSecret>",
)

client.actions.run(
    id="id",
    external_user_id="external_user_id",
)
```

Sections: Pipedream Python Library, Reference, Usage, Environments, Async Client, Exception Handling, Pagination, Oauth Token Override, Advanced, Access Raw Response Data, Retries, Timeouts, Custom Client

</details>

### elementary-data

Data monitoring and lineage

`pip install elementary-data` · does not install on CPython 3.14 · licence: Apache Software License · rank 4318 · last release 2026-10-11 · [PyPI](https://pypi.org/project/elementary-data/) · [docs](https://docs.elementary-data.com) · [source](https://github.com/elementary-data/elementary)

<details><summary>README extract</summary>

Docs » | Join the Elementary Community »

 ⭐️ Star the repo

Built by the Elementary team, helping you deliver trusted data in the AI era.

Elementary OSS is the open-source CLI for dbt-native data observability. ...

Features:
- Anomaly detection tests - Collect data quality metrics and detect anomalies, as native dbt tests.
- Automated monitors - Out-of-the-box cloud monitors to detect freshness, volume and schema issues. ...

Sections: Elementary OSS: dbt-native data observability, How It Works, Quickstart, Features, #

</details>

### okta

Python SDK for the Okta Management API

`pip install okta` · installs (wheel) · licence: Apache Software License · rank 4320 · last release 2026-10-27 · [PyPI](https://pypi.org/project/okta/)

<details><summary>README extract</summary>

A Python library for the Okta Management APIs.

Getting Started

</details>

### pyasynchat

Make asynchat available for Python 3.12 onwards

`pip install pyasynchat` · installs (wheel) · licence: Python Software Foundation License · rank 4331 · last release 2026-01-05 · [PyPI](https://pypi.org/project/pyasynchat/)

<details><summary>README extract</summary>

This package contains the asynchat module as found in Python versions prior to 3.12.
It is provided so that existing code relying on `import asynchat` is able to continue being used without significant refactoring.

The module's source code is taken directly from the Python standard library<sup id="a1">[[1]](#f1)</sup>. ...

Example:
```python
import asynchat
```

Sections: Purpose, Usage, Maintenance, Footnotes

</details>

### envyaml

Simple YAML configuration file parser with easy access for structured data

`pip install envyaml` · installs (wheel) · licence: MIT License · rank 4341 · last release 2022-01-08 · [PyPI](https://pypi.org/project/envyaml/)

<details><summary>README extract</summary>

Modern configuration files become to be more and more complex, flexible, and readable.
YAML file format is perfect to store configuration but had no option to pass environment variables. They give flexibility, readability and provide an option to store complex data structure. ...

Example:
```python
from envyaml import EnvYAML

# read file env.yaml and parse config
env = EnvYAML('env.yaml')

# access project name
print(env['project.name'])

# >> simple-hello-42

# access whole database section
print(env['database'])

# {
# 'database': 'test',
# 'host': 'xxx.xxx.xxx.xxx',
# 'password': 'super-secret-password',
# 'port': 3301,
# 'table':
# {
...
```

Sections: Motivation, Basic usage, Strict mode, Escaped variables

</details>

### memoization

A powerful caching library for Python, with TTL support and multiple algorithm options. (https://github.com/lonelyenvoy/python-memoization)

`pip install memoization` · installs from source (sdist only) · licence: MIT License · rank 4344 · last release 2021-08-01 · [PyPI](https://pypi.org/project/memoization/)

<details><summary>README extract</summary>

[][repository] [][travis] [][codacy]
[][coveralls] [][repository]

[][pr] [][license] [][python]

A powerful caching library for Python, with TTL support and multiple algorithm options.

If you like this work, please star it on GitHub.

Features:
Perhaps you know about ```functools.lru_cache```
in Python 3, and you may be wondering why we are reinventing the wheel.

Well, actually not. This lib is based on ```functools```. Please find below the comparison with ```lru_cache```. ...

Example:
```python
2. ```lru_cache``` is vulnerable to hash collision attack
   and can be hacked or compromised. Using this technique, attackers can make your program unexpectedly slow by
   feeding the cached function with certain cleverly designed inputs. However, in ```memoization```, caching is always
...
...

</details>

### currency-symbols

Get currency symbol by currency code

`pip install currency-symbols` · installs (wheel) · licence: MIT · rank 4387 · last release 2026-08-01 · [PyPI](https://pypi.org/project/currency-symbols/) · [source](https://github.com/arshadkazmi42/currency-symbols)

<details><summary>README extract</summary>

Get the currency symbol for an ISO 4217 currency code — `USD → $`, `EUR → €`, `INR → ₹`.

- Covers all active ISO 4217 codes, plus common historical, crypto and commodity codes
- Zero dependencies
- Fully typed (PEP 561, ships `py.typed`)
- Python 3.9+

Example:
```python
from currency_symbols import CurrencySymbols

CurrencySymbols.get_symbol("USD")
# '$'

CurrencySymbols.get_symbol("EUR")
# '€'

CurrencySymbols.get_symbol("gbp")
# '£' — codes are case-insensitive

CurrencySymbols.get_symbol("XYZ")
# None — unknown codes return None
```

Sections: currency-symbols :money_with_wings, Usage

</details>

### knockapi

The official Python library for the knock API

`pip install knockapi` · installs (wheel) · licence: Apache Software License · rank 4388 · last release 2026-10-21 · [PyPI](https://pypi.org/project/knockapi/) · [source](https://github.com/knocklabs/knock-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Knock Python library provides convenient access to the Knock REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from knockapi import Knock

client = Knock(
    api_key=os.environ.get("KNOCK_API_KEY"),  # This is the default and can be omitted
)

response = client.workflows.trigger(
    key="dinosaurs-loose",
    recipients=["dnedry"],
    data={"dinosaur": "triceratops"},
)
print(response.workflow_run_id)
```

...

</details>

### pem

PEM file parsing in Python.

`pip install pem` · installs (wheel) · licence: MIT License · rank 4402 · last release 2023-06-21 · [PyPI](https://pypi.org/project/pem/) · [docs](https://pem.readthedocs.io/) · [source](https://github.com/hynek/pem)

<details><summary>README extract</summary>

*pem* is a Python module for parsing and splitting of PEM files, i.e. Base64-encoded DER keys and certificates.

It has no dependencies and does not attempt to interpret the certificate data in any way. ...

Example:
```python
>>> import pem
>>> certs = pem.parse_file("chain.pem")
>>> certs
[<Certificate(PEM string with SHA-1 digest '...')>, <Certificate(PEM string with SHA-1 digest '...')>]
>>> str(certs[0])
'-----BEGIN CERTIFICATE-----\n...'
```

Sections: pem: PEM file parsing for Python, Project Information, pem* for Enterprise, Removed, Added

</details>

### cartesia

The official Python library for the cartesia API

`pip install cartesia` · installs (wheel) · licence: Apache Software License · rank 4403 · last release 2026-09-02 · [PyPI](https://pypi.org/project/cartesia/) · [source](https://github.com/cartesia-ai/cartesia-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Cartesia Python library provides convenient access to the Cartesia REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by
httpx, as well as websockets support powered
by websockets.

Example:
```python
import os
from cartesia import Cartesia

client = Cartesia(
    api_key=os.getenv("CARTESIA_API_KEY"),
)

response = client.tts.generate(
    model_id="sonic-latest",
    output_format={
        "container": "wav",
        "encoding": "pcm_f32le",
        "sample_rate": 44100,
    },
...
```

...

</details>

### pyroute2

Python Netlink library

`pip install pyroute2` · installs (wheel) · licence: GPL-2.0-or-later OR Apache-2.0 · rank 4422 · last release 2026-10-23 · [PyPI](https://pypi.org/project/pyroute2/)

_README extract left out: share-alike licence._

### graphql-server-core

GraphQL Server tools for powering your server

`pip install graphql-server-core` · installs from source (sdist only) · licence: MIT License · rank 4434 · last release 2020-03-17 · [PyPI](https://pypi.org/project/graphql-server-core/)

<details><summary>README extract</summary>

GraphQL-Server-Core is a base library that serves as a helper
for building GraphQL servers or integrations into existing web frameworks using
GraphQL-Core.

| Server integration | Package | ...

Sections: GraphQL-Server-Core, Existing integrations built with GraphQL-Server-Core, Other integrations using GraphQL-Core or Graphene, Documentation

</details>

### plac

The smartest command line arguments parser in the world

`pip install plac` · installs (wheel) · licence: BSD License · rank 4435 · last release 2026-09-07 · [PyPI](https://pypi.org/project/plac/)

<details><summary>README extract</summary>

`plac` is a Python package that can generate command line parameters
from function signatures.

`plac` works on Python 2.6 through all versions of Python 3.

`plac` has no dependencies beyond modules already present in the Python
standard library. ...

Example:
```python
import plac

def main(model, iter=100, debug=False):
    """
    A script for machine learning
    """
    print (model, iter, debug)

if name == 'main':
    # Execute function via plac.call()
    plac.call(main)
```

Sections: Plac: parsing the command line the easy way, Quickstart, Additional customization, Decorator reference, Zero dependencies ... not even plac :-), Avoiding name clashes, Variable arguments, Code, Issues

</details>

### pyDeprecate

Python deprecation decorator: call forwarding, argument mapping, class proxying, CI audit. Zero deps.

`pip install pyDeprecate` · installs (wheel) · licence: Apache-2.0 · rank 4437 · last release 2026-10-20 · [PyPI](https://pypi.org/project/pyDeprecate/) · [docs](https://borda.github.io/pyDeprecate/stable/) · [source](https://github.com/Borda/pyDeprecate)

<details><summary>README extract</summary>

Deprecate Python APIs without breaking existing callers.

Use pyDeprecate when you renamed a function, moved a class, or retired an argument but still need old user code to work during the migration window. ...

Example:
```python
from deprecate import deprecated

# NEW/FUTURE API — renamed to be more explicit about what it computes
def compute_sum(a: int = 0, b: int = 3) -> int:
    return a + b

# DEPRECATED API — `addition` was the original name before the rename
@deprecated(target=compute_sum, deprecated_in="1.0", remove_in="2.0")
...
```

...

</details>

### google-play-scraper

Google-Play-Scraper provides APIs to easily crawl the Google Play Store for Python without any external dependencies!

`pip install google-play-scraper` · installs (wheel) · licence: MIT License · rank 4445 · last release 2024-06-07 · [PyPI](https://pypi.org/project/google-play-scraper/) · [source](https://github.com/JoMingyu/google-play-scraper)

<details><summary>README extract</summary>

Google-Play-Scraper provides APIs to easily crawl the Google Play Store for Python *without any external dependencies!*

> Node.js scraper to get data from Google Play

I have referred a lot to the API design of this library.

Example:
```python
from google_play_scraper import app

result = app(
    'com.nianticlabs.pokemongo',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)
```

Sections: Google-Play-Scraper, Related Projects, google-play-scraper, Usage, App Detail, App Reviews, App All Reviews, App Permissions, App Search, Changes

</details>

### pytest-cases

Separate test code from test cases in pytest.

`pip install pytest-cases` · installs (wheel) · licence: BSD License · rank 4447 · last release 2026-03-02 · [PyPI](https://pypi.org/project/pytest-cases/)

<details><summary>README extract</summary>

Separate test code from test cases in `pytest`.

The documentation for users is available here:

A readme for developers is available here:

</details>

### Flask-GraphQL

Adds GraphQL support to your Flask application

`pip install Flask-GraphQL` · installs from source (sdist only) · licence: MIT License · rank 4448 · last release 2019-12-05 · [PyPI](https://pypi.org/project/Flask-GraphQL/)

<details><summary>README extract</summary>

Adds GraphQL support to your Flask application.

Example:
```python
from flask_graphql import GraphQLView

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Optional, for adding batch query support (used in Apollo-Client)
app.add_url_rule('/graphql/batch', view_func=GraphQLView.as_view('graphql', schema=schema, batch=True))
```

Sections: Flask-GraphQL, Usage

</details>

### wikipedia

Wikipedia API for Python

`pip install wikipedia` · installs from source (sdist only) · licence: MIT License · rank 4449 · last release 2014-11-15 · [PyPI](https://pypi.org/project/wikipedia/)

<details><summary>README extract</summary>

Wikipedia is a Python library that makes it easy to access and parse
data from Wikipedia.

Search Wikipedia, get article summaries, get data like links and images
from a page, and more. Wikipedia wraps the MediaWiki
API so you can focus on using
Wikipedia data, not getting it. ...

Example:
```python
>>> import wikipedia
>>> print wikipedia.summary("Wikipedia")
# Wikipedia (/ˌwɪkɨˈpiːdiə/ or /ˌwɪkiˈpiːdiə/ WIK-i-PEE-dee-ə) is a collaboratively edited, multilingual, free Internet encyclopedia supported by the non-profit Wikimedia Foundation...

>>> wikipedia.search("Barack")
...
```

Sections: Wikipedia, Documentation

</details>

### first

Return the first true value of an iterable.

`pip install first` · installs (wheel) · licence: MIT License · rank 4450 · last release 2019-03-07 · [PyPI](https://pypi.org/project/first/)

<details><summary>README extract</summary>

`first` is an MIT-licensed Python package with a simple function that returns the first true value from an iterable, or `None` if there is none.
If you need more power, you can also supply a `key` function that is used to judge the truth value of the element or a `default` value if `None` doesn’t fit your use case.

N.B. ...

Example:
```python
>>> from first import first
>>> first([0, None, False, [], (), 42])
42
```

Sections: first: The function you always missed in Python, Examples, Usage, Alternatives, Background, 2.0.2 (2019-03-07), 2.0.1 (2013-08-04), 2.0.0 (2012-10-13), 1.0.2 (2012-10-09), 1.0.1 (2012-10-09), 1.0.0 (2012-10-09)

</details>

### cons

An implementation of Lisp/Scheme-like cons in Python.

`pip install cons` · installs (wheel) · licence: not stated · rank 4462 · last release 2025-07-11 · [PyPI](https://pypi.org/project/cons/)

<details><summary>README extract</summary>

An implementation of `cons` in Python.

Features:
* Built-in support for the standard Python ordered sequence types: i.e. `list`, `tuple`, `Iterator`, `OrderedDict`.
* Existing `cons` behavior can be changed and support for new collections can be added through the generic functions `cons.core._car` ...

Example:
```python
>>> from cons import cons, car, cdr
>>> cons(1, [])
[1]

>>> cons(1, ())
(1,)

>>> cons(1, [2, 3])
[1, 2, 3]
```

Sections: Python `cons`, Usage and Design, Features

</details>

### logical-unification

Logical unification in Python

`pip install logical-unification` · installs (wheel) · licence: BSD-3-Clause · rank 4477 · last release 2025-10-20 · [PyPI](https://pypi.org/project/logical-unification/)

<details><summary>README extract</summary>

Logical unification in Python, extensible via dispatch.

Example:
```python
>>> from unification import *
>>> unify(1, 1)
{}
>>> unify(1, 2)
False
>>> x = var()
>>> unify((1, x), (1, 2))
{~x: 2}
>>> unify((x, x), (1, 2))
False
```

Sections: Logical Unification, Examples, Performance and Reliability, About

</details>

### linkml-runtime

Runtime environment for LinkML, the Linked open data modeling language

`pip install linkml-runtime` · installs (wheel) · licence: CC0-1.0 · rank 4486 · last release 2026-10-13 · [PyPI](https://pypi.org/project/linkml-runtime/)

<details><summary>README extract</summary>

Runtime support for linkml generated data classes.

This Python library provides runtime support for LinkML datamodels.

See the LinkML repo for the Python Dataclass Generator which will convert a schema into a Python object model. That model will have dependencies on functionality in this library.

The library also provides ...

Sections: linkml-runtime, About, Notebooks

</details>

### domdf-python-tools

Helpful functions for Python 🐍 🛠️

`pip install domdf-python-tools` · installs (wheel) · licence: MIT License · rank 4495 · last release 2026-10-22 · [PyPI](https://pypi.org/project/domdf-python-tools/) · [docs](https://domdf-python-tools.readthedocs.io/en/latest) · [source](https://github.com/domdfcoding/domdf_python_tools)

<details><summary>README extract</summary>

Helpful functions for Python 🐍 🛠️

Note: Before version 3 `domdf_python_tools` was licensed under the LGPLv3+.
Version 3 and later are licensed under the MIT License.

`domdf_python_tools` can be installed from PyPI or Anaconda.

To install with `pip`:

To install with `conda`:

</details>

### flake8-print

print statement checker plugin for flake8

`pip install flake8-print` · installs (wheel) · licence: MIT License · rank 4507 · last release 2022-04-30 · [PyPI](https://pypi.org/project/flake8-print/) · [source](https://github.com/jbkahn/flake8-print)

<details><summary>README extract</summary>

Check for Print statements in python files.

This module provides a plugin for ``flake8``, the Python code checker.

Installation

You can install or upgrade ``flake8-print`` with these commands::

 $ pip install flake8-print
 $ pip install --upgrade flake8-print

Plugin for Flake8 ...

Sections: Flake8 print plugin, 5.0.0 - 2022-04-30, 4.0.1 - 2022-04-30, 4.0.0 - 2020-11-29, 3.1.4 - 2019-1-11, 3.1.3 - 2019-31-10, 3.1.1 - 2019-03-12, 3.1.0 - 2018-02-11, 3.0.1 - 2017-11-06, 3.0.0 - 2017-11-05, 2.0.2 - 2016-02-29, 2.0.1 - 2015-11-21, 2.0 - 2015-11-10, 1.6.1 - 2015-05-22

</details>

### linq-python

The official Python library for the linq-api-v3 API

`pip install linq-python` · installs (wheel) · licence: Apache Software License · rank 4510 · last release 2026-11-06 · [PyPI](https://pypi.org/project/linq-python/) · [source](https://github.com/linq-team/linq-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Linq API V3 Python library provides convenient access to the Linq API V3 REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from linq import LinqAPIV3

client = LinqAPIV3(
    api_key=os.environ.get("LINQ_API_V3_API_KEY"),  # This is the default and can be omitted
)

chat = client.chats.create(
    from="+12052535597",
    message={},
    to=["+12052532136"],
)
print(chat.chat)
```

...

</details>

### metronome-sdk

The official Python library for the metronome API

`pip install metronome-sdk` · installs (wheel) · licence: Apache Software License · rank 4512 · last release 2026-10-27 · [PyPI](https://pypi.org/project/metronome-sdk/) · [source](https://github.com/Metronome-Industries/metronome-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Metronome Python library provides convenient access to the Metronome REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from metronome import Metronome

client = Metronome(
    bearer_token=os.environ.get("METRONOME_BEARER_TOKEN"),  # This is the default and can be omitted
)

client.v1.usage.ingest(
    usage=[
        {
            "transaction_id": "90e9401f-0f8c-4cd3-9a9f-d6beb56d8d72",
            "customer_id": "team@example.com",
...
```

...

</details>

### graphene-pydantic

Graphene Pydantic integration

`pip install graphene-pydantic` · installs (wheel) · licence: Apache Software License · rank 4518 · last release 2024-02-01 · [PyPI](https://pypi.org/project/graphene-pydantic/) · [source](https://github.com/graphql-python/graphene-pydantic)

<details><summary>README extract</summary>

A Pydantic integration for Graphene.

Example:
```python
import uuid
import pydantic

class PersonModel(pydantic.BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str
```

Sections: graphene-pydantic, Examples, Input Object Types, Custom resolve functions, Forward declarations and circular references, Full Examples, Third Party Code, Caveats, Mappings, Union types, Unions between subclasses don't work in Python 3.6

</details>

### pywinauto

A set of Python modules to automate the Microsoft Windows GUI

`pip install pywinauto` · installs (wheel) · licence: BSD License · rank 4520 · last release 2025-01-06 · [PyPI](https://pypi.org/project/pywinauto/)

<details><summary>README extract</summary>

At it's simplest it allows you to send mouse and keyboard
actions to windows dialogs and controls, but it has support for more complex
controls also.

Useful links

</details>

### taskcluster

Python client for Taskcluster

`pip install taskcluster` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 4526 · last release 2026-11-04 · [PyPI](https://pypi.org/project/taskcluster/) · [docs](https://docs.taskcluster.net) · [source](https://github.com/taskcluster/taskcluster)

<details><summary>README extract</summary>

A Taskcluster client library for Python.

This library is a complete interface to Taskcluster in Python. It provides
both synchronous and asynchronous interfaces for all Taskcluster API methods.

Example:
```python
import taskcluster

index = taskcluster.Index(
    {
        "rootUrl": "
        "credentials": {"clientId": "id", "accessToken": "accessToken"},
    }
)
```

Sections: Taskcluster Client for Python, Usage, Setup, Authentication Options, Other Options, Calling API Methods, Generating URLs, Generating Temporary Credentials, Handling Timestamps, Generating SlugIDs, Scope Analysis, Pagination, Pulse Events, Logging

</details>

### rumdl

A fast Markdown linter and formatter written in Rust

`pip install rumdl` · installs (wheel) · licence: MIT License · rank 4530 · last release 2026-10-28 · [PyPI](https://pypi.org/project/rumdl/) · [docs](https://rumdl.dev) · [source](https://github.com/rvben/rumdl.git)

<details><summary>README extract</summary>

One fast native binary for checking and formatting Markdown, with broad
markdownlint configuration compatibility and built-in support for modern
Markdown flavors.

| Get Started
| Docs
| Rules
| Configuration
| Markdown Flavors
| vs markdownlint |

Features:
rumdl helps authors and maintainers keep Markdown consistent without pulling
slow feedback out of the editor and CI loop. Inspired by
Ruff, it combines linting, formatting,
caching, and editor integration in a single tool. ...

Sections: rumdl, Clean Markdown. Fast., Quick Start, Overview, Performance, Using winget (Windows), Using Homebrew (macOS/Linux), Using Cargo (Rust), Using npm, Using pip (Python), Using uv, Using mise, Using Nix (macOS/Linux), Using Termux User Repository (TUR) (Android)

</details>

### async-interrupt

Context manager to raise an exception when a future is done

`pip install async-interrupt` · installs (wheel) · licence: Apache Software License · rank 4537 · last release 2025-02-22 · [PyPI](https://pypi.org/project/async-interrupt/) · [source](https://github.com/bluetooth-devices/async_interrupt)

<details><summary>README extract</summary>

Interrupt context manager for asyncio.

This module provides a context manager that can be used to interrupt
a block of code as soon as possible when a future is done.

The purpose is to raise as soon as possible to avoid any race conditions.

This is based loosely on async_timeout by Andrew Svetlov and cpython asyncio.timeout

Example:
```python
async with interrupt(future, ValueError, "message"):
    future.set_result(None)
    await asyncio.sleep(0)
```

Sections: async_interrupt, Usage

</details>

### pynetbox

NetBox API client library

`pip install pynetbox` · installs (wheel) · licence: Apache-2.0 · rank 4539 · last release 2026-10-08 · [PyPI](https://pypi.org/project/pynetbox/) · [source](https://github.com/netbox-community/pynetbox)

<details><summary>README extract</summary>

Python API client library for NetBox.

> Note: Version 6.7 and later of the library only supports NetBox 3.3 and above.

Each pyNetBox Version listed below has been tested with its corresponding NetBox Version.

| NetBox Version | Plugin Version | ...

Example:
```python
import pynetbox
nb = pynetbox.api(
    '
    token='d6f4e314a5b5fefd164995169f28ae32d987704f'
)
```

Sections: Pynetbox, Compatibility, Quick Start, Queries, Threading, Filters validation, Running Tests

</details>

### jsonasobj2

JSON as python objects - version 2

`pip install jsonasobj2` · installs (wheel) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication · rank 4550 · last release 2021-06-02 · [PyPI](https://pypi.org/project/jsonasobj2/)

### mecab-python3

Python wrapper for the MeCab morphological analyzer for Japanese

`pip install mecab-python3` · installs (wheel) · licence: BSD License · rank 4558 · last release 2025-11-25 · [PyPI](https://pypi.org/project/mecab-python3/)

<details><summary>README extract</summary>

This is a Python wrapper for the MeCab morphological analyzer for Japanese
text. It currently works with Python 3.8 and greater.

Note: If using MacOS Big Sur, you'll need to upgrade pip to version 20.3 or
higher to use wheels due to a pip issue.

issueを英語で書く必要はありません。 ...

Example:
```python
>>> import MeCab
>>> wakati = MeCab.Tagger("-Owakati")
>>> wakati.parse("pythonが大好きです").split()
['python', 'が', '大好き', 'です']

>>> tagger = MeCab.Tagger()
>>> print(tagger.parse("pythonが大好きです"))
python  python  python  python  名詞-普通名詞-一般
が      ガ      ガ      が      助詞-格助詞
大好き  ダイスキ        ダイスキ        大好き  形状詞-一般
...
```

Sections: Basic usage, Dictionaries, Common Issues, Windows Redistributable, Specifying a mecabrc, Alternatives, Licensing

</details>

### retell-sdk

The official Python library for the retell API

`pip install retell-sdk` · installs (wheel) · licence: Apache Software License · rank 4560 · last release 2026-11-07 · [PyPI](https://pypi.org/project/retell-sdk/) · [source](https://github.com/RetellAI/retell-python-sdk)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Retell Python library provides convenient access to the Retell REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx. ...

Example:
```python
import os
from retell import Retell

client = Retell(
    api_key=os.environ.get("RETELL_API_KEY"),  # This is the default and can be omitted
)

agent_response = client.agent.create(
    response_engine={
        "llm_id": "llm_234sdertfsdsfsdf",
        "type": "retell-llm",
    },
    voice_id="retell-Cimo",
)
print(agent_response.agent_id)
```

...

</details>

### asyncua

Pure Python OPC-UA client and server library

`pip install asyncua` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 4569 · last release 2026-10-06 · [PyPI](https://pypi.org/project/asyncua/) · [source](https://github.com/FreeOpcUa/opcua-asyncio)

_README extract left out: share-alike licence._

### dict2xml

Small utility to convert a python dictionary into an XML string

`pip install dict2xml` · installs (wheel) · licence: MIT · rank 4584 · last release 2026-01-14 · [PyPI](https://pypi.org/project/dict2xml/)

<details><summary>README extract</summary>

Super Simple utility to convert a python dictionary into an xml string

Example:
```python
from dict2xml import dict2xml

data = {
  'a': 1,
  'b': [2, 3],
  'c': {
    'd': [
      {'p': 9},
      {'o': 10}
    ],
    'e': 7
  }
}

print dict2xml(data, wrap="all", indent="  ")
```

Sections: dict2xml, example, Output, methods, Self closing tags, Limitations

</details>

### monty

Monty is the missing complement to Python.

`pip install monty` · installs (wheel) · licence: MIT License · rank 4585 · last release 2026-10-20 · [PyPI](https://pypi.org/project/monty/)

<details><summary>README extract</summary>

Monty is the missing complement to Python. It implements supplementary
utilities that are not part of the standard library: transparent support for
compressed files, JSON/YAML/msgpack serialization of arbitrary objects, design
patterns such as `cached_class`, deprecation helpers, and many more. ...

Features:
Transparent compressed I/O. `zopen` opens plain, `.gz`, `.bz2`, `.xz` and
`.lzma` files with one call; `reverse_readline` reads large files from the end.

Serialization of arbitrary objects. ...

Example:
```python
from monty.io import reverse_readline, zopen

with zopen("OUTCAR.gz", mode="rt", encoding="utf-8") as f:
    for line in reverse_readline(f):
        if "TOTAL-FORCE" in line:
            break
```

Sections: Monty: Python Made Even Easier, Highlights

</details>

### ncclient

Python library for NETCONF clients

`pip install ncclient` · installs (wheel) · licence: Apache-2.0 · rank 4596 · last release 2026-03-15 · [PyPI](https://pypi.org/project/ncclient/) · [docs](https://ncclient.readthedocs.io/) · [source](https://github.com/ncclient/ncclient)

<details><summary>README extract</summary>

ncclient is a Python library that facilitates client-side scripting and
application development around the NETCONF protocol. `ncclient` was
developed by `Shikar Bhushan < It is now
maintained by `Leonidas Poulopoulos (@leopoul) <
and `Einar Nilsen-Nygaard (@einarnn)`.

Docs:

Github:

- Python 2.7 or Python 3.4+
- setuptools 0.6+
- Paramiko 1.7+ ...

Example:
```python
from ncclient import manager

with manager.connect(host=host, port=830, username=user, hostkey_verify=False) as m:
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % host, 'w') as f:
        f.write(c)
```

Sections: ncclient: Python library for NETCONF clients, Requirements, Examples, Usage, Get device running config, Changes \| brief

</details>

### adbutils

Pure Python Adb Library

`pip install adbutils` · installs (wheel) · licence: MIT · rank 4602 · last release 2025-11-12 · [PyPI](https://pypi.org/project/adbutils/)

### django-cte

Common Table Expressions (CTE) for Django

`pip install django-cte` · installs (wheel) · licence: BSD-3-Clause · rank 4603 · last release 2026-10-27 · [PyPI](https://pypi.org/project/django-cte/)

<details><summary>README extract</summary>

Sections: Common Table Expressions with Django, Documentation, Running tests, Publishing a new verison to PyPI

</details>

### frictionless

Data management framework for Python that provides functionality to describe, extract, validate, and transform tabular data

`pip install frictionless` · installs (wheel) · licence: MIT · rank 4605 · last release 2026-10-15 · [PyPI](https://pypi.org/project/frictionless/)

<details><summary>README extract</summary>

Data management framework for Python that provides functionality to describe, extract, validate, and transform tabular data (DEVT Framework). It supports a great deal of data sources and formats, as well as provides popular platforms integrations. The framework is powered by the lightweight yet comprehensive Frictionless Standards.

Features:
- Open Source (MIT)
- Powerful Python framework
- Convenient command-line interface
- Low memory consumption for data of any size
- Reasonable performance on big data
- Support for compressed files
- Custom checks and formats ...

Sections: frictionless-py, Purpose, Features, Example, Documentation

</details>

### icmplib

Easily forge ICMP packets and make your own ping and traceroute.

`pip install icmplib` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 4610 · last release 2023-10-10 · [PyPI](https://pypi.org/project/icmplib/)

_README extract left out: share-alike licence._

### graphene-sqlalchemy

Graphene SQLAlchemy integration

`pip install graphene-sqlalchemy` · installs (wheel) · licence: MIT · rank 4623 · last release 2020-06-04 · [PyPI](https://pypi.org/project/graphene-sqlalchemy/)

<details><summary>README extract</summary>

Please read
UPGRADE-v2.0.md
to learn how to upgrade to Graphene `2.0`.

A SQLAlchemy integration for
Graphene.

Example:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserModel(Base):
    tablename = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
```

Sections: Graphene-SQLAlchemy, Examples

</details>

### pyenchant

Python bindings for the Enchant spellchecking system

`pip install pyenchant` · installs (wheel) · licence: LGPL · rank 4624 · last release 2025-09-14 · [PyPI](https://pypi.org/project/pyenchant/) · [source](https://github.com/pyenchant/pyenchant)

_README extract left out: share-alike licence._

### pluginbase

PluginBase is a module for Python that enables the development of flexible plugin systems in Python.

`pip install pluginbase` · installs from source (sdist only) · licence: BSD License · rank 4643 · last release 2021-05-16 · [PyPI](https://pypi.org/project/pluginbase/)

<details><summary>README extract</summary>

PluginBase is a module for Python that enables the development of flexible plugin systems in Python.

Step 1:

Step 2:

Step 3:

Or alternatively:

Example:
```python
from pluginbase import PluginBase
plugin_base = PluginBase(package='yourapplication.plugins')
```

</details>

### PyGObject

Python bindings for GObject Introspection

`pip install PyGObject` · installs from source (sdist only) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 4661 · last release 2026-10-09 · [PyPI](https://pypi.org/project/PyGObject/) · [source](https://gitlab.gnome.org/GNOME/pygobject.git)

_README extract left out: share-alike licence._

### izulu

The exceptional library

`pip install izulu` · installs (wheel) · licence: MIT License · rank 4666 · last release 2026-09-03 · [PyPI](https://pypi.org/project/izulu/) · [docs](https://izulu.readthedocs.io/en/latest/) · [source](https://github.com/pyctrl/izulu)

<details><summary>README extract</summary>

*"The exceptional library"*


Installation

For Python versions prior to 3.11 also install `izulu[compatibility]`.

You can read docs *from top to bottom* or jump straight into "Quickstart" section.
For details note "Specifications" sections below.

Features:
The `izulu error class behaviour is controlled by _features__` class attribute.

(For details about "runtime" and "class definition" stages
see Validation and behavior in case of problems below)

Example:
```python
if not data:
    raise ValueError("Data is invalid: no data")

amount = data["amount"]
if amount < 0:
    raise ValueError(f"Data is invalid: amount can't be negative ({amount})")
elif amount > 1000:
    raise ValueError(f"Data is invalid: amount is too large ({amount})")

if data["status"] not in {"READY", "IN_PROGRESS"}:
...

</details>

### requests-pkcs12

Add PKCS#12 support to the requests library in a clean way, without monkey patching or temporary files

`pip install requests-pkcs12` · installs (wheel) · licence: ISC License (ISCL) · rank 4681 · last release 2025-09-07 · [PyPI](https://pypi.org/project/requests-pkcs12/)

<details><summary>README extract</summary>

Example:
```python
from requests_pkcs12 import get

r = get(' pkcs12_filename='clientcert.p12', pkcs12_password='correcthorsebatterystaple')
```

Sections: Usage, Arguments

</details>

### ibm-platform-services

Python client library for IBM Cloud Platform Services

`pip install ibm-platform-services` · installs (wheel) · licence: Apache Software License · rank 4690 · last release 2026-10-29 · [PyPI](https://pypi.org/project/ibm-platform-services/) · [docs](https://github.com/IBM/platform-services-python-sdk/blob/main/README.md) · [source](https://github.com/IBM/platform-services-python-sdk)

<details><summary>README extract</summary>

Python client library to interact with various
IBM Cloud Platform Service APIs.

Features:
The IBM Cloud Platform Services Python SDK allows developers to programmatically interact with the following
IBM Cloud services:

Service Name | Module Name | Service Class Name ...

Sections: IBM Cloud Platform Services Python SDK Version 0.77.2, Overview, Prerequisites, Using the SDK, Questions, Issues, Open source @ IBM

</details>

### rdflib-jsonld

rdflib extension adding JSON-LD parser and serializer

`pip install rdflib-jsonld` · installs (wheel) · licence: BSD License · rank 4693 · last release 2021-09-18 · [PyPI](https://pypi.org/project/rdflib-jsonld/)

<details><summary>README extract</summary>

*This rdflib plugin is deprecated
for, as of the 2021-09-17 release of rdflib 6.0.1, JSON-LD handing has been
integrated. All functionality in this package has been removed, as of release 0.6.2.*

*This plugin is now 'tombstoned' meaning this - 0.6.2 - is a final release and
all users of Python > 3.6 are encouraged to move to rdflib > 6.0.1.* ...

Example:
```python
>>> from rdflib import Graph, plugin
>>> from rdflib.serializer import Serializer

>>> testrdf = """
... @prefix dcterms: < .
... <
...     dcterms:title "Someone's Homepage"@en .
... """

>>> g = Graph().parse(data=testrdf, format='n3')

>>> print(g.serialize(format='json-ld', indent=4))
{
    "@id": "
    " [
        {
...
```

...

</details>

### pyexcel

A wrapper library that provides one API to read, manipulate and writedata in different excel formats

`pip install pyexcel` · installs (wheel) · licence: New BSD · rank 4700 · last release 2026-06-29 · [PyPI](https://pypi.org/project/pyexcel/)

<details><summary>README extract</summary>

Features:
1. One application programming interface(API) to handle multiple data sources:

 * physical file
 * memory file
 * SQLAlchemy table
 * Django Model
 * Python data structures: dictionary, records and array

2. ...

Example:
```python
>>> records = p.get_records(file_name="your_file.xls")
```

Sections: pyexcel - Let you focus on data, instead of file formats, Known constraints, Introduction, Feature Highlights, One liners, Read from the excel files, Get a list of dictionaries, Get two dimensional array, Get a dictionary, Get a dictionary of two dimensional array, Write data, Export an array, Export a list of dictionaries, Export a dictionary of single key value pair

</details>

### whisper-normalizer

A python package for whisper normalizer

`pip install whisper-normalizer` · installs (wheel) · licence: MIT · rank 4703 · last release 2026-10-31 · [PyPI](https://pypi.org/project/whisper-normalizer/) · [docs](https://kurianbenoy.github.io/whisper_normalizer) · [source](https://github.com/kurianbenoy/whisper_normalizer)

<details><summary>README extract</summary>

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

> A python package for text standardisation/normalization. It uses normalization algorithm mentioned in OpenAI whisper paper. Using Whisper normalization can cause issues in Indic languages and other low resource languages when using `BasicTextNormalizer`. ...

Features:
- In ASR systems it’s important to normalize the text to reduce unintentional penalties in
 metrics like WER, CER etc.
- Text normalization/standardization is process of converting texts in different styles into a standardized form, which is a ...

Example:
```python
from whisper_normalizer.english import EnglishTextNormalizer

english_normalizer = EnglishTextNormalizer()
english_normalizer("I'm a little teapot, short and stout. Tip me over and pour me out!")
...

</details>

### razorpay

Razorpay Python Client

`pip install razorpay` · installs (wheel) · licence: MIT License · rank 4707 · last release 2026-03-09 · [PyPI](https://pypi.org/project/razorpay/)

<details><summary>README extract</summary>

Python bindings for interacting with the Razorpay API

This is primarily meant for merchants who wish to perform interactions with the Razorpay API programatically.

Example:
```python
import razorpay
client = razorpay.Client(auth=("<YOUR_API_KEY>", "<YOUR_API_SECRET>"))

client.enable_retry(True)  # Enable retry mechanism for failed API calls
```

Sections: Razorpay Python Client, Usage, App Details, Bugs? Feature requests? Pull requests?

</details>

### cbor

RFC 7049 - Concise Binary Object Representation

`pip install cbor` · installs from source (sdist only) · licence: Apache Software License · rank 4720 · last release 2016-02-09 · [PyPI](https://pypi.org/project/cbor/)

<details><summary>README extract</summary>

An implementation of RFC 7049 - Concise Binary Object Representation (CBOR).

CBOR is comparable to JSON, has a superset of JSON's ability, but serializes to a binary format which is smaller and faster to generate and parse.

The two primary functions are cbor.loads() and cbor.dumps(). ...

</details>

### b2sdk

Backblaze B2 SDK

`pip install b2sdk` · installs (wheel) · licence: MIT License · rank 4744 · last release 2026-11-06 · [PyPI](https://pypi.org/project/b2sdk/)

<details><summary>README extract</summary>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

This repository contains a client library and a few handy utilities for easy access to all of the capabilities of B2 Cloud Storage.

B2 command-line tool is an example of how it can be used to provide command-line access to the B2 service, but there are many possible applications (including FUSE filesystems, storage ...

Sections: B2 Python SDK, Documentation, Version policy

</details>

### pyecharts

Python options, make charting easier

`pip install pyecharts` · installs (wheel) · licence: MIT License · rank 4750 · last release 2026-02-10 · [PyPI](https://pypi.org/project/pyecharts/)

### smithy-core

Core components for implementing Smithy tooling in Python.

`pip install smithy-core` · installs (wheel) · licence: Apache Software License · rank 4760 · last release 2026-10-08 · [PyPI](https://pypi.org/project/smithy-core/) · [source](https://github.com/smithy-lang/smithy-python/blob/develop/packages/smithy-core/)

<details><summary>README extract</summary>

This is the core package that provides foundational SDK interfaces for both client and server
tooling generated by Smithy.

</details>

### browsermob-proxy

A library for interacting with the Browsermob Proxy

`pip install browsermob-proxy` · installs from source (sdist only) · licence: Apache Software License · rank 4778 · last release 2017-02-07 · [PyPI](https://pypi.org/project/browsermob-proxy/)

### nanobind-backend

Compiled nanobind backend for extensions built in split mode

`pip install nanobind-backend` · installs (wheel) · licence: BSD License · rank 4781 · last release 2026-08-22 · [PyPI](https://pypi.org/project/nanobind-backend/) · [docs](https://nanobind.readthedocs.io/en/latest/split_mode.html)

<details><summary>README extract</summary>

This package contains the backend part of the
nanobind C++ binding library. It serves
extension modules built using nanobind's *split mode*, in which the extension
delegates to an externally hosted backend instead of shipping its own. ...

</details>

### aws-sdk-signers

Standalone HTTP Request Signers for Amazon Web Services

`pip install aws-sdk-signers` · installs (wheel) · licence: Apache Software License · rank 4784 · last release 2026-10-08 · [PyPI](https://pypi.org/project/aws-sdk-signers/) · [source](https://github.com/smithy-lang/smithy-python/blob/develop/packages/aws-sdk-signers/)

<details><summary>README extract</summary>

AWS SDK Signers for Python provides stand-alone signing functionality. This enables users to
create standardized request signatures (currently only SigV4) and apply them to
common HTTP utilities like AIOHTTP, Curl, Postman, Requests and urllib3.

This project is currently in an Alpha phase of development. ...

Sections: AWS SDK Signers for Python, Getting Started

</details>

### yarg

A semi hard Cornish cheese, also queries PyPI (PyPI client)

`pip install yarg` · installs (wheel) · licence: MIT License · rank 4792 · last release 2024-08-09 · [PyPI](https://pypi.org/project/yarg/)

<details><summary>README extract</summary>

Yarg is a PyPI client.

Full documentation is at <

Yarg is released under the MIT license. The source code is on
GitHub and issues are also tracked on
GitHub.

Example:
```python
>>> import yarg
>>> package = yarg.get("yarg")
>>> package.name
u'yarg'
>>> package.author
Author(name=u'Kura', email=u'kura@kura.io')
```

Sections: yarg(1) -- A semi hard Cornish cheese, also queries PyPI, 0.1.9 (2014-08-11), Splatting bugs, 0.1.8 (2014-08-10), 0.1.6 & 0.1.7 (2014-08-10), 0.1.5 (2014-08-10), API changes, 0.1.4 (2014-08-09), Other, 0.1.2 (2014-08-08)

</details>

### smithy-http

HTTP components for Smithy tooling.

`pip install smithy-http` · installs (wheel) · licence: Apache Software License · rank 4793 · last release 2026-10-08 · [PyPI](https://pypi.org/project/smithy-http/) · [source](https://github.com/smithy-lang/smithy-python/blob/develop/packages/smithy-http/)

<details><summary>README extract</summary>

This package provides primitives and interfaces for http functionality in tooling generated by Smithy.

Example:
```python
from smithy_http.testing import MockHTTPClient

# Create mock client and configure responses
mock_client = MockHTTPClient()
mock_client.add_response(
   status=200,
   headers=[("Content-Type", "application/json")],
   body=b'{"message": "success"}'
)

# Use with your smithy-python client
config = Config(transport=mock_client)
...
```

Sections: smithy-http, MockHTTPClient, Basic Usage, Utilities

</details>

### logfury

('Toolkit for responsible, low-boilerplate logging of library method calls',)

`pip install logfury` · installs (wheel) · licence: BSD License · rank 4794 · last release 2021-10-23 · [PyPI](https://pypi.org/project/logfury/)

<details><summary>README extract</summary>

Logfury is a tool for python library maintainers. It allows for responsible, low-boilerplate logging of method calls.

If you were to use logfury in your library, any change to the API could potentially break your program. Nobody wants that.

Thanks to this import trick I can keep the API very stable. ...

Example:
```python
from logfury.v1 import DefaultTraceMeta
```

Sections: Logfury, whats with the weird import, Current stable, Basic usage, DefaultTraceMeta metaclass, trace_call decorator

</details>

### smithy-aws-core

Core Smithy components for AWS services and protocols.

`pip install smithy-aws-core` · installs (wheel) · licence: Apache Software License · rank 4795 · last release 2026-10-08 · [PyPI](https://pypi.org/project/smithy-aws-core/) · [source](https://github.com/smithy-lang/smithy-python/blob/develop/packages/smithy-aws-core/)

<details><summary>README extract</summary>

This is the core package that provides AWS specific interfaces for both client and server
tooling generated by Smithy.

</details>

### linkml

Linked Open Data Modeling Language

`pip install linkml` · installs (wheel) · licence: Apache-2.0 · rank 4812 · last release 2026-10-13 · [PyPI](https://pypi.org/project/linkml/)

<details><summary>README extract</summary>

LinkML is a linked data modeling language following object-oriented and ontological principles. LinkML models are typically authored in YAML, and can be converted to other schema representation formats such as JSON or RDF.

This repo holds the tools for generating and working with LinkML. For the LinkML schema (metamodel), please see ...

</details>

### smithy-json

JSON serialization and deserialization support for Smithy tooling.

`pip install smithy-json` · installs (wheel) · licence: Apache Software License · rank 4815 · last release 2026-08-20 · [PyPI](https://pypi.org/project/smithy-json/) · [source](https://github.com/smithy-lang/smithy-python/blob/develop/packages/smithy-json/)

<details><summary>README extract</summary>

This package provides generic JSON serialization and deserialization support
for Smithy clients and servers.

</details>

### cosmic-ray

Mutation testing

`pip install cosmic-ray` · installs (wheel) · licence: MIT License · rank 4816 · last release 2026-11-08 · [PyPI](https://pypi.org/project/cosmic-ray/) · [source](https://github.com/sixty-north/cosmic-ray)

### hyperscan

Python bindings for Hyperscan.

`pip install hyperscan` · installs (wheel) · licence: MIT License · rank 4825 · last release 2026-10-08 · [PyPI](https://pypi.org/project/hyperscan/) · [docs](https://python-hyperscan.readthedocs.io/en/latest/) · [source](https://github.com/darvid/python-hyperscan)

<details><summary>README extract</summary>

A CPython extension for Vectorscan, an open source fork of
Hyperscan, Intel's open source (prior to version 5.4),
high-performance multiple regex matching library.

* ✅ Binary manylinux-compatible wheels
* ✅ Statically linked (no need to build Hyperscan/Vectorscan)
* ✅ Chimera support

Sections: Hyperscan/Vectorscan for Python, Build Optimization, Resources

</details>

### unittest2

The new features in unittest backported to Python 2.4+.

`pip install unittest2` · installs (wheel) · licence: BSD License · rank 4837 · last release 2015-06-30 · [PyPI](https://pypi.org/project/unittest2/)

<details><summary>README extract</summary>

unittest2 is a backport of the new features added to the unittest testing
framework in Python 2.7 and onwards. It is tested to run on Python 2.6, 2.7,
3.2, 3.3, 3.4 and pypy.

To use unittest2 instead of unittest simply replace `import unittest` with
`import unittest2`.

unittest2 is maintained in a mercurial repository. ...

Sections: Differences, Issues, 2015-06-20 - 1.1.0, 2015-03-12 - 1.0.1, 2015-03-06 - 1.0.0, 2014/11/05 - 0.8, 2014/10/31 - 0.7.1, 2014/10/31 - 0.7.0, 2014/10/28 - 0.6.0, 2010/07/12 - 0.5.1, 2010/07/11 - 0.5.0, 2010/06/06 - 0.4.2, 2010/05/09 - 0.4.1, 2010/04/08 - 0.4.0

</details>

### types-botocore

Proxy package for botocore-stubs

`pip install types-botocore` · installs (wheel) · licence: MIT License · rank 4874 · last release 2022-04-01 · [PyPI](https://pypi.org/project/types-botocore/) · [docs](https://mypy-boto3-builder.readthedocs.io/en/latest/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Sections: VSCode extension, From PyPI with pip, From conda-forge, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, How it works, What's new, Implemented features

</details>

### swagger-spec-validator

Validation of Swagger specifications

`pip install swagger-spec-validator` · installs (wheel) · licence: Apache License, Version 2.0 · rank 4896 · last release 2024-06-27 · [PyPI](https://pypi.org/project/swagger-spec-validator/)

<details><summary>README extract</summary>

Swagger Spec Validator is a Python library that validates Swagger Specs against the Swagger 1.2 or Swagger 2.0 specification. The validator aims to check for full compliance with the Specification.

Example:
```python
from swagger_spec_validator import validate_spec_url

# example for swagger spec v1.2
validate_spec_url('

# example for swagger spec v2.0
validate_spec_url('
```

Sections: swagger\_spec\_validator, About, Example Usage, Documentation

</details>

### libusb1

Pure-python wrapper for libusb-1.0

`pip install libusb1` · installs (wheel) · licence: LGPL-2.1-or-later · rank 4901 · last release 2026-05-16 · [PyPI](https://pypi.org/project/libusb1/)

_README extract left out: share-alike licence._

### partialjson

Parse incomplete or partial JSON, e.g. from a streaming LLM response

`pip install partialjson` · installs (wheel) · licence: MIT License · rank 4902 · last release 2026-09-11 · [PyPI](https://pypi.org/project/partialjson/) · [source](https://github.com/iw4p/partialjson)

<details><summary>README extract</summary>

Example:
```python
from partialjson import JSONParser
parser = JSONParser()

incomplete_json = '{"name": "John Doe", "age": 30, "is_student": false, "courses": ["Math", "Science"'
print(parser.parse(incomplete_json))
# {'name': 'John Doe', 'age': 30, 'is_student': False, 'courses': ['Math', 'Science']}
```

Sections: PartialJson, Parse Partial and incomplete JSON in python, Example, What you get while a string is still streaming, Extra tokens, How can I use it?, Issues

</details>

### pymongo-search-utils

Utility library for working with vector search in MongoDB using PyMongo

`pip install pymongo-search-utils` · installs (wheel) · licence: BSD License · rank 4904 · last release 2026-09-22 · [PyPI](https://pypi.org/project/pymongo-search-utils/)

<details><summary>README extract</summary>

A utility library for working with vector search in MongoDB using PyMongo.

</details>

### apache-libcloud

A standard Python library that abstracts away differences among multiple cloud provider APIs. For more information and documentation, please see https://libcloud.apache.org

`pip install apache-libcloud` · installs (wheel) · licence: Apache Software License · rank 4907 · last release 2026-04-21 · [PyPI](https://pypi.org/project/apache-libcloud/) · [docs](https://libcloud.readthedocs.io) · [source](https://github.com/apache/libcloud)

<details><summary>README extract</summary>

Apache Libcloud is a Python library which hides differences between different
cloud provider APIs and allows you to manage different cloud resources
through a unified and easy to use API. ...

Sections: Apache Libcloud - a unified interface for the cloud, Documentation, Note on Python Version Compatibility, Feedback, Website, Reporting a Vulnerability

</details>

### systemd-python

Python interface for libsystemd

`pip install systemd-python` · installs from source (sdist only) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 4910 · last release 2023-02-11 · [PyPI](https://pypi.org/project/systemd-python/)

_README extract left out: share-alike licence._

### pika-stubs

Mypy plugin and stubs for Pika

`pip install pika-stubs` · installs from source (sdist only) · licence: MIT License · rank 4918 · last release 2020-06-10 · [PyPI](https://pypi.org/project/pika-stubs/)

<details><summary>README extract</summary>

This package contains type stubs to provide more precise static types and type inference for pika, the RabbitMQ client library.

</details>

### kerberos

Kerberos high-level interface

`pip install kerberos` · installs from source (sdist only) · licence: Apache Software License · rank 4923 · last release 2021-01-09 · [PyPI](https://pypi.org/project/kerberos/)

<details><summary>README extract</summary>

This Python package is a high-level wrapper for Kerberos (GSSAPI)
operations. The goal is to avoid having to build a module that wraps
the entire Kerberos.framework, and instead offer a limited set of
functions that do what is needed for client/server Kerberos
authentication based on < ...

Example:
```python
import hashlib

def get_channel_bindings_application_data(socket):
    # This is a highly simplified example, there are other use cases
    # where you might need to use different hash types or get a socket
    # object somehow.
    server_certificate = socket.getpeercert(True)
...
```

Sections: PyKerberos Package, Build, IMPORTANT, Channel Bindings, Python APIs

</details>

### awesomeversion

One version package to rule them all, One version package to find them, One version package to bring them all, and in the darkness bind them.

`pip install awesomeversion` · installs (wheel) · licence: MIT · rank 4924 · last release 2025-08-03 · [PyPI](https://pypi.org/project/awesomeversion/) · [source](https://github.com/ludeeus/awesomeversion)

<details><summary>README extract</summary>

_One version package to rule them all, One version package to find them, One version package to bring them all, and in the darkness bind them._

Make anything a version object, and compare against a vast section of other version formats.

Example:
```python
from awesomeversion import AwesomeVersion

current = AwesomeVersion("1.2.2")
upstream = AwesomeVersion("1.2.3")

print(upstream > current)
> True
```

Sections: AwesomeVersion, AwesomeVersion class, AwesomeVersion methods, AwesomeVersion properties, Example usage, General behavior, Modifiers, Special versions (container)

</details>

### prefect-github

Prefect integrations interacting with GitHub

`pip install prefect-github` · installs (wheel) · licence: Apache Software License · rank 4929 · last release 2026-06-12 · [PyPI](https://pypi.org/project/prefect-github/)

### smithy-aws-event-stream

Smithy components for Amazon Event Streams.

`pip install smithy-aws-event-stream` · installs (wheel) · licence: Apache Software License · rank 4936 · last release 2026-05-05 · [PyPI](https://pypi.org/project/smithy-aws-event-stream/) · [source](https://github.com/smithy-lang/smithy-python/blob/develop/packages/smithy-aws-event-stream/)

<details><summary>README extract</summary>

This package provides AWS specific interfaces for Amazon Event Stream implementations in tooling generated by Smithy.

</details>

### modern-treasury

The official Python library for the Modern Treasury API

`pip install modern-treasury` · installs (wheel) · licence: MIT License · rank 4965 · last release 2026-10-28 · [PyPI](https://pypi.org/project/modern-treasury/) · [source](https://github.com/Modern-Treasury/modern-treasury-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Modern Treasury Python library provides convenient access to the Modern Treasury REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx. ...

Example:
```python
import os
from modern_treasury import ModernTreasury

client = ModernTreasury(
    organization_id=os.environ.get(
        "MODERN_TREASURY_ORGANIZATION_ID"
    ),  # This is the default and can be omitted
    api_key=os.environ.get("MODERN_TREASURY_API_KEY"),  # This is the default and can be omitted
)

...
```

...

</details>

### subprocess32

A backport of the subprocess module from Python 3 for use on 2.x.

`pip install subprocess32` · installs from source (sdist only) · licence: Python Software Foundation License · rank 4966 · last release 2020-06-16 · [PyPI](https://pypi.org/project/subprocess32/)

<details><summary>README extract</summary>

This is a backport of the subprocess standard library module from
Python 3.2 - 3.5 for use on Python 2.

It includes bugfixes and some new features. On POSIX systems it is
guaranteed to be reliable when used in threaded applications.
It includes timeout support from Python 3.3 and the run() API from 3.5
but otherwise matches 3.2's API. ...

</details>

### prefect-docker

Prefect integrations for interacting with Docker.

`pip install prefect-docker` · installs (wheel) · licence: Apache Software License · rank 4968 · last release 2026-09-08 · [PyPI](https://pypi.org/project/prefect-docker/)

### Distance

Utilities for comparing sequences

`pip install Distance` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 4977 · last release 2013-11-21 · [PyPI](https://pypi.org/project/Distance/)

_README extract left out: share-alike licence._

### bleak-retry-connector

A connector for Bleak Clients that handles transient connection failures

`pip install bleak-retry-connector` · installs (wheel) · licence: MIT · rank 4989 · last release 2026-09-14 · [PyPI](https://pypi.org/project/bleak-retry-connector/) · [docs](https://bleak-retry-connector.readthedocs.io) · [source](https://github.com/bluetooth-devices/bleak-retry-connector)

<details><summary>README extract</summary>

A connector for Bleak Clients that handles transient connection failures

Features:
- Automatic Retry Logic: Handles transient connection failures automatically
- Intelligent Backoff: Uses appropriate delays between retry attempts
- Service Caching: `BleakClientWithServiceCache` caches services for faster reconnections ...

Example:
```python
import asyncio
from bleak import BleakScanner
from bleak_retry_connector import establish_connection, BleakClientWithServiceCache

async def connect_to_device():
    # Find your device
    device = await BleakScanner.find_device_by_address("AA:BB:CC:DD:EE:FF")

    if device is None:
        print("Device not found!")
        return

...
```

...

</details>

### aws-assume-role-lib

Assumed role session chaining (with credential refreshing) for boto3

`pip install aws-assume-role-lib` · installs (wheel) · licence: Apache Software License · rank 4995 · last release 2022-05-14 · [PyPI](https://pypi.org/project/aws-assume-role-lib/) · [source](https://github.com/benkehoe/aws-assume-role-lib)

<details><summary>README extract</summary>

Assumed role session chaining (with credential refreshing) for boto3

The typical way to use boto3 when programmatically assuming a role is to explicitly call `sts.AssumeRole` and use the returned credentials to create a new `boto3.Session` or client.
It looks like this mess of code: ...

Example:
```python
import boto3
from aws_assume_role_lib import assume_role

# Get a session
session = boto3.Session()
# or with a profile:
# session = boto3.Session(profile_name="my-profile")

# Assume the session
assumed_role_session = assume_role(session, "arn:aws:iam::123456789012:role/MyRole")

# do stuff with the original credentials
...
```

Sections: aws-assume-role-lib, Usage, Interface, Patching boto3, Role session names for Lambda functions, ARN formatting, Caching, Command line use

</details>

### intel-openmp

Intel OpenMP* Runtime Library

`pip install intel-openmp` · installs (wheel) · licence: Other/Proprietary License · rank 4998 · last release 2026-10-16 · [PyPI](https://pypi.org/project/intel-openmp/)

<details><summary>README extract</summary>

Intel OpenMP* Runtime Library x86_64 dynamic libraries for Windows*. Intel OpenMP* Runtime Library provides OpenMP API specification support in Intel® C Compiler, Intel® C++ Compiler and Intel® Fortran Compiler. It helps to improve performance by creating multithreaded software using shared memory and running on multi-core processor systems.

</details>

### aiooui

Async OUI lookups

`pip install aiooui` · installs (wheel) · licence: MIT License · rank 5028 · last release 2026-09-25 · [PyPI](https://pypi.org/project/aiooui/) · [source](https://github.com/bluetooth-devices/aiooui)

<details><summary>README extract</summary>

Source Code:

Async OUI lookups

Example:
```python
import aiooui

await aiooui.async_load()
aiooui.get_vendor("00:00:00:11:22:33")  # "XEROX CORPORATION"
```

Sections: aiooui, Usage, How lookups work, Data file format

</details>

### pytest-examples

Pytest plugin for testing examples in docstrings and markdown files.

`pip install pytest-examples` · installs (wheel) · licence: MIT · rank 5037 · last release 2025-05-06 · [PyPI](https://pypi.org/project/pytest-examples/) · [source](https://github.com/pydantic/pytest-examples)

<details><summary>README extract</summary>

Example:
```python
import pytest
from pytest_examples import find_examples, CodeExample, EvalExample

@pytest.mark.parametrize('example', find_examples('foo_dir', 'bar_file.py'), ids=str)
def test_docstrings(example: CodeExample, eval_example: EvalExample):
    eval_example.lint(example)
    eval_example.run(example)
```

Sections: pytest-examples, Usage, Basic usage, Check print statements, > 3, Updating files

</details>

### simplegeneric

Simple generic functions (similar to Python's own len(), pickle.dump(), etc.)

`pip install simplegeneric` · installs from source (sdist only) · licence: Zope Public License · rank 5048 · last release 2012-04-01 · [PyPI](https://pypi.org/project/simplegeneric/)

<details><summary>README extract</summary>

* New in 0.8: Source and tests are compatible with Python 3 (w/o ``setup.py``)

 * 0.8.1: setup.py is now compatible with Python 3 as well

* New in 0.7: `Multiple Types or Objects`_

* New in 0.6: `Inspection and Extension`_, and thread-safe method registration ...

</details>

### bluetooth-adapters

Tools to enumerate and find Bluetooth Adapters

`pip install bluetooth-adapters` · installs (wheel) · licence: Apache-2.0 · rank 5051 · last release 2026-05-26 · [PyPI](https://pypi.org/project/bluetooth-adapters/) · [docs](https://bluetooth-adapters.readthedocs.io) · [source](https://github.com/bluetooth-devices/bluetooth-adapters)

<details><summary>README extract</summary>

Tools to enumerate and find Bluetooth Adapters

</details>

### backports.weakref

Backport of new features in Python's weakref module

`pip install backports.weakref` · installs (wheel) · licence: Python Software Foundation License · rank 5060 · last release 2017-09-17 · [PyPI](https://pypi.org/project/backports.weakref/)

<details><summary>README extract</summary>

This package provides backports of new features in Python's weakref module
under the backports namespace.

Sections: backports.weakref, Backported functionality

</details>

### fuzzysearch

fuzzysearch is useful for finding approximate subsequence matches

`pip install fuzzysearch` · installs from source (sdist only) · licence: MIT License · rank 5071 · last release 2025-11-11 · [PyPI](https://pypi.org/project/fuzzysearch/)

<details><summary>README extract</summary>

Fuzzy search: Find parts of long text or data, allowing for some
changes/typos.

Highly optimized, simple to use, does one thing well.

* Two simple functions to use: one for in-memory data and one for files

 * Fastest search algorithm is chosen automatically

* Levenshtein Distance metric with configurable parameters ...

Example:
```python
>>> from fuzzysearch import find_near_matches
# search for 'PATTERN' with a maximum Levenshtein Distance of 1
>>> find_near_matches('PATTERN', '---PATERN---', max_l_dist=1)
[Match(start=3, end=9, dist=1, matched="PATERN")]
```

...

</details>

### usb-devices

Tools for mapping, describing, and resetting USB devices

`pip install usb-devices` · installs (wheel) · licence: MIT License · rank 5086 · last release 2026-05-27 · [PyPI](https://pypi.org/project/usb-devices/) · [docs](https://usb-devices.readthedocs.io) · [source](https://github.com/bluetooth-devices/usb-devices)

### fnv-hash-fast

A fast version of fnv1a

`pip install fnv-hash-fast` · installs (wheel) · licence: MIT · rank 5093 · last release 2026-05-16 · [PyPI](https://pypi.org/project/fnv-hash-fast/) · [source](https://github.com/bluetooth-devices/fnv-hash-fast)

<details><summary>README extract</summary>

A fast version of fnv1a

This library will use a CPP implementation of fnv1a (32) if cython is available, and will fallback to pure python from the fnvhash package if it is not.

Example:
```python
>>> import fnv_hash_fast
>>> fnv_hash_fast.fnv1a_32(b"hello")
1335831723
>>> fnv_hash_fast.fnv1a_32(b"goodbye")
1188507472
```

Sections: FNV Hash Fast, Example

</details>

### pyodps

ODPS Python SDK and data analysis framework

`pip install pyodps` · installs (wheel) · licence: Apache License 2.0 · rank 5096 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pyodps/) · [source](http://github.com/aliyun/aliyun-odps-python-sdk)

<details><summary>README extract</summary>

Elegent way to access ODPS API.
Documentation

Example:
```python
>>> import os
>>> from odps import ODPS
>>> # Make sure environment variable CLOUD_ACCESS_KEY_ID already set to Access Key ID of user
>>> # while environment variable CLOUD_ACCESS_KEY_SECRET set to Access Key Secret of user.
>>> # Not recommended to hardcode Access Key ID or Access Key Secret in your code.
>>> o = ODPS(
...
```

Sections: ODPS Python SDK, Dependencies, Run Tests, Usage, Command-line and IPython enhancement, Python UDF Debugging Tool

</details>

### backports.tempfile

Backport of new features in Python's tempfile module

`pip install backports.tempfile` · installs (wheel) · licence: Python Software Foundation License · rank 5106 · last release 2017-10-13 · [PyPI](https://pypi.org/project/backports.tempfile/)

<details><summary>README extract</summary>

This package provides backports of new features in Python's tempfile module
under the backports namespace.

Sections: backports.tempfile, Backported functionality

</details>

### uart-devices

UART Devices for Linux

`pip install uart-devices` · installs (wheel) · licence: MIT License · rank 5117 · last release 2025-02-22 · [PyPI](https://pypi.org/project/uart-devices/) · [docs](https://uart-devices.readthedocs.io) · [source](https://github.com/bluetooth-devices/uart-devices)

<details><summary>README extract</summary>

Documentation:

Source Code:

UART Devices for Linux

</details>

### pyhwp

hwp file format parser

`pip install pyhwp` · installs from source (sdist only) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 5125 · last release 2020-05-30 · [PyPI](https://pypi.org/project/pyhwp/)

_README extract left out: share-alike licence._

### blessings

A thin, practical wrapper around terminal coloring, styling, and positioning

`pip install blessings` · installs (wheel) · licence: MIT License · rank 5126 · last release 2018-06-21 · [PyPI](https://pypi.org/project/blessings/)

<details><summary>README extract</summary>

Coding with Blessings looks like this...:
Or, for byte-level control, you can drop down and play with raw terminal
capabilities:
Full API Reference

Example:
```python
from blessings import Terminal

t = Terminal()

print t.bold('Hi there!')
print t.bold_red_on_bright_green('It hurts my eyes!')

with t.location(0, t.height - 1):
    print 'This is at the bottom.'
```

Sections: Blessings, The Pitch, Before And After, What It Provides, Simple Formatting, Color, Compound Formatting, Moving The Cursor, Moving Temporarily, Moving Permanently, One-Notch Movement, Height And Width, Clearing The Screen, Full-Screen Mode

</details>

### jupyter-cache

A defined interface for working with a cache of jupyter notebooks.

`pip install jupyter-cache` · installs (wheel) · licence: MIT License · rank 5127 · last release 2024-11-15 · [PyPI](https://pypi.org/project/jupyter-cache/) · [docs](https://jupyter-cache.readthedocs.io)

<details><summary>README extract</summary>

[][github-link]
[][codecov-link]
[][rtd-link]
[][black-link]
[][pypi-link]

A defined interface for working with a cache of jupyter notebooks.

Features:
If you have a number of notebooks whose execution outputs you want to ensure are kept up to date, without having to re-execute them every time (particularly for long running code, or text-based formats that do not store the outputs). ...

Sections: jupyter-cache, Why use jupyter-cache?, Code Style

</details>

### pytest-describe

Describe-style plugin for pytest

`pip install pytest-describe` · installs (wheel) · licence: MIT · rank 5136 · last release 2026-06-12 · [PyPI](https://pypi.org/project/pytest-describe/) · [source](https://github.com/pytest-dev/pytest-describe)

<details><summary>README extract</summary>

pytest-describe is a plugin for pytest
that allows tests to be written in arbitrary nested describe-blocks,
similar to RSpec (Ruby) and Jasmine (JavaScript).

The main inspiration for this was
a video by Gary Bernhardt.

Features:
I've found that quite often my tests have one "dimension" more than my production
code. The production code is organized into packages, modules, classes
(sometimes), and functions. ...

Example:
```python
import pytest

class Wallet:

    def init(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise ValueError(f'Not enough available to spend {amount}')
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount

...
```

...

</details>

### prefect-client

Workflow orchestration and management.

`pip install prefect-client` · installs (wheel) · licence: Apache Software License · rank 5145 · last release 2026-11-06 · [PyPI](https://pypi.org/project/prefect-client/) · [docs](https://www.prefect.io/docs) · [source](https://github.com/PrefectHQ/prefect)

<details><summary>README extract</summary>

The `prefect-client` package is a minimal-installation of `prefect` which is designed for interacting with Prefect Cloud
or remote any `prefect` server. It sheds some functionality and dependencies in exchange for a smaller installation size,
making it ideal for use in lightweight or ephemeral environments. ...

Example:
```python
from prefect.deployments import run_deployment

def my_lambda(event):
    ...
    run_deployment(
        name="my-flow/my-deployment",
        parameters={"foo": "bar"},
        timeout=0,
    )

my_lambda({})
```

Sections: prefect-client, Getting started, Known limitations, Next steps

</details>

### ulid-transform

Create and transform ULIDs

`pip install ulid-transform` · installs (wheel) · licence: MIT · rank 5164 · last release 2026-05-25 · [PyPI](https://pypi.org/project/ulid-transform/) · [source](https://github.com/bluetooth-devices/ulid-transform)

<details><summary>README extract</summary>

Create and transform ULIDs

This library will use the C++ implementation from when the C extension is available, and will fallback to pure python if it is not.

Example:
```python
>>> import ulid_transform
>>> ulid_transform.ulid_hex()
'01869a2ea5fb0b43aa056293e47c0a35'
>>> ulid_transform.ulid_now()
'0001HZX0NW00GW0X476W5TVBFE'
>>> ulid_transform.ulid_now_bytes()
b'\x01\x9eS\x9d\x1bhl~\x1e\xf7\x959\xe1\xf2\xbe\xea'
>>> ulid_transform.ulid_at_time(1234)
'000000016JC62D620DGYNG2R8H'
>>> ulid_transform.ulid_at_time_bytes(1234)
...
```

Sections: Fast ULID transformations, Example

</details>

### cmudict

A versioned python wrapper package for The CMU Pronouncing Dictionary data files.

`pip install cmudict` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 5168 · last release 2026-01-03 · [PyPI](https://pypi.org/project/cmudict/) · [source](https://github.com/prosegrinder/python-cmudict)

_README extract left out: share-alike licence._

### kernel

The official Python library for the kernel API

`pip install kernel` · installs (wheel) · licence: Apache Software License · rank 5170 · last release 2026-11-07 · [PyPI](https://pypi.org/project/kernel/) · [source](https://github.com/kernel/kernel-python-sdk)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Kernel Python library provides convenient access to the Kernel REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from kernel import Kernel

client = Kernel(
    api_key=os.environ.get("KERNEL_API_KEY"),  # This is the default and can be omitted
    # defaults to "production".
    environment="development",
)

browser = client.browsers.create(
    stealth=True,
)
print(browser.session_id)
```

...

</details>

### python-youtube

A Python wrapper around for YouTube Data API.

`pip install python-youtube` · installs (wheel) · licence: Apache Software License; MIT License · rank 5172 · last release 2026-04-17 · [PyPI](https://pypi.org/project/python-youtube/) · [source](https://github.com/sns-sdks/python-youtube)

<details><summary>README extract</summary>

Python YouTube

A Python wrapper for the YouTube Data API V3.

Inspired by Python-Twitter.

Thanks a lot to Python-Twitter Developers.

This library provides an easy way to use the YouTube Data API V3.

Example:
```python
>>> from pyyoutube import Client
>>> client = Client(api_key="your api key")
```

Sections: THANKS, Introduction, Documentation, Using, Work with Client, Work with API

</details>

### myst-nb

A Jupyter Notebook Sphinx reader built on top of the MyST markdown parser.

`pip install myst-nb` · installs (wheel) · licence: not stated · rank 5190 · last release 2026-03-02 · [PyPI](https://pypi.org/project/myst-nb/) · [docs](https://myst-nb.readthedocs.io)

<details><summary>README extract</summary>

[][github-link]
[][codecov-link]
[][rtd-link]
[][pypi-link]
[][conda-link]

A collection of tools for working with Jupyter Notebooks in Sphinx.

The primary tool this package provides is a Sphinx parser for `ipynb` files.
This allows you to directly convert Jupyter Notebooks into Sphinx documents.
It relies heavily on the `MyST` parser. ...

</details>

### sigtools

Utilities for working with inspect.Signature objects.

`pip install sigtools` · installs (wheel) · licence: MIT License · rank 5193 · last release 2022-10-13 · [PyPI](https://pypi.org/project/sigtools/)

<details><summary>README extract</summary>

The `sigtools` python library provides:

* `sigtools.signature` to resolve function signatures,
 taking into account parameters added or removed by decorators.
* Decorators to specify keyword-only parameters, annotations and
 positional-only parameters, even on python2: `sigtools.modifiers`
* Decorators to specify how `*args, **kwargs` are ...

</details>

### home-assistant-bluetooth

Home Assistant Bluetooth Models and Helpers

`pip install home-assistant-bluetooth` · installs (wheel) · licence: Apache Software License · rank 5194 · last release 2025-07-09 · [PyPI](https://pypi.org/project/home-assistant-bluetooth/) · [source](https://github.com/home-assistant-libs/home-assistant-bluetooth)

<details><summary>README extract</summary>

Home Assistant Bluetooth Models and Helpers

Example:
```python
@dataclasses.dataclass
class BluetoothServiceInfo(BaseServiceInfo):
    """Prepared info from bluetooth entries."""

    name: str
    address: str
    rssi: int
    manufacturer_data: dict[int, bytes]
    service_data: dict[str, bytes]
    service_uuids: list[str]
    source: str
```

Sections: Home Assistant Bluetooth, Usage

</details>

### ovh

"Official module to perform HTTP requests to the OVHcloud APIs"

`pip install ovh` · installs (wheel) · licence: BSD License · rank 5205 · last release 2024-07-23 · [PyPI](https://pypi.org/project/ovh/) · [source](https://github.com/ovh/python-ovh.git)

<details><summary>README extract</summary>

Lightweight wrapper around OVHcloud's APIs. Handles all the hard work including
credential creation and requests signing.

Example:
```python
import ovh

# Instantiate. Visit
# to get your credentials
client = ovh.Client(
    endpoint='ovh-eu',
    application_key='<application key>',
    application_secret='<application secret>',
    consumer_key='<consumer key>',
)

# Print nice welcome message
print("Welcome", client.get('/me')['firstname'])
```

...

</details>

### grafana-foundation-sdk

A set of tools, types and libraries for building and manipulating Grafana objects.

`pip install grafana-foundation-sdk` · installs (wheel) · licence: Apache Software License · rank 5221 · last release 2026-01-29 · [PyPI](https://pypi.org/project/grafana-foundation-sdk/) · [source](https://github.com/grafana/grafana-foundation-sdk.git)

<details><summary>README extract</summary>

A set of tools, types and *builder libraries* for building and manipulating Grafana objects in Python.

> [!NOTE]
> This branch contains types and builders generated for Grafana v10.1.x.
> Other supported versions of Grafana can be found at this repository's root.

Example:
```python
from grafana_foundation_sdk.builders.dashboard import Dashboard, Row
from grafana_foundation_sdk.builders.prometheus import Dataquery as PrometheusQuery
from grafana_foundation_sdk.builders.timeseries import Panel as Timeseries
from grafana_foundation_sdk.cog.encoder import JSONEncoder
...
```

Sections: Grafana Foundation SDK – Python, Example usage, Building a dashboard, Unmarshaling a dashboard, Defining a custom query type, Defining a custom panel type, Maturity

</details>

### pyexcel-xls

A wrapper library to read, manipulate and write data in xls format. Itreads xlsx and xlsm format

`pip install pyexcel-xls` · installs (wheel) · licence: New BSD · rank 5230 · last release 2025-03-08 · [PyPI](https://pypi.org/project/pyexcel-xls/)

<details><summary>README extract</summary>

pyexcel-xls is a tiny wrapper library to read, manipulate and
write data in xls format and it can read xlsx and xlsm fromat.
You are likely to use it with pyexcel.

1. v0.7.0 removed the pin on xlrd < 2. If you have xlrd >= 2, this
library will NOT read 'xlsx' format and you need to install pyexcel-xlsx. ...

Example:
```python
>>> from pyexcel_xls import save_data
>>> data = OrderedDict() # from collections import OrderedDict
>>> data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
>>> data.update({"Sheet 2": [["row 1", "row 2", "row 3"]]})
>>> save_data("your_file.xls", data)
```

...

</details>

### apeye-core

Core (offline) functionality for the apeye library.

`pip install apeye-core` · installs (wheel) · licence: BSD License · rank 5232 · last release 2024-01-30 · [PyPI](https://pypi.org/project/apeye-core/) · [source](https://github.com/domdfcoding/apeye-core)

<details><summary>README extract</summary>

Core (offline) functionality for the apeye library.

</details>

### zope.component

Zope Component Architecture

`pip install zope.component` · installs (wheel) · licence: ZPL-2.1 · rank 5238 · last release 2026-02-03 · [PyPI](https://pypi.org/project/zope.component/) · [docs](https://zopecomponent.readthedocs.io/) · [source](https://github.com/zopefoundation/zope.component)

<details><summary>README extract</summary>

This package represents the core of the Zope Component Architecture.
Together with the zope.interface package, it provides facilities for
defining, registering and looking up components.

Please see for the
documentation.

- Move package metadata from setup.py to pyproject.toml.

- Add support for Python 3.14.

- Drop support for Python 3.9. ...

Sections: zope.component, Changes, 7.1 (2026-02-03), 7.0 (2025-09-12), 6.1 (2025-09-09), 6.0 (2023-04-14), 5.1.0 (2023-01-03), 5.0.1 (2021-07-09), 5.0.0 (2021-03-19), 4.6.2 (2020-07-03), 4.6.1 (2020-03-23), 4.6.0 (2019-11-12), 4.5.0 (2018-10-10), 4.4.1 (2017-09-26)

</details>

### bluetooth-auto-recovery

Recover bluetooth adapters that are in an stuck state

`pip install bluetooth-auto-recovery` · installs (wheel) · licence: MIT · rank 5239 · last release 2026-05-25 · [PyPI](https://pypi.org/project/bluetooth-auto-recovery/) · [docs](https://bluetooth-auto-recovery.readthedocs.io) · [source](https://github.com/bluetooth-devices/bluetooth-auto-recovery)

<details><summary>README extract</summary>

Recover bluetooth adapters that are in an stuck state

</details>

### django-dirtyfields

Tracking dirty fields on a Django model instance.

`pip install django-dirtyfields` · installs (wheel) · licence: BSD-3-Clause · rank 5250 · last release 2026-01-22 · [PyPI](https://pypi.org/project/django-dirtyfields/) · [docs](https://django-dirtyfields.readthedocs.io) · [source](https://github.com/romgar/django-dirtyfields.git)

<details><summary>README extract</summary>

Tracking dirty fields on a Django model instance.
Dirty means that field in-memory and database values are different.

This package is compatible and tested with the following Python & Django versions: ...

Example:
```python
from django.db import models
from dirtyfields import DirtyFieldsMixin

class ExampleModel(DirtyFieldsMixin, models.Model):
    """A simple example model to test dirty fields mixin with"""
    boolean = models.BooleanField(default=True)
    characters = models.CharField(blank=True, max_length=80)
```

Sections: Django Dirty Fields, Usage, Example

</details>

### toon-format

Official Python implementation of TOON (Token-Oriented Object Notation), a compact, human-readable encoding of the JSON data model for LLM prompts.

`pip install toon-format` · installs (wheel) · licence: MIT · rank 5263 · last release 2026-10-18 · [PyPI](https://pypi.org/project/toon-format/) · [docs](https://toon-format.readthedocs.io/en/stable/) · [source](https://github.com/toon-format/toon-python)

<details><summary>README extract</summary>

The official Python implementation of TOON (Token-Oriented Object Notation):
a compact, human-readable encoding of the JSON data model, designed to save
tokens in LLM prompts. Keep working with dictionaries and lists in your code,
and encode them as TOON only where a model reads them. ...

Example:
```python
import toon_format

data = {
    "context": {"task": "Our favorite hikes together", "location": "Boulder"},
    "friends": ["ana", "luis", "sam"],
    "hikes": [
        {"id": 1, "name": "Blue Lake Trail", "distanceKm": 7.5, "wasSunny": True},
        {"id": 2, "name": "Ridge Overlook", "distanceKm": 9.2, "wasSunny": False},
    ],
}

...
```

...

</details>

### hologram

JSON schema generation from dataclasses

`pip install hologram` · installs (wheel) · licence: MIT License · rank 5264 · last release 2023-03-24 · [PyPI](https://pypi.org/project/hologram/)

<details><summary>README extract</summary>

Hologram is a lightweight library to generate Draft 7 compatible JSON Schemas from python 3.7 dataclasses. Python 3.6 is supported through the dataclasses backport. It is forked from dataclasses-jsonschema created by s-knibbs.

</details>

### pytest-cache

pytest plugin with mechanisms for caching across test runs

`pip install pytest-cache` · installs from source (sdist only) · licence: MIT License · rank 5278 · last release 2013-06-04 · [PyPI](https://pypi.org/project/pytest-cache/)

<details><summary>README extract</summary>

Example:
```python
# content of test_50.py
import pytest

@pytest.mark.parametrize("i", range(50))
def test_num(i):
    if i in (17,25):
       pytest.fail("bad luck")
```

Sections: pytest-cache: working with cross-testrun state, Usage, Rerunning only failures or failures first, The new config.cache object, Inspecting Cache content, Clearing Cache content, Notes

</details>

### gtfs-realtime-bindings

Python classes generated from the GTFS-realtime protocol buffer specification.

`pip install gtfs-realtime-bindings` · installs (wheel) · licence: Apache Software License · rank 5280 · last release 2026-09-17 · [PyPI](https://pypi.org/project/gtfs-realtime-bindings/)

### pyink

Pyink is a python formatter, forked from Black with slightly different behavior.

`pip install pyink` · installs (wheel) · licence: MIT · rank 5282 · last release 2026-08-25 · [PyPI](https://pypi.org/project/pyink/) · [source](https://github.com/google/pyink)

<details><summary>README extract</summary>

*Pyink*, pronounced pī-ˈiŋk, is a Python formatter, forked from
*Black* with a few different formatting
behaviors. We intend to keep rebasing on top of *Black*'s latest changes.

Features:
We would love to adopt *Black*, but adopting it overnight is too disruptive to
the thousands of developers working in our monorepo. ...

Example:
```python
# Pyink:
result = some_other_module._private_function(arg="value")  # pylint: disable=protected-access

# Black:
result = some_other_module._private_function(
    arg="value"
)  # pylint: disable=protected-access
```

Sections: Why *Pyink*?, What are the main differences?, Historical differences, How do I use *Pyink*?, Is there a VS Code extension for *Pyink*?, Can I use *Pyink* with the pre-commit framework?, Why the name?, Disclaimer

</details>

### lakefs

lakeFS Python SDK Wrapper

`pip install lakefs` · installs (wheel) · licence: Apache-2.0 · rank 5287 · last release 2026-04-10 · [PyPI](https://pypi.org/project/lakefs/)

<details><summary>README extract</summary>

lakeFS High Level SDK for Python, provides developers with the following features:
1. Simpler programming interface with less configuration
2. Inferring identity from environment
3. Better abstractions for common, more complex operations (I/O, transactions, imports)

Python 3.10+

Example:
```python
import lakefs
from lakefs.client import Client

# Using default client will attempt to authenticate with lakeFS server using configured credentials
# If environment variables or .lakectl.yaml file exist
repo = lakefs.repository(repository_id="my-repo")

# Or explicitly initialize and provide a Client object
...
```

...

</details>

### fixit

A lint framework that writes better Python code for you.

`pip install fixit` · installs (wheel) · licence: MIT License · rank 5288 · last release 2025-11-12 · [PyPI](https://pypi.org/project/fixit/) · [source](https://github.com/Instagram/Fixit)

<details><summary>README extract</summary>

Fixit provides a highly configurable linting framework with support for
auto-fixes, custom "local" lint rules, and hierarchical configuration, built
on LibCST.

Fixit makes it quick and easy to write new lint rules and offer suggested
changes for any errors found, which can then be accepted automatically,
or presented to the user for ...

</details>

### django-tinymce

A Django application that contains a widget to render a

`pip install django-tinymce` · installs (wheel) · licence: MIT AND GPL-2.0-or-later · rank 5294 · last release 2025-10-21 · [PyPI](https://pypi.org/project/django-tinymce/) · [docs](https://django-tinymce.readthedocs.org/)

_README extract left out: share-alike licence._

### CFGraph

rdflib collections flattening graph

`pip install CFGraph` · installs from source (sdist only) · licence: Apache 2.0 · rank 5321 · last release 2018-11-20 · [PyPI](https://pypi.org/project/CFGraph/)

### faust-cchardet

cChardet is high speed universal character encoding detector.

`pip install faust-cchardet` · installs (wheel) · licence: MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later · rank 5324 · last release 2026-08-10 · [PyPI](https://pypi.org/project/faust-cchardet/)

_README extract left out: share-alike licence._

### zope.schema

zope.interface extension for defining data schemas

`pip install zope.schema` · installs (wheel) · licence: Zope Public License · rank 5340 · last release 2025-10-26 · [PyPI](https://pypi.org/project/zope.schema/)

<details><summary>README extract</summary>

Schemas extend the notion of interfaces to detailed descriptions of
`Attributes` (but not methods). Every schema is an interface and
specifies the public fields of an object. A *field* roughly
corresponds to an attribute of a Python object. But a Field provides
space for at least a title and a description. ...

Example:
```python
  Date(defaultFactory=datetime.date.today)

If the factory needs a context to compute a sensible default value, then it
must provide `IContextAwareDefaultFactory, which can be used as follows::

  @provider(IContextAwareDefaultFactory)
  def today(context):
      return context.today()

  Date(defaultFactory=today)
```

...

</details>

### aurora-data-api

A Python DB-API 2.0 client for the AWS Aurora Serverless Data API

`pip install aurora-data-api` · installs (wheel) · licence: Apache Software License · rank 5356 · last release 2023-12-29 · [PyPI](https://pypi.org/project/aurora-data-api/)

<details><summary>README extract</summary>

Example:
```python
import aurora_data_api

cluster_arn = "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-serverless-cluster"
secret_arn = "arn:aws:secretsmanager:us-east-1:123456789012:secret:rds-db-credentials/MY_DB"
with aurora_data_api.connect(aurora_cluster_arn=cluster_arn, secret_arn=secret_arn, database="my_db") as conn:
    with conn.cursor() as cursor:
...
```

Sections: Prerequisites, Usage, Motivation, Links, Bugs

</details>

### apipkg

apipkg: namespace control and lazy-import mechanism

`pip install apipkg` · installs (wheel) · licence: MIT License · rank 5359 · last release 2023-09-19 · [PyPI](https://pypi.org/project/apipkg/)

<details><summary>README extract</summary>

With apipkg you can control the exported namespace of a Python package and
greatly reduce the number of imports for your users.
It is a small pure Python module that works on CPython 3.7+,
Jython and PyPy. It cooperates well with Python's `help()` system,
custom importers (PEP302) and common command-line completion tools. ...

Example:
```python
# mypkg/init.py
import apipkg
apipkg.initpkg(name, {
    'path': {
        'Class1': "_mypkg.somemodule:Class1",
        'clsattr': "_mypkg.othermodule:Class2.attr",
    }
}
```

Sections: Welcome to apipkg !, Tutorial example, Including apipkg in your package, Feedback?

</details>

### linkup-sdk

A Python Client SDK for the Linkup API

`pip install linkup-sdk` · installs (wheel) · licence: MIT · rank 5363 · last release 2026-10-22 · [PyPI](https://pypi.org/project/linkup-sdk/) · [docs](https://github.com/LinkupPlatform/linkup-python-sdk#readme) · [source](https://github.com/LinkupPlatform/linkup-python-sdk)

<details><summary>README extract</summary>

A Python SDK for the Linkup API, allowing easy integration with Linkup's
services in any Python application. 🐍

Checkout the official
API documentation and
SDK documentation for additional details on how to
benefit from Linkup services to the full extent. 📝

- ✅ Simple and intuitive API client. ...

Example:
```python
import os
import linkup

os.environ["LINKUP_API_KEY"] = "<your-linkup-api-key>"
# or dotenv.load_dotenv()
client = linkup.Client()
...
```

Sections: 🚀 Linkup Python SDK, 🌟 Features, 🛠️ Usage, Setting Up Your Environment, 📋 Examples, 📝 Search, 🪝 Fetch, 🧠 Research, 🗂️ Tasks, ⌛ Asynchronous Calls

</details>

### aiozoneinfo

Tools to fetch zoneinfo with asyncio

`pip install aiozoneinfo` · installs (wheel) · licence: Apache Software License · rank 5371 · last release 2025-02-04 · [PyPI](https://pypi.org/project/aiozoneinfo/) · [docs](https://aiozoneinfo.readthedocs.io) · [source](https://github.com/bluetooth-devices/aiozoneinfo)

<details><summary>README extract</summary>

Documentation:

Source Code:

Tools to fetch zoneinfo with asyncio

Example:
```python
zone_info = await async_get_time_zone("America/Los_Angeles")
```

Sections: aiozoneinfo, Usage

</details>

### prefect-kubernetes

Prefect integrations for interacting with Kubernetes.

`pip install prefect-kubernetes` · installs (wheel) · licence: Apache Software License · rank 5377 · last release 2026-10-19 · [PyPI](https://pypi.org/project/prefect-kubernetes/)

### securetar

Python module to handle tarfile backups.

`pip install securetar` · installs (wheel) · licence: Apache-2.0 · rank 5382 · last release 2026-10-09 · [PyPI](https://pypi.org/project/securetar/)

<details><summary>README extract</summary>

Secure Tarfile library

SecureTar is a streaming wrapper around Python's `tarfile` module. It
creates and reads tar archives that contain inner tar files, which can be
encrypted. It is the archive format used for Home Assistant backups.

A SecureTar archive is a plain, uncompressed outer tar in PAX format. ...

Example:
```python
from pathlib import Path

from securetar import SecureTarArchive, atomic_contents_add

with SecureTarArchive(Path("backup.tar"), "w", password="hunter2") as archive:
    with archive.create_tar("./homeassistant.tar.gz", gzip=True) as inner_tar:
        atomic_contents_add(
            inner_tar,
            Path("/config"),
...
```

...

</details>

### sqlalchemy-aurora-data-api

An AWS Aurora Serverless Data API dialect for SQLAlchemy

`pip install sqlalchemy-aurora-data-api` · installs (wheel) · licence: Apache Software License · rank 5386 · last release 2023-12-30 · [PyPI](https://pypi.org/project/sqlalchemy-aurora-data-api/)

<details><summary>README extract</summary>

This package provides a SQLAlchemy
dialect for accessing PostgreSQL and MySQL databases via the
AWS Aurora Data API.

Example:
```python
from sqlalchemy import create_engine

cluster_arn = "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-serverless-cluster"
secret_arn = "arn:aws:secretsmanager:us-east-1:123456789012:secret:rds-db-credentials/MY_DB"

engine = create_engine('postgresql+auroradataapi://:@/my_db_name',
                       echo=True,
...
```

Sections: Prerequisites, Usage, Motivation, Debugging, Links, Bugs

</details>

### progressbar

Text progress bar library for Python.

`pip install progressbar` · installs from source (sdist only) · licence: BSD License; GNU Library or Lesser General Public License (LGPL) · rank 5390 · last release 2018-06-29 · [PyPI](https://pypi.org/project/progressbar/)

_README extract left out: share-alike licence._

### rq-scheduler

Provides job scheduling capabilities to RQ (Redis Queue)

`pip install rq-scheduler` · installs (wheel) · licence: MIT License · rank 5395 · last release 2024-10-29 · [PyPI](https://pypi.org/project/rq-scheduler/)

<details><summary>README extract</summary>

RQ Scheduler is a small package that
adds job scheduling capabilities to RQ,
a Redis based Python queuing library.

Example:
```python
from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler
from datetime import datetime

scheduler = Scheduler(connection=Redis()) # Get a scheduler for the "default" queue
scheduler = Scheduler('foo', connection=Redis()) # Get a scheduler for the "foo" queue

# You can also instantiate a Scheduler using an RQ Queue
...
```

Sections: RQ Scheduler, Requirements, Usage, Scheduling a Job, Periodic & Repeated Jobs, Cron Jobs, Retrieving scheduled jobs, Checking if a job is scheduled, Canceling a job, Running the scheduler, Running the Scheduler as a Service on Ubuntu, Running Multiple Schedulers

</details>

### django-fsm-2

Django friendly finite state machine support.

`pip install django-fsm-2` · installs (wheel) · licence: MIT · rank 5399 · last release 2026-10-28 · [PyPI](https://pypi.org/project/django-fsm-2/) · [docs](http://github.com/django-commons/django-fsm-2) · [source](http://github.com/django-commons/django-fsm-2)

<details><summary>README extract</summary>

Example:
```python
from django.db import models
import django_fsm as fsm

class BlogPost(fsm.FSMModelMixin, models.Model):
    state = fsm.FSMField(default="new")

    @fsm.transition(field=state, source="new", target="published")
    def publish(self, **kwargs):
        pass
```

Sections: Introduction, Quick start, Usage, Core ideas, Adding an FSM field, Declaring a transition, Preconditions (conditions), Protected state fields, Source and target states, Custom transition metadata, Error target state, Permissions, Model helpers, FSMIntegerField (enum-style states)

</details>

### textual-image

Render images via Kitty's Terminal Graphics Protocol with Rich and Textual

`pip install textual-image` · installs (wheel) · licence: LGPL-3.0-or-later · rank 5412 · last release 2026-10-20 · [PyPI](https://pypi.org/project/textual-image/) · [docs](https://github.com/lnqs/textual-image) · [source](https://github.com/lnqs/textual-image)

_README extract left out: share-alike licence._

### jsonpath-rust-bindings

(no summary)

`pip install jsonpath-rust-bindings` · installs (wheel) · licence: not stated · rank 5413 · last release 2025-11-16 · [PyPI](https://pypi.org/project/jsonpath-rust-bindings/)

### pylint-actions

Pylint plugin for GitHub Actions

`pip install pylint-actions` · installs (wheel) · licence: MIT · rank 5423 · last release 2026-08-03 · [PyPI](https://pypi.org/project/pylint-actions/)

<details><summary>README extract</summary>

This is a plugin for Pylint that allows it to output annotations
in the format that GitHub Actions understands.
See annotations from examples workflows.
Also these annotations will be displayed in your pull requests changes

Sections: Pylint plugin for GitHub Actions annotations, Usage

</details>

### pysignalr

Modern, reliable and async-ready client for SignalR protocol

`pip install pysignalr` · installs (wheel) · licence: MIT License · rank 5424 · last release 2026-10-17 · [PyPI](https://pypi.org/project/pysignalr/) · [source](https://github.com/baking-bad/pysignalr)

<details><summary>README extract</summary>

pysignalr is a modern, reliable, and async-ready client for the SignalR protocol. This project started as an asyncio fork of mandrewcito's signalrcore library and ended up as a complete rewrite.

Example:
```python
from future import annotations

import asyncio
from contextlib import suppress
from typing import TYPE_CHECKING
from typing import Any

from pysignalr.client import SignalRClient

if TYPE_CHECKING:
    from pysignalr.messages import CompletionMessage

async def on_open() -> None:
    print('Connected to the server')

async def on_close() -> None:
...
```

Sections: pysignalr, Basic Usage, Usage with Token Authentication, API Reference, `SignalRClient`, Parameters, Methods, `CompletionMessage`, Attributes

</details>

### mt-940

A library to parse MT940 files and returns smart Python collections for statistics and manipulation.

`pip install mt-940` · installs (wheel) · licence: BSD-3-Clause · rank 5442 · last release 2026-10-28 · [PyPI](https://pypi.org/project/mt-940/) · [docs](https://mt940.readthedocs.io/) · [source](https://github.com/WoLpH/mt940)

<details><summary>README extract</summary>

Parse MT940 bank statements into Python transactions, decimal amounts, dates
and balances. The `mt-940` distribution imports as `mt940`, supports Python
3.10 through 3.15 and has no runtime dependencies. Type information ships in the
package through `py.typed`.

Install the package in your project's environment: ...

Example:
```python
import mt940

source: str = """:20:EXAMPLE-001
:25:EXAMPLE-ACCOUNT
:28C:1/1
:60F:C260101EUR100,00
:61:2601020102D12,50NTRFCOFFEE//BANK-001
:86:Coffee supplies
:62F:C260102EUR87,50
"""
statement: mt940.models.Transactions = mt940.parse(source)
transaction: mt940.models.Transaction = statement[0]
...
```

Sections: MT940, Parse your first statement, Choose the input and output you need, Bank formats and compatibility

</details>

### pydantic-argparse

Typed Argument Parsing with Pydantic

`pip install pydantic-argparse` · installs (wheel) · licence: MIT · rank 5445 · last release 2025-02-09 · [PyPI](https://pypi.org/project/pydantic-argparse/) · [docs](https://pydantic-argparse.supimdos.com) · [source](https://github.com/SupImDos/pydantic-argparse)

<details><summary>README extract</summary>

Typed Argument Parsing with Pydantic

See documentation for help.

Requires Python 3.8+, and is compatible with the Pydantic v1 API.

Example:
```python
import pydantic.v1 as pydantic

import pydantic_argparse

class Arguments(pydantic.BaseModel):
    # Required Args
    string: str = pydantic.Field(description="a required string", aliases=["-s"])
    integer: int = pydantic.Field(description="a required integer", aliases=["-i"])
...
```

Sections: Pydantic Argparse, Help, Requirements, Example

</details>

### asyncio-throttle

Simple, easy-to-use throttler for asyncio

`pip install asyncio-throttle` · installs (wheel) · licence: MIT License · rank 5451 · last release 2021-04-07 · [PyPI](https://pypi.org/project/asyncio-throttle/)

<details><summary>README extract</summary>

Simple, easy-to-use throttler for asyncio.

Example:
```python
import time
import random
import asyncio

from asyncio_throttle import Throttler

async def worker(no, throttler, n):
    for _ in range(n):
        await asyncio.sleep(random.random() * 2)

        async with throttler:
            print(time.time(), 'Worker #%d: Bang!' % no)

async def main():
    throttler = Throttler(rate_limit=5)

...
```

Sections: asyncio-throttle, Example, Usage

</details>

### psutil-home-assistant

Wrapper for psutil to allow it to be used several times in the same process.

`pip install psutil-home-assistant` · installs (wheel) · licence: Apache License 2.0 · rank 5452 · last release 2022-08-25 · [PyPI](https://pypi.org/project/psutil-home-assistant/)

<details><summary>README extract</summary>

The `psutil` library relies on global variable to maintain state between calls. This wrapper
allows making local copies of the `psutil` library, wrapped in an object to allow `psutil` to
be used more than once in a process.

</details>

### javaobj-py3

Module for serializing and de-serializing Java objects.

`pip install javaobj-py3` · installs (wheel) · licence: Apache-2.0 · rank 5462 · last release 2026-08-12 · [PyPI](https://pypi.org/project/javaobj-py3/) · [source](http://github.com/tcalmant/python-javaobj/)

<details><summary>README extract</summary>

*python-javaobj* is a python library that provides functions for reading and
writing Java objects serialized or to be deserialized by `ObjectOutputStream`.
This form of object representation is a standard data interchange format in
Java world. ...

Features:
* Java object instance un-marshalling
* Java classes un-marshalling
* Primitive values un-marshalling
* Automatic conversion of Java Collections to python ones
 (`HashMap` => `dict`, `ArrayList` => `list`, etc.)
* Basic marshalling of simple Java ...

Example:
```python
import javaobj

with open("obj5.ser", "rb") as fd:
    jobj = fd.read()

pobj = javaobj.loads(jobj)
print(pobj)
```

...

</details>

### tml-renderers

Public TML chat types, tokenizers, and native renderers

`pip install tml-renderers` · installs (wheel) · licence: Apache-2.0 · rank 5478 · last release 2026-11-06 · [PyPI](https://pypi.org/project/tml-renderers/)

<details><summary>README extract</summary>

`tml-renderers` turns structured text, image, and audio chat into model-ready
tokens and media for training and inference. It supports Thinking Machines Lab
models, including Inkling and Inkling-Small, through TMLv0, and the
supported third-party models served on Tinker
through model-specific renderers.

Example:
```python
from tml_renderers import chat, renderers

user = chat.Message(
    content=chat.Text("Hello, world!"),
    author=chat.Author(chat.AuthorKind.User),
)
assistant = chat.Message(
    content=chat.Text("Hello!"),
    author=chat.Author(chat.AuthorKind.Model),
)
native_messages = chat.MessageList([user, assistant])

renderer = renderers.Qwen3()
...
```

...

</details>

### delighted

Delighted API Python Client.

`pip install delighted` · installs (wheel) · licence: MIT License · rank 5479 · last release 2026-03-17 · [PyPI](https://pypi.org/project/delighted/)

<details><summary>README extract</summary>

> DEPRECATION NOTICE: Delighted is being sunset on June 30, 2026. This package is deprecated and will no longer be maintained or receive updates. For more information, visit the Delighted Sunset FAQ.

Official Python client for the Delighted API.

Example:
```python
# Add a new person, and schedule a survey immediately
person1 = delighted.Person.create(email='foo+test1@delighted.com')

# Add a new person, and schedule a survey after 1 minute (60 seconds)
person2 = delighted.Person.create(email='foo+test2@delighted.com', delay=60)

# Add a new person, but do not schedule a survey
...
```

Sections: Delighted API Python Client, Upgrading from delighted-python, Configuration, Usage, Rate limits, Releasing

</details>

### ariadne-codegen

Generate fully typed GraphQL client from schema, queries and mutations!

`pip install ariadne-codegen` · installs (wheel) · licence: BSD-3-Clause · rank 5488 · last release 2026-08-28 · [PyPI](https://pypi.org/project/ariadne-codegen/) · [source](https://github.com/mirumee/ariadne-codegen)

<details><summary>README extract</summary>

Python code generator that turns a GraphQL schema and your operations into a fully typed, async (or sync) Python client built on Pydantic. You write your queries, mutations and subscriptions in GraphQL, and ariadne-codegen generates a typed Python method for each one, returning Pydantic models - so you get autocompletion and static type checking ...

Features:
- Fully typed models - Pydantic models for schema types, inputs, enums, fragments, and every operation's result.
- Typed client methods - each query, mutation, and subscription becomes a method with typed arguments and a typed return value. ...

Example:
```python
import asyncio
from graphql_client import Client

async def main():
    async with Client(url=" as client:
        result = await client.greet(name="World")
...

</details>

### flake8-polyfill

Polyfill package for Flake8 plugins

`pip install flake8-polyfill` · installs (wheel) · licence: MIT License · rank 5494 · last release 2017-12-30 · [PyPI](https://pypi.org/project/flake8-polyfill/)

<details><summary>README extract</summary>

`flake8-polyfill` is a package that provides some compatibility helpers for
Flake8 plugins that intend to support Flake8 2.x and 3.x simultaneously.

Example:
```python
from flake8_polyfill import options

class MyFlake8Plugin(object):
    @classmethod
    def add_options(cls, parser):
        options.register(parser, '--my-long-option-name',
                         parse_from_config=True,
                         comma_separated_list=True,
                         default='...',
...
```

Sections: Polyfill for Flake8 Plugins, Usage, Option Handling, Retrieving Standard In, Version Comparison, Creator

</details>

### pydantic-function-models

Migrating v1 Pydantic ValidatedFunction to v2.

`pip install pydantic-function-models` · installs (wheel) · licence: MIT · rank 5495 · last release 2026-04-16 · [PyPI](https://pypi.org/project/pydantic-function-models/) · [source](https://github.com/lmmx/pydantic-function-models)

<details><summary>README extract</summary>

A library to model Python function signatures using Pydantic, inspired by the now-deprecated `ValidatedFunction` from Pydantic v1. This package helps validate function arguments according to type hints, bridging the gap between Pydantic v1 and v2.

Features:
- Signature modelling: Wrap any Python function to model its signature (positional, keyword, etc.) using Pydantic. Note that if you are after just validation (whether the arguments are valid) then you want validate call ...

Example:
```python
from pydantic_function_models import ValidatedFunction

def add(a: int, b: int) -> int:
    return a + b

vf = ValidatedFunction(add)

# Build arguments for validation
args_to_validate = (1,)
kwargs_to_validate = {"b": 2}

validated = vf.model.model_validate({
    "a": args_to_validate[0],
...

</details>

### testrail-api

Python wrapper of the TestRail API

`pip install testrail-api` · installs (wheel) · licence: MIT · rank 5502 · last release 2026-10-26 · [PyPI](https://pypi.org/project/testrail-api/) · [source](https://github.com/tolstislon/testrail-api)

<details><summary>README extract</summary>

This is a Python wrapper of the TestRail API according
to the official documentation

Install

Install using pip with

Example:
```python
from datetime import datetime
import simplejson

from testrail_api import TestRailAPI

def my_handler(response):
    if response.ok:
        return simplejson.loads(response.text)
    return 'Error'

api = TestRailAPI(" "example@mail.com", "password", response_handler=my_handler)
new_milestone = api.milestones.add_milestone(
    project_id=1,
...
```

Sections: Testrail Api, Custom response handler, Getting started

</details>

### hyperliquid-python-sdk

SDK for Hyperliquid API trading with Python.

`pip install hyperliquid-python-sdk` · installs (wheel) · licence: MIT License · rank 5504 · last release 2026-06-04 · [PyPI](https://pypi.org/project/hyperliquid-python-sdk/) · [source](https://github.com/hyperliquid-dex/hyperliquid-python-sdk)

<details><summary>README extract</summary>

SDK for Hyperliquid API trading with Python.

Example:
```python
from hyperliquid.info import Info
from hyperliquid.utils import constants

info = Info(constants.TESTNET_API_URL, skip_ws=True)
user_state = info.user_state("0xcd5051944f780a621ee62e39e493c489668acf4d")
print(user_state)
```

Sections: hyperliquid-python-sdk, Configuration, [Optional] Generate a new API key for an API Wallet, Usage Examples, Makefile usage, List of labels and corresponding titles, Building and releasing

</details>

### nose2

unittest with plugins

`pip install nose2` · installs (wheel) · licence: BSD License · rank 5507 · last release 2026-03-02 · [PyPI](https://pypi.org/project/nose2/) · [docs](https://docs.nose2.io/) · [source](https://github.com/nose-devs/nose2)

<details><summary>README extract</summary>

nose2's extends `unittest` to make testing nicer.

`nose2` originated as the successor to `nose`.

`nose2` is a distinct project and does not support all of the behaviors of `nose`.
See differences for a thorough rundown.

pytest is an excellent test framework and we encourage users to consider
it for new projects. ...

Example:
```python
# in test_simple.py
import unittest

class TestStrings(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("spam".upper(), "SPAM")
```

Sections: Welcome to nose2, nose2 vs nose, nose2 vs pytest, Quickstart, Full Docs, Python Versions, Python 2

</details>

### pyobjc-framework-ApplicationServices

Wrappers for the framework ApplicationServices on macOS

`pip install pyobjc-framework-ApplicationServices` · installs from source (sdist only) · licence: MIT · rank 5524 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ApplicationServices/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ApplicationServices" framework on macOS 10.5 or later. Core Text is an
advanced, low-level technology for laying out text and handling fonts. It is
designed for high performance and ease of use. ...

</details>

### keyboard

Hook and simulate keyboard events on Windows and Linux

`pip install keyboard` · installs (wheel) · licence: MIT License · rank 5525 · last release 2020-03-23 · [PyPI](https://pypi.org/project/keyboard/)

<details><summary>README extract</summary>

Take full control of your keyboard with this small Python library. Hook global events, register hotkeys, simulate key presses and much more.

Features:
- Global event hook on all keyboards (captures keys regardless of focus).
- Listen and send keyboard events.
- Works with Windows and Linux (requires sudo), with experimental OS X support (thanks @glitchassassin!). ...

Example:
```python
import keyboard

keyboard.press_and_release('shift+s, space')

keyboard.write('The quick brown fox jumps over the lazy dog.')

keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# Press PAGE UP then PAGE DOWN to type "foobar".
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

...
```

Sections: keyboard, Features, Usage, Example, Known limitations

</details>

### pyobjc-framework-CoreText

Wrappers for the framework CoreText on macOS

`pip install pyobjc-framework-CoreText` · installs from source (sdist only) · licence: MIT · rank 5536 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreText/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreText" framework on macOS 10.5 or later. Core Text is an
advanced, low-level technology for laying out text and handling fonts. It is
designed for high performance and ease of use. ...

</details>

### MarkupPy

An HTML/XML generator

`pip install MarkupPy` · installs (wheel) · licence: MIT License · rank 5537 · last release 2025-03-19 · [PyPI](https://pypi.org/project/MarkupPy/) · [docs](https://tylerbakke.github.io/MarkupPy/)

<details><summary>README extract</summary>

This is MarkupPy - a Python module that attempts to make it easier to generate HTML/XML from a Python program in an intuitive, lightweight, customizable and pythonic way. It works with both python 2 and 3.

<b>Installation:</b>

 pip install MarkupPy

Documentation and further info is at ...

Example:
```python
from MarkupPy import markup

# Create an HTML page
page = markup.page()
page.init(title="My Title")
page.p("Hello, World!")
page.p.close()

# Print the HTML
print(page)
```

Sections: MarkupPy, Usage Examples, Basic Example, Inline Styles and Scripts (v1.16+), Avoiding Extra Newlines in Pre Tags (v1.17+), Running Tests

</details>

### mcp-proxy

A MCP server which proxies requests to a remote MCP server over streamable HTTP or SSE.

`pip install mcp-proxy` · installs (wheel) · licence: MIT · rank 5543 · last release 2026-11-02 · [PyPI](https://pypi.org/project/mcp-proxy/) · [docs](https://github.com/sparfenyuk/mcp-proxy) · [source](https://github.com/sparfenyuk/mcp-proxy)

<details><summary>README extract</summary>

- mcp-proxy
 - About
 - 1. stdio to SSE/StreamableHTTP
 - 1.1 Configuration
 - 1.2 Example usage
 - 2. SSE to stdio
 - 2.1 Configuration
 - 2.2 Example usage
 - Named Servers
 - Installation
 - Installing via PyPI
 - Installing via Github repository (latest)
 - Installing as container
 - Troubleshooting
 - Extending the container image
 - Docker ...

Sections: mcp-proxy, About, 1. stdio to SSE/StreamableHTTP, 1.1 Configuration, 1.2 Example usage, 2. SSE to stdio, 2.1 Configuration, 2.2 Example usage, Named Servers, Troubleshooting, Extending the container image, Docker Compose Setup, Command line arguments, Example config file

</details>

### hdf5plugin

HDF5 Plugins for Windows, MacOS, and Linux

`pip install hdf5plugin` · installs (wheel) · licence: not stated · rank 5546 · last release 2026-09-01 · [PyPI](https://pypi.org/project/hdf5plugin/) · [docs](http://www.silx.org/doc/hdf5plugin/latest/) · [source](https://github.com/silx-kit/hdf5plugin)

<details><summary>README extract</summary>

*hdf5plugin* provides HDF5 compression filters (namely: Blosc, Blosc2, BitShuffle, BZip2, Htj2k, FciDecomp, LZ4, Sperr, SZ, SZ3, Zfp, ZStd) and makes them usable from h5py.

See documentation.

Sections: hdf5plugin, How-to use

</details>

### intel-cmplr-lib-ur

Intel® oneAPI Unified Runtime Libraries package

`pip install intel-cmplr-lib-ur` · installs (wheel) · licence: Other/Proprietary License · rank 5548 · last release 2026-10-16 · [PyPI](https://pypi.org/project/intel-cmplr-lib-ur/)

<details><summary>README extract</summary>

This Intel® oneAPI Runtime COMMON LIBRARIES package contains shared common libraries needed to provide a unified interface to device agnostic runtimes such as DPC++ across a wide variety of software platforms. ...

</details>

### iterators

Iterator utility classes and functions

`pip install iterators` · installs (wheel) · licence: MIT License · rank 5551 · last release 2023-01-23 · [PyPI](https://pypi.org/project/iterators/)

<details><summary>README extract</summary>

Available at PyPi

Provides a wrapper class TimeoutIterator to add timeout feature to normal iterators

Example:
```python
from iterators import TimeoutIterator

def iter_simple():
    yield 1
    yield 2

def test_normal_iteration(self):
    i = iter_simple()
    it = TimeoutIterator(i)

    self.assertEqual(next(it), 1)
    self.assertEqual(next(it), 2)

    self.assertRaises(StopIteration, next, it)
    self.assertRaises(StopIteration, next, it)
```

Sections: Example, Run unit tests locally

</details>

### django-fsm

State machines for Python objects and Django models.

`pip install django-fsm` · installs (wheel) · licence: AGPL-3.0-or-later WITH viewflow-library-exception · rank 5561 · last release 2026-10-27 · [PyPI](https://pypi.org/project/django-fsm/)

_README extract left out: share-alike licence._

### youdotcom

The official You.com Python SDK.

`pip install youdotcom` · installs (wheel) · licence: MIT · rank 5562 · last release 2026-10-15 · [PyPI](https://pypi.org/project/youdotcom/) · [source](https://github.com/youdotcom-oss/youdotcom-python-sdk)

<details><summary>README extract</summary>

The official Python SDK for the You.com API: web search, citation-backed answers, page contents, and multi-step research.

Example:
```python
import os
from youdotcom import You

with You(api_key_auth=os.getenv("YDC_API_KEY"), timeout_ms=60_000) as you:
    res = you.answer(query="What caused the 2008 financial crisis?")
    print(res.answer)
```

Sections: Quickstart, The APIs, Answer, Search, Page content extraction, Knowledge results, Research, Async, Long-running research, Authentication, Errors, Configuration, Retries, Timeouts

</details>

### LunarCalendar

A lunar calendar converter, including a number of lunar and solar holidays, mainly from China.

`pip install LunarCalendar` · installs (wheel) · licence: MIT License · rank 5579 · last release 2018-06-13 · [PyPI](https://pypi.org/project/LunarCalendar/)

<details><summary>README extract</summary>

Features:
Chinese version(中文版) is provided.

LunarCalendar is a Lunar-Solar Converter, containing a number of lunar and solar festivals in China.

Korean, Japanese or Vietnamese lunar calendar is the same as Chinese calendar, but has different festivals. ...

Example:
```python
import datetime
from lunarcalendar import Converter, Solar, Lunar, DateNotExist

solar = Solar(2018, 1, 1)
print(solar)
lunar = Converter.Solar2Lunar(solar)
print(lunar)
solar = Converter.Lunar2Solar(lunar)
print(solar)
print(solar.to_date(), type(solar.to_date()))
```

Sections: LunarCalendar: A Lunar-Solar Converter, Overview, Features, Console Commands, Quickstart, About

</details>

### logtail-python

Better Stack client library

`pip install logtail-python` · installs (wheel) · licence: ISC License (ISCL) · rank 5594 · last release 2026-11-06 · [PyPI](https://pypi.org/project/logtail-python/)

<details><summary>README extract</summary>

📣 Logtail is now part of Better Stack. Learn more ⇗

Experience SQL-compatible structured log management based on ClickHouse. Learn more ⇗

Getting started ⇗

Please let us know at hello@betterstack.com. We're happy to help!

ISC license, example project

Sections: Better Stack Python client, Documentation, Need help?

</details>

### mdformat_tables

An mdformat plugin for rendering tables.

`pip install mdformat_tables` · installs (wheel) · licence: MIT License · rank 5615 · last release 2024-08-23 · [PyPI](https://pypi.org/project/mdformat_tables/)

<details><summary>README extract</summary>

[][ci-link]
[][cov-link]
[][pypi-link]

An mdformat plugin for rendering tables.

For example, converting:

to:

For further examples, see tests/fixtures.md in the repository.

Sections: mdformat-tables, Publish to PyPi

</details>

### nvidia-ml-py3

Python Bindings for the NVIDIA Management Library

`pip install nvidia-ml-py3` · installs from source (sdist only) · licence: BSD License · rank 5621 · last release 2017-06-03 · [PyPI](https://pypi.org/project/nvidia-ml-py3/)

<details><summary>README extract</summary>

Patched to support Python 3

Provides a Python interface to GPU management and monitoring functions.

This is a wrapper around the NVML library.
For information about the NVML library, see the NVML developer page

Download the latest package from: ...

Example:
```python
nvmlReturn_t nvmlDeviceGetEccMode(nvmlDevice_t device,
                                  nvmlEnableState_t *current,
                                  nvmlEnableState_t *pending);

>>> nvmlInit()
>>> handle = nvmlDeviceGetHandleByIndex(0)
>>> (current, pending) = nvmlDeviceGetEccMode(handle)
```

Sections: pyNVML, Python bindings to the NVIDIA Management Library, REQUIRES, USAGE, FUNCTIONS, VARIABLES, COPYRIGHT

</details>

### postgrid-python

The official Python library for the PostGrid API

`pip install postgrid-python` · installs (wheel) · licence: Apache Software License · rank 5625 · last release 2026-06-15 · [PyPI](https://pypi.org/project/postgrid-python/) · [source](https://github.com/postgrid/postgrid-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The PostGrid Python library provides convenient access to the PostGrid REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx. ...

Example:
```python
import os
from postgrid import PostGrid

client = PostGrid(
    print_mail_api_key=os.environ.get(
        "POSTGRID_PRINT_MAIL_API_KEY"
    ),  # This is the default and can be omitted
)

contact = client.print_mail.contacts.create(
    address_line1="addressLine1",
    country_code="countryCode",
    first_name="firstName",
)
print(contact.id)
```

...

</details>

### plux

A dynamic code loading framework for building pluggable Python distributions

`pip install plux` · installs (wheel) · licence: Apache-2.0 · rank 5635 · last release 2026-03-31 · [PyPI](https://pypi.org/project/plux/) · [source](https://github.com/localstack/plux)

<details><summary>README extract</summary>

plux is the dynamic code loading framework used in LocalStack.

Overview

Plux builds a higher-level plugin mechanism around Python's entry point mechanism.
It provides tools to load plugins from entry points at run time, and to discover entry points from plugins at build time (so you don't have to declare entry points statically in your ...

Example:
```python
from plux import Plugin

# abstract case (not discovered at build time, missing name)
class CliPlugin(Plugin):
    namespace = "my.plugins.cli"

    def load(self, cli):
        self.attach(cli)

    def attach(self, cli):
        raise NotImplementedError

# discovered at build time (has a namespace, name, and is a Plugin)
...
```

...

</details>

### pgzip

A multi-threading implementation of Python gzip module

`pip install pgzip` · installs (wheel) · licence: MIT License · rank 5649 · last release 2025-12-23 · [PyPI](https://pypi.org/project/pgzip/)

<details><summary>README extract</summary>

👷👷👷 Maintainers Wanted 👷👷👷 See

`pgzip` is a multi-threaded `gzip` implementation for `python` that increases the compression and decompression performance.

Compression and decompression performance gains are made by parallelizing the usage of block indexing within a `gzip` file. ...

Example:
```python
import pgzip

s = "a big string..."

# An explanation of parameters:
# `thread=8` - Use 8 threads to compress. `None` or `0` uses all cores (default)
# `blocksize=2*10**8` - Use a compression block size of 200MB
with pgzip.open("test.txt.gz", "wt", thread=8, blocksize=2*10**8) as fw:
    fw.write(s)
```

Sections: pgzip, Usage and Examples, CLI, Programatically, Performance, Compression Performance, Decompression Performance, Warning

</details>

### django-tailwind

Tailwind CSS Framework for Django projects

`pip install django-tailwind` · installs (wheel) · licence: MIT · rank 5654 · last release 2026-10-13 · [PyPI](https://pypi.org/project/django-tailwind/) · [docs](https://django-tailwind.readthedocs.io/)

<details><summary>README extract</summary>

This project provides a convenient way to integrate the *Tailwind CSS* framework into a Django project.
It creates a new Django app (named theme by default) that includes all the necessary files and configurations to get
started with *Tailwind CSS* quickly and without even needing to install `Node.js` if you choose the standalone binary mode.

Features:
* An opinionated *Tailwind CSS* setup that makes your life easier;
* Two installation modes: standalone binary (works without `Node.js`) or npm-based (`Node.js` required);
* Hot reloading of CSS, configuration files, and *Django* templates. ...

Sections: Goal, Features, Requirements, Documentation, Getting Started, Bugs and suggestions

</details>

### json_logic_qubit

Build complex rules, serialize them as JSON, and execute them in Python

`pip install json_logic_qubit` · installs (wheel) · licence: MIT License · rank 5656 · last release 2018-08-15 · [PyPI](https://pypi.org/project/json_logic_qubit/)

<details><summary>README extract</summary>

This parser accepts JsonLogic rules and
executes them in Python.

This is a Python porting of the excellent GitHub project by
jwadhams for JavaScript:
json-logic-js.

All credit goes to him, this is simply an implementation of the same
logic in Python (small differences below). ...

Example:
```python
from json_logic import jsonLogic
jsonLogic( { "==" : [1, 1] } )
# True
```

Sections: json-logic-py, Examples, Simple, Compound, Data-Driven

</details>

### Lazify

Lazify all the things!

`pip install Lazify` · installs (wheel) · licence: BSD · rank 5662 · last release 2018-06-14 · [PyPI](https://pypi.org/project/Lazify/)

<details><summary>README extract</summary>

Lazify aims to be the defacto standard and most complete library for Python
tools related to lazy evaluation.

It's originally based on Babel and its `babel.support.LazyProxy` class.

</details>

### standard-telnetlib

Standard library telnetlib redistribution. "dead battery".

`pip install standard-telnetlib` · installs (wheel) · licence: Python Software Foundation License · rank 5669 · last release 2024-10-30 · [PyPI](https://pypi.org/project/standard-telnetlib/)

<details><summary>README extract</summary>

Python is moving forward! Python finally started to remove dead batteries.
For more information, see PEP 594.

If your project depends on a module that has been removed from the standard,
here is the redistribution of the dead batteries.

</details>

### rule-engine

A lightweight, optionally typed expression language with a custom grammar for matching arbitrary Python objects.

`pip install rule-engine` · installs (wheel) · licence: BSD-3-Clause · rank 5692 · last release 2026-10-28 · [PyPI](https://pypi.org/project/rule-engine/)

<details><summary>README extract</summary>

A lightweight, optionally typed expression language with a custom grammar for matching arbitrary Python objects.

Documentation is available at

:Warning:
 Version 6.0 will remove support for Python version 3.10. There is currently no timeline for its release. ...

Example:
```python
import rule_engine
# match a literal first name and applying a regex to the email
rule = rule_engine.Rule(
    'first_name == "Luke" and email =~ ".*@rebels.org$"'
) # => <Rule text='first_name == "Luke" and email =~ ".*@rebels.org$"' >
rule.matches({
    'first_name': 'Luke', 'last_name': 'Skywalker', 'email': 'luke@rebels.org'
}) # => True
...
```

Sections: Rule Engine, Example Usage

</details>

### tailscale

Asynchronous Python client for the Tailscale API.

`pip install tailscale` · installs (wheel) · licence: MIT · rank 5695 · last release 2026-10-10 · [PyPI](https://pypi.org/project/tailscale/) · [docs](https://github.com/frenck/python-tailscale) · [source](https://github.com/frenck/python-tailscale)

<details><summary>README extract</summary>

[][releases]
[][pypi]

[](LICENSE.md)

[][build]
[][codecov]
[][scorecard]
[][devcontainer]

[][github-sponsors]

[][patreon]

Asynchronous Python client for the Tailscale API.

This package allows you to control and monitor Tailscale clients
programmatically. It is mainly created to allow third-party programs to
integrate with Tailscale. ...

Example:
```python
import asyncio

from tailscale import Tailscale

async def main() -> None:
    """Show example of using the Tailscale API client."""
    async with Tailscale(api_key="tskey-api-...") as tailscale:
        devices = await tailscale.devices()

        for device in devices.values():
            print(f"{device.hostname} ({device.os})")
...
```

...

</details>

### urllib3-secure-extra

Marker library to detect whether urllib3 was installed with the deprecated [secure] extra

`pip install urllib3-secure-extra` · installs (wheel) · licence: MIT License · rank 5709 · last release 2022-08-01 · [PyPI](https://pypi.org/project/urllib3-secure-extra/) · [source](https://github.com/urllib3/urllib3-secure-extra)

<details><summary>README extract</summary>

Marker library to detect whether urllib3 was installed with the deprecated `[secure]` extra.

Read the issue on the urllib3 repository for more information.

</details>

### easy-thumbnails

Easy thumbnails for Django

`pip install easy-thumbnails` · installs (wheel) · licence: BSD License · rank 5714 · last release 2025-08-17 · [PyPI](https://pypi.org/project/easy-thumbnails/)

<details><summary>README extract</summary>

A powerful, yet easy to implement thumbnailing application for Django 4.2+

Below is a quick summary of usage. For more comprehensive information, view the
full documentation online or the peruse the project's `docs` directory.


Version 2.8.0 adds support for thumbnailing SVG images when installed with the `[svg]` extra. ...

Example:
```python
from easy_thumbnails.files import get_thumbnailer
thumb_url = get_thumbnailer(profile.photo)['avatar'].url
```

Sections: Easy Thumbnails, Breaking News, Example usage, Using a predefined alias, Manually specifying size / options, Using in combination with other thumbnailers, Fields, Thumbnail options, `crop`, `quality=XX`, `keep_icc_profile`, Other options, Changes, 2.10.1 (2025-08-17)

</details>

### pyftdi

FTDI device driver (pure Python)

`pip install pyftdi` · installs (wheel) · licence: BSD-3-Clause · rank 5721 · last release 2026-06-02 · [PyPI](https://pypi.org/project/pyftdi/)

<details><summary>README extract</summary>

The latest PyFtdi online documentation is always available from
here.

Beware the online version may be more recent than the PyPI hosted version, as
intermediate development versions are not published to
PyPi.

PyFtdi documentation can be locally build with Sphinx, see the installation
instructions. ...

Features:
PyFtdi aims at providing a user-space driver for popular FTDI devices,
implemented in pure Python language.

Supported FTDI devices include:

* UART and GPIO bridges

 * FT232R (single port, 3Mbps)
 * FT230X/FT231X/FT234X (single port, 3Mbps) ...

Sections: PyFtdi, Documentation, Source code, Overview, Features

</details>

### textwrap3

textwrap from Python 3.6 backport (plus a few tweaks)

`pip install textwrap3` · installs (wheel) · licence: Python Software Foundation License · rank 5728 · last release 2019-01-23 · [PyPI](https://pypi.org/project/textwrap3/)

<details><summary>README extract</summary>

travisciversionversionsimplswheelcoverage|

`textwrap3` is a compatibility back-port of Python 3.6's `textwrap`
module that supports Python 2.6 forward. (Though honestly, if you're not
already using *at least* 2.7, you're way behind the times!) ...

Example:
```python
from textwrap3 import wrap

text = 'long text here...'
print(wrap(text, 40))
```

Sections: Bias and Tweaks, Notes

</details>

### python-toon

TOON (Token-Oriented Object Notation) encoder/decoder for Python - Bidirectional JSON-to-TOON converter optimized for LLMs

`pip install python-toon` · installs (wheel) · licence: MIT · rank 5733 · last release 2026-09-29 · [PyPI](https://pypi.org/project/python-toon/) · [docs](https://github.com/toon-format/spec) · [source](https://github.com/xaviviro/python-toon)

<details><summary>README extract</summary>

> Note: This is an unofficial community implementation. The official TOON projects live in the toon-format organization, including the specification and the official Python implementation toon-format/toon-python.

Token-Oriented Object Notation for Python ...

Features:
- 30-60% token reduction compared to standard JSON on uniform data
- Minimal syntax: Eliminates redundant punctuation (braces, brackets, most quotes)
- Tabular arrays: CSV-like rows for uniform object collections, including nested uniform objects ...

Example:
```python
from toon import encode

# Simple object
data = {"name": "Alice", "age": 30}
print(encode(data))
# name: Alice
# age: 30

# Tabular array (uniform objects)
users = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
...

</details>

### soniox

The official Python SDK for the Soniox API (STT, REST)

`pip install soniox` · installs (wheel) · licence: Apache-2.0 · rank 5748 · last release 2026-11-03 · [PyPI](https://pypi.org/project/soniox/) · [docs](https://soniox.com/docs) · [source](https://github.com/soniox/soniox-python)

<details><summary>README extract</summary>

The SDK exposes two clients: `SonioxClient` (sync) and `AsyncSonioxClient` (async). Each client supports:

- STT over REST (`client.stt`) and realtime WebSocket (`client.realtime.stt`)
- TTS over REST (`client.tts`) and realtime WebSocket (`client.realtime.tts`) ...

Example:
```python
summary = client.usage.summary(
    start_time="2026-04-01T00:00:00Z",
    end_time="2026-05-01T00:00:00Z",
)
print(summary.total.total_cost_usd)
for entry in summary.models:
    print(entry.model, entry.total_cost_usd)
```

Sections: Soniox Python SDK, Quick run (STT + TTS, REST + realtime), Usage and cost, Organization administration, Repository layout, Docs, Resources

</details>

### flake8-annotations

Flake8 Type Annotation Checks

`pip install flake8-annotations` · installs (wheel) · licence: MIT · rank 5759 · last release 2026-10-29 · [PyPI](https://pypi.org/project/flake8-annotations/) · [docs](https://github.com/sco1/flake8-annotations/blob/main/README.md) · [source](https://github.com/sco1/flake8-annotations)

<details><summary>README extract</summary>

`flake8-annotations` is a plugin for Flake8 that detects the absence of PEP 3107-style function annotations.

What this won't do: replace mypy, check type comments (see: PEP 484), check variable annotations (see: PEP 526), or respect stub files.

Example:
```python
import functools

@functools.singledispatch
def foo(a):
    print(a)

@foo.register
def _(a: list) -> None:
    for idx, thing in enumerate(a):
        print(idx, thing)
```

...

</details>

### annotatedyaml

Annotated YAML that supports secrets for Python

`pip install annotatedyaml` · installs (wheel) · licence: Apache-2.0 · rank 5765 · last release 2025-10-04 · [PyPI](https://pypi.org/project/annotatedyaml/) · [docs](https://annotatedyaml.readthedocs.io) · [source](https://github.com/home-assistant-libs/annotatedyaml)

<details><summary>README extract</summary>

Documentation:

Source Code:

Annotated YAML that supports secrets for Python

</details>

### formic2

An implementation of Apache Ant FileSet and Globs

`pip install formic2` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 5779 · last release 2018-05-28 · [PyPI](https://pypi.org/project/formic2/)

_README extract left out: share-alike licence._

### pytest-harvest

Store data created during your pytest tests execution, and retrieve it at the end of the session, e.g. for applicative benchmarking purposes.

`pip install pytest-harvest` · installs (wheel) · licence: BSD License · rank 5787 · last release 2024-03-16 · [PyPI](https://pypi.org/project/pytest-harvest/)

<details><summary>README extract</summary>

Store data created during your `pytest` tests execution, and retrieve it at the end of the session, e.g. for applicative benchmarking purposes.

The documentation for users is available here:

A readme for developers is available here:

</details>

### modelsearch

A library for indexing Django models with Elasicsearch, OpenSearch or database and searching them with the Django ORM.

`pip install modelsearch` · installs (wheel) · licence: BSD-3-Clause · rank 5788 · last release 2026-08-11 · [PyPI](https://pypi.org/project/modelsearch/) · [docs](https://django-modelsearch.readthedocs.io/en/latest) · [source](https://github.com/wagtail/django-modelsearch)

<details><summary>README extract</summary>

Django ModelSearch allows you to index Django models and search them using the ORM!

It supports PostgreSQL FTS, SQLite FTS5, MySQL FTS, MariaDB FTS, Elasticsearch (7.x, 8.x, and 9.x), and OpenSearch (2.x and 3.x).

Features:

- Index models in Elasticsearch and OpenSearch and query with the Django ORM ...

Example:
```python
from modelsearch import index
from modelsearch.queryset import SearchableQuerySetMixin

# This mixin adds a .search() method to the models QuerySet
class SongQuerySet(SearchableQuerySetMixin, models.QuerySet):
    pass

# Create a model that inherits from Indexed
class Song(index.Indexed, models.Model):
    name = models.TextField()
...
```

Sections: Django ModelSearch, Indexing, Searching

</details>

### isoweek

Objects representing a week

`pip install isoweek` · installs (wheel) · licence: BSD License · rank 5789 · last release 2017-01-04 · [PyPI](https://pypi.org/project/isoweek/)

<details><summary>README extract</summary>

The isoweek module provide the class *Week*. Instances represent specific weeks
spanning Monday to Sunday. There are 52 or 53 numbered weeks in a year. Week
1 is defined to be the first week with 4 or more days in January.

It's called isoweek because this is the week definition of ISO 8601. ...

Example:
```python
from isoweek import Week
w = Week(2011, 20)
print "Week %s starts on %s" % (w, w.monday())

print "Current week number is", Week.thisweek().week
print "Next week is", Week.thisweek() + 1
```

Sections: ISO Week, Reference

</details>

### jschon

A JSON toolkit for Python developers.

`pip install jschon` · installs (wheel) · licence: MIT License · rank 5794 · last release 2023-10-22 · [PyPI](https://pypi.org/project/jschon/)

<details><summary>README extract</summary>

A JSON toolkit for Python developers.

Features:
* JSON Schema validator implementation
 (drafts 2019-09, 2020-12)

 * Schema compilation and indexing
 * $ref loading from local and remote sources
 * Support for custom keywords, vocabularies and meta-schemas
 * Support for format validation ...

Example:
```python
from jschon import create_catalog, JSON, JSONSchema

create_catalog('2020-12')

demo_schema = JSONSchema({
    "$id": "
    "$schema": "
    "type": "array",
    "items": {
        "anyOf": [
            {
                "type": "string",
                "description": "Cool! We got a string here!"
            },
            {
...
```

Sections: jschon, Features, Basic usage, Links

</details>

### groundx

(no summary)

`pip install groundx` · installs (wheel) · licence: MIT License · rank 5801 · last release 2026-10-30 · [PyPI](https://pypi.org/project/groundx/) · [source](https://github.com/eyelevelai/groundx-python)

<details><summary>README extract</summary>

The GroundX Python library provides convenient access to the GroundX API from Python.

API reference documentation is available here.

Example:
```python
from groundx import Document, GroundX

client = GroundX(
    api_key="YOUR_API_KEY",
)

client.ingest(
    documents=[
        Document(
            bucket_id=1234,
            file_name="my_file1.txt",
            file_type="txt",
            source_url="
        )
    ],
)
```

Sections: GroundX Python Library, Documentation, Reference, Usage, Extraction Workflows, Async Client, Exception Handling, Advanced, Retries, Timeouts, Custom Client, Protected files

</details>

### barcodenumber

Python module to validate Product codes (EAN, EAN13, ISBN,...)

`pip install barcodenumber` · installs (wheel) · licence: GNU General Public License (GPL) · rank 5807 · last release 2019-11-06 · [PyPI](https://pypi.org/project/barcodenumber/)

_README extract left out: share-alike licence._

### flake8-eradicate

Flake8 plugin to find commented out code

`pip install flake8-eradicate` · installs (wheel) · licence: MIT License · rank 5811 · last release 2023-05-31 · [PyPI](https://pypi.org/project/flake8-eradicate/) · [source](https://github.com/wemake-services/flake8-eradicate)

<details><summary>README extract</summary>

`flake8` plugin to find commented out (or so called "dead") code.

This is quite important for the project in a long run.
Based on `eradicate` project.

Sections: flake8-eradicate, Usage, Options, Error codes, Output example

</details>

### xvfbwrapper

Manage headless displays with Xvfb (X virtual framebuffer)

`pip install xvfbwrapper` · installs (wheel) · licence: MIT · rank 5832 · last release 2026-10-23 · [PyPI](https://pypi.org/project/xvfbwrapper/) · [docs](https://coreygoldberg.com/xvfbwrapper) · [source](https://github.com/cgoldberg/xvfbwrapper)

<details><summary>README extract</summary>

`xvfbwrapper` is a Python library for managing X11 virtual displays with
Xvfb (X virtual framebuffer),
a virtual X server that runs without a physical display. It provides the `Xvfb` class,
a Python interface for configuring and controlling the Xvfb program.

See the module API documentation for more information. ...

Example:
```python
from xvfbwrapper import Xvfb

xvfb = Xvfb()
xvfb.start()
try:
    # launch stuff inside virtual display here
finally:
    xvfb.stop()
```

...

</details>

### weighted-levenshtein

Library providing functions to calculate Levenshtein distance, Optimal String Alignment distance, and Damerau-Levenshtein distance, where the cost of each operation can be weighted by letter.

`pip install weighted-levenshtein` · installs from source (sdist only) · licence: MIT License · rank 5841 · last release 2023-01-31 · [PyPI](https://pypi.org/project/weighted-levenshtein/)

<details><summary>README extract</summary>

Most existing Levenshtein libraries are not very flexible: all edit operations have cost 1.

However, sometimes not all edits are created equal. For instance, if you are doing OCR correction, maybe substituting '0' for 'O' should have a smaller cost than substituting 'X' for 'O'. ...

Example:
```python
import numpy as np
from weighted_levenshtein import lev, osa, dam_lev

insert_costs = np.ones(128, dtype=np.float64)  # make an array of all 1's of size 128, the number of ASCII characters
insert_costs[ord('D')] = 1.5  # make inserting the character 'D' have cost 1.5 (instead of 1)

# you can just specify the insertion costs
...
```

Sections: weighted-levenshtein, Use Cases, More Information, Usage Example, Detailed Documentation, Important Notes, Use as Cython library

</details>

### Salesforce-FuelSDK-Sans

Salesforce Marketing Cloud Fuel SDK for Python

`pip install Salesforce-FuelSDK-Sans` · installs (wheel) · licence: MIT License · rank 5851 · last release 2022-06-20 · [PyPI](https://pypi.org/project/Salesforce-FuelSDK-Sans/)

<details><summary>README extract</summary>

Salesforce Marketing Cloud Fuel SDK for Python

This is a fork of the original repo,
the original repo is not maintained, so I decided to fork and maintain.

Features:
The Fuel SDK for Python provides easy access to Salesforce Marketing Cloud's Fuel API Family services, including a collection of REST APIs and a SOAP API. ...

Example:
```python
stubObj = ET_Client.ET_Client(
  False, False,
  {
      'clientid': '<CLIENT_ID>',
      'clientsecret': '<CLIENT_SECRET>',
      'defaultwsdl': '
      'authenticationurl': '<AUTH TENANT SPECIFIC ENDPOINT>',
      'baseapiurl': '<REST TENANT SPECIFIC ENDPOINT>',
      'soapendpoint': '<SOAP TENANT SPECIFIC ENDPOINT>',
...
```

...

</details>

### pyperf

Python module to run and analyze benchmarks

`pip install pyperf` · installs (wheel) · licence: MIT License · rank 5854 · last release 2026-02-07 · [PyPI](https://pypi.org/project/pyperf/)

<details><summary>README extract</summary>

The Python `pyperf` module is a toolkit to write, run and analyze benchmarks.

Features:
* Simple API to run reliable benchmarks
* Automatically calibrate a benchmark for a time budget.
* Spawn multiple worker processes.
* Compute the mean and standard deviation.
* Detect if a benchmark result seems unstable. ...

Example:
```python
# !/usr/bin/env python3
import pyperf

runner = pyperf.Runner()
runner.timeit(name="sort a sorted list",
              stmt="sorted(s, key=f)",
              setup="f = lambda x: x; s = list(range(1000))")
```

Sections: pyperf, Features, Usage, Quick Links

</details>

### uhashring

Full featured consistent hashing python library compatible with ketama.

`pip install uhashring` · installs (wheel) · licence: BSD-3-Clause · rank 5855 · last release 2026-08-03 · [PyPI](https://pypi.org/project/uhashring/)

<details><summary>README extract</summary>

uhashring implements consistent hashing in pure Python.

Consistent hashing is mostly used on distributed
systems/caches/databases as this avoid the total reshuffling of your
key-node mappings when adding or removing a node in your ring (called
continuum on libketama). ...

Example:
```python
from uhashring import HashRing

# create a consistent hash ring of 3 nodes of weight 1
hr = HashRing(nodes=['node1', 'node2', 'node3'])

# get the node name for the 'coconut' key
target_node = hr.get_node('coconut')
```

Sections: uhashring, Python 2 EOL, IMPORTANT, Usage, Basic usage, Ketama usage, Advanced usage, Default node configuration, Adding / removing nodes, Customizable node weight calculation, Customizable hash function, HashRing options, Available methods, Available properties

</details>

### restate-sdk

A Python SDK for Restate

`pip install restate-sdk` · installs (wheel) · licence: not stated · rank 5856 · last release 2026-11-05 · [PyPI](https://pypi.org/project/restate-sdk/) · [docs](https://docs.restate.dev) · [source](https://github.com/restatedev/sdk-python)

<details><summary>README extract</summary>

Restate is a system for easily building resilient applications using *distributed durable async/await*. This repository contains the Restate SDK for writing services in Python.

Example:
```python
import restate

greeter = restate.Service("greeter")

@greeter.handler()
async def greet(ctx: restate.Context, name: str) -> str:
    return f"Hello {name}!"

app = restate.app(services=[greeter])
```

Sections: Restate Python SDK, Using the SDK, Serving using an ASGI server, Connecting to Restate Cloud, Clients, Versions, Releasing the package

</details>

### python-terraform

This is a python module provide a wrapper of terraform command line tool

`pip install python-terraform` · installs from source (sdist only) · licence: MIT License · rank 5871 · last release 2019-06-21 · [PyPI](https://pypi.org/project/python-terraform/)

### openai-guardrails

OpenAI Guardrails: A framework for building safe and reliable AI systems.

`pip install openai-guardrails` · installs (wheel) · licence: MIT · rank 5877 · last release 2026-10-26 · [PyPI](https://pypi.org/project/openai-guardrails/) · [source](https://github.com/openai/openai-guardrails-python)

<details><summary>README extract</summary>

Add configurable safety and compliance checks to LLM applications. OpenAI Guardrails wraps the OpenAI Python client to validate inputs and outputs, and integrates with the OpenAI Agents SDK.

Configure guardrails · Documentation · Examples

Example:
```python
from pathlib import Path

from guardrails import GuardrailsOpenAI, GuardrailTripwireTriggered

client = GuardrailsOpenAI(config=Path("guardrails_config.json"))

try:
    # Chat Completions API
    chat = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": "Hello world"}],
    )
...
```

Sections: OpenAI Guardrails: Python (Preview), Quickstart, Agents SDK, Evaluations, Available Guardrails, Disclaimers

</details>

### pluralizer

Singularize or pluralize a given word using a pre-defined list of rules

`pip install pluralizer` · installs (wheel) · licence: MIT · rank 5884 · last release 2025-06-11 · [PyPI](https://pypi.org/project/pluralizer/)

<details><summary>README extract</summary>

Features:
This repo is simply a Python port of which has > 1.4m github usages and 3.5 million downloads per week when I evaluating different libraries. ...

Example:
```python
from pluralizer import Pluralizer

pluralizer = Pluralizer()

assert pluralizer.pluralize('apple', 1, False) == 'apple'
assert pluralizer.pluralize('apple', 1, True) == '1 apple'
assert pluralizer.pluralize('apple', 2, False) == 'apples'
assert pluralizer.pluralize('apple', 2, True) == '2 apples'

assert pluralizer.plural('apple') == 'apples'
...
```

Sections: Why this project?, Usage

</details>

### shodan

Python library and command-line utility for Shodan (https://developer.shodan.io)

`pip install shodan` · installs from source (sdist only) · licence: MIT License · rank 5889 · last release 2023-12-17 · [PyPI](https://pypi.org/project/shodan/)

<details><summary>README extract</summary>

Shodan is a search engine for Internet-connected devices. Google lets you search for websites,
Shodan lets you search for devices. This library provides developers easy access to all of the
data stored in Shodan in order to automate tasks and integrate into existing tools.

Features:
- Search Shodan
- Fast/ bulk IP lookups
- Streaming API support for real-time consumption of Shodan firehose
- Network alerts (aka private firehose)
- Manage Email Notifications
- Exploit search API fully implemented
- Bulk data downloads ...

Example:
```python
from shodan import Shodan

api = Shodan('MY API KEY')

# Lookup an IP
ipinfo = api.host('8.8.8.8')
print(ipinfo)

# Search for websites that have been "hacked"
for banner in api.search_cursor('http.title:"hacked by"'):
    print(banner)

...

</details>

### twelvelabs

(no summary)

`pip install twelvelabs` · installs (wheel) · licence: not stated · rank 5899 · last release 2026-11-05 · [PyPI](https://pypi.org/project/twelvelabs/)

<details><summary>README extract</summary>

The TwelveLabs Python SDK provides a set of intuitive classes and methods that streamline platform interaction, minimizing the need for boilerplate code.

> Note: The examples in this guide show only the required parameters. For the complete guides, see the Search, Analyze videos, and Create embeddings pages. ...

Example:
```python
import time
from twelvelabs import TwelveLabs
```

Sections: TwelveLabs Python SDK, Prerequisites, Initialize the SDK, Use the SDK, Upload a video, Search, Create an index, Add your video to the index, Monitor the indexing process, Run a query, Analyze videos, Create embeddings, Error Handling

</details>

### proxmoxer

Python Wrapper for the Proxmox 2.x API (HTTP and SSH)

`pip install proxmoxer` · installs (wheel) · licence: MIT License · rank 5921 · last release 2026-03-04 · [PyPI](https://pypi.org/project/proxmoxer/)

<details><summary>README extract</summary>

master branch:

develop branch:

Proxmoxer is a python wrapper around the Proxmox REST API v2.
It currently supports the Proxmox services of Proxmox Virtual Environment (PVE), Proxmox Mail Gateway (PMG), and Proxmox Backup Server (PBS).

It was inspired by slumber, but it is dedicated only to Proxmox. ...

Example:
```python
from proxmoxer import ProxmoxAPI

proxmox = ProxmoxAPI(
    "proxmox_host", user="admin@pam", password="secret_word", verify_ssl=False
)
```

Sections: Proxmoxer: A Python wrapper for Proxmox REST API, Full Documentation is available at

</details>

### rich-text-renderer

Contentful Rich Text Renderer

`pip install rich-text-renderer` · installs (wheel) · licence: MIT License · rank 5935 · last release 2023-10-26 · [PyPI](https://pypi.org/project/rich-text-renderer/)

<details><summary>README extract</summary>

Contentful provides a content infrastructure for digital teams to power content in websites, apps, and devices. Unlike a CMS, Contentful was built to integrate with the modern software stack. ...

Example:
```python
from rich_text_renderer import RichTextRenderer

renderer = RichTextRenderer()
```

Sections: Contentful Rich Text Renderer, Usage, Using different renderers, Dealing with unknown node types

</details>

### python-graphql-client

Python GraphQL Client

`pip install python-graphql-client` · installs (wheel) · licence: MIT License · rank 5936 · last release 2021-03-04 · [PyPI](https://pypi.org/project/python-graphql-client/)

<details><summary>README extract</summary>

> Simple package for making requests to a graphql server.

<!-- Badges here. -->

Example:
```python
from python_graphql_client import GraphqlClient

# Instantiate the client with an endpoint.
client = GraphqlClient(endpoint="

# Create the query string and variables required for the request.
query = """
    query countryQuery($countryCode: String) {
        country(code:$countryCode) {
            code
            name
        }
    }
"""
...
```

Sections: Python GraphQL Client, Usage, Advanced Usage, Disable SSL verification, Custom Authentication, Roadmap

</details>

### javalang

Pure Python Java parser and tools

`pip install javalang` · installs (wheel) · licence: MIT License · rank 5938 · last release 2020-03-28 · [PyPI](https://pypi.org/project/javalang/)

<details><summary>README extract</summary>

javalang is a pure Python library for working with Java source
code. javalang provies a lexer and parser targeting Java 8. The
implementation is based on the Java language spec available at

</details>

### skills-ref

Reference library for Agent Skills

`pip install skills-ref` · installs (wheel) · licence: Apache-2.0 · rank 5957 · last release 2026-01-10 · [PyPI](https://pypi.org/project/skills-ref/) · [docs](https://agentskills.io) · [source](https://github.com/anthropics/agentskills)

<details><summary>README extract</summary>

Agent Skills are a simple, open format for giving agents new capabilities and expertise.

Skills are folders of instructions, scripts, and resources that agents can discover and use to perform better at specific tasks. Write once, use everywhere.

Features:
- Validation: Check skills for proper format and required fields
- Parsing: Extract skill metadata from SKILL.md frontmatter
- Prompt Generation: Create XML blocks for agent system prompts ...

Example:
```python
from pathlib import Path
from skills_ref import validate, read_properties, to_prompt

# Validate a skill directory
errors = validate(Path("my-skill"))
if errors:
    print("Validation errors:", errors)
else:
    print("Valid skill!")

# Read skill properties
props = read_properties(Path("my-skill"))
...

</details>

### pyjks

Pure-Python Java Keystore (JKS) library

`pip install pyjks` · installs (wheel) · licence: MIT License · rank 5972 · last release 2020-04-19 · [PyPI](https://pypi.org/project/pyjks/)

<details><summary>README extract</summary>

PyJKS enables Python projects to load and manipulate Java KeyStore
(JKS) data without a JVM dependency. PyJKS supports JKS, JCEKS, BKS
and UBER (BouncyCastle) keystores. Simply::

 pip install pyjks

Or::

 easy_install pyjks

Then::

 import jks

 keystore = jks.KeyStore.load('keystore.jks', 'passphrase') ...

</details>

### pynng

Networking made simply using nng

`pip install pynng` · installs (wheel) · licence: MIT License · rank 5974 · last release 2026-02-04 · [PyPI](https://pypi.org/project/pynng/) · [docs](https://pynng.readthedocs.io/en/latest/) · [source](https://github.com/codypiersall/pynng)

<details><summary>README extract</summary>

Ergonomic bindings for [nanomsg next generation] \(nng), in Python.
pynng provides a nice interface on top of the full power of nng. nng, and
therefore pynng, make it easy to communicate between processes on a single
computer or computers across a network. This library is compatible with Python
≥ 3.6. ...

Example:
```python
from pynng import Pair0

s1 = Pair0()
s1.listen('tcp://127.0.0.1:54321')
s2 = Pair0()
s2.dial('tcp://127.0.0.1:54321')
s1.send(b'Well hello there')
print(s2.recv())
s1.close()
s2.close()
```

Sections: This is pynng., Using pynng with an async framework

</details>

### anyconfig

Library provides common APIs to load and dump configuration files in various formats

`pip install anyconfig` · installs (wheel) · licence: MIT · rank 5977 · last release 2026-08-11 · [PyPI](https://pypi.org/project/anyconfig/) · [docs](http://python-anyconfig.readthedocs.org) · [source](https://github.com/ssato/python-anyconfig)

<details><summary>README extract</summary>

python-anyconfig [#]_ is a python library provides common APIs to load and dump
configuration files in various formats with some useful features such as
contents merge, templates, query, schema validation and generation support.

- Author: Satoru SATOH <satoru.satoh@gmail.com>
- License: MIT licensed

Features:
python-anyconfig provides very simple and unified APIs to process configuration
files in various formats and related functions: ...

Example:
```python
import anyconfig

# Config type (format) is automatically detected by filename (file
# extension) in some cases.
conf1 = anyconfig.load("/path/to/foo/conf.d/a.yml")

# Similar to the above but the input is pathlib.Path object.
import pathlib
path_1 = pathlib.Path("/path/to/foo/conf.d/a.yml")
conf1_1 = anyconfig.load(path_1)

...
```
...

</details>

### mkl

Intel® oneAPI Math Kernel Library

`pip install mkl` · installs (wheel) · licence: Other/Proprietary License · rank 5980 · last release 2026-10-16 · [PyPI](https://pypi.org/project/mkl/)

<details><summary>README extract</summary>

Intel® oneAPI Math Kernel Library (Intel® oneMKL) is a computing math library of highly optimized, extensively threaded routines for applications that require maximum performance. This package provides C and Data Parallel C++ (DPC++) programming language interfaces. ...

</details>

### openxlab

openxlab tools

`pip install openxlab` · installs (wheel) · licence: Apache License 2.0 · rank 6001 · last release 2025-10-21 · [PyPI](https://pypi.org/project/openxlab/) · [source](https://github.com/xxx/xxxx)

<details><summary>README extract</summary>

Example:
```python
def get_jwt(ak=None, sk=None):
    return get_token(ak, sk).jwt
```

Sections: openxlab-cli, Getting started, 代码结构, 架构说明, 安装依赖环境, 本地测试, testpypi 联调, ak和sk的设置, token的获取, v0.1.0

</details>

### filehash

Module and command-line tool that wraps around hashlib and zlib to facilitate generating checksums / hashes of files and directories.

`pip install filehash` · installs (wheel) · licence: MIT License · rank 6011 · last release 2021-10-11 · [PyPI](https://pypi.org/project/filehash/)

<details><summary>README extract</summary>

Python module to facilitate calculating the checksum or hash of a file. Tested against Python 2.7.x, Python 3.6.x, Python 3.7.x, Python 3.8.x, Python 3.9.x, Python 3.10.x, PyPy 2.7.x and PyPy3 3.7.x. Currently supports Adler-32, BLAKE2b, BLAKE2s, CRC32, MD5, SHA-1, SHA-224, SHA-256, SHA-384 and SHA-512. ...

Example:
```python
>>> import os
>>> from filehash import FileHash
>>> md5hasher = FileHash('md5')
>>> md5hasher.hash_file("./testdata/lorem_ipsum.txt")
'72f5d9e3a5fa2f2e591487ae02489388'
>>> sha1hasher = FileHash('sha1')
>>> sha1hasher.hash_dir("./testdata", "*.zip")
[FileHashResult(filename='lorem_ipsum.zip', hash='03da86258449317e8834a54cf8c4d5b41e7c7128')]
...
```

Sections: `filehash`, `FileHash` class, Example usage, `chkfilehash` command line tool

</details>

### ansiwrap

textwrap, but savvy to ANSI colors and styles

`pip install ansiwrap` · installs (wheel) · licence: Apache Software License · rank 6021 · last release 2019-01-23 · [PyPI](https://pypi.org/project/ansiwrap/)

<details><summary>README extract</summary>

travisciversionversionsimplswheelcoverage|

`ansiwrap` wraps text, like the standard `textwrap` module.
But it also correctly wraps text that contains ANSI control
sequences that colorize or style text. ...

Example:
```python
from future import print_function
from colors import *     # ansicolors on PyPI
from ansiwrap import *

s = ' '.join([red('this string'),
              blue('is going on a bit long'),
              green('and may need to be'),
              color('shortened a bit', fg='purple')])

print('-- original string --')
print(s)
print('-- now filled --')
...
```

</details>

### prefect-shell

Prefect integrations for interacting with shell commands.

`pip install prefect-shell` · installs (wheel) · licence: Apache Software License · rank 6025 · last release 2026-09-30 · [PyPI](https://pypi.org/project/prefect-shell/)

### attributes-doc

PEP 224 implementation

`pip install attributes-doc` · installs (wheel) · licence: MIT License · rank 6032 · last release 2026-08-18 · [PyPI](https://pypi.org/project/attributes-doc/) · [source](https://github.com/tkukushkin/attributes-doc)

<details><summary>README extract</summary>

Hacky implementation of PEP 224.

Example:
```python
from attributes_doc import attributes_doc

@attributes_doc
class Foo:
    bar = 1
    """This is the docstring for the bar attribute.

    It will be stored in `Foo.doc_bar` and will be accessible at runtime.
    """

    baz = 2
    """This is the docstring for the baz attribute."""

print(Foo.doc_bar)
print(getattr(Foo, "doc_baz"))
```

Sections: attributes-doc, Usage, Decorator `attributes_doc`, Function `get_attributes_doc`, Decorator `enum_doc`, Function `get_doc`

</details>

### pyminizip

A minizip wrapper - To create a password encrypted zip file in python.

`pip install pyminizip` · installs from source (sdist only) · licence: zlib/libpng License · rank 6045 · last release 2021-12-21 · [PyPI](https://pypi.org/project/pyminizip/)

<details><summary>README extract</summary>

To create a password encrypted zip file in python.
And the zip file is able to extract in WINDOWS.

This is a simple Minizip wrapper of python.

This software uses zlib.
License: zlib/libpng License.

Example:
```python
pyminizip.compress("/srcfile/path.txt", "file_path_prefix", "/distfile/path.zip", "password", int(compress_level))
```

Sections: pyminizip, How to use

</details>

### Autologging

Autologging makes logging and tracing Python classes easy.

`pip install Autologging` · installs (wheel) · licence: MIT License · rank 6047 · last release 2019-04-20 · [PyPI](https://pypi.org/project/Autologging/)

<details><summary>README extract</summary>

Autologging eliminates boilerplate logging setup code and tracing code,
and provides a means to separate application logging from program flow
and data tracing.

Python modules that make use of Autologging are cleaner, leaner, and
more resilient to changes that would otherwise require updating tracing
statements. ...

Example:
```python
 1 import logging
 2 import sys
 3
 4 from autologging import logged, TRACE, traced
 5
 6 @traced
 7 @logged
 8 class Example:
 9
10     def init(self):
11         self.__log.info("initialized")
12
13     def backwards(self, *words):
14         for word in words:
15             yield "".join(reversed(word))
16
17
18 if name == "main":
...
```

...

</details>

### Adyen

Adyen Python Api

`pip install Adyen` · installs (wheel) · licence: MIT License · rank 6057 · last release 2026-09-17 · [PyPI](https://pypi.org/project/Adyen/)

<details><summary>README extract</summary>

This is the officially supported Python library for using Adyen's APIs.

Sections: Adyen APIs Library for Python, Prerequisites, For usage purpose, Using the library, Using all services, Create the all-in-one client, Configure the client, Prepare the request, Make the API call through the long-form path, Using Individual Service Clients, Import the core client and the service-level API class, Create and configure the core AdyenClient, Instantiate the AdyenCheckoutApi service, Make API calls using the sub-clients within the service

</details>

### splitio-client

Split.io Python Client

`pip install splitio-client` · installs from source (sdist only) · licence: Apache License 2.0 · rank 6068 · last release 2026-11-06 · [PyPI](https://pypi.org/project/splitio-client/)

<details><summary>README extract</summary>

Features:
This SDK is designed to work with Split, the platform for controlled rollouts, which serves features to your users via a Split feature flag to manage your complete customer experience.

Example:
```python
from splitio import get_factory
from splitio.exceptions import TimeoutException
factory = get_factory('YOUR_SDK_TYPE_API_KEY', config=config)
try:
    factory.block_until_ready(5) # wait up to 5 seconds
    split = factory.client()
    treatment = split.get_treatment('CUSTOMER_ID', 'FEATURE_FLAG_NAME')
    if treatment == "on":
...
```

Sections: Split Python SDK, Overview, Compatibility, Getting started, Submitting issues, About Split

</details>

### sendsafely

The SendSafely Client API allows programmatic access to SendSafely and provides a layer of abstraction from our REST API, which requires developers to perform several complex tasks in a correct manner.

`pip install sendsafely` · installs from source (sdist only) · licence: Apache Software License · rank 6083 · last release 2026-07-23 · [PyPI](https://pypi.org/project/sendsafely/)

<details><summary>README extract</summary>

The SendSafely Python API lets you integrate SendSafely secure data transfer capabilities directly into your Python application.

Example:
```python
from sendsafely import SendSafely, Package
```

Sections: SendSafely Python API, Quickstart, Examples

</details>

### common

Common tools and data structures implemented in pure python.

`pip install common` · installs from source (sdist only) · licence: MIT License · rank 6095 · last release 2016-05-19 · [PyPI](https://pypi.org/project/common/)

### clipboard

A cross-platform clipboard library for text, images, HTML dual offers, and file-list reads.

`pip install clipboard` · installs (wheel) · licence: MIT · rank 6096 · last release 2026-11-06 · [PyPI](https://pypi.org/project/clipboard/)

<details><summary>README extract</summary>

A cross platform clipboard library for Python (Windows, macOS, Linux). Text
`copy` / `paste` follow this package's own contract: it owns the macOS
and Linux helper paths, uses pyperclip's Windows backend, and delegates other
environments to pyperclip; richer APIs sit beside them. ...

</details>

### jsonschema-spec

JSONSchema Spec with object-oriented paths

`pip install jsonschema-spec` · installs (wheel) · licence: Apache Software License · rank 6113 · last release 2023-08-16 · [PyPI](https://pypi.org/project/jsonschema-spec/) · [source](https://github.com/p1c2u/jsonschema-spec)

<details><summary>README extract</summary>

Object-oriented JSONSchema

Features:
* Traverse schema like paths
* Access schema on demand with separate dereferencing accessor layer

Example:
```python
>>> from jsonschema_spec import SchemaPath

>>> d = {
...     "properties": {
...        "info": {
...            "$ref": "#/$defs/Info",
...        },
...     },
...     "$defs": {
...         "Info": {
...             "properties": {
...                 "title": {
...                     "$ref": "
...                 },
...
```

Sections: JSONSchema Spec, About, Key features, Usage, Related projects

</details>

### install-playwright

Execute `playwright install` from Python

`pip install install-playwright` · installs (wheel) · licence: MIT · rank 6117 · last release 2026-11-02 · [PyPI](https://pypi.org/project/install-playwright/) · [docs](https://egpl.dev/install-playwright-python/) · [source](https://github.com/eggplants/install-playwright-python)

<details><summary>README extract</summary>

Example:
```python
from install_playwright import install
```

</details>

### acachecontrol

Cache-Control for aiohttp

`pip install acachecontrol` · installs (wheel) · licence: Apache Software License · rank 6118 · last release 2026-01-26 · [PyPI](https://pypi.org/project/acachecontrol/)

<details><summary>README extract</summary>

> Requires Python3.6+

Example:
```python
import asyncio
from acachecontrol import AsyncCache, AsyncCacheControl

async def main():
    cache = AsyncCache(config={"sleep_time": 0.2})
    # `AsyncCache()` with default configuration is used
    # if `cache` not provided
    async with AsyncCacheControl(cache=cache) as cached_sess:
        async with cached_sess.get(' as resp:
...
```

Sections: Async CacheControl for aiohttp, What and why, Usage, Extending or creating new classes

</details>

### gdtoolkit

Independent set of tools for working with GDScript - parser, linter and formatter

`pip install gdtoolkit` · installs (wheel) · licence: MIT License · rank 6119 · last release 2025-10-09 · [PyPI](https://pypi.org/project/gdtoolkit/)

<details><summary>README extract</summary>

This project provides a set of tools for daily work with `GDScript`. At the moment it provides:

- A parser that produces a parse tree for debugging and educational purposes.
- A linter that performs a static analysis according to some predefined configuration.
- A formatter that formats the code according to some predefined rules. ...

Example:
```python
class X:
    var x=[1,2,{'a':1}]
    var y=[1,2,3,]     # trailing comma
    func foo(a:int,b,c=[1,2,3]):
        if a in c and \
           b > 100:
            print('foo')
func bar():
    print('bar')
```

...

</details>

### simile

Package for interfacing with Simile AI agents for simulation

`pip install simile` · installs (wheel) · licence: MIT · rank 6133 · last release 2026-01-22 · [PyPI](https://pypi.org/project/simile/)

<details><summary>README extract</summary>

A Python client for interacting with the Simile API server.

Example:
```python
from simile import Simile

client = Simile(api_key="your_api_key")
```

Sections: Simile API Python Client, Dependencies, Usage, Publishing

</details>

### pyobjc-framework-CoreML

Wrappers for the framework CoreML on macOS

`pip install pyobjc-framework-CoreML` · installs from source (sdist only) · licence: MIT · rank 6138 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreML/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreML" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-Vision

Wrappers for the framework Vision on macOS

`pip install pyobjc-framework-Vision` · installs from source (sdist only) · licence: MIT · rank 6144 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Vision/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Vision" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pydantic-ai-backend

File storage and sandbox backends for AI agents

`pip install pydantic-ai-backend` · installs (wheel) · licence: MIT · rank 6149 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pydantic-ai-backend/) · [docs](https://vstorm-co.github.io/pydantic-ai-backend/) · [source](https://github.com/vstorm-co/pydantic-ai-backend)

<details><summary>README extract</summary>

From the team behind this repo: AgenticOS, the Sovereign Agentic AI Layer. AI agents your whole team can use and improve: open source (Apache-2.0), self-hosted, built on Pydantic AI.

 Workspaces & console tools for Pydantic AI agents.

 Docker / sandboxd / Kubernetes / Daytona / State workspaces and a console toolset that works in any of them, ...

Features:
| Feature | Description |

| Native Pydantic AI workspaces | Docker, sandboxd, Kubernetes, Daytona and state documents behind `ctx.workspace` |
| Console Toolset | Ready-to-use tools that work in any workspace, including the harness's |
| Permission ...

Example:
```python
from pydantic_ai import Agent

from pydantic_ai_backends import ConsoleCapability, DockerWorkspace

agent = Agent(
    "anthropic:claude-opus-5-5",
...

</details>

### django-add-default-value

This django Migration Operation can be used to transfer a fields default value to the database scheme.

`pip install django-add-default-value` · installs (wheel) · licence: Apache Software License · rank 6151 · last release 2022-02-02 · [PyPI](https://pypi.org/project/django-add-default-value/)

<details><summary>README extract</summary>

Django Migration Operation that can be used to transfer a field's default value
to the database scheme.

Supported Databases

* MySQL (or compatible)
* PostgreSQL
* MSSQL (currently not tested)
* CockroachDB

Installation

`pip install django-add-default-value` ...

Example:
```python
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ...
    ]

    operations = [
         migrations.AddField(
             field=models.CharField(default='my_default', max_length=255),
             model_name='my_model',
             name='my_field',
         ),
     ]
```

Sections: Django Add Default Value, Example

</details>

### llm-sandbox

LLM Sandbox is a lightweight and portable sandbox environment designed to run large language model (LLM) generated code in a safe and isolated mode.

`pip install llm-sandbox` · installs (wheel) · licence: not stated · rank 6153 · last release 2026-10-16 · [PyPI](https://pypi.org/project/llm-sandbox/) · [docs](https://vndee.github.io/llm-sandbox/) · [source](https://github.com/vndee/llm-sandbox)

<details><summary>README extract</summary>

*Securely Execute LLM-Generated Code with Ease*

LLM Sandbox runs Large Language Model (LLM) generated code through a common API for container and local Linux and Windows sandbox backends. Choose an isolation backend for your deployment, configure its security controls, and reuse the same code execution and file APIs.

Documentation: ...

Features:
- Secure Code Execution: Execute code in isolated containers with your preferred backend
- Multi-Language Support: Run Python, JavaScript, Java, C++, Go, R, and Ruby code ...

Example:
```python
from llm_sandbox import SandboxSession

# Create and use a sandbox session
with SandboxSession(lang="python") as session:
    result = session.run("""
print("Hello from LLM Sandbox!")
print("I'm running in a secure container.")
    """)
...

</details>

### sphinx-markdown-builder

A Sphinx extension to add markdown generation support.

`pip install sphinx-markdown-builder` · installs (wheel) · licence: MIT · rank 6178 · last release 2026-08-16 · [PyPI](https://pypi.org/project/sphinx-markdown-builder/)

<details><summary>README extract</summary>

A Sphinx extension to add markdown generation support.

Sections: sphinx-markdown-builder, Usage, Configurations

</details>

### django-admin-logs

View, delete or disable Django admin log entries.

`pip install django-admin-logs` · installs (wheel) · licence: MIT License · rank 6188 · last release 2025-12-03 · [PyPI](https://pypi.org/project/django-admin-logs/)

<details><summary>README extract</summary>

Log entries are automatically created by the Django framework whenever a user
adds, changes or deletes objects through the admin interface.

Django Admin Logs is a package that allows you to either view the admin
log entries from within the admin interface, or to disable them entirely.

* Python 3.8+
* Django 4.2+

Sections: Django Admin Logs, Requirements, Configuration

</details>

### convertapi

ConvertAPI Python Client

`pip install convertapi` · installs (wheel) · licence: MIT · rank 6189 · last release 2026-10-20 · [PyPI](https://pypi.org/project/convertapi/) · [docs](https://www.convertapi.com/doc) · [source](https://github.com/ConvertAPI/convertapi-library-python)

<details><summary>README extract</summary>

ConvertAPI helps to convert various file formats. Creating PDF and Images from various sources like Word, Excel, Powerpoint, images, web pages or raw HTML codes. Merge, Encrypt, Split, Repair and Decrypt PDF files and many other manipulations. You can integrate it into your application in just a few minutes and use it easily.

Example:
```python
import convertapi

convertapi.api_credentials = 'api-token'
```

Sections: ConvertAPI Python Client, Convert your files with our online file conversion API, Requirements, Usage, Configuration, Proxy configuration, File conversion, Convert file url, Specifying from format, Additional conversion parameters, User information, Alternative domain, More examples

</details>

### ofxparse

Tools for working with the OFX (Open Financial Exchange) file format

`pip install ofxparse` · installs from source (sdist only) · licence: MIT License · rank 6192 · last release 2021-05-31 · [PyPI](https://pypi.org/project/ofxparse/)

<details><summary>README extract</summary>

ofxparse is a parser for Open Financial Exchange (.ofx) format files. OFX
files are available from almost any online banking site, so they work well
if you want to pull together your finances from multiple sources. Online
trading accounts also provide account statements in OFX files. ...

Example:
```python
from ofxparse import OfxParser
with codecs.open('file.ofx') as fileobj:
    ofx = OfxParser.parse(fileobj)

# The OFX object

ofx.account               # An Account object

# AccountType
# (Unknown, Bank, CreditCard, Investment)

# Account

account = ofx.account
account.account_id        # The account number
...
```

Sections: ofxparse, Example Usage, Help!, Homepage

</details>

### pytailwindcss

Standalone Tailwind CSS CLI, installable via pip. Use Tailwind CSS without Node.js.

`pip install pytailwindcss` · installs (wheel) · licence: MIT · rank 6200 · last release 2026-10-13 · [PyPI](https://pypi.org/project/pytailwindcss/) · [source](https://github.com/timonweb/pytailwindcss)

<details><summary>README extract</summary>

Features:
*Tailwind CSS* is notoriously dependent on *Node.js*. If you're a *Python* developer, this dependency may not be welcome
in your team, your Docker container, or your inner circle. ...

Example:
```python
import pytailwindcss

# Download the binary (optional, see auto_install below).
pytailwindcss.install(version="v4.3.3")

# Run the CLI and get its output as a string.
pytailwindcss.run("-i input.css -o output.css --minify", version="v4.3.3")

# Arguments can be a list too; auto_install downloads the binary if it's missing.
...
```

Sections: Why, Get started, Pinning a Tailwind CSS version, Where the binary lives, Docker, Using it from Python, Caveats, Bugs and Suggestions

</details>

### pyobjc-framework-WebKit

Wrappers for the framework WebKit on macOS

`pip install pyobjc-framework-WebKit` · installs from source (sdist only) · licence: MIT · rank 6201 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-WebKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "WebKit" and "JavaScriptCore" frameworks on macOS. The
WebKit framework contains the views and support classes for creating a
browser. The JavaScriptCore framework implements a JavaScript interpreter. ...

</details>

### rudder-sdk-python

RudderStack is an open-source Segment alternative written in Go, built for the enterprise.

`pip install rudder-sdk-python` · installs (wheel) · licence: MIT License · rank 6222 · last release 2026-11-05 · [PyPI](https://pypi.org/project/rudder-sdk-python/)

<details><summary>README extract</summary>

RudderStack’s Python SDK lets you track events from your Python application. Once enabled, the event requests hit the RudderStack servers. RudderStack then transforms and routes these events to your specified destination platforms.

More details on the Python SDK can be found in our documentation

Example:
```python
import rudderstack.analytics as analytics

analytics.write_key =
analytics.on_error =
analytics.debug =
analytics.dataPlaneUrl =

analytics.gzip =
```

Sections: RudderStack Python SDK, Getting Started with Python SDK, Initializing the RudderStack Client, Sending Events, Editing or dropping events before enqueue, Proxy configuration, About RudderStack, Contact Us

</details>

### cwcwidth

Python bindings for wc(s)width

`pip install cwcwidth` · installs (wheel) · licence: MIT · rank 6227 · last release 2025-11-01 · [PyPI](https://pypi.org/project/cwcwidth/)

<details><summary>README extract</summary>

`cwcwidth` provides Python bindings for `wcwidth` and `wcswidth` functions defined in POSIX.1-2001
and POSIX.1-2008 based on Cython. These functions compute the printable
length of a unicode character/string on a terminal. The module provides the same functions as
wcwidth and its behavior is compatible. ...

Example:
```python
>>> import cwcwidth
>>> cwcwidth.wcwidth("a")
1
>>> cwcwidth.wcswidth("コ")
2
>>> cwcwidth.wcswidth("コンニチハ, セカイ!")
19
>>> cwcwidth.wcswidth("コンニチハ, セカイ!", 5)
10
```

Sections: Python bindings for wc(s)width, Dependencies, Usage, Comparison with `wcwidth`

</details>

### lagom

Lagom is a dependency injection container designed to give you 'just enough' help with building your dependencies.

`pip install lagom` · installs (wheel) · licence: MIT License · rank 6232 · last release 2025-07-16 · [PyPI](https://pypi.org/project/lagom/) · [docs](https://lagom-di.readthedocs.io/) · [source](https://github.com/meadsteve/lagom)

<details><summary>README extract</summary>

Lagom is a dependency injection container designed to give you "just enough"
help with building your dependencies. The intention is that almost
all of your code doesn't know about or rely on lagom. Lagom will
only be involved at the top level to pull everything together.

Features:
* Type based auto wiring with zero configuration.
 * Fully based on types. Strong integration with mypy.
 * Minimal changes to existing code.
 * Integration with a few common web frameworks.
 * Support for async python.
 * Thread-safe at runtime ...

Example:
```python
container = Container()
some_thing = container[SomeClass]
```

Sections: What, Features, Usage, Auto-wiring (with zero configuration), Singletons, Explicit build instructions when required, Hooks in to existing systems

</details>

### python-string-utils

Utility functions for strings validation and manipulation.

`pip install python-string-utils` · installs (wheel) · licence: MIT License · rank 6234 · last release 2020-03-04 · [PyPI](https://pypi.org/project/python-string-utils/)

<details><summary>README extract</summary>

A handy library to validate, manipulate and generate strings, which is:

- Simple and "pythonic"
- Fully documented and with examples! (html version on readthedocs.io)
- 100% code coverage! (see it with your own eyes on codecov.io)
- Tested (automatically on each push thanks to Travis CI) against all officially supported Python versions ...

Sections: Python String Utils, Latest version: 1.0.0 (March 2020), What's inside..., Library structure, Api overview, String validation functions, String manipulation, returns, String generations, possible ouput: 'd1eedff4033a2e9867c37ded', Documentation

</details>

### umf

Unified Memory Framework

`pip install umf` · installs (wheel) · licence: Other/Proprietary License · rank 6236 · last release 2026-10-16 · [PyPI](https://pypi.org/project/umf/)

<details><summary>README extract</summary>

Construct allocators and memory pools. Manage multiple memory pools characterized by different attributes, allowing certain allocation types to be isolated from others and allocated using different hardware resources as required.

</details>

### webflow

(no summary)

`pip install webflow` · installs (wheel) · licence: MIT License · rank 6237 · last release 2026-03-12 · [PyPI](https://pypi.org/project/webflow/) · [source](https://github.com/webflow/webflow-python)

<details><summary>README extract</summary>

The Webflow Python Library provides convenient access to the Webflow Data API from
applications written in Python.

The library includes type definitions for all
request and response fields, and offers both synchronous and asynchronous clients powered by httpx.

Explore the API reference documentation here.

Example:
```python
from webflow.client import Webflow

client = Webflow(
  access_token="YOUR_ACCESS_TOKEN"
)
site = client.sites.get("site-id")
```

Sections: Webflow Python Library, Documentation, Usage, Async Client, OAuth, Step 2: Retrieve your acccess token, Step 3: Instantiate the client, Webflow Module, Exception Handling, Advanced, Timeouts, Custom HTTP client

</details>

### pyobjc-framework-Security

Wrappers for the framework Security on macOS

`pip install pyobjc-framework-Security` · installs from source (sdist only) · licence: MIT · rank 6257 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Security/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Security" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### django-bootstrap5

Bootstrap 5 for Django

`pip install django-bootstrap5` · installs (wheel) · licence: BSD-3-Clause · rank 6259 · last release 2026-10-11 · [PyPI](https://pypi.org/project/django-bootstrap5/) · [docs](https://django-bootstrap5.readthedocs.io/) · [source](https://github.com/zostera/django-bootstrap5)

<details><summary>README extract</summary>

Bootstrap 5 for Django.

The goal of this project is to seamlessly blend Django and Bootstrap 5.

Sections: django-bootstrap5, Goal, Requirements, Documentation, Example template, Example app, Bugs and suggestions

</details>

### siphash24

Streaming-capable SipHash-1-3 and SipHash-2-4 Implementation

`pip install siphash24` · installs (wheel) · licence: Apache-2.0 OR LGPL-2.1-or-later · rank 6273 · last release 2026-09-08 · [PyPI](https://pypi.org/project/siphash24/) · [docs](https://dnicolodi.github.io/python-siphash24/) · [source](https://github.com/dnicolodi/python-siphash24/)

_README extract left out: share-alike licence._

### Inflector

Inflector for Python

`pip install Inflector` · installs (wheel) · licence: Python Software Foundation License · rank 6274 · last release 2024-01-12 · [PyPI](https://pypi.org/project/Inflector/)

<details><summary>README extract</summary>

The Inflector is used for getting the plural and singular form of nouns. This piece of code helps on creating code that favors convention over configuration.

Only English and Spanish nouns are supported. ...

Sections: Inflector for Python, pluralize(word), singularize(word), conditionalPlural(numer_of_records, word), titleize(word, uppercase = ''), camelize(word), underscore(word), humanize(word, uppercase = ''), variablize(word), tableize(class_name), classify(table_name), ordinalize(number), unaccent(text), urlize(text)

</details>

### pyiso8583

A serializer and deserializer of ISO8583 data.

`pip install pyiso8583` · installs (wheel) · licence: MIT License · rank 6294 · last release 2025-08-28 · [PyPI](https://pypi.org/project/pyiso8583/)

<details><summary>README extract</summary>

`iso8583` package serializes and deserializes ISO8583 data between
raw `bytes` ISO8583 data and a regular Python `dict`.

`iso8583` package supports custom specifications
that can define:

- Field length and data encoding, such as BCD, ASCII, EBCDIC, etc.
- Field length count measured in bytes or nibbles. ...

Example:
```python
>>> import pprint
>>> import iso8583
>>> from iso8583.specs import default_ascii as spec
>>> encoded_raw = b'02004000000000000000101234567890'
>>> decoded, encoded = iso8583.decode(encoded_raw, spec)
>>> pprint.pp(decoded)
{'t': '0200', 'p': '4000000000000000', '2': '1234567890'}
>>> pprint.pp(encoded)
{'t': {'len': b'', 'data': b'0200'},
...
```

Sections: iso8583 - a Python package for parsing ISO8583 data, Encoding & Decoding, Pretty Print Messages

</details>

### lexid

Variable width build numbers with lexical ordering.

`pip install lexid` · installs (wheel) · licence: MIT License · rank 6297 · last release 2021-04-02 · [PyPI](https://pypi.org/project/lexid/)

<details><summary>README extract</summary>

`lexid` is a micro library to increment lexically ordered numerical ids.

Throughout the sequence of ids, this expression will always be true, whether you are dealing with integers or strings:

 older_id < newer_id ...

Example:
```python
>>> import lexid
>>> lexid.incr("1")
'22'
>>> lexid.incr("0001")
'0002'
>>> lexid.incr("0999")
'11000'
```

Sections: lexid, Usage, Lexical Ids, 2021.1006, 2020.1005

</details>

### bumpver

Bump version numbers in project files.

`pip install bumpver` · installs (wheel) · licence: MIT License · rank 6299 · last release 2026-05-22 · [PyPI](https://pypi.org/project/bumpver/)

<details><summary>README extract</summary>

With the CLI command `bumpver`, you can search for and update version strings in your project files. It has a flexible pattern syntax to support many version schemes (SemVer, CalVer or otherwise). BumpVer features:

- Configurable version patterns
- Optional Git or Mercurial integration
- Works with plaintext, so you can use it with any project. ...

Example:
```python
$ bumpver --help
Usage: bumpver [OPTIONS] COMMAND [ARGS]...

  Automatically update version strings in plaintext files.

Options:
  --version      Show the version and exit.
  -v, --verbose  Control log level. -vv for debug level.
  -h, --help     Show this message and exit.

Commands:
  grep    Search file(s) for a version pattern.
...
```

...

</details>

### quickjs-ng

Thin Python wrapper of quickjs-ng

`pip install quickjs-ng` · installs (wheel) · licence: not stated · rank 6313 · last release 2026-11-05 · [PyPI](https://pypi.org/project/quickjs-ng/) · [source](https://github.com/genotrance/quickjs-ng)

<details><summary>README extract</summary>

Python wrapper around quickjs-ng, the actively maintained fork of the QuickJS JavaScript engine.

Drop-in replacement for the archived quickjs package — `import quickjs` works unchanged.

Example:
```python
import quickjs

# Evaluate expressions
ctx = quickjs.Context()
ctx.eval("1 + 2")  # => 3

# Call JS functions from Python
ctx.eval("function add(a, b) { return a + b; }")
add = ctx.get("add")
add(3, 4)  # => 7

# Call Python functions from JS
ctx.add_callable("py_add", lambda a, b: a + b)
ctx.eval("py_add(3, 4)")  # => 7

...
```

Sections: quickjs-ng, Usage, Threading, Versioning, Documentation, Fork safety

</details>

### pybind11-global

Seamless operability between C++11 and Python

`pip install pybind11-global` · installs (wheel) · licence: BSD-3-Clause · rank 6348 · last release 2026-08-06 · [PyPI](https://pypi.org/project/pybind11-global/) · [docs](https://pybind11.readthedocs.io/)

<details><summary>README extract</summary>

pybind11 (v3) — Seamless interoperability between C++ and Python

 |SPEC 4 — Using and Creating Nightly Wheels|

Setuptools example
• Scikit-build example
• CMake example

pybind11 is a lightweight header-only library that exposes C++ types
in Python and vice versa, mainly to create Python bindings of existing
C++ code. ...

Sections: Core features, Goodies, About

</details>

### python-binance

Binance REST API python implementation

`pip install python-binance` · installs (wheel) · licence: MIT License · rank 6366 · last release 2026-06-08 · [PyPI](https://pypi.org/project/python-binance/)

<details><summary>README extract</summary>

This is an unofficial Python wrapper for the Binance exchange REST API v3.

If you came here looking for the Binance exchange to purchase cryptocurrencies, then go here.
If you want to automate interactions with Binance stick around.

This project is powered by ...

Features:
- Implementation of all General, Market Data and Account endpoints.
- Asyncio implementation
- Demo trading support (by providing demo=True)
- Testnet support for Spot, Futures and Vanilla Options (deprecated) ...

Example:
```python
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
client = Client(api_key, api_secret)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')

# place a test market buy order, to place an actual order use the create_order function
...

</details>

### dict2css

A μ-library for constructing cascading style sheets from Python dictionaries.

`pip install dict2css` · installs (wheel) · licence: MIT License · rank 6388 · last release 2026-05-21 · [PyPI](https://pypi.org/project/dict2css/) · [docs](https://dict2css.readthedocs.io/en/latest) · [source](https://github.com/sphinx-toolbox/dict2css)

<details><summary>README extract</summary>

A μ-library for constructing cascading style sheets from Python dictionaries.

`dict2css` provides an API similar to the json and
toml modules, with `dump` and `load` functions.
The `dump` function takes a mapping of CSS selectors
to mappings of CSS properties. ...

</details>

### torch-complex

A fugacious python class for PyTorch-ComplexTensor

`pip install torch-complex` · installs (wheel) · licence: Apache Software License · rank 6393 · last release 2024-06-28 · [PyPI](https://pypi.org/project/torch-complex/)

<details><summary>README extract</summary>

A temporal python class for PyTorch-ComplexTensor

A Python class to perform as `ComplexTensor` in PyTorch: Nothing except for the following,

Features:
PyTorch is great DNN Python library, except that it doesn't support `ComplexTensor` in Python level.

I'm looking forward to the completion, but I need `ComplexTensor` for now.
 I created this cheap module for the temporal replacement of it. ...

Example:
```python
class ComplexTensor:
    def init(self, ...):
        self.real = torch.Tensor(...)
        self.imag = torch.Tensor(...)
```

Sections: pytorch_complex, What is this?, Why?, Requirements, How to use, Basic mathematical operation, Functional, For DNN

</details>

### xpress9

Python bindings for the Xpress9 compression library

`pip install xpress9` · installs (wheel) · licence: MIT License · rank 6406 · last release 2026-09-14 · [PyPI](https://pypi.org/project/xpress9/) · [source](https://github.com/Hugoberry/xpress9-python)

<details><summary>README extract</summary>

Xpress9-python is a lightweight wrapper for the Xpress9 compression library by Microsoft. This project provides a C extension along with a Cython wrapper, enabling efficient compression and decompression in Python.

Features:
- Compression: Compress data using the Xpress9 encoder.
- Decompression: Decompress data using the Xpress9 decoder.
- High Performance: Optimized with compiler flags and optional OpenMP for multi-threading. ...

Example:
```python
from xpress9 import Xpress9

# Initialize the wrapper
x = Xpress9()
print("Xpress9 initialized successfully!")

# Create some sample, compressible data (e.g., repetitive string)
original_data = b"Hello, world! " * 64
print(f"Original data size: {len(original_data)} bytes")

# Specify the maximum compressed size (adjust as needed)
...
```

...

</details>

### dlipower

Control digital loggers web power switch

`pip install dlipower` · installs from source (sdist only) · licence: BSD License · rank 6419 · last release 2018-06-16 · [PyPI](https://pypi.org/project/dlipower/)

<details><summary>README extract</summary>

This is a python module and a script to mange the
Digital Loggers Web Power switch.

The module provides a python class named
PowerSwitch that allows managing the web power
switch from python programs.

When run as a script this acts as a command
line utility to manage the DLI Power switch.

Example:
```python
import dlipower

print('Connecting to a DLI PowerSwitch at lpc.digital-loggers.com')
switch = dlipower.PowerSwitch(hostname="lpc.digital-loggers.com", userid="admin")

print('Turning off the first outlet')
switch.off(1)

print('The powerstate of the first outlet is currently', switch[0].state)

print('Renaming the first outlet as "Traffic light"')
...
```

Sections: Digital Loggers Network Power Switch Python Module, DESCRIPTION, Example

</details>

### indexed-zstd

Fast random access to zstd files

`pip install indexed-zstd` · installs (wheel) · licence: MIT License · rank 6426 · last release 2026-10-12 · [PyPI](https://pypi.org/project/indexed-zstd/)

<details><summary>README extract</summary>

A Python module for fast random access to zstd-compressed files without full decompression.

`IndexedZstdFile` implements Python's `io.BufferedReader` interface, so it works as a drop-in replacement for `open()` on `.zst` files — supporting `seek()`, `read()`, `readline()`, `tell()`, and context managers. ...

Example:
```python
from indexed_zstd import IndexedZstdFile

with IndexedZstdFile("example.zst") as f:
    f.seek(1024)
    data = f.read(256)
    print(f.tell())       # 1280
    print(f.seekable())   # True
```

Sections: indexed_zstd, How it works, pip (recommended), conda, Arch Linux, Usage, Basic random access, Reading line by line, Opening by file descriptor, Inspecting frame structure, API reference, Building from source, Linux, macOS

</details>

### mygeotab

A Python client for the MyGeotab SDK

`pip install mygeotab` · installs (wheel) · licence: Apache Software License · rank 6434 · last release 2026-07-16 · [PyPI](https://pypi.org/project/mygeotab/)

<details><summary>README extract</summary>

A Python client for the MyGeotab SDK.

Features:
- Automatic serialization and deserialization of API call results
- Clean, Pythonic API for querying, adding, updating, and removing entities
- Both synchronous and `async`/`await` interfaces
- Cross-platform and compatible with Python 3.10+ ...

Example:
```python
import mygeotab

client = mygeotab.API(
    username='hello@example.com',
    password='mypass',
    database='MyDatabase',
)
client.authenticate()

devices = client.get('Device', name='%Test Dev%')
print(devices)

# [{'name': 'Test Device',
# 'maxSecondsBetweenLogs': 200.0,
# 'activeTo': '2050-01-01',
# ...}]
```

...

</details>

### kiwipiepy

Kiwi, the Korean Tokenizer for Python

`pip install kiwipiepy` · installs (wheel) · licence: Apache-2.0 · rank 6440 · last release 2026-10-20 · [PyPI](https://pypi.org/project/kiwipiepy/)

<details><summary>README extract</summary>

kiwipiepy is a python version package of Kiwi(Korean Intelligent Word Identifier) which is a morphological analyzer for Korean.

</details>

### pydeps

Display module dependencies

`pip install pydeps` · installs (wheel) · licence: BSD-2-Clause · rank 6445 · last release 2026-10-01 · [PyPI](https://pypi.org/project/pydeps/)

<details><summary>README extract</summary>

Python module dependency visualization.

This package is primarily intended to be used from the command line through the
`pydeps` command.

Feature requests and bug reports:

Please report bugs and feature requests on GitHub at

Example:
```python
usage: pydeps [-h] [--debug] [--config FILE] [--no-config] [--version] [-L LOG]
              [--find-package] [-v] [-o file] [-T FORMAT] [--display PROGRAM]
              [--noshow] [--show-deps] [--show-raw-deps] [--deps-output DEPS_OUT]
              [--show-dot] [--dot-output DOT_OUT] [--nodot] [--no-output]
...
```

Sections: pydeps, Usage, What to point pydeps at, Example, Notes, Configuration files, Bacon (Scoring), Import cycles, Clustering, Maximum module depth, Graph direction, Collapsing target package, Intermediate format, . Fork it

</details>

### PyDriller

Framework for MSR

`pip install PyDriller` · installs (wheel) · licence: Apache Software License · rank 6447 · last release 2026-09-11 · [PyPI](https://pypi.org/project/PyDriller/)

<details><summary>README extract</summary>

PyDriller is a Python framework that helps developers on mining software repositories. With PyDriller you can easily extract information from any Git repository, such as commits, developers, modifications, diffs, and source codes, and quickly export CSV files.

</details>

### base32-crockford

A Python implementation of Douglas Crockford's base32 encoding scheme

`pip install base32-crockford` · installs (wheel) · licence: BSD License · rank 6488 · last release 2015-03-19 · [PyPI](https://pypi.org/project/base32-crockford/)

<details><summary>README extract</summary>

A Python module implementing the alternate base32 encoding as described
by Douglas Crockford at:

He designed the encoding to:

 * Be human and machine readable
 * Be compact
 * Be error resistant
 * Be pronounceable

It uses a symbol set of 10 digits and 22 letters, excluding I, L O and
U. ...

</details>

### pyobjc-framework-UniformTypeIdentifiers

Wrappers for the framework UniformTypeIdentifiers on macOS

`pip install pyobjc-framework-UniformTypeIdentifiers` · installs (wheel) · licence: MIT · rank 6493 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-UniformTypeIdentifiers/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "UniformTypeIdentifiers" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### honcho-ai

Official DX Optimized Python SDK for Honcho

`pip install honcho-ai` · installs (wheel) · licence: Apache-2.0 · rank 6496 · last release 2026-10-30 · [PyPI](https://pypi.org/project/honcho-ai/) · [source](https://github.com/plastic-labs/honcho)

<details><summary>README extract</summary>

The official Python library for the Honcho conversational memory platform. Honcho provides tools for managing peers, sessions, and conversation context across multi-party interactions, enabling advanced conversational AI applications with persistent memory and theory-of-mind capabilities.

Example:
```python
from honcho import Honcho

# Initialize client
client = Honcho(api_key="your-api-key")

# Create peers (participants in conversations)
alice = client.peer("alice")
bob = client.peer("bob")

# Create a session for group conversations
session = client.session("conversation-1")

# Add messages to the session
session.add_messages([
...
```

...

</details>

### msgfy

msgfy is a Python library for convert Exception instance to a human-readable error message.

`pip install msgfy` · installs (wheel) · licence: MIT License · rank 6517 · last release 2023-09-17 · [PyPI](https://pypi.org/project/msgfy/) · [source](https://github.com/thombashi/msgfy)

<details><summary>README extract</summary>

msgfy is a Python library for convert Exception instance to a human-readable error message.

Sections: Summary, Usage, Convert from Exception instance to an error message, Specify message format, Convert from Exception instance to a debug message, Available keywords for message formats, Dependencies, Test dependencies

</details>

### nimble_python

The official Python library for the nimble API

`pip install nimble_python` · installs (wheel) · licence: Apache Software License · rank 6525 · last release 2026-09-07 · [PyPI](https://pypi.org/project/nimble_python/) · [source](https://github.com/Nimbleway/nimble-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Nimble Python library provides convenient access to the Nimble REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from nimble_python import Nimble

client = Nimble(
    api_key=os.environ.get("NIMBLE_API_KEY"),  # This is the default and can be omitted
)

response = client.extract.run(
    url="
)
print(response.task_id)
```

...

</details>

### chacha20poly1305-reuseable

ChaCha20Poly1305 that is reuseable for asyncio

`pip install chacha20poly1305-reuseable` · installs (wheel) · licence: Other/Proprietary License · rank 6526 · last release 2024-07-21 · [PyPI](https://pypi.org/project/chacha20poly1305-reuseable/) · [source](https://github.com/bdraco/chacha20poly1305-reuseable)

<details><summary>README extract</summary>

ChaCha20Poly1305 that is reuseable for asyncio

</details>

### drain3

Persistent & streaming log template miner

`pip install drain3` · installs from source (sdist only) · licence: MIT License · rank 6534 · last release 2022-07-17 · [PyPI](https://pypi.org/project/drain3/)

<details><summary>README extract</summary>

Drain3 is an online log template miner that can extract templates (clusters) from a stream of log messages in a timely
manner. It employs a parse tree with fixed depth to guide the log group search process, which effectively avoids
constructing a very deep and unbalanced tree. ...

Example:
```python
Starting Drain3 template miner
Checking for saved state
Saved state not found
Drain3 started with 'FILE' persistence
Starting training mode. Reading from std-in ('q' to finish)
> connected to 10.0.0.1
Saving state of 1 clusters with 1 messages, 528 bytes, reason: cluster_created (1)
...
```

...

</details>

### flake8-black

flake8 plugin to call black as a code style validator

`pip install flake8-black` · installs (wheel) · licence: MIT · rank 6536 · last release 2026-11-03 · [PyPI](https://pypi.org/project/flake8-black/) · [docs](https://github.com/peterjc/flake8-black/blob/master/README.rst) · [source](https://github.com/peterjc/flake8-black/)

<details><summary>README extract</summary>

This is an MIT licensed flake8 plugin
for validating Python code style with the command line code formatting tool
black. It is available to install from
the Python Package Index (PyPI). ...

Sections: flake8-black, Introduction, Flake8 Validation codes, Python package management, Configuration, Ignoring validation codes, Ignoring files

</details>

### fhirclient

A flexible client for FHIR servers supporting the SMART on FHIR protocol

`pip install fhirclient` · installs (wheel) · licence: Apache Software License · rank 6540 · last release 2026-02-10 · [PyPI](https://pypi.org/project/fhirclient/) · [docs](https://docs.smarthealthit.org/client-py/)

<details><summary>README extract</summary>

This is _fhirclient_, a flexible Python client for FHIR servers supporting the SMART on FHIR protocol.

Client versioning is not identical to FHIR versioning.
The `main` branch is usually on the latest version of the client, as shown below, and possibly on their bugfix releases. ...

Example:
```python
from fhirclient import client
from fhirclient.models.patient import Patient

settings = {
    'app_id': 'my_web_app',
    'api_base': '
}
smart = client.FHIRClient(settings=settings)

patient = Patient.read('2cda5aad-e409-4070-9a15-e1c35c46ed5a', smart.server)
print(patient.birthDate.isostring)
# '1992-07-03'
...
```

...

</details>

### pyfunctional

Package for creating data pipelines with chain functional programming

`pip install pyfunctional` · installs (wheel) · licence: MIT License · rank 6556 · last release 2024-03-13 · [PyPI](https://pypi.org/project/pyfunctional/) · [docs](https://docs.pyfunctional.pedro.ai/en/master/) · [source](https://github.com/EntilZha/PyFunctional)

<details><summary>README extract</summary>

Features:
`PyFunctional` makes creating data pipelines easy by using chained functional operators. Here are a
few examples of what it can do:

- Chained operators: `seq(1, 2, 3).map(lambda x: x * 2).reduce(lambda x, y: x + y)` ...

Example:
```python
from functional import seq

seq(1, 2, 3, 4)\
    .map(lambda x: x * 2)\
    .filter(lambda x: x > 4)\
    .reduce(lambda x, y: x + y)
# 14

# or if you don't like backslash continuation
(seq(1, 2, 3, 4)
    .map(lambda x: x * 2)
    .filter(lambda x: x > 4)
    .reduce(lambda x, y: x + y)
)
# 14
```

...

</details>

### pyzxing

Reliable Python bindings for the ZXing barcode decoder.

`pip install pyzxing` · installs (wheel) · licence: MIT · rank 6567 · last release 2026-07-17 · [PyPI](https://pypi.org/project/pyzxing/) · [docs](https://pyzxing.readthedocs.io/) · [source](https://github.com/ChenjieXu/pyzxing)

<details><summary>README extract</summary>

English | 简体中文

Reliable Python bindings for the ZXing
barcode decoder. pyzxing exposes a stable Python API while delegating decoding
to a versioned, checksum-verified Java Runner.

Features:
- Decode one image or a glob of images into one consistent result list.
- Read QR Code, Data Matrix, PDF417, Aztec, and common one-dimensional formats.
- Accept file paths and NumPy arrays. ...

Example:
```python
from pyzxing import BarCodeReader

reader = BarCodeReader()
results = reader.decode("/path/to/qrcode.png")

for result in results:
    print(result["format"], result["text"])
```

Sections: pyzxing, Features, Requirements, Quick start, NumPy arrays, Results, Documentation, Command-line examples, Project links

</details>

### async-factory-boy

factory_boy extension with asynchronous ORM support

`pip install async-factory-boy` · installs (wheel) · licence: MIT License · rank 6568 · last release 2023-08-12 · [PyPI](https://pypi.org/project/async-factory-boy/)

<details><summary>README extract</summary>

factory_boy extension
with asynchronous ORM support

- python (3.8, 3.9, 3.10)

Install using `pip`

Example:
```python
from async_factory_boy.factory.sqlalchemy import AsyncSQLAlchemyFactory

class TestModelFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = TestModel
        session = session

    name = Faker("name")
    created_at = Faker("date_time")
```

Sections: async_factory_boy, Requirements, Instalation, Usage, For test configuration examples check `tests/` directory.

</details>

### pluginlib

A framework for creating and importing plugins

`pip install pluginlib` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 6574 · last release 2026-04-26 · [PyPI](https://pypi.org/project/pluginlib/)

<details><summary>README extract</summary>

docsgh_actionscodecov|
pypisupported-versionssupported-implementations|
fedoraEPEL|

Features:
Pluginlib makes creating plugins for your project simple.

Example:
```python
"""
sample.py
"""
import pluginlib

@pluginlib.Parent('parser')
class Parser():

    @pluginlib.abstractmethod
    def parse(self, string):
        pass
```

Sections: Overview, Features, PIP, Fedora and EL (RHEL/CentOS/Rocky/Alma), EL7 (RHEL/CentOS), Usage, Step 1: Define plugin parent classes, Step 2: Define plugin classes, Step 3: Load plugins

</details>

### allpairspy

Pairwise test combinations generator

`pip install allpairspy` · installs (wheel) · licence: MIT License · rank 6584 · last release 2023-07-08 · [PyPI](https://pypi.org/project/allpairspy/) · [source](https://github.com/thombashi/allpairspy)

<details><summary>README extract</summary>

AllPairs is an open source test combinations generator written in
Python, developed and maintained by MetaCommunications Engineering.
The generator allows one to create a set of tests using "pairwise
combinations" method, reducing a number of combinations of variables
into a lesser set that covers most situations. ...

Features:
* Produces good enough dataset.
* Pythonic, iterator-style enumeration interface.
* Allows to filter out "invalid" combinations during search for the next combination.
* Goes beyond pairs! If/when required can generate n-wise combinations.

Sections: AllPairs test combinations generator, Features, Get Started, Basic Usage, Filtering, Data Source: OrderedDict, Other Examples, Known issues, Dependencies

</details>

### contentful

Contentful Delivery API Client

`pip install contentful` · installs (wheel) · licence: MIT License · rank 6586 · last release 2025-08-29 · [PyPI](https://pypi.org/project/contentful/) · [docs](https://contentful.github.io/contentful.py) · [source](https://github.com/contentful/contentful.py)

<details><summary>README extract</summary>

What is Contentful?

Contentful provides a content infrastructure for digital teams to power content in websites, apps, and devices. Unlike a CMS, Contentful was built to integrate with the modern software stack. ...

Example:
```python
import contentful

client = contentful.Client(
  'cfexampleapi',  # This is the space ID. A space is like a project folder in Contentful terms
  'b4c0n73n7fu1'  # This is the access token for this space. Normally you get both ID and the token in the Contentful web app
)

...
```

...

</details>

### aiogithubapi

Asynchronous Python client for the GitHub API

`pip install aiogithubapi` · installs (wheel) · licence: MIT · rank 6615 · last release 2026-02-28 · [PyPI](https://pypi.org/project/aiogithubapi/) · [source](https://github.com/ludeeus/aiogithubapi)

<details><summary>README extract</summary>

_Asynchronous Python client for the GitHub API

This is not a full client for the API (Have you seen it, it's huge), and will probably never be.
Things are added when needed or requested.

If something you need is missing please raise a feature request to have it added or create a PR 🎉.

For examples on how to use it see the tests directory.

Sections: aiogithubapi, Project transition, Versioning

</details>

### everett

Configuration library for Python applications

`pip install everett` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 6625 · last release 2025-10-15 · [PyPI](https://pypi.org/project/everett/) · [source](https://github.com/willkg/everett/)

<details><summary>README extract</summary>

Status 2025-10-15: This project is deprecated.

Everett is a Python configuration library for your app.

:Code:
:Issues:
:License: MPL v2
:Documentation:

Goals of Everett:

1. flexible configuration from multiple configured environments
2. easy testing with configuration
3. easy automated documentation of configuration for users ...

Features:
Most other libraries I looked at had one or more of the following issues:

* were tied to a specific web app framework
* didn't allow you to specify configuration sources
* provided poor error messages when users configure things wrong
* had a ...

Example:
```python
# myserver.py

"""
Minimal example showing how to use configuration for a web app.
"""

from everett.manager import ConfigManager

config = ConfigManager.basic_config(
...

</details>

### observable

minimalist event system

`pip install observable` · installs (wheel) · licence: MIT License · rank 6629 · last release 2018-09-20 · [PyPI](https://pypi.org/project/observable/)

<details><summary>README extract</summary>

pyobservable is a minimalist event system for python. It provides you an easy-to-use interface to trigger arbitrary functions when specific events occur.

Note: We are Python 3 only! Only Python Versions >= 3.5 are supported. Use v0.3.2 for older Python Versions.

Example:
```python
from observable import Observable

obs = Observable()
```

Sections: observable, How to use, Usage, `on`: Register event handler with `on`, `once`: Register event handler with `once`, `trigger`: trigger event, `off`: remove handler and events

</details>

### rapidgzip

Parallel random access to gzip files

`pip install rapidgzip` · installs (wheel) · licence: Apache Software License; MIT License · rank 6639 · last release 2026-11-07 · [PyPI](https://pypi.org/project/rapidgzip/)

<details><summary>README extract</summary>

Example:
```python
A gzip decompressor tool based on the rapidgzip backend from ratarmount
Usage:
  rapidgzip [OPTION...] positional parameters

 Actions options:
  -d, --decompress        Force decompression. Only for compatibility. No
                          compression supported anyways.
      --import-index arg  Uses an existing gzip index.
...
```

...

</details>

### flake8-broken-line

Flake8 plugin to forbid backslashes for line breaks

`pip install flake8-broken-line` · installs (wheel) · licence: MIT License · rank 6642 · last release 2023-05-31 · [PyPI](https://pypi.org/project/flake8-broken-line/) · [source](https://github.com/wemake-services/flake8-broken-line)

<details><summary>README extract</summary>

Do not break the line! 🚨

Example:
```python
# String line breaks, use `()` or `"""` instead:

some_string = 'first line\
second line'

# Use a single line, `()`, or new variables instead:

if 1 == 1 and \
    2 == 2:
    print('Do not do that!')

# Do not use for method chaining:
some_object \
  .call_method(param1, param2) \
  .call_other(keyword=value) \
  .finalize()

# Instead use:
...
```

Sections: flake8-broken-line, Code example, Error codes

</details>

### python-i18n

Translation library for Python

`pip install python-i18n` · installs (wheel) · licence: MIT License · rank 6649 · last release 2020-08-26 · [PyPI](https://pypi.org/project/python-i18n/)

<details><summary>README extract</summary>

This library provides i18n functionality for Python 3 out of the box. The usage is mostly based on Rails i18n library.

Sections: python-i18n, Usage, Basic usage, Using translation files, Memoization, Namespaces, File namespaces, Directory namespaces, Functionalities, Placeholder, Pluralization, Fallback, Skip locale from root

</details>

### langwatch

LangWatch Python SDK, for monitoring your LLMs

`pip install langwatch` · does not install on CPython 3.14 · licence: MIT License · rank 6653 · last release 2026-09-06 · [PyPI](https://pypi.org/project/langwatch/)

<details><summary>README extract</summary>

The LangWatch Python SDK allows you to integrate LangWatch into your Python application to start observing your LLM interactions. This guide covers the setup and basic usage of the LangWatch Python SDK.

First, you need a LangWatch API key. Sign up at app.langwatch.ai and find your API key in your project settings. ...

Example:
```python
import langwatch

# The SDK will automatically use the LANGWATCH_API_KEY environment variable
# Or you can pass it explicitly: langwatch.setup(api_key="your_api_key")
langwatch.setup()

# Your application code...
```

...

</details>

### python-envcfg

Accessing environment variables with a magic module.

`pip install python-envcfg` · installs (wheel) · licence: MIT License · rank 6670 · last release 2016-07-07 · [PyPI](https://pypi.org/project/python-envcfg/)

<details><summary>README extract</summary>

Accessing environment variables with a magic module.

It works with many frameworks such as Django and Flask. Then you can store your
config in the environment variables instead of framework-specific config files.
It is recommended by 12-Factor.

Example:
```python
>>> import os
>>> from envcfg.raw.python import CONFIGURE_OPTS
>>>
>>> CONFIGURE_OPTS
'--enable-shared --enable-universalsdk=/ --with-universal-archs=intel'
>>> CONFIGURE_OPTS == os.environ['PYTHON_CONFIGURE_OPTS']
True
```

Sections: python-envcfg, Examples, Uses with Flask, Uses with Django, Uses with Tornado, Works on Projects, Issues

</details>

### tox-gh-actions

Seamless integration of tox into GitHub Actions

`pip install tox-gh-actions` · installs (wheel) · licence: MIT License · rank 6671 · last release 2025-10-22 · [PyPI](https://pypi.org/project/tox-gh-actions/)

<details><summary>README extract</summary>

Features:
When running tox on GitHub Actions, tox-gh-actions
* detects which environment to run based on configurations and
* provides utilities such as grouping log lines.

Sections: Features, Usage, Examples, Basic Example, tox-gh-actions Configuration, Workflow Configuration, Advanced Examples, Factor-Conditional Settings: Python Version, Factor-Conditional Settings: Environment Variable, tox requires, Overriding Environments to Run, Versioning, Versions and Compatibility, Understanding Behavior of tox-gh-actions

</details>

### deflate

Python wrapper for libdeflate.

`pip install deflate` · installs (wheel) · licence: MIT License · rank 6672 · last release 2026-08-24 · [PyPI](https://pypi.org/project/deflate/)

<details><summary>README extract</summary>

This is a very thin Python wrapper Eric Biggers' excellent
libdeflate.

Currently, it handles:

The original size of the decompressed data needs to be kept through additional logic.

Example:
```python
import deflate

level = 6  # The default; may be 1-12 for libdeflate.
compressed = deflate.gzip_compress(b"hello world!" * 1000, level)
original = deflate.gzip_decompress(compressed)
```

Sections: deflate API, Compression and decompression of raw DEFLATE or zlib data, CRC32 computation, Adler-32 computation

</details>

### mkdocs-static-i18n

MkDocs i18n plugin using static translation markdown files

`pip install mkdocs-static-i18n` · installs (wheel) · licence: MIT · rank 6675 · last release 2026-02-20 · [PyPI](https://pypi.org/project/mkdocs-static-i18n/) · [docs](https://github.com/ultrabug/mkdocs-static-i18n#readme) · [source](https://github.com/ultrabug/mkdocs-static-i18n)

<details><summary>README extract</summary>

*The MkDocs plugin that helps you support multiple language versions of your site / documentation.*

*Like what you :eyes:? Using this plugin? Give it a :star:!*

The `mkdocs-static-i18n` plugin allows you to support multiple languages of your documentation by adding static translation files to your existing documentation pages. ...

Sections: MkDocs static i18n plugin, Documentation, Upgrading from 0.x versions, See it in action

</details>

### brevo-python

(no summary)

`pip install brevo-python` · installs (wheel) · licence: not stated · rank 6684 · last release 2026-10-13 · [PyPI](https://pypi.org/project/brevo-python/) · [docs](https://developers.brevo.com) · [source](https://github.com/getbrevo/brevo-python)

<details><summary>README extract</summary>

Website · API Reference · Support

Official SDK for the Brevo API.

Example:
```python
from brevo import Brevo
from brevo.transactional_emails import (
    SendTransacEmailRequestSender,
    SendTransacEmailRequestToItem,
)

client = Brevo(
    api_key="YOUR_API_KEY",
)
client.transactional_emails.send_transac_email(
...
```

Sections: Brevo Python SDK, Documentation, Reference, Upgrading from v4.x, Breaking changes, Added, Migration from v1.x, Usage, Authentication, API key, OAuth 2.0 machine-to-machine (M2M), Async Client, Exception Handling, Advanced

</details>

### starsessions

Advanced sessions for Starlette and FastAPI frameworks

`pip install starsessions` · installs (wheel) · licence: MIT License · rank 6700 · last release 2024-10-23 · [PyPI](https://pypi.org/project/starsessions/) · [docs](https://github.com/alex-oleshkevich/starsessions) · [source](https://github.com/alex-oleshkevich/starsessions)

<details><summary>README extract</summary>

from sqlite3 import connect

Advanced sessions for Starlette and FastAPI frameworks

Example:
```python
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import JSONResponse
from starlette.routing import Route

from starsessions import CookieStore, load_session, SessionMiddleware

async def index_view(request):
    await load_session(request)

    session_data = request.session
...
```

Sections: Starsessions, Quick start, Usage, Loading session, Session autoload, Rolling sessions, Cookie path, Cookie domain, Session-only cookies, Built-in stores, Memory, CookieStore, Redis, Redis key prefix

</details>

### infi.systray

Windows system tray icon

`pip install infi.systray` · installs (wheel) · licence: BSD License · rank 6705 · last release 2025-01-11 · [PyPI](https://pypi.org/project/infi.systray/)

<details><summary>README extract</summary>

For the complete document, please refer to the README.md file over at GitHub

</details>

### pyu2f

U2F host library for interacting with a U2F device over USB.

`pip install pyu2f` · installs from source (sdist only) · licence: Apache Software License · rank 6709 · last release 2020-10-30 · [PyPI](https://pypi.org/project/pyu2f/)

<details><summary>README extract</summary>

pyu2f is a python based U2F host library for Linux, Windows, and MacOS. It provides functionality for interacting with a U2F device over USB.

</details>

