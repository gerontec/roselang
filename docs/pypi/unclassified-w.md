# Unclassified / W

[Index](README.md) · 90 packages in this topic, by downloads.

### websockets

An implementation of the WebSocket Protocol (RFC 6455 & 7692)

`pip install websockets` · installs (wheel) · licence: BSD-3-Clause · rank 64 · last release 2026-10-30 · [PyPI](https://pypi.org/project/websockets/) · [docs](https://websockets.readthedocs.io/)

<details><summary>README extract</summary>

websockets is a library for building WebSocket servers and clients in Python
with a focus on correctness, simplicity, robustness, and performance.

Built on top of `asyncio`, Python's standard asynchronous I/O framework, the
default implementation provides an elegant coroutine-based API. ...

Features:
The development of `websockets` is shaped by four principles:

1. Correctness: `websockets` is heavily tested for compliance with
 6455. Continuous integration fails under 100% branch coverage.

2. ...

Example:
```python
# !/usr/bin/env python

import asyncio
from websockets.asyncio.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    server = await serve(echo, "localhost", 8765)
...

</details>

### wrapt

Module for decorators, wrappers and monkey patching.

`pip install wrapt` · installs (wheel) · licence: BSD-2-Clause · rank 75 · last release 2026-10-29 · [PyPI](https://pypi.org/project/wrapt/) · [docs](https://wrapt.readthedocs.io/)

<details><summary>README extract</summary>

A Python module for decorators, wrappers and monkey patching.

Features:
The wrapt module provides a transparent object proxy for Python, which can be used as the basis for the construction of function wrappers and decorator functions.

The wrapt module focuses very much on correctness. ...

Example:
```python
import wrapt

@wrapt.decorator
def pass_through(wrapped, instance, args, kwargs):
    return wrapped(*args, **kwargs)

@pass_through
def function():
    pass
```

Sections: wrapt, Overview, Key Features, Documentation, Quick Start, Links

</details>

### wsproto

Pure-Python WebSocket protocol implementation

`pip install wsproto` · installs (wheel) · licence: MIT · rank 359 · last release 2025-11-20 · [PyPI](https://pypi.org/project/wsproto/) · [docs](https://python-hyper.org/) · [source](https://github.com/python-hyper/wsproto/)

<details><summary>README extract</summary>

This repository contains a pure-Python implementation of a WebSocket protocol
stack. It's written from the ground up to be embeddable in whatever program you
choose to use, ensuring that you can communicate via WebSockets, as defined in
RFC6455, regardless of your programming
paradigm. ...

Example:
```python
from wsproto import WSConnection, ConnectionType
from wsproto.events import Request

ws = WSConnection(ConnectionType.CLIENT)
ws.send(Request(host='echo.websocket.org', target='/'))
```

Sections: Pure Python, pure state-machine WebSocket implementation, Usage, Documentation

</details>

### widgetsnbextension

Jupyter interactive widgets for Jupyter Notebook

`pip install widgetsnbextension` · installs (wheel) · licence: BSD License · rank 563 · last release 2026-08-18 · [PyPI](https://pypi.org/project/widgetsnbextension/)

<details><summary>README extract</summary>

This package makes Jupyter widgets available in the classic Jupyter Notebook. This package provides the necessary JavaScript controls in the Jupyter Notebook that communicate with the widget objects in the kernel.

Install the corresponding Jupyter widgets package into your kernel, i.e., IPython users would install `ipywidgets` into their kernel.

</details>

### wasabi

A lightweight console printing and formatting toolkit

`pip install wasabi` · installs (wheel) · licence: MIT · rank 794 · last release 2024-05-31 · [PyPI](https://pypi.org/project/wasabi/)

<details><summary>README extract</summary>

Over the years, I've written countless implementations of coloring and
formatting utilities to output messages in our libraries like
spaCy, Thinc and
Prodigy. While there are many other great open-source
options, I've always ended up wanting something slightly different or slightly
custom. ...

Features:
I was looking for a short and descriptive name, but everything was already
taken. So I ended up naming this package after one of my rats, Wasabi. 🐀

Example:
```python
from wasabi import msg

msg.good("Success!")
```

...

</details>

### webauthn

Pythonic WebAuthn

`pip install webauthn` · installs (wheel) · licence: BSD-3-Clause · rank 1246 · last release 2026-09-25 · [PyPI](https://pypi.org/project/webauthn/)

<details><summary>README extract</summary>

A Python3 implementation of the server-side of the WebAuthn API focused on making it easy to leverage the power of WebAuthn.

This library supports all FIDO2-compliant authenticators, including security keys, Touch ID, Face ID, Windows Hello, Android biometrics...and pretty much everything else.

Sections: py_webauthn, Requirements, Usage, Registration, Authentication, Linting and Formatting

</details>

### workos

WorkOS Python Client

`pip install workos` · installs (wheel) · licence: MIT · rank 1418 · last release 2026-11-05 · [PyPI](https://pypi.org/project/workos/) · [docs](https://workos.com/docs/reference)

<details><summary>README extract</summary>

The WorkOS library for Python provides convenient access to the WorkOS API from applications written in Python, hosted on PyPI.

See the API Reference for Python usage examples.

Features:
The runtime client keeps an environment's feature flag configuration in memory and evaluates flags locally, with no network request per evaluation. ...

Example:
```python
from workos import WorkOSClient

client = WorkOSClient(api_key="sk_1234", client_id="client_1234")

# List organizations
page = client.organizations.list_organizations()
for org in page.auto_paging_iter():
    print(org.name)

# Create an organization
org = client.organizations.create_organization(name="Acme Corp")
print(org.id)
```

...

</details>

### whenever

Type-safe datetimes for Python that get DST right, in Rust or pure Python

`pip install whenever` · installs (wheel) · licence: MIT · rank 1701 · last release 2026-10-02 · [PyPI](https://pypi.org/project/whenever/) · [docs](https://whenever.readthedocs.io) · [source](https://github.com/ariebovenberg/whenever)

<details><summary>README extract</summary>

Type-safe datetimes for Python that get DST right. Rust or pure Python, your choice.

Do you cross your fingers every time you work with Python's datetime—hoping that you didn't
mix naive and aware, or run into one of its other pitfalls? ...

Features:
Over 20+ years, Python's `datetime` has grown
out of step with what you'd expect from a modern datetime library.
Two points stand out:

1. It doesn't always account for daylight saving time (DST).
 Here is a simple example: ...

Example:
```python
>>> from whenever import (
...    # Explicit types for different use cases
...    Instant,
...    ZonedDateTime,
...    PlainDateTime,
... )

# Identify moments in time, without time zone/calendar complexity
>>> now = Instant.now()
Instant("2024-07-04 10:36:56Z")

# Simple, explicit conversions
...

</details>

### wadler-lindig

A Wadler–Lindig pretty-printer for Python.

`pip install wadler-lindig` · installs (wheel) · licence: Apache Software License · rank 1717 · last release 2026-10-25 · [PyPI](https://pypi.org/project/wadler-lindig/) · [source](https://github.com/patrick-kidger/wadler_lindig)

<details><summary>README extract</summary>

This library is for you if you need:

- Something like the built-in `pprint.pprint`, but which consumes less horizontal space. For example in error messages.
- If you have complicated custom types that you'd like to create pretty well-formatted reprs for. For example nested trees of dataclasses / PyTorch modules / etc.

Main features: ...

Example:
```python
import dataclasses
import numpy as np
import wadler_lindig as wl

@dataclasses.dataclass
class MyDataclass:
    x: list[str]
    y: np.ndarray

obj = MyDataclass(["lorem", "ipsum", "dolor sit amet"], np.zeros((2, 3)))

wl.pprint(obj, width=30, indent=4)
# MyDataclass(
# x=[
# 'lorem',
# 'ipsum',
# 'dolor sit amet'
# ],
# y=f642,3
# )
```

...

</details>

### weaviate-client

A python native Weaviate client

`pip install weaviate-client` · installs (wheel) · licence: BSD 3-clause · rank 1753 · last release 2026-10-26 · [PyPI](https://pypi.org/project/weaviate-client/) · [docs](https://weaviate-python-client.readthedocs.io) · [source](https://github.com/weaviate/weaviate-python-client)

<details><summary>README extract</summary>

A python native client for easy interaction with a Weaviate instance.

The client is tested for python 3.9 and higher.

Visit the official Weaviate website for more information about the Weaviate and how to use it in production.

We currently support the following versions client versions:

- 4.X: actively supported ...

Sections: Weaviate python client, Client Versions, Articles, Documentation

</details>

### web3

web3: A Python library for interacting with Ethereum

`pip install web3` · installs (wheel) · licence: MIT · rank 1767 · last release 2026-08-31 · [PyPI](https://pypi.org/project/web3/) · [docs](https://web3py.readthedocs.io/) · [source](https://github.com/ApeWorX/web3.py.git)

<details><summary>README extract</summary>

web3.py allows you to interact with the Ethereum blockchain using Python, enabling you to build decentralized applications, interact with smart contracts, and much more.

- Python 3.10+ support

Sections: web3.py, A Python Library for Interacting with Ethereum, Documentation, Want to Help?, Questions on Implementation or Usage?

</details>

### wirerope

'Turn functions and methods into fully controllable objects'

`pip install wirerope` · installs (wheel) · licence: BSD License · rank 1930 · last release 2025-01-16 · [PyPI](https://pypi.org/project/wirerope/)

<details><summary>README extract</summary>

The concepts:

- `wirerope.rope.WireRope` is a wrapper interface for python callable.
- Custom `wirerope.wire.Wire` class provides user-defined behavior.
 A subclass of this class is working similar to a *decorator function* body.
- A wire object is associated with a bound method.
- Rope is dispatching types. ...

Sections: wirerope, See also

</details>

### wordfreq

Look up the frequencies of words in many languages, based on many sources of data.

`pip install wordfreq` · installs (wheel) · licence: Apache Software License · rank 2735 · last release 2023-11-21 · [PyPI](https://pypi.org/project/wordfreq/)

<details><summary>README extract</summary>

wordfreq is a Python library for looking up the frequencies of words in many
languages, based on many sources of data.

Author: Robyn Speer

Sections: Usage, Frequency bins, The figure-skating metric, Numbers, Other functions, Tokenization, Multi-script languages, Similar, overlapping, and varying languages, Citing wordfreq

</details>

### webdataset

High performance storage and I/O for deep learning and data processing.

`pip install webdataset` · installs (wheel) · licence: BSD-3-Clause · rank 3114 · last release 2025-06-19 · [PyPI](https://pypi.org/project/webdataset/) · [source](http://github.com/webdataset/webdataset)

<details><summary>README extract</summary>

WebDataset format files are tar files, with two conventions:

- within each tar file, files that belong together and make up a training sample share the same basename when stripped of all filename extensions ...

Example:
```python
%matplotlib inline
import matplotlib.pyplot as plt
import torch.utils.data
import torch.nn
from random import randrange
import os
os.environ["WDS_VERBOSE_CACHE"] = "1"
os.environ["GOPEN_VERBOSE"] = "0"
```

Sections: The WebDataset Format, WebDataset Libraries, The `webdataset` Library, The `webdataset` Pipeline API, Secure Mode, Dependencies

</details>

### watchdog-gevent

A gevent-based observer for watchdog.

`pip install watchdog-gevent` · installs (wheel) · licence: not stated · rank 3256 · last release 2024-10-19 · [PyPI](https://pypi.org/project/watchdog-gevent/)

### waybackpy

Python package that interfaces with the Internet Archive's Wayback Machine APIs. Archive pages and retrieve archived pages easily.

`pip install waybackpy` · installs (wheel) · licence: MIT License · rank 3301 · last release 2022-03-15 · [PyPI](https://pypi.org/project/waybackpy/) · [docs](https://github.com/akamhy/waybackpy/wiki) · [source](https://github.com/akamhy/waybackpy)

<details><summary>README extract</summary>

Waybackpy is a Python package and a CLI tool that interfaces with the Wayback Machine APIs.

Wayback Machine has 3 client side APIs.

- SavePageNow or Save API
- CDX Server API
- Availability API

These three APIs can be accessed via the waybackpy either by importing it from a python file/module or from the command-line interface.

Example:
```python
>>> from waybackpy import WaybackMachineSaveAPI
>>> url = "
>>> user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
>>>
>>> save_api = WaybackMachineSaveAPI(url, user_agent)
>>> save_api.save()

>>> save_api.cached_save
False
>>> save_api.timestamp()
datetime.datetime(2022, 1, 18, 12, 52, 49)
```

...

</details>

### wordcloud

A little word cloud generator

`pip install wordcloud` · installs (wheel) · licence: MIT · rank 3570 · last release 2026-01-22 · [PyPI](https://pypi.org/project/wordcloud/)

<details><summary>README extract</summary>

A little word cloud generator in Python. Read more about it on the blog
post or the website.

The code is tested against Python 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13.

Sections: word_cloud, Examples, Command-line usage, Licensing

</details>

### wimpy

Anti-copy-pasta

`pip install wimpy` · installs (wheel) · licence: MIT · rank 3872 · last release 2022-04-03 · [PyPI](https://pypi.org/project/wimpy/)

<details><summary>README extract</summary>

:target:

Some commonly used helpers that I should stop copy-pasting all over the place

</details>

### winrt-runtime

The runtime that every PyWinRT projection package runs on

`pip install winrt-runtime` · installs from source (sdist only) · licence: MIT · rank 3898 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-runtime/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

This package provides the PyWinRT runtime including the `winrt.system` module.

Every PyWinRT package requires it, so pip installs it with any of them. Each
WinRT namespace is a package of its own, so install the package of each
namespace your code imports from, such as `winrt-Windows.Foundation`. ...

Sections: winrt-runtime, For interop modules

</details>

### winrt-Windows.Foundation

PyWinRT projection of the Windows.Foundation namespace

`pip install winrt-Windows.Foundation` · installs (wheel) · licence: MIT · rank 3956 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Foundation/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Foundation` namespace.

This package provides the `winrt.windows.foundation` module.

The WinRT APIs in it are those of version 10.0.28000.2957 of the
`Microsoft.Windows.SDK.CPP` NuGet package. ...

</details>

### winrt-Windows.Foundation.Collections

PyWinRT projection of the Windows.Foundation.Collections namespace

`pip install winrt-Windows.Foundation.Collections` · installs (wheel) · licence: MIT · rank 3996 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Foundation.Collections/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Foundation.Collections` namespace.

This package provides the `winrt.windows.foundation.collections` module.

The WinRT APIs in it are those of version 10.0.28000.2957 of the
`Microsoft.Windows.SDK.CPP` NuGet package. ...

</details>

### west

Zephyr RTOS Project meta-tool

`pip install west` · installs (wheel) · licence: Apache Software License · rank 4034 · last release 2025-09-23 · [PyPI](https://pypi.org/project/west/)

<details><summary>README extract</summary>

This is the Zephyr RTOS meta tool, `west`.

Example:
```python
# Run a subset of tests
tox  --  tests/test_project.py

# Debug the `test_update_narrow()` code with `pdb` (but _not_ the
# west code which is running in subprocesses)
tox  --  --verbose --exitfirst --trace -k test_update_narrow

# Run all tests with "import" in their name and let them log to the
# current terminal
...
```

Sections: Basic Usage, Additional Commands, Hacking on West, Creating a wheel package, Running the Tests

</details>

### wheel-stub

wheel stub package build backend

`pip install wheel-stub` · installs (wheel) · licence: Apache-2.0 · rank 4057 · last release 2026-02-06 · [PyPI](https://pypi.org/project/wheel-stub/)

<details><summary>README extract</summary>

This is a PEP 517 build backend to act as a "soft link" between a package released on a 3rd party package index and pypi.org. This allows users to keep the simple UX of `pip install foo` while hosting the actual wheel files on a non-PyPi index.

Sections: wheel-stub, Demo usage, Configuration

</details>

### wmill

A client library for accessing Windmill server wrapping the Windmill client API

`pip install wmill` · installs (wheel) · licence: Apache Software License · rank 4059 · last release 2026-11-06 · [PyPI](https://pypi.org/project/wmill/) · [docs](https://windmill.dev)

<details><summary>README extract</summary>

The core client for the Windmill platform.

Example:
```python
import time

import wmill

def main():
    # Get the value of a variable
    wmill.get_variable("u/user/variable_path")

    # Run a script synchronously and get the result
    wmill.run_script("f/pathto/script", args={"arg1": "value1"})

    # Get the value of a resource
    wmill.get_resource("u/user/resource_path")

    # Set the script's state
...
```

Sections: wmill, Usage, Basic Usage, Advanced Usage

</details>

### workalendar

Worldwide holidays and working days helper and toolkit.

`pip install workalendar` · installs (wheel) · licence: MIT License · rank 4223 · last release 2023-01-01 · [PyPI](https://pypi.org/project/workalendar/)

<details><summary>README extract</summary>

Features:
Workalendar is a Python module that offers classes able to handle calendars, list legal / religious holidays and gives working-day-related computation functions.

Example:
```python
>>> from datetime import date
>>> from workalendar.europe import France
>>> cal = France()
>>> cal.holidays(2012)
[(datetime.date(2012, 1, 1), 'New year'),
 (datetime.date(2012, 4, 9), 'Easter Monday'),
 (datetime.date(2012, 5, 1), 'Labour Day'),
 (datetime.date(2012, 5, 8), 'Victory in Europe Day'),
 (datetime.date(2012, 5, 17), 'Ascension Day'),
...
```

Sections: Workalendar, Overview, Extra dependencies, Usage sample, External dependencies, Conditional dependencies, Tests, Available Calendars, Europe, America, Asia, Oceania, Africa, Caveats

</details>

### wurlitzer

Capture C-level output in context managers

`pip install wurlitzer` · installs (wheel) · licence: MIT License · rank 4427 · last release 2024-06-12 · [PyPI](https://pypi.org/project/wurlitzer/)

<details><summary>README extract</summary>

Capture C-level stdout/stderr pipes in Python via `os.dup2`.

For more details on why this is needed, please read this blog post.

Example:
```python
from wurlitzer import pipes

with pipes() as (out, err):
    call_some_c_function()

stdout = out.read()
```

Sections: Wurlitzer, Usage, Wurlitzer?!

</details>

### wordninja

Probabilistically split concatenated words using NLP based on English Wikipedia uni-gram frequencies.

`pip install wordninja` · installs from source (sdist only) · licence: not stated · rank 4765 · last release 2019-08-10 · [PyPI](https://pypi.org/project/wordninja/)

### winrt-Windows.ApplicationModel

PyWinRT projection of the Windows.ApplicationModel namespace

`pip install winrt-Windows.ApplicationModel` · installs (wheel) · licence: MIT · rank 4801 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.ApplicationModel/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.ApplicationModel` namespace.

This package provides the `winrt.windows.applicationmodel` module.

The WinRT APIs in it are those of version 10.0.28000.2957 of the
`Microsoft.Windows.SDK.CPP` NuGet package. ...

</details>

### winrt-Windows.Services.Store

PyWinRT projection of the Windows.Services.Store namespace

`pip install winrt-Windows.Services.Store` · installs (wheel) · licence: MIT · rank 4824 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Services.Store/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Services.Store` namespace.

This package provides the `winrt.windows.services.store` module.

The WinRT APIs in it are those of version 10.0.28000.2957 of the
`Microsoft.Windows.SDK.CPP` NuGet package. ...

</details>

### webarena-verified

A verified version of the WebArena Benchmark

`pip install webarena-verified` · installs (wheel) · licence: not stated · rank 4932 · last release 2026-02-07 · [PyPI](https://pypi.org/project/webarena-verified/)

<details><summary>README extract</summary>

WebArena-Verified is the verified release of the WebArena benchmark. It distributes a curated, version-controlled dataset of web tasks together with deterministic evaluators that operate on agent responses and captured network traces. ...

Example:
```python
from datasets import load_dataset

dataset = load_dataset("AmineHA/WebArena-Verified", split="full")
```

Sections: WebArena-Verified, 📢 Announcements, 🎯 Highlights, Usage, pip / uv (project dependency), Docker, Dataset, Full dataset, Hard subset, 🌐 Environments, Start and Stop Sites, Environment Control, 🧪 Evaluate A Task, 📊 Dataset

</details>

### whisper

Fixed size round-robin style database

`pip install whisper` · installs from source (sdist only) · licence: Apache Software License 2.0 · rank 4955 · last release 2022-05-22 · [PyPI](https://pypi.org/project/whisper/)

<details><summary>README extract</summary>

Features:
Whisper is one of three components within the Graphite project:

1. Graphite-Web, a Django-based web application that renders graphs and dashboards
2. The Carbon metric processing daemons
3. The Whisper time-series database library ...

Example:
```python
Usage: whisper-dump.py path

Options:
  -h, --help            show this help message and exit
  --pretty              Show human-readable timestamps instead of unix times
  -t TIME_FORMAT, --time-format=TIME_FORMAT
                        Time format to use with --pretty; see time.strftime()
...
```

Sections: Whisper, Overview, Whisper Scripts

</details>

### win_unicode_console

Enable Unicode input and display when running Python from Windows console.

`pip install win_unicode_console` · installs from source (sdist only) · licence: MIT License · rank 5146 · last release 2016-06-25 · [PyPI](https://pypi.org/project/win_unicode_console/)

<details><summary>README extract</summary>

A Python package to enable Unicode input and display when running Python from Windows console.

When running Python in the standard console on Windows, there are several problems when one tries to enter or display Unicode characters. The relevant issue is This package solves some of them. ...

Sections: win-unicode-console, General information, Usage, Compatibility, Backward incompatibility

</details>

### WMI

Windows Management Instrumentation

`pip install WMI` · installs (wheel) · licence: http://www.opensource.org/licenses/mit-license.php · rank 5331 · last release 2020-04-28 · [PyPI](https://pypi.org/project/WMI/)

<details><summary>README extract</summary>

Windows Management Instrumentation (WMI) is Microsoft's implementation of
Web-Based Enterprise Management (WBEM), an industry initiative to provide
a Common Information Model (CIM) for pretty much any information about a
computer system. ...

Example:
```python
import wmi

c = wmi.WMI()
for s in c.Win32_Service(StartMode="Auto", State="Stopped"):
    if raw_input("Restart %s? " % s.Caption).upper() == "Y":
        s.StartService()
```

Sections: WMI - Windows Management Instrumentation, What is it?, Where do I get it?, How do I use it?, What's Changed?, Prerequisites, Python, pywin32 (was win32all), makepy

</details>

### waiting

Utility for waiting for stuff to happen

`pip install waiting` · installs (wheel) · licence: BSD 3-Clause License · rank 5457 · last release 2024-08-28 · [PyPI](https://pypi.org/project/waiting/)

<details><summary>README extract</summary>

Features:
*waiting* is a small library for waiting for stuff to happen. It basically waits for a function to return True, in various modes.

*Waiting* is compatible with flux for simulated timelines.

Example:
```python
>>> predicate = lambda : True
```

Sections: Overview, Usage

</details>

### webrtc-models

Python WebRTC models

`pip install webrtc-models` · installs (wheel) · licence: Apache-2.0 · rank 5468 · last release 2024-11-18 · [PyPI](https://pypi.org/project/webrtc-models/) · [source](https://github.com/home-assistant-libs/python-webrtc-models)

<details><summary>README extract</summary>

This package provides some data classes for the WebRTC spec

</details>

### www-authenticate

Parser for WWW-Authenticate headers.

`pip install www-authenticate` · installs from source (sdist only) · licence: BSD · rank 5511 · last release 2015-08-05 · [PyPI](https://pypi.org/project/www-authenticate/)

<details><summary>README extract</summary>

Parsing WWW-Authenticate headers is difficult. Let this tiny library do all the
hard work for you.

The header contains a set of comma-separated challenges, but the parameters for
each challenge are also comma-separated. Some challenges in the wild don't have
parameters, which violates the spec. ...

Example:
```python
import www_authenticate

parsed = www_authenticate.parse(response.headers['WWW-Authenticate'])

if 'Basic' in parsed:
    realm = parsed'Basic'
if 'Negotiate' in parsed:
    challenge = parsed['Negotiate']
```

Sections: WWW-Authenticate header parser, What's so difficult?, Usage

</details>

### whisperx

Time-Accurate Automatic Speech Recognition using Whisper.

`pip install whisperx` · does not install on CPython 3.14 · licence: BSD-2-Clause · rank 5521 · last release 2026-05-25 · [PyPI](https://pypi.org/project/whisperx/) · [source](https://github.com/m-bain/whisperx)

<details><summary>README extract</summary>

If you’re looking for a transcription API for meetings, consider checking out Recall.ai's Meeting Transcription API, an API that works with Zoom, Google Meet, Microsoft Teams, and more. ...

Example:
```python
import whisperx
import gc
from whisperx.diarize import DiarizationPipeline

device = "cuda"
audio_file = "audio.mp3"
batch_size = 16 # reduce if low on GPU mem
compute_type = "float16" # change to "int8" if low on GPU mem (may reduce accuracy)

# 1. Transcribe with original whisper (batched)
...
```

Sections: WhisperX, Recall.ai - Meeting Transcription API, New🚨, Setup ⚙️, Speaker Diarization, Usage 💬 (command line), English, Other languages, E.g. German, Python usage 🐍, Demos 🚀, Technical Details 👷‍♂️, Limitations ⚠️, TODO 🗓

</details>

### webdav4

WebDAV client library with an fsspec-based filesystem and a CLI

`pip install webdav4` · installs (wheel) · licence: MIT · rank 5942 · last release 2026-02-19 · [PyPI](https://pypi.org/project/webdav4/) · [docs](https://skshetry.github.io/webdav4) · [source](https://github.com/skshetry/webdav4)

<details><summary>README extract</summary>

Webdav API with an (optional) fsspec implementation and a CLI.

Example:
```python
from webdav4.client import Client

client = Client(" auth=("username", "password"))
client.exists("Documents/Readme.md")

client.ls("Photos", detail=False)
client.upload_file("Gorilla.jpg", "Photos/Gorilla.jpg")
```

Sections: webdav4, Usage, webdav4 Client, fsspec, CLI

</details>

### whichcraft

This package provides cross-platform cross-python shutil.which functionality.

`pip install whichcraft` · installs (wheel) · licence: BSD License · rank 6115 · last release 2019-09-06 · [PyPI](https://pypi.org/project/whichcraft/)

<details><summary>README extract</summary>

This package provides cross-platform cross-python `shutil.which` functionality.

Example:
```python
>>> from whichcraft import which
>>> which('date')
'/bin/date'
>>> which('calendar')
'/bin/calendar'
>>> which('cookiecutter')
'/Users/pydanny/.envs/fun/bin/cookiecutter'
>>> which('a-made-up-name') is None
True
```

Sections: whichcraft, Usage, Notes, 0.6.1 (2019-09-06), 0.6.0 (2019-07-12), 0.5.3 (2018-10-10), 0.5.2 (2018-10-09), 0.5.1 (2018-10-09), 0.5.0 (2018-10-09), 0.4.2 (2018-04-16), 0.4.1 (2017-04-25), 0.3.1 (2016-05-10), 0.3.1 (2016-04-24), 0.3.0 (2016-04-24)

</details>

### winrt-Windows.Storage.Streams

PyWinRT projection of the Windows.Storage.Streams namespace

`pip install winrt-Windows.Storage.Streams` · installs (wheel) · licence: MIT · rank 6641 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Storage.Streams/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Storage.Streams` namespace.

This package provides the `winrt.windows.storage.streams` module.

The WinRT APIs in it are those of version 10.0.28000.2957 of the
`Microsoft.Windows.SDK.CPP` NuGet package. ...

</details>

### wadllib

Navigate HTTP resources using WADL files as guides.

`pip install wadllib` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 6814 · last release 2026-07-01 · [PyPI](https://pypi.org/project/wadllib/) · [docs](https://wadllib.readthedocs.io/en/latest/) · [source](https://code.launchpad.net/wadllib)

_README extract left out: share-alike licence._

### wait-for2

Asyncio wait_for that can handle simultaneous cancellation and future completion.

`pip install wait-for2` · installs (wheel) · licence: Apache-2.0 · rank 7053 · last release 2025-06-13 · [PyPI](https://pypi.org/project/wait-for2/)

<details><summary>README extract</summary>

If you only want to support Python 3.12+ then you should not need this library.

Alternate implementation of `asyncio.wait_for()`. It handles several edge cases like simultaneous
cancellation of wait and completion of future differently and consistently across Python versions 3.7+. ...

Sections: wait_for2, Updates, Details, Cancellation behaviour with simultaneous result, Timeout handling behaviour with results, Cancellation behaviour with timeout handling

</details>

### workers-runtime-sdk

Python SDK for Cloudflare Workers

`pip install workers-runtime-sdk` · installs (wheel) · licence: MIT · rank 7097 · last release 2026-11-04 · [PyPI](https://pypi.org/project/workers-runtime-sdk/)

### wandb-osh

Trigger wandb offline syncs from a compute node without internet

`pip install wandb-osh` · installs (wheel) · licence: MIT License · rank 7151 · last release 2024-03-21 · [PyPI](https://pypi.org/project/wandb-osh/) · [docs](https://wandb_osh.readthedocs.io/) · [source](https://github.com/klieret/wandb-offline-sync-hook)

<details><summary>README extract</summary>

A convenient way to trigger synchronizations to wandb if your compute nodes don't have internet!

- ✅ You use `wandb`/Weights & Biases to record your machine learning trials?
- ✅ Your ML experiments run on compute nodes without internet access (for example, using a batch system)? ...

Example:
```python
import wandb
from wandb_osh.hooks import TriggerWandbSyncHook  # <-- New!

trigger_sync = TriggerWandbSyncHook()  # <--- New!

wandb.init(config=args, mode="offline")

model = ... # set up your model

# Magic
wandb.watch(model, log_freq=100)

model.train()
for batch_idx, (data, target) in enumerate(train_loader):
    output = model(data)
...
```

...

</details>

### wfdb

The WFDB Python package: tools for reading, writing, and processing physiologic signals and annotations.

`pip install wfdb` · installs (wheel) · licence: MIT License · rank 7200 · last release 2026-02-03 · [PyPI](https://pypi.org/project/wfdb/) · [docs](https://wfdb.readthedocs.io/) · [source](https://github.com/MIT-LCP/wfdb-python/)

<details><summary>README extract</summary>

A Python-native package for reading, writing, processing, and plotting physiologic signal and annotation data. The core I/O functionality is based on the Waveform Database (WFDB) specifications.

This package is heavily inspired by the original WFDB Software Package, and initially aimed to replicate many of its command-line APIs. ...

Sections: The WFDB Python Package, Introduction, Documentation and Usage, Citing

</details>

### wsgiref

WSGI (PEP 333) Reference Library

`pip install wsgiref` · installs from source (sdist only) · licence: PSF or ZPL · rank 7391 · last release 2006-06-12 · [PyPI](https://pypi.org/project/wsgiref/)

<details><summary>README extract</summary>

This is a standalone release of the ``wsgiref`` library, that provides
validation support for WSGI 1.0.1 (PEP 3333) for Python versions < 3.2,
and includes the new ``wsgiref.util.test()`` utility function.

For this version's documentation, see:

HTML

PDF

(You can also check out the `development version`_ using
``easy_install wsgiref==dev``.) ...

</details>

### wetext

WeTextProcessing Runtime

`pip install wetext` · installs (wheel) · licence: Apache-2.0 · rank 7615 · last release 2026-10-31 · [PyPI](https://pypi.org/project/wetext/) · [docs](https://github.com/pengzhendong/wetext#readme)

<details><summary>README extract</summary>

Multilingual text normalization for speech applications, without a Pynini runtime dependency.

Quick start · Languages · Python API · Streaming · Development

`wetext` runs the weighted finite-state transducer (WFST) grammars from
WeTextProcessing using
kaldifst. ...

Example:
```python
from wetext import Normalizer

normalizer = Normalizer(lang="zh", operator="tn")
print(normalizer.normalize("价格是12.5元"))  # 价格是十二点五元

inverse_normalizer = Normalizer(lang="en", operator="itn")
print(inverse_normalizer.normalize("twenty three dollars and fifty cents"))  # $23.50
```

Sections: WeTextProcessing Runtime, Quick start, Python, Command line, Python API, Normalize text, Rule modes and case, Code-mixed ITN, Processing options, N-best candidates and costs, Exact input/output mappings, Streaming

</details>

### wolframalpha

Wolfram|Alpha 2.0 API client

`pip install wolframalpha` · installs (wheel) · licence: MIT · rank 7776 · last release 2026-10-03 · [PyPI](https://pypi.org/project/wolframalpha/) · [source](https://github.com/jaraco/wolframalpha)

<details><summary>README extract</summary>

Python Client built against the Wolfram|Alpha
v2.0 API.

</details>

### websockify

Websockify.

`pip install websockify` · installs (wheel) · licence: LGPLv3 · rank 8038 · last release 2025-05-26 · [PyPI](https://pypi.org/project/websockify/)

_README extract left out: share-alike licence._

### wordsegment

English word segmentation.

`pip install wordsegment` · installs (wheel) · licence: Apache Software License · rank 8604 · last release 2018-07-07 · [PyPI](https://pypi.org/project/wordsegment/)

<details><summary>README extract</summary>

WordSegment is an Apache2 licensed module for English word
segmentation, written in pure-Python, and based on a trillion-word corpus.

Based on code from the chapter "Natural Language Corpus Data" by Peter
Norvig from the book "Beautiful Data" (Segaran and Hammerbacher, 2009). ...

Features:
- Pure-Python
- Fully documented
- 100% Test Coverage
- Includes unigram and bigram data
- Command line interface for batch processing
- Easy to hack (e.g. different scoring, new data, different language)
- Developed on Python 2.7 ...

Example:
```python
>>> import wordsegment
>>> help(wordsegment)
```

Sections: Python Word Segmentation, Features, Quickstart, Tutorial, User Guide, References

</details>

### whool

whool - build backend for Odoo addons

`pip install whool` · installs (wheel) · licence: MIT License · rank 9201 · last release 2026-10-15 · [PyPI](https://pypi.org/project/whool/) · [docs](https://github.com/sbidoul/whool) · [source](https://github.com/sbidoul/whool)

<details><summary>README extract</summary>

A standards-compliant Python build backend to package individual Odoo addons.

> [!NOTE]
> If you are looking at packaging a customer project or a collection of addons, you
> may want to consider the hatch-odoo project.

Sections: whool, Quick start, Files included in the distribution packages, Version number of the generated packages, Configuration, Standard compliance, Comparison to setuptools-odoo

</details>

### wmctrl

A tool to programmatically control windows inside X

`pip install wmctrl` · installs (wheel) · licence: MIT License · rank 9256 · last release 2023-09-16 · [PyPI](https://pypi.org/project/wmctrl/)

<details><summary>README extract</summary>

A tool to programmatically control windows inside X

</details>

### window-ops

Implementations of window operations such as rolling and expanding.

`pip install window-ops` · installs (wheel) · licence: Apache Software License · rank 9287 · last release 2024-03-04 · [PyPI](https://pypi.org/project/window-ops/)

<details><summary>README extract</summary>

This library is intended to be used as an alternative to
`pd.Series.rolling` and `pd.Series.expanding` to gain a speedup by using
numba optimized functions operating on numpy arrays. There are also
online classes for more efficient updates of window statistics.

Example:
```python
times.applymap('{:.2f}'.format)
```

Sections: Window ops, How to use, Transformations, Benchmarks, Online

</details>

### winrt-Windows.Graphics.Imaging

PyWinRT projection of the Windows.Graphics.Imaging namespace

`pip install winrt-Windows.Graphics.Imaging` · installs (wheel) · licence: MIT · rank 9331 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Graphics.Imaging/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Graphics.Imaging` namespace.

This package provides the `winrt.windows.graphics.imaging` module.

The WinRT APIs in it are those of version 10.0.28000.2957 of the
`Microsoft.Windows.SDK.CPP` NuGet package. ...

</details>

### warc3-wet

Python library to work with ARC and WARC files

`pip install warc3-wet` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 9360 · last release 2024-07-17 · [PyPI](https://pypi.org/project/warc3-wet/)

_README extract left out: share-alike licence._

### workers-py

A set of libraries and tools for Python Workers

`pip install workers-py` · installs (wheel) · licence: MIT · rank 9369 · last release 2026-10-23 · [PyPI](https://pypi.org/project/workers-py/)

<details><summary>README extract</summary>

A set of libraries and tools for Python Workers.

A CLI tool for managing vendored packages in a Python Workers project.

Sections: workers-py, Pywrangler, Usage, Lint, Tests

</details>

### winrt-Windows.Media.Ocr

PyWinRT projection of the Windows.Media.Ocr namespace

`pip install winrt-Windows.Media.Ocr` · installs (wheel) · licence: MIT · rank 9384 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Media.Ocr/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Media.Ocr` namespace.

This package provides the `winrt.windows.media.ocr` module.

The WinRT APIs in it are those of version 10.0.28000.2957 of the
`Microsoft.Windows.SDK.CPP` NuGet package. ...

</details>

### winrt-Windows.Globalization

PyWinRT projection of the Windows.Globalization namespace

`pip install winrt-Windows.Globalization` · installs (wheel) · licence: MIT · rank 9510 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Globalization/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Globalization` namespace.

This package provides the `winrt.windows.globalization` module.

The WinRT APIs in it are those of version 10.0.28000.2957 of the
`Microsoft.Windows.SDK.CPP` NuGet package. ...

</details>

### winrt-Windows.Devices.Enumeration

PyWinRT projection of the Windows.Devices.Enumeration namespace

`pip install winrt-Windows.Devices.Enumeration` · installs (wheel) · licence: MIT · rank 9899 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Devices.Enumeration/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Devices.Enumeration` namespace.

This package provides the `winrt.windows.devices.enumeration` module.

The WinRT APIs in it are those of version 10.0.28000.2957 of the
`Microsoft.Windows.SDK.CPP` NuGet package. ...

</details>

### winrt-Windows.Devices.Bluetooth

PyWinRT projection of the Windows.Devices.Bluetooth namespace

`pip install winrt-Windows.Devices.Bluetooth` · installs (wheel) · licence: MIT · rank 9953 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Devices.Bluetooth/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Devices.Bluetooth` namespace.

This package provides the `winrt.windows.devices.bluetooth` module.

The WinRT APIs in it are those of version 10.0.28000.2957 of the
`Microsoft.Windows.SDK.CPP` NuGet package. ...

</details>

### winrt-Windows.Devices.Bluetooth.Advertisement

PyWinRT projection of the Windows.Devices.Bluetooth.Advertisement namespace

`pip install winrt-Windows.Devices.Bluetooth.Advertisement` · installs (wheel) · licence: MIT · rank 10127 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Devices.Bluetooth.Advertisement/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Devices.Bluetooth.Advertisement` namespace.

This package provides the `winrt.windows.devices.bluetooth.advertisement` module. ...

</details>

### winrt-Windows.Devices.Bluetooth.GenericAttributeProfile

PyWinRT projection of the Windows.Devices.Bluetooth.GenericAttributeProfile namespace

`pip install winrt-Windows.Devices.Bluetooth.GenericAttributeProfile` · installs (wheel) · licence: MIT · rank 10128 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Devices.Bluetooth.GenericAttributeProfile/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Devices.Bluetooth.GenericAttributeProfile` namespace.

This package provides the `winrt.windows.devices.bluetooth.genericattributeprofile` module. ...

</details>

### winrt-Windows.Devices.Radios

PyWinRT projection of the Windows.Devices.Radios namespace

`pip install winrt-Windows.Devices.Radios` · installs (wheel) · licence: MIT · rank 10359 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Devices.Radios/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Devices.Radios` namespace.

This package provides the `winrt.windows.devices.radios` module.

The WinRT APIs in it are those of version 10.0.28000.2957 of the
`Microsoft.Windows.SDK.CPP` NuGet package. ...

</details>

### warc3-wet-clueweb09

Python library to work with ARC and WARC files, with fixes for ClueWeb09

`pip install warc3-wet-clueweb09` · installs from source (sdist only) · licence: GNU General Public License v2 (GPLv2) · rank 10377 · last release 2020-12-07 · [PyPI](https://pypi.org/project/warc3-wet-clueweb09/)

_README extract left out: share-alike licence._

### whisper-timestamped

Multi-lingual Automatic Speech Recognition (ASR) based on Whisper models, with accurate word timestamps, access to language detection confidence, several options for Voice Activity Detection (VAD), and more.

`pip install whisper-timestamped` · installs (wheel) · licence: GPLv3 · rank 10393 · last release 2025-09-09 · [PyPI](https://pypi.org/project/whisper-timestamped/)

_README extract left out: share-alike licence._

### whoisit

A Python client to RDAP WHOIS-like services for internet resources.

`pip install whoisit` · installs (wheel) · licence: not stated · rank 10482 · last release 2026-10-26 · [PyPI](https://pypi.org/project/whoisit/)

<details><summary>README extract</summary>

A Python client to RDAP WHOIS-like services for internet resources (IPs, ASNs, domains,
etc.). `whoisit` is a simple library that makes requests to the "new" RDAP (Registration
Data Access Protocol) query services for internet resource information. These services
started to appear in 2017 and have become more widespread since 2020. ...

Example:
```python
import whoisit

whoisit.bootstrap()

results = whoisit.asn(1234)
print(results["name"])

results = whoisit.domain("example.com")
print(results["nameservers"])

results = whoisit.ip("1.2.3.4")
print(results["name"])

results = whoisit.ip("1.2.3.0/24")
print(results["name"])

results = whoisit.ip("2404:1234:1234:1234:1234:1234:1234:1234")
...
```

...

</details>

### wincertstore

Python module to extract CA and CRL certs from Windows' cert store (ctypes based).

`pip install wincertstore` · installs (wheel) · licence: Python Software Foundation License · rank 10665 · last release 2021-06-08 · [PyPI](https://pypi.org/project/wincertstore/)

<details><summary>README extract</summary>

wincertstore provides an interface to access Windows' CA and CRL certificates.
It uses ctypes and Windows's sytem cert store API through crypt32.dll.

Example:
```python
import wincertstore
for storename in ("CA", "ROOT"):
    with wincertstore.CertSystemStore(storename) as store:
        for cert in store.itercerts(usage=wincertstore.SERVER_AUTH):
            print(cert.get_pem().decode("ascii"))
            print(cert.get_name())
            print(cert.enhanced_keyusage_names())
```

Sections: wincertstore, Example, Requirements, References, wincertstore 0.2, wincertstore 0.1

</details>

### WebUI

WebUI lets you create first class desktop applications in Python with HTML/CSS

`pip install WebUI` · installs from source (sdist only) · licence: MIT · rank 11303 · last release 2013-09-25 · [PyPI](https://pypi.org/project/WebUI/)

<details><summary>README extract</summary>

WebUI is a Python module that allows you to convert Flask apps into cross platform desktop apps with three lines of code.

Example:
```python
from WebUI import WebUI # Add WebUI to your imports
from flask import Flask, render_template, request

app = Flask(name)
ui = WebUI(app, debug=True) # Create a WebUI instance

# all of your standard flask logic

if name == 'main':
  ui.run() #replace app.run() with ui.run(), and that's it
```

Sections: WebUI, Usage

</details>

### wagtail-factories

Factory boy classes for wagtail

`pip install wagtail-factories` · installs (wheel) · licence: MIT License · rank 11522 · last release 2026-06-04 · [PyPI](https://pypi.org/project/wagtail-factories/)

<details><summary>README extract</summary>

Factory boy classes for Wagtail CMS

Example:
```python
import wagtail_factories
from wagtail import models as wt_models

from . import models

class MyCarouselItemFactory(wagtail_factories.StructBlockFactory):
    label = 'my-label'
    image = factory.SubFactory(
        wagtail_factories.ImageChooserBlockFactory)

    class Meta:
        model = models.MyBlockItem

...
```

Sections: wagtail-factories, Usage, Using StreamBlockFactory, Alternative StreamFieldFactory declaration syntax

</details>

### wagtail-modeladmin

Add any model in your project to the Wagtail admin. Formerly wagtail.contrib.modeladmin.

`pip install wagtail-modeladmin` · installs (wheel) · licence: BSD-3-Clause · rank 11691 · last release 2026-09-25 · [PyPI](https://pypi.org/project/wagtail-modeladmin/) · [source](https://github.com/wagtail-nest/wagtail-modeladmin)

<details><summary>README extract</summary>

Add any model in your project to the Wagtail admin. Formerly `wagtail.contrib.modeladmin`.

This package is in maintenance mode and will not receive new features. Consider migrating to Wagtail's built-in features and opening new feature requests in the Wagtail issue tracker.

- Documentation
- Changelog
- Contributing
- Discussions
- Security

Sections: Wagtail ModelAdmin, Links, Using pip, Using flit, pre-commit, How to run tests

</details>

### wgpu

WebGPU for Python

`pip install wgpu` · installs (wheel) · licence: not stated · rank 12103 · last release 2026-11-06 · [PyPI](https://pypi.org/project/wgpu/) · [docs](https://wgpu-py.readthedocs.io) · [source](https://github.com/pygfx/wgpu-py)

<details><summary>README extract</summary>

A Python implementation of WebGPU - the next generation GPU API. 🚀

The purpose of wgpu-py is to provide Python with a powerful and reliable GPU API.

It serves as a basis to build a broad range of applications and libraries
related to visualization and GPU compute. We use it in
pygfx to create a modern Pythonic render
engine. ...

Example:
```python
import wgpu
```

Sections: wgpu-py, Introduction, What is WebGPU / wgpu?, Usage, Projects using `wgpu-py`, Quick tips

</details>

### wntr

Water Network Tool for Resilience

`pip install wntr` · installs from source (sdist only) · licence: Revised BSD · rank 12307 · last release 2026-07-01 · [PyPI](https://pypi.org/project/wntr/)

<details><summary>README extract</summary>

The Water Network Tool for Resilience (WNTR) is a Python package designed to simulate and
analyze resilience of water distribution networks. The software includes capability to: ...

</details>

### wtpsplit

Universal Robust, Efficient and Adaptable Sentence Segmentation

`pip install wtpsplit` · installs (wheel) · licence: MIT · rank 12462 · last release 2026-09-25 · [PyPI](https://pypi.org/project/wtpsplit/)

<details><summary>README extract</summary>

This repository allows you to segment text into sentences or other semantic units. It implements the models from:

- SaT — Segment Any Text: A Universal Approach for Robust, Efficient and Adaptable Sentence Segmentation by Markus Frohmann, Igor Sterner, Benjamin Minixhofer, Ivan Vulić and Markus Schedl (state-of-the-art, encouraged). ...

Example:
```python
from wtpsplit import SaT

sat = SaT("sat-3l")
# optionally run on GPU for better performance
# also supports TPUs via e.g. sat.to("xla:0"), in that case pass `pad_last_batch=True` to sat.split
sat.half().to("cuda")

sat.split("This is a test This is another test.")
# returns ["This is a test ", "This is another test."]

...
```

...

</details>

### winacl

ACL/ACE/Security Descriptor manipulation library in pure Python

`pip install winacl` · installs (wheel) · licence: MIT License · rank 12765 · last release 2024-05-06 · [PyPI](https://pypi.org/project/winacl/)

### wily

A Python application for tracking, reporting on timing and complexity in tests and applications.

`pip install wily` · installs (wheel) · licence: Apache Software License · rank 12956 · last release 2023-10-11 · [PyPI](https://pypi.org/project/wily/) · [docs](https://wily.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

A command-line application for tracking, reporting on complexity of Python tests and applications.

Wily uses git to go through each revision (commit) in a branch and run complexity and code-analysis metrics over the code. You can use this to limit your code or report on trends for complexity, length etc.

Sections: Usage, Demo, Using Wily in a CI/CD pipeline, pre-commit plugin, Command line usage, `wily build`, `wily report`, `wily rank`, `wily graph`, `wily index`, `wily list-metrics`, Configuration, IPython/Jupyter Notebooks

</details>

### whitebox

An advanced geospatial data analysis platform

`pip install whitebox` · installs (wheel) · licence: MIT License · rank 13037 · last release 2025-02-23 · [PyPI](https://pypi.org/project/whitebox/)

<details><summary>README extract</summary>

This repository is related to the WhiteboxTools Python Frontend only. You can report issues to this repo if you have problems installing this Python package. If you encounter any tool functioning specific errors, please open an issue on Dr. John Lindsay's WhiteboxTools repo.

Links

* Authors: Dr. John Lindsay (
* Contributors: Dr. Qiusheng Wu ( ...

Example:
```python
import os
from importlib_resources import files
import whitebox

wbt = whitebox.WhiteboxTools()
print(wbt.version())
print(wbt.help())

# identify the sample data directory of the package
data_dir = str(files("whitebox").joinpath("testdata"))

wbt.set_working_dir(data_dir)
wbt.verbose = False
...
```

...

</details>

### wotan

Detrending algorithms

`pip install wotan` · installs (wheel) · licence: MIT · rank 13533 · last release 2026-11-06 · [PyPI](https://pypi.org/project/wotan/)

<details><summary>README extract</summary>

...offers free and open source algorithms to automagically remove trends from time-series data.

> In Germanic mythology, Odin (/ˈoːðinː/ Old High German: Wōtan) is a widely revered god. He gave one of his eyes to Mimir in return for wisdom. Thus, in order to achieve a goal, one sometimes has to turn a blind eye. ...

Example:
```python
from wotan import flatten
flatten_lc, trend_lc = flatten(time, flux, window_length=0.5, method='biweight', return_trend=True)
```

Sections: Wōtan..., Speed

</details>

### wbgapi

wbgapi provides a comprehensive interface to the World Bank's data and metadata APIs

`pip install wbgapi` · installs (wheel) · licence: MIT · rank 13585 · last release 2026-02-27 · [PyPI](https://pypi.org/project/wbgapi/)

<details><summary>README extract</summary>

WBGAPI provides modern, pythonic access to the World Bank's data API.
It is designed both for data novices and data scientist types.

WBGAPI differs from other packages for World Bank data in a few respects and in general tries
to take full advantage of the World Bank's powerful API while mitigating
the impact of some its ideosyncracies. ...

Sections: WBGAPI, Quick Start, Design Overview, Looking Around, Accessing Data, Non-Standard and Custom Dimensions, Access the Economies Data Frame, Accessing Metadata, Resolving Country Names, Customizing the Display, Proxy Servers and Other HTTP Options, Caching

</details>

### wordybin

Memorable word-based encoding for binary data.

`pip install wordybin` · installs (wheel) · licence: MIT License · rank 13788 · last release 2023-08-29 · [PyPI](https://pypi.org/project/wordybin/) · [source](https://github.com/petergaultney/wordybin/)

<details><summary>README extract</summary>

What the world needs is yet another word-based encoding system for
binary data. In this case, a 16-bit encoding system, with one of 512
5-letter words standing in for the first 9 bits, and one of 128
3-letter words standing in for the next 7 bits.

Features:
1. Because the words are fixed length, the encoded string length has a
 stepwise linear relationship to the source data. This can be
 advantageous for humans who are trying to eyeball something, and
 stands in contrast to encodings like BIP39.
2. ...

Sections: WordyBin, Why?, Why would I actually use this?

</details>

### whylogs

Profile and monitor your ML data pipeline end-to-end

`pip install whylogs` · installs (wheel) · licence: Apache Software License · rank 13867 · last release 2024-12-03 · [PyPI](https://pypi.org/project/whylogs/)

<details><summary>README extract</summary>

Slack Community •
 Python Quickstart •
 WhyLabs Quickstart

whylogs is an open source library for logging any kind of data. With whylogs, users are able to generate summaries of their datasets (called _whylogs profiles) which they can use to:

1. Track changes in their dataset
2. ...

Example:
```python
import whylogs as why
import pandas as pd

df = pd.read_csv("path/to/file.csv")
results = why.log(df)
```

Sections: The open standard for data logging, Documentation •, What is whylogs, Quickstart

</details>

### watermark

IPython magic function to print date/time stamps and various system information.

`pip install watermark` · installs (wheel) · licence: BSD License · rank 13925 · last release 2025-12-21 · [PyPI](https://pypi.org/project/watermark/)

<details><summary>README extract</summary>

An IPython magic extension for printing date and time stamps, version numbers, and hardware information.

- Examples
- Installation and updating
- Usage
- Development guidelines
- Changelog

Example:
```python
from watermark import watermark
print(watermark())
```

Sections: watermark, Sections, Examples, Using watermark in Jupyter notebooks and IPython sessions, Using watermark as a module, Usage, v. 2.6.0 (TBA), v. 2.5.1 (Dec 14, 2025), v. 2.5.0 (Sep 20, 2024), v. 2.4.3 (May 23, 2023), v. 2.4.1 and v 2.4.2 (May 23, 2023), v. 2.4.0 (May 23, 2023), v. 2.3.1 (May 27, 2022), v. 2.3.0 (January 3, 2022)

</details>

### waldur-api-client

A client library for accessing Waldur API

`pip install waldur-api-client` · installs (wheel) · licence: MIT License · rank 13977 · last release 2026-11-06 · [PyPI](https://pypi.org/project/waldur-api-client/) · [docs](https://docs.waldur.com)

<details><summary>README extract</summary>

A client library for accessing Waldur API

Example:
```python
from waldur_api_client import Client

client = Client(base_url="
```

Sections: waldur-api-client, Usage, Advanced customizations, Building / publishing this package

</details>

### wagtail-localize

Translation plugin for Wagtail CMS

`pip install wagtail-localize` · installs (wheel) · licence: BSD-3-Clause · rank 14012 · last release 2026-08-19 · [PyPI](https://pypi.org/project/wagtail-localize/) · [docs](https://wagtail-localize.org) · [source](https://github.com/wagtail/wagtail-localize)

<details><summary>README extract</summary>

<!--content-start-->

Wagtail Localize is a translation plugin for the Wagtail CMS. It allows pages or snippets to be translated within Wagtail's admin interface. It also provides integrations with external translations services such as Pontoon or DeepL, and importing/exporting translations with PO files.

Documentation
Changelog ...

Sections: Wagtail localize, Requirements, Using pip, Using flit, pre-commit, How to run tests, Thanks

</details>

### wsaccel

Accelerator for ws4py and AutobahnPython

`pip install wsaccel` · installs from source (sdist only) · licence: Apache 2.0 · rank 14092 · last release 2024-10-10 · [PyPI](https://pypi.org/project/wsaccel/)

<details><summary>README extract</summary>

NOTE: AutobahnPython and ws4py are not actively maintained. So I will stop this project too.
Please migrate to Tornado or
websockets.

WSAccell is WebSocket accelerator for AutobahnPython,
and ws4py.

WSAccell replaces per-byte process in them with Cython version.

AutobahnPython beginning with version 0.6 automatically uses WSAccell if available. ...

Example:
```python
import wsaccel
wsaccel.patch_autobahn()  # for autobahn.
wsaccel.patch_ws4py()     # for ws4py.
```

Sections: WSAccell, test

</details>

### winrt-Windows.Storage

PyWinRT projection of the Windows.Storage namespace

`pip install winrt-Windows.Storage` · installs (wheel) · licence: MIT · rank 14100 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Storage/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Storage` namespace.

This package provides the `winrt.windows.storage` module.

The WinRT APIs in it are those of version 10.0.28000.2957 of the
`Microsoft.Windows.SDK.CPP` NuGet package. ...

</details>

### witan

Witan spreadsheet CLI and Python SDK for coding agents

`pip install witan` · installs (wheel) · licence: Apache-2.0 · rank 14112 · last release 2026-07-17 · [PyPI](https://pypi.org/project/witan/)

<details><summary>README extract</summary>

The Office toolkit for coding agents — edit, render, calculate, and lint Excel workbooks, plus render, script, and lint PPTX files.

Documentation | How we built it

Example:
```python
from witan import Workbook

with Workbook("report.xlsx") as wb:
    sheets = wb.list_sheets()
    tsv = wb.read_range_tsv("Summary!A1:F20")
```

Sections: witan-cli, From PyPI, From npm, From Source, Quick Start, What This CLI Covers, Auth, Config, and Modes, CI

</details>

### windmill-api

A client library for accessing Windmill API

`pip install windmill-api` · installs (wheel) · licence: Apache Software License · rank 14190 · last release 2026-11-06 · [PyPI](https://pypi.org/project/windmill-api/)

<details><summary>README extract</summary>

This is the raw autogenerated api client. You are most likely more interested in wmill which leverages this client to offer an user friendly experience. We use this openapi python client generator

A client library for accessing Windmill API

Example:
```python
from windmill_api import Client

client = Client(base_url="
```

Sections: Autogenerated Windmill OpenApi Client, windmill-api, Usage, Advanced customizations

</details>

### whylabs-client

WhyLabs API client

`pip install whylabs-client` · installs (wheel) · licence: Apache License 2.0 · rank 14288 · last release 2025-01-13 · [PyPI](https://pypi.org/project/whylabs-client/)

<details><summary>README extract</summary>

WhyLabs API that enables end-to-end AI observability

This Python package is automatically generated by the OpenAPI Generator project:

- API version: 0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
 For more information, please visit

Python >= 3.6

Example:
```python
import time
import whylabs_client
from pprint import pprint
from whylabs_client.api import dataset_profile_api
from whylabs_client.model.delete_analyzer_results_response import DeleteAnalyzerResultsResponse
from whylabs_client.model.delete_dataset_profiles_response import DeleteDatasetProfilesResponse
...
```

Sections: whylabs-client, Requirements., Setuptools, Getting Started

</details>

### winrt-Windows.Media.Control

PyWinRT projection of the Windows.Media.Control namespace

`pip install winrt-Windows.Media.Control` · installs (wheel) · licence: MIT · rank 14658 · last release 2026-10-31 · [PyPI](https://pypi.org/project/winrt-Windows.Media.Control/) · [docs](https://pywinrt.readthedocs.io) · [source](https://github.com/pywinrt/pywinrt)

<details><summary>README extract</summary>

<!-- warning: Please don't edit this file. It was automatically generated. -->

Windows Runtime (WinRT) APIs for the `Windows.Media.Control` namespace.

This package provides the `winrt.windows.media.control` module.

The WinRT APIs in it are those of version 10.0.28000.2957 of the
`Microsoft.Windows.SDK.CPP` NuGet package. ...

</details>

### webull-openapi-python-sdk

Webull Python SDK.

`pip install webull-openapi-python-sdk` · installs (wheel) · licence: Apache License 2.0 · rank 14682 · last release 2026-10-17 · [PyPI](https://pypi.org/project/webull-openapi-python-sdk/)

