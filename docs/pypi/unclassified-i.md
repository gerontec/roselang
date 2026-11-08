# Unclassified / I

[Index](README.md) · 129 packages in this topic, by downloads.

### importlib-metadata

Read metadata from Python packages

`pip install importlib-metadata` · installs (wheel) · licence: Apache-2.0 · rank 83 · last release 2026-10-24 · [PyPI](https://pypi.org/project/importlib-metadata/) · [source](https://github.com/python/importlib_metadata)

<details><summary>README extract</summary>

Library to access the metadata for a Python package.

This package supplies third-party access to the functionality of
importlib.metadata
including improvements added to subsequent Python versions.

New features are introduced in this third-party library and later merged
into CPython. ...

Sections: Compatibility, Usage, Caveats, Project details, For Enterprise

</details>

### itsdangerous

Safely pass data to untrusted environments and back.

`pip install itsdangerous` · installs (wheel) · licence: BSD License · rank 147 · last release 2024-04-16 · [PyPI](https://pypi.org/project/itsdangerous/) · [docs](https://itsdangerous.palletsprojects.com/) · [source](https://github.com/pallets/itsdangerous/)

<details><summary>README extract</summary>

... so better sign this

Various helpers to pass data to untrusted environments and to get it
back safe and sound. Data is cryptographically signed to ensure that a
token has not been tampered with.

It's possible to customize how data is serialized. Data is compressed as
needed. ...

Example:
```python
from itsdangerous import URLSafeSerializer
auth_s = URLSafeSerializer("secret key", "auth")
token = auth_s.dumps({"id": 5, "name": "itsdangerous"})

print(token)
# eyJpZCI6NSwibmFtZSI6Iml0c2Rhbmdlcm91cyJ9.6YP6T0BaO67XP--9UzTrmurXSmg

data = auth_s.loads(token)
print(data["name"])
# itsdangerous
```

Sections: ItsDangerous, A Simple Example

</details>

### identify

File identification library for Python

`pip install identify` · installs (wheel) · licence: MIT · rank 209 · last release 2026-09-26 · [PyPI](https://pypi.org/project/identify/)

<details><summary>README extract</summary>

File identification library for Python.

Given a file (or some information about a file), return a set of standardized
tags identifying what the file is.

Example:
```python
>>> from identify import identify
>>> identify.tags_from_path('/path/to/file.py')
{'file', 'text', 'python', 'non-executable'}
>>> identify.tags_from_path('/path/to/file-with-shebang')
{'file', 'text', 'shell', 'bash', 'executable'}
>>> identify.tags_from_path('/bin/bash')
{'file', 'binary', 'executable'}
...
```

Sections: identify, Usage, With a file on disk, If you only have the filename, If you only have the interpreter, As a cli, How it works

</details>

### importlib-resources

Read resources from Python packages

`pip install importlib-resources` · installs (wheel) · licence: Apache-2.0 · rank 372 · last release 2026-04-12 · [PyPI](https://pypi.org/project/importlib-resources/) · [source](https://github.com/python/importlib_resources)

<details><summary>README extract</summary>

`importlib_resources` is a backport of Python standard library
importlib.resources
module for older Pythons.

The key goal of this module is to replace parts of pkg_resources with a
solution in Python's stdlib that relies on well-defined APIs. This makes
reading resources included in packages easier, with more stable and consistent
semantics. ...

Sections: Compatibility, For Enterprise

</details>

### ipython-pygments-lexers

Defines a variety of Pygments lexers for highlighting IPython code.

`pip install ipython-pygments-lexers` · installs (wheel) · licence: BSD License · rank 375 · last release 2025-01-17 · [PyPI](https://pypi.org/project/ipython-pygments-lexers/) · [source](https://github.com/ipython/ipython-pygments-lexers)

<details><summary>README extract</summary>

A Pygments plugin for IPython code & console sessions

IPython is an interactive Python shell. Among other features,
it adds some special convenience syntax, including `%magics`, `!shell commands`
and `help?`. This package contains lexers for these, to use with the Pygments syntax
highlighting package. ...

</details>

### ipykernel

IPython Kernel for Jupyter

`pip install ipykernel` · installs (wheel) · licence: BSD-3-Clause · rank 389 · last release 2026-09-29 · [PyPI](https://pypi.org/project/ipykernel/) · [docs](https://ipykernel.readthedocs.io) · [source](https://github.com/ipython/ipykernel)

<details><summary>README extract</summary>

This package provides the IPython kernel for Jupyter.

Sections: IPython Kernel for Jupyter, Running tests, Running tests with coverage, Our Copyright Policy

</details>

### installer

A library for installing Python wheels.

`pip install installer` · installs (wheel) · licence: MIT · rank 415 · last release 2026-10-12 · [PyPI](https://pypi.org/project/installer/) · [source](https://github.com/pypa/installer)

### ImageIO

Read and write images and video across all major formats. Supports scientific and volumetric data.

`pip install ImageIO` · installs (wheel) · licence: BSD-2-Clause · rank 523 · last release 2026-10-08 · [PyPI](https://pypi.org/project/ImageIO/) · [docs](https://imageio.readthedocs.io) · [source](https://github.com/imageio/imageio)

<details><summary>README extract</summary>

Website: <

Imageio is a mature Python library that makes it easy to read and write image
and video data. This includes animated images, video, volumetric data, and
scientific formats. It is cross-platform, runs on Python 3.11 through 3.14, and is easy to
install.

Professional support is available via
Tidelift.

Features:
- Simple interface via a concise set of functions
- Easy to
 install
 using Conda or pip
- Few core dependencies (only NumPy and Pillow)
- Pure Python, runs on Python 3.11 through 3.14, and PyPy
- Cross platform, runs on Windows, Linux, macOS ...

Example:
```python
import imageio.v3 as iio
im = iio.imread('imageio:chelsea.png')  # read a standard image
im.shape  # im is a NumPy array of shape (300, 451, 3)
iio.imwrite('chelsea.jpg', im)  # convert to jpg
```

...

</details>

### inflection

A port of Ruby on Rails inflector to Python

`pip install inflection` · installs (wheel) · licence: MIT License · rank 543 · last release 2020-08-22 · [PyPI](https://pypi.org/project/inflection/)

<details><summary>README extract</summary>

Inflection is a string transformation library. It singularizes and pluralizes
English words, and transforms strings from CamelCase to underscored string.
Inflection is a port of Ruby on Rails' inflector to Python.

- Documentation
- Issue Tracker
- Code
- Development Version

Sections: Inflection, Resources

</details>

### ipywidgets

Jupyter interactive widgets

`pip install ipywidgets` · installs (wheel) · licence: BSD License · rank 574 · last release 2026-08-18 · [PyPI](https://pypi.org/project/ipywidgets/)

<details><summary>README extract</summary>

ipywidgets, also known as jupyter-widgets or simply widgets, are
interactive HTML widgets
for Jupyter notebooks and the IPython kernel.

This package contains the python implementation of the core interactive widgets bundled in ipywidgets.

The fundamental widgets provided by this library are called core interactive
widgets. ...

Sections: ipywidgets: Interactive HTML Widgets, Core Interactive Widgets

</details>

### imageio-ffmpeg

FFMPEG wrapper for Python

`pip install imageio-ffmpeg` · installs (wheel) · licence: BSD License · rank 776 · last release 2026-11-03 · [PyPI](https://pypi.org/project/imageio-ffmpeg/)

<details><summary>README extract</summary>

FFMPEG wrapper for Python.

Note that the platform-specific wheels contain the binary executable
of ffmpeg, which makes this package around 60 MiB in size.
I guess that's the cost for being able to read/write video files. ...

</details>

### Incremental

A CalVer version manager that supports the future.

`pip install Incremental` · installs (wheel) · licence: MIT License · rank 985 · last release 2025-11-28 · [PyPI](https://pypi.org/project/Incremental/) · [docs](https://twisted.org/incremental/docs/)

<details><summary>README extract</summary>

Incremental is a CalVer version manager supports the future.

API documentation can be found here.
Narrative documentation follows.

- A version number has the form YY.MM.PATCH.
- If your project is named "Shrubbery", its code is found in `shrubbery/` or `src/shrubbery/`. ...

Example:
```python
setup(
    use_incremental=True,
    setup_requires=['incremental'],
    install_requires=['incremental'], # along with any other install dependencies
    ...
}
```

Sections: Incremental, Theory of Operation, Quick Start, Using setuptools, Using Hatchling, Using `setup.py`, Initialize the project, Runtime integration, Incremental Versions, Updating, Indeterminate Versions

</details>

### interface-meta

`interface_meta` provides a convenient way to expose an extensible API with enforced method signatures and consistent documentation.

`pip install interface-meta` · installs (wheel) · licence: MIT · rank 1052 · last release 2026-04-30 · [PyPI](https://pypi.org/project/interface-meta/) · [source](https://github.com/matthewwardrop/interface_meta)

<details><summary>README extract</summary>

`interface_meta` provides a convenient way to expose an extensible API with
enforced method signatures and consistent documentation.

- Documentation: See below (full documentation will come at some point).

Features:
This library has been extracted (with some modifications) from
`omniduct`, a library also principally
written by this author, where it was central to the extensible plugin
architecture. ...

Example:
```python
from abc import abstractmethod
from interface_meta import InterfaceMeta, inherit_docs, override

class MyInterface(metaclass=InterfaceMeta):
    """
    An example interface.
    """

    INTERFACE_EXPLICIT_OVERRIDES = True
    INTERFACE_RAISE_ON_VIOLATION = False

    @property
    @abstractmethod
    def name(self) -> str:
        """
...
```

...

</details>

### iso8601

Simple module to parse ISO 8601 dates

`pip install iso8601` · installs (wheel) · licence: MIT License · rank 1180 · last release 2023-10-03 · [PyPI](https://pypi.org/project/iso8601/) · [docs](https://pyiso8601.readthedocs.io/en/latest/) · [source](https://github.com/micktwomey/pyiso8601)

<details><summary>README extract</summary>

Simple module to parse ISO 8601 dates

`pip install iso8601`

Documentation:

PyPI:

Source:

This module parses the most common forms of ISO 8601 date strings (e.g. 2007-01-14T20:34:22+00:00) into datetime objects.

>>> import iso8601
>>> iso8601.parse_date("2007-01-25T12:00:00Z")
datetime.datetime(2007, 1, 25, 12, 0, tzinfo=<iso8601.Utc>)
>>> ...

Sections: Parsed Formats, Dates, Times, Time Zones, Where it Differs From ISO 8601, References, Releasing

</details>

### instructor

structured outputs for llm

`pip install instructor` · installs (wheel) · licence: MIT · rank 1295 · last release 2026-09-09 · [PyPI](https://pypi.org/project/instructor/) · [source](https://github.com/567-labs/instructor)

<details><summary>README extract</summary>

Get reliable JSON from any LLM. Built on Pydantic for validation, type safety, and IDE support.

That's it. No JSON parsing, no error handling, no retries. Just define a model and get structured data.

> Use Instructor for fast extraction, reach for PydanticAI when you need agents. Instructor keeps schema-first flows simple and cheap. ...

Features:
Getting structured data from LLMs is hard. You need to:

1. Write complex JSON schemas
2. Handle validation errors
3. Retry failed extractions
4. Parse unstructured responses
5. Deal with different provider APIs ...

Example:
```python
import instructor
from pydantic import BaseModel

# Define what you want
class User(BaseModel):
    name: str
    age: int

# Extract it from natural language
...

</details>

### icalendar

RFC 5545 compatible parser and generator of iCalendar files

`pip install icalendar` · installs (wheel) · licence: BSD-2-Clause · rank 1313 · last release 2026-08-19 · [PyPI](https://pypi.org/project/icalendar/) · [docs](https://icalendar.readthedocs.io/en/stable/) · [source](https://github.com/collective/icalendar)

<details><summary>README extract</summary>

The icalendar package is an 5545 compatible parser and generator of iCalendar files.

icalendar can create, inspect, and modify calendaring information with Python.

icalendar supports multiple timezone implementations, including zoneinfo, dateutil.tz, and pytz. ...

Sections: Internet Calendaring and Scheduling (iCalendar) for Python, Usage, Related projects

</details>

### ImageHash

Image Hashing library

`pip install ImageHash` · installs (wheel) · licence: 2-clause BSD License · rank 1620 · last release 2025-02-01 · [PyPI](https://pypi.org/project/ImageHash/)

<details><summary>README extract</summary>

An image hashing library written in Python. ImageHash supports:

* Average hashing
* Perceptual hashing
* Difference hashing
* Wavelet hashing
* HSV color hashing (colorhash)
* Crop-resistant hashing

Image hashes tell whether two images look nearly identical. ...

Example:
```python
>>> from PIL import Image
>>> import imagehash
>>> hash = imagehash.average_hash(Image.open('tests/data/imagehash.png'))
>>> print(hash)
ffd7918181c9ffff
>>> otherhash = imagehash.average_hash(Image.open('tests/data/peppers.png'))
>>> print(otherhash)
9f172786e71f1e00
>>> print(hash == otherhash)
False
...
```

Sections: ImageHash, Rationale, Basic usage, References, Examples, Example 1: Icon dataset, Example 2: Art dataset, Storing hashes, Efficient database search, Other projects

</details>

### iso3166

Self-contained ISO 3166-1 country definitions.

`pip install iso3166` · installs (wheel) · licence: MIT · rank 1794 · last release 2026-09-03 · [PyPI](https://pypi.org/project/iso3166/)

<details><summary>README extract</summary>

:Authors:
 Mike Spindel
:Version: 3.0.0

ISO 3166-1 defines two-letter, three-letter, and three-digit country
codes. `python-iso3166` is a self-contained module that converts
between these codes and the corresponding country name.

Example:
```python
>>> from iso3166 import countries
>>>
>>> countries.get('us')
Country(name='United States', alpha2='US', alpha3='USA', numeric='840')
>>> countries.get('ala')
Country(name='Åland Islands', alpha2='AX', alpha3='ALA', numeric='248')
>>> countries.get(8)
Country(name='Albania', alpha2='AL', alpha3='ALB', numeric='008')
```

Sections: python-iso3166 - Standalone ISO 3166-1 country definitions, Usage, Country details, Country lists and indexes

</details>

### icdiff

improved colored diff

`pip install icdiff` · installs (wheel) · licence: Python Software Foundation License · rank 1877 · last release 2026-02-08 · [PyPI](https://pypi.org/project/icdiff/) · [source](https://github.com/jeffkaufman/icdiff)

<details><summary>README extract</summary>

Improved colored diff

Sections: Icdiff, Usage, Options, Using with Git, Using with subversion, Using with Mercurial, Setting up a dev environment, Running tests

</details>

### interegular

a regex intersection checker

`pip install interegular` · installs (wheel) · licence: MIT License · rank 2024 · last release 2024-01-06 · [PyPI](https://pypi.org/project/interegular/)

<details><summary>README extract</summary>

*regex intersection checker*

A library to check a subset of python regexes for intersections.
Based on grennery by @qntm. Adapted for lark-parser.

The primary difference with `grennery` library is that `interegular` is focused on speed and compatibility with python re syntax, whereas grennery has a way to reconstruct a regex from a FSM, which ...

Sections: Interegular, Interface, TODO

</details>

### ipython_genutils

Vestigial utilities from IPython

`pip install ipython_genutils` · installs (wheel) · licence: BSD License · rank 2030 · last release 2017-03-13 · [PyPI](https://pypi.org/project/ipython_genutils/)

### intelhex

Python library for Intel HEX files manipulations

`pip install intelhex` · installs (wheel) · licence: BSD License · rank 2115 · last release 2020-10-20 · [PyPI](https://pypi.org/project/intelhex/)

<details><summary>README extract</summary>

Python IntelHex library
*******

Introduction

The Intel HEX file format is widely used in microprocessors and microcontrollers
area (embedded systems etc) as the de facto standard
for representation of code to be programmed into microelectronic devices. ...

</details>

### injector

Injector - Python dependency injection framework, inspired by Guice

`pip install injector` · installs (wheel) · licence: BSD · rank 2169 · last release 2026-01-09 · [PyPI](https://pypi.org/project/injector/)

<details><summary>README extract</summary>

Introduction

While dependency injection is easy to do in Python due to its support for keyword arguments, the ease with which objects can be mocked and its dynamic nature, a framework for assisting in this process can remove a lot of boiler-plate from larger applications. That's where Injector can help. ...

Example:
```python
class MyClass:
    @inject
    def init(t: SomeType):
        # ...

MyClass()
```

</details>

### iterable-io

Adapt generators and other iterables to a file-like interface

`pip install iterable-io` · installs (wheel) · licence: LGPL-3.0-only · rank 2236 · last release 2026-05-17 · [PyPI](https://pypi.org/project/iterable-io/) · [source](https://github.com/pR0Ps/iterable-io)

_README extract left out: share-alike licence._

### ipaddress

IPv4/IPv6 manipulation library

`pip install ipaddress` · installs (wheel) · licence: Python Software Foundation License · rank 2318 · last release 2019-10-18 · [PyPI](https://pypi.org/project/ipaddress/)

### img2pdf

Lossless conversion of raster images to PDF.

`pip install img2pdf` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 2448 · last release 2025-11-05 · [PyPI](https://pypi.org/project/img2pdf/)

_README extract left out: share-alike licence._

### inputimeout

Multi platform standard input with timeout

`pip install inputimeout` · installs (wheel) · licence: MIT License · rank 2472 · last release 2018-03-02 · [PyPI](https://pypi.org/project/inputimeout/)

<details><summary>README extract</summary>

Multi platform standard input with timeout

Example:
```python
from inputimeout import inputimeout, TimeoutOccurred
try:
    something = inputimeout(prompt='>>', timeout=5)
except TimeoutOccurred:
    something = 'something'
print(something)
```

Sections: inputimeout, Description, Usage

</details>

### iterative-telemetry

Common library for sending telemetry

`pip install iterative-telemetry` · installs (wheel) · licence: Apache-2.0 · rank 2710 · last release 2025-02-11 · [PyPI](https://pypi.org/project/iterative-telemetry/)

<details><summary>README extract</summary>

Features:
* can be disabled in all tools by setting `ITERATIVE_DO_NOT_TRACK=1` env var
* single anonymised `user_id` across all `iterative` projects

Sections: Iterative Telemetry, Features, Requirements, Usage, Issues

</details>

### iopath

A library for providing I/O abstraction.

`pip install iopath` · installs from source (sdist only) · licence: MIT licensed, as found in the LICENSE file · rank 2946 · last release 2022-07-09 · [PyPI](https://pypi.org/project/iopath/)

### imagecodecs

Image transformation, compression, and decompression codecs

`pip install imagecodecs` · installs (wheel) · licence: BSD-3-Clause · rank 2964 · last release 2026-10-09 · [PyPI](https://pypi.org/project/imagecodecs/) · [source](https://github.com/cgohlke/imagecodecs)

<details><summary>README extract</summary>

Imagecodecs is a Python library that provides block-oriented, in-memory buffer
transformation, compression, and decompression functions for use in tifffile,
liffile, czifile, zarr, and other scientific image input/output packages. ...

Sections: Image transformation, compression, and decompression codecs, Quickstart, Requirements, Revisions, Objectives, Notes, Examples

</details>

### infisicalsdk

Official Infisical SDK for Python (Latest)

`pip install infisicalsdk` · installs (wheel) · licence: not stated · rank 2995 · last release 2026-11-05 · [PyPI](https://pypi.org/project/infisicalsdk/)

<details><summary>README extract</summary>

The official Infisical SDK for Python.
 Documentation can be found at

</details>

### ifcopenshell

Python bindings, utility functions, and high-level API for IfcOpenShell

`pip install ifcopenshell` · installs (wheel) · licence: LGPL-3.0-or-later · rank 3411 · last release 2026-10-15 · [PyPI](https://pypi.org/project/ifcopenshell/)

_README extract left out: share-alike licence._

### intuit-oauth

Intuit OAuth Client

`pip install intuit-oauth` · installs (wheel) · licence: Apache 2.0 · rank 3509 · last release 2026-07-22 · [PyPI](https://pypi.org/project/intuit-oauth/)

<details><summary>README extract</summary>

The official Python client library for working with Intuit APIs.
The `AuthClient` object response can be used for the
Intuit UserInfo API,
QuickBooks Accounting API,
and QuickBooks Payments API.

This library supports:

- Raising authorization requests
- Requesting OAuth2 bearer (access) tokens
- Refreshing OAuth2 tokens
- Revoking OAuth2 tokens ...

Sections: Intuit's OAuth2 and OpenID Connect Python Client, Documentation, Sample App

</details>

### ibm-cos-sdk

IBM SDK for Python

`pip install ibm-cos-sdk` · installs from source (sdist only) · licence: Apache Software License · rank 3622 · last release 2026-04-14 · [PyPI](https://pypi.org/project/ibm-cos-sdk/) · [docs](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-python) · [source](https://github.com/IBM/ibm-cos-sdk-python)

<details><summary>README extract</summary>

This package allows Python developers to write software that interacts with IBM Cloud Object Storage. It is a fork of the `boto3` library and can stand as a drop-in replacement if the application needs to connect to object storage using an S3-like API and does not make use of other AWS services.

IBM has added a Language Support Policy. ...

Sections: IBM Cloud Object Storage - Python SDK, Notice, Documentation, Quick start, Using Python, Using a Service Credential, Immutable Object Storage, Accelerated Archive, LEGACY: Aspera high-speed transfer, Building from source, Getting Help

</details>

### ibm-cos-sdk-core

Low-level, data-driven core of IBM SDK for Python

`pip install ibm-cos-sdk-core` · installs from source (sdist only) · licence: Apache Software License · rank 3687 · last release 2026-04-14 · [PyPI](https://pypi.org/project/ibm-cos-sdk-core/)

<details><summary>README extract</summary>

A low-level interface to IBM Cloud Object Storage based on the `ibm_botocore` package. This core package is the foundation for the `ibm-cos-sdk-python` package.

Documentation for `ibm-cos-sdk-python-core` can be found IBM COS Python Core SDK Documentation. ...

Sections: `ibm-cos-sdk-python-core`, Documentation, Getting Help

</details>

### inngest

Python SDK for Inngest

`pip install inngest` · installs (wheel) · licence: not stated · rank 3760 · last release 2026-11-02 · [PyPI](https://pypi.org/project/inngest/)

<details><summary>README extract</summary>

Serverless event-driven queues, background jobs, and scheduled jobs for Python.

 Add durable functions and workflows to any framework and platform.

 Read the documentation and get started in minutes.

Inngest's SDK adds durable functions to Python in a few lines of code. ...

Example:
```python
import flask
import inngest.flask
import requests

inngest_client = inngest.Inngest(
    app_id="flask_example",
    is_production=False,
)

@inngest_client.create_function(
    fn_id="find_person",
    trigger=inngest.TriggerEvent(event="app/person.find"),
)
def fetch_person(ctx: inngest.ContextSync) -> dict:
...
```

Sections: Inngest Python SDK, Getting started, Examples, Basic (no steps), Step run, Async function, Sending an event outside a function, Using in production

</details>

### ibm-cos-sdk-s3transfer

IBM S3 Transfer Manager

`pip install ibm-cos-sdk-s3transfer` · installs from source (sdist only) · licence: Apache Software License · rank 3959 · last release 2026-04-14 · [PyPI](https://pypi.org/project/ibm-cos-sdk-s3transfer/)

<details><summary>README extract</summary>

`s3transfer` is a Python library for managing IBM COS transfers.

</details>

### itables

Python DataFrames as interactive DataTables

`pip install itables` · installs (wheel) · licence: MIT License · rank 3979 · last release 2026-07-22 · [PyPI](https://pypi.org/project/itables/) · [docs](https://itables.org) · [source](https://github.com/mwouts/itables.git)

<details><summary>README extract</summary>

This package changes how Pandas and Polars DataFrames are rendered in Python notebooks and applications.
With `itables` you can display your tables as interactive DataTables
that you can sort, paginate, scroll or filter.

ITables is just about how tables are displayed. ...

Example:
```python
import itables

itables.init_notebook_mode()
```

Sections: Documentation, Quick start, ITables in Notebooks, ITables in Python applications

</details>

### inspect-swe

Software engineering agents for Inspect AI.

`pip install inspect-swe` · installs (wheel) · licence: MIT License · rank 4150 · last release 2026-10-20 · [PyPI](https://pypi.org/project/inspect-swe/) · [docs](https://meridianlabs-ai.github.io/inspect_swe/) · [source](https://github.com/meridianlabs-ai/inspect_swe)

<details><summary>README extract</summary>

Welcome to Inspect SWE, a suite of software engineering agents for Inspect AI.

For details on using Inspect SWE, please visit <

</details>

### isolate

Managed isolated environments for Python

`pip install isolate` · installs (wheel) · licence: not stated · rank 4179 · last release 2026-09-30 · [PyPI](https://pypi.org/project/isolate/) · [source](https://github.com/fal-ai/isolate)

<details><summary>README extract</summary>

Run any Python function, with any dependencies, in any machine you want. Isolate offers a
pluggable end-to-end solution for building, managing, and using isolated environments (virtualenv,
conda, remote, and more).

The fact that nearly every piece of software uses some other libraries or some
other programs is undeniable. ...

Sections: Isolate, Motivation, Running tests, Pre-commit, Commit format

</details>

### imutils

A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, displaying Matplotlib images, sorting contours, detecting edges, and much more easier with OpenCV and both Python 2.7 and Python 3.

`pip install imutils` · installs from source (sdist only) · licence: not stated · rank 4227 · last release 2021-01-15 · [PyPI](https://pypi.org/project/imutils/)

### isolate-proto

(internal) gRPC definitions for Isolate Cloud

`pip install isolate-proto` · installs (wheel) · licence: not stated · rank 4282 · last release 2026-10-16 · [PyPI](https://pypi.org/project/isolate-proto/)

<details><summary>README extract</summary>

For regenerating definitions:

The `<isolate version>` argument needs to be a tag from the isolate Github project minus the leading `v`.

</details>

### inspect-scout

Transcript Analysis for AI Agents

`pip install inspect-scout` · installs (wheel) · licence: MIT License · rank 4294 · last release 2026-10-29 · [PyPI](https://pypi.org/project/inspect-scout/) · [source](https://github.com/meridianlabs-ai/inspect_scout)

<details><summary>README extract</summary>

Welcome to Inspect Scout.

To get started with Inspect Scout, please see the documentation.

</details>

### impyla

Python client for the Impala distributed query engine

`pip install impyla` · installs (wheel) · licence: Apache License, Version 2.0 · rank 4335 · last release 2026-06-19 · [PyPI](https://pypi.org/project/impyla/) · [source](https://github.com/cloudera/impyla)

<details><summary>README extract</summary>

Python client for HiveServer2 implementations (e.g., Impala, Hive) for
distributed query engines.

For higher-level Impala functionality, including a Pandas-like interface over
distributed data sets, see the Ibis project.

Features:
* HiveServer2 compliant; works with Impala and Hive, including nested data

* Fully DB API 2.0 (PEP 249)-compliant Python client (similar to
sqlite or MySQL clients) supporting Python 3.8+.

* Works with Kerberos, LDAP, SSL, JWT ...

Example:
```python
from impala.dbapi import connect
conn = connect(host='my.host.com', port=21050) # auth_mechanism='PLAIN' for unsecured Hive connection, see function doc
cursor = conn.cursor()
cursor.execute('SELECT * FROM mytable LIMIT 100')
print cursor.description  # prints the result set's schema
results = cursor.fetchall()
...

</details>

### imap-tools

Work with email by IMAP

`pip install imap-tools` · installs (wheel) · licence: Apache Software License · rank 4456 · last release 2026-10-14 · [PyPI](https://pypi.org/project/imap-tools/)

<details><summary>README extract</summary>

High level lib for work with email by IMAP:

- Basic message operations: fetch, uids, numbers
- Parsed email message attributes
- Query builder for search criteria
- Actions with emails: copy, delete, flag, move, append
- Actions with folders: list, set, get, create, exists, rename, subscribe, delete, status ...

Example:
```python
from imap_tools import MailBox, AND

# Get date, subject and body len of all emails from INBOX folder
with MailBox('imap.mail.com').login('test@mail.com', 'pwd') as mailbox:
    for msg in mailbox.fetch():
        print(msg.date, msg.subject, len(msg.text or msg.html))
```

Sections: imap_tools 📧, 📘 Guide, 📋 Basic, 📧 Email attributes, 🔍 Search criteria, 🗃️ Actions with emails, 📁 Actions with folders, ⏳ IDLE workflow, ⚠️ Exceptions, 💡 Reasons, ✨ Thanks

</details>

### insightface

InsightFace Python Library

`pip install insightface` · installs (wheel) · licence: not stated · rank 4460 · last release 2026-10-03 · [PyPI](https://pypi.org/project/insightface/)

<details><summary>README extract</summary>

InsightFace provides face detection, recognition, alignment, and attributes
through Python and ONNX Runtime. Optional features include RGB liveness,
PrivateFrame for video face blur/mosaic, PersonAnalysis for person detection and
face/body reference matching, and the Evaluation Studio desktop GUI.

Example:
```python
import cv2
from insightface.app import FaceAnalysis
from insightface.data import get_image

app = FaceAnalysis()
app.prepare()
image = get_image("t1")
faces = app.get(image)
cv2.imwrite("t1_output.jpg", app.draw_on(image, faces))
```

...

</details>

### iregexp-check

(no summary)

`pip install iregexp-check` · installs (wheel) · licence: MIT License · rank 4544 · last release 2024-09-24 · [PyPI](https://pypi.org/project/iregexp-check/) · [source](https://github.com/jg-rp/rust-iregexp/tree/main/crates/python)

<details><summary>README extract</summary>

RFC 9485 I-Regexp: An Interoperable Regular Expression Format

Example:
```python
from iregexp_check import check

print(check(r"[ab]{3}"))  # True
print(check(r"[0-9]*?"))  # False
```

Sections: I-Regexp Check, Usage

</details>

### idna_ssl

Patch ssl.match_hostname for Unicode(idna) domains support

`pip install idna_ssl` · installs from source (sdist only) · licence: MIT License · rank 4598 · last release 2018-07-05 · [PyPI](https://pypi.org/project/idna_ssl/)

<details><summary>README extract</summary>

:info: Patch ssl.match_hostname for Unicode(idna) domains support

Example:
```python
from idna_ssl import patch_match_hostname  # noqa isort:skip
patch_match_hostname()  # noqa isort:skip

import asyncio

import aiohttp

URL = '

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            print(response)

loop = asyncio.get_event_loop()
...
```

Sections: idna-ssl, Usage, Motivation, Thanks

</details>

### idf-component-manager

Espressif IDF Component Manager

`pip install idf-component-manager` · installs (wheel) · licence: Apache Software License · rank 4659 · last release 2026-09-02 · [PyPI](https://pypi.org/project/idf-component-manager/) · [docs](https://docs.espressif.com/projects/idf-component-manager/en/latest/) · [source](https://github.com/espressif/idf-component-manager.git)

<details><summary>README extract</summary>

The IDF Component Manager is a tool that ensures the correct versions of all components required for a successful build are present in your ESP-IDF project.

- The Component Manager downloads the dependencies for your project automatically during a `CMake` run. ...

Sections: IDF Component Manager, Resources, Disabling the Component Manager, Using with a project, Defining dependencies in the manifest, Component metadata caching, External links, Add examples to the component, Custom example paths

</details>

### iterproxy

Give any iterable object capability to use .one(), .one_or_none(), .many(k), .skip(k), .all() API.

`pip install iterproxy` · installs (wheel) · licence: MIT License · rank 5003 · last release 2023-11-02 · [PyPI](https://pypi.org/project/iterproxy/)

<details><summary>README extract</summary>

You may seen the following code style in many ORM framework, this pattern provides a user friendly API to access items from the iterator object:

iterproxy library can give any iterable object similar capabilities.

Example:
```python
from iterproxy import IterProxy

# Suppose you have an iterable object
iterator = range(10)

# Convert it to a IterProxy object
proxy = IterProxy(iterator)
```

Sections: ⏩ Welcome to `iterproxy` Documentation, Usage Example

</details>

### influxdb3-python

Community Python client for InfluxDB 3.0

`pip install influxdb3-python` · installs (wheel) · licence: MIT License · rank 5104 · last release 2026-08-27 · [PyPI](https://pypi.org/project/influxdb3-python/)

<details><summary>README extract</summary>

`influxdb_client_3` is a Python module that provides a simple and convenient way to interact with InfluxDB 3.0. This module supports both writing data to InfluxDB and querying data using the Flight client, which allows you to execute SQL and InfluxQL queries on InfluxDB 3.0. ...

Example:
```python
from influxdb_client_3 import InfluxDBClient3, Point
```

Sections: InfluxDB 3.0 Python Client, Introduction, Dependencies, CLI (Agent-Friendly Query Tool), Run a query, Config precedence, Usage, Importing the Module, Initialization, Writing Data, Using Points, Write from file, Pandas DataFrame, Polars DataFrame

</details>

### inotify-simple

A simple wrapper around inotify. No fancy bells and whistles, just a literal wrapper with ctypes. Under 100 lines of code!

`pip install inotify-simple` · installs (wheel) · licence: BSD-2-Clause · rank 5296 · last release 2025-08-25 · [PyPI](https://pypi.org/project/inotify-simple/) · [docs](http://inotify-simple.readthedocs.io/) · [source](https://github.com/chrisjbillington/inotify_simple.git)

<details><summary>README extract</summary>

`inotify-simple` is a simple Python wrapper around
inotify. No fancy bells and
whistles, just a literal wrapper with ctypes. Less than 100 lines of code!

`inotify_init1()` is wrapped as a file-like object, `INotify()`, holding the inotify
file descriptor. ...

Example:
```python
import os
from inotify_simple import INotify, flags

os.mkdir('/tmp/inotify_test')

inotify = INotify()
watch_flags = flags.CREATE | flags.DELETE | flags.MODIFY | flags.DELETE_SELF
wd = inotify.add_watch('/tmp/inotify_test', watch_flags)

# Now create, delete and modify some files in the directory being monitored:
os.chdir('/tmp/inotify_test')
...
```

Sections: inotify-simple 2.0, Introduction, Example usage

</details>

### icalendar-searcher

Search, filter and sort iCalendar components

`pip install icalendar-searcher` · installs (wheel) · licence: GPL-3.0-or-later OR Apache-2.0 · rank 5440 · last release 2026-10-21 · [PyPI](https://pypi.org/project/icalendar-searcher/) · [source](https://github.com/pycalendar/icalendar-searcher)

_README extract left out: share-alike licence._

### inversion

Flexible version handling

`pip install inversion` · installs (wheel) · licence: BSD-3-Clause OR Apache-2.0 · rank 5897 · last release 2026-10-15 · [PyPI](https://pypi.org/project/inversion/)

<details><summary>README extract</summary>

inversion is a Python library for handling software versions and specifiers,
adapted from the `packaging` package.

Example:
```python
>>> from inversion import python
>>> v1 = python.Version('1.0')
>>> s1 = python.SpecifierSet('~=1.0')
>>> v1 in s1
True

>>> from inversion import loose
>>> v2 = loose.Version('1.0')
>>> s2 = loose.SpecifierSet('>=1.0')
>>> v2 in s2
True
```

Sections: inversion, An Example

</details>

### impacket

Network protocols Constructors and Dissectors

`pip install impacket` · installs (wheel) · licence: Apache modified · rank 5925 · last release 2026-05-19 · [PyPI](https://pypi.org/project/impacket/)

<details><summary>README extract</summary>

Copyright Fortra, LLC and its affiliated companies. All rights reserved.

Impacket was originally created by SecureAuth, and now maintained by Fortra's Core Security.

Impacket is a collection of Python classes for working with network
protocols. ...

Sections: Impacket, Getting Impacket, Latest version, Setup, Quick start, Licensing, Disclaimer, Contact Us

</details>

### inspect-test-utils

Simple models and tasks for integration testing

`pip install inspect-test-utils` · installs (wheel) · licence: MIT · rank 6007 · last release 2026-10-22 · [PyPI](https://pypi.org/project/inspect-test-utils/) · [source](https://github.com/METR/inspect-test-utils)

<details><summary>README extract</summary>

inspect-test-utils

A small collection of tasks, scorers, and a simple model for use with the Inspect AI framework. It is designed to support integration/acceptance tests, demos, and reproductions by providing: ...

</details>

### icechunk

Icechunk Python

`pip install icechunk` · installs (wheel) · licence: not stated · rank 6176 · last release 2026-10-27 · [PyPI](https://pypi.org/project/icechunk/)

<details><summary>README extract</summary>

> [!TIP]
> Icechunk 2.0 is released! Better consistency, performance, and reliability for tensor storage

Icechunk is an open-source (Apache 2.0), transactional storage engine for tensor / ND-array data designed for use on cloud object storage. ...

Sections: Icechunk, Documentation and Resources, Crate Structure, Icechunk Overview, Key Concepts, Groups, Arrays, and Chunks, Snapshots, Branches and Tags, Chunk References, How Does It Work?

</details>

### ipsw-parser

python3 utility for parsing and extracting data from IPSW

`pip install ipsw-parser` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6433 · last release 2026-10-28 · [PyPI](https://pypi.org/project/ipsw-parser/)

_README extract left out: share-alike licence._

### ibm-quantum-schemas

IBM Quantum Pydantic models.

`pip install ibm-quantum-schemas` · installs (wheel) · licence: Apache-2.0 · rank 6487 · last release 2026-10-16 · [PyPI](https://pypi.org/project/ibm-quantum-schemas/)

<details><summary>README extract</summary>

This repository contains the Pydantic models that describe the inputs and outputs of IBM Quantum
primitives and programs, to allow easier programmatic interfacing from Python.

The resulting `ibm-quantum-schemas` Python package contains the versioned definition of such
inputs and outputs, using the following structure: ...

</details>

### icontract

Provide design-by-contract with informative violation messages.

`pip install icontract` · installs (wheel) · licence: License :: OSI Approved :: MIT License · rank 6614 · last release 2026-01-29 · [PyPI](https://pypi.org/project/icontract/)

<details><summary>README extract</summary>

icontract provides design-by-contract to Python3 with informative
violation messages and inheritance.

It also gives a base for a flourishing of a wider ecosystem:

* A linter pyicontract-lint,
* A sphinx plug-in sphinx-icontract,
* A tool icontract-hypothesis for automated testing and ghostwriting test files which infers
 Hypothesis strategies ...

Example:
```python
>>> import icontract

>>> @icontract.require(lambda x: x > 3)
... def some_func(x: int, y: int = 5) -> None:
...     pass
...

>>> some_func(x=5)

# Pre-condition violation
>>> some_func(x=1)
Traceback (most recent call last):
  ...
icontract.errors.ViolationError: File <doctest README.rst[1]>, line 1 in <module>:
x > 3:
x was 1
y was 5

...
```

Sections: icontract, Related Projects, Teasers, Versioning

</details>

### ipinfo

Official Python library for IPInfo

`pip install ipinfo` · installs (wheel) · licence: Apache License 2.0 · rank 6673 · last release 2026-04-22 · [PyPI](https://pypi.org/project/ipinfo/) · [docs](https://ipinfo.io/developers)

<details><summary>README extract</summary>

This is the official Python client library for the IPinfo.io IP address API, allowing you to look up your own IP address, or get any of the following details for an IP:

- IP geolocation (city, region, country, postal code, latitude, and longitude) ...

Example:
```python
>>> import ipinfo
>>> access_token = '123456789abc'
>>> handler = ipinfo.getHandler(access_token)
>>> ip_address = '216.239.36.21'
>>> details = handler.getDetails(ip_address)
>>> details.city
'Mountain View'
>>> details.loc
'37.3861,-122.0840'
```

Sections: []( IPinfo Python Client Library, Getting Started, Quick Start, Async/Await, Usage, Authentication, Details Data, Country Name, Longitude and Latitude, Accessing all properties, Lite API, Core API, Plus API, Residential Proxy API

</details>

### icalevents

Simple Python 3 library to download, parse and query iCal sources.

`pip install icalevents` · installs (wheel) · licence: MIT License · rank 6762 · last release 2025-09-26 · [PyPI](https://pypi.org/project/icalevents/)

<details><summary>README extract</summary>

Simple Python 3 library to download, parse and query iCal sources.

last push:

master:

Example:
```python
from icalevents.icalevents import events

es  = events(<iCloud URL>, fix_apple=True)
```

Sections: iCalEvents, Build info, Documentation, Usage, iCloud, Google

</details>

### imblearn

Toolbox for imbalanced dataset in machine learning.

`pip install imblearn` · installs (wheel) · licence: not stated · rank 6817 · last release 2017-01-19 · [PyPI](https://pypi.org/project/imblearn/)

### inotify

An adapter to Linux kernel support for inotify directory-watching.

`pip install inotify` · installs (wheel) · licence: GPL 2 · rank 6934 · last release 2025-07-07 · [PyPI](https://pypi.org/project/inotify/)

_README extract left out: share-alike licence._

### ipyevents

A custom widget for returning mouse and keyboard events to Python

`pip install ipyevents` · installs (wheel) · licence: BSD License · rank 7062 · last release 2025-09-15 · [PyPI](https://pypi.org/project/ipyevents/)

<details><summary>README extract</summary>

*ipyevents* provides a custom widget for returning mouse and keyboard events to
Python. Use it to:

 - add keyboard shortcuts to an existing widget;
 - react to the user clicking on an image;
 - add callbacks on arbitrary mouse and keyboard events.

See this demo notebook for documentation.

Special thanks to the contributors to `ipyevents`! ...

Sections: ipyevents, Browsers events for your jupyter widgets, Try it on binder, Documentation

</details>

### importlib

Backport of importlib.import_module() from Python 2.7

`pip install importlib` · installs from source (sdist only) · licence: not stated · rank 7079 · last release 2016-08-31 · [PyPI](https://pypi.org/project/importlib/)

<details><summary>README extract</summary>

This package contains the code from importlib as found in Python 2.7. It is
provided so that people who wish to use `importlib.import_module()` with a
version of Python prior to 2.7 or in 3.0 have the function readily available.
The code in no way deviates from what can be found in the Python 2.7 standard
library. ...

Sections: Purpose, Notice about maintenance

</details>

### icet

A Pythonic approach to cluster expansions

`pip install icet` · installs from source (sdist only) · licence: MPL-2.0 · rank 7136 · last release 2026-09-05 · [PyPI](https://pypi.org/project/icet/) · [docs](https://icet.materialsmodeling.org) · [source](https://gitlab.com/materials-modeling/icet/)

<details><summary>README extract</summary>

icet is a tool for the construction and sampling of alloy cluster expansions.
A detailed description of the functionality provided as well as an extensive tutorial can be found in the user guide. ...

Example:
```python
cs = ClusterSpace(primitive_cell, cutoffs, species)
sc = StructureContainer(cs)
for structure in training_structures:
    sc.add_structure(structure)
opt = Optimizer(sc.get_fit_data())
opt.train()
ce = ClusterExpansion(cs, opt.parameters)
```

</details>

### igittigitt

A spec-compliant .gitignore parser and path filter, 100% git-compatible, with an include/whitelist mode and a streaming, memory-bounded CLI

`pip install igittigitt` · installs (wheel) · licence: MIT License · rank 7546 · last release 2026-10-28 · [PyPI](https://pypi.org/project/igittigitt/) · [source](https://github.com/bitranox/igittigitt.git)

<details><summary>README extract</summary>

<!-- Badges -->

`igittigitt` is a spec-compliant `.gitignore` parser for Python - a library and a
command-line tool. Point it at `.gitignore` rules (or pass rules as strings) and ask
whether a path is ignored, or use it directly as the `ignore=` callback of
`shutil.copytree`.

Features:
- 100% git-compatible matching. The matching engine reproduces git's algorithm
 exactly - a single ordered pass with *last-matching-pattern-wins*, correct
 negations (`!pattern`), the rule that a file cannot be re-included when a parent
 directory ...

Example:
```python
import igittigitt

parser = igittigitt.IgnoreParser()

# discover and parse every .gitignore below base_dir (per-directory precedence)
parser.parse_rule_files(base_dir="/opt/project")

# ... or add rules explicitly
...

</details>

### ignore-python

Python bindings for the Rust crate ignore

`pip install ignore-python` · installs (wheel) · licence: not stated · rank 7592 · last release 2026-10-22 · [PyPI](https://pypi.org/project/ignore-python/) · [docs](https://borsattoz.github.io/ignore-python) · [source](https://github.com/borsattoz/ignore-python)

<details><summary>README extract</summary>

This is a Python library that binds to the Rust crate
ignore.

ignore's Python bindings can be used for building a fast recursive
directory iterator that respects various filters such as globs, file
types and `.gitignore` files.

Example:
```python
from ignore import Walk

for entry in Walk("./"):
    print(entry.path())
```

Sections: ignore in Python, Example, Example: advanced, On Arch Linux, From pip

</details>

### ipylab

Control JupyterLab from Python notebooks

`pip install ipylab` · installs (wheel) · licence: BSD License · rank 7716 · last release 2025-06-24 · [PyPI](https://pypi.org/project/ipylab/) · [source](https://github.com/jtpio/ipylab)

<details><summary>README extract</summary>

Control JupyterLab from Python notebooks.

The goal is to provide access to most of the JupyterLab environment from Python notebooks. For example:

- Adding widgets to the main area `DockPanel`, left, right or top area
- Build more advanced interfaces leveraging `SplitPanel`, `Toolbar` and other Lumino widgets ...

Sections: ipylab, Try it online, Examples, Add Jupyter Widgets to the JupyterLab interface, Execute Commands, Custom Python Commands and Command Palette, Build small applications, Compatibility with RetroLab, Running the examples locally, Under the hood, Related projects

</details>

### ipadic

IPAdic packaged for Python

`pip install ipadic` · installs from source (sdist only) · licence: not stated · rank 8182 · last release 2020-07-20 · [PyPI](https://pypi.org/project/ipadic/)

<details><summary>README extract</summary>

This is a version of IPAdic packaged for use in Python with
mecab-python3 or
fugashi.

This is the version of IPAdic included with MeCab. It hasn't been updated since
at least 2007. The organization that created it no longer does this kind of
work. The contact URLs listed in the source no longer resolve. ...

Sections: ipadic-py, You Shouldn't Use This, Usage

</details>

### isosurfaces

Construct isolines/isosurfaces over a 2D/3D scalar field defined by a function (not a uniform grid)

`pip install isosurfaces` · installs (wheel) · licence: MIT License · rank 8192 · last release 2024-02-26 · [PyPI](https://pypi.org/project/isosurfaces/)

<details><summary>README extract</summary>

Construct isolines/isosurfaces of a 2D/3D scalar field defined by a function, i.e. curves over which `f(x,y)=0` or surfaces over which `f(x,y,z)=0`. Most similar libraries use marching squares or similar over a uniform grid, but this uses a quadtree to avoid wasting time sampling many far from the implicit surface. ...

Example:
```python
from isosurfaces import plot_isoline
import numpy as np

def f(x, y):
    return y * (x - y) ** 2 - 4 * x - 8

curves = plot_isoline(
    lambda u: f(u[0], u[1]),
    np.array([-8, -6]),
    np.array([8, 6]),
    # Increasing min_depth can help if you have small features
    min_depth=3,
...
```

Sections: Isosurfaces, Usage, Dev examples, Code formatting, Related

</details>

### ibm-watsonx-orchestrate-core

Core Shared Dependecies of the IBM watsonx Orchestrate ADK

`pip install ibm-watsonx-orchestrate-core` · installs (wheel) · licence: MIT License · rank 8623 · last release 2026-10-22 · [PyPI](https://pypi.org/project/ibm-watsonx-orchestrate-core/)

### ibm-watsonx-orchestrate-clients

IBM watsonx Orchestrate ADK API Client Library

`pip install ibm-watsonx-orchestrate-clients` · installs (wheel) · licence: MIT License · rank 8626 · last release 2026-10-22 · [PyPI](https://pypi.org/project/ibm-watsonx-orchestrate-clients/)

### ioc-fanger

Python package to defang and fang indicators of compromise from text.

`pip install ioc-fanger` · installs (wheel) · licence: MIT License · rank 8633 · last release 2026-06-17 · [PyPI](https://pypi.org/project/ioc-fanger/) · [docs](https://github.com/ioc-fang/ioc-fanger) · [source](https://github.com/ioc-fang/ioc-fanger)

<details><summary>README extract</summary>

Python package to fang (`example[.]com => example.com`) and defang (`example.com => example[.]com`) indicators of compromise in text.

Read more in our interactive documentation!

`ioc_fanger.fang` recognises the following defanging patterns and restores them to their normal form: ...

Sections: IOC Fanger, What can be fanged?, What can be defanged?, Updating Benchmarks

</details>

### inspect-petri

An auditing agent that enables automated monitoring and interaction with language models to detect potential alignment issues, reward hacking, and other concerning behaviors.

`pip install inspect-petri` · installs (wheel) · licence: MIT License · rank 8749 · last release 2026-10-01 · [PyPI](https://pypi.org/project/inspect-petri/) · [source](https://github.com/meridianlabs-ai/inspect_petri)

<details><summary>README extract</summary>

Welcome to Inspect Petri, an auditing agent that enables automated monitoring and interaction with language models to detect potential alignment issues, reward hacking, and other concerning behaviors.

Petri helps you rapidly test concrete alignment hypotheses end‑to‑end. It:

- Generates realistic audit scenarios (via your seed instructions) ...

</details>

### ipydagred3

ipywidgets wrapper around dagre-d3

`pip install ipydagred3` · installs (wheel) · licence: Apache Software License · rank 9688 · last release 2023-10-31 · [PyPI](https://pypi.org/project/ipydagred3/) · [source](https://github.com/timkpaine/ipydagred3)

<details><summary>README extract</summary>

ipywidgets library for drawing directed acyclic graphs in jupyterlab using dagre-d3

Features:
- Dynamically create and modify graphs from python
- Change color, shape, tooltip, etc
- Click events (click on node or edge and get event in ipywidget indicating source, good for node inspector tools)

Sections: ipydagred3, Features, Tooltips and Click events, Examples

</details>

### internetarchive

A Python interface to archive.org.

`pip install internetarchive` · installs (wheel) · licence: AGPL-3.0-only · rank 9729 · last release 2026-10-22 · [PyPI](https://pypi.org/project/internetarchive/) · [docs](https://archive.org/developers/internetarchive/) · [source](https://github.com/jjjake/internetarchive)

_README extract left out: share-alike licence._

### ipyfilechooser

Python file chooser widget for use in Jupyter/IPython in conjunction with ipywidgets

`pip install ipyfilechooser` · installs (wheel) · licence: MIT License · rank 9786 · last release 2021-09-15 · [PyPI](https://pypi.org/project/ipyfilechooser/)

<details><summary>README extract</summary>

A simple Python file chooser widget for use in Jupyter/IPython in conjunction with ipywidgets. The selected path and file are available via `.selected_path` and `.selected_filename` respectvely or as a single combined filepath via `.selected`. The dialog can be reset to its default path and filename by using `.reset()`. ...

Example:
```python
from ipyfilechooser import FileChooser

# Create and display a FileChooser widget
fc = FileChooser('/Users/crahan/FC demo')
display(fc)

# Print the selected path, filename, or both
print(fc.selected_path)
print(fc.selected_filename)
print(fc.selected)

# Change defaults and reset the dialog
fc.default_path = '/Users/crahan/'
...
```

...

</details>

### imgcat

imgcat as Python API and CLI

`pip install imgcat` · installs from source (sdist only) · licence: MIT License · rank 9819 · last release 2024-11-21 · [PyPI](https://pypi.org/project/imgcat/)

<details><summary>README extract</summary>

The imgcat CLI, written in Python (and Python API, too).

It works with iTerm2 and WezTerm, and even inside tmux (for tmux, see Notes below).

Installation and Usage

Command-line interface (similar to iTerm2's imgcat):

Python API:

Matplotlib Backend: `module://imgcat`

IPython magic (works both in terminal and notebook)

Notes ...

Example:
```python
>>> from imgcat import imgcat

# from the content of image (e.g. buffer in python3, str in python2)
>>> imgcat(open("./local_image.png"))

# or numpy arrays!
>>> im = skimage.data.chelsea()   # [300, 451, 3] ndarray, dtype=uint8
>>> imgcat(im, height=7)

# matplotlib, PIL.Image, etc.
>>> imgcat(Image.fromarray(im))

...
```

</details>

### indic-nlp-library

The goal of the Indic NLP Library is to build Python based libraries for common text processing and Natural Language Processing in Indian languages.

`pip install indic-nlp-library` · installs (wheel) · licence: MIT License · rank 9836 · last release 2023-05-15 · [PyPI](https://pypi.org/project/indic-nlp-library/)

<details><summary>README extract</summary>

The goal of the Indic NLP Library is to build Python based libraries for common text processing and Natural Language Processing in Indian languages. Indian languages share a lot of similarity in terms of script, phonology, language syntax, etc. ...

Sections: Indic NLP Library, Pre-requisites, Configuration, Usage, Getting Started, Documentation, Citing, Website, Companies, Organizations, Projects using IndicNLP Library, Revision Log

</details>

### itanium-demangler

Pure Python parser for mangled itanium symbols

`pip install itanium-demangler` · installs (wheel) · licence: BSD · rank 10007 · last release 2022-08-20 · [PyPI](https://pypi.org/project/itanium-demangler/)

<details><summary>README extract</summary>

The *Python Itanium Demangler* is a pure Python parser for the Itanium C++ ABI symbol mangling language. Note that MSVC mangling language is not supported.

This demangler generates an abstract syntax tree from mangled symbols, which can be used for directly extracting type information, as opposed to having to interpret the C++ source code ...

Example:
```python
from itanium_demangler import parse as demangle

ast = demangle("_ZN5boost6chrono24process_system_cpu_clock3nowEv")

print(repr(ast))
# <FuncNode func <Node qual_name (<Node name 'boost'>, <Node name 'chrono'>, <Node name 'process_system_cpu_clock'>, <Node name 'now'>)> (<Node builtin 'void'>,) None>

print(ast)
...
```

Sections: Itanium Demangler, Requirements, Usage, Future considerations

</details>

### icsneopy

(no summary)

`pip install icsneopy` · installs (wheel) · licence: not stated · rank 10122 · last release 2026-11-01 · [PyPI](https://pypi.org/project/icsneopy/) · [docs](https://libicsneo.readthedocs.io) · [source](https://github.com/intrepidcs/libicsneo)

<details><summary>README extract</summary>

libicsneo is the Intrepid Control Systems device
communication library. Installation and usage documentation can be found within
each of the respective APIs.

Sections: libicsneo, Documentation

</details>

### idf-build-apps

Tools for building ESP-IDF related apps.

`pip install idf-build-apps` · installs (wheel) · licence: Apache Software License · rank 10427 · last release 2026-10-26 · [PyPI](https://pypi.org/project/idf-build-apps/) · [docs](https://docs.espressif.com/projects/idf-build-apps) · [source](https://github.com/espressif/idf-build-apps)

<details><summary>README extract</summary>

`idf-build-apps` is a tool that helps users find and build ESP-IDF, and ESP8266 RTOS projects in a large scale.

A project using ESP-IDF SDK, or ESP8266 RTOS SDK typically contains:

- Build recipe in CMake or Make and the main component with app sources
- (Optional) One or more sdkconfig files

`app` is the abbreviation for application. ...

Sections: idf-build-apps, What is an `app`?, Basic Usage, Quick CLI Example, Documentation

</details>

### img2table

img2table is a table identification and extraction Python Library for PDF and images, based on OpenCV image processing

`pip install img2table` · installs (wheel) · licence: MIT · rank 10442 · last release 2026-05-10 · [PyPI](https://pypi.org/project/img2table/)

<details><summary>README extract</summary>

`img2table` is a simple, easy to use, table identification and extraction Python Library based on OpenCV image
processing that supports most common image file formats as well as PDF files.

Thanks to its design, it provides a practical and lighter alternative to Neural Networks based solutions, especially for usage on CPU.

Features:
- Table identification for images and PDF files, including bounding boxes at the table cell level
- Handling of complex table structures such as merged cells
- Table content extraction by providing support for OCR services / tools ...

Example:
```python
from img2table.document import Image

image = Image(src,
              detect_rotation=False)
```

Sections: img2table, Features, Usage, Documents, Images, Parameters, PDF, OCR

</details>

### iamdata

IAM data for AWS actions, resources, and conditions based on IAM policy documents. Checked for updates daily.

`pip install iamdata` · installs (wheel) · licence: MIT License · rank 10449 · last release 2026-11-08 · [PyPI](https://pypi.org/project/iamdata/)

<details><summary>README extract</summary>

This is a simple package for utilizing AWS IAM data for Services, Actions, Resources, and Condition Keys. Data is embedded in the python package.

New data is checked against the AWS IAM documentation and updated daily if there are changes.

Example:
```python
from iamdata import IAMData

iam_data = IAMData()
print(f"Data Version {iam_data.data_version()} updated at {iam_data.data_updated_at()}")
for service_key in iam_data.services.get_service_keys():
    service_name = iam_data.services.get_service_name(service_key)
    print(f"Getting Actions for {service_name}")
...
```

Sections: IAM Data In Python Package, Usage, API, Services, Actions, Resources, Conditions Keys, Version Info

</details>

### identity

This is an authentication/authorization library, currently optimized for web apps. It provides some higher level APIs built on top of Microsoft's MSAL Python.

`pip install identity` · installs (wheel) · licence: MIT License · rank 10454 · last release 2025-07-07 · [PyPI](https://pypi.org/project/identity/) · [docs](https://identity-library.readthedocs.io/)

<details><summary>README extract</summary>

<!-- The following summary is reused in, and needs to be in-sync with, the docs/index.rst -->
This Identity library is an authentication/authorization library that:

* Suitable for apps that are targeting end users on
 Microsoft identity platform, a.k.a. ...

Sections: Identity library, Versions

</details>

### islo

Typed Python SDK for the Islo sandbox platform

`pip install islo` · installs (wheel) · licence: not stated · rank 10523 · last release 2026-10-12 · [PyPI](https://pypi.org/project/islo/) · [docs](https://docs.islo.dev) · [source](https://github.com/islo-labs/islo-sdk)

<details><summary>README extract</summary>

The Islo Python library provides convenient access to the Islo APIs from Python.

Example:
```python
from islo import Islo

# Automatically reads ISLO_API_KEY from environment
client = Islo()

# Create a sandbox
sandbox = client.sandboxes.create_sandbox(
    name="my-sandbox",
    image="ubuntu:22.04",
    vcpus=2,
    memory_mb=4096,
)

# Execute a command
result = client.sandboxes.exec_in_sandbox(
    sandbox_name=sandbox.name,
...
```

Sections: Islo Python Library, Quick Start, Authentication, Environment variable (recommended), Explicit token, Auto-refreshing token provider, Configuration, Regenerating the SDK, Reference, Usage, Environments, Async Client, Exception Handling, Advanced

</details>

### in-n-out

plugable dependency injection and result processing

`pip install in-n-out` · installs (wheel) · licence: BSD License · rank 10617 · last release 2024-04-22 · [PyPI](https://pypi.org/project/in-n-out/) · [source](https://github.com/pyapp-kit/in-n-out)

<details><summary>README extract</summary>

Python dependency injection you can taste.

A lightweight dependency injection and result processing framework
for Python using type hints. Emphasis is on simplicity, ease of use,
and minimal impact on source code.

This also supports processing *return* values as well
(injection of intentional side effects):

Example:
```python
import in_n_out as ino

class Thing:
    def init(self, name: str):
        self.name = name

# use ino.inject to create a version of the function
# that will retrieve the required dependencies at call time
@ino.inject
def func(thing: Thing):
    return thing.name

def give_me_a_thing() -> Thing:
    return Thing("Thing")

...
```

Sections: in-n-out, Alternatives

</details>

### invisible-watermark

The library for creating and decoding invisible image watermarks

`pip install invisible-watermark` · installs (wheel) · licence: MIT License · rank 10710 · last release 2023-07-06 · [PyPI](https://pypi.org/project/invisible-watermark/)

<details><summary>README extract</summary>

invisible-watermark is a python library and command line tool for creating invisible watermark over image (a.k.a. blink image watermark, digital image watermark). The algorithm doesn't rely on the original image. ...

Example:
```python
import cv2
from imwatermark import WatermarkEncoder

bgr = cv2.imread('test.png')
wm = 'test'

encoder = WatermarkEncoder()
encoder.set_watermark('bytes', wm.encode('utf-8'))
bgr_encoded = encoder.encode(bgr, 'dwtDct')

cv2.imwrite('test_wm.png', bgr_encoded)
```

Sections: invisible-watermark, Library API, Embed watermark, Decode watermark, CLI Usage, Test Result, Input, Attack Performance, Running Speed (CPU Only), RivaGAN Experimental

</details>

### ifcfg

Python ifconfig wrapper for Unix/Linux/MacOSX + ipconfig for Windows

`pip install ifcfg` · installs (wheel) · licence: BSD License · rank 11034 · last release 2023-04-19 · [PyPI](https://pypi.org/project/ifcfg/)

<details><summary>README extract</summary>

Ifcfg is a cross-platform (Windows/Unix) library for parsing `ifconfig` and
`ipconfig` output in Python. It is useful for pulling information such as IP,
Netmask, MAC Address, Hostname, etc.

A fallbacks to `ip` is included for newer Unix systems w/o `ifconfig`. Windows
systems are supported (in English) through `ipconfig`.

Example:
```python
import ifcfg
import json

for name, interface in ifcfg.interfaces().items():
    # do something with interface
    print interface['device']       # Device name
    print interface['inet']         # First IPv4 found
    print interface['inet4']        # List of ips
    print interface['inet6']        # List of ips
...
```

Sections: Python cross-platform network interface discovery, Usage, 0.24

</details>

### image

Django application that provides cropping, resizing, thumbnailing, overlays and masking for images and videos with the ability to set the center of attention,

`pip install image` · installs (wheel) · licence: BSD · rank 11053 · last release 2026-11-07 · [PyPI](https://pypi.org/project/image/)

<details><summary>README extract</summary>

Django application that provides cropping, resizing, thumbnailing, overlays and masking for images and videos with the ability to set the center of attention,

</details>

### ipycanvas

Interactive widgets library exposing the browser's Canvas API

`pip install ipycanvas` · installs (wheel) · licence: BSD License · rank 11413 · last release 2025-12-11 · [PyPI](https://pypi.org/project/ipycanvas/)

<details><summary>README extract</summary>

Interactive Canvas in Jupyter

ipycanvas is a lightweight, fast and stable library exposing the browser's Canvas API to IPython.
It allows you to draw simple primitives directly from Python like text, lines, polygons, arcs, images etc. This simple toolset allows you to draw literally anything!

You can try it online by clicking on this badge:

Sections: ipycanvas, Try it online!, Documentation, Questions?, Examples, Create John Conway's Game Of Life, Draw Particles from IPython, Custom Sprites, Draw data directly from a NumPy array, Create your own plotting library fully in Python

</details>

### imfp

Python package for downloading economic data from the International Monetary Fund SDMX 3.0 API, following econdataverse conventions.

`pip install imfp` · installs (wheel) · licence: MIT License · rank 11626 · last release 2026-10-22 · [PyPI](https://pypi.org/project/imfp/) · [source](https://github.com/Promptly-Technologies-LLC/imfp)

<details><summary>README extract</summary>

`imfp`, by Christopher C. Smith, is a Python package for downloading data from the International Monetary Fund's RESTful JSON API.

📚 Full Documentation

Features:
- Comprehensive access to IMF's extensive economic databases
- Dataset, dimension, and code discovery
- Tidy `pandas` DataFrame output, with numeric observation values
- Rate limit and bandwidth management

Example:
```python
import imfp

# 1. Find a dataset
dataflows = imfp.imf_get_dataflows()

# 2. See how it can be filtered
dimensions = imfp.imf_get_datastructure("PCPS")

# 3. Find valid codes for those dimensions
codes = imfp.imf_get_codelists(["INDICATOR", "FREQUENCY"], "PCPS")

# 4. Fetch the data
df = imfp.imf_get(
    "PCPS",
    dimensions={
...
```

Sections: imfp, Quick Start, Upgrading from 1.x, Key Features

</details>

### icu4py

Python bindings to the ICU (International Components for Unicode) library (ICU4C).

`pip install icu4py` · installs (wheel) · licence: MIT · rank 11637 · last release 2026-10-20 · [PyPI](https://pypi.org/project/icu4py/) · [docs](https://icu4py.readthedocs.io/) · [source](https://github.com/adamchainz/icu4py)

<details><summary>README extract</summary>

Python bindings to the ICU (International Components for Unicode) library (ICU4C).

Please see

Sections: icu4py, Documentation

</details>

### inspect-viz

Data visualization for Inspect AI large language model evalutions.

`pip install inspect-viz` · installs (wheel) · licence: MIT License · rank 11837 · last release 2026-10-19 · [PyPI](https://pypi.org/project/inspect-viz/) · [docs](https://meridianlabs-ai.github.io/inspect_viz/) · [source](https://github.com/meridianlabs-ai/inspect_viz)

<details><summary>README extract</summary>

Welcome to Inspect Viz, a data visualisation library for Inspect AI. Inspect Viz provides flexible tools for high quality interactive visualisations from Inspect evaluations.

To get started with Inspect Viz, please see the documentation at <

</details>

### imbalance-xgboost

XGBoost for label-imbalanced data: XGBoost with weighted and focal loss functions

`pip install imbalance-xgboost` · installs (wheel) · licence: MIT License · rank 11962 · last release 2021-02-08 · [PyPI](https://pypi.org/project/imbalance-xgboost/)

<details><summary>README extract</summary>

This software includes the codes of Weighted Loss and Focal Loss [1] implementations for Xgboost 2 in binary classification problems. The principal reason for us to use Weighted and Focal Loss functions is to address the problem of label-imbalanced data. ...

Example:
```python
from imxgboost.imbalance_xgb import imbalance_xgboost as imb_xgb
```

Sections: Imbalance-Xgboost, Software Update, Version Notification, Usage, Theories and derivatives, 1. Weighted Imbalance (Cross-entropoy) Loss, 2. Focal Loss, References

</details>

### ibapi

Official Interactive Brokers API

`pip install ibapi` · installs from source (sdist only) · licence: Other/Proprietary License · rank 12006 · last release 2020-12-06 · [PyPI](https://pypi.org/project/ibapi/)

<details><summary>README extract</summary>

A couple of things/definitions/conventions:

- a *low level message* is some data prefixed with its size
- a *high level message* is a list of fields separated by the NULL
 character; the fields are all strings; the message ID is the first
 field, the come others whose number and semantics depend on the
 message itself ...

</details>

### ipyparallel

Interactive Parallel Computing with IPython

`pip install ipyparallel` · installs (wheel) · licence: BSD License · rank 12199 · last release 2026-05-12 · [PyPI](https://pypi.org/project/ipyparallel/)

<details><summary>README extract</summary>

IPython Parallel (`ipyparallel`) is a Python package and collection of CLI scripts for controlling clusters of IPython processes, built on the Jupyter protocol.

IPython Parallel provides the following commands:

- ipcluster - start/stop/list clusters
- ipcontroller - start a controller
- ipengine - start an engine

Example:
```python
import os
import ipyparallel as ipp

cluster = ipp.Cluster(n=4)
with cluster as rc:
    ar = rc[:].apply_async(os.getpid)
    pid_map = ar.get_dict()
```

Sections: Interactive Parallel Computing with IPython, Run

</details>

### icd9cms

A utility for searching across the full icd9cms (2015) diagnosis hierarchy

`pip install icd9cms` · installs (wheel) · licence: MIT License · rank 12204 · last release 2018-11-30 · [PyPI](https://pypi.org/project/icd9cms/)

<details><summary>README extract</summary>

A helper utility that offers fast lookup of ICD9-CM V32 (2015) codes,
complete with the entire hierarchy.

Features:
ICD9-CMS extends the original (already outdated) ICD9 code standard.

The billable ICD9 codes are available here.
However, these flat files lack the non-billable hierarchical relations between codes and the intermediate code descriptions. ...

Example:
```python
>>> from icd9cms.icd9 import search
>>>search('001')
001:Cholera:None
>>> # Codes can be searched for with or without the implied '.'
>>> search('001.0') == search('0010')
True
>>> # The root node is under the code 'n/a' or None
>>> search('n/a')
n/a:root:None
```

...

</details>

### infini-gram

A Python package for infini-gram

`pip install infini-gram` · does not install on CPython 3.14 · licence: Apache 2.0 · rank 12400 · last release 2025-05-15 · [PyPI](https://pypi.org/project/infini-gram/)

<details><summary>README extract</summary>

To use this package, please check out its documentation here: <

To learn more about infini-gram:
* Paper: <
* Project Home: <
* Web Interface: <
* API Endpoint: <
* Python Package: <
* Code: <

</details>

### iab-tcf

A Python implementation of the IAB consent strings (v1.1 and v2)

`pip install iab-tcf` · installs (wheel) · licence: MIT · rank 12412 · last release 2026-11-02 · [PyPI](https://pypi.org/project/iab-tcf/) · [docs](https://iab-tcf.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

A Python implementation of the IAB consent strings (v1.1 and v2)

Example:
```python
from iab_tcf import decode

consent = decode("CO5VTlWO5VTlWH1AAAENAwCwAIAAAAAAAIAAAAoAAAAA.YAAAAAAAAAA")

print(consent.version) # prints 2
```

Sections: iab-tcf, Documentation, A Simple Example, Tests, Thanks

</details>

### instance-repo

InstanceRepo SDK — 评测 Instance 统一存储客户端（SDK-only；控制面由 apiserver 承载）

`pip install instance-repo` · installs (wheel) · licence: not stated · rank 12452 · last release 2026-11-06 · [PyPI](https://pypi.org/project/instance-repo/)

<details><summary>README extract</summary>

Python、Go、Java SDK 源码版本均为 `1.4.6`。Split create 可将初始 `run_type` 交给支持该能力的服务端原子写入，重复创建保留已有标签。具体兼容条件见下文。实际安装版本以获准制品库的发布记录为准。三语言功能矩阵。

Python3.10+。从批准的索引中选择已发布版本，真实OSS使用`oss` extra；镜像操作需要`skopeo`，不用镜像时显式`push_image=False`。源码隔离环境已有依赖时可使用： ...

Example:
```python
from instance_repo import Repo
from instance_repo.models import OwnerReference

def publish_input(repo: Repo, dataset: str, local_dir: str, owner: OwnerReference):
    repo.splits.create(dataset, 'test')
    result = repo.instances.push(local_dir, dataset, '', split='test',
        owner_reference=owner, push_image=False, register=False)
...
```

Sections: InstanceRepository Python SDK, 安装与配置, Dataset 实例操作, Split 创建与服务端兼容, canonical user-data 与 shared, 验证

</details>

### istari-digital-core

Python bindings for the Istari Digital platform

`pip install istari-digital-core` · installs (wheel) · licence: MIT License · rank 12503 · last release 2026-10-06 · [PyPI](https://pypi.org/project/istari-digital-core/) · [docs](https://docs.istaridigital.com)

<details><summary>README extract</summary>

The `istari-digital-core` library contains compiled Rust binaries for interacting with the Istari Digital platform. It is intended to serve as a dependency of the `istari-digital-client` Python library. Users should not have to interact with it directly.

- Install: Most users should instead install `istari-digital-client`. ...

</details>

### inference-schema

This package is intended to provide a uniform schema for common machine learning applications, as well as a set of decorators that can be used to aid in web based ML prediction applications.

`pip install inference-schema` · installs (wheel) · licence: not stated · rank 12589 · last release 2024-05-17 · [PyPI](https://pypi.org/project/inference-schema/)

### ipydatawidgets

A set of widgets to help facilitate reuse of large datasets across widgets

`pip install ipydatawidgets` · installs (wheel) · licence: BSD License · rank 12694 · last release 2023-06-14 · [PyPI](https://pypi.org/project/ipydatawidgets/)

### ipyflow-core

Backend package for ipyflow's dataflow functionality

`pip install ipyflow-core` · installs (wheel) · licence: BSD License · rank 12727 · last release 2026-08-14 · [PyPI](https://pypi.org/project/ipyflow-core/)

<details><summary>README extract</summary>

TL;DR

Precise reactive Python notebooks for Jupyter[Lab]:

1. `pip install ipyflow`
2. Pick `Python 3 (ipyflow)` from the launcher or kernel selector.
3. For each cell execution, the (minimal) set of out-of-sync upstream and
 downstream cells also re-execute, so that executed cells appear as they
 would when running the notebook from ...

Example:
```python
from ipyflow import reproduce_cell
reproduce_cell(4, lookback=1)  # to reproduce the previous execution of cell 4
```

Sections: IPyflow, Reactive execution model, Autosave and recovering prior executions, Opting into reactivity, In-order and any-order semantics, Memoization, IPyWidgets integration, State API

</details>

### instructure-dap-client

Data Access Platform client library

`pip install instructure-dap-client` · installs (wheel) · licence: MIT · rank 13071 · last release 2026-09-28 · [PyPI](https://pypi.org/project/instructure-dap-client/)

<details><summary>README extract</summary>

Data Access Platform (DAP) acts as a single source of data for analytics at Instructure. It provides efficient access to data collected across various educational products in bulk with high fidelity and low latency, adhering to a canonical data model. ...

Sections: Data Access Platform Client Library, Links to documentation

</details>

### istari-digital-client

Python client for the Istari Digital platform

`pip install istari-digital-client` · installs (wheel) · licence: MIT License · rank 13215 · last release 2026-11-06 · [PyPI](https://pypi.org/project/istari-digital-client/) · [docs](https://docs.istaridigital.com)

<details><summary>README extract</summary>

The `istari-digital-client` library is a client SDK for interacting with the Istari Digital platform.

- Install: `pip install istari-digital-client`
- Documentation and Usage: Please see docs.istaridigital.com.
- Supported Versions: This library requires Python 3.11 or newer (Python 4 is not supported). ...

Sections: Istari Digital Client, Direct S3 Upload, Identity-service API version, The deprecated key surface, Choosing identity-service or a personal access token

</details>

### irepo-artifact

Standalone HTTP artifact downloads

`pip install irepo-artifact` · installs (wheel) · licence: not stated · rank 13367 · last release 2026-11-05 · [PyPI](https://pypi.org/project/irepo-artifact/)

<details><summary>README extract</summary>

> 当前范围（2026-11-04）：本文件描述独立 `irepo-artifact` 包，不是主 SDK 的完整功能清单。主 SDK 的源码/发布范围和三语言API对照见 当前指南。以下接口与限制以本目录源码为准，真实服务支持及发布状态需单独核实。

Python 3.10+ 的独立产物下载包。通过 AP 获取链接后 HTTP 下载，不依赖
`instance-repo`、`ap-client`、`oss2` 或 STS。完整 SDK 与其他客户端
可单向依赖此包，独立包不反向依赖上层 SDK。 ...

Example:
```python
from irepo_artifact import ArtifactClient

client = ArtifactClient(
    ap_endpoint="  # 根地址，不带 /api
    api_key=api_key,
    cluster=cluster,
)
archive = client.download("job-a", output_dir="out/job-a")
expanded = client.download("job-b", output_dir="out/job-b", extract=True)
selected = client.download(
    "job-c", output_dir="out/job-c",
...
```

Sections: irepo-artifact, 使用, 文件筛选, 传输与输出, 服务端前提与兼容, 请求配置与 AP export 接入（0.1.0.dev2）, 调试日志（0.1.2 起）, OSS 内网短探测, 解包资源与链接边界

</details>

### imgsize

(no summary)

`pip install imgsize` · installs (wheel) · licence: not stated · rank 13439 · last release 2026-10-28 · [PyPI](https://pypi.org/project/imgsize/)

### is-safe-url

Django's is_safe_url() bundled as a standalone package.

`pip install is-safe-url` · installs (wheel) · licence: BSD License · rank 13451 · last release 2018-10-10 · [PyPI](https://pypi.org/project/is-safe-url/)

<details><summary>README extract</summary>

Redirecting a visitor to another URL is common. It's also common that the
redirect target is controllable by a visitor. One can often find a `?next` or
`?on_complete` GET parameter with the redirect target. ...

Example:
```python
>>> from is_safe_url import is_safe_url
>>> is_safe_url("/redirect/target", {"example.com", "www.example.com"})
True
>>> is_safe_url("//example.com/redirect/target", {"example.com", "www.example.com"})
True
>>> is_safe_url("//evil.net/redirect/target", {"example.com"})
False
>>> is_safe_url(" {"example.com"})
True
...
```

</details>

### infinity-client

A client library for accessing ♾️ Infinity - Embedding Inference Server

`pip install infinity-client` · installs (wheel) · licence: not stated · rank 13614 · last release 2026-10-19 · [PyPI](https://pypi.org/project/infinity-client/)

<details><summary>README extract</summary>

A client library for accessing ♾️ Infinity - Embedding Inference Server

Example:
```python
from infinity_client import Client
i_client = Client(base_url="
```

Sections: infinity_client, Usage, Advanced customizations, Building / publishing this package

</details>

### ipysigma

A Jupyter widget using sigma.js to render interactive networks.

`pip install ipysigma` · installs (wheel) · licence: BSD License · rank 13791 · last release 2025-11-25 · [PyPI](https://pypi.org/project/ipysigma/)

<details><summary>README extract</summary>

A Jupyter widget using sigma.js and graphology to render interactive networks directly within the result of a notebook cell.

Live Demo

`ipysigma` has been designed to work with either `networkx` or `igraph`. ...

Features:
Labels are costly to render and can negate the benefit of using a WebGL renderer such as sigma.js to render interactive graphs. ...

Example:
```python
import networkx as nx
from ipysigma import Sigma

# Importing a gexf graph
g = nx.read_gexf('./my-graph.gexf')

# Displaying the graph with a size mapped on degree and
# a color mapped on a categorical attribute of the nodes
Sigma(g, node_size=g.degree, node_color='category')
```

...

</details>

### inspect-eval-utils

Shared utilities for METR Inspect AI eval repos: task scaffolder + common runtime helpers.

`pip install inspect-eval-utils` · installs (wheel) · licence: MIT · rank 13884 · last release 2026-08-27 · [PyPI](https://pypi.org/project/inspect-eval-utils/) · [source](https://github.com/METR/inspect-eval-utils)

<details><summary>README extract</summary>

Shared utilities for METR Inspect AI eval repos -- used by both task authors
and agent scaffolding:

- `inspect_eval_utils.setting`: the `Setting` protocol that lets tasks declare
 what they need from agent scaffolding (workspaces, tools, callbacks,
 environment features). Imported by *both* tasks and the scaffolding that
 consumes them. ...

Features:
`Features` are boolean flags about the *environment* -- `vision`, `internet`.
They tell scaffolding "this task involves images" or "this environment has
network access." The scaffolding responds by providing generic tools
(`view_image`, web search) ...

Example:
```python
Setting(workspaces=(Workspace(name="dev"),))
```

...

</details>

### iam-rolesanywhere-session

Boto3 session creator for IAM Roles Anywhere

`pip install iam-rolesanywhere-session` · installs (wheel) · licence: Apache-2.0 · rank 14105 · last release 2026-09-23 · [PyPI](https://pypi.org/project/iam-rolesanywhere-session/) · [docs](https://awslabs.github.io/iam-rolesanywhere-session/) · [source](https://github.com/awslabs/iam-roles-anywhere-session.git)

<details><summary>README extract</summary>

This package provides an easy way to create a refreshable boto3 Session with IAM Roles Anywhere, without defining an AWS profile with relevant configuration for IAM roles anywhere.

This package implements the algorithm described here: <

- Python 3.9 or later
- Creation and configuration of a trust anchor. See documentation ...

Example:
```python
from iam_rolesanywhere_session import IAMRolesAnywhereSession
roles_anywhere_session = IAMRolesAnywhereSession(
    profile_arn="arn:aws:rolesanywhere:eu-central-1:111122223333:profile/a6294488-77cf-4d4a-8c5c-40b96690bbf0",
    role_arn="arn:aws:iam::111122223333:role/IAMRolesAnywhere-01",
...
```

Sections: IAM Roles Anywhere Session, Requirements, Configuration, Documentation

</details>

### infi.pyutils

Misc. pure-python utilities

`pip install infi.pyutils` · installs from source (sdist only) · licence: BSD · rank 14255 · last release 2016-09-14 · [PyPI](https://pypi.org/project/infi.pyutils/)

<details><summary>README extract</summary>

Features:
*infi.pyutils* is a set of utilities for various tasks in Python.

Example:
```python
>>> from future import print_function
>>> from infi.pyutils import iterate
>>> for iteration, element in iterate(range(3)):
...     print(element)
...     print(iteration.first)
...     print(iteration.counter0)
...     print(iteration.counter1)
...     print(iteration.last)
0
True
0
1
False
1
False
1
2
False
2
False
2
3
True
```

Sections: Overview, iterate, renumerate, Reflection, Method Map, Functors, Misc. Functors, PASS, Predicates, Lazy, cached_property and cached_method, Decorator Utilities, Context Utilities, Import Utilities

</details>

### imagequant

Image Quantization Library

`pip install imagequant` · installs (wheel) · licence: BSD-3-Clause · rank 14424 · last release 2025-10-28 · [PyPI](https://pypi.org/project/imagequant/) · [docs](https://github.com/wanadev/imagequant-python#usage) · [source](https://github.com/wanadev/imagequant-python)

<details><summary>README extract</summary>

Imagequant Python are bindings to allow using libimagequant from Python.

Libimagequant is a small, portable C library for high-quality conversion of RGBA images to 8-bit indexed-color (palette) images.

Example:
```python
from PIL import Image
import imagequant

input_image = Image.open("./example.png")
output_image = imagequant.quantize_pil_image(
    input_image,
    dithering_level=1.0,  # from 0.0 to 1.0
    max_colors=256,       # from 1 to 256
    min_quality=0,        # from 0 to 100
    max_quality=100,      # from 0 to 100
)
...
```

Sections: Imagequant Python - Python Bindings for libimagequant, Usage, With PIL / Pillow, With Raw Data

</details>

### ibm-watsonx-orchestrate

IBM watsonx.orchestrate ADK

`pip install ibm-watsonx-orchestrate` · installs (wheel) · licence: MIT License · rank 14476 · last release 2026-10-22 · [PyPI](https://pypi.org/project/ibm-watsonx-orchestrate/)

### infrablocks.invoke_terraform

Provides invoke tasks to interact with terraform

`pip install infrablocks.invoke_terraform` · installs (wheel) · licence: MIT License · rank 14488 · last release 2026-06-04 · [PyPI](https://pypi.org/project/infrablocks.invoke_terraform/)

<details><summary>README extract</summary>

Provides invoke tasks to interact with terraform

</details>

### iterm2

Python interface to iTerm2's scripting API

`pip install iterm2` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 14509 · last release 2026-10-12 · [PyPI](https://pypi.org/project/iterm2/)

_README extract left out: share-alike licence._

### infrablocks.invoke_factory

Base classes and modules to aid in creating custom invoke tasks.

`pip install infrablocks.invoke_factory` · installs (wheel) · licence: MIT License · rank 14520 · last release 2026-06-04 · [PyPI](https://pypi.org/project/infrablocks.invoke_factory/)

<details><summary>README extract</summary>

Base classes and modules to aid in creating custom invoke tasks.

</details>

### infrablocks.terraform_pkl_type_gen

Provides invoke tasks to interact with terraform

`pip install infrablocks.terraform_pkl_type_gen` · installs (wheel) · licence: MIT License · rank 14559 · last release 2026-06-29 · [PyPI](https://pypi.org/project/infrablocks.terraform_pkl_type_gen/)

<details><summary>README extract</summary>

A library for creating Pkl types from Terraform variables definitions.

</details>

### ioregistry

IORegistry exploration library

`pip install ioregistry` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 14647 · last release 2026-09-23 · [PyPI](https://pypi.org/project/ioregistry/)

_README extract left out: share-alike licence._

### infobip-api-python-client

This is a Python package for Infobip API and you can use it as a dependency to add Infobip APIs to your application.

`pip install infobip-api-python-client` · installs (wheel) · licence: not stated · rank 14739 · last release 2026-01-22 · [PyPI](https://pypi.org/project/infobip-api-python-client/)

<details><summary>README extract</summary>

OpenAPI specification containing public endpoints supported in client API libraries.

</details>

### ida-hcli

HCLI - Hex-Rays CLI Utility

`pip install ida-hcli` · installs (wheel) · licence: MIT · rank 14781 · last release 2026-10-29 · [PyPI](https://pypi.org/project/ida-hcli/) · [source](https://github.com/HexRaysSA/ida-hcli)

<details><summary>README extract</summary>

A modern command-line interface for managing IDA Pro licenses, downloads, ...

Sections: IDA HCLI, Quickstart, Documentation, Prerequisites, Setup, Build System

</details>

### infrared-protocols

Library to decode and encode infrared signals.

`pip install infrared-protocols` · installs (wheel) · licence: MIT · rank 14806 · last release 2026-11-02 · [PyPI](https://pypi.org/project/infrared-protocols/)

### icd-mappings

This python tool enables a variety of mappings between ICD diagnostic codes (International Classification of Diseases) with a single line of code.

`pip install icd-mappings` · installs (wheel) · licence: MIT License · rank 14834 · last release 2026-04-27 · [PyPI](https://pypi.org/project/icd-mappings/) · [source](https://github.com/snovaisg/ICDMappings)

<details><summary>README extract</summary>

This python tool enables a variety of mappings of ICD codes (International Classification of Diseases) to different medical concepts with a single line of code.

Latest data refresh: ICD-10 chapter and block mappings were fetched from the latest available code ranges on `2026-04-27`.

Features:
Feel free to request a new functionality or report a bug by creating a new issue.

Example:
```python
from icdmappings import Mapper

mapper = Mapper()

icd9code = '29410'
mapper.map(icd9code, source='icd9', target='ccs')
>>> '653'

# you can pass any Iterable of codes (list, numpy array, pandas Series, you name it)
icd9codes = ['29410', '5362', 'NOT_A_CODE', '3669']
mapper.map(icd9codes, source='icd9', target='ccs')
>>> ['653', '141', None, '86']
...
```

...

</details>

### ifctester

IFC model auditing tool with support for IDS

`pip install ifctester` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 14926 · last release 2026-09-29 · [PyPI](https://pypi.org/project/ifctester/) · [docs](https://docs.ifcopenshell.org)

_README extract left out: share-alike licence._

