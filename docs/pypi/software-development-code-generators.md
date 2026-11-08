# Software Development / Code Generators

[Index](README.md) · 44 packages in this topic, 54 more listed under another topic, by downloads.

### proto-plus

Beautiful, Pythonic protocol buffers

`pip install proto-plus` · installs (wheel) · licence: Apache Software License · rank 117 · last release 2026-09-29 · [PyPI](https://pypi.org/project/proto-plus/) · [docs](https://googleapis.dev/python/proto-plus/latest/) · [source](https://github.com/googleapis/google-cloud-python)

<details><summary>README extract</summary>

Beautiful, Pythonic protocol buffers.

This is a wrapper around protocol buffers. Protocol buffers is a
specification format for APIs, such as those inside Google.
This library provides protocol buffer message classes and objects that
largely behave like native Python types.

API Documentation is available on Read the Docs.

Sections: Proto Plus for Python, Documentation

</details>

### asttokens

Annotate AST trees with source code positions

`pip install asttokens` · installs (wheel) · licence: Apache 2.0 · rank 278 · last release 2026-07-12 · [PyPI](https://pypi.org/project/asttokens/) · [docs](https://asttokens.readthedocs.io/en/latest/index.html)

<details><summary>README extract</summary>

The `asttokens` module annotates Python abstract syntax trees (ASTs) with the positions of tokens
and text in the source code that generated them.

It makes it possible for tools that work with logical AST nodes to find the particular text that
resulted in those nodes, for example for automated refactoring or highlighting.

Example:
```python
import asttokens, ast
source = "Robot('blue').walk(steps=10*n)"
atok = asttokens.ASTTokens(source, parse=True)
```

Sections: ASTTokens, Usage, Documentation

</details>

### Cython

The Cython compiler for writing C extensions in the Python language.

`pip install Cython` · installs (wheel) · licence: Apache-2.0 · rank 312 · last release 2026-11-01 · [PyPI](https://pypi.org/project/Cython/) · [docs](https://cython.readthedocs.io/) · [source](https://github.com/cython/cython)

<details><summary>README extract</summary>

The Cython language makes writing C extensions for the Python language as
easy as Python itself. Cython is a source code translator based on Pyrex,
but supports more cutting edge functionality and optimizations. ...

Features:
* Declarations for the C99 `bool` type in `<stdbool.h>` were added.
 (Github issue

* Fused function objects are slightly smaller in the Limited API.
 (Github issue ...

Sections: 3.3.1 (2026-11-01), Features added, Bugs fixed, Other changes

</details>

### beartype

Unbearably fast near-real-time pure-Python runtime-static type-checker.

`pip install beartype` · installs (wheel) · licence: MIT · rank 324 · last release 2026-10-11 · [PyPI](https://pypi.org/project/beartype/) · [docs](https://beartype.readthedocs.io) · [source](https://github.com/beartype/beartype)

<details><summary>README extract</summary>

Beartype documentation lives at ReadTheDocs (RTD). It's
 readable, structured, and soothing to the deep folds of your big galactic
 brain. Open your mind to an ocean of mundane knowledge that will exhaust
 you at work. Enter... the Bearpedia: ...

Example:
```python
from beartype.claw import beartype_this_package       # <-- hype comes
beartype_this_package()                               # <-- hype goes
```

</details>

### llvmlite

lightweight wrapper around basic LLVM functionality

`pip install llvmlite` · installs (wheel) · licence: BSD-2-Clause AND Apache-2.0 WITH LLVM-exception · rank 386 · last release 2026-09-29 · [PyPI](https://pypi.org/project/llvmlite/) · [source](https://github.com/numba/llvmlite)

<details><summary>README extract</summary>

llvmlite is a project originally tailored for Numba's needs, using the
following approach:

* A small C wrapper around the parts of the LLVM C++ API we need that are
 not already exposed by the LLVM C API.
* A ctypes Python wrapper around the C API.
* A pure Python implementation of the subset of the LLVM IR builder that we
 need for Numba.

Features:
The old llvmpy binding exposes a lot of LLVM APIs but the mapping of
C++-style memory management to Python is error prone. Numba and many JIT
compilers do not need a full LLVM API. Only the IR builder, optimizer,
and JIT compiler APIs are necessary.

Sections: llvmlite, A Lightweight LLVM Python Binding for Writing JIT Compilers, Why llvmlite, Key Benefits, Compatibility, Documentation, Pre-built binaries, Other build methods

</details>

### parse

parse() is the opposite of format()

`pip install parse` · installs (wheel) · licence: MIT · rank 950 · last release 2026-10-20 · [PyPI](https://pypi.org/project/parse/)

<details><summary>README extract</summary>

Example:
```python
>>> parse("It's {}, I love it!", "It's spam, I love it!")

>>> _[0]
'spam'
```

Sections: Usage, Format Syntax, Format Specification, Result and Match Objects, Custom Type Conversions, Potential Gotchas

</details>

### astor

Read/rewrite/write Python ASTs

`pip install astor` · installs (wheel) · licence: BSD License · rank 1205 · last release 2019-12-10 · [PyPI](https://pypi.org/project/astor/)

<details><summary>README extract</summary>

:PyPI:
:Documentation:
:Source:
:License: 3-clause BSD
:Build status:
 .. image::
 :alt: Travis CI
 :target:

astor is designed to allow easy manipulation of Python source via the AST.

There are some other similar libraries, but astor focuses on the following areas:

 - Modified AST doesn't need linenumbers, ctx, etc. ...

</details>

### astunparse

An AST unparser for Python

`pip install astunparse` · installs (wheel) · licence: BSD License · rank 1320 · last release 2019-12-22 · [PyPI](https://pypi.org/project/astunparse/)

<details><summary>README extract</summary>

An AST unparser for Python.

This is a factored out version of `unparse` found in the Python
source distribution; under Demo/parser in Python 2 and under Tools/parser
in Python 3.

Basic example:
This library is single-source compatible with Python 2.6 through Python 3.5. ...

Features:
* unparses Python AST.
* pretty-prints AST.

Example:
```python
import inspect
import ast
import astunparse

# get back the source code
astunparse.unparse(ast.parse(inspect.getsource(ast)))

# get a pretty-printed dump of the AST
astunparse.dump(ast.parse(inspect.getsource(ast)))
```

...

</details>

### parse-type

Simplifies to build parse types based on the parse module

`pip install parse-type` · installs (wheel) · licence: MIT · rank 1501 · last release 2025-08-11 · [PyPI](https://pypi.org/project/parse-type/) · [source](https://github.com/jenisys/parse_type)

<details><summary>README extract</summary>

|badge.CI_statusbadge.latest_versionbadge.licensebadge.downloads|

parse_type extends the parse module (opposite of string.format())
with the following features:

* build type converters for common use cases (enum/mapping, choice)
* build a type converter with a cardinality constraint (0..1, 0..*, 1..*)
 from the type converter with cardinality=1. ...

Example:
```python
# -- USE CASE:
def parse_number(text):
    return int(text)
parse_number.pattern = r"\d+"  # -- REGULAR EXPRESSION pattern for type.
```

Sections: parse_type, Definitions, Basic Example, Cardinality, Enumeration (Name-to-Value Mapping), Choice (Name Enumeration), Variant (Type Alternatives)

</details>

### openapi-python-client

Generate modern Python clients from OpenAPI

`pip install openapi-python-client` · installs (wheel) · licence: MIT · rank 2045 · last release 2026-11-07 · [PyPI](https://pypi.org/project/openapi-python-client/) · [source](https://github.com/openapi-generators/openapi-python-client)

<details><summary>README extract</summary>

Generate modern Python clients from OpenAPI 3.0 and 3.1 documents.

_This generator does not support OpenAPI 2.x FKA Swagger. If you need to use an older document, try upgrading it to
version 3 first with one of many available converters._

This project is still in development and does not support all OpenAPI features

Features:
This tool focuses on creating the best developer experience for Python developers by:

1. Using all the latest and greatest Python features like type annotations and dataclasses.
2. ...

Example:
```python
class Color(IntEnum):
    RED = 0
    GREEN = 1
    BLUE = 2
```

...

</details>

### xsdata

Python XML Binding

`pip install xsdata` · installs (wheel) · licence: MIT · rank 2326 · last release 2026-10-16 · [PyPI](https://pypi.org/project/xsdata/) · [docs](https://xsdata.readthedocs.io/) · [source](https://github.com/tefra/xsdata)

<details><summary>README extract</summary>

xsData is a complete data binding library for python allowing developers to access and
use XML and JSON documents as simple objects rather than using DOM.

The code generator supports XML schemas, DTD, WSDL definitions, XML & JSON documents. It
produces simple dataclasses with type hints and simple binding metadata. ...

Features:
Code Generator

- XML Schemas 1.0 & 1.1
- WSDL 1.1 definitions with SOAP 1.1 bindings
- DTD external definitions
- Directly from XML and JSON Documents
- Extensive configuration to customize output
- Pluggable code writer for custom output formats ...

Example:
```python
>>> from tests.fixtures.primer import PurchaseOrder
>>> from xsdata.formats.dataclass.parsers import XmlParser
>>>
>>> parser = XmlParser()
...

</details>

### pytablewriter

pytablewriter is a Python library to write a table in various formats: AsciiDoc / CSV / Elasticsearch / HTML / JavaScript / JSON / LaTeX / LDJSON / LTSV / Markdown / MediaWiki / NumPy / Excel / Pandas / Python / reStructuredText / SQLite / TOML / TSV / YAML.

`pip install pytablewriter` · installs (wheel) · licence: MIT License · rank 2684 · last release 2025-01-01 · [PyPI](https://pypi.org/project/pytablewriter/) · [docs](https://pytablewriter.rtfd.io/) · [source](https://github.com/thombashi/pytablewriter)

<details><summary>README extract</summary>

pytablewriter is a Python library to write a table in various formats: AsciiDoc / CSV / Elasticsearch / HTML / JavaScript / JSON / LaTeX / LDJSON / LTSV / Markdown / MediaWiki / NumPy / Excel / Pandas / Python / reStructuredText / SQLite / TOML / TSV / YAML.

Features:
- AsciiDoc
 - CSV / Tab-separated values (TSV) / Space-separated values (SSV)
 - HTML / CSS
 - JSON / Line-delimited JSON(LDJSON)
 - Labeled Tab-separated Values (LTSV)
 - LaTeX: `tabular`/`array` environment
 - Markdown: CommonMark / GitHub ...

Example:
```python
from multiprocessing import cpu_count
import pytablewriter as ptw

def main():
    writer = ptw.MarkdownTableWriter()
    writer.max_workers = cpu_count()
    ...

if name == "main":
    main()
```

...

</details>

### stone

Stone is an interface description language (IDL) for APIs.

`pip install stone` · installs (wheel) · licence: MIT · rank 2963 · last release 2026-09-23 · [PyPI](https://pypi.org/project/stone/)

<details><summary>README extract</summary>

The Official Api Spec Language for Dropbox.

Documentation can be found on GitHub

Features:
Define an API once in Stone. Use backends, i.e. code generators, to translate
your specification into objects and functions in the programming languages of
your choice. ...

Sections: Alternative, Overview, Language, Command-Line Interface, Backends, JSON Serialization, Motivation, Assumptions, Examples, Getting Help

</details>

### esprima

ECMAScript parsing infrastructure for multipurpose analysis in Python

`pip install esprima` · installs from source (sdist only) · licence: BSD License · rank 3818 · last release 2018-08-24 · [PyPI](https://pypi.org/project/esprima/)

<details><summary>README extract</summary>

Esprima (esprima.org, BSD license) is a
high performance, standard-compliant
ECMAScript
parser officially written in ECMAScript (also popularly known as
JavaScript) and ported to
Python. Esprima is created and maintained by Ariya
Hidayat, with the help of many
contributors. ...

Features:
- Full support for ECMAScript 2017 (ECMA-262 8th
 Edition)
- Sensible syntax tree
 format as
 standardized by ESTree project
- Experimental support for JSX, a
 syntax extension for React ...

Sections: Features, API

</details>

### PyLaTeX

A Python library for creating LaTeX files and snippets

`pip install PyLaTeX` · installs from source (sdist only) · licence: MIT License · rank 4132 · last release 2023-10-19 · [PyPI](https://pypi.org/project/PyLaTeX/)

<details><summary>README extract</summary>

PyLaTeX is a Python library for creating and compiling LaTeX files or
snippets. The goal of this library is being an easy, but extensible
interface between Python and LaTeX.

Sections: PyLaTeX, Ubuntu, Documentation, Examples

</details>

### abnf

Parsers for ABNF grammars.

`pip install abnf` · installs (wheel) · licence: MIT License · rank 4211 · last release 2026-10-21 · [PyPI](https://pypi.org/project/abnf/) · [docs](https://abnf.readthedocs.io/) · [source](https://github.com/declaresub/abnf)

<details><summary>README extract</summary>

ABNF generates parsers from ABNF grammars as described in
RFC 5234 and
RFC 7405. Its main purpose is parsing data
specified in RFCs — HTTP headers, email addresses, URIs, and the like — but it
handles any ABNF grammar. ...

Example:
```python
from abnf.grammars import rfc7232

# parse an ETag header value
node, offset = rfc7232.Rule("ETag").parse('W/"moof"', 0)
print(node.value)          # 'W/"moof"'

# validate a whole string against a rule (raises ParseError otherwise)
from abnf.grammars import rfc5322
rfc5322.Rule("address").parse_all("test@example.com")

...
```

Sections: ABNF, Quick start, Parsing bytes, Documentation, Third-party packages

</details>

### protoc-gen-connect-python

Code generator for connect-python

`pip install protoc-gen-connect-python` · installs (wheel) · licence: Apache-2.0 · rank 4776 · last release 2026-03-19 · [PyPI](https://pypi.org/project/protoc-gen-connect-python/) · [source](https://github.com/connectrpc/connect-python)

### toml-sort

Toml sorting library

`pip install toml-sort` · installs (wheel) · licence: MIT License · rank 5200 · last release 2026-09-12 · [PyPI](https://pypi.org/project/toml-sort/) · [source](https://github.com/pappasam/toml-sort)

<details><summary>README extract</summary>

A command line utility to sort and format toml files.

Sections: toml-sort, Motivation, Command line usage, Configuration file, Configuration Overrides, Comments, Header, Footer, Inline, Block, Orphan, Example, Unformatted, unsorted input, Formatted, sorted output

</details>

### pythran

Ahead of Time compiler for numeric kernels

`pip install pythran` · installs (wheel) · licence: not stated · rank 5575 · last release 2026-08-17 · [PyPI](https://pypi.org/project/pythran/) · [docs](https://pythran.readthedocs.io)

<details><summary>README extract</summary>

Pythran is an ahead of time compiler for a subset of the Python language, with a
focus on scientific computing. It takes a Python module annotated with a few
interface descriptions and turns it into a native Python module with the same
interface, but (hopefully) faster. ...

Example:
```python
"""
Naive dotproduct! Pythran supports numpy.dot
"""
# pythran export dprod(int list, int list)
def dprod(l0,l1):
    """WoW, generator expression, zip and sum."""
    return sum(x * y for x, y in zip(l0, l1))
```

Sections: Pythran, What is it?, Debian/Ubuntu, Using `pip`, Using `mamba` or `conda`, Mac OSX, ArchLinux, Fedora, Windows, Other Platform, Basic Usage, Documentation, Examples, Contact

</details>

### bump-pydantic

Convert Pydantic from V1 to V2 ♻

`pip install bump-pydantic` · installs (wheel) · licence: MIT License · rank 6849 · last release 2023-12-28 · [PyPI](https://pypi.org/project/bump-pydantic/) · [docs](https://github.com/pydantic/bump-pydantic#readme) · [source](https://github.com/pydantic/bump-pydantic)

<details><summary>README extract</summary>

Bump Pydantic is a tool to help you migrate your code from Pydantic V1 to V2.

> [!NOTE]\
> If you find bugs, please report them on the issue tracker.

Example:
```python
class User(BaseModel):
    name: Optional[str]
```

Sections: Bump Pydantic ♻️, Usage, Check diff before applying changes, Apply changes, Rules, BP002: Replace `Config` class by `model_config` attribute, BP003: Replace `Field` old parameters to new ones, BP004: Replace imports, BP005: Replace `GenericModel` by `BaseModel`, BP006: Replace `root` by `RootModel`, BP007: Replace decorators, BP008: Replace `con*` functions by `Annotated` versions

</details>

### hatch-protobuf

A Hatch build plugin to generate Python files from Protocol Buffers .proto files

`pip install hatch-protobuf` · installs (wheel) · licence: MPL-2.0 · rank 7007 · last release 2025-07-16 · [PyPI](https://pypi.org/project/hatch-protobuf/) · [source](https://github.com/nanoporetech/hatch-protobuf)

<details><summary>README extract</summary>

Example:
```python
# example/v1/example_pb2.py
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
```

Sections: Usage, Custom generators, Mypy output, Import `.proto` files from `site-packages`

</details>

### cogapp

Cog: A content generator for executing Python snippets in source files.

`pip install cogapp` · installs (wheel) · licence: MIT · rank 7042 · last release 2025-09-21 · [PyPI](https://pypi.org/project/cogapp/) · [docs](https://cog.readthedocs.io/) · [source](http://github.com/nedbat/cog)

<details><summary>README extract</summary>

licenseversionsstatus|
ci-statuskitformat|
sponsorbluesky-nedbatmastodon-nedbat|

Cog content generation tool. Small bits of computation for static files.

See the cog docs for details.

Code repository and issue tracker are at
GitHub.

To run the tests:

</details>

### ansible-creator

A CLI tool for scaffolding Ansible Content.

`pip install ansible-creator` · installs (wheel) · licence: Apache Software License · rank 7471 · last release 2026-11-05 · [PyPI](https://pypi.org/project/ansible-creator/) · [docs](https://ansible.readthedocs.io/projects/creator/) · [source](https://github.com/ansible/ansible-creator)

<details><summary>README extract</summary>

A CLI tool for scaffolding all your Ansible Content.

Sections: ansible-creator, Usage, Command line completion, Upcoming features, Communication, Licensing

</details>

### protoc-gen-connectrpc

Code generator for Connect RPC

`pip install protoc-gen-connectrpc` · installs (wheel) · licence: Apache-2.0 · rank 7552 · last release 2026-10-25 · [PyPI](https://pypi.org/project/protoc-gen-connectrpc/) · [source](https://github.com/connectrpc/connect-py)

### xsdata-pydantic

xsdata pydantic plugin

`pip install xsdata-pydantic` · installs (wheel) · licence: MIT License · rank 7629 · last release 2024-05-08 · [PyPI](https://pypi.org/project/xsdata-pydantic/) · [docs](https://xsdata-pydantic.readthedocs.io/) · [source](https://github.com/tefra/xsdata-pydantic)

<details><summary>README extract</summary>

xsData is a complete data binding library for python allowing developers to access and
use XML and JSON documents as simple objects rather than using DOM.

Now powered by pydantic!

Example:
```python
class Rss(BaseModel):
    class Meta:
        name = "rss"

    model_config = ConfigDict(defer_build=True)
    version: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    channel: Channel = field(
        metadata={
            "type": "Element",
            "required": True,
...
```

</details>

### pyangbind

PyangBind is a plugin for pyang which converts YANG data models into a Python class hierarchy, such that Python can be used to manipulate data that conforms with a YANG model.

`pip install pyangbind` · installs (wheel) · licence: Apache Software License · rank 7877 · last release 2025-12-10 · [PyPI](https://pypi.org/project/pyangbind/)

<details><summary>README extract</summary>

PyangBind is a plugin for pyang which converts YANG data models into a Python class hierarchy, such that Python can be used to manipulate data that conforms with a YANG model.

This module provides the supporting classes and functions that PyangBind modules utilise, particularly: ...

</details>

### modelcontextprotocol

CLI tool and utilities for scaffolding Model Context Protocol (MCP) projects with enhanced logging

`pip install modelcontextprotocol` · installs (wheel) · licence: MIT License · rank 8135 · last release 2025-11-26 · [PyPI](https://pypi.org/project/modelcontextprotocol/) · [docs](https://github.com/leanmcp/modelcontextprotocol#readme) · [source](https://github.com/leanmcp/modelcontextprotocol)

<details><summary>README extract</summary>

Features:
- Quick Scaffolding - Generate MCP projects instantly
- Enhanced Logging - Beautiful logs with loguru out of the box
- Analytics - Optional PostHog integration for usage tracking
- Beautiful CLI - Rich terminal UI with helpful prompts ...

Example:
```python
from mcp.server.fastmcp import FastMCP
from loguru import logger

# Configure logging
logger.add("my-server.log", rotation="10 MB", level="INFO")
logger.info("Initializing my-server MCP server")

# Initialize server
mcp = FastMCP("my-server")

@mcp.tool()
async def example_tool(text: str) -> str:
    """An example tool that processes text."""
...
```

...

</details>

### spark-parser

An Earley-Algorithm Context-free grammar Parser Toolkit

`pip install spark-parser` · installs (wheel) · licence: MIT · rank 8329 · last release 2024-10-14 · [PyPI](https://pypi.org/project/spark-parser/)

<details><summary>README extract</summary>

This package uses Jay Earley's algorithm for parsing context-free
grammars, and comes with some generic Abstract Syntax Tree
routines. There is also a prototype scanner that does its job by
combining Python regular expressions.

(SPARK stands for Scanning, Parsing, and Rewriting Kit. ...

Features:
Many of the added features are directly related to using it in the Python decompiler uncompyle6.

One unique feature of this code is the ability to have it profile
which grammar rules have been used over a series of parses. ...

Sections: An Earley Algorithm Parser toolkit., Features, Example, See Also

</details>

### PyXB-X

PyXB-X ("pixbix") is a pure Python package that generates Python source code for classes that correspond to data structures defined by XMLSchema.

`pip install PyXB-X` · installs (wheel) · licence: Apache Software License · rank 9134 · last release 2026-07-28 · [PyPI](https://pypi.org/project/PyXB-X/)

<details><summary>README extract</summary>

PyXB is a pure `Python < package that generates
Python code for classes that correspond to data structures defined by
`XMLSchema < In concept it is similar to
`JAXB < for Java and `CodeSynthesis XSD
< for C++.

The major goals of PyXB are: ...

</details>

### openrewrite

OpenRewrite automated refactoring for Python.

`pip install openrewrite` · installs (wheel) · licence: LicenseRef-Moderne-Source-Available · rank 9368 · last release 2026-11-07 · [PyPI](https://pypi.org/project/openrewrite/) · [docs](https://docs.openrewrite.org) · [source](https://github.com/openrewrite/rewrite.git)

<details><summary>README extract</summary>

OpenRewrite automated refactoring for Python source code. This package provides
the recipe framework, the Python Lossless Semantic Tree (LST), and the testing
helpers you use to author and test Python recipes.

Example:
```python
from rewrite.test import RecipeSpec, python

def test_renames_a_call():
    spec = RecipeSpec(recipe=RenameFunctionCall(
        old_name="assertEquals",
        new_name="assertEqual",
    ))
    spec.rewrite_run(
        python("assertEquals(a, b)", "assertEqual(a, b)"),
    )
```

Sections: OpenRewrite Python, How it works, Quick start, Writing a recipe, Inspecting type attribution, Against a file on disk, Running recipes with the Moderne CLI, Learn more

</details>

### barectf

Generator of ANSI C tracers which output CTF data streams

`pip install barectf` · installs (wheel) · licence: MIT License · rank 9673 · last release 2023-05-17 · [PyPI](https://pypi.org/project/barectf/) · [source](https://github.com/efficios/barectf/)

### pytest-beartype

Pytest plugin type-checking tests, fixtures, and/or your codebase with beartype: the unbearably fast near-real-time pure-Python runtime-static type-checker.

`pip install pytest-beartype` · installs (wheel) · licence: MIT License · rank 10105 · last release 2026-09-30 · [PyPI](https://pypi.org/project/pytest-beartype/)

<details><summary>README extract</summary>

<!-- ---------------( LICENSE )--------------------
Copyright (c) 2024-2026 Beartype authors.
See "LICENSE" for further details.

--------------------( MAIN )--------------------

<!-- FIXME: Also document below how users can *DISABLE* this plugin: e.g.,
 # In "pytest.ini":
 addopts = -p no:beartype ...

Features:
`pytest-beartype` configurably type-checks any combination of pytest tests,
pytest fixtures, and one or more arbitrary Python packages through
plugin-specific options either temporarily passed to the `pytest`
command *or* permanently set from within ...

...

</details>

### pydoc-markdown

Create Python API documentation in Markdown format.

`pip install pydoc-markdown` · installs (wheel) · licence: MIT License · rank 10213 · last release 2023-06-26 · [PyPI](https://pypi.org/project/pydoc-markdown/)

<details><summary>README extract</summary>

Pydoc-Markdown is a tool to create Python API documentation in Markdown format. Instead of executing your Python
code like so many other documentation tools, it parses it using docspec instead.

→ Go to the Documentation 📘

Table of Contents ...

Features:
* Understands multiple documentation styles (Sphinx, Google, Pydoc-Markdown specific) and converts them to properly
 formatted Markdown
* Can parse docstrings for variables thanks to docspec (`#:` block before or string literal after the ...

Sections: Pydoc-Markdown 📃, Features 🌟, News 📢, 4.7.0 (Undeprecating YAML configuration), 4.6.0 (Novella integration), Questions / Need help? 🤔, Projects using Pydoc-Markdown 📚

</details>

### jedi-language-server

A language server for Jedi!

`pip install jedi-language-server` · installs (wheel) · licence: MIT · rank 10604 · last release 2026-05-31 · [PyPI](https://pypi.org/project/jedi-language-server/) · [source](https://github.com/pappasam/jedi-language-server)

<details><summary>README extract</summary>

MAINTENANCE MODE: we suggest that new users consider the successor to Jedi: A Mypy-Compatible Python Language Server Built in Rust - Zuban

A Python Language Server, with additional support for computational notebooks, powered by the latest version of Jedi.

Sections: Jedi Language Server, Editor Setup, Vim and Neovim, Emacs, Visual Studio Code (vscode), Configuration, markupKindPreferred, jediSettings.autoImportModules, jediSettings.caseInsensitiveCompletion, jediSettings.debug, codeAction.nameExtractFunction, codeAction.nameExtractVariable, completion.disableSnippets, completion.resolveEagerly

</details>

### jsonschema-gentypes

Tool to generate Python types based on TypedDict from a JSON Schema

`pip install jsonschema-gentypes` · installs (wheel) · licence: BSD-2-Clause · rank 11721 · last release 2025-11-26 · [PyPI](https://pypi.org/project/jsonschema-gentypes/) · [source](https://github.com/camptocamp/jsonschema-gentypes)

<details><summary>README extract</summary>

Tools to generate Python types based on TypedDict from a JSON schema

Example:
```python
value_with_default = my_object.get('field_name', my_schema.FIELD_DEFAULT)
```

Sections: JSON Schema generate Python types, Quick start, Config file, Default, Limitations, Pre-commit hooks, OpenAPI3

</details>

### lesscpy

Python LESS compiler

`pip install lesscpy` · installs (wheel) · licence: MIT · rank 12211 · last release 2026-07-30 · [PyPI](https://pypi.org/project/lesscpy/)

<details><summary>README extract</summary>

Python LESS Compiler.

A compiler written in Python for the LESS language. For those of us not willing
or able to have node.js installed in our environment. Not all features of LESS
are supported. Some features will probably never be supported (JavaScript
evaluation). ...

Example:
```python
from io import StringIO
import lesscpy

print(lesscpy.compile(StringIO("a { border-width: 2px * 3; }"), minify=True))
```

Sections: LESSCPY, Differences from less.js, Requirements, Local setup, Build, Test, Using tox, Compiler script usage, Python usage

</details>

### pyScss

pyScss, a Scss compiler for Python

`pip install pyScss` · installs from source (sdist only) · licence: MIT License · rank 12601 · last release 2022-02-23 · [PyPI](https://pypi.org/project/pyScss/)

<details><summary>README extract</summary>

pyScss is a compiler for the Sass language, a superset of CSS3 that adds
programming capabilities and some other syntactic sugar.

Features:
95% of Sass 3.2 is supported. If it's not supported, it's a bug! Please file
a ticket.

Most of Compass 0.11 is also built in.

Example:
```python
from scss import Compiler
Compiler().compile_string("a { color: red + green; }")
```

Sections: pyScss, a Scss compiler for Python, Quickstart, Features, Further reading, Obligatory

</details>

### PyXB

Python XML Schema Bindings

`pip install PyXB` · installs from source (sdist only) · licence: Apache Software License · rank 12910 · last release 2017-09-03 · [PyPI](https://pypi.org/project/PyXB/)

<details><summary>README extract</summary>

PyXB is a pure `Python < package that generates
Python code for classes that correspond to data structures defined by
`XMLSchema < In concept it is similar to
`JAXB < for Java and `CodeSynthesis XSD
< for C++.

The major goals of PyXB are: ...

</details>

### code-puppy

Code generation agent

`pip install code-puppy` · installs (wheel) · licence: MIT License · rank 12978 · last release 2026-11-06 · [PyPI](https://pypi.org/project/code-puppy/) · [source](https://github.com/mpfaffenberger/code_puppy)

<details><summary>README extract</summary>

🐶✨The sassy AI code agent that makes IDEs look outdated ✨🐶

⭐ Star this repo if you hate expensive IDEs! ⭐

*"Who needs an IDE when you have 1024 angry puppies?"* - Someone, probably.

Features:
*This project was coded angrily in reaction to Windsurf and Cursor removing access to models and raising prices.*

*You could also run 50 code puppies at once if you were insane enough.* ...

Example:
```python
from .base_agent import BaseAgent

class MyCustomAgent(BaseAgent):
    @property
    def name(self) -> str:
        return "my-agent"

    @property
    def display_name(self) -> str:
        return "My Custom Agent ✨"

    @property
    def description(self) -> str:
        return "A custom agent for specialized tasks"

...
```

...

</details>

### dataclass-mapper

Autogenerate mappings between dataclasses

`pip install dataclass-mapper` · installs (wheel) · licence: MIT License · rank 13922 · last release 2024-02-10 · [PyPI](https://pypi.org/project/dataclass-mapper/) · [docs](https://dataclass-mapper.readthedocs.io) · [source](https://github.com/dataclass-mapper/dataclass-mapper)

<details><summary>README extract</summary>

Writing mapper methods between two similar dataclasses is boring, need to be actively maintained and are error-prone.
Much better to let this library auto-generate them for you.

The focus of this library is: ...

Features:
The current version has support for:

* Python's `dataclass` (with recursive models, custom initializers, optional types, extra-context, ...): see Supported features for the full list and examples
* Mappings between Enum classes: see Enum mappings
* ...

Example:
```python
>>> from dataclasses import dataclass

>>> @dataclass
... class Person:
...     first_name: str
...     second_name: str
...     age: int
```

Sections: dataclass-mapper, Motivation, Example, Features

</details>

### phoebusgen

Screen generator for CS-Studio Phoebus displays

`pip install phoebusgen` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 14069 · last release 2026-11-06 · [PyPI](https://pypi.org/project/phoebusgen/) · [docs](https://als-epics.github.io/phoebusgen) · [source](https://github.com/als-epics/phoebusgen)

_README extract left out: share-alike licence._

### bourbaki.application

CLIs derived directly from type signatures and docstrings years before typer existed

`pip install bourbaki.application` · installs (wheel) · licence: Apache-2.0 · rank 14350 · last release 2026-03-04 · [PyPI](https://pypi.org/project/bourbaki.application/) · [source](https://github.com/bourbaki-py/application.git)

### bourbaki.introspection

Introspection utilities for Python: types, signatures, objects, docstrings, and more

`pip install bourbaki.introspection` · installs (wheel) · licence: Apache-2.0 · rank 14380 · last release 2026-03-05 · [PyPI](https://pypi.org/project/bourbaki.introspection/) · [source](https://github.com/bourbaki-py/introspection.git)

### TatSu-LTS

TatSu takes a grammar in a variation of EBNF as input, and outputs a memoizing PEG/Packrat parser in Python.

`pip install TatSu-LTS` · installs (wheel) · licence: BSD License · rank 14390 · last release 2026-01-14 · [PyPI](https://pypi.org/project/TatSu-LTS/) · [docs](https://tatsu.readthedocs.io/en/stable/) · [source](https://github.com/dnicolodi/TatSu-LTS)

<details><summary>README extract</summary>

license|
pyversions|
fury|
actions|
docs|

 is a friendly fork of that guarantees compatibility with all supported versions of Python.
Compatibility with older Python versions is maintained as long as that does not require additional changes. ...

Example:
```python
parser = tatsu.compile(grammar)
```

Sections: Using the Tool, Documentation, Questions?, Changes

</details>

## Also in this topic

- [genson](file-formats-json.md#genson) - GenSON is a powerful, user-friendly JSON Schema generator.
- [drf-spectacular](documentation.md#drf-spectacular) - Sane and flexible OpenAPI 3 schema generation for Django REST framework
- [construct](software-development-build-tools.md#construct) - A powerful declarative symmetric parser/builder for binary data
- [PySide6-Essentials](database.md#pyside6-essentials) - Python bindings for the Qt cross-platform application and UI framework (Essentials)
- [shiboken6](database.md#shiboken6) - Python/C++ bindings helper module
- [PySide6-Addons](database.md#pyside6-addons) - Python bindings for the Qt cross-platform application and UI framework (Addons)
- [PySide6](database.md#pyside6) - Python bindings for the Qt cross-platform application and UI framework
- [ibis-framework](database-front-ends.md#ibis-framework) - The portable Python dataframe library
- [drf-spectacular-sidecar](documentation.md#drf-spectacular-sidecar) - Serve self-contained distribution builds of Swagger UI and Redoc with Django
- [libsass](internet-www-http.md#libsass) - Sass for Python: A straightforward binding of libsass for Python.
- [sqlacodegen](database.md#sqlacodegen) - Automatic model code generator for SQLAlchemy
- [drf-yasg](documentation.md#drf-yasg) - Automated generation of real Swagger/OpenAPI 2.0 schemas from Django Rest Framework code.
- [PySide6-WebEngine](database.md#pyside6-webengine) - Python bindings for the Qt cross-platform application and UI framework (WebEngine)
- [ziglang](software-development-build-tools.md#ziglang) - Zig is a general-purpose programming language and toolchain for maintaining robust, optimal, and reusable software.
- [PySide6-Pdf](database.md#pyside6-pdf) - Python bindings for the Qt cross-platform application and UI framework (Pdf)
- [seleniumbase](internet.md#seleniumbase) - SeleniumBase is a framework for web crawling, scraping, and testing. Supports pytest. CDP Mode adds stealth. Includes many tools.
- [ct3](internet-www-http.md#ct3) - Cheetah is a template engine and code generation tool
- [construct-typing](software-development-build-tools.md#construct-typing) - Extension for the python package 'construct' that adds typing features
- [pytensor](scientific-engineering-mathematics.md#pytensor) - Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
- [systemrdl-compiler](scientific-engineering-electronic-design-automation-eda.md#systemrdl-compiler) - Parse and elaborate front-end for SystemRDL 2.0
- [PyJSG](software-development.md#pyjsg) - Python JSON Schema Grammar interpreter
- [pyglove](scientific-engineering-artificial-intelligence.md#pyglove) - PyGlove: A library for manipulating Python objects.
- [chalkpy](scientific-engineering-artificial-intelligence.md#chalkpy) - Python SDK for Chalk
- [mcpforunityserver](games-entertainment.md#mcpforunityserver) - MCP for Unity Server: A Unity package for Unity Editor integration via the Model Context Protocol (MCP).
- [cxxheaderparser](software-development.md#cxxheaderparser) - Modern C++ header parser
- [Cheetah3](internet-www-http.md#cheetah3) - Cheetah is a template engine and code generation tool
- [protoc-gen-py](file-formats.md#protoc-gen-py) - 
- [zcbor](file-formats-json.md#zcbor) - Code generation and data validation using CDDL schemas
- [baron](software-development.md#baron) - Full Syntax Tree for python to make writing refactoring code a realist task
- [redbaron](software-development.md#redbaron) - Abstraction on top of baron, a FST for python to make writing refactoring code a realistic task
- [airium](database-front-ends.md#airium) - Easy and quick html builder with natural syntax correspondence (python->html). No templates needed. Serves pure pythonic library with no dependencies.
- [prophy](scientific-engineering-interface-engine-protocol-translator.md#prophy) - prophy: fast serialization protocol
- [renew](software-development.md#renew) - Gives a reproducible manner to your objects and can serialize them in 100% pythonic format.
- [Theano-PyMC](scientific-engineering-mathematics.md#theano-pymc) - Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
- [bernstein](software-development.md#bernstein) - The open-source governance layer for AI agents. No model in the coordination loop, so replaying a plan reproduces its task graph byte-identically, and run receipts are byte-identical across independent builds. Signed lineage plus an opt-in HMAC audit chain a reviewer checks offline, without rerunning it. Runs Claude Code, Codex, Gemini CLI, and 50+ CLI agents; governs any deliverable from code to research to audit evidence packs. Cluster mode, air-gap deploy.
- [PySide2](database.md#pyside2) - Python bindings for the Qt cross-platform application and UI framework
- [ctypesgen](software-development-build-tools.md#ctypesgen) - Python wrapper generator for ctypes
- [ouroboros-ai](software-development-build-tools.md#ouroboros-ai) - Pins an acceptance spec and omits any verify command or expected output from the worker's contract. Works with Claude Code, Codex CLI, OpenCode and 10 more runtimes.
- [gxformat2](software-development.md#gxformat2) - Galaxy Workflow Format 2 Descriptions
- [CppHeaderParser](software-development.md#cppheaderparser) - Parse C++ header files and generate a data structure representing the class
- [pyrig](software-development-build-tools.md#pyrig) - A Python project setup and management tool built on infrastructure as code and convention over configuration.
- [chalk-remote-call-python](scientific-engineering-artificial-intelligence.md#chalk-remote-call-python) - Chalk remote call Python runtime interface client
- [Theano](scientific-engineering-mathematics.md#theano) - Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
- [highcharts-core](internet-www-http-2.md#highcharts-core) - High-end Data Visualization for the Python Ecosystem. Official wrapper for Highcharts Core (JS).
- [edam-ontology](software-development.md#edam-ontology) - Versioned, Python packaged EDAM ontology (http://edamontology.org/) data.
- [godot-ai](games-entertainment.md#godot-ai) - Production-grade MCP server and AI tools for the Godot engine
- [buf-bin](software-development-build-tools.md#buf-bin) - Buf CLI distributed via PyPI
- [shiboken2](database.md#shiboken2) - Python / C++ bindings helper module
- [pysqlsync](database-database-engines-servers.md#pysqlsync) - Synchronize schema and large volumes of data
- [qiskit-connector](scientific-engineering-2.md#qiskit-connector) - Quantum Computing Qiskit Connector For Quantum Backend Use In Realtime
- [galaxy-release-util](software-development.md#galaxy-release-util) - Utlity for various tasks around creating Galaxy releases
- [markdown-it-reporter](software-development.md#markdown-it-reporter) - Galaxy Workflow Format 2 Descriptions
- [nunavut](scientific-engineering-2.md#nunavut) - Generate code from DSDL using Jinja2 templates.
- [licenseheaders](software-development.md#licenseheaders) - Add or change license headers for all files in a directory
