# Text Processing / General

[Index](README.md) · 8 packages in this topic, 57 more listed under another topic, by downloads.

### anyascii

Unicode to ASCII transliteration

`pip install anyascii` · installs (wheel) · licence: ISC License (ISCL) · rank 1974 · last release 2025-06-29 · [PyPI](https://pypi.org/project/anyascii/)

<details><summary>README extract</summary>

Unicode to ASCII transliteration

Web Demo

Converts Unicode characters to their best ASCII representation

AnyAscii provides ASCII-only replacement strings for practically all Unicode characters. Text is converted character-by-character without considering the context. ...

Example:
```python
from anyascii import anyascii

s = anyascii('άνθρωποι')
assert s == 'anthropoi'
```

</details>

### pyjson5

JSON5 serializer and parser for Python 3 written in Cython.

`pip install pyjson5` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 2165 · last release 2026-05-15 · [PyPI](https://pypi.org/project/pyjson5/) · [docs](https://pyjson5.readthedocs.io/) · [source](https://github.com/Kijewski/pyjson5)

<details><summary>README extract</summary>

A JSON5 serializer and parser library for Python 3 written in
Cython.

The serializer returns ASCII data that can safely be used in an HTML template.
Apostrophes, ampersands, greater-than, and less-then signs are encoded as
unicode escaped sequences. E.g. this snippet is safe for any and all input: ...

Sections: PyJSON5, Serializer, Parser, Functions, Compatibility

</details>

### tabula-py

Simple wrapper for tabula-java, read tables from PDF into DataFrame

`pip install tabula-py` · installs (wheel) · licence: MIT License · rank 3576 · last release 2024-10-17 · [PyPI](https://pypi.org/project/tabula-py/)

<details><summary>README extract</summary>

`tabula-py` is a simple Python wrapper of tabula-java, which can read tables in a PDF.
You can read tables from a PDF and convert them into a pandas DataFrame. tabula-py also enables you to convert a PDF file into a CSV, a TSV or a JSON file. ...

Example:
```python
import tabula

# Read pdf into list of DataFrame
dfs = tabula.read_pdf("test.pdf", pages='all')

# Read remote pdf into list of DataFrame
dfs2 = tabula.read_pdf("

# convert PDF into CSV file
tabula.convert_into("test.pdf", "output.csv", output_format="csv", pages='all')

# convert all PDFs in a directory
...
```

Sections: tabula-py, Requirements, OS, Usage, Example

</details>

### pytrec-eval-terrier

Provides Python bindings for popular Information Retrieval measures implemented within trec_eval.

`pip install pytrec-eval-terrier` · installs (wheel) · licence: MIT License · rank 4333 · last release 2026-10-16 · [PyPI](https://pypi.org/project/pytrec-eval-terrier/)

### strsimpy

A library implementing different string similarity and distance measures

`pip install strsimpy` · installs (wheel) · licence: MIT · rank 6079 · last release 2026-11-05 · [PyPI](https://pypi.org/project/strsimpy/) · [source](https://github.com/luozhouyang/python-string-similarity)

<details><summary>README extract</summary>

Rust implementation with Python bindings of tdebatty/java-string-similarity

A library implementing different string similarity and distance measures. A dozen of algorithms (including Levenshtein edit distance and sibblings, Jaro-Winkler, Longest Common Subsequence, cosine similarity etc.) are currently implemented. ...

Features:
The main characteristics of each implemented algorithm are presented below. The "cost" column gives an estimation of the computational cost to compute the similarity between two strings of length m and n respectively. ...

Example:
```python
from strsimpy import (
    Levenshtein, NormalizedLevenshtein, WeightedLevenshtein,
    Damerau, OptimalStringAlignment, JaroWinkler,
    LongestCommonSubsequence, MetricLCS, NGram,
...

</details>

### ranx

ranx: A Blazing-Fast Python Library for Ranking Evaluation, Comparison, and Fusion

`pip install ranx` · installs (wheel) · licence: MIT License · rank 10037 · last release 2025-08-07 · [PyPI](https://pypi.org/project/ranx/)

<details><summary>README extract</summary>

.svg" alt="Documentation Status">

ranx ([raŋks]) is a library of fast ranking evaluation metrics implemented in Python, leveraging Numba for high-speed vector operations and automatic parallelization.
It offers a user-friendly interface to evaluate and compare Information Retrieval and Recommender Systems. ...

Example:
```python
qrels = Qrels.from_ir_datasets("msmarco-document/dev")
```

Sections: ⚡️ Introduction, ✨ Features, Metrics, Statistical Tests, Off-the-shelf Qrels, Off-the-shelf Runs, Fusion Algorithms, Normalization Strategies, 🔌 Requirements, 💡 Usage, Create Qrels and Run, Evaluate, Compare, Fusion

</details>

### pytrec-eval

Provides Python bindings for popular Information Retrieval measures implemented within trec_eval.

`pip install pytrec-eval` · installs from source (sdist only) · licence: MIT License · rank 12487 · last release 2020-09-07 · [PyPI](https://pypi.org/project/pytrec-eval/)

### uctools

Unicode tools.

`pip install uctools` · installs from source (sdist only) · licence: MIT License · rank 13035 · last release 2020-07-14 · [PyPI](https://pypi.org/project/uctools/)

<details><summary>README extract</summary>

Tools for showing information about unicode characters (UTF-8) and
performing normalization.

Copyright ® 2018, Luís Gomes <luismsgomes@gmail.com>.

The following command line tools are provided:

 ucinfo
 writes on stdout the name of each unicode character read from stdin

 ucenum
 enumerates on stdout all unicode characters of a chosen category ...

Sections: uctools, ucinfo, ucenum, ucnorm

</details>

## Also in this topic

- [regex](scientific-engineering-information-analysis.md#regex) - Alternative regular expression module, to replace re.
- [docutils](documentation.md#docutils) - Docutils -- Python Documentation Utilities
- [lark](software-development-libraries.md#lark) - a modern parsing library
- [humanize](text-processing.md#humanize) - Python humanize utilities
- [humanfriendly](communications.md#humanfriendly) - Human friendly output for text interfaces using Python
- [nltk](scientific-engineering.md#nltk) - Natural Language Toolkit
- [Sphinx](documentation.md#sphinx) - Python documentation generator
- [parsimonious](scientific-engineering-information-analysis.md#parsimonious) - (Soon to be) the fastest pure-Python PEG parser I could muster
- [pylatexenc](scientific-engineering.md#pylatexenc) - Simple LaTeX parser providing latex-to-unicode and unicode-to-latex conversion
- [python-stdnum](office-business-financial.md#python-stdnum) - Python module to handle standardized numbers and codes
- [intervaltree](scientific-engineering-artificial-intelligence.md#intervaltree) - Editable interval tree data structure for Python 2 and 3
- [jaconv](text-processing.md#jaconv) - Pure-Python Japanese character interconverter for Hiragana, Katakana, Hankaku, Zenkaku and more
- [semchunk](scientific-engineering-artificial-intelligence.md#semchunk) - A Python library for splitting text into smaller chunks while preserving as much local semantic context as possible.
- [xhtml2pdf](documentation.md#xhtml2pdf) - PDF generator using HTML and CSS
- [pdfkit](text-processing.md#pdfkit) - Wkhtmltopdf python wrapper to convert html to pdf using the webkit rendering engine and qt
- [lark-parser](software-development-libraries.md#lark-parser) - a modern parsing library
- [python-iso639](text-processing.md#python-iso639) - ISO 639 language codes, names, and other associated information
- [stringzilla](file-formats.md#stringzilla) - Search, hash, sort, and process strings faster via SWAR and SIMD
- [jaro-winkler](text-processing.md#jaro-winkler) - Original, standard and customisable versions of the Jaro-Winkler functions.
- [csscompressor](software-development-build-tools.md#csscompressor) - A python port of YUI CSS Compressor
- [esprima](software-development-code-generators.md#esprima) - ECMAScript parsing infrastructure for multipurpose analysis in Python
- [art](multimedia.md#art) - ASCII Art Library For Python
- [pythainlp](scientific-engineering-artificial-intelligence.md#pythainlp) - Thai Natural Language Processing library
- [empy](software-development-interpreters.md#empy) - A templating system for Python.
- [cpsat-logutils](scientific-engineering-mathematics.md#cpsat-logutils) - Parse CP-SAT (OR-Tools) solver logs into line-anchored, JSON-serializable pydantic models.
- [uroman](text-processing.md#uroman) - uroman is a universal romanizer. It converts text in any script to the standard Latin alphabet.
- [TatSu](software-development-compilers.md#tatsu) - TatSu takes a grammar in a variation of EBNF as input, and outputs a memoizing PEG/Packrat parser in Python.
- [imgkit](text-processing.md#imgkit) - Wkhtmltopdf python wrapper to convert html to image using the webkit rendering engine and qt
- [django-autoslug](software-development-libraries-3.md#django-autoslug) - An automated slug field for Django.
- [gibberish-detector](software-development-libraries-3.md#gibberish-detector) - Detects gibberish strings.
- [cdifflib](software-development.md#cdifflib) - C implementation of parts of difflib
- [phonetics](internet-www-http.md#phonetics) - Compute phonetic key of strings for indexing or fuzzy matching
- [tangled-up-in-unicode](database.md#tangled-up-in-unicode) - Access to the Unicode Character Database (UCD)
- [kreuzberg](office-business.md#kreuzberg) - High-performance document intelligence library for Python. Extract text, metadata, and structured data from PDFs, Office documents, images, and 88+ formats. Powered by Rust core for 10-50x speed improvements.
- [pdf-oxide](scientific-engineering-information-analysis.md#pdf-oxide) - The fastest Python PDF library — 0.8ms mean, 5× faster than the industry leaders, 100% pass rate on 3,830 real-world PDFs. Text extraction, Markdown/HTML conversion, PDF creation and editing.
- [json-diff](software-development-libraries-3.md#json-diff) - Generates diff between two JSON files
- [humps](software-development.md#humps) - camelCase converter
- [nvidia-sphinx-theme](documentation.md#nvidia-sphinx-theme) - A Sphinx theme for NVIDIA projects
- [eventregistry](internet-www-http.md#eventregistry) - A package that can be used to query information in Event Registry (https://eventregistry.org/)
- [mwxml](scientific-engineering.md#mwxml) - A set of utilities for processing MediaWiki XML dump data.
- [mwtypes](scientific-engineering.md#mwtypes) - A set of types for processing MediaWiki data.
- [mwcli](scientific-engineering.md#mwcli) - Utilities for processing MediaWiki on the command line.
- [sphinx-intl](documentation.md#sphinx-intl) - Sphinx utility that make it easy to translate and to apply translation.
- [kitchen](software-development-internationalization.md#kitchen) - Kitchen contains a cornucopia of useful code
- [lark-js](software-development-libraries-3.md#lark-js) - An extension to Lark that generates a Javascript standalone
- [asciimatics](software-development-user-interfaces.md#asciimatics) - A cross-platform package to replace curses (mouse/keyboard input & text colours/positioning) and create ASCII animations
- [chompjs](software-development-libraries-4.md#chompjs) - Parsing JavaScript objects into Python dictionaries
- [fortranformat](scientific-engineering-2.md#fortranformat) - Mimics Fortran textual IO in Python.
- [pytextrank](scientific-engineering-artificial-intelligence.md#pytextrank) - Python implementation of TextRank as a spaCy pipeline extension, for graph-based natural language work plus related knowledge graph practices; used for for phrase extraction of text documents.
- [formualizer](office-business-financial.md#formualizer) - Embeddable spreadsheet engine — parse, evaluate & mutate Excel workbooks at native speed
- [Fuzzy](text-processing.md#fuzzy) - Fast Python phonetic algorithms
- [vsg](software-development-quality-assurance.md#vsg) - VHDL Style Guide
- [konlpy](scientific-engineering-2.md#konlpy) - Python package for Korean natural language processing.
- [pystempel](scientific-engineering-2.md#pystempel) - Polish stemmer.
- [TatSu-LTS](software-development-code-generators.md#tatsu-lts) - TatSu takes a grammar in a variation of EBNF as input, and outputs a memoizing PEG/Packrat parser in Python.
- [isbnlib](software-development-libraries-5.md#isbnlib) - Extract, clean, transform, hyphenate and metadata for ISBNs (International Standard Book Number).
- [emoji-country-flag](communications-chat.md#emoji-country-flag) - En/Decode unicode country flags emoji
