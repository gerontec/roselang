# Software Development / Build Tools

[Index](README.md) · 227 packages in this topic, 53 more listed under another topic, by downloads.

### pip

The PyPA recommended tool for installing Python packages.

`pip install pip` · installs (wheel) · licence: MIT · rank 62 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pip/) · [docs](https://pip.pypa.io) · [source](https://github.com/pypa/pip)

### hatchling

Modern, extensible Python build backend

`pip install hatchling` · installs (wheel) · licence: MIT · rank 89 · last release 2026-10-28 · [PyPI](https://pypi.org/project/hatchling/) · [source](https://github.com/pypa/hatch/tree/master/backend)

<details><summary>README extract</summary>

| | |

| Package | |
| Meta | |

This is the extensible, standards compliant build backend used by Hatch.

Sections: Hatchling, Usage, Documentation

</details>

### poetry-core

Poetry PEP 517 Build Backend

`pip install poetry-core` · installs (wheel) · licence: MIT · rank 311 · last release 2026-09-19 · [PyPI](https://pypi.org/project/poetry-core/) · [source](https://github.com/python-poetry/poetry-core)

<details><summary>README extract</summary>

A PEP 517 build backend implementation developed for
Poetry. This project is intended to be a lightweight, fully compliant,
self-contained package allowing PEP 517-compatible build frontends to build Poetry-managed projects.

Features:
Prior to the release of version `1.1.0`, Poetry was a project management tool that included a PEP 517
build backend. This was inefficient and time consuming when a PEP 517 build was required. ...

Sections: Poetry Core, Usage, Why is this required?

</details>

### triton

A language and compiler for custom Deep Learning operations

`pip install triton` · installs (wheel) · licence: MIT · rank 473 · last release 2026-10-27 · [PyPI](https://pypi.org/project/triton/)

### poetry

Python dependency management and packaging made easy.

`pip install poetry` · installs (wheel) · licence: MIT · rank 500 · last release 2026-09-20 · [PyPI](https://pypi.org/project/poetry/) · [docs](https://python-poetry.org/docs) · [source](https://github.com/python-poetry/poetry)

<details><summary>README extract</summary>

[][PyPI Releases]
[][PyPI Releases]
[][PyPI]

[][Discord]

Poetry helps you declare, manage and install dependencies of Python projects,
ensuring you have the right stack everywhere.

Poetry replaces `setup.py`, `requirements.txt`, `setup.cfg`, `MANIFEST.in` and `Pipfile` with a simple `pyproject.toml`
based project format.

Sections: Documentation, Resources, Related Projects

</details>

### ninja

Ninja is a small build system with a focus on speed

`pip install ninja` · installs (wheel) · licence: Apache-2.0 · rank 682 · last release 2026-08-30 · [PyPI](https://pypi.org/project/ninja/) · [docs](https://github.com/scikit-build/ninja-python-distributions#readme) · [source](https://github.com/scikit-build/ninja-python-distributions)

<details><summary>README extract</summary>

Ninja is a small build system with a focus on speed.

The latest Ninja python wheels provide ninja 1.13.2.g7659b.kitware.jobserver-pipe-1 executable
and `ninja_syntax.py` for generating `.ninja` files. ...

Example:
```python
import ninja
writer = ninja.Writer(sys.stdout)
```

Sections: Ninja Python Distributions, Miscellaneous

</details>

### firebase-admin

Firebase Admin Python SDK

`pip install firebase-admin` · installs (wheel) · licence: Apache Software License · rank 909 · last release 2026-09-23 · [PyPI](https://pypi.org/project/firebase-admin/) · [source](https://github.com/firebase/firebase-admin-python)

<details><summary>README extract</summary>

The Firebase Admin Python SDK enables server-side (backend) Python developers to integrate Firebase into their services and applications.

</details>

### maturin

Build and publish crates with pyo3, cffi and uniffi bindings as well as rust binaries as python packages

`pip install maturin` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 928 · last release 2026-10-29 · [PyPI](https://pypi.org/project/maturin/) · [docs](https://maturin.rs) · [source](https://github.com/PyO3/maturin)

<details><summary>README extract</summary>

_formerly pyo3-pack

Build and publish crates with pyo3, cffi and uniffi bindings as well as rust binaries as python packages with minimal configuration.
It supports building wheels for python 3.8+ on Windows, Linux, macOS and FreeBSD, can upload them to pypi and has basic PyPy and GraalPy support.

Check out the User Guide!

Sections: Maturin, Usage, Python packaging basics, Mixed rust/python projects, Python metadata, Source distribution, Manylinux and auditwheel, Examples

</details>

### cmake

CMake is an open-source, cross-platform family of tools designed to build, test and package software

`pip install cmake` · installs (wheel) · licence: Apache Software License; BSD License · rank 957 · last release 2026-10-04 · [PyPI](https://pypi.org/project/cmake/) · [docs](https://cmake-python-distributions.readthedocs.io) · [source](https://github.com/scikit-build/cmake-python-distributions)

<details><summary>README extract</summary>

CMake is used to control the software compilation
process using simple platform and compiler independent configuration files,
and generate native makefiles and workspaces that can be used in the
compiler environment of your choice. ...

Sections: CMake Python Distributions, Platforms, Miscellaneous

</details>

### sshtunnel

Pure python SSH tunnels

`pip install sshtunnel` · installs (wheel) · licence: MIT License · rank 1007 · last release 2026-10-09 · [PyPI](https://pypi.org/project/sshtunnel/)

<details><summary>README extract</summary>

Author: Pahaz

Repo:

Inspired by which doesn't work on
Windows.

See also:

* paramiko

Example:
```python
from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    'alfa.8iq.dev',
    ssh_username="pahaz",
    ssh_password="secret",
    remote_bind_address=('127.0.0.1', 8080)
)

server.start()

print(server.local_bind_port)  # show assigned local port
# work with `SECRET SERVICE` through `server.local_bind_port`.

server.stop()
```

Sections: Requirements, Usage scenarios, Usage examples, Example 1, Example 2, Example 3, Example 4, CLI usage, Online documentation

</details>

### meson

A high performance build system

`pip install meson` · installs (wheel) · licence: Apache Software License · rank 1128 · last release 2026-09-22 · [PyPI](https://pypi.org/project/meson/) · [source](https://github.com/mesonbuild/meson)

<details><summary>README extract</summary>

Meson is a cross-platform build system designed to be both as fast and as user friendly as possible. It supports many languages and compilers, including GCC, Clang, PGI, Intel, and Visual Studio. Its build definitions are written in a simple non-Turing complete DSL.

</details>

### patchelf

A small utility to modify the dynamic linker and RPATH of ELF executables.

`pip install patchelf` · installs (wheel) · licence: Apache Software License; GNU General Public License v3 or later (GPLv3+) · rank 1164 · last release 2026-11-03 · [PyPI](https://pypi.org/project/patchelf/) · [source](https://github.com/mayeut/patchelf-pypi)

_README extract left out: share-alike licence._

### pyinstaller-hooks-contrib

Community maintained hooks for PyInstaller

`pip install pyinstaller-hooks-contrib` · installs (wheel) · licence: Apache Software License; GNU General Public License v2 (GPLv2) · rank 1226 · last release 2026-10-20 · [PyPI](https://pypi.org/project/pyinstaller-hooks-contrib/)

_README extract left out: share-alike licence._

### junit-xml

Creates JUnit XML test result documents that can be read by tools such as Jenkins

`pip install junit-xml` · installs (wheel) · licence: Freely Distributable; MIT License · rank 1241 · last release 2023-01-24 · [PyPI](https://pypi.org/project/junit-xml/)

<details><summary>README extract</summary>

A Python module for creating JUnit XML test result documents that can be
read by tools such as Jenkins or Bamboo. If you are ever working with test tool or
test suite written in Python and want to take advantage of Jenkins' or Bamboo's
pretty graphs and test reporting capabilities, this module will let you
generate the XML test reports. ...

Example:
```python
from junit_xml import TestSuite, TestCase

test_cases = [TestCase('Test1', 'some.class.name', 123.345, 'I am stdout!', 'I am stderr!')]
ts = TestSuite("my test suite", test_cases)
# pretty printing is on by default but can be disabled using prettyprint=False
print(TestSuite.to_xml_string([ts]))
```

Sections: python-junit-xml, About, Using, Running the tests

</details>

### meson-python

The Python build backend for Meson projects

`pip install meson-python` · installs (wheel) · licence: MIT · rank 1278 · last release 2026-10-01 · [PyPI](https://pypi.org/project/meson-python/) · [docs](https://mesonbuild.com/meson-python/) · [source](https://github.com/mesonbuild/meson-python)

<details><summary>README extract</summary>

`meson-python` is a Python build back-end built on top of the Meson_
build system. It enables using Meson for the configuration and build
steps of Python packages. Meson is an open source build system meant
to be both extremely fast, and, even more importantly, as user
friendly as possible. ...

</details>

### dbt-core-experimental-parser

Build analytics the way engineers build applications

`pip install dbt-core-experimental-parser` · installs from source (sdist only) · licence: Apache-2.0 · rank 1457 · last release 2026-11-03 · [PyPI](https://pypi.org/project/dbt-core-experimental-parser/) · [docs](https://docs.getdbt.com) · [source](https://github.com/dbt-labs/dbt-core)

<details><summary>README extract</summary>

> [!WARNING]
> dbt v1 development has moved to the `1.latest` branch.
> The `main` branch now contains all the Apache 2.0 source code of dbt v2.0 — a ground-up rewrite of dbt in Rust. If you're looking for the v1 Python implementation of the dbt framework, switch to `1.latest`. ...

Sections: About dbt v2.0, Understanding dbt, Getting started

</details>

### poethepoet

A task runner that works well with poetry and uv.

`pip install poethepoet` · installs (wheel) · licence: MIT · rank 1500 · last release 2026-10-15 · [PyPI](https://pypi.org/project/poethepoet/) · [docs](https://poethepoet.natn.io/) · [source](https://github.com/nat-n/poethepoet)

<details><summary>README extract</summary>

A batteries included task runner that works well with poetry or uv.

📖 Read the documentation 📖

Features:
- ✅ Straight forward declaration of project tasks in your pyproject.toml (or poe_tasks.toml)

- ✅ Tasks are run in poetry or uv's virtualenv (or another env you specify)

- ✅ Shell completion of task names and arguments ...

Sections: Poe the Poet, Features, Quick start

</details>

### kaitaistruct

Kaitai Struct declarative parser generator for binary data: runtime library for Python

`pip install kaitaistruct` · installs (wheel) · licence: MIT · rank 1542 · last release 2025-09-08 · [PyPI](https://pypi.org/project/kaitaistruct/) · [docs](https://doc.kaitai.io/) · [source](https://github.com/kaitai-io/kaitai_struct_python_runtime)

<details><summary>README extract</summary>

This library implements Kaitai Struct API for Python.

Kaitai Struct is a declarative language used for
describe various binary data structures, laid out in files or in memory:
i.e. binary file formats, network stream packet formats, etc.

It is similar to Python's Construct 2.10
but it is language-agnostic. ...

</details>

### sh

Python subprocess replacement

`pip install sh` · installs (wheel) · licence: MIT License · rank 1565 · last release 2026-07-25 · [PyPI](https://pypi.org/project/sh/) · [docs](https://sh.readthedocs.io/) · [source](https://github.com/amoffat/sh)

<details><summary>README extract</summary>

sh is a full-fledged subprocess replacement for Python 3.10 - 3.14, and PyPy
that allows you to call *any* program as if it were a function:

sh is *not* a collection of system commands implemented in Python.

sh relies on various Unix system calls and only works on Unix-like operating
systems - Linux, macOS, BSDs etc. ...

Example:
```python
from sh import git
print(git("status", "--short"))
```

Sections: Docs, Coverage

</details>

### plumbum

Plumbum: shell combinators library

`pip install plumbum` · installs (wheel) · licence: MIT · rank 1637 · last release 2026-07-22 · [PyPI](https://pypi.org/project/plumbum/) · [docs](https://plumbum.readthedocs.io/)

<details><summary>README extract</summary>

Ever wished the compactness of shell scripts be put into a real programming language?
Say hello to *Plumbum Shell Combinators*. Plumbum (Latin for *lead*, which was used to create
pipes back in the day) is a small yet feature-rich library for shell script-like programs in Python. ...

Example:
```python
>>> from plumbum import local
>>> local.cmd.ls
LocalCommand(/bin/ls)
>>> local.cmd.ls()
'build.py\nCHANGELOG.rst\nCONTRIBUTING.rst\ndocs\nexamples\nexperiments\nLICENSE\nMANIFEST.in\nPipfile\nplumbum\nplumbum.egg-info\npytest.ini\nREADME.rst\nsetup.cfg\nsetup.py\ntests\ntranslations.py\n'
>>> notepad = local["c:\\windows\\notepad.exe"]
...
```

...

</details>

### construct

A powerful declarative symmetric parser/builder for binary data

`pip install construct` · installs (wheel) · licence: MIT License · rank 1680 · last release 2023-11-29 · [PyPI](https://pypi.org/project/construct/) · [docs](https://construct.readthedocs.io/en/latest/) · [source](https://github.com/construct/construct)

<details><summary>README extract</summary>

Construct is a powerful declarative and symmetrical parser and builder for binary data.

Instead of writing *imperative code* to parse a piece of data, you declaratively define a *data structure* that describes your data. ...

Example:
```python
>>> format = Struct(
...     "signature" / Const(b"BMP"),
...     "width" / Int8ub,
...     "height" / Int8ub,
...     "pixels" / Array(this.width * this.height, Byte),
... )
>>> format.build(dict(width=3,height=2,pixels=[7,8,9,11,12,13]))
b'BMP\x03\x02\x07\x08\t\x0b\x0c\r'
>>> format.parse(b'BMP\x03\x02\x07\x08\t\x0b\x0c\r')
...
```

Sections: Construct 2.10, Example

</details>

### pex

The PEX packaging toolchain.

`pip install pex` · installs (wheel) · licence: Apache-2.0 · rank 1847 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pex/) · [docs](https://docs.pex-tool.org/) · [source](https://github.com/pex-tool/pex/tree/v2.107.1)

<details><summary>README extract</summary>

Features:
pex is a library for generating .pex (Python EXecutable) files which are
executable Python environments in the spirit of virtualenvs. ...

Sections: PEX, Overview, Simple Examples, Save Dependencies From Pip, Ephemeral Environments, Using Entry Points, Specifying A Specific Interpreter, Documentation

</details>

### hatch

Modern, extensible Python project management

`pip install hatch` · installs (wheel) · licence: MIT · rank 1856 · last release 2026-10-28 · [PyPI](https://pypi.org/project/hatch/) · [source](https://github.com/pypa/hatch)

<details><summary>README extract</summary>

| | |

| CI/CD | |
| Docs | |
| Package | |
| Meta | |

Hatch is a modern, extensible Python project manager.

Features:
- Standardized build system with reproducible builds by default
- Robust environment management with support for custom scripts and UV
- Configurable Python distribution management
- Test execution with known best practices ...

Sections: Hatch, Features, Documentation

</details>

### patch-ng

Library to parse and apply unified diffs.

`pip install patch-ng` · installs (wheel) · licence: MIT License · rank 1932 · last release 2026-04-23 · [PyPI](https://pypi.org/project/patch-ng/)

<details><summary>README extract</summary>

Features:
This project is a fork from the original python-patch project.

As any other project, bugs are common during the development process, the combination of issues + pull requests are
able to keep the constant improvement of a project. ...

Sections: Patch NG (New Generation), Library to parse and apply unified diffs., Why did we fork this project?, Features, Usage, Other stuff

</details>

### blockbuster

Utility to detect blocking calls in the async event loop

`pip install blockbuster` · installs (wheel) · licence: Apache Software License · rank 1967 · last release 2026-10-09 · [PyPI](https://pypi.org/project/blockbuster/) · [source](https://github.com/cbornet/blockbuster.git)

<details><summary>README extract</summary>

Blockbuster is a Python package designed to detect and prevent blocking calls within an asynchronous event loop.
It is particularly useful when executing tests to ensure that your asynchronous code does not inadvertently call blocking operations,
which can lead to performance bottlenecks and unpredictable behavior. ...

Example:
```python
import pytest
import time
from blockbuster import BlockBuster, BlockingError, blockbuster_ctx
from typing import Iterator

@pytest.fixture(autouse=True)
def blockbuster() -> Iterator[BlockBuster]:
    with blockbuster_ctx() as bb:
        yield bb

async def test_time_sleep() -> None:
    with pytest.raises(BlockingError, match="sleep"):
...
```

...

</details>

### pkgconfig

Interface Python with pkg-config

`pip install pkgconfig` · installs (wheel) · licence: MIT License · rank 2013 · last release 2026-03-06 · [PyPI](https://pypi.org/project/pkgconfig/)

<details><summary>README extract</summary>

`pkgconfig` is a Python module to interface with the `pkg-config`
command-line tool for Python 3.9+.

The `pkg-config` command-line tool typically comes from a package either
called `pkg-config` (the original implementation) or `pkgconf` (a more
recent, improved reimplementation intended as a drop-in replacement). ...

Example:
```python
>>> packages = pkgconfig.list_all()
```

Sections: pkgconfig, Version 1.6.0, Version 1.5.5, Version 1.5.4, Version 1.5.3, Version 1.5.2, Version 1.5.0, Version 1.4.0, Version 1.3.1, Version 1.3.0, Version 1.2.1 and 1.2.2, Version 1.2.0, Version 1.1.0, Version 1.0.0

</details>

### hatch-fancy-pypi-readme

Fancy PyPI READMEs with Hatch

`pip install hatch-fancy-pypi-readme` · installs (wheel) · licence: MIT · rank 2048 · last release 2025-05-01 · [PyPI](https://pypi.org/project/hatch-fancy-pypi-readme/) · [docs](https://github.com/hynek/hatch-fancy-pypi-readme#readme) · [source](https://github.com/hynek/hatch-fancy-pypi-readme)

<details><summary>README extract</summary>

*hatch-fancy-pypi-readme* is an MIT-licensed metadata plugin for Hatch by Hynek Schlawack.

Its purpose is to help you to have fancy PyPI readmes – unlike *this* one you’re looking at right now.

Please check out the documentation to see what *hatch-fancy-pypi-readme* can do for you and your projects!

</details>

### pdm-backend

The build backend used by PDM that supports latest packaging standards

`pip install pdm-backend` · installs (wheel) · licence: MIT · rank 2192 · last release 2026-09-30 · [PyPI](https://pypi.org/project/pdm-backend/) · [docs](https://backend.pdm-project.org) · [source](https://github.com/pdm-project/pdm-backend)

<details><summary>README extract</summary>

The build backend used by [PDM] that supports latest packaging standards.

This is the backend for [PDM] projects that is fully-compatible with [PEP 517] spec, but you can also use it alone.
It reads the metadata of [PEP 621] format and coverts it to [Core metadata].

- Documentation
- Changelog
- PDM Documentation
- PyPI
- Discord ...

Sections: PDM-Backend, Links

</details>

### conan

Conan C/C++ package manager

`pip install conan` · installs (wheel) · licence: MIT License · rank 2203 · last release 2026-10-28 · [PyPI](https://pypi.org/project/conan/) · [docs](https://docs.conan.io) · [source](https://github.com/conan-io/conan)

<details><summary>README extract</summary>

Decentralized, open-source (MIT), C/C++ package manager.

Conan is a package manager for C and C++ developers:

- It is fully decentralized. Users can host their packages on their servers, privately. Integrates with Artifactory and Bintray.
- Portable. ...

Sections: Conan, Setup, Running the tests

</details>

### html-for-docx

Convert HTML to DOCX easily and quickly

`pip install html-for-docx` · installs (wheel) · licence: MIT · rank 2514 · last release 2026-10-19 · [PyPI](https://pypi.org/project/html-for-docx/) · [source](https://github.com/dfop02/html4docx)

<details><summary>README extract</summary>

Convert html to docx, this project is a fork from descontinued pqzx/html2docx.

Features:
My goal in forking and fixing/updating this package was to complete my current task at work, which involves converting HTML to DOCX. The original package lacked a few features and had some bugs, preventing me from completing the task. ...

Example:
```python
from html4docx import HtmlToDocx

parser = HtmlToDocx()
html_string = '
# Hello world
'
parser.add_html_to_document(html_string, filename_docx)
```

Sections: HTML FOR DOCX, Usage, The basic usage, Convert files directly, Convert files from a string, Change table styles, Options, Extended Styling Features, CSS Class to Word Style Mapping, Tag Style Overrides, Default Paragraph Style, CSS, Inline CSS Styles, External CSS Styles

</details>

### tokenspeed-triton

A language and compiler for custom Deep Learning operations (vendor release for TokenSpeed)

`pip install tokenspeed-triton` · installs (wheel) · licence: MIT · rank 2751 · last release 2026-10-28 · [PyPI](https://pypi.org/project/tokenspeed-triton/)

### rust-just

(no summary)

`pip install rust-just` · installs (wheel) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication · rank 2932 · last release 2026-10-16 · [PyPI](https://pypi.org/project/rust-just/) · [docs](https://just.systems/man/en) · [source](https://github.com/gnpaone/rust-just)

<details><summary>README extract</summary>

Table of Contents↗️

`just` is a handy way to save and run project-specific commands.

This readme is also available as a book. The
book reflects the latest release, whereas the
readme on GitHub
reflects latest master.

(中文文档在 这里,
快看过来!)

Commands, called recipes, are stored in a file called `justfile` with syntax
inspired by `make`: ...

Example:
```python
# Built-in Functions

`just` provides many built-in functions for use in expressions, including
recipe body `{{…}}` substitutions, assignments, and default parameter values.

All functions ending in `_directory` can be abbreviated to `_dir`. So
`home_directory()` can also be written as `home_dir()`. In addition,
...
```

...

</details>

### taskipy

tasks runner for python projects

`pip install taskipy` · installs (wheel) · licence: MIT License · rank 3186 · last release 2024-11-26 · [PyPI](https://pypi.org/project/taskipy/) · [source](https://github.com/taskipy/taskipy)

<details><summary>README extract</summary>

- General
- Requirements
- Usage
 - Installation
 - Adding Tasks
 - Running Tasks
 - Passing Command Line Args to Tasks
 - Composing Tasks
 - Grouping Subtasks Together
 - Pre Task Hook
 - Post Task Hook
 - Using Variables
 - String Formatting
 - Always Use Variables
 - Recursive Variables
 - Working directory
 - Using Taskipy Without Poetry
 - ...

Sections: General, Requirements, Usage, Adding Tasks, Running Tasks, Passing Command Line Args to Tasks, Composing Tasks, Grouping Subtasks Together, Pre Task Hook, Post Task Hook, Using Variables, String Formatting, Always Use Variables, Recursive Variables

</details>

### uipath

Python SDK and CLI for UiPath Platform, enabling programmatic interaction with automation services, process management, and deployment tools.

`pip install uipath` · installs (wheel) · licence: not stated · rank 3206 · last release 2026-11-06 · [PyPI](https://pypi.org/project/uipath/) · [docs](https://uipath.github.io/uipath-python/) · [source](https://github.com/UiPath/uipath-python)

<details><summary>README extract</summary>

A Python SDK that enables programmatic interaction with UiPath Cloud Platform services including processes, assets, buckets, context grounding, data services, jobs, and more. The package also features a CLI for creation, packaging, and deployment of automations to UiPath Cloud Platform. ...

Example:
```python
from uipath.platform import UiPath
# Initialize the SDK
sdk = UiPath()
# Execute a process
job = sdk.processes.invoke(
    name="MyProcess",
    input_arguments={"param1": "value1", "param2": 42}
)
# Work with assets
asset = sdk.assets.retrieve(name="MyAsset")
```

...

</details>

### ziglang

Zig is a general-purpose programming language and toolchain for maintaining robust, optimal, and reusable software.

`pip install ziglang` · installs (wheel) · licence: MIT · rank 3241 · last release 2026-11-05 · [PyPI](https://pypi.org/project/ziglang/) · [source](https://codeberg.org/ziglang/zig-pypi)

<details><summary>README extract</summary>

Zig is a general-purpose programming language and toolchain for maintaining robust, optimal, and reusable software. The ziglang Python package redistributes the Zig toolchain so that it can be used as a dependency of Python projects.

Rationale ...

Example:
```python
import sys, subprocess

subprocess.call([sys.executable, "-m", "ziglang"])
```

</details>

### macholib

Mach-O header analysis and editing

`pip install macholib` · installs (wheel) · licence: MIT License · rank 3269 · last release 2025-11-22 · [PyPI](https://pypi.org/project/macholib/) · [docs](https://macholib.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/macholib)

<details><summary>README extract</summary>

macholib can be used to analyze and edit Mach-O headers, the executable
format used by Mac OS X.

It's typically used as a dependency analysis tool, and also to rewrite dylib
references in Mach-O headers to be @executable_path relative. ...

Sections: Project links, macholib 1.16.4, macholib 1.16.3, macholib 1.16.2, macholib 1.16.1, macholib 1.16, macholib 1.15.2, macholib 1.15.1, macholib 1.15, macholib 1.14, macholib 1.13, 31: Add two new load commands introduced in macOS 10.15, macholib 1.12, macholib 1.11

</details>

### versioningit

Versioning It with your Version In Git

`pip install versioningit` · installs (wheel) · licence: MIT · rank 3487 · last release 2025-06-27 · [PyPI](https://pypi.org/project/versioningit/) · [docs](https://versioningit.readthedocs.io) · [source](https://github.com/jwodder/versioningit)

<details><summary>README extract</summary>

GitHub
| PyPI
| Documentation
| Issues
| Changelog

`versioningit` — *Versioning It with your Version In Git*

`versioningit` is yet another Python packaging plugin for automatically
determining your package's version based on your version control repository's
tags. ...

</details>

### pdm

A modern Python package and dependency manager supporting the latest PEP standards

`pip install pdm` · installs (wheel) · licence: MIT · rank 3550 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pdm/) · [docs](https://pdm-project.org) · [source](https://github.com/pdm-project/pdm)

<details><summary>README extract</summary>

A modern Python package and dependency manager supporting the latest PEP standards.
中文版本说明

PDM is meant to be a next-generation package manager.
It was originally built for personal use. If you feel you are going well
with `Pipenv` or `Poetry` and don't want to introduce another package manager,
just stick to it. ...

Features:
- Simple and fast dependency resolver, mainly for large binary distributions.
- A [PEP 517] build backend.
- [PEP 621] project metadata.
- Flexible and powerful plug-in system.
- Versatile user scripts. ...

Sections: PDM, What is PDM?, Highlights of features, Comparisons to other alternatives, Pipenv, Poetry, Hatch, This project, Quickstart, PDM Eco-system, Experimental

</details>

### uipath-langchain

Python SDK that enables developers to build and deploy LangGraph agents to the UiPath Cloud Platform

`pip install uipath-langchain` · installs (wheel) · licence: not stated · rank 3652 · last release 2026-11-06 · [PyPI](https://pypi.org/project/uipath-langchain/) · [docs](https://uipath.github.io/uipath-python/) · [source](https://github.com/UiPath/uipath-langchain-python)

<details><summary>README extract</summary>

A Python SDK that enables developers to build and deploy LangGraph agents to the UiPath Cloud Platform. It provides programmatic interaction with UiPath Cloud Platform services and human-in-the-loop (HITL) semantics through Action Center integration.

This package is an extension to the UiPath Python SDK and implements the UiPath Runtime Protocol. ...

Sections: UiPath LangChain Python SDK, Requirements, Configuration, Environment Variables, Command Line Interface (CLI), Initialize a Project, Authentication, Debug a Project, Package a Project, Publish a Package, Project Structure, Special Thanks

</details>

### construct-typing

Extension for the python package 'construct' that adds typing features

`pip install construct-typing` · installs (wheel) · licence: MIT · rank 3671 · last release 2026-07-23 · [PyPI](https://pypi.org/project/construct-typing/)

<details><summary>README extract</summary>

This project is an extension of the python package *construct*, which is a powerful declarative and symmetrical parser and builder for binary data. This Repository consists of two packages:

- construct-stubs: Adding .pyi for the whole *construct 2.10* package (according to PEP 561 stub-only packages) ...

Example:
```python
import dataclasses
import typing as t
from construct import Array, Byte, Bytes, Int8ub, this
from construct_typed import DataclassMixin, DataclassStruct, EnumBase, TEnum, csfield, csfield_const

class Orientation(EnumBase):
    HORIZONTAL = 0
    VERTICAL = 1

@dataclasses.dataclass
class Image(DataclassMixin):
...
```

...

</details>

### liccheck

Check python packages from requirement.txt and report issues

`pip install liccheck` · installs (wheel) · licence: Apache Software License · rank 3731 · last release 2023-09-22 · [PyPI](https://pypi.org/project/liccheck/)

<details><summary>README extract</summary>

Sections: About, Assumption, How to use, Using liccheck with pre-commit, Licensing

</details>

### csscompressor

A python port of YUI CSS Compressor

`pip install csscompressor` · installs from source (sdist only) · licence: BSD License · rank 3775 · last release 2017-11-26 · [PyPI](https://pypi.org/project/csscompressor/)

<details><summary>README extract</summary>

Almost exact port of YUI CSS Compressor.
Passes all original unittests.

Example:
```python
>>> from csscompressor import compress
>>> compress('''
...    your css {
...        content: "!";
...    }
... ''')
'your css{content:"!"}'
```

Sections: Usage, Compatibility

</details>

### cmeel

Create Wheel from CMake projects

`pip install cmeel` · installs (wheel) · licence: BSD-2-Clause · rank 3866 · last release 2026-11-01 · [PyPI](https://pypi.org/project/cmeel/) · [docs](https://cmeel.readthedocs.io/)

<details><summary>README extract</summary>

Wheel build backend using CMake, to package any CMake project with pip and distribute on PyPI.

Following those relevant PEPs:
- PEP 427, The Wheel Binary Package Format 1.0
- PEP 517, A build-system independent format for source trees
- PEP 518, Specifying Minimum Build System Requirements for Python Projects ...

Sections: CMake Wheel: cmeel, Chat, Basic idea, Basic pyproject.toml example

</details>

### bump-my-version

Version bump your Python project

`pip install bump-my-version` · installs (wheel) · licence: MIT License · rank 4021 · last release 2026-11-01 · [PyPI](https://pypi.org/project/bump-my-version/) · [docs](https://callowayproject.github.io/bump-my-version/) · [source](https://github.com/callowayproject/bump-my-version.git)

<details><summary>README extract</summary>

> NOTE
> This is a maintained refactor of the bump2version fork of the excellent bumpversion project. The main goals of this refactor were:
> - Add support for `pyproject.toml` configuration files. ...

Features:
Bump My Version's purpose is to:

- Work as a part of an automated build system
- Manage project versioning through the project's development life cycle
 - Incrementing and serializing version numbers
 - parsing version numbers
 - supporting SemVer, ...

Sections: Bump My Version, Overview, Semantic versioning example, Create a default configuration, Visualize the versioning path, Get the new version in a script, Visualize the new versioning path, Visualize the pre_n versioning path, GitHub Actions

</details>

### calver

Setuptools extension for CalVer package versions

`pip install calver` · installs (wheel) · licence: Apache-2.0 · rank 4105 · last release 2025-10-20 · [PyPI](https://pypi.org/project/calver/) · [source](https://github.com/di/calver)

<details><summary>README extract</summary>

The `calver` package is a setuptools extension
for automatically defining your Python package version as a calendar version.

Example:
```python
from setuptools import setup

setup(
    ...
    use_calver=True,
    setup_requires=['calver'],
    ...
)
```

Sections: CalVer, Usage, Configuration

</details>

### kconfiglib

A flexible Python Kconfig implementation

`pip install kconfiglib` · installs (wheel) · licence: ISC License (ISCL) · rank 4177 · last release 2020-01-31 · [PyPI](https://pypi.org/project/kconfiglib/)

<details><summary>README extract</summary>

To fix issues with dependency loops on recent linux-next kernels, apply this
patch. Hopefully,
it will be in `linux-next` soon.

Features:
Kconfiglib is a Kconfig
implementation in Python 2/3. It started out as a helper library, but now has a
enough functionality to also work well as a standalone Kconfig implementation
(including terminal and GUI menuconfig interfaces
and Kconfig ...

Example:
```python
$ make iscriptconfig
A Kconfig instance 'kconf' for the architecture x86 has been created.
>>> kconf  # Calls Kconfig.repr()
<configuration with 13711 symbols, main menu prompt "Linux/x86 4.14.0-rc7 Kernel Configuration", srctree ".", config symbol prefix "CONFIG", warnings enabled, undef. symbol assignment warnings disabled>
...
```

...

</details>

### django-colorfield

color field for django models with a nice color-picker in the admin.

`pip install django-colorfield` · installs (wheel) · licence: MIT License · rank 4220 · last release 2025-04-30 · [PyPI](https://pypi.org/project/django-colorfield/) · [docs](https://github.com/fabiocaccamo/django-colorfield#readme)

<details><summary>README extract</summary>

simple color field for your models with a nice color-picker in the admin-interface.

Example:
```python
from colorfield.fields import ColorField
from django.db import models

class MyModel(models.Model):
    color = ColorField(default='#FF0000')
```

Sections: django-colorfield, Usage, Settings, Models, Field Options, format, image_field, samples, Forms, Model forms, Plain forms, Admin, See also

</details>

### httpx-auth

Authentication for HTTPX

`pip install httpx-auth` · installs (wheel) · licence: MIT License · rank 4229 · last release 2025-01-07 · [PyPI](https://pypi.org/project/httpx-auth/) · [docs](https://colin-b.github.io/httpx_auth/) · [source](https://github.com/Colin-b/httpx_auth)

<details><summary>README extract</summary>

> [!NOTE]
> Version 1.0.0 will be released once httpx is considered as stable (release of 1.0.0).
> However, current state can be considered as stable.

Provides authentication classes to be used with `httpx` authentication parameter.

Some of the supported authentication ...

Example:
```python
import httpx
from httpx_auth import OktaAuthorizationCodePKCE

okta = OktaAuthorizationCodePKCE(instance='testserver.okta-emea.com', client_id='54239d18-c68c-4c47-8bdd-ce71ea1d50cd')
with httpx.Client() as client:
    client.get(' auth=okta)
```

Sections: Authentication for HTTPX, Available authentication, OAuth 2, Parameters, Common providers, Okta (OAuth2 Proof Key for Code Exchange), Resource Owner Password Credentials flow

</details>

### pycarlo

Monte Carlo's Python SDK

`pip install pycarlo` · installs (wheel) · licence: Apache Software License · rank 4581 · last release 2026-11-08 · [PyPI](https://pypi.org/project/pycarlo/)

<details><summary>README extract</summary>

Features:
Pycarlo comprises two components: `core` and `features`.

All Monte Carlo API queries and mutations that you could execute via the API are supported via the
`core` library. ...

Example:
```python
from pycarlo.core import Client, Session
from pycarlo.features.circuit_breakers import CircuitBreakerService

# Example from our test.snowflake account.
endpoint = "

service = CircuitBreakerService(
    mc_client=Client(Session(mcd_profile="test-snow", endpoint=endpoint)), print_func=print
)
...
```

Sections: Pycarlo - Monte Carlo's Python SDK, Overview, Basic usage, Core, Examples, Circuit Breaker Example, Insight Upload Example, Features, Session configuration, Authenticating with OAuth, Integration Gateway API, Advanced configuration, Enum Backward Compatibility, References

</details>

### swig

SWIG is a software development tool that connects programs written in C and C++ with a variety of high-level programming languages.

`pip install swig` · installs (wheel) · licence: GPL-3.0-or-later · rank 4734 · last release 2026-10-08 · [PyPI](https://pypi.org/project/swig/) · [source](https://github.com/nightlark/swig-pypi)

_README extract left out: share-alike licence._

### Nuitka

Python compiler with full language support and CPython compatibility

`pip install Nuitka` · installs from source (sdist only) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 4855 · last release 2026-11-01 · [PyPI](https://pypi.org/project/Nuitka/) · [docs](https://nuitka.net/doc/user-manual.html) · [source](https://github.com/Nuitka/Nuitka)

_README extract left out: share-alike licence._

### frappe-bench

CLI to manage Multi-tenant deployments for Frappe apps

`pip install frappe-bench` · installs (wheel) · licence: GPL-3.0-only · rank 4858 · last release 2026-10-23 · [PyPI](https://pypi.org/project/frappe-bench/) · [docs](https://frappeframework.com/docs/user/en/bench) · [source](https://github.com/frappe/bench)

_README extract left out: share-alike licence._

### cibuildwheel

Build Python wheels on CI with minimal configuration.

`pip install cibuildwheel` · installs (wheel) · licence: BSD-2-Clause · rank 4969 · last release 2026-10-27 · [PyPI](https://pypi.org/project/cibuildwheel/) · [docs](https://cibuildwheel.pypa.io)

<details><summary>README extract</summary>

Documentation

Python wheels are great. Building them across Mac, Linux, Windows, on multiple versions of Python, is not.

`cibuildwheel` is here to help. `cibuildwheel` runs on your CI server - currently it supports GitHub Actions, Azure Pipelines, CircleCI, and GitLab CI - and it builds and tests your wheels across all of your platforms. ...

Sections: cibuildwheel, v4.3.5, v4.3.4, v4.3.3, v4.3.2, v4.3.1, See also

</details>

### extension-helpers

Utilities for building and installing packages with compiled extensions

`pip install extension-helpers` · installs (wheel) · licence: BSD-3-Clause · rank 4994 · last release 2026-09-15 · [PyPI](https://pypi.org/project/extension-helpers/)

<details><summary>README extract</summary>

The extension-helpers package includes convenience helpers to assist with
building Python packages with compiled C/Cython extensions. It is developed by
the Astropy project but is intended to be general and usable by any Python
package.

For more information, see the documentation at

</details>

### SCons

Open Source next-generation build tool.

`pip install SCons` · installs (wheel) · licence: MIT · rank 5049 · last release 2026-08-27 · [PyPI](https://pypi.org/project/SCons/) · [docs](https://scons.org/documentation.html) · [source](https://github.com/SCons/scons)

<details><summary>README extract</summary>

SCons is an Open Source software construction tool which orchestrates the construction of software
(and other tangible products such as documentation files) by determining which
component pieces must be built or rebuilt and invoking the necessary
commands to build them.

Features: ...

Sections: SCons - a Software Construction Tool, What is SCons?, Documentation, Execution Requirements, Getting Started Using SCons, Reporting Bugs, scons-help., Mailing Lists, For More Information

</details>

### uipath-runtime

Runtime abstractions and interfaces for building agents and automation scripts in the UiPath ecosystem

`pip install uipath-runtime` · installs (wheel) · licence: not stated · rank 5075 · last release 2026-10-21 · [PyPI](https://pypi.org/project/uipath-runtime/) · [docs](https://uipath.github.io/uipath-python/) · [source](https://github.com/UiPath/uipath-runtime-python)

<details><summary>README extract</summary>

Runtime abstractions and contracts for the UiPath Python SDK.

Features:
`uipath-runtime` provides the foundational interfaces and base contracts for building agent runtimes in the UiPath ecosystem. It defines the protocols that all runtime implementations must follow and provides utilities for execution context, event ...

Example:
```python
from typing import Any, Optional, AsyncGenerator

from uipath.core import UiPathTraceManager
from uipath.runtime import (
    UiPathExecutionRuntime,
    UiPathRuntimeResult,
    UiPathRuntimeStatus,
    UiPathExecuteOptions,
    UiPathStreamOptions,
    UiPathRuntimeProtocol,
    UiPathRuntimeFactoryProtocol
)

class ChildRuntime:
...
```

...

</details>

### apted

APTED algorithm for the Tree Edit Distance

`pip install apted` · installs (wheel) · licence: MIT License · rank 5240 · last release 2017-11-08 · [PyPI](https://pypi.org/project/apted/)

<details><summary>README extract</summary>

This is a Python implementation of the APTED algorithm, the
state-of-the-art solution for computing the tree edit distance [1,2],
which supersedes the RTED algorithm [3].

It is a port of the original Java implementation available at
 During the port, some changes
were made to reduce the duplication on symmetric operations and to make
it look more ...

Example:
```python
from apted import APTED, Config

class CustomConfig(Config):
   def rename(self, node1, node2):
        """Compares attribute .value of trees"""
        return 1 if node1.value != node2.value else 0

    def children(self, node):
        """Get left and right children of binary tree"""
        return [x for x in (node.left, node.right) if x]

...
```

...

</details>

### uipath-platform

HTTP client library for programmatic access to UiPath Platform

`pip install uipath-platform` · installs (wheel) · licence: not stated · rank 5286 · last release 2026-11-06 · [PyPI](https://pypi.org/project/uipath-platform/) · [docs](https://uipath.github.io/uipath-python/) · [source](https://github.com/UiPath/uipath-python)

<details><summary>README extract</summary>

Python SDK for interacting programmatically with UiPath services.

</details>

### b2luigi

b2luigi - bringing batch 2 luigi

`pip install b2luigi` · installs (wheel) · licence: GPL-3.0-or-later · rank 5292 · last release 2026-10-09 · [PyPI](https://pypi.org/project/b2luigi/) · [docs](https://b2luigi.belle2.org/)

_README extract left out: share-alike licence._

### uipath-core

UiPath Core abstractions

`pip install uipath-core` · installs (wheel) · licence: not stated · rank 5400 · last release 2026-11-02 · [PyPI](https://pypi.org/project/uipath-core/) · [docs](https://uipath.github.io/uipath-python/) · [source](https://github.com/UiPath/uipath-python)

<details><summary>README extract</summary>

Core abstractions and contracts for the UiPath Python SDK.

Example:
```python
from uipath.core.errors import ErrorCategory, UiPathFaultedTriggerError
```

Sections: UiPath Core, Modules, Errors, Serialization, Tracing, Guardrails, Chat, Dependencies

</details>

### imgtool

MCUboot's image signing and key management

`pip install imgtool` · installs (wheel) · licence: Apache Software License · rank 5542 · last release 2026-10-22 · [PyPI](https://pypi.org/project/imgtool/)

### sampleproject

A sample Python project

`pip install sampleproject` · installs (wheel) · licence: MIT License · rank 5706 · last release 2024-11-06 · [PyPI](https://pypi.org/project/sampleproject/) · [source](https://github.com/pypa/sampleproject/)

<details><summary>README extract</summary>

A sample project that exists as an aid to the Python Packaging User
Guide's Tutorial on Packaging and Distributing
Projects.

This project does not aim to cover best practices for Python project
development as a whole. For example, it does not provide guidance or tool
recommendations for version control, documentation, or testing. ...

</details>

### pcpp

A C99 preprocessor written in pure Python

`pip install pcpp` · installs (wheel) · licence: BSD License · rank 5723 · last release 2021-10-29 · [PyPI](https://pypi.org/project/pcpp/)

<details><summary>README extract</summary>

\(C) 2018-2021 Niall Douglas and (C) 2007-2020 David Beazley

PyPI: Github: API reference docs:

Travis master branch all tests passing for Python v2, v3 and PyPy v2, v3:

A pure universal Python C (pre-)preprocessor implementation very useful for pre-preprocessing header only
C++ libraries into single file includes and other such build or ...

...

</details>

### pypiserver

A minimal PyPI server for use with pip/easy_install.

`pip install pypiserver` · installs (wheel) · licence: BSD License; zlib/libpng License · rank 5806 · last release 2026-09-20 · [PyPI](https://pypi.org/project/pypiserver/) · [source](https://github.com/pypiserver/pypiserver)

<details><summary>README extract</summary>

Example:
```python
>>> from pypiserver import bottle_wrapper as bottle
>>> list(bottle.server_names.keys())
['cgi', 'gunicorn', 'cherrypy', 'eventlet', 'tornado', 'geventSocketIO',
'rocket', 'diesel', 'twisted', 'wsgiref', 'fapws3', 'bjoern', 'gevent',
'meinheld', 'auto', 'aiohttp', 'flup', 'gae', 'paste', 'waitress']
```

Sections: pypiserver, More details about pypi server run, More details about pypi-server update, Client-Side Configurations, Configuring pip, Uploading Packages Remotely, Apache Like Authentication (htpasswd), Upload with setuptools, Upload with twine, Using the Docker Image, Passing Arguments via Dockerfile CMD or ENTRYPOINT, Recipes, Managing the Package Directory, Serving Thousands of Packages

</details>

### ansible-builder

A tool for building Ansible Execution Environments

`pip install ansible-builder` · installs (wheel) · licence: Apache-2.0 · rank 5816 · last release 2026-10-13 · [PyPI](https://pypi.org/project/ansible-builder/) · [docs](https://docs.ansible.com/projects/builder/en/latest/) · [source](https://github.com/ansible/ansible-builder)

<details><summary>README extract</summary>

Ansible Builder is a tool that automates the process of building execution
environments using the schemas and tooling defined in various Ansible
Collections and by the user.

See the readthedocs page for `ansible-builder` at:

* We welcome your feedback, questions and ideas.
 See our Communication guide
 to learn how to join the conversation. ...

Sections: Ansible Builder, Get Involved

</details>

### invoke-tasklib

Reusable Invoke tasks shared across Python projects.

`pip install invoke-tasklib` · installs (wheel) · licence: BSD-3-Clause · rank 5845 · last release 2026-10-03 · [PyPI](https://pypi.org/project/invoke-tasklib/) · [docs](https://durandtibo.github.io/invoke-tasklib/) · [source](https://github.com/durandtibo/invoke-tasklib)

<details><summary>README extract</summary>

Reusable Invoke tasks shared across Python
projects: formatting, linting, type-checking, testing, environment setup,
security auditing, releasing, documentation, and cleanup — all as a single
importable package instead of a `tasks.py` you copy-paste and let drift
between repositories.

:book: Full documentation:

Example:
```python
# tasks.py
from invoke_tasklib import ns
```

Sections: invoke-tasklib, Quickstart, Tasks, Configuration, Composing a custom subset of tasks, API Stability

</details>

### mmdb-writer

Make `mmdb` format ip library file which can be read by maxmind official language reader

`pip install mmdb-writer` · installs (wheel) · licence: MIT License · rank 5971 · last release 2026-06-01 · [PyPI](https://pypi.org/project/mmdb-writer/) · [source](https://github.com/vimt/MaxMind-DB-Writer-python)

<details><summary>README extract</summary>

- MaxMind-DB-Writer-python
 * Install
 * Usage
 * Examples
 * Using the Java Client
 + TLDR
 + Underlying Principles
 * Type Enforcement

Make `mmdb` format ip library file which can be read by
`maxmind` official language reader

~~The official perl writer was written in perl,
which was difficult to customize. ...

Example:
```python
from netaddr import IPSet

from mmdb_writer import MMDBWriter

writer = MMDBWriter()

writer.insert_network(IPSet(['1.1.0.0/24', '1.1.1.0/24']), {'country': 'COUNTRY', 'isp': 'ISP'})
writer.to_db_file('test.mmdb')

import maxminddb

m = maxminddb.open_database('test.mmdb')
r = m.get('1.1.1.1')
assert r == {'country': 'COUNTRY', 'isp': 'ISP'}
```

...

</details>

### cxxfilt

Python interface to c++filt / abi::__cxa_demangle

`pip install cxxfilt` · installs (wheel) · licence: BSD License · rank 5998 · last release 2021-08-21 · [PyPI](https://pypi.org/project/cxxfilt/)

<details><summary>README extract</summary>

Demangling C++ symbols in Python / interface to abi::__cxa_demangle

Example:
```python
>>> import cxxfilt
>>> cxxfilt.demangle('_ZNSt22condition_variable_anyD2Ev')
'std::condition_variable_any::~condition_variable_any()'
```

Sections: cxxfilt, Usage, 0.3.0

</details>

### podman-compose

A script to run docker-compose.yml using podman

`pip install podman-compose` · installs (wheel) · licence: GPL-2.0-only · rank 6073 · last release 2026-06-03 · [PyPI](https://pypi.org/project/podman-compose/)

_README extract left out: share-alike licence._

### livereload

Python LiveReload is an awesome tool for web developers

`pip install livereload` · installs (wheel) · licence: BSD License · rank 6077 · last release 2024-12-18 · [PyPI](https://pypi.org/project/livereload/)

<details><summary>README extract</summary>

Reload webpages on changes, without hitting refresh in your browser.

Sections: LiveReload, Documentation

</details>

### nanopb

Nanopb is a small code-size Protocol Buffers implementation in ansi C. It is especially suitable for use in microcontrollers, but fits any memory restricted system.

`pip install nanopb` · installs (wheel) · licence: OSI Approved · rank 6120 · last release 2024-12-01 · [PyPI](https://pypi.org/project/nanopb/) · [docs](https://jpa.kapsi.fi/nanopb/docs/index.html) · [source](https://github.com/nanopb/nanopb/)

### delocate

Move macOS dynamic libraries into package

`pip install delocate` · installs (wheel) · licence: BSD License · rank 6152 · last release 2025-01-30 · [PyPI](https://pypi.org/project/delocate/)

<details><summary>README extract</summary>

macOS utilities to:

* find dynamic libraries imported from python extensions
* copy needed dynamic libraries to directory within package
* update macOS `install_names` and `rpath` to cause code to load from copies
 of libraries

Provides scripts: ...

Example:
```python
$ delocate-wheel --require-archs=intel scipy-0.14.0-cp34-cp34m-macosx_10_6_intel.whl
Traceback (most recent call last):
File "/Users/mb312/.virtualenvs/delocate/bin/delocate-wheel", line 77, in <module>
    main()
File "/Users/mb312/.virtualenvs/delocate/bin/delocate-wheel", line 69, in main
    check_verbose=opts.verbose)
...
```

Sections: Delocate, The problem, A solution, Checking required architectures, Making dual-architecture binaries, Troubleshooting, DelocationError: "library does not exist", Code

</details>

### tombi

🦅 TOML Toolkit 🦅

`pip install tombi` · installs (wheel) · licence: MIT License · rank 6202 · last release 2026-11-04 · [PyPI](https://pypi.org/project/tombi/) · [source](https://github.com/tombi-toml/tombi)

<details><summary>README extract</summary>

TOML Toolkit

 Tombi(鳶 /toɴbi/) provides a Formatter, Linter, and Language Server

 Documentation

Sections: 🦅, Quick Start

</details>

### triton-windows

A language and compiler for custom Deep Learning operations

`pip install triton-windows` · does not install on CPython 3.14 · licence: MIT · rank 6266 · last release 2026-10-28 · [PyPI](https://pypi.org/project/triton-windows/)

### graphtty

Turn any directed graph into colored ASCII art for your terminal

`pip install graphtty` · installs (wheel) · licence: MIT · rank 6276 · last release 2026-02-15 · [PyPI](https://pypi.org/project/graphtty/) · [docs](https://uipath.github.io/uipath-python/) · [source](https://github.com/uipath/graphtty)

<details><summary>README extract</summary>

Turn any directed graph into colored ASCII art for your terminal. Pure Python, zero external dependencies.

Example:
```python
from graphtty import render

graph = {
    "nodes": [
        {"id": "start", "name": "User Input", "type": "entry"},
        {"id": "router", "name": "Router", "type": "condition"},
        {"id": "search", "name": "Web Search", "type": "tool"},
        {"id": "calc", "name": "Calculator", "type": "tool"},
...
```

Sections: graphtty, Deep Agent (ocean theme), Supervisor Agent (dracula theme), Quick start, CLI, Themes, JSON format, Benchmarks, Related Projects

</details>

### cmarkgfm

Minimal bindings to GitHub's fork of cmark

`pip install cmarkgfm` · installs (wheel) · licence: MIT · rank 6277 · last release 2025-10-22 · [PyPI](https://pypi.org/project/cmarkgfm/) · [source](https://github.com/theacodes/cmarkgfm)

<details><summary>README extract</summary>

Minimalist Python bindings to GitHub's fork of cmark.

Example:
```python
import cmarkgfm

html = cmarkgfm.markdown_to_html(markdown_text)
```

Sections: cmarkgfm - Python bindings to GitHub's cmark, Usage, Advanced Usage

</details>

### firebase-functions

Firebase Functions Python SDK

`pip install firebase-functions` · installs (wheel) · licence: Apache-2.0 · rank 6532 · last release 2026-06-04 · [PyPI](https://pypi.org/project/firebase-functions/) · [docs](https://firebase.google.com/docs/functions) · [source](https://github.com/firebase/firebase-functions-python)

<details><summary>README extract</summary>

The `firebase-functions` package provides an SDK for defining Cloud Functions for Firebase in Python.

Cloud Functions provides hosted, private, and scalable environment where you can run server code. ...

Example:
```python
# functions/main.py
from firebase_functions import db_fn
from notify_users import api

@db_fn.on_value_created(reference="/posts/{post_id}")
def new_post(event):
    print(f"Received new post with ID: {event.params.get('post_id')}")
    return notifyUsers(event.data)
```

Sections: Cloud Functions for Firebase Python SDK, Learn more, Usage

</details>

### check-wheel-contents

Check your wheels have the right contents

`pip install check-wheel-contents` · installs (wheel) · licence: MIT · rank 6707 · last release 2025-08-02 · [PyPI](https://pypi.org/project/check-wheel-contents/) · [source](https://github.com/jwodder/check-wheel-contents)

<details><summary>README extract</summary>

GitHub
| PyPI
| Issues
| Changelog

Getting the right files into your wheel is tricky, and sometimes we mess up and
publish a wheel containing `pycache` directories or `tests/`. ...

Sections: Usage, Options, Configuration, Configuration File, Configuration Options, Checks, W001 — Wheel contains .pyc/.pyo files, W002 — Wheel contains duplicate files, W003 — Wheel contains non-module at library toplevel, W004 — Module is not located at importable path, W005 — Wheel contains common toplevel name in library, W006 — _init__.py at top level of library, W007 — Wheel library is empty, W008 — Wheel is empty

</details>

### pytest-cmake

Provide CMake module for Pytest

`pip install pytest-cmake` · installs (wheel) · licence: MIT License · rank 6795 · last release 2026-09-28 · [PyPI](https://pypi.org/project/pytest-cmake/) · [docs](https://python-cmake.github.io/pytest-cmake) · [source](https://github.com/python-cmake/pytest-cmake)

<details><summary>README extract</summary>

This project provides convenient ways to use Pytest
within a CMake project. The package can be discovered from a specific range of
versions on Linux, macOS or Windows using the
find_package
function:

A ``pytest_discover_tests`` function is provided to simplify automatic
testing for C++ projects with Python bindings. ...

Sections: Pytest CMake, Documentation

</details>

### dbt

Build analytics the way engineers build applications

`pip install dbt` · installs from source (sdist only) · licence: not stated · rank 6853 · last release 2026-11-03 · [PyPI](https://pypi.org/project/dbt/)

<details><summary>README extract</summary>

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

Analysts using dbt can transform their data by simply writing select statements, while dbt handles turning these statements into tables and views in a data warehouse. ...

Sections: dbt, Understanding dbt, Getting started

</details>

### fno

Run your coding agents as one team: one backlog they all work from, and a chat where they message each other and you, across harnesses and machines.

`pip install fno` · installs (wheel) · licence: Apache Software License · rank 7098 · last release 2026-11-06 · [PyPI](https://pypi.org/project/fno/) · [source](https://github.com/fnodotdev/fno)

<details><summary>README extract</summary>

CLI for the footnote autonomous delivery pipeline.

Sections: fno (footnote CLI), Quickstart, Compat alias: `footnote`, Removed binary: `megawalk`, v2 state layout (vestigial), Subcommand trees, Backlog commands (top-level), Backlog health monitoring, `fno agents mail` (cross-project messaging), Commands, Message kinds, Shared options, Invariants

</details>

### verlib2

A standalone bundle of "distutils.version" and "packaging.version", without anything else.

`pip install verlib2` · installs (wheel) · licence: not stated · rank 7203 · last release 2026-07-08 · [PyPI](https://pypi.org/project/verlib2/) · [source](https://github.com/pyveci/verlib2)

<details><summary>README extract</summary>

<!-- » [Documentation] -->

» [Changelog]
| [PyPI]
| [Issues]
| [Source code]
| [License]

A standalone bundle of `distutils.version` and `packaging.version`,
without anything else.

[verlib] and [Distutils] are the implementations of [PEP 386].
[packaging.version] is the implementation of [PEP 440]. ...

Example:
```python
from verlib2 import Version

assert Version("1.0.dev456") < Version("1!1.2.rev33+123456")
```

Sections: verlib2, About, Rationale, Setup, Usage, Versioning, Other projects, Prior Art

</details>

### fusesoc

Award-winnning package manager and build abstraction tool for HDL code

`pip install fusesoc` · installs (wheel) · licence: BSD License · rank 7377 · last release 2026-09-08 · [PyPI](https://pypi.org/project/fusesoc/) · [docs](https://fusesoc.readthedocs.io) · [source](https://github.com/olofk/fusesoc)

<details><summary>README extract</summary>

FuseSoC is an award-winning package manager and a set of build tools for
HDL (Hardware Description Language) code.

Its main purpose is to increase reuse of IP (Intellectual Property)
cores and be an aid for creating, building and simulating SoC solutions.

FuseSoC makes it easier to

- reuse existing cores ...

Sections: FuseSoC, Introduction, Getting started, Quick start, Next steps, Need help?, Further reading

</details>

### django-admin-interface

django's default admin interface with superpowers - customizable themes, popup windows replaced by modals and many other features.

`pip install django-admin-interface` · installs (wheel) · licence: MIT License · rank 7481 · last release 2025-12-19 · [PyPI](https://pypi.org/project/django-admin-interface/) · [docs](https://github.com/fabiocaccamo/django-admin-interface#readme)

<details><summary>README extract</summary>

django-admin-interface is a modern responsive flat admin interface customizable by the admin itself.

Features:
- Beautiful default django-theme
- Themes management and customization *(you can customize admin title, logo and colors)*
- Responsive
- Related modal *(instead of the old popup window)*
- Environment name/marker
- Language chooser ...

Example:
```python
class MyModelAdmin(admin.ModelAdmin):
    # ...
    fieldsets = [
        ("Section title", {
            "classes": ("collapse", "expanded"),
            "fields": (...),
        }),
    ]
    # ...
```

...

</details>

### mmtf-python

A decoding libary for the PDB mmtf format

`pip install mmtf-python` · installs (wheel) · licence: MIT License · rank 7680 · last release 2022-07-06 · [PyPI](https://pypi.org/project/mmtf-python/)

### astrapy

A Python client for the Data API on DataStax Astra DB

`pip install astrapy` · installs (wheel) · licence: Apache Software License · rank 7721 · last release 2026-10-19 · [PyPI](https://pypi.org/project/astrapy/) · [docs](https://docs.datastax.com/en/astra-db-serverless/api-reference/dataapiclient.html) · [source](https://github.com/datastax/astrapy)

<details><summary>README extract</summary>

A pythonic client for DataStax Astra DB.

_This README targets AstraPy version 2.0+. Click here for v1 and here for the v0 API (which you should not really be using by now)._

Example:
```python
from astrapy import DataAPIClient
from astrapy.constants import VectorMetric
from astrapy.ids import UUID
from astrapy.info import CollectionDefinition

ASTRA_DB_APPLICATION_TOKEN = "AstraCS:..."
ASTRA_DB_API_ENDPOINT = "

# Connect and create the Database object
my_client = DataAPIClient()
my_database = my_client.get_database(
...
```

...

</details>

### requests-auth

Authentication for Requests

`pip install requests-auth` · installs (wheel) · licence: MIT License · rank 7802 · last release 2024-06-18 · [PyPI](https://pypi.org/project/requests-auth/) · [docs](https://colin-b.github.io/requests_auth/) · [source](https://github.com/Colin-b/requests_auth)

<details><summary>README extract</summary>

Provides authentication classes to be used with `requests` authentication parameter.

Some of the supported authentication

- OAuth2
 - Authorization Code Flow
 - Okta
 - Authorization Code Flow with PKCE
 - Okta
 - Resource Owner Password Credentials flow
 - Client Credentials Flow
 - Okta
 - Implicit Flow
 - Microsoft Entra (Access Token)
 - ...

Example:
```python
import requests
from requests_auth import OktaAuthorizationCodePKCE

okta = OktaAuthorizationCodePKCE(instance='testserver.okta-emea.com', client_id='54239d18-c68c-4c47-8bdd-ce71ea1d50cd')
requests.get(' auth=okta)
```

Sections: Authentication for Requests, Available authentication, OAuth 2, Parameters, Common providers, Okta (OAuth2 Proof Key for Code Exchange), Resource Owner Password Credentials flow

</details>

### solc-select

Manage multiple Solidity compiler versions.

`pip install solc-select` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 7829 · last release 2025-12-04 · [PyPI](https://pypi.org/project/solc-select/) · [source](https://github.com/crytic/solc-select.git)

_README extract left out: share-alike licence._

### pproxy

Proxy server that can tunnel among remote servers by regex rules.

`pip install pproxy` · installs (wheel) · licence: MIT License · rank 7871 · last release 2024-01-16 · [PyPI](https://pypi.org/project/pproxy/)

<details><summary>README extract</summary>

HTTP/HTTP2/HTTP3/Socks4/Socks5/Shadowsocks/SSH/Redirect/Pf/QUIC TCP/UDP asynchronous tunnel proxy implemented in Python3 asyncio.

Features:
- Lightweight single-thread asynchronous IO.
- Pure python, no additional library required.
- Proxy client/server for TCP/UDP.
- Schedule (load balance) among remote servers.
- Incoming traffic auto-detect.
- Tunnel/jump/backward-jump support. ...

Sections: python-proxy, QuickStart, Run With Docker, Features, Scheduling Algorithms, Requirement, Usage, URI Syntax, Client API, Server API, Examples, Projects

</details>

### fbmessenger

A python library to communicate with the Facebook Messenger API's

`pip install fbmessenger` · installs (wheel) · licence: Apache Software License · rank 7903 · last release 2019-04-24 · [PyPI](https://pypi.org/project/fbmessenger/)

### wavedrom

WaveDrom compatible python command line

`pip install wavedrom` · installs from source (sdist only) · licence: MIT License · rank 7966 · last release 2022-05-27 · [PyPI](https://pypi.org/project/wavedrom/)

<details><summary>README extract</summary>

This is a python module and command line fully compatible with WaveDrom, which is originally implemented in JavaScript. It is useful if you want to generate wavedrom diagrams from a python environment or simply don't want to install the _Node.js environment just to use WaveDrom as simple command line. ...

Sections: WaveDromPy, Usage, Important notice, AsciiDoctor example

</details>

### modulegraph

Python module dependency analysis tool

`pip install modulegraph` · installs (wheel) · licence: MIT License · rank 8067 · last release 2025-11-22 · [PyPI](https://pypi.org/project/modulegraph/) · [docs](https://modulegraph.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/modulegraph)

<details><summary>README extract</summary>

modulegraph determines a dependency graph between Python modules primarily
by bytecode analysis for import statements.

modulegraph uses similar methods to modulefinder from the standard library,
but uses a more flexible internal representation, has more extensive
knowledge of special cases, and is extensible.

Sections: modulegraph, Project links, Version 0.19.7, Version 0.19.6, 0.19.5, 0.19.4, 0.19.3, 0.19.2, 0.19.1, 0.19, 0.18, 0.17, 0.16, 0.15

</details>

### unicon

Unicon Connection Library

`pip install unicon` · installs (wheel) · licence: Apache Software License · rank 8150 · last release 2026-11-03 · [PyPI](https://pypi.org/project/unicon/)

<details><summary>README extract</summary>

Unicon is a package aiming to provide a unified connection experience to network
devices through typical command-line management interface. By wrapping the
underlying session (eg, telnet, ssh), Unicon provides:

- direct and proxied connections through any common CLI interface (telnet, ssh, serial etc) ...

Sections: Unicon - Universal Connection Library, Requirements, Quick Start, Examples

</details>

### go-task-bin

A fast, cross-platform build tool inspired by Make, designed for modern workflows.

`pip install go-task-bin` · installs (wheel) · licence: MIT · rank 8181 · last release 2026-10-02 · [PyPI](https://pypi.org/project/go-task-bin/) · [source](https://github.com/Bing-su/pip-binary-factory)

<details><summary>README extract</summary>

A fast, cross-platform build tool inspired by Make, designed for modern workflows.

 Installation • Getting Started • Docs • Twitter • Bluesky • Mastodon • Discord

Sections: Task: The Modern Task Runner, go-task-bin

</details>

### django-maintenance-mode

shows a 503 error page when maintenance-mode is on.

`pip install django-maintenance-mode` · installs (wheel) · licence: MIT License · rank 8387 · last release 2026-07-14 · [PyPI](https://pypi.org/project/django-maintenance-mode/) · [docs](https://github.com/fabiocaccamo/django-maintenance-mode#readme)

<details><summary>README extract</summary>

django-maintenance-mode shows a 503 error page when maintenance-mode is on.

It works at application level, so your django instance should be up.

It doesn't use database and doesn't prevent database access.

Example:
```python
# by default, to get/set the state value a local file backend is used
# if you want to use the db or cache, you can create a custom backend
# custom backends must extend 'maintenance_mode.backends.AbstractStateBackend' class
# and implement get_value(self) and set_value(self, val) methods
...
```

Sections: django-maintenance-mode, Configuration (optional), Settings, Context Processors, Logging, Context Managers, URLs, Views, Function-based views, Class-based views, Usage, Python, Templates, Terminal

</details>

### rake-nltk

RAKE short for Rapid Automatic Keyword Extraction algorithm, is a domain independent keyword extraction algorithm which tries to determine key phrases in a body of text by analyzing the frequency of word appearance and its co-occurance with other words in the text.

`pip install rake-nltk` · installs (wheel) · licence: MIT License · rank 8409 · last release 2021-09-15 · [PyPI](https://pypi.org/project/rake-nltk/) · [source](https://github.com/csurfer/rake-nltk)

<details><summary>README extract</summary>

RAKE short for Rapid Automatic Keyword Extraction algorithm, is a domain
independent keyword extraction algorithm which tries to determine key
phrases in a body of text by analyzing the frequency of word appearance
and its co-occurance with other words in the text.

Features:
* Ridiculously simple interface.
* Configurable word and sentence tokenizers, language based stop words etc
* Configurable ranking metric.

Example:
```python
from rake_nltk import Rake

# Uses stopwords for english from NLTK, and all puntuation characters by
# default
r = Rake()

# Extraction given the text.
r.extract_keywords_from_text(<text to process>)

# Extraction given the list of strings where each string is a sentence.
r.extract_keywords_from_sentences(<list of sentences>)

...
```

...

</details>

### unicon.plugins

Unicon Connection Library Plugins

`pip install unicon.plugins` · installs (wheel) · licence: Apache Software License · rank 8427 · last release 2026-11-03 · [PyPI](https://pypi.org/project/unicon.plugins/)

<details><summary>README extract</summary>

Unicon is a package aiming to provide a unified connection experience to network
devices through typical command-line management interface. By wrapping the
underlying session (eg, telnet, ssh), Unicon provides:

- direct and proxied connections through any common CLI interface (telnet, ssh, serial etc) ...

Sections: Unicon Plugins, Requirements, Quick Start, Examples

</details>

### pyats

pyATS - Python Automation Test System

`pip install pyats` · installs (wheel) · licence: Apache Software License · rank 8508 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS - Cisco Python Automated Test System, pyATS Package, Requirements, Quick Start, Example

</details>

### eniris

Eniris API driver for Python

`pip install eniris` · installs (wheel) · licence: MIT License · rank 8539 · last release 2026-02-10 · [PyPI](https://pypi.org/project/eniris/)

<details><summary>README extract</summary>

This repository contains the official Eniris API driver for Python. This driver takes care of authentication as well as request retries and timeouts, in accordance with the authentication API documentation. It offers users an interface which is inspired by the popular requests library.

Example:
```python
from eniris import ApiDriver

driver = ApiDriver("myUsername", "myPassword")
http_response = driver.get("/v1/device")
response_body = http_response.json()
print(response_body'device')
driver.close()
```

Sections: Eniris API driver for Python, Quick Example, Details

</details>

### venv-pack

Package virtual environments for redistribution

`pip install venv-pack` · installs (wheel) · licence: BSD License · rank 8553 · last release 2018-08-23 · [PyPI](https://pypi.org/project/venv-pack/) · [source](https://github.com/jcrist/venv-pack/)

<details><summary>README extract</summary>

`venv-pack` is a command-line tool for packaging virtual environments for
distribution. Please refer to the documentation for more information.

For a similar tool for conda environments, see conda-pack

</details>

### keystone-engine

Keystone assembler engine

`pip install keystone-engine` · installs (wheel) · licence: BSD License · rank 8585 · last release 2020-06-21 · [PyPI](https://pypi.org/project/keystone-engine/)

<details><summary>README extract</summary>

Keystone is a lightweight multi-platform, multi-architecture assembler framework.
It offers some unparalleled features:

- Multi-architecture, with support for Arm, Arm64 (AArch64/Armv8), Ethereum Virtual Machine, Hexagon, Mips, PowerPC, Sparc, SystemZ & X86 (include 16/32/64bit).
- Clean/simple/lightweight/intuitive architecture-neutral API. ...

</details>

### pyats.datastructures

pyATS Datastructures: Extended Datastructures for Grownups

`pip install pyats.datastructures` · installs (wheel) · licence: Apache Software License · rank 8611 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.datastructures/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS Datastructures Component, Datastructures Package, Requirements, Quick Start

</details>

### pyats.easypy

pyATS Easypy: launcher and runtime environment

`pip install pyats.easypy` · installs (wheel) · licence: Apache Software License · rank 8616 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.easypy/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS Easypy Component, Easypy Package, Requirements, Quick Start

</details>

### pyats.topology

pyATS Topology: Topology Objects and Testbed YAMLs

`pip install pyats.topology` · installs (wheel) · licence: Apache Software License · rank 8629 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.topology/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS Topology Component, Topology Package, Requirements, Quick Start

</details>

### pyats.aetest

pyATS AEtest: Testscript Engine

`pip install pyats.aetest` · installs (wheel) · licence: Apache Software License · rank 8632 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.aetest/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS AEtest Component, AEtest Package, Requirements, Quick Start

</details>

### pyats.utils

pyATS Utils: Utilities Module

`pip install pyats.utils` · installs (wheel) · licence: Apache Software License · rank 8635 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.utils/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS Utilities Component, Utilities Package, Requirements, Quick Start

</details>

### pyats.reporter

pyATS Reporter: Result Collection and Reporting

`pip install pyats.reporter` · installs (wheel) · licence: Apache Software License · rank 8647 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.reporter/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS Reporter Component, Reporter Package, Requirements, Quick Start

</details>

### pyats.connections

pyATS Connection: Device Connection Handling & Base Classes

`pip install pyats.connections` · installs (wheel) · licence: Apache Software License · rank 8651 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.connections/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS Connections Component, Connections Package, Requirements, Quick Start

</details>

### pyats.aereport

pyATS AEreport: Result Collection and Reporting

`pip install pyats.aereport` · installs (wheel) · licence: Apache Software License · rank 8661 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.aereport/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS AEReport Component, AEReport Package, Requirements, Quick Start

</details>

### pyats.tcl

pyATS Tcl: Tcl Integration and Objects

`pip install pyats.tcl` · installs (wheel) · licence: Apache Software License · rank 8664 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.tcl/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS Tcl Component, Tcl Package, Requirements, Quick Start

</details>

### pyats.log

pyATS Log: Logging Format and Utilities

`pip install pyats.log` · installs (wheel) · licence: Apache Software License · rank 8667 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.log/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS Logs Component, Logs Package, Requirements, Quick Start

</details>

### pyats.kleenex

pyATS Kleenex: Testbed Preparation, Clean & Finalization

`pip install pyats.kleenex` · installs (wheel) · licence: Apache Software License · rank 8668 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.kleenex/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS Kleenex Component, Kleenex Package, Requirements, Quick Start

</details>

### montecarlodata

Monte Carlo's CLI

`pip install montecarlodata` · installs (wheel) · licence: Apache Software License · rank 8672 · last release 2026-10-23 · [PyPI](https://pypi.org/project/montecarlodata/)

<details><summary>README extract</summary>

Monte Carlo's Alpha CLI!

Sections: Monte Carlo CLI, Quick start, User settings, Help, Examples, Configure a named profile with custom config-path, List active integrations, Apply monitors configuration, Import DBT manifest

</details>

### pyats.results

pyATS Results: Representing Results using Objects

`pip install pyats.results` · installs (wheel) · licence: Apache Software License · rank 8684 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.results/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS Results Component, Results Package, Requirements, Quick Start

</details>

### pyats.async

pyATS Async: Asynchronous Execution of Codes

`pip install pyats.async` · installs (wheel) · licence: Apache Software License · rank 8694 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.async/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS Async Component, Async Package, Requirements, Quick Start

</details>

### airflow-mcd

Monte Carlo's Apache Airflow Provider

`pip install airflow-mcd` · installs (wheel) · licence: Apache Software License · rank 8895 · last release 2026-05-07 · [PyPI](https://pypi.org/project/airflow-mcd/)

<details><summary>README extract</summary>

Monte Carlo's Airflow provider.

Example:
```python
dag = DAG(
    'dag_name',~~~~
    **mcd_callbacks.dag_callbacks,
)

task = BashOperator(
    task_id='task_name',
    bash_command='command',
    dag=dag,
    **mcd_callbacks.task_callbacks,
)
```

Sections: airflow-mcd, Basic usage, Callbacks, Broad Callbacks, Explicit Callbacks, Hooks, Operators

</details>

### genie

Genie: THE standard pyATS Library System

`pip install genie` · installs (wheel) · licence: Apache Software License · rank 8933 · last release 2026-11-03 · [PyPI](https://pypi.org/project/genie/)

<details><summary>README extract</summary>

Genie is both a library framework and a test harness that facilitates rapid
development, encourage re-usable and simplify writing test automation. Genie bundled with
the modular architecture of pyATS framework accelerates and simplifies test
automation leveraging all the perks of the Python programming language in an
object-orienting fashion. ...

Sections: Genie - THE pyATS Standard Library, Component Breakdown, Requirements, Quick Start, Example

</details>

### http-exceptions

Raisable HTTP Exceptions

`pip install http-exceptions` · installs (wheel) · licence: MIT License · rank 8994 · last release 2022-02-15 · [PyPI](https://pypi.org/project/http-exceptions/) · [source](https://github.com/DeveloperRSquared/http-exceptions)

<details><summary>README extract</summary>

Raisable HTTP Exceptions

Example:
```python
# e.g. app/internal.py
def some_function() -> None:
    raise SomeError()

# e.g. app/api.py
def api(request: Request) -> Response:
    try:
        response = some_function()
    except SomeError:
        response = Response(status_code=403)
    return response
```

Sections: HTTP Exceptions, What is it good for?, What else?, `HTTPException`, `ClientException`, `ServerException`, Available Exceptions, First time setup, Running tests, Links

</details>

### fastapi-health

Heath check on FastAPI applications.

`pip install fastapi-health` · installs (wheel) · licence: MIT License · rank 9119 · last release 2021-08-20 · [PyPI](https://pypi.org/project/fastapi-health/) · [source](https://github.com/Kludex/fastapi-health)

<details><summary>README extract</summary>

The goal of this package is to help you to implement the Health Check API pattern.

Example:
```python
from fastapi import FastAPI, Depends
from fastapi_health import health

def get_session():
    return True

def is_database_online(session: bool = Depends(get_session)):
    return session

app = FastAPI()
app.add_api_route("/health", health([is_database_online]))
```

Sections: FastAPI Health 🚑️, Quick Start, Advanced Usage

</details>

### javascript

Call and interop Node.js APIs with Python

`pip install javascript` · installs (wheel) · licence: MIT License · rank 9123 · last release 2025-09-25 · [PyPI](https://pypi.org/project/javascript/) · [source](https://github.com/extremeheat/JSPyBridge/)

<details><summary>README extract</summary>

Interoperate Node.js and Python. You can run Python from Node.js, *or* run Node.js from Python. Work in progress.

Requires Node.js 18 and Python 3.8 or newer.

Features:
* Ability to call async and sync functions and get object properties with a native feel
* Built-in garbage collection
* Bidirectional callbacks with arbitrary arguments
* Iteration and exception handling support
* Object inspection allows you to ...

Example:
```python
from javascript import require, globalThis

chalk, fs = require("chalk"), require("fs")

print("Hello", chalk.red("world!"), "it's", globalThis.Date().toLocaleString())
fs.writeFileSync("HelloWorld.txt", "hi!")
```

...

</details>

### vbuild

A simple module to extract html/script/style from a vuejs '.vue' file (can minimize/es2015 compliant js) ... just py2 or py3, NO nodejs !

`pip install vbuild` · installs (wheel) · licence: MIT License · rank 9133 · last release 2023-08-03 · [PyPI](https://pypi.org/project/vbuild/) · [docs](https://github.com/manatlan/vbuild) · [source](https://github.com/manatlan/vbuild)

<details><summary>README extract</summary>

"Compile" your VueJS components (*.vue) to standalone html/js/css ... python only, no need of nodejs. And you can use python components with vbuild, in your vue/sfc files !!!

It's just an utility to generate HTML(template), SCRIPT and STYLE from a VUE/SFC component (*.vue). ...

Features:
* NO node-js stack, only pure python (py2 or py3 compliant)
 * Ability to use python components
 * Components can be styled with SASS or LESS ccs-pre-processors !
 * Provide a JS-minifier (ES5 compliant JS, via closure)
 * Ability to post process ...

Example:
```python
import vbuild

c=vbuild.render("mycompo.vue")
# c=vbuild.render("vues/*.vue")
# c=vbuild.render( "c1.vue", "c2.vue" )
# c=vbuild.render( "c1.vue", "vues/*.vue" )

print( c.html )
print( c.script )
print( c.style )

# or

...

</details>

### pipmaster

A versatile Python package manager utility for simplifying package installation, updates, checks, and environment management.

`pip install pipmaster` · installs (wheel) · licence: Apache-2.0 · rank 9184 · last release 2026-10-26 · [PyPI](https://pypi.org/project/pipmaster/) · [source](https://github.com/ParisNeo/pipmaster)

<details><summary>README extract</summary>

🎉 Now available on PyPI! Install with: `pip install pipmaster`

Stop telling your users to `pip install -r requirements.txt`. Start building professional, self‑sufficient Python applications that just work.

`pipmaster` is the ultimate toolkit for declarative and programmatic package management. ...

Features:
`pipmaster` bridges the gap between development and deployment, solving the classic “it works on my machine” problem.

* Automate Your Setup: Your application can configure its own environment on first launch. ...

Example:
```python
import pipmaster as pm

# Ensure a single package is installed
pm.ensure_packages("rich")

# Ensure multiple packages with version requirements
pm.ensure_packages(["pandas", "numpy>=1.20"], verbose=True)

# Ensure packages from a requirements.txt file
...

</details>

### loki-mode-sdk

Python SDK for Loki Mode - autonomous multi-agent development platform

`pip install loki-mode-sdk` · installs (wheel) · licence: BUSL-1.1 · rank 9186 · last release 2026-11-06 · [PyPI](https://pypi.org/project/loki-mode-sdk/) · [docs](https://github.com/asklokesh/loki-mode/wiki) · [source](https://github.com/asklokesh/loki-mode)

<details><summary>README extract</summary>

Python SDK for Loki Mode, the autonomous multi-agent development platform.

Example:
```python
from loki_mode_sdk import Client

client = Client(base_url="

# Check dashboard status
status = client.get_status()
print(status)

# List projects
projects = client.list_projects()
for p in projects:
    print(f"{p.id}: {p.name} ({p.status})")
```

Sections: loki-mode-sdk, Quick Start, API Reference, Client Methods, Requirements

</details>

### pyaxmlparser

Python3 Parser for Android XML file and get Application Name without using Androguard

`pip install pyaxmlparser` · installs (wheel) · licence: Apache Software License · rank 9210 · last release 2024-03-20 · [PyPI](https://pypi.org/project/pyaxmlparser/)

<details><summary>README extract</summary>

A simple parser to parse Android XML file.

Sections: axmlparser, Usage, CLI, Python package

</details>

### py-automapper

Library for automatically mapping one object to another

`pip install py-automapper` · installs (wheel) · licence: MIT License · rank 9217 · last release 2025-03-09 · [PyPI](https://pypi.org/project/py-automapper/) · [source](https://github.com/anikolaienko/py-automapper.git)

<details><summary>README extract</summary>

> [!IMPORTANT]
> Renewing maintanance of this library!
> After a long pause, I see the library is still in use and receives more stars. Thank you all who likes and uses it. So, I renew the py-automapper maintanance.
> Expect fixes and new version soon.

Build Status

Table of Contents:
- Versions
- About
- Contribute ...

Example:
```python
class UserInfo:
    def init(self, name: str, profession: str, age: int):
        self.name = name
        self.profession = profession
        self.age = age

class PublicUserInfo:
    def init(self, name: str, profession: str):
        self.name = name
        self.profession = profession

user_info = UserInfo("John Malkovich", "engineer", 35)
```

...

</details>

### doppler-env

Inject Doppler secrets as environment variables into your Python application during local development with debugging support for PyCharm and Visual Studio Code.

`pip install doppler-env` · installs (wheel) · licence: Apache Software License · rank 9337 · last release 2022-12-08 · [PyPI](https://pypi.org/project/doppler-env/) · [source](https://github.com/dopplerhq/python-doppler-env)

<details><summary>README extract</summary>

The doppler-env package automates the injection of Doppler secrets as environment variables into any Python application and works in the terminal, PyCharm, and Visual Studio Code.

The Doppler CLI provides the easiest method of injecting secrets into your application: ...

Sections: doppler-env, Motivation, Setup, Configuration, Issues

</details>

### genie.libs.parser

Genie libs Parser: Genie Parser Libraries

`pip install genie.libs.parser` · installs (wheel) · licence: Apache Software License · rank 9380 · last release 2026-11-03 · [PyPI](https://pypi.org/project/genie.libs.parser/)

<details><summary>README extract</summary>

Genie is both a library framework and a test harness that facilitates rapid
development, encourage re-usable and simplify writing test automation. Genie bundled with
the modular architecture of pyATS framework accelerates and simplifies test
automation leveraging all the perks of the Python programming language in an
object-orienting fashion. ...

Sections: Genie Parser Component, Parser Package, Requirements, Quick Start

</details>

### genie.libs.sdk

Genie libs sdk: Libraries containing all Triggers and Verifications

`pip install genie.libs.sdk` · installs (wheel) · licence: Apache Software License · rank 9428 · last release 2026-11-03 · [PyPI](https://pypi.org/project/genie.libs.sdk/)

<details><summary>README extract</summary>

Genie is both a library framework and a test harness that facilitates rapid
development, encourage re-usable and simplify writing test automation. Genie
bundled with the modular architecture of pyATS framework accelerates and
simplifies test automation leveraging all the perks of the Python programming
language in an object-orienting fashion. ...

Sections: Genie Libs Sdk Component, Ops Libs Package, Requirements, Quick Start

</details>

### genie.libs.ops

Genie libs Ops: Libraries to retrieve operational state of the topology

`pip install genie.libs.ops` · installs (wheel) · licence: Apache Software License · rank 9458 · last release 2026-11-03 · [PyPI](https://pypi.org/project/genie.libs.ops/)

<details><summary>README extract</summary>

Genie is both a library framework and a test harness that facilitates rapid
development, encourage re-usable and simplify writing test automation. Genie
bundled with the modular architecture of pyATS framework accelerates and
simplifies test automation leveraging all the perks of the Python programming
language in an object-orienting fashion. ...

Sections: Genie Libs Ops Component, Ops Libs Package, Requirements, Quick Start

</details>

### genie.libs.clean

Genie Library for device clean support

`pip install genie.libs.clean` · installs (wheel) · licence: Apache Software License · rank 9460 · last release 2026-11-03 · [PyPI](https://pypi.org/project/genie.libs.clean/)

<details><summary>README extract</summary>

Genie is both a library framework and a test harness that facilitates rapid
development, encourage re-usable and simplify writing test automation. Genie
bundled with the modular architecture of pyATS framework accelerates and
simplifies test automation leveraging all the perks of the Python programming
language in an object-orienting fashion. ...

Sections: Genie Clean Component, Clean Package, Requirements, Quick Start

</details>

### genie.libs.conf

Genie libs Conf: Libraries to configures topology through Python object attributes

`pip install genie.libs.conf` · installs (wheel) · licence: Apache Software License · rank 9469 · last release 2026-11-03 · [PyPI](https://pypi.org/project/genie.libs.conf/)

<details><summary>README extract</summary>

Genie is both a library framework and a test harness that facilitates rapid
development, encourage re-usable and simplify writing test automation. Genie
bundled with the modular architecture of pyATS framework accelerates and
simplifies test automation leveraging all the perks of the Python programming
language in an object-orienting fashion. ...

Sections: Genie Libs Conf Component, Conf Libs Package, Requirements, Quick Start

</details>

### genie.libs.filetransferutils

Genie libs FileTransferUtils: Genie FileTransferUtils Libraries

`pip install genie.libs.filetransferutils` · installs (wheel) · licence: Apache Software License · rank 9496 · last release 2026-11-03 · [PyPI](https://pypi.org/project/genie.libs.filetransferutils/)

<details><summary>README extract</summary>

Genie is both a library framework and a test harness that facilitates rapid
development, encourage re-usable and simplify writing test automation. Genie bundled with
the modular architecture of pyATS framework accelerates and simplifies test
automation leveraging all the perks of the Python programming language in an
object-orienting fashion. ...

Sections: Genie FileTransferUtils libs Component, FileTransferUtils Package, Requirements, Quick Start

</details>

### genie.libs.health

pyATS Health Check for monitoring device health status

`pip install genie.libs.health` · installs (wheel) · licence: Apache Software License · rank 9504 · last release 2026-11-03 · [PyPI](https://pypi.org/project/genie.libs.health/)

<details><summary>README extract</summary>

Genie is both a library framework and a test harness that facilitates rapid
development, encourage re-usable and simplify writing test automation. Genie
bundled with the modular architecture of pyATS framework accelerates and
simplifies test automation leveraging all the perks of the Python programming
language in an object-orienting fashion. ...

Sections: pyATS Health Component, Health Package, Requirements, Quick Start

</details>

### rest.connector

pyATS REST connection package

`pip install rest.connector` · installs (wheel) · licence: Apache Software License · rank 9545 · last release 2026-11-03 · [PyPI](https://pypi.org/project/rest.connector/)

### sphinx-markdown-tables

A Sphinx extension for rendering tables written in markdown

`pip install sphinx-markdown-tables` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 9743 · last release 2022-07-29 · [PyPI](https://pypi.org/project/sphinx-markdown-tables/) · [source](https://github.com/ryanfox/sphinx-markdown-tables/)

_README extract left out: share-alike licence._

### pdm-pep517

A PEP 517 backend for PDM that supports PEP 621 metadata

`pip install pdm-pep517` · installs (wheel) · licence: MIT · rank 9814 · last release 2023-04-12 · [PyPI](https://pypi.org/project/pdm-pep517/) · [source](https://github.com/pdm-project/pdm-pep517)

<details><summary>README extract</summary>

This project has been renamed and re-published as pdm-backend

Yet another PEP 517 backend.

This is the backend for PDM projects, while you can also use it alone.
It reads the metadata of PEP 621 format and coverts it to Core metadata.

Edit your `pyproject.toml` as follows:

Example:
```python
def build(src, dst):
    with open(os.path.join(dst, "myfile.txt"), "w") as f:
        # Put a file in the wheel
        f.write("Hello World!")
```

Sections: PDM-PEP517, Use as PEP 517 build backend, Tool specific settings, Dynamic project version, Writing SCM version to file, Custom Build Script

</details>

### hatch-mypyc

Hatch build hook plugin for Mypyc

`pip install hatch-mypyc` · installs (wheel) · licence: MIT License · rank 9938 · last release 2023-02-23 · [PyPI](https://pypi.org/project/hatch-mypyc/) · [source](https://github.com/ofek/hatch-mypyc)

<details><summary>README extract</summary>

| | |

| CI/CD | |
| Package | |
| Meta | |

This provides a build hook plugin for Hatch that compiles code with Mypyc.

Table of Contents

- Configuration
 - File selection
 - Mypy arguments
 - Options
- Missing types
- License

The build hook plugin name is `mypyc`.

- *pyproject.toml*

- *hatch.toml*

Sections: hatch-mypyc, Configuration, File selection, Mypy arguments, Options, Missing types

</details>

### cx-Freeze

Create standalone executables from Python scripts

`pip install cx-Freeze` · installs (wheel) · licence: PSF-2.0 · rank 10033 · last release 2026-10-27 · [PyPI](https://pypi.org/project/cx-Freeze/) · [docs](https://cx-freeze.readthedocs.io) · [source](https://github.com/marcelotduarte/cx_Freeze)

<details><summary>README extract</summary>

cx_Freeze Creates standalone executables from Python scripts with the same performance
as the original script.

It is cross-platform and should work on any platform that Python runs on.

</details>

### uipath-mcp

UiPath MCP SDK

`pip install uipath-mcp` · installs (wheel) · licence: not stated · rank 10137 · last release 2026-10-21 · [PyPI](https://pypi.org/project/uipath-mcp/) · [source](https://github.com/UiPath/uipath-mcp-python)

<details><summary>README extract</summary>

A Python SDK that enables hosting local MCP servers on UiPath Platform.

Check out our samples directory to explore various MCP server implementations. You can also learn how to pack and host binary servers written in languages like Go within UiPath.

Sections: UiPath MCP Python SDK, Configuration, Servers Definition, Command Line Interface (CLI), Authentication, Initialize a Project, Debug a Project, Package a Project, Publish a Package, Project Structure

</details>

### modulegraph2

A module import dependency graph for Python projects.

`pip install modulegraph2` · installs (wheel) · licence: MIT License · rank 10200 · last release 2025-11-23 · [PyPI](https://pypi.org/project/modulegraph2/) · [docs](https://modulegraph2.readthedocs.io/) · [source](https://github.com/ronaldoussoren/modulegraph2/)

<details><summary>README extract</summary>

Modulegraph2 is a library for creating and introspecting
the dependency graph between Python modules. The graph is
created using static analisys from source and byte code.

The dependency graph contains information about packages,
modules, extensions and their dependencies. ...

</details>

### setupmeta

Simplify your setup.py

`pip install setupmeta` · installs (wheel) · licence: MIT · rank 10201 · last release 2026-10-27 · [PyPI](https://pypi.org/project/setupmeta/)

<details><summary>README extract</summary>

setupmeta derives your project's version from git tags, bumps it for you, and fills in the
rest of your `setup.py` metadata from the files your project already has.
A complete, ready to publish `setup.py` can look like this:
Run `python setup.py explain` to see every setting setupmeta determined, along with the
file and line each value came from. ...

Example:
```python
from setuptools import setup

setup(
    name="myproject",
    versioning="distance",      # Optional: activates git-tag-based versioning
    setup_requires="setupmeta",  # This is what activates setupmeta
)
```

Sections: Simplify your setup.py, Versioning, Bumping, Custom formats, Environment, Auto-filled metadata, Requirements, Commands

</details>

### conda-pack

Package conda environments for redistribution

`pip install conda-pack` · installs (wheel) · licence: BSD-3-Clause · rank 10240 · last release 2026-06-16 · [PyPI](https://pypi.org/project/conda-pack/) · [docs](https://conda.github.io/conda-pack/) · [source](https://github.com/conda/conda-pack)

<details><summary>README extract</summary>

`conda-pack` is a command line tool for creating relocatable conda
environments. This is useful for deploying code in a consistent environment,
potentially in locations where python or conda isn't already installed.

See the documentation
for more information.

Conda-pack is offered under a New BSD license; see the
license file.

</details>

### pyion2json

Convert an Amazon Ion document(s) to JSON

`pip install pyion2json` · installs from source (sdist only) · licence: MIT License · rank 10263 · last release 2020-03-13 · [PyPI](https://pypi.org/project/pyion2json/)

<details><summary>README extract</summary>

Convert an Amazon Ion document(s) to JSON

Example:
```python
import json
import amazon.ion.simpleion as ion
from pyion2json import ion_to_json

ion_doc = ion.loads('{ first: "Tom" , last: "Riddle" }')
json_doc = ion_to_json(ion_doc)
print(json.dumps(json_doc, indent=' '))
```

Sections: pyion2json, Usage, Convert individual Ion values, Convert a cursor from QLDB, TODO

</details>

### xclienttransaction

Twitter X-Client-Transaction-Id generator written in python.

`pip install xclienttransaction` · installs (wheel) · licence: MIT License · rank 10266 · last release 2026-06-26 · [PyPI](https://pypi.org/project/xclienttransaction/)

<details><summary>README extract</summary>

Twitter X-Client-Transaction-Id generator written in python.

Reference :

- Twitter Header: Part 1, Deobfuscation
- Twitter Header: Part 2, Reverse Engineering
- Twitter Header: Part 3, Generating the header

Example:
```python
import bs4
import requests
from x_client_transaction.utils import generate_headers, handle_x_migration, get_ondemand_file_url

# INITIALIZE SESSION
session = requests.Session()
session.headers = generate_headers()

# GET HOME PAGE RESPONSE
# required only when hitting twitter.com but not x.com
# returns bs4.BeautifulSoup object
...
```

Sections: X-Client-Transaction-ID, Usage/Examples, Get x.com Home Page and ondemand.s File Response, Synchronous Version, Async Version, Generate X-Client-Transaction-Id (tid), Feedback

</details>

### colcon-core

Command line tool to build sets of software packages.

`pip install colcon-core` · installs (wheel) · licence: Apache-2.0 · rank 10348 · last release 2026-09-17 · [PyPI](https://pypi.org/project/colcon-core/) · [source](https://github.com/colcon/colcon-core/)

<details><summary>README extract</summary>

`colcon` is a command line tool to improve the workflow of building, testing and using multiple software packages.
It automates the process, handles the ordering and sets up the environment to use the packages.

For more information see colcon.readthedocs.io.

</details>

### keepachangelog

Manipulate keep a changelog files

`pip install keepachangelog` · installs (wheel) · licence: MIT License · rank 10440 · last release 2024-06-14 · [PyPI](https://pypi.org/project/keepachangelog/) · [docs](https://colin-b.github.io/keepachangelog/) · [source](https://github.com/Colin-b/keepachangelog)

<details><summary>README extract</summary>

Example:
```python
import keepachangelog

changes = keepachangelog.to_raw_dict("path/to/CHANGELOG.md")
```

Sections: Retrieving the raw content, Using CLI, Using python module, Usage from command line, Endpoint, Starlette, Flask-RestX

</details>

### dbt-osmosis

A dbt utility for managing YAML to make developing with dbt more delightful.

`pip install dbt-osmosis` · does not install on CPython 3.14 · licence: Apache Software License · rank 10599 · last release 2026-07-05 · [PyPI](https://pypi.org/project/dbt-osmosis/)

<details><summary>README extract</summary>

`dbt-osmosis` is a Python CLI and package for dbt development workflows.

It centers on four primary surfaces:

- schema YAML management (`yaml organize`, `yaml document`, `yaml refactor`)
- column-level documentation inheritance across dbt lineage
- ad-hoc SQL compile/run helpers ...

Sections: dbt-osmosis, Quick start, CLI surface, Workbench, Pre-commit hook

</details>

### cognite-toolkit

Official Cognite Data Fusion tool for project templates and configuration deployment

`pip install cognite-toolkit` · installs (wheel) · licence: Apache-2.0 · rank 10754 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cognite-toolkit/) · [docs](https://docs.cognite.com/cdf/deploy/cdf_toolkit/references/resource_library) · [source](https://github.com/cognitedata/toolkit)

<details><summary>README extract</summary>

The CDF Toolkit is a command-line interface (`cdf`) used for configuring and administrating
Cognite Data Fusion (CDF) projects. It ships with modularised `templates` that helps you
configure Cognite Data Fusion according to best practices.

It supports three different modes of operation:

1. ...

Sections: Cognite Data Fusion Toolkit, Usage, For more information

</details>

### keynote-parser

A tool for manipulating Apple Keynote presentation files.

`pip install keynote-parser` · installs (wheel) · licence: MIT License · rank 10843 · last release 2026-08-08 · [PyPI](https://pypi.org/project/keynote-parser/) · [source](https://github.com/psobot/keynote-parser/)

<details><summary>README extract</summary>

`keynote-parser` is a Python module for unpacking and re-packing
Apple Keynote `.key` files. It supports Keynote
files generated by Keynote version 14.4 (current as of April 2025).

Keynote uses a proprietary, compressed binary format to store its presentations. ...

Sections: keynote-parser, Usage, Formats, Replacing Images, Compatibility, Updates, Rebuilding the generated code, Troubleshooting

</details>

### colcon-cmake

Extension for colcon to support CMake packages.

`pip install colcon-cmake` · installs (wheel) · licence: Apache-2.0 · rank 10939 · last release 2026-06-16 · [PyPI](https://pypi.org/project/colcon-cmake/) · [source](https://github.com/colcon/colcon-cmake/)

<details><summary>README extract</summary>

An extension for colcon-core to support CMake projects.

</details>

### pycstruct

Binary data handling in Python using dictionaries

`pip install pycstruct` · installs (wheel) · licence: MIT License · rank 10951 · last release 2024-03-24 · [PyPI](https://pypi.org/project/pycstruct/) · [docs](https://pycstruct.readthedocs.io/en/latest/) · [source](https://github.com/midstar/pycstruct)

<details><summary>README extract</summary>

pycstruct is a python library for converting binary data to and from ordinary
python dictionaries or specific instance objects.

Data is defined similar to what is done in C language structs, unions,
bitfields and enums.

Typical usage of this library is read/write binary files or binary data
transmitted over a network. ...

Example:
```python
import pycstruct

person = pycstruct.StructDef()
person.add('utf-8', 'name', length=50)
person.add('uint32', 'age')
person.add('float32','height')
person.add('bool8', 'is_male')
person.add('uint32', 'nbr_of_children')
person.add('uint32', 'child_ages', length=10)

with open('simple_example.dat', 'rb') as f:
    inbytes = f.read()

...
```

Sections: pycstruct, Example, Parsing source files, Full documentation

</details>

### aegra-cli

Aegra CLI - Manage your self-hosted agent deployments

`pip install aegra-cli` · installs (wheel) · licence: Apache-2.0 · rank 10959 · last release 2026-10-23 · [PyPI](https://pypi.org/project/aegra-cli/)

<details><summary>README extract</summary>

Aegra CLI - Command-line interface for managing self-hosted agent deployments.

Aegra is an open-source, self-hosted alternative to LangSmith Deployments. Use this CLI to initialize projects, run development servers, and manage Docker services.

Sections: aegra-cli, From PyPI, From Source, Quick Start, Commands, `aegra version`, `aegra init`, `aegra dev`, `aegra serve`, `aegra up`, `aegra down`, Environment Variables, Requirements, Related Packages

</details>

### colcon-ros

Extension for colcon to support ROS packages.

`pip install colcon-ros` · installs (wheel) · licence: Apache Software License · rank 10997 · last release 2024-06-24 · [PyPI](https://pypi.org/project/colcon-ros/) · [source](https://github.com/colcon/colcon-ros/)

<details><summary>README extract</summary>

An extension for colcon-core to support ROS packages.

</details>

### colcon-python-setup-py

Extension for colcon to support Python packages with the metadata in the setup.py file.

`pip install colcon-python-setup-py` · installs (wheel) · licence: Apache Software License · rank 11006 · last release 2024-10-08 · [PyPI](https://pypi.org/project/colcon-python-setup-py/) · [source](https://github.com/colcon/colcon-python-setup-py/)

<details><summary>README extract</summary>

An extension for colcon-core to identify packages with a `setup.py` file by introspecting the arguments to the `setup()` function call of setuptools.

</details>

### colcon-test-result

Extension for colcon to provide information about the test results.

`pip install colcon-test-result` · installs (wheel) · licence: Apache Software License · rank 11012 · last release 2019-10-01 · [PyPI](https://pypi.org/project/colcon-test-result/) · [source](https://github.com/colcon/colcon-test-result/)

<details><summary>README extract</summary>

An extension for colcon-core to provide information about the test results.

</details>

### colcon-library-path

Extension for colcon adding an environment variable to find libraries.

`pip install colcon-library-path` · installs (wheel) · licence: Apache Software License · rank 11019 · last release 2019-01-16 · [PyPI](https://pypi.org/project/colcon-library-path/) · [source](https://github.com/colcon/colcon-library-path/)

<details><summary>README extract</summary>

An extension for colcon-core to set an environment variable to find shared libraries at runtime.

</details>

### colcon-recursive-crawl

Extension for colcon to recursively crawl for packages.

`pip install colcon-recursive-crawl` · installs (wheel) · licence: Apache Software License · rank 11023 · last release 2023-10-05 · [PyPI](https://pypi.org/project/colcon-recursive-crawl/) · [source](https://github.com/colcon/colcon-recursive-crawl/)

<details><summary>README extract</summary>

An extension for colcon-core to recursively crawl for packages.

</details>

### colcon-pkg-config

Extension for colcon adding an environment variable to find pkg-config files.

`pip install colcon-pkg-config` · installs (wheel) · licence: Apache Software License · rank 11048 · last release 2018-06-28 · [PyPI](https://pypi.org/project/colcon-pkg-config/) · [source](https://github.com/colcon/colcon-pkg-config/)

<details><summary>README extract</summary>

An extension for colcon-core to set an environment variable to find pkg-config files.

</details>

### ctypesgen

Python wrapper generator for ctypes

`pip install ctypesgen` · installs (wheel) · licence: BSD License · rank 11068 · last release 2022-10-19 · [PyPI](https://pypi.org/project/ctypesgen/)

<details><summary>README extract</summary>

ctypesgen

 (c) Ctypesgen developers 2007-2022

_ctypesgen_ is a pure-python ctypes wrapper generator. It parses C header files
and creates a wrapper for libraries based on what it finds.

Preprocessor macros are handled in a manner consistent with typical C code. ...

Sections: Documentation, Basic Usage, Related Software of Interest, v1.1.1, v1.1.0, v1.0.2, v1.0.1, v1.0.0

</details>

### panflute

Pythonic Pandoc filters

`pip install panflute` · installs (wheel) · licence: BSD License · rank 11074 · last release 2024-03-20 · [PyPI](https://pypi.org/project/panflute/) · [docs](http://scorreia.com/software/panflute/) · [source](https://github.com/sergiocorreia/panflute)

<details><summary>README extract</summary>

panflute is a Python package that makes creating Pandoc filters fun.

For a detailed user guide, documentation, and installation instructions, see
For examples that you can use as starting points, check the examples repo, the sample template, or this github search.
If you want to contribute, head here. ...

Sections: Panflute: Pythonic Pandoc Filters, Pip, Conda, Note on versions

</details>

### pytest-parametrization

Simpler PyTest parametrization

`pip install pytest-parametrization` · installs from source (sdist only) · licence: MIT License · rank 11082 · last release 2022-05-22 · [PyPI](https://pypi.org/project/pytest-parametrization/)

<details><summary>README extract</summary>

Simpler PyTest parametrization

Example:
```python
from parametrization import Parametrization

@Parametrization.parameters("actual", "expected")
@Parametrization.case(name="some_case_0", actual=1, expected=2)
@Parametrization.case("some_case_1", actual=1, expected=2)
@Parametrization.case("some_case_2", 1, expected=1)
@Parametrization.case("some_case_3", 2, 2)
...
```

Sections: pytest-parametrization, How to use, Explicit parameters, Auto-detect parameters, Auto-detect parameters with default parameter, Generate name based on arguments

</details>

### ouroboros-ai

Pins an acceptance spec and omits any verify command or expected output from the worker's contract. Works with Claude Code, Codex CLI, OpenCode and 10 more runtimes.

`pip install ouroboros-ai` · installs (wheel) · licence: MIT License · rank 11083 · last release 2026-10-25 · [PyPI](https://pypi.org/project/ouroboros-ai/) · [source](https://github.com/Q00/ouroboros)

<details><summary>README extract</summary>

English | 한국어 | 简体中文

 ◯ ─────────── ◯

 O U R O B O R O S

 ◯ ─────────── ◯

 It gets smarter on its own. We just hold the line.

 Skip the prompt engineering. The agent runs, fails, and gets smarter every generation. The grading command and expected result never make it into the success contract we hand it. ...

Features:
Most AI coding fails at the input, not the output. The bottleneck is not AI capability -- it is human clarity.

| Problem | What Happens | Ouroboros Fix | ...

Example:
```python
Ralph Cycle 1: evolve_step(lineage, seed) -> Gen 1 -> action=CONTINUE
Ralph Cycle 2: evolve_step(lineage)       -> Gen 2 -> action=CONTINUE
Ralph Cycle 3: evolve_step(lineage)       -> Gen 3 -> action=CONVERGED
                                                +-- Ralph stops.
...
```

...

</details>

### django-naomi

Email backend for Django. Preview your email in browser instead of sending it.

`pip install django-naomi` · installs (wheel) · licence: MIT License · rank 11121 · last release 2015-08-15 · [PyPI](https://pypi.org/project/django-naomi/)

<details><summary>README extract</summary>

Django-naomi is a email backend for Django that let you preview email from your web browser instead of sending it using SMTP server. This is perfect for development environment that lack of SMTP server or you want to debug the email message. Attachment will be shown as link. This library is inspired from Letter Opener. ...

Sections: django-naomi, Django Setup

</details>

### freeze-core

Core dependency for cx_Freeze

`pip install freeze-core` · installs (wheel) · licence: MIT · rank 11322 · last release 2026-10-23 · [PyPI](https://pypi.org/project/freeze-core/) · [docs](https://cx-freeze.readthedocs.io) · [source](https://github.com/marcelotduarte/freeze-core)

<details><summary>README extract</summary>

Core dependency for cx_Freeze.

Sections: freeze-core, Building redistributable binary wheels, See also

</details>

### colcon-output

Extension for colcon to customize the output in various ways.

`pip install colcon-output` · installs (wheel) · licence: Apache-2.0 · rank 11391 · last release 2026-09-17 · [PyPI](https://pypi.org/project/colcon-output/) · [source](https://github.com/colcon/colcon-output/)

<details><summary>README extract</summary>

An extension for colcon-core to customize the output in various ways.

</details>

### genie.telemetry

Genie libs Telemetry: Genie Telemetry Libraries

`pip install genie.telemetry` · installs (wheel) · licence: Apache Software License · rank 11466 · last release 2026-11-03 · [PyPI](https://pypi.org/project/genie.telemetry/)

<details><summary>README extract</summary>

Genie Telemetry is a testbed Health Status Monitoring Tool. It is a package
within pyATS.

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. ...

Sections: Genie Telemetry Component, Telemetry Package, Requirements, Quick Start

</details>

### junit-xml-2

Fork of https://github.com/kyrus/python-junit-xml that has tarball published to pypi

`pip install junit-xml-2` · installs (wheel) · licence: Freely Distributable; MIT License · rank 11482 · last release 2020-09-30 · [PyPI](https://pypi.org/project/junit-xml-2/)

<details><summary>README extract</summary>

Fork of to publish on pypi as tarball so
 can rely on this as a pypi package

</details>

### genie.libs.robot

Genie libs Robot: RobotFramework libraries to interact with Genie

`pip install genie.libs.robot` · installs (wheel) · licence: Apache Software License · rank 11548 · last release 2026-11-03 · [PyPI](https://pypi.org/project/genie.libs.robot/)

<details><summary>README extract</summary>

Genie is both a library framework and a test harness that facilitates rapid
development, encourage re-usable and simplify writing test automation. Genie
bundled with the modular architecture of pyATS framework accelerates and
simplifies test automation leveraging all the perks of the Python programming
language in an object-orienting fashion. ...

Sections: Genie Libs Robot Component, Ops Libs Package, Requirements, Quick Start

</details>

### genie.trafficgen

Genie Library for traffic generator connection support

`pip install genie.trafficgen` · installs (wheel) · licence: Apache Software License · rank 11560 · last release 2026-11-03 · [PyPI](https://pypi.org/project/genie.trafficgen/)

<details><summary>README extract</summary>

Genie is both a library framework and a test harness that facilitates rapid
development, encourage re-usable and simplify writing test automation. Genie
bundled with the modular architecture of pyATS framework accelerates and
simplifies test automation leveraging all the perks of the Python programming
language in an object-orienting fashion. ...

Sections: Genie Traffic Component, Traffic Package, Requirements, Quick Start

</details>

### pyats.contrib

Open source package for pyATS framework extensions.

`pip install pyats.contrib` · installs (wheel) · licence: Apache Software License · rank 11573 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.contrib/)

<details><summary>README extract</summary>

Sections: General Information, Solution Documentation

</details>

### authorizenet

Authorize.Net Python SDK

`pip install authorizenet` · installs from source (sdist only) · licence: Other/Proprietary License · rank 11575 · last release 2025-04-28 · [PyPI](https://pypi.org/project/authorizenet/)

<details><summary>README extract</summary>

Example:
```python
merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = 'YOUR_API_LOGIN_ID'
merchantAuth.transactionKey = 'YOUR_TRANSACTION_KEY'
```

Sections: Requirements, TLS 1.2, Registration & Configuration, Authentication, To set your API credentials for an API request, Enable Logging in the SDK, SDK Usage Examples and Sample Code, Create a Chase Pay Transaction, Transaction Hash Upgrade

</details>

### pyats.robot

pyATS Robot: Robot Module

`pip install pyats.robot` · installs (wheel) · licence: Apache Software License · rank 11581 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyats.robot/)

<details><summary>README extract</summary>

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites. ...

Sections: pyATS Robot Component, Robot Package, Requirements, Quick Start

</details>

### compiledb

Tool for generating Clang JSON Compilation Database files for make-based build systems.

`pip install compiledb` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 11820 · last release 2025-03-23 · [PyPI](https://pypi.org/project/compiledb/) · [source](https://github.com/nickdiego/compiledb.git)

_README extract left out: share-alike licence._

### openssl-ocsp-responder

Simple wrapper for OpenSSL OCSP server

`pip install openssl-ocsp-responder` · installs from source (sdist only) · licence: MIT License · rank 11857 · last release 2021-12-30 · [PyPI](https://pypi.org/project/openssl-ocsp-responder/)

### colcon-bash

Extension for colcon to provide Bash scripts.

`pip install colcon-bash` · installs (wheel) · licence: Apache Software License · rank 11922 · last release 2023-09-25 · [PyPI](https://pypi.org/project/colcon-bash/) · [source](https://github.com/colcon/colcon-bash/)

<details><summary>README extract</summary>

An extension for colcon-core to provide Bash scripts.

</details>

### colcon-package-selection

Extension for colcon to select the packages to process.

`pip install colcon-package-selection` · installs (wheel) · licence: Apache Software License · rank 11974 · last release 2020-10-06 · [PyPI](https://pypi.org/project/colcon-package-selection/) · [source](https://github.com/colcon/colcon-package-selection/)

<details><summary>README extract</summary>

An extension for colcon-core to select a subset of packages for processing.

</details>

### colcon-zsh

Extension for colcon to provide Z shell scripts.

`pip install colcon-zsh` · installs (wheel) · licence: Apache Software License · rank 11977 · last release 2023-10-06 · [PyPI](https://pypi.org/project/colcon-zsh/) · [source](https://github.com/colcon/colcon-zsh/)

<details><summary>README extract</summary>

An extension for colcon-core to provide Z shell scripts.

</details>

### colcon-package-information

Extension for colcon to output package information.

`pip install colcon-package-information` · installs (wheel) · licence: Apache-2.0 · rank 11979 · last release 2026-03-27 · [PyPI](https://pypi.org/project/colcon-package-information/) · [source](https://github.com/colcon/colcon-package-information/)

<details><summary>README extract</summary>

An extension for colcon-core to provide information about the packages.

</details>

### colcon-defaults

Extension for colcon to read defaults from a config file.

`pip install colcon-defaults` · installs (wheel) · licence: Apache Software License · rank 11993 · last release 2024-12-18 · [PyPI](https://pypi.org/project/colcon-defaults/) · [source](https://github.com/colcon/colcon-defaults/)

<details><summary>README extract</summary>

An extension for colcon-core to provide custom default values for the command line arguments from a configuration file.

For more information about the format of the configuration file see colcon.readthedocs.io.

</details>

### colcon-notification

Extension for colcon to provide status notifications.

`pip install colcon-notification` · installs (wheel) · licence: Apache-2.0 · rank 12028 · last release 2026-09-17 · [PyPI](https://pypi.org/project/colcon-notification/) · [source](https://github.com/colcon/colcon-notification/)

<details><summary>README extract</summary>

An extension for colcon-core to provide status notifications.

</details>

### azdev

Microsoft Azure CLI Developer Tools

`pip install azdev` · installs (wheel) · licence: MIT · rank 12065 · last release 2026-11-04 · [PyPI](https://pypi.org/project/azdev/)

<details><summary>README extract</summary>

The `azdev` tool is designed to aid new and experienced developers in contributing to Azure CLI command modules and extensions.

Notes: `azdev` command line tool is only designed for internal use and running on a local machine. It should never be used to take input from untrusted/outside sources or used behind another application.

Sections: Microsoft Azure CLI Dev Tools (azdev), Latest packaged indices, Common azdev commands, Reporting issues and feedback, 0.2.14, 0.2.13, 0.2.12, 0.2.12b3, 0.2.12b2, 0.2.12b1, 0.2.11, 0.2.10, 0.2.9, 0.2.8

</details>

### colcon-metadata

Extension for colcon to read package metadata from files.

`pip install colcon-metadata` · installs (wheel) · licence: Apache-2.0 · rank 12094 · last release 2026-09-13 · [PyPI](https://pypi.org/project/colcon-metadata/) · [source](https://github.com/colcon/colcon-metadata/)

<details><summary>README extract</summary>

An extension for colcon-core to fetch and manage package metadata from repositories.

For an example repository containing metadata see colcon-metadata-repository.

</details>

### colcon-common-extensions

Meta package aggregating colcon-core and common extensions.

`pip install colcon-common-extensions` · installs (wheel) · licence: Apache Software License · rank 12099 · last release 2022-08-31 · [PyPI](https://pypi.org/project/colcon-common-extensions/) · [source](https://github.com/colcon/colcon-common-extensions/)

<details><summary>README extract</summary>

A meta package aggregating colcon-core as well as a set of common extensions.

</details>

### colcon-parallel-executor

Extension for colcon to process packages in parallel.

`pip install colcon-parallel-executor` · installs (wheel) · licence: Apache Software License · rank 12105 · last release 2025-08-13 · [PyPI](https://pypi.org/project/colcon-parallel-executor/) · [source](https://github.com/colcon/colcon-parallel-executor/)

<details><summary>README extract</summary>

An extension for colcon-core to process packages in parallel.

</details>

### buildozer

Turns Python applications into binary packages ready for installation on a number of platforms.

`pip install buildozer` · installs (wheel) · licence: MIT · rank 12107 · last release 2026-05-12 · [PyPI](https://pypi.org/project/buildozer/) · [docs](https://buildozer.readthedocs.io/en/stable/#) · [source](https://github.com/kivy/buildozer)

<details><summary>README extract</summary>

Buildozer is a development tool for turning Python
applications into binary packages ready for installation on any of a number of
platforms, including mobile devices.

The app developer provides a single "buildozer.spec" file, which describes the
application's requirements and settings, such as title and icons. ...

Sections: Buildozer, Buildozer Docker image, Example Build with Caching, Buildozer GitHub action, Usage, Examples of Buildozer commands, `buildozer.spec`, Default config, Documentation, Backers, 1.6.0 (2026-05-11), 1.5.0, 1.4.0 (2022-07-20), 1.3.0 (2022-03-13)

</details>

### pyrig

A Python project setup and management tool built on infrastructure as code and convention over configuration.

`pip install pyrig` · installs (wheel) · licence: MIT · rank 12117 · last release 2026-11-08 · [PyPI](https://pypi.org/project/pyrig/) · [docs](https://Winipedia.github.io/pyrig) · [source](https://github.com/Winipedia/pyrig)

<details><summary>README extract</summary>

<!-- project-status -->

<!-- code-quality -->

<!-- tooling -->

<!-- project-info -->

<!-- rumdl-disable MD013 -->

> A Python project setup and management tool built on infrastructure as code and convention over configuration.

<!-- rumdl-enable MD013 --> ...

Sections: pyrig, What is pyrig?, Requirements, Quick Start, Features, Project Scaffolding & Initialization, File & Configuration Management, Automatic CLI, Mirror Test Structure, Plugin Architecture, CI/CD & Repository Protection, Commands, Comparisons, Documentation

</details>

### colcon-powershell

Extension for colcon to provide PowerShell scripts.

`pip install colcon-powershell` · installs (wheel) · licence: Apache-2.0 · rank 12126 · last release 2026-02-10 · [PyPI](https://pypi.org/project/colcon-powershell/) · [source](https://github.com/colcon/colcon-powershell/)

<details><summary>README extract</summary>

An extension for colcon-core to provide PowerShell scripts.

</details>

### colcon-devtools

Extension for colcon to provide information about all extension points and extensions

`pip install colcon-devtools` · installs (wheel) · licence: Apache Software License · rank 12138 · last release 2024-03-13 · [PyPI](https://pypi.org/project/colcon-devtools/) · [source](https://github.com/colcon/colcon-devtools/)

<details><summary>README extract</summary>

An extension for colcon-core to provide information about the plugin system.

</details>

### import-ipynb

Imports A.ipynb into B.ipynb

`pip install import-ipynb` · installs (wheel) · licence: BSD License · rank 12192 · last release 2026-08-14 · [PyPI](https://pypi.org/project/import-ipynb/)

<details><summary>README extract</summary>

Suppose you want to import the contents of A.ipynb into B.ipynb.

Example:
```python
import import_ipynb
import A
```

Sections: Motivation, How to use, How it works

</details>

### ipfn

Iterative Proportional Fitting with N dimensions, for python

`pip install ipfn` · installs (wheel) · licence: MIT License · rank 12277 · last release 2021-12-30 · [PyPI](https://pypi.org/project/ipfn/)

<details><summary>README extract</summary>

Iterative proportional fitting is an algorithm used is many different fields such as economics or social sciences, to alter results in such a way that aggregates along one or several dimensions match known marginals (or aggregates along these same dimensions).

The algorithm exists in 2 versions: ...

Example:
```python
import numpy as np
from ipfn import ipfn

m = [[40, 30, 20, 10], [35, 50, 100, 75], [30, 80, 70, 120], [20, 30, 40, 50]]
m = np.array(m)
xip = np.array([150, 300, 400, 150])
xpj = np.array([200, 300, 400, 100])

aggregates = [xip, xpj]
dimensions = [[0], [1]]

IPF = ipfn.ipfn(m, aggregates, dimensions, convergence_rate=1e-6)
m = IPF.iteration()
...
```

...

</details>

### code-coordinator

Coordinate Claude Code workers across multiple machines and repos.

`pip install code-coordinator` · installs (wheel) · licence: LicenseRef-FSL-1.1-MIT · rank 12345 · last release 2026-11-08 · [PyPI](https://pypi.org/project/code-coordinator/) · [source](https://github.com/JDonaghy/claude-coordinator)

<details><summary>README extract</summary>

A harness for running Claude Code on real projects, mostly unattended.

I built this tool to help me develop vimcode, and later
quadraui, with Claude Code doing most of the work. ...

Features:
- You are still the tech lead. It doesn't decide what's worth building, and it escalates
 rather than guesses when a gate is ambiguous. Expect to spend your time on triage and design,
 not watching sessions.
- It still drops things. ...

Sections: code-coordinator, Where it's gotten me to, The problems, and what it does about each, What it does not solve, How it works, The pipeline, Quick start, Minimal configuration, Adding machines, Requirements, Documentation

</details>

### logging-json

JSON formatter for python logging

`pip install logging-json` · installs (wheel) · licence: MIT License · rank 12499 · last release 2025-02-04 · [PyPI](https://pypi.org/project/logging-json/) · [docs](https://colin-b.github.io/logging_json/) · [source](https://github.com/Colin-b/logging_json)

<details><summary>README extract</summary>

This module provides a JSON formatter for the python `logging` module that will format to JSON formatted string.

Using this formatter allows to have the proper format for logging to `Splunk` or `ElasticSearch`, but it can also be used for logging to stdout as a string is issued.

- Features
 - Custom fields
 - dict logging
 - str logging ...

Example:
```python
import logging

logging.info({"key": "value", "other key": "other value"})
```

...

</details>

### rpm-vercmp

Pure Python implementation of rpmvercmp

`pip install rpm-vercmp` · installs from source (sdist only) · licence: Apache Software License · rank 12525 · last release 2018-10-30 · [PyPI](https://pypi.org/project/rpm-vercmp/)

<details><summary>README extract</summary>

Pure Python implementation of rpmvercmp.

The RPM Package Manager ( has a version comparision algorithm,
implemented in its C library, which performs the comparison in a certain way. ...

Sections: Source Code, Usage

</details>

### colcon-argcomplete

Completion for colcon command lines using argcomplete.

`pip install colcon-argcomplete` · installs (wheel) · licence: Apache Software License · rank 12579 · last release 2019-07-16 · [PyPI](https://pypi.org/project/colcon-argcomplete/) · [source](https://github.com/colcon/colcon-argcomplete/)

<details><summary>README extract</summary>

An extension for colcon-core to provide command line completion using argcomplete.

</details>

### colcon-cd

A shell function for colcon to change the current working directory.

`pip install colcon-cd` · installs (wheel) · licence: Apache Software License · rank 12582 · last release 2019-10-21 · [PyPI](https://pypi.org/project/colcon-cd/) · [source](https://github.com/colcon/colcon-cd/)

<details><summary>README extract</summary>

A shell function for colcon-core to change the current working directory.

</details>

### hashin

Edits your requirements.txt by hashing them in

`pip install hashin` · installs (wheel) · licence: MIT · rank 12677 · last release 2025-06-12 · [PyPI](https://pypi.org/project/hashin/)

<details><summary>README extract</summary>

Helps you write your `requirements.txt` with hashes so you can
install with `pip install --require-hashes -r ...`

If you want to add a package or edit the version of one you're currently
using you have to do the following steps:

1. Go to pypi for that package
2. Download the `.tgz` file
3. Possibly download the `.whl` file
4. ...

Example:
```python
import hashin
from pprint import pprint
pprint(hashin.get_package_hashes('Django'))
```

Sections: hashin, A Word of Warning!, How to use it, Dry run mode, PEP-0496 Environment Markers, Using as a Python library, Running tests, Running tests with test coverage, Debugging, Code Style, Future

</details>

### python-codicefiscale

encode / decode italian fiscal codes - codifica / decodifica del Codice Fiscale italiano.

`pip install python-codicefiscale` · installs (wheel) · licence: MIT License · rank 12732 · last release 2026-05-08 · [PyPI](https://pypi.org/project/python-codicefiscale/) · [docs](https://github.com/fabiocaccamo/python-codicefiscale#readme)

<details><summary>README extract</summary>

python-codicefiscale is a library for encode/decode Italian fiscal code - codifica/decodifica del Codice Fiscale.

Features:
- `NEW` Auto-updated data (once a week) directly from ANPR data-source.
- `NEW` Command Line Interface available.
- Transliteration for name/surname
- Multiple birthdate formats (date/string) *(you can see all the supported string formats here)* ...

Example:
```python
from codicefiscale import codicefiscale
```

Sections: python-codicefiscale, Features, Usage, Python, Import, Encode, Decode, Check, Command Line, Encode (CLI), Decode (CLI), See also

</details>

### pretrainedmodels

Pretrained models for Pytorch

`pip install pretrainedmodels` · installs from source (sdist only) · licence: MIT License · rank 12774 · last release 2018-10-29 · [PyPI](https://pypi.org/project/pretrainedmodels/)

<details><summary>README extract</summary>

The goal of this repo is:

- to help to reproduce research papers results (transfer learning setups for instance),
- to access pretrained ConvNets with a unique interface/API inspired by torchvision.

News:
- 27/10/2018: Fix compatibility issues, Add tests, Add travis
- 04/06/2018: PolyNet and PNASNet-5-Large thanks to Alex Parinov ...

Example:
```python
import pretrainedmodels
```

Sections: Pretrained models for Pytorch (Work in progress), Summary, Quick examples, Few use cases, Compute imagenet logits, Compute imagenet evaluation metrics, Evaluation on imagenet, Accuracy on validation set (single model), Reproducing results, Documentation, Available models, NASNet, FaceBook ResNet, Caffe ResNet

</details>

### python-msilib

Read and write Microsoft Installer files

`pip install python-msilib` · installs from source (sdist only) · licence: PSF-2.0 · rank 12814 · last release 2026-10-23 · [PyPI](https://pypi.org/project/python-msilib/) · [docs](https://docs.python.org/3.12/library/msilib.html) · [source](https://github.com/marcelotduarte/python-msilib)

<details><summary>README extract</summary>

Read and write Microsoft Installer files.

This library is legacy code borrowed from Python 3.12, intended to allow
cx_Freeze's `bdist_msi` command to continue working in Python 3.13+.

Sections: python-msilib, Documentation

</details>

### kas

Setup tool for bitbake based projects

`pip install kas` · installs (wheel) · licence: MIT License · rank 12879 · last release 2026-08-21 · [PyPI](https://pypi.org/project/kas/) · [docs](https://kas.readthedocs.io/) · [source](https://github.com/siemens/kas.git)

<details><summary>README extract</summary>

+--------------------+

+====================+
workflow-master
+--------------------+
workflow-next
+--------------------+

This tool provides an easy mechanism to setup bitbake based
projects.

The OpenEmbedded tooling support starts at step 2 with bitbake. The
downloading of sources and then configuration has to be done by
hand. ...

</details>

### pip-check-reqs

Find packages that should or should not be in requirements for a project

`pip install pip-check-reqs` · installs (wheel) · licence: MIT License · rank 12901 · last release 2026-09-08 · [PyPI](https://pypi.org/project/pip-check-reqs/)

<details><summary>README extract</summary>

It happens: you start using a module in your project and it works and you
don't realise that it's only being included in your virtualenv because
it's a dependency of a package you're using. pip-missing-reqs finds those
modules so you can include them in the requirements.txt for the project. ...

Example:
```python
try:
    import Levenshtein
except ImportError:
    Levenshtein = None
```

Sections: pip-check-reqs, Sample tox.ini configuration, Excluding test files (or others) from this check, Excluding modules from the check, Excluding requirements from the check, Checking transitive dependencies, Using pyproject.toml instead of requirements.txt, Comparison with deptry, With Thanks To

</details>

### veracode-api-py

Python helper library for working with the Veracode APIs. Handles retries, pagination, and other features of the modern Veracode REST APIs.

`pip install veracode-api-py` · installs (wheel) · licence: MIT License · rank 13018 · last release 2026-08-20 · [PyPI](https://pypi.org/project/veracode-api-py/)

<details><summary>README extract</summary>

Python helper library for working with the Veracode APIs. Handles retries, pagination, and other features of the modern Veracode REST APIs.

Not an official Veracode product. Heavily based on original work by CTCampbell.

Install from pypi:

 pip install veracode-api-py

Sections: Veracode API Python, Setup, Authenticating from a pipeline, Authenticating through a proxy, Use in your applications, Docs, Notes

</details>

### a2a

Finds corresponding service offerings in Microsoft Azure and Amazon AWS .

`pip install a2a` · installs from source (sdist only) · licence: MIT License · rank 13124 · last release 2020-08-04 · [PyPI](https://pypi.org/project/a2a/)

### buf-bin

Buf CLI distributed via PyPI

`pip install buf-bin` · installs (wheel) · licence: Apache-2.0 · rank 13233 · last release 2026-10-22 · [PyPI](https://pypi.org/project/buf-bin/) · [docs](https://buf.build/docs/cli/) · [source](https://github.com/bufbuild/buf)

<details><summary>README extract</summary>

[][badges_slack]

Buf is the modern toolchain for Protobuf. It replaces day-to-day `protoc` use with a fast compiler, module-aware workspaces, formatting, linting, breaking-change detection, code generation, dependency management, API calls, and a client for the Buf Schema Registry. ...

Features:
| Protobuf work | With `protoc` and scripts | With Buf |

| Finding files | Maintain `-I` paths and hope import order does not change behavior. | Declare modules once in `buf.yaml`; Buf discovers files and rejects ambiguous imports. ...

Sections: Buf, Start, Why Buf wins, Core workflow, Code generation, Breaking changes, Buf Schema Registry, Related projects, CLI stability, Documentation

</details>

### mongo-ninja-python

(no summary)

`pip install mongo-ninja-python` · installs (wheel) · licence: Apache Software License; BSD License · rank 13568 · last release 2023-12-13 · [PyPI](https://pypi.org/project/mongo-ninja-python/)

### styleframe

A library that wraps pandas and openpyxl and allows easy styling of dataframes in excel. Documentation can be found at http://styleframe.readthedocs.org

`pip install styleframe` · installs (wheel) · licence: MIT License · rank 13610 · last release 2023-11-13 · [PyPI](https://pypi.org/project/styleframe/)

<details><summary>README extract</summary>

A library that wraps pandas and openpyxl and allows easy styling of dataframes in excel. Documentation can be found at

</details>

### tilt-mcp

Model Context Protocol server for Tilt - interact with Tilt resources through MCP

`pip install tilt-mcp` · installs (wheel) · licence: MIT License · rank 13654 · last release 2025-07-15 · [PyPI](https://pypi.org/project/tilt-mcp/) · [docs](https://github.com/aryan-agrawal-glean/tilt-mcp#readme)

<details><summary>README extract</summary>

A Model Context Protocol (MCP) server that integrates with Tilt to provide programmatic access to Tilt resources and logs through LLM applications.

Features:
The Tilt MCP server allows Large Language Models (LLMs) and AI assistants to interact with your Tilt development environment. It provides tools to:

- List all enabled Tilt resources
- Fetch logs from specific resources ...

Sections: Tilt MCP Server, Overview, Features, Prerequisites, From PyPI (recommended), From Source, Configuration, For Claude Desktop, Usage, `get_all_resources`, `get_resource_logs`, Example Prompts, Running tests, Code formatting and linting

</details>

### KalturaApiClient

A Python module for accessing the Kaltura API.

`pip install KalturaApiClient` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 13675 · last release 2026-10-22 · [PyPI](https://pypi.org/project/KalturaApiClient/)

_README extract left out: share-alike licence._

### hyperi-ci

HyperI CI/CD CLI tool - multi-language build, test, and publish automation

`pip install hyperi-ci` · installs (wheel) · licence: LicenseRef-BUSL-1.1-HyperI · rank 13777 · last release 2026-11-05 · [PyPI](https://pypi.org/project/hyperi-ci/) · [docs](https://github.com/hyperi-io/hyperi-ci/blob/main/docs/README.md) · [source](https://github.com/hyperi-io/hyperi-ci)

<details><summary>README extract</summary>

One CLI for all your CI. Python, Rust, TypeScript, Go — same tool locally
and in GitHub Actions. No bash scripts, no composite actions, no submodules.

Version-first single-run pipeline. A `Release: true` git trailer on
your head commit is the single signal that a push is a release. ...

Features:
You get:

- One command before every push: `hyperi-ci check`
- Same quality / test / build runs locally as in CI — no "works on my machine"
- Automatic versioning via semantic-release (just use conventional commits) ...

Sections: hyperi-ci, What's New in v2.0, Why Use This, Preventative, Not Detective, Set Up a Project, Daily Workflow, Releasing, Commit Messages, Channel behaviour, Graduating to GA, Commands, How It Works, Config, Container Builds

</details>

### dbt-orchestra

Orchestra wrapper for dbt (dbt-core 1.x and dbt v2), including state aware orchestration.

`pip install dbt-orchestra` · installs (wheel) · licence: Apache-2.0 · rank 13793 · last release 2026-10-28 · [PyPI](https://pypi.org/project/dbt-orchestra/) · [source](https://github.com/orchestra-hq/sao-paolo)

<details><summary>README extract</summary>

`dbt-orchestra` wraps dbt commands, on dbt-core 1.x or dbt v2, using previous run state to reduce unnecessary work. It is designed to be added to an existing dbt project, not used as a standalone dbt repository.

There are a few core reasons to use this project: ...

Features:
dbt's `--indirect-selection` is global — it applies to your `--select` as much as to our reused-node exclusion. Forcing it to `cautious` everywhere would change what your own selection means, so when you pass your own `--select`/`--exclude`, `orc` ...

...

</details>

### TikTokApi

The Unofficial TikTok API Wrapper in Python 3.

`pip install TikTokApi` · installs (wheel) · licence: MIT License · rank 13813 · last release 2026-04-01 · [PyPI](https://pypi.org/project/TikTokApi/)

<details><summary>README extract</summary>

This is an unofficial api wrapper for TikTok.com in python. With this api you are able to call most trending and fetch specific user information as well as much more.

This api is designed to retrieve data TikTok. It can not be used post or upload content to TikTok on the behalf of a user. ...

Example:
```python
from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get("ms_token", None) # get your own ms_token from your cookies on tiktok.com

async def trending_videos():
    async with TikTokApi() as api:
...
```

Sections: Unofficial TikTok API in Python, Documentation, Getting Started, Common Issues, Quick Start Guide

</details>

### commit-check

Commit policy as code for teams and AI agents: check commit messages, branch names, authors, tags, files and AI attribution.

`pip install commit-check` · installs (wheel) · licence: MIT · rank 14004 · last release 2026-11-04 · [PyPI](https://pypi.org/project/commit-check/) · [docs](https://commit-check.com/) · [source](https://github.com/commit-check/commit-check)

<details><summary>README extract</summary>

Catch bad commits before they merge.

Docs ·
Rules ·
GitHub Action ·
GitHub App ·
MCP server

Commit Check is commit policy as code for teams and AI agents. It validates
commit messages, branch names, authors, sign-offs, tags, committed files and AI
attribution against one `cchk.toml` — in your commit hook, in CI, on every
pull request and inside ...

Features:
| | Commit Check | commitlint | GitHub Rulesets |
|---|:-:|:-:|:-:|
| Conventional Commits | ✅ | ✅ | regex only |
| Branch, tag, author and file rules | ✅ | ❌ | ✅\* |
| Feedback before the push | ✅ | ✅ | ❌ |
| Works with zero config | ✅ | ❌ | ❌ |
| ...

Example:
```python
from commit_check.api import validate_message

validate_message("feat: add streaming support")["status"]  # "pass"
```

...

</details>

### geetools

A collection of tools to work with Google Earth Engine Python API

`pip install geetools` · installs (wheel) · licence: MIT License · rank 14135 · last release 2026-10-29 · [PyPI](https://pypi.org/project/geetools/)

<details><summary>README extract</summary>

Google Earth Engine is a cloud-based service for geospatial processing of vector and raster data. The Earth Engine platform has a JavaScript and a Python API with different methods to process geospatial objects. ...

Features:
New utility methods and constructors are added to most of the GEE classes. They can be simple wrapper for repetitive tasks, complex algorithm or mandatory preprocessing steps. ...

Example:
```python
import ee
import geetools #noqa: F401
import pygaul # another gee-community package to access FAO GAUl 2015 dataset

# we assume you are already authenticated to GEE
ee.Initialize.geetools.from_user() # yes we also support multi users

amazonas = pygaul.Items(name="Amazonas").centroid()

S2 = (
   ee.ImageCollection('COPERNICUS/S2_SR')
...
```

...

</details>

### vcrpy-unittest

Python unittest integration for vcr.py

`pip install vcrpy-unittest` · installs (wheel) · licence: MIT License · rank 14145 · last release 2018-09-25 · [PyPI](https://pypi.org/project/vcrpy-unittest/)

<details><summary>README extract</summary>

This package provides `VCRTestCase` for simple integration between
VCR.py and Python's venerable unittest.

Example:
```python
from vcr_unittest import VCRTestCase
import requests

class MyTestCase(VCRTestCase):
   def test_something(self):
       response = requests.get('
```

Sections: vcrpy-unittest, Usage, VCRMixin, Compatibility

</details>

### maturin-import-hook

Import hook to load rust projects built with maturin

`pip install maturin-import-hook` · installs (wheel) · licence: Apache Software License; MIT License · rank 14205 · last release 2025-06-08 · [PyPI](https://pypi.org/project/maturin-import-hook/) · [docs](https://maturin.rs) · [source](https://github.com/PyO3/maturin-import-hook.git)

<details><summary>README extract</summary>

A python import hook to automatically rebuild maturin projects and import stand-alone rust files.

Using this import hook reduces friction when developing mixed python/rust codebases because changes made to rust
components take effect automatically like changes to python components do. ...

Example:
```python
import maturin_import_hook

# install the import hook with default settings.
# this call must be before any imports that you want the hook to be active for.
maturin_import_hook.install()

# when a rust package that is installed in editable mode is imported,
# that package will be automatically recompiled if necessary.
...
```

Sections: Maturin Import Hook, Usage, CLI, Debugging

</details>

### sfctl

Azure Service Fabric command line

`pip install sfctl` · installs (wheel) · licence: MIT License · rank 14219 · last release 2024-06-27 · [PyPI](https://pypi.org/project/sfctl/)

<details><summary>README extract</summary>

A command line interface for interacting with Azure Service Fabric clusters
and their related entities.

To get started, after installation run the following:

Sections: Service Fabric CLI, Invocation, 11.2.1, 11.2.0, 11.1.0, 11.0.0, 10.0.0, 9.0.0, 8.0.0, 7.1.0, 7.0.2, 7.0.1, 7.0.0, 6.0.1

</details>

### pur

Update packages in a requirements.txt file to latest versions.

`pip install pur` · installs from source (sdist only) · licence: BSD License · rank 14286 · last release 2026-04-26 · [PyPI](https://pypi.org/project/pur/)

<details><summary>README extract</summary>

Update the packages in a `requirements.txt` file.

Sections: pip-update-requirements, Usage, Options

</details>

### uiprotect

Python API for Unifi Protect (Unofficial)

`pip install uiprotect` · installs (wheel) · licence: MIT · rank 14356 · last release 2026-11-06 · [PyPI](https://pypi.org/project/uiprotect/) · [docs](https://uiprotect.readthedocs.io) · [source](https://github.com/uilibs/uiprotect)

<details><summary>README extract</summary>

Documentation:

Source Code:

Unofficial Python API and CLI for UniFi Protect, for any UniFi OS console that runs Protect. It is the library behind the Home Assistant UniFi Protect integration and can be used on its own. uiprotect is not affiliated with or endorsed by Ubiquiti. ...

Example:
```python
import asyncio

from uiprotect import ProtectApiClient, ProtectDeviceChange

def on_device(change: ProtectDeviceChange) -> None:
    print(change.change, change.device_id, sorted(change.changed_fields))

async def main() -> None:
    protect = ProtectApiClient.public_only(
        "YOUR_CONSOLE_IP", 443, "YOUR_API_KEY", verify_ssl=False
    )
...
```

...

</details>

### lightningcss-cli

(no summary)

`pip install lightningcss-cli` · installs (wheel) · licence: not stated · rank 14503 · last release 2025-10-23 · [PyPI](https://pypi.org/project/lightningcss-cli/) · [docs](https://lightningcss.dev/docs.html) · [source](https://github.com/joshuadavidthomas/lightningcss)

<details><summary>README extract</summary>

A Python package for installing the Lightning CSS CLI tool.

Sections: lightningcss-cli, Using pip, Using uv, Documentation and Usage

</details>

### spdx3-validate

Validates SPDX 3 data files

`pip install spdx3-validate` · installs (wheel) · licence: MIT License · rank 14533 · last release 2026-08-10 · [PyPI](https://pypi.org/project/spdx3-validate/) · [source](https://github.com/JPEWdev/spdx3-validate.git)

<details><summary>README extract</summary>

Validates SPDX 3 documents

While standalone tools like `pyshacl` and `check-jsonschema` can be used to
validate SPDX 3 documents, there are a few context-aware checks that can be
useful. This includes:

1. Ignored SHACL errors for missing `spdxId`s if they are defined in an
 `ExternalMap`
2. ...

Example:
```python
import spdx3_validate

result = spdx3_validate.validate("doc.spdx3.json")
if not result:
    print(result)  # prints the errors, one per line

# Or inspect the individual findings:
for error in result.errors:
    print(error)
```

Sections: SPDX 3 Validation Tool, Using as a library, TODO

</details>

### pywav

Read and write wav files with PCMA/PCMU compression

`pip install pywav` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 14633 · last release 2020-02-05 · [PyPI](https://pypi.org/project/pywav/)

_README extract left out: share-alike licence._

### blockfrost-python

The official Python SDK for Blockfrost API v0.1.86

`pip install blockfrost-python` · installs (wheel) · licence: Apache Software License · rank 14695 · last release 2026-03-16 · [PyPI](https://pypi.org/project/blockfrost-python/)

<details><summary>README extract</summary>

A Python SDK for Blockfrost.io API

 Getting started •
 Installation •
 Usage

Example:
```python
from blockfrost import BlockFrostApi, ApiError, ApiUrls

api = BlockFrostApi(
    project_id='YOUR API KEY HERE',  # or export environment variable BLOCKFROST_PROJECT_ID
    # optional: pass base_url or export BLOCKFROST_API_URL to use testnet, defaults to ApiUrls.mainnet.value
    base_url=ApiUrls.testnet.value,
)
try:
    health = api.health()
...
```

Sections: blockfrost-python, Getting started, Usage, Cardano, IPFS, Verifying Secure Webhook signature

</details>

### localspelling

Translates input between UK and US spelling

`pip install localspelling` · installs from source (sdist only) · licence: MIT License · rank 14705 · last release 2020-10-13 · [PyPI](https://pypi.org/project/localspelling/)

<details><summary>README extract</summary>

Developed by Fast Data Science,

Source code at

Python library for localising spelling between British and American conventions, conserving case.

Please note this library converts only spelling variants such as US "honour" vs UK "honor".

It does not localise vocabulary such as "pavement" vs "sidewalk" or "aubergine" vs "eggplant". ...

Example:
```python
from localspelling import convert_spelling
convert_spelling("it has been an honor", "gb")
```

Sections: Local spelling, Requirements, Usage examples, Who to contact

</details>

### django-treenode

probably the best abstract model/admin for your tree based stuff.

`pip install django-treenode` · installs (wheel) · licence: MIT License · rank 14707 · last release 2026-08-26 · [PyPI](https://pypi.org/project/django-treenode/) · [docs](https://github.com/fabiocaccamo/django-treenode#readme)

<details><summary>README extract</summary>

Probably the best abstract model / admin for your tree based stuff.

Features:
- Fast - get `ancestors`, `children`, `descendants`, `parent`, `root`, `siblings`, `tree` with no queries
- Synced - in-memory model instances are automatically updated
- Compatibility - you can easily add `treenode` to existing projects ...

Example:
```python
from django.db import models

from treenode.models import TreeNodeModel

class Category(TreeNodeModel):

    # the field used to display the model instance
    # default value 'pk'
    treenode_display_field = "name"

    name = models.CharField(max_length=50)

    class Meta(TreeNodeModel.Meta):
        verbose_name = "Category"
...
```

...

</details>

### essential-generators

Generate fake data for application testing based on simple but flexible templates.

`pip install essential-generators` · installs (wheel) · licence: MIT License · rank 14832 · last release 2020-12-17 · [PyPI](https://pypi.org/project/essential-generators/)

<details><summary>README extract</summary>

Whether it's testing database performance or a new web interface, we've all needed a dead simple
solution that'a flexible enough to generate a complex data set. If this is one of those times,
you've come to the right place. ...

Features:
There are several great python module out there that generate fake data, so why did I make this?
Two reasons really:

1. I wanted a dead simple way to generate data to test other projects and I just wasn't finding
the flexibility I was looking for. ...

Example:
```python
>>> from essential_generators import DocumentGenerator

>>> gen = DocumentGenerator()

>>> gen.email()
'cal.atis@prand.com'

>>> gen.url()
''

>>> gen.phone()
'547-922-3848'

>>> gen.slug()
'ehillote-henaiour-ebemaice-qsiat76-heheellti'

>>> gen.word()
'choleg'

>>> gen.sentence()
...
...

</details>

### onepipeline-cli

Execute a task DAG over oneagentgraph and onevcs, merging their event streams into one.

`pip install onepipeline-cli` · does not install on CPython 3.14 · licence: MIT License · rank 14911 · last release 2026-10-26 · [PyPI](https://pypi.org/project/onepipeline-cli/) · [source](https://github.com/nickderobertis/onepipeline)

<details><summary>README extract</summary>

<!-- llmlint: ignore[contracts_have_one_source_or_a_drift_gate] the hero renders the same
run the hash-gated stills come from, and a GIF is not byte-reproducible, so it is
deliberately the one image with no hash gate. `screenshots/AGENTS.md` holds that ruling
and what to re-render on. --> ...

Features:
The verbs, in one screen:

`start` drives the run itself: a node — and each step within a lifecycle
node — dispatches the moment its dependencies settle, and settlement triggers
integration and publication immediately. No agent is required. ...

Sections: onepipeline, How the npm launcher is published, Where a plan lives, What it does, Where a dispatch runs

</details>

### membrowse

Memory footprint analysis tools for embedded firmware

`pip install membrowse` · installs (wheel) · licence: not stated · rank 14992 · last release 2026-11-04 · [PyPI](https://pypi.org/project/membrowse/) · [docs](https://github.com/membrowse/membrowse-action#readme) · [source](https://github.com/membrowse/membrowse-action)

<details><summary>README extract</summary>

Catch memory regressions before they ship. MemBrowse tracks the flash and RAM footprint of your firmware on every commit, comments the memory diff on every pull request, and fails the build when you blow your budget. ...

Features:
- Architecture Agnostic: Works with any toolchain that produces ELFs with DWARF debug info (ARM, Xtensa, RISC-V, and more)
- Source File Mapping: Symbols are mapped back to their definition source files ...

Sections: MemBrowse, Firmware teams tracking memory with MemBrowse, Features, Quick Start, Analyze your firmware locally (no account required), Track memory in CI (GitHub Actions), Set it up with Claude Code

</details>

## Also in this topic

- [tqdm](desktop-environment.md#tqdm) - Fast, Extensible Progress Meter
- [invoke](software-development.md#invoke) - Pythonic task execution
- [progressbar2](desktop-environment.md#progressbar2) - A Python Progressbar library to provide visual (yet text based) progress to long running operations.
- [pytest-httpx](internet-www-http.md#pytest-httpx) - Send responses to httpx.
- [pyinstaller](software-development.md#pyinstaller) - PyInstaller bundles a Python application and all its dependencies into a single package.
- [scikit-build-core](scientific-engineering.md#scikit-build-core) - Build backend for CMake based projects
- [fabric](software-development.md#fabric) - High level SSH command execution
- [aws-sam-translator](internet.md#aws-sam-translator) - AWS SAM Translator is a library that transform SAM templates into AWS CloudFormation templates
- [checkov](security.md#checkov) - Infrastructure as code static analysis
- [shtab](desktop-environment.md#shtab) - Automagic shell tab completion for Python CLI applications
- [ccxt](office-business-financial.md#ccxt) - A cryptocurrency trading API with more than 100 exchanges in JavaScript / TypeScript / Python / C# / PHP / Go
- [platformio](software-development.md#platformio) - Your Gateway to Embedded Software Development Excellence. Unlock the true potential of embedded software development with PlatformIO's collaborative ecosystem, embracing declarative principles, test-driven methodologies, and modern toolchains for unrivaled success.
- [pyngrok](internet-proxy-servers.md#pyngrok) - The complete ngrok agent for Python: programmatic tunnels for ingress, inspection, webhooks, demos, and APIs
- [aws-sam-cli](internet.md#aws-sam-cli) - AWS SAM CLI is a CLI tool for local development and testing of Serverless applications
- [aws-lambda-builders](internet.md#aws-lambda-builders) - Python library to compile, build & package AWS Lambda functions for several runtimes & frameworks.
- [auditwheel](software-development.md#auditwheel) - Cross-distribution Linux wheels
- [sec-api](office-business-financial.md#sec-api) - SEC EDGAR Filings API
- [python-fsutil](desktop-environment-file-managers.md#python-fsutil) - high-level file-system operations for lazy devs.
- [spark-nlp](scientific-engineering.md#spark-nlp) - John Snow Labs Spark NLP is a natural language processing library built on top of Apache Spark ML. It provides simple, performant & accurate NLP annotations for machine learning pipelines, that scale easily in a distributed environment.
- [ydata-profiling](scientific-engineering.md#ydata-profiling) - Generate profile report for pandas DataFrame
- [doit](scientific-engineering.md#doit) - doit - Automation Tool
- [python-benedict](education-testing.md#python-benedict) - python-benedict is a dict subclass with keylist/keypath/keyattr support, normalized I/O operations (base64, csv, ini, json, pickle, plist, query-string, toml, xls, xml, yaml) and many utilities... for humans, obviously.
- [pyarmor](security.md#pyarmor) - A tool used to obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts.
- [pyarmor.cli.core](security.md#pyarmorclicore) - Provide extension module pytransform3 for Pyarmor
- [delvewheel](software-development.md#delvewheel) - Self-contained wheels for Windows
- [lerobot](scientific-engineering-artificial-intelligence.md#lerobot) - 🤗 LeRobot: State-of-the-art Machine Learning for Real-World Robotics in Pytorch
- [pioarduino](software-development.md#pioarduino) - pioarduino core is needed to run pioarduino Platform espressif32.
- [asciichartpy](office-business-financial.md#asciichartpy) - Nice-looking lightweight console ASCII line charts ╭┈╯ with no dependencies
- [yagmail](communications-email.md#yagmail) - Yet Another GMAIL client
- [siliconcompiler](scientific-engineering-electronic-design-automation-eda.md#siliconcompiler) - A compiler framework that automates translation from source code to silicon.
- [scour](internet.md#scour) - Scour SVG Optimizer
- [zcbor](file-formats-json.md#zcbor) - Code generation and data validation using CDDL schemas
- [arcp](internet.md#arcp) - arcp (Archive and Package) URI parser and generator
- [pr-commenter](communications.md#pr-commenter) - Create and manage automatic comments in a Github PR
- [flawfinder](security.md#flawfinder) - a program that examines source code looking for security weaknesses
- [gitman](software-development.md#gitman) - A language-agnostic dependency manager using Git.
- [bittensor-wallet](scientific-engineering.md#bittensor-wallet) - 
- [braindecode](scientific-engineering-artificial-intelligence.md#braindecode) - Deep learning software to decode EEG, ECG or MEG signals
- [bernstein](software-development.md#bernstein) - The open-source governance layer for AI agents. No model in the coordination loop, so replaying a plan reproduces its task graph byte-identically, and run receipts are byte-identical across independent builds. Signed lineage plus an opt-in HMAC audit chain a reviewer checks offline, without rerunning it. Runs Claude Code, Codex, Gemini CLI, and 50+ CLI agents; governs any deliverable from code to research to audit evidence packs. Cluster mode, air-gap deploy.
- [pandas-profiling](scientific-engineering-2.md#pandas-profiling) - Deprecated 'pandas-profiling' package, use 'ydata-profiling' instead
- [bittensor-drand](scientific-engineering-2.md#bittensor-drand) - Rust-backed Python library for generating timelock-encrypted weight commitments for Bittensor's commit-reveal mechanism using drand randomness.
- [httpx2-pytest](internet-www-http-2.md#httpx2-pytest) - Send responses to httpx2.
- [Paver](documentation.md#paver) - Easy build, distribution and deployment scripting
- [rebound](scientific-engineering-astronomy.md#rebound) - An open-source multi-purpose N-body code
- [bridgecrew](security.md#bridgecrew) - Infrastructure as code static analysis
- [latch](scientific-engineering-2.md#latch) - The Latch SDK
- [flit-scm](software-development.md#flit-scm) - A PEP 518 build backend that uses setuptools_scm to generate a version file from your version control system, then flit to build the package.
- [pyinstaller-versionfile](software-development.md#pyinstaller-versionfile) - Create a windows version-file from metadata stored in a simple self-written YAML file or obtained from an installed distribution.
- [fabric2](software-development.md#fabric2) - High level SSH command execution
- [qiskit-connector](scientific-engineering-2.md#qiskit-connector) - Quantum Computing Qiskit Connector For Quantum Backend Use In Realtime
- [nunavut](scientific-engineering-2.md#nunavut) - Generate code from DSDL using Jinja2 templates.
- [hexor](internet-www-http-2.md#hexor) - Coloring texts and their backgrounds in command line interface (cli), with rgb or hex types.
- [Fabric3](software-development.md#fabric3) - Fabric is a simple, Pythonic tool for remote execution and deployment (py2.7/py3.4+ compatible fork).
