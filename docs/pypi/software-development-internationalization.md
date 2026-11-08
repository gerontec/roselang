# Software Development / Internationalization

[Index](README.md) · 26 packages in this topic, 5 more listed under another topic, by downloads.

### wcwidth

Measures the displayed width of unicode strings in a terminal

`pip install wcwidth` · installs (wheel) · licence: MIT License · rank 119 · last release 2026-10-24 · [PyPI](https://pypi.org/project/wcwidth/)

<details><summary>README extract</summary>

This Python and C11 library is mainly for CLI/TUI programs that carefully produce output for
Terminals. This page is about the Python library, see libwcwidth for the portable C11 library.

Features:
A brief overview, through examples, for all of the public API functions.

Full API Documentation at

Example:
```python
>>> # result consumes 16 total cells, 11 expected,
>>> 'コンニチハ'.rjust(11, 'X')
'XXXXXXコンニチハ'

>>> # combining acute accent: result consumes 5 total cells, 6 expected,
>>> 'cafe\u0301'.center(6, 'X')
'caféX'
```

Sections: Introduction, Problem, Solution, Discrepancies, Overview, wcwidth(), wcswidth(), wcstwidth(), width(), iter_sequences(), iter_graphemes(), ljust(), rjust(), center()

</details>

### babel

Internationalization utilities

`pip install babel` · installs (wheel) · licence: BSD License · rank 259 · last release 2026-02-01 · [PyPI](https://pypi.org/project/babel/) · [source](https://github.com/python-babel/babel)

<details><summary>README extract</summary>

A collection of tools for internationalizing Python applications.

</details>

### pycountry

ISO country, subdivision, language, currency and script definitions and their translations

`pip install pycountry` · installs (wheel) · licence: LGPL-2.1-only · rank 586 · last release 2026-02-17 · [PyPI](https://pypi.org/project/pycountry/) · [source](https://github.com/pycountry/pycountry)

_README extract left out: share-alike licence._

### num2words

Modules to convert numbers to words. Easily extensible.

`pip install num2words` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 1258 · last release 2024-12-17 · [PyPI](https://pypi.org/project/num2words/)

_README extract left out: share-alike licence._

### polib

A library to manipulate gettext files (po and mo files).

`pip install polib` · installs (wheel) · licence: MIT License · rank 1759 · last release 2023-02-23 · [PyPI](https://pypi.org/project/polib/)

<details><summary>README extract</summary>

Features:
polib is a library to manipulate, create, modify gettext files (pot, po and mo
files). You can load existing files, iterate through it's entries, add, modify
entries, comments or metadata, etc... or create new po files from scratch. ...

Example:
```python
import polib

pofile = polib.pofile('/path/to/pofile.po')

for entry in pofile:
    print(entry.msgid, entry.msgstr)
```

Sections: polib, Overview, Basic example, Version 1.2.0 (2023/02/23), Version 1.1.1 (2021/03/26), Version 1.1.0 (2017/11/27), Version 1.0.8 (2016/11/21), Version 1.0.7 (2015/07/08), Version 1.0.6 (2015/01/04), Version 1.0.5 (2014/08/22), Version 1.0.4 (2014/02/19), Version 1.0.3 (2013/02/09), Version 1.0.2 (2012/10/23), Version 1.0.1 (2012/09/11)

</details>

### pyunormalize

A library for Unicode normalization (NFC, NFD, NFKC, NFKD) independent of Python's core Unicode database.

`pip install pyunormalize` · installs (wheel) · licence: MIT · rank 2211 · last release 2026-09-26 · [PyPI](https://pypi.org/project/pyunormalize/) · [source](https://github.com/mlodewijck/pyunormalize)

<details><summary>README extract</summary>

The `pyunormalize` package is a pure-Python, zero-dependency implementation of the Unicode normalization algorithm.

It supports the four standard Unicode normalization forms:

- NFC
- NFD
- NFKC
- NFKD ...

Example:
```python
from pyunormalize import NFC, NFD, NFKC, NFKD, normalize
```

Sections: pyunormalize, Requirements, Public API, Usage examples, Dedicated functions, Generic `normalize` function, Related resources

</details>

### translationstring

Utility library for i18n relied on by various Repoze and Pyramid packages

`pip install translationstring` · installs (wheel) · licence: Repoze Public License · rank 2970 · last release 2020-07-09 · [PyPI](https://pypi.org/project/translationstring/)

<details><summary>README extract</summary>

A library used by various Pylons Project packages
for internationalization (i18n) duties related to translation.

This package provides a *translation string* class, a *translation string
factory* class, translation and pluralization primitives, and a utility that
helps Chameleon templates use
translation facilities of this package. ...

Sections: translationstring, 1.4 (2020-07-09), 1.3 (2014-11-05), 1.2 (2014-11-04), 1.1 (2012-02-08), 1.0 (2012-02-04), 0.4 (09-22-2011), 0.3 (06-25-2010), 0.2 (04-25-2010), 0.1 (04-24-2010)

</details>

### pyicu

Python extension wrapping the ICU C++ API

`pip install pyicu` · installs from source (sdist only) · licence: OSI Approved · rank 5222 · last release 2026-10-23 · [PyPI](https://pypi.org/project/pyicu/)

<details><summary>README extract</summary>

Welcome to PyICU, a Python extension wrapping the ICU C++ libraries.

ICU stands for "International Components for Unicode".
These are the i18n libraries of the Unicode Consortium.
They implement much of the Unicode Standard,
many of its companion Unicode Technical Standards,
and much of Unicode CLDR.

The PyICU source code is hosted at ...

Example:
```python
e = TimeZone.createEnumeration()
[s for s in e] # a list of 'str' objects
[s for s in iter(e.unext, '')] # a list of 'str' or 'unicode' objects
[s for s in iter(e.snext, '')] # a list of 'UnicodeString' objects
```

...

</details>

### forex-python

Free foreign exchange rates and currency conversion.

`pip install forex-python` · installs (wheel) · licence: MIT License · rank 5558 · last release 2025-05-22 · [PyPI](https://pypi.org/project/forex-python/) · [docs](https://forex-python.readthedocs.io/) · [source](https://github.com/MicroPyramid/forex-python)

<details><summary>README extract</summary>

Forex Python is a free library for foreign exchange rates and currency conversion, supporting Python 3.6 and above.

> Note: Install the latest version (`forex-python>=1.6`) to avoid `RatesNotAvailableError`.

Features:
- List all currency rates
- Bitcoin price for all currencies
- Convert amounts to and from Bitcoin
- Get historical rates (since 1999)
- Currency conversion (e.g., USD to INR)
- Currency symbols and names

Example:
```python
from forex_python.converter import CurrencyRates
c = CurrencyRates()
```

Sections: forex-python, Features, Currency Source, Bitcoin Price Source, Usage Examples

</details>

### iso639-lang

A fast, comprehensive, ISO 639 library.

`pip install iso639-lang` · installs (wheel) · licence: MIT License · rank 6044 · last release 2025-07-23 · [PyPI](https://pypi.org/project/iso639-lang/)

<details><summary>README extract</summary>

`iso639-lang` handles the ISO 639 code for individual languages and language groups.

Example:
```python
>>> from iso639 import Lang
```

Sections: iso639-lang, Usage, Other Language Names, Language Type, Macrolanguage & Individual Languages, Exceptions, Checker, Iterator, Speed, Sources

</details>

### flufl.i18n

A high level API for internationalizing Python libraries and applications

`pip install flufl.i18n` · installs (wheel) · licence: Apache Software License · rank 6275 · last release 2026-10-13 · [PyPI](https://pypi.org/project/flufl.i18n/) · [docs](https://flufli18n.readthedocs.io) · [source](https://gitlab.com/flufl/flufl.i18n.git)

<details><summary>README extract</summary>

A high level API for internationalizing Python libraries and applications.

The `flufl.i18n` library provides a convenient API for managing translation
contexts in Python applications. ...

Sections: flufl.i18n, Project details

</details>

### i18nice

Translation library for Python

`pip install i18nice` · installs (wheel) · licence: MIT License · rank 6714 · last release 2025-05-29 · [PyPI](https://pypi.org/project/i18nice/)

<details><summary>README extract</summary>

This library provides i18n functionality for Python 3 out of the box. The usage is mostly based on Rails i18n library.

CHANGELOG

CONTRIBUTING

Example:
```python
import i18n
i18n.add_translation('foo', 'bar')
i18n.t('foo') # bar
```

Sections: i18nice, Usage, Basic usage, Using translation files, Memoization, Load everything, Namespaces, File namespaces, Directory namespaces, Functionalities, Placeholder, Pluralization, Fallback, Skip locale from root

</details>

### python-gettext

Python Gettext po to mo file compiler.

`pip install python-gettext` · installs (wheel) · licence: BSD License · rank 8266 · last release 2023-03-30 · [PyPI](https://pypi.org/project/python-gettext/)

<details><summary>README extract</summary>

Features:
This implementation of Gettext for Python includes a Msgfmt class which can be
used to generate compiled mo files from Gettext po files and includes support
for the newer msgctxt keyword. ...

Sections: Overview, 5.0 (2023-03-30), 4.1 (2022-08-26), 4.0 (2018-11-27), 3.0 - 2016-01-04, 2.1 - 2013-02-10, 2.0 - 2011-12-22, 1.2 - 2011-11-01, 1.1.1 - 2011-03-21, 1.1 - 2011-03-20, 1.0 - 2009-05-23, 0.6 - 2007-11-02, 0.5 - 2007-11-01, 0.4 - 2007-10-13

</details>

### PyICU-binary

Python extension wrapping the ICU C++ API

`pip install PyICU-binary` · installs from source (sdist only) · licence: OSI Approved · rank 8588 · last release 2021-09-14 · [PyPI](https://pypi.org/project/PyICU-binary/)

<details><summary>README extract</summary>

Welcome to PyICU, a Python extension wrapping the ICU C++ libraries.

ICU stands for "International Components for Unicode".
These are the i18n libraries of the Unicode Consortium.
They implement much of the Unicode Standard,
many of its companion Unicode Technical Standards,
and much of Unicode CLDR.

The PyICU source code is hosted at ...

Example:
```python
e = TimeZone.createEnumeration()
[s for s in e] # a list of 'str' objects
[s for s in iter(e.unext, '')] # a list of 'str' or 'unicode' objects
[s for s in iter(e.snext, '')] # a list of 'UnicodeString' objects
```

Sections: README file for PyICU, Welcome, Building PyICU, Running PyICU, What's available, API Documentation, strings, error reporting, dates, arrays, StringEnumeration, timezones, Further Reading

</details>

### django-rosetta

A Django application that eases the translation of Django projects

`pip install django-rosetta` · installs (wheel) · licence: MIT License · rank 8743 · last release 2025-12-07 · [PyPI](https://pypi.org/project/django-rosetta/)

<details><summary>README extract</summary>

Rosetta is a Django application that facilitates the translation process of your Django projects.

Because it doesn't export any models, Rosetta doesn't create any tables in your project's database. ...

Features:
* Reads and writes your project's `gettext` catalogs (po and mo files)
* Installed and uninstalled in under a minute
* Uses Django's admin interface CSS
* Get automatic translations via Deepl, OpenAI, Google Translate and more.

Sections: Django-Rosetta, Features, Documentation

</details>

### google-i18n-address

Address validation helpers for Google's i18n address database

`pip install google-i18n-address` · installs (wheel) · licence: BSD License · rank 9226 · last release 2024-09-04 · [PyPI](https://pypi.org/project/google-i18n-address/) · [source](https://github.com/mirumee/google-i18n-address)

<details><summary>README extract</summary>

This package contains a copy of Google's i18n address metadata repository that contains great data but comes with no uptime guarantees.

Contents of this package will allow you to programmatically build address forms that adhere to rules of a particular region or country, validate local addresses, and format them to produce a valid address label ...

Example:
```python
from i18naddress import InvalidAddressError, normalize_address

try:
    address = normalize_address({'country_code': 'US'})
except InvalidAddressError as e:
    print(e.errors)
```

Sections: Google i18n address, Addresses validation, Address fields, Errors, Address latinization, Address formatting, Validation rules, All known fields, Raw i18n data, Used with Django form

</details>

### l18n

Internationalization for pytz timezones and territories

`pip install l18n` · installs (wheel) · licence: MIT License · rank 9975 · last release 2021-11-12 · [PyPI](https://pypi.org/project/l18n/)

<details><summary>README extract</summary>

2014-2021 Thomas Khyn

Locale internationalization package. Translations for places, timezones ...

Tested with the latest minor versions of Python 2 and 3.

Supported languages: English, French, German, Czech, Chinese
(want to add yours?) ...

Example:
```python
>>> import l18n
```

Sections: l18n, What is l18n?, How does it work?, Lazy mappings special features (v.2016.6.3 onwards), Selecting the language, Utilities, Versionning, Want to add a language?, Roadmap

</details>

### kitchen

Kitchen contains a cornucopia of useful code

`pip install kitchen` · installs from source (sdist only) · licence: GNU Library or Lesser General Public License (LGPL) · rank 10061 · last release 2019-05-14 · [PyPI](https://pypi.org/project/kitchen/)

_README extract left out: share-alike licence._

### translate-toolkit

Tools and API for translation and localization engineering.

`pip install translate-toolkit` · installs (wheel) · licence: GPL-3.0-or-later · rank 10724 · last release 2026-11-06 · [PyPI](https://pypi.org/project/translate-toolkit/) · [docs](https://docs.translatehouse.org/projects/translate-toolkit/) · [source](https://github.com/translate/translate)

_README extract left out: share-alike licence._

### speaklater

implements a lazy string for python useful for use with gettext

`pip install speaklater` · installs from source (sdist only) · licence: BSD License · rank 10833 · last release 2012-07-01 · [PyPI](https://pypi.org/project/speaklater/)

<details><summary>README extract</summary>

speaklater
~~~~~~~~~~

A module that provides lazy strings for translations. Basically you
get an object that appears to be a string but changes the value every
time the value is evaluated based on a callable you provide. ...

</details>

### wlc

A command-line utility for Weblate, translation tool with tight version control integration

`pip install wlc` · installs (wheel) · licence: GPL-3.0-or-later · rank 11407 · last release 2026-11-03 · [PyPI](https://pypi.org/project/wlc/) · [docs](https://docs.weblate.org/) · [source](https://github.com/WeblateOrg/wlc)

_README extract left out: share-alike licence._

### pyicu-wheels

Wheels for PyICU

`pip install pyicu-wheels` · installs (wheel) · licence: Apache-2.0 · rank 11662 · last release 2026-03-11 · [PyPI](https://pypi.org/project/pyicu-wheels/) · [docs](https://github.com/Init7/pyicu#readme) · [source](https://github.com/Init7/pyicu)

### icu-messageformat

ICU MessageFormat runtime backed by Rust and ICU4X

`pip install icu-messageformat` · installs (wheel) · licence: BSD-3-Clause · rank 11815 · last release 2026-10-19 · [PyPI](https://pypi.org/project/icu-messageformat/)

<details><summary>README extract</summary>

Python bindings for FormatJS's Rust ICU MessageFormat runtime.

Example:
```python
from icu_messageformat import IcuMessageFormat

message = IcuMessageFormat("{count, plural, one {# item} other {# items}}")
assert message.format({"count": 2}) == "2 items"
```

</details>

### babelfish

A module to work with countries and languages

`pip install babelfish` · installs (wheel) · licence: BSD License · rank 11943 · last release 2024-05-09 · [PyPI](https://pypi.org/project/babelfish/) · [source](https://github.com/Diaoul/babelfish)

<details><summary>README extract</summary>

BabelFish is a Python library to work with countries and languages.

Example:
```python
>>> import babelfish
>>> script = babelfish.Script('Hira')
>>> script
<Script [Hira]>
```

Sections: BabelFish, Usage, Script, Country, Language

</details>

### weblate-fonts

Weblate fonts collection

`pip install weblate-fonts` · installs (wheel) · licence: OFL-1.1 · rank 14071 · last release 2026-01-20 · [PyPI](https://pypi.org/project/weblate-fonts/) · [docs](https://docs.weblate.org/) · [source](https://github.com/WeblateOrg/fonts)

<details><summary>README extract</summary>

**Weblate is libre software web-based continuous localization system,
used by over 2500 libre projects and companies in more than 165 countries.**

Fonts used in Weblate.

</details>

### precis-i18n

PRECIS-i18n: Internationalized Usernames and Passwords

`pip install precis-i18n` · installs (wheel) · licence: MIT License · rank 14840 · last release 2025-10-13 · [PyPI](https://pypi.org/project/precis-i18n/)

<details><summary>README extract</summary>

If you want your application to accept Unicode user names and passwords,
you must be careful in how you validate and compare them. The PRECIS
framework makes internationalized user names and passwords safer for use
by applications. PRECIS profiles transform Unicode strings into a
canonical form, suitable for comparison. ...

Example:
```python
>>> from precis_i18n import get_profile
>>> username = get_profile('UsernameCaseMapped')
>>> username.enforce('Kevin')
'kevin'
>>> username.enforce('\u212Aevin')
'kevin'
>>> username.enforce('\uFF2Bevin')
'kevin'
>>> username.enforce('\U0001F17Aevin')
Traceback (most recent call last):
  ...
...
```

...

</details>

## Also in this topic

- [lingua-language-detector](scientific-engineering-information-analysis.md#lingua-language-detector) - An accurate natural language detection library, suitable for short text and mixed-language text
- [hijridate](scientific-engineering.md#hijridate) - Accurate Hijri-Gregorian dates converter based on Umm al-Qura calendar
- [iso4217](office-business-financial.md#iso4217) - ISO 4217 currency data package for Python
- [spark-nlp](scientific-engineering.md#spark-nlp) - John Snow Labs Spark NLP is a natural language processing library built on top of Apache Spark ML. It provides simple, performant & accurate NLP annotations for machine learning pipelines, that scale easily in a distributed environment.
- [simplemma](scientific-engineering-information-analysis.md#simplemma) - Fast and zero-dependency lemmatization, tokenization and sentence splitting for 54 languages.
