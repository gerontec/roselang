# Utilities

[Index](README.md) · 205 packages in this topic, 742 more listed under another topic, by downloads.

### PyJWT

JSON Web Token implementation in Python

`pip install PyJWT` · installs (wheel) · licence: MIT · rank 36 · last release 2026-09-28 · [PyPI](https://pypi.org/project/PyJWT/)

<details><summary>README extract</summary>

A Python implementation of RFC 7519. Original implementation was written by @progrium.

Example:
```python
>>> import jwt
>>> encoded = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
>>> print(encoded)
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg
>>> jwt.decode(encoded, "secret", algorithms=["HS256"])
{'some': 'payload'}
```

Sections: PyJWT, Usage, Documentation, Tests

</details>

### tenacity

Retry code until it succeeds

`pip install tenacity` · installs (wheel) · licence: Apache-2.0 · rank 82 · last release 2026-10-07 · [PyPI](https://pypi.org/project/tenacity/) · [docs](https://tenacity.readthedocs.io) · [source](https://github.com/jd/tenacity)

<details><summary>README extract</summary>

Tenacity is a general-purpose retrying library to simplify the task of adding
retry behavior to just about anything.

See the documentation for examples and the
API reference.

</details>

### kubernetes

Kubernetes python client

`pip install kubernetes` · installs (wheel) · licence: Apache-2.0 · rank 322 · last release 2026-11-06 · [PyPI](https://pypi.org/project/kubernetes/)

### markdownify

Convert HTML to markdown.

`pip install markdownify` · installs (wheel) · licence: MIT License · rank 411 · last release 2026-06-30 · [PyPI](https://pypi.org/project/markdownify/)

<details><summary>README extract</summary>

Example:
```python
from markdownify import markdownify as md
md('Yay GitHub')  # > 'Yay GitHub'
```

Sections: Usage, Options, Converting BeautifulSoup objects, Creating Custom Converters, Command Line Interface

</details>

### click-plugins

An extension module for click to enable registering CLI commands via setuptools entry-points.

`pip install click-plugins` · installs (wheel) · licence: BSD License · rank 438 · last release 2025-06-25 · [PyPI](https://pypi.org/project/click-plugins/)

<details><summary>README extract</summary>

This PyPI package is no longer actively maintained, but the underlying
library can be vendored. See homepage
for more information.

An extension module for click to register
external CLI commands via setuptools entry-points.

Features:
Lets say you develop a commandline interface and someone requests a new feature
that is absolutely related to your project but would have negative consequences
like additional dependencies, major refactoring, or maybe its just too domain
specific to ...

Example:
```python
from pkg_resources import iter_entry_points

import click
from click_plugins import with_plugins

@with_plugins(iter_entry_points('core_package.cli_plugins'))
@click.group()
def cli():
    """Commandline interface for yourpackage."""

@cli.command()
def subcommand():
...

</details>

### webcolors

A library for working with the color formats defined by HTML and CSS.

`pip install webcolors` · installs (wheel) · licence: BSD License · rank 476 · last release 2025-10-31 · [PyPI](https://pypi.org/project/webcolors/) · [docs](https://webcolors.readthedocs.io) · [source](https://github.com/ubernostrum/webcolors)

<details><summary>README extract</summary>

`webcolors` is a module for working with and converting between the
various HTML/CSS color formats.

Support is included for normalizing and converting between the
following formats (RGB colorspace only; conversion to/from HSL can be
handled by the `colorsys` module in the Python standard library):

* Specification-defined color names ...

Example:
```python
>>> import webcolors
>>> webcolors.hex_to_name("#daa520")
'goldenrod'
```

</details>

### tldextract

Accurately separates a URL's subdomain, domain, and public suffix, using the Public Suffix List (PSL). By default, this includes the public ICANN TLDs and their exceptions. You can optionally support the Public Suffix List's private domains as well.

`pip install tldextract` · installs (wheel) · licence: BSD-3-Clause · rank 533 · last release 2026-10-03 · [PyPI](https://pypi.org/project/tldextract/)

<details><summary>README extract</summary>

`tldextract` accurately separates a URL's subdomain, domain, and public suffix,
using the Public Suffix List (PSL).

Why? Naive URL parsing like splitting on dots fails for domains like
`forums.bbc.co.uk` (gives "co" instead of "bbc"). `tldextract` handles the edge
cases, so you don't have to.

Features:
See URL validation and
How to validate URLs before extraction.

Example:
```python
>>> import tldextract

>>> tldextract.extract('
ExtractResult(subdomain='forums.news', domain='cnn', suffix='com', is_private=False)

>>> tldextract.extract('
ExtractResult(subdomain='forums', domain='bbc', suffix='co.uk', is_private=False)

>>> # Access the parts you need
>>> ext = tldextract.extract('
>>> ext.domain
'bbc'
...
```

...

</details>

### grimp

Builds a queryable graph of the imports within one or more Python packages.

`pip install grimp` · installs (wheel) · licence: BSD License · rank 605 · last release 2026-11-06 · [PyPI](https://pypi.org/project/grimp/) · [docs](https://grimp.readthedocs.io/)

<details><summary>README extract</summary>

Builds a queryable graph of the imports within one or more Python packages.

Example:
```python
>>> import grimp
>>> graph = grimp.build_graph('somepackage')
```

Sections: Grimp, Quick start, External packages, Multiple packages, Namespace packages, What's a namespace package?

</details>

### lazy-object-proxy

A fast and thorough lazy object proxy.

`pip install lazy-object-proxy` · installs (wheel) · licence: BSD-2-Clause · rank 615 · last release 2026-10-20 · [PyPI](https://pypi.org/project/lazy-object-proxy/) · [docs](https://python-lazy-object-proxy.readthedocs.io/)

<details><summary>README extract</summary>

Features:
A fast and thorough lazy object proxy.

* Free software: BSD 2-Clause License

Note that this is based on wrapt's ObjectProxy with one big change: it calls a function the first time the proxy object is
used, while `wrapt.ObjectProxy` just forwards ...

Example:
```python
import lazy_object_proxy

def expensive_func():
    from time import sleep
    print('starting calculation')
    # just as example for a very slow computation
    sleep(2)
    print('finished calculation')
    # return the result of the calculation
    return 10

obj = lazy_object_proxy.Proxy(expensive_func)
...
```

Sections: Overview, Documentation

</details>

### python-jose

JOSE implementation in Python

`pip install python-jose` · installs (wheel) · licence: MIT License · rank 621 · last release 2025-05-28 · [PyPI](https://pypi.org/project/python-jose/) · [docs](https://python-jose.readthedocs.io/en/latest/) · [source](https://github.com/mpdavis/python-jose/)

<details><summary>README extract</summary>

A JOSE implementation in Python

Docs are available on ReadTheDocs.

The JavaScript Object Signing and Encryption (JOSE) technologies - JSON
Web Signature (JWS), JSON Web Encryption (JWE), JSON Web Key (JWK), and
JSON Web Algorithms (JWA) - collectively can be used to encrypt and/or
sign content using a variety of algorithms. ...

Example:
```python
>>> from jose import jwt
>>> token = jwt.encode({'key': 'value'}, 'secret', algorithm='HS256')
u'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ2YWx1ZSJ9.FG-8UppwHaFp1LgRYQQeS6EDQF7_6-bMFegNucHjmWg'

>>> jwt.decode(token, 'secret', algorithms=['HS256'])
{u'key': u'value'}
```

Sections: python-jose, Cryptographic Backends, . cryptography, . pycryptodome, . native-python, Usage, Thanks

</details>

### import-linter

Lint your Python architecture

`pip install import-linter` · installs (wheel) · licence: BSD License · rank 625 · last release 2026-11-06 · [PyPI](https://pypi.org/project/import-linter/) · [docs](https://import-linter.readthedocs.io/)

<details><summary>README extract</summary>

Lint your Python architecture.

Import Linter allows you to impose constraints on the imports between your Python modules.

It also provides a browser-based user interface for exploring the architecture of any Python package.

 Get started.

</details>

### tblib

Traceback serialization library.

`pip install tblib` · installs (wheel) · licence: BSD-2-Clause · rank 697 · last release 2025-11-12 · [PyPI](https://pypi.org/project/tblib/) · [docs](https://python-tblib.readthedocs.io/)

<details><summary>README extract</summary>

Features:
Serialization library for Exceptions and Tracebacks.

* Free software: BSD license

It allows you to:

* Pickle tracebacks and raise exceptions
 with pickled tracebacks in different processes. ...

Example:
```python
>>> from tblib import pickling_support
>>> pickling_support.install()
>>> import pickle, sys
>>> def inner_0():
...     raise Exception('fail')
...
>>> def inner_1():
...     inner_0()
...
>>> def inner_2():
...     inner_1()
...
>>> try:
...     inner_2()
... except:
...     s1 = pickle.dumps(sys.exc_info())
...
>>> len(s1) > 1
True
>>> try:
...
```

...

</details>

### docopt

Pythonic argument parser, that will make you smile

`pip install docopt` · installs from source (sdist only) · licence: MIT License · rank 763 · last release 2014-06-16 · [PyPI](https://pypi.org/project/docopt/)

<details><summary>README extract</summary>

Video introduction to docopt: PyCon UK 2012: Create *beautiful*
command-line interfaces with Python

 New in version 0.6.1:

 - Fix issue #85
 which caused improper handling of `[options]` shortcut
 if it was present several times.

 New in version 0.6.0:

 - New argument `options_first`, disallows interspersing options
 and arguments. ...

Example:
```python
"""Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
  naval_fate.py (-h | --help)
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
...
```

...

</details>

### schema

Simple data validation library

`pip install schema` · installs (wheel) · licence: MIT License · rank 826 · last release 2025-10-11 · [PyPI](https://pypi.org/project/schema/)

<details><summary>README extract</summary>

schema is a library for validating Python data structures, such as those
obtained from config-files, forms, external services or command-line
parsing, converted from JSON/YAML (or something else) to Python data-types.

Example:
```python
from schema import Schema, And, Use, Optional, SchemaError

schema = Schema(
    [
        {
            "name": And(str, len),
            "age": And(Use(int), lambda n: 18 <= n <= 99),
            Optional("gender"): And(
                str,
                Use(str.lower),
                lambda s: s in ("squid", "kid"),
            ),
...
```

...

</details>

### daff

Diff and patch tables

`pip install daff` · installs (wheel) · licence: MIT License · rank 843 · last release 2025-05-04 · [PyPI](https://pypi.org/project/daff/)

<details><summary>README extract</summary>

This is a library for comparing tables, producing a summary of their
differences, and using such a summary as a patch file. It is
optimized for comparing tables that share a common origin, in other
words multiple versions of the "same" table.

For a live demo, see:

Install the library for your favorite language:

Use on the web from a CDN: ...

</details>

### py-cpuinfo

Get CPU info with pure Python

`pip install py-cpuinfo` · installs (wheel) · licence: MIT License · rank 853 · last release 2022-10-25 · [PyPI](https://pypi.org/project/py-cpuinfo/)

<details><summary>README extract</summary>

Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work
without any extra programs or libraries, beyond what your OS provides.
It does not require any compilation(C/C++, assembly, et cetera) to use.
It works with Python 3.

Documentation can be viewed here:

</details>

### bitarray

efficient arrays of booleans -- C extension

`pip install bitarray` · installs (wheel) · licence: PSF-2.0 · rank 942 · last release 2026-10-19 · [PyPI](https://pypi.org/project/bitarray/)

<details><summary>README extract</summary>

This library provides an object type which efficiently represents an array
of booleans. Bitarrays are sequence types and behave very much like usual
lists. Eight bits are represented by one byte in a contiguous block of
memory. The user can select between two representations: little-endian
and big-endian. All functionality is implemented in C. ...

Features:
* The bit-endianness can be specified for each bitarray object, see below.
* Sequence methods: slicing (including slice assignment and deletion),
 operations `+`, `*`, `+=`, `*=`, the `in` operator, `len()`
* Bitwise operations: `~`, `&`, `|`, `^`, ...

Example:
```python
>>> from bitarray import bitarray
>>> a = bitarray()         # create empty bitarray
>>> a.append(1)
>>> a.extend([1, 0])
>>> a
bitarray('110')
...

</details>

### django-extensions

Extensions for Django

`pip install django-extensions` · installs (wheel) · licence: MIT · rank 1013 · last release 2025-04-11 · [PyPI](https://pypi.org/project/django-extensions/) · [docs](https://django-extensions.readthedocs.io/) · [source](https://github.com/django-extensions/django-extensions)

<details><summary>README extract</summary>

Django Extensions is a collection of custom extensions for the Django Framework.

Sections: Django Extensions, Getting Started, Requirements, Getting It, Using It, Getting Involved, Documentation

</details>

### kubernetes-asyncio

Kubernetes Asynchronous Python Client

`pip install kubernetes-asyncio` · installs (wheel) · licence: Apache-2.0 · rank 1062 · last release 2026-06-04 · [PyPI](https://pypi.org/project/kubernetes-asyncio/)

<details><summary>README extract</summary>

Asynchronous (AsyncIO) client library for the Kubernetes API.

This library is created in the same way as the official but
uses asynchronous version of OpenAPI generator.
My motivation is described here:

Example:
```python
import asyncio
from kubernetes_asyncio import client, config
from kubernetes_asyncio.client.api_client import ApiClient

async def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    await config.load_kube_config()

...
```

Sections: Kubernetes Python Client, Example, Documentation, Microsoft Windows, Versions

</details>

### fasteners

A python package that provides useful locks

`pip install fasteners` · installs (wheel) · licence: Apache-2.0 · rank 1074 · last release 2025-08-11 · [PyPI](https://pypi.org/project/fasteners/)

<details><summary>README extract</summary>

Cross-platform locks for threads and processes.

🔩 Install

🔩 Usage

Lock for processes has the same API as the
threading.Lock
for threads:

Reader Writer lock has a similar API, which is the same for threads or processes:

🔩 Overview

Python standard library provides a lock for threads (both a reentrant one, and a
non-reentrant one, see below). ...

Example:
```python
import fasteners
import threading

lock = threading.Lock()                                 # for threads
lock = fasteners.InterProcessLock('path/to/lock.file')  # for processes

with lock:
    ... # exclusive access

# or alternatively

lock.acquire()
... # exclusive access
lock.release()
```

Sections: Fasteners, Process locks, Thread locks

</details>

### pytest-benchmark

A ``pytest`` fixture for benchmarking code. It will group the tests into rounds that are calibrated to the chosen timer.

`pip install pytest-benchmark` · installs (wheel) · licence: BSD-2-Clause · rank 1152 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pytest-benchmark/) · [docs](https://pytest-benchmark.readthedocs.io/)

<details><summary>README extract</summary>

Features:
A `pytest` fixture for benchmarking code. It will group the tests into rounds that are calibrated to the chosen
timer.

See calibration and FAQ.

* Free software: BSD 2-Clause License

Example:
```python
def something(duration=0.000001):
    """
    Function that needs some serious benchmarking.
    """
    time.sleep(duration)
    # You may return anything you want, like the result of a computation
    return 123

def test_my_stuff(benchmark):
    # benchmark something
    result = benchmark(something)

...
```

Sections: Overview, Documentation, Examples, Screenshots, v5.3.1 (2026-11-01), v5.3.0 (2026-08-23), v5.2.3 (2025-11-09), v5.2.2 (2025-11-07), v5.2.1 (2025-11-04), v5.2.0 (2025-10-30), v5.1.0 (2024-10-30), v5.0.1 (2024-10-30), v5.0.0 (2024-10-29), v4.0.0 (2022-10-26)

</details>

### puremagic

Pure python implementation of magic file detection

`pip install puremagic` · installs (wheel) · licence: MIT · rank 1244 · last release 2026-04-08 · [PyPI](https://pypi.org/project/puremagic/)

<details><summary>README extract</summary>

puremagic is a pure python module that will identify a file based off
its magic numbers. It has zero runtime dependencies and serves as a
lightweight, cross-platform alternative to python-magic/libmagic.

It is designed to be minimalistic and inherently cross platform
compatible. It is also designed to be a stand in for python-magic. ...

Example:
```python
import puremagic

filename = "test/resources/images/test.gif"

ext = puremagic.from_file(filename)
# '.gif'

puremagic.magic_file(filename)
# [['.gif', 'image/gif', 'Graphics interchange format file (GIF87a)', 0.7],
# ['.gif', '', 'GIF file', 0.5]]
```

Sections: puremagic, Compatibility, Usage, Deep Scan, Script, Upgrading from 1.x, FAQ

</details>

### django-timezone-field

A Django app providing DB, form, and REST framework fields for zoneinfo and pytz timezone objects.

`pip install django-timezone-field` · installs (wheel) · licence: BSD License · rank 1290 · last release 2026-06-06 · [PyPI](https://pypi.org/project/django-timezone-field/) · [source](https://github.com/mfogel/django-timezone-field/)

<details><summary>README extract</summary>

A Django app providing DB, form, and REST framework fields for
`zoneinfo` and `pytz` timezone
objects.

Like Django, this app supports both `pytz` and `zoneinfo` objects while the community transitions away from `pytz` to
`zoneinfo`. All exposed fields and functions that return a timezone object accept an optional boolean kwarg `use_pytz`. ...

Example:
```python
import zoneinfo
import pytz
from django.db import models
from timezone_field import TimeZoneField

class MyModel(models.Model):
    tz1 = TimeZoneField(default="Asia/Dubai")               # defaults supported, in ModelForm renders like "Asia/Dubai"
...
```

...

</details>

### docker-pycreds

Python bindings for the docker credentials store API

`pip install docker-pycreds` · installs (wheel) · licence: Apache Software License · rank 1585 · last release 2018-11-29 · [PyPI](https://pypi.org/project/docker-pycreds/)

<details><summary>README extract</summary>

Python bindings for the docker credentials store API

Docker documentation page

On top of the dependencies in `requirements.txt`, the `docker-credential`
executable for the platform must be installed on the user's system.

Example:
```python
import dockerpycreds

store = dockerpycreds.Store('secretservice')
store.store(
    server=' username='johndoe',
    secret='hunter2'
)

print(store.list())

print(store.get('

store.erase('
```

Sections: docker-pycreds, Credentials store info, Requirements, API usage

</details>

### optree

Optimized PyTree Utilities.

`pip install optree` · installs (wheel) · licence: Apache-2.0 · rank 1595 · last release 2026-08-20 · [PyPI](https://pypi.org/project/optree/) · [docs](https://optree.readthedocs.io) · [source](https://github.com/metaopt/optree)

<details><summary>README extract</summary>

<!-- markdownlint-disable html -->

Optimized PyTree Utilities.

Example:
```python
>>> tree = {'b': (2, [3, 4]), 'a': 1, 'c': 5, 'd': 6}
>>> optree.tree_flatten(tree)
([1, 2, 3, 4, 5, 6], PyTreeSpec({'a': *, 'b': (*, [*, *]), 'c': *, 'd': *}))
>>> optree.tree_flatten(1)
([1], PyTreeSpec(*))
>>> optree.tree_flatten(None)
([], PyTreeSpec(None))
>>> optree.tree_map(lambda x: x**2, tree)
{'b': (4, [9, 16]), 'a': 1, 'c': 25, 'd': 36}
```

Sections: OpTree, PyTrees, Tree Nodes and Leaves, Built-in PyTree Node Types, Registering a Container-like Custom Type as Non-leaf Nodes, Notes about the PyTree Type Registry, `None` is Non-leaf Node vs. `None` is Leaf, Key Ordering for Dictionaries

</details>

### nanoid

A tiny, secure, URL-friendly, unique string ID generator for Python

`pip install nanoid` · installs (wheel) · licence: MIT License · rank 1645 · last release 2018-11-20 · [PyPI](https://pypi.org/project/nanoid/)

<details><summary>README extract</summary>

A tiny, secure, URL-friendly, unique string ID generator for Python.

* Safe. It uses cryptographically strong random APIs and tests distribution of symbols;
* Compact. It uses a larger alphabet than UUID (A-Za-z0-9-). So ID size was reduced from 36 to 21 symbols.

Example:
```python
from nanoid import generate

generate() # => NDzkGoTCdRcaRyt7GOepg
```

Sections: Nano ID, Usage, Normal, Custom Alphabet or Length, Tools, Other Programming Languages

</details>

### dictdiffer

Dictdiffer is a library that helps you to diff and patch dictionaries.

`pip install dictdiffer` · installs (wheel) · licence: MIT · rank 1670 · last release 2026-07-16 · [PyPI](https://pypi.org/project/dictdiffer/) · [docs](https://dictdiffer.rtfd.io/)

<details><summary>README extract</summary>

Dictdiffer is a helper module that helps you to diff and patch
dictionaries.

Sections: Dictdiffer, About, Documentation

</details>

### django-appconf

A helper class for handling configuration defaults of packaged apps gracefully.

`pip install django-appconf` · installs (wheel) · licence: BSD License · rank 1842 · last release 2025-11-08 · [PyPI](https://pypi.org/project/django-appconf/) · [source](https://github.com/django-compressor/django-appconf)

<details><summary>README extract</summary>

A helper class for handling configuration defaults of packaged Django
apps gracefully.

Features:
Say you have an app called `myapp` with a few defaults, which you want
to refer to in the app's code without repeating yourself all the time.
`appconf` provides a simple class to implement those defaults. ...

Example:
```python
from appconf import AppConf

class MyAppConf(AppConf):
    SETTING_1 = "one"
    SETTING_2 = (
        "two",
    )
```

Sections: django-appconf, Overview

</details>

### fixedint

simple fixed-width integers

`pip install fixedint` · installs (wheel) · licence: Python Software Foundation License · rank 1929 · last release 2022-09-16 · [PyPI](https://pypi.org/project/fixedint/)

<details><summary>README extract</summary>

This module provides fixed-size integer classes which retain their fixed nature across
arithmetic operations. It is geared towards users who need to emulate machine integers.

It provides flexible classes for defining integers with a fixed number of bits, as well
as predefined classes for common machine integer sizes. ...

Example:
```python
x = UInt32(0)
print(hex(~x)) # prints 0xffffffff
```

Sections: fixedint: simple fixed-width integers, Basic Usage, Arithmetic Operations, Slicing, Byte Conversion

</details>

### python-keycloak

python-keycloak is a Python package providing access to the Keycloak API.

`pip install python-keycloak` · installs (wheel) · licence: MIT License · rank 1968 · last release 2026-02-15 · [PyPI](https://pypi.org/project/python-keycloak/) · [docs](https://python-keycloak.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

python-keycloak is a Python package providing access to the Keycloak API.

Example:
```python
from keycloak import KeycloakOpenID

# Configure client
keycloak_openid = KeycloakOpenID(server_url="
                                 client_id="example_client",
                                 realm_name="example_realm",
                                 client_secret_key="secret")

# Get WellKnown
...
```

Sections: Python Keycloak, Bug reports, Documentation, Example of Using Keycloak OpenID, Example of Using Keycloak Admin API

</details>

### py-cpuinfo2

Get CPU info with pure Python

`pip install py-cpuinfo2` · installs (wheel) · licence: MIT · rank 2037 · last release 2026-03-25 · [PyPI](https://pypi.org/project/py-cpuinfo2/)

<details><summary>README extract</summary>

> This is a friendly drop-in fork of py-cpuinfo.

Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work without any
extra programs or libraries, beyond what your OS provides. It does not require
any compilation(C/C++, assembly, et cetera) to use. It works with Python 3.

Example ...

</details>

### flatten-dict

A flexible utility for flattening and unflattening dict-like objects in Python.

`pip install flatten-dict` · installs (wheel) · licence: MIT License · rank 2157 · last release 2026-04-28 · [PyPI](https://pypi.org/project/flatten-dict/) · [source](https://github.com/ianlini/flatten-dict)

<details><summary>README extract</summary>

A flexible utility for flattening and unflattening dict-like objects in Python.

This package provides a function `flatten()` for flattening dict-like objects in Python (tested with 3.10-3.15).
It also provides some key joining methods (reducer), and you can choose the reducer you want or even implement your own reducer. ...

Example:
```python
def flatten(d, reducer='tuple', inverse=False, enumerate_types=(), keep_empty_types=()):
    """Flatten `Mapping` object.

    Parameters

    d : dict-like object
        The dict that will be flattened.
    reducer : {'tuple', 'path', 'underscore', 'dot', Callable}
        The key joining method. If a `Callable` is given, the `Callable` will be
...
```

Sections: flatten-dict, Introduction, Documentation, Flatten, Unflatten

</details>

### easydict

Access dict values as attributes (works recursively).

`pip install easydict` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 2341 · last release 2024-03-04 · [PyPI](https://pypi.org/project/easydict/)

_README extract left out: share-alike licence._

### magic-filter

(no summary)

`pip install magic-filter` · installs (wheel) · licence: MIT License · rank 2443 · last release 2023-10-01 · [PyPI](https://pypi.org/project/magic-filter/) · [docs](https://docs.aiogram.dev/en/dev-3.x/dispatcher/filters/magic_filters.html) · [source](https://github.com/aiogram/magic-filter)

<details><summary>README extract</summary>

This package provides magic filter based on dynamic attribute getter

</details>

### python-jenkins

Python bindings for the remote Jenkins API

`pip install python-jenkins` · installs (wheel) · licence: BSD License · rank 2540 · last release 2025-08-03 · [PyPI](https://pypi.org/project/python-jenkins/) · [docs](https://python-jenkins.readthedocs.io/)

<details><summary>README extract</summary>

Python Jenkins is a python wrapper for the Jenkins
REST API which aims to provide a more conventionally pythonic way of controlling
a Jenkins server. It provides a higher-level API containing a number of
convenience functions.

We like to use python-jenkins to automate our Jenkins servers. Here are some of
the things you can use it for: ...

Sections: README, Writing a patch

</details>

### pytest-docker

Simple pytest fixtures for Docker and Docker Compose based tests

`pip install pytest-docker` · installs (wheel) · licence: MIT License · rank 2549 · last release 2026-10-16 · [PyPI](https://pypi.org/project/pytest-docker/)

<details><summary>README extract</summary>

Simple pytest fixtures that help you write integration
tests with Docker and Docker Compose.
Specify all necessary containers in a `docker-compose.yml` file and
`pytest-docker` will spin them up for the duration of your tests.

`pytest-docker` was originally created by André Caron.

Example:
```python
import pytest
import requests

from requests.exceptions import ConnectionError

def is_responsive(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except ConnectionError:
        return False

@pytest.fixture(scope="session")
def http_service(docker_ip, docker_services):
...
```

...

</details>

### pyzbar

Read one-dimensional barcodes and QR codes from Python 2 and 3.

`pip install pyzbar` · installs (wheel) · licence: MIT License · rank 2596 · last release 2022-03-15 · [PyPI](https://pypi.org/project/pyzbar/)

<details><summary>README extract</summary>

Read one-dimensional barcodes and QR codes from Python 2 and 3 using the
zbar library.

- Pure python
- Works with PIL / Pillow images, OpenCV / imageio / numpy `ndarray`\ s, and raw bytes
- Decodes locations of barcodes
- No dependencies, other than the zbar library itself
- Tested on Python 2.7, and Python 3.5 to 3.10 ...

Example:
```python
>>> from pyzbar.pyzbar import decode
>>> from PIL import Image
>>> decode(Image.open('pyzbar/tests/code128.png'))
[
    Decoded(
        data=b'Foramenifera', type='CODE128',
        rect=Rect(left=37, top=550, width=324, height=76),
        polygon=[
            Point(x=37, y=551), Point(x=37, y=625), Point(x=361, y=626),
...
```

Sections: pyzbar, Example usage, ZBar versions, Quality field, Bounding boxes and polygons, Windows error message

</details>

### asn1

Python-ASN1 is a simple ASN.1 encoder and decoder for Python 2.7+ and 3.5+.

`pip install asn1` · installs (wheel) · licence: MIT · rank 2781 · last release 2026-05-15 · [PyPI](https://pypi.org/project/asn1/)

<details><summary>README extract</summary>

Features:
Python-ASN1 is a simple ASN.1 encoder and decoder for Python 2.7 and 3.5+.

Example:
```python
import asn1

encoder = asn1.Encoder()
encoder.start()
encoder.write('1.2.3', asn1.Numbers.ObjectIdentifier)
encoded_bytes = encoder.output()
```

Sections: Overview, Features, Dependencies, How to use Python-asn1, Encoding, Decoding, Documentation, Copyright, 3.3.0 (2026-05-15), 3.2.0 (2026-02-06), 3.1.0 (2025-05-16), 3.0.1 (2025-05-02), 3.0.0 (2025-03-03), 2.8.0 (2025-02-20)

</details>

### appier

Appier Framework

`pip install appier` · installs (wheel) · licence: Apache Software License · rank 2814 · last release 2026-05-31 · [PyPI](https://pypi.org/project/appier/)

<details><summary>README extract</summary>

Joyful Python Web App development

Appier is an object-oriented Python web framework built for super fast app development.
It's as lightweight as possible, but not too lightweight.
It gives you the power of bigger frameworks, without their complexity.

Example:
```python
import appier

class HelloApp(appier.App):

    @appier.route("/", "GET")
    def hello(self):
        return "Hello World"

HelloApp().serve()
```

Sections: Appier, Usage, More

</details>

### google_api

Google API Client

`pip install google_api` · installs (wheel) · licence: Apache Software License · rank 2876 · last release 2017-09-05 · [PyPI](https://pypi.org/project/google_api/)

### sgqlc

Simple GraphQL Client

`pip install sgqlc` · installs (wheel) · licence: ISC License (ISCL) · rank 2933 · last release 2026-02-06 · [PyPI](https://pypi.org/project/sgqlc/) · [docs](https://sgqlc.readthedocs.io/) · [source](http://github.com/profusion/sgqlc)

<details><summary>README extract</summary>

This package offers an easy to use GraphQL
client. It's composed of the following modules:

- `sgqlc.types`: declare GraphQL in Python, base to generate and
 interpret queries. Submodule `sgqlc.types.datetime` will
 provide bindings for `datetime` and ISO 8601, while
 `sgqlc.types.relay` will expose `Node`, `PageInfo` and
 `Connection`. ...

Features:
Since we don't want to clobber GraphQL fields, we cannot provide
nicely named methods. Therefore we use overloaded methods such as
_iadd, _add, _bytes__ (compressed GraphQL
representation) and _str__ (indented GraphQL representation). ...

Example:
```python
from sgqlc.endpoint.http import HTTPEndpoint

url = '
headers = {'Authorization': 'bearer TOKEN'}

query = 'query { ... }'
variables = {'varName': 'value'}

...

</details>

### marshmallow-union

Union fields for marshmallow.

`pip install marshmallow-union` · installs (wheel) · licence: MIT License · rank 3046 · last release 2020-06-24 · [PyPI](https://pypi.org/project/marshmallow-union/)

<details><summary>README extract</summary>

Features:
Union fields for marshmallow.

* Free software: MIT license

Sections: Overview, Warning, Documentation, 0.1.15 (2020-05-30), Changes, 0.1.12 (2019-10-24), Backward-incompatible Changes, 0.1.11 (2019-06-19), 0.1.10 (2019-06-08), 0.1.0 (2019-06-07)

</details>

### python-vagrant

Python bindings for interacting with Vagrant virtual machines.

`pip install python-vagrant` · installs (wheel) · licence: MIT License · rank 3138 · last release 2022-03-31 · [PyPI](https://pypi.org/project/python-vagrant/) · [source](https://github.com/pycontribs/python-vagrant)

<details><summary>README extract</summary>

Python-vagrant is a python module that provides a _thin_ wrapper around the
`vagrant` command line executable, allowing programmatic control of Vagrant
virtual machines (boxes). This module is useful for:

- Starting a Vagrant virtual machine (VM) (`up`).
- Terminating a Vagrant VM (`destroy`). ...

Example:
```python
import vagrant
from fabric.api import env, execute, task, run

@task
def mytask():
    run('echo $USER')

v = vagrant.Vagrant()
v.up()
env.hosts = [v.user_hostname_port()]
env.key_filename = v.keyfile()
env.disable_known_hosts = True # useful for when the vagrant box ip changes.
execute(mytask) # run a fabric task on the vagrant host.
```

...

</details>

### PyScaffold

Template tool for putting up the scaffold of a Python project

`pip install PyScaffold` · installs (wheel) · licence: MIT License · rank 3304 · last release 2024-09-23 · [PyPI](https://pypi.org/project/PyScaffold/) · [docs](https://pyscaffold.org/) · [source](https://github.com/pyscaffold/pyscaffold/)

<details><summary>README extract</summary>

PyScaffold is a project generator for bootstrapping high quality Python
packages, ready to be shared on PyPI and installable via pip.
It is easy to use and encourages the adoption of the best tools and
practices of the Python ecosystem, helping you and your team
to stay sane, happy and productive. ...

Sections: Quickstart, Configuration & Packaging, Versioning and Git Integration, Sphinx Documentation, Automation, Tests & Coverage, Extensions, Easy Updating

</details>

### ruyaml

ruyaml is a fork of ruamel.yaml

`pip install ruyaml` · installs (wheel) · licence: MIT License · rank 3442 · last release 2021-12-07 · [PyPI](https://pypi.org/project/ruyaml/) · [source](https://github.com/pycontribs/ruyaml)

<details><summary>README extract</summary>

`ruyaml` package is a fork of `ruamel.yaml` aimed to made in order to
secure the future of the library, mainly by having a pool of maintainers.

- The current version has the same API as the "ruamel.yaml" package.
 However, it will install the `ruyaml` python module. ...

Sections: ruyaml, Notes

</details>

### strip-hints

Function and command-line program to strip Python type hints.

`pip install strip-hints` · installs (wheel) · licence: MIT · rank 3458 · last release 2026-10-11 · [PyPI](https://pypi.org/project/strip-hints/)

<details><summary>README extract</summary>

This package provides a command-line command and a corresponding importable
function that strips type hints from Python code files. The stripping process
leaves runnable code, assuming the rest of the code is runnable in the
interpreter version. ...

Example:
```python
from strip_hints import strip_on_import
strip_on_import(file, to_empty=False, strip_nl=False, no_ast=False,
                no_colon_move=False, no_equal_move=False,
                only_assigns_and_defs=False, py3_also=True,
                keep_class_annotations=None, legacy_output=False)
```

Sections: strip-hints, Running the code, Dataclasses and similar classes, Disabling for sections of code, Automatically running on import, Calling from a Python program, Limitations, How it works

</details>

### trailrunner

Run things on paths

`pip install trailrunner` · installs (wheel) · licence: MIT License · rank 3463 · last release 2023-03-27 · [PyPI](https://pypi.org/project/trailrunner/) · [source](https://github.com/omnilib/trailrunner)

<details><summary>README extract</summary>

Walk paths and run things

trailrunner is a simple library for walking paths on the filesystem, and executing
functions for each file found. trailrunner obeys project level `.gitignore` files,
and runs functions on a process pool for increased performance. ...

Example:
```python
>>> from trailrunner import walk
>>> sorted(walk(Path("trailrunner")))
[
    PosixPath('trailrunner/init.py'),
    PosixPath('trailrunner/version.py'),
    PosixPath('trailrunner/core.py'),
    PosixPath('trailrunner/tests/init.py'),
    PosixPath('trailrunner/tests/main.py'),
    PosixPath('trailrunner/tests/core.py'),
]
```

</details>

### django-admin-rangefilter

django-admin-rangefilter app, add the filter by a custom date range on the admin UI.

`pip install django-admin-rangefilter` · installs (wheel) · licence: MIT License · rank 3494 · last release 2026-08-28 · [PyPI](https://pypi.org/project/django-admin-rangefilter/)

<details><summary>README extract</summary>

A Django app that adds a filter by date range and numeric range to the admin UI.

* Python 3.6+
* Django 1.11+

Example:
```python
from datetime import datetime

from django.contrib import admin
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = (
...
```

Sections: django-admin-rangefilter, Requirements, Example usage, In admin

</details>

### google-search-results

Scrape and search localized results from Google, Bing, Baidu, Yahoo, Yandex, Ebay, Homedepot, youtube at scale using SerpApi.com

`pip install google-search-results` · installs from source (sdist only) · licence: MIT License · rank 3514 · last release 2023-03-10 · [PyPI](https://pypi.org/project/google-search-results/)

<details><summary>README extract</summary>

This Python package is meant to scrape and parse search results from Google, Bing, Baidu, Yandex, Yahoo, Home Depot, eBay and more, using SerpApi.

The following services are provided:
- Search API
- Search Archive API
- Account API
- Location API (Google Only)

SerpApi provides a script builder to get you started quickly.

Example:
```python
from serpapi import GoogleSearch
search = GoogleSearch({
    "q": "coffee",
    "location": "Austin,Texas",
    "api_key": "<your secret api key>"
  })
result = search.get_dict()
```

Sections: Google Search Results in Python, Quick start, Summary, Google Search API capability, How to set SERP API key, Example by specification, Location API, Search Archive API, Account API, Search Bing, Search Baidu, Search Yandex, Search Yahoo, Search eBay

</details>

### stdlibs

List of packages in the stdlib

`pip install stdlibs` · installs (wheel) · licence: MIT · rank 3574 · last release 2026-09-03 · [PyPI](https://pypi.org/project/stdlibs/) · [docs](https://stdlibs.omnilib.dev/en/latest/) · [source](https://github.com/omnilib/stdlibs)

<details><summary>README extract</summary>

Simple list of top-level packages in Python's standard library

This package provides a static listing of all known modules in the Python standard
library, with separate lists available for each major release dating back to Python 2.3. ...

Example:
```python
>>> from stdlibs import module_names
>>> print("os" in module_names)
True
>>> print("zoneinfo" in module_names)  # 3.9+
True
```

</details>

### amazon-textract-response-parser

Easily parse JSON returned by Amazon Textract.

`pip install amazon-textract-response-parser` · installs (wheel) · licence: Apache Software License · rank 3632 · last release 2024-06-13 · [PyPI](https://pypi.org/project/amazon-textract-response-parser/)

<details><summary>README extract</summary>

You can use Textract response parser library to easily parser JSON returned by Amazon Textract. Library parses JSON and provides programming language specific constructs to work with different parts of the document. ...

Example:
```python
# j holds the Textract JSON dict
from trp.trp2 import TDocument, TDocumentSchema
t_doc = TDocumentSchema().load(j)
```

Sections: Textract Response Parser, Pipeline and Serializer/Deserializer, Serializer/Deserializer, Deserialize Textract JSON, Serialize Textract, Deserialize Textract AnalyzeId JSON, Serialize Textract AnalyzeId object to JSON, Pipeline, Page orientation in degrees, Using the pipeline on command line, Merge or link tables across pages, Add OCR confidence score to KEY and VALUE, Parse JSON response from Textract, Test

</details>

### fancycompleter

colorful TAB completion for Python prompt

`pip install fancycompleter` · installs (wheel) · licence: BSD License · rank 3696 · last release 2025-05-26 · [PyPI](https://pypi.org/project/fancycompleter/)

<details><summary>README extract</summary>

`fancycompleter` is a module to improve your experience in Python by
adding TAB completion to the interactive prompt. It is an extension of
the stdlib's rlcompleter module.

Its best feature is that the completions are displayed in different
colors, depending on their type: ...

Sections: fancycompleter: colorful Python TAB completion, What is is?, Other features, How do I get colors?, Customization, What is really going on?

</details>

### praw

Python Reddit API Wrapper.

`pip install praw` · installs (wheel) · licence: BSD License · rank 3734 · last release 2026-08-12 · [PyPI](https://pypi.org/project/praw/) · [docs](https://praw.readthedocs.io/) · [source](https://github.com/praw-dev/praw)

<details><summary>README extract</summary>

PRAW, an acronym for "Python Reddit API Wrapper", is a Python package that allows for
simple access to Reddit's API. PRAW aims to be easy to use and internally follows all of
Reddit's API rules. With PRAW there's no
need to introduce `sleep` calls in your code. Give your client an appropriate user
agent and you're set.

Example:
```python
import praw

reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    password="PASSWORD",
    user_agent="USERAGENT",
    username="USERNAME",
)
```

Sections: PRAW: The Python Reddit API Wrapper, Quickstart, Discord Bots and Asynchronous Environments, Documentation

</details>

### ufmt

Safe, atomic formatting with black and µsort

`pip install ufmt` · installs (wheel) · licence: MIT License · rank 3784 · last release 2026-02-08 · [PyPI](https://pypi.org/project/ufmt/) · [docs](https://ufmt.omnilib.dev) · [source](https://github.com/omnilib/ufmt)

<details><summary>README extract</summary>

Safe, atomic formatting with black and µsort

µfmt is a safe, atomic code formatter for Python built on top of black and µsort:

> Black makes code review faster by producing the smallest diffs possible. Blackened code looks the same regardless of the project you’re reading.

> μsort is a safe, minimal import sorter. ...

Sections: µfmt, GitHub Actions, pre-commit hook, Visual Studio Code

</details>

### git-remote-codecommit

Git remote prefix to simplify pushing to and pulling from CodeCommit.

`pip install git-remote-codecommit` · installs from source (sdist only) · licence: Apache Software License · rank 3811 · last release 2023-08-25 · [PyPI](https://pypi.org/project/git-remote-codecommit/)

<details><summary>README extract</summary>

This package provides a simple method for pushing and pulling from AWS
CodeCommit. This package extends git to support repository URLs prefixed with
codecommit://. For example, if using IAM...

... you can clone repositories as simply as...

The *git-remote-codecommit* package works on Python versions:

* 3.8.x
* 3.9.x
* 3.10.x
* 3.11.x

Sections: git-remote-codecommit, Prerequisites, Set Up, Step 1: Look Up Your AWS Account ID and IAM User Access Key, Step 4: Clone your repository, Usage, Getting Help

</details>

### paddleocr

Awesome multilingual OCR and document parsing toolkits based on PaddlePaddle

`pip install paddleocr` · installs (wheel) · licence: Apache License 2.0 · rank 3824 · last release 2026-06-11 · [PyPI](https://pypi.org/project/paddleocr/) · [docs](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md) · [source](https://github.com/PaddlePaddle/PaddleOCR.git)

<details><summary>README extract</summary>

English | 简体中文 | 繁體中文 | 日本語 | 한국어 | Français | Русский | Español | العربية

PaddleOCR converts PDF documents and images into structured, LLM-ready data (JSON/Markdown) with industry-leading accuracy. ...

Sections: Global Leading OCR Toolkit & Document AI Engine, 🚀 Key Features, 📄 Intelligent Document Parsing (LLM-Ready), 🔍 Universal Text Recognition (Scene OCR), 📣 Recent updates, 🚀 Quick Start, Step 1: Try Online, Step 2: Local Deployment, 🧩 More Features, 🔄 Quick Overview of Execution Results, PP-OCRv5, PP-StructureV3, PaddleOCR-VL, ✨ Stay Tuned

</details>

### docker-py

Python client for Docker.

`pip install docker-py` · installs (wheel) · licence: Apache Software License · rank 3829 · last release 2016-11-02 · [PyPI](https://pypi.org/project/docker-py/)

<details><summary>README extract</summary>

A Python library for the Docker Remote API. It does everything the
`docker` command does, but from within Python – run containers, manage
them, pull/push images, etc.

Sections: docker-py, Documentation

</details>

### amazon-textract-caller

Amazon Textract Caller tools

`pip install amazon-textract-caller` · installs (wheel) · licence: Apache Software License · rank 3855 · last release 2024-06-20 · [PyPI](https://pypi.org/project/amazon-textract-caller/)

<details><summary>README extract</summary>

amazon-textract-caller provides a collection of ready to use functions and sample implementations to speed up the evaluation and development for any project using Amazon Textract.

Making it easy to call Amazon Textract regardless of file type and location.

Example:
```python
from textractcaller import call_textract
def call_textract(input_document: Union[str, bytes],
                  features: Optional[List[Textract_Features]] = None,
                  queries_config: Optional[QueriesConfig] = None,
                  output_config: Optional[OutputConfig] = None,
...
```

Sections: Textract-Caller, Functions, Samples, Call with images located on S3 but force asynchronous API, Call with OutputConfig, Customer-Managed-Key

</details>

### django-constance

Django live settings with pluggable backends, including Redis.

`pip install django-constance` · installs (wheel) · licence: BSD License · rank 4041 · last release 2026-10-28 · [PyPI](https://pypi.org/project/django-constance/) · [docs](https://django-constance.readthedocs.io/en/latest/) · [source](https://github.com/django-commons/django-constance/)

<details><summary>README extract</summary>

A Django app for storing dynamic settings in pluggable backends (Redis and
Django model backend built in) with an integration with the Django admin app.

For more information see the documentation at:

If you have questions or have trouble using the app please file a bug report
at:

</details>

### timeago

A very simple python library, used to format datetime with `*** time ago` statement. eg: "3 hours ago".

`pip install timeago` · installs (wheel) · licence: MIT · rank 4054 · last release 2022-08-18 · [PyPI](https://pypi.org/project/timeago/)

<details><summary>README extract</summary>

A very simple python lib, used to format datetime with `*** time ago`
statement. Javascript version here. timeago.js.

Such as:

For other languages see below.

Example:
```python
# -*- coding: utf-8 -*-
import timeago, datetime

now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)

date = datetime.datetime.now()

# locale
print (timeago.format(date, now, 'zh_CN')) # will print `3分钟前`

# input datetime
print (timeago.format(date, now)) # will print 3 minutes ago

# input timedelta
...
```

Sections: timeago, Usage & Example, Method & Parameter, Locale, Localization, Notes

</details>

### yamlfix

A simple opionated yaml formatter that keeps your comments!

`pip install yamlfix` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 4093 · last release 2025-12-18 · [PyPI](https://pypi.org/project/yamlfix/) · [docs](https://lyz-code.github.io/yamlfix)

_README extract left out: share-alike licence._

### rlPyCairo

Plugin backend renderer for reportlab.graphics.renderPM

`pip install rlPyCairo` · installs (wheel) · licence: BSD License · rank 4130 · last release 2025-08-15 · [PyPI](https://pypi.org/project/rlPyCairo/)

<details><summary>README extract</summary>

=====================================

(C) Copyright ReportLab Europe Ltd. 2000-2021.
See ``LICENSE.txt`` for license details.

This is a plugin for the ReportLab PDF Toolkit.
which constructs rich PDF documents, and also creation
of charts in a variety of bitmap and vector formats. ...

Sections: README, 1. Licensing, 3. Prerequisites / Dependencies, 4. Documentation, 5. Test suite, 5.1 Building

</details>

### python-redis-lock

Lock context manager implemented via redis SETNX/BLPOP.

`pip install python-redis-lock` · installs (wheel) · licence: BSD-2-Clause · rank 4381 · last release 2026-04-08 · [PyPI](https://pypi.org/project/python-redis-lock/) · [docs](https://python-redis-lock.readthedocs.io/)

<details><summary>README extract</summary>

Features:
Lock context manager implemented via redis SETNX/BLPOP.

* Free software: BSD 2-Clause License

Interface targeted to be exactly like threading.Lock.

Example:
```python
from redis import Redis
conn = Redis()

import redis_lock
lock = redis_lock.Lock(conn, "name-of-the-lock")
if lock.acquire(blocking=False):
    print("Got the lock.")
    lock.release()
else:
    print("Someone else has the lock.")
```

Sections: Overview, Usage, Locks as Context Managers, Avoid dogpile effect in django, Troubleshooting, Features, Implementation, Documentation, Requirements, Similar projects, v4.0.1 (2026-04-08), v4.0.0 (2022-10-17), v3.7.0 (2020-11-20), v3.6.0 (2020-07-23)

</details>

### pyrepl

A library for building flexible command line interfaces

`pip install pyrepl` · installs (wheel) · licence: BSD License · rank 4389 · last release 2026-08-02 · [PyPI](https://pypi.org/project/pyrepl/)

<details><summary>README extract</summary>

This is `pyrepl`, a readline-a-like in pure Python.

It requires python 3.8 (or newer) and features:

- sane multi-line editing
- history, with incremental search
- completion, including displaying of available options
- a fairly large subset of the readline emacs-mode keybindings
 (adding more is mostly just a matter of typing) ...

</details>

### bsdiff4

binary diff and patch using the BSDIFF4-format

`pip install bsdiff4` · installs (wheel) · licence: BSD · rank 4549 · last release 2026-11-04 · [PyPI](https://pypi.org/project/bsdiff4/)

<details><summary>README extract</summary>

The code is mostly derived from `cx_bsdiff` (written by Anthony Tuininga,
 The `cx_bsdiff` code in turn was
derived from bsdiff, the standalone utility produced for BSD which can be
found at

Key features of this package include: ...

Example:
```python
>>> import bsdiff4
>>> a = 100_000 * b'a'
>>> b = bytearray(a)
>>> b[100:106] = b' diff '
>>> p = bsdiff4.diff(a, bytes(b))
>>> len(p)
154
>>> bsdiff4.patch(a, p) == b
True
```

</details>

### json-numpy

JSON encoding/decoding for Numpy arrays and scalars

`pip install json-numpy` · installs (wheel) · licence: MIT License · rank 4567 · last release 2025-06-30 · [PyPI](https://pypi.org/project/json-numpy/) · [source](https://github.com/Crimson-Crow/json-numpy.git)

<details><summary>README extract</summary>

Description

`json-numpy` provides lossless and quick JSON encoding/decoding for NumPy arrays and scalars.

`json-numpy` follows Semantic Versioning.

Installation

`json-numpy` can be installed using `pip`:

 $ pip install json-numpy

Usage

For a quick start, `json_numpy` can be used as a simple drop-in replacement of the built-in `json` module. ...

Example:
```python
import numpy as np
import json_numpy

arr = np.array([0, 1, 2])
encoded_arr_str = json_numpy.dumps(arr)
decoded_arr = json_numpy.loads(encoded_arr_str)
```

</details>

### ExifRead

Library to extract Exif information from digital camera image files.

`pip install ExifRead` · installs (wheel) · licence: not stated · rank 4709 · last release 2025-08-23 · [PyPI](https://pypi.org/project/ExifRead/) · [source](https://github.com/ianare/exif-py)

<details><summary>README extract</summary>

Easy to use Python module to extract Exif metadata from digital image files.

Pure Python, lightweight, no dependencies.

Supported formats: TIFF, JPEG, JPEG XL, PNG, Webp, HEIC, RAW

EXIF.py is tested and officially supported on Python 3.7 to 3.13

Example:
```python
import exifread
from PIL import Image
import logging

def _read_img_and_correct_exif_orientation(path):
    im = Image.open(path)
    tags = {}
    with open(path, "rb") as file_handle:
        tags = exifread.process_file(file_handle, details=False)

    if "Image Orientation" in tags:
        orientation = tags["Image Orientation"]
...
```

...

</details>

### cloudwatch

A small handler for AWS Cloudwatch

`pip install cloudwatch` · installs (wheel) · licence: MIT License · rank 4719 · last release 2023-09-01 · [PyPI](https://pypi.org/project/cloudwatch/)

<details><summary>README extract</summary>

This small log handler is designed to send events to AWS Cloudwatch. It is useful when operating infrastructure outside of the AWS, when AWS does not log automatically (EC2) or when you want to separate logs. If you are logging on Serverless Infrastructure (e.g. ...

Example:
```python
import logging
# Create the logger
logger = logging.getLogger('my_logger')
# Create the formatter
formatter = logging.Formatter('%(asctime)s : %(levelname)s - %(message)s')

# Import cloudwath and create the new handler
from cloudwatch import cloudwatch
handler = cloudwatch.CloudwatchHandler(log_group = 'my_log_group')

...
```

Sections: AWS Cloudwatch Lightweight Handler, Usage, Credentials, Specifying credentials and region, Specifying log stream, Overflow

</details>

### remote-pdb

Remote vanilla PDB (over TCP sockets) *done right*: no extras, proper handling around connection failures and CI. Based on `pdbx <https://pypi.python.org/pypi/pdbx>`_.

`pip install remote-pdb` · installs (wheel) · licence: BSD License · rank 4890 · last release 2020-07-24 · [PyPI](https://pypi.org/project/remote-pdb/) · [docs](https://python-remote-pdb.readthedocs.io/)

<details><summary>README extract</summary>

Features:
Remote vanilla PDB (over TCP sockets) *done right*: no extras, proper handling around connection failures and CI. Based
on pdbx.

* Free software: BSD 2-Clause License

Example:
```python
from remote_pdb import set_trace
set_trace() # you'll see the port number in the logs
```

Sections: Overview, Usage, Using in containers, Integration with breakpoint() in Python 3.7+, Note about OS X, Requirements, Similar projects, 2.1.0 (2020-07-24), 2.0.0 (2019-07-31), 1.3.0 (2019-03-13), 1.2.0 (2015-09-26), 1.1.3 (2015-07-06), 1.1.2 (2015-07-06), 1.1.1 (2015-07-06)

</details>

### smbus2

smbus2 is a drop-in replacement for smbus-cffi/smbus-python in pure Python

`pip install smbus2` · installs (wheel) · licence: MIT License · rank 5032 · last release 2026-04-09 · [PyPI](https://pypi.org/project/smbus2/)

<details><summary>README extract</summary>

A drop-in replacement for smbus-cffi/smbus-python in pure Python

smbus2 is a pure Python, drop-in replacement for the `python-smbus` / `python3-smbus` Linux SMBus bindings.

It was designed with two goals in mind:

1. Provide an interface that is familiar to users of `smbus`.
2. ...

Example:
```python
from smbus2 import SMBus

# Open i2c bus 1 and read one byte from address 80, offset 0
bus = SMBus(1)
b = bus.read_byte_data(80, 0)
print(b)
bus.close()
```

...

</details>

### enlighten

Enlighten Progress Bar

`pip install enlighten` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 5133 · last release 2025-03-10 · [PyPI](https://pypi.org/project/enlighten/) · [docs](https://python-enlighten.readthedocs.io)

<details><summary>README extract</summary>

docsgh_actionscodecov|
linuxwindowsmacbsd|
pypisupported-versionssupported-implementations|
FedoraEPELDebianUbuntuAnaconda|
Python-Bytes|

Features:
Enlighten Progress Bar is a console progress bar library for Python.

The main advantage of Enlighten is it allows writing to stdout and stderr without any
redirection or additional code. Just print or log as you normally would. ...

Example:
```python
import enlighten
manager = enlighten.get_manager()
```

Sections: Overview, Documentation, PIP, RPM, Fedora and EL8 (RHEL/CentOS), DEB, Debian and Ubuntu, Conda, How to Use, Managers, Progress Bars, Counters, Color, Multicolored

</details>

### posix-ipc

POSIX IPC primitives (semaphores, shared memory and message queues) for Python

`pip install posix-ipc` · installs from source (sdist only) · licence: BSD-3-Clause · rank 5237 · last release 2025-10-23 · [PyPI](https://pypi.org/project/posix-ipc/)

<details><summary>README extract</summary>

`posix_ipc` is a Python module (written in C) that permits creation and manipulation of POSIX inter-process semaphores, shared memory and message queues on platforms supporting the POSIX Realtime Extensions a.k.a. POSIX 1003.1b-1993. This includes nearly all Unices, and Windows + Cygwin ≥ 1.7.

For complete documentation, see the usage notes. ...

Sections: POSIX IPC, Tests, Related

</details>

### codeguru-profiler-agent

The Python agent to be used for Amazon CodeGuru Profiler

`pip install codeguru-profiler-agent` · installs (wheel) · licence: Apache Software License · rank 5349 · last release 2025-12-11 · [PyPI](https://pypi.org/project/codeguru-profiler-agent/)

<details><summary>README extract</summary>

For more details, check the documentation:

Sections: Amazon CodeGuru Profiler Python Agent, How to use it

</details>

### django-cleanup

Deletes old files.

`pip install django-cleanup` · installs (wheel) · licence: MIT License · rank 5432 · last release 2024-09-18 · [PyPI](https://pypi.org/project/django-cleanup/)

<details><summary>README extract</summary>

Features:
The django-cleanup app automatically deletes files for FileField, ImageField and
subclasses. When a FileField's value is changed and the model is saved, the old file is
deleted. When a model that has a FileField is deleted, the file is also deleted. ...

Example:
```python
from django.apps import apps
apps.get_models()
```

Sections: Django Cleanup, Features, Compatibility, How does it work?, Configuration, Troubleshooting, Known limitations, File referenced by multiple model instances, Advanced, Signals, Refresh the cache, Ignore cleanup for a specific model, Only cleanup selected models, How to run tests

</details>

### jc

Converts the output of popular command-line tools and file-types to JSON.

`pip install jc` · installs (wheel) · licence: MIT License · rank 5434 · last release 2026-10-29 · [PyPI](https://pypi.org/project/jc/)

<details><summary>README extract</summary>

> Check out the `jc` Python package documentation for developers

> Try the `jc` web demo and REST API

> `jc` is available as an
Ansible filter plugin
in the `community.general` collection. See this
blog post
for an example.

JSON Convert

`jc` JSONifies the output of many CLI tools, file-types, and common strings
for easier parsing in scripts. ...

Features:
For more information on the motivations for this project, please see my blog
post on Bringing the Unix Philosophy to the 21st Century and my interview with Console.

See also:
- libxo on FreeBSD
- powershell ...

Example:
```python
>>> import subprocess
>>> import jc
>>>
>>> cmd_output = subprocess.check_output(['dig', 'example.com'], text=True)
>>> data = jc.parse('dig', cmd_output)
>>>
>>> data0
...

</details>

### f90nml

Fortran 90 namelist parser

`pip install f90nml` · installs (wheel) · licence: Apache Software License · rank 5826 · last release 2025-10-07 · [PyPI](https://pypi.org/project/f90nml/)

<details><summary>README extract</summary>

A Python module and command line tool for parsing Fortran namelist files

The documentation for `f90nml` is available from Read The Docs.

`f90nml` is a Python module and command line tool that provides a simple
interface for the reading, writing, and modifying Fortran namelist files. ...

Example:
```python
import f90nml
nml = f90nml.read('sample.nml')
```

Sections: f90nml - A Fortran namelist parser, generator, and editor, Documentation, About f90nml, Quick usage guide, Command line interface, conda, Package distribution

</details>

### requestsexceptions

Import exceptions from potentially bundled packages in requests.

`pip install requestsexceptions` · installs (wheel) · licence: Apache Software License · rank 5830 · last release 2018-02-01 · [PyPI](https://pypi.org/project/requestsexceptions/)

<details><summary>README extract</summary>

The python requests library bundles the urllib3 library, however, some
software distributions modify requests to remove the bundled library.
This makes some operations, such as supressing the "insecure platform
warning" messages that urllib emits difficult. ...

</details>

### google-cloud-sqlcommenter

Augment SQL statements with meta information about frameworks and the running environment.

`pip install google-cloud-sqlcommenter` · installs (wheel) · licence: BSD License · rank 5833 · last release 2021-08-18 · [PyPI](https://pypi.org/project/google-cloud-sqlcommenter/)

<details><summary>README extract</summary>

Python modules for popular projects that add meta info to your SQL queries as comments.

 * Django
 * SQLAlchemy
 * Psycopg2

Example:
```python
import sqlalchemy
from google.cloud.sqlcommenter.sqlalchemy.executor import BeforeExecuteFactory

engine = sqlalchemy.create_engine(...)
listener = BeforeExecuteFactory(
    with_db_driver=True,
    with_db_framework=True,
    # you may use one of opencensus or opentelemetry
    with_opencensus=True,
    with_opentelemetry=True,
)
...
```

Sections: sqlcommenter, Usage, Django, SQLAlchemy, Psycopg2, Options, [1] `opencensus`, [2] `opentelemetry`, [3] `traceparent/tracestate`

</details>

### ansicon

Python wrapper for loading Jason Hood's ANSICON

`pip install ansicon` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 5849 · last release 2019-04-29 · [PyPI](https://pypi.org/project/ansicon/)

<details><summary>README extract</summary>

appveyorcodecov|
pypisupported-versionssupported-implementations|

Features:
ansicon is a Python wrapper for loading Jason Hood's ANSICON

Example:
```python
import ansicon

# Load ansicon
ansicon.load()

# Have fun with terminal codes
print(u'\x1b[32mGreen\x1b[m')

# Unload ansicon
ansicon.unload()

# Check if ansicon is loaded
if not ansicon.loaded():
    ansicon.load()
if ansicon.loaded():
    ansicon.unload()
```

Sections: Overview, Usage

</details>

### pymupdf-fonts

Collection of font binaries for use in PyMuPDF

`pip install pymupdf-fonts` · installs (wheel) · licence: SIL OFL V1.1 · rank 5982 · last release 2021-12-27 · [PyPI](https://pypi.org/project/pymupdf-fonts/) · [docs](https://pymupdf.readthedocs.io/en/latest/font.html)

<details><summary>README extract</summary>

Collection of optional fonts for PyMuPDF

Release date: December 27, 2021

Example:
```python
page.insert_font(fontname="F0", fontbuffer=font.buffer)
page.insert_text(point, text, fontname="F0", ...)
# or similarly:
page.insert_textbox(rect, text, fontname="F0", ...)
```

Sections: pymupdf-fonts, Introduction, Usage and Documentation

</details>

### jupyter-nbextensions-configurator

jupyter serverextension providing configuration interfaces for nbextensions.

`pip install jupyter-nbextensions-configurator` · installs (wheel) · licence: BSD License · rank 6136 · last release 2024-06-05 · [PyPI](https://pypi.org/project/jupyter-nbextensions-configurator/)

<details><summary>README extract</summary>

The jupyter_nbextensions_configurator jupyter server extension provides
graphical user interfaces for configuring which nbextensions are enabled (load
automatically for every notebook), and display their readme files. ...

</details>

### checksumdir

Compute a single hash of the file contents of a directory.

`pip install checksumdir` · installs (wheel) · licence: MIT License · rank 6159 · last release 2025-08-15 · [PyPI](https://pypi.org/project/checksumdir/)

<details><summary>README extract</summary>

A simple module for creating a single hash for a directory of files, with file contents;
ignoring any metadata such as file name. Options exist to also exclude specific files
or files with specific extensions.

Example:
```python
from checksumdir import dirhash

directory  = '/path/to/directory/'
md5hash    = dirhash(directory, 'md5')
sha1hash   = dirhash(directory, 'sha1', excluded_files=['package.json'])
sha256hash = dirhash(directory, 'sha256', excluded_extensions=['pyc'])
```

Sections: Checksumdir, Usage

</details>

### exrex

Irregular methods for regular expressions

`pip install exrex` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 6198 · last release 2024-11-13 · [PyPI](https://pypi.org/project/exrex/)

_README extract left out: share-alike licence._

### jupyter-contrib-nbextensions

A collection of Jupyter nbextensions.

`pip install jupyter-contrib-nbextensions` · installs from source (sdist only) · licence: BSD License · rank 6304 · last release 2022-11-15 · [PyPI](https://pypi.org/project/jupyter-contrib-nbextensions/)

<details><summary>README extract</summary>

Contains a collection of extensions that add functionality to the Jupyter
notebook. These extensions are mostly written in Javascript, and are loaded
locally in the browser.

Read
`the documentation <
for more information. ...

</details>

### pyclean

Pure Python cross-platform pyclean. Clean up your Python bytecode.

`pip install pyclean` · installs (wheel) · licence: GPL-3.0-or-later · rank 6321 · last release 2026-05-23 · [PyPI](https://pypi.org/project/pyclean/)

_README extract left out: share-alike licence._

### jupyter-contrib-core

Common utilities for jupyter-contrib projects.

`pip install jupyter-contrib-core` · installs from source (sdist only) · licence: BSD License · rank 6365 · last release 2022-11-15 · [PyPI](https://pypi.org/project/jupyter-contrib-core/)

<details><summary>README extract</summary>

Common utilities for jupyter-contrib projects. Includes:

- providing a notebook-4.2-compatible nbextension API in order to
 smooth over differences in versions 4.0 and 4.1
- common application components and cli scripts
- utility classes and functions for use in tests

</details>

### pilkit

A collection of utilities and processors for the Python Imaging Library.

`pip install pilkit` · installs (wheel) · licence: BSD License · rank 6384 · last release 2023-09-27 · [PyPI](https://pypi.org/project/pilkit/)

<details><summary>README extract</summary>

PILKit is a collection of utilities for working with PIL (the Python Imaging
Library).

One of its main features is a set of processors which expose a simple
interface for performing manipulations on PIL images.

Looking for more advanced processors? Check out Instakit! ...

Example:
```python
from pilkit.processors import ResizeToFit

img = Image.open('/path/to/my/image.png')
processor = ResizeToFit(100, 100)
new_img = processor.process(img)
```

Sections: Usage Overview, Processors, Utilities, imagekit channel on Freenode. (Both of

</details>

### django-imagekit

Automated image processing for Django models.

`pip install django-imagekit` · installs (wheel) · licence: BSD-3-Clause · rank 6413 · last release 2026-09-15 · [PyPI](https://pypi.org/project/django-imagekit/)

<details><summary>README extract</summary>

ImageKit is a Django app for processing images. Need a thumbnail? A
black-and-white version of a user-uploaded image? ImageKit will make them for
you. If you need to programmatically generate one image from another, you need
ImageKit. ...

Example:
```python
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars')
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(100, 50)],
...
```

...

</details>

### apkutils2

Utils for parsing apk.

`pip install apkutils2` · installs from source (sdist only) · licence: MIT License · rank 6417 · last release 2019-07-31 · [PyPI](https://pypi.org/project/apkutils2/)

### django-configurations

A helper for organizing Django settings.

`pip install django-configurations` · installs (wheel) · licence: BSD License · rank 6429 · last release 2024-03-27 · [PyPI](https://pypi.org/project/django-configurations/) · [source](https://github.com/jazzband/django-configurations)

<details><summary>README extract</summary>

django-configurations eases Django project configuration by relying
on the composability of Python classes. It extends the notion of
Django's module based settings loading with well established
object oriented programming patterns.

Check out the documentation for more complete examples.

Example:
```python
# mysite/settings.py

from configurations import Configuration

class Dev(Configuration):
    DEBUG = True
```

Sections: django-configurations, Quickstart

</details>

### jsonformatter

Python log in json format.

`pip install jsonformatter` · installs from source (sdist only) · licence: BSD License · rank 6436 · last release 2024-11-21 · [PyPI](https://pypi.org/project/jsonformatter/)

<details><summary>README extract</summary>

- jsonformatter -- for python log json
 - Installation
 - Contributing
 - Basic Usage
 - Case 1. Initial root logger like `logging.basicConfig`
 - Case 2. Complete config in python code
 - Case 3. Use config file
 - Case 4. In `Flask` project, add `LogRecord` attribute for auto output
 - Case 5. ...

Example:
```python
import logging

from jsonformatter import basicConfig

# default keyword parameter `format`: """{"levelname": "levelname", "name": "name", "message": "message"}"""
basicConfig(level=logging.INFO)
logging.info('hello, jsonformatter')
```

...

</details>

### cigam

magic

`pip install cigam` · installs (wheel) · licence: MIT License · rank 6444 · last release 2018-03-21 · [PyPI](https://pypi.org/project/cigam/)

### pyimg4

A Python library/CLI tool for parsing Apple's Image4 format.

`pip install pyimg4` · installs (wheel) · licence: not stated · rank 6569 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pyimg4/) · [source](https://github.com/m1stadev/PyIMG4)

<details><summary>README extract</summary>

A Python library/CLI tool for parsing Apple's Image4 format.

Sections: PyIMG4, Usage, Requirements, Notes

</details>

### s3torchconnectorclient

Internal S3 client implementation for s3torchconnector

`pip install s3torchconnectorclient` · installs (wheel) · licence: BSD License · rank 6599 · last release 2026-02-20 · [PyPI](https://pypi.org/project/s3torchconnectorclient/)

<details><summary>README extract</summary>

The Amazon S3 Connector for PyTorch delivers high throughput for PyTorch training jobs that access or store data in
Amazon S3. Using the S3 Connector for PyTorch
automatically optimizes performance when downloading training data from and writing checkpoints to Amazon S3,
eliminating the need to write your own code to list S3 buckets and manage ...

Features:
Amazon S3 Connector for PyTorch provides robust support for PyTorch distributed checkpoints. This feature includes:

- `S3StorageWriter`: Implementation of PyTorch's StorageWriter interface. ...

Example:
```python
from s3torchconnector import S3MapDataset, S3IterableDataset

# You need to update <BUCKET> and <PREFIX>
DATASET_URI="s3://<BUCKET>/<PREFIX>"
REGION = "us-east-1"

...

</details>

### pycosat

bindings to picosat (a SAT solver)

`pip install pycosat` · installs from source (sdist only) · licence: MIT · rank 6621 · last release 2023-10-03 · [PyPI](https://pypi.org/project/pycosat/)

<details><summary>README extract</summary>

PicoSAT is a popular
SAT solver
written by Armin Biere in pure C.
This package provides efficient Python bindings to picosat on the C level,
i.e. when importing pycosat, the picosat solver becomes part of the
Python process itself. For ease of deployment, the picosat source (namely
picosat.c and picosat.h) is included in this project. ...

Example:
```python
>>> import pycosat
>>> cnf = [[1, -5, 4], [-1, 5, 3, 4], [-3, -4]]
>>> pycosat.solve(cnf)
[1, -2, -3, -4, 5]
```

Sections: pycosat: bindings to picosat (a SAT solver), Usage, Example, Implementation of itersolve

</details>

### yamlordereddictloader

YAML loader and dumper for PyYAML allowing to keep keys order.

`pip install yamlordereddictloader` · installs (wheel) · licence: MIT License · rank 6637 · last release 2023-09-22 · [PyPI](https://pypi.org/project/yamlordereddictloader/)

<details><summary>README extract</summary>

DEPRECATED: the Phynix/yamlloader **project
provide an improved version of this library with unit tests, performance improvements
(by providing access to the C implementation of PyYAML) and is more actively developed.
You should use it!** ...

Example:
```python
import yaml
import yamlordereddictloader

data = yaml.load(open('myfile.yml'), Loader=yamlordereddictloader.Loader)
```

Sections: python-yamlordereddictloader, Loader usage, Dumper usage

</details>

### s3torchconnector

S3 connector integration for PyTorch

`pip install s3torchconnector` · installs from source (sdist only) · licence: BSD License · rank 6787 · last release 2026-02-20 · [PyPI](https://pypi.org/project/s3torchconnector/)

<details><summary>README extract</summary>

The Amazon S3 Connector for PyTorch delivers high throughput for PyTorch training jobs that access or store data in
Amazon S3. Using the S3 Connector for PyTorch
automatically optimizes performance when downloading training data from and writing checkpoints to Amazon S3,
eliminating the need to write your own code to list S3 buckets and manage ...

Features:
Amazon S3 Connector for PyTorch provides robust support for PyTorch distributed checkpoints. This feature includes:

- `S3StorageWriter`: Implementation of PyTorch's StorageWriter interface. ...

Example:
```python
from s3torchconnector import S3MapDataset, S3IterableDataset

# You need to update <BUCKET> and <PREFIX>
DATASET_URI="s3://<BUCKET>/<PREFIX>"
REGION = "us-east-1"

...

</details>

### varint

Simple python varint implementation

`pip install varint` · installs from source (sdist only) · licence: MIT License · rank 6802 · last release 2016-02-24 · [PyPI](https://pypi.org/project/varint/)

### click-configfile

This package supports click commands that use configuration files.

`pip install click-configfile` · installs (wheel) · licence: BSD License · rank 6813 · last release 2017-09-24 · [PyPI](https://pypi.org/project/click-configfile/)

<details><summary>README extract</summary>

click is a framework to simplify writing composable commands for
command-line tools. This package extends the click functionality
by adding support for commands that use configuration files.

.. _click:

EXAMPLE:

A configuration file, like:

.. code-block:: INI ...

</details>

### aws-error-utils

Error-handling functions for boto3/botocore

`pip install aws-error-utils` · installs (wheel) · licence: Apache Software License · rank 6961 · last release 2022-11-03 · [PyPI](https://pypi.org/project/aws-error-utils/) · [source](https://github.com/benkehoe/aws-error-utils)

<details><summary>README extract</summary>

Making botocore.exceptions.ClientError easier to deal with

All AWS service exceptions are raised by `boto3` as a `botocore.exceptions.ClientError`, with the contents of the exception indicating what kind of exception happened. ...

Example:
```python
import boto3, botocore.exceptions

s3 = boto3.client('s3')
try:
    s3.get_object(Bucket='my-bucket', Key='example')
except botocore.exceptions.ClientError as error:
    if error.response'Error' == 'NoSuchBucket':
        print(error.response'Error')
        # error handling
    else:
        raise
```

Sections: aws-error-utils, Usage, `errors`, `catch_aws_error()`, `get_aws_error_info()`, `aws_error_matches()`, `make_aws_error()`

</details>

### stopit

Timeout control decorator and context managers, raise any exception in another thread

`pip install stopit` · installs from source (sdist only) · licence: MIT License · rank 7058 · last release 2018-02-09 · [PyPI](https://pypi.org/project/stopit/)

<details><summary>README extract</summary>

Raise asynchronous exceptions in other threads, control the timeout of
blocks or callables with two context managers and two decorators.

Features:
This module provides:

- a function that raises an exception in another thread, including the main
 thread.

- two context managers that may stop its inner block activity on timeout. ...

Example:
```python
import stopit
# ...
with stopit.ThreadingTimeout(10) as to_ctx_mgr:
    assert to_ctx_mgr.state == to_ctx_mgr.EXECUTING
    # Something potentially very long but which
    # ...

# OK, let's check what happened
if to_ctx_mgr.state == to_ctx_mgr.EXECUTED:
    # All's fine, everything was executed within 10 seconds
...
```

...

</details>

### certipy

Utility to create and sign CAs and certificates

`pip install certipy` · installs (wheel) · licence: BSD License · rank 7067 · last release 2026-04-29 · [PyPI](https://pypi.org/project/certipy/)

<details><summary>README extract</summary>

A simple python tool for creating certificate authorities and certificates on
the fly.

Certipy was made to simplify the certificate creation process. To that end,
Certipy exposes methods for creating and managing certificate authorities,
certificates, signing and building trust bundles. Behind the scenes Certipy: ...

Example:
```python
from certipy import Certipy

certipy = Certipy(store_dir='/tmp')
certipy.create_ca('foo')
record = certipy.store.get_record('foo')
```

Sections: Certipy, Introduction, Usage, Command line, Code

</details>

### openshift

OpenShift python client

`pip install openshift` · installs (wheel) · licence: Apache Software License · rank 7111 · last release 2023-07-25 · [PyPI](https://pypi.org/project/openshift/)

### ttp

Template Text Parser

`pip install ttp` · installs (wheel) · licence: MIT License · rank 7153 · last release 2026-03-21 · [PyPI](https://pypi.org/project/ttp/) · [docs](https://ttp.readthedocs.io/) · [source](https://github.com/dmulyalin/ttp)

<details><summary>README extract</summary>

TTP is a Python library for semi-structured text parsing using templates.

Features:
To save ones time on transforming raw text into structured data and beyond.

Example:
```python
from ttp import ttp
import pprint

data = """
interface Loopback0
 description Router-id-loopback
 ip address 192.168.0.113/24
!
interface Vlan778
 description CPE_Acces_Vlan
 ip address 2002::fd37/124
 ip vrf CPE1
!
"""

template = """
interface {{ interface }}
 ip address {{ ip }}/{{ mask }}
 description {{ description }}
 ip vrf {{ vrf }}
"""

...
```

Sections: Template Text Parser, Why?, How?, What?, Example - as simple as it can be, Example - a bit more complicated

</details>

### pypdftk

Python wrapper for PDFTK

`pip install pypdftk` · installs from source (sdist only) · licence: BSD License · rank 7202 · last release 2021-04-11 · [PyPI](https://pypi.org/project/pypdftk/)

<details><summary>README extract</summary>

Python module to drive the awesome pdftk binary.

Proudly brought to you by the revolunet team and awesome
contributors

Sections: pypdftk, Features, `fill_form`, `concat`, `get_pages`, `split`, `gen_xfdf`, `get_num_pages`, `replace_page`, `stamp`, `[compress | uncompress]`, `dump_data_fields`, Example

</details>

### mmengine

Engine of OpenMMLab projects

`pip install mmengine` · installs (wheel) · licence: Apache Software License · rank 7287 · last release 2025-03-04 · [PyPI](https://pypi.org/project/mmengine/)

<details><summary>README extract</summary>

OpenMMLab website

 HOT

 OpenMMLab platform

 TRY IT OUT

Introduction |
Installation |
Get Started |
📘Documentation |
🤔Reporting Issues

English | 简体中文

v0.10.6 was released on 2025-01-13.

Highlights:

- Support custom `artifact_location` in MLflowVisBackend #1505 ...

Example:
```python
import torch.nn.functional as F
import torchvision
from mmengine.model import BaseModel

class MMResNet50(BaseModel):
    def init(self):
        super().init()
        self.resnet = torchvision.models.resnet50()

    def forward(self, imgs, labels, mode):
        x = self.resnet(imgs)
        if mode == 'loss':
...
```

Sections: What's New, Introduction, Get Started, Learn More, Ecosystem, Projects in OpenMMLab

</details>

### pycln

A formatter for finding and removing unused import statements.

`pip install pycln` · installs (wheel) · licence: MIT License · rank 7414 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pycln/) · [source](https://github.com/hadialqattan/pycln)

<details><summary>README extract</summary>

Read the documentation on Github pages!

Sections: Usage, Configuration, Used by

</details>

### jws

JSON Web Signatures implementation in Python

`pip install jws` · installs from source (sdist only) · licence: MIT License · rank 7419 · last release 2015-03-10 · [PyPI](https://pypi.org/project/jws/)

<details><summary>README extract</summary>

python-jws
A Python implementation of JSON Web Signatures draft 02

Also now works on Python 3.3+ as well as Python 2.7+. However, it's a naive conversion to support both Python 2 and Python 3 so there may well be hidden bugs.

Sections: Algorithms, Usage, Advanced Usage, TODO, Tests

</details>

### django-querycount

Middleware that Prints the number of DB queries to the runserver console.

`pip install django-querycount` · installs from source (sdist only) · licence: MIT License · rank 7650 · last release 2023-01-05 · [PyPI](https://pypi.org/project/django-querycount/)

<details><summary>README extract</summary>

this project gives you a middleware thatprints DB query counts in Django's runserver console output.

</details>

### django-registration

An extensible user-registration application for Django.

`pip install django-registration` · installs (wheel) · licence: BSD License · rank 7818 · last release 2025-04-07 · [PyPI](https://pypi.org/project/django-registration/) · [docs](https://django-registration.readthedocs.io/) · [source](https://github.com/ubernostrum/django-registration)

<details><summary>README extract</summary>

This is a user-registration application for Django sites.

It has built-in support for:

* User registration with the default Django user model

* User registration with many custom user models

* Two-step (email an activation link) registration

* One-step (register and be immediately logged in) registration ...

Example:
```python
from django.urls import include, path

urlpatterns = [
    # Other URL patterns ...
    path("accounts/", include("django_registration.backends.one_step.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    # More URL patterns ...
]
```

</details>

### fastremap

Remap, mask, renumber, unique, and in-place transposition of 3D labeled images. Point cloud too.

`pip install fastremap` · installs (wheel) · licence: LGPL-3.0 · rank 7867 · last release 2026-10-16 · [PyPI](https://pypi.org/project/fastremap/) · [source](https://github.com/seung-lab/fastremap/)

_README extract left out: share-alike licence._

### uuid7-standard

Pure Python UUIDv7 with datetime-based creation and timestamp extraction, filling gaps in stdlib and other implementations.

`pip install uuid7-standard` · installs (wheel) · licence: MIT OR Unlicense · rank 7870 · last release 2026-09-06 · [PyPI](https://pypi.org/project/uuid7-standard/) · [source](https://git.zi.fi/LeoVasanko/uuid7-standard)

<details><summary>README extract</summary>

A simple module for generating UUIDv7s with creation times, and for extracting the time from a UUID.

ℹ️ At the time of writing, Python had no UUIDv7 support. It does now, but still doesn't allow providing or extracting timestamps, which we do. ...

Example:
```python
import uuid7
from datetime import datetime, UTC
from uuid import UUID

# Create a random UUIDv7 with the current timestamp, same as uuid.uuid7()
u = uuid7.create()
print(str(u), u.bytes)

# Create one with a specific timestamp
when = datetime(1970, 1, 1, tzinfo=UTC)
u = uuid7.create(when)

# Extract the timestamp
...
```

Sections: UUIDv7 for Python, Usage, `uuid7.create(when: datetime?) -> UUID`, `uuid7.time(u: UUID|str) -> datetime`, `uuid7.UUID`: re-export of stdlib UUID

</details>

### django-haystack

Pluggable search for Django.

`pip install django-haystack` · installs from source (sdist only) · licence: BSD-3-Clause · rank 7893 · last release 2026-06-04 · [PyPI](https://pypi.org/project/django-haystack/) · [docs](https://django-haystack.readthedocs.io) · [source](https://github.com/django-haystack/django-haystack)

<details><summary>README extract</summary>

:author: Daniel Lindsley
:date: 2013/07/28

Haystack provides modular search for Django. It features a unified, familiar
API that allows you to plug in different search backends (such as Solr,
Elasticsearch, Whoosh, Xapian, etc.) without having to modify your code. ...

Sections: Haystack, Getting Help, Documentation, Requirements

</details>

### django-sql-explorer

SQL Reporting that Just Works. Fast, simple, and confusion-free.Write and share queries in a delightful SQL editor, with AI assistance

`pip install django-sql-explorer` · installs (wheel) · licence: MIT License · rank 8024 · last release 2026-09-24 · [PyPI](https://pypi.org/project/django-sql-explorer/) · [docs](https://django-sql-explorer.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

* Official Website
* Live Demo
* Documentation

Sections: SQL Explorer, Video Tour, Quick Start, About, Screenshots

</details>

### sling

Slings data from a source to a target

`pip install sling` · installs (wheel) · licence: not stated · rank 8119 · last release 2026-11-05 · [PyPI](https://pypi.org/project/sling/)

<details><summary>README extract</summary>

Slings from a data source to a data target.

Example:
```python
import os
from sling import Sling, Mode

# Set postgres & snowflake connection
# see
os.environ["POSTGRES"] = 'postgres://...'
os.environ["SNOWFLAKE"] = 'snowflake://...'

# Database to database transfer
Sling(
    src_conn="postgres",
    src_stream="public.users",
    tgt_conn="snowflake",
    tgt_object="public.users_copy",
...
```

...

</details>

### cosl

Utils for COS Lite charms

`pip install cosl` · installs (wheel) · licence: Apache Software License · rank 8287 · last release 2026-10-09 · [PyPI](https://pypi.org/project/cosl/)

<details><summary>README extract</summary>

> [!NOTE]
> The `coordinated_workers` module and its related support files have been removed from `cosl`. This functionality now lives in a standalone coordinated-workers PyPI package. Please migrate to that package.

This library provides utilities for
COS Lite charms:

- `CosTool`: bindings for
 cos-tool ...

</details>

### str2bool

Convert string to boolean

`pip install str2bool` · installs from source (sdist only) · licence: BSD License · rank 8511 · last release 2017-12-25 · [PyPI](https://pypi.org/project/str2bool/)

### ppf-datamatrix

Python port of https://github.com/datalog/datamatrix-svg

`pip install ppf-datamatrix` · installs (wheel) · licence: MIT License · rank 8716 · last release 2023-08-23 · [PyPI](https://pypi.org/project/ppf-datamatrix/)

<details><summary>README extract</summary>

ppf.datamatrix is a pure-python package to generate datamatrix codes in SVG.
Also, it integrates nicely in IPython.

ppf.datamatrix has been ported from datalog's
datamatrix-svg, which is written in
javascript. If you like to see what you'll get before installation, check out
their nice web demo. ...

Example:
```python
from ppf.datamatrix import DataMatrix

myDataMatrix = DataMatrix('Test!')
```

</details>

### stockstats

DataFrame with inline stock statistics support.

`pip install stockstats` · installs (wheel) · licence: BSD-3-Clause · rank 8762 · last release 2026-10-26 · [PyPI](https://pypi.org/project/stockstats/)

<details><summary>README extract</summary>

Example:
```python
# Initialize all indicators with shortcuts

Some indicators, such as KDJ, BOLL, MFI, have shortcuts. Use `df.init_all()`
to initialize all these indicators.

This operation generates lots of columns. Please use it with caution.

# Tutorial

# Column naming patterns

Use pattern `__` for full control:

...
```

Sections: Introduction, from CSV, from yfinance (disable multi-level index for compatibility), indicators with default windows, moving averages on any column, MACD generates three columns at once, Bollinger Bands, cross-over detection, comparison operators

</details>

### awsiot

Command Line utility to easily provision IoT things in AWS

`pip install awsiot` · installs (wheel) · licence: MIT License · rank 8993 · last release 2017-12-10 · [PyPI](https://pypi.org/project/awsiot/)

### pygaljs

Python package providing assets from https://github.com/Kozea/pygal.js

`pip install pygaljs` · installs (wheel) · licence: BSD License · rank 9257 · last release 2020-04-03 · [PyPI](https://pypi.org/project/pygaljs/)

<details><summary>README extract</summary>

Python package providing assets from

* Free software: LGPLv3 license

Sections: pygal.js, Releasing, 1.0.2 (2020-04-03), 1.0.1 (2015-09-04), 1.0.0 (2015-08-13)

</details>

### pygments-styles

A curated collection of Pygments styles based on VS Code themes.

`pip install pygments-styles` · installs (wheel) · licence: BSD License · rank 9311 · last release 2025-11-04 · [PyPI](https://pypi.org/project/pygments-styles/) · [source](https://github.com/lepture/pygments-styles)

<details><summary>README extract</summary>

A curated collection of Pygments styles based on VS Code themes.

- Using Pygments styles in Sphinx
- Using Pygments styles in MkDocs

</details>

### ara

ARA Records Ansible

`pip install ara` · installs (wheel) · licence: not stated · rank 9483 · last release 2026-07-13 · [PyPI](https://pypi.org/project/ara/)

<details><summary>README extract</summary>

ARA Records Ansible and makes it easier to understand and troubleshoot.

It is another recursive acronym with a focus on simplicity.

ara provides Ansible reporting by recording ``ansible`` and ``ansible-playbook`` commands regardless of how and where they run: ...

Sections: ARA Records Ansible, About ara, How it works, Requirements, Getting started, Recording playbooks without an API server, Recording playbooks with an API server, Live demo, Copyright

</details>

### django-netfields

Django PostgreSQL netfields implementation

`pip install django-netfields` · installs (wheel) · licence: BSD License · rank 9653 · last release 2026-10-08 · [PyPI](https://pypi.org/project/django-netfields/)

<details><summary>README extract</summary>

This project is an attempt at making proper PostgreSQL net related fields for
Django. In Django pre 1.4 the built in `IPAddressField` does not support IPv6
and uses an inefficient `HOST()` cast in all lookups. As of 1.4 you can use
`GenericIPAddressField` for IPv6, but the casting problem remains. ...

Example:
```python
from netfields import InetAddressField, NetManager

class Example(models.Model):
    inet = InetAddressField()
    # ...

    objects = NetManager()
```

Sections: Django PostgreSQL Netfields, Dependencies, Getting started, Database Functions, Indexes, Related Django bugs, Similar projects

</details>

### hashring

Implements consistent hashing in Python (using md5 as hashing function).

`pip install hashring` · installs (wheel) · licence: BSD License · rank 9713 · last release 2015-04-14 · [PyPI](https://pypi.org/project/hashring/)

<details><summary>README extract</summary>

docstravisappveyorcoverallslandscapescrutinizer|
versiondownloadswheelsupported-versionssupported-implementations|

Implements consistent hashing in Python (using md5 as hashing function).

* Free software: BSD license

Sections: hashring, Documentation, 1.4.0 (2014-12-20)

</details>

### pylibdmtx

Read and write Data Matrix barcodes from Python 2 and 3.

`pip install pylibdmtx` · installs (wheel) · licence: MIT License · rank 9752 · last release 2022-03-15 · [PyPI](https://pypi.org/project/pylibdmtx/)

<details><summary>README extract</summary>

Read and write Data Matrix barcodes from Python 2 and 3 using the
libdmtx library.

- Pure python
- Works with PIL / Pillow images, OpenCV / imageio / numpy `ndarray`\ s, and raw bytes
- Decodes locations of barcodes
- No dependencies, other than the libdmtx library itself
- Tested on Python 2.7, and Python 3.5 to 3.10 ...

Example:
```python
>>> from pylibdmtx.pylibdmtx import decode
>>> from PIL import Image
>>> decode(Image.open('pylibdmtx/tests/datamatrix.png'))
[Decoded(data='Stegosaurus', rect=Rect(left=5, top=6, width=96, height=95)),
 Decoded(data='Plesiosaurus', rect=Rect(left=298, top=6, width=95, height=95))]
```

Sections: pylibdmtx, Example usage, Windows error message, Limitations

</details>

### pwned-passwords-django

A Pwned Passwords implementation for Django sites.

`pip install pwned-passwords-django` · installs (wheel) · licence: BSD License · rank 9765 · last release 2025-04-06 · [PyPI](https://pypi.org/project/pwned-passwords-django/) · [docs](https://pwned-passwords-django.readthedocs.io/) · [source](https://github.com/ubernostrum/pwned-passwords-django)

<details><summary>README extract</summary>

`pwned-passwords-django` provides helpers for working with the
Pwned Passwords database from Have I Been Pwned in Django powered sites. Pwned Passwords is
an extremely large database of passwords known to have been
compromised through data breaches, and is useful as a tool for
rejecting common or weak passwords. ...

</details>

### ipynbname

Simply returns either notebook filename or the full path to the notebook when run from Jupyter notebook in browser.

`pip install ipynbname` · installs (wheel) · licence: MIT License · rank 9795 · last release 2025-08-17 · [PyPI](https://pypi.org/project/ipynbname/)

<details><summary>README extract</summary>

When run in a Jupyter notebook, simply returns the notebook filename or the full path to the notebook.
I created this to help with automating posting blog posts written in Jupyter notebooks directly to
GitHub Pages. ...

Example:
```python
import ipynbname
nb_fname = ipynbname.name()
```

Sections: ipynbname, Examples, Limitations

</details>

### django-eventstream

Server-Sent Events for Django

`pip install django-eventstream` · installs (wheel) · licence: MIT License · rank 9915 · last release 2026-05-29 · [PyPI](https://pypi.org/project/django-eventstream/)

<details><summary>README extract</summary>

EventStream provides Django views that can push data to connected clients. Data is sent using the Server-Sent Events protocol (SSE), in which data is streamed over a never-ending HTTP response.

For example, you could create an endpoint, `/events/`, that a client could connect to with a GET request: ...

Example:
```python
from django.urls import path, include
import django_eventstream

urlpatterns = [
    ...
    path("events/", include(django_eventstream.urls), {"channels": ["test"]}),
]
```

Sections: Django EventStream, Setup, Sending events, Deploying, Multiple instances and scaling, Views with Django REST Framework, Event storage, Receiving in the browser, Routes and channel selection, Cross-Origin Resource Sharing (CORS) Headers

</details>

### desert

Deserialize to objects while staying DRY

`pip install desert` · installs (wheel) · licence: MIT License · rank 10003 · last release 2022-09-23 · [PyPI](https://pypi.org/project/desert/)

<details><summary>README extract</summary>

Desert generates serialization schemas for `dataclasses` and `attrs` classes. Writing
code that's DRY ("don't repeat yourself") helps avoid bugs and improve readability. Desert
helps you write code that's DRY.

Example:
```python
    from dataclasses import dataclass

    # Or using attrs
    # from attr import dataclass

    from typing import List

import desert

    @dataclass
    class Person:
        name: str
        age: int

    @dataclass
    class Car:
        passengers: List[Person]

    # Load some simple data types.
...
```

Sections: Desert: DRY deserialization, Usage, Documentation, Limitations, 2022.09.22 (2022-09-22), Backward-incompatible Changes, Changes, 2020.11.18 (2020-11-18), 2020.01.06 (2020-01-06), 2020.01.05 (2020-01-05), 2020.01.04 (2020-01-04)

</details>

### morphys

Smart conversions between unicode and bytes types for common cases

`pip install morphys` · installs (wheel) · licence: MIT License · rank 10013 · last release 2017-01-10 · [PyPI](https://pypi.org/project/morphys/)

<details><summary>README extract</summary>

Morphys is a simple, small library providing utilities for easy smart
conversions between `unicode` and `bytes` types.

In Python 2, the treatment of `unicode` and `bytes` objects is a potential
source of many surprising and annoying errors, should a non-ASCII character
appear anywhere in a string. ...

Sections: Morphys, Conversion functions, Lazy conversion wrapper, Default encoding, Python 3

</details>

### sysv-ipc

SysV IPC primitives (semaphores, shared memory and message queues) for Python

`pip install sysv-ipc` · installs (wheel) · licence: BSD-3-Clause · rank 10026 · last release 2026-01-09 · [PyPI](https://pypi.org/project/sysv-ipc/)

<details><summary>README extract</summary>

`sysv_ipc` is a Python module (written in C) that permits creation and manipulation of System V semaphores, shared memory and message queues. Most (all?) Unixes (including OS X) support System V IPC well. Windows plus WSL or Cygwin might work.

For complete documentation, see the usage notes. ...

Sections: SYSV IPC, Tests, Related

</details>

### pubcontrol

EPCP library

`pip install pubcontrol` · installs from source (sdist only) · licence: MIT License · rank 10086 · last release 2023-07-05 · [PyPI](https://pypi.org/project/pubcontrol/)

### iteration-utilities

Utilities based on Pythons iterators and generators.

`pip install iteration-utilities` · installs from source (sdist only) · licence: Apache License Version 2.0 · rank 10099 · last release 2024-10-08 · [PyPI](https://pypi.org/project/iteration-utilities/) · [docs](https://iteration-utilities.readthedocs.io/en/latest/) · [source](https://github.com/MSeifert04/iteration_utilities.git)

<details><summary>README extract</summary>

Utilities based on Pythons iterators and generators.

The full list of functions and classes included in this package:

========================================================================================================== ...

Sections: Iteration utilities, Documentation, Downloads

</details>

### gripcontrol

GRIP library

`pip install gripcontrol` · installs from source (sdist only) · licence: MIT License · rank 10142 · last release 2026-05-14 · [PyPI](https://pypi.org/project/gripcontrol/)

### awslogs

awslogs is a simple command line tool to read aws cloudwatch logs.

`pip install awslogs` · installs (wheel) · licence: BSD License · rank 10148 · last release 2024-04-02 · [PyPI](https://pypi.org/project/awslogs/)

<details><summary>README extract</summary>

awslogs is a simple command line tool to read aws cloudwatch logs.

</details>

### django-grip

Django GRIP library

`pip install django-grip` · installs from source (sdist only) · licence: MIT License · rank 10162 · last release 2025-03-24 · [PyPI](https://pypi.org/project/django-grip/)

### pyoxipng

Python wrapper for multithreaded .png image file optimizer oxipng

`pip install pyoxipng` · installs from source (sdist only) · licence: MIT License · rank 10165 · last release 2025-08-21 · [PyPI](https://pypi.org/project/pyoxipng/) · [docs](https://github.com/nfrasser/pyoxipng#readme) · [source](https://github.com/nfrasser/pyoxipng)

<details><summary>README extract</summary>

Python wrapper for multithreaded .png image file optimizer
oxipng (written in Rust). Use
`pyoxipng` to reduce the file size of your PNG images.

Jump to a section

- Installation
- API

 - optimize
 - optimize_from_memory
 - RawImage

- Options
 - filter
 - interlace
 - strip
 - deflate
- Development
- License

Example:
```python
oxipng.optimize("/path/to/image.png")
```

Sections: pyoxipng, API, oxipng.optimize(input, output=None, \*\*kwargs), oxipng.optimize_from_memory(data, \*\*kwargs), oxipng.RawImage, add_png_chunk(name, data), add_icc_profile(data), create_optimized_png(\*\*kwargs), Options, filter, interlace, strip, deflate

</details>

### JSON_minify

A simple script to minify valid JSON, containing C/C++ style comments

`pip install JSON_minify` · installs (wheel) · licence: MIT License · rank 10169 · last release 2017-10-10 · [PyPI](https://pypi.org/project/JSON_minify/)

<details><summary>README extract</summary>

A port of the `JSON-minify` utility to the Python language.

Features:
`JSON-minify` minifies blocks of JSON-like content into valid JSON by removing
all whitespace *and* JS-style comments (single-line `//` and multi-line
 `/* .. */`). ...

Sections: JSON-minify, Overview

</details>

### DrissionPage

Python based web automation tool. It can control the browser and send and receive data packets.

`pip install DrissionPage` · installs (wheel) · licence: not stated · rank 10218 · last release 2026-05-27 · [PyPI](https://pypi.org/project/DrissionPage/)

<details><summary>README extract</summary>

DrissionPage 是一个基于 python 的网页自动化工具。

它既能控制浏览器，也能收发数据包，还能把两者合而为一。

可兼顾浏览器自动化的便利性和 requests 的高效率。

它功能强大，内置无数人性化设计和便捷功能。

它的语法简洁而优雅，代码量少，对新手友好。

> IPWO 提供的真实住宅 IP，大幅降低被封禁风险。195 + 国家 / 地区精准定位，轻松应对大型爬虫任务。让爬虫更简单，让数据更安全。戳本信息注册可获得有效保护账号的高匿名ip流量。

官方网站：

项目地址：gitee | github | gitcode

您的星星是对我最大的支持💖

支持系统：Windows、Linux、Mac

python 版本：3.6 及以上 ...

Sections: ✨️ 概述, 🛠 如何使用, 💡 理念, ☀️ 特性和亮点, 🎇 强大的自研内核, 🎇 亮点功能, 📝 使用条款, ☕ 请我喝咖啡

</details>

### sailthru-client

Python client for Sailthru API

`pip install sailthru-client` · installs from source (sdist only) · licence: MIT License · rank 10254 · last release 2018-07-26 · [PyPI](https://pypi.org/project/sailthru-client/)

<details><summary>README extract</summary>

For installation instructions, documentation, and examples please visit:

A simple client library to remotely access the `Sailthru REST API` as per

Python binding for Sailthru API based on Requests

It will make requests in `JSON` format.

Supports Python 2.6, 2.7, 3.3+

Sections: sailthru-python-client, Running tests, API Rate Limiting, ... make some api calls ...

</details>

### autoimport

Autoimport missing python libraries.

`pip install autoimport` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 10589 · last release 2024-10-01 · [PyPI](https://pypi.org/project/autoimport/) · [docs](https://lyz-code.github.io/autoimport)

_README extract left out: share-alike licence._

### django-activity-stream

Generate generic activity streams from the actions on your site. Users can follow any actors' activities for personalized streams.

`pip install django-activity-stream` · installs (wheel) · licence: BSD License · rank 10616 · last release 2023-10-04 · [PyPI](https://pypi.org/project/django-activity-stream/)

<details><summary>README extract</summary>

Django Activity Stream is a way of creating activities generated by the actions on your site.

It is designed for generating and displaying streams of interesting actions and can handle following and unfollowing of different activity sources. ...

Sections: Django Activity Stream, What is Django Activity Stream?

</details>

### ttp_templates

Template Text Parser Templates collections

`pip install ttp_templates` · installs (wheel) · licence: MIT License · rank 10621 · last release 2026-11-01 · [PyPI](https://pypi.org/project/ttp_templates/) · [docs](https://dmulyalin.github.io/ttp_templates/) · [source](https://github.com/dmulyalin/ttp_templates)

<details><summary>README extract</summary>

This repository contains a collection of TTP templates.

If you solved a problem using TTP and feel that your work can be useful to other people, feel
free to raise an issue or submit pull request to include your template(s) in this repository.
Refer to Contribute Guide for details.

Documentation:

Repository:

TTP:

Example:
```python
from ttp_templates import parse_output
import pprint

data = """
interface GigabitEthernet1/3.251
 description Customer #32148
 encapsulation dot1q 251
 ip address 172.16.33.10 255.255.255.128
 shutdown
!
interface GigabitEthernet1/3.251
 description Customer #32148
 encapsulation dot1q 251
 ip address 172.16.33.10 255.255.255.128
 shutdown
"""

...
```

...

</details>

### atomicx

easy-to-use lock-free atomic integers, booleans, and floats for Python

`pip install atomicx` · installs (wheel) · licence: MIT License · rank 10632 · last release 2025-09-28 · [PyPI](https://pypi.org/project/atomicx/) · [docs](https://github.com/RuneBlaze/atomicx/blob/main/DOCS.md)

<details><summary>README extract</summary>

atomicx is an easy-to-use atomics library for Python, providing atomic integer, boolean, and floats. It allows you to perform atomic operations on shared variables, ensuring thread-safety and preventing race conditions in concurrent programming. Everything is entirely lock-free and is backed by Rust's atomic types (or from `portable-atomic`). ...

Features:
- Atomic integer operations: load, store, add, subtract, swap, compare and exchange, multiply, divide, increment, decrement.
- Atomic boolean operations: load, store, swap, compare and exchange, flip. ...

Example:
```python
from atomicx import AtomicInt

# Create an atomic integer with an initial value of 0
atom = AtomicInt()

# Perform atomic operations
atom.store(10)
value = atom.load()
print(f"Value: {value}")

...

</details>

### napalm

Network Automation and Programmability Abstraction Layer with Multivendor support

`pip install napalm` · installs (wheel) · licence: Apache Software License · rank 10777 · last release 2026-07-27 · [PyPI](https://pypi.org/project/napalm/) · [source](https://github.com/napalm-automation/napalm)

<details><summary>README extract</summary>

NAPALM (Network Automation and Programmability Abstraction Layer with Multivendor support) is a Python library that implements a set of functions to interact with different router vendor devices using a unified API.

NAPALM supports several methods to connect to the devices, to manipulate configurations or to retrieve data. ...

Sections: NAPALM, Documentation, Upgrading, Automation Frameworks, Contact, News, Thanks

</details>

### ydiff

View colored, incremental diff in a workspace or from stdin, in side-by-side or unified moded, and auto paged.

`pip install ydiff` · installs (wheel) · licence: BSD License · rank 11105 · last release 2025-12-06 · [PyPI](https://pypi.org/project/ydiff/)

<details><summary>README extract</summary>

Ydiff is a terminal-based tool to view *colored*, *incremental* diffs in
a version-controlled workspace or from stdin, in *side-by-side* (similar to
`diff -y`) or unified mode, and *auto-paged*. It only requires Python >= 3.3
*without external dependencies* and `less` as a pager.

The diffs in side-by-side mode appear below. ...

Sections: Ydiff, Usage, Customized themes, Notes, Known issues

</details>

### DrissionRecord

用于记录数据的模块。

`pip install DrissionRecord` · installs (wheel) · licence: MIT License · rank 11292 · last release 2026-09-04 · [PyPI](https://pypi.org/project/DrissionRecord/)

<details><summary>README extract</summary>

本库是一个基于 python 的工具集，用于记录数据到文件。

使用方便，代码简洁，是一个可靠、省心且实用的工具。

支持多线程同时写入文件。

联系邮箱： g1879@qq.com

使用手册： 📒点击打开

简单，可靠，省心。

进行数据采集的时候，常常要保存数据到文件，频繁开关文件会影响效率，而如果等采集结束再写入，会有因异常而丢失数据的风险。

因此写了这个工具，只要把数据扔进去，它能缓存到一定数量再一次写入，减少文件开关次数，且在程序崩溃或退出时尽量自动保存。

它们使用非常方便，无论何时何地，无论什么格式，只要使用`add_data()`方法把数据存进去即可，语法极其简明扼要，使程序员能更专注业务逻辑。 ...

Example:
```python
from DrissionRecord import Recorder

data = ((1, 2, 3, 4),
        (5, 6, 7, 8))

r = Recorder('data.csv')
r.add_data(data)  # 一次记录多行数据
r.add_data('abc')  # 记录单行数据
r.record()
```

Sections: ⭐️ 简介, ✨️ 理念, 📕 背景, 🍀 特性, 🌠 概览, ☕ 请我喝咖啡

</details>

### robotframework-debuglibrary

RobotFramework debug library and an interactive shell

`pip install robotframework-debuglibrary` · installs (wheel) · licence: BSD License · rank 11323 · last release 2024-01-12 · [PyPI](https://pypi.org/project/robotframework-debuglibrary/)

<details><summary>README extract</summary>

Robotframework-DebugLibrary is a debug library for RobotFramework,
which can be used as an interactive shell(REPL) also.

Example:
```python
$ rfdebug
[...snap...]
>>>>> Enter interactive shell
> help
Input Robotframework keywords, or commands listed below.
Use "libs" or "l" to see available libraries,
use "keywords" or "k" to see the list of library keywords,
use the TAB keyboard key to autocomplete keywords.

# Documented commands (type help <topic>):
...
```

Sections: Debug Library for Robot Framework, Introduction, NOTICE: 2.0 is not compatible with python 2, Usage, Step debugging, Submitting issues

</details>

### atomos

Atomic primitives for Python.

`pip install atomos` · installs from source (sdist only) · licence: BSD License · rank 11331 · last release 2015-07-05 · [PyPI](https://pypi.org/project/atomos/)

### DrissionGet

一个简洁易用的多线程文件下载工具。

`pip install DrissionGet` · installs (wheel) · licence: BSD License · rank 11465 · last release 2026-06-04 · [PyPI](https://pypi.org/project/DrissionGet/)

<details><summary>README extract</summary>

DrissionGet 是一个基于 python 的简洁易用的多线程文件下载工具。
使用简单，功能强大。

使用文档：点击查看

- 多线程，可同时下载多个文件
- 大文件自动分块用多线程下载
- 自动任务调度，简易的任务添加方式
- 可使用已有`Session`对象，便于保持登录状态
- 与 DrissionPage 良好兼容
- 自动创建目标路径
- 自动去除路径中的非法字符
- 自动处理文件名冲突
- 可对现有文件追加内容
- 连接失败自动重试

Example:
```python
from DrissionGet import DrissionGet

# 创建下载器对象
d = DrissionGet(r'.\files')

# 添加多个任务
url1 = '
url2 = '

d.download(url1)
d.download(url2)
```

Sections: 简介, 特性, 简单示例, ☕ 请我喝咖啡

</details>

### django-tastypie

A flexible & capable API layer for Django.

`pip install django-tastypie` · installs from source (sdist only) · licence: BSD License · rank 11499 · last release 2025-02-23 · [PyPI](https://pypi.org/project/django-tastypie/)

<details><summary>README extract</summary>

Creating delicious APIs for Django apps since 2010.

Currently in beta but being used actively in production on several
sites.

* Python 3.8+ (Whatever is supported by your version of Django)
* Django 4.2 (LTS releases) or Django 4.0+ (intermediate releases, including 5.0 and 5.1)
* dateutil ( >= 2.1

Features:
There are other API frameworks out there for Django. You need to
assess the options available and decide for yourself. That said, here are some
common reasons for tastypie.

* You need an API that is RESTful and uses HTTP well. ...

Example:
```python
# myapp/api.py
# ============
from tastypie.resources import ModelResource
from myapp.models import Entry

class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()

# urls.py
# =======
...

</details>

### typecode-libmagic

A ScanCode path provider plugin to provide a prebuilt native libmagic binary and database.

`pip install typecode-libmagic` · installs (wheel) · licence: not stated · rank 11508 · last release 2021-05-31 · [PyPI](https://pypi.org/project/typecode-libmagic/)

<details><summary>README extract</summary>

A ScanCode path provider plugin to provide a prebuilt native libmagic binary and database.

</details>

### claude-swap

Multi-account switcher for Claude Code

`pip install claude-swap` · installs (wheel) · licence: MIT License · rank 11591 · last release 2026-11-07 · [PyPI](https://pypi.org/project/claude-swap/) · [source](https://github.com/realiti4/claude-swap)

<details><summary>README extract</summary>

Multi-account switcher for Claude Code. Easily switch between multiple Claude accounts without logging out, or let it switch for you before you hit a rate limit. Track usage for every account in a live dashboard, and run accounts in parallel. Works with both the Claude Code CLI and the VS Code extension.

Sections: claude-swap, Using uv (recommended), Using pipx, From source, Updating, Usage, Add your first account, Add more accounts, Switch accounts, Automatic switching, Run multiple accounts at the same time (session mode), Interactive dashboard (TUI), Refresh expired tokens, Other commands

</details>

### mongo-query-match

A utility library that provides a MongoDB-like query language for querying python collections. It's mainly intended to parse objects structured as fundamental types in a similar fashion to what is produced by JSON or YAML parsers.

`pip install mongo-query-match` · installs (wheel) · licence: not stated · rank 11594 · last release 2025-02-02 · [PyPI](https://pypi.org/project/mongo-query-match/)

<details><summary>README extract</summary>

A utility library that provides a MongoDB-like query
language for querying python collections. It's mainly intended to parse objects
structured as fundamental types in a similar fashion to what is produced by `JSON`
or `YAML` parsers. It follows the specification of queries for MongoDB version 3.4.

Example:
```python
from mongoquery import Query, QueryError

records = [
    {"a": 5, "b": 5, "c": None},
    {"a": 3, "b": None, "c": 8},
    {"a": None, "b": 3, "c": 9},
    {"a": 1, "b": 2, "c": 3},
    {"a": 2, "c": 5},
    {"a": 3, "b": 2},
    {"a": 4},
    {"b": 2, "c": 4},
    {"b": 2},
    {"c": 6}
]

a_is_3 = Query({"a": 3})

# match a single object
...
```

Sections: mongoquery, Usage, Query syntax, Functional differences with MongoDB's queries

</details>

### boilerpy3

Python port of Boilerpipe, for HTML boilerplate removal and text extraction

`pip install boilerpy3` · installs (wheel) · licence: Apache Software License · rank 11695 · last release 2023-11-01 · [PyPI](https://pypi.org/project/boilerpy3/)

<details><summary>README extract</summary>

BoilerPy3 is a native Python port of Christian Kohlschütter's Boilerpipe library, released under the Apache 2.0 Licence.

This package is based on sammyer's BoilerPy, specifically mercuree's Python3-compatible fork. ...

Example:
```python
from boilerpy3 import extractors

extractor = extractors.ArticleExtractor()

# From a URL
content = extractor.get_content_from_url('

# From a file
content = extractor.get_content_from_file('tests/test.html')

# From raw HTML
content = extractor.get_content('
# Example
')
```

Sections: BoilerPy3, About, Usage, Text Extraction, Marked HTML Extraction, Other, Extractors, DefaultExtractor, ArticleExtractor, ArticleSentencesExtractor, LargestContentExtractor, CanolaExtractor, KeepEverythingExtractor, NumWordsRulesExtractor

</details>

### mongoquery

A utility library that provides a MongoDB-like query language for querying python collections. It's mainly intended to parse objects structured as fundamental types in a similar fashion to what is produced by JSON or YAML parsers.

`pip install mongoquery` · installs (wheel) · licence: not stated · rank 11798 · last release 2025-09-16 · [PyPI](https://pypi.org/project/mongoquery/)

<details><summary>README extract</summary>

A utility library that provides a MongoDB-like query
language for querying python collections. It's mainly intended to parse objects
structured as fundamental types in a similar fashion to what is produced by `JSON`
or `YAML` parsers. It follows the specification of queries for MongoDB version 3.4.

Example:
```python
from mongoquery import Query, QueryError

records = [
    {"a": 5, "b": 5, "c": None},
    {"a": 3, "b": None, "c": 8},
    {"a": None, "b": 3, "c": 9},
    {"a": 1, "b": 2, "c": 3},
    {"a": 2, "c": 5},
    {"a": 3, "b": 2},
    {"a": 4},
    {"b": 2, "c": 4},
    {"b": 2},
    {"c": 6}
]

a_is_3 = Query({"a": 3})

# match a single object
...
```

Sections: mongoquery, Usage, Query syntax, Functional differences with MongoDB's queries

</details>

### extractcode-libarchive

A ScanCode path provider plugin to provide a prebuilt native libarchive binary.

`pip install extractcode-libarchive` · installs (wheel) · licence: apache-2.0 AND bsd-simplified · rank 11853 · last release 2021-05-31 · [PyPI](https://pypi.org/project/extractcode-libarchive/)

<details><summary>README extract</summary>

A ScanCode path provider plugin to provide a prebuilt native libarchive binary.

</details>

### code128

Create code128 barcodes

`pip install code128` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 11918 · last release 2015-01-18 · [PyPI](https://pypi.org/project/code128/)

_README extract left out: share-alike licence._

### brazilnum

Validate Brazilian CNPJ, CEI, CPF, PIS/PASEP, CEP, and municipal numbers

`pip install brazilnum` · installs (wheel) · licence: MIT · rank 12027 · last release 2026-07-24 · [PyPI](https://pypi.org/project/brazilnum/) · [source](https://github.com/poliquin/brazilnum)

<details><summary>README extract</summary>

Python functions for working with CNPJ, CEI, CPF, PIS/PASEP, CEP, and município
numbers, which identify firms, people, and places in Brazil.

Installation

 pip install brazilnum

Usage Examples

Requires Python 3.9 or newer.

Validate a CNPJ number for a firm, in this case Telefônica Brasil: ...

Sections: Validate Brazilian Identification Numbers, Validation Functions, Formatting and Padding, CNPJ Parsing, CEP Parsing, Municípios (Municipalities), Random Identifiers, Check Digits

</details>

### azure-log-analytics-data-collector-api

Azure Log Analytics Data Collector API Client

`pip install azure-log-analytics-data-collector-api` · installs (wheel) · licence: MIT License · rank 12073 · last release 2020-07-21 · [PyPI](https://pypi.org/project/azure-log-analytics-data-collector-api/)

### named

Named types.

`pip install named` · installs (wheel) · licence: MIT License · rank 12075 · last release 2024-03-15 · [PyPI](https://pypi.org/project/named/) · [docs](https://nekitdev.github.io/named) · [source](https://github.com/nekitdev/named)

<details><summary>README extract</summary>

[][License]
[][Package]
[][Package]
[][Discord]

[][Documentation]
[][Actions]
[][Actions]
[][Coverage]

> *Named types.*

Example:
```python
>>> from named import get_name, get_type_name, is_named
>>> print(is_named(int))
True
>>> print(get_name(int))
int
>>> print(is_named(42))
False
>>> print(get_type_name(42))
int
```

Sections: `named`, pip, poetry, Example, Documentation

</details>

### bitarray-hardbyte

efficient arrays of booleans -- C extension

`pip install bitarray-hardbyte` · installs from source (sdist only) · licence: Python Software Foundation License · rank 12149 · last release 2022-02-28 · [PyPI](https://pypi.org/project/bitarray-hardbyte/)

<details><summary>README extract</summary>

This library provides an object type which efficiently represents an array
of booleans. Bitarrays are sequence types and behave very much like usual
lists. Eight bits are represented by one byte in a contiguous block of
memory. The user can select between two representations: little-endian
and big-endian. All functionality is implemented in C. ...

Features:
* The bit endianness can be specified for each bitarray object, see below.
* Sequence methods: slicing (including slice assignment and deletion),
 operations `+`, `*`, `+=`, `*=`, the `in` operator, `len()`
* Fast methods for encoding and decoding ...

Example:
```python
>>> from bitarray import bitarray
>>> a = bitarray()         # create empty bitarray
>>> a.append(1)
>>> a.extend([1, 0])
>>> a
bitarray('110')
...

</details>

### django-leaflet

A Django map widget using Leaflet

`pip install django-leaflet` · installs (wheel) · licence: LGPL-3.0-only · rank 12173 · last release 2026-08-17 · [PyPI](https://pypi.org/project/django-leaflet/)

_README extract left out: share-alike licence._

### pycryptosat

Bindings to CryptoMiniSat, an advanced SAT solver

`pip install pycryptosat` · does not install on CPython 3.14 · licence: MIT License · rank 12357 · last release 2026-10-09 · [PyPI](https://pypi.org/project/pycryptosat/)

<details><summary>README extract</summary>

Python bindings to CryptoMiniSat. The solver runs inside the Python process.

Example:
```python
>>> from pycryptosat import Solver
>>> s = Solver()
>>> s.add_clause([1, 2])
>>> s.add_clause([-1])
>>> s.solve()
(True, (None, False, True))
>>> s.solve([-2])
(False, None)
>>> s.get_conflict()
[2]
>>> s.solve()
(True, (None, False, True))
```

Sections: pycryptosat SAT solver, Usage, Solver options

</details>

### extractcode-7z

A ScanCode path provider plugin to provide a prebuilt native sevenzip binary.

`pip install extractcode-7z` · installs (wheel) · licence: apache-2.0 AND lgpl-2.1 and unrar and brian-gladman-3-clause · rank 12370 · last release 2021-05-31 · [PyPI](https://pypi.org/project/extractcode-7z/)

_README extract left out: share-alike licence._

### fastcov

A massively parallel gcov wrapper for generating intermediate coverage formats fast

`pip install fastcov` · installs (wheel) · licence: MIT License · rank 12435 · last release 2026-05-29 · [PyPI](https://pypi.org/project/fastcov/)

<details><summary>README extract</summary>

<!-- # SPDX-License-Identifier: MIT -->

A parallelized gcov wrapper for generating intermediate coverage formats *fast*

The goal of fastcov is to generate code coverage intermediate formats *as fast as possible*, even for large projects with hundreds of gcda objects. ...

Sections: fastcov, Quick Start, Filtering Options, Combine Operations, Utilities, Benchmarks

</details>

### mmcv

OpenMMLab Computer Vision Foundation

`pip install mmcv` · installs from source (sdist only) · licence: Apache Software License · rank 12465 · last release 2024-04-24 · [PyPI](https://pypi.org/project/mmcv/)

### datapackage

Utilities to work with Data Packages as defined on specs.frictionlessdata.io

`pip install datapackage` · installs (wheel) · licence: MIT License · rank 12467 · last release 2024-03-12 · [PyPI](https://pypi.org/project/datapackage/)

<details><summary>README extract</summary>

A library for working with Data Packages.

> [Important Notice] We have released Frictionless Framework. This framework provides improved `datapackage` functionality extended to be a complete data solution. The change in not breaking for the existing software so no actions are required. ...

Features:
- `Package` class for working with data packages
 - `Resource` class for working with data resources
 - `Profile` class for working with profiles
 - `validate` function for validating data package descriptors
 - `infer` function for inferring data ...

Example:
```python
from datapackage import Package

package = Package('datapackage.json')
package.get_resource('resource').read()
```

...

</details>

### wakepy

wakelock / keep-awake / stay-awake

`pip install wakepy` · installs (wheel) · licence: MIT License · rank 12532 · last release 2026-02-07 · [PyPI](https://pypi.org/project/wakepy/) · [docs](https://wakepy.readthedocs.io/) · [source](https://github.com/wakepy/wakepy)

<details><summary>README extract</summary>

Cross-platform wakelock / keep-awake / stay-awake written in Python.

Wakepy is a package with an Python API and a CLI tool for *keeping a system awake*. It has two main modes:

⌛ Keeping CPU awake: For long running tasks. ...

Features:
Here's some reasons why you might want to consider using wakepy:

 🙅🏼‍♂️ Non-disruptive methods ✅
 No mouse wiggling or pressing random keys like F15. Wakepy is completely non-disruptive. ...

Example:
```python
from wakepy import keep

@keep.running
def long_running_task():
    # Do something that takes a long time
```

Sections: What is wakepy?, Why wakepy?, Command line interface (CLI), Basic usage within Python, Where wakepy is used?, Links, Wakepy roadmap, Footnotes

</details>

### netius

Netius System

`pip install netius` · installs (wheel) · licence: Apache Software License · rank 12609 · last release 2026-11-06 · [PyPI](https://pypi.org/project/netius/)

<details><summary>README extract</summary>

Fast and readable async non-blocking network apps

Netius is a Python network library that can be used for the rapid creation of asynchronous non-blocking
servers and clients. It has no dependencies, it's cross-platform, and brings some sample netius-powered
servers out of the box, namely a production-ready WSGI server. ...

Example:
```python
import netius.servers

def app(environ, start_response):
    status = "200 OK"
    contents = "Hello World"
    content_l = len(contents)
    headers = (
        ("Content-Length", content_l),
        ("Content-Type", "text/plain"),
        ("Connection", "keep-alive")
    )
    start_response(status, headers)
    yield contents

...
```

Sections: Netius, Usage, WSGI Server, More

</details>

### inform

print & logging utilities for communicating with user

`pip install inform` · installs (wheel) · licence: MIT License · rank 12696 · last release 2026-06-28 · [PyPI](https://pypi.org/project/inform/) · [docs](https://inform.readthedocs.io) · [source](https://github.com/kenkundert/inform)

<details><summary>README extract</summary>

:Author: Ken Kundert
:Version: 1.37
:Released: 2026-06-28

A package that provides specialized print functions that are used when
communicating with the user. It allows you to easily print attractive,
informative, and consistent error messages. For example:

Inform also provides logging and output control. ...

Example:
```python
>> from inform import display, warn, error
>> display(
..     'Display is like print'
..     'except that it supports logging and can be disabled.'
..     sep=', ')
Display is like print, except that it supports logging and can be disabled.

>> warn('warnings get a header that is printed in yellow.')
...
```

Sections: Inform — Print & Logging Utilities, Introduction, Exception, Utilities

</details>

### robotcode-plugin

Some classes for RobotCode plugin management

`pip install robotcode-plugin` · installs (wheel) · licence: Apache-2.0 · rank 12775 · last release 2026-10-26 · [PyPI](https://pypi.org/project/robotcode-plugin/) · [docs](https://github.com/robotcodedev/robotcode#readme) · [source](https://github.com/robotcodedev/robotcode)

<details><summary>README extract</summary>

Plugin management system for RobotCode.

This package is part of the RobotCode project. The complete source code is available at github.com/robotcodedev/robotcode.

Sections: robotcode-plugin, Introduction, Documentation

</details>

### robotcode-robot

Support classes for RobotCode for handling Robot Framework projects.

`pip install robotcode-robot` · installs (wheel) · licence: Apache-2.0 · rank 12805 · last release 2026-10-26 · [PyPI](https://pypi.org/project/robotcode-robot/) · [docs](https://github.com/robotcodedev/robotcode#readme) · [source](https://github.com/robotcodedev/robotcode)

<details><summary>README extract</summary>

Robot Framework project handling and integration utilities for RobotCode.

This package is part of the RobotCode project. The complete source code is available at github.com/robotcodedev/robotcode.

Sections: robotcode-robot, Introduction, Documentation

</details>

### robotcode-core

Some core classes for RobotCode

`pip install robotcode-core` · installs (wheel) · licence: Apache-2.0 · rank 12810 · last release 2026-10-26 · [PyPI](https://pypi.org/project/robotcode-core/) · [docs](https://github.com/robotcodedev/robotcode#readme) · [source](https://github.com/robotcodedev/robotcode)

<details><summary>README extract</summary>

Core utilities and type definitions for RobotCode.

This package is part of the RobotCode project. The complete source code is available at github.com/robotcodedev/robotcode.

Sections: robotcode-core, Introduction, Documentation

</details>

### ResourceBundle

ResourceBundle is a module that manages internationalization of string resources.

`pip install ResourceBundle` · installs (wheel) · licence: MIT License · rank 12828 · last release 2024-04-18 · [PyPI](https://pypi.org/project/ResourceBundle/) · [docs](https://github.com/felix-zenk/ResourceBundle) · [source](https://github.com/felix-zenk/ResourceBundle)

<details><summary>README extract</summary>

ResourceBundle is a package that manages internationalization / localization (i18n / l10n) of string resources.
It is inspired by Java's ResourceBundle and accepts the same format as a Java ``PropertyResourceBundle``.

> Note: ResourceBundle is not the pythonic way of internationalization / localization. ...

Example:
```python
import ResourceBundle

bundle = ResourceBundle.get_bundle("Strings", "en")

# It is now possible to get a resource with the get() method
bundle.get("key")
```

Sections: ResourceBundle, Usage, gettext

</details>

### pyTooling

pyTooling is a powerful collection of arbitrary useful classes, decorators, meta-classes and exceptions.

`pip install pyTooling` · installs (wheel) · licence: Apache-2.0 · rank 12835 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pyTooling/) · [docs](https://pyTooling.GitHub.io/pyTooling) · [source](https://GitHub.com/pyTooling/pyTooling)

<details><summary>README extract</summary>

<!--


pyTooling is a powerful collection of arbitrary useful abstract data models, missing classes, decorators, a new
performance boosting meta-class and enhanced exceptions. It also provides lots of helper functions e.g. to ease the
handling of package descriptions or to unify multiple existing APIs into a single API. ...

Features:
* Colored command line outputs based on `colorama`.
* Message classification in `fatal`, `error`, `warning`, `normal`, `quiet`, ...
* Get information like terminal dimensions from underlying terminal window.

Example:
```python
from sys    import argv
from typing import ClassVar, NoReturn

from pyTooling.TerminalUI import TerminalApplication

class Application(TerminalApplication):
  HEADLINE: ClassVar[str] = "My Application"

  def Run(self) -> None:
...

</details>

### api4jenkins

Jenkins Python Client

`pip install api4jenkins` · installs (wheel) · licence: Apache Software License · rank 12866 · last release 2025-11-19 · [PyPI](https://pypi.org/project/api4jenkins/) · [docs](https://api4jenkins.readthedocs.io) · [source](https://github.com/joelee2012/api4jenkins)

<details><summary>README extract</summary>

Python3 client library for Jenkins API which provides sync and async APIs.

Features:
- Provides sync and async APIs
- Object oriented, each Jenkins item has corresponding class, easy to use and extend
- Base on `api/json`, easy to query/filter attribute of item
- Setup relationship between class just like Jenkins item ...

Example:
```python
>>> from api4jenkins import Jenkins
>>> client = Jenkins(' auth=('admin', 'admin'))
>>> client.version
'2.176.2'
>>> xml = """<?xml version='1.1' encoding='UTF-8'?>
... <project>
...   <builders>
...     <hudson.tasks.Shell>
...       <command>echo $JENKINS_VERSION</command>
...     </hudson.tasks.Shell>
...   </builders>
... </project>"""
...
```

Sections: Jenkins Python Client, Features, Quick start, Documentation

</details>

### endec

Web-compatible encoding and decoding library

`pip install endec` · installs (wheel) · licence: MIT License · rank 12889 · last release 2026-10-15 · [PyPI](https://pypi.org/project/endec/) · [source](https://github.com/fluxth/endec)

<details><summary>README extract</summary>

Web-compatible encoding and decoding library

endec uses `encoding_rs` (which powers Firefox) under the hood.

Example:
```python
import endec

utf8_bytes = endec.encode("こんにちは")
assert utf8_bytes == b"\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf"

iso2022jp_bytes = endec.encode("㊤㊥㊦", "iso-2022-jp")
assert iso2022jp_bytes == b"\x1b$B-e-f-g\x1b(B"

"㊤㊥㊦".encode("iso-2022-jp")  # Standard Library `encode`
...
```

Sections: endec, Using uv package manager (recommended), Using Poetry package manager, Using pip, Examples, Codecs, Encode, Decode, Error Handling

</details>

### random-password-generator

Simple and custom random password generator for python

`pip install random-password-generator` · installs (wheel) · licence: MIT License · rank 12935 · last release 2021-07-12 · [PyPI](https://pypi.org/project/random-password-generator/)

<details><summary>README extract</summary>

* No dependencies.
 * Generate a simple password of default length 6-16.
 * Generate a password with custom properties.
 * Generate a password from given characters.
 * Generate Non Duplicate Password.
 * Available at (API and WEB versions are available @ repo)

Example:
```python
from password_generator import PasswordGenerator

pwo = PasswordGenerator()
pwo.generate()
```

Sections: Random password Generator, A minimal and custom random password generator., [NOTICE] API and WEB versions are now moved to, Usage, Configuration, Update V2.2.0, Update V2.1.0, Update V1.1.0, Generate a custom password, Generate a password from given characters, Generate Non Duplicate Password

</details>

### koji

Koji is a system for building and tracking RPMS. The base package contains shared libraries and the command-line interface.

`pip install koji` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 12998 · last release 2026-07-08 · [PyPI](https://pypi.org/project/koji/)

_README extract left out: share-alike licence._

### openshift-client

OpenShift python client

`pip install openshift-client` · installs (wheel) · licence: Apache Software License · rank 13011 · last release 2026-10-28 · [PyPI](https://pypi.org/project/openshift-client/)

<details><summary>README extract</summary>

<!-- Install doctoc with `npm install -g doctoc` then `doctoc README.md --github` -->

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
Table of Contents *generated with DocToc*

- Overview
- Reader Prerequisites ...

Features:
The openshift-client-python library aims to provide a readable, concise, comprehensive, and fluent
API for rich interactions with an OpenShift cluster. ...

Example:
```python
# !/usr/bin/python
import openshift_client as oc

print('OpenShift client version: {}'.format(oc.get_client_version()))
print('OpenShift server version: {}'.format(oc.get_server_version()))

# Set a project context for all inner `oc` invocations and limit execution to 10 minutes
...

</details>

### pyrosm

A Python tool to parse OSM data from Protobuf format into GeoDataFrame.

`pip install pyrosm` · installs (wheel) · licence: BSD-3-Clause AND MIT AND ISC · rank 13039 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pyrosm/) · [docs](https://pyrosm.readthedocs.org/)

<details><summary>README extract</summary>

Pyrosm is a Python library for reading OpenStreetMap data from Protocolbuffer Binary Format -files (`*.osm.pbf`) into Geopandas GeoDataFrames.
Pyrosm makes it easy to extract various datasets from OpenStreetMap pbf-dumps including e.g. road networks, buildings,
Points of Interest (POI), landuse and natural elements. ...

Sections: Pyrosm – Python’s Rapid OSM Parser, Current features, Troubleshooting, When should I use Pyrosm?, How to use?, Download responsibly, Citing pyrosm

</details>

### protoc-wheel-0

Google Protocol buffers compiler

`pip install protoc-wheel-0` · installs (wheel) · licence: BSD License · rank 13259 · last release 2025-04-04 · [PyPI](https://pypi.org/project/protoc-wheel-0/)

### fastapi-camelcase

Package provides an easy way to have camelcase request/response bodies for Pydantic

`pip install fastapi-camelcase` · installs from source (sdist only) · licence: MIT License · rank 13366 · last release 2023-12-09 · [PyPI](https://pypi.org/project/fastapi-camelcase/) · [docs](https://nf1s.github.io/fastapi-camelcase/) · [source](https://github.com/nf1s/fastapi-camelcase)

<details><summary>README extract</summary>

Package for providing a class for camelizing request and response bodies for fastapi
while keeping your python code snake cased.

Full documentation can be found here

Example:
```python
# using CamelModel instead of Pydantic BaseModel
from fastapi_camelcase import CamelModel

class User(CamelModel):
    first_name: str
    last_name: str
    age: int
```

Sections: Fastapi Camelcase, Dependencies, How to use, How to use (full example)

</details>

### aws-sso-util

Utilities to make AWS SSO easier

`pip install aws-sso-util` · installs (wheel) · licence: Apache Software License · rank 13425 · last release 2024-06-02 · [PyPI](https://pypi.org/project/aws-sso-util/) · [source](https://github.com/benkehoe/aws-sso-util)

<details><summary>README extract</summary>

AWS IAM Identity Center (formerly AWS SSO) has some rough edges, and `aws-sso-util` is here to smooth them out, hopefully temporarily until AWS makes it better.

`aws-sso-util` contains utilities for the following:
* Configuring `.aws/config`
* Logging in/out
* AWS SDK support
* Looking up identifiers
* CloudFormation ...

Sections: aws-sso-util, Making life with Identity Center a little easier, Quickstart, Documentation

</details>

### asyncpraw

Asynchronous Python Reddit API Wrapper.

`pip install asyncpraw` · installs (wheel) · licence: BSD License · rank 13644 · last release 2026-08-12 · [PyPI](https://pypi.org/project/asyncpraw/) · [docs](https://asyncpraw.readthedocs.io/) · [source](https://github.com/praw-dev/asyncpraw)

<details><summary>README extract</summary>

Async PRAW, an abbreviation for "Asynchronous Python Reddit API Wrapper", is a Python
package that allows for simple access to Reddit's API. Async PRAW aims to be easy to use
and internally follows all of Reddit's API rules. With Async PRAW there's no need to
introduce `sleep` calls in your code. ...

Example:
```python
import asyncpraw

reddit = asyncpraw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    password="PASSWORD",
    user_agent="USERAGENT",
    username="USERNAME",
)
```

Sections: Async PRAW: The Asynchronous Python Reddit API Wrapper, Quickstart, Documentation

</details>

### ry

ry == rust | python

`pip install ry` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 13703 · last release 2026-11-06 · [PyPI](https://pypi.org/project/ry/) · [docs](https://ryo3.dev) · [source](https://github.com/jessekrubin/ry)

<details><summary>README extract</summary>

python bindings for rust crates ~ `ry == rust | python`

DOCS: ryo3.dev (WIP)

API: ryo3.dev/api

This is a work in progress ~ feedback and PRs are welcome.

- Async/Blocking http-clients: Built on `reqwest`, with a `fetch`-like API. ...

Sections: ry, What it do!?, Quickstart, What?, Who?, FAQ, Crate bindings, DEV, SEE ALSO

</details>

### contexttimer

A timer context manager measuring the clock wall time of the code block it contains.

`pip install contexttimer` · installs from source (sdist only) · licence: GNU General Public License v3 (GPLv3) · rank 13736 · last release 2016-09-02 · [PyPI](https://pypi.org/project/contexttimer/)

_README extract left out: share-alike licence._

### django-multi-email-field

Provides a model field and a form field to manage list of e-mails

`pip install django-multi-email-field` · installs (wheel) · licence: not stated · rank 13763 · last release 2025-05-16 · [PyPI](https://pypi.org/project/django-multi-email-field/)

<details><summary>README extract</summary>

Field and widget to store a list of e-mail addresses in a Django project.

It provides:

* A form field and a form widget to edit a list of e-mails in a Django form;
* A model field to store the captured list of e-mails;

* Python 3.9+
* Django 4.2+

Example:
```python
# forms.py
from django import forms
from multi_email_field.forms import MultiEmailField

class SendMessageForm(forms.Form):
    emails = MultiEmailField()
```

Sections: COMPATIBILITY, USAGE, IN YOUR MODELS

</details>

### hopsworks

Hopsworks Python SDK to interact with Hopsworks Platform, Feature Store, Model Registry and Model Serving

`pip install hopsworks` · installs (wheel) · licence: Apache Software License · rank 14418 · last release 2026-11-04 · [PyPI](https://pypi.org/project/hopsworks/) · [docs](https://docs.hopsworks.ai/latest) · [source](https://github.com/logicalclocks/hopsworks-api)

<details><summary>README extract</summary>

*hopsworks* is the python API for interacting with a Hopsworks cluster. Don't have a Hopsworks cluster just yet? Register an account on Hopsworks SaaS and get started. Once connected to your project, you can: ...

Features:
Access the Feature Store of your project to use as a central repository for your feature data. Use *your* favourite data engineering library (pandas, polars, Spark, etc...) to insert data into the Feature Store, create training datasets or serve ...

Example:
```python
import hopsworks

project = hopsworks.login()
```

Sections: Hopsworks Client, Getting Started On Hopsworks, Feature Store API, Machine Learning API, Usage, Tutorials, Documentation, Issues

</details>

### lazyasd

Lazy & self-destructive tools for speeding up module imports

`pip install lazyasd` · installs from source (sdist only) · licence: OSI Approved · rank 14427 · last release 2018-03-21 · [PyPI](https://pypi.org/project/lazyasd/)

<details><summary>README extract</summary>

A package that provides lazy and self-destructive tools for speeding up module
imports. This is useful whenever startup times are critical, such as for
command line interfaces or other user-facing applications.

The tools in this module implement two distinct strategies for speeding up
module import. ...

Example:
```python
import re

def has_foo_simple(s):
    return re.search('foo', s) is not None
```

Sections: lazyasd, Lazy Construction, Specific Laziness, Background Imports

</details>

### typing-aliases

Various type aliases.

`pip install typing-aliases` · installs (wheel) · licence: MIT License · rank 14523 · last release 2024-04-22 · [PyPI](https://pypi.org/project/typing-aliases/) · [docs](https://nekitdev.github.io/typing-aliases) · [source](https://github.com/nekitdev/typing-aliases)

<details><summary>README extract</summary>

[][License]
[][Package]
[][Package]
[][Discord]

[][Documentation]
[][Actions]

> *Various type aliases.*

Sections: `typing-aliases`, pip, poetry, Documentation

</details>

### django-admin-sortable

Drag and drop sorting for models and inline models in Django admin.

`pip install django-admin-sortable` · installs from source (sdist only) · licence: Apache Software License · rank 14546 · last release 2021-12-22 · [PyPI](https://pypi.org/project/django-admin-sortable/)

<details><summary>README extract</summary>

This project makes it easy to add drag-and-drop ordering to any model in
Django admin. Inlines for a sortable model may also be made sortable,
enabling individual items or groups of items to be sortable.

If you find Django Admin Sortable to be helpful, consider buying me a
coffee!

Sorting model instances with a sortable parent:

Sorting inlines:

Example:
```python
# models.py
from adminsortable.models import SortableMixin

class MySortableClass(SortableMixin):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'My Sortable Class'
        verbose_name_plural = 'My Sortable Classes'
        ordering = ['the_order']

    # define the field the model should be ordered by
...
```

...

</details>

### solus

Singleton types.

`pip install solus` · installs (wheel) · licence: MIT License · rank 14619 · last release 2024-02-26 · [PyPI](https://pypi.org/project/solus/) · [docs](https://nekitdev.github.io/solus) · [source](https://github.com/nekitdev/solus)

<details><summary>README extract</summary>

[][License]
[][Package]
[][Package]
[][Discord]

[][Documentation]
[][Actions]
[][Actions]
[][Coverage]

> *Singleton types.*

Example:
```python
from solus import Singleton

class Null(Singleton):
    ...
```

Sections: `solus`, pip, poetry, Examples, Default, Unsafe, Warning, Documentation

</details>

### multiline-log-formatter

Python logging formatter that prefix multiline log message and trackebacks.

`pip install multiline-log-formatter` · installs (wheel) · licence: BSD License · rank 14662 · last release 2016-01-15 · [PyPI](https://pypi.org/project/multiline-log-formatter/)

<details><summary>README extract</summary>

Features:
Python logging formatter that prefix multiline log message and trackebacks. Makes the logs more readable, both for
tracebacks and for multiline log messages.

* Free software: BSD license

Sections: Overview, Benchmarking, Usage, Documentation, Other, 0.1.8 (2016-01-15)

</details>

### entrypoint

Decorated functions as entry points.

`pip install entrypoint` · installs (wheel) · licence: MIT License · rank 14686 · last release 2024-06-16 · [PyPI](https://pypi.org/project/entrypoint/) · [docs](https://nekitdev.github.io/entrypoint) · [source](https://github.com/nekitdev/entrypoint)

<details><summary>README extract</summary>

[][License]
[][Package]
[][Package]
[][Discord]

[][Documentation]
[][Actions]
[][Actions]
[][Coverage]

> *Decorated functions as entry points.*

In python, an *entry point* can be thought of as an explicit function
that gets called when the script is run directly from the console. ...

Example:
```python
from entrypoint import entrypoint

@entrypoint(name)
def main() -> None:
    print("Hello, world!")
```

Sections: `entrypoint`, pip, poetry, Examples, Decorated, Note, Direct, Check, Return, Async, Implicit, Documentation

</details>

### pip-compile-multi

Compile multiple requirements files to lock dependency versions

`pip install pip-compile-multi` · installs (wheel) · licence: MIT · rank 14699 · last release 2026-10-03 · [PyPI](https://pypi.org/project/pip-compile-multi/)

<details><summary>README extract</summary>

Compile multiple requirements files to lock dependency versions.

Sections: pip-compile-multi, Run, Links, 3.3.2 (2026-10-02), 3.3.1 (2025-04-19), 3.3.0 (2025-03-25), 3.2.2 (2025-06-19), 3.2.1 (2025-06-19), 3.2.0 (2025-06-17), 3.1.0 (2025-05-23), 3.0.0 (2025-04-23), 2.8.0 (2024-11-27), 2.7.0 (2024-11-27), 2.6.4 (2023-06-06)

</details>

### versions

Parsing, inspecting and specifying versions.

`pip install versions` · installs (wheel) · licence: MIT License · rank 14724 · last release 2024-02-26 · [PyPI](https://pypi.org/project/versions/) · [docs](https://nekitdev.github.io/versions) · [source](https://github.com/nekitdev/versions)

<details><summary>README extract</summary>

[][License]
[][Package]
[][Package]
[][Discord]

[][Documentation]
[][Actions]
[][Actions]
[][Coverage]

> *Parsing, inspecting and specifying versions.*

Example:
```python
from versions import parse_version

version = parse_version("1.0.0-dev.1+build.1")

print(version)  # 1.0.0-dev.1+build.1
```

Sections: `versions`, pip, poetry, Examples, Versions, Segments, Comparison, Specification, Versioned, Documentation

</details>

### orderings

Ordering enumeration and protocols.

`pip install orderings` · installs (wheel) · licence: MIT License · rank 14759 · last release 2024-06-05 · [PyPI](https://pypi.org/project/orderings/) · [docs](https://nekitdev.github.io/orderings) · [source](https://github.com/nekitdev/orderings)

<details><summary>README extract</summary>

[][License]
[][Package]
[][Package]
[][Discord]

[][Documentation]
[][Actions]
[][Actions]
[][Coverage]

> *Ordering enumeration and protocols.*

Example:
```python
from typing import Generic, TypeVar

from attrs import frozen
from orderings import Compare, Ordered, Ordering, compare
from typing_extensions import Self

T = TypeVar("T", bound=Ordered)

@frozen()
class Wrap(Compare, Generic[T]):
    value: T

    def compare(self, other: Self) -> Ordering:
        return compare(self.value, other.value)
```

Sections: `orderings`, `pip`, `poetry`, Motivation, Examples, Core, Documentation

</details>

### robotcode-runner

RobotCode runner for Robot Framework

`pip install robotcode-runner` · installs (wheel) · licence: Apache-2.0 · rank 14778 · last release 2026-10-26 · [PyPI](https://pypi.org/project/robotcode-runner/) · [docs](https://github.com/robotcodedev/robotcode#readme) · [source](https://github.com/robotcodedev/robotcode)

<details><summary>README extract</summary>

Test execution and runner utilities for Robot Framework in RobotCode.

This package is part of the RobotCode project. The complete source code is available at github.com/robotcodedev/robotcode.

Sections: robotcode-runner, Introduction, Documentation

</details>

### cdflib

A python CDF reader toolkit

`pip install cdflib` · installs (wheel) · licence: not stated · rank 14782 · last release 2026-10-21 · [PyPI](https://pypi.org/project/cdflib/)

<details><summary>README extract</summary>

`cdflib` is a python module to read/write CDF (Common Data Format `.cdf`) files without needing to install the
CDF NASA library.

Python >= 3.9 is required.
The core of this package uses only numpy, with no complicated compiler requirements.

Sections: CDFlib, Documentation

</details>

### pip-upgrader

An interactive pip requirements upgrader. It also updates the version in your requirements.txt file.

`pip install pip-upgrader` · installs (wheel) · licence: Apache-2.0 · rank 14783 · last release 2026-08-10 · [PyPI](https://pypi.org/project/pip-upgrader/)

<details><summary>README extract</summary>

An interactive pip requirements upgrader. Because upgrading
requirements, package by package, is a pain in the ass. It also updates
the version in your requirements.txt, pyproject.toml, and Pipfile files. ...

Sections: pip-upgrader, Purpose, Usage, Releasing

</details>

### robotcode-modifiers

Some Robot Framework Modifiers for RobotCode

`pip install robotcode-modifiers` · installs (wheel) · licence: Apache-2.0 · rank 14794 · last release 2026-10-26 · [PyPI](https://pypi.org/project/robotcode-modifiers/) · [docs](https://github.com/robotcodedev/robotcode#readme) · [source](https://github.com/robotcodedev/robotcode)

<details><summary>README extract</summary>

Robot Framework execution modifiers for RobotCode.

This package is part of the RobotCode project. The complete source code is available at github.com/robotcodedev/robotcode.

Sections: robotcode-modifiers, Introduction, Documentation

</details>

### depinfo

List any package's direct dependencies and their versions.

`pip install depinfo` · installs (wheel) · licence: Apache Software License · rank 14803 · last release 2022-09-07 · [PyPI](https://pypi.org/project/depinfo/) · [source](https://github.com/Midnighter/dependency-info)

<details><summary>README extract</summary>

Example:
```python
from depinfo.application import DisplayApplication

DisplayApplication.run("depinfo")
```

Sections: Package Dependency Information, Example, Copyright

</details>

## Also in this topic

- [idna](internet-name-service-dns.md#idna) - Internationalized Domain Names in Applications (IDNA)
- [charset-normalizer](text-processing-linguistic.md#charset-normalizer) - The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet.
- [pluggy](software-development-libraries.md#pluggy) - plugin and hook calling mechanisms for python
- [Pygments](text-processing-filters.md#pygments) - Pygments is a syntax highlighting package written in Python.
- [six](software-development-libraries.md#six) - Python 2 and 3 compatibility utilities
- [setuptools](software-development-libraries.md#setuptools) - Most extensible Python build backend with support for C/C++ extension modules
- [pytest](software-development-libraries.md#pytest) - pytest: simple powerful testing with Python
- [iniconfig](software-development-libraries.md#iniconfig) - brain-dead simple config-ini parsing
- [python-dotenv](system-systems-administration.md#python-dotenv) - Read key-value pairs from a .env file and set them as environment variables
- [pathspec](software-development-libraries.md#pathspec) - Utility library for gitignore style pattern matching of file paths.
- [tqdm](desktop-environment.md#tqdm) - Fast, Extensible Progress Meter
- [psutil](software-development-libraries.md#psutil) - Cross-platform lib for process and system monitoring.
- [editables](software-development-libraries.md#editables) - Editable installations
- [virtualenv](software-development-libraries.md#virtualenv) - Virtual Python Environment builder
- [pytest-cov](software-development-testing.md#pytest-cov) - Pytest plugin for measuring coverage.
- [python-discovery](software-development-libraries.md#python-discovery) - Python interpreter discovery
- [joblib](scientific-engineering.md#joblib) - Lightweight pipelining with Python functions
- [pytest-xdist](software-development-quality-assurance.md#pytest-xdist) - pytest xdist plugin for distributed testing, most importantly across multiple CPUs
- [decorator](software-development-libraries.md#decorator) - Decorators for Humans
- [jsonpointer](software-development-libraries.md#jsonpointer) - Identify specific nodes in a JSON document (RFC 6901)
- [backoff](internet-www-http.md#backoff) - Function decoration for backoff and retry
- [docutils](documentation.md#docutils) - Docutils -- Python Documentation Utilities
- [docker](software-development.md#docker) - A Python library for the Docker Engine API.
- [jsonpatch](software-development-libraries.md#jsonpatch) - Apply JSON-Patches (RFC 6902)
- [pymupdf](multimedia-graphics.md#pymupdf) - A high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents.
- [gunicorn](internet.md#gunicorn) - WSGI HTTP Server for UNIX
- [jedi](software-development-libraries.md#jedi) - An autocompletion tool for Python that can be used for text editors.
- [parso](software-development-libraries.md#parso) - A Python Parser
- [brotli](software-development-libraries.md#brotli) - Python bindings for the Brotli compression library
- [watchdog](software-development-libraries.md#watchdog) - Filesystem events monitoring
- [isort](software-development-libraries.md#isort) - A Python utility / library to sort Python imports.
- [griffelib](documentation.md#griffelib) - Signatures for entire Python programs. Extract the structure, the frame, the skeleton of your project, to generate API documentation or find breaking changes in your API.
- [setuptools-scm](software-development-libraries.md#setuptools-scm) - the blessed package to manage your versions by scm tags
- [Faker](software-development-libraries.md#faker) - Faker is a Python package that generates fake data for you.
- [mmh3](software-development-libraries.md#mmh3) - Python extension for MurmurHash (MurmurHash3), a set of fast and robust hash functions.
- [pyflakes](software-development.md#pyflakes) - passive checker of Python programs
- [humanfriendly](communications.md#humanfriendly) - Human friendly output for text interfaces using Python
- [colorlog](terminals.md#colorlog) - Add colours to the output of Python's logging module.
- [boolean.py](scientific-engineering-mathematics.md#booleanpy) - Define boolean algebras, create and parse boolean expressions and create custom boolean DSL.
- [license-expression](software-development.md#license-expression) - license-expression is a comprehensive utility library to parse, compare, simplify and normalize license expressions (such as SPDX license expressions) using boolean logic.
- [py](software-development-libraries.md#py) - library with cross-python path, ini-parsing, io, code, log facilities
- [fqdn](internet.md#fqdn) - Validates fully-qualified domain names against RFC 1123, so that they are acceptable to modern browsers
- [packageurl-python](software-development-libraries.md#packageurl-python) - A purl aka. Package URL parser and builder
- [filetype](system.md#filetype) - Infer file type and MIME type of any file/buffer. No external dependencies.
- [pytest-rerunfailures](software-development-quality-assurance.md#pytest-rerunfailures) - pytest plugin to re-run tests to eliminate flaky failures
- [coloredlogs](communications.md#coloredlogs) - Colored terminal output for Python's logging module
- [pip-requirements-parser](software-development.md#pip-requirements-parser) - pip requirements parser - a mostly correct pip requirements parsing library because it uses pip's own code.
- [rfc3987-syntax](scientific-engineering.md#rfc3987-syntax) - Helper functions to syntactically validate strings according to RFC 3987.
- [boltons](software-development-libraries.md#boltons) - When they're not builtins, they're boltons.
- [glom](software-development-libraries.md#glom) - A declarative object transformer and formatter, for conglomerating nested data.
- [face](software-development-libraries.md#face) - A command-line application framework (and CLI parser). Friendly for users, full-featured for developers.
- [griffe](documentation.md#griffe) - Signatures for entire Python programs. Extract the structure, the frame, the skeleton of your project, to generate API documentation or find breaking changes in your API.
- [retrying](internet.md#retrying) - Retrying
- [pytest-metadata](software-development-quality-assurance.md#pytest-metadata) - pytest plugin for test session metadata
- [jsonconversion](internet-www-http.md#jsonconversion) - This python module helps converting arbitrary Python objects into JSON strings and back.
- [pybind11](software-development-libraries.md#pybind11) - Seamless operability between C++11 and Python
- [pybase64](software-development-libraries.md#pybase64) - Fast Base64 encoding/decoding
- [texttable](software-development-libraries.md#texttable) - module to create simple ASCII tables
- [Sphinx](documentation.md#sphinx) - Python documentation generator
- [hyperlink](software-development-libraries.md#hyperlink) - A featureful, immutable, and correct URL for Python.
- [py-spy](software-development-libraries.md#py-spy) - 
- [sphinxcontrib-serializinghtml](documentation.md#sphinxcontrib-serializinghtml) - sphinxcontrib-serializinghtml is a sphinx extension which outputs "serialized" HTML files (json and pickle)
- [sphinxcontrib-jsmath](documentation.md#sphinxcontrib-jsmath) - sphinxcontrib-jsmath is a sphinx extension which renders displayed maths in HTML via JavaScript
- [progressbar2](desktop-environment.md#progressbar2) - A Python Progressbar library to provide visual (yet text based) progress to long running operations.
- [sphinxcontrib-htmlhelp](documentation.md#sphinxcontrib-htmlhelp) - sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files
- [sphinxcontrib-applehelp](documentation.md#sphinxcontrib-applehelp) - sphinxcontrib-applehelp is a Sphinx extension which outputs Apple help books
- [sphinxcontrib-qthelp](documentation.md#sphinxcontrib-qthelp) - sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp documents
- [sphinxcontrib-devhelp](documentation.md#sphinxcontrib-devhelp) - sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp documents
- [pydub](multimedia-sound-audio.md#pydub) - Manipulate audio with an simple and easy high level interface
- [genson](file-formats-json.md#genson) - GenSON is a powerful, user-friendly JSON Schema generator.
- [tox](software-development-libraries.md#tox) - tox is a generic virtualenv management and test command line tool
- [blake3](security.md#blake3) - Python bindings for the Rust blake3 crate
- [natsort](scientific-engineering-information-analysis.md#natsort) - Simple yet flexible natural sorting in Python.
- [ansible-core](system-installation-setup.md#ansible-core) - Radically simple IT automation
- [jsonlines](internet-log-analysis.md#jsonlines) - Library with helpers for the jsonlines file format
- [pytest-html](software-development-quality-assurance.md#pytest-html) - pytest plugin for generating HTML reports
- [frozendict](software-development-libraries.md#frozendict) - A simple immutable dictionary
- [trafilatura](internet-www-http.md#trafilatura) - Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extraction, output as CSV, JSON, HTML, MD, TXT, XML.
- [pytest-repeat](software-development-quality-assurance.md#pytest-repeat) - pytest plugin for repeating tests
- [pip-tools](software-development-quality-assurance.md#pip-tools) - pip-tools keeps your pinned dependencies fresh.
- [griffecli](documentation.md#griffecli) - Signatures for entire Python programs. Extract the structure, the frame, the skeleton of your project, to generate API documentation or find breaking changes in your API.
- [pyroscope-io](software-development.md#pyroscope-io) - Pyroscope Python integration
- [pyproject-api](software-development-libraries.md#pyproject-api) - API to interact with the python pyproject.toml based projects
- [polyfactory](software-development.md#polyfactory) - Mock data generation factories
- [syrupy](software-development-libraries.md#syrupy) - Pytest Snapshot Test Utility
- [django-redis](software-development-libraries.md#django-redis) - Full featured redis cache backend for Django.
- [sqlfluff](software-development-quality-assurance.md#sqlfluff) - The SQL Linter for Humans
- [detect-secrets](software-development.md#detect-secrets) - Tool for detecting secrets in the codebase
- [pcodedmp](security.md#pcodedmp) - A VBA p-code disassembler
- [cytoolz](scientific-engineering.md#cytoolz) - Cython implementation of Toolz: High performance functional utilities
- [pyinstaller](software-development.md#pyinstaller) - PyInstaller bundles a Python application and all its dependencies into a single package.
- [pglast](database.md#pglast) - PostgreSQL Languages AST and statements prettifier
- [pytest-base-url](software-development-quality-assurance.md#pytest-base-url) - pytest plugin for URL based testing
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [tritonclient](scientific-engineering.md#tritonclient) - Python client library and utilities for communicating with Triton Inference Server
- [atpublic](software-development-libraries.md#atpublic) - Keep all y'all's __all__'s in sync
- [segno](multimedia-graphics.md#segno) - QR Code and Micro QR Code generator for Python
- [jsii](software-development-libraries.md#jsii) - Python client for jsii runtime
- [django-environ](software-development-libraries.md#django-environ) - A package that allows you to utilize 12factor inspired environment variables to configure your Django application.
- [crcmod](communications.md#crcmod) - CRC Generator
- [atlassian-python-api](internet.md#atlassian-python-api) - Python Atlassian REST API Wrapper
- [pytest-sugar](software-development-libraries.md#pytest-sugar) - pytest-sugar is a plugin for pytest that changes the default look and feel of pytest (e.g. progressbar, show tests that fail instantly).
- [pydash](software-development-libraries.md#pydash) - The kitchen sink of Python utility libraries for doing "stuff" in a functional way. Based on the Lo-Dash Javascript library.
- [mkdocs-autorefs](documentation.md#mkdocs-autorefs) - Automatically link across pages in MkDocs.
- [mkdocstrings](documentation.md#mkdocstrings) - Automatic documentation from sources, for MkDocs.
- [mkdocstrings-python](documentation.md#mkdocstrings-python) - A Python handler for mkdocstrings.
- [aws-sam-translator](internet.md#aws-sam-translator) - AWS SAM Translator is a library that transform SAM templates into AWS CloudFormation templates
- [pprintpp](software-development.md#pprintpp) - A drop-in replacement for pprint that's actually pretty
- [flexparser](software-development-libraries.md#flexparser) - Parsing made fun ... using typing.
- [flexcache](software-development-libraries.md#flexcache) - Saves and loads to the cache a transformed versions of a source object.
- [fake-useragent](internet-www-http.md#fake-useragent) - Up-to-date simple useragent faker with real world database
- [pytest-testmon](software-development-libraries.md#pytest-testmon) - selects tests affected by changed files and methods
- [mando](software-development.md#mando) - Create Python CLI apps with little to no effort at all!
- [radon](software-development.md#radon) - Code Metrics in Python
- [bokeh](office-business.md#bokeh) - Interactive plots and applications in the browser from Python
- [databricks-labs-dqx](software-development-libraries.md#databricks-labs-dqx) - Data Quality eXtended (DQX) is a Python library for data quality checks and data quality monitoring
- [svglib](documentation.md#svglib) - A pure-Python library for reading and converting SVG
- [publicsuffix2](internet-name-service-dns.md#publicsuffix2) - Get a public suffix for a domain name using the Public Suffix List. Forked from and using the same API as the publicsuffix package.
- [discord.py](internet.md#discordpy) - A Python wrapper for the Discord API
- [python-box](software-development.md#python-box) - Advanced Python dictionaries with dot notation access
- [subprocess-tee](system-systems-administration.md#subprocess-tee) - subprocess-tee
- [dynaconf](software-development-libraries.md#dynaconf) - The dynamic configurator for your Python Project
- [libtmux](software-development-libraries.md#libtmux) - Typed library that provides an ORM wrapper for tmux, a terminal multiplexer.
- [pyaml](software-development.md#pyaml) - PyYAML-based module to produce a bit more pretty and readable YAML-serialized data
- [ansible-compat](software-development-bug-tracking.md#ansible-compat) - Ansible compatibility goodies
- [spdx-tools](software-development-documentation.md#spdx-tools) - SPDX parser and tools.
- [pytest-order](software-development-quality-assurance.md#pytest-order) - pytest plugin to run tests in a specific order
- [pex](software-development-build-tools.md#pex) - The PEX packaging toolchain.
- [sqlparams](database.md#sqlparams) - Convert between various DB API 2.0 parameter styles.
- [pytest-forked](software-development-quality-assurance.md#pytest-forked) - run tests in isolated forked subprocesses
- [yaspin](software-development.md#yaspin) - Yet Another Terminal Spinner
- [crcmod-plus](communications.md#crcmod-plus) - CRC generator - modernized
- [tinydb](database.md#tinydb) - TinyDB is a tiny, document oriented database optimized for your happiness :)
- [bc-detect-secrets](software-development.md#bc-detect-secrets) - Tool for detecting secrets in the codebase
- [semchunk](scientific-engineering-artificial-intelligence.md#semchunk) - A Python library for splitting text into smaller chunks while preserving as much local semantic context as possible.
- [ansible-lint](software-development-quality-assurance.md#ansible-lint) - Checks playbooks for practices and behavior that could potentially be improved
- [xhtml2pdf](documentation.md#xhtml2pdf) - PDF generator using HTML and CSS
- [pdfkit](text-processing.md#pdfkit) - Wkhtmltopdf python wrapper to convert html to pdf using the webkit rendering engine and qt
- [django-health-check](software-development-quality-assurance.md#django-health-check) - Monitor the health of your Django app and its connected services.
- [pdfrw](multimedia-graphics.md#pdfrw) - PDF file reader/writer library
- [hijridate](scientific-engineering.md#hijridate) - Accurate Hijri-Gregorian dates converter based on Umm al-Qura calendar
- [formulas](scientific-engineering.md#formulas) - Parse and compile Excel formulas and workbooks in python code.
- [schedula](scientific-engineering.md#schedula) - Produce a plan that dispatches calls based on a graph of functions, satisfying data dependencies.
- [shtab](desktop-environment.md#shtab) - Automagic shell tab completion for Python CLI applications
- [pyunormalize](software-development-internationalization.md#pyunormalize) - A library for Unicode normalization (NFC, NFD, NFKC, NFKD) independent of Python's core Unicode database.
- [magic-wormhole](security-cryptography.md#magic-wormhole) - Securely transfer data between computers
- [recurring-ical-events](office-business-scheduling.md#recurring-ical-events) - Calculate recurrence times of events, todos, alarms and journals based on icalendar RFC5545.
- [x-wr-timezone](software-development-libraries.md#x-wr-timezone) - Repair Google Calendar - This Python module and program makes ICS/iCalendar files using X-WR-TIMEZONE compatible with the RFC 5545 standard.
- [pytest-github-actions-annotate-failures](software-development-quality-assurance.md#pytest-github-actions-annotate-failures) - pytest plugin to annotate failed tests with a workflow command for GitHub Actions
- [pytest-bdd](software-development-libraries.md#pytest-bdd) - BDD for pytest
- [pytimeparse2](software-development-libraries.md#pytimeparse2) - Time expression parser.
- [pytest-check](software-development-testing.md#pytest-check) - A pytest plugin that allows multiple failures per test.
- [pytest-unordered](software-development-libraries.md#pytest-unordered) - Test equality of unordered collections in pytest
- [pytest-factoryboy](software-development-libraries.md#pytest-factoryboy) - Factory Boy support for pytest.
- [rjsmin](internet-www-http.md#rjsmin) - Javascript Minifier
- [gcovr](software-development.md#gcovr) - Generate C/C++ code coverage reports with gcov
- [wget](software-development-libraries.md#wget) - pure python download utility
- [python-can](software-development-embedded-systems.md#python-can) - Controller Area Network interface module for Python
- [rcssmin](internet-www-http.md#rcssmin) - CSS Minifier
- [asciinema](system-shells.md#asciinema) - Terminal session recorder
- [sphinxcontrib-mermaid](documentation.md#sphinxcontrib-mermaid) - Mermaid diagrams in your Sphinx-powered docs
- [javaproperties](software-development.md#javaproperties) - Read & write Java .properties files
- [commonmark](documentation.md#commonmark) - Python parser for the CommonMark Markdown spec
- [sqlfluff-templater-dbt](software-development-quality-assurance.md#sqlfluff-templater-dbt) - Lint your dbt project SQL
- [pyspellchecker](software-development-libraries.md#pyspellchecker) - Pure python spell checker based on work by Peter Norvig
- [html-for-docx](software-development-build-tools.md#html-for-docx) - Convert HTML to DOCX easily and quickly
- [about-time](software-development-user-interfaces.md#about-time) - Easily measure timing and throughput of code blocks, with beautiful human friendly representations.
- [pytest-codspeed](software-development-testing.md#pytest-codspeed) - Pytest plugin to create CodSpeed benchmarks
- [pytest-instafail](software-development-libraries.md#pytest-instafail) - pytest plugin to show failures instantly
- [word2number](documentation-sphinx.md#word2number) - Convert number words eg. three hundred and forty two to numbers (342).
- [expandvars](software-development.md#expandvars) - Expand system variables Unix style
- [loky](scientific-engineering.md#loky) - A robust implementation of concurrent.futures.ProcessPoolExecutor
- [munch](software-development.md#munch) - A dot-accessible dictionary (a la JavaScript objects)
- [nanobind](software-development-libraries.md#nanobind) - nanobind: tiny and efficient C++/Python bindings
- [uncertainties](education.md#uncertainties) - calculations with values with uncertainties, error propagation
- [runtype](software-development-libraries.md#runtype) - Type dispatch and validation for run-time Python
- [pypinyin](text-processing.md#pypinyin) - 汉字拼音转换模块/工具.
- [mdutils](software-development-documentation.md#mdutils) - Useful package for creating Markdown files while executing python code.
- [filterpy](scientific-engineering.md#filterpy) - Kalman filtering and optimal estimation library
- [open3d](education.md#open3d) - Open3D: A Modern Library for 3D Data Processing.
- [pytube](internet.md#pytube) - Python 3 library for downloading YouTube Videos.
- [crowdstrike-falconpy](security.md#crowdstrike-falconpy) - The CrowdStrike Falcon SDK for Python
- [rust-just](software-development-build-tools.md#rust-just) - 
- [async-property](software-development.md#async-property) - Python decorator for async properties.
- [casefy](text-processing.md#casefy) - Utilities for string case conversion.
- [line-profiler](software-development-libraries.md#line-profiler) - Line-by-line profiler
- [pyshacl](software-development-libraries.md#pyshacl) - Python SHACL Validator
- [mimesis](software-development.md#mimesis) - Mimesis: Fake Data Generator.
- [PyMuPDFb](multimedia-graphics.md#pymupdfb) - MuPDF shared libraries for PyMuPDF.
- [gsutil](system-filesystems.md#gsutil) - A command line tool for interacting with cloud storage services.
- [mistral-vibe](software-development.md#mistral-vibe) - Minimal CLI coding agent by Mistral
- [svgelements](multimedia-graphics.md#svgelements) - Svg Elements Parsing
- [sphinx-autobuild](documentation.md#sphinx-autobuild) - Rebuild Sphinx documentation on changes, with hot reloading in the browser.
- [pytest-profiling](software-development-libraries-2.md#pytest-profiling) - Profiling plugin for py.test
- [pytest-ordering](software-development-quality-assurance.md#pytest-ordering) - pytest plugin to run your tests in a specific order
- [scrubadub](scientific-engineering-information-analysis.md#scrubadub) - Clean personally identifiable information from dirty dirty text.
- [gnupg](security-cryptography.md#gnupg) - A Python wrapper for GnuPG
- [meshio](scientific-engineering.md#meshio) - I/O for many mesh formats
- [pytest-watcher](software-development-testing.md#pytest-watcher) - Automatically rerun your tests on file modifications
- [pymodbus](system-networking.md#pymodbus) - A fully featured modbus protocol stack in python
- [seleniumbase](internet.md#seleniumbase) - SeleniumBase is a framework for web crawling, scraping, and testing. Supports pytest. CDP Mode adds stealth. Includes many tools.
- [stpyv8](internet.md#stpyv8) - Python Wrapper for Google V8 Engine
- [circular-dict](software-development-debuggers.md#circular-dict) - CircularDict is a high-performance Python data structure that blends the functionality of dictionaries and circular buffers. Inheriting the usage of traditional dictionaries, it allows you to define constraints on size and memory usage. This way, the CircularDict will be always up-to-date with the last N added elements, ensuring that neither the maximum length nor the memory usage limit is exceeded. It is ideal for caching large data structures while maintaining control over memory footprint.
- [pybtex](text-processing-markup.md#pybtex) - A BibTeX-compatible bibliography processor in Python
- [mido](multimedia-sound-audio.md#mido) - MIDI Objects for Python
- [crccheck](scientific-engineering.md#crccheck) - Calculation library for CRCs and checksums
- [confusable-homoglyphs](text-processing.md#confusable-homoglyphs) - Detect confusable usage of unicode homoglyphs, prevent homograph attacks.
- [molecule](software-development-bug-tracking.md#molecule) - Molecule aids in the development and testing of Ansible roles
- [enrich](system-systems-administration.md#enrich) - enrich
- [ansi2html](software-development-quality-assurance.md#ansi2html) - Convert text with ANSI color codes to HTML or to LaTeX
- [awkward-cpp](scientific-engineering.md#awkward-cpp) - CPU kernels and compiled extensions for Awkward Array
- [warcio](software-development-libraries-2.md#warcio) - Streaming WARC (and ARC) IO library
- [pytest-timeouts](software-development-testing.md#pytest-timeouts) - Linux-only Pytest plugin to control durations of various test case execution phases
- [awkward](scientific-engineering.md#awkward) - Manipulate JSON-like data with NumPy-like idioms.
- [ansible-runner](software-development-libraries-2.md#ansible-runner) - "Consistent Ansible Python API and CLI with container and process isolation runtime capabilities"
- [scenedetect](multimedia-video.md#scenedetect) - Video scene cut/shot detection program and Python library (bundles the opencv-python OpenCV variant and the scenedetect CLI).
- [inscriptis](text-processing.md#inscriptis) - inscriptis - HTML to text converter.
- [measurement](scientific-engineering.md#measurement) - Easily use and manipulate unit-aware measurements in Python.
- [simple-term-menu](terminals.md#simple-term-menu) - A Python package which creates simple interactive menus on the command line.
- [usort](software-development.md#usort) - Safe, minimal import sorting
- [markdown-exec](documentation.md#markdown-exec) - Utilities to execute code blocks in Markdown files.
- [sphinx-click](documentation.md#sphinx-click) - Sphinx extension that automatically documents click applications
- [pdbpp](software-development-debuggers.md#pdbpp) - pdb++, a drop-in replacement for pdb
- [davey](software-development-libraries-2.md#davey) - A Discord Audio & Video End-to-End Encryption (DAVE) Protocol implementation
- [salt-lint](software-development-bug-tracking.md#salt-lint) - A command-line utility that checks for best practices in SaltStack.
- [country-converter](scientific-engineering.md#country-converter) - The country converter (coco) - a Python package for converting country names between different classifications schemes
- [valkey-glide](database.md#valkey-glide) - Valkey GLIDE Async client. Supports Valkey and Redis OSS.
- [csscompressor](software-development-build-tools.md#csscompressor) - A python port of YUI CSS Compressor
- [returns](software-development-libraries-2.md#returns) - Make your functions return something meaningful, typed, and safe!
- [pymp4](multimedia-sound-audio.md#pymp4) - Python parser for MP4 boxes
- [xenon](internet-www-http.md#xenon) - Monitor code metrics for Python on your CI server
- [django-treebeard](software-development-libraries-2.md#django-treebeard) - Efficient tree implementations for Django
- [mdx-truly-sane-lists](text-processing-markup.md#mdx-truly-sane-lists) - Extension for Python-Markdown that makes lists truly sane. Custom indents for nested lists and fix for messy linebreaks.
- [aws-sam-cli](internet.md#aws-sam-cli) - AWS SAM CLI is a CLI tool for local development and testing of Serverless applications
- [enum-tools](documentation.md#enum-tools) - Tools to expand Python's enum module.
- [aws-lambda-builders](internet.md#aws-lambda-builders) - Python library to compile, build & package AWS Lambda functions for several runtimes & frameworks.
- [rauth](internet-www-http.md#rauth) - A Python library for OAuth 1.0/a, 2.0, and Ofly.
- [s3cmd](system-archiving.md#s3cmd) - Command line tool for managing Amazon S3 and CloudFront services
- [sphinx-tabs](documentation.md#sphinx-tabs) - Tabbed views for Sphinx
- [certbot](internet-www-http.md#certbot) - ACME client
- [asynciolimiter](internet.md#asynciolimiter) - Rate limiter for Async IO
- [autopage](software-development-libraries-2.md#autopage) - A library to provide automatic paging for console output
- [selinux](system-systems-administration.md#selinux) - shim selinux module
- [pdoc](documentation.md#pdoc) - API Documentation for Python Projects
- [xlsx2csv](office-business.md#xlsx2csv) - xlsx to csv converter
- [boost-histogram](scientific-engineering.md#boost-histogram) - The Boost::Histogram Python wrapper.
- [xdoctest](software-development-libraries-2.md#xdoctest) - A rewrite of the builtin doctest module
- [molecule-plugins](software-development-bug-tracking.md#molecule-plugins) - Molecule Plugins
- [envyaml](software-development-libraries-2.md#envyaml) - Simple YAML configuration file parser with easy access for structured data
- [proxy.py](internet.md#proxypy) - \u26a1 Fast \u2022 \U0001fab6 Lightweight \u2022 \U0001f51f Dependency \u2022 \U0001f50c Pluggable \u2022 \U0001f608 TLS interception \u2022 \U0001f512 DNS-over-HTTPS \u2022 \U0001f525 Poor Mans VPN \u2022 \u23ea Reverse & \u23e9 Forward \u2022 \U0001f46e\U0001f3ff Proxy Server framework \u2022 \U0001f310 Web Server framework \u2022 \u27b5 \u27b6 \u27b7 \u27a0 PubSub framework \u2022 \U0001f477 Work acceptor & executor framework.
- [uproot](scientific-engineering.md#uproot) - ROOT I/O in pure Python and NumPy.
- [art](multimedia.md#art) - ASCII Art Library For Python
- [plac](software-development-libraries-2.md#plac) - The smartest command line arguments parser in the world
- [sigfig](education.md#sigfig) - Python library for rounding numbers (with expected results)
- [google-play-scraper](software-development-libraries-2.md#google-play-scraper) - Google-Play-Scraper provides APIs to easily crawl the Google Play Store for Python without any external dependencies!
- [fastapi-utils](internet.md#fastapi-utils) - Reusable utilities for FastAPI
- [mailjet-rest](communications-email.md#mailjet-rest) - Mailjet V3 API wrapper
- [pyproject-fmt](software-development-quality-assurance.md#pyproject-fmt) - Format pyproject.toml files
- [certbot-dns-cloudflare](internet-www-http.md#certbot-dns-cloudflare) - Cloudflare DNS Authenticator plugin for Certbot
- [ps-mem](system-systems-administration.md#ps-mem) - A utility to report core memory usage per program
- [breathe](documentation.md#breathe) - Sphinx Doxygen renderer
- [fnvhash](internet.md#fnvhash) - Pure Python FNV hash implementation.
- [coacd](education.md#coacd) - Approximate Convex Decomposition for 3D Meshes with Collision-Aware Concavity and Tree Search
- [fickling](security.md#fickling) - A static analyzer and interpreter for Python pickle data
- [DracoPy](scientific-engineering.md#dracopy) - Python wrapper for Google's Draco Mesh Compression Library
- [unix-ar](system-archiving.md#unix-ar) - AR file handling
- [opencage](scientific-engineering-gis.md#opencage) - Wrapper module for the OpenCage Geocoder API
- [pwntools](security.md#pwntools) - Pwntools CTF framework and exploit development library.
- [polyfile-weave](security.md#polyfile-weave) - A utility to recursively map the structure of a file.
- [python-fsutil](desktop-environment-file-managers.md#python-fsutil) - high-level file-system operations for lazy devs.
- [case-converter](text-processing.md#case-converter) - A string case conversion package.
- [hyperscan](software-development-libraries-2.md#hyperscan) - Python bindings for Hyperscan.
- [pottery](database-front-ends.md#pottery) - Redis for Humans.
- [valkey-glide-sync](database.md#valkey-glide-sync) - Valkey GLIDE Sync client. Supports Valkey and Redis OSS.
- [pyocd](software-development.md#pyocd) - Cortex-M debugger for Python
- [empy](software-development-interpreters.md#empy) - A templating system for Python.
- [aws-assume-role-lib](software-development-libraries-2.md#aws-assume-role-lib) - Assumed role session chaining (with credential refreshing) for boto3
- [cmsis-pack-manager](software-development.md#cmsis-pack-manager) - Python manager for CMSIS-Pack index and cache with fast Rust backend
- [pdbp](scientific-engineering.md#pdbp) - pdbp (Pdb+): A drop-in replacement for pdb and pdbpp.
- [bindep](software-development-quality-assurance.md#bindep) - Binary dependency utility
- [pytest-variables](software-development-quality-assurance.md#pytest-variables) - pytest plugin for providing variables to tests/fixtures
- [potracer](multimedia-graphics.md#potracer) - Python Potrace
- [tabcompleter](scientific-engineering.md#tabcompleter) - tabcompleter --- Autocompletion in the Python console.
- [robotframework-robocop](software-development-quality-assurance.md#robotframework-robocop) - Static code analysis tool (linter) and code formatter for Robot Framework
- [ngrok](system-networking.md#ngrok) - The ngrok Agent SDK for Python
- [feu](scientific-engineering.md#feu) - A lightweight Python library for managing packages and versions across different Python environments
- [pytest-describe](software-development-libraries-2.md#pytest-describe) - Describe-style plugin for pytest
- [sphinxcontrib-plantuml](documentation.md#sphinxcontrib-plantuml) - Sphinx "plantuml" extension
- [httpie](internet-www-http.md#httpie) - HTTPie: modern, user-friendly command-line HTTP client for the API era.
- [uroman](text-processing.md#uroman) - uroman is a universal romanizer. It converts text in any script to the standard Latin alphabet.
- [toml-sort](software-development-code-generators.md#toml-sort) - Toml sorting library
- [sphinx-reredirects](documentation.md#sphinx-reredirects) - The extension for Sphinx documentation projects that handle redirects for moved pages. It generates HTML pages with meta refresh redirects to the new page location to prevent 404 errors if you rename or move your documents.
- [PyRIC](security.md#pyric) - Python Wireless Library
- [pytest-cache](software-development-libraries-2.md#pytest-cache) - pytest plugin with mechanisms for caching across test runs
- [lakefs](software-development-libraries-2.md#lakefs) - lakeFS Python SDK Wrapper
- [sphinxcontrib-bibtex](documentation.md#sphinxcontrib-bibtex) - Sphinx extension for BibTeX style citations.
- [canmatrix](software-development-embedded-systems.md#canmatrix) - Automotive Communication Matrix
- [python-benedict](education-testing.md#python-benedict) - python-benedict is a dict subclass with keylist/keypath/keyattr support, normalized I/O operations (base64, csv, ini, json, pickle, plist, query-string, toml, xls, xml, yaml) and many utilities... for humans, obviously.
- [pudb](software-development.md#pudb) - A full-screen, console-based Python debugger
- [sphinxcontrib-httpdomain](documentation.md#sphinxcontrib-httpdomain) - Sphinx extension that provides domains for documenting HTTP and WebSocket APIs.
- [cacheout](database.md#cacheout) - A caching library for Python
- [pgqueuer](database.md#pgqueuer) - PostgreSQL-backed background job and task queue for Python.
- [sbvirtualdisplay](internet.md#sbvirtualdisplay) - A customized pyvirtualdisplay for SeleniumBase.
- [llm](scientific-engineering-artificial-intelligence.md#llm) - CLI utility and Python library for interacting with Large Language Models from organizations like OpenAI, Anthropic and Gemini plus local models installed on your own machine.
- [keyboard](software-development-libraries-2.md#keyboard) - Hook and simulate keyboard events on Windows and Linux
- [pytest-selenium](software-development-quality-assurance.md#pytest-selenium) - pytest plugin for Selenium
- [mcp-proxy](software-development-libraries-2.md#mcp-proxy) - A MCP server which proxies requests to a remote MCP server over streamable HTTP or SSE.
- [mycdp](internet.md#mycdp) - Autogenerated CDP utilities for Python
- [doc8](system-systems-administration.md#doc8) - Style checker for Sphinx (or other) RST documentation
- [retryhttp](internet-www-http.md#retryhttp) - Retry potentially transient HTTP errors in Python.
- [LunarCalendar](software-development-libraries-2.md#lunarcalendar) - A lunar calendar converter, including a number of lunar and solar holidays, mainly from China.
- [plux](software-development-libraries-2.md#plux) - A dynamic code loading framework for building pluggable Python distributions
- [pytest-cover](software-development-testing.md#pytest-cover) - Pytest plugin for measuring coverage. Forked from `pytest-cov`.
- [django-tailwind](software-development-libraries-2.md#django-tailwind) - Tailwind CSS Framework for Django projects
- [serpapi](internet-www-http.md#serpapi) - The official Python client for SerpApi.com.
- [coralogix-logger](internet-log-analysis.md#coralogix-logger) - Coralogix Python SDK
- [univers](software-development.md#univers) - A mostly universal library to parse and compare software package versions and version ranges. A companion to Package URLs.
- [sphinxcontrib-spelling](documentation.md#sphinxcontrib-spelling) - Sphinx spelling extension
- [formic2](software-development-libraries-2.md#formic2) - An implementation of Apache Ant FileSet and Globs
- [pytest-ansible](software-development-quality-assurance.md#pytest-ansible) - Plugin for pytest to simplify calling ansible modules from tests or fixtures
- [selenium-stealth](internet.md#selenium-stealth) - Trying to make python selenium more stealthy.
- [nemo-toolkit](scientific-engineering.md#nemo-toolkit) - NeMo - a toolkit for Conversational AI
- [python-backoff](internet-www-http.md#python-backoff) - Function decoration for backoff and retry
- [ansible-builder](software-development-build-tools.md#ansible-builder) - A tool for building Ansible Execution Environments
- [2captcha-python](scientific-engineering-image-recognition.md#2captcha-python) - Python module for easy integration with 2Captcha API
- [sphinxcontrib-websupport](documentation.md#sphinxcontrib-websupport) - sphinxcontrib-websupport provides a Python API to easily integrate Sphinx documentation into your Web application
- [authheaders](communications-email.md#authheaders) - A library wrapping email authentication header verification and generation.
- [megatron-core](scientific-engineering.md#megatron-core) - Megatron Core - a library for efficient and scalable training of transformer based models
- [pymupdfpro](multimedia-graphics.md#pymupdfpro) - Commercial extensions for PyMuPDF; enables Office document handling, including doc, docx, hwp, hwpx, ppt, pptx, xls, xls, and others. Supports text and table extraction, document conversion and more.
- [imgkit](text-processing.md#imgkit) - Wkhtmltopdf python wrapper to convert html to image using the webkit rendering engine and qt
- [diceware](security-cryptography.md#diceware) - Passphrases you will remember
- [sphinxext-opengraph](documentation.md#sphinxext-opengraph) - Sphinx Extension to enable OGP support
- [textsearch](software-development.md#textsearch) - Find strings/words in text; convenience and C speed
- [pyjks](software-development-libraries-2.md#pyjks) - Pure-Python Java Keystore (JKS) library
- [dissect.cstruct](internet-log-analysis.md#dissectcstruct) - A Dissect module implementing a parser for C-like structures: structure parsing in Python made easy
- [anyconfig](software-development-libraries-2.md#anyconfig) - Library provides common APIs to load and dump configuration files in various formats
- [veracode-api-signing](internet-www-http.md#veracode-api-signing) - Easily sign any request destined for the Veracode API Gateway
- [filehash](software-development-libraries-2.md#filehash) - Module and command-line tool that wraps around hashlib and zlib to facilitate generating checksums / hashes of files and directories.
- [contractions](software-development.md#contractions) - Fixes contractions such as `you're` to you `are`
- [plantuml](internet-www-http.md#plantuml) - 
- [pytest-doctestplus](software-development-testing.md#pytest-doctestplus) - Pytest plugin with advanced doctest features.
- [pytest-parallel](software-development-quality-assurance.md#pytest-parallel) - a pytest plugin for parallel and concurrent testing
- [py-cord](internet.md#py-cord) - A Python wrapper for the Discord API
- [install-playwright](software-development-libraries-2.md#install-playwright) - Execute `playwright install` from Python
- [vermin](software-development.md#vermin) - Concurrently detect the minimum Python versions needed to run code
- [jenkinsapi](software-development-testing.md#jenkinsapi) - A Python API for accessing resources on a Jenkins continuous-integration server.
- [ofxparse](software-development-libraries-2.md#ofxparse) - Tools for working with the OFX (Open Financial Exchange) file format
- [pytailwindcss](software-development-libraries-2.md#pytailwindcss) - Standalone Tailwind CSS CLI, installable via pip. Use Tailwind CSS without Node.js.
- [tombi](software-development-build-tools.md#tombi) - 🦅 TOML Toolkit 🦅
- [numpydantic](file-formats-json.md#numpydantic) - Type and shape validation and serialization for arbitrary array types in pydantic models
- [django-bootstrap5](software-development-libraries-2.md#django-bootstrap5) - Bootstrap 5 for Django
- [clickhouse-cityhash](internet.md#clickhouse-cityhash) - Python-bindings for CityHash, a fast non-cryptographic hash algorithm
- [sphinx-toolbox](documentation.md#sphinx-toolbox) - Box of handy tools for Sphinx 🧰 📔
- [pybind11-global](software-development-libraries-2.md#pybind11-global) - Seamless operability between C++11 and Python
- [pywikibot](internet-www-http.md#pywikibot) - Python MediaWiki Bot Framework
- [licensecheck](security.md#licensecheck) - Output the licenses used by dependencies and check if these are compatible with the project license
- [gallery-dl](internet-www-http.md#gallery-dl) - Command-line program to download image galleries and collections from several image hosting sites
- [pytools](scientific-engineering.md#pytools) - A collection of tools for Python
- [dlipower](software-development-libraries-2.md#dlipower) - Control digital loggers web power switch
- [gerbonara](artistic-software.md#gerbonara) - Tools to handle Gerber and Excellon files in Python
- [base32-crockford](software-development-libraries-2.md#base32-crockford) - A Python implementation of Douglas Crockford's base32 encoding scheme
- [POT](scientific-engineering-artificial-intelligence.md#pot) - Python Optimal Transport Library
- [validator-collection](internet-www-http.md#validator-collection) - Collection of 60+ Python functions for validating data
- [pyarmor](security.md#pyarmor) - A tool used to obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts.
- [allpairspy](software-development-libraries-2.md#allpairspy) - Pairwise test combinations generator
- [tox-gh-actions](software-development-libraries-2.md#tox-gh-actions) - Seamless integration of tox into GitHub Actions
- [tox-ansible](software-development-quality-assurance.md#tox-ansible) - A radical approach to testing ansible content
- [pygmsh](scientific-engineering.md#pygmsh) - Python frontend for Gmsh
- [ansible-dev-environment](software-development.md#ansible-dev-environment) - A pip-like ansible collection installer.
- [rtfparse](software-development-testing.md#rtfparse) - Tool to parse Microsoft Rich Text Format (RTF)
- [html2image](multimedia-graphics.md#html2image) - Package acting as a wrapper around the headless mode of existing web browsers to generate images from URLs and from HTML+CSS strings or files.
- [unlzw3](system-archiving.md#unlzw3) - Pure Python decompression module for .Z files compressed using Unix compress utility
- [pyarmor.cli.core](security.md#pyarmorclicore) - Provide extension module pytransform3 for Pyarmor
- [fastapi-debug-toolbar](internet.md#fastapi-debug-toolbar) - A debug toolbar for FastAPI.
- [pgsanity](database.md#pgsanity) - Check syntax of sql for PostgreSQL
- [pytest-spec](software-development-libraries-3.md#pytest-spec) - Library pytest-spec is a pytest plugin to display test execution output like a SPECIFICATION.
- [pdfrw2](multimedia-graphics.md#pdfrw2) - PDF file reader/writer library
- [pytest-loop](software-development-quality-assurance.md#pytest-loop) - pytest plugin for looping tests
- [motor-types](text-editors.md#motor-types) - Python stubs for Motor, a Non-Blocking MongoDB driver for Python's Tornado and AsyncIO based applications.
- [pathtools](software-development-libraries-3.md#pathtools) - File system general utilities
- [griffe-pydantic](documentation.md#griffe-pydantic) - Griffe extension for Pydantic.
- [gibberish-detector](software-development-libraries-3.md#gibberish-detector) - Detects gibberish strings.
- [bitmath](communications-file-sharing.md#bitmath) - Pythonic module for representing and manipulating file sizes with different prefix notations (file size unit conversion)
- [dissect.util](internet-log-analysis.md#dissectutil) - A Dissect module implementing various utility functions for the other Dissect modules
- [pybloom-live](database-database-engines-servers.md#pybloom-live) - Bloom filter: A Probabilistic data structure
- [getmac](software-development-libraries-3.md#getmac) - Get MAC addresses of remote hosts and local interfaces
- [detect-delimiter](software-development-libraries-3.md#detect-delimiter) - Detects the delimiter used in CSV, TSV and other ad hoc file formats.
- [cloudsmith-cli](internet.md#cloudsmith-cli) - Cloudsmith Command-Line Interface (CLI)
- [mailgun](communications-email.md#mailgun) - Python SDK for Mailgun
- [edalize](scientific-engineering-electronic-design-automation-eda.md#edalize) - Library for interfacing EDA tools such as simulators, linters or synthesis tools, using a common interface
- [demoji](text-processing.md#demoji) - Accurately remove and replace emojis in text strings
- [pytubefix](internet.md#pytubefix) - Python3 library for downloading YouTube Videos.
- [ansible-navigator](software-development-quality-assurance.md#ansible-navigator) - A text-based user interface (TUI) for the Red Hat Ansible Automation Platform
- [pytest-xprocess](software-development-libraries-3.md#pytest-xprocess) - A pytest plugin for managing processes across test runs.
- [fusesoc](software-development-build-tools.md#fusesoc) - Award-winnning package manager and build abstraction tool for HDL code
- [sphinx-needs](documentation.md#sphinx-needs) - Sphinx needs extension for managing needs/requirements and specifications
- [ansible-creator](software-development-code-generators.md#ansible-creator) - A CLI tool for scaffolding Ansible Content.
- [p4python](software-development.md#p4python) - P4Python - Python interface to Perforce API
- [pytest-remotedata](software-development-testing.md#pytest-remotedata) - Pytest plugin for controlling remote data access.
- [pynmeagps](scientific-engineering-gis.md#pynmeagps) - NMEA protocol parser and generator
- [fhconfparser](security.md#fhconfparser) - Provides a config language independent way to read a config file.
- [mmhash3](software-development-libraries-3.md#mmhash3) - Python wrapper for MurmurHash (MurmurHash3), a set of fast and robust hash functions.
- [appdata](system-filesystems.md#appdata) - Utils to manage application data folder.
- [otel-extensions](software-development-libraries-3.md#otel-extensions) - Python extensions for OpenTelemetry
- [spsdk](scientific-engineering.md#spsdk) - Open Source Secure Provisioning SDK for NXP MCU/MPU
- [ansible-dev-tools](software-development.md#ansible-dev-tools) - Ansible Developtment Tools kit bundles all tools needed for content creation and testing.
- [signify](scientific-engineering-information-analysis.md#signify) - Module to generate and verify PE signatures
- [sphinxcontrib-napoleon](documentation.md#sphinxcontrib-napoleon) - Sphinx "napoleon" extension.
- [PyExifTool](multimedia.md#pyexiftool) - Python wrapper for exiftool
- [to-requirements.txt](software-development.md#to-requirementstxt) - Automatically add and delete modules to requirements.txt installing them using pip.
- [ansible-sign](software-development-quality-assurance.md#ansible-sign) - Ansible content validation library and CLI
- [pockets](software-development-libraries-3.md#pockets) - A collection of helpful Python tools!
- [yagmail](communications-email.md#yagmail) - Yet Another GMAIL client
- [django-bootstrap4](software-development-libraries-3.md#django-bootstrap4) - Bootstrap 4 for Django
- [git-url-parse](system-systems-administration.md#git-url-parse) - git-url-parse - A simple GIT URL parser.
- [django-bootstrap3](software-development-libraries-3.md#django-bootstrap3) - Bootstrap 3 for Django
- [favicon](internet-www-http.md#favicon) - Get a website's favicon.
- [rasterstats](scientific-engineering-gis.md#rasterstats) - Summarize geospatial raster datasets based on vector geometries
- [mkdocs-llmstxt](documentation.md#mkdocs-llmstxt) - MkDocs plugin to generate an /llms.txt file.
- [sphinxext-rediraffe](documentation.md#sphinxext-rediraffe) - Sphinx Extension that redirects non-existent pages to working pages
- [yamlloader](software-development-libraries-3.md#yamlloader) - Ordered YAML loader and dumper for PyYAML.
- [zuban](software-development-libraries-3.md#zuban) - Zuban - The Zuban Language Server
- [hachoir](multimedia.md#hachoir) - Package of Hachoir parsers used to open binary files
- [laboratory](software-development-testing.md#laboratory) - Sure-footed refactoring achieved through experimenting
- [collate-sqlfluff](software-development-quality-assurance.md#collate-sqlfluff) - The SQL Linter for Humans
- [csvkit](scientific-engineering-information-analysis.md#csvkit) - A suite of command-line tools for working with CSV, the king of tabular file formats.
- [pyvalid](software-development-debuggers.md#pyvalid) - The module, which allows easily validate function's input/output values.
- [libusbsio](scientific-engineering.md#libusbsio) - Python wrapper around NXP LIBUSBSIO library
- [biothings-client](scientific-engineering-bio-informatics.md#biothings-client) - Python Client for BioThings API services.
- [django-pipeline](internet-www-http.md#django-pipeline) - Pipeline is an asset packaging library for Django.
- [scour](internet.md#scour) - Scour SVG Optimizer
- [sphinxcontrib-confluencebuilder](documentation.md#sphinxcontrib-confluencebuilder) - Sphinx extension to build Atlassian Confluence Storage Markup
- [geoip2fast](internet.md#geoip2fast) - GeoIP2Fast is the fastest GeoIP2 country/city/asn lookup library that supports IPv4 and IPv6. A search takes less than 0.00003 seconds. It has its own data file updated twice a week with Maxmind-Geolite2-CSV, supports IPv4/IPv6 and is Pure Python!
- [nvitop](system-hardware.md#nvitop) - An interactive NVIDIA-GPU process viewer and beyond, the one-stop solution for GPU process management.
- [dllist](system.md#dllist) - List the shared libraries loaded by the current process.
- [fastapi-utilities](internet-www-http.md#fastapi-utilities) - Reusable utilities for FastAPI
- [ofxtools](office-business.md#ofxtools) - Library for working with Open Financial Exchange (OFX) data
- [pyfcm](communications.md#pyfcm) - Python client for FCM - Firebase Cloud Messaging (Android, iOS and Web)
- [mygene](scientific-engineering-bio-informatics.md#mygene) - Python Client for MyGene.Info services.
- [coffea](scientific-engineering.md#coffea) - Basic tools and wrappers for enabling not-too-alien syntax when running columnar Collider HEP analysis.
- [pytest-filter-subpackage](software-development-testing.md#pytest-filter-subpackage) - Pytest plugin for filtering based on sub-packages
- [sphinxcontrib-programoutput](documentation.md#sphinxcontrib-programoutput) - Sphinx extension to include program output
- [tangled-up-in-unicode](database.md#tangled-up-in-unicode) - Access to the Unicode Character Database (UCD)
- [fawltydeps](software-development-libraries-3.md#fawltydeps) - Find undeclared and unused 3rd-party dependencies in your Python project.
- [install-jdk](software-development.md#install-jdk) - install-jdk allows you to easily install latest Java OpenJDK version. Supports OpenJDK builds from Adoptium (previously AdoptOpenJDK), Corretto, and Zulu. Simplify your Java development with the latest OpenJDK builds.
- [lunar-python](software-development-libraries-3.md#lunar-python) - lunar is a calendar library for Solar and Chinese Lunar.
- [pyinfra](system-installation-setup.md#pyinfra) - pyinfra automates/provisions/manages/deploys infrastructure.
- [fastapi-restful](internet.md#fastapi-restful) - Quicker FastApi developing tools
- [beautysh](software-development-libraries-3.md#beautysh) - A Bash beautifier for the masses.
- [docstr-coverage](documentation.md#docstr-coverage) - Utility for examining python source files to ensure proper documentation. Lists missing docstrings, and calculates overall docstring coverage percentage rating.
- [rst2ansi](software-development-libraries-3.md#rst2ansi) - A rst converter to ansi-decorated console output
- [pip-check](software-development.md#pip-check) - Display installed pip packages and their update status.
- [fastapi-problem](internet.md#fastapi-problem) - FastAPI support for RFC9457 problems.
- [rfc9457](internet.md#rfc9457) - Implementation of RFC9457 problems.
- [starlette-problem](internet.md#starlette-problem) - Starlette support for RFC9457 problems.
- [mixer](software-development-libraries-3.md#mixer) - Mixer -- Is a fixtures replacement. Supported Django ORM, SqlAlchemy ORM, Mongoengine ODM and custom python objects.
- [peewee-migrate](software-development-libraries-3.md#peewee-migrate) - Support for migrations in Peewee ORM
- [pytest-arraydiff](software-development-testing.md#pytest-arraydiff) - pytest plugin to help with comparing array output from tests
- [joblibspark](scientific-engineering.md#joblibspark) - Joblib Apache Spark Backend
- [abx-dl](internet-www-http.md#abx-dl) - All-in-one CLI tool to download and extract content from URLs
- [tavern](software-development-testing.md#tavern) - Simple testing of RESTful APIs
- [cyksuid](scientific-engineering.md#cyksuid) - Cython implementation of ksuid
- [pytest-astropy](software-development-testing.md#pytest-astropy) - Meta-package containing dependencies for testing
- [mailbits](communications-email.md#mailbits) - Assorted e-mail utility functions
- [pypcd4](scientific-engineering.md#pypcd4) - Read and write PCL .pcd files in python
- [airium](database-front-ends.md#airium) - Easy and quick html builder with natural syntax correspondence (python->html). No templates needed. Serves pure pythonic library with no dependencies.
- [fastnumbers](scientific-engineering-information-analysis.md#fastnumbers) - Super-fast and clean conversions to numbers.
- [cwltool](scientific-engineering.md#cwltool) - Common workflow language reference implementation
- [ascii-colors](software-development-libraries-3.md#ascii-colors) - A Python library for rich terminal output with advanced logging features.
- [molecule-docker](system-systems-administration.md#molecule-docker) - Molecule aids in the development and testing of Ansible roles
- [sphinxcontrib-video](documentation.md#sphinxcontrib-video) - Allows embedding of HTML5 videos in sphinx
- [pyAesCrypt](security.md#pyaescrypt) - Encrypt and decrypt files and streams in AES Crypt format (version 2)
- [sphinxcontrib-svg2pdfconverter](documentation.md#sphinxcontrib-svg2pdfconverter) - Sphinx SVG to PDF or PNG converter extension
- [humps](software-development.md#humps) - camelCase converter
- [nvidia-sphinx-theme](documentation.md#nvidia-sphinx-theme) - A Sphinx theme for NVIDIA projects
- [robotframework-tidy](software-development-quality-assurance.md#robotframework-tidy) - Code autoformatter for Robot Framework
- [classproperties](software-development-libraries-3.md#classproperties) - property for class methods
- [datafiles](software-development.md#datafiles) - File-based ORM for dataclasses.
- [pdoc3](documentation.md#pdoc3) - Auto-generate API documentation for Python projects.
- [wechatpy](software-development-libraries-3.md#wechatpy) - WeChat SDK for Python
- [pymongo_inmemory](database-database-engines-servers.md#pymongo_inmemory) - A mongo mocking library with an ephemeral MongoDB running in memory.
- [wait-for-it](internet.md#wait-for-it) - Wait for service(s) to be available before executing a command.
- [optionaldict](software-development-libraries-3.md#optionaldict) - A dict-like object that ignore NoneType values for Python
- [oschmod](system-filesystems.md#oschmod) - Consistent chmod-style file permissions on Windows, macOS, and Linux
- [dissect.ntfs](internet-log-analysis.md#dissectntfs) - A Dissect module implementing a parser for the NTFS file system, used by the Windows operating system
- [sphinxemoji](documentation.md#sphinxemoji) - An extension to use emoji codes in your Sphinx documentation
- [prophy](scientific-engineering-interface-engine-protocol-translator.md#prophy) - prophy: fast serialization protocol
- [universal-startfile](desktop-environment-file-managers.md#universal-startfile) - A cross-platform version of 'os.startfile' from the standard library.
- [redislite](software-development-libraries-3.md#redislite) - Redis built into a python package
- [sphinxcontrib-towncrier](documentation-sphinx.md#sphinxcontrib-towncrier) - An RST directive for injecting a Towncrier-generated changelog draft containing fragments for the unreleased (next) project version
- [2captcha-python-async](scientific-engineering-image-recognition.md#2captcha-python-async) - Python module for easy integration with 2Captcha API
- [empty-files](software-development-libraries-3.md#empty-files) - Serves empty files of many types
- [manhole](software-development-debuggers.md#manhole) - Manhole is in-process service that will accept unix domain socket connections and present thestacktraces for all threads and an interactive prompt.
- [doppler-env](software-development-build-tools.md#doppler-env) - Inject Doppler secrets as environment variables into your Python application during local development with debugging support for PyCharm and Visual Studio Code.
- [copier-template-extensions](software-development.md#copier-template-extensions) - Special Jinja2 extension for Copier that allows to load extensions using file paths relative to the template root instead of Python dotted paths.
- [regipy](software-development-libraries-3.md#regipy) - Python Registry Parser
- [approvaltests](software-development-libraries-3.md#approvaltests) - Assertion/verification library to aid testing
- [pydivert](software-development-libraries-3.md#pydivert) - Python binding to WinDivert (Windows) and eBPFDivert (Linux) for packet capture, filtering and injection
- [mwxml](scientific-engineering.md#mwxml) - A set of utilities for processing MediaWiki XML dump data.
- [mwtypes](scientific-engineering.md#mwtypes) - A set of types for processing MediaWiki data.
- [none](software-development-libraries-3.md#none) - An extensive library providing additional facilities to the Python Standard Library.
- [para](scientific-engineering.md#para) - a set utilities that ake advantage of python's 'multiprocessing' module to distribute CPU-intensive tasks
- [mwcli](scientific-engineering.md#mwcli) - Utilities for processing MediaWiki on the command line.
- [iptools](internet.md#iptools) - Python utilites for manipulating IPv4 and IPv6 addresses
- [pytest-faker](software-development-libraries-3.md#pytest-faker) - Faker integration with the pytest framework.
- [cachier](other-nonlisted-topic.md#cachier) - Persistent, stale-free, local and cross-machine caching for Python functions.
- [dirsync](desktop-environment.md#dirsync) - Advanced directory tree synchronisation tool
- [segyio](scientific-engineering.md#segyio) - Simple & fast IO for SEG-Y files
- [qbittorrent-api](communications-file-sharing.md#qbittorrent-api) - Python client for qBittorrent v4.1+ Web API.
- [distinctipy](multimedia-graphics.md#distinctipy) - A lightweight package for generating visually distinct colours.
- [md2pdf](office-business.md#md2pdf) - The Markdown to PDF conversion tool with styles
- [aiohttp-asgi-connector](software-development-testing.md#aiohttp-asgi-connector) - AIOHTTP Connector for running ASGI applications
- [pytest-shutil](software-development-libraries-3.md#pytest-shutil) - A goodie-bag of unix shell and environment tools for py.test
- [snakebite-py3](software-development-libraries-3.md#snakebite-py3) - Pure Python HDFS client
- [python-status](internet.md#python-status) - HTTP Status for Humans
- [bytesparse](scientific-engineering-interface-engine-protocol-translator.md#bytesparse) - Library to handle sparse bytes within a virtual memory space
- [grafana-client](communications.md#grafana-client) - A client library for accessing the Grafana HTTP API, written in Python
- [hexrec](scientific-engineering-interface-engine-protocol-translator.md#hexrec) - Library to handle hexadecimal record files
- [hunter](software-development-debuggers.md#hunter) - Hunter is a flexible code tracing toolkit.
- [streamlink](internet-www-http.md#streamlink) - Streamlink is a command-line utility that extracts streams from various services and pipes them into a video player of choice.
- [pymupdf-stubs](software-development-libraries-3.md#pymupdf-stubs) - Type stubs for PyMuPDF (fitz), automatically generated
- [sphinx-intl](documentation.md#sphinx-intl) - Sphinx utility that make it easy to translate and to apply translation.
- [backoff-utils](internet-www-http.md#backoff-utils) - Python functions and decorators for various backoff/retry strategies
- [pysplashsurf](scientific-engineering.md#pysplashsurf) - Python bindings for splashsurf, a surface reconstruction library for SPH simulations.
- [sphinx-pyproject](documentation.md#sphinx-pyproject) - Move some of your Sphinx configuration into pyproject.toml
- [cx-Freeze](software-development-build-tools.md#cx-freeze) - Create standalone executables from Python scripts
- [tox-toml-fmt](software-development-quality-assurance.md#tox-toml-fmt) - Format tox.toml files
- [executor](internet.md#executor) - Programmer friendly subprocess wrapper
- [magicgui](desktop-environment.md#magicgui) - build GUIs from python types
- [aws-sso-lib](software-development-libraries-3.md#aws-sso-lib) - Library to make AWS SSO easier
- [aiomisc](internet.md#aiomisc) - aiomisc - miscellaneous utils for asyncio
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
- [version-utils](software-development-libraries-3.md#version-utils) - Library for parsing system package strings and comparing package versions
- [dissect.esedb](internet-log-analysis.md#dissectesedb) - Superseded by dissect.database. A Dissect module implementing a parser for Microsofts Extensible Storage Engine Database (ESEDB), used for example in Active Directory, Exchange and Windows Update
- [pydbml](documentation.md#pydbml) - Python parser and builder for DBML
- [setupmeta](software-development-build-tools.md#setupmeta) - Simplify your setup.py
- [pydoc-markdown](software-development-code-generators.md#pydoc-markdown) - Create Python API documentation in Markdown format.
- [sphinxcontrib-youtube](documentation.md#sphinxcontrib-youtube) - Sphinx "youtube" extension.
- [aws-kinesis-agg](software-development-libraries-3.md#aws-kinesis-agg) - Python module to assist in taking advantage of the Kinesis message aggregation format for both aggregation and deaggregation.
- [sphinxcontrib-apidoc](documentation.md#sphinxcontrib-apidoc) - A Sphinx extension for running 'sphinx-apidoc' on each build
- [workdays](software-development-libraries-3.md#workdays) - Workday date utility functions to extend python's datetime
- [debian-inspector](software-development.md#debian-inspector) - Utilities to parse Debian package, copyright and control files.
- [saneyaml](software-development.md#saneyaml) - Read and write readable YAML safely preserving order and avoiding bad surprises with unwanted infered type conversions. This library is a PyYaml wrapper with sane behaviour to read and write readable YAML safely, typically when used for configuration.
- [nemo-text-processing](scientific-engineering.md#nemo-text-processing) - NeMo text processing for ASR and TTS
- [django-summernote](internet-www-http.md#django-summernote) - Summernote plugin for Django
- [times](internet.md#times) - Times is a small, minimalistic, Python library for dealing with time conversions between universal time and arbitrary timezones.
- [epiweeks](scientific-engineering.md#epiweeks) - Epidemiological weeks calculation based on CDC and ISO week numbering systems
- [pytest-grpc](software-development-quality-assurance.md#pytest-grpc) - pytest plugin for grpc
- [otpauth](security.md#otpauth) - Implements one time password of HOTP/TOTP
- [rst2pdf](documentation.md#rst2pdf) - Convert reStructured Text to PDF via ReportLab.
- [sqlfluffrs](software-development-quality-assurance.md#sqlfluffrs) - The SQL Linter for Humans
- [PyPDFForm](file-formats.md#pypdfform) - The Python library & CLI for PDF forms.
- [sapien](education.md#sapien) - ['SAPIEN: A SimulAted Parted based Interactive ENvironment']
- [rpm](software-development.md#rpm) - Shim RPM module for use in virtualenvs.
- [commoncode](software-development.md#commoncode) - Set of common utilities, originally split from ScanCode
- [plyara](security.md#plyara) - Parse YARA rules
- [hickle](software-development-libraries-3.md#hickle) - Hickle - an HDF5 based version of pickle
- [jedi-language-server](software-development-code-generators.md#jedi-language-server) - A language server for Jedi!
- [django-graphiql-debug-toolbar](internet.md#django-graphiql-debug-toolbar) - Django Debug Toolbar for GraphiQL IDE.
- [domaintools-api](software-development-libraries-3.md#domaintools-api) - DomainTools Official Python API
- [molecule-vagrant](system-systems-administration.md#molecule-vagrant) - Vagrant Molecule Plugin :: run molecule tests using Vagrant
- [sas7bdat](text-processing.md#sas7bdat) - A sas7bdat file reader for Python
- [base58check](internet-www-http.md#base58check) - Base58check encoding and decoding of binary data
- [python-redmine](internet-www-http.md#python-redmine) - Library for communicating with a Redmine project management application
- [pymediawiki](internet.md#pymediawiki) - Wikipedia and MediaWiki API wrapper for Python
- [ruff-lsp](software-development-libraries-3.md#ruff-lsp) - A Language Server Protocol implementation for Ruff.
- [napari-plugin-engine](scientific-engineering.md#napari-plugin-engine) - napari plugin engine, fork of pluggy
- [napari](scientific-engineering.md#napari) - n-dimensional array viewer in Python
- [tmuxp](system-shells.md#tmuxp) - Session manager for tmux, which allows users to save and load tmux sessions through simple configuration files.
- [kolo](software-development.md#kolo) - Kolo is a text-based Python debugger for AI agents. Capture every executed function call, return value, local variable, HTTP request, and more in greppable trace files.
- [depgather](security.md#depgather) - Get a list of deps given a pyproject.toml, uv.lock, requirements.txt etc
- [port-ocean](software-development-libraries-4.md#port-ocean) - Port Ocean is a Python framework for building integrations that ingest data into Port, the platform for building your AI software factory.
- [tippecanoe](scientific-engineering-2.md#tippecanoe) - Builds vector tilesets from large (or small) collections of GeoJSON, FlatGeobuf, or CSV features
- [inputs](software-development-embedded-systems.md#inputs) - Cross-platform Python support for keyboards, mice and gamepads.
- [django-tailwind-cli](software-development-libraries-4.md#django-tailwind-cli) - Django and Tailwind integration based on the prebuilt Tailwind CSS CLI.
- [faker-vehicle](software-development-libraries-4.md#faker-vehicle) - Vehicle related Provider for the Faker Python package.
- [copier-templates-extensions](software-development.md#copier-templates-extensions) - Deprecated (renamed). Install `copier-template-extensions` instead.
- [pylspci](software-development-libraries-4.md#pylspci) - Simple parser for lspci -mmnn.
- [poetry-dotenv-plugin](software-development.md#poetry-dotenv-plugin) - A Poetry plugin to automatically load environment variables from .env files
- [pkginfo2](software-development.md#pkginfo2) - Query metadata from sdists / bdists / installed packages. Safer fork of pkginfo to avoid doing arbitrary imports and eval.
- [fdt](scientific-engineering-2.md#fdt) - Flattened Device Tree Python Module
- [quadrilateral-fitter](scientific-engineering-artificial-intelligence.md#quadrilateral-fitter) - QuadrilateralFitter is an efficient and easy-to-use Python library for fitting irregular quadrilaterals from irregular polygons or any noisy data.
- [tempenv](security.md#tempenv) - Environment Variable Context Manager
- [typecode](software-development.md#typecode) - Comprehensive filetype and mimetype detection using libmagic and Pygments.
- [ansible-base](system-installation-setup.md#ansible-base) - Radically simple IT automation
- [plugincode](software-development.md#plugincode) - plugincode is a library that provides plugin functionality for ScanCode toolkit.
- [container-inspector](software-development.md#container-inspector) - Docker, containers, rootfs and virtual machine related software composition analysis (SCA) utilities.
- [rowdump](software-development-libraries-4.md#rowdump) - A modern structured Python library for formatted table output
- [tuna](software-development-user-interfaces.md#tuna) - Visualize Python performance profiles
- [pytest-jira](software-development-quality-assurance.md#pytest-jira) - py.test JIRA integration plugin, using markers
- [discord-protos](internet.md#discord-protos) - Discord user settings protobufs.
- [sphobjinv](documentation.md#sphobjinv) - Sphinx objects.inv Inspection/Manipulation Tool
- [pygmars](software-development.md#pygmars) - Craft simple regex-based small language lexers and parsers. Build parsers from grammars and accept Pygments lexers as an input. Derived from NLTK.
- [freeze-core](software-development-build-tools.md#freeze-core) - Core dependency for cx_Freeze
- [Unipath](software-development-libraries-4.md#unipath) - Object-oriented alternative to os/os.path/shutil
- [censys](documentation-sphinx.md#censys) - An easy-to-use and lightweight API wrapper for Censys APIs (censys.io).
- [click-extra](documentation-sphinx.md#click-extra) - 🌈 Drop-in replacement for Click to make user-friendly and colorful CLI
- [gemfileparser2](software-development.md#gemfileparser2) - Parse Ruby Gemfile, .gemspec and Cocoapod .podspec files using Python.
- [wlc](software-development-internationalization.md#wlc) - A command-line utility for Weblate, translation tool with tight version control integration
- [sphinx-favicon](documentation.md#sphinx-favicon) - Sphinx Extension adding support for custom favicons
- [extra-platforms](software-development-libraries-4.md#extra-platforms) - 🔎 Detect architectures, platforms, shells, terminals, CI systems and agents, grouped by family
- [git-changelog](documentation.md#git-changelog) - Automatic Changelog generator using Jinja2 templates.
- [pylint-junit](software-development-libraries-4.md#pylint-junit) - pylint reporter for junit format.
- [scancode-toolkit](software-development.md#scancode-toolkit) - ScanCode is a tool to scan code for license, copyright, package and their documented dependencies and other interesting facts.
- [pyprof2calltree](desktop-environment-k-desktop-environment-kde.md#pyprof2calltree) - Help visualize profiling data from cProfile with kcachegrind and qcachegrind
- [extractcode](software-development.md#extractcode) - A mostly universal archive extractor using 7zip, libarchive and the Python standard library for reliable archive extraction.
- [h2o-authn](internet.md#h2o-authn) - H2O Python Clients Authentication Helpers
- [pip-licenses-lib](software-development.md#pip-licenses-lib) - Retrieve the software license list of Python packages installed with pip.
- [static3](software-development-libraries-4.md#static3) - A really simple WSGI way to serve static (or mixed) content.
- [hanziconv](system.md#hanziconv) - Hanzi Converter for Traditional and Simplified Chinese
- [fspath](software-development-libraries-4.md#fspath) - semantic path names and more
- [nbtoolbelt](education.md#nbtoolbelt) - Tools to work with Jupyter notebooks
- [aiohttp-middlewares](internet-www-http-2.md#aiohttp-middlewares) - Collection of useful middlewares for aiohttp applications.
- [json-source-map](software-development-disassemblers.md#json-source-map) - Calculate the source map for a JSON document.
- [certbot-dns-route53](internet-www-http-2.md#certbot-dns-route53) - Route53 DNS Authenticator plugin for Certbot
- [djangorestframework-bulk](internet-www-http-2.md#djangorestframework-bulk) - Django REST Framework bulk CRUD view mixins
- [html2docx](software-development-libraries-4.md#html2docx) - Convert valid HTML input to docx.
- [pysphere](software-development-libraries-4.md#pysphere) - Python API for interacting with the vSphere Web Services SDK
- [pyap2](scientific-engineering-information-analysis.md#pyap2) - Pyap2 is a maintained fork of pyap, a regex-based library for parsing US, CA, and UK addresses. The fork adds typing support, handles more address formats and edge cases.
- [blendmodes](multimedia-graphics.md#blendmodes) - Use this module to apply a number of blending modes to a background and foreground image
- [pytkdocs](documentation.md#pytkdocs) - Load Python objects documentation.
- [ignore](internet-www-http-2.md#ignore) - Download .gitignore files for a given language
- [pyprobables](software-development-libraries-4.md#pyprobables) - Probabilistic data structures in python
- [certbot-nginx](internet-www-http-2.md#certbot-nginx) - Nginx plugin for Certbot
- [pyDOE3](education.md#pydoe3) - Design of experiments for Python
- [griffe2md](documentation.md#griffe2md) - Output API docs to Markdown using Griffe.
- [pansi](software-development.md#pansi) - Text mode rendering library
- [bagit-profile](communications-file-sharing.md#bagit-profile) - This module can be used to validate BagitProfiles.
- [pydantic-factories](software-development.md#pydantic-factories) - Mock data generation for pydantic based models and python dataclasses
- [pyjoulescope-driver](scientific-engineering-2.md#pyjoulescope-driver) - Joulescope™ driver
- [yamlpath](software-development-libraries-4.md#yamlpath) - Command-line get/set/merge/validate/scan/convert/diff processors for YAML/JSON/Compatible data using powerful, intuitive, command-line friendly syntax
- [xlcalculator](office-business-financial.md#xlcalculator) - Converts MS Excel formulas to Python and evaluates them.
- [pyrtcm](scientific-engineering-gis.md#pyrtcm) - RTCM3 protocol parser
- [Paver](documentation.md#paver) - Easy build, distribution and deployment scripting
- [ops-scenario](software-development-quality-assurance.md#ops-scenario) - Python library providing a state-transition testing API for Operator Framework charms.
- [roc-validator](scientific-engineering-2.md#roc-validator) - A Python package to validate RO-Crates
- [faker-e164](software-development-libraries-4.md#faker-e164) - Faker Provider to generate phone numbers in E164 format.
- [django-redis-cache](software-development-libraries-4.md#django-redis-cache) - Redis Cache Backend for Django
- [robotcode](software-development-debuggers.md#robotcode) - Command line interface for RobotCode
- [highcharts-core](internet-www-http-2.md#highcharts-core) - High-end Data Visualization for the Python Ecosystem. Official wrapper for Highcharts Core (JS).
- [python-xmp-toolkit](multimedia.md#python-xmp-toolkit) - XMP I/O wrapping Exempi
- [unittest-parallel](software-development-testing.md#unittest-parallel) - Parallel unit test runner with coverage support
- [stcrestclient](software-development-libraries-4.md#stcrestclient) - stcrestclient: Client modules for STC ReST API
- [interruptingcow](software-development-debuggers.md#interruptingcow) - A watchdog that interrupts long running code.
- [python-msilib](software-development-build-tools.md#python-msilib) - Read and write Microsoft Installer files
- [py3-wget](communications-file-sharing.md#py3-wget) - A tool to download files. It supports progress bar, cksum, timeout, retry failed download.
- [cabarchive](system-archiving.md#cabarchive) - A pure-python library for creating and extracting cab files
- [df2gspread](office-business.md#df2gspread) - Export tables to Google Spreadsheets.
- [dns-lexicon](internet-name-service-dns.md#dns-lexicon) - Manipulate DNS records on various DNS providers in a standardized/agnostic way
- [edt](scientific-engineering-2.md#edt) - Multi-Label Anisotropic Euclidean Distance Transform 3D
- [privata](software-development-libraries-4.md#privata) - A Python module privacy checker for keeping public interfaces intentional.
- [deepfilternet](multimedia-sound-audio.md#deepfilternet) - Noise supression using deep filtering
- [attrs-strict](software-development-libraries-4.md#attrs-strict) - Runtime validators for attrs
- [simple-ddl-parser](software-development.md#simple-ddl-parser) - Simple DDL Parser to parse SQL & dialects like HQL, TSQL (MSSQL), Oracle, AWS Redshift, Snowflake, MySQL, PostgreSQL, etc ddl files to json/python dict with full information about columns: types, defaults, primary keys, etc.; sequences, alters, custom types & other entities from ddl.
- [lazydocs](documentation.md#lazydocs) - Generate markdown API documentation for Google-style Python docstring.
- [pyc-wheel](software-development-libraries-4.md#pyc-wheel) - Compile all py files in a wheel to pyc files.
- [linuxdoc](software-development-documentation.md#linuxdoc) - Sphinx-doc extensions & tools to extract documentation from C/C++ source file comments.
- [archivebox](internet-www-http-2.md#archivebox) - Self-hosted internet archiving solution.
- [fparser](scientific-engineering-2.md#fparser) - Python implementation of a Fortran parser
- [mplib](education.md#mplib) - A lightweight motion planning library
- [mkdocstrings-python-legacy](documentation.md#mkdocstrings-python-legacy) - A legacy Python handler for mkdocstrings.
- [sphinxcontrib-katex](documentation.md#sphinxcontrib-katex) - A Sphinx extension for rendering math in HTML pages
- [scenedetect-headless](multimedia-video.md#scenedetect-headless) - Video scene cut/shot detection program and Python library (bundles the opencv-python-headless OpenCV variant and the scenedetect CLI; for servers without GUI libraries).
- [genpy](scientific-engineering-2.md#genpy) - AST-based generation of Python source code
- [editorconfig-checker](text-processing.md#editorconfig-checker) - Python wrapper around invoking editorconfig-checker (https://github.com/editorconfig-checker/editorconfig-checker)
- [vcstool](software-development-version-control.md#vcstool) - vcstool provides a command line tool to invoke vcs commands on multiple repositories.
- [random-address](software-development-libraries-4.md#random-address) - Retrieve real random US addresses, with coordinates, for tests and fixtures
- [pyjsonpatch](file-formats-json.md#pyjsonpatch) - A Python implementation of JSON Pointer and JSON Patch
- [sphinxcontrib-googleanalytics](documentation.md#sphinxcontrib-googleanalytics) - Sphinx extension googleanalytics
- [faker-enum](software-development-libraries-4.md#faker-enum) - Enum provider for the Faker Python package.
- [griffe-typingdoc](documentation.md#griffe-typingdoc) - Griffe extension for PEP 727 – Documentation Metadata in Typing.
- [meshioplusplus](scientific-engineering-2.md#meshioplusplus) - meshio++: I/O for many mesh formats (C++20 core + Python bindings)
- [crudini](system-systems-administration.md#crudini) - A utility for manipulating ini files
- [flynt](software-development-libraries-4.md#flynt) - CLI tool to convert a python project's %-formatted strings to f-strings.
- [discord.py-self](internet.md#discordpy-self) - A Python wrapper for the Discord user API
- [dictdumper](system-networking.md#dictdumper) - DictDumper: comprehensive network packet analysis library
- [xtgeo](scientific-engineering-2.md#xtgeo) - XTGeo is a Python library for 3D grids, surfaces, wells, etc
- [qiskit-connector](scientific-engineering-2.md#qiskit-connector) - Quantum Computing Qiskit Connector For Quantum Backend Use In Realtime
- [version-parser](software-development.md#version-parser) - This package can parse and compare semantic versioning.
- [hankel](scientific-engineering-2.md#hankel) - Hankel Transformations using method of Ogata 2005
- [pydantic-cli](software-development.md#pydantic-cli) - Turn Pydantic defined Data Models into CLI Tools
- [pysnowflake](software-development-libraries-4.md#pysnowflake) - Python Snowflake Kit
- [pyubx2](scientific-engineering-gis.md#pyubx2) - UBX protocol parser and generator
- [nestedtext](text-processing-markup.md#nestedtext) - human readable and writable data interchange format
- [cyseq](software-development.md#cyseq) - "A Cython version of ScanCode-toolkit's licensedcode.seq"
- [gstools](scientific-engineering-2.md#gstools) - GSTools: A geostatistical toolbox.
- [sphinxcontrib-typer](documentation.md#sphinxcontrib-typer) - Auto generate docs for typer commands.
- [django-model-info](documentation.md#django-model-info) - A set of Django Management Commands to help you understand and visualize your project's models.
- [transferit-py](communications-file-sharing.md#transferit-py) - Pure-Python client for transfer.it — upload and download files via the MEGA backend, no browser required.
- [pytest-progress](software-development-libraries-4.md#pytest-progress) - pytest plugin for instant test progress status
- [pypemicro](scientific-engineering-2.md#pypemicro) - Python tool to control PEMicro Debug probes
- [PySmbClient](software-development-libraries-4.md#pysmbclient) - A convenient smbclient wrapper
- [pyavd-utils](software-development-libraries-4.md#pyavd-utils) - Rust based utilities used by PyAVD. Should not be used directly and may not follow semantic versioning.
- [pyCalverter](software-development-libraries-4.md#pycalverter) - Python Calendar Converter
- [ansi2txt](terminals.md#ansi2txt) - ansi to plain text converter
- [django-bootstrap-datepicker-plus](software-development-libraries-4.md#django-bootstrap-datepicker-plus) - Bootstrap3/Bootstrap4/Bootstrap5 DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
- [python-upwork-oauth2](software-development-libraries-4.md#python-upwork-oauth2) - Python bindings for Upwork API (OAuth2)
- [pyexcel-webio](internet-www-http-2.md#pyexcel-webio) - A generic request and response interface for pyexcel web extensions.
- [metaclass-registry](software-development-libraries-4.md#metaclass-registry) - Zero-boilerplate metaclass-driven plugin registry system with lazy discovery and caching
- [pyocd-pemicro](scientific-engineering-2.md#pyocd-pemicro) - PyOCD debug probe plugin for PEMicro debug probes
- [django-valkey](software-development-libraries-4.md#django-valkey) - a valkey backend for django
- [cachettl](software-development-libraries-4.md#cachettl) - cachettl is an elegant LRU TTL cache decorator that also works with asyncio. It has the cache_info(), cache_clear() methods and access to the remainingttl property.
- [appthreat-vulnerability-db](security.md#appthreat-vulnerability-db) - AppThreat's vulnerability database and package search library with a built-in sqlite based storage. OSV, CVE, GitHub, npm are the primary sources of vulnerabilities.
- [commit-check](software-development-build-tools.md#commit-check) - Commit policy as code for teams and AI agents: check commit messages, branch names, authors, tags, files and AI attribution.
- [weblate-fonts](software-development-internationalization.md#weblate-fonts) - Weblate fonts collection
- [kdtree](software-development-libraries-4.md#kdtree) - A Python implementation of a kd-tree
- [dissect.target](internet-log-analysis.md#dissecttarget) - This module ties all other Dissect modules together, it provides a programming API and command line tools which allow easy access to various data sources inside disk images or file collections (a.k.a. targets)
- [Flask-Injector](software-development-libraries-5.md#flask-injector) - Adds Injector, a Dependency Injection framework, support to Flask.
- [yandex-cli](office-business.md#yandex-cli) - Interact with Yandex 360 services (Wiki, Tracker, Forms, …) from a CLI, an MCP server, or a Python SDK.
- [dotted-notation](software-development-libraries-5.md#dotted-notation) - Dotted notation for safe nested data traversal with optional chaining, pattern matching, and transforms
- [gstools-cython](scientific-engineering-2.md#gstools-cython) - Cython backend for GSTools.
- [pyexcel-ezodf](office-business.md#pyexcel-ezodf) - A Python package to create/manipulate OpenDocumentFormat files
- [PyLink](internet.md#pylink) - Universal communication interface using File-Like API
- [textcharts](scientific-engineering-visualization.md#textcharts) - Beautiful ASCII charts for your terminal — bar, histogram, heatmap, box plot, and 11 more chart types with zero dependencies
- [PyKrige](scientific-engineering-2.md#pykrige) - Kriging Toolkit for Python.
- [bourbaki.application](software-development-code-generators.md#bourbakiapplication) - CLIs derived directly from type signatures and docstrings years before typer existed
- [bourbaki.introspection](software-development-code-generators.md#bourbakiintrospection) - Introspection utilities for Python: types, signatures, objects, docstrings, and more
- [pytest-cython](software-development-testing.md#pytest-cython) - A plugin for testing Cython extension modules.
- [marionette-driver](software-development-quality-assurance.md#marionette-driver) - Marionette Driver
- [lightningcss-cli](software-development-build-tools.md#lightningcss-cli) - 
- [retrie](software-development-libraries-5.md#retrie) - Efficient Trie-based regex unions for blacklist/whitelist filtering and one-pass mapping-based string replacing
- [PySquashfsImage](software-development-libraries-5.md#pysquashfsimage) - Squashfs image parser
- [prompt](software-development-libraries-5.md#prompt) - Library for prompting input on the command line.
- [morph-kgc](database.md#morph-kgc) - Powerful [R2]RML engine to create RDF knowledge graphs from heterogeneous data sources.
- [yubikey-manager](security-cryptography.md#yubikey-manager) - Library and CLI for managing your YubiKey configuration.
- [PyCampbellCR1000](internet.md#pycampbellcr1000) - Communication tools for Campbell CR1000-type Dataloggers
- [click-shell](software-development-user-interfaces.md#click-shell) - An extension to click that easily turns your click app into a shell utility
- [mouse](software-development-libraries-5.md#mouse) - Hook and simulate mouse events on Windows and Linux
- [open3d-cpu](education.md#open3d-cpu) - Open3D: A Modern Library for 3D Data Processing.
- [climage](artistic-software.md#climage) - Convert images to beautiful ANSI escape codes
- [griffe-inherited-docstrings](documentation.md#griffe-inherited-docstrings) - Griffe extension for inheriting docstrings.
- [django-registration-redux](software-development-libraries-5.md#django-registration-redux) - An extensible user-registration application for Django
- [miss-hit-core](scientific-engineering-2.md#miss-hit-core) - Code formatting and code metrics for programs written in the MATLAB/Simulink and Octave languages.
- [tini](software-development-libraries-5.md#tini) - Read simple .ini/configuration files.
- [pytest-splinter](software-development-libraries-5.md#pytest-splinter) - Splinter plugin for pytest testing framework
- [pypyp](software-development.md#pypyp) - Easily run Python at the shell! Magical, but never mysterious.
- [pyxnat](internet-www-http-2.md#pyxnat) - XNAT in Python
- [saleae](scientific-engineering-2.md#saleae) - Library to control a Saleae
- [owasp-depscan](security.md#owasp-depscan) - Fully open-source security audit for project dependencies based on known vulnerabilities and advisories.
- [pygad](scientific-engineering-2.md#pygad) - PyGAD: A Python Library for Building the Genetic Algorithm and Training Machine Learning Algoithms (Keras & PyTorch).
- [pytidylib](text-processing-markup.md#pytidylib) - Python wrapper for HTML Tidy (tidylib) on Python 2 and 3
- [griffe-warnings-deprecated](documentation.md#griffe-warnings-deprecated) - Griffe extension for `@warnings.deprecated` (PEP 702).
