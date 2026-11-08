# Text Processing / Markup

[Index](README.md) · 40 packages in this topic, 176 more listed under another topic, by downloads.

### defusedxml

XML bomb protection for Python stdlib modules

`pip install defusedxml` · installs (wheel) · licence: Python Software Foundation License · rank 135 · last release 2021-03-08 · [PyPI](https://pypi.org/project/defusedxml/)

<details><summary>README extract</summary>

Christian Heimes <christian@python.org>

The results of an attack on a vulnerable XML library can be fairly dramatic.
With just a few hundred Bytes of XML data an attacker can occupy several
Gigabytes of memory within seconds. An attacker can also keep
CPUs busy for a long time with a small to medium size request. ...

Example:
```python
>>> from xml.etree.ElementTree import parse
>>> et = parse(xmlfile)
```

...

</details>

### xmltodict

Makes working with XML feel like you are working with JSON

`pip install xmltodict` · installs (wheel) · licence: MIT · rank 279 · last release 2026-02-22 · [PyPI](https://pypi.org/project/xmltodict/)

<details><summary>README extract</summary>

`xmltodict` is a Python module that makes working with XML feel like you are working with JSON, as in this "spec":

Example:
```python
>>> print(json.dumps(xmltodict.parse("""
...
...
...      elements
...      more elements
...
...
...      element as well
...
...
...  """), indent=4))
{
    "mydocument": {
        "@has": "an attribute",
        "and": {
            "many": [
                "elements",
                "more elements"
            ]
        },
        "plus": {
...
```

Sections: xmltodict, Streaming mode, Roundtripping, API Reference, xmltodict.parse(), xmltodict.unparse(), Examples, Selective force_cdata, Selective force_list, Ok, how do I get it?, Using pypi, Using conda, RPM-based distro (Fedora, RHEL, …), Arch Linux

</details>

### mistune

A sane and fast Markdown parser with useful plugins and renderers

`pip install mistune` · installs (wheel) · licence: BSD License · rank 358 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mistune/) · [docs](https://mistune.lepture.com/) · [source](https://github.com/lepture/mistune)

<details><summary>README extract</summary>

A fast yet powerful Python Markdown parser with renderers and plugins.

Features:
Convert Markdown to HTML with ease:

`create_markdown()` escapes raw HTML by default. The legacy
`mistune.html(trusted_markdown_text)` helper enables raw HTML and several
plugins; use it only for trusted input or sanitize its output externally.

Example:
```python
import mistune

markdown = mistune.create_markdown()
markdown(your_markdown_text)
```

Sections: Mistune v3, Overview, Useful Links

</details>

### chevron

Mustache templating language renderer

`pip install chevron` · installs (wheel) · licence: MIT License · rank 1100 · last release 2021-01-02 · [PyPI](https://pypi.org/project/chevron/)

<details><summary>README extract</summary>

A python implementation of the mustache templating language.

Why chevron?

I'm glad you asked!

Chevron runs in less than half the time of pystache (Which is not even up to date on the spec).
And in about 70% the time of Stache (A 'trimmed' version of mustache, also not spec compliant).

The flake8 command is run by travis to ensure consistency.

Example:
```python
import chevron

chevron.render('Hello, {{ mustache }}!', {'mustache': 'World'})
```

Sections: chevron is fast, chevron is pep8, chevron is spec compliant, chevron is Python 2 and 3 compatible

</details>

### firecrawl-anydoc

Convert documents (doc, docx, odt, rtf, epub, pdf, presentations, spreadsheets, csv) to GitHub-Flavored Markdown

`pip install firecrawl-anydoc` · installs (wheel) · licence: MIT · rank 1216 · last release 2026-08-27 · [PyPI](https://pypi.org/project/firecrawl-anydoc/) · [source](https://github.com/firecrawl/anydoc)

<details><summary>README extract</summary>

Convert Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, and PDF files into clean GitHub-Flavored Markdown. Python bindings for the anydoc Rust crate, built by Firecrawl. Also available as a hosted API through Firecrawl Parse, which adds our OCR models for the scanned pages anydoc can't read on its own. ...

Example:
```python
import anydoc

# From a file path:
markdown = anydoc.to_markdown("report.docx")

# From bytes, with the format detected from the content:
markdown = anydoc.to_markdown_bytes(data)

# Or name it, which signature-less formats (CSV) need:
markdown = anydoc.to_markdown_bytes(data, "csv")

...
```

Sections: firecrawl-anydoc, Usage, Scanned pages, Errors, Format detection, Images and embedded objects

</details>

### xmlsec

Python bindings for the XML Security Library

`pip install xmlsec` · installs (wheel) · licence: MIT · rank 1345 · last release 2026-10-29 · [PyPI](https://pypi.org/project/xmlsec/) · [docs](https://xmlsec.readthedocs.io) · [source](https://github.com/xmlsec/python-xmlsec)

<details><summary>README extract</summary>

Python bindings for the XML Security
Library.

Documentation for `xmlsec` can be found at
xmlsec.readthedocs.io.

Sections: python-xmlsec, Documentation, Usage, Requirements, Linux (Debian), Linux (CentOS), Linux (Fedora), Mac, Alpine, Troubleshooting, `lxml & xmlsec libxml2 library version mismatch`, Windows, Building from source

</details>

### restructuredtext-lint

reStructuredText linter

`pip install restructuredtext-lint` · installs (wheel) · licence: Public Domain · rank 2109 · last release 2025-11-23 · [PyPI](https://pypi.org/project/restructuredtext-lint/)

<details><summary>README extract</summary>

reStructuredText linter

This was created out of frustration with PyPI; it sucks finding out your reST is invalid after uploading it. It is being developed in junction with a Sublime Text linter.

Example:
```python
import restructuredtext_lint
errors = restructuredtext_lint.lint("""
# Hello World
""")

# `errors` will be list of system messages
# [<system_message: <paragraph...><literal_block...>>]
errors[0].message  # Title underline too short.
```

Sections: restructuredtext-lint, Getting Started, CLI Utility, Other tools, PyPI issues, Breaking changes in 2.0.0, Documentation, Extension, Sphinx, Examples

</details>

### jupytext

Jupyter notebooks as Markdown documents, Julia, Python or R scripts

`pip install jupytext` · installs (wheel) · licence: MIT License · rank 2205 · last release 2026-10-04 · [PyPI](https://pypi.org/project/jupytext/) · [docs](https://jupytext.org) · [source](https://github.com/jupytext/jupytext)

<details><summary>README extract</summary>

<!-- INDEX-START -->

Have you always wished Jupyter notebooks were plain text documents? Wished you could edit them in your favorite IDE? And get clear and meaningful diffs when doing version control? Then, Jupytext may well be the tool you're looking for! ...

Example:
```python
# %% [markdown]
# This is a markdown cell

# %%
def f(x):
  return 3*x+1
```

Sections: Jupytext, Text Notebooks, Paired Notebooks, Command line, Sample use cases, Notebooks under version control, Collaborating on notebooks with Git, Editing or refactoring a notebook in an IDE, More resources

</details>

### parsel

Parsel is a library to extract data from HTML and XML using XPath and CSS selectors

`pip install parsel` · installs (wheel) · licence: BSD-3-Clause · rank 2224 · last release 2026-09-28 · [PyPI](https://pypi.org/project/parsel/) · [docs](https://parsel.readthedocs.io/en/latest/) · [source](https://github.com/scrapy/parsel)

<details><summary>README extract</summary>

Parsel is a BSD-licensed Python library to extract data from HTML, JSON, and
XML documents.

It supports:

- CSS and XPath expressions for HTML and XML documents

- JMESPath expressions for JSON documents

- Regular expressions

Find the Parsel online documentation at

Example (open online demo):

Example:
```python
>>> from parsel import Selector
>>> text = """
...
...
...
# Hello, Parsel!

...
...
- Link 1

...
- Link 2

...
...         {"a": ["b", "c"]}
...
... """
>>> selector = Selector(text=text)
>>> selector.css("h1::text").get()
'Hello, Parsel!'
>>> selector.xpath("//h1/text()").re(r"\w+")
['Hello', 'Parsel']
>>> for li in selector.css("ul > li"):
...
```

</details>

### bibtexparser

Bibtex parser for python 3

`pip install bibtexparser` · installs (wheel) · licence: MIT · rank 3239 · last release 2026-10-02 · [PyPI](https://pypi.org/project/bibtexparser/) · [source](https://github.com/sciunto-org/python-bibtexparser)

<details><summary>README extract</summary>

Welcome to python-bibtexparser, a parser for `.bib` files with a long history and wide adoption.

Bibtexparser is available in two versions: V1 and V2. V2 is the current, recommended version and the default you get from PyPI. It provides an overall more robust and faster experience than v1, and is where all development and maintenance effort goes. ...

Example:
```python
# Parsing a bibtex string with default values
bib_database = bibtexparser.parse_string(bibtex_string)
# Converting it back to a bibtex string, again with default values
new_bibtex_string = bibtexparser.write_string(bib_database)
```

Sections: python-bibtexparser, Documentation, Advantages of `v2` compared to `v1`, TLDR Usage Example, Architecture and Terminology, Library, A Splitter, Middleware, Writer, About

</details>

### pybtex

A BibTeX-compatible bibliography processor in Python

`pip install pybtex` · installs (wheel) · licence: MIT · rank 3451 · last release 2026-04-03 · [PyPI](https://pypi.org/project/pybtex/) · [docs](https://docs.pybtex.org/) · [source](https://codeberg.org/pybtex/pybtex)

<details><summary>README extract</summary>

Pybtex reads citation information from a file and
produces a formatted bibliography. BibTeX style files are supported.
Alternatively it is possible to write styles in Python.

Pybtex currently understands the following bibliography formats:

- BibTeX

- BibTeXML

- YAML-based format ...

Sections: BibTeX-compatible bibliography processor in Python, Synopsis, Description, See also

</details>

### django-htmlmin

HTML minifier for Python frameworks (not only Django, despite the name).

`pip install django-htmlmin` · installs from source (sdist only) · licence: BSD License · rank 3796 · last release 2019-03-18 · [PyPI](https://pypi.org/project/django-htmlmin/)

<details><summary>README extract</summary>

django-html is an HTML minifier for Python, with full support for HTML 5. It
supports Django, Flask and many other Python web frameworks. It also provides a
command line tool, that can be used for static websites or deployment scripts.

Features:
One of the important points on client side optimization is to minify HTML. With
minified HTML code, you reduce the size of the data transferred from the server
to the client, which results in faster load times.

Example:
```python
from htmlmin.decorators import minified_response

@minified_response
def home(request):
    return render_to_response('home.html')
```

...

</details>

### mdx-truly-sane-lists

Extension for Python-Markdown that makes lists truly sane. Custom indents for nested lists and fix for messy linebreaks.

`pip install mdx-truly-sane-lists` · installs (wheel) · licence: MIT License · rank 3849 · last release 2022-07-19 · [PyPI](https://pypi.org/project/mdx-truly-sane-lists/)

<details><summary>README extract</summary>

An extension for Python-Markdown that makes lists truly sane. Features custom indents for nested lists and fix for messy linebreaks and paragraphs between lists.

Features:
* `nested_indent` option: Custom indent for nested lists. Defaults to `2`. Doesn't mess with code indents, which is still 4.

* `truly_sane` option: Makes linebreaks and paragraphs in lists behave as usually expected by user. ...

Example:
```python
from markdown import markdown

# Default config is truly_sane: True, nested_indent: 2
markdown(text='some text', extensions=['mdx_truly_sane_lists'])
```

Sections: Mdx Truly Sane Lists, Features, Pypi, Directly from git, Usage, Screenshots and examples, HTML

</details>

### htmlmin2

An HTML Minifier

`pip install htmlmin2` · installs (wheel) · licence: BSD License · rank 4066 · last release 2023-03-14 · [PyPI](https://pypi.org/project/htmlmin2/)

<details><summary>README extract</summary>

> :warning: This is a fork of htmlmin. You can install this work with `pip install htmlmin2`.

A configurable HTML Minifier with safety features.

Documentation:

</details>

### mf2py

Microformats parser

`pip install mf2py` · installs (wheel) · licence: MIT License · rank 4459 · last release 2026-09-18 · [PyPI](https://pypi.org/project/mf2py/)

<details><summary>README extract</summary>

`mf2py` is a Python microformats parser with full support for `microformats2`, backwards-compatible support for `microformats1` and experimental support for `metaformats`.

Example:
```python
>>> import mf2py
```

Sections: Welcome 👋, Quickstart 🚀, Parse an HTML Document from a file or string, Parse an HTML Document from a URL, Experimental Options, `expose_dom`, `metaformats`, `filter_roots`, Advanced Usage, Filter by Microformat Type, JSON Output, Breaking Changes in `mf2py` 2.0, Notes 📝

</details>

### mwparserfromhell

MWParserFromHell is a parser for MediaWiki wikicode

`pip install mwparserfromhell` · installs from source (sdist only) · licence: MIT · rank 4467 · last release 2025-07-01 · [PyPI](https://pypi.org/project/mwparserfromhell/) · [docs](https://mwparserfromhell.readthedocs.io/) · [source](https://github.com/earwig/mwparserfromhell)

<details><summary>README extract</summary>

mwparserfromhell (the *MediaWiki Parser from Hell*) is a Python package
that provides an easy-to-use and outrageously powerful parser for MediaWiki
wikicode. It supports Python 3.9+.

Developed by Earwig with contributions from Σ, Legoktm, and others.
Full documentation is available on ReadTheDocs. Development occurs on GitHub.

Example:
```python
>>> import mwparserfromhell
>>> wikicode = mwparserfromhell.parse(text)
```

Sections: mwparserfromhell, Usage, Limitations, Integration

</details>

### htmlmin

An HTML Minifier

`pip install htmlmin` · installs from source (sdist only) · licence: BSD License · rank 4600 · last release 2017-12-29 · [PyPI](https://pypi.org/project/htmlmin/)

<details><summary>README extract</summary>

A configurable HTML Minifier with safety features.

Documentation:

</details>

### html5tagger

Pythonic HTML generation/templating (no template files)

`pip install html5tagger` · installs (wheel) · licence: MIT License; Public Domain · rank 4841 · last release 2026-07-10 · [PyPI](https://pypi.org/project/html5tagger/) · [source](https://github.com/sanic-org/html5tagger)

<details><summary>README extract</summary>

If you're looking for a more efficient and streamlined way to generate HTML5, look no further than html5tagger! This is a super fast HTML generation module that can run faster than Jinja. But the main difference is you'll be writing HTML tags with Python syntax, from your code. ...

Example:
```python
E.p("Powered by:").br.a(href="...")("html5tagger")
```

Sections: HTML5 templating with Pure Python, Intro, Templating, Nesting, Escaping and special methods, Name mangling and boolean attributes, Appending classes, CSS selector style attributes, Conditional elements, Preformatted HTML, Performance

</details>

### faicons

An interface to Font-Awesome for use in Shiny.

`pip install faicons` · installs (wheel) · licence: MIT License · rank 5293 · last release 2024-01-16 · [PyPI](https://pypi.org/project/faicons/) · [source](https://github.com/rstudio/py-faicons)

<details><summary>README extract</summary>

An interface to Font-Awesome for use in Shiny for Python.

This package currently uses Font-Awesome 6.2.0.

Example:
```python
from faicons import icon_svg
icon_svg("play")
```

Sections: Font Awesome for Shiny, Usage

</details>

### hyperscript

HyperText with Python

`pip install hyperscript` · installs (wheel) · licence: MIT License · rank 5687 · last release 2024-10-22 · [PyPI](https://pypi.org/project/hyperscript/)

<details><summary>README extract</summary>

Hyperscript is a lightweight library that allows you to write HTML with Python. It is heavily inspired by HyperScript.

Example:
```python
>>> print(h("p", "Hello world!"))
Hello world!
```

Sections: Hyperscript, Example usage

</details>

### multimark

Python bindings to cmark: CommonMark parsing and rendering (HTML, LaTeX, man, XML)

`pip install multimark` · installs (wheel) · licence: MIT AND BSD-2-Clause · rank 5805 · last release 2026-10-06 · [PyPI](https://pypi.org/project/multimark/)

<details><summary>README extract</summary>

The multimark package has Python bindings to cmark-gfm, the C reference implementation of CommonMark with GitHub Flavored Markdown extensions.

Renders Markdown to HTML, LaTeX, groff man, XML, and normalized CommonMark: all from a single, lightweight package.

Features:
Several Python packages wrap cmark or provide CommonMark parsing. Here's how they compare:

| | multimark | cmarkgfm | commonmark.py | ...

Example:
```python
from multimark import markdown_to_html, markdown_to_latex

html = markdown_to_html("Hello, *world*!")
# 'Hello, world!
\n'

latex = markdown_to_latex("Hello, *world*!")
# '\\textbf{Hello}, \\emph{world}!\n'
```

Sections: Quick Start, Renderers, Options, GFM Extensions, All Renderer Parameters, Why multimark?

</details>

### xmltojson

A Python module and cli tool to quickly convert xml text or files into json

`pip install xmltojson` · installs (wheel) · licence: Apache Software License · rank 5987 · last release 2024-10-20 · [PyPI](https://pypi.org/project/xmltojson/) · [source](https://github.com/shanahanjrs/xmltojson)

<details><summary>README extract</summary>

Python library and cli tool for converting XML to JSON

Example:
```python
...:     my_xml = f.read()

'{"name": "John"}'
```

Sections: xmltojson, Usage, Command line, Converting an XML file and sending the output to STDOUT, Send output to a file, xmltojson can also read from STDIN, Library

</details>

### arelle-release

An open source XBRL platform.

`pip install arelle-release` · installs (wheel) · licence: Apache-2.0 · rank 6167 · last release 2026-10-31 · [PyPI](https://pypi.org/project/arelle-release/) · [docs](https://arelle.readthedocs.io/en/latest/) · [source](https://github.com/Arelle/Arelle/)

<details><summary>README extract</summary>

Features:
- Fully-featured XBRL processor with GUI, CLI, Python API and Web Service API.

 - XBRL v2.1 and XBRL Dimensions v1.0
 - XBRL Formula v1.0
 - Taxonomy Packages v1.0
 - xBRL-JSON v1.0 and xBRL-CSV v1.0
 - Inline XBRL v1.1
 - Units Registry v1.0 ...

Sections: Arelle, Description, Documentation, Features, Arelle Within Other Products, EDGAR or EFM Validations, Bug Report or Feature Request, How-To and General XBRL Questions, Email

</details>

### prettierfier

Intelligently pretty-print HTML/XML with inline tags.

`pip install prettierfier` · installs (wheel) · licence: MIT License · rank 6702 · last release 2019-07-22 · [PyPI](https://pypi.org/project/prettierfier/)

<details><summary>README extract</summary>

While I love Beautiful Soup as a parser, `BeautifulSoup.prettify()` adds a linebreak between *every* tag.
This results in unwanted white space between tags that should be inline, like ``, ``, ``, etc:

Introducing GitHub®

vs.

 Introducing GitHub


This module parses HTML/XML as a raw string to more intelligently format tags.

Example:
```python
import prettierfier

ugly_html = """
    Introducing GitHub

        ®

"""

pretty_html = prettierfier.prettify_html(ugly_html)
print(pretty_html)

# Output
>>> Introducing GitHub®
```

Sections: prettierfier, Functions, Example, Links

</details>

### xmldiff

Creates diffs of XML files

`pip install xmldiff` · installs (wheel) · licence: MIT License · rank 7029 · last release 2026-06-11 · [PyPI](https://pypi.org/project/xmldiff/) · [source](https://github.com/Shoobx/xmldiff)

<details><summary>README extract</summary>

`xmldiff` is a library and a command-line utility for making diffs out of XML.
This may seem like something that doesn't need a dedicated utility,
but change detection in hierarchical data is very different from change detection in flat data. ...

Example:
```python
from lxml import etree
from xmldiff import main, formatting

diff = main.diff_files('file1.xml', 'file2.xml',
                       formatter=formatting.XMLFormatter())
```

Sections: xmldiff, Quick usage, Changes from `xmldiff` 0.6/1.x

</details>

### htpy

htpy - HTML in Python

`pip install htpy` · installs (wheel) · licence: MIT · rank 7338 · last release 2026-05-22 · [PyPI](https://pypi.org/project/htpy/) · [docs](https://htpy.dev) · [source](https://github.com/pelme/htpy)

<details><summary>README extract</summary>

htpy is a library that makes writing HTML in plain Python fun and efficient,
without a template language.

Define HTML in Python:

And Get HTML:

Features:
- Leverage static types: Use mypy or pyright to type check your code.

- Great debugging: Avoid cryptic stack traces from templates. Use your favorite Python debugger.

- Easy to extend: There is no special way to define template tags/filters. ...

Example:
```python
from htpy import body, h1, head, html, li, title, ul

menu = ["egg+bacon", "bacon+spam", "eggs+spam"]

print(
    html[
        head[title["Today's menu"]],
        body[
            h1["Menu"],
            ul(".menu")[(li[item] for item in menu)],
        ],
    ]
)
```

...

</details>

### leptris

Python bindings for libleptris — fast XML 1.0 parsing and XPath 1.0, shaped like lxml

`pip install leptris` · installs (wheel) · licence: MIT · rank 8645 · last release 2026-11-06 · [PyPI](https://pypi.org/project/leptris/) · [source](https://github.com/leptris/leptris-py)

<details><summary>README extract</summary>

`leptris` wraps the libleptris
C API (XML 1.0 parsing, XPath 1.0) using `cffi` in ABI mode, with a
required C accelerator for Element allocation and the hot accessors
(`tag`, `text`, `attrib`, `get`, indexing, sibling navigation and
plain-path XPath evaluation). Wheels ship it compiled; sdist builds
require a C compiler. ...

Example:
```python
from leptris import fromstring, tostring

root = fromstring("
- Ulysses")

root.tag                                # "library"
root[0].get("id")                       # "1"
root[0].attrib                          # {"id": "1", "lang": "en"}
root[0].text                            # "Ulysses"

root.xpath("count(//book)")             # 1.0
...
```

...

</details>

### pynliner

Python CSS-to-inline-styles conversion tool for HTML using BeautifulSoup and cssutils

`pip install pynliner` · installs (wheel) · licence: MIT License · rank 8646 · last release 2017-01-10 · [PyPI](https://pypi.org/project/pynliner/)

### mathml2omml

(no summary)

`pip install mathml2omml` · installs (wheel) · licence: MIT License · rank 8741 · last release 2019-11-24 · [PyPI](https://pypi.org/project/mathml2omml/)

<details><summary>README extract</summary>

Pure Python library to convert MathML to OMML (Office Math Markup Language).

Example:
```python
import mathml2omml

mathml = '<math><mi>x</mi><mo>+</mo><mi>y</mi></math>'
omml = math2omml.convert(mathml)
```

Sections: math2omml, Usage

</details>

### psims

Writers and controlled vocabulary manager for PSI-MS's mzML and mzIdentML standards

`pip install psims` · installs (wheel) · licence: Apache Software License · rank 10332 · last release 2026-08-08 · [PyPI](https://pypi.org/project/psims/) · [source](https://github.com/mobiusklein/psims)

<details><summary>README extract</summary>

Prototype work for a unified API for writing Proteomics Standards Initiative standardized formats
for mass spectrometry:

1. mzML
2. mzIdentML
3. mzMLb

See the Documenation for more information

Example:
```python
from psims.mzml.writer import MzMLWriter

# Load the data to write
scans = get_scan_data()

with MzMLWriter(open("out.mzML", 'wb'), close=True) as out:
    # Add default controlled vocabularies
    out.controlled_vocabularies()
    # Open the run and spectrum list sections
    with out.run(id="my_analysis"):
...
```

Sections: psims, mzML Minimal Example, Citing

</details>

### quill-delta

Python port of the quill.js delta library that enables operational transformation with aditional functionality for rendering html

`pip install quill-delta` · installs (wheel) · licence: MIT License · rank 11249 · last release 2020-10-20 · [PyPI](https://pypi.org/project/quill-delta/) · [source](https://github.com/forgeworks/delta-py)

<details><summary>README extract</summary>

Python port of the javascript Delta library for QuillJS:

Some basic pythonizing has been done, but mostly it works exactly like the above library.

There is no other python specific documentation at this time, sorry. Please see the tests
for reference examples.

Sections: Delta (Python Port), Rendering HTML in Python, Setup, Tests

</details>

### jxmlease

jxmlease converts between XML and intelligent Python data structures.

`pip install jxmlease` · installs (wheel) · licence: MIT License · rank 11257 · last release 2020-05-29 · [PyPI](https://pypi.org/project/jxmlease/)

### jira2markdown

Convert text from JIRA markup to Markdown using parsing expression grammars

`pip install jira2markdown` · installs (wheel) · licence: MIT · rank 12754 · last release 2026-10-07 · [PyPI](https://pypi.org/project/jira2markdown/) · [source](https://github.com/catcombo/jira2markdown)

<details><summary>README extract</summary>

Features:
`jira2markdown` is a text converter from JIRA markup to YouTrack Markdown using parsing expression grammars. The Markdown implementation in YouTrack follows the CommonMark specification with extensions. ...

Example:
```python
from jira2markdown import convert

convert("Some *Jira text* formatting [example|
# >>> Some Jira text formatting example.

# To convert user mentions provide a mapping Jira internal account id to username
# as a second argument to convert function
convert(
...
```

Sections: Overview, Prerequisites, Command line tool, Usage, Conversion tables, Headings, Text Effects, Text Breaks, Links, Lists, Images, Tables, Advanced Formatting, Customization

</details>

### xmlformatter

Format and compress XML documents

`pip install xmlformatter` · installs (wheel) · licence: MIT · rank 12790 · last release 2026-05-06 · [PyPI](https://pypi.org/project/xmlformatter/)

<details><summary>README extract</summary>

xmlformatter is an Open Source Python package, which provides formatting of XML documents. *It is the replacement for the Python 2 package XmlFormatter, which has been removed from PyPi completely (see Notes)*. ...

Example:
```python
class xmlformatter.Formatter(compress ::= False, selfclose ::= False, indent ::= 2, indent_char ::= " ", inline ::= True, encoding_input ::= None, encoding_output ::= None, preserve ::= [ ], blanks ::= False)
```

Sections: xmlformatter, Formatting Rules, Class, Members, Methods, Cmd, Notes

</details>

### z3c.pt

Fast ZPT engine.

`pip install z3c.pt` · installs (wheel) · licence: ZPL-2.1 · rank 13129 · last release 2026-10-21 · [PyPI](https://pypi.org/project/z3c.pt/) · [docs](https://z3cpt.readthedocs.io/) · [source](https://github.com/zopefoundation/z3c.pt)

<details><summary>README extract</summary>

This is a fast implementation of the ZPT template engine for Zope 3
which uses Chameleon to compile templates to byte-code.

The package provides application support equivalent to
`zope.pagetemplate`.

Sections: z3c.pt, 5.2 (2026-10-21), 5.1 (2025-06-19), 5.0 (2025-04-14), 4.5 (2025-03-24), 4.4 (2024-08-07), 4.3 (2024-02-01), 4.2 (2024-01-31), 4.1 (2024-01-09), 4.0 (2023-03-27), 3.3.1 (2021-12-17), 3.3.0 (2020-03-31), 3.2.0 (2019-01-05), 3.1.0 (2017-10-17)

</details>

### DocumentTemplate

Document Templating Markup Language (DTML)

`pip install DocumentTemplate` · installs (wheel) · licence: ZPL-2.1 · rank 13136 · last release 2026-08-20 · [PyPI](https://pypi.org/project/DocumentTemplate/) · [docs](https://zope.readthedocs.io/en/latest/zopebook/index.html) · [source](https://github.com/zopefoundation/DocumentTemplate)

<details><summary>README extract</summary>

This package implements the original Document Templating Markup Language
(DTML). It uses custom SGML tags to implement simple programmatic features,
such as variable replacement, conditional logic and loops.

Inside Zope environments page templates and TAL have superseded DTML for most
use cases.

Features:
- Add support for Python 3.5, 3.6, 3.7, 3.8.

- Make the rendering encoding configurable to fix rendering on Zope 4.
 (#43)

- Add _contains__` support to DocumentTemplate.TemplateDict.

Sections: DocumentTemplate, 5.4 (2026-08-20), 5.3 (2026-02-25), 5.2 (2026-02-23), 5.1 (2026-01-19), 5.0 (2025-11-27), 4.6 (2023-11-13), 4.5 (2023-09-18), 4.4 (2022-01-12), 4.3 (2022-12-21), 4.2 (2022-12-16), 4.1 (2022-09-20), 4.0 (2020-11-12), 3.2.2 (2020-02-04)

</details>

### gravitasml

(no summary)

`pip install gravitasml` · installs (wheel) · licence: MIT License · rank 13419 · last release 2025-12-26 · [PyPI](https://pypi.org/project/gravitasml/)

<details><summary>README extract</summary>

A lightweight Python library for parsing custom markup languages, built and used by AutoGPT

GravitasML is purpose-built for parsing simple markup structures, particularly LLM-generated outputs.

By design, it excludes XML features that can introduce security risks:
- No DTD processing - Prevents billion laughs and quadratic blowup attacks ...

Example:
```python
from gravitasml.token import tokenize
from gravitasml.parser import Parser

# Parse simple markup
markup = "GravitasML"
tokens = tokenize(markup)
parser = Parser(tokens)
result = parser.parse()

print(result)  # {'name': 'GravitasML'}
```

...

</details>

### nestedtext

human readable and writable data interchange format

`pip install nestedtext` · installs (wheel) · licence: MIT License · rank 13709 · last release 2025-12-26 · [PyPI](https://pypi.org/project/nestedtext/) · [docs](https://nestedtext.org) · [source](https://github.com/kenkundert/nestedtext)

<details><summary>README extract</summary>

| Authors: Ken & Kale Kundert
| Version: 3.8
| Released: 2025-12-26
| Documentation: nestedtext.org
| Please post all questions, suggestions, and bug reports to GitHub.

*NestedText* is a file format for holding structured data. ...

Sections: NestedText — Structured Data for Humans, Typical Applications, Configuration, Structured Code, ```, expected type: regex

</details>

### meld3

Unmaintained templating system used by old versions of Supervisor

`pip install meld3` · installs (wheel) · licence: BSD-derived (http://www.repoze.org/LICENSE.txt) · rank 14405 · last release 2020-04-08 · [PyPI](https://pypi.org/project/meld3/)

<details><summary>README extract</summary>

No further development of the meld3 package is planned. The meld3 package
should be considered unmaintained as of April 2020. Since 2007, meld3
received only minimal updates to keep compatible with newer Python versions.
It was only maintained because it was a dependency of the Supervisor package. ...

</details>

### pytidylib

Python wrapper for HTML Tidy (tidylib) on Python 2 and 3

`pip install pytidylib` · installs from source (sdist only) · licence: MIT License · rank 14948 · last release 2016-11-16 · [PyPI](https://pypi.org/project/pytidylib/)

<details><summary>README extract</summary>

PyTidyLib is a Python package that wraps the HTML Tidy library. This
allows you, from Python code, to "fix" invalid (X)HTML markup. Some of the
library's many capabilities include: ...

Example:
```python
from tidylib import tidy_document
document, errors = tidy_document('''fõo ''',
  options={'numeric-entities':1})
print document
print errors
```

Sections: Changes, Small example of use, Docs

</details>

## Also in this topic

- [PyYAML](software-development-libraries.md#pyyaml) - YAML parser and emitter for Python
- [MarkupSafe](internet-www-http.md#markupsafe) - Safely add untrusted strings to HTML/XML markup.
- [Jinja2](internet-www-http.md#jinja2) - A very fast and expressive template engine.
- [markdown-it-py](software-development-libraries.md#markdown-it-py) - Python port of markdown-it. Markdown parsing, done right!
- [lxml](software-development-libraries.md#lxml) - Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.
- [beautifulsoup4](software-development-libraries.md#beautifulsoup4) - Screen-scraping library
- [docstring-parser](documentation-sphinx.md#docstring-parser) - Parse Python docstrings in reST, Google and Numpydoc format
- [ruamel.yaml](software-development-libraries.md#ruamelyaml) - ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order
- [docutils](documentation.md#docutils) - Docutils -- Python Documentation Utilities
- [Markdown](communications-email.md#markdown) - Python implementation of John Gruber's Markdown.
- [reportlab](printing.md#reportlab) - The Reportlab Toolkit
- [mdit-py-plugins](software-development-libraries.md#mdit-py-plugins) - Collection of plugins for markdown-it-py
- [weasyprint](internet-www-http.md#weasyprint) - The Awesome Document Factory
- [tinyhtml5](software-development-libraries.md#tinyhtml5) - HTML parser based on the WHATWG HTML specification
- [strictyaml](software-development-libraries.md#strictyaml) - Strict, typed YAML parser
- [html5lib](software-development-libraries.md#html5lib) - HTML parser based on the WHATWG HTML specification
- [pymdown-extensions](internet-www-http.md#pymdown-extensions) - Extension pack for Python Markdown.
- [Sphinx](documentation.md#sphinx) - Python documentation generator
- [fpdf2](multimedia-graphics.md#fpdf2) - Simple & fast PDF generation for Python
- [htmldate](internet-www-http.md#htmldate) - Fast and robust extraction of original and updated publication dates from URLs and web pages.
- [pyyaml-env-tag](software-development-libraries.md#pyyaml-env-tag) - A custom YAML tag for referencing environment variables in YAML files.
- [feedparser](software-development-libraries.md#feedparser) - Universal feed parser, handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds
- [trafilatura](internet-www-http.md#trafilatura) - Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extraction, output as CSV, JSON, HTML, MD, TXT, XML.
- [mkdocs-material](documentation.md#mkdocs-material) - Documentation that simply works
- [jusText](internet-www-http.md#justext) - Heuristic based boilerplate removal tool
- [mkdocs-material-extensions](internet-www-http.md#mkdocs-material-extensions) - Extension pack for Python Markdown and MkDocs Material.
- [jsonpath-python](software-development-libraries.md#jsonpath-python) - A lightweight and powerful JSONPath implementation for Python
- [colorclass](software-development-libraries.md#colorclass) - Colorful worry-free console applications for Linux, Mac OS X, and Windows.
- [RTFDE](communications-email.md#rtfde) - A library for extracting HTML content from RTF encapsulated HTML as commonly found in the exchange MSG email format.
- [cssutils](internet.md#cssutils) - A CSS Cascading Style Sheets library for Python
- [markdown2](software-development-documentation.md#markdown2) - A fast and complete Python implementation of Markdown
- [pylatexenc](scientific-engineering.md#pylatexenc) - Simple LaTeX parser providing latex-to-unicode and unicode-to-latex conversion
- [elementpath](software-development-libraries.md#elementpath) - XPath 1.0/2.0/3.0/3.1 parsers and selectors for ElementTree and lxml
- [xmlschema](software-development-libraries.md#xmlschema) - An XML Schema validator and decoder
- [latex2mathml](scientific-engineering-mathematics.md#latex2mathml) - Pure Python library for LaTeX to MathML conversion
- [selectolax](internet.md#selectolax) - A fast HTML5 parser with CSS selectors, written in Cython, using the Lexbor engine.
- [svglib](documentation.md#svglib) - A pure-Python library for reading and converting SVG
- [myst-parser](software-development-libraries.md#myst-parser) - An extended [CommonMark](https://spec.commonmark.org/) compliant parser,
- [PyYAML-ft](software-development-libraries.md#pyyaml-ft) - YAML parser and emitter for Python with support for free-threading
- [intervaltree](scientific-engineering-artificial-intelligence.md#intervaltree) - Editable interval tree data structure for Python 2 and 3
- [doclang](software-development-libraries.md#doclang) - DocLang reference toolkit
- [terminaltables](software-development-libraries.md#terminaltables) - Generate simple tables in terminals from a nested list of strings.
- [djlint](software-development-quality-assurance.md#djlint) - HTML template linter and formatter (Django, Jinja, Twig, Nunjucks, Handlebars, Mustache, Liquid, Go templates, Angular, Tera, Askama, Mako)
- [xhtml2pdf](documentation.md#xhtml2pdf) - PDF generator using HTML and CSS
- [pdfkit](text-processing.md#pdfkit) - Wkhtmltopdf python wrapper to convert html to pdf using the webkit rendering engine and qt
- [mdformat](documentation.md#mdformat) - CommonMark compliant Markdown formatter
- [xsdata](software-development-code-generators.md#xsdata) - Python XML Binding
- [pyyaml-include](software-development-libraries.md#pyyaml-include) - An extending constructor of PyYAML: include other YAML files into current YAML document
- [sphinx_design](software-development-libraries.md#sphinx_design) - A sphinx extension for designing beautiful, view size responsive web components.
- [commonmark](documentation.md#commonmark) - Python parser for the CommonMark Markdown spec
- [html-for-docx](software-development-build-tools.md#html-for-docx) - Convert HTML to DOCX easily and quickly
- [coloraide](internet-www-http.md#coloraide) - A color library for Python.
- [pydantic-handlebars](software-development-libraries.md#pydantic-handlebars) - Handlebars template engine for composing LLM prompts, built on Pydantic
- [pydantic-xml](software-development-libraries.md#pydantic-xml) - pydantic xml extension
- [pytablewriter](software-development-code-generators.md#pytablewriter) - pytablewriter is a Python library to write a table in various formats: AsciiDoc / CSV / Elasticsearch / HTML / JavaScript / JSON / LaTeX / LDJSON / LTSV / Markdown / MediaWiki / NumPy / Excel / Pandas / Python / reStructuredText / SQLite / TOML / TSV / YAML.
- [mdutils](software-development-documentation.md#mdutils) - Useful package for creating Markdown files while executing python code.
- [mistletoe](software-development-libraries.md#mistletoe) - A fast, extensible Markdown parser in pure Python.
- [zensical](documentation.md#zensical) - A modern static site generator built by the creators of Material for MkDocs
- [html5rdf](software-development-libraries-2.md#html5rdf) - HTML parser based on the WHATWG HTML specification
- [mdformat-gfm](documentation.md#mdformat-gfm) - Mdformat plugin for GitHub Flavored Markdown compatibility
- [dominate](internet-www-http.md#dominate) - Dominate is a Python library for creating and manipulating HTML documents using an elegant DOM API.
- [latexcodec](text-processing-filters.md#latexcodec) - A lexer and codec to work with LaTeX code in Python.
- [mkdocs-redirects](documentation.md#mkdocs-redirects) - A MkDocs plugin for dynamic page redirects to prevent broken links
- [ansi2html](software-development-quality-assurance.md#ansi2html) - Convert text with ANSI color codes to HTML or to LaTeX
- [inscriptis](text-processing.md#inscriptis) - inscriptis - HTML to text converter.
- [docstring-to-markdown](documentation-sphinx.md#docstring-to-markdown) - On the fly conversion of Python docstrings to markdown
- [docstring-parser-fork](documentation-sphinx.md#docstring-parser-fork) - Parse Python docstrings in reST, Google and Numpydoc format
- [mkdocs-gen-files](documentation.md#mkdocs-gen-files) - MkDocs plugin to programmatically generate documentation pages during the build
- [markdown-to-confluence](documentation.md#markdown-to-confluence) - Publish Markdown files to Confluence wiki
- [scrapling](internet-www-http.md#scrapling) - Scrapling is an undetectable, powerful, flexible, high-performance Python framework that makes Web Scraping easy and effortless as it should be!
- [PyLaTeX](software-development-code-generators.md#pylatex) - A Python library for creating LaTeX files and snippets
- [jsonpath](software-development-libraries-2.md#jsonpath) - An XPath for JSON
- [urlextract](software-development-libraries-2.md#urlextract) - Collects and extracts URLs from given text.
- [mkdocs-literate-nav](documentation.md#mkdocs-literate-nav) - MkDocs plugin to specify the navigation in Markdown instead of YAML
- [htmltools](internet-www-http.md#htmltools) - Tools for HTML generation and output.
- [plantuml-markdown](software-development-documentation.md#plantuml-markdown) - A PlantUML plugin for Markdown
- [rumdl](software-development-libraries-2.md#rumdl) - A fast Markdown linter and formatter written in Rust
- [dict2xml](software-development-libraries-2.md#dict2xml) - Small utility to convert a python dictionary into an XML string
- [empy](software-development-interpreters.md#empy) - A templating system for Python.
- [aspose-words](office-business.md#aspose-words) - Aspose.Words for Python is a Document Processing library that allows developers to work with documents in many popular formats without needing Office Automation.
- [mkdocs-include-markdown-plugin](documentation.md#mkdocs-include-markdown-plugin) - Mkdocs Markdown includer plugin.
- [myst-nb](software-development-libraries-2.md#myst-nb) - A Jupyter Notebook Sphinx reader built on top of the MyST markdown parser.
- [great-tables](internet-www-http.md#great-tables) - Easily generate information-rich, publication-quality tables from Python.
- [toon-format](software-development-libraries-2.md#toon-format) - Official Python implementation of TOON (Token-Oriented Object Notation), a compact, human-readable encoding of the JSON data model for LLM prompts.
- [mkdocs-section-index](documentation.md#mkdocs-section-index) - MkDocs plugin to allow clickable sections that lead to an index page
- [python-benedict](education-testing.md#python-benedict) - python-benedict is a dict subclass with keylist/keypath/keyattr support, normalized I/O operations (base64, csv, ini, json, pickle, plist, query-string, toml, xls, xml, yaml) and many utilities... for humans, obviously.
- [pybtex-docutils](text-editors-text-processing.md#pybtex-docutils) - A docutils backend for pybtex.
- [MarkupPy](software-development-libraries-2.md#markuppy) - An HTML/XML generator
- [minijinja](internet-www-http.md#minijinja) - An experimental Python binding of the Rust MiniJinja template engine.
- [mdit-plain](text-processing.md#mdit-plain) - A plain text renderer for markdown-it-py
- [python-toon](software-development-libraries-2.md#python-toon) - TOON (Token-Oriented Object Notation) encoder/decoder for Python - Bidirectional JSON-to-TOON converter optimized for LLMs
- [python-markdown-math](scientific-engineering-mathematics.md#python-markdown-math) - Math extension for Python-Markdown
- [imgkit](text-processing.md#imgkit) - Wkhtmltopdf python wrapper to convert html to image using the webkit rendering engine and qt
- [anyconfig](software-development-libraries-2.md#anyconfig) - Library provides common APIs to load and dump configuration files in various formats
- [pytest-md-report](software-development-quality-assurance.md#pytest-md-report) - A pytest plugin to generate test outcomes reports with markdown table format.
- [tombi](software-development-build-tools.md#tombi) - 🦅 TOML Toolkit 🦅
- [feedgen](communications.md#feedgen) - Feed Generator (ATOM, RSS, Podcasts)
- [termflow-md](terminals.md#termflow-md) - A streaming markdown renderer for modern terminals
- [python-hwpx](software-development-libraries-3.md#python-hwpx) - 한글 없이 HWPX 문서를 열고, 편집하고, 생성하고, 검증하는 Python 문서 라이브러리
- [mjml](communications-email.md#mjml) - Python implementation for MJML - a framework that makes responsive-email easy
- [newspaper4k](software-development-libraries-3.md#newspaper4k) - Simplified python article discovery & extraction.
- [jupyter-book](software-development-libraries-3.md#jupyter-book) - Create computational narratives that are reusable, reproducible, and interactive.
- [pysubs2](multimedia-video.md#pysubs2) - A library for editing subtitle files
- [pagefind](text-processing-indexing.md#pagefind) - Python API for Pagefind
- [sphinx-data-viewer](software-development-libraries-3.md#sphinx-data-viewer) - "Sphinx extension to show data in an interactive list view.
- [citeurl](internet-www-http.md#citeurl) - an extensible tool to process legal citations in text
- [xsdata-pydantic](software-development-code-generators.md#xsdata-pydantic) - xsdata pydantic plugin
- [markdown-include](internet-www-http.md#markdown-include) - A Python-Markdown extension which provides an 'include' function
- [pysrt](multimedia-video.md#pysrt) - SubRip (.srt) subtitle parser and writer
- [junos-eznc](software-development-libraries-3.md#junos-eznc) - Junos 'EZ' automation for non-programmers
- [fastkml](scientific-engineering-gis.md#fastkml) - Fast KML processing in python
- [latex2sympy2](education.md#latex2sympy2) - Convert latex to sympy with ANTLR and support Matrix, Linear Algebra and CAS functions.
- [ultimate-sitemap-parser](internet-www-http.md#ultimate-sitemap-parser) - A performant library for parsing and crawling sitemaps
- [rst2ansi](software-development-libraries-3.md#rst2ansi) - A rst converter to ansi-decorated console output
- [pypi-simple](software-development-libraries-3.md#pypi-simple) - PyPI Simple Repository API client library
- [mechanize](internet.md#mechanize) - Stateful, programmatic web browsing
- [py-yaml12](software-development-libraries-3.md#py-yaml12) - A modern YAML 1.2 parser and emitter for Python, written in Rust.
- [m2r2](documentation.md#m2r2) - Markdown to RST converter.
- [pdf-oxide](scientific-engineering-information-analysis.md#pdf-oxide) - The fastest Python PDF library — 0.8ms mean, 5× faster than the industry leaders, 100% pass rate on 3,830 real-world PDFs. Text extraction, Markdown/HTML conversion, PDF creation and editing.
- [mkdocs-click](documentation.md#mkdocs-click) - An MkDocs extension to generate documentation for Click command line applications
- [airium](database-front-ends.md#airium) - Easy and quick html builder with natural syntax correspondence (python->html). No templates needed. Serves pure pythonic library with no dependencies.
- [django-markdownx](internet-www-http.md#django-markdownx) - A comprehensive Markdown editor built for Django.
- [turbohtml](internet.md#turbohtml) - A fast, fully typed HTML toolkit for Python, powered by a C-accelerated core.
- [sphinx_external_toc](software-development-libraries-3.md#sphinx_external_toc) - A sphinx extension that allows the site-map to be defined in a single YAML file.
- [nvidia-sphinx-theme](documentation.md#nvidia-sphinx-theme) - A Sphinx theme for NVIDIA projects
- [PyXB-X](software-development-code-generators.md#pyxb-x) - PyXB-X ("pixbix") is a pure Python package that generates Python source code for classes that correspond to data structures defined by XMLSchema.
- [Genshi](internet-www-http.md#genshi) - A toolkit for generation of output for the web
- [BeautifulSoup](software-development-libraries-3.md#beautifulsoup) - Screen-scraping library
- [pydbml](documentation.md#pydbml) - Python parser and builder for DBML
- [fullbleed](office-business.md#fullbleed) - Deterministic Python PDF engine for reports, invoices, accessible documents, print-ready output, and compiled VDP
- [xlsx2html](text-processing.md#xlsx2html) - A simple export from xlsx format to html tables with keep cell formatting
- [sumy](education.md#sumy) - Module for automatic summarization of text documents and HTML pages.
- [terminaltables3](software-development-libraries-4.md#terminaltables3) - Generate simple tables in terminals from a nested list of strings. Fork of terminaltables.
- [rendercv](printing.md#rendercv) - Resume builder for academics and engineers
- [click-extra](documentation-sphinx.md#click-extra) - 🌈 Drop-in replacement for Click to make user-friendly and colorful CLI
- [igwn-ligolw](scientific-engineering-2.md#igwn-ligolw) - Python LIGO Light-Weight XML I/O Library
- [markdown-callouts](documentation.md#markdown-callouts) - Markdown extension: a classier syntax for admonitions
- [pytest-reporter-html1](software-development-testing.md#pytest-reporter-html1) - A basic HTML report template for Pytest
- [rl-accel](printing.md#rl-accel) - Acclerator for ReportLab
- [breadability](internet-www-http-2.md#breadability) - Port of Readability HTML parser in Python
- [mdformat-ruff](documentation.md#mdformat-ruff) - Mdformat plugin to ruffen Python code blocks
- [mdx-include](text-processing-filters.md#mdx-include) - Python Markdown extension to include local or remote files
- [sec-parser](office-business-financial.md#sec-parser) - Parse SEC EDGAR HTML documents into a tree of elements that correspond to the visual structure of the document.
- [json-strong-typing](file-formats-json.md#json-strong-typing) - Type-safe data interchange for Python data classes
- [matrx-scraper](internet-www-http-2.md#matrx-scraper) - Web scraping engine, HTML parsing, and search integration for the Matrx ecosystem
- [pansi](software-development.md#pansi) - Text mode rendering library
- [markdown-gfm-admonition](software-development-documentation.md#markdown-gfm-admonition) - GFM admonition syntax for Python Markdown
- [docling-rs](scientific-engineering-artificial-intelligence.md#docling-rs) - Fast, local document-to-Markdown for LLMs and RAG: docling in Rust, with docling's, MarkItDown's, Marker's and MinerU's Python APIs. PDF (layout, tables, OCR), DOCX, PPTX, XLSX, HTML, EPUB, email and more.
- [pyScss](software-development-code-generators.md#pyscss) - pyScss, a Scss compiler for Python
- [PyXB](software-development-code-generators.md#pyxb) - Python XML Schema Bindings
- [adf-lib](software-development-libraries-4.md#adf-lib) - A Python library for creating and manipulating ADF (Atlassian Document Format) documents
- [lazydocs](documentation.md#lazydocs) - Generate markdown API documentation for Google-style Python docstring.
- [blockdiag](software-development.md#blockdiag) - blockdiag generates block-diagram image from text
- [HTMLCompare](internet-www-http-2.md#htmlcompare) - library to compare HTML while ignoring non-functional differences
- [bioc](software-development-libraries-4.md#bioc) - bioc - Processing BioC, Brat, and PubTator with Python.
- [shinyswatch](internet-www-http-2.md#shinyswatch) - Bootswatch + Bootstrap 5 themes for Shiny.
- [gravitas-md2gdocs](software-development-libraries-4.md#gravitas-md2gdocs) - Convert Markdown to Google Docs API requests
- [mdformat-toc](documentation.md#mdformat-toc) - Mdformat plugin to generate table of contents
- [mdformat-beautysh](documentation.md#mdformat-beautysh) - Mdformat plugin to beautify Bash scripts
- [jupyterlite-core](software-development-documentation.md#jupyterlite-core) - 
- [dumbyaml](software-development-libraries-4.md#dumbyaml) - A YAML parser that reads only a restricted version of YAML.
- [mkdocs-rss-plugin](documentation.md#mkdocs-rss-plugin) - MkDocs plugin to generate RSS and JSON feeds using Mkdocs site configuration, git log and Mkdocs pages'meta.
- [fast-ebook](software-development-libraries-4.md#fast-ebook) - Rust-powered EPUB2/EPUB3 library for Python. Fast reading, writing, validation, and markdown conversion.
- [jinja2-fragments](internet-www-http-2.md#jinja2-fragments) - Render Jinja2 template block as HTML page fragments on Python web frameworks.
- [dramatiq-crontab](communications-email.md#dramatiq-crontab) - Cron style scheduler for asynchronous Dramatiq tasks in Django.
- [mdformat-black](documentation.md#mdformat-black) - Mdformat plugin to Blacken Python code blocks
- [slack-blocks-markdown](communications-chat.md#slack-blocks-markdown) - Convert Markdown to Slack Block Kit blocks using mistletoe
- [plutoprint](multimedia-graphics.md#plutoprint) - Paged HTML rendering library
- [minisignxml](security-cryptography.md#minisignxml) - Minimal XML signature and verification, intended for use with SAML2
- [markdown-it-pyrs](software-development-libraries-5.md#markdown-it-pyrs) - A Python interface for markdown-it.rs, using Rust for blazingly fast Markdown parsing ⚡️
- [pymantic](internet-www-http-2.md#pymantic) - Semantic Web and RDF library for Python
- [tinyhtml](internet-www-http-2.md#tinyhtml) - A tiny library to safely render compact HTML5 from Python expressions.
- [markdown-inline-graphviz-extension](documentation.md#markdown-inline-graphviz-extension) - Render inline graphs with Markdown and Graphviz (python3 version)
- [pytest-github-report](software-development-testing.md#pytest-github-report) - Generate a GitHub report using pytest in GitHub Workflows
- [markdown-grid-tables](software-development.md#markdown-grid-tables) - Python-Markdown extension to support grid tables.
- [svgutils](multimedia-graphics.md#svgutils) - Python SVG editor
