# Documentation / Sphinx

[Index](README.md) · 19 packages in this topic, 38 more listed under another topic, by downloads.

### docstring-parser

Parse Python docstrings in reST, Google and Numpydoc format

`pip install docstring-parser` · installs (wheel) · licence: MIT License · rank 129 · last release 2026-04-14 · [PyPI](https://pypi.org/project/docstring-parser/) · [source](https://github.com/rr-/docstring_parser)

<details><summary>README extract</summary>

Parse Python docstrings. Currently support ReST, Google, Numpydoc-style and
Epydoc docstrings.

Example usage:

Read API Documentation.

Example:
```python
>>> from docstring_parser import parse
>>>
>>>
>>> docstring = parse(
...     '''
...     Short description
...
...     Long description spanning multiple lines
...     - First line
...     - Second line
...     - Third line
...
...     :param name: description 1
...     :param int priority: description 2
...     :param str sender: description 3
...
```

</details>

### word2number

Convert number words eg. three hundred and forty two to numbers (342).

`pip install word2number` · installs from source (sdist only) · licence: MIT License · rank 2542 · last release 2017-06-02 · [PyPI](https://pypi.org/project/word2number/)

<details><summary>README extract</summary>

This is a Python module to convert number words (eg. twenty one) to numeric digits (21). It works for positive numbers upto the range of 999,999,999,999 (i.e. billions).

Example:
```python
from word2number import w2n
```

Sections: Word to Number, Usage, Bugs/Errors

</details>

### python-arango

Python Driver for ArangoDB

`pip install python-arango` · installs (wheel) · licence: MIT License · rank 2689 · last release 2026-10-27 · [PyPI](https://pypi.org/project/python-arango/)

<details><summary>README extract</summary>

Python driver for ArangoDB, a scalable multi-model
database natively supporting documents, graphs and search.

If you're interested in using asyncio, please check python-arango-async.

- ArangoDB version 3.11+
- Python version 3.10+

Example:
```python
from arango import ArangoClient

# Initialize the client for ArangoDB.
client = ArangoClient(hosts="

# Connect to "_system" database as root user.
sys_db = client.db("_system", username="root", password="passwd")

# Create a new database named "test".
sys_db.create_database("test")

# Connect to "test" database as root user.
...
```

Sections: Python-Arango, Requirements, Getting Started

</details>

### docstring-to-markdown

On the fly conversion of Python docstrings to markdown

`pip install docstring-to-markdown` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 3603 · last release 2025-05-02 · [PyPI](https://pypi.org/project/docstring-to-markdown/) · [source](https://github.com/python-lsp/docstring-to-markdown)

_README extract left out: share-alike licence._

### docstring-parser-fork

Parse Python docstrings in reST, Google and Numpydoc format

`pip install docstring-parser-fork` · installs (wheel) · licence: MIT License · rank 3750 · last release 2026-07-03 · [PyPI](https://pypi.org/project/docstring-parser-fork/) · [source](https://github.com/rr-/docstring_parser)

<details><summary>README extract</summary>

This is a fork of docstring_parser.

This fork fixes bugs that the upstream library has not fixed, and it also
offers additional functionalities. To inspect the difference between this
fort and the upstream, go to CHANGELOG.md and read the
entries that start with "(Fork)".

Parse Python docstrings. ...

Example:
```python
>>> from docstring_parser import parse
>>>
>>>
>>> docstring = parse(
...     '''
...     Short description
...
...     Long description spanning multiple lines
...     - First line
...     - Second line
...     - Third line
...
...     :param name: description 1
...     :param int priority: description 2
...     :param str sender: description 3
...
```

</details>

### nbsphinx

Jupyter Notebook Tools for Sphinx

`pip install nbsphinx` · installs (wheel) · licence: MIT · rank 4235 · last release 2025-11-28 · [PyPI](https://pypi.org/project/nbsphinx/) · [docs](https://nbsphinx.readthedocs.io/) · [source](https://github.com/spatialaudio/nbsphinx/)

<details><summary>README extract</summary>

`nbsphinx` is a Sphinx extension that provides a source parser for
`*.ipynb` files.
Custom Sphinx directives are used to show Jupyter Notebook code cells (and of
course their results) in both HTML and LaTeX output.
Un-evaluated notebooks -- i.e. ...

</details>

### sphinx-lint

Check for stylistic and formal issues in .rst and .py files included in the documentation.

`pip install sphinx-lint` · installs (wheel) · licence: PSF-2.0 · rank 5619 · last release 2025-11-19 · [PyPI](https://pypi.org/project/sphinx-lint/) · [source](https://github.com/sphinx-contrib/sphinx-lint)

<details><summary>README extract</summary>

Sphinx Lint is based on rstlint.py from
CPython.

Sphinx Lint should:

- be reasonably fast so it's comfortable to use as a linter in your editor.
- be usable on a single file.
- not give any false positives (probably a utopia, but let's try).
- not spend too much effort finding errors that sphinx-build already finds (or can easily find). ...

Sections: Sphinx Lint, What is Sphinx Lint, what is it not?, Using Sphinx Lint, Known issues, Releasing

</details>

### sphinx-notfound-page

Sphinx extension to build a 404 page with absolute URLs

`pip install sphinx-notfound-page` · installs (wheel) · licence: MIT License · rank 5916 · last release 2025-01-28 · [PyPI](https://pypi.org/project/sphinx-notfound-page/) · [docs](https://sphinx-notfound-page.readthedocs.io/) · [source](https://github.com/readthedocs/sphinx-notfound-page)

<details><summary>README extract</summary>

Create a custom 404 page with absolute URLs hardcoded.

Sections: sphinx-notfound-page, Configuration, Documentation, Thanks

</details>

### sphinx-sitemap

Sitemap generator for Sphinx

`pip install sphinx-sitemap` · installs (wheel) · licence: MIT · rank 6018 · last release 2025-10-06 · [PyPI](https://pypi.org/project/sphinx-sitemap/) · [docs](https://sphinx-sitemap.readthedocs.io/en/latest/index.html) · [source](https://github.com/jdillard/sphinx-sitemap)

<details><summary>README extract</summary>

A Sphinx extension to generate multiversion and multilanguage
sitemaps.org compliant sitemaps for the HTML version of your Sphinx
documentation.

PyPI versionConda ForgeDownloadsParallel Safe|
Code style: BlackDocs BuildCI Workflow|

See sphinx-sitemap documentation for installation and configuration instructions.

Sections: Sphinx Sitemap Generator Extension, Documentation

</details>

### sphinx-last-updated-by-git

Get the "last updated" time for each Sphinx page from Git

`pip install sphinx-last-updated-by-git` · installs (wheel) · licence: BSD License · rank 6084 · last release 2024-08-11 · [PyPI](https://pypi.org/project/sphinx-last-updated-by-git/)

<details><summary>README extract</summary>

This is a little Sphinx extension that does exactly that.
It also checks for included files and other dependencies and
uses their "last updated" time if it's more recent.
For each file, the "author date" of the Git commit where it was last changed
is taken to be its "last updated" time. Uncommitted changes are ignored. ...

</details>

### autodoc_pydantic

Seamlessly integrate pydantic models in your Sphinx documentation.

`pip install autodoc_pydantic` · installs (wheel) · licence: MIT License · rank 6587 · last release 2024-04-27 · [PyPI](https://pypi.org/project/autodoc_pydantic/) · [docs](https://github.com/mansenfranzen/autodoc_pydantic) · [source](https://github.com/mansenfranzen/autodoc_pydantic)

<details><summary>README extract</summary>

You love pydantic ❤ and you want to
document your models and configuration settings with sphinx?

Perfect, let's go. But wait, sphinx' autodoc
does not integrate too well with pydantic models 😕.

Don't worry - just `pip install autodoc_pydantic` ☺.

- 💬 provides default values, alias and constraints for model fields ...

Sections: 🌟 Features, 📄 Documentation

</details>

### exhale

Automatic C++ library API documentation generator using Doxygen, Sphinx, and

`pip install exhale` · installs (wheel) · licence: BSD License · rank 9091 · last release 2024-01-21 · [PyPI](https://pypi.org/project/exhale/) · [docs](https://exhale.readthedocs.io/en/latest/) · [source](https://github.com/svenevs/exhale)

<details><summary>README extract</summary>

Automatic C++ library API documentation generator using Doxygen, Sphinx, and Breathe.
Exhale revives Doxygen's class, file, and page hierarchies in reStructuredText documents
to make these hierarchies available in Sphinx documented projects. ...

Sections: Exhale, Is it For Me?, See it in Action

</details>

### sphinxcontrib-towncrier

An RST directive for injecting a Towncrier-generated changelog draft containing fragments for the unreleased (next) project version

`pip install sphinxcontrib-towncrier` · installs (wheel) · licence: BSD License · rank 9263 · last release 2025-02-28 · [PyPI](https://pypi.org/project/sphinxcontrib-towncrier/)

<details><summary>README extract</summary>

An RST directive for injecting a Towncrier-generated changelog draft
containing fragments for the unreleased (next) project version.

Sections: sphinxcontrib-towncrier, How to use this?, Does anybody actually use this?

</details>

### property-manager

Useful property variants for Python programming (required properties, writable properties, cached properties, etc)

`pip install property-manager` · installs (wheel) · licence: MIT License · rank 9725 · last release 2020-03-02 · [PyPI](https://pypi.org/project/property-manager/)

<details><summary>README extract</summary>

The `property-manager` package defines several custom property variants for
Python programming including required properties, writable properties, cached
properties, etc. It's currently tested on Python 2.7, 3.5, 3.6, 3.7, 3.8 and
PyPy. For usage instructions please refer to the documentation.

Example:
```python
from random import random
from property_manager import writable_property

class WritablePropertyDemo(object):

    @writable_property
    def change_me(self):
        return random()
```

Sections: Usage, Writable properties, Required properties, Cached properties, Properties based on environment variables, The `PropertyManager` class, Similar projects, Distinguishing features, Contact

</details>

### sphinx-jsonschema

Sphinx extension to display JSON Schema

`pip install sphinx-jsonschema` · installs (wheel) · licence: GPL-3.0-only · rank 10474 · last release 2026-10-25 · [PyPI](https://pypi.org/project/sphinx-jsonschema/)

_README extract left out: share-alike licence._

### sphinx-immaterial

Adaptation of mkdocs-material theme for the Sphinx documentation system

`pip install sphinx-immaterial` · installs (wheel) · licence: MIT License · rank 10700 · last release 2026-11-08 · [PyPI](https://pypi.org/project/sphinx-immaterial/) · [docs](https://jbms.github.io/sphinx-immaterial) · [source](https://github.com/jbms/sphinx-immaterial)

<details><summary>README extract</summary>

This theme is an adaptation of the popular mkdocs-material theme for the Sphinx documentation tool.

This theme is regularly maintained to stay up to date with the upstream
mkdocs-material repository.
The HTML templates, JavaScript, and styles from the mkdocs-material theme are incoroprated directly
with mostly minor modifications. ...

Example:
```python
{# Import the theme's layout. #}
{% extends '!layout.html' %}

{%- block extrahead %}
{# Add custom things to the head HTML tag #}
{# Call the parent block #}
{{ super() }}
{%- endblock %}
```

Sections: Sphinx-Immaterial Theme, Configuration, Customizing the layout, Differences from mkdocs-material

</details>

### censys

An easy-to-use and lightweight API wrapper for Censys APIs (censys.io).

`pip install censys` · installs (wheel) · licence: Apache-2.0 · rank 11341 · last release 2026-08-28 · [PyPI](https://pypi.org/project/censys/) · [docs](https://censys-python.rtfd.io) · [source](https://github.com/censys/censys-python)

<details><summary>README extract</summary>

> [!WARNING]
> DEPRECATION NOTICE: The Censys Search v1 and v2 APIs will be deprecated soon. Please migrate to the new Censys Platform.
> - 📖 New API Documentation:
> - 📦 New Python SDK: Install with `pip install censys-platform` -
> - 🖥️ New CLI Tool (`cencli`):
> - ⚠️ If you plan to use the new CLI, you will need to uninstall this package's CLI ...

Features:
- Search Censys data
- Bulk Certificate lookups
- Download Bulk Data
- Manage assets, events, and seeds in Censys ASM
- Command-line interface

Sections: Censys Python Library, Features, Getting Started, Examples, Documentation, Resources

</details>

### click-extra

🌈 Drop-in replacement for Click to make user-friendly and colorful CLI

`pip install click-extra` · installs (wheel) · licence: GPL-2.0-or-later · rank 11346 · last release 2026-11-06 · [PyPI](https://pypi.org/project/click-extra/) · [docs](https://kdeldycke.github.io/click-extra/) · [source](https://github.com/kdeldycke/click-extra)

_README extract left out: share-alike licence._

### SnakeMD

A markdown generation library for Python.

`pip install SnakeMD` · installs (wheel) · licence: MIT License · rank 11919 · last release 2026-05-30 · [PyPI](https://pypi.org/project/SnakeMD/) · [docs](https://www.snakemd.io/en/latest/docs/) · [source](https://github.com/TheRenegadeCoder/SnakeMD)

<details><summary>README extract</summary>

SnakeMD is your ticket to generating Markdown in Python. To prove it to you, we've generated this entire README using SnakeMD. See readme.py for how it was done. To get started, download and install SnakeMD:

In the remainder of this document, we'll show you all of the things this library can do. ...

Example:
```python
def _paragraph(doc: Document):
    doc.add_paragraph("I think. Therefore, I am.")
```

Sections: Welcome to SnakeMD, Paragraphs, Links, Images, Lists, Ordered List, Unordered List, Checklist, Nested Lists, Tables, Code Blocks, Quotes, Horizontal Rule, Raw

</details>

## Also in this topic

- [Sphinx](documentation.md#sphinx) - Python documentation generator
- [alabaster](documentation.md#alabaster) - A light, configurable Sphinx theme
- [sphinxcontrib-serializinghtml](documentation.md#sphinxcontrib-serializinghtml) - sphinxcontrib-serializinghtml is a sphinx extension which outputs "serialized" HTML files (json and pickle)
- [sphinxcontrib-jsmath](documentation.md#sphinxcontrib-jsmath) - sphinxcontrib-jsmath is a sphinx extension which renders displayed maths in HTML via JavaScript
- [sphinxcontrib-htmlhelp](documentation.md#sphinxcontrib-htmlhelp) - sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files
- [sphinxcontrib-applehelp](documentation.md#sphinxcontrib-applehelp) - sphinxcontrib-applehelp is a Sphinx extension which outputs Apple help books
- [sphinxcontrib-qthelp](documentation.md#sphinxcontrib-qthelp) - sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp documents
- [sphinxcontrib-devhelp](documentation.md#sphinxcontrib-devhelp) - sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp documents
- [sphinxcontrib-jquery](documentation.md#sphinxcontrib-jquery) - Extension to include jQuery on newer Sphinx releases
- [sphinx-autodoc-typehints](documentation.md#sphinx-autodoc-typehints) - Render Python type hints in Sphinx autodoc documentation
- [sphinx-autobuild](documentation.md#sphinx-autobuild) - Rebuild Sphinx documentation on changes, with hot reloading in the browser.
- [sphinx-click](documentation.md#sphinx-click) - Sphinx extension that automatically documents click applications
- [enum-tools](documentation.md#enum-tools) - Tools to expand Python's enum module.
- [sphinx-argparse](documentation.md#sphinx-argparse) - A sphinx extension that automatically documents argparse commands and options
- [sphinx-tabs](documentation.md#sphinx-tabs) - Tabbed views for Sphinx
- [breathe](documentation.md#breathe) - Sphinx Doxygen renderer
- [sphinx-reredirects](documentation.md#sphinx-reredirects) - The extension for Sphinx documentation projects that handle redirects for moved pages. It generates HTML pages with meta refresh redirects to the new page location to prevent 404 errors if you rename or move your documents.
- [sphinxcontrib-websupport](documentation.md#sphinxcontrib-websupport) - sphinxcontrib-websupport provides a Python API to easily integrate Sphinx documentation into your Web application
- [sphinxext-opengraph](documentation.md#sphinxext-opengraph) - Sphinx Extension to enable OGP support
- [sphinx-prompt](documentation.md#sphinx-prompt) - Sphinx directive to add unselectable prompt
- [sphinx-toolbox](documentation.md#sphinx-toolbox) - Box of handy tools for Sphinx 🧰 📔
- [sphinx-jinja2-compat](documentation.md#sphinx-jinja2-compat) - Patches Jinja2 v3 to restore compatibility with earlier Sphinx versions.
- [sphinxext-rediraffe](documentation.md#sphinxext-rediraffe) - Sphinx Extension that redirects non-existent pages to working pages
- [sphinxcontrib-confluencebuilder](documentation.md#sphinxcontrib-confluencebuilder) - Sphinx extension to build Atlassian Confluence Storage Markup
- [docstr-coverage](documentation.md#docstr-coverage) - Utility for examining python source files to ensure proper documentation. Lists missing docstrings, and calculates overall docstring coverage percentage rating.
- [sphinxcontrib-openapi](documentation.md#sphinxcontrib-openapi) - OpenAPI (fka Swagger) spec renderer for Sphinx
- [m2r2](documentation.md#m2r2) - Markdown to RST converter.
- [nvidia-sphinx-theme](documentation.md#nvidia-sphinx-theme) - A Sphinx theme for NVIDIA projects
- [sphinx-intl](documentation.md#sphinx-intl) - Sphinx utility that make it easy to translate and to apply translation.
- [sphinx-pyproject](documentation.md#sphinx-pyproject) - Move some of your Sphinx configuration into pyproject.toml
- [sphinxcontrib-apidoc](documentation.md#sphinxcontrib-apidoc) - A Sphinx extension for running 'sphinx-apidoc' on each build
- [esbonio](documentation.md#esbonio) - A language server for sphinx/docutils based documentation projects.
- [swagger-plugin-for-sphinx](documentation.md#swagger-plugin-for-sphinx) - Sphinx plugin which renders a OpenAPI specification with Swagger
- [sphobjinv](documentation.md#sphobjinv) - Sphinx objects.inv Inspection/Manipulation Tool
- [sphinx-favicon](documentation.md#sphinx-favicon) - Sphinx Extension adding support for custom favicons
- [lazydocs](documentation.md#lazydocs) - Generate markdown API documentation for Google-style Python docstring.
- [sphinxcontrib-typer](documentation.md#sphinxcontrib-typer) - Auto generate docs for typer commands.
- [Pallets-Sphinx-Themes](documentation.md#pallets-sphinx-themes) - Sphinx themes for Pallets and related projects.
