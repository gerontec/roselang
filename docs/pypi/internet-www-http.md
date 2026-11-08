# Internet / WWW/HTTP (part 1 of 2)

[Index](README.md) · 607 packages in this topic, 86 more listed under another topic, by downloads.

part 1 · [part 2](internet-www-http-2.md)

### urllib3

HTTP library with thread-safe connection pooling, file post, and more.

`pip install urllib3` · installs (wheel) · licence: MIT · rank 6 · last release 2026-09-15 · [PyPI](https://pypi.org/project/urllib3/) · [docs](https://urllib3.readthedocs.io) · [source](https://github.com/urllib3/urllib3)

<details><summary>README extract</summary>

urllib3 is a powerful, *user-friendly* HTTP client for Python.
urllib3 brings many critical features that are missing from the Python
standard libraries:

- Thread safety.
- Connection pooling.
- Client-side SSL/TLS verification.
- File uploads with multipart encoding.
- Helpers for retrying requests and dealing with HTTP redirects. ...

Example:
```python
>>> import urllib3
>>> resp = urllib3.request("GET", "
>>> resp.status
200
>>> resp.data
b"User-agent: *\nDisallow: /deny\n"
```

Sections: Getting Started, For Enterprise

</details>

### requests

Python HTTP for Humans.

`pip install requests` · installs (wheel) · licence: Apache Software License · rank 8 · last release 2026-05-14 · [PyPI](https://pypi.org/project/requests/) · [docs](https://requests.readthedocs.io) · [source](https://github.com/psf/requests)

<details><summary>README extract</summary>

Requests is a simple, yet elegant, HTTP library.

Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your `PUT` & `POST` data — but nowadays, just use the `json` method! ...

Example:
```python
>>> import requests
>>> r = requests.get(' auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"authenticated": true, ...'
>>> r.json()
{'authenticated': True, ...}
```

Sections: Requests, Cloning the repository

</details>

### h11

A pure-Python, bring-your-own-I/O implementation of HTTP/1.1

`pip install h11` · installs (wheel) · licence: MIT License · rank 28 · last release 2025-04-24 · [PyPI](https://pypi.org/project/h11/)

<details><summary>README extract</summary>

This is a little HTTP/1.1 library written from scratch in Python,
heavily inspired by hyper-h2.

It's a "bring-your-own-I/O" library; h11 contains no IO code
whatsoever. This means you can hook h11 up to your favorite network
API, and that could be anything you want: synchronous, threaded,
asynchronous, or your own implementation of RFC 6214 -- ...

Sections: h11, FAQ

</details>

### MarkupSafe

Safely add untrusted strings to HTML/XML markup.

`pip install MarkupSafe` · installs (wheel) · licence: BSD-3-Clause · rank 30 · last release 2026-10-02 · [PyPI](https://pypi.org/project/MarkupSafe/) · [docs](https://markupsafe.palletsprojects.com/) · [source](https://github.com/pallets/markupsafe/)

<details><summary>README extract</summary>

MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are
replaced so that they display as the actual characters. This mitigates
injection attacks, meaning untrusted user input can safely be displayed
on a page.

Example:
```python
>>> from markupsafe import Markup, escape

>>> # escape replaces special characters and wraps in Markup
>>> escape("alert(document.cookie);")
Markup('<script>alert(document.cookie);</script>')

>>> # wrap in Markup to mark text "safe" and prevent escaping
>>> Markup("Hello")
Markup('hello')

>>> escape(Markup("Hello"))
Markup('hello')

...
```

Sections: MarkupSafe, Examples

</details>

### httpx

The next generation HTTP client.

`pip install httpx` · installs (wheel) · licence: BSD License · rank 31 · last release 2024-12-06 · [PyPI](https://pypi.org/project/httpx/) · [docs](https://www.python-httpx.org) · [source](https://github.com/encode/httpx)

<details><summary>README extract</summary>

HTTPX - A next-generation HTTP client for Python.

HTTPX is a fully featured HTTP client library for Python 3. It includes an integrated command line client, has support for both HTTP/1.1 and HTTP/2, and provides both sync and async APIs.

Install HTTPX using pip:

Now, let's get started:

Or, using the command-line client. ...

Features:
HTTPX builds on the well-established usability of `requests`, and gives you:

* A broadly requests-compatible API.
* An integrated command-line client.
* HTTP/1.1 and HTTP/2 support. ...

Example:
```python
>>> import httpx
>>> r = httpx.get('
>>> r

>>> r.status_code
200
>>> r.headers['content-type']
'text/html; charset=UTF-8'
>>> r.text
'<!doctype html>\n\n\nExample Domain...'
```

Sections: Features, Documentation, Dependencies, Fixed

</details>

### httpcore

A minimal low-level HTTP client.

`pip install httpcore` · installs (wheel) · licence: BSD-3-Clause · rank 32 · last release 2025-04-24 · [PyPI](https://pypi.org/project/httpcore/) · [docs](https://www.encode.io/httpcore) · [source](https://github.com/encode/httpcore)

<details><summary>README extract</summary>

> *Do one thing, and do it well.*

The HTTP Core package provides a minimal low-level HTTP client, which does
one thing only. Sending HTTP requests.

It does not provide any high level model abstractions over the API,
does not handle redirects, multipart uploads, building authentication headers,
transparent HTTP caching, URL parsing, session ...

Example:
```python
import httpcore

response = httpcore.request("GET", "

print(response)
# <Response [200]>
print(response.status)
# 200
print(response.headers)
# [(b'Accept-Ranges', b'bytes'), (b'Age', b'557328'), (b'Cache-Control', b'max-age=604800'), ...]
print(response.content)
...
```

...

</details>

### Jinja2

A very fast and expressive template engine.

`pip install Jinja2` · installs (wheel) · licence: BSD License · rank 37 · last release 2025-03-05 · [PyPI](https://pypi.org/project/Jinja2/) · [docs](https://jinja.palletsprojects.com/) · [source](https://github.com/pallets/jinja/)

<details><summary>README extract</summary>

Jinja is a fast, expressive, extensible templating engine. Special
placeholders in the template allow writing code similar to Python
syntax. Then the template is passed data to render the final document.

It includes:

- Template inheritance and inclusion.
- Define and import macros within templates. ...

Sections: Jinja, In A Nutshell

</details>

### starlette

The little ASGI library that shines.

`pip install starlette` · installs (wheel) · licence: BSD-3-Clause · rank 40 · last release 2026-10-24 · [PyPI](https://pypi.org/project/starlette/) · [docs](https://starlette.dev/) · [source](https://github.com/Kludex/starlette)

<details><summary>README extract</summary>

✨ The little ASGI framework that shines. ✨

Documentation:

Source Code:

Starlette is a lightweight ASGI framework/toolkit,
which is ideal for building async web services in Python.

It is production-ready, and gives you the following:

* A lightweight, low-complexity HTTP web framework.
* WebSocket support.
* In-process background tasks. ...

Example:
```python
from starlette.responses import PlainTextResponse

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, world!')
    await response(scope, receive, send)
```

Sections: Starlette, Example, Dependencies, Framework or Toolkit, Modularity

</details>

### uvicorn

The lightning-fast ASGI server.

`pip install uvicorn` · installs (wheel) · licence: BSD-3-Clause · rank 44 · last release 2026-09-25 · [PyPI](https://pypi.org/project/uvicorn/) · [source](https://github.com/Kludex/uvicorn)

<details><summary>README extract</summary>

An ASGI web server, for Python.

Documentation:

Source Code:

Uvicorn is an ASGI web server implementation for Python.

Until recently Python has lacked a minimal low-level server/application interface for
async frameworks. ...

Features:
Most well established Python Web frameworks started out as WSGI-based frameworks.

WSGI applications are a single, synchronous callable that takes a request and returns a response. ...

Example:
```python
async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            (b'content-type', b'text/plain'),
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })
```

...

</details>

### aiohttp

Async http client/server framework (asyncio)

`pip install aiohttp` · installs (wheel) · licence: Apache-2.0 AND MIT · rank 58 · last release 2026-10-11 · [PyPI](https://pypi.org/project/aiohttp/)

<details><summary>README extract</summary>

Features:
- Supports both client and server side of HTTP protocol.
- Supports both client and server Web-Sockets out-of-the-box and avoids
 Callback Hell.
- Provides Web-server with middleware and pluggable routing.

Example:
```python
import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get(' as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")
...
```

Sections: Async http client/server framework, Key Features, Getting started, Client, Server, Documentation, Demos, External links, Communication channels, Requirements, Keepsafe, Source code, Benchmarks

</details>

### yarl

Yet another URL library

`pip install yarl` · installs (wheel) · licence: Apache-2.0 · rank 59 · last release 2026-09-15 · [PyPI](https://pypi.org/project/yarl/)

<details><summary>README extract</summary>

The module provides handy URL class for URL parsing and changing.

Url is constructed from `str`:

All url parts: *scheme*, *user*, *password*, *host*, *port*, *path*,

All url manipulations produce a new url object:

Strings passed to constructor and modification methods are
automatically encoded giving canonical representation as result: ...

Features:
There is no standard for boolean representation of boolean values.

Some systems prefer `true`/`false`, others like `yes`/`no`, `on`/`off`,
`Y`/`N`, `1`/`0`, etc. ...

Example:
```python
>>> from yarl import URL
>>> url = URL('
>>> url
URL('
```

...

</details>

### propcache

Accelerated property cache

`pip install propcache` · installs (wheel) · licence: Apache-2.0 · rank 61 · last release 2026-09-16 · [PyPI](https://pypi.org/project/propcache/)

<details><summary>README extract</summary>

The module provides a fast implementation of cached properties for Python 3.10+.

The API is designed to be nearly identical to the built-in `functools.cached_property` class,
except for the additional `under_cached_property` class which uses `self._cache`
instead of `self.dict to store the cached values and prevents _set__` from being called. ...

Features:
- Added support for newer type hints and remove `Optional` and `Union` from all annotations
 -- by @Vizonex

 *Related issues and pull requests on GitHub:*
 #193.

Sections: propcache, Introduction, API documentation, Source code, Discussion list, 0.5.4, Packaging updates and notes for downstreams, 0.5.3, Bug fixes, Removals and backward incompatible breaking changes, Improved documentation, 0.5.2, 0.5.1

</details>

### google-auth

Google Authentication Library

`pip install google-auth` · installs (wheel) · licence: Apache Software License · rank 77 · last release 2026-11-03 · [PyPI](https://pypi.org/project/google-auth/)

<details><summary>README extract</summary>

This library simplifies using Google's various server-to-server authentication
mechanisms to access Google APIs.

Sections: Google Auth Python Library, Extras, Documentation

</details>

### httpx2

The next generation HTTP client.

`pip install httpx2` · installs (wheel) · licence: BSD-3-Clause · rank 98 · last release 2026-10-21 · [PyPI](https://pypi.org/project/httpx2/) · [source](https://github.com/pydantic/httpx2)

<details><summary>README extract</summary>

A next-generation HTTP client for Python.

HTTPX2 is a fully featured HTTP client library for Python. It includes an integrated command line client, has support for both HTTP/1.1 and HTTP/2, and provides both sync and async APIs.

> [!NOTE]
> HTTPX2 is a continuation of the wonderful work started by @lovelydinosaur and the broader HTTPX community. ...

Features:
HTTPX2 builds on the well-established usability of `requests`, and gives you:

* A broadly requests-compatible API.
* An integrated command-line client.
* HTTP/1.1 and HTTP/2 support. ...

Example:
```python
>>> import httpx2
>>> r = httpx2.get('
>>> r

>>> r.status_code
200
>>> r.headers['content-type']
'text/html; charset=UTF-8'
>>> r.text
'<!doctype html>\n\n\nExample Domain...'
```

...

</details>

### httpcore2

A minimal low-level HTTP client.

`pip install httpcore2` · installs (wheel) · licence: BSD-3-Clause · rank 100 · last release 2026-10-21 · [PyPI](https://pypi.org/project/httpcore2/) · [source](https://github.com/pydantic/httpx2/blob/main/src/httpcore2)

<details><summary>README extract</summary>

> *Do one thing, and do it well.*

The HTTPCore 2 package provides a minimal low-level HTTP client, which does
one thing only. Sending HTTP requests.

It does not provide any high level model abstractions over the API,
does not handle redirects, multipart uploads, building authentication headers,
transparent HTTP caching, URL parsing, session ...

Example:
```python
import httpcore2

response = httpcore2.request("GET", "

print(response)
# <Response [200]>
print(response.status)
# 200
print(response.headers)
# [(b'Accept-Ranges', b'bytes'), (b'Age', b'557328'), (b'Cache-Control', b'max-age=604800'), ...]
print(response.content)
...
```

...

</details>

### soupsieve

A modern CSS selector implementation for Beautiful Soup.

`pip install soupsieve` · installs (wheel) · licence: MIT · rank 105 · last release 2026-11-04 · [PyPI](https://pypi.org/project/soupsieve/)

<details><summary>README extract</summary>

[][donate-link]
[][codecov-link]
[][pypi-link]
[][pypi-link]
[][pypi-link]
[][license-link]

Features:
Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4. It aims to provide selecting,
matching, and filtering using modern CSS selectors. ...

Sections: Soup Sieve, Overview, Documentation

</details>

### sse-starlette

SSE plugin for Starlette

`pip install sse-starlette` · installs (wheel) · licence: BSD-3-Clause · rank 112 · last release 2026-11-07 · [PyPI](https://pypi.org/project/sse-starlette/) · [source](https://github.com/sysid/sse-starlette)

<details><summary>README extract</summary>

[][pypi-url]
[][build-url]

> Background:

Production ready Server-Sent Events implementation for Starlette and FastAPI following the W3C SSE specification.

Example:
```python
import asyncio
from starlette.applications import Starlette
from starlette.routing import Route
from sse_starlette import EventSourceResponse

async def generate_events():
    for i in range(10):
        yield {"data": f"Event {i}"}
        await asyncio.sleep(1)

async def sse_endpoint(request):
    return EventSourceResponse(generate_events())

...
```

...

</details>

### Werkzeug

The comprehensive WSGI web application library.

`pip install Werkzeug` · installs (wheel) · licence: BSD-3-Clause · rank 132 · last release 2026-09-27 · [PyPI](https://pypi.org/project/Werkzeug/) · [docs](https://werkzeug.palletsprojects.com/) · [source](https://github.com/pallets/werkzeug/)

<details><summary>README extract</summary>

*werkzeug* German noun: "tool". Etymology: *werk* ("work"), *zeug* ("stuff")

Werkzeug is a comprehensive WSGI web application library. It began as
a simple collection of various utilities for WSGI applications and has
become one of the most advanced WSGI utility libraries.

It includes: ...

Example:
```python
# save this as app.py
from werkzeug.wrappers import Request, Response

@Request.application
def application(request: Request) -> Response:
    return Response("Hello, World!")

if name == "main":
    from werkzeug.serving import run_simple

    run_simple("127.0.0.1", 5000, application)
```

Sections: Werkzeug, A Simple Example

</details>

### Mako

A super-fast templating language that borrows the best ideas from the existing templating languages.

`pip install Mako` · installs (wheel) · licence: MIT · rank 149 · last release 2026-09-22 · [PyPI](https://pypi.org/project/Mako/) · [docs](https://docs.makotemplates.org)

<details><summary>README extract</summary>

Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. ...

Example:
```python
<%inherit file="base.html"/>
<%
    rows = [[v for v in range(0,10)] for row in range(0,10)]
%>
<table>
    % for row in rows:
        ${makerow(row)}
    % endfor
</table>

<%def name="makerow(row)">
    <tr>
    % for name in row:
        <td>${name}</td>\
    % endfor
    </tr>
</%def>
```

Sections: Mako Templates for Python, Nutshell, Philosophy, Documentation

</details>

### Flask

A simple framework for building complex web applications.

`pip install Flask` · installs (wheel) · licence: BSD-3-Clause · rank 162 · last release 2026-02-19 · [PyPI](https://pypi.org/project/Flask/) · [docs](https://flask.palletsprojects.com/) · [source](https://github.com/pallets/flask/)

<details><summary>README extract</summary>

Flask is a lightweight [WSGI] web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around [Werkzeug]
and [Jinja], and has become one of the most popular Python web
application frameworks. ...

Example:
```python
# save this as app.py
from flask import Flask

app = Flask(name)

@app.route("/")
def hello():
    return "Hello, World!"
```

Sections: Flask, A Simple Example

</details>

### backoff

Function decoration for backoff and retry

`pip install backoff` · installs (wheel) · licence: MIT License · rank 224 · last release 2022-10-05 · [PyPI](https://pypi.org/project/backoff/) · [source](https://github.com/litl/backoff)

<details><summary>README extract</summary>

Function decoration for backoff and retry

This module provides function decorators which can be used to wrap a
function such that it will be retried until some condition is met. It
is meant to be of use when accessing unreliable resources with the
potential for intermittent failures i.e. network resources and external
APIs. ...

Example:
```python
@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException)
def get_url(url):
    return requests.get(url)
```

Sections: backoff, Examples, @backoff.on_exception, ...

</details>

### asgiref

ASGI specs, helper code, and adapters

`pip install asgiref` · installs (wheel) · licence: BSD-3-Clause · rank 225 · last release 2026-10-23 · [PyPI](https://pypi.org/project/asgiref/) · [docs](https://asgi.readthedocs.io/)

<details><summary>README extract</summary>

ASGI is a standard for Python asynchronous web apps and servers to communicate
with each other, and positioned as an asynchronous successor to WSGI. You can
read more at

This package includes ASGI base libraries, such as: ...

Example:
```python
class ASGIHandler(...):
    ...

    async def call(...):
        ...

        async with ThreadSensitiveContext():
            await self.handle(...)
```

Sections: asgiref, Function wrappers, Thread-sensitive contexts, Threadlocal replacement, Server base classes, WSGI-to-ASGI adapter, Dependencies, Building the documentation, Releasing, Implementation Details, Synchronous code & threads

</details>

### webencodings

Character encoding aliases for legacy web content

`pip install webencodings` · installs (wheel) · licence: BSD License · rank 233 · last release 2026-08-15 · [PyPI](https://pypi.org/project/webencodings/) · [docs](https://doc.courtbouillon.org/webencodings) · [source](https://github.com/CourtBouillon/webencodings)

<details><summary>README extract</summary>

webencodings is a Python implementation of the WHATWG Encoding standard.

In order to be compatible with legacy web content when interpreting something like
`Content-Type: text/html; charset=latin1`, tools need to use a particular set of
aliases for encoding labels as well as some overriding rules. ...

</details>

### google-api-python-client

Google API Client Library for Python

`pip install google-api-python-client` · installs (wheel) · licence: Apache Software License · rank 238 · last release 2026-09-30 · [PyPI](https://pypi.org/project/google-api-python-client/)

<details><summary>README extract</summary>

This is the Google API Python client library
for Google's discovery based APIs. To get started, please see the
docs folder.

This library is considered complete and is in maintenance mode. This means
that we will address critical bugs and security issues but will not add any
new features.

This library is officially supported by Google. ...

Sections: Google API Client, Documentation, Other Google API libraries, Mac/Linux, Windows, Third Party Libraries and Dependencies

</details>

### google-auth-httplib2

Google Authentication Library: httplib2 transport

`pip install google-auth-httplib2` · installs (wheel) · licence: Apache Software License · rank 242 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-auth-httplib2/)

<details><summary>README extract</summary>

The library was created to help clients migrate from oauth2client to google-auth, however this library is no longer maintained. For any new usages please see provided transport layers by google-auth library.

httplib2 Transport for Google Auth Documentation

This library provides an httplib2 transport for google-auth.

Sections: `httplib2` Transport for Google Auth, Documentation, Introduction

</details>

### httplib2

A comprehensive HTTP client library.

`pip install httplib2` · installs (wheel) · licence: MIT License · rank 245 · last release 2026-10-28 · [PyPI](https://pypi.org/project/httplib2/)

<details><summary>README extract</summary>

A comprehensive HTTP client library, ``httplib2`` supports many features left out of other HTTP libraries.

HTTP and HTTPS
 HTTPS support is only available if the socket module was compiled with SSL support.

Keep-Alive
 Supports HTTP 1.1 Keep-Alive, keeping the socket open and performing multiple requests over the same connection if possible. ...

</details>

### Authlib

The ultimate Python library in building OAuth and OpenID Connect servers and clients.

`pip install Authlib` · installs (wheel) · licence: BSD License · rank 248 · last release 2026-11-05 · [PyPI](https://pypi.org/project/Authlib/) · [docs](https://docs.authlib.org/) · [source](https://github.com/authlib/authlib)

<details><summary>README extract</summary>

The ultimate Python library in building OAuth and OpenID Connect servers.
JWS, JWK, JWA, JWT are included.

Authlib is compatible with Python3.10+.

Authlib will deprecate `authlib.jose` module, please read:

- Migrating from `authlib.jose` to `joserfc`

Features:
Generic, spec-compliant implementation to build clients and providers:

- The OAuth 1.0 Protocol
 - RFC5849: The OAuth 1.0 Protocol ...

Sections: Migrations, Features, Useful Links

</details>

### playwright

A high-level API to automate web browsers

`pip install playwright` · installs (wheel) · licence: Apache-2.0 · rank 253 · last release 2026-10-22 · [PyPI](https://pypi.org/project/playwright/)

<details><summary>README extract</summary>

Playwright is a Python library to automate Chromium, Firefox and WebKit browsers with a single API. Playwright delivers automation that is ever-green, capable, reliable and fast. See how Playwright is better.

| | Linux | macOS | Windows | ...

Example:
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto('
        page.screenshot(path=f'example-{browser_type.name}.png')
        browser.close()
```

Sections: 🎭 Playwright for Python, Documentation, API Reference, Example, Other languages

</details>

### google-auth-oauthlib

Google Authentication Library

`pip install google-auth-oauthlib` · installs (wheel) · licence: Apache Software License · rank 255 · last release 2026-09-29 · [PyPI](https://pypi.org/project/google-auth-oauthlib/)

<details><summary>README extract</summary>

This library provides oauthlib integration with google-auth.

Sections: oauthlib integration for Google Auth, Documentation

</details>

### CacheControl

httplib2 caching for requests

`pip install CacheControl` · installs (wheel) · licence: Apache-2.0 · rank 297 · last release 2025-11-14 · [PyPI](https://pypi.org/project/CacheControl/) · [source](https://github.com/psf/cachecontrol)

<details><summary>README extract</summary>

CacheControl is a port of the caching algorithms in httplib2 for use with
requests session object.

It was written because httplib2's better support for caching is often
mitigated by its lack of thread safety. The same is true of requests in
terms of caching.

Example:
```python
import requests

from cachecontrol import CacheControl

sess = requests.session()
cached_sess = CacheControl(sess)

response = cached_sess.get('
```

Sections: CacheControl, Quickstart

</details>

### cssselect2

CSS selectors for Python ElementTree

`pip install cssselect2` · installs (wheel) · licence: BSD License · rank 417 · last release 2026-08-31 · [PyPI](https://pypi.org/project/cssselect2/) · [docs](https://doc.courtbouillon.org/cssselect2/) · [source](https://github.com/Kozea/cssselect2/)

<details><summary>README extract</summary>

cssselect2 is a straightforward implementation of CSS4 Selectors for markup
documents (HTML, XML, etc.) that can be read by ElementTree-like parsers
(including cElementTree, lxml, html5lib, etc.)

* Free software: BSD license
* For Python 3.10+, tested on CPython and PyPy ...

</details>

### requests-aws4auth

AWS4 authentication for Requests

`pip install requests-aws4auth` · installs (wheel) · licence: MIT License · rank 434 · last release 2026-10-09 · [PyPI](https://pypi.org/project/requests-aws4auth/)

<details><summary>README extract</summary>

Amazon Web Services version 4 authentication for the Python Requests library.

Features:
- Requests authentication for all AWS services that support AWS auth v4
- Independent signing key objects
- Automatic regeneration of keys when scope date boundary is passed
- Support for STS temporary credentials ...

Sections: Features, Python versions, Behaviour changes in 0.8, Basic usage, STS Temporary Credentials, Date handling, Automatic key regeneration, Secret key storage, Multithreading, API reference, 1.4.0 (2026-10-09), 1.3.2 (2026-05-01), 1.3.1 (2024-07-21), 1.3.0 (2024-07-21)

</details>

### grpclib

Pure-Python gRPC implementation for asyncio

`pip install grpclib` · installs (wheel) · licence: BSD License · rank 447 · last release 2025-12-14 · [PyPI](https://pypi.org/project/grpclib/)

<details><summary>README extract</summary>

This project is based on hyper-h2 and requires Python >= 3.10.

Example:
```python
import asyncio

from grpclib.client import Channel

# generated by protoc
from .helloworld_pb2 import HelloRequest, HelloReply
from .helloworld_grpc import GreeterStub

async def main():
    async with Channel('127.0.0.1', 50051) as channel:
        greeter = GreeterStub(channel)

...
```

Sections: Pure-Python gRPC implementation for asyncio, Example, Client, Server

</details>

### Django

A high-level Python web framework that encourages rapid development and clean, pragmatic design.

`pip install Django` · installs (wheel) · licence: BSD-3-Clause · rank 466 · last release 2026-11-03 · [PyPI](https://pypi.org/project/Django/) · [docs](https://docs.djangoproject.com/) · [source](https://github.com/django/django)

<details><summary>README extract</summary>

Django is a high-level Python web framework that encourages rapid development
and clean, pragmatic design. Thanks for checking it out.

All documentation is in the "`docs`" directory and online at
 If you're just getting started,
here's how we recommend you read the docs: ...

</details>

### weasyprint

The Awesome Document Factory

`pip install weasyprint` · installs (wheel) · licence: BSD License · rank 540 · last release 2026-09-08 · [PyPI](https://pypi.org/project/weasyprint/) · [docs](https://doc.courtbouillon.org/weasyprint/) · [source](https://github.com/Kozea/WeasyPrint)

<details><summary>README extract</summary>

The Awesome Document Factory

WeasyPrint is a smart solution helping web developers to create PDF
documents. It turns simple HTML pages into gorgeous statistical reports,
invoices, tickets…

From a technical point of view, WeasyPrint is a visual rendering engine for
HTML and CSS that can export to PDF. ...

</details>

### djangorestframework

Web APIs for Django, made easy.

`pip install djangorestframework` · installs (wheel) · licence: BSD-3-Clause · rank 678 · last release 2026-10-06 · [PyPI](https://pypi.org/project/djangorestframework/) · [source](https://github.com/encode/django-rest-framework)

<details><summary>README extract</summary>

[![build-status-image]][build-status]
[![coverage-status-image]][codecov]
[![pypi-version]][pypi]

Awesome web-browsable Web APIs.

Full documentation for the project is available at

Features:
Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:

* The Web browsable API is a huge usability win for your developers. ...

Example:
```python
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]

...
```

...

</details>

### oauth2client

OAuth 2.0 client library

`pip install oauth2client` · installs (wheel) · licence: Apache Software License · rank 700 · last release 2018-09-07 · [PyPI](https://pypi.org/project/oauth2client/)

<details><summary>README extract</summary>

oauth2client is a client library for OAuth 2.0.

Note: oauth2client is now deprecated. No more features will be added to the
 libraries and the core team is turning down support. We recommend you use
 `google-auth < and
 `oauthlib <

</details>

### pymdown-extensions

Extension pack for Python Markdown.

`pip install pymdown-extensions` · installs (wheel) · licence: MIT · rank 767 · last release 2026-10-14 · [PyPI](https://pypi.org/project/pymdown-extensions/)

<details><summary>README extract</summary>

[][donate-link]
[][codecov-link]
[][pypi-link]
[][pypi-link]
[][pypi-link]
[][license-link]

Extensions for Python Markdown.

Extension documentation is found here:

Sections: PyMdown Extensions, Documentation

</details>

### jsonconversion

This python module helps converting arbitrary Python objects into JSON strings and back.

`pip install jsonconversion` · installs (wheel) · licence: BSD License · rank 790 · last release 2026-10-16 · [PyPI](https://pypi.org/project/jsonconversion/)

<details><summary>README extract</summary>

This python module helps converting arbitrary Python objects into JSON
strings and back. It extends the basic features of the `JSONEncoder` and
`JSONDecoder` classes provided by the native `json` package, making it possible to preserve object information when saving data and reconstructing it later. ...

Example:
```python
import json

from jsonconversion.decoder import JSONObjectDecoder
from jsonconversion.encoder import JSONObjectEncoder

var = (1, 2, 3)  # variable to be serialized

allowed_classes = {
    "my_package.models.ExampleObject": ExampleObject,
}

allowed_types = {"int": int, "tuple": tuple,}

...
```

...

</details>

### ua-parser

Python port of Browserscope's user agent parser

`pip install ua-parser` · installs (wheel) · licence: Apache-2.0 · rank 796 · last release 2026-04-05 · [PyPI](https://pypi.org/project/ua-parser/) · [docs](https://uap-python.readthedocs.io) · [source](https://github.com/ua-parser/uap-python)

<details><summary>README extract</summary>

Official python implementation of the User Agent String
Parser project.

Example:
```python
>>> from ua_parser import parse
>>> ua_string = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36'
>>> parse(ua_string) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
Result(user_agent=UserAgent(family='Chrome',
                            major='41',
...
```

Sections: uap-python, Quick Start, Retrieve all data on a user-agent string, Extract only browser data from user-agent string, Extract OS information from user-agent string, Extract device information from user-agent string, Upgrading

</details>

### emoji

Emoji for Python

`pip install emoji` · installs (wheel) · licence: BSD License · rank 817 · last release 2026-09-16 · [PyPI](https://pypi.org/project/emoji/) · [source](https://github.com/carpedm20/emoji/)

<details><summary>README extract</summary>

Emoji for Python. This project was inspired by kyokomi.

Example:
```python
>>> import emoji
>>> print(emoji.emojize('Python is :thumbs_up:'))
Python is 👍
>>> print(emoji.emojize('Python is :thumbsup:', language='alias'))
Python is 👍
>>> print(emoji.demojize('Python is 👍'))
Python is :thumbs_up:
>>> print(emoji.emojize("Python is fun :red_heart:"))
Python is fun ❤
...
```

Sections: Emoji, Example, Links

</details>

### vcrpy

Automatically mock your HTTP interactions to simplify and speed up testing

`pip install vcrpy` · installs (wheel) · licence: MIT License · rank 818 · last release 2026-11-02 · [PyPI](https://pypi.org/project/vcrpy/)

<details><summary>README extract</summary>

This is a Python version of Ruby's VCR
library.

Source code

Documentation

VCR.py simplifies and speeds up tests that make HTTP requests. The
first time you run code that is inside a VCR.py context manager or
decorated function, VCR.py records all HTTP interactions that take
place through the libraries it supports and serializes and writes ...

Sections: VCR.py 📼, Rationale, Usage with Pytest

</details>

### simple-salesforce

A basic Salesforce.com REST API client.

`pip install simple-salesforce` · installs (wheel) · licence: Apache-2.0 · rank 830 · last release 2026-07-08 · [PyPI](https://pypi.org/project/simple-salesforce/) · [docs](https://simple-salesforce.readthedocs.io/) · [source](https://github.com/simple-salesforce/simple-salesforce.git)

<details><summary>README extract</summary>

Simple Salesforce is a basic Salesforce.com REST API client built for Python 3.9, 3.10, 3.11, 3.12, and 3.13. The goal is to provide a very low-level interface to the REST Resource and APEX API, returning a dictionary of the API JSON response. ...

Example:
```python
from simple_salesforce import Salesforce
sf = Salesforce(instance='na1.salesforce.com', session_id='')
```

Sections: Simple Salesforce, Documentation, Examples, Record Management, Queries, CRUD Metadata API Calls, File Based Metadata API Calls, Other Options, Using Bulk, Using Bulk 2.0, Using Apex, Additional Features, Helpful Datetime Resources, Helpful Pandas Resources

</details>

### ua-parser-builtins

Precompiled rules for User Agent Parser

`pip install ua-parser-builtins` · installs (wheel) · licence: Apache Software License · rank 846 · last release 2026-10-02 · [PyPI](https://pypi.org/project/ua-parser-builtins/) · [source](https://github.com/ua-parser/uap-python)

<details><summary>README extract</summary>

This project does not do anything on its own, nor does it have any
actual API: it contains the dataset of [uap-core] pre-compiled for use
by [ua-parser] to decrease
initialisation times.

The precompiled ruleset is released monthly based on whatever
[uap-core]'s default branch is at that moment. ...

</details>

### jira

Python library for interacting with JIRA via REST APIs.

`pip install jira` · installs (wheel) · licence: BSD License · rank 864 · last release 2025-07-28 · [PyPI](https://pypi.org/project/jira/) · [docs](https://jira.readthedocs.io) · [source](https://github.com/pycontribs/jira.git)

<details><summary>README extract</summary>

This library eases the use of the Jira REST API from Python and it has been used in production for years.

As this is an open-source project that is community maintained, do not be surprised if some bugs or features are not implemented quickly enough.

Example:
```python
from jira import JIRA

jira = JIRA('

issue = jira.issue('JRA-9')
print(issue.fields.project.key)            # 'JRA'
print(issue.fields.issuetype.name)         # 'New Feature'
print(issue.fields.reporter.displayName)   # 'Mike Cannon-Brookes [Atlassian]'
```

Sections: Jira Python Library, Quickstart, Usage, Setup, Automatic (VS Code), Manual, tox envs, Jira REST API Reference Links

</details>

### whitenoise

Radically simplified static file serving for WSGI applications

`pip install whitenoise` · installs (wheel) · licence: MIT · rank 873 · last release 2026-02-27 · [PyPI](https://pypi.org/project/whitenoise/) · [docs](https://whitenoise.readthedocs.io/) · [source](https://github.com/evansd/whitenoise)

<details><summary>README extract</summary>

Radically simplified static file serving for Python web apps

With a couple of lines of config WhiteNoise allows your web app to serve its
own static files, making it a self-contained unit that can be deployed anywhere
without relying on nginx, Amazon S3 or any other external service. ...

</details>

### Flask-Login

User authentication and session management for Flask.

`pip install Flask-Login` · installs (wheel) · licence: MIT License · rank 894 · last release 2023-10-30 · [PyPI](https://pypi.org/project/Flask-Login/) · [docs](https://flask-login.readthedocs.io/) · [source](https://github.com/maxcountryman/flask-login)

<details><summary>README extract</summary>

Flask-Login provides user session management for Flask. It handles the common
tasks of logging in, logging out, and remembering your users' sessions over
extended periods of time.

Flask-Login is not bound to any particular database system or permissions
model. ...

Example:
```python
import flask

app = flask.Flask(name)
app.secret_key = 'super secret string'  # Change this!
```

Sections: Flask-Login, Usage

</details>

### pytest-httpx

Send responses to httpx.

`pip install pytest-httpx` · installs (wheel) · licence: MIT License · rank 900 · last release 2026-04-09 · [PyPI](https://pypi.org/project/pytest-httpx/) · [docs](https://colin-b.github.io/pytest_httpx/) · [source](https://github.com/Colin-b/pytest_httpx)

<details><summary>README extract</summary>

> [!NOTE]
> Version 1.0.0 will be released once httpx is considered as stable (release of 1.0.0).
> However, current state can be considered as stable.

Once installed, `httpx_mock` `pytest` fixture will make sure every `httpx` request will be replied to with user provided responses (unless some hosts are explicitly skipped). ...

Example:
```python
import pytest
import httpx

def test_something(httpx_mock):
    httpx_mock.add_response()

    with httpx.Client() as client:
        response = client.get("

@pytest.mark.asyncio
async def test_something_async(httpx_mock):
    httpx_mock.add_response()

    async with httpx.AsyncClient() as client:
        response = await client.get("
```

...

</details>

### htmldate

Fast and robust extraction of original and updated publication dates from URLs and web pages.

`pip install htmldate` · installs (wheel) · licence: Apache-2.0 · rank 901 · last release 2026-10-02 · [PyPI](https://pypi.org/project/htmldate/) · [source](https://github.com/adbar/htmldate)

<details><summary>README extract</summary>

Find original and updated publication dates of any web page.
It is often not possible to do it using just the URL or the server response.

On the command-line or with Python, all the steps needed from web page
download to HTML parsing, scraping, and text analysis are included. ...

Features:
- Flexible input: URLs, HTML files, or HTML trees can be used as input
 (including batch processing).
- Customizable output: Any date format (defaults to ISO 8601
 YMD).
- Detection of both original and updated dates.
- Multilingual. ...

Example:
```python
>>> from htmldate import find_date
>>> find_date('
'2016-12-23'
```

Sections: Htmldate: Find the Publication Date of Web Pages, In a nutshell, With Python, On the command-line, Features, How it works, Performance, Documentation

</details>

### SQLAlchemy-Utils

Various utility functions for SQLAlchemy.

`pip install SQLAlchemy-Utils` · installs (wheel) · licence: BSD-3-Clause · rank 939 · last release 2026-10-09 · [PyPI](https://pypi.org/project/SQLAlchemy-Utils/)

<details><summary>README extract</summary>

Various utility functions, new data types and helpers for SQLAlchemy.

- Documentation
- Issue Tracker
- Code

Sections: SQLAlchemy-Utils, Resources

</details>

### courlan

Clean, filter and sample URLs to optimize data collection – includes spam, content type and language filters.

`pip install courlan` · installs (wheel) · licence: Apache-2.0 · rank 983 · last release 2026-06-01 · [PyPI](https://pypi.org/project/courlan/)

<details><summary>README extract</summary>

Features:
> "It is important for the crawler to visit 'important' pages first,
> so that the fraction of the Web that is visited (and kept up to date)
> is more meaningful." (Cho et al. ...

Example:
```python
>>> from courlan import check_url

# return url and domain name
>>> check_url('
(' 'github.com')

# filter out bogus domains
>>> check_url('
>>>

# tracker removal
>>> check_url('
(' 'test.net')

# use strict for further trimming
>>> my_url = '
>>> check_url(my_url, strict=True)
(' 'httpbin.org')

# check for redirects (HEAD request)
...
```

...

</details>

### trafilatura

Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extraction, output as CSV, JSON, HTML, MD, TXT, XML.

`pip install trafilatura` · installs (wheel) · licence: Apache-2.0 · rank 989 · last release 2026-10-06 · [PyPI](https://pypi.org/project/trafilatura/) · [source](https://github.com/adbar/trafilatura)

<details><summary>README extract</summary>

Features:
- Support for sitemaps (TXT, XML) and feeds (ATOM, JSON, RSS)
 - Smart crawling and URL management (filtering and deduplication) ...

Example:
```python
>>> from trafilatura import fetch_url, extract
>>> downloaded = fetch_url("
>>> extract(downloaded)
'Erin Spiceland is a software engineer and ...'
>>> extract(downloaded, output_format="json", with_metadata=True)
'{"title": "Leader spotlight: Erin Spiceland", "author": "Jessica Rudder", "text": "Erin Spiceland is a software engineer and ..."}'
```

Sections: Introduction, Features, Evaluation, Other evaluations, Documentation, Context, Citing Trafilatura, Software ecosystem

</details>

### jusText

Heuristic based boilerplate removal tool

`pip install jusText` · installs (wheel) · licence: BSD License · rank 1027 · last release 2025-02-25 · [PyPI](https://pypi.org/project/jusText/)

<details><summary>README extract</summary>

Program jusText is a tool for removing boilerplate content, such as navigation
links, headers, and footers from HTML pages. It is
designed to preserve
mainly text containing full sentences and it is therefore well suited for
creating linguistic resources such as Web corpora. You can
try it online. ...

Example:
```python
import requests
import justext

response = requests.get("
paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
for paragraph in paragraphs:
  if not paragraph.is_boilerplate:
    print paragraph.text
```

Sections: jusText, Dependencies, Usage, Python API, 3.0.2 (2025-02-25), 3.0.1 (2024-05-09), 3.0.0 (2021-10-21), 2.2.0 (2016-03-06), 2.1.1 (2014-05-27), 2.1.0 (2014-01-25), 2.0.0 (2013-08-26), 1.2.0 (2011-08-08), 1.1.0 (2011-03-09)

</details>

### mkdocs-material-extensions

Extension pack for Python Markdown and MkDocs Material.

`pip install mkdocs-material-extensions` · installs (wheel) · licence: MIT License · rank 1028 · last release 2023-11-22 · [PyPI](https://pypi.org/project/mkdocs-material-extensions/)

<details><summary>README extract</summary>

[][donate-link]
[][github-ci-link]
[][codecov-link]
[][pypi-link]
[][pypi-link]

> NOTE: This project is now deprecated as MkDocs for Material now implements this logic directly. ...

Sections: MkDocs Material Extensions, Inline SVG Icons, Using Local Custom Icons

</details>

### granian

A Rust HTTP server for Python applications

`pip install granian` · installs (wheel) · licence: BSD License · rank 1069 · last release 2026-10-28 · [PyPI](https://pypi.org/project/granian/) · [source](https://github.com/emmett-framework/granian)

<details><summary>README extract</summary>

The Rust HTTP server for Python

Granian is a Rust HTTP server for Python applications built on top of Hyper and Tokio.

The main reasons behind Granian design are:

- Have a single, correct HTTP implementation, supporting versions 1, 2 (and eventually 3)
- Provide a single package for several platforms ...

Features:
- Supports ASGI/3, RSGI and WSGI interface applications
- HTTP/1 and HTTP/2 protocols
- HTTPS and mTLS
- Websockets
- Direct static files serving
- ASGI pathsend extension

Example:
```python
async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
...

</details>

### Flask-SQLAlchemy

Add SQLAlchemy support to your Flask application.

`pip install Flask-SQLAlchemy` · installs (wheel) · licence: BSD License · rank 1093 · last release 2023-09-11 · [PyPI](https://pypi.org/project/Flask-SQLAlchemy/) · [docs](https://flask-sqlalchemy.palletsprojects.com) · [source](https://github.com/pallets-eco/flask-sqlalchemy/)

<details><summary>README extract</summary>

Flask-SQLAlchemy is an extension for Flask that adds support for
SQLAlchemy to your application. It aims to simplify using SQLAlchemy
with Flask by providing useful defaults and extra helpers that make it
easier to accomplish common tasks.

Example:
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(name)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(app, model_class=Base)

class User(db.Model):
...
```

Sections: Flask-SQLAlchemy, A Simple Example, Links

</details>

### aiohttp-cors

CORS support for aiohttp

`pip install aiohttp-cors` · installs (wheel) · licence: Apache Software License · rank 1160 · last release 2025-03-31 · [PyPI](https://pypi.org/project/aiohttp-cors/)

<details><summary>README extract</summary>

Example:
```python
import asyncio
from aiohttp import web
import aiohttp_cors

@asyncio.coroutine
def handler(request):
    return web.Response(
        text="Hello!",
        headers={
            "X-Custom-Server-Header": "Custom data",
        })

app = web.Application()

# `aiohttp_cors.setup` returns `aiohttp_cors.CorsConfig` instance.
...
```

Sections: Same-origin policy, Cross-origin resource sharing, Usage, Running Selenium tests, Bugs, CHANGES, 0.8.1 (2025-03-31), 0.8.0 (2025-03-11), 0.7.0 (2018-03-05), 0.6.0 (2017-12-21), 0.5.3 (2017-04-21), 0.5.2 (2017-03-28), 0.5.1 (2017-03-23), 0.5.0 (2016-11-18)

</details>

### py-vapid

Simple VAPID header generation library

`pip install py-vapid` · installs (wheel) · licence: MPL-2.0 · rank 1181 · last release 2026-10-14 · [PyPI](https://pypi.org/project/py-vapid/)

<details><summary>README extract</summary>

This minimal library contains the minimal set of functions you need to
generate a VAPID key set and get the headers you’ll need to sign a
WebPush subscription update.

VAPID is a voluntary standard for WebPush subscription providers (sites
that send WebPush updates to remote customers) to self-identify to Push
Servers (the servers that convey the ...

Sections: Easy VAPID generation, App Usage

</details>

### user-agents

A library to identify devices (phones, tablets) and their capabilities by parsing browser user agent strings.

`pip install user-agents` · installs (wheel) · licence: MIT License · rank 1198 · last release 2020-08-23 · [PyPI](https://pypi.org/project/user-agents/)

<details><summary>README extract</summary>

`user_agents` is a Python library that provides an easy way to identify/detect devices like mobile phones, tablets and their capabilities by parsing (browser/HTTP) user agent strings. The goal is to reliably detect whether:

* User agent is a mobile, tablet or PC based device
* User agent has touch capabilities (has touch screen) ...

Example:
```python
from user_agents import parse

# iPhone's user agent string
ua_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
user_agent = parse(ua_string)

# Accessing user agent's browser attributes
...
```

...

</details>

### office365-rest-python-client

Microsoft 365 & Microsoft Graph Library for Python

`pip install office365-rest-python-client` · installs (wheel) · licence: MIT License · rank 1207 · last release 2026-11-07 · [PyPI](https://pypi.org/project/office365-rest-python-client/) · [source](https://github.com/vgrem/office365-rest-python-client)

<details><summary>README extract</summary>

A Python client library for Microsoft 365, the SharePoint REST API and Microsoft Graph.

Python 3.8+ · typed models · fluent queries · deferred execution · 700+ runnable examples

- Two clients, one library — `ClientContext` speaks the SharePoint REST API; `GraphClient` speaks Microsoft Graph. ...

Example:
```python
from office365.sharepoint.client_context import ClientContext

ctx = ClientContext("
    "contoso.onmicrosoft.com", client_id, thumbprint, cert_path="./private.pem"
)

tasks = ctx.web.lists.get_by_title("Tasks")
item = tasks.add_item({"Title": "Write the release notes"}).execute_query()
print("Created item:", item.id)

...
```

...

</details>

### httpx-ws

WebSockets support for HTTPX

`pip install httpx-ws` · installs (wheel) · licence: MIT License · rank 1210 · last release 2026-03-28 · [PyPI](https://pypi.org/project/httpx-ws/) · [docs](https://frankie567.github.io/httpx-ws/) · [source](https://github.com/frankie567/httpx-ws)

<details><summary>README extract</summary>

WebSockets support for HTTPX

Documentation:

Source Code:

Features:
- [x] Sync and async client
- [x] Helper methods to send text, binary and JSON data
- [x] Helper methods to receive text, binary and JSON data
- [x] Automatic ping/pong answers
- [x] HTTPX transport to test WebSockets defined in ASGI apps ...

Sections: HTTPX WS, Features, Setup environment, Run unit tests, Format the code

</details>

### WTForms

Form validation and rendering for Python web development.

`pip install WTForms` · installs (wheel) · licence: BSD License · rank 1213 · last release 2026-11-01 · [PyPI](https://pypi.org/project/WTForms/) · [docs](https://wtforms.readthedocs.io) · [source](https://github.com/pallets-eco/wtforms/)

<details><summary>README extract</summary>

WTForms is a flexible forms validation and rendering library for Python
web development. It can work with whatever web framework and template
engine you choose. It supports data validation, CSRF protection,
internationalization (I18N), and more. There are various community
libraries that provide closer integration with popular frameworks.

Sections: WTForms, Third-Party Library Integrations, Links

</details>

### primp

HTTP client that can impersonate web browsers

`pip install primp` · installs (wheel) · licence: MIT License · rank 1215 · last release 2026-09-13 · [PyPI](https://pypi.org/project/primp/) · [source](https://github.com/deedy5/primp)

<details><summary>README extract</summary>

> HTTP client that can impersonate web browsers

Example:
```python
import primp

client = primp.Client(impersonate="chrome_146")
resp = client.get("
print(resp.text)
```

Sections: 🪞 PRIMP 🐍, 🔧 Building from Source, 🚀 Quick Start, Sync API, Async API, More examples, 📊 Benchmark, 🎭 Browser profiles, 📖 Documentation, Disclaimer

</details>

### pywebpush

WebPush publication library

`pip install pywebpush` · installs (wheel) · licence: MPL-2.0 · rank 1227 · last release 2026-08-30 · [PyPI](https://pypi.org/project/pywebpush/)

<details><summary>README extract</summary>

This library is available on pypi as pywebpush.
Source is available on github.
Please note: This library was designated as a `Critical Project` by PyPi, it is currently
maintained by a single person. I still accept PRs and Issues, but
make of that what you will.

Example:
```python
from pywebpush import webpush, WebPushException

try:
    webpush(
        subscription_info={
            "endpoint": "
            "keys": {
                "p256dh": "0123abcde...",
                "auth": "abc123..."
            }},
        data="Mary had a little lamb, with a nice mint jelly",
...
```

...

</details>

### pyqwest

A modern, high-performance HTTP client for Python and Rust.

`pip install pyqwest` · installs (wheel) · licence: MIT License · rank 1230 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pyqwest/) · [source](https://github.com/curioswitch/pyqwest.git)

<details><summary>README extract</summary>

pyqwest is a Python HTTP client supporting modern HTTP features, based on the Rust library reqwest.
It does not reinvent any features of HTTP or sockets, delegating to the excellent reqwest, which uses hyper, for all core functionality
while presenting a familiar Pythonic API.

Features:
- All features of HTTP, including bidirectional streaming, trailers, and HTTP/3
- Async and sync clients
- The stability and performance of the Rust HTTP client stack
- A fully-typed, Pythonic API - no runtime-checked union types

Example:
```python
client = pyqwest.Client()

response = await client.get("
print(len(response.content))
```

Sections: pyqwest, Features, Usage

</details>

### Protego

Pure-Python robots.txt parser with support for modern conventions

`pip install Protego` · installs (wheel) · licence: BSD-3-Clause · rank 1234 · last release 2026-09-21 · [PyPI](https://pypi.org/project/Protego/) · [source](https://github.com/scrapy/protego)

<details><summary>README extract</summary>

Protego is a pure-Python `robots.txt` parser. It implements the parsing and
URL matching rules of RFC 9309, and additionally supports the
`Crawl-delay`, `Request-rate`, `Visit-time` and `Host` extensions. ...

Example:
```python
>>> from protego import Protego
>>> robotstxt = """
... User-agent: *
... Disallow: /
... Allow: /about
... Allow: /account
... Disallow: /account/contact$
... Disallow: /account/*/profile
... Crawl-delay: 4
... Request-rate: 10/1m                 # 10 requests every 1 minute
...
... Sitemap:
... Host:
... """
>>> rp = Protego.parse(robotstxt)
...
```

Sections: Protego, Usage, Comparison, API Reference, Properties, Methods

</details>

### browser-harness

The simplest, thinnest, and most powerful harness to control your real browser with your agent.

`pip install browser-harness` · installs (wheel) · licence: MIT · rank 1253 · last release 2026-09-04 · [PyPI](https://pypi.org/project/browser-harness/) · [source](https://github.com/browser-use/browser-harness)

<details><summary>README extract</summary>

Connect an LLM directly to your real browser through one editable CDP websocket. The agent writes missing helpers as it works, so the harness improves with every task.

Try browser-harness in Browser Use Cloud or paste the setup prompt into your coding agent.

You will never use the browser again.

Sections: Browser Harness ♞, See it work, Setup prompt, How it works, Scale with Browser Use Cloud, MCP server

</details>

### fetch-use

Python client for Browser-Use Fetch HTTP service

`pip install fetch-use` · installs (wheel) · licence: MIT License · rank 1255 · last release 2026-04-09 · [PyPI](https://pypi.org/project/fetch-use/) · [docs](https://docs.browser-use.com) · [source](https://github.com/browser-use/fetch-use)

<details><summary>README extract</summary>

Python client for the Browser-Use Fetch HTTP service. Routes HTTP requests through Browser-Use's proxy infrastructure with Chrome TLS fingerprinting, session-based IP persistence, and server-side cookie management.

Example:
```python
import os
from fetch_use import fetch_sync

os.environ["BROWSER_USE_API_KEY"] = "bu_your-api-key"

response = fetch_sync("
print(response.status_code)  # 200
print(response.json())
```

Sections: fetch-use, Quick Start, Configuration, Session Persistence, Usage, Basic GET Request, POST with JSON, Custom Headers and Cookies, Proxy Country, Retry Configuration, Server-Side Cookies, Output Format, Response Object, Error Handling

</details>

### Flask-WTF

Form rendering, validation, and CSRF protection for Flask with WTForms.

`pip install Flask-WTF` · installs (wheel) · licence: BSD License · rank 1321 · last release 2026-04-23 · [PyPI](https://pypi.org/project/Flask-WTF/) · [docs](https://flask-wtf.readthedocs.io/) · [source](https://github.com/pallets-eco/flask-wtf/)

<details><summary>README extract</summary>

Simple integration of Flask and WTForms, including CSRF, file upload,
and reCAPTCHA.

Sections: Flask-WTF, Links

</details>

### dj-database-url

Use Database URLs in your Django Application.

`pip install dj-database-url` · installs (wheel) · licence: BSD-3-Clause · rank 1332 · last release 2026-02-19 · [PyPI](https://pypi.org/project/dj-database-url/)

<details><summary>README extract</summary>

This simple Django utility allows you to utilize the
12factor inspired
`DATABASE_URL` environment variable to configure your Django application.

The `dj_database_url.config` method returns a Django database connection
dictionary, populated with all the data specified in your URL. ...

Example:
```python
DATABASES['default'] = dj_database_url.config(default='postgres://...', test_options={'NAME': 'mytestdatabase'})
```

Sections: DJ-Database-URL, Usage, URL schema, Raising Issues or helping others

</details>

### bottle

Fast and simple WSGI-framework for small web-applications.

`pip install bottle` · installs (wheel) · licence: MIT License · rank 1385 · last release 2025-06-15 · [PyPI](https://pypi.org/project/bottle/) · [source](https://github.com/bottlepy/bottle)

### djangorestframework-simplejwt

A minimal JSON Web Token authentication plugin for Django REST Framework

`pip install djangorestframework-simplejwt` · installs (wheel) · licence: MIT License · rank 1428 · last release 2025-07-21 · [PyPI](https://pypi.org/project/djangorestframework-simplejwt/)

<details><summary>README extract</summary>

Simple JWT is a JSON Web Token authentication plugin for the Django REST
Framework.

For full documentation, visit django-rest-framework-simplejwt.readthedocs.io.

Contribute translations directly with PRs or via inlang

Sections: Simple JWT, Abstract, Translations

</details>

### w3lib

Library of web-related functions

`pip install w3lib` · installs (wheel) · licence: BSD-3-Clause · rank 1454 · last release 2026-11-05 · [PyPI](https://pypi.org/project/w3lib/) · [docs](https://w3lib.readthedocs.io/en/latest/) · [source](https://github.com/scrapy/w3lib)

<details><summary>README extract</summary>

Features:
This is a Python library of web-related functions, such as:

* remove comments, or tags from HTML snippets
* extract base url from HTML snippets
* translate entities on HTML strings
* convert raw HTTP headers to dicts and vice-versa
* construct HTTP ...

Sections: w3lib, Overview, Requirements, Documentation

</details>

### Hypercorn

A ASGI Server based on Hyper libraries and inspired by Gunicorn

`pip install Hypercorn` · installs (wheel) · licence: MIT License · rank 1459 · last release 2025-11-08 · [PyPI](https://pypi.org/project/Hypercorn/)

<details><summary>README extract</summary>

Hypercorn is an ASGI and
WSGI web server based on the sans-io hyper, h11, h2, and wsproto libraries and inspired by
Gunicorn. Hypercorn supports HTTP/1, HTTP/2, WebSockets (over HTTP/1
and HTTP/2), ASGI, and WSGI specifications. Hypercorn can utilise
asyncio, uvloop, or trio worker types. ...

Example:
```python
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

from module import app

asyncio.run(serve(app, Config()))
```

Sections: Hypercorn, Quickstart, Help

</details>

### waitress

Waitress WSGI server

`pip install waitress` · installs (wheel) · licence: Zope Public License · rank 1486 · last release 2024-11-16 · [PyPI](https://pypi.org/project/waitress/) · [docs](https://docs.pylonsproject.org/projects/waitress/en/latest/index.html)

<details><summary>README extract</summary>

Waitress is a production-quality pure-Python WSGI server with very acceptable
performance. It has no dependencies except ones which live in the Python
standard library. It runs on CPython on Unix and Windows under Python 3.9+. It
is also known to run on PyPy 3 (version 3.9 compatible python and above) on
UNIX. It supports HTTP/1.0 and HTTP/1.1. ...

Features:
- Added support for Python 3.13.
 See

Sections: Waitress, 3.0.2 (2024-11-16), 3.0.1 (2024-10-28), Backward Incompatibilities, Features, 3.0.0 (2024-02-04), Updated Defaults

</details>

### python-socks

Proxy (SOCKS4, SOCKS5, HTTP CONNECT) client for Python

`pip install python-socks` · installs (wheel) · licence: Apache-2.0 · rank 1503 · last release 2026-10-31 · [PyPI](https://pypi.org/project/python-socks/) · [source](https://github.com/romis2012/python-socks)

<details><summary>README extract</summary>

<!--


The `python-socks` package provides a core proxy client functionality for Python.
Supports `SOCKS4(a)`, `SOCKS5(h)`, `HTTP CONNECT` proxy and provides sync and async (asyncio, trio, anyio) APIs.
You probably don't need to use `python-socks` directly.
It is used internally by
aiohttp-socks and httpx-socks packages.

- Python >= 3.9 ...

Example:
```python
import ssl
from python_socks.sync import Proxy

def fetch():
    proxy1 = Proxy.from_url("socks5://user:password@127.0.0.1:1080")
    proxy2 = Proxy.from_url("socks4://127.0.0.1:1081", forward=proxy1)
    proxy3 = Proxy.from_url(" forward=proxy2)

    sock = proxy3.connect(
        dest_host="check-host.net",
        dest_port=443,
    )

...
```

...

</details>

### django-phonenumber-field

An international phone number field for django models.

`pip install django-phonenumber-field` · installs (wheel) · licence: MIT · rank 1514 · last release 2026-10-21 · [PyPI](https://pypi.org/project/django-phonenumber-field/) · [docs](https://django-phonenumber-field.readthedocs.io/) · [source](https://github.com/django-phonenumber-field/django-phonenumber-field)

<details><summary>README extract</summary>

A Django library which interfaces with python-phonenumbers to validate, pretty print and convert
phone numbers. `python-phonenumbers` is a port of Google's libphonenumber library, which
powers Android's phone number handling.

tox needs to be installed. ...

Sections: django-phonenumber-field, Documentation, Running tests

</details>

### fake-useragent

Up-to-date simple useragent faker with real world database

`pip install fake-useragent` · installs (wheel) · licence: Apache-2.0 · rank 1528 · last release 2025-04-14 · [PyPI](https://pypi.org/project/fake-useragent/)

<details><summary>README extract</summary>

Up-to-date simple useragent faker with real world database.

Features:
- Data is pre-downloaded & post-processed from Intoli LLC and the data is part of the package itself
- The data consists of a wide range of browser agents and various browsers ...

Example:
```python
from fake_useragent import UserAgent
ua = UserAgent()

# Get a random browser user-agent string
print(ua.random)
# Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0

# Or get user-agent string from a specific browser
print(ua.chrome)
...
```

Sections: fake-useragent, Features, Usage, Additional usage, User-agent Python Dictionary, Notes, Experiencing issues?, User-agent Data, Python Virtual Environment, Tests, Linting

</details>

### python3-openid

OpenID support for modern servers and consumers.

`pip install python3-openid` · installs (wheel) · licence: Apache Software License · rank 1537 · last release 2020-06-29 · [PyPI](https://pypi.org/project/python3-openid/)

<details><summary>README extract</summary>

This is a set of Python packages to support use of
the OpenID decentralized identity system in your application, update to Python
3. Want to enable single sign-on for your web site? Use the openid.consumer
package. Want to run your own OpenID server? Check out openid.server.
Includes example code and support for a variety of storage back-ends.

</details>

### ddgs

Dux Distributed Global Search. A metasearch library that aggregates results from diverse web search services.

`pip install ddgs` · installs (wheel) · licence: MIT · rank 1569 · last release 2026-10-23 · [PyPI](https://pypi.org/project/ddgs/) · [docs](https://github.com/deedy5/ddgs/blob/main/README.md) · [source](https://github.com/deedy5/ddgs)

<details><summary>README extract</summary>

A metasearch library that aggregates results from diverse web search services.

Example:
```python
from ddgs import DDGS

results = DDGS().text("python programming", max_results=5)
print(results)
```

Sections: DDGS | Dux Distributed Global Search, CLI version, API Server, Endpoints, MCP Server, Available Tools, Client Configuration, Engines, DDGS class, 1. text(), 2. images(), 3. videos(), 4. news(), 5. books()

</details>

### mangum

AWS Lambda support for ASGI applications

`pip install mangum` · installs (wheel) · licence: MIT License · rank 1575 · last release 2026-08-22 · [PyPI](https://pypi.org/project/mangum/) · [docs](https://mangum.fastapiexpert.com) · [source](https://github.com/Kludex/mangum)

<details><summary>README extract</summary>

Mangum is an adapter for running ASGI applications in AWS Lambda to handle Function URL, API Gateway, ALB, and Lambda@Edge events.

Features:
- Event handlers for API Gateway HTTP and REST APIs, Application Load Balancer, Function URLs, and CloudFront Lambda@Edge.

- Compatibility with ASGI application frameworks, such as Starlette, FastAPI, Quart and Django. ...

Example:
```python
from mangum import Mangum

async def app(scope, receive, send):
    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [[b"content-type", b"text/plain; charset=utf-8"]],
        }
    )
    await send({"type": "http.response.body", "body": b"Hello, world!"})

...
```

Sections: Mangum, Features, Example

</details>

### flask-babel

Adds i18n/l10n support for Flask applications.

`pip install flask-babel` · installs (wheel) · licence: BSD License · rank 1642 · last release 2023-10-02 · [PyPI](https://pypi.org/project/flask-babel/) · [docs](https://python-babel.github.io/flask-babel/) · [source](https://github.com/python-babel/flask-babel)

<details><summary>README extract</summary>

Implements i18n and l10n support for Flask. This is based on the Python
babel and pytz modules.

The latest documentation is available here.

Sections: Flask Babel, Documentation

</details>

### connectrpc

Server and client runtime library for Connect RPC

`pip install connectrpc` · installs (wheel) · licence: Apache-2.0 · rank 1671 · last release 2026-10-25 · [PyPI](https://pypi.org/project/connectrpc/) · [docs](https://connectrpc.com/docs/python/getting-started/) · [source](https://github.com/connectrpc/connect-py)

<details><summary>README extract</summary>

Connect is the easiest way to build modern APIs.

Docs •
API reference •
Example •
New to Connect?

Features:
Building an API usually means writing the same types at least twice: once on the server, and once in every client. Connect makes this simple - define your API schema using Protobuf, and Connect generates type-safe server stubs and idiomatic client ...

Example:
```python
from connectrpc.request import RequestContext
from your_service_pb import HelloRequest, HelloResponse
from your_service_connect import HelloService, HelloServiceASGIApplication

class MyHelloService(HelloService):
    async def say_hello(
        self, request: HelloRequest, ctx: RequestContext
    ) -> HelloResponse:
...
```

Sections: Connect for Python, Why Connect?, Features, Getting started, Usage

</details>

### channels

Brings async, event-driven capabilities to Django.

`pip install channels` · installs (wheel) · licence: BSD License · rank 1675 · last release 2025-11-20 · [PyPI](https://pypi.org/project/channels/)

<details><summary>README extract</summary>

Channels augments Django to bring WebSocket, long-poll HTTP,
task offloading and other async support to your code, using familiar Django
design patterns and a flexible underlying framework that lets you not only
customize behaviours but also write support for your own protocols and needs. ...

Sections: Django Channels, Dependencies, Other Projects

</details>

### django-oauth-toolkit

OAuth 2.0 authorization server for Django

`pip install django-oauth-toolkit` · installs (wheel) · licence: BSD License · rank 1697 · last release 2026-08-21 · [PyPI](https://pypi.org/project/django-oauth-toolkit/) · [source](https://github.com/django-oauth/django-oauth-toolkit)

<details><summary>README extract</summary>

*OAuth2 goodies for the Djangonauts!*

Django OAuth Toolkit is an OAuth 2.0 authorization server for teams already running Django.
It provides, out of the box, the endpoints, models, and logic to issue and manage OAuth2 tokens
from your existing Django project, instead of standing up and operating a separate service. ...

Sections: Django OAuth Toolkit, Requirements, Documentation, Help Wanted, Join the team, How you can help, Discussions, Submit PRs and Perform Reviews

</details>

### django-ipware

A Django application to retrieve a client's real IP address.

`pip install django-ipware` · installs (wheel) · licence: MIT · rank 1706 · last release 2026-09-22 · [PyPI](https://pypi.org/project/django-ipware/) · [docs](https://github.com/un33k/django-ipware#readme) · [source](https://github.com/un33k/django-ipware)

<details><summary>README extract</summary>

Best-effort client IP detection for Django — one call, in any view or middleware.

[![status-image]][status-link]
[![version-image]][version-link]
[![coverage-image]][coverage-link]
[![maintained-image]][maintained-link]

Example:
```python
from ipware import get_client_ip

client_ip, is_routable = get_client_ip(request)

if client_ip is None:
    ...  # no usable IP in the request
elif is_routable:
    ...  # a public internet address
else:
    ...  # private, link-local or loopback (intranet, VPN, local dev)
```

Sections: Django IPware, Quickstart, What you get, What it's used for, How it fits together, API, Settings, Selection rules, Default header precedence, Trusted proxies, Proxy count, Strict mode, Right-most client networks, Middleware

</details>

### aioresponses

Mock out requests made by ClientSession from aiohttp package

`pip install aioresponses` · installs (wheel) · licence: MIT License · rank 1724 · last release 2026-06-23 · [PyPI](https://pypi.org/project/aioresponses/)

<details><summary>README extract</summary>

Aioresponses is a helper to mock/fake web requests in python aiohttp package.

For *requests* module there are a lot of packages that help us with testing (eg. *httpretty*, *responses*, *requests-mock*).

When it comes to testing asynchronous HTTP requests it is a bit harder (at least at the beginning). ...

Features:
* Easy to mock out HTTP requests made by *aiohttp.ClientSession*

Example:
```python
import aiohttp
import asyncio
from aioresponses import aioresponses

@aioresponses()
def test_request(mocked):
    loop = asyncio.get_event_loop()
    mocked.get(' status=200, body='test')
    session = aiohttp.ClientSession()
    resp = loop.run_until_complete(session.get('

    assert resp.status == 200
    mocked.assert_called_once_with('
```

Sections: aioresponses, Usage, Features

</details>

### asgi-correlation-id

Middleware correlating project logs to individual requests

`pip install asgi-correlation-id` · installs (wheel) · licence: MIT · rank 1736 · last release 2026-06-09 · [PyPI](https://pypi.org/project/asgi-correlation-id/) · [source](https://github.com/snok/asgi-correlation-id)

<details><summary>README extract</summary>

Middleware for reading or generating correlation IDs for each incoming request. Correlation IDs can then be added to your
logs, making it simple to retrieve all logs generated from a single HTTP request.

When the middleware detects a correlation ID HTTP header in an incoming request, the ID is stored. ...

Example:
```python
from fastapi import FastAPI

from asgi_correlation_id import CorrelationIdMiddleware

app = FastAPI()
app.add_middleware(CorrelationIdMiddleware)
```

Sections: ASGI Correlation ID middleware, Example, Setup, Adding the middleware, Configure logging, Middleware configuration, CORS, Starlette, FastAPI, Exception handling, Setting up logging from scratch, Integration with structlog

</details>

### curlify

Convert Requests request objects to curl commands.

`pip install curlify` · installs (wheel) · licence: MIT License · rank 1739 · last release 2025-05-25 · [PyPI](https://pypi.org/project/curlify/)

<details><summary>README extract</summary>

Example:
```python
import curlify
import requests

response = requests.get("
print(curlify.to_curl(response.request))
# curl -X 'GET' -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'User-Agent: python-requests/2.18.4' '

print(curlify.to_curl(response.request, compressed=True))
...
```

Sections: Changes, v3.0.0, v2.2.0, v2.1.1, v2.1.0, v2.0.1, v2.0, v1.2, Example

</details>

### python-ipware

A Python package to retrieve a client's real IP address.

`pip install python-ipware` · installs (wheel) · licence: MIT · rank 1771 · last release 2026-10-01 · [PyPI](https://pypi.org/project/python-ipware/) · [docs](https://github.com/un33k/python-ipware#readme) · [source](https://github.com/un33k/python-ipware)

<details><summary>README extract</summary>

Best-effort client IP detection for Python server applications — Django, Flask, or any WSGI/ASGI framework.

[![status-image]][status-link]
[![version-image]][version-link]
[![coverage-image]][coverage-link]
[![maintained-image]][maintained-link]

Example:
```python
from python_ipware import IpWare

ipw = IpWare()

# Django: request.META  |  Flask: request.environ
ip, trusted_route = ipw.get_client_ip(request.META)

if ip:
    # ip is an ipaddress.IPv4Address or IPv6Address
    ip.is_global     # publicly routable
    ip.is_private    # private network
    ip.is_loopback   # 127.0.0.1 / ::1

if trusted_route:
...
```

...

</details>

### fastapi-mcp

Automatic MCP server generator for FastAPI applications - converts FastAPI endpoints to MCP tools for LLM integration

`pip install fastapi-mcp` · installs (wheel) · licence: MIT License · rank 1774 · last release 2025-07-28 · [PyPI](https://pypi.org/project/fastapi-mcp/) · [docs](https://github.com/tadata-org/fastapi_mcp#readme) · [source](https://github.com/tadata-org/fastapi_mcp)

<details><summary>README extract</summary>

Built by Tadata

Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth!

Features:
- Authentication built in, using your existing FastAPI dependencies!

- FastAPI-native: Not just another OpenAPI -> MCP converter

- Zero/Minimal configuration required - just point it at your FastAPI app and it works ...

Example:
```python
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()

mcp = FastApiMCP(app)

# Mount the MCP server directly to your FastAPI app
mcp.mount()
```

Sections: FastAPI-MCP, Features, Hosted Solution, Basic Usage, Documentation, Examples and Advanced Usage, FastAPI-first Approach, Requirements

</details>

### Scrapy

A high-level Web Crawling and Web Scraping framework

`pip install Scrapy` · installs (wheel) · licence: BSD-3-Clause · rank 1779 · last release 2026-11-06 · [PyPI](https://pypi.org/project/Scrapy/) · [docs](https://docs.scrapy.org/) · [source](https://github.com/scrapy/scrapy)

<details><summary>README extract</summary>

Scrapy is a web scraping framework to extract structured data from websites.
It is cross-platform, and requires Python 3.11+. It is maintained by Zyte
(formerly Scrapinghub) and many other contributors.

Install with:

And follow the documentation to learn how to use it.

If you wish to contribute, see Contributing.

</details>

### port-for

Utility that helps with local TCP ports management. It can find an unused TCP localhost port and remember the association.

`pip install port-for` · installs (wheel) · licence: MIT · rank 1826 · last release 2026-10-05 · [PyPI](https://pypi.org/project/port-for/) · [source](https://github.com/fizyk/port-for/)

<details><summary>README extract</summary>

`port-for` is a command-line utility and a python library that
helps with local TCP ports management.

It can find an unused TCP localhost port and remember the association:
This can be useful when you are installing a stack of software
with multiple parts needing port numbers. ...

Example:
```python
>>> import port_for
>>> port_for.select_random()
37774

>>> port_for.select_random()
48324

>>> 80 in port_for.available_good_ports()
False

>>> port_for.get_port()
34455

>>> port_for.get_port("1234")
1234

>>> port_for.get_port((2000, 3000))
2345

>>> port_for.get_port({4001, 4003, 4005})
4005

>>> port_for.get_port([{4000, 4001}, (4100, 4200)])
...
```

Sections: port-for, Script usage, Library usage

</details>

### Flask-Session

Server-side session support for Flask

`pip install Flask-Session` · installs (wheel) · licence: BSD License · rank 1859 · last release 2024-03-26 · [PyPI](https://pypi.org/project/Flask-Session/) · [docs](https://flask-session.readthedocs.io) · [source](https://github.com/pallets-eco/flask-session/)

<details><summary>README extract</summary>

Flask-Session is an extension for Flask that adds support for server-side sessions to
your application.

Example:
```python
from flask import Flask, session
from flask_session import Session

app = Flask(name)
# Check Configuration section for more details
SESSION_TYPE = 'redis'
app.config.from_object(name)
Session(app)

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')
```

Sections: Flask-Session, A Simple Example, Documentation

</details>

### WebOb

WSGI request and response object

`pip install WebOb` · installs (wheel) · licence: MIT License · rank 1873 · last release 2026-08-02 · [PyPI](https://pypi.org/project/WebOb/)

<details><summary>README extract</summary>

WebOb provides objects for HTTP requests and responses. Specifically
it does this by wrapping the WSGI request
environment and response status/headers/app_iter(body).

The request and response objects provide many conveniences for parsing
HTTP request and forming HTTP responses. ...

Features:
- Add Request.remote_host, exposing REMOTE_HOST environment variable.

- Added `acceptparse.Accept.parse_offer` to codify what types of offers
 are compatible with `acceptparse.AcceptValidHeader.acceptable_offers`, ...

Sections: WebOb, 1.8.11 (2026-08-02), 1.8.10 (2026-06-02), 1.8.9 (2024-11-23), Bugfix, 1.8.8 (2024-08-13), 1.8.7 (2021-02-17), 1.8.6 (2020-01-21), Experimental Features, 1.8.5 (2019-01-03), Warnings, 1.8.4 (2018-11-11)

</details>

### aiohttp_socks

Proxy connector for aiohttp

`pip install aiohttp_socks` · installs (wheel) · licence: Apache-2.0 · rank 1892 · last release 2026-08-12 · [PyPI](https://pypi.org/project/aiohttp_socks/) · [source](https://github.com/romis2012/aiohttp-socks)

<details><summary>README extract</summary>

<!--

The `aiohttp-socks` package provides a proxy connector for aiohttp.
Supports SOCKS4(a), SOCKS5(h), HTTP (CONNECT) as well as Proxy chains.
It uses python-socks for core proxy functionality.

- Python >= 3.9
- aiohttp >= 3.10.0
- python-socks[asyncio] >= 2.4.3

Features:
Unlike aiosocksy, aiohttp_socks has only single point of integration with aiohttp.
This makes it easier to maintain compatibility with new aiohttp versions.

Example:
```python
import aiohttp
from aiohttp_socks import ProxyType, ProxyConnector, ChainProxyConnector

async def fetch(url):
    connector = ProxyConnector.from_url('socks5://user:password@127.0.0.1:1080')

    ### or use ProxyConnector constructor
    # connector = ProxyConnector(
    #     proxy_type=ProxyType.SOCKS5,
    #     host='127.0.0.1',
...
```

...

</details>

### daphne

Django ASGI (HTTP/WebSocket) server

`pip install daphne` · installs (wheel) · licence: BSD License · rank 1905 · last release 2026-07-21 · [PyPI](https://pypi.org/project/daphne/) · [docs](https://channels.readthedocs.io) · [source](https://github.com/django/daphne.git)

### patchright

Undetected Python version of the Playwright testing and automation library.

`pip install patchright` · installs (wheel) · licence: Apache-2.0 · rank 1927 · last release 2026-11-02 · [PyPI](https://pypi.org/project/patchright/) · [source](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-python)

<details><summary>README extract</summary>

Example:
```python
# patchright here!
from patchright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("
    page.screenshot(path=f"example-{p.chromium.name}.png")
    browser.close()
```

Sections: 🎭 Patchright Python, Usage, Best Practice - use Chrome without Fingerprint Injection, Patches, Runtime.enable Leak, Console.enable Leak, Command Flags Leaks, General Leaks, Closed Shadow Roots, Stealth, Documentation and API Reference, Extended Patchright API, `evaluate_all` Method (`Locator.evaluate_all`), Bugs

</details>

### tinytag

Read audio file metadata

`pip install tinytag` · installs (wheel) · licence: MIT License · rank 1946 · last release 2026-09-07 · [PyPI](https://pypi.org/project/tinytag/)

<details><summary>README extract</summary>

<!--
 SPDX-FileCopyrightText: 2014-2026 tinytag Contributors
 SPDX-License-Identifier: MIT

tinytag is a Python library for reading audio file metadata

Features:
* Read tags, images and properties of audio files

 * ID3 v1, v1.1, v2.2, v2.3, v2.4
 * MP3 / MP2 / MP1
 * MP4 (MPEG-4 Audio / AAC / ALAC)
 * WAVE / WAV
 * OGG (FLAC / Opus / Speex / Vorbis)
 * FLAC
 * ASF (WMA)
 * AIFF / AIFF-C
 * Same API for all ...

Example:
```python
from tinytag import TinyTag
tag: TinyTag = TinyTag.get('/some/music.mp3')

print(f'This track is by {tag.artist}.')
print(f'It is {tag.duration:.2f} seconds long.')
```

...

</details>

### xai-sdk

The official Python SDK for the xAI API

`pip install xai-sdk` · installs (wheel) · licence: Apache-2.0 · rank 1975 · last release 2026-10-23 · [PyPI](https://pypi.org/project/xai-sdk/) · [docs](https://docs.x.ai) · [source](https://github.com/xai-org/xai-sdk-python)

<details><summary>README extract</summary>

The official Python SDK for xAI's APIs

The xAI Python SDK is a gRPC-based Python library for interacting with xAI's APIs. Built for Python 3.10 and above, it offers both synchronous and asynchronous clients. ...

Example:
```python
from xai_sdk import Client, AsyncClient

# Synchronous client
sync_client = Client()

# Asynchronous client
async_client = AsyncClient()
```

Sections: xAI Python SDK, Documentation, Requirements, Usage, Client Instantiation, Multi-Turn Chat (Synchronous), Multi-Turn Chat (Asynchronous), Streaming, Image Understanding, Video Generation, Video Editing, Video Extension, Advanced Features, Telemetry & Observability

</details>

### prance

Resolving Swagger/OpenAPI 2.0 and 3.0.0 Parser

`pip install prance` · installs (wheel) · licence: MITNFA · rank 1987 · last release 2026-07-19 · [PyPI](https://pypi.org/project/prance/)

<details><summary>README extract</summary>

Prance provides parsers for Swagger/OpenAPI
2.0 and 3.0 API specifications in Python.
It uses openapi\_spec\_validator,
swagger\_spec\_validator or
flex
to validate specifications, but additionally resolves JSON
references
in accordance with the OpenAPI spec. ...

Example:
```python
from prance import ResolvingParser
parser = ResolvingParser('path/to/my/swagger.yaml')
parser.specification  # contains fully resolved specs as a dict
```

Sections: Usage, Command Line Interface, Code, Compatibility, Partial Reference Resolution, Extensions

</details>

### marshmallow-dataclass

Python library to convert dataclasses into marshmallow schemas.

`pip install marshmallow-dataclass` · installs (wheel) · licence: MIT License · rank 1990 · last release 2024-09-12 · [PyPI](https://pypi.org/project/marshmallow-dataclass/)

<details><summary>README extract</summary>

Automatic generation of marshmallow schemas from dataclasses.

Features:
Using schemas in Python often means having both a class to represent your data and a class to represent its schema, which results in duplicated code that could fall out of sync. ...

Example:
```python
from dataclasses import dataclass
from datetime import date

import marshmallow_dataclass

@dataclass
class Person:
    name: str
    birth: date

PersonSchema = marshmallow_dataclass.class_schema(Person)
```

...

</details>

### pylsqpack

Python wrapper for the ls-qpack QPACK library

`pip install pylsqpack` · installs (wheel) · licence: BSD-3-Clause · rank 2028 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pylsqpack/) · [docs](https://pylsqpack.readthedocs.io/)

<details><summary>README extract</summary>

`pylsqpack` is a wrapper around the ls-qpack library. It provides Python
`Decoder` and `Encoder` objects to read or write HTTP/3 headers compressed
with QPACK.

To learn more about `pylsqpack` please read the documentation.

</details>

### vercel-runtime

(no summary)

`pip install vercel-runtime` · installs (wheel) · licence: Apache-2.0 · rank 2038 · last release 2026-10-22 · [PyPI](https://pypi.org/project/vercel-runtime/)

### aioquic

An implementation of QUIC and HTTP/3

`pip install aioquic` · installs (wheel) · licence: BSD-3-Clause · rank 2041 · last release 2026-11-02 · [PyPI](https://pypi.org/project/aioquic/) · [docs](https://aioquic.readthedocs.io/)

<details><summary>README extract</summary>

`aioquic` is a library for the QUIC network protocol in Python. It features
a minimal TLS 1.3 implementation, a QUIC stack and an HTTP/3 stack.

`aioquic` is used by Python opensource projects such as dnspython,
hypercorn, mitmproxy and the Web Platform Tests cross-browser test
suite. ...

Features:
`aioquic` has been designed to be embedded into Python client and server
libraries wishing to support QUIC and / or HTTP/3. The goal is to provide a
common codebase for Python libraries in the hope of avoiding duplicated effort. ...

Sections: aioquic, What is `aioquic`?, Why should I use `aioquic`?, Features, Building from source, Running the examples

</details>

### multipart

Parser for multipart/form-data

`pip install multipart` · installs (wheel) · licence: MIT License · rank 2114 · last release 2026-09-25 · [PyPI](https://pypi.org/project/multipart/) · [docs](https://multipart.readthedocs.io/) · [source](https://github.com/defnull/multipart)

<details><summary>README extract</summary>

This module provides a fast incremental non-blocking parser for
`multipart/form-data` [HTML5, RFC7578], as well as blocking alternatives for
easier use in WSGI or CGI applications:

* PushMultipartParser: Fast SansIO (incremental, non-blocking) parser suitable
 for ASGI, asyncio and other IO, time or memory constrained environments. ...

Features:
* Pure python single file module with no dependencies.
* Optimized for both blocking and non-blocking applications.
* 100% test coverage with test data from actual browsers and HTTP clients.
* High throughput and low latency (see benchmarks). ...

Sections: Python multipart/form-data parser, Features, Scope and compatibility, Documentation

</details>

### duckduckgo-search

Search for words, documents, images, news, maps and text translation using the DuckDuckGo.com search engine.

`pip install duckduckgo-search` · installs (wheel) · licence: MIT License · rank 2140 · last release 2025-07-06 · [PyPI](https://pypi.org/project/duckduckgo-search/)

<details><summary>README extract</summary>

Example:
```python
from duckduckgo_search import DDGS

results = DDGS().text("python programming", max_results=5)
print(results)
```

Sections: Duckduckgo_search, CLI version, Duckduckgo search operators, Regions, DDGS class, Proxy, Exceptions, 1. text(), 2. images(), 3. videos(), 4. news(), Disclaimer

</details>

### django-formtools

A set of high-level abstractions for Django forms

`pip install django-formtools` · installs (wheel) · licence: BSD License · rank 2238 · last release 2026-07-09 · [PyPI](https://pypi.org/project/django-formtools/) · [source](https://github.com/jazzband/django-formtools)

<details><summary>README extract</summary>

Django's "formtools" is a set of high-level abstractions for Django forms.
Currently for form previews and multi-step forms.

This code used to live in Django proper -- in `django.contrib.formtools`
-- but was separated into a standalone package in Django 1.8 to keep the
framework's core clean.

For a full list of available formtools, see ...

</details>

### httpx-retries

A retry layer for HTTPX.

`pip install httpx-retries` · installs (wheel) · licence: MIT License · rank 2279 · last release 2026-07-06 · [PyPI](https://pypi.org/project/httpx-retries/) · [docs](https://will-ockmore.github.io/httpx-retries) · [source](https://github.com/will-ockmore/httpx-retries)

<details><summary>README extract</summary>

<em>A retry layer for HTTPX.</em>

HTTPX Retries implements request retry for HTTPX.

It's very common to deal with flaky and unreliable APIs. When requests fail, your program needs to be able
to retry them.

Install HTTPX Retries using pip:

To get started, add the transport to your client:

Async usage is just as straightforward. ...

Features:
HTTPX Retries builds on the patterns users will expect from `urllib` and `requests`. The typical approach has been
to use urllib3's Retry
utility to configure a retry policy. The equivalent code to match the above example using
requests is: ...

Example:
```python
import httpx
from httpx_retries import RetryTransport

with httpx.Client(transport=RetryTransport()) as client:
    response = client.get("
```

...

</details>

### connect-python

Server and client runtime library for Connect RPC

`pip install connect-python` · installs (wheel) · licence: Apache-2.0 · rank 2300 · last release 2026-03-19 · [PyPI](https://pypi.org/project/connect-python/) · [docs](https://connectrpc.com/docs/python/getting-started/) · [source](https://github.com/connectrpc/connect-python)

<details><summary>README extract</summary>

A Python implementation of Connect: Protobuf RPC that works.

This repo provides a Python implementation of Connect, including both client and server support. It includes a protoc plugin that generates typed client stubs and server interfaces from your `.proto` files, along with runtime libraries for both synchronous and asynchronous code.

Features:
- Clients: Both synchronous and asynchronous clients backed by pyqwest
- Servers: WSGI and ASGI server implementations for use with any Python app server
- Type Safety: Fully type-annotated, including the generated code ...

Example:
```python
from your_service_pb2 import HelloRequest, HelloResponse
from your_service_connect import HelloServiceClient

# Create async client
async def main():
    async with HelloServiceClient(
...

</details>

### scrapy-playwright

Playwright integration for Scrapy

`pip install scrapy-playwright` · installs (wheel) · licence: BSD-3-Clause · rank 2305 · last release 2026-07-10 · [PyPI](https://pypi.org/project/scrapy-playwright/)

<details><summary>README extract</summary>

A Scrapy Download Handler which performs requests using
Playwright for Python.
It can be used to handle pages that require JavaScript (among other things),
while adhering to the regular Scrapy workflow (i.e. without interfering
with request scheduling, item processing, etc). ...

Example:
```python
import scrapy

class AwesomeSpider(scrapy.Spider):
    name = "awesome"

    async def start(self):  # start_requests in Scrapy < 2.13
        # GET request
        yield scrapy.Request(" meta={"playwright": True})
        # POST request
        yield scrapy.FormRequest(
            url="
            formdata={"foo": "bar"},
...
```

...

</details>

### rjsmin

Javascript Minifier

`pip install rjsmin` · installs (wheel) · licence: Apache-2.0 · rank 2311 · last release 2026-10-10 · [PyPI](https://pypi.org/project/rjsmin/)

<details><summary>README extract</summary>

rJSmin is a javascript minifier written in python.

The minifier is based on the semantics of jsmin.c by Douglas Crockford\.

The module is a re-implementation aiming for speed, so it can be used at
runtime (rather than during a preprocessing step). Usually it produces the
same results as the original `jsmin.c`. It differs in the following ways: ...

Sections: Javascript Minifier, Bugs

</details>

### Quart

A Python ASGI web framework with the same API as Flask

`pip install Quart` · installs (wheel) · licence: MIT · rank 2328 · last release 2026-08-29 · [PyPI](https://pypi.org/project/Quart/) · [docs](https://quart.palletsprojects.com) · [source](https://github.com/pallets/quart/)

<details><summary>README extract</summary>

Quart is an async Python web application framework. Using Quart you can,

- render and serve HTML templates,
- write (RESTful) JSON APIs,
- serve WebSockets,
- stream request and response data,
- do pretty much anything over the HTTP or WebSocket protocols.

Example:
```python
from quart import Quart, render_template, websocket

app = Quart(name)

@app.route("/")
async def hello():
    return await render_template("index.html")

@app.route("/api")
async def json():
    return {"hello": "world"}

@app.websocket("/ws")
async def ws():
    while True:
        await websocket.send("hello")
...
```

Sections: Quart, Quickstart, Help, Relationship with Flask, Migrating from Flask

</details>

### Flask-Compress

Compress responses in your Flask app with gzip, deflate, brotli or zstandard.

`pip install Flask-Compress` · installs (wheel) · licence: MIT License · rank 2343 · last release 2026-10-29 · [PyPI](https://pypi.org/project/Flask-Compress/)

<details><summary>README extract</summary>

Flask-Compress allows you to easily compress your Flask application's responses with gzip, deflate, brotli or zstd. It originally started as a fork of Flask-gzip. Supported Python versions are 3.9 and newer.

The preferred solution is to have a server (like Nginx) automatically compress the static files for you. ...

Example:
```python
from flask import Flask
from flask_compress import Compress
from flask_cache import Cache

# Initializing flask app
app = Flask(name)

cache = Cache(config={
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 60*60  # 1 hour cache timeout
})
cache.init_app(app)

# Define a function to return cache key for incoming requests
...
```

Sections: Flask-Compress, How it works, Using Flask-Compress, Globally, Per-view compression, Cache example, Options

</details>

### hishel

Elegant HTTP Caching for Python

`pip install hishel` · installs (wheel) · licence: BSD License · rank 2346 · last release 2026-11-05 · [PyPI](https://pypi.org/project/hishel/) · [source](https://github.com/karpetrosyan/hishel)

<details><summary>README extract</summary>

Elegant HTTP Caching for Python

Hishel (հիշել, *to remember* in Armenian) is a modern HTTP caching library for Python. It adds caching to HTTPX, Requests and ASGI applications with minimal code changes, either by your own limits or by following the RFC 9111 specification. ...

Sections: Hishel, ✨ Features

</details>

### acme

ACME protocol implementation in Python

`pip install acme` · installs (wheel) · licence: Apache-2.0 · rank 2376 · last release 2026-10-29 · [PyPI](https://pypi.org/project/acme/)

### rcssmin

CSS Minifier

`pip install rcssmin` · installs (wheel) · licence: Apache-2.0 · rank 2406 · last release 2026-10-10 · [PyPI](https://pypi.org/project/rcssmin/)

<details><summary>README extract</summary>

RCSSmin is a CSS minifier.

The minifier is based on the semantics of the YUI compressor\, which itself
is based on the rule list by Isaac Schlueter\.

This module is a re-implementation aiming for speed instead of maximum
compression, so it can be used at runtime (rather than during a preprocessing
step). ...

Sections: CSS Minifier, Bugs

</details>

### cloudscraper

A Python module to bypass Cloudflare's anti-bot page.

`pip install cloudscraper` · installs (wheel) · licence: MIT License · rank 2407 · last release 2023-04-25 · [PyPI](https://pypi.org/project/cloudscraper/)

<details><summary>README extract</summary>

A simple Python module to bypass Cloudflare's anti-bot page (also known as "I'm Under Attack Mode", or IUAM), implemented with Requests. Cloudflare changes their techniques periodically, so I will update this repo frequently.

This can be useful if you wish to scrape or crawl a website protected with Cloudflare. ...

Example:
```python
import cloudscraper

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
print(scraper.get("  # => "<!DOCTYPE html>..."
```

Sections: cloudscraper, Dependencies, Javascript Interpreters and Engines, Usage, Options, Disable Cloudflare V1, Description, Parameters, Example, Brotli, Browser / User-Agent Filtering

</details>

### libsass

Sass for Python: A straightforward binding of libsass for Python.

`pip install libsass` · installs (wheel) · licence: MIT License · rank 2421 · last release 2024-01-06 · [PyPI](https://pypi.org/project/libsass/)

<details><summary>README extract</summary>

This package provides a simple Python extension module `sass` which is
binding LibSass (written in C/C++ by Hampton Catlin and Aaron Leung).
It's very straightforward and there isn't any headache related to Python
distribution/deployment. ...

Features:
- You don't need any Ruby/Node.js stack at all, for development or deployment
 either.
- Fast. (LibSass is written in C++.)
- Simple API. See the below example code for details.
- Custom functions.
- `@import` callbacks. ...

Example:
```python
>>> import sass
>>> print sass.compile(string='a { b { color: blue; } }')
a b {
  color: blue; }
```

Sections: libsass-python: Sass/SCSS for Python, Features, Example, Docs, Credit

</details>

### algoliasearch

A fully-featured and blazing-fast Python API client to interact with Algolia.

`pip install algoliasearch` · installs (wheel) · licence: MIT License · rank 2466 · last release 2026-10-29 · [PyPI](https://pypi.org/project/algoliasearch/) · [source](https://github.com/algolia/algoliasearch-client-python)

<details><summary>README extract</summary>

Documentation •
 Django •
 Community Forum •
 Stack Overflow •
 Report a bug •
 Support

- Thin & minimal low-level HTTP client to interact with Algolia's API
- Supports Python from `3.8`

Example:
```python
from algoliasearch.search.client import SearchClient

_client = SearchClient("YOUR_APP_ID", "YOUR_API_KEY")

# Add a new record to your Algolia index
response = await _client.save_object(
    index_name="",
    body={
        "objectID": "id",
        "test": "val",
    },
)

# use the class directly
print(response)

# print the JSON response
...
```

Sections: ✨ Features, 💡 Getting Started, ❓ Troubleshooting

</details>

### cloudinary

Upload, transform, optimize, and manage images and videos with Cloudinary from Python or Django.

`pip install cloudinary` · installs (wheel) · licence: MIT License · rank 2501 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cloudinary/) · [source](https://github.com/cloudinary/pycloudinary)

<details><summary>README extract</summary>

Upload, transform, optimize, and manage images and videos with Cloudinary from Python or Django — the `cloudinary` package on PyPI.

Example:
```python
import cloudinary
import cloudinary.uploader  # cloudinary.uploader must be imported explicitly

# Configuration is read from CLOUDINARY_URL automatically.

def main():
    # Upload a remote image (a local file path works the same way)
    result = cloudinary.uploader.upload(
        "
        public_id="quickstart-sample",
    )
...
```

Sections: Cloudinary Python SDK, Quick start, Common tasks, When to use this SDK, Documentation, For AI coding agents

</details>

### jwt

JSON Web Token library for Python 3.

`pip install jwt` · installs (wheel) · licence: Apache Software License · rank 2505 · last release 2025-06-23 · [PyPI](https://pypi.org/project/jwt/) · [source](https://github.com/GehirnInc/python-jwt.git)

<details><summary>README extract</summary>

*python-jwt* is a JSON Web Token (JWT) implementation in Python developed by Gehirn Inc.

Example:
```python
import json
from datetime import datetime, timedelta, timezone

from jwt import (
    JWT,
    jwk_from_dict,
    jwk_from_pem,
)
from jwt.utils import get_int_from_datetime

instance = JWT()

message = {
    'iss': '
    'sub': 'yosida95',
    'iat': get_int_from_datetime(datetime.now(timezone.utc)),
    'exp': get_int_from_datetime(
...
```

Sections: python-jwt, Examples, Implementation Details

</details>

### itemloaders

Base library for scrapy's ItemLoader

`pip install itemloaders` · installs (wheel) · licence: BSD-3-Clause · rank 2510 · last release 2026-09-29 · [PyPI](https://pypi.org/project/itemloaders/) · [docs](https://itemloaders.readthedocs.io/) · [source](https://github.com/scrapy/itemloaders)

<details><summary>README extract</summary>

`itemloaders` is a library that helps you collect data from HTML and XML sources.

It comes in handy to extract data from web pages, as it supports
data extraction using CSS and XPath Selectors.

It's specially useful when you need to standardize the data from many sources. ...

Example:
```python
from itemloaders import ItemLoader
from parsel import Selector

html_data = '''
<!DOCTYPE html>

        Some random product page

        Some random product page

        $ 100.12

'''
loader = ItemLoader(selector=Selector(html_data))
loader.add_xpath('name', '//div[@class="product_name"]/text()')
...
```

</details>

### itemadapter

Common interface for data container classes

`pip install itemadapter` · installs (wheel) · licence: BSD-3-Clause · rank 2517 · last release 2026-10-29 · [PyPI](https://pypi.org/project/itemadapter/) · [source](https://github.com/scrapy/itemadapter)

<details><summary>README extract</summary>

The `ItemAdapter` class is a wrapper for data container objects, providing a
common interface to handle objects of different types in an uniform manner,
regardless of their underlying implementation.

Currently supported types are: ...

Example:
```python
>>> from dataclasses import dataclass
>>> from itemadapter import ItemAdapter
>>> @dataclass
... class InventoryItem:
...     name: str
...     price: float
...     stock: int
>>>
```

...

</details>

### coloraide

A color library for Python.

`pip install coloraide` · installs (wheel) · licence: MIT · rank 2552 · last release 2026-11-02 · [PyPI](https://pypi.org/project/coloraide/)

<details><summary>README extract</summary>

[][donate-link]
[][codecov-link]
[][pypi-link]
[][pypi-link]
[][pypi-link]
[][license-link]

Features:
ColorAide is a pure Python, object oriented approach to colors.

ColorAide particularly has a focus on the following:

- Accurate colors.

- Proper round tripping (where reasonable).

- Be generally easy to pick up for the average user. ...

Example:
```python
>>> from coloraide import Color
>>> c = Color("red")
>>> c.to_string()
'rgb(255 0 0)'
>>> c.convert('hsl').to_string()
'hsl(0 100% 50%)'
>>> c.set("lch.chroma", 30).to_string()
'rgb(173.81 114.29 97.218)'
>>> Color("blue").mix("yellow", space="lch").to_string()
'rgb(255 65.751 107.47)'
```

Sections: ColorAide, Overview, Documentation

</details>

### repoze-lru

A tiny LRU cache implementation and decorator

`pip install repoze-lru` · installs (wheel) · licence: LicenseRef-Repoze-BSD-derived · rank 2553 · last release 2026-05-16 · [PyPI](https://pypi.org/project/repoze-lru/) · [docs](https://repozelru.readthedocs.io/en/stable/index.html) · [source](https://github.com/repoze/repoze.lru)

<details><summary>README extract</summary>

`repoze.lru` is a LRU (least recently used) cache implementation. Keys and
values that are not used frequently will be evicted from the cache faster
than keys and values that are used frequently. It works under Python 2.7 and Python 3.4+.

Please see `docs/index.rst` for detailed documentation, or view them
online at

</details>

### cheroot

Highly-optimized, pure-python HTTP server

`pip install cheroot` · installs (wheel) · licence: BSD License · rank 2587 · last release 2025-11-07 · [PyPI](https://pypi.org/project/cheroot/)

<details><summary>README extract</summary>

Cheroot is the high-performance, pure-Python HTTP server used by CherryPy.

</details>

### pusher

A Python library to interract with the Pusher Channels API

`pip install pusher` · installs (wheel) · licence: MIT License · rank 2607 · last release 2026-03-19 · [PyPI](https://pypi.org/project/pusher/)

<details><summary>README extract</summary>

A Python library to interract with the Pusher Channels API

</details>

### django-js-asset

script tag with additional attributes for django.forms.Media

`pip install django-js-asset` · installs (wheel) · licence: BSD License · rank 2665 · last release 2026-10-26 · [PyPI](https://pypi.org/project/django-js-asset/)

<details><summary>README extract</summary>

Example:
```python
from js_asset import JSON, InlineStyle, Script, Stylesheet

forms.Media(js=[
    JSON({"configuration": 42}, id="widget-configuration"),
    Stylesheet("widget/style.css", media="all"),
    InlineStyle("p{color:red;}"),
    Script("widget/script.js", type="module"),
    Script("widget/data.js", **{"id": "data-script", "data-answer": "42"}),
])
```

Sections: Assets, Deduplication, Import maps, Rendering media in views and the admin, In a front-facing view, In the Django admin, CSP nonces, Django 6.1 and newer (built-in CSP), Django 6.0 (built-in CSP, no `csp_nonce_attr`), Django 4.2 to 5.x (with `django-csp`), Anywhere: set the nonce explicitly

</details>

### PasteDeploy

Load, configure, and compose WSGI applications and servers

`pip install PasteDeploy` · installs (wheel) · licence: MIT License · rank 2681 · last release 2023-11-21 · [PyPI](https://pypi.org/project/PasteDeploy/) · [docs](https://docs.pylonsproject.org/projects/pastedeploy/en/latest/)

<details><summary>README extract</summary>

This tool provides code to load WSGI applications and servers from
URIs. These URIs can refer to Python eggs for INI-style configuration
files. Paste Script provides
commands to serve applications based on this configuration file.

The latest version is available on GitHub (or download a wheel or tarball from
PyPI). ...

</details>

### django-compressor

Compresses linked and inline JavaScript or CSS into single cached files.

`pip install django-compressor` · installs (wheel) · licence: MIT · rank 2685 · last release 2025-11-10 · [PyPI](https://pypi.org/project/django-compressor/) · [source](https://github.com/django-compressor/django-compressor)

<details><summary>README extract</summary>

Django Compressor processes, combines and minifies linked and inline
Javascript or CSS in a Django template into cacheable static files.

It supports compilers such as coffeescript, LESS and SASS and is
extensible by custom processing steps. ...

Sections: Django Compressor, How it works, Configurability & Extensibility

</details>

### django-silk

Silky smooth profiling for the Django Framework

`pip install django-silk` · installs (wheel) · licence: MIT License · rank 2693 · last release 2026-09-12 · [PyPI](https://pypi.org/project/django-silk/)

<details><summary>README extract</summary>

Silk is a live profiling and inspection tool for the Django framework. Silk intercepts and stores HTTP requests and database queries before presenting them in a user interface for further inspection:

Features:
Silk primarily consists of:

* Middleware for intercepting Requests/Responses
* A wrapper around SQL execution for profiling of database queries
* A context manager/decorator for profiling blocks of code and functions either manually or dynamically. ...

Example:
```python
from silk.profiling.profiler import silk_profile

@silk_profile(name='View Blog Post')
def post(request, post_id):
    p = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {
        'post': p
    })
```

...

</details>

### djangorestframework-dataclasses

A dataclasses serializer for Django REST Framework

`pip install djangorestframework-dataclasses` · installs (wheel) · licence: BSD License · rank 2717 · last release 2025-05-14 · [PyPI](https://pypi.org/project/djangorestframework-dataclasses/) · [docs](https://github.com/oxan/djangorestframework-dataclasses/blob/master/README.rst) · [source](https://github.com/oxan/djangorestframework-dataclasses)

<details><summary>README extract</summary>

A dataclasses serializer for the Django REST Framework.


* Python (3.8+)
* Django (3.2+)
* Django REST Framework (3.11+)

These are the supported Python and package versions. Older versions will probably work as well, but aren't tested.

Example:
```python
from rest_framework_dataclasses.serializers import DataclassSerializer
```

Sections: Dataclasses serializer, Requirements, Basic usage, Field mapping, Customize field generation, Changing default behaviour, Nesting, Nested dataclasses, Nesting models, New serializer field types, DefaultDecimalField, EnumField, IterableField, MappingField

</details>

### django-crispy-forms

Best way to have Django DRY forms

`pip install django-crispy-forms` · installs (wheel) · licence: MIT · rank 2723 · last release 2026-07-29 · [PyPI](https://pypi.org/project/django-crispy-forms/)

<details><summary>README extract</summary>

The best way to have Django DRY forms. Build programmatic reusable layouts out of components, having full control of the rendered HTML without writing HTML in templates. All this without breaking the standard way of doing things in Django, so it plays nice with any other form application. ...

Sections: django-crispy-forms, Example, Documentation, Special thanks

</details>

### python-whois

Whois querying and parsing of domain registration information.

`pip install python-whois` · installs (wheel) · licence: MIT License · rank 2725 · last release 2025-10-07 · [PyPI](https://pypi.org/project/python-whois/)

<details><summary>README extract</summary>

- Create a simple importable Python module which will produce parsed
 WHOIS data for a given domain.
- Able to extract data for all the popular TLDs (com, org, net, ...)
- Query a WHOIS server directly instead of going through an
 intermediate web service like many others do.

Example:
```python
>>> import whois
>>> w = whois.whois('example.com')
>>> w.expiration_date  # dates converted to datetime object
datetime.datetime(2022, 8, 13, 4, 0, tzinfo=tzoffset('UTC', 0))
>>> w.text  # the content downloaded from whois server
u'\nDomain Name: EXAMPLE.COM
Registry Domain ID: 2336799_DOMAIN_COM-VRSN
...'

...
```

Sections: Goal, Example, Using a proxy., Problems?

</details>

### josepy

JOSE protocol implementation in Python

`pip install josepy` · installs (wheel) · licence: Apache-2.0 · rank 2729 · last release 2025-10-14 · [PyPI](https://pypi.org/project/josepy/)

<details><summary>README extract</summary>

JOSE protocol implementation in Python using cryptography

For more information about contributing to this project, see CONTRIBUTING.md.

</details>

### browserforge

Intelligent browser header & fingerprint generator

`pip install browserforge` · installs (wheel) · licence: Apache Software License · rank 2738 · last release 2026-02-03 · [PyPI](https://pypi.org/project/browserforge/) · [source](https://github.com/daijro/browserforge)

<details><summary>README extract</summary>

BrowserForge is a browser header and fingerprint generator that mimics the frequency of different browsers, operating systems, and devices found in the wild.

It is a reimplementation of Apify's fingerprint-suite in Python.

Features:
- Uses a Bayesian generative network to mimic actual web traffic
- Extremely fast runtime (0.1-0.2 miliseconds)
- Easy and simple for humans to use ...

Example:
```python
>>> from browserforge.headers import HeaderGenerator
>>> headers = HeaderGenerator()
>>> headers.generate()
...
```

...

</details>

### language-tags

This project is a Python version of the language-tags Javascript project.

`pip install language-tags` · installs (wheel) · licence: MIT · rank 2759 · last release 2026-10-23 · [PyPI](https://pypi.org/project/language-tags/) · [docs](https://language-tags.readthedocs.io/en/latest/) · [source](https://github.com/OnroerendErfgoed/language-tags)

<details><summary>README extract</summary>

This Python API offers a way to validate and lookup languages tags.

It is based on BCP 47 (RFC 5646) and the latest IANA language subtag registry.

This project will be updated as the standards change.

Language-tags 1.0.0 only supports Python 3, for Python 2 support, please use language-tags 0.5.0. ...

Sections: IANA Language Tags for Python, Standard, JSON data, Javascript version, 1.3.2, 1.3.1, 1.3.0, 1.2.0, 1.1.0, 1.0.0, 0.5.0, 0.4.6, 0.4.5, 0.4.4

</details>

### django-admin-sortable2

Generic drag-and-drop sorting for the List, the Stacked- and the Tabular-Inlines Views in the Django Admin

`pip install django-admin-sortable2` · installs (wheel) · licence: MIT License · rank 2792 · last release 2026-01-22 · [PyPI](https://pypi.org/project/django-admin-sortable2/)

<details><summary>README extract</summary>

This Django package adds functionality for generic drag-and-drop ordering of items in the List, the Stacked- and the
Tabular-Inlines Views of the Django Admin interface.

Check the demo: ...

Sections: django-admin-sortable2, Version 2.0, Project's Home

</details>

### drf-nested-routers

Nested resources for the Django Rest Framework

`pip install drf-nested-routers` · installs (wheel) · licence: Apache Software License · rank 2956 · last release 2026-07-31 · [PyPI](https://pypi.org/project/drf-nested-routers/)

<details><summary>README extract</summary>

**This is a work in progress. It "works for me" at www.apiregistro.com.br,
but I cannot warranty that it fully "works everywhere" yet. Join us on Gitter (below) if you need some help.**

This package provides routers and fields to create nested resources in the Django Rest Framework ...

Sections: drf-nested-routers, Requirements & Compatibility, urls.py, Official DRF docs on this option, views.py, For Django' ORM-based resources, OR: non-ORM resources, serializers.py, generates, /clients/, /clients/{pk}/, /clients/{client_pk}/maildrops/

</details>

### pyramid

The Pyramid Web Framework, a Pylons project

`pip install pyramid` · installs (wheel) · licence: LicenseRef-Repoze-BSD-derived · rank 3003 · last release 2026-03-11 · [PyPI](https://pypi.org/project/pyramid/) · [docs](https://docs.pylonsproject.org/projects/pyramid/en/2.1-branch/) · [source](https://github.com/Pylons/pyramid)

<details><summary>README extract</summary>

Pyramid is a small, fast, down-to-earth, open source Python web framework.
It makes real-world web application development
and deployment more fun, more predictable, and more productive.
Try Pyramid, browse its add-ons and documentation, and get an overview.

Pyramid is a project of the Pylons Project.

Example:
```python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello World!')

if name == 'main':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
...
```

</details>

### django-admin-list-filter-dropdown

Use dropdowns in Django admin list filter

`pip install django-admin-list-filter-dropdown` · installs (wheel) · licence: MIT License · rank 3009 · last release 2019-10-14 · [PyPI](https://pypi.org/project/django-admin-list-filter-dropdown/)

### django-cacheops

A slick ORM cache with automatic granular event-driven invalidation for Django.

`pip install django-cacheops` · installs (wheel) · licence: BSD License · rank 3058 · last release 2025-04-20 · [PyPI](https://pypi.org/project/django-cacheops/)

<details><summary>README extract</summary>

A slick app that supports automatic or manual queryset caching and automatic
granular event-driven invalidation.

It uses redis as backend for ORM cache and redis or
filesystem for simple time-invalidated one.

And there is more to it:

- decorators to cache any user function or view as a queryset or by time ...

Example:
```python
Article.objects.filter(tag=2).cache()
```

Sections: Cacheops, Requirements, Setup, Usage, Invalidation, Components, Simple time-invalidated cache, File Cache, Django templates integration, Jinja2 extension, Special topics, Transactions, Dog-pile effect prevention, Sharing redis instance

</details>

### qh3

A lightweight and fast implementation of QUIC and HTTP/3

`pip install qh3` · installs (wheel) · licence: BSD License · rank 3095 · last release 2026-10-25 · [PyPI](https://pypi.org/project/qh3/) · [docs](https://qh3.readthedocs.io/)

<details><summary>README extract</summary>

`qh3` is a fast QUIC and HTTP/3 implementation for Python, backed by a
native Rust transport core. It is a maintained fork of `aioquic` and is not
a drop-in replacement.

It provides: ...

Sections: qh3, Documentation, Standards

</details>

### ariadne

Ariadne is a Python library for implementing GraphQL servers.

`pip install ariadne` · installs (wheel) · licence: BSD-3-Clause · rank 3123 · last release 2026-10-07 · [PyPI](https://pypi.org/project/ariadne/) · [source](https://github.com/mirumee/ariadne)

<details><summary>README extract</summary>

- - - - -

Ariadne is a Python library for implementing GraphQL servers.

- Schema-first: Ariadne enables Python developers to use schema-first approach to the API implementation. This is the leading approach used by the GraphQL community and supported by dozens of frontend and backend developer tools, examples, and learning resources. ...

Features:
- Simple, quick to learn and easy to memorize API.
- Queries, mutations and input types.
- Asynchronous resolvers and query execution.
- Subscriptions (async and sync generators, with customizable handlers). ...

Example:
```python
from ariadne import ObjectType, QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

# Define types using Schema Definition Language (
...

</details>

### stagehand

Browserbase's SDK for building browser agents

`pip install stagehand` · installs (wheel) · licence: MIT · rank 3130 · last release 2026-11-04 · [PyPI](https://pypi.org/project/stagehand/) · [docs](https://docs.stagehand.dev) · [source](https://github.com/browserbase/stagehand)

<details><summary>README extract</summary>

Stagehand is the SDK for browser agents.

 Read the Docs

Stagehand is the SDK for browser agents. Playwright was built for testing, Stagehand is built for agents. Use familiar APIs, self-healing actions, and network-level security across TypeScript, Python, and Go.

Features:
Stagehand gives browser agents an interface built for how they actually work. It combines familiar Playwright-style APIs with self-healing actions, agent-optimized page context, and native support for complex DOM structures like out-of-process ...

Example:
```python
import asyncio
import os

from pydantic import BaseModel

from stagehand import Stagehand, browserbase, local_browser

class PullRequest(BaseModel):
    author: str
    title: str

async def main() -> None:
...

</details>

### drf-extensions

Extensions for Django REST Framework

`pip install drf-extensions` · installs (wheel) · licence: MIT License · rank 3164 · last release 2025-04-10 · [PyPI](https://pypi.org/project/drf-extensions/)

<details><summary>README extract</summary>

DRF-extensions is a collection of custom extensions for Django REST Framework

</details>

### django-admin-inline-paginator

The "Django Admin Inline Paginator" is simple way to paginate your inline in django admin

`pip install django-admin-inline-paginator` · installs (wheel) · licence: MIT License · rank 3202 · last release 2023-04-26 · [PyPI](https://pypi.org/project/django-admin-inline-paginator/)

<details><summary>README extract</summary>

The "Django Admin Inline Paginator" is simple way to paginate your inline in django admin

If you use or like the project, click `Star` and `Watch` to generate metrics and i evaluate project continuity.

Example:
```python
from django_admin_inline_paginator.admin import TabularInlinePaginated

class ModelWithFKAdminInline(TabularInlinePaginated):
    fields = (...)
    per_page = 1
    model = ModelWithFK
```

Sections: Django Admin Inline Paginator, Usage, Advanced Usage, Images

</details>

### aiohttp-jinja2

jinja2 template renderer for aiohttp.web (http server for asyncio)

`pip install aiohttp-jinja2` · installs (wheel) · licence: Apache Software License · rank 3217 · last release 2023-11-18 · [PyPI](https://pypi.org/project/aiohttp-jinja2/)

<details><summary>README extract</summary>

jinja2 template renderer for aiohttp.web.

__ aiohttp_web

Example:
```python
app = web.Application()
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('/path/to/templates/folder'))
```

Sections: aiohttp_jinja2, Usage, CHANGES, 1.6 (2023-11-18), 1.5.1 (2023-02-01), 1.5 (2021-08-21), 1.4.2 (2020-11-23), 1.4.1 (2020-11-22), 1.4.0 (2020-11-12), 1.3.0 (2020-10-30), 1.2.0 (2019-10-21), 1.1.1 (2019-04-25), 1.1.0 (2018-09-05), 1.0.0 (2018-03-12)

</details>

### webargs

Declarative parsing and validation of HTTP request objects, with built-in support for popular web frameworks, including Flask, Django, Bottle, Tornado, Pyramid, Falcon, and aiohttp.

`pip install webargs` · installs (wheel) · licence: MIT License · rank 3227 · last release 2025-10-29 · [PyPI](https://pypi.org/project/webargs/) · [source](https://github.com/marshmallow-code/webargs)

<details><summary>README extract</summary>

Homepage:

webargs is a Python library for parsing and validating HTTP request objects, with built-in support for popular web frameworks, including Flask, Django, Bottle, Tornado, Pyramid, Falcon, and aiohttp.

Example:
```python
from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

app = Flask(name)

@app.route("/")
@use_args({"name": fields.Str(required=True)}, location="query")
def index(args):
    return "Hello " + args["name"]

if name == "main":
    app.run()

# curl
# Hello World
```

Sections: webargs, Documentation, Project Links

</details>

### dominate

Dominate is a Python library for creating and manipulating HTML documents using an elegant DOM API.

`pip install dominate` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 3247 · last release 2026-10-30 · [PyPI](https://pypi.org/project/dominate/) · [source](https://github.com/Knio/dominate)

_README extract left out: share-alike licence._

### pyramid-debugtoolbar

A package which provides an interactive HTML debugger for Pyramid application development

`pip install pyramid-debugtoolbar` · installs (wheel) · licence: Repoze Public License · rank 3356 · last release 2024-02-05 · [PyPI](https://pypi.org/project/pyramid-debugtoolbar/)

<details><summary>README extract</summary>

`pyramid_debugtoolbar` provides a debug toolbar useful while you're
developing your Pyramid application.

Note that `pyramid_debugtoolbar` is a blatant rip-off of Michael van
Tellingen's `flask-debugtoolbar` (which itself was derived from Rob Hudson's
`django-debugtoolbar`). ...

Example:
```python
require.config({
  paths: {
    "jquery": "jquery-1.7.2.min",
    "toolbar": "/_debug_toolbar/static/js/toolbar"
  }
});

require(["jquery", "toolbar"], function($, toolbar) {
  $(function() {
    // your module
  });
});
```

...

</details>

### algoliasearch-django

Algolia Search integration for Django

`pip install algoliasearch-django` · installs (wheel) · licence: MIT License · rank 3421 · last release 2025-01-06 · [PyPI](https://pypi.org/project/algoliasearch-django/)

<details><summary>README extract</summary>

Documentation •
 Community Forum •
 Stack Overflow •
 Report a bug •
 FAQ •
 Support

You can find the full reference on Algolia's website.

1. Setup

 - Introduction
 - Install
 - Setup
 - Quick Start

1. Commands

 - Commands

1. Search

 - Search

1. Geo-Search

 - Geo-Search

1. Tags

 - Tags

1. Options ...

Example:
```python
# index.py

import algoliasearch_django as algoliasearch

from .models import YourModel

algoliasearch.register(YourModel)
```

Sections: API Documentation, Setup, Introduction, Quick Start, Commands, Search, Geo-Search, Tags, Options

</details>

### djangorestframework-role-filters

django-rest-framework-role-filters

`pip install djangorestframework-role-filters` · installs (wheel) · licence: MIT License · rank 3468 · last release 2023-10-06 · [PyPI](https://pypi.org/project/djangorestframework-role-filters/)

<details><summary>README extract</summary>

Features:
I want work easily with roles without multiple ifs in code

Example:
```python
from rest_framework_role_filters.role_filters import RoleFilter

from .serializers import PostSerializerForUser

class AdminRoleFilter(RoleFilter):
    role_id = 'admin'

class UserRoleFilter(RoleFilter):
    role_id = 'user'

    def get_allowed_actions(self, request, view, obj=None):
...
```

Sections: django-rest-framework-role-filters, Why i wrote this project?, How to use

</details>

### csp-toolkit

Parse, analyze, generate, and find bypasses in Content Security Policy headers

`pip install csp-toolkit` · installs (wheel) · licence: MIT · rank 3471 · last release 2026-09-19 · [PyPI](https://pypi.org/project/csp-toolkit/) · [docs](https://sampsonc.github.io/csp_toolkit/) · [source](https://github.com/sampsonc/csp_toolkit)

<details><summary>README extract</summary>

Parse, analyze, generate, and find bypasses in Content Security Policy headers.

A Python library and CLI tool for security researchers and bug bounty hunters. Auto-generate CSPs by crawling a website, analyze policies with 23 weakness checks, find bypasses against a database of 79 domains (66 JSONP + 13 CDNs), score policies A+ to F, emit a ...

Example:
```python
import csp_toolkit

# Parse
policy = csp_toolkit.parse("script-src 'self' 'unsafe-inline' *.googleapis.com")

# Analyze + score
findings = csp_toolkit.analyze(policy)
grade, score = csp_toolkit.score_policy(policy)
print(f"{grade} ({score}/100), {len(findings)} findings")

# Find bypasses
bypasses = csp_toolkit.find_bypasses(policy)
...
```

...

</details>

### cuid

Fast, scalable unique ID generation

`pip install cuid` · installs from source (sdist only) · licence: Apache Software License · rank 3482 · last release 2023-03-06 · [PyPI](https://pypi.org/project/cuid/)

<details><summary>README extract</summary>

Implementation of in Python.

A `cuid` is a portable and sequentially-ordered unique identifier designed for
horizontal scalability and speed -- this version is ported from the reference
implementation in Javascript.

NOTE: Particularly if you have security concerns, the `cuid` standard has been deprecated in favor of `cuid2`! ...

</details>

### urllib3-future

urllib3.future is a powerful HTTP 1.1, 2, and 3 client with both sync and async interfaces

`pip install urllib3-future` · installs (wheel) · licence: MIT · rank 3490 · last release 2026-10-28 · [PyPI](https://pypi.org/project/urllib3-future/) · [docs](https://urllib3future.readthedocs.io) · [source](https://github.com/jawah/urllib3.future)

<details><summary>README extract</summary>

Modern HTTP. Familiar urllib3 API. Broad deployment choice.

urllib3.future is an independently maintained, compatibility-first fork of
urllib3. It provides HTTP/1.1, HTTP/2, HTTP/3, synchronous and asynchronous
APIs, multiplexing, advanced DNS resolution, and multiple TLS backends while
preserving the established urllib3 programming model. ...

Example:
```python
import urllib3

with urllib3.PoolManager() as pool:
    response = pool.request("GET", "

print(response.status)   # 200
print(response.version)  # 11, 20, or 30
print(response.data)
```

...

</details>

### falcon

The ultra-reliable, fast ASGI+WSGI framework for building data plane APIs at scale.

`pip install falcon` · installs (wheel) · licence: Apache-2.0 · rank 3520 · last release 2026-09-30 · [PyPI](https://pypi.org/project/falcon/) · [docs](https://falcon.readthedocs.io/en/stable/) · [source](https://github.com/falconry/falcon)

<details><summary>README extract</summary>

|codecov.ioPyPI packagePython versions|

Falcon is a minimalist ASGI/WSGI framework for
building mission-critical REST APIs and microservices, with a focus on
reliability, correctness, and performance at scale.

When it comes to building HTTP APIs, other frameworks weigh you down with tons
of dependencies and unnecessary abstractions. ...

Features:
Falcon tries to do as little as possible while remaining highly effective.

- ASGI, WSGI, and WebSocket support
- Native `asyncio` support
- No reliance on magic globals for routing and state management ...

Example:
```python
# examples/things.py

# Let's get this party started!
from wsgiref.simple_server import make_server

import falcon

# Falcon follows the REST architectural style, meaning (among
...

</details>

### fastapi-users

Ready-to-use and customizable users management for FastAPI

`pip install fastapi-users` · installs (wheel) · licence: MIT License · rank 3534 · last release 2026-03-27 · [PyPI](https://pypi.org/project/fastapi-users/) · [docs](https://fastapi-users.github.io/fastapi-users/) · [source](https://github.com/fastapi-users/fastapi-users)

<details><summary>README extract</summary>

Ready-to-use and customizable users management for FastAPI

> [!NOTE]
> This project is now in maintenance mode. While we'll continue to provide security updates and dependency maintenance, no new features will be added. We encourage you to explore the project and use it as-is, knowing it will remain stable and secure. ...

Features:
- [x] Extensible base user model
- [x] Ready-to-use register, login, reset password and verify e-mail routes
- [x] Ready-to-use social OAuth2 login flow
- [x] Dependency callables to inject current user in route
- [x] Pluggable password validation ...

Sections: FastAPI Users, Features, Setup environment, Run unit tests, Format the code, Serve the documentation

</details>

### jsmin

JavaScript minifier.

`pip install jsmin` · installs from source (sdist only) · licence: MIT License · rank 3544 · last release 2022-01-16 · [PyPI](https://pypi.org/project/jsmin/)

<details><summary>README extract</summary>

JavaScript minifier.

Example:
```python
from jsmin import jsmin
with open('myfile.js') as js_file:
    minified = jsmin(js_file.read())
```

Sections: jsmin, Usage, Where to get it, v3.0.0 (2021-09-08) Ben Bradshaw, v2.2.2 (2017-05-01) Tikitu de Jager, v2.2.1 (2016-03-06) Tikitu de Jager, v2.2.0 (2015-12-19) Tikitu de Jager, v2.1.6 (2015-10-14) Tikitu de Jager, v2.1.5 (2015-10-11) Tikitu de Jager, v2.1.4 (2015-08-23) Tikitu de Jager, v2.1.3 (2015-08-09) Tikitu de Jager, v2.1.2 (2015-07-12) Tikitu de Jager, v2.1.1 (2015-02-14) Tikitu de Jager, v2.1.0 (2014-12-24) Tikitu de Jager

</details>

### jh2

HTTP/2 State-Machine based protocol implementation

`pip install jh2` · installs (wheel) · licence: MIT · rank 3555 · last release 2026-09-21 · [PyPI](https://pypi.org/project/jh2/) · [source](https://github.com/jawah/h2)

### wassima

Access your OS root certificates with utmost ease

`pip install wassima` · installs (wheel) · licence: MIT · rank 3579 · last release 2026-10-22 · [PyPI](https://pypi.org/project/wassima/) · [docs](https://wassima.readthedocs.io) · [source](https://github.com/jawah/wassima)

<details><summary>README extract</summary>

I named this library after my wife, whom I trust the most. ❤️

This project offers you a great alternative to the MPL licensed certifi.

This project allows you to access your original operating system trust store, thus
helping you to verify the remote peer certificates. ...

Example:
```python
import wassima

ctx = wassima.create_default_ssl_context()
# ... The context magically contain your system root CAs, the rest is up to you!
```

Sections: Wassima 🔒, Get started, ⏱️ Cache invalidation

</details>

### ct3

Cheetah is a template engine and code generation tool

`pip install ct3` · installs (wheel) · licence: MIT License · rank 3585 · last release 2025-11-29 · [PyPI](https://pypi.org/project/ct3/) · [docs](https://cheetahtemplate.org/users_guide/index.html)

<details><summary>README extract</summary>

Cheetah3 is a free and open source template engine and code generation tool.

It can be used standalone or combined with other tools and frameworks. Web
development is its principle use, but Cheetah is very flexible and
is also being used to generate C++ game code, Java, sql, form emails
and even Python code. ...

Sections: Documentation, Recent Changes

</details>

### niquests

Niquests is a simple, yet elegant, HTTP library. It is a drop-in replacement for Requests, which is under feature freeze.

`pip install niquests` · installs (wheel) · licence: Apache-2.0 · rank 3607 · last release 2026-09-23 · [PyPI](https://pypi.org/project/niquests/) · [docs](https://niquests.readthedocs.io) · [source](https://github.com/jawah/niquests)

<details><summary>README extract</summary>

Niquests is a simple, yet elegant, HTTP library. It is a drop-in replacement for Requests, which is under feature freeze. ✨ Were you used to betamax, requests-mock, responses, ...? See how they still work! We got you covered.

 Target:

 Conditions: All default parameters, one shared session, everything simultaneously.

 HTTP/2 when supported. ...

Example:
```python
>>> import niquests
>>> r = niquests.get(' params={'hello': 'world'}, timeout=10)
>>> r.raise_for_status()
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf-8'
>>> r.json()['args']
{'hello': ['world']}
```

Sections: Live Benchmark, 📝 Why did we pursue this?, 💼 For Enterprise

</details>

### fastapi-users-db-sqlalchemy

FastAPI Users database adapter for SQLAlchemy

`pip install fastapi-users-db-sqlalchemy` · installs (wheel) · licence: MIT License · rank 3713 · last release 2025-01-04 · [PyPI](https://pypi.org/project/fastapi-users-db-sqlalchemy/) · [docs](https://fastapi-users.github.io/fastapi-users) · [source](https://github.com/fastapi-users/fastapi-users-db-sqlalchemy)

<details><summary>README extract</summary>

Ready-to-use and customizable users management for FastAPI

Documentation:

Source Code:

Add quickly a registration and authentication system to your FastAPI project. FastAPI Users is designed to be as customizable and adaptable as possible.

Sub-package for SQLAlchemy ORM support in FastAPI Users.

Sections: FastAPI Users - Database adapter for SQLAlchemy ORM, Setup environment, Run unit tests, Format the code

</details>

### uptime-kuma-api

A python wrapper for the Uptime Kuma WebSocket API

`pip install uptime-kuma-api` · installs from source (sdist only) · licence: MIT License · rank 3729 · last release 2023-09-26 · [PyPI](https://pypi.org/project/uptime-kuma-api/)

<details><summary>README extract</summary>

A wrapper for the Uptime Kuma Socket.IO API

uptime-kuma-api is a Python wrapper for the Uptime Kuma Socket.IO API.

This package was developed to configure Uptime Kuma with Ansible. The Ansible collection can be found at

Python version 3.7+ is required.

Supported Uptime Kuma versions:

| Uptime Kuma | uptime-kuma-api | ...

Example:
```python
>>> from uptime_kuma_api import UptimeKumaApi, MonitorType
>>> api = UptimeKumaApi('INSERT_URL')
>>> api.login('INSERT_USERNAME', 'INSERT_PASSWORD')
```

</details>

### flask-marshmallow

Flask + marshmallow for beautiful APIs

`pip install flask-marshmallow` · installs (wheel) · licence: MIT · rank 3755 · last release 2026-04-16 · [PyPI](https://pypi.org/project/flask-marshmallow/)

<details><summary>README extract</summary>

Flask-Marshmallow is a thin integration layer for Flask (a Python web framework) and marshmallow (an object serialization/deserialization library) that adds additional features to marshmallow, including URL and Hyperlinks fields for HATEOAS-ready APIs. It also (optionally) integrates with Flask-SQLAlchemy.

Create your app.

Write your models. ...

Example:
```python
from flask import Flask
from flask_marshmallow import Marshmallow

app = Flask(name)
ma = Marshmallow(app)
```

Sections: Flask-Marshmallow, Flask + marshmallow for beautiful APIs, Get it now, Learn More, Project Links

</details>

### nicegui

Create web-based user interfaces with Python. The nice way.

`pip install nicegui` · installs (wheel) · licence: MIT · rank 3816 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nicegui/) · [docs](https://nicegui.io/documentation) · [source](https://github.com/zauberzeug/nicegui)

<details><summary>README extract</summary>

NiceGUI is an easy-to-use, Python-based UI framework, which shows up in your web browser.
You can create buttons, dialogs, Markdown, 3D scenes, plots and much more.

It is great for micro web apps, dashboards, robotics projects, smart home solutions and similar use cases. ...

Features:
- browser-based graphical user interface
- implicit reload on code change
- acts as webserver (accessed by the browser) or in native mode (eg. desktop window) ...

Example:
```python
from nicegui import ui

ui.label('Hello NiceGUI!')
ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed'))

ui.run()
```

Sections: NiceGUI, Features, Usage, Documentation and Examples, Why?, Included Web Dependencies, Architecture

</details>

### xenon

Monitor code metrics for Python on your CI server

`pip install xenon` · installs (wheel) · licence: MIT License · rank 3823 · last release 2024-10-21 · [PyPI](https://pypi.org/project/xenon/)

<details><summary>README extract</summary>

Xenon is a monitoring tool based on Radon.
It monitors your code's complexity. Ideally, Xenon is run every time you
commit code. Through command line options, you can set various thresholds for
the complexity of your code. It will fail (i.e. it will exit with a
non-zero exit code) when any of these requirements is not met.

Sections: xenon, Usage, The command line, An actual example, Pre-commit hook, Other resources

</details>

### rauth

A Python library for OAuth 1.0/a, 2.0, and Ofly.

`pip install rauth` · installs from source (sdist only) · licence: MIT License · rank 3889 · last release 2017-01-22 · [PyPI](https://pypi.org/project/rauth/)

<details><summary>README extract</summary>

rauth

 A simple Python OAuth 1.0/a, OAuth 2.0, and Ofly consumer library built on
 top of Requests.

 Links

</details>

### yattag

Generate HTML or XML in a pythonic way. Pure python alternative to web template engines.Can fill HTML forms with default values and error messages.

`pip install yattag` · installs from source (sdist only) · licence: GNU Library or Lesser General Public License (LGPL) · rank 3912 · last release 2024-11-02 · [PyPI](https://pypi.org/project/yattag/)

_README extract left out: share-alike licence._

### fredapi

Python API for Federal Reserve Economic Data (FRED) from St. Louis Fed

`pip install fredapi` · installs (wheel) · licence: not stated · rank 3972 · last release 2024-05-05 · [PyPI](https://pypi.org/project/fredapi/)

<details><summary>README extract</summary>

`fredapi` is a Python API for the
FRED data provided by the
Federal Reserve Bank of St. Louis. `fredapi` provides a wrapper in
python to the FRED web
service, and also provides
several conveninent methods for parsing and analyzing point-in-time data
(i.e. historic data revisions) from
ALFRED ...

Example:
```python
from fredapi import Fred
fred = Fred(api_key='insert api key here')
data = fred.get_series('SP500')
```

Sections: Basic Usage, Working with data revisions, Get latest data, Get latest data known on a given date, Get all vintage dates, Search for data series, Dependencies, More Examples

</details>

### requests-oauth

Hook for adding Open Authentication support to Python-requests HTTP library.

`pip install requests-oauth` · installs from source (sdist only) · licence: BSD License · rank 4035 · last release 2012-06-21 · [PyPI](https://pypi.org/project/requests-oauth/)

<details><summary>README extract</summary>

This plugins adds OAuth v1.0 support to @kennethreitz well-known requests library providing both header and url-encoded authentication.

requests-oauth wants to provide the simplest and easiest way to do OAuth in Python. ...

Sections: requests-oauth, Usage, Step 1: Obtaining a request token, Step 3: Authenticate

</details>

### certbot

ACME client

`pip install certbot` · installs (wheel) · licence: Apache-2.0 · rank 4058 · last release 2026-10-29 · [PyPI](https://pypi.org/project/certbot/)

<details><summary>README extract</summary>

Certbot is part of EFF’s effort to encrypt the entire Internet. Secure communication over the Web relies on HTTPS, which requires the use of a digital certificate that lets browsers verify the identity of web servers (e.g., is that really google.com?). ...

Sections: Getting Started, Links, Current Features, Thanks

</details>

### SharePlum

Python SharePoint Library

`pip install SharePlum` · installs (wheel) · licence: MIT License · rank 4075 · last release 2020-04-22 · [PyPI](https://pypi.org/project/SharePlum/)

<details><summary>README extract</summary>

SharePlum is an easier way to work with SharePoint services. It handles all of the messy parts of dealing with SharePoint and allows you to write clean and Pythonic code.

Features:
- Reading and writing data to SharePoint lists using Python Dictionaries.
- Automatic conversion between SharePoint internal names and displayed names.
- Using Queries to filter data when retrieving List Items.
- Automatic conversion of data types. ...

Example:
```python
from shareplum import Site
from requests_ntlm import HttpNtlmAuth

auth = HttpNtlmAuth('DIR\\username', 'password')
site = Site(' auth=auth)
sp_list = site.List('list name')
data = sp_list.GetListItems('All Items', rowlimit=200)
```

...

</details>

### scrapling

Scrapling is an undetectable, powerful, flexible, high-performance Python framework that makes Web Scraping easy and effortless as it should be!

`pip install scrapling` · installs (wheel) · licence: BSD License · rank 4096 · last release 2026-11-04 · [PyPI](https://pypi.org/project/scrapling/) · [docs](https://scrapling.readthedocs.io/en/latest/) · [source](https://github.com/D4Vinci/Scrapling)

<details><summary>README extract</summary>

Effortless Web Scraping for the Modern Web

 Selection methods
 Fetchers
 Spiders
 Proxy Rotation
 CLI
 MCP

Scrapling is a Python Web Scraping framework that brings fast HTTP requests, stealth browsers, powerful parsing, and concurrent crawling into one library. ...

Example:
```python
from scrapling.fetchers import Fetcher, FetcherSession

with FetcherSession(impersonate='chrome') as session:  # Use latest version of Chrome's TLS fingerprint
    page = session.get(' stealthy_headers=True)
    quotes = page.css('.quote .text::text').getall()

# Or use one-off requests
page = Fetcher.get('
...
```

...

</details>

### camoufox

Wrapper around Playwright to help launch Camoufox

`pip install camoufox` · installs (wheel) · licence: MIT License · rank 4098 · last release 2026-11-01 · [PyPI](https://pypi.org/project/camoufox/) · [source](https://github.com/daijro/camoufox)

<details><summary>README extract</summary>

`camoufox` drives the Camoufox browser through Playwright. On every launch it
draws a complete device identity from fpgen,
a model of real-world traffic, checks that the parts agree with each other, and
hands it to the browser, which spoofs it in C++. ...

Example:
```python
from camoufox.sync_api import Camoufox

with Camoufox(headless=True) as browser:
    page = browser.new_page()
    page.goto("
```

Sections: camoufox (Python), The Python launcher for the Camoufox anti-detect browser., Usage, Sync and async, Proxy with a matching location, Persistent profile, One browser, many identities, The canvas on another OS, Headless modes, The GPU display, Remote server, Your own Playwright instance, Launch options, CLI

</details>

### itypes

Simple immutable types for python.

`pip install itypes` · installs (wheel) · licence: BSD License · rank 4156 · last release 2020-04-19 · [PyPI](https://pypi.org/project/itypes/)

<details><summary>README extract</summary>

Basic immutable container types for Python.

A simple implementation that's designed for simplicity over performance.

Use these in circumstances where it may result in more comprehensible code,
or when you want to create custom types with restricted, immutable interfaces. ...

Sections: itypes, Instantiating dictionaries and lists., On instantiation, nested types are coerced to immutables., Assignments and deletions return new copies., Standard assignments and deletions fail., Nested lookups., Nested assignments and deletions., Equality works against standard types., Objects are hashable., Subclassing., Custom immutable objects.

</details>

### token-bucket

Very fast implementation of the token bucket algorithm.

`pip install token-bucket` · installs (wheel) · licence: Apache-2.0 · rank 4163 · last release 2026-06-12 · [PyPI](https://pypi.org/project/token-bucket/)

<details><summary>README extract</summary>

The `token-bucket` package provides an implementation of the
token bucket algorithm
suitable for use in web applications for shaping or policing request
rates. This implementation does not require the use of an independent
timer thread to manage the bucket state. ...

</details>

### Flask-Bcrypt

Brcrypt hashing for Flask.

`pip install Flask-Bcrypt` · installs (wheel) · licence: BSD License · rank 4171 · last release 2022-04-05 · [PyPI](https://pypi.org/project/Flask-Bcrypt/)

<details><summary>README extract</summary>

Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for
your application.

Due to the recent increased prevalence of powerful hardware, such as modern
GPUs, hashes have become increasingly easy to crack. A proactive solution to
this is to use a hash that was designed to be "de-optimized". ...

Sections: Flask-Bcrypt, Usage, Documentation

</details>

### sqladmin

SQLAlchemy admin for FastAPI and Starlette

`pip install sqladmin` · installs (wheel) · licence: BSD-3-Clause · rank 4201 · last release 2026-09-20 · [PyPI](https://pypi.org/project/sqladmin/) · [docs](https://smithyhq.github.io/sqladmin/) · [source](https://github.com/smithyhq/sqladmin)

<details><summary>README extract</summary>

SQLAdmin is a flexible Admin interface for SQLAlchemy models.

Main features include:

* SQLAlchemy sync/async engines
* Starlette integration
* FastAPI integration
* WTForms form building
* SQLModel support
* UI using Tabler

Documentation:

Source Code:

Live Demo: (Username: `superadmin` Password: `superadmin`)

Example:
```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine(
    "sqlite:///example.db",
    connect_args={"check_same_thread": False},
)

class User(Base):
    tablename = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

...
```

...

</details>

### starlette-compress

Compression middleware for Starlette - supporting ZStd, Brotli, and GZip

`pip install starlette-compress` · installs (wheel) · licence: 0BSD · rank 4205 · last release 2026-10-27 · [PyPI](https://pypi.org/project/starlette-compress/) · [source](https://github.com/Zaczero/pkgs/tree/main/starlette-compress)

<details><summary>README extract</summary>

starlette-compress compresses ASGI HTTP responses with Zstandard, Brotli, or
Gzip. Use it with Starlette, FastAPI, or another
ASGI application on Python 3.11+.

Works with asyncio and Trio, including streaming responses and server-sent events.

Example:
```python
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import PlainTextResponse
from starlette.routing import Route
from starlette_compress import CompressMiddleware

async def homepage(request):
    return PlainTextResponse("Hello!" * 200)

app = Starlette(
...
```

...

</details>

### django-tables2

Table/data-grid framework for Django

`pip install django-tables2` · installs (wheel) · licence: BSD License · rank 4210 · last release 2026-08-30 · [PyPI](https://pypi.org/project/django-tables2/) · [docs](https://django-tables2.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

django-tables2 simplifies the task of turning sets of data into HTML tables. It
has native support for pagination and sorting. It does for HTML tables what
`django.forms` does for HTML forms. e.g.

- Available on pypi as django-tables2
- Tested against currently supported versions of Django
 and supported python 3 versions Django supports. ...

Example:
```python
import django_tables2 as tables

class SimpleTable(tables.Table):
    class Meta:
        model = Simple
```

Sections: django-tables2 - An app for creating HTML tables, Example

</details>

### mohawk

Library for Hawk HTTP authorization

`pip install mohawk` · installs (wheel) · licence: MPL 2.0 (Mozilla Public License) · rank 4273 · last release 2019-10-28 · [PyPI](https://pypi.org/project/mohawk/)

<details><summary>README extract</summary>

Hawk lets two parties securely communicate with each other using
messages signed by a shared key.
It is based on HTTP MAC access authentication (which
was based on parts of OAuth 1.0).

The Mohawk API is a little different from that of the Node library
(i.e. ...

</details>

### coreapi

Python client library for Core API.

`pip install coreapi` · installs (wheel) · licence: BSD License · rank 4296 · last release 2017-10-05 · [PyPI](https://pypi.org/project/coreapi/)

### django-localflavor

Country-specific Django helpers

`pip install django-localflavor` · installs (wheel) · licence: BSD-3-Clause · rank 4299 · last release 2026-08-01 · [PyPI](https://pypi.org/project/django-localflavor/) · [source](https://github.com/django/django-localflavor)

<details><summary>README extract</summary>

Django's "localflavor" packages offer additional functionality for particular
countries or cultures. For example, these might include form fields for your
country's postal codes or government ID numbers. ...

</details>

### WebTest

Helper to test WSGI applications

`pip install WebTest` · installs (wheel) · licence: MIT License · rank 4338 · last release 2025-10-06 · [PyPI](https://pypi.org/project/WebTest/)

<details><summary>README extract</summary>

This wraps any WSGI application and makes it easy to send test
requests to that application, without starting up an HTTP server.

This provides convenient full-stack testing of applications written
with any WSGI-compatible framework.

Full docs can be found at

</details>

### coreschema

Core Schema.

`pip install coreschema` · installs from source (sdist only) · licence: BSD License · rank 4362 · last release 2017-02-08 · [PyPI](https://pypi.org/project/coreschema/)

### htmltools

Tools for HTML generation and output.

`pip install htmltools` · installs (wheel) · licence: MIT License · rank 4400 · last release 2026-05-21 · [PyPI](https://pypi.org/project/htmltools/) · [source](https://github.com/rstudio/py-htmltools)

<details><summary>README extract</summary>

Tools for creating, manipulating, and writing HTML from Python.

</details>

### crispy-bootstrap5

Bootstrap5 template pack for django-crispy-forms

`pip install crispy-bootstrap5` · installs (wheel) · licence: MIT · rank 4433 · last release 2026-09-02 · [PyPI](https://pypi.org/project/crispy-bootstrap5/)

<details><summary>README extract</summary>

Bootstrap5 template pack for django-crispy-forms

Example:
```python
from crispy_bootstrap5.bootstrap5 import FloatingField

# then in your Layout
... Layout(
    FloatingField("first_name"),
)
```

Sections: crispy-bootstrap5, Usage, What's new?

</details>

### rollbar

Easy and powerful exception tracking with Rollbar. Send messages and exceptions with arbitrary context, get back aggregates, and debug production issues quickly.

`pip install rollbar` · installs (wheel) · licence: MIT License · rank 4471 · last release 2026-09-18 · [PyPI](https://pypi.org/project/rollbar/) · [docs](https://docs.rollbar.com/docs/python) · [source](https://github.com/rollbar/pyrollbar/)

<details><summary>README extract</summary>

Proactively discover, predict, and resolve errors in real-time with Rollbar’s error monitoring platform. Start tracking errors today!

Python notifier for reporting exceptions, errors, and log messages to Rollbar.

- Frameworks: Pyrollbar supports popular Python frameworks such as Django, Flask, FastAPI, AWS Lambda and more! ...

Sections: Pyrollbar, Key benefits of using Pyrollbar are, Setup Instructions, Usage and Reference

</details>

### bleach-allowlist

Curated lists of tags and attributes for sanitizing html

`pip install bleach-allowlist` · installs (wheel) · licence: BSD License · rank 4474 · last release 2020-08-13 · [PyPI](https://pypi.org/project/bleach-allowlist/)

<details><summary>README extract</summary>

A curated list of tags, attributes, and styles suitable for filtering
user-provided HTML using bleach.

Currently, it consists of basic set of tags suitable for rendering markdown,
and markup intended for printing, as well as a list of all CSS styles. ...

Example:
```python
import bleach
from bleach_allowlist import print_tags, print_attrs, all_styles

bleach.clean(raw_html, print_tags, print_attrs, all_styles)
```

Sections: Bleach allowlist, Use

</details>

### django-rest-knox

Authentication for django rest framework

`pip install django-rest-knox` · installs (wheel) · licence: MIT License · rank 4492 · last release 2026-11-04 · [PyPI](https://pypi.org/project/django-rest-knox/) · [docs](https://django-commons.org/django-rest-knox/)

<details><summary>README extract</summary>

Authentication module for Django rest auth.

Knox provides easy-to-use authentication for Django REST
Framework The aim is to allow
for common patterns in applications that are REST-based, with little
extra effort; and to ensure that connections remain secure. ...

Sections: django-rest-knox, Run the tests locally, Work on the documentation

</details>

### certbot-dns-cloudflare

Cloudflare DNS Authenticator plugin for Certbot

`pip install certbot-dns-cloudflare` · installs (wheel) · licence: Apache-2.0 · rank 4559 · last release 2026-10-29 · [PyPI](https://pypi.org/project/certbot-dns-cloudflare/)

<details><summary>README extract</summary>

Cloudflare DNS Authenticator plugin for Certbot

</details>

### aiohttp-sse

Server-sent events support for aiohttp.

`pip install aiohttp-sse` · installs (wheel) · licence: Apache Software License · rank 4599 · last release 2026-10-11 · [PyPI](https://pypi.org/project/aiohttp-sse/)

<details><summary>README extract</summary>

The EventSource interface is used to receive server-sent events. It connects
to a server over HTTP and receives events in text/event-stream format without
closing the connection. *aiohttp-sse* provides support for server-sent
events for aiohttp.

Example:
```python
import asyncio
import json
from datetime import datetime

from aiohttp import web

from aiohttp_sse import sse_response

async def hello(request: web.Request) -> web.StreamResponse:
    async with sse_response(request) as resp:
        while resp.is_connected():
            time_dict = {"time": f"Server Time : {datetime.now()}"}
...
```

Sections: aiohttp-sse, Example, Requirements

</details>

### Paste

Tools for using a Web Server Gateway Interface stack

`pip install Paste` · installs (wheel) · licence: MIT License · rank 4654 · last release 2026-10-28 · [PyPI](https://pypi.org/project/Paste/) · [docs](https://pythonpaste.readthedocs.io) · [source](https://github.com/pasteorg/paste)

<details><summary>README extract</summary>

*Paste is in maintenance mode and recently moved from bitbucket to github.
Patches are accepted to keep it on life support, but for the most part, please
consider using other options.*

**As of release 3.7.0 Paste no longer supports Python 2. If you are
required to continue using Python 2 please pin an earlier version of Paste.** ...

</details>

### python-logging-loki

Python logging handler for Grafana Loki.

`pip install python-logging-loki` · installs (wheel) · licence: MIT License · rank 4729 · last release 2019-11-28 · [PyPI](https://pypi.org/project/python-logging-loki/)

<details><summary>README extract</summary>

Python logging handler for Loki.

Example:
```python
import logging
import logging_loki

handler = logging_loki.LokiHandler(
    url="
    tags={"application": "my-app"},
    auth=("username", "password"),
    version="1",
)

logger = logging.getLogger("my-logger")
logger.addHandler(handler)
logger.error(
    "Something happened",
    extra={"tags": {"service": "my-service"}},
)
```

Sections: python-logging-loki, Usage

</details>

### draftjs_exporter

Library to convert rich text from Draft.js raw ContentState to HTML

`pip install draftjs_exporter` · installs (wheel) · licence: MIT · rank 4767 · last release 2026-10-20 · [PyPI](https://pypi.org/project/draftjs_exporter/) · [docs](https://wagtail.github.io/draftjs_exporter/) · [source](https://github.com/wagtail/draftjs_exporter)

<details><summary>README extract</summary>

> Library to convert rich text from Draft.js raw ContentState to HTML.

Features:
This project adheres to Semantic Versioning, and measures performance and code coverage. Code is checked with mypy.

- Extensive configuration of the generated HTML.
- Default, extensible block & inline style maps for common HTML elements. ...

Sections: Draft.js exporter, Features, When to use the exporter, Documentation

</details>

### scrapy-stealth

Stealthy Crawling. Maximum Results. A pluggable anti-bot and stealth framework for Scrapy.

`pip install scrapy-stealth` · installs (wheel) · licence: MIT License · rank 4769 · last release 2026-09-25 · [PyPI](https://pypi.org/project/scrapy-stealth/) · [docs](https://scrapy-stealth.readthedocs.io/en/latest/) · [source](https://github.com/fawadss1/scrapy-stealth)

<details><summary>README extract</summary>

Stealthy Crawling. Maximum Results.

Per-request drivers and automatic HTTP → browser fallback.

`scrapy-stealth` adds TLS impersonation, behavioral fingerprinting, adaptive rate limiting, smart proxies, and real Chrome to Scrapy —
with per-request driver selection and automatic HTTP → browser fallback. ...

Example:
```python
yield scrapy.Request("
```

Sections: scrapy-stealth, Quick setup, Documentation

</details>

### ua-generator

A random user-agent generator

`pip install ua-generator` · installs (wheel) · licence: Apache Software License · rank 4838 · last release 2026-11-02 · [PyPI](https://pypi.org/project/ua-generator/)

<details><summary>README extract</summary>

A random user-agent generator for Python >= 3.9

Features:
- No dependency.
- No external user-agent list, no downloads.
- User-agent versions are hardcoded into the code.
- Platform and browser versions are based on real releases.
- Client Hints (Sec-CH-UA fields).
- Easy to integrate into HTTP libraries.

Example:
```python
import ua_generator

ua = ua_generator.generate()
print(ua) # Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/15.2 Safari/604.1.38
```

Sections: ua-generator, Features, Basic usage, Customization, Customized user-agent generation, Headers, Integrating into the requests, Integrating into the httpx, Integrating into the urllib, Integrating into the Selenium, Options, weighted_versions, version_ranges, latest_versions

</details>

### purgatory

A circuit breaker implementation for asyncio

`pip install purgatory` · installs (wheel) · licence: MIT License · rank 4854 · last release 2024-11-02 · [PyPI](https://pypi.org/project/purgatory/) · [docs](https://mardiros.github.io/purgatory) · [source](https://github.com/mardiros/purgatory.git)

<details><summary>README extract</summary>

Purgatory is a Python library for robust failure management, built to prevent
repetitive errors in synchronous and asynchronous systems through an easy-to-use
circuit breaker pattern. ...

Features:
Purgatory supports the creation of many circuit breakers easily, that
can be used as context manager or decorator.

Circuit breaker can be asynchronous or synchronous. ...

Example:
```python
from purgatory import AsyncCircuitBreakerFactory

circuitbreaker = AsyncCircuitBreakerFactory()
async with await circuitbreaker.get_breaker("my_circuit"):
   ...
```

...

</details>

### httpretty

HTTP client mock for Python

`pip install httpretty` · installs from source (sdist only) · licence: MIT License · rank 4917 · last release 2021-08-16 · [PyPI](https://pypi.org/project/httpretty/) · [docs](https://httpretty.readthedocs.io/en/latest/) · [source](https://github.com/gabrielfalcao/httpretty)

<details><summary>README extract</summary>

HTTP Client mocking tool for Python created by Gabriel Falcão . It provides a full fake TCP socket module. Inspired by FakeWeb

- Github Repository
- Documentation
- PyPI Package

Python Support:

- 3.6
- 3.7
- 3.8
- 3.9

Example:
```python
import sure
import httpretty
import requests

@httpretty.activate(verbose=True, allow_net_connect=False)
def test_httpbin():
    httpretty.register_uri(
        httpretty.GET,
        "
        body='{"origin": "127.0.0.1"}'
    )

    response = requests.get('
    response.json().should.equal({'origin': '127.0.0.1'})

...
```

Sections: HTTPretty 1.1.4, Common Use Cases, Simple Example, checking multiple responses

</details>

### SQLAlchemy-Continuum

Versioning and auditing extension for SQLAlchemy.

`pip install SQLAlchemy-Continuum` · installs (wheel) · licence: BSD-3-Clause · rank 4919 · last release 2026-10-14 · [PyPI](https://pypi.org/project/SQLAlchemy-Continuum/) · [docs](https://sqlalchemy-continuum.github.io/)

<details><summary>README extract</summary>

Versioning and auditing extension for SQLAlchemy.

Features:
- Creates versions for inserts, deletes and updates
- Does not store updates which don't change anything
- Supports alembic migrations
- Can revert objects data as well as all object relations at given transaction even if the object was deleted ...

Example:
```python
import sqlalchemy as sa
from sqlalchemy_continuum import make_versioned

make_versioned(user_cls=None)

class Article(Base):
    versioned = {}
    tablename = 'article'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Unicode(255))
    content = sa.Column(sa.UnicodeText)

...
```

Sections: SQLAlchemy-Continuum, Features, QuickStart, Resources, More information

</details>

### django-tasks

A backport of Django's built in Tasks framework

`pip install django-tasks` · installs (wheel) · licence: BSD-3-Clause · rank 4957 · last release 2026-02-06 · [PyPI](https://pypi.org/project/django-tasks/) · [source](https://github.com/RealOrangeOne/django-tasks)

<details><summary>README extract</summary>

An backport of `django.tasks` - Django's built-in Tasks framework.

Example:
```python
from django_tasks import task

@task()
def calculate_meaning_of_life() -> int:
    return 42
```

Sections: Django Tasks, Usage, Defining tasks, Task context, Enqueueing tasks, Queue names, Retrieving task result, Return values, Errors, Attempts, Backend introspecting, Signals

</details>

### django-autocomplete-light

Fresh autocompletes for Django

`pip install django-autocomplete-light` · installs (wheel) · licence: MIT License · rank 4970 · last release 2026-06-18 · [PyPI](https://pypi.org/project/django-autocomplete-light/) · [source](https://github.com/yourlabs/django-autocomplete-light)

<details><summary>README extract</summary>

Features:
- Python 3.11–3.14 and Django 5.2–6.0+ support
- Django (multiple) choice support,
- Django (multiple) model choice support,
- Django generic foreign key support (through django-querysetsequence), ...

Sections: Features, Resources

</details>

### python-logstash

Python logging handler for Logstash.

`pip install python-logstash` · installs from source (sdist only) · licence: MIT License · rank 4972 · last release 2022-03-30 · [PyPI](https://pypi.org/project/python-logstash/)

<details><summary>README extract</summary>

Python logging handler for Logstash.

Example:
```python
import logging
import logstash
import sys

host = 'localhost'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5959, version=1))
# test_logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))

...
```

Sections: python-logstash, Usage, Using with Django, Example Logstash Configuration

</details>

### wagtail

A Django content management system.

`pip install wagtail` · installs (wheel) · licence: BSD-3-Clause · rank 4986 · last release 2026-11-02 · [PyPI](https://pypi.org/project/wagtail/) · [docs](https://docs.wagtail.org) · [source](https://github.com/wagtail/wagtail)

<details><summary>README extract</summary>

Wagtail is an open source content management system built on Django, with a strong community and commercial support. It's focused on user experience, and offers precise control for designers and developers.

- A fast, attractive interface for authors
- Complete control over front-end design and structure ...

Sections: 🔥 Features, 👉 Getting started, 👨‍👩‍👧‍👦 Who’s using it?, 📖 Documentation, 📌 Compatibility, 👏 Thanks

</details>

### Flask-Testing

Unit testing for Flask

`pip install Flask-Testing` · installs from source (sdist only) · licence: BSD License · rank 5022 · last release 2020-12-24 · [PyPI](https://pypi.org/project/Flask-Testing/)

<details><summary>README extract</summary>

Flask-Testing

Flask unittest integration.

Links

</details>

### demjson3

encoder, decoder, and lint/validator for JSON (JavaScript Object Notation) compliant with RFC 7159

`pip install demjson3` · installs from source (sdist only) · licence: GNU Library or Lesser General Public License (LGPL) · rank 5025 · last release 2022-10-22 · [PyPI](https://pypi.org/project/demjson3/)

_README extract left out: share-alike licence._

### Flask-OpenID

OpenID support for Flask

`pip install Flask-OpenID` · installs (wheel) · licence: BSD License · rank 5064 · last release 2024-05-26 · [PyPI](https://pypi.org/project/Flask-OpenID/)

<details><summary>README extract</summary>

Adds support for OpenID to flask applications. Check out the
example for more information.

Documentation:

Note that this library is for a very old and outdated version of OpenID.
Almost no-one uses this Open ID protocol, the OpenID Connect protocol is
the current standard.

</details>

### django-ckeditor

Django admin CKEditor integration.

`pip install django-ckeditor` · installs (wheel) · licence: BSD License · rank 5067 · last release 2026-10-20 · [PyPI](https://pypi.org/project/django-ckeditor/) · [docs](https://django-ckeditor.readthedocs.io/en/latest/) · [source](https://github.com/django-ckeditor/django-ckeditor)

<details><summary>README extract</summary>

I do not recommend using this package anymore since the open source version of CKEditor 4 has unfixed security issues. More on this in my blog post. Alternatives are listed here on Django Packages. I personally am using django-prose-editor. Thanks!

Django admin CKEditor integration. ...

Example:
```python
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
...
```

...

</details>

### runpod

🐍 | Python library for Runpod API and serverless worker SDK.

`pip install runpod` · installs (wheel) · licence: MIT License · rank 5070 · last release 2026-11-03 · [PyPI](https://pypi.org/project/runpod/) · [docs](https://docs.runpod.io) · [source](https://github.com/runpod/runpod-python)

<details><summary>README extract</summary>

Define GPU functions in Python. Run them in the cloud with one decorator.

Documentation • Examples • Discord

Using an AI agent? Point it to to install the Runpod skills and MCP server.

Example:
```python
import runpod
from runpod import App, Model, NetworkVolume, Secret

app = App("inference")

models = NetworkVolume("models", size=100)
llama = Model("meta-llama/Llama-3.1-8B-Instruct")

# an autoscaling job queue on cloud H100s: weights pre-cached,
# dependencies vendored at deploy time, scale-to-zero when idle
@app.queue(
    gpu="H100",
...
```

Sections: Runpod Python, Example, ⚡ | Serverless Worker (SDK), Quick Start, Local Test Worker, 📁 | Directory

</details>

### tls-client

Advanced Python HTTP Client.

`pip install tls-client` · installs (wheel) · licence: MIT · rank 5143 · last release 2026-10-10 · [PyPI](https://pypi.org/project/tls-client/) · [source](https://github.com/FlorianREGAZ/Python-Tls-Client)

<details><summary>README extract</summary>

Python-TLS-Client is an advanced HTTP library based on requests and tls-client.

Example:
```python
import tls_client

# `client_identifier` picks the browser profile to impersonate, e.g. chrome_120, firefox_120, safari_ios_17_0 or
# okhttp4_android_13. Every supported name is listed in tls_client/settings.py; unknown names raise a ValueError.

session = tls_client.Session(
    client_identifier="chrome_112",
    random_tls_extension_order=True
...
```

Sections: Python-TLS-Client, Examples

</details>

### databases

Async database support for Python.

`pip install databases` · installs (wheel) · licence: BSD License · rank 5154 · last release 2024-03-01 · [PyPI](https://pypi.org/project/databases/)

<details><summary>README extract</summary>

Databases gives you simple asyncio support for a range of databases.

It allows you to make queries using the powerful SQLAlchemy Core
expression language, and provides support for PostgreSQL, MySQL, and SQLite. ...

Example:
```python
# Create a database instance, and connect to it.
from databases import Database
database = Database('sqlite+aiosqlite:///example.db')
await database.connect()

# Create a table.
query = """CREATE TABLE HighScores (id INTEGER PRIMARY KEY, name VARCHAR(100), score INTEGER)"""
await database.execute(query=query)

# Insert some data.
...
```

Sections: Databases, Quickstart

</details>

### httpie

HTTPie: modern, user-friendly command-line HTTP client for the API era.

`pip install httpie` · installs (wheel) · licence: BSD License · rank 5165 · last release 2024-11-01 · [PyPI](https://pypi.org/project/httpie/) · [docs](https://httpie.io/docs) · [source](https://github.com/httpie/cli)

<details><summary>README extract</summary>

HTTPie CLI: human-friendly HTTP client for the API era

HTTPie (pronounced _aitch-tee-tee-pie) is a command-line HTTP client.
Its goal is to make CLI interaction with web services as human-friendly as possible.
HTTPie is designed for testing, debugging, and generally interacting with APIs & HTTP servers. ...

Features:
- Expressive and intuitive syntax
- Formatted and colorized terminal output
- Built-in JSON support
- Forms and file uploads
- HTTPS, proxies, and authentication
- Arbitrary request data
- Custom headers
- Persistent sessions ...

Sections: We lost 54k GitHub stars, Getting started, Features, Examples

</details>

### great-tables

Easily generate information-rich, publication-quality tables from Python.

`pip install great-tables` · installs (wheel) · licence: MIT License · rank 5212 · last release 2026-10-15 · [PyPI](https://pypi.org/project/great-tables/) · [docs](https://posit-dev.github.io/great-tables/)

<details><summary>README extract</summary>

_Absolutely Delightful Table-making in Python

With Great Tables anyone can make wonderful-looking tables in Python. The philosophy here is that we can construct a wide variety of useful tables by working with a cohesive set of table components. ...

Example:
```python
from great_tables import GT
from great_tables.data import sp500

# Define the start and end dates for the data range
start_date = "2010-06-07"
end_date = "2010-06-14"

# Filter sp500 using Pandas to dates between `start_date` and `end_date`
sp500_mini = sp500[(sp500["date"] >= start_date) & (sp500["date"] <= end_date)]

...
```

</details>

### Flask-Bootstrap

An extension that includes Bootstrap in your project, without any boilerplate code.

`pip install Flask-Bootstrap` · installs from source (sdist only) · licence: BSD License · rank 5214 · last release 2017-01-11 · [PyPI](https://pypi.org/project/Flask-Bootstrap/)

<details><summary>README extract</summary>

Flask-Bootstrap packages Bootstrap into an extension that mostly consists
of a blueprint named 'bootstrap'. It can also create links to serve Bootstrap
from a CDN and works with no boilerplate code in your application.

Example:
```python
from flask_bootstrap import Bootstrap

[...]

Bootstrap(app)
```

Sections: Flask-Bootstrap, Usage

</details>

### django-q2

A multiprocessing distributed task queue for Django

`pip install django-q2` · installs (wheel) · licence: MIT · rank 5227 · last release 2026-08-26 · [PyPI](https://pypi.org/project/django-q2/) · [docs](https://django-q2.readthedocs.org) · [source](https://github.com/GDay/django-q2)

<details><summary>README extract</summary>

Django Q2 is a fork of Django Q. Big thanks to Ilan Steemers for starting this project. Unfortunately, development has stalled since June 2021. Django Q2 is the new updated version of Django Q, with dependencies updates, docs updates and several bug fixes. Original repository:

Features:
- Multiprocessing worker pool
- Asynchronous tasks
- Scheduled, cron and repeated tasks
- Signed and compressed packages
- Failure and success database or cache
- Result hooks, groups and chains
- Django Admin integration ...

Example:
```python
from django_q.tasks import async_task, result

# create the task
async_task('math.copysign', 2, -2)

# or with a reference
import math.copysign

task_id = async_task(copysign, 2, -2)

# get the result
task_result = result(task_id)

...

</details>

### peppercorn

A library for converting a token stream into a data structure for use in web form posts

`pip install peppercorn` · installs (wheel) · licence: BSD-derived (http://www.repoze.org/LICENSE.txt) · rank 5233 · last release 2018-08-24 · [PyPI](https://pypi.org/project/peppercorn/)

<details><summary>README extract</summary>

A library for converting a token stream into a data structure comprised of
sequences, mappings, and scalars, developed primarily for converting HTTP form
post data into a richer data structure. It runs on Python 2.7, 3.4, 3.5, 3.6
and 3.7.

Please see
for the documentation.

See for in-development version. ...

Sections: Peppercorn, Changes, 0.6 (2018-08-24), 0.5 (2014-09-29), 0.4 (2012-02-14), 0.3 (2010-09-02), 0.2 (2010-09-02), 0.1 (2010-03-23)

</details>

### django-encrypted-model-fields

A set of fields that wrap standard Django fields with encryption provided by the python cryptography library.

`pip install django-encrypted-model-fields` · installs (wheel) · licence: MIT License · rank 5244 · last release 2022-02-24 · [PyPI](https://pypi.org/project/django-encrypted-model-fields/) · [source](https://gitlab.com/lansharkconsulting/django/django-encrypted-model-fields)

<details><summary>README extract</summary>

This is a fork of
< It has
been renamed, and updated to properly support Python3 and latest
versions of Django.

`django-encrypted-model-fields` is set of fields that wrap standard
Django fields with encryption provided by the python cryptography
library. ...

Sections: Django Encrypted Model Fields, About, Generating an Encryption Key, Getting Started

</details>

### streaming-form-data

Streaming parser for multipart/form-data

`pip install streaming-form-data` · installs from source (sdist only) · licence: MIT License · rank 5256 · last release 2026-06-10 · [PyPI](https://pypi.org/project/streaming-form-data/) · [docs](https://streaming-form-data.readthedocs.io) · [source](https://github.com/siddhantgoel/streaming-form-data)

<details><summary>README extract</summary>

`streaming_form_data` provides a Python parser for parsing `multipart/form-data`
input chunks (the encoding used when submitting data over HTTP through HTML
forms).

> _this speeds up file uploads to my Flask app by more than factor 10_

> _Thanks a lot for your fix with streaming-form-data. ...

Example:
```python
>>> from streaming_form_data import StreamingFormDataParser
>>> from streaming_form_data.targets import FileTarget, NullTarget, GCSTarget, S3Target, ValueTarget
>>>
>>> headers = {"Content-Type": "multipart/form-data; boundary=boundary"}
>>>
>>> parser = StreamingFormDataParser(headers=headers)
>>>
>>> parser.register("name", ValueTarget())
...
```

Sections: Streaming multipart/form-data parser, Testimonials, Usage, Documentation

</details>

### pymacaroons

Macaroon library for Python

`pip install pymacaroons` · installs (wheel) · licence: MIT License · rank 5325 · last release 2018-02-21 · [PyPI](https://pypi.org/project/pymacaroons/)

<details><summary>README extract</summary>

PyMacaroons is a Python implementation of Macaroons. *They're better than cookies!*

</details>

### django-jsonform

A user-friendly JSON editing form for Django admin.

`pip install django-jsonform` · installs (wheel) · licence: BSD License · rank 5365 · last release 2025-01-29 · [PyPI](https://pypi.org/project/django-jsonform/)

<details><summary>README extract</summary>

A user-friendly JSON editing form for django admin.

 Documentation •
 Playground •
 PyPI

Features:
- [x] File uploads
 - [x] Postgres `ArrayField`
 - [x] Many inputs and field types
 - [x] UI matches with Django admin's
 - [x] Recursion (nesting with self references)
 - [x] Validation

Sections: Features, Screenshots, Upgrading notes, Documentation

</details>

### CherryPy

Object-Oriented HTTP framework

`pip install CherryPy` · installs (wheel) · licence: Freely Distributable; BSD License · rank 5369 · last release 2024-06-14 · [PyPI](https://pypi.org/project/CherryPy/)

<details><summary>README extract</summary>

Welcome to the GitHub repository of CherryPy!

CherryPy is a pythonic, object-oriented HTTP framework.

1. It allows building web applications in much the same way one would
 build any other object-oriented program.
2. This design results in more concise and readable code developed faster.
 It's all just properties and methods.
3. ...

Example:
```python
import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

cherrypy.quickstart(HelloWorld())
```

</details>

### django-mathfilters

A set of simple math filters for Django

`pip install django-mathfilters` · installs (wheel) · licence: MIT License · rank 5378 · last release 2020-02-10 · [PyPI](https://pypi.org/project/django-mathfilters/)

<details><summary>README extract</summary>

django-mathfilters is a Python 3 module that provides different simple math
filters for Django.

Django provides an `add` template filter, but no corresponding subtracting,
multiplying or dividing filters.

Django ticket #361 has been
closed as *wontfix*, so I had to create an alternative that is easy to install
in a new Django project. ...

Sections: django-mathfilters, Usage

</details>

### tool

A compact modular conf/web/console framework.

`pip install tool` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 5380 · last release 2011-11-25 · [PyPI](https://pypi.org/project/tool/)

_README extract left out: share-alike licence._

### django-admin-autocomplete-filter

A simple Django app to render list filters in django admin using autocomplete widget

`pip install django-admin-autocomplete-filter` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 5393 · last release 2021-09-11 · [PyPI](https://pypi.org/project/django-admin-autocomplete-filter/)

_README extract left out: share-alike licence._

### django-test-migrations

Test django schema and data migrations, including ordering

`pip install django-test-migrations` · installs (wheel) · licence: MIT · rank 5398 · last release 2026-09-23 · [PyPI](https://pypi.org/project/django-test-migrations/) · [source](https://github.com/wemake-services/django-test-migrations)

<details><summary>README extract</summary>

Features:
- Allows to test `django` schema and data migrations
- Allows to test both forward and rollback migrations
- Allows to test the migrations order
- Allows to test migration names
- Allows to test database configuration ...

Example:
```python
migrator = Migrator()

# Currently our model has two field, but we need a rollback:
old_state = migrator.apply_initial_migration(
    ('main_app', '0002_someitem_is_clean'),
)
SomeItem = old_state.apps.get_model('main_app', 'SomeItem')

# Create some data to illustrate your cases:
# ...

# Now this migration will drop `is_clean` field:
...
```

...

</details>

### djangosaml2

pysaml2 integration for Django

`pip install djangosaml2` · installs (wheel) · licence: Apache Software License · rank 5430 · last release 2026-02-17 · [PyPI](https://pypi.org/project/djangosaml2/)

<details><summary>README extract</summary>

A Django application that builds a Fully Compliant SAML2 Service Provider on top of PySAML2 library.
 Djangosaml2 protects your project with a SAML2 SSO Authentication.

Features:

- HTTP-REDIRECT SSO Binding
- HTTP-POST SSO Binding
- SLO POST and HTTP-REDIRECT Binding
- Discovery Service
- embedded Wayf page with customizable html template ...

Sections: djangosaml2, Special thanks

</details>

### aiohttp-asyncmdnsresolver

An async resolver for aiohttp that supports MDNS

`pip install aiohttp-asyncmdnsresolver` · installs (wheel) · licence: Apache-2.0 · rank 5449 · last release 2026-05-20 · [PyPI](https://pypi.org/project/aiohttp-asyncmdnsresolver/)

<details><summary>README extract</summary>

This module provides an `aiohttp` resolver that supports mDNS, which uses the `zeroconf` library
to resolve mDNS queries.

For full documentation please read

Example:
```python
import asyncio
import aiohttp
from aiohttp_asyncmdnsresolver.api import AsyncMDNSResolver

async def main():
    resolver = AsyncMDNSResolver()
    # aiohttp does not own a resolver passed to TCPConnector, so close it here.
    try:
        connector = aiohttp.TCPConnector(resolver=resolver)
...
```

Sections: aiohttp-asyncmdnsresolver, Introduction, Quick start, Resolving with both mDNS and DNS, API documentation, Source code

</details>

### django-rest-passwordreset

An extension of django rest framework, providing a configurable password reset strategy

`pip install django-rest-passwordreset` · installs (wheel) · licence: BSD License · rank 5496 · last release 2026-06-29 · [PyPI](https://pypi.org/project/django-rest-passwordreset/)

<details><summary>README extract</summary>

This python package provides a simple password reset strategy for django rest framework, where users can request password
reset tokens via their registered e-mail address.

The main idea behind this package is to not make any assumptions about how the token is delivered to the end-user (e-mail, text-message, etc...). ...

Example:
```python
from django.urls import path, include

urlpatterns = [
    ...
    path(r'^api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    ...
]
```

...

</details>

### drf-writable-nested

Writable nested helpers for django-rest-framework's serializers

`pip install drf-writable-nested` · installs (wheel) · licence: BSD License · rank 5499 · last release 2025-03-10 · [PyPI](https://pypi.org/project/drf-writable-nested/)

<details><summary>README extract</summary>

This is a writable nested model serializer for Django REST Framework which
allows you to create/update your models with related nested data.

The following relations are supported:
- OneToOne (direct/reverse)
- ForeignKey (direct/reverse)
- ManyToMany (direct/reverse excluding m2m relations with through model) ...

Example:
```python
from django.db import models

class Site(models.Model):
    url = models.CharField(max_length=100)

class User(models.Model):
    username = models.CharField(max_length=100)

class AccessKey(models.Model):
    key = models.CharField(max_length=100)

class Profile(models.Model):
    sites = models.ManyToManyField(Site)
...
```

Sections: DRF Writable Nested, Requirements, Usage, Known problems with solutions, Example of usage, Mixin ordering, Example

</details>

### python-mimeparse

A module provides basic functions for parsing mime-type names and matching them against a list of media-ranges.

`pip install python-mimeparse` · installs (wheel) · licence: MIT License · rank 5500 · last release 2024-08-25 · [PyPI](https://pypi.org/project/python-mimeparse/)

<details><summary>README extract</summary>

This module provides basic functions for handling mime-types. It can
handle matching mime-types against a list of media-ranges. See section
5.3.2 of the HTTP 1.1 Semantics and Content specification [RFC 7231] for
a complete explanation:

Sections: Python-MimeParse, Functions

</details>

### apeye

Handy tools for working with URLs and APIs.

`pip install apeye` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 5506 · last release 2023-08-14 · [PyPI](https://pypi.org/project/apeye/) · [docs](https://apeye.readthedocs.io/en/latest) · [source](https://github.com/domdfcoding/apeye)

_README extract left out: share-alike licence._

### retryhttp

Retry potentially transient HTTP errors in Python.

`pip install retryhttp` · installs (wheel) · licence: Apache Software License · rank 5574 · last release 2026-06-22 · [PyPI](https://pypi.org/project/retryhttp/) · [docs](https://retryhttp.readthedocs.io) · [source](https://github.com/austind/retryhttp.git)

<details><summary>README extract</summary>

Retry potentially transient HTTP errors in Python.

See documentation.

Features:
Several HTTP errors are often transient, and might succeed if retried:

* HTTP status codes
 * `429 Too Many Requests` (rate limited)
 * `500 Internal Server Error`
 * `502 Bad Gateway`
 * `503 Service Unavailable`
 * `504 Gateway Timeout`
* Network ...

Example:
```python
import httpx
from retryhttp import retry

# Retries safely retryable status codes (429, 500, 502, 503, 504), network errors,
# and timeouts, up to a total of 3 times, with appropriate wait strategies for each
# type of error. All of these behaviors are customizable.
@retry
def example():
    response = httpx.get("
    response.raise_for_status()
...
```

Sections: RetryHTTP, Overview, Quickstart

</details>

### minijinja

An experimental Python binding of the Rust MiniJinja template engine.

`pip install minijinja` · installs (wheel) · licence: Apache Software License · rank 5591 · last release 2026-11-07 · [PyPI](https://pypi.org/project/minijinja/) · [source](https://github.com/mitsuhiko/minijinja)

<details><summary>README extract</summary>

MiniJinja for Python: a powerful template engine for Rust and Python

`minijinja-py` is an experimental binding of
MiniJinja to Python. It has somewhat
limited functionality compared to the Rust version. These bindings use
maturin and pyo3. ...

Example:
```python
from minijinja import Environment

env = Environment(templates={
    "template_name": "Template source"
})
```

Sections: Basic API, Purpose, Dynamic Template Loading, Auto Escaping, Finalizers, State Access, Runtime Behavior, Threading

</details>

### zope.i18nmessageid

Message Identifiers for internationalization

`pip install zope.i18nmessageid` · installs (wheel) · licence: ZPL-2.1 · rank 5603 · last release 2026-10-16 · [PyPI](https://pypi.org/project/zope.i18nmessageid/) · [docs](https://zopei18nmessageid.readthedocs.io) · [source](https://github.com/zopefoundation/zope.i18nmessageid)

<details><summary>README extract</summary>

To translate any text, we must be able to discover the source domain
of the text. A source domain is an identifier that identifies a
project that produces program source strings. Source strings occur as
literals in python programs, text in templates, and some text in XML
data. The project implies a source language and an application
context. ...

Sections: `zope.i18nmessageid`, 8.4 (2026-10-16), 8.3 (2026-08-20), 8.2 (2025-11-18), 8.1 (2025-10-29), 8.0 (2025-09-12), 7.0 (2024-09-17), 5.0.0 (2019-11-12), 4.3.1 (2018-10-19), 4.3.0 (2018-10-18), 4.2.0 (2018-10-05), 4.1.0 (2017-05-02), 4.0.3 (2014-03-19), 4.0.2 (2012-12-31)

</details>

### django-recaptcha

Django recaptcha form field/widget app.

`pip install django-recaptcha` · installs (wheel) · licence: BSD License · rank 5642 · last release 2025-03-28 · [PyPI](https://pypi.org/project/django-recaptcha/) · [source](https://github.com/django-recaptcha/django-recaptcha)

<details><summary>README extract</summary>

Example:
```python
from django import forms
from django_recaptcha.fields import ReCaptchaField

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()
```

Sections: Requirements, Usage, Fields, Widgets, reCAPTCHA V3 Score, reCAPTCHA V3 Action

</details>

### html-sanitizer

HTML sanitizer

`pip install html-sanitizer` · installs (wheel) · licence: BSD License · rank 5657 · last release 2026-10-25 · [PyPI](https://pypi.org/project/html-sanitizer/)

<details><summary>README extract</summary>

This is a allowlist-based and very opinionated HTML sanitizer that
can be used both for untrusted and trusted sources. It attempts to clean
up the mess made by various rich text editors and or copy-pasting to
make styling of webpages simpler and more consistent. ...

Example:
```python
DEFAULT_SETTINGS = {
    "tags": {
        "a", "h1", "h2", "h3", "strong", "em", "p", "ul", "ol",
        "li", "br", "sub", "sup", "hr",
    },
    "attributes": {"a": ("href", "name", "target", "title", "id", "rel")},
    "empty": {"hr", "a", "br"},
    "separate": {"a", "p", "li"},
    "whitespace": {"br"},
    "preserve_whitespace": {"pre"},
...
```

Sections: HTML sanitizer, Goals, Usage, Settings, Django

</details>

### zope.configuration

Zope Configuration Markup Language (ZCML)

`pip install zope.configuration` · installs (wheel) · licence: ZPL-2.1 · rank 5658 · last release 2026-04-10 · [PyPI](https://pypi.org/project/zope.configuration/) · [docs](https://zopeconfiguration.readthedocs.io/) · [source](https://github.com/zopefoundation/zope.configuration)

<details><summary>README extract</summary>

The Zope configuration system provides an extensible system for
supporting various kinds of configurations.

It is based on the idea of configuration directives. Users of the
configuration system provide configuration directives in some
language that express configuration choices. The intent is that the
language be pluggable. ...

Sections: `zope.configuration`, Changes, 7.1 (2026-04-10), 7.0 (2025-09-12), 6.0 (2024-12-06), 5.0.1 (2024-02-12), 5.0 (2023-05-04), 4.4.1 (2022-04-07), 4.4.0 (2020-03-22), 4.3.1 (2019-02-12), 4.3.0 (2018-10-01), 4.2.2 (2018-09-27), 4.2.1 (2018-09-26), 4.2.0 (2018-09-26)

</details>

### gcs-oauth2-boto-plugin

Auth plugin allowing use the use of OAuth 2.0 credentials for Google Cloud Storage in the Boto library.

`pip install gcs-oauth2-boto-plugin` · installs from source (sdist only) · licence: Apache Software License · rank 5678 · last release 2025-06-24 · [PyPI](https://pypi.org/project/gcs-oauth2-boto-plugin/)

<details><summary>README extract</summary>

gcs-oauth2-boto-plugin is a Python application whose purpose is to behave as an
auth plugin for the boto auth plugin framework for use with OAuth 2.0
credentials for the Google Cloud Platform. ...

</details>

### sorl-thumbnail

Thumbnails for Django, made in the template on first use with Pillow, libvips or ImageMagick, stored on any Django storage

`pip install sorl-thumbnail` · installs (wheel) · licence: BSD-3-Clause · rank 5679 · last release 2026-10-25 · [PyPI](https://pypi.org/project/sorl-thumbnail/) · [docs](https://sorl-thumbnail.readthedocs.io/en/latest/) · [source](https://github.com/mariocesar/sorl-thumbnail)

<details><summary>README extract</summary>

Thumbnails for Django. You write the size in the template, or ask for it in
Python, and sorl-thumbnail makes the thumbnail on first use with Pillow,
libvips or ImageMagick, saves it on your media storage and remembers it in a
key-value store, so later renders cost no image work and no storage request.

Features:
- Resize to a box, a width or a height. Crop by position, percentage, pixels
 or a crop box, crop to the busiest part of the image, or cut plain borders
 first. ...

Example:
```python
from sorl.thumbnail import get_thumbnail

im = get_thumbnail(item.image, '100x100', crop='center', quality=99)
```

Sections: sorl-thumbnail, Quick start, Features, Engines, Using it next to another thumbnail library, Help

</details>

### cloakbrowser

Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches.

`pip install cloakbrowser` · installs (wheel) · licence: MIT · rank 5701 · last release 2026-11-07 · [PyPI](https://pypi.org/project/cloakbrowser/) · [docs](https://github.com/CloakHQ/CloakBrowser#readme) · [source](https://github.com/CloakHQ/CloakBrowser)

<details><summary>README extract</summary>

Not a patched config. Not a JS injection. A real Chromium binary with fingerprints modified at the C++ source level. Antibot systems score it as a normal browser — because it is a normal browser.

Cloudflare Turnstile — 3 live tests passing (headed mode, macOS)

Drop-in Playwright/Puppeteer replacement for Python and JavaScript. ...

Features:
- Config-level patches break — `playwright-stealth`, `undetected-chromedriver`, and `puppeteer-extra` inject JavaScript or tweak flags. Every Chrome update breaks them. Antibot systems detect the patches themselves. ...

Example:
```python
# Pin a specific seed
browser = launch(args=["--fingerprint=42069"])

# Full control — disable defaults, set everything yourself
browser = launch(stealth_args=False, args=[
    "--fingerprint=42069",
...

</details>

### aiosonic

Async HTTP/WebSocket client

`pip install aiosonic` · installs (wheel) · licence: MIT License · rank 5720 · last release 2026-11-04 · [PyPI](https://pypi.org/project/aiosonic/) · [source](https://github.com/sonic182/aiosonic)

<details><summary>README extract</summary>

A very fast, lightweight Python asyncio HTTP/1.1, HTTP/2, and WebSocket client.

The repository is hosted on GitHub.

For full documentation, please see aiosonic docs.

Features:
- Keepalive support and smart pool of connections
- Multipart file uploads
- Handling of chunked responses and requests
- Connection timeouts and automatic decompression
- Automatic redirect following
- Fully type-annotated
- WebSocket support ...

Example:
```python
import asyncio
import aiosonic
import json

async def run():
    client = aiosonic.HTTPClient()

    # Sample GET request
    response = await client.get('
    assert response.status_code == 200
    assert 'Google' in (await response.text())

    # POST data as URL-encoded form
    url = "
    posted_data = {'foo': 'bar'}
...
```

...

</details>

### flask-oidc

OpenID Connect extension for Flask

`pip install flask-oidc` · installs (wheel) · licence: BSD License · rank 5730 · last release 2025-06-16 · [PyPI](https://pypi.org/project/flask-oidc/) · [source](https://github.com/fedora-infra/flask-oidc)

<details><summary>README extract</summary>

OpenID Connect support for Flask.

This library should work with any standards compliant OpenID Connect provider.

The full documentation is at

It has been tested with:

* Ipsilon

</details>

### serpapi

The official Python client for SerpApi.com.

`pip install serpapi` · installs (wheel) · licence: MIT · rank 5738 · last release 2026-10-30 · [PyPI](https://pypi.org/project/serpapi/) · [docs](https://serpapi-python.readthedocs.io/en/latest/) · [source](https://github.com/serpapi/serpapi-python)

<details><summary>README extract</summary>

Integrate search data into your AI workflow, RAG / fine-tuning, or Python application using this official wrapper for SerpApi.

SerpApi supports Google, Google Maps, Google Shopping, Baidu, Yandex, Yahoo, eBay, App Stores, and more. ...

Example:
```python
import os
import serpapi

client = serpapi.Client(api_key=os.getenv("SERPAPI_KEY"))
results = client.search({
  "engine": "google",
  "q": "coffee"
})

print(results)
```

Sections: SerpApi Python Library & Package, Quick start, Extract content from a URL, Error handling, Documentation, Markdown output for AI agents, Basic examples, Search Bing, Search Baidu, Search Yahoo, Search YouTube, Search Walmart, Search eBay, Search Naver

</details>

### django-split-settings

Organize Django settings into multiple files and directories. Easily override and modify settings. Use wildcards and optional settings files.

`pip install django-split-settings` · installs (wheel) · licence: BSD License · rank 5756 · last release 2024-07-05 · [PyPI](https://pypi.org/project/django-split-settings/) · [source](https://github.com/sobolevn/django-split-settings)

<details><summary>README extract</summary>

Organize Django settings into multiple files and directories. Easily
override and modify settings. Use wildcards in settings file paths
and mark settings files as optional.

Read this blog post
for more information.
Also, check this example project. ...

Example:
```python
from split_settings.tools import optional, include

include(
    'components/base.py',
    'components/database.py',
    optional('local_settings.py')
)
```

Sections: Requirements, Usage, Tips and tricks, Updating `BASE_DIR`

</details>

### django-user-agents

A django package that allows easy identification of visitors' browser, operating system and device information (mobile phone, tablet or has touch capabilities).

`pip install django-user-agents` · installs (wheel) · licence: MIT License · rank 5757 · last release 2019-06-22 · [PyPI](https://pypi.org/project/django-user-agents/)

<details><summary>README extract</summary>

A django package that allows easy identification of visitor's browser, OS and device information,
including whether the visitor uses a mobile phone, tablet or a touch capable device. Under the hood,
it uses user-agents.

Example:
```python
from django_user_agents.utils import get_user_agent

def my_view(request):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        # Do stuff here...
    elif user_agent.is_tablet:
        # Do other stuff...
```

Sections: Django User Agents, Usage, Middleware, View Usage, Template Usage, Running Tests, 0.4.0, 0.3.1, 0.3.0, 0.2.2, 0.2.1, 0.2.0, 0.1.1, 0.1

</details>

### python-backoff

Function decoration for backoff and retry

`pip install python-backoff` · installs (wheel) · licence: MIT · rank 5810 · last release 2026-08-31 · [PyPI](https://pypi.org/project/python-backoff/) · [docs](https://python-backoff.github.io/backoff) · [source](https://github.com/python-backoff/backoff)

<details><summary>README extract</summary>

Function decoration for backoff and retry

This module provides function decorators which can be used to wrap a
function such that it will be retried until some condition is met. It
is meant to be of use when accessing unreliable resources with the
potential for intermittent failures i.e. network resources and external
APIs. ...

Example:
```python
@backoff.on_exception(
    backoff.expo,
    requests.exceptions.RequestException,
)
def get_url(url):
    return requests.get(url)
```

Sections: backoff, Examples, @backoff.on_exception

</details>

### Routes

Routing Recognition and Generation Tools

`pip install Routes` · installs (wheel) · licence: MIT License · rank 5874 · last release 2020-10-14 · [PyPI](https://pypi.org/project/Routes/)

<details><summary>README extract</summary>

Routes is a Python re-implementation of the Rails routes system for mapping
URL's to Controllers/Actions and generating URL's. Routes makes it easy to
create pretty and concise URL's that are RESTful with little effort.

Speedy and dynamic URL generation means you get a URL with minimal cruft
(no big dangling query args). ...

</details>

### httpr

Fast HTTP client for Python

`pip install httpr` · installs (wheel) · licence: MIT License · rank 5910 · last release 2026-10-21 · [PyPI](https://pypi.org/project/httpr/)

<details><summary>README extract</summary>

Blazing fast http-client for Python in Rust 🦀 that can be used as drop-in replacement for `httpx` and `requests` in most cases.

- Fast: `httpr` is built on top of `reqwests`, which is a blazing fast http client in Rust. Check out the benchmark.
- Both async and sync: `httpr` provides both a sync and async client. ...

Example:
```python
import httpr

# Initialize the client
client = httpr.Client()

# GET request
resp = client.get("
print(resp.json())

# GET request with passing params and setting timeout
params = {"param1": "value1", "param2": "value2"}
resp = client.post(url=" params=params, timeout=10)
print(r.text)

# POST Binary Request Data
content = b"some_data"
...
```

...

</details>

### Flask-BasicAuth

HTTP basic access authentication for Flask.

`pip install Flask-BasicAuth` · installs from source (sdist only) · licence: BSD License · rank 5955 · last release 2013-06-15 · [PyPI](https://pypi.org/project/Flask-BasicAuth/)

<details><summary>README extract</summary>

Flask-BasicAuth is a Flask extension that provides an easy way to protect
certain views or your whole application with HTTP basic access
authentication.

- Documentation
- Issue Tracker
- Code
- Development Version

Sections: Flask-BasicAuth, Links, 0.2.0 (June 15, 2013), 0.1.1 (May 20, 2013), 0.1.0 (April 30, 2012)

</details>

### Flask-Pydantic

Flask extension for integration with Pydantic library.

`pip install Flask-Pydantic` · installs (wheel) · licence: MIT License · rank 5979 · last release 2025-12-22 · [PyPI](https://pypi.org/project/Flask-Pydantic/) · [source](https://github.com/pallets-eco/flask-pydantic)

<details><summary>README extract</summary>

Flask extension for integration of the awesome pydantic package with Flask.

Example:
```python
from typing import Optional
from flask import Flask, request
from pydantic import BaseModel

from flask_pydantic import validate

app = Flask("flask_pydantic_app")

class QueryModel(BaseModel):
  age: int

class ResponseModel(BaseModel):
  id: int
  age: int
  name: str
  nickname: Optional[str] = None

# Example 1: query parameters only
...
```

...

</details>

### veracode-api-signing

Easily sign any request destined for the Veracode API Gateway

`pip install veracode-api-signing` · installs (wheel) · licence: MIT License · rank 6010 · last release 2026-05-27 · [PyPI](https://pypi.org/project/veracode-api-signing/)

### quart-cors

A Quart extension to provide Cross Origin Resource Sharing, access control, support

`pip install quart-cors` · installs (wheel) · licence: MIT License · rank 6075 · last release 2024-12-27 · [PyPI](https://pypi.org/project/quart-cors/)

<details><summary>README extract</summary>

Quart-CORS is an extension for Quart to enable and control Cross
Origin Resource Sharing, CORS (also
known as access control).

CORS is required to share resources in browsers due to the Same
Origin Policy
which prevents resources being used from a different origin. ...

Example:
```python
from quart_cors import cors

app = Quart(name)
app = cors(app, **settings)

blueprint = Blueprint(name)
blueprint = cors(blueprint, **settings)
```

Sections: Quart-CORS, Usage, Simple examples, Help

</details>

### celery-progress

Drop in, configurable, dependency-free progress bars for your Django/Celery applications.

`pip install celery-progress` · installs (wheel) · licence: MIT License · rank 6076 · last release 2025-01-30 · [PyPI](https://pypi.org/project/celery-progress/)

<details><summary>README extract</summary>

Drop in, dependency-free progress bars for your Django/Celery applications.

Super simple setup. Lots of customization available.

Celery Progress Bar demo on SaaS Pegasus

Starting with Celery can be challenging, eeintech built a complete Django demo application along with a step-by-step guide to get you started on building your own progress bar!

Example:
```python
from django.urls import path, include

urlpatterns = [
    # your project's patterns here
    ...
    path(r'^celery-progress/', include('celery_progress.urls')),  # add this line (the endpoint is configurable)
]
```

...

</details>

### plantuml

(no summary)

`pip install plantuml` · installs (wheel) · licence: BSD License · rank 6082 · last release 2019-11-01 · [PyPI](https://pypi.org/project/plantuml/)

<details><summary>README extract</summary>

Plantuml is a library for
generating UML diagrams from a simple text markup language.

This is a simple python remote client interface to a
plantuml server using the
same custom encoding used by most other plantuml
clients. ...

Sections: Python-PlantUML, Command line help, Project Links

</details>

### django-jazzmin

Drop-in theme for django admin, that utilises AdminLTE 3 & Bootstrap 5 to make yo' admin look jazzy

`pip install django-jazzmin` · installs (wheel) · licence: MIT · rank 6098 · last release 2026-06-25 · [PyPI](https://pypi.org/project/django-jazzmin/) · [docs](https://django-jazzmin.readthedocs.io) · [source](https://github.com/farridav/django-jazzmin)

<details><summary>README extract</summary>

Features:
- Drop-in admin skin, all configuration optional
- Customisable side menu
- Customisable top menu
- Customisable user menu
- 4 different Change form templates (horizontal tabs, vertical tabs, carousel, collapsible) ...

Sections: Django jazzmin (Jazzy Admin), Documentation, Demo, Features, Screenshots, Dashboard, List view, Change form templates, Collapsed side menu, Expanded side menu, Horizontal tabs, Vertical tabs, Collapsible, Carousel

</details>

### django-postgres-extra

Bringing all of PostgreSQL's awesomeness to Django.

`pip install django-postgres-extra` · installs (wheel) · licence: MIT License · rank 6150 · last release 2026-10-05 · [PyPI](https://pypi.org/project/django-postgres-extra/)

<details><summary>README extract</summary>

| | | |

| :white_check_mark: | Tests | |
| :memo: | License | |
| :package: | PyPi | |
| :four_leaf_clover: | Code coverage | |
| | Django Versions | 2.0, 2.1, 2.2, 3.0, 3.1, 3.2, 4.0, 4.1, 4.2, 5.0, 5.1, 5.2 |
| | Python Versions | 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13 |
| | Psycopg Versions | 2, 3 |
| :book: | Documentation | Read The Docs |
| ...

Sections: Major features, Working with the code, Prerequisites, Getting started

</details>

### django-bulk-update

Bulk update using one query over Django ORM.

`pip install django-bulk-update` · installs (wheel) · licence: BSD License · rank 6163 · last release 2017-08-12 · [PyPI](https://pypi.org/project/django-bulk-update/)

<details><summary>README extract</summary>

Simple bulk update over Django ORM or with helper function.

This project aims to bulk update given objects using one query over
Django ORM.

Example:
```python
# Note: SQlite is unable to run the `timeit` tests
# due to the max number of sql variables
In [1]: import os
In [2]: import timeit
In [3]: import django

In [4]: os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
In [5]: django.setup()

In [6]: from tests.fixtures import create_fixtures

...
```

Sections: django-bulk-update, Usage, Performance Tests, Requirements, TODO

</details>

### django-auth-ldap

Django LDAP authentication backend

`pip install django-auth-ldap` · installs (wheel) · licence: BSD-3-Clause · rank 6171 · last release 2026-10-20 · [PyPI](https://pypi.org/project/django-auth-ldap/) · [docs](https://django-auth-ldap.readthedocs.io/) · [source](https://github.com/django-auth-ldap/django-auth-ldap)

<details><summary>README extract</summary>

This is a Django authentication backend that authenticates against an LDAP
service. Configuration can be as simple as a single distinguished name
template, but there are many rich configuration options for working with users,
groups, and permissions.

* License: BSD 2-Clause

Example:
```python
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

# Baseline configuration.
AUTH_LDAP_SERVER_URI = 'ldap://ldap.example.com'

AUTH_LDAP_BIND_DN = 'cn=django-agent,dc=example,dc=com'
AUTH_LDAP_BIND_PASSWORD = 'phlebotinum'
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    'ou=users,dc=example,dc=com',
    ldap.SCOPE_SUBTREE,
...
```

Sections: Django Authentication Using LDAP, Example Configuration

</details>

### django-migrations-git-conflicts

A Django app to trigger git conflict on migrations conflict

`pip install django-migrations-git-conflicts` · installs (wheel) · licence: BSD License · rank 6182 · last release 2020-06-23 · [PyPI](https://pypi.org/project/django-migrations-git-conflicts/)

<details><summary>README extract</summary>

Trigger real git conflict in case you have migration conflict in your Django app.

Sections: Django migrations git conflicts, Usage, How it works

</details>

### crispy-bootstrap4

Bootstrap4 template pack for django-crispy-forms

`pip install crispy-bootstrap4` · installs (wheel) · licence: MIT · rank 6183 · last release 2026-02-11 · [PyPI](https://pypi.org/project/crispy-bootstrap4/)

<details><summary>README extract</summary>

Bootstrap4 template pack for django-crispy-forms. This template pack was
included with the core django-crispy-forms package until version 2.0.

Sections: crispy-bootstrap4, Usage

</details>

### netsuitesdk

Python SDK for accessing the NetSuite SOAP webservice

`pip install netsuitesdk` · installs (wheel) · licence: MIT License · rank 6256 · last release 2026-07-21 · [PyPI](https://pypi.org/project/netsuitesdk/)

<details><summary>README extract</summary>

Netsuite-sdk-py is a Python SDK. It uses the SOAP client library zeep( for accessing NetSuite resources via the NetSuite SOAP web service SuiteTalk( but hides the complexity from the SDK user.

Example:
```python
import os
import itertools
import json
from netsuitesdk import NetSuiteConnection

def connect_tba():
    NS_ACCOUNT = os.getenv('NS_ACCOUNT')
    NS_CONSUMER_KEY = os.getenv('NS_CONSUMER_KEY')
    NS_CONSUMER_SECRET = os.getenv('NS_CONSUMER_SECRET')
    NS_TOKEN_KEY = os.getenv('NS_TOKEN_KEY')
    NS_TOKEN_SECRET = os.getenv('NS_TOKEN_SECRET')
...
```

Sections: netsuite-sdk-py, Get Started, Token-based Auth, Remarks and possible errors regarding authentication, Search, Upsert, UpsertList, Integration Tests, Code coverage, Documentation

</details>

### google-reauth

Google Reauth Library

`pip install google-reauth` · installs (wheel) · licence: Apache Software License · rank 6269 · last release 2020-12-01 · [PyPI](https://pypi.org/project/google-reauth/)

<details><summary>README extract</summary>

This library provides Reauth support to Google's authentication libraries for
Python. Reauth allows using two-factor authentication for end-user credentials.

Other than for reference purposes, this library is of little use to non-Google
developers.

</details>

### drf-extra-fields

Additional fields for Django Rest Framework.

`pip install drf-extra-fields` · installs (wheel) · licence: BSD License · rank 6283 · last release 2023-08-08 · [PyPI](https://pypi.org/project/drf-extra-fields/)

<details><summary>README extract</summary>

Extra Fields for Django Rest Framework

- v3.7.0
 - `psycopg` (psycopg 3) is now supported and it's used automatically instead of `psycopg2` if available.
- v3.6.0
 - File objects without an actual file-system path can now be used in `Base64ImageField`, `Base64FileField` and `HybridImageField` ...

Example:
```python
# serializer

from drf_extra_fields.fields import Base64ImageField

class UploadedBase64ImageSerializer(serializers.Serializer):
    file = Base64ImageField(required=False)
    created = serializers.DateTimeField()

# use the serializer
file = 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='
...
```

...

</details>

### pywikibot

Python MediaWiki Bot Framework

`pip install pywikibot` · installs (wheel) · licence: MIT · rank 6367 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pywikibot/) · [docs](https://doc.wikimedia.org/pywikibot/stable/) · [source](https://gerrit.wikimedia.org/r/plugins/gitiles/pywikibot/core/)

<details><summary>README extract</summary>

The Pywikibot framework is a Python library that interfaces with the
MediaWiki API
version 1.31 or higher.

Also included are various general function scripts that can be adapted for
different tasks.

For further information about the library excluding scripts see
the full code documentation.

Example:
```python
import pywikibot
site = pywikibot.Site('en', 'wikipedia')  # The site we want to run our bot on
page = pywikibot.Page(site, 'Wikipedia:Sandbox')
page.text = page.text.replace('foo', 'bar')
page.save('Replacing "foo" with "bar"')  # Saves the page
```

Sections: Pywikibot, Quick start, Basic Usage, Wikibase Usage, Script example, Roadmap, Deprecations, Pending removal in Pywikibot 12, Pending removal in Pywikibot 13, Pending removal in Pywikibot 14

</details>

### wiremock

Wiremock Admin API Client

`pip install wiremock` · installs (wheel) · licence: Apache Software License; Other/Proprietary License · rank 6381 · last release 2025-07-28 · [PyPI](https://pypi.org/project/wiremock/)

<details><summary>README extract</summary>

WireMock open source is supported by WireMock Cloud. Please consider trying it out if your team needs advanced capabilities such as OpenAPI, dynamic state, data sources and more.

Python WireMock is a library that allows users to interact with a WireMock instance from within a Python project. ...

Features:
WireMock can run in unit tests, as a standalone process or a container. Key features include:

- Testcontainers Python module to easily start WireMock server for your tests
- REST API Client for a standalone WireMock Java server ...

Sections: Python WireMock, Key Features, References, Examples

</details>

### gallery-dl

Command-line program to download image galleries and collections from several image hosting sites

`pip install gallery-dl` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 6383 · last release 2026-10-31 · [PyPI](https://pypi.org/project/gallery-dl/)

_README extract left out: share-alike licence._

### django-crum

Django middleware to capture current request and user.

`pip install django-crum` · installs (wheel) · licence: BSD License · rank 6435 · last release 2020-11-10 · [PyPI](https://pypi.org/project/django-crum/) · [docs](https://django-crum.rtfd.org/) · [source](https://github.com/ninemoreminutes/django-crum/)

<details><summary>README extract</summary>

Django-CRUM (Current Request User Middleware) captures the current request and
user in thread local storage.

It enables apps to check permissions, capture audit trails or otherwise access
the current request and user without requiring the request object to be passed
directly. ...

</details>

### Flask-Principal

Identity management for flask

`pip install Flask-Principal` · installs from source (sdist only) · licence: MIT License · rank 6442 · last release 2013-06-14 · [PyPI](https://pypi.org/project/Flask-Principal/)

<details><summary>README extract</summary>

Flask Principal

Identity management for Flask.

Links

</details>

### django-cryptography-django5

Easily encrypt data in Django - Fork for Django 5 support

`pip install django-cryptography-django5` · installs (wheel) · licence: BSD License · rank 6507 · last release 2024-06-04 · [PyPI](https://pypi.org/project/django-cryptography-django5/) · [docs](https://django-cryptography.readthedocs.io) · [source](https://github.com/chrisclark/django-cryptography)

<details><summary>README extract</summary>

A set of primitives for easily encrypting data in Django, wrapping
the Python Cryptography library. Also provided is a drop in
replacement for Django's own cryptographic primitives, using
Cryptography as the backend provider.

Do not forget to read the documentation.

Example:
```python
from django.db import models

from django_cryptography.fields import encrypt

class MyModel(models.Model):
    name = models.CharField(max_length=50)
    sensitive_data = encrypt(models.CharField(max_length=50))
```

Sections: Django Cryptography, Cryptography by example, Requirements

</details>

### pylogbeat

Simple, incomplete implementation of the Beats protocol used by Elastic Beats and Logstash.

`pip install pylogbeat` · installs (wheel) · licence: Apache Software License · rank 6539 · last release 2025-11-23 · [PyPI](https://pypi.org/project/pylogbeat/) · [source](https://github.com/eht16/pylogbeat/)

<details><summary>README extract</summary>

PyLogBeat is a simple, incomplete implementation of the Beats protocol
used by Elastic Beats and Logstash. For more information about Beats see
 and

With this library it is possible to send log messages or any data to
Logstash' beats input plugin or any other service which implements
the Beats protocol. ...

Example:
```python
import logging
logging.getLogger('pylogbeat').setLevel(logging.DEBUG)
```

Sections: PyLogBeat, Simple use, Using a context manager, Using a SSL connection, Example message, 2.1.0 / 2025-11-23, 2.0.1 / 2023-07-30, 2.0.0 / 2020-10-04, 1.0.5 / 2020-10-04, 1.0.4 / 2020-05-06, 1.0.3 / 2020-04-22, 1.0.2 / 2018-12-31, 1.0.1 / 2018-12-31, 1.0.0 / 2018-12-31

</details>

### djangorestframework-xml

XML support for Django REST Framework

`pip install djangorestframework-xml` · installs (wheel) · licence: BSD License · rank 6541 · last release 2020-04-12 · [PyPI](https://pypi.org/project/djangorestframework-xml/)

<details><summary>README extract</summary>

[![build-status-image]][github-action]
[![pypi-version]][pypi]

XML support for Django REST Framework

Full documentation for the project is available at

Features:
XML support extracted as a third party package directly from the official Django REST Framework implementation. It requires the defusedxml package only because it safeguards against some security issues that were discovered. ...

Example:
```python
from rest_framework import routers, serializers, viewsets
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

...
```

...

</details>

### validator-collection

Collection of 60+ Python functions for validating data

`pip install validator-collection` · installs (wheel) · licence: MIT License · rank 6559 · last release 2020-10-12 · [PyPI](https://pypi.org/project/validator-collection/) · [docs](http://validator-collection.readthedocs.io/en/latest) · [source](https://github.com/insightindustry/validator-collection/)

<details><summary>README extract</summary>

Python library of 60+ commonly-used validator functions

The Validator Collection is a Python library that provides more than 60
functions that can be used to validate the type and contents of an input value.

Each function has a consistent syntax for easy use, and has been tested on
Python 2.7, 3.4, 3.5, 3.6, 3.7, and 3.8. ...

Example:
```python
from validator_collection import validators, checkers, errors

email_address = validators.email('test@domain.dev')
# The value of email_address will now be "test@domain.dev"

email_address = validators.email('this-is-an-invalid-email')
# Will raise a ValueError

try:
    email_address = validators.email(None)
    # Will raise an EmptyValueError
...
```

...

</details>

### djangorestframework-filters

Better filtering for Django REST Framework

`pip install djangorestframework-filters` · installs (wheel) · licence: BSD License · rank 6604 · last release 2019-03-21 · [PyPI](https://pypi.org/project/djangorestframework-filters/)

<details><summary>README extract</summary>

`django-rest-framework-filters` is an extension to Django REST framework and Django filter
that makes it easy to filter across relationships. Historically, this extension also provided a
number of additional features and fixes, however the number of features has shrunk as they are
merged back into `django-filter`. ...

Features:
* Easy filtering across relationships
* Support for method filtering across relationships
* Automatic filter negation with a simple `param!=value` syntax
* Backend caching to increase performance

Example:
```python
# django-filter
from django_filters.rest_framework import FilterSet, filters

class ProductFilter(FilterSet):
    manufacturer = filters.ModelChoiceFilter(queryset=Manufacturer.objects.all())
    ...

# django-rest-framework-filters
...

</details>

### pysolr

Lightweight Python client for Apache Solr

`pip install pysolr` · installs from source (sdist only) · licence: BSD License · rank 6613 · last release 2025-11-18 · [PyPI](https://pypi.org/project/pysolr/)

<details><summary>README extract</summary>

`pysolr` is a lightweight Python client for Apache Solr. It provides an
interface that queries the server and returns results based on the query.

Features:
* Basic operations such as selecting, updating & deleting.
* Index optimization.
* "More Like This" support (if set up in Solr).
* Spelling correction (if set up in Solr).
* Timeout support.
* SolrCloud awareness

Example:
```python
import pysolr

# Create a client instance. The timeout and authentication options are not required.
solr = pysolr.Solr(' always_commit=True, [timeout=10], [auth=<type of authentication>])

# Note that auto_commit defaults to False for performance. You can set
# `auto_commit=True` to have commands always update the index immediately, make
...
```

...

</details>

### RESTFly

Write your own API Client libraries quickly.

`pip install RESTFly` · installs (wheel) · licence: not stated · rank 6616 · last release 2026-11-06 · [PyPI](https://pypi.org/project/RESTFly/) · [docs](https://restfly.rtfd.io) · [source](https://github.com/librestfly/restfly)

<details><summary>README extract</summary>

Building API SDKs can be often be difficult. There is often a lot of boilerplate code
that is reused over and over again between classes, packages, and even libraries.
RESTFly is designed to try to remove as much of that boilerplate code as possible. ...

Features:
After building several SDKs over the years, I wanted something that could abstract away
a lot of the boilerplate code that I kept having to write over and over. ...

Sections: What is RESTFly?, Why RESTFly?

</details>

### djangorestframework-gis

Geographic add-ons for Django Rest Framework

`pip install djangorestframework-gis` · installs (wheel) · licence: BSD License · rank 6627 · last release 2026-09-01 · [PyPI](https://pypi.org/project/djangorestframework-gis/) · [source](https://github.com/openwisp/django-rest-framework-gis)

<details><summary>README extract</summary>

Geographic add-ons for Django Rest Framework.

- Discussions
- Mailing List

Example:
```python
class Location(models.Model):
    """
    A model which holds information about a particular location
    """
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    point = models.PointField()
```

Sections: django-rest-framework-gis, Setup, Compatibility with DRF, Django and Python, Fields, GeometryField, GeometrySerializerMethodField, Serializers, GeoModelSerializer (DEPRECATED), GeoFeatureModelSerializer, Specifying the geometry field: "geo_field", Using GeometrySerializerMethodField as "geo_field", Specifying the ID: "id_field", Bounding Box: "auto_bbox" and "bbox_geo_field", Custom GeoJSON properties source

</details>

### nodriver

[Docs here](https://ultrafunkamsterdam.github.io/nodriver)

`pip install nodriver` · installs (wheel) · licence: not stated · rank 6689 · last release 2026-10-26 · [PyPI](https://pypi.org/project/nodriver/) · [source](https://github.com/UltrafunkAmsterdam/nodriver)

<details><summary>README extract</summary>

* This is the official successor of the Undetected-Chromedriver python package.
* No more webdriver, no more selenium

Direct communication provides even better resistance against web applicatinon firewalls (WAF’s), while
performance gets a massive boost.
This module is, contrary to undetected-chromedriver, fully asynchronous. ...

Example:
```python
import random
import string
import logging

logging.basicConfig(level=30)

import nodriver as uc

months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]

async def main():
    driver = await uc.start()

...
```

Sections: NODRIVER, for docs click here, Some features, more examples in the ./example/ folder

</details>

### supertokens-python

SuperTokens SDK for Python

`pip install supertokens-python` · installs (wheel) · licence: Apache Software License · rank 6699 · last release 2026-10-21 · [PyPI](https://pypi.org/project/supertokens-python/)

<details><summary>README extract</summary>

This is a Python library that is used to interface between a python API process and the SuperTokens http service.

Learn more at

To see documentation, please click here.

Sections: SuperTokens Python SDK, About, Documentation, Contact us

</details>

### django-jinja

Jinja2 templating language integrated in Django.

`pip install django-jinja` · installs (wheel) · licence: BSD License · rank 6727 · last release 2023-09-03 · [PyPI](https://pypi.org/project/django-jinja/)

<details><summary>README extract</summary>

Simple and nonobstructive jinja2 integration with Django.

Documentation:

</details>

### Flask-Script

Scripting support for Flask

`pip install Flask-Script` · installs from source (sdist only) · licence: BSD License · rank 6760 · last release 2017-09-06 · [PyPI](https://pypi.org/project/Flask-Script/)

<details><summary>README extract</summary>

Flask-Script

Flask support for writing external scripts.

Links

</details>

### fpgen

A fast & comprehensive browser fingerprint generator

`pip install fpgen` · installs (wheel) · licence: Apache Software License · rank 6777 · last release 2025-03-22 · [PyPI](https://pypi.org/project/fpgen/) · [source](https://github.com/scrapfly/fingerprint-generator)

<details><summary>README extract</summary>

A fast browser data generator that mimics actual traffic patterns in the wild. With extensive data coverage.

Created by daijro. Data provided by Scrapfly.

Features:
- Uses a Bayesian generative network to mimic real-world web traffic patterns
- Extensive data coverage for nearly all known browser data points
- Creates complete fingerprints in a few milliseconds ⚡ ...

Example:
```python
# Constrain `client`:
fpgen.generate(client={'browser': {'major': lambda v: int(v) >= 130}})
# Or, just pass a dot seperated path:
fpgen.generate({'client.browser.major': lambda v: int(v) >= 130})
```

...

</details>

### zernio-sdk

The official Python library for the Zernio API

`pip install zernio-sdk` · installs (wheel) · licence: Apache Software License · rank 6778 · last release 2026-11-08 · [PyPI](https://pypi.org/project/zernio-sdk/) · [docs](https://docs.zernio.com) · [source](https://github.com/zernio-dev/zernio-python)

<details><summary>README extract</summary>

One API to post everywhere. 16 platforms, zero headaches.

The official Python SDK for the Zernio API — schedule and publish social media posts across Instagram, TikTok, YouTube, LinkedIn, X/Twitter, Facebook, Pinterest, Threads, Bluesky, Reddit, Snapchat, Telegram, WhatsApp, and Google Business Profile with a single integration.

Example:
```python
from zernio import Zernio

# Reads ZERNIO_API_KEY from environment (or pass explicitly)
client = Zernio()

# Publish to multiple platforms with one call
post = client.posts.create(
    content="Hello world from Zernio!",
    platforms=[
        {"platform": "twitter", "accountId": "acc_xxx"},
...
```

...

</details>

### python-logstash-async

Asynchronous Python logging handler for Logstash.

`pip install python-logstash-async` · installs (wheel) · licence: MIT License · rank 6780 · last release 2025-11-23 · [PyPI](https://pypi.org/project/python-logstash-async/) · [docs](https://python-logstash-async.readthedocs.io/en/stable/) · [source](https://github.com/eht16/python-logstash-async/)

<details><summary>README extract</summary>

Python Logstash Async is an asynchronous Python logging handler to submit
log events to a remote Logstash instance.

Unlike most other Python Logstash logging handlers, this package works asynchronously
by collecting log events from Python's logging subsystem and then transmitting the
collected events in a separate worker thread to Logstash. ...

Sections: python-logstash-async, Get the Source

</details>

### args

Command Arguments for Humans.

`pip install args` · installs from source (sdist only) · licence: BSD License · rank 6828 · last release 2012-05-08 · [PyPI](https://pypi.org/project/args/)

<details><summary>README extract</summary>

args
~~~~

This simple module gives you an elegant interface for your command line argumemnts.

</details>

### starlette-prometheus

Prometheus integration for Starlette

`pip install starlette-prometheus` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6859 · last release 2024-09-03 · [PyPI](https://pypi.org/project/starlette-prometheus/) · [source](https://github.com/PeRDy/starlette-prometheus)

_README extract left out: share-alike licence._

### pyuwsgi

The uWSGI server

`pip install pyuwsgi` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 6891 · last release 2026-02-24 · [PyPI](https://pypi.org/project/pyuwsgi/)

_README extract left out: share-alike licence._

### drf-jwt

JSON Web Token based authentication for Django REST framework

`pip install drf-jwt` · installs (wheel) · licence: MIT License · rank 6904 · last release 2022-01-09 · [PyPI](https://pypi.org/project/drf-jwt/)

<details><summary>README extract</summary>

JSON Web Token Authentication support for Django REST Framework

Features:
This package provides JSON Web Token Authentication support
for Django REST framework.

If you want to know more about JWT, check out the following resources:

 - DjangoCon 2014 - JSON Web Tokens Video | Slides
 - Auth with JSON Web Tokens
 - JWT.io

Sections: REST framework JWT Auth, Overview, Requirements

</details>

### graphene-file-upload

Lib for adding file upload functionality to GraphQL mutations in Graphene Django and Flask-Graphql

`pip install graphene-file-upload` · installs (wheel) · licence: MIT License · rank 6916 · last release 2021-02-20 · [PyPI](https://pypi.org/project/graphene-file-upload/)

<details><summary>README extract</summary>

`graphene-file-upload` is a drop in replacement for the the GraphQL
view in Graphene for Django, and for Flask-Graphql.

It supports multi-part file uploads that adhere to the Multipart Request Spec.

It currently supports Python 2.7 and 3.4+.

Example:
```python
from graphene_file_upload.scalars import Upload

class UploadMutation(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)

    success = graphene.Boolean()

    def mutate(self, info, file, **kwargs):
        # do something with your file

        return UploadMutation(success=True)
```

Sections: graphene-file-upload, Usage, Django Integration, Flask Integration, Flask, Django, Using pytest, Using unittest, Packaging for PyPi

</details>

### flask-smorest

Flask/Marshmallow-based REST API framework

`pip install flask-smorest` · installs (wheel) · licence: MIT License · rank 6942 · last release 2026-03-22 · [PyPI](https://pypi.org/project/flask-smorest/) · [source](https://github.com/marshmallow-code/flask-smorest)

<details><summary>README extract</summary>

flask-smorest (formerly known as flask-rest-api) is a REST API framework
built upon Flask and
marshmallow.

Features:
- Serialization, deserialization and validation using marshmallow `Schema`
- Explicit validation error messages returned in response
- Database-agnostic ...

Sections: flask-smorest, 'cause everybody wants s'more, Features, Documentation

</details>

### pywhatwgurl

Pure Python implementation of the WHATWG URL Standard.

`pip install pywhatwgurl` · installs (wheel) · licence: MIT License · rank 7005 · last release 2026-07-14 · [PyPI](https://pypi.org/project/pywhatwgurl/) · [docs](https://pywhatwgurl.github.io/pywhatwgurl) · [source](https://github.com/pywhatwgurl/pywhatwgurl)

<details><summary>README extract</summary>

Pure Python implementation of the WHATWG URL Standard. The goal is a small, spec-faithful library for parsing, serializing, and manipulating URLs.

> pywhatwgurl is listed as a complete Python implementation in the official WHATWG URL repository.

Status

- 100% WHATWG URL Standard conformance for core URL parsing ...

Example:
```python
from pywhatwgurl import URL

url = URL("

url.hostname   # 'example.com'
url.port       # '8080'
url.pathname   # '/path'
url.search     # '?q=1'
url.hash       # '#frag'
str(url)       # '
```

Sections: pywhatwgurl - Python WHATWG URL Parser, IDNA Limitations

</details>

### Flask-Security-Too

Quickly add security features to your Flask application.

`pip install Flask-Security-Too` · installs (wheel) · licence: MIT License · rank 7124 · last release 2026-10-21 · [PyPI](https://pypi.org/project/Flask-Security-Too/) · [docs](https://flask-security.readthedocs.io) · [source](https://github.com/pallets-eco/flask-security)

### grequests

Requests + Gevent

`pip install grequests` · installs (wheel) · licence: BSD License · rank 7135 · last release 2023-06-08 · [PyPI](https://pypi.org/project/grequests/)

<details><summary>README extract</summary>

GRequests allows you to use Requests with Gevent to make asynchronous HTTP
Requests easily.

Usage

Usage is simple::

 import grequests

 urls = [

Create a set of unsent Requests::

 >>> rs = (grequests.get(u) for u in urls)

Send them all at the same time:: ...

</details>

### broadcaster

Simple broadcast channels.

`pip install broadcaster` · installs (wheel) · licence: BSD License · rank 7245 · last release 2024-08-01 · [PyPI](https://pypi.org/project/broadcaster/)

<details><summary>README extract</summary>

Broadcaster helps you develop realtime streaming functionality by providing
a simple broadcast API onto a number of different backend services.

It currently supports Redis PUB/SUB, Redis Streams, Apache Kafka, and Postgres LISTEN/NOTIFY, plus a simple in-memory backend, that you can use for local development or during testing. ...

Example:
```python
# Requires: `starlette`, `uvicorn`, `jinja2`
# Run with `uvicorn example:app`
import anyio
from broadcaster import Broadcast
from starlette.applications import Starlette
from starlette.routing import Route, WebSocketRoute
from starlette.templating import Jinja2Templates

broadcast = Broadcast("redis://localhost:6379")
...
```

...

</details>

### django-classy-tags

Class based template tags for Django

`pip install django-classy-tags` · installs (wheel) · licence: BSD License · rank 7289 · last release 2023-07-29 · [PyPI](https://pypi.org/project/django-classy-tags/)

<details><summary>README extract</summary>

The goal of this project is to create a new way of writing Django template tags
which is fully compatible with the current Django templating infrastructure.
This new way should be easy, clean and require as little boilerplate code as
possible while still staying as powerful as possible. Some features:

* Class based template tags. ...

Example:
```python
from classytags.core import Options
from classytags.helpers import AsTag
from classytags.arguments import Argument
from django import template

register = template.Library()

class Hello(AsTag):
    options = Options(
        Argument('name', required=False, default='world'),
        'as',
        Argument('varname', required=False, resolve=False)
...
```

Sections: Django Classy Tags, Documentation, Example, Running Tests

</details>

### phonetics

Compute phonetic key of strings for indexing or fuzzy matching

`pip install phonetics` · installs from source (sdist only) · licence: MIT License · rank 7290 · last release 2018-03-23 · [PyPI](https://pypi.org/project/phonetics/)

<details><summary>README extract</summary>

The phonetics module computes the phonetic key of a string using different algorithms.

 * Soundex
 * NYSISS
 * Metaphone
 * Double Metaphone

Example:
```python
>>> import phonetics
>>> phonetics.dmetaphone('Danger')
('TNJR', 'TNKR')
```

Sections: Phonetics, Running tests, Usage

</details>

### django-cache-memoize

Django utility for a memoization decorator that uses the Django cache framework.

`pip install django-cache-memoize` · installs (wheel) · licence: MIT License; Mozilla Public License 2.0 (MPL 2.0) · rank 7353 · last release 2024-12-18 · [PyPI](https://pypi.org/project/django-cache-memoize/)

<details><summary>README extract</summary>

* License: MPL 2.0

Django utility for a memoization decorator that uses the Django cache framework.

For versions of Python and Django, check out the tox.ini file.

Features:
* Memoized function calls can be invalidated.

* Works with non-trivial arguments and keyword arguments

* Insight into cache hits and cache missed with a callback. ...

Example:
```python
# Import the decorator
from cache_memoize import cache_memoize

# Attach decorator to cacheable function with a timeout of 100 seconds.
@cache_memoize(100)
def expensive_function(start, end):
    return random.randint(start, end)

# Just a regular Django view
def myview(request):
    # If you run this view repeatedly you'll get the same
...
```

...

</details>

### python-jobspy

JobSpy: job scraper for LinkedIn, Indeed, Glassdoor, ZipRecruiter, Bayt, Naukri, BDJobs & HelloWork

`pip install python-jobspy` · installs (wheel) · licence: MIT · rank 7385 · last release 2026-10-23 · [PyPI](https://pypi.org/project/python-jobspy/) · [docs](https://github.com/speedyapply/JobSpy#readme)

<details><summary>README extract</summary>

JobSpy is a job scraping library that aggregates jobs from popular job boards with one tool:

- Scrapes job postings from LinkedIn, Indeed, Glassdoor, ZipRecruiter, Bayt, Naukri, BDJobs & HelloWork concurrently
- Aggregates the job postings in a dataframe
- Proxy support to bypass blocking

Example:
```python
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],  # also "bayt", "naukri", "bdjobs", "hellowork"
    search_term="software engineer",
    location="San Francisco, CA",
    results_wanted=20,
    hours_old=72,
    country_indeed="USA",
...
```

...

</details>

### httpx2-jsfetch

httpx2 transports for Emscripten/Pyodide, backed by the JavaScript fetch API.

`pip install httpx2-jsfetch` · installs (wheel) · licence: BSD-3-Clause · rank 7402 · last release 2026-08-07 · [PyPI](https://pypi.org/project/httpx2-jsfetch/)

### urlcanon

url canonicalization library for python and java

`pip install urlcanon` · installs from source (sdist only) · licence: Apache Software License · rank 7439 · last release 2019-07-02 · [PyPI](https://pypi.org/project/urlcanon/)

<details><summary>README extract</summary>

A URL canonicalization (normalization) library for Python and Java.

It currently provides:

* A URL parser which preserves the input bytes exactly
* A precanned canonicalization ruleset that tries to match the normalization
 implicit in the parsing rules used by browsers
* An alternative URL serialization suitable for sorting and ...

Example:
```python
>>> import urlcanon
>>> input_url = "
>>> parsed_url = urlcanon.parse_url(input_url)
>>> print(parsed_url)

>>> urlcanon.whatwg(parsed_url)
<urlcanon.parse.ParsedUrl object at 0x10eb13a58>
>>> print(parsed_url)

>>> print(parsed_url.ssurt())
b'com,example,//:http/bar'
>>>
>>> rule = urlcanon.MatchRule(ssurt=b'com,example,//:http/bar')
...
```

Sections: urlcanon, Examples, Python, Java

</details>

### django-cachalot

Caches your Django ORM queries and automatically invalidates them.

`pip install django-cachalot` · installs (wheel) · licence: BSD License · rank 7467 · last release 2026-08-10 · [PyPI](https://pypi.org/project/django-cachalot/)

<details><summary>README extract</summary>

Caches your Django ORM queries and automatically invalidates them.

Documentation:

Table of Contents:

- Quickstart
- Usage
- Hacking
- Benchmark
- Third-Party Cache Comparison
- Discussion

Sections: Django Cachalot, Quickstart, Usage, . If you use multiple servers with a common cache server,, . If you modify data outside Django, . Be aware of the few other limits, . If you use, . Enjoy!, Hacking, . For PostgreSQL: `CREATE ROLE cachalot LOGIN SUPERUSER;`, Benchmark, . Run: ``python benchmark.py`, Third-Party Cache Comparison

</details>

### zendriver

A blazing fast, async-first, undetectable webscraping/web automation framework

`pip install zendriver` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 7490 · last release 2026-10-02 · [PyPI](https://pypi.org/project/zendriver/)

_README extract left out: share-alike licence._

### django-chunkator

Chunk large QuerySets into small chunks, and iterate over them without killing your RAM.

`pip install django-chunkator` · installs (wheel) · licence: MIT License · rank 7524 · last release 2020-06-22 · [PyPI](https://pypi.org/project/django-chunkator/)

<details><summary>README extract</summary>

Chunk large QuerySets into small chunks, and iterate over them without killing
your RAM.

Tested with all the combinations of:

* Python: 3.5, 3.6, 3.7, 3.8
* Django: 2, 2.1, 2.2, 3.0, master

Example:
```python
from chunkator import chunkator
for item in chunkator(LargeModel.objects.all(), 200):
    do_something(item)
```

Sections: django-chunkator, Usage

</details>

### Sanic-Cors

A Sanic extension adding a decorator for CORS support. Based on flask-cors by Cory Dolphin.

`pip install Sanic-Cors` · installs (wheel) · licence: MIT License · rank 7525 · last release 2022-10-07 · [PyPI](https://pypi.org/project/Sanic-Cors/)

<details><summary>README extract</summary>

A Sanic extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible. Based on
flask-cors by Cory Dolphin.

This package has a simple philosophy, when you want to enable CORS, you
wish to enable it for all use cases on a domain. This means no mucking
around with different allowed headers, methods, etc. ...

Example:
```python
from sanic import Sanic
from sanic.response import text
from sanic_cors import CORS, cross_origin

app = Sanic(name)
CORS(app)

@app.route("/", methods=['GET', 'OPTIONS'])
def hello_world(request):
  return text("Hello, cross-origin-world!")
```

Sections: Sanic-CORS, Usage, Simple Usage, Resource specific CORS, Route specific CORS via decorator, Sanic-Ext Usage, Documentation, Preflight Requests, Tests

</details>

### envparse

Simple environment variable parsing

`pip install envparse` · installs from source (sdist only) · licence: MIT License · rank 7533 · last release 2015-12-19 · [PyPI](https://pypi.org/project/envparse/)

<details><summary>README extract</summary>

`envparse` is a simple utility to parse environment variables.

If you use Heroku and/or subscribe to the tenets of the
12 Factor App
you'll be using a lot of environment variable-based configuration in your app. ...

Example:
```python
# Standard
from envparse import env

# Schema
from envparse import Env
env = Env(BOOLEAN_VAR=bool, LIST_VAR=dict(type=list, subtype=int))
```

Sections: envparse, Usage, Schemas, Pre- and Postprocessors, Environment File, Tests

</details>

### Cheetah3

Cheetah is a template engine and code generation tool

`pip install Cheetah3` · installs from source (sdist only) · licence: MIT License · rank 7570 · last release 2021-02-22 · [PyPI](https://pypi.org/project/Cheetah3/) · [docs](https://cheetahtemplate.org/users_guide/index.html)

<details><summary>README extract</summary>

Cheetah3 is a free and open source template engine and code generation tool.

It can be used standalone or combined with other tools and frameworks. Web
development is its principle use, but Cheetah is very flexible and
is also being used to generate C++ game code, Java, sql, form emails
and even Python code. ...

Sections: Documentation, Recent Changes

</details>

### citeurl

an extensible tool to process legal citations in text

`pip install citeurl` · installs (wheel) · licence: MIT License · rank 7577 · last release 2026-09-25 · [PyPI](https://pypi.org/project/citeurl/)

<details><summary>README extract</summary>

CiteURL is an extensible tool that parses legal citations and makes links to websites where you can read the relevant law for free. It can be used to quickly look up a reference, or to insert a hyperlink for every long- or short-form citation found in a longer text.

If you want to quickly try it out, it's available as a web app at citation.link. ...

</details>

### dj-email-url

Use an URL to configure email backend settings in your Django Application.

`pip install dj-email-url` · installs (wheel) · licence: BSD License · rank 7596 · last release 2022-09-24 · [PyPI](https://pypi.org/project/dj-email-url/)

<details><summary>README extract</summary>

This utility is based on dj-database-url by Kenneth Reitz.

It allows to utilize the 12factor_ inspired environments variable to
configure the email backend in a Django application.

Example:
```python
import dj_email_url
```

Sections: dj-email-url, Usage, Set from email addresses, Other settings, More info, SMTP backend, File backend, 1.0.6_ - 2022-09-24, 1.0.5_ - 2022-02-05, 1.0.4_ - 2022-01-16, 1.0.3_ - 2022-01-16, 1.0.2_ - 2021-01-23, 1.0.1_ - 2020-06-03, 1.0.0_ - 2020-02-16

</details>

### late-sdk

The official Python library for the Zernio API

`pip install late-sdk` · installs (wheel) · licence: Apache Software License · rank 7606 · last release 2026-11-08 · [PyPI](https://pypi.org/project/late-sdk/) · [docs](https://docs.zernio.com) · [source](https://github.com/zernio-dev/zernio-python)

<details><summary>README extract</summary>

One API to post everywhere. 16 platforms, zero headaches.

The official Python SDK for the Zernio API — schedule and publish social media posts across Instagram, TikTok, YouTube, LinkedIn, X/Twitter, Facebook, Pinterest, Threads, Bluesky, Reddit, Snapchat, Telegram, WhatsApp, and Google Business Profile with a single integration.

Example:
```python
from zernio import Zernio

# Reads ZERNIO_API_KEY from environment (or pass explicitly)
client = Zernio()

# Publish to multiple platforms with one call
post = client.posts.create(
    content="Hello world from Zernio!",
    platforms=[
        {"platform": "twitter", "accountId": "acc_xxx"},
...
```

...

</details>

### markdown-include

A Python-Markdown extension which provides an 'include' function

`pip install markdown-include` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 7691 · last release 2023-02-07 · [PyPI](https://pypi.org/project/markdown-include/)

_README extract left out: share-alike licence._

### wsgidav

Generic and extendable WebDAV server based on WSGI

`pip install wsgidav` · installs (wheel) · licence: MIT · rank 7752 · last release 2026-11-01 · [PyPI](https://pypi.org/project/wsgidav/) · [docs](https://wsgidav.readthedocs.io) · [source](https://github.com/mar10/wsgidav)

<details><summary>README extract</summary>

A generic and extendable WebDAV server
written in Python and based on WSGI.

Main features:

- WsgiDAV is a stand-alone WebDAV server with SSL support, that can be
 installed and run as Python command line script on Linux, OSX, and Windows:

 Run `wsgidav --help` for a list of available options. ...

Sections: WsgiDAV, More info, this project.

</details>

### favicon

Get a website's favicon.

`pip install favicon` · installs (wheel) · licence: MIT License · rank 7789 · last release 2019-08-31 · [PyPI](https://pypi.org/project/favicon/)

<details><summary>README extract</summary>

`favicon` is a Python library to find a website's favicon.

Example:
```python
>>> import favicon
>>> icons = favicon.get('
Icon(url=' width=144, height=144, format='png')
Icon(url=' width=114, height=114, format='png')
Icon(url=' width=72, height=72, format='png')
Icon(url=' width=0, height=0, format='png')
Icon(url=' width=0, height=0, format='ico')
```

Sections: favicon, Usage, Requirements, Inspiration, 0.7.0 (2019-08-31), 0.6.0 (2019-08-10), 0.5.1 (2018-11-05), 0.5.0 (2018-11-05), 0.4.1 (2018-10-01), 0.4.0 (2018-07-19), 0.3.0 (2018-05-18), 0.2.0 (2018-05-17), 0.1.0 (2018-05-07)

</details>

### Flask-OAuthlib

OAuthlib for Flask

`pip install Flask-OAuthlib` · installs (wheel) · licence: OSI Approved; BSD License · rank 7806 · last release 2020-09-07 · [PyPI](https://pypi.org/project/Flask-OAuthlib/)

<details><summary>README extract</summary>

You SHOULD use instead.

Flask-OAuthlib is an extension to Flask that allows you to interact with
remote OAuth enabled applications. On the client site, it is a replacement
for Flask-OAuth. But it does more than that, it also helps you to create
OAuth providers.

Flask-OAuthlib relies on oauthlib.

Features:
- Support for OAuth 1.0a, 1.0, 1.1, OAuth2 client
- Friendly API (same as Flask-OAuth)
- Direct integration with Flask
- Basic support for remote method invocation of RESTful APIs
- Support OAuth1 provider with HMAC and RSA signature ...

Sections: Flask-OAuthlib, Notice, Features, Links

</details>

### django-sekizai

Django Sekizai

`pip install django-sekizai` · installs (wheel) · licence: BSD License · rank 7824 · last release 2023-05-02 · [PyPI](https://pypi.org/project/django-sekizai/)

<details><summary>README extract</summary>

Sekizai means "blocks" in Japanese, and that's what this app provides. A fresh
look at blocks. With django-sekizai you can define placeholders where your
blocks get rendered and at different places in your templates append to those
blocks. This is especially useful for css and javascript. ...

Sections: Django Sekizai, Documentation, Running Tests

</details>

### zenrows

Zenrows Python SDK: Fetch, Extract (structured data), Batch and Crawl APIs

`pip install zenrows` · installs (wheel) · licence: MIT License · rank 7904 · last release 2026-11-06 · [PyPI](https://pypi.org/project/zenrows/) · [docs](https://www.zenrows.com/documentation) · [source](https://github.com/ZenRows/zenrows-python-sdk)

<details><summary>README extract</summary>

SDK to access Zenrows APIs directly from Python.
Zenrows handles proxies rotation, headless browsers, and CAPTCHAs for you.

This package ships three clients:

 - `ZenRowsClient` — the original synchronous scraping client.
 One URL in, one HTML/JSON response out. Best for ad-hoc scraping.
 - `ZenRowsBatchClient` — the async-job / Batch API client. ...

Example:
```python
from zenrows import ZenRowsClient

client = ZenRowsClient("YOUR-API-KEY", retries=1)
url = "

response = client.fetch(url, params={
    # Deprecated: use client.extract() for structured data instead
    "autoparse": False,

    # CSS Selectors for data extraction (i.e. {"links":"a @href"} to get href attributes from links)
    "css_extractor": "",
...
```

...

</details>

### zope.deferredimport

zope.deferredimport allows you to perform imports names that will only be resolved when used in the code.

`pip install zope.deferredimport` · installs (wheel) · licence: ZPL-2.1 · rank 7909 · last release 2026-02-16 · [PyPI](https://pypi.org/project/zope.deferredimport/) · [docs](https://zopedeferredimport.readthedocs.io/) · [source](https://github.com/zopefoundation/zope.deferredimport)

<details><summary>README extract</summary>

Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary.
The zope.deferredimport package provided facilities for defining names
in modules that will be imported from somewhere else when used. You
can also cause deprecation warnings to be issued when a variable is
used. ...

Sections: `zope.deferredimport`, Changes, 6.1.1 (2026-02-16), 6.1 (2026-02-09), 6.0 (2025-09-12), 5.1 (2025-08-11), 5.0 (2023-06-29), 4.4 (2021-12-10), 4.3.1 (2019-08-05), 4.3 (2018-10-05), 4.2.1 (2017-10-24), 4.2.0 (2017-08-08), 4.1.0 (2014-12-26), 4.0.0 (2013-02-28)

</details>

### django-pipeline

Pipeline is an asset packaging library for Django.

`pip install django-pipeline` · installs (wheel) · licence: MIT License · rank 7944 · last release 2025-09-13 · [PyPI](https://pypi.org/project/django-pipeline/) · [docs](https://django-pipeline.readthedocs.io/) · [source](https://github.com/jazzband/django-pipeline)

<details><summary>README extract</summary>

Pipeline is an asset packaging library for Django, providing both CSS and
JavaScript concatenation and compression, built-in JavaScript template support,
and optional data-URI image and font embedding.

Example:
```python
# The folowing config merges CSS files(main.css, normalize.css)
# and JavaScript files(app.js, script.js) and compress them using
# `yuglify` into `css/styles.css` and `js/main.js`
# NOTE: Pipeline only works when DEBUG is False
PIPELINE = {
    'STYLESHEETS': {
        'css_files': {
            'source_filenames': (
...
```

Sections: Pipeline, Quickstart, Documentation, Issues

</details>

### http-sfv

Parse and serialise HTTP Structured Field Values

`pip install http-sfv` · installs (wheel) · licence: MIT License · rank 7954 · last release 2024-01-25 · [PyPI](https://pypi.org/project/http-sfv/)

<details><summary>README extract</summary>

See the http-sf package for a replacement. This package will only be updated for security issues, and may be yanked in the future.

This is a Python 3 library implementing parsing and serialisation of HTTP Structured Fields.

The library's initial purpose is to prove the algorithms in the specification; as a result, it is not at all optimised. ...

Sections: HTTP Structured Field Values in Python, This Package is DEPRECATED, Introduction, Python API, Command Line Use

</details>

### django-weasyprint

Django WeasyPrint integration

`pip install django-weasyprint` · installs (wheel) · licence: Apache Software License · rank 7982 · last release 2026-10-01 · [PyPI](https://pypi.org/project/django-weasyprint/) · [source](https://github.com/fdemmer/django-weasyprint)

<details><summary>README extract</summary>

A [Django] [WeasyPrint] integration providing class-based view and response
class for generating PDF from templates.

Example:
```python
# views.py
import functools

from django.conf import settings
from django.views.generic import DetailView

from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import WeasyTemplateResponse
from django_weasyprint.utils import DjangoURLFetcher

class MyDetailView(DetailView):
    # vanilla Django DetailView
...
```

Sections: Django-WeasyPrint, Usage, Example, Settings, Links

</details>

### fastapi-utilities

Reusable utilities for FastAPI

`pip install fastapi-utilities` · installs (wheel) · licence: MIT License · rank 8013 · last release 2025-03-25 · [PyPI](https://pypi.org/project/fastapi-utilities/)

<details><summary>README extract</summary>

🎨⚡️🔥 Reusable Utilities for FastAPI

Features:
- Repeat At / Every for scheduling cron jobs
- TTL LRU Cache
- Timing Middleware that logs you the time taken by a request
- Session Middleware
- CLI tool to generate skeleton

Source Code:
Youtube Link: Click Here

_Inspired From: dmontagu/fastapi-utils

Features:
This package includes a number of utilities to help reduce boilerplate and reuse common functionality across projects:

- 🕒Repeated Tasks: Easily trigger periodic tasks on server startup using repeat_every. ...

Example:
```python
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi_utilities import repeat_every, repeat_at

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- startup ---
    await test()
    test2()
    yield
...

</details>

### zttp

A sans-IO HTTP/1.1, HTTP/2, and HTTP/3 parser for Python with a Zig core.

`pip install zttp` · installs (wheel) · licence: BSD-3-Clause · rank 8023 · last release 2026-10-25 · [PyPI](https://pypi.org/project/zttp/) · [source](https://github.com/Kludex/zttp)

<details><summary>README extract</summary>

A sans-IO HTTP parser for Python with a Zig core! ⚡

Documentation:

Source Code:

> [!WARNING]
> zttp is experimental. The API and behaviour may change at any time, and it is not yet ready for production use.

zttp is a sans-IO HTTP parser whose engine is
written in Zig. ...

Features:
- SIMD-accelerated line and field scans with comptime-built character tables.
- Headers stay in a compact `HeaderBlock` until you access their Python values. ...

Example:
```python
import zttp

conn = zttp.Connection(zttp.SERVER)
request = conn.receive_event(b"GET /path?q=1 HTTP/1.1\r\nHost: example.com\r\n\r\n")
request.end_stream           # True: this bodyless request is already complete
conn.next_event()   # NEED_DATA

# Build a response:
conn.send_response(200, [(b"Content-Length", b"5")])
...

</details>

### django-rest-swagger

Swagger UI for Django REST Framework 3.5+

`pip install django-rest-swagger` · installs (wheel) · licence: BSD License · rank 8057 · last release 2018-04-30 · [PyPI](https://pypi.org/project/django-rest-swagger/)

<details><summary>README extract</summary>

Django REST Swagger

An API documentation generator for Swagger UI and Django REST Framework.

Installation
From pip:

pip install django-rest-swagger

Project @
Docs @

</details>

### pubnub

PubNub Real-time push service in the cloud

`pip install pubnub` · installs from source (sdist only) · licence: Other/Proprietary License · rank 8060 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pubnub/) · [docs](https://www.pubnub.com/docs/sdks/python) · [source](https://github.com/pubnub/python)

### django-ckeditor-5

CKEditor 5 for Django.

`pip install django-ckeditor-5` · installs (wheel) · licence: BSD License · rank 8077 · last release 2026-02-21 · [PyPI](https://pypi.org/project/django-ckeditor-5/) · [source](https://github.com/hvlads/django-ckeditor-5)

<details><summary>README extract</summary>

CKEditor 5 for Django >= 2.0

Sections: /Django CKEditor 5, Quick start, Examples, Example of using a widget in a form, Example of using a widget in a template, Custom storage example, Changing the language, Creating a CKEditor5 instance from javascript, Using JS callbacks in the config, Allow file uploading as link, Automatic image cleanup, Restrict upload file size

</details>

### WTForms-JSON

Adds smart json support for WTForms. Useful for when using WTForms with RESTful APIs.

`pip install WTForms-JSON` · installs from source (sdist only) · licence: BSD License · rank 8129 · last release 2022-04-16 · [PyPI](https://pypi.org/project/WTForms-JSON/)

<details><summary>README extract</summary>

WTForms-JSON

Adds smart json support for WTForms. Useful for when using WTForms with RESTful
APIs.

</details>

### starlette-admin

Fast, beautiful and extensible administrative interface framework for FastAPI & Starlette applications

`pip install starlette-admin` · installs (wheel) · licence: MIT · rank 8137 · last release 2026-10-24 · [PyPI](https://pypi.org/project/starlette-admin/) · [docs](https://jowilf.github.io/starlette-admin) · [source](https://github.com/jowilf/starlette-admin)

<details><summary>README extract</summary>

*An extensible administrative interface framework for FastAPI and Starlette applications.*

Features:
- Generated CRUD pages for your models
- Pagination, sorting, search, and shareable URLs
- Nested AND/OR filter builder
- Inline editing for related models
- Bulk actions and custom row actions
- CSV, Excel, JSON, and PDF export ...

Example:
```python
from contextlib import asynccontextmanager
from datetime import datetime, timezone

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from starlette_admin.contrib.sqla import Admin, ModelView

...
```

Sections: starlette-admin, Quickstart, Features, Documentation & Resources, Live Demo

</details>

### Beaker

A Session and Caching library with WSGI Middleware

`pip install Beaker` · installs (wheel) · licence: BSD License · rank 8246 · last release 2026-05-30 · [PyPI](https://pypi.org/project/Beaker/) · [docs](https://beaker.readthedocs.io/)

<details><summary>README extract</summary>

Beaker is a web session and general caching library that includes WSGI
middleware for use in web applications.

As a general caching library, Beaker can handle storing for various times
any Python object that can be pickled with optional back-ends on a
fine-grained basis. ...

Features:
* Fast, robust performance
* Multiple reader/single writer lock system to avoid duplicate simultaneous
 cache creation
* Cache back-ends include dbm, file, memory, memcached, Redis, MongoDB, and
 database (Using SQLAlchemy for multiple-db vendor ...

Sections: Cache and Session Library, About, Features, Documentation, Source

</details>

### djangorestframework-jsonapi

A Django REST framework API adapter for the JSON:API spec.

`pip install djangorestframework-jsonapi` · installs (wheel) · licence: BSD License · rank 8250 · last release 2026-10-27 · [PyPI](https://pypi.org/project/djangorestframework-jsonapi/) · [docs](https://django-rest-framework-json-api.readthedocs.org/) · [source](https://github.com/django-json-api/django-rest-framework-json-api)

<details><summary>README extract</summary>

Features:
JSON:API support for Django REST framework

By default, Django REST framework will produce a response like:

However, for an `identity` model in JSON:API format the response should look
like the following:

Sections: JSON:API and Django REST framework, Overview, Goals, Requirements, Running the example app, Usage, Settings

</details>

### django-guid

Middleware that enables single request-response cycle tracing by injecting a unique ID into project logs

`pip install django-guid` · installs (wheel) · licence: BSD License; MIT License · rank 8275 · last release 2026-05-05 · [PyPI](https://pypi.org/project/django-guid/) · [docs](https://django-guid.readthedocs.io/en/latest) · [source](https://github.com/snok/django-guid)

<details><summary>README extract</summary>

Django GUID attaches a unique correlation ID/request ID to all your log outputs for every request.
In other words, all logs connected to a request now has a unique ID attached to it, making debugging simple.

Which version of Django GUID you should use depends on your Django version and whether you run `ASGI` or `WSGI` servers. ...

Sections: Django GUID, Settings, Configuration, 2. Middleware, 3. Logging Configuration, 4. Django GUID Logger (Optional)

</details>

### webassets

Media asset management for Python, with glue code for various web frameworks

`pip install webassets` · installs (wheel) · licence: BSD License · rank 8276 · last release 2025-08-17 · [PyPI](https://pypi.org/project/webassets/)

<details><summary>README extract</summary>

Asset management application for Python web development - use it to
merge and compress your JavaScript and CSS files.

Documentation:

 Since releases aren't exactly happening on a regular schedule, you are
 encouraged to use the latest code. ...

</details>

### django-tasks-db

An ORM-based backend for Django Tasks

`pip install django-tasks-db` · installs (wheel) · licence: BSD-3-Clause · rank 8289 · last release 2026-08-28 · [PyPI](https://pypi.org/project/django-tasks-db/) · [source](https://github.com/RealOrangeOne/django-tasks-db)

<details><summary>README extract</summary>

A Django Tasks backend which uses Django's ORM to store tasks in the database.

Sections: Django Tasks DB, Usage, Worker, Pruning old tasks, Customizing the task id

</details>

### ultimate-sitemap-parser

A performant library for parsing and crawling sitemaps

`pip install ultimate-sitemap-parser` · installs (wheel) · licence: GPL-3.0-or-later · rank 8322 · last release 2026-06-16 · [PyPI](https://pypi.org/project/ultimate-sitemap-parser/) · [docs](https://ultimate-sitemap-parser.readthedocs.io/) · [source](https://github.com/GateNLP/ultimate-sitemap-parser)

_README extract left out: share-alike licence._

### pyodata

Enterprise ready Python OData client

`pip install pyodata` · installs (wheel) · licence: Apache Software License · rank 8369 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pyodata/)

<details><summary>README extract</summary>

Python OData client which provides comfortable Python agnostic
way for communication with OData services.

The goal of this Python module is to hide all OData protocol implementation
details.

Example:
```python
import requests
import pyodata

SERVICE_URL = '

# Create instance of OData client
client = pyodata.Client(SERVICE_URL, requests.Session())
```

Sections: Python OData Client - pyodata, Requirements, Configuration, Limitations, Known Issues, Usage

</details>

### hstspreload

Chromium HSTS Preload list as a Python package

`pip install hstspreload` · installs (wheel) · licence: BSD License · rank 8443 · last release 2025-01-01 · [PyPI](https://pypi.org/project/hstspreload/)

<details><summary>README extract</summary>

Chromium HSTS Preload list as a Python package.

Install via `python -m pip install hstspreload`

See for more information regarding the list itself.

The package provides a single function: `in_hsts_preload()` which takes an
IDNA-encoded host and returns either `True` or `False` regarding whether
that host should be only accessed via HTTPS.

Sections: hstspreload, API

</details>

### zope.dottedname

Resolver for Python dotted names.

`pip install zope.dottedname` · installs (wheel) · licence: ZPL-2.1 · rank 8464 · last release 2026-03-02 · [PyPI](https://pypi.org/project/zope.dottedname/) · [docs](https://zopedottedname.readthedocs.io/) · [source](https://github.com/zopefoundation/zope.dottedname)

<details><summary>README extract</summary>

Resolve strings containing dotted names into the appropriate Python object.

- Read documentation

- Move package metadata from setup.py to pyproject.toml.

- Add support for Python 3.14.

- Drop support for Python 3.9.

Sections: `zope.dottedname`, Changes, 7.1 (2026-03-02), 7.0 (2025-09-12), 6.1 (2025-08-11), 6.0 (2023-03-27), 5.0 (2022-09-08), 4.3 (2018-10-05), 4.2 (2017-05-11), 4.1.0 (2014-12-26), 4.0.0 (2013-02-05), 3.4.6 (2009-09-15), 3.4.5 (2009-01-27), 3.4.4 (2009-01-27)

</details>

### django-push-notifications

Send push notifications to mobile devices through GCM, APNS or WNS and to WebPush (Chrome, Firefox and Opera) in Django

`pip install django-push-notifications` · installs (wheel) · licence: MIT License · rank 8486 · last release 2025-11-16 · [PyPI](https://pypi.org/project/django-push-notifications/)

<details><summary>README extract</summary>

A minimal Django app that implements Device models that can send messages through APNS, FCM/GCM, WNS and WebPush.

The app implements four models: `GCMDevice`, `APNSDevice`, `WNSDevice` and `WebPushDevice`. Those models share the same attributes:
 - `name` (optional): A name for the device. ...

Example:
```python
INSTALLED_APPS = (
    ...
    "push_notifications"
)

# Import the firebase service
from firebase_admin import auth

# Initialize the default app (either use `GOOGLE_APPLICATION_CREDENTIALS` environment variable, or pass a firebase_admin.credentials.Certificate instance)
...
```

...

</details>

### quart-schema

A Quart extension to provide schema validation

`pip install quart-schema` · installs (wheel) · licence: MIT License · rank 8512 · last release 2026-08-31 · [PyPI](https://pypi.org/project/quart-schema/)

<details><summary>README extract</summary>

Quart-Schema is a Quart extension that provides schema validation and
auto-generated API documentation. This is particularly useful when
writing RESTful APIs.

Quart-Schema can use either msgspec or pydantic to validate.

Example:
```python
from dataclasses import dataclass
from datetime import datetime

from quart import Quart, websocket
from quart_schema import QuartSchema, validate_request, validate_response

app = Quart(name)
QuartSchema(app)

@dataclass
class Todo:
    task: str
    due: datetime | None

@app.post("/")
@validate_request(Todo)
@validate_response(Todo, 201)
...
```

Sections: Quart-Schema, Quickstart, Help

</details>

### APIFlask

A lightweight web API framework based on Flask.

`pip install APIFlask` · installs (wheel) · licence: MIT License · rank 8529 · last release 2026-11-02 · [PyPI](https://pypi.org/project/APIFlask/) · [docs](https://apiflask.com/docs) · [source](https://github.com/apiflask/apiflask)

<details><summary>README extract</summary>

APIFlask is a lightweight Python web API framework based on Flask. It's easy to use, highly customizable, ORM/ODM-agnostic, and 100% compatible with the Flask ecosystem.

APIFlask supports both marshmallow schemas and Pydantic models through a pluggable schema adapter system, giving you the flexibility to choose the validation approach that best ...

Example:
```python
from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf

app = APIFlask(name)

pets = [
    {'id': 0, 'name': 'Kitty', 'category': 'cat'},
    {'id': 1, 'name': 'Coco', 'category': 'dog'}
]

class PetIn(Schema):
    name = String(required=True, validate=Length(0, 10))
...
```

...

</details>

### jupyter-http-over-ws

Jupyter support for HTTP-over-ws

`pip install jupyter-http-over-ws` · installs (wheel) · licence: Apache Software License · rank 8531 · last release 2020-03-12 · [PyPI](https://pypi.org/project/jupyter-http-over-ws/)

### django-dotenv

foreman reads from .env. manage.py doesn't. Let's fix that.

`pip install django-dotenv` · installs (wheel) · licence: MIT License · rank 8534 · last release 2017-12-11 · [PyPI](https://pypi.org/project/django-dotenv/)

### scrapegraph-py

Official Python SDK for ScrapeGraph AI API

`pip install scrapegraph-py` · installs (wheel) · licence: MIT · rank 8556 · last release 2026-07-31 · [PyPI](https://pypi.org/project/scrapegraph-py/) · [docs](https://docs.scrapegraphai.com) · [source](https://github.com/ScrapeGraphAI/scrapegraph-py)

<details><summary>README extract</summary>

Official Python SDK for the ScrapeGraphAI API.

Example:
```python
from scrapegraph_py import ScrapeGraphAI

# reads SGAI_API_KEY from env, or pass explicitly: ScrapeGraphAI(api_key="...")
sgai = ScrapeGraphAI()

result = sgai.scrape("

if result.status == "success":
    print(result.data"results"["data"])
else:
    print(result.error)
```

Sections: ScrapeGraphAI Python SDK, Quick Start, 🆚 Open Source vs Managed API, API, scrape, extract, search, crawl, monitor, Async Client, Async Extract, Async Search, Async Crawl, Async Monitor

</details>

### zappa

Server-less Python Web Services for AWS Lambda and API Gateway

`pip install zappa` · installs (wheel) · licence: Apache Software License · rank 8568 · last release 2026-10-08 · [PyPI](https://pypi.org/project/zappa/)

<details><summary>README extract</summary>

- About
- Quick Reference
 - Minimal Configs
 - CLI Commands
 - Limitations and Constraints
- Installation and Configuration
 - Running the Initial Setup / Settings
 - Alternative: Generating Settings via CLI
 - Nested JSON Configurations ...

Example:
```python
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def homepage(request):
    return JSONResponse({"message": "Hello from Starlette!"})

app = Starlette(routes=[Route("/", homepage)])
```

...

</details>

### tableschema

A utility library for working with Table Schema in Python

`pip install tableschema` · installs (wheel) · licence: MIT License · rank 8605 · last release 2024-11-14 · [PyPI](https://pypi.org/project/tableschema/)

<details><summary>README extract</summary>

A Python implementation of the Table Schema standard.

> [Important Notice] We have released Frictionless Framework. This framework provides improved `tableschema` functionality extended to be a complete data solution. The change in not breaking for the existing software so no actions are required. ...

Features:
- `Table` to work with data tables described by Table Schema
- `Schema` representing Table Schema
- `Field` representing Table Schema field
- `validate` to validate Table Schema
- `infer` to infer Table Schema from data ...

Example:
```python
from tableschema import Table

# Create table
table = Table('path.csv', schema='schema.json')

# Print schema descriptor
print(table.schema.descriptor)

# Print cast rows in a dict form
for keyed_row in table.iter(keyed=True):
...

</details>

### pydap

A pure python implementation of the Data Access Protocol.

`pip install pydap` · installs (wheel) · licence: MIT License · rank 8613 · last release 2026-09-11 · [PyPI](https://pypi.org/project/pydap/)

<details><summary>README extract</summary>

What is pydap?

pydap is an open-source implementation of the OPeNDAP protocol, written from scratch in pure Python. You can use `pydap` to access scientific data available on the many OPeNDAP servers publicly-available through the internet. ...

Example:
```python
from pydap.client import open_url
pyds = open_url(' protocol='dap4')
pyds.tree()
```

Sections: pydap, Running pydap as a Server, Documentation

</details>

### abx-dl

All-in-one CLI tool to download and extract content from URLs

`pip install abx-dl` · installs (wheel) · licence: MIT License · rank 8637 · last release 2026-11-07 · [PyPI](https://pypi.org/project/abx-dl/) · [docs](https://abx-dl.archivebox.io/) · [source](https://github.com/ArchiveBox/abx-dl)

<details><summary>README extract</summary>

> A simple all-in-one CLI tool to auto-detect and download *everything* available from a URL.

✨ *Ever wish you could `yt-dlp`, `gallery-dl`, `wget`, `curl`, `puppeteer`, etc. all in one command?*

`abx-dl` is an all-in-one CLI tool for downloading URLs "by any means necessary". ...

Sections: ⬇️ `abx-dl`, 🍜 What does it save?, 🧩 How does it work?, ⚙️ Configuration, Docker, 🔠 Usage, Commands, Output Structure, All Outputs, Available Plugins, Snapshot / Extraction Plugins, AI Skill, Architecture, Related Projects

</details>

### device-detector

Python3 port of matomo's Device Detector

`pip install device-detector` · installs (wheel) · licence: not stated · rank 8706 · last release 2026-10-08 · [PyPI](https://pypi.org/project/device-detector/) · [source](https://github.com/thinkwelltwd/device_detector.git)

<details><summary>README extract</summary>

DeviceDetector is a precise and fast user agent parser and device detector written in Python, backed by the largest and most up-to-date user agent database.

DeviceDetector will parse any user agent and detect the browser, operating system, device used (desktop, tablet, mobile, tv, cars, console, etc.), brand and model. ...

Example:
```python
from device_detector import DeviceDetector

ua = 'Mozilla/5.0 (Linux; Android 4.3; C5502 Build/10.4.1.B.0.101) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.136 Mobile Safari/537.36'

# Parse UA string and load data to dict of 'os', 'client', 'device' keys
device = DeviceDetector(ua).parse()

...
```

...

</details>

### LinkChecker

check links in web documents or full websites

`pip install LinkChecker` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 8744 · last release 2025-07-28 · [PyPI](https://pypi.org/project/LinkChecker/) · [source](https://github.com/linkchecker/linkchecker)

_README extract left out: share-alike licence._

### django-clone

Create a clone of a django model instance.

`pip install django-clone` · installs (wheel) · licence: Apache Software License; MIT License · rank 8782 · last release 2025-06-10 · [PyPI](https://pypi.org/project/django-clone/)

<details><summary>README extract</summary>

| Python | Django | Downloads | Code Style |

| | | | |

| PyPI | Test | Vulnerabilities | Coverage | Code Quality | Pre-Commit |

| | | |
 | | |

Create copies of a model instance with explicit control on how the instance should be duplicated (limiting fields or related objects copied) with unique field detection. ...

Features:
* 100% test coverage.
* More control over how a model instance should be duplicated
* Multi Database support i.e Create duplicates on one or more databases.
* Restrict fields used for creating a duplicate instance. ...

...

</details>

### django-tree-queries

Tree queries with explicit opt-in, without configurability

`pip install django-tree-queries` · installs (wheel) · licence: BSD License · rank 8784 · last release 2026-10-23 · [PyPI](https://pypi.org/project/django-tree-queries/)

<details><summary>README extract</summary>

Query Django model trees using adjacency lists and recursive common
table expressions. Supports PostgreSQL, sqlite3 (3.8.3 or higher) and
MariaDB (10.2.2 or higher) and MySQL (8.0 or higher, if running without
`ONLY_FULL_GROUP_BY`).

Supports Django 4.2 or better, Python 3.10 or better. See the GitHub actions
build for more details.

Features:
- Supports only integer and UUID primary keys (for now).
- Allows specifying ordering among siblings.
- Uses the correct definition of depth, where root nodes have a depth of
 zero. ...

Example:
```python
# Basic usage, disregards the tree structure completely.
nodes = Node.objects.all()

# Fetch nodes in depth-first search order. All nodes will have the
# tree_path, tree_ordering and tree_depth attributes.
nodes = Node.objects.with_tree_fields()

...

</details>

### django-sass-processor

SASS processor to compile SCSS files into *.css, while rendering, or offline.

`pip install django-sass-processor` · installs (wheel) · licence: MIT License · rank 8822 · last release 2025-06-26 · [PyPI](https://pypi.org/project/django-sass-processor/)

<details><summary>README extract</summary>

Annoyed having to run a Compass, Grunt or Gulp daemon while developing Django projects?

Well, then this app is for you! Compile SASS/SCSS files on the fly without having to manage
third party services nor special IDE plugins. ...

Example:
```python
import os

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(PROJECT_PATH, 'extra-styles/scss'),
    os.path.join(PROJECT_PATH, 'node_modules'),
]
```

...

</details>

### Frozen-Flask

Freezes a Flask application into a set of static files.

`pip install Frozen-Flask` · installs (wheel) · licence: BSD License · rank 8830 · last release 2024-02-09 · [PyPI](https://pypi.org/project/Frozen-Flask/) · [docs](https://frozen-flask.readthedocs.io/) · [source](https://github.com/Frozen-Flask/Frozen-Flask/)

<details><summary>README extract</summary>

Freezes a Flask application into a set of static files. The result can be hosted
without any server-side software other than a traditional web server.

See documentation:

</details>

### google-oauth2-tool

Create OAuth2 key file from OAuth2 client id file

`pip install google-oauth2-tool` · installs (wheel) · licence: BSD License · rank 8836 · last release 2019-05-01 · [PyPI](https://pypi.org/project/google-oauth2-tool/)

<details><summary>README extract</summary>

Simple wrapper for oauth2client.tools module.

Sections: Create OAuth2 key file from OAuth2 client id file, PIP, Usage

</details>

### django-enum

Full and natural support for enumerations as Django model fields.

`pip install django-enum` · installs (wheel) · licence: MIT · rank 8861 · last release 2026-07-31 · [PyPI](https://pypi.org/project/django-enum/) · [docs](https://django-enum.readthedocs.io) · [source](https://github.com/django-commons/django-enum)

<details><summary>README extract</summary>

🚨 See migration guide for notes on 1.x to 2.x migration. 🚨

Full and natural support for PEP435 enumerations as Django model fields.

Many packages aim to ease usage of Python enumerations as model fields. Most were superseded when Django provided TextChoices and IntegerChoices types. The motivation for django-enum was to: ...

Example:
```python
from django.db import models
from django_enum import EnumField

class MyModel(models.Model):
    class TextEnum(models.TextChoices):
        VALUE0 = "V0", "Value 0"
        VALUE1 = "V1", "Value 1"
        VALUE2 = "V2", "Value 2"

    class IntEnum(models.IntegerChoices):
        ONE = 1, "One"
        TWO = (
            2,
            "Two",
...
```

Sections: django-enum, Complex Enumerations, Further Reading

</details>

### behave-django

Behave BDD integration for Django

`pip install behave-django` · installs (wheel) · licence: MIT · rank 8862 · last release 2026-06-04 · [PyPI](https://pypi.org/project/behave-django/) · [docs](https://behave-django.readthedocs.io/) · [source](https://github.com/behave/behave-django)

<details><summary>README extract</summary>

Behave BDD integration for Django

Features:
- Web browser automation ready
- Database transactions per scenario
- Use Django's test client
- Use unittest + Django assert library
- Use behave's command line arguments
- Use behave's configuration file
- Fixture loading
- Page objects

Sections: behave-django, Features, Documentation

</details>

### dj-inmemorystorage

A non-persistent in-memory data storage backend for Django.

`pip install dj-inmemorystorage` · installs (wheel) · licence: BSD License · rank 8863 · last release 2020-03-30 · [PyPI](https://pypi.org/project/dj-inmemorystorage/)

<details><summary>README extract</summary>

An in-memory data storage backend for Django.

Compatible with Django's storage
API.

Sections: dj-inmemorystorage, Usage, Differences

</details>

### django-markdownx

A comprehensive Markdown editor built for Django.

`pip install django-markdownx` · installs (wheel) · licence: BSD License · rank 8869 · last release 2026-05-23 · [PyPI](https://pypi.org/project/django-markdownx/)

<details><summary>README extract</summary>

Django MarkdownX is a comprehensive Markdown plugin built for Django, the renowned high-level Python web framework, with flexibility, extensibility, and ease-of-use at its core.

GitHub:

PyPi:

Features:
* Raw editing.
* Live preview.
* Drag & drop image uploads (automatically stored in the designated location in the *Media* directory).
* Customizable image insertion tag.
* Definition of maximum size for an image. ...

Sections: Django MarkdownX, Key features, Preview

</details>

### dataflows-tabulator

Consistent interface for stream reading and writing tabular data (csv/xls/json/etc)

`pip install dataflows-tabulator` · installs (wheel) · licence: MIT License · rank 8930 · last release 2024-03-24 · [PyPI](https://pypi.org/project/dataflows-tabulator/)

<details><summary>README extract</summary>

A library for reading and writing tabular data (csv/xls/json/etc).

> [Important Notice] This is a fork of the archived tabulator-py repository. The original repository is no longer maintained. This fork is maintained by Adam Kariv.

Features:
- Supports most common tabular formats: CSV, XLS, ODS, JSON, Google Sheets, SQL, and others. See complete list below.
- Loads local and remote data: Supports HTTP, FTP and S3. ...

Example:
```python
from tabulator import Stream

with Stream('data.csv', headers=1) as stream:
    stream.headers # [header1, header2, ..]
    for row in stream:
        print(row)  # [value1, value2, ..]
```

...

</details>

### python-openid

OpenID support for servers and consumers.

`pip install python-openid` · installs from source (sdist only) · licence: Apache Software License · rank 8937 · last release 2010-07-01 · [PyPI](https://pypi.org/project/python-openid/)

<details><summary>README extract</summary>

This is a set of Python packages to support use of
the OpenID decentralized identity system in your application. Want to enable
single sign-on for your web site? Use the openid.consumer package. Want to
run your own OpenID server? Check out openid.server. Includes example code
and support for a variety of storage back-ends.

</details>

### webapp2

Taking Google App Engine's webapp to the next level!

`pip install webapp2` · installs from source (sdist only) · licence: Apache Software License · rank 8987 · last release 2012-09-28 · [PyPI](https://pypi.org/project/webapp2/)

<details><summary>README extract</summary>

webapp2 is a lightweight Python web framework compatible with Google App
Engine's webapp.

webapp2 is simple. it follows the simplicity of webapp, but
improves it in some ways: it adds better URI routing and exception handling,
a full featured response object and a more flexible dispatching mechanism. ...

Sections: webapp2, Quick links

</details>

### crispy-tailwind

Tailwind CSS for Django Crispy Forms

`pip install crispy-tailwind` · installs (wheel) · licence: MIT License · rank 9034 · last release 2024-02-13 · [PyPI](https://pypi.org/project/crispy-tailwind/)

<details><summary>README extract</summary>

A Tailwind CSS template pack for the wonderful django-crispy-forms.

WARNING

This project is still in its early stages of development. Any contributions to
the package would be very welcomed.

Currently the template pack allows the use of the `|crispy` filter to style
your form. Here is an example image.

Example:
```python
class CustomTextWidget(forms.TextInput):
    pass

class CustomTextWidgetForm(forms.Form):
    name = forms.CharField(
        widget=CustomTextWidget(attrs={"class": "custom-css"})
    )
```

Sections: Crispy-Tailwind, How to use, Documentation, FAQs, What about custom widgets?

</details>

### intervals

Python tools for handling intervals (ranges of comparable objects).

`pip install intervals` · installs (wheel) · licence: BSD License · rank 9079 · last release 2021-07-02 · [PyPI](https://pypi.org/project/intervals/)

<details><summary>README extract</summary>

intervals

Python tools for handling intervals (ranges of comparable objects).

</details>

### Genshi

A toolkit for generation of output for the web

`pip install Genshi` · installs (wheel) · licence: BSD License · rank 9166 · last release 2026-10-26 · [PyPI](https://pypi.org/project/Genshi/)

<details><summary>README extract</summary>

Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or
other textual content for output generation on the web. The major
feature is a template language, which is heavily inspired by Kid.

</details>

### pychrome

A Python Package for the Google Chrome Dev Protocol

`pip install pychrome` · installs (wheel) · licence: BSD License · rank 9332 · last release 2023-07-10 · [PyPI](https://pypi.org/project/pychrome/)

<details><summary>README extract</summary>

A Python Package for the Google Chrome Dev Protocol, more document

Example:
```python
import pychrome

# create a browser instance
browser = pychrome.Browser(url="

# create a tab
tab = browser.new_tab()

# register callback if you want
def request_will_be_sent(**kwargs):
    print("loading: %s" % kwargs.get('request').get('url'))

tab.Network.requestWillBeSent = request_will_be_sent

# start the tab
tab.start()

# call method
...
```

Sections: pychrome, Setup Chrome, Getting Started, Debug, Tab management, Examples, Ref

</details>

### pySmartDL

A Smart Download Manager for Python

`pip install pySmartDL` · installs (wheel) · licence: Public Domain · rank 9338 · last release 2020-09-19 · [PyPI](https://pypi.org/project/pySmartDL/)

<details><summary>README extract</summary>

`pySmartDL` strives to be a full-fledged smart download manager for Python. Main features:

* Built-in download acceleration (with the multipart downloading technique).
* Mirrors support.
* Pause/Unpause feature.
* Speed limiting feature.
* Hash checking.
* Non-blocking, shows progress bar, download speed and eta. ...

Sections: Python Smart Download Manager -- pySmartDL, Project Links, Usage, Requirements

</details>

### eventregistry

A package that can be used to query information in Event Registry (https://eventregistry.org/)

`pip install eventregistry` · installs (wheel) · licence: MIT · rank 9441 · last release 2026-10-14 · [PyPI](https://pypi.org/project/eventregistry/) · [docs](https://github.com/EventRegistry/event-registry-python/wiki) · [source](https://github.com/EventRegistry/event-registry-python)

<details><summary>README extract</summary>

`eventregistry` is a Python package for accessing the news data available in Event Registry through its API. It can be used to search for articles or events using a large set of filters, like keywords, concepts, categories, sources, sentiment, date, etc., to follow the feed of new content and to compute summaries (top sources, concepts, sentiment, ...

Example:
```python
from eventregistry import *
er = EventRegistry(apiKey = YOUR_API_KEY)

# get the USA URI
usUri = er.getLocationUri("USA")    # =

q = QueryArticlesIter(
    keywords = QueryItems.OR(["George Clooney", "Sandra Bullock"]),
    minSentiment = 0.4,
    sourceLocationUri = usUri,
    dataType = ["news", "blog"])

...
```

...

</details>

### PyLTI1p3

LTI 1.3 Advantage Tool implementation in Python

`pip install PyLTI1p3` · installs (wheel) · licence: MIT License · rank 9481 · last release 2022-11-20 · [PyPI](https://pypi.org/project/PyLTI1p3/)

<details><summary>README extract</summary>

This project is a Python implementation of the similar PHP tool.
This library contains adapters for use with the Django and Flask web frameworks. However, there are no difficulties with adapting it to other frameworks; you just need to re-implement the `OIDCLogin` and `MessageLaunch` classes as it is already done in existing adapters.

Example:
```python
from pylti1p3.tool_config import ToolConfJsonFile
tool_conf = ToolConfJsonFile('path/to/json')

from pylti1p3.tool_config import ToolConfDict
settings = {
    "<issuer_1>": { },  # one issuer ~ one client-id (outdated and not recommended)
    "<issuer_2>": [{ }, { }]  # one issuer ~ many client-ids (recommended method)
}
private_key = '...'
...
```

...

</details>

### aiohttp-session

sessions for aiohttp.web

`pip install aiohttp-session` · installs (wheel) · licence: Apache Software License · rank 9498 · last release 2024-09-25 · [PyPI](https://pypi.org/project/aiohttp-session/)

<details><summary>README extract</summary>

The library provides sessions for aiohttp.web.

__ aiohttp_web

Example:
```python
import time
from cryptography import fernet
from aiohttp import web
from aiohttp_session import setup, get_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage

async def handler(request):
    session = await get_session(request)
    last_visit = session['last_visit'] if 'last_visit' in session else None
...
```

Sections: aiohttp_session, Usage, Third party extensions, 2.12.1 (2024-09-25), 2.12.0 (2022-10-28), 2.11.0 (2021-01-31), 2.10.0 (2021-12-30), 2.9.0 (2019-11-04), 2.8.0 (2019-09-17), 2.7.0 (2018-10-13), 2.6.0 (2018-09-12), 2.5.0 (2018-05-12), 2.4.0 (2018-05-04), 2.3.0 (2018-02-13)

</details>

### django-esi

Django app for accessing the EVE Stable Interface (ESI).

`pip install django-esi` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 9503 · last release 2026-10-30 · [PyPI](https://pypi.org/project/django-esi/) · [docs](https://django-esi.readthedocs.io/en/latest/) · [source](https://gitlab.com/allianceauth/django-esi)

_README extract left out: share-alike licence._

### allianceauth

An auth system for EVE Online to help in-game organizations

`pip install allianceauth` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 9577 · last release 2026-10-29 · [PyPI](https://pypi.org/project/allianceauth/) · [docs](https://allianceauth.readthedocs.io/) · [source](https://gitlab.com/allianceauth/allianceauth)

_README extract left out: share-alike licence._

### WTForms-SQLAlchemy

SQLAlchemy tools for WTForms

`pip install WTForms-SQLAlchemy` · installs (wheel) · licence: BSD License · rank 9588 · last release 2024-10-25 · [PyPI](https://pypi.org/project/WTForms-SQLAlchemy/) · [docs](https://wtforms-sqlalchemy.readthedocs.io/) · [source](https://github.com/pallets-eco/wtforms-sqlalchemy/)

<details><summary>README extract</summary>

WTForms-SQLAlchemy is a fork of the `wtforms.ext.sqlalchemy` package from WTForms.
The package has been renamed to `wtforms_sqlalchemy` but otherwise should
function the same as `wtforms.ext.sqlalchemy` did.

to install:
An example using Flask is included in `examples/flask`.

Features:
1. Provide `SelectField` integration with SQLAlchemy models

 - `wtforms_sqlalchemy.fields.QuerySelectField`
 - `wtforms_sqlalchemy.fields.QuerySelectMultipleField`

2. Generate forms from SQLAlchemy models using
 `wtforms_sqlalchemy.orm.model_form`

Sections: WTForms-SQLAlchemy, Features, Rationale

</details>

### django-parler

Simple Django model translations without nasty hacks, featuring nice admin integration.

`pip install django-parler` · installs (wheel) · licence: Apache Software License · rank 9608 · last release 2026-05-14 · [PyPI](https://pypi.org/project/django-parler/)

<details><summary>README extract</summary>

Simple Django model translations without nasty hacks.

Features:

* Nice admin integration.
* Access translated attributes like regular attributes.
* Automatic fallback to the default language.
* Separate table for translated fields, compatible with django-hvad.
* Plays nice with others, compatible with django-polymorphic, django-mptt and such: ...

Example:
```python
from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class MyModel(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Title"), max_length=200)
    )

    def unicode(self):
        return self.title
```

...

</details>

### django-simple-captcha

A very simple, yet powerful, Django captcha application

`pip install django-simple-captcha` · installs (wheel) · licence: MIT License · rank 9677 · last release 2026-07-30 · [PyPI](https://pypi.org/project/django-simple-captcha/)

<details><summary>README extract</summary>

Django Simple Captcha is an extremely simple, yet highly customizable Django application to add captcha images to any Django form.

Features:
* Very simple to setup and deploy, yet very configurable
* Can use custom challenges (e.g. random chars, simple math, dictionary word, ...)
* Custom generators, noise and filter functions alter the look of the generated image
* Supports ...

Sections: Django Simple Captcha, Features, Requirements, Documentation

</details>

### spider-browser

Browser automation client for Spider's pre-warmed browser fleet with smart retry and browser switching

`pip install spider-browser` · installs (wheel) · licence: MIT · rank 9701 · last release 2026-07-19 · [PyPI](https://pypi.org/project/spider-browser/) · [docs](https://spider.cloud/docs) · [source](https://github.com/spider-rs/spider-browser)

### airspeed-ext

Airspeed is a powerful and easy-to-use templating engine for Python that aims for a high level of compatibility with Velocity templates in AWS cloud services.

`pip install airspeed-ext` · installs from source (sdist only) · licence: BSD License · rank 9799 · last release 2025-05-30 · [PyPI](https://pypi.org/project/airspeed-ext/)

### django-typer

Use Typer to define the CLI for your Django management commands.

`pip install django-typer` · installs (wheel) · licence: MIT · rank 9821 · last release 2026-09-30 · [PyPI](https://pypi.org/project/django-typer/) · [docs](https://django-typer.readthedocs.io) · [source](https://github.com/django-commons/django-typer)

<details><summary>README extract</summary>

Use static typing to define the CLI for your Django management commands with Typer. Optionally use the provided TyperCommand class that inherits from BaseCommand. This class maps the Typer interface onto a class based interface that Django developers will be familiar with. ...

Example:
```python
from django_typer.management import TyperCommand

class Command(TyperCommand):
    def handle(self, arg1: str, arg2: str, arg3: float = 0.5, arg4: int = 1):
        """
        A basic command that uses Typer
        """
```

Sections: django-typer, 🚨 Upgrade Notice, Basic Example, Multiple Subcommands Example, Grouping and Hierarchies Example

</details>

### python-documentcloud

A simple Python wrapper for the DocumentCloud API

`pip install python-documentcloud` · installs (wheel) · licence: MIT License · rank 9825 · last release 2026-06-29 · [PyPI](https://pypi.org/project/python-documentcloud/)

<details><summary>README extract</summary>

<pre><code> __ _ __ _ _
 | _ \ _ _ _ _ _ _ _ _ | |_ / _| | _ _ _ __| |
 | | | |/ _ \ / | | | | '_ ` _ \ / _ \ '_ \| | | | |/ _ \| | | |/ _` |
 | |_| | (_) | (| |_| | | | | | | / | | | |_| |___| | (_) | |_| | (_| |
 |__/ \_/ \_|\,_|_| |_| |_|\_|_| |_|\|\__|_|\_/ \,_|\,_|/ </code></pre>

A simple python wrapper for the DocumentCloud API

Features:
- Retrieve and edit documents and projects, both public and private, from documentcloud.org
- Upload PDFs into your documentcloud.org account and organize them into projects
- Download text and images extracted from your PDFs by DocumentCloud

Sections: Features, Getting started

</details>

### aiohttp-basicauth

Proxy connector for aiohttp

`pip install aiohttp-basicauth` · installs (wheel) · licence: Apache Software License · rank 9830 · last release 2026-06-05 · [PyPI](https://pypi.org/project/aiohttp-basicauth/) · [source](https://github.com/romis2012/aiohttp-basicauth)

<details><summary>README extract</summary>

HTTP basic authentication middleware for aiohttp.
Inspired by Flask-BasicAuth.

- Python >= 3.8
- aiohttp >= 3.10

Example:
```python
from aiohttp import web
from aiohttp_basicauth import BasicAuthMiddleware

auth = BasicAuthMiddleware(username='user', password='password')
app = web.Application(middlewares=[auth])

web.run_app(app, host='127.0.0.1', port=80)
```

Sections: aiohttp-basicauth, Requirements, Simple usage, Protect specific view(s), Advanced usage

</details>

### djangorestframework-datatables

Seamless integration between Django REST framework and Datatables (https://datatables.net)

`pip install djangorestframework-datatables` · installs (wheel) · licence: MIT License · rank 9845 · last release 2024-06-14 · [PyPI](https://pypi.org/project/djangorestframework-datatables/)

<details><summary>README extract</summary>

Features:
This package provides seamless integration between Django REST framework and Datatables.

Install django-rest-framework-datatables, call your API with `?format=datatables` and it will return a JSON structure that is fully compatible with what ...

Example:
```python
class ArtistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Artist
        fields = (
            'id', 'name',
        )
        datatables_always_serialize = ('id',)
```

...

</details>

### streamlink

Streamlink is a command-line utility that extracts streams from various services and pipes them into a video player of choice.

`pip install streamlink` · installs (wheel) · licence: BSD-2-Clause · rank 9894 · last release 2026-10-29 · [PyPI](https://pypi.org/project/streamlink/) · [docs](https://streamlink.github.io/) · [source](https://github.com/streamlink/streamlink)

<details><summary>README extract</summary>

A Python library and command-line interface which pipes streams from various services into a video player.

 Avoid resource-heavy and unoptimized websites, and still enjoy streamed content.

 Streamlink was forked in 2016 from the abandoned Livestreamer project.

Sections: Streamlink, 👍 Features, 💡 Quickstart

</details>

### djangorestframework-recursive

Recursive Serialization for Django REST framework

`pip install djangorestframework-recursive` · installs (wheel) · licence: BSD License · rank 9924 · last release 2017-07-04 · [PyPI](https://pypi.org/project/djangorestframework-recursive/)

### backoff-utils

Python functions and decorators for various backoff/retry strategies

`pip install backoff-utils` · installs (wheel) · licence: MIT License · rank 9958 · last release 2020-07-11 · [PyPI](https://pypi.org/project/backoff-utils/) · [docs](http://backoff-utils.readthedocs.io/en/) · [source](https://github.com/insightindustry/backoff-utils/)

<details><summary>README extract</summary>

Python Library for Backoff/Retry Strategies

Backoff-Utils is a Python library that provides Python functions and decorators
that apply various backoff / retry strategies to your Python function and method
calls.

The library has a consistent syntax for easy use, and has been tested on
Python 2.7, 3.4, 3.5, 3.6, 3.7 and 3.8. ...

Features:
Often, when making external API calls to third-party systems, something goes
wrong. The internet might glitch. The API we're calling might timeout. Gremlins
might eat your packets. ...

Example:
```python
from backoff_utils import strategies

# Using a Function Call
from backoff_utils import backoff

def some_function(arg1, arg2, kwarg1 = None):
    # your code goes here
    pass

result = backoff(some_function,
...

</details>

### arcgis

ArcGIS API for Python

`pip install arcgis` · installs (wheel) · licence: LicenseRef-Esri-MLA · rank 10035 · last release 2026-10-20 · [PyPI](https://pypi.org/project/arcgis/)

<details><summary>README extract</summary>

Work with maps and geospatial data in Python using The ArcGIS API for Python.

Use simple and efficient tools powered by Web GIS, for sophisticated vector and raster analysis, geocoding, map making, routing and directions. Administer, organize and manage users, groups and information items in your GIS. ...

</details>

### Flask-PyMongo

PyMongo support for Flask applications

`pip install Flask-PyMongo` · installs (wheel) · licence: BSD License · rank 10036 · last release 2025-01-29 · [PyPI](https://pypi.org/project/Flask-PyMongo/)

<details><summary>README extract</summary>

PyMongo support for Flask applications. Requires `flask>=3.0` and `pymongo>=4.0`

Example:
```python
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(name)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html", online_users=online_users)
```

Sections: Flask-PyMongo, Quickstart, More Info

</details>

### infinity

All-in-one infinity value for Python. Can be compared to any object.

`pip install infinity` · installs from source (sdist only) · licence: BSD License · rank 10039 · last release 2020-06-03 · [PyPI](https://pypi.org/project/infinity/)

<details><summary>README extract</summary>

infinity

All-in-one infinity value for Python. Can be compared to any object.

</details>

### fhirpy

FHIR client for python

`pip install fhirpy` · installs (wheel) · licence: not stated · rank 10046 · last release 2026-10-27 · [PyPI](https://pypi.org/project/fhirpy/) · [docs](https://github.com/beda-software/fhir-py#readme) · [source](https://github.com/beda-software/fhir-py.git)

<details><summary>README extract</summary>

async/sync FHIR client for python3.
This package provides an API for CRUD operations over FHIR resources

You can test this library by interactive FHIR course in the repository Aidbox/jupyter-course. ...

Example:
```python
import asyncio
from fhirpy import AsyncFHIRClient

async def main():
    # Create an instance
    client = AsyncFHIRClient(
        '
        authorization='Bearer TOKEN',
    )

    # Search for patients
    resources = client.resources('Patient')  # Return lazy search set
    resources = resources.search(name='John').limit(10).sort('name')
...
```

...

</details>

### drf-excel

Django REST Framework renderer for Excel spreadsheet (xlsx) files.

`pip install drf-excel` · installs (wheel) · licence: BSD-3-Clause · rank 10049 · last release 2026-08-06 · [PyPI](https://pypi.org/project/drf-excel/) · [docs](https://github.com/django-commons/drf-excel/) · [source](https://github.com/django-commons/drf-excel/)

<details><summary>README extract</summary>

`drf-excel` provides an Excel spreadsheet (xlsx) renderer for Django REST Framework. It uses OpenPyXL to create the spreadsheet and provide the file to the end user.

We aim to support Django's currently supported versions, as well as:

* Django REST Framework >= 3.14
* OpenPyXL >= 2.4

Example:
```python
class MyExampleViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = MyExampleModel.objects.all()
    serializer_class = MyExampleSerializer
    renderer_classes = (XLSXRenderer,)

    column_header = {
        'titles': [
            "Column_1_name",
            "Column_2_name",
            "Column_3_name",
        ],
...
```

...

</details>

### Flask-Assets

Asset management for Flask, to compress and merge CSS and Javascript files.

`pip install Flask-Assets` · installs (wheel) · licence: BSD License · rank 10062 · last release 2023-10-22 · [PyPI](https://pypi.org/project/Flask-Assets/)

<details><summary>README extract</summary>

Flask-Assets

Integrates the ``webassets`` library with Flask, adding support for
merging, minifying and compiling CSS and Javascript files.

</details>

### fastapi-csrf-protect

Stateless implementation of Cross-Site Request Forgery (XSRF) Protection by using Double Submit Cookie mitigation pattern

`pip install fastapi-csrf-protect` · installs (wheel) · licence: MIT · rank 10114 · last release 2025-09-16 · [PyPI](https://pypi.org/project/fastapi-csrf-protect/)

<details><summary>README extract</summary>

Features:
FastAPI extension that provides stateless Cross-Site Request Forgery (XSRF) Protection support.
Aimed to be easy to use and lightweight, we adopt Double Submit Cookie mitigation pattern. ...

Example:
```python
from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError
from pydantic_settings import BaseSettings

app = FastAPI()
...
```

...

</details>

### httpx-socks

Proxy (HTTP, SOCKS) transports for httpx

`pip install httpx-socks` · installs (wheel) · licence: Apache-2.0 · rank 10125 · last release 2026-08-14 · [PyPI](https://pypi.org/project/httpx-socks/) · [source](https://github.com/romis2012/httpx-socks)

<details><summary>README extract</summary>

<!--


The `httpx-socks` package provides proxy transports for httpx client.
SOCKS4(a), SOCKS5(h), HTTP CONNECT proxy supported.
It uses python-socks for core proxy functionality.

- Python >= 3.9
- httpx>=0.28.0,<0.29.0
- python-socks>=2.4.3,<3.0.0
- trio>=0.30 (optional)
- anyio>=4.12,<5.0.0 (optional)

Example:
```python
import httpx
from httpx_socks import SyncProxyTransport

def fetch(url):
    transport = SyncProxyTransport.from_url('socks5://user:password@127.0.0.1:1080')
    with httpx.Client(transport=transport) as client:
        res = client.get(url)
        return res.text
```

Sections: httpx-socks, Requirements, Usage, sync transport, async transport (asyncio, trio)

</details>

### user-agent

Library to build content for User-Agent HTTP header

`pip install user-agent` · installs (wheel) · licence: MIT License · rank 10182 · last release 2025-09-10 · [PyPI](https://pypi.org/project/user-agent/)

<details><summary>README extract</summary>

This module is for generating random, valid web user agents:

* content of "User-Agent" HTTP headers
* content of `window.navigator` JavaScript object

Example:
```python
>>> from user_agent import generate_user_agent, generate_navigator
>>> from pprint import pprint
>>> generate_user_agent()
'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Win64; x64)'
>>> generate_user_agent(os=('mac', 'linux'))
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:36.0) Gecko/20100101 Firefox/36.0'
>>> pprint(generate_navigator())
...
```

Sections: Documentation for user_agent package, What is user_agent module for?, Usage Example, Command Line Usage, Documentation

</details>

### spyne

A transport and architecture agnostic rpc library that focuses on exposing public services with a well-defined API.

`pip install spyne` · installs from source (sdist only) · licence: LGPL-2.1 · rank 10237 · last release 2022-02-03 · [PyPI](https://pypi.org/project/spyne/)

_README extract left out: share-alike licence._

### Bootstrap-Flask

Bootstrap 4 & 5 helper for your Flask projects.

`pip install Bootstrap-Flask` · installs (wheel) · licence: MIT · rank 10288 · last release 2026-08-23 · [PyPI](https://pypi.org/project/Bootstrap-Flask/) · [docs](https://bootstrap-flask.readthedocs.io/en/stable/) · [source](https://github.com/helloflask/bootstrap-flask/)

<details><summary>README extract</summary>

Bootstrap-Flask is a collection of Jinja macros for Bootstrap 4 & 5 and Flask. It helps you to
render Flask-related data and objects to Bootstrap markup HTML more easily:

- Render Flask-WTF/WTForms form object to Bootstrap Form.
- Render data objects (dict or class objects) to Bootstrap Table. ...

Example:
```python
from flask import Flask
# To follow the naming rule of Flask extension, although
# this project's name is Bootstrap-Flask, the actual package
# installed is named `flask_bootstrap`.
from flask_bootstrap import Bootstrap5

app = Flask(name)
bootstrap = Bootstrap5(app)
```

Sections: Bootstrap-Flask, Example, Live demo, Links, Migration from Flask-Bootstrap

</details>

### flask-paginate

Simple paginate support for flask

`pip install flask-paginate` · installs (wheel) · licence: BSD License · rank 10290 · last release 2026-10-22 · [PyPI](https://pypi.org/project/flask-paginate/)

<details><summary>README extract</summary>

flask-paginate

Simple paginate for flask (study from will_paginate).
Use bootstrap css framework, supports bootstrap2&3 and foundation

</details>

### django-cloudinary-storage

Django package that provides Cloudinary storages for both media and static files as well as management commands for removing unnecessary files.

`pip install django-cloudinary-storage` · installs (wheel) · licence: MIT · rank 10293 · last release 2020-08-23 · [PyPI](https://pypi.org/project/django-cloudinary-storage/)

<details><summary>README extract</summary>

Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary
by implementing Django Storage API.
With several lines of configuration, you can start using Cloudinary for both media and static files.
Also, it provides management commands for removing unnecessary files, so any cleanup will be a breeze. ...

Example:
```python
from django.db import models

from cloudinary_storage.storage import RawMediaCloudinaryStorage

class TestModelWithRawFileAndImage(models.Model):
    name = models.CharField(max_length=100)
    raw_file = models.ImageField(upload_to='raw/', blank=True, storage=RawMediaCloudinaryStorage())
...
```

Sections: Django Cloudinary Storage, Usage with raw files, Usage with video files, collectstatic, deleteorphanedmedia, deleteredundantstatic

</details>

### wkhtmltopdf

Simple python wrapper for wkhtmltopdf

`pip install wkhtmltopdf` · installs from source (sdist only) · licence: BSD License · rank 10302 · last release 2011-07-21 · [PyPI](https://pypi.org/project/wkhtmltopdf/)

<details><summary>README extract</summary>

A simple python wrapper for the wkhtmltopdf lib ( with flash support.

- Xvfd
- wkhtmltopdf
- flashplugin-nonfree
- python 2.5+

Example:
```python
from wkhtmltopdf import WKHtmlToPdf

wkhtmltopdf = WKHtmlToPdf(
    url='
    output_file='~/example.pdf',
)
wkhtmltopdf.render()
```

Sections: python-wkhtmltopdf, Requirements, System, wkhtmltopdf, Usage, Required Arguments, Optional Arguments

</details>

### django-summernote

Summernote plugin for Django

`pip install django-summernote` · installs from source (sdist only) · licence: MIT License · rank 10366 · last release 2021-10-14 · [PyPI](https://pypi.org/project/django-summernote/)

### wafer-py

Anti-detection HTTP client for Python

`pip install wafer-py` · installs (wheel) · licence: Apache-2.0 · rank 10381 · last release 2026-11-06 · [PyPI](https://pypi.org/project/wafer-py/) · [source](https://github.com/Averyy/wafer)

<details><summary>README extract</summary>

> Proof of concept. This project is experimental and not intended for production use. Expect breaking changes, rough edges, and missing features.

Anti-detection HTTP client for Python. Built on wreq (Rust + BoringSSL). ...

Example:
```python
import wafer

# One-shot request
resp = wafer.get("
print(resp.status_code)  # 200
print(resp.text)          # HTML string
print(resp.json())        # parsed JSON
print(resp.content)       # raw bytes (for PDFs, images, etc.)

# Session (reuses TLS identity, cookies, fingerprint)
with wafer.SyncSession() as session:
    resp = session.get("
...
```

...

</details>

### cornice

Define Web Services in Pyramid.

`pip install cornice` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 10420 · last release 2024-02-08 · [PyPI](https://pypi.org/project/cornice/) · [source](https://github.com/Cornices/cornice)

<details><summary>README extract</summary>

Cornice provides helpers to build & document Web Services with Pyramid.

The full documentation is available at:

Here is a (alphabetically-ordered) list of the people who contributed to
Cornice: ...

</details>

### asyncore-wsgi

Asynchronous WSGI and WebSocket server based on asyncore module

`pip install asyncore-wsgi` · installs (wheel) · licence: MIT License · rank 10438 · last release 2023-07-05 · [PyPI](https://pypi.org/project/asyncore-wsgi/)

<details><summary>README extract</summary>

This is a single-threaded asynchronous WSGI server with WebSockets support
based on asyncore module.
It should be compatible with Python 2.7 and 3.

Example:

The server in the preceding example serves a demo WSGI app from
the Standard Library and the echo WebSocket handler on `'/ws'` path.

WebSocket part was borrowed from
this project.

Example:
```python
from from wsgiref.simple_server import demo_app
from asyncore_wsgi import AsyncWebSocketHandler, make_server

class SimpleEchoHandler(AsyncWebSocketHandler):

    def handleMessage(self):
        print('Received WebSocket message: {}'.format(self.data))
        self.sendMessage(self.data)

    def handleConnected(self):
...
```

</details>

### django-compression-middleware

Django middleware to compress responses using several algorithms.

`pip install django-compression-middleware` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 10447 · last release 2023-03-23 · [PyPI](https://pypi.org/project/django-compression-middleware/)

<details><summary>README extract</summary>

This middleware implements compressed content encoding for HTTP. It is similar
to Django's `GZipMiddleware` (documentation), but additionally supports
other compression methods. It is meant to be a drop-in replacement for Django's
`GZipMiddleware`. Its documentation — including security warnings — therefore
apply here as well. ...

</details>

### starlette-csrf

Starlette middleware implementing Double Submit Cookie technique to mitigate CSRF

`pip install starlette-csrf` · installs (wheel) · licence: MIT License · rank 10462 · last release 2023-06-27 · [PyPI](https://pypi.org/project/starlette-csrf/) · [docs](https://github.com/frankie567/starlette-csrf) · [source](https://github.com/frankie567/starlette-csrf)

<details><summary>README extract</summary>

Starlette middleware implementing Double Submit Cookie technique to mitigate CSRF.

1. The user makes a first request with a method considered safe (by default `GET`, `HEAD`, `OPTIONS`, `TRACE`).
2. It receives in response a cookie (named by default `csrftoken`) which contains a secret value.
3. ...

Example:
```python
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette_csrf import CSRFMiddleware

routes = ...

middleware = [
    Middleware(CSRFMiddleware, secret="CHANGE_ME")
]

app = Starlette(routes=routes, middleware=middleware)
```

Sections: Starlette CSRF Middleware, How it works?, Usage with Starlette, Usage with FastAPI, Arguments, Customize error response, Setup environment, Run unit tests, Format the code

</details>

### httpcloak

Browser fingerprint emulation HTTP client with HTTP/1.1, HTTP/2, and HTTP/3 support

`pip install httpcloak` · installs (wheel) · licence: MIT License · rank 10508 · last release 2026-10-13 · [PyPI](https://pypi.org/project/httpcloak/) · [docs](https://github.com/sardanioss/httpcloak#readme) · [source](https://github.com/sardanioss/httpcloak)

<details><summary>README extract</summary>

Browser fingerprint emulation HTTP client with HTTP/1.1, HTTP/2, and HTTP/3 support.

Example:
```python
from httpcloak import Session

# Create a session with Chrome fingerprint
session = Session(preset="chrome-latest")

# Make requests
response = session.get("
print(response.status_code)
print(response.text)

# POST request with JSON
response = session.post(" json={"key": "value"})

# POST request with form data
...
```

Sections: HTTPCloak Python, Quick Start, Synchronous Usage, Context Manager (Recommended), Asynchronous Usage, Fast Response Mode, Streaming Downloads, HTTP Proxy, SOCKS5 Proxy, HTTP/3 MASQUE Proxy, Split Proxy Configuration, Advanced Features, Encrypted Client Hello (ECH), Domain Fronting (Connect-To)

</details>

### tendo

A Python library that extends some core functionality

`pip install tendo` · installs (wheel) · licence: Python Software Foundation License · rank 10528 · last release 2022-10-09 · [PyPI](https://pypi.org/project/tendo/)

<details><summary>README extract</summary>

Tendo is a python module that adds basic functionality that is
not provided by Python. Read the documentation for more info.

- transparent Unicode support for text file operations (BOM detection)
- console logging coloring
- enable you to use symlinks under windows ...

Sections: tendo, Requirements and compatibility, Related projects and packages

</details>

### django-eveonline-sde

Eve Online SDE Export in Django Model form

`pip install django-eveonline-sde` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 10544 · last release 2026-11-05 · [PyPI](https://pypi.org/project/django-eveonline-sde/)

_README extract left out: share-alike licence._

### django-qr-code

An application that provides tools for displaying QR codes on your Django site.

`pip install django-qr-code` · installs (wheel) · licence: BSD-3-Clause · rank 10553 · last release 2026-10-03 · [PyPI](https://pypi.org/project/django-qr-code/) · [docs](https://django-qr-code.readthedocs.io/)

<details><summary>README extract</summary>

This is an application that provides tools for displaying QR codes on your Django site.

This application depends on the Segno QR Code generator library.

This app makes no usage of the Django models and therefore do not use any database.

Only Python >= 3.10 is supported. ...

Features:
* Generate QR codes as embedded SVG or PNG images in HTML templates.
* Customize QR codes with various parameters (size, error correction, border, etc.).
* Generate URLs for QR code images. ...

Sections: Django QR Code, Features, Binary Package from PyPi, From the Source Code, Usage, Example: Inline QR Code, Example: URL QR Code, Advanced Usage of Tags, Demo Application, Generating Image Object Representing a QR Code, Projects Using this App

</details>

### django-admin-inline-paginator-plus

The 'Django Admin Inline Paginator Plus' is simple way to paginate your inlines in Django admin

`pip install django-admin-inline-paginator-plus` · installs (wheel) · licence: MIT License · rank 10574 · last release 2026-03-06 · [PyPI](https://pypi.org/project/django-admin-inline-paginator-plus/)

<details><summary>README extract</summary>

🍴 This is a forked and updated version based on original library django-admin-inline-paginator.

> *As for 10.07.2024 nobody took responsibility, so I decided to take it since we need additional functionlity like AJAX for pagination.*

The "Django Admin Inline Paginator Plus" is simple way to paginate your inline in django admin ...

Features:
- Easy Inline Pagination: Quickly paginate inlines in the Django admin.
- AJAX Support: Smooth and dynamic pagination without page reloads with `htmx`.
- Multiple Inline Pagination: Manage multiple paginated inlines seamlessly. ...

Example:
```python
from django_admin_inline_paginator_plus.admin import TabularInlinePaginated

class ModelWithFKAdminInline(TabularInlinePaginated):
    model = ModelWithFK
    fields = (...)
    per_page = 5
```

...

</details>

### urlpath

Object-oriented URL from urllib.parse and pathlib

`pip install urlpath` · installs (wheel) · licence: MIT · rank 10635 · last release 2025-10-13 · [PyPI](https://pypi.org/project/urlpath/) · [source](https://github.com/brandonschabell/urlpath)

<details><summary>README extract</summary>

URLPath provides URL manipulator class that extends `pathlib.PurePath`.

* Python 3.9–3.14
* Requests
* JMESPath (Optional)
* WebOb (Optional)

Example:
```python
from urlpath import URL

# Create URL object
url = URL(
    '

# Representation
assert str(url) == '
assert url.as_uri() == '
assert url.as_posix() == '

# Access pathlib.PurePath compatible properties
assert url.drive == '
assert url.root == '/'
assert url.anchor == '
assert url.path == '/path/to/file.ext'
assert url.name == 'file.ext'
...
```

Sections: URLPath, Dependencies, Examples, HTTP requests, Jail, Trailing separator will be retained

</details>

### browser-act-cli

CLI for browser automation with stealth and captcha solving capabilities.

`pip install browser-act-cli` · does not install on CPython 3.14 · licence: not stated · rank 10640 · last release 2026-11-05 · [PyPI](https://pypi.org/project/browser-act-cli/)

### django-auth-adfs

A Django authentication backend for Microsoft ADFS and AzureAD

`pip install django-auth-adfs` · installs (wheel) · licence: OSI Approved; BSD License · rank 10691 · last release 2026-01-08 · [PyPI](https://pypi.org/project/django-auth-adfs/) · [docs](https://django-auth-adfs.readthedocs.io/en/latest) · [source](https://github.com/snok/django-auth-adfs)

<details><summary>README extract</summary>

A Django authentication backend for Microsoft ADFS and Azure AD

* Free software: BSD License

Features:
* Integrates Django with Active Directory on Windows 2012 R2, 2016 or Azure AD in the cloud.
* Provides seamless single sign on (SSO) for your Django project on intranet environments. ...

Sections: ADFS Authentication for Django, Features

</details>

### fastapi-etag

Convenience library for working with etags in fastapi

`pip install fastapi-etag` · installs (wheel) · licence: MIT License · rank 10696 · last release 2021-06-23 · [PyPI](https://pypi.org/project/fastapi-etag/) · [source](https://github.com/steinitzu/fastapi-etag)

<details><summary>README extract</summary>

Example:
```python
# app.py

from fastapi import FastAPI
from starlette.requests import Request
from fastapi_etag import Etag, add_exception_handler

app = FastAPI()
add_exception_handler(app)

async def get_hello_etag(request: Request):
    return "etagfor" + request.path_params["name"]

@app.get("/hello/{name}", dependencies=[Depends(Etag(get_hello_etag))])
...
```

Sections: fastapi-etag, Quickstart, Add response headers

</details>

### base58check

Base58check encoding and decoding of binary data

`pip install base58check` · installs (wheel) · licence: MIT License · rank 10698 · last release 2018-04-07 · [PyPI](https://pypi.org/project/base58check/)

<details><summary>README extract</summary>

Example:
```python
>>> import base58check
```

Sections: Base58Check, Introduction, Usage, encoding, decoding (input can be text or bytes here), Changes

</details>

### python-redmine

Library for communicating with a Redmine project management application

`pip install python-redmine` · installs (wheel) · licence: Apache Software License · rank 10703 · last release 2024-03-31 · [PyPI](https://pypi.org/project/python-redmine/) · [docs](https://python-redmine.com)

<details><summary>README extract</summary>

Python-Redmine is a library for communicating with a Redmine
project management application. Redmine exposes some of its data via REST API for which Python-Redmine provides
a simple but powerful Pythonic API inspired by a well-known Django ORM:

Features:
* Supports 100% of Redmine API
* Supports external Redmine plugins API
* Supports Python 3.7 - 3.12 and PyPy3
* Supports different request engines
* Extendable via custom resources and custom request engines
* Extensively documented
* Provides ...

Example:
```python
>>> from redminelib import Redmine

>>> redmine = Redmine(' username='foo', password='bar')
>>> project = redmine.project.get('vacation')

>>> project.id
30404

>>> project.identifier
'vacation'

>>> project.created_on
datetime.datetime(2013, 12, 31, 13, 27, 47)

...

</details>

### zope.exceptions

Zope Exceptions

`pip install zope.exceptions` · installs (wheel) · licence: Zope Public License · rank 10708 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.exceptions/)

<details><summary>README extract</summary>

This package contains exception exceptions and implementations which are so
general purpose that they don't belong in Zope application-specific packages.

Please see for the documentation.

Sections: zope.exceptions, 6.0 (2025-09-12), 5.2 (2024-10-30), 5.1 (2024-06-07), 5.0.1 (2023-07-11), 5.0 (2023-06-29), 4.6 (2022-11-10), 4.5 (2022-02-11), 4.4 (2020-07-16), 4.3 (2018-10-04), 4.2.0 (2017-09-12), 4.1.0 (2017-04-12), 4.0.8 (2015-08-13), 4.0.7 (2014-03-19)

</details>

### ebaysdk

eBay SDK for Python

`pip install ebaysdk` · installs (wheel) · licence: COMMON DEVELOPMENT AND DISTRIBUTION LICENSE (CDDL) Version 1.0 · rank 10733 · last release 2020-04-20 · [PyPI](https://pypi.org/project/ebaysdk/)

<details><summary>README extract</summary>

This SDK is a programatic inteface into the eBay
APIs. It simplifies development and cuts development time by standerizing
calls, response processing, error handling, debugging across the Finding,
Shopping, Merchandising, & Trading APIs.

</details>

### allianceauth-app-utils

Commonly used utilities and helpers for rapid development of Alliance Auth apps.

`pip install allianceauth-app-utils` · installs (wheel) · licence: MIT License · rank 10764 · last release 2026-07-11 · [PyPI](https://pypi.org/project/allianceauth-app-utils/) · [docs](https://allianceauth-app-utils.readthedocs.io/en/latest/) · [source](https://github.com/AllianceAuth-Apps/allianceauth-app-utils)

<details><summary>README extract</summary>

Commonly used utility functions and classes for rapid development of Alliance Auth apps.

This package contains a variety of commonly used utility functions and classes that help speed up development of Alliance Auth apps and reduce code duplication across apps.

For a full description of the API please see the documentation.

Sections: allianceauth-app-utils, Description, Documentation

</details>

### crispy-bootstrap3

Bootstrap3 template pack for django-crispy-forms

`pip install crispy-bootstrap3` · installs (wheel) · licence: MIT License · rank 10771 · last release 2024-01-13 · [PyPI](https://pypi.org/project/crispy-bootstrap3/)

<details><summary>README extract</summary>

Bootstrap3 template pack for django-crispy-forms. This template pack was
included with the core django-crispy-forms package until version 2.0.

Sections: crispy-bootstrap3, Usage

</details>

### allianceauth-discordbot

Alliance Auth Modular Discord Bot

`pip install allianceauth-discordbot` · installs (wheel) · licence: MIT License · rank 10778 · last release 2026-07-18 · [PyPI](https://pypi.org/project/allianceauth-discordbot/) · [source](https://github.com/Solar-Helix-Independent-Transport/allianceauth-discordbot)

<details><summary>README extract</summary>

AA-Discordbot for Alliance Auth.

Features:
* Bot Framework, easily extensible with more Cogs
* Integration with Alliance Auth, able to fetch data directly from its django project. ...

Example:
```python
from django.contrib.auth.models import User
from django.apps import apps

# Use a small helper to check if AA-Discordbot is installs
def discord_bot_active():
    return apps.is_installed('aadiscordbot')

# Only import it, if it is installed
if discord_bot_active():
    from aadiscordbot.tasks import send_message
...
```

...

</details>

### pecan

A WSGI object-dispatching web framework, designed to be lean and fast, with few dependencies.

`pip install pecan` · installs (wheel) · licence: BSD License · rank 10787 · last release 2026-03-12 · [PyPI](https://pypi.org/project/pecan/)

### aa-srp

Improved SRP Module for Alliance Auth

`pip install aa-srp` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 10824 · last release 2026-11-07 · [PyPI](https://pypi.org/project/aa-srp/) · [docs](https://github.com/ppfeufer/aa-srp/blob/master/README.md) · [source](https://github.com/ppfeufer/aa-srp)

_README extract left out: share-alike licence._

### devpi-server

devpi-server: backend for hosting private package indexes and PyPI on-demand mirrors

`pip install devpi-server` · installs (wheel) · licence: MIT · rank 10850 · last release 2026-10-27 · [PyPI](https://pypi.org/project/devpi-server/) · [docs](https://doc.devpi.net) · [source](https://github.com/devpi/devpi)

<details><summary>README extract</summary>

You can point `uv`, `pip` or another Python package installer to the `root/pypi/+simple/` index,
serving as a transparent on-demand mirror for PyPI-hosted packages.

Each user (which can represent a person, project or team) can have multiple indexes,
and can upload packages and documents to these indexes via standard `twine` or `setup.py` ...

Features:
- Use sha256 for login token signing. Existing tokens will be invalidated, but they are valid for only 10 hours anyway.

Sections: PyPI on-demand package mirror, User specific indexes, Index inheritance, Sensible defaults for a low friction deployment, 6.21.0 (2026-10-26), Features, Bug Fixes, 6.20.3 (2026-06-30), 6.20.2 (2026-06-11), 6.20.1 (2026-05-11), 6.20.0 (2026-04-30)

</details>

### scrapinghub

Client interface for Scrapinghub API

`pip install scrapinghub` · installs (wheel) · licence: BSD License · rank 10852 · last release 2026-08-12 · [PyPI](https://pypi.org/project/scrapinghub/)

<details><summary>README extract</summary>

The `scrapinghub` is a Python 3.10+ library for communicating with the
Scrapinghub API.

Sections: Client interface for Scrapinghub API, Documentation

</details>

### aa-memberaudit

An Alliance Auth app that provides full access to Eve characters

`pip install aa-memberaudit` · installs (wheel) · licence: not stated · rank 10853 · last release 2026-10-05 · [PyPI](https://pypi.org/project/aa-memberaudit/) · [docs](https://aa-memberaudit.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

An Alliance Auth app that provides full access to Eve characters and related reports for auditing, vetting and monitoring.

Features:
Member Audit gives Alliance Auth full visibility into a corporation's or alliance's Eve characters.

Users can monitor their characters, recruiters can vet the characters of applicants, and leadership can audit the characters of their members to ...

Sections: Member Audit, Overview, Features, Highlights, Character Launcher, Character Viewer, Skill Sets, Character Finder, Documentation

</details>

### django-filer

A file management application for django that makes handling of files and images a breeze.

`pip install django-filer` · installs (wheel) · licence: BSD License · rank 10885 · last release 2026-09-11 · [PyPI](https://pypi.org/project/django-filer/)

<details><summary>README extract</summary>

django Filer is a file management application for django that makes
handling of files and images a breeze.

+-------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| .. image:: | .. ...

Sections: Django Filer, Documentation

</details>

### django-robots

Robots exclusion application for Django, complementing Sitemaps.

`pip install django-robots` · installs (wheel) · licence: BSD-3-Clause · rank 10896 · last release 2026-11-01 · [PyPI](https://pypi.org/project/django-robots/) · [docs](https://django-robots.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

This is a basic Django application to manage robots.txt files following the
robots exclusion protocol, complementing the Django Sitemap contrib app.

For installation instructions, see the documentation install section;
for instructions on how to use this application, and on
what it provides, see the file "overview.txt" in the "docs/"
directory or ...

</details>

### zope.security

Zope Security Framework

`pip install zope.security` · installs (wheel) · licence: ZPL-2.1 · rank 10912 · last release 2026-10-27 · [PyPI](https://pypi.org/project/zope.security/) · [docs](https://zopesecurity.readthedocs.io) · [source](https://github.com/zopefoundation/zope.security)

<details><summary>README extract</summary>

Sections: 8.5 (2026-10-27), 8.4 (2026-08-20), 8.3 (2025-11-17), 8.2 (2025-10-28), 8.1 (2025-09-23), 8.0 (2025-09-15), 7.3 (2024-10-02), 7.2 (2024-09-17), 7.1 (2024-08-16), 7.0 (2024-05-30), 6.2 (2023-10-05), 6.1 (2023-01-18), 6.0 (2023-01-16), 5.8 (2022-11-30)

</details>

### aa-structures

An app for managing EVE Online structures with Alliance Auth.

`pip install aa-structures` · installs (wheel) · licence: not stated · rank 10974 · last release 2026-10-05 · [PyPI](https://pypi.org/project/aa-structures/) · [docs](https://aa-structures.readthedocs.io)

<details><summary>README extract</summary>

An app for managing EVE Online structures with Alliance Auth.

Features:
Built for Alliance Auth, it allows all member corporations to see a current list of all their structures in Auth. In addition it allows forwarding EVE Online notifications to Discord.

Sections: Structures, Overview, Features, Screenshots, Documentation

</details>

### flask-redis

A nice way to use Redis in your Flask app

`pip install flask-redis` · installs (wheel) · licence: not stated · rank 10989 · last release 2019-05-29 · [PyPI](https://pypi.org/project/flask-redis/)

<details><summary>README extract</summary>

A nice way to use Redis in your Flask app.

Start by installing the extension with `pip install flask-redis`.
Once that's done, configure it within your Flask config.
Set the URL of your Redis instance like this:

If you wanna connect to a Unix socket,
you can specify it like `"unix://:password@/path/to/socket.sock?db=0"`.

Example:
```python
from flask import Flask
from flask_redis import FlaskRedis

app = Flask(name)
redis_client = FlaskRedis(app)
```

Sections: flask-redis, Configuration, Usage, Setup, Accessing Redis, Extra features in flask-redis, Custom providers, 0.4.0 (2019-05-29), 0.3.0 (2016-07-18), 0.2.0 (2015-04-15), 0.1.0 (2015-04-15), 0.0.6 (2014-04-09), 0.0.5 (2014-02-17), 0.0.4 (2014-02-17)

</details>

### django-cryptography-5

Easily encrypt data in Django

`pip install django-cryptography-5` · installs (wheel) · licence: BSD License · rank 11015 · last release 2025-01-28 · [PyPI](https://pypi.org/project/django-cryptography-5/) · [docs](https://django-cryptography.readthedocs.io) · [source](https://github.com/saaspegasus/django-cryptography)

<details><summary>README extract</summary>

Note: This is a fork of the official django-cryptography project,
which appears to be abandoned.
The only change made in this fork that the patch that fixes Django 5 compatibility
has been applied and pushed to pypi as a new project.

You can install the forked version from pypi with the following command: ...

Example:
```python
from django.db import models

from django_cryptography.fields import encrypt

class MyModel(models.Model):
    name = models.CharField(max_length=50)
    sensitive_data = encrypt(models.CharField(max_length=50))
```

Sections: Django Cryptography 5, Django Cryptography, Cryptography by example, Requirements

</details>

### aa-fleetpings

Fleet Ping Tool for Alliance Auth supporting pings via webhooks to Discord.

`pip install aa-fleetpings` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 11031 · last release 2026-10-06 · [PyPI](https://pypi.org/project/aa-fleetpings/) · [docs](https://github.com/ppfeufer/aa-fleetpings/blob/master/README.md) · [source](https://github.com/ppfeufer/aa-fleetpings)

_README extract left out: share-alike licence._

### django-more-admin-filters

Additional filters for django-admin.

`pip install django-more-admin-filters` · installs (wheel) · licence: BSD License · rank 11043 · last release 2026-01-07 · [PyPI](https://pypi.org/project/django-more-admin-filters/)

<details><summary>README extract</summary>

> Note
> If you are looking for a generic way of building and applying complex filters with a dynamic form right in the django admin backend, please checkout django-searchkit.

Django-more-admin-filters is a collection of Django admin filters with a focus on filters using dropdown widgets, multiple choice filters and filters working with annotated ...

Sections: Welcome to django-more-admin-filters, Description, Filter classes

</details>

### django-slowtests

locate your slowest tests

`pip install django-slowtests` · installs from source (sdist only) · licence: MIT License · rank 11065 · last release 2019-02-12 · [PyPI](https://pypi.org/project/django-slowtests/)

<details><summary>README extract</summary>

Welcome to the documentation for django-slowtests!

*Code tested on Django 1.6, 1.7, 1.8, 1.9, 1.10 and 1.11 with Python 2.7 and 3.6

1. Install:
2. Add the following settings:
3. Run test suite:
3.1. Save report to file:
3.2. Generating full reports to file:
4. Sample output:

Sections: django-slowtests, Welcome!, Instructions, Running the Tests, Known Issues

</details>

### allianceauth-afat

Another Fleet Activity Tracking tool for Alliance Auth

`pip install allianceauth-afat` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 11069 · last release 2026-10-04 · [PyPI](https://pypi.org/project/allianceauth-afat/) · [docs](https://github.com/ppfeufer/allianceauth-afat/blob/master/README.md) · [source](https://github.com/ppfeufer/allianceauth-afat)

_README extract left out: share-alike licence._

### django-eveuniverse

Complete set of Eve Universe models with on-demand loading from ESI.

`pip install django-eveuniverse` · installs (wheel) · licence: not stated · rank 11088 · last release 2026-10-05 · [PyPI](https://pypi.org/project/django-eveuniverse/) · [docs](https://django-eveuniverse.readthedocs.io)

<details><summary>README extract</summary>

Complete set of Eve Online Universe models in Django with on-demand loading from ESI.

Features:
*django-eveuniverse* is a foundation app meant to help speed up the development of Eve Online apps with Django and ESI. It provides all classic "static" Eve classes as Django models, including all relationships, ready to be used in your project. ...

Sections: Eve Universe, Overview, Documentation

</details>

### pyshorteners

A Python lib to wrap and consume the most used shorteners APIs

`pip install pyshorteners` · installs from source (sdist only) · licence: GNU General Public License v3 or later (GPLv3+) · rank 11095 · last release 2020-03-19 · [PyPI](https://pypi.org/project/pyshorteners/)

_README extract left out: share-alike licence._

### django-defender

redis based Django app that locks out users after too many failed login attempts.

`pip install django-defender` · installs (wheel) · licence: Apache Software License · rank 11103 · last release 2024-02-15 · [PyPI](https://pypi.org/project/django-defender/)

<details><summary>README extract</summary>

redis based Django app based on speed, that locks outusers after too many failed login attempts.

</details>

### advocate

A wrapper around the requests library for safely making HTTP requests on behalf of a third party

`pip install advocate` · installs (wheel) · licence: Apache Software License · rank 11110 · last release 2020-07-14 · [PyPI](https://pypi.org/project/advocate/)

<details><summary>README extract</summary>

Advocate is a set of tools based around the requests library for safely making
HTTP requests on behalf of a third party. Specifically, it aims to prevent
common techniques that enable SSRF attacks.

Advocate was inspired by fin1te's SafeCurl project.

Example:
```python
>>> import advocate
>>> print advocate.get("
<Response [200]>
```

Sections: Advocate, See it in action, Examples, Conditionally bypassing protection, When should I use Advocate?, When should I not use Advocate?, This seems like it's been done before, It sees URLs the same as the underlying HTTP library, It deals with DNS rebinding, It handles redirects sanely, TODO, Caveats

</details>

### aws-wsgi

WSGI adapter for AWS API Gateway/Lambda Proxy Integration

`pip install aws-wsgi` · installs (wheel) · licence: MIT License · rank 11130 · last release 2020-07-07 · [PyPI](https://pypi.org/project/aws-wsgi/)

<details><summary>README extract</summary>

AWSGI allows you to use WSGI-compatible middleware and frameworks like Flask and Django with the AWS API Gateway/Lambda proxy integration.

Example:
```python
import awsgi
from flask import (
    Flask,
    jsonify,
)

app = Flask(name)

@app.route('/')
def index():
    return jsonify(status=200, message='OK')

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})
```

Sections: AWSGI, A WSGI adapter for AWS API Gateway/Lambda Proxy Integration, Example

</details>

### aa-killtracker

An app for running killmail trackers with Alliance Auth and Discord.

`pip install aa-killtracker` · installs (wheel) · licence: not stated · rank 11144 · last release 2026-10-05 · [PyPI](https://pypi.org/project/aa-killtracker/)

<details><summary>README extract</summary>

An app for running killmail trackers with Alliance Auth and Discord.

Features:
Killtracker is an app for running killmail based trackers with Alliance Auth and Discord. Trackers are small programs that automatically select killmails based on a set of pre-defined conditions and then post them to a Discord channel as soon as ...

Sections: Killtracker, Overview, Key Features, Screenshots, Step 1 - Check preconditions, Step 3 - Configure settings, Killtracker configuration, Additional settings (optional), Step 5 - Load Eve Universe map data, Step 6 - Setup trackers, Trackers, Settings

</details>

### aa-killstats

Killboard Stats shows Hall of Shame/Fame, Kills, Top Kills,Loss,etc.

`pip install aa-killstats` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 11177 · last release 2026-10-03 · [PyPI](https://pypi.org/project/aa-killstats/) · [docs](https://github.com/Geuthur/aa-killstats/blob/master/README.md) · [source](https://github.com/Geuthur/aa-killstats)

_README extract left out: share-alike licence._

### ormar

An async ORM with fastapi in mind and pydantic validation.

`pip install ormar` · installs (wheel) · licence: MIT License · rank 11206 · last release 2026-10-27 · [PyPI](https://pypi.org/project/ormar/) · [docs](https://ormar-orm.github.io/ormar/) · [source](https://github.com/ormar-orm/ormar)

<details><summary>README extract</summary>

Features:
The `ormar` package is an async mini ORM for Python, with support for **Postgres,
MySQL, and SQLite**.

The main benefits of using `ormar` are: ...

Example:
```python
from typing import Optional

import ormar
import pydantic
import sqlalchemy

DATABASE_URL = "sqlite+aiosqlite:///db.sqlite"

# note that this step is optional -> all ormar cares is an individual
# OrmarConfig for each of the models, but this way you do not
# have to repeat the same parameters if you use only one database
...
```

...

</details>

### aa-taskmonitor

An Alliance Auth app for monitoring celery tasks.

`pip install aa-taskmonitor` · installs (wheel) · licence: MIT License · rank 11213 · last release 2026-06-30 · [PyPI](https://pypi.org/project/aa-taskmonitor/) · [source](https://github.com/AllianceAuth-Apps/aa-taskmonitor)

<details><summary>README extract</summary>

An Alliance Auth app for monitoring celery tasks.

Features:
Task Monitor enables administrators to monitor celery tasks running on their system.

- Creates a log of all recently executed celery tasks including failed and retried tasks. ...

Sections: Task Monitor, Features, Screenshots, Full log of all recently executed tasks, View details for each task incl. exception tracelogs, Example chart in reports, View detailed statistics for all tasks, Step 1 - Check prerequisites, Step 3 - Configure Auth settings, Command line utility, Settings, FAQ, How is this app different from celery analytics?, How is this app different from celery's flower?

</details>

### aa-contacts

Contacts tool for AllianceAuth

`pip install aa-contacts` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 11234 · last release 2026-10-04 · [PyPI](https://pypi.org/project/aa-contacts/) · [source](https://github.com/Maestro-Zacht/aa-contacts)

_README extract left out: share-alike licence._

