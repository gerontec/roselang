# Education / Testing

[Index](README.md) · 4 packages in this topic, 7 more listed under another topic, by downloads.

### hypothesis

The property-based testing library for Python

`pip install hypothesis` · installs (wheel) · licence: MPL-2.0 · rank 384 · last release 2026-11-06 · [PyPI](https://pypi.org/project/hypothesis/) · [docs](https://hypothesis.readthedocs.io) · [source](https://github.com/HypothesisWorks/hypothesis)

<details><summary>README extract</summary>

* Website
* Documentation
* Source code
* Contributing
* Community

Hypothesis is the property-based testing library for Python. With Hypothesis, you write tests which should pass for all inputs in whatever range you describe, and let Hypothesis randomly choose which of those inputs to check - including edge cases you might not have thought about. ...

Example:
```python
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_matches_builtin(ls):
    assert sorted(ls) == my_sort(ls)
```

</details>

### hypothesis-jsonschema

Generate test data from JSON schemata with Hypothesis

`pip install hypothesis-jsonschema` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 2718 · last release 2026-10-27 · [PyPI](https://pypi.org/project/hypothesis-jsonschema/)

<details><summary>README extract</summary>

A Hypothesis strategy for generating data
that matches some JSON schema.

Here's the PyPI page.

The public API consists of just one function: `hypothesis_jsonschema.from_schema`,
which takes a JSON schema and returns a strategy for allowed JSON objects. ...

Example:
```python
from hypothesis import given

from hypothesis_jsonschema import from_schema

@given(from_schema({"type": "integer", "minimum": 1, "exclusiveMaximum": 10}))
def test_integers(value):
    assert isinstance(value, int)
    assert 1 <= value < 10

@given(
    from_schema(
        {"type": "string", "format": "card"},
...
```

Sections: hypothesis-jsonschema, API

</details>

### python-benedict

python-benedict is a dict subclass with keylist/keypath/keyattr support, normalized I/O operations (base64, csv, ini, json, pickle, plist, query-string, toml, xls, xml, yaml) and many utilities... for humans, obviously.

`pip install python-benedict` · installs (wheel) · licence: MIT License · rank 5323 · last release 2026-10-20 · [PyPI](https://pypi.org/project/python-benedict/) · [docs](https://github.com/fabiocaccamo/python-benedict#readme)

<details><summary>README extract</summary>

python-benedict is a dict subclass with keylist/keypath/keyattr support, I/O shortcuts (`base64`, `cli`, `csv`, `html`, `ini`, `json`, `pickle`, `plist`, `query-string`, `toml`, `xls`, `xml`, `yaml`) and many utilities... for humans, obviously.

Features:
- 100% backward-compatible, you can safely wrap existing dictionaries.
- `NEW` Keyattr support for get/set items using keys as attributes.
- Keylist support using list of keys as key. ...

Example:
```python
from benedict import benedict

# create a new empty instance
d = benedict()

# or cast an existing dict
d = benedict(existing_dict)

# or create from data source (filepath, url or data-string) in a supported format:
# Base64, CSV, JSON, TOML, XML, YAML, query-string
d = benedict(" format="json")

# or in a Django view
...
```

...

</details>

### radish-bdd

Behaviour-Driven-Development tool for Python

`pip install radish-bdd` · installs (wheel) · licence: MIT License · rank 12284 · last release 2026-02-24 · [PyPI](https://pypi.org/project/radish-bdd/)

<details><summary>README extract</summary>

> Awesome python BDD tool



radish is a Behavior Driven Development tool completely written in python.
It supports all *gherkin* language features.
In addition to that, radish implements a few *unconventional* BDD features such as Preconditions, Scenario Loops, Constants and Expressions.

Sections: radish - the root from red to green, What is radish?, Getting started, Documentation, Special Thanks

</details>

## Also in this topic

- [tqdm](desktop-environment.md#tqdm) - Fast, Extensible Progress Meter
- [progressbar2](desktop-environment.md#progressbar2) - A Python Progressbar library to provide visual (yet text based) progress to long running operations.
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [shtab](desktop-environment.md#shtab) - Automagic shell tab completion for Python CLI applications
- [word2number](documentation-sphinx.md#word2number) - Convert number words eg. three hundred and forty two to numbers (342).
- [lap](education.md#lap) - Linear Assignment Problem solver (LAPJV/LAPMOD).
- [lapx](education.md#lapx) - Linear assignment problem solvers, including single and batch solvers.
