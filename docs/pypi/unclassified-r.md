# Unclassified / R

[Index](README.md) · 225 packages in this topic, by downloads.

### rpds-py

Python bindings to Rust's persistent data structures (rpds)

`pip install rpds-py` · installs (wheel) · licence: MIT · rank 46 · last release 2026-10-04 · [PyPI](https://pypi.org/project/rpds-py/) · [docs](https://rpds.readthedocs.io/) · [source](https://github.com/crate-py/rpds)

<details><summary>README extract</summary>

Python bindings to the Rust rpds crate for persistent data structures.

What's here is quite minimal (in transparency, it was written initially to support replacing `pyrsistent` in the referencing library).
If you see something missing (which is very likely), a PR is definitely welcome to add it.

Example:
```python
>>> from rpds import HashTrieMap, HashTrieSet, List

>>> m = HashTrieMap({"foo": "bar", "baz": "quux"})
>>> m.insert("spam", 37) == HashTrieMap({"foo": "bar", "baz": "quux", "spam": 37})
True
>>> m.remove("foo") == HashTrieMap({"baz": "quux"})
True

>>> s = HashTrieSet({"foo", "bar", "baz", "quux"})
...
```

Sections: `rpds.py`, Usage

</details>

### rich

Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal

`pip install rich` · installs (wheel) · licence: MIT License · rank 57 · last release 2026-04-12 · [PyPI](https://pypi.org/project/rich/) · [docs](https://rich.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

English readme
 • 简体中文 readme
 • 正體中文 readme
 • Lengua española readme
 • Deutsche readme
 • Läs på svenska
 • 日本語 readme
 • 한국어 readme
 • Français readme
 • Schwizerdütsch readme
 • हिन्दी readme
 • Português brasileiro readme
 • Italian readme
 • Русский readme
 • Indonesian readme
 • فارسی readme
 • Türkçe readme
 • Polskie readme ...

Example:
```python
from rich import print

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())
```

Sections: Compatibility, Rich Print, Rich REPL, Using the Console, Rich Inspect, Rich Library, Rich CLI, Textual, Toad

</details>

### requests-oauthlib

OAuthlib authentication support for Requests.

`pip install requests-oauthlib` · installs (wheel) · licence: BSD License · rank 123 · last release 2024-03-22 · [PyPI](https://pypi.org/project/requests-oauthlib/)

<details><summary>README extract</summary>

This project provides first-class OAuth library support for Requests.

OAuth 1 can seem overly complicated and it sure has its quirks. Luckily,
requests_oauthlib hides most of these and let you focus at the task at hand.

Accessing protected resources using requests_oauthlib is as simple as: ...

Example:
```python
>>> from requests_oauthlib import OAuth1Session
>>> twitter = OAuth1Session('client_key',
                            client_secret='client_secret',
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')
>>> url = '
>>> r = twitter.get(url)
```

...

</details>

### redis

Python client for Redis database and key-value store

`pip install redis` · installs (wheel) · licence: MIT · rank 140 · last release 2026-07-30 · [PyPI](https://pypi.org/project/redis/) · [docs](https://redis.readthedocs.io/en/latest/) · [source](https://github.com/redis/redis-py)

<details><summary>README extract</summary>

The Python interface to the Redis key-value store.

Installation | Usage | Advanced Topics | Contributing

Note: redis-py 5.0 is the last version of redis-py that supports Python 3.7, as it has reached end of life. redis-py 5.1 supports Python 3.8+. ...

Example:
```python
>>> import redis
>>> r = redis.Redis(host='localhost', port=6379, db=0)
>>> r.set('foo', 'bar')
True
>>> r.get('foo')
b'bar'
```

Sections: redis-py, How do I Redis?, Usage, Basic Example, Connection Pools, Redis Commands, Advanced Topics, Pipelines, PubSub, Redis’ search and query capabilities default dialect, Multi-database client (Active-Active), Bulk hash ingestion (HIMPORT)

</details>

### requests-toolbelt

A utility belt for advanced users of python-requests

`pip install requests-toolbelt` · installs (wheel) · licence: Apache Software License · rank 151 · last release 2023-05-01 · [PyPI](https://pypi.org/project/requests-toolbelt/) · [source](https://github.com/requests/toolbelt)

<details><summary>README extract</summary>

This is just a collection of utilities for python-requests, but don't
really belong in `requests` proper. The minimum tested requests version is
`2.1.0`. In reality, the toolbelt should work with `2.0.1` as well, but
some idiosyncracies prevent effective or sane testing on that version.

`pip install requests-toolbelt` to get started! ...

Example:
```python
from requests_toolbelt import MultipartEncoder
import requests

m = MultipartEncoder(
    fields={'field0': 'value', 'field1': 'value',
            'field2': ('filename', open('file.py', 'rb'), 'text/plain')}
    )

r = requests.post(' data=m,
                  headers={'Content-Type': m.content_type})
```

...

</details>

### RapidFuzz

rapid fuzzy string matching

`pip install RapidFuzz` · installs (wheel) · licence: MIT · rank 244 · last release 2026-08-30 · [PyPI](https://pypi.org/project/RapidFuzz/) · [docs](https://rapidfuzz.github.io/RapidFuzz/) · [source](https://github.com/rapidfuzz/RapidFuzz.git)

<details><summary>README extract</summary>

Description •
 Installation •
 Usage •
 License

RapidFuzz is a fast string matching library for Python and C++, which is using the string similarity calculations from FuzzyWuzzy. ...

Example:
```python
words = [
    "".join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    for _ in range(10_000)
]
samples = words[:: len(words) // 100]
```

Sections: Description, Requirements, with pip, with conda, from git, Usage, Scorers, Simple Ratio, Partial Ratio, Token Sort Ratio, Token Set Ratio, Weighted Ratio, Quick Ratio, Process

</details>

### rfc3339-validator

A pure python RFC3339 validator

`pip install rfc3339-validator` · installs (wheel) · licence: MIT License · rank 350 · last release 2021-05-12 · [PyPI](https://pypi.org/project/rfc3339-validator/)

<details><summary>README extract</summary>

A pure python RFC3339 validator

Example:
```python
from rfc3339_validator import validate_rfc3339

validate_rfc3339('1424-45-93T15:32:12.9023368Z')
>>> False

validate_rfc3339('2001-10-23T15:32:12.9023368Z')
>>> True
```

Sections: rfc3339-validator, Usage

</details>

### rich-rst

A beautiful reStructuredText renderer for rich

`pip install rich-rst` · installs (wheel) · licence: MIT · rank 360 · last release 2026-09-27 · [PyPI](https://pypi.org/project/rich-rst/) · [docs](https://rich-rst.readthedocs.io/en/latest/) · [source](https://github.com/wasi-master/rich-rst)

<details><summary>README extract</summary>

rich-rst

Render reStructuredText with Rich. This package turns reST documents into Rich renderables so you can preview documentation, docstrings, and snippets directly in the terminal. Also includes a CLI.

Features:
- Supports all currently documented RST elements.
- Handles common documentation features such as headings, lists, tables, links, images, code blocks, footnotes, and many Sphinx roles.
- Provides both a Python API and a command-line interface. ...

Example:
```python
from rich import print
from rich_rst import RestructuredText

document = """
# rich-rst
This is a test document.

- Item one
- Item two

.. code-block:: python

   print("hello")
"""

print(RestructuredText(document))
```

Sections: Highlights, Python API, Command Line Interface, Compatibility, Documentation

</details>

### requests-file

File transport adapter for Requests

`pip install requests-file` · installs (wheel) · licence: Apache Software License · rank 369 · last release 2025-10-20 · [PyPI](https://pypi.org/project/requests-file/)

<details><summary>README extract</summary>

Requests-File is a transport adapter for use with the Requests Python
library to allow local filesystem access via file:\/\/ URLs.

To use:

Features:
- Will open and read local files
- Might set a Content-Length header
- That's about it

No encoding information is set in the response object, so be careful using
Response.text: the chardet library will be used to convert the file to a
unicode type ...

Example:
```python
import requests
from requests_file import FileAdapter

s = requests.Session()
s.mount('file://', FileAdapter())

resp = s.get('file:///path/to/file')
```

Sections: Requests-File, Features

</details>

### rfc3986-validator

Pure python rfc3986 validator

`pip install rfc3986-validator` · installs (wheel) · licence: MIT License · rank 527 · last release 2019-10-28 · [PyPI](https://pypi.org/project/rfc3986-validator/)

<details><summary>README extract</summary>

A pure python RFC3986 validator

Example:
```python
>>> from rfc3986_validator import validate_rfc3986
>>> validate_rfc3986(' should be encoded')
False

>>> validate_rfc3986('
True
```

Sections: rfc3986-validator, Usage

</details>

### rignore

Python Bindings for the ignore crate

`pip install rignore` · installs (wheel) · licence: MIT · rank 552 · last release 2026-08-04 · [PyPI](https://pypi.org/project/rignore/)

<details><summary>README extract</summary>

`rignore` is a Python module that provides a high-performance, Rust-powered file system traversal functionality. It wraps the Rust `ignore` crate using PyO3, offering an efficient way to walk through directories while respecting various ignore rules.

- 🚀 Fast directory traversal powered by Rust
- 🙈 Respects `.gitignore` rules ...

Example:
```python
import rignore

for file_path in rignore.walk("/path/to/directory"):
    print(file_path)
```

Sections: rignore 🚀🐍, ✨ Features, 🚀 Usage, 🔧 Advanced Usage, 📝 Parameters, ⚡ Performance

</details>

### realtime

(no summary)

`pip install realtime` · installs (wheel) · licence: MIT · rank 639 · last release 2026-11-06 · [PyPI](https://pypi.org/project/realtime/) · [docs](https://github.com/supabase/supabase/tree/main/src/realime) · [source](https://github.com/supabase/supabase-py)

<details><summary>README extract</summary>

Guides
 Reference Docs
 Multiplayer Demo

Features:
This client enables you to use the following Supabase Realtime's features:

- Broadcast: send ephemeral messages from client to clients with minimal latency. Use cases include sharing cursor positions between users. ...

Example:
```python
import asyncio
from typing import Optional

from realtime import AsyncRealtimeClient, RealtimeSubscribeStates

async def main():
    REALTIME_URL = "ws://localhost:4000/websocket"
    API_KEY = "1234567890"

    client = AsyncRealtimeClient(REALTIME_URL, API_KEY)
    channel = client.channel("test-channel")

...
```

...

</details>

### respx

A utility for mocking out the Python HTTPX and HTTP Core libraries.

`pip install respx` · installs (wheel) · licence: BSD License · rank 652 · last release 2026-04-08 · [PyPI](https://pypi.org/project/respx/) · [source](https://github.com/lundberg/respx)

<details><summary>README extract</summary>

RESPX - Mock HTTPX with awesome request patterns and response side effects.

Full documentation is available at
lundberg.github.io/respx

Example:
```python
import httpx
import respx

from httpx import Response

@respx.mock
def test_example():
    my_route = respx.get("
    response = httpx.get("
    assert my_route.called
    assert response.status_code == 204
```

Sections: Documentation, QuickStart, pytest + httpx

</details>

### rfc3986

Validating URI References per RFC 3986

`pip install rfc3986` · installs (wheel) · licence: Apache Software License · rank 760 · last release 2022-01-10 · [PyPI](https://pypi.org/project/rfc3986/)

<details><summary>README extract</summary>

A Python implementation of RFC 3986 including validation and authority
parsing.

Example:
```python
from rfc3986 import urlparse

ssh = urlparse('ssh://user@git.openstack.org:29418/openstack/glance.git')
print(ssh.scheme)  # => ssh
print(ssh.userinfo)  # => user
print(ssh.params)  # => None
print(ssh.port)  # => 29418
```

Sections: rfc3986, Example Usage, Replacing `urlparse`, Strictly Parsing a URI and Applying Validation, Requiring Components, Alternatives

</details>

### readme-renderer

readme_renderer is a library for rendering readme descriptions for Warehouse

`pip install readme-renderer` · installs (wheel) · licence: Apache-2.0 · rank 927 · last release 2026-08-28 · [PyPI](https://pypi.org/project/readme-renderer/)

<details><summary>README extract</summary>

Readme Renderer is a library that will safely render arbitrary
`README` files into HTML. It is designed to be used in Warehouse to
render the `long_description` for packages. It can handle Markdown,
reStructuredText (`.rst`), and plain text. ...

Sections: Readme Renderer, Check Description Locally

</details>

### ray

Ray provides a simple, universal API for building distributed applications.

`pip install ray` · installs (wheel) · licence: Apache 2.0 · rank 978 · last release 2026-11-04 · [PyPI](https://pypi.org/project/ray/)

<details><summary>README extract</summary>

Ray is a unified framework for scaling AI and Python applications. Ray consists of a core distributed runtime and a set of AI libraries for simplifying ML compute:

Learn more about Ray AI Libraries:

- Data: Scalable Datasets for ML
- Train: Distributed Training
- Tune: Scalable Hyperparameter Tuning
- RLlib: Scalable Reinforcement Learning ...

Features:
Today's ML workloads are increasingly compute-intensive. As convenient as they are, single-node development environments such as your laptop cannot scale to meet these demands. ...

Sections: Why Ray?, More Information, Getting Involved

</details>

### rich-click

Format click help output nicely with rich

`pip install rich-click` · installs (wheel) · licence: not stated · rank 1001 · last release 2026-09-05 · [PyPI](https://pypi.org/project/rich-click/) · [docs](https://github.com/ewels/rich-click) · [source](https://github.com/ewels/rich-click)

<details><summary>README extract</summary>

Richly rendered command line interfaces in click.

 Documentation · Source Code · Changelog

rich-click is a wrapper around Click that renders help output nicely using Rich.

- Click is a _"Python package for creating beautiful command line interfaces"_.
- Rich is a _"Python library for rich text and beautiful formatting in the terminal"_. ...

Features:
- 🌈 Rich command-line formatting of click help and error messages
- 😌 Same API as Click: usage is simply `import rich_click as click`
- 🎨 Over 100 themes that can be set by developers and end-users (`export RICH_CLICK_THEME=...`) ...

Example:
```python
import rich_click as click

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
...

</details>

### resend

Resend Python SDK

`pip install resend` · installs (wheel) · licence: MIT License · rank 1015 · last release 2026-11-05 · [PyPI](https://pypi.org/project/resend/)

<details><summary>README extract</summary>

Example:
```python
import os
import resend

resend.api_key = "re_yourkey"

params: resend.Emails.SendParams = {
    "from": "onboarding@resend.dev",
    "to": ["delivered@resend.dev"],
    "subject": "hi",
    "html": "<strong>hello, world!</strong>",
    "reply_to": "to@gmail.com",
    "bcc": "bcc@resend.dev",
    "cc": ["cc@resend.dev"],
    "tags": [
...
```

Sections: Resend Python SDK, Setup, Example, Custom async client

</details>

### resvg_py

(no summary)

`pip install resvg_py` · installs (wheel) · licence: not stated · rank 1195 · last release 2026-08-24 · [PyPI](https://pypi.org/project/resvg_py/) · [docs](https://resvg-py.readthedocs.io/) · [source](https://github.com/baseplate-admin/resvg-py)

<details><summary>README extract</summary>

A safe and high level binding for the resvg project

Sections: resvg_py, Requires

</details>

### roman-numerals

Manipulate well-formed Roman numerals

`pip install roman-numerals` · installs (wheel) · licence: 0BSD OR CC0-1.0 · rank 1251 · last release 2025-12-17 · [PyPI](https://pypi.org/project/roman-numerals/) · [source](https://github.com/AA-Turner/roman-numerals/)

<details><summary>README extract</summary>

A library for manipulating well-formed Roman numerals.

Integers between 1 and 3,999 (inclusive) are supported.
Numbers beyond this range will return an `OutOfRangeError`.

The classical system of roman numerals requires that
the same character may not appear more than thrice consecutively,
meaning that 'MMMCMXCIX' (3,999) is the largest ...

Example:
```python
from roman_numerals import RomanNumeral

num = RomanNumeral(16)
assert str(num) == 'XVI'

num = RomanNumeral.from_string("XVI")
assert int(num) == 16
```

Sections: roman-numerals, Example usage, Creating a roman numeral, Convert a roman numeral to a string, Extract the decimal value of a roman numeral, Invalid input

</details>

### rank-bm25

Various BM25 algorithms for document ranking

`pip install rank-bm25` · installs (wheel) · licence: Apache2.0 · rank 1309 · last release 2022-02-16 · [PyPI](https://pypi.org/project/rank-bm25/)

<details><summary>README extract</summary>

A collection of algorithms for querying a set of documents and returning the ones most relevant to the query. The most common use case for these algorithms is, as you might have guessed, to create search engines.

So far the algorithms that have been implemented are:
- [x] Okapi BM25
- [x] BM25L
- [x] BM25+
- [ ] BM25-Adpt
- [ ] BM25T ...

Example:
```python
from rank_bm25 import BM25Okapi

corpus = [
    "Hello there good man!",
    "It is quite windy in London",
    "How is the weather today?"
]

tokenized_corpus = [doc.split(" ") for doc in corpus]

bm25 = BM25Okapi(tokenized_corpus)
# <rank_bm25.BM25Okapi at 0x1047881d0>
```

Sections: Rank-BM25: A two line search engine, Usage, Initalizing, Ranking of documents

</details>

### rlp

rlp: A package for Recursive Length Prefix encoding and decoding

`pip install rlp` · installs (wheel) · licence: MIT · rank 1425 · last release 2026-08-21 · [PyPI](https://pypi.org/project/rlp/) · [docs](https://pyrlp.readthedocs.io/) · [source](https://github.com/ApeWorX/pyrlp.git)

<details><summary>README extract</summary>

A package for Recursive Length Prefix encoding and decoding

Read the documentation.

View the change log.

</details>

### red-black-tree-mod

Flexible python implementation of red black trees

`pip install red-black-tree-mod` · installs from source (sdist only) · licence: MIT · rank 1448 · last release 2023-12-26 · [PyPI](https://pypi.org/project/red-black-tree-mod/)

<details><summary>README extract</summary>

A pair of python modules implementing red black trees is provided.

Red-black trees are a little slower than treaps (some question this), but they give a nice
low standard deviation in operation times, and this code is rather flexible.

A module is provided for red black trees that enforce uniqueness. ...

</details>

### requests-ntlm

This package allows for HTTP NTLM authentication using the requests library.

`pip install requests-ntlm` · installs (wheel) · licence: ISC License (ISCL) · rank 1519 · last release 2024-06-09 · [PyPI](https://pypi.org/project/requests-ntlm/)

<details><summary>README extract</summary>

This package allows for HTTP NTLM authentication using the requests library.

Example:
```python
import requests
from requests_ntlm import HttpNtlmAuth

requests.get("
```

Sections: requests-ntlm, Usage, Requirements

</details>

### rdkit

A collection of chemoinformatics and machine-learning software written in C++ and Python

`pip install rdkit` · installs (wheel) · licence: BSD-3-Clause · rank 1522 · last release 2026-10-09 · [PyPI](https://pypi.org/project/rdkit/)

<details><summary>README extract</summary>

This repository holds the code to build RDKit platform wheels for Linux, macOS, and Windows on Github Action and Circle CI. The wheels contain the compiled platform-specific dynamic libraries (`*.so`, `*.dylib`, and `*.dll`) and are available at PyPI. RDKit can easily be installed using ...

Sections: 🔥 RDKit Python Wheels, Available Builds, PIP, uv, Local builds on Linux

</details>

### rustworkx

A High-Performance Graph Library for Python

`pip install rustworkx` · installs (wheel) · licence: Apache-2.0 · rank 1545 · last release 2026-07-30 · [PyPI](https://pypi.org/project/rustworkx/) · [docs](https://www.rustworkx.org/) · [source](https://github.com/Qiskit/rustworkx)

<details><summary>README extract</summary>

A high-performance, general-purpose graph library for Python, written in Rust.

Example:
```python
import rustworkx

# Rustworkx's undirected graph type.
graph = rustworkx.PyGraph()

# Each time add node is called, it returns a new node index
a = graph.add_node("A")
b = graph.add_node("B")
c = graph.add_node("C")

# add_edges_from takes tuples of node indices and weights,
# and returns edge indices
...
```

Sections: rustworkx, Usage, Optional dependencies, Conda Ecosystem, rustworkx. You can join the, Building from source

</details>

### rapidocr

Awesome OCR Library

`pip install rapidocr` · installs (wheel) · licence: Apache-2.0 · rank 1750 · last release 2026-10-08 · [PyPI](https://pypi.org/project/rapidocr/) · [docs](https://rapidai.github.io/RapidOCRDocs)

### rouge-score

Pure python implementation of ROUGE-1.5.5.

`pip install rouge-score` · installs from source (sdist only) · licence: Apache Software License · rank 1821 · last release 2022-07-22 · [PyPI](https://pypi.org/project/rouge-score/)

<details><summary>README extract</summary>

Features:
This is a native python implementation of ROUGE, designed to replicate results
from the original perl package.

Maintainers may be contacted at rouge-opensource@google.com.

ROUGE was originally introduced in the paper:

Lin, Chin-Yew. ...

Example:
```python
from rouge_score import rouge_scorer

scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
scores = scorer.score('The quick brown fox jumps over the lazy dog',
                      'The quick brown dog jumps on the log.')
```

Sections: Python ROUGE Implementation, Overview, ROUGE for Python, Stopword removal, Two flavors of ROUGE-L, How to run, Using pip, Disclaimer

</details>

### regress

Python bindings to Rust's regress ECMA regular expressions library

`pip install regress` · installs (wheel) · licence: MIT · rank 1852 · last release 2026-09-05 · [PyPI](https://pypi.org/project/regress/) · [source](https://github.com/crate-py/regress)

<details><summary>README extract</summary>

Python bindings to the Rust regress crate, exposing ECMA regular expressions.

Example:
```python
>>> from regress import Regex
>>> regex = Regex(r"\d{4}")
>>> regex.find("2020-20-05") is not None
True
```

</details>

### requests-futures

Asynchronous Python HTTP for Humans.

`pip install requests-futures` · installs (wheel) · licence: Apache-2.0 · rank 2063 · last release 2026-08-29 · [PyPI](https://pypi.org/project/requests-futures/) · [source](https://github.com/ross/requests-futures)

<details><summary>README extract</summary>

Small add-on for the python requests http library that makes use of the
standard library's concurrent.futures. Requires Python 3.10 or newer.

The additional API and changes are minimal and strives to avoid surprises.

The following synchronous code: ...

Example:
```python
from requests import Session

session = Session()
# first requests starts and blocks until finished
response_one = session.get('
# second request starts once first is finished
response_two = session.get('
# both requests are complete
print('response one status: {0}'.format(response_one.status_code))
print(response_one.content)
...
```

Sections: Asynchronous Python HTTP Requests for Humans, Tying extra information to the request/response, Using ProcessPoolExecutor, Documentation

</details>

### runs

🏃 Run a block of text as a subprocess 🏃

`pip install runs` · installs (wheel) · licence: MIT · rank 2082 · last release 2026-02-03 · [PyPI](https://pypi.org/project/runs/)

<details><summary>README extract</summary>

`runs` has improved versions of `call()`, `check_call()`, `check_output()`,
and `run()` from Python's `subprocess` module that handle multiple commands and
blocks of text, fix some defects, and add some features.

`subprocess` is essential but:

* You can only run one command at a time ...

Example:
```python
import runs

runs('''
    ls
    df -k  # or perhaps -h?
    echo 'Done and done'
''')
```

Sections: 🏃 runs: a better subprocess 🏃, API, `runs()`, `runs.call()`, `runs.check_call()`, `runs.check_output()`

</details>

### rapidocr-onnxruntime

A cross platform OCR Library based on OnnxRuntime.

`pip install rapidocr-onnxruntime` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 2143 · last release 2025-01-17 · [PyPI](https://pypi.org/project/rapidocr-onnxruntime/) · [docs](https://rapidai.github.io/RapidOCRDocs)

### renderers

Chat template renderers — deterministic message-to-token conversion for LLM training

`pip install renderers` · installs (wheel) · licence: Apache-2.0 · rank 2190 · last release 2026-10-29 · [PyPI](https://pypi.org/project/renderers/)

<details><summary>README extract</summary>

Programmable chat templates for LLM training and inference. A renderer turns a model's chat template into a Python object that can render messages → token ids, parse completion ids → structured assistant messages, and extend a multi-turn rollout without re-rendering model-sampled history. ...

Features:
For RL the trainer must see the exact token ids the sampler saw. The standard alternative — let the inference engine apply the chat template, parse tool calls, parse reasoning, and re-render full history every turn — silently breaks token identity. ...

Example:
```python
from renderers import create_renderer
from renderers.base import load_tokenizer

tok = load_tokenizer("Qwen/Qwen3-8B")              # renderers[transformers]
...

</details>

### rfc3161-client

(no summary)

`pip install rfc3161-client` · installs (wheel) · licence: Apache Software License · rank 2366 · last release 2026-09-14 · [PyPI](https://pypi.org/project/rfc3161-client/) · [docs](https://trailofbits.github.io/rfc3161-client/) · [source](https://github.com/trailofbits/rfc3161-client)

<details><summary>README extract</summary>

`rfc3161-client` is a Python library implementing the Time-Stamp Protocol (TSP)
described in RFC 3161.

It is composed of three subprojects:

- :crab: tsp-asn1: A Rust crate using
 `rust-asn1` to create the
 types used by the Time-Stamp protocol. This crate depends on `rust-asn1`
 and `cryptography` to minimize the amount of duplicated code. ...

Example:
```python
# /// script
# dependencies = [
# "requests",
# "rfc3161-client",
# ]
# ///
import requests
from rfc3161_client import (
    decode_timestamp_response,
    TimestampRequestBuilder,
    VerifierBuilder,
    VerificationError,
)

# the data to sign. Could be a hash or any message. Should be bytes
message = b"Hello, World!"

...
```

...

</details>

### result

A Rust-like result type for Python

`pip install result` · installs (wheel) · licence: MIT License · rank 2447 · last release 2024-06-02 · [PyPI](https://pypi.org/project/result/)

<details><summary>README extract</summary>

A simple Result type for Python 3 inspired by
Rust, fully type annotated.

Example:
```python
def get_user_by_email(email: str) -> Tuple[Optional[User], Optional[str]]:
    """
    Return the user instance or an error message.
    """
    if not user_exists(email):
        return None, 'User does not exist'
    if not user_active(email):
        return None, 'User is inactive'
    user = get_user(email)
    return user, None

...
```

Sections: Result, Summary, API, `as_result` Decorator, Do notation, FAQ, Related Projects

</details>

### redis-py-cluster

Library for communicating with Redis Clusters. Built on top of redis-py lib

`pip install redis-py-cluster` · installs (wheel) · licence: MIT License · rank 2494 · last release 2021-05-30 · [PyPI](https://pypi.org/project/redis-py-cluster/)

<details><summary>README extract</summary>

This client provides a client for redis cluster that was added in redis 3.0.

This project is a port of `redis-rb-cluster` by antirez, with a lot of added functionality. The original source can be found at

The branch `master` will always contain the latest unstable/development code that has been merged from Pull Requests. ...

Example:
```python
>>> from rediscluster import RedisCluster

>>> # Requires at least one node for cluster discovery. Multiple nodes is recommended.
>>> startup_nodes = [{"host": "127.0.0.1", "port": "7000"}, {"host": "127.0.0.1", "port": "7001"}]
>>> rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

...
```

Sections: redis-py-cluster, Python 2 Compatibility Note, Documentation, Usage example

</details>

### requests-aws-sign

This package provides AWS V4 request signing using the requests library.

`pip install requests-aws-sign` · installs (wheel) · licence: ISC License (ISCL) · rank 2598 · last release 2020-07-05 · [PyPI](https://pypi.org/project/requests-aws-sign/)

### readerwriterlock

A python implementation of the three Reader-Writer problems.

`pip install readerwriterlock` · installs (wheel) · licence: MIT License · rank 2687 · last release 2026-10-13 · [PyPI](https://pypi.org/project/readerwriterlock/) · [source](https://github.com/elarivie/pyReaderWriterLock)

<details><summary>README extract</summary>

A python implementation of a solution for the three Reader-Writer problems.

[][pyReaderWriterLock_BugTracker]

[][python]
[][pyReaderWriterLock_Pypi]

[][pyReaderWriterLock_repo]
[][pyReaderWriterLock_License]

[][pyReaderWriterLock_repo_star] ...

Example:
```python
from readerwriterlock import rwlock
a = rwlock.RWLockFairD()
```

Sections: Reader Writer Lock, Usage, Pythonic usage example, Use case (Timeout) example, Use case (Downgrade) example, Live example

</details>

### requests-unixsocket

Use requests to talk HTTP via a UNIX domain socket

`pip install requests-unixsocket` · installs (wheel) · licence: not stated · rank 2982 · last release 2025-03-07 · [PyPI](https://pypi.org/project/requests-unixsocket/)

<details><summary>README extract</summary>

Use requests to talk HTTP via a UNIX domain socket

Example:
```python
import json

import requests_unixsocket

session = requests_unixsocket.Session()

r = session.get('http+unix://%2Fvar%2Frun%2Fdocker.sock/info')
registry_config = r.json()['RegistryConfig']
print(json.dumps(registry_config, indent=4))
```

Sections: requests-unixsocket, Usage, Explicit, Implicit (monkeypatching), Abstract namespace sockets, See also

</details>

### ratelim

Makes it easy to respect rate limits.

`pip install ratelim` · installs (wheel) · licence: MIT · rank 3080 · last release 2015-02-27 · [PyPI](https://pypi.org/project/ratelim/)

<details><summary>README extract</summary>

Ratelim is a simple Python library that limits the number of times a function can be called during a time interval. It is particularly useful when using online APIs, which commonly enforce rate limits.

Features:
- Works in Py2 and Py3.
- Greedy and patient rate limiting.
- Preserves function signature.

Example:
```python
# 10 times in 5 seconds
@ratelim.greedy(10, 5)
def hello():
    print("hello")
```

Sections: Ratelim, Features, Usage

</details>

### redisvl

Python client library and CLI for using Redis as a vector database

`pip install redisvl` · installs (wheel) · licence: MIT · rank 3111 · last release 2026-11-06 · [PyPI](https://pypi.org/project/redisvl/) · [docs](https://docs.redisvl.com) · [source](https://github.com/redis/redis-vl-python)

<details><summary>README extract</summary>

The AI-native Redis Python client

Documentation • Recipes • GitHub

Redis Vector Library (RedisVL) is the production-ready Python client for AI applications built on Redis. Lightning-fast vector search meets enterprise-grade reliability. ...

Example:
```python
from redisvl.schema import IndexSchema

schema = IndexSchema.from_yaml("schemas/schema.yaml")
```

Sections: Redis Vector Library, Introduction, 💪 Getting Started, Redis, Overview, Index Management, Retrieval, Vector Search, Complex Filtering, Hybrid Search, Dev Utilities, Vectorizers, Rerankers, Extensions

</details>

### roman-numerals-py

This package is deprecated, switch to roman-numerals.

`pip install roman-numerals-py` · installs (wheel) · licence: 0BSD OR CC0-1.0 · rank 3146 · last release 2025-12-17 · [PyPI](https://pypi.org/project/roman-numerals-py/) · [source](https://github.com/AA-Turner/roman-numerals/)

<details><summary>README extract</summary>

This package is deprecated, switch to roman-numerals.

</details>

### requests-sigv4

Library for making sigv4 requests to AWS API endpoints

`pip install requests-sigv4` · installs (wheel) · licence: Apache Software License · rank 3191 · last release 2022-06-24 · [PyPI](https://pypi.org/project/requests-sigv4/)

<details><summary>README extract</summary>

Library for making sigv4 requests to AWS API endpoints

</details>

### replicate

Python client for Replicate

`pip install replicate` · installs (wheel) · licence: not stated · rank 3418 · last release 2025-05-27 · [PyPI](https://pypi.org/project/replicate/) · [source](https://github.com/replicate/replicate-python)

<details><summary>README extract</summary>

This is a Python client for Replicate. It lets you run models from your Python code or Jupyter notebook, and do various other things on Replicate.

The 1.0.0 release contains breaking changes:

- The `replicate.run()` method now returns `FileOutput`s instead of URL strings by default for models that output files. ...

Example:
```python
output = replicate.run("acmecorp/acme-model", use_file_output=False)
```

Sections: Replicate Python client, Breaking Changes in 1.0.0, Requirements, Authenticate, Run a model, Run a model and stream its output, Run a model in the background, Run a model in the background and get a webhook, Compose models into a pipeline, Get output from a running model, Cancel a prediction, List predictions, Load output files, FileOutput

</details>

### readability-lxml

fast html to text parser (article readability tool) with python 3 support

`pip install readability-lxml` · installs (wheel) · licence: Apache Software License · rank 3426 · last release 2026-08-27 · [PyPI](https://pypi.org/project/readability-lxml/)

<details><summary>README extract</summary>

Given an HTML document, extract and clean up the main body text and title.

This is a Python port of a Ruby port of arc90's Readability project.

Example:
```python
>>> import requests
>>> from readability import Document

>>> response = requests.get('
>>> doc = Document(response.content)
>>> print(doc.title())
Example Domain

>>> print(doc.summary())

# Example Domain

This domain is established to be used for illustrative examples in documents. You may
...
```

Sections: python-readability, Usage, Licensing, Thanks to

</details>

### redo

Utilities to retry Python callables.

`pip install redo` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 3433 · last release 2026-10-05 · [PyPI](https://pypi.org/project/redo/)

<details><summary>README extract</summary>

Redo provides various means to add seamless ability to retry to any Python callable. Redo includes plain functions (`redo.retry`, `redo.retry_async`), decorators (`redo.retriable`, `redo.retriable_async`), and a context manager (`redo.retrying`) to enable you to integrate it in the best possible way for your project. ...

Example:
```python
>>> n = 0
>>> for _ in retrier(sleeptime=0, jitter=0):
...     if n == 3:
...         # We did the thing!
...         break
...     n += 1
>>> n
3
>>> n = 0
>>> for _ in retrier(sleeptime=0, jitter=0):
...     if n == 6:
...         # We did the thing!
...         break
...     n += 1
... else:
...     print("max tries hit")
max tries hit
```

...

</details>

### Resiliparse

A collection of robust and fast processing tools for parsing and analyzing (not only) web archive data.

`pip install Resiliparse` · installs (wheel) · licence: Apache-2.0 · rank 3504 · last release 2026-11-04 · [PyPI](https://pypi.org/project/Resiliparse/) · [docs](https://resiliparse.chatnoir.eu) · [source](https://github.com/chatnoir-eu/chatnoir-resiliparse)

<details><summary>README extract</summary>

A collection of robust and fast processing tools for parsing and analyzing web archive data written in Rust with
bindings for Python.

This package contains the Python bindings for Resiliparse, including HTML parsing and DOM manipulation, text extraction,
encoding and language detection, HTTP parsing, process guards, and Apache Beam utilities. ...

Sections: Resiliparse (Python), Building Python Bindings From Source, Usage Instructions

</details>

### randomname

Generate random adj-noun names like docker and github.

`pip install randomname` · installs from source (sdist only) · licence: MIT License · rank 3612 · last release 2023-01-29 · [PyPI](https://pypi.org/project/randomname/)

<details><summary>README extract</summary>

Generate random unique ids using real words - like docker containers or github repos.

Often, I get tired of trying to hunt down files in folders differentiated by some numeric id, and unless I need to encode a timestep into the name, I'd rather use an id that's memorable and easy to type.

The wordlists are graciously sourced from: ...

Example:
```python
import randomname

# generate name using all categories
name = randomname.get_name()
# or specify a subset of the categories
name = randomname.get_name(adj=('music_theory',), noun=('cats', 'food'))
# or - you can take a bit more liberty about
name = randomname.generate(
    'v/fire', 'adj/music_theory', ('n/cats', 'n/food'))

...
```

Sections: randomname, Usage, It's importable too!, Available, Examples

</details>

### ragas

Evaluation framework for RAG and LLM applications

`pip install ragas` · installs (wheel) · licence: not stated · rank 3742 · last release 2026-01-13 · [PyPI](https://pypi.org/project/ragas/) · [docs](https://docs.ragas.io) · [source](https://github.com/vibrantlabsai/ragas)

<details><summary>README extract</summary>

Supercharge Your LLM Application Evaluations 🚀

 Documentation |
 Quick start |
 Join Discord |
 Blog |
 NewsLetter |
 Careers

Objective metrics, intelligent test generation, and data-driven insights for LLM apps

Ragas is your ultimate toolkit for evaluating and optimizing Large Language Model (LLM) applications. ...

Features:
- 🎯 Objective Metrics: Evaluate your LLM applications with precision using both LLM-based and traditional metrics.
- 🧪 Test Data Generation: Automatically create comprehensive test datasets covering a wide range of scenarios. ...

Example:
```python
import asyncio
from ragas.metrics.collections import AspectCritic
from ragas.llms import llm_factory

# Setup your LLM
llm = llm_factory("gpt-4o")

# Create a metric
metric = AspectCritic(
    name="summary_accuracy",
...

</details>

### roman

Integer to Roman numerals converter

`pip install roman` · installs (wheel) · licence: Zope Public License · rank 3938 · last release 2025-11-11 · [PyPI](https://pypi.org/project/roman/)

<details><summary>README extract</summary>

Small helper library to convert arabic to roman numerals.

There are two ways to use this library.

1. Importing it into your application

2. `roman` CLI command

Example:
```python
import roman

# to roman
number = int(input('> ')) # 10
print(roman.toRoman(number))

# from roman
number = input('> ') # X
print(roman.fromRoman(number))
```

Sections: roman, 5.2 (2025-11-11), 5.1 (2025-07-18), 5.0 (2025-01-15), 4.2 (2024-04-25), 4.1 (2023-05-26), 4.0 (2023-02-28), 3.3 (2020-07-12), 3.2 (2019-04-14), 3.1 (2018-10-24), 3.0 (2018-05-28), 2.0.0 (2013-02-25), 1.4.0 (2009-07-23)

</details>

### robust-downloader

A Simple Robust Downloader written in Python

`pip install robust-downloader` · installs (wheel) · licence: Apache Software License · rank 4024 · last release 2023-11-13 · [PyPI](https://pypi.org/project/robust-downloader/)

<details><summary>README extract</summary>

A minimal Python downloader with robustness in mind - resumable downloads, retries, and more.

Example:
```python
from robust_downloader import download

download("
```

Sections: Robust Downloader, Usage, From Python, From CLI, Available Arguments

</details>

### readabilipy

Python wrapper for Mozilla's Readability.js

`pip install readabilipy` · installs (wheel) · licence: MIT License · rank 4118 · last release 2024-12-02 · [PyPI](https://pypi.org/project/readabilipy/)

<details><summary>README extract</summary>

`ReadabiliPy` contains a Python wrapper for Mozilla's Readability.js Node.js package, as well as article extraction routines written in pure Python.

This package augments the output of `Readability.js` to also return a list of plain text representations of article paragraphs. ...

Example:
```python
>>> import requests
>>> from readabilipy import simple_json_from_html_string
>>> req = requests.get('
>>> article = simple_json_from_html_string(req.text, use_readability=True)
```

Sections: ReadabiliPy, Usage, Command line application, Library, Notes

</details>

### robosuite

robosuite: A Modular Simulation Framework and Benchmark for Robot Learning

`pip install robosuite` · installs (wheel) · licence: not stated · rank 4244 · last release 2025-12-24 · [PyPI](https://pypi.org/project/robosuite/)

<details><summary>README extract</summary>

[[Homepage]]( &ensp; [[White Paper]]( &ensp; [[Documentations]]( &ensp; [[ARISE Initiative]](

- [10/28/2024] v1.5: Added support for diverse robot embodiments (including humanoids), custom robot composition, composite controllers (including whole body controllers), more teleoperation devices, photo-realistic rendering. ...

Sections: robosuite, Latest Updates

</details>

### requests-auth-aws-sigv4

AWS SigV4 Authentication with the python requests module

`pip install requests-auth-aws-sigv4` · installs (wheel) · licence: Apache Software License · rank 4246 · last release 2021-02-16 · [PyPI](https://pypi.org/project/requests-auth-aws-sigv4/)

<details><summary>README extract</summary>

Use AWS signature version 4 Authentication with the python requests module

This package provides an authentication class that can be used with the popular
requests package to add the
AWS Signature Version 4
authentication information.

The signing code is inspired by the python example provided by AWS. ...

Example:
```python
import requests
from requests_auth_aws_sigv4 import AWSSigV4

r = requests.request('POST', '
    data=dict(Version='2011-06-15', Action='GetCallerIdentity'),
    auth=AWSSigV4('sts'))
print(r.text)
```

Sections: requests-auth-aws-sigv4, Usage, Example using environment variables, Example using parameters, Usage with Elasticsearch Client (elasticsearch-py), Debug Logging, Command Line Usage

</details>

### recordlinkage

A record linkage toolkit for linking and deduplication

`pip install recordlinkage` · installs (wheel) · licence: BSD License · rank 4285 · last release 2023-07-20 · [PyPI](https://pypi.org/project/recordlinkage/) · [source](https://github.com/J535D165/recordlinkage)

<details><summary>README extract</summary>

RecordLinkage is a powerful and modular record linkage toolkit to
link records in or between data sources. The toolkit provides most of
the tools needed for record linkage and deduplication. The package
contains indexing methods, functions to compare records and classifiers. ...

Example:
```python
import recordlinkage
import pandas
```

Sections: Basic linking example, Main Features, Documentation, Need help?

</details>

### requests-kerberos

A Kerberos authentication handler for python-requests

`pip install requests-kerberos` · installs (wheel) · licence: ISC License (ISCL) · rank 4313 · last release 2024-06-03 · [PyPI](https://pypi.org/project/requests-kerberos/)

<details><summary>README extract</summary>

Requests is an HTTP library, written in Python, for human beings. This library
adds optional Kerberos/GSSAPI authentication support and supports mutual
authentication. Basic GET usage:

The entire `requests.api` should be supported.

Example:
```python
>>> import requests
>>> from requests_kerberos import HTTPKerberosAuth
>>> r = requests.get(" auth=HTTPKerberosAuth())
...
```

Sections: requests Kerberos/GSSAPI authentication library, Setup, Authentication Failures, Mutual Authentication, REQUIRED, OPTIONAL, DISABLED, Preemptive Authentication, Hostname Override, Explicit Principal, Password Authentication, Delegation, Logging, Channel Binding

</details>

### redis-entraid

Entra ID credentials provider implementation for Redis-py client

`pip install redis-entraid` · installs (wheel) · licence: not stated · rank 4352 · last release 2026-10-08 · [PyPI](https://pypi.org/project/redis-entraid/)

<details><summary>README extract</summary>

Note: redis-py-entraid 1.0.0 is the last version of redis-py that supports Python 3.9, as it has reached end of life. redis-py-entraid 1.1.0 supports Python 3.9+.

The `redis-entraid` Python package helps simplifying the authentication with Azure Managed Redis and Azure Cache for Redis using Microsoft Entra ID (formerly Azure Active Directory). ...

Example:
```python
credential_provider = create_from_managed_identity(
    identity_type=ManagedIdentityType.SYSTEM_ASSIGNED,
    resource="
)
```

Sections: Preparation, Create a service principal in Azure, Create cache and grant access, Usage, Step 1 - Import the dependencies, Examples, Step 3 - Provide optional token renewal configuration, Step 4 - Connect to Redis

</details>

### rpmfile

Read rpm archive files

`pip install rpmfile` · installs (wheel) · licence: MIT · rank 4378 · last release 2026-05-06 · [PyPI](https://pypi.org/project/rpmfile/) · [source](https://github.com/srossross/rpmfile)

<details><summary>README extract</summary>

Tools for inspecting RPM files in python. This module is modeled after the
tarfile module.

Example:
```python
import rpmfile

with rpmfile.open('file.rpm') as rpm:

    # Inspect the RPM headers
    print(rpm.headers.keys())
    print(rpm.headers.get('arch', 'noarch'))

    # Extract a fileobject from the archive
    fd = rpm.extractfile('./usr/bin/script')
    print(fd.read())

    for member in rpm.getmembers():
        print(member)
```

Sections: rpmfile, Example, Command line usage, Classes, Code in this module was borrowed from

</details>

### reportportal-client

Python client for ReportPortal v5.

`pip install reportportal-client` · installs (wheel) · licence: Apache-2.0 · rank 4476 · last release 2026-10-26 · [PyPI](https://pypi.org/project/reportportal-client/)

<details><summary>README extract</summary>

Library used only for implementors of custom listeners for ReportPortal

- PyTest Framework
- Robot Framework
- Behave Framework
- Nose Framework (archived)

Example:
```python
import os
import subprocess
from mimetypes import guess_type

from reportportal_client import RPClient
from reportportal_client.helpers import timestamp

endpoint = "
project = "default"
# You can get UUID from user profile page in the ReportPortal.
api_key = "1adf271d-505f-44a8-ad71-0afbdf8c83bd"
launch_name = "Test launch"
...
```

Sections: ReportPortal python client, Already implemented listeners, Usage, Send attachment (screenshots), Copyright Notice

</details>

### requests-ratelimiter

Rate-limiting for the requests library

`pip install requests-ratelimiter` · installs (wheel) · licence: MIT · rank 4627 · last release 2026-04-22 · [PyPI](https://pypi.org/project/requests-ratelimiter/) · [docs](https://requests-ratelimiter.readthedocs.io) · [source](https://github.com/JWCook/requests-ratelimiter)

<details><summary>README extract</summary>

This package is a simple wrapper around pyrate-limiter
that adds convenient integration with the requests library.

Full project documentation can be found at requests-ratelimiter.readthedocs.io.

Features:
* `pyrate-limiter` is a general-purpose rate-limiting library that implements the leaky bucket
 algorithm, supports multiple rate limits, and has optional persistence with SQLite and Redis
 backends
* `requests-ratelimiter` adds some conveniences ...

Example:
```python
from requests import Session
from requests_cache import CacheMixin
from requests_ratelimiter import LimiterMixin, SQLiteBucket

class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    """
    Session class with caching and rate-limiting behavior. Accepts arguments for both
...

</details>

### reuse

reuse is a tool for compliance with the REUSE recommendations.

`pip install reuse` · installs (wheel) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication; DFSG approved; OSI Approve · rank 4678 · last release 2026-10-30 · [PyPI](https://pypi.org/project/reuse/) · [docs](https://reuse.readthedocs.org/) · [source](https://codeberg.org/fsfe/reuse-tool)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: 2017 Free Software Foundation Europe e.V. <

SPDX-License-Identifier: CC-BY-SA-4.0

reuse is a tool for compliance with the REUSE
recommendations.

- Documentation: < and <
- Source code: <
- PyPI: <
- REUSE: 3.3
- Python: 3.10+

Sections: reuse, Background, Dependencies, Usage, CLI, Example demo, Run in Docker, Run as pre-commit hook, Shell completion, Licensing

</details>

### requests-unixsocket2

Use requests to talk HTTP via a UNIX domain socket

`pip install requests-unixsocket2` · installs (wheel) · licence: ISC License (ISCL) · rank 4691 · last release 2025-09-03 · [PyPI](https://pypi.org/project/requests-unixsocket2/) · [source](https://gitlab.com/thelabnyc/requests-unixsocket2)

<details><summary>README extract</summary>

Use requests to talk HTTP via a UNIX domain socket.

Example:
```python
import json

import requests_unixsocket

session = requests_unixsocket.Session()

r = session.get('http+unix://%2Fvar%2Frun%2Fdocker.sock/info')
registry_config = r.json()['RegistryConfig']
print(json.dumps(registry_config, indent=4))
```

Sections: requests-unixsocket2, Usage, Explicit, Implicit (monkeypatching), Abstract namespace sockets, See also

</details>

### ruamel.yaml.jinja2

jinja2 pre and post-processor to update with YAML

`pip install ruamel.yaml.jinja2` · installs (wheel) · licence: MIT License · rank 4762 · last release 2021-09-23 · [PyPI](https://pypi.org/project/ruamel.yaml.jinja2/)

<details><summary>README extract</summary>

:version: 0.2.7
:updated: 2021-09-23
:repository:
:pypi:

jinja2 templates for YAML files can normally not be loaded as YAML before
rendering the template. This plugin allows pre and post-processing based on the
round-trip processor. ...

</details>

### rdflib-shim

Shim for rdflib 5 and 6 incompatibilities

`pip install rdflib-shim` · installs (wheel) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication · rank 4833 · last release 2021-12-21 · [PyPI](https://pypi.org/project/rdflib-shim/)

### rev-ai

Rev AI makes speech applications easy to build!

`pip install rev-ai` · installs (wheel) · licence: MIT License · rank 4905 · last release 2024-11-27 · [PyPI](https://pypi.org/project/rev-ai/)

<details><summary>README extract</summary>

See the API docs for more information about the API and
more python examples.

Example:
```python
from rev_ai import apiclient, RevAiApiDeploymentConfigMap, RevAiApiDeployment

# create your client
# optionally configure the Rev AI deployment to use
client = apiclient.RevAiAPIClient("ACCESS TOKEN", url=RevAiApiDeploymentConfigMapRevAiApiDeployment.US)
```

Sections: Rev AI Python SDK, Documentation, Requirements, Usage, Sending a file, Human Transcription, Checking multiple files, Deleting a job, Getting your transcript, Getting transcript summary, Getting captions output, Streamed outputs, Streaming audio, Submitting custom vocabularies

</details>

### ringcentral

RingCentral Python SDK

`pip install ringcentral` · installs (wheel) · licence: not stated · rank 4938 · last release 2025-06-18 · [PyPI](https://pypi.org/project/ringcentral/)

### recommonmark

A docutils-compatibility bridge to CommonMark, enabling you to write CommonMark inside of Docutils & Sphinx projects.

`pip install recommonmark` · installs (wheel) · licence: MIT License · rank 4983 · last release 2020-12-17 · [PyPI](https://pypi.org/project/recommonmark/)

### rangehttpserver

SimpleHTTPServer with support for Range requests

`pip install rangehttpserver` · installs (wheel) · licence: Apache Software License · rank 5006 · last release 2024-08-27 · [PyPI](https://pypi.org/project/rangehttpserver/)

<details><summary>README extract</summary>

SimpleHTTPServer with support for Range requests

Quickstart:

 $ pip install rangehttpserver
 $ python -m RangeHTTPServer
 Serving HTTP on 0.0.0.0 port 8000 ...

See the GitHub repo for more information:

</details>

### robotspy

Robots Exclusion Protocol File Parser

`pip install robotspy` · installs (wheel) · licence: MIT License · rank 5162 · last release 2026-03-01 · [PyPI](https://pypi.org/project/robotspy/)

<details><summary>README extract</summary>

The `robotspy` Python module implements a parser for `robots.txt` files. The recommended class to use is
`robots.RobotsParser`.

A thin facade `robots.RobotFileParser` can also be used as a substitute for `urllib.robotparser.RobotFileParser`,
available in the Python standard library. ...

Example:
```python
(.venv) $ python
>>> import robots
>>> parser = robots.RobotsParser.from_uri('
>>> useragent = 'Nutch'
>>> path = '/brian/'
>>> result = parser.can_fetch(useragent, path)
>>> print(f'Can {useragent} fetch {path}? {result}')
Can Nutch fetch /brian/? True
>>>
```

Sections: Robots Exclusion Standard Parser for Python, Docker Image, Usage, Execute the Tool, Examples, Use the Module in a Project, Bug in the Python standard library, Global Tools

</details>

### ripgrep

ripgrep is a line-oriented search tool that recursively searches the current directory for a regex pattern while respecting gitignore rules. ripgrep has first class support on Windows, macOS and Linux.

`pip install ripgrep` · installs (wheel) · licence: Unlicense OR MIT · rank 5463 · last release 2026-05-24 · [PyPI](https://pypi.org/project/ripgrep/) · [docs](https://github.com/BurntSushi/ripgrep) · [source](https://github.com/BurntSushi/ripgrep)

<details><summary>README extract</summary>

ripgrep (rg)

ripgrep is a line-oriented search tool that recursively searches the current
directory for a regex pattern. By default, ripgrep will respect gitignore rules
and automatically skip hidden files/directories and binary files. ...

Features:
* It can replace many use cases served by other search tools
 because it contains most of their features and is generally faster. ...

Sections: Documentation quick links, Screenshot of search results, Quick examples comparing tools, Why should I use ripgrep?, Why shouldn't I use ripgrep?, Is it really faster than everything else?, Feature comparison, Playground, Building, Running tests, Related tools, Vulnerability reporting, Translations

</details>

### rbloom

Highly optimized Bloom filter that mimics the Python set API, written in Rust

`pip install rbloom` · installs (wheel) · licence: not stated · rank 5490 · last release 2025-09-09 · [PyPI](https://pypi.org/project/rbloom/) · [source](https://github.com/KenanHanke/rbloom)

<details><summary>README extract</summary>

A fast, simple and lightweight
Bloom filter library for
Python, implemented in Rust. It's designed to be as pythonic as possible,
mimicking the built-in `set` type where it can, and works with any
hashable object. ...

Features:
Why should you use this library instead of one of the other
Bloom filter libraries on PyPI?

- Simple: Almost all important methods work exactly like their
 counterparts in the built-in `set`
 type. ...

Example:
```python
>>> from rbloom import Bloom
>>> bf = Bloom(200, 0.01)  # 200 items max, false positive rate of 1%
>>> bf.add("hello")
>>> "hello" in bf
True
>>> "world" in bf
False
>>> bf.update(["hello", "world"])  # "hello" and "world" now in bf
>>> other_bf = Bloom(200, 0.01)

# add some items to other_bf

...
```

...

</details>

### rclone-python

A python wrapper for rclone.

`pip install rclone-python` · installs (wheel) · licence: MIT License · rank 5645 · last release 2026-07-18 · [PyPI](https://pypi.org/project/rclone-python/)

<details><summary>README extract</summary>

A python wrapper for rclone that makes rclone's functionality usable in python.
rclone needs to be installed on the system for the wrapper to work.

Features:
- Copy, move and sync files between remotes
- Delete and prune files/directories
- List files in a directory including properties of the files.
- List available remotes.
- Generate hashes from files or validate them with their hashsum. ...

Example:
```python
from rclone_python import rclone

print(rclone.is_installed())
```

Sections: rclone-python ☁️, Features ⚒️, How to use 💡, Create new remote, Copy, Delete, Prune, Get Hash, Check, Custom config file, Custom Progressbar, Set the log level

</details>

### ratelimiter

Simple python rate limiting object

`pip install ratelimiter` · installs (wheel) · licence: Apache Software License · rank 5715 · last release 2017-12-12 · [PyPI](https://pypi.org/project/ratelimiter/)

<details><summary>README extract</summary>

Simple Python module providing rate limiting.

Features:
This package provides the `ratelimiter` module, which ensures that an
operation will not be executed more than a given number of times on a
given period. ...

Example:
```python
from ratelimiter import RateLimiter

@RateLimiter(max_calls=10, period=1)
def do_something():
    pass
```

Sections: RateLimiter, Overview, Usage, Decorator, Context Manager, Callback, asyncio

</details>

### rules

Awesome Django authorization, without the database

`pip install rules` · installs (wheel) · licence: MIT License · rank 5762 · last release 2024-09-02 · [PyPI](https://pypi.org/project/rules/)

<details><summary>README extract</summary>

`rules` is a tiny but powerful app providing object-level permissions to
Django, without requiring a database. At its core, it is a generic framework
for building rule-based systems, similar to decision trees. It can also be
used as a standalone library in other contexts and frameworks.

Features:
`rules` has got you covered. `rules` is:

- Documented, tested, reliable and easy to use.
- Versatile. Decorate callables to build complex graphs of predicates. ...

Example:
```python
>>> @rules.predicate
>>> def is_book_author(user, book):
...     return book.author == user
...
>>> is_book_author
<Predicate:is_book_author object at 0x10eeaa490>
```

...

</details>

### reverse-geocode

Reverse geocode the given latitude / longitude

`pip install reverse-geocode` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 5777 · last release 2025-05-15 · [PyPI](https://pypi.org/project/reverse-geocode/)

_README extract left out: share-alike licence._

### runai-model-streamer

(no summary)

`pip install runai-model-streamer` · installs (wheel) · licence: not stated · rank 5785 · last release 2026-10-29 · [PyPI](https://pypi.org/project/runai-model-streamer/)

### robotframework-assertion-engine

Generic way to create meaningful and easy to use assertions for the Robot Framework libraries.

`pip install robotframework-assertion-engine` · installs (wheel) · licence: Apache-2.0 · rank 5838 · last release 2026-06-04 · [PyPI](https://pypi.org/project/robotframework-assertion-engine/)

<details><summary>README extract</summary>

Generic way to create meaningful and easy to use assertions for the Robot Framework libraries. This tool is a spin off from the Browser library project, where the Assertion Engine was developed as part of that library.

Example:
```python
def keyword(
    arg_to_get_value: str,
    assertion_operator: Optional[AssertionOperator] = None,
    assertion_expected: Any = None,
    message: str = None,
):
    value = method_to_get_value(arg_to_get_value)
    return verify_assertion(
        value,
        assertion_operator,
        assertion_expected,
        "Prefix message",
...
```

Sections: Assertion Engine, Assertion operator matches return value, Usage

</details>

### rectpack

2D Rectangle packing library

`pip install rectpack` · installs from source (sdist only) · licence: Apache Software License · rank 5944 · last release 2021-11-24 · [PyPI](https://pypi.org/project/rectpack/)

<details><summary>README extract</summary>

A collection of heuristic algorithms for solving the 2D knapsack problem,
also known as the bin packing problem. In essence packing a set of rectangles into the
smallest number of bins.

</details>

### rospkg

ROS package library

`pip install rospkg` · installs (wheel) · licence: BSD License · rank 5992 · last release 2026-09-11 · [PyPI](https://pypi.org/project/rospkg/) · [source](https://github.com/ros-infrastructure/rospkg)

<details><summary>README extract</summary>

Library for retrieving information about ROS packages and stacks.

</details>

### rl-rock

ROCK-Reinforcement Open Construction Kit

`pip install rl-rock` · installs (wheel) · licence: not stated · rank 6037 · last release 2026-07-27 · [PyPI](https://pypi.org/project/rl-rock/)

<details><summary>README extract</summary>

ROCK (Reinforcement Open Construction Kit) is a easy-to-use, and scalable sandbox environment management framework, primarily for agentic reinforcement learning environments. It provides tools for building, managing, and scheduling reinforcement learning environments, suitable for development, testing, and research scenarios. ...

Example:
```python
import asyncio

from rock.actions import CreateBashSessionRequest
from rock.sdk.sandbox.client import Sandbox
from rock.sdk.sandbox.config import SandboxConfig

async def run_sandbox():
    config = SandboxConfig(image="python:3.11", memory="8g", cpus=2.0)
    sandbox = Sandbox(config)

    await sandbox.start()
...
```

...

</details>

### reverse_geocoder

Fast, offline reverse geocoder

`pip install reverse_geocoder` · installs from source (sdist only) · licence: lgpl · rank 6039 · last release 2016-09-15 · [PyPI](https://pypi.org/project/reverse_geocoder/)

_README extract left out: share-alike licence._

### rsl-rl-lib

Fast and simple RL algorithms implemented in PyTorch

`pip install rsl-rl-lib` · installs (wheel) · licence: BSD-3-Clause · rank 6125 · last release 2026-10-28 · [PyPI](https://pypi.org/project/rsl-rl-lib/)

<details><summary>README extract</summary>

RSL-RL is a GPU-accelerated, lightweight learning library for robotics research. Its compact design allows
researchers to prototype and test new ideas without the overhead of modifying large, complex libraries. ...

Features:
- Minimal, readable codebase with clear extension points for rapid prototyping.
- Robotics-first methods including PPO and Student-Teacher Distillation.
- High-throughput training with native Multi-GPU support. ...

Sections: RSL-RL, Key Features, Learning Environments

</details>

### roundrobin

Collection of roundrobin utilities

`pip install roundrobin` · installs (wheel) · licence: MIT License · rank 6128 · last release 2026-01-25 · [PyPI](https://pypi.org/project/roundrobin/)

<details><summary>README extract</summary>

A small collection of round-robin selectors:

- `basic()` - plain round-robin (A, B, C, A, B, C, ...)
- `weighted()` - weighted round-robin (classic LVS-style)
- `smooth()` - smooth weighted round-robin (Nginx-style; avoids long clumps)
- `smooth_stateful()` - smooth weighted RR with runtime controls (health checks / slow-start)

Example:
```python
>>> import roundrobin
>>> get_roundrobin = roundrobin.basic(["A", "B", "C"])
>>> ''.join([get_roundrobin() for _ in range(7)])
'ABCABCA'
>>> # weighted round-robin balancing algorithm as seen in LVS
>>> get_weighted = roundrobin.weighted([("A", 5), ("B", 1), ("C", 1)])
>>> ''.join([get_weighted() for _ in range(7)])
'AAAAABC'
...
```

Sections: roundrobin, Quickstart, Stateful smooth weighted round-robin, Gotchas, Thread Safety

</details>

### regexploit

Find regular expressions vulnerable to ReDoS

`pip install regexploit` · installs (wheel) · licence: Apache Software License · rank 6160 · last release 2021-03-11 · [PyPI](https://pypi.org/project/regexploit/)

<details><summary>README extract</summary>

Find regexes which are vulnerable to Regular Expression Denial of Service (ReDoS).

Many default regular expression parsers have unbounded worst-case complexity. Regex matching may be quick when presented with a matching input string. ...

Example:
```python
Importing ua_parser.user_agent_parser
Vulnerable regex in /somewhere/.env/lib/python3.9/site-packages/ua_parser/user_agent_parser.py #183
Pattern: \bSmartWatch *\( *([^;]+) *; *([^;]+) *;
Context: self.user_agent_re = re.compile(self.pattern)

Worst-case complexity: 3 ⭐⭐⭐
Repeated character: [20]
Example: 'SmartWatch(' + ' ' * 3456

...
```

...

</details>

### render

Python SDK for Render Workflows

`pip install render` · installs (wheel) · licence: Apache Software License · rank 6230 · last release 2026-11-06 · [PyPI](https://pypi.org/project/render/)

<details><summary>README extract</summary>

The official Python SDK for Render. Define Workflow tasks and flows, manage task runs and flow runs, and access experimental platform features like object storage.

Features:
- REST API Client: Run, monitor, cancel, and list task runs and flow runs
- Task Definition: Decorator-based task registration with the `Workflows` class
- Durable Flows: Flows that replay after a crash, with steps that retry in-process ...

Example:
```python
import asyncio
from render import RenderAsync

async def main():
    render = RenderAsync()

    result = await render.workflows.run_task("my-workflow/my-task", [3, 4])
    print(result.results)

    # start_task() returns an awaitable task run
    task_run = await render.workflows.start_task("my-workflow/my-task", [3, 4])
...
```

...

</details>

### Resemblyzer

Analyze and compare voices with deep learning

`pip install Resemblyzer` · installs (wheel) · licence: Apache Software License · rank 6244 · last release 2023-10-12 · [PyPI](https://pypi.org/project/Resemblyzer/)

<details><summary>README extract</summary>

Resemblyzer allows you to derive a high-level representation of a voice through a deep learning model (referred to as the voice encoder). Given an audio file of speech, it creates a summary vector of 256 values (an embedding, often shortened to "embed" in this repo) that summarizes the characteristics of the voice spoken. ...

Example:
```python
from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np

fpath = Path("path_to_an_audio_file")
wav = preprocess_wav(fpath)

encoder = VoiceEncoder()
embed = encoder.embed_utterance(wav)
np.set_printoptions(precision=3, suppress=True)
print(embed)
```

Sections: Demos, What can I do with this package?, Code example, Additional info

</details>

### ring-flash-attn

Ring attention implementation with flash attention.

`pip install ring-flash-attn` · installs (wheel) · licence: MIT License · rank 6250 · last release 2025-09-10 · [PyPI](https://pypi.org/project/ring-flash-attn/)

<details><summary>README extract</summary>

This repo implements RingAttention using FlashAttention. The current implementation supports:

- varlen (packing samples) api, corresponding to `flash_attn_varlen_func`:
 - `ring_flash_attn_varlen_func`: A basic implementation of ring attention.
 - `zigzag_ring_flash_attn_varlen_func`: an more compute-balanced version of ring attention. ...

Example:
```python
# torchrun --nproc_per_node=2 this_script.py
import torch
from ring_flash_attn import substitute_hf_flash_attn, update_ring_flash_attn_params
from torch import distributed as dist
from transformers import AutoModelForCausalLM, AutoTokenizer

def main():
    # Initialize distributed training
    dist.init_process_group(backend="nccl")

...
```

...

</details>

### requests-html

HTML Parsing for Humans.

`pip install requests-html` · installs (wheel) · licence: MIT License · rank 6400 · last release 2019-02-17 · [PyPI](https://pypi.org/project/requests-html/)

<details><summary>README extract</summary>

This library intends to make parsing HTML (e.g. scraping the web) as
simple and intuitive as possible.

If you're interested in financially supporting Kenneth Reitz open source, consider visiting this link. Your support helps tremendously with sustainability of motivation, as Open Source is no longer part of my day job. ...

Example:
```python
>>> from requests_html import HTMLSession
>>> session = HTMLSession()

>>> r = session.get('
```

Sections: Requests-HTML: HTML Parsing for Humans™, Tutorial & Usage, Using without Requests

</details>

### roboflow

Official Python package for working with the Roboflow API

`pip install roboflow` · installs (wheel) · licence: Apache Software License · rank 6571 · last release 2026-10-26 · [PyPI](https://pypi.org/project/roboflow/)

<details><summary>README extract</summary>

notebooks | inference | autodistill | collect | supervision

Roboflow provides everything you need to build and deploy computer vision models. `roboflow-python` is the official Roboflow Python package. `roboflow-python` enables you to interact with models, datasets, and projects hosted on Roboflow.

With this Python package, you can:

1. ...

Example:
```python
import roboflow
roboflow.login()
```

Sections: Roboflow Python Package, 🚀 Getting Started, Using Roboflow EU, Quickstart, Search and Export, Library Structure

</details>

### retry-decorator

Retry Decorator

`pip install retry-decorator` · installs from source (sdist only) · licence: MIT · rank 6575 · last release 2020-03-10 · [PyPI](https://pypi.org/project/retry-decorator/)

<details><summary>README extract</summary>

Example:
```python
# !/usr/bin/env python

from future import print_function
from retry_decorator import *

@retry(Exception, tries = 3, timeout_secs = 0.1)
def test_retry():
    import sys
    print('hello', file = sys.stderr)
    raise Exception('Testing retry')

if name == 'main':
    try:
        test_retry()
    except Exception as e:
...
```

</details>

### remotezip2

Fork of python-remotezip

`pip install remotezip2` · installs (wheel) · licence: MIT License · rank 6634 · last release 2024-12-01 · [PyPI](https://pypi.org/project/remotezip2/)

### redlines

Compare text, and produce human-readable differences or deltas which look like track changes in Microsoft Word.

`pip install redlines` · installs (wheel) · licence: MIT · rank 6701 · last release 2026-08-28 · [PyPI](https://pypi.org/project/redlines/) · [docs](https://houfu.github.io/redlines/) · [source](https://github.com/houfu/redlines)

<details><summary>README extract</summary>

`Redlines` compares two strings/text and produces structured output showing their differences. Changes are represented with strike-throughs and highlights, similar to Microsoft Word's track changes. The output includes detailed change information, positions, and statistics for programmatic use. ...

Example:
```python
from redlines import Redlines

test = Redlines(
    "The quick brown fox jumps over the lazy dog.",
    "The quick brown fox walks past the lazy dog.",
    markdown_style="none"
)
assert (
    test.output_markdown
    == "The quick brown fox <del>jumps over </del><ins>walks past </ins>the lazy dog."
)
```

Sections: Redlines, Quick Start, Usage, Python API, CLI, Advanced Features, Custom Processors, For AI Agents & Automation, Documentation & Resources

</details>

### readcon-db

Mmap CON corpus store (LMDB/Heed) with xxHash exact match

`pip install readcon-db` · installs (wheel) · licence: MIT · rank 6842 · last release 2026-10-15 · [PyPI](https://pypi.org/project/readcon-db/) · [docs](https://lode-org.github.io/readcon-db/) · [source](https://github.com/lode-org/readcon-db)

<details><summary>README extract</summary>

Mmap-backed CON/convel corpus store (LMDB via Heed), non-SQL selection, xxHash3-128 exact match, and Rust / C / C++ / Python / Fortran bindings.

Part of the readcon ecosystem with `readcon-core` (Python package `readcon`):

| Crate / package | Role | Docs |

| readcon-core / `readcon` | CON interchange (parse/write/spec v2–v3). ...

Sections: readcon-db, Quick start (from source), Design, Cooked SoA tier

</details>

### records

SQL for Humans

`pip install records` · installs (wheel) · licence: ISC License (ISCL) · rank 6875 · last release 2024-03-29 · [PyPI](https://pypi.org/project/records/)

<details><summary>README extract</summary>

**Records is a very simple, but powerful, library for making raw SQL queries
to most relational databases.**

Just write SQL. No bells, no whistles. This common task can be
surprisingly difficult with the standard tools available. ...

Example:
```python
import records

db = records.Database('postgres://...')
rows = db.query('select * from active_users')    # or db.query_file('sqls/active-users.sql')
```

Sections: Records: SQL for Humans™, ☤ The Basics, ☤ Features, ☤ Data Export Functionality, ☤ Thank You, v0.6.0 (04-29-2024), v0.5.1 (09-01-2017), v0.5.0 (11-15-2016), v0.4.3 (02-16-2016), v0.4.2 (02-15-2016), v0.4.1 (02-15-2016), v0.4.0 (02-13-2016), v0.3.0 (02-11-2016), v0.2.0 (02-10-2016)

</details>

### reasoning-gym

A library of procedural dataset generators for training reasoning models

`pip install reasoning-gym` · installs (wheel) · licence: Apache-2.0 · rank 6888 · last release 2026-03-28 · [PyPI](https://pypi.org/project/reasoning-gym/)

<details><summary>README extract</summary>

Reasoning Gym is a community-created Python library of procedural dataset generators and algorithmically verifiable reasoning environments for training reasoning models with reinforcement learning (RL). The goal is to generate virtually infinite training data with adjustable complexity. ...

Example:
```python
import reasoning_gym
data = reasoning_gym.create_dataset('leg_counting', size=10, seed=42)
for i, x in enumerate(data):
    print(f'{i}: q="{x['question']}", a="{x['answer']}"')
    print('metadata:', x['metadata'])
    # use the dataset's `score_answer` method for algorithmic verification
...
```

Sections: Reasoning Gym, 🧠 About, 🖼️ Dataset Gallery, ✨ Quickstart, 🔍 Evaluation, 🤓 Training, 🚀 Projects Using Reasoning Gym

</details>

### rocketchat-API

Python API wrapper for Rocket.Chat

`pip install rocketchat-API` · installs (wheel) · licence: MIT · rank 6895 · last release 2026-11-07 · [PyPI](https://pypi.org/project/rocketchat-API/)

<details><summary>README extract</summary>

Python API wrapper for Rocket.Chat

Example:
```python
from rocketchat_API.rocketchat import RocketChat

rocket = RocketChat('user', 'pass', server_url='

# Get current user info
rocket.me()

# List all channels
for channel in rocket.channels_list():
    print(channel.get("name"))

# Post a message
rocket.chat_post_message('good news everyone!', channel='GENERAL', alias='Farnsworth')

...
```

Sections: rocketchat_API, Requirements, Compatibility, Usage, Basic Authentication, Token-Based Authentication, Method Parameters, Running Tests, Code Style

</details>

### roma

A lightweight library to deal with 3D rotations in PyTorch.

`pip install roma` · installs (wheel) · licence: BSD-3-Clause · rank 6930 · last release 2026-10-22 · [PyPI](https://pypi.org/project/roma/)

<details><summary>README extract</summary>

*RoMa* (which stands for Rotation Manipulation) provides differentiable mappings between 3D rotation representations, mappings from Euclidean to rotation space, and various utilities related to rotations. ...

Example:
```python
import torch
import roma

# Arbitrary numbers of batch dimensions are supported, for convenience.
batch_shape = (2, 3)

# Conversion between rotation representations
rotvec = torch.randn(batch_shape + (3,))
q = roma.rotvec_to_unitquat(rotvec)
R = roma.unitquat_to_rotmat(q)
Rbis = roma.rotvec_to_rotmat(rotvec)
...
```

Sections: Documentation, References

</details>

### rlbot

A framework for writing custom Rocket League bots that run offline.

`pip install rlbot` · installs from source (sdist only) · licence: MIT License · rank 7083 · last release 2024-06-02 · [PyPI](https://pypi.org/project/rlbot/)

<details><summary>README extract</summary>

The RLBot framework helps people create bots for use in Rocket League's offline modes, just for fun.
It provides values from the game like car and ball position, and carries back button presses.
RLBot works for up to 10 bots.

To get started quickly with a simple working bot, you can clone this repository: ...

Sections: RLBot, Requirements, Wikis, Extras

</details>

### rapidata

Rapidata package containing the Rapidata Python Client to interact with the Rapidata Web API in an easy way.

`pip install rapidata` · installs (wheel) · licence: Apache-2.0 · rank 7096 · last release 2026-11-06 · [PyPI](https://pypi.org/project/rapidata/) · [docs](https://docs.rapidata.ai/?utm_source=pypi&utm_medium=referral&utm_campaign=python_sdk&utm_content=project_links)

<details><summary>README extract</summary>

Python client to interface with the Rapidata API.

Docs:

Point it at the guide that ships with the SDK instead of letting it read the installed source:

The guide is edited in `src/rapidata/_skill/`, so it always matches the installed version.

Details and per-agent install commands:

Sections: Rapidata Python Client, Using a coding agent?

</details>

### rply

A pure Python Lex/Yacc that works with RPython

`pip install rply` · installs (wheel) · licence: BSD 3-Clause License · rank 7137 · last release 2021-01-27 · [PyPI](https://pypi.org/project/rply/)

<details><summary>README extract</summary>

Welcome to RPLY! A pure Python parser generator, that also works with RPython.
It is a more-or-less direct port of David Beazley's awesome PLY, with a new
public API, and RPython support.

You can find the documentation online.

Basic API:

Then you can do:

You can also substitute your own lexer. ...

Features:
In RPython, like other statically typed languages, a variable must have a
specific type, we take advantage of polymorphism to keep values in a box so
that everything is statically typed. You can write whatever boxes you need for
your project. ...

Example:
```python
from rply import ParserGenerator, LexerGenerator
from rply.token import BaseBox

lg = LexerGenerator()
# Add takes a rule name, and a regular expression that defines the rule.
lg.add("PLUS", r"\+")
...

</details>

### rjieba

jieba-rs Python binding

`pip install rjieba` · installs (wheel) · licence: MIT · rank 7365 · last release 2026-10-26 · [PyPI](https://pypi.org/project/rjieba/) · [source](https://github.com/messense/rjieba-py)

<details><summary>README extract</summary>

jieba-rs Python binding.

Example:
```python
import rjieba

print(rjieba.cut('我们中出了一个叛徒'))
print(rjieba.tag('我们中出了一个叛徒'))
```

Sections: rjieba-py, Usage, Performance

</details>

### raindrop-ai

Raindrop AI (Python SDK)

`pip install raindrop-ai` · installs (wheel) · licence: MIT License · rank 7457 · last release 2026-10-09 · [PyPI](https://pypi.org/project/raindrop-ai/)

<details><summary>README extract</summary>

The official Python SDK for Raindrop AI — track AI events, collect user signals, and instrument LLM applications with OpenTelemetry-based tracing.

Example:
```python
import raindrop.analytics as raindrop

raindrop.init(api_key="your-api-key", tracing_enabled=True)

# Track an AI event
raindrop.track_ai(
    user_id="user-123",
    event="chat-completion",
    model="gpt-4",
    input="What is the weather?",
    output="It's sunny and 72°F.",
    convo_id="conv-456",
)
```

Sections: Raindrop Python SDK, Quick Start, Evals, Application Git provenance, Instance-based clients (multiple projects in one process), Tracing with multiple instances, Payload size limits, Projects, Interactions, Tool Definitions, Resuming Interactions, Decorators, Spans, Context Managers

</details>

### reflex

Web apps in pure Python.

`pip install reflex` · installs (wheel) · licence: Apache Software License · rank 7505 · last release 2026-10-27 · [PyPI](https://pypi.org/project/reflex/) · [docs](https://reflex.dev/docs/getting-started/introduction) · [source](https://github.com/reflex-dev/reflex)

<details><summary>README extract</summary>

> [!NOTE]
> Build faster with Reflex:
> - AI Builder - Generate full-stack Reflex apps in seconds.
> - Agent Toolkit - Connect MCP and Skills to your coding assistant.
> - App Management - Deploy and manage your Reflex apps.

Reflex is a library to build full-stack web apps in pure Python.

Key features: ...

Example:
```python
import reflex as rx
import openai

client = openai.AsyncOpenAI()

class State(rx.State):
    prompt: str = ""
    image_url: str = ""
    processing: bool = False

    @rx.event
    def set_prompt(self, value: str):
        self.prompt = value

    @rx.event
    async def generate(self):
        self.processing = True
        yield
...
```

Sections: Introduction, 🥳 Create your first app, 🫧 Example App

</details>

### rpy2

Python interface to the R language (embedded R)

`pip install rpy2` · installs (wheel) · licence: GPL-2.0-or-later · rank 7521 · last release 2026-10-11 · [PyPI](https://pypi.org/project/rpy2/) · [docs](https://rpy2.github.io/doc.html) · [source](https://github.com/rpy2/rpy2)

_README extract left out: share-alike licence._

### ruamel.yaml.string

add dump_to_string/dumps method that returns YAML document as string

`pip install ruamel.yaml.string` · installs (wheel) · licence: MIT License · rank 7556 · last release 2023-05-02 · [PyPI](https://pypi.org/project/ruamel.yaml.string/)

<details><summary>README extract</summary>

:version: 0.1.1
:updated: 2023-05-02

This plug-in adds a method `dump_to_string` (and its equivalent `dumps`)
to the `ruamel.yaml.YAML` instance that returns the document as
a Python `string`.

Example:
```python
import ruamel.yaml

yaml = ruamel.yaml.YAML(typ=['rt', 'string'])
data  = dict(abc=42, help=['on', 'its', 'way'])
print('retval', yaml.dump_to_string(data))
print('>>>> done')
```

Sections: ruamel.yaml.string, Usage

</details>

### robocorp-storage

Robocorp Asset Storage library

`pip install robocorp-storage` · installs (wheel) · licence: Apache Software License · rank 7581 · last release 2026-08-23 · [PyPI](https://pypi.org/project/robocorp-storage/) · [source](https://github.com/robocorp/robocorp/)

<details><summary>README extract</summary>

`robocorp-storage` is a library which provides read and write access to the Asset Storage in Robocorp Control Room.

Example:
```python
from robocorp import storage

def store_email():
    storage.set_text("cosmin", "cosmin@robocorp.com")
    print("E-mail:", storage.get_text("cosmin"))
    storage.delete_asset("cosmin")
```

Sections: robocorp-storage, Getting started, Guides, API Reference

</details>

### random-user-agent

A package to get random user agents based filters provided by user

`pip install random-user-agent` · installs (wheel) · licence: MIT License · rank 7586 · last release 2018-12-26 · [PyPI](https://pypi.org/project/random-user-agent/)

<details><summary>README extract</summary>

Random User Agents is a python library that provides list of user agents,
from a collection of more than 326,000+ user agents, based on filters.

Some of the filter names which can be passed to `UserAgent()` are listed below:

 operating_systems : [
 UNIX, LINUX, WINDOWS, MAC, ...

 hardware_types : [
 MOBILE, COMPUTER, SERVER, ... ...

Example:
```python
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

# you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
# you can also set number of user agents required by providing `limit` as parameter

...
```

</details>

### reflex-hosting-cli

Reflex Hosting CLI

`pip install reflex-hosting-cli` · installs (wheel) · licence: Apache-2.0 · rank 7621 · last release 2026-10-27 · [PyPI](https://pypi.org/project/reflex-hosting-cli/)

<details><summary>README extract</summary>

Hosting CLI for Reflex.

When an app is still scaling, `reflex deploy` waits 15 seconds between confirmed
scaling refusals, for up to 7 retries to update instance bounds and 11 retries
to submit the deployment. The CLI reports each wait, and you can cancel
with Ctrl-C. Submission retries reuse the uploaded build. ...

</details>

### requests-credssp

HTTPS CredSSP authentication with the requests library.

`pip install requests-credssp` · installs (wheel) · licence: BSD License · rank 7624 · last release 2022-02-21 · [PyPI](https://pypi.org/project/requests-credssp/)

<details><summary>README extract</summary>

This package allows for HTTPS CredSSP authentication using the requests
library. CredSSP is a Microsoft authentication that allows your credentials to
be delegated to a server giving you double hop authentication.

Features:
This library supports the following CredSSP features

* Protocol version 2 to 6
* Initial authentication with NTLM or Kerberos
* Message encryption support using the `wrap` and `unwrap` functions

Example:
```python
import requests
from requests_credssp import HttpCredSSPAuth

# use SPNEGO (default if omitted)
credssp_auth = HttpCredSSPAuth('domain\\user', 'password',
                               auth_mechanism='auto')

# only allow Kerberos
credssp_auth = HttpCredSSPAuth('user@REALM.COM', 'password',
...
```

...

</details>

### runai-model-streamer-gcs

(no summary)

`pip install runai-model-streamer-gcs` · installs (wheel) · licence: not stated · rank 7631 · last release 2026-10-29 · [PyPI](https://pypi.org/project/runai-model-streamer-gcs/)

### rectangle-packer

Pack a set of rectangles into a bounding box with minimum area

`pip install rectangle-packer` · installs (wheel) · licence: MIT License · rank 7651 · last release 2026-10-13 · [PyPI](https://pypi.org/project/rectangle-packer/)

<details><summary>README extract</summary>

Fast rectangle packing for Python.

Given a set of rectangles with fixed orientations, `rectangle-packer` finds
an enclosing bounding box with small area and no overlaps.

Example:
```python
import rpack

sizes = [(58, 206), (231, 176), (35, 113), (46, 109)]
positions = rpack.pack(sizes)
print(positions)
```

Sections: rectangle-packer, Quick start, Documentation and source

</details>

### robotframework-databaselibrary

Database Library for Robot Framework

`pip install robotframework-databaselibrary` · installs (wheel) · licence: Apache Software License · rank 7663 · last release 2026-09-20 · [PyPI](https://pypi.org/project/robotframework-databaselibrary/)

<details><summary>README extract</summary>

The Database Library for Robot Framework allows you to query a database and verify the results.
It requires an appropriate Python module to be installed separately - depending on your database, like e.g. `oracledb` or `pymysql`.

The library consists of some keywords designed to perform different checks on your database. ...

Sections: Robot Framework Database Library, Requirements, Basic usage examples, Handling multiple database connections, Example, Connection examples for different DB modules, Using configuration file, Config file examples, Config file with a specific alias, Config file with some params only, Config file with some custom DB module specific params, Inline assertions, Examples, Retry mechanism

</details>

### rush

A library for throttling algorithms

`pip install rush` · installs (wheel) · licence: MIT License · rank 7715 · last release 2021-04-01 · [PyPI](https://pypi.org/project/rush/)

<details><summary>README extract</summary>

This library is a small collection of algorithms that can be reused
when throttling user interactions with a resource (e.g., an API).

This library strives to allow any limiter and backing store to be used
together without needing to be worried about potential compatibility.

Features:
- A basic periodic interval rate limiter - N accesses per period of time. An
 example would be the GitHub API that limits authenticated users to 5,000
 requests per hour. ...

Sections: rush: A library for throttles, Features, Quality

</details>

### ruamel.base

common routines for ruamel packages

`pip install ruamel.base` · installs (wheel) · licence: MIT License · rank 7810 · last release 2015-08-27 · [PyPI](https://pypi.org/project/ruamel.base/)

<details><summary>README extract</summary>

ruamel.base

- (future) place for elements common to multiple packages

</details>

### rapidyaml

Parse and emit YAML, and do it fast. Python wrapper for the C++ library

`pip install rapidyaml` · installs (wheel) · licence: MIT · rank 7858 · last release 2026-06-25 · [PyPI](https://pypi.org/project/rapidyaml/)

<details><summary>README extract</summary>

Or ryml, for short. ryml is a C++ library to parse and emit
YAML, and do it fast, on
everything from x64 to bare-metal chips without operating system. This
repo contains the rapidyaml python package, which was previously in
the original repo (up to release 0.11.0). ...

Example:
```python
+----------------------------------------+-------+----------+----------+-----------+
| style_seqs_blck_outer1000_inner100.yml | count | time(ms) | avg(ms)  | avg(MB/s) |
+----------------------------------------+-------+----------+----------+-----------+
| parse:RuamelYamlParse                  |     1 | 4564.812 | 4564.812 |     0.173 |
...
```

Sections: Rapid YAML - Python package, Performance, Examples, Parsing a file, Creating and emitting a tree

</details>

### runai-model-streamer-s3

(no summary)

`pip install runai-model-streamer-s3` · installs (wheel) · licence: not stated · rank 7938 · last release 2026-10-29 · [PyPI](https://pypi.org/project/runai-model-streamer-s3/)

### rabbitmq-admin

A python interface for the RabbitMQ Admin HTTP API

`pip install rabbitmq-admin` · installs (wheel) · licence: MIT License · rank 8070 · last release 2015-10-16 · [PyPI](https://pypi.org/project/rabbitmq-admin/)

<details><summary>README extract</summary>

This project is a python wrapper around the RabbitMQ Management HTTP API.

Example:
```python
>>> from rabbitmq_admin import AdminAPI
>>> api = AdminAPI(url=' auth=('guest', 'guest'))
>>> api.create_vhost('second_vhost')
>>> api.create_user('second_user', 'password')
>>> api.create_user_permission('second_user', 'second_vhost')
>>> api.list_permission()
[{'configure': '.*',
  'read': '.*',
  'user': 'guest',
  'vhost': '/',
...
```

Sections: rabbitmq-admin, Example, Documentation

</details>

### r7insight-python

Python Logger plugin to send logs to Rapid7 Insight

`pip install r7insight-python` · installs (wheel) · licence: MIT License · rank 8241 · last release 2025-02-19 · [PyPI](https://pypi.org/project/r7insight-python/)

<details><summary>README extract</summary>

This is a plugin library to enable logging to Rapid7 Insight from the Python Logger.
Additionally this plugin allows the user to get an overview of methods being executed,
their execution time, as well as CPU and Memory statistics.
More info at Note that this plugin is
asynchronous. ...

Example:
```python
# !/usr/bin/env python

import logging
from r7insight import R7InsightHandler

log = logging.getLogger('r7insight')
log.setLevel(logging.INFO)
test = R7InsightHandler(TOKEN, REGION)

log.addHandler(test)

log.warn("Warning message")
log.info("Info message")

sleep(10)
```

Sections: Rapid7 Insight Logger, Setup, Usage, Usage with metric functionality, Metric.Time(), Configure

</details>

### reflex-base

Core types for the Reflex framework.

`pip install reflex-base` · installs (wheel) · licence: Apache-2.0 · rank 8263 · last release 2026-10-27 · [PyPI](https://pypi.org/project/reflex-base/)

### rensa

High-performance MinHash implementation in Rust with Python bindings for similarity estimation and deduplication

`pip install rensa` · installs (wheel) · licence: MIT · rank 8292 · last release 2026-09-06 · [PyPI](https://pypi.org/project/rensa/) · [source](https://github.com/beowolx/rensa)

<details><summary>README extract</summary>

Rensa is a MinHash library written in Rust with Python bindings. It estimates
Jaccard similarity from compact signatures and finds near-duplicate documents
using locality-sensitive hashing (LSH). Rensa supports batch and streaming
deduplication on Linux, macOS and Windows.

Try it in Maxime Labonne's AutoDedup notebook.

Features:
- You want to find near-duplicates in a dataset without comparing every pair of
 documents. With LSH enabled, `RMinHashDeduplicator` finds candidate matches and
 checks their estimated similarity against your threshold. ...

Example:
```python
from rensa import RMinHash

first, second = RMinHash.from_token_sets(
    ["the quick brown fox".split(), "the quick brown dog".split()],
    num_perm=128,
    seed=42,
)
print(first.jaccard(second))
```

...

</details>

### rtp

A library for decoding/encoding rtp packets

`pip install rtp` · installs (wheel) · licence: apache-2.0 · rank 8310 · last release 2023-12-05 · [PyPI](https://pypi.org/project/rtp/)

<details><summary>README extract</summary>

This python library provides a means to decode, encode, and interact with RTP packets. It is intended to be used together with other libraries that decode, encode, and interact with the payload bitstreams. This library does not provide any network functionality.

Example:
```python
from rtp import RTP, Extension, PayloadType
from copy import deepcopy

baseRTP = RTP(
    marker=True,
    payloadType=PayloadType.L16_2chan,
    extension=Extension(
        startBits=getExtStartBits(),
        headerExtension=getExtBody()
        ),
    csrcList=getCSRCList()
)
thisRTPBitstream = thisRTP.toBytearray()

while runing:
...
```

Sections: rtp, Example usage

</details>

### reflex-components-core

UI components for Reflex.

`pip install reflex-components-core` · installs (wheel) · licence: Apache-2.0 · rank 8386 · last release 2026-10-27 · [PyPI](https://pypi.org/project/reflex-components-core/)

### reflex-components-lucide

Reflex lucide components.

`pip install reflex-components-lucide` · installs (wheel) · licence: Apache-2.0 · rank 8428 · last release 2026-10-27 · [PyPI](https://pypi.org/project/reflex-components-lucide/)

### remotezip

Access zip file content hosted remotely without downloading the full file.

`pip install remotezip` · installs (wheel) · licence: MIT · rank 8454 · last release 2026-08-29 · [PyPI](https://pypi.org/project/remotezip/)

<details><summary>README extract</summary>

This module provides a way to access single members of a zip file archive without downloading the full content from a remote web server. For this library to work, the web server hosting the archive needs to support the range header.

Example:
```python
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth
from hashlib import sha256

auth = BotoAWSRequestsAuth(
    aws_host='s3-eu-west-1.amazonaws.com',
    aws_region='eu-west-1',
    aws_service='s3'
)
headers = {'x-amz-content-sha256': sha256('').hexdigest()}
url = "

with RemoteZip(url, auth=auth, headers=headers) as z:
...
```

Sections: remotezip, Usage, Initialization, Class Interface, Examples, List members in archive, Download a member, S3 example, Command line tool, Example, How it works, Alternative module

</details>

### river

Online machine learning in Python

`pip install river` · installs (wheel) · licence: BSD-3-Clause · rank 8458 · last release 2026-08-21 · [PyPI](https://pypi.org/project/river/) · [source](https://github.com/online-ml/river/)

<details><summary>README extract</summary>

River is a Python library for online machine learning. It aims to be the most user-friendly library for doing machine learning on streaming data. River is the result of a merger between creme and scikit-multiflow.

Example:
```python
>>> from pprint import pprint
>>> from river import datasets

>>> dataset = datasets.Phishing()

>>> for x, y in dataset:
...     pprint(x)
...     print(y)
...     break
{'age_of_domain': 1,
 'anchor_from_other_domain': 0.0,
 'empty_server_form_handler': 0.0,
 'https': 0.0,
 'ip_in_url': 1,
 'is_popular': 0.5,
 'long_url': 1.0,
...
```

Sections: ⚡️ Quickstart, 🔮 Features, 🤔 Should I be using River?, 🔗 Useful links, 🤝 Affiliations

</details>

### reflex-components-sonner

Reflex sonner components.

`pip install reflex-components-sonner` · installs (wheel) · licence: Apache-2.0 · rank 8515 · last release 2026-10-08 · [PyPI](https://pypi.org/project/reflex-components-sonner/)

### reflex-components-radix

Reflex radix components.

`pip install reflex-components-radix` · installs (wheel) · licence: Apache-2.0 · rank 8766 · last release 2026-10-27 · [PyPI](https://pypi.org/project/reflex-components-radix/)

### reflex-components-code

Reflex code display components.

`pip install reflex-components-code` · installs (wheel) · licence: Apache-2.0 · rank 8818 · last release 2026-10-27 · [PyPI](https://pypi.org/project/reflex-components-code/)

### requests-gssapi

A GSSAPI authentication handler for python-requests

`pip install requests-gssapi` · installs (wheel) · licence: ISC · rank 8831 · last release 2025-10-16 · [PyPI](https://pypi.org/project/requests-gssapi/)

<details><summary>README extract</summary>

Requests is an HTTP library, written in Python, for human beings. This library
adds optional GSSAPI authentication support and supports mutual
authentication.

It provides a fully backward-compatible shim for the old
python-requests-kerberos library: simply replace `import requests_kerberos`
with `import requests_gssapi`. ...

Example:
```python
>>> import requests
>>> from requests_gssapi import HTTPSPNEGOAuth
>>> r = requests.get(" auth=HTTPSPNEGOAuth())
...
```

Sections: requests GSSAPI authentication library, Setup, Authentication Failures, Mutual Authentication, DISABLED, REQUIRED, OPTIONAL, Opportunistic Authentication, `Expect-Continue`, Hostname Override, Explicit Principal, Explicit Mechanism, Delegation, Logging

</details>

### reflex-components-dataeditor

Reflex dataeditor components.

`pip install reflex-components-dataeditor` · installs (wheel) · licence: Apache-2.0 · rank 8868 · last release 2026-10-27 · [PyPI](https://pypi.org/project/reflex-components-dataeditor/)

### reflex-components-plotly

Reflex plotly components.

`pip install reflex-components-plotly` · installs (wheel) · licence: Apache-2.0 · rank 8880 · last release 2026-10-08 · [PyPI](https://pypi.org/project/reflex-components-plotly/)

### reflex-components-recharts

Reflex recharts components.

`pip install reflex-components-recharts` · installs (wheel) · licence: Apache-2.0 · rank 8883 · last release 2026-10-08 · [PyPI](https://pypi.org/project/reflex-components-recharts/)

### reflex-components-gridjs

Reflex gridjs components.

`pip install reflex-components-gridjs` · installs (wheel) · licence: Apache-2.0 · rank 8885 · last release 2026-10-08 · [PyPI](https://pypi.org/project/reflex-components-gridjs/)

### reflex-components-markdown

Reflex markdown components.

`pip install reflex-components-markdown` · installs (wheel) · licence: Apache-2.0 · rank 8917 · last release 2026-10-08 · [PyPI](https://pypi.org/project/reflex-components-markdown/)

### reflex-components-moment

Reflex moment components.

`pip install reflex-components-moment` · installs (wheel) · licence: Apache-2.0 · rank 8927 · last release 2026-10-27 · [PyPI](https://pypi.org/project/reflex-components-moment/)

### reflex-components-react-player

Reflex react-player components.

`pip install reflex-components-react-player` · installs (wheel) · licence: Apache-2.0 · rank 8934 · last release 2026-10-08 · [PyPI](https://pypi.org/project/reflex-components-react-player/)

### runstats

Compute statistics and regression in one pass

`pip install runstats` · installs from source (sdist only) · licence: Apache Software License · rank 8953 · last release 2021-06-11 · [PyPI](https://pypi.org/project/runstats/) · [docs](http://www.grantjenks.com/docs/runstats/) · [source](https://github.com/grantjenks/python-runstats)

<details><summary>README extract</summary>

RunStats is an Apache2 licensed Python module for online statistics and
online regression. Statistics and regression summaries are computed in a single
pass. Previous values are not recorded in summaries.

Long running systems often generate numbers summarizing performance. It could
be the latency of a response or the time between requests. ...

Features:
- Pure-Python
- Fully Documented
- 100% Test Coverage
- Numerically Stable
- Optional Cython-optimized Extension (5-100 times faster)
- Statistics summary computes mean, variance, standard deviation, skewness,
 kurtosis, minimum and maximum. ...

Example:
```python
>>> import runstats
>>> help(runstats)                             # doctest: +SKIP
>>> help(runstats.Statistics)                  # doctest: +SKIP
...

</details>

### rust-demangler

A package for demangling Rust symbols

`pip install rust-demangler` · installs (wheel) · licence: MIT License · rank 9244 · last release 2021-04-24 · [PyPI](https://pypi.org/project/rust-demangler/)

<details><summary>README extract</summary>

A package for demangling Rust symbols, written in Python.

Setup

Usage

Example

License

This project is licensed under the MIT License

Example:
```python
from rust-demangler import demangle
print(demangle(<mangled_name>))
```

</details>

### repomix

A tool for analyzing and summarizing code repositories

`pip install repomix` · installs (wheel) · licence: MIT · rank 9255 · last release 2026-02-13 · [PyPI](https://pypi.org/project/repomix/)

<details><summary>README extract</summary>

English | 简体中文

Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. It's perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, and Gemini.

The original Repomix is written in JavaScript, and this is the ported Python version. ...

Features:
- ✅ Complete MCP protocol support
- ✅ Detailed operation logging
- ✅ Security file checking
- ✅ Multiple output formats
- ✅ File search and reading
- ✅ Temporary file management
- 🔄 Remote repository support (in development) ...

Example:
```python
def calculate_sum(a: int, b: int) -> int:
    """
    Calculate the sum of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The sum of a and b
    """
...

</details>

### rustici-software-cloud-v2

SCORM Cloud Rest API

`pip install rustici-software-cloud-v2` · installs (wheel) · licence: not stated · rank 9351 · last release 2026-05-06 · [PyPI](https://pypi.org/project/rustici-software-cloud-v2/)

<details><summary>README extract</summary>

REST API used for SCORM Cloud integrations. # noqa: E501

</details>

### roifile

Read and write ImageJ ROI format

`pip install roifile` · installs (wheel) · licence: BSD-3-Clause · rank 9416 · last release 2026-11-07 · [PyPI](https://pypi.org/project/roifile/) · [docs](https://www.cgohlke.com/docs/roifile/) · [source](https://github.com/cgohlke/roifile)

<details><summary>README extract</summary>

Roifile is a Python library to read, write, create, and plot ImageJ ROIs,
an undocumented and ImageJ application specific format to store regions of
interest, geometric shapes, paths, text, and whatnot for image overlays.

:Author: Christoph Gohlke
:License: BSD-3-Clause
:Version: 2026.11.6
:DOI: 10.5281/zenodo.6941603

Sections: Read and write ImageJ ROI format, Quickstart, Requirements, Revisions, Notes, Examples

</details>

### reqif

Python library for ReqIF format. ReqIF parsing and unparsing.

`pip install reqif` · installs (wheel) · licence: Apache Software License · rank 9518 · last release 2026-08-11 · [PyPI](https://pypi.org/project/reqif/) · [source](https://github.com/strictdoc-project/reqif)

<details><summary>README extract</summary>

ReqIF is a Python library for working with ReqIF format.

Example:
```python
from reqif.parser import ReqIFParser

input_file_path = "input.reqif"

reqif_bundle = ReqIFParser.parse(input_file_path)
for specification in reqif_bundle.core_content.req_if_content.specifications:
    print(specification.long_name)

    for current_hierarchy in reqif_bundle.iterate_specification_hierarchy(specification):
...
```

Sections: ReqIF, Getting started, Using ReqIF as a library, Parsing ReqIF, Unparsing ReqIF, Reporting parsing/unparsing progress, Logging, Using ReqIF as a command-line tool, Validate command, Passthrough command, Formatting ReqIF, Anonymizing ReqIF, How-to examples, Implementation details

</details>

### reproject

Reproject astronomical images

`pip install reproject` · installs (wheel) · licence: BSD 3-Clause · rank 9597 · last release 2026-06-25 · [PyPI](https://pypi.org/project/reproject/)

<details><summary>README extract</summary>

The `reproject` package is a Python package to reproject astronomical
images using various techniques via a uniform interface. By
*reprojection*, we mean the re-gridding of images from one world
coordinate system to another (for example changing the pixel resolution,
orientation, coordinate system). ...

</details>

### razdel

Splits russian text into tokens, sentences, section. Rule-based

`pip install razdel` · installs (wheel) · licence: MIT License · rank 9874 · last release 2020-03-26 · [PyPI](https://pypi.org/project/razdel/)

<details><summary>README extract</summary>

`razdel` — rule-based system for Russian sentence and word tokenization..

Example:
```python
>>> from razdel import tokenize

>>> tokens = list(tokenize('Кружка-термос на 0.5л (50/64 см³, 516;...)'))
>>> tokens
[Substring(0, 13, 'Кружка-термос'),
 Substring(14, 16, 'на'),
 Substring(17, 20, '0.5'),
 Substring(20, 21, 'л'),
 Substring(22, 23, '(')
 ...]

>>> [_.text for _ in tokens]
...
```

Sections: Usage, Quality, performance, Tokens, Sentencies

</details>

### runware

The Python Runware SDK is used to interact with the Runware API, powered by the Runware inference platform. It supports image generation, video generation, image upscale, video upscale, image caption, video caption, image background removal, video background removal, audio generation, and more. It also allows the use of an existing gallery of models or selecting any model or LoRA from the CivitAI gallery. The API also supports inpainting, outpainting, and a series of other ControlNet models.

`pip install runware` · installs (wheel) · licence: MIT License · rank 9895 · last release 2026-06-30 · [PyPI](https://pypi.org/project/runware/) · [docs](https://docs.runware.ai/) · [source](https://github.com/runware/sdk-python)

<details><summary>README extract</summary>

> [!NOTE]
> A new official SDK is available at runware-python. It covers the full inference and utility surface with REST or WebSocket transports and gets all new features going forward. This library remains supported during the transition. ...

Example:
```python
from runware import Runware, IImageInference

async def main() -> None:
    runware = Runware(api_key=RUNWARE_API_KEY)
    await runware.connect()

    request_image = IImageInference(
        positivePrompt="a beautiful mountain landscape",
        model="civitai:36520@76907",
        height=512,
        width=512,
        webhookURL="
    )

...
```

...

</details>

### ripgrepy

(no summary)

`pip install ripgrepy` · installs from source (sdist only) · licence: not stated · rank 10172 · last release 2025-07-11 · [PyPI](https://pypi.org/project/ripgrepy/) · [docs](https://ripgrepy.readthedocs.io/)

<details><summary>README extract</summary>

`ripgrepy` is a python interface to ripgrep.
It is written to support Python 3.7+ only and is built on ripgrep version 11.0.1

For complete usage and details, refer to the docs at

Readthedocs

Use pip to install

`ripgrepy` leverages the system ripgrep to run its commands. ...

Example:
```python
from ripgrepy import Ripgrepy
# The Ripgrepy class takes two arguments. The regex to search for and the folder path to search in

rg = Ripgrepy('he[l]{2}o', '/some/path/to/files')
```

Sections: ripgrepy, Instal, Requirements, Usage, Output methods

</details>

### regopy

Python interface for the OPA Rego Language and Runtime

`pip install regopy` · installs (wheel) · licence: MIT · rank 10208 · last release 2026-07-06 · [PyPI](https://pypi.org/project/regopy/) · [docs](https://microsoft.github.io/rego-cpp/) · [source](https://github.com/microsoft/rego-cpp)

<details><summary>README extract</summary>

Rego
is the native query language of the Open Policy Agent project. If you want to
learn more about Rego as a language, and its various use cases, we refer
you to the language documentation above which OPA provides. ...

Example:
```python
from regopy import Interpreter
rego = Interpreter()
print(rego.query("x=5;y=x + (2 - 4 * 0.25) * -3 + 7.4;2 * 5"))
# {"expressions":[true, true, 10], "bindings":{"x":5, "y":9.4}}
input0 = {
    "a": 10,
    "b": "20",
    "c": 30.0,
    "d": True
}
data0 = {
    "one": {
        "bar": "Foo",
        "baz": 5,
        "be": True,
...
```

Sections: `regopy`, Example Usage, Builtins, Compatibility with the OPA Rego Go implementation

</details>

### recurly

Recurly v4

`pip install recurly` · installs (wheel) · licence: not stated · rank 10265 · last release 2026-10-30 · [PyPI](https://pypi.org/project/recurly/)

<details><summary>README extract</summary>

This repository houses the official python library for Recurly's V3 API.

> *Note*:
> If you were looking for the V2 client, see the v2 branch.

This library's python documentation is hosted on ReadTheDocs.
It contains the Getting Started guide as well as the reference documentation. ...

Sections: Recurly, Documentation

</details>

### reorder-python-imports

Tool for reordering python imports

`pip install reorder-python-imports` · installs (wheel) · licence: MIT · rank 10289 · last release 2026-10-12 · [PyPI](https://pypi.org/project/reorder-python-imports/)

<details><summary>README extract</summary>

Tool for automatically reordering python imports. Similar to `isort` but
uses static analysis more.

Features:
The style chosen by `reorder-python-imports` has a single aim: reduce merge
conflicts.

By having a single import per line, multiple contributors can
add / remove imports from a single module without resulting in a conflict. ...

Example:
```python
import sys
import pyramid
import reorder_python_imports
```

...

</details>

### robocorp-vault

Robocorp Control Room Vault API integration library

`pip install robocorp-vault` · installs (wheel) · licence: Apache Software License · rank 10375 · last release 2026-10-18 · [PyPI](https://pypi.org/project/robocorp-vault/) · [source](https://github.com/robocorp/robocorp/)

<details><summary>README extract</summary>

`robocorp-vault` is a library that provides read and write access to the Vault in Robocorp Control Room, which can be used to store and retrieve secret values such as passwords.

Example:
```python
from robocorp.tasks import task
from robocorp import vault

@task
def inspect_secret():
    secret = vault.get_secret("login_credentials")
    print("Secret name:", secret.name)
    print("Secret description:", secret.description)
    print("Secret keys:", secret.keys())
    print("Secret value:", secret["username"])
```

Sections: robocorp-vault, Getting started, Guides, API Reference

</details>

### rigour

Financial crime domain data validation and normalization library.

`pip install rigour` · installs (wheel) · licence: MIT License · rank 10410 · last release 2026-11-07 · [PyPI](https://pypi.org/project/rigour/) · [docs](https://rigour.followthemoney.tech/) · [source](https://github.com/opensanctions/rigour.git)

<details><summary>README extract</summary>

Data cleaning and validation functions for processing various types of text emanating and describing the business world. This applies to human and company names, language, territory
and country codes, corporate and tax identifiers, etc. ...

Sections: rigour, Usage & documentation

</details>

### robocorp

Robocorp core libraries for Python automation

`pip install robocorp` · installs (wheel) · licence: Apache Software License · rank 10411 · last release 2026-11-01 · [PyPI](https://pypi.org/project/robocorp/) · [source](https://github.com/robocorp/robocorp/)

<details><summary>README extract</summary>

The purpose of this meta-package is to simplify dependency management by having all the essentials packed in a single easy-to-install dependency.

The following libraries are currently included:

| Release in PyPI | Description |

| | Python framework designed to simplify the development of Python automations. ...

</details>

### rs-data

RegScale gRPC contract library — assets, issues, and vulnerabilities

`pip install rs-data` · installs (wheel) · licence: not stated · rank 10489 · last release 2026-05-05 · [PyPI](https://pypi.org/project/rs-data/)

### robocorp-workitems

Robocorp Work Items library

`pip install robocorp-workitems` · installs (wheel) · licence: Apache Software License · rank 10503 · last release 2026-08-23 · [PyPI](https://pypi.org/project/robocorp-workitems/) · [source](https://github.com/robocorp/robocorp/)

<details><summary>README extract</summary>

Work items are used in Robocorp Control Room for managing data that go through multiple steps and tasks inside a process. Each step of a process receives input work items from the previous step, and creates output work items for the next step.

Example:
```python
from robocorp import workitems
from robocorp.tasks import task

@task
def handle_item():
    item = workitems.inputs.current
    print("Received payload:", item.payload)
    workitems.outputs.create(payload={"key": "value"})
```

Sections: robocorp-workitems, Getting started, Work item structure, Guides, API Reference

</details>

### redlock-py

Redis locking mechanism

`pip install redlock-py` · installs from source (sdist only) · licence: MIT License · rank 10738 · last release 2016-03-08 · [PyPI](https://pypi.org/project/redlock-py/)

<details><summary>README extract</summary>

redlock-py - Redis distributed locks in Python

This python lib implements the Redis-based distributed lock manager algorithm
described in this blog post.

To create a lock manager:

 dlm = Redlock([{"host": "localhost", "port": 6379, "db": 0}, ])

To acquire a lock:

 my_lock = dlm.lock("my_resource_name",1000) ...

</details>

### repartipy

Helper for handling PySpark DataFrame partition size 📑🎛️

`pip install repartipy` · installs (wheel) · licence: Apache Software License · rank 10808 · last release 2024-03-08 · [PyPI](https://pypi.org/project/repartipy/)

<details><summary>README extract</summary>

RepartiPy helps you to elaborately handle PySpark DataFrame partition size.

- Repartition your DataFrame precisely, without knowing the whole DataFrame size (i.e. `Dynamic Repartition`)
- Estimate your DataFrame size with more accuracy

Features:
Although Spark SizeEstimator can be used to estimate a DataFrame size, it is not accurate sometimes.
RepartiPy uses Spark's execution plan statistics in order to provide a roundabout way.
It suggests two approaches to achieve this: ...

Example:
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
input_data = [
        (1, "Seoul"),
        (2, "Busan"),
    ]
df = spark.createDataFrame(data=input_data, schema=["id", "location"])
```

...

</details>

### regendoc

a tool to check/update simple file/shell examples in documentation

`pip install regendoc` · installs (wheel) · licence: MPL2 · rank 10876 · last release 2021-10-01 · [PyPI](https://pypi.org/project/regendoc/)

<details><summary>README extract</summary>

re-render examples in documentation

regendoc copies examples from documentation into custom folders and renders it

</details>

### rsconnect-python

The Posit Connect command-line interface.

`pip install rsconnect-python` · installs (wheel) · licence: not stated · rank 11002 · last release 2026-10-16 · [PyPI](https://pypi.org/project/rsconnect-python/) · [docs](https://docs.posit.co/rsconnect-python) · [source](http://github.com/posit-dev/rsconnect-python)

<details><summary>README extract</summary>

The command-line interface for Posit Connect and Posit Connect Cloud.

Sections: rsconnect-python, uv, pipx, into your project, Usage with Posit Connect, Usage with Posit Connect Cloud

</details>

### reno

RElease NOtes manager

`pip install reno` · installs (wheel) · licence: Apache Software License · rank 11014 · last release 2024-03-04 · [PyPI](https://pypi.org/project/reno/)

### rendercv-fonts

Some fonts for RenderCV

`pip install rendercv-fonts` · installs (wheel) · licence: MIT · rank 11111 · last release 2025-12-09 · [PyPI](https://pypi.org/project/rendercv-fonts/) · [source](https://github.com/rendercv/rendercv-fonts)

<details><summary>README extract</summary>

A Python package with some fonts for the `rendercv` package.

</details>

### rdflib-neo4j

RDFLib Store backed by neo4j

`pip install rdflib-neo4j` · installs (wheel) · licence: Apache 2 · rank 11285 · last release 2024-08-19 · [PyPI](https://pypi.org/project/rdflib-neo4j/)

### redis-simple-mq

Simple message queue based on Redis.

`pip install redis-simple-mq` · installs (wheel) · licence: MIT License · rank 11293 · last release 2026-07-01 · [PyPI](https://pypi.org/project/redis-simple-mq/)

<details><summary>README extract</summary>

A simple message queue for Redis.

This is a light-weight message queue based on Redis.

Key features:

- Class based API to the queue with all basic queue functions
- Queue is implement as FIFO
- All messages are stored and retrieved as UTF-8 strings
- Bulk methods for enqueue and dequeue
- No limit on the number of parallel queues
- Fully tested

Example:
```python
from redis import Redis
from simple_mq import SimpleMQ

conn = Redis()
q = SimpleMQ(conn)
q.enqueue('Hello, World!')
message = q.dequeue()
print(message)
```

Sections: redis-simple-mq, Description, Basic example

</details>

### readme-metrics

ReadMe API Metrics SDK

`pip install readme-metrics` · installs (wheel) · licence: not stated · rank 11320 · last release 2025-03-20 · [PyPI](https://pypi.org/project/readme-metrics/)

<details><summary>README extract</summary>

Track usage of your API and troubleshoot issues faster.

With ReadMe's Metrics API your team can get deep insights into your API's usage. If you're a developer, it takes a few small steps to send your API logs to ReadMe. Here's an overview of how the integration works:

- You add the ReadMe middleware to your Django, Flask, or WSGI application. ...

</details>

### runtime-builder

Allow automatic builds in edit mode

`pip install runtime-builder` · installs from source (sdist only) · licence: not stated · rank 11328 · last release 2024-01-20 · [PyPI](https://pypi.org/project/runtime-builder/)

<details><summary>README extract</summary>

Sometimes python developers want to include compiled output or other binary blob artifacts in their wheels. The source materials for this output is checked into git, but the blobs are not, since they're not source material and are at risk getting out of sync with the source distribution.

When building the wheel, the blobs need to be generated. ...

Example:
```python
from pathlib import Path
from typing import Callable

class MultiplyBuild:
    def init(self, factor: int) -> None:
        self.factor = factor

    def call(self, target_path: Path):
        source_path = target_path.with_suffix(".source")
        t = int(open(source_path).read())
        with open(target_path, "w") as f:
...
```

Sections: Runtime Builder, Example, Configuration, Build-time, Runtime

</details>

### ruff-format

Python bindings for the Ruff code formatter, built with Rust and PyO3.

`pip install ruff-format` · installs (wheel) · licence: MIT · rank 11343 · last release 2026-08-10 · [PyPI](https://pypi.org/project/ruff-format/) · [source](https://github.com/reflex-dev/ruff-format)

<details><summary>README extract</summary>

A fast Python code formatter powered by Ruff's formatting engine.

Features:
`ruff-format` is a Python package that provides Python bindings to Ruff's Python formatter.

Example:
```python
from ruff_format import format_string, is_valid_syntax, parse_code

code = """
def hello(  x,y,   z  ):
    print( x+y+z )
"""

# Check if code has valid syntax
assert is_valid_syntax(code)

# Parse code (raises RuntimeError on syntax errors)
parse_code(code)

# Format code (default line width: 80)
formatted = format_string(code)
print(formatted)

...
```

Sections: ruff-format, Overview, Usage, Prerequisites, Building from source, Links

</details>

### rest-framework-generic-relations

Generic Relations for Django Rest Framework

`pip install rest-framework-generic-relations` · installs (wheel) · licence: BSD License · rank 11486 · last release 2024-03-27 · [PyPI](https://pypi.org/project/rest-framework-generic-relations/) · [source](https://github.com/craigds/rest-framework-generic-relations)

<details><summary>README extract</summary>

This library implements Django REST Framework serializers to handle generic foreign keys.

Example:
```python
class TaggedItem(models.Model):
    tag_name = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    tagged_object = GenericForeignKey('content_type', 'object_id')
```

Sections: Rest Framework Generic Relations, Requirements, API Reference, GenericRelatedField, Writing to generic foreign keys, GenericModelSerializer, A few things you should note

</details>

### rf100vl

RF100-VL Dataset Interface

`pip install rf100vl` · installs (wheel) · licence: MIT License · rank 11605 · last release 2026-05-23 · [PyPI](https://pypi.org/project/rf100vl/)

<details><summary>README extract</summary>

A Multi-Domain Object Detection
Benchmark
for Vision-Language Models

Peter Robicheaux 1†
Matvei Popov1†
Anish Madan 2
Isaac Robinson 1

Joseph Nelson 1
Deva Ramanan 2
Neehar Peri 2

Roboflow
Carnegie Mellon University

† Equal Contribution ...

Example:
```python
from rf100vl import download_rf100vl

download_rf100vl(path="./rf100-vl/")
```

Sections: Roboflow 100-VL, Download RF100-VL, Introduction, Submission Details, Official Baseline, Timeline, References

</details>

### reflex-build-sdk

Python client for the Reflex Build API.

`pip install reflex-build-sdk` · installs (wheel) · licence: Apache-2.0 · rank 11696 · last release 2026-10-27 · [PyPI](https://pypi.org/project/reflex-build-sdk/)

<details><summary>README extract</summary>

Python client for the Reflex Build API, with synchronous and asynchronous interfaces.

Install it with the HTTP library the client should send requests with:

Without any of them, pass the client a transport of your own.

Example:
```python
from reflex_build_sdk import ReflexBuild

with ReflexBuild() as client:
    me = client.auth.me()
    print(me.email, me.tier)
```

Sections: reflex-build-sdk, Apps and projects, Custom domains, Deploying, Environments, Managed database, Signing users in, Third-party connections, Authentication, Pointing at another deployment, Google Cloud, Errors, Transports

</details>

### reuters-style

Reuters editorial formatting and Graphics chart colours

`pip install reuters-style` · installs (wheel) · licence: MIT · rank 11748 · last release 2026-10-06 · [PyPI](https://pypi.org/project/reuters-style/) · [docs](https://palewi.re/docs/reuters-style/) · [source](https://github.com/palewire/reuters-style)

<details><summary>README extract</summary>

A Python library for Reuters editorial formatting and Graphics chart colours.
The current development setup supports Python 3.11 through 3.14.

- Documentation
- Source code
- Issues
- PyPI

</details>

### realesrgan

Real-ESRGAN aims at developing Practical Algorithms for General Image Restoration

`pip install realesrgan` · installs (wheel) · licence: Apache Software License · rank 12004 · last release 2022-09-20 · [PyPI](https://pypi.org/project/realesrgan/)

<details><summary>README extract</summary>

👀Demos | 🚩Updates | ⚡Usage | 🏰Model Zoo | 🔧Install | 💻Train | ❓FAQ | 🎨Contribution

🔥 AnimeVideo-v3 model (动漫视频小模型). Please see [*anime video models*] and [*comparisons*]

🔥 RealESRGAN_x4plus_anime_6B for anime images (动漫插图模型). Please see [*anime_model*]

1. :boom: Update online Replicate demo:
1. ...

Sections: English | 简体中文, 🚩 Updates, 👀 Demos Videos, Bilibili, YouTube, ⚡ Quick Inference, Online inference, Portable executable files (NCNN), Usage of portable executable files, Python script, Usage of python script, Inference general images, Inference anime images, BibTeX

</details>

### rdp

Pure Python implementation of the Ramer-Douglas-Peucker algorithm

`pip install rdp` · installs from source (sdist only) · licence: MIT License · rank 12066 · last release 2016-12-19 · [PyPI](https://pypi.org/project/rdp/)

<details><summary>README extract</summary>

Python/NumPy implementation of the Ramer-Douglas-Peucker algorithm
(Ramer 1972; Douglas and Peucker 1973) for 2D and 3D data.

The Ramer-Douglas-Peucker algorithm is an algorithm for reducing the number
of points in a curve that is approximated by a series of points.

Example:
```python
from rdp import rdp

rdp([[1, 1], [2, 2], [3, 3], [4, 4]])
```

Sections: Ramer-Douglas-Peucker Algorithm, Usage, Links, References

</details>

### readthedocs-sphinx-ext

Sphinx extension for Read the Docs overrides

`pip install readthedocs-sphinx-ext` · installs (wheel) · licence: MIT · rank 12084 · last release 2023-12-19 · [PyPI](https://pypi.org/project/readthedocs-sphinx-ext/)

<details><summary>README extract</summary>

This module adds extensions that make Sphinx easier to use.
Some of them require Read the Docs features,
others are just code that we ship and enable during builds on Read the Docs.

We currently ship:

* An extension for building docs like Read the Docs
* `template-meta` - Allows users to specify template overrides in per-page context.

Sections: Read the Docs Sphinx Extensions, Releasing, . Increment the version in `setup.py`, . Push the tag to GitHub: `git push --tags origin main`, . Upload the package to PyPI

</details>

### rest_condition

Complex permissions flow for django-rest-framework

`pip install rest_condition` · installs from source (sdist only) · licence: MIT License · rank 12140 · last release 2016-11-01 · [PyPI](https://pypi.org/project/rest_condition/)

<details><summary>README extract</summary>

Complex permissions flow for django-rest-framework.

Example:
```python
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission
from rest_condition import ConditionalPermission, C, And, Or, Not

class Perm1(BasePermission):

   def has_permission(self, request, view):
        # You permissions check here
        return True

...
```

Sections: rest\_condition, Example

</details>

### rdrobust

Implements local polynomial Regression Discontinuity (RD) point estimators with robust bias-corrected confidence intervals and inference procedures.

`pip install rdrobust` · installs (wheel) · licence: GPL-3.0-only · rank 12170 · last release 2026-10-07 · [PyPI](https://pypi.org/project/rdrobust/)

_README extract left out: share-alike licence._

### rich-pixels

A Rich-compatible library for writing pixel images and ASCII art to the terminal.

`pip install rich-pixels` · installs (wheel) · licence: not stated · rank 12202 · last release 2024-03-30 · [PyPI](https://pypi.org/project/rich-pixels/)

<details><summary>README extract</summary>

A Rich-compatible library for writing pixel images and other colourful grids to the
terminal.

Example:
```python
from rich_pixels import Pixels
from rich.console import Console

console = Console()
pixels = Pixels.from_image_path("pokemon/bulbasaur.png")
console.print(pixels)
```

Sections: Rich Pixels, Basic Usage, Images, Image from a file, Pillow image object, ASCII Art, Using with Textual

</details>

### robocorp-browser

Robocorp browser automation library

`pip install robocorp-browser` · installs (wheel) · licence: Apache Software License · rank 12313 · last release 2026-03-13 · [PyPI](https://pypi.org/project/robocorp-browser/) · [source](https://github.com/robocorp/robocorp/)

<details><summary>README extract</summary>

The robocorp-browser package is a light wrapper for the Playwright -project, with quality-of-life improvements, such as automatic lifecycle management for Playwright objects (meant to be used with robocorp-tasks).

Example:
```python
from robocorp import browser, vault
from robocorp.tasks import task

@task
def automate_browser():
    """Start a browser to login in the surfed page."""
    # The configuration is used to set the basic `robocorp.browser` settings.
    # It must be called before calling APIs that create Playwright objects.
    browser.configure(
...
```

Sections: robocorp-browser, Usage, Guides, API Reference

</details>

### romatch

Robust Dense Feature Matching

`pip install romatch` · installs (wheel) · licence: not stated · rank 12323 · last release 2025-10-24 · [PyPI](https://pypi.org/project/romatch/)

<details><summary>README extract</summary>

Robust Dense Feature Matching
 ⭐CVPR 2024⭐

 Johan Edstedt
 Qiyu Sun
 Georg Bökman
 Mårten Wadenbäck
 Michael Felsberg

 Paper |
 Project Page

 RoMa is the robust dense feature matcher capable of estimating pixel-dense warps and reliable certainties for almost any image pair.

Example:
```python
from romatch import roma_outdoor
roma_model = roma_outdoor(device=device)
# Match
warp, certainty = roma_model.match(imA_path, imB_path, device=device)
# Sample matches for estimation
matches, certainty = roma_model.sample(warp, certainty)
# Convert to pixel coordinates (RoMa produces matches in [-1,1]x[-1,1])
...
```

Sections: RoMa 🏛️, Fused local correlation kernel, Demo / How to Use, Settings, Resolution, Sampling, Reproducing Results, Training, Tiny RoMa, Reproducibility, BibTeX

</details>

### rodi

Implementation of dependency injection for Python 3

`pip install rodi` · installs (wheel) · licence: not stated · rank 12344 · last release 2026-03-08 · [PyPI](https://pypi.org/project/rodi/)

<details><summary>README extract</summary>

Features:

* types resolution by signature types annotations (_type hints)
* types resolution by class annotations (_type hints)
* types resolution by names and aliases (_convention over configuration)
* unintrusive: builds objects graph without the need to change the
 source code of classes
* minimum overhead to obtain services, once the objects ...

Sections: Implementation of dependency injection for Python 3, Documentation, Efficient, Flexible, Examples, Recommended practices, Service life style, Usage in BlackSheep

</details>

### rucio-clients

Rucio client package

`pip install rucio-clients` · installs (wheel) · licence: Apache-2.0 · rank 12510 · last release 2026-10-21 · [PyPI](https://pypi.org/project/rucio-clients/) · [docs](https://rucio.cern.ch/documentation/) · [source](https://github.com/rucio/rucio.git)

<details><summary>README extract</summary>

Rucio is a software framework that provides functionality to organize, manage, and access large volumes of scientific data using customisable policies.
The data can be spread across globally distributed locations and across heterogeneous data centers, uniting different storage and network technologies as a single federated entity. ...

Sections: Rucio - Scientific Data Management, Documentation, Try it out, Operators

</details>

### rerun-notebook

Implementation helper for running rerun-sdk in notebooks

`pip install rerun-notebook` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 12529 · last release 2026-11-04 · [PyPI](https://pypi.org/project/rerun-notebook/)

<details><summary>README extract</summary>

Part of the Rerun project.

`rerun-notebook` is a support package for `rerun-sdk`'s notebook integration. This is an implementation package that shouldn't be directly interacted with. It is typically installed using the `notebook` extra of `rerun-sdk`:

Features:
There are several reasons for this package to be separate from the main `rerun-sdk` package:

- `rerun-notebook` includes the JS+Wasm distribution of the Rerun viewer (~31MiB). Adding it to the main `rerun-sdk` package would double its file size. ...

Sections: `rerun-notebook`, What?, Why a separate package?, Ways to access the widget assets, Inlined assets, Locally served assets, Manually hosted assets, Run from source

</details>

### random-slugs

A Python package for generating random slugs using a customizable vocabulary of words.

`pip install random-slugs` · installs (wheel) · licence: not stated · rank 12630 · last release 2024-05-26 · [PyPI](https://pypi.org/project/random-slugs/) · [source](https://github.com/fkapsahili/random-slugs/)

<details><summary>README extract</summary>

`random-slugs` is a user-friendly Python package that generates those random word slugs. This package is customizable and allows users to specify the parts of speech, categories of words, and the reproducibility.

Features:
- Generate slugs with a specified number of words
- Customize the parts of speech and categories of words used
- Choose the format of the slug (`kebab-case`, `snake_case` or `camelCase`)
- Set a random seed for reproducibility ...

Example:
```python
from random_slugs import generate_slug

slug = generate_slug()
print(slug) # E.g. 'quick-brown-fox'
```

Sections: Random Slugs, Features, Usage, Customize the Slug, API, Total Unique Slugs, Exceptions, Example

</details>

### robotpy-wpiutil

Binary wrapper for FRC WPIUtil library

`pip install robotpy-wpiutil` · installs (wheel) · licence: BSD-3-Clause · rank 12693 · last release 2026-03-13 · [PyPI](https://pypi.org/project/robotpy-wpiutil/) · [source](https://github.com/robotpy/mostrobotpy)

### ruamel.yaml.clibz

C version of reader, parser and emitter for ruamel.yaml, compiled with Zig, derived from libyaml

`pip install ruamel.yaml.clibz` · installs from source (sdist only) · licence: MIT · rank 12780 · last release 2026-01-02 · [PyPI](https://pypi.org/project/ruamel.yaml.clibz/) · [docs](https://yaml.dev/doc/ruamel.yaml.clibz) · [source](https://sourceforge.net/p/ruamel-yaml-clibz/code/ci/default/tree/)

<details><summary>README extract</summary>

`ruamel.yaml.clibz` is a C based reader/scanner and emitter for ruamel.yaml
based on the same sources as `ruamel.yaml.clib`, but compiled using Zig (with the
packages `setuptools-zig` and `ziglang`). ...

</details>

### rpy2-robjects

Python interface to the R language (embedded R)

`pip install rpy2-robjects` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 12802 · last release 2026-10-10 · [PyPI](https://pypi.org/project/rpy2-robjects/) · [docs](https://rpy2.github.io/doc.html) · [source](https://github.com/rpy2/rpy2)

_README extract left out: share-alike licence._

### runai-model-streamer-azure

(no summary)

`pip install runai-model-streamer-azure` · installs (wheel) · licence: not stated · rank 12817 · last release 2026-10-29 · [PyPI](https://pypi.org/project/runai-model-streamer-azure/)

### remotion-lambda

Remotion Lambda client

`pip install remotion-lambda` · installs (wheel) · licence: not stated · rank 12823 · last release 2026-11-05 · [PyPI](https://pypi.org/project/remotion-lambda/)

<details><summary>README extract</summary>

Remotion is a framework for creating videos programmatically using React.

</details>

### rpy2-rinterface

Low-level interface from Python to the R.

`pip install rpy2-rinterface` · installs from source (sdist only) · licence: GPL-2.0-or-later · rank 12895 · last release 2026-09-20 · [PyPI](https://pypi.org/project/rpy2-rinterface/) · [docs](https://rpy2.github.io/doc.html) · [source](https://github.com/rpy2/rpy2)

_README extract left out: share-alike licence._

### robotpy-wpimath

Binary wrapper for FRC WPIMath library

`pip install robotpy-wpimath` · installs (wheel) · licence: BSD-3-Clause · rank 12930 · last release 2026-03-13 · [PyPI](https://pypi.org/project/robotpy-wpimath/) · [source](https://github.com/robotpy/mostrobotpy)

### repo-standards

Deterministic pull-request sizing and reviewed repository policy

`pip install repo-standards` · installs (wheel) · licence: MIT · rank 12969 · last release 2026-11-07 · [PyPI](https://pypi.org/project/repo-standards/) · [docs](https://engineering.sarj.ai/projects/repo-standards/) · [source](https://github.com/sarj-ai/repo-standards)

<details><summary>README extract</summary>

`repo-standards` measures pull-request review size without executing repository code. Its
repository rules are available for review but remain disabled until individually approved
and explicitly activated by a consumer. ...

Sections: repo-standards, Where rules belong, Run it, Pull-request commit policy, Commit-message policy, Pull-request commits Action and pre-commit hook, GitHub Action, Safety model

</details>

### rapids-dask-dependency

Dask and Distributed version pinning for RAPIDS

`pip install rapids-dask-dependency` · installs (wheel) · licence: Apache-2.0 · rank 13057 · last release 2026-10-08 · [PyPI](https://pypi.org/project/rapids-dask-dependency/)

<details><summary>README extract</summary>

This repository provides metapackages for pip and conda that centralize the Dask version dependency across RAPIDS.
Dask's API instability means that each RAPIDS release must pin to a very specific Dask release to avoid incompatibilities.
These metapackages provide a centralized, versioned storehouse for that pinning. ...

Sections: Dask Metapackage, Versioning the Metapackage Itself, Patching

</details>

### real-time-monitor

A probe and a monitor to investigate your application real time behavior.

`pip install real-time-monitor` · installs (wheel) · licence: CeCILL-C · rank 13125 · last release 2026-09-14 · [PyPI](https://pypi.org/project/real-time-monitor/)

<details><summary>README extract</summary>

A monitor (GUI + probe) to inspect the real-time behavior of your code

A few dependencies are required for building:
- the GUI
- the units test

To do so, you can either install them by calling conan directly or by using the helper script setup_build.sh

This project uses Conan to manage its dependencies.

- Conan (>= 2.10)
- CMake (>= 3.28) ...

Sections: real-time-monitor, Dependency Management, Requirements, Build, Build Python Bindings

</details>

### retina-face

RetinaFace: Deep Face Detection Framework in TensorFlow, PyTorch and ONNX for Python

`pip install retina-face` · installs (wheel) · licence: MIT License · rank 13180 · last release 2026-10-09 · [PyPI](https://pypi.org/project/retina-face/)

<details><summary>README extract</summary>

RetinaFace is a deep learning based cutting-edge facial detector for Python coming with facial landmarks. Its detection performance is amazing even in the crowd as shown in the following illustration.

RetinaFace is the face detection module of insightface project. The original implementation is mainly based on mxnet. ...

</details>

### rendercanvas

One canvas API, multiple backends

`pip install rendercanvas` · installs (wheel) · licence: not stated · rank 13209 · last release 2026-11-05 · [PyPI](https://pypi.org/project/rendercanvas/) · [docs](https://rendercanvas.readthedocs.io) · [source](https://github.com/pygfx/rendercanvas)

<details><summary>README extract</summary>

rendercanvas

One canvas API, multiple backends 🚀

*This project is part of pygfx.org*

See how the two windows above look the same? That's the idea; they also look the
same to the code that renders to them. Yet, the GUI systems are very different
(Qt vs glfw in this case). Now that's a powerful abstraction!

Providing a generic API for: ...

Example:
```python
import numpy as np
from rendercanvas.auto import RenderCanvas, loop

canvas = RenderCanvas(update_mode="continuous")
context = canvas.get_bitmap_context()

@canvas.request_draw
def animate():
    w, h = canvas.get_logical_size()
    bitmap = np.random.uniform(0, 255, (h, w)).astype(np.uint8)
    context.set_bitmap(bitmap)

loop.run()
```

Sections: Introduction, Purpose, Usage, Async or not async, Quick tips

</details>

### rabbitizer

MIPS instruction decoder

`pip install rabbitizer` · installs (wheel) · licence: not stated · rank 13234 · last release 2026-05-29 · [PyPI](https://pypi.org/project/rabbitizer/)

<details><summary>README extract</summary>

MIPS instruction decoder API.

Features:
- Should produce matching assembly.
- Fully written in C for fast decoding.
 - The library is completely allocation-less, in other words `rabbitizer`
 doesn't allocate in anything in the heap by itself. ...

Sections: rabbitizer, Features, Non-features, Python bindings, Rust bindings, References

</details>

### regula-documentreader-webclient

Regula's Document Reader python client

`pip install regula-documentreader-webclient` · installs (wheel) · licence: not stated · rank 13293 · last release 2026-10-08 · [PyPI](https://pypi.org/project/regula-documentreader-webclient/)

<details><summary>README extract</summary>

Package name has been changed from `regula.documentreader.webclient` to `regula_documentreader_webclient`

Documents recognition as easy as reading two bytes.

If you have any problems with or questions about this client, please contact us
through a GitHub issue. ...

Example:
```python
from regula_documentreader_webclient import *

with open("australia_passport.jpg", "rb") as f:
    input_image = f.read()

with DocumentReaderApi(host=' as api:
    params = ProcessParams(
        scenario=Scenario.FULL_PROCESS,
        result_type_output=[Result.DOCUMENT_IMAGE, Result.STATUS, Result.TEXT, Result.IMAGES]
    )
...
```

Sections: Regula Document Reader web API Python 3.9+ client, ⚠️ Warning: Package Name Changed, Example

</details>

### rrcf

Robust random cut forest for anomaly detection

`pip install rrcf` · installs from source (sdist only) · licence: MIT · rank 13371 · last release 2023-04-30 · [PyPI](https://pypi.org/project/rrcf/)

### rootutils

Simple package for easy project root setup

`pip install rootutils` · installs (wheel) · licence: MIT · rank 13489 · last release 2023-05-19 · [PyPI](https://pypi.org/project/rootutils/)

<details><summary>README extract</summary>

A simple python package to solve all your problems with pythonpath, working directory, file paths, module imports and environment variables.

Features:
Problem: I would like to be able to:

- Run my python scripts from anywhere
- Always import python modules relatively to the project root directory ...

Example:
```python
import rootutils

# find absolute root path (searches for directory containing .project-root file)
# search starts from current file and recursively goes over parent directories
# returns pathlib object
path = rootutils.find_root(search_from=file, indicator=".project-root")

...
```

Sections: rootutils, Why rootutils?, Setup, Usage, Defaults, Autoroot, Inspirations

</details>

### robotpy-native-wpiutil

WPILib Utility Library

`pip install robotpy-native-wpiutil` · installs (wheel) · licence: BSD-3-Clause · rank 13636 · last release 2026-03-13 · [PyPI](https://pypi.org/project/robotpy-native-wpiutil/)

### rwslib

Rave Web Services for Python

`pip install rwslib` · installs (wheel) · licence: MIT · rank 13664 · last release 2025-10-30 · [PyPI](https://pypi.org/project/rwslib/) · [docs](https://rwslib.readthedocs.io) · [source](https://github.com/mdsol/rwslib)

<details><summary>README extract</summary>

The Goal of this library is to provide a (programmer) friendly client library to Rave Web Services (RWS).

Philosophy

rwslib provides a convenient interface to RWS without hiding the implementation details. ...

</details>

### repofs

File system view of git repositories

`pip install repofs` · installs from source (sdist only) · licence: Apache Software License · rank 13706 · last release 2021-02-01 · [PyPI](https://pypi.org/project/repofs/)

<details><summary>README extract</summary>

RepoFS represents the Git version control system as
a virtual file system where all commits and their contents
can be traversed concurrently in a read-only manner
using shell commands.

Read the complete description and methodology on
SoftwareX

You can cite RepoFS as follows.
Vitalis Salis and Diomidis Spinellis. ...

Sections: RepoFS, Debian & Ubuntu, Arch Linux, OSx, Usage

</details>

### robotpy-native-wpimath

WPILib Math Library

`pip install robotpy-native-wpimath` · installs (wheel) · licence: BSD-3-Clause · rank 13718 · last release 2026-03-13 · [PyPI](https://pypi.org/project/robotpy-native-wpimath/)

### rpdb

pdb wrapper with remote access via tcp socket

`pip install rpdb` · installs (wheel) · licence: not stated · rank 13732 · last release 2024-12-26 · [PyPI](https://pypi.org/project/rpdb/)

<details><summary>README extract</summary>

rpdb is a wrapper around pdb that re-routes stdin and stdout to a socket
handler. By default it opens the debugger on port 4444:

But you can change that by simply instantiating Rpdb manually:

It is known to work on Jython 2.5 to 2.7, Python 2.5 to 3.1. ...

Example:
```python
import rpdb; rpdb.set_trace()
```

Sections: rpdb - remote debugger based on pdb, Trigger rpdb with signal, Known bugs

</details>

### rtmlib

RTMPose series (RTMPose, DWPose, RTMO, RTMW, VitPose) without mmcv, mmpose, mmdet etc.

`pip install rtmlib` · installs (wheel) · licence: Apache License 2.0 · rank 13776 · last release 2026-08-04 · [PyPI](https://pypi.org/project/rtmlib/)

<details><summary>README extract</summary>

`rtmlib` is a super lightweight library to conduct human and animal pose estimation based on RTMPose and ViTPose models WITHOUT any dependencies like mmcv, mmpose, mmdet, etc.

Basically, rtmlib only requires these dependencies:

- numpy
- opencv-python
- opencv-contrib-python
- onnxruntime ...

Example:
```python
import cv2
from rtmlib import Wholebody, draw_skeleton

img = cv2.imread('./demo.jpg')

device = 'cpu'  # cpu, cuda, mps
backend = 'onnxruntime'  # opencv, onnxruntime, openvino
openpose_skeleton = False  # True for openpose-style (required for animals), False for mmpose-style

wholebody = Wholebody(to_openpose=openpose_skeleton,
...
```

Sections: rtmlib, Quick Start, Usage, WebUI, APIs, Model Zoo, Detectors, Pose Estimators, Visualization, Additional resources

</details>

### rstream

A python client for RabbitMQ Streams

`pip install rstream` · installs (wheel) · licence: MIT License · rank 13807 · last release 2026-10-19 · [PyPI](https://pypi.org/project/rstream/) · [source](https://github.com/rabbitmq-community/rstream)

<details><summary>README extract</summary>

A Python asyncio-based client for RabbitMQ Streams

The RabbitMQ stream plug-in is required. See the documentation for enabling it.

Example:
```python
 amqp_message = AMQPMessage(
  body=bytes("hello: {}".format(i), "utf-8"),
)
```

Sections: RabbitMQ Stream Python Client, Examples, Client Codecs, AMQP 1.0 codec vs Binary, Publishing messages, Publishing with confirmation, Sub-Entry Batching and Compression, Deduplication, Consuming messages, Server-side offset tracking, Superstreams, Single Active Consumer, Filtering, Connecting with SSL

</details>

### radboy

A Retail Calculator for Android/Linux

`pip install radboy` · installs (wheel) · licence: GPL-3.0-only · rank 13827 · last release 2026-11-07 · [PyPI](https://pypi.org/project/radboy/)

_README extract left out: share-alike licence._

### rdkit-pypi

A collection of chemoinformatics and machine-learning software written in C++ and Python

`pip install rdkit-pypi` · does not install on CPython 3.14 · licence: BSD-3-Clause · rank 13856 · last release 2023-02-26 · [PyPI](https://pypi.org/project/rdkit-pypi/)

<details><summary>README extract</summary>

This repository holds the code to build RDKit platform wheels for Linux, macOS, and Windows on Github Action and Circle CI. The wheels contain the compiled platform-specific dynamic libraries (`*.so`, `*.dylib`, and `*.dll`) and are available at PyPI. RDKit can easily be installed using ...

Sections: 🔥 RDKit Python Wheels, Available Builds, PIP, Poetry, Local builds on Linux

</details>

### random2

Python 3 compatible Python 2 `random` Module.

`pip install random2` · installs (wheel) · licence: Python Software Foundation License · rank 14006 · last release 2023-12-18 · [PyPI](https://pypi.org/project/random2/)

<details><summary>README extract</summary>

- Change support to Python 3.10, 3.11, 3.12, and 3.13 only.

- Fix setup.py so that an install of the package will actually work.

Sections: CHANGES, 1.0.2 (2023-12-18), 1.0.1 (2013-03-15), 1.0.0 (2013-03-06), Random 2

</details>

### ruamel.ext.msgpack

thin wrapper around msgpack to deal with naive datetime and ruamel defined extension types

`pip install ruamel.ext.msgpack` · installs (wheel) · licence: Other/Proprietary License · rank 14009 · last release 2023-08-05 · [PyPI](https://pypi.org/project/ruamel.ext.msgpack/)

<details><summary>README extract</summary>

ruamel.ext.msgpack is a thin wrapper around msgpack, that deals with naive datetime instances and ruamel defined
extension types (date).

If you try to pack a naive datetime.datetime instance, you'll get an error:

which will print: ...

Example:
```python
import datetime
from msgpack import packb

try:
    packb(datetime.datetime(2011, 10, 2), datetime=True)
except Exception as e:
    print('exception:', type(e), e)
```

Sections: ruamel.ext.msgpack, naive datetime.datetime, use_bin_type=True, extension types, datetime.date

</details>

### rainbow-api

Read chromatography and mass spectrometry binary files

`pip install rainbow-api` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 14098 · last release 2026-10-17 · [PyPI](https://pypi.org/project/rainbow-api/) · [docs](https://rainbow-api.readthedocs.io) · [source](https://github.com/evanyeyeye/rainbow)

_README extract left out: share-alike licence._

### resfo

A (lazy) parser and writer for reservoir simulator fortran output format.

`pip install resfo` · installs (wheel) · licence: LGPL-3.0-or-later · rank 14120 · last release 2026-11-02 · [PyPI](https://pypi.org/project/resfo/) · [docs](https://resfo.readthedocs.io/en/stable/) · [source](https://github.com/equinor/resfo)

_README extract left out: share-alike licence._

### requests-negotiate-sspi

This package allows for Single-Sign On HTTP Negotiate authentication using the requests library on Windows.

`pip install requests-negotiate-sspi` · installs (wheel) · licence: Apache Software License · rank 14215 · last release 2018-10-10 · [PyPI](https://pypi.org/project/requests-negotiate-sspi/)

<details><summary>README extract</summary>

An implementation of HTTP Negotiate authentication for Requests. This
module provides single-sign-on using Kerberos or NTLM using the Windows
SSPI interface.

This module supports Extended Protection for Authentication (aka Channel
Binding Hash), which makes it usable for services that require it,
including Active Directory Federation Services. ...

</details>

### runta-sdk

Python SDK for Runta runtime management

`pip install runta-sdk` · installs (wheel) · licence: MIT · rank 14301 · last release 2026-10-30 · [PyPI](https://pypi.org/project/runta-sdk/)

<details><summary>README extract</summary>

This package provides matching async and sync SDKs. Both call the public
`runta-api` HTTP/JSON service; they do not speak control-plane gRPC directly.

Example:
```python
runtime.files.upload("./project", "/workspace/project")
runtime.files.download("/workspace/dist", "./artifacts/")
```

Sections: Runta Python SDK, Public REST endpoint lifecycle test, REST contract, Generate API reference, Live tests

</details>

### resource-backed-dask-array

experimental Dask array that opens/closes a resource when computing

`pip install resource-backed-dask-array` · installs (wheel) · licence: BSD License · rank 14370 · last release 2022-02-18 · [PyPI](https://pypi.org/project/resource-backed-dask-array/) · [source](https://github.com/tlambert03/resource-backed-dask-array)

<details><summary>README extract</summary>

`ResourceBackedDaskArray` is an experimental Dask array subclass
that opens/closes a resource when computing (but only once per compute call).

Example:
```python
>>> from resource_backed_dask_array import resource_backed_dask_array
>>> safe_dsk_ary = resource_backed_dask_array(dsk_ary, fr)
>>> safe_dsk_ary.compute().shape
(4, 4, 4)

>>> fr.closed  # leave it as we found it
True
```

Sections: resource-backed-dask-array, motivation for this package, usage, Important Caveats

</details>

### re-assert

show where your regex match assertion failed!

`pip install re-assert` · installs (wheel) · licence: MIT License · rank 14378 · last release 2020-02-25 · [PyPI](https://pypi.org/project/re-assert/)

<details><summary>README extract</summary>

show where your regex match assertion failed!

Example:
```python
>>> import re
>>> reg = re.compile('foo')
>>> Matches.from_pattern(reg) == 'fork'
False
>>> Matches.from_pattern(reg) == 'food'
True
```

Sections: re-assert, usage, `re_assert.Matches(pattern: str, *args, **kwargs)`, `Matches.eq(other)` (`==`), `Matches.repr()` (`repr(...)`), `Matches.assert_matches(s: str)`

</details>

### rustypot

(no summary)

`pip install rustypot` · installs from source (sdist only) · licence: not stated · rank 14497 · last release 2026-10-14 · [PyPI](https://pypi.org/project/rustypot/)

### runtime-type-checker

Runtime-type-checker performs type check at runtime with help of type annotations

`pip install runtime-type-checker` · installs (wheel) · licence: MIT License · rank 14516 · last release 2024-02-28 · [PyPI](https://pypi.org/project/runtime-type-checker/) · [source](https://github.com/pjcampi/runtime-type-checker)

<details><summary>README extract</summary>

This package performs type-check at runtime with help of type annotations.

Example:
```python
from typing import List, Sequence, Optional, Mapping
from dataclasses import dataclass
from runtime_type_checker import check_type

check_type("a", str)  # OK
check_type(["a"], List[str])  # OK
check_type(["a", 1], Sequence[str])  # raises TypeError

@dataclass
class Foo:
    a: int
    b: Optional[Mapping[str, int]] = None

...
```

Sections: runtime-type-checker, How to use this package, 1- the `check_type` function, 2- The check_types decorator, Package features and short-comings, 1- Features, 2- Short-comings

</details>

### rispy

A Python reader/writer of RIS reference files

`pip install rispy` · installs (wheel) · licence: MIT License · rank 14545 · last release 2025-05-23 · [PyPI](https://pypi.org/project/rispy/) · [source](https://github.com/mrtango/rispy)

<details><summary>README extract</summary>

A Python reader/writer of RIS reference files.

*Pronunciation* - `rispee` - like "crispy", but without the c.

Example:
```python
>>> import rispy
>>> filepath = 'tests/data/example_full.ris'
>>> with open(filepath, 'r') as bibliography_file:
...     entries = rispy.load(bibliography_file)
...     for entry in entries:
...         print(entry['id'])
...         print(entry['first_authors'])
12345
['Marx, Karl', 'Lindgren, Astrid']
12345
['Marxus, Karlus', 'Lindgren, Astrid']
```

...

</details>

### rbo

Simple library to calculate Rank-biased Overlap between two lists

`pip install rbo` · installs (wheel) · licence: MIT License · rank 14555 · last release 2023-01-31 · [PyPI](https://pypi.org/project/rbo/) · [source](https://github.com/changyaochen/rbo)

<details><summary>README extract</summary>

This project contains a Python implementation of Rank-Biased Overlap (RBO) from: Webber, William, Alistair Moffat, and Justin Zobel. "A similarity measure for indefinite rankings." ACM Transactions on Information Systems (TOIS) 28.4 (2010): 20." (Download). ...

Example:
```python
In [1]: import rbo

In [2]: S = [1, 2, 3]

In [3]: T = [1, 3, 2]

In [4]: rbo.RankingSimilarity(S, T).rbo()
Out[4]: 0.8333333333333334
```

Sections: Rank-biased Overlap (RBO), Introduction, Usage, Computing RBO, Computing extrapolated RBO

</details>

### rison

Rison encoder/decoder

`pip install rison` · installs (wheel) · licence: MIT · rank 14558 · last release 2026-04-26 · [PyPI](https://pypi.org/project/rison/)

<details><summary>README extract</summary>

Features:
Rison is intended to meet the following goals, in roughly this order:

- Comply with URI specifications and usage
- Express nested data structures
- Be human-readable
- Be compact ...

Example:
```python
>>> import rison
>>> rison.dumps({'foo': 'bar'})
'(foo:bar)'
>>> rison.loads('(foo:bar)')
{'foo': 'bar'}
>>> rison.dumps({'foo': 'bar'}, format='O')
'foo:bar'
>>> rison.dumps(['foo', 'bar'], format='A')
'foo,bar'
```

Sections: rison, a Python encoder/decoder for Rison, Quickstart, API notes, Pygments lexers, Rison - Compact Data in URIs, Why another data serialization format?, Differences from JSON syntax, Interaction with URI %-encoding, Interaction with IRIs, Emailing URIs, Further Rationale, Variations, O-Rison, A-Rison

</details>

### rst2html

reStructuredText to html

`pip install rst2html` · installs from source (sdist only) · licence: Public Domain · rank 14604 · last release 2020-07-15 · [PyPI](https://pypi.org/project/rst2html/)

<details><summary>README extract</summary>

Example:
```python
from rst2html import rst2html

html, warning = rst2html('reStructuredText string')
```

</details>

### redlock

Distributed locks with Redis

`pip install redlock` · installs from source (sdist only) · licence: MIT License · rank 14713 · last release 2015-12-21 · [PyPI](https://pypi.org/project/redlock/)

<details><summary>README extract</summary>

This library implements the RedLock algorithm introduced by
@antirez

There are already a few redis based lock implementations in the Python
world, e.g. retools,
redis-lock.

However, these libraries can only work with *single-master* redis
server. When the Redis master goes down, your application has to face a
single point of failure . ...

Example:
```python
from redlock import RedLock
# By default, if no redis connection details are
# provided, RedLock uses redis://127.0.0.1:6379/0
lock =  RedLock("distributed_lock")
lock.acquire()
do_something()
lock.release()
```

...

</details>

### relplot

Compute and plot reliability diagrams based on calibration distance.

`pip install relplot` · installs (wheel) · licence: not stated · rank 14791 · last release 2025-11-04 · [PyPI](https://pypi.org/project/relplot/)

<details><summary>README extract</summary>

`relplot` is a Python package for plotting reliability diagrams and measuring calibration error,
in a theoretically-principled way.
The package generates reliability diagrams as shown on the right:

*How to Read the Diagram*

pairs of predicted probability and true outcomes $(f_i, y_i) \in [0, 1] \times \{0, 1\}$. ...

Example:
```python
import relplot as rp

# ...
# f: array of probabilities [f_i]
# y: array of binary labels [y_i]

calib_error = rp.smECE(f, y)   # compute calibration error (scalar)
fig, ax = rp.rel_diagram(f, y) # plot
```

Sections: relplot: Principled Reliability Diagrams, Getting Started, Manual Bandwidth, Data Format, Multi-class Confidence Calibration, Customization and Usage Tips, Additional Notebooks and Features

</details>

### rox

Rollout.io ROX Python SDK

`pip install rox` · installs (wheel) · licence: Other/Proprietary License · rank 14814 · last release 2025-07-23 · [PyPI](https://pypi.org/project/rox/)

<details><summary>README extract</summary>

Rollout is a Secure Feature Managment Solution for the Enterprise.

> Accelerate development and minimize the risk of deploying new code with simple to create feature flags, controlled rollouts, advanced target groups & deployment rules.

Sections: Getting Started, Documentation, Rollout Python SDK, Feedback

</details>

### rdiff

A native python implementation of the rdiff tool by librsync

`pip install rdiff` · installs (wheel) · licence: not stated · rank 14816 · last release 2024-03-24 · [PyPI](https://pypi.org/project/rdiff/)

<details><summary>README extract</summary>

This project is an implementation of the rdiff tool of librsync used for finding
the diff of a file on a remote machine.

This tool isn't concerned with how the signature, and delta files are
sent/received over the network. It's only concerned with working with these files
and performing the patch.

Example:
```python
import rdiff

# create an instance of the checksum class
checksum = rdiff.signature.Checksum()

# Create an instance of the signature class, passing in the checksum object
# Optionally a blocksize can be specified, defaults to 1024 bytes
signature = rdiff.signature.Signature(checksum=checksum)

# create the signature file
...
```

Sections: RDIFF, Note, Usage, File Formats, Further Reading

</details>

### rtfunicode

Encoder for unicode to RTF 1.5 command sequences

`pip install rtfunicode` · installs (wheel) · licence: BSD-2-Clause · rank 14852 · last release 2026-01-17 · [PyPI](https://pypi.org/project/rtfunicode/) · [source](https://github.com/mjpieters/rtfunicode)

<details><summary>README extract</summary>

This module implements an encoder for unicode to RTF 1.5 command sequences; it
can be used to generate valid RTF output with international characters.

Importing this module adds a new `rtfunicode` codec, allowing you to encode
unicode strings to valid RTF bytecode sequences: ...

Example:
```python
>>> import rtfunicode
>>> 'RTF and unicode mix just fine! \u263A'.encode('rtfunicode')
'RTF and unicode mix just fine! \\u9786?'
```

Sections: Unicode to RTF command code conversion, Requirements, Linting and formatting

</details>

