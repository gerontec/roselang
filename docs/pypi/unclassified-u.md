# Unclassified / U

[Index](README.md) · 82 packages in this topic, by downloads.

### uritemplate

Implementation of RFC 6570 URI Templates

`pip install uritemplate` · installs (wheel) · licence: BSD 3-Clause OR Apache-2.0 · rank 231 · last release 2025-06-02 · [PyPI](https://pypi.org/project/uritemplate/) · [source](https://github.com/python-hyper/uritemplate)

<details><summary>README extract</summary>

Documentation -- GitHub -- Travis-CI

Simple python library to deal with URI Templates. The API looks like

Where it might be useful to have a class

When the module containing this class is loaded, `GitHubUser.url` is
evaluated and so the template is created once. ...

Example:
```python
from uritemplate import URITemplate, expand

# NOTE: URI params must be strings not integers

gist_uri = '
t = URITemplate(gist_uri)
print(t.expand(gist_id='123456'))
# =>

# or
print(expand(gist_uri, gist_id='123456'))

# also
t.expand({'gist_id': '123456'})
print(expand(gist_uri, {'gist_id': '123456'}))
```

</details>

### uuid-utils

Fast, drop-in replacement for Python's uuid module, powered by Rust.

`pip install uuid-utils` · installs (wheel) · licence: BSD-3-Clause · rank 326 · last release 2026-10-26 · [PyPI](https://pypi.org/project/uuid-utils/) · [docs](https://github.com/aminalaee/uuid-utils) · [source](https://github.com/aminalaee/uuid-utils)

<details><summary>README extract</summary>

Fast, drop-in replacement for Python's uuid module, powered by Rust.

Available UUID versions:

- `uuid1` - Version 1 UUIDs using a timestamp and monotonic counter.
- `uuid3` - Version 3 UUIDs based on the MD5 hash of some data.
- `uuid4` - Version 4 UUIDs with random data.
- `uuid5` - Version 5 UUIDs based on the SHA1 hash of some data. ...

Example:
```python
>>> import uuid_utils.compat as uuid

>>> uuid.uuid4()
UUID('ffe95fcc-b818-4aca-a350-e0a35b9de6ec')
```

Sections: Python UUID Utils, Example, Compatibility with Python UUID, Benchmarks

</details>

### uncalled-for

Async dependency injection for Python functions

`pip install uncalled-for` · installs (wheel) · licence: MIT · rank 394 · last release 2026-11-05 · [PyPI](https://pypi.org/project/uncalled-for/) · [source](https://github.com/chrisguidry/uncalled-for)

<details><summary>README extract</summary>

Async dependency injection for Python functions.

Declare what your function needs as parameter defaults. They show up resolved
when the function runs. No ceremony, no container, no configuration.

Features:
- Zero dependencies — standard library only
- Async-native — built on `AsyncExitStack` and `ContextVar`
- Context manager lifecycle — sync and async generators get proper cleanup ...

Example:
```python
from uncalled_for import Depends

async def get_db():
    db = await connect()
    try:
        yield db
    finally:
        await db.close()

async def handle_request(db: Connection = Depends(get_db)):
    await db.execute("SELECT 1")
```

Sections: uncalled-for, Features, Annotated dependencies, Call arguments, Bindings

</details>

### ujson

Ultra fast JSON encoder and decoder for Python

`pip install ujson` · installs (wheel) · licence: BSD-3-Clause AND TCL · rank 656 · last release 2026-11-03 · [PyPI](https://pypi.org/project/ujson/) · [source](https://github.com/ultrajson/ultrajson)

<details><summary>README extract</summary>

UltraJSON is an ultra fast JSON encoder and decoder written in pure C with bindings for
Python.

Install with pip:

Example:
```python
>>> import ujson
>>> ujson.dumps([{"key": "value"}, 81, True])
'[{"key":"value"},81,true]'
>>> ujson.loads("""[{"key": "value"}, 81, true]""")
[{'key': 'value'}, 81, True]
```

Sections: UltraJSON, Usage, Encoder options, encode_html_chars, ensure_ascii, escape_forward_slashes, indent, Benchmarks, Test machine, Versions, Build options, Debugging symbols, UJSON_BUILD_NO_STRIP, UJSON_BUILD_DC_INCLUDES

</details>

### universal-pathlib

pathlib api extended to use fsspec backends

`pip install universal-pathlib` · installs (wheel) · licence: MIT · rank 789 · last release 2026-02-22 · [PyPI](https://pypi.org/project/universal-pathlib/)

<details><summary>README extract</summary>

Universal Pathlib is a Python library that extends the
`pathlib_abc.JoinablePath` API to provide a
`pathlib.Path`-like interface for a variety of backend filesystems
via `filesystem_spec`.

Example:
```python
# pip install universal_pathlib fsspec[s3]
>>> from upath import UPath
>>>
>>> s3path = UPath("s3://test_bucket") / "example.txt"
>>> s3path.name
example.txt
>>> s3path.stem
example
>>> s3path.suffix
.txt
>>> s3path.exists()
True
>>> s3path.read_text()
'Hello World'
```

...

</details>

### uuid6

New time-based UUID formats which are suited for use as a database key

`pip install uuid6` · installs (wheel) · licence: MIT License · rank 1175 · last release 2025-07-04 · [PyPI](https://pypi.org/project/uuid6/)

<details><summary>README extract</summary>

New time-based UUID formats which are suited for use as a database key.

This module extends immutable UUID objects (the UUID class) with the functions `uuid6()`, `uuid7()`, and `uuid8()` from the proposed IETF RFC 9562.

Example:
```python
import uuid6

my_uuid = uuid6.uuid6()
print(my_uuid)
assert my_uuid < uuid6.uuid6()

my_uuid = uuid6.uuid7()
print(my_uuid)
assert my_uuid < uuid6.uuid7()

my_uuid = uuid6.uuid8()
print(my_uuid)
assert my_uuid < uuid6.uuid8()

import uuid

my_uuid = uuid.UUID(hex="C232AB00-9414-11EC-B3C8-9E6BDECED846")
...
```

...

</details>

### uuid7

UUID version 7, generating time-sorted UUIDs with 200ns time resolution and 48 bits of randomness

`pip install uuid7` · installs (wheel) · licence: MIT License · rank 1225 · last release 2021-12-29 · [PyPI](https://pypi.org/project/uuid7/)

<details><summary>README extract</summary>

This module implements the version 7 UUIDs, proposed by Peabody and Davis in

as an extension to RFC4122.

Version 7 has the nice characteristic that the start of a UUID encodes
the time with a chronological sort order and potentially ~50ns time
resolution, while the end of the UUID includes sufficient random bits to
ensure consecutive UUIDs will ...

Example:
```python
>>> from uuid_extensions import uuid7, uuid7str
>>> uuid7()
UUID('061cb26a-54b8-7a52-8000-2124e7041024')

>>> uuid7(0)
UUID('00000000-0000-0000-0000-00000000000')

>>> for fmt in ('bytes', 'hex', 'int', 'str', 'uuid', None):
...     print(fmt, repr(uuid7(as_type=fmt)))
bytes b'\x06\x1c\xb8\xfe\x0f\x0b|9\x80\x00\tjt\x85\xb3\xbb'
...
```

Sections: uuid7 - time-sortable UUIDs, Implementation notes, Usage, 0.1.0 (2021-12-28)

</details>

### uvicorn-worker

Uvicorn worker for Gunicorn! ✨

`pip install uvicorn-worker` · installs (wheel) · licence: BSD-3-Clause · rank 1266 · last release 2025-09-20 · [PyPI](https://pypi.org/project/uvicorn-worker/) · [source](https://github.com/Kludex/uvicorn-worker)

<details><summary>README extract</summary>

The Uvicorn Worker is a package designed for the mature and comprehensive server and process manager, Gunicorn.
This package allows you to run ASGI applications, leverages Uvicorn's high-performance capabilities, and provides Gunicorn's
robust process management. ...

Sections: Uvicorn Worker, Getting Started, Deployment

</details>

### userpath

Cross-platform tool for adding locations to the user PATH

`pip install userpath` · installs (wheel) · licence: MIT License · rank 1371 · last release 2024-02-29 · [PyPI](https://pypi.org/project/userpath/) · [source](https://github.com/ofek/userpath)

<details><summary>README extract</summary>

| | |

| CI/CD | |
| Package | |
| Meta | |

This is a tool for modifying a user's `PATH`.

Table of Contents

- Installation
- CLI
- API
- License

Example:
```python
>>> import userpath
>>> location = r'C:\Users\Ofek\Desktop\test'
>>>
>>> userpath.in_current_path(location)
False
>>> userpath.in_new_path(location)
False
>>> userpath.append(location)
True
>>> userpath.in_new_path(location)
True
>>> userpath.need_shell_restart(location)
True
```

Sections: userpath, CLI, API

</details>

### url-normalize

URL normalization for Python

`pip install url-normalize` · installs (wheel) · licence: MIT · rank 1482 · last release 2026-10-29 · [PyPI](https://pypi.org/project/url-normalize/) · [source](https://github.com/niksite/url-normalize)

<details><summary>README extract</summary>

Normalize URL spelling consistently for storage, comparison, and display. Use `url_normalize()` for normalized URLs and `url_humanize()` for readable display URLs.

Requires Python 3.11 or newer. Normalization operates on URL text; it does not fetch pages or follow redirects.

Example:
```python
from url_normalize import url_normalize

print(url_normalize("HTTP://Example.COM:80/a/../b"))
# Output:

print(url_normalize("bücher.de/résumé"))
# Output:
```

Sections: url-normalize, Quick start, Normalization behavior, Python API, Query parameter filtering, Default domain and scheme, Human-readable URLs, Command-line usage

</details>

### uv-dynamic-versioning

Dynamic versioning based on VCS tags for uv/hatch project

`pip install uv-dynamic-versioning` · installs (wheel) · licence: not stated · rank 1632 · last release 2026-08-18 · [PyPI](https://pypi.org/project/uv-dynamic-versioning/) · [source](https://github.com/ninoseki/uv-dynamic-versioning/)

<details><summary>README extract</summary>

poetry-dynamic-versioning influenced dynamic versioning tool for uv/hatch, powered by dunamai.

> [!NOTE]
> This plugin doesn't work with the uv build backend right now. (ref. astral-sh/uv#14561)

Sections: uv-dynamic-versioning, Plugins, Tips, Examples, Projects Using `uv-dynamic-versioning`, Alternatives

</details>

### unicodecsv

Python2's stdlib csv module is nice, but it doesn't support unicode. This module is a drop-in replacement which *does*.

`pip install unicodecsv` · installs from source (sdist only) · licence: BSD License · rank 1663 · last release 2015-09-22 · [PyPI](https://pypi.org/project/unicodecsv/)

<details><summary>README extract</summary>

The unicodecsv is a drop-in replacement for Python 2.7's csv module which supports unicode strings without a hassle. Supported versions are python 2.7, 3.3, 3.4, 3.5, and pypy 2.4.0.

Python 2's csv module doesn't easily deal with unicode strings, leading to the dreaded "'ascii' codec can't encode characters in position ..." exception. ...

Example:
```python
>>> import unicodecsv as csv
>>> from io import BytesIO
>>> f = BytesIO()
>>> w = csv.writer(f, encoding='utf-8')
>>> _ = w.writerow((u'é', u'ñ'))
>>> _ = f.seek(0)
>>> r = csv.reader(f, encoding='utf-8')
>>> next(r) == [u'é', u'ñ']
True
```

Sections: unicodecsv, More fully

</details>

### uamqp

AMQP 1.0 Client Library for Python

`pip install uamqp` · installs from source (sdist only) · licence: MIT License · rank 1954 · last release 2024-10-28 · [PyPI](https://pypi.org/project/uamqp/)

<details><summary>README extract</summary>

An AMQP 1.0 client library for Python.

This repo is no longer in active maintenance and we plan on deprecating
it sometime in the first quarter of 2025. The EventHubs & Service Bus
client libraries are now using the python based AMQP library which is
under active development. ...

Sections: uAMQP for Python, Disclaimer, Documentation, Pre-requisites, Building the extension, Tests, Provide Feedback, 1.6.11 (2024-10-28), 1.6.10 (2024-09-11), 1.6.9 (2024-03-20), 1.6.8 (2024-01-29), 1.6.7 (2024-01-17), 1.6.6 (2023-11-16), 1.6.5 (2023-07-12)

</details>

### ua-parser-rs

native accelerator for ua-parser

`pip install ua-parser-rs` · installs (wheel) · licence: Apache Software License · rank 2083 · last release 2026-04-05 · [PyPI](https://pypi.org/project/ua-parser-rs/) · [source](https://github.com/ua-parser/uap-rust/)

<details><summary>README extract</summary>

This package is (currently) not intended to be used directly, instead
it is one of the native accelerators for ua-parser.

The API is very simplistic and should be pretty stable (if only
because having to update ua-parser all the time is undesirable),
but there is no formal guarantee that it'll keep, as the goal is
really nothing more than a very ...

</details>

### unstructured-client

Python Client SDK for Unstructured API

`pip install unstructured-client` · installs (wheel) · licence: MIT · rank 2151 · last release 2026-11-05 · [PyPI](https://pypi.org/project/unstructured-client/) · [source](https://github.com/Unstructured-IO/unstructured-python-client.git)

<details><summary>README extract</summary>

This is a HTTP client for the Unstructured Platform API. You can sign up here and process 1000 free pages per day for 14 days.

Please refer to the our documentation for a full guide on integrating the Workflow Endpoint and Partition Endpoint into your Python code.

Example:
```python
# !/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
# "unstructured-client",
# ]
# ///

from unstructured_client import UnstructuredClient

sdk = UnstructuredClient(
  # SDK arguments
)

# Rest of script here...
```

Sections: Python SDK for the Unstructured API, Summary, uv, PIP, Poetry, Shell and script usage with `uv`, Retries, Error Handling, Example, Error Classes, Custom HTTP Client, PyCharm, SDK Example Usage

</details>

### usaddress-scourgify

Clean US addresses following USPS pub 28 and RESO guidelines

`pip install usaddress-scourgify` · installs (wheel) · licence: not stated · rank 2292 · last release 2026-08-07 · [PyPI](https://pypi.org/project/usaddress-scourgify/)

### us

US state metadata

`pip install us` · installs (wheel) · licence: not stated · rank 2422 · last release 2026-09-29 · [PyPI](https://pypi.org/project/us/)

<details><summary>README extract</summary>

A package for easily working with US and state metadata.

* all US states and territories
* postal abbreviations
* Associated Press style abbreviations
* FIPS codes
* capitals
* years of statehood
* time zones
* phonetic state name lookup
* is contiguous or continental
* URLs to shapefiles for state, census, congressional districts,
 counties, and ...

Features:
Easy access to state information:

Includes territories too:

List of all (actual) states:

And the whole shebang, if you want it: ...

Example:
```python
>>> import us
>>> us.states.MD
<State:Maryland>
>>> us.states.MD.fips
'24'
>>> us.states.MD.name
'Maryland'
>>> us.states.MD.is_contiguous
True
```

...

</details>

### uuid

UUID object and generation functions (Python 2.3 or higher)

`pip install uuid` · installs from source (sdist only) · licence: UNKNOWN · rank 2495 · last release 2007-05-26 · [PyPI](https://pypi.org/project/uuid/)

<details><summary>README extract</summary>

UUID object and generation functions (Python 2.3 or higher)

</details>

### uharfbuzz

Streamlined Cython bindings for the harfbuzz shaping engine

`pip install uharfbuzz` · installs (wheel) · licence: Apache License 2.0 · rank 2611 · last release 2026-10-23 · [PyPI](https://pypi.org/project/uharfbuzz/)

<details><summary>README extract</summary>

Streamlined Cython bindings for the HarfBuzz shaping engine.

Example:
```python
import sys

import uharfbuzz as hb

fontfile = sys.argv[1]
text = sys.argv[2]

blob = hb.Blob.from_file_path(fontfile)
face = hb.Face(blob)
font = hb.Font(face)

buf = hb.Buffer()
buf.add_str(text)
buf.guess_segment_properties()

features = {"kern": True, "liga": True}
hb.shape(font, buf, features)

infos = buf.glyph_infos
...
```

Sections: uharfbuzz, Example

</details>

### undetected-chromedriver

('Selenium.webdriver.Chrome replacement with compatiblity for Brave, and other Chromium based browsers.', 'Not triggered by CloudFlare/Imperva/hCaptcha and such.', 'NOTE: results may vary due to many factors. No guarantees are given, except for ongoing efforts in understanding detection algorithms.')

`pip install undetected-chromedriver` · installs from source (sdist only) · licence: GNU General Public License v3 (GPLv3) · rank 2719 · last release 2024-02-17 · [PyPI](https://pypi.org/project/undetected-chromedriver/)

_README extract left out: share-alike licence._

### utilsforecast

Forecasting utilities

`pip install utilsforecast` · installs (wheel) · licence: Apache Software License · rank 2978 · last release 2026-10-05 · [PyPI](https://pypi.org/project/utilsforecast/) · [docs](https://nixtlaverse.verse.io/utilsforecast) · [source](https://github.com/Nixtla/utilsforecast)

<details><summary>README extract</summary>

Example:
```python
from utilsforecast.data import generate_series

series = generate_series(3, with_trend=True, static_as_categorical=False)
series
```

Sections: PyPI, Conda, How to use, Generate synthetic data, Plotting, Preprocessing, Evaluating

</details>

### UnleashClient

Python client for the Unleash feature toggle system!

`pip install UnleashClient` · installs (wheel) · licence: MIT License · rank 3011 · last release 2026-10-15 · [PyPI](https://pypi.org/project/UnleashClient/) · [docs](https://docs.getunleash.io/reference/sdks/python) · [source](https://github.com/Unleash/unleash-python-sdk)

<details><summary>README extract</summary>

Unleash is a private, secure, and scalable feature management platform built to reduce the risk of releasing new features and accelerate software development. This server-side Python SDK is designed to help you integrate with Unleash and evaluate feature flags inside your application. ...

Example:
```python
from UnleashClient import UnleashClient

client = UnleashClient(
    url="https:<YOUR-API-URL>",
    app_name="my-python-app",
    custom_headers={'Authorization': '<API token>'})

client.initialize_client()
```

Sections: Unleash SDK for Python, Getting Started, Initialization, Check features, Shutdown, Usage, Context, Fallback function, Configuration options, Bootstrap, Bootstrap from dict, Bootstrap from file, Bootstrap from URL, Custom strategies

</details>

### uWSGI

The uWSGI server

`pip install uWSGI` · installs from source (sdist only) · licence: GPL2 · rank 3030 · last release 2025-10-11 · [PyPI](https://pypi.org/project/uWSGI/)

_README extract left out: share-alike licence._

### unearth

A utility to fetch and download python packages

`pip install unearth` · installs (wheel) · licence: MIT · rank 3216 · last release 2026-10-27 · [PyPI](https://pypi.org/project/unearth/) · [docs](https://unearth.readthedocs.io)

<details><summary>README extract</summary>

<!--index start-->

A utility to fetch and download python packages

Features:
This project exists as the last piece to complete the puzzle of a package manager. The other pieces are:

- resolvelib - Resolves concrete dependencies from a set of (abstract) requirements. ...

Example:
```python
>>> from unearth import PackageFinder
>>> finder = PackageFinder(index_urls=["
>>> result = finder.find_best_match("flask>=2")
>>> result.best
Package(name='flask', version='2.1.2')
```

Sections: unearth, Why this project?, Why not pip?, Requirements, Quickstart, Documentation

</details>

### unicorn

Unicorn CPU emulator engine

`pip install unicorn` · installs (wheel) · licence: BSD License · rank 3284 · last release 2025-09-09 · [PyPI](https://pypi.org/project/unicorn/) · [source](https://github.com/unicorn-engine/unicorn)

<details><summary>README extract</summary>

Unicorn is a lightweight, multi-platform, multi-architecture CPU emulator framework
based on QEMU.

Unicorn offers some unparalleled features:

- Multi-architecture: ARM, ARM64 (ARMv8), M68K, MIPS, PowerPC, RISCV, SPARC, S390X, TriCore and X86 (16, 32, 64-bit)
- Clean/simple/lightweight/intuitive architecture-neutral API ...

Sections: Unicorn, Python Bindings for Unicorn, Python2 compatibility

</details>

### unicodedata2

Unicodedata backport updated to the latest Unicode version.

`pip install unicodedata2` · installs (wheel) · licence: Apache-2.0 · rank 4086 · last release 2026-09-18 · [PyPI](https://pypi.org/project/unicodedata2/)

<details><summary>README extract</summary>

[unicodedata] backport/updates. Currently supports Unicode 18.0.0.

Requires Python 3.9 or newer.

The versions of this package match Unicode versions, so unicodedata2==13.0.0 is data from Unicode 13.0.0.

Pre-compiled wheel packages are available on [PyPI] and can be installed via pip.

Sections: unicodedata2, 18.0.0, 17.0.0, 16.0.0, 15.0.0, 14.0.0, 13.0.0-2, 13.0.0, 12.1.0, 12.0.0, 11.0.0, 10.0.0-2, 10.0.0, 9.0.0-4

</details>

### unpaddedbase64

Encode and decode Base64 without "=" padding

`pip install unpaddedbase64` · installs (wheel) · licence: Apache Software License · rank 4206 · last release 2021-03-09 · [PyPI](https://pypi.org/project/unpaddedbase64/)

<details><summary>README extract</summary>

Encode and decode Base64 without "=" padding.

RFC 4648 specifies that Base64 should be padded to a multiple of 4 bytes
using "=" characters. However many protocols choose to omit the "=" padding.

Example:
```python
import unpaddedbase64
assert (unpaddedbase64.encode_base64(b'\x00')) == 'AA'
assert (unpaddedbase64.decode_base64('AA')) == b'\x00'
```

Sections: Unpadded Base64, Using

</details>

### unclecode-litellm

Pre-compromise fork of litellm - Library to easily interface with LLM API providers

`pip install unclecode-litellm` · installs (wheel) · licence: MIT · rank 4361 · last release 2026-03-24 · [PyPI](https://pypi.org/project/unclecode-litellm/) · [source](https://github.com/unclecode/litellm)

<details><summary>README extract</summary>

Call 100+ LLMs in OpenAI format. [Bedrock, Azure, OpenAI, VertexAI, Anthropic, Groq, etc.]

LLMs - Call 100+ LLMs (Python SDK + AI Gateway)

All Supported Endpoints - `/chat/completions`, `/responses`, `/embeddings`, `/images`, `/audio`, `/batches`, `/rerank`, `/a2a`, `/messages` and more.

Features:
- Need for simplicity: Our code started to get extremely complicated managing & translating calls between Azure, OpenAI and Cohere.

Example:
```python
from litellm import completion
import os

os.environ["OPENAI_API_KEY"] = "your-openai-key"
os.environ["ANTHROPIC_API_KEY"] = "your-anthropic-key"

# OpenAI
response = completion(model="openai/gpt-4o", messages=[{"role": "user", "content": "Hello!"}])

# Anthropic
...
```

...

</details>

### ummalqura

Python Hijri Ummalqura

`pip install ummalqura` · installs from source (sdist only) · licence: Waqef · rank 4430 · last release 2017-12-26 · [PyPI](https://pypi.org/project/ummalqura/)

<details><summary>README extract</summary>

Python Umalqurra Calender is an API that will give you the ability to convert Gregorian to Hijri and hijri to Gregorian
it will give you the day name in arabic and english , and the month name in Hijri arabic and Gregorian.

Thanks for Khalid Al-hussayen :

- `Install <#install>`__
- `Features <#features>`__
- `Usage <#usage>`__

Install: ...

</details>

### unidic-lite

A small version of UniDic packaged for Python

`pip install unidic-lite` · installs from source (sdist only) · licence: MIT License · rank 4540 · last release 2021-01-25 · [PyPI](https://pypi.org/project/unidic-lite/)

<details><summary>README extract</summary>

This is a version of unidic-py that is
designed to be installable with pip alone, not requiring any extra downloads.

At the moment it uses Unidic 2.1.2, from 2013, which is the most recent release
of UniDic that's small enough to be distributed via PyPI.

Note this package takes roughly 250MB on disk after being installed. ...

</details>

### unsloth-zoo

Utils for Unsloth

`pip install unsloth-zoo` · installs (wheel) · licence: LGPL-3.0-or-later · rank 4617 · last release 2026-11-06 · [PyPI](https://pypi.org/project/unsloth-zoo/) · [docs](https://github.com/unslothai/unsloth) · [source](https://github.com/unslothai/unsloth)

_README extract left out: share-alike licence._

### uszipcode

USA zipcode programmable database, includes 2020 census data and geometry information.

`pip install uszipcode` · installs (wheel) · licence: MIT License · rank 4669 · last release 2022-01-06 · [PyPI](https://pypi.org/project/uszipcode/)

<details><summary>README extract</summary>

If you are on www.pypi.org or www.github.com, this is not the complete document. Here is the Complete Document.

If you are looking for technical support, click the badge below to join this gitter chat room and ask question to the author.

`uszipcode` is the most powerful and easy to use programmable zipcode database in Python. ...

Sections: Welcome to `uszipcode` Documentation, About the Data, The Data point

</details>

### uiautomator2

uiautomator for android device

`pip install uiautomator2` · installs (wheel) · licence: MIT License · rank 4827 · last release 2026-10-23 · [PyPI](https://pypi.org/project/uiautomator2/)

<details><summary>README extract</summary>

<!-- filepath: /Users/codeskyblue/Codes/uiautomator2/README.md -->

📖 Read the Chinese version

A simple, easy-to-use, and stable Android automation library.

- QQ Group: 815453846
- Discord: <

> Users still on version 2.x.x, please check 2to3 before deciding to upgrade to 3.x.x (Upgrade is highly recommended). ...

Example:
```python
import uiautomator2 as u2

d = u2.connect() # Specify device serial number if multiple devices are connected
print(d.info)
# Expected output
...
```

Sections: uiautomator2, How it Works, Dependencies, Quick Start, Documentation, Connecting to Device, Operating Elements with XPath, Plugins, Operating Elements with UiAutomator API, Element Wait Timeout, Get Device Information, Clipboard, Key Events, Gesture interaction with the device

</details>

### unstructured.pytesseract

Python-tesseract is a python wrapper for Google's Tesseract-OCR

`pip install unstructured.pytesseract` · installs (wheel) · licence: Apache Software License · rank 4846 · last release 2025-03-05 · [PyPI](https://pypi.org/project/unstructured.pytesseract/)

<details><summary>README extract</summary>

.. image::
 :target:
 :alt: Python versions

.. image::
 :target:
 :alt: Github release

.. image::
 :target:
 :alt: PyPI release

.. image::
 :target:
 :alt: Conda release

.. image::
 :target:
 :alt: Pre-commit CI status

.. image::
 :target:
 :alt: CI workflow status

Python-tesseract is an optical character recognition (OCR) tool for python. ...

</details>

### uncurl

A library to convert curl requests to python-requests.

`pip install uncurl` · installs (wheel) · licence: not stated · rank 5042 · last release 2021-03-21 · [PyPI](https://pypi.org/project/uncurl/)

### untokenize

Transforms tokens into original source code (while preserving whitespace).

`pip install untokenize` · installs from source (sdist only) · licence: MIT License · rank 5592 · last release 2014-02-08 · [PyPI](https://pypi.org/project/untokenize/)

<details><summary>README extract</summary>

*untokenize* transforms tokens into source code. Unlike the standard library's
`tokenize.untokenize()`, it preserves the original whitespace between tokens.

Example:
```python
import untokenize
source_code = untokenize.untokenize(tokens)
```

Sections: untokenize, Usage, Tests

</details>

### unitycatalog-langchain

Support for Unity Catalog functions as LangChain tools

`pip install unitycatalog-langchain` · installs (wheel) · licence: Apache-2.0 · rank 5965 · last release 2026-04-24 · [PyPI](https://pypi.org/project/unitycatalog-langchain/)

<details><summary>README extract</summary>

Integrate the Unity Catalog AI package with `Langchain` to allow seamless usage of UC functions as tools in agentic applications.

Example:
```python
import asyncio
from unitycatalog.ai.core.client import UnitycatalogFunctionClient
from unitycatalog.client import ApiClient, Configuration

# Configure the Unity Catalog API client
config = Configuration(
    host="  # Replace with your UC server URL
)

# Initialize the asynchronous ApiClient
api_client = ApiClient(configuration=config)

...
```

...

</details>

### unitycatalog-openai

Support for Unity Catalog functions as OpenAI tools

`pip install unitycatalog-openai` · installs (wheel) · licence: Apache-2.0 · rank 6110 · last release 2026-10-27 · [PyPI](https://pypi.org/project/unitycatalog-openai/)

<details><summary>README extract</summary>

Integrate Unity Catalog AI package with OpenAI to allow seamless usage of UC functions as tools in agents application.

Example:
```python
import asyncio
from unitycatalog.ai.core.client import UnitycatalogFunctionClient
from unitycatalog.client import ApiClient, Configuration

# Configure the Unity Catalog API client
config = Configuration(
    host="  # Replace with your UC server URL
)

# Initialize the asynchronous ApiClient
api_client = ApiClient(configuration=config)

...
```

...

</details>

### unidic

UniDic packaged for Python

`pip install unidic` · installs from source (sdist only) · licence: MIT License · rank 6247 · last release 2021-10-10 · [PyPI](https://pypi.org/project/unidic/)

<details><summary>README extract</summary>

This is a version of UniDic packaged for use
with pip.

Currently it supports 2.3.0, the latest version of UniDic. **Note this will
take up 1GB on disk after install.** If you want a small package, try
unidic-lite.

The data for this dictionary is hosted as part of the AWS Open Data
Sponsorship Program. You can read the announcement
here. ...

Sections: unidic-py, Fields

</details>

### u-msgpack-python

A portable, lightweight MessagePack serializer and deserializer written in pure Python.

`pip install u-msgpack-python` · installs (wheel) · licence: MIT License · rank 6522 · last release 2023-05-18 · [PyPI](https://pypi.org/project/u-msgpack-python/)

<details><summary>README extract</summary>

u-msgpack-python is a lightweight `MessagePack < serializer and deserializer module written in pure Python, compatible with both Python 2 and Python 3, as well as CPython and PyPy implementations of Python. ...

</details>

### ucumvert

Python parser & interface for UCUM (Unified Code for Units of Measure).

`pip install ucumvert` · installs (wheel) · licence: MIT · rank 6808 · last release 2026-11-06 · [PyPI](https://pypi.org/project/ucumvert/) · [docs](https://github.com/dalito/ucumvert) · [source](https://github.com/dalito/ucumvert)

<details><summary>README extract</summary>

> Feedback welcome!
> Currently only the conversion direction from UCM to pint is supported.
> Please review the definitions before you trust them.
> While we have many tests in place and reviewed the mappings carefully, bugs may still be present.

UCUM (Unified Code for Units of Measure) is a code system intended to cover all units of measures. ...

Example:
```python
>>> from ucumvert import PintUcumRegistry
>>> ureg = PintUcumRegistry()
>>> ureg.from_ucum("m/s2.kg")
<Quantity(1.0, 'kilogram * meter / second ** 2')>
>>> ureg.from_ucum("m[H2O]{35Cel}")  # UCUM code with annotation
<Quantity(1, 'm_H2O')>
>>> _.to("mbar")
<Quantity(98.0665, 'millibar')>
>>> ureg("degC")   # a standard pint unit
...
```

Sections: Easier access to UCUM from Python, Demo, Tests, Useful links

</details>

### uiautomation

Python UIAutomation for Windows

`pip install uiautomation` · installs (wheel) · licence: Apache 2.0 · rank 6846 · last release 2025-08-05 · [PyPI](https://pypi.org/project/uiautomation/)

<details><summary>README extract</summary>

Python UIAutomation for Windows. Supports Python3.4+, x86, x64

</details>

### uipath-ipc

Python client and server for UiPath.Ipc — an interface-based RPC framework over Named Pipes and TCP.

`pip install uipath-ipc` · installs (wheel) · licence: not stated · rank 6851 · last release 2026-09-15 · [PyPI](https://pypi.org/project/uipath-ipc/)

<details><summary>README extract</summary>

Python client and server for UiPath.Ipc — an interface-based RPC framework with .NET server and client, TypeScript client, and now a Python client and server.

This package speaks the same wire protocol as the .NET package, so a Python client can talk to any UiPath.Ipc server (and a Python `IpcServer` can host services for any client).

Example:
```python
from abc import ABC, abstractmethod

class IComputingService(ABC):
    @abstractmethod
    async def AddFloats(self, x: float, y: float) -> float: ...

    @abstractmethod
    async def Wait(self, duration: float) -> bool: ...
```

...

</details>

### udtools

Python tools for Universal Dependencies

`pip install udtools` · installs (wheel) · licence: GPL-2.0-or-later · rank 7108 · last release 2026-10-22 · [PyPI](https://pypi.org/project/udtools/)

_README extract left out: share-alike licence._

### udapi

Python framework for processing Universal Dependencies data

`pip install udapi` · installs (wheel) · licence: GPL-3.0-or-later · rank 7113 · last release 2026-03-16 · [PyPI](https://pypi.org/project/udapi/)

_README extract left out: share-alike licence._

### uipath-llm-client

UiPath LLM Client

`pip install uipath-llm-client` · installs (wheel) · licence: not stated · rank 7142 · last release 2026-11-06 · [PyPI](https://pypi.org/project/uipath-llm-client/)

<details><summary>README extract</summary>

A Python client for interacting with UiPath's LLM services. This package provides both a low-level HTTP client and a LangChain integration for accessing LLMs through UiPath's infrastructure.

This repository is organized as a monorepo with the following packages: ...

Example:
```python
from uipath_langchain_client.clients.openai.chat_models import UiPathAzureChatOpenAI

# No settings needed - uses defaults from environment (AgentHub backend)
chat = UiPathAzureChatOpenAI(model="gpt-4o-2024-11-20")
response = chat.invoke("What is the capital of France?")
print(response.content)
```

...

</details>

### uipath-langchain-client

LangChain-compatible chat models and embeddings for UiPath's LLM services

`pip install uipath-langchain-client` · installs (wheel) · licence: not stated · rank 7190 · last release 2026-11-06 · [PyPI](https://pypi.org/project/uipath-langchain-client/)

<details><summary>README extract</summary>

LangChain-compatible chat models and embeddings for accessing LLMs through UiPath's infrastructure.

Example:
```python
from uipath_langchain_client import get_chat_model, get_embedding_model
from uipath_langchain_client.settings import get_default_client_settings

# Get default settings (uses UIPATH_LLM_SERVICE env var or defaults to AgentHub)
settings = get_default_client_settings()

# Chat model - vendor auto-detected from model name
chat_model = get_chat_model(
...
```

Sections: UiPath LangChain Client, Quick Start, Using Factory Functions (Recommended), Using Direct Client Classes, Available Client Types, Passthrough Mode (Default), Normalized Mode, Features, Streaming, Tool Calling, LangGraph Agents, Extended Thinking (Model-Specific), Configuration, Retry Configuration

</details>

### untangle

Converts XML to Python objects

`pip install untangle` · installs (wheel) · licence: MIT · rank 7258 · last release 2026-09-23 · [PyPI](https://pypi.org/project/untangle/)

<details><summary>README extract</summary>

Documentation

* Converts XML to a Python object.
* Siblings with similar names are grouped into a list.
* Children can be accessed with `parent.child`, attributes with `element['attribute']`.
* You can call the `parse()` method with a filename, an URL or an XML string. ...

Example:
```python
import untangle

obj = untangle.parse(resource)
```

Sections: untangle, Usage

</details>

### uv-sort

Sort uv's dependencies alphabetically

`pip install uv-sort` · installs (wheel) · licence: not stated · rank 7309 · last release 2026-08-30 · [PyPI](https://pypi.org/project/uv-sort/) · [source](https://github.com/ninoseki/uv-sort)

<details><summary>README extract</summary>

Sort uv's dependencies alphabetically.

The following sections are supported:

- `build-system.requires`
- `dependency-groups`
- `project.dependencies`
- `project.optional-dependencies`
- `tool.uv.build-constraint-dependencies`
- `tool.uv.constraint-dependencies`
- `tool.uv.dev-dependencies`
- `tool.uv.exclude-dependencies` ...

Sections: uv-sort, Usage, Options, With pre-commit, With Lefthook

</details>

### URLObject

A utility class for manipulating URLs.

`pip install URLObject` · installs (wheel) · licence: Public Domain · rank 7504 · last release 2025-07-11 · [PyPI](https://pypi.org/project/URLObject/)

<details><summary>README extract</summary>

`URLObject` is a utility class for manipulating URLs. The latest
incarnation of this library builds upon the ideas of its predecessor,
but aims for a clearer API, focusing on proper method names over
operator overrides. It's also being developed from the ground up in a
test-driven manner, and has full Sphinx documentation.

Sections: URLObject 3, Quickstart

</details>

### unittest-parametrize

Parametrize tests within unittest TestCases.

`pip install unittest-parametrize` · installs (wheel) · licence: MIT · rank 7792 · last release 2026-09-16 · [PyPI](https://pypi.org/project/unittest-parametrize/) · [source](https://github.com/adamchainz/unittest-parametrize)

<details><summary>README extract</summary>

Parametrize tests within unittest TestCases.

Testing a Django project?
Check out my book Speed Up Your Django Tests which covers loads of recommendations to write faster, more accurate tests.

Features:
|TestCase.subTest()|__ is unittest’s built-in “parametrization” solution.
You use it in a loop within a single test method:


This approach crams multiple actual tests into one test method, with several consequences: ...

Example:
```python
from unittest_parametrize import ParametrizedTestCase, parametrize

class SquareTests(ParametrizedTestCase):
    @parametrize(
        "x,expected",
        [
            (1, 1),
            (2, 4),
        ],
    )
    def test_square(self, x: int, expected: int) -> None:
        self.assertEqual(x**2, expected)
```

...

</details>

### Unified-python-sdk

Python Client SDK for Unified.to

`pip install Unified-python-sdk` · installs (wheel) · licence: not stated · rank 7949 · last release 2026-11-06 · [PyPI](https://pypi.org/project/Unified-python-sdk/) · [source](https://github.com/unified-to/unified-python-sdk.git)

<details><summary>README extract</summary>

Unified.to API: One API to Rule Them All

For more information about the API: API Documentation

Example:
```python
# !/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
# "Unified-python-sdk",
# ]
# ///

from unified_python_sdk import UnifiedTo

sdk = UnifiedTo(
  # SDK arguments
)

# Rest of script here...
```

Sections: Summary, uv, PIP, Poetry, Shell and script usage with `uv`, PyCharm, SDK Example Usage, Example, Available Resources and Operations, Account, Accounting, Activation, Activity, Ad

</details>

### uuid-extension

UUID7 Extension for Python

`pip install uuid-extension` · installs (wheel) · licence: not stated · rank 8184 · last release 2025-07-21 · [PyPI](https://pypi.org/project/uuid-extension/)

<details><summary>README extract</summary>

A Python library implementing UUID version 7 as specified in the RFC, providing time-ordered UUIDs for modern applications.

Features:
- Full implementation of UUID version 7
- Time-ordered UUIDs for better database performance
- Compatible with standard Python UUID objects
- Timestamp extraction capabilities
- Optional counter for monotonicity within milliseconds

Example:
```python
from uuid_extension import uuid7

# Generate a new UUID7
uuid = uuid7()
print(uuid)  # e.g., 018c1585-5e7c-7601-b322-5bf9f7478708

# Access the underlying UUID object
uuid_obj = uuid.uuid7
```

Sections: UUID Extension for Python, Features, Usage, Basic Usage, With Timestamp, With Counter, Time Extraction, Comparison Operations, Technical Details

</details>

### uefivars

UEFI variable store tools

`pip install uefivars` · installs (wheel) · licence: MIT License · rank 8305 · last release 2024-03-07 · [PyPI](https://pypi.org/project/uefivars/)

<details><summary>README extract</summary>

This is a set of Python modules and a helper application "uefivars" to
introspect and modify UEFI variable stores.

Features:
UEFI variable stores are typically opaque to users. You access them using
UEFI runtime services as function calls. However, the data is then stored
in a binary data format. ...

Sections: uefivars, Why do I need this?, How do I use it?

</details>

### universal-analytics-python3

Universal analytics python library

`pip install universal-analytics-python3` · installs (wheel) · licence: MIT License · rank 8681 · last release 2021-04-28 · [PyPI](https://pypi.org/project/universal-analytics-python3/)

<details><summary>README extract</summary>

It's a fork of universal-analytics-python
whith support for Python 3, batch requests, synchronous and asynchronous API calls.

This library provides a Python interface to Google Analytics, supporting the
Universal Analytics Measurement Protocol, with an interface modeled (loosely)
after Google's `analytics.js`. ...

Example:
```python
from universal_analytics import Tracker, HTTPRequest, HTTPBatchRequest

with HTTPRequest() as http:
    tracker = Tracker("UA-XXXXX-Y", http, client_id="unique-id")
    tracker.send("event", "Subscription", "billing")

with HTTPBatchRequest() as http:
    tracker = Tracker("UA-XXXXX-Y", http, client_id="unique-id")
...
```

Sections: Universal Analytics for Python, Usage, Changes

</details>

### utf-queue-client

No description provided

`pip install utf-queue-client` · installs (wheel) · licence: not stated · rank 8725 · last release 2026-10-28 · [PyPI](https://pypi.org/project/utf-queue-client/)

### unrar

Wrapper for UnRAR library, ctypes-based.

`pip install unrar` · installs (wheel) · licence: GPL-3 · rank 8859 · last release 2019-09-08 · [PyPI](https://pypi.org/project/unrar/)

_README extract left out: share-alike licence._

### ubai-client

Universal Binary Archiver Service

`pip install ubai-client` · installs (wheel) · licence: not stated · rank 9216 · last release 2025-12-09 · [PyPI](https://pypi.org/project/ubai-client/)

### ucimlrepo

Package to easily import datasets from the UC Irvine Machine Learning Repository into scripts and notebooks.

`pip install ucimlrepo` · installs (wheel) · licence: MIT License · rank 9955 · last release 2024-05-21 · [PyPI](https://pypi.org/project/ucimlrepo/)

<details><summary>README extract</summary>

Package to easily import datasets from the UC Irvine Machine Learning Repository into scripts and notebooks.

Current Version: 0.0.7

Sections: `ucimlrepo` package, Example Usage, `fetch_ucirepo`, Parameters, Returns, `list_available_datasets`, Metadata, Links

</details>

### uwsgitop

uWSGI top-like interface

`pip install uwsgitop` · installs from source (sdist only) · licence: MIT · rank 9970 · last release 2024-04-01 · [PyPI](https://pypi.org/project/uwsgitop/)

<details><summary>README extract</summary>

`uwsgitop` is a top-like command that uses the uWSGI Stats Server to
monitor your uwsgi application.

To use uWSGI Stat Server simply use the `stats` option followed by
a valid socket address, for example:
To start monitoring your application with `uwsgitop` call it with
the socket address like so:
If you want the stats served over HTTP you will ...

Sections: uwsgitop, Usage, Colors, Further Reading

</details>

### unicrypto

Unified interface for cryptographic libraries

`pip install unicrypto` · installs (wheel) · licence: not stated · rank 9971 · last release 2025-10-29 · [PyPI](https://pypi.org/project/unicrypto/)

### usd-exchange

OpenUSD Exchange provides higher-level convenience functions as a companion to lower-level OpenUSD concepts

`pip install usd-exchange` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 10134 · last release 2026-10-07 · [PyPI](https://pypi.org/project/usd-exchange/) · [docs](https://docs.omniverse.nvidia.com/usd/code-docs/usd-exchange-sdk) · [source](https://github.com/NVIDIA-Omniverse/usd-exchange)

<details><summary>README extract</summary>

OpenUSD Exchange SDK accelerates OpenUSD adoption by helping developers design, build, and test their own USD I/O solutions, producing consistent and correct USD assets across diverse 3D ecosystems. ...

</details>

### usd-validation-nvidia

USD Validation NVIDIA

`pip install usd-validation-nvidia` · installs (wheel) · licence: Apache-2.0 AND CC-BY-4.0 · rank 10215 · last release 2026-10-27 · [PyPI](https://pypi.org/project/usd-validation-nvidia/) · [docs](https://nvidia-omniverse.github.io/usd-validation-nvidia/) · [source](https://github.com/NVIDIA-Omniverse/usd-validation-nvidia)

<details><summary>README extract</summary>

An extensible framework to validate OpenUSD assets.
Inspired by Pixar's usdchecker,
this library extends validation capabilities with additional rules and provides automatic issue fixing.

It is the standalone successor to `omniverse-asset-validator` and is intended for use in any USD pipeline.

Features:
- Rule-based validation — Modular rule interface with registration mechanism for custom validators
- Flexible engine — Run validation on a `Usd.Stage`, individual layers, or recursively search folders ...

Example:
```python
from usd_validation_nvidia import ValidationEngine, IssueFixer

engine = ValidationEngine()
asset = "path/to/asset.usda"
results = engine.validate(asset)

for issue in results.issues():
    print(f"{issue.severity}: {issue.message}")

fixer = IssueFixer(asset)
...

</details>

### unsync

Unsynchronize asyncio

`pip install unsync` · installs from source (sdist only) · licence: MIT · rank 10347 · last release 2021-10-21 · [PyPI](https://pypi.org/project/unsync/)

<details><summary>README extract</summary>

Unsynchronize `asyncio` by using an ambient event loop, or executing in separate threads or processes.

Functions marked with the `@unsync` decorator will behave in one of the following ways:
* `async` functions will run in the `unsync.loop` event loop executed from `unsync.thread`
* Regular functions will execute in `unsync.thread_executor`, a ...

Example:
```python
async def sync_async():
    await asyncio.sleep(1)
    return 'I hate event loops'

async def main():
    future1 = asyncio.create_task(sync_async())
    future2 = asyncio.create_task(sync_async())

    await future1, future2

    print(future1.result() + future2.result())

asyncio.run(main())
# Takes 1 second to run
```

...

</details>

### ulid

Pyhton version of this: https://github.com/alizain/ulid

`pip install ulid` · installs from source (sdist only) · licence: BSD · rank 10793 · last release 2016-08-01 · [PyPI](https://pypi.org/project/ulid/)

### urdf-usd-converter

A URDF to OpenUSD Data Converter

`pip install urdf-usd-converter` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 10805 · last release 2026-11-05 · [PyPI](https://pypi.org/project/urdf-usd-converter/) · [docs](https://github.com/newton-physics/urdf-usd-converter/#readme) · [source](https://github.com/newton-physics/urdf-usd-converter)

<details><summary>README extract</summary>

Features:
A URDF to OpenUSD Data Converter

> Important: This is currently an Alpha product. See the CHANGELOG for features and known limitations.

Key Features:
- Converts an input URDF file into an OpenUSD Layer ...

Example:
```python
import urdf_usd_converter
import usdex.core
from pxr import Sdf, Usd

converter = urdf_usd_converter.Converter()
asset: Sdf.AssetPath = converter.convert("/path/to/robot.urdf", "/path/to/usd_robot")
stage: Usd.Stage = Usd.Stage.Open(asset.path)
# modify further using Usd or usdex.core functionality
...
```

Sections: urdf-usd-converter, Overview, Implementation Details & Dependencies, Get Started, Specifying ROS packages, CLI, Python, Loading the USD Asset, References

</details>

### up-pyperplan

up_pyperplan

`pip install up-pyperplan` · installs (wheel) · licence: APACHE · rank 11275 · last release 2024-01-30 · [PyPI](https://pypi.org/project/up-pyperplan/)

### unidep

Unified Conda and Pip requirements management.

`pip install unidep` · installs (wheel) · licence: not stated · rank 11423 · last release 2026-06-25 · [PyPI](https://pypi.org/project/unidep/)

<details><summary>README extract</summary>

> UniDep streamlines Python project dependency management by unifying Conda and Pip packages in a single system.
> Learn when to use UniDep in our FAQ.

Handling dependencies in Python projects can be challenging, especially when juggling Python and non-Python packages. ...

Sections: UniDep - Unified Conda and Pip Dependency Management, rocket: Bootstrap from Scratch, memo: `requirements.yaml` and `pyproject.toml` structure, Example, Example `requirements.yaml`, Example `pyproject.toml`, Key Points, Conflict Resolution, How It Works, Platform Selectors, Usage, Implementation, Custom Pip Index URLs

</details>

### unifi-core

UniFi controller connectivity: auth, detection, retry, exceptions

`pip install unifi-core` · installs (wheel) · licence: not stated · rank 12082 · last release 2026-11-07 · [PyPI](https://pypi.org/project/unifi-core/)

### udatetime

Fast RFC3339 compliant date-time library

`pip install udatetime` · installs from source (sdist only) · licence: Apache Software License · rank 12137 · last release 2022-08-12 · [PyPI](https://pypi.org/project/udatetime/)

### unyt

A package for handling numpy arrays with units

`pip install unyt` · installs (wheel) · licence: BSD-3-Clause · rank 12164 · last release 2026-10-19 · [PyPI](https://pypi.org/project/unyt/) · [docs](https://unyt.readthedocs.io/en/stable/index.html)

<details><summary>README extract</summary>

.. image::
 :target:
 :alt: The yt Project

A package for handling numpy arrays with units.

Often writing code that deals with data that has units can be confusing. A
function might return an array but at least with plain NumPy arrays, there is no
way to easily tell what the units of the data are without somehow knowing *a
priori*. ...

</details>

### use-computer

Python SDK for use.computer macOS sandboxes

`pip install use-computer` · installs (wheel) · licence: not stated · rank 12505 · last release 2026-09-04 · [PyPI](https://pypi.org/project/use-computer/) · [docs](https://api.use.computer/docs) · [source](https://github.com/josancamon19/use-computer-sdk)

<details><summary>README extract</summary>

use.computer gives you macOS sandboxes: VMs on dedicated Apple M4 Mac minis that you reserve for 24 hours or more, up to 2 VMs at a time per Mac.

Optional agent integrations are installed explicitly:

Base installs only the SDK client and `httpx`. ...

Example:
```python
from use_computer import Computer

client = Computer()

# 1. Reserve one Mac Mini for 24 hours
reservation = client.reserve(hours=24)

# 2. Launch a macOS sandbox on the reserved Mac
with client.create(reservation_id=reservation.id) as mac:
    # 3. Drive the macOS sandbox
    mac.exec("open -a Safari")
...
```

Sections: use-computer Python SDK, Quickstart, Runtime Snapshots, Examples, HTTP API

</details>

### urdf-parser-py

This package contains a python parser for the Unified Robot Description Format (URDF), which is an XML format for representing a robot model.

`pip install urdf-parser-py` · installs from source (sdist only) · licence: not stated · rank 12594 · last release 2021-11-11 · [PyPI](https://pypi.org/project/urdf-parser-py/)

<details><summary>README extract</summary>

This package contains a python parser for the Unified Robot Description Format (URDF), which is an XML format for representing a robot model.

</details>

### uptrace

OpenTelemetry Python distribution for Uptrace

`pip install uptrace` · installs (wheel) · licence: BSD-3-Clause · rank 12898 · last release 2026-10-06 · [PyPI](https://pypi.org/project/uptrace/) · [source](https://github.com/uptrace/uptrace-python)

<details><summary>README extract</summary>

uptrace-python is a thin wrapper over
opentelemetry-python that exports
traces,
metrics, and logs to Uptrace.

- Documentation
- Examples
- OpenTelemetry Django
- OpenTelemetry Flask
- OpenTelemetry FastAPI
- OpenTelemetry SQLAlchemy

Sections: Uptrace for Python, Introduction

</details>

### unasync

The async transformation code.

`pip install unasync` · installs (wheel) · licence: Apache Software License; MIT License · rank 13082 · last release 2024-05-03 · [PyPI](https://pypi.org/project/unasync/)

<details><summary>README extract</summary>

Welcome to unasync, a project that can transform your asynchronous code into synchronous code.

See for more details about unasync.

 * httpcore, another low-level HTTP client uses a different implementation of the same idea:

Example:
```python
import unasync

setuptools.setup(
    ...
    cmdclass={'build_py': unasync.cmdclass_build_py()},
    ...
)
```

Sections: unasync, Users, Usage, Documentation

</details>

### unidiff2

Unified diff parsing/metadata extraction library.

`pip install unidiff2` · installs (wheel) · licence: MIT License · rank 13630 · last release 2025-10-30 · [PyPI](https://pypi.org/project/unidiff2/)

<details><summary>README extract</summary>

Simple Python library to parse and interact with unified diff data.

The original version seems not to be actively maintained.
This repository intend to offer an actively maintained version of unidiff.

Example:
```python
>>> import urllib.request
>>> from unidiff import PatchSet
>>> diff = urllib.request.urlopen('
>>> encoding = diff.headers.get_charsets()[0]
>>> patch = PatchSet(diff, encoding=encoding)
>>> patch
<PatchSet: [<PatchedFile: .gitignore>, <PatchedFile: unidiff/patch.py>, <PatchedFile: unidiff/utils.py>]>
>>> patch[0]
<PatchedFile: .gitignore>
...
```

Sections: Unidiff, Quick start, Load a local diff file, References

</details>

### ur-rtde

A Python interface for controlling and receiving data from a UR robot using the Real-Time Data Exchange (RTDE) interface of the robot.

`pip install ur-rtde` · installs from source (sdist only) · licence: MIT License · rank 13671 · last release 2026-08-09 · [PyPI](https://pypi.org/project/ur-rtde/) · [docs](https://sdurobotics.gitlab.io/ur_rtde/) · [source](https://gitlab.com/sdurobotics/ur_rtde.git)

<details><summary>README extract</summary>

A C++ interface for controlling and receiving data from a UR robot using the
Real-Time Data Exchange (RTDE)
 interface of the robot. The interface can also be used with python, through the provided python bindings. ...

Features:
* Fast and lightweight interface for programming UR robots.
 * Uses the Real-Time Data Exchange (RTDE) of the robot.
 * Execute with real-time priority on operating systems with a real-time kernel, see the Real-time Setup Guide
 * Available on ...

Sections: Key Features, Documentation, From PPA, From PyPi, Dependencies, Compatible Robots, Compatible Operating Systems, Contact

</details>

### unifi-network-mcp

Unifi Network MCP Server

`pip install unifi-network-mcp` · installs (wheel) · licence: not stated · rank 14090 · last release 2026-11-06 · [PyPI](https://pypi.org/project/unifi-network-mcp/)

<details><summary>README extract</summary>

MCP server exposing 210 UniFi Network Controller tools for AI assistants and
other MCP-capable clients. Query clients, devices, firewall rules, VLANs, VPNs,
Traffic Flows, stats, and more with safe-by-default permissions and
preview-before-confirm for all mutations. ...

Sections: UniFi Network MCP Server, Claude Code (recommended), Codex, PyPI / Docker, Usage Examples, V2 NAT rules, Configure, API-key inventory and session authentication, MCP response size, Sensitive response fields, Run, Claude Desktop, Agent Skills, Network Health Check

</details>

### unifi-mcp-shared

Shared MCP server patterns: permissions, confirmation, lazy loading, config

`pip install unifi-mcp-shared` · installs (wheel) · licence: not stated · rank 14159 · last release 2026-11-02 · [PyPI](https://pypi.org/project/unifi-mcp-shared/)

### urlman

Django URL pattern helpers

`pip install urlman` · installs (wheel) · licence: not stated · rank 14236 · last release 2025-12-23 · [PyPI](https://pypi.org/project/urlman/)

<details><summary>README extract</summary>

A nicer way to do URLs for Django models.

Replaces things like `get_absolute_url` with a `.urls` attribute that
can reference other URLs and build sensible trees of things, and can
then be accessed using `instance.urls.name`. ...

Example:
```python
import urlman

class Group(models.Model):

...

    class urls(urlman.Urls):
        view = "/{self.slug}/"
        users = "{view}users/"
        admin = "{view}admin/"

def my_view(request):
    group = ...
    return redirect(group.urls.view)
```

</details>

### ursina

An easy to use game engine/framework for python.

`pip install ursina` · installs (wheel) · licence: MIT · rank 14760 · last release 2025-12-06 · [PyPI](https://pypi.org/project/ursina/)

<details><summary>README extract</summary>

Website | Discord | Twitter | Patreon | Sponsor

An easy to use game engine/framework for python.

Example:
```python
from ursina import *            # this will import everything we need from ursina with just one line.

app = Ursina()
ground = Entity(
    model = 'cube',
    color = color.magenta,
    z = -.1,
    y = -3,
    origin = (0, .5),
    scale = (50, 1, 10),
    collider = 'box',
    )

...
```

Sections: ursina ʕ •ᴥ•ʔゝ□, Getting Started, Dependencies, Examples, How do I make a game?, Documentation, Project Structure

</details>

### update

(no summary)

`pip install update` · installs (wheel) · licence: MIT · rank 14874 · last release 2017-11-13 · [PyPI](https://pypi.org/project/update/)

<details><summary>README extract</summary>

update is a

Example:
```python
import update

update.check()
```

Sections: update, Usage

</details>

