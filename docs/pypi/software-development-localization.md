# Software Development / Localization

[Index](README.md) · 3 packages in this topic, 25 more listed under another topic, by downloads.

### timezonefinder

Python package for offline timezone lookup of WGS84 coordinates, with no polygon simplification

`pip install timezonefinder` · installs (wheel) · licence: not stated · rank 1635 · last release 2026-10-22 · [PyPI](https://pypi.org/project/timezonefinder/) · [docs](https://timezonefinder.readthedocs.io/en/latest/) · [source](https://github.com/jannikmi/timezonefinder)

<details><summary>README extract</summary>

Python package for offline timezone lookup of WGS84 coordinates, with no polygon simplification - so the answer stays correct at timezone borders.

In comparison to other alternatives this package aims at maximum accuracy around timezone borders while offering fast lookup performance and compatibility with many (Python) runtime environments. ...

Example:
```python
# use the global function for convenience:
from timezonefinder import timezone_at

tz = timezone_at(lng=13.358, lat=52.5061)  # 'Europe/Berlin'

# For improved performance and control, reuse one instance for the whole job.
# The context manager releases its coordinate data even if the job raises:
from timezonefinder import TimezoneFinder

...
```

...

</details>

### timezonefinder-data

the packaged timezone boundary data for the timezonefinder Python package

`pip install timezonefinder-data` · installs (wheel) · licence: not stated · rank 3068 · last release 2026-11-01 · [PyPI](https://pypi.org/project/timezonefinder-data/) · [docs](https://timezonefinder.readthedocs.io/en/latest/) · [source](https://github.com/jannikmi/timezonefinder)

<details><summary>README extract</summary>

The timezone boundary data used by
timezonefinder, compiled from
timezone-boundary-builder
releases into the binary format described in
the data format reference.

`pip install timezonefinder` installs this package automatically - there is nothing
extra to do. ...

</details>

### tzwhere

Python library to look up timezone from lat / long offline

`pip install tzwhere` · installs from source (sdist only) · licence: MIT License · rank 7078 · last release 2017-08-24 · [PyPI](https://pypi.org/project/tzwhere/)

<details><summary>README extract</summary>

pytzwhere

pytzwhere is a Python library to lookup the timezone for a given lat/lng entirely offline.

Version 3.0 fixes how `pytzwhere` deals with holes in timezones. It is recommended that you use version 3.0.

It is a port from with a few improvements. The underlying timezone data is based on work done by Eric Muller ...

</details>

## Also in this topic

- [wcwidth](software-development-internationalization.md#wcwidth) - Measures the displayed width of unicode strings in a terminal
- [pycountry](software-development-internationalization.md#pycountry) - ISO country, subdivision, language, currency and script definitions and their translations
- [num2words](software-development-internationalization.md#num2words) - Modules to convert numbers to words. Easily extensible.
- [polib](software-development-internationalization.md#polib) - A library to manipulate gettext files (po and mo files).
- [lingua-language-detector](scientific-engineering-information-analysis.md#lingua-language-detector) - An accurate natural language detection library, suitable for short text and mixed-language text
- [hijridate](scientific-engineering.md#hijridate) - Accurate Hijri-Gregorian dates converter based on Umm al-Qura calendar
- [pyunormalize](software-development-internationalization.md#pyunormalize) - A library for Unicode normalization (NFC, NFD, NFKC, NFKD) independent of Python's core Unicode database.
- [translationstring](software-development-internationalization.md#translationstring) - Utility library for i18n relied on by various Repoze and Pyramid packages
- [measurement](scientific-engineering.md#measurement) - Easily use and manipulate unit-aware measurements in Python.
- [OpenCC](scientific-engineering.md#opencc) - Conversion between Traditional and Simplified Chinese
- [pythainlp](scientific-engineering-artificial-intelligence.md#pythainlp) - Thai Natural Language Processing library
- [spark-nlp](scientific-engineering.md#spark-nlp) - John Snow Labs Spark NLP is a natural language processing library built on top of Apache Spark ML. It provides simple, performant & accurate NLP annotations for machine learning pipelines, that scale easily in a distributed environment.
- [pyicu](software-development-internationalization.md#pyicu) - Python extension wrapping the ICU C++ API
- [iso639-lang](software-development-internationalization.md#iso639-lang) - A fast, comprehensive, ISO 639 library.
- [flufl.i18n](software-development-internationalization.md#flufli18n) - A high level API for internationalizing Python libraries and applications
- [simplemma](scientific-engineering-information-analysis.md#simplemma) - Fast and zero-dependency lemmatization, tokenization and sentence splitting for 54 languages.
- [geoip2fast](internet.md#geoip2fast) - GeoIP2Fast is the fastest GeoIP2 country/city/asn lookup library that supports IPv4 and IPv6. A search takes less than 0.00003 seconds. It has its own data file updated twice a week with Maxmind-Geolite2-CSV, supports IPv4/IPv6 and is Pure Python!
- [python-gettext](software-development-internationalization.md#python-gettext) - Python Gettext po to mo file compiler.
- [PyICU-binary](software-development-internationalization.md#pyicu-binary) - Python extension wrapping the ICU C++ API
- [django-rosetta](software-development-internationalization.md#django-rosetta) - A Django application that eases the translation of Django projects
- [translate-toolkit](software-development-internationalization.md#translate-toolkit) - Tools and API for translation and localization engineering.
- [wlc](software-development-internationalization.md#wlc) - A command-line utility for Weblate, translation tool with tight version control integration
- [pyicu-wheels](software-development-internationalization.md#pyicu-wheels) - Wheels for PyICU
- [pyCalverter](software-development-libraries-4.md#pycalverter) - Python Calendar Converter
- [weblate-fonts](software-development-internationalization.md#weblate-fonts) - Weblate fonts collection
