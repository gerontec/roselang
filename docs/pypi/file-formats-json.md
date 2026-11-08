# File Formats / JSON

[Index](README.md) · 13 packages in this topic, by downloads.

### jsonschema

An implementation of JSON Schema validation for Python

`pip install jsonschema` · installs (wheel) · licence: MIT · rank 48 · last release 2026-01-07 · [PyPI](https://pypi.org/project/jsonschema/) · [docs](https://python-jsonschema.readthedocs.io/) · [source](https://github.com/python-jsonschema/jsonschema)

<details><summary>README extract</summary>

`jsonschema` is an implementation of the JSON Schema specification for Python.

It can also be used from the command line by installing check-jsonschema.

Features:
* Full support for Draft 2020-12, Draft 2019-09, Draft 7, Draft 6, Draft 4 and Draft 3

* Lazy validation that can iteratively report *all* validation errors.

* Programmatic querying of which properties or items failed validation.

Example:
```python
>>> from jsonschema import validate

>>> # A sample schema, like what we'd get from json.load()
>>> schema = {
...     "type" : "object",
...     "properties" : {
...         "price" : {"type" : "number"},
...         "name" : {"type" : "string"},
...     },
... }

>>> # If no exception is raised by validate(), the instance is valid.
...
```

...

</details>

### referencing

JSON Referencing + Python

`pip install referencing` · installs (wheel) · licence: MIT · rank 52 · last release 2025-10-13 · [PyPI](https://pypi.org/project/referencing/) · [docs](https://referencing.readthedocs.io/) · [source](https://github.com/python-jsonschema/referencing)

<details><summary>README extract</summary>

An implementation-agnostic implementation of JSON reference resolution.

See the documentation for more details.

</details>

### jsonschema-specifications

The JSON Schema meta-schemas and vocabularies, exposed as a Registry

`pip install jsonschema-specifications` · installs (wheel) · licence: MIT · rank 54 · last release 2025-09-08 · [PyPI](https://pypi.org/project/jsonschema-specifications/) · [docs](https://jsonschema-specifications.readthedocs.io/) · [source](https://github.com/python-jsonschema/jsonschema-specifications)

<details><summary>README extract</summary>

JSON support files from the JSON Schema Specifications (metaschemas, vocabularies, etc.), packaged for runtime access from Python as a referencing-based Schema Registry.

</details>

### jiter

Fast iterable JSON parser.

`pip install jiter` · installs (wheel) · licence: MIT · rank 87 · last release 2026-11-06 · [PyPI](https://pypi.org/project/jiter/)

<details><summary>README extract</summary>

This is a standalone version of the JSON parser used in `pydantic-core`. The recommendation is to only use this package directly if you do not use `pydantic`.

The API is extremely minimal:

Example:
```python
import jiter

json_data = b'{"name": "John", "age": 30}'
parsed_data = jiter.from_json(json_data)
print(parsed_data)  # Output: {'name': 'John', 'age': 30}
```

Sections: jiter, Examples, Handling Partial JSON, Catching Duplicate Keys

</details>

### holidays

Open World Holidays Framework

`pip install holidays` · installs (wheel) · licence: MIT · rank 638 · last release 2026-11-02 · [PyPI](https://pypi.org/project/holidays/) · [docs](https://holidays.readthedocs.io/en/latest/) · [source](https://github.com/vacanza/holidays/)

<details><summary>README extract</summary>

A fast, efficient Python library for generating country- and subdivision- (e.g. state or province)
specific sets of government-designated holidays on the fly. It aims to make determining whether a
specific date is a holiday as fast and flexible as possible.

 PyPI


 Code

 Docs

 GitHub

 Citation

Example:
```python
from datetime import date
import holidays

us_holidays = holidays.US()  # this is a dict-like object
# the below is the same, but takes a string:
us_holidays = holidays.country_holidays("US")  # this is a dict-like object

nyse_holidays = holidays.NYSE()  # this is a dict-like object
# the below is the same, but takes a string:
...
```

Sections: Holidays, Documentation, ICS Exports, Quick Start, Available Countries, Available Financial Markets

</details>

### genson

GenSON is a powerful, user-friendly JSON Schema generator.

`pip install genson` · installs (wheel) · licence: MIT License · rank 903 · last release 2026-07-06 · [PyPI](https://pypi.org/project/genson/)

<details><summary>README extract</summary>

GenSON is a powerful, user-friendly JSON Schema generator built in Python.

GenSON's core function is to take JSON objects and generate schemas that describe them, but it is unique in its ability to *merge* schemas. ...

Example:
```python
from genson import SchemaBuilder
from genson.schema.strategies import Number

class MinNumber(Number):
    # add 'minimum' to list of keywords
    KEYWORDS = (*Number.KEYWORDS, 'minimum')

    # create a new instance variable
    def init(self, node_class):
        super().init(node_class)
        self.min = None

...
```

...

</details>

### rfc8785

A pure-Python implementation of RFC 8785 (JSON Canonicalization Scheme)

`pip install rfc8785` · installs (wheel) · licence: Apache Software License · rank 1063 · last release 2024-09-27 · [PyPI](https://pypi.org/project/rfc8785/) · [docs](https://trailofbits.github.io/rfc8785.py/) · [source](https://github.com/trailofbits/rfc8785.py)

<details><summary>README extract</summary>

<!--- BADGES: START --->

<!--- BADGES: END --->

A pure-Python, no-dependency implementation of [RFC 8785], a.k.a. JSON Canonicalization Scheme or JCS.

This implementation should be behaviorally comparable to
[Andrew Rundgren's reference implementation], with the following added constraints:

1. ...

Example:
```python
import rfc8785

foo = {
    "key": "value",
    "another-key": 2,
    "a-third": [1, 2, 3, [4], (5, 6, "this works too")],
    "more": [None, True, False],
}

rfc8785.dumps(foo)
```

Sections: rfc8785.py, Usage, Licensing

</details>

### jsonschema-rs

A high-performance JSON Schema validator for Python

`pip install jsonschema-rs` · installs (wheel) · licence: MIT License · rank 1431 · last release 2026-10-27 · [PyPI](https://pypi.org/project/jsonschema-rs/) · [source](https://github.com/Stranger6667/jsonschema)

<details><summary>README extract</summary>

[](

A high-performance JSON Schema validator for Python.

> ⚠️ Upgrading from older versions? See the Migration Guide for breaking changes.

> Migrating from `jsonschema`? See the jsonschema migration guide.

Features:
- 📚 Drafts 4, 6, 7, 2019-09 and 2020-12
- 🔧 Custom keywords and format validators
- ⚡ Compile-time validators for your own extension modules, via the Rust crate
- 🌐 `$ref` resolution over HTTP and from files ...

Example:
```python
import jsonschema_rs

validator = jsonschema_rs.validator_for('{"minimum": 42}')
...
```

...

</details>

### numpydantic

Type and shape validation and serialization for arbitrary array types in pydantic models

`pip install numpydantic` · installs (wheel) · licence: MIT · rank 6233 · last release 2026-11-06 · [PyPI](https://pypi.org/project/numpydantic/) · [docs](https://numpydantic.readthedocs.io) · [source](https://github.com/p2p-ld/numpydantic)

<details><summary>README extract</summary>

A python package for specifying, validating, and serializing arrays with arbitrary backends with or without pydantic. Static typing and type checker integration for array constraints.

Problem:
1) Pydantic is great for modeling data.
2) Arrays are one of a few elemental types in computing,

but ... ...

Features:
- Types - Annotations (based on npytyping)
 for specifying arrays in pydantic models, with static type checker support!
- Validation - Shape, dtype, and other array validations ...

Example:
```python
from typing import Literal as L, Union
from pydantic import BaseModel
import numpy as np

from numpydantic import NDArray, Shape

class Image(BaseModel):
    array: Union[
        NDArray[Shape[int, int], float],
        NDArray[Shape[int, int, L[3]], np.uint8],
...

</details>

### zcbor

Code generation and data validation using CDDL schemas

`pip install zcbor` · installs (wheel) · licence: Apache Software License · rank 8092 · last release 2024-10-17 · [PyPI](https://pypi.org/project/zcbor/)

<details><summary>README extract</summary>

After installing, zcbor can be invoked on the command line as `zcbor`, or included as a module via `import zcbor`.

This package has 2 uses:

1. Schema-based validation and conversion of YAML/JSON/CBOR data.
2. Generating C code that decodes/encodes and validates CBOR data according to a schema. ...

</details>

### json-strong-typing

Type-safe data interchange for Python data classes

`pip install json-strong-typing` · installs (wheel) · licence: MIT · rank 12270 · last release 2026-10-27 · [PyPI](https://pypi.org/project/json-strong-typing/) · [source](https://github.com/hunyadi/strong_typing)

<details><summary>README extract</summary>

JSON is a popular message interchange format employed in API design for its simplicity, readability, flexibility and wide support. However, `json.dump` and `json.load` offer no direct support when working with Python data classes employing type annotations. ...

Features:
This package offers the following services:

* JSON serialization and de-serialization
 * Generate a JSON object from a Python object (`serialization.object_to_json`)
 * Parse a JSON object into a Python object (`serialization.json_to_object`)
* ...

Example:
```python
@dataclass
class Example:
    "A simple data class with multiple properties."

    bool_value: bool = True
    int_value: int = 23
    float_value: float = 4.5
    str_value: str = "string"
...

</details>

### jixia

Python binding for jixia

`pip install jixia` · installs (wheel) · licence: MIT · rank 13218 · last release 2026-01-18 · [PyPI](https://pypi.org/project/jixia/) · [source](https://github.com/frenzymath/jixia_py)

### pyjsonpatch

A Python implementation of JSON Pointer and JSON Patch

`pip install pyjsonpatch` · installs (wheel) · licence: Apache Software License · rank 13394 · last release 2025-02-25 · [PyPI](https://pypi.org/project/pyjsonpatch/)

<details><summary>README extract</summary>

A Python implementation of JSON Pointer (RFC 6902) and JSON Patch (RFC 6902). Primarily, the package can do the following to Python object(s) representing JSON(s):
- `apply_patch` to modify an object with a JSON patch
- `generate_patch` to generate a JSON Patch from two objects
- `get_by_ptr` to retrieve a value from object using a JSON pointer

Example:
```python
from pyjsonpatch import get_by_ptr

source = {"": 1, "foo": [2, 3]}

print(get_by_ptr(source, "").obj)
# {"": 1, "foo": [2, 3]}
print(get_by_ptr(source, "/").obj)
# 1
print(get_by_ptr(source, "/foo").obj)
# [2, 3]
print(get_by_ptr(source, "/foo/0").obj)
# 2
```

Sections: pyjsonpatch, About, Linting and Formatting, Building and Releasing, Examples, `get_by_ptr`, `apply_patch`, `generate_patch`

</details>

