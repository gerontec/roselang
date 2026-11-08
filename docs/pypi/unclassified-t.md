# Unclassified / T (part 1 of 2)

[Index](README.md) · 514 packages in this topic, by downloads.

part 1 · [part 2](unclassified-t-2.md)

### tzdata

Provider of IANA time zone data

`pip install tzdata` · installs (wheel) · licence: Apache-2.0 · rank 51 · last release 2026-10-28 · [PyPI](https://pypi.org/project/tzdata/) · [docs](https://tzdata.python.org) · [source](https://github.com/python/tzdata)

<details><summary>README extract</summary>

This is a Python package containing `zic`-compiled binaries for the IANA time
zone database. It is intended to be a fallback for systems that do not have
system time zone data installed (or don't have it installed in a standard
location), as a part of PEP 615.

This repository generates a `pip`-installable package, published on PyPI as
tzdata. ...

</details>

### tomlkit

Style preserving TOML library

`pip install tomlkit` · installs (wheel) · licence: MIT · rank 53 · last release 2026-10-16 · [PyPI](https://pypi.org/project/tomlkit/) · [source](https://github.com/python-poetry/tomlkit)

<details><summary>README extract</summary>

[](
[](
[](
[](

[](

TOML Kit is a 1.1.0-compliant TOML library.

It includes a parser that preserves all comments, indentations, whitespace and internal element ordering,
and makes them accessible and editable via an intuitive API.

You can also create new TOML documents from scratch using the provided helpers. ...

Sections: TOML Kit - Style-preserving TOML library for Python, Usage, Limitations, Running tests

</details>

### trove-classifiers

Canonical source for classifiers on PyPI (pypi.org).

`pip install trove-classifiers` · installs (wheel) · licence: Apache Software License · rank 79 · last release 2026-09-21 · [PyPI](https://pypi.org/project/trove-classifiers/)

<details><summary>README extract</summary>

Canonical source for classifiers on PyPI.

Classifiers categorize projects per PEP 301. Use this package to
validate classifiers in packages for PyPI upload or download.

Example:
```python
>>> from trove_classifiers import classifiers
>>> 'License :: OSI Approved' in classifiers
True
>>> 'Fuzzy :: Wuzzy :: Was :: A :: Bear' in classifiers
False
>>>
```

Sections: Usage, Classifiers (`trove_classifiers.classifiers`)

</details>

### truststore

Verify certificates using native system trust stores

`pip install truststore` · installs (wheel) · licence: MIT · rank 94 · last release 2026-10-12 · [PyPI](https://pypi.org/project/truststore/) · [docs](https://truststore.readthedocs.io) · [source](https://github.com/sethmlarson/truststore)

<details><summary>README extract</summary>

Truststore is a library which exposes native system certificate stores (ie "trust stores")
through an `ssl.SSLContext`-like API. This means that Python applications no longer need to
rely on certifi as a root certificate store. Native system certificate stores
have many helpful features compared to a static certificate bundle like certifi: ...

Example:
```python
import truststore
truststore.inject_into_ssl()

# Automatically works with urllib3, requests, aiohttp, and more:
import urllib3
http = urllib3.PoolManager()
resp = http.request("GET", "

import aiohttp
http = aiohttp.ClientSession()
resp = await http.request("GET", "

import requests
resp = requests.get("
```

Sections: Truststore, User Guide

</details>

### tiktoken

tiktoken is a fast BPE tokeniser for use with OpenAI's models

`pip install tiktoken` · installs (wheel) · licence: not stated · rank 154 · last release 2026-08-17 · [PyPI](https://pypi.org/project/tiktoken/) · [source](https://github.com/openai/tiktoken)

<details><summary>README extract</summary>

tiktoken is a fast BPE tokeniser for use with
OpenAI's models.

The open source version of `tiktoken` can be installed from PyPI:

The tokeniser API is documented in `tiktoken/core.py`.

Example code using `tiktoken` can be found in the
OpenAI Cookbook.

Example:
```python
import tiktoken
enc = tiktoken.get_encoding("o200k_base")
assert enc.decode(enc.encode("hello world")) == "hello world"

# To get the tokeniser corresponding to a specific model in the OpenAI API:
enc = tiktoken.encoding_for_model("gpt-4o")
```

Sections: ⏳ tiktoken, Performance, Getting help, What is BPE anyway?, Extending tiktoken

</details>

### tzlocal

tzinfo object for the local timezone

`pip install tzlocal` · installs (wheel) · licence: MIT · rank 174 · last release 2026-10-22 · [PyPI](https://pypi.org/project/tzlocal/) · [source](https://github.com/regebro/tzlocal)

<details><summary>README extract</summary>

With version 3.0 of tzlocal, tzlocal no longer returned `pytz` objects, but
`zoneinfo` objects, which has a different API. Since 4.0, it now restored
partial compatibility for `pytz` users through Paul Ganssle's
`pytz_deprecation_shim`. ...

Example:
```python
import logging
logging.basicConfig(level="DEBUG")
import tzlocal
tzlocal.get_localzone()
```

Sections: tzlocal, API CHANGE!, Info, What it's not for, Notes on Docker, Usage, Troubleshooting

</details>

### toml

Python Library for Tom's Obvious, Minimal Language

`pip install toml` · installs (wheel) · licence: MIT License · rank 230 · last release 2020-11-01 · [PyPI](https://pypi.org/project/toml/)

<details><summary>README extract</summary>

A Python library for parsing and creating TOML.

The module passes the TOML test suite.

See also:

* The TOML Standard
* The currently supported TOML specification

Example:
```python
>>> import toml
>>> toml_string = """
... # This is a TOML document.
...
... title = "TOML Example"
...
... [owner]
... name = "Tom Preston-Werner"
... dob = 1979-05-27T07:32:00-08:00 # First class dates
...
... [database]
... server = "192.168.1.1"
... ports = [ 8001, 8001, 8002 ]
... connection_max = 5000
... enabled = true
...
... [servers]
...
...
```

Sections: TOML, Quick Tutorial, Note, API Reference, Licensing

</details>

### traitlets

Traitlets Python configuration system

`pip install traitlets` · installs (wheel) · licence: BSD License · rank 236 · last release 2026-08-03 · [PyPI](https://pypi.org/project/traitlets/) · [docs](https://traitlets.readthedocs.io) · [source](https://github.com/ipython/traitlets)

<details><summary>README extract</summary>

| | |

| home | |
| pypi-repo | |
| docs | |
| license | Modified BSD License |

Traitlets is a pure Python library enabling:

- the enforcement of strong typing for attributes of Python objects
 (typed attributes are called _"traits"_);
- dynamically calculated default values; ...

Example:
```python
import getpass
from traitlets import HasTraits, Unicode, default

class Identity(HasTraits):
    username = Unicode()

    @default('username')
    def _username_default(self):
        return getpass.getuser()
```

Sections: Traitlets, Running the tests, Code Styling, Usage, Dynamic default values, Callbacks when a trait attribute changes, Validation and coercion, Our Copyright Policy

</details>

### tornado

Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed.

`pip install tornado` · installs (wheel) · licence: Apache Software License · rank 264 · last release 2026-10-21 · [PyPI](https://pypi.org/project/tornado/) · [source](https://github.com/tornadoweb/tornado)

<details><summary>README extract</summary>

Tornado is a Python web framework and
asynchronous networking library, originally developed at FriendFeed. By using non-blocking network I/O, Tornado
can scale to tens of thousands of open connections, making it ideal for
long polling,
WebSockets, and other
applications that require a long-lived connection to each user. ...

Example:
```python
import asyncio
import tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if name == "main":
...
```

Sections: Tornado Web Server, Hello, world, Documentation

</details>

### typedload

Load and dump data from json-like format into typed data structures

`pip install typedload` · installs (wheel) · licence: GPL-3.0-only · rank 301 · last release 2026-05-23 · [PyPI](https://pypi.org/project/typedload/)

_README extract left out: share-alike licence._

### types-PyYAML

Typing stubs for PyYAML

`pip install types-PyYAML` · installs (wheel) · licence: Apache-2.0 · rank 307 · last release 2026-11-03 · [PyPI](https://pypi.org/project/types-PyYAML/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `PyYAML` package. It can be used by type checkers
to check code that uses `PyYAML`. This version of
`types-PyYAML` aims to provide accurate annotations for
`PyYAML==6.0.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-requests

Typing stubs for requests

`pip install types-requests` · installs (wheel) · licence: Apache-2.0 · rank 333 · last release 2026-10-30 · [PyPI](https://pypi.org/project/types-requests/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `requests` package. It can be used by type checkers
to check code that uses `requests`. This version of
`types-requests` aims to provide accurate annotations for
`requests~=2.33.0`.

Note: `types-requests` has required `urllib3>=2` since v2.31.0.7. ...

</details>

### types-protobuf

Typing stubs for protobuf

`pip install types-protobuf` · installs (wheel) · licence: Apache-2.0 · rank 363 · last release 2026-09-06 · [PyPI](https://pypi.org/project/types-protobuf/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `protobuf` package. It can be used by type checkers
to check code that uses `protobuf`. This version of
`types-protobuf` aims to provide accurate annotations for
`protobuf~=7.35.1`.

Partially generated using mypy-protobuf==3.6.0 and libprotoc 35.1 on protobuf v35.1 (python `protobuf==7.35.1`). ...

</details>

### toolz

List processing tools and functional utilities

`pip install toolz` · installs (wheel) · licence: BSD-3-Clause · rank 377 · last release 2026-10-07 · [PyPI](https://pypi.org/project/toolz/) · [docs](https://toolz.readthedocs.io/en/latest/) · [source](https://github.com/pytoolz/toolz)

<details><summary>README extract</summary>

A set of utility functions for iterators, functions, and dictionaries.

See the PyToolz documentation at

Example:
```python
>>> def stem(word):
...     """ Stem word to primitive form """
...     return word.lower().rstrip(",.!:;'-\"").lstrip("'\"")

>>> from toolz import compose, frequencies
>>> from toolz.curried import map
>>> wordcount = compose(frequencies, map(stem), str.split)

>>> sentence = "This cat jumped over this other cat!"
>>> wordcount(sentence)
...
```

Sections: Toolz, Structure and Heritage, Example, Dependencies, CyToolz, See Also

</details>

### typeguard

Run-time type checker for Python

`pip install typeguard` · installs (wheel) · licence: MIT · rank 398 · last release 2026-07-26 · [PyPI](https://pypi.org/project/typeguard/) · [docs](https://typeguard.readthedocs.io/en/latest/) · [source](https://github.com/agronholm/typeguard)

<details><summary>README extract</summary>

This library provides run-time type checking for functions defined with
PEP 484 argument (and return) type
annotations, and any arbitrary objects. It can be used together with static type
checkers as an additional layer of type safety, to catch type violations that could only
be detected at run time. ...

Sections: . The `check_type` function, . Code instrumentation, . the `@typechecked` function

</details>

### textual

Modern Text User Interface framework

`pip install textual` · installs (wheel) · licence: MIT License · rank 406 · last release 2026-06-30 · [PyPI](https://pypi.org/project/textual/) · [docs](https://textual.textualize.io/) · [source](https://github.com/Textualize/textual)

<details><summary>README extract</summary>

Build cross-platform user interfaces with a simple Python API. Run your apps in the terminal *or* a web browser.

Textual's API combines modern Python with the best of developments from the web world, for a lean app development experience.
De-coupled components and an advanced testing framework ensure you can maintain your app for the long-term. ...

Example:
```python
"""
An App to show the current time.
"""

from datetime import datetime

from textual.app import App, ComposeResult
from textual.widgets import Digits

class ClockApp(App):
    CSS = """
    Screen { align: center middle; }
    Digits { width: auto; }
    """

    def compose(self) -> ComposeResult:
        yield Digits("")

...
```

...

</details>

### types-toml

Typing stubs for toml

`pip install types-toml` · installs (wheel) · licence: Apache-2.0 · rank 430 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-toml/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `toml` package. It can be used by type checkers
to check code that uses `toml`. This version of
`types-toml` aims to provide accurate annotations for
`toml==0.10.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

</details>

### types-certifi

Typing stubs for certifi

`pip install types-certifi` · installs (wheel) · licence: Apache Software License · rank 454 · last release 2022-06-09 · [PyPI](https://pypi.org/project/types-certifi/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `certifi` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `certifi`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-python-dateutil

Typing stubs for python-dateutil

`pip install types-python-dateutil` · installs (wheel) · licence: Apache-2.0 · rank 503 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-python-dateutil/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `python-dateutil` package. It can be used by type checkers
to check code that uses `python-dateutil`. This version of
`types-python-dateutil` aims to provide accurate annotations for
`python-dateutil==2.9.*`.

This package is part of the typeshed project. ...

</details>

### temporalio

Temporal.io Python SDK

`pip install temporalio` · installs (wheel) · licence: MIT · rank 516 · last release 2026-10-28 · [PyPI](https://pypi.org/project/temporalio/) · [docs](https://docs.temporal.io/docs/python) · [source](https://github.com/temporalio/sdk-python)

<details><summary>README extract</summary>

Temporal is a distributed, scalable, durable, and highly available orchestration engine used to
execute asynchronous, long-running business logic in a scalable and resilient way.

"Temporal Python SDK" is the framework for authoring workflows and activities using the Python programming language. ...

Example:
```python
# Use the plugin when connecting
client = await Client.connect(
    "my-server.com:7233",
    plugins=[SomePlugin()]
)
```

Sections: Quick Start, Implementing a Workflow, Running a Workflow, Next Steps, Usage, Client, Data Conversion, Custom Type Data Conversion, External Storage, Driver Selection, Built-in Drivers, Custom Drivers, Workers, Workflows

</details>

### types-pytz

Typing stubs for pytz

`pip install types-pytz` · installs (wheel) · licence: Apache-2.0 · rank 684 · last release 2026-10-31 · [PyPI](https://pypi.org/project/types-pytz/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `pytz` package. It can be used by type checkers
to check code that uses `pytz`. This version of
`types-pytz` aims to provide accurate annotations for
`pytz==2026.6`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

</details>

### tifffile

Read and write TIFF files

`pip install tifffile` · installs (wheel) · licence: BSD-3-Clause · rank 755 · last release 2026-10-16 · [PyPI](https://pypi.org/project/tifffile/) · [docs](https://www.cgohlke.com/docs/tifffile/) · [source](https://github.com/cgohlke/tifffile)

<details><summary>README extract</summary>

Tifffile is a comprehensive Python library to

(1) store NumPy arrays in TIFF (Tagged Image File Format) files, and
(2) read image and metadata from TIFF-like files used in bioimaging. ...

Sections: Read and write TIFF files, Quickstart, Requirements, Revisions, Notes, References, Examples

</details>

### types-setuptools

Typing stubs for setuptools

`pip install types-setuptools` · installs (wheel) · licence: Apache-2.0 · rank 761 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-setuptools/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `setuptools` package. It can be used by type checkers
to check code that uses `setuptools`. This version of
`types-setuptools` aims to provide accurate annotations for
`setuptools==84.2.*`.

Given that `pkg_resources` is typed since `setuptools >= 71.1`, it is no longer included with `types-setuptools`. ...

</details>

### time-machine

Travel through time in your tests.

`pip install time-machine` · installs (wheel) · licence: MIT · rank 791 · last release 2026-10-25 · [PyPI](https://pypi.org/project/time-machine/) · [docs](https://time-machine.readthedocs.io/) · [source](https://github.com/adamchainz/time-machine)

<details><summary>README extract</summary>

*Travel through time in your tests.*

A quick example:

Please see

Example:
```python
import datetime as dt
from zoneinfo import ZoneInfo
import time_machine

hill_valley_tz = ZoneInfo("America/Los_Angeles")

@time_machine.travel(dt.datetime(1985, 10, 26, 1, 24, tzinfo=hill_valley_tz))
def test_delorean():
    assert dt.date.today().isoformat() == "1985-10-26"
```

Sections: time-machine, Documentation

</details>

### types-jsonschema

Typing stubs for jsonschema

`pip install types-jsonschema` · installs (wheel) · licence: Apache-2.0 · rank 859 · last release 2026-10-06 · [PyPI](https://pypi.org/project/types-jsonschema/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `jsonschema` package. It can be used by type checkers
to check code that uses `jsonschema`. This version of
`types-jsonschema` aims to provide accurate annotations for
`jsonschema~=4.26.0`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### torchvision

image and video datasets and models for torch deep learning

`pip install torchvision` · installs (wheel) · licence: BSD · rank 907 · last release 2026-10-28 · [PyPI](https://pypi.org/project/torchvision/)

<details><summary>README extract</summary>

The torchvision package consists of popular datasets, model architectures, and common image transformations for computer
vision.

Sections: torchvision, Image Backends, Documentation, Disclaimer on Datasets, Citing TorchVision

</details>

### types-urllib3

Typing stubs for urllib3

`pip install types-urllib3` · installs (wheel) · licence: Apache Software License · rank 921 · last release 2023-07-20 · [PyPI](https://pypi.org/project/types-urllib3/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `urllib3` package. It
can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`urllib3`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-cachetools

Typing stubs for cachetools

`pip install types-cachetools` · installs (wheel) · licence: Apache-2.0 · rank 925 · last release 2026-07-13 · [PyPI](https://pypi.org/project/types-cachetools/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `cachetools` package. It can be used by type checkers
to check code that uses `cachetools`. This version of
`types-cachetools` aims to provide accurate annotations for
`cachetools==7.0.*`.

*Note:* The `cachetools` package includes type annotations or type stubs
since version 7.1.0. ...

</details>

### twine

Collection of utilities for publishing packages on PyPI

`pip install twine` · installs (wheel) · licence: Apache-2.0 · rank 935 · last release 2026-07-27 · [PyPI](https://pypi.org/project/twine/) · [docs](https://twine.readthedocs.io/en/latest/) · [source](https://github.com/pypa/twine/)

<details><summary>README extract</summary>

Twine is a utility for publishing Python packages on PyPI.

It provides build system independent uploads of source and binary
distribution artifacts for both new and existing
projects.

See our documentation for a description of features, installation
and usage instructions, and links to additional resources.

</details>

### types-cffi

Typing stubs for cffi

`pip install types-cffi` · installs (wheel) · licence: Apache-2.0 · rank 974 · last release 2026-08-27 · [PyPI](https://pypi.org/project/types-cffi/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `cffi` package. It can be used by type checkers
to check code that uses `cffi`. This version of
`types-cffi` aims to provide accurate annotations for
`cffi==2.1.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

</details>

### types-redis

Typing stubs for redis

`pip install types-redis` · installs (wheel) · licence: Apache Software License · rank 980 · last release 2024-10-04 · [PyPI](https://pypi.org/project/types-redis/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561
type stub package for the `redis` package.
It can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`redis`.

This version of `types-redis` aims to provide accurate annotations
for `redis==4.6.0`. ...

</details>

### Twisted

An asynchronous networking framework written in Python

`pip install Twisted` · installs (wheel) · licence: MIT · rank 994 · last release 2026-10-30 · [PyPI](https://pypi.org/project/Twisted/) · [docs](https://docs.twisted.org/) · [source](https://github.com/twisted/twisted)

<details><summary>README extract</summary>

For information on changes in this release, see the NEWS file.

Sections: Twisted, What is this?, Unit Tests, Static Code Checkers, Copyright, Warranty

</details>

### types-pyOpenSSL

Typing stubs for pyOpenSSL

`pip install types-pyOpenSSL` · installs (wheel) · licence: Apache Software License · rank 997 · last release 2024-07-22 · [PyPI](https://pypi.org/project/types-pyOpenSSL/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561
type stub package for the `pyOpenSSL` package.
It can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`pyOpenSSL`.

This version of `types-pyOpenSSL` aims to provide accurate annotations
for `pyOpenSSL==24.1.*`. ...

</details>

### types-paramiko

Typing stubs for paramiko

`pip install types-paramiko` · installs (wheel) · licence: Apache-2.0 · rank 1000 · last release 2026-10-30 · [PyPI](https://pypi.org/project/types-paramiko/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `paramiko` package. It can be used by type checkers
to check code that uses `paramiko`. This version of
`types-paramiko` aims to provide accurate annotations for
`paramiko==5.1.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-Deprecated

Typing stubs for Deprecated

`pip install types-Deprecated` · installs (wheel) · licence: Apache-2.0 · rank 1104 · last release 2026-09-28 · [PyPI](https://pypi.org/project/types-Deprecated/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `Deprecated` package. It can be used by type checkers
to check code that uses `Deprecated`. This version of
`types-Deprecated` aims to provide accurate annotations for
`Deprecated~=1.3.1`.

*Note:* The `Deprecated` package includes type annotations or type stubs
since version 3.0.0. ...

</details>

### types-aiobotocore-s3

Type annotations for aiobotocore S3 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-s3` · installs (wheel) · licence: MIT · rank 1183 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-s3/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-aiobotocore

Type annotations for aiobotocore 3.10.0 generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore` · installs (wheel) · licence: MIT · rank 1188 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore/) · [docs](https://youtype.github.io/types_aiobotocore_docs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, How it works, What's new, Implemented features

</details>

### types-boto3

Type annotations for boto3 1.43.126 generated with mypy-boto3-builder 8.12.0

`pip install types-boto3` · installs (wheel) · licence: MIT · rank 1202 · last release 2026-11-06 · [PyPI](https://pypi.org/project/types-boto3/) · [docs](https://youtype.github.io/types_boto3_docs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 1.43.126
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found in
types-boto3 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-aiofiles

Typing stubs for aiofiles

`pip install types-aiofiles` · installs (wheel) · licence: Apache-2.0 · rank 1222 · last release 2026-11-07 · [PyPI](https://pypi.org/project/types-aiofiles/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `aiofiles` package. It can be used by type checkers
to check code that uses `aiofiles`. This version of
`types-aiofiles` aims to provide accurate annotations for
`aiofiles==25.1.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tyro

CLI interfaces & config objects, from types

`pip install tyro` · installs (wheel) · licence: MIT License · rank 1261 · last release 2026-11-04 · [PyPI](https://pypi.org/project/tyro/) · [docs](https://brentyi.github.io/tyro/) · [source](https://github.com/brentyi/tyro)

<details><summary>README extract</summary>

Documentation
 pip install tyro

tyro.cli() is a tool for generating CLI
interfaces from type-annotated Python.

We can define configurable scripts using functions:

Or instantiate configs defined using tools like `dataclasses`, `pydantic`, and `attrs`: ...

Features:
1. Define things once. Standard Python type annotations, docstrings, and default values are parsed to automatically generate command-line interfaces with nice helptext.

2. Static types. ...

Sections: tyro, Why `tyro`?, In the wild, Alternatives

</details>

### thefuzz

Fuzzy string matching in python

`pip install thefuzz` · installs (wheel) · licence: MIT License · rank 1292 · last release 2024-01-19 · [PyPI](https://pypi.org/project/thefuzz/)

<details><summary>README extract</summary>

Fuzzy string matching like a boss. It uses Levenshtein Distance to calculate the differences between sequences in a simple-to-use package.

- Python 3.8 or higher
- rapidfuzz

Example:
```python
>>> from thefuzz import fuzz
>>> from thefuzz import process
```

Sections: TheFuzz, Requirements, Usage, Simple Ratio, Partial Ratio, Token Sort Ratio, Token Set Ratio, Partial Token Sort Ratio, Process

</details>

### types-croniter

Typing stubs for croniter

`pip install types-croniter` · installs (wheel) · licence: Apache-2.0 · rank 1293 · last release 2026-10-06 · [PyPI](https://pypi.org/project/types-croniter/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `croniter` package. It can be used by type checkers
to check code that uses `croniter`. This version of
`types-croniter` aims to provide accurate annotations for
`croniter==6.2.4`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-Markdown

Typing stubs for Markdown

`pip install types-Markdown` · installs (wheel) · licence: Apache-2.0 · rank 1354 · last release 2026-11-07 · [PyPI](https://pypi.org/project/types-Markdown/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `Markdown` package. It can be used by type checkers
to check code that uses `Markdown`. This version of
`types-Markdown` aims to provide accurate annotations for
`Markdown~=3.11.2`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-psutil

Typing stubs for psutil

`pip install types-psutil` · installs (wheel) · licence: Apache-2.0 · rank 1383 · last release 2026-09-06 · [PyPI](https://pypi.org/project/types-psutil/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `psutil` package. It can be used by type checkers
to check code that uses `psutil`. This version of
`types-psutil` aims to provide accurate annotations for
`psutil==7.2.2`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-openpyxl

Typing stubs for openpyxl

`pip install types-openpyxl` · installs (wheel) · licence: Apache-2.0 · rank 1409 · last release 2026-10-17 · [PyPI](https://pypi.org/project/types-openpyxl/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `openpyxl` package. It can be used by type checkers
to check code that uses `openpyxl`. This version of
`types-openpyxl` aims to provide accurate annotations for
`openpyxl==3.1.5`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tree-sitter-languages

Binary Python wheels for all tree sitter languages.

`pip install tree-sitter-languages` · does not install on CPython 3.14 · licence: Apache Software License · rank 1410 · last release 2024-02-04 · [PyPI](https://pypi.org/project/tree-sitter-languages/) · [docs](https://github.com/grantjenks/py-tree-sitter-languages) · [source](https://github.com/grantjenks/py-tree-sitter-languages)

<details><summary>README extract</summary>

Binary Python wheels for all tree sitter languages.

py-tree-sitter is a fantastic library that provides Python bindings for the
even more fantastic tree-sitter parsing library.

py-tree-sitter-languages provides binary Python wheels for all tree sitter
languages. ...

Example:
```python
from tree_sitter_languages import get_language, get_parser

language = get_language('python')
parser = get_parser('python')
```

Sections: Python Bindings for Tree Sitter with All Languages, Usage, Demo

</details>

### types-psycopg2

Typing stubs for psycopg2

`pip install types-psycopg2` · installs (wheel) · licence: Apache-2.0 · rank 1439 · last release 2026-10-30 · [PyPI](https://pypi.org/project/types-psycopg2/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `psycopg2` package. It can be used by type checkers
to check code that uses `psycopg2`. This version of
`types-psycopg2` aims to provide accurate annotations for
`psycopg2==2.9.13`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-tabulate

Typing stubs for tabulate

`pip install types-tabulate` · installs (wheel) · licence: Apache-2.0 · rank 1467 · last release 2026-10-06 · [PyPI](https://pypi.org/project/types-tabulate/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `tabulate` package. It can be used by type checkers
to check code that uses `tabulate`. This version of
`types-tabulate` aims to provide accurate annotations for
`tabulate==0.10.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tokenize-rt

A wrapper around the stdlib `tokenize` which roundtrips.

`pip install tokenize-rt` · installs (wheel) · licence: MIT · rank 1471 · last release 2025-05-23 · [PyPI](https://pypi.org/project/tokenize-rt/)

<details><summary>README extract</summary>

The stdlib `tokenize` module does not properly roundtrip. This wrapper
around the stdlib provides two additional tokens `ESCAPED_NL` and
`UNIMPORTANT_WS`, and a `Token` data type. Use `src_to_tokens` and
`tokens_to_src` to roundtrip.

This library is useful if you're writing a refactoring tool based on the
python tokenization.

Example:
```python
>>> parse_string_literal('f"foo"')
('f', '"foo"')
```

...

</details>

### types-html5lib

Typing stubs for html5lib

`pip install types-html5lib` · installs (wheel) · licence: Apache-2.0 · rank 1495 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-html5lib/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `html5lib` package. It can be used by type checkers
to check code that uses `html5lib`. This version of
`types-html5lib` aims to provide accurate annotations for
`html5lib==1.1.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tavily-python

Python wrapper for the Tavily API

`pip install tavily-python` · installs (wheel) · licence: MIT License · rank 1505 · last release 2026-10-06 · [PyPI](https://pypi.org/project/tavily-python/)

<details><summary>README extract</summary>

The Tavily Python wrapper allows for easy interaction with the Tavily API, offering the full range of our search, extract, crawl, map, and research functionalities directly from your Python programs. Easily integrate smart search, content extraction, and research capabilities into your applications, harnessing Tavily's powerful features.

Example:
```python
result = tavily_client.get_research(request_id, include_usage=True)
print(result.get("usage", {}).get("credits"))
```

...

</details>

### types-tqdm

Typing stubs for tqdm

`pip install types-tqdm` · installs (wheel) · licence: Apache-2.0 · rank 1561 · last release 2026-11-06 · [PyPI](https://pypi.org/project/types-tqdm/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `tqdm` package. It can be used by type checkers
to check code that uses `tqdm`. This version of
`types-tqdm` aims to provide accurate annotations for
`tqdm==4.70.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

Sections: Typing stubs for tqdm, Optional dependencies

</details>

### types-PyMySQL

Typing stubs for PyMySQL

`pip install types-PyMySQL` · installs (wheel) · licence: Apache-2.0 · rank 1579 · last release 2026-09-23 · [PyPI](https://pypi.org/project/types-PyMySQL/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `PyMySQL` package. It can be used by type checkers
to check code that uses `PyMySQL`. This version of
`types-PyMySQL` aims to provide accurate annotations for
`PyMySQL==1.2.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-aioboto3

Type annotations for aioboto3 15.5.0 generated with mypy-boto3-builder 8.11.0

`pip install types-aioboto3` · installs (wheel) · licence: MIT License · rank 1617 · last release 2025-10-31 · [PyPI](https://pypi.org/project/types-aioboto3/) · [docs](https://youtype.github.io/types_aioboto3_docs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for aioboto3 15.5.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.11.0.

More information can be found in
types-aioboto3 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

...

</details>

### types-boto3-s3

Type annotations for boto3 S3 1.43.106 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-s3` · installs (wheel) · licence: MIT · rank 1633 · last release 2026-09-30 · [PyPI](https://pypi.org/project/types-boto3-s3/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_s3/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 S3 1.43.106
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-s3 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-retry

Typing stubs for retry

`pip install types-retry` · installs (wheel) · licence: Apache-2.0 · rank 1693 · last release 2026-04-08 · [PyPI](https://pypi.org/project/types-retry/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `retry` package. It can be used by type checkers
to check code that uses `retry`. This version of
`types-retry` aims to provide accurate annotations for
`retry==0.9.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

</details>

### types-webencodings

Typing stubs for webencodings

`pip install types-webencodings` · installs (wheel) · licence: Apache-2.0 · rank 1740 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-webencodings/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `webencodings` package. It can be used by type checkers
to check code that uses `webencodings`. This version of
`types-webencodings` aims to provide accurate annotations for
`webencodings==0.6.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tablib

Format agnostic tabular data library (XLS, JSON, YAML, CSV, etc.)

`pip install tablib` · installs (wheel) · licence: MIT License · rank 1756 · last release 2026-07-31 · [PyPI](https://pypi.org/project/tablib/) · [docs](https://tablib.readthedocs.io) · [source](https://github.com/jazzband/tablib)

<details><summary>README extract</summary>

_ __ ___ __
 /_ __ /_ _ /_(_)_ /_
 _ /_ `/ \ / / \
 / /_ / /_/ / _ /_/ /_ / _ / _ /_/ /
 \/ \,_/ /_._/ /_/ /_/ /_._/

Tablib is a format-agnostic tabular dataset library, written in Python.

Output formats supported:

- Excel (Sets + Books)
- JSON (Sets + Books)
- YAML (Sets + Books)
- Pandas DataFrames (Sets)
- HTML (Sets)
- Jira (Sets) ...

</details>

### tree-sitter-language-pack

Pre-compiled tree-sitter grammars for 371 programming languages

`pip install tree-sitter-language-pack` · installs (wheel) · licence: MIT · rank 1763 · last release 2026-11-06 · [PyPI](https://pypi.org/project/tree-sitter-language-pack/) · [source](https://github.com/xberg-io/tree-sitter-language-pack)

### types-python-slugify

Typing stubs for python-slugify

`pip install types-python-slugify` · installs (wheel) · licence: Apache Software License · rank 1803 · last release 2024-03-10 · [PyPI](https://pypi.org/project/types-python-slugify/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561
type stub package for the `python-slugify` package.
It can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`python-slugify`.

This version of `types-python-slugify` aims to provide accurate annotations
for `python-slugify==8.0.2`. ...

</details>

### types-six

Typing stubs for six

`pip install types-six` · installs (wheel) · licence: Apache-2.0 · rank 1850 · last release 2026-10-08 · [PyPI](https://pypi.org/project/types-six/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `six` package. It can be used by type checkers
to check code that uses `six`. This version of
`types-six` aims to provide accurate annotations for
`six==1.17.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

</details>

### thrift-sasl

Thrift SASL Python module that implements SASL transports for Thrift (`TSaslClientTransport`).

`pip install thrift-sasl` · installs (wheel) · licence: Apache License, Version 2.0 · rank 1862 · last release 2021-05-26 · [PyPI](https://pypi.org/project/thrift-sasl/)

<details><summary>README extract</summary>

Thrift SASL Python module that implements SASL transports for Thrift (`TSaslClientTransport`).

</details>

### types-Pillow

Typing stubs for Pillow

`pip install types-Pillow` · installs (wheel) · licence: Apache Software License · rank 1909 · last release 2024-08-22 · [PyPI](https://pypi.org/project/types-Pillow/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561
type stub package for the `Pillow` package.
It can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`Pillow`.

This version of `types-Pillow` aims to provide accurate annotations
for `Pillow==10.2.*`. ...

</details>

### types-docutils

Typing stubs for docutils

`pip install types-docutils` · installs (wheel) · licence: Apache-2.0 · rank 1942 · last release 2026-11-07 · [PyPI](https://pypi.org/project/types-docutils/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `docutils` package. It can be used by type checkers
to check code that uses `docutils`. This version of
`types-docutils` aims to provide accurate annotations for
`docutils==0.23`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-defusedxml

Typing stubs for defusedxml

`pip install types-defusedxml` · installs (wheel) · licence: Apache-2.0 · rank 1949 · last release 2026-05-04 · [PyPI](https://pypi.org/project/types-defusedxml/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `defusedxml` package. It can be used by type checkers
to check code that uses `defusedxml`. This version of
`types-defusedxml` aims to provide accurate annotations for
`defusedxml==0.7.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### torch-c-dlpack-ext

torch c dlpack ext

`pip install torch-c-dlpack-ext` · installs (wheel) · licence: Apache Software License · rank 1999 · last release 2026-01-12 · [PyPI](https://pypi.org/project/torch-c-dlpack-ext/)

<details><summary>README extract</summary>

<!--- Licensed to the Apache Software Foundation (ASF) under one -->
<!--- or more contributor license agreements. See the NOTICE file -->
<!--- distributed with this work for additional information -->
<!--- regarding copyright ownership. ...

</details>

### types-simplejson

Typing stubs for simplejson

`pip install types-simplejson` · installs (wheel) · licence: Apache-2.0 · rank 2001 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-simplejson/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `simplejson` package. It can be used by type checkers
to check code that uses `simplejson`. This version of
`types-simplejson` aims to provide accurate annotations for
`simplejson==4.2.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### torchcodec

A video decoder for PyTorch

`pip install torchcodec` · installs (wheel) · licence: not stated · rank 2022 · last release 2026-09-30 · [PyPI](https://pypi.org/project/torchcodec/) · [docs](https://pytorch.org/torchcodec/stable/index.html) · [source](https://github.com/pytorch/torchcodec)

<details><summary>README extract</summary>

Installation | Documentation | Contributing | License

TorchCodec is a PyTorch-native library for decoding and encoding media: videos,
audio, and images, on CPU and CUDA GPU. It aims to be fast, easy to
use, and well integrated into the PyTorch ecosystem. ...

Example:
```python
from torchcodec.decoders import VideoDecoder

device = "cpu"  # or e.g. "cuda" !
decoder = VideoDecoder("path/to/video.mp4", device=device)

decoder.metadata
# VideoStreamMetadata:
# num_frames: 250
# duration_seconds: 10.0
# bit_rate: 31315.0
# codec: h264
# average_fps: 25.0
# ... (truncated output)

# Simple Indexing API
...
```

Sections: Usage Examples, Video Decoding, Video and Audio Encoding, Image Decoding and Encoding, Compatibility with `torch` versions

</details>

### tensorboardX

TensorBoardX lets you watch Tensors Flow without Tensorflow

`pip install tensorboardX` · installs (wheel) · licence: MIT · rank 2029 · last release 2026-04-03 · [PyPI](https://pypi.org/project/tensorboardX/) · [source](https://github.com/lanpa/tensorboardX.git)

<details><summary>README extract</summary>

Sections: 2.6.5 (2026-04-03), 2.6.3 (2025-04-24), 2.6.2.2 (2023-08-20), 2.6.2.1 (2023-08-20), 2.6.2 (2023-07-30), 2.6.1 (2023-06-18), 2.6 (2023-02-12), 2.5.1 (2022-06-05), 2.5 (2022-02-22), 2.4.1 (2021-11-20), 2.4 (2021-06-30), 2.3 (2021-06-20), 2.2 (2021-04-03), 2.1 (2020-07-05)

</details>

### tableauserverclient

A Python module for working with the Tableau Server REST API.

`pip install tableauserverclient` · installs (wheel) · licence: MIT · rank 2071 · last release 2026-10-15 · [PyPI](https://pypi.org/project/tableauserverclient/) · [source](https://github.com/tableau/server-client-python)

<details><summary>README extract</summary>

Use the Tableau Server Client (TSC) library to increase your productivity as you interact with the Tableau Server REST API. With the TSC library you can do almost everything that you can do with the REST API, including:

* Publish workbooks and data sources.
* Create users and groups.
* Query projects, sites, and more. ...

</details>

### types-beautifulsoup4

Typing stubs for beautifulsoup4

`pip install types-beautifulsoup4` · installs (wheel) · licence: Apache-2.0 · rank 2105 · last release 2025-05-16 · [PyPI](https://pypi.org/project/types-beautifulsoup4/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561
type stub package for the `beautifulsoup4` package.
It can be used by type-checking tools like
mypy,
pyright,
pytype,
Pyre,
PyCharm, etc. to check code that uses `beautifulsoup4`. This version of
`types-beautifulsoup4` aims to provide accurate annotations for
`beautifulsoup4==4.12.*`. ...

</details>

### types-httplib2

Typing stubs for httplib2

`pip install types-httplib2` · installs (wheel) · licence: Apache-2.0 · rank 2200 · last release 2026-10-29 · [PyPI](https://pypi.org/project/types-httplib2/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `httplib2` package. It can be used by type checkers
to check code that uses `httplib2`. This version of
`types-httplib2` aims to provide accurate annotations for
`httplib2==0.32.1`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-regex

Typing stubs for regex

`pip install types-regex` · installs (wheel) · licence: Apache-2.0 · rank 2230 · last release 2026-10-30 · [PyPI](https://pypi.org/project/types-regex/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `regex` package. It can be used by type checkers
to check code that uses `regex`. This version of
`types-regex` aims to provide accurate annotations for
`regex==2026.9.29`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-boto3-ses

Type annotations for boto3 SES 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-ses` · installs (wheel) · licence: MIT · rank 2294 · last release 2026-04-29 · [PyPI](https://pypi.org/project/types-boto3-ses/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_ses/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SES 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-ses docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-aiobotocore-sqs

Type annotations for aiobotocore SQS 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-sqs` · installs (wheel) · licence: MIT · rank 2301 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-sqs/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-mock

Typing stubs for mock

`pip install types-mock` · installs (wheel) · licence: Apache-2.0 · rank 2364 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-mock/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `mock` package. It can be used by type checkers
to check code that uses `mock`. This version of
`types-mock` aims to provide accurate annotations for
`mock==5.2.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

</details>

### types-freezegun

Typing stubs for freezegun

`pip install types-freezegun` · installs (wheel) · licence: Apache Software License · rank 2416 · last release 2022-06-09 · [PyPI](https://pypi.org/project/types-freezegun/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `freezegun` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `freezegun`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-Pygments

Typing stubs for Pygments

`pip install types-Pygments` · installs (wheel) · licence: Apache-2.0 · rank 2439 · last release 2026-08-19 · [PyPI](https://pypi.org/project/types-Pygments/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `Pygments` package. It can be used by type checkers
to check code that uses `Pygments`. This version of
`types-Pygments` aims to provide accurate annotations for
`Pygments==2.21.*`.

This stub package is marked as partial.
If you find that annotations are missing, feel free to contribute and help complete them. ...

</details>

### types-MarkupSafe

Typing stubs for MarkupSafe

`pip install types-MarkupSafe` · installs (wheel) · licence: Apache Software License · rank 2460 · last release 2021-11-27 · [PyPI](https://pypi.org/project/types-MarkupSafe/)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `MarkupSafe` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `MarkupSafe`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-Jinja2

Typing stubs for Jinja2

`pip install types-Jinja2` · installs (wheel) · licence: Apache Software License · rank 2464 · last release 2021-11-26 · [PyPI](https://pypi.org/project/types-Jinja2/)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `Jinja2` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `Jinja2`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-ujson

Typing stubs for ujson

`pip install types-ujson` · installs (wheel) · licence: Apache-2.0 · rank 2544 · last release 2025-08-22 · [PyPI](https://pypi.org/project/types-ujson/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `ujson` package. It can be used by type checkers
to check code that uses `ujson`. This version of
`types-ujson` aims to provide accurate annotations for
`ujson==5.10.*`.

*Note:* The `ujson` package includes type annotations or type stubs
since version 5.11.0. ...

</details>

### types-boto3-sqs

Type annotations for boto3 SQS 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-sqs` · installs (wheel) · licence: MIT · rank 2606 · last release 2026-04-29 · [PyPI](https://pypi.org/project/types-boto3-sqs/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_sqs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SQS 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-sqs docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-lxml

Complete lxml external type annotation

`pip install types-lxml` · installs (wheel) · licence: Apache-2.0 · rank 2625 · last release 2026-02-17 · [PyPI](https://pypi.org/project/types-lxml/)

<details><summary>README extract</summary>

- Partial support of `ty` type checker
 - Supports type checking under `PyPy` 3.11

 - Support for `pyrefly` type checker
 - New `mypy` plugin that mimics `XMLParser.set_element_class_lookup()` behavior ...

Sections: Important note, Introduction, Goal ① : Completion, Goal ③: Review and test suite, Goal ④ : Geared towards users, Docstring, Warnings for exception and wrong code, Class inheritance change, Mypy plugin usage, Choosing the build

</details>

### types-Authlib

Typing stubs for Authlib

`pip install types-Authlib` · installs (wheel) · licence: Apache-2.0 · rank 2626 · last release 2026-11-06 · [PyPI](https://pypi.org/project/types-Authlib/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `Authlib` package. It can be used by type checkers
to check code that uses `Authlib`. This version of
`types-Authlib` aims to provide accurate annotations for
`Authlib==1.8.0`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

Sections: Typing stubs for Authlib, Optional dependencies

</details>

### types-grpcio

Typing stubs for grpcio

`pip install types-grpcio` · installs (wheel) · licence: Apache-2.0 · rank 2641 · last release 2026-10-28 · [PyPI](https://pypi.org/project/types-grpcio/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `grpcio` package. It can be used by type checkers
to check code that uses `grpcio`. This version of
`types-grpcio` aims to provide accurate annotations for
`grpcio~=1.85.0`.

This stub package is marked as partial.
If you find that annotations are missing, feel free to contribute and help complete them. ...

</details>

### types-click

Typing stubs for click

`pip install types-click` · installs (wheel) · licence: Apache Software License · rank 2644 · last release 2021-11-23 · [PyPI](https://pypi.org/project/types-click/)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `click` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `click`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-Werkzeug

Typing stubs for Werkzeug

`pip install types-Werkzeug` · installs (wheel) · licence: Apache Software License · rank 2650 · last release 2021-11-26 · [PyPI](https://pypi.org/project/types-Werkzeug/)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `Werkzeug` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `Werkzeug`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-boto3-rds

Type annotations for boto3 RDS 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-rds` · installs (wheel) · licence: MIT · rank 2660 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-boto3-rds/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_rds/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 RDS 1.43.124
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-rds docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-boto3-dynamodb

Type annotations for boto3 DynamoDB 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-dynamodb` · installs (wheel) · licence: MIT · rank 2669 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-boto3-dynamodb/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_dynamodb/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 DynamoDB 1.43.124
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-dynamodb docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### treescope

Treescope: An interactive HTML pretty-printer for ML research in IPython notebooks.

`pip install treescope` · installs (wheel) · licence: Apache Software License · rank 2683 · last release 2025-08-08 · [PyPI](https://pypi.org/project/treescope/) · [source](https://github.com/google-deepmind/treescope)

<details><summary>README extract</summary>

Treescope is an interactive HTML pretty-printer and N-dimensional array
("tensor") visualizer, designed for machine learning and neural networks
research in IPython notebooks. It's a drop-in replacement for the standard
IPython/Colab renderer, and adds support for: ...

Example:
```python
import treescope
```

Sections: Treescope, Getting Started

</details>

### textual-speedups

(no summary)

`pip install textual-speedups` · installs (wheel) · licence: not stated · rank 2694 · last release 2025-11-28 · [PyPI](https://pypi.org/project/textual-speedups/)

### types-boto3-ec2

Type annotations for boto3 EC2 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-ec2` · installs (wheel) · licence: MIT · rank 2704 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-boto3-ec2/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_ec2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 EC2 1.43.124
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-ec2 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-boto3-lambda

Type annotations for boto3 Lambda 1.43.123 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-lambda` · installs (wheel) · licence: MIT · rank 2742 · last release 2026-10-30 · [PyPI](https://pypi.org/project/types-boto3-lambda/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_lambda/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Lambda 1.43.123
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-lambda docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### taskiq-dependencies

FastAPI like dependency injection implementation

`pip install taskiq-dependencies` · installs (wheel) · licence: not stated · rank 2760 · last release 2025-02-26 · [PyPI](https://pypi.org/project/taskiq-dependencies/)

<details><summary>README extract</summary>

This project is used to add FastAPI-like dependency injection to projects.

This project is a part of the taskiq, but it doesn't have any dependencies,
and you can easily integrate it in any project.

Example:
```python
from taskiq_dependencies import Depends

def dep1() -> int:
    return 1

def target_func(some_int: int = Depends(dep1)):
    print(some_int)
    return some_int + 1
```

Sections: Taskiq dependencies, Usage, Async usage, Q&A, Getting parameters information, Exception propagation, Dependencies replacement, Annotated types

</details>

### torchao

Package for applying ao techniques to GPU models

`pip install torchao` · installs (wheel) · licence: not stated · rank 2766 · last release 2026-08-03 · [PyPI](https://pypi.org/project/torchao/)

<details><summary>README extract</summary>

- Pre-train Llama-3.1-70B 1.5x faster with float8 training
- Recover 67% of quantized accuracy degradation on Gemma3-4B with QAT
- Quantize Llama-3-8B to int4 for 1.89x faster inference with 58% less memory

Latest News | Overview | Quick Start | Installation | Integrations | Inference | Training | Videos | Citation ...

Example:
```python
import torch
from torchao.quantization import Int4WeightOnlyConfig, quantize
quantize(model, Int4WeightOnlyConfig(group_size=32, int4_packing_format="tile_packed_to_4d", int4_choose_qparams_algorithm="hqq"))
```

...

</details>

### transitions

A lightweight, object-oriented Python state machine implementation with many extensions.

`pip install transitions` · installs (wheel) · licence: MIT License · rank 2786 · last release 2025-07-02 · [PyPI](https://pypi.org/project/transitions/)

<details><summary>README extract</summary>

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

Sections: Quickstart, The non-quickstart, Some key concepts, Basic initialization, States, Callbacks, Checking state, Enumerations, Transitions, Triggering a transition, Triggering invalid transitions, Automatic transitions for all states, Transitioning from multiple states, Reflexive transitions from multiple states

</details>

### trl

Train transformer language models with reinforcement learning.

`pip install trl` · installs (wheel) · licence: Apache-2.0 · rank 2808 · last release 2026-10-30 · [PyPI](https://pypi.org/project/trl/)

<details><summary>README extract</summary>

🔥 Mistral Large 4: Fine-tune Mistral Large 4 with `SFTTrainer` on a single node of 8 B300s, on top of its FP8 weights. See the LoRA example.

🚀 Training on AMD GPUs: TRL's trainers now run on AMD Instinct GPUs through PyTorch's ROCm build.

🔥 Beam: Fine-tune Beam with `SFTTrainer` on a single node of 8 B300s. See the LoRA example. ...

Features:
TRL is a cutting-edge library designed for post-training foundation models using advanced techniques like Supervised Fine-Tuning (SFT), Group Relative Policy Optimization (GRPO), and Direct Preference Optimization (DPO). ...

Example:
```python
from trl import SFTTrainer
from datasets import load_dataset

dataset = load_dataset("trl-lib/Capybara", split="train")

trainer = SFTTrainer(
    model="Qwen/Qwen2.5-0.5B",
    train_dataset=dataset,
)
...

</details>

### types-boto3-cloudformation

Type annotations for boto3 CloudFormation 1.43.110 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-cloudformation` · installs (wheel) · licence: MIT · rank 2848 · last release 2026-10-08 · [PyPI](https://pypi.org/project/types-boto3-cloudformation/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_cloudformation/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CloudFormation 1.43.110 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-cloudformation docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### tokenspeed-mla

Speed-of-light TokenSpeed MLA kernels.

`pip install tokenspeed-mla` · installs (wheel) · licence: not stated · rank 2856 · last release 2026-11-06 · [PyPI](https://pypi.org/project/tokenspeed-mla/) · [source](https://github.com/lightseekorg/tokenspeed)

<details><summary>README extract</summary>

Speed-of-light TokenSpeed MLA kernels for `SM100/SM103/SM107` with:

 - CuTe DSL JIT backend for ragged varlen FMHA (no padding)
 - BF16 output, optional LSE output, causal/non-causal modes, PDL support ...

Example:
```python
import torch
from tokenspeed_mla import tokenspeed_mla_decode

# query: [B, q_len, H, D_qk]
# kv_cache: [num_pages, page_size, D_total]
out = tokenspeed_mla_decode(
    query=query,
    kv_cache=kv_cache,
    workspace_buffer=workspace_buffer,  # torch.int8, 1D
    kv_lora_rank=kv_lora_rank,
    qk_rope_head_dim=qk_rope_head_dim,
...
```

...

</details>

### types-colorama

Typing stubs for colorama

`pip install types-colorama` · installs (wheel) · licence: Apache-2.0 · rank 2864 · last release 2026-05-08 · [PyPI](https://pypi.org/project/types-colorama/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `colorama` package. It can be used by type checkers
to check code that uses `colorama`. This version of
`types-colorama` aims to provide accurate annotations for
`colorama==0.4.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-docker

Typing stubs for docker

`pip install types-docker` · installs (wheel) · licence: Apache-2.0 · rank 2949 · last release 2026-11-02 · [PyPI](https://pypi.org/project/types-docker/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `docker` package. It can be used by type checkers
to check code that uses `docker`. This version of
`types-docker` aims to provide accurate annotations for
`docker==7.2.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

Sections: Typing stubs for docker, Optional dependencies

</details>

### types-aiobotocore-lambda

Type annotations for aiobotocore Lambda 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-lambda` · installs (wheel) · licence: MIT · rank 2996 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-lambda/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### testfixtures

A collection of helpers and mock objects for unit tests and doc tests.

`pip install testfixtures` · installs (wheel) · licence: MIT License · rank 3012 · last release 2026-10-02 · [PyPI](https://pypi.org/project/testfixtures/) · [docs](http://testfixtures.readthedocs.org/en/latest/) · [source](https://github.com/Simplistix/testfixtures)

<details><summary>README extract</summary>

Testfixtures is a collection of helpers and mock objects that are useful when
writing automated tests in Python.

The areas of testing this package can help with are listed below:

Comparing, asserting equality and explaining differences ...

</details>

### types-Flask

Typing stubs for Flask

`pip install types-Flask` · installs (wheel) · licence: Apache Software License · rank 3022 · last release 2021-11-26 · [PyPI](https://pypi.org/project/types-Flask/)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `Flask` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `Flask`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-pyasn1

Typing stubs for pyasn1

`pip install types-pyasn1` · installs (wheel) · licence: Apache-2.0 · rank 3032 · last release 2026-07-24 · [PyPI](https://pypi.org/project/types-pyasn1/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `pyasn1` package. It can be used by type checkers
to check code that uses `pyasn1`. This version of
`types-pyasn1` aims to provide accurate annotations for
`pyasn1==0.6.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-networkx

Typing stubs for networkx

`pip install types-networkx` · installs (wheel) · licence: Apache-2.0 · rank 3056 · last release 2026-11-07 · [PyPI](https://pypi.org/project/types-networkx/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `networkx` package. It can be used by type checkers
to check code that uses `networkx`. This version of
`types-networkx` aims to provide accurate annotations for
`networkx==3.6.1`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

Sections: Typing stubs for networkx, Optional dependencies

</details>

### tantivy

Official Python bindings for the Tantivy search engine

`pip install tantivy` · installs (wheel) · licence: MIT · rank 3086 · last release 2026-10-22 · [PyPI](https://pypi.org/project/tantivy/) · [docs](https://tantivy-py.readthedocs.io/en/latest/) · [source](https://github.com/quickwit-oss/tantivy-py)

<details><summary>README extract</summary>

Python bindings for Tantivy the full-text search engine library written in Rust.

Sections: tantivy-py, Documentation

</details>

### types-chardet

Typing stubs for chardet

`pip install types-chardet` · installs (wheel) · licence: Apache Software License · rank 3099 · last release 2023-05-10 · [PyPI](https://pypi.org/project/types-chardet/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `chardet` package. It
can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`chardet`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### towncrier

Building newsfiles for your project.

`pip install towncrier` · installs (wheel) · licence: MIT · rank 3122 · last release 2026-09-04 · [PyPI](https://pypi.org/project/towncrier/) · [docs](https://towncrier.readthedocs.io/) · [source](https://github.com/twisted/towncrier)

<details><summary>README extract</summary>

`towncrier` is a utility to produce useful, summarized news files (also known as changelogs) for your project.

Rather than reading the Git history, or having one single file which developers all write to and produce merge conflicts, `towncrier` reads "news fragments" which contain information useful to end users. ...

Sections: Hear ye, hear ye, says the `towncrier`, Philosophy, Project Links

</details>

### typst

Python binding to Typst, a new markup-based typesetting system that is powerful and easy to learn.

`pip install typst` · installs (wheel) · licence: not stated · rank 3129 · last release 2026-11-05 · [PyPI](https://pypi.org/project/typst/) · [docs](https://github.com/messense/typst-py/blob/main/README.md) · [source](https://github.com/messense/typst-py)

<details><summary>README extract</summary>

Python binding to typst,
a new markup-based typesetting system that is powerful and easy to learn.

Example:
```python
import datetime
import typst

# Compile `hello.typ` to PDF and save as `hello.pdf`
typst.compile("hello.typ", output="hello.pdf")

# Compile `hello.typ` to PNG and save as `hello.png`
typst.compile("hello.typ", output="hello.png", format="png", ppi=144.0)

# Or pass `hello.typ` content as bytes
with open("hello.typ", "rb") as f:
...
```

Sections: typst-py, Usage, Watch mode, Multi-file projects, Packages, Passing values

</details>

### traceloop-sdk

Traceloop Software Development Kit (SDK) for Python

`pip install traceloop-sdk` · installs (wheel) · licence: Apache-2.0 · rank 3133 · last release 2026-11-05 · [PyPI](https://pypi.org/project/traceloop-sdk/) · [docs](https://traceloop.com/docs/openllmetry) · [source](https://github.com/traceloop/openllmetry)

<details><summary>README extract</summary>

Traceloop’s Python SDK allows you to easily start monitoring and debugging your LLM execution. Tracing is done in a non-intrusive way, built on top of OpenTelemetry. You can choose to export the traces to Traceloop, or to your existing observability stack.

Example:
```python
Traceloop.init(app_name="joke_generation_service")

@workflow(name="joke_creation")
def create_joke():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Tell me a joke about opentelemetry"}],
    )

    return completion.choices[0].message.content
```

</details>

### types-tzlocal

Typing stubs for tzlocal

`pip install types-tzlocal` · installs (wheel) · licence: Apache Software License · rank 3167 · last release 2023-10-24 · [PyPI](https://pypi.org/project/types-tzlocal/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561
type stub package for the `tzlocal` package.
It can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`tzlocal`.

This version of `types-tzlocal` aims to provide accurate annotations
for `tzlocal==5.1`. ...

</details>

### types-aiobotocore-dynamodb

Type annotations for aiobotocore DynamoDB 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-dynamodb` · installs (wheel) · licence: MIT · rank 3195 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-dynamodb/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dynamodb/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### taskiq-redis

Redis integration for taskiq

`pip install taskiq-redis` · installs (wheel) · licence: MIT · rank 3223 · last release 2026-09-28 · [PyPI](https://pypi.org/project/taskiq-redis/) · [source](https://github.com/taskiq-python/taskiq-redis)

<details><summary>README extract</summary>

Taskiq-redis is a plugin for taskiq that adds a new broker and result backend based on redis.

Example:
```python
# broker.py
import asyncio

from taskiq_redis import RedisAsyncResultBackend, RedisStreamBroker

result_backend = RedisAsyncResultBackend(
    redis_url="redis://localhost:6379",
)

# Or you can use PubSubBroker if you need broadcasting
# Or ListQueueBroker if you don't want acknowledges
broker = RedisStreamBroker(
...
```

Sections: TaskIQ-Redis, Usage, Brokers, PubSub, ListQueue, Stream, RedisAsyncResultBackend configuration, Schedule sources, RedisScheduleSource, ListRedisScheduleSource, Migration from one source to another, Dynamic queue names

</details>

### twirp

Twirp server and client lib

`pip install twirp` · installs (wheel) · licence: not stated · rank 3237 · last release 2022-04-24 · [PyPI](https://pypi.org/project/twirp/)

<details><summary>README extract</summary>

Python implementation of Twirp RPC framework (supports Twirp Wire Protocol v7).

This repo contains a protoc plugin that generates sever and client code and a pypi package with common implementation details.

For details about the twirp project, check

Example:
```python
# server.py
import random

from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument

from . import haberdasher_twirp, haberdasher_pb2

class HaberdasherService(object):
    def MakeHat(self, context, size):
        if size.inches <= 0:
...
```

Sections: Twirpy, Generate and run, Server code, Client code, Message Body Length, Standing on the shoulders of giants

</details>

### types-bleach

Typing stubs for bleach

`pip install types-bleach` · installs (wheel) · licence: Apache-2.0 · rank 3242 · last release 2026-07-28 · [PyPI](https://pypi.org/project/types-bleach/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `bleach` package. It can be used by type checkers
to check code that uses `bleach`. This version of
`types-bleach` aims to provide accurate annotations for
`bleach==6.4.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-dateparser

Typing stubs for dateparser

`pip install types-dateparser` · installs (wheel) · licence: Apache-2.0 · rank 3267 · last release 2026-09-07 · [PyPI](https://pypi.org/project/types-dateparser/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `dateparser` package. It can be used by type checkers
to check code that uses `dateparser`. This version of
`types-dateparser` aims to provide accurate annotations for
`dateparser==1.4.3`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tensordict

A dict[str, torch.Tensor] that behaves like one tensor.

`pip install tensordict` · installs (wheel) · licence: MIT · rank 3276 · last release 2026-11-05 · [PyPI](https://pypi.org/project/tensordict/) · [docs](https://docs.pytorch.org/tensordict/stable/)

<details><summary>README extract</summary>

A `dict[str, torch.Tensor]` that behaves like one tensor.

PyTorch code that handles groups of tensors, such as a training batch, a
particle system, or a batch of graphs, usually repeats every operation for
every tensor, and nested dicts need recursion. A TensorDict holds the group as
one object: ...

Example:
```python
import torch
from tensordict import TensorDict, lazy_stack

episodes = [TensorDict({"obs": torch.randn(n, 4)}, batch_size=[n]) for n in (3, 5, 2)]
batch = lazy_stack(episodes)      # keeps each sample as it is
print(batch.batch_size)           # torch.Size([3, -1]): -1 marks the dimension that varies
print(batch1.shape)      # torch.Size([5, 4])
...
```

Sections: TensorDict, More examples, FAQ, Documentation

</details>

### types-boto3-iam

Type annotations for boto3 IAM 1.43.70 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-iam` · installs (wheel) · licence: MIT · rank 3349 · last release 2026-08-12 · [PyPI](https://pypi.org/project/types-boto3-iam/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_iam/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 IAM 1.43.70
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-iam docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-aiobotocore-secretsmanager

Type annotations for aiobotocore SecretsManager 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-secretsmanager` · installs (wheel) · licence: MIT · rank 3373 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-secretsmanager/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_secretsmanager/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-passlib

Typing stubs for passlib

`pip install types-passlib` · installs (wheel) · licence: Apache-2.0 · rank 3374 · last release 2026-02-10 · [PyPI](https://pypi.org/project/types-passlib/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `passlib` package. It can be used by type checkers
to check code that uses `passlib`. This version of
`types-passlib` aims to provide accurate annotations for
`passlib==1.7.*`.

*Note:* `types-passlib` is unmaintained and won't be updated.

This package is part of the typeshed project. ...

</details>

### types-aiobotocore-sts

Type annotations for aiobotocore STS 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-sts` · installs (wheel) · licence: MIT · rank 3396 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-sts/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sts/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Literals

</details>

### types-boto3-sesv2

Type annotations for boto3 SESV2 1.43.110 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-sesv2` · installs (wheel) · licence: MIT · rank 3400 · last release 2026-10-08 · [PyPI](https://pypi.org/project/types-boto3-sesv2/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_sesv2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SESV2 1.43.110
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-sesv2 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### taskgroup

backport of asyncio.TaskGroup, asyncio.Runner and asyncio.timeout

`pip install taskgroup` · installs (wheel) · licence: MIT License · rank 3405 · last release 2025-01-03 · [PyPI](https://pypi.org/project/taskgroup/)

<details><summary>README extract</summary>

a backport of asyncio.TaskGroup, asyncio.Runner and asyncio.timeout

This is a backport of the TaskGroup, Runner and timeout code from
Python 3.12.8 to Python 3.8, Python 3.9, Python 3.10 and Python 3.11. ...

Example:
```python
if sys.python_version >= (3, 11):
    from asyncio import run, TaskGroup, timeout
else:
    from taskgroup import run, TaskGroup, timeout

async def main():
    async with TaskGroup() as group:
        group.create_task(task1())
        group.create_task(task2())

run(main())
```

Sections: taskgroup, background, operation, example, 0.2.2, What's Changed, 0.2.1, 0.2.0, 0.1.1, 0.1.0

</details>

### torch-geometric

Graph Neural Network Library for PyTorch

`pip install torch-geometric` · installs (wheel) · licence: MIT · rank 3469 · last release 2026-10-12 · [PyPI](https://pypi.org/project/torch-geometric/) · [docs](https://pytorch-geometric.readthedocs.io) · [source](https://github.com/pyg-team/pytorch_geometric.git)

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

### types-python-jose

Typing stubs for python-jose

`pip install types-python-jose` · installs (wheel) · licence: Apache-2.0 · rank 3474 · last release 2026-04-08 · [PyPI](https://pypi.org/project/types-python-jose/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `python-jose` package. It can be used by type checkers
to check code that uses `python-jose`. This version of
`types-python-jose` aims to provide accurate annotations for
`python-jose==3.5.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tensorboard-plugin-wit

What-If Tool TensorBoard plugin.

`pip install tensorboard-plugin-wit` · installs (wheel) · licence: Apache 2.0 · rank 3485 · last release 2022-01-05 · [PyPI](https://pypi.org/project/tensorboard-plugin-wit/)

<details><summary>README extract</summary>

The tensorboard-plugin-wit package adds the What-If Tool
to the standard distribution of the TensorBoard toolkit, as a plugin.

The What-If Tool is an interactive visual probe for ML model understanding.

The source code for the plugin, and the entire What-If Tool, can be found at ...

</details>

### textparser

A text parser library for python.

`pip install textparser` · installs (wheel) · licence: MIT · rank 3492 · last release 2026-06-20 · [PyPI](https://pypi.org/project/textparser/) · [docs](https://textparser.readthedocs.io/) · [source](https://github.com/cantools/textparser)

<details><summary>README extract</summary>

A text parser written in the Python language.

The project has one goal, speed! See the benchmark below more details.

Project homepage:

Documentation:

Example:
```python
import textparser
from textparser import Sequence

class Parser(textparser.Parser):

    def token_specs(self):
        return [
            ('SKIP',          r'[ \r\n\t]+'),
            ('WORD',          r'\w+'),
            ('EMARK',    '!', r'!'),
            ('COMMA',    ',', r','),
            ('MISMATCH',      r'.')
        ]

...
```

Sections: About, Example usage, Benchmark, . Fork the repository., . Implement the new feature or bug fix., . Run the tests., . Create a pull request.

</details>

### types-emoji

Typing stubs for emoji

`pip install types-emoji` · installs (wheel) · licence: Apache Software License · rank 3532 · last release 2023-03-27 · [PyPI](https://pypi.org/project/types-emoji/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `emoji` package. It
can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`emoji`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-xmltodict

Typing stubs for xmltodict

`pip install types-xmltodict` · installs (wheel) · licence: Apache-2.0 · rank 3572 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-xmltodict/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `xmltodict` package. It can be used by type checkers
to check code that uses `xmltodict`. This version of
`types-xmltodict` aims to provide accurate annotations for
`xmltodict~=1.0.1`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-boto

Typing stubs for boto

`pip install types-boto` · installs (wheel) · licence: Apache Software License · rank 3573 · last release 2024-10-19 · [PyPI](https://pypi.org/project/types-boto/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561
type stub package for the `boto` package.
It can be used by type-checking tools like
mypy,
pyright,
pytype,
Pyre,
PyCharm, etc. to check code that uses `boto`. This version of
`types-boto` aims to provide accurate annotations for
`boto==2.49.*`.

*Note:* `types-boto` is unmaintained and won't be updated. ...

</details>

### types-oauthlib

Typing stubs for oauthlib

`pip install types-oauthlib` · installs (wheel) · licence: Apache-2.0 · rank 3596 · last release 2026-11-07 · [PyPI](https://pypi.org/project/types-oauthlib/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `oauthlib` package. It can be used by type checkers
to check code that uses `oauthlib`. This version of
`types-oauthlib` aims to provide accurate annotations for
`oauthlib==4.0.0`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-aiobotocore-ec2

Type annotations for aiobotocore EC2 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-ec2` · installs (wheel) · licence: MIT · rank 3597 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-ec2/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### torch-pitch-shift

(no summary)

`pip install torch-pitch-shift` · installs (wheel) · licence: MIT License · rank 3617 · last release 2024-09-25 · [PyPI](https://pypi.org/project/torch-pitch-shift/)

<details><summary>README extract</summary>

Pitch-shift audio clips quickly with PyTorch (CUDA supported)! Additional utilities for searching efficient transformations are included.

View on PyPI / View Documentation

This package includes two main features:
* Pitch-shift audio clips quickly using PyTorch (with CUDA support)
* Calculate efficient pitch-shift targets (useful for ...

Sections: Torch Pitch Shift, About, Usage, Example, Documentation

</details>

### types-termcolor

Typing stubs for termcolor

`pip install types-termcolor` · installs (wheel) · licence: Apache Software License · rank 3668 · last release 2023-03-28 · [PyPI](https://pypi.org/project/types-termcolor/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `termcolor` package. It
can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`termcolor`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-cryptography

Typing stubs for cryptography

`pip install types-cryptography` · installs (wheel) · licence: Apache Software License · rank 3692 · last release 2022-11-08 · [PyPI](https://pypi.org/project/types-cryptography/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `cryptography` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `cryptography`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-aiobotocore-sns

Type annotations for aiobotocore SNS 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-sns` · installs (wheel) · licence: MIT · rank 3714 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-sns/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sns/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-enum34

Typing stubs for enum34

`pip install types-enum34` · installs (wheel) · licence: Apache Software License · rank 3721 · last release 2022-01-20 · [PyPI](https://pypi.org/project/types-enum34/)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `enum34` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `enum34`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there.

See for more details. ...

</details>

### torchsde

SDE solvers and stochastic adjoint sensitivity analysis in PyTorch.

`pip install torchsde` · installs (wheel) · licence: Apache Software License · rank 3740 · last release 2023-09-26 · [PyPI](https://pypi.org/project/torchsde/)

<details><summary>README extract</summary>

This library provides stochastic differential equation (SDE) solvers with GPU support and efficient backpropagation.

Example:
```python
import torch
import torchsde

batch_size, state_size, brownian_size = 32, 3, 2
t_size = 20

class SDE(torch.nn.Module):
    noise_type = 'general'
    sde_type = 'ito'

    def init(self):
        super().init()
        self.mu = torch.nn.Linear(state_size,
                                  state_size)
...
```

Sections: PyTorch Implementation of Differentiable SDE Solvers, Documentation, Examples, Quick example, Notebook, Latent SDE, Neural SDEs as GANs, References

</details>

### trampoline

Simple and tiny yield-based trampoline implementation.

`pip install trampoline` · installs (wheel) · licence: MIT License · rank 3761 · last release 2018-08-18 · [PyPI](https://pypi.org/project/trampoline/)

<details><summary>README extract</summary>

This trampoline allows recursive functions to recurse virtually (or literally)
infinitely. Most existing recursive functions can be converted with simple
modifications.

The implementation is tiny: the gist of the module consists of a single
function with around 30 lines of simple python code. ...

Example:
```python
raise TailCall(...)
yield
```

Sections: trampoline - unlimited recursion, Conversion from simple recursion, Return values, Exceptions, Tail Calls, Suggestions, Expose a wrapper, Use it in classes, Caveats, Yield, Memory consumption, Performance, Tracebacks

</details>

### tqdm-loggable

TQDM progress bar helpers for logging and other headless application

`pip install tqdm-loggable` · installs (wheel) · licence: MIT License · rank 3781 · last release 2026-03-16 · [PyPI](https://pypi.org/project/tqdm-loggable/) · [source](https://github.com/tradingstrategy-ai/tqdm-loggable)

<details><summary>README extract</summary>

`tqdm-loggable` is a petite Python package providing logging-friendly TQDM progress bars.

If your Python application has tqdm progress bars and you use them in a non-interactive session like...

- Background worker
- Docker container
- Edge computing
- Logstash, Sentry, Datadog or other external log tools
- Long-running machine learning tasks ...

Example:
```python
from tqdm import tqdm -> from tqdm_loggable.auto import tqdm
from tqdm.auto import tqdm -> from tqdm_loggable.auto import tqdm
```

</details>

### types-futures

Typing stubs for futures

`pip install types-futures` · installs (wheel) · licence: Apache Software License · rank 3805 · last release 2022-01-27 · [PyPI](https://pypi.org/project/types-futures/)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `futures` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `futures`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there.

See for more details. ...

</details>

### typesense

Python client for Typesense, an open source and typo tolerant search engine.

`pip install typesense` · installs (wheel) · licence: Apache Software License · rank 3807 · last release 2026-10-23 · [PyPI](https://pypi.org/project/typesense/) · [docs](https://typesense.org/) · [source](https://github.com/typesense/typesense-python)

<details><summary>README extract</summary>

Python client for the Typesense API:

Example:
```python
import asyncio
import typesense

async def main() -> None:
    client = typesense.AsyncClient({
        "api_key": "abcd",
        "nodes": [{"host": "localhost", "port": "8108", "protocol": "http"}],
        "connection_timeout_seconds": 2,
    })

    print(await client.collections.retrieve())
    await client.api_call.aclose()

...
```

Sections: Typesense Python Client, Usage, Async usage, Using httpx2, Compatibility

</details>

### types-aiobotocore-bedrock-runtime

Type annotations for aiobotocore BedrockRuntime 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-bedrock-runtime` · installs (wheel) · licence: MIT · rank 3827 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-bedrock-runtime/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_runtime/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-reportlab

Typing stubs for reportlab

`pip install types-reportlab` · installs (wheel) · licence: Apache-2.0 · rank 3839 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-reportlab/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `reportlab` package. It can be used by type checkers
to check code that uses `reportlab`. This version of
`types-reportlab` aims to provide accurate annotations for
`reportlab==5.1.0`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### trustcall

Tenacious & trustworthy tool calling built on LangGraph.

`pip install trustcall` · installs (wheel) · licence: MIT · rank 3932 · last release 2025-04-14 · [PyPI](https://pypi.org/project/trustcall/)

<details><summary>README extract</summary>

LLMs struggle when asked to generate or modify large JSON blobs. `trustcall` solves this by asking the LLM to generate JSON patch operations. This is a simpler task that can be done iteratively. This enables:

- ⚡ Faster & cheaper generation of structured output. ...

Features:
Tool calling makes it easier to compose LLM calls within reliable software systems, but LLM's today can be error prone and inefficient in two common scenarios:

1. Populating complex, nested schemas
2. ...

Example:
```python
from typing import List

from langchain_fireworks import ChatFireworks
from pydantic.v1 import BaseModel, Field, validator
from trustcall import create_extractor

class Preferences(BaseModel):
    foods: List[str] = Field(description="Favorite foods")

    @validator("foods")
...

</details>

### telesign

TeleSign SDK

`pip install telesign` · installs (wheel) · licence: MIT License · rank 3957 · last release 2026-10-01 · [PyPI](https://pypi.org/project/telesign/)

<details><summary>README extract</summary>

TeleSign is a communications platform as a service (CPaaS) company, founded on security. Since 2005, TeleSign has
been a trusted partner to the world’s leading websites and mobile applications, helping secure billions of end-user
accounts. ...

Example:
```python
from future import print_function
from telesign.messaging import MessagingClient

customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

phone_number = "phone_number"
message = "You're scheduled for a dentist appointment at 2:30PM."
...
```

Sections: TeleSign Python SDK, Documentation, Authentication, Dependencies, Python Code Example: Messaging

</details>

### telesignenterprise

Telesign Enterprise SDK

`pip install telesignenterprise` · installs (wheel) · licence: MIT License · rank 3969 · last release 2026-07-22 · [PyPI](https://pypi.org/project/telesignenterprise/)

### tentaclio

Unification of data connectors for distributed data tasks

`pip install tentaclio` · installs (wheel) · licence: MIT · rank 3977 · last release 2026-10-23 · [PyPI](https://pypi.org/project/tentaclio/) · [source](https://github.com/octopus-energy/tentaclio)

<details><summary>README extract</summary>

Python library that simplifies:
* Handling streams from different protocols such as `file:`, `ftp:`, `sftp:`, `s3:`, ...
* Opening database connections.
* Managing the credentials in distributed systems.

Main considerations in the design:
* Easy to use: all streams are open via `tentaclio.open`, all database connections through `tentaclio.db`. ...

Example:
```python
import tentaclio
contents = "👋 🐙"

with tentaclio.open("ftp://localhost:2021/upload/file.txt", mode="w") as writer:
    writer.write(contents)

# Using boto3 authentication under the hood.
bucket = "s3://my-bucket/octopus/hello.txt"
with tentaclio.open(bucket) as reader:
    print(reader.read())
```

...

</details>

### types-greenlet

Typing stubs for greenlet

`pip install types-greenlet` · installs (wheel) · licence: Apache-2.0 · rank 4001 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-greenlet/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `greenlet` package. It can be used by type checkers
to check code that uses `greenlet`. This version of
`types-greenlet` aims to provide accurate annotations for
`greenlet==3.5.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-aiobotocore-rds

Type annotations for aiobotocore RDS 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-rds` · installs (wheel) · licence: MIT · rank 4094 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-rds/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rds/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-aiobotocore-ssm

Type annotations for aiobotocore SSM 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-ssm` · installs (wheel) · licence: MIT · rank 4100 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-ssm/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-stripe

Typing stubs for stripe

`pip install types-stripe` · installs (wheel) · licence: Apache Software License · rank 4104 · last release 2024-01-06 · [PyPI](https://pypi.org/project/types-stripe/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561
type stub package for the `stripe` package.
It can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`stripe`.

This version of `types-stripe` aims to provide accurate annotations
for `stripe==3.5.*`. ...

</details>

### tentaclio-s3

A python project containing all the dependencies for schema s3 for tentaclio.

`pip install tentaclio-s3` · installs (wheel) · licence: MIT · rank 4114 · last release 2026-10-26 · [PyPI](https://pypi.org/project/tentaclio-s3/)

<details><summary>README extract</summary>

A package containing all the dependencies for the s3 tentaclio schema .

Sections: tentaclio-s3, Quick Start

</details>

### types-aiobotocore-ecs

Type annotations for aiobotocore ECS 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-ecs` · installs (wheel) · licence: MIT · rank 4145 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-ecs/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ecs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### typing-utils

utils to inspect Python type annotations

`pip install typing-utils` · installs (wheel) · licence: Apache License 2.0 · rank 4186 · last release 2021-05-23 · [PyPI](https://pypi.org/project/typing-utils/)

<details><summary>README extract</summary>

Backport Python3.8+ typing utils &amp; issubtype &amp; more

- Install
- API
 - issubtype
 - get_origin
 - get_args
 - get_type_hints

Example:
```python
from typing_utils import issubtype

issubtype(typing.List, typing.Any) == True
issubtype(list, list) == True
issubtype(list, typing.List) == True
issubtype(list, typing.Sequence) == True
issubtype(typing.List[int], list) == True
issubtype(typing.List[typing.List], list) == True
issubtype(list, typing.List[int]) == False
...
```

Sections: typing-utils, API, issubtype, get_origin, get_args, get_type_hints

</details>

### types-xlrd

Typing stubs for xlrd

`pip install types-xlrd` · installs (wheel) · licence: Apache-2.0 · rank 4192 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-xlrd/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `xlrd` package. It can be used by type checkers
to check code that uses `xlrd`. This version of
`types-xlrd` aims to provide accurate annotations for
`xlrd==2.0.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

</details>

### types-pyserial

Typing stubs for pyserial

`pip install types-pyserial` · installs (wheel) · licence: Apache-2.0 · rank 4219 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-pyserial/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `pyserial` package. It can be used by type checkers
to check code that uses `pyserial`. This version of
`types-pyserial` aims to provide accurate annotations for
`pyserial==3.5.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-shapely

Typing stubs for shapely

`pip install types-shapely` · installs (wheel) · licence: Apache-2.0 · rank 4243 · last release 2026-10-30 · [PyPI](https://pypi.org/project/types-shapely/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `shapely` package. It can be used by type checkers
to check code that uses `shapely`. This version of
`types-shapely` aims to provide accurate annotations for
`shapely==2.1.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### typish

Functionality for types

`pip install typish` · installs (wheel) · licence: MIT License · rank 4292 · last release 2021-08-05 · [PyPI](https://pypi.org/project/typish/)

<details><summary>README extract</summary>

* Functions for thorough checks on types
* Instance checks considering generics
* Typesafe Duck-typing

Example:
```python
>>> from typing import Iterable
>>> from typish import instance_of
>>> instance_of([1, 2, 3], Iterable[int])
True
```

Sections: Typish, Example, Content, Functions, Types, Decorators, hintable, Classes, SubscriptableType, Something, ClsDict, ClsFunction, Literal

</details>

### types-PySocks

Typing stubs for PySocks

`pip install types-PySocks` · installs (wheel) · licence: Apache-2.0 · rank 4319 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-PySocks/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `PySocks` package. It can be used by type checkers
to check code that uses `PySocks`. This version of
`types-PySocks` aims to provide accurate annotations for
`PySocks==1.7.1`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-aiobotocore-cloudformation

Type annotations for aiobotocore CloudFormation 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-cloudformation` · installs (wheel) · licence: MIT · rank 4359 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-cloudformation/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-aiobotocore-stepfunctions

Type annotations for aiobotocore SFN 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-stepfunctions` · installs (wheel) · licence: MIT · rank 4376 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-stepfunctions/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_stepfunctions/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### tecton

Tecton Python SDK

`pip install tecton` · installs (wheel) · licence: Other/Proprietary License · rank 4420 · last release 2025-12-05 · [PyPI](https://pypi.org/project/tecton/) · [docs](https://docs.tecton.ai)

<details><summary>README extract</summary>

Tecton is the fastest way to build operational machine learning applications. It helps automate real-time decision making like fraud detection, product recommendations, and search result ranking in production applications. ...

</details>

### textual-serve

Turn your Textual TUIs in to web applications

`pip install textual-serve` · installs (wheel) · licence: MIT License · rank 4423 · last release 2025-11-01 · [PyPI](https://pypi.org/project/textual-serve/)

<details><summary>README extract</summary>

Every Textual application is now a web application.

With 3 lines of code, any Textual app can run in the browser.

 This is Posting running in the terminal.

 This is Posting running in the browser.

Example:
```python
from textual_serve.server import Server
```

Sections: textual-serve, Getting Started, Creating a server, Summary, Configuration, How does it work?, See also

</details>

### types-factory-boy

Typing stubs for factory-boy

`pip install types-factory-boy` · installs (wheel) · licence: MIT License · rank 4426 · last release 2023-03-12 · [PyPI](https://pypi.org/project/types-factory-boy/) · [source](https://github.com/youtux/types-factory-boy)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `factory-boy` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `factory-boy`.

</details>

### types-decorator

Typing stubs for decorator

`pip install types-decorator` · installs (wheel) · licence: Apache-2.0 · rank 4440 · last release 2026-07-12 · [PyPI](https://pypi.org/project/types-decorator/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `decorator` package. It can be used by type checkers
to check code that uses `decorator`. This version of
`types-decorator` aims to provide accurate annotations for
`decorator==5.2.*`.

*Note:* The `decorator` package includes type annotations or type stubs
since version 5.3.0. ...

</details>

### tuspyserver

A Python tus server implementation as a FastAPI router

`pip install tuspyserver` · installs (wheel) · licence: MIT · rank 4483 · last release 2026-10-23 · [PyPI](https://pypi.org/project/tuspyserver/)

<details><summary>README extract</summary>

A FastAPI router implementing a tus upload protocol server, with optional dependency-injected hooks for post-upload processing.

Only depends on `fastapi>=0.110` and `python>=3.8`.

Features:
* ⏸️ Resumable uploads via TUS protocol
* 🍰 Chunked transfer with configurable max size
* 🗃️ Metadata storage (filename, filetype)
* 🧹 Expiration & cleanup of old uploads (default retention: 5 days)
* 💉 Dependency injection for seamless validation ...

Example:
```python
from tuspyserver import create_tus_router

tus_router = create_tus_router(
    prefix="files",                                   # route prefix (default: 'files')
    files_dir="/tmp/files",                  # path to store files
    max_size=128_849_018_880,             # max upload size in bytes (default is ~128GB)
...
```

...

</details>

### trafaret

Validation and parsing library

`pip install trafaret` · installs (wheel) · licence: BSD License · rank 4487 · last release 2022-04-01 · [PyPI](https://pypi.org/project/trafaret/)

<details><summary>README extract</summary>

Ultimate transformation library that supports validation, contexts and `aiohttp`.

Trafaret is rigid and powerful lib to work with foreign data, configs etc.
It provides simple way to check anything, and convert it accordingly to your needs.

It has shortcut syntax and ability to express anything that you can code: ...

Example:
```python
>>> from trafaret.constructor import construct
>>> validator = construct({'a': int, 'b': [str]})
>>> validator({'a': 5, 'b': ['lorem', 'ipsum']})
{'a': 5, 'b': ['lorem', 'ipsum']}

>>> validator({'a': 5, 'b': ['gorky', 9]})
Traceback (most recent call last):
  File "<console>", line 1, in <module>
...
```

Sections: Trafaret, New, 2.0.2, 2.0.0, 1.x.x, Doc, Related projects

</details>

### types-pexpect

Typing stubs for pexpect

`pip install types-pexpect` · installs (wheel) · licence: Apache-2.0 · rank 4521 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-pexpect/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `pexpect` package. It can be used by type checkers
to check code that uses `pexpect`. This version of
`types-pexpect` aims to provide accurate annotations for
`pexpect==4.9.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tableauhyperapi

Hyper API for Python

`pip install tableauhyperapi` · installs (wheel) · licence: Apache Software License · rank 4538 · last release 2026-10-17 · [PyPI](https://pypi.org/project/tableauhyperapi/)

<details><summary>README extract</summary>

The Hyper API contains a set of functions you can use to automate your interactions with Tableau extract (.hyper) files. You can use the API to create new extract files, or to open existing files, and then insert, delete, update, or read data from those files.

Using the Hyper API developers and administrators can: ...

</details>

### types-boto3-sts

Type annotations for boto3 STS 1.43.94 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-sts` · installs (wheel) · licence: MIT · rank 4546 · last release 2026-09-14 · [PyPI](https://pypi.org/project/types-boto3-sts/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_sts/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 STS 1.43.94
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-sts docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### troposphere

AWS CloudFormation creation library

`pip install troposphere` · installs (wheel) · licence: BSD-2-Clause · rank 4557 · last release 2026-10-20 · [PyPI](https://pypi.org/project/troposphere/) · [source](https://github.com/cloudtools/troposphere)

<details><summary>README extract</summary>

troposphere - library to create AWS CloudFormation descriptions

The troposphere library allows for easier creation of the AWS CloudFormation
JSON by writing Python code to describe the AWS resources. troposphere also
includes some basic support for OpenStack resources via Heat. ...

Example:
```python
>>> from troposphere import Ref, Template
>>> import troposphere.ec2 as ec2
>>> t = Template()
>>> instance = ec2.Instance("myinstance")
>>> instance.ImageId = "ami-951945d0"
>>> instance.InstanceType = "t1.micro"
>>> t.add_resource(instance)
<troposphere.ec2.Instance object at 0x101bf3390>
>>> print(t.to_json())
{
    "Resources": {
...
```

Sections: troposphere, About, Examples, Duplicating a single instance sample would look like this, Licensing

</details>

### types-boto3-full

All-in-one type annotations for boto3 1.43.126 generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-full` · installs (wheel) · licence: MIT · rank 4562 · last release 2026-11-07 · [PyPI](https://pypi.org/project/types-boto3-full/) · [docs](https://youtype.github.io/types_boto3_docs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 1.43.126
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-full docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### taskcluster-urls

Standardized url generator for taskcluster resources.

`pip install taskcluster-urls` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 4587 · last release 2026-08-26 · [PyPI](https://pypi.org/project/taskcluster-urls/)

<details><summary>README extract</summary>

A simple library to generate URLs for various Taskcluster resources across our various deployment methods.

This serves as both a simple shim for projects that use JavaScript but also is the reference implementation for
how we define these paths.

URLs are defined in the 'Taskcluster URL Format.

Changelog

View the changelog on the releases page. ...

Example:
```python
import taskcluster_urls

taskcluster_urls.api(root_url, 'auth', 'v1', 'foo/bar')
taskcluster_urls.schema(root_url, 'auth', 'v1/foo.yml') # Note that schema names have versions in them
taskcluster_urls.api_manifest_schema(root_url, 'v1')
taskcluster_urls.api_reference_schema(root_url, 'v1')
...
```

Sections: Taskcluster URL Building Library, Node / npm, Go, Python / PyPI, Java / Maven

</details>

### types-boto3-kms

Type annotations for boto3 KMS 1.43.119 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-kms` · installs (wheel) · licence: MIT · rank 4609 · last release 2026-10-26 · [PyPI](https://pypi.org/project/types-boto3-kms/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_kms/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 KMS 1.43.119
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-kms docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-boto3-secretsmanager

Type annotations for boto3 SecretsManager 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-secretsmanager` · installs (wheel) · licence: MIT · rank 4620 · last release 2026-04-29 · [PyPI](https://pypi.org/project/types-boto3-secretsmanager/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_secretsmanager/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 SecretsManager 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-secretsmanager docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### ta

Technical Analysis Library in Python

`pip install ta` · installs from source (sdist only) · licence: MIT License · rank 4626 · last release 2023-11-02 · [PyPI](https://pypi.org/project/ta/)

<details><summary>README extract</summary>

It is a Technical Analysis library to financial time series datasets. You can use to do feature engineering. It is built on Python Pandas library.

</details>

### torch-memory-saver

(no summary)

`pip install torch-memory-saver` · installs (wheel) · licence: not stated · rank 4635 · last release 2026-09-12 · [PyPI](https://pypi.org/project/torch-memory-saver/)

### tencentcloud-sdk-python-common

Tencent Cloud Common SDK for Python

`pip install tencentcloud-sdk-python-common` · installs (wheel) · licence: Apache Software License · rank 4638 · last release 2026-11-06 · [PyPI](https://pypi.org/project/tencentcloud-sdk-python-common/)

<details><summary>README extract</summary>

Tencent Cloud Python Common SDK is the official software development kit, which allows Python developers to write software that makes use of Tencent Cloud services like CVM and CBS.
The SDK works on Python versions:

 * 2.7 and greater, including 3.x

Sections: Tencent Cloud SDK for Python, Quick Start

</details>

### types-gevent

Typing stubs for gevent

`pip install types-gevent` · installs (wheel) · licence: Apache-2.0 · rank 4653 · last release 2026-11-07 · [PyPI](https://pypi.org/project/types-gevent/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `gevent` package. It can be used by type checkers
to check code that uses `gevent`. This version of
`types-gevent` aims to provide accurate annotations for
`gevent==26.9.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-aiobotocore-ecr

Type annotations for aiobotocore ECR 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-ecr` · installs (wheel) · licence: MIT · rank 4714 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-ecr/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ecr/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-aiobotocore-athena

Type annotations for aiobotocore Athena 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-athena` · installs (wheel) · licence: MIT · rank 4730 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-athena/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-aiobotocore-scheduler

Type annotations for aiobotocore EventBridgeScheduler 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-scheduler` · installs (wheel) · licence: MIT · rank 4772 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-scheduler/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_scheduler/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-pycurl

Typing stubs for pycurl

`pip install types-pycurl` · installs (wheel) · licence: Apache-2.0 · rank 4796 · last release 2026-10-30 · [PyPI](https://pypi.org/project/types-pycurl/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `pycurl` package. It can be used by type checkers
to check code that uses `pycurl`. This version of
`types-pycurl` aims to provide accurate annotations for
`pycurl==7.49.0`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### traittypes

Scipy trait types

`pip install traittypes` · installs (wheel) · licence: BSD License · rank 4844 · last release 2025-10-22 · [PyPI](https://pypi.org/project/traittypes/)

### types-jmespath

Typing stubs for jmespath

`pip install types-jmespath` · installs (wheel) · licence: Apache-2.0 · rank 4868 · last release 2026-07-24 · [PyPI](https://pypi.org/project/types-jmespath/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `jmespath` package. It can be used by type checkers
to check code that uses `jmespath`. This version of
`types-jmespath` aims to provide accurate annotations for
`jmespath==1.1.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### threejs-materials

Download PBR materials on demand and convert to Three.js MeshPhysicalMaterial JSON

`pip install threejs-materials` · installs (wheel) · licence: Apache-2.0 · rank 4872 · last release 2026-10-15 · [PyPI](https://pypi.org/project/threejs-materials/) · [source](https://github.com/bernhard-42/threejs-materials)

<details><summary>README extract</summary>

A Python library that converts PBR materials into Three.js `MeshPhysicalMaterial`-compatible JSON. Textures are stored as separate files on disk and only base64-encoded when sending to the viewer.

Uses pygltflib for standard glTF 2.0 file I/O (`.gltf` and `.glb`).

Supported input formats: ...

Example:
```python
from threejs_materials import wood, metal, glass

wood.ash()
metal.gold_brushed()
```

Sections: threejs-materials, Bundled materials, `plastic_fdm` — printed layer lines, Composing beyond the exposed parameters, Input Formats, 1 Blender glTF exports, Format mapping glTF → internal, Limitations, 2 MaterialX, Shader model coverage, MaterialX limitations, Output Formats, 1 Three.js (internal format), 2 glTF

</details>

### torchdiffeq

ODE solvers and adjoint sensitivity analysis in PyTorch.

`pip install torchdiffeq` · installs (wheel) · licence: MIT License · rank 4873 · last release 2024-11-21 · [PyPI](https://pypi.org/project/torchdiffeq/)

### tempora

(no summary)

`pip install tempora` · installs (wheel) · licence: not stated · rank 4906 · last release 2026-10-01 · [PyPI](https://pypi.org/project/tempora/) · [source](https://github.com/jaraco/tempora)

<details><summary>README extract</summary>

Objects and routines pertaining to date and time (tempora).

Modules include:

- tempora (top level package module) contains miscellaneous
 utilities and constants.
- timing contains routines for measuring and profiling.
- schedule contains an event scheduler.
- utc contains routines for getting datetime-aware UTC values.

</details>

### types-auth0-python

Typing stubs for auth0-python

`pip install types-auth0-python` · installs (wheel) · licence: Apache-2.0 · rank 4981 · last release 2026-11-02 · [PyPI](https://pypi.org/project/types-auth0-python/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `auth0-python` package. It can be used by type checkers
to check code that uses `auth0-python`. This version of
`types-auth0-python` aims to provide accurate annotations for
`auth0-python==4.10.*`.

*Note:* The `auth0-python` package includes type annotations or type stubs
since version 5.4.0. ...

</details>

### types-qrcode

Typing stubs for qrcode

`pip install types-qrcode` · installs (wheel) · licence: Apache-2.0 · rank 5012 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-qrcode/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `qrcode` package. It can be used by type checkers
to check code that uses `qrcode`. This version of
`types-qrcode` aims to provide accurate annotations for
`qrcode==8.2.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### typeid-python

Python implementation of TypeIDs: type-safe, K-sortable, and globally unique identifiers inspired by Stripe IDs

`pip install typeid-python` · installs (wheel) · licence: MIT License · rank 5023 · last release 2026-10-26 · [PyPI](https://pypi.org/project/typeid-python/) · [source](https://github.com/akhundMurad/typeid-python)

<details><summary>README extract</summary>

> [!WARNING]
> `main` may contain unreleased changes. For stable usage, use the latest release tag.

A high-performance Python implementation of TypeIDs — type-safe,
sortable identifiers based on UUIDv7.

TypeIDs are designed for modern systems where identifiers should be:

- globally unique
- sortable by creation time ...

Features:
- ✅ UUIDv7-based, time-sortable identifiers
- ✅ Schema-based ID explanations (JSON / YAML)
- ✅ Fast generation & parsing (Rust-accelerated)
- ✅ Multiple integrations (Pydantic, FastAPI, ...)
- ✅ Type-safe prefixes (`user`, `order`, ...) ...

Example:
```python
from typeid import TypeID

tid = TypeID(prefix="user")

assert tid.prefix == "user"
assert isinstance(tid.suffix, str)
assert str(tid).startswith("user")
```

...

</details>

### test-results-parser

(no summary)

`pip install test-results-parser` · installs (wheel) · licence: not stated · rank 5150 · last release 2025-11-17 · [PyPI](https://pypi.org/project/test-results-parser/)

### tokamax

A Pallas Custom Kernel Library.

`pip install tokamax` · installs (wheel) · licence: not stated · rank 5171 · last release 2026-10-20 · [PyPI](https://pypi.org/project/tokamax/)

<details><summary>README extract</summary>

Tokamax is a library of custom accelerator kernels. It provides highly optimized
implementations of key operators, including mixture-of-experts building blocks
like grouped matrix multiplication and token gathers/scatters, attention
variants like paged attention, splash attention, gated deltanet, Kimi delta
attention and multiheaded latent ...

Sections: Tokamax, Documentation, Getting Started, Usage Examples

</details>

### torch-stoi

Computes Short Term Objective Intelligibility in PyTorch

`pip install torch-stoi` · installs (wheel) · licence: MIT License · rank 5234 · last release 2024-09-30 · [PyPI](https://pypi.org/project/torch-stoi/)

<details><summary>README extract</summary>

[][travis]

Implementation of the classical and extended Short
Term Objective Intelligibility in PyTorch.
See also Cees Taal's website and
the python implementation

Example:
```python
import torch
from torch import nn
from torch_stoi import NegSTOILoss

sample_rate = 16000
loss_func = NegSTOILoss(sample_rate=sample_rate)
# Your nnet and optimizer definition here
nnet = nn.Module()

noisy_speech = torch.randn(2, 16000)
clean_speech = torch.randn(2, 16000)
# Estimate clean speech
est_speech = nnet(noisy_speech)
...
```

Sections: PyTorch implementation of STOI, Important warning, Usage, Comparing NumPy and PyTorch versions : the static test, 8kHz, 16kHz, Comparing NumPy and PyTorch versions : Training a DNN, References

</details>

### types-sqlalchemy-utils

Type Stubs for sqlalchemy-utils

`pip install types-sqlalchemy-utils` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 5262 · last release 2024-05-13 · [PyPI](https://pypi.org/project/types-sqlalchemy-utils/) · [source](https://github.com/cex-solutions/types-sqlalchemy-utils)

_README extract left out: share-alike licence._

### telepath

A library for exchanging data between Python and JavaScript

`pip install telepath` · installs (wheel) · licence: BSD License · rank 5328 · last release 2023-06-12 · [PyPI](https://pypi.org/project/telepath/)

<details><summary>README extract</summary>

*telepath* is a Django library for exchanging data between Python and JavaScript, allowing you to build apps with rich client-side interfaces while keeping the business logic in server-side code.

It provides a mechanism for packing structured data, including Python objects, into a JSON-serializable format. ...

Sections: telepath, What does it do?

</details>

### tableau-api-lib

This library enables developers to call any method seen in Tableau Server's REST API documentation.

`pip install tableau-api-lib` · installs (wheel) · licence: MIT License · rank 5338 · last release 2022-10-15 · [PyPI](https://pypi.org/project/tableau-api-lib/)

<details><summary>README extract</summary>

Features:
This library allows developers to call all methods as seen in Tableau Server's REST API reference.
Each method returns the corresponding HTTP response, providing among other things the status code and a JSON response body. ...

Sections: Overview of tableau-api-lib, Use case, Why use tableau-api-lib, How it all works, Defining your config object, Try it out, For more details, see Tableau's REST API reference., Example of unpacking paginated results

</details>

### types-olefile

Typing stubs for olefile

`pip install types-olefile` · installs (wheel) · licence: Apache-2.0 · rank 5348 · last release 2026-05-08 · [PyPI](https://pypi.org/project/types-olefile/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `olefile` package. It can be used by type checkers
to check code that uses `olefile`. This version of
`types-olefile` aims to provide accurate annotations for
`olefile==0.47.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-fpdf2

Typing stubs for fpdf2

`pip install types-fpdf2` · installs (wheel) · licence: Apache-2.0 · rank 5375 · last release 2026-07-24 · [PyPI](https://pypi.org/project/types-fpdf2/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `fpdf2` package. It can be used by type checkers
to check code that uses `fpdf2`. This version of
`types-fpdf2` aims to provide accurate annotations for
`fpdf2==2.8.4`.

*Note:* The `fpdf2` package includes type annotations or type stubs
since version 2.8.6. ...

</details>

### types-tensorflow

Typing stubs for tensorflow

`pip install types-tensorflow` · installs (wheel) · licence: Apache-2.0 · rank 5402 · last release 2026-10-09 · [PyPI](https://pypi.org/project/types-tensorflow/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `tensorflow` package. It can be used by type checkers
to check code that uses `tensorflow`. This version of
`types-tensorflow` aims to provide accurate annotations for
`tensorflow~=2.18.0`.

Partially generated using mypy-protobuf==3.6.0 and libprotoc 27.2 on `tensorflow==2.18.0`. ...

</details>

### types-dataclasses

Typing stubs for dataclasses

`pip install types-dataclasses` · installs (wheel) · licence: Apache Software License · rank 5501 · last release 2022-06-30 · [PyPI](https://pypi.org/project/types-dataclasses/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `dataclasses` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `dataclasses`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there.

*Note:* `types-dataclasses` is unmaintained and won't be updated. ...

</details>

### tsdownsample

Time series downsampling in rust

`pip install tsdownsample` · installs (wheel) · licence: MIT License · rank 5519 · last release 2026-06-01 · [PyPI](https://pypi.org/project/tsdownsample/) · [source](https://github.com/predict-idlab/tsdownsample)

<details><summary>README extract</summary>

Extremely fast time series downsampling 📈 for visualization, written in Rust.

Features:
- Fast: written in rust with PyO3 bindings
 - leverages optimized argminmax - which is SIMD accelerated with runtime feature detection
 - scales linearly with the number of data points

 - multithreaded with Rayon (in Rust) ...

Example:
```python
from tsdownsample import MinMaxLTTBDownsampler
import numpy as np

# Create a time series
y = np.random.randn(10_000_000)
x = np.arange(len(y))

# Downsample to 1000 points (assuming constant sampling rate)
s_ds = MinMaxLTTBDownsampler().downsample(y, n_out=1000)

# Select downsampled data
downsampled_y = y[s_ds]

...
```

...

</details>

### torch-ema

PyTorch library for computing moving averages of model parameters.

`pip install torch-ema` · installs (wheel) · licence: not stated · rank 5580 · last release 2021-11-17 · [PyPI](https://pypi.org/project/torch-ema/)

### trio-typing

Static type checking support for Trio and related projects

`pip install trio-typing` · installs (wheel) · licence: Apache Software License; MIT License · rank 5588 · last release 2023-12-01 · [PyPI](https://pypi.org/project/trio-typing/)

<details><summary>README extract</summary>

This repository provides:

 * trio (`trio-stubs`)

 * outcome (`outcome-stubs`)

 * async_generator
 (`async_generator-stubs`)

* A package `trio_typing` containing types that Trio programs often want
 to refer to (`AsyncGenerator[Y, S]` and `TaskStatus[T]`)
 (`Nursery` is exported publicly by mainline Trio as of version 0.12.0.) ...

Example:
```python
    from mypy_extensions import VarArg

    @trio_typing.takes_callable_and_args
    def start_soon(
        async_fn: Callable[[VarArg()], Awaitable[T]],
        *args: Any,
        other_keywords: str = are_ok_too,
    ):
        # your implementation here

`start_soon(async_fn, *args)` will raise an error if `async_fn(*args)`
...
```

...

</details>

### types-boto3-bedrock-runtime

Type annotations for boto3 BedrockRuntime 1.43.62 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-bedrock-runtime` · installs (wheel) · licence: MIT · rank 5616 · last release 2026-07-31 · [PyPI](https://pypi.org/project/types-boto3-bedrock-runtime/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_runtime/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 BedrockRuntime 1.43.62 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-bedrock-runtime docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-aiobotocore-kms

Type annotations for aiobotocore KMS 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-kms` · installs (wheel) · licence: MIT · rank 5632 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-kms/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kms/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### tonyg-rfc3339

Python implementation of RFC 3339

`pip install tonyg-rfc3339` · installs from source (sdist only) · licence: UNKNOWN · rank 5667 · last release 2015-12-05 · [PyPI](https://pypi.org/project/tonyg-rfc3339/)

### torch-fidelity

High-fidelity performance metrics for generative models in PyTorch

`pip install torch-fidelity` · installs (wheel) · licence: Apache License 2.0 · rank 5668 · last release 2026-02-17 · [PyPI](https://pypi.org/project/torch-fidelity/)

<details><summary>README extract</summary>

torch-fidelity is the reference implementation of generative image model evaluation metrics in
PyTorch, providing epsilon-exact computation of Inception Score (ISC), Fréchet Inception Distance
(FID), Kernel Inception Distance (KID), and Precision and Recall (PRC). ...

</details>

### types-babel

Typing stubs for babel

`pip install types-babel` · installs (wheel) · licence: Apache Software License · rank 5684 · last release 2023-07-20 · [PyPI](https://pypi.org/project/types-babel/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `babel` package. It
can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`babel`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### textual-dev

Development tools for working with Textual

`pip install textual-dev` · installs (wheel) · licence: MIT License · rank 5686 · last release 2025-10-11 · [PyPI](https://pypi.org/project/textual-dev/)

<details><summary>README extract</summary>

Development tools for Textual.

This package contains the `textual` command line app, which will help to develop Textual applications.

See Getting Started for how to use it.

</details>

### targ

Build a Python CLI for your app, just using type hints and docstrings.

`pip install targ` · installs (wheel) · licence: MIT License · rank 5690 · last release 2026-07-19 · [PyPI](https://pypi.org/project/targ/)

<details><summary>README extract</summary>

Build a Python CLI for your app, just using type hints and docstrings.

Just register your type annotated functions, and that's it - there's no special
syntax to learn, and it's super easy.

And from the command line:

To get documentation:

Example:
```python
# main.py
from targ import CLI

def add(a: int, b: int):
    """
    Add the two numbers.

    :param a:
        The first number.
    :param b:
        The second number.
    """
    print(a + b)

if name == "main":
    cli = CLI()
    cli.register(add)
    cli.run()
```

Sections: targ, Documentation

</details>

### thop

A tool to count the FLOPs of PyTorch model.

`pip install thop` · installs (wheel) · licence: MIT · rank 5711 · last release 2022-09-07 · [PyPI](https://pypi.org/project/thop/)

<details><summary>README extract</summary>

Example:
```python
from torchvision.models import resnet50
from thop import profile
model = resnet50()
input = torch.randn(1, 3, 224, 224)
macs, params = profile(model, inputs=(input, ))
```

Sections: THOP: PyTorch-OpCounter, How to use, Results of Recent Models

</details>

### torchinfo

Model summary in PyTorch, based off of the original torchsummary.

`pip install torchinfo` · installs (wheel) · licence: MIT License · rank 5731 · last release 2023-05-14 · [PyPI](https://pypi.org/project/torchinfo/)

<details><summary>README extract</summary>

(formerly torch-summary)

Torchinfo provides information complementary to what is provided by `print(your_model)` in PyTorch, similar to Tensorflow's `model.summary()` API to view the visualization of the model, which is helpful while debugging your network. ...

Example:
```python
from torchinfo import summary

model = ConvNet()
batch_size = 16
summary(model, input_size=(batch_size, 1, 28, 28))
```

Sections: torchinfo, Usage, How To Use, ```, ├─Linear: 1-5 [7, 50] [7, 10] 510 3,570, Total mult-adds (M): 3.41, Estimated Total Size (MB): 0.51, ResNet, Layer (type:depth-idx) Output Shape Param #, ├─Linear: 1-10 [1, 1000] 2,049,000, Total mult-adds (G): 11.51, Estimated Total Size (MB): 602.25, References

</details>

### tencentcloud-sdk-python-wsa

Tencent Cloud Wsa SDK for Python

`pip install tencentcloud-sdk-python-wsa` · installs (wheel) · licence: Apache Software License · rank 5742 · last release 2026-10-26 · [PyPI](https://pypi.org/project/tencentcloud-sdk-python-wsa/)

<details><summary>README extract</summary>

Tencent Cloud Python Wsa SDK is the official software development kit, which allows Python developers to write software that makes use of Tencent Cloud services like CVM and CBS.
The SDK works on Python versions:

 * 2.7 and greater, including 3.x

Sections: Tencent Cloud SDK for Python, Quick Start

</details>

### tencentcloud-sdk-python

Tencent Cloud SDK for Python

`pip install tencentcloud-sdk-python` · installs (wheel) · licence: Apache Software License · rank 5766 · last release 2026-11-06 · [PyPI](https://pypi.org/project/tencentcloud-sdk-python/)

<details><summary>README extract</summary>

Tencent Cloud Python SDK is the official software development kit, which allows Python developers to write software that makes use of Tencent Cloud services like CVM and CBS.

The SDK works on Python versions:

 * 2.7 and greater, including 3.x

Sections: Tencent Cloud SDK for Python, Quick Start

</details>

### types-pkg-resources

Typing stubs for pkg_resources

`pip install types-pkg-resources` · does not install on CPython 3.14 · licence: Apache Software License · rank 5815 · last release 2021-06-17 · [PyPI](https://pypi.org/project/types-pkg-resources/)

<details><summary>README extract</summary>

This is an auto-generated PEP 561 type stub package for `pkg_resources` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `pkg_resources`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there.

See for more details. ...

</details>

### types-aiobotocore-cloudwatch

Type annotations for aiobotocore CloudWatch 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-cloudwatch` · installs (wheel) · licence: MIT · rank 5818 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-cloudwatch/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-Flask-Cors

Typing stubs for Flask-Cors

`pip install types-Flask-Cors` · installs (wheel) · licence: Apache-2.0 · rank 5822 · last release 2026-07-12 · [PyPI](https://pypi.org/project/types-Flask-Cors/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `Flask-Cors` package. It can be used by type checkers
to check code that uses `Flask-Cors`. This version of
`types-Flask-Cors` aims to provide accurate annotations for
`Flask-Cors==6.0.3`.

*Note:* The `Flask-Cors` package includes type annotations or type stubs
since version 6.0.4. ...

</details>

### torchlibrosa

PyTorch implemention of part of librosa functions.

`pip install torchlibrosa` · installs (wheel) · licence: MIT License · rank 5829 · last release 2023-02-21 · [PyPI](https://pypi.org/project/torchlibrosa/)

<details><summary>README extract</summary>

This codebase provides PyTorch implementation of some librosa functions. If users previously used for training cpu-extracted features from librosa, but want to add GPU acceleration during training and evaluation, TorchLibrosa will provide almost identical features to standard torchlibrosa functions (numerical difference less than 1e-5).

Example:
```python
import torch
import torchlibrosa as tl

batch_size = 16
sample_rate = 22050
win_length = 2048
hop_length = 512
n_mels = 128

batch_audio = torch.empty(batch_size, sample_rate).uniform(-1, 1)  # (batch_size, sample_rate)

# TorchLibrosa feature extractor the same as librosa.feature.melspectrogram()
feature_extractor = torch.nn.Sequential(
...
```

...

</details>

### typedspark

Column-wise type annotations for pyspark DataFrames

`pip install typedspark` · installs (wheel) · licence: Apache-2.0 · rank 5866 · last release 2026-10-28 · [PyPI](https://pypi.org/project/typedspark/)

<details><summary>README extract</summary>

We love Spark! But in production code we're wary when we see:

Because… How do we know which columns are supposed to be in ``df``?

Using ``typedspark``, we can be more explicit about what these data should look like.

The advantages include: ...

Example:
```python
from pyspark.sql import DataFrame

def foo(df: DataFrame) -> DataFrame:
    # do stuff
    return df
```

Sections: Documentation, Compatibility, Demo videos, IDE demo, Jupyter / Databricks notebooks demo, FAQ

</details>

### treelite

Treelite: Universal model exchange format for decision tree forests

`pip install treelite` · installs (wheel) · licence: Apache Software License · rank 5869 · last release 2026-10-27 · [PyPI](https://pypi.org/project/treelite/) · [docs](https://treelite.readthedocs.io/en/latest/) · [source](https://github.com/dmlc/treelite)

<details><summary>README extract</summary>

Treelite is a universal model exchange and serialization format for decision tree forests.

See the documentation for more details.

</details>

### types-jwcrypto

Typing stubs for jwcrypto

`pip install types-jwcrypto` · installs (wheel) · licence: Apache-2.0 · rank 5893 · last release 2026-09-28 · [PyPI](https://pypi.org/project/types-jwcrypto/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `jwcrypto` package. It can be used by type checkers
to check code that uses `jwcrypto`. This version of
`types-jwcrypto` aims to provide accurate annotations for
`jwcrypto==1.6.1`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tinytuya

Python module to interface with Tuya WiFi smart devices

`pip install tinytuya` · installs (wheel) · licence: MIT License · rank 5929 · last release 2026-07-06 · [PyPI](https://pypi.org/project/tinytuya/)

<details><summary>README extract</summary>

Python module to interface with Tuya WiFi smart devices

This python module controls and reads state of Tuya compatible WiFi Smart Devices (Plugs, Switches, Lights, Window Covers, etc.) using the local area network (LAN) or the cloud (TuyaCloud API). ...

Example:
```python
import tinytuya

"""
OUTLET Device
"""
d = tinytuya.Device('DEVICE_ID_HERE', 'IP_ADDRESS_HERE', 'LOCAL_KEY_HERE', version=3.3)  # Set version to match your device (3.1, 3.2, 3.3, 3.4, or 3.5)
data = d.status()

# Show status and state of first controlled switch on device
print('Dictionary %r' % data)
...
```

...

</details>

### types-boto3-ssm

Type annotations for boto3 SSM 1.43.126 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-ssm` · installs (wheel) · licence: MIT · rank 5962 · last release 2026-11-06 · [PyPI](https://pypi.org/project/types-boto3-ssm/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_ssm/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SSM 1.43.126
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-ssm docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### tomlrt

A format-preserving TOML reader and writer for Python.

`pip install tomlrt` · installs (wheel) · licence: MIT · rank 5966 · last release 2026-10-31 · [PyPI](https://pypi.org/project/tomlrt/) · [docs](https://dimbleby.github.io/tomlrt/) · [source](https://github.com/dimbleby/tomlrt)

<details><summary>README extract</summary>

A format-preserving TOML reader and writer for Python.

Parse a document, edit it, dump it, and the bytes you didn't touch round-trip exactly — comments, whitespace, string style, and number formatting all intact.

Supports TOML 1.1.

Build a document from scratch:

Example:
```python
import tomlrt

with open("pyproject.toml", "rb") as f:
    doc = tomlrt.load(f)

doc"project" = "0.2.0"
doc"project".append("requests>=2")

print(tomlrt.dumps(doc))   # comments and layout are preserved
```

Sections: tomlrt, Documentation

</details>

### types-google-cloud-ndb

Typing stubs for google-cloud-ndb

`pip install types-google-cloud-ndb` · installs (wheel) · licence: Apache-2.0 · rank 5986 · last release 2026-10-21 · [PyPI](https://pypi.org/project/types-google-cloud-ndb/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `google-cloud-ndb` package. It can be used by type checkers
to check code that uses `google-cloud-ndb`. This version of
`types-google-cloud-ndb` aims to provide accurate annotations for
`google-cloud-ndb==2.4.*`.

This stub package is marked as partial. ...

</details>

### tbats

BATS and TBATS for time series forecasting

`pip install tbats` · installs (wheel) · licence: MIT · rank 6061 · last release 2026-09-16 · [PyPI](https://pypi.org/project/tbats/)

<details><summary>README extract</summary>

Package provides BATS and TBATS time series forecasting methods described in:

> De Livera, A.M., Hyndman, R.J., & Snyder, R. D. (2011), Forecasting time series with complex seasonal patterns using exponential smoothing, Journal of the American Statistical Association, 106(496), 1513-1527.

Example:
```python
from tbats import TBATS
import numpy as np

# required on windows for multi-processing,
# see
if name == 'main':
    np.random.seed(2342)
    t = np.array(range(0, 160))
    y = 5 * np.sin(t * 2 * np.pi / 7) + 2 * np.cos(t * 2 * np.pi / 30.5) + \
        ((t / 20) ** 1.5 + np.random.normal(size=160) * t / 50) + 10

    # Create estimator
...
```

Sections: BATS and TBATS time series forecasting, Minimal working example, Troubleshooting, Comparison to R implementation

</details>

### tpk-ar

A package for parsing type tree packages (TPK)

`pip install tpk-ar` · installs from source (sdist only) · licence: not stated · rank 6086 · last release 2026-08-01 · [PyPI](https://pypi.org/project/tpk-ar/)

<details><summary>README extract</summary>

A Python port of AssetRipper/Tpk, primarily for use in UnityPy.

This is maintained as a separate project to ensure forward compatibility for older UnityPy versions against potential breaking changes in the original code. ...

Sections: tpk_ar, Options, TODO, Benchmarking

</details>

### tensorrt-cu12

A high performance deep learning inference library

`pip install tensorrt-cu12` · installs from source (sdist only) · licence: Other/Proprietary License · rank 6123 · last release 2026-10-08 · [PyPI](https://pypi.org/project/tensorrt-cu12/)

<details><summary>README extract</summary>

NVIDIA TensorRT is an SDK that facilitates high-performance machine learning inference. It is designed to work in a complementary fashion with training frameworks such as PyTorch. It focuses specifically on running an already-trained network quickly and efficiently on NVIDIA hardware.

</details>

### types-pyRFC3339

Typing stubs for pyRFC3339

`pip install types-pyRFC3339` · installs (wheel) · licence: Apache-2.0 · rank 6145 · last release 2025-08-25 · [PyPI](https://pypi.org/project/types-pyRFC3339/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `pyRFC3339` package. It can be used by type checkers
to check code that uses `pyRFC3339`. This version of
`types-pyRFC3339` aims to provide accurate annotations for
`pyRFC3339~=2.0.1`.

*Note:* The `pyRFC3339` package includes type annotations or type stubs
since version 2.1.0. ...

</details>

### throttler

Zero-dependency Python package for easy throttling with asyncio support

`pip install throttler` · installs (wheel) · licence: MIT License · rank 6146 · last release 2026-01-27 · [PyPI](https://pypi.org/project/throttler/) · [source](https://github.com/uburuntu/throttler)

<details><summary>README extract</summary>

Zero-dependency Python package for easy throttling with asyncio support.


Example:
```python
import asyncio
import time

from throttler import throttle

# Limit to two calls per second
@throttle(rate_limit=2, period=1.0)
async def task():
    return await asyncio.sleep(0.1)

async def many_tasks(count: int):
    coros = [task() for _ in range(count)]
    for coro in asyncio.as_completed(coros):
        _ = await coro
...
```

Sections: Throttler, 📌 API Overview, ✅ Choosing the Right Tool, 🛠 Usage Examples, Throttler and ThrottlerSimultaneous, Simple Example, API Example, ExecutionTimer, Timer, 🧠 Behavior Notes, ⚠️ Error Handling

</details>

### triangle

Python binding to the triangle library

`pip install triangle` · does not install on CPython 3.14 · licence: LGPL-3.0 · rank 6172 · last release 2025-01-07 · [PyPI](https://pypi.org/project/triangle/) · [source](https://github.com/drufat/triangle)

_README extract left out: share-alike licence._

### types-Flask-Migrate

Typing stubs for Flask-Migrate

`pip install types-Flask-Migrate` · installs (wheel) · licence: Apache-2.0 · rank 6207 · last release 2026-05-08 · [PyPI](https://pypi.org/project/types-Flask-Migrate/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `Flask-Migrate` package. It can be used by type checkers
to check code that uses `Flask-Migrate`. This version of
`types-Flask-Migrate` aims to provide accurate annotations for
`Flask-Migrate==4.1.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### transliterate

Bi-directional transliterator for Python

`pip install transliterate` · installs (wheel) · licence: GPL 2.0/LGPL 2.1 · rank 6254 · last release 2018-09-17 · [PyPI](https://pypi.org/project/transliterate/)

_README extract left out: share-alike licence._

### types-ipaddress

Typing stubs for ipaddress

`pip install types-ipaddress` · installs (wheel) · licence: Apache Software License · rank 6285 · last release 2022-01-30 · [PyPI](https://pypi.org/project/types-ipaddress/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `ipaddress` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `ipaddress`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there.

See for more details. ...

</details>

### types-requests-oauthlib

Typing stubs for requests-oauthlib

`pip install types-requests-oauthlib` · installs (wheel) · licence: Apache-2.0 · rank 6300 · last release 2026-10-06 · [PyPI](https://pypi.org/project/types-requests-oauthlib/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `requests-oauthlib` package. It can be used by type checkers
to check code that uses `requests-oauthlib`. This version of
`types-requests-oauthlib` aims to provide accurate annotations for
`requests-oauthlib==2.0.*`.

This package is part of the typeshed project. ...

</details>

### toolbox-core

Python Base SDK for interacting with the Toolbox service

`pip install toolbox-core` · installs (wheel) · licence: Apache Software License · rank 6320 · last release 2026-09-01 · [PyPI](https://pypi.org/project/toolbox-core/) · [source](https://github.com/googleapis/mcp-toolbox-sdk-python.git)

<details><summary>README extract</summary>

This SDK allows you to seamlessly integrate the functionalities of
MCP Toolbox allowing you to load and
use tools defined in the service as standard Python functions within your GenAI
applications.

For detailed guides, authentication examples, and advanced configuration, visit the Python SDK Core Guide.

<!-- TOC ignore:true -->
<!-- TOC --> ...

Example:
```python
import asyncio
from toolbox_core import ToolboxClient

async def main():
    # Replace with the actual URL where your Toolbox service is running
    async with ToolboxClient(" as toolbox:
        weather_tool = await toolbox.load_tool("get_weather")
        result = await weather_tool(location="London")
        print(result)

if name == "main":
...
```

Sections: MCP Toolbox Core SDK, Quickstart, Usage

</details>

### tabmat

Efficient matrix representations for working with tabular data.

`pip install tabmat` · installs (wheel) · licence: not stated · rank 6389 · last release 2026-11-05 · [PyPI](https://pypi.org/project/tabmat/)

<details><summary>README extract</summary>

Example:
```python
import tabmat as tm
import numpy as np

dense_array = np.random.normal(size=(100, 1))
```

Sections: Getting Started, Use case, This library and its design, Matrix types, Benchmarks, API documentation

</details>

### types-pywin32

Typing stubs for pywin32

`pip install types-pywin32` · installs (wheel) · licence: Apache-2.0 · rank 6451 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-pywin32/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `pywin32` package. It can be used by type checkers
to check code that uses `pywin32`. This version of
`types-pywin32` aims to provide accurate annotations for
`pywin32==312.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tinker-cookbook

Implementations of post-training algorithms using the Tinker API

`pip install tinker-cookbook` · installs (wheel) · licence: Apache-2.0 · rank 6460 · last release 2026-11-06 · [PyPI](https://pypi.org/project/tinker-cookbook/) · [docs](https://tinker-docs.thinkingmachines.ai/) · [source](https://github.com/thinking-machines-lab/tinker-cookbook)

<details><summary>README extract</summary>

We provide two libraries for the broader community to customize their language models: `tinker` and `tinker-cookbook`.

- `tinker` is a training SDK for researchers and developers to fine-tune language models. You send API requests to us and we handle the complexities of distributed training. ...

Example:
```python
from tinker_cookbook import weights

export = training_client.save_weights_external(name="export").result()
weights.download(tinker_path=export.path, output_dir="model-checkpoint")
```

Sections: Tinker Cookbook, Using Inkling models, Tinker, Tutorials, Evaluation (experimental), Documentation, Utilities, Claude Code Skills

</details>

### tarsafe

A safe subclass of the TarFile class for interacting with tar files. Can be used as a direct drop-in replacement for safe usage of extractall()

`pip install tarsafe` · installs (wheel) · licence: MIT License · rank 6492 · last release 2026-08-15 · [PyPI](https://pypi.org/project/tarsafe/)

<details><summary>README extract</summary>

Tarsafe is a drop-in replacement for the tarfile module from the standard library to safely handle the vulnerable `extractall()` method. Inspired by a 6 year old security bug.

Example:
```python
from tarsafe import TarSafe

tar = TarSafe.open("example.tar", "r")
tar.extractall()
tar.close()

# OR

with TarSafe.open("example.tar", "r") as tar:
    tar.extractall()
```

Sections: Tarsafe, Usage, Note on Python 3.12+

</details>

### typed-argument-parser

Typed Argument Parser

`pip install typed-argument-parser` · installs (wheel) · licence: MIT · rank 6497 · last release 2026-03-28 · [PyPI](https://pypi.org/project/typed-argument-parser/)

<details><summary>README extract</summary>

Tap is a typed modernization of Python's argparse library.

Tap provides the following benefits:
- Static type checking
- Code completion
- Source code navigation (e.g. go to definition and go to implementation) ...

Example:
```python
# square.py
from tap import tapify

def square(num: float) -> float:
    return num ** 2

if name == 'main':
    print(f'The square of your number is {tapify(square)}.')
```

Sections: Typed Argument Parser (Tap), Tap is Python-native, Tap features, Arguments, Tap help, Configuring arguments, Adding special argument behavior, Adding subparsers, Types, `str`, `int`, and `float`, `bool`, `Optional`, `List`, `Set`

</details>

### tf-playwright-stealth

Makes playwright stealthy like a ninja!

`pip install tf-playwright-stealth` · installs (wheel) · licence: MIT License · rank 6499 · last release 2025-06-13 · [PyPI](https://pypi.org/project/tf-playwright-stealth/) · [source](https://github.com/tinyfish-io/tf-playwright-stealth)

<details><summary>README extract</summary>

> Transplanted from puppeteer-extra-plugin-stealth.

This is a package that makes playwright stealthy like a ninja by spoofing browser features in order to reduce the chance of detection.

Example:
```python
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

with sync_playwright() as p:
    browser = p.chromium.launch(
            headless=True,
        )
    page = browser.new_page()
    stealth_sync(page)
    page.goto("
    page.screenshot(path=f"example_with_stealth.png", full_page=True)
    browser.close()
```

Sections: 🥷🏻 tf-playwright-stealth, Usage, sync, async, Results

</details>

### tqdm-multiprocess

Easy multiprocessing with tqdm and logging redirected to main process.

`pip install tqdm-multiprocess` · installs (wheel) · licence: MIT License · rank 6544 · last release 2020-10-27 · [PyPI](https://pypi.org/project/tqdm-multiprocess/)

<details><summary>README extract</summary>

Using queues, tqdm-multiprocess supports multiple worker processes, each with multiple tqdm progress bars, displaying them cleanly through the main process. The worker processes also have access to a single global tqdm for aggregate progress monitoring.

Logging is also redirected from the subprocesses to the root logger in the main process. ...

Example:
```python
from time import sleep
import multiprocessing
import tqdm

import logging
from tqdm_multiprocess.logger import setup_logger_tqdm
logger = logging.getLogger(name)

from tqdm_multiprocess import TqdmMultiProcessPool

iterations1 = 100
iterations2 = 5
iterations3 = 2
def some_other_function(tqdm_func, global_tqdm):

...
```

Sections: tqdm-multiprocess, Usage, examples/basic_example.py

</details>

### toml-cli

Command line interface to read and write keys/values to/from toml files

`pip install toml-cli` · installs (wheel) · licence: MIT AND (Apache-2.0 OR BSD-2-Clause) · rank 6591 · last release 2025-09-12 · [PyPI](https://pypi.org/project/toml-cli/) · [source](https://github.com/mrijken/toml-cli)

<details><summary>README extract</summary>

Command line interface for toml files.

This can be usefull for getting or setting parts of a toml file without an editor.
Which can be convinient when values have to be read by a script for example in
continuous development steps.

Sections: toml-cli, Get a value, Search with JMESPath, Set a value, Add a section, Unset a value

</details>

### types-boto3-bedrock

Type annotations for boto3 Bedrock 1.43.116 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-bedrock` · installs (wheel) · licence: MIT · rank 6628 · last release 2026-10-20 · [PyPI](https://pypi.org/project/types-boto3-bedrock/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Bedrock 1.43.116
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-bedrock docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### timesfm

A time series foundation model.

`pip install timesfm` · installs (wheel) · licence: Apache-2.0 · rank 6692 · last release 2026-09-09 · [PyPI](https://pypi.org/project/timesfm/)

<details><summary>README extract</summary>

TimesFM (Time Series Foundation Model) is a pretrained time-series foundation
model developed by Google Research for time-series forecasting.

 A decoder-only foundation model for time-series forecasting,
 ICML 2024.
* <span style="color:red">(NEW!)</span> TimesFM 3.0 Checkpoint:
 `google/timesfm-3.0-pytorch`.

 TimesFM Hugging Face Collection. ...

Features:
- Native Multivariate & Univariate Forecasting with Covariates: Seamlessly
 forecast multi-channel multivariate series as well as individual univariate
 series, with native support for past-only and past-and-future dynamic
 covariates without ...

Example:
```python
import numpy as np
from timesfm3 import TimesFM3Evaluator, ModelConfig

# Initialize TimesFM 3.0
config = ModelConfig(
    checkpoint_path="google/timesfm-3.0-pytorch",
...

</details>

### truss-transfer

Speed up file transfers with the baseten.co + baseten_fs.

`pip install truss-transfer` · installs (wheel) · licence: not stated · rank 6695 · last release 2026-10-21 · [PyPI](https://pypi.org/project/truss-transfer/) · [source](https://github.com/basetenlabs/truss.git)

<details><summary>README extract</summary>

Python-optional download utility for resolving Baseten Pointers (bptr).

Example:
```python
import truss_transfer

# Resolve bptr using default download directory from environment
result_dir = truss_transfer.lazy_data_resolve()

# Resolve bptr with custom download directory
result_dir = truss_transfer.lazy_data_resolve("/custom/download/path")

# Example usage in a data loader
def lazy_data_loader(download_dir: str):
...
```

Sections: Truss-Transfer, How to Resolve a bptr, Via Python Package, Via CLI, How to Build a bptr and Save it via Python, PyModelRepo Parameters, End-to-End Flow, Step 1: Create a bptr Manifest, Step 2: Set up Environment (Optional), Step 3: Resolve the bptr, Step 4: Use the Downloaded Files, Complete Workflow, Secrets, AWS

</details>

### types-antlr4-python3-runtime

Typing stubs for antlr4-python3-runtime

`pip install types-antlr4-python3-runtime` · installs (wheel) · licence: Apache-2.0 · rank 6732 · last release 2026-08-07 · [PyPI](https://pypi.org/project/types-antlr4-python3-runtime/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `antlr4-python3-runtime` package. It can be used by type checkers
to check code that uses `antlr4-python3-runtime`. This version of
`types-antlr4-python3-runtime` aims to provide accurate annotations for
`antlr4-python3-runtime==4.13.*`.

This package is part of the typeshed project. ...

</details>

### truss

A seamless bridge from model development to model delivery

`pip install truss` · installs (wheel) · licence: MIT · rank 6750 · last release 2026-11-05 · [PyPI](https://pypi.org/project/truss/) · [docs](https://truss.baseten.co) · [source](https://github.com/basetenlabs/truss)

<details><summary>README extract</summary>

The simplest way to serve AI/ML models in production

Truss is the CLI for deploying and serving ML models on Baseten. Package your model's serving logic in Python, launch training jobs, and deploy to production—Truss handles containerization, dependency management, and GPU configuration. ...

Features:
* Write once, run anywhere: Package model code, weights, and dependencies with a model server that behaves the same in development and production. ...

Example:
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["BASETEN_API_KEY"],
    base_url="
)

response = client.chat.completions.create(
    model="Qwen-2.5-3B",
    messages=[
        {"role": "user", "content": "What is machine learning?"}
    ],
)

print(response.choices[0].message.content)
```

...

</details>

### tensorrt-cu12-bindings

A high performance deep learning inference library

`pip install tensorrt-cu12-bindings` · installs (wheel) · licence: Other/Proprietary License · rank 6801 · last release 2026-10-08 · [PyPI](https://pypi.org/project/tensorrt-cu12-bindings/)

<details><summary>README extract</summary>

A high performance deep learning inference library

</details>

### types-PyJWT

Typing stubs for PyJWT

`pip install types-PyJWT` · installs (wheel) · licence: Apache Software License · rank 6818 · last release 2021-06-17 · [PyPI](https://pypi.org/project/types-PyJWT/)

<details><summary>README extract</summary>

This is an auto-generated PEP 561 type stub package for `PyJWT` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `PyJWT`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-aiobotocore-cognito-idp

Type annotations for aiobotocore CognitoIdentityProvider 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-cognito-idp` · installs (wheel) · licence: MIT · rank 6897 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-cognito-idp/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cognito_idp/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-orjson

Typing stubs for orjson

`pip install types-orjson` · installs (wheel) · licence: Apache Software License · rank 6910 · last release 2022-01-07 · [PyPI](https://pypi.org/project/types-orjson/)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `orjson` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `orjson`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### trackio

A lightweight, local-first, and free experiment tracking library built on top of Hugging Face Datasets and Spaces.

`pip install trackio` · installs (wheel) · licence: MIT License · rank 6953 · last release 2026-11-02 · [PyPI](https://pypi.org/project/trackio/) · [source](https://github.com/gradio-app/trackio)

<details><summary>README extract</summary>

Welcome to `trackio`: a lightweight, free experiment tracking library built by Hugging Face for humans and AI agents 🤗.

Why Trackio when other experiment-tracking libraries exist? Trackio has a few qualities that make it particularly useful for agents:
* It is local-first, because you shouldn't need to make an account to log data
* Logs are ...

Example:
```python
import trackio
import random
import time

runs = 3
epochs = 8

for run in range(runs):
    trackio.init(
        project="my-project",
        config={"epochs": epochs, "learning_rate": 0.001, "batch_size": 64}
    )

    for epoch in range(epochs):
        train_loss = random.uniform(0.2, 1.0)
        train_acc = random.uniform(0.6, 0.95)

...
```

...

</details>

### tensorrt-cu12-libs

TensorRT Libraries

`pip install tensorrt-cu12-libs` · installs from source (sdist only) · licence: Other/Proprietary License · rank 6965 · last release 2026-10-08 · [PyPI](https://pypi.org/project/tensorrt-cu12-libs/)

### textract

extract text from any document. no muss. no fuss.

`pip install textract` · installs (wheel) · licence: MIT · rank 6988 · last release 2026-09-01 · [PyPI](https://pypi.org/project/textract/) · [source](https://github.com/deanmalmgren/textract)

<details><summary>README extract</summary>

Extract text from any document. No muss. No fuss.

Full documentation.

</details>

### tensorlake

Tensorlake SDK for agent sandboxes and sandbox-native orchestration

`pip install tensorlake` · installs (wheel) · licence: not stated · rank 7020 · last release 2026-11-06 · [PyPI](https://pypi.org/project/tensorlake/) · [source](https://github.com/tensorlakeai/tensorlake)

<details><summary>README extract</summary>

Build agents with sandboxes and serverless orchestration runtime

Tensorlake is a compute infrastructure platform for building agentic applications with sandboxes.

The Sandbox API creates MicroVM sandboxes which you can use to run agents, or use them as an isolated environment for running tools or LLM generated code. ...

Features:
* Fastest Filesystem I/O — Block-based storage achieving near-SSD speeds inside virtual machines. In SQLite benchmarks (2 vCPUs, 4 GB RAM), Tensorlake completes in 2.45s vs Vercel 3.00s (1.2×), E2B 3.92s (1.6×), Modal 4.66s (1.9×), and Daytona 5.51s ...

Example:
```python
from agents import Agent, Runner
from agents.tool import WebSearchTool, function_tool
from tensorlake.applications import application, function, Image

...

</details>

### types-first

Typing stubs for first

`pip install types-first` · installs (wheel) · licence: Apache-2.0 · rank 7035 · last release 2026-04-08 · [PyPI](https://pypi.org/project/types-first/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `first` package. It can be used by type checkers
to check code that uses `first`. This version of
`types-first` aims to provide accurate annotations for
`first==2.0.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

</details>

### types-aiobotocore-ses

Type annotations for aiobotocore SES 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-ses` · installs (wheel) · licence: MIT · rank 7050 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-ses/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ses/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### tftpy

A TFTP protocol library for Python

`pip install tftpy` · installs (wheel) · licence: MIT · rank 7082 · last release 2026-02-04 · [PyPI](https://pypi.org/project/tftpy/)

<details><summary>README extract</summary>

Copyright, Michael P. Soulier, 2010+

Sections: About Tftpy, Purpose, Dependencies, Trifles, Limitations

</details>

### tkinterdnd2

TkinterDnD2 is a python wrapper for George Petasis'' tkDnD Tk extension version 2

`pip install tkinterdnd2` · installs (wheel) · licence: MIT License · rank 7106 · last release 2026-10-25 · [PyPI](https://pypi.org/project/tkinterdnd2/)

<details><summary>README extract</summary>

Eliav2/tkinterdnd2 is a fork of the (unmaintained) pmgagne/tkinterdnd2 which is a python wrapper for tkdnd .

This repo was originally forked and edited for the purpose of publishing to pypi so one could simply install this package with `pip install tkinterdnd2`. ...

Example:
```python
import tkinter as tk

from tkinterdnd2 import DND_FILES, TkinterDnD

root = TkinterDnD.Tk()  # notice - use this instead of tk.Tk()

lb = tk.Listbox(root)
lb.insert(1, "drag files to here")

def on_drop(event):
    # event.data is a raw Tcl list string, not a Python list - see note below
    for path in root.tk.splitlist(event.data):
...
```

Sections: TkinterDnD2, What is TkDnD, Usage, Framework Integration, PySimpleGUI, CustomTkinter

</details>

### types-aiobotocore-sesv2

Type annotations for aiobotocore SESV2 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-sesv2` · installs (wheel) · licence: MIT · rank 7114 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-sesv2/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sesv2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### textual-autocomplete

Easily add autocomplete dropdowns to your Textual apps.

`pip install textual-autocomplete` · installs (wheel) · licence: MIT · rank 7143 · last release 2025-09-24 · [PyPI](https://pypi.org/project/textual-autocomplete/)

<details><summary>README extract</summary>

Example:
```python
from textual.app import App, ComposeResult
from textual.widgets import Input
from textual_autocomplete import AutoComplete, DropdownItem

class ColorFinder(App):
    def compose(self) -> ComposeResult:
        # Create a standard Textual input
        text_input = Input(placeholder="Type a color...")
        yield text_input

...
```

Sections: Quick Start, Core Features, Examples, With Left Metadata Column, Styled Two-Column Layout, Keyboard Controls, Styling, Styling the prefix, Completing Paths, Dynamic Data with Callbacks, Customizing Behavior, More Examples

</details>

### types-zxcvbn

Typing stubs for zxcvbn

`pip install types-zxcvbn` · installs (wheel) · licence: Apache-2.0 · rank 7150 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-zxcvbn/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `zxcvbn` package. It can be used by type checkers
to check code that uses `zxcvbn`. This version of
`types-zxcvbn` aims to provide accurate annotations for
`zxcvbn==4.5.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-maxminddb

Typing stubs for maxminddb

`pip install types-maxminddb` · installs (wheel) · licence: Apache Software License · rank 7171 · last release 2021-09-20 · [PyPI](https://pypi.org/project/types-maxminddb/)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `maxminddb` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `maxminddb`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### tensorrt

TensorRT Metapackage

`pip install tensorrt` · installs from source (sdist only) · licence: Other/Proprietary License · rank 7234 · last release 2026-10-08 · [PyPI](https://pypi.org/project/tensorrt/)

<details><summary>README extract</summary>

NVIDIA TensorRT is an SDK that facilitates high-performance machine learning inference. It is designed to work in a complementary fashion with training frameworks such as PyTorch. It focuses specifically on running an already-trained network quickly and efficiently on NVIDIA hardware.

</details>

### torchcrepe

Pytorch implementation of CREPE pitch tracker

`pip install torchcrepe` · installs (wheel) · licence: MIT License · rank 7286 · last release 2025-05-16 · [PyPI](https://pypi.org/project/torchcrepe/)

<details><summary>README extract</summary>

Pytorch implementation of the CREPE [1] pitch tracker. The original Tensorflow
implementation can be found here. The
provided model weights were obtained by converting the "tiny" and "full" models
using MMdnn, an open-source model
management framework.

Example:
```python
import torchcrepe

# Load audio
audio, sr = torchcrepe.load.audio( ... )

# Here we'll use a 5 millisecond hop length
hop_length = int(sr / 200.)

# Provide a sensible frequency range for your domain (upper limit is 2006 Hz)
# This would be a reasonable range for speech
fmin = 50
fmax = 550

# Select a model capacity--one of "tiny" or "full"
...
```

...

</details>

### types-boto3-ecs

Type annotations for boto3 ECS 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-ecs` · installs (wheel) · licence: MIT · rank 7288 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-boto3-ecs/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_ecs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 ECS 1.43.124
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-ecs docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-ldap3

Typing stubs for ldap3

`pip install types-ldap3` · installs (wheel) · licence: Apache-2.0 · rank 7294 · last release 2026-11-07 · [PyPI](https://pypi.org/project/types-ldap3/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `ldap3` package. It can be used by type checkers
to check code that uses `ldap3`. This version of
`types-ldap3` aims to provide accurate annotations for
`ldap3==2.9.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

</details>

### tardis-client

Python client for tardis.dev - historical tick-level cryptocurrency market data replay API.

`pip install tardis-client` · installs (wheel) · licence: OSI Approved · rank 7299 · last release 2026-03-26 · [PyPI](https://pypi.org/project/tardis-client/)

<details><summary>README extract</summary>

`tardis-client` is deprecated and frozen.

This package has been replaced by `tardis-dev`, the unified Python package for replay, dataset downloads, exchange metadata, and cache helpers.

This `1.4.2` release does not introduce new features. Its purpose is to point existing `tardis-client` users to the migration path.

Migration notice: ...

Example:
```python
from tardis_client import TardisClient, Channel

client = TardisClient(api_key="YOUR_API_KEY")

async for item in client.replay(
    exchange="bitmex",
    from_date="2019-06-01",
    to_date="2019-06-02",
    filters=[Channel("trade", ["XBTUSD"])],
):
    print(item)
```

Sections: tardis-client, Migrate To `tardis-dev`, Old To New, Replay, Cache Cleanup, Dataset Downloads

</details>

### types-toposort

Typing stubs for toposort

`pip install types-toposort` · installs (wheel) · licence: Apache-2.0 · rank 7312 · last release 2026-04-08 · [PyPI](https://pypi.org/project/types-toposort/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `toposort` package. It can be used by type checkers
to check code that uses `toposort`. This version of
`types-toposort` aims to provide accurate annotations for
`toposort==1.10`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tentaclio-postgres

A python project containing all the dependencies for schema postgres for tentaclio.

`pip install tentaclio-postgres` · installs (wheel) · licence: MIT · rank 7315 · last release 2026-10-26 · [PyPI](https://pypi.org/project/tentaclio-postgres/)

<details><summary>README extract</summary>

A package containing all the dependencies for the postgresql tentaclio schema .

Sections: tentaclio-postgres, Quick Start

</details>

### types-aiobotocore-full

All-in-one type annotations for aiobotocore 3.10.0 generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-full` · installs (wheel) · licence: MIT · rank 7378 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-full/) · [docs](https://youtype.github.io/types_aiobotocore_docs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, How it works, What's new, Implemented features

</details>

### types-typed-ast

Typing stubs for typed-ast

`pip install types-typed-ast` · installs (wheel) · licence: Apache Software License · rank 7380 · last release 2023-07-05 · [PyPI](https://pypi.org/project/types-typed-ast/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `typed-ast` package. It
can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`typed-ast`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### telegramify-markdown

Convert Markdown to Telegram plain text + MessageEntity pairs

`pip install telegramify-markdown` · installs (wheel) · licence: MIT · rank 7416 · last release 2026-10-30 · [PyPI](https://pypi.org/project/telegramify-markdown/) · [source](https://github.com/sudoskys/telegramify-markdown)

<details><summary>README extract</summary>

**Effortlessly convert raw Markdown to Telegram plain text +
MessageEntity pairs.**

Say goodbye to MarkdownV2 escaping headaches! This library parses Markdown (including LLM output, GitHub READMEs, etc.)
and produces `(text, entities)` tuples that can be sent directly via the Telegram Bot API — no `parse_mode` needed. ...

Example:
```python
from telebot import TeleBot
from telegramify_markdown import convert

bot = TeleBot("YOUR_TOKEN")

md = "Bold, _italic_, and `code`."
text, entities = convert(md)

bot.send_message(
    chat_id,
    text,
    entities=[e.to_dict() for e in entities],
)
```

...

</details>

### types-channels

Typing stubs for channels

`pip install types-channels` · installs (wheel) · licence: Apache-2.0 · rank 7417 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-channels/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `channels` package. It can be used by type checkers
to check code that uses `channels`. This version of
`types-channels` aims to provide accurate annotations for
`channels==4.3.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-hvac

Typing stubs for hvac

`pip install types-hvac` · installs (wheel) · licence: Apache-2.0 · rank 7422 · last release 2026-11-02 · [PyPI](https://pypi.org/project/types-hvac/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `hvac` package. It can be used by type checkers
to check code that uses `hvac`. This version of
`types-hvac` aims to provide accurate annotations for
`hvac==2.4.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

</details>

### types-boto3-sns

Type annotations for boto3 SNS 1.43.97 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-sns` · installs (wheel) · licence: MIT · rank 7431 · last release 2026-09-17 · [PyPI](https://pypi.org/project/types-boto3-sns/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_sns/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SNS 1.43.97
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-sns docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### tdda

Test-driven data analysis: command-line tools and Python APIs for data validation, testing analytical pipelines, automatic test generation and more.

`pip install tdda` · installs (wheel) · licence: MIT · rank 7472 · last release 2026-07-13 · [PyPI](https://pypi.org/project/tdda/)

<details><summary>README extract</summary>

The `tdda` package provides Python support for
test-driven data analysis
(1-page summary,
blog,
book).

Features:
- Reference Testing (`tdda.referencetest`): extensions to `unittest` and
 `pytest` for testing data analysis pipelines. Supports file-based
 comparisons, semantic equivalence, automatic rewriting of reference results,
 and test tagging. ...

Sections: Test-Driven Data Analysis (TDDA), Features, Documentation, Resources

</details>

### toolbox-adk

Agent Development Kit Integration for MCP Toolbox

`pip install toolbox-adk` · installs (wheel) · licence: Apache Software License · rank 7485 · last release 2026-09-01 · [PyPI](https://pypi.org/project/toolbox-adk/) · [source](https://github.com/googleapis/mcp-toolbox-sdk-python.git)

<details><summary>README extract</summary>

This package allows Google ADK (Agent Development Kit) agents to natively use tools from the MCP Toolbox.

For detailed guides, authentication examples, and advanced configuration, visit the Python SDK ADK Guide.

Sections: MCP Toolbox SDK for ADK, Usage

</details>

### types-aiobotocore-logs

Type annotations for aiobotocore CloudWatchLogs 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-logs` · installs (wheel) · licence: MIT · rank 7487 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-logs/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_logs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-boto3-bedrock-agent

Type annotations for boto3 AgentsforBedrock 1.43.126 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-bedrock-agent` · installs (wheel) · licence: MIT · rank 7512 · last release 2026-11-06 · [PyPI](https://pypi.org/project/types-boto3-bedrock-agent/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 AgentsforBedrock 1.43.126 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-bedrock-agent docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-boto3-sagemaker-runtime

Type annotations for boto3 SageMakerRuntime 1.43.68 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-sagemaker-runtime` · installs (wheel) · licence: MIT · rank 7513 · last release 2026-08-10 · [PyPI](https://pypi.org/project/types-boto3-sagemaker-runtime/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_runtime/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 SageMakerRuntime 1.43.68 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-sagemaker-runtime docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-django-filter

Typing stubs for django-filter

`pip install types-django-filter` · installs (wheel) · licence: Apache-2.0 · rank 7584 · last release 2026-11-07 · [PyPI](https://pypi.org/project/types-django-filter/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `django-filter` package. It can be used by type checkers
to check code that uses `django-filter`. This version of
`types-django-filter` aims to provide accurate annotations for
`django-filter==26.2.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tos

Volc TOS (Tinder Object Storage) SDK

`pip install tos` · installs from source (sdist only) · licence: not stated · rank 7595 · last release 2026-09-20 · [PyPI](https://pypi.org/project/tos/)

<details><summary>README extract</summary>

The TOS Python SDK enables Python developers to easily work with TOS(Tinder Object Storage) service in the volcengine.
This document will show developers some basic examples about TOS bucket and object operation.

Example:
```python
import tos

ak = "your access key"
sk = "your secret key"
endpoint = "your endpoint"
region = "your region"
bucket_name = "your bucket name"
object_key = "your object key"
client = tos.TosClientV2(ak, sk, endpoint, region)
```

Sections: Volcengine TOS SDK for Python, Requirements, Quick Start, Create a TOS Client, Use VKE IRSA, Use clients with fork, Create a bucket, Put Object, Get Object, Delete Object

</details>

### types-boto3-events

Type annotations for boto3 EventBridge 1.43.102 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-events` · installs (wheel) · licence: MIT · rank 7609 · last release 2026-09-24 · [PyPI](https://pypi.org/project/types-boto3-events/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_events/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 EventBridge 1.43.102 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-events docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-aiobotocore-elbv2

Type annotations for aiobotocore ElasticLoadBalancingv2 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-elbv2` · installs (wheel) · licence: MIT · rank 7614 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-elbv2/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elbv2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### tushare

A utility for crawling historical and Real-time Quotes data of China stocks

`pip install tushare` · installs (wheel) · licence: BSD License · rank 7628 · last release 2026-03-25 · [PyPI](https://pypi.org/project/tushare/)

<details><summary>README extract</summary>

.. image::
 :target:

.. image::
 :target:

* easy to use as most of the data returned are pandas DataFrame objects
* can be easily saved as csv, excel or json files
* can be inserted into MySQL or Mongodb

Target Users ...

</details>

### tardis-dev

Python client for tardis.dev - historical tick-level cryptocurrency market data replay API.

`pip install tardis-dev` · installs (wheel) · licence: MPL-2.0 · rank 7630 · last release 2026-10-28 · [PyPI](https://pypi.org/project/tardis-dev/)

<details><summary>README extract</summary>

Python `tardis-dev` package provides convenient access to tick-level historical cryptocurrency market data in exchange-native format. It focuses on two primary workflows: replaying historical market data and downloading historical market data as CSV files. ...

Features:
- historical tick-level market data replay backed by Tardis.dev HTTP API

- historical market data downloads as CSV files

- support for many cryptocurrency exchanges — see docs.tardis.dev for the full list

Example:
```python
import asyncio
from tardis_dev import Channel, replay

async def main():
    async for local_timestamp, message in replay(
        exchange="binance",
        from_date="2024-03-01",
        to_date="2024-03-02",
        filters=[Channel("trade", ["btcusdt"]), Channel("depth", ["btcusdt"])],
...

</details>

### testcontainers-core

Core component of testcontainers-python.

`pip install testcontainers-core` · installs (wheel) · licence: not stated · rank 7634 · last release 2023-01-06 · [PyPI](https://pypi.org/project/testcontainers-core/)

### tfparse

Python HCL/Terraform parser via extension for AquaSecurity defsec

`pip install tfparse` · installs (wheel) · licence: Apache-2.0 · rank 7694 · last release 2026-09-22 · [PyPI](https://pypi.org/project/tfparse/)

<details><summary>README extract</summary>

A python extension for parsing and evaluating terraform using defsec.

While terraform uses HCL as its configuration format, it requires numerous
forms of variable interpolation, function and expression evaluation, which
is beyond the typical usage of an hcl parser. ...

Example:
```python
from tfparse import load_from_path
parsed = load_from_path('path_to_terraform_root')
print(parsed.keys())
```

Sections: What, Usage, Building from source, Running the tests

</details>

### types-aiobotocore-iam

Type annotations for aiobotocore IAM 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-iam` · installs (wheel) · licence: MIT · rank 7726 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-iam/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iam/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### typer-injector

Dependency injection for typer

`pip install typer-injector` · installs (wheel) · licence: MIT · rank 7748 · last release 2026-04-29 · [PyPI](https://pypi.org/project/typer-injector/) · [docs](https://github.com/BenjyWiener/typer-injector#readme) · [source](https://github.com/BenjyWiener/typer-injector)

<details><summary>README extract</summary>

`typer-injector` adds FastAPI-style dependency injection to Typer.

Example:
```python
import socket
from typing import Annotated, TypeAlias

import typer
from typer_injector import Depends, InjectingTyper

app = InjectingTyper()

def address_dependency(
    host: Annotated[str, typer.Option()],
    port: Annotated[int, typer.Option()],
) -> tuple[str, int]:
    return host, port

...
```

Sections: typer-injector, Usage

</details>

### types-boto3-cognito-idp

Type annotations for boto3 CognitoIdentityProvider 1.43.108 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-cognito-idp` · installs (wheel) · licence: MIT · rank 7759 · last release 2026-10-02 · [PyPI](https://pypi.org/project/types-boto3-cognito-idp/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CognitoIdentityProvider 1.43.108
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-cognito-idp docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### torchtune

A native-PyTorch library for LLM fine-tuning

`pip install torchtune` · installs (wheel) · licence: not stated · rank 7768 · last release 2025-04-07 · [PyPI](https://pypi.org/project/torchtune/) · [docs](https://pytorch.org/torchtune/main/index.html) · [source](https://github.com/pytorch/torchtune)

<details><summary>README extract</summary>

Overview | Installation | Get Started | Documentation | Community | Citing torchtune | License

* *February 2025*: Multi-node training is officially open for business in torchtune! Full finetune on multiple nodes to take advantage of larger batch sizes and models. ...

Features:
torchtune is a PyTorch library for easily authoring, post-training, and experimenting with LLMs. It provides:

- Hackable training recipes for SFT, knowledge distillation, DPO, PPO, GRPO, and quantization-aware training ...

...

</details>

### tiktok-business-api-sdk-official

TikTok Business API SDK

`pip install tiktok-business-api-sdk-official` · installs (wheel) · licence: MIT License · rank 7880 · last release 2026-02-27 · [PyPI](https://pypi.org/project/tiktok-business-api-sdk-official/)

<details><summary>README extract</summary>

Comprehensive collection of client libraries that enable our developers to build software to integrate with Business API faster and in a more standardized way.

This Python package is automatically generated by the Swagger Codegen project:

- API version: 1.2.1

Python 2.7 and 3.4+

Example:
```python
from future import print_function
import time
import business_api_client
from business_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = business_api_client.APPManagementApi(business_api_client.ApiClient(configuration))
...
```

Sections: TikTok Business API SDK - Python, Requirements., Getting Started, Documentation for API Endpoints, Documentation For Models

</details>

### trie

Python implementation of the Ethereum Trie structure

`pip install trie` · installs (wheel) · licence: MIT · rank 7915 · last release 2026-08-22 · [PyPI](https://pypi.org/project/trie/) · [source](https://github.com/ApeWorX/py-trie.git)

<details><summary>README extract</summary>

> This library and repository was previously located at pipermerriam/py-trie. It was transferred to the Ethereum foundation GitHub in
> November 2017 and renamed to `py-trie`.

Read more in the documentation below.

View the change log.

Example:
```python
>>> from trie import HexaryTrie
>>> t = HexaryTrie(db={})
>>> t.root_hash
b'V\xe8\x1f\x17\x1b\xccU\xa6\xff\x83E\xe6\x92\xc0\xf8n[H\xe0\x1b\x99l\xad\xc0\x01b/\xb5\xe3c\xb4!'
>>> t.set(b'my-key', b'some-value')
>>> t.get(b'my-key')
b'some-value'
>>> t.exists(b'another-key')
False
>>> t.set(b'another-key', b'another-value')
...
```

Sections: Python Implementation of the Ethereum Trie structure, Running the tests, Usage, Traversing (inspecting trie internals), Walking a full trie, BinaryTrie, BinaryTrie branch and witness helper functions

</details>

### treq

High-level Twisted HTTP Client API

`pip install treq` · installs (wheel) · licence: MIT · rank 7932 · last release 2026-07-02 · [PyPI](https://pypi.org/project/treq/) · [docs](https://treq.readthedocs.io/) · [source](https://github.com/twisted/treq)

<details><summary>README extract</summary>

`treq` is an HTTP library inspired by
requests but written on top of
Twisted's
Agents.

It provides a simple, higher level API for making HTTP requests when
using Twisted.

For more info read the docs.

Example:
```python
>>> import treq

>>> async def main(reactor):
...     response = await treq.get("
...     print(response.code)
...     body = await response.text()
...     print("<!DOCTYPE html>" in body)

>>> from twisted.internet.task import react
>>> react(main)
200
True
```

</details>

### types-aiobotocore-lite

Lite type annotations for aiobotocore 3.10.0 generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-lite` · installs (wheel) · licence: MIT · rank 7945 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-lite/) · [docs](https://youtype.github.io/types_aiobotocore_docs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, How it works, What's new, Implemented features

</details>

### types-aiobotocore-kinesis

Type annotations for aiobotocore Kinesis 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-kinesis` · installs (wheel) · licence: MIT · rank 7964 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-kinesis/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### tqdm-joblib

Tracking progress of joblib.Parallel execution

`pip install tqdm-joblib` · installs (wheel) · licence: CC-BY-SA-4.0 · rank 7989 · last release 2025-08-17 · [PyPI](https://pypi.org/project/tqdm-joblib/) · [source](https://github.com/louisabraham/tqdm_joblib)

_README extract left out: share-alike licence._

### torchrunx

Automatically initialize distributed PyTorch environments

`pip install torchrunx` · installs (wheel) · licence: not stated · rank 8022 · last release 2026-08-04 · [PyPI](https://pypi.org/project/torchrunx/) · [docs](https://torchrun.xyz) · [source](https://github.com/apoorvkh/torchrunx.git)

<details><summary>README extract</summary>

By Apoorv Khandelwal and Peter Curtin

The easiest way to run PyTorch on multiple GPUs or machines.

`torchrunx` is a *functional* utility for distributing PyTorch code across devices. This is a more convenient, robust, and featureful alternative to CLI-based launchers, like `torchrun`, `accelerate launch`, and `deepspeed`. ...

Example:
```python
def distributed_training(output_dir: str, num_steps: int = 10) -> str:
    # returns path to model checkpoint
```

Sections: torchrunx 🔥, Example: simple training loop

</details>

### types-braintree

Typing stubs for braintree

`pip install types-braintree` · installs (wheel) · licence: Apache-2.0 · rank 8026 · last release 2026-09-28 · [PyPI](https://pypi.org/project/types-braintree/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `braintree` package. It can be used by type checkers
to check code that uses `braintree`. This version of
`types-braintree` aims to provide accurate annotations for
`braintree==4.47.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-aiobotocore-events

Type annotations for aiobotocore EventBridge 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-events` · installs (wheel) · licence: MIT · rank 8030 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-events/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_events/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-seaborn

Typing stubs for seaborn

`pip install types-seaborn` · installs (wheel) · licence: Apache-2.0 · rank 8031 · last release 2026-11-07 · [PyPI](https://pypi.org/project/types-seaborn/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `seaborn` package. It can be used by type checkers
to check code that uses `seaborn`. This version of
`types-seaborn` aims to provide accurate annotations for
`seaborn==0.13.2`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-aiobotocore-dataexchange

Type annotations for aiobotocore DataExchange 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-dataexchange` · installs (wheel) · licence: MIT · rank 8039 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-dataexchange/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dataexchange/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-zstd

Typing stubs for zstd

`pip install types-zstd` · installs (wheel) · licence: Apache-2.0 · rank 8075 · last release 2026-07-22 · [PyPI](https://pypi.org/project/types-zstd/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `zstd` package. It can be used by type checkers
to check code that uses `zstd`. This version of
`types-zstd` aims to provide accurate annotations for
`zstd~=1.5.7.3`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

</details>

### types-aiobotocore-elasticache

Type annotations for aiobotocore ElastiCache 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-elasticache` · installs (wheel) · licence: MIT · rank 8134 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-elasticache/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticache/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-grpcio-health-checking

Typing stubs for grpcio-health-checking

`pip install types-grpcio-health-checking` · installs (wheel) · licence: Apache-2.0 · rank 8164 · last release 2026-10-29 · [PyPI](https://pypi.org/project/types-grpcio-health-checking/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `grpcio-health-checking` package. It can be used by type checkers
to check code that uses `grpcio-health-checking`. This version of
`types-grpcio-health-checking` aims to provide accurate annotations for
`grpcio-health-checking==1.85.*`.

This package is part of the typeshed project. ...

</details>

### types-aiobotocore-bedrock

Type annotations for aiobotocore Bedrock 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-bedrock` · installs (wheel) · licence: MIT · rank 8177 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-bedrock/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### taktile-auth

Auth Package for Taktile

`pip install taktile-auth` · installs (wheel) · licence: Apache Software License · rank 8229 · last release 2026-11-02 · [PyPI](https://pypi.org/project/taktile-auth/)

<details><summary>README extract</summary>

This package is part of the Taktile ecosystem.

Taktile enables data science teams to industrialize, scale, and maintain machine learning models. Our ML development platform makes it easy to create your own end-to-end ML applications:

- Turn models into auto-scaling APIs in a few lines of code
- Easily add model tests ...

</details>

### types-pyperclip

Typing stubs for pyperclip

`pip install types-pyperclip` · installs (wheel) · licence: Apache-2.0 · rank 8249 · last release 2026-05-08 · [PyPI](https://pypi.org/project/types-pyperclip/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `pyperclip` package. It can be used by type checkers
to check code that uses `pyperclip`. This version of
`types-pyperclip` aims to provide accurate annotations for
`pyperclip==1.11.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-gunicorn

Typing stubs for gunicorn

`pip install types-gunicorn` · installs (wheel) · licence: Apache-2.0 · rank 8274 · last release 2026-10-08 · [PyPI](https://pypi.org/project/types-gunicorn/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `gunicorn` package. It can be used by type checkers
to check code that uses `gunicorn`. This version of
`types-gunicorn` aims to provide accurate annotations for
`gunicorn==26.2.0`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

Sections: Typing stubs for gunicorn, Optional dependencies

</details>

### types-boto3-logs

Type annotations for boto3 CloudWatchLogs 1.43.125 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-logs` · installs (wheel) · licence: MIT · rank 8290 · last release 2026-11-06 · [PyPI](https://pypi.org/project/types-boto3-logs/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_logs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CloudWatchLogs 1.43.125 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-logs docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### tclint

A CLI utility for linting and analyzing Tcl code.

`pip install tclint` · installs (wheel) · licence: MIT License · rank 8372 · last release 2026-08-01 · [PyPI](https://pypi.org/project/tclint/)

<details><summary>README extract</summary>

`tclint` is a collection of modern dev tools for Tcl. It includes a linter, a formatter, and a language server that provides Tcl support to your editor of choice.

Features:
- Editor integration for VS Code, Neovim, and Emacs
- Linting for common Tcl errors
- Formatter that enforces a consistent, readable style
- Plugin system that supports Tcl variants
- More features coming soon!

Sections: tclint &nbsp;, Features, Getting Started, Example, Usage

</details>

### tensordict-nightly

A dict[str, torch.Tensor] that behaves like one tensor.

`pip install tensordict-nightly` · installs (wheel) · licence: MIT · rank 8376 · last release 2026-11-07 · [PyPI](https://pypi.org/project/tensordict-nightly/) · [docs](https://docs.pytorch.org/tensordict/stable/)

<details><summary>README extract</summary>

A `dict[str, torch.Tensor]` that behaves like one tensor.

PyTorch code that handles groups of tensors, such as a training batch, a
particle system, or a batch of graphs, usually repeats every operation for
every tensor, and nested dicts need recursion. A TensorDict holds the group as
one object: ...

Example:
```python
import torch
from tensordict import TensorDict, lazy_stack

episodes = [TensorDict({"obs": torch.randn(n, 4)}, batch_size=[n]) for n in (3, 5, 2)]
batch = lazy_stack(episodes)      # keeps each sample as it is
print(batch.batch_size)           # torch.Size([3, -1]): -1 marks the dimension that varies
print(batch1.shape)      # torch.Size([5, 4])
...
```

Sections: TensorDict, More examples, FAQ, Documentation

</details>

### toppra

toppra: time-optimal parametrization of trajectories for robots subject to constraints.

`pip install toppra` · installs (wheel) · licence: MIT · rank 8404 · last release 2026-11-05 · [PyPI](https://pypi.org/project/toppra/)

<details><summary>README extract</summary>

toppra is a library for computing the time-optimal path parametrization for robots subject to kinematic and dynamic constraints.

Refer to the GitHub repo or full documentation for more information.

</details>

### types-pyfarmhash

Typing stubs for pyfarmhash

`pip install types-pyfarmhash` · installs (wheel) · licence: Apache-2.0 · rank 8424 · last release 2026-08-19 · [PyPI](https://pypi.org/project/types-pyfarmhash/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `pyfarmhash` package. It can be used by type checkers
to check code that uses `pyfarmhash`. This version of
`types-pyfarmhash` aims to provide accurate annotations for
`pyfarmhash==0.5.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tensorrt-cu13

A high performance deep learning inference library

`pip install tensorrt-cu13` · installs from source (sdist only) · licence: Other/Proprietary License · rank 8455 · last release 2026-10-08 · [PyPI](https://pypi.org/project/tensorrt-cu13/)

<details><summary>README extract</summary>

NVIDIA TensorRT is an SDK that facilitates high-performance machine learning inference. It is designed to work in a complementary fashion with training frameworks such as PyTorch. It focuses specifically on running an already-trained network quickly and efficiently on NVIDIA hardware.

</details>

### types-aiobotocore-eks

Type annotations for aiobotocore EKS 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-eks` · installs (wheel) · licence: MIT · rank 8460 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-eks/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-grpcio-status

Typing stubs for grpcio-status

`pip install types-grpcio-status` · installs (wheel) · licence: Apache-2.0 · rank 8533 · last release 2026-04-08 · [PyPI](https://pypi.org/project/types-grpcio-status/) · [source](https://github.com/python/typeshed)

### types-waitress

Typing stubs for waitress

`pip install types-waitress` · installs (wheel) · licence: Apache-2.0 · rank 8555 · last release 2026-07-24 · [PyPI](https://pypi.org/project/types-waitress/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `waitress` package. It can be used by type checkers
to check code that uses `waitress`. This version of
`types-waitress` aims to provide accurate annotations for
`waitress~=3.0.1`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-SQLAlchemy

Typing stubs for SQLAlchemy

`pip install types-SQLAlchemy` · installs (wheel) · licence: Apache Software License · rank 8573 · last release 2023-05-01 · [PyPI](https://pypi.org/project/types-SQLAlchemy/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `SQLAlchemy` package. It
can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`SQLAlchemy`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### tensorrt-cu13-libs

TensorRT Libraries

`pip install tensorrt-cu13-libs` · installs from source (sdist only) · licence: Other/Proprietary License · rank 8579 · last release 2026-10-08 · [PyPI](https://pypi.org/project/tensorrt-cu13-libs/)

### trcli

(no summary)

`pip install trcli` · installs (wheel) · licence: not stated · rank 8592 · last release 2026-10-30 · [PyPI](https://pypi.org/project/trcli/)

<details><summary>README extract</summary>

The TR CLI (trcli) is a command line tool for interacting with TestRail and uploading test automation results.

</details>

### type-enforced

A dependency free type enforcer for python type annotations

`pip install type-enforced` · installs (wheel) · licence: MIT License · rank 8617 · last release 2026-10-23 · [PyPI](https://pypi.org/project/type-enforced/) · [docs](https://connor-makowski.github.io/type_enforced/type_enforced/enforcer.html)

<details><summary>README extract</summary>

Fast where it counts, thorough where it matters. Runtime validation for Python type annotations. Zero dependencies and uncompromising performance.

Features:
Static type checkers (like `mypy` or `pyright`) catch errors during development, but offer zero protection at runtime against dynamic payloads, untyped API inputs, or user data.

Existing runtime type checkers force an unnecessary compromise: ...

Example:
```python
import type_enforced

# 1. Complete validation
@type_enforced.Enforcer
def greet(name: list[str], repeat: int = 1) -> str:
    return f"Hello {', '.join(name)}!" * repeat

greet(["Alice"], 2)       # Returns "Hello Alice!Hello Alice!"
greet(["Alice"], "twice")  # Raises TypeError at runtime!

...
```

...

</details>

### types-aiobotocore-route53

Type annotations for aiobotocore Route53 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-route53` · installs (wheel) · licence: MIT · rank 8630 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-route53/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-aiobotocore-batch

Type annotations for aiobotocore Batch 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-batch` · installs (wheel) · licence: MIT · rank 8634 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-batch/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_batch/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### tinynetrc

Read and write .netrc files.

`pip install tinynetrc` · installs (wheel) · licence: MIT License · rank 8666 · last release 2021-08-15 · [PyPI](https://pypi.org/project/tinynetrc/)

<details><summary>README extract</summary>

Read and write .netrc files in Python.

`tinynetrc` uses the netrc
module from the standard library under the hood and adds a few
improvements:

* Adds write functionality.
* Fixes a std lib bug with
 formatting a .netrc file.*
* Parses .netrc into dictionary values rather than tuples.

\*This bug is fixed in newer versions of Python. ...

Example:
```python
from tinynetrc import Netrc

netrc = Netrc()  # parse ~/.netrc
# Get credentials
netrc'api.heroku.com'
netrc'api.heroku.com'

# Modify an existing entry
netrc'api.heroku.com' = 'newpassword'
netrc.save()  # writes to ~/.netrc

# Add a new entry
netrc['surge.surge.sh'] = {
    'login': 'sloria1@gmail.com',
    'password': 'secret'
}
netrc.save()

...
```

Sections: tinynetrc, Get it now, Usage

</details>

### types-aws-xray-sdk

Typing stubs for aws-xray-sdk

`pip install types-aws-xray-sdk` · installs (wheel) · licence: Apache-2.0 · rank 8670 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-aws-xray-sdk/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `aws-xray-sdk` package. It can be used by type checkers
to check code that uses `aws-xray-sdk`. This version of
`types-aws-xray-sdk` aims to provide accurate annotations for
`aws-xray-sdk==2.16.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-boto3-cloudwatch

Type annotations for boto3 CloudWatch 1.43.116 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-cloudwatch` · installs (wheel) · licence: MIT · rank 8714 · last release 2026-10-20 · [PyPI](https://pypi.org/project/types-boto3-cloudwatch/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_cloudwatch/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CloudWatch 1.43.116 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-cloudwatch docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### timing-asgi

ASGI middleware to emit timing metrics with something like statsd

`pip install timing-asgi` · installs (wheel) · licence: not stated · rank 8742 · last release 2026-02-17 · [PyPI](https://pypi.org/project/timing-asgi/) · [source](https://github.com/steinnes/timing-asgi)

<details><summary>README extract</summary>

This is a timing middleware for ASGI, useful for automatic instrumentation of ASGI endpoints.

This was developed at GRID for use with our backend services which are built using
python and the ASGI framework Starlette, and intended to emit metrics to Datadog,
a statsd-based cloud monitoring service. ...

Example:
```python
import logging
import uvicorn

from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from timing_asgi import TimingMiddleware, TimingClient
from timing_asgi.integrations import StarletteScopeToName

class PrintTimings(TimingClient):
    def timing(self, metric_name, timing, tags):
...
```

Sections: timing-asgi, ASGI version, usage

</details>

### types-geopandas

Typing stubs for geopandas

`pip install types-geopandas` · installs (wheel) · licence: Apache-2.0 · rank 8797 · last release 2026-11-07 · [PyPI](https://pypi.org/project/types-geopandas/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `geopandas` package. It can be used by type checkers
to check code that uses `geopandas`. This version of
`types-geopandas` aims to provide accurate annotations for
`geopandas==1.2.0`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-chevron

Typing stubs for chevron

`pip install types-chevron` · installs (wheel) · licence: Apache-2.0 · rank 8855 · last release 2026-04-08 · [PyPI](https://pypi.org/project/types-chevron/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `chevron` package. It can be used by type checkers
to check code that uses `chevron`. This version of
`types-chevron` aims to provide accurate annotations for
`chevron==0.14.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-filelock

Typing stubs for filelock

`pip install types-filelock` · installs (wheel) · licence: Apache Software License · rank 8976 · last release 2022-06-09 · [PyPI](https://pypi.org/project/types-filelock/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `filelock` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `filelock`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### traia-iatp

Inter-Agent Transfer Protocol (IATP) - Enable AI Agents to utilize other AI Agents as tools

`pip install traia-iatp` · installs (wheel) · licence: not stated · rank 9032 · last release 2026-05-05 · [PyPI](https://pypi.org/project/traia-iatp/) · [docs](https://docs.d402.net) · [source](https://github.com/Traia-IO/IATP)

<details><summary>README extract</summary>

Example:
```python
from fastapi import FastAPI
from traia_iatp.d402.servers.fastapi import D402FastAPIMiddleware
from traia_iatp.d402.price_builder import D402PriceBuilder

app = FastAPI()

# Add D402 (5 lines)
price_builder = D402PriceBuilder(network="sepolia")
d402 = D402FastAPIMiddleware(server_address="0x...", facilitator_url="
...
```

Sections: 🚀 Quick Start, Add D402 to Your FastAPI Server (5 lines), Call D402-Protected Servers (2 lines), 📚 Documentation, Quick Links, Complete Integration Examples, 🌟 Key Features, Server Integration, Client Integration, MCP & A2A, 🔧 What's in the Package, Core Components (IN pip package), Examples (NOT in pip package), Documentation (NOT in pip package)

</details>

### tensorrt-cu13-bindings

A high performance deep learning inference library

`pip install tensorrt-cu13-bindings` · installs (wheel) · licence: Other/Proprietary License · rank 9033 · last release 2026-10-08 · [PyPI](https://pypi.org/project/tensorrt-cu13-bindings/)

<details><summary>README extract</summary>

A high performance deep learning inference library

</details>

### tenant-schemas-celery

Celery integration for django-tenant-schemas and django-tenants

`pip install tenant-schemas-celery` · installs (wheel) · licence: MIT License · rank 9070 · last release 2026-08-01 · [PyPI](https://pypi.org/project/tenant-schemas-celery/)

<details><summary>README extract</summary>

Celery application implementation that allows celery tasks to cooperate with the
django-tenants package.

This project might not seem frequently updated, but it just has all the functionality needed. Issues and questions are answered quickly.

Installation

Usage

 * Define a celery app using given `CeleryApp` class. ...

Example:
```python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

from django.conf import settings

from tenant_schemas_celery.app import CeleryApp as TenantAwareCeleryApp

app = TenantAwareCeleryApp()
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
```

...

</details>

### tetgen

Python interface to tetgen

`pip install tetgen` · installs (wheel) · licence: MIT · rank 9081 · last release 2026-05-04 · [PyPI](https://pypi.org/project/tetgen/) · [docs](https://tetgen.pyvista.org/) · [source](https://github.com/pyvista/tetgen)

<details><summary>README extract</summary>

This Python library is an interface to Hang Si's TetGen C++ software. This module combines
speed of C++ with the portability and ease of installation of Python
along with integration to PyVista for 3D
visualization and analysis. See the TetGen GitHub page for more details on the
underlying software. ...

Example:
```python
import pyvista as pv
import tetgen
import numpy as np
pv.set_plot_theme('document')

sphere = pv.Sphere()
tet = tetgen.TetGen(sphere)
tet.tetrahedralize(order=1, mindihedral=20, minratio=1.5)
grid = tet.grid
grid.plot(show_edges=True)
```

Sections: tetgen, Basic Example, Using a Background Mesh, . Prepare Your PLC and Background Mesh, . Define the Sizing Function and Write to Disk, . Use TetGen with the Background Mesh

</details>

### tabpfn-common-utils

Utilities shared between TabPFN codebases

`pip install tabpfn-common-utils` · installs (wheel) · licence: Apache Software License · rank 9095 · last release 2026-06-22 · [PyPI](https://pypi.org/project/tabpfn-common-utils/)

<details><summary>README extract</summary>

Shared Python utilities used across the TabPFN ecosystem (the tabular foundation model).

Example:
```python
from tabpfn_common_utils.regression_pred_result import RegressionPredictResult

# Handle regression prediction results
result = RegressionPredictResult({
    "mean": [1.2, 2.3, 3.4],
    "median": [1.1, 2.2, 3.3],
    "mode": [1.0, 2.0, 3.0],
    "quantile_0.25": [0.9, 1.9, 2.9],
    "quantile_0.75": [1.5, 2.5, 3.5]
})

...
```

Sections: TabPFN Common Utilities, Features, Data Processing Utilities, Cost Estimation, Telemetry (optional, opt-out), Quick Start, Regression Results, Data Utilities, Telemetry, Telemetry notes, Setup, Adding Dependencies, Links

</details>

### types-polib

Typing stubs for polib

`pip install types-polib` · installs (wheel) · licence: Apache-2.0 · rank 9189 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-polib/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `polib` package. It can be used by type checkers
to check code that uses `polib`. This version of
`types-polib` aims to provide accurate annotations for
`polib==1.2.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

</details>

### talon

Mailgun library to extract message quotations and signatures.

`pip install talon` · installs from source (sdist only) · licence: APACHE2 · rank 9229 · last release 2017-08-24 · [PyPI](https://pypi.org/project/talon/)

<details><summary>README extract</summary>

Mailgun library to extract message quotations and signatures.

If you ever tried to parse message quotations or signatures you know that absence of any formatting standards in this area could make this task a nightmare. Hopefully this library will make your life much easier. ...

Example:
```python
import talon
from talon import quotations

talon.init()

text =  """Reply

-----Original Message-----

Quote"""

reply = quotations.extract_from(text, 'text/plain')
reply = quotations.extract_from_plain(text)
# reply == "Reply"
```

Sections: talon, Usage, Open-source Dataset, Research

</details>

### timeout-sampler

Timeout utility class to wait for any function output and interact with it in given time

`pip install timeout-sampler` · installs from source (sdist only) · licence: Apache-2.0 · rank 9315 · last release 2026-11-03 · [PyPI](https://pypi.org/project/timeout-sampler/) · [source](https://github.com/RedHatQE/timeout-sampler)

<details><summary>README extract</summary>

Utility class for waiting to any function output and interact with it in given time.

📖 Full Documentation

Example:
```python
from random import randint
from timeout_sampler import TimeoutSampler

def random_number(start, end):
    if isinstance(start, str) or isinstance(end, str):
        raise TypeError("start and end must be int type")

    if end <= start:
        raise ValueError("End must be greater than start")

    return randint(start, end)

...
```

Sections: TimeoutSampler, Usage

</details>

### trec-car-tools

Support tools for TREC CAR participants. Also see trec-car.cs.unh.edu

`pip install trec-car-tools` · installs (wheel) · licence: BSD 3-Clause · rank 9365 · last release 2022-02-01 · [PyPI](https://pypi.org/project/trec-car-tools/)

### types-attrs

Typing stubs for attrs

`pip install types-attrs` · installs (wheel) · licence: Apache Software License · rank 9397 · last release 2021-06-06 · [PyPI](https://pypi.org/project/types-attrs/)

<details><summary>README extract</summary>

This is an auto-generated PEP 561 type stub package for `attrs` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `attrs`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-aiobotocore-securityhub

Type annotations for aiobotocore SecurityHub 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-securityhub` · installs (wheel) · licence: MIT · rank 9411 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-securityhub/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_securityhub/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### tf-models-nightly

TensorFlow Official Models

`pip install tf-models-nightly` · installs (wheel) · licence: Apache 2.0 · rank 9455 · last release 2026-02-17 · [PyPI](https://pypi.org/project/tf-models-nightly/)

<details><summary>README extract</summary>

The TensorFlow official models are a collection of
models that use TensorFlow's high-level APIs.
They are intended to be well-maintained, tested, and kept up to date with the
latest TensorFlow API. They should also be reasonably optimized for fast
performance while still being easy to read.

</details>

### tbump

Bump software releases

`pip install tbump` · installs (wheel) · licence: BSD License · rank 9473 · last release 2023-09-09 · [PyPI](https://pypi.org/project/tbump/) · [source](https://github.com/dmerejkowsky/tbump)

<details><summary>README extract</summary>

Sections: Note, Screenshot, Usage, Advanced configuration, Command-line options, Restricting the lines that are replaced, Using a custom version template, Running commands before commit, Running commands after push, Setting default values for version fields

</details>

### types-WTForms

Typing stubs for WTForms

`pip install types-WTForms` · installs (wheel) · licence: Apache-2.0 · rank 9500 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-WTForms/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `WTForms` package. It can be used by type checkers
to check code that uses `WTForms`. This version of
`types-WTForms` aims to provide accurate annotations for
`WTForms==3.3.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tlparse

Parse TORCH_LOG logs produced by PyTorch torch.compile

`pip install tlparse` · installs (wheel) · licence: BSD-3-Clause · rank 9514 · last release 2025-09-12 · [PyPI](https://pypi.org/project/tlparse/) · [source](https://github.com/ezyang/tlparse)

<details><summary>README extract</summary>

`tlparse` parses structured torch trace logs and outputs HTML files analyzing data.

Quick start:
Run PT2 with the TORCH_TRACE environment variable set:

Feed input into tlparse:

You can extend tlparse with custom parsers which take existing structured log data and output any file. To do so, first implement StructuredLogParser with your own trait:

Sections: tlparse: Parse structured PT2 logs, Adding custom parsers

</details>

### types-boto3-elbv2

Type annotations for boto3 ElasticLoadBalancingv2 1.43.88 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-elbv2` · installs (wheel) · licence: MIT · rank 9533 · last release 2026-09-03 · [PyPI](https://pypi.org/project/types-boto3-elbv2/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_elbv2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ElasticLoadBalancingv2 1.43.88
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-elbv2 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### theine_core

(no summary)

`pip install theine_core` · installs (wheel) · licence: BSD-3-Clause · rank 9586 · last release 2026-03-18 · [PyPI](https://pypi.org/project/theine_core/)

### tpu-info

CLI tool to view TPU metrics

`pip install tpu-info` · installs (wheel) · licence: Apache-2.0 · rank 9612 · last release 2026-07-06 · [PyPI](https://pypi.org/project/tpu-info/) · [source](https://github.com/AI-Hypercomputer/cloud-accelerator-diagnostics)

<details><summary>README extract</summary>

<!--
 Copyright 2023 Google LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at ...

Example:
```python
# JAX
>>> import jax
>>> jax.device_count()
4
# Create a tensor on the TPU
>>> t = jax.numpy.ones((300, 300))

# PyTorch/XLA
>>> import torch
>>> import torch_xla
>>> t = torch.randn((300, 300), device=torch_xla.device())
```

Sections: `tpu-info` CLI, What's New in Version 0.14.2, Usage, Static Mode, Streaming Mode, Version, Compatible Environment, Incompatible Environment (Python 3.12+), Process, List Metrics, Metric

</details>

### types-aiobotocore-textract

Type annotations for aiobotocore Textract 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-textract` · installs (wheel) · licence: MIT · rank 9685 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-textract/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_textract/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-backports

Typing stubs for backports

`pip install types-backports` · installs (wheel) · licence: Apache Software License · rank 9745 · last release 2021-06-17 · [PyPI](https://pypi.org/project/types-backports/)

<details><summary>README extract</summary>

This is an auto-generated PEP 561 type stub package for `backports` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `backports`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there.

See for more details. ...

</details>

### types-mysqlclient

Typing stubs for mysqlclient

`pip install types-mysqlclient` · installs (wheel) · licence: Apache-2.0 · rank 9753 · last release 2026-09-23 · [PyPI](https://pypi.org/project/types-mysqlclient/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `mysqlclient` package. It can be used by type checkers
to check code that uses `mysqlclient`. This version of
`types-mysqlclient` aims to provide accurate annotations for
`mysqlclient==2.3.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-grpcio-reflection

Typing stubs for grpcio-reflection

`pip install types-grpcio-reflection` · installs (wheel) · licence: Apache-2.0 · rank 9767 · last release 2026-05-08 · [PyPI](https://pypi.org/project/types-grpcio-reflection/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `grpcio-reflection` package. It can be used by type checkers
to check code that uses `grpcio-reflection`. This version of
`types-grpcio-reflection` aims to provide accurate annotations for
`grpcio-reflection==1.*`.

This package is part of the typeshed project. ...

</details>

### types-aioboto3-lite

Lite type annotations for aioboto3 15.5.0 generated with mypy-boto3-builder 8.11.0

`pip install types-aioboto3-lite` · installs (wheel) · licence: MIT License · rank 9771 · last release 2025-10-31 · [PyPI](https://pypi.org/project/types-aioboto3-lite/) · [docs](https://youtype.github.io/types_aioboto3_docs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for aioboto3 15.5.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.11.0.

More information can be found on
types-aioboto3 page and in
types-aioboto3-lite docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

...

</details>

### typeapi

(no summary)

`pip install typeapi` · installs (wheel) · licence: MIT · rank 9898 · last release 2025-10-23 · [PyPI](https://pypi.org/project/typeapi/) · [docs](https://niklasrosenstein.github.io/python-typeapi/)

<details><summary>README extract</summary>

The `typeapi` package provides a unified and consistent API for the reflection and introspection of
Python type hints. In addition, it allows evaluating future annotations such as
PEP585 (such as `list[str]`) and
PEP604 (such as `int | str`) in versions that don't
natively support them.

Requirements:

* Python 3.8 or newer ...

</details>

### toolguard

Policy adherence code generation for guarding AI agent tools

`pip install toolguard` · installs (wheel) · licence: Apache Software License · rank 9974 · last release 2026-06-30 · [PyPI](https://pypi.org/project/toolguard/)

<details><summary>README extract</summary>

This tool analyzes policy documents and generates deterministic Python code to enforce operational policies when invoking AI agent tools.
This work is described in EMNLP 2025 Towards Enforcing Company Policy Adherence in Agentic Workflows. ...

Example:
```python
# tools.py
def divide_tool(g: float, h: float) -> float:
    """Divides one number by another."""
    return g / h

def add_tool(a: float, b: float) -> float:
    """Adds two numbers."""
    return a + b

def multiply_tool(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b

def map_kdi_number(i: float) -> float:
...
```

...

</details>

### types-appdirs

Typing stubs for appdirs

`pip install types-appdirs` · installs (wheel) · licence: Apache Software License · rank 9982 · last release 2023-03-14 · [PyPI](https://pypi.org/project/types-appdirs/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `appdirs` package. It
can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`appdirs`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### types-aiobotocore-service-quotas

Type annotations for aiobotocore ServiceQuotas 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-service-quotas` · installs (wheel) · licence: MIT · rank 10060 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-service-quotas/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_service_quotas/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-humanfriendly

Typing stubs for humanfriendly

`pip install types-humanfriendly` · installs (wheel) · licence: Apache Software License · rank 10103 · last release 2025-03-19 · [PyPI](https://pypi.org/project/types-humanfriendly/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561
type stub package for the `humanfriendly` package.
It can be used by type-checking tools like
mypy,
pyright,
pytype,
Pyre,
PyCharm, etc. to check code that uses `humanfriendly`. This version of
`types-humanfriendly` aims to provide accurate annotations for
`humanfriendly==10.0.*`. ...

</details>

### tinyobjloader

Python module for tinyobjloader

`pip install tinyobjloader` · installs from source (sdist only) · licence: MIT License · rank 10119 · last release 2019-05-17 · [PyPI](https://pypi.org/project/tinyobjloader/)

<details><summary>README extract</summary>

`tinyobjloader` is a python wrapper for C++ wavefront .obj loader.
`tinyobjloader` is rather fast and feature rich than other pure python version of .obj loader.

Example:
```python
import sys
import tinyobjloader

# Create reader.
reader = tinyobjloader.ObjReader()

filename = "cornellbox.obj"

# Load .obj(and .mtl) using default configuration
ret = reader.ParseFromFile(filename)

if ret == False:
    print("Warn:", reader.Warning())
    pint("Err:", reader.Error())
    print("Failed to load : ", filename)

    sys.exit(-1)

...
```

Sections: tinyobjloader, Wavefront .obj loader, Quick tutorial, More detailed usage, TODO

</details>

### threadloop

Tornado IOLoop Backed Concurrent Futures

`pip install threadloop` · installs from source (sdist only) · licence: MIT License · rank 10305 · last release 2016-04-01 · [PyPI](https://pypi.org/project/threadloop/)

<details><summary>README extract</summary>

Run Tornado Coroutines from Synchronous Python.

Example:
```python
from threadloop import ThreadLoop
from tornado import gen

@gen.coroutine
def coroutine(greeting="Goodbye"):
    yield gen.sleep(1)
    raise gen.Return("%s World" % greeting)

with ThreadLoop() as threadloop:
    future = threadloop.submit(coroutine, "Hello")

    print future.result() # Hello World
```

</details>

### types-aiobotocore-iot-data

Type annotations for aiobotocore IoTDataPlane 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-iot-data` · installs (wheel) · licence: MIT · rank 10363 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-iot-data/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_data/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### torchft-nightly

(no summary)

`pip install torchft-nightly` · installs (wheel) · licence: not stated · rank 10390 · last release 2026-11-07 · [PyPI](https://pypi.org/project/torchft-nightly/) · [docs](https://meta-pytorch.org/torchft/) · [source](https://github.com/meta-pytorch/torchft)

<details><summary>README extract</summary>

| Documentation
 | Poster
 | Design Doc

This repository implements techniques for doing a per-step fault tolerance so
you can keep training if errors occur without interrupting the entire training
job.

This is based on the large scale training techniques presented at PyTorch
Conference 2024.

Features:
torchft is designed to provide the primitives required to implement fault
tolerance in any application/train script as well as the primitives needed to
implement custom fault tolerance strategies. ...

Example:
```python
from torchft import Manager, DistributedDataParallel, Optimizer, ProcessGroupGloo

manager = Manager(
    pg=ProcessGroupGloo(),
    load_state_dict=...,
    state_dict=...,
)

m = nn.Linear(2, 3)
m = DistributedDataParallel(manager, m)
...

</details>

### tembo-pgmq-python

Python client for the PGMQ Postgres extension.

`pip install tembo-pgmq-python` · installs (wheel) · licence: OSI Approved · rank 10398 · last release 2025-03-31 · [PyPI](https://pypi.org/project/tembo-pgmq-python/) · [docs](https://github.com/tembo-io/pgmq/tree/main/tembo-pgmq-python) · [source](https://github.com/tembo-io/pgmq/tree/main/tembo-pgmq-python)

<details><summary>README extract</summary>

Example:
```python
@transaction
def transactional_operation(queue: PGMQueue, conn=None):
    # Perform multiple queue operations within a transaction
    queue.create_queue("transactional_queue", conn=conn)
    queue.send("transactional_queue", {"message": "Hello, World!"}, conn=conn)
```

Sections: Tembo's Python Client for PGMQ, Usage, Using Environment Variables, Note on the async version, Create a queue, Or create a partitioned queue, List all queues, Send a message, Send a batch of messages, Read a message, set it invisible for 30 seconds, Read a batch of messages, Read messages with polling, Archive the message after we're done with it, Archive a batch of messages

</details>

### types-aiobotocore-iot

Type annotations for aiobotocore IoT 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-iot` · installs (wheel) · licence: MIT · rank 10399 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-iot/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-influxdb-client

Typing stubs for influxdb-client

`pip install types-influxdb-client` · installs (wheel) · licence: Apache Software License · rank 10417 · last release 2024-12-21 · [PyPI](https://pypi.org/project/types-influxdb-client/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561
type stub package for the `influxdb-client` package.
It can be used by type-checking tools like
mypy,
pyright,
pytype,
Pyre,
PyCharm, etc. to check code that uses `influxdb-client`. This version of
`types-influxdb-client` aims to provide accurate annotations for
`influxdb-client==1.45.*`. ...

</details>

### typing-validation

A library to perform runtime validation of Python objects using type hints.

`pip install typing-validation` · installs (wheel) · licence: LGPL-3.0-or-later · rank 10418 · last release 2026-07-18 · [PyPI](https://pypi.org/project/typing-validation/) · [docs](https://typing-validation.readthedocs.io) · [source](https://github.com/hashberg-io/typing-validation)

_README extract left out: share-alike licence._

### types-boto3-lite

Lite type annotations for boto3 1.43.126 generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-lite` · installs (wheel) · licence: MIT · rank 10422 · last release 2026-11-06 · [PyPI](https://pypi.org/project/types-boto3-lite/) · [docs](https://youtype.github.io/types_boto3_docs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 1.43.126
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-lite docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-boto3-textract

Type annotations for boto3 Textract 1.43.69 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-textract` · installs (wheel) · licence: MIT · rank 10432 · last release 2026-08-11 · [PyPI](https://pypi.org/project/types-boto3-textract/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_textract/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Textract 1.43.69
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-textract docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### teptris

TOML for Python at libteptris speed (native C extension, no fallback)

`pip install teptris` · installs (wheel) · licence: MIT · rank 10458 · last release 2026-11-07 · [PyPI](https://pypi.org/project/teptris/) · [source](https://github.com/leptris/teptris-py)

<details><summary>README extract</summary>

**Mission: be the best TOML parser and builder ever made — in C, Ruby,
Rust, and JS — measured, not claimed.** The bar and the family ledger:
BEST-EVER.md.

A native C-extension binding (no ctypes, no fallback) over
libteptris — the TOML counterpart
of leptris-py (XML) and yeptris-py (YAML). ...

Example:
```python
import teptris
teptris.edit('# conf\n[serve]\nport = 8080  # keep\n', 'serve.port', '9090')
# '# conf\n[serve]\nport = 9090  # keep\n'
```

Sections: teptris-py — TOML for Python at libleptris speed, Schema validation (engine 0.3.20+), Performance (end-to-end, Python tier), Packaging, Many-small batch (`loads_batch`), Lazy load (`loads_lazy`), Descriptor (planned-key materialization), Typing

</details>

### types-boto3-cloudfront

Type annotations for boto3 CloudFront 1.43.114 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-cloudfront` · installs (wheel) · licence: MIT · rank 10518 · last release 2026-10-14 · [PyPI](https://pypi.org/project/types-boto3-cloudfront/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_cloudfront/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CloudFront 1.43.114 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-cloudfront docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### tbparse

Load tensorboard event logs as pandas DataFrames; Read, parse, and plot tensorboard event logs with ease!

`pip install tbparse` · installs (wheel) · licence: Apache Software License · rank 10525 · last release 2024-08-16 · [PyPI](https://pypi.org/project/tbparse/) · [source](https://github.com/j3soon/tbparse)

<details><summary>README extract</summary>

A simple yet powerful tensorboard event log parser/reader.

* Supports parsing tensorboard event scalars, tensors, histograms, images, audio, hparams, and text.
* Supports event generated by
 PyTorch, Tensorboard/Keras, and TensorboardX, with their respective usage examples documented in detail. ...

Example:
```python
from tbparse import SummaryReader
log_dir = "<PATH_TO_EVENT_FILE_OR_DIRECTORY>"
reader = SummaryReader(log_dir)
df = reader.scalars
print(df)
```

Sections: tbparse, Gallery

</details>

### transparent-background

Make images with transparent background

`pip install transparent-background` · installs (wheel) · licence: MIT License · rank 10546 · last release 2025-05-14 · [PyPI](https://pypi.org/project/transparent-background/)

<details><summary>README extract</summary>

This is a background removing tool powered by InSPyReNet (ACCV 2022). You can easily remove background from the image or video or bunch of other stuffs when you can make the background transparent!

Image | Video | Webcam
:-:|:-:|:-:
 | |

Example:
```python
import cv2
import numpy as np

from PIL import Image
from transparent_background import Remover

# Load model
remover = Remover() # default setting
remover = Remover(mode='fast', jit=True, device='cuda:0', ckpt='~/latest.pth') # custom setting
remover = Remover(mode='base-nightly') # nightly release checkpoint
...
```

...

</details>

### types-aiobotocore-autoscaling

Type annotations for aiobotocore AutoScaling 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-autoscaling` · installs (wheel) · licence: MIT · rank 10641 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-autoscaling/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_autoscaling/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-boto3-ecr

Type annotations for boto3 ECR 1.43.119 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-ecr` · installs (wheel) · licence: MIT · rank 10651 · last release 2026-10-26 · [PyPI](https://pypi.org/project/types-boto3-ecr/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_ecr/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 ECR 1.43.119
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-ecr docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### traveltimepy

Python Interface to Travel Time.

`pip install traveltimepy` · installs (wheel) · licence: MIT License · rank 10799 · last release 2026-08-21 · [PyPI](https://pypi.org/project/traveltimepy/)

<details><summary>README extract</summary>

The TravelTime Python SDK provides a simple and efficient way to access the TravelTime API, enabling you to calculate travel times and distances, generate isochrones, and perform location-based queries using real-world transportation data.

Features:
- Time Matrix & Filtering: Calculate travel times between multiple origins and destinations
- Isochrone Generation: Create time-based catchment areas in multiple formats (GeoJSON, WKT) ...

Example:
```python
from datetime import datetime
from traveltimepy import Client
from traveltimepy.requests.common import Location, Coordinates, Property
from traveltimepy.requests.time_filter import TimeFilterDepartureSearch
from traveltimepy.requests.transportation import PublicTransport
from traveltimepy.errors import TravelTimeApiError

...

</details>

### types-peewee

Typing stubs for peewee

`pip install types-peewee` · installs (wheel) · licence: Apache-2.0 · rank 10800 · last release 2026-10-29 · [PyPI](https://pypi.org/project/types-peewee/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `peewee` package. It can be used by type checkers
to check code that uses `peewee`. This version of
`types-peewee` aims to provide accurate annotations for
`peewee==4.5.3`.

This stub package is marked as partial.
If you find that annotations are missing, feel free to contribute and help complete them. ...

</details>

### types-aiobotocore-application-autoscaling

Type annotations for aiobotocore ApplicationAutoScaling 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-application-autoscaling` · installs (wheel) · licence: MIT · rank 10810 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-application-autoscaling/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### TextArena

A Collection of Competitive Text-Based Games for Language Model Evaluation and Reinforcement Learning

`pip install TextArena` · installs (wheel) · licence: MIT · rank 10816 · last release 2025-10-16 · [PyPI](https://pypi.org/project/TextArena/)

<details><summary>README extract</summary>

A suite of 100+ {single,two,multi}-Player texted based games for benchmarking and training of LLMs.

Example:
```python
import textarena as ta

# Initialize agents
agents = {
    0: ta.agents.OpenRouterAgent(model_name="GPT-4o-mini"),
    1: ta.agents.OpenRouterAgent(model_name="anthropic/claude-3.5-haiku"),
}

# Initialize the environment
env = ta.make(env_id="TicTacToe-v0")

# wrap it for additional visualizations
env = ta.wrappers.SimpleRenderWrapper(env=env)

...
```

Sections: Play | Leaderboard | Games | Examples, Updates, Introduction, Getting Started, Offline Play

</details>

### truelayer-signing

Produce & verify TrueLayer API requests signatures

`pip install truelayer-signing` · installs (wheel) · licence: Other/Proprietary License · rank 10825 · last release 2026-06-18 · [PyPI](https://pypi.org/project/truelayer-signing/) · [source](https://github.com/TrueLayer/truelayer-signing)

<details><summary>README extract</summary>

Python package to produce & verify TrueLayer API requests signatures.

Example:
```python
tl_signature = sign_with_pem(KID, PRIVATE_KEY) \
    .set_method(HttpMethod.POST) \
    .set_path(path) \
    .add_header("Idempotency-Key", idempotency_key) \
    .set_body(body) \
    .sign()
```

Sections: truelayer-signing, Generating a signature, Verifying webhooks

</details>

### types-aiobotocore-glue

Type annotations for aiobotocore Glue 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-glue` · installs (wheel) · licence: MIT · rank 10826 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-glue/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glue/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-boto3-batch

Type annotations for boto3 Batch 1.43.106 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-batch` · installs (wheel) · licence: MIT · rank 10831 · last release 2026-09-30 · [PyPI](https://pypi.org/project/types-boto3-batch/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_batch/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Batch 1.43.106
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-batch docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-boto3-athena

Type annotations for boto3 Athena 1.43.126 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-athena` · installs (wheel) · licence: MIT · rank 10839 · last release 2026-11-06 · [PyPI](https://pypi.org/project/types-boto3-athena/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_athena/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Athena 1.43.126
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-athena docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### telebot

A Telegram bot library, with simple route decorators.

`pip install telebot` · installs (wheel) · licence: MIT License · rank 10928 · last release 2023-02-14 · [PyPI](https://pypi.org/project/telebot/)

<details><summary>README extract</summary>

Telebot

Note: This is not `pyTelegramBotAPI < but do to often confusion I have included
it within this package. So if you accidentally install this instead of `pyTelegramBotAPI <
the examples, etc will still work. ...

</details>

### types-boto3-guardduty

Type annotations for boto3 GuardDuty 1.43.115 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-guardduty` · installs (wheel) · licence: MIT · rank 10948 · last release 2026-10-19 · [PyPI](https://pypi.org/project/types-boto3-guardduty/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_guardduty/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 GuardDuty 1.43.115 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-guardduty docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### target-hotglue

`target-hotglue` is an SDK for building Singer Targets for hotglue.

`pip install target-hotglue` · does not install on CPython 3.14 · licence: Other/Proprietary License · rank 10955 · last release 2026-02-03 · [PyPI](https://pypi.org/project/target-hotglue/)

### types-objgraph

Typing stubs for objgraph

`pip install types-objgraph` · installs (wheel) · licence: Apache-2.0 · rank 10956 · last release 2026-10-18 · [PyPI](https://pypi.org/project/types-objgraph/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `objgraph` package. It can be used by type checkers
to check code that uses `objgraph`. This version of
`types-objgraph` aims to provide accurate annotations for
`objgraph==3.7.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tosa-tools

TOSA Tools: serialization library, reference model, optional MLIR translator

`pip install tosa-tools` · installs (wheel) · licence: Apache Software License · rank 10976 · last release 2026-08-25 · [PyPI](https://pypi.org/project/tosa-tools/)

<details><summary>README extract</summary>

<!--
 SPDX-FileCopyrightText: Copyright 2020-2026 Arm Limited and/or its affiliates <open-source-office@arm.com>
 SPDX-License-Identifier: Apache-2.0

A toolkit for working with the *Tensor Operator Set Architecture (TOSA) Specification* (< providing serialization, reference implementation, and MLIR translation capabilities. ...

Sections: TOSA Tools, Introduction, PyPI package, Prerequisites, Test environments, System Requirements, External Dependencies, LLVM/MLIR, Quick Build (POSIX), Selective Build, Debug Build, Build a wheel locally (optional), Pre-Commit Checks, Versioning

</details>

### tls-parser

Small library to parse TLS records.

`pip install tls-parser` · installs (wheel) · licence: not stated · rank 10996 · last release 2025-04-06 · [PyPI](https://pypi.org/project/tls-parser/)

### torchtitan

A PyTorch native platform for training generative AI models

`pip install torchtitan` · installs (wheel) · licence: not stated · rank 11013 · last release 2026-10-28 · [PyPI](https://pypi.org/project/torchtitan/) · [docs](https://github.com/pytorch/torchtitan/tree/main/docs) · [source](https://github.com/pytorch/torchtitan)

<details><summary>README extract</summary>

A PyTorch-native platform for pretraining and post-training generative AI models at scale

Quick start · Models · Features · RL · Docs · Contributing

`torchtitan` is a clean-room, PyTorch-native implementation of large-scale
training. ...

Features:
Parallelism
- FSDP2, HSDP, and DDP
- Tensor parallel, including async TP
- Pipeline parallel: 1F1B, Interleaved 1F1B, GPipe, and other `torch.distributed.pipelining` schedules
- Context parallel: all-gather KV and Ulysses ...

Example:
```python
# my_recipes.py
from torchtitan_recipes.models.llama3 import llama3_8b

def llama3_8b_tp2():
    config = llama3_8b()
    config.parallelism.tensor_parallel_degree = 2
    return config
```

Sections: Latest news, Quick start, Features, Documentation

</details>

### types-boto3-identitystore

Type annotations for boto3 IdentityStore 1.43.105 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-identitystore` · installs (wheel) · licence: MIT · rank 11049 · last release 2026-09-29 · [PyPI](https://pypi.org/project/types-boto3-identitystore/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_identitystore/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 IdentityStore 1.43.105 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page and in
types-boto3-identitystore docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### types-aiobotocore-cloudtrail

Type annotations for aiobotocore CloudTrail 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-cloudtrail` · installs (wheel) · licence: MIT · rank 11128 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-cloudtrail/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudtrail/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-python-http-client

Typing stubs for python-http-client

`pip install types-python-http-client` · installs (wheel) · licence: Apache-2.0 · rank 11148 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-python-http-client/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `python-http-client` package. It can be used by type checkers
to check code that uses `python-http-client`. This version of
`types-python-http-client` aims to provide accurate annotations for
`python-http-client==3.3.7`.

This package is part of the typeshed project. ...

</details>

### twikit

Twitter API wrapper for python with **no API key required**.

`pip install twikit` · installs (wheel) · licence: MIT · rank 11151 · last release 2025-02-07 · [PyPI](https://pypi.org/project/twikit/)

<details><summary>README extract</summary>

[日本語]
[中文]

A Simple Twitter API Scraper

You can use functions such as posting or searching for tweets without an API key using this library.

- Documentation (English)

🔵 Discord

> [!NOTE]
> Released twikit_grok an extension for using Grok AI with Twikit.
> For more details, visit:

Example:
```python
import asyncio
from twikit import Client

USERNAME = 'example_user'
EMAIL = 'email@example.com'
PASSWORD = 'password0000'

# Initialize client
client = Client('en-US')

async def main():
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD,
        cookies_file='cookies.json'
    )

...
```

Sections: Twikit, Features, No API Key Required, Free, Functionality, Quick Example

</details>

### tradingview-ta

Unofficial TradingView technical analysis API wrapper.

`pip install tradingview-ta` · installs (wheel) · licence: MIT License · rank 11165 · last release 2022-10-05 · [PyPI](https://pypi.org/project/tradingview-ta/) · [docs](https://python-tradingview-ta.readthedocs.io) · [source](https://github.com/brian-the-dev/python-tradingview-ta)

<details><summary>README extract</summary>

An unofficial python API wrapper to retrieve technical analysis from TradingView.

 - Always update tradingview-ta for new features and bug fixes: `pip install -U tradingview_ta`
 - Technical analysis for indices (index) is not supported by both TradingView and tradingview-ta, see issue #67 and #84.

Features:
* Faster response (compared to v2, which uses Selenium)
* Retrieve analysis for multiple symbols
* Indicators

Example:
```python
from tradingview_ta import TA_Handler, Interval, Exchange

tesla = TA_Handler(
    symbol="TSLA",
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_DAY,
    # proxies={'http': ' # Uncomment to enable proxy (replace the URL).
)
print(tesla.get_analysis().summary)
...
```

...

</details>

### topojson

topojson - a powerful library to encode geographic data as topology in Python!🌍

`pip install topojson` · installs (wheel) · licence: BSD License · rank 11208 · last release 2026-10-14 · [PyPI](https://pypi.org/project/topojson/) · [docs](https://mattijn.github.io/topojson) · [source](https://github.com/mattijn/topojson)

<details><summary>README extract</summary>

Topojson is a library that is capable of creating a topojson encoded format of nearly any spatial object in Python.

With topojson it is possible to reduce the size of your spatial data. Mostly by orders of magnitude. It is able to do so through:

- Eliminating redundancy through computation of a topology ...

Sections: topojson, Encode spatial data as topology in Python!, Usage, Other resources, Get in touch

</details>

### types-geoip2

Typing stubs for geoip2

`pip install types-geoip2` · installs (wheel) · licence: Apache Software License · rank 11381 · last release 2021-08-28 · [PyPI](https://pypi.org/project/types-geoip2/)

<details><summary>README extract</summary>

This is a PEP 561 type stub package for the `geoip2` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `geoip2`. The source for this package can be found at
 All fixes for
types and metadata should be contributed there. ...

</details>

### tokencost

To calculate token and translated USD cost of string and message calls to OpenAI, for example when used by AI agents

`pip install tokencost` · installs (wheel) · licence: MIT License · rank 11384 · last release 2025-08-13 · [PyPI](https://pypi.org/project/tokencost/)

<details><summary>README extract</summary>

Clientside token counting + price estimation for LLM apps and AI agents.

🐦 Twitter
📢 Discord
🖇️ AgentOps

Tokencost helps calculate the USD cost of using major Large Language Model (LLMs) APIs by calculating the estimated cost of prompts and completions.

Building AI agents? Check out AgentOps

Features:
* LLM Price Tracking Major LLM providers frequently add new models and update pricing. This repo helps track the latest price changes
* Token counting Accurately count prompt tokens before sending OpenAI requests
* Easy integration Get the cost of a ...

Example:
```python
from tokencost import calculate_prompt_cost, calculate_completion_cost

model = "gpt-3.5-turbo"
prompt = [{ "role": "user", "content": "Hello world"}]
completion = "How may I assist you today?"

...

</details>

### terminaltexteffects

TerminalTextEffects (TTE) is a terminal visual effects engine.

`pip install terminaltexteffects` · installs (wheel) · licence: MIT · rank 11422 · last release 2026-05-10 · [PyPI](https://pypi.org/project/terminaltexteffects/) · [docs](https://chrisbuilds.github.io/terminaltexteffects/) · [source](https://github.com/ChrisBuilds/terminaltexteffects)

<details><summary>README extract</summary>

Inline Visual Effects in the Terminal


Sections: Terminal Text Effects, TTE, Requirements

</details>

### texterrors

For WER

`pip install texterrors` · installs from source (sdist only) · licence: Apache-2.0 License · rank 11445 · last release 2026-09-09 · [PyPI](https://pypi.org/project/texterrors/)

<details><summary>README extract</summary>

`texterrors` scores ASR or transcription output against a reference and helps you inspect what went wrong.

It supports:
- WER and CER
- standard and character-aware alignment
- detailed aligned error reports
- colored output for inspecting alignments
- comparison of multiple hypothesis files against the same reference ...

Example:
```python
from texterrors import align_texts

ref_aligned, hyp_aligned, cost = align_texts(
    ["speedbird", "eight", "six", "two"],
    ["hello", "speedbird", "six", "two"],
    use_chardiff=True,
)
```

Sections: texterrors, 1.1.9, 1.1.8, 1.1.7, Common usage, Input formats, Output modes, Common analysis options, Entity scoring, Python usage, Benchmarking, Note on `--use-chardiff`

</details>

### tomesd

Token Merging for Stable Diffusion

`pip install tomesd` · installs (wheel) · licence: MIT · rank 11449 · last release 2023-05-14 · [PyPI](https://pypi.org/project/tomesd/)

<details><summary>README extract</summary>

Using nothing but pure python and pytorch, ToMe for SD speeds up diffusion by merging _redundant_ tokens.

This is the official implementation of ToMe for SD from our short paper:
Token Merging for Fast Stable Diffusion
Daniel Bolya, Judy Hoffman
_GitHub_ | _arXiv_ | _BibTeX_ ...

Example:
```python
import tomesd

# Patch a Stable Diffusion model with ToMe for SD using a 50% merging ratio.
# Using the default options are recommended for the highest quality, tune ratio to suit your needs.
tomesd.apply_patch(model, ratio=0.5)

# However, if you want to tinker around with the settings, we expose several options.
...
```

Sections: Token Merging for Stable Diffusion, What is ToMe for SD?, News, Usage, Example, Diffusers, ToMe + xformers / flash attn / torch 2.0

</details>

### twscrape

Twitter GraphQL and Search API implementation with SNScrape data models

`pip install twscrape` · installs (wheel) · licence: MIT License · rank 11507 · last release 2026-11-06 · [PyPI](https://pypi.org/project/twscrape/) · [source](https://github.com/vladkens/twscrape)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](

twscrape is an async Python library and CLI for X/Twitter Search and GraphQL endpoints. It runs on your own account pool, keeps sessions in SQLite, rotates accounts when an endpoint is rate-limited, and returns either parsed SNScrape-style models or raw API responses.

Features:
- Search and GraphQL X/Twitter API methods
- Async/await API for running multiple scrapers concurrently
- Login flow with optional email verification code retrieval
- Cookie-based account setup
- Saved account sessions and per-account proxies ...

Example:
```python
import asyncio
from twscrape import API, gather

async def main():
    api = API()  # or API("accounts.db")

    # Add once; the session is stored in the account database.
...

</details>

### types-aiobotocore-route53domains

Type annotations for aiobotocore Route53Domains 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-route53domains` · installs (wheel) · licence: MIT · rank 11520 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-route53domains/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53domains/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-aiobotocore-wafv2

Type annotations for aiobotocore WAFV2 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-wafv2` · installs (wheel) · licence: MIT · rank 11555 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-wafv2/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Literals

</details>

### types-netaddr

Typing stubs for netaddr

`pip install types-netaddr` · installs (wheel) · licence: Apache-2.0 · rank 11574 · last release 2026-07-24 · [PyPI](https://pypi.org/project/types-netaddr/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `netaddr` package. It can be used by type checkers
to check code that uses `netaddr`. This version of
`types-netaddr` aims to provide accurate annotations for
`netaddr==1.3.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### tb-mqtt-client

ThingsBoard python client SDK

`pip install tb-mqtt-client` · installs (wheel) · licence: Apache Software License (Apache Software License 2.0) · rank 11577 · last release 2026-09-21 · [PyPI](https://pypi.org/project/tb-mqtt-client/)

<details><summary>README extract</summary>

ThingsBoard is an open-source IoT platform for data collection, processing, visualization, and device management.
This project is a Python library that provides convenient client SDK for both Device and Gateway APIs.

SDK supports:
- Unencrypted and encrypted (TLS v1.2) connection
- QoS 0 and 1 (MQTT only)
- Automatic reconnect ...

Example:
```python
from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo

telemetry = {"temperature": 41.9, "enabled": False, "currentFirmwareVersion": "v1.2.2"}

# Initialize ThingsBoard client
client = TBDeviceMqttClient("127.0.0.1", username="A1_TEST_TOKEN")
# Connect to ThingsBoard
client.connect()
# Sending telemetry without checking the delivery status
...
```

...

</details>

### twisted-iocpsupport

An extension for use in the twisted I/O Completion Ports reactor.

`pip install twisted-iocpsupport` · installs from source (sdist only) · licence: MIT · rank 11580 · last release 2025-10-28 · [PyPI](https://pypi.org/project/twisted-iocpsupport/)

### types-m3u8

Typing stubs for m3u8

`pip install types-m3u8` · installs (wheel) · licence: Apache-2.0 · rank 11604 · last release 2026-05-18 · [PyPI](https://pypi.org/project/types-m3u8/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `m3u8` package. It can be used by type checkers
to check code that uses `m3u8`. This version of
`types-m3u8` aims to provide accurate annotations for
`m3u8==6.0.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there.
See the README
for more details. ...

</details>

### types-aiobotocore-verifiedpermissions

Type annotations for aiobotocore VerifiedPermissions 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-verifiedpermissions` · installs (wheel) · licence: MIT · rank 11608 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-verifiedpermissions/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-aiobotocore-iot-jobs-data

Type annotations for aiobotocore IoTJobsDataPlane 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-iot-jobs-data` · installs (wheel) · licence: MIT · rank 11609 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-iot-jobs-data/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_jobs_data/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Literals

</details>

### twilio-stubs

Type declarations for the Twilio API

`pip install twilio-stubs` · installs from source (sdist only) · licence: MIT License · rank 11649 · last release 2023-02-15 · [PyPI](https://pypi.org/project/twilio-stubs/)

<details><summary>README extract</summary>

mypy type declaration stubs for the Twilio Python API.

</details>

### tinybird

Tinybird Command Line Tool

`pip install tinybird` · does not install on CPython 3.14 · licence: not stated · rank 11656 · last release 2026-10-23 · [PyPI](https://pypi.org/project/tinybird/)

<details><summary>README extract</summary>

The Tinybird command-line tool allows you to use all the Tinybird functionality directly from the command line. Additionally, it includes several functions to create and manage data projects easily.

Sections: Tinybird CLI, 5.0.3, 5.0.2, 5.0.1, 5.0.0, 4.6.22, 4.6.21, 4.6.20, 4.6.19, 4.6.18, 4.6.17, 4.6.16, 4.6.15

</details>

### torchfcpe

The official Pytorch implementation of Fast Context-based Pitch Estimation (FCPE)

`pip install torchfcpe` · installs (wheel) · licence: MIT License · rank 11665 · last release 2024-03-06 · [PyPI](https://pypi.org/project/torchfcpe/)

<details><summary>README extract</summary>

Example:
```python
from torchfcpe import spawn_bundled_infer_model
import torch
import librosa

# configure device and target hop_size
device = 'cpu'
sr = 16000
hop_size = 160

# load audio
audio, sr = librosa.load('test.wav', sr=sr)
audio = librosa.to_mono(audio)
audio_length = len(audio)
f0_target_length=(audio_length // hop_size) + 1
...
```

Sections: TorchFCPE, Useage

</details>

### TM1py

A python module for TM1.

`pip install TM1py` · installs (wheel) · licence: MIT License · rank 11764 · last release 2026-09-21 · [PyPI](https://pypi.org/project/TM1py/)

<details><summary>README extract</summary>

TM1py is the python package for IBM Planning Analytics (TM1).

Features:
TM1py offers handy features to interact with TM1 from Python, such as

- Functions to read data from cubes through cube views or MDX queries (e.g. `tm1.cells.execute_mdx`)
- Functions to write data to cubes (e.g. `tm1.cells.write`) ...

Example:
```python
from TM1py.Services import TM1Service

with TM1Service(address='localhost', port=8001, user='admin', password='apple', ssl=True) as tm1:
    print(tm1.server.get_product_version())
```

Sections: Features, Requirements, Optional Python Packages, Usage, Documentation, Issues

</details>

### types-unidiff

Typing stubs for unidiff

`pip install types-unidiff` · installs (wheel) · licence: Apache-2.0 · rank 11772 · last release 2026-07-27 · [PyPI](https://pypi.org/project/types-unidiff/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `unidiff` package. It can be used by type checkers
to check code that uses `unidiff`. This version of
`types-unidiff` aims to provide accurate annotations for
`unidiff==0.7.*`.

*Note:* The `unidiff` package includes type annotations or type stubs
since version 1.0.0. ...

</details>

### timedelta-isoformat

Supplemental ISO8601 duration format support for datetime.timedelta

`pip install timedelta-isoformat` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 11832 · last release 2024-12-22 · [PyPI](https://pypi.org/project/timedelta-isoformat/) · [source](https://github.com/jayaddison/timedelta-isoformat.git/)

_README extract left out: share-alike licence._

### torchtext

Text utilities, models, transforms, and datasets for PyTorch.

`pip install torchtext` · does not install on CPython 3.14 · licence: BSD · rank 11902 · last release 2024-04-24 · [PyPI](https://pypi.org/project/torchtext/)

<details><summary>README extract</summary>

CAUTION: As of September 2023 we have paused active development of TorchText because our focus has shifted away from building out this library offering.
We will continue to release new versions but do not anticipate any new feature development as we figure out future investments in this space.

This repository consists of: ...

Sections: torchtext, Optional requirements, Building from source, Documentation, Datasets, Models, Tokenizers, Tutorials, Disclaimer on Datasets

</details>

### types-aiobotocore-sagemaker-runtime

Type annotations for aiobotocore SageMakerRuntime 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-sagemaker-runtime` · installs (wheel) · licence: MIT · rank 11921 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-sagemaker-runtime/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_runtime/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Literals

</details>

### tools

python syntax tool

`pip install tools` · installs (wheel) · licence: MIT License · rank 12044 · last release 2026-10-06 · [PyPI](https://pypi.org/project/tools/)

<details><summary>README extract</summary>

(`tools` package was replaced on 2025.04.28. If you're looking for web scraping tools, visit

Python syntax tools for faster programming. github \
jsyoo61@unc.edu

 pip install tools

 import tools as T
 T.save_pickle(data, 'data.p')
 data = T.load_pickle('data.p') ...

</details>

### tockloader

Tockloader is a tool for installing Tock applications.

`pip install tockloader` · installs (wheel) · licence: not stated · rank 12132 · last release 2026-10-23 · [PyPI](https://pypi.org/project/tockloader/)

<details><summary>README extract</summary>

Tool for programming Tock onto hardware boards.

Install

If you want tab completions:

Usage

This tool installs a binary called `tockloader`, which supports several commands.

These are the main commands for managing apps on a board.

Sections: Primary Commands, Board Inspection Commands, Utility Commands, Other Commands, Test Locally, Upload to PyPI, Build Docs, Create requirements.txt

</details>

### timelib

parse english textual date descriptions

`pip install timelib` · installs from source (sdist only) · licence: zlib/php · rank 12171 · last release 2023-03-18 · [PyPI](https://pypi.org/project/timelib/)

### types-aiobotocore-identitystore

Type annotations for aiobotocore IdentityStore 3.10.0 service generated with mypy-boto3-builder 8.12.0

`pip install types-aiobotocore-identitystore` · installs (wheel) · licence: MIT · rank 12197 · last release 2026-10-24 · [PyPI](https://pypi.org/project/types-aiobotocore-identitystore/) · [docs](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_identitystore/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_aiobotocore_ec2 import EC2Client, EC2ServiceResource
    from types_aiobotocore_ec2.waiters import BundleTaskCompleteWaiter
    from types_aiobotocore_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
...
```

Sections: Generate locally (recommended), From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations, Paginators annotations

</details>

### types-editdistance

Typing stubs for editdistance

`pip install types-editdistance` · installs (wheel) · licence: Apache-2.0 · rank 12219 · last release 2026-04-08 · [PyPI](https://pypi.org/project/types-editdistance/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `editdistance` package. It can be used by type checkers
to check code that uses `editdistance`. This version of
`types-editdistance` aims to provide accurate annotations for
`editdistance==0.8.*`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### torchsr

Super Resolution Networks for pytorch

`pip install torchsr` · installs (wheel) · licence: MIT License · rank 12265 · last release 2022-08-21 · [PyPI](https://pypi.org/project/torchsr/)

<details><summary>README extract</summary>

Super-resolution is a process that increases the resolution of an image, adding additional details.
Methods using neural networks give the most accurate results, much better than other interpolation methods.
With the right training, it is even possible to make photo-realistic images. ...

Example:
```python
from torchsr.datasets import Div2K
from torchsr.models import ninasr_b0
from torchvision.transforms.functional import to_pil_image, to_tensor

# Div2K dataset
dataset = Div2K(root="./data", scale=2, download=False)

# Get the first image in the dataset (High-Res and Low-Res)
hr, lr = dataset[0]

# Download a pretrained NinaSR model
...
```

Sections: Super-Resolution Networks for Pytorch, Models, Datasets, Usage, Training

</details>

### types-paho-mqtt

Typing stubs for paho-mqtt

`pip install types-paho-mqtt` · installs (wheel) · licence: Apache Software License · rank 12322 · last release 2024-03-21 · [PyPI](https://pypi.org/project/types-paho-mqtt/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a PEP 561
type stub package for the `paho-mqtt` package.
It can be used by type-checking tools like
mypy,
pyright,
pytype,
PyCharm, etc. to check code that uses
`paho-mqtt`.

This version of `types-paho-mqtt` aims to provide accurate annotations
for `paho-mqtt==1.6.*`. ...

</details>

### tiered-debug

A Python logging helper module that allows multiple levels of debug logging

`pip install tiered-debug` · installs (wheel) · licence: Apache-2.0 · rank 12334 · last release 2026-08-04 · [PyPI](https://pypi.org/project/tiered-debug/) · [docs](https://tiered-debug.readthedocs.io/) · [source](https://github.com/untergeek/tiered-debug)

### trackpy

particle-tracking toolkit

`pip install trackpy` · installs from source (sdist only) · licence: not stated · rank 12372 · last release 2025-07-18 · [PyPI](https://pypi.org/project/trackpy/)

<details><summary>README extract</summary>

What is it?

trackpy is a Python package for particle tracking in 2D, 3D, and higher dimensions.
Read the walkthrough to skim or study an example project from start to finish.

Documentation

Read the documentation for

- an introduction
- tutorials on the basics, 3D tracking, and much, much more
- easy installation instructions ...

</details>

### tdqm

Alias for typos of tqdm

`pip install tdqm` · installs from source (sdist only) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 12431 · last release 2020-08-19 · [PyPI](https://pypi.org/project/tdqm/)

<details><summary>README extract</summary>

Alias for typos of tqdm.

It's tqdm, *taqaddum*, *te quiero demasiado*!

If you don't like it... have a meta comic: xkcd#302.

Also see tqdm#995.

</details>

### transformations

Homogeneous Transformation Matrices and Quaternions

`pip install transformations` · installs (wheel) · licence: BSD-3-Clause · rank 12587 · last release 2026-08-09 · [PyPI](https://pypi.org/project/transformations/) · [source](https://github.com/cgohlke/transformations)

<details><summary>README extract</summary>

Transformations is a Python library for calculating 4x4 matrices for
translating, rotating, reflecting, scaling, shearing, projecting,
orthogonalizing, and superimposing arrays of 3D homogeneous coordinates
as well as for converting between rotation matrices, Euler angles,
and quaternions. ...

Sections: Homogeneous Transformation Matrices and Quaternions, Quickstart, Requirements, Revisions, Notes, References, Examples

</details>

### tinsel

PySpark schema generator

`pip install tinsel` · installs (wheel) · licence: MIT License · rank 12628 · last release 2018-09-01 · [PyPI](https://pypi.org/project/tinsel/)

<details><summary>README extract</summary>

*Your data IS your schema*

This tiny library helps to overcome excessive complexity in hand-written pyspark
dataframe schemas.

Shape your data as `NamedTuple` or dataclasses - they can freely mix:
Transform root node (`User` in our case) into schema:
Create some data, if necessary:
And… voilà!:
This will output:

Features:
* use native python types; no extra DSL, no cryptic API — just plain Python;
* small and fast;
* provide type shims for some types absent in Python, like `long` or `short`;
* nullable fields naturally fits into schema definition;

Example:
```python
from dataclasses import dataclass
from tinsel import struct, transform
from typing import NamedTuple, Optional, Dict, List

@struct
@dataclass
class UserInfo:
    hobby: List[str]
    last_seen: Optional[int]
...

</details>

### tacacs_plus

A client for TACACS+ authentication

`pip install tacacs_plus` · installs (wheel) · licence: BSD License · rank 12697 · last release 2018-08-20 · [PyPI](https://pypi.org/project/tacacs_plus/)

### TextGrid

Praat TextGrid manipulation.

`pip install TextGrid` · installs from source (sdist only) · licence: not stated · rank 12819 · last release 2024-02-29 · [PyPI](https://pypi.org/project/TextGrid/)

### types-nanoid

Typing stubs for nanoid

`pip install types-nanoid` · installs (wheel) · licence: Apache-2.0 · rank 12844 · last release 2026-05-08 · [PyPI](https://pypi.org/project/types-nanoid/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `nanoid` package. It can be used by type checkers
to check code that uses `nanoid`. This version of
`types-nanoid` aims to provide accurate annotations for
`nanoid==2.0.0`.

This package is part of the typeshed project.
All fixes for types and metadata should be contributed there. ...

</details>

### types-mypy-extensions

Typing stubs for mypy-extensions

`pip install types-mypy-extensions` · installs (wheel) · licence: Apache-2.0 · rank 12858 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-mypy-extensions/) · [source](https://github.com/python/typeshed)

<details><summary>README extract</summary>

This is a type stub package
for the `mypy-extensions` package. It can be used by type checkers
to check code that uses `mypy-extensions`. This version of
`types-mypy-extensions` aims to provide accurate annotations for
`mypy-extensions==1.2.*`.

This package is part of the typeshed project. ...

</details>

### tzcron

Timezone aware Cron/Quartz parser

`pip install tzcron` · installs (wheel) · licence: Apache Software License · rank 12875 · last release 2016-09-25 · [PyPI](https://pypi.org/project/tzcron/)

<details><summary>README extract</summary>

A library to work with cron/quartz expressions and timezones.

Features:
tzcron provides a way to define schedules attached to timezones and get time occurrences out of it by just iterating the object created.

Sections: tzcron, Overview, Usage

</details>

### types-boto3-securityhub

Type annotations for boto3 SecurityHub 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install types-boto3-securityhub` · installs (wheel) · licence: MIT · rank 12885 · last release 2026-11-04 · [PyPI](https://pypi.org/project/types-boto3-securityhub/) · [docs](https://youtype.github.io/types_boto3_docs/types_boto3_securityhub/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types_boto3_ec2 import EC2Client, EC2ServiceResource
    from types_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from types_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

Sections: Generate locally (recommended), VSCode extension, From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations

</details>

### temp

temp.tempdir(), temp.tempfile() functions

`pip install temp` · installs from source (sdist only) · licence: Public Domain · rank 12950 · last release 2020-07-07 · [PyPI](https://pypi.org/project/temp/)

<details><summary>README extract</summary>

Example:
```python
>>> import temp
>>> temp.tempdir() # dir
'/var/folders/rv/gy6_gnfs1d7_pd1518p27tsr0000gn/T/tmpqlLDxb'

>>> temp.tempfile() # file
'/var/folders/rv/gy6_gnfs1d7_pd1518p27tsr0000gn/T/tmpsctFHJ'

>>> temp.TMPDIR
'/var/folders/rv/gy6_gnfs1d7_pd1518p27tsr0000gn/T'
```

</details>

### tableschema-to-template

Given a Frictionless Table Schema, generates an Excel template with input validation

`pip install tableschema-to-template` · installs (wheel) · licence: MIT License · rank 12972 · last release 2023-02-01 · [PyPI](https://pypi.org/project/tableschema-to-template/)

<details><summary>README extract</summary>

Given a Frictionless Table Schema
(like this),
generate an Excel template with input validation
(like this).

Features:
- Enum constraints transformed into pull-downs.
- Field descriptions transformed into comments in header.
- Float, integer, and boolean type validation, with range checks on numbers.

More details in the changelog.

Example:
```python
from tableschema_to_template import create_xlsx
schema = {'fields': [{
  'name': 'a_number',
  'description': 'A number!',
  'type': 'number'
}]}
create_xlsx(schema, '/tmp/template.xlsx')
```

Sections: tableschema-to-template, Usage, Features, Related work

</details>

### tcp-modbus-aio

asyncio client library for tcp modbus devices

`pip install tcp-modbus-aio` · installs (wheel) · licence: MIT License · rank 12985 · last release 2026-09-14 · [PyPI](https://pypi.org/project/tcp-modbus-aio/)

<details><summary>README extract</summary>

asyncio client library for tcp modbus devices. built on top of umodbus but extended for more *industrial robustness* and asyncio compat. the umodbus documentation is recommended reading to have any hope of using this code.

narrowly constructed for the use cases of Tutor Intelligence, but feel free to post an issue or PR if relevant to you.

Sections: tcp-modbus-aio, usage

</details>

### twelvedata

Python client for Twelve Data

`pip install twelvedata` · installs (wheel) · licence: MIT · rank 12986 · last release 2026-04-27 · [PyPI](https://pypi.org/project/twelvedata/)

<details><summary>README extract</summary>

Official python library for Twelve Data. This package supports all main features of the service:

* Get stock, forex, cryptocurrency, ETF, and index OHLC time series.
* Companies' profiles, financials, and much more fundamentals data.
* Get over 100+ technical indicators. ...

Features:
* Real-time low latency stream of financial quotes.
* You might subscribe to stocks, forex, and crypto.

Example:
```python
import time
from twelvedata import TDClient

messages_history = []

def on_event(e):
    # do whatever is needed with data
    print(e)
    messages_history.append(e)

td = TDClient(apikey="YOUR_API_KEY_HERE")
ws = td.websocket(symbols="BTC/USD", on_event=on_event)
ws.subscribe(['ETH/BTC', 'AAPL'])
ws.connect()
while True:
...
```

...

</details>

