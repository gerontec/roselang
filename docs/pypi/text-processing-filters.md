# Text Processing / Filters

[Index](README.md) · 9 packages in this topic, 44 more listed under another topic, by downloads.

### Pygments

Pygments is a syntax highlighting package written in Python.

`pip install Pygments` · installs (wheel) · licence: BSD-2-Clause · rank 14 · last release 2026-08-17 · [PyPI](https://pypi.org/project/Pygments/) · [docs](https://pygments.org/docs) · [source](https://github.com/pygments/pygments)

<details><summary>README extract</summary>

Pygments is a syntax highlighting package written in Python.

It is a generic syntax highlighter suitable for use in code hosting, forums,
wikis or other applications that need to prettify source code. Highlights
are: ...

</details>

### pandocfilters

Utilities for writing pandoc filters in python

`pip install pandocfilters` · installs (wheel) · licence: BSD License · rank 418 · last release 2024-01-18 · [PyPI](https://pypi.org/project/pandocfilters/)

<details><summary>README extract</summary>

A python module for writing pandoc filters

Pandoc filters
are pipes that read a JSON serialization of the Pandoc AST
from stdin, transform it in some way, and write it to stdout. ...

Example:
```python
# !/usr/bin/env python

"""
Pandoc filter to convert all regular text to uppercase.
Code, link URLs, etc. are not affected.
"""

from pandocfilters import toJSONFilter, Str

def caps(key, value, format, meta):
  if key == 'Str':
    return Str(value.upper())

if name == "main":
  toJSONFilter(caps)
```

Sections: pandocfilters, What are pandoc filters?, Compatibility, Available functions, How to use, Examples, API documentation

</details>

### titlecase

Python Port of John Gruber's titlecase.pl

`pip install titlecase` · installs from source (sdist only) · licence: MIT License · rank 3120 · last release 2023-09-23 · [PyPI](https://pypi.org/project/titlecase/) · [source](https://github.com/ppannuto/python-titlecase)

<details><summary>README extract</summary>

This filter changes a given text to Title Caps, and attempts to be clever
about SMALL words like a/an/the in the input.
The list of "SMALL words" which are not capped comes from the New York
Times Manual of Style, plus some others like 'vs' and 'v'.

The filter employs some heuristics to guess abbreviations that don't need conversion. ...

Example:
```python
>>> from titlecase import titlecase
>>> titlecase('a thing')
'A Thing'
```

Sections: Titlecase, Usage, Command Line Usage, Limitations

</details>

### latexcodec

A lexer and codec to work with LaTeX code in Python.

`pip install latexcodec` · installs (wheel) · licence: MIT License · rank 3448 · last release 2025-06-17 · [PyPI](https://pypi.org/project/latexcodec/)

<details><summary>README extract</summary>

* Instead of using latexcodec, I encourage you to consider pylatexenc instead, which is far superior:

.. |ci| image::
 :target:
 :alt: ci

.. |codecov| image::
 :target:
 :alt: codecov

The codec provides a convenient way of going between text written in
LaTeX and unicode. ...

</details>

### text2num

Parse and convert numbers written in French, Spanish, English, Portuguese, German, Dutch, Danish, or Italian into their digit representation.

`pip install text2num` · installs (wheel) · licence: MIT License · rank 3605 · last release 2026-08-21 · [PyPI](https://pypi.org/project/text2num/) · [docs](https://text2num.readthedocs.io) · [source](https://github.com/allo-media/text2num)

<details><summary>README extract</summary>

A fast and robust text2num converter library a library for recognizing, parsing and transcribing into digits (base 10) numbers expressed in natural language. It works on strings as well as on custom token lists.

No IA involved: it is low on resources (and energy!) consumption and the latency is very small. ...

Example:
```python
>>> from text_to_num import text2num
>>> text2num('quatre-vingt-quinze', "fr")
95

>>> text2num('nonante-cinq', "fr")
95

>>> text2num('mille neuf cent quatre-vingt dix-neuf', "fr")
1999

>>> text2num('dix-neuf cent quatre-vingt dix-neuf', "fr")
1999

>>> text2num("cinquante et un million cinq cent soixante dix-huit mille trois cent deux", "fr")
...
```

...

</details>

### smartypants

Python with the SmartyPants

`pip install smartypants` · installs (wheel) · licence: BSD License · rank 9181 · last release 2025-06-17 · [PyPI](https://pypi.org/project/smartypants/)

<details><summary>README extract</summary>

smartypants is a Python fork of SmartyPants_.

__ SmartyPantsPerl

Example:
```python
import smartypants

text = '"SmartyPants" is smart, so is <code>smartypants</code> -- a Python port'
print(smartypants.smartypants(text))
```

Sections: smartypants, Quick usage, More information

</details>

### mdx-include

Python Markdown extension to include local or remote files

`pip install mdx-include` · installs (wheel) · licence: BSD License · rank 12104 · last release 2022-07-26 · [PyPI](https://pypi.org/project/mdx-include/)

<details><summary>README extract</summary>

Include extension for Python Markdown. It lets you include local or remote (downloadable) files into your markdown at arbitrary positions.

This project is motivated by markdown-include and provides the same functionalities with some extras.

Inclusion for local file is by default recursive and for remote file non-recursive. ...

Example:
```python
text = r"""
some text {! test1.md !} some more text {! test2.md | utf-8 !}

Escaping will give you the exact literal \{! some_file !}

If you escape, then the backslash will be removed.

If you want the backslash too, then provide two more: \\\{! some_file !}
"""
md = markdown.Markdown(extensions=['mdx_include'])
html = md.convert(text)
print(html)
```

...

</details>

### rcslice

Slice a list of sliceables (1 indexed, start and end index both are inclusive)

`pip install rcslice` · installs (wheel) · licence: BSD License · rank 12233 · last release 2018-09-27 · [PyPI](https://pypi.org/project/rcslice/)

<details><summary>README extract</summary>

This package provides Python module to slice a list of sliceables (1 indexed, both start and end index are inclusive). Helps to slice file content line by line or column by column or a combination of both.

Example:
```python
from rcslice import RowSlice

rs = RowSlice()

list_of_sliceables = rs.slice(list_of_sliceables, '1-2,2.4-4.5,8-2.6')
```

Sections: Usage, Slicing syntax, Examples

</details>

### toolwrapper

A base class for wrapping text-processing tools

`pip install toolwrapper` · installs from source (sdist only) · licence: MIT License · rank 12687 · last release 2020-05-13 · [PyPI](https://pypi.org/project/toolwrapper/)

<details><summary>README extract</summary>

A Python module for interfacing with external text tools.

This module provides a single class `toolwrapper.ToolWrapper`. Objects of
this class will launch subprocesses and communicate with them via stdin/stdout
pipes.

Copyright ® 2015-2019 Luís Gomes <luismsgomes@gmail.com>.

Sections: toolwrapper, TODO

</details>

## Also in this topic

- [Markdown](communications-email.md#markdown) - Python implementation of John Gruber's Markdown.
- [nltk](scientific-engineering.md#nltk) - Natural Language Toolkit
- [Unidecode](text-processing.md#unidecode) - ASCII transliterations of Unicode text
- [pymdown-extensions](internet-www-http.md#pymdown-extensions) - Extension pack for Python Markdown.
- [courlan](internet-www-http.md#courlan) - Clean, filter and sample URLs to optimize data collection – includes spam, content type and language filters.
- [jusText](internet-www-http.md#justext) - Heuristic based boilerplate removal tool
- [mkdocs-material-extensions](internet-www-http.md#mkdocs-material-extensions) - Extension pack for Python Markdown and MkDocs Material.
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [RTFDE](communications-email.md#rtfde) - A library for extracting HTML content from RTF encapsulated HTML as commonly found in the exchange MSG email format.
- [markdown2](software-development-documentation.md#markdown2) - A fast and complete Python implementation of Markdown
- [pypandoc](text-processing.md#pypandoc) - Thin wrapper for pandoc.
- [xhtml2pdf](documentation.md#xhtml2pdf) - PDF generator using HTML and CSS
- [publicsuffixlist](internet-name-service-dns.md#publicsuffixlist) - publicsuffixlist implement
- [pypandoc-binary](text-processing.md#pypandoc-binary) - Thin wrapper for pandoc.
- [rjsmin](internet-www-http.md#rjsmin) - Javascript Minifier
- [rcssmin](internet-www-http.md#rcssmin) - CSS Minifier
- [coloraide](internet-www-http.md#coloraide) - A color library for Python.
- [confusable-homoglyphs](text-processing.md#confusable-homoglyphs) - Detect confusable usage of unicode homoglyphs, prevent homograph attacks.
- [jsmin](internet-www-http.md#jsmin) - JavaScript minifier.
- [plantuml-markdown](software-development-documentation.md#plantuml-markdown) - A PlantUML plugin for Markdown
- [empy](software-development-interpreters.md#empy) - A templating system for Python.
- [pyhwp](software-development-libraries-2.md#pyhwp) - hwp file format parser
- [mdit-plain](text-processing.md#mdit-plain) - A plain text renderer for markdown-it-py
- [textwrap3](software-development-libraries-2.md#textwrap3) - textwrap from Python 3.6 backport (plus a few tweaks)
- [ansiwrap](software-development-libraries-2.md#ansiwrap) - textwrap, but savvy to ANSI colors and styles
- [ripgrep-bin](terminals.md#ripgrep-bin) - ripgrep is a line-oriented search tool that recursively searches the current directory for a regex pattern while respecting gitignore rules.
- [bitmath](communications-file-sharing.md#bitmath) - Pythonic module for representing and manipulating file sizes with different prefix notations (file size unit conversion)
- [citeurl](internet-www-http.md#citeurl) - an extensible tool to process legal citations in text
- [markdown-include](internet-www-http.md#markdown-include) - A Python-Markdown extension which provides an 'include' function
- [stop-words](software-development.md#stop-words) - Get list of common stop words in various languages in Python
- [beautysh](software-development-libraries-3.md#beautysh) - A Bash beautifier for the masses.
- [kreuzberg](office-business.md#kreuzberg) - High-performance document intelligence library for Python. Extract text, metadata, and structured data from PDFs, Office documents, images, and 88+ formats. Powered by Rust core for 10-50x speed improvements.
- [fastnumbers](scientific-engineering-information-analysis.md#fastnumbers) - Super-fast and clean conversions to numbers.
- [fortune](games-entertainment.md#fortune) - Python version of old BSD Unix fortune program
- [sumy](education.md#sumy) - Module for automatic summarization of text documents and HTML pages.
- [panflute](software-development-build-tools.md#panflute) - Pythonic Pandoc filters
- [click-extra](documentation-sphinx.md#click-extra) - 🌈 Drop-in replacement for Click to make user-friendly and colorful CLI
- [breadability](internet-www-http-2.md#breadability) - Port of Readability HTML parser in Python
- [gitignorefile](software-development-libraries-4.md#gitignorefile) - A spec-compliant `.gitignore` parser for Python
- [navi-sanitize](security.md#navi-sanitize) - Deterministic sanitization for untrusted text: strips invisible and control characters, applies NFKC and replaces common homoglyphs. No dependencies.
- [markdown-gfm-admonition](software-development-documentation.md#markdown-gfm-admonition) - GFM admonition syntax for Python Markdown
- [ansi2txt](terminals.md#ansi2txt) - ansi to plain text converter
- [konlpy](scientific-engineering-2.md#konlpy) - Python package for Korean natural language processing.
- [gitmatch](software-development-version-control.md#gitmatch) - Gitignore-style path matching
