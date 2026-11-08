# Unclassified / E

[Index](README.md) · 151 packages in this topic, by downloads.

### et-xmlfile

An implementation of lxml.xmlfile for the standard library

`pip install et-xmlfile` · installs (wheel) · licence: MIT License · rank 104 · last release 2024-10-25 · [PyPI](https://pypi.org/project/et-xmlfile/) · [docs](https://openpyxl.pages.heptapod.net/et_xmlfile/) · [source](https://foss.heptapod.net/openpyxl/et_xmlfile)

<details><summary>README extract</summary>

XML can use lots of memory, and et_xmlfile is a low memory library for creating large XML files
And, although the standard library already includes an incremental parser, `iterparse` it has no equivalent when writing XML. Once an element has been added to the tree, it is written to
the file or stream and the memory is then cleared. ...

Sections: et_xmfile, Note on performance

</details>

### exceptiongroup

Backport of PEP 654 (exception groups)

`pip install exceptiongroup` · installs (wheel) · licence: MIT License · rank 142 · last release 2025-11-21 · [PyPI](https://pypi.org/project/exceptiongroup/) · [source](https://github.com/agronholm/exceptiongroup)

<details><summary>README extract</summary>

This is a backport of the `BaseExceptionGroup` and `ExceptionGroup` classes from
Python 3.11.

It contains the following:

* The `exceptiongroup.BaseExceptionGroup` and `exceptiongroup.ExceptionGroup`
 classes
* A utility function (`exceptiongroup.catch()`) for catching exceptions possibly
 nested in an exception group
* Patches to the ...

Example:
```python
try:
    ...
except* (ValueError, KeyError) as excgroup:
    for exc in excgroup.exceptions:
        print('Caught exception:', type(exc))
except* RuntimeError:
    print('Caught runtime error')
```

Sections: Catching exceptions, Suppressing exceptions, Notes on monkey patching, Formatting exception groups

</details>

### executing

Get the currently executing AST node of a frame, and other information

`pip install executing` · installs (wheel) · licence: MIT License · rank 254 · last release 2026-10-10 · [PyPI](https://pypi.org/project/executing/) · [source](https://github.com/alexmojaki/executing)

<details><summary>README extract</summary>

This mini-package lets you get information about what a frame is currently doing, particularly the AST node being executed.

* Usage
 * Getting the AST node
 * Getting the source code of the node
 * Getting the `qualname` of the current function
 * The Source class
* Installation
* How does it work?
* Is it reliable?
* Which nodes can it ...

Example:
```python
import executing

node = executing.Source.executing(frame).node
```

Sections: executing, Usage, Getting the AST node, Getting the source code of the node, Getting the `qualname` of the current function, The `Source` class, How does it work?, Is it reliable?, Which nodes can it identify?, Projects that use this, My Projects

</details>

### ecdsa

ECDSA cryptographic signature library (pure python)

`pip install ecdsa` · installs (wheel) · licence: MIT · rank 508 · last release 2026-03-26 · [PyPI](https://pypi.org/project/ecdsa/)

<details><summary>README extract</summary>

This is an easy-to-use implementation of ECC (Elliptic Curve Cryptography)
with support for ECDSA (Elliptic Curve Digital Signature Algorithm),
EdDSA (Edwards-curve Digital Signature Algorithm) and ECDH
(Elliptic Curve Diffie-Hellman), implemented purely in Python, released under
the MIT license. ...

Features:
This library provides key generation, signing, verifying, and shared secret
derivation for five
popular NIST "Suite B" GF(p) (_prime field) curves, with key lengths of 192,
224, 256, 384, and 521 bits. ...

Example:
```python
from ecdsa import SigningKey
sk = SigningKey.generate() # uses NIST192p
vk = sk.verifying_key
signature = sk.sign(b"message")
assert vk.verify(signature, b"message")
```

...

</details>

### envier

Python application configuration via the environment

`pip install envier` · installs (wheel) · licence: MIT License · rank 531 · last release 2024-10-22 · [PyPI](https://pypi.org/project/envier/)

<details><summary>README extract</summary>

Envier is a Python library for extracting configuration from environment
variables in a declarative and (eventually) 12-factor-app-compliant way.

Sections: Envier, Python application configuration from the environment, Synopsis, Usage, Type Checking, Roadmap

</details>

### elasticsearch

Python client for Elasticsearch

`pip install elasticsearch` · installs (wheel) · licence: Apache-2.0 · rank 581 · last release 2026-09-09 · [PyPI](https://pypi.org/project/elasticsearch/) · [docs](https://elasticsearch-py.readthedocs.io/) · [source](https://github.com/elastic/elasticsearch-py)

<details><summary>README extract</summary>

*The official Python client for Elasticsearch.*

Features:
* Translating basic Python data types to and from JSON
* Configurable automatic discovery of cluster nodes
* Persistent connections
* Load balancing (with pluggable selection strategy) across available nodes
* Failed connection penalization (time ...

Sections: Elasticsearch Python Client, Features, Connecting, Usage, Compatibility, Documentation, Try Elasticsearch and Kibana locally

</details>

### entrypoints

Discover and load entry points from installed packages.

`pip install entrypoints` · installs (wheel) · licence: not stated · rank 591 · last release 2026-10-15 · [PyPI](https://pypi.org/project/entrypoints/) · [docs](https://entrypoints.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

This package is in maintenance-only mode. New code should use the
importlib.metadata module
in the Python standard library to find and load entry points.

Entry points are a way for Python packages to advertise objects with some
common interface. ...

</details>

### einops

A new flavour of deep learning operations

`pip install einops` · installs (wheel) · licence: MIT License · rank 742 · last release 2026-01-26 · [PyPI](https://pypi.org/project/einops/)

<details><summary>README extract</summary>

Flexible and powerful tensor operations for readable and reliable code.

Supports numpy, pytorch, tensorflow, jax, and others.

- 0.8.0: tinygrad backend added, small fixes
- 0.7.0: no-hassle `torch.compile`, support of array api standard and more
- 10'000🎉: github reports that more than 10k project use einops ...

Example:
```python
from einops import rearrange, reduce, repeat
# rearrange elements according to the pattern
output_tensor = rearrange(input_tensor, 't b c -> b c t')
# combine rearrangement and reduction
output_tensor = reduce(input_tensor, 'b c (h h2) (w w2) -> b h w c', 'mean', h2=2, w2=2)
# copy along a new axis
...
```

...

</details>

### elastic-transport

Transport classes and utilities shared among Python Elastic client libraries

`pip install elastic-transport` · installs (wheel) · licence: Apache Software License · rank 787 · last release 2026-06-16 · [PyPI](https://pypi.org/project/elastic-transport/) · [docs](https://elastic-transport-python.readthedocs.io) · [source](https://github.com/elastic/elastic-transport-python)

<details><summary>README extract</summary>

Transport classes and utilities shared among Python Elastic client libraries

This library was lifted from `elasticsearch-py`
and then transformed to be used across all Elastic services
rather than only Elasticsearch.

Sections: elastic-transport-python, Documentation

</details>

### eval-type-backport

Like `typing._eval_type`, but lets older Python versions use newer typing features.

`pip install eval-type-backport` · installs (wheel) · licence: MIT License · rank 810 · last release 2026-06-02 · [PyPI](https://pypi.org/project/eval-type-backport/)

<details><summary>README extract</summary>

This package makes runtime typing inspection with the `typing` module possible with newer syntax in older Python versions.
Specifically, this transforms `X | Y` into `typing.Union[X, Y]`
and `list[X]` into `typing.List[X]` etc. (for all the types made generic in PEP 585)
if the original syntax is not supported in the current Python version. ...

Example:
```python
import typing

from eval_type_backport import install_patch

install_patch()

class Foo:
    a: 'int | str'

print(typing.get_type_hints(Foo))
```

</details>

### edge-tts

Microsoft Edge's TTS

`pip install edge-tts` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 1256 · last release 2026-10-13 · [PyPI](https://pypi.org/project/edge-tts/)

_README extract left out: share-alike licence._

### extract-msg

Extracts emails and attachments saved in Microsoft Outlook's .msg files

`pip install extract-msg` · installs (wheel) · licence: GPL · rank 1289 · last release 2026-11-05 · [PyPI](https://pypi.org/project/extract-msg/)

_README extract left out: share-alike licence._

### eth-utils

eth-utils: Common utility functions for python code that interacts with Ethereum

`pip install eth-utils` · installs (wheel) · licence: MIT License · rank 1381 · last release 2026-03-25 · [PyPI](https://pypi.org/project/eth-utils/)

<details><summary>README extract</summary>

Common utility functions for python code that interacts with Ethereum

Read the documentation.

View the change log.

Sections: Ethereum Utilities, Update Networks, How to bumpversion

</details>

### eth-hash

eth-hash: The Ethereum hashing function, keccak256, sometimes (erroneously) called sha3

`pip install eth-hash` · installs (wheel) · licence: MIT License · rank 1382 · last release 2026-03-25 · [PyPI](https://pypi.org/project/eth-hash/)

<details><summary>README extract</summary>

The Ethereum hashing function, keccak256, sometimes (erroneously) called sha3

Note: the similarly named pyethash
has a completely different use: it generates proofs of work.

This is a low-level library, intended to be used internally by other Ethereum tools. ...

</details>

### eth-typing

eth-typing: Common type annotations for ethereum python packages

`pip install eth-typing` · installs (wheel) · licence: MIT License · rank 1387 · last release 2026-03-25 · [PyPI](https://pypi.org/project/eth-typing/)

<details><summary>README extract</summary>

Common type annotations for ethereum python packages.

Read the documentation.

View the change log.

</details>

### e2b

E2B SDK that give agents cloud environments

`pip install e2b` · installs (wheel) · licence: MIT · rank 1408 · last release 2026-11-04 · [PyPI](https://pypi.org/project/e2b/) · [source](https://github.com/e2b-dev/e2b/tree/main/packages/python-sdk)

<details><summary>README extract</summary>

E2B is an open-source infrastructure that allows you to run AI-generated code in secure isolated sandboxes in the cloud. To start and control sandboxes, use our JavaScript SDK or Python SDK.

Example:
```python
from e2b import Sandbox

with Sandbox.create() as sandbox:
    result = sandbox.commands.run('echo "Hello from E2B!"')
    print(result.stdout)  # Hello from E2B!
```

Sections: What is E2B?, Run your first Sandbox, 2. Get your E2B API key, 3. Start a sandbox and run commands, 4. Bind the configuration to a client, High-concurrency sandbox streams, 5. Code execution with Code Interpreter, 6. Check docs, 7. E2B cookbook

</details>

### eth-abi

eth_abi: Python utilities for working with Ethereum ABI definitions, especially encoding and decoding

`pip install eth-abi` · installs (wheel) · licence: MIT · rank 1411 · last release 2026-08-22 · [PyPI](https://pypi.org/project/eth-abi/) · [docs](https://eth-abi.readthedocs.io/) · [source](https://github.com/ApeWorX/eth-abi.git)

<details><summary>README extract</summary>

Python utilities for working with Ethereum ABI definitions, especially encoding and decoding

Read the documentation.

View the change log.

</details>

### EditorConfig

EditorConfig File Locator and Interpreter for Python

`pip install EditorConfig` · installs (wheel) · licence: Python Software Foundation License · rank 1567 · last release 2025-06-09 · [PyPI](https://pypi.org/project/EditorConfig/) · [source](https://github.com/editorconfig/editorconfig-core-py)

<details><summary>README extract</summary>

EditorConfig Python Core provides the same functionality as the
EditorConfig C Core.
EditorConfig Python core can be used as a command line program or as an
importable library.

EditorConfig makes it easy to maintain the correct coding style when switching
between different text editors and between different projects. ...

Example:
```python
from editorconfig import get_properties, EditorConfigError

filename = "/home/zoidberg/humans/anatomy.md"

try:
    options = get_properties(filename)
except EditorConfigError:
    print("Error occurred while getting EditorConfig properties")
else:
    for key, value in options.items():
        print(f"{key}={value}")
```

Sections: EditorConfig Python Core, EditorConfig Project, Getting Help, Using as a Library, Running Test Cases

</details>

### exa-py

Python SDK for Exa API.

`pip install exa-py` · installs (wheel) · licence: MIT License · rank 1599 · last release 2026-11-06 · [PyPI](https://pypi.org/project/exa-py/)

<details><summary>README extract</summary>

The official Python SDK for Exa, the web search API for AI.

Documentation | Dashboard

Example:
```python
from exa_py import Exa

exa = Exa(api_key="your-api-key")

# Search the web
results = exa.search(
    "blog post about artificial intelligence",
    type="auto",
    contents={"highlights": True}
)

# Ask a question
response = exa.answer("What is the capital of France?")
```

Sections: Exa Python SDK, Quick Start, Search, Raw body fields, Answer, Agent API, Agent Monitors (Beta), Async, Request options, Timeouts and cancellation, Warnings, More

</details>

### eth-account

eth-account: Sign Ethereum transactions and messages with local private keys

`pip install eth-account` · installs (wheel) · licence: MIT · rank 1681 · last release 2026-08-23 · [PyPI](https://pypi.org/project/eth-account/) · [docs](https://eth-account.readthedocs.io/) · [source](https://github.com/ApeWorX/eth-account.git)

<details><summary>README extract</summary>

Sign Ethereum transactions and messages with local private keys

Read the documentation.

View the change log.

</details>

### eth-keys

eth-keys: Common API for Ethereum key operations

`pip install eth-keys` · installs (wheel) · licence: MIT · rank 1683 · last release 2026-08-21 · [PyPI](https://pypi.org/project/eth-keys/) · [source](https://github.com/ApeWorX/eth-keys.git)

<details><summary>README extract</summary>

Common API for Ethereum key operations

> This library and repository was previously located at It was transferred to the Ethereum foundation github in November 2017 and renamed to `eth-keys`. The PyPi package was also renamed from `ethereum-keys` to `eth-keys`.

Read more in the documentation below. View the change log.

Example:
```python
>>> from eth_keys import KeyAPI
>>> from eth_keys.backends import NativeECCBackend
# These are all the same
>>> keys = KeyAPI(NativeECCBackend)
>>> keys = KeyAPI(NativeECCBackend())
>>> keys = KeyAPI('eth_keys.backends.NativeECCBackend')
# Or for the coincurve base backend
>>> keys = KeyAPI('eth_keys.backends.CoinCurveECCBackend')
```

...

</details>

### eth-rlp

eth-rlp: RLP definitions for common Ethereum objects in Python

`pip install eth-rlp` · installs (wheel) · licence: MIT · rank 1685 · last release 2026-08-22 · [PyPI](https://pypi.org/project/eth-rlp/) · [docs](https://eth-rlp.readthedocs.io/) · [source](https://github.com/ApeWorX/eth-rlp.git)

<details><summary>README extract</summary>

RLP definitions for common Ethereum objects in Python

Read the documentation.

View the change log.

</details>

### eth-keyfile

A library for handling the encrypted keyfiles used to store ethereum private keys

`pip install eth-keyfile` · installs (wheel) · licence: MIT · rank 1702 · last release 2026-08-21 · [PyPI](https://pypi.org/project/eth-keyfile/) · [source](https://github.com/ApeWorX/eth-keyfile.git)

<details><summary>README extract</summary>

A library for handling the encrypted keyfiles used to store ethereum private keys

> This library and repository was previously located at It was transferred to the Ethereum foundation github in November 2017 and renamed to `eth-keyfile`. The PyPi package was also renamed from `ethereum-keyfile` to `eth-keyfile`. ...

Example:
```python
>>> from eth_keyfile import load_keyfile
>>> load_keyfile('path/to-my-keystore/keystore.json')
{
    "crypto" : {
        "cipher" : "aes-128-ctr",
        "cipherparams" : {
            "iv" : "6087dab2f9fdbbfaddc31a909735c1e6"
        },
        "ciphertext" : "5318b4d5bcd28de64ee5559e671353e16f075ecae9f99c7a79a38af5f869aa46",
...
```

Sections: eth-keyfile, Documentation, A note on private keys

</details>

### editor

🖋 Open the default text editor 🖋

`pip install editor` · installs (wheel) · licence: MIT · rank 2040 · last release 2026-09-19 · [PyPI](https://pypi.org/project/editor/) · [docs](https://rec.github.io/editor) · [source](https://github.com/rec/editor)

<details><summary>README extract</summary>

`editor` opens the default text editor or your favorite editor to edit an existing file,
a new file, or a tempfile, blocks while the user edits text, then returns the contents
of the file.

You can pass a parameter `editor=` to specify an editor or leave it empty, in which
case the editor is: ...

Sections: 🖋 editor - Open a text editor 🖋, Example 1: Using a temporary file, Example 2: Using a named file, Command and text handling, API Documentation, A note on AI use

</details>

### elasticsearch-dsl

Python client for Elasticsearch

`pip install elasticsearch-dsl` · installs (wheel) · licence: Apache Software License · rank 2057 · last release 2025-04-16 · [PyPI](https://pypi.org/project/elasticsearch-dsl/)

<details><summary>README extract</summary>

As of release 8.18.0, the Elasticsearch DSL package is part of the official
Elasticsearch Python client,
so a separate install is not needed anymore. To migrate, follow these steps:

- Uninstall the `elasticsearch-dsl` package
- Make sure you have version 8.18.0 or newer of the `elasticsearch` package
 installed ...

Example:
```python
from elasticsearch import Elasticsearch
client = Elasticsearch("

response = client.search(
    index="my-index",
    body={
      "query": {
        "bool": {
          "must": [{"match": {"title": "python"}}],
          "must_not": [{"match": {"description": "beta"}}],
          "filter": [{"term": {"category": "search"}}]
        }
      },
...
```

...

</details>

### encutils

(no summary)

`pip install encutils` · installs (wheel) · licence: LGPL-3.0-or-later · rank 2088 · last release 2026-04-19 · [PyPI](https://pypi.org/project/encutils/) · [source](https://github.com/coherent-oss/encutils)

_README extract left out: share-alike licence._

### environs

simplified environment variable parsing

`pip install environs` · installs (wheel) · licence: MIT · rank 2201 · last release 2026-08-29 · [PyPI](https://pypi.org/project/environs/) · [source](https://github.com/sloria/environs)

<details><summary>README extract</summary>

environs is a Python library for parsing environment variables.
It allows you to store configuration separate from your code, as per
The Twelve-Factor App methodology.

Features:
- Type-casting
- Read `.env` files without mutating `os.environ`
- Validation
- Define custom parser behavior
- Framework-agnostic, but integrates well with Flask and Django

Example:
```python
from environs import env

env.read_env()  # read .env file, if it exists
# required variables
gh_user = env("GITHUB_USER")  # => 'sloria'
secret = env("SECRET")  # => raises error if not set

# casting
max_connections = env.int("MAX_CONNECTIONS")  # => 100
ship_date = env.date("SHIP_DATE")  # => datetime.date(1984, 6, 25)
...
```

...

</details>

### e2b-code-interpreter

E2B Code Interpreter - Stateful code execution

`pip install e2b-code-interpreter` · installs (wheel) · licence: MIT · rank 2310 · last release 2026-11-04 · [PyPI](https://pypi.org/project/e2b-code-interpreter/) · [source](https://github.com/e2b-dev/e2b/tree/main/packages/code-interpreter-python)

<details><summary>README extract</summary>

E2B is an open-source infrastructure that allows you run to AI-generated code in secure isolated sandboxes in the cloud. To start and control sandboxes, use our JavaScript SDK or Python SDK.

Source: packages/code-interpreter-python

Example:
```python
from e2b_code_interpreter import Sandbox

with Sandbox.create() as sandbox:
    sandbox.run_code("x = 1")
    execution = sandbox.run_code("x+=1; x")
    print(execution.text)  # outputs 2
```

Sections: What is E2B?, Run your first Sandbox, 2. Get your E2B API key, 3. Execute code with code interpreter inside Sandbox, 4. Bind the configuration to a client, 5. Check docs, 6. E2B cookbook

</details>

### editdistance

Fast implementation of the edit distance (Levenshtein distance)

`pip install editdistance` · installs from source (sdist only) · licence: MIT · rank 2532 · last release 2024-02-10 · [PyPI](https://pypi.org/project/editdistance/) · [docs](https://github.com/roy-ht/editdistance) · [source](https://github.com/roy-ht/editdistance)

<details><summary>README extract</summary>

Fast implementation of the edit distance (Levenshtein distance).

This library simply implements Levenshtein distance with C++ and Cython.

The algorithm used in this library is proposed by
Heikki Hyyrö, "Explaining and extending the bit-parallel approximate string matching algorithm of Myers", (2001) ...

Example:
```python
import editdistance
editdistance.eval('banana', 'bahama')
# 2L
```

Sections: editdistance, Binary wheels, Usage, Simple Benchmark, Distance with Any Object

</details>

### espeakng-loader

A Python package that provides shared library loader for eSpeak NG

`pip install espeakng-loader` · installs (wheel) · licence: not stated · rank 2757 · last release 2025-01-17 · [PyPI](https://pypi.org/project/espeakng-loader/)

<details><summary>README extract</summary>

This package loads the espeak-ng shared library so it will be available for other libraries.

- Linux (x86-64, arm64)
- Windows (x86-64, arm64)
- macOS (x86-64, arm)

Example:
```python
from espeakng_loader import get_library_path, load_library, make_library_available

library_path = get_library_path() # Pass it to the library
# Or use load_library() for load it directly
# Or use make_library_available() for making it available for other libraries
```

Sections: espeakng-loader, Platforms, Usage, Usage with phonemizer

</details>

### easyocr

End-to-End Multi-Lingual Optical Character Recognition (OCR) Solution

`pip install easyocr` · installs (wheel) · licence: Apache License 2.0 · rank 2883 · last release 2024-09-24 · [PyPI](https://pypi.org/project/easyocr/)

<details><summary>README extract</summary>

Ready-to-use OCR with 80+ supported languages and all popular writing scripts including: Latin, Chinese, Arabic, Devanagari, Cyrillic, etc.

Try Demo on our website

Integrated into Huggingface Spaces 🤗 using Gradio. Try out the Web Demo:

- 24 September 2024 - Version 1.7.2
 - Fix several compatibilities

- Read all release notes ...

Example:
```python
import easyocr
reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
result = reader.readtext('chinese.jpg')
```

Sections: EasyOCR, What's new, What's coming next, Examples, Usage, Run on command line, Train/use your own model, Implementation Roadmap, Guideline for new language request, Github Issues, Business Inquiries

</details>

### evergreen.py

Python client for the Evergreen API

`pip install evergreen.py` · does not install on CPython 3.14 · licence: Apache Software License · rank 2959 · last release 2026-10-02 · [PyPI](https://pypi.org/project/evergreen.py/) · [source](https://github.com/evergreen-ci/evergreen.py)

<details><summary>README extract</summary>

A client library for the Evergreen API written in python. Currently supports the V2 version of
the API. For more details, see

Example:
```python
>> from evergreen.api import EvgAuth, EvergreenApi
>> api = EvergreenApi.get_api(EvgAuth('your.username', '***'))
>> project = api.project_by_id('mongodb-mongo-master')
>> project.display_name
'MongoDB (master)'
```

Sections: Evergreen.py, Description, Getting Help, What's the right channel to ask my question?, How can I request a change/report a bug in evergreen.py?, Dependencies, Usage, Documentation, Requirements, Linting/formatting, Running tests, Changes to doc site building, Automatically running checks on commit, Versioning

</details>

### envs

Easy access of environment variables from Python with support for strings, booleans, list, tuples, and dicts.

`pip install envs` · installs (wheel) · licence: Apache Software License · rank 2961 · last release 2021-12-09 · [PyPI](https://pypi.org/project/envs/)

### expecttest

(no summary)

`pip install expecttest` · installs (wheel) · licence: MIT License · rank 2991 · last release 2024-12-11 · [PyPI](https://pypi.org/project/expecttest/) · [source](https://github.com/ezyang/expecttest)

<details><summary>README extract</summary>

This library implements expect tests (also known as "golden" tests). Expect
tests are a method of writing tests where instead of hard-coding the expected
output of a test, you run the test to get the output, and the test framework
automatically populates the expected output. ...

Example:
```python
# test.py
import unittest
from expecttest import TestCase

class TestStringMethods(TestCase):
    def test_split(self):
        s = 'hello world'
        self.assertExpectedInline(str(s.split()), """""")

if name == 'main':
    unittest.main()
```

Sections: expecttest, A minimal working example, Some tips and tricks, Similar libraries

</details>

### emr-notebooks-magics

Jupyter Magics for EMR Notebooks.

`pip install emr-notebooks-magics` · installs from source (sdist only) · licence: Apache Software License · rank 3067 · last release 2023-06-30 · [PyPI](https://pypi.org/project/emr-notebooks-magics/)

<details><summary>README extract</summary>

This repository contains iPython magics that can be used in Amazon EMR Notebooks.

Sections: EMR Notebooks iPython Magics, Usage

</details>

### embreex

Python binding for Intel's Embree ray engine

`pip install embreex` · installs (wheel) · licence: not stated · rank 3353 · last release 2026-10-21 · [PyPI](https://pypi.org/project/embreex/) · [source](https://github.com/trimesh/embreex)

<details><summary>README extract</summary>

A fork of scopatz/pyembree that is configured to
build wheels for Intel Mac, Windows, and Linux for Python 3.6 and newer. The name change
is to avoid confusion with the other forks and install methods available. ...

Sections: embreeX, Alternatives

</details>

### eccodes

Python interface to the ecCodes GRIB and BUFR decoder/encoder

`pip install eccodes` · installs (wheel) · licence: Apache Software License · rank 3470 · last release 2026-10-15 · [PyPI](https://pypi.org/project/eccodes/)

<details><summary>README extract</summary>

Python 3 interface to decode and encode GRIB and BUFR files via the
ECMWF ecCodes library.

Features:

- reads and writes GRIB 1 and 2 files,
- reads and writes BUFR 3 and 4 files,
- supports all modern versions of Python and PyPy3,
- works on most *Linux* distributions and *MacOS*, the *ecCodes* C-library
 is the only system dependency, ...

Sections: Bypassing the provided binary library, Linux and MacOS, Windows, System dependencies, Debugging the library search, Usage, Experimental features, Fast bindings, Project resources, 2.47.0 (2026-04-21), 2.46.0 (2026-02-24), 2.45.0 (2025-01-16), 2.44.0 (2025-10-03), 2.43.0 (2025-07-24)

</details>

### einx

Universal Notation for Tensor Operations in Python

`pip install einx` · installs (wheel) · licence: MIT · rank 3703 · last release 2026-04-01 · [PyPI](https://pypi.org/project/einx/) · [docs](https://einx.readthedocs.io) · [source](https://github.com/fferflo/einx)

<details><summary>README extract</summary>

einx is a notation and Python library that provides a universal interface to formulate tensor operations in frameworks such as Numpy, PyTorch, Jax, Tensorflow, and MLX.

* Quickstart
* What does einx look like?
* How does the notation work?
* How are einx operations implemented?
* Which operations are supported?

Example:
```python
import einx
import numpy as np

x = np.ones((10, 20, 30)) # Create some tensor (numpy/torch/jax/tensorflow/mlx/...)

y = einx.sum("a [b] c", x) # Call an einx operation

print(y.shape)
```

Sections: einx* - Universal Notation for Tensor Operations, Quickstart, What does einx look like?, How does the notation work?, How are einx operations implemented?

</details>

### eckitlib

"eckitlib"

`pip install eckitlib` · installs (wheel) · licence: not stated · rank 3709 · last release 2026-11-06 · [PyPI](https://pypi.org/project/eckitlib/)

<details><summary>README extract</summary>

&style=flat-square&logo=github)
&style=flat-square&logo=github)

> [!IMPORTANT]
> This software is Graduated and subject to ECMWF's guidelines on
> Software Maturity.

Features:
EcKit is a cross-platform C++ toolkit that supports development of tools and
applications at ECMWF. It is based on code developed over the last 20 years
within the MARS software and was re-factored out to be reused by other
applications. ...

Sections: EcKit, Overview, Features, Requirements

</details>

### eccodeslib

"eccodeslib"

`pip install eccodeslib` · installs (wheel) · licence: not stated · rank 3720 · last release 2026-11-06 · [PyPI](https://pypi.org/project/eccodeslib/)

<details><summary>README extract</summary>

> [!IMPORTANT]
> This software is Graduated and subject to ECMWF's guidelines on Software Maturity.

ecCodes is a package developed by ECMWF which provides an application programming interface
and a set of tools for decoding and encoding messages in the following formats: ...

</details>

### ecos

This is the Python package for ECOS: Embedded Cone Solver. See Github page for more information.

`pip install ecos` · installs from source (sdist only) · licence: GPLv3 · rank 3860 · last release 2024-06-18 · [PyPI](https://pypi.org/project/ecos/)

_README extract left out: share-alike licence._

### eigenpy

Bindings between Numpy and Eigen using Boost.Python

`pip install eigenpy` · installs (wheel) · licence: BSD-2-Clause · rank 3869 · last release 2026-05-21 · [PyPI](https://pypi.org/project/eigenpy/)

<details><summary>README extract</summary>

EigenPy is an open-source framework that allows the binding of the famous Eigen C++ library in Python via Boost.Python.

EigenPy provides:

- full memory sharing between Numpy and Eigen, avoiding memory allocation
- full support Eigen::Ref avoiding memory allocation
- full support of the Eigen::Tensor module ...

Sections: Conda, Ubuntu, Add robotpkg apt repository, Mac OS X, Docker, Build

</details>

### emcee

The Python ensemble sampling toolkit for MCMC

`pip install emcee` · installs (wheel) · licence: MIT License · rank 4025 · last release 2024-04-19 · [PyPI](https://pypi.org/project/emcee/) · [source](https://github.com/dfm/emcee)

<details><summary>README extract</summary>

The Python ensemble sampling toolkit for affine-invariant MCMC

emcee is a stable, well tested Python implementation of the affine-invariant
ensemble sampler for Markov chain Monte Carlo (MCMC)
proposed by
Goodman & Weare (2010).
The code is open source and has
already been used in several published projects in the Astrophysics
literature. ...

Sections: emcee, Documentation, Attribution

</details>

### evergreen-lint

(no summary)

`pip install evergreen-lint` · installs (wheel) · licence: not stated · rank 4080 · last release 2025-06-17 · [PyPI](https://pypi.org/project/evergreen-lint/)

### edgegrid-python

{OPEN} client authentication protocol for python-requests

`pip install edgegrid-python` · installs (wheel) · licence: Apache Software License · rank 4213 · last release 2026-10-27 · [PyPI](https://pypi.org/project/edgegrid-python/)

<details><summary>README extract</summary>

This library implements an Authentication handler for HTTP requests using the Akamai EdgeGrid Authentication scheme for Python.

Example:
```python
import requests
from akamai.edgegrid import EdgeGridAuth, EdgeRc

edgerc = EdgeRc('~/.edgerc')
section = 'default'
baseurl = ' % edgerc.get(section, 'host')

session = requests.Session()
session.auth = EdgeGridAuth.from_edgerc(edgerc, section)
```

Sections: EdgeGrid for Python, Authentication, Use, Query string parameters, Headers, Body data, Debug, Virtual environment, Reporting issues

</details>

### ec2-metadata

An easy interface to query the EC2 metadata API, with caching.

`pip install ec2-metadata` · installs (wheel) · licence: MIT · rank 4332 · last release 2026-02-11 · [PyPI](https://pypi.org/project/ec2-metadata/) · [source](https://github.com/adamchainz/ec2-metadata)

<details><summary>README extract</summary>

An easy interface to query the EC2 metadata API (version 2), with caching.

A quick example:

Working on a Django project?
Improve your skills with one of my books.

Features:
`boto` came with a utility function to retrieve the instance metadata as a lazy loading dictionary, `boto.utils.get_instance_metadata`, but this has not been ported to `boto3`, as per this issue. ...

Example:
```python
>>> from ec2_metadata import ec2_metadata
>>> print(ec2_metadata.region)
us-east-1
>>> print(ec2_metadata.instance_id)
i-123456
```

...

</details>

### extruct

Extract embedded metadata from HTML markup

`pip install extruct` · installs (wheel) · licence: BSD License · rank 4451 · last release 2024-11-08 · [PyPI](https://pypi.org/project/extruct/)

<details><summary>README extract</summary>

*extruct* is a library for extracting embedded metadata from HTML markup.

Currently, *extruct* supports:

- W3C's HTML Microdata
- embedded JSON-LD
- Microformat via mf2py
- Facebook's Open Graph
- (experimental) RDFa via rdflib
- Dublin Core Metadata (DC-HTML-2003) ...

Example:
```python
>>> import extruct
>>> import requests
>>> import pprint
>>> from w3lib.html import get_base_url
>>>
>>> pp = pprint.PrettyPrinter(indent=2)
>>> r = requests.get('
>>> base_url = get_base_url(r.text, r.url)
>>> data = extruct.extract(r.text, base_url=base_url)
>>>
>>> pp.pprint(data)
{ 'dublincore': [ { 'elements': [ { 'URI': '
...
```

...

</details>

### etuples

Python S-expression emulation using tuple-like objects.

`pip install etuples` · installs (wheel) · licence: Apache-2.0 · rank 4468 · last release 2025-07-14 · [PyPI](https://pypi.org/project/etuples/) · [source](http://github.com/pythological/etuples)

<details><summary>README extract</summary>

Python S-expression emulation using tuple-like objects.

Example:
```python
>>> from operator import add
>>> from etuples import etuple, etuplize

>>> et = etuple(add, 1, 2)
>>> et
ExpressionTuple((<built-in function add>, 1, 2))

>>> from IPython.lib.pretty import pprint
>>> pprint(et)
e(<function _operator.add(a, b, /)>, 1, 2)

>>> et[0:2]
ExpressionTuple((<built-in function add>, 1))
```

Sections: `etuples`, Examples

</details>

### evidently

Open-source tools to analyze, monitor, and debug machine learning model in production.

`pip install evidently` · installs (wheel) · licence: Apache Software License · rank 4687 · last release 2026-09-11 · [PyPI](https://pypi.org/project/evidently/)

<details><summary>README extract</summary>

An open-source framework to evaluate, test and monitor ML and LLM-powered systems.

 Documentation
 API Reference
 Discord Community
 Blog
 Twitter
 Evidently Cloud

Evidently is an open-source Python library to evaluate, test, and monitor ML and LLM systems—from experiments to production.

* 🔡 Works with tabular and text data. ...

Example:
```python
import pandas as pd
from evidently import Report
from evidently import Dataset, DataDefinition
from evidently.descriptors import Sentiment, TextLength, Contains
from evidently.presets import TextEvals
```

...

</details>

### e2b-dockerfile-utils

E2B Dockerfile utils - Dockerfile parser, shell lexer and .dockerignore matcher ported from BuildKit and Moby

`pip install e2b-dockerfile-utils` · installs (wheel) · licence: Apache-2.0 · rank 4742 · last release 2026-10-13 · [PyPI](https://pypi.org/project/e2b-dockerfile-utils/) · [source](https://github.com/e2b-dev/e2b/tree/main/packages/dockerfile-utils-python)

<details><summary>README extract</summary>

Dockerfile parser and shell lexer ported from BuildKit and a `.dockerignore` matcher ported from moby/patternmatcher, with no runtime dependencies. Used by the E2B SDK to implement `Template.from_dockerfile` and to filter the build context. ...

Example:
```python
from e2b_dockerfile_utils import ShellLex, parse_dockerfile_ast

ast = parse_dockerfile_ast(
    """
FROM node:24 AS build
ENV KEY="a  b" OTHER=c
RUN <<EOF
npm ci
npm run build
EOF
"""
)

for instruction in ast.instructions:
    print(instruction.name, instruction.flags, instruction.args)

lex = ShellLex(ast.escape_token)
...
```

</details>

### exit-codes

Platform-independent exit codes.

`pip install exit-codes` · installs (wheel) · licence: MIT · rank 4817 · last release 2019-07-09 · [PyPI](https://pypi.org/project/exit-codes/)

<details><summary>README extract</summary>

Platform-independent exit codes.

Python provides standard exit status codes for some platforms, but not all. This
is technically, pedantically correct, but it makes it awkward to provide
practical cross-platform exit statuses. This package takes the exit status codes
defined in `os` for Unixes and make them available to the unwashed masses. ...

Example:
```python
from exit_codes import ExitCode

def main():
    if big_operation():
        # If your program exits normally, return OK
        return ExitCode.OK
    else:
        # Otherwise, return the appropriate error code
        return ExitCode.IO_ERR
```

</details>

### einshape

DSL-based reshaping library for JAX and other frameworks

`pip install einshape` · installs (wheel) · licence: Apache 2.0 · rank 4950 · last release 2022-12-19 · [PyPI](https://pypi.org/project/einshape/)

### e3nn

Equivariant convolutional neural networks for the group E(3) of 3 dimensional rotations, translations, and mirrors.

`pip install e3nn` · installs (wheel) · licence: MIT License · rank 5040 · last release 2026-02-13 · [PyPI](https://pypi.org/project/e3nn/) · [docs](https://docs.e3nn.org/) · [source](https://github.com/e3nn/e3nn.git)

<details><summary>README extract</summary>

Documentation | Code | CHANGELOG | Colab

The aim of this library is to help the development of E(3) equivariant neural networks.
It contains fundamental mathematical operations such as tensor products and spherical harmonics.

Example:
```python
import torch
from e3nn import o3

# Create a random array made of scalar (0e) and a vector (1o)
irreps_in = o3.Irreps("0e + 1o")
x = irreps_in.randn(-1)

# Apply a linear layer
irreps_out = o3.Irreps("2x0e + 2x1o")
linear = o3.Linear(irreps_in=irreps_in, irreps_out=irreps_out)
y = linear(x)

# Compute a tensor product with itself
...
```

Sections: Euclidean neural networks, Breaking changes, Help, Want to get involved? Great!, Citing, Euclidean Neural Networks, e3nn, Copyright

</details>

### exponent-server-sdk

Expo Server SDK for Python

`pip install exponent-server-sdk` · installs (wheel) · licence: MIT · rank 5277 · last release 2025-07-03 · [PyPI](https://pypi.org/project/exponent-server-sdk/)

<details><summary>README extract</summary>

This repo is maintained by Expo's awesome community :heart_eyes:! So, if you have problems with the code in this repository, please feel free to open an issue, and make a PR. Thanks!

Example:
```python
from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)
import os
import requests
from requests.exceptions import ConnectionError, HTTPError

# Optionally providing an access token within a session if you have enabled push security
session = requests.Session()
...
```

Sections: exponent-server-sdk-python, Usage

</details>

### eventkit

Event-driven data pipelines

`pip install eventkit` · installs (wheel) · licence: BSD License · rank 5392 · last release 2023-12-11 · [PyPI](https://pypi.org/project/eventkit/)

<details><summary>README extract</summary>

|Build| |PyVersion| |Status| |PyPiVersion| |License| |Docs|

Introduction

The primary use cases of eventkit are

* to send events between loosely coupled components;
* to compose all kinds of event-driven data pipelines.

The interface is kept as Pythonic as possible,
with familiar names from Python and its libraries where possible. ...

</details>

### envoy_data_plane

Python dataclasses for the Envoy Data-Plane-API

`pip install envoy_data_plane` · installs (wheel) · licence: MIT · rank 5421 · last release 2026-07-21 · [PyPI](https://pypi.org/project/envoy_data_plane/)

<details><summary>README extract</summary>

A conversion of envoyproxy/data-plane-api protocol buffers into Python dataclasses using betterproto

Sections: envoy_data_plane, Intended usage, Examples

</details>

### EasyProcess

Easy to use Python subprocess interface.

`pip install EasyProcess` · installs (wheel) · licence: BSD License · rank 5431 · last release 2022-01-15 · [PyPI](https://pypi.org/project/EasyProcess/)

<details><summary>README extract</summary>

Easy to use Python subprocess interface.

Documentation:

</details>

### elasticsearch8

Python client for Elasticsearch

`pip install elasticsearch8` · installs (wheel) · licence: Apache-2.0 · rank 5465 · last release 2025-12-23 · [PyPI](https://pypi.org/project/elasticsearch8/) · [docs](https://elasticsearch8-py.readthedocs.io/) · [source](https://github.com/elastic/elasticsearch8-py)

<details><summary>README extract</summary>

*The official Python client for Elasticsearch.*

Features:
* Translating basic Python data types to and from JSON
* Configurable automatic discovery of cluster nodes
* Persistent connections
* Load balancing (with pluggable selection strategy) across available nodes
* Failed connection penalization (time ...

Sections: Elasticsearch Python Client, Features, Connecting, Usage, Compatibility, Documentation, Feedback 🗣️

</details>

### e2b-desktop

E2B Desktop Sandbox - Desktop sandbox in cloud powered by E2B

`pip install e2b-desktop` · installs (wheel) · licence: MIT · rank 5650 · last release 2026-10-22 · [PyPI](https://pypi.org/project/e2b-desktop/) · [source](https://github.com/e2b-dev/e2b/tree/main/packages/desktop-python)

<details><summary>README extract</summary>

E2B Desktop Sandbox is a secure virtual desktop ready for Computer Use. Powered by E2B.

Each sandbox is isolated from the others and can be customized with any dependencies you want.

Source: packages/desktop-python

Example:
```python
from e2b_desktop import Sandbox

# Create a new desktop sandbox
desktop = Sandbox.create()

# Launch an application
desktop.launch('google-chrome')  # or vscode, firefox, etc.

# Wait 10s for the application to open
desktop.wait(10000)

# Stream the application's window
# Note: There can be only one stream at a time
...
```

...

</details>

### elasticsearch-dbapi

A DBAPI and SQLAlchemy dialect for Elasticsearch

`pip install elasticsearch-dbapi` · installs (wheel) · licence: Apache License, Version 2.0 · rank 5683 · last release 2026-10-06 · [PyPI](https://pypi.org/project/elasticsearch-dbapi/)

<details><summary>README extract</summary>

`elasticsearch-dbapi` Implements a DBAPI (PEP-249) and SQLAlchemy dialect,
that enables SQL access on elasticsearch clusters for query only access.

On Elastic Elasticsearch:
Uses Elastic X-Pack SQL API

On OpenSearch (AWS ES):
OpenSearch SQL

This library supports Elasticsearch 7.x, Elasticsearch 8.x (via compatibility mode), and OpenSearch 2.x. ...

Example:
```python
from es.elastic.api import connect

conn = connect(host='localhost')
curs = conn.cursor()
curs.execute(
    "select * from flights LIMIT 10"
)
print([row for row in curs])
```

...

</details>

### ephemeral-port-reserve

Bind to an ephemeral port, force it into the TIME_WAIT state, and unbind it.

`pip install ephemeral-port-reserve` · installs (wheel) · licence: MIT License · rank 6158 · last release 2021-02-11 · [PyPI](https://pypi.org/project/ephemeral-port-reserve/)

<details><summary>README extract</summary>

Sometimes you need a networked program to bind to a port that can't be hard-coded.
Generally this is when you want to run several of them in parallel; if they all
bind to port 8080, only one of them can succeed.

The usual solution is the "port 0 trick". ...

</details>

### econml

This package contains several methods for calculating Conditional Average Treatment Effects

`pip install econml` · installs (wheel) · licence: MIT · rank 6521 · last release 2026-07-31 · [PyPI](https://pypi.org/project/econml/) · [docs](https://www.pywhy.org/EconML/) · [source](https://github.com/py-why/EconML)

<details><summary>README extract</summary>

EconML: A Python Package for ML-Based Heterogeneous Treatment Effects Estimation

EconML is a Python package for estimating heterogeneous treatment effects from observational data via machine learning. ...

Example:
```python
from econml.dml import LinearDML
from sklearn.linear_model import LassoCV
from econml.inference import BootstrapInference

est = LinearDML(model_y=LassoCV(), model_t=LassoCV())
### Estimate with OLS confidence intervals
est.fit(Y, T, X=X, W=W) # W -> high-dimensional confounders, X -> features
treatment_effects = est.effect(X_test)
...
```

...

</details>

### extra-streamlit-components

An all-in-one place, to find complex or just natively unavailable components on streamlit.

`pip install extra-streamlit-components` · installs (wheel) · licence: MIT License · rank 6663 · last release 2025-08-17 · [PyPI](https://pypi.org/project/extra-streamlit-components/)

<details><summary>README extract</summary>

An all-in-one place, to find complex or just not available components by default on streamlit.

_Explained in details in my book Web Application Development with Streamlit

Firstly, add `import extra_streamlit_components as stx`

- ### Router
- Route to specific pages in Streamlit. ...

Example:
```python
@st.cache_resource(hash_funcs={"_thread.RLock": lambda _: None})
def init_router():
    return stx.Router({"/home": home, "/landing": landing})

def home():
    return st.write("This is a home page")

def landing():
    return st.write("This is the landing page")

router = init_router()
router.show_route_view()

c1, c2, c3 = st.columns(3)

...
```

Sections: Extra-Streamlit-Components, Components

</details>

### executable-application

An example of an executable application.

`pip install executable-application` · installs (wheel) · licence: not stated · rank 6786 · last release 2025-01-17 · [PyPI](https://pypi.org/project/executable-application/)

<details><summary>README extract</summary>

An example of an executable application, used for testing in uv.

</details>

### email-to

Simplyify sending HTML emails

`pip install email-to` · installs (wheel) · licence: MIT License · rank 6951 · last release 2017-10-01 · [PyPI](https://pypi.org/project/email-to/)

<details><summary>README extract</summary>

Simplyify sending HTML emails

* Free software: MIT license

Judgement rendered by:

Features:
The built in Python modules for sending email are powerful, but require a lot of
boilerplate to write an HTML formatted email.

With `email_to` sending a simple email becomes much more succint. ...

Example:
```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart('alternative')
message['Subject'] = 'Test'
message['From'] = 'user@gmail.com'
message['To'] = 'someone@else.com'

message.attach(MIMEText('# A Heading\nSomething else in the body', 'plain')
...
```

Sections: Email To, Features, 0.1.0 (2017-09-27)

</details>

### editdistpy

Fast Levenshtein and Damerau optimal string alignment algorithms.

`pip install editdistpy` · installs (wheel) · licence: MIT · rank 7059 · last release 2026-11-02 · [PyPI](https://pypi.org/project/editdistpy/) · [source](https://github.com/mammothb/editdistpy)

<details><summary>README extract</summary>

editdistpy

========

editdistpy is a fast implementation of the Levenshtein edit distance and
the Damerau-Levenshtein optimal string alignment (OSA) edit distance
algorithms. The original C# project can be found at SoftWx.Match.

Example:
```python
import sys

from editdistpy import levenshtein

string_1 = "flintstone"
string_2 = "hanson"

max_distance = 2
print(levenshtein.distance(string_1, string_2, max_distance))
# expected output: -1

max_distance = sys.maxsize
print(levenshtein.distance(string_1, string_2, max_distance))
# expected output: 6
```

Sections: Usage, Levenshtein, Damerau-Levenshtein OSA, Benchmark, Single word (completely different), Single word (similar), Single word (identical ending), Short string, Long string

</details>

### e3nn-jax

Equivariant convolutional neural networks for the group E(3) of 3 dimensional rotations, translations, and mirrors.

`pip install e3nn-jax` · installs (wheel) · licence: not stated · rank 7072 · last release 2026-04-01 · [PyPI](https://pypi.org/project/e3nn-jax/) · [docs](https://e3nn-jax.readthedocs.io) · [source](https://github.com/e3nn/e3nn-jax)

<details><summary>README extract</summary>

Example:
```python
import e3nn_jax as e3nn

# Create a random array made of a scalar (0e) and a vector (1o)
array = e3nn.normal("0e + 1o", jax.random.PRNGKey(0))

print(array)
# 1x0e+1x1o [ 1.8160863  -0.75488514  0.33988908 -0.53483534]

# Compute the norms
norms = e3nn.norm(array)
print(norms)
# 1x0e+1x0e [1.8160863  0.98560894]

...
```

Sections: e3nn-jax, Documentation, rocket: 44% faster than pytorch, Need Help?, What is different from the PyTorch version?, Citing

</details>

### entrypoint2

easy to use command-line interface for python modules

`pip install entrypoint2` · installs (wheel) · licence: BSD License · rank 7374 · last release 2022-06-11 · [PyPI](https://pypi.org/project/entrypoint2/)

<details><summary>README extract</summary>

easy to use command-line interface for Python modules

home:

</details>

### emmet-core

Core Emmet Library

`pip install emmet-core` · installs (wheel) · licence: BSD-3-Clause-LBNL · rank 7426 · last release 2026-10-22 · [PyPI](https://pypi.org/project/emmet-core/) · [docs](https://materialsproject.github.io/emmet/)

### edk2-pytool-library

Python library supporting UEFI EDK2 firmware development

`pip install edk2-pytool-library` · installs (wheel) · licence: not stated · rank 7661 · last release 2026-09-17 · [PyPI](https://pypi.org/project/edk2-pytool-library/) · [docs](https://www.tianocore.org/edk2-pytool-library/)

<details><summary>README extract</summary>

[![pypi]][_pypi]
[![codecov]][_codecov]
[![ci]][_ci]
[![docs]][_docs]

This is a Tianocore maintained project consisting of a python library supporting
UEFI firmware development. This package's intent is to provide an easy way to
organize and share python code to facilitate reuse across environments, tools,
and scripts. ...

Example:
```python
from edk2toollib.<module> import <class>
```

Sections: Tianocore Edk2 PyTool Library (edk2toollib), Content, Usage, Documentation, Users and Consumers

</details>

### encord

Encord Python SDK Client

`pip install encord` · installs (wheel) · licence: Apache Software License · rank 7746 · last release 2026-10-28 · [PyPI](https://pypi.org/project/encord/) · [docs](https://docs.encord.com/sdk-documentation/getting-started-sdk/sdk-intro) · [source](https://github.com/encord-team/encord-client-python)

<details><summary>README extract</summary>

- Minimal low-level Python client that allows you to interact with Encord's API
- Supports Python: `3.9`, `3.10`, `3.11`, `3.12`, `3.13` and `3.14`

Example:
```python
# Import dependencies
from encord import EncordUserClient

# Authenticate with Encord using the path to your private key.  Replace  with the path to your private key.
user_client = EncordUserClient.create_with_ssh_private_key(
  ssh_private_key_path=""
)
```

Sections: Encord Python API Client, 💻 Features, ✨ Relevant Links, 💡 Getting Started, 🐛 Troubleshooting

</details>

### eppo-server-sdk

Eppo SDK for Python

`pip install eppo-server-sdk` · installs (wheel) · licence: MIT License · rank 7826 · last release 2026-01-07 · [PyPI](https://pypi.org/project/eppo-server-sdk/)

<details><summary>README extract</summary>

Eppo is a modular flagging and experimentation analysis tool. Eppo's Python SDK is built to make assignments in multi-user server side contexts. Before proceeding you'll need an Eppo account.

Features:
- Feature gates
- Kill switches
- Progressive rollouts
- A/B/n experiments
- Mutually exclusive experiments (Layers)
- Holdouts
- Contextual multi-armed bandits
- Dynamic configuration

Example:
```python
import eppo_client
from eppo_client import Config, AssignmentLogger

client_config = Config(
    api_key="<SDK-KEY-FROM-DASHBOARD>", assignment_logger=AssignmentLogger()
)
eppo_client.init(client_config)
```

Sections: Eppo Python SDK, Features, Quick start, Initialize once, Assign anywhere, Assignment functions, Initialization options, Assignment logger, Export configuration, Philosophy

</details>

### edk2-pytool-extensions

Python tools supporting UEFI EDK2 firmware development

`pip install edk2-pytool-extensions` · installs (wheel) · licence: not stated · rank 7910 · last release 2026-10-16 · [PyPI](https://pypi.org/project/edk2-pytool-extensions/) · [docs](https://www.tianocore.org/edk2-pytool-extensions/)

<details><summary>README extract</summary>

[![pypi]][_pypi]
[![codecov]][_codecov]
[![ci]][_ci]
[![docs]][_docs]

Getting Started? Check out our documentation at

This is a Tianocore maintained project consisting of command line and other
python tools and extensions for building and maintaining an Edk2 based UEFI
firmware code tree. ...

Example:
```python
from edk2toolext.<module> import <class>
```

Sections: Tianocore Edk2 PyTool Extensions (edk2toolext), Content, Usage, Documentation

</details>

### emrvalidator

A Data Validation Tool for Healthcare Data

`pip install emrvalidator` · installs (wheel) · licence: MIT · rank 7946 · last release 2026-01-26 · [PyPI](https://pypi.org/project/emrvalidator/)

<details><summary>README extract</summary>

A modern, healthcare-focused data quality and validation library

EMRValidator is a Python library designed as a cleaner, faster, and more intuitive alternative to Great Expectations, with specialized features for Electronic Medical Records (EMR) and healthcare data validation. ...

Example:
```python
from emrvalidator import DataValidator
import pandas as pd

# Load your data
df = pd.read_csv('patient_data.csv')

# Create validator and run validations
validator = DataValidator("Patient Data Quality Check")
validator.load_data(df)

# Chain validation rules
(validator
    .expect_column_exists('mrn')
...
```

...

</details>

### edlib

Lightweight, super fast library for sequence alignment using edit (Levenshtein) distance.

`pip install edlib` · installs from source (sdist only) · licence: MIT · rank 8048 · last release 2024-09-04 · [PyPI](https://pypi.org/project/edlib/)

<details><summary>README extract</summary>

Lightweight, super fast library for sequence alignment using edit (Levenshtein) distance.

Popular use cases: aligning DNA sequences, calculating word/text similarity.

Edlib is actually a C/C++ library, and this package is it's wrapper for Python. ...

Features:
* Calculates edit distance.
* It can find optimal alignment path (instructions how to transform first sequence into the second sequence). ...

Example:
```python
import edlib

edlib.align("ACTG", "CACTRT", mode="HW", task="path")
# {'editDistance': 1, 'alphabetLength': 5, 'locations': [(1, 3), (1, 4)], 'cigar': '3=1I'}

# You can provide additional equalities.
edlib.align("ACTG", "CACTRT", mode="HW", task="path", additionalEqualities=[("R", "A"), ("R", "G")])
...
```

...

</details>

### exactextract

Fast and accurate raster zonal statistics

`pip install exactextract` · installs (wheel) · licence: not stated · rank 8133 · last release 2025-12-01 · [PyPI](https://pypi.org/project/exactextract/) · [docs](https://isciences.github.io/exactextract/) · [source](https://github.com/isciences/exactextract)

<details><summary>README extract</summary>

`exactextract` provides a fast and accurate algorithm for summarizing values in the portion of a raster dataset that is covered by a polygon, often referred to as zonal statistics. Implemented in C++, it is available through a command line interface as well as packages for Python and R. More information is available in the project documentation.

</details>

### elasticsearch-curator

Tending your Elasticsearch indices and snapshots

`pip install elasticsearch-curator` · installs (wheel) · licence: Apache Software License · rank 8212 · last release 2025-10-03 · [PyPI](https://pypi.org/project/elasticsearch-curator/)

<details><summary>README extract</summary>

Have indices in Elasticsearch? This is the tool for you!

Like a museum curator manages the exhibits and collections on display,
Elasticsearch Curator helps you curate, or manage your indices.

Curator is breaking into version dependent releases. ...

Sections: Curator, ANNOUNCEMENT, New Client Configuration, Action File Configuration

</details>

### eth-bloom

A python implementation of the bloom filter used by Ethereum

`pip install eth-bloom` · installs (wheel) · licence: MIT · rank 8429 · last release 2026-08-22 · [PyPI](https://pypi.org/project/eth-bloom/) · [source](https://github.com/ApeWorX/eth-bloom.git)

<details><summary>README extract</summary>

A python implementation of the bloom filter used by Ethereum.

> This library and repository was previously located at It was transferred to the Ethereum foundation github in November 2017 and renamed to `eth-bloom`. The PyPI package was also renamed from `ethereum-bloom` to `eth-bloom`.

Read more in the documentation below. View the change log. ...

Example:
```python
>>> from eth_bloom import BloomFilter
>>> b = BloomFilter()
>>> b'a value' in b  # check whether a value is present
False
>>> b.add(b'a value')  # add a single value
>>> b'a value' in b
True
>>> int(b)  # cast to an integer
...
```

Sections: eth-bloom, Usage, Checks

</details>

### ecmwf-opendata

A package to download ECMWF open data

`pip install ecmwf-opendata` · installs (wheel) · licence: Apache Software License · rank 8440 · last release 2026-10-16 · [PyPI](https://pypi.org/project/ecmwf-opendata/)

<details><summary>README extract</summary>

`ecmwf-opendata` is a package to simplify the download of ECMWF open data. It implements a request-based interface to the dataset using ECMWF's MARS language to select meteorological fields, similar to the existing ecmwf-api-client Python package.

A collection of Jupyter Notebooks that make use of that package is available here.

Example:
```python
or directly as arguments to the `retrieve()` method:
```

Sections: ecmwf-opendata, or

</details>

### efficientnet-pytorch

EfficientNet implemented in PyTorch.

`pip install efficientnet-pytorch` · installs from source (sdist only) · licence: Apache Software License · rank 8457 · last release 2021-04-15 · [PyPI](https://pypi.org/project/efficientnet-pytorch/)

<details><summary>README extract</summary>

Features:
This repository contains an op-for-op PyTorch reimplementation of EfficientNet, along with pre-trained models and examples.

The goal of this implementation is to be simple, highly extensible, and easy to integrate into your own projects. ...

Example:
```python
from efficientnet_pytorch import EfficientNet
model = EfficientNet.from_pretrained('efficientnet-b0')
```

Sections: EfficientNet PyTorch, Quickstart, Updates, Update (April 2, 2021), Update (Aug 25, 2020), Update (May 14, 2020), Update (January 23, 2020), Update (October 15, 2019), Update (October 12, 2019), Update (July 31, 2019), Update (June 29, 2019), Update (June 23, 2019), Overview, About EfficientNet

</details>

### essentials

General purpose classes and functions

`pip install essentials` · installs (wheel) · licence: MIT License · rank 8478 · last release 2025-11-23 · [PyPI](https://pypi.org/project/essentials/)

<details><summary>README extract</summary>

Core classes and functions, reusable in any kind of Python application.

Features:
* exception classes to express common scenarios
* friendly JSON encoder, handling `datetime`, `date`, `time`, `UUID`, `bytes`, built-in enums, and instances of classes implementing a `dict()` method, like pydantic BaseModel
* utilities to work with `folders` and ...

Sections: Essentials, Documentation

</details>

### essentials-openapi

Classes to generate OpenAPI Documentation v3 and v2, in JSON and YAML.

`pip install essentials-openapi` · installs (wheel) · licence: MIT License · rank 8516 · last release 2026-03-07 · [PyPI](https://pypi.org/project/essentials-openapi/)

<details><summary>README extract</summary>

Classes to generate OpenAPI Documentation
v3 and v2, in JSON and YAML, and to generate other kinds of documents from
OpenAPI Documentation files.

To install with dependencies to generate other kinds of artifacts from source
OpenAPI Documentation files:

Features:
These require the full package: install it using `pip install essentials-openapi[full]`.

To generate output for MkDocs and PyMdown extentions:

_Example of MkDocs documentation generated using Neoteroi/mkdocs-plugins._ ...

Sections: essentials-openapi, Useful links, Usage, Features to generate artifacts from Open API Documentation, Using custom templates, Goals, Non-Goals, Limitations, Styles

</details>

### escapism

Simple, generic API for escaping strings.

`pip install escapism` · installs (wheel) · licence: MIT · rank 8537 · last release 2025-12-11 · [PyPI](https://pypi.org/project/escapism/) · [source](https://github.com/jupyterhub/escapism)

<details><summary>README extract</summary>

Simple escaping of text, given a set of safe characters and an escape character.

Example:
```python
escaped = escapism.escape('string to escape')
# 'string_20to_20escape'
original = escapism.unescape(escaped)
```

Sections: Escapism, Usage, Slugs

</details>

### evtx

(no summary)

`pip install evtx` · installs (wheel) · licence: MIT License · rank 8707 · last release 2026-11-01 · [PyPI](https://pypi.org/project/evtx/)

### emot

Emoji and Emoticons detection package for Python

`pip install emot` · installs (wheel) · licence: GNU GENERAL PUBLIC LICENSE · rank 8898 · last release 2021-08-02 · [PyPI](https://pypi.org/project/emot/)

_README extract left out: share-alike licence._

### ecs-deploy

Powerful CLI tool to simplify Amazon ECS deployments, rollbacks & scaling

`pip install ecs-deploy` · installs (wheel) · licence: BSD-3-Clause · rank 9035 · last release 2026-08-17 · [PyPI](https://pypi.org/project/ecs-deploy/)

<details><summary>README extract</summary>

`ecs-deploy` simplifies deployments on Amazon ECS by providing a convenience CLI tool for complex actions, which are executed pretty often.

Features:
- support for complex task definitions (e.g. multiple containers & task role)
- easily redeploy the current task definition (including `docker pull` of eventually updated images) ...

Sections: ECS Deploy, Key Features, TL;DR, Run via Docker, Configuration, AWS IAM, Actions, deploy, scale, run, update, cron (scheduled task), Usage, Examples

</details>

### eth-retry

Provides a decorator that automatically catches known transient exceptions that are common in the Ethereum/EVM ecosystem and reattempts to evaluate your decorated function

`pip install eth-retry` · installs (wheel) · licence: MIT License · rank 9230 · last release 2026-08-09 · [PyPI](https://pypi.org/project/eth-retry/) · [docs](https://github.com/BobTheBuidler/eth_retry) · [source](https://github.com/BobTheBuidler/eth_retry)

<details><summary>README extract</summary>

> Stop transient errors from wasting your time!

`eth_retry` is a Python library that provides one decorator, `eth_retry.auto_retry`.

`auto_retry` will automatically catch known transient exceptions that are common in the Ethereum/EVM ecosystem and will reattempt to evaluate your decorated function up to `os.environ['MAX_RETRIES']` (default: 10) ...

Example:
```python
import eth_retry

@eth_retry.auto_retry
def some_function_that_errors_sometimes():
    i = 0
    am = 1
    doing = 2
    stuff = 3
    return stuff

error_free_result = some_function_that_errors_sometimes()
```

Sections: eth_retry, Usage, Environment

</details>

### expiring-dict

Python dict with TTL support for auto-expiring caches

`pip install expiring-dict` · installs (wheel) · licence: MIT License · rank 9405 · last release 2025-02-28 · [PyPI](https://pypi.org/project/expiring-dict/)

<details><summary>README extract</summary>

Python dict with TTL support for auto-expiring caches

Example:
```python
from time import sleep
from expiring_dict import ExpiringDict

cache = ExpiringDict(1)  # Keys will exist for 1 second

cache["abc123"] = "some value"
assert "abc123" in cache
sleep(1)
assert "abc123" not in cache
```

Sections: py-expiring-dict, Usage, Class Level TTL, Key Level TTL

</details>

### extras

Useful extra bits for Python - things that shold be in the standard library

`pip install extras` · installs (wheel) · licence: MIT License · rank 9435 · last release 2016-05-18 · [PyPI](https://pypi.org/project/extras/)

<details><summary>README extract</summary>

extras is a set of extensions to the Python standard library, originally
written to make the code within testtools cleaner, but now split out for
general use outside of a testing context.

pydoc extras is your friend. extras currently contains the following functions:

* try_import

* try_imports

* safe_hasattr

Which do what their name suggests.

Sections: extras, Documentation, Licensing, Required Dependencies, Bug reports and patches, Thanks

</details>

### exitstatus

POSIX exit status codes

`pip install exitstatus` · installs (wheel) · licence: MIT · rank 9488 · last release 2026-11-04 · [PyPI](https://pypi.org/project/exitstatus/) · [source](https://github.com/johnthagen/exitstatus)

<details><summary>README extract</summary>

Example:
```python
import sys
from exitstatus import ExitStatus

sys.exit(ExitStatus.success)
```

</details>

### eks-token

EKS Token package, an alternate to "aws eks get-token ..." CLI

`pip install eks-token` · installs (wheel) · licence: not stated · rank 9538 · last release 2025-01-03 · [PyPI](https://pypi.org/project/eks-token/)

<details><summary>README extract</summary>

EKS Token package, an alternate to "aws eks get-token ..." CLI

Example:
```python
from eks_token import get_token
from pprint import pprint

response = get_token(cluster_name='<value>')
pprint(response)
```

Sections: eks-token, Usage, Basic usage, Extract token from response, Get Token signed for particular IAM role, Custom region

</details>

### esdk-obs-python

OBS Python SDK

`pip install esdk-obs-python` · installs from source (sdist only) · licence: Apache-2.0 · rank 9720 · last release 2026-07-12 · [PyPI](https://pypi.org/project/esdk-obs-python/)

### EWMHlib

Extended Window Manager Hints implementation in Python 3

`pip install EWMHlib` · installs (wheel) · licence: BSD License · rank 9788 · last release 2024-04-17 · [PyPI](https://pypi.org/project/EWMHlib/)

<details><summary>README extract</summary>

Extended Window Manager Hints implementation in Python 3 and python-xlib, which allows to easily query and control
Window Managers following these standards.

It also adds some additional, useful features like managing hints and handling events.

For more information, refer to official documentation at: ...

Sections: EWMH-lib, EwmhRoot: Root queries, changes and messages, EwmhWindow: Window queries, changes and messages, General variables, Display functions, Properties and Messages functions, Properties, atoms and hints values, Data Structs, USING THIS CODE, TEST

</details>

### english-words

Generate sets of english words by combining different word lists

`pip install english-words` · installs (wheel) · licence: MIT License · rank 9841 · last release 2025-08-14 · [PyPI](https://pypi.org/project/english-words/)

<details><summary>README extract</summary>

Returns sets of English words created by combining different words
lists together. Example usage: to get a set of English words from the
"web2" word list, including only lower-case letters, you write the
following:

Example:
```python
>>> from english_words import get_english_words_set
>>> web2lowerset = get_english_words_set(['web2'], lower=True)
```

Sections: english-words-py, Usage, Word lists, Adding additional word lists

</details>

### eth-tester

eth-tester: Tools for testing Ethereum applications.

`pip install eth-tester` · installs (wheel) · licence: MIT · rank 9922 · last release 2026-08-23 · [PyPI](https://pypi.org/project/eth-tester/) · [source](https://github.com/ApeWorX/eth-tester.git)

<details><summary>README extract</summary>

Tools for testing Ethereum applications

Read more in the documentation below.

View the change log.

Example:
```python
>>> from eth_tester import EthereumTester
>>> t = EthereumTester()
>>> t.get_accounts()
('0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
 '0x2B5AD5c4795c026514f8317c7a215E218DcCD6cF',
 '0x6813Eb9362372EEF6200f3b1dbC3f819671cBA69',
 '0x1efF47bc3a10a45D4B230B5d10E37751FE6AA718',
 '0xe1AB8145F7E55DC933d51a18c793F901A3A0b276',
...
```

Sections: eth-tester, Quick Start, Documentation, Input and output data formats, Block Numbers, `eth_tester.EthereumTester`, API, Instantiation, Fork Rules, Time Travel, `EthereumTester.time_travel(timestamp)`, Mining, `EthereumTester.mine_block(coinbase=ZERO_ADDRESS)`, Auto-mining transactions

</details>

### embit

A minimal bitcoin library for MicroPython and Python3 with a focus on embedded systems.

`pip install embit` · installs from source (sdist only) · licence: MIT License · rank 9933 · last release 2024-05-30 · [PyPI](https://pypi.org/project/embit/)

<details><summary>README extract</summary>

A minimal bitcoin library for MicroPython and Python3 with a focus on embedded systems.

Should remain minimal to fit in a microcontroller. Also easy to audit.

Examples can be found in `examples/` folder.

Documentation:

Support the project: `bc1qd4flfrxjctls9ya244u39hd67pcprhvka723gv` ...

Example:
```python
spanish_wordlist = [
    "ábaco",
    "abdomen",
    "abeja",
    "abierto",
    "abogado",
    "abono",
    "aborto",
    "abrazo",
    "abrir",
    "abuelo",
    ...
]

mnemonic_is_valid(mnemonic, wordlist=spanish_wordlist)
mnemonic_to_seed(mnemonic, wordlist=spanish_wordlist)
mnemonic_to_bytes(mnemonic, wordlist=spanish_wordlist)
...
```

Sections: embit, Requirements, MicroPython, Python 3, Using non-English BIP39 wordlists

</details>

### ecoji

Encode and decode data as emojis.

`pip install ecoji` · installs from source (sdist only) · licence: Apache · rank 9968 · last release 2024-07-13 · [PyPI](https://pypi.org/project/ecoji/)

<details><summary>README extract</summary>

A Python3 implemention of Ecoji. Ecoji encodes data as 1024 emojis, its base1024 with an emoji character set. Give Ecoji a try at ecoji.io.

Example:
```python
>>> import io
>>> from ecoji import encode
>>> r = io.BytesIO(b'hello')
>>> w = io.StringIO()
>>> encode(r, w)
>>> print(w.getvalue())
👲🔩🚗🌷
```

Sections: Ecoji-py 🏣🔉🦐🔼🍽🚃🔓☕, For CLI usage, For python lib

</details>

### etcd3

Python client for the etcd3 API

`pip install etcd3` · installs from source (sdist only) · licence: Apache Software License · rank 10192 · last release 2020-03-31 · [PyPI](https://pypi.org/project/etcd3/)

<details><summary>README extract</summary>

Python client for the etcd API v3, supported under python 2.7, 3.4 and 3.5.

Warning: the API is mostly stable, but may change in the future

If you're interested in using this library, please get involved.

* Free software: Apache Software License 2.0

Basic usage:

Example:
```python
import etcd3

etcd = etcd3.client()

etcd.get('foo')
etcd.put('bar', 'doot')
etcd.delete('bar')

# locks
lock = etcd.lock('thing')
lock.acquire()
# do something
lock.release()

with etcd.lock('doot-machine') as lock:
    # do something

# transactions
etcd.transaction(
    compare=[
        etcd.transactions.value('/doot/testing') == 'doot',
...
```

Sections: python-etcd3, 0.1.0 (2016-09-30)

</details>

### egl-probe

(no summary)

`pip install egl-probe` · installs from source (sdist only) · licence: not stated · rank 10314 · last release 2021-07-16 · [PyPI](https://pypi.org/project/egl-probe/)

<details><summary>README extract</summary>

Author: Fei Xia (feixia@stanford.edu)

Adapted from (

Sections: egl_probe, Example output

</details>

### evmdasm

A lightweight ethereum evm bytecode asm instruction registry and disassembler library.

`pip install evmdasm` · installs (wheel) · licence: GPLv2 · rank 10360 · last release 2022-03-11 · [PyPI](https://pypi.org/project/evmdasm/)

_README extract left out: share-alike licence._

### ethereum-dasm

An ethereum bytecode disassembler with static and dynamic analysis features

`pip install ethereum-dasm` · installs (wheel) · licence: GPLv2 · rank 10406 · last release 2019-07-06 · [PyPI](https://pypi.org/project/ethereum-dasm/)

_README extract left out: share-alike licence._

### euclid3

2D and 3D vector, matrix, quaternion and geometry module. updated to python 3.

`pip install euclid3` · installs from source (sdist only) · licence: UNKNOWN · rank 10480 · last release 2014-05-14 · [PyPI](https://pypi.org/project/euclid3/)

<details><summary>README extract</summary>

euclid3
2D and 3D maths module for Python

Homepage:
Contact: Alex Holkner
 Alex.Holkner@mail.google.com

Changes: Update to Python 3 in 2014 by Michael Zimmermann (www.incunabulum.de)

Usage

See "euclid.txt" for detailed documentation. The file is readable as
plain text, and can also be compiled to a set of HTML pages with the
included Makefile. ...

</details>

### expo

Selectively expose module functionality

`pip install expo` · installs (wheel) · licence: not stated · rank 10557 · last release 2021-10-29 · [PyPI](https://pypi.org/project/expo/)

### enumb

Concise, Pythonic Enums

`pip install enumb` · installs (wheel) · licence: not stated · rank 10561 · last release 2021-11-10 · [PyPI](https://pypi.org/project/enumb/)

### etelemetry

Etelemetry python client API

`pip install etelemetry` · installs (wheel) · licence: Apache Software License · rank 10615 · last release 2023-10-13 · [PyPI](https://pypi.org/project/etelemetry/)

<details><summary>README extract</summary>

A lightweight python client to communicate with the etelemetry server

Example:
```python
import etelemetry
etelemetry.get_project("nipy/nipype")

{'version': '1.4.2', 'bad_versions': ['1.2.1', '1.2.3', '1.3.0']}
```

Sections: Etelemetry-client, Usage, Adding etelemetry to your project

</details>

### environ-config

Boilerplate-free configuration with env variables.

`pip install environ-config` · installs (wheel) · licence: Apache-2.0 · rank 10676 · last release 2026-07-22 · [PyPI](https://pypi.org/project/environ-config/) · [docs](https://environ-config.readthedocs.io/) · [source](https://github.com/hynek/environ-config/)

<details><summary>README extract</summary>

<!-- teaser-begin -->

*environ-config* allows you to load your application's configuration from environment variables – as recommended in *The Twelve-Factor App* methodology – with elegant, boilerplate-free, and declarative code:

`AppConfig.from_environ({...})` is equivalent to the code above, depending on your taste.

Features:
- Declarative & boilerplate-free.

- Nested configuration from flat environment variable names.

- Default & mandatory values: enforce configuration structure without writing a line of code. ...

Example:
```python
>>> import environ
>>> # Extracts secrets from Vault-via-envconsul: 'secret/your-app':
>>> vault = environ.secrets.VaultEnvSecrets(vault_prefix="SECRET_YOUR_APP")
>>> @environ.config(prefix="APP")
... class AppConfig:
...    @environ.config
...

</details>

### eclipse-sumo

A microscopic, multi-modal traffic simulation package

`pip install eclipse-sumo` · installs (wheel) · licence: EPL-2.0 OR GPL-2.0-or-later · rank 10714 · last release 2026-10-08 · [PyPI](https://pypi.org/project/eclipse-sumo/) · [docs](https://sumo.dlr.de/docs) · [source](https://github.com/eclipse-sumo/sumo)

_README extract left out: share-alike licence._

### event-model

Data model used by the bluesky ecosystem.

`pip install event-model` · installs (wheel) · licence: BSD License · rank 10776 · last release 2026-06-03 · [PyPI](https://pypi.org/project/event-model/) · [source](https://github.com/bluesky/event-model)

<details><summary>README extract</summary>

Data model used by the bluesky ecosystem.

A primary design goal of bluesky is to enable better research by recording
rich metadata alongside measured data for use in later analysis. Documents are
how we do this. ...

</details>

### escavador

A library to interact with Escavador API

`pip install escavador` · installs (wheel) · licence: MIT License · rank 10827 · last release 2026-01-09 · [PyPI](https://pypi.org/project/escavador/) · [docs](https://api.escavador.com/docs/) · [source](https://github.com/Escavador/escavador-python)

<details><summary>README extract</summary>

- API V1
- API V2

O SDK pode ser instalado via `pip` através do comando:

Example:
```python
import escavador
escavador.config("SUA_API_KEY")
```

Sections: O SDK em Python da API do Escavador, Documentação disponível, Instalação, Requisitos, Como Configurar, Exemplos, Buscando as movimentações de um processo usando a API V2, Solicitar busca assíncrona de processo usando a API V1, Criando Monitoramentos na API V1, Módulos Disponíveis e Referência da API, V1, V2

</details>

### elasticsearch7

Python client for Elasticsearch

`pip install elasticsearch7` · installs (wheel) · licence: Apache Software License · rank 10903 · last release 2026-01-12 · [PyPI](https://pypi.org/project/elasticsearch7/) · [docs](https://elasticsearch-py.readthedocs.io) · [source](https://github.com/elastic/elasticsearch-py)

<details><summary>README extract</summary>

*The official Python client for Elasticsearch.*

Features:
* Translating basic Python data types to and from JSON
* Configurable automatic discovery of cluster nodes
* Persistent connections
* Load balancing (with pluggable selection strategy) across available nodes
* Failed connection penalization (time ...

Example:
```python
# Import the client from the 'elasticsearch' module
>>> from elasticsearch import Elasticsearch

# Instantiate a client instance
>>> client = Elasticsearch("

# Call an API, in this example `info()`
>>> resp = client.info()

# View the result
>>> resp
{
  "name" : "instance-name",
  "cluster_name" : "cluster-name",
...
```

Sections: Elasticsearch Python Client, Features, Compatibility, Documentation, Quick Start

</details>

### es-client

Elasticsearch Client builder, complete with schema validation

`pip install es-client` · installs (wheel) · licence: Apache Software License · rank 11161 · last release 2025-10-03 · [PyPI](https://pypi.org/project/es-client/) · [docs](https://es-client.readthedocs.io/) · [source](http://github.com/untergeek/es_client)

<details><summary>README extract</summary>

You may wonder why this even exists, as at first glance it doesn't seem to make
anything any easier than just using the elasticsearch9 Python module to
build a client connection. I needed to be able to reuse the more complex
schema validation bits I was employing, namely: ...

Example:
```python
from es_client import Builder

config = {
    'elasticsearch': {
        'client': {
            'hosts': '
            'ca_certs': '/etc/elasticsearch/certs/ca.crt',
            'request_timeout': 60,
        },
        'other_settings': {
            'master_only': false,
            'username': 'joe_user',
            'password': 'password',
...
```

Sections: es_client, Example Usage

</details>

### etcd-sdk-python

Python client for the etcd v3 API for python >= 3.8

`pip install etcd-sdk-python` · installs (wheel) · licence: Apache Software License · rank 11190 · last release 2025-08-04 · [PyPI](https://pypi.org/project/etcd-sdk-python/) · [source](https://github.com/XuanYang-cn/pyetcd)

<details><summary>README extract</summary>

Python client for the etcd API v3, supported python >= 3.7, under active maintenance

Example:
```python
import pyetcd

etcd = pyetcd.client()

etcd.get('foo')
etcd.put('bar', 'doot')
etcd.delete('bar')

# locks
lock = etcd.lock('thing')
lock.acquire()
# do something
lock.release()

with etcd.lock('doot-machine') as lock:
    # do something

# transactions
etcd.transaction(
    compare=[
        etcd.transactions.value('/doot/testing') == 'doot',
...
```

Sections: pyetcd, Basic usage, Dev

</details>

### espn-api

ESPN API

`pip install espn-api` · installs (wheel) · licence: MIT License · rank 11263 · last release 2026-10-09 · [PyPI](https://pypi.org/project/espn-api/)

<details><summary>README extract</summary>

This package uses ESPN's Fantasy API to extract data from any public or private league for Fantasy Football and Basketball (NHL, MLB, and WNBA are in development).
Please feel free to make suggestions, bug reports, and pull request for features or fixes!

This package was inspired and based off of rbarton65/espnff.

Example:
```python
# Football API
from espn_api.football import League
# Basketball API
from espn_api.basketball import League
# Hockey API
from espn_api.hockey import League
# Baseball API
from espn_api.baseball import League
# Init
league = League(league_id=222, year=2019)
```

Sections: ESPN API, Note, Tests, Format, Type check, Usage, For Getting Started and API details head over to the Wiki!, Discussions (new), Issue Reporting

</details>

### ExtensionClass

Metaclass for subclassable extension types

`pip install ExtensionClass` · installs (wheel) · licence: ZPL-2.1 · rank 11424 · last release 2026-10-16 · [PyPI](https://pypi.org/project/ExtensionClass/) · [source](https://github.com/zopefoundation/ExtensionClass)

<details><summary>README extract</summary>

This package provides a metaclass that allows classes implemented in
extension modules to be subclassed in Python. Unless you need
ExtensionClasses for legacy applications (e.g. Zope), you probably
want to use Python's new-style classes (available since Python 2.2). ...

Sections: ExtensionClass and ExtensionClass-related packages, ExtensionClass, ComputedAttribute, MethodObject, 6.5 (2026-10-16), 6.4 (2026-08-20), 6.3 (2026-04-30), 6.2 (2025-11-16), 6.1 (2025-10-29), 6.0 (2024-09-17), 5.1 (2023-10-05), 5.0 (2023-01-19), 4.9 (2022-11-17), 4.8 (2022-11-03)

</details>

### envsubst

Substitute environment variables in a string

`pip install envsubst` · installs (wheel) · licence: MIT · rank 11457 · last release 2019-10-05 · [PyPI](https://pypi.org/project/envsubst/)

<details><summary>README extract</summary>

Substitute environment variables in a string:
Also supports $0, $1, etc. from argv.

Example:
```python
>>> import os
>>> from envsubst import envsubst

>>> del os.environ['PS1']
>>> print(envsubst('$USER@$HOST ${PS1:-$}:'))
ashafer01@github.com $:

>>> os.environ['PS1'] = ''
>>> print(envsubst('$USER@$HOST ${PS1:-$}:'))
ashafer01@github.com $:

>>> print(envsubst('$USER@$HOST ${PS1-foo}:'))
ashafer01@github.com :

...
```

</details>

### elasticsearch6

Python client for Elasticsearch

`pip install elasticsearch6` · installs (wheel) · licence: Apache Software License · rank 11735 · last release 2021-03-09 · [PyPI](https://pypi.org/project/elasticsearch6/)

<details><summary>README extract</summary>

Official low-level client for Elasticsearch. Its goal is to provide common
ground for all Elasticsearch-related code in Python; because of this it tries
to be opinion-free and very extendable. ...

Features:
The client's features include:

 * translating basic Python data types to and from json (datetimes are not
 decoded for performance reasons)
 * configurable automatic discovery of cluster nodes
 * persistent connections
 * load balancing (with ...

Example:
```python
>>> from datetime import datetime
>>> from elasticsearch import Elasticsearch

# by default we connect to localhost:9200
>>> es = Elasticsearch()

# create an index in elasticsearch, ignore status code 400 (index already exists)
>>> es.indices.create(index='my-index', ignore=400)
{u'acknowledged': True}

...

</details>

### extendable-enum

A utility package for extending, subclassing and reusing Enum classes.

`pip install extendable-enum` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 11767 · last release 2022-06-29 · [PyPI](https://pypi.org/project/extendable-enum/) · [docs](https://extendable-enum.readthedocs.io/en/latest/)

_README extract left out: share-alike licence._

### elasticsearch8-dsl

Python client for Elasticsearch

`pip install elasticsearch8-dsl` · installs (wheel) · licence: Apache Software License · rank 11813 · last release 2024-01-19 · [PyPI](https://pypi.org/project/elasticsearch8-dsl/)

<details><summary>README extract</summary>

Elasticsearch DSL is a high-level library whose aim is to help with writing and
running queries against Elasticsearch. It is built on top of the official
low-level client (elasticsearch-py).

It provides a more convenient and idiomatic way to write and manipulate
queries. ...

Example:
```python
from elasticsearch import Elasticsearch
client = Elasticsearch("

response = client.search(
    index="my-index",
    body={
      "query": {
        "bool": {
          "must": [{"match": {"title": "python"}}],
          "must_not": [{"match": {"description": "beta"}}],
          "filter": [{"term": {"category": "search"}}]
        }
      },
...
```

Sections: Elasticsearch DSL, Examples, Compatibility, Search Example, Persistence Example, Migration from `elasticsearch-py`, Documentation

</details>

### eng-to-ipa

take English text and convert it to IPA

`pip install eng-to-ipa` · installs from source (sdist only) · licence: not stated · rank 12455 · last release 2020-04-17 · [PyPI](https://pypi.org/project/eng-to-ipa/)

<details><summary>README extract</summary>

This Python program utilizes the Carnegie-Mellon University Pronouncing Dictionary to convert English text into the International Phonetic Alphabet.

The `convert` function is used to take English text and convert it to IPA, like so:

Note that words that cannot be found in the CMU dictionary are simply reprinted with an asterisk.

Example:
```python
>>> import eng_to_ipa as ipa
>>> ipa.convert("The quick brown fox jumped over the lazy dog.")
'ðə kwɪk braʊn fɑks ʤəmpt ˈoʊvər ðə ˈleɪzi dɔg.'
```

Sections: English to IPA (eng_to_ipa), `convert` parameters

</details>

### e2cnn

E(2)-Equivariant CNNs Library for PyTorch

`pip install e2cnn` · installs (wheel) · licence: BSD 3-Clause Clear · rank 12463 · last release 2023-02-02 · [PyPI](https://pypi.org/project/e2cnn/)

<details><summary>README extract</summary>

General E(2)-Equivariant Steerable CNNs

Documentation | Experiments | Paper | Thesis | new escnn library

Check out our new escnn library which extends *e2cnn* to a wider class of equivariance groups. ...

Example:
```python
from e2cnn import gspaces                                          #  1
from e2cnn import nn                                               #  2
import torch                                                       #  3
                                                                   #  4
...
```

Sections: Demo, Experimental results, Getting Started, Dependencies

</details>

### elevenlabs-mcp

ElevenLabs MCP Server

`pip install elevenlabs-mcp` · installs (wheel) · licence: MIT License · rank 12570 · last release 2026-08-04 · [PyPI](https://pypi.org/project/elevenlabs-mcp/)

<details><summary>README extract</summary>

Official ElevenLabs Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech and audio processing APIs. This server allows MCP clients like Claude Desktop, Cursor, Windsurf, OpenAI Agents and others to generate speech, clone voices, transcribe audio, and more.

Sections: Quickstart with Claude Desktop, Other MCP clients, Example usage, Optional features, File Output Configuration, Output Modes, Data residency keys, Troubleshooting, Timeouts when using certain tools, MCP ElevenLabs: spawn uvx ENOENT

</details>

### exp-gateway-native

Rust data plane for the Experiential local gateway (compiled extension module).

`pip install exp-gateway-native` · installs (wheel) · licence: not stated · rank 12574 · last release 2026-11-07 · [PyPI](https://pypi.org/project/exp-gateway-native/)

### edfio

Read and write EDF/EDF+C/BDF/BDF+C files.

`pip install edfio` · installs (wheel) · licence: Apache Software License · rank 12704 · last release 2026-10-01 · [PyPI](https://pypi.org/project/edfio/) · [docs](https://edfio.readthedocs.io) · [source](https://github.com/the-siesta-group/edfio)

<details><summary>README extract</summary>

edfio is a Python package for reading and writing EDF and EDF+C files.

It requires Python>=3.9 and NumPy>=1.22 and is available on PyPI:

 pip install edfio

- Support for EDF, EDF+C, BDF, and BDF+C including annotations
- Fast I/O thanks to NumPy - read and write GB-sized files in seconds ...

Features:
- Read/write from/to files or file-like objects
- Modify signal and recording headers
- Drop EDF+ annotations
- Slice recordings (by seconds or annotation texts)
- Drop individual signals
- Anonymize recordings
- BDF file (BioSemi) support

Example:
```python
from edfio import read_edf

edf = read_edf("example.edf")
```

Sections: edfio, Features, Known limitations, Usage

</details>

### esp-bool-parser

Tools for building ESP-IDF related apps.

`pip install esp-bool-parser` · installs (wheel) · licence: Apache Software License · rank 12957 · last release 2026-03-18 · [PyPI](https://pypi.org/project/esp-bool-parser/) · [docs](https://docs.espressif.com/projects/esp-bool-parser) · [source](https://github.com/espressif/esp-bool-parser)

<details><summary>README extract</summary>

`esp-bool-parser` is a package that provides a way to process boolean statements based on `soc_caps` files in the ESP-IDF.

It helps you locate `soc_headers` files in the ESP-IDF, parse them, and store the parsed values as constants, which are then used in `ChipAttr`. ...

Example:
```python
stmt_string = 'IDF_TARGET == "esp32"'
stmt = parse_bool_expr(stmt_string)
result = stmt.get_value("esp32", "config_name")
```

Sections: esp-bool-parser, Key Functions, `parse_bool_expr(stmt: str)`

</details>

### ewokscore

API for graphs and tasks in Ewoks

`pip install ewokscore` · installs (wheel) · licence: MIT License · rank 13023 · last release 2026-07-01 · [PyPI](https://pypi.org/project/ewokscore/) · [docs](https://ewokscore.readthedocs.io/) · [source](https://github.com/ewoks-kit/ewokscore)

<details><summary>README extract</summary>

*ewokscore* provides an API to define workflows and implement tasks in ewoks.

Example:
```python
from ewokscore.task import Task
from ewokscore import execute_graph

# Implement a workflow task
class SumTask(
    Task, input_names=["a"], optional_input_names=["b"], output_names=["result"]
):
    def run(self):
        result = self.inputs.a
        if self.inputs.b:
            result += self.inputs.b
        self.outputs.result = result

...
```

Sections: ewokscore, Test, Getting started, Documentation

</details>

### ezc3d

Easy to use C3D reader/writer for C++, Python, and Matlab

`pip install ezc3d` · installs (wheel) · licence: not stated · rank 13044 · last release 2026-08-07 · [PyPI](https://pypi.org/project/ezc3d/)

<details><summary>README extract</summary>

EZC3D is an easy to use reader, modifier and writer for C3D format files. It is written in C++ with proper binders for Python and MATLAB scripting languages.

C3D ( is a format specifically designed to store biomechanics data. Hence many biomechanics softwares can produce C3D files in order to share data. ...

Example:
```python
    // ...
    int desired_frame = 0;

    pf_0.forces()[desired_frame];   // Forces on the platform
    pf_0.moments()[desired_frame];  // Moments on the platform in global reference frame
    pf_0.CoP()[desired_frame];      // Center of pressure
    pf_0.Tz()[desired_frame];       // Moments expressed at the center of pressure

...
```

...

</details>

### emailable

This is the official python wrapper for the Emailable API.

`pip install emailable` · installs (wheel) · licence: MIT License · rank 13081 · last release 2025-06-02 · [PyPI](https://pypi.org/project/emailable/) · [docs](https://emailable.com/docs/api?python) · [source](https://github.com/emailable/emailable-python)

<details><summary>README extract</summary>

This is the official python wrapper for the Emailable API.

See the Python API docs.

Example:
```python
client = emailable.Client('your_api_key')
```

Sections: Emailable Python Library, Documentation, Usage, Authentication, Verification, Slow Email Server Handling, Batch Verification, Start a batch

</details>

### envresolve

Resolve env vars from secret stores.

`pip install envresolve` · installs (wheel) · licence: MIT · rank 13107 · last release 2026-07-03 · [PyPI](https://pypi.org/project/envresolve/) · [docs](https://osoekawaitlab.github.io/envresolve/) · [source](https://github.com/osoekawaitlab/envresolve)

<details><summary>README extract</summary>

Resolve environment variables from secret stores like Azure Key Vault.

Features:
- Variable expansion: Expand `${VAR}` and `$VAR` syntax in strings
- Secret resolution: Fetch secrets from Azure Key Vault (more providers coming)
- Circular reference detection: Prevents infinite loops in variable chains ...

Example:
```python
from envresolve import expand_variables

env = {"VAULT": "corp-kv", "SECRET": "db-password"}
result = expand_variables("akv://${VAULT}/${SECRET}", env)
print(result)  # akv://corp-kv/db-password
```

Sections: envresolve, Features, Quick Start, Variable Expansion, Default Values, Load from .env File, Direct Secret Resolution, Custom Provider Configuration, Resolve Existing Environment Variables, Error Handling, Documentation, Setup, Running Tests, Code Quality

</details>

### edx-opaque-keys

Create and introspect course and xblock identities through a clear and consistent API

`pip install edx-opaque-keys` · installs (wheel) · licence: AGPL-3.0-only · rank 13109 · last release 2026-09-30 · [PyPI](https://pypi.org/project/edx-opaque-keys/)

_README extract left out: share-alike licence._

### edx-django-utils

EdX utilities for Django Application development.

`pip install edx-django-utils` · installs (wheel) · licence: Apache Software License · rank 13219 · last release 2026-10-01 · [PyPI](https://pypi.org/project/edx-django-utils/)

<details><summary>README extract</summary>

EdX utilities for Django Application development.

Note that some utilities may warrant their own repository. A judgement call
needs to be made as to whether code properly belongs here or not. Please
review with the Architecture Team if you have any questions.

This repository includes shared utilities for: ...

Sections: edx-django-utils, Purpose, Documentation, Design Pattern followed by packages, Getting Help, People, 8.1.0 - 2026-10-01, 8.0.2 - 2026-08-21, 8.0.1 - 2025-09-29, 8.0.0 - 2025-05-22, 7.4.0 - 2025-04-10, 7.3.0 - 2025-04-09, Added, 7.2.0 - 2025-02-26

</details>

### eli5

Debug machine learning classifiers and explain their predictions

`pip install eli5` · installs (wheel) · licence: MIT License · rank 13239 · last release 2025-04-20 · [PyPI](https://pypi.org/project/eli5/)

<details><summary>README extract</summary>

ELI5 is a Python package which helps to debug machine learning
classifiers and explain their predictions.

It provides support for the following machine learning frameworks and packages:

* scikit-learn. ...

Sections: ELI5, 0.16.0 (2024-04-20), 0.15.0 (2025-04-06), 0.14.0 (2025-03-26), 0.13.0 (2022-05-11), 0.12.0 (2022-05-11), 0.11.0 (2021-01-23), 0.10.1 (2019-08-29), 0.10.0 (2019-08-21), 0.9.0 (2019-07-05), 0.8.2 (2019-04-04), 0.8.1 (2018-11-19), 0.8 (2017-08-25), 0.7 (2017-07-03)

</details>

### etcd3gw

A Python client for etcd3 grpc-gateway v3 API

`pip install etcd3gw` · installs (wheel) · licence: Apache Software License · rank 13310 · last release 2026-06-09 · [PyPI](https://pypi.org/project/etcd3gw/) · [source](https://opendev.org/openstack/etcd3gw)

<details><summary>README extract</summary>

The etcd3gw library provides a python client for etcd3 grpc-gateway v3 API.

* License: Apache License, Version 2.0

</details>

### earthkit-data

A format-agnostic Python interface for geospatial data

`pip install earthkit-data` · installs (wheel) · licence: Apache-2.0 · rank 13369 · last release 2026-10-28 · [PyPI](https://pypi.org/project/earthkit-data/) · [docs](https://earthkit-data.readthedocs.io/) · [source](https://github.com/ecmwf/earthkit-data/)

<details><summary>README extract</summary>

Quick Start
 Installation
 Documentation

> \[!IMPORTANT\]
> This software is Graduated and subject to ECMWF's guidelines on Software Maturity.

earthkit-data is a format-agnostic interface for geospatial data with a focus on meteorology and
climate science. It is the data handling component of earthkit.

Example:
```python
import earthkit.data as ekd

data = ekd.from_source("sample", "test.grib")
arr = data.to_numpy()
df = data.to_pandas()
dataset = data.to_xarray()
```

</details>

### experiential

Build simulations and optimize model routing from agent traces.

`pip install experiential` · installs (wheel) · licence: not stated · rank 13428 · last release 2026-11-07 · [PyPI](https://pypi.org/project/experiential/)

<details><summary>README extract</summary>

Experiential is an open source gateway and router for agent workflows:

1. Use hosted, BYOK, and local models through one OpenAI-compatible API.
2. Control which users and agents can use which models, for which use cases, and how much they can spend.
3. Turn production traffic into a custom router or model optimized for quality, speed, and cost. ...

Example:
```python
import exp

with exp.load_router("my-project") as client:
    response = client.chat.completions.create(
        model="my-project",
        messages=[{"role": "user", "content": "hello"}],
    )
```

Sections: Experiential, Getting Started, Setup / get started with the hosted gateway, Using the API, Capture Traffic, Optimize from Traffic, Telemetry

</details>

### esperanto

A light-weight, production-ready, unified interface for various AI model providers

`pip install esperanto` · does not install on CPython 3.14 · licence: MIT · rank 13446 · last release 2026-10-03 · [PyPI](https://pypi.org/project/esperanto/) · [docs](https://github.com/lfnovo/esperanto#readme) · [source](https://github.com/lfnovo/esperanto)

<details><summary>README extract</summary>

Esperanto is a powerful Python library that provides a unified interface for interacting with various Large Language Model (LLM) providers. It simplifies the process of working with different AI models (LLMs, Embedders, Transcribers, and TTS) APIs by offering a consistent interface while maintaining provider-specific optimizations.

Features:
🪶 Ultra-Lightweight Architecture
- Direct HTTP Communication: All providers communicate directly via HTTP APIs using `httpx` - no bulky vendor SDKs required ...

Example:
```python
from esperanto.factory import AIFactory

# Get available providers for each model type
providers = AIFactory.get_available_providers()
print(providers)
# Output:
# {
...
```

...

</details>

### envtpl

Render jinja2 templates on the command line using shell environment variables

`pip install envtpl` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 13519 · last release 2026-03-19 · [PyPI](https://pypi.org/project/envtpl/)

_README extract left out: share-alike licence._

### edx-enterprise

Enterprise features for the Open edX platform

`pip install edx-enterprise` · installs (wheel) · licence: AGPL-3.0-or-later · rank 13520 · last release 2026-11-03 · [PyPI](https://pypi.org/project/edx-enterprise/) · [source](https://github.com/openedx/edx-enterprise)

_README extract left out: share-alike licence._

### emport

Utility library for performing programmatic imports

`pip install emport` · installs (wheel) · licence: BSD 3-Clause License · rank 13659 · last release 2024-10-13 · [PyPI](https://pypi.org/project/emport/) · [source](https://github.com/vmalloc/emport)

<details><summary>README extract</summary>

Features:
Emport is a small utility library for importing files by file name. It exposed a single function, ``import_file(filename)``.

Unlike traditional usages of ``import``, ``execfile`` or even ``imp.load_source``, Emport takes care of all cases that you ...

</details>

### ensureconda

Lightweight bootstrapper for a conda executable

`pip install ensureconda` · installs (wheel) · licence: MIT · rank 13787 · last release 2026-10-18 · [PyPI](https://pypi.org/project/ensureconda/)

<details><summary>README extract</summary>

Sections: ensureconda, Python-based, Go based, Usage, Configuring conda-standalone channel

</details>

### excel

This package name is reserved by Microsoft Corporation

`pip install excel` · installs (wheel) · licence: not stated · rank 13822 · last release 2023-01-09 · [PyPI](https://pypi.org/project/excel/)

<details><summary>README extract</summary>

This is not a usable Python package, but the name is
reserved by Microsoft Corporation.

Visit `aka.ms/Python < for information about
tools and products released by Microsoft for Python developers.

You can find other packages published by Microsoft at
`pypi.org/user/microsoft < ...

</details>

### eventsourcing-sqlalchemy

Python package for eventsourcing with SQLAlchemy.

`pip install eventsourcing-sqlalchemy` · installs (wheel) · licence: BSD License; Other/Proprietary License · rank 13894 · last release 2026-02-28 · [PyPI](https://pypi.org/project/eventsourcing-sqlalchemy/) · [source](https://github.com/pyeventsourcing/eventsourcing-sqlalchemy)

<details><summary>README extract</summary>

This package supports using the Python
eventsourcing library
with SQLAlchemy.

Example:
```python
from eventsourcing.application import Application
from eventsourcing.domain import Aggregate, event
from uuid import uuid5, NAMESPACE_URL

class TrainingSchool(Application):
    def register(self, name):
        dog = Dog(name)
        self.save(dog)

    def add_trick(self, name, trick):
        dog = self.repository.get(Dog.create_id(name))
...
```

Sections: Event Sourcing in Python with SQLAlchemy, Quick start, Getting started, Managing transactions outside the application, Using SQLAlchemy scoped sessions, Managing sessions with Flask-SQLAlchemy, Managing sessions with FastAPI-SQLAlchemy, Google Cloud SQL Python Connector, More information

</details>

### embedchain

Simplest open source retrieval (RAG) framework

`pip install embedchain` · does not install on CPython 3.14 · licence: Other/Proprietary License · rank 13983 · last release 2025-03-25 · [PyPI](https://pypi.org/project/embedchain/)

<details><summary>README extract</summary>

Embedchain is an Open Source Framework for personalizing LLM responses. It makes it easy to create and deploy personalized AI apps. At its core, Embedchain follows the design principle of being *"Conventional but Configurable"* to serve both software engineers and machine learning engineers. ...

Example:
```python
import os
from embedchain import App

# Create a bot instance
os.environ["OPENAI_API_KEY"] = ""
app = App()

# Embed online resources
app.add("
app.add("

# Query the app
app.query("How many companies does Elon Musk run and name those?")
...
```

Sections: What is Embedchain?, Python API, ✨ Live demo, 🔍 Usage, 📖 Documentation, 🤝 Schedule a 1-on-1 Session, Anonymous Telemetry

</details>

### epik8s-tools

A set of tools for generating Kubernetes Helm charts for EPICS-based systems.

`pip install epik8s-tools` · installs (wheel) · licence: MIT License · rank 14060 · last release 2026-09-21 · [PyPI](https://pypi.org/project/epik8s-tools/)

<details><summary>README extract</summary>

`epik8s-tools` is a Python-based toolset for automating project structure generation, Helm chart creation, and deployment for EPICS (Experimental Physics and Industrial Control System) applications in Kubernetes environments *EPIK8s*. ...

Features:
- Project Structure Generation: Automatically create directories and files needed for EPICS-based projects.
- Helm Chart Creation: Generate Helm charts for Kubernetes deployments with custom values and templates. ...

Sections: epik8s-tools, Features, CLI Options, Examples, Basic Beamline Generation, IOC configuration format, Generating OPI Panels, Example Command, Detailed Launcher, Specifying CA and PVA Gateway IPs, Running IOCs with `epik8s-run`

</details>

### ecmwf-api-client

Python client for ECMWF web services API.

`pip install ecmwf-api-client` · installs (wheel) · licence: Apache Software License · rank 14166 · last release 2026-06-17 · [PyPI](https://pypi.org/project/ecmwf-api-client/)

<details><summary>README extract</summary>

Python client for the ECMWF Web API. Two entry points:

- `ECMWFDataServer` — retrieve IFS research experiments.
- `ECMWFService` — access MARS, ECMWF's Meteorological Archival and Retrieval System, for authorized users.

- IFS research experiments — available anonymously, or with registered access for a better quality of service. ...

Example:
```python
from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()
server.retrieve({
    # ... request parameters ...
})
```

Sections: ecmwf-api-client, What this client is for, Looking for public datasets?, Configure, Anonymous access (default), Registered access (recommended), Retrieving IFS research experiments, Accessing MARS, Retrieving efficiently, Logging

</details>

### entmax

The entmax mapping and its loss, a family of sparse alternatives to softmax.

`pip install entmax` · installs (wheel) · licence: MIT · rank 14213 · last release 2024-02-07 · [PyPI](https://pypi.org/project/entmax/)

### edgescaleai-cube-mcp

MCP server for EdgescaleAI Cube operations

`pip install edgescaleai-cube-mcp` · installs (wheel) · licence: not stated · rank 14239 · last release 2026-10-26 · [PyPI](https://pypi.org/project/edgescaleai-cube-mcp/)

<details><summary>README extract</summary>

MCP server for EdgescaleAI Cube management and Apollo deployments.

> New owner / inheriting this repo? Jump to Operations & Ownership. The two runbooks you need are docs/admin.md (full RBAC + infra reference) and docs/adding-new-user.md (onboard a teammate end-to-end). ...

Sections: cube-mcp, Architecture, How it works, Getting Started, Tools, Auth, Kubernetes, Apps, App Exposure, Build & Registry, Apollo Environments, Apollo Modules, Apollo Secrets, Groundcover (observability)

</details>

### execnb

A description of your project

`pip install execnb` · installs (wheel) · licence: Apache-2.0 · rank 14393 · last release 2026-10-27 · [PyPI](https://pypi.org/project/execnb/) · [docs](https://AnswerDotAI.github.io/execnb/) · [source](https://github.com/AnswerDotAI/execnb/)

<details><summary>README extract</summary>

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

Example:
```python
from execnb.shell import *
from fastcore.utils import *
from fastcore.nbio import *
```

Sections: execnb, How to use

</details>

### epubcheck

Python epubcheck wrapper

`pip install epubcheck` · installs (wheel) · licence: BSD-3-Clause · rank 14513 · last release 2026-08-18 · [PyPI](https://pypi.org/project/epubcheck/) · [source](https://github.com/titusz/epubcheck/)

<details><summary>README extract</summary>

> A command line tool and lib that wraps EpubCheck for Python.

The original EpubCheck is the standard Java-based validation
tool for EPUB maintained by DAISY Consortium on behalf of the
W3C, originally developed by the
IDPF. ...

Example:
```python
from epubcheck import EpubCheck

result = EpubCheck("/path/to/book.epub")
print(result.valid)
print(result.messages)
```

Sections: Python wrappers and CLI for EpubCheck, Introduction, Quickstart, Command line usage examples, Using epubcheck as a python library, Documentation, Releasing, 5.3.0 - 2026-08-18, 5.1.0 - 2024-06-05, 4.2.6 - 2021-11-06, 0.4.3 - 2021-09-28, 0.4.2 - 2019-08-07, 0.3.1 - 2016-04-20, 0.3.0 - 2016-04-10

</details>

### eip712

eip712: Message classes for typed structured data hashing and signing in Ethereum

`pip install eip712` · installs (wheel) · licence: Apache-2.0 · rank 14541 · last release 2025-12-23 · [PyPI](https://pypi.org/project/eip712/)

<details><summary>README extract</summary>

Example:
```python
from eip712.messages import EIP712Message

# NOTE: It is highly recommended to use ABI types from this library
from eth_pydantic_types import abi

from pydantic import BaseModel

# You can define your inner nested types using normal Pydantic models
class Person(EIP712Type):
    # Define fields using types from the `abi` module
    name: abi.string
...
```

Sections: Quick Start, Dependencies, via `pip`, via `uv`, Quick Usage

</details>

### edison-client

A client for interacting with endpoints of the Edison Scientific service.

`pip install edison-client` · installs (wheel) · licence: not stated · rank 14853 · last release 2026-10-23 · [PyPI](https://pypi.org/project/edison-client/)

<details><summary>README extract</summary>

Documentation and tutorials for edison-client,
a client for interacting with endpoints of the EdisonScientific platform.

See our cookbook
for detailed documentation on usage.

<!--TOC-->

Table of Contents

- Installation
- Quickstart
- Functionalities
- Authentication
- Simple task running
- Task Continuation
- Asynchronous tasks

<!--TOC-->

Example:
```python
from edison_client import EdisonClient, JobNames

# Set your API key to EDISON_API_KEY environment variable,
# or pass it as a string literal to the api_key parameter
client = EdisonClient()

task_data = {
    "name": JobNames.LITERATURE,
    "query": (
        "Which neglected diseases had a treatment developed"
...
```

...

</details>

### envpool-assets

Runtime data assets for EnvPool.

`pip install envpool-assets` · installs (wheel) · licence: Apache-2.0 · rank 14876 · last release 2026-08-29 · [PyPI](https://pypi.org/project/envpool-assets/)

<details><summary>README extract</summary>

Runtime data assets for EnvPool.

This repository builds platform-independent data wheels. Platform-specific
executables and native libraries stay in the main `envpool` wheels.

Most assets are shipped in the main `envpool-assets` wheel. Asset groups that
would push that wheel over PyPI's file-size limit are split into their own
wheels. ...

Sections: envpool-assets, Packages, Build Locally, Expected Asset Root Layouts

</details>

