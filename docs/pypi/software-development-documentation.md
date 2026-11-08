# Software Development / Documentation

[Index](README.md) · 23 packages in this topic, 69 more listed under another topic, by downloads.

### mkdocs-get-deps

An extra command for MkDocs that infers required PyPI packages from `plugins` in mkdocs.yml

`pip install mkdocs-get-deps` · installs (wheel) · licence: MIT · rank 961 · last release 2026-03-10 · [PyPI](https://pypi.org/project/mkdocs-get-deps/) · [source](https://github.com/mkdocs/get-deps)

<details><summary>README extract</summary>

An extra command for MkDocs that infers required PyPI packages from `plugins` in mkdocs.yml.

<table>
<tr><td>Installation:</td><td>Alternatively through MkDocs itself:</td></tr>
<tr><td>

</td><td>

</td>
</tr></table>

This command guesses the Python dependencies that a MkDocs site requires in order to build. ...

Sections: mkdocs-get-deps, MkDocs' official catalog of plugins

</details>

### pyrate-limiter

Python rate limiter with pluggable algorithms and backends

`pip install pyrate-limiter` · installs (wheel) · licence: MIT · rank 1236 · last release 2026-10-20 · [PyPI](https://pypi.org/project/pyrate-limiter/) · [docs](https://pyratelimiter.readthedocs.io) · [source](https://github.com/vutran1710/PyrateLimiter)

<details><summary>README extract</summary>

A fast, async-friendly rate limiter for Python — pluggable algorithms and backends.

 Documentation ·
 Quickstart ·
 Backends ·
 Migrating from v3

> [!NOTE]
> Upgrading from v3.x? The v4 API is simpler and has breaking changes — see the Migration Guide.

Features:
- 🧮 Pluggable algorithms — sliding-window log (exact, the default), fixed window, and GCRA / token bucket (constant memory).
- ⏱️ Multiple rates at once — e.g. *5/second* and *1000/hour* on the same key. ...

Example:
```python
from pyrate_limiter import Duration, Rate, Limiter

# A Limiter with a single rate, backed by an in-memory bucket
limiter = Limiter(Rate(5, Duration.SECOND * 2))

# Blocking (default): waits until a permit is available
for i in range(6):
    limiter.try_acquire("my-resource")
    print(f"acquired {i}")

...

</details>

### markdown2

A fast and complete Python implementation of Markdown

`pip install markdown2` · installs (wheel) · licence: MIT · rank 1413 · last release 2026-03-02 · [PyPI](https://pypi.org/project/markdown2/)

<details><summary>README extract</summary>

markdown2: A fast and complete Python implementation of Markdown.

Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML. Markdown's text
format is most similar to that of plain text email, and supports
features such as headers, *emphasis*, code blocks, blockquotes, and
links. -- ...

</details>

### spdx-tools

SPDX parser and tools.

`pip install spdx-tools` · installs (wheel) · licence: Apache-2.0 · rank 1820 · last release 2026-03-13 · [PyPI](https://pypi.org/project/spdx-tools/) · [docs](https://spdx.github.io/tools-python/) · [source](https://github.com/spdx/tools-python.git)

<details><summary>README extract</summary>

CI status (Linux, macOS and Windows): [][2]

Please be aware that the upcoming 0.8 release has undergone a significant refactoring in preparation for the upcoming
SPDX v3.0 release, leading to breaking changes in the API.
Please refer to the migration guide
to update your existing code.

The main features of v0.8 are: ...

Features:
- API to create and manipulate SPDX v2.2 and v2.3 documents
- Parse, convert, create and validate SPDX files
- Supported formats: Tag/Value, RDF, JSON, YAML, XML
- Visualize the structure of a SPDX document by creating an `AGraph`. ...

Example:
```python
import logging

from license_expression import get_spdx_licensing

from spdx_tools.spdx.model import (Checksum, ChecksumAlgorithm, File,
...

</details>

### mdutils

Useful package for creating Markdown files while executing python code.

`pip install mdutils` · installs (wheel) · licence: MIT License · rank 2811 · last release 2025-10-18 · [PyPI](https://pypi.org/project/mdutils/) · [docs](http://mdutils.readthedocs.io) · [source](https://github.com/didix21/mdutils)

<details><summary>README extract</summary>

Features:
This Python package contains a set of basic tools that can help to create a markdown file while running a Python code.
Thus, if you are executing a Python code and you save the result in a text file, Why not format it? So
using files such as ...

Sections: mdutils, Overview, Features, Writing and Reading Files, Markdown, Pip, Poetry

</details>

### scalar-fastapi

FastAPI plugin to serve beautiful, interactive API documentation from OpenAPI/Swagger documents.

`pip install scalar-fastapi` · installs (wheel) · licence: MIT License · rank 3049 · last release 2026-09-25 · [PyPI](https://pypi.org/project/scalar-fastapi/) · [docs](https://scalar.com/products/api-references/integrations/fastapi) · [source](https://github.com/scalar/scalar/tree/main/integrations/fastapi)

<details><summary>README extract</summary>

<!--
 This file is auto-generated by the Scalar README generator.
 Command: pnpm --filter @scalar-internal/build-scripts start generate-readme

 Do not edit this file manually. Changes will be lost when the file is regenerated.

FastAPI plugin to serve beautiful, interactive API documentation from OpenAPI/Swagger documents. ...

Sections: Scalar API Reference Plugin for FastAPI, Documentation

</details>

### interrogate

Interrogate a codebase for docstring coverage.

`pip install interrogate` · installs (wheel) · licence: MIT License · rank 3548 · last release 2024-04-07 · [PyPI](https://pypi.org/project/interrogate/) · [docs](https://interrogate.readthedocs.io) · [source](https://github.com/econchick/interrogate)

<details><summary>README extract</summary>

Interrogate a codebase for docstring coverage.

Features:
`interrogate` checks your code base for missing docstrings.

Documentation should be as important as code itself. And it should live *within* code. ...

Example:
```python
>>> from interrogate import coverage
>>> cov = coverage.InterrogateCoverage(paths=["src"])
>>> results = cov.get_coverage()
>>> results
InterrogateResults(total=68, covered=65, missing=3)
```

Sections: `interrogate`: explain yourself, Why Do I Need This?, Requirements, Extras, Usage, Other Usage, Configuration, Command Line Options, Users of Interrogate, Interrogate in the Wild, 1.7.0 (2024-04-07), Added, Fixed, Removed

</details>

### plantuml-markdown

A PlantUML plugin for Markdown

`pip install plantuml-markdown` · installs (wheel) · licence: BSD-3-Clause · rank 4454 · last release 2026-10-26 · [PyPI](https://pypi.org/project/plantuml-markdown/)

<details><summary>README extract</summary>

* Introduction
* Installation
 * Using a local PlantUML binary
 * Using a remote server
 * Using a PlantUML server
 * Using a Kroki server
 * File inclusion management
* Plugin options
 * A note on the `priority` configuration
* Running tests
* Running tests using Docker

Introduction ...

Sections: PlantUML Extension for Python-Markdown, Using a local PlantUML binary, Using a remote server, Using a PlantUML server, Using a Kroki server, File inclusion management, A note on the `priority` configuration

</details>

### darglint

A utility for ensuring Google-style docstrings stay up to date with the source code.

`pip install darglint` · installs (wheel) · licence: MIT License · rank 4958 · last release 2021-10-18 · [PyPI](https://pypi.org/project/darglint/)

<details><summary>README extract</summary>

A functional docstring linter which checks whether a docstring's
description matches the actual function/method implementation.
*Darglint* expects docstrings to be formatted using the
Google Python Style Guide,
or Sphinx Style Guide,
or Numpy Style Guide. ...

Example:
```python
def double(x):
    # <docstring>
    return x * 2
```

Sections: Darglint, Configuration, Error Configuration, Message Template Configuration, Strictness Configuration, Ignoring common exceptions, Logging, Usage, Command Line use, Ignoring Errors in a Docstring, Type Annotations, Error Codes, Scope, Sphinx

</details>

### cognitive-complexity

Library to calculate Python functions cognitive complexity via code

`pip install cognitive-complexity` · installs from source (sdist only) · licence: MIT · rank 6147 · last release 2022-08-09 · [PyPI](https://pypi.org/project/cognitive-complexity/)

<details><summary>README extract</summary>

Library to calculate Python functions cognitive complexity via code.

Example:
```python
>>> import ast

>>> funcdef = ast.parse("""
... def f(a):
...     return a * f(a - 1)  # +1 for recursion
... """).body[0]

>>> from cognitive_complexity.api import get_cognitive_complexity
>>> get_cognitive_complexity(funcdef)
1
```

Sections: congnitive-complexity, Usage, Flake8-Cognitive-Complexity Extension, What is cognitive complexity, Realization details

</details>

### flake8-cognitive-complexity

An extension for flake8 that validates cognitive functions complexity

`pip install flake8-cognitive-complexity` · installs from source (sdist only) · licence: MIT · rank 7466 · last release 2020-08-01 · [PyPI](https://pypi.org/project/flake8-cognitive-complexity/)

<details><summary>README extract</summary>

An extension for flake8 that validates cognitive functions complexity.

Cognitive complexity is analog of cyclomatic complexity, that measure
how difficult to understand piece of code. Introduced by G. Ann Campbell
and currently used by SonarSource, CodeClimate and others. ...

Example:
```python
def f(a, b):
    if a:
        for i in range(b):
            if b:
                return 1
```

Sections: flake8-cognitive-complexity, Example, Error codes

</details>

### flake8-variables-names

A flake8 extension that helps to make more readable variables names

`pip install flake8-variables-names` · installs (wheel) · licence: MIT · rank 8043 · last release 2023-06-22 · [PyPI](https://pypi.org/project/flake8-variables-names/)

<details><summary>README extract</summary>

An extension for flake8 that helps to make more readable variables names.

We believe, that variable name should unmistakably shows, what it contains.
Thats why we try not to use varnames with only one symbol or not to use
too common names, such as `result`, `value` or `info`.

This extensions helps to detect such names. ...

Sections: flake8-variables-names, Example, Error codes

</details>

### trogon

Automatically generate a Textual TUI for your Click CLI

`pip install trogon` · installs (wheel) · licence: MIT License · rank 8121 · last release 2024-10-02 · [PyPI](https://pypi.org/project/trogon/)

<details><summary>README extract</summary>

Auto-generate friendly terminal user interfaces for command line apps.

 🎬 Video demonstration

A quick tour of a Trogon app applied to sqlite-utils.

Trogon works with the popular Click library for Python, but will support other libraries and languages in the future. ...

Features:
Command line apps reward repeated use, but they lack in *discoverability*.
If you don't use a CLI app frequently, or there are too many options to commit to memory, a Trogon TUI interface can help you (re)discover options and switches.

Example:
```python
from trogon import tui

@tui()
@click.group(...)
def cli():
    ...
```

Sections: Trogon, How it works, Screenshots, Why?, What does the name mean?, Roadmap, Quickstart, Click, Typer, Custom command name and custom help, Follow this project

</details>

### flake8-functions

A flake8 extension that checks functions

`pip install flake8-functions` · installs (wheel) · licence: MIT · rank 8865 · last release 2026-08-14 · [PyPI](https://pypi.org/project/flake8-functions/) · [source](https://github.com/best-doctor/flake8-functions)

<details><summary>README extract</summary>

An extension for flake8 to report on issues with functions.

We believe code readability is very important for a team that consists of
more than one person. One of the issues we've encountered is functions
that are more that two screens long.

The validator checks for: ...

Example:
```python
def some_long_function(
    first_parameter: int,
    second_parameter: int,
    third_parameter: int,
):
    first_parameter = (
        first_parameter +
        second_parameter +
        third_parameter
    )

    first_parameter = (
        first_parameter +
        second_parameter +
        third_parameter
    )

    first_parameter = (
...
```

Sections: flake8-functions, Example, Error codes, Code prerequisites

</details>

### comment-parser

Parse comments from various source files.

`pip install comment-parser` · installs (wheel) · licence: MIT License · rank 9072 · last release 2026-03-16 · [PyPI](https://pypi.org/project/comment-parser/)

<details><summary>README extract</summary>

Python module used to extract comments from source code files of various types.

Example:
```python
>>> from comment_parser import comment_parser
>>> # Returns a list of comment_parser.parsers.common.Comments
>>> comment_parser.extract_comments('/path/to/source_file')
>>> # Or
>>> comment_parser.extract_comments_from_str('...')
```

Sections: Comment Parser, Prerequisites, Linux/Unix, OSX and Windows, Usage, extract_comments signatures, Comments Interface, Running locally, Running tests, Running pylint, Running formatter, Deploying to PyPi

</details>

### flake8-class-attributes-order

A flake8 extension that checks classes attributes order

`pip install flake8-class-attributes-order` · installs (wheel) · licence: MIT · rank 9190 · last release 2025-03-20 · [PyPI](https://pypi.org/project/flake8-class-attributes-order/)

<details><summary>README extract</summary>

An extension for flake8 to report on wrong class attributes order and
class level logic.

The validator can extract class attribute type: docstring, property,
nested class, `GLOBAL_VAR`, etc.
If django model fields are detected, the validator can detect,
if the field is link to another table (foreign key, generic key, etc)
or not. ...

Example:
```python
DEBUG = True

class User:
    def fetch_info_from_crm(self):
        pass

    LOGIN_FIELD = 'email'  # wtf? this should be on top of class definition!

class UserNode:
    class Meta:
        model = User

    if DEBUG:  # not great idea at all
        def is_synced_with_crm(self):
            pass
```

Sections: flake8-class-attributes-order, Configuration, Strict mode, Manual order configuration, Example, Error codes

</details>

### flake8-expression-complexity

A flake8 extension that checks expressions complexity

`pip install flake8-expression-complexity` · installs (wheel) · licence: MIT · rank 9604 · last release 2026-08-14 · [PyPI](https://pypi.org/project/flake8-expression-complexity/) · [source](https://github.com/best-doctor/flake8-expression-complexity)

<details><summary>README extract</summary>

An extension for flake8 that validates expression complexity.

Splits code into expression and scores each according to how much one is complicated.
Fires an error on each expression more complex than theshold.

Default complexity is 7, can be configured via `--max-expression-complexity` option. ...

Example:
```python
if (
    (user and user.is_authorized)
    and user.subscriptions.filter(start_datelt=today, end_dategt=today).exists()
    and (
        user.total_credits_added
        - Check.objects.filter(user=user).aggregate(Sum('price'))['check__sum']
    )
    and UserAction.objects.filter(user=user).last().datetime > today - datetime.timedelta(days=10)
...
```

Sections: flake8-expression-complexity, Example, Error codes

</details>

### sphinx-issues

A Sphinx extension for linking to your project's issue tracker

`pip install sphinx-issues` · installs (wheel) · licence: MIT License · rank 9676 · last release 2026-03-13 · [PyPI](https://pypi.org/project/sphinx-issues/) · [source](https://github.com/sloria/sphinx-issues)

<details><summary>README extract</summary>

A Sphinx extension for linking to your project's issue tracker. Includes roles for linking to issues, pull requests, user profiles, with built-in support for GitHub (though this works with other services).

Sections: sphinx-issues, Example, Usage inside the documentation, Important note about :cwe: and :cve: roles, 6.0.0 (2026-03-13), 5.0.1 (2025-04-10), 5.0.0 (2024-10-11), 4.1.0 (2024-04-14), 4.0.0 (2024-01-19), 3.0.1 (2022-01-11), 3.0.0 (2022-01-10), 2.0.0 (2022-01-01), 1.2.0 (2018-12-26), 1.1.0 (2018-09-18)

</details>

### flake8-annotations-complexity

A flake8 extension that checks for type annotations complexity

`pip install flake8-annotations-complexity` · installs (wheel) · licence: MIT · rank 9929 · last release 2026-08-14 · [PyPI](https://pypi.org/project/flake8-annotations-complexity/) · [source](https://github.com/best-doctor/flake8-annotations-complexity)

<details><summary>README extract</summary>

An extension for flake8 to report on too complex type annotations.

Complex type annotations often means bad annotations usage,
wrong code decomposition or improper data structure choice.
They are also hard to read and make code look java-like.

Annotation complexity is maximum annotation nesting level. ...

Example:
```python
# test.py

def foo() -> List[int]:
    return [1]
```

Sections: flake8-annotations-complexity, Checks, Requirements, Example

</details>

### pyblock-builder

A lightweight Python library with a declarative syntax for simplifying building apps using Slack's Block Kit UI framework

`pip install pyblock-builder` · installs (wheel) · licence: BSD License · rank 11544 · last release 2024-03-13 · [PyPI](https://pypi.org/project/pyblock-builder/) · [source](https://github.com/codywb/slack-pyblock-builder)

<details><summary>README extract</summary>

PyBlock Builder is a lightweight library written in Python for constructing UI with Slack's Block Kit UI
framework. It was designed to make it easier for anyone—from hobbyists to professional devs—to create Slack apps faster
with fewer lines of code. ...

Example:
```python
from pyblock_builder.surfaces import Message
from pyblock_builder.blocks import Section, Actions
from pyblock_builder.elements import Button
```

Sections: 💡 Features, 🎯Benefits, 🔰 Getting Started, Using pip, Usage, Compatibility, Importing, Working with Messages, Working with App Home, Working with Modals

</details>

### markdown-gfm-admonition

GFM admonition syntax for Python Markdown

`pip install markdown-gfm-admonition` · installs (wheel) · licence: LGPL-3.0-or-later · rank 12428 · last release 2025-11-28 · [PyPI](https://pypi.org/project/markdown-gfm-admonition/) · [source](https://github.com/dahlia/markdown-gfm-admonition)

_README extract left out: share-alike licence._

### linuxdoc

Sphinx-doc extensions & tools to extract documentation from C/C++ source file comments.

`pip install linuxdoc` · installs (wheel) · licence: AGPL-3.0-or-later · rank 13148 · last release 2026-05-04 · [PyPI](https://pypi.org/project/linuxdoc/) · [docs](https://return42.github.io/linuxdoc) · [source](https://github.com/return42/linuxdoc)

_README extract left out: share-alike licence._

### jupyterlite-core

(no summary)

`pip install jupyterlite-core` · installs (wheel) · licence: BSD License · rank 13661 · last release 2026-10-30 · [PyPI](https://pypi.org/project/jupyterlite-core/) · [source](https://github.com/jupyterlite/jupyterlite)

<details><summary>README extract</summary>

[![docs-badge]][docs]

The `jupyterlite-core` package provides the core functionality for building JupyterLite
websites, the `jupyter-lite` CLI, and
extension points
for authoring custom addons.

Sections: jupyterlite-core, Getting Started, Documentation

</details>

## Also in this topic

- [docutils](documentation.md#docutils) - Docutils -- Python Documentation Utilities
- [Markdown](communications-email.md#markdown) - Python implementation of John Gruber's Markdown.
- [griffelib](documentation.md#griffelib) - Signatures for entire Python programs. Extract the structure, the frame, the skeleton of your project, to generate API documentation or find breaking changes in your API.
- [griffe](documentation.md#griffe) - Signatures for entire Python programs. Extract the structure, the frame, the skeleton of your project, to generate API documentation or find breaking changes in your API.
- [Sphinx](documentation.md#sphinx) - Python documentation generator
- [alabaster](documentation.md#alabaster) - A light, configurable Sphinx theme
- [mkdocs-material](documentation.md#mkdocs-material) - Documentation that simply works
- [griffecli](documentation.md#griffecli) - Signatures for entire Python programs. Extract the structure, the frame, the skeleton of your project, to generate API documentation or find breaking changes in your API.
- [mkdocs-autorefs](documentation.md#mkdocs-autorefs) - Automatically link across pages in MkDocs.
- [mkdocstrings](documentation.md#mkdocstrings) - Automatic documentation from sources, for MkDocs.
- [mkdocstrings-python](documentation.md#mkdocstrings-python) - A Python handler for mkdocstrings.
- [sphinx-rtd-theme](documentation.md#sphinx-rtd-theme) - Read the Docs theme for Sphinx
- [commonmark](documentation.md#commonmark) - Python parser for the CommonMark Markdown spec
- [furo](documentation.md#furo) - A clean customisable Sphinx documentation theme.
- [sphinx-basic-ng](documentation.md#sphinx-basic-ng) - A modern skeleton for Sphinx themes.
- [sphinx-autodoc-typehints](documentation.md#sphinx-autodoc-typehints) - Render Python type hints in Sphinx autodoc documentation
- [zensical](documentation.md#zensical) - A modern static site generator built by the creators of Material for MkDocs
- [sphinx-autobuild](documentation.md#sphinx-autobuild) - Rebuild Sphinx documentation on changes, with hot reloading in the browser.
- [mkdocs-redirects](documentation.md#mkdocs-redirects) - A MkDocs plugin for dynamic page redirects to prevent broken links
- [mkdocs-gen-files](documentation.md#mkdocs-gen-files) - MkDocs plugin to programmatically generate documentation pages during the build
- [enum-tools](documentation.md#enum-tools) - Tools to expand Python's enum module.
- [markdown-to-confluence](documentation.md#markdown-to-confluence) - Publish Markdown files to Confluence wiki
- [sphinx-tabs](documentation.md#sphinx-tabs) - Tabbed views for Sphinx
- [pdoc](documentation.md#pdoc) - API Documentation for Python Projects
- [mkdocs-literate-nav](documentation.md#mkdocs-literate-nav) - MkDocs plugin to specify the navigation in Markdown instead of YAML
- [breathe](documentation.md#breathe) - Sphinx Doxygen renderer
- [mkdocs-include-markdown-plugin](documentation.md#mkdocs-include-markdown-plugin) - Mkdocs Markdown includer plugin.
- [sphinx-reredirects](documentation.md#sphinx-reredirects) - The extension for Sphinx documentation projects that handle redirects for moved pages. It generates HTML pages with meta refresh redirects to the new page location to prevent 404 errors if you rename or move your documents.
- [mkdocs-section-index](documentation.md#mkdocs-section-index) - MkDocs plugin to allow clickable sections that lead to an index page
- [sphinx-notfound-page](documentation-sphinx.md#sphinx-notfound-page) - Sphinx extension to build a 404 page with absolute URLs
- [sphinxext-opengraph](documentation.md#sphinxext-opengraph) - Sphinx Extension to enable OGP support
- [sphinx-prompt](documentation.md#sphinx-prompt) - Sphinx directive to add unselectable prompt
- [sphinx-toolbox](documentation.md#sphinx-toolbox) - Box of handy tools for Sphinx 🧰 📔
- [sphinx-jinja2-compat](documentation.md#sphinx-jinja2-compat) - Patches Jinja2 v3 to restore compatibility with earlier Sphinx versions.
- [peakrdl-html](scientific-engineering-electronic-design-automation-eda.md#peakrdl-html) - HTML documentation generator for SystemRDL-based register models
- [autodoc_pydantic](documentation-sphinx.md#autodoc_pydantic) - Seamlessly integrate pydantic models in your Sphinx documentation.
- [markdown-include](internet-www-http.md#markdown-include) - A Python-Markdown extension which provides an 'include' function
- [sphinxext-rediraffe](documentation.md#sphinxext-rediraffe) - Sphinx Extension that redirects non-existent pages to working pages
- [peakrdl-uvm](scientific-engineering-electronic-design-automation-eda.md#peakrdl-uvm) - Generate UVM register model from compiled SystemRDL input
- [docstr-coverage](documentation.md#docstr-coverage) - Utility for examining python source files to ensure proper documentation. Lists missing docstrings, and calculates overall docstring coverage percentage rating.
- [mkdocs-click](documentation.md#mkdocs-click) - An MkDocs extension to generate documentation for Click command line applications
- [citeproc-py](documentation.md#citeproc-py) - Citations and bibliography formatter
- [nvidia-sphinx-theme](documentation.md#nvidia-sphinx-theme) - A Sphinx theme for NVIDIA projects
- [pdoc3](documentation.md#pdoc3) - Auto-generate API documentation for Python projects.
- [shibuya](documentation.md#shibuya) - A clean, responsive, and customizable Sphinx documentation theme with light/dark mode.
- [exhale](documentation-sphinx.md#exhale) - Automatic C++ library API documentation generator using Doxygen, Sphinx, and
- [mkdocs-same-dir](documentation.md#mkdocs-same-dir) - ProperDocs plugin to allow placing properdocs.yml in the same directory as documentation
- [sphinxcontrib-towncrier](documentation-sphinx.md#sphinxcontrib-towncrier) - An RST directive for injecting a Towncrier-generated changelog draft containing fragments for the unreleased (next) project version
- [jsonschema2md](documentation.md#jsonschema2md) - Convert JSON Schema to human-readable Markdown documentation
- [property-manager](documentation-sphinx.md#property-manager) - Useful property variants for Python programming (required properties, writable properties, cached properties, etc)
- [sphinx-intl](documentation.md#sphinx-intl) - Sphinx utility that make it easy to translate and to apply translation.
- [sphinx-pyproject](documentation.md#sphinx-pyproject) - Move some of your Sphinx configuration into pyproject.toml
- [sphinx-press-theme](documentation.md#sphinx-press-theme) - A Sphinx-doc theme based on Vuepress
- [sphinx-jsonschema](documentation-sphinx.md#sphinx-jsonschema) - Sphinx extension to display JSON Schema
- [kolo](software-development.md#kolo) - Kolo is a text-based Python debugger for AI agents. Capture every executed function call, return value, local variable, HTTP request, and more in greppable trace files.
- [sphobjinv](documentation.md#sphobjinv) - Sphinx objects.inv Inspection/Manipulation Tool
- [sphinx-favicon](documentation.md#sphinx-favicon) - Sphinx Extension adding support for custom favicons
- [git-changelog](documentation.md#git-changelog) - Automatic Changelog generator using Jinja2 templates.
- [markdown-callouts](documentation.md#markdown-callouts) - Markdown extension: a classier syntax for admonitions
- [pydoctor](documentation.md#pydoctor) - API doc generator.
- [sphinx-bootstrap-theme](internet.md#sphinx-bootstrap-theme) - Sphinx Bootstrap Theme.
- [json-source-map](software-development-disassemblers.md#json-source-map) - Calculate the source map for a JSON document.
- [python-docs-theme](documentation.md#python-docs-theme) - The Sphinx theme for the CPython docs and related projects
- [mmdr](multimedia-graphics.md#mmdr) - Fast native Mermaid diagram rendering (Rust-based, no browser required) with two backends: mermaid-rs-renderer and merman
- [blockdiag](software-development.md#blockdiag) - blockdiag generates block-diagram image from text
- [mkdocs-kroki-plugin](documentation.md#mkdocs-kroki-plugin) - MkDocs plugin for Kroki-Diagrams
- [griffe-typingdoc](documentation.md#griffe-typingdoc) - Griffe extension for PEP 727 – Documentation Metadata in Typing.
- [mkdocs-rss-plugin](documentation.md#mkdocs-rss-plugin) - MkDocs plugin to generate RSS and JSON feeds using Mkdocs site configuration, git log and Mkdocs pages'meta.
- [Pallets-Sphinx-Themes](documentation.md#pallets-sphinx-themes) - Sphinx themes for Pallets and related projects.
