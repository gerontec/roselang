# Unclassified / B

[Index](README.md) · 172 packages in this topic, by downloads.

### boto3

The AWS SDK for Python (Boto3)

`pip install boto3` · installs (wheel) · licence: Apache-2.0 · rank 1 · last release 2026-11-06 · [PyPI](https://pypi.org/project/boto3/) · [docs](https://docs.aws.amazon.com/boto3/latest/) · [source](https://github.com/boto/boto3)

<details><summary>README extract</summary>

Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use
of services like Amazon S3 and Amazon EC2. You can find the latest, most
up to date, documentation at our doc site, including a list of
services that are supported. ...

Example:
```python
>>> import boto3
>>> s3 = boto3.resource('s3')
>>> for bucket in s3.buckets.all():
        print(bucket.name)
```

Sections: Boto3 - The AWS SDK for Python, Notices, Getting Started, Using Boto3, Running Tests, Getting Help, More Resources

</details>

### botocore

Low-level, data-driven core of boto 3.

`pip install botocore` · installs (wheel) · licence: Apache-2.0 · rank 22 · last release 2026-11-06 · [PyPI](https://pypi.org/project/botocore/)

<details><summary>README extract</summary>

Sections: Notices, Getting Started, Getting Help, More Resources

</details>

### blinker

Fast, simple object-to-object and broadcast signaling

`pip install blinker` · installs (wheel) · licence: MIT License · rank 171 · last release 2024-11-08 · [PyPI](https://pypi.org/project/blinker/) · [docs](https://blinker.readthedocs.io) · [source](https://github.com/pallets-eco/blinker/)

<details><summary>README extract</summary>

Blinker provides a fast dispatching system that allows any number of
interested parties to subscribe to events, or "signals".

Example:
```python
>>> from blinker import signal
>>> started = signal('round-started')
>>> def each(round):
...     print(f"Round {round}")
...
>>> started.connect(each)

>>> def round_two(round):
...     print("This is round two.")
...
>>> started.connect(round_two, sender=2)

>>> for round in range(1, 4):
...     started.send(round)
...
Round 1!
Round 2!
...
```

Sections: Blinker, Example

</details>

### bcrypt

Modern password hashing for your software and your servers

`pip install bcrypt` · installs (wheel) · licence: Apache Software License · rank 189 · last release 2025-09-25 · [PyPI](https://pypi.org/project/bcrypt/)

<details><summary>README extract</summary>

Acceptable password hashing for your software and your servers (but you should
really use argon2id or scrypt)

Example:
```python
>>> import bcrypt
>>> password = b"super secret password"
>>> # Hash a password for the first time, with a randomly-generated salt
>>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
>>> # Check that an unhashed password matches one that has previously been
>>> # hashed
>>> if bcrypt.checkpw(password, hashed):
...     print("It Matches!")
...
```

Sections: bcrypt, Alternatives, 5.0.0, 4.3.0, 4.2.1, 4.2.0, 4.1.3, 4.1.2, 4.1.1, 4.1.0, 4.0.1, 4.0.0, 3.2.2, 3.2.1

</details>

### build

A simple, correct Python build frontend

`pip install build` · installs (wheel) · licence: MIT · rank 290 · last release 2026-09-10 · [PyPI](https://pypi.org/project/build/) · [source](https://github.com/pypa/build)

<details><summary>README extract</summary>

A simple, correct Python build frontend.

See the documentation for more information.

Sections: build, Usage, Common arguments, Integration with other tools, pipx, uv, cibuildwheel, Conda-forge

</details>

### boto3-stubs

Type annotations for boto3 1.43.126 generated with mypy-boto3-builder 8.12.0

`pip install boto3-stubs` · installs (wheel) · licence: MIT · rank 498 · last release 2026-11-06 · [PyPI](https://pypi.org/project/boto3-stubs/) · [docs](https://youtype.github.io/boto3_stubs_docs/) · [source](https://github.com/youtype/mypy_boto3_builder)

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
boto3-stubs docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### backports.tarfile

Backport of CPython tarfile module

`pip install backports.tarfile` · installs (wheel) · licence: MIT License · rank 547 · last release 2024-05-28 · [PyPI](https://pypi.org/project/backports.tarfile/)

### bidict

The bidirectional mapping library for Python.

`pip install bidict` · installs (wheel) · licence: MPL-2.0 · rank 673 · last release 2026-08-25 · [PyPI](https://pypi.org/project/bidict/) · [docs](https://bidict.readthedocs.io) · [source](https://github.com/jab/bidict)

<details><summary>README extract</summary>

*The bidirectional mapping library for Python.*

Features:
- Mature: Depended on by
 Google, Venmo, CERN, Baidu, Tencent,
 and teams across the world since 2009

- Familiar, Pythonic APIs
 that are carefully designed for
 safety, simplicity, flexibility, and ergonomics ...

Example:
```python
>>> from bidict import bidict
>>> element_by_symbol = bidict({'H': 'hydrogen'})
>>> element_by_symbol['H']
'hydrogen'
>>> element_by_symbol.inverse['hydrogen']
'H'
```

Sections: bidict, Features, Quick Start, Notice of Usage, Learning from bidict, Finding Documentation

</details>

### bs4

Dummy package for Beautiful Soup (beautifulsoup4)

`pip install bs4` · installs (wheel) · licence: MIT License · rank 911 · last release 2024-01-17 · [PyPI](https://pypi.org/project/bs4/)

<details><summary>README extract</summary>

This is a dummy package designed to prevent namesquatting on PyPI. You should install beautifulsoup4 instead.

</details>

### basedpyright

static type checking for Python (but based)

`pip install basedpyright` · installs (wheel) · licence: MIT License · rank 940 · last release 2026-10-04 · [PyPI](https://pypi.org/project/basedpyright/) · [source](https://github.com/detachhead/basedpyright)

<details><summary>README extract</summary>

Basedpyright is a fork of pyright with various type checking improvements, pylance features and more.

See the documentation for information about why this fork exists, and a comprehensive list of features and improvements we've made to pyright.

</details>

### binaryornot

Ultra-lightweight pure Python package to check if a file is binary or text.

`pip install binaryornot` · installs (wheel) · licence: MIT License · rank 1079 · last release 2026-03-08 · [PyPI](https://pypi.org/project/binaryornot/) · [docs](https://binaryornot.github.io/binaryornot/)

<details><summary>README extract</summary>

Python library and CLI tool to check if a file is binary or text. Zero dependencies.

Features:
That's the first thing everyone tries. It works until it doesn't:

- A UTF-16 text file is full of null bytes. Your tool thinks it's binary and corrupts it.
- A Big5 or GB2312 text file has high-ASCII bytes everywhere. ...

Example:
```python
from binaryornot.check import is_binary

is_binary("image.png")    # True
is_binary("README.md")    # False
is_binary("data.sqlite")  # True
is_binary("report.csv")   # False
```

Sections: BinaryOrNot, Why not just check for null bytes?, API

</details>

### burner-redis

An embedded, in-process Redis-compatible database

`pip install burner-redis` · installs (wheel) · licence: MIT License · rank 1267 · last release 2026-05-08 · [PyPI](https://pypi.org/project/burner-redis/) · [source](https://github.com/PrefectHQ/burner-redis)

<details><summary>README extract</summary>

> Experimental: This library is under active development and not yet ready for production use. APIs may change without notice.

An embedded, in-process Redis-compatible database written in Rust with Python bindings. Drop-in replacement for `redis.asyncio.Redis` that runs inside the host process with no external server needed. ...

Example:
```python
from burner_redis import BurnerRedis

db = BurnerRedis()

# Use like redis.asyncio.Redis
await db.set("key", "value")
value = await db.get("key")

# Persistence across restarts
db = BurnerRedis(persistence_path="data.dat")
await db.set("key", "value")
# Data is saved on process exit and reloaded on next start
```

...

</details>

### backcall

Specifications for callback functions passed in to an API

`pip install backcall` · installs (wheel) · licence: BSD License · rank 1373 · last release 2020-06-09 · [PyPI](https://pypi.org/project/backcall/)

<details><summary>README extract</summary>

Specifications for callback functions passed in to an API

If your code lets other people supply callback functions, it's important to
specify the function signature you expect, and check that functions support that.
Adding extra parameters later would break other peoples code unless you're careful. ...

Example:
```python
from backcall import callback_prototype

@callback_prototype
def handle_ping(sender, delay=None):
    # Specify positional parameters without a default, and keyword
    # parameters with a default.
    pass

def register_ping_handler(callback):
    # This checks and adapts the function passed in:
    callback = handle_ping.adapt(callback)
...
```

</details>

### braintrust

SDK for integrating Braintrust

`pip install braintrust` · installs (wheel) · licence: MIT · rank 1460 · last release 2026-11-06 · [PyPI](https://pypi.org/project/braintrust/) · [source](https://github.com/braintrustdata/braintrust-sdk-python)

<details><summary>README extract</summary>

The official Python SDK for logging, tracing, and evaluating AI applications with Braintrust.

Example:
```python
from braintrust import Eval

def is_equal(expected, output):
    return expected == output

Eval(
    "Say Hi Bot",
    data=lambda: [
        {"input": "Foo", "expected": "Hi Foo"},
        {"input": "Bar", "expected": "Hello Bar"},
    ],
    task=lambda input: "Hi " + input,
    scores=[is_equal],
)
```

Sections: Braintrust Python SDK, Quickstart, Optional Extras, Documentation

</details>

### bazel-runfiles

(no summary)

`pip install bazel-runfiles` · installs (wheel) · licence: Apache Software License · rank 1469 · last release 2026-10-30 · [PyPI](https://pypi.org/project/bazel-runfiles/)

<details><summary>README extract</summary>

This is a Bazel Runfiles lookup library for Bazel-built Python binaries and tests.

Learn about runfiles: read Runfiles guide
or watch Fabian's BazelCon talk.

The Runfiles API is available from two sources, a direct Bazel target, and a pypi package.

1. ...

Example:
```python
r = Runfiles.Create()
# ...
with open(r.Rlocation("my_workspace/path/to/my/data.txt"), "r") as f:
    contents = f.readlines()
    # ...
```

Sections: bazel-runfiles library, Importing, Pure Bazel imports, Pypi imports, Typical Usage

</details>

### browser-use

Open-source browser agent + hosted cloud browsers for AI agents, from $0.02/browser-hour

`pip install browser-use` · installs (wheel) · licence: MIT License · rank 1523 · last release 2026-10-26 · [PyPI](https://pypi.org/project/browser-use/) · [docs](https://docs.browser-use.com) · [source](https://github.com/browser-use/browser-use)

<details><summary>README extract</summary>

The open-source browser agent. Run it locally with any LLM, or on Browser Use Cloud: stealth browsers from $0.02/hour, top score (90.5%) on Stealth Bench V2.

Find an available slot, pick a date and time, handle the CAPTCHA, and book a driving test.

Explore more demos and prompts ↗ ...

Example:
```python
import asyncio

from browser_use import Agent, Browser, ChatBrowserUse, ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

async def main():
    llm = ChatOpenAI(model='gpt-5.6-luna', reasoning_effort='xhigh')
    # llm = ChatBrowserUse(model='bu-2-0')  # Use BU2 instead; requires BROWSER_USE_API_KEY
    agent = Agent(
...
```

...

</details>

### browser-use-sdk

Python SDK for the Browser Use cloud API

`pip install browser-use-sdk` · installs (wheel) · licence: MIT · rank 1558 · last release 2026-10-17 · [PyPI](https://pypi.org/project/browser-use-sdk/) · [source](https://github.com/browser-use/sdk)

<details><summary>README extract</summary>

Official Python SDK for Browser Use Cloud.

Example:
```python
from browser_use_sdk.v4 import BrowserUse

with BrowserUse() as client:
    run = client.runs.create("Find the top 3 trending repos on GitHub today")
    result = client.runs.wait_for_completion(run.id)
    print(result.result)
```

Sections: browser-use-sdk, Quick Start, v3 Bring Your Own LLM Key, Docs, V4 structured output

</details>

### bubus

Advanced Pydantic-powered event bus with async support

`pip install bubus` · installs (wheel) · licence: MIT License · rank 1574 · last release 2025-08-30 · [PyPI](https://pypi.org/project/bubus/) · [source](https://github.com/browser-use/bubus)

<details><summary>README extract</summary>

Bubus is a fully-featured, Pydantic-powered event bus library for async Python.

It's designed for quickly building event-driven applications with Python in a way that "just works" with async support, proper support for nested events, and real concurrency control. ...

Example:
```python
import asyncio
from bubus import EventBus, BaseEvent
from your_auth_events import AuthRequestEvent, AuthResponseEvent

class UserLoginEvent(BaseEvent[str]):
    username: str
    is_admin: bool

async def handle_login(event: UserLoginEvent) -> str:
    auth_request = await event.event_bus.dispatch(AuthRequestEvent(...))  # nested events supported
...
```

...

</details>

### blobfile

Read GCS, ABS and local paths with the same interface, clone of tensorflow.io.gfile

`pip install blobfile` · installs (wheel) · licence: Public Domain · rank 1684 · last release 2026-08-20 · [PyPI](https://pypi.org/project/blobfile/)

<details><summary>README extract</summary>

This is a library that provides a Python-like interface for reading local and remote files (only from blob storage), with an API similar to `open()` as well as some of the `os.path` and `shutil` functions. `blobfile` supports local paths, Google Cloud Storage paths (`gs://<bucket>`), and Azure Blob Storage paths (`az://<account>/<container>` or ` ...

Example:
```python
# write a file, then read it back

import blobfile as bf

with bf.BlobFile("gs://my-bucket-name/cats", "wb") as f:
    f.write(b"meow!")

print("exists:", bf.exists("gs://my-bucket-name/cats"))

with bf.BlobFile("gs://my-bucket-name/cats", "rb") as f:
    print("contents:", f.read())
```

...

</details>

### bullmq

BullMQ for Python

`pip install bullmq` · installs (wheel) · licence: MIT License · rank 1805 · last release 2026-11-04 · [PyPI](https://pypi.org/project/bullmq/)

<details><summary>README extract</summary>

This is the official BullMQ Python library. It is a close port of the NodeJS version of the library.
Python Queues are interoperable with NodeJS Queues, as both libraries use the same .lua scripts that
power all the functionality.

Features:
Currently, the library does not support all the features available in the NodeJS version. The following
have been ported so far:

- [x] Add jobs to queues.
 - [x] Regular jobs.
 - [x] Delayed jobs.
 - [x] Job deduplication.
 - [x] Job priority. ...

Example:
```python
from bullmq import Queue

queue = Queue('my-queue')

job = await queue.add('my-job', {'foo': 'bar'})
```

Sections: BullMQ For Python, Features, Usage, Basic Example, Job Priority, Job Deduplication, Documentation, Copyright

</details>

### banks

A prompt programming language

`pip install banks` · installs (wheel) · licence: MIT · rank 1844 · last release 2026-09-10 · [PyPI](https://pypi.org/project/banks/) · [docs](https://github.com/masci/banks#readme) · [source](https://github.com/masci/banks)

<details><summary>README extract</summary>

Banks is the linguist professor who will help you generate meaningful
LLM prompts using a template language that makes sense. If you're still using `f-strings` for the job, keep reading.

Docs are available here.

Table of Contents ...

Features:
Prompts are instrumental for the success of any LLM application, and Banks focuses around specific areas of their
lifecycle:
- :orange_book: Templating: Banks provides tools and functions to build prompts text and chat messages from generic ...

Example:
```python
from banks import Prompt

prompt_template = """
{% chat role="system" %}
You are a {{ persona }}.
{% endchat %}

{% chat role="user" %}
Hello, how are you?
{% endchat %}
"""

p = Prompt(prompt_template)
print(p.chat_messages({"persona": "helpful assistant"}))

# Output:
# [
...

</details>

### backports.zoneinfo

Backport of the standard library zoneinfo module

`pip install backports.zoneinfo` · installs from source (sdist only) · licence: Apache Software License · rank 1958 · last release 2020-06-23 · [PyPI](https://pypi.org/project/backports.zoneinfo/) · [docs](https://zoneinfo.readthedocs.io/en/latest/) · [source](https://github.com/pganssle/zoneinfo)

<details><summary>README extract</summary>

This package was originally the reference implementation for PEP 615, which proposes support for the IANA time zone database in the standard library, and now serves as a backport to Python 3.6+ (including PyPy).

This exposes the `backports.zoneinfo` module, which is a backport of the `zoneinfo` module. ...

Example:
```python
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo
```

</details>

### base58

Base58 and Base58Check implementation.

`pip install base58` · installs (wheel) · licence: MIT License · rank 2222 · last release 2021-10-30 · [PyPI](https://pypi.org/project/base58/)

<details><summary>README extract</summary>

[](
[](
[](
[](

Base58 and Base58Check implementation compatible with what is used by the
bitcoin network. Any other alternative alphabet (like the XRP one) can be used.

Starting from version 2.0.0 python2 is no longer supported the 1.x series
will remain supported but no new features will be added.

Sections: base58, Command line usage, Module usage

</details>

### bpy

Blender as a Python module

`pip install bpy` · does not install on CPython 3.14 · licence: GPL-3.0 · rank 2351 · last release 2026-10-22 · [PyPI](https://pypi.org/project/bpy/)

_README extract left out: share-alike licence._

### betterproto

A better Protobuf / gRPC generator & library

`pip install betterproto` · installs from source (sdist only) · licence: MIT · rank 2405 · last release 2020-05-27 · [PyPI](https://pypi.org/project/betterproto/)

<details><summary>README extract</summary>

Example:
```python
>>> MyMessage().to_dict(casing=betterproto.Casing.SNAKE)
```

Sections: Motivation, JSON, Determining if a message was sent, Well-Known Google Types, Code style, Tests, Standard tests, Custom tests, Running, TODO

</details>

### bitstruct

This module performs conversions between Python values and C bit field structs represented as Python byte strings.

`pip install bitstruct` · installs (wheel) · licence: MIT · rank 2601 · last release 2026-10-23 · [PyPI](https://pypi.org/project/bitstruct/) · [docs](https://bitstruct.readthedocs.io/en/latest/) · [source](https://github.com/eerimoq/bitstruct)

<details><summary>README extract</summary>

This module is intended to have a similar interface as the python
struct module, but working on bits instead of primitive data types
(char, int, ...).

Project homepage:

Documentation:

Example:
```python
>>> from bitstruct import *
>>> pack('u1u3u4s16', 1, 2, 3, -4)
b'\xa3\xff\xfc'
>>> unpack('u1u3u4s16', b'\xa3\xff\xfc')
(1, 2, 3, -4)
>>> calcsize('u1u3u4s16')
24
```

Sections: About, Performance, MicroPython, Example usage, . Fork the repository., . Implement the new feature or bug fix., . Run the tests., . Create a pull request.

</details>

### braceexpand

Bash-style brace expansion for Python

`pip install braceexpand` · installs (wheel) · licence: MIT License · rank 2621 · last release 2021-05-07 · [PyPI](https://pypi.org/project/braceexpand/)

<details><summary>README extract</summary>

Implements Brace Expansion as described in
bash(1),
with the following limitations:

- A pattern containing unbalanced braces will raise an
 `UnbalancedBracesError` exception. In bash, unbalanced braces will
 either be partly expanded or ignored. ...

Example:
```python
>>> from braceexpand import braceexpand

# Integer range
>>> list(braceexpand('item{1..3}'))
['item1', 'item2', 'item3']

# Character range
>>> list(braceexpand('{a..c}'))
['a', 'b', 'c']

# Sequence
>>> list(braceexpand('index.html{,.backup}'))
['index.html', 'index.html.backup']

# Nested patterns
...
```

Sections: Bash-style brace expansion for Python, Examples

</details>

### branca

Generate complex HTML+JS pages with Python

`pip install branca` · installs (wheel) · licence: MIT License · rank 2680 · last release 2025-10-06 · [PyPI](https://pypi.org/project/branca/)

<details><summary>README extract</summary>

This library is a spinoff from folium. It can be used to generate HTML + JS. It is based on Jinja2.

</details>

### browser-cookie3

Loads cookies from your browser into a cookiejar object so can download with urllib and other libraries the same content you see in the web browser.

`pip install browser-cookie3` · installs (wheel) · licence: lgpl · rank 2773 · last release 2025-01-04 · [PyPI](https://pypi.org/project/browser-cookie3/)

_README extract left out: share-alike licence._

### braintrust-core

Shared core dependencies for Braintrust packages

`pip install braintrust-core` · installs (wheel) · licence: not stated · rank 2795 · last release 2025-05-12 · [PyPI](https://pypi.org/project/braintrust-core/)

<details><summary>README extract</summary>

This package contains a small set of dependencies shared by various packages in
the braintrust ecosystem.

</details>

### backports.strenum

Base class for creating enumerated constants that are also subclasses of str

`pip install backports.strenum` · does not install on CPython 3.14 · licence: MIT License · rank 2943 · last release 2023-12-09 · [PyPI](https://pypi.org/project/backports.strenum/) · [source](https://github.com/clbarnes/backports.strenum)

<details><summary>README extract</summary>

A backport of (copy and paste from) python 3.11's `StrEnum` class for >=3.8.6:

See the design discussion,
and Ethan Furman's first and
second PR with this implementation.

A slightly different implementation would likely be compatible with lower python versions;
PRs are welcome if they pass the test suite. ...

Example:
```python
import sys

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from backports.strenum import StrEnum

class MyStrEnum(StrEnum):
    POTATO = "potato"
    ORANGE = "orange"
    SPADE = "spade"

MyStrEnum.POTATO == "potato"  # True
MyStrEnum.ORANGE.upper() == "ORANGE"  # True
str(MyStrEnum.SPADE) == "spade"  # True
```

Sections: backports.strenum, Gotchas, `class enum.StrEnum`

</details>

### braintree

Braintree Python Library

`pip install braintree` · installs (wheel) · licence: MIT License · rank 2948 · last release 2026-10-19 · [PyPI](https://pypi.org/project/braintree/)

<details><summary>README extract</summary>

The Braintree Python SDK provides integration access to the Braintree Gateway.

 1. - README and Samples
 2. - API Reference

</details>

### bleak

Bluetooth Low Energy platform Agnostic Klient

`pip install bleak` · installs (wheel) · licence: MIT · rank 3083 · last release 2026-11-07 · [PyPI](https://pypi.org/project/bleak/) · [docs](https://bleak.readthedocs.io)

<details><summary>README extract</summary>

Bleak is an acronym for Bluetooth Low Energy platform Agnostic Klient.

* Free software: MIT license

Bleak is a GATT client software, capable of connecting to BLE devices
acting as GATT servers. It is designed to provide a asynchronous,
cross-platform Python API to connect and communicate with e.g. sensors.

Features:
* Supports Windows 11, version 22000 and greater
* Supports Linux distributions with BlueZ >= 5.55
* OS X/macOS support via Core Bluetooth API, from at least OS X version 10.15
* Android backend compatible with python-for-android ...

Example:
```python
import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main())
```

Sections: Bleak, Features, Usage

</details>

### brotlicffi

Python CFFI bindings to the Brotli library

`pip install brotlicffi` · installs (wheel) · licence: MIT · rank 3145 · last release 2026-10-22 · [PyPI](https://pypi.org/project/brotlicffi/)

<details><summary>README extract</summary>

This library contains Python CFFI bindings for the reference Brotli encoder/decoder,
available here. This allows Python software to use the Brotli compression
algorithm directly from Python code.

Install from PyPI:

Install from Conda:

To use it simply, try this:

More information can be found in the documentation.

Example:
```python
import brotlicffi
data = brotlicffi.decompress(compressed_data)
```

Sections: BrotliCFFI, Using BrotliCFFI in Projects, 1.2.1.0 (2026-10-21), 1.2.0.2 (2026-08-21), 1.2.0.1 (2026-03-05), 1.2.0.0 (2025-11-21), 1.1.0.0 (2023-09-14), 1.0.9.2 (2021-04-06), 1.0.9.1 (2021-01-27), 1.0.9.0 (2021-01-20), 0.8.0 (2020-11-30), 0.7.0 (2017-05-30), 0.6.0 (2016-09-08), 0.5.1 (2016-08-17)

</details>

### braintrust-langchain

DEPRECATED: LangChain integration is now included in the main braintrust package. Install braintrust instead.

`pip install braintrust-langchain` · installs (wheel) · licence: MIT · rank 3278 · last release 2026-04-01 · [PyPI](https://pypi.org/project/braintrust-langchain/) · [source](https://github.com/braintrustdata/braintrust-sdk-python)

<details><summary>README extract</summary>

SDK for integrating Braintrust with LangChain. This package provides a callback handler to automatically log LangChain executions to Braintrust.

> This package is deprecated. The LangChain integration is now included in the main `braintrust` package.

1. Remove `braintrust-langchain` from your dependencies
2. Install or upgrade `braintrust`:
3. ...

Example:
```python
import asyncio
from braintrust import init_logger
from braintrust_langchain import BraintrustCallbackHandler, set_global_handler
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

async def main():
    # Initialize the logger with your project
    init_logger(project="your-project-name")

...
```

...

</details>

### better-profanity

Blazingly fast cleaning swear words (and their leetspeak) in strings

`pip install better-profanity` · installs (wheel) · licence: MIT License · rank 3298 · last release 2020-11-02 · [PyPI](https://pypi.org/project/better-profanity/)

<details><summary>README extract</summary>

*Blazingly fast cleaning swear words (and their leetspeak) in strings*

Inspired from package profanity of Ben Friedland, this library is significantly faster than the original one, by using string comparison instead of regex.

It supports modified spellings (such as `p0rn`, `h4NDjob`, `handj0b` and `b*tCh`). ...

Example:
```python
from better_profanity import profanity

if name == "main":
    profanity.load_censor_words()

    text = "You p1ec3 of sHit."
    censored_text = profanity.censor(text)
    print(censored_text)
    # You ** of **.
```

...

</details>

### binapy

Binary Data manipulation, for humans.

`pip install binapy` · installs (wheel) · licence: MIT License · rank 3314 · last release 2024-01-19 · [PyPI](https://pypi.org/project/binapy/)

<details><summary>README extract</summary>

BinaPy is a module that makes Binary Data manipulation simpler and easier than what is offered in the Python standard library.

With BinaPy, encoding or decoding data in a number of formats (base64, base64url, hex, url-encoding, etc.), compressing or decompressing (gzip), hashing (SHA1, SHA256, MD5, etc., with or without salt), is all a single ...

Features:
- Fluent interface, based on a `bytes` subclass
- Provides a convenient interface over `hashlib`, `base64`, `zlib`, `urllib.parse`, `json`, `pickle` and more
- Easy to extend with new formats

Example:
```python
from binapy import BinaPy

bp = BinaPy("Hello, World!").to("deflate").to("b64u")
print(bp)
# b'80jNycnXUQjPL8pJUQQA'
bp.decode_from("b64u").decode_from("deflate").ascii()
# "Hello, World!"
isinstance(bp, bytes)
# True
```

...

</details>

### boto3-type-annotations

Type annotations for boto3. Adds code completion in IDEs such as PyCharm.

`pip install boto3-type-annotations` · installs (wheel) · licence: MIT License · rank 3370 · last release 2019-05-02 · [PyPI](https://pypi.org/project/boto3-type-annotations/)

<details><summary>README extract</summary>

A programmatically created package that defines `boto3` services as stand in classes with type annotations. `boto3` is
an incredibly useful, well designed interface to the AWS API. However, we live in an age where even free IDEs like
PyCharm CE have full code completion (IntelliSense). ...

Example:
```python
import boto3
from boto3_type_annotations.s3 import Client, ServiceResource
from boto3_type_annotations.s3.waiter import BucketExists
from boto3_type_annotations.s3.paginator import ListObjectsV2

# With type annotations

client: Client = boto3.client('s3')
client.create_bucket(Bucket='foo')  # Not only does your IDE knows the name of this method,
...
```

...

</details>

### bm25s

An ultra-fast implementation of BM25 based on sparse matrices.

`pip install bm25s` · installs (wheel) · licence: MIT License · rank 3480 · last release 2026-10-28 · [PyPI](https://pypi.org/project/bm25s/)

<details><summary>README extract</summary>

BM25S (or BM25-Sparse) is an ultrafast implementation of BM25 in pure Python, powered by Numpy

 💻 GitHub

 🏠 Homepage

 📝 Technical Report

 🤗 Blog Post

 🛠️ Installation

Welcome to `bm25s`, a library that implements BM25 in Python, allowing you to rank documents based on a query. ...

Example:
```python
import bm25s
import Stemmer  # optional: for stemming

# Create your corpus here
corpus = [
    "a cat is a feline and likes to purr",
    "a dog is the human's best friend and loves to play",
    "a bird is a beautiful animal that can fly",
    "a fish is a creature that lives in water and swims",
]

# optional: create a stemmer
...
```

...

</details>

### brotlipy

Python binding to the Brotli library

`pip install brotlipy` · installs (wheel) · licence: MIT · rank 3502 · last release 2021-09-02 · [PyPI](https://pypi.org/project/brotlipy/)

<details><summary>README extract</summary>

This library contains Python bindings for the reference Brotli encoder/decoder,
available here. This allows Python software to use the Brotli compression
algorithm directly from Python code.

To use it simply, try this:

More information can be found in the documentation.

Example:
```python
import brotli
data = brotli.decompress(compressed_data)
```

Sections: brotlipy, 0.7.0 (2017-05-30), 0.6.0 (2016-09-08), 0.5.1 (2016-08-17), 0.5.0 (2016-08-16), 0.4.0 (2016-08-01), 0.3.0 (2016-05-11), 0.2.0 (2015-10-05), 0.1.3 (2015-10-05)

</details>

### backports.functools-lru-cache

Backport of functools.lru_cache

`pip install backports.functools-lru-cache` · installs (wheel) · licence: MIT License · rank 3533 · last release 2023-12-13 · [PyPI](https://pypi.org/project/backports.functools-lru-cache/)

<details><summary>README extract</summary>

Backport of functools.lru_cache from Python 3.3 as published at ActiveState.

Example:
```python
try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache
```

Sections: Usage, For Enterprise

</details>

### boto3-stubs-full

All-in-one type annotations for boto3 1.43.126 generated with mypy-boto3-builder 8.12.0

`pip install boto3-stubs-full` · installs (wheel) · licence: MIT · rank 3653 · last release 2026-11-07 · [PyPI](https://pypi.org/project/boto3-stubs-full/) · [docs](https://youtype.github.io/boto3_stubs_docs/) · [source](https://github.com/youtype/mypy_boto3_builder)

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
boto3-stubs page and in
boto3-stubs-full docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### bump2version

Version-bump your software with a single command!

`pip install bump2version` · installs (wheel) · licence: MIT License · rank 3719 · last release 2020-10-07 · [PyPI](https://pypi.org/project/bump2version/)

<details><summary>README extract</summary>

This is a maintained fork of the excellent bumpversion project.

Features:
Version-bump your software with a single command!

A small command line tool to simplify releasing software by updating all
version strings in your source code by the correct increment. Also creates
commits and tags: ...

Sections: bump2version, NOTE, Overview, Alternatives, Usage, `part`, `file`, Configuration file, Configuration file -- Global configuration, `current_version`, `new_version`, `tag = (True | False)`, `sign_tags = (True | False)`, `tag_name =`

</details>

### boostedblob

Command line tool and async library to perform basic file operations on local paths, Google Cloud Storage paths and Azure Blob Storage paths.

`pip install boostedblob` · installs (wheel) · licence: MIT · rank 3843 · last release 2026-07-30 · [PyPI](https://pypi.org/project/boostedblob/)

<details><summary>README extract</summary>

boostedblob is a command line tool and async library to perform basic file operations on local
paths, Google Cloud Storage paths and Azure Blob Storage paths.

boostedblob is derived from the excellent blobfile. ...

Sections: boostedblob, Usage

</details>

### build123d

A python CAD programming library

`pip install build123d` · installs (wheel) · licence: Apache Software License · rank 3861 · last release 2026-09-21 · [PyPI](https://pypi.org/project/build123d/) · [docs](https://build123d.readthedocs.io/en/latest/index.html)

<details><summary>README extract</summary>

Documentation |
Cheat Sheet |
Discord |
Discussions |
Issues |
Contributing

build123d is a Python-based, parametric boundary representation (BREP) modeling framework for 2D and 3D CAD. ...

Features:
Designed for modern, maintainable CAD-as-code, build123d combines clear architecture with expressive, algebraic modeling. It offers:
- Minimal or no internal state depending on mode, ...

Example:
```python
from build123d import *
```

Sections: Features, Usage, Constructing a 1D Shape, Upgrading to 2D and 3D, Adding to and modifying part, Builder Mode, Extending objects, Data interchange, Further reading, Viewers, Attribution

</details>

### bce-python-sdk

BCE SDK for python

`pip install bce-python-sdk` · installs (wheel) · licence: Apache License 2.0 · rank 3919 · last release 2026-09-01 · [PyPI](https://pypi.org/project/bce-python-sdk/)

### buildkite-sdk

Automatically generated by Nx.

`pip install buildkite-sdk` · installs (wheel) · licence: not stated · rank 3965 · last release 2026-07-23 · [PyPI](https://pypi.org/project/buildkite-sdk/)

<details><summary>README extract</summary>

A Python SDK for Buildkite! 🪁

Example:
```python
from buildkite_sdk import Pipeline

pipeline = Pipeline()
pipeline.add_step({"command": "echo 'Hello, world!'"})

print(pipeline.to_json())
print(pipeline.to_yaml())
```

Sections: buildkite-sdk, Usage

</details>

### bgutil-ytdlp-pot-provider

(no summary)

`pip install bgutil-ytdlp-pot-provider` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 4148 · last release 2026-10-07 · [PyPI](https://pypi.org/project/bgutil-ytdlp-pot-provider/)

_README extract left out: share-alike licence._

### bson

BSON codec for Python

`pip install bson` · installs from source (sdist only) · licence: BSD · rank 4194 · last release 2020-05-26 · [PyPI](https://pypi.org/project/bson/)

<details><summary>README extract</summary>

Independent BSON codec for Python that doesn't depend on MongoDB.

</details>

### bayesian-optimization

Bayesian Optimization package

`pip install bayesian-optimization` · installs (wheel) · licence: MIT License · rank 4290 · last release 2026-10-02 · [PyPI](https://pypi.org/project/bayesian-optimization/) · [docs](https://bayesian-optimization.github.io/BayesianOptimization) · [source](https://github.com/bayesian-optimization/BayesianOptimization)

<details><summary>README extract</summary>

Pure Python implementation of bayesian global optimization with gaussian
processes.

This is a constrained global optimization package built upon bayesian inference
and gaussian processes, that attempts to find the maximum value of an unknown
function in as few iterations as possible. ...

Example:
```python
from bayes_opt import BayesianOptimization

# Bounded region of parameter space
pbounds = {'x': (2, 4), 'y': (-3, 3)}

optimizer = BayesianOptimization(
    f=black_box_function,
    pbounds=pbounds,
    random_state=1,
)
```

Sections: Bayesian Optimization, How does it work?, Basic tour of the Bayesian Optimization package, 1. Specifying the function to be optimized, 2. Getting Started, Minutiae

</details>

### brotli-asgi

A compression AGSI middleware using brotli

`pip install brotli-asgi` · installs (wheel) · licence: MIT · rank 4444 · last release 2026-10-27 · [PyPI](https://pypi.org/project/brotli-asgi/)

<details><summary>README extract</summary>

A compression AGSI middleware using brotli.

Built using starlette under the hood, it can be used as a drop-in replacement to
GZipMiddleware for Starlette or FastAPI.

</details>

### buildkite-test-collector

Buildkite Test Engine collector

`pip install buildkite-test-collector` · installs (wheel) · licence: MIT · rank 4619 · last release 2026-10-21 · [PyPI](https://pypi.org/project/buildkite-test-collector/)

<details><summary>README extract</summary>

The official Python adapter for Buildkite Test Engine which collects information about your tests.

Supported Python versions: >=3.10

⚒ Supported test frameworks: pytest.

📦 Supported CI systems: Buildkite, GitHub Actions, CircleCI, and others via the `BUILDKITE_ANALYTICS*` environment variables.

Example:
```python
import pytest

@pytest.mark.execution_tag("color", "red")
def test_red_feature():
    assert True

@pytest.mark.execution_tag("color", "blue")
def test_blue_feature():
    assert True
```

Sections: Buildkite Test Collector for Python, 🏷️ Filtering Tests by Tags, 🔁 Running batches with `bktec pool exec`, 🎢 Tracing, 🔜 Roadmap, 🚀 Releasing, 🤙 Thanks

</details>

### boto3-stubs-lite

Lite type annotations for boto3 1.43.126 generated with mypy-boto3-builder 8.12.0

`pip install boto3-stubs-lite` · installs (wheel) · licence: MIT · rank 4892 · last release 2026-11-06 · [PyPI](https://pypi.org/project/boto3-stubs-lite/) · [docs](https://youtype.github.io/boto3_stubs_docs/) · [source](https://github.com/youtype/mypy_boto3_builder)

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
boto3-stubs page and in
boto3-stubs-lite docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### boto_session_manager

A boto3 session manager: cached clients, typed client properties for 400+ AWS services, assume role with auto-refresh, and AWS CLI credential handoff.

`pip install boto_session_manager` · installs (wheel) · licence: Apache-2.0 · rank 4913 · last release 2026-10-18 · [PyPI](https://pypi.org/project/boto_session_manager/) · [docs](https://boto-session-manager.readthedocs.io/en/latest/) · [source](https://github.com/MacHu-GWU/boto_session_manager-project)

<details><summary>README extract</summary>

`boto_session_manager` is a light weight, zero dependency python library that simplify managing your AWS boto3 session in your application code. It bring auto complete and type hint to the default `boto3` SDK, and provide smooth development experience with the following goodies: ...

Example:
```python
from boto_session_manager.api import BotoSesManager

# 1. Use default credential chain (env vars, ~/.aws/credentials, instance profile, etc.)
bsm = BotoSesManager()

# 2. Use a named AWS profile from ~/.aws/credentials or ~/.aws/config
bsm = BotoSesManager(profile_name="my_aws_profile")

...
```

...

</details>

### betterproto2

A better Protobuf / gRPC generator & library

`pip install betterproto2` · installs (wheel) · licence: MIT · rank 4992 · last release 2026-05-10 · [PyPI](https://pypi.org/project/betterproto2/) · [docs](https://betterproto.github.io/python-betterproto2/) · [source](https://github.com/betterproto/python-betterproto2)

### bigquery-schema-generator

BigQuery schema generator from JSON or CSV data

`pip install bigquery-schema-generator` · installs from source (sdist only) · licence: Apache 2.0 · rank 5050 · last release 2024-01-13 · [PyPI](https://pypi.org/project/bigquery-schema-generator/)

<details><summary>README extract</summary>

This script generates the BigQuery schema from the newline-delimited data
records on the STDIN. The records can be in JSON format or CSV format. The
BigQuery data importer (`bq load`) uses only the
first 500 records
when the schema auto-detection feature is enabled. In contrast, this script uses
all data records to generate the schema.

Usage: ...

Example:
```python
from bigquery_schema_generator.generate_schema import SchemaGenerator

generator = SchemaGenerator(
    input_format=input_format,
    infer_mode=infer_mode,
    keep_nulls=keep_nulls,
    quoted_values_are_strings=quoted_values_are_strings,
    debugging_interval=debugging_interval,
    debugging_map=debugging_map,
...
```

...

</details>

### blingfire

Python wrapper of lightning fast Finite State Machine based NLP library.

`pip install blingfire` · installs (wheel) · licence: MIT License · rank 5092 · last release 2021-09-24 · [PyPI](https://pypi.org/project/blingfire/)

<details><summary>README extract</summary>

Hi, we are a team at Microsoft called Bling (Beyond Language Understanding), we help Bing be smarter. Here we wanted to share with all of you our FInite State machine and REgular expression manipulation library (FIRE). ...

Example:
```python
from blingfire import *

text = 'After reading this post, you will know: What "natural language" is and how it is different from other types of data. What makes working with natural language so challenging. [1]'

print(text_to_sentences(text))
print(text_to_words(text))
```

Sections: Bling Fire, Introduction, Bling Fire Tokenizer Overview, Python API Description, Examples, 1. Python example, using default pattern-based tokenizer, 3. Python example, calling BERT BASE tokenizer, Working Branch, Pull Request, Feedback

</details>

### bingads

A library to make working with the Bing Ads APIs and bulk services easy

`pip install bingads` · installs from source (sdist only) · licence: MIT License · rank 5109 · last release 2026-10-14 · [PyPI](https://pypi.org/project/bingads/)

<details><summary>README extract</summary>

.. image:: :target:

The Bing Ads Python Software Development Kit (SDK) Version 13.0 enhances the experience of developing Bing Ads applications
with the Python programming language.
The SDK includes proxy classes for all Bing Ads API web services and abstracts the low level details of authentication with OAuth. ...

Sections: Bing Ads Python SDK, Getting Started, External Dependencies

</details>

### bumpversion

Version-bump your software with a single command!

`pip install bumpversion` · installs (wheel) · licence: MIT License · rank 5177 · last release 2020-05-14 · [PyPI](https://pypi.org/project/bumpversion/)

<details><summary>README extract</summary>

⚠️ Current status of this project

* 🎬If you want to start using bumpversion, you're best advised to install one of the maintained forks, e.g. ➡ @c4urself's bump2version.
* 🔨If you want to help maintain bumpversion, there's an ongoing discussion about merging the fork back to the original project as well as forming a group of maintainers to ensure ...

Sections: bumpversion, Screencast, Usage, Configuration, Global configuration, Part specific configuration, File specific configuration, Options, Using bumpversion in a script, Changes

</details>

### binary

(no summary)

`pip install binary` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 5266 · last release 2025-06-11 · [PyPI](https://pypi.org/project/binary/)

<details><summary>README extract</summary>

`binary` provides a bug-free and easy way to convert between and within
binary (IEC) and decimal (SI) units.

Example:
```python
>>> from binary import BinaryUnits, DecimalUnits, convert_units
```

Sections: binary, Examples, Usage, Types, 1.0.2, 1.0.1, 1.0.0

</details>

### bloom-filter2

Pure Python Bloom Filter module

`pip install bloom-filter2` · installs (wheel) · licence: MIT · rank 5317 · last release 2021-05-05 · [PyPI](https://pypi.org/project/bloom-filter2/)

<details><summary>README extract</summary>

A pure python bloom filter (low storage requirement, probabilistic
set datastructure) is provided. It is known to work on CPython 3.x, Pypy,
and Jython.

Includes mmap, in-memory and disk-seek backends.

This project builds on `drs-bloom-filter` and `bloom_filter_mod`.
Credits and links can be found in AUTHORS.md.

Example:
```python
from bloom_filter2 import BloomFilter

# instantiate BloomFilter with custom settings,
# max_elements is how many elements you expect the filter to hold.
# error_rate defines accuracy; You can use defaults with
# `BloomFilter()` without any arguments. Following example
# is same as defaults:
bloom = BloomFilter(max_elements=10000, error_rate=0.1)

...
```

Sections: bloom-filter, Usage

</details>

### bincopy

Mangling of various file formats that conveys binary information (Motorola S-Record, Intel HEX and binary files).

`pip install bincopy` · installs (wheel) · licence: MIT License · rank 5346 · last release 2026-02-24 · [PyPI](https://pypi.org/project/bincopy/)

<details><summary>README extract</summary>

Mangling of various file formats that conveys binary information
(Motorola S-Record, Intel HEX, TI-TXT, Verilog VMEM, ELF and binary
files).

Project homepage:

Documentation:

Example:
```python
>>> import bincopy
>>> f = bincopy.BinFile("tests/files/in.hex")
>>> print(f.as_ihex())
:20010000214601360121470136007EFE09D219012146017E17C20001FF5F16002148011979
:20012000194E79234623965778239EDA3F01B2CA3F0156702B5E712B722B7321460134219F
:00000001FF

>>> print(f.as_srec())
...
```

Sections: About, Example usage, Scripting, Command line tool, The info subcommand, The convert subcommand, The pretty subcommand, The fill subcommand, . Fork the repository., . Implement the new feature or bug fix., . Run the tests., . Create a pull request., Similar projects

</details>

### bfi

A fast optimizing Brainfuck interpreter in pure python

`pip install bfi` · installs (wheel) · licence: MIT License · rank 5360 · last release 2025-11-08 · [PyPI](https://pypi.org/project/bfi/)

<details><summary>README extract</summary>

This is a pure python interpreter for the
Brainfuck esoteric programming
language. `bfi` is quite fast without requiring any special python implementations
or compiled extension modules. `bfi` Supports Python 2x and 3x. ...

Example:
```python
>>> import bfi
>>> with open('samples/hello_world.b', 'r') as fh:
...     brainfuck_code = fh.read()
...
>>> Brainfuck.interpret(brainfuck_code)

Hello World!
```

Sections: Fast Brainfuck interpreter in pure python, Speed benchmark, Implementation details, Using the interpreter from the command-line, Using the interpreter in your own code, Reference, Gratuitous unnecessary extras, Example Brainfuck programs

</details>

### beniget

Extract semantic information about static Python code

`pip install beniget` · installs (wheel) · licence: BSD License · rank 5614 · last release 2025-11-29 · [PyPI](https://pypi.org/project/beniget/)

<details><summary>README extract</summary>

A static analyzer for Python code.

Beniget provides a static over-approximation of the global and
local definitions inside Python Module/Class/Function.
It can also compute def-use chains from each definition.

</details>

### baml-py

BAML v0 — Python runtime for baml_client

`pip install baml-py` · installs (wheel) · licence: not stated · rank 5665 · last release 2026-10-28 · [PyPI](https://pypi.org/project/baml-py/) · [docs](https://docs.boundaryml.com) · [source](https://github.com/BoundaryML/baml)

### brainstem

Acroname BrainStem Software Control Package

`pip install brainstem` · installs (wheel) · licence: Other/Proprietary License · rank 5741 · last release 2026-11-03 · [PyPI](https://pypi.org/project/brainstem/)

<details><summary>README extract</summary>

The BrainStem python package gives access to simple python commands
to control and interact with a collection of BrainStem devices

Features:
- Easily interact with BrainStem devices using python
- Learn more about the capabilities of BrainStem devices in Acroname's reference documentation

Example:
```python
>>>  import brainstem
```

Sections: BrainStem Python Library, Features, Download, Troubleshooting, A Tour of the Python Example, Working with BrainStem from the Interpreter, Additional Requirements, python, pip, libffi, CentOS package manager

</details>

### brickflows

Deploy scalable workflows to databricks using python

`pip install brickflows` · does not install on CPython 3.14 · licence: Apache Software License · rank 5835 · last release 2026-08-07 · [PyPI](https://pypi.org/project/brickflows/) · [source](https://github.com/Nike-Inc/brickflow)

<details><summary>README extract</summary>

BrickFlow is specifically designed to enable the development of Databricks workflows using Python, streamlining the
process through a command-line interface (CLI) tool.

Example:
```python
from brickflow import (
    ctx,
    Cluster,
    Workflow,
    NotebookTask,
)
from airflow.operators.bash import BashOperator

cluster = Cluster(
    name="job_cluster",
    node_type_id="m6gd.xlarge",
    spark_version="13.3.x-scala2.12",
    min_workers=1,
    max_workers=2,
)

wf = Workflow(
    "hello_world_workflow",
...
```

Sections: Brickflow, Documentation, Getting Started, Prerequisites, Hello World workflow, Deploy the workflow to databricks, Run the demo workflow, Examples

</details>

### basic-pitch

Basic Pitch, a lightweight yet powerful audio-to-MIDI converter with pitch bend detection.

`pip install basic-pitch` · installs (wheel) · licence: not stated · rank 5950 · last release 2024-08-16 · [PyPI](https://pypi.org/project/basic-pitch/)

<details><summary>README extract</summary>

Basic Pitch is a Python library for Automatic Music Transcription (AMT), using lightweight neural network developed by Spotify's Audio Intelligence Lab. It's small, easy-to-use, `pip install`-able and `npm install`-able via its sibling repo. ...

Example:
```python
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH

model_output, midi_data, note_events = predict(<input-audio-path>)
```

Sections: Research Paper, Demo, Compatible Environments, Model Runtime, Usage, Model Prediction, Command Line Tool, Programmatic, Model Input, VST

</details>

### better-exceptions

Pretty and helpful exceptions, automatically

`pip install better-exceptions` · installs (wheel) · licence: not stated · rank 6111 · last release 2021-01-29 · [PyPI](https://pypi.org/project/better-exceptions/)

### bigtree

Tree Implementation and Methods for Python, integrated with list, dictionary, pandas and polars DataFrame.

`pip install bigtree` · installs (wheel) · licence: MIT · rank 6114 · last release 2026-07-16 · [PyPI](https://pypi.org/project/bigtree/) · [docs](https://bigtree.readthedocs.io) · [source](https://github.com/kayjan/bigtree)

<details><summary>README extract</summary>

Tree Implementation and Methods for Python, integrated with list, dictionary, pandas and polars DataFrame.

It is pythonic, making it easy to learn and extendable to many types of workflows.

Related Links:
- Documentation
- GitHub
- Community
 - Issues
 / Discussions
 / Changelog
 / Contributing
- Package
 - PyPI
 / Conda ...

Sections: Big Tree Python Package, Components

</details>

### backports_abc

A backport of recent additions to the 'collections.abc' module.

`pip install backports_abc` · installs (wheel) · licence: Python Software Foundation License · rank 6157 · last release 2016-11-12 · [PyPI](https://pypi.org/project/backports_abc/)

<details><summary>README extract</summary>

Usage:

You can also install the ABCs into the stdlib by calling the `patch()`
function:

Currently, `patch()` provides the following names if missing:

* `collections.abc.Generator`
* `collections.abc.Awaitable`
* `collections.abc.Coroutine`
* `inspect.isawaitable(obj)` ...

Example:
```python
try:
    # ABCs live in "collections.abc" in Python >= 3.3
    from collections.abc import Coroutine, Generator
except ImportError:
    # fall back to import from "backports_abc"
    from backports_abc import Coroutine, Generator
```

Sections: ABC-Backports, 0.5 (2016-11-12), 0.4 (2015-09-14), 0.3 (2015-07-03), 0.2 (2015-07-03), 0.1 (2015-06-24)

</details>

### blackduck

Package for using the Synopsys Black Duck Hub REST API.

`pip install blackduck` · installs (wheel) · licence: Apache Software License · rank 6241 · last release 2024-04-19 · [PyPI](https://pypi.org/project/blackduck/)

<details><summary>README extract</summary>

Features:
The hub-rest-api-python provides Python bindings for Hub REST API.

Example:
```python
from blackduck import Client
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(module)s:%(lineno)d} %(levelname)s - %(message)s"
)

bd = Client(
    token=os.environ.get('blackduck_token'),
    base_url="
    # verify=False  # TLS certificate verification
)

...
```

Sections: Overview, Paging and Black Duck v2022.2, New in 1.0.0, Important Notes, To use, Examples, v1.1.0, Test, Documentation

</details>

### baseten-performance-client

A ultra-high performance package for sending requests to Baseten Embedding Inference'

`pip install baseten-performance-client` · installs (wheel) · licence: not stated · rank 6281 · last release 2026-10-14 · [PyPI](https://pypi.org/project/baseten-performance-client/) · [source](https://github.com/basetenlabs/truss.git)

<details><summary>README extract</summary>

This library provides a high-performance Python client for Baseten.co endpoints including embeddings, reranking, and classification. It was built for massive concurrent post requests to any URL, also outside of baseten.co. PerformanceClient releases the GIL while performing requests in the Rust, and supports simultaneous sync and async usage. ...

Example:
```python
import os
import asyncio
from baseten_performance_client import PerformanceClient, OpenAIEmbeddingsResponse, RerankResponse, ClassificationResponse

api_key = os.environ.get("BASETEN_API_KEY")
base_url_embed = "
# Also works with OpenAI or Mixedbread.
# base_url_embed = " or "

# Basic client setup
...
```

...

</details>

### bpython

A fancy curses interface to the Python interactive interpreter

`pip install bpython` · installs (wheel) · licence: MIT · rank 6324 · last release 2025-10-28 · [PyPI](https://pypi.org/project/bpython/) · [docs](https://docs.bpython-interpreter.org) · [source](https://github.com/bpython/bpython)

<details><summary>README extract</summary>

bpython is a lightweight Python interpreter that adds several features common
to IDEs. These features include syntax highlighting, **expected parameter
list, auto-indentation, and autocompletion**. (See below for example
usage). ...

Features:
* Readline-like autocomplete, with suggestions displayed as you type.

* In-line syntax highlighting. This uses Pygments for lexing the code as you
 type, and colours appropriately.

* Expected parameter list. ...

Sections: Features & Examples, Configuration, Dependencies, bpython-urwid, Ubuntu/Debian, Arch Linux, Fedora, GNU Guix, macOS, Known Bugs

</details>

### backports.shutil_get_terminal_size

A backport of the get_terminal_size function from Python 3.3's shutil.

`pip install backports.shutil_get_terminal_size` · installs (wheel) · licence: MIT License · rank 6359 · last release 2014-08-19 · [PyPI](https://pypi.org/project/backports.shutil_get_terminal_size/)

<details><summary>README extract</summary>

A backport of the get_terminal_size function from Python 3.3's shutil.

Unlike the original version it is written in pure Python rather than C,
so it might be a tiny bit slower.

Example:
```python
>>> from backports.shutil_get_terminal_size import get_terminal_size
>>> get_terminal_size()
terminal_size(columns=105, lines=33)
```

Sections: backports.shutil_get_terminal_size, Example usage, 1.0.0 (2014-08-19)

</details>

### bpylist2

Parse and generate NSKeyedArchiver archives

`pip install bpylist2` · installs (wheel) · licence: MIT License · rank 6398 · last release 2023-09-11 · [PyPI](https://pypi.org/project/bpylist2/)

<details><summary>README extract</summary>

This is a fork of Marketcircle/bpylist. This one is hopefully more responsive to PRs.

Implementation of the Apple's Binary
Plist
and the NSKeyedArchiver format

Example:
```python
from bpylist2 import archiver

with open('my_archived_object', 'rb') as f:
    archiver.unarchive(f.read())
```

Sections: bpylist2, Usage, Binary Plists, KeyedArchives, Custom objects, Implementation Note, How to publish a new version to PyPI

</details>

### bech32

Reference implementation for Bech32 and segwit addresses.

`pip install bech32` · installs (wheel) · licence: MIT License · rank 6399 · last release 2020-02-17 · [PyPI](https://pypi.org/project/bech32/)

<details><summary>README extract</summary>

Since this implementation wasn't in a place that was easy to use for Python programmers I took it from from and published on GitHub and on PyPI.

The original version of this package is probably the one at but apparently Rusty Russel commented out the 90-length limit of bech32-encoded stuff so it could be used for Lightning invoices. ...

</details>

### banal

Commons of banal micro-functions for Python.

`pip install banal` · installs (wheel) · licence: MIT License · rank 6455 · last release 2026-04-14 · [PyPI](https://pypi.org/project/banal/)

<details><summary>README extract</summary>

Commons of Python micro-functions. This basically an out-sourced, shared
utils module with a focus on functions that buffer type uncertainties in
Python (e.g. "is this a list?").

Rules:

* Functions are properly typed, library passes `mypy`.
* Cannot depend on anything but the standard library ...

Sections: banal, Functions

</details>

### boa-str

Convert strings to snakecase

`pip install boa-str` · installs (wheel) · licence: MIT License · rank 6485 · last release 2017-07-10 · [PyPI](https://pypi.org/project/boa-str/)

<details><summary>README extract</summary>

Boa is a Python package for normalizing and converting strings to snakecase.

For example, it translates the user-defined event `'User Buys Item'` to `'user_buys_item'` which can then be used in a file path in S3, or as the name of a schema or table in Redshift. ...

Example:
```python
>>> import boa
>>> my_str = 'Hello Boa'
>>> boa.constrict(my_str)
'hello_boa'
```

Sections: Boa, Quickstart, Examples, Tests, Style

</details>

### backports.entry-points-selectable

Compatibility shim providing selectable entry points for older implementations

`pip install backports.entry-points-selectable` · installs (wheel) · licence: MIT License · rank 6558 · last release 2023-11-27 · [PyPI](https://pypi.org/project/backports.entry-points-selectable/)

<details><summary>README extract</summary>

Compatibility shim to ease adoption of importlib_metadata 3.6. Supplies forward-compatibility of "selectable" entry points even on older versions of `importlib_metadata` and `importlib.metadata`, and avoids usage that triggers deprecation warnings. ...

Example:
```python
from backports.entry_points_selectable import entry_points
```

</details>

### bpyutils

A collection of various common Python utilities.

`pip install bpyutils` · installs (wheel) · licence: MIT License · rank 6769 · last release 2022-09-14 · [PyPI](https://pypi.org/project/bpyutils/)

<details><summary>README extract</summary>

Features:
* Python 2.7+ and Python 3.4+ compatible.

Example:
```python
>>> import bpyutils
```

Sections: bpyutils, A collection of various common Python utilities., Features, Quick Start, Usage, Application Interface, Command-Line Interface

</details>

### blaxel

Blaxel - AI development platform SDK

`pip install blaxel` · installs (wheel) · licence: not stated · rank 6866 · last release 2026-11-06 · [PyPI](https://pypi.org/project/blaxel/) · [docs](https://docs.blaxel.ai) · [source](https://github.com/blaxel-ai/sdk-python)

<details><summary>README extract</summary>

Blaxel is a perpetual sandbox platform that achieves near instant latency by keeping infinite secure sandboxes on automatic standby, while co-hosting your agent logic to cut network overhead.

This repository contains Blaxel's Python SDK, which lets you create and manage sandboxes and other resources on Blaxel.

Example:
```python
from blaxel.core import SandboxInstance

page = await SandboxInstance.list(limit=50)

for sandbox in page.data:
    print(sandbox.metadata.name)

if page.has_more:
    next_page = await page.next_page()
    print(next_page.next_cursor)
```

Sections: Blaxel Python SDK, Authentication, Usage, Paginated list responses, Sandboxes, Preview URLs, Process execution, Filesystem operations, Drives, Volumes, Error handling, Batch jobs, Framework integrations, Model use

</details>

### bounded-pool-executor

Bounded Process&Thread Pool Executor

`pip install bounded-pool-executor` · installs (wheel) · licence: MIT License · rank 7069 · last release 2019-06-04 · [PyPI](https://pypi.org/project/bounded-pool-executor/)

<details><summary>README extract</summary>

BoundedSemaphore for ProcessPoolExecutor & ThreadPoolExecutor from concurrent.futures

Example:
```python
from bounded_pool_executor import BoundedProcessPoolExecutor
from time import sleep
from random import randint

def do_job(num):
    sleep_sec = randint(1, 10)
    print('value: %d, sleep: %d sec.' % (num, sleep_sec))
    sleep(sleep_sec)

with BoundedProcessPoolExecutor(max_workers=5) as worker:
    for num in range(10000):
...
```

Sections: Bounded Process&Thread Pool Executor, What is the main problem?, BoundedProcessPoolExecutor VS ProcessPoolExecutor, BoundedProcessPoolExecutor, Result, Classic concurrent.futures.ProcessPoolExecutor

</details>

### browserstack-local

Python bindings for Browserstack Local

`pip install browserstack-local` · installs (wheel) · licence: not stated · rank 7243 · last release 2026-08-07 · [PyPI](https://pypi.org/project/browserstack-local/)

<details><summary>README extract</summary>

Python bindings for BrowserStack Local.

Example:
```python
from browserstack.local import Local

# creates an instance of Local
bs_local = Local()

# replace <browserstack-accesskey> with your key. You can also set an environment variable - "BROWSERSTACK_ACCESS_KEY".
bs_local_args = { "key": "<browserstack-accesskey>" }

# starts the Local instance with the required arguments
...
```

Sections: browserstack-local-python, Example, Arguments, Verbose Logging, Force Start, Only Automate, Force Local, Proxy, Local Proxy, PAC (Proxy Auto-Configuration), Local Identifier, Additional Arguments, Binary Path, Logfile

</details>

### binpacking

Heuristic distribution of weighted items to bins (either a fixed number of bins or a fixed number of volume per bin). Data may be in form of list, dictionary, list of tuples or csv-file.

`pip install binpacking` · installs (wheel) · licence: MIT License · rank 7468 · last release 2026-01-22 · [PyPI](https://pypi.org/project/binpacking/) · [source](https://www.github.com/benmaier/binpacking)

<details><summary>README extract</summary>

This package contains greedy algorithms to solve two typical bin packing
problems:

1. Constant bin number: Distribute items into exactly *N* bins with
 approximately equal total weight per bin.
2. Constant volume: Distribute items into the minimum number of
 bins, each with a maximum capacity *V*.

- Python 3.10+ ...

Example:
```python
import binpacking

# Distribute items to 4 bins with balanced weights
b = {'a': 10, 'b': 10, 'c': 11, 'd': 1, 'e': 2, 'f': 7}
bins = binpacking.to_constant_bin_number(b, 4)
print(bins)
# [{'c': 11}, {'b': 10}, {'a': 10}, {'f': 7, 'e': 2, 'd': 1}]

# Distribute items to bins with max volume 11
values = [10, 10, 11, 1, 2, 7]
...
```

...

</details>

### basicsr

Open Source Image and Video Super-Resolution Toolbox

`pip install basicsr` · installs from source (sdist only) · licence: Apache Software License · rank 7486 · last release 2022-08-30 · [PyPI](https://pypi.org/project/basicsr/)

<details><summary>README extract</summary>

⚡HowTo | 🔧Installation | 💻Training Commands | 🐢DatasetPrepare | 🏰Model Zoo

📕中文解读文档 | 📊 Plot scripts | 📝Introduction | | ⏳TODO List | ❓FAQ

🚀 We add BasicSR-Examples, which provides guidance and templates of using BasicSR as a python package. 🚀

📢 技术交流QQ群：320960100   入群答案：互帮互助共同进步

🧭 入群二维码 (QQ、微信)    入群指南 (腾讯文档) ...

Sections: English | 简体中文, ⚡ HOWTOs, ✨ Projects that use BasicSR, 📧 Contact

</details>

### betacal

Beta calibration

`pip install betacal` · installs (wheel) · licence: MIT · rank 7503 · last release 2021-04-01 · [PyPI](https://pypi.org/project/betacal/)

<details><summary>README extract</summary>

This package provides a BetaCalibration class which allows the user to fit any of our three proposed beta calibration models. For the paper and tutorials, check

* [Numpy] - NumPy is the fundamental package for scientific computing with
 Python.
* [Scikit-learn] - Machine Learning in Python.

Sections: Beta calibration - Python package, Dependencies, Usage, Unittest

</details>

### bpemb

Byte-pair embeddings in 275 languages

`pip install bpemb` · installs (wheel) · licence: MIT License · rank 7619 · last release 2024-10-01 · [PyPI](https://pypi.org/project/bpemb/)

<details><summary>README extract</summary>

BPEmb is a collection of pre-trained subword embeddings in 275 languages, based on Byte-Pair Encoding (BPE) and trained on Wikipedia. Its intended use is as input for neural models in natural language processing.

Website ・
Usage ・
Download ・
MultiBPEmb ・
Paper (pdf) ・
Citing BPEmb

Example:
```python
>>> from bpemb import BPEmb
# load English BPEmb model with default vocabulary size (10k) and 50-dimensional embeddings
>>> bpemb_en = BPEmb(lang="en", dim=50)
downloading
downloading
```

Sections: BPEmb, Usage, Downloads for each language, MultiBPEmb, Citing BPEmb

</details>

### blender-mcp

Renamed to mcp-for-blender. Installing this package installs it for you.

`pip install blender-mcp` · installs (wheel) · licence: MIT · rank 7707 · last release 2026-09-16 · [PyPI](https://pypi.org/project/blender-mcp/)

<details><summary>README extract</summary>

This project has been renamed. `blender-mcp` is now a compatibility wrapper that
installs `mcp-for-blender` for you.

Nothing you have today breaks. There is no config change required.

Keep going. `uvx blender-mcp` continues to work exactly as before — this package
depends on `mcp-for-blender` and hands off to it at startup. ...

Features:
The new name is clearer about what this is: an MCP server for Blender. The code,
the Blender addon, and the import path (`blender_mcp`) are all unchanged.

Source, issues, and documentation:

Sections: blender-mcp is now mcp-for-blender, If you already use it, When convenient, Why the rename?

</details>

### bddl

(no summary)

`pip install bddl` · installs from source (sdist only) · licence: not stated · rank 8221 · last release 2025-06-23 · [PyPI](https://pypi.org/project/bddl/)

<details><summary>README extract</summary>

Note: If you are interested in the BEHAVIOR-100 version of BDDL, please go to the tags menu and navigate to the latest 1.x.x version.

The Behavior Domain Definition Language (BDDL) is a domain-specific language designed for the Benchmark for Everyday Household Activities in Virtual, Interactive, and ecOlogical enviRonments (BEHAVIOR). ...

Example:
```python
from bddl.activity import Conditions

behavior_activity = "storing_the_groceries"     # the activity you want to try, full list in bddl/bddl/activity_definitions
activity_definition = 0                         # the specific definition you want to use. As of BEHAVIOR100 2021, this should always be 0.
...
```

...

</details>

### beancount

Command-line Double-Entry Accounting

`pip install beancount` · installs (wheel) · licence: GPL-2.0-only · rank 8360 · last release 2026-05-05 · [PyPI](https://pypi.org/project/beancount/) · [docs](https://beancount.github.io/docs/) · [source](https://github.com/beancount/beancount)

_README extract left out: share-alike licence._

### bqplot

Interactive plotting for the Jupyter notebook, using d3.js and ipywidgets.

`pip install bqplot` · installs (wheel) · licence: Apache-2.0 · rank 8406 · last release 2026-05-07 · [PyPI](https://pypi.org/project/bqplot/)

<details><summary>README extract</summary>

2-D plotting library for Project Jupyter

`bqplot` is a 2-D visualization system for Jupyter, based on the constructs of
the *Grammar of Graphics*.

In `bqplot`, every component of a plot is an interactive widget. ...

Sections: bqplot, Introduction, Documentation, Trying it online, Dependencies, Examples, Using the `pyplot` API, Using the `Object Model` API

</details>

### bip-utils

Generation of mnemonics, seeds, private/public keys and addresses for different types of cryptocurrencies

`pip install bip-utils` · installs (wheel) · licence: MIT · rank 8444 · last release 2026-10-26 · [PyPI](https://pypi.org/project/bip-utils/) · [docs](https://bip-utils.readthedocs.io) · [source](https://github.com/ebellocchia/bip_utils)

<details><summary>README extract</summary>

| |

| |
| |
| |
| |

This package allows generating mnemonics, seeds, private/public keys and addresses for different types of cryptocurrencies. In particular:
- Mnemonic and seed generation as defined by BIP-0039
- Private key encryption/decryption as defined by BIP-0038

 - BIP-0032
 - SLIP-0010
 - BIP32-Ed25519 (Khovratovich/Law) ...

Sections: BIP Utility Library, Introduction, Alternative secp256k1 library, Test and Coverage, Modules description, Documentation, Code examples, Buy me a coffee

</details>

### bilibili-api-python

The fork of module bilibili-api. 哔哩哔哩的各种 API 调用便捷整合（视频、动态、直播等），另外附加一些常用的功能。

`pip install bilibili-api-python` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 8551 · last release 2026-06-19 · [PyPI](https://pypi.org/project/bilibili-api-python/) · [docs](https://nemo2011.github.io/bilibili-api) · [source](https://github.com/Nemo2011/bilibili-api)

_README extract left out: share-alike licence._

### bittensor

A lean Python SDK (import bittensor) and CLI (btcli) for the Bittensor chain.

`pip install bittensor` · installs (wheel) · licence: Apache-2.0 · rank 8601 · last release 2026-11-06 · [PyPI](https://pypi.org/project/bittensor/) · [docs](https://bittensor.com/docs) · [source](https://github.com/RaoFoundation/subtensor)

<details><summary>README extract</summary>

title: "Bittensor Python SDK and CLI"
description: "Install and use the Bittensor SDK and command line for wallets, transactions, and chain data."

A lean Python SDK and CLI for the Bittensor chain. One install gives you both a
library (`import bittensor`) and a command line (`btcli`).

Documentation: bittensor.com/docs ...

Features:
Almost everything is a projection of the chain's own runtime metadata:

- The generated layer (`bittensor.storage`, `runtime_api`, `constants`,
 `calls`) is emitted from metadata, so it can't drift from the chain. ...

Example:
```python
import bittensor as bt

sub = bt.Subtensor()          # defaults to finney; "test" | "local" | "ws://..."

# Typed namespaces — every read in the catalog, one namespace per
# category, with autocomplete and typed returns
...

</details>

### base64io

(no summary)

`pip install base64io` · installs (wheel) · licence: Apache Software License · rank 8693 · last release 2018-12-10 · [PyPI](https://pypi.org/project/base64io/)

<details><summary>README extract</summary>

This project is designed to develop a class, `base64io.Base64IO`, that implements
a streaming interface for Base64 encoding.

Python has supported native Base64 encoding since version 2.4. However, there is no
streaming interface for Base64 encoding, and none is available from the community. ...

Example:
```python
from base64io import Base64IO

with open("source_file", "rb") as source, open("encoded_file", "wb") as target:
    with Base64IO(target) as encoded_target:
        for line in source:
            encoded_target.write(line)
```

Sections: base64io, Getting Started, Use, Encode data, Decode data

</details>

### brave-search-python-client

🦁 Brave Search Python Client supporting Web, Image, News and Video search.

`pip install brave-search-python-client` · installs (wheel) · licence: MIT License · rank 8703 · last release 2025-04-27 · [PyPI](https://pypi.org/project/brave-search-python-client/) · [docs](https://brave-search-python-client.readthedocs.io/en/latest/) · [source](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client)

<details><summary>README extract</summary>

> [!TIP]
> 📚 Online documentation - 📖 PDF Manual

> [!NOTE]
> 🧠 This project was scaffolded using the template oe-python-template with copier.

Brave Search Python Client supporting Web, Image, News and Video search.

Use Cases:

1. Integrate into your Python code to help users find what they're looking for.
2. ...

Features:
Adding Brave Search Python Client to your project as a dependency is easy.

If you don't have uv installed follow
these instructions.
If you still prefer pip over the modern and fast package manager
uv, you can install the library like this: ...

Example:
```python
"""
Example script demonstrating the usage of the Brave Search Python Client.

For web, image, video and news search.
"""

import asyncio
import os

from dotenv import load_dotenv
...

</details>

### bigquery

Easily send data to Big Query

`pip install bigquery` · installs from source (sdist only) · licence: MIT License · rank 8750 · last release 2025-01-09 · [PyPI](https://pypi.org/project/bigquery/)

### benchling-api-client

Autogenerated Python client from OpenAPI Python Client generator

`pip install benchling-api-client` · installs (wheel) · licence: Apache Software License · rank 8787 · last release 2026-11-05 · [PyPI](https://pypi.org/project/benchling-api-client/)

<details><summary>README extract</summary>

A client generated from Benchling's OpenAPI definition files using openapi-python-client.

Rather than using this package directly, we recommend using the
Benchling SDK, which has extra scaffolding to make some endpoints
easier to use and has been released to general availability.

</details>

### benchling-sdk

SDK for interacting with the Benchling Platform.

`pip install benchling-sdk` · installs (wheel) · licence: Apache Software License · rank 9069 · last release 2026-05-14 · [PyPI](https://pypi.org/project/benchling-sdk/)

<details><summary>README extract</summary>

A Python 3.8+ SDK for the Benchling platform designed to provide typed, fluent
interactions with Benchling APIs.

Sections: Benchling SDK, Documentation

</details>

### byteplus-python-sdk-v2

Byteplus SDK for Python (all services)

`pip install byteplus-python-sdk-v2` · installs (wheel) · licence: Apache License 2.0 · rank 9438 · last release 2026-11-05 · [PyPI](https://pypi.org/project/byteplus-python-sdk-v2/)

<details><summary>README extract</summary>

在 byteplus-python-sdk-v2 的部分历史版本（3.0.1 ～ 3.0.23，含）中，发现 SDK 内置的重试机制存在缺陷。

当请求过程中出现异常（如网络抖动、接口返回错误等）时，SDK 虽会触发重试逻辑，但由于该缺陷，重试未能实际生效，客户端仍可能直接感知到首次请求异常，导致重试机制无法有效提升请求成功率。

- SDK：byteplus-python-sdk-v2
- 受影响版本：3.0.1 ～ 3.0.23（含）

Example:
```python
configuration = byteplussdkcore.Configuration()
configuration.client_side_validation = True
configuration.schema = "http"
configuration.debug = False
configuration.logger_file = "sdk.log"

byteplussdkcore.Configuration.set_default(configuration)
```

Sections: byteplus SDK for Python, ⚠️ 已知缺陷说明（历史版本）, 影响范围, 影响说明, 解决方案与建议, 非兼容升级通知, Requirements, Usage, SDK Documentation, SDK Integration

</details>

### bellows

Library implementing EZSP

`pip install bellows` · installs (wheel) · licence: GPL-3.0 · rank 9810 · last release 2026-10-23 · [PyPI](https://pypi.org/project/bellows/) · [source](https://github.com/zigpy/bellows)

_README extract left out: share-alike licence._

### browserstack-sdk

Python SDK for browserstack selenium-webdriver tests

`pip install browserstack-sdk` · installs from source (sdist only) · licence: BrowserStack Software License Agreement · rank 9835 · last release 2026-07-01 · [PyPI](https://pypi.org/project/browserstack-sdk/)

<details><summary>README extract</summary>

The “Licensed Software” under this BrowserStack Software License Agreement (“Agreement”) shall be used by
you only if You agree to the following terms and conditions. Downloading the Licensed Software and indicating
your consent to the terms of this license constitutes a binding Agreement between BrowserStack and You. ...

</details>

### betterproto-fw

A better Protobuf / gRPC generator & library

`pip install betterproto-fw` · installs (wheel) · licence: MIT License · rank 10093 · last release 2025-05-18 · [PyPI](https://pypi.org/project/betterproto-fw/)

<details><summary>README extract</summary>

Example:
```python
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: example.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

@dataclass
class Greeting(betterproto.Message):
    """Greeting represents a message you can tell a user."""

    message: str = betterproto.string_field(1)
```

Sections: Motivation, Getting Started, Compiling proto files, JSON, Determining if a message was sent, Well-Known Google Types, Generating Pydantic Models, Configuration typing imports, Direct, Root, 310, Requirements, Setup, Code style

</details>

### batchgenerators

Data augmentation toolkit

`pip install batchgenerators` · installs (wheel) · licence: not stated · rank 10194 · last release 2026-10-29 · [PyPI](https://pypi.org/project/batchgenerators/)

<details><summary>README extract</summary>

Copyright German Cancer Research Center (DKFZ) and contributors.
Please make sure that your usage of this code is in compliance with its
`license`.

batchgenerators is a python package for data augmentation. ...

Sections: batchgenerators by MIC@DKFZ, How to use it, Data Structure

</details>

### budoux

BudouX is the successor of Budou

`pip install budoux` · installs (wheel) · licence: Apache-2.0 · rank 10247 · last release 2026-11-06 · [PyPI](https://pypi.org/project/budoux/)

<details><summary>README extract</summary>

<!-- markdownlint-disable MD014 -->

[][pypi-url]
[][npm-url]
[][maven-url]

Standalone. Small. Language-neutral.

BudouX is the successor to Budou,
the machine learning powered line break organizer tool.

It is standalone. It works with no dependency on third-party word segmenters
such as Google cloud natural language API.

It is small. ...

Example:
```python
import budoux
parser = budoux.load_default_japanese_parser()
print(parser.parse('今日は天気です。'))
# ['今日は', '天気です。']
```

Sections: BudouX, Demo, Python module, Usage, Library, CLI, Caveat, Background, How it works, Building a custom model, Disclaimer

</details>

### batched

Batched is a flexible and efficient batch processing library implemented in Python. It supports asynchronous batch processing with dynamic batching and prioritization.

`pip install batched` · installs (wheel) · licence: not stated · rank 10338 · last release 2025-07-14 · [PyPI](https://pypi.org/project/batched/)

<details><summary>README extract</summary>

The Batched API provides a flexible and efficient way to process multiple requests in a batch, with a primary focus on dynamic batching of inference workloads. It is designed to optimize throughput while maintaining a low-latency experience, especially useful in scenarios where you need to handle a high volume of requests simultaneously. ...

Features:
Dynamic batching is a technique that automatically groups multiple incoming inference requests into a single batch for processing. ...

Example:
```python
@batched.dynamically(batch_size=64, timeout_ms=5.0, small_batch_threshold=2)
def custom_batch_function(data):
    # Custom processing logic here
    pass
```

...

</details>

### bio

(no summary)

`pip install bio` · installs (wheel) · licence: MIT · rank 10412 · last release 2026-09-03 · [PyPI](https://pypi.org/project/bio/) · [docs](https://github.com/ialbert/bio#readme) · [source](https://github.com/ialbert/bio/)

<details><summary>README extract</summary>

`bio` - command-line utilities to make bioinformatics explorations more enjoyable.

`bio` is a bioinformatics toy to play with.

Like LEGO pieces that match one another `bio` aims to provide you with commands that naturally fit together and let you express your intent with short, explicit and simple commands. ...

Sections: bio: making bioinformatics fun again, What does this software do?, Usage examples, Documentation, `bio` is stream oriented, Who is `bio` designed for?, Generating documentation

</details>

### bambi

BAyesian Model Building Interface in Python

`pip install bambi` · installs (wheel) · licence: not stated · rank 10583 · last release 2026-09-10 · [PyPI](https://pypi.org/project/bambi/) · [docs](https://bambinos.github.io/bambi) · [source](https://github.com/bambinos/bambi)

<details><summary>README extract</summary>

BAyesian Model-Building Interface in Python

Features:
Bambi is a high-level Bayesian model-building interface written in Python. It's built on top of the PyMC probabilistic programming framework, and is designed to make it extremely easy to fit mixed-effects models common in social sciences settings ...

Example:
```python
import arviz as az
import bambi as bmb
import numpy as np
import pandas as pd
```

Sections: Overview, Dependencies, Examples, Linear regression, Logistic regression, More, Documentation

</details>

### binsize

Tool to analyze the size of a binary from .elf file

`pip install binsize` · installs (wheel) · licence: MIT License · rank 10605 · last release 2025-01-27 · [PyPI](https://pypi.org/project/binsize/) · [source](https://github.com/grdddj/binsize)

<details><summary>README extract</summary>

Tool for analyzing the sizes of symbols in binaries.

It can be used to find out which symbols are taking up the most space in a binary.

It requires `bloaty` and `nm` tools to be installed.

It analyzes the `.elf` file and optionally also the `.map` file from the binary creation process.

Sections: Binsize tool, Tool basic usage, Setting root directory, Manually, Via environmental variable, Via CLI argument, Via exposed function

</details>

### based58

A fast Python library for Base58 and Base58Check

`pip install based58` · installs (wheel) · licence: not stated · rank 10653 · last release 2022-07-18 · [PyPI](https://pypi.org/project/based58/) · [docs](https://kevinheavey.github.io/based58/) · [source](https://github.com/kevinheavey/based58)

<details><summary>README extract</summary>

A fast base-58 Python library

`based58` is a fast Python library for
Base58
encoding and decoding. It includes support for Base58Check and configurable alphabets.

It is
significantly faster
than the pure-Python
base58 library,
as it calls the Rust bs58 library
under the hood. ...

Example:
```python
>>> import based58
>>> data = [1, 2, 3]
>>> based58.b58encode(b'hello world')
b'StV1DL6CwTryKyV'
>>> based58.b58decode(b'StV1DL6CwTryKyV')
b'hello world'
>>> based58.b58encode_check(b'hello world')
b'3vQB7B6MrGQZaxCuFg4oh'
>>> based58.b58decode_check(b'3vQB7B6MrGQZaxCuFg4oh')
b'hello world'
...
```

Sections: based58, Usage, Setup

</details>

### borsh-construct

Python implementation of Borsh serialization, built on the Construct library.

`pip install borsh-construct` · installs (wheel) · licence: MIT License · rank 10854 · last release 2021-10-20 · [PyPI](https://pypi.org/project/borsh-construct/) · [source](https://github.com/near/borsh-construct-py)

<details><summary>README extract</summary>

`borsh-construct` is an implementation of the Borsh binary serialization format for Python projects.

Borsh stands for Binary Object Representation Serializer for Hashing. It is meant to be used in security-critical projects as it prioritizes consistency, safety, speed, and comes with a strict specification.

Read the Documentation.

Sections: borsh-construct, Quick Tests, Full Tests

</details>

### Boruta

Python Implementation of Boruta Feature Selection

`pip install Boruta` · installs (wheel) · licence: BSD 3 clause · rank 10938 · last release 2024-08-13 · [PyPI](https://pypi.org/project/Boruta/)

<details><summary>README extract</summary>

This project hosts Python implementations of the Boruta all-relevant feature selection method.

Related blog post

Example:
```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from boruta import BorutaPy

# load X and y
# NOTE BorutaPy accepts numpy arrays only, hence the .values attribute
X = pd.read_csv('examples/test_X.csv', index_col=0).values
y = pd.read_csv('examples/test_y.csv', header=None, index_col=0).values
y = y.ravel()

...
```

Sections: boruta_py, Dependencies, How to use, Description, What's different in BorutaPy?, Parameters, Attributes, Examples, References

</details>

### bases

Python library for general Base-N encodings.

`pip install bases` · installs (wheel) · licence: not stated · rank 10962 · last release 2023-12-18 · [PyPI](https://pypi.org/project/bases/)

<details><summary>README extract</summary>

Bases provides a customisable, parametric implementation of several common styles of Base-N encoding, covering all cases appearing in the multibase specification (except for proquints).

Sections: bases: A Python library for Base-N encodings, Usage, Base encoding objects, Encoding, Decoding, Case/padding variations, Case sensitivity variations, Custom base encodings, API

</details>

### bumble

Bluetooth Stack for Apps, Emulation, Test and Experimentation

`pip install bumble` · installs (wheel) · licence: Apache-2.0 · rank 10964 · last release 2026-10-15 · [PyPI](https://pypi.org/project/bumble/)

<details><summary>README extract</summary>

_ _ _
 | | | | | |
 | | _ _ | | | | _
 | _ \| | | | \| _ \| || ___ |
 | |_) ) |_| | | | | |_) ) || ____|
 |__/|/|_|_|_|/ \_)___)

Bumble is a full-featured Bluetooth stack written entirely in Python. ...

Sections: Documentation, Usage, Getting Started, Dependencies, Examples, Using Bumble With a USB Dongle, Disclaimer

</details>

### beta9

(no summary)

`pip install beta9` · installs (wheel) · licence: not stated · rank 11036 · last release 2026-11-06 · [PyPI](https://pypi.org/project/beta9/)

### bandwidth-sdk

Bandwidth

`pip install bandwidth-sdk` · installs (wheel) · licence: not stated · rank 11050 · last release 2026-11-04 · [PyPI](https://pypi.org/project/bandwidth-sdk/)

<details><summary>README extract</summary>

Bandwidth's Communication APIs

This Python package is automatically generated by the OpenAPI Generator project:

- API version: 1.0.0
- Package version: 24.0.0
- Generator version: 7.17.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit

Python 3.9+

Example:
```python
import bandwidth
from bandwidth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to
# See configuration.py for a list of all supported configuration parameters.
configuration = bandwidth.Configuration(
    host = "
)

# The client must configure the authentication and authorization parameters
...
```

...

</details>

### beaapi

BEA API Python package

`pip install beaapi` · installs (wheel) · licence: Public Domain · rank 11092 · last release 2026-02-17 · [PyPI](https://pypi.org/project/beaapi/)

<details><summary>README extract</summary>

`beaapi`: A Python library library to make it easier to retrieve and work with BEA data. For the parallel R-package, see bea.R.

To install the package, use `pip install beaapi`.

For help, see our documentation.

For development and building information, see CONTRIBUTING.md. ...

Example:
```python
import beaapi
```

Sections: beaapi, To Get Started, Get metadata, Get data, Advanced topics, Quick Links, Disclaimer

</details>

### blockkit

A fast way to build Block Kit interfaces in Python

`pip install blockkit` · installs (wheel) · licence: MIT License · rank 11113 · last release 2026-01-18 · [PyPI](https://pypi.org/project/blockkit/)

<details><summary>README extract</summary>

Documentation:

Source Code:

Build beautiful Slack UIs fast. Fluent API with type hints, validation, and zero
dependencies.

Building Slack apps shouldn't feel like writing JSON by hand. It's tedious. It's
error prone. And honestly? It's a waste of your time.

You know what you want to build. Your editor should help you build it. ...

Features:
We got tired of:

- Reading Slack's docs for the 100th time
- Building UIs that are impossible to refactor
- Shipping "perfect" JSON that Slack rejects for mysterious reasons

So we fixed it. One library. No dependencies. Just better.

Example:
```python
from blockkit import Modal, Section, Input, PlainTextInput, RadioButtons, Option

modal = (
    Modal()
    .title("Expense Approval")
    .add_block(Section("*New expense request from Alice*"))
...

</details>

### bandit-sarif-formatter

A Bandit formatter for the Static Analysis Results Interchange Format (SARIF) Version 2.1.0 file format.

`pip install bandit-sarif-formatter` · installs (wheel) · licence: MIT License · rank 11191 · last release 2019-10-05 · [PyPI](https://pypi.org/project/bandit-sarif-formatter/)

<details><summary>README extract</summary>

Features:
`bandit_sarif_formatter` is a report formatter
for Bandit, a security analyzer for Python.
It produces output in the Static Analysis Results Interchange Format (SARIF) Version 2.1.0 file format,
an OASIS Committee Specification. ...

Sections: SARIF formatter for Bandit, Overview, Building, Publishing, Using

</details>

### bootstrapped

Implementations of the percentile based bootstrap

`pip install bootstrapped` · installs from source (sdist only) · licence: not stated · rank 11302 · last release 2018-10-17 · [PyPI](https://pypi.org/project/bootstrapped/)

<details><summary>README extract</summary>

bootstrapped is a Python library that allows you to build confidence
intervals from data. This is useful in a variety of contexts - including
during ad-hoc a/b test analysis.

Example:
```python
import numpy as np
import bootstrapped.bootstrap as bs
import bootstrapped.stats_functions as bs_stats

mean = 100
stdev = 10

population = np.random.normal(loc=mean, scale=stdev, size=50000)

# take 1k 'samples' from the larger population
samples = population[:1000]

print(bs.bootstrap(samples, stat_func=bs_stats.mean))
>> 100.08  (99.46, 100.69)
...
```

Sections: bootstrapped - confidence intervals made easy, Motivating Example - A/B Test, The Gist - Mean of a Sample, bootstrapped - Benefits, Example Usage, Extended Examples, Requirements, How bootstrapped works

</details>

### binho-host-adapter

Python Libraries for Binho Multi-Protocol USB Host Adapters

`pip install binho-host-adapter` · installs (wheel) · licence: MIT License · rank 11334 · last release 2020-06-04 · [PyPI](https://pypi.org/project/binho-host-adapter/)

<details><summary>README extract</summary>

Cross-platform Python 3.x library for automated control of Binho Multi-Protocol USB Host Adapters. More information about the device can be found at

This library requires pySerial for cross-platform access of the serial port. ...

Example:
```python
from binhoHostAdapter import binhoHostAdapter
from binhoHostAdapter import binhoUtilities

print("Demo Script with Binho Host Adapter Python Libraries")
print

devices = binhoUtilities.listAvailableDevices()

if len(devices) == 0:
    print("No Devices Found!")
    exit()

elif len(devices) == 1:
    COMPORT = devices[0]
...
```

Sections: Binho Host Adapter Python Libraries, Introduction, Dependencies, Example Usage, Documentation

</details>

### bluesky

Experiment specification & orchestration.

`pip install bluesky` · installs (wheel) · licence: Apache Software License · rank 11351 · last release 2026-10-29 · [PyPI](https://pypi.org/project/bluesky/) · [source](https://github.com/bluesky/bluesky)

<details><summary>README extract</summary>

| Source | < |

| PyPI | `pip install bluesky` |
| Documentation | < |
| Releases | < |

Bluesky is a library for experiment control and collection of scientific data
and metadata. It emphasizes the following virtues:

* Live, Streaming Data: Available for inline visualization and processing. ...

</details>

### bond-pricing

Bond Price with YTM/zero-curve & NPV, IRR, annuities

`pip install bond-pricing` · installs (wheel) · licence: GPL-3.0-or-later · rank 11353 · last release 2026-10-03 · [PyPI](https://pypi.org/project/bond-pricing/)

_README extract left out: share-alike licence._

### bqscales

Grammar of Graphics in Python.

`pip install bqscales` · installs (wheel) · licence: not stated · rank 11373 · last release 2025-12-10 · [PyPI](https://pypi.org/project/bqscales/)

<details><summary>README extract</summary>

Grammar of Graphics in Python for bqplot and other Jupyter widgets libraries

</details>

### blacken-docs

Run Black on Python code blocks in documentation files.

`pip install blacken-docs` · installs (wheel) · licence: MIT · rank 11393 · last release 2025-09-08 · [PyPI](https://pypi.org/project/blacken-docs/) · [source](https://github.com/asottile/blacken-docs)

<details><summary>README extract</summary>

Run Black on Python code blocks in documentation files.

Example:
```python
def f():
    """docstring here

    ``python
    print("hello world")
    ``
    """
```

Sections: blacken-docs, pre-commit hook, Usage, Markdown, reStructuredText, LaTeX

</details>

### brightdata-sdk

Modern async-first Python SDK for Bright Data APIs

`pip install brightdata-sdk` · installs (wheel) · licence: MIT · rank 11455 · last release 2026-08-12 · [PyPI](https://pypi.org/project/brightdata-sdk/)

<details><summary>README extract</summary>

The official Python SDK for Bright Data APIs. Scrape any website, get SERP results, bypass bot detection and CAPTCHAs, and access 100+ ready-made datasets.

Example:
```python
import asyncio
from brightdata import BrightDataClient

async def main():
    async with BrightDataClient() as client:
        result = await client.scrape_url("
        print(result.data)

asyncio.run(main())
```

Sections: Bright Data Python SDK, Configuration, Quick Start, Usage Examples, Web Scraping, Web Scraping Async Mode, Search Engines (SERP), SERP Async Mode, Web Scraper API, Browser API, Discover API, Scraper Studio, Datasets API, Async Usage

</details>

### beam-client

(no summary)

`pip install beam-client` · installs (wheel) · licence: not stated · rank 11498 · last release 2026-11-06 · [PyPI](https://pypi.org/project/beam-client/)

### badX12

A Python Library for parsing ANSI ASC X12 files.

`pip install badX12` · installs (wheel) · licence: MIT License · rank 11509 · last release 2018-12-07 · [PyPI](https://pypi.org/project/badX12/)

<details><summary>README extract</summary>

A Python Library for parsing ANSI ASC X12 files.

Features:
* Parse x12 file format into a python object
* Parse x12 file format into JSON and XML

Example:
```python
from badx12 import Parser

parser = Parser()
document = parser.parse_document("path-to-file/file.edi")
```

Sections: badX12, A Simple Example, Features, Links, 0.1.0 (2018-10-26), 0.2.0 (2018-12-04)

</details>

### base2048

Binary encoding with Base2048 in Rust.

`pip install base2048` · installs (wheel) · licence: MIT · rank 11566 · last release 2022-09-26 · [PyPI](https://pypi.org/project/base2048/)

<details><summary>README extract</summary>

Example:
```python
import base2048

base2048.encode(b'Hello!')
# => 'ϓțƘ໐µ'

base2048.decode('ϓțƘ໐µ')
# => b'Hello!'
```

Sections: When Base 64 is not enough, - Charset displayable on most locales and platforms, Getting Started, Up to 2x less counted characters compared to Base 64, Related and prior works

</details>

### betterproto2-compiler

Compiler for betterproto2

`pip install betterproto2-compiler` · installs (wheel) · licence: MIT · rank 11657 · last release 2026-05-13 · [PyPI](https://pypi.org/project/betterproto2-compiler/) · [docs](https://betterproto.github.io/python-betterproto2/) · [source](https://github.com/betterproto/python-betterproto2)

### bittensor-core

The chain-defined compute core for Bittensor clients: sp-core keys, keyfiles, drand timelock, ML-KEM, SCALE codec, and RFC-0078 metadata digest, built from the bittensor monorepo

`pip install bittensor-core` · installs (wheel) · licence: Apache-2.0 · rank 11684 · last release 2026-11-06 · [PyPI](https://pypi.org/project/bittensor-core/) · [source](https://github.com/RaoFoundation/subtensor)

<details><summary>README extract</summary>

The chain-defined compute core for Bittensor clients, as a single Python
extension module (`import bittensor_core`). Built from the bittensor monorepo
against the same crate revisions as the subtensor runtime itself. ...

</details>

### bitcoin-utils

Bitcoin utility functions

`pip install bitcoin-utils` · installs (wheel) · licence: MIT · rank 11689 · last release 2026-09-29 · [PyPI](https://pypi.org/project/bitcoin-utils/)

<details><summary>README extract</summary>

This is a bitcoin library that provides tools/utilities to interact with the Bitcoin network. One of the primary goals of the library is to explain the low-level details of Bitcoin. The code is easy to read and properly documented explaining in detail all the thorny aspects of the implementation. ...

Sections: python-bitcoin-utils, Notes, Educational trace helpers, Examples, Keys and Addresses, Legacy Transactions (P2PKH, P2SH), Non-standard Transactions, Segwit Transactions, Timelock Transactions, Taproot (segwit v1) Transactions, Taproot with Single Script Path, Taproot with Multiple Script Paths, Partially Signed Bitcoin Transactions (PSBT), Output Descriptors

</details>

### big-O

Empirical estimation of time complexity from execution time

`pip install big-O` · installs from source (sdist only) · licence: LICENSE.txt · rank 11747 · last release 2023-06-06 · [PyPI](https://pypi.org/project/big-O/)

<details><summary>README extract</summary>

big_O is a Python module to estimate the time complexity of Python code from
its execution time. It can be used to analyze how functions scale with inputs
of increasing size.

big_O executes a Python function for input of increasing size `N`, and measures
its execution time. ...

Sections: big_O, Usage, Submodules, Standard library examples, `numpy` examples, Additional examples, Report Generation

</details>

### breez-sdk-spark

Python language bindings for the Breez Spark SDK

`pip install breez-sdk-spark` · installs (wheel) · licence: MIT · rank 11769 · last release 2026-11-05 · [PyPI](https://pypi.org/project/breez-sdk-spark/)

<details><summary>README extract</summary>

Python language bindings for the Breez Spark SDK.

</details>

### bioregistry

Integrated registry of biological databases and nomenclatures

`pip install bioregistry` · installs (wheel) · licence: MIT · rank 11901 · last release 2026-11-07 · [PyPI](https://pypi.org/project/bioregistry/) · [docs](https://bioregistry.readthedocs.io) · [source](https://github.com/biopragmatics/bioregistry.git)

<details><summary>README extract</summary>

A community-driven integrative meta-registry of life science databases, ontologies, and other resources.

More information here.

The Bioregistry can be accessed, searched, and queried through its associated
website at .

The underlying data of the Bioregistry can be downloaded (or edited) directly
from
here. ...

Example:
```python
from bioregistry import normalize_prefix

# Doesn't affect canonical prefixes
assert "ncbitaxon" == normalize_prefix("ncbitaxon")

# This works for uppercased prefixes, like:
assert "chebi" == normalize_prefix("CHEBI")

# This works for mixed case prefixes like
assert "fbbt" == normalize_prefix("FBbt")

# This works for synonym prefixes, like:
...
```

...

</details>

### bd-warehouse

A build123d parametric part collection

`pip install bd-warehouse` · installs (wheel) · licence: Apache Software License · rank 11948 · last release 2026-10-07 · [PyPI](https://pypi.org/project/bd-warehouse/)

<details><summary>README extract</summary>

build123d, a parametric part collection

If you've ever wondered about finding a better alternative to proprietary
software for mechanical CAD, consider exploring
Build123d, along with related
packages like bd_warehouse and
cq_gears. ...

</details>

### bacpypes3

BACnet Communications Library

`pip install bacpypes3` · installs (wheel) · licence: MIT · rank 12042 · last release 2026-09-24 · [PyPI](https://pypi.org/project/bacpypes3/) · [source](https://github.com/JoelBender/bacpypes3)

<details><summary>README extract</summary>

BACpypes provides a BACnet application layer and network layer written in
Python for daemons, scripting, and graphical interfaces. This version is the
next generation for Python3.8+, completely overhauled from the Python2.5+
version using async/await methods and asyncio for communications.

</details>

### betterproto-beta9

A better Protobuf / gRPC generator & library

`pip install betterproto-beta9` · installs (wheel) · licence: MIT License · rank 12095 · last release 2025-03-20 · [PyPI](https://pypi.org/project/betterproto-beta9/) · [source](https://github.com/beam-cloud/python-betterproto)

<details><summary>README extract</summary>

Example:
```python
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: example.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

@dataclass
class Greeting(betterproto.Message):
    """Greeting represents a message you can tell a user."""

    message: str = betterproto.string_field(1)
```

Sections: Motivation, Getting Started, Compiling proto files, JSON, Determining if a message was sent, Well-Known Google Types, Generating Pydantic Models, Requirements, Setup, Code style, Tests, Standard tests, Custom tests, Running

</details>

### blurhash-python

BlurHash encoder implementation for Python

`pip install blurhash-python` · installs from source (sdist only) · licence: MIT License · rank 12122 · last release 2024-01-24 · [PyPI](https://pypi.org/project/blurhash-python/)

<details><summary>README extract</summary>

This is an encoder for the BlurHash algorithm. To find out more about BlurHash, see

Installation

Install blurhash with pip
or pipenv

Usage

Create blurhash from image file
Alternatively, scale the image to produce a faster hash, and create a blurhash from the in-memory image directly
You can also pass file name as parameter to the ...

Example:
```python
import blurhash

with open('image.jpg', 'rb') as image_file:
    hash = blurhash.encode(image_file, x_components=4, y_components=3)
```

</details>

### bbpb

Library for working with protobuf messages without a protobuf type definition.

`pip install bbpb` · installs (wheel) · licence: MIT License · rank 12141 · last release 2025-03-14 · [PyPI](https://pypi.org/project/bbpb/) · [source](https://github.com/nccgroup/blackboxprotobuf)

<details><summary>README extract</summary>

Blackbox protobuf library is a Python module for decoding and re-encoding protobuf
messages without access to the source protobuf descriptor file. This library
provides a simple Python interface to encode/decode messages that can be
integrated into other tools. ...

Example:
```python
import blackboxprotobuf
import base64

data = base64.b64decode('KglNb2RpZnkgTWU=')
message,typedef = blackboxprotobuf.protobuf_to_json(data)
print(message)
```

Sections: BlackBox Protobuf Library, Description, Background, How it works, Usage, CLI, Interface, Decode, Encode, Type definition structure, JSON Encode/Decode, Export/import protofile, Validate Typedef, Output Helper Functions

</details>

### base36

Yet another implementation for the positional numeral system using 36 as the radix.

`pip install base36` · installs (wheel) · licence: MIT License · rank 12429 · last release 2014-12-07 · [PyPI](https://pypi.org/project/base36/)

<details><summary>README extract</summary>

Yet another implementation for the positional numeral system using 36 as the radix.

Example:
```python
import base36

assert base36.dumps(19930503) == 'bv6h3'
assert base36.loads('bv6h3') == 19930503
```

Sections: Base36 in Python, Usage, Issues

</details>

### bdbag

Big Data Bag Utilities

`pip install bdbag` · installs (wheel) · licence: Apache Software License · rank 12433 · last release 2025-09-29 · [PyPI](https://pypi.org/project/bdbag/)

<details><summary>README extract</summary>

The `bdbag` utilities are a collection of software programs for working with
BagIt packages that conform to the BDBag and Bagit/RO profiles.

The `bdbag` profiles specify the use of the `fetch.txt`
file, require serialization, and specify what manifests must be provided with a `bdbag`. ...

Sections: bdbag, Big Data Bag Utilities, Technical Papers, Python Dependencies, Usage, Configuration, Application Programming Interface, Utilities

</details>

### Box2D

Python Box2D

`pip install Box2D` · does not install on CPython 3.14 · licence: zlib · rank 12438 · last release 2024-11-29 · [PyPI](https://pypi.org/project/Box2D/)

<details><summary>README extract</summary>

2D physics library Box2D 2.3 for usage in Python.

After installing please be sure to try out the testbed demos.
They require either pygame or pyglet and are available on the
homepage or directly in this package.

pybox2d homepage:
Box2D homepage:

</details>

### busypie

Easy and expressive busy-waiting for Python

`pip install busypie` · installs (wheel) · licence: Apache Software License · rank 12477 · last release 2026-02-07 · [PyPI](https://pypi.org/project/busypie/)

<details><summary>README extract</summary>

Easy and expressive busy-waiting for Python

Although you typically wouldn't want to do much busy-waiting in your production code,
testing is a different matter. When testing asynchronous systems,
it's very helpful to wait for some scenario to finish its course.
busypie helps you perform busy waiting easily and expressively.

Example:
```python
from busypie import wait, SECOND

def test_create_user():
    create_user_from(USER_DETAILS)
    wait().at_most(2, SECOND).until(lambda: is_user_exists(USER_DETAILS))
```

Sections: Quickstart, Documentation, Links

</details>

### bioversions

Get the current version for biological databases

`pip install bioversions` · installs (wheel) · licence: MIT · rank 12530 · last release 2026-11-08 · [PyPI](https://pypi.org/project/bioversions/) · [docs](https://bioversions.readthedocs.io) · [source](https://github.com/biopragmatics/bioversions.git)

<details><summary>README extract</summary>

What's the current version for each biological database?

A daily updated static listing of all current versions (that are incorporated)
can be found at

Example:
```python
import bioversions

assert bioversions.get_version("biogrid") == "4.2.192", "This was true on Dec 5th, 2020!"

# If you want more information, use the resolve() function
bioversion = bioversions.resolve("biogrid")
assert bioversion.version == "4.2.192"
```

Sections: Bioversions, 💪 Getting Started, 🌐 Web Application, CLI Usage, 👋 Attribution, 🍪 Cookiecutter, 📖 Building the Documentation, Initial Configuration, Configuring ReadTheDocs, Configuring Archival on Zenodo, Registering with the Python Package Index (PyPI), Configuring your machine's connection to PyPI, Uploading to PyPI, Releasing on GitHub

</details>

### business-rules

Python DSL for setting up business intelligence rules that can be configured without code

`pip install business-rules` · installs (wheel) · licence: MIT · rank 12531 · last release 2022-03-18 · [PyPI](https://pypi.org/project/business-rules/)

<details><summary>README extract</summary>

As a software system grows in complexity and usage, it can become burdensome if
every change to the logic/behavior of the system also requires you to write and
deploy new code. The goal of this business rules engine is to provide a simple
interface allowing anyone to capture new rules and logic defining the behavior
of a system, and a way to then ...

Example:
```python
class ProductVariables(BaseVariables):

    def init(self, product):
        self.product = product

    @numeric_rule_variable
    def current_inventory(self):
        return self.product.current_inventory

    @numeric_rule_variable(label='Days until expiration')
    def expiration_days(self)
        last_order = self.product.orders[-1]
...
```

...

</details>

### boring-semantic-layer

A boring semantic layer built with ibis

`pip install boring-semantic-layer` · installs (wheel) · licence: MIT · rank 12539 · last release 2026-08-24 · [PyPI](https://pypi.org/project/boring-semantic-layer/)

<details><summary>README extract</summary>

The Boring Semantic Layer (BSL) is a lightweight semantic layer based on Ibis.

Key Features:
- Lightweight: `pip install boring-semantic-layer`
- Ibis-powered: Built on top of Ibis, supporting any database engine that Ibis integrates with (DuckDB, Snowflake, BigQuery, PostgreSQL, and more) ...

Example:
```python
import ibis

# Create a simple in-memory table
flights_tbl = ibis.memtable({
    "origin": ["JFK", "LAX", "JFK", "ORD", "LAX"],
    "carrier": ["AA", "UA", "AA", "UA", "AA"]
})
```

Sections: Boring Semantic Layer (BSL), Quick Start, 📚 Documentation

</details>

### bencode2

A fast and correct bencode serialize/deserialize library

`pip install bencode2` · installs (wheel) · licence: MIT License · rank 12722 · last release 2026-10-11 · [PyPI](https://pypi.org/project/bencode2/) · [source](https://github.com/trim21/bencode-py)

<details><summary>README extract</summary>

Why yet another bencode package in python?

because I need a bencode library:

It should fully validate its inputs, both encoded bencode bytes, or python object to be
encoded.

And it should not decode bencode bytes to `str` by default. ...

Example:
```python
import bencode2

assert bencode2.bdecode(b"d4:spaml1:a1:bee") == {b"spam": [b"a", b"b"]}

assert bencode2.bencode({'hello': 'world'}) == b'd5:hello5:worlde'
```

Sections: A fast and correct bencode serialize/deserialize library, introduction, 1. Correct, 2. Fast enough, 3. still cross implement, pypi, conda/pixi, basic usage, Decoding, Encoding, free threading

</details>

### biocommons.seqrepo

Non-redundant, compressed, journalled, file-based storage for biological sequences

`pip install biocommons.seqrepo` · installs (wheel) · licence: Apache Software License · rank 12796 · last release 2025-03-19 · [PyPI](https://pypi.org/project/biocommons.seqrepo/)

<details><summary>README extract</summary>

SeqRepo is a Python package for storing and reading a local collection of
biological sequences. The repository is non-redundant, compressed, and
journalled, making it efficient to store and transfer multiple snapshots. ...

Features:
- Timestamped, read-only snapshots.
- Space-efficient storage of sequences within a single snapshot and across snapshots.
- Bandwidth-efficient transfer incremental updates.
- Fast fetching of sequence slices on chromosome-scale sequences. ...

Sections: biocommons.seqrepo, Introduction, Features, Deployments Scenarios, Technical Quick Peek, Requirements, Quick Start, OS X, Ubuntu, All platforms, Environment Variables, Building a docker image, Building

</details>

### bump

Bumps package version numbers

`pip install bump` · installs (wheel) · licence: MIT License · rank 12836 · last release 2026-01-21 · [PyPI](https://pypi.org/project/bump/)

<details><summary>README extract</summary>

Bumps package versions.

Example:
```python
$ bump
1.0.1
$ git diff setup.py
─────────────────────────────────────────────────
modified: setup.py
─────────────────────────────────────────────────
@ setup.py:6 @ from setuptools import setup

setup(
    name='bump',
-    version='1.0.0',
+    version='1.0.1',
    description='Bumps package version numbers',
...
```

Sections: bump, Example, Options

</details>

### bz

这是第一个对外发布的模块，测试哦

`pip install bz` · installs from source (sdist only) · licence: not stated · rank 12945 · last release 2020-06-06 · [PyPI](https://pypi.org/project/bz/)

### bcp47

Language tags made easy

`pip install bcp47` · installs (wheel) · licence: MIT License · rank 13015 · last release 2026-09-19 · [PyPI](https://pypi.org/project/bcp47/)

<details><summary>README extract</summary>

Language tags are not your everyday ISO standard, but instead composed of an ISO-639 language code, and an ISO-3166 country/region code
(and occationally an ISO-15924 script tag for the written language).

The file is generated from Microsoft's seminal piece, [MS-LCID].pdf.

Example:
```python
>>> import bcp47

>>> 'dje' in bcp47.tags and 'es-DO' in bcp47.tags
True

>>> [v for k,v in bcp47.languages.items() if 'English' in k]
['en', 'en-AS', 'en-AI', 'en-AG', 'en-AU', 'en-AT', 'en-BS', 'en-BB', 'en-BE', 'en-BZ', 'en-BM', 'en-BW', 'en-IO', ...]
```

Sections: BCP47, Example, Discontentment

</details>

### bomiot-cmd

Bomiot CMD library

`pip install bomiot-cmd` · does not install on CPython 3.14 · licence: not stated · rank 13097 · last release 2026-10-24 · [PyPI](https://pypi.org/project/bomiot-cmd/)

### betfairlightweight

Lightweight python wrapper for Betfair API-NG

`pip install betfairlightweight` · installs (wheel) · licence: MIT License · rank 13257 · last release 2026-09-04 · [PyPI](https://pypi.org/project/betfairlightweight/) · [docs](https://betcode-org.github.io/betfair/) · [source](https://github.com/betcode-org/betfair.git)

<details><summary>README extract</summary>

Lightweight, super fast (uses C and Rust libraries) pythonic wrapper for Betfair API-NG allowing all betting operations (including market and order streaming) and account operations, see examples.

docs

join betcode slack group

Currently tested on Python 3.9, 3.10, 3.11, 3.12, 3.13 and 3.14.

Example:
```python
import betfairlightweight

trading = betfairlightweight.APIClient('username', 'password', app_key='app_key', certs='/certs')

trading.login()
```

Sections: betfairlightweight, setup, App Key, SSL certificates, Using the library, streaming, historic data

</details>

### boto3-extensions

Extensions to the AWS SDK for Python

`pip install boto3-extensions` · installs (wheel) · licence: Apache Software License · rank 13306 · last release 2023-11-22 · [PyPI](https://pypi.org/project/boto3-extensions/) · [docs](https://bitbucket.org/atlassian/boto3_extensions/) · [source](https://bitbucket.org/atlassian/boto3_extensions/)

<details><summary>README extract</summary>

Features:
This module adds more resource files to the Boto3 library and includes some functionality enhancements.

Example:
```python
import boto3
import boto3_extensions

r = boto3.resource('cloudtrail', region_name='us-east-1')
for trail in r.trails.all():
    print(trail.trail_arn)
```

Sections: Boto3 Extensions, Overview, Quick Start, Resource Files, RefreshableAssumeRoleProvider, ARN Patch, Session Caching, Getting Help

</details>

### blingfire2

Python wrapper of lightning fast Finite State Machine based NLP library.

`pip install blingfire2` · installs (wheel) · licence: not stated · rank 13321 · last release 2025-05-07 · [PyPI](https://pypi.org/project/blingfire2/)

<details><summary>README extract</summary>

Hi, we are a team at Microsoft called Bling (Beyond Language Understanding), we help Bing be smarter. Here we wanted to share with all of you our FInite State machine and REgular expression manipulation library (FIRE). ...

Example:
```python
from blingfire import *

text = 'After reading this post, you will know: What "natural language" is and how it is different from other types of data. What makes working with natural language so challenging. [1]'

print(text_to_sentences(text))
print(text_to_words(text))
```

Sections: Bling Fire, Introduction, Bling Fire Tokenizer Overview, Python API Description, Examples, 1. Python example, using default pattern-based tokenizer, 3. Python example, calling BERT BASE tokenizer, Working Branch, Pull Request, Feedback

</details>

### basedpl

BasedPL, the Based-array Programming Language, is an APL-derived array language, borrowing ideas from J and BQN, with an emphasis on simple, consistent notation.

`pip install basedpl` · installs from source (sdist only) · licence: Apache-2.0 · rank 13548 · last release 2026-11-08 · [PyPI](https://pypi.org/project/basedpl/) · [docs](https://answerdotai.github.io/basedpl) · [source](https://github.com/AnswerDotAI/basedpl)

<details><summary>README extract</summary>

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

BasedPL, the Based-array Programming Language, is an array language derived from APL, with ideas from J and BQN. Its notation aims to be simple and consistent. Most of this documentation calls it BPL. ...

Example:
```python
from basedpl import fn

mean = fn('+/÷≢')
mean([1, 2, 3])
```

Sections: BasedPL, Interactive use, New to APL?, What’s distinctive?, Numbers, Array literals and broadcasting, Keys and named axes, Function operators, Mathematical tools, Data and text, Drawing, Python

</details>

### backports.csv

Backport of Python 3 csv module

`pip install backports.csv` · installs (wheel) · licence: not stated · rank 13595 · last release 2019-03-11 · [PyPI](https://pypi.org/project/backports.csv/)

<details><summary>README extract</summary>

The API of the csv module in Python 2 is drastically different from
the csv module in Python 3. This is due, for the most part, to the
difference between str in Python 2 and Python 3.

The semantics of Python 3's version are more useful because they support
unicode natively, while Python 2's csv does not.

Example:
```python
from backports import csv
```

Sections: backports.csv: Backport of Python 3's csv module, Usage, 1.0.7 (2019-03-10), 1.0.6 (2018-05-22), 1.0.5 (2017-05-29), 1.0.4 (2017-02-17), 1.0.3 (2017-01-23), 1.0.2 (2016-09-15), 1.0.1 (2016-02-11), 1.0 (2016-02-11)

</details>

### bnnumerizer

Bangla Number text to String Converter

`pip install bnnumerizer` · installs from source (sdist only) · licence: MIT License · rank 13601 · last release 2022-10-11 · [PyPI](https://pypi.org/project/bnnumerizer/)

<details><summary>README extract</summary>

Bangla number to Bangla string converter based on the work banglakit/number-to-bengali-word

Example:
```python
from bnnumerizer import numerize
text= "বিল গেটসের ব্যাংক ব্যালেন্স ২২২১২৩৪৫৬.১২৩৪ টাকা। এর মধ্যে আমার অর্থের পরিমাণ ৩৪৫ টাকা মাত্র "
numerize(text)
```

Sections: bnNumerizer, useage, Limitations, Citing

</details>

### bfcl-eval

Berkeley Function Calling Leaderboard (BFCL)

`pip install bfcl-eval` · installs (wheel) · licence: Apache 2.0 · rank 13653 · last release 2026-03-23 · [PyPI](https://pypi.org/project/bfcl-eval/) · [source](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard)

<details><summary>README extract</summary>

Sections: Berkeley Function Calling Leaderboard (BFCL), Introduction, Extra Dependencies for Self-Hosted Models, Configuring Project Root Directory, Setting up Environment Variables, Configuring SerpAPI for Web Search Category, Running Evaluations, Generating LLM Responses, Selecting Models and Test Categories, Selecting Specific Test Cases with `--run-ids`, Output and Logging, For API-based Models, For Locally-hosted OSS Models, For Pre-existing OpenAI-compatible Endpoints

</details>

### binance-connector

This is a deprecated lightweight library that works as a connector to Binance public API.

`pip install binance-connector` · installs (wheel) · licence: MIT License · rank 13921 · last release 2026-04-30 · [PyPI](https://pypi.org/project/binance-connector/)

<details><summary>README extract</summary>

This is a deprecated lightweight library that works as a connector to Binance public API. To access Binance APIs, we recommend using the new Binance Python Connectors which contains auto-generated SDKs for all Binance APIs, including Spot, Futures, Options, and more. ...

Example:
```python
from binance.spot import Spot

client = Spot()

# Get server timestamp
print(client.time())
# Get klines of BTCUSDT at 1m interval
print(client.klines("BTCUSDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
print(client.klines("BNBUSDT", "1h", limit=10))

# API key/secret are required for user data endpoints
...
```

...

</details>

### brand-yml

Read brand yaml files, a unified way to store brand information.

`pip install brand-yml` · installs (wheel) · licence: MIT License · rank 13980 · last release 2026-05-21 · [PyPI](https://pypi.org/project/brand-yml/) · [docs](https://posit-dev.github.io/brand-yml/pkg/py/) · [source](https://github.com/posit-dev/brand-yml)

<details><summary>README extract</summary>

Create reports, apps, dashboards, plots and more that match your
company’s brand guidelines with a single `_brand.yml` file.

brand.yml is a simple, portable YAML file that codifies your
company’s brand guidelines into a format that can be used by
Quarto, Python and R tooling to create branded
outputs. ...

Example:
```python
from brand_yml import Brand

brand = Brand.from_yaml_str(
    # Typically, this file is stored in `_brand.yml`
    # and read with `Brand.from_yaml()`.
    """
    meta:
      name: Posit Software, PBC
      link:
    color:
      palette:
        pblue: "#447099"
        green: "#72994E"
        teal: "#419599"
        orange: "#EE6331"
...
```

Sections: brand.yml Python Package, Example, From PyPI, From GitHub

</details>

### BabelDOC

Yet Another Document Translator

`pip install BabelDOC` · does not install on CPython 3.14 · licence: AGPL-3.0 · rank 13981 · last release 2026-11-07 · [PyPI](https://pypi.org/project/BabelDOC/)

_README extract left out: share-alike licence._

### blastdns

Async Python interface on top of the BlastDNS resolver

`pip install blastdns` · installs (wheel) · licence: AGPL-3.0-or-later · rank 14129 · last release 2026-11-05 · [PyPI](https://pypi.org/project/blastdns/)

_README extract left out: share-alike licence._

### bluesky-queueserver

Server for queueing and executing Bluesky plans.

`pip install bluesky-queueserver` · installs (wheel) · licence: Apache Software License · rank 14252 · last release 2026-11-05 · [PyPI](https://pypi.org/project/bluesky-queueserver/) · [source](https://github.com/bluesky/bluesky-queueserver)

<details><summary>README extract</summary>

Server for managing and executing Bluesky plans.

* Free software: 3-clause BSD license
* Installation instructions.
* Brief description of the project.
* Full documentation.
* 'bluesky-queueserver-api': Python API for Queue Server.
* 'bluesky-httpserver': HTTP Server providing REST API for Queue Server.

</details>

### bluesky-queueserver-api

HTTP Server for communicating with Bluesky Queue Server.

`pip install bluesky-queueserver-api` · installs (wheel) · licence: Apache Software License · rank 14347 · last release 2026-11-06 · [PyPI](https://pypi.org/project/bluesky-queueserver-api/) · [source](https://github.com/bluesky/bluesky-queueserver-api)

<details><summary>README extract</summary>

Python API for Bluesky Queue Server

The project is currently containing a prototype of the API, which can change at any moment.

* Free software: 3-clause BSD license

</details>

### bitfab-py

Bitfab client for provider-based API calls with local BAML execution

`pip install bitfab-py` · installs (wheel) · licence: not stated · rank 14501 · last release 2026-11-08 · [PyPI](https://pypi.org/project/bitfab-py/)

<details><summary>README extract</summary>

Bitfab client for provider-based API calls.

This package is part of the Harvest monorepo. While the TypeScript/JavaScript packages use a pnpm workspace for shared dependencies, this Python package uses Poetry for its dependency management.

Note: The pnpm workspace includes:

- `bitfab-web` - Next.js web application ...

Example:
```python
from bitfab import Bitfab

client = Bitfab(
    api_key="bf_your_api_key_here",
    service_url="  # Optional, defaults to production
    env_vars={"OPENAI_API_KEY": "sk-your-openai-key"},  # Optional, for local BAML execution
)

result = client.call("method_name", arg1="value1", arg2="value2")
```

...

</details>

### botoinator

A decoration mechanism for boto3 that allows automatic decoration of any and all boto3 clients and resources

`pip install botoinator` · installs (wheel) · licence: Apache Software License · rank 14512 · last release 2020-06-05 · [PyPI](https://pypi.org/project/botoinator/)

<details><summary>README extract</summary>

Features:
Botoinator allows you to apply decorators to boto3 methods on either a class or object level. It works through boto3 sessions to allow you to apply decorators to either all clients/resources of a particular session, or to specific clients/resources ...

Example:
```python
import boto3
import botoinator
from moto import mock_s3, mock_sqs

""" This is our decorator that we will apply to boto3 methods """
def myDecorator(func):
  def test_decorator(*args, **kwargs):
    setattr(test_decorator, 'testValue', True) # Add this attribute to the returned function for testing
    return func(*args, **kwargs)
...
```

...

</details>

### bauplan

The client SDK and CLI for Bauplan

`pip install bauplan` · installs (wheel) · licence: Apache-2.0 OR MIT · rank 14540 · last release 2026-11-06 · [PyPI](https://pypi.org/project/bauplan/) · [docs](https://docs.bauplanlabs.com/) · [source](https://github.com/BauplanLabs/bauplan/)

<details><summary>README extract</summary>

Bauplan is a code-first data platform with git-like semantics that lets you bring modern engineering practices to your pipelines.

This repo contains the CLI and SDK code for interacting with the platform.

For more information about Bauplan or the SDK, you can check out: ...

Sections: Bauplan, Running the test suite, Maintaining the python stubs

</details>

### boltdb

python port of boltdb

`pip install boltdb` · installs (wheel) · licence: MIT License · rank 14584 · last release 2020-10-06 · [PyPI](https://pypi.org/project/boltdb/)

<details><summary>README extract</summary>

A Python port of Bolt key/value store.

Sections: boltdb, Example

</details>

### bizdays

Functions to handle business days calculations

`pip install bizdays` · installs (wheel) · licence: not stated · rank 14856 · last release 2026-01-04 · [PyPI](https://pypi.org/project/bizdays/)

<details><summary>README extract</summary>

In several countries and markets, the accountability of the price of a financial
instrument, mainly bonds and derivatives, involves the use of different rules to
compute the way the days go by.
In Brazil, several financial instruments pay interest according to the business
days along their life cycle. ...

</details>

