# Text Processing

[Index](README.md) · 60 packages in this topic, 122 more listed under another topic, by downloads.

### tinycss2

A tiny CSS parser

`pip install tinycss2` · installs (wheel) · licence: BSD License · rank 270 · last release 2025-11-23 · [PyPI](https://pypi.org/project/tinycss2/) · [docs](https://doc.courtbouillon.org/tinycss2/) · [source](https://github.com/Kozea/tinycss2/)

<details><summary>README extract</summary>

tinycss2 is a low-level CSS parser and generator written in Python: it can
parse strings, return objects representing tokens and blocks, and generate CSS
strings corresponding to these objects. ...

</details>

### pdfminer.six

PDF parser and analyzer

`pip install pdfminer.six` · installs (wheel) · licence: MIT · rank 385 · last release 2026-01-07 · [PyPI](https://pypi.org/project/pdfminer.six/)

<details><summary>README extract</summary>

*We fathom PDF*

Pdfminer.six is a community maintained fork of the original PDFMiner. It is a tool for extracting information from PDF
documents. It focuses on getting and analyzing text data. Pdfminer.six extracts the text from a page directly from the
sourcecode of the PDF. ...

</details>

### humanize

Python humanize utilities

`pip install humanize` · installs (wheel) · licence: MIT · rank 445 · last release 2026-06-30 · [PyPI](https://pypi.org/project/humanize/) · [docs](https://humanize.readthedocs.io/) · [source](https://github.com/python-humanize/humanize)

<details><summary>README extract</summary>

This modest package contains various common humanization utilities, like turning a
number into a fuzzy human-readable duration ("3 minutes ago") or into a human-readable
size or throughput. It is localized to:

- Arabic
- Basque
- Bengali
- Brazilian Portuguese
- Catalan
- Danish
- Dutch
- Esperanto
- European Portuguese
- Finnish
- French ...

Example:
```python
>>> import humanize
>>> humanize.intcomma(12345)
'12,345'
>>> humanize.intword(123455913)
'123.5 million'
>>> humanize.intword(12345591313)
'12.3 billion'
>>> humanize.apnumber(4)
'four'
>>> humanize.apnumber(41)
'41'
```

...

</details>

### prettytable

A simple Python library for easily displaying tabular data in a visually appealing ASCII table format

`pip install prettytable` · installs (wheel) · licence: BSD-3-Clause · rank 490 · last release 2026-06-22 · [PyPI](https://pypi.org/project/prettytable/) · [source](https://github.com/prettytable/prettytable)

<details><summary>README extract</summary>

PrettyTable lets you print tables in an attractive ASCII form:

Example:
```python
from prettytable import PrettyTable
from typing import Any
from termcolor import colored

def _colored(field: str, val: Any) -> str:
    if isinstance(val, (int, float)):
        if val >= 0:
            return colored(f"{val:.2f}", "green")
        return colored(f"{val:.2f}", "red")
    elif isinstance(val, str):
...
```

Sections: PrettyTable, Demo, Tutorial on how to use the PrettyTable API, Getting your data into (and out of) the table, Row by row, All rows at once, Column by column, Mixing and matching, Importing data from a CSV file, Importing data from a database cursor, Getting data out, Displaying your table in ASCII form, Printing, Stringing

</details>

### pyphen

Pure Python module to hyphenate text

`pip install pyphen` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+); GNU Lesser General Public Licen · rank 537 · last release 2026-08-14 · [PyPI](https://pypi.org/project/pyphen/) · [docs](https://pyphen.org/) · [source](https://github.com/Kozea/Pyphen)

_README extract left out: share-alike licence._

### Unidecode

ASCII transliterations of Unicode text

`pip install Unidecode` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 672 · last release 2025-04-24 · [PyPI](https://pypi.org/project/Unidecode/)

_README extract left out: share-alike licence._

### pytimeparse

Time expression parser

`pip install pytimeparse` · installs (wheel) · licence: MIT License · rank 710 · last release 2026-10-17 · [PyPI](https://pypi.org/project/pytimeparse/)

<details><summary>README extract</summary>

Copyright (c) 2014 Will Roberts <wildwilhelm@gmail.com>

Licensed under the MIT License (see source file `timeparse.py` for
details).

A small Python library to parse various kinds of time expressions,
inspired by
this StackOverflow question. ...

Example:
```python
>>> from pytimeparse import parse
>>> parse('1.2 minutes')
72
```

Sections: pytimeparse: time expression parser, Future work

</details>

### junitparser

Manipulates JUnit/xUnit Result XML files

`pip install junitparser` · installs (wheel) · licence: Apache-2.0 · rank 1155 · last release 2026-09-01 · [PyPI](https://pypi.org/project/junitparser/) · [docs](https://junitparser.readthedocs.io/)

<details><summary>README extract</summary>

junitparser handles JUnit/xUnit Result XML files. Use it to parse and manipulate
existing Result XML files, or create new JUnit/xUnit result XMLs from scratch.

Features:
* Parse or modify existing JUnit/xUnit XML files.
* Parse or modify non-standard or customized JUnit/xUnit XML files, by monkey
 patching existing element definitions.
* Create JUnit/xUnit test results from scratch.
* Merge test result XML files. ...

Example:
```python
from junitparser import TestCase, TestSuite, JUnitXml, Skipped, Error

# Create cases
case1 = TestCase('case1', 'class.name', 0.5) # params are optional
case1.classname = "modified.class.name" # specify or change case attrs
case1.result = [Skipped()] # You can have a list of results
case2 = TestCase('case2')
...
```

...

</details>

### python-bidi

Python Bidi layout wrapping the Rust crate unicode-bidi

`pip install python-bidi` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 1276 · last release 2026-10-20 · [PyPI](https://pypi.org/project/python-bidi/) · [docs](https://python-bidi.readthedocs.io/en/latest/) · [source](https://github.com/MeirKriheli/python-bidi)

_README extract left out: share-alike licence._

### ebcdic

Additional EBCDIC codecs

`pip install ebcdic` · installs (wheel) · licence: BSD-2-Clause · rank 1282 · last release 2026-03-03 · [PyPI](https://pypi.org/project/ebcdic/) · [docs](https://github.com/roskakori/CodecMapper/blob/master/ebcdic/README.md) · [source](https://github.com/roskakori/CodecMapper.git)

<details><summary>README extract</summary>

`ebcdic` is a Python package adding additional EBCDIC codecs for data exchange with legacy systems.

EBCDIC is short for "Extended Binary Coded Decimal Interchange Code" and is a family of character encodings that is mainly used on mainframe computers. There is no real point in using it unless you have to exchange data with legacy systems. ...

Example:
```python
>>> import ebcdic
>>> 'hello world'.encode('cp1141')
b'\x88\x85\x93\x93\x96@\xa6\x96\x99\x93\x84O'
```

Sections: ebcdic, Example usage, Source code

</details>

### pyfiglet

Pure-python FIGlet implementation

`pip install pyfiglet` · installs (wheel) · licence: MIT License · rank 1524 · last release 2025-08-15 · [PyPI](https://pypi.org/project/pyfiglet/)

<details><summary>README extract</summary>

Example:
```python
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('text to render'))
```

Sections: pyfiglet, Synopsis, FAQ, Usage, Pyfiglet is also a library that can be used in python code, Thanks

</details>

### pyhcl

HCL configuration parser for python

`pip install pyhcl` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 1676 · last release 2023-09-01 · [PyPI](https://pypi.org/project/pyhcl/)

<details><summary>README extract</summary>

Implements a parser for HCL (HashiCorp Configuration
Language) in Python. This
implementation aims to be compatible with the original golang version of
the parser.

pyhcl does not support HCL2 (which is what modern terraform uses). You might try
 instead (though I've never personally tried it). ...

Example:
```python
import hcl

with open('file.hcl', 'r') as fp:
    obj = hcl.load(fp)
```

Sections: pyhcl, Usage, Convert HCL to JSON, Structure Validation, Syntax, Debug Mode

</details>

### jieba

Chinese Words Segmentation Utilities

`pip install jieba` · installs from source (sdist only) · licence: MIT License · rank 1694 · last release 2020-01-20 · [PyPI](https://pypi.org/project/jieba/)

<details><summary>README extract</summary>

“结巴”中文分词：做最好的 Python 中文分词组件

"Jieba" (Chinese for "to stutter") Chinese text segmentation: built to
be the best Python Chinese word segmentation module.

完整文档见 `README.md`

GitHub:

- 支持三种分词模式：

 - 精确模式，试图将句子最精确地切开，适合文本分析；
 - 全模式，把句子中所有的可以成词的词语都扫描出来,
 速度非常快，但是不能解决歧义；
 - 搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。

- 支持繁体分词
- 支持自定义词典
- MIT 授权协议 ...

Sections: jieba, 特点, 安装说明

</details>

### jaconv

Pure-Python Japanese character interconverter for Hiragana, Katakana, Hankaku, Zenkaku and more

`pip install jaconv` · installs (wheel) · licence: MIT License · rank 1867 · last release 2026-02-08 · [PyPI](https://pypi.org/project/jaconv/)

<details><summary>README extract</summary>

jaconv (Japanese Converter) is interconverter for Hiragana, Katakana, Hankaku (half-width character) and Zenkaku (full-width character)

Japanese README is available.

Example:
```python
import jaconv

# Hiragana to Katakana
jaconv.hira2kata('ともえまみ')
# => 'トモエマミ'

# Hiragana to half-width Katakana
jaconv.hira2hkata('ともえまみ')
# => 'ﾄﾓｴﾏﾐ'

# Katakana to Hiragana
jaconv.kata2hira('巴マミ')
# => '巴まみ'

# half-width character to full-width character
# default parameters are followings: kana=True, ascii=False, digit=False
...
```

Sections: jaconv, USAGE, NOTE, CHANGES, 0.5.0 (2026-02-08), 0.4.1 (2025-11-30), 0.4.0 (2024-07-26), 0.3.4 (2023-02-18), 0.3.3 (2022-12-31), 0.3.1 (2022-12-14), 0.3 (2021-03-29), 0.2.4 (2018-02-04), 0.2.3 (2018-02-03), 0.2.2 (2018-01-22)

</details>

### pypandoc

Thin wrapper for pandoc.

`pip install pypandoc` · installs (wheel) · licence: MIT · rank 1893 · last release 2026-03-14 · [PyPI](https://pypi.org/project/pypandoc/) · [source](https://github.com/JessicaTegner/pypandoc)

<details><summary>README extract</summary>

Pypandoc provides a thin wrapper for pandoc, a universal
document converter.

Example:
```python
import pypandoc

# With an input file: it will infer the input format from the filename
output = pypandoc.convert_file('somefile.md', 'rst')

# ...but you can overwrite the format via the `format` argument:
output = pypandoc.convert_file('somefile.txt', 'rst', format='md')

# alternatively you could just pass some string. In this case you need to
...
```

Sections: pypandoc, Specifying the location of pandoc binaries, Usage, Dealing with Formatting Arguments, Quick Start, Logging Messages, Getting Pandoc Version, Command-Line Usage, Related

</details>

### pdfkit

Wkhtmltopdf python wrapper to convert html to pdf using the webkit rendering engine and qt

`pip install pdfkit` · installs (wheel) · licence: MIT · rank 2087 · last release 2021-11-14 · [PyPI](https://pypi.org/project/pdfkit/)

<details><summary>README extract</summary>

Python 2 and 3 wrapper for wkhtmltopdf utility to convert HTML to PDF using Webkit.

This is adapted version of ruby PDFKit library, so big thanks to them!

Example:
```python
import pdfkit

pdfkit.from_url(' 'out.pdf')
pdfkit.from_file('test.html', 'out.pdf')
pdfkit.from_string('Hello!', 'out.pdf')
```

Sections: Python-PDFKit: HTML to PDF wrapper, Usage, Configuration, Troubleshooting, Debugging issues with PDF generation, Common errors

</details>

### pypandoc-binary

Thin wrapper for pandoc.

`pip install pypandoc-binary` · installs (wheel) · licence: MIT · rank 2189 · last release 2026-03-14 · [PyPI](https://pypi.org/project/pypandoc-binary/) · [source](https://github.com/JessicaTegner/pypandoc)

<details><summary>README extract</summary>

Pypandoc provides a thin wrapper for pandoc, a universal
document converter.

Example:
```python
import pypandoc

# With an input file: it will infer the input format from the filename
output = pypandoc.convert_file('somefile.md', 'rst')

# ...but you can overwrite the format via the `format` argument:
output = pypandoc.convert_file('somefile.txt', 'rst', format='md')

# alternatively you could just pass some string. In this case you need to
...
```

Sections: pypandoc, Specifying the location of pandoc binaries, Usage, Dealing with Formatting Arguments, Quick Start, Logging Messages, Getting Pandoc Version, Command-Line Usage, Related

</details>

### python-iso639

ISO 639 language codes, names, and other associated information

`pip install python-iso639` · installs (wheel) · licence: Apache-2.0 · rank 2358 · last release 2026-11-07 · [PyPI](https://pypi.org/project/python-iso639/) · [source](https://github.com/jacksonllee/iso639)

<details><summary>README extract</summary>

`python-iso639` is a Python package for ISO 639 language codes, names, and
other associated information.

Current features:

* 🌐 A representation of languages mapped across ISO 639-1, 639-2, and 639-3.
* 🔎 Functionality to "guess" what a language is for a given
 unknown language code or name. ...

Features:
Both packages iso639
and iso-639 exist on PyPI.
However, as of this writing (May 2022), they were last updated in 2016 and don't seem to be maintained anymore
for updating the language codes. ...

Example:
```python
>>> import iso639
>>> lang1 = iso639.Language.from_part3('fra')
>>> type(lang1)
<class 'iso639.language.Language'>
>>> lang1
...
```

...

</details>

### pypinyin

汉字拼音转换模块/工具.

`pip install pypinyin` · installs (wheel) · licence: MIT License · rank 2788 · last release 2025-07-20 · [PyPI](https://pypi.org/project/pypinyin/) · [docs](https://pypinyin.readthedocs.io/) · [source](https://github.com/mozillazg/python-pinyin)

<details><summary>README extract</summary>

将汉字转为拼音。可以用于汉字注音、排序、检索(Russian translation) 。

最初版本的代码参考了 hotoo/pinyin 的实现。

* License: MIT license

* Python version: 2.7, pypy, pypy3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

* 根据词组智能匹配最正确的拼音。
* 支持多音字。
* 简单的繁体支持，注音支持，威妥玛拼音支持。
* 支持多种不同拼音/注音风格。

Example:
```python
>>> from pypinyin import pinyin, lazy_pinyin, Style
>>> pinyin('中心')  # or pinyin(['中心'])，参数值为列表时表示输入的是已分词后的数据
[['zhōng'], ['xīn']]
>>> pinyin('中心', heteronym=True)  # 启用多音字模式
[['zhōng', 'zhòng'], ['xīn']]
>>> pinyin('中心', style=Style.FIRST_LETTER)  # 设置拼音风格
[['z'], ['x']]
>>> pinyin('中心', style=Style.TONE2, heteronym=True)
...
```

Sections: 汉字拼音转换工具（Python 版）, 特性, 安装, 使用示例, 文档, FAQ, 拼音有误？, 为什么没有 y, w, yu 几个声母？, 存在既没有声母也没有韵母的拼音？, 如何将某一风格的拼音转换为其他风格的拼音？, 如何减少内存占用？, 拼音数据, Related Projects

</details>

### casefy

Utilities for string case conversion.

`pip install casefy` · installs (wheel) · licence: MIT License · rank 2936 · last release 2025-03-07 · [PyPI](https://pypi.org/project/casefy/) · [docs](https://dmlls.github.io/python-casefy/)

<details><summary>README extract</summary>

Casefy (/keɪsfaɪ/) is a lightweight Python package to convert the casing of
strings. It has no third-party dependencies and supports Unicode.

Example:
```python
import casefy

# Alphanum3ric case (removes non-alphanumeric chars)
string = casefy.alphanumcase("foo - 123 ; bar!")
print(string)  # foo123bar

# camelCase
string = casefy.camelcase("foo_bar")
print(string)  # fooBar

string = casefy.camelcase("FooBar")
print(string)  # fooBar

string = casefy.camelcase("FOO BAR")
print(string)  # fooBar

...
```

Sections: Introduction, Examples, Related projects

</details>

### vobject

A full-featured Python package for parsing and creating iCalendar and vCard files

`pip install vobject` · installs (wheel) · licence: Apache Software License · rank 3136 · last release 2024-12-16 · [PyPI](https://pypi.org/project/vobject/) · [source](https://github.com/py-vobject/vobject)

<details><summary>README extract</summary>

Description

Parses iCalendar and vCard files into Python data structures, decoding the
relevant encodings. Also serializes vobject data structures to iCalendar, vCard,
or (experimentally) hCalendar unicode strings.

Requirements

Requires python 2.7 or later, dateutil 2.4.0 or later and six.

Recent changes ...

</details>

### jaro-winkler

Original, standard and customisable versions of the Jaro-Winkler functions.

`pip install jaro-winkler` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 3359 · last release 2022-08-05 · [PyPI](https://pypi.org/project/jaro-winkler/)

_README extract left out: share-alike licence._

### confusable-homoglyphs

Detect confusable usage of unicode homoglyphs, prevent homograph attacks.

`pip install confusable-homoglyphs` · installs (wheel) · licence: MIT License · rank 3493 · last release 2024-01-30 · [PyPI](https://pypi.org/project/confusable-homoglyphs/)

<details><summary>README extract</summary>

This project has been adopted from the original confusable_homoglyphs
by Victor Felder.

*a homoglyph is one of two or more graphemes, characters, or glyphs with
shapes that appear identical or very similar*
wikipedia:Homoglyph

Unicode homoglyphs can be a nuisance on the web. ...

Sections: confusable_homoglyphs [doc], API documentation, Is the data up to date?, 1.0.0, 2.0.0, 2.0.1, 3.0.0, 3.1.0, 3.1.1, 3.2.0, 3.3.0, 3.3.1

</details>

### inscriptis

inscriptis - HTML to text converter.

`pip install inscriptis` · installs (wheel) · licence: Apache-2.0 · rank 3600 · last release 2026-10-23 · [PyPI](https://pypi.org/project/inscriptis/) · [docs](https://inscriptis.readthedocs.io/en/latest/) · [source](https://github.com/weblyzard/inscriptis)

<details><summary>README extract</summary>

A python based HTML to text conversion library, command line client and Web
service with support for nested tables, a subset of CSS and optional
support for providing an annotated output. ...

Example:
```python
import urllib.request
from inscriptis import get_text

url = "
html = urllib.request.urlopen(url).read().decode('utf-8')

text = get_text(html)
print(text)
```

Sections: Statement of need - why inscriptis?, Python library, Standalone command line client, Command line parameters, HTML to text conversion, HTML to annotated text conversion, Annotation postprocessors, Web Service, Run the Web Service on your host system, Run the Web Service with Docker, Run as Kubernetes Deployment, Use the Web Service, Example annotation profiles, Wikipedia tables and table metadata

</details>

### textstat

Calculate statistical features from text

`pip install textstat` · installs (wheel) · licence: MIT · rank 4042 · last release 2026-02-18 · [PyPI](https://pypi.org/project/textstat/)

<details><summary>README extract</summary>

Textstat is an easy to use library to calculate statistics from text. It helps determine readability, complexity, and grade level.

 Photo by Patrick Tomasso
 on Unsplash

Example:
```python
>>> import textstat

>>> test_data = (
    "Playing games has always been thought to be important to "
    "the development of well-balanced and creative children; "
    "however, what part, if any, they should play in the lives "
    "of adults has never been researched that deeply. I believe "
...
```

...

</details>

### pdf-inspector

Fast PDF inspection, classification, and text extraction with smart scanned vs text-based detection

`pip install pdf-inspector` · installs (wheel) · licence: MIT License · rank 4304 · last release 2026-09-28 · [PyPI](https://pypi.org/project/pdf-inspector/) · [docs](https://github.com/firecrawl/pdf-inspector/blob/main/docs/python.md) · [source](https://github.com/firecrawl/pdf-inspector)

<details><summary>README extract</summary>

Fast PDF classification, text extraction, and selective OCR. Detects whether a PDF is text-based or scanned, extracts text with position awareness, and converts clean native and OCR results to Markdown. Python bindings via PyO3 for the pdf-inspector Rust library. ...

Features:
- Smart classification — `text_based` / `scanned` / `image_based` / `mixed` in ~10–50ms, with a confidence score and per-page OCR routing. ...

Example:
```python
import pdf_inspector

# Full processing: detect + extract + convert to Markdown
result = pdf_inspector.process_pdf("document.pdf")
print(result.pdf_type)      # "text_based", "scanned", "image_based", "mixed"
print(result.confidence)     # 0.0 - 1.0
print(result.page_count)     # number of pages
...
```

...

</details>

### match

Match tokenized words and phrases within the original, untokenized, often messy, text.

`pip install match` · installs from source (sdist only) · licence: Apache Software License · rank 4689 · last release 2022-10-03 · [PyPI](https://pypi.org/project/match/)

<details><summary>README extract</summary>

\ \

The purpose of the module `Match` is to get the offsets (as well as
the string between those offsets, for debugging) of a cleaned-up,
tokenized string from its original, untokenized source. ...

Example:
```python
In [2]: import match

In [3]: match.match(original_text, ['-LRB-', 'and', 'do', 'weird', 'stuff', 'with', 'punctuation', '-RRB-'])
Out[3]: [(60, 97, '(and do weird stuff with punctuation)')]

In [4]: match.match(original_text, ['I', 'am', 'writing', 'a', 'letter', '!'])
Out[4]: [(0, 25, 'I   am writing a letter !')]

...
```

Sections: match, Requirements, Documentation

</details>

### case-converter

A string case conversion package.

`pip install case-converter` · installs (wheel) · licence: MIT License · rank 4813 · last release 2025-02-19 · [PyPI](https://pypi.org/project/case-converter/)

<details><summary>README extract</summary>

A robust python package for transforming string cases such as `Hello, world!` into
 `helloWorld` (camelcase).

Example:
```python
from caseconverter import camelcase

camelcase("Hello, world!") # output: helloWorld
```

Sections: Case Converter, General usage, Available conversions, `camelcase`, `cobolcase`, `flatcase`, `kebabcase`, `macrocase`, Additional options, `pascalcase`, `snakecase`, `titlecase`, Options for all conversions, Stripping punctuation

</details>

### chonkie-core

The fastest semantic text chunking library

`pip install chonkie-core` · installs (wheel) · licence: Apache Software License; MIT License · rank 4975 · last release 2026-05-28 · [PyPI](https://pypi.org/project/chonkie-core/) · [source](https://github.com/chonkie-inc/chunk)

<details><summary>README extract</summary>

the fastest text chunking library — up to 1 TB/s throughput

you know how every chunking library claims to be fast? yeah, we actually meant it.

chonkie-core splits text at semantic boundaries (periods, newlines, the usual suspects) and does it stupid fast. we're talking "chunk the entire english wikipedia in 120ms" fast. ...

Example:
```python
from chonkie_core import Chunker

text = "Hello world. How are you? I'm fine.\nThanks for asking."

# with defaults (4KB chunks, split at \n . ?)
for chunk in Chunker(text):
    print(bytes(chunk))

# with custom size
for chunk in Chunker(text, size=1024):
    print(bytes(chunk))

# with custom delimiters
...
```

Sections: chonkie-core, 🚀 usage

</details>

### uroman

uroman is a universal romanizer. It converts text in any script to the standard Latin alphabet.

`pip install uroman` · installs (wheel) · licence: Apache Software License · rank 5166 · last release 2024-06-28 · [PyPI](https://pypi.org/project/uroman/) · [source](https://github.com/isi-nlp/uroman)

<details><summary>README extract</summary>

*uroman* is a *universal romanizer*. It converts text in any script to the standard Latin alphabet.

 Example (Greek): Νεπάλ → Nepal

 Example (Hindi): नेपाल → nepaal

 Example (Urdu): نیپال → nypal

 Example (Chinese): 三万一 → 31000 ...

Sections: uroman, (New) Python version, Command Line Interface (CLI), Examples, uroman.py* Argument Structure Highlights, Using _uroman_ inside Python, Methods, Old Perl Version, Usage, Bibliography, Other features, Limitations

</details>

### PTable

A simple Python library for easily displaying tabular data in a visually appealing ASCII table format

`pip install PTable` · installs from source (sdist only) · licence: BSD License · rank 5598 · last release 2015-05-28 · [PyPI](https://pypi.org/project/PTable/)

<details><summary>README extract</summary>

Example:
```python
from prettytable import PrettyTable
x = PrettyTable()
```

Sections: PTable Tutorial, Links, Getting your data into (and out of) the table, Row by row, Column by column, Mixing and matching, Importing data from a CSV file, Importing data from a database cursor, Getting data out, Displaying your table in ASCII form, Printing, Stringing, Controlling which data gets displayed, Changing the alignment of columns

</details>

### mdit-plain

A plain text renderer for markdown-it-py

`pip install mdit-plain` · installs (wheel) · licence: MIT License · rank 5629 · last release 2023-01-02 · [PyPI](https://pypi.org/project/mdit-plain/)

<details><summary>README extract</summary>

A renderer for markdown-it-py that converts markdown documents into plain text by removing all markup.

</details>

### ir-datasets

provides a common interface to many IR ad-hoc ranking benchmarks, training datasets, etc.

`pip install ir-datasets` · installs (wheel) · licence: MIT License · rank 5900 · last release 2026-07-18 · [PyPI](https://pypi.org/project/ir-datasets/) · [docs](https://project.readthedocs.io/) · [source](https://github.com/ir-datasets/ir-datasets)

<details><summary>README extract</summary>

`ir_datasets` is a python package that provides a common interface to many IR ad-hoc ranking
benchmarks, training datasets, etc.

The package takes care of downloading datasets (including documents, queries, relevance judgments,
etc.) when available from public sources. ...

Features:
Python and Command Line Interfaces. Access datasts both through a simple Python API and
via the command line.

Automatically downloads source files (when available). Will download and verify the source
files for queries, documents, qrels, etc. ...

Example:
```python
import ir_datasets
dataset = ir_datasets.load('msmarco-passage/train')
# Documents
for doc in dataset.docs_iter():
    print(doc)
# GenericDoc(doc_id='0', text='The presence of communication amid scientific minds was equa...
...

</details>

### imgkit

Wkhtmltopdf python wrapper to convert html to image using the webkit rendering engine and qt

`pip install imgkit` · installs (wheel) · licence: MIT License · rank 5905 · last release 2023-02-23 · [PyPI](https://pypi.org/project/imgkit/)

<details><summary>README extract</summary>

Python 2 and 3 wrapper for wkhtmltoimage utility to convert HTML to IMG using Webkit.

Example:
```python
import imgkit

imgkit.from_url(' 'out.jpg')
imgkit.from_file('test.html', 'out.jpg')
imgkit.from_string('Hello!', 'out.jpg')
```

Sections: IMGKit: Python library of HTML to IMG wrapper, Usage, Configuration, Troubleshooting, Credit

</details>

### playa-pdf

Parallel and LazY Analyzer for PDFs

`pip install playa-pdf` · installs (wheel) · licence: MIT · rank 6246 · last release 2026-03-09 · [PyPI](https://pypi.org/project/playa-pdf/)

<details><summary>README extract</summary>

You can read this document, or just go look at some
notebooks to
get an idea of what this package does.

There are already too many PDF libraries, unfortunately none of which
does everything that everybody wants it to do, and we probably don't
need another one. ...

Example:
```python
pdf = playa.open("my_awesome_document.pdf")
raw_byte_stream = pdf.buffer
a_bunch_of_tokens = list(pdf.tokens)
a_bunch_of_indirect_object_ids = list(pdf.keys())
a_bunch_of_indirect_objects = list(pdf.values())
a_bunch_of_pages = list(pdf.pages)
```

...

</details>

### mecab

a Python binding for unofficial fork of MeCab

`pip install mecab` · installs (wheel) · licence: BSD License; GNU General Public License v2 (GPLv2); GNU Lesser General Public Li · rank 6310 · last release 2026-10-25 · [PyPI](https://pypi.org/project/mecab/)

_README extract left out: share-alike licence._

### sphinx_mdinclude

Markdown extension for Sphinx

`pip install sphinx_mdinclude` · installs (wheel) · licence: MIT License · rank 7039 · last release 2024-08-03 · [PyPI](https://pypi.org/project/sphinx_mdinclude/) · [source](https://github.com/omnilib/sphinx-mdinclude)

<details><summary>README extract</summary>

Sphinx extension for including or writing pages in Markdown format.

sphinx-mdinclude is a simple Sphinx extension that enables including Markdown documents
from within reStructuredText. It provides the `.. mdinclude::` directive, and
automatically converts the content of Markdown documents to reStructuredText format. ...

Features:
* Basic markdown and some extensions (see below)
 * inline/block-level raw html
 * fenced-code block
 * tables
 * footnotes (``[^1]``)
* Inline- and Block-level rst markups
 * single- and multi-line directives (`.. ...

Sections: sphinx-mdinclude, Features, Restrictions, Usage

</details>

### lunr

A Python implementation of Lunr.js

`pip install lunr` · installs (wheel) · licence: MIT · rank 7154 · last release 2026-11-01 · [PyPI](https://pypi.org/project/lunr/) · [docs](https://lunr.readthedocs.io/en/latest/) · [source](https://github.com/yeraydiazdiaz/lunr.py)

<details><summary>README extract</summary>

A Python implementation of Lunr.js by Oliver Nightingale.

> A bit like Solr, but much smaller and not as bright.

This Python version of Lunr.js aims to bring the simple and powerful full text search
capabilities into Python guaranteeing results as close as the original
implementation as possible.

- Documentation ...

Example:
```python
>>> from lunr import lunr
>>>
>>> documents = [{
...     'id': 'a',
...     'title': 'Mr. Green kills Colonel Mustard',
...     'body': 'Mr. Green killed Colonel Mustard in the study with the candlestick.',
... }, {
...     'id': 'b',
...     'title': 'Plumb waters plant',
...     'body': 'Professor Plumb has a green plant in his study',
... }]
...
```

Sections: Lunr.py, What does this even do?, Interoperability with Lunr.js, Usage

</details>

### demoji

Accurately remove and replace emojis in text strings

`pip install demoji` · installs (wheel) · licence: Apache-2.0 · rank 7301 · last release 2026-04-19 · [PyPI](https://pypi.org/project/demoji/) · [docs](https://github.com/bsolomon1124/demoji/blob/master/README.md) · [source](https://github.com/bsolomon1124/demoji)

<details><summary>README extract</summary>

Accurately find or remove emojis from a blob of text using
data from the Unicode Consortium's emoji code repository.

Example:
```python
>>> tweet = """\
... #startspreadingthenews yankees win great start by 🎅🏾 going 5strong innings with 5k’s🔥 🐂
... solo homerun 🌋🌋 with 2 solo homeruns and👹 3run homerun… 🤡 🚣🏼 👨🏽‍⚖️ with rbi’s … 🔥🔥
... 🇲🇽 and 🇳🇮 to close the game🔥🔥!!!….
... WHAT A GAME!!..
... """
>>> demoji.findall(tweet)
{
    "🔥": "fire",
    "🌋": "volcano",
...
```

Sections: demoji, Basic Usage, Command-line Use, Reference, Footnote: Emoji Sequences

</details>

### uniseg

Determine Unicode text segmentations

`pip install uniseg` · installs (wheel) · licence: MIT License · rank 7323 · last release 2026-01-09 · [PyPI](https://pypi.org/project/uniseg/) · [docs](https://uniseg-py.readthedocs.io/) · [source](https://bitbucket.org/emptypage/uniseg-py.git)

<details><summary>README extract</summary>

A Python package to determine Unicode text segmentations.

- uniseg · PyPI
- emptypage / uniseg-py — Bitbucket
- uniseg documentation — Read the Docs

We released the version 0.9.0 on November, 2024, and this is the first
release ever which passes all the Unicode breaking tests (congrats!). ...

Features:
This package provides:

- Functions to get Unicode Character Database (UCD) properties concerned with
 text segmentations.
- Functions to determine segmentation boundaries of Unicode strings. ...

Sections: uniseg, News, Features, Requirements, Changes, References, Related / Similar Projects

</details>

### pdfminer

PDF parser and analyzer

`pip install pdfminer` · installs from source (sdist only) · licence: MIT License · rank 7773 · last release 2019-11-25 · [PyPI](https://pypi.org/project/pdfminer/)

<details><summary>README extract</summary>

PDFMiner is a text extraction tool for PDF documents.

Warning: Starting from version 20191010, PDFMiner supports Python 3 only.
For Python 2 support, check out
pdfminer.six.

Features:
* Pure Python (3.6 or above).
 * Supports PDF-1.7. (well, almost)
 * Obtains the exact location of text as well as other layout information (fonts, etc.).
 * Performs automatic layout analysis.
 * Can convert PDF into other formats (HTML/XML). ...

Sections: PDFMiner, Features, How to Use, Command Line Syntax, pdf2txt.py, dumppdf.py, TODO, Related Projects

</details>

### pyuca

a Python implementation of the Unicode Collation Algorithm

`pip install pyuca` · installs (wheel) · licence: MIT License · rank 7996 · last release 2017-09-25 · [PyPI](https://pypi.org/project/pyuca/)

### overpunch

Overpunch Parser/Formatter

`pip install overpunch` · installs from source (sdist only) · licence: MIT License · rank 8051 · last release 2017-04-24 · [PyPI](https://pypi.org/project/overpunch/)

<details><summary>README extract</summary>

Extract and generate overpunch ( formatted numbers.

Sections: Overpunch Parser/Formatter, Examples, Requirements, Tests

</details>

### english

English language utility library for Python

`pip install english` · installs (wheel) · licence: Apache Software License · rank 8378 · last release 2020-07-17 · [PyPI](https://pypi.org/project/english/) · [source](https://github.com/technige/english)

<details><summary>README extract</summary>

English

*English* is an English language utility library for Python.

</details>

### treetable

Helper to pretty print an ascii table with a tree-like structure

`pip install treetable` · installs (wheel) · licence: Unlicense license · rank 8569 · last release 2025-09-03 · [PyPI](https://pypi.org/project/treetable/)

<details><summary>README extract</summary>

Helper to pretty print an ascii table with a tree-like structure.

Example:
```python
from treetable import table, group, leaf

mytable = table([
    group('info', [
        leaf('name'),
        leaf('index')]),
    group('metrics', align='>', groups=[
        leaf('speed', '.0f'),
        leaf('accuracy', '.1%'),
        leaf('special', '.1%', align='=')]),
])
```

Sections: treetable, Quick example, Usage and examples, Colors

</details>

### cpca

Chinese Province, City and Area Recognition Utilities

`pip install cpca` · installs (wheel) · licence: MIT License · rank 9848 · last release 2021-02-20 · [PyPI](https://pypi.org/project/cpca/)

<details><summary>README extract</summary>

chinese_province_city_area_mapper：一个用于识别简体中文字符串中省，市和区并能够进行映射，检验和简单绘图的python模块

举个例子:
chinese_province_city_area_mapper: built to be recognize Chinese province,city and area in simplified Chinese string, it can automaticall map area to city
and map city to province.

for example:
完整文档见该模块的Github，
GitHub:

Example:
```python
location_str = ["徐汇区虹漕路461号58号楼5楼", "泉州市洛江区万安塘西工业区", "北京朝阳区北苑华贸城"]
import cpca
df = cpca.transform(location_str)
df
```

Sections: chinese_province_city_area_mapper, 安装说明, Get Started

</details>

### sas7bdat

A sas7bdat file reader for Python

`pip install sas7bdat` · installs (wheel) · licence: MIT License · rank 10681 · last release 2026-08-24 · [PyPI](https://pypi.org/project/sas7bdat/)

<details><summary>README extract</summary>

This module will read sas7bdat files using pure Python (2.6+, 3+). No SAS software
required! The module started out as a port of the R script of the same name
found here: < but has since been
completely rewritten.

Also included with this library is a simple command line script,
`sas7bdat_to_csv`, which converts sas7bdat files to csv files. ...

Example:
```python
# !python
from sas7bdat import SAS7BDAT
with SAS7BDAT('foo.sas7bdat', skip_header=True) as reader:
    for row in reader:
        print row
```

Sections: sas7bdat.py, Usage

</details>

### xlsx2html

A simple export from xlsx format to html tables with keep cell formatting

`pip install xlsx2html` · installs (wheel) · licence: MIT License · rank 10694 · last release 2026-02-23 · [PyPI](https://pypi.org/project/xlsx2html/)

<details><summary>README extract</summary>

A simple export from xlsx format to html tables with keep cell formatting

Example:
```python
from xlsx2html import xlsx2html

out_stream = xlsx2html('path/to/example.xlsx')
out_stream.seek(0)
print(out_stream.read())
```

Sections: xlsx2html, Usage

</details>

### Tempita

A very small text templating language

`pip install Tempita` · installs (wheel) · licence: MIT License · rank 10791 · last release 2024-11-12 · [PyPI](https://pypi.org/project/Tempita/)

<details><summary>README extract</summary>

Tempita is a small templating language for text substitution.

This isn't meant to be the Next Big Thing in templating; it's just a
handy little templating language for when your project outgrows
``string.Template`` or ``%`` substitution. It's small, it embeds
Python in strings, and it doesn't do much else. ...

</details>

### pyjarowinkler

Finds the Jaro Winkler Distance indicating a distance or similarity score between two strings.

`pip install pyjarowinkler` · installs (wheel) · licence: Apache Software License · rank 10829 · last release 2025-12-06 · [PyPI](https://pypi.org/project/pyjarowinkler/) · [docs](https://github.com/nap/jaro-winkler-distance#readme) · [source](https://github.com/nap/jaro-winkler-distance.git)

<details><summary>README extract</summary>

Finds a non-euclidean distance or similarity between two strings.

Jaro and Jaro-Winkler equations provide a score between two short strings where errors are more prone at the end of the string. Jaro's equation measure is the weighted sum of the percentage of matching and transposed characters from each string. ...

Example:
```python
from pyjarowinkler import distance

distance.get_jaro_similarity("PENNSYLVANIA", "PENNCISYLVNIA", decimals=12)
# 0.830031080031
distance.get_jaro_winkler_similarity("PENNSYLVANIA", "PENNCISYLVNIA", decimals=12)
# 0.898018648019
distance.get_jaro_distance("hello", "haloa", decimals=4)
# 0.2667
...
```

Sections: Jaro Winkler Distance, Implementation, Example, Benchmark, Usage

</details>

### docx-mailmerge

Performs a Mail Merge on docx (Microsoft Office Word) files

`pip install docx-mailmerge` · installs (wheel) · licence: MIT License · rank 11108 · last release 2019-10-09 · [PyPI](https://pypi.org/project/docx-mailmerge/)

<details><summary>README extract</summary>

Performs a Mail Merge on Office Open XML (docx) files. Can be used on any
system without having to install Microsoft Office Word. Supports Python 2.7,
3.3 and up.

Example:
```python
from mailmerge import MailMerge
with MailMerge('input.docx') as document:
    ...
```

Sections: docx Mail Merge, Usage, Todo / Wish List, Unit tests

</details>

### twitter-text-parser

A library to parse or validate Twitter texts properly

`pip install twitter-text-parser` · installs (wheel) · licence: MIT License · rank 11211 · last release 2023-05-24 · [PyPI](https://pypi.org/project/twitter-text-parser/) · [source](https://github.com/swen128/twitter-text-python)

<details><summary>README extract</summary>

This is a Python port of the twitter/twitter-text libraries, fully compliant with the official conformance test suite.

Features:
This library calculates length of a tweet message according to the documentation from Twitter Developers,
so that you can validate the tweet without calling the Web API at all. ...

Example:
```python
from twitter_text import parse_tweet, extract_emojis_with_indices, extract_urls_with_indices

text = 'english text 日本語 😷

assert parse_tweet(text).asdict() == {
    'weightedLength': 46,
    'valid': True,
    'permillage': 164,
    'validRangeStart': 0,
    'validRangeEnd': 38,
    'displayRangeStart': 0,
    'displayRangeEnd': 38
}

...
```

Sections: twitter-text-python, Features, Usage, Examples, Related Links

</details>

### wikitextparser

A simple parsing tool for MediaWiki's wikitext markup.

`pip install wikitextparser` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 12046 · last release 2026-10-08 · [PyPI](https://pypi.org/project/wikitextparser/)

_README extract left out: share-alike licence._

### dynamicprompts

Dynamic prompts templating library for Stable Diffusion

`pip install dynamicprompts` · installs (wheel) · licence: MIT · rank 12735 · last release 2026-11-08 · [PyPI](https://pypi.org/project/dynamicprompts/)

<details><summary>README extract</summary>

Dynamic prompts is a Python library that provides developers with a flexible and intuitive templating language and tools for generating prompts for text-to-image generators like Stable Diffusion, MidJourney or Dall-e 2. ...

Example:
```python
from dynamicprompts.generators import RandomPromptGenerator

generator = RandomPromptGenerator()
generator.generate("I love {red|green|blue} roses", num_images=5)

>> ['I love blue roses', 'I love red roses', 'I love green roses', 'I love red roses', 'I love red roses']
```

Sections: Dynamic Prompts, Quick overview of the templating language, Variants, Choosing multiple variants, Wildcards, Let's try a real-world prompt, Use whitespace for readability, Quick Start, Random seeds, Combinatorial Generation, Usage, Magic Prompt, Other models

</details>

### acora

Fast multi-keyword search engine for text strings

`pip install acora` · installs from source (sdist only) · licence: BSD License · rank 13161 · last release 2024-09-14 · [PyPI](https://pypi.org/project/acora/)

<details><summary>README extract</summary>

Acora is 'fgrep' for Python, a fast multi-keyword text search engine.

Based on a set of keywords and the
Aho-Corasick algorithm,
it generates a search automaton and runs it over string input, either unicode
or bytes.

Acora comes with both a pure Python implementation and a fast binary
module written in Cython. ...

Features:
* works with unicode strings and byte strings
* about 2-3x as fast as Python's regular expression engine for most input
* finds overlapping matches, i.e. ...

Example:
```python
>>> from acora import AcoraBuilder
```

Sections: Acora, What is Acora?, Features, How do I use it?, FAQs and recipes, ) How do I parse line-by-line with arbitrary line endings?

</details>

### python-mecab-ko

A python binding for mecab-ko

`pip install python-mecab-ko` · installs from source (sdist only) · licence: BSD License · rank 13298 · last release 2024-07-14 · [PyPI](https://pypi.org/project/python-mecab-ko/)

<details><summary>README extract</summary>

A python binding for mecab-ko

See documentation for more details.

Example:
```python
>>> from mecab import MeCab
>>> mecab = MeCab()
```

Sections: python-mecab-ko, Help, Usage

</details>

### python-mecab-ko-dic

mecab-ko-dic packaged for Python

`pip install python-mecab-ko-dic` · installs (wheel) · licence: Apache Software License · rank 13305 · last release 2022-12-14 · [PyPI](https://pypi.org/project/python-mecab-ko-dic/)

<details><summary>README extract</summary>

This is a version of`mecab-ko-dic` packaged for easy use in Python. In order to use `mecab-ko-dic`, a complicated process of installing `mecab-ko` and building the dictionary is required. This library performs these processes in advance and makes the built dictionary available just through installation.

Example:
```python
import mecab_ko_dic
print("Dictionary path:", mecab_ko_dic.dictionary_path)
```

Sections: python-mecab-ko-dic, Usage

</details>

### editorconfig-checker

Python wrapper around invoking editorconfig-checker (https://github.com/editorconfig-checker/editorconfig-checker)

`pip install editorconfig-checker` · installs from source (sdist only) · licence: MIT · rank 13360 · last release 2026-08-10 · [PyPI](https://pypi.org/project/editorconfig-checker/)

<details><summary>README extract</summary>

A Python wrapper to provide a pip-installable editorconfig-checker binary.

Internally, this package provides a convenient way to download the pre-built `editorconfig-checker` binary for your particular platform.

Sections: editorconfig-checker.python, Usage, Usage with the pre-commit git hooks framework

</details>

### Fuzzy

Fast Python phonetic algorithms

`pip install Fuzzy` · installs from source (sdist only) · licence: Artistic License; MIT License · rank 13503 · last release 2017-10-16 · [PyPI](https://pypi.org/project/Fuzzy/)

<details><summary>README extract</summary>

Fuzzy is a python library implementing common phonetic algorithms quickly.
Typically this is in string similarity exercises, but they're pretty versatile.

It uses C Extensions (via Cython) for speed.

The algorithms are:

* Soundex
* NYSIIS
* Double Metaphone Based on Maurice
 Aubrey's C code from his perl implementation.

Example:
```python
In [3]: timeit soundex('fuzzy')
1000000 loops, best of 3: 326 ns per loop

In [4]: timeit dmeta('fuzzy')
100000 loops, best of 3: 2.18 us per loop

In [5]: timeit fuzzy.nysiis('fuzzy')
100000 loops, best of 3: 13.7 us per loop
```

Sections: Usage, Performance, Distance Metrics

</details>

### neologdn

Japanese text normalizer for mecab-neologd

`pip install neologdn` · installs (wheel) · licence: Apache-2.0 · rank 14296 · last release 2025-12-02 · [PyPI](https://pypi.org/project/neologdn/) · [source](https://github.com/ikegami-yukino/neologdn.git)

<details><summary>README extract</summary>

neologdn is a Japanese text normalizer for mecab-neologd.

The normalization is based on the neologd's rules:

And also some optional features are added.

Contributions are welcome!

NOTE: Installing this module requires C++11 compiler.

Example:
```python
import neologdn
neologdn.normalize("ﾊﾝｶｸｶﾅ")
# => 'ハンカクカナ'
neologdn.normalize("全角記号！？＠＃")
# => '全角記号!?@#'
neologdn.normalize("全角記号例外「・」")
# => '全角記号例外「・」'
neologdn.normalize("長音短縮ウェーーーーイ")
# => '長音短縮ウェーイ'
neologdn.normalize("チルダ削除ウェ~∼∾〜〰～イ")
# => 'チルダ削除ウェイ'
neologdn.normalize("いろんなハイフン˗֊‐‑‒–⁃⁻₋−")
# => 'いろんなハイフン-'
...
```

...

</details>

## Also in this topic

- [pyparsing](software-development-compilers.md#pyparsing) - pyparsing - Classes and methods to define and execute parsing grammars
- [regex](scientific-engineering-information-analysis.md#regex) - Alternative regular expression module, to replace re.
- [docutils](documentation.md#docutils) - Docutils -- Python Documentation Utilities
- [nltk](scientific-engineering.md#nltk) - Natural Language Toolkit
- [langchain-text-splitters](scientific-engineering-artificial-intelligence.md#langchain-text-splitters) - LangChain text splitting utilities
- [parsedatetime](software-development-libraries.md#parsedatetime) - Parse human-readable date/time text.
- [texttable](software-development-libraries.md#texttable) - module to create simple ASCII tables
- [Sphinx](documentation.md#sphinx) - Python documentation generator
- [sphinxcontrib-serializinghtml](documentation.md#sphinxcontrib-serializinghtml) - sphinxcontrib-serializinghtml is a sphinx extension which outputs "serialized" HTML files (json and pickle)
- [sphinxcontrib-jsmath](documentation.md#sphinxcontrib-jsmath) - sphinxcontrib-jsmath is a sphinx extension which renders displayed maths in HTML via JavaScript
- [sphinxcontrib-htmlhelp](documentation.md#sphinxcontrib-htmlhelp) - sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files
- [sphinxcontrib-applehelp](documentation.md#sphinxcontrib-applehelp) - sphinxcontrib-applehelp is a Sphinx extension which outputs Apple help books
- [sphinxcontrib-qthelp](documentation.md#sphinxcontrib-qthelp) - sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp documents
- [sphinxcontrib-devhelp](documentation.md#sphinxcontrib-devhelp) - sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp documents
- [mkdocs](documentation.md#mkdocs) - Project documentation with Markdown.
- [natsort](scientific-engineering-information-analysis.md#natsort) - Simple yet flexible natural sorting in Python.
- [pathvalidate](software-development-libraries.md#pathvalidate) - pathvalidate is a Python library to sanitize/validate a string such as filenames/file-paths/etc.
- [compressed-rtf](system-archiving.md#compressed-rtf) - Compressed Rich Text Format (RTF) compression and decompression package
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [bashlex](software-development-libraries.md#bashlex) - Python parser for bash
- [selectolax](internet.md#selectolax) - A fast HTML5 parser with CSS selectors, written in Cython, using the Lexbor engine.
- [diff-match-patch](software-development-libraries.md#diff-match-patch) - Repackaging of Google's Diff Match and Patch libraries.
- [firecrawl-py](internet.md#firecrawl-py) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [pysbd](scientific-engineering.md#pysbd) - pysbd (Python Sentence Boundary Disambiguation) is a rule-based sentence boundary detection that works out-of-the-box across many languages.
- [parsy](software-development-compilers.md#parsy) - Easy-to-use parser combinators, for parsing in pure Python
- [xhtml2pdf](documentation.md#xhtml2pdf) - PDF generator using HTML and CSS
- [sacrebleu](scientific-engineering.md#sacrebleu) - Hassle-free computation of shareable, comparable, and reproducible BLEU, chrF, and TER scores
- [ast-grep-cli](security.md#ast-grep-cli) - Structural Search and Rewrite code at large scale using precise AST pattern.
- [pdfrw](multimedia-graphics.md#pdfrw) - PDF file reader/writer library
- [pyunormalize](software-development-internationalization.md#pyunormalize) - A library for Unicode normalization (NFC, NFD, NFKC, NFKD) independent of Python's core Unicode database.
- [pytimeparse2](software-development-libraries.md#pytimeparse2) - Time expression parser.
- [rjsmin](internet-www-http.md#rjsmin) - Javascript Minifier
- [mbstrdecoder](software-development-libraries.md#mbstrdecoder) - mbstrdecoder is a Python library for multi-byte character string decoder
- [rcssmin](internet-www-http.md#rcssmin) - CSS Minifier
- [html-for-docx](software-development-build-tools.md#html-for-docx) - Convert HTML to DOCX easily and quickly
- [pytablewriter](software-development-code-generators.md#pytablewriter) - pytablewriter is a Python library to write a table in various formats: AsciiDoc / CSV / Elasticsearch / HTML / JavaScript / JSON / LaTeX / LDJSON / LTSV / Markdown / MediaWiki / NumPy / Excel / Pandas / Python / reStructuredText / SQLite / TOML / TSV / YAML.
- [properdocs](documentation.md#properdocs) - Project documentation with Markdown.
- [tcolorpy](software-development-libraries.md#tcolorpy) - tcolopy is a Python library to apply true color for terminal text.
- [scrubadub](scientific-engineering-information-analysis.md#scrubadub) - Clean personally identifiable information from dirty dirty text.
- [ast-grep-py](security.md#ast-grep-py) - Structural Search and Rewrite code at large scale using precise AST pattern.
- [whatthepatch](software-development.md#whatthepatch) - A patch parsing and application library.
- [deep-translator](communications.md#deep-translator) - A flexible free and unlimited python tool to translate between different languages in a simple way using multiple translators
- [ansi2html](software-development-quality-assurance.md#ansi2html) - Convert text with ANSI color codes to HTML or to LaTeX
- [ct3](internet-www-http.md#ct3) - Cheetah is a template engine and code generation tool
- [srt](multimedia-video.md#srt) - A tiny library for parsing, modifying, and composing SRT files.
- [mkdocs-glightbox](documentation.md#mkdocs-glightbox) - MkDocs plugin supports image lightbox with GLightbox.
- [sphinx-tabs](documentation.md#sphinx-tabs) - Tabbed views for Sphinx
- [urlextract](software-development-libraries-2.md#urlextract) - Collects and extracts URLs from given text.
- [stanza](scientific-engineering.md#stanza) - A Python NLP Library for Many Human Languages, by the Stanford NLP Group
- [breathe](documentation.md#breathe) - Sphinx Doxygen renderer
- [sentencex](software-development.md#sentencex) - Sentence segmenter that supports ~300 languages
- [pythainlp](scientific-engineering-artificial-intelligence.md#pythainlp) - Thai Natural Language Processing library
- [liteparse](scientific-engineering-information-analysis.md#liteparse) - Python bindings for LiteParse - fast, lightweight PDF and document parsing
- [firecrawl](internet.md#firecrawl) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [partialjson](software-development-libraries-2.md#partialjson) - Parse incomplete or partial JSON, e.g. from a streaming LLM response
- [aspose-words](office-business.md#aspose-words) - Aspose.Words for Python is a Document Processing library that allows developers to work with documents in many popular formats without needing Office Automation.
- [mkdocs-include-markdown-plugin](documentation.md#mkdocs-include-markdown-plugin) - Mkdocs Markdown includer plugin.
- [pyhwp](software-development-libraries-2.md#pyhwp) - hwp file format parser
- [httpie](internet-www-http.md#httpie) - HTTPie: modern, user-friendly command-line HTTP client for the API era.
- [markdown-graphviz-inline](documentation.md#markdown-graphviz-inline) - Render inline graphs with Markdown and Graphviz (python3 version)
- [tokie](scientific-engineering-artificial-intelligence.md#tokie) - Blazingly fast tokenizer — 50x faster, 10x smaller, 100% accurate
- [nicknames](scientific-engineering-information-analysis.md#nicknames) - Hand-curated dataset of English names and nicknames.
- [textwrap3](software-development-libraries-2.md#textwrap3) - textwrap from Python 3.6 backport (plus a few tweaks)
- [sphinxcontrib-websupport](documentation.md#sphinxcontrib-websupport) - sphinxcontrib-websupport provides a Python API to easily integrate Sphinx documentation into your Web application
- [sphinxext-opengraph](documentation.md#sphinxext-opengraph) - Sphinx Extension to enable OGP support
- [ansiwrap](software-development-libraries-2.md#ansiwrap) - textwrap, but savvy to ANSI colors and styles
- [borb](artistic-software.md#borb) - borb is a library for reading, creating and manipulating PDF files in python.
- [ripgrep-bin](terminals.md#ripgrep-bin) - ripgrep is a line-oriented search tool that recursively searches the current directory for a regex pattern while respecting gitignore rules.
- [pytest-md-report](software-development-quality-assurance.md#pytest-md-report) - A pytest plugin to generate test outcomes reports with markdown table format.
- [feedgen](communications.md#feedgen) - Feed Generator (ATOM, RSS, Podcasts)
- [segtok](scientific-engineering-information-analysis.md#segtok) - sentence segmentation and word tokenization tools
- [mkdocs-swagger-ui-tag](documentation.md#mkdocs-swagger-ui-tag) - A MkDocs plugin supports for add Swagger UI in page.
- [msgfy](software-development-libraries-2.md#msgfy) - msgfy is a Python library for convert Exception instance to a human-readable error message.
- [DateTimeRange](software-development-libraries-3.md#datetimerange) - DateTimeRange is a Python library to handle a time range. e.g. check whether a time is within the time range, get the intersection of time ranges, truncate a time range, iterate through a time range, and so forth.
- [yake](scientific-engineering-information-analysis.md#yake) - Keyword extraction Python package
- [pdfrw2](multimedia-graphics.md#pdfrw2) - PDF file reader/writer library
- [mkdocs-git-authors-plugin](documentation.md#mkdocs-git-authors-plugin) - Mkdocs plugin to display git authors of a page
- [newspaper4k](software-development-libraries-3.md#newspaper4k) - Simplified python article discovery & extraction.
- [detect-delimiter](software-development-libraries-3.md#detect-delimiter) - Detects the delimiter used in CSV, TSV and other ad hoc file formats.
- [Cheetah3](internet-www-http.md#cheetah3) - Cheetah is a template engine and code generation tool
- [mkdocs-print-site-plugin](documentation.md#mkdocs-print-site-plugin) - MkDocs plugin that combines all pages into one, allowing for easy export to PDF and standalone HTML.
- [sphinxext-rediraffe](documentation.md#sphinxext-rediraffe) - Sphinx Extension that redirects non-existent pages to working pages
- [hachoir](multimedia.md#hachoir) - Package of Hachoir parsers used to open binary files
- [t61codec](communications.md#t61codec) - Python Codec for ITU T.61 Strings
- [tangled-up-in-unicode](database.md#tangled-up-in-unicode) - Access to the Unicode Character Database (UCD)
- [stop-words](software-development.md#stop-words) - Get list of common stop words in various languages in Python
- [lorem](software-development-libraries-3.md#lorem) - Generator for random text that looks like Latin.
- [kreuzberg](office-business.md#kreuzberg) - High-performance document intelligence library for Python. Extract text, metadata, and structured data from PDFs, Office documents, images, and 88+ formats. Powered by Rust core for 10-50x speed improvements.
- [tailer](software-development-libraries-3.md#tailer) - Python tail is a simple implementation of GNU tail and head.
- [beautifultable](printing.md#beautifultable) - Print text tables for terminals
- [mechanize](internet.md#mechanize) - Stateful, programmatic web browsing
- [pdf-oxide](scientific-engineering-information-analysis.md#pdf-oxide) - The fastest Python PDF library — 0.8ms mean, 5× faster than the industry leaders, 100% pass rate on 3,830 real-world PDFs. Text extraction, Markdown/HTML conversion, PDF creation and editing.
- [fastnumbers](scientific-engineering-information-analysis.md#fastnumbers) - Super-fast and clean conversions to numbers.
- [humps](software-development.md#humps) - camelCase converter
- [nvidia-sphinx-theme](documentation.md#nvidia-sphinx-theme) - A Sphinx theme for NVIDIA projects
- [sphinx-intl](documentation.md#sphinx-intl) - Sphinx utility that make it easy to translate and to apply translation.
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
- [rst2pdf](documentation.md#rst2pdf) - Convert reStructured Text to PDF via ReportLab.
- [PyPDFForm](file-formats.md#pypdfform) - The Python library & CLI for PDF forms.
- [base58check](internet-www-http.md#base58check) - Base58check encoding and decoding of binary data
- [stringparser](software-development-libraries-3.md#stringparser) - Easy to use pattern matching and information extraction
- [suffix-trees](scientific-engineering-2.md#suffix-trees) - Suffix trees, generalized suffix trees and string processing methods
- [textcase](software-development.md#textcase) - Python library for text case conversions.
- [rowdump](software-development-libraries-4.md#rowdump) - A modern structured Python library for formatted table output
- [sphinx-favicon](documentation.md#sphinx-favicon) - Sphinx Extension adding support for custom favicons
- [sharepoint-to-text](communications-email.md#sharepoint-to-text) - Text extraction library for typical file formats found in SharePoint repositories
- [hanziconv](system.md#hanziconv) - Hanzi Converter for Traditional and Simplified Chinese
- [json-source-map](software-development-disassemblers.md#json-source-map) - Calculate the source map for a JSON document.
- [pansi](software-development.md#pansi) - Text mode rendering library
- [docling-rs](scientific-engineering-artificial-intelligence.md#docling-rs) - Fast, local document-to-Markdown for LLMs and RAG: docling in Rust, with docling's, MarkItDown's, Marker's and MinerU's Python APIs. PDF (layout, tables, OCR), DOCX, PPTX, XLSX, HTML, EPUB, email and more.
- [dxpdf](office-business.md#dxpdf) - A fast DOCX-to-PDF converter powered by Skia, written in Rust
- [humanreadable](software-development-libraries-4.md#humanreadable) - humanreadable is a Python library to convert human-readable values to other units.
- [linuxdoc](software-development-documentation.md#linuxdoc) - Sphinx-doc extensions & tools to extract documentation from C/C++ source file comments.
- [ascii-guard](software-development-quality-assurance.md#ascii-guard) - A minimal-dependency Python linter for detecting and fixing misaligned ASCII art boxes in documentation
- [pingparsing](software-development-libraries-4.md#pingparsing) - pingparsing is a CLI-tool/Python-library parser and transmitter for the ping command.
- [ansi2txt](terminals.md#ansi2txt) - ansi to plain text converter
- [toonify](software-development-libraries-4.md#toonify) - TOON (Token-Oriented Object Notation) - A compact, human-readable serialization format for LLMs
- [konlpy](scientific-engineering-2.md#konlpy) - Python package for Korean natural language processing.
- [pystempel](scientific-engineering-2.md#pystempel) - Polish stemmer.
- [endesive](communications-email.md#endesive) - Digital signatures for PDF, S/MIME, XML (XAdES), and CMS in Python.
- [tika-client](software-development-libraries-5.md#tika-client) - A modern REST client for Apache Tika server
- [pytest-github-report](software-development-testing.md#pytest-github-report) - Generate a GitHub report using pytest in GitHub Workflows
