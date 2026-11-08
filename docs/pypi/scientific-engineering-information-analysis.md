# Scientific/Engineering / Information Analysis

[Index](README.md) · 67 packages in this topic, 168 more listed under another topic, by downloads.

### regex

Alternative regular expression module, to replace re.

`pip install regex` · installs (wheel) · licence: Apache-2.0 AND CNRI-Python · rank 93 · last release 2026-11-06 · [PyPI](https://pypi.org/project/regex/)

<details><summary>README extract</summary>

This regex implementation is backwards-compatible with the standard 're' module, but offers additional functionality.

Python 2 is no longer supported. The last release that supported Python 2 was 2021.11.10.

This module is targeted at CPython. ...

Example:
```python
>>> # Normal matching.
>>> regex.search(r'Mr|Mrs', 'Mrs')
<regex.Match object; span=(0, 2), match='Mr'>
>>> regex.search(r'one(self)?(selfsufficient)?', 'oneselfsufficient')
<regex.Match object; span=(0, 7), match='oneself'>
>>> # POSIX matching.
>>> regex.search(r'(?p)Mr|Mrs', 'Mrs')
<regex.Match object; span=(0, 3), match='Mrs'>
...
```

...

</details>

### contourpy

Python library for calculating contours of 2D quadrilateral grids

`pip install contourpy` · installs (wheel) · licence: BSD-3-Clause · rank 196 · last release 2026-09-11 · [PyPI](https://pypi.org/project/contourpy/) · [docs](https://contourpy.readthedocs.io) · [source](https://github.com/contourpy/contourpy)

<details><summary>README extract</summary>

ContourPy is a Python library for calculating contours of 2D quadrilateral grids. It is written in C++11 and wrapped using pybind11.

It contains the 2005 and 2014 algorithms used in Matplotlib as well as a newer algorithm that includes more features and is available in both serial and multithreaded versions. ...

</details>

### fastavro

Fast read/write of AVRO files

`pip install fastavro` · installs (wheel) · licence: MIT · rank 611 · last release 2026-10-08 · [PyPI](https://pypi.org/project/fastavro/)

<details><summary>README extract</summary>

> [!IMPORTANT]
> Fastavro is currently in maintenance mode. Efforts will be made to try to
> update to the latest versions of Python, fix security issues, and merge
> simple bug fixes or features, but even those might be significantly delayed.

Because the Apache Python `avro` package is written in pure Python, it is
relatively slow. ...

Sections: fastavro, Missing Features, Documentation, Releasing, Changes, Contact

</details>

### agate

A data analysis library that is optimized for humans instead of machines.

`pip install agate` · installs (wheel) · licence: MIT License · rank 778 · last release 2026-02-27 · [PyPI](https://pypi.org/project/agate/) · [source](https://github.com/wireservice/agate)

<details><summary>README extract</summary>

agate is a Python data analysis library that is optimized for humans instead of machines. It is an alternative to numpy and pandas that solves real-world problems with readable code.

agate was previously known as journalism.

Important links:

</details>

### natsort

Simple yet flexible natural sorting in Python.

`pip install natsort` · installs (wheel) · licence: MIT License · rank 938 · last release 2023-06-20 · [PyPI](https://pypi.org/project/natsort/)

<details><summary>README extract</summary>

Simple yet flexible natural sorting in Python.

 - Examples and Recipes
 - How Does Natsort Work?
 - API

 - Quick Description
 - Quick Examples
 - FAQ
 - Requirements
 - Optional Dependencies
 - Installation
 - How to Run Tests
 - How to Build Documentation
 - Dropped Deprecated APIs
 - History ...

Example:
```python
>>> a = ['2 ft 7 in', '1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '7 ft 6 in']
>>> sorted(a)
['1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '2 ft 7 in', '7 ft 6 in']
```

...

</details>

### PyPika

A SQL query builder API for Python

`pip install PyPika` · installs (wheel) · licence: Apache Software License · rank 1308 · last release 2026-02-04 · [PyPI](https://pypi.org/project/PyPika/)

<details><summary>README extract</summary>

What is ?

 is a Python API for building SQL queries. The motivation behind is to provide a simple interface for
building SQL queries without limiting the flexibility of handwritten SQL. Designed with data analysis in mind,
leverages the builder design pattern to construct queries to avoid messy string formatting and concatenation. ...

Example:
```python
from pypika import Query, Table, Field
```

Sections: PyPika - Python Query Builder, Abstract, What are the design goals for ?, Tutorial, Selecting Data, Tables, Columns, Schemas, and Databases, Arithmetic, Filtering, Convenience Methods, Grouping and Aggregating, GROUP BY Modifiers, Joining Tables and Subqueries, Join Types, Example of a join using `ON`

</details>

### parsimonious

(Soon to be) the fastest pure-Python PEG parser I could muster

`pip install parsimonious` · installs (wheel) · licence: MIT License · rank 1372 · last release 2025-11-12 · [PyPI](https://pypi.org/project/parsimonious/)

<details><summary>README extract</summary>

Parsimonious aims to be the fastest arbitrary-lookahead parser written in pure
Python—and the most usable. It's based on parsing expression grammars (PEGs),
which means you feed it a simplified sort of EBNF notation. ...

Features:
Some have asked why we don't process the tree as we go, SAX-style. There are
two main reasons:

1. It wouldn't work. With a PEG parser, no parsing decision is final until the
 whole text is parsed. ...

Example:
```python
>>> from parsimonious.grammar import Grammar
>>> grammar = Grammar(
...     """
...     bold_text  = bold_open text bold_close
...     text       = ~"[A-Z 0-9]*"i
...     bold_open  = "(("
...     bold_close = "))"
...     """)
```

...

</details>

### lingua-language-detector

An accurate natural language detection library, suitable for short text and mixed-language text

`pip install lingua-language-detector` · installs (wheel) · licence: Apache Software License · rank 1981 · last release 2026-03-09 · [PyPI](https://pypi.org/project/lingua-language-detector/) · [source](https://github.com/pemistahl/lingua-py)

<details><summary>README extract</summary>

Its task is simple: It tells you which language some text is written in.
This is very useful as a preprocessing step for linguistic data
in natural language processing applications such as text classification and
spell checking. ...

Example:
```python
>>> from lingua import Language, LanguageDetectorBuilder
>>> languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH]
>>> detector = LanguageDetectorBuilder.from_languages(*languages).build()
>>> language = detector.detect_language_of("languages are awesome")
>>> language
Language.ENGLISH
>>> language.iso_code_639_1
...
```

...

</details>

### cmdstanpy

Python interface to CmdStan

`pip install cmdstanpy` · installs (wheel) · licence: BSD License · rank 2065 · last release 2026-11-03 · [PyPI](https://pypi.org/project/cmdstanpy/)

<details><summary>README extract</summary>

CmdStanPy is a lightweight pure-Python interface to CmdStan which provides access to the Stan compiler and all inference algorithms. It supports both development and production workflows. ...

Example:
```python
import os
from cmdstanpy import cmdstan_path, CmdStanModel

# specify locations of Stan program file and data
stan_file = os.path.join(cmdstan_path(), 'examples', 'bernoulli', 'bernoulli.stan')
data_file = os.path.join(cmdstan_path(), 'examples', 'bernoulli', 'bernoulli.data.json')

# instantiate a model; compiles the Stan program by default
...
```

Sections: CmdStanPy, Goals, Source Repository, Docs, Licensing, Example

</details>

### marisa-trie

Static memory-efficient and fast Trie-like structures for Python.

`pip install marisa-trie` · installs (wheel) · licence: MIT AND (BSD-2-Clause OR LGPL-2.1-or-later) · rank 2363 · last release 2026-04-08 · [PyPI](https://pypi.org/project/marisa-trie/) · [source](https://github.com/pytries/marisa-trie)

_README extract left out: share-alike licence._

### pyvista

3D visualization and mesh analysis for science and engineering.

`pip install pyvista` · installs (wheel) · licence: MIT · rank 3172 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pyvista/) · [docs](https://docs.pyvista.org/) · [source](https://github.com/pyvista/pyvista)

<details><summary>README extract</summary>

3D visualization and mesh analysis for science and engineering

 PyVista is an open source, community-owned project, MIT licensed and
 NumFOCUS Affiliated.

 CoDimensional PBC,
 founded by PyVista maintainers, is the project's commercial steward.

PyVista provides:

- a NumPy-native API for 3D visualization and mesh analysis ...

Features:
PyVista is the foundational Python library for 3D visualization and mesh
analysis in scientific computing and engineering. It plays the same role for
3D data that pandas plays for tabular data and xarray plays for labeled
n-dimensional arrays: ...

Sections: Why PyVista, Built for production, Built to extend, Quickstart, Command line interface, Documentation, Connections, Citing PyVista

</details>

### scrubadub

Clean personally identifiable information from dirty dirty text.

`pip install scrubadub` · installs (wheel) · licence: Apache Software License · rank 3183 · last release 2023-09-01 · [PyPI](https://pypi.org/project/scrubadub/)

<details><summary>README extract</summary>

Remove personally identifiable information from free text. Sometimes we have
additional metadata about the people we wish to anonymize. Other times we don't.
This package makes it easy to seamlessly scrub personal information from free
text, without compromising the privacy of the people we are trying to protect. ...

Example:
```python
>>> import scrubadub

# My cat may be more tech-savvy than most, but he doesn't want other people to know it.
>>> text = "My cat can be contacted on example@example.com, or 1800 555-5555"

# Replaces the phone number and email addresse with anonymous IDs.
>>> scrubadub.clean(text)
'My cat can be contacted on {{EMAIL}}, or {{PHONE}}'
```

Sections: scrubadub, Quick start

</details>

### leidenalg

Leiden is a general algorithm for methods of community detection in large networks.

`pip install leidenalg` · installs (wheel) · licence: GPL-3.0-or-later · rank 3722 · last release 2026-05-24 · [PyPI](https://pypi.org/project/leidenalg/)

_README extract left out: share-alike licence._

### liteparse

Python bindings for LiteParse - fast, lightweight PDF and document parsing

`pip install liteparse` · installs (wheel) · licence: Apache-2.0 · rank 4711 · last release 2026-11-04 · [PyPI](https://pypi.org/project/liteparse/) · [docs](https://github.com/run-llama/liteparse#readme) · [source](https://github.com/run-llama/liteparse)

<details><summary>README extract</summary>

Python bindings for LiteParse — fast, lightweight PDF and document parsing with spatial text extraction.

Example:
```python
from liteparse import LiteParse

parser = LiteParse()
result = parser.parse("document.pdf")
print(result.text)
print(f"Source document pages: {result.total_pages}")

# Access structured data
for page in result.pages:
    print(f"Page {page.page_num}: {len(page.text_items)} text items")
```

Sections: LiteParse Python, Quick Start, Markdown Output, Configuration, Parsing from Bytes, Worker Pool and Hard Timeouts, Screenshots, Document Complexity, CLI

</details>

### pygraphviz

Python interface to Graphviz

`pip install pygraphviz` · installs (wheel) · licence: BSD-3-Clause · rank 5276 · last release 2026-10-15 · [PyPI](https://pypi.org/project/pygraphviz/) · [docs](https://pygraphviz.github.io/documentation/stable/) · [source](https://github.com/pygraphviz/pygraphviz/)

<details><summary>README extract</summary>

PyGraphviz is a Python interface to the Graphviz graph layout and
visualization package.
With PyGraphviz you can create, edit, read, write, and draw graphs using
Python to access the Graphviz graph data structure and layout algorithms.
PyGraphviz provides a similar programming interface to NetworkX

Example:
```python
>>> import pygraphviz as pgv
>>> G = pgv.AGraph()
>>> G.add_node("a")
>>> G.add_edge("b", "c")
>>> print(G)
strict graph "" {
        a;
        b -- c;
}
```

Sections: PyGraphviz, Simple example

</details>

### cityhash

Python bindings for CityHash and FarmHash

`pip install cityhash` · installs from source (sdist only) · licence: MIT License · rank 5285 · last release 2025-10-09 · [PyPI](https://pypi.org/project/cityhash/)

<details><summary>README extract</summary>

Python wrapper for FarmHash and
CityHash, a family of fast
non-cryptographic hash functions.

Example:
```python
>>> from farmhash import FarmHash32, FarmHash64, FarmHash128
>>> FarmHash32("abc")
1961358185
>>> FarmHash64("abc")
2640714258260161385
>>> FarmHash128("abc")
76434233956484675513733017140465933893
```

Sections: CityHash/FarmHash, Getting Started, Usage Examples, Stateless hashing, Hardware-independent fingerprints, Incremental hashing, Fast hashing of NumPy arrays, Local workflow, Distribution, See Also

</details>

### nicknames

Hand-curated dataset of English names and nicknames.

`pip install nicknames` · installs (wheel) · licence: Apache-2.0 · rank 5318 · last release 2026-03-06 · [PyPI](https://pypi.org/project/nicknames/)

<details><summary>README extract</summary>

A hand-curated CSV file containing English given names (first names) and
their associated nicknames.

For more info on the source and format of the data, see
In case that is useful to you, there are also SQL and typescript bindings there.

The Python package is available on PyPI from

and then you can get to the csv data directly: ...

Example:
```python
from nicknames import name_triplets

# name_triplets() returns a list of a NamedTuples:
print(name_triplets()[:3])
# [NameTriplet(name1='aaron', relationship='has_nickname', name2='erin'), NameTriplet(name1='aaron', relationship='has_nickname', name2='ron'), NameTriplet(name1='aaron', relationship='has_nickname', name2='ronnie')]
```

Sections: Nicknames, Python API

</details>

### pymorphy3-dicts-ru

Russian dictionaries for pymorphy2

`pip install pymorphy3-dicts-ru` · installs (wheel) · licence: MIT License · rank 5343 · last release 2022-01-08 · [PyPI](https://pypi.org/project/pymorphy3-dicts-ru/)

<details><summary>README extract</summary>

Russian dictionaries for pymorphy3.

Sections: pymorphy3-dicts-ru, Usage

</details>

### pymorphy3

Morphological analyzer (POS tagger + inflection engine) for Russian language.

`pip install pymorphy3` · installs (wheel) · licence: MIT License · rank 5344 · last release 2025-10-09 · [PyPI](https://pypi.org/project/pymorphy3/)

<details><summary>README extract</summary>

pymorphy3 is the continuation of the unmaintained project pymorphy2 which is an morphological analyzer (POS tagger + inflection engine) for Russian and Ukrainian languages.

pymorphy3 officially supports Python 3.9 ~ 3.14.

</details>

### DAWG2-Python

Pure-python reader for DAWGs (DAFSAs) created by dawgdic C++ library or DAWG Python extension.

`pip install DAWG2-Python` · installs (wheel) · licence: MIT License · rank 5433 · last release 2025-02-17 · [PyPI](https://pypi.org/project/DAWG2-Python/) · [source](https://github.com/pymorphy2-fork/DAWG-Python/)

<details><summary>README extract</summary>

This pure-python package provides read-only access for files created by
dawgdic C++ library and
DAWG python package.

This package is not capable of creating DAWGs. It works with DAWGs built
by dawgdic C++ library or
DAWG Python extension module. The main
purpose of DAWG-Python is to provide access to DAWGs without
requiring compiled extensions. ...

Example:
```python
import dawg

d = dawg.DAWG(data)
d.save('words.dawg')
```

Sections: DAWG2-Python, Usage, Benchmarks, Current limitations, Running tests and benchmarks, Changes, 0.8.1 (2024-08-01), 0.8.0 (2023-09-27), 0.7.2 (2015-04-18), 0.7.1 (2014-06-05), 0.7 (2013-10-13), 0.6 (2013-03-23), 0.5.1 (2013-03-01), 0.5 (2012-10-08)

</details>

### kneed

Knee-point detection in Python

`pip install kneed` · installs (wheel) · licence: not stated · rank 5872 · last release 2026-10-19 · [PyPI](https://pypi.org/project/kneed/) · [docs](https://kneed.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Knee-point detection in Python

A Python library for detecting knee (elbow) points in curves using the Kneedle algorithm. Given a set of `x` and `y` values, `kneed` returns the point of maximum curvature.

Features:
- Detect knee/elbow points in concave or convex curves
- Support for increasing and decreasing functions
- Automatic curve shape detection with `find_shape()`
- Multiple knee detection via online mode (`all_knees` / `all_elbows`) ...

Example:
```python
from kneed import KneeLocator, DataGenerator

# Generate sample data
x, y = DataGenerator.figure2()

# Find the knee point
kl = KneeLocator(x, y, curve="concave", direction="increasing")
print(kl.knee)       # 0.222
print(kl.knee_y)     # 1.897
```

...

</details>

### segtok

sentence segmentation and word tokenization tools

`pip install segtok` · installs (wheel) · licence: MIT License · rank 6340 · last release 2021-12-15 · [PyPI](https://pypi.org/project/segtok/)

<details><summary>README extract</summary>

NB: segtok v2, code-named syntok, is available and fixes some tricky issues with segtok, in particular splitting sentence with terminals not followed by spaces.Like this :-).

The segtok package provides two modules, `segtok.segmenter` and `segtok.tokenizer`.
The segmenter provides functionality for splitting (Indo-European) text into sentences. ...

Sections: segtok, Sentence segmentation and word tokenization, Test Suite, Usage, A command-line, B `segtok.segmenter`, C `segtok.tokenizer`, Legal

</details>

### pbixray

A Python library to parse and analyze PBIX files used with Microsoft Power BI and Excel PowerPivot.

`pip install pbixray` · installs (wheel) · licence: MIT License · rank 6546 · last release 2026-08-27 · [PyPI](https://pypi.org/project/pbixray/)

<details><summary>README extract</summary>

Read Power BI semantic models without Power BI.

No Power BI Desktop. No Analysis Services instance. No XMLA endpoint, no Premium capacity, no workspace, no restore. Just a file path.

PBIXRay is a Python reader for the VertiPaq engine's on-disk format. ...

Example:
```python
from pbixray import PBIXRay

model = PBIXRay("sales.pbix")

model.dax_measures         # every measure, as a DataFrame
model.relationships        # the full model graph
model.power_query          # all M code
model.get_table("Sales")   # actual decoded rows
```

Sections: PBIXRay, What you can pull out, Three formats, one API, The 40 DMVs, from a file, Models bigger than your RAM, Built on PBIXRay, 🖥️ PBIXRay for macOS, 🌐 pbix.info, 🦆 DuckDB extension, Scope, Built on, Links

</details>

### yake

Keyword extraction Python package

`pip install yake` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 7004 · last release 2026-02-09 · [PyPI](https://pypi.org/project/yake/) · [docs](https://inesctec.github.io/yake/docs/--home) · [source](https://github.com/INESCTEC/yake)

_README extract left out: share-alike licence._

### prov

A library for W3C Provenance Data Model supporting PROV-N, PROV-JSON, PROV-XML, PROV-O (RDF) and PROV-JSONLD

`pip install prov` · installs (wheel) · licence: MIT · rank 7036 · last release 2026-10-19 · [PyPI](https://pypi.org/project/prov/) · [docs](https://prov.readthedocs.io) · [source](https://github.com/trungdong/prov)

<details><summary>README extract</summary>

A Python implementation of the W3C PROV Data Model, with
import and export in PROV-N, PROV-JSON, PROV-JSONLD, PROV-XML and PROV-O (RDF).

- Documentation: <
- Licence: MIT
- Python 3.10 or later

Features:
- In-memory classes for every PROV-DM record type, readable from and printable as
 PROV-N.
- Serialization to and from PROV-N,
 PROV-JSON,
 PROV-JSONLD,
 PROV-XML and PROV-O (RDF). ...

Sections: prov, Features

</details>

### nflreadpy

A Python package for downloading NFL data from nflverse repositories

`pip install nflreadpy` · installs (wheel) · licence: MIT · rank 7355 · last release 2025-11-19 · [PyPI](https://pypi.org/project/nflreadpy/) · [docs](https://nflreadpy.nflverse.com) · [source](https://github.com/nflverse/nflreadpy)

<details><summary>README extract</summary>

A Python package for downloading NFL data from nflverse repositories. This is a
Python port of the popular R package nflreadr,
designed to provide easy access to NFL data with caching, progress tracking, and
modern Python conventions.

Features:
- Compatible API with nflreadr R package
- Fast data loading with Polars DataFrames
- Intelligent caching (memory or filesystem)
- Progress tracking for large downloads

Example:
```python
import nflreadpy as nfl

# Load current season play-by-play data
pbp = nfl.load_pbp()

# Load player game-level stats for multiple seasons
player_stats = nfl.load_player_stats([2022, 2023])

# Load all available team level stats
team_stats = nfl.load_team_stats(seasons=True)

# nflreadpy uses Polars instead of pandas. Convert to pandas if needed:
...
```

...

</details>

### signify

Module to generate and verify PE signatures

`pip install signify` · installs (wheel) · licence: MIT · rank 7698 · last release 2026-10-11 · [PyPI](https://pypi.org/project/signify/) · [docs](http://signify.readthedocs.io/en/latest/) · [source](https://github.com/ralphje/signify)

<details><summary>README extract</summary>

Signify, a portmanteau of *signature* and *verify*, is a Python module that provides
validation and inspection of digital code signatures. These types of signatures are
used to verify the authenticity and integrity of executable code, providing assurance
about who published a piece of software and whether is has been altered since it was
signed. ...

Sections: Signify, Documentation, Thanks

</details>

### simplemma

Fast and zero-dependency lemmatization, tokenization and sentence splitting for 54 languages.

`pip install simplemma` · installs (wheel) · licence: MIT License · rank 7819 · last release 2026-08-12 · [PyPI](https://pypi.org/project/simplemma/) · [docs](https://adbar.github.io/simplemma/)

<details><summary>README extract</summary>

Fast, dependency-free lemmatization for 54 languages.
Pure Python, no models to download, works offline.

- A 19 MB install with no per-language downloads: 9 of the 54 languages have
 no Stanza lemmatizer and 34 no spaCy pipeline ...

Example:
```python
>>> import simplemma

>>> simplemma.lemmatize('masks', lang='en')
'mask'

>>> mytokens = ['Hier', 'sind', 'Vaccines']
>>> [simplemma.lemmatize(t, lang='de') for t in mytokens]
['hier', 'sein', 'Vaccines']

>>> simplemma.is_known('spaghetti', lang='it')
True

>>> simplemma.simple_tokenizer('Hier sind Vaccines.')
['Hier', 'sind', 'Vaccines', '.']

...
```

...

</details>

### agate-sql

agate-sql adds SQL read/write support to agate.

`pip install agate-sql` · installs (wheel) · licence: MIT License · rank 7833 · last release 2025-12-15 · [PyPI](https://pypi.org/project/agate-sql/)

<details><summary>README extract</summary>

agate-sql adds SQL read/write support to agate.

Important links:

* agate

</details>

### agate-excel

agate-excel adds read support for Excel files (xls and xlsx) to agate.

`pip install agate-excel` · installs (wheel) · licence: MIT License · rank 7844 · last release 2025-12-15 · [PyPI](https://pypi.org/project/agate-excel/)

<details><summary>README extract</summary>

agate-excel adds read support for Excel files (xls and xlsx) to agate.

Important links:

* agate

</details>

### carelytics

A Python library for Healthcare Data Analytics and Revenue Cycle Management.

`pip install carelytics` · installs (wheel) · licence: MIT License · rank 7866 · last release 2025-11-17 · [PyPI](https://pypi.org/project/carelytics/)

<details><summary>README extract</summary>

*A modular Python package for healthcare data cleaning, validation, and revenue cycle insights.*

Features:
Carelytics is a Python library designed to simplify data analytics and automation in the healthcare domain, especially focusing on Revenue Cycle Management (RCM) workflows.

It provides functions to: ...

Example:
```python
import pandas as pd
from carelytics.utils import validator, cleaner
from carelytics.models import denial_prediction

# Load your healthcare dataset
df = pd.read_csv("claims.csv")

# Validate structure
validator.validate_columns(df, ["claim_id", "payer", "amount", "denial_flag"])

# Clean and prepare
df = cleaner.fill_missing(df, "median")

...
```

...

</details>

### agate-dbf

agate-dbf adds read support for dbf files to agate.

`pip install agate-dbf` · installs (wheel) · licence: MIT License · rank 7887 · last release 2025-12-15 · [PyPI](https://pypi.org/project/agate-dbf/)

<details><summary>README extract</summary>

agate-dbf adds read support for dbf files to agate.

Important links:

* agate

</details>

### csvkit

A suite of command-line tools for working with CSV, the king of tabular file formats.

`pip install csvkit` · installs (wheel) · licence: MIT License · rank 7895 · last release 2025-12-15 · [PyPI](https://pypi.org/project/csvkit/) · [docs](https://csvkit.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

csvkit is a suite of command-line tools for converting to and working with CSV, the king of tabular file formats.

It is inspired by pdftk, GDAL and the original csvcut tool by Joe Germuska and Aaron Bycoffe.

Important links:

</details>

### ansys-tools-common

A set of tools for PyAnsys libraries

`pip install ansys-tools-common` · installs (wheel) · licence: MIT · rank 8159 · last release 2026-08-31 · [PyPI](https://pypi.org/project/ansys-tools-common/) · [docs](https://tools.docs.pyansys.com/) · [source](https://github.com/ansys/ansys-tools-common)

<details><summary>README extract</summary>

Features:
Ansys Common Tools provides a set of tools for the PyAnsys ecosystem.

Sections: Ansys Common Tools, Overview, Documentation and issues

</details>

### pyvistaqt

pyvista qt plotter

`pip install pyvistaqt` · installs (wheel) · licence: MIT License · rank 8436 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pyvistaqt/)

<details><summary>README extract</summary>

`pyvistaqt` is a helper module for `pyvista` to enable you to
plot using Qt by placing a vtk-widget into a background renderer.
This can be quite useful when you desire to update your plot in
real-time.

For the installation and usage of this package, please visit the
PyVistaQt documentation. ...

Sections: PyVistaQt, Documentation

</details>

### Gammatone

(no summary)

`pip install Gammatone` · installs (wheel) · licence: not stated · rank 8492 · last release 2024-09-10 · [PyPI](https://pypi.org/project/Gammatone/)

<details><summary>README extract</summary>

*Utilities for analysing sound using perceptual models of human hearing.*

This is a port of Malcolm Slaney's and Dan Ellis' gammatone filterbank MATLAB
code, detailed below, to Python 2 and 3 using Numpy and Scipy. It analyses signals by
running them through banks of gammatone filters, similar to Fourier-based
spectrogram analysis.

Sections: Gammatone Filterbank Toolkit, Summary, Using the Code, Basis, Interest, Verifying the port

</details>

### policyengine-core

Core microsimulation engine enabling country-specific policy models.

`pip install policyengine-core` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 8622 · last release 2026-11-08 · [PyPI](https://pypi.org/project/policyengine-core/)

_README extract left out: share-alike licence._

### pdf-oxide

The fastest Python PDF library — 0.8ms mean, 5× faster than the industry leaders, 100% pass rate on 3,830 real-world PDFs. Text extraction, Markdown/HTML conversion, PDF creation and editing.

`pip install pdf-oxide` · installs (wheel) · licence: Apache Software License; MIT License · rank 8671 · last release 2026-09-08 · [PyPI](https://pypi.org/project/pdf-oxide/) · [docs](https://pdf.oxide.fyi/docs/getting-started/python) · [source](https://github.com/yfedoseev/pdf_oxide)

<details><summary>README extract</summary>

The fastest Python PDF library for text extraction, image extraction, and markdown conversion. Powered by a pure-Rust core, exposed to Python through PyO3. 0.8ms mean per document, 5× faster than PyMuPDF, 15× faster than pypdf. 100% pass rate on 3,830 real-world PDFs. MIT / Apache-2.0 licensed.

> Part of the PDF Oxide toolkit. ...

Features:
- Fast — 0.8ms mean per document, 5× faster than PyMuPDF, 15× faster than pypdf, 29× faster than pdfplumber
- Reliable — 100% pass rate on 3,830 test PDFs, zero panics, zero timeouts, no segfaults ...

Example:
```python
from pdf_oxide import PdfDocument

with PdfDocument("paper.pdf") as doc:
    print(len(doc))                          # number of pages
    for page in doc:
        text = page.text                     # lazy property
...

</details>

### fastnumbers

Super-fast and clean conversions to numbers.

`pip install fastnumbers` · installs (wheel) · licence: MIT · rank 8781 · last release 2026-06-28 · [PyPI](https://pypi.org/project/fastnumbers/) · [docs](https://fastnumbers.readthedocs.io/)

<details><summary>README extract</summary>

Super-fast and clean conversions to numbers.

 - Quick Start
 - Timing
 - High-level Algorithm
 - How To Run Tests
 - History

`fastnumbers` is a module with the following three objectives (in order
of decreasing importance as to why the module was created):

 #. ...

Example:
```python
>>> from fastnumbers import RAISE, try_float
>>> # Convert string to a float
>>> try_float('56.07')
56.07
>>> # Integers are converted to floats
>>> try_float(54)
54.0
>>>
>>> # Unconvertable string returned as-is by default
>>> try_float('bad input')
'bad input'
>>> # Unconvertable strings can trigger a default value
...
```

...

</details>

### policyengine-us

US federal and state tax-benefit microsimulation model.

`pip install policyengine-us` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 8835 · last release 2026-11-08 · [PyPI](https://pypi.org/project/policyengine-us/)

_README extract left out: share-alike licence._

### ir-measures

Provides a common interface to many IR measure tools

`pip install ir-measures` · installs (wheel) · licence: Apache Software License · rank 9666 · last release 2025-11-25 · [PyPI](https://pypi.org/project/ir-measures/) · [source](https://github.com/terrierteam/ir_measures)

<details><summary>README extract</summary>

New: Explore IR measures using our demo at demo.ir-measur.es!

Check out our documentation website: ir-measur.es

Provides a common interface to many IR measure tools.

Provided by the Terrier Team @ Glasgow. Find us at terrierteam/ir_measures.

Example:
```python
import ir_measures
from ir_measures import * # imports all supported measures, e.g., AP, nDCG, RR, P

qrels = {
    'Q0': {"D0": 0, "D1": 1},
    "Q1": {"D0": 0, "D3": 2}
}
run = {
    'Q0': {"D0": 1.2, "D1": 1.0},
    "Q1": {"D0": 2.4, "D3": 3.6}
}

# aggregated results
ir_measures.calc_aggregate([AP, nDCG, RR, nDCG@10, P(rel=2)@10], qrels, run)
...
```

Sections: ir_measures, Getting Started, Python API, Command Line Interface, PyTerrier API, Documentation

</details>

### DAWG-Python

Pure-python reader for DAWGs (DAFSAs) created by dawgdic C++ library or DAWG Python extension.

`pip install DAWG-Python` · installs (wheel) · licence: MIT License · rank 9932 · last release 2015-04-18 · [PyPI](https://pypi.org/project/DAWG-Python/)

<details><summary>README extract</summary>

This pure-python package provides read-only access for files
created by dawgdic C++ library and DAWG python package.

This package is not capable of creating DAWGs. It works with DAWGs built by
dawgdic C++ library or DAWG Python extension module. ...

Example:
```python
import dawg
d = dawg.DAWG(data)
d.save('words.dawg')
```

Sections: DAWG-Python, Usage, Benchmarks, Current limitations, Running tests and benchmarks, Changes, 0.7.2 (2015-04-18), 0.7.1 (2014-06-05), 0.7 (2013-10-13), 0.6 (2013-03-23), 0.5.1 (2013-03-01), 0.5 (2012-10-08), 0.3.1 (2012-10-01), 0.3 (2012-09-26)

</details>

### policyengine-uk

PolicyEngine tax and benefit system for the UK.

`pip install policyengine-uk` · installs (wheel) · licence: AGPL-3.0 · rank 9950 · last release 2026-11-06 · [PyPI](https://pypi.org/project/policyengine-uk/) · [source](https://github.com/PolicyEngine/policyengine-uk)

_README extract left out: share-alike licence._

### pymorphy2-dicts-ru

Russian dictionaries for pymorphy2

`pip install pymorphy2-dicts-ru` · installs (wheel) · licence: MIT License · rank 10040 · last release 2020-10-11 · [PyPI](https://pypi.org/project/pymorphy2-dicts-ru/)

<details><summary>README extract</summary>

Russian dictionaries for pymorphy2.

Sections: pymorphy2-dicts-ru, Usage

</details>

### wn

Wordnet interface library

`pip install wn` · installs (wheel) · licence: MIT License · rank 10092 · last release 2026-08-14 · [PyPI](https://pypi.org/project/wn/) · [docs](https://wn.readthedocs.io)

<details><summary>README extract</summary>

a Python library for wordnets

 Available Wordnets
 | Documentation
 | FAQ
 | Migrating from NLTK
 | Citation

Wn is a Python library for exploring information in wordnets.

Features:
- Multilingual by design; first-class support for wordnets in any language
- Interlingual queries via the Collaborative Interlingual Index
- Six similarity metrics
- Functions for exploring taxonomies ...

Example:
```python
>>> import wn
>>> en = wn.Wordnet('oewn:2025+')       # Create Wordnet object to query
>>> ss = en.synsets('win', pos='v')[0]  # Get the first synset for 'win'
>>> ss.definition()                     # Get the synset's definition
'be the winner in a contest or competition; be victorious'
```

...

</details>

### pymorphy2

Morphological analyzer (POS tagger + inflection engine) for Russian language.

`pip install pymorphy2` · installs (wheel) · licence: MIT License · rank 10542 · last release 2020-09-26 · [PyPI](https://pypi.org/project/pymorphy2/)

<details><summary>README extract</summary>

Morphological analyzer (POS tagger + inflection engine)
for Russian and Ukrainian languages. License is MIT.

* source code: github

Links:

* Springer
* PDF

BibTeX:

Sections: pymorphy2, Citing

</details>

### dbt-mcp

A MCP (Model Context Protocol) server for interacting with dbt resources.

`pip install dbt-mcp` · installs (wheel) · licence: Apache Software License · rank 11354 · last release 2026-11-03 · [PyPI](https://pypi.org/project/dbt-mcp/) · [docs](https://docs.getdbt.com/docs/dbt-ai/about-mcp) · [source](https://github.com/dbt-labs/dbt-mcp)

<details><summary>README extract</summary>

This MCP (Model Context Protocol) server provides various tools to interact with dbt. You can use this MCP server to provide AI agents with context of your project in dbt Core, dbt Fusion, and dbt Platform.

Read our documentation here to learn more. This blog post provides more details for what is possible with the dbt MCP server. ...

Sections: dbt MCP Server, Experimental MCP Bundle, Feedback, Architecture, Tools, SQL, Semantic Layer, Discovery, dbt CLI, Admin API, dbt Codegen, dbt LSP, Product Docs, MCP Server Metadata

</details>

### pymorphy3-dicts-uk

Ukrainian dictionaries for pymorphy3

`pip install pymorphy3-dicts-uk` · installs (wheel) · licence: MIT License · rank 11371 · last release 2022-09-13 · [PyPI](https://pypi.org/project/pymorphy3-dicts-uk/)

<details><summary>README extract</summary>

Ukrainian dictionaries for pymorphy3.

Sections: pymorphy3-dicts-uk, Usage

</details>

### scikit-posthocs

Statistical post-hoc analysis and outlier detection algorithms

`pip install scikit-posthocs` · installs (wheel) · licence: MIT License · rank 11440 · last release 2026-10-09 · [PyPI](https://pypi.org/project/scikit-posthocs/) · [docs](https://scikit-posthocs.rtfd.io)

<details><summary>README extract</summary>

scikit-posthocs is a Python package that provides post hoc tests for
pairwise multiple comparisons that are usually performed in statistical
data analysis to assess the differences between group levels if a
statistically significant result of ANOVA test has been obtained. ...

Features:
- Scheffe test.
 - Student T test.
 - Tamhane T2 test.
 - TukeyHSD test.

 - Conover test.
 - Dunn test.
 - Dwass, Steel, Critchlow, and Fligner test.
 - Mann-Whitney test.
 - Nashimoto and Wright (NPM) test.
 - Nemenyi test.
 - van Waerden test. ...

Sections: scikit-posthocs, Background, Features, Dependencies, Compatibility

</details>

### datrie

Super-fast, efficiently stored Trie for Python.

`pip install datrie` · installs from source (sdist only) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 11462 · last release 2025-08-28 · [PyPI](https://pypi.org/project/datrie/)

_README extract left out: share-alike licence._

### gridstatus

Access electricity grid data (load, fuel mix, prices, forecasts) from North American ISOs through one consistent Python API

`pip install gridstatus` · installs (wheel) · licence: BSD License · rank 11999 · last release 2026-10-23 · [PyPI](https://pypi.org/project/gridstatus/) · [docs](https://opensource.gridstatus.io/) · [source](https://github.com/gridstatus/gridstatus/)

<details><summary>README extract</summary>

`gridstatus` is an open source Python library, maintained by Grid Status, that fetches electricity market data directly from North American independent system operators (ISOs), regional transmission organizations (RTOs), and the U.S. EIA.

 ⚡ Have you considered our Hosted API? ...

Example:
```python
from gridstatus import CAISO, Ercot, SPP, list_isos

# See the ISO classes exposed by the discovery helper
list_isos()

# Pick an ISO and pull a dataset for a fixed date
iso = Ercot()
fuel_mix = iso.get_fuel_mix("2024-06-01")

# Source-specific methods expose other datasets and market intervals
...
```

Sections: Getting started, What's available, Resources & help

</details>

### bidsschematools

Python tools for working with the BIDS schema.

`pip install bidsschematools` · installs (wheel) · licence: MIT License · rank 12056 · last release 2026-10-14 · [PyPI](https://pypi.org/project/bidsschematools/)

<details><summary>README extract</summary>

A Python library (available after installation in the Python interpreter as `bidsschematools`)
for working with the Brain Imaging Data Structure (BIDS) schema.

Features:
* lightweight
* reference schema parsing implementation used for schema testing
* simple CLI bindings (e.g. `bst export`) ...

</details>

### pyap2

Pyap2 is a maintained fork of pyap, a regex-based library for parsing US, CA, and UK addresses. The fork adds typing support, handles more address formats and edge cases.

`pip install pyap2` · installs (wheel) · licence: MIT License · rank 12101 · last release 2026-09-28 · [PyPI](https://pypi.org/project/pyap2/) · [docs](https://github.com/argyle-engineering/pyap) · [source](https://github.com/argyle-engineering/pyap)

<details><summary>README extract</summary>

Pyap2 is a maintained fork of Pyap, a regex-based python library for
detecting and parsing addresses. Currently it supports US 🇺🇸, Canadian 🇨🇦 and British 🇬🇧 addresses.

Example:
```python
>>> import pyap
>>> test_address = """
    Lorem ipsum
    225 E. John Carpenter Freeway,
    Suite 1500 Irving, Texas 75062
    Dorem sit amet
    """
>>> addresses = pyap.parse(test_address, country='US')
>>> for address in addresses:
        # shows found address
        print(address)
        # shows address parts
...
```

Sections: Pyap2: Python address parser, About, Typical workflow, Limitations

</details>

### pyedb

Higher-Level Pythonic Ansys Electronics Data Base

`pip install pyedb` · installs (wheel) · licence: MIT · rank 12152 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pyedb/) · [docs](https://edb.docs.pyansys.com) · [source](https://github.com/ansys/pyedb)

<details><summary>README extract</summary>

PyEDB is a high-level Python API for processing complex and large layout designs in the
Ansys Electronics Database (EDB) format, which stores information describing designs for
Ansys Electronics Desktop (AEDT).

PyEDB is designed to make EDB automation easier to learn and faster to use. ...

Example:
```python
from pyedb import Edb

edb = Edb(edbpath="myedb.aedb", version="2026.1")

# Your workflow here
# stackup, materials, components, nets, ports, padstacks, cutouts, ...

edb.close()
```

Sections: PyEDB, What is PyEDB?, New user path, Open an EDB project, Advanced: explicitly choose a backend, About PyEDB, What is EDB?, Documentation and issues, Backend guidance

</details>

### ansys-mapdl-reader

Pythonic interface to files generated by MAPDL

`pip install ansys-mapdl-reader` · installs (wheel) · licence: MIT · rank 12556 · last release 2026-05-19 · [PyPI](https://pypi.org/project/ansys-mapdl-reader/)

<details><summary>README extract</summary>

This is the legacy module for reading in binary and ASCII files
generated from MAPDL.

This Python module allows you to extract data directly from binary
ANSYS v14.5+ files and to display or animate them rapidly using a
straightforward API coupled with C libraries based on header files
provided by ANSYS. ...

Example:
```python
from ansys.mapdl import reader as pymapdl_reader
from ansys.mapdl.reader import examples

# Sample *.cdb
filename = examples.hexarchivefile

# Read ansys archive file
archive = pymapdl_reader.Archive(filename)

# Print raw data from cdb
for key in archive.raw:
   print("%s : %s" % (key, archive.raw[key]))

...
```

...

</details>

### ansys-edb-core

A python wrapper for Ansys Edb service

`pip install ansys-edb-core` · installs (wheel) · licence: MIT License · rank 12782 · last release 2026-06-24 · [PyPI](https://pypi.org/project/ansys-edb-core/) · [docs](https://edb.core.docs.pyansys.com) · [source](https://github.com/ansys/pyedb-core)

<details><summary>README extract</summary>

PyEDB-Core is a Python client for the Electronics Database (EDB), a format for storing
information describing designs for Ansys Electronic Desktop (AEDT). Using the PyEDB-Core API,
you can make calls to an EDB server that is running either locally or remotely.

The EDB server can create, edit, read, and write EDB files to disk. ...

Sections: PyEDB-Core, Documentation and issues

</details>

### pyiges

Pythonic IGES reader

`pip install pyiges` · installs (wheel) · licence: MIT License · rank 12843 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pyiges/) · [docs](https://github.com/pyvista/pyiges) · [source](https://github.com/pyvista/pyiges.git)

<details><summary>README extract</summary>

Python IGES reader with basic functionality to read an IGES file and
convert some entities to a `pyvista` or `vtk` mesh.

This module can read in and perform basic parsing of all entities and
can perform additional parsing and geometry visualization of the
following entities:

- Vertex List (Type 502 Form 1)
- Edge List ...

Example:
```python
import pyiges
from pyiges import examples

# load an example impeller
iges = pyiges.read(examples.impeller)

# print an invidiual entity (boring)
print(iges[0])

# convert all lines to a vtk mesh and plot it
lines = iges.to_vtk(bsplines=True, surfaces=False, merge=True)
lines.plot(color='w', line_width=2)

...
```

Sections: pyIGES, Usage, Lines, Surfaces

</details>

### pytetwild

Python wrapper of fTetWild

`pip install pytetwild` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 13171 · last release 2026-08-17 · [PyPI](https://pypi.org/project/pytetwild/)

<details><summary>README extract</summary>

`pytetwild` is a Python library for mesh tetrahedralization. It is a
Python wrapper around the efficient C++ library for tetrahedral meshing provided by
fTetWild.

Example:
```python
import pyvista as pv
import pytetwild

# Load or create a PyVista PolyData surface mesh
# Here, we'll create a simple sphere mesh as an example
surface_mesh = pv.Icosphere(nsub=2)

# Convert the surface mesh to a tetrahedral mesh. For this example let's
# use a coarse mesh
...
```

Sections: pytetwild, Usage, Usage - Sizing Field

</details>

### ansys-tools-visualization-interface

A Python visualization interface for PyAnsys libraries

`pip install ansys-tools-visualization-interface` · installs (wheel) · licence: MIT · rank 13208 · last release 2026-09-25 · [PyPI](https://pypi.org/project/ansys-tools-visualization-interface/) · [docs](https://visualization-interface.tools.docs.pyansys.com/) · [source](https://github.com/ansys/ansys-tools-visualization-interface)

<details><summary>README extract</summary>

Features:
The Visualization Interface Tool is a Python API that provides an interface between PyAnsys libraries and
different plotting backends.

The Visualization Interface Tool offers these main features: ...

Sections: Visualization Interface Tool, Overview, Documentation and issues

</details>

### ansys-units

Pythonic interface for units, unit systems, and unit conversions.

`pip install ansys-units` · installs (wheel) · licence: MIT · rank 13382 · last release 2026-11-05 · [PyPI](https://pypi.org/project/ansys-units/) · [docs](https://units.docs.pyansys.com/) · [source](https://github.com/ansys/pyansys-units)

<details><summary>README extract</summary>

Features:
PyAnsys Units is a Python library designed for managing physical quantities,
which are combinations of numerical values and corresponding units of
measurement. This package facilitates arithmetic operations and conversions
between various units. ...

Example:
```python
import ansys.units as ansunits
from ansys.units.common import m

# Using the pre-defined units in ansys.units.common

volume = 1 * m**3

volume.value  # 1.0
volume.units.name  # "m^3"

# Using unit strings

volume = ansunits.Quantity(value=1, units="m^3")

volume.value  # 1.0
volume.units.name  # "m^3"

# Using Unit instances

...
```

Sections: PyAnsys Units, Overview, Documentation and issues, Getting started, Examples

</details>

### ansys-dpf-core

Data Processing Framework - Python Core

`pip install ansys-dpf-core` · installs (wheel) · licence: MIT · rank 13412 · last release 2026-10-16 · [PyPI](https://pypi.org/project/ansys-dpf-core/) · [docs](https://dpf.docs.pyansys.com/) · [source](https://github.com/ansys/pydpf-core)

<details><summary>README extract</summary>

Ansys Data Processing Framework (DPF) provides numerical simulation
users and engineers with a toolbox for accessing and transforming simulation
data. With DPF, you can perform complex preprocessing or postprocessing of
large amounts of simulation data within a simulation workflow. ...

Example:
```python
>>> from ansys.dpf import core as dpf
>>> from ansys.dpf.core import examples
>>> model = dpf.Model(examples.find_simple_bar())
>>> print(model)

    DPF Model

    Static analysis
    Unit system: Metric (m, kg, N, s, V, A)
    Physics Type: Mechanical
    Available results:
         -  displacement: Nodal Displacement
...
```

Sections: DPF - Ansys Data Processing Framework, Documentation and issues, Brief demo, Starting the service

</details>

### nfl-data-py

python library for interacting with NFL data sourced from nflfastR

`pip install nfl-data-py` · installs (wheel) · licence: MIT License · rank 13831 · last release 2024-09-20 · [PyPI](https://pypi.org/project/nfl-data-py/)

<details><summary>README extract</summary>

nfl_data_py is a Python library for interacting with NFL data sourced from nflfastR, nfldata, dynastyprocess, and Draft Scout.

Includes import functions for play-by-play data, weekly data, seasonal data, rosters, win totals, scoring lines, officials, draft picks, draft pick values, schedules, team descriptive info, combine results and id mappings ...

Example:
```python
import nfl_data_py as nfl
```

Sections: nfl_data_py, Usage, Recognition

</details>

### matrx-rag

Multi-tenant RAG: hybrid retrieval, chunking, embeddings, ingestion, PDF + image + repo pipelines, agent-extraction indexing, priority-aware ranking.

`pip install matrx-rag` · installs (wheel) · licence: MIT License · rank 13911 · last release 2026-10-30 · [PyPI](https://pypi.org/project/matrx-rag/)

<details><summary>README extract</summary>

Multi-tenant RAG: hybrid retrieval, chunking, embeddings, ingestion,
PDF + image + repo pipelines, agent-extraction indexing, NER/KG writes,
priority-aware ranking — extracted from `aidream/services/rag/` so any
host (aidream's cloud server, matrx-local) can consume the same stack. ...

Features:
- Ingestion: `ingest_source(source_kind, source_id, ...)` — chunk → embed → upsert; NER inline for non-code sources.
- PDF / image / code repo pipelines with provenance.
- Hybrid search: pgvector HNSW + lexical FTS → RRF → optional Cohere → MMR. ...

Sections: matrx-rag, What it does, Host integration, Schema

</details>

### ansys-mechanical-stubs

Mechanical scripting API stubs for PyMechanical.

`pip install ansys-mechanical-stubs` · installs (wheel) · licence: MIT License · rank 14333 · last release 2026-08-18 · [PyPI](https://pypi.org/project/ansys-mechanical-stubs/) · [docs](https://scripting.mechanical.docs.pyansys.com) · [source](https://github.com/ansys/mechanical-stubs/)

<details><summary>README extract</summary>

Features:
PyMechanical Stubs generates `init.py` files from assembly files in the Mechanical
application to create python files that can be used for autocomplete with PyMechanical.
Stubs are generated for each version of Mechanical, starting with 2024 R1. ...

Example:
```python
from typing import TYPE_CHECKING
import ansys.mechanical.core as mech

if TYPE_CHECKING:
    import ansys.mechanical.stubs.v261.Ansys as Ansys

geometry_import_group = app.Model.GeometryImportGroup
geometry_import = geometry_import_group.AddGeometryImport()

# Lines that start with "Ansys." will autocomplete as you type
geometry_import_format = (
...
```

Sections: PyMechanical Stubs, Overview, Why clr-stubs?, Manually create _init__.py` files, Basic usage, Documentation and issues

</details>

### ansys-mechanical-core

A python wrapper for Ansys Mechanical

`pip install ansys-mechanical-core` · installs (wheel) · licence: MIT · rank 14352 · last release 2026-10-26 · [PyPI](https://pypi.org/project/ansys-mechanical-core/) · [docs](https://mechanical.docs.pyansys.com) · [source](https://github.com/ansys/pymechanical)

<details><summary>README extract</summary>

Features:
PyMechanical is a Python interface for Ansys Mechanical
(FEA software for structural engineering), enabling automation and integration
of simulation workflows from 2024 R2 and later.

PyMechanical provides two distinct modes of interaction: ...

Example:
```python
from ansys.mechanical.core import App

app = App(globals=globals())
print(app)

# Access Mechanical objects directly
Model.AddStaticStructuralAnalysis()
```

Sections: Overview, Compatibility, Quick start, Troubleshooting

</details>

### tablescope

A lazy table viewer with narwhals-backed query pushdown, for Marimo or Juptyer

`pip install tablescope` · installs (wheel) · licence: MIT · rank 14800 · last release 2026-06-25 · [PyPI](https://pypi.org/project/tablescope/)

<details><summary>README extract</summary>

`tablescope` is a Marimo-oriented lazy table viewer. It accepts a dataframe-like
object that Narwhals can normalize, keeps sort and aggregation work pushed down
to the underlying engine, and renders a Solid + TanStack data grid via
`anywidget`.

Example:
```python
import marimo as mo
import polars as pl
import tablescope

lf = pl.scan_parquet("data.parquet")
viewer = tablescope.view(lf, page_size=100)
viewer
```

Sections: tablescope, Usage, CLI, Databricks, Frontend build, Python workflow

</details>

### gridstatusio

Python client for the GridStatus.io API: normalized electricity market data (load, fuel mix, LMPs, forecasts) from every North American ISO through a single REST API.

`pip install gridstatusio` · installs (wheel) · licence: BSD License · rank 14954 · last release 2026-10-15 · [PyPI](https://pypi.org/project/gridstatusio/) · [docs](https://www.gridstatus.io/api) · [source](https://github.com/gridstatus/gridstatusio/)

<details><summary>README extract</summary>

Features:
The hosted API differs from the open-source `gridstatus` library in several ways:

| Hosted API | Open-source `gridstatus` |

| Consistent column names, timestamp formats, and DST handling | Raw data directly from ISO sources |
| Single REST API | ...

Example:
```python
from gridstatusio import GridStatusClient

client = GridStatusClient()  # reads GRIDSTATUS_API_KEY from the environment

client.list_datasets()

df = client.get_dataset(
    "ercot_fuel_mix",
    start="2024-06-01",
    end="2024-06-02",
    limit=1000,
)
```

Sections: Why the hosted API?, Getting started, Dataset metadata, Return formats, Using without pandas (advanced), Checking your API usage, Retry configuration, Version check, More examples, Resources, Get help

</details>

## Also in this topic

- [networkx](scientific-engineering-bio-informatics.md#networkx) - Python package for creating and manipulating graphs and networks
- [nltk](scientific-engineering.md#nltk) - Natural Language Toolkit
- [snowflake-sqlalchemy](database.md#snowflake-sqlalchemy) - Snowflake SQLAlchemy Dialect
- [streamlit](database-front-ends.md#streamlit) - A faster way to build and share data apps
- [leather](multimedia-graphics.md#leather) - Python charting for 80% of humans.
- [htmldate](internet-www-http.md#htmldate) - Fast and robust extraction of original and updated publication dates from URLs and web pages.
- [courlan](internet-www-http.md#courlan) - Clean, filter and sample URLs to optimize data collection – includes spam, content type and language filters.
- [trafilatura](internet-www-http.md#trafilatura) - Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extraction, output as CSV, JSON, HTML, MD, TXT, XML.
- [snowflake-snowpark-python](database.md#snowflake-snowpark-python) - Snowflake Snowpark for Python
- [torchmetrics](scientific-engineering-artificial-intelligence.md#torchmetrics) - PyTorch native Metrics
- [clickhouse-driver](database.md#clickhouse-driver) - Python driver with native interface for ClickHouse
- [pytorch-lightning](scientific-engineering-artificial-intelligence.md#pytorch-lightning) - PyTorch Lightning is the lightweight PyTorch wrapper for ML researchers. Scale your models. Write less boilerplate.
- [cytoolz](scientific-engineering.md#cytoolz) - Cython implementation of Toolz: High performance functional utilities
- [python-crfsuite](scientific-engineering.md#python-crfsuite) - Python binding for CRFsuite
- [bokeh](office-business.md#bokeh) - Interactive plots and applications in the browser from Python
- [probableparsing](scientific-engineering.md#probableparsing) - Common methods for propbable parsers
- [usaddress](scientific-engineering.md#usaddress) - Parse US addresses using conditional random fields
- [jaxtyping](scientific-engineering-artificial-intelligence.md#jaxtyping) - Type annotations and runtime checking for shape and dtype of JAX/NumPy/PyTorch/etc. arrays.
- [docling-core](database.md#docling-core) - A python library to define and validate data types in Docling.
- [vtk](multimedia-graphics.md#vtk) - VTK is an open-source toolkit for 3D computer graphics, image processing, and visualization
- [intervaltree](scientific-engineering-artificial-intelligence.md#intervaltree) - Editable interval tree data structure for Python 2 and 3
- [lightning](scientific-engineering-artificial-intelligence.md#lightning) - The Deep Learning framework to train, deploy, and ship AI products Lightning fast.
- [pysbd](scientific-engineering.md#pysbd) - pysbd (Python Sentence Boundary Disambiguation) is a rule-based sentence boundary detection that works out-of-the-box across many languages.
- [datasketch](database.md#datasketch) - Probabilistic data structures for processing and searching very large datasets
- [snowflake.core](database.md#snowflakecore) - Snowflake Python API for Resource Management
- [formulas](scientific-engineering.md#formulas) - Parse and compile Excel formulas and workbooks in python code.
- [schedula](scientific-engineering.md#schedula) - Produce a plan that dispatches calls based on a graph of functions, satisfying data dependencies.
- [igraph](scientific-engineering.md#igraph) - High performance graph data structures and algorithms
- [gensim](scientific-engineering-artificial-intelligence.md#gensim) - Python framework for fast Vector Space Modelling
- [simsimd](scientific-engineering-artificial-intelligence.md#simsimd) - Portable mixed-precision BLAS-like vector math library for x86 and ARM
- [clickhouse-sqlalchemy](database.md#clickhouse-sqlalchemy) - Simple ClickHouse SQLAlchemy Dialect
- [vllm](scientific-engineering-artificial-intelligence.md#vllm) - A high-throughput and memory-efficient inference and serving engine for LLMs
- [stringzilla](file-formats.md#stringzilla) - Search, hash, sort, and process strings faster via SWAR and SIMD
- [snowflake.-legacy](database.md#snowflake-legacy) - You should switch to the snowflake-uuid package
- [snowflake](database.md#snowflake) - Snowflake Python API
- [equinox](scientific-engineering-artificial-intelligence.md#equinox) - Elegant easy-to-use neural networks in JAX.
- [svgpathtools](multimedia-graphics.md#svgpathtools) - A collection of tools for manipulating and analyzing SVG Path objects and Bezier curves.
- [chonkie](scientific-engineering-artificial-intelligence.md#chonkie) - 🦛 CHONK your texts with Chonkie ✨ - The no-nonsense chunking library
- [awkward-cpp](scientific-engineering.md#awkward-cpp) - CPU kernels and compiled extensions for Awkward Array
- [awkward](scientific-engineering.md#awkward) - Manipulate JSON-like data with NumPy-like idioms.
- [webrtcvad-wheels](scientific-engineering-artificial-intelligence.md#webrtcvad-wheels) - Python interface to the Google WebRTC Voice Activity Detector (VAD) [released with binary wheels!]
- [panel](office-business.md#panel) - The powerful data exploration & web app framework for Python.
- [edgartools](office-business-financial.md#edgartools) - Python library to access and analyze SEC Edgar filings, XBRL financial statements, 10-K, 10-Q, and 8-K reports
- [boost-histogram](scientific-engineering.md#boost-histogram) - The Boost::Histogram Python wrapper.
- [stanza](scientific-engineering.md#stanza) - A Python NLP Library for Many Human Languages, by the Stanford NLP Group
- [simpleitk](scientific-engineering.md#simpleitk) - SimpleITK is a simplified interface to the Insight Toolkit (ITK) for image registration and segmentation
- [proxy.py](internet.md#proxypy) - \u26a1 Fast \u2022 \U0001fab6 Lightweight \u2022 \U0001f51f Dependency \u2022 \U0001f50c Pluggable \u2022 \U0001f608 TLS interception \u2022 \U0001f512 DNS-over-HTTPS \u2022 \U0001f525 Poor Mans VPN \u2022 \u23ea Reverse & \u23e9 Forward \u2022 \U0001f46e\U0001f3ff Proxy Server framework \u2022 \U0001f310 Web Server framework \u2022 \u27b5 \u27b6 \u27b7 \u27a0 PubSub framework \u2022 \U0001f477 Work acceptor & executor framework.
- [uproot](scientific-engineering.md#uproot) - ROOT I/O in pure Python and NumPy.
- [sigfig](education.md#sigfig) - Python library for rounding numbers (with expected results)
- [hist](scientific-engineering.md#hist) - Hist classes and utilities
- [prefixcommons](scientific-engineering-bio-informatics.md#prefixcommons) - A python API for working with ID prefixes
- [weave](database-front-ends.md#weave) - A toolkit for building composable interactive data driven applications.
- [pymatgen](scientific-engineering-chemistry.md#pymatgen) - Python Materials Genomics is a robust materials analysis code that defines core object representations for structures and molecules with support for many electronic structure codes. It is currently the core analysis code powering the Materials Project (https://materialsproject.org).
- [mlxtend](scientific-engineering.md#mlxtend) - Machine Learning Library Extensions
- [spark-nlp](scientific-engineering.md#spark-nlp) - John Snow Labs Spark NLP is a natural language processing library built on top of Apache Spark ML. It provides simple, performant & accurate NLP annotations for machine learning pipelines, that scale easily in a distributed environment.
- [webrtcvad](scientific-engineering-artificial-intelligence.md#webrtcvad) - Python interface to the Google WebRTC Voice Activity Detector (VAD)
- [pymatgen-io-validation](scientific-engineering.md#pymatgen-io-validation) - A comprehensive I/O validator for electronic structure calculations
- [ibm-watsonx-ai](internet.md#ibm-watsonx-ai) - IBM watsonx.ai API Client
- [monai](scientific-engineering.md#monai) - AI Toolkit for Healthcare Imaging
- [python-igraph](scientific-engineering.md#python-igraph) - High performance graph data structures and algorithms (legacy package)
- [pymatgen-core](scientific-engineering-chemistry.md#pymatgen-core) - Python Materials Genomics is a robust materials analysis code that defines core object representations for structures and molecules with support for many electronic structure codes. It is currently the core analysis code powering the Materials Project (https://materialsproject.org). This repository is for pymatgen-core, which implements the core data structures and algorithms.
- [numkong](scientific-engineering-artificial-intelligence.md#numkong) - Portable mixed-precision math, linear-algebra, & retrieval library with 2000+ SIMD kernels for x86, Arm, RISC-V, LoongArch, Power, & WebAssembly
- [tinysegmenter](scientific-engineering-artificial-intelligence.md#tinysegmenter) - Very compact Japanese tokenizer
- [lineax](scientific-engineering-artificial-intelligence.md#lineax) - Linear solvers in JAX and Equinox.
- [osmnx](scientific-engineering-gis.md#osmnx) - Download, model, analyze, and visualize street networks and other geospatial features from OpenStreetMap
- [dissect.cstruct](internet-log-analysis.md#dissectcstruct) - A Dissect module implementing a parser for C-like structures: structure parsing in Python made easy
- [planarity](scientific-engineering.md#planarity) - Python Wrapper for the Edge Addition Planarity Suite and Graph Library
- [mplfinance](office-business-financial.md#mplfinance) - Utilities for the visualization, and visual analysis, of financial data
- [optimistix](scientific-engineering-artificial-intelligence.md#optimistix) - Nonlinear optimisation in JAX and Equinox.
- [pandas-ta](office-business-financial.md#pandas-ta) - A Comprehensive Python 3 Technical Analysis Library with Pandas Dataframe Extension for Quantitative Researchers, Traders, and Investors.
- [clickhouse-cityhash](internet.md#clickhouse-cityhash) - Python-bindings for CityHash, a fast non-cryptographic hash algorithm
- [pytools](scientific-engineering.md#pytools) - A collection of tools for Python
- [autogluon.tabular](scientific-engineering-artificial-intelligence.md#autogluontabular) - Fast and Accurate ML in 3 Lines of Code
- [autogluon.core](scientific-engineering-artificial-intelligence.md#autogluoncore) - Fast and Accurate ML in 3 Lines of Code
- [POT](scientific-engineering-artificial-intelligence.md#pot) - Python Optimal Transport Library
- [quantstats](office-business-financial.md#quantstats) - Portfolio analytics for quants
- [vectorbt](office-business-financial.md#vectorbt) - Python library for backtesting and analyzing trading strategies at scale
- [autogluon.features](scientific-engineering-artificial-intelligence.md#autogluonfeatures) - Fast and Accurate ML in 3 Lines of Code
- [pybaselines](scientific-engineering.md#pybaselines) - A library of algorithms for the baseline correction of experimental data.
- [autogluon.common](scientific-engineering-artificial-intelligence.md#autogluoncommon) - Fast and Accurate ML in 3 Lines of Code
- [diffrax](scientific-engineering-artificial-intelligence.md#diffrax) - GPU+autodiff-capable ODE/SDE/CDE solvers written in JAX.
- [GDAL](scientific-engineering-gis.md#gdal) - GDAL: Geospatial Data Abstraction Library
- [lasio](scientific-engineering.md#lasio) - Read/write well data from Log ASCII Standard (LAS) files
- [chalkpy](scientific-engineering-artificial-intelligence.md#chalkpy) - Python SDK for Chalk
- [pyvista-cad](multimedia-graphics.md#pyvista-cad) - PyVista accessor and reader-registry plugin for CAD formats (STEP, IGES, BREP, DXF, 3MF, IFC, FCStd) and bridges to build123d, cadquery, and OCP.
- [bitmath](communications-file-sharing.md#bitmath) - Pythonic module for representing and manipulating file sizes with different prefix notations (file size unit conversion)
- [dissect.util](internet-log-analysis.md#dissectutil) - A Dissect module implementing various utility functions for the other Dissect modules
- [doped](scientific-engineering-chemistry.md#doped) - Python package to setup, process and analyse solid-state defect calculations with VASP
- [vector](scientific-engineering.md#vector) - Vector classes and utilities
- [pyAgrum-nightly](scientific-engineering-artificial-intelligence.md#pyagrum-nightly) - Bayesian networks and other Probabilistic Graphical Models.
- [snowflake-telemetry-python](database.md#snowflake-telemetry-python) - Snowflake Telemetry for Python
- [litdata](scientific-engineering-artificial-intelligence.md#litdata) - The Deep Learning framework to train, deploy, and ship AI products Lightning fast.
- [eql](database.md#eql) - Event Query Language
- [hachoir](multimedia.md#hachoir) - Package of Hachoir parsers used to open binary files
- [pyroomacoustics](multimedia-sound-audio.md#pyroomacoustics) - A simple framework for room acoustics and audio processing in Python.
- [snowflake-ml-python](database.md#snowflake-ml-python) - The machine learning client library that is used for interacting with Snowflake to build machine learning solutions.
- [coffea](scientific-engineering.md#coffea) - Basic tools and wrappers for enabling not-too-alien syntax when running columnar Collider HEP analysis.
- [tangled-up-in-unicode](database.md#tangled-up-in-unicode) - Access to the Unicode Character Database (UCD)
- [probablepeople](scientific-engineering.md#probablepeople) - Parse romanized names & companies using advanced NLP methods
- [fiftyone-brain](scientific-engineering-artificial-intelligence.md#fiftyone-brain) - FiftyOne Brain
- [pandas-ta-classic](office-business-financial.md#pandas-ta-classic) - Technical Analysis Indicators - Pandas TA Classic is an easy to use Python 3 Pandas Extension with a comprehensive collection of indicators and TA-Lib patterns.
- [kreuzberg](office-business.md#kreuzberg) - High-performance document intelligence library for Python. Extract text, metadata, and structured data from PDFs, Office documents, images, and 88+ formats. Powered by Rust core for 10-50x speed improvements.
- [fiftyone-db](scientific-engineering-artificial-intelligence.md#fiftyone-db) - FiftyOne DB
- [voxel51-eta](scientific-engineering-artificial-intelligence.md#voxel51-eta) - Extensible Toolkit for Analytics
- [fasttext-langdetect](scientific-engineering-artificial-intelligence.md#fasttext-langdetect) - 80x faster and 95% accurate language identification with fastText
- [sdmx1](scientific-engineering.md#sdmx1) - Statistical Data and Metadata eXchange (SDMX)
- [databend-driver](database.md#databend-driver) - Databend Driver Python Binding
- [cwltool](scientific-engineering.md#cwltool) - Common workflow language reference implementation
- [autogluon.timeseries](scientific-engineering-artificial-intelligence.md#autogluontimeseries) - Fast and Accurate ML in 3 Lines of Code
- [dissect.ntfs](internet-log-analysis.md#dissectntfs) - A Dissect module implementing a parser for the NTFS file system, used by the Windows operating system
- [cwl-utils](file-formats.md#cwl-utils) - 
- [eventregistry](internet-www-http.md#eventregistry) - A package that can be used to query information in Event Registry (https://eventregistry.org/)
- [fiftyone](scientific-engineering-artificial-intelligence.md#fiftyone) - FiftyOne: the open-source tool for building high-quality datasets and computer vision models
- [h2o](scientific-engineering-artificial-intelligence.md#h2o) - H2O, Fast Scalable Machine Learning, for python
- [mixpanel-headless](database.md#mixpanel-headless) - Python library for working with Mixpanel analytics data, designed for AI coding agents
- [grafana-client](communications.md#grafana-client) - A client library for accessing the Grafana HTTP API, written in Python
- [graph-retriever](scientific-engineering-artificial-intelligence.md#graph-retriever) - Retriever combining unstructured similarity and structured document traversal.
- [langchain-graph-retriever](scientific-engineering-artificial-intelligence.md#langchain-graph-retriever) - LangChain retriever for traversing document graphs on top of vector-based similarity search.
- [arcgis](internet-www-http.md#arcgis) - ArcGIS API for Python
- [highdicom](multimedia-graphics.md#highdicom) - High-level DICOM abstractions.
- [autogluon](scientific-engineering-artificial-intelligence.md#autogluon) - Fast and Accurate ML in 3 Lines of Code
- [ndex2](scientific-engineering-bio-informatics.md#ndex2) - Nice CX Python includes a client and a data model.
- [dissect.esedb](internet-log-analysis.md#dissectesedb) - Superseded by dissect.database. A Dissect module implementing a parser for Microsofts Extensible Storage Engine Database (ESEDB), used for example in Active Directory, Exchange and Windows Update
- [py-vollib-vectorized](office-business-financial.md#py-vollib-vectorized) - A fast, vectorized approach to calculating Implied Volatility and Greeks using the Black, Black-Scholes and Black-Scholes-Merton pricing.
- [fastdigest](scientific-engineering.md#fastdigest) - A fast t-digest library for Python built on Rust.
- [napari-plugin-engine](scientific-engineering.md#napari-plugin-engine) - napari plugin engine, fork of pluggy
- [napari](scientific-engineering.md#napari) - n-dimensional array viewer in Python
- [networkit](scientific-engineering-bio-informatics.md#networkit) - NetworKit is a toolbox for high-performance network analysis
- [analytics-mcp](internet.md#analytics-mcp) - MCP server for Google Analytics
- [sumy](education.md#sumy) - Module for automatic summarization of text documents and HTML pages.
- [autogluon.multimodal](scientific-engineering-artificial-intelligence.md#autogluonmultimodal) - Fast and Accurate ML in 3 Lines of Code
- [quadrilateral-fitter](scientific-engineering-artificial-intelligence.md#quadrilateral-fitter) - QuadrilateralFitter is an efficient and easy-to-use Python library for fitting irregular quadrilaterals from irregular polygons or any noisy data.
- [itk-core](scientific-engineering-2.md#itk-core) - ITK is an open-source toolkit for multidimensional image analysis
- [datamol](scientific-engineering-artificial-intelligence.md#datamol) - A python library to work with molecules. Built on top of RDKit.
- [pylakekeeper](database.md#pylakekeeper) - Official Lakekeeper client — generic-tables API and OAuth2 auth (static token / client_credentials with refresh)
- [fastcluster](scientific-engineering-artificial-intelligence.md#fastcluster) - Fast hierarchical clustering routines for R and Python.
- [itk-filtering](scientific-engineering-2.md#itk-filtering) - ITK is an open-source toolkit for multidimensional image analysis
- [itk-numerics](scientific-engineering-2.md#itk-numerics) - ITK is an open-source toolkit for multidimensional image analysis
- [censys](documentation-sphinx.md#censys) - An easy-to-use and lightweight API wrapper for Censys APIs (censys.io).
- [itk](scientific-engineering-2.md#itk) - ITK is an open-source toolkit for multidimensional image analysis
- [itk-io](scientific-engineering-2.md#itk-io) - ITK is an open-source toolkit for multidimensional image analysis
- [suitesparse-graphblas](scientific-engineering-2.md#suitesparse-graphblas) - SuiteSparse:GraphBLAS Python bindings.
- [itk-segmentation](scientific-engineering-2.md#itk-segmentation) - ITK is an open-source toolkit for multidimensional image analysis
- [ridgeplot](scientific-engineering-2.md#ridgeplot) - Beautiful ridgeline plots in python
- [itk-registration](scientific-engineering-2.md#itk-registration) - ITK is an open-source toolkit for multidimensional image analysis
- [sec-parser](office-business-financial.md#sec-parser) - Parse SEC EDGAR HTML documents into a tree of elements that correspond to the visual structure of the document.
- [ft-pandas-ta](office-business-financial.md#ft-pandas-ta) - An easy to use Python 3 Pandas Extension with 130+ Technical Analysis Indicators. Can be called from a Pandas DataFrame or standalone like TA-Lib. Correlation tested with TA-Lib.
- [lmcache](scientific-engineering-artificial-intelligence.md#lmcache) - A LLM serving engine extension to reduce TTFT and increase throughput, especially under long-context scenarios.
- [st-theme](database-front-ends.md#st-theme) - A component that returns the active theme of the Streamlit app.
- [xlcalculator](office-business-financial.md#xlcalculator) - Converts MS Excel formulas to Python and evaluates them.
- [chalk-remote-call-python](scientific-engineering-artificial-intelligence.md#chalk-remote-call-python) - Chalk remote call Python runtime interface client
- [news-please](internet.md#news-please) - news-please is an open source easy-to-use news extractor that just works.
- [highcharts-core](internet-www-http-2.md#highcharts-core) - High-end Data Visualization for the Python Ecosystem. Official wrapper for Highcharts Core (JS).
- [dicomweb-client](internet-www-http-2.md#dicomweb-client) - Client for DICOMweb RESTful services.
- [pytextrank](scientific-engineering-artificial-intelligence.md#pytextrank) - Python implementation of TextRank as a spaCy pipeline extension, for graph-based natural language work plus related knowledge graph practices; used for for phrase extraction of text documents.
- [trendspy](internet.md#trendspy) - A Python library for accessing Google Trends data
- [qiskit-connector](scientific-engineering-2.md#qiskit-connector) - Quantum Computing Qiskit Connector For Quantum Backend Use In Realtime
- [pyaedt](scientific-engineering-electronic-design-automation-eda.md#pyaedt) - High-level Python API for Ansys Electronics Desktop Framework
- [keyphrase-vectorizers](scientific-engineering-artificial-intelligence.md#keyphrase-vectorizers) - Set of vectorizers that extract keyphrases with part-of-speech patterns from a collection of text documents and convert them into a document-keyphrase matrix.
- [konlpy](scientific-engineering-2.md#konlpy) - Python package for Korean natural language processing.
- [pyxDamerauLevenshtein](scientific-engineering-bio-informatics.md#pyxdameraulevenshtein) - pyxDamerauLevenshtein implements the Damerau-Levenshtein (DL) edit distance algorithm for Python in Cython for high performance.
- [dissect.target](internet-log-analysis.md#dissecttarget) - This module ties all other Dissect modules together, it provides a programming API and command line tools which allow easy access to various data sources inside disk images or file collections (a.k.a. targets)
- [pystempel](scientific-engineering-2.md#pystempel) - Polish stemmer.
- [torchtyping](scientific-engineering-artificial-intelligence.md#torchtyping) - Runtime type annotations for the shape, dtype etc. of PyTorch Tensors.
- [easydev](scientific-engineering-bio-informatics.md#easydev) - Common utilities to ease development of Python packages
- [pymantic](internet-www-http-2.md#pymantic) - Semantic Web and RDF library for Python
- [vowpalwabbit](scientific-engineering-2.md#vowpalwabbit) - Vowpal Wabbit Python package
- [pygdal](scientific-engineering-gis.md#pygdal) - Virtualenv and setuptools friendly version of standard GDAL python bindings
