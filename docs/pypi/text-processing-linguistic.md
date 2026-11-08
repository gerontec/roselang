# Text Processing / Linguistic

[Index](README.md) · 24 packages in this topic, 141 more listed under another topic, by downloads.

### charset-normalizer

The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet.

`pip install charset-normalizer` · installs (wheel) · licence: MIT · rank 7 · last release 2026-09-30 · [PyPI](https://pypi.org/project/charset-normalizer/) · [docs](https://charset-normalizer.readthedocs.io/) · [source](https://github.com/jawah/charset_normalizer)

<details><summary>README extract</summary>

The Real First Universal Charset Detector

 Featured Packages

 In other language (unofficial port - by the community)

> A library that helps you read text from an unknown charset encoding.
 Motivated by `chardet`,
> I'm trying to resolve the issue by taking a new approach. ...

Example:
```python
usage: normalizer [-h] [-v] [-a] [-n] [-m] [-r] [-f] [-t THRESHOLD]
                  file [file ...]

The Real First Universal Charset Detector. Discover originating encoding used
on text file. Normalize text to unicode.

positional arguments:
  files                 File(s) to be analysed

optional arguments:
...
```

...

</details>

### textblob

Simple, Pythonic text processing. Sentiment analysis, part-of-speech tagging, noun phrase parsing, and more.

`pip install textblob` · installs (wheel) · licence: MIT · rank 2538 · last release 2026-07-18 · [PyPI](https://pypi.org/project/textblob/) · [source](https://github.com/sloria/TextBlob)

<details><summary>README extract</summary>

Homepage:

`TextBlob` is a Python library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, and more.

TextBlob stands on the giant shoulders of NLTK and pattern, and plays nicely with both.

Features:
- Noun phrase extraction
- Part-of-speech tagging
- Sentiment analysis
- Classification (Naive Bayes, Decision Tree)
- Tokenization (splitting text into words and sentences)
- Word and phrase frequencies
- Parsing
- `n`-grams ...

Example:
```python
from textblob import TextBlob

text = """
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
...

</details>

### syllapy

Calculate syllable counts for English words.

`pip install syllapy` · installs (wheel) · licence: MIT · rank 3857 · last release 2026-08-01 · [PyPI](https://pypi.org/project/syllapy/)

<details><summary>README extract</summary>

Calculate syllable counts for English words.

Installation

Usage

</details>

### fugashi

Cython MeCab wrapper for fast, pythonic Japanese tokenization.

`pip install fugashi` · installs (wheel) · licence: MIT AND BSD-3-Clause · rank 4452 · last release 2025-10-24 · [PyPI](https://pypi.org/project/fugashi/) · [source](https://github.com/polm/fugashi)

<details><summary>README extract</summary>

fugashi is a Cython wrapper for MeCab, a
Japanese tokenizer and morphological analysis tool. Wheels are provided for
Linux, OSX (Intel), and Win64, and UniDic is easy to install.

issueを英語で書く必要はありません。 ...

Example:
```python
from fugashi import Tagger

tagger = Tagger('-Owakati')
text = "麩菓子は、麩を主材料とした日本の菓子。"
tagger.parse(text)
# => '麩 菓子 は 、 麩 を 主材 料 と し た 日本 の 菓子 。'
for word in tagger(text):
    print(word, word.feature.lemma, word.pos, sep='\t')
    # "feature" is the Unidic feature data as a named tuple
```

Sections: fugashi, Usage, Dictionary Use, Alternatives

</details>

### pycld2

Python bindings around Google Chromium's embedded compact language detection library (CLD2)

`pip install pycld2` · installs from source (sdist only) · licence: Apache Software License · rank 4685 · last release 2025-03-28 · [PyPI](https://pypi.org/project/pycld2/)

<details><summary>README extract</summary>

Python bindings for the Compact Langauge Detect 2 (CLD2).

This package contains forks of:

- The `cld2` C++ library, developed by Dick Sites
- The `chromium-compact-language-detector` C++ extension module,
 originally created by Mike McCandless, which has been modified post-fork. ...

Example:
```python
import pycld2 as cld2

isReliable, textBytesFound, details = cld2.detect(
    "а неправильный формат идентификатора дн назад"
)

print(isReliable)
# True
details[0]
# ('RUSSIAN', 'ru', 98, 404.0)

fr_en_Latn = """\
France is the largest country in Western Europe and the third-largest in Europe as a whole.
...
```

Sections: PYCLD2 - Python Bindings to CLD2, Example, API, Constants, What About CLD3?

</details>

### rouge

Full Python ROUGE Score Implementation (not a wrapper)

`pip install rouge` · installs (wheel) · licence: LICENCE.txt · rank 5047 · last release 2021-07-20 · [PyPI](https://pypi.org/project/rouge/)

<details><summary>README extract</summary>

*A full Python librarie for the ROUGE metric (paper).*

This implementation is independant from the "official" ROUGE script (aka. `ROUGE-155`).
Results may be *slighlty* different, see discussions in #2.

Example:
```python
from rouge import Rouge

hypothesis = "the #### transcript is a written version of each day 's cnn student news program use this transcript to he    lp students with reading comprehension and vocabulary use the weekly newsquiz to test your knowledge of storie s you     saw on cnn student news"

...
```

Sections: Rouge, Disclaimer, Quickstart, Use it from the shell (JSON Output), As a library, Score 1 sentence, Score multiple sentences, Score two files (line by line)

</details>

### wonderwords

Generate random english words and phrases.

`pip install wonderwords` · installs (wheel) · licence: MIT License · rank 5260 · last release 2025-10-30 · [PyPI](https://pypi.org/project/wonderwords/) · [docs](https://wonderwords.readthedocs.io)

<details><summary>README extract</summary>

Generate random words and sentences with ease in python

Quick links:

 * GitHub repository
 * PyPI page
 * Official Documentation


Wonderwords is a python package useful for generating random words and
structured random sentences. It also comes with a colorful command line
interface for quickly generating random words. ...

Features:
Here's what Wonderwords is capable of:

- Random word generation
- Specify word length, what it starts and ends with, category, and even custom
 regular expressions!
- Use custom word lists and define custom categories of words ...

Example:
```python
from wonderwords import RandomWord

r = RandomWord()

# generate a random word
r.word()

# random word that starts with a and ends with en
r.word(starts_with="a", ends_with="en")

...

</details>

### zhconv

A simple implementation of Simplified-Traditional Chinese conversion.

`pip install zhconv` · installs from source (sdist only) · licence: GNU General Public License v2 or later (GPLv2+) · rank 5688 · last release 2021-10-31 · [PyPI](https://pypi.org/project/zhconv/)

_README extract left out: share-alike licence._

### sentence-stream

A small sentence splitter for text streams

`pip install sentence-stream` · installs (wheel) · licence: Apache Software License · rank 5705 · last release 2026-10-28 · [PyPI](https://pypi.org/project/sentence-stream/) · [source](http://github.com/OHF-Voice/sentence-stream)

<details><summary>README extract</summary>

A small sentence splitter for text streams.

Sentences come out as soon as their boundary is certain, so a stream of text
chunks — from an LLM, say — can be handed to a text-to-speech engine a sentence
at a time instead of waiting for the whole response.

Example:
```python
from sentence_stream import stream_to_sentences

text_chunks = [
    "Text chunks that a",
    "re not on",
    " word or se",
    "ntence boundarie",
    "s. But, they w",
    "ill sti",
    "ll get sp",
    "lit right",
    "!!! Goo",
    "d",
]

assert list(stream_to_sentences(text_chunks)) == [
...
```

Sections: Sentence Stream, Example, Pushing chunks yourself, What counts as a boundary, Known limitations

</details>

### rouge-metric

A fast python implementation of full ROUGE metrics for automatic summarization.

`pip install rouge-metric` · installs (wheel) · licence: MIT License · rank 7587 · last release 2020-10-21 · [PyPI](https://pypi.org/project/rouge-metric/)

<details><summary>README extract</summary>

A fast Python implementation of full ROUGE metric for automatic summarization evaluation. A Python wrapper of the official `ROUGE-1.5.5.pl` Perl script is also available.

Features:
For the Perl script wrapper:

+ Easy to install: No need to manually download and configure the Perl scripts. It works as long as Perl is installed.
+ Cross platform: Support Linux, macOS and Windows machines. ...

Example:
```python
from rouge_metric import PerlRouge

rouge = PerlRouge(rouge_n_max=3, rouge_l=True, rouge_w=True,
    rouge_w_weight=1.2, rouge_s=True, rouge_su=True, skip_gap=4)

# Load summary results and evaluate
hypotheses = [
    'how are you\ni am fine',                       # document 1: hypothesis
...
```

...

</details>

### unicode-rbnf

Rule-based number formatting using Unicode CLDR data

`pip install unicode-rbnf` · installs (wheel) · licence: MIT License · rank 9004 · last release 2026-10-06 · [PyPI](https://pypi.org/project/unicode-rbnf/) · [source](https://github.com/rhasspy/unicode-rbnf)

<details><summary>README extract</summary>

A pure Python implementation of rule based number formatting (RBNF) using the Unicode Common Locale Data Repository (CLDR).

This lets you spell out numbers for a large number of locales:

Different formatting purposes are supported as well, depending on the locale: ...

Example:
```python
from unicode_rbnf import RbnfEngine

engine = RbnfEngine.for_language("en")
assert engine.format_number(1234).text == "one thousand two hundred thirty-four"
```

Sections: Unicode RBNF, Engine implementation

</details>

### recurrent

Natural language parsing and formatting of recurring events

`pip install recurrent` · installs from source (sdist only) · licence: BSD License · rank 9321 · last release 2021-08-16 · [PyPI](https://pypi.org/project/recurrent/)

### spylls

Hunspell ported to pure Python

`pip install spylls` · installs (wheel) · licence: MIT License · rank 9736 · last release 2022-01-23 · [PyPI](https://pypi.org/project/spylls/)

<details><summary>README extract</summary>

Spylls is an effort of porting prominent spellcheckers into clear, well-structured, well-documented Python. It is intended to be useful both as a library and as some kind of "reference (or investigatory, if you will) implementation". Currently, only Hunspell is ported. ...

Example:
```python
from spylls.hunspell import Dictionary

# en_US dictionary is distributed with spylls
# See docs to load other dictionaries
dictionary = Dictionary.from_files('en_US')

print(dictionary.lookup('spylls'))
# False
for suggestion in dictionary.suggest('spylls'):
    print(suggestion)
# spells
# spills
```

Sections: Spylls: Hunspell ported to Python, Usage as a library, Documentation, Project Links

</details>

### PyArabic

Arabic text tools for Python

`pip install PyArabic` · installs (wheel) · licence: GPL · rank 9944 · last release 2022-06-18 · [PyPI](https://pypi.org/project/PyArabic/)

_README extract left out: share-alike licence._

### hassil

The Home Assistant Intent Language parser

`pip install hassil` · installs (wheel) · licence: Apache Software License · rank 10812 · last release 2026-09-14 · [PyPI](https://pypi.org/project/hassil/) · [source](https://github.com/OHF-Voice/hassil)

<details><summary>README extract</summary>

The Home Assistant Intent Language (HassIL) parser for intents.

Template syntax

* PyYAML

Sections: HassIL, Dependencies, Running, Sampling Sentences, Sentence Templates, YAML Format, Inline Range Lists

</details>

### home-assistant-intents

Intents for Home Assistant

`pip install home-assistant-intents` · installs (wheel) · licence: Apache-2.0 · rank 10933 · last release 2026-10-27 · [PyPI](https://pypi.org/project/home-assistant-intents/) · [source](https://github.com/OHF-Voice/intents)

### wyoming

Peer-to-peer protocol for voice assistants

`pip install wyoming` · installs (wheel) · licence: MIT · rank 11725 · last release 2026-11-02 · [PyPI](https://pypi.org/project/wyoming/)

<details><summary>README extract</summary>

Sections: Wyoming Projects, Format, Event Types, Audio, Info, Speech Recognition, Text to Speech, Wake Word, Voice Activity Detection, Intent Recognition, Intent Handling, Audio Output, Voice Satellite, Timers

</details>

### mosestokenizer

Wrappers for several pre-processing scripts from the Moses toolkit.

`pip install mosestokenizer` · installs from source (sdist only) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 12701 · last release 2021-10-22 · [PyPI](https://pypi.org/project/mosestokenizer/)

_README extract left out: share-alike licence._

### textacy

NLP, before and after spaCy

`pip install textacy` · installs (wheel) · licence: Apache Software License · rank 13006 · last release 2023-04-02 · [PyPI](https://pypi.org/project/textacy/) · [docs](https://textacy.readthedocs.io)

<details><summary>README extract</summary>

`textacy` is a Python library for performing a variety of natural language processing (NLP) tasks, built on the high-performance spaCy library. With the fundamentals --- tokenization, part-of-speech tagging, dependency parsing, etc. --- delegated to another library, `textacy` focuses primarily on the tasks that come before and follow after.

Features:
- Access and extend spaCy's core functionality for working with one or many documents through convenient methods and custom extensions ...

Sections: textacy: NLP, before and after spaCy, features, links

</details>

### stopwordsiso

Collection of stopwords for multiple languages, using ISO 639-1 language code.

`pip install stopwordsiso` · installs (wheel) · licence: MIT · rank 13301 · last release 2026-07-07 · [PyPI](https://pypi.org/project/stopwordsiso/) · [source](https://github.com/bact/stopwords-iso.git)

<details><summary>README extract</summary>

Collection of stopwords for multiple languages, using ISO 639-1 language code.

This Python package is based on Stopwords ISO project by
Gene Diaz. You can see the full list of stopwords in every language available
there. Contribution to the word lists should also happen there.

Comparable packages also published on
npm and
bower.

Example:
```python
import stopwordsiso

stopwordsiso.has_lang("th")  # True if there are stopwords for Thai
stopwordsiso.langs()  # frozenset of all supported ISO 639-1 language codes
```

Sections: stopwordsiso, Usage, Stopwords data

</details>

### indic-transliteration

Transliteration tools to convert text in one indic script encoding to another

`pip install indic-transliteration` · installs (wheel) · licence: MIT License · rank 13715 · last release 2026-04-06 · [PyPI](https://pypi.org/project/indic-transliteration/)

### rouge-chinese

Python ROUGE Score Implementation for Chinese Language Task (official rouge score)

`pip install rouge-chinese` · installs (wheel) · licence: LICENCE.txt · rank 14147 · last release 2022-09-18 · [PyPI](https://pypi.org/project/rouge-chinese/)

<details><summary>README extract</summary>

*A full Python librarie for the ROUGE metric in Chinese Language Task (paper).*

专用于计算中文rouge指标的python库。

This library based on the code from pltrdy. Using the original code to compute rouge score in Chinese would meet some problems. For example, the stack overflow issue would occur and the Chinese sentences are not splited correctly. ...

Example:
```python
from rouge_chinese import Rouge
import jieba # you can use any other word cutting library

hypothesis = "###刚刚发声，A股这种情况十分罕见！大聪明逆市抄底330亿，一篇研报引爆全球，市场逻辑生变？"
hypothesis = ' '.join(jieba.cut(hypothesis))

...
```

Sections: Rouge-Chinese, Difference, 不同点, Quickstart, Use it as a library, Score 1 sentence, Score multiple sentences, Score two files (line by line), Use it from the shell (JSON Output)

</details>

### pysilero-vad

Pre-packaged voice activity detector using silero-vad

`pip install pysilero-vad` · installs (wheel) · licence: MIT License · rank 14391 · last release 2026-07-07 · [PyPI](https://pypi.org/project/pysilero-vad/)

<details><summary>README extract</summary>

A pre-packaged voice activity detector using silero-vad.

Example:
```python
from pysilero_vad import SileroVoiceActivityDetector

vad = SileroVoiceActivityDetector()

# Audio must be 16Khz, 16-bit mono PCM with correct chunk size
# See also: vad.chunk_samples()
assert len(audio_bytes) == vad.chunk_bytes()

if vad(audio_bytes) >= 0.5:
    print("Speech")
else:
    print("Silence")
```

</details>

### iso-639

Python library for ISO 639 standard

`pip install iso-639` · installs from source (sdist only) · licence: GNU Affero General Public License v3 · rank 14788 · last release 2016-04-29 · [PyPI](https://pypi.org/project/iso-639/)

_README extract left out: share-alike licence._

## Also in this topic

- [chardet](software-development-libraries.md#chardet) - Universal character encoding detector
- [lark](software-development-libraries.md#lark) - a modern parsing library
- [text-unidecode](software-development-libraries.md#text-unidecode) - The most basic Text::Unidecode port
- [humanfriendly](communications.md#humanfriendly) - Human friendly output for text interfaces using Python
- [tree-sitter](software-development-compilers.md#tree-sitter) - Python bindings to the Tree-sitter parsing library
- [nltk](scientific-engineering.md#nltk) - Natural Language Toolkit
- [pyphen](text-processing.md#pyphen) - Pure Python module to hyphenate text
- [snowballstemmer](database.md#snowballstemmer) - This package provides 36 stemmers for 34 languages generated from Snowball algorithms.
- [sentencepiece](software-development-libraries.md#sentencepiece) - Unsupervised text tokenizer and detokenizer.
- [inflect](software-development-libraries.md#inflect) - Correctly generate plurals, singular nouns, ordinals, indefinite articles
- [htmldate](internet-www-http.md#htmldate) - Fast and robust extraction of original and updated publication dates from URLs and web pages.
- [courlan](internet-www-http.md#courlan) - Clean, filter and sample URLs to optimize data collection – includes spam, content type and language filters.
- [trafilatura](internet-www-http.md#trafilatura) - Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extraction, output as CSV, JSON, HTML, MD, TXT, XML.
- [tree-sitter-javascript](software-development-compilers.md#tree-sitter-javascript) - JavaScript grammar for tree-sitter
- [tree-sitter-python](software-development-compilers.md#tree-sitter-python) - Python grammar for tree-sitter
- [tree-sitter-typescript](software-development-compilers.md#tree-sitter-typescript) - TypeScript and TSX grammars for tree-sitter
- [tree-sitter-bash](software-development-compilers.md#tree-sitter-bash) - Bash grammar for tree-sitter
- [num2words](software-development-internationalization.md#num2words) - Modules to convert numbers to words. Easily extensible.
- [tree-sitter-c](software-development-compilers.md#tree-sitter-c) - C grammar for tree-sitter
- [tree-sitter-java](software-development-compilers.md#tree-sitter-java) - Java grammar for tree-sitter
- [tree-sitter-go](software-development-compilers.md#tree-sitter-go) - Go grammar for tree-sitter
- [tree-sitter-c-sharp](software-development-compilers.md#tree-sitter-c-sharp) - C# grammar for tree-sitter
- [tree-sitter-rust](software-development-compilers.md#tree-sitter-rust) - Rust grammar for tree-sitter
- [python-crfsuite](scientific-engineering.md#python-crfsuite) - Python binding for CRFsuite
- [tree-sitter-yaml](software-development-compilers.md#tree-sitter-yaml) - YAML grammar for tree-sitter
- [jieba](text-processing.md#jieba) - Chinese Words Segmentation Utilities
- [tree-sitter-cpp](software-development-compilers.md#tree-sitter-cpp) - C++ grammar for tree-sitter
- [polib](software-development-internationalization.md#polib) - A library to manipulate gettext files (po and mo files).
- [intervaltree](scientific-engineering-artificial-intelligence.md#intervaltree) - Editable interval tree data structure for Python 2 and 3
- [tree-sitter-ruby](software-development-compilers.md#tree-sitter-ruby) - Ruby grammar for tree-sitter
- [tree-sitter-php](software-development-compilers.md#tree-sitter-php) - PHP grammar for tree-sitter
- [anyascii](text-processing-general.md#anyascii) - Unicode to ASCII transliteration
- [lingua-language-detector](scientific-engineering-information-analysis.md#lingua-language-detector) - An accurate natural language detection library, suitable for short text and mixed-language text
- [pysbd](scientific-engineering.md#pysbd) - pysbd (Python Sentence Boundary Disambiguation) is a rule-based sentence boundary detection that works out-of-the-box across many languages.
- [pyunormalize](software-development-internationalization.md#pyunormalize) - A library for Unicode normalization (NFC, NFD, NFKC, NFKD) independent of Python's core Unicode database.
- [lark-parser](software-development-libraries.md#lark-parser) - a modern parsing library
- [nameparser](software-development-libraries.md#nameparser) - A simple Python module for parsing human names into their individual components.
- [tree-sitter-json](software-development-compilers.md#tree-sitter-json) - JSON grammar for tree-sitter
- [python-iso639](text-processing.md#python-iso639) - ISO 639 language codes, names, and other associated information
- [marisa-trie](scientific-engineering-information-analysis.md#marisa-trie) - Static memory-efficient and fast Trie-like structures for Python.
- [tree-sitter-embedded-template](software-development-compilers.md#tree-sitter-embedded-template) - Embedded Template (ERB, EJS) grammar for tree-sitter
- [gensim](scientific-engineering-artificial-intelligence.md#gensim) - Python framework for fast Vector Space Modelling
- [tree-sitter-elixir](software-development-compilers.md#tree-sitter-elixir) - Elixir grammar for tree-sitter
- [tree-sitter-kotlin](software-development-compilers.md#tree-sitter-kotlin) - Kotlin grammar for tree-sitter
- [tree-sitter-swift](software-development-compilers.md#tree-sitter-swift) - Swift grammar for tree-sitter
- [tree-sitter-powershell](software-development-compilers.md#tree-sitter-powershell) - A Powershell grammar for tree-sitter
- [tree-sitter-scala](software-development-compilers.md#tree-sitter-scala) - Scala grammar for tree-sitter
- [tree-sitter-lua](software-development-compilers.md#tree-sitter-lua) - Lua grammar for tree-sitter
- [tree-sitter-groovy](software-development-compilers.md#tree-sitter-groovy) - Groovy grammar for tree-sitter
- [tree-sitter-toml](software-development-compilers.md#tree-sitter-toml) - TOML grammar for tree-sitter
- [tree-sitter-objc](software-development-compilers.md#tree-sitter-objc) - Objective-C grammar for tree-sitter
- [tree-sitter-zig](software-development-compilers.md#tree-sitter-zig) - Zig grammar for tree-sitter
- [tree-sitter-julia](software-development-compilers.md#tree-sitter-julia) - Julia grammar for tree-sitter
- [tree-sitter-verilog](software-development-compilers.md#tree-sitter-verilog) - Verilog grammar for tree-sitter
- [tree-sitter-fortran](software-development-compilers.md#tree-sitter-fortran) - Fortran grammar for tree-sitter
- [deep-translator](communications.md#deep-translator) - A flexible free and unlimited python tool to translate between different languages in a simple way using multiple translators
- [tree-sitter-sql](software-development-compilers.md#tree-sitter-sql) - Tree-sitter Grammar for SQL
- [tree-sitter-xml](software-development-compilers.md#tree-sitter-xml) - XML & DTD grammars for tree-sitter
- [tree-sitter-html](software-development-compilers.md#tree-sitter-html) - HTML grammar for tree-sitter
- [PyStemmer](database.md#pystemmer) - Snowball stemming algorithms, for information retrieval
- [chonkie](scientific-engineering-artificial-intelligence.md#chonkie) - 🦛 CHONK your texts with Chonkie ✨ - The no-nonsense chunking library
- [tree-sitter-markdown](software-development-compilers.md#tree-sitter-markdown) - Markdown grammar for tree-sitter
- [tree-sitter-css](software-development-compilers.md#tree-sitter-css) - CSS grammar for tree-sitter
- [text2num](text-processing-filters.md#text2num) - Parse and convert numbers written in French, Spanish, English, Portuguese, German, Dutch, Danish, or Italian into their digit representation.
- [zhon](software-development-libraries-2.md#zhon) - Zhon provides constants used in Chinese text processing.
- [tree-sitter-regex](software-development-compilers.md#tree-sitter-regex) - Regex grammar for tree-sitter
- [hanzidentifier](software-development-libraries-2.md#hanzidentifier) - Python module that identifies Chinese text as Simplified or Traditional.
- [OpenCC](scientific-engineering.md#opencc) - Conversion between Traditional and Simplified Chinese
- [ocrmypdf](scientific-engineering-image-recognition.md#ocrmypdf) - OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched
- [stanza](scientific-engineering.md#stanza) - A Python NLP Library for Many Human Languages, by the Stanford NLP Group
- [mecab-python3](software-development-libraries-2.md#mecab-python3) - Python wrapper for the MeCab morphological analyzer for Japanese
- [pyenchant](software-development-libraries-2.md#pyenchant) - Python bindings for the Enchant spellchecking system
- [py3langid](scientific-engineering-artificial-intelligence.md#py3langid) - Fork of the language identification tool langid.py, featuring a modernized codebase and faster execution times.
- [sentencex](software-development.md#sentencex) - Sentence segmenter that supports ~300 languages
- [pythainlp](scientific-engineering-artificial-intelligence.md#pythainlp) - Thai Natural Language Processing library
- [langid](scientific-engineering-artificial-intelligence.md#langid) - langid.py is a standalone Language Identification (LangID) tool.
- [spark-nlp](scientific-engineering.md#spark-nlp) - John Snow Labs Spark NLP is a natural language processing library built on top of Apache Spark ML. It provides simple, performant & accurate NLP annotations for machine learning pipelines, that scale easily in a distributed environment.
- [kaldialign](scientific-engineering-artificial-intelligence.md#kaldialign) - Kaldi alignment methods wrapped into Python
- [uroman](text-processing.md#uroman) - uroman is a universal romanizer. It converts text in any script to the standard Latin alphabet.
- [cmudict](software-development-libraries-2.md#cmudict) - A versioned python wrapper package for The CMU Pronouncing Dictionary data files.
- [tokie](scientific-engineering-artificial-intelligence.md#tokie) - Blazingly fast tokenizer — 50x faster, 10x smaller, 100% accurate
- [nicknames](scientific-engineering-information-analysis.md#nicknames) - Hand-curated dataset of English names and nicknames.
- [pymorphy3-dicts-ru](scientific-engineering-information-analysis.md#pymorphy3-dicts-ru) - Russian dictionaries for pymorphy2
- [pymorphy3](scientific-engineering-information-analysis.md#pymorphy3) - Morphological analyzer (POS tagger + inflection engine) for Russian language.
- [DAWG2-Python](scientific-engineering-information-analysis.md#dawg2-python) - Pure-python reader for DAWGs (DAFSAs) created by dawgdic C++ library or DAWG Python extension.
- [llm](scientific-engineering-artificial-intelligence.md#llm) - CLI utility and Python library for interacting with Large Language Models from organizations like OpenAI, Anthropic and Gemini plus local models installed on your own machine.
- [tree-sitter-hcl](software-development-compilers.md#tree-sitter-hcl) - HCL and terraform grammar for tree-sitter
- [tinysegmenter](scientific-engineering-artificial-intelligence.md#tinysegmenter) - Very compact Japanese tokenizer
- [weighted-levenshtein](software-development-libraries-2.md#weighted-levenshtein) - Library providing functions to calculate Levenshtein distance, Optimal String Alignment distance, and Damerau-Levenshtein distance, where the cost of each operation can be weighted by letter.
- [iso639-lang](software-development-internationalization.md#iso639-lang) - A fast, comprehensive, ISO 639 library.
- [segtok](scientific-engineering-information-analysis.md#segtok) - sentence segmentation and word tokenization tools
- [kiwipiepy](software-development-libraries-2.md#kiwipiepy) - Kiwi, the Korean Tokenizer for Python
- [yake](scientific-engineering-information-analysis.md#yake) - Keyword extraction Python package
- [kiwipiepy-model](software-development-libraries-3.md#kiwipiepy-model) - Model for kiwipiepy
- [phonetics](internet-www-http.md#phonetics) - Compute phonetic key of strings for indexing or fuzzy matching
- [demoji](text-processing.md#demoji) - Accurately remove and replace emojis in text strings
- [gigatoken](scientific-engineering-artificial-intelligence.md#gigatoken) - Tokenize your documents at GB/s
- [nagisa](software-development-libraries-3.md#nagisa) - A Japanese tokenizer based on recurrent neural networks
- [simplemma](scientific-engineering-information-analysis.md#simplemma) - Fast and zero-dependency lemmatization, tokenization and sentence splitting for 54 languages.
- [pynini](scientific-engineering-artificial-intelligence.md#pynini) - Finite-state grammar compilation
- [lorem](software-development-libraries-3.md#lorem) - Generator for random text that looks like Latin.
- [english](text-processing.md#english) - English language utility library for Python
- [quantulum3](scientific-engineering.md#quantulum3) - Extract quantities from unstructured text.
- [fasttext-langdetect](scientific-engineering-artificial-intelligence.md#fasttext-langdetect) - 80x faster and 95% accurate language identification with fastText
- [tree-sitter-starlark](software-development-compilers.md#tree-sitter-starlark) - Starlark grammar for tree-sitter
- [language_tool_python](software-development-libraries-3.md#language_tool_python) - Checks grammar using LanguageTool.
- [tree-sitter-dart](software-development-compilers.md#tree-sitter-dart) - Dart grammar for tree-sitter (covers Flutter)
- [mwxml](scientific-engineering.md#mwxml) - A set of utilities for processing MediaWiki XML dump data.
- [DAWG-Python](scientific-engineering-information-analysis.md#dawg-python) - Pure-python reader for DAWGs (DAFSAs) created by dawgdic C++ library or DAWG Python extension.
- [pymorphy2-dicts-ru](scientific-engineering-information-analysis.md#pymorphy2-dicts-ru) - Russian dictionaries for pymorphy2
- [lark-js](software-development-libraries-3.md#lark-js) - An extension to Lark that generates a Javascript standalone
- [wn](scientific-engineering-information-analysis.md#wn) - Wordnet interface library
- [snapper-fmt](software-development-version-control.md#snapper-fmt) - Semantic line break formatter for Org, LaTeX, Markdown, and plaintext
- [pymorphy2](scientific-engineering-information-analysis.md#pymorphy2) - Morphological analyzer (POS tagger + inflection engine) for Russian language.
- [sumy](education.md#sumy) - Module for automatic summarization of text documents and HTML pages.
- [textcase](software-development.md#textcase) - Python library for text case conversions.
- [pymorphy3-dicts-uk](scientific-engineering-information-analysis.md#pymorphy3-dicts-uk) - Ukrainian dictionaries for pymorphy3
- [datrie](scientific-engineering-information-analysis.md#datrie) - Super-fast, efficiently stored Trie for Python.
- [urduhack](software-development-libraries-4.md#urduhack) - Natural Language Processing (NLP) library for Urdu language.
- [pyleri](software-development-libraries-4.md#pyleri) - Python Left-Right Parser
- [panphon](software-development-libraries-4.md#panphon) - Tools for using the International Phonetic Alphabet with phonological features
- [chompjs](software-development-libraries-4.md#chompjs) - Parsing JavaScript objects into Python dictionaries
- [natasha](scientific-engineering-artificial-intelligence.md#natasha) - Named-entity recognition for russian language
- [polyglot](scientific-engineering-artificial-intelligence.md#polyglot) - Polyglot is a natural language pipeline that supports massive multilingual applications.
- [pytextrank](scientific-engineering-artificial-intelligence.md#pytextrank) - Python implementation of TextRank as a spaCy pipeline extension, for graph-based natural language work plus related knowledge graph practices; used for for phrase extraction of text documents.
- [python-mecab-ko](text-processing.md#python-mecab-ko) - A python binding for mecab-ko
- [python-mecab-ko-dic](text-processing.md#python-mecab-ko-dic) - mecab-ko-dic packaged for Python
- [Fuzzy](text-processing.md#fuzzy) - Fast Python phonetic algorithms
- [mecab-ko](software-development-libraries-4.md#mecab-ko) - Python wrapper for the MeCab-ko morphological analyzer for Korean
- [tree-sitter-fsharp](software-development-compilers.md#tree-sitter-fsharp) - F# grammars (implementation and signature files) for tree-sitter
- [postal](internet-www-http-2.md#postal) - Python bindings to libpostal for fast international address parsing/normalization
- [konlpy](scientific-engineering-2.md#konlpy) - Python package for Korean natural language processing.
- [tree-sitter-cmake](software-development-compilers.md#tree-sitter-cmake) - CMake grammar for tree-sitter
- [pyxDamerauLevenshtein](scientific-engineering-bio-informatics.md#pyxdameraulevenshtein) - pyxDamerauLevenshtein implements the Damerau-Levenshtein (DL) edit distance algorithm for Python in Cython for high performance.
- [tree-sitter-pascal](software-development-compilers.md#tree-sitter-pascal) - Pascal grammar for tree-sitter
- [tree-sitter-haskell](software-development-compilers.md#tree-sitter-haskell) - Haskell grammar for tree-sitter
- [pystempel](scientific-engineering-2.md#pystempel) - Polish stemmer.
- [tree-sitter-vb-dotnet](software-development-compilers.md#tree-sitter-vb-dotnet) - Tree sitter grammar for VB.NET
- [neologdn](text-processing.md#neologdn) - Japanese text normalizer for mecab-neologd
- [tree-sitter-luau](software-development-compilers.md#tree-sitter-luau) - Luau grammar for tree-sitter
- [tree-sitter-svelte](software-development-compilers.md#tree-sitter-svelte) - Svelte grammar for tree-sitter
