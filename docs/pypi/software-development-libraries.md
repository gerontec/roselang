# Software Development / Libraries (part 1 of 5)

[Index](README.md) · 1884 packages in this topic, 1694 more listed under another topic, by downloads.

part 1 · [part 2](software-development-libraries-2.md) · [part 3](software-development-libraries-3.md) · [part 4](software-development-libraries-4.md) · [part 5](software-development-libraries-5.md)

### pluggy

plugin and hook calling mechanisms for python

`pip install pluggy` · installs (wheel) · licence: MIT License · rank 11 · last release 2026-10-15 · [PyPI](https://pypi.org/project/pluggy/) · [docs](https://pluggy.readthedocs.io/) · [source](https://github.com/pytest-dev/pluggy)

<details><summary>README extract</summary>

This is the core framework used by the pytest, tox, and devpi projects.

Please read the docs to learn more!

Example:
```python
import pluggy

hookspec = pluggy.HookspecMarker("myproject")
hookimpl = pluggy.HookimplMarker("myproject")

class MySpec:
    """A hook specification namespace."""

    @hookspec
    def myhook(self, arg1, arg2):
        """My special little hook that you can customize."""

class Plugin_1:
    """A hook implementation namespace."""

    @hookimpl
...
```

Sections: pluggy - A minimalist production ready plugin system, A definitive example

</details>

### PyYAML

YAML parser and emitter for Python

`pip install PyYAML` · installs (wheel) · licence: MIT License · rank 12 · last release 2025-09-29 · [PyPI](https://pypi.org/project/PyYAML/) · [docs](https://pyyaml.org/wiki/PyYAMLDocumentation) · [source](https://github.com/yaml/pyyaml)

<details><summary>README extract</summary>

YAML is a data serialization format designed for human readability
and interaction with scripting languages. PyYAML is a YAML parser
and emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages. ...

</details>

### python-dateutil

Extensions to the standard Python datetime module

`pip install python-dateutil` · installs (wheel) · licence: BSD-3-Clause · rank 15 · last release 2026-11-01 · [PyPI](https://pypi.org/project/python-dateutil/) · [docs](https://dateutil.readthedocs.io/en/stable/) · [source](https://github.com/dateutil/dateutil)

<details><summary>README extract</summary>

The `dateutil` module provides powerful extensions to
the standard `datetime` module, available in Python.

Features:
* Computing of relative deltas (next month, next year,
 next Monday, last week of month, etc);
* Computing of relative deltas between two given
 date and/or datetime objects;
* Computing of dates based on very flexible recurrence rules,
 using a ...

Example:
```python
>>> from dateutil.relativedelta import *
>>> from dateutil.easter import *
>>> from dateutil.rrule import *
>>> from dateutil.parser import *
>>> from datetime import *
>>> now = parse("Sat Oct 11 17:13:46 UTC 2003")
>>> today = now.date()
>>> year = rrule(YEARLY,dtstart=now,bymonth=8,bymonthday=13,byweekday=FR)[0].year
...
```

...

</details>

### six

Python 2 and 3 compatibility utilities

`pip install six` · installs (wheel) · licence: MIT License · rank 16 · last release 2024-12-04 · [PyPI](https://pypi.org/project/six/)

<details><summary>README extract</summary>

Six is a Python 2 and 3 compatibility library. It provides utility functions
for smoothing over the differences between the Python versions with the goal of
writing Python code that is compatible on both Python versions. See the
documentation for more information on what is provided.

Six supports Python 2.7 and 3.3+. ...

</details>

### setuptools

Most extensible Python build backend with support for C/C++ extension modules

`pip install setuptools` · installs (wheel) · licence: MIT · rank 17 · last release 2026-10-20 · [PyPI](https://pypi.org/project/setuptools/) · [docs](https://setuptools.pypa.io/) · [source](https://github.com/pypa/setuptools)

<details><summary>README extract</summary>

See the Quickstart
and the User's Guide for
instructions on how to use Setuptools.

Questions and comments should be directed to GitHub Discussions.
Bug reports and especially tested patches may be
submitted directly to the bug tracker.

</details>

### annotated-types

Reusable constraint types to use with typing.Annotated

`pip install annotated-types` · installs (wheel) · licence: MIT · rank 24 · last release 2026-07-23 · [PyPI](https://pypi.org/project/annotated-types/) · [source](https://github.com/annotated-types/annotated-types)

<details><summary>README extract</summary>

PEP-593 added `typing.Annotated` as a way of
adding context-specific metadata to existing types, and specifies that
`Annotated[T, x]` _should_ be treated as `T` by any tool or library without special
logic for `x`. ...

Example:
```python
from typing import Annotated
from annotated_types import Gt, Len, Predicate

class MyClass:
    age: Annotated[int, Gt(18)]                         # Valid: 19, 20, ...
                                                        # Invalid: 17, 18, "19", 19.0, ...
    factors: list[Annotated[int, Predicate(is_prime)]]  # Valid: 2, 3, 5, 7, 11, ...
...
```

...

</details>

### pytest

pytest: simple powerful testing with Python

`pip install pytest` · installs (wheel) · licence: MIT · rank 25 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pytest/) · [source](https://github.com/pytest-dev/pytest)

<details><summary>README extract</summary>

The `pytest` framework makes it easy to write small tests, yet
scales to support complex functional testing for applications and libraries.

An example of a simple test:

To execute it:
Thanks to `pytest`'s detailed assertion introspection, you can simply use plain `assert` statements. See getting-started for more examples.

Features:
- Detailed info on failing assert statements (no need to remember `self.assert*` names)

- Auto-discovery
 of test modules and functions

- Modular fixtures for
 managing small or parametrized long-lived test resources ...

Example:
```python
# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
```

Sections: Features, Documentation, Bugs/Requests, pytest for enterprise

</details>

### iniconfig

brain-dead simple config-ini parsing

`pip install iniconfig` · installs (wheel) · licence: MIT · rank 26 · last release 2026-10-06 · [PyPI](https://pypi.org/project/iniconfig/)

<details><summary>README extract</summary>

iniconfig is a small and simple INI-file parser module
having a unique set of features:

* maintains order of sections and entries
* supports multi-line values with or without line-continuations
* supports "#" comments everywhere
* raises errors with proper line-numbers
* no bells and whistles like automatic substitutions
* iniconfig raises an ...

Example:
```python
>>> import iniconfig
>>> ini = iniconfig.IniConfig.parse("example.ini")
>>> ini'section1' # raises KeyError if not exists
'value1'
>>> ini.get('section1', 'name1b', [], lambda x: x.split(","))
['value1', 'value2']
>>> ini.get('section1', 'notexist', [], lambda x: x.split(","))
[]
>>> [x.name for x in list(ini)]
['section1', 'section2']
...
```

Sections: iniconfig: brain-dead simple parsing of ini files, Basic Example

</details>

### typing-inspection

Runtime typing introspection tools

`pip install typing-inspection` · installs (wheel) · licence: MIT · rank 27 · last release 2026-11-04 · [PyPI](https://pypi.org/project/typing-inspection/) · [docs](https://pydantic.github.io/typing-inspection/dev/) · [source](https://github.com/pydantic/typing-inspection)

<details><summary>README extract</summary>

`typing-inspection` provides tools to inspect type annotations at runtime.

</details>

### platformdirs

A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`.

`pip install platformdirs` · installs (wheel) · licence: MIT · rank 42 · last release 2026-11-04 · [PyPI](https://pypi.org/project/platformdirs/) · [docs](https://platformdirs.readthedocs.io) · [source](https://github.com/tox-dev/platformdirs)

<details><summary>README extract</summary>

A Python package for determining platform-specific directories (e.g. user data, config, cache, logs). Handles the
differences between macOS, Windows, Linux/Unix, Android, and iOS so you don't have to.

Example:
```python
from platformdirs import PlatformDirs

dirs = PlatformDirs("MyApp", "MyCompany")
dirs.user_data_dir  # ~/.local/share/MyApp (Linux)
dirs.user_config_dir  # ~/.config/MyApp (Linux)
dirs.user_cache_dir  # ~/.cache/MyApp (Linux)
dirs.user_state_dir  # ~/.local/state/MyApp (Linux)
dirs.user_log_dir  # ~/.local/state/MyApp/log (Linux)
...
```

Sections: platformdirs, Quick start, Directory types, Documentation

</details>

### pathspec

Utility library for gitignore style pattern matching of file paths.

`pip install pathspec` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 45 · last release 2026-04-27 · [PyPI](https://pypi.org/project/pathspec/) · [docs](https://python-path-specification.readthedocs.io/en/latest/index.html) · [source](https://github.com/cpburnz/python-pathspec)

<details><summary>README extract</summary>

*pathspec* is a utility library for pattern matching of file paths. So far this
only includes Git's gitignore pattern matching.

Example:
```python
>>> from pathspec import PathSpec
>>> # The gitignore-style patterns for files to select, but we're including
>>> # instead of ignoring.
>>> spec_text = """
...
... # This is a comment because the line begins with a hash: "#"
...
... # Include several project directories (and all descendants) relative to
...
```

Sections: PathSpec, Tutorial, Performance, FAQ, 1. How do I ignore files like *.gitignore*?, Source, Documentation, Other Languages, 1.1.1 (2026-04-26), 1.1.0 (2026-04-22), 1.0.4 (2026-01-26), 1.0.3 (2026-01-09), 1.0.2 (2026-01-07), 1.0.1 (2026-01-06)

</details>

### filelock

A platform independent file lock.

`pip install filelock` · installs (wheel) · licence: MIT · rank 49 · last release 2026-11-04 · [PyPI](https://pypi.org/project/filelock/) · [docs](https://py-filelock.readthedocs.io) · [source](https://github.com/tox-dev/filelock)

<details><summary>README extract</summary>

For more information checkout the official documentation.

</details>

### markdown-it-py

Python port of markdown-it. Markdown parsing, done right!

`pip install markdown-it-py` · installs (wheel) · licence: MIT License · rank 56 · last release 2026-05-07 · [PyPI](https://pypi.org/project/markdown-it-py/) · [docs](https://markdown-it-py.readthedocs.io)

<details><summary>README extract</summary>

[][github-link]
[][codecov-link]
[][pypi-link]
[][conda-link]
[][install-link]

> Markdown parser done right.

- Follows the CommonMark spec for baseline parsing
- Configurable syntax: you can add new rules and even replace existing ones.
- Pluggable: Adds syntax extensions to extend the parser (see the plugin list). ...

Example:
```python
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin

md = (
    MarkdownIt('commonmark', {'breaks':True,'html':True})
    .use(front_matter_plugin)
    .use(footnote_plugin)
    .enable('table')
)
text = ("""

a: 1

a | b
- | -
1 | 2

A footnote [^1]

...
```

...

</details>

### mdurl

Markdown URL utilities

`pip install mdurl` · installs (wheel) · licence: MIT License · rank 60 · last release 2022-08-14 · [PyPI](https://pypi.org/project/mdurl/)

<details><summary>README extract</summary>

This is a Python port of the JavaScript mdurl package.
See the upstream README.md file for API documentation.

</details>

### pytz

World timezone definitions, modern and historical

`pip install pytz` · installs (wheel) · licence: MIT License · rank 67 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pytz/) · [source](https://github.com/stub42/pytz.git)

<details><summary>README extract</summary>

:Author: Stuart Bishop <stuart@stuartbishop.net>

pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.4
or higher. ...

Sections: pytz - World Timezone Definitions for Python, Introduction, pytz for Enterprise, Example & Usage, Localized times and date arithmetic, `tzinfo` API, Problems with Localtime, Country Information, What is UTC, Helpers, Internationalization - i18n/l10n, Latest Versions, Bugs, Feature Requests & Patches, Issues & Limitations

</details>

### aiohappyeyeballs

Happy Eyeballs for asyncio

`pip install aiohappyeyeballs` · installs (wheel) · licence: Python Software Foundation License · rank 72 · last release 2026-07-01 · [PyPI](https://pypi.org/project/aiohappyeyeballs/) · [docs](https://aiohappyeyeballs.readthedocs.io) · [source](https://github.com/aio-libs/aiohappyeyeballs)

<details><summary>README extract</summary>

Documentation:

Source Code:

Happy Eyeballs
(RFC 8305)

This library exists to allow connecting with
Happy Eyeballs
(RFC 8305)
when you
already have a list of addrinfo and not a DNS name. ...

Example:
```python
addr_infos = await loop.getaddrinfo("example.org", 80)

socket = await start_connection(addr_infos)
socket = await start_connection(addr_infos, local_addr_infos=local_addr_infos, happy_eyeballs_delay=0.2)

transport, protocol = await loop.create_connection(
    MyProtocol, sock=socket, ...)

...
```

Sections: aiohappyeyeballs, Use case, Example usage

</details>

### python-multipart

A streaming multipart parser for Python

`pip install python-multipart` · installs (wheel) · licence: Apache-2.0 · rank 76 · last release 2026-10-31 · [PyPI](https://pypi.org/project/python-multipart/) · [docs](https://kludex.github.io/python-multipart/) · [source](https://github.com/Kludex/python-multipart)

<details><summary>README extract</summary>

Python-Multipart reads the data that a web browser sends when someone submits a form or uploads a file.

It powers file uploads in Starlette and FastAPI.

When you fill in a form on a website and click "Submit", your browser sends the data to a server. ...

Example:
```python
from io import BytesIO

from python_multipart import parse_form

body = (
    b"--boundary\r\n"
    b'Content-Disposition: form-data; name="username"\r\n'
    b"\r\n"
    b"alice\r\n"
    b"--boundary\r\n"
    b'Content-Disposition: form-data; name="avatar"; filename="cat.txt"\r\n'
    b"Content-Type: text/plain\r\n"
    b"\r\n"
    b"meow\r\n"
...
```

...

</details>

### lxml

Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.

`pip install lxml` · installs (wheel) · licence: BSD-3-Clause · rank 81 · last release 2026-09-03 · [PyPI](https://pypi.org/project/lxml/) · [source](https://github.com/lxml/lxml)

<details><summary>README extract</summary>

lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.
It provides safe and convenient access to these libraries using the
ElementTree API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more. ...

Sections: 6.1.3 (2026-09-02), Bugs fixed

</details>

### ruff

An extremely fast Python linter and code formatter, written in Rust.

`pip install ruff` · installs (wheel) · licence: MIT · rank 85 · last release 2026-11-05 · [PyPI](https://pypi.org/project/ruff/) · [docs](https://docs.astral.sh/ruff/) · [source](https://github.com/astral-sh/ruff)

<details><summary>README extract</summary>

Docs | Playground

An extremely fast Python linter and code formatter, written in Rust.

 Linting the CPython codebase from scratch.

- ⚡️ 10-100x faster than existing linters (like Flake8) and formatters (like Black)
- 🐍 Installable via `pip`
- 🛠️ `pyproject.toml` support
- 🤝 Python 3.15 compatibility ...

Sections: Ruff, Testimonials, Getting Started, Usage, Configuration, Rules

</details>

### greenlet

Lightweight in-process concurrent programming

`pip install greenlet` · installs (wheel) · licence: MIT AND PSF-2.0 · rank 88 · last release 2026-09-14 · [PyPI](https://pypi.org/project/greenlet/) · [docs](https://greenlet.readthedocs.io) · [source](https://github.com/python-greenlet/greenlet)

<details><summary>README extract</summary>

Greenlets are lightweight coroutines for in-process concurrent
programming.

The "greenlet" package is a spin-off of Stackless, a version of
CPython that supports micro-threads called "tasklets". Tasklets run
pseudo-concurrently (typically in a single or a few OS-level threads)
and are synchronized with data exchanges on "channels". ...

Sections: Who is using Greenlet?, Getting Greenlet

</details>

### openai

The official Python library for the openai API

`pip install openai` · installs (wheel) · licence: Apache-2.0 · rank 97 · last release 2026-11-05 · [PyPI](https://pypi.org/project/openai/) · [source](https://github.com/openai/openai-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The OpenAI Python library provides convenient access to the OpenAI REST API from any Python 3.10+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by HTTPX2.

It is generated from our OpenAPI specification. ...

Example:
```python
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.responses.create(
    model="gpt-5.5",
    instructions="You are a coding assistant that talks like a pirate.",
...
```

...

</details>

### watchfiles

Simple, modern and high performance file watching and code reload in python.

`pip install watchfiles` · installs (wheel) · licence: MIT License · rank 99 · last release 2026-09-21 · [PyPI](https://pypi.org/project/watchfiles/) · [docs](https://watchfiles.helpmanual.io) · [source](https://github.com/samuelcolvin/watchfiles)

<details><summary>README extract</summary>

Simple, modern and high performance file watching and code reload in python.

Documentation: watchfiles.helpmanual.io

Source Code: github.com/samuelcolvin/watchfiles

Underlying file system notifications are handled by the Notify rust library.

This package was previously named "watchgod",
see the migration guide for more information.

Example:
```python
from watchfiles import watch

for changes in watch('./path/to/dir'):
    print(changes)
```

Sections: watchfiles, Usage, `watch` Usage, `awatch` Usage, `run_process` Usage, `arun_process` Usage, CLI

</details>

### psutil

Cross-platform lib for process and system monitoring.

`pip install psutil` · installs (wheel) · licence: BSD-3-Clause · rank 101 · last release 2026-01-28 · [PyPI](https://pypi.org/project/psutil/)

<details><summary>README extract</summary>

downloadsstarsforkscontributorspackages|
versionlicensestackoverflowtwittertidelift|
github-actions-wheelsgithub-actions-bsd|

- Home page
- Install
- Documentation
- Download
- Forum
- StackOverflow
- Blog
- What's new ...

Example:
```python
>>> import psutil
>>>
>>> psutil.cpu_times()
scputimes(user=3961.46, nice=169.729, system=2150.659, idle=16900.540, iowait=629.59, irq=0.0, softirq=19.42, steal=0.0, guest=0, guest_nice=0.0)
>>>
>>> for x in range(3):
...     psutil.cpu_percent(interval=1)
...
4.0
5.9
3.8
>>>
>>> for x in range(3):
...
```

Sections: Quick links, Summary, Example usages, CPU, Memory, Disks, Network, Sensors, Other system info, Process management, Further process APIs, Heap info, Windows services, Projects using psutil

</details>

### distro

Distro - an OS platform information API

`pip install distro` · installs (wheel) · licence: Apache Software License · rank 106 · last release 2023-12-24 · [PyPI](https://pypi.org/project/distro/)

<details><summary>README extract</summary>

`distro` provides information about the
OS distribution it runs on, such as a reliable machine-readable ID, or
version information.

It is the recommended replacement for Python's original
`platform.linux_distribution`
function (removed in Python 3.8). ...

Sections: Distro - an OS platform information API, Usage, Documentation, Background, Package manager distributions

</details>

### beautifulsoup4

Screen-scraping library

`pip install beautifulsoup4` · installs (wheel) · licence: MIT License · rank 110 · last release 2026-06-07 · [PyPI](https://pypi.org/project/beautifulsoup4/)

<details><summary>README extract</summary>

Beautiful Soup is a library that makes it easy to scrape information
from web pages. It sits atop an HTML or XML parser, providing Pythonic
idioms for iterating, searching, and modifying the parse tree.

Example:
```python
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup("SomebadHTML")
>>> print(soup.prettify())

   Some

    bad

     HTML

>>> soup.find(string="bad")
'bad'
>>> soup.i
HTML

>>> soup = BeautifulSoup("SomebadXML", "xml")

>>> print(soup.prettify())
<?xml version="1.0" encoding="utf-8"?>

 Some

 bad

  XML
```

Sections: Quick start, Links, Note on Python 2 sunsetting, Building the documentation, Running the unit tests

</details>

### shellingham

Tool to Detect Surrounding Shell

`pip install shellingham` · installs (wheel) · licence: ISC License (ISCL) · rank 111 · last release 2023-10-24 · [PyPI](https://pypi.org/project/shellingham/)

<details><summary>README extract</summary>

Shellingham detects what shell the current Python executable is running in.

Example:
```python
>>> import shellingham
>>> shellingham.detect_shell()
('bash', '/bin/bash')
```

Sections: Shellingham: Tool to Detect Surrounding Shell, Usage, Notes

</details>

### tomli

A lil' TOML parser

`pip install tomli` · installs (wheel) · licence: MIT · rank 125 · last release 2026-10-07 · [PyPI](https://pypi.org/project/tomli/)

<details><summary>README extract</summary>

> A lil' TOML parser

Table of Contents *generated with mdformat-toc*

- Intro
- Installation
- Usage
 - Parse a TOML string
 - Parse a TOML file
 - Handle invalid TOML
 - Construct `decimal.Decimal`s from TOML floats
 - Building a `tomli`/`tomllib` compatibility layer ...

Features:
- it's lil'
- pure Python with zero dependencies

 14x as fast as tomlkit,
 2.1x as fast as toml
- outputs basic data types only
- 100% spec compliant: passes all tests in
 toml-lang/toml-test
 test suite
- thoroughly tested: 100% branch coverage

Example:
```python
import tomli

toml_str = """
[[players]]
name = "Lehtinen"
number = 26

[[players]]
name = "Numminen"
number = 27
"""

toml_dict = tomli.loads(toml_str)
assert toml_dict == {
...

</details>

### cachetools

Extensible memoizing collections and decorators

`pip install cachetools` · installs (wheel) · licence: MIT · rank 127 · last release 2026-11-07 · [PyPI](https://pypi.org/project/cachetools/) · [docs](https://cachetools.readthedocs.io/en/stable/) · [source](https://github.com/tkem/cachetools/)

<details><summary>README extract</summary>

This module provides various memoizing collections and decorators,
including variants of the Python Standard Library's @lru_cache
function decorator.

For the purpose of this module, a *cache* is a mutable mapping of a
fixed maximum size. When the cache is full, i.e. ...

Example:
```python
from cachetools import cached, LRUCache, TTLCache

# speed up calculating Fibonacci numbers with dynamic programming
@cached(cache={})
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

# cache least recently used Python Enhancement Proposals
@cached(cache=LRUCache(maxsize=32))
def get_pep(num):
    from urllib.request import urlopen
...
```

Sections: cachetools, Project Resources, Related Projects

</details>

### editables

Editable installations

`pip install editables` · installs (wheel) · licence: MIT License · rank 130 · last release 2026-04-14 · [PyPI](https://pypi.org/project/editables/) · [docs](https://editables.readthedocs.io) · [source](https://github.com/pfmoore/editables)

<details><summary>README extract</summary>

This library supports the building of wheels which, when installed, will
expose packages in a local directory on `sys.path` in "editable mode". In
other words, changes to the package source will be reflected in the package
visible to Python, without needing a reinstall.

Example:
```python
from editables import EditableProject

my_project = EditableProject("foo", "/path/to/foo")
my_project.add_to_path("src")

# Build a wheel however you prefer...
wheel = BuildAWheel()

# Add files to the wheel
for name, content in my_project.files():
    wheel.add_file(name, content)

# Record any runtime dependencies
...
```

Sections: A Python library for creating "editable wheels", Usage, Python Compatibility

</details>

### oauthlib

A generic, spec-compliant, thorough implementation of the OAuth request-signing logic

`pip install oauthlib` · installs (wheel) · licence: BSD-3-Clause · rank 131 · last release 2026-10-31 · [PyPI](https://pypi.org/project/oauthlib/) · [docs](https://oauthlib.readthedocs.io/) · [source](https://github.com/oauthlib/oauthlib)

<details><summary>README extract</summary>

*A generic, spec-compliant, thorough implementation of the OAuth request-signing
logic for Python 3.8+*

OAuth often seems complicated and difficult-to-implement. There are several
prominent libraries for handling OAuth requests, but they all suffer from one or
both of the following:

1. They predate the OAuth 1.0 spec, AKA RFC 5849.
2. ...

Sections: OAuthLib - Python Framework for OAuth1 & OAuth2, Documentation, Interested in making OAuth requests?, Using OAuthLib? Please get in touch!

</details>

### more-itertools

More routines for operating on iterables, beyond itertools

`pip install more-itertools` · installs (wheel) · licence: MIT · rank 133 · last release 2026-10-14 · [PyPI](https://pypi.org/project/more-itertools/) · [docs](https://more-itertools.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

Python's `itertools` library is a gem - you can compose elegant solutions
for a variety of problems with the functions it provides. In `more-itertools`
we collect additional building blocks, recipes, and routines for working with
Python iterables. ...

Example:
```python
>>> from more_itertools import flatten
>>> iterable = [(0, 1), (2, 3)]
>>> list(flatten(iterable))
[0, 1, 2, 3]
```

Sections: More Itertools, Getting started, Links elsewhere

</details>

### virtualenv

Virtual Python Environment builder

`pip install virtualenv` · installs (wheel) · licence: MIT · rank 134 · last release 2026-11-06 · [PyPI](https://pypi.org/project/virtualenv/) · [docs](https://virtualenv.pypa.io) · [source](https://github.com/pypa/virtualenv)

<details><summary>README extract</summary>

A tool for creating isolated `virtual` python environments.

- Installation
- Documentation
- Changelog
- Issues
- PyPI
- Github

</details>

### threadpoolctl

threadpoolctl

`pip install threadpoolctl` · installs (wheel) · licence: BSD-3-Clause · rank 159 · last release 2026-11-05 · [PyPI](https://pypi.org/project/threadpoolctl/)

<details><summary>README extract</summary>

Python helpers to limit the number of threads used in the
threadpool-backed of common native libraries used for scientific
computing and data science (e.g. BLAS and OpenMP).

Fine control of the underlying thread-pool size can be useful in
workloads that involve nested parallelism so as to mitigate
oversubscription issues. ...

Example:
```python
>>> from threadpoolctl import threadpool_info
>>> from pprint import pprint
>>> pprint(threadpool_info())
[]

>>> import numpy
>>> pprint(threadpool_info())
[{'filepath': '/home/ogrisel/miniconda3/envs/tmp/lib/libmkl_rt.so',
  'internal_api': 'mkl',
  'num_threads': 2,
  'prefix': 'libmkl_rt',
  'threading_layer': 'intel',
  'user_api': 'blas',
...
```

...

</details>

### email-validator

A robust email address syntax and deliverability validation library.

`pip install email-validator` · installs (wheel) · licence: The Unlicense (Unlicense) · rank 163 · last release 2025-08-26 · [PyPI](https://pypi.org/project/email-validator/)

<details><summary>README extract</summary>

A robust email address syntax and deliverability validation library for
Python 3.8+ by Joshua Tauberer.

This library validates that a string is of the form `name@example.com`
and optionally checks that the domain name is set up to receive email. ...

Features:
The module provides a function `validate_email(email_address)` which
takes an email address and:

- Raises a `EmailNotValidError` with a helpful, human-readable error
 message explaining why the email address is not valid, or ...

Example:
```python
from email_validator import validate_email, EmailNotValidError

email = "my+address@example.org"

try:

  # Check that the email address is valid. Turn on check_deliverability
  # for first-time validations like on account creation pages (but not
  # login pages).
...

</details>

### anthropic

The official Python library for the anthropic API

`pip install anthropic` · installs (wheel) · licence: Apache Software License · rank 164 · last release 2026-11-05 · [PyPI](https://pypi.org/project/anthropic/) · [source](https://github.com/anthropics/anthropic-sdk-python)

<details><summary>README extract</summary>

The Anthropic SDK for Python provides access to the Claude API from Python applications.

Full documentation is available at platform.claude.com/docs/en/api/sdks/python.

Example:
```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude",
        }
    ],
...
```

Sections: Anthropic SDK for Python, Documentation, Getting started, Requirements

</details>

### nodeenv

Node.js virtual environment builder

`pip install nodeenv` · installs (wheel) · licence: BSD License · rank 165 · last release 2026-10-31 · [PyPI](https://pypi.org/project/nodeenv/)

<details><summary>README extract</summary>

`nodeenv` (node.js virtual environment) is a tool to create
isolated node.js environments.

It creates an environment that has its own installation directories,
that doesn't share libraries with other node.js virtual environments.

Also the new environment can be integrated with the environment which was built
by virtualenv (python). ...

Example:
```python
$ SSL_CERT_FILE=$(python -c 'import certifi; print(certifi.where())') nodeenv env
```

Sections: Node.js virtual environment, Shell completion, Dependency, For nodeenv, For node.js, Usage, Basic, Advanced, Command Line Options, Basic options, Configuration, Alternatives, Version 1.12.0, Version 1.11.1

</details>

### python-discovery

Python interpreter discovery

`pip install python-discovery` · installs (wheel) · licence: MIT · rank 167 · last release 2026-11-06 · [PyPI](https://pypi.org/project/python-discovery/) · [docs](https://python-discovery.readthedocs.io) · [source](https://github.com/tox-dev/python-discovery)

<details><summary>README extract</summary>

`python-discovery` is a library for discovering Python interpreters installed on your machine. You may have multiple
Python versions from system packages, pyenv, mise,
asdf, uv, or the Windows registry (PEP 514). This library finds
the right one for you. ...

Example:
```python
from pathlib import Path

from python_discovery import DiskCache, get_interpreter

cache = DiskCache(root=Path("~/.cache/python-discovery").expanduser())
result = get_interpreter("python3.12", cache=cache)
if result is not None:
    print(result.executable)  # /usr/bin/python3.12
    print(result.implementation)  # CPython
...
```

Sections: `python-discovery`, What is python-discovery?, Usage, Documentation

</details>

### execnet

execnet: rapid multi-Python deployment

`pip install execnet` · installs (wheel) · licence: MIT · rank 175 · last release 2025-11-12 · [PyPI](https://pypi.org/project/execnet/)

<details><summary>README extract</summary>

execnet provides carefully tested means to ad-hoc interact with Python
interpreters across version, platform and network barriers. It provides
a minimal and fast API targeting the following uses:

* distribute tasks to local or remote processes
* write and deploy hybrid multi-process applications
* write scripts to administer multiple hosts

Features:
* zero-install bootstrapping: no remote installation required!

* flexible communication: send/receive as well as
 callback/queue mechanisms supported

* simple serialization of python builtin types (no pickling) ...

Sections: execnet: distributed Python deployment and communication, Features

</details>

### tabulate

Pretty-print tabular data

`pip install tabulate` · installs (wheel) · licence: MIT · rank 183 · last release 2026-03-04 · [PyPI](https://pypi.org/project/tabulate/)

<details><summary>README extract</summary>

Pretty-print tabular data in Python, a library and a command-line
utility.

The main use cases of the library are:

- printing small tables without hassle: just one function call,
 formatting is guided by the data itself ...

Example:
```python
>>> from tabulate import tabulate

>>> table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
...          ["Moon",1737,73.5],["Mars",3390,641.85]]
>>> print(tabulate(table))
-----  ------  -------------
Sun    696000     1.9891e+09
Earth    6371  5973.6
Moon     1737    73.5
Mars     3390   641.85
-----  ------  -------------
```

...

</details>

### pypdf

A pure-python PDF library capable of splitting, merging, cropping, and transforming PDF files

`pip install pypdf` · installs (wheel) · licence: BSD-3-Clause · rank 187 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pypdf/) · [docs](https://pypdf.readthedocs.io/en/latest/) · [source](https://github.com/py-pdf/pypdf)

<details><summary>README extract</summary>

pypdf is a free and open-source pure-python PDF library capable of splitting,
merging,
cropping, and transforming
the pages of PDF files. It can also add
custom data, viewing options, and
passwords
to PDF files. pypdf can
retrieve text
and
metadata
from PDFs as well.

See pdfly for a CLI application that uses pypdf to interact with PDFs.

Example:
```python
from pypdf import PdfReader

reader = PdfReader("example.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
```

Sections: pypdf, Usage, Q&A, Issues, Code

</details>

### ruamel.yaml

ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order

`pip install ruamel.yaml` · installs (wheel) · licence: MIT License · rank 188 · last release 2026-01-02 · [PyPI](https://pypi.org/project/ruamel.yaml/) · [docs](https://yaml.dev/doc/ruamel.yaml) · [source](https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/)

<details><summary>README extract</summary>

`ruamel.yaml` is a YAML 1.2 loader/dumper package for Python.

| | |
| - | - |
| version |0.19.0 |
| updated |2025-01-02 |
| documentation | |
| repository | |
| pypi | |

*If you are interested in future upgrades of `ruamel.yaml`
please check the documentation on installing,
since at some point I might not be able to upload a new version to PyPI ...

</details>

### chardet

Universal character encoding detector

`pip install chardet` · installs (wheel) · licence: 0BSD · rank 193 · last release 2026-10-18 · [PyPI](https://pypi.org/project/chardet/) · [docs](https://chardet.readthedocs.io) · [source](https://github.com/chardet/chardet)

<details><summary>README extract</summary>

Universal character encoding detector.

chardet 7 is a ground-up, 0BSD-licensed rewrite of chardet.
Same package name, same public API — drop-in replacement for chardet 5.x/6.x, just much faster and more accurate.
Python 3.10+, zero runtime dependencies, works on PyPy.

Read more details about the rewrite process.

Features:
99.7% accuracy on 3,138 test files. 359x faster than chardet 6.0.0,
and +13.1pp more accurate than charset-normalizer 3.5.2 while being
1.3x faster. Language detection for every text result. MIME type detection for
binary files. 0BSD licensed. ...

Example:
```python
import chardet

chardet.detect(b"Python is a great programming language for beginners and experts alike.")
# {'encoding': 'ascii', 'confidence': 1.0, 'language': 'en', 'mime_type': 'text/plain'}

...

</details>

### decorator

Decorators for Humans

`pip install decorator` · installs (wheel) · licence: BSD-2-Clause · rank 208 · last release 2026-05-18 · [PyPI](https://pypi.org/project/decorator/)

<details><summary>README extract</summary>

The goal of the decorator module is to make it easy to define
signature-preserving function decorators and decorator factories.
It also includes an implementation of multiple dispatch and other niceties
(please check the docs). It is released under a two-clauses
BSD license, i.e. ...

Example:
```python
from decorator import decorator

@decorator
def warn_slow(func, timelimit=60, *args, **kw):
    t0 = time.time()
    result = func(*args, **kw)
    dt = time.time() - t0
    if dt > timelimit:
        logging.warning('%s took %d seconds', func.name, dt)
    else:
        logging.info('%s took %d seconds', func.name, dt)
    return result

...
```

Sections: Decorators for Humans, Repository, Documentation, For the impatient

</details>

### uv

An extremely fast Python package and project manager, written in Rust.

`pip install uv` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 215 · last release 2026-11-03 · [PyPI](https://pypi.org/project/uv/) · [docs](https://docs.astral.sh/uv) · [source](https://github.com/astral-sh/uv)

<details><summary>README extract</summary>

An extremely fast Python package and project manager, written in Rust.

 Installing Trio's dependencies with a warm cache.

Features:
- A single tool to replace `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, and
 more.
- 10-100x faster than `pip`.
- Provides comprehensive project management, with a
 universal lockfile. ...

Sections: uv, Highlights, Documentation, Features, Projects, Scripts, Tools, Python versions, The pip interface, FAQ, How do you pronounce uv?, How should I stylize uv?, Is uv ready for production?

</details>

### jsonpointer

Identify specific nodes in a JSON document (RFC 6901)

`pip install jsonpointer` · installs (wheel) · licence: BSD License · rank 216 · last release 2026-11-06 · [PyPI](https://pypi.org/project/jsonpointer/)

<details><summary>README extract</summary>

Resolve JSON Pointers in Python

Library to resolve JSON Pointers according to
RFC 6901

See source code for examples

</details>

### sentry-sdk

Python client for Sentry (https://sentry.io)

`pip install sentry-sdk` · installs (wheel) · licence: MIT · rank 217 · last release 2026-11-05 · [PyPI](https://pypi.org/project/sentry-sdk/) · [docs](https://docs.sentry.io/platforms/python/)

<details><summary>README extract</summary>

_Bad software is everywhere, and we're tired of it. Sentry is on a mission to help developers write better software faster, so we can get back to enjoying technology. If you want to join us
Check out our open positions.

Welcome to the official Python SDK for Sentry.

Example:
```python
import sentry_sdk
sentry_sdk.init(...)  # same as above

sentry_sdk.capture_message("Hello Sentry!")  # You'll see this in your Sentry dashboard.

raise ValueError("Oops, something went wrong!")  # This will create an error event in Sentry.
```

Sections: Official Sentry SDK for Python, 📦 Getting Started, Prerequisites, Basic Configuration, Quick Usage Example, 📚 Documentation, 🧩 Integrations, 🚧 Migrating Between Versions?, From `1.x` to `2.x`, From `raven-python`, 🛟 Need Help?, 🔗 Resources

</details>

### Deprecated

Python @deprecated decorator to deprecate old python classes, functions or methods.

`pip install Deprecated` · installs (wheel) · licence: MIT · rank 227 · last release 2026-10-30 · [PyPI](https://pypi.org/project/Deprecated/) · [docs](https://deprecated.readthedocs.io/en/latest/) · [source](https://github.com/laurent-laporte-pro/deprecated)

<details><summary>README extract</summary>

Python `@deprecated` decorator to deprecate old python classes, functions or methods.

Removing a function from a library breaks the code of its users. Deprecating it first gives
them time to migrate: the Deprecated library marks classes, functions, methods and parameters
as deprecated, emits a warning that points at the calling code, and can ...

Features:
Since Python 3.13, `warnings.deprecated`
(PEP 702) emits a runtime warning and lets the type
checkers report the use of deprecated objects. ...

Example:
```python
from deprecated import deprecated

@deprecated(reason="use new_function", version="2.1.0")
def some_old_function(x, y):
    return x + y

some_old_function(1, 2)
```

Sections: Deprecated Decorator, Usage, Documenting the life cycle, Why not `warnings.deprecated`?

</details>

### fastjsonschema

Fastest Python implementation of JSON schema

`pip install fastjsonschema` · installs (wheel) · licence: BSD License · rank 250 · last release 2026-11-01 · [PyPI](https://pypi.org/project/fastjsonschema/)

### jsonpatch

Apply JSON-Patches (RFC 6902)

`pip install jsonpatch` · installs (wheel) · licence: BSD-3-Clause · rank 251 · last release 2026-11-06 · [PyPI](https://pypi.org/project/jsonpatch/) · [docs](https://python-json-patch.readthedocs.org/) · [source](https://github.com/stefankoegl/python-json-patch.git)

<details><summary>README extract</summary>

Applying JSON Patches in Python

Library to apply JSON Patches according to
RFC 6902

See source code for examples

Type hints

jsonpatch ships type stubs (in the `jsonpatch-stubs` directory, as
jsonpatch.py is a single-file module), so type checkers such as mypy and
pyright work with it without further setup. JSON documents are typed as `Any`. ...

</details>

### black

The uncompromising code formatter.

`pip install black` · installs (wheel) · licence: MIT · rank 252 · last release 2026-10-10 · [PyPI](https://pypi.org/project/black/) · [docs](https://black.readthedocs.io/) · [source](https://github.com/psf/black)

<details><summary>README extract</summary>

> “Any color you like.”

_Black_ is the uncompromising Python code formatter. By using it, you agree to cede
control over minutiae of hand-formatting. In return, _Black_ gives you speed,
determinism, and freedom from `pycodestyle` nagging about formatting. You will save time
and mental energy for more important matters. ...

Features:
This release fixes a security issue in Black's bundled GitHub Action. Repositories that
use the action are encouraged to update to the latest version of Black immediately. ...

Sections: The Uncompromising Code Formatter, Usage, The _Black_ code style, Pragmatism, Configuration, Used by, Testimonials, Show your style, Version 26.10.1, Highlights, Stable style, Preview style, Performance

</details>

### async-timeout

Timeout context manager for asyncio programs

`pip install async-timeout` · installs (wheel) · licence: Apache Software License · rank 261 · last release 2024-11-06 · [PyPI](https://pypi.org/project/async-timeout/)

<details><summary>README extract</summary>

asyncio-compatible timeout context manager.

This library has effectively been upstreamed into Python 3.11+.

Therefore this library is considered deprecated and no longer actively supported. ...

Example:
```python
from async_timeout import timeout
async with timeout(1.5):
    await inner()
```

Sections: async-timeout, DEPRECATED, Usage example

</details>

### jedi

An autocompletion tool for Python that can be used for text editors.

`pip install jedi` · installs (wheel) · licence: MIT License · rank 272 · last release 2026-10-12 · [PyPI](https://pypi.org/project/jedi/) · [docs](https://jedi.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Features:
Jedi's features are listed here:
Features.

You can run Jedi on Python 3.10+ but it should also
understand code that is older than those versions. Additionally you should be
able to use Virtualenvs
very well. ...

Sections: Issues & Questions, Features and Limitations, API, Static Analysis, Refactoring, Code Search, 0.20.1 (2026-10-12), 0.20.0 (2026-05-02), 0.19.2 (2024-11-10), 0.19.1 (2023-10-02), 0.19.0 (2023-07-29), 0.18.2 (2022-11-21), 0.18.1 (2021-11-17), 0.18.0 (2020-12-25)

</details>

### parso

A Python Parser

`pip install parso` · installs (wheel) · licence: MIT License · rank 274 · last release 2026-05-01 · [PyPI](https://pypi.org/project/parso/)

<details><summary>README extract</summary>

Parso is a Python parser that supports error recovery and round-trip parsing
for different Python versions (in multiple Python versions). Parso is also able
to list multiple syntax errors in your python file.

Parso has been battle-tested by jedi. It was pulled out of jedi to be useful
for other projects as well. ...

Example:
```python
>>> import parso
>>> module = parso.parse('hello + 1', version="3.9")
>>> expr = module.children[0]
>>> expr
PythonNode(arith_expr, [<Name: hello@1,0>, <Operator: +>, <Number: 1>])
>>> print(expr.get_code())
hello + 1
>>> name = expr.children[0]
>>> name
<Name: hello@1,0>
>>> name.end_pos
(1, 5)
>>> expr.end_pos
(1, 9)
```

...

</details>

### flatbuffers

The FlatBuffers serialization format for Python

`pip install flatbuffers` · installs (wheel) · licence: Apache Software License · rank 276 · last release 2025-12-19 · [PyPI](https://pypi.org/project/flatbuffers/) · [docs](https://google.github.io/flatbuffers/) · [source](https://github.com/google/flatbuffers)

<details><summary>README extract</summary>

Python runtime library for use with the `Flatbuffers < serialization format.

</details>

### brotli

Python bindings for the Brotli compression library

`pip install brotli` · installs (wheel) · licence: MIT · rank 283 · last release 2026-10-22 · [PyPI](https://pypi.org/project/brotli/)

<details><summary>README extract</summary>

Brotli is a generic-purpose lossless compression algorithm that compresses data
using a combination of a modern variant of the LZ77 algorithm, Huffman coding
and 2nd order context modeling, with a compression ratio comparable to the best
currently available general-purpose compression methods. ...

Sections: Introduction, Build instructions, Vcpkg, Bazel, CMake, Python, Benchmarks, Related projects

</details>

### watchdog

Filesystem events monitoring

`pip install watchdog` · installs (wheel) · licence: Apache-2.0 · rank 289 · last release 2026-11-05 · [PyPI](https://pypi.org/project/watchdog/) · [docs](https://python-watchdog.readthedocs.io/en/stable/) · [source](https://github.com/gorakhargosh/watchdog/)

<details><summary>README extract</summary>

Python API and shell utilities to monitor file system events.

Browse the documentation online.

Works on 3.11+.

Features:
Too many people tried to do the same thing and none did what I needed Python
to do:

* pnotify
* unison fsmonitor
* fsmonitor
* guard
* pyinotify
* inotify-tools
* jnotify
* treewatcher
* file.monitor
* pyfilesystem

Example:
```python
import sys
import time

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event: FileSystemEvent) -> None:
        print(event)

event_handler = MyEventHandler()
observer = Observer()
...
```

...

</details>

### aioitertools

itertools and builtins for AsyncIO and mixed iterables

`pip install aioitertools` · installs (wheel) · licence: MIT · rank 294 · last release 2025-11-06 · [PyPI](https://pypi.org/project/aioitertools/) · [docs](https://aioitertools.omnilib.dev) · [source](https://github.com/omnilib/aioitertools)

<details><summary>README extract</summary>

Implementation of itertools, builtins, and more for AsyncIO and mixed-type iterables.

Install

aioitertools requires Python 3.9 or newer.
You can install it from PyPI:

Usage

aioitertools shadows the standard library whenever possible to provide
asynchronous version of the modules and functions you already know. ...

Example:
```python
from aioitertools import iter, next, map, zip

something = iter(...)
first_item = await next(something)

async for item in iter(something):
    ...

async def fetch(url):
    response = await aiohttp.request(...)
    return response.json

async for value in map(fetch, MANY_URLS):
    ...

async for a, b in zip(something, something_else):
    ...
```

</details>

### isort

A Python utility / library to sort Python imports.

`pip install isort` · installs (wheel) · licence: MIT · rank 296 · last release 2026-09-28 · [PyPI](https://pypi.org/project/isort/) · [docs](https://isort.readthedocs.io/) · [source](https://github.com/PyCQA/isort)

<details><summary>README extract</summary>

[][pypi status]

_____

Read Latest Documentation - Browse GitHub Code Repository
_____

isort is a Python utility / library to sort imports alphabetically and
automatically separate into sections and by type. It provides a command line
utility, Python library and plugins for various
editors to
quickly sort all your imports. ...

Features:
isort simply stands for import sort. It was originally called
"sortImports" however I got tired of typing the extra characters and
came to the realization camelCase is not pythonic. ...

Example:
```python
from my_lib import Object

import os

from my_lib import Object3

from my_lib import Object2

import sys

from third_party import lib15, lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8, lib9, lib10, lib11, lib12, lib13, lib14

import sys

...

</details>

### langsmith

Client library to connect to the LangSmith Observability and Evaluation Platform.

`pip install langsmith` · installs (wheel) · licence: MIT License · rank 308 · last release 2026-11-02 · [PyPI](https://pypi.org/project/langsmith/) · [source](https://github.com/langchain-ai/langsmith-python)

<details><summary>README extract</summary>

This package contains the Python client for interacting with the LangSmith platform.

To install:

Then trace:

Every LLM call inside `pipeline` is nested under a single trace in the LangSmith UI.

LangSmith helps you and your team develop and evaluate language models and intelligent agents. It is compatible with any LLM application. ...

Example:
```python
import os
from langsmith import Langsmith

client = Langsmith(
    api_key=os.environ.get("LANGSMITH_API_KEY"),  # This is the default and can be omitted
    tenant_id=os.environ.get("LANGSMITH_TENANT_ID"),  # This is the default and can be omitted
)

page = client.runs.query_v2(
    project_ids=["00000000-0000-0000-0000-000000000000"],
)
...
```

...

</details>

### lark

a modern parsing library

`pip install lark` · installs (wheel) · licence: MIT License · rank 321 · last release 2025-10-27 · [PyPI](https://pypi.org/project/lark/)

<details><summary>README extract</summary>

Lark is a modern general-purpose parsing library for Python.
With Lark, you can parse any context-free grammar, efficiently, with very little code.
Main Features:
- Builds a parse-tree (AST) automagically, based on the structure of the grammar
- Earley parser
- Can parse all context-free grammars
- Full support for ambiguous grammars ...

</details>

### tomli-w

A lil' TOML writer

`pip install tomli-w` · installs (wheel) · licence: MIT License · rank 327 · last release 2025-01-15 · [PyPI](https://pypi.org/project/tomli-w/)

<details><summary>README extract</summary>

> A lil' TOML writer

Table of Contents *generated with mdformat-toc*

- Intro
- Installation
- Usage
 - Write to string
 - Write to file
- FAQ
 - Does Tomli-W sort the document?
 - Does Tomli-W support writing documents with comments?
 - Can I customize insignificant whitespace?
 - Why does Tomli-W not write a multi-line string if the string ...

Features:
This default was chosen to achieve lossless parse/write round-trips.

TOML strings can contain newlines where exact bytes matter, e.g.

TOML strings also can contain newlines where exact byte representation is not relevant, e.g. ...

Example:
```python
import tomli_w

doc = {"table": {"nested": {}, "val3": 3}, "val2": 2, "val1": 1}
expected_toml = """\
val2 = 2
val1 = 1

[table]
val3 = 3

[table.nested]
"""
...

</details>

### setuptools-scm

the blessed package to manage your versions by scm tags

`pip install setuptools-scm` · installs (wheel) · licence: MIT · rank 328 · last release 2026-09-23 · [PyPI](https://pypi.org/project/setuptools-scm/) · [docs](https://setuptools-scm.readthedocs.io/) · [source](https://github.com/pypa/setuptools-scm/)

<details><summary>README extract</summary>

[setuptools-scm] extracts Python package versions from `git` or `hg` metadata
instead of declaring them as the version argument
or in a Source Code Managed (SCM) managed file.

Additionally [setuptools-scm] provides `setuptools` with a list of
files that are managed by the SCM

(i.e. it automatically adds all the SCM-managed files to the sdist). ...

Sections: setuptools-scm, about, `pyproject.toml` usage, Interaction with Enterprise Distributions

</details>

### fastuuid

Python bindings to Rust's UUID library.

`pip install fastuuid` · installs (wheel) · licence: BSD License · rank 334 · last release 2025-10-19 · [PyPI](https://pypi.org/project/fastuuid/)

### text-unidecode

The most basic Text::Unidecode port

`pip install text-unidecode` · installs (wheel) · licence: Artistic License; GNU General Public License (GPL); GNU General Public License v · rank 342 · last release 2019-08-30 · [PyPI](https://pypi.org/project/text-unidecode/)

_README extract left out: share-alike licence._

### pathable

Object-oriented paths

`pip install pathable` · installs (wheel) · licence: Apache Software License · rank 347 · last release 2026-05-19 · [PyPI](https://pypi.org/project/pathable/) · [source](https://github.com/p1c2u/pathable)

<details><summary>README extract</summary>

Pathable provides a small set of "path" objects for traversing hierarchical data (mappings, lists, and other subscriptable trees) using a familiar path-like syntax.

It’s especially handy when you want to: ...

Features:
* Intuitive path-based navigation for nested data (e.g., dicts/lists)
* Pluggable accessor layer for custom backends
* Pythonic, chainable API for concise and readable code
* Per-instance (bounded LRU) cached lookup accessor for repeated reads of ...

Example:
```python
from pathable import LookupPath

data = {
    "parts": {
        "part1": {"name": "Part One"},
        "part2": {"name": "Part Two"},
    }
}

root = LookupPath.from_lookup(data)

name = (root / "parts" / "part2" / "name").read_value()
assert name == "Part Two"
```

...

</details>

### mdit-py-plugins

Collection of plugins for markdown-it-py

`pip install mdit-py-plugins` · installs (wheel) · licence: MIT License · rank 348 · last release 2026-05-13 · [PyPI](https://pypi.org/project/mdit-py-plugins/) · [docs](https://mdit-py-plugins.readthedocs.io)

<details><summary>README extract</summary>

[][github-link]
[][codecov-link]
[][pypi-link]
[][conda-link]
[][black-link]

Collection of core plugins for markdown-it-py.

</details>

### jsonschema-path

JSONSchema Spec with object-oriented paths

`pip install jsonschema-path` · installs (wheel) · licence: Apache Software License · rank 349 · last release 2026-05-19 · [PyPI](https://pypi.org/project/jsonschema-path/) · [source](https://github.com/p1c2u/jsonschema-path)

<details><summary>README extract</summary>

Object-oriented JSONSchema

Features:
* Traverse schema like paths
* Access schema on demand with separate dereferencing accessor layer

Example:
```python
>>> from jsonschema_path import SchemaPath

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

Sections: JSONSchema Path, About, Key features, Usage, Identity and equality, Resolved cache, Benchmarks, Related projects

</details>

### mccabe

McCabe checker, plugin for flake8

`pip install mccabe` · installs (wheel) · licence: MIT License · rank 351 · last release 2022-01-24 · [PyPI](https://pypi.org/project/mccabe/)

<details><summary>README extract</summary>

Ned's script to check McCabe complexity.

This module provides a plugin for `flake8`, the Python code checker.

Sections: McCabe complexity checker, Standalone script, Plugin for Flake8, Links, Changes, 0.7.0 - 2021-01-23, 0.6.1 - 2017-01-26, 0.6.0 - 2017-01-23, 0.5.3 - 2016-12-14, 0.5.2 - 2016-07-31, 0.5.1 - 2016-07-28, 0.5.0 - 2016-05-30, 0.4.0 - 2016-01-27, 0.3.1 - 2015-06-14

</details>

### Faker

Faker is a Python package that generates fake data for you.

`pip install Faker` · installs (wheel) · licence: MIT License · rank 353 · last release 2026-10-28 · [PyPI](https://pypi.org/project/Faker/) · [docs](http://faker.rtfd.org/) · [source](https://github.com/joke2k/faker)

<details><summary>README extract</summary>

*Faker* is a Python package that generates fake data for you. Whether
you need to bootstrap your database, create good-looking XML documents,
fill-in your persistence to stress test it, or anonymize data taken from
a production service, Faker is for you.

Faker is heavily inspired by PHP Faker, Perl Faker, and by Ruby Faker.

Example:
```python
from faker import Faker
fake = Faker()

fake.name()
# 'Lucy Cechtelar'

fake.address()
# '426 Jordy Lodge
# Cartwrightshire, SC 88120-6700'

fake.text()
# 'Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi
# beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt
...
```

...

</details>

### semver

Python helper for Semantic Versioning (https://semver.org)

`pip install semver` · installs (wheel) · licence: BSD License · rank 354 · last release 2026-09-12 · [PyPI](https://pypi.org/project/semver/) · [docs](https://python-semver.rtfd.io)

### bleach

An easy safelist-based HTML-sanitizing tool.

`pip install bleach` · installs (wheel) · licence: Apache Software License · rank 361 · last release 2026-06-05 · [PyPI](https://pypi.org/project/bleach/)

<details><summary>README extract</summary>

**NOTE: 2026-06-05: Bleach is no longer maintained. There will be no future
releases including for security issues.**
See issue: _

Bleach is an allowed-list-based HTML sanitizing library that escapes or strips
markup and attributes. ...

Example:
```python
>>> import bleach

>>> bleach.clean('an evil() example')
u'an <script>evil()</script> example'

>>> bleach.linkify('an  url')
u'an  url'
```

Sections: Bleach, Reporting Bugs, Upgrading Bleach, Basic use, Bleach changes, Version 6.4.0 (June 5th, 2026), Version 6.3.0 (October 27th, 2025), Version 6.2.0 (October 29th, 2024), Version 6.1.0 (October 6th, 2023), Version 6.0.0 (January 23rd, 2023), Version 5.0.1 (June 27th, 2022), Version 5.0.0 (April 7th, 2022), Version 4.1.0 (August 25th, 2021), Version 4.0.0 (August 3rd, 2021)

</details>

### deprecation

A library to handle automated deprecations

`pip install deprecation` · installs (wheel) · licence: Apache Software License · rank 364 · last release 2020-04-20 · [PyPI](https://pypi.org/project/deprecation/) · [docs](http://deprecation.readthedocs.io/en/latest/) · [source](https://github.com/briancurtin/deprecation)

<details><summary>README extract</summary>

The `deprecation` library provides a `deprecated` decorator and a
`fail_if_not_removed` decorator for your tests. Together, the two
enable the automation of several things:

1. The docstring of a deprecated method gets the deprecation details
 appended to the end of it. ...

Example:
```python
import deprecation

@deprecation.deprecated(deprecated_in="1.0", removed_in="2.0",
                        current_version=version,
                        details="Use the bar function instead")
def foo():
    """Do some stuff"""
    return 1
```

Sections: deprecation, Usage, ...but doesn't Python ignore `DeprecationWarning`?

</details>

### linkify-it-py

Links recognition library with FULL unicode support.

`pip install linkify-it-py` · installs (wheel) · licence: MIT License · rank 365 · last release 2026-08-29 · [PyPI](https://pypi.org/project/linkify-it-py/)

<details><summary>README extract</summary>

This is Python port of linkify-it.

> Links recognition library with FULL unicode support.
> Focused on high quality link patterns detection in plain text.

Demo

Javascript Demo

Why it's awesome:

- Full unicode support, _with astral characters!
- International domains support.
- Allows rules extension & custom normalizers.

Example:
```python
from linkify_it import LinkifyIt

linkify = LinkifyIt()

print(linkify.test("Site github.com!"))
# => True

print(linkify.match("Site github.com!"))
# => [linkify_it.main.Match({
# 'schema': '',
# 'index': 5,
# 'last_index': 15,
# 'raw': 'github.com',
# 'text': 'github.com',
# 'url': '
# }]
```

...

</details>

### aiosqlite

asyncio bridge to the standard sqlite3 module

`pip install aiosqlite` · installs (wheel) · licence: MIT License · rank 368 · last release 2025-12-23 · [PyPI](https://pypi.org/project/aiosqlite/) · [docs](https://aiosqlite.omnilib.dev) · [source](https://github.com/omnilib/aiosqlite)

<details><summary>README extract</summary>

aiosqlite provides a friendly, async interface to sqlite databases.

It replicates the standard `sqlite3` module, but with async versions
of all the standard connection and cursor methods, plus context managers for
automatically closing connections and cursors:

It can also be used in the traditional, procedural manner: ...

Example:
```python
async with aiosqlite.connect(...) as db:
    await db.execute("INSERT INTO some_table ...")
    await db.commit()

    async with db.execute("SELECT * FROM some_table") as cursor:
        async for row in cursor:
            ...
```

Sections: aiosqlite\: Sqlite for AsyncIO, Details

</details>

### arrow

Better dates & times for Python

`pip install arrow` · installs (wheel) · licence: Apache Software License · rank 370 · last release 2025-10-18 · [PyPI](https://pypi.org/project/arrow/) · [docs](https://arrow.readthedocs.io) · [source](https://github.com/arrow-py/arrow)

<details><summary>README extract</summary>

Arrow is a Python library that offers a sensible and human-friendly approach to creating, manipulating, formatting and converting dates, times and timestamps. It implements and updates the datetime type, plugging gaps in functionality and providing an intelligent module API that supports many common creation scenarios. ...

Features:
Python's standard library and some other low-level modules have near-complete date, time and timezone functionality, but don't work very well from a usability perspective:

- Too many modules: datetime, time, calendar, dateutil, pytz and more ...

Example:
```python
>>> import arrow
>>> arrow.get('2013-05-11T21:23:58.970460+07:00')
<Arrow [2013-05-11T21:23:58.970460+07:00]>

>>> utc = arrow.utcnow()
>>> utc
<Arrow [2013-05-11T21:23:58.970460+00:00]>

...

</details>

### ruamel.yaml.clib

C version of reader, parser and emitter for ruamel.yaml derived from libyaml

`pip install ruamel.yaml.clib` · installs (wheel) · licence: MIT License · rank 376 · last release 2025-11-16 · [PyPI](https://pypi.org/project/ruamel.yaml.clib/) · [docs](https://yaml.dev/doc/ruamel.yaml.clib/) · [source](https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/)

<details><summary>README extract</summary>

`ruamel.yaml.clib` is the C based reader/scanner and emitter for ruamel.yaml

 version
 0.2.15

 updated
 2025-11-16

 documentation

 repository

 pypi

This package was split of from ruamel.yaml, so that ruamel.yaml can be
build as a universal wheel. ...

</details>

### py4j

Enables Python programs to dynamically access arbitrary Java objects

`pip install py4j` · installs (wheel) · licence: BSD License · rank 378 · last release 2025-01-15 · [PyPI](https://pypi.org/project/py4j/)

<details><summary>README extract</summary>

Py4J enables Python programs running in a Python interpreter to dynamically access Java objects in a Java Virtual Machine. Methods are called as if the Java objects resided in the Python interpreter and Java collections can be accessed through standard Python collection methods. Py4J also enables Java programs to call back Python objects.

</details>

### mmh3

Python extension for MurmurHash (MurmurHash3), a set of fast and robust hash functions.

`pip install mmh3` · installs (wheel) · licence: MIT License · rank 379 · last release 2026-09-30 · [PyPI](https://pypi.org/project/mmh3/) · [docs](https://mmh3.readthedocs.io/) · [source](https://github.com/hajimes/mmh3)

<details><summary>README extract</summary>

`mmh3` is a Python extension for
MurmurHash (MurmurHash3), a set of
fast and robust non-cryptographic hash functions invented by Austin Appleby.

By combining `mmh3` with probabilistic techniques like
Bloom filter,
MinHash, and
feature hashing, you can
develop high-performance systems in fields such as data mining, machine
learning, and natural ...

Example:
```python
>>> import mmh3
>>> mmh3.hash(b"foo")  # returns a 32-bit signed int
-156908512
>>> mmh3.hash("foo")  # accepts str (UTF-8 encoded)
-156908512
>>> mmh3.hash(b"foo", 42)  # uses 42 as the seed
-1322301282
>>> mmh3.hash(b"foo", 0, False)  # returns a 32-bit unsigned int
4138058784
```

...

</details>

### pycodestyle

Python style guide checker

`pip install pycodestyle` · installs (wheel) · licence: MIT · rank 395 · last release 2026-09-22 · [PyPI](https://pypi.org/project/pycodestyle/)

<details><summary>README extract</summary>

pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8.

Features:
* Plugin architecture: Adding new checks is easy.

* Parseable output: Jump to error location in your editor.

* Small: Just one Python file, requires only stdlib. You can use just
 the `pycodestyle.py` file for this purpose. ...

Example:
```python
$ pycodestyle --show-source --show-pep8 testing/data/E40.py
testing/data/E40.py:2:10: E401 multiple imports on one line
import os, sys
         ^
    Imports should usually be on separate lines.

    Okay: import os\nimport sys
    E401: import sys, os
```

Sections: Features, Example usage and output, Links

</details>

### aiofile

Asynchronous file operations.

`pip install aiofile` · installs (wheel) · licence: Apache-2.0 · rank 404 · last release 2026-08-04 · [PyPI](https://pypi.org/project/aiofile/)

<details><summary>README extract</summary>

Real asynchronous file operations with asyncio support.

Features:
* Since version 2.0.0, uses caio, which provides multiple
 async I/O backends:
 * Linux io_uring — the modern, high-performance Linux kernel AIO interface.
 * Linux libaio — the classic kernel AIO mechanism via libaio. ...

Example:
```python
import asyncio
from pathlib import Path
from tempfile import gettempdir

from aiofile import async_open

tmp_filename = Path(gettempdir()) / "hello.txt"

async def main():
    async with async_open(tmp_filename, 'w+') as afp:
        await afp.write("Hello ")
        await afp.write("world")
        afp.seek(0)

        print(await afp.read())

...
```

...

</details>

### botocore-stubs

Type annotations and code completion for botocore

`pip install botocore-stubs` · installs (wheel) · licence: MIT · rank 420 · last release 2026-11-06 · [PyPI](https://pypi.org/project/botocore-stubs/) · [docs](https://youtype.github.io/mypy_boto3_builder/) · [source](https://github.com/youtype/botocore-stubs)

### bracex

Bash style brace expander.

`pip install bracex` · installs (wheel) · licence: MIT · rank 429 · last release 2026-11-07 · [PyPI](https://pypi.org/project/bracex/)

<details><summary>README extract</summary>

[][donate-link]
[][codecov-link]
[][pypi-link]
[][pypi-link]
[][license-link]

Bracex is a brace expanding library (à la Bash) for Python. Brace expanding is used to generate arbitrary strings.

Bracex adds this ability to Python:

and as a command:

- Why Bracex over other solutions? ...

Example:
```python
>>> bracex.expand(r'file-{{a,b},c}d.txt')
['file-ad.txt', 'file-bd.txt', 'file-cd.txt']
```

Sections: Bracex, Documentation

</details>

### types-s3transfer

Type annotations and code completion for s3transfer

`pip install types-s3transfer` · installs (wheel) · licence: MIT · rank 433 · last release 2026-10-20 · [PyPI](https://pypi.org/project/types-s3transfer/) · [docs](https://youtype.github.io/mypy_boto3_builder/) · [source](https://github.com/youtype/types-s3transfer)

<details><summary>README extract</summary>

Type annotations and code completion for s3transfer package.
This package is a part of mypy_boto3_builder project.

- types-s3transfer
 - Installation
 - Usage
 - Versioning
 - Support and contributing

Sections: types-s3transfer, Usage, Versioning

</details>

### wcmatch

Wildcard/glob file name matcher.

`pip install wcmatch` · installs (wheel) · licence: MIT · rank 439 · last release 2026-11-07 · [PyPI](https://pypi.org/project/wcmatch/)

<details><summary>README extract</summary>

[][donate-link]
[][codecov-link]
[][pypi-link]
[][pypi-link]
[][pypi-link]
[][license-link]

> [!warning]
> Security Considerations
> Wildcard Match translates the more simple, path-centric syntax of glob patterns to regular expression for the purpose
> of iterating and matching file systems. ...

Features:
Wildcard Match translates the more simple, path-centric syntax of glob patterns to regular expression for the purpose of
iterating and matching file systems. ...

Sections: Wildcard Match, Overview, Features, Documentation

</details>

### pkginfo

Query metadata from sdists / bdists / installed packages

`pip install pkginfo` · installs (wheel) · licence: not stated · rank 443 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pkginfo/) · [docs](https://tseaver.github.io/pkginfo) · [source](https://github.com/tseaver/pkginfo)

<details><summary>README extract</summary>

This package provides an API for querying the distutils metadata written in
the `PKG-INFO` file inside a source distribution (an `sdist`) or a
binary distribution (e.g., created by running `bdist_egg`). ...

</details>

### billiard

Python multiprocessing fork with improvements and bugfixes

`pip install billiard` · installs (wheel) · licence: BSD License · rank 450 · last release 2026-11-02 · [PyPI](https://pypi.org/project/billiard/)

<details><summary>README extract</summary>

:Version: 4.3.2
:Web:
:Download:
:Source:
:DeepWiki:

`billiard` is a fork of the Python 2.7 multiprocessing
package. The multiprocessing package itself is a renamed and updated version of
R Oudkerk's pyprocessing package.
This standalone variant draws its fixes/improvements from python-trunk and provides
additional bug fixes and improvements. ...

Sections: billiard, About, Documentation, Bug reporting, billiard is part of the Tidelift Subscription

</details>

### semantic-version

A library implementing the 'SemVer' scheme.

`pip install semantic-version` · installs (wheel) · licence: BSD License · rank 456 · last release 2022-05-26 · [PyPI](https://pypi.org/project/semantic-version/)

<details><summary>README extract</summary>

This small python library provides a few tools to handle SemVer in Python.
It follows strictly the 2.0.0 version of the SemVer scheme.

- Semantic Version specification: SemVer

Example:
```python
import semantic_version
```

Sections: Introduction, Links, Getting started, Versions, Working with versions, Requirement specification, The `SimpleSpec` scheme, Using a specification

</details>

### pyright

Command line wrapper for pyright

`pip install pyright` · installs (wheel) · licence: MIT · rank 458 · last release 2026-09-10 · [PyPI](https://pypi.org/project/pyright/) · [source](https://github.com/RobertCraigie/pyright-python)

<details><summary>README extract</summary>

> This project is not affiliated with Microsoft in any way, shape, or form

Pyright for Python is a Python command-line wrapper over pyright, a static type checker for Python.

Sections: Pyright for Python, Usage, Pre-commit, Motivation, How Pyright for Python Works, Automatically keeping pyright up to date, Configuration, Debugging, Modify Pyright Version, Keeping Pyright and Pylance in sync, Show NPM logs, Modify NPM Package Location, Force Node Env, Modify Node Env Location

</details>

### ty

An extremely fast Python type checker, written in Rust.

`pip install ty` · installs (wheel) · licence: MIT License · rank 462 · last release 2026-11-06 · [PyPI](https://pypi.org/project/ty/) · [source](https://github.com/astral-sh/ty)

<details><summary>README extract</summary>

An extremely fast Python type checker and language server, written in Rust.

 Type checking the home-assistant project without caching.

ty is backed by Astral, the creators of
uv and Ruff.

ty is currently in beta.

Features:
- 10x - 100x faster than mypy and Pyright
- Comprehensive diagnostics with rich contextual information
- Configurable rule levels, per-file overrides, suppression comments, and first-class project support ...

Sections: ty, Highlights, Getting started, Getting help, Version policy, FAQ, Why is ty doing \_\_\_\_\_?, How do you pronounce ty?, How should I stylize ty?

</details>

### rich-toolkit

Rich toolkit for building command-line applications

`pip install rich-toolkit` · installs (wheel) · licence: MIT · rank 464 · last release 2026-10-08 · [PyPI](https://pypi.org/project/rich-toolkit/)

<details><summary>README extract</summary>

This is a very opinionated set of components for building CLI applications.
It is based on Rich

Sections: Rich Toolkit, Example usage, Output encoding, Running tests with an encoding

</details>

### absl-py

Abseil Python Common Libraries, see https://github.com/abseil/abseil-py.

`pip install absl-py` · installs (wheel) · licence: Apache-2.0 · rank 468 · last release 2026-10-09 · [PyPI](https://pypi.org/project/absl-py/) · [docs](https://abseil.io/docs/python/) · [source](https://github.com/abseil/abseil-py)

<details><summary>README extract</summary>

This repository is a collection of Python library code for building Python
applications. The code is collected from Google's own Python code base, and has
been extensively tested and used in production.

Features:
* Simple application startup
* Distributed commandline flags system
* Custom logging module with additional features
* Testing utilities

Sections: Abseil Python Common Libraries, Features, Getting Started, Running Tests, Example Code, Documentation

</details>

### simplejson

Simple, fast, extensible JSON encoder/decoder for Python

`pip install simplejson` · installs (wheel) · licence: MIT OR AFL-2.1 · rank 469 · last release 2026-10-03 · [PyPI](https://pypi.org/project/simplejson/)

<details><summary>README extract</summary>

simplejson

simplejson is a simple, fast, complete, correct and extensible
JSON < encoder and decoder for Python 3.9+
with legacy support for Python 2.7. It is pure Python code
with no dependencies, but includes an optional C extension
for a serious speed boost.

The latest documentation for simplejson can be read online here: ...

</details>

### stripe

Python bindings for the Stripe API

`pip install stripe` · installs (wheel) · licence: MIT License · rank 470 · last release 2026-10-29 · [PyPI](https://pypi.org/project/stripe/) · [docs](https://stripe.com/docs/api/?lang=python) · [source](https://github.com/stripe/stripe-python)

<details><summary>README extract</summary>

> [!TIP]
> Want to chat live with Stripe engineers? Join us on our Discord server.

The Stripe Python library provides convenient access to the Stripe API from
applications written in the Python language. ...

Example:
```python
from stripe import StripeClient

client = StripeClient("sk_test...")

# list customers
customers = client.v1.customers.list()

# print the first customer's email
print(customers.data[0].email)

# retrieve specific Customer
customer = client.v1.customers.retrieve("cus_123456789")

# print that customer's email
print(customer.email)
```

...

</details>

### portalocker

Cross-platform file locking, with Redis, PID-file and bounded-semaphore locks

`pip install portalocker` · installs (wheel) · licence: BSD-3-Clause · rank 478 · last release 2026-10-28 · [PyPI](https://pypi.org/project/portalocker/) · [docs](https://portalocker.readthedocs.io/en/latest/) · [source](https://github.com/wolph/portalocker/)

<details><summary>README extract</summary>

Portalocker provides file locks for Python on Linux, macOS and Windows.
Use a context manager to coordinate access between processes, a semaphore to
limit concurrent workers, or a Redis lock to coordinate across machines.
Python 3.10 or later is required.

Get started |
Choose a lock |
API reference |
Changelog

Example:
```python
import portalocker

with portalocker.Lock('report.txt', 'a', timeout=5) as fh:
    fh.write('Report complete.\n')
```

Sections: Coordinate access. Keep your code simple., Start with a file lock, Choose a lock, Locking details that matter

</details>

### ijson

Iterative JSON parser with standard Python iterator interfaces

`pip install ijson` · installs (wheel) · licence: BSD-3-Clause AND ISC · rank 491 · last release 2026-10-12 · [PyPI](https://pypi.org/project/ijson/)

<details><summary>README extract</summary>

Ijson is an iterative JSON parser with standard Python iterator interfaces.

Features:
Apart from their performance,
all backends are designed to support the same capabilities.
There are however some small known differences,
all of which can be queried by inspecting
the `capabilities` module constant. ...

Example:
```python
import ijson

f = urlopen('
objects = ijson.items(f, 'earth.europe.item')
cities = (o for o in objects if o['type'] == 'city')
for city in cities:
    do_something_with(city)
```

Sections: ijson, Usage, High-level interfaces, Lower-level interfaces, Command line, Benchmarking, Intercepting events, Push interfaces, Options, Events, Prefix, Backends, Capabilities, Performance tips

</details>

### flask-cors

A Flask extension simplifying CORS support

`pip install flask-cors` · installs (wheel) · licence: MIT · rank 492 · last release 2026-06-08 · [PyPI](https://pypi.org/project/flask-cors/) · [docs](https://corydolphin.github.io/flask-cors/) · [source](https://github.com/corydolphin/flask-cors)

<details><summary>README extract</summary>

A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.

This package has a simple philosophy: when you want to enable CORS, you wish to enable it for all use cases on a domain.
This means no mucking around with different allowed headers, methods, etc. ...

Example:
```python
from flask import Flask
from flask_cors import CORS

app = Flask(name)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"
```

Sections: Flask-CORS, Usage, Simple Usage, Resource specific CORS, Route specific CORS via decorator, Documentation, Troubleshooting

</details>

### isoduration

Operations with ISO 8601 durations

`pip install isoduration` · installs (wheel) · licence: ISC License (ISCL) · rank 493 · last release 2020-11-01 · [PyPI](https://pypi.org/project/isoduration/) · [source](https://github.com/bolsote/isoduration)

<details><summary>README extract</summary>

ISO 8601 is most commonly known as a way to exchange datetimes in textual format. A
lesser known aspect of the standard is the representation of durations. They have a
shape similar to this:

This string represents a duration of 3 years, 6 months, 4 days, 12 hours, 30 minutes,
and 5 seconds. ...

Features:
`timedelta` cannot represent certain durations, such as those involving years or months.
Since it cannot represent all possible durations without dangerous arithmetic, then it
must not be the right type.

Example:
```python
>>> from isoduration import parse_duration
>>> duration = parse_duration("P3Y6M4DT12H30M5S")
>>> duration.date
DateDuration(years=Decimal('3'), months=Decimal('6'), days=Decimal('4'), weeks=Decimal('0'))
>>> duration.time
...

</details>

### confluent-kafka

Confluent's Python client for Apache Kafka

`pip install confluent-kafka` · installs (wheel) · licence: Apache Software License · rank 494 · last release 2026-10-28 · [PyPI](https://pypi.org/project/confluent-kafka/)

<details><summary>README extract</summary>

confluent-kafka-python provides a high-level `Producer`, `Consumer` and `AdminClient` compatible with all Apache Kafka brokers >= v0.8, Confluent Cloud and Confluent Platform.

Recommended for Production: While this client works with any Kafka deployment, it's optimized for and fully supported with Confluent Cloud (fully managed) and Confluent ...

Features:
Unlike the basic Apache Kafka Python client, `confluent-kafka-python` provides:

- Production-Ready Performance: Built on `librdkafka` (C library) for maximum throughput and minimal latency, significantly outperforming pure Python implementations. ...

Example:
```python
from confluent_kafka import Producer
from confluent_kafka.schema_registry import SchemaRegistryClient
...

</details>

### py

library with cross-python path, ini-parsing, io, code, log facilities

`pip install py` · installs (wheel) · licence: MIT License · rank 495 · last release 2021-11-04 · [PyPI](https://pypi.org/project/py/)

<details><summary>README extract</summary>

NOTE: this library is in maintenance mode and should not be used in new code.

The py lib is a Python development support library featuring
the following tools and modules:

* `py.path`: uniform local and svn path objects -> please use pathlib/pathlib2 instead
* `py.apipkg`: explicit API control and lazy-importing -> please use the standalone ...

</details>

### thrift

Python bindings for the Apache Thrift RPC system

`pip install thrift` · installs (wheel) · licence: Apache License 2.0 · rank 501 · last release 2026-09-30 · [PyPI](https://pypi.org/project/thrift/)

<details><summary>README extract</summary>

Thrift Python Software Library

Sections: Using Thrift with Python, Breaking Changes

</details>

### bytecode

Python module to generate and modify bytecode

`pip install bytecode` · installs (wheel) · licence: MIT License · rank 502 · last release 2026-10-07 · [PyPI](https://pypi.org/project/bytecode/) · [docs](https://bytecode.readthedocs.io/en/latest/) · [source](https://github.com/MatthieuDartiailh/bytecode)

<details><summary>README extract</summary>

`bytecode` is a Python module to generate and modify bytecode.

* bytecode project homepage at GitHub (code, bugs)
* bytecode documentation
* Download latest bytecode release at the Python Cheeseshop (PyPI)

Install bytecode: `python3 -m pip install bytecode`. It requires Python 3.8
or newer. ...

Example:
```python
from bytecode import Instr, Bytecode

bytecode = Bytecode([Instr("LOAD_GLOBAL", (True, 'print')),
                     Instr("LOAD_CONST", 'Hello World!'),
                     Instr("CALL", 1),
                     Instr("POP_TOP"),
                     Instr("LOAD_CONST", None),
                     Instr("RETURN_VALUE")])
...
```

</details>

### uri-template

RFC 6570 URI Template Processor

`pip install uri-template` · installs (wheel) · licence: MIT License · rank 507 · last release 2023-06-21 · [PyPI](https://pypi.org/project/uri-template/)

<details><summary>README extract</summary>

An implementation of RFC 6570 URI Templates.

This packages implements URI Template expansion in strict adherence to RFC 6570,
but adds a few extensions.

RFC 6570 is silent regarding variable values that are not strings, lists, associative arrays, or null.

This package handles value types as follows: ...

Sections: uri-template, RFC 6570 Extensions, Non-string Values, Nested Structures, Default Values, Specifying Value Keys, Partial expansion, Comma Expansion: {,var}, Reserved Comma Expansion: {,+var}, API, uri_template.validate(template: str) -> bool: ..., uri_template.URITemplate, URITemplate(template: str), URITemplate.variables: Iterable[Variable]

</details>

### packageurl-python

A purl aka. Package URL parser and builder

`pip install packageurl-python` · installs (wheel) · licence: MIT License · rank 509 · last release 2025-11-24 · [PyPI](https://pypi.org/project/packageurl-python/)

<details><summary>README extract</summary>

Python library to parse and build "purl" aka. Package URLs.
See for details.

Join the discussion at or enter a ticket for support.

License: MIT

Example:
```python
>>> from packageurl import PackageURL

>>> purl = PackageURL.from_string("pkg:maven/org.apache.commons/io@1.3.4")
>>> print(purl.to_dict())
{'type': 'maven', 'namespace': 'org.apache.commons', 'name': 'io', 'version': '1.3.4', 'qualifiers': None, 'subpath': None}

>>> print(purl.to_string())
pkg:maven/org.apache.commons/io@1.3.4

...
```

Sections: packageurl-python, Usage, Utilities, Django models, SQLAlchemy mixin, URL to PURL, PURL to URL, Run tests

</details>

### flake8

the modular source code checker: pep8 pyflakes and co

`pip install flake8` · installs (wheel) · licence: MIT · rank 514 · last release 2026-10-28 · [PyPI](https://pypi.org/project/flake8/)

<details><summary>README extract</summary>

Flake8 is a wrapper around these tools:

- PyFlakes
- pycodestyle
- Ned Batchelder's McCabe script

Flake8 runs all the tools by launching the single `flake8` command.
It displays the warnings in a per-file, merged output.

It also adds a few features:

- lines that contain a `# noqa` comment at the end will not issue warnings. ...

Sections: Flake8, Quickstart, Frequently Asked Questions, Questions or Feedback, Links, Maintenance

</details>

### astroid

An abstract syntax tree for Python with inference support.

`pip install astroid` · installs (wheel) · licence: LGPL-2.1-or-later · rank 522 · last release 2026-10-08 · [PyPI](https://pypi.org/project/astroid/) · [docs](https://pylint.readthedocs.io/projects/astroid/en/latest/) · [source](https://github.com/pylint-dev/astroid)

_README extract left out: share-alike licence._

### fakeredis

Python implementation of redis API, can be used for testing purposes.

`pip install fakeredis` · installs (wheel) · licence: BSD-3-Clause · rank 524 · last release 2026-10-14 · [PyPI](https://pypi.org/project/fakeredis/) · [docs](https://fakeredis.moransoftware.ca/) · [source](https://github.com/cunla/fakeredis-py)

<details><summary>README extract</summary>

Example:
```python
import fakeredis

r = fakeredis.FakeStrictRedis()
r.lpush("queue", "a", "b", "c")
r.lrange("queue", 0, -1)  # [b'c', b'b', b'a']
```

Sections: ✨ Why fakeredis?, 🚀 Quickstart, Using it in tests (pytest), 🌐 TCP server mode

</details>

### limits

Rate limiting utilities

`pip install limits` · installs (wheel) · licence: MIT · rank 532 · last release 2026-02-05 · [PyPI](https://pypi.org/project/limits/) · [docs](https://limits.readthedocs.org) · [source](https://github.com/alisaifee/limits)

<details><summary>README extract</summary>

limits is a python library for rate limiting via multiple strategies
with commonly used storage backends (Redis, Memcached & MongoDB).

The library provides identical APIs for use in sync and
async codebases.

Example:
```python
weighted_count = current_count + floor(previous_count * weight)
```

Sections: limits, Fixed Window, Moving Window, Sliding Window Counter, Storage backends, Dive right in, Links

</details>

### nh3

Python binding to Ammonia HTML sanitizer Rust crate

`pip install nh3` · installs (wheel) · licence: MIT · rank 535 · last release 2026-08-23 · [PyPI](https://pypi.org/project/nh3/) · [source](https://github.com/messense/nh3)

<details><summary>README extract</summary>

Python bindings to the ammonia HTML sanitization library.

Example:
```python
Python 3.11.0 (main, Oct 25 2022, 16:25:24) [Clang 14.0.0 (clang-1400.0.29.102)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.9.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import requests

In [2]: import bleach

In [3]: import nh3

In [4]: html = requests.get("

In [5]: %timeit bleach.clean(html)
...
```

Sections: nh3, Usage, Performance

</details>

### libcst

A concrete syntax tree with AST-like properties for Python 3.0 through 3.15 programs.

`pip install libcst` · installs (wheel) · licence: MIT License · rank 546 · last release 2026-08-11 · [PyPI](https://pypi.org/project/libcst/) · [docs](https://libcst.readthedocs.io/en/latest/) · [source](https://github.com/Instagram/LibCST)

<details><summary>README extract</summary>

A Concrete Syntax Tree (CST) parser and serializer library for Python

LibCST parses Python 3.0 -> 3.15 source code as a CST tree that keeps
all formatting details (comments, whitespaces, parentheses, etc). It's useful for
building automated refactoring (codemod) applications and linters. ...

Example:
```python
BinaryOperation(
    left=Integer(
        value='1',
        lpar=[],
        rpar=[],
    ),
    operator=Add(
        whitespace_before=SimpleWhitespace(
            value=' ',
        ),
        whitespace_after=SimpleWhitespace(
            value=' ',
        ),
    ),
    right=Integer(
        value='2',
        lpar=[],
        rpar=[],
...
```

...

</details>

### olefile

Python package to parse, read and write Microsoft OLE2 files (Structured Storage or Compound Document, Microsoft Office)

`pip install olefile` · installs (wheel) · licence: BSD License · rank 559 · last release 2023-12-01 · [PyPI](https://pypi.org/project/olefile/)

<details><summary>README extract</summary>

olefile is a Python package to parse, read and write
Microsoft OLE2 files
(also called Structured Storage, Compound File Binary Format or Compound Document File Format),
such as Microsoft Office 97-2003 documents, vbaProject.bin in MS Office 2007+ files, Image Composer
and FlashPix files, Outlook messages, StickyNotes, several Microscopy file ...

Sections: olefile, Real-life examples

</details>

### fastar

High-level bindings for the Rust tar crate

`pip install fastar` · installs (wheel) · licence: MIT License · rank 565 · last release 2026-08-20 · [PyPI](https://pypi.org/project/fastar/) · [docs](https://github.com/DoctorJohn/fastar) · [source](https://github.com/DoctorJohn/fastar)

<details><summary>README extract</summary>

[][versions-url]
[][pypi-url]
[][downloads-url]
[][license-url]
[][codspeed-url]

The `fastar` library wraps the Rust tar, flate2, and zstd crates, providing a high-performance way to work with compressed and uncompressed tar archives in Python.

Example:
```python
import fastar
from pathlib import Path

input_file = Path("file.txt")
input_file.write_text("Hello, Fastar!")

with fastar.open("archive.tar", "w") as archive:
    archive.append(input_file)

with fastar.open("archive.tar", "r") as archive:
    archive.unpack("output/")

unpacked_file = Path("output/file.txt")
...
```

Sections: Fastar, Usage, Opening Modes

</details>

### msgspec

A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML.

`pip install msgspec` · installs (wheel) · licence: BSD-3-Clause · rank 567 · last release 2026-09-29 · [PyPI](https://pypi.org/project/msgspec/) · [source](https://github.com/msgspec/msgspec)

<details><summary>README extract</summary>

`msgspec` is a *fast* serialization and validation library, with builtin
support for JSON, MessagePack,
YAML, and TOML. It features:

- 🚀 High performance encoders/decoders for common protocols. The JSON and
 MessagePack implementations regularly
 benchmark as the fastest
 options for Python.

- 🎉 Support for a wide variety of Python types. ...

Example:
```python
>>> import msgspec

>>> class User(msgspec.Struct):
...     """A new type describing a User"""
...     name: str
...     groups: set[str] = set()
...     email: str | None = None
```

</details>

### testcontainers

Python library for throwaway instances of anything that can run in a Docker container

`pip install testcontainers` · installs (wheel) · licence: Apache-2.0 · rank 573 · last release 2026-07-24 · [PyPI](https://pypi.org/project/testcontainers/) · [source](https://github.com/testcontainers/testcontainers-python)

<details><summary>README extract</summary>

`testcontainers-python` facilitates the use of Docker containers for functional and integration testing.

For more information, see the docs.

Example:
```python
>>> from testcontainers.postgres import PostgresContainer
>>> import sqlalchemy

>>> with PostgresContainer("postgres:16") as postgres:
...     engine = sqlalchemy.create_engine(postgres.get_connection_url())
...     with engine.begin() as connection:
...         result = connection.execute(sqlalchemy.text("select version()"))
...
```

Sections: Testcontainers Python, Getting Started, Configuration

</details>

### types-awscrt

Type annotations and code completion for awscrt

`pip install types-awscrt` · installs (wheel) · licence: MIT · rank 578 · last release 2026-10-13 · [PyPI](https://pypi.org/project/types-awscrt/) · [docs](https://youtype.github.io/mypy_boto3_builder/) · [source](https://github.com/youtype/types-awscrt)

<details><summary>README extract</summary>

Type annotations and code completion for awscrt package.
This package is a part of mypy_boto3_builder project.

- types-awscrt
 - Installation
 - Usage
 - Versioning
 - Support and contributing

Sections: types-awscrt, Usage, Versioning

</details>

### pytest-split

Pytest plugin which splits the test suite to equally sized sub suites based on test execution time.

`pip install pytest-split` · installs (wheel) · licence: MIT License · rank 580 · last release 2026-02-03 · [PyPI](https://pypi.org/project/pytest-split/) · [docs](https://jerry-git.github.io/pytest-split) · [source](https://github.com/jerry-git/pytest-split)

<details><summary>README extract</summary>

Documentation:

Source Code:

PyPI:

Pytest plugin which splits the test suite to equally sized "sub suites" based on test execution time.

* Splitting the test suite is a prerequisite for parallelization (who does not want faster CI builds?). It's valuable to have sub suites which execution time is around the same. ...

Sections: pytest-split, Motivation, Usage, CLI commands, slowest-tests, Interactions with other pytest plugins, Splitting algorithms, Documentation, Releasing, Pre-commit

</details>

### tinyhtml5

HTML parser based on the WHATWG HTML specification

`pip install tinyhtml5` · installs (wheel) · licence: MIT License · rank 587 · last release 2026-03-05 · [PyPI](https://pypi.org/project/tinyhtml5/) · [docs](https://doc.courtbouillon.org/tinyhtml5/) · [source](https://github.com/CourtBouillon/tinyhtml5)

<details><summary>README extract</summary>

A tiny HTML5 parser

tinyhtml5 is a HTML5 parser that transforms a possibly malformed HTML document
into an ElementTree tree.

This module is a simplified fork of html5lib, written and maintained by James
Graham, Sam Sneddon, Łukasz Langa and Will Kahn-Greene.

* Free software: MIT license
* For Python 3.10+, tested on CPython and PyPy ...

</details>

### uc-micro-py

Micro subset of unicode data files for linkify-it-py projects.

`pip install uc-micro-py` · installs (wheel) · licence: MIT License · rank 627 · last release 2026-03-01 · [PyPI](https://pypi.org/project/uc-micro-py/)

<details><summary>README extract</summary>

This is a Python port of uc.micro.

> Micro subset of unicode data files for linkify-it-py projects.

This package content is ONLY for linkify-it-pyprojects needs.

</details>

### selenium

Official Python bindings for Selenium WebDriver

`pip install selenium` · installs (wheel) · licence: Apache-2.0 · rank 634 · last release 2026-10-29 · [PyPI](https://pypi.org/project/selenium/)

<details><summary>README extract</summary>

Python language bindings for Selenium WebDriver.

The `selenium` package is used to automate web browser interaction from Python.

+-------------------+--------------------------------------------------------+
| Home: | |
+-------------------+--------------------------------------------------------+
| GitHub: | ...

Example:
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("
driver.quit()
```

Sections: Selenium Client Driver, Introduction, Drivers, Example 0, Example 1, Example 2, Example 3, Selenium Grid (optional), Use The Source Luke!

</details>

### click-option-group

Option groups missing in Click

`pip install click-option-group` · installs (wheel) · licence: BSD-3-Clause · rank 644 · last release 2025-10-09 · [PyPI](https://pypi.org/project/click-option-group/) · [docs](https://click-option-group.readthedocs.io) · [source](https://github.com/click-contrib/click-option-group)

<details><summary>README extract</summary>

click-option-group is a Click-extension package that adds option groups
missing in Click.

Click is a package for creating powerful and beautiful command line interfaces (CLI) in Python,
but it has no the functionality for creating option groups. ...

Example:
```python
# app.py

import click
from click_option_group import optgroup, RequiredMutuallyExclusiveOptionGroup

@click.command()
@optgroup.group('Server configuration',
                help='The configuration of some server connection')
@optgroup.option('-h', '--host', default='localhost', help='Server host name')
...
```

Sections: click-option-group, Aim and Motivation, Quickstart, A Simple Example, Documentation

</details>

### unidiff

Unified diff parsing/metadata extraction library.

`pip install unidiff` · installs (wheel) · licence: MIT License · rank 650 · last release 2026-09-15 · [PyPI](https://pypi.org/project/unidiff/) · [source](https://github.com/matiasb/python-unidiff)

<details><summary>README extract</summary>

Simple Python library to parse and interact with unified diff data.

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

Sections: Unidiff, Quick start, Load a local diff file, Inspecting files, hunks and lines, Git file modes, symlinks, submodules and line numbers, Parsing from bytes, Diffs with embedded carriage returns or control characters, References

</details>

### graphql-relay

Relay library for graphql-core

`pip install graphql-relay` · installs (wheel) · licence: MIT License · rank 658 · last release 2022-04-16 · [PyPI](https://pypi.org/project/graphql-relay/)

<details><summary>README extract</summary>

GraphQL-relay-py is the Relay library for
GraphQL-core.

It allows the easy creation of Relay-compliant servers using GraphQL-core.

GraphQL-Relay-Py is a Python port of
graphql-relay-js,
while GraphQL-Core is a Python port of
GraphQL.js,
the reference implementation of GraphQL for JavaScript. ...

Example:
```python
from graphql_relay import connection_definitions
```

Sections: Relay Library for GraphQL Python, Getting Started, Using Relay Library for GraphQL Python (graphql-core), Connections, Object Identification, Mutations

</details>

### sentencepiece

Unsupervised text tokenizer and detokenizer.

`pip install sentencepiece` · installs (wheel) · licence: Apache-2.0 · rank 659 · last release 2026-11-05 · [PyPI](https://pypi.org/project/sentencepiece/)

<details><summary>README extract</summary>

Python wrapper for SentencePiece. This API supports the encoding, decoding, and training of SentencePiece models.

For a detailed feature and API comparison with Hugging Face Tokenizers and OpenAI's tiktoken, see the Tokenizer Comparison Cheat Sheet.

Features:
* Zero-Copy Encoding: When you pass `bytes` to the encoder (e.g., read directly via `open(..., 'rb')`), the wrapper extracts the memory pointer zero-copy to construct `std::string_view` directly. ...

Example:
```python
import sentencepiece as spm

sp = spm.SentencePieceProcessor(model_file="test.model")

# 1. Optimal Encoding: Read and pass raw bytes
with open("large_file.txt", "rb") as f:
  lines_bytes = f.read().splitlines()
ids = sp.encode(lines_bytes, return_type=int)

# 2. Optimal Decoding: Reconstruct directly to bytes
...
...

</details>

### appdirs

A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir".

`pip install appdirs` · installs (wheel) · licence: MIT License · rank 661 · last release 2020-05-11 · [PyPI](https://pypi.org/project/appdirs/)

<details><summary>README extract</summary>

What directory should your app use for storing user data? If running on Mac OS X, you
should use:
If on Windows (at least English Win XP) that should be:
or possibly:
for roaming profiles but that is another story.

On Linux (and other Unices) the dir, according to the XDG
spec, is:

Example:
```python
>>> from appdirs import *
>>> appname = "SuperApp"
>>> appauthor = "Acme"
>>> user_data_dir(appname, appauthor)
'/Users/trentm/Library/Application Support/SuperApp'
>>> site_data_dir(appname, appauthor)
'/Library/Application Support/SuperApp'
>>> user_cache_dir(appname, appauthor)
'/Users/trentm/Library/Caches/SuperApp'
...
```

...

</details>

### graphene

GraphQL Framework for Python

`pip install graphene` · installs (wheel) · licence: MIT · rank 662 · last release 2024-11-09 · [PyPI](https://pypi.org/project/graphene/)

<details><summary>README extract</summary>

���� Join the community on Discord

We are looking for contributors! Please check the current issues to see how you can help ������

Graphene is an opinionated Python library for building GraphQL schemas/types fast and easily.

- Easy to use: Graphene helps you use GraphQL in Python without effort.
- Relay: Graphene has builtin support for Relay. ...

Example:
```python
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(description='A typical hello world')

    def resolve_hello(self, info):
        return 'World'

schema = graphene.Schema(query=Query)
```

Sections: Graphene, Introduction, Integrations, Examples, Documentation, Building Documentation

</details>

### strictyaml

Strict, typed YAML parser

`pip install strictyaml` · installs (wheel) · licence: MIT License · rank 670 · last release 2023-03-10 · [PyPI](https://pypi.org/project/strictyaml/) · [docs](https://hitchdev.com/strictyaml/using) · [source](https://github.com/crdoconnor/strictyaml)

<details><summary>README extract</summary>

StrictYAML is a type-safe YAML parser
that parses and validates a restricted subset of the YAML
specification.

Priorities:

- Beautiful API
- Refusing to parse the ugly, hard to read and insecure features of YAML like the Norway problem.
- Strict validation of markup and straightforward type casting. ...

Features:
There are a number of formats and approaches that can achieve more or
less the same purpose as StrictYAML. I've tried to make it the best one.
Below is a series of documented justifications: ...

Example:
```python
from strictyaml import load, Map, Str, Int, Seq, YAMLError
```

Sections: StrictYAML, Why StrictYAML?, Using StrictYAML, Design justifications

</details>

### html5lib

HTML parser based on the WHATWG HTML specification

`pip install html5lib` · installs (wheel) · licence: MIT License · rank 671 · last release 2020-06-22 · [PyPI](https://pypi.org/project/html5lib/)

<details><summary>README extract</summary>

html5lib is a pure-python library for parsing HTML. It is designed to
conform to the WHATWG HTML specification, as is implemented by all major
web browsers.

Example:
```python
import html5lib
with open("mydocument.html", "rb") as f:
    document = html5lib.parse(f)
```

Sections: html5lib, Usage, Optional Dependencies, Bugs, Tests, Questions?, 1.1, 1.0.1, 1.0, 0.999999999/1.0b10, 0.99999999/1.0b9, 0.9999999/1.0b8, 0.999999/1.0b7, 0.99999/1.0b6

</details>

### boltons

When they're not builtins, they're boltons.

`pip install boltons` · installs (wheel) · licence: BSD License · rank 674 · last release 2026-09-07 · [PyPI](https://pypi.org/project/boltons/)

<details><summary>README extract</summary>

*boltons should be builtins.*

Boltons is a set of over 230 BSD-licensed, pure-Python utilities
in the same spirit as — and yet conspicuously missing from —
the standard library, including: ...

Sections: Boltons, Third-party packages, Gaps

</details>

### trio-websocket

WebSocket library for Trio

`pip install trio-websocket` · installs (wheel) · licence: MIT License · rank 676 · last release 2025-02-25 · [PyPI](https://pypi.org/project/trio-websocket/) · [source](https://github.com/python-trio/trio-websocket)

<details><summary>README extract</summary>

This library implements both server and client aspects of the the WebSocket
protocol, striving for safety,
correctness, and ergonomics. It is based on the wsproto
project, which is a
Sans-IO state machine that implements the
majority of the WebSocket protocol, including framing, codecs, and events. ...

Example:
```python
import trio
from sys import stderr
from trio_websocket import open_websocket_url

async def main():
    try:
        async with open_websocket_url('wss://echo.websocket.org') as ws:
            await ws.send_message('hello world!')
            message = await ws.get_message()
            print('Received message: %s' % message)
...
```

Sections: Trio WebSocket, Alternatives, Client Example, Server Example

</details>

### inflect

Correctly generate plurals, singular nouns, ordinals, indefinite articles

`pip install inflect` · installs (wheel) · licence: MIT · rank 686 · last release 2026-10-21 · [PyPI](https://pypi.org/project/inflect/) · [source](https://github.com/jaraco/inflect)

<details><summary>README extract</summary>

inflect.py - Accurately generate plurals, singular nouns, ordinals, indefinite articles, and word-based representations of numbers. This functionality is limited to English.

Simple example with pluralization and word-representation of numbers:

When `count=243`, the same code will generate:

Example:
```python
>>> import inflect
>>> p = inflect.engine()
```

Sections: NAME, SYNOPSIS, Methods, Plurality/Singularity, Unconditionally Form the Plural, Conditionally Form the Plural, Form Plurals for Specific Parts of Speech, Form the Singular of Plural Nouns, Select the Gender of Singular Pronouns, Deal with "0/1/N" -> "no/1/N" Translation, Use Default Counts, Compare Two Words Number-Intensitively, Add Correct *a* or *an* for a Given Word, Convert Numerals into Ordinals

</details>

### pybreaker

Python implementation of the Circuit Breaker pattern

`pip install pybreaker` · installs (wheel) · licence: BSD License · rank 688 · last release 2025-09-21 · [PyPI](https://pypi.org/project/pybreaker/) · [source](http://github.com/danielfm/pybreaker)

<details><summary>README extract</summary>

PyBreaker is a Python implementation of the Circuit Breaker pattern, described
in Michael T. Nygard's book Release It!.

In Nygard's words, *"circuit breakers exists to allow one subsystem to fail
without destroying the entire system. ...

Features:
* Configurable list of excluded exceptions (e.g. business exceptions)
* Configurable failure threshold and reset timeout
* Support for several event listeners per circuit breaker
* Can guard generator functions
* Functions and properties for easy ...

Example:
```python
import pybreaker

# Used in database integration points
db_breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)
```

Sections: PyBreaker, Features, Requirements, Usage, Event Listening, What Does a Circuit Breaker Do?, Excluding Exceptions, Monitoring and Management

</details>

### agent-client-protocol

A Python implement of Agent Client Protocol (ACP, by Zed Industries)

`pip install agent-client-protocol` · installs (wheel) · licence: not stated · rank 689 · last release 2026-08-16 · [PyPI](https://pypi.org/project/agent-client-protocol/) · [docs](https://agentclientprotocol.github.io/python-sdk/) · [source](https://github.com/agentclientprotocol/python-sdk)

<details><summary>README extract</summary>

Sections: At a glance, Who benefits, How to get started, Quick links, Project layout

</details>

### py-partiql-parser

Pure Python PartiQL Parser

`pip install py-partiql-parser` · installs (wheel) · licence: MIT · rank 695 · last release 2025-10-18 · [PyPI](https://pypi.org/project/py-partiql-parser/)

<details><summary>README extract</summary>

A tokenizer/parser/executor for the PartiQL-language, in Python.

Much beta, such wow. Feel free to raise any issues you encounter.

Example:
```python
import json
from py_partiql_parser import S3SelectParser

original_json = json.dumps({"a1": "b1", "a2": "b2"})
parser = S3SelectParser(source_data={"s3object": original_json})
result = parser.parse("SELECT * FROM s3object")
```

Sections: py-partiql-parser, S3 Usage, DynamoDB Usage, Meat, Outstanding, Notes

</details>

### questionary

Python library to build pretty command line user prompts ⭐️

`pip install questionary` · installs (wheel) · licence: MIT License · rank 698 · last release 2025-08-28 · [PyPI](https://pypi.org/project/questionary/) · [docs](https://questionary.readthedocs.io/) · [source](https://github.com/tmbo/questionary)

<details><summary>README extract</summary>

✨ Questionary is a Python library for effortlessly building pretty command line interfaces ✨

* Features
* Installation
* Usage
* Documentation
* Support

Used and supported by

[](

Features:
Questionary supports the following input prompts:

 * Text
 * Password
 * File Path
 * Confirmation
 * Select
 * Raw select
 * Checkbox
 * Autocomplete ...

Example:
```python
import questionary

questionary.select(
    "What do you want to do?",
    choices=[
        'Order a pizza',
        'Make a reservation',
        'Ask for opening hours'
    ]).ask()  # returns value of selection
```

Sections: Questionary, Features, Usage, Documentation

</details>

### delta-spark

Python APIs for using Delta Lake with Apache Spark

`pip install delta-spark` · installs (wheel) · licence: Apache Software License · rank 699 · last release 2026-10-05 · [PyPI](https://pypi.org/project/delta-spark/) · [docs](https://docs.delta.io/latest/index.html) · [source](https://github.com/delta-io/delta)

<details><summary>README extract</summary>

Delta Lake is an open source storage layer that brings reliability to data lakes. Delta Lake provides ACID transactions, scalable metadata handling, and unifies streaming and batch data processing. Delta Lake runs on top of your existing data lake and is fully compatible with Apache Spark APIs. ...

Sections: Delta Lake, Documentation

</details>

### glom

A declarative object transformer and formatter, for conglomerating nested data.

`pip install glom` · installs (wheel) · licence: BSD License · rank 703 · last release 2025-12-29 · [PyPI](https://pypi.org/project/glom/) · [docs](https://glom.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

*Restructuring data, the Python way*

Real applications have real data, and real data nests. Objects inside
of objects inside of lists of objects.

glom is a new and powerful way to handle real-world data, featuring: ...

Example:
```python
>>> data = {'a': {'b': {'c': 'd'}}}
>>> data'a'['c']
'd'
>>> data2 = {'a': {'b': None}}
>>> data2'a'['c']
Traceback (most recent call last):
...
TypeError: 'NoneType' object is not subscriptable
```

Sections: glom, Examples, Without glom, With glom, Learn more

</details>

### face

A command-line application framework (and CLI parser). Friendly for users, full-featured for developers.

`pip install face` · installs (wheel) · licence: not stated · rank 705 · last release 2026-06-17 · [PyPI](https://pypi.org/project/face/) · [docs](https://python-face.readthedocs.io/)

<details><summary>README extract</summary>

*Command-line parser and interface builder*

Docs here.

* Montage administration tools
* Pocket Protector
* glom CLI

Sections: Face, Users

</details>

### zope.event

Very basic event publishing system

`pip install zope.event` · installs (wheel) · licence: ZPL-2.1 · rank 708 · last release 2026-04-28 · [PyPI](https://pypi.org/project/zope.event/) · [docs](https://zopeevent.readthedocs.io/) · [source](https://github.com/zopefoundation/zope.event)

<details><summary>README extract</summary>

The `zope.event` package provides a simple event system, including:

- An event publishing API, intended for use by applications which are
 unaware of any subscribers to their events.

- A very simple synchronous event-dispatching system, on which more sophisticated
 event dispatching systems can be built. ...

Sections: zope.event, 6.2 (2026-04-28), 6.1 (2025-11-07), 6.0 (2025-09-12), 5.1.1 (2025-07-22), 5.1 (2025-06-26), 5.0 (2023-06-23), 4.6 (2022-12-15), 4.5.0 (2020-09-18), 4.4 (2018-10-05), 4.3.0 (2017-07-25), 4.2.0 (2016-02-17), 4.1.0 (2015-10-18), 4.0.3 (2014-03-19)

</details>

### parsedatetime

Parse human-readable date/time text.

`pip install parsedatetime` · installs (wheel) · licence: Apache Software License · rank 725 · last release 2020-05-31 · [PyPI](https://pypi.org/project/parsedatetime/)

<details><summary>README extract</summary>

Parse human-readable date/time strings.

Python 2.6 or greater is required for parsedatetime version 1.0 or greater.

While we still test with Python 2.6 we cannot guarantee that future changes will not break under 2.6

Example:
```python
import parsedatetime

cal = parsedatetime.Calendar()

cal.parse("tomorrow")
```

Sections: parsedatetime, Running Tests, Using parsedatetime, Documentation, Notes

</details>

### dacite

Simple creation of data classes from dictionaries.

`pip install dacite` · installs (wheel) · licence: MIT License · rank 737 · last release 2025-02-05 · [PyPI](https://pypi.org/project/dacite/)

<details><summary>README extract</summary>

Features:
Dacite supports following features:

- nested structures
- (basic) type checking
- optional fields (i.e. `typing.Optional`)
- unions
- generics
- forward references
- collections
- custom type hooks
- case conversion

Example:
```python
from dataclasses import dataclass
from dacite import from_dict

@dataclass
class User:
    name: str
    age: int
    is_active: bool

data = {
    'name': 'John',
    'age': 30,
    'is_active': True,
}

user = from_dict(data_class=User, data=data)

assert user == User(name='John', age=30, is_active=True)
```

Sections: Requirements, Quick start, Features, Motivation, Usage, Nested structures, Optional fields, Unions, Collections, Generics, Type hooks, Casting, Forward References, Type checking

</details>

### validators

Python Data Validation for Humans™

`pip install validators` · installs (wheel) · licence: MIT License · rank 743 · last release 2026-10-11 · [PyPI](https://pypi.org/project/validators/) · [docs](https://nandgator.github.io/pyvalidators) · [source](https://github.com/python-validators/validators)

<details><summary>README extract</summary>

[][pycqa-link] [][sast-link] [][docs-link] [][vs-link] [][dw-link]

<!-- [][package-link] -->

Python has all kinds of data validation tools, but every one of them seems to
require defining a schema or form. I wanted to create a simple validation
library where validating a simple value does not require defining a form or a
schema.

Then,

Example:
```python
>>> import validators
>>>
>>> validators.email('someone@example.com')
True
```

Sections: validators - Python Data Validation for Humans™, Resources

</details>

### factory-boy

A versatile test fixtures replacement based on thoughtbot's factory_bot for Ruby.

`pip install factory-boy` · installs (wheel) · licence: MIT License · rank 756 · last release 2025-02-03 · [PyPI](https://pypi.org/project/factory-boy/)

<details><summary>README extract</summary>

factory_boy is a fixtures replacement based on thoughtbot's factory_bot.

As a fixtures replacement tool, it aims to replace static, hard to maintain fixtures
with easy-to-use factories for complex objects. ...

Example:
```python
class FooTests(unittest.TestCase):

    def test_with_factory_boy(self):
        # We need a 200€, paid order, shipping to australia, for a VIP customer
        order = OrderFactory(
            amount=200,
            status='PAID',
            customer__is_vip=True,
            address__country='AU',
        )
        # Run the tests here

...
```

...

</details>

### fire

A library for automatically generating command line interfaces.

`pip install fire` · installs (wheel) · licence: Apache-2.0 · rank 772 · last release 2025-08-16 · [PyPI](https://pypi.org/project/fire/) · [source](https://github.com/google/python-fire)

<details><summary>README extract</summary>

_Python Fire is a library for automatically generating command line interfaces
(CLIs) from absolutely any Python object._

- Python Fire is a simple way to create a CLI in Python.
 [[1]](docs/benefits.md#simple-cli)
- Python Fire is a helpful tool for developing and debugging Python code.
 [[2]](docs/benefits.md#debugging) ...

Features:
When you call `Fire`, it fires off (executes) your command.

Example:
```python
import fire

def hello(name="World"):
  return "Hello %s!" % name

if name == 'main':
  fire.Fire(hello)
```

Sections: Python Fire, Basic Usage, Why is it called Fire?, Where can I learn more?, Reference, Disclaimer

</details>

### gql

GraphQL client for Python

`pip install gql` · installs (wheel) · licence: MIT · rank 783 · last release 2026-09-27 · [PyPI](https://pypi.org/project/gql/)

<details><summary>README extract</summary>

This is a GraphQL client for Python.
Plays nicely with `graphene`, `graphql-core`, `graphql-js` and any other GraphQL implementation
compatible with the GraphQL specification.

GQL architecture is inspired by `React-Relay` and `Apollo-Client`.

[][gh-url]
[][pyversion-url]
[][pypi-url]
[][conda-url]
[][codecov-url] ...

Features:
* http
 * including the multipart protocol for subscriptions

 * apollo or graphql-ws protocol
 * Phoenix channels
 * AWS AppSync realtime protocol
* Possibility to validate the requests locally using a GraphQL schema provided locally or fetched ...

Example:
```python
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="

...

</details>

### openapi-schema-validator

OpenAPI schema validation for Python

`pip install openapi-schema-validator` · installs (wheel) · licence: BSD License · rank 792 · last release 2026-04-27 · [PyPI](https://pypi.org/project/openapi-schema-validator/) · [source](https://github.com/python-openapi/openapi-schema-validator)

<details><summary>README extract</summary>

openapi-schema-validator is a Python library that validates schemas against:

* OpenAPI Schema Specification v3.0 which is an extended subset of the JSON Schema Specification Wright Draft 00.
* OpenAPI Schema Specification v3.1 which is an extended superset of the JSON Schema Specification Draft 2020-12. ...

Example:
```python
validate(
    instance,
    schema,
    cls=OAS32Validator,
    allow_remote_references=False,
    check_schema=True,
    enforce_properties_required=False,
    **kwargs,
)
```

Sections: openapi-schema-validator, About, Documentation, Usage, Default dialect resolution, Binary Data Semantics, OpenAPI 3.0, OpenAPI 3.1+, Regex Behavior, Related projects

</details>

### pybind11

Seamless operability between C++11 and Python

`pip install pybind11` · installs (wheel) · licence: BSD-3-Clause · rank 798 · last release 2026-08-06 · [PyPI](https://pypi.org/project/pybind11/) · [docs](https://pybind11.readthedocs.io/)

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

### flit-core

Distribution-building parts of Flit. See flit package for more information

`pip install flit-core` · installs (wheel) · licence: BSD-3-Clause · rank 801 · last release 2026-10-27 · [PyPI](https://pypi.org/project/flit-core/) · [docs](https://flit.pypa.io) · [source](https://github.com/pypa/flit)

<details><summary>README extract</summary>

This provides a PEP 517 build backend
for packages using Flit. The only public
interface is the API specified by PEP 517, at `flit_core.buildapi`.

See the Flit documentation for more
information.

</details>

### openapi-spec-validator

OpenAPI 2.0 (aka Swagger) and OpenAPI 3 spec validator

`pip install openapi-spec-validator` · installs (wheel) · licence: Apache-2.0 · rank 803 · last release 2026-05-20 · [PyPI](https://pypi.org/project/openapi-spec-validator/) · [docs](https://openapi-spec-validator.readthedocs.io/en/latest/) · [source](https://github.com/python-openapi/openapi-spec-validator)

<details><summary>README extract</summary>

OpenAPI Spec Validator is a CLI, pre-commit hook and python package that validates OpenAPI Specs
against the OpenAPI 2.0 (aka Swagger),
OpenAPI 3.0
OpenAPI 3.1
and OpenAPI 3.2
specification. The validator aims to check for full compliance with the Specification.

Check documentation to see more details about the features. ...

Example:
```python
from openapi_spec_validator import validate
from openapi_spec_validator.readers import read_from_filename

spec_dict, base_uri = read_from_filename('openapi.yaml')

# If no exception is raised by validate(), the spec is valid.
validate(spec_dict)

# Example of an intentionally invalid spec.
invalid_spec = {'openapi': '3.1.0'}

...
```

...

</details>

### pytest-env

Set environment variables for pytest sessions.

`pip install pytest-env` · installs (wheel) · licence: MIT · rank 804 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pytest-env/) · [source](https://github.com/pytest-dev/pytest-env)

<details><summary>README extract</summary>

A `pytest` plugin that sets environment variables from `pyproject.toml`, `pytest.toml`, `.pytest.toml`, or `pytest.ini`
configuration files. It can also load variables from `.env` files.

Changelog · Contributing.

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- Installation
- Quick start ...

Example:
```python
import os

def test_database_connection():
    assert os.environ["DATABASE_URL"] == "postgresql://localhost/test_db"
    assert os.environ["DEBUG"] == "true"
```

...

</details>

### mock

Rolling backport of unittest.mock for all Pythons

`pip install mock` · installs (wheel) · licence: BSD License · rank 809 · last release 2025-03-03 · [PyPI](https://pypi.org/project/mock/) · [source](https://github.com/testing-cabal/mock)

<details><summary>README extract</summary>

mock is a library for testing in Python. It allows you to replace parts of
your system under test with mock objects and make assertions about how they
have been used.

mock is now part of the Python standard library, available as `unittest.mock
< in Python 3.3
onwards. ...

</details>

### pybase64

Fast Base64 encoding/decoding

`pip install pybase64` · installs (wheel) · licence: BSD-2-Clause · rank 814 · last release 2026-10-04 · [PyPI](https://pypi.org/project/pybase64/) · [docs](https://pybase64.readthedocs.io/en/stable) · [source](https://github.com/mayeut/pybase64)

<details><summary>README extract</summary>

This project is a wrapper on libbase64.

It aims to provide a fast base64 implementation for base64 encoding/decoding.

Example:
```python
import pybase64

print(pybase64.b64encode(b'>>>foo???', altchars='_:'))
# b'Pj4_Zm9vPz8:'
print(pybase64.b64decode(b'Pj4_Zm9vPz8:', altchars='_:', validate=True))
# b'>>>foo???'

# Standard encoding helpers
print(pybase64.standard_b64encode(b'>>>foo???'))
# b'Pj4+Zm9vPz8/'
print(pybase64.standard_b64decode(b'Pj4+Zm9vPz8/'))
# b'>>>foo???'

...
```

Sections: Fast Base64 implementation, Usage, Benchmark, 1.5.1, 1.5.0, 1.4.3, 1.4.2, 1.4.1, 1.4.0, 1.3.2, 1.3.1, 1.3.0, 1.2.3, 1.2.2

</details>

### shortuuid

A generator library for concise, unambiguous and URL-safe UUIDs.

`pip install shortuuid` · installs (wheel) · licence: BSD License · rank 815 · last release 2024-03-11 · [PyPI](https://pypi.org/project/shortuuid/)

<details><summary>README extract</summary>

`shortuuid` is a simple python library that generates concise, unambiguous, URL-safe
UUIDs.

Often, one needs to use non-sequential IDs in places where users will see them, but the
IDs must be as concise and easy to use as possible. ...

Example:
```python
>>> import shortuuid
```

</details>

### texttable

module to create simple ASCII tables

`pip install texttable` · installs (wheel) · licence: MIT License · rank 824 · last release 2026-10-18 · [PyPI](https://pypi.org/project/texttable/)

<details><summary>README extract</summary>

Python module to create simple ASCII tables

This module is available on PyPI, and has been packaged for several Linux/Unix platforms
(Debian,
FreeBSD, Fedora, Suse...).

If available, cjkwrap library is used instead of textwrap, for a better wrapping of CJK text.

If available, wcwidth library is used for a better rendering (basic emoji support).

Example:
```python
NAME
    texttable - module to create simple ASCII tables

FILE
    /usr/local/lib/python2.7/dist-packages/texttable.py

DESCRIPTION

    Example:

        table = Texttable()
        table.set_cols_align(["l", "r", "c"])
        table.set_cols_valign(["t", "m", "b"])
        table.add_rows([["Name", "Age", "Nickname"],
...
```

Sections: texttable, Availability, Dependencies, Documentation, Forks

</details>

### hyperlink

A featureful, immutable, and correct URL for Python.

`pip install hyperlink` · installs (wheel) · licence: MIT License · rank 835 · last release 2021-01-08 · [PyPI](https://pypi.org/project/hyperlink/)

<details><summary>README extract</summary>

The humble, but powerful, URL runs everything around us. Chances
are you've used several just to read this text.

Hyperlink is a featureful, pure-Python implementation of the URL, with
an emphasis on correctness. MIT licensed.

See the docs at

</details>

### py-spy

(no summary)

`pip install py-spy` · installs (wheel) · licence: MIT License · rank 842 · last release 2026-11-02 · [PyPI](https://pypi.org/project/py-spy/)

### uv-build

The uv build backend

`pip install uv-build` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 850 · last release 2026-11-03 · [PyPI](https://pypi.org/project/uv-build/) · [docs](https://docs.astral.sh/uv) · [source](https://github.com/astral-sh/uv)

<details><summary>README extract</summary>

This package is a slimmed down version of uv containing only the build backend. See
 and for the main project package and
documentation.

</details>

### opt-einsum

Path optimization of einsum functions.

`pip install opt-einsum` · installs (wheel) · licence: MIT License · rank 851 · last release 2024-09-26 · [PyPI](https://pypi.org/project/opt-einsum/)

<details><summary>README extract</summary>

Optimized einsum can significantly reduce the overall execution time of einsum-like expressions (e.g.,
`np.einsum`,
`dask.array.einsum`,
`pytorch.einsum`,
`tensorflow.einsum`,
by optimizing the expression's contraction order and dispatching many
operations to canonical BLAS, cuBLAS, or other specialized routines. ...

Features:
The algorithms found in this repository often power the `einsum` optimizations
in many of the above projects. For example, the optimization of `np.einsum`
has been passed upstream and most of the same features that can be found in
this repository ...

Example:
```python
import numpy as np
from opt_einsum import contract

N = 10
C = np.random.rand(N, N)
I = np.random.rand(N, N, N, N)

%timeit np.einsum('pi,qj,ijkl,rk,sl->pqrs', C, C, I, C, C)
...

</details>

### ansicolors

ANSI colors for Python

`pip install ansicolors` · installs (wheel) · licence: ISC License (ISCL) · rank 856 · last release 2017-06-02 · [PyPI](https://pypi.org/project/ansicolors/)

<details><summary>README extract</summary>

travisciversionversionsimplswheelcoveragebr-coverage|

Add ANSI colors and decorations to your strings.

Example:
```python
from future import print_function  # accomodate Python 2
from colors import *

print(color('my string', fg='blue'))
print(color('some text', fg='red', bg='yellow', style='underline'))
```

Sections: ANSI colors for Python, Example Usage, 24-bit Color and CSS Compatibility, Caveats, More Examples, Utility Functions

</details>

### cchardet

cChardet is high speed universal character encoding detector.

`pip install cchardet` · installs (wheel) · licence: MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later · rank 878 · last release 2026-10-11 · [PyPI](https://pypi.org/project/cchardet/)

_README extract left out: share-alike licence._

### immutabledict

Immutable wrapper around dictionaries (a fork of frozendict)

`pip install immutabledict` · installs (wheel) · licence: MIT · rank 889 · last release 2026-02-15 · [PyPI](https://pypi.org/project/immutabledict/) · [docs](https://immutabledict.corenting.fr) · [source](https://github.com/corenting/immutabledict)

<details><summary>README extract</summary>

An immutable wrapper around dictionaries. immutabledict implements the complete mapping interface and can be used as a drop-in replacement for dictionaries where immutability is desired.

It's a fork of slezica's frozendict. This library is a pure Python, MIT-licensed alternative to the new LGPL-3.0 licensed frozendict.

Example:
```python
from immutabledict import immutabledict

my_item = immutabledict({"a": "value", "b": "other_value"})
print(my_item["a"]) # Print "value"
```

Sections: immutabledict, Example, Differences with the old original frozendict package

</details>

### kafka-python

Pure Python client for Apache Kafka

`pip install kafka-python` · installs (wheel) · licence: Apache-2.0 · rank 890 · last release 2026-11-06 · [PyPI](https://pypi.org/project/kafka-python/) · [docs](https://kafka-python.readthedocs.io) · [source](https://github.com/dpkp/kafka-python)

<details><summary>README extract</summary>

kafka-python is a pure-python client library for Apache Kafka, the distributed
stream processing engine. It has no external dependencies and no Cython/C/rust
core, making installation across a wide variety of environments simple and easy
to manage. ...

Example:
```python
from kafka import KafkaConsumer
consumer = KafkaConsumer('my_favorite_topic')
for msg in consumer:
    print (msg)
```

Sections: kafka-python, What's New in 3.0, KafkaConsumer, KafkaProducer, Module CLI Interface, Compression, Optimized CRC32 Validation, Debugging

</details>

### resolvelib

Resolve abstract dependencies into concrete ones

`pip install resolvelib` · installs (wheel) · licence: ISC License (ISCL) · rank 905 · last release 2025-10-11 · [PyPI](https://pypi.org/project/resolvelib/)

<details><summary>README extract</summary>

ResolveLib at the highest level provides a `Resolver` class that includes
dependency resolution logic. You give it some things, and a little information
on how it should interact with them, and it will spit out a resolution result.

Example:
```python
import resolvelib

# Things I want to resolve.
requirements = [...]

# Implement logic so the resolver understands the requirement format.
class MyProvider:
    ...

provider = MyProvider()
reporter = resolvelib.BaseReporter()

# Create the (reusable) resolver.
resolver = resolvelib.Resolver(provider, reporter)

...
```

Sections: ResolveLib, Intended Usage, Terminology, Package, Version, Specifier, Candidate, Requirement

</details>

### tox

tox is a generic virtualenv management and test command line tool

`pip install tox` · installs (wheel) · licence: MIT · rank 908 · last release 2026-11-06 · [PyPI](https://pypi.org/project/tox/) · [docs](https://tox.wiki) · [source](https://github.com/tox-dev/tox)

<details><summary>README extract</summary>

`tox` aims to automate and standardize testing in Python. It is part of a larger vision of easing the packaging, testing
and release process of Python software (alongside pytest and
devpi).

tox is a generic virtual environment management and test command line tool you can use for: ...

</details>

### groq

The official Python library for the groq API

`pip install groq` · installs (wheel) · licence: Apache Software License · rank 914 · last release 2026-08-26 · [PyPI](https://pypi.org/project/groq/) · [source](https://github.com/groq/groq-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Groq Python library provides convenient access to the Groq REST API from any Python 3.10+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
...
```

...

</details>

### multitasking

Non-blocking Python methods using decorators

`pip install multitasking` · installs (wheel) · licence: Apache Software License · rank 933 · last release 2026-04-23 · [PyPI](https://pypi.org/project/multitasking/)

<details><summary>README extract</summary>

MultiTasking is a lightweight Python library that lets you convert
your Python methods into asynchronous, non-blocking methods simply by
using a decorator. Perfect for I/O-bound tasks, API calls, web scraping,
and any scenario where you want to run multiple operations concurrently
without the complexity of manual thread or process management.

Example:
```python
import multitasking
import time

@multitasking.task
def fetch_data(url_id):
    # Simulate API call or I/O operation
    time.sleep(1)
    return f"Data from {url_id}"

# These run concurrently, not sequentially!
for i in range(5):
    fetch_data(i)

# Wait for all tasks to complete
multitasking.wait_for_tasks()
print("All data fetched!")
```

...

</details>

### pyyaml-env-tag

A custom YAML tag for referencing environment variables in YAML files.

`pip install pyyaml-env-tag` · installs (wheel) · licence: MIT · rank 936 · last release 2025-05-13 · [PyPI](https://pypi.org/project/pyyaml-env-tag/) · [source](https://github.com/waylan/pyyaml-env-tag)

<details><summary>README extract</summary>

A custom YAML tag for referencing environment variables in YAML files.

[][pypi-link]
[][GHAction-link]
[][codecov-link]

Example:
```python
import yaml
from yaml_env_tag import add_env_tag

myLoader = add_env_tag(yaml.Loader)
```

Sections: pyyaml_env_tag, Enabling the tag, Using the tag, Related, [1.1] - 2025-05-13, [1.0] - 2025-05-09, [0.1] - 2020-11-11

</details>

### rdflib

RDFLib is a Python library for working with RDF, a simple yet powerful language for representing information.

`pip install rdflib` · installs (wheel) · licence: BSD License · rank 937 · last release 2026-02-13 · [PyPI](https://pypi.org/project/rdflib/) · [docs](https://rdflib.readthedocs.org/) · [source](https://github.com/RDFLib/rdflib)

<details><summary>README extract</summary>

RDFLib is a pure Python package for working with RDF. RDFLib contains most things you need to work with RDF, including:

* parsers and serializers for RDF/XML, N3, NTriples, N-Quads, Turtle, TriX, Trig, JSON-LD and even HexTuples
* a Graph interface which can be backed by any one of a number of Store implementations
* Store implementations for ...

Features:
The library contains parsers and serializers for RDF/XML, N3,
NTriples, N-Quads, Turtle, TriX, JSON-LD, RDFa and Microdata.

The library presents a Graph interface which can be backed by
any one of a number of Store implementations. ...

Example:
```python
from rdflib import Graph
g = Graph()
g.parse('

for s, p, o in g:
    print(s, p, o)
```

...

</details>

### nvidia-ml-py

Python Bindings for the NVIDIA Management Library

`pip install nvidia-ml-py` · installs (wheel) · licence: BSD License · rank 946 · last release 2026-09-25 · [PyPI](https://pypi.org/project/nvidia-ml-py/)

<details><summary>README extract</summary>

Python bindings to the NVIDIA Management Library

Provides a Python interface to GPU management and monitoring functions.

This is a wrapper around the NVML library.
For information about the NVML library, see the NVML developer page

Download the latest package from: ...

Example:
```python
>>> from pynvml import *
>>> nvmlInit()
>>> print(f"Driver Version: {nvmlSystemGetDriverVersion()}")
Driver Version: 11.515.48
>>> deviceCount = nvmlDeviceGetCount()
>>> for i in range(deviceCount):
...     handle = nvmlDeviceGetHandleByIndex(i)
...     print(f"Device {i} : {nvmlDeviceGetName(handle)}")
...
Device 0 : Tesla K40c

>>> nvmlShutdown()
```

</details>

### openai-agents

OpenAI Agents SDK

`pip install openai-agents` · installs (wheel) · licence: MIT · rank 954 · last release 2026-10-15 · [PyPI](https://pypi.org/project/openai-agents/) · [source](https://github.com/openai/openai-agents-python)

<details><summary>README extract</summary>

The OpenAI Agents SDK is a lightweight yet powerful framework for building multi-agent workflows. It is provider-agnostic, supporting the OpenAI Responses and Chat Completions APIs, as well as 100+ other LLMs.

> [!NOTE]
> Looking for the JavaScript/TypeScript version? Check out Agents SDK JS/TS.

1. ...

Example:
```python
from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.
```

Sections: OpenAI Agents SDK, Core concepts, Get started, venv, uv, Run your first agents, Run a text agent, Run a sandbox agent, Run a realtime agent, Run a voice agent

</details>

### feedparser

Universal feed parser, handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds

`pip install feedparser` · installs (wheel) · licence: BSD-2-Clause · rank 968 · last release 2026-07-30 · [PyPI](https://pypi.org/project/feedparser/)

<details><summary>README extract</summary>

Parse Atom and RSS feeds in Python.

Sections: feedparser, Documentation

</details>

### dockerfile-parse

Python library for Dockerfile manipulation

`pip install dockerfile-parse` · installs (wheel) · licence: BSD License · rank 975 · last release 2023-07-18 · [PyPI](https://pypi.org/project/dockerfile-parse/)

<details><summary>README extract</summary>

[![unittests status badge]][unittests status link]
[![coveralls status badge]][coveralls status link]
[![lgtm python badge]][lgtm python link]
[![lgtm alerts badge]][lgtm alerts link]
[![linters status badge]][linters status link]

Python library for parsing Dockerfile files.

Example:
```python
from pprint import pprint
from dockerfile_parse import DockerfileParser

dfp = DockerfileParser()
dfp.content = """\
From  base
LABEL foo="bar baz"
USER  me"""

# Print the parsed structure:
pprint(dfp.structure)
pprint(dfp.json)
pprint(dfp.labels)

# Set a new base:
dfp.baseimage = 'centos:7'

# Print the new Dockerfile with an updated FROM line:
...
```

Sections: dockerfile-parse, From PyPI, From git, Usage

</details>

### ldap3

A strictly RFC 4510 conforming LDAP V3 pure Python client library

`pip install ldap3` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 982 · last release 2021-07-18 · [PyPI](https://pypi.org/project/ldap3/)

_README extract left out: share-alike licence._

### frozendict

A simple immutable dictionary

`pip install frozendict` · installs (wheel) · licence: LGPL-3.0-only · rank 984 · last release 2026-10-30 · [PyPI](https://pypi.org/project/frozendict/) · [source](https://github.com/Marco-Sulla/python-frozendict)

_README extract left out: share-alike licence._

### pathvalidate

pathvalidate is a Python library to sanitize/validate a string such as filenames/file-paths/etc.

`pip install pathvalidate` · installs (wheel) · licence: MIT License · rank 988 · last release 2025-06-15 · [PyPI](https://pypi.org/project/pathvalidate/) · [docs](https://pathvalidate.rtfd.io/) · [source](https://github.com/thombashi/pathvalidate)

<details><summary>README extract</summary>

pathvalidate is a Python library to sanitize/validate a string such as filenames/file-paths/etc.

Features:
- file name
 - file path

 - Remove invalid characters for a target platform
 - Replace reserved names for a target platform
 - Normalize
 - Remove unprintable characters
- Argument validator/sanitizer for `argparse` and `click` ...

Sections: Summary, Features, CLI tool, Examples, Sanitize a filename, Sanitize a filepath, Validate a filename, Check a filename, filename/filepath validator for `argparse`, filename/filepath sanitizer for `argparse`, filename/filepath validator for `click`, filename/filepath sanitizer for `click`, For more information, Dependencies

</details>

### deptry

A command line utility to check for unused, missing and transitive dependencies in a Python project.

`pip install deptry` · installs (wheel) · licence: MIT · rank 1005 · last release 2026-03-18 · [PyPI](https://pypi.org/project/deptry/) · [docs](https://deptry.com) · [source](https://github.com/osprey-oss/deptry)

<details><summary>README extract</summary>

_deptry_ is a command line tool to check for issues with dependencies in a Python project, such as unused or missing
dependencies. It supports projects
using Poetry, pip, PDM, uv,
and more generally any project supporting PEP 621 specification. ...

Sections: Quickstart, Prerequisites, Usage, Configuration

</details>

### constantly

Symbolic constants in Python

`pip install constantly` · installs (wheel) · licence: MIT License · rank 1008 · last release 2023-10-28 · [PyPI](https://pypi.org/project/constantly/)

<details><summary>README extract</summary>

A library that provides symbolic constant support. It includes collections and
constants with text, numeric, and bit flag values. Originally
`twisted.python.constants` from the Twisted
project.

Sections: Constantly, Documentation, Tests

</details>

### lockfile

Platform-independent file locking module

`pip install lockfile` · installs (wheel) · licence: MIT License · rank 1017 · last release 2015-11-25 · [PyPI](https://pypi.org/project/lockfile/)

<details><summary>README extract</summary>

Note: This package is deprecated. It is highly preferred that instead of
using this code base that instead `fasteners`_ or `oslo.concurrency`_ is
used instead. For any questions or comments or further help needed
please email `openstack-dev`_ and prefix your email subject
with ``oslo`` (for a faster response).

.. _fasteners:
.. ...

</details>

### PyPDF2

A pure-python PDF library capable of splitting, merging, cropping, and transforming PDF files

`pip install PyPDF2` · installs (wheel) · licence: BSD License · rank 1024 · last release 2022-12-31 · [PyPI](https://pypi.org/project/PyPDF2/) · [docs](https://pypdf2.readthedocs.io/en/latest/) · [source](https://github.com/py-pdf/PyPDF2)

<details><summary>README extract</summary>

Example:
```python
from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
```

Sections: PyPDF2, Usage, Q&A, Issues, Code

</details>

### paginate

Divides large result sets into pages for easier browsing

`pip install paginate` · installs (wheel) · licence: MIT License · rank 1033 · last release 2024-08-25 · [PyPI](https://pypi.org/project/paginate/)

<details><summary>README extract</summary>

What is pagination?

This module helps dividing large lists of items into pages. The user is shown one page at a time and
can navigate to other pages. Imagine you are offering a company phonebook and let the user search
the entries. If the search result contains 23 entries but you may want to display no more than 10
entries at once. ...

</details>

### makefun

Small library to dynamically create python functions.

`pip install makefun` · installs (wheel) · licence: BSD License · rank 1034 · last release 2025-05-09 · [PyPI](https://pypi.org/project/makefun/)

<details><summary>README extract</summary>

Small library to dynamically create python functions.

The documentation for users is available here:

A readme for developers is available here:

</details>

### numexpr

Fast numerical expression evaluator for NumPy

`pip install numexpr` · installs (wheel) · licence: MIT · rank 1047 · last release 2026-07-18 · [PyPI](https://pypi.org/project/numexpr/) · [docs](https://numexpr.readthedocs.io) · [source](https://github.com/pydata/numexpr)

<details><summary>README extract</summary>

:Author: David M. Cooke, Francesc Alted, and others.
:Maintainer: Francesc Alted
:Contact: faltet@gmail.com
:URL:
:Documentation:
:GitHub Actions:
:PyPi:
:DOI:
:readthedocs:

NumExpr is a fast numerical expression evaluator for NumPy. ...

Example:
```python
>>> import numpy as np
>>> import numexpr as ne

>>> a = np.arange(1e6)   # Choose large arrays for better speedups
>>> b = np.arange(1e6)

>>> ne.evaluate("a + 1")   # a simple expression
array([  1.00000000e+00,   2.00000000e+00,   3.00000000e+00, ...,
         9.99998000e+05,   9.99999000e+05,   1.00000000e+06])

...
```

Sections: NumExpr: Fast numerical expression evaluator for NumPy, What is NumExpr?, How NumExpr achieves high performance, From wheels, From Source, Usage, Documentation

</details>

### backrefs

A wrapper around re and regex that adds additional back references.

`pip install backrefs` · installs (wheel) · licence: MIT · rank 1054 · last release 2026-11-03 · [PyPI](https://pypi.org/project/backrefs/)

<details><summary>README extract</summary>

[][donate-link]
[][codecov-link]
[][pypi-link]
[][pypi-link]
[][pypi-link]
[][license-link]

Backrefs is a wrapper around Python's built-in Re and the 3rd party Regex library. Backrefs adds various
additional back references (and a couple other features) that are known to some regular expression engines, but not to
Python's Re and/or Regex. ...

Example:
```python
>>> from backrefs import bre
>>> pattern = bre.compile(r'(\p{Letter}+)')
>>> pattern.sub(r'\C\1\E', 'sometext')
'SOMETEXT'
```

Sections: Backrefs, Documentation

</details>

### huey

a little task queue

`pip install huey` · installs (wheel) · licence: not stated · rank 1055 · last release 2026-11-01 · [PyPI](https://pypi.org/project/huey/) · [docs](https://huey.readthedocs.io/) · [source](https://github.com/coleifer/huey)

<details><summary>README extract</summary>

*a lightweight alternative*.

huey is:

* a task queue
* written in python
* clean and simple API

huey has:

* support for redis (or valkey/redict), postgres, sqlite, file-system, or in-memory storage
* zero dependencies (`redis-py` required to use redis-like brokers,
 `psycopg` for postgres).
* example code. ...

Example:
```python
from huey import RedisHuey, crontab

# Or PostgresHuey, SqliteHuey, FileHuey, etc...
huey = RedisHuey('my-app', host='redis.myapp.com')

@huey.task()
def add_numbers(a, b):
    return a + b

@huey.task(retries=2, retry_delay=60)
def flaky_task(url):
    # This task might fail, in which case it will be retried up to 2 times
...
```

Sections: At a glance, Running the consumer, Storage, Frameworks, Documentation, Project page

</details>

### PyWavelets

PyWavelets, wavelet transform module

`pip install PyWavelets` · installs (wheel) · licence: MIT AND BSD-3-Clause · rank 1060 · last release 2026-09-07 · [PyPI](https://pypi.org/project/PyWavelets/) · [docs](https://pywavelets.readthedocs.io/) · [source](https://github.com/PyWavelets/pywt)

<details><summary>README extract</summary>

+---------------+-----------------+
 Master branch |
+===============+=================+
+---------------+-----------------+
+---------------+-----------------+
+---------------+-----------------+

PyWavelets is a free Open Source library for wavelet transforms in Python. ...

Sections: PyWavelets, What is PyWavelets, Documentation, Contact

</details>

### python-ulid

Universally unique lexicographically sortable identifier

`pip install python-ulid` · installs (wheel) · licence: MIT · rank 1071 · last release 2026-10-27 · [PyPI](https://pypi.org/project/python-ulid/) · [docs](https://python-ulid.readthedocs.io) · [source](https://github.com/mdomke/python-ulid)

<details><summary>README extract</summary>

A `ULID` is a *universally unique lexicographically sortable identifier*. It is

* 128-bit compatible with `UUID`
* 1.21e+24 unique ULIDs per millisecond
* Lexicographically sortable!
* Canonically encoded as a 26 character string, as opposed to the 36 character UUID
* Uses Crockford's base32 for better efficiency and readability (5 bits per ...

Example:
```python
>>> from ulid import ULID
>>> ULID()
ULID(01E75HZVW36EAZKMF1W7XNMSB4)
```

Sections: Basic Usage, Pydantic integration, Generators and policies, Choosing a monotonicity policy, Overriding the default generator, Command line interface, Other implementations

</details>

### python-gnupg

A wrapper for the Gnu Privacy Guard (GPG or GnuPG)

`pip install python-gnupg` · installs (wheel) · licence: BSD License · rank 1081 · last release 2026-09-29 · [PyPI](https://pypi.org/project/python-gnupg/) · [docs](https://gnupg.readthedocs.io/) · [source](https://github.com/vsajip/python-gnupg)

<details><summary>README extract</summary>

This module allows easy access to GnuPG's key management, encryption and signature
functionality from Python programs. It is intended for use with Python 2.7 or
greater.

Releases are normally signed using a GnuPG key with the user id
vinay_sajip@yahoo.co.uk and the following fingerprint:

CA74 9061 914E AC13 8E66 EADB 9147 B477 339A 9B86 ...

</details>

### cachebox

The fastest memoizing and caching Python library written in Rust

`pip install cachebox` · installs (wheel) · licence: MIT License · rank 1088 · last release 2026-10-29 · [PyPI](https://pypi.org/project/cachebox/) · [source](https://github.com/awolverp/cachebox)

<details><summary>README extract</summary>

_The fastest caching Python library written in Rust

> [!WARNING]\
> The new version v6 has incompatibilities with v5. For more info see Migration Guide.

You can easily perform powerful caching operations in Python as fast as possible.
This can make your application a lot faster and it can be a good choice in complex applications. ...

Features:
- ⚡ Rust \
 It uses the _Rust_ language for high-performance.

- 🧮 SwissTable \
 It uses Google's high-performance SwissTable hash map. Thanks to hashbrown.

- ✨ Low memory usage \
 It has very low memory usage. ...

Example:
```python
import cachebox

@cachebox.cached(cachebox.FIFOCache(maxsize=128))
def factorial(number: int) -> int:
    fact = 1
    for num in range(2, number + 1):
        fact *= num
    return fact

...

</details>

### toposort

Implements a topological sort algorithm.

`pip install toposort` · installs (wheel) · licence: Apache Software License · rank 1098 · last release 2023-02-27 · [PyPI](https://pypi.org/project/toposort/) · [source](https://gitlab.com/ericvsmith/toposort)

<details><summary>README extract</summary>

Features:
Implements a topological sort algorithm.

From `Wikipedia <
In computer science, a topological sort (sometimes abbreviated topsort
or toposort) or topological ordering of a directed graph is a linear
ordering of its vertices such that for every ...

Sections: toposort, Overview, Input data description, Typical usage, Circular dependencies

</details>

### cronsim

Cron expression parser and evaluator

`pip install cronsim` · installs (wheel) · licence: BSD License · rank 1105 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cronsim/) · [source](https://github.com/cuu508/cronsim.git)

<details><summary>README extract</summary>

Cron Sim(ulator), a cron expression parser and evaluator. Works with Python 3.11+.
CronSim is written for and being used in
Healthchecks
(a cron job monitoring service).

Development priorities:

* Correctness. CronSim tries to match Debian's cron as closely as possible,
 including its quirky behaviour during DST transitions.
* Readability. ...

Example:
```python
from datetime import datetime
from cronsim import CronSim

it = CronSim("0 0 * 2 MON#5", datetime(2020, 1, 1))
for x in range(0, 5):
    print(next(it))
```

Sections: CronSim, Usage, CronSim Works With zoneinfo, DST Transitions, Cron Expression Feature Matrix, The `explain()` Method

</details>

### jsonpath-python

A lightweight and powerful JSONPath implementation for Python

`pip install jsonpath-python` · installs (wheel) · licence: MIT License · rank 1106 · last release 2026-05-07 · [PyPI](https://pypi.org/project/jsonpath-python/) · [source](https://github.com/sean2077/jsonpath-python)

<details><summary>README extract</summary>

A lightweight and powerful JSONPath implementation for Python.

Features:
There are already several JSONPath libraries in Python, so why choose this one?

1. Lightweight & Zero Dependency: Unlike `jsonpath-ng` which relies on complex AST parsing frameworks like `ply`, `jsonpath-python` is implemented with pure Python ...

Example:
```python
>>> from jsonpath import JSONPath

# For the data used in the following example, please refer to the Appendix part.
```

Sections: jsonpath-python, Why jsonpath-python?, Features, JSONPath Syntax, Operators, Examples, Select Fields, Recursive Descent, Slice, Filter Expression, Sorter Expression, Field-Extractor Expression, Update Data, API Reference

</details>

### pyproject-api

API to interact with the python pyproject.toml based projects

`pip install pyproject-api` · installs (wheel) · licence: MIT · rank 1110 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pyproject-api/) · [source](https://github.com/tox-dev/pyproject-api)

### python-hcl2

A parser for HCL2

`pip install python-hcl2` · installs (wheel) · licence: MIT License · rank 1117 · last release 2026-09-08 · [PyPI](https://pypi.org/project/python-hcl2/)

<details><summary>README extract</summary>

A parser for HCL2 written in Python using
Lark. It can be used as a Python library or through its CLI tools:
`hcl2tojson`, `jsontohcl2`, and `hq` — a jq-like query tool for HCL files.
Supports HCL2 only (not backwards compatible with HCL v1) and works with any HCL2 config file such as Terraform. ...

Example:
```python
import hcl2

with open("main.tf") as f:
    data = hcl2.load(f)
```

Sections: Python HCL2, About Amplify, Getting Started, Prerequisites, Usage, Documentation, CLI Tools, Building From Source, Running Tests, Releasing, Roadmap, Responsible Disclosure, Limitations

</details>

### a2a-sdk

A2A Python SDK

`pip install a2a-sdk` · installs (wheel) · licence: Apache-2.0 · rank 1121 · last release 2026-10-27 · [PyPI](https://pypi.org/project/a2a-sdk/) · [docs](https://a2a-protocol.org/latest/sdk/python/) · [source](https://github.com/a2aproject/a2a-python)

<details><summary>README extract</summary>

Sections: A2A Python SDK, ✨ Features, 🧩 Compatibility, 🚀 Getting Started, Prerequisites, Examples, Helloworld Example, 🌐 More Examples

</details>

### geventhttpclient

HTTP client library for gevent

`pip install geventhttpclient` · installs (wheel) · licence: MIT · rank 1122 · last release 2026-10-09 · [PyPI](https://pypi.org/project/geventhttpclient/) · [source](https://github.com/geventhttpclient/geventhttpclient)

<details><summary>README extract</summary>

**A fast, gevent-native HTTP client for Python with a low-overhead C parser, and drop-in APIs for
`requests`, `httpx` and `http.client`.**

Features:
- Low per-request overhead. HTTP parsing is done by the C-based
 llhttp parser, which reduces client-side CPU cost. This does
 not make transfers faster; see Benchmarks for what is measured.
- Built for concurrency. ...

Example:
```python
from geventhttpclient import Session

with Session() as s:
    r = s.get("
    r.raise_for_status()
    print(r.json())
```

Sections: geventhttpclient, Why geventhttpclient?, Quick start, Choose your interface, requests-compatible, httpx-compatible, http.client / httplib, httplib2 and urllib monkey patching, Low-level HTTPClient, Concurrency, Streaming responses, Chunked request bodies, Benchmarks

</details>

### syrupy

Pytest Snapshot Test Utility

`pip install syrupy` · installs (wheel) · licence: MIT · rank 1123 · last release 2026-09-13 · [PyPI](https://pypi.org/project/syrupy/) · [source](https://github.com/syrupy-project/syrupy)

<details><summary>README extract</summary>

Features:
Syrupy is a zero-dependency pytest snapshot plugin that enables developers to write tests which assert immutability of computed results. ...

Example:
```python
def test_foo(snapshot):
    actual = "Some computed value!"
    assert actual == snapshot
```

Sections: syrupy, Overview, Motivation, Pytest and Python Compatibility, Usage, Basic Usage, Usage in `unittest.TestCase` subclasses, Custom Objects, Representation, Attributes, CLI Options, Assertion Options, `matcher`, Composing Matchers

</details>

### django-redis

Full featured redis cache backend for Django.

`pip install django-redis` · installs (wheel) · licence: BSD-3-Clause · rank 1132 · last release 2026-06-02 · [PyPI](https://pypi.org/project/django-redis/) · [source](https://github.com/jazzband/django-redis)

<details><summary>README extract</summary>

This is a Jazzband project. By contributing you agree
to abide by the Contributor Code of Conduct and follow the guidelines.

django-redis is a BSD licensed, full featured Redis cache and session backend
for Django.

Features:
- Uses native redis-py url notation connection strings
- Pluggable clients
- Pluggable parsers
- Pluggable serializers
- Primary/secondary support in the default client
- Comprehensive test suite ...

Example:
```python
cache.set("key", "value", timeout=None)
```

...

</details>

### uritools

URI parsing, classification and composition

`pip install uritools` · installs (wheel) · licence: MIT · rank 1143 · last release 2026-11-07 · [PyPI](https://pypi.org/project/uritools/) · [docs](https://uritools.readthedocs.io/en/stable/) · [source](https://github.com/tkem/uritools/)

<details><summary>README extract</summary>

This module provides RFC 3986 compliant functions for parsing,
classifying and composing URIs and URI references, largely replacing
the Python Standard Library's `urllib.parse` module.

For various reasons, `urllib.parse` is not compliant with current
Internet standards. As stated in Lib/urllib/parse.py: ...

Example:
```python
>>> from uritools import uricompose, urijoin, urisplit, uriunsplit
>>> uricompose(scheme='foo', host='example.com', port=8042,
...            path='/over/there', query={'name': 'ferret'},
...            fragment='nose')
'foo://example.com:8042/over/there?name=ferret#nose'
>>> parts = urisplit(_)
>>> parts.scheme
'foo'
>>> parts.authority
...
```

Sections: uritools, Project Resources, Related Projects

</details>

### monotonic

An implementation of time.monotonic() for Python 2 & < 3.3

`pip install monotonic` · installs (wheel) · licence: Apache Software License · rank 1144 · last release 2021-08-11 · [PyPI](https://pypi.org/project/monotonic/)

<details><summary>README extract</summary>

monotonic
~~~~~~~~~

This module provides a ``monotonic()`` function which returns the
value (in fractional seconds) of a clock which never goes backwards.

On Python 3.3 or newer, ``monotonic`` will be an alias of
``time.monotonic`` from the standard library. On older versions,
it will fall back to an equivalent implementation: ...

</details>

### colorclass

Colorful worry-free console applications for Linux, Mac OS X, and Windows.

`pip install colorclass` · installs (wheel) · licence: MIT License · rank 1169 · last release 2021-12-09 · [PyPI](https://pypi.org/project/colorclass/) · [docs](https://github.com/matthewdeanmartin/colorclass) · [source](https://github.com/matthewdeanmartin/colorclass)

<details><summary>README extract</summary>

Yet another ANSI color text library for Python. Provides "auto colors" for dark/light terminals. Works on Linux, OS X,
and Windows. For Windows support you just need to call ``Windows.enable()`` in your application.

On Linux/OS X ``autocolors`` are toggled by calling ``set_light_background()`` and ``set_dark_background()``. ...

Example:
```python
from colorclass import Color
color_string = Color('{red}Test{/red}')

>>> color_string
u'\x1b31mTest\x1b[39m'

>>> len(color_string)
4

>>> color_string.istitle()
True
```

Sections: colorclass, Quickstart, Piped Command Line, Example Implementation, Usage

</details>

### cohere

(no summary)

`pip install cohere` · installs (wheel) · licence: MIT License · rank 1176 · last release 2026-11-04 · [PyPI](https://pypi.org/project/cohere/) · [source](https://github.com/cohere-ai/cohere-python)

<details><summary>README extract</summary>

The Cohere Python SDK allows access to Cohere models across many different platforms: the cohere platform, AWS (Bedrock, Sagemaker), Azure, GCP and Oracle OCI. For a full list of support and snippets, please take a look at the SDK support docs page.

Cohere documentation and API reference is available here.

Example:
```python
import cohere

co = cohere.ClientV2()

response = co.chat(
    model="command-r-plus-08-2024",
    messages=[{"role": "user", "content": "hello world!"}],
)

print(response)
```

Sections: Cohere Python SDK, Documentation, Usage, Streaming, Oracle Cloud Infrastructure (OCI), OCI Authentication Methods, OCI Model Availability and Limitations

</details>

### python-daemon

Library to implement a well-behaved Unix daemon process.

`pip install python-daemon` · installs (wheel) · licence: Apache Software License · rank 1182 · last release 2024-12-03 · [PyPI](https://pypi.org/project/python-daemon/) · [source](https://pagure.io/python-daemon/)

<details><summary>README extract</summary>

This library implements the well-behaved daemon specification of
:pep:`3143`, “Standard daemon process library”.

A well-behaved Unix daemon process is tricky to get right, but the
required steps are much the same for every daemon program. ...

</details>

### pyppmd

PPMd compression/decompression library

`pip install pyppmd` · installs (wheel) · licence: LGPL-2.1-or-later · rank 1187 · last release 2025-11-27 · [PyPI](https://pypi.org/project/pyppmd/) · [docs](https://pyppmd.readthedocs.io/en/stable/) · [source](https://github.com/miurahr/pyppmd)

_README extract left out: share-alike licence._

### asyncio

Deprecated backport of asyncio; use the stdlib package instead

`pip install asyncio` · installs (wheel) · licence: Apache-2.0 · rank 1189 · last release 2025-08-05 · [PyPI](https://pypi.org/project/asyncio/) · [source](https://github.com/python/asyncio)

<details><summary>README extract</summary>

This package once provided a backport of the `asyncio` module for Python
versions prior to 3.4. The `asyncio` module has shipped with the Python
standard library since Python 3.4 and this separate distribution is no longer
needed.

Do not install this package. Use the implementation that comes with
Python instead: ...

</details>

### inflate64

deflate64 compression/decompression library

`pip install inflate64` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 1191 · last release 2025-11-28 · [PyPI](https://pypi.org/project/inflate64/) · [docs](https://inflate64.readthedocs.io/en/stable/) · [source](https://github.com/miurahr/inflate64)

_README extract left out: share-alike licence._

### py7zr

Pure python 7-zip library

`pip install py7zr` · installs (wheel) · licence: LGPL-2.1-or-later · rank 1192 · last release 2026-10-12 · [PyPI](https://pypi.org/project/py7zr/) · [docs](https://py7zr.readthedocs.io/en/stable/) · [source](https://github.com/miurahr/py7zr)

_README extract left out: share-alike licence._

### expiringdict

Dictionary with auto-expiring values for caching purposes

`pip install expiringdict` · installs (wheel) · licence: Apache Software License · rank 1197 · last release 2022-06-21 · [PyPI](https://pypi.org/project/expiringdict/)

<details><summary>README extract</summary>

ChangeLog

expiringdict is a Python caching library. The core of the library is ExpiringDict class which
is an ordered dictionary with auto-expiring values for caching purposes. Expiration happens on
any access, object is locked during cleanup from expired values. ...

Example:
```python
from expiringdict import ExpiringDict
cache = ExpiringDict(max_len=100, max_age_seconds=10)
```

Sections: Expiring Dict, Usage

</details>

### pybcj

bcj filter library

`pip install pybcj` · installs (wheel) · licence: LGPL-2.1-or-later · rank 1200 · last release 2026-07-16 · [PyPI](https://pypi.org/project/pybcj/) · [source](https://github.com/miurahr/pybcj)

_README extract left out: share-alike licence._

### simpleeval

A simple, safe single expression evaluator library.

`pip install simpleeval` · installs (wheel) · licence: MIT License · rank 1206 · last release 2026-09-12 · [PyPI](https://pypi.org/project/simpleeval/) · [source](https://github.com/danthedeckie/simpleeval)

<details><summary>README extract</summary>

A single file library for easily adding evaluatable expressions into
python projects. Say you want to allow a user to set an alarm volume, which
could depend on the time of day, alarm level, how many previous alarms had gone
off, and if there is music playing at the time. ...

Example:
```python
from simpleeval import simple_eval

simple_eval("21 + 21")
```

Sections: simpleeval (Simple Eval), Basic Usage, Note, Operators, Limited Power, Strings (and other Iterables) Safety, If Expressions, Functions, Names, Creating an Evaluator Class, Compound Types, Extending, Limiting Attribute Access, Allowlist recommendation

</details>

### minio

MinIO Python SDK for Amazon S3 Compatible Cloud Storage

`pip install minio` · installs (wheel) · licence: Apache Software License · rank 1209 · last release 2025-11-27 · [PyPI](https://pypi.org/project/minio/)

<details><summary>README extract</summary>

The MinIO Python Client SDK provides high level APIs to access any MinIO Object Storage or other Amazon S3 compatible service.

This Quickstart Guide covers how to install the MinIO client SDK, connect to the object storage service, and create a sample file uploader.

The example below uses:
- Python version 3.7+ ...

Example:
```python
from minio import Minio

client = Minio("play.min.io",
    access_key="Q3AM3UQ867SPQQA43P2F",
    secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
)
```

Sections: Using `pip`, Using Source From GitHub, Create a MinIO Client, Example - File Uploader, `file_uploader.py`, More References, Explore Further

</details>

### multivolumefile

multi volume file wrapper library

`pip install multivolumefile` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 1218 · last release 2021-04-29 · [PyPI](https://pypi.org/project/multivolumefile/)

_README extract left out: share-alike licence._

### elevenlabs

(no summary)

`pip install elevenlabs` · installs (wheel) · licence: MIT License · rank 1237 · last release 2026-11-06 · [PyPI](https://pypi.org/project/elevenlabs/) · [source](https://github.com/elevenlabs/elevenlabs-python)

<details><summary>README extract</summary>

The official Python SDK for ElevenLabs. ElevenLabs brings the most compelling, rich and lifelike voices to creators and developers in just a few lines of code.

Check out the HTTP API documentation.

Example:
```python
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation, ClientTools
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

elevenlabs = ElevenLabs(
  api_key="YOUR_API_KEY",
)

# Create audio interface for real-time audio input/output
...
```

Sections: ElevenLabs Python Library, 📖 API & Docs, Usage, Main Models, Voices, Clone Voice, Streaming, Async Client, ElevenAgents, Basic Usage, Disconnection Details, Tool Registration, Agent workflows as code, Editing an existing agent

</details>

### blessed

Easy, practical library for making terminal apps, by providing an elegant, well-documented interface for Terminals.

`pip install blessed` · installs (wheel) · licence: MIT · rank 1242 · last release 2026-10-20 · [PyPI](https://pypi.org/project/blessed/) · [docs](https://blessed.readthedocs.io) · [source](https://github.com/jquast/blessed)

<details><summary>README extract</summary>

pypi_downloadscodecovwindowslinuxmacbsd|

Blessed is an easy, practical *library* for making *terminal* apps, by providing an elegant,
well-documented interface to Colors, Keyboard input, and screen position and Location
capabilities.

It's meant to be *fun* and *easy*, to do basic terminal graphics and styling with Python using
*blessed*. ...

Example:
```python
from blessed import Terminal

term = Terminal()

print(term.home + term.clear + term.move_y(term.height // 2))
print(term.black_on_darkkhaki(term.center('press any key to continue.')))

with term.cbreak(), term.hidden_cursor():
    inp = term.inkey()

print(term.move_down(2) + 'You pressed ' + term.bold(repr(inp)))
```

Sections: Introduction, Examples, Requirements, Brief Overview, Before And After

</details>

### google-adk

Agent Development Kit

`pip install google-adk` · installs (wheel) · licence: Apache Software License · rank 1243 · last release 2026-11-07 · [PyPI](https://pypi.org/project/google-adk/) · [docs](https://google.github.io/adk-docs/) · [source](https://github.com/google/adk-python)

<details><summary>README extract</summary>

Example:
```python
from google.adk import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-3.5-flash",
    instruction="You are a helpful assistant. Greet the user warmly.",
)
```

Sections: Important Links, ADK in other languages, ✨ Key Features, Quick Start, Agent, Workflow, Run Locally, Evaluate Agents, 🚀 Deployment Options, 📚 Documentation, Vibe Coding

</details>

### django-debug-toolbar

A configurable set of panels that display various debug information about the current request/response.

`pip install django-debug-toolbar` · installs (wheel) · licence: BSD License · rank 1257 · last release 2026-09-01 · [PyPI](https://pypi.org/project/django-debug-toolbar/) · [docs](https://django-debug-toolbar.readthedocs.io/) · [source](https://github.com/django-commons/django-debug-toolbar)

<details><summary>README extract</summary>

The Django Debug Toolbar is a configurable set of panels that display various
debug information about the current request/response and when clicked, display
more details about the panel's content.

Here's a screenshot of the toolbar in action:

In addition to the built-in panels, a number of third-party panels are
contributed by the community. ...

</details>

### dpath

Filesystem-like pathing and searching for dictionaries

`pip install dpath` · installs (wheel) · licence: MIT License · rank 1265 · last release 2024-06-12 · [PyPI](https://pypi.org/project/dpath/)

<details><summary>README extract</summary>

A python library for accessing and searching dictionaries via
/slashed/paths ala xpath

Basically it lets you glob over a dictionary as if it were a filesystem.
It allows you to specify globs (ala the bash eglob syntax, through some
advanced fnmatch.fnmatch magic) to access dictionary elements, and
provides some facility for filtering those ...

Example:
```python
>>> help(dpath.set)
Help on function set in module dpath:

set(obj, glob, value)
Given a path glob, set all existing elements in the document
to the given value. Returns the number of elements changed.

>>> dpath.set(x, 'a/b/[cd]', 'Waffles')
2
>>> print(json.dumps(x, indent=4, sort_keys=True))
{
    "a": {
        "b": {
            "3": 2,
...
```

...

</details>

### statsd

A simple statsd client.

`pip install statsd` · installs (wheel) · licence: MIT License · rank 1270 · last release 2022-11-06 · [PyPI](https://pypi.org/project/statsd/)

<details><summary>README extract</summary>

statsd is a friendly front-end to Graphite. This is a Python client
for the statsd daemon.

:Code:
:License: MIT; see LICENSE file
:Issues:
:Documentation:

Quickly, to use:

You can also add a prefix to all your stats:

Example:
```python
>>> import statsd
>>> c = statsd.StatsClient('localhost', 8125)
>>> c.incr('foo')  # Increment the 'foo' counter.
>>> c.timing('stats.timed', 320)  # Record a 320ms 'stats.timed'.
```

Sections: A Python statsd client, Docs

</details>

### pytzdata

The Olson timezone database for Python.

`pip install pytzdata` · installs (wheel) · licence: MIT License · rank 1275 · last release 2020-07-13 · [PyPI](https://pypi.org/project/pytzdata/) · [source](https://github.com/sdispater/pytzdata)

<details><summary>README extract</summary>

The Olson timezone database for Python.

Supports Python 2.7+ and 3.5+.

Example:
```python
from pytzdata import tz_file

with tz_file('Europe/Paris') as f:
    # Do something with the file
```

Sections: Pytzdata, Usage, Resources

</details>

### agent-detector

Detect AI coding agents from their execution environment or User-Agent

`pip install agent-detector` · installs (wheel) · licence: MIT · rank 1277 · last release 2026-09-02 · [PyPI](https://pypi.org/project/agent-detector/) · [source](https://github.com/patrick91/agent-detector)

<details><summary>README extract</summary>

`agent-detector` is a small, dependency-free Python package for detecting which
AI coding agent is driving the current process, and for parsing that identity
back out of a `User-Agent` header on the receiving side.

It returns evidence rather than only a boolean, so callers can distinguish an
explicit identity from a broad environmental hint.

Example:
```python
from agent_detector import detect_agent

detection = detect_agent()

if detection:
    print(detection.agent)       # "codex"
    print(detection.confidence)  # "high"
    print(detection.signal)      # "CODEX_THREAD_ID"
```

Sections: Agent Detector, Usage, User-Agent propagation, Important limitations, Privacy

</details>

### dagster

Dagster is an orchestration platform for the development, production, and observation of data assets.

`pip install dagster` · installs (wheel) · licence: Apache-2.0 · rank 1280 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster/) · [docs](https://docs.dagster.io) · [source](https://github.com/dagster-io/dagster)

<details><summary>README extract</summary>

Dagster is a cloud-native data pipeline orchestrator for the whole development lifecycle, with integrated lineage and observability, a declarative programming model, and best-in-class testability.

It is designed for developing and maintaining data assets, such as tables, data sets, machine learning models, and reports. ...

Example:
```python
import dagster as dg
import pandas as pd

from sklearn.linear_model import LinearRegression

@dg.asset
def country_populations() -> pd.DataFrame:
    df = pd.read_html("
    df.columns = ["country", "pop2022", "pop2023", "change", "continent", "region"]
    df["change"] = df["change"].str.rstrip("%").astype("float")
    return df

@dg.asset
...
```

...

</details>

### korean-lunar-calendar

Convert the Korean lunar calendar to/from the Gregorian solar calendar (KARI standard).

`pip install korean-lunar-calendar` · installs (wheel) · licence: MIT · rank 1285 · last release 2026-06-15 · [PyPI](https://pypi.org/project/korean-lunar-calendar/) · [source](https://github.com/usingsky/korean_lunar_calendar_py)

<details><summary>README extract</summary>

Convert between the Korean lunar calendar (음력) and the
 Gregorian solar calendar (양력) — entirely offline, following the
 KARI (Korea Astronomy and Space Science Institute) standard.

> The Korean and Chinese lunar calendars share the same astronomical basis but can fall on
> different dates. This library uses the Korean (KARI) standard.

Features:
- Two-way conversion — solar → lunar and lunar → solar.
- Offline — the conversion table is bundled; no network calls, no external services.
- GapJa (간지) strings — the sexagenary year/month/day in both Korean (정유년 병오월) and Chinese (丁酉年 丙午月). ...

Example:
```python
calendar = KoreanLunarCalendar()

# setSolarDate(year, month, day) -> bool
calendar.setSolarDate(2017, 6, 24)

print(calendar.LunarIsoFormat())        # 2017-05-01 Intercalation
...

</details>

### apprise

Push Notifications that work with just about every platform!

`pip install apprise` · installs (wheel) · licence: BSD-2-Clause · rank 1287 · last release 2026-11-08 · [PyPI](https://pypi.org/project/apprise/) · [docs](https://appriseit.com) · [source](https://github.com/caronc/apprise)

<details><summary>README extract</summary>

ap·prise / *verb*

To inform or tell (someone). To make one aware of something.

*Apprise* allows you to send a notification to *almost* all of the most popular *notification* services available to us today such as: Telegram, Discord, Slack, Amazon SNS, Gotify, etc.

* One notification library to rule them all. ...

Example:
```python
from apprise.decorators import notify

# The below assumes you want to catch foobar:// calls:

@notify(on="foobar", name="My Custom Foobar Plugin")
def my_custom_notification_wrapper(body, title, notify_type, *args, **kwargs):
    """My custom notification function that triggers on all foobar:// calls
    """
...
```

...

</details>

### txaio

Compatibility API between asyncio/Twisted/Trollius

`pip install txaio` · installs (wheel) · licence: MIT · rank 1327 · last release 2026-06-18 · [PyPI](https://pypi.org/project/txaio/) · [docs](https://txaio.readthedocs.io/) · [source](https://github.com/crossbario/txaio)

<details><summary>README extract</summary>

txaio is a helper library for writing code that runs unmodified on
both Twisted and
asyncio /
Trollius.

This is like six, but for wrapping over
differences between Twisted and asyncio so one can write code that runs
unmodified on both (aka *source code compatibility*). ...

Example:
```python
import txaio
txaio.use_twisted()  # or .use_asyncio()

f0 = txaio.create_future()
f1 = txaio.as_future(some_func, 1, 2, key='word')
txaio.add_callbacks(f0, callback, errback)
txaio.add_callbacks(f1, callback, errback)
# ...
txaio.resolve(f0, "value")
txaio.reject(f1, RuntimeError("it failed"))
```

Sections: txaio, How it works, AI Policy

</details>

### atpublic

Keep all y'all's __all__'s in sync

`pip install atpublic` · installs (wheel) · licence: Apache Software License · rank 1333 · last release 2026-10-13 · [PyPI](https://pypi.org/project/atpublic/) · [docs](https://public.readthedocs.io) · [source](https://gitlab.com/flufl/public.git)

<details><summary>README extract</summary>

This library provides two very simple decorators that document the public visibility of the names in
your module. They keep your module's `all in sync so you don't have to.

Also included is a function that you can put at the bottom of your module to simply infer all the
public names, and populate the _all__` for you.

Sections: @public and @private, Project details

</details>

### protobuf3-to-dict

Ben Hodgson: A teeny Python library for creating Python dicts from protocol buffers and the reverse. Useful as an intermediate step before serialisation (e.g. to JSON). Kapor: upgrade it to PB3 and PY3, rename it to protobuf3-to-dict

`pip install protobuf3-to-dict` · installs from source (sdist only) · licence: Public Domain · rank 1337 · last release 2017-02-23 · [PyPI](https://pypi.org/project/protobuf3-to-dict/)

### etils

Collection of common python utils

`pip install etils` · installs (wheel) · licence: Apache Software License · rank 1342 · last release 2026-11-02 · [PyPI](https://pypi.org/project/etils/) · [docs](https://etils.readthedocs.io) · [source](https://github.com/google/etils)

<details><summary>README extract</summary>

etils (eclectic utils) is an open-source collection of utils for python.

Each top-level submodule is a self-contained independent module (with its
own `BUILD` rule), meant to be imported individually. To avoid collisions with
other modules/variables, module names are prefixed by `e` (arbitrary
convention): ...

Example:
```python
from etils import epath  # Path utils
from etils import epy  # Python utils
from etils import ejax  # Jax utils
...
```

Sections: Etils, Documentation

</details>

### jsii

Python client for jsii runtime

`pip install jsii` · installs (wheel) · licence: Apache Software License · rank 1344 · last release 2026-10-20 · [PyPI](https://pypi.org/project/jsii/) · [source](https://github.com/aws/jsii.git)

<details><summary>README extract</summary>

Features:
`jsii` allows code in any language to naturally interact with JavaScript classes. It is the technology that enables the
AWS Cloud Development Kit to deliver polyglot libraries from a single codebase! ...

Sections: Overview, question: Documentation, book: Blog Posts

</details>

### ezdxf

A Python package to create/manipulate DXF drawings.

`pip install ezdxf` · installs (wheel) · licence: MIT License · rank 1346 · last release 2026-10-16 · [PyPI](https://pypi.org/project/ezdxf/) · [docs](https://ezdxf.readthedocs.io) · [source](https://github.com/mozman/ezdxf)

<details><summary>README extract</summary>

This Python package is designed to facilitate the creation and manipulation of DXF
documents, with compatibility across various DXF versions. It empowers users to
seamlessly load and edit DXF files while preserving all content, except for comments. ...

Example:
```python
import ezdxf
from ezdxf import colors
from ezdxf.enums import TextEntityAlignment

# Create a new DXF document.
doc = ezdxf.new(dxfversion="R2010")

# Create new table entries (layers, linetypes, text styles, ...).
doc.layers.add("TEXTLAYER", color=colors.RED)

# DXF entities (LINE, TEXT, ...) reside in a layout (modelspace,
...
```

Sections: ezdxf, Abstract, Quick-Info, Included Extensions, Command Line, Website, Documentation, Knowledge Graph, Feedback, Contact

</details>

### django-environ

A package that allows you to utilize 12factor inspired environment variables to configure your Django application.

`pip install django-environ` · installs (wheel) · licence: MIT · rank 1374 · last release 2026-06-18 · [PyPI](https://pypi.org/project/django-environ/) · [docs](https://django-environ.readthedocs.org) · [source](https://github.com/joke2k/django-environ)

<details><summary>README extract</summary>

`django-environ` is the Python package that allows you to use
Twelve-factor methodology to configure your
Django application with environment variables.

For that, it gives you an easy way to configure Django application using
environment variables obtained from an environment file and provided by the OS: ...

Features:
Feature requests are welcome. But take a moment to find out whether your idea
fits with the scope and aims of the project. It's up to *you* to make a strong
case to convince the project's developers of the merits of this feature. ...

Example:
```python
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(file)))

...

</details>

### auth0-python

Auth0 Python SDK - Management and Authentication APIs

`pip install auth0-python` · installs (wheel) · licence: MIT License · rank 1378 · last release 2026-11-04 · [PyPI](https://pypi.org/project/auth0-python/) · [source](https://github.com/auth0/auth0-python)

<details><summary>README extract</summary>

The Auth0 Python library provides convenient access to the Auth0 APIs from Python.

Example:
```python
from auth0.authentication import GetToken

token_client = GetToken(
    domain="your-tenant.auth0.com",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

# Get an access token using client credentials
token_response = token_client.client_credentials(
    audience="
)
access_token = token_response["access_token"]
```

Sections: Auth0 Python Library, Reference, Authentication API, Management API, Recommended: Using ManagementClient, Using a Token from the Authentication API, Using the Base Client, Async Client, Exception Handling, Pagination, Advanced, Access Raw Response Data, Retries, Timeouts

</details>

### prefect

Workflow orchestration and management.

`pip install prefect` · installs (wheel) · licence: Apache Software License · rank 1391 · last release 2026-11-06 · [PyPI](https://pypi.org/project/prefect/) · [docs](https://www.prefect.io/docs) · [source](https://github.com/PrefectHQ/prefect)

<details><summary>README extract</summary>

Installation


 Quickstart


 Build workflows


 Deploy workflows


 Agent setup


 Prefect Cloud

Prefect is a workflow orchestration framework for building data pipelines in Python.
It's the simplest way to elevate a script into a production workflow. ...

Example:
```python
from prefect import flow, task
import httpx

@task(log_prints=True)
def get_stars(repo: str):
    url = f"
    count = httpx.get(url).json()["stargazers_count"]
    print(f"{repo} has {count} stars!")

@flow(name="GitHub Stars")
def github_stars(repos: list[str]):
    for repo in repos:
        get_stars(repo)

# run the flow!
if name == "main":
...
```

Sections: Prefect, Getting started, Work with your agent, Prefect Cloud, prefect-client, Stay Informed

</details>

### pytest-sugar

pytest-sugar is a plugin for pytest that changes the default look and feel of pytest (e.g. progressbar, show tests that fail instantly).

`pip install pytest-sugar` · installs (wheel) · licence: BSD License · rank 1400 · last release 2025-08-23 · [PyPI](https://pypi.org/project/pytest-sugar/)

<details><summary>README extract</summary>

This plugin extends pytest by showing failures and errors instantly, adding a progress bar, improving the test results, and making the output look better.

Sections: pytest-sugar ✨, Usage, Requirements, Running on Windows, Similar projects

</details>

### pydash

The kitchen sink of Python utility libraries for doing "stuff" in a functional way. Based on the Lo-Dash Javascript library.

`pip install pydash` · installs (wheel) · licence: MIT · rank 1417 · last release 2026-08-29 · [PyPI](https://pypi.org/project/pydash/) · [docs](https://pydash.readthedocs.org) · [source](https://github.com/dgilland/pydash)

<details><summary>README extract</summary>

The kitchen sink of Python utility libraries for doing "stuff" in a functional way. Based on the Lo-Dash Javascript library.

Looking for a library that is more memory efficient and better suited for large datasets? Check out fnc! It's built around generators and iteration and has iteratee-first function signatures.

Sections: pydash, Note, Links

</details>

### pygtrie

A pure Python trie data structure implementation.

`pip install pygtrie` · installs (wheel) · licence: Apache-2.0 · rank 1420 · last release 2026-09-14 · [PyPI](https://pypi.org/project/pygtrie/)

<details><summary>README extract</summary>

pygtrie is a pure Python implementation of a trie data structure.

Trie data structure, also known
as radix or prefix tree, is a tree associating keys to values where
all the descendants of a node have a common prefix (associated with
that node). ...

Features:
- A full mutable mapping implementation.

- Supports iterating over as well as deleting a subtrie.

- Supports prefix checking as well as shortest and longest prefix
 look-up.

- Extensible for any kind of user-defined keys. ...

Sections: pygtrie, Features

</details>

### funcy

A fancy and practical functional tools

`pip install funcy` · installs (wheel) · licence: BSD License · rank 1422 · last release 2026-09-10 · [PyPI](https://pypi.org/project/funcy/)

<details><summary>README extract</summary>

A collection of fancy functional tools focused on practicality.

Inspired by clojure, underscore and my own abstractions. Keep reading to get an overview
or read the docs.
Or jump directly to cheatsheet.

Works with Python 3.4+ and pypy3.

Features:
Import stuff from funcy to make things happen:

Merge collections of same type
(works for dicts, sets, lists, tuples, iterators and even strings):

Walk through collection, creating its transform (like map but preserves type): ...

Example:
```python
from funcy import whatever, you, need
```

Sections: Funcy, Overview, Dive in, Related Projects, Running tests

</details>

### json-rpc

JSON-RPC transport implementation

`pip install json-rpc` · installs (wheel) · licence: MIT License · rank 1456 · last release 2023-06-11 · [PyPI](https://pypi.org/project/json-rpc/)

<details><summary>README extract</summary>

JSON-RPC2.0 and JSON-RPC1.0 transport specification implementation.
Supports Python 2.6+, Python 3.3+, PyPy. Has optional Django and Flask support. 200+ tests.

Features:
This implementation does not have any transport functionality realization, only protocol.
Any client or server implementation is easy based on current code, but requires transport libraries, such as requests, gevent or zmq, see examples. ...

Example:
```python
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

@dispatcher.add_method
def foobar(**kwargs):
    return kwargs["foo"] + kwargs["bar"]

@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
...
```

...

</details>

### Flask-Limiter

Rate limiting for flask applications

`pip install Flask-Limiter` · installs (wheel) · licence: MIT · rank 1461 · last release 2025-12-06 · [PyPI](https://pypi.org/project/Flask-Limiter/) · [docs](https://flask-limiter.readthedocs.org) · [source](https://github.com/alisaifee/flask-limiter)

<details><summary>README extract</summary>

Flask-Limiter adds rate limiting to Flask applications.

You can configure rate limits at different levels such as:

- Application wide global limits per user
- Default limits per route
- By Blueprints
- By Class-based views
- By individual routes

Flask-Limiter can be configured to fit your application in many ways, including: ...

Example:
```python
# app.py

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(name)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["2 per minute", "1 per second"],
    storage_uri="memory://",
    # Redis
    # storage_uri="redis://localhost:6379",
...
```

...

</details>

### autopep8

A tool that automatically formats Python code to conform to the PEP 8 style guide

`pip install autopep8` · installs (wheel) · licence: MIT License · rank 1465 · last release 2025-01-14 · [PyPI](https://pypi.org/project/autopep8/) · [source](https://github.com/hhatto/autopep8)

<details><summary>README extract</summary>

autopep8 automatically formats Python code to conform to the PEP 8 style
guide. It uses the pycodestyle utility to determine what parts of the code
needs to be formatted. autopep8 is capable of fixing most of the formatting
issues that can be reported by pycodestyle.

Features:
autopep8 fixes the following issues reported by pycodestyle:
autopep8 also fixes some issues not found by pycodestyle.

- Normalize files with mixed line endings.
- Put a blank line between a class docstring and its first method
 declaration. ...

Example:
```python
import math, sys;

def example1():
    ####This is a long comment. This should be wrapped to fit within 72 characters.
    some_tuple=(   1,2, 3,'a'  );
    some_variable={'long':'Long code lines should be wrapped within 79 characters.',
...

</details>

### elementpath

XPath 1.0/2.0/3.0/3.1 parsers and selectors for ElementTree and lxml

`pip install elementpath` · installs (wheel) · licence: MIT · rank 1470 · last release 2026-08-08 · [PyPI](https://pypi.org/project/elementpath/)

<details><summary>README extract</summary>

The proposal of this package is to provide XPath 1.0, 2.0, 3.0 and 3.1
selectors for ElementTree XML data structures, both for the standard
ElementTree library and for the lxml.etree library.

For lxml.etree this package can be useful for providing
XPath 2.0/3.0/3.1 selectors, because lxml.etree already
has it's own implementation of XPath 1.0.

Sections: elementpath, About parsers

</details>

### pyluach

A Python package for dealing with Hebrew (Jewish) calendar dates.

`pip install pyluach` · installs (wheel) · licence: MIT License · rank 1488 · last release 2025-09-09 · [PyPI](https://pypi.org/project/pyluach/) · [docs](https://readthedocs.org/projects/pyluach/) · [source](https://github.com/simlist/pyluach)

<details><summary>README extract</summary>

Pyluach is a Python package for dealing with Hebrew (Jewish) calendar dates.

Features:
* Conversion between Hebrew and Gregorian dates
* Finding the difference between two dates
* Finding a date at a given duration from the given date
* Rich comparisons between dates
* Finding the weekday of a given date
* Finding the weekly Parsha ...

Example:
```python
>>> from pyluach import dates, hebrewcal, parshios

>>> today = dates.HebrewDate.today()
>>> lastweek_gregorian = (today - 7).to_greg()
>>> lastweek_gregorian < today
True
>>> today - lastweek_gregorian
7
>>> greg = dates.GregorianDate(1986, 3, 21)
>>> heb = dates.HebrewDate(5746, 13, 10)
>>> greg == heb
True

...
```

Sections: pyluach, Features, Documentation, Examples, Contact

</details>

### aniso8601

A library for parsing ISO 8601 strings.

`pip install aniso8601` · installs (wheel) · licence: BSD License · rank 1493 · last release 2025-04-18 · [PyPI](https://pypi.org/project/aniso8601/) · [docs](https://aniso8601.readthedocs.io/) · [source](https://codeberg.org/nielsenb-jf/aniso8601)

<details><summary>README extract</summary>

Features:
* Pure Python implementation
* Logical behavior

 - Parse a time, get a datetime.time
 - Parse a date, get a datetime.date
 - Parse a datetime, get a datetime.datetime
 - Parse a duration, get a datetime.timedelta
 - Parse an interval, get a tuple ...

Example:
```python
>>> import aniso8601
>>> aniso8601.parse_datetime('1977-06-10T12:00:00Z')
datetime.datetime(1977, 6, 10, 12, 0, tzinfo=+0:00:00 UTC)
```

Sections: aniso8601, Another ISO 8601 parser for Python, Features, Use, Parsing datetimes, Parsing dates, Parsing times, Parsing durations, Parsing intervals, Builders, TupleBuilder, Datetimes, Dates, Times

</details>

### pefile

Python PE parsing module

`pip install pefile` · installs (wheel) · licence: MIT · rank 1509 · last release 2024-08-26 · [PyPI](https://pypi.org/project/pefile/)

<details><summary>README extract</summary>

pefile, Portable Executable reader module

All the PE file basic structures are available with their default names as
attributes of the instance returned.

Processed elements such as the import table are made available with lowercase
names, to differentiate them from the upper case basic structure names. ...

</details>

### flexparser

Parsing made fun ... using typing.

`pip install flexparser` · installs (wheel) · licence: BSD License · rank 1510 · last release 2024-11-07 · [PyPI](https://pypi.org/project/flexparser/)

<details><summary>README extract</summary>

Why write another parser? I have asked myself the same question while
working on this project. It is clear that there are excellent parsers out
there but I wanted to experiment with another way of writing them.

The idea is quite simple. You write a class for every type of content
(called here `ParsedStatement`) you need to parse. ...

Example:
```python
from dataclasses import dataclass

import flexparser as fp

@dataclass(frozen=True)
class Assigment(fp.ParsedStatement):
    """Parses the following `this <- other`
    """

    lhs: str
    rhs: str

    @classmethod
    def from_string(cls, s):
        lhs, rhs = s.split("<-")
        return cls(lhs.strip(), rhs.strip())
```

...

</details>

### bashlex

Python parser for bash

`pip install bashlex` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 1511 · last release 2023-01-18 · [PyPI](https://pypi.org/project/bashlex/)

_README extract left out: share-alike licence._

### flexcache

Saves and loads to the cache a transformed versions of a source object.

`pip install flexcache` · installs (wheel) · licence: BSD License · rank 1512 · last release 2024-03-09 · [PyPI](https://pypi.org/project/flexcache/)

<details><summary>README extract</summary>

An robust and extensible package to cache on disk the result of expensive
calculations.

Consider an expensive function `parse` that takes a path and returns a
parsed version:

It would be nice to automatically and persistently cache this result and
this is where flexcache comes in.

First, we create a `DiskCache` object:

and then is loaded: ...

Example:
```python
>>> content = parse("source.txt")
```

Sections: flexcache, Building your own caching logic, Headers, Invalidate, Naming

</details>

### dataclasses

A backport of the dataclasses module for Python 3.6

`pip install dataclasses` · does not install on CPython 3.14 · licence: Apache Software License · rank 1521 · last release 2020-11-13 · [PyPI](https://pypi.org/project/dataclasses/)

<details><summary>README extract</summary>

This is an implementation of PEP 557, Data Classes. It is a backport
for Python 3.6. Because dataclasses will be included in Python 3.7,
any discussion of dataclass features should occur on the python-dev
mailing list at
At this point this repo should only be used for historical purposes
(it's where the original dataclasses discussions took place) ...

Example:
```python
from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

item = InventoryItem('hammers', 10.49, 12)
print(item.total_cost())
```

Sections: Example Usage, Compatibility

</details>

### python-decouple

Strict separation of settings from code.

`pip install python-decouple` · installs (wheel) · licence: MIT License · rank 1525 · last release 2023-03-01 · [PyPI](https://pypi.org/project/python-decouple/)

<details><summary>README extract</summary>

*Decouple* helps you to organize your settings so that you can
change parameters without having to redeploy your app.

It also makes it easy for you to:

Features:
The settings files in web frameworks store many different kinds of parameters:

* Locale and i18n;
* Middlewares and Installed Apps;
* Resource handles to the database, Memcached, and other backing services;
* Credentials to external services such ...

Example:
```python
# coding: utf-8
from decouple import config
from unipath import Path
from dj_database_url import parse as db_url

BASE_DIR = Path(file).parent

DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + BASE_DIR.child('db.sqlite3'),
...
```

...

</details>

### xmlschema

An XML Schema validator and decoder

`pip install xmlschema` · installs (wheel) · licence: MIT · rank 1527 · last release 2026-06-30 · [PyPI](https://pypi.org/project/xmlschema/)

<details><summary>README extract</summary>

The *xmlschema* library is an implementation of XML Schema
for Python.

This library arises from the needs of a solid Python layer for processing XML
Schema based files for
MaX (Materials design at the Exascale) European project.
A significant problem is the encoding and the decoding of the XML data files
produced by different simulation software. ...

Features:
This library includes the following features:

* Full XSD 1.0 and XSD 1.1 support
* Building of XML schema objects from XSD files
* Validation of XML instances against XSD schemas
* Decoding of XML data into Python data and to JSON
* Encoding of ...

Example:
```python
>>> import xmlschema
>>> my_schema = xmlschema.XMLSchema('tests/test_cases/examples/vehicles/vehicles.xsd')
```

Sections: xmlschema, Features, Usage

</details>

### pytest-testmon

selects tests affected by changed files and methods

`pip install pytest-testmon` · installs (wheel) · licence: MIT · rank 1551 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pytest-testmon/) · [source](https://github.com/tarpas/pytest-testmon)

<details><summary>README extract</summary>

This is a pytest plug-in which automatically selects and re-executes
only tests affected by recent changes. How is this possible in dynamic
language like Python and how reliable is it? Read here: Determining
affected tests

</details>

### strawberry-graphql

A library for creating GraphQL APIs

`pip install strawberry-graphql` · installs (wheel) · licence: MIT · rank 1553 · last release 2026-11-07 · [PyPI](https://pypi.org/project/strawberry-graphql/) · [docs](https://strawberry.rocks/) · [source](https://github.com/strawberry-graphql/strawberry)

<details><summary>README extract</summary>

> Python GraphQL library based on dataclasses

Example:
```python
import strawberry

@strawberry.type
class User:
    name: str
    age: int

@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)

schema = strawberry.Schema(query=Query)
```

Sections: Strawberry GraphQL, Getting Started, Type-checking, Django Integration, Examples, Pre commit, Links, Licensing

</details>

### pyahocorasick

pyahocorasick is a fast and memory efficient library for exact or approximate multi-pattern string search. With the ``ahocorasick.Automaton`` class, you can find multiple key string occurrences at once in some input text. You can use it as a plain dict-like Trie or convert a Trie to an automaton for efficient Aho-Corasick search. And pickle to disk for easy reuse of large automatons. Implemented in C and tested on Python 3.6+. Works on Linux, macOS and Windows. BSD-3-Cause license.

`pip install pyahocorasick` · installs (wheel) · licence: BSD-3-Clause and Public-Domain · rank 1559 · last release 2026-04-27 · [PyPI](https://pypi.org/project/pyahocorasick/)

<details><summary>README extract</summary>

pyahocorasick is a fast and memory efficient library for exact or approximate
multi-pattern string search meaning that you can find multiple key strings
occurrences at once in some input text. The strings "index" can be built ahead
of time and saved (as a pickle) to disk to reload and reuse later. ...

Example:
```python
>>> import ahocorasick
>>> automaton = ahocorasick.Automaton()
```

Sections: pyahocorasick, Testimonials, Download and source code, Quick start, Documentation, Unicode and bytes

</details>

### anytree

Powerful and Lightweight Python Tree Data Structure with various plugins

`pip install anytree` · installs (wheel) · licence: not stated · rank 1573 · last release 2025-04-08 · [PyPI](https://pypi.org/project/anytree/) · [docs](https://anytree.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

* Documentation
* PyPI
* GitHub
* Changelog
* Issues
* Contributors
* If you enjoy anytree

Sections: Links, Getting started, Documentation

</details>

### webdriver-manager

Library provides the way to automatically manage drivers for different browsers

`pip install webdriver-manager` · installs (wheel) · licence: Apache-2.0 · rank 1578 · last release 2026-06-04 · [PyPI](https://pypi.org/project/webdriver-manager/) · [source](https://github.com/SergeyPirogov/webdriver_manager)

<details><summary>README extract</summary>

`webdriver-manager` is a Python library for explicit browser driver management.

It helps download, resolve, cache, and reuse driver binaries for browser automation with Selenium. Instead of downloading a driver manually, unpacking it, and hardcoding a path, you can install the required driver directly from Python code. ...

Example:
```python
from selenium import webdriver

driver = webdriver.Chrome()
```

Sections: Webdriver Manager for Python, When should I use webdriver-manager?, Selenium Manager vs webdriver-manager, Environment scope, Usage, Use with Chrome, Selenium 4, Selenium 3, Use with Chromium, Use with Brave

</details>

### numcodecs

A Python package providing buffer compression and transformation codecs for use in data storage and communication applications.

`pip install numcodecs` · installs (wheel) · licence: MIT · rank 1592 · last release 2026-10-20 · [PyPI](https://pypi.org/project/numcodecs/) · [docs](https://numcodecs.readthedocs.io/)

<details><summary>README extract</summary>

Numcodecs is a Python package providing buffer compression and transformation
codecs for use in data storage and communication applications.

</details>

### addict

Addict is a dictionary whose items can be set using both attribute and item syntax.

`pip install addict` · installs (wheel) · licence: MIT License · rank 1596 · last release 2020-11-21 · [PyPI](https://pypi.org/project/addict/)

<details><summary>README extract</summary>

Addict is a module that exposes a dictionary subclass that allows items to be set like attributes. Values are gettable and settable using both attribute and item syntax. For more info check out the README at 'github.com/mewwts/addict'.

</details>

### ciso8601

Fast ISO8601 date time parser for Python written in C

`pip install ciso8601` · installs (wheel) · licence: MIT License · rank 1604 · last release 2025-08-20 · [PyPI](https://pypi.org/project/ciso8601/)

<details><summary>README extract</summary>

`ciso8601` converts ISO 8601 or RFC 3339 date time strings into Python datetime objects.

Since it's written as a C module, it is much faster than other Python libraries.
Tested with cPython 2.7, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14. ...

Example:
```python
In [1]: import ciso8601

In [2]: ciso8601.parse_datetime('2014-12-05T12:30:45.123456-05:30')
Out[2]: datetime.datetime(2014, 12, 5, 12, 30, 45, 123456, tzinfo=pytz.FixedOffset(330))

In [3]: ciso8601.parse_datetime('20141205T123045')
Out[3]: datetime.datetime(2014, 12, 5, 12, 30, 45)
```

...

</details>

### turbopuffer

The official Python library for the turbopuffer API

`pip install turbopuffer` · installs (wheel) · licence: MIT License · rank 1605 · last release 2026-10-28 · [PyPI](https://pypi.org/project/turbopuffer/) · [source](https://github.com/turbopuffer/turbopuffer-python)

<details><summary>README extract</summary>

The turbopuffer Python library provides convenient access to the turbopuffer HTTP API from any Python 3.11+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx2.

It is generated with Stainless. ...

Example:
```python
import os
from turbopuffer import Turbopuffer

tpuf = Turbopuffer(
    # Pick the right region
    region="gcp-us-central1",
    # This is the default and can be omitted
    api_key=os.environ.get("TURBOPUFFER_API_KEY"),
)

ns = tpuf.namespace("example")

# Query nearest neighbors with a vector.
vector_result = ns.query(
...
```

...

</details>

### enum-compat

enum/enum34 compatibility package

`pip install enum-compat` · installs (wheel) · licence: MIT · rank 1618 · last release 2019-10-14 · [PyPI](https://pypi.org/project/enum-compat/)

<details><summary>README extract</summary>

This is a virtual package, its whole purpose is to install enum34 on
Python older than 3.4. On Python 3.4+ it's a no-op.

</details>

### func-timeout

Python module which allows you to specify timeouts when calling any existing function. Also provides support for stoppable-threads

`pip install func-timeout` · installs from source (sdist only) · licence: GNU Lesser General Public License v2 (LGPLv2) · rank 1621 · last release 2019-08-19 · [PyPI](https://pypi.org/project/func-timeout/)

_README extract left out: share-alike licence._

### Expression

Practical functional programming for Python 3.10+

`pip install Expression` · installs (wheel) · licence: MIT · rank 1622 · last release 2026-10-29 · [PyPI](https://pypi.org/project/Expression/)

<details><summary>README extract</summary>

> Pragmatic functional programming

Expression aims to be a solid, type-safe, pragmatic, and high performance library for
frictionless and practical functional programming in Python 3.10+. ...

Example:
```python
from expression import pipe
from expression.collections import seq

total = pipe(
    [4, 7, 12, 15],
    seq.filter(lambda score: score >= 10),
    seq.map(lambda score: score * 2),
    seq.sum,
)

assert total == 54
```

Sections: Expression, Getting Started, Start with a practical workflow, Goals, Pipelining, Composition, Fluent and Functional, Fluent syntax, Functional syntax, Option, Option as an effect, Option as an applicative, Result, AsyncResult

</details>

### dirtyjson

JSON decoder for Python that can extract data from the muck

`pip install dirtyjson` · installs (wheel) · licence: Academic Free License (AFL); MIT License · rank 1646 · last release 2022-11-28 · [PyPI](https://pypi.org/project/dirtyjson/)

<details><summary>README extract</summary>

JSON (JavaScript Object Notation) < is a subset of JavaScript
syntax (ECMA-262 3rd edition) used as a lightweight data interchange format.

`dirtyjson` is a JSON decoder meant for extracting JSON-type data from .js
files. The returned data structure includes information about line and column
numbers, so you can output more useful error messages. ...

Example:
```python
>>> import dirtyjson
>>> obj = [u'foo', {u'bar': [u'baz', None, 1.0, 2]}]
>>> d = dirtyjson.loads("""["foo", /* not fu*/ {bar: ['baz', null, 1.0, 2,]}] and then ignore this junk""")
>>> d == obj
True
>>> pos = d.attributes(0)  # line/column position of first element in array
>>> pos.line == 1
True
>>> pos.column == 2
True
...
```

...

</details>

### lru-dict

An Dict like LRU container.

`pip install lru-dict` · installs (wheel) · licence: MIT · rank 1652 · last release 2025-11-02 · [PyPI](https://pypi.org/project/lru-dict/)

<details><summary>README extract</summary>

Note: This project is stable and production ready, but looking for a lead maintainer. Preferably someone who uses this library and made contributions to it.

A fixed size dict like container which evicts Least Recently Used (LRU) items
once size limit is exceeded. There are many python implementations available
which does similar things. ...

Example:
```python
from lru import LRU
l = LRU(5)         # Create an LRU container that can hold 5 items

print l.peek_first_item(), l.peek_last_item()  #return the MRU key and LRU key
# Would print None None

for i in range(5):
   l[i] = str(i)
print l.items()    # Prints items in MRU order
# Would print [(4, '4'), (3, '3'), (2, '2'), (1, '1'), (0, '0')]

...
```

Sections: LRU Dict, Usage, When to use this

</details>

### zarr

An implementation of chunked, compressed, N-dimensional arrays for Python

`pip install zarr` · installs (wheel) · licence: MIT · rank 1654 · last release 2026-10-27 · [PyPI](https://pypi.org/project/zarr/) · [docs](https://zarr.readthedocs.io/)

<details><summary>README extract</summary>

The `zarr` library is a Python implementation of the Zarr storage format. `zarr` delivers compressed, chunked, N-dimensional arrays that work well for parallel computing and object storage. See the documentation for more information.

- Create N-dimensional arrays with NumPy-compatible `dtype`s.
- Chunk arrays along any dimension. ...

Sections: Zarr, What is it?, Main Features, Where to get it, Repository sub-packages

</details>

### databricks-labs-dqx

Data Quality eXtended (DQX) is a Python library for data quality checks and data quality monitoring

`pip install databricks-labs-dqx` · does not install on CPython 3.14 · licence: Other/Proprietary License · rank 1656 · last release 2026-11-06 · [PyPI](https://pypi.org/project/databricks-labs-dqx/) · [source](https://github.com/databrickslabs/dqx)

<details><summary>README extract</summary>

Simplified Data Quality checking at Scale for PySpark Workloads on streaming and standard DataFrames.

- Rule-based quality checks — 80+ built-in checks (null, range, regex, referential, aggregate, geo, PII, and more) for row-level and column/dataset-level validation, with support for custom check functions. ...

Sections: DQX by Databricks Labs, ✨ Key capabilities, 📖 Documentation

</details>

### diff-match-patch

Repackaging of Google's Diff Match and Patch libraries.

`pip install diff-match-patch` · installs (wheel) · licence: Apache Software License · rank 1689 · last release 2024-10-21 · [PyPI](https://pypi.org/project/diff-match-patch/) · [source](https://github.com/diff-match-patch-python/diff-match-patch)

<details><summary>README extract</summary>

Google's Diff Match and Patch library, packaged for modern Python.

Since August 2024, Googles diff-match-patch library is archived, and
this project will now track the maintained fork.

Example:
```python
from diff_match_patch import diff_match_patch

dmp = diff_match_patch()
patches = dmp.patch_make(text1, text2)
diff = dmp.patch_toText(patches)
```

Sections: diff-match-patch, Usage, Original README, Reference, Languages, Algorithms

</details>

### urwid

A full-featured console (xterm et al.) user interface library

`pip install urwid` · installs (wheel) · licence: LGPL-2.1-only · rank 1692 · last release 2026-11-06 · [PyPI](https://pypi.org/project/urwid/) · [docs](https://urwid.org/manual/index.html) · [source](https://github.com/urwid/urwid)

_README extract left out: share-alike licence._

### arabic-reshaper

Reconstruct Arabic sentences to be used in applications that do not support Arabic

`pip install arabic-reshaper` · installs (wheel) · licence: MIT · rank 1695 · last release 2026-11-02 · [PyPI](https://pypi.org/project/arabic-reshaper/) · [source](https://github.com/mpcabd/python-arabic-reshaper/)

<details><summary>README extract</summary>

Reconstruct Arabic sentences to be used in applications that don't support
Arabic script.

Works with Python 3.x

Arabic script is very special with two essential features:

1. It is written from right to left.
2. The characters change shape according to their surrounding characters. ...

Example:
```python
import arabic_reshaper

text_to_be_reshaped = 'اللغة العربية رائعة'
reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
```

Sections: Python Arabic Reshaper, Description, Usage, Example using PIL Image, Settings, Via ArabicReshaper instance `configuration`, Via ArabicReshaper instance `configuration_file`, Settings based on a TrueType® font, Tashkeel/Harakat issue, Demo, Download, 3.0.1, 3.0.0, 2.1.4

</details>

### cross-web

A library for working with web frameworks

`pip install cross-web` · installs (wheel) · licence: MIT · rank 1703 · last release 2026-11-06 · [PyPI](https://pypi.org/project/cross-web/) · [source](https://github.com/usecross/cross-web)

<details><summary>README extract</summary>

Write once, run everywhere - A universal web framework adapter for Python that lets you write code once and use it across multiple web frameworks.

Features:
Cross provides a unified interface for common web framework operations, allowing you to write framework-agnostic code that can be easily adapted to work with FastAPI, Flask, Django, and other popular Python web frameworks.

Example:
```python
import json

import pytest
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from cross_web.request._starlette import StarletteRequestAdapter
from cross_web.testing.clients.starlette import StarletteHttpClient

...
```

...

</details>

### orderedmultidict

Ordered Multivalue Dictionary

`pip install orderedmultidict` · installs (wheel) · licence: Freely Distributable · rank 1707 · last release 2025-11-18 · [PyPI](https://pypi.org/project/orderedmultidict/)

<details><summary>README extract</summary>

A multivalue dictionary is a dictionary that can store multiple values for the
same key. An ordered multivalue dictionary is a multivalue dictionary that
retains the order of insertions and deletions.

omdict retains method parity with dict.

Information and documentation at

</details>

### myst-parser

An extended [CommonMark](https://spec.commonmark.org/) compliant parser,

`pip install myst-parser` · installs (wheel) · licence: MIT License · rank 1712 · last release 2026-05-13 · [PyPI](https://pypi.org/project/myst-parser/) · [docs](https://myst-parser.readthedocs.io)

<details><summary>README extract</summary>

[][github-link]
[][codecov-link]
[][rtd-link]
[][black-link]
[][pypi-link]
[][conda-link]
[][install-link]

MyST is a rich and extensible flavor of Markdown meant for technical documentation and publishing.

MyST is a flavor of markdown that is designed for simplicity, flexibility, and extensibility. ...

</details>

### tach

A Python tool to maintain a modular package architecture.

`pip install tach` · installs (wheel) · licence: MIT License · rank 1713 · last release 2026-10-06 · [PyPI](https://pypi.org/project/tach/)

<details><summary>README extract</summary>

Tach is a Python tool to enforce dependencies and interfaces, written in Rust.

Tach is inspired by the modular monolith architecture.

Docs

Tach can enforce:

- 📋 Imports only come from declared dependencies
- 🤝 Cross-module calls use the public interface
- ⛓️‍💥 No cycles in the dependency graph

Tach is:

- 🌎 Open source ...

Sections: Tach, Getting Started, Setup, Enforcement, Extras

</details>

### furl

URL manipulation made simple.

`pip install furl` · installs (wheel) · licence: Public Domain · rank 1715 · last release 2025-03-09 · [PyPI](https://pypi.org/project/furl/)

<details><summary>README extract</summary>

manipulating URLs easy.

Python's standard
urllib and
urlparse modules
provide a number of URL related functions, but using these functions to
perform common URL operations proves tedious. Furl makes parsing and
manipulating URLs easy.

Furl is well tested, Unlicensed in the public
domain, and supports Python 3 and PyPy3. ...

Example:
```python
>>> from furl import furl
>>> f = furl('
>>> f /= 'path'
>>> del f.args['one']
>>> f.args['three'] = '3'
>>> f.url
'
```

Sections: furl is a small Python library that makes parsing and, API, Basics, Path, Manipulation, Query, Parameters, Fragment, Encoding, Inline manipulation, Miscellaneous

</details>

### backports.asyncio.runner

Backport of asyncio.Runner, a context manager that controls event loop life cycle.

`pip install backports.asyncio.runner` · does not install on CPython 3.14 · licence: Python Software Foundation License · rank 1722 · last release 2025-07-02 · [PyPI](https://pypi.org/project/backports.asyncio.runner/)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](
[](

This is a backport of Python 3.11 asyncio.Runner, a context manager that simplifies multiple async
function calls in the same context.

This backports provides full compatibility with Python 3.11 `asyncio.Runner` features, including `contextvars.Context` support. ...

Example:
```python
import sys

if sys.version_info < (3, 11):
    from backports.asyncio.runner import Runner
else:
    from asyncio import Runner

async def echo(msg: str) -> None:
    print(f"Hello {msg}")

with Runner() as runner:
    runner.run(echo("World"))

# Hello World
```

Sections: backports.asyncio.runner, uvloop, Caveats, 1.2.0, 1.1.0, 1.0.2, 1.0.1, 1.0.0

</details>

### yapf

A formatter for Python code

`pip install yapf` · installs (wheel) · licence: Apache Software License · rank 1728 · last release 2024-11-14 · [PyPI](https://pypi.org/project/yapf/) · [docs](https://github.com/google/yapf/blob/main/README.md#yapf)

<details><summary>README extract</summary>

YAPF is a Python formatter based on `clang-format`
(developed by Daniel Jasper). In essence, the algorithm takes the code and
calculates the best formatting that conforms to the configured style. It takes
away a lot of the drudgery of maintaining your code. ...

Features:
YAPF tries very hard to get the formatting correct. But for some code, it won't
be as good as hand-formatting. In particular, large data literals may become
horribly disfigured under YAPF.

The reasons for this are manyfold. ...

Example:
```python
x = {  'a':37,'b':42,

'c':927}

y = 'hello ''world'
z = 'hello '+'world'
a = 'hello {}'.format('world')
class foo  (     object  ):
  def f    (self   ):
    return       37*-+2
  def g(self, x,y=42):
      return y
def f  (   a ) :
  return      37+-+a[42-x :  y**3]
```

...

</details>

### dlt

dlt is an open-source python-first scalable data loading library that does not require any backend to run.

`pip install dlt` · installs (wheel) · licence: Apache-2.0 · rank 1733 · last release 2026-10-29 · [PyPI](https://pypi.org/project/dlt/) · [source](https://github.com/dlt-hub/dlt)

<details><summary>README extract</summary>

Be it a Google Colab notebook, AWS Lambda function, an Airflow DAG, your local laptop,
or an AI coding agent—dlt can be dropped in anywhere.

Features:
dlt loads data from messy, often unstructured sources into well-structured, typed datasets. It's a library, not a platform — you `pip install` it into your existing code and keep your workflow and the other tools you already use. ...

Example:
```python
import dlt
from dlt.sources.rest_api import rest_api_source

# 1. Describe the API declaratively
source = rest_api_source({
    "client": {"base_url": "
    "resources": [
        {
          "name": "playlist_tracks",
          "endpoint": {"path": "playlists/{playlist_id}/tracks"},
        },
    ],
})

# 2. Point a pipeline at any destination
...
```

...

</details>

### unittest-xml-reporting

unittest-based test runner with Ant/JUnit like XML reporting.

`pip install unittest-xml-reporting` · installs (wheel) · licence: BSD-2-Clause · rank 1747 · last release 2026-01-07 · [PyPI](https://pypi.org/project/unittest-xml-reporting/)

<details><summary>README extract</summary>

A unittest test runner that can save test results to XML files in xUnit format.
The files can be consumed by a wide range of tools, such as build systems, IDEs
and continuous integration servers.

Example:
```python
import io
import unittest
import xmlrunner

# run the tests storing results in memory
out = io.BytesIO()
unittest.main(
    testRunner=xmlrunner.XMLTestRunner(output=out),
    failfast=False, buffer=False, catchbreak=False, exit=False)
```

Sections: unittest-xml-reporting (aka xmlrunner), Requirements, Jenkins plugins, Jenkins JUnit plugin, Jenkins xUnit plugin version 1.100, Jenkins xUnit plugin version 1.104+, JUnit Schema ?, Command-line, Usage, Reporting to a single file

</details>

### pyhocon

HOCON parser for Python

`pip install pyhocon` · installs from source (sdist only) · licence: Apache Software License · rank 1764 · last release 2026-03-20 · [PyPI](https://pypi.org/project/pyhocon/)

<details><summary>README extract</summary>

pyhocon is a HOCON parser for Python. Additionally we provide a tool (pyhocon) to convert any HOCON content into json, yaml and properties format.

</details>

### configobj

Config file reading, writing and validation.

`pip install configobj` · installs (wheel) · licence: BSD License · rank 1766 · last release 2024-11-26 · [PyPI](https://pypi.org/project/configobj/)

<details><summary>README extract</summary>

ConfigObj is a simple but powerful config file reader and writer: an *ini
file round tripper*. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files.

List of Features ...

</details>

### dynaconf

The dynamic configurator for your Python Project

`pip install dynaconf` · installs (wheel) · licence: MIT License · rank 1776 · last release 2026-08-05 · [PyPI](https://pypi.org/project/dynaconf/)

<details><summary>README extract</summary>

> dynaconf - Configuration Management for Python.

Features:
- Inspired by the 12-factor application guide
- Settings management (default values, validation, parsing, templating)
- Protection of sensitive information (passwords/tokens) ...

Example:
```python
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",  # export envvars with `export DYNACONF_FOO=bar`.
    settings_files=['settings.yaml', '.secrets.yaml'],  # Load files in the given order.
)
```

Sections: Features, Initialize Dynaconf on project root directory, Dynaconf init creates the following files, Using Dynaconf, More

</details>

### PyYAML-ft

YAML parser and emitter for Python with support for free-threading

`pip install PyYAML-ft` · installs from source (sdist only) · licence: MIT License · rank 1781 · last release 2025-06-10 · [PyPI](https://pypi.org/project/PyYAML-ft/) · [docs](https://pyyaml.org/wiki/PyYAMLDocumentation) · [source](https://github.com/Quansight-Labs/pyyaml-ft)

<details><summary>README extract</summary>

A full-featured YAML processing framework for Python with support for free-threading

Features:
PEP 703 introduced free-threaded Python as a
separate build of CPython 3.13. Thread-safety issues that might have otherwise gone
unnoticed are now much easier to trigger because of the absence of protection from
the GIL. ...

Example:
```python
import io
import threading
import yaml_ft as yaml

class Dice:
    def init(self, first, second):
        self.first = first
        self.second = second
    def repr(self):
        return f"Dice({self.first}, {self.second})"

def construct_dice(constructor, node):
    mapping = constructor.construct_mapping(node)
    return Dice(**mapping)

...
```

...

</details>

### libtmux

Typed library that provides an ORM wrapper for tmux, a terminal multiplexer.

`pip install libtmux` · installs (wheel) · licence: MIT License · rank 1789 · last release 2026-07-12 · [PyPI](https://pypi.org/project/libtmux/) · [docs](https://libtmux.git-pull.com) · [source](https://github.com/tmux-python/libtmux)

<details><summary>README extract</summary>

Drive tmux from Python: typed, object-oriented control over servers, sessions, windows, and panes.

libtmux is a typed Python API over [tmux], the terminal multiplexer. Stop shelling out and parsing `tmux ls`. Instead, interact with real Python objects: `Server`, `Session`, `Window`, and `Pane`. ...

Example:
```python
>>> import libtmux
>>> svr = libtmux.Server()
>>> svr
Server(socket_path=/tmp/tmux-.../default)
```

Sections: ⚙️ libtmux, 🐍 What is libtmux?, ✨ Features, 🚀 Quickstart, Open a tmux session, Pilot your tmux session via Python, Run any tmux command, List and filter sessions, Control sessions and windows, Split windows and send keys, Capture pane output, Traverse the hierarchy, Know where you're running, Core concepts

</details>

### reductoai

The official Python library for the reducto API

`pip install reductoai` · installs (wheel) · licence: Apache Software License · rank 1806 · last release 2026-11-04 · [PyPI](https://pypi.org/project/reductoai/) · [source](https://github.com/reductoai/reducto-python-sdk)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Reducto Python library provides convenient access to the Reducto REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx. ...

Example:
```python
import os
from reducto import Reducto

client = Reducto(
    api_key=os.environ.get("REDUCTO_API_KEY"),  # This is the default and can be omitted
    # or 'production' | 'au'; defaults to "production".
    environment="eu",
)

response = client.parse.run(
    input="
)
```

...

</details>

### janus

Mixed sync-async queue to interoperate between asyncio tasks and classic threads

`pip install janus` · installs (wheel) · licence: Apache Software License · rank 1808 · last release 2024-12-13 · [PyPI](https://pypi.org/project/janus/)

<details><summary>README extract</summary>

Mixed sync-async queue, supposed to be used for communicating between
classic synchronous (threaded) code and asynchronous (in terms of
asyncio) one.

Like Janus god the queue
object from the library has two faces: synchronous and asynchronous
interface. ...

Example:
```python
import asyncio
import janus

def threaded(sync_q: janus.SyncQueue[int]) -> None:
    for i in range(100):
        sync_q.put(i)
    sync_q.join()

async def async_coro(async_q: janus.AsyncQueue[int]) -> None:
    for i in range(100):
        val = await async_q.get()
        assert val == i
        async_q.task_done()

async def main() -> None:
...
```

Sections: janus, Usage, Example, Limitations, Communication channels, Thanks

</details>

### Flask-JWT-Extended

Extended JWT integration with Flask

`pip install Flask-JWT-Extended` · installs (wheel) · licence: MIT License · rank 1829 · last release 2026-05-13 · [PyPI](https://pypi.org/project/Flask-JWT-Extended/)

<details><summary>README extract</summary>

Features:
Flask-JWT-Extended not only adds support for using JSON Web Tokens (JWT) to Flask for protecting routes,
but also many helpful (and optional) features built in to make working with JSON Web Tokens
easier. These include: ...

Sections: Flask-JWT-Extended, Features, Usage, Upgrading from 3.x.x to 4.0.0, Chatting

</details>

### multimethod

Multiple argument dispatching.

`pip install multimethod` · installs (wheel) · licence: Apache-2.0 · rank 1833 · last release 2026-07-29 · [PyPI](https://pypi.org/project/multimethod/) · [docs](https://coady.github.io/multimethod)

<details><summary>README extract</summary>

Multimethod provides a decorator for adding multiple argument dispatching to functions. The decorator creates a multimethod object as needed, and registers the function with its annotations.

There are several multiple dispatch libraries on PyPI. This one aims for simplicity and speed. ...

Example:
```python
from multimethod import multimethod

@multimethod
def func(x: int, y: float): ...
```

Sections: Usage, multimethod, multidispatch, instance checks, classes, Tests

</details>

### mirakuru

Process executor (not only) for tests.

`pip install mirakuru` · installs (wheel) · licence: LGPL-3.0-or-later · rank 1861 · last release 2026-11-03 · [PyPI](https://pypi.org/project/mirakuru/) · [source](https://github.com/dbfixtures/mirakuru)

_README extract left out: share-alike licence._

### bitstring

Simple construction, analysis and modification of binary data: bit arrays, bitfields and unaligned binary formats.

`pip install bitstring` · installs (wheel) · licence: MIT License · rank 1886 · last release 2026-10-11 · [PyPI](https://pypi.org/project/bitstring/) · [docs](https://bitstring.readthedocs.io/) · [source](https://github.com/scott-griffiths/bitstring)

<details><summary>README extract</summary>

bitstring is a Python library to help make the creation and analysis of all types of bit-level binary data as simple and efficient as possible. It has been actively maintained since 2006.

> [!NOTE]
> To see what's been added, improved or fixed, see the release notes.

This is a major update with breaking changes. ...

Example:
```python
>>> from bitstring import Bits, BitArray, Reader, pack
>>> a = BitArray(bin='00101')
>>> b = Bits.from_file(a_file_object)
>>> c = BitArray('0xff, 0b101, 0o65, u6=22')
>>> d = pack('ile16, hex=a, 0b1', 100, a='0x34f')
>>> e = pack('<16h', *range(16))
```

...

</details>

### django-csp

Django Content Security Policy support.

`pip install django-csp` · installs (wheel) · licence: BSD License · rank 1888 · last release 2025-04-02 · [PyPI](https://pypi.org/project/django-csp/) · [docs](http://django-csp.readthedocs.org/) · [source](https://github.com/mozilla/django-csp)

<details><summary>README extract</summary>

Django-CSP adds Content-Security-Policy headers to Django.

The code lives on GitHub, where you can report Issues.

The full documentation is available on ReadTheDocs.

</details>

### pathlib

Object-oriented filesystem paths

`pip install pathlib` · installs (wheel) · licence: MIT License · rank 1889 · last release 2022-05-04 · [PyPI](https://pypi.org/project/pathlib/)

<details><summary>README extract</summary>

Attention: this backport module isn't maintained anymore. If you want to report issues or contribute patches, please consider the pathlib2 project instead.

pathlib offers a set of classes to handle filesystem paths. It offers the
following advantages over using string objects:

* No more cumbersome use of os and os.path functions. ...

Example:
```python
>>> from pathlib import *
```

Sections: Description, Requirements, Examples, Documentation, Version 1.0.1, Version 1.0, Version 0.97, Version 0.8, Version 0.7, Version 0.6, Version 0.5

</details>

### parallel-web

The official Python library for the Parallel API

`pip install parallel-web` · installs (wheel) · licence: MIT License · rank 1920 · last release 2026-10-23 · [PyPI](https://pypi.org/project/parallel-web/) · [source](https://github.com/parallel-web/parallel-sdk-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Parallel Python library provides convenient access to the Parallel REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from parallel import Parallel

client = Parallel(
    api_key=os.environ.get("PARALLEL_API_KEY"),  # This is the default and can be omitted
)

task_run = client.task_run.create(
    input="What was the GDP of France in 2023?",
    processor="base",
)
print(task_run.interaction_id)
```

...

</details>

### pure-sasl

Pure Python client SASL implementation

`pip install pure-sasl` · installs from source (sdist only) · licence: MIT License · rank 1924 · last release 2019-10-14 · [PyPI](https://pypi.org/project/pure-sasl/)

<details><summary>README extract</summary>

This package provides a reasonably high-level SASL client written
in pure Python. New mechanisms may be integrated easily, but by default,
support for PLAIN, ANONYMOUS, EXTERNAL, CRAM-MD5, DIGEST-MD5, and GSSAPI are
provided.

</details>

### structlog-sentry

Sentry integration for structlog

`pip install structlog-sentry` · installs (wheel) · licence: MIT License · rank 1925 · last release 2024-11-12 · [PyPI](https://pypi.org/project/structlog-sentry/) · [source](https://github.com/kiwicom/structlog-sentry)

<details><summary>README extract</summary>

| What | Where |

| Documentation | < |
| Maintainer | @kiwicom/platform |

Based on <

Example:
```python
import sentry_sdk
import structlog
from structlog_sentry import SentryProcessor

sentry_sdk.init()  # pass dsn in argument or via SENTRY_DSN env variable

structlog.configure(
    processors=[
        structlog.stdlib.add_logger_name,  # optional, must be placed before SentryProcessor()
...
```

Sections: structlog-sentry, Usage, Sentry Tags, Skip Context, Ignore specific loggers, Logging as JSON

</details>

### flask-appbuilder

Simple and rapid application development framework, built on top of Flask. includes detailed security, auto CRUD generation for your models, google charts and much more.

`pip install flask-appbuilder` · installs (wheel) · licence: BSD License · rank 1928 · last release 2026-10-22 · [PyPI](https://pypi.org/project/flask-appbuilder/)

<details><summary>README extract</summary>

Simple and rapid application development framework, built on top of Flask.
includes detailed security, auto CRUD generation for your models, google charts and much more.

Extensive configuration of all functionality, easily integrate with normal Flask/Jinja2 development.

- Documentation: Documentation

- Mailing list: Google group ...

Sections: Flask App Builder, Includes, Some pictures, Projects/Organizations using FAB, Depends on

</details>

### pydantic-ai-harness

The official capability library and harness for Pydantic AI

`pip install pydantic-ai-harness` · installs (wheel) · licence: MIT · rank 1934 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pydantic-ai-harness/) · [docs](https://pydantic.dev/docs/ai/harness/) · [source](https://github.com/pydantic/pydantic-ai)

<details><summary>README extract</summary>

Your agent's favorite harness, built on Pydantic AI

Pydantic AI Harness is the official capability and harness library for Pydantic AI. Every Pydantic AI agent already has a light harness: the typed agent loop, any model, your own tools, structured output. For simple agents that's enough. ...

Features:
Every capability is a self-contained unit you drop into `capabilities=[...]`, and they all compose, with each other and with your own. Some come with `pydantic-ai` itself, the rest with this package; the Package column says which. ...

Example:
```python
from pydantic_ai_harness.modal_sandbox import ModalSandbox

agent = Agent('anthropic:claude-opus-5-5', capabilities=[ModalSandbox(), Coder()])
```

...

</details>

### aiomultiprocess

AsyncIO version of the standard multiprocessing module

`pip install aiomultiprocess` · installs (wheel) · licence: MIT License · rank 1944 · last release 2024-04-23 · [PyPI](https://pypi.org/project/aiomultiprocess/) · [docs](https://aiomultiprocess.omnilib.dev/en/latest/) · [source](https://github.com/omnilib/aiomultiprocess)

<details><summary>README extract</summary>

Take a modern Python codebase to the next level of performance.

On their own, AsyncIO and multiprocessing are useful, but limited:
AsyncIO still can't exceed the speed of GIL, and multiprocessing only works on
one task at a time. But together, they can fully realize their true potential. ...

Example:
```python
async with Pool() as pool:
    results = await pool.map(<coroutine function>, <items>)
```

</details>

### requests-cache

A persistent cache for python requests

`pip install requests-cache` · installs (wheel) · licence: BSD-2-Clause · rank 1965 · last release 2026-07-03 · [PyPI](https://pypi.org/project/requests-cache/) · [docs](https://requests-cache.readthedocs.io) · [source](https://github.com/requests-cache/requests-cache)

<details><summary>README extract</summary>

requests-cache is a persistent HTTP cache that provides an easy way to get better
performance with the python requests library.

<!-- RTD-IGNORE -->
Complete project documentation can be found at requests-cache.readthedocs.io.
<!-- END-RTD-IGNORE -->

Features:
* Ease of use: Keep using the `requests` library you're already familiar with. Add caching
 with a drop-in replacement
 for `requests.Session`, or
 install globally
 to add transparent caching to all `requests` functions. ...

Example:
```python
import requests

session = requests.Session()
for i in range(60):
    session.get('
```

Sections: Summary, Features, Quickstart, Patching, Headers and Expiration, Settings, Next Steps

</details>

### bc-python-hcl2

A parser for HCL2

`pip install bc-python-hcl2` · installs (wheel) · licence: MIT License · rank 1970 · last release 2025-07-14 · [PyPI](https://pypi.org/project/bc-python-hcl2/)

<details><summary>README extract</summary>

This is a fork of the Python HCL2 repo by Amplify and is
officially supported by Bridgecrew. We contributed as much as possible to the upstream project, but the two projects
are now deviating in a way that pushing new changes upstream doesn't make sense anymore.

A parser for HCL2 written in Python using
Lark. ...

Example:
```python
import hcl2
with open('foo.tf', 'r') as file:
    dict = hcl2.load(file)
```

Sections: Notice, Python HCL2, About Amplify, Getting Started, Prerequisites, Usage, Building From Source, Running Tests, Responsible Disclosure

</details>

### doclang

DocLang reference toolkit

`pip install doclang` · installs (wheel) · licence: Apache-2.0 · rank 1983 · last release 2026-10-30 · [PyPI](https://pypi.org/project/doclang/) · [docs](https://github.com/doclang-project/doclang/blob/main/README.md) · [source](https://github.com/doclang-project/doclang)

<details><summary>README extract</summary>

DocLang is the AI-native markup format for unstructured content — including documents, images, and more. It maps cleanly to LLM tokens while preserving structure, semantics, layout, and geometry in a single, unambiguous representation.

This repository is the home of the normative specification and the reference toolkit for DocLang. ...

Sections: DocLang, Specification, Reference Toolkit, Validation, Packaging, We ❤️ Open Source AI

</details>

### pytest-postgresql

Postgresql fixtures and fixture factories for Pytest.

`pip install pytest-postgresql` · installs (wheel) · licence: LGPL-3.0-or-later · rank 1985 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pytest-postgresql/) · [source](https://github.com/dbfixtures/pytest-postgresql)

_README extract left out: share-alike licence._

### terminaltables

Generate simple tables in terminals from a nested list of strings.

`pip install terminaltables` · installs (wheel) · licence: MIT License · rank 1989 · last release 2021-12-07 · [PyPI](https://pypi.org/project/terminaltables/) · [docs](https://github.com/matthewdeanmartin/terminaltables) · [source](https://github.com/matthewdeanmartin/terminaltables)

<details><summary>README extract</summary>

Easily draw tables in terminal/console applications from a list of lists of strings. Supports multi-line rows.

- Python 2.6, 2.7, PyPy, PyPy3, 3.3, 3.4, and 3.5+ supported on Linux and OS X.
- Python 2.7, 3.3, 3.4, and 3.5+ supported on Windows (both 32 and 64 bit versions of Python).

📖 Full documentation:

Example:
```python
from terminaltables import AsciiTable

table_data = [
    ['Heading1', 'Heading2'],
    ['row1 column1', 'row1 column2'],
    ['row2 column1', 'row2 column2'],
    ['row3 column1', 'row3 column2']
]
table = AsciiTable(table_data)
print
table.table
```

Sections: terminaltables, What is it, Quickstart, Example Implementations

</details>

### bc-jsonpath-ng

A final implementation of JSONPath for Python that aims to be standard compliant, including arithmetic and binary comparison operators and providing clear AST for metaprogramming.

`pip install bc-jsonpath-ng` · installs (wheel) · licence: Apache Software License · rank 2004 · last release 2023-11-26 · [PyPI](https://pypi.org/project/bc-jsonpath-ng/)

<details><summary>README extract</summary>

A final implementation of JSONPath for Python that aims to be standard compliant, including arithmetic
and binary comparison operators, as defined in the original JSONPath proposal.

This packages merges both jsonpath-rw and jsonpath-rw-ext and
provides several AST API enhancements, such as the ability to update or removes nodes in the tree. ...

Example:
```python
$ python

>>> from jsonpath_ng import jsonpath, parse

# A robust parser, not just a regex. (Makes powerful extensions possible; see below)
>>> jsonpath_expr = parse('foo[*].baz')

# Extracting values is easy
>>> [match.value for match in jsonpath_expr.find({'foo': [{'baz': 1}, {'baz': 2}]})]
[1, 2]

# Matches remember where they came from
...
```

...

</details>

### browserbase

The official Python library for the Browserbase API

`pip install browserbase` · installs (wheel) · licence: Apache Software License · rank 2007 · last release 2026-11-04 · [PyPI](https://pypi.org/project/browserbase/) · [source](https://github.com/browserbase/sdk-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Browserbase Python library provides convenient access to the Browserbase REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from playwright.sync_api import Playwright, sync_playwright
from browserbase import Browserbase

BROWSERBASE_API_KEY = os.environ.get("BROWSERBASE_API_KEY")
BROWSERBASE_PROJECT_ID = os.environ.get("BROWSERBASE_PROJECT_ID")

client = Browserbase(
    # This is the default and can be omitted
    api_key=BROWSERBASE_API_KEY,
)

...
```

...

</details>

### reactivex

ReactiveX (Rx) for Python

`pip install reactivex` · installs (wheel) · licence: MIT · rank 2018 · last release 2026-10-24 · [PyPI](https://pypi.org/project/reactivex/) · [docs](https://rxpy.readthedocs.io/en/latest/) · [source](https://github.com/ReactiveX/RxPY)

<details><summary>README extract</summary>

*A library for composing asynchronous and event-based programs using observable
collections and query operator functions in Python*

Example:
```python
import reactivex as rx
from reactivex import operators as ops

source = rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

composed = source.pipe(
    ops.map(lambda s: len(s)),
    ops.filter(lambda i: i >= 5)
)
composed.subscribe(lambda value: print("Received {0}".format(value)))
```

Sections: The ReactiveX for Python (RxPY), About ReactiveX, Fluent and Functional Syntax, Learning ReactiveX, Differences from .NET and RxJS

</details>

### netCDF4

Provides an object-oriented python interface to the netCDF version 4 library

`pip install netCDF4` · installs (wheel) · licence: MIT · rank 2054 · last release 2026-10-29 · [PyPI](https://pypi.org/project/netCDF4/) · [docs](https://unidata.github.io/netcdf4-python/) · [source](https://github.com/Unidata/netcdf4-python)

<details><summary>README extract</summary>

netCDF version 4 has many features not found in earlier versions of the library,
such as hierarchical groups, zlib compression, multiple unlimited dimensions,
and new data types. It is implemented on top of HDF5. This module implements
most of the new features, and can read and write netCDF files compatible with
older versions of the library. ...

</details>

### hjson

Hjson, a user interface for JSON.

`pip install hjson` · installs (wheel) · licence: Academic Free License (AFL); MIT License · rank 2058 · last release 2022-08-13 · [PyPI](https://pypi.org/project/hjson/)

<details><summary>README extract</summary>

Hjson, a user interface for JSON

Hjson works with Python 2.5+ and Python 3.3+ (based on simplejson)

Example:
```python
import hjson
```

Sections: hjson-py, Commandline, Usage, Decoding Hjson, Encoding Python object hierarchies, Encoding as JSON, API

</details>

### google

Python bindings to the Google search engine.

`pip install google` · installs (wheel) · licence: BSD License · rank 2068 · last release 2020-07-11 · [PyPI](https://pypi.org/project/google/)

### bluetooth-data-tools

Tools for converting bluetooth data and packets

`pip install bluetooth-data-tools` · installs (wheel) · licence: Apache-2.0 · rank 2078 · last release 2026-08-30 · [PyPI](https://pypi.org/project/bluetooth-data-tools/) · [docs](https://bluetooth-data-tools.readthedocs.io) · [source](https://github.com/bdraco/bluetooth-data-tools)

<details><summary>README extract</summary>

Tools for converting bluetooth data and packets

Example:
```python
from bluetooth_data_tools import parse_advertisement_data_bytes

# Parse raw GAP advertisement bytes
parsed = parse_advertisement_data_bytes(raw_bytes)
local_name = parsed[0]        # str | None
service_uuids = parsed[1]     # list[str]
service_data = parsed[2]      # dict[str, bytes]
manufacturer_data = parsed[3] # dict[int, bytes]
...
```

Sections: Bluetooth Data Tools, Usage, Parsing BLE GAP Advertisement Data, Bluetooth Address Utilities, Distance Estimation, Monotonic Time, Private Address Resolution (RPA)

</details>

### timeout-decorator

Timeout decorator

`pip install timeout-decorator` · installs from source (sdist only) · licence: MIT License · rank 2085 · last release 2020-11-15 · [PyPI](https://pypi.org/project/timeout-decorator/)

<details><summary>README extract</summary>

Example:
```python
import time
import timeout_decorator

@timeout_decorator.timeout(5)
def mytest():
    print("Start")
    for i in range(1,10):
        time.sleep(1)
        print("{} seconds have passed".format(i))

if name == 'main':
    mytest()
```

Sections: Timeout decorator, Usage, Multithreading, 0.3.1, 0.3.0, 0.2.1

</details>

### tox-uv

Integration of uv with tox (meta package with bundled uv).

`pip install tox-uv` · installs (wheel) · licence: MIT · rank 2097 · last release 2026-11-07 · [PyPI](https://pypi.org/project/tox-uv/) · [docs](https://github.com/tox-dev/tox-uv#tox-uv) · [source](https://github.com/tox-dev/tox-uv)

<details><summary>README extract</summary>

tox-uv is a `tox` plugin, which replaces `virtualenv` and pip with `uv` in your `tox` environments. Note that you
will get both the benefits (performance) or downsides (bugs) of `uv`.

Changelog · Contributing

<!--ts-->

- How to use
 - Require it from the project
 - Installation options
 - uv discovery
- tox environment types provided ...

Example:
```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["requests>=2.31", "rich"]
# ///

import requests
from rich import print

print(requests.get("
```

Sections: tox-uv, How to use, Require it from the project, uv discovery, tox environment types provided, PEP 723 inline script metadata, `package`, `extras`, `no_default_groups`, `dependency_groups`, `only_groups`, `uv_sync_flags`, `uv_sync_locked`, Environment creation

</details>

### inquirer

Collection of common interactive command line user interfaces, based on Inquirer.js

`pip install inquirer` · installs (wheel) · licence: MIT License · rank 2098 · last release 2025-08-02 · [PyPI](https://pypi.org/project/inquirer/) · [docs](https://python-inquirer.readthedocs.io) · [source](https://github.com/magmax/python-inquirer)

<details><summary>README extract</summary>

[][pypi status]
[][pypi status]
[][pypi status]
[][license]
[][black]

[][read the docs]
[][tests]
[][codecov]
[][pre-commit]

Collection of common interactive command line user interfaces, based on [Inquirer.js].

Born as a [Inquirer.js] clone, it shares part of the goals and philosophy. ...

Example:
```python
import re

import inquirer
questions = [
  inquirer.Text('name', message="What's your name"),
  inquirer.Text('surname', message="What's your surname"),
  inquirer.Text('phone', message="What's your phone number",
                validate=lambda _, x: re.match('\+?\d[\d ]+\d', x),
                )
]
answers = inquirer.prompt(questions)
```

Sections: python-inquirer, Goal and Philosophy, Documentation, Text, Editor, List, Checkbox, Path

</details>

### aiologic

GIL-powered* locking library for Python

`pip install aiologic` · installs (wheel) · licence: ISC License (ISCL) · rank 2106 · last release 2026-06-27 · [PyPI](https://pypi.org/project/aiologic/) · [docs](https://aiologic.readthedocs.io)

<details><summary>README extract</summary>

aiologic is a locking library for tasks synchronization and their
communication. It provides primitives that are both *async-aware* and

- async codes (async <-> async) in one thread as regular async primitives
- async codes (async <-> async) in multiple threads (!)
- async code and sync one (async <-> sync) in one thread (!) ...

Features:
* Python 3.8+ support
* CPython and PyPy
 support
* Experimental Nuitka support
* Pickling and weakrefing support
* Cancellation and timeouts support

 * enabled by default for Trio itself
 * disabled by default for all others ...

Example:
```python
import asyncio

from threading import Thread

import aiologic

lock = aiologic.Lock()

async def func(i: int, j: int) -> None:
    print(f"thread={i} task={j} start")

    async with lock:
...

</details>

### accessible-pygments

A collection of accessible pygments styles

`pip install accessible-pygments` · installs (wheel) · licence: BSD License · rank 2107 · last release 2024-05-10 · [PyPI](https://pypi.org/project/accessible-pygments/)

<details><summary>README extract</summary>

Example:
```python
from pygments.formatters import HtmlFormatter
HtmlFormatter(style='a11y-light').style
<class 'accessible-pygments.A11yLight'>
```

Sections: Accessible pygments themes, Accessibility details ♿️, WCAG 2.1 - AAA compliant, WCAG 2.1 - AA compliant, Documentation 📖, Using the themes directly in your code or app, Using the themes in your Sphinx documentation

</details>

### Keras-Applications

Reference implementations of popular deep learning models

`pip install Keras-Applications` · installs (wheel) · licence: MIT License · rank 2110 · last release 2019-05-30 · [PyPI](https://pypi.org/project/Keras-Applications/)

<details><summary>README extract</summary>

Keras Applications is the `applications` module of
the Keras deep learning library.
It provides model definitions and pre-trained weights for a number
of popular archictures, such as VGG16, ResNet50, Xception, MobileNet, and more.

Read the documentation at:

Keras Applications may be imported directly
from an up-to-date installation of Keras: ...

Example:
```python
from keras import applications
```

</details>

### pytest_httpserver

pytest-httpserver is a httpserver for pytest

`pip install pytest_httpserver` · installs (wheel) · licence: MIT · rank 2127 · last release 2026-10-05 · [PyPI](https://pypi.org/project/pytest_httpserver/) · [docs](https://pytest-httpserver.readthedocs.io/en/latest/) · [source](https://github.com/csernazs/pytest-httpserver)

<details><summary>README extract</summary>

HTTP server for pytest

This library is designed to help to test http clients without contacting the real http server.
In other words, it is a fake http server which is accessible via localhost can be started with
the pre-defined expected http requests and their responses.

Features:
You can set up a dozen of expectations for the requests, and also what response should be sent by the server to the client.

Example:
```python
def test_my_client(
    httpserver,
):  # httpserver is a pytest fixture which starts the server
    # set up the server to serve /foobar with the json
    httpserver.expect_request("/foobar").respond_with_json({"foo": "bar"})
    # check that the request is served
    assert requests.get(httpserver.url_for("/foobar")).json() == {"foo": "bar"}
```

...

</details>

### apache-beam

Apache Beam SDK for Python

`pip install apache-beam` · installs (wheel) · licence: Apache Software License · rank 2135 · last release 2026-10-07 · [PyPI](https://pypi.org/project/apache-beam/)

<details><summary>README extract</summary>

Apache Beam is a unified model for defining both batch and streaming data-parallel processing pipelines, as well as a set of language-specific SDKs for constructing pipelines and Runners for executing them on distributed processing backends, including Apache Flink, Apache Spark, Google Cloud Dataflow, and Hazelcast Jet.

Features:
Beam provides a general approach to expressing embarrassingly parallel data processing pipelines and supports three categories of users, each of which have relatively disparate backgrounds and needs.

1. ...

...

</details>

### pathlib2

Object-oriented filesystem paths

`pip install pathlib2` · installs (wheel) · licence: MIT License · rank 2158 · last release 2022-02-10 · [PyPI](https://pypi.org/project/pathlib2/)

<details><summary>README extract</summary>

The `old pathlib <
module on bitbucket is no longer maintained.
The goal of pathlib2 is to provide a backport of
`standard pathlib <
module which tracks the standard library module,
so all the newest features of the standard pathlib can be
used also on older Python versions.

Download

Standalone releases are available on PyPI:

Development ...

</details>

### dagster-cloud

(no summary)

`pip install dagster-cloud` · installs (wheel) · licence: Apache Software License · rank 2163 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-cloud/) · [source](https://github.com/dagster-io/dagster-cloud)

<details><summary>README extract</summary>

The enterprise orchestration platform that puts developer experience first, with fully serverless or hybrid deployments, native branching, and out-of-the-box CI/CD.

Sections: Dagster Cloud, Getting Started, Documentation

</details>

### culsans

Thread-safe async-aware queue for Python

`pip install culsans` · installs (wheel) · licence: ISC License (ISCL) · rank 2177 · last release 2025-12-31 · [PyPI](https://pypi.org/project/culsans/) · [docs](https://culsans.readthedocs.io)

<details><summary>README extract</summary>

Mixed sync-async queue, supposed to be used for communicating between classic
synchronous (threaded) code and asynchronous one, between two asynchronous
codes in different threads, and for any other combination that you want. Based
on the queue module. Built on
the aiologic package. Inspired by
the janus library. ...

Example:
```python
import anyio
import culsans

def sync_run(sync_q: culsans.SyncQueue[int]) -> None:
    for i in range(100):
        sync_q.put(i)
    else:
        sync_q.join()

async def async_run(async_q: culsans.AsyncQueue[int]) -> None:
    for i in range(100):
        value = await async_q.get()

        assert value == i

        async_q.task_done()

...
```

...

</details>

### standard-aifc

Standard library aifc redistribution. "dead battery".

`pip install standard-aifc` · installs (wheel) · licence: Python Software Foundation License · rank 2220 · last release 2024-10-30 · [PyPI](https://pypi.org/project/standard-aifc/)

<details><summary>README extract</summary>

Python is moving forward! Python finally started to remove dead batteries.
For more information, see PEP 594.

If your project depends on a module that has been removed from the standard,
here is the redistribution of the dead batteries.

</details>

### standard-chunk

Standard library chunk redistribution. "dead battery".

`pip install standard-chunk` · installs (wheel) · licence: Python Software Foundation License · rank 2225 · last release 2024-10-30 · [PyPI](https://pypi.org/project/standard-chunk/)

<details><summary>README extract</summary>

Python is moving forward! Python finally started to remove dead batteries.
For more information, see PEP 594.

If your project depends on a module that has been removed from the standard,
here is the redistribution of the dead batteries.

</details>

### lark-parser

a modern parsing library

`pip install lark-parser` · installs (wheel) · licence: MIT License · rank 2226 · last release 2021-08-30 · [PyPI](https://pypi.org/project/lark-parser/)

<details><summary>README extract</summary>

Lark is a modern general-purpose parsing library for Python.

With Lark, you can parse any context-free grammar, efficiently, with very little code.

Main Features:
 - Builds a parse-tree (AST) automagically, based on the structure of the grammar
 - Earley parser
 - Can parse all context-free grammars
 - Full support for ambiguous grammars
 - ...

</details>

### deepgram-sdk

(no summary)

`pip install deepgram-sdk` · installs (wheel) · licence: MIT License · rank 2228 · last release 2026-11-04 · [PyPI](https://pypi.org/project/deepgram-sdk/) · [source](https://github.com/deepgram/deepgram-python-sdk)

<details><summary>README extract</summary>

The official Python SDK for Deepgram's automated speech recognition, text-to-speech, and language understanding APIs. Power your applications with world-class speech and Language AI models.

Comprehensive API documentation and guides are available at developers.deepgram.com.

- v6 to v7 (current)
- v5 to v6
- v3+ to v5
- v2 to v3+

Example:
```python
from deepgram import DeepgramClient
from deepgram.core.events import EventType

client = DeepgramClient()

with client.listen.v2.connect(
    model="flux-general-en",
    encoding="linear16",
    sample_rate=16000
) as connection:
    def on_message(message):
        print(f"Received {message.type} event")

...
```

...

</details>

### gdown

Google Drive Public File/Folder Downloader

`pip install gdown` · installs (wheel) · licence: MIT License · rank 2229 · last release 2026-10-29 · [PyPI](https://pypi.org/project/gdown/)

<details><summary>README extract</summary>

Google Drive public file/folder downloader when curl/wget fails.

Features:
Downloading public files from Google Drive with curl or wget doesn't work —
Google serves a confirmation page for large files, and the URL formats are a mess.

gdown gets around that: ...

Example:
```python
import gdown

# Download a file
url = "
gdown.download(url=url, output="fcn8s_from_caffe.npz")

# Download by file ID
gdown.download(id="0B9P1L--7Wd2vNm9zMTJWOGxobkU", output="output.npz")

# Download from a share link
url = "
gdown.download(url=url, output="output.npz")

# Download with hash verification and caching
gdown.cached_download(
...
```

...

</details>

### zeroconf

A pure python implementation of multicast DNS service discovery

`pip install zeroconf` · installs (wheel) · licence: LGPL-2.1-or-later · rank 2232 · last release 2026-11-06 · [PyPI](https://pypi.org/project/zeroconf/) · [docs](https://python-zeroconf.readthedocs.io) · [source](https://github.com/python-zeroconf/python-zeroconf)

_README extract left out: share-alike licence._

### x-wr-timezone

Repair Google Calendar - This Python module and program makes ICS/iCalendar files using X-WR-TIMEZONE compatible with the RFC 5545 standard.

`pip install x-wr-timezone` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 2233 · last release 2025-02-06 · [PyPI](https://pypi.org/project/x-wr-timezone/)

_README extract left out: share-alike licence._

### tox-uv-bare

Integration of uv with tox (bare package, bring your own uv).

`pip install tox-uv-bare` · installs (wheel) · licence: MIT · rank 2239 · last release 2026-11-07 · [PyPI](https://pypi.org/project/tox-uv-bare/) · [docs](https://github.com/tox-dev/tox-uv#tox-uv) · [source](https://github.com/tox-dev/tox-uv)

<details><summary>README extract</summary>

tox-uv is a `tox` plugin, which replaces `virtualenv` and pip with `uv` in your `tox` environments. Note that you
will get both the benefits (performance) or downsides (bugs) of `uv`.

Changelog · Contributing

<!--ts-->

- How to use
 - Require it from the project
 - Installation options
 - uv discovery
- tox environment types provided ...

Example:
```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["requests>=2.31", "rich"]
# ///

import requests
from rich import print

print(requests.get("
```

Sections: tox-uv, How to use, Require it from the project, uv discovery, tox environment types provided, PEP 723 inline script metadata, `package`, `extras`, `no_default_groups`, `dependency_groups`, `only_groups`, `uv_sync_flags`, `uv_sync_locked`, Environment creation

</details>

### tensorstore

Read and write large, multi-dimensional arrays

`pip install tensorstore` · installs (wheel) · licence: Apache-2.0 · rank 2240 · last release 2026-10-26 · [PyPI](https://pypi.org/project/tensorstore/) · [docs](https://google.github.io/tensorstore) · [source](https://github.com/google/tensorstore)

<details><summary>README extract</summary>

TensorStore is an open-source C++ and Python software library designed for
storage and manipulation of large multi-dimensional arrays that:

* Provides advanced, fully composable indexing operations and virtual views.

* Provides a uniform API for reading and writing multiple array formats, including
 zarr and N5. ...

Sections: TensorStore, Getting Started

</details>

### pystache

Mustache for Python

`pip install pystache` · installs (wheel) · licence: MIT License · rank 2243 · last release 2025-03-18 · [PyPI](https://pypi.org/project/pystache/) · [docs](http://mustache.github.io/) · [source](https://github.com/PennyDreadfulMTG/pystache.git)

<details><summary>README extract</summary>

This updated fork of Pystache is currently tested on Python 3.8+ and in
Conda, on Linux, Macos, and Windows.

Pystache is a Python
implementation of Mustache.
Mustache is a framework-agnostic, logic-free templating system inspired
by ctemplate and
et. ...

Example:
```python
>>> import pystache
>>> print(pystache.render('Hi {{person}}!', {'person': 'Mom'}))
Hi Mom!
```

Sections: Pystache, Requirements, Quick Start, Use It, Unicode

</details>

### PyDispatcher

Multi-producer multi-consumer in-memory signal dispatch system

`pip install PyDispatcher` · installs (wheel) · licence: BSD License · rank 2249 · last release 2023-02-17 · [PyPI](https://pypi.org/project/PyDispatcher/)

<details><summary>README extract</summary>

PyDispatcher provides the Python programmer with a multiple-producer-multiple-consumer signal-registration and
routing infrastructure for use in multiple contexts. The mechanism
of PyDispatcher started life as a highly rated recipe
in the Python Cookbook. ...

Example:
```python
from pydispatch import dispatcher

metaKey = "moo"
MyNode = object()
event = {"sample": "event"}

def callback(event=None):
    """Handle signal being sent"""
    print("Signal received", event)

dispatcher.connect(callback, sender=MyNode, signal=metaKey)
dispatcher.send(metaKey, MyNode, event=event)
```

Sections: PyDispatcher Multi-producer Multi-consumer Observables, Usage

</details>

### nameparser

A simple Python module for parsing human names into their individual components.

`pip install nameparser` · installs (wheel) · licence: LGPL-2.1-or-later · rank 2277 · last release 2026-11-05 · [PyPI](https://pypi.org/project/nameparser/)

_README extract left out: share-alike licence._

### pytest-bdd

BDD for pytest

`pip install pytest-bdd` · installs (wheel) · licence: MIT · rank 2282 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pytest-bdd/) · [docs](https://pytest-bdd.readthedocs.io/) · [source](https://github.com/pytest-dev/pytest-bdd)

<details><summary>README extract</summary>

pytest-bdd implements a subset of the Gherkin language to enable automating project
requirements testing and to facilitate behavioral driven development.

Unlike many other BDD tools, it does not require a separate runner and benefits from
the power and flexibility of pytest. ...

Features:
By default, pytest-bdd will use the current module's path as the base path for finding feature files, but this behaviour can be changed in the pytest configuration file (i.e. ...

Example:
```python
# content of test_publish_article.py

from pytest_bdd import scenario, given, when, then

@scenario('publish_article.feature', 'Publishing the article')
def test_publish():
    pass

@given("I'm an author user")
def author_user(auth, author):
    auth['user'] = author.user

...

</details>

### pytimeparse2

Time expression parser.

`pip install pytimeparse2` · installs (wheel) · licence: MIT License · rank 2285 · last release 2023-05-11 · [PyPI](https://pypi.org/project/pytimeparse2/) · [source](https://github.com/onegreyonewhite/pytimeparse2.git)

<details><summary>README extract</summary>

This is a pytimeparse based project with the aim of optimizing functionality and providing stable support.

Copyright (c) 2021 Sergey Klyuykov <onegreyonewhite@mail.ru>

Licensed under the MIT License (see source file `pytimeparse2.py` for
details). ...

Example:
```python
>>> from pytimeparse import parse
>>> parse('1.2 minutes')
72
```

Sections: pytimeparse2: time expression parser, Notes, Future work

</details>

### statsig

Statsig Python Server SDK

`pip install statsig` · installs (wheel) · licence: ISC · rank 2286 · last release 2026-08-19 · [PyPI](https://pypi.org/project/statsig/)

<details><summary>README extract</summary>

The python SDK for server/multi-user environments.

Statsig helps you move faster with Feature Gates (Feature Flags) and Dynamic Configs. It also allows you to run A/B tests to validate your new features and understand their impact on your KPIs. If you're new to Statsig, create an account at statsig.com.

Sections: Statsig Python Server SDK, Getting Started, Guidelines

</details>

### JSON-log-formatter

JSON log formatter

`pip install JSON-log-formatter` · installs (wheel) · licence: MIT License · rank 2290 · last release 2026-06-08 · [PyPI](https://pypi.org/project/JSON-log-formatter/) · [source](https://github.com/marselester/json-log-formatter)

<details><summary>README extract</summary>

The library helps you to store logs in JSON format. Why is it important?
Well, it facilitates integration with Logstash.

Usage example:

The log file will contain the following log record (inline).

If you use a log collection and analysis system,
you might need to include the built-in
log record attributes
with `VerboseJSONFormatter`. ...

Example:
```python
import logging

import json_log_formatter

formatter = json_log_formatter.JSONFormatter()

json_handler = logging.FileHandler(filename='/var/log/my-log.json')
json_handler.setFormatter(formatter)

logger = logging.getLogger('my_json')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)

...
```

Sections: JSON log formatter 🪵, JSON libraries, Django integration, Custom formatter, Tests

</details>

### pytest-unordered

Test equality of unordered collections in pytest

`pip install pytest-unordered` · installs (wheel) · licence: MIT License · rank 2291 · last release 2026-06-16 · [PyPI](https://pypi.org/project/pytest-unordered/)

<details><summary>README extract</summary>

`pytest_unordered` allows you to write simple (pytest) assertions
to test whether collections have the same content, regardless of order.
For example:

 assert [1, 20, 300] == unordered([20, 300, 1])

It is especially useful when testing APIs that return some complex data structures
in an arbitrary order, e.g.: ...

Sections: pytest-unordered: Test collection content, ignoring order, Usage, Basics, Nesting, Container type checking

</details>

### pytest-factoryboy

Factory Boy support for pytest.

`pip install pytest-factoryboy` · installs (wheel) · licence: MIT License · rank 2303 · last release 2025-07-01 · [PyPI](https://pypi.org/project/pytest-factoryboy/) · [docs](https://pytest-factoryboy.readthedocs.io/) · [source](https://github.com/pytest-dev/pytest-factoryboy)

<details><summary>README extract</summary>

pytest-factoryboy makes it easy to combine `factory` approach to the test setup with the `dependency` injection,
heart of the pytest fixtures.

Example:
```python
import factory
from pytest_factoryboy import register

@register
class AuthorFactory(factory.Factory):
    class Meta:
        model = Author

    name = "Charles Dickens"

def test_model_fixture(author):
    assert author.name == "Charles Dickens"
```

Sections: factory_boy integration with the pytest runner, Concept, Model Fixture, Attributes are Fixtures, Multiple fixtures, SubFactory, Related Factory, post-generation, Factory Fixture, Integration, Fixture partial specialization, Fixture attributes, Generic container classes as models, Post-generation dependencies

</details>

### typepy

typepy is a Python library for variable type checker/validator/converter at a run time.

`pip install typepy` · installs (wheel) · licence: MIT License · rank 2313 · last release 2026-05-09 · [PyPI](https://pypi.org/project/typepy/) · [docs](https://typepy.rtfd.io/) · [source](https://github.com/thombashi/typepy)

<details><summary>README extract</summary>

typepy is a Python library for variable type checker/validator/converter at a run time.

Features:
- checking a value type
- validate a value for a type
- convert a value from one type to the other type

The correspondence between Python types and `typepy` classes are as follows:

Sections: Summary, Features, Dependencies, Optional dependencies, Usage, Type Check Method, Type Validation Method, Type Conversion Methods, convert method, try_convert method, force_convert, For more information, Documentation

</details>

### mbstrdecoder

mbstrdecoder is a Python library for multi-byte character string decoder

`pip install mbstrdecoder` · installs (wheel) · licence: MIT License · rank 2314 · last release 2026-05-05 · [PyPI](https://pypi.org/project/mbstrdecoder/) · [source](https://github.com/thombashi/mbstrdecoder)

<details><summary>README extract</summary>

mbstrdecoder is a Python library for multi-byte character string decoder.

Sections: Summary, Usage, Dependencies

</details>

### multi-key-dict

Multi key dictionary implementation

`pip install multi-key-dict` · installs (wheel) · licence: MIT · rank 2316 · last release 2026-10-30 · [PyPI](https://pypi.org/project/multi-key-dict/)

<details><summary>README extract</summary>

Implementation of a multi-key dictionary, i.e.:

(key1[,key2, ..]) => value

This dictionary has a similar interface to the standard dictionary => but is extended to support multiple keys referring to the same element.

If element is created using multiple keys, e.g.: ...

Example:
```python
from multi_key_dict import multi_key_dict

k = multi_key_dict()
k[1000, 'kilo', 'k'] = 'kilo (x1000)'

print k[1000] # will print 'kilo (x1000)'
print k['k'] # will also print 'kilo (x1000)'

# the same way objects can be updated, deleted:
# and if an object is updated using one key, the new value will
...
```

</details>

### blosc2

A fast & compressed ndarray library with a flexible compute engine.

`pip install blosc2` · installs (wheel) · licence: BSD-3-Clause · rank 2322 · last release 2026-09-30 · [PyPI](https://pypi.org/project/blosc2/) · [docs](https://www.blosc.org/python-blosc2/python-blosc2.html)

<details><summary>README extract</summary>

:Author: The Blosc development team
:Contact: blosc@blosc.org
:Github:
:Actions:
:PyPi:
:NumFOCUS:
:Code of Conduct:

Python-Blosc2 is a high-performance compressor, compute engine, and format for binary data containers that are portable and open-source. ...

Sections: Python-Blosc2, What is Python-Blosc2?, Command line tools, Documentation, Discussion forum, Social feeds, Thanks, Citing Blosc

</details>

### wget

pure python download utility

`pip install wget` · installs from source (sdist only) · licence: Public Domain · rank 2323 · last release 2015-10-22 · [PyPI](https://pypi.org/project/wget/)

### nulltype

Null values and sentinels like (but not) None, False & True

`pip install nulltype` · installs (wheel) · licence: Apache Software License · rank 2331 · last release 2018-06-03 · [PyPI](https://pypi.org/project/nulltype/)

<details><summary>README extract</summary>

travisciversionversionsimplswheelcoveragebr-coverage|

Helps define 'null' values and sentinels parallel to, but different from,
Python built-ins such as `None`, `False`, and `True`.

`None` is a great sentinel value
and a classic implementation of the
null object pattern. ...

Example:
```python
from nulltype import NullType

Void = NullType('Void')

# following just to show it's working
assert bool(Void) == False
assert len(EmpVoidty) == 0
assert list(Void) == []
assert Void.some_attribute is Empty
assert Void[22] is Nothing
assert Void("hey", 12) is Empty
```

Sections: Usage, The Power of Nothing, General Sentinels and Distinguished Values, Uniqueness, Notes

</details>

### concurrent-log-handler

RotatingFileHandler replacement with concurrency, gzip and Windows support. Size and time based rotation.

`pip install concurrent-log-handler` · installs (wheel) · licence: Apache-2.0 · rank 2332 · last release 2026-10-21 · [PyPI](https://pypi.org/project/concurrent-log-handler/)

<details><summary>README extract</summary>

<!-- markdownlint-disable MD026 -->

The `concurrent-log-handler` package provides robust logging handlers for
Python's standard `logging` package (PEP 282). It enables multiple processes
(and threads) to safely write to a single log file, with built-in support for
size-based and time-based log rotation and optional log compression. ...

Features:
- Concurrent Logging: Multiple processes and threads safely write to the
 same log file.
- File Rotation: Size-based and time-based rotation with optional
 compression.
- Cross-Platform: Windows and POSIX support with reliable file locking. ...

Example:
```python
import logging
from concurrent_log_handler import ConcurrentRotatingFileHandler
import os

logger = logging.getLogger(name)
logger.setLevel(logging.INFO)

...

</details>

### pykakasi

Kana kanji simple inversion library

`pip install pykakasi` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 2338 · last release 2024-06-24 · [PyPI](https://pypi.org/project/pykakasi/) · [source](https://codeberg.org/miurahr/pykakasi)

_README extract left out: share-alike licence._

### pyfakefs

Implements a fake file system that mocks the Python file system modules.

`pip install pyfakefs` · installs (wheel) · licence: Apache-2.0 · rank 2340 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyfakefs/) · [docs](https://pytest-pyfakefs.readthedocs.io/) · [source](https://github.com/pytest-dev/pyfakefs)

<details><summary>README extract</summary>

`pyfakefs` implements a fake file system that mocks the Python file system modules.
Using `pyfakefs`, your tests operate on a fake file system in memory without
touching the real disk. The software under test requires no modification to
work with `pyfakefs`. ...

Features:
Apart from automatically mocking most file-system functions, pyfakefs
provides some additional features:

- mapping files and directories from the real file system into the fake filesystem
- configuration and tracking of the file system size ...

Sections: pyfakefs, Usage, Documentation, Features, Limitations

</details>

### pyyaml-include

An extending constructor of PyYAML: include other YAML files into current YAML document

`pip install pyyaml-include` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 2345 · last release 2024-11-09 · [PyPI](https://pypi.org/project/pyyaml-include/) · [docs](https://pyyaml-include.readthedocs.io/en/latest/) · [source](https://github.com/tanbro/pyyaml-include.git)

_README extract left out: share-alike licence._

### flit

A simple packaging tool for simple packages.

`pip install flit` · installs (wheel) · licence: BSD-3-Clause · rank 2348 · last release 2026-10-27 · [PyPI](https://pypi.org/project/flit/) · [docs](https://flit.pypa.io) · [source](https://github.com/pypa/flit)

<details><summary>README extract</summary>

Flit is a simple way to put Python packages and modules on PyPI.
It tries to require less thought about packaging and help you avoid common
mistakes.
See Why use Flit? for
more about how it compares to other Python packaging tools.

</details>

### sphinx_design

A sphinx extension for designing beautiful, view size responsive web components.

`pip install sphinx_design` · installs (wheel) · licence: MIT License · rank 2356 · last release 2026-01-19 · [PyPI](https://pypi.org/project/sphinx_design/) · [docs](https://sphinx-design.readthedocs.io)

<details><summary>README extract</summary>

[][github-link]
[][codecov-link]
[][pypi-link]

A sphinx extension for designing beautiful, view size responsive web components.

Created with inspiration from Bootstrap (v5), Material Design and Material-UI design frameworks.

Sections: sphinx-design, Usage, Comparison to sphinx-panels, TODO

</details>

### tweepy

Library for accessing the X API (Twitter)

`pip install tweepy` · installs (wheel) · licence: MIT License · rank 2359 · last release 2026-07-02 · [PyPI](https://pypi.org/project/tweepy/) · [docs](https://docs.tweepy.org) · [source](https://github.com/tweepy/tweepy)

<details><summary>README extract</summary>

Installation

The easiest way to install the latest version from PyPI is by using
pip:

 pip install tweepy

To use the `tweepy.asynchronous` subpackage, be sure to install with the
`async` extra:

 pip install tweepy[async]

You can also use Git to clone the repository from GitHub to install the latest
development version: ...

</details>

### ip3country

A zero-dependency, local, fast, tiny ip-address to country lookup

`pip install ip3country` · installs (wheel) · licence: ISC · rank 2365 · last release 2025-07-10 · [PyPI](https://pypi.org/project/ip3country/)

### plaid-python

Python client library for the Plaid API and Link

`pip install plaid-python` · installs from source (sdist only) · licence: MIT · rank 2368 · last release 2026-10-19 · [PyPI](https://pypi.org/project/plaid-python/)

### llama-cloud

The official Python library for the llama-cloud API

`pip install llama-cloud` · installs (wheel) · licence: MIT License · rank 2371 · last release 2026-10-21 · [PyPI](https://pypi.org/project/llama-cloud/) · [source](https://github.com/run-llama/llama-parse-py)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Llama Cloud Python library provides convenient access to the Llama Cloud REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)

parsing = client.parsing.create(
    tier="agentic",
    version="latest",
    file_id="abc1234",
)
print(parsing.id)
```

...

</details>

### prime-sandboxes

Prime Intellect Sandboxes SDK - Manage remote code execution environments

`pip install prime-sandboxes` · installs (wheel) · licence: MIT License · rank 2383 · last release 2026-11-06 · [PyPI](https://pypi.org/project/prime-sandboxes/) · [docs](https://github.com/PrimeIntellect-ai/prime/tree/main/packages/prime-sandboxes) · [source](https://github.com/PrimeIntellect-ai/prime.git)

<details><summary>README extract</summary>

Lightweight Python SDK for managing Prime Intellect sandboxes - secure remote code execution environments.

Features:
- Synchronous and async clients - Use with sync or async/await code
- Full sandbox lifecycle - Create, list, execute commands, upload/download files, delete
- Type-safe - Full type hints and Pydantic models ...

Example:
```python
from prime_sandboxes import APIClient, SandboxClient, CreateSandboxRequest, StartCommand

# Initialize
client = APIClient(api_key="your-api-key")
sandbox_client = SandboxClient(client)

# Create a VM-backed sandbox.
request = CreateSandboxRequest(
    name="my-sandbox",
    docker_image="python:3.11-slim",
    cpu_cores=2,
    memory_gb=4,
)

...
```

...

</details>

### sarif-om

Classes implementing the SARIF 2.1.0 object model.

`pip install sarif-om` · installs (wheel) · licence: MIT License · rank 2386 · last release 2019-10-05 · [PyPI](https://pypi.org/project/sarif-om/)

<details><summary>README extract</summary>

Python classes for the SARIF 2.1.0 object model

Example:
```python
pip install sarif-python-om

import sarif_om
```

Sections: sarif-python-om, Usage, Description, Generation

</details>

### lark-oapi

Lark OpenAPI SDK for Python

`pip install lark-oapi` · installs (wheel) · licence: MIT License · rank 2391 · last release 2026-10-15 · [PyPI](https://pypi.org/project/lark-oapi/) · [source](https://github.com/larksuite/oapi-sdk-python)

<details><summary>README extract</summary>

The Feishu Open Platform provides server-side APIs for messaging, contacts,
approval, sheets, Base, and many other product capabilities. This SDK wraps the
repeated platform work around API calls, including token management, request
signing, encryption/decryption, event dispatching, and typed request/response
models. ...

Example:
```python
import lark_oapi as lark
from lark_oapi.api.im.v1 import *

client = lark.Client.builder() \
    .app_id("cli_xxx") \
    .app_secret("your_app_secret") \
    .build()

request = CreateMessageRequest.builder() \
    .receive_id_type("chat_id") \
    .request_body(CreateMessageRequestBody.builder()
        .receive_id("oc_xxx")
...
```

...

</details>

### promise

Promises/A+ implementation for Python

`pip install promise` · installs from source (sdist only) · licence: MIT License · rank 2392 · last release 2019-12-18 · [PyPI](https://pypi.org/project/promise/)

<details><summary>README extract</summary>

This is a implementation of Promises in Python. It is a super set of
Promises/A+ designed to have readable, performant code and to provide
just the extensions that are absolutely necessary for using promises in
Python.

Its fully compatible with the Promises/A+
spec

Example:
```python
from promise import Promise

promise = Promise(
    lambda resolve, reject: resolve('RESOLVED!')
)
```

Sections: Promise, Usage, API, Promise(resolver), Class Methods, Promise.resolve(value), Promise.reject(value), Promise.all(list), Promise.cast(obj), Promise.for\_dict(d), Promise.is\_thenable(obj), Promise.promisify(func), Instance Methods, promise.then(did\_fulfill, did\_reject)

</details>

### yappi

Yet Another Python Profiler

`pip install yappi` · installs (wheel) · licence: MIT License · rank 2400 · last release 2026-03-17 · [PyPI](https://pypi.org/project/yappi/)

<details><summary>README extract</summary>

A tracing profiler that is multithreading, asyncio and gevent aware.

Features:
- Fast: Yappi is fast. It is completely written in C and lots of love and care went into making it fast.
- Unique: Yappi supports multithreaded, asyncio and gevent profiling. Tagging/filtering multiple profiler results has interesting use cases. ...

Example:
```python
import yappi

def a():
    for _ in range(10000000):  # do something CPU heavy
        pass

yappi.set_clock_type("cpu") # Use set_clock_type("wall") for wall time
yappi.start()
a()

yappi.get_func_stats().print_all()
yappi.get_thread_stats().print_all()
'''

Clock type: CPU
Ordered by: totaltime, desc

...
```

...

</details>

### json-schema-to-pydantic

A Python library for automatically generating Pydantic v2 models from JSON Schema definitions

`pip install json-schema-to-pydantic` · installs (wheel) · licence: MIT · rank 2403 · last release 2026-10-21 · [PyPI](https://pypi.org/project/json-schema-to-pydantic/) · [docs](https://github.com/richard-gyiko/json-schema-to-pydantic#readme)

<details><summary>README extract</summary>

A Python library for automatically generating Pydantic v2 models from JSON Schema definitions.

Features:
- Converts JSON Schema to Pydantic v2 models

 - References ($ref) with circular reference detection
 - Combiners (allOf, anyOf, oneOf) with discriminated unions where possible
 - Type constraints and validations
 - Array and object validations
 - ...

Example:
```python
from json_schema_to_pydantic import create_model

# Define your JSON Schema
schema = {
    "title": "User",
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "age": {"type": "integer", "minimum": 0}
    },
    "required": ["name", "email"]
}

...
```

...

</details>

### prime-tunnel

Prime Intellect Tunnel SDK - Expose local services via secure tunnels

`pip install prime-tunnel` · installs (wheel) · licence: MIT License · rank 2409 · last release 2026-11-02 · [PyPI](https://pypi.org/project/prime-tunnel/) · [docs](https://github.com/PrimeIntellect-ai/prime/tree/main/packages/prime-tunnel) · [source](https://github.com/PrimeIntellect-ai/prime.git)

<details><summary>README extract</summary>

Expose local services via secure tunnels on Prime infrastructure.

Example:
```python
from prime_tunnel import Tunnel

# Create and start a tunnel
async with Tunnel(local_port=8765) as tunnel:
    print(f"Tunnel URL: {tunnel.url}")
    # Your local service on port 8765 is now accessible at tunnel.url
```

Sections: Prime Tunnel SDK, Quick Start, Keeping a tunnel up, CLI Usage, Documentation, Related Packages

</details>

### tibs

A sleek Python library for binary data.

`pip install tibs` · installs (wheel) · licence: MIT License · rank 2425 · last release 2026-10-06 · [PyPI](https://pypi.org/project/tibs/) · [docs](https://tibs.readthedocs.io/)

<details><summary>README extract</summary>

A sleek Python library for binary data

``tibs`` is a Python library for binary data.
It's 100% written in Rust and has excellent performance.

Use it for packets, registers, instruction
formats, bitsets, compressed data and streams where fields can have many different
interpretations and be any number of bits long. ...

Features:
The tibs library provides two main classes: `Tibs`, which is an immutable sequence of bits
(similar to how `bytes` works in Python as a sequence of bytes) and `Mutibs`, which is a mutable version (similar to `bytearray` in Python). ...

Example:
```python
>>> from tibs import Tibs
>>> # A 5-bit header, a message, then 3 bits of padding: nothing is byte aligned.
>>> frame = Tibs('0b10110') + b'the cat rarely blinked' + [0, 0, 0]
...

</details>

### python-xlib

Python X Library

`pip install python-xlib` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 2429 · last release 2022-12-25 · [PyPI](https://pypi.org/project/python-xlib/)

_README extract left out: share-alike licence._

### openapi-core

client-side and server-side support for the OpenAPI Specification v3

`pip install openapi-core` · installs (wheel) · licence: BSD License · rank 2430 · last release 2026-04-02 · [PyPI](https://pypi.org/project/openapi-core/) · [docs](https://openapi-core.readthedocs.io) · [source](https://github.com/python-openapi/openapi-core)

<details><summary>README extract</summary>

Openapi-core is a Python library that provides client-side and server-side support
for the OpenAPI v3.0
and OpenAPI v3.1
and OpenAPI v3.2 specifications.

Features:
- Validation and unmarshalling of request and response data (including webhooks)
- Integration with popular libraries (Requests, Werkzeug) and frameworks (Django, Falcon, Flask, Starlette) ...

Example:
```python
from openapi_core import OpenAPI

openapi = OpenAPI.from_file_path('openapi.json')
```

Sections: openapi-core, About, Key features, Documentation, Integrations compatibility matrix, First steps, Related projects

</details>

### jinja2-simple-tags

Base classes for quick-and-easy template tag development

`pip install jinja2-simple-tags` · installs (wheel) · licence: BSD License · rank 2431 · last release 2024-03-06 · [PyPI](https://pypi.org/project/jinja2-simple-tags/)

<details><summary>README extract</summary>

`jinja2-simple-tags` is a library that provides a simple way to create custom template
tags in Jinja2 templates.

- `python` >= 3.6
- `Jinja2` >= 2.10

Example:
```python
from datetime import datetime
from jinja2_simple_tags import StandaloneTag

class NowExtension(StandaloneTag):
    tags = {"now"}

    def render(self, format="%Y-%m-%d %H:%I:%S"):
        return datetime.now().strftime(format)
```

Sections: jinja2-simple-tags, Compatibility, Usage, `StandaloneTag`, Escaping, `ContainerTag`, `InclusionTag`, Context Inheritance, Context, Assignment

</details>

### boxsdk

Official Box Python SDK

`pip install boxsdk` · installs (wheel) · licence: Apache Software License · rank 2434 · last release 2026-10-15 · [PyPI](https://pypi.org/project/boxsdk/)

<details><summary>README extract</summary>

- Introduction
- Supported versions
 - Version v4
 - Version v10
 - Which Version Should I Use?
- Installing
- Getting Started
- Authentication
- Documentation
- Migration guides
- Versioning
 - Version schedule
- Contributing
- FIPS 140-2 Compliance
- Questions, Bugs, and Feature Requests?
- Copyright and License ...

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

### djangorestframework-api-key

API key permissions for the Django REST Framework

`pip install djangorestframework-api-key` · installs (wheel) · licence: MIT · rank 2457 · last release 2025-04-04 · [PyPI](https://pypi.org/project/djangorestframework-api-key/) · [docs](https://florimondmanca.github.io/djangorestframework-api-key/)

<details><summary>README extract</summary>

API key permissions for the Django REST Framework.

Django REST Framework API Key is a library for allowing server-side clients to safely use your API. These clients are typically third-party backends and services (i.e. _machines_) which do not have a user account but still need to interact with your API in a secure way.

Features:
- ✌️ Simple to use: create, view and revoke API keys via the admin site, or use built-in helpers to create API keys programmatically.
- 🔒 As secure as possible: API keys are treated with the same level of care as user passwords. ...

Sections: Django REST Framework API Key, Introduction, Features, Should I use API keys?, Quickstart, 3.1.0 - 2025-04-04, Added, 3.0.0 - 2023-09-30, Changed, Removed, 2.3.0 - 2023-01-19, Fixed

</details>

### hatch-requirements-txt

Hatchling plugin to read project dependencies from requirements.txt

`pip install hatch-requirements-txt` · installs (wheel) · licence: MIT License · rank 2468 · last release 2024-01-24 · [PyPI](https://pypi.org/project/hatch-requirements-txt/) · [source](https://github.com/repo-helper/hatch-requirements-txt)

<details><summary>README extract</summary>

Hatchling plugin to read project dependencies from requirements.txt

Sections: hatch-requirements-txt, Usage, Requirements file format

</details>

### pyspellchecker

Pure python spell checker based on work by Peter Norvig

`pip install pyspellchecker` · installs (wheel) · licence: MIT · rank 2491 · last release 2026-10-10 · [PyPI](https://pypi.org/project/pyspellchecker/) · [docs](https://pyspellchecker.readthedocs.io/)

<details><summary>README extract</summary>

Pure Python Spell Checking based on Peter
Norvig's blog post on setting
up a simple spell checking algorithm.

It uses a Levenshtein Distance
algorithm to find permutations within an edit distance of 2 from the
original word. ...

Example:
```python
from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))
```

Sections: pyspellchecker, Quickstart, Non-English Dictionaries, Dictionary Creation and Updating, Additional Methods

</details>

### flake8-bugbear

A plugin for flake8 finding likely bugs and design problems in your program. Contains warnings that don't belong in pyflakes and pycodestyle.

`pip install flake8-bugbear` · installs (wheel) · licence: MIT License · rank 2500 · last release 2026-10-27 · [PyPI](https://pypi.org/project/flake8-bugbear/)

<details><summary>README extract</summary>

A plugin for `flake8` finding likely bugs and design problems in your
program. Contains warnings that don't belong in `pyflakes` and
`pycodestyle`:
It is felt that these lints don't belong in the main Python tools as they
are very opinionated and do not have a PEP or standard behind them. ...

Sections: flake8-bugbear, List of warnings, Opinionated warnings, How to enable opinionated warnings, Configuration, Tests / Lints, 26.10.27, 26.9.30, 26.9.9, 25.11.29, 25.10.21, 24.12.12, 24.10.31, 24.8.19

</details>

### apify-client

Apify API client for Python

`pip install apify-client` · installs (wheel) · licence: Apache-2.0 · rank 2507 · last release 2026-10-27 · [PyPI](https://pypi.org/project/apify-client/) · [docs](https://docs.apify.com/api/client/python/docs/overview/introduction) · [source](https://github.com/apify/apify-client-python)

<details><summary>README extract</summary>

The official Python client for the Apify REST API.

`apify-client` lets you talk to the Apify platform from Python — run Actors, manage storages (datasets, key-value stores, request queues), schedule tasks, configure webhooks, and use everything else exposed by the Apify API. ...

Features:
- Synchronous and asynchronous clients — pick `ApifyClient` or `ApifyClientAsync` to match your codebase; both expose the same API (Asyncio support). ...

Example:
```python
from apify_client import ApifyClient

client = ApifyClient('MY-APIFY-TOKEN')

# Start an Actor and wait for it to finish.
run = client.actor('apify/hello-world').call(
    run_input={'message': 'Hello, Apify!'},
)
if run is None:
    raise RuntimeError('Actor run was not found.')

# Iterate items from the run's default dataset.
...
...

</details>

### QtPy

Provides an abstraction layer on top of the various Qt bindings (PyQt5/6 and PySide2/6).

`pip install QtPy` · installs (wheel) · licence: MIT License · rank 2511 · last release 2025-02-11 · [PyPI](https://pypi.org/project/QtPy/) · [source](https://github.com/spyder-ide/qtpy)

<details><summary>README extract</summary>

*Copyright © 2009– The Spyder Development Team*

QtPy is a small abstraction layer that lets you
write applications using a single API call to either PyQt or PySide.

It provides support for PyQt5, PySide2, PyQt6 and PySide6 using the Qt5 layout
(where the QtGui module has been split into QtGui and QtWidgets). ...

Sections: QtPy: Abstraction layer for PyQt5/PySide2/PyQt6/PySide6, Description, Requirements, Module aliases and constants, Compat module, Type checker integration, Mypy, Pyright/Pylance

</details>

### lm-format-enforcer

Enforce the output format (JSON Schema, Regex etc) of a language model

`pip install lm-format-enforcer` · installs (wheel) · licence: MIT License · rank 2515 · last release 2025-08-24 · [PyPI](https://pypi.org/project/lm-format-enforcer/) · [docs](https://github.com/noamgat/lm-format-enforcer) · [source](https://github.com/noamgat/lm-format-enforcer)

<details><summary>README extract</summary>

Enforce the output format (JSON Schema, Regex etc) of a language model

Language models are able to generate text, but when requiring a precise output format, they do not always perform as instructed.
Various prompt engineering techniques have been introduced to improve the robustness of the generated text, but they are not always sufficient. ...

...

</details>

### toons

A high-performance TOON (Token Oriented Object Notation) parser and serializer for Python, implemented in Rust.

`pip install toons` · installs (wheel) · licence: Apache-2.0 · rank 2523 · last release 2026-09-29 · [PyPI](https://pypi.org/project/toons/) · [docs](https://toons.readthedocs.io) · [source](https://github.com/alesanfra/toons)

<details><summary>README extract</summary>

A high-performance TOON (Token Oriented Object Notation) parser and serializer for Python.

TOONS is a Rust implementation with a Python interface that mirrors the `json`
module, for the TOON format: a token-efficient serialization format designed
for Large Language Model contexts. ...

Features:
TOON uses 30-60% fewer tokens than the equivalent JSON, which matters when
data goes into a prompt. This example saves 40%:

JSON (26 tokens):

TOON (16 tokens):

> Token counts measured with the Anthropic Claude tokenizer. ...

Example:
```python
import toons

# Parse a TOON string
data = toons.loads("""
name: Alice
age: 30
tags[3]: python,rust,toon
""")
print(data)
# {'name': 'Alice', 'age': 30, 'tags': ['python', 'rust', 'toon']}

# Serialize to TOON
...

</details>

### pytest-instafail

pytest plugin to show failures instantly

`pip install pytest-instafail` · installs (wheel) · licence: BSD License · rank 2531 · last release 2023-03-31 · [PyPI](https://pypi.org/project/pytest-instafail/)

<details><summary>README extract</summary>

pytest-instafail is a plugin for pytest that shows
failures and errors instantly instead of waiting until the end of test session.

You will need the following prerequisites in order to use pytest-instafail:

- Python 3.7+ or PyPy3
- pytest 5 or newer

Sections: pytest-instafail, Requirements, Resources

</details>

### rarfile

RAR archive reader for Python

`pip install rarfile` · installs (wheel) · licence: ISC License (ISCL) · rank 2539 · last release 2026-08-02 · [PyPI](https://pypi.org/project/rarfile/)

<details><summary>README extract</summary>

This is Python module for RAR archive reading.
The interface follows the style of zipfile.
Licensed under ISC license.

Features:

* Supports both RAR3 and RAR5 format archives.
* Supports multi volume archives.
* Supports Unicode filenames.
* Supports password-protected archives.
* Supports archive and file comments. ...

</details>

### gitignore-parser

A spec-compliant gitignore parser for Python 3.5+

`pip install gitignore-parser` · installs from source (sdist only) · licence: MIT License · rank 2548 · last release 2025-08-25 · [PyPI](https://pypi.org/project/gitignore-parser/)

<details><summary>README extract</summary>

A spec-compliant gitignore parser for Python 3.5+

</details>

### cloudflare

The official Python library for the cloudflare API

`pip install cloudflare` · installs (wheel) · licence: Apache Software License · rank 2568 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cloudflare/) · [source](https://github.com/cloudflare/cloudflare-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Cloudflare Python library provides convenient access to the Cloudflare REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from cloudflare import Cloudflare

client = Cloudflare(
    api_token=os.environ.get("CLOUDFLARE_API_TOKEN"),  # This is the default and can be omitted
)

zone = client.zones.create(
    account={"id": "023e105f4ecef8ad9ca31a8372d0c353"},
    name="example.com",
    type="full",
)
print(zone.id)
```

...

</details>

### influxdb

InfluxDB client

`pip install influxdb` · installs (wheel) · licence: MIT License · rank 2575 · last release 2024-04-18 · [PyPI](https://pypi.org/project/influxdb/)

<details><summary>README extract</summary>

The v1 client libraries for InfluxDB were typically developed and maintained by
community members. For InfluxDB 3.0 users, this library is succeeded by the
lightweight v3 client library.
For InfluxDB 2.0 users, look at the v2 client library. ...

Example:
```python
$ python

>>> from influxdb import InfluxDBClient

>>> json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "value": 0.64
        }
    }
]

...
```

Sections: InfluxDB-Python, InfluxDB pre v1.1.0 users, Dependencies, Documentation, Examples, Source code, TODO

</details>

### flufl.lock

NFS-safe file locking with timeouts for POSIX and Windows

`pip install flufl.lock` · installs (wheel) · licence: Apache Software License · rank 2580 · last release 2026-10-12 · [PyPI](https://pypi.org/project/flufl.lock/) · [docs](https://flufllock.readthedocs.io) · [source](https://gitlab.com/flufl/flufl.lock.git)

<details><summary>README extract</summary>

NFS-safe file locking with timeouts for POSIX and Windows.

The `flufl.lock` library provides an NFS-safe file-based locking algorithm
influenced by the GNU/Linux `open(2)` manpage, under the description of the
`O_EXCL` option. ...

Sections: flufl.lock, Project details

</details>

### pydantic-handlebars

Handlebars template engine for composing LLM prompts, built on Pydantic

`pip install pydantic-handlebars` · installs (wheel) · licence: MIT · rank 2583 · last release 2026-05-25 · [PyPI](https://pypi.org/project/pydantic-handlebars/) · [source](https://github.com/pydantic/pydantic-handlebars)

<details><summary>README extract</summary>

A Handlebars template engine for composing LLM prompts, built on Pydantic.

Designed for AI/agent developers who build system prompts from dynamic data — few-shot examples,
user-specific context, tool descriptions, and other content that shouldn't be hardcoded. ...

Features:
In the age of agent development, templates are everywhere — system prompts, user-facing messages, tool descriptions. But templates have traditionally had a weakness: no type checking. ...

Example:
```python
from pydantic_handlebars import render

# Simple variable interpolation
print(render('Hello {{name}}!', {'name': 'World'}))
# > Hello World!

# Dot-notation paths
print(render('{{person.name}}', {'person': {'name': 'Alice'}}))
# > Alice

# Block helpers
...
```

...

</details>

### nanobind

nanobind: tiny and efficient C++/Python bindings

`pip install nanobind` · installs (wheel) · licence: BSD License · rank 2617 · last release 2026-09-18 · [PyPI](https://pypi.org/project/nanobind/)

<details><summary>README extract</summary>

_nanobind_ is a small binding library that exposes C++ types in Python and
vice versa. It is reminiscent of
Boost.Python
and pybind11 and uses near-identical
syntax. In contrast to these existing tools, nanobind is more efficient:
bindings compile in a shorter amount of time, produce smaller binaries, and
have better runtime performance. ...

</details>

### cassandra-driver

Apache Cassandra Python Driver

`pip install cassandra-driver` · installs (wheel) · licence: Apache-2.0 · rank 2628 · last release 2026-07-06 · [PyPI](https://pypi.org/project/cassandra-driver/) · [docs](https://docs.datastax.com/en/developer/python-driver/latest/) · [source](https://github.com/apache/cassandra-python-driver/)

<details><summary>README extract</summary>

A modern, feature-rich and highly-tunable Python client library for Apache Cassandra (2.1+) and
DataStax Enterprise (4.7+) using exclusively Cassandra's binary protocol and Cassandra Query Language v3.

The driver supports Python 3.10 through 3.14.

Note: DataStax products do not support big-endian systems.

Features:
* Synchronous and Asynchronous APIs
* Simple, Prepared, and Batch statements
* Asynchronous IO, parallel execution, request pipelining
* Connection pooling
* Automatic node discovery
* Automatic reconnection
* Configurable load balancing and retry ...

Sections: Apache Cassandra Python Driver, Features, Documentation, Object Mapper, Reporting Problems, Getting Help

</details>

### pydantic-xml

pydantic xml extension

`pip install pydantic-xml` · installs (wheel) · licence: OSI Approved; Public Domain · rank 2629 · last release 2026-10-18 · [PyPI](https://pypi.org/project/pydantic-xml/) · [docs](https://pydantic-xml.readthedocs.io) · [source](https://github.com/dapper91/pydantic-xml)

<details><summary>README extract</summary>

`pydantic-xml` is a pydantic extension providing model fields xml binding
and xml serialization / deserialization.
It is closely integrated with `pydantic` which means it supports most of its features.

Features:
- pydantic v1 / v2 support
- flexible attributes, elements and text binding
- python collection types support (`Dict`, `TypedDict`, `List`, `Set`, `Tuple`, ...)
- `Union` type support
- pydantic generic models support ...

Example:
```python
class Product(BaseXmlModel):
    status: Literal['running', 'development'] = attr()  # extracted from the 'status' attribute
    launched: Optional[int] = attr(default=None)  # extracted from the 'launched' attribute
    title: str  # extracted from the element text

class Company(BaseXmlModel):
...
```

...

</details>

### agentmail

(no summary)

`pip install agentmail` · installs (wheel) · licence: MIT License · rank 2631 · last release 2026-11-06 · [PyPI](https://pypi.org/project/agentmail/) · [source](https://github.com/agentmail-to/agentmail-python)

<details><summary>README extract</summary>

The Agentmail Python library provides convenient access to the Agentmail APIs from Python.

Example:
```python
from agentmail import AgentMail

client = AgentMail(
    api_key="<token>",
)

client.inboxes.create()
```

Sections: Agentmail Python Library, Reference, Usage, Async Client, Exception Handling, Advanced, Access Raw Response Data, Retries, Timeouts, Custom Client, Websockets

</details>

### django-ratelimit

Cache-based rate-limiting for Django.

`pip install django-ratelimit` · installs (wheel) · licence: Apache Software License · rank 2635 · last release 2023-07-24 · [PyPI](https://pypi.org/project/django-ratelimit/)

<details><summary>README extract</summary>

Django Ratelimit provides a decorator to rate-limit views. Limiting can
be based on IP address or a field in the request--either a GET or POST
variable.

:Code:
:License: Apache Software License 2.0; see LICENSE file
:Issues:
:Documentation:

</details>

### impit

A library for making HTTP requests through browser impersonation

`pip install impit` · installs (wheel) · licence: Apache Software License · rank 2637 · last release 2026-10-22 · [PyPI](https://pypi.org/project/impit/) · [docs](https://apify.github.io/impit/python) · [source](https://github.com/apify/impit)

<details><summary>README extract</summary>

> This documents the `impit` Python package, which provides bindings for the `impit` library.
> See documentation for the JavaScript/TypeScript version of `impit` here.

`impit` is a Python package that provides bindings for the `impit` library. ...

Example:
```python
import asyncio
from impit import AsyncClient

async def main():
    impit = AsyncClient(http3=True, browser='firefox')

    response = await impit.get(
        "
    );

    print(response.status_code)
    print(response.text)
    print(response.http_version)

asyncio.run(main())
```

Sections: `impit` for Python, Compatibility, Usage

</details>

### DataProperty

Python library for extract property from data.

`pip install DataProperty` · installs (wheel) · licence: MIT License · rank 2643 · last release 2026-05-09 · [PyPI](https://pypi.org/project/DataProperty/) · [source](https://github.com/thombashi/DataProperty)

<details><summary>README extract</summary>

A Python library for extract property from data.

Example:
```python
>>> from dataproperty import DataProperty
>>> DataProperty(-1.1)
data=-1.1, type=REAL_NUMBER, align=right, ascii_width=4, int_digits=1, decimal_places=1, extra_len=1
```

Sections: Summary, Usage, Extract property of data, e.g. Extract a `float` value property, e.g. Extract a `int` value property, e.g. Extract a `str` (ascii) value property, e.g. Extract a `str` (multi-byte) value property, e.g. Extract a time (`datetime`) value property, e.g. Extract a `bool` value property, Extract data property for each element from a matrix, Extract properties for each column from a matrix, Dependencies, Optional dependencies

</details>

### ConfigUpdater

Parser like ConfigParser but for updating configuration files

`pip install ConfigUpdater` · installs (wheel) · licence: MIT · rank 2645 · last release 2026-11-02 · [PyPI](https://pypi.org/project/ConfigUpdater/) · [docs](https://configupdater.readthedocs.io/) · [source](https://github.com/pyscaffold/configupdater/)

<details><summary>README extract</summary>

| | |

| CI/CD | [][Tests-link] [][Coverage-link] [][Publish-link] [][sponsor-link] |
| Package | [][PyPI_ver-link] [][Conda-link] [][PyPI_down-link] [][PyPI_py-link] |
| Details | [][uv-link] [][ruff-link] [][pytest-link] [][precommit-link] [][mypy-link] [][MIT-link] [][rtd-link] | ...

Features:
The key differences to [ConfigParser] are:

- minimally invasive changes in the updated configuration file,
- proper handling of comments,
- only a single config file can be updated at a time,
- the original case of sections and keys is kept, ...

Example:
```python
from configupdater import ConfigUpdater

updater = ConfigUpdater()
updater.read("setup.cfg")
```

Sections: Features, Usage, Adding and removing options, Adding and removing sections, Notes

</details>

### docker-image-py

Parse docker image as distribution does.

`pip install docker-image-py` · installs (wheel) · licence: Apache-2.0 · rank 2646 · last release 2026-06-29 · [PyPI](https://pypi.org/project/docker-image-py/) · [source](https://github.com/realityone/docker-image-py)

<details><summary>README extract</summary>

Parse docker image as distribution does.

Example:
```python
>>> from docker_image import reference
>>>
>>> ref = reference.Reference.parse_normalized_named('ubuntu')
>>> print(ref)
{'name': 'docker.io/library/ubuntu', 'tag': None, 'digest': None}
>>> print(ref.familiar_name())
ubuntu
>>> ref = reference.Reference.parse_normalized_named('containous/traefik')
>>> print(ref)
...
```

Sections: docker-image-py, Usage, Parse Docker Image Names, Reference

</details>

### SQLAlchemy-JSONField

SQLALchemy JSONField implementation for storing dicts at SQL

`pip install SQLAlchemy-JSONField` · installs (wheel) · licence: Apache-2.0 · rank 2647 · last release 2026-05-11 · [PyPI](https://pypi.org/project/SQLAlchemy-JSONField/) · [source](https://github.com/penguinolog/sqlalchemy_jsonfield)

<details><summary>README extract</summary>

SQLALchemy JSONField implementation for storing dicts at SQL independently from JSON type support.

Features:
SqlAlchemy provides JSON field support for several database types (PostgreSQL and MySQL for now)
and semi-working dict <-> JSON <-> VARCHAR example, but... ...

Example:
```python
import sqlalchemy_jsonfield

class ExampleTable(Base):
    tablename = table_name
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    row_name = sqlalchemy.Column(
        sqlalchemy.Unicode(64),
        unique=True,
    )
    json_record = sqlalchemy.Column(
        sqlalchemy_jsonfield.JSONField(
...
```

Sections: SQLAlchemy-JSONField, Why?, Solution, Pros, Usage, CI systems

</details>

### sparkmeasure

Python API for sparkMeasure, a tool for performance troubleshooting of Apache Spark workloads.

`pip install sparkmeasure` · installs (wheel) · licence: Apache Software License · rank 2648 · last release 2026-05-19 · [PyPI](https://pypi.org/project/sparkmeasure/) · [docs](https://github.com/lucacanali/sparkMeasure) · [source](https://github.com/lucacanali/sparkMeasure)

<details><summary>README extract</summary>

SparkMeasure is a tool for performance troubleshooting of Apache Spark workloads.
It simplifies the collection and analysis of Spark performance metrics. The bulk of sparkMeasure is written in Scala.
This package contains the Python API for sparkMeasure. ...

</details>

### trame-server

Internal server side implementation of trame

`pip install trame-server` · installs (wheel) · licence: Apache Software License · rank 2667 · last release 2026-10-09 · [PyPI](https://pypi.org/project/trame-server/)

<details><summary>README extract</summary>

trame-server is the server implementation of trame.
This Python library provide the server implementation of the shared state and controller along with the definition of the web server.
The web server aims to be flexible so it can be use within a Jupyter environment or as a standalone desktop application. ...

Sections: trame-server: server implementation of trame, Usage, Enjoying trame?

</details>

### tabledata

tabledata is a Python library to represent tabular data. Used for pytablewriter/pytablereader/SimpleSQLite/etc.

`pip install tabledata` · installs (wheel) · licence: MIT License · rank 2671 · last release 2026-05-11 · [PyPI](https://pypi.org/project/tabledata/) · [docs](https://tabledata.rtfd.io/) · [source](https://github.com/thombashi/tabledata)

<details><summary>README extract</summary>

tabledata is a Python library to represent tabular data. Used for pytablewriter/pytablereader/SimpleSQLite/etc.

Sections: Summary, Dependencies, Optional Python packages, Documentation

</details>

### trame-client

Internal client of trame

`pip install trame-client` · installs (wheel) · licence: MIT License · rank 2675 · last release 2026-10-06 · [PyPI](https://pypi.org/project/trame-client/)

<details><summary>README extract</summary>

trame-client is the generic single page application that come with trame.
trame-client provides the infrastructure on the client-side (browser) to connect to a trame server, synchronize
its state with the server, make method call, load dynamically components and feed a dynamic template provided by the server. ...

Sections: trame-client: core client for trame, Usage, Enjoying trame?, Runtime configuration, JavaScript dependency

</details>

### trame

Trame, a framework to build applications in plain Python

`pip install trame` · installs (wheel) · licence: Apache Software License · rank 2688 · last release 2026-09-09 · [PyPI](https://pypi.org/project/trame/)

<details><summary>README extract</summary>

trame - a web framework that weaves together open source components into customized visual analytics easily.

trame is French for

* the core that ties things together
* a guide providing the essence of a task

With trame, create stunning, interactive web applications compactly and intuitively. ...

Sections: trame: simple, powerful, innovative, 3D Visualization, Rich Features, Problem Focused, Desktop to cloud, Usage, Enjoying trame?, Optional dependencies, Environments variables, Life cycle callbacks, Reserved state entries

</details>

### inject

Python dependency injection framework.

`pip install inject` · installs (wheel) · licence: Apache-2.0 · rank 2695 · last release 2026-07-13 · [PyPI](https://pypi.org/project/inject/) · [source](https://github.com/ivankorobkov/python-inject)

<details><summary>README extract</summary>

Dependency injection the python way, the good way.

Features:
* Fast.
* Thread-safe.
* Simple to use.
* Does not steal class constructors.
* Does not try to manage your application object graph.
* Transparently integrates into tests.
* Autoparams leveraging type annotations. ...

Example:
```python
@inject.autoparams
def refresh_cache(cache: RedisCache, db: DbInterface):
    pass
```

Sections: python-inject, Key features, Autoparams example, Step-by-step example, Context managers, Usage with Django, Composable configurations, Thread-safety, Binding types, Disabling runtime binding, Keys, Why no scopes?, Links

</details>

### trame-vtk

VTK widgets for trame

`pip install trame-vtk` · installs (wheel) · licence: BSD License · rank 2696 · last release 2026-09-22 · [PyPI](https://pypi.org/project/trame-vtk/)

<details><summary>README extract</summary>

trame-vtk extend trame widgets with components that can interface with VTK and/or ParaView.

VTK integration in trame allows you to create rich visualization and data processing applications by leveraging the Python wrapping of the VTK library. ...

Example:
```python
from trame.widgets import vtk

def end():
    pass

remote_view = vtk.vtkRemoteView(
    view=...,               # Instance of vtkRenderWindow (required)
    ref=...,                # Identifier for this component
    interactive_quality=60, # [0, 100] 0 for fastest render, 100 for best quality
...
```

Sections: VTK/ParaView widgets for trame, Usage, Enjoying trame?, Trame widgets, VtkRemoteView, How to use it?, Examples, VtkLocalView, Interactor Settings, VtkRemoteLocalView, Namespace parameter

</details>

### webvtt-py

WebVTT reader, writer and segmenter

`pip install webvtt-py` · installs (wheel) · licence: MIT · rank 2702 · last release 2026-11-01 · [PyPI](https://pypi.org/project/webvtt-py/)

<details><summary>README extract</summary>

`webvtt-py` is a Python library for reading, writing and converting WebVTT caption files. It also features caption segmentation useful when captioning HLS videos.

Documentation is available at

Example:
```python
import webvtt

for caption in webvtt.read('captions.vtt'):
    print(caption.identifier)  # cue identifier if any
    print(caption.start)       # cue start time
    print(caption.end)         # cue end time
    print(caption.text)        # cue payload
    print(caption.voice)       # cue voice span if any
```

Sections: webvtt-py, Usage, Writing captions, Segmenting for HLS, Converting captions from other formats, CLI

</details>

### json-logic

Build complex rules, serialize them as JSON, and execute them in Python

`pip install json-logic` · installs (wheel) · licence: MIT License · rank 2716 · last release 2015-12-04 · [PyPI](https://pypi.org/project/json-logic/)

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

### cron-converter

Cron string parser and scheduler for Python

`pip install cron-converter` · installs (wheel) · licence: MIT · rank 2721 · last release 2026-09-30 · [PyPI](https://pypi.org/project/cron-converter/)

<details><summary>README extract</summary>

Cron-converter provides a Cron string parser ( from string/lists to string/lists ) and iteration for the datetime object with a cron like format.

This project would be a transposition in Python of JS cron-converter by roccivic.

Example:
```python
# Parse a string to init a schedule
cron_instance.from_string('*/5 * * * *')

# Raw datetime without timezone info (not aware)
reference = datetime.now()
# Get the iterator, initialised to now
schedule = cron_instance.schedule(reference)

# Calls to .next() and .prev()
# return a Datetime object

# Examples with time now: '2021-01-01T09:32:00
...
```

...

</details>

### tbb

Intel® oneAPI Threading Building Blocks

`pip install tbb` · installs (wheel) · licence: Other/Proprietary License · rank 2734 · last release 2026-10-16 · [PyPI](https://pypi.org/project/tbb/)

<details><summary>README extract</summary>

Intel® oneAPI Threading Building Blocks (oneTBB) x86_64 dynamic libraries for Windows*. Intel® oneAPI Threading Building Blocks (oneTBB) is a flexible performance library that supports scalable parallel programming using C++ code compliant with ISO C++ standard.

</details>

### array-api-compat

A wrapper around NumPy and other array libraries to make them compatible with the Array API standard

`pip install array-api-compat` · installs (wheel) · licence: MIT · rank 2754 · last release 2026-10-25 · [PyPI](https://pypi.org/project/array-api-compat/) · [source](https://github.com/data-apis/array-api-compat/)

<details><summary>README extract</summary>

This is a small wrapper around common array libraries that is compatible with
the Array API standard. Currently,
NumPy, CuPy, PyTorch, Dask, JAX, mparray, ndonnx, `sparse` and dpnp are
supported. If you want
support for other array libraries, or if you encounter any issues, please open
an issue.

See the documentation for more details

</details>

### pynvml

Python utilities for the NVIDIA Management Library

`pip install pynvml` · installs (wheel) · licence: BSD License · rank 2764 · last release 2025-09-05 · [PyPI](https://pypi.org/project/pynvml/) · [source](https://github.com/gpuopenanalytics/pynvml)

<details><summary>README extract</summary>

> [!WARNING]
> This project has been deprecated.
> The `pynvml` module is NOT developed or maintained in this project!
> This project provides unofficial NVML Python utilities (i.e. the `pynvml_utils` module).
> The `pynvml_utils` module is intended for demonstration purposes only.
> There is no guarantee for long-term maintenence or support. ...

Example:
```python
from pynvml_utils import nvidia_smi
nvsmi = nvidia_smi.getInstance()
nvsmi.DeviceQuery('memory.free, memory.total')
```

</details>

### apify-fingerprint-datapoints

Browser fingerprint datapoints collected by Apify

`pip install apify-fingerprint-datapoints` · installs (wheel) · licence: Apache Software License · rank 2765 · last release 2026-08-05 · [PyPI](https://pypi.org/project/apify-fingerprint-datapoints/) · [docs](https://docs.apify.com/academy/anti-scraping/techniques/fingerprinting) · [source](https://github.com/apify/fingerprint-suite)

<details><summary>README extract</summary>

Fingerprint datapoints files collected by Apify and originally stored at
This package contains datafiles and helper functions for getting the path to the datafiles.

</details>

### runtype

Type dispatch and validation for run-time Python

`pip install runtype` · installs (wheel) · licence: MIT License · rank 2775 · last release 2025-03-03 · [PyPI](https://pypi.org/project/runtype/) · [source](https://github.com/erezsh/runtype)

<details><summary>README extract</summary>

Runtype is a collection of run-time type utilities for Python.

It is:

:runner: Fast! Uses an internal typesystem for maximum performance.

:brain: Smart! Supports `typing`, forward-references, constraints, auto-casting, and more.

:gear: Configurative! Write your own type system, and use it with *dataclass* and *dispatch*. ...

Example:
```python
from runtype import isa, issubclass

assert isa({'a': 1}, dict[str, int])        # == True
assert not isa({'a': 'b'}, dict[str, int])  # == False

assert issubclass(dict[str, int], typing.Mapping[str, int])     # == True
assert not issubclass(dict[str, int], typing.Mapping[int, str]) # == False
```

Sections: Modules, Docs, Examples, Validation (Isa & Subclass), Dataclasses, Multiple Dispatch, Benchmarks

</details>

### application-properties

A simple, easy to use, unified manner of accessing program properties.

`pip install application-properties` · installs (wheel) · licence: MIT License · rank 2777 · last release 2026-06-02 · [PyPI](https://pypi.org/project/application-properties/) · [docs](https://application_properties.readthedocs.io/)

<details><summary>README extract</summary>

| | |

|Project| |
|Quality| |
| | |
|Community| |
|Maintainers||

- I want a high-level overview.\
 Stay on this page to learn what `application_properties` is, why you might use it, what it
 can do, and whether it fits your projects. ...

Sections: Library Package: application_properties, Jumping Off Points, What Is `application_properties`?, Requirements, Getting Started

</details>

### aiodataloader

Asyncio DataLoader implementation for Python

`pip install aiodataloader` · installs (wheel) · licence: MIT License · rank 2783 · last release 2025-11-29 · [PyPI](https://pypi.org/project/aiodataloader/)

<details><summary>README extract</summary>

DataLoader is a generic utility to be used as part of your application's data
fetching layer to provide a simplified and consistent API over various remote
data sources such as databases or web services via batching and caching. ...

Example:
```python
from aiodataloader import DataLoader

class UserLoader(DataLoader):
    async def batch_load_fn(self, keys):
        return await my_batch_get_users(keys)

user_loader = UserLoader()
```

Sections: Asyncio DataLoader, Getting Started, Batching, Batch Function, Caching, Caching per-Request, Clearing Cache, Caching Exceptions, Disabling Cache, API, class DataLoader, `DataLoader(batch_load_fn, **options)`, `load(key)`, `load_many(keys)`

</details>

### pywinrm

Python library for Windows Remote Management

`pip install pywinrm` · installs (wheel) · licence: MIT License · rank 2789 · last release 2024-07-16 · [PyPI](https://pypi.org/project/pywinrm/)

<details><summary>README extract</summary>

pywinrm is a Python client for the Windows Remote Management (WinRM) service.
It allows you to invoke commands on target Windows machines from any machine
that can run Python.

WinRM allows you to perform various management tasks remotely. These include,
but are not limited to: running batch scripts, powershell scripts, and fetching
WMI variables. ...

Example:
```python
import winrm

s = winrm.Session('windows-host.example.com', auth=('john.smith', 'secret'))
r = s.run_cmd('ipconfig', ['/all'])
>>> r.status_code
0
>>> r.std_out
Windows IP Configuration

   Host Name . . . . . . . . . . . . : WINDOWS-HOST
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
...
```

...

</details>

### trame-vuetify

Vuetify widgets for trame

`pip install trame-vuetify` · installs (wheel) · licence: MIT License · rank 2790 · last release 2026-09-29 · [PyPI](https://pypi.org/project/trame-vuetify/)

<details><summary>README extract</summary>

Trame-vuetify extend trame widgets and ui with all the beautiful Vuetify UI components.
Vuetify is a UI Library with beautifully handcrafted Material Components. No design skills required — everything you need to create amazing applications is at your fingertips. ...

Example:
```python
from trame.widgets import vuetify

# <v-btn>Hello World</v-btn>
btn = vuetify.VBtn("Hello World")
```

Sections: trame-vuetify: Material Design widgets, Usage, Material Design Widgets, Boolean attributes, Dash and colon separators, Events, Enjoying trame?, JavaScript dependency

</details>

### pymarkdownlnt

A GitHub Flavored Markdown compliant Markdown linter.

`pip install pymarkdownlnt` · installs (wheel) · licence: MIT License · rank 2799 · last release 2026-10-13 · [PyPI](https://pypi.org/project/pymarkdownlnt/) · [docs](https://pymarkdown.readthedocs.io/)

<details><summary>README extract</summary>

<!-- pyml disable-num-lines 8 line-length-->
| | |

|Project| |
|Quality| |
| | |
|Community| |
|Maintainers||

- I want a high-level overview.\
 Stay on this page to learn what PyMarkdown is, why you might use it, what it
 can do, and whether it fits your projects. ...

Features:
Use PyMarkdown if:

- you already use spell or grammar checkers,
- you run static analysis before committing code, or
- you want project‑specific Markdown guidelines without much setup. ...

...

</details>

### dbus-fast

A faster version of dbus-next

`pip install dbus-fast` · installs (wheel) · licence: MIT License · rank 2810 · last release 2026-10-02 · [PyPI](https://pypi.org/project/dbus-fast/) · [docs](https://dbus-fast.readthedocs.io) · [source](https://github.com/bluetooth-devices/dbus-fast)

<details><summary>README extract</summary>

A faster version of dbus-next originally from the great DBus next library ❤️

Example:
```python
from dbus_fast.aio import MessageBus

import asyncio

async def main():
    bus = await MessageBus().connect()
    # the introspection xml would normally be included in your project, but
    # this is convenient for development
    introspection = await bus.introspect(
        "org.mpris.MediaPlayer2.vlc", "/org/mpris/MediaPlayer2"
    )

...
```

Sections: dbus-fast, The Client Interface, The Service Interface, The Low-Level Interface, Projects that use dbus-fast, Copyright

</details>

### tcmlib

Thread Composability Manager

`pip install tcmlib` · installs (wheel) · licence: Other/Proprietary License · rank 2835 · last release 2026-10-16 · [PyPI](https://pypi.org/project/tcmlib/)

<details><summary>README extract</summary>

Thread Composability Manager coordinates CPU resources usage between Intel® oneAPI Threading Building Blocks and Intel® OpenMP to avoid excessive oversubscription when both runtimes are used within a process.

</details>

### pysaml2

Python implementation of SAML Version 2 Standard

`pip install pysaml2` · installs (wheel) · licence: not stated · rank 2850 · last release 2026-09-17 · [PyPI](https://pypi.org/project/pysaml2/) · [docs](https://pysaml2.readthedocs.io) · [source](https://github.com/IdentityPython/pysaml2)

<details><summary>README extract</summary>

PySAML2 is a pure python implementation of SAML Version 2 Standard.
It contains all necessary pieces for building a SAML2 service provider
or an identity provider. The distribution contains examples of both.
Originally written to work in a WSGI environment
there are extensions that allow you to use it with other frameworks.

Website: ...

Sections: PySAML2 - SAML2 for Python, Specifications, SAML V2.0 Standard, Profiles and extensions, Committee Specifications, External dependencies, Releasing, Pre-commit

</details>

### mistletoe

A fast, extensible Markdown parser in pure Python.

`pip install mistletoe` · installs (wheel) · licence: MIT License · rank 2866 · last release 2026-07-11 · [PyPI](https://pypi.org/project/mistletoe/)

<details><summary>README extract</summary>

[][github-actions]
[][coveralls]
[][pypi]
[][pypi]

mistletoe is a Markdown parser in pure Python,
designed to be fast, spec-compliant and fully customizable.

Apart from being the fastest
CommonMark-compliant Markdown parser implementation in pure Python,
mistletoe also supports easy definitions of custom tokens. ...

Example:
```python
import mistletoe

with open('foo.md', 'r') as fin:
    rendered = mistletoe.markdown(fin)
```

Sections: mistletoe, Usage from Python, Usage from command-line, mistletoe interactive mode, Run mistletoe from CopyQ

</details>

### prefect-aws

Prefect integrations for interacting with Amazon Web Services.

`pip install prefect-aws` · installs (wheel) · licence: Apache Software License · rank 2872 · last release 2026-09-08 · [PyPI](https://pypi.org/project/prefect-aws/)

<details><summary>README extract</summary>

Build production-ready data workflows that seamlessly integrate with AWS services. `prefect-aws` provides battle-tested blocks, tasks, and infrastructure integrations for AWS, featuring support for ECS, S3, Secrets Manager, Lambda, Batch, and Glue.

Features:
While you could integrate with AWS services directly using boto3, `prefect-aws` offers significant advantages:

- Production-ready integrations: Pre-built, tested components that handle common AWS patterns and edge cases ...

Example:
```python
from prefect_aws import AwsCredentials

AwsCredentials(
    aws_access_key_id="PLACEHOLDER",
    aws_secret_access_key="PLACEHOLDER",
    aws_session_token=None,  # replace this with token if necessary
    region_name="us-east-2"
).save("BLOCK-NAME-PLACEHOLDER")
```

...

</details>

### dropbox

Official Dropbox API Client

`pip install dropbox` · installs (wheel) · licence: MIT · rank 2875 · last release 2026-10-22 · [PyPI](https://pypi.org/project/dropbox/) · [source](https://github.com/dropbox/dropbox-sdk-python)

<details><summary>README extract</summary>

Important: Use v12.0.2 or newer of this SDK for compatibility with the Dropbox API servers. Older versions stopped working in January 2026. Please refer to this blog post for more information:

The official Dropbox SDK for Python.

Documentation can be found on Read The Docs.

This SDK requires Python 3.11 or newer. ...

Example:
```python
import dropbox
from dropbox import files
from dropbox.file_transfer import (
    DownloadOptions,
    File,
    FileUpload,
    Uploader,
    UploadOptions,
    Downloader,
)

dbx = dropbox.Dropbox("YOUR_ACCESS_TOKEN")

Downloader(dbx).download(
    "/large-file.bin",
    File("large-file.bin"),
    DownloadOptions(parallel_downloads=4),
)

...
```

Sections: Requirements, Examples, Reliable File Transfers, Getting Help

</details>

### ibm-cloud-sdk-core

Core library used by SDKs for IBM Cloud Services

`pip install ibm-cloud-sdk-core` · installs (wheel) · licence: Apache Software License · rank 2877 · last release 2026-11-06 · [PyPI](https://pypi.org/project/ibm-cloud-sdk-core/) · [docs](https://github.com/IBM/python-sdk-core/blob/main/README.md) · [source](https://github.com/IBM/python-sdk-core)

<details><summary>README extract</summary>

This project contains core functionality required by Python code generated by the IBM Cloud OpenAPI SDK Generator
(openapi-sdkgen).

The current minimum Python version supported is 3.11.

Example:
```python
import logging

# Create a basic logging configuration that:
# 1. Defines a handler to display messages on the console.
# 2. Sets the root logger's logging level to DEBUG.
# 3. Sets the 'format' string used to display messages.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(name)s:%(levelname)s] %(message)s', force=True)
```

Sections: IBM Python SDK Core Version 3.28.2, Python Version, Authentication, Issues, Logging, Enable logging, Open source @ IBM

</details>

### objsize

Traversal over Python's objects subtree and calculate the total size of the subtree in bytes (deep size).

`pip install objsize` · installs (wheel) · licence: BSD License · rank 2884 · last release 2026-01-18 · [PyPI](https://pypi.org/project/objsize/)

<details><summary>README extract</summary>

The `objsize` Python package allows for the exploration and
measurement of an object’s complete memory usage in bytes, including its
child objects. This process, often referred to as deep size calculation,
is achieved through Python’s internal Garbage Collection (GC) mechanism. ...

Features:
* Traverse objects’ subtree
* Calculates the size of objects, including nested objects (deep size), in bytes
* Exclude non-exclusive objects
* Exclude specified objects subtree
* Provides flexibility by allowing users to define custom handlers for: ...

Example:
```python
>>> import objsize
>>> objsize.get_deep_size(dict(arg1='hello', arg2='world'))
340
```

...

</details>

### cucumber-tag-expressions

Provides a tag-expression parser and evaluation logic for cucumber/behave

`pip install cucumber-tag-expressions` · installs (wheel) · licence: MIT · rank 2893 · last release 2026-08-05 · [PyPI](https://pypi.org/project/cucumber-tag-expressions/) · [source](https://github.com/cucumber/tag-expressions)

<details><summary>README extract</summary>

Cucumber Tag Expressions

 Readable boolean expressions to select features and scenarios marked with tags in Gherkin

Example:
```python
>>> from cucumber_tag_expressions import parse

# Tagged with @fast
>>> fast = parse("@fast")
>>> fast({"@fast", "@wip"})
True
>>> fast({"@performance", "@slow"})
False

# Tagged with @wip and not @slow
>>> wip_not_slow = parse("@wip and not @slow")
>>> wip_not_slow({"@wip", "@home"})
True
>>> wip_not_slow({"wet", "warm", "raining"})
False

...
```

Sections: Getting Started, Test Runner Usage

</details>

### openai-codex

Python SDK for Codex

`pip install openai-codex` · installs (wheel) · licence: Apache-2.0 · rank 2895 · last release 2026-11-06 · [PyPI](https://pypi.org/project/openai-codex/) · [docs](https://github.com/openai/codex/tree/main/sdk/python/docs) · [source](https://github.com/openai/codex)

<details><summary>README extract</summary>

Build Python applications that start Codex threads, run turns, stream progress,
and control workspace access.

Example:
```python
from openai_codex import Codex

with Codex() as codex:
    thread = codex.thread_start()
    result = thread.run("Explain this repository in three bullets.")
    print(result.final_response)
```

Sections: OpenAI Codex Python SDK, Quickstart, Authentication, Built-In Help, Documentation

</details>

### application-file-scanner

A small package to deal with the headaches of scanning for files for an application to execute on.

`pip install application-file-scanner` · installs (wheel) · licence: MIT License · rank 2896 · last release 2026-01-19 · [PyPI](https://pypi.org/project/application-file-scanner/) · [docs](https://application_file_scanner.readthedocs.io/)

<details><summary>README extract</summary>

| | |

|Project| |
|Quality| |
| | |
|Community| |
|Maintainers||

NOTE: This project has just recently been updated, and we have plans to update this
documentation by 2026Mar30.

The `application_file_scanner` package was born out of necessity. ...

Sections: Library Package: application_file_scanner, Requirements, How To Use This Package, Examples, Issues and Future Plans, When Did Things Change?, Still Have Questions?

</details>

### line-profiler

Line-by-line profiler

`pip install line-profiler` · installs (wheel) · licence: BSD-3-Clause · rank 2938 · last release 2026-10-18 · [PyPI](https://pypi.org/project/line-profiler/)

<details><summary>README extract</summary>

This is the official `line_profiler` repository. The most recent version of
line-profiler on pypi points to
this repo.
The original line_profiler package
by @rkern is unmaintained.
This fork is the official continuation of the project. ...

Example:
```python
from line_profiler import profile

@profile
def slow_function():
    ...
```

Sections: line_profiler and kernprof, Quick Start, Older `kernprof` workflow, Documentation, Bugs and Such

</details>

### ultralytics-platform

Typed Python SDK for the Ultralytics Platform API

`pip install ultralytics-platform` · installs (wheel) · licence: AGPL-3.0-only · rank 2941 · last release 2026-11-07 · [PyPI](https://pypi.org/project/ultralytics-platform/) · [source](https://github.com/ultralytics/sdk)

_README extract left out: share-alike licence._

### pyshacl

Python SHACL Validator

`pip install pyshacl` · installs (wheel) · licence: Apache Software License · rank 2951 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pyshacl/) · [source](https://github.com/RDFLib/pySHACL)

<details><summary>README extract</summary>

A Python validator for SHACL.

This is a pure Python module which allows for the validation of RDF graphs against Shapes Constraint Language (SHACL) graphs. This module uses the rdflib Python library for working with RDF and is dependent on the OWL-RL Python module for OWL2 RL Profile based expansion of data graphs. ...

Features:
A features matrix is kept in the FEATURES file.

Example:
```python
from pyshacl import validate

data_graph = "some-data.ttl"
shacl_graph = "some-shacl.ttl"
ont_graph = "some-ontology.ttl"

r = validate(data_graph,
      shacl_graph=shacl_graph,
      ont_graph=ont_graph,
      inference='rdfs',
      abort_on_first=False,
      allow_infos=False,
      allow_warnings=False,
      meta_shacl=False,
...
```

...

</details>

### opencc-python-reimplemented

OpenCC made with Python

`pip install opencc-python-reimplemented` · installs (wheel) · licence: Apache Software License · rank 2957 · last release 2023-02-11 · [PyPI](https://pypi.org/project/opencc-python-reimplemented/)

<details><summary>README extract</summary>

﻿# 開放中文轉換（Pure Python）

Open Chinese convert (OpenCC) in pure Python.

opencc-python 是用純 Python 所寫，使用由 BYVoid(<byvoid.kcp@gmail.com>) 所開發的 OpenCC 中的字典檔案。

opencc-python 可以支援 Python2.7 及 Python3.x。

opencc-python is made by pure Python with the dictionary files of OpenCC which is developed by BYVoid(<byvoid.kcp@gmail.com>). ...

Example:
```python
from opencc import OpenCC

cc = OpenCC('s2t')  # convert from Simplified Chinese to Traditional Chinese

# can also set conversion by calling set_conversion

# cc.set_conversion('s2tw')

to_convert = '开放中文转换'

converted = cc.convert(to_convert)
```

Sections: Introduction 簡介, Usage 使用方式, Code, Command Line, Conversions 轉換, Issues 問題

</details>

### tcolorpy

tcolopy is a Python library to apply true color for terminal text.

`pip install tcolorpy` · installs (wheel) · licence: MIT License · rank 2972 · last release 2024-12-29 · [PyPI](https://pypi.org/project/tcolorpy/) · [source](https://github.com/thombashi/tcolorpy)

<details><summary>README extract</summary>

tcolopy is a Python library to apply true color for terminal text.

Sections: Summary, Usage, Library usage, Other examples, CLI usage, Command help, Dependencies

</details>

### chispa

Pyspark test helper library

`pip install chispa` · installs (wheel) · licence: MIT License · rank 2997 · last release 2026-03-24 · [PyPI](https://pypi.org/project/chispa/) · [docs](https://mrpowers.github.io/chispa) · [source](https://github.com/MrPowers/chispa)

<details><summary>README extract</summary>

*chispa* provides fast PySpark test helper methods that output descriptive error messages.

This library makes it easy to write high quality PySpark code.

Fun fact: "chispa" means Spark in Spanish ;)

Example:
```python
def remove_non_word_characters(col):
    return F.regexp_replace(col, "[^\\w\\s]+", "")
```

Sections: chispa, Column equality, DataFrame equality, Ignore row order, Ignore column order, Ignore specific columns, Ignore nullability, Allow NaN equality, Customize formatting, Approximate column equality, Approximate DataFrame equality, Schema mismatch messages, Benchmarks

</details>

### python-baseconv

Convert numbers from base 10 integers to base X strings and back again.

`pip install python-baseconv` · installs from source (sdist only) · licence: Python Software Foundation License · rank 3006 · last release 2019-04-04 · [PyPI](https://pypi.org/project/python-baseconv/)

<details><summary>README extract</summary>

Copyright (c) 2010, 2011, 2012, 2015, 2017 Guilherme Gondim.
All rights reserved.

Copyright (c) 2009 Simon Willison.
All rights reserved.

Copyright (c) 2002 Drew Perttula.
All rights reserved.

Description:
 Python module to convert numbers from base 10 integers to base X strings and back again. ...

Sections: baseconv, Django

</details>

### apify-shared

DEPRECATED - Tools and constants shared across Apify projects.

`pip install apify-shared` · installs (wheel) · licence: Apache-2.0 · rank 3008 · last release 2026-08-03 · [PyPI](https://pypi.org/project/apify-shared/) · [source](https://github.com/apify/apify-shared-python)

<details><summary>README extract</summary>

> ⚠️ DEPRECATED - this package is no longer maintained.
> The `apify-shared` package is not used by any Apify Python library anymore - its constants and utilities were moved
> into the packages that need them. ...

Sections: Apify Shared Python, What to use instead

</details>

### fcache

a dictionary-like, file-based cache module for Python

`pip install fcache` · installs (wheel) · licence: MIT License · rank 3016 · last release 2024-11-19 · [PyPI](https://pypi.org/project/fcache/) · [docs](https://tsroten.github.io/fcache) · [source](https://github.com/tsroten/fcache)

<details><summary>README extract</summary>

fcache is a dictionary-like, file-based cache module for Python. It's simple
to use, has an optional write buffer, and is
Shelf-compatible.

Example:
```python
>>> from fcache.cache import FileCache
>>> mycache = FileCache('myapp')
>>> mycache['foo'] = [1, 2, 3, 4, 5]
>>> mycache['foo']
[1, 2, 3, 4, 5]
>>> mycache['bar'] = 'value'
>>> list(mycache)
['foo', 'bar']
>>> del mycache['foo']
>>> mycache['foo']
    ...
    KeyError: 'foo'
```

Sections: fcache, Documentation, Bug/Issues Tracker

</details>

### pycognito

Python class to integrate Boto3's Cognito client so it is easy to login users. With SRP support.

`pip install pycognito` · installs (wheel) · licence: Apache License 2.0 · rank 3024 · last release 2024-05-16 · [PyPI](https://pypi.org/project/pycognito/)

<details><summary>README extract</summary>

Makes working with AWS Cognito easier for Python developers.

Example:
```python
from pycognito import Cognito

u = Cognito('your-user-pool-id','your-client-id',
    client_secret='optional-client-secret'
    username='optional-username',
    id_token='optional-id-token',
    refresh_token='optional-refresh-token',
    access_token='optional-access-token',
    access_key='optional-access-key',
...
```

Sections: pyCognito, Getting Started, Environment Variables, COGNITO_JWKS, Cognito Utility Class, Example with All Arguments, Arguments, Examples with Realistic Arguments, User Pool Id and Client ID Only, Username, Tokens, Cognito Attributes, Cognito Methods, Register

</details>

### pierre-storage

Pierre Git Storage SDK for Python

`pip install pierre-storage` · installs (wheel) · licence: MIT · rank 3027 · last release 2026-09-17 · [PyPI](https://pypi.org/project/pierre-storage/) · [docs](https://docs.pierre.io) · [source](https://github.com/pierrecomputer/pierre)

<details><summary>README extract</summary>

Pierre Git Storage SDK for Python applications.

Example:
```python
from pierre_storage import GitStorage

# Initialize the client with your name and key
storage = GitStorage({
    "name": "your-name",  # e.g., 'v0'
    "key": "your-key",  # Your API key in PEM format
})
```

Sections: pierre-storage, Usage, Basic Setup, Creating a Repository, Finding a Repository, Hydrating a Repository Without a Request, Grep, Getting Remote URLs, Working with Repository Content, Creating Commits, Creating Commits from Diff Streams, Ephemeral Branches, Streaming Large Files, GitHub Repository Sync

</details>

