# Unclassified / S (part 1 of 2)

[Index](README.md) · 537 packages in this topic, by downloads.

part 1 · [part 2](unclassified-s-2.md)

### s3transfer

An Amazon S3 Transfer Manager

`pip install s3transfer` · installs (wheel) · licence: Apache Software License · rank 33 · last release 2026-10-19 · [PyPI](https://pypi.org/project/s3transfer/)

<details><summary>README extract</summary>

S3transfer is a Python library for managing Amazon S3 transfers.
This project is maintained and published by Amazon Web Services.

</details>

### sniffio

Sniff out which async library your code is running under

`pip install sniffio` · installs (wheel) · licence: Apache Software License; MIT License · rank 73 · last release 2024-02-25 · [PyPI](https://pypi.org/project/sniffio/) · [docs](https://sniffio.readthedocs.io/)

<details><summary>README extract</summary>

You're writing a library. You've decided to be ambitious, and support
multiple async I/O packages, like Trio, and asyncio, and ... You've
written a bunch of clever code to handle all the differences. But...
how do you know *which* piece of clever code to run? ...

Example:
```python
from sniffio import current_async_library
import trio
import asyncio

async def print_library():
    library = current_async_library()
    print("This is:", library)

# Prints "This is trio"
trio.run(print_library)

# Prints "This is asyncio"
asyncio.run(print_library())
```

</details>

### s3fs

Convenient Filesystem interface over S3

`pip install s3fs` · installs (wheel) · licence: BSD License · rank 113 · last release 2026-09-18 · [PyPI](https://pypi.org/project/s3fs/)

### sortedcontainers

Sorted Containers -- Sorted List, Sorted Dict, Sorted Set

`pip install sortedcontainers` · installs (wheel) · licence: Apache Software License · rank 136 · last release 2021-05-16 · [PyPI](https://pypi.org/project/sortedcontainers/)

<details><summary>README extract</summary>

Sorted Containers is an Apache2 licensed sorted collections library,
written in pure-Python, and fast as C-extensions.

Python's standard library is great until you need a sorted collections
type. ...

Features:
- Pure-Python
- Fully documented
- Benchmark comparison (alternatives, runtimes, load-factors)
- 100% test coverage
- Hours of stress testing
- Performance matters (often faster than C implementations) ...

Example:
```python
>>> import sortedcontainers
>>> help(sortedcontainers)
>>> from sortedcontainers import SortedDict
>>> help(SortedDict)
>>> help(SortedDict.popitem)
```

Sections: Python Sorted Containers, Testimonials, Features, Quickstart, Documentation, Talks, Resources

</details>

### smmap

A pure Python implementation of a sliding window memory map manager

`pip install smmap` · installs (wheel) · licence: BSD License · rank 232 · last release 2026-03-09 · [PyPI](https://pypi.org/project/smmap/)

<details><summary>README extract</summary>

When reading from many possibly large files in a fashion similar to random access, it is usually the fastest and most efficient to use memory maps.

Although memory maps have many advantages, they represent a very limited system resource as every map uses one file descriptor, whose amount is limited per process. ...

Features:
Smmap wraps an interface around mmap and tracks the mapped files as well as the amount of clients who use it. If the system runs out of resources, or if a memory limit is reached, it will automatically unload unused maps to allow continued ...

Sections: Motivation, Limitations, Overview, Prerequisites, Homepage and Links

</details>

### sqlglot

An easily customizable SQL parser and transpiler

`pip install sqlglot` · installs (wheel) · licence: MIT · rank 318 · last release 2026-11-06 · [PyPI](https://pypi.org/project/sqlglot/) · [docs](https://sqlglot.com/sqlglot.html) · [source](https://github.com/tobymao/sqlglot)

<details><summary>README extract</summary>

SQLGlot is a no-dependency SQL parser, transpiler, optimizer, and engine. It can be used to format SQL or translate between over 30 dialects like DuckDB, Presto / Trino, Spark / Databricks, Snowflake, and BigQuery. It aims to read a wide variety of SQL inputs and output syntactically and semantically correct SQL in the targeted dialects. ...

Example:
```python
import sqlglot
sqlglot.transpile("SELECT EPOCH_MS(1618088028295)", read="duckdb", write="hive")[0]
```

Sections: Versioning, Get in Touch, FAQ, Examples, Formatting and Transpiling, Metadata, Parser Errors, Build and Modify SQL, SQL Optimizer, AST Introspection, AST Diff, Custom Dialects, SQL Execution, Used By

</details>

### scramp

An implementation of the SCRAM protocol.

`pip install scramp` · installs (wheel) · licence: MIT-0 · rank 383 · last release 2026-10-25 · [PyPI](https://pypi.org/project/scramp/)

<details><summary>README extract</summary>

A Python implementation of the SCRAM authentication protocol.
Scramp supports the following mechanisms:

- SCRAM-SHA-1
- SCRAM-SHA-1-PLUS
- SCRAM-SHA-256
- SCRAM-SHA-256-PLUS
- SCRAM-SHA-512
- SCRAM-SHA-512-PLUS
- SCRAM-SHA3-512
- SCRAM-SHA3-512-PLUS

Example:
```python
>>> from scramp import ScramClient, ScramMechanism
>>>
>>> USERNAME = 'user'
>>> PASSWORD = 'pencil'
>>> MECHANISMS = ['SCRAM-SHA-256']
>>>
>>>
>>> # Choose a mechanism for our server
>>> m = ScramMechanism()  # Default is SCRAM-SHA-256
>>>
>>> # On the server side we create the authentication information for each user
...
```

...

</details>

### synchronicity

Export blocking and async library versions from a single async implementation

`pip install synchronicity` · installs (wheel) · licence: Apache Software License · rank 481 · last release 2026-10-26 · [PyPI](https://pypi.org/project/synchronicity/)

<details><summary>README extract</summary>

Python 3 has some amazing support for async programming but it's arguably made it a bit harder to develop libraries. Are you tired of implementing synchronous _and_ asynchronous methods doing basically the same thing? This might be a simple solution for you.

Example:
```python
@synchronizer.wrap
class DBConnection:
    def init(self, url):
        self._url = url

    async def connect(self):
        self._connection = await connect_to_database(self._url)

    async def query(self, q):
        return await self._connection.run_query(q)

# Now we can call it synchronously, if we want to
...
```

...

</details>

### StrEnum

An Enum that inherits from str.

`pip install StrEnum` · installs (wheel) · licence: MIT License · rank 551 · last release 2026-10-31 · [PyPI](https://pypi.org/project/StrEnum/) · [docs](https://strenum.readthedocs.io/)

<details><summary>README extract</summary>

StrEnum is a Python `enum.Enum` that inherits from `str` to complement
`enum.IntEnum` in the standard library. Supports python 3.7+.

Example:
```python
from enum import auto
from strenum import StrEnum

class HttpMethod(StrEnum):
    GET = auto()
    HEAD = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()
    CONNECT = auto()
    OPTIONS = auto()
    TRACE = auto()
    PATCH = auto()

assert HttpMethod.GET == "GET"

# You can use StrEnum values just like strings:

...
```

Sections: StrEnum, Usage, Running the tests, Releasing

</details>

### stevedore

Manage dynamic plugins for Python applications

`pip install stevedore` · installs (wheel) · licence: Apache-2.0 · rank 582 · last release 2026-08-20 · [PyPI](https://pypi.org/project/stevedore/) · [source](https://opendev.org/openstack/stevedore)

<details><summary>README extract</summary>

Python makes loading code dynamically easy, allowing you to configure
and extend your application by discovering and loading extensions
("*plugins*") at runtime. Many applications implement their own
library for doing this, using `import` or `importlib`. ...

</details>

### storage3

Supabase Storage client for Python.

`pip install storage3` · installs (wheel) · licence: MIT · rank 641 · last release 2026-11-06 · [PyPI](https://pypi.org/project/storage3/) · [docs](https://supabase.github.io/storage-py) · [source](https://github.com/supabase/supabase-py)

<details><summary>README extract</summary>

Python Client library to interact with Supabase Storage.

`storage3` only guarantees compatibility with the latest Supabase Storage release. Older Supabase Storage releases are supported on a best-effort basis, but compatibility is not guaranteed. ...

Example:
```python
from storage3 import AsyncStorageClient

url = "
key = "<your api key>"
headers = {"apiKey": key, "Authorization": f"Bearer {key}"}

storage_client = AsyncStorageClient(url, headers)

async def get_buckets():
  await storage_client.list_buckets()
```

Sections: Storage-py, Supabase Service Compatibility, How to use, Uploading files

</details>

### supabase

Supabase client for Python.

`pip install supabase` · installs (wheel) · licence: MIT · rank 643 · last release 2026-11-06 · [PyPI](https://pypi.org/project/supabase/) · [docs](https://github.com/supabase/supabase-py/src/supabase) · [source](https://github.com/supabase/supabase-py)

<details><summary>README extract</summary>

Python client for Supabase

- Documentation: supabase.com/docs

 - GitHub OAuth in your Python Flask app
 - Python data loading with Supabase

Example:
```python
import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
```

Sections: `supabase-py`, Supabase Service Compatibility, Usage, Sign-up, Sign-in, Insert Data, Select Data, Update Data, Update data with duplicate keys, Delete Data, Call Edge Functions, Download a file from Storage, Upload a file, Remove a file

</details>

### supabase-auth

Python Client Library for Supabase Auth

`pip install supabase-auth` · installs (wheel) · licence: MIT · rank 677 · last release 2026-11-06 · [PyPI](https://pypi.org/project/supabase-auth/) · [docs](https://github.com/supabase/supabase-py/tree/main/src/auth) · [source](https://github.com/supabase/supabase-py)

<details><summary>README extract</summary>

This is a Python port of the supabase js gotrue client. The current state is that there is a features parity but with small differences that are mentioned in the section Differences to the JS client. As of December 14th, we renamed to repo from `gotrue-py` to `auth-py` to mirror the changes in the JavaScript library.

Features:
- Full feature parity with the JavaScript client
- Support for both synchronous and asynchronous operations
- MFA (Multi-Factor Authentication) support
- OAuth and SSO integration
- Magic link and OTP authentication
- Phone number authentication ...

Example:
```python
from supabase_auth import SyncGoTrueClient

headers = {
    "apiKey": "my-mega-awesome-api-key",
    # ... any other headers you might need.
}
...

</details>

### supabase-functions

Library for Supabase Functions

`pip install supabase-functions` · installs (wheel) · licence: MIT · rank 681 · last release 2026-11-06 · [PyPI](https://pypi.org/project/supabase-functions/) · [source](https://github.com/supabase/supabase-py)

<details><summary>README extract</summary>

Example:
```python
import asyncio
from supabase_functions import AsyncFunctionsClient

async def run_func():
    # Initialize the client with your project URL and optional headers
    headers = {
        "Authorization": "Bearer your-publishable-key",
        # Add any other headers you might need
    }

    fc = AsyncFunctionsClient(" headers)

    try:
...
```

Sections: Functions-py, Pip, UV, Poetry, Supabase Service Compatibility, Usage, Asynchronous Client, Synchronous Client

</details>

### simple-websocket

Simple WebSocket server and client for Python

`pip install simple-websocket` · installs (wheel) · licence: MIT License · rank 691 · last release 2024-10-10 · [PyPI](https://pypi.org/project/simple-websocket/)

<details><summary>README extract</summary>

Simple WebSocket server and client for Python.

- Documentation
- PyPI
- Change Log

Sections: simple-websocket, Resources

</details>

### slowapi

A rate limiting extension for Starlette and Fastapi

`pip install slowapi` · installs (wheel) · licence: MIT License · rank 750 · last release 2026-06-13 · [PyPI](https://pypi.org/project/slowapi/) · [docs](https://slowapi.readthedocs.io/en/latest/) · [source](https://github.com/laurents/slowapi)

<details><summary>README extract</summary>

A rate limiting library for Starlette and FastAPI adapted from flask-limiter.

This package is used in various production setups, handling millions of requests per month, and seems to behave as expected.
There might be some API changes when changing the code to be fully `async`, but we will notify users via appropriate `semver` version changes. ...

Features:
Most feature are coming from FlaskLimiter and the underlying limits.

Supported now:

- Single and multiple `limit` decorator on endpoint functions to apply limits
- redis, memcached and memory backends to track your limits (memory as a fallback) ...

Example:
```python
@limiter.limit("5/minute")
async def myendpoint(request: Request)
    pass
```

Sections: SlowApi, Quick start, Features, Limitations and known issues

</details>

### sendgrid

Twilio SendGrid library for Python

`pip install sendgrid` · installs (wheel) · licence: MIT · rank 777 · last release 2025-09-19 · [PyPI](https://pypi.org/project/sendgrid/)

<details><summary>README extract</summary>

This library allows you to quickly and easily use the Twilio SendGrid Web API v3 via Python.

NEW:

- Version 6.X release is a BREAKING CHANGE from version 5.X, please see the release notes for details.
- Send SMS messages with Twilio.

This library provides full support for all Twilio SendGrid Web API v3 endpoints, including v3 /mail/send. ...

Example:
```python
import os
from sendgrid import SendGridAPIClient

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
response = sg.client.suppression.bounces.get()
print(response.status_code)
print(response.body)
print(response.headers)
```

...

</details>

### spacy-loggers

Logging utilities for SpaCy

`pip install spacy-loggers` · installs (wheel) · licence: MIT · rank 816 · last release 2023-09-11 · [PyPI](https://pypi.org/project/spacy-loggers/)

<details><summary>README extract</summary>

Starting with spaCy v3.2, alternate loggers are moved into a separate package
so that they can be added and updated independently from the core spaCy
library.

`spacy-loggers` currently provides loggers for:

- Weights & Biases
- MLflow
- ClearML
- PyTorch
- CuPy ...

Sections: spacy-loggers: Logging utilities for spaCy, Loggers, WandbLogger, Usage, Example config, MLflowLogger, ClearMLLogger, PyTorchLogger

</details>

### swifter

A package which efficiently applies any function to a pandas dataframe or series in the fastest available manner

`pip install swifter` · installs from source (sdist only) · licence: not stated · rank 840 · last release 2023-07-31 · [PyPI](https://pypi.org/project/swifter/)

### snowplow-tracker

Snowplow event tracker for Python. Add analytics to your Python and Django apps, webapps and games

`pip install snowplow-tracker` · installs (wheel) · licence: Apache Software License · rank 858 · last release 2025-02-21 · [PyPI](https://pypi.org/project/snowplow-tracker/)

<details><summary>README extract</summary>

Overview

Add analytics to your Python apps and Python games with the
Snowplow event tracker for
Python.

With this tracker you can collect event data from your Python-based
applications, games or Python web servers/frameworks.

Find out more

 | Snowplow Docs | API Docs | Contributing |

 | | | |
 | Snowplow Docs | API Docs| Contributing | ...

</details>

### swebench

The official SWE-bench package - a benchmark for evaluating LMs on software engineering

`pip install swebench` · installs (wheel) · licence: MIT License · rank 896 · last release 2026-08-18 · [PyPI](https://pypi.org/project/swebench/) · [docs](https://github.com/swe-bench/SWE-bench) · [source](http://github.com/swe-bench/SWE-bench)

<details><summary>README extract</summary>

[ Read the Docs ]

 日本語 |
 中文简体 |
 中文繁體

Code and data for the following works:
* [ICLR 2025] SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?
* [ICLR 2024 Oral] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

* [Jan. ...

Example:
```python
from datasets import load_dataset
swebench = load_dataset('princeton-nlp/SWE-bench', split='test')
```

Sections: 📰 News, 👋 Overview, 🚀 Set Up, 💽 Usage, ⬇️ Downloads, Our Other Projects

</details>

### slack-bolt

The Bolt Framework for Python

`pip install slack-bolt` · installs (wheel) · licence: MIT License · rank 953 · last release 2026-07-15 · [PyPI](https://pypi.org/project/slack-bolt/) · [docs](https://docs.slack.dev/tools/bolt-python/) · [source](https://github.com/slackapi/bolt-python)

<details><summary>README extract</summary>

A Python framework to build Slack apps in a flash with the latest platform features. Read the getting started guide and look at our code examples to learn how to build apps using Bolt. The Python module documents are available here.

Example:
```python
import logging
logging.basicConfig(level=logging.DEBUG)

from slack_bolt import App

# export SLACK_SIGNING_SECRET=***
# export SLACK_BOT_TOKEN=xoxb-***
app = App()

# Add functionality here

if name == "main":
    app.start(3000)  # POST
```

Sections: Bolt for Python, Setup, Creating an app, Running an app, Running a Socket Mode app, Listening for events, Making things happen, Creating an async app, Getting Help

</details>

### sagemaker

Open source library for training and deploying models on Amazon SageMaker.

`pip install sagemaker` · installs (wheel) · licence: Apache Software License · rank 999 · last release 2026-11-05 · [PyPI](https://pypi.org/project/sagemaker/)

<details><summary>README extract</summary>

SageMaker Python SDK is an open source library for training and deploying machine learning models on Amazon SageMaker.

With the SDK, you can train and deploy models using popular deep learning frameworks Apache MXNet and PyTorch. ...

Example:
```python
from sagemaker.estimator import Estimator
estimator = Estimator(
    image_uri="my-training-image",
    role="arn:aws:iam::123456789012:role/SageMakerRole",
    instance_count=1,
    instance_type="ml.m5.xlarge",
    output_path="s3://my-bucket/output"
)
estimator.fit({"training": "s3://my-bucket/train"})
```

...

</details>

### sseclient-py

SSE client for Python

`pip install sseclient-py` · installs (wheel) · licence: Apache Software License v2 · rank 1107 · last release 2026-01-02 · [PyPI](https://pypi.org/project/sseclient-py/)

<details><summary>README extract</summary>

A Python client for SSE event sources that seamlessly integrates with
`urllib3` and `requests`.

Example:
```python
import sseclient

def with_urllib3(url):
    """Get a streaming response for the given event feed using urllib3."""
    import urllib3
    http = urllib3.PoolManager()
    res = http.request('GET', url, preload_content=False)
    yield from sseclient.SSEClient(res).events()

def with_requests(url):
...
```

Sections: Server Side Events (SSE) client for Python, Usage, Resources

</details>

### smdebug-rulesconfig

SMDebug RulesConfig

`pip install smdebug-rulesconfig` · installs (wheel) · licence: Apache Software License · rank 1165 · last release 2020-12-18 · [PyPI](https://pypi.org/project/smdebug-rulesconfig/)

<details><summary>README extract</summary>

This library, intended to be used with Amazon SageMaker Python SDK, helps you specify builtin rules without worrying about any details or tweak the configuration of builtin rules. ...

</details>

### sentinels

Various objects to denote special meanings in python

`pip install sentinels` · installs (wheel) · licence: BSD 3-Clause License · rank 1304 · last release 2025-08-12 · [PyPI](https://pypi.org/project/sentinels/)

<details><summary>README extract</summary>

Features:
The sentinels module is a small utility providing the Sentinel class, along with useful instances.

Example:
```python
>>> from sentinels import NOTHING
```

Sections: Overview, What are Sentinels?, Why Do I Need Sentinels?, Semantics

</details>

### slicer

A small package for big slicing.

`pip install slicer` · installs (wheel) · licence: MIT License · rank 1306 · last release 2024-03-09 · [PyPI](https://pypi.org/project/slicer/)

<details><summary>README extract</summary>

*(Equal Contribution) Samuel Jenkins & Harsha Nori & Scott Lundberg*

slicer wraps tensor-like objects and provides a uniform slicing interface via `getitem`.

It supports many data types including:

numpy |
pandas |
scipy |
pytorch |
list |
tuple |
dict

And enables upgraded slicing functionality on its objects: ...

Example:
```python
from slicer import Slicer as S
li = [[1, 2, 3], [4, 5, 6]]
S(li)[:, 0:2].o
# [[1, 2], [4, 5]]
di = {'x': [1, 2, 3], 'y': [4, 5, 6]}
S(di)[:, 0:2].o
# {'x': [1, 2], 'y': [4, 5]}
```

Sections: slicer [alpha], Getting Started, Contact us

</details>

### sqlalchemy-spanner

SQLAlchemy dialect integrated into Cloud Spanner database

`pip install sqlalchemy-spanner` · installs (wheel) · licence: Apache Software License · rank 1339 · last release 2026-09-03 · [PyPI](https://pypi.org/project/sqlalchemy-spanner/)

<details><summary>README extract</summary>

Spanner dialect for SQLAlchemy represents an interface API designed to
make it possible to control Cloud Spanner databases with SQLAlchemy API.
The dialect is built on top of the Spanner DB
API,
which is designed in accordance with
PEP-249.

Known limitations are listed here. ...

Example:
```python
engine = create_engine(
    "spanner+spanner:///projects/project-id/instances/instance-id/databases/database-id",
    connect_args={'client': spanner.Client(project="project-id")},
    isolation_level="SERIALIZABLE"
)
```

Sections: Spanner dialect for SQLAlchemy, Quick Start, Samples, A Minimal App, Database URL, Create a table, Insert a row, Read, Migration, Features and limitations, Interleaved tables, Commit timestamps, Unique constraints, Automatic transaction retry

</details>

### scantree

Flexible recursive directory iterator: scandir meets glob("**", recursive=True)

`pip install scantree` · installs (wheel) · licence: MIT · rank 1341 · last release 2024-08-03 · [PyPI](https://pypi.org/project/scantree/)

<details><summary>README extract</summary>

Recursive directory iterator supporting:

- flexible filtering including wildcard path matching
- in memory representation of file-tree (for repeated access)
- efficient access to directory entry properties (`os.DirEntry` interface) extended with real path and path relative to the recursion root directory
- detection and handling of cyclic symlinks

Example:
```python
from scantree import scantree, RecursionFilter

tree = scantree('/path/to/dir', RecursionFilter(match=['*.txt']))
print([path.relative for path in tree.filepaths()])
print([path.real for path in tree.filepaths()])
```

Sections: `scantree`, Usage

</details>

### std-uritemplate

std-uritemplate implementation for Python

`pip install std-uritemplate` · installs (wheel) · licence: Apache Software License · rank 1365 · last release 2026-10-30 · [PyPI](https://pypi.org/project/std-uritemplate/) · [source](https://github.com/std-uritemplate/std-uritemplate)

<details><summary>README extract</summary>

This is a complete and maintained cross-language implementation of the Uri Template specification RFC 6570 Level 4.

> [!NOTE]
> Low activity is this repository is expected as long as there are no outstanding bug reports the implementations are considered stable and mature.

| Language | Complete | Reviewed | Published | ...

Example:
```python
from stduritemplate import StdUriTemplate

...

StdUriTemplate.expand(template, substitutions)
```

Sections: std-uritemplate, Available implementations, Usage, Java, Python, Typescript/Javascript, Go, C, Ruby, PHP, Swift, Dart, Rust, Design decisions

</details>

### striprtf

A simple library to convert rtf to text

`pip install striprtf` · installs (wheel) · licence: BSD-3-Clause · rank 1453 · last release 2026-10-24 · [PyPI](https://pypi.org/project/striprtf/) · [source](https://github.com/joshy/striprtf.git)

<details><summary>README extract</summary>

This is a library to convert Rich Text Format (RTF) files to plain text files. A lot of medical documents are written in RTF format which is not ideal for parsing and further processing. This library converts it to plain old text.

Example:
```python
from striprtf.striprtf import rtf_to_text
rtf = "some rtf encoded string"
text = rtf_to_text(rtf)
print(text)
```

Sections: striprtf, Purpose, How to use it, Online version, PostgreSQL

</details>

### smbprotocol

Interact with a server using the SMB 2/3 Protocol

`pip install smbprotocol` · installs (wheel) · licence: MIT · rank 1480 · last release 2026-07-07 · [PyPI](https://pypi.org/project/smbprotocol/)

<details><summary>README extract</summary>

Features:
* Negotiation of the SMB 2.0.2 protocol to SMB 3.1.1 (Windows 10/Server 2016)
* Authentication with both NTLM and Kerberos
* Message signing
* Message encryption (SMB 3.x.x+)
* Connect to a Tree/Share
* Opening of files, pipes and directories
* Set ...

Example:
```python
try:
    from gssapi.raw import inquire_sec_context_by_oid
    print("python-gssapi extension is available")
except ImportError as exc:
    print(f"python-gssapi extension is not available: {exc}")
```

Sections: Features, Requirements, Additional Info, Examples, smbclient Interface, Logging, Backlog

</details>

### starkbank-ecdsa

A lightweight and fast pure python ECDSA library

`pip install starkbank-ecdsa` · installs (wheel) · licence: MIT License · rank 1543 · last release 2026-04-23 · [PyPI](https://pypi.org/project/starkbank-ecdsa/)

<details><summary>README extract</summary>

Features:
We tried other Python libraries such as [python-ecdsa], [fast-ecdsa] and other less famous ones, but we didn't find anything that suited our needs. The first one was pure Python, but it was too slow. ...

Example:
```python
from json import dumps
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey

# Generate privateKey from PEM string
privateKey = PrivateKey.fromPem("""
    -----BEGIN EC PARAMETERS-----
    BgUrgQQACg==
    -----END EC PARAMETERS-----
    -----BEGIN EC PRIVATE KEY-----
...
```

Sections: A lightweight and fast pure Python ECDSA, Overview, Curves, Speed, Sample Code, OpenSSL, Run unit tests, Run benchmark

</details>

### sqlite-vec

(no summary)

`pip install sqlite-vec` · installs (wheel) · licence: MIT License, Apache License, Version 2.0 · rank 1544 · last release 2026-03-31 · [PyPI](https://pypi.org/project/sqlite-vec/)

### schedule

Job scheduling for humans.

`pip install schedule` · installs (wheel) · licence: MIT License · rank 1630 · last release 2024-06-18 · [PyPI](https://pypi.org/project/schedule/) · [docs](https://schedule.readthedocs.io) · [source](https://github.com/dbader/schedule.git)

<details><summary>README extract</summary>

Python job scheduling for humans. Run Python functions (or any other callable) periodically using a friendly syntax.

- A simple to use API for scheduling jobs, made for humans.
- In-process scheduler for periodic jobs. No extra processes needed!
- Very lightweight and no external dependencies.
- Excellent test coverage. ...

Example:
```python
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
...
```

Sections: schedule, Usage, Documentation, Meta

</details>

### shellcheck-py

Python wrapper around invoking shellcheck (https://www.shellcheck.net/)

`pip install shellcheck-py` · installs (wheel) · licence: MIT · rank 1665 · last release 2025-08-09 · [PyPI](https://pypi.org/project/shellcheck-py/)

<details><summary>README extract</summary>

A python wrapper to provide a pip-installable [shellcheck] binary.

Internally this package provides a convenient way to download the pre-built
shellcheck binary for your particular platform.

Sections: shellcheck-py, usage, As a pre-commit hook

</details>

### stringcase

String case converter.

`pip install stringcase` · installs from source (sdist only) · licence: MIT · rank 1719 · last release 2017-08-06 · [PyPI](https://pypi.org/project/stringcase/)

<details><summary>README extract</summary>

Convert string cases between camel case, pascal case, snake case etc...

Example:
```python
import stringcase
stringcase.camelcase('foo_bar_baz') # => "fooBarBaz"
stringcase.camelcase('FooBarBaz') # => "fooBarBaz"
stringcase.capitalcase('foo_bar_baz') # => "Foo_bar_baz"
stringcase.capitalcase('FooBarBaz') # => "FooBarBaz"
stringcase.constcase('foo_bar_baz') # => "FOO_BAR_BAZ"
stringcase.constcase('FooBarBaz') # => "_FOO_BAR_BAZ"
...
```

Sections: stringcase, Usage

</details>

### sgmllib3k

Py3k port of sgmllib.

`pip install sgmllib3k` · installs from source (sdist only) · licence: BSD License · rank 1762 · last release 2010-08-24 · [PyPI](https://pypi.org/project/sgmllib3k/)

<details><summary>README extract</summary>

sgmllib was dropped in Python 3. For those depending on it, that's somewhat unfortunate. This is a quick and dirty port of this old module. I just ran 2to3 on it and published it. I don't intend to maintain it, so it might be a good idea to eventually think about finding another module to use.

</details>

### sly

"SLY - Sly Lex Yacc"

`pip install sly` · installs (wheel) · licence: MIT License · rank 1809 · last release 2022-10-25 · [PyPI](https://pypi.org/project/sly/)

<details><summary>README extract</summary>

"SLY is an implementation of lex and yacc. No longer maintained on PyPI. Latest version on GitHub."

</details>

### stamina

Production-grade retries made easy.

`pip install stamina` · installs (wheel) · licence: MIT · rank 1825 · last release 2026-04-13 · [PyPI](https://pypi.org/project/stamina/) · [docs](https://stamina.hynek.me/) · [source](https://github.com/hynek/stamina)

<details><summary>README extract</summary>

Transient failures are common in distributed systems.
To make your systems resilient, you need to retry failed operations.
But bad retries can make things *much worse*.

*stamina* is an opinionated wrapper around the great-but-unopinionated Tenacity package. ...

Example:
```python
import httpx

import stamina

@stamina.retry(on=httpx.HTTPError, attempts=3)
def do_it(code: int) -> httpx.Response:
    resp = httpx.get(f"
    resp.raise_for_status()

    return resp
```

Sections: stamina*: Production-grade Retries Made Easy, Changed, Fixed, stamina* for Enterprise

</details>

### safehttpx

A small Python library created to help developers protect their applications from Server Side Request Forgery (SSRF) attacks.

`pip install safehttpx` · installs (wheel) · licence: MIT License · rank 1839 · last release 2026-09-28 · [PyPI](https://pypi.org/project/safehttpx/) · [source](https://github.com/gradio-app/safehttpx)

<details><summary>README extract</summary>

A small Python library created to help developers protect their applications from Server Side Request Forgery (SSRF) attacks. It implements an asynchronous GET method called `safehttpx.get()`, which is a wrapper around `httpx2.AsyncClient.get()` (HTTPX2, the maintained fork of `httpx`) while performing DNS validation on the supplied URL using ...

Features:
Server Side Request Forgery (SSRF) attacks can be particularly dangerous as they allow attackers to make arbitrary HTTP requests from your server, potentially accessing sensitive internal services that are normally unreachable from the internet. ...

Example:
```python
import safehttpx as sh

await sh.get("
>>> <Response [200 OK]>

await sh.get("
>>> ValueError: Hostname 127.0.0.1 failed validation
```

...

</details>

### scs

Splitting conic solver

`pip install scs` · installs (wheel) · licence: MIT License · rank 1849 · last release 2026-09-05 · [PyPI](https://pypi.org/project/scs/)

<details><summary>README extract</summary>

Python interface for SCS 3.0.0 and higher.
The full documentation is available here.

Example:
```python
import numpy as np
import scipy.sparse as sp
import scs

m, n = 4, 2
A = sp.random(m, n, density=0.5, format="csc")
b = np.random.randn(m)
c = np.random.randn(n)
P = sp.eye(n, format="csc")

cone = {"l": m}  # non-negative cone
data = {"P": P, "A": A, "b": b, "c": c}

solver = scs.SCS(data, cone, verbose=False)
sol = solver.solve()

...
```

Sections: scs-python, Linear solver backends, Usage, Anderson acceleration tuning, Cone types

</details>

### sql-metadata

Uses sqlglot to parse SQL queries and extract metadata

`pip install sql-metadata` · installs (wheel) · licence: MIT License · rank 2016 · last release 2026-06-30 · [PyPI](https://pypi.org/project/sql-metadata/) · [source](https://github.com/macbre/sql-metadata)

<details><summary>README extract</summary>

Uses `sqlglot` to parse SQL queries and extract metadata.

Extracts column names and tables used by the query.
Automatically conduct column alias resolution, sub queries aliases resolution as well as tables aliases resolving.

Provides also a helper for normalization of SQL queries.

Supported queries syntax: ...

Example:
```python
from sql_metadata import Parser

# extract raw sql-metadata tokens
Parser("SELECT * FROM foo").tokens
# ['SELECT', '*', 'FROM', 'foo']
```

...

</details>

### sqlglotrs

Deprecated: use sqlglotc instead

`pip install sqlglotrs` · installs (wheel) · licence: MIT · rank 2076 · last release 2026-02-23 · [PyPI](https://pypi.org/project/sqlglotrs/) · [source](https://github.com/tobymao/sqlglot)

### segment-analytics-python

The hassle-free way to integrate analytics into any python application.

`pip install segment-analytics-python` · installs (wheel) · licence: MIT · rank 2081 · last release 2026-09-29 · [PyPI](https://pypi.org/project/segment-analytics-python/) · [source](https://github.com/segmentio/analytics-python)

<details><summary>README extract</summary>

=======

=======

analytics-python is a python client for Segment

This library is in maintenance mode. It will send data as intended, but receive no new feature support and only critical maintenance updates from Segment.

 You can't fix what you can't measure

Analytics helps you measure your users, product, and business. ...

Example:
```python
import segment.analytics as analytics

analytics.write_key = 'YOUR_WRITE_KEY'
```

Sections: ﻿analytics-python, ⚠️ Maintenance ⚠️, 🚀 How to get started, 🤔 Why?, 👨‍💻 Getting Started, 🚀 Startup Program, Documentation

</details>

### scipy-stubs

The official type stubs for SciPy

`pip install scipy-stubs` · installs (wheel) · licence: BSD-3-Clause · rank 2091 · last release 2026-09-20 · [PyPI](https://pypi.org/project/scipy-stubs/) · [source](https://github.com/scipy/scipy-stubs)

<details><summary>README extract</summary>

The official type stubs for SciPy.

> Used by Pandas, JAX, Apache Spark, Astropy, Ultralytics, Altair, and many other projects.

Features:
- Complete coverage: the entire public SciPy API is annotated.
- Shape- and dtype-aware: array shapes and dtypes are tracked where applicable.
- Generics: subscriptable types for sparse arrays, distributions, splines, and linear operators. ...

Sections: scipy-stubs, Features, Examples, Accurate type hints for shapes and dtypes, Prevent mistakes with precise type hints, Using pip (PyPI), Using conda (conda-forge), Why is scipy-stubs a separate package?, Separation of concerns, Opt-in by design, CI efficiency, Frequently Asked Questions, Q: Do I need to change my existing code?, Q: How much of SciPy is covered?

</details>

### statsig-python-core

Statsig Python bindings for the Statsig Core SDK.

`pip install statsig-python-core` · installs (wheel) · licence: ISC · rank 2129 · last release 2026-11-06 · [PyPI](https://pypi.org/project/statsig-python-core/) · [docs](https://docs.statsig.com/server-core/python-core) · [source](https://github.com/statsig-io/statsig-server-core/tree/main/statsig-pyo3)

<details><summary>README extract</summary>

Statsig

Statsig helps you move faster with feature gates (feature flags), and/or dynamic configs. It also allows you to run A/B/n tests to validate your new features and understand their impact on your KPIs. If you're new to Statsig, check out our product and create an account at statsig.com.

Sections: Getting Started, Packages

</details>

### stanio

Utilities for preparing Stan inputs and processing Stan outputs

`pip install stanio` · installs (wheel) · licence: BSD-3-Clause · rank 2179 · last release 2024-07-08 · [PyPI](https://pypi.org/project/stanio/)

<details><summary>README extract</summary>

A set of Python functions for data-wrangling in the formats used by
the Stan probabalistic programming language.

It is primarily developed for use in cmdstanpy.

Features:
- Writing Python dictionaries to Stan-compatible JSON (with optional support for using `ujson` for faster serialization)
- Basic reading of StanCSV files into numpy arrays ...

Sections: StanIO, Features

</details>

### sphinx-copybutton

Add a copy button to each of your code cells.

`pip install sphinx-copybutton` · installs (wheel) · licence: MIT License · rank 2187 · last release 2023-04-14 · [PyPI](https://pypi.org/project/sphinx-copybutton/)

<details><summary>README extract</summary>

| |

A small sphinx extension to add a "copy" button to code blocks.

See the sphinx-copybutton documentation for more details!

Sections: sphinx-copybutton, Usage, Customization

</details>

### simple-gcp-object-downloader

(no summary)

`pip install simple-gcp-object-downloader` · installs (wheel) · licence: not stated · rank 2260 · last release 2022-08-02 · [PyPI](https://pypi.org/project/simple-gcp-object-downloader/)

### svcs

A Flexible Service Locator

`pip install svcs` · installs (wheel) · licence: MIT · rank 2272 · last release 2026-08-24 · [PyPI](https://pypi.org/project/svcs/) · [docs](https://svcs.hynek.me/) · [source](https://github.com/hynek/svcs)

<details><summary>README extract</summary>

A flexible service locator for Python

*svcs* (pronounced *services*) is a dependency container for Python.
It gives you a central place to register factories for types/interfaces and then imperatively acquire instances of those types with automatic cleanup and health checks. ...

Example:
```python
from svcs.your_framework import svcs_from

def view(request):
    db, api, cache = svcs_from(request).get(Database, WebAPIClient, Cache)
```

Sections: Project links, Removed, Added, Fixed, svcs* for Enterprise

</details>

### sagemaker-core

An python package for sagemaker core functionalities

`pip install sagemaker-core` · installs (wheel) · licence: Apache Software License · rank 2333 · last release 2026-11-05 · [PyPI](https://pypi.org/project/sagemaker-core/)

<details><summary>README extract</summary>

Welcome to the sagemaker-core Python SDK, an SDK designed to provide an object-oriented interface for interacting with Amazon SageMaker resources. It offers full parity with SageMaker APIs, allowing developers to leverage all SageMaker capabilities directly through the SDK. ...

Features:
* Object-Oriented Interface: Provides a structured way to interact with SageMaker resources, making it easier to manage them using familiar object-oriented programming techniques. ...

Sections: SageMaker Core, Introduction, Key Features, Benefits, Docs and Examples

</details>

### snapshot-restore-py

Runtime Hooks for AWS Lambda SnapStart - Python

`pip install snapshot-restore-py` · installs (wheel) · licence: Apache Software License · rank 2339 · last release 2024-11-13 · [PyPI](https://pypi.org/project/snapshot-restore-py/)

<details><summary>README extract</summary>

This is the Snapshot Restore for Python library which can be used for registering runtime hooks in Snapstart enabled Python Lambda functions

This library provides two decorators that you can use to define your runtime hooks: ...

Example:
```python
from snapshot_restore_py import register_before_snapshot, register_after_restore

def lambda_handler(event, context):
    # your logic here
    ...

@register_before_snapshot
def fn_before_snapshot():
    # your logic here
    ...

@register_after_restore
def fn_after_restore():
    # your logic here
    ...
```

...

</details>

### sqlalchemy-redshift

Amazon Redshift Dialect for sqlalchemy

`pip install sqlalchemy-redshift` · installs (wheel) · licence: MIT License · rank 2385 · last release 2026-04-28 · [PyPI](https://pypi.org/project/sqlalchemy-redshift/)

<details><summary>README extract</summary>

Amazon Redshift dialect for SQLAlchemy.

Example:
```python
>>> import sqlalchemy as sa
>>> sa.create_engine('redshift+psycopg2://username@host.amazonaws.com:5439/database')
Engine(redshift+psycopg2://username@host.amazonaws.com:5439/database)
```

Sections: sqlalchemy-redshift, Usage, Running Tests, Continuous Integration (CI), Releasing, 1.0.0 (2026-04-27), 0.8.14 (2023-04-07), 0.8.13 (2023-03-28), 0.8.12 (2022-12-08), 0.8.11 (2022-07-27), 0.8.10 (2022-07-21), 0.8.9 (2021-12-15), 0.8.8 (2021-11-03), 0.8.7 (2021-10-27)

</details>

### salesforce-bulk

Python interface to the Salesforce.com Bulk API.

`pip install salesforce-bulk` · installs from source (sdist only) · licence: MIT License · rank 2477 · last release 2020-11-12 · [PyPI](https://pypi.org/project/salesforce-bulk/)

<details><summary>README extract</summary>

Python client library for accessing the asynchronous Salesforce.com Bulk
API.

Example:
```python
from salesforce_bulk import SalesforceBulk

bulk = SalesforceBulk(username=username, password=password, security_token=security_token)
...
```

Sections: Salesforce Bulk, Authentication, Operations, Bulk Query, PK Chunk Header, Bulk Insert, Update, Delete, Concurrency mode

</details>

### supafunc

Library for Supabase Functions

`pip install supafunc` · installs (wheel) · licence: MIT License · rank 2574 · last release 2025-08-08 · [PyPI](https://pypi.org/project/supafunc/) · [source](https://github.com/supabase/functions-py)

<details><summary>README extract</summary>

The `supafunc` package name is deprecated and is not going to receive any more updates. Please, use `supabase_functions` instead.

1. Use `uv add supabase_functions` instead of `uv add supafunc`.
2. Replace `supafunc` with `supabase_functions` in your `requirements.txt`, `pyproject.toml`, `setup.py`, etc.
3. ...

Sections: ⚠️⚠️⚠️ Deprecation notice ⚠️⚠️⚠️, How to switch, Reasoning

</details>

### sparsediffpy

Python bindings for SparseDiffEngine algorithmic differentiation

`pip install sparsediffpy` · installs (wheel) · licence: Apache-2.0 · rank 2599 · last release 2026-10-15 · [PyPI](https://pypi.org/project/sparsediffpy/)

<details><summary>README extract</summary>

Python bindings for SparseDiffEngine, a C library for computing sparse Jacobians and Hessians.

Example:
```python
from sparsediffpy import _sparsediffengine
```

Sections: SparseDiffPy, Usage, Free-threaded Python

</details>

### sigstore-rekor-types

Python models for Rekor's API types

`pip install sigstore-rekor-types` · installs (wheel) · licence: Apache Software License · rank 2714 · last release 2024-11-22 · [PyPI](https://pypi.org/project/sigstore-rekor-types/) · [docs](https://trailofbits.github.io/sigstore-rekor-types/) · [source](https://github.com/trailofbits/sigstore-rekor-types)

<details><summary>README extract</summary>

<!--- BADGES: START --->

<!--- BADGES: END --->

Python models for Rekor's API types.

This package contains only data models for [Rekor]. You may be looking for
[sigstore-python] or [sigstore-protobuf-specs].

</details>

### sqlglotc

mypyc-compiled extensions for sqlglot

`pip install sqlglotc` · installs (wheel) · licence: MIT · rank 2728 · last release 2026-11-06 · [PyPI](https://pypi.org/project/sqlglotc/) · [source](https://github.com/tobymao/sqlglot)

### sigstore-models

Pydantic based models for Sigstore's protobuf specifications

`pip install sigstore-models` · installs (wheel) · licence: not stated · rank 2731 · last release 2026-11-02 · [PyPI](https://pypi.org/project/sigstore-models/) · [source](https://github.com/astral-sh/sigstore-models)

<details><summary>README extract</summary>

Pydantic-based data models for Sigstore.

These models mirror the subset of the [protobuf-specs] that
are used by the [sigstore-python] library.

* Providing high-quality, type-safe data models to [sigstore-python].
* Matching Sigstore's (mostly protobuf influenced) JSON serialization
 format.

* Supporting protobuf serialization/deserialization. ...

Sections: sigstore-models, Goals, Anti-goals, Releasing

</details>

### sqlalchemy-stubs

SQLAlchemy stubs and mypy plugin

`pip install sqlalchemy-stubs` · installs (wheel) · licence: MIT License · rank 2739 · last release 2021-01-12 · [PyPI](https://pypi.org/project/sqlalchemy-stubs/)

<details><summary>README extract</summary>

This package contains type stubs and mypy plugin to provide more precise
static types and type inference for SQLAlchemy framework. SQLAlchemy uses
dynamic Python features that are hard to understand by static type checkers,
this is why the plugin is needed in addition to type stubs. ...

</details>

### starlette-testclient

A backport of Starlette TestClient using requests! ⏪️

`pip install starlette-testclient` · installs (wheel) · licence: BSD License · rank 2880 · last release 2024-04-29 · [PyPI](https://pypi.org/project/starlette-testclient/) · [source](https://github.com/Kludex/starlette-testclient)

<details><summary>README extract</summary>

This is a backport of Starlette's `TestClient` using `requests` instead of `httpx`.

The reason behind here is to give more time for people to migrate.

Example:
```python
from starlette.testclient import TestClient
```

Sections: starlette-testclient, Usage

</details>

### simple-parsing

A small utility to simplify and clean up argument parsing scripts.

`pip install simple-parsing` · installs (wheel) · licence: not stated · rank 2890 · last release 2026-07-27 · [PyPI](https://pypi.org/project/simple-parsing/)

<details><summary>README extract</summary>

Features:
- ### Automatic "--help" strings

 As developers, we want to make it easy for people coming into our projects to understand how to run them. ...

Example:
```python
options: Options = simple_parsing.parse(Options)
# or:
options, leftover_args = simple_parsing.parse_known_args(Options)
```

Sections: (*new*) Simplified API, Examples, API Documentation (Under construction), Features

</details>

### s3path

(no summary)

`pip install s3path` · installs (wheel) · licence: Apache Software License · rank 2930 · last release 2026-01-24 · [PyPI](https://pypi.org/project/s3path/)

<details><summary>README extract</summary>

S3Path provide a Python convenient File-System/Path like interface for AWS S3 Service using boto3 S3 resource as a driver.

Like pathlib, but for S3 Buckets
________

AWS S3 is among the most popular cloud storage solutions. It's object storage, is built to store and retrieve various amounts of data from anywhere. ...

Example:
```python
>>> from s3path import S3Path
```

Sections: S3Path, Basic use, Versioned S3 Objects, Requirements, Further Documentation

</details>

### safety-schemas

Schemas for Safety tools

`pip install safety-schemas` · installs (wheel) · licence: MIT License · rank 2947 · last release 2026-09-08 · [PyPI](https://pypi.org/project/safety-schemas/)

### strawberry-graphql-django

Strawberry GraphQL Django extension

`pip install strawberry-graphql-django` · installs (wheel) · licence: MIT License · rank 2973 · last release 2026-11-07 · [PyPI](https://pypi.org/project/strawberry-graphql-django/) · [docs](https://strawberry.rocks/docs/django) · [source](https://github.com/strawberry-graphql/strawberry-django)

<details><summary>README extract</summary>

Documentation | Discord

Strawberry GraphQL Django integration provides powerful tools to build GraphQL APIs with Django. Automatically generate GraphQL types, queries, mutations, and resolvers from your Django models with full type safety.

Features:
- 🍓 Automatic Type Generation - Generate GraphQL types from Django models with full type safety
- 🔍 Advanced Filtering - Powerful filtering system with lookups (contains, exact, in, etc.) ...

Example:
```python
# models.py
from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=20)
    color = models.ForeignKey("Color", on_delete=models.CASCADE, related_name="fruits")

class Color(models.Model):
    name = models.CharField(max_length=20)
```

...

</details>

### scooby

A Great Dane turned Python environment detective

`pip install scooby` · installs (wheel) · licence: MIT · rank 2994 · last release 2026-10-27 · [PyPI](https://pypi.org/project/scooby/) · [source](https://github.com/banesullivan/scooby)

<details><summary>README extract</summary>

_Great Dane turned Python environment detective

This is a lightweight tool for easily reporting your Python environment's
package versions and hardware resources.

Install from PyPI

or from conda-forge

Scooby has HTML formatting for Jupyter notebooks and rich text formatting for
just about every other environment. ...

Example:
```python
>>> import scooby
>>> scooby.Report()
```

Sections: Usage, Generating Reports, Implementing scooby in your project, Implementing as a soft dependency, Autogenerate Reports for any Packages, Solving Mysteries, How does scooby get version numbers?, Using scooby to get version information., Tracking Imports in a Session, Command-Line Interface, Optional Requirements

</details>

### sqltrie

SQL-based prefix tree inspired by pygtrie and python-diskcache

`pip install sqltrie` · installs (wheel) · licence: Apache-2.0 · rank 3018 · last release 2026-09-01 · [PyPI](https://pypi.org/project/sqltrie/) · [source](https://github.com/efiop/sqltrie)

<details><summary>README extract</summary>

Features:
* TODO

Sections: SQLTrie, Features, Requirements, Usage, Issues

</details>

### sagemaker-studio

Python library to interact with Amazon SageMaker Unified Studio

`pip install sagemaker-studio` · installs (wheel) · licence: Apache Software License · rank 3064 · last release 2026-11-05 · [PyPI](https://pypi.org/project/sagemaker-studio/)

<details><summary>README extract</summary>

SageMaker Studio is an open source library for interacting with Amazon SageMaker Unified Studio resources. With the library, you can access these resources such as domains, projects, connections, and databases, all in one place with minimal code.

Example:
```python
from sagemaker_studio import ClientConfig

conf = ClientConfig(profile_name="my_profile_name")
```

Sections: SageMaker Studio, Licensing, 2) Usage, Setting Up Credentials and ClientConfig, AWS Named Profile, Boto3 Session, Using ClientConfig, Domain, Domain Properties, Project, Project Properties, IAM Role ARN, KMS Key ARN, MLflow Tracking Server ARN

</details>

### sagemaker-mlflow

AWS Plugin for MLflow with SageMaker

`pip install sagemaker-mlflow` · installs (wheel) · licence: Apache Software License · rank 3072 · last release 2026-06-27 · [PyPI](https://pypi.org/project/sagemaker-mlflow/)

<details><summary>README extract</summary>

This plugin generates Signature V4 headers in each outgoing request to the Amazon SageMaker with MLflow capability,
determines the URL of capability to connect to tracking servers, and registers models to the SageMaker Model Registry. ...

Example:
```python
import boto3
import mlflow
import sagemaker_mlflow

custom = boto3.Session(profile_name="my-profile")

with sagemaker_mlflow.use_session(custom):
    mlflow.MlflowClient().search_experiments(max_results=1)
```

Sections: SageMaker MLflow Plugin, What does this Plugin do?, Custom AWS session, setup.py, Running tests, Setup, Running format checks, Formatting code to comply with format checks, Running unit tests, Running integration tests, Available test environments by default

</details>

### starlette-exporter

Prometheus metrics exporter for Starlette applications.

`pip install starlette-exporter` · installs (wheel) · licence: Apache License 2.0 · rank 3115 · last release 2026-07-29 · [PyPI](https://pypi.org/project/starlette-exporter/)

<details><summary>README extract</summary>

starlette_exporter collects basic metrics for Starlette and FastAPI based applications:

* starlette_requests_total: a counter representing the total requests
* starlette_request_duration_seconds: a histogram representing the distribution of request response times
* starlette_requests_in_progress: a gauge that keeps track of how many concurrent ...

Example:
```python
from starlette.applications import Starlette
from starlette_exporter import PrometheusMiddleware, handle_metrics

app = Starlette()
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

...
```

...

</details>

### sudachidict-core

Sudachi Dictionary for SudachiPy - Core Edition

`pip install sudachidict-core` · installs (wheel) · licence: Apache-2.0 · rank 3142 · last release 2026-10-15 · [PyPI](https://pypi.org/project/sudachidict-core/)

<details><summary>README extract</summary>

- WorksApplications/SudachiDict
- WorksApplications/SudachiPy

Managing the dictionary resources as Python packages.

- SudachiDict-small · PyPI
- SudachiDict-core · PyPI
- SudachiDict-full · PyPI

The dictionary files are not included in the packages; It will be downloaded upon installation (the procedure in `setup.py`). ...

Sections: Sudachi Dictionary for SudachiPy, Commands to download and set the dictionaries, Dictionary option in SudachiPy before v0.5.2

</details>

### sqlalchemy-adapter

SQLAlchemy Adapter for PyCasbin

`pip install sqlalchemy-adapter` · installs (wheel) · licence: Apache Software License · rank 3181 · last release 2025-11-17 · [PyPI](https://pypi.org/project/sqlalchemy-adapter/)

<details><summary>README extract</summary>

SQLAlchemy Adapter is the SQLAlchemy adapter for PyCasbin. With this library, Casbin can load policy from SQLAlchemy supported database or save policy to it.

Based on Officially Supported Databases, The current supported databases are:

- PostgreSQL
- MySQL
- SQLite
- Oracle
- Microsoft SQL Server
- Firebird
- Sybase

Example:
```python
import sqlalchemy_adapter
import casbin

adapter = sqlalchemy_adapter.Adapter('sqlite:///test.db')

e = casbin.Enforcer('path/to/model.conf', adapter)

sub = "alice"  # the user that wants to access a resource.
obj = "data1"  # the resource that is going to be accessed.
act = "read"  # the operation that the user performs on the resource.

...
```

Sections: SQLAlchemy Adapter for PyCasbin, Simple Example, Prevent Automatic Table Creation, Getting Help

</details>

### skl2onnx

Convert scikit-learn models to ONNX

`pip install skl2onnx` · installs (wheel) · licence: Apache Software License · rank 3226 · last release 2026-01-30 · [PyPI](https://pypi.org/project/skl2onnx/)

<details><summary>README extract</summary>

*sklearn-onnx* converts scikit-learn models to ONNX.
Once in the ONNX format, you can use tools like ONNX Runtime for high performance scoring.
All converters are tested with onnxruntime.
Any external converter can be registered to convert scikit-learn pipeline
including models or transformers coming from external libraries. ...

Example:
```python
# Train a model.
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X, y = iris.data, iris.target
X = X.astype(np.float32)
X_train, X_test, y_train, y_test = train_test_split(X, y)
clr = RandomForestClassifier()
...
```

Sections: Introduction, Documentation, Getting started, PR

</details>

### SudachiPy

Python version of Sudachi, the Japanese Morphological Analyzer

`pip install SudachiPy` · installs (wheel) · licence: Apache-2.0 · rank 3236 · last release 2026-09-24 · [PyPI](https://pypi.org/project/SudachiPy/)

<details><summary>README extract</summary>

Documentation

SudachiPy is a Python version of Sudachi, a Japanese morphological analyzer.

This is not a pure Python implementation, but bindings for the
Sudachi.rs.

> IMPORTANT
> v0.7 introduces a new dictionary binary format (V1). ...

Example:
```python
from sudachipy import Dictionary, SplitMode

tokenizer_obj = Dictionary().tokenizer()
```

Sections: SudachiPy, TL;DR, Setup, Step 2. Get a Dictionary, Usage: As a command, Output, Usage: As a Python package, API, Example, Dictionary Edition, Dictionary option: command line, Dictionary option: Python package, Dictionary in The Setting File, User Dictionary

</details>

### statsforecast

Time series forecasting suite using statistical models

`pip install statsforecast` · installs (wheel) · licence: Apache Software License · rank 3253 · last release 2026-07-16 · [PyPI](https://pypi.org/project/statsforecast/) · [docs](https://nixtlaverse.nixtla.io/statsforecast/) · [source](https://github.com/Nixtla/statsforecast/)

<details><summary>README extract</summary>

StatsForecast offers a collection of widely used univariate time series forecasting models, including automatic `ARIMA`, `ETS`, `CES`, and `Theta` modeling optimized for high performance. It also includes a large battery of benchmarking models.

Features:
Current Python alternatives for statistical models are slow, inaccurate and don't scale well. So we created a library that can be used to forecast in production environments or as benchmarks. ...

Example:
```python
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA
from statsforecast.utils import AirPassengersDF

df = AirPassengersDF
sf = StatsForecast(
    models=[AutoARIMA(season_length=12)],
    freq='ME',
)
sf.fit(df)
sf.predict(h=12, level=[95])
```

...

</details>

### soda-core

Soda core library & CLI

`pip install soda-core` · installs (wheel) · licence: Proprietary · rank 3265 · last release 2026-11-05 · [PyPI](https://pypi.org/project/soda-core/)

### sglang

SGLang is a fast serving framework for large language models and vision language models.

`pip install sglang` · does not install on CPython 3.14 · licence: Apache Software License · rank 3266 · last release 2026-10-30 · [PyPI](https://pypi.org/project/sglang/) · [docs](https://docs.sglang.io)

<details><summary>README extract</summary>

Docs |
 Cookbook |
 Website |
 Blog |
 Slack

SGLang is an open-source inference framework for large language, vision-language, and diffusion models, optimized for agentic workloads, large-scale serving, and RL rollouts. SGLang Diffusion is its built-in image and video generation engine, included in this repository and the `sglang` Python package. ...

Sections: SGLang: Fast inference for LLMs and multimodal models, Get Started, SGL Ecosystem, Trusted by Industry and Research

</details>

### scmrepo

scmrepo

`pip install scmrepo` · installs (wheel) · licence: Apache-2.0 · rank 3273 · last release 2026-03-31 · [PyPI](https://pypi.org/project/scmrepo/) · [source](https://github.com/treeverse/scmrepo)

<details><summary>README extract</summary>

SCM wrapper and fsspec filesystem for Git for use in DVC.

Features:
* Works with multiple backends: `pygit2`, `dulwich` and `gitpython`.
* Provides fsspec filesystem over Git: `GitFileSystem`.

See fsspec docs for full list of available fs methods.

Example:
```python
from scmrepo.fs import GitFileSystem

fs = GitFileSystem("path/to/my/repo", rev="mybranch")

for root, dnames, fnames in fs.walk("path/in/repo"):
    for dname in dnames:
        print(fs.path.join(root, dname))

    for fname in fnames:
        print(fs.path.join(root, fname))
```

Sections: scmrepo, Features, Requirements, Usage, Git File System, Issues

</details>

### saxonche

Official Saxonica python package for the SaxonC-HE 13.1.1 processor: for XSLT 3.0, XQuery 3.1, XPath 3.1 and XML Schema processing.

`pip install saxonche` · installs (wheel) · licence: not stated · rank 3317 · last release 2026-10-27 · [PyPI](https://pypi.org/project/saxonche/) · [docs](https://www.saxonica.com/saxon-c/documentation13/index.html)

<details><summary>README extract</summary>

This is the official Saxonica Python wheel package for
Saxon, an XML document processor. SaxonC
provides APIs to run XSLT 3.0 transformations, XQuery 3.1 queries, XPath 3.1, and
XML Schema validation.

Features:
The main reason for using SaxonC in preference to other XML
tools available for Python is that it supports all the latest W3C
standards: XSLT 3.0, XPath 3.1, XQuery 3.1, and XSD 1.1.

Example:
```python
from saxonche import *
```

Sections: Welcome to SaxonC-HE, SaxonC-HE, Why choose SaxonC?, What's new in this version?, About SaxonC, About Saxonica, Getting started, Example: Running a transformation, Using `pylint` on a project which uses `saxonche`

</details>

### shrub.py

Library for creating evergreen configurations

`pip install shrub.py` · installs (wheel) · licence: Apache Software License · rank 3318 · last release 2026-06-04 · [PyPI](https://pypi.org/project/shrub.py/) · [source](https://github.com/evergreen-ci/shrub.py)

<details><summary>README extract</summary>

A python based Evergreen project config generation library

Features:
Based on shrub, shrub.py is a library for programatically
building Evergreen project configurations described here.

Example:
```python
from shrub.v3.evg_task import EvgTask, EvgTaskDependency
from shrub.v3.evg_build_variant import BuildVariant, DisplayTask
from shrub.v3.evg_command import FunctionCall
from shrub.v3.evg_project import EvgProject
from shrub.v3.shrub_service import ShrubService

n_tasks = 10
def define_task(index):
    name = f"task_name{index}"

    return EvgTask(
...
```

Sections: shrub.py, Overview, Example, Run tests

</details>

### sqlalchemy2-stubs

Typing Stubs for SQLAlchemy 1.4

`pip install sqlalchemy2-stubs` · installs (wheel) · licence: MIT License · rank 3320 · last release 2023-12-30 · [PyPI](https://pypi.org/project/sqlalchemy2-stubs/)

<details><summary>README extract</summary>

These are interim PEP-484 typing stubs for the
SQLAlchemy 1.4 release series only. They
are released concurrently along with a
Mypy extension
which is designed to work with these stubs, which assists primarily in the area
of ORM mappings.

The stubs replace the use of the "sqlalchemy-stubs" package published by
Dropbox. ...

</details>

### sqlakeyset

offset-free paging for sqlalchemy

`pip install sqlakeyset` · installs (wheel) · licence: Unlicense · rank 3321 · last release 2026-08-29 · [PyPI](https://pypi.org/project/sqlakeyset/) · [source](https://github.com/djrobstep/sqlakeyset)

<details><summary>README extract</summary>

sqlakeyset implements keyset-based paging for SQLAlchemy (both ORM and core). Now with full SQLAlchemy 2 support and type hints!

This library is tested with PostgreSQL, MariaDB/MySQL and SQLite. It should work with many other SQLAlchemy-supported databases, too; but caveat emptor - you should verify the results are correct. ...

Example:
```python
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlakeyset import select_page

from models import Book

engine = create_engine('postgresql:///books')
with Session(engine) as s:
    q = select(Book).order_by(Book.author, Book.title, Book.id)

    # gets the first page
    page1 = select_page(s, q, per_page=20)

...
```

...

</details>

### solders

Python bindings for Solana Rust tools

`pip install solders` · installs (wheel) · licence: not stated · rank 3323 · last release 2026-08-13 · [PyPI](https://pypi.org/project/solders/) · [docs](https://kevinheavey.github.io/solders/) · [source](https://github.com/kevinheavey/solders)

### shelved-cache

Persistent cache for Python cachetools.

`pip install shelved-cache` · installs (wheel) · licence: MIT License · rank 3340 · last release 2025-12-15 · [PyPI](https://pypi.org/project/shelved-cache/) · [docs](https://github.com/mariushelf/shelved_cache) · [source](https://github.com/mariushelf/shelved_cache)

<details><summary>README extract</summary>

from shelved_cache import PersistentCache

Persistent cache implementation for Python
cachetools.

Behaves like any `Cache` implementation, but entries are persisted to disk.

Original repository:

Example:
```python
from shelved_cache import PersistentCache
from cachetools import LRUCache

filename = 'mycache'

# create persistency around an LRUCache
pc = PersistentCache(LRUCache, filename=filename, maxsize=2)

# we can now use the cache like a normal LRUCache.
# But: the cache is persisted to disk.
pc["a"] = 42
pc["b"] = 43

assert pc["a"] == 42
...
```

Sections: Shelved Cache, Usage example, Use as a decorator, Note: decorating multiple functions, Features, persistent cache, Async decorators, Known issues

</details>

### squawk-cli

Linter for PostgreSQL migrations

`pip install squawk-cli` · installs (wheel) · licence: Apache Software License; MIT License · rank 3361 · last release 2026-10-29 · [PyPI](https://pypi.org/project/squawk-cli/) · [source](https://github.com/sbdchd/squawk)

<details><summary>README extract</summary>

> Linter for Postgres migrations & SQL

Quick Start | Playground | Rules Documentation | GitHub Action | DIY GitHub Integration

Features:
Prevent unexpected downtime caused by database migrations and encourage best
practices around Postgres schemas and SQL.

Example:
```python
Find problems in your SQL

Usage: squawk [OPTIONS] [path]... [COMMAND]

Commands:
  server            Run the language server
  upload-to-github  Comment on a PR with Squawk's results
  help              Print this message or the help of the given subcommand(s)

Arguments:
  [path]...
          Paths or patterns to search

Options:
...
```

...

</details>

### simple-azure-blob-downloader

(no summary)

`pip install simple-azure-blob-downloader` · installs (wheel) · licence: not stated · rank 3365 · last release 2022-07-25 · [PyPI](https://pypi.org/project/simple-azure-blob-downloader/)

### sacremoses

SacreMoses

`pip install sacremoses` · installs (wheel) · licence: MIT License · rank 3429 · last release 2026-08-14 · [PyPI](https://pypi.org/project/sacremoses/)

<details><summary>README extract</summary>

Example:
```python
>>> from sacremoses import MosesTokenizer, MosesDetokenizer
>>> mt = MosesTokenizer(lang='en')
>>> text = 'This, is a sentence with weird\xbb symbols\u2026 appearing everywhere\xbf'
>>> expected_tokenized = 'This , is a sentence with weird \xbb symbols \u2026 appearing everywhere \xbf'
>>> tokenized_text = mt.tokenize(text, return_str=True)
...
```

Sections: Sacremoses, Usage (Python), Tokenizer and Detokenizer, Truecaser, Normalizer, Usage (CLI), Pipeline, Tokenizer, Detokenizer, Truecase, Detruecase, Normalize

</details>

### sklearn

deprecated sklearn package, use scikit-learn instead

`pip install sklearn` · installs from source (sdist only) · licence: not stated · rank 3481 · last release 2023-12-01 · [PyPI](https://pypi.org/project/sklearn/)

<details><summary>README extract</summary>

⚠️⚠️⚠️ The `sklearn` PyPI package is deprecated use `scikit-learn` instead ⚠️⚠️⚠️

- use `pip install scikit-learn` rather than `pip install sklearn`
- replace `sklearn` by `scikit-learn` in your pip requirements files
 (`requirements.txt`, `setup.py,` `setup.cfg`, `Pipfile`, etc ...) ...

Sections: ⚠️⚠️⚠️ Summary ⚠️⚠️⚠️, How to fix the error for the main use cases, Reason for the deprecation, Historical brownout schedule

</details>

### sortedcontainers-stubs

Type stubs for sortedcontainers

`pip install sortedcontainers-stubs` · installs (wheel) · licence: Apache Software License · rank 3530 · last release 2025-04-23 · [PyPI](https://pypi.org/project/sortedcontainers-stubs/) · [source](https://github.com/h4l/sortedcontainers-stubs)

<details><summary>README extract</summary>

Community-maintained Python type stubs for the
sortedcontainers Python
library. sortedcontainers provides dict, set and list data structures that
maintain the order of their elements by value (not by insertion order). ...

Sections: sortedcontainers-stubs, Usage Notes, Version numbers, Reporting Issues

</details>

### swesmith

The official SWE-smith package - A toolkit for generating software engineering training data at scale.

`pip install swesmith` · installs (wheel) · licence: MIT License · rank 3552 · last release 2026-02-27 · [PyPI](https://pypi.org/project/swesmith/) · [docs](https://github.com/SWE-bench/SWE-smith) · [source](https://github.com/SWE-bench/SWE-smith)

<details><summary>README extract</summary>

NeurIPS 2025 Datasets & Benchmarks Track - Spotlight 🔦

SWE-smith is a toolkit for training SWE-agents. You can:
* Turn any Github repository into a SWE-gym.
* Create *unlimited* tasks (e.g., file localization, program repair, SWE-bench) for that repo.
* Train an LM to become a better SWE (SWE-agent-LM-32B). ...

Example:
```python
from swesmith.profiles import registry
from datasets import load_dataset
ds = load_dataset("SWE-bench/SWE-smith", split="train") # Loads all 52k task instances
for task in ds:
    rp = registry.get_from_inst(task)  # Get the RepoProfile for the task
...
```

Sections: ⚒️ Build Environments, 🏋️ Train SWE-agent's, 💿 Resources, 📕 Our Other Projects

</details>

### setuptools-download

setuptools plugin to download external files

`pip install setuptools-download` · installs (wheel) · licence: MIT License · rank 3560 · last release 2024-07-07 · [PyPI](https://pypi.org/project/setuptools-download/)

<details><summary>README extract</summary>

setuptools plugin to download external files

Sections: setuptools-download, usage, file settings, example

</details>

### sparklines

Generate sparklines for numbers using Unicode characters only.

`pip install sparklines` · installs (wheel) · licence: MIT · rank 3563 · last release 2026-06-08 · [PyPI](https://pypi.org/project/sparklines/) · [docs](https://github.com/deeplook/sparklines) · [source](https://github.com/deeplook/sparklines.git)

<details><summary>README extract</summary>

Sparklines brings Edward Tufte's [sparklines] to your terminal — compact Unicode bar charts like ▃▁▄▁▅█▂▅, right in your shell or Python code. Originally built for sanity-checking sensor data in IoT networks, it works anywhere you need a quick visual summary of a sequence of numbers. ...

Example:
```python
from sparklines import sparklines

for line in sparklines([1, 2, 3, 4, 5.0, None, 3, 2, 1]):
    print(line)
# ▁▃▅▆█ ▅▃▁

for line in sparklines([1, 2, 3, 4, 5.0, None, 3, 2, 1], num_lines=2):
    print(line)
# ▁▅█ ▁
# ▁▅███ █▅▁
```

Sections: Sparklines, Use cases, Sample output, Usage, Python, Mixed and negative datasets, References

</details>

### singledispatch

Backport functools.singledispatch to older Pythons.

`pip install singledispatch` · installs (wheel) · licence: MIT · rank 3565 · last release 2025-05-14 · [PyPI](https://pypi.org/project/singledispatch/) · [source](https://github.com/jaraco/singledispatch)

<details><summary>README extract</summary>

PEP 443 proposed to expose
a mechanism in the `functools` standard library module in Python 3.4
that provides a simple form of generic programming known as
single-dispatch generic functions.

This library is a backport of this functionality and its evolution.

Refer to the upstream documentation
for API guidance. ...

Sections: Maintenance, For Enterprise

</details>

### stactools-met-office-deterministic

Python package for generating STAC metadata for the Met Office Deterministic Numerical Weather Prediction model

`pip install stactools-met-office-deterministic` · installs (wheel) · licence: Apache Software License · rank 3630 · last release 2026-01-28 · [PyPI](https://pypi.org/project/stactools-met-office-deterministic/)

<details><summary>README extract</summary>

A package to create STAC items and collections for the Met Office UK deterministic weather forecasts.

> [!NOTE]
> This package was not created and is not maintained by the Met Office.
> Please use issues to report bugs or request features; do not contact the Met Office.

These were provided by the Met Office.

| Run Time | Objects Per Run | ...

Sections: met-office-deterministic, Model run schedules and asset counts, Global, UK

</details>

### splink

Fast probabilistic data linkage at scale

`pip install splink` · installs (wheel) · licence: MIT · rank 3664 · last release 2026-09-28 · [PyPI](https://pypi.org/project/splink/) · [source](https://github.com/moj-analytical-services/splink)

<details><summary>README extract</summary>

> [!IMPORTANT]
> 🎉 Splink 4 has been released! Examples of new syntax are here and a release announcement is here.

Splink is a Python package for probabilistic record linkage (entity resolution) that allows you to deduplicate and link records from datasets that lack unique identifiers. ...

Features:
⚡ Speed: Capable of linking a million records on a laptop in around a minute.

🎯 Accuracy: Support for term frequency adjustments and user-defined fuzzy matching logic. ...

Example:
```python
import splink.comparison_library as cl
from splink import DuckDBAPI, Linker, SettingsCreator, block_on, splink_datasets

db_api = DuckDBAPI()

df = splink_datasets.fake_1000
df_sdf = db_api.register(df, dataset_display_name="fake_1000")

settings = SettingsCreator(
    link_type="dedupe_only",
...

</details>

### scikit-network

Graph algorithms

`pip install scikit-network` · installs from source (sdist only) · licence: BSD License · rank 3666 · last release 2025-11-19 · [PyPI](https://pypi.org/project/scikit-network/) · [docs](https://scikit-network.readthedocs.io/) · [source](https://github.com/sknetwork-team/scikit-network)

<details><summary>README extract</summary>

Free software library in Python for machine learning on graphs:

* Memory-efficient representation of graphs as sparse matrices in scipy format
* Fast algorithms
* Simple API inspired by scikit-learn

* Free software: BSD license

Features:
An overview of the package is presented in this notebook.

Example:
```python
import sknetwork
```

Sections: Resources, Quick start, Overview, Documentation, Citing

</details>

### sparse

Sparse n-dimensional arrays for the PyData ecosystem

`pip install sparse` · installs (wheel) · licence: BSD License · rank 3686 · last release 2026-10-26 · [PyPI](https://pypi.org/project/sparse/) · [docs](https://sparse.pydata.org/) · [source](https://github.com/pydata/sparse.git)

<details><summary>README extract</summary>

- 📚 Documentation

- 🙌 Contributing

- 🪲 Bug Reports/Feature Requests

- 💬 Discord Server Channel

Sections: Sparse Multidimensional Arrays, This library provides multi-dimensional sparse arrays.

</details>

### shellescape

Shell escape a string to safely use it as a token in a shell command (backport of cPython shlex.quote for Python versions 2.x & < 3.3)

`pip install shellescape` · installs (wheel) · licence: MIT License · rank 3689 · last release 2020-01-25 · [PyPI](https://pypi.org/project/shellescape/)

<details><summary>README extract</summary>

The shellescape Python module defines the `shellescape.quote()` function that returns a shell-escaped version of a Python string. This is a backport of the `shlex.quote()` function from Python 3.8 that makes it accessible to users of Python 3 versions < 3.3 and all Python 2.x versions.

Return a shell-escaped version of the string s. ...

Example:
```python
setup(
    ...
    install_requires=['shellescape'],
    ...
)
```

Sections: shellescape, Description, quote(s), Usage

</details>

### speechbrain

All-in-one speech toolkit in pure Python and Pytorch

`pip install speechbrain` · installs (wheel) · licence: Apache Software License · rank 3704 · last release 2026-10-14 · [PyPI](https://pypi.org/project/speechbrain/)

<details><summary>README extract</summary>

| 📘 Tutorials | 🌐 Website | 📚 Documentation | 🤝 Contributing | 🤗 HuggingFace | ▶️ YouTube | 🐦 X |

 *Please, help our community project. Star on GitHub!*

Exciting News (January, 2024): Discover what is new in SpeechBrain 1.0 here! ...

Example:
```python
from speechbrain.inference import EncoderDecoderASR

asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-conformer-transformerlm-librispeech", savedir="pretrained_models/asr-transformer-transformerlm-librispeech")
asr_model.transcribe_file("speechbrain/asr-conformer-transformerlm-librispeech/example.wav")
```

...

</details>

### swe-rex

Sandboxed code execution for AI agents, locally or on the cloud.

`pip install swe-rex` · installs (wheel) · licence: MIT License · rank 3708 · last release 2025-08-14 · [PyPI](https://pypi.org/project/swe-rex/) · [docs](https://swe-rex.com/latest/) · [source](http://github.com/SWE-agent/SWE-rex)

<details><summary>README extract</summary>

SWE-ReX is a runtime interface for interacting with sandboxed shell environments, allowing you to effortlessly let your AI agent run *any command* on *any environment*.

Whether commands are executed locally or remotely in Docker containers, AWS remote machines, Modal, or something else, your agent code remains the same. ...

Sections: SWE-agent Remote Execution Framework, Get started, Our other projects

</details>

### super-collections

file: README.md

`pip install super-collections` · installs (wheel) · licence: MIT License · rank 3717 · last release 2025-09-30 · [PyPI](https://pypi.org/project/super-collections/) · [source](https://github.com/fralau/super-collections)

<details><summary>README extract</summary>

Dictionaries and lists as you dreamed them when you were a kid.

Instantly Convert json and YAML files into objects with attributes.

____

- Python Super Collections
 - What are SuperCollections?
 - What is the problem?
 - Definitions
 - How it works
 - Superdicts
 - Superlists
 - Why Combining SuperDicts with SuperLists?
 - SuperCollection
 - ...

Features:
The structure of JSON, YAML or HTML data is generally a deeply nested combination of dictionaries and lists. Using superdictionaries alone would not be sufficient, since lists within the data contained in a list would still contain regular ...

Example:
```python
from super_collections import SuperDict, SuperList

d = SuperDict({'foo':5, 'bar': 'hello'})
l = SuperList([5, 7, 'foo', {'foo': 5}])
```

...

</details>

### segments

Segmentation with orthography profiles

`pip install segments` · installs (wheel) · licence: Apache Software License · rank 3780 · last release 2026-03-07 · [PyPI](https://pypi.org/project/segments/)

<details><summary>README extract</summary>

The segments package provides Unicode Standard tokenization routines and orthography segmentation,
implementing the linear algorithm described in the orthography profile specification from
*The Unicode Cookbook* (Moran and Cysouw 2018 ).

Command line usage

Create a text file:

Now look at the profile:

Write the profile to a file: ...

Example:
```python
>>> from segments import Profile, Tokenizer
>>> t = Tokenizer()
>>> t('abcd')
'a b c d'
>>> prf = Profile({'Grapheme': 'ab', 'mapping': 'x'}, {'Grapheme': 'cd', 'mapping': 'y'})
>>> print(prf)
Grapheme    mapping
ab    x
cd    y
>>> t = Tokenizer(profile=prf)
>>> t('abcd')
'ab cd'
>>> t('abcd', column='mapping')
'x y'
```

</details>

### soda-core-spark

(no summary)

`pip install soda-core-spark` · installs (wheel) · licence: not stated · rank 3783 · last release 2025-09-24 · [PyPI](https://pypi.org/project/soda-core-spark/)

### session-info2

Print versions of imported packages.

`pip install session-info2` · installs (wheel) · licence: MPL-2.0 · rank 3793 · last release 2026-08-04 · [PyPI](https://pypi.org/project/session-info2/) · [docs](https://session-info2.readthedocs.io/) · [source](https://github.com/flying-sheep/session-info2)

<details><summary>README extract</summary>

Example:
```python
>>> httpx
>>> from session_info2 import session_info
```

Sections: session-info2, Usage

</details>

### sunshine-conversations-client

Sunshine Conversations API

`pip install sunshine-conversations-client` · installs (wheel) · licence: not stated · rank 3821 · last release 2025-09-04 · [PyPI](https://pypi.org/project/sunshine-conversations-client/)

### soda-core-spark-df

(no summary)

`pip install soda-core-spark-df` · installs (wheel) · licence: not stated · rank 3835 · last release 2025-09-24 · [PyPI](https://pypi.org/project/soda-core-spark-df/)

### scikit-build

Improved build system generator for Python C/C++/Fortran/Cython extensions

`pip install scikit-build` · installs (wheel) · licence: MIT License · rank 3895 · last release 2026-06-23 · [PyPI](https://pypi.org/project/scikit-build/) · [docs](https://scikit-build.readthedocs.io/)

<details><summary>README extract</summary>

scikit-build is a Python build system for CPython C/C++/Fortran/Cython
extensions using CMake.

The scikit-build package is fundamentally just glue between the `setuptools`
Python module and CMake.

The next generation of scikit-build, scikit-build-core, is currently under development. ...

Features:
* Support Visual Studio 18 2026 in #1186

Sections: Scikit-build 0.19.1, Features, Bug fixes, Miscellaneous, Scikit-build 0.19.0, Scikit-build 0.18.1, Scikit-build 0.18.0, Fedora CI

</details>

### sagemaker-schema-inference-artifacts

Open source library for Hugging Face Task Sample Inputs and Outputs

`pip install sagemaker-schema-inference-artifacts` · installs (wheel) · licence: Apache Software License · rank 3942 · last release 2024-04-08 · [PyPI](https://pypi.org/project/sagemaker-schema-inference-artifacts/)

<details><summary>README extract</summary>

SageMaker Schema Inference Artifacts is an open source library

</details>

### semantic-link-sempy

Semantic link for Microsoft Fabric

`pip install semantic-link-sempy` · installs (wheel) · licence: Other/Proprietary License · rank 3943 · last release 2026-10-22 · [PyPI](https://pypi.org/project/semantic-link-sempy/)

<details><summary>README extract</summary>

Semantic link is a feature that allows you to establish a connection between Power BI datasets and Synapse Data Science in Microsoft Fabric.

The primary goals of semantic link are to facilitate data connectivity, enable the propagation of semantic information, and seamlessly integrate with established tools used by data scientists, such as ...

Sections: Getting started, Prerequisites, About the semantic link packages, Key concepts, 0.14.3, 0.14.2, 0.14.1, 0.14.0, 0.13.0, 0.12.3, 0.12.2, 0.12.1, 0.12.0, 0.11.2

</details>

### spinners

Spinners for terminals

`pip install spinners` · installs (wheel) · licence: MIT · rank 3949 · last release 2020-02-19 · [PyPI](https://pypi.org/project/spinners/)

<details><summary>README extract</summary>

More than 60 spinners for terminal, this is python port of amazing node library cli-spinners. Find the documentation here:

</details>

### SmartlingApiSdk

python library to work with Smartling translation services APIs

`pip install SmartlingApiSdk` · installs (wheel) · licence: Apache License v2.0 · rank 3955 · last release 2025-09-03 · [PyPI](https://pypi.org/project/SmartlingApiSdk/)

<details><summary>README extract</summary>

python SDK to work with Smartling API for computer assisted translation

</details>

### smg-grpc-proto

SMG gRPC proto definitions for vLLM, TRT-LLM, MLX, TokenSpeed, and SGLang

`pip install smg-grpc-proto` · installs (wheel) · licence: Apache-2.0 · rank 3985 · last release 2026-10-25 · [PyPI](https://pypi.org/project/smg-grpc-proto/) · [source](https://github.com/smg-project/smg)

<details><summary>README extract</summary>

Protocol Buffer definitions for SMG (Shepherd Model Gateway) gRPC services.

This package provides pre-compiled Python gRPC stubs for:
- SGLang scheduler service (`sglang_scheduler.proto`)
- SGLang encoder service (`sglang_encoder.proto`)
- vLLM engine service (`vllm_engine.proto`)
- TensorRT-LLM service (`trtllm_service.proto`)

Example:
```python
from smg_grpc_proto import sglang_scheduler_pb2, sglang_scheduler_pb2_grpc
from smg_grpc_proto import sglang_encoder_pb2, sglang_encoder_pb2_grpc
from smg_grpc_proto import vllm_engine_pb2, vllm_engine_pb2_grpc
from smg_grpc_proto import trtllm_service_pb2, trtllm_service_pb2_grpc
```

Sections: smg-grpc-proto, Usage, Proto Source

</details>

### setuptools-git-versioning

Use git repo data for building a version number according to PEP-440

`pip install setuptools-git-versioning` · installs (wheel) · licence: MIT · rank 4074 · last release 2026-10-05 · [PyPI](https://pypi.org/project/setuptools-git-versioning/) · [docs](https://setuptools-git-versioning.readthedocs.io) · [source](https://github.com/dolfinus/setuptools-git-versioning)

<details><summary>README extract</summary>

|pre-commit.ci|

Use git repo data (latest tag, current commit hash, etc) for building a
version number according to 440.

Features:

- Can be installed & configured through both `setup.py` and 518's `pyproject.toml`

- Does not require to change source code of the project

- Tag-, file-, and callback-based versioning schemas are supported ...

Sections: setuptools-git-versioning, Documentation, `pyproject.toml`, or

</details>

### scverse-misc

Miscellaneous utility code used by scverse packages

`pip install scverse-misc` · installs (wheel) · licence: not stated · rank 4099 · last release 2026-10-28 · [PyPI](https://pypi.org/project/scverse-misc/) · [docs](https://scverse-misc.readthedocs.io/) · [source](https://github.com/scverse/scverse-misc)

<details><summary>README extract</summary>

[][pypi]
[][tests]
[][codecov]
[][documentation]

Miscellaneous utility code used by scverse packages

Sections: scverse-misc, Getting started, Contact

</details>

### sqllineage

SQL Lineage Analysis Tool powered by Python

`pip install sqllineage` · installs (wheel) · licence: MIT · rank 4117 · last release 2026-09-05 · [PyPI](https://pypi.org/project/sqllineage/) · [docs](https://sqllineage.readthedocs.io/en/latest/) · [source](https://github.com/reata/sqllineage.git)

<details><summary>README extract</summary>

SQL Lineage Analysis Tool powered by Python

Never get the hang of a SQL parser? SQLLineage comes to the rescue. Given a SQL command, SQLLineage will tell you its
source and target tables, without worrying about Tokens, Keyword, Identifier and all the jagons used by SQL parsers. ...

Example:
```python
$ sqllineage -e "insert into db1.table1 select * from db2.table2"
Statements(#): 1
Source Tables:
    db2.table2
Target Tables:
    db1.table1
```

Sections: SQLLineage, Demo & Documentation, Quick Start, Advanced Usage, Multiple SQL Statements, Verbose Lineage Result, Dialect-Awareness Lineage, Column-Level Lineage, MetaData-Awareness Lineage, Lineage Visualization

</details>

### sanic

A web server and web framework that's written to go fast. Build fast. Run fast.

`pip install sanic` · installs (wheel) · licence: MIT License · rank 4147 · last release 2026-05-31 · [PyPI](https://pypi.org/project/sanic/)

<details><summary>README extract</summary>

Sanic is a Python 3.10+ web server and web framework that's written to go fast. It allows the usage of the `async/await` syntax added in Python 3.5, which makes your code non-blocking and speedy.

Sanic is also ASGI compliant, so you can deploy it with an alternative ASGI webserver.

Source code on GitHub User Guide | Chat on Discord ...

Example:
```python
from sanic import Sanic
from sanic.response import json

app = Sanic("my-hello-world-app")

@app.route('/')
async def test(request):
    return json({'hello': 'world'})
```

Sections: Sanic | Build fast. Run fast., Hello World Example, Documentation, Questions and Discussion

</details>

### sqlite-fts4

Python functions for working with SQLite FTS4 search

`pip install sqlite-fts4` · installs (wheel) · licence: Apache License, Version 2.0 · rank 4160 · last release 2022-07-30 · [PyPI](https://pypi.org/project/sqlite-fts4/)

<details><summary>README extract</summary>

Custom SQLite functions written in Python for ranking documents indexed using the FTS4 extension.

Read Exploring search relevance algorithms with SQLite for further details on this project.

You can try out these SQL functions using this interactive demo.

Example:
```python
import sqlite3
from sqlite_fts4 import register_functions

conn = sqlite3.connect(":memory:")
register_functions(conn)
```

Sections: sqlite-fts4, Demo, Usage, rank_score(), rank_bm25(), decode_matchinfo(), annotate_matchinfo()

</details>

### sanic-routing

Core routing component for Sanic

`pip install sanic-routing` · installs (wheel) · licence: MIT License · rank 4202 · last release 2023-12-31 · [PyPI](https://pypi.org/project/sanic-routing/)

<details><summary>README extract</summary>

Beginning in v21.3, Sanic makes use of this new AST-style router in two use cases:

1. Routing paths; and
2. Routing signals.

Therefore, this package comes with a `BaseRouter` that needs to be subclassed in order to be used for its specific needs.

Most Sanic users should never need to concern themselves with the details here.

Example:
```python
import logging

from sanic_routing import BaseRouter

logging.basicConfig(level=logging.DEBUG)

class Router(BaseRouter):
    def get(self, path, *args, **kwargs):
        return self.resolve(path, *args, **kwargs)

router = Router()

router.add("/<foo>", lambda: ...)
router.finalize()
router.tree.display()
logging.info(router.find_route_src)

...
```

Sections: Sanic Routing, Background, Basic Example, What's it doing?, Special cases

</details>

### smg-grpc-servicer

SMG gRPC servicer implementations for LLM inference engines (vLLM, MLX, TokenSpeed, SGLang)

`pip install smg-grpc-servicer` · installs (wheel) · licence: Apache-2.0 · rank 4240 · last release 2026-11-02 · [PyPI](https://pypi.org/project/smg-grpc-servicer/) · [source](https://github.com/smg-project/smg)

<details><summary>README extract</summary>

gRPC servicer implementations for LLM inference engines. Supports vLLM, MLX, TokenSpeed, and SGLang.

Example:
```python
from smg_grpc_servicer.vllm import resolve_servicer_impl, serve_rust

if resolve_servicer_impl(args) == "rust":
    raise SystemExit(await serve_rust(args))
```

Sections: smg-grpc-servicer, Usage, vLLM, Worker-side multimodal processing (media refs), Rust request path (`SMG_VLLM_SERVICER_IMPL=rust`), Metrics (`--metrics-port`), Planned warm-up before SERVING (`SMG_VLLM_SERVICER_WARMUP`), CUDA-graph capture cap, Multi-node engines: the worker pod's liveness, MLX, TokenSpeed, SGLang

</details>

### stomp.py

Python STOMP client, supporting versions 1.0, 1.1 and 1.2 of the protocol

`pip install stomp.py` · installs (wheel) · licence: Apache Software License · rank 4254 · last release 2026-05-12 · [PyPI](https://pypi.org/project/stomp.py/) · [docs](https://jasonrbriggs.codeberg.page/stomp.py.pages/) · [source](https://codeberg.org/jasonrbriggs/stomp.py)

<details><summary>README extract</summary>

"stomp.py" is a Python client library for accessing messaging servers (such as ActiveMQ Classic, ActiveMQ Artemis or RabbitMQ) using the STOMP protocol (STOMP v1.0, STOMP v1.1 and STOMP v1.2). It can also be run as a standalone, command-line client for testing. NOTE: Stomp.py has officially ended support for Python2.x. ...

Example:
```python
import stomp

conn = stomp.Connection()
conn.connect('admin', 'password', wait=True)
conn.send(body=' '.join(sys.argv[1:]), destination='/queue/test')
conn.disconnect()
```

Sections: stomp.py, Quick Start, Documentation and Resources, . Create the docker (or podman) image, . Run the container, . Run stomp.py unit tests

</details>

### semantic-link-labs

Semantic Link Labs for Microsoft Fabric

`pip install semantic-link-labs` · does not install on CPython 3.14 · licence: MIT License · rank 4271 · last release 2026-11-03 · [PyPI](https://pypi.org/project/semantic-link-labs/) · [source](https://github.com/microsoft/semantic-link-labs.git)

<details><summary>README extract</summary>

Read the documentation on ReadTheDocs!

Read the Wiki!

See code examples!

Semantic Link Labs is a Python library designed for use in Microsoft Fabric notebooks. This library extends the capabilities of Semantic Link offering additional functionalities to seamlessly integrate and work alongside it. ...

Example:
```python
import sempy_labs as labs
import requests

workspace_name = None # Update this to the workspace in which you want to save the notebooks
api_url = "
response = requests.get(api_url)
files = response.json()
notebook_files = {file'name': file['html_url'] for file in files if file['name'].endswith('.ipynb')}

...
```

...

</details>

### strict-rfc3339

Strict, simple, lightweight RFC3339 functions

`pip install strict-rfc3339` · installs from source (sdist only) · licence: GNU General Public License v3 (GPLv3) · rank 4283 · last release 2016-04-24 · [PyPI](https://pypi.org/project/strict-rfc3339/)

_README extract left out: share-alike licence._

### svix-ksuid

A pure-Python KSUID implementation

`pip install svix-ksuid` · installs (wheel) · licence: MIT · rank 4311 · last release 2026-03-14 · [PyPI](https://pypi.org/project/svix-ksuid/) · [source](https://github.com/svix/python-ksuid/)

<details><summary>README extract</summary>

Svix - Webhooks as a service

This library is inspired by Segment's KSUID implementation:

For the Rust version, please check out

A ksuid is a K sorted UID. In other words, a KSUID also stores a date component, so that ksuids can be approximately
sorted based on the time they were created.

Read more here.

Example:
```python
from ksuid import Ksuid

ksuid = Ksuid()
```

Sections: Svix-KSUID (Python), What is a ksuid?, Usage, Higher timestamp accuracy mode, Examples, Default ksuid, ksuid from datetime, ksuid from base62, ksuid from bytes, Compare ksuid(s), Order of ksuid(s)

</details>

### source-distribution

(no summary)

`pip install source-distribution` · installs from source (sdist only) · licence: not stated · rank 4391 · last release 2024-11-03 · [PyPI](https://pypi.org/project/source-distribution/) · [docs](https://github.com/unknown/source-distribution#readme) · [source](https://github.com/unknown/source-distribution)

### sphn

(no summary)

`pip install sphn` · installs (wheel) · licence: not stated · rank 4413 · last release 2026-01-07 · [PyPI](https://pypi.org/project/sphn/)

### solana

Solana.py

`pip install solana` · installs (wheel) · licence: MIT · rank 4414 · last release 2026-10-03 · [PyPI](https://pypi.org/project/solana/) · [docs](https://michaelhly.com/solana-py/) · [source](https://github.com/michaelhly/solana-py)

<details><summary>README extract</summary>

🐍 The Solana Python SDK 🐍

Solana.py is the base Python library for interacting with Solana.
You can use it to build transactions and interact
with the
Solana JSON RPC API,
much like you would do with
solana-web3.js

It also covers the
SPL Token Program.

Latest Documentation. ...

Example:
```python
import asyncio
from solana.rpc.async_api import AsyncClient

async def main():
    async with AsyncClient(" as client:
        res = await client.is_connected()
    print(res)  # True

    # Alternatively, close the client explicitly instead of using a context manager:
    client = AsyncClient("
    res = await client.is_connected()
...
```

Sections: Solana.py, ⚡ Quickstart, General Usage, Async API Client, Websockets Client, Setup, Lint, Tests, Documentation

</details>

### sudachidict-full

Sudachi Dictionary for SudachiPy - Full Edition

`pip install sudachidict-full` · installs from source (sdist only) · licence: Apache-2.0 · rank 4419 · last release 2026-10-15 · [PyPI](https://pypi.org/project/sudachidict-full/)

<details><summary>README extract</summary>

- WorksApplications/SudachiDict
- WorksApplications/SudachiPy

Managing the dictionary resources as Python packages.

- SudachiDict-small · PyPI
- SudachiDict-core · PyPI
- SudachiDict-full · PyPI

The dictionary files are not included in the packages; It will be downloaded upon installation (the procedure in `setup.py`). ...

Sections: Sudachi Dictionary for SudachiPy, Commands to download and set the dictionaries, Dictionary option in SudachiPy before v0.5.2

</details>

### ssf

Spreadsheet Number Format processor - a Python port of SheetJS/ssf.js

`pip install ssf` · installs (wheel) · licence: Apache Software License · rank 4497 · last release 2020-12-08 · [PyPI](https://pypi.org/project/ssf/)

<details><summary>README extract</summary>

Spreadsheet Number Format processor - a Python port of SheetJS/ssf.js

* Free software: Apache Software License 2.0

Features:
ssf (Spreadsheet Format) is a pure python library to format data using ECMA-376
spreadsheet format codes (used in popular spreadsheet software packages). ...

Sections: ssf, Features, Python Version and Required Libraries, Example, 0.2.2 (2020-10-29), 0.2.1 (2020-10-26), 0.2.0 (2020-10-25), 0.1.5 (2020-10-14), 0.1.2 (2020-10-08), 0.1.0 (2020-10-05)

</details>

### sparkdantic

A pydantic -> spark schema library

`pip install sparkdantic` · installs (wheel) · licence: not stated · rank 4501 · last release 2026-10-13 · [PyPI](https://pypi.org/project/sparkdantic/)

<details><summary>README extract</summary>

> 1️⃣ version: 2.9.0

> ✍️ author: Mitchell Lisle

This Python module provides a utility for converting Pydantic models to PySpark schemas. It's implemented as a class
named `SparkModel` that extends the Pydantic's `BaseModel`.

Features:
- Conversion from Pydantic model to PySpark schema (`StructType` or JSON)
- Type coercion
- PySpark as an optional dependency

Example:
```python
from sparkdantic import SparkModel
from typing import List

class MyModel(SparkModel):
    name: str
    age: int
    hobbies: List[str]
```

Sections: SparkDantic, PySpark Model Conversion Tool, Features, Usage, Creating a new SparkModel, Generating a PySpark Schema, Using `SparkModel`, Using Pydantic `BaseModel`

</details>

### stix2-patterns

Validate STIX 2 Patterns.

`pip install stix2-patterns` · installs (wheel) · licence: BSD License · rank 4523 · last release 2026-02-11 · [PyPI](https://pypi.org/project/stix2-patterns/)

<details><summary>README extract</summary>

This is an OASIS TC Open Repository. See the
Governance section for more information.

The STIX 2 Pattern Validator is a software tool for checking the syntax of the
Cyber Threat Intelligence (CTI) STIX Pattern expressions, which are used within
STIX to express conditions (prepresented with the Cyber Observable data model)
that indicate particular ...

Sections: cti-pattern-validator, Quickstart, Governance, About OASIS TC Open Repositories, Feedback

</details>

### spacy-curated-transformers

Curated transformer models for spaCy pipelines

`pip install spacy-curated-transformers` · installs (wheel) · licence: MIT · rank 4556 · last release 2024-09-30 · [PyPI](https://pypi.org/project/spacy-curated-transformers/)

<details><summary>README extract</summary>

This package provides spaCy components and
architectures to use a curated set of transformer models via
`curated-transformers` in
spaCy.

Features:
- Use pretrained models based on one of the following architectures to
 power your spaCy pipeline:
 - ALBERT
 - BERT
 - CamemBERT
 - RoBERTa
 - XLM-RoBERTa ...

Sections: 💫 🤖 spaCy Curated Transformers, Features, 🚀 Quickstart, 📖 Documentation, Bug reports and other issues

</details>

### sagemaker-train

Open source library for training and deploying models on Amazon SageMaker.

`pip install sagemaker-train` · installs (wheel) · licence: not stated · rank 4577 · last release 2026-11-05 · [PyPI](https://pypi.org/project/sagemaker-train/)

<details><summary>README extract</summary>

SageMaker Python SDK is an open source library for training and deploying machine learning models on Amazon SageMaker.

With the SDK, you can train and deploy models using popular deep learning frameworks Apache MXNet and TensorFlow. ...

Sections: SageMaker Python SDK, . Using the SageMaker Python SDK, Telemetry, AWS Permissions, Licensing, Running tests, Git Hooks

</details>

### sagemaker-serve

SageMaker Serve package for model serving and deployment

`pip install sagemaker-serve` · installs (wheel) · licence: Apache Software License · rank 4592 · last release 2026-11-05 · [PyPI](https://pypi.org/project/sagemaker-serve/)

<details><summary>README extract</summary>

SageMaker Serve package for model serving and deployment.

Sections: SageMaker Serve, Usage

</details>

### sagemaker-mlops

SageMaker MLOps package for workflow orchestration and model building

`pip install sagemaker-mlops` · installs (wheel) · licence: Apache Software License · rank 4608 · last release 2026-11-05 · [PyPI](https://pypi.org/project/sagemaker-mlops/)

<details><summary>README extract</summary>

The `sagemaker-mlops` package provides high-level orchestration capabilities for Amazon SageMaker workflows, including pipeline definitions, step implementations, and model building utilities.

This package sits at the top of the SageMaker SDK dependency hierarchy and orchestrates components from the Core, Train, and Serve packages. ...

Sections: SageMaker MLOps Package, Purpose, Architecture, Package Responsibilities, What's in This Package, Workflow Orchestration (from Core), Model Building, What Stayed in Core

</details>

### slugid

Base64 encoded uuid v4 slugs

`pip install slugid` · installs (wheel) · licence: MPL 2.0 · rank 4630 · last release 2019-02-15 · [PyPI](https://pypi.org/project/slugid/)

### sphinx-book-theme

A clean book theme for scientific explanations and documentation with Sphinx

`pip install sphinx-book-theme` · installs (wheel) · licence: BSD License · rank 4662 · last release 2026-07-19 · [PyPI](https://pypi.org/project/sphinx-book-theme/) · [docs](https://sphinx-book-theme.readthedocs.io/) · [source](https://github.com/executablebooks/sphinx-book-theme)

<details><summary>README extract</summary>

[][codecov-link] [][rtd-link] [][pypi-link]

> [!NOTE]
> Maintenance Mode: This project is currently in maintenance mode. We are accepting bug fixes as best we can, but there are not dedicated resources to review and merge. New feature development is not likely. ...

Sections: sphinx-book-theme, Get started, Documentation

</details>

### sox

Python wrapper around SoX.

`pip install sox` · installs from source (sdist only) · licence: BSD-3-Clause · rank 4740 · last release 2024-03-20 · [PyPI](https://pypi.org/project/sox/)

<details><summary>README extract</summary>

Python wrapper around sox. Read the Docs here.

This library was presented in the following paper:

R. M. Bittner, E. J. Humphrey and J. P. Bello, "pysox: Leveraging the Audio Signal Processing Power of SoX in Python", in Proceedings of the 17th International Society for Music Information Retrieval Conference Late Breaking and Demo Papers, New ...

Sections: pysox, create transformer, trim the audio between 5 and 10.5 seconds., apply compression, apply a fade in and fade out, create an output file., or equivalently using the legacy API, get the output in-memory as a numpy array, see the applied effects, sample rate in Hz, generate a 1-second sine tone at 440 Hz, create a transformer, shift the pitch up by 2 semitones, transform an in-memory array and return an array

</details>

### sasl

Cyrus-SASL bindings for Python

`pip install sasl` · installs from source (sdist only) · licence: Apache License, Version 2.0 · rank 4749 · last release 2021-06-16 · [PyPI](https://pypi.org/project/sasl/)

### sparqlslurper

SPARQL Slurper for rdflib

`pip install sparqlslurper` · installs (wheel) · licence: CC0 1.0 Universal · rank 4859 · last release 2021-12-21 · [PyPI](https://pypi.org/project/sparqlslurper/)

### singer-python

Singer.io utility library

`pip install singer-python` · installs from source (sdist only) · licence: not stated · rank 4861 · last release 2026-11-02 · [PyPI](https://pypi.org/project/singer-python/)

### s3pathlib

s3pathlib is the python package provides the Pythonic objective oriented programming (OOP) interface to manipulate AWS S3 object / directory. The api is similar to the pathlib standard library and very intuitive for human.

`pip install s3pathlib` · installs (wheel) · licence: Apache-2.0 · rank 4871 · last release 2026-10-13 · [PyPI](https://pypi.org/project/s3pathlib/) · [docs](https://s3pathlib.readthedocs.io/en/latest/) · [source](https://github.com/MacHu-GWU/s3pathlib-project)

<details><summary>README extract</summary>

s3pathlib is a Python SDK on top of boto3 that works with Amazon S3 the way the standard library pathlib works with local files: build paths, read and write objects, list and filter folders, copy, move and delete them, with or without versioning.

The full guide and the API reference are on Read the Docs.

Example:
```python
from s3pathlib.api import S3Path

p = S3Path("bucket", "folder", "file.txt")  # also S3Path("s3://bucket/folder/file.txt")
p.uri          # 's3://bucket/folder/file.txt'
p.key          # 'folder/file.txt'
p.parent       # S3Path('s3://bucket/folder/')
p.arn          # 'arn:aws:s3:::bucket/folder/file.txt'
p.console_url  # '
```

...

</details>

### streamlit-aggrid

Streamlit component implementation of ag-grid

`pip install streamlit-aggrid` · installs (wheel) · licence: MIT License · rank 4881 · last release 2025-12-29 · [PyPI](https://pypi.org/project/streamlit-aggrid/)

<details><summary>README extract</summary>

[][share_link] [][github_link] [][pypi_link] [][downloads_link]

> [!IMPORTANT]
> 💡 Support the Development of streamlit-aggrid!
> This project is the result of countless hours of dedication by a solo Python developer. If you find it useful, consider giving back to help keep it alive and thriving. ...

Example:
```python
from st_aggrid import AgGrid
import pandas as pd

df = pd.read_csv('
AgGrid(df)
```

Sections: streamlit-aggrid, Quick Use, Demo

</details>

### stable-baselines3

Pytorch version of Stable Baselines, implementations of reinforcement learning algorithms.

`pip install stable-baselines3` · installs (wheel) · licence: MIT · rank 4903 · last release 2026-10-26 · [PyPI](https://pypi.org/project/stable-baselines3/) · [docs](https://stable-baselines3.readthedocs.io/) · [source](https://github.com/DLR-RM/stable-baselines3)

<details><summary>README extract</summary>

Stable Baselines3 is a set of reliable implementations of reinforcement learning algorithms in PyTorch. It is the next major version of Stable Baselines.

These algorithms will make it easier for the research community and industry to replicate, refine, and identify new ideas, and will create good baselines to build projects on top of. ...

Example:
```python
import gymnasium

from stable_baselines3 import PPO

env = gymnasium.make("CartPole-v1", render_mode="human")

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10_000)

vec_env = model.get_env()
obs = vec_env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
...
```

Sections: Stable Baselines3, Links, Quick example

</details>

### suds-py3

Lightweight SOAP client

`pip install suds-py3` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 4914 · last release 2021-11-15 · [PyPI](https://pypi.org/project/suds-py3/)

_README extract left out: share-alike licence._

### sglang-kernel

Kernel Library for SGLang

`pip install sglang-kernel` · installs (wheel) · licence: Apache Software License · rank 4916 · last release 2026-10-15 · [PyPI](https://pypi.org/project/sglang-kernel/)

<details><summary>README extract</summary>

Kernel Library for LLM inference engines

`sglang-kernel` provides optimized compute primitives for LLM inference engines, enabling efficient inference for large language models and vision-language models through custom kernel operations. ...

Sections: sglang-kernel (prior sgl-kernel), Building from Source, Use Makefile to build from the sgl-kernel source tree, Limit build resource usage (CPU / parallelism), Steps to add a new kernel, Adapting C++ Native Types for Torch Compatibility, Kernel Size Analysis, FAQ

</details>

### simpervisor

Simple async process supervisor

`pip install simpervisor` · installs (wheel) · licence: not stated · rank 4926 · last release 2023-05-18 · [PyPI](https://pypi.org/project/simpervisor/) · [docs](https://github.com/jupyterhub/simpervisor#readme) · [source](https://github.com/jupyterhub/simpervisor)

<details><summary>README extract</summary>

simpervisor provides the SupervisedProcess class that provides async methods
`start`, `ready`, `terminate`, and `kill` to manage it. As an example of how it
can be used, see how jupyterhub/jupyter-server-proxy uses it.

</details>

### sqlalchemy-mate

A library extend sqlalchemy module, makes CRUD easier.

`pip install sqlalchemy-mate` · installs (wheel) · licence: MIT License · rank 4954 · last release 2024-06-06 · [PyPI](https://pypi.org/project/sqlalchemy-mate/)

<details><summary>README extract</summary>

A sweet syntax sugar library simplify your in writing `sqlalchemy` code.

📔 Full document is HERE

Example:
```python
from sqlalchemy_mate.api import EngineCreator

ec = EngineCreator.from_json(
    json_file="path-to-json-file",
    json_path="credentials.db1", # dot notation json path
)
engine = ec.create_postgresql_pg8000()
```

Sections: Welcome to `sqlalchemy_mate` Documentation, Features, Read Database Credential Safely, From json file, From `$HOME/.db.json`, From json file on AWS S3, From Environment Variable, Smart Insert, Smart Update / Upsert

</details>

### stytch

Stytch python client

`pip install stytch` · installs (wheel) · licence: MIT License · rank 4996 · last release 2026-06-24 · [PyPI](https://pypi.org/project/stytch/)

<details><summary>README extract</summary>

The Stytch Python library makes it easy to use the Stytch user infrastructure API in Python applications.

It pairs well with the Stytch Web SDK or your own custom authentication flow.

The Stytch Python library supports Python 3.10+

Example:
```python
import stytch

client = stytch.Client(
    project_id="project-live-c60c0abe-c25a-4472-a9ed-320c6667d317",
    secret="secret-live-80JASucyk7z_G8Z-7dVwZVGXL5NT_qGAQ2I=",
    # Optionally specify a custom base URL for all API calls
    # custom_base_url="
)
```

Sections: Stytch Python Library, Requirements, Usage, B2C, B2B, Example B2C usage, Example B2B usage, Handling Errors, Documentation

</details>

### sqids

Generate YouTube-like ids from numbers.

`pip install sqids` · installs (wheel) · licence: MIT License · rank 5076 · last release 2025-05-13 · [PyPI](https://pypi.org/project/sqids/)

<details><summary>README extract</summary>

Sqids (*pronounced "squids"*) is a small library that lets you generate unique IDs from numbers. It's good for link shortening, fast & URL-safe ID generation and decoding back into numbers for quicker database lookups.

Features:

- Encode multiple numbers - generate short IDs from one or several non-negative numbers ...

Example:
```python
from sqids import Sqids
sqids = Sqids()
```

Sections: Sqids Python, 🧰 Use-cases, 🚀 Getting started, 👩‍💻 Examples

</details>

### sqlalchemy-rdsiam

SQLAlchemy dialects to connect to Amazon RDS instances with IAM authentication

`pip install sqlalchemy-rdsiam` · installs (wheel) · licence: not stated · rank 5116 · last release 2023-11-08 · [PyPI](https://pypi.org/project/sqlalchemy-rdsiam/)

<details><summary>README extract</summary>

SQLAlchemy dialect to connect to Amazon RDS instances with IAM authentication.

The following are supported:

- Amazon RDS PostgreSQL, with `psycopg2`.
- Amazon RDS PostgreSQL, with `asyncpg`.

SQLAlchemy 1.3, 1.4 and 2.0 are supported. ...

Sections: `sqlalchemy-rdsiam`, Background, Getting Started, Additional Configuration, AWS Region, Creating the Database If It Doesn't Exists, Set `sslrootcert` to the Amazon RDS Certificate Bundle

</details>

### sql-formatter

A SQL formatter

`pip install sql-formatter` · installs (wheel) · licence: Apache Software License · rank 5139 · last release 2021-05-01 · [PyPI](https://pypi.org/project/sql-formatter/)

<details><summary>README extract</summary>

> A Python based SQL formatter

Example:
```python
from sql_formatter.core import format_sql
print(format_sql(example_sql))
```

Sections: sql_formatter, How to use, Controlling maximum length line via truncation, Usage with `pre-commit`, Usage in Python, A note of caution, What `sql_formatter` does not do, Formatting Logic, Versioning

</details>

### substrait

A python package for Substrait.

`pip install substrait` · installs (wheel) · licence: Apache-2.0 · rank 5175 · last release 2026-11-03 · [PyPI](https://pypi.org/project/substrait/)

<details><summary>README extract</summary>

A Python package for Substrait, the cross-language specification for data compute operations.

Example:
```python
import substrait.dataframe as sub

plan = (
    sub.read_named_table("people", {"id": sub.i64, "age": sub.i64, "name": sub.string})
    .filter(sub.col("age") > 25)
    .with_columns(adult=sub.col("age") >= 18)
    .select("id", "name", "adult")
    .to_plan()
)
```

Sections: Substrait, Goals, Non-goals, Substrait version, Building plans with the DataFrame API, Example (low-level API), Produce a Substrait Plan, Consume the Substrait Plan, Load a Substrait Plan from JSON, Deeply nested expressions, Produce a Substrait Plan with Ibis, Getting Involved

</details>

### structlog-gcp

A structlog set of processors to output as Google Cloud Logging format

`pip install structlog-gcp` · installs (wheel) · licence: not stated · rank 5185 · last release 2026-07-07 · [PyPI](https://pypi.org/project/structlog-gcp/) · [docs](https://github.com/multani/structlog-gcp#readme) · [source](https://github.com/multani/structlog-gcp)

<details><summary>README extract</summary>

This is an opiniated package that configures structlog
to output log compatible with the Google Cloud Logging log
format.

The intention of this package is to be used for applications that run in Google
Kubernetes Engine (GKE) or Google
Cloud Function, or any other systems that
know how to send logs to Google Cloud. ...

Example:
```python
import structlog
import structlog_gcp

processors = structlog_gcp.build_processors()
structlog.configure(processors=processors)
```

Sections: Google Cloud Logging formatter for `structlog`, How to use?, Errors, Using `logger.exception`, Using `logger.$LEVEL(..., exception=exc)`, Using `logger.$LEVEL(...)`, Configuration, Advanced Configuration, Examples, Reference

</details>

### scikit-fem

Simple finite element assemblers

`pip install scikit-fem` · installs (wheel) · licence: BSD License · rank 5203 · last release 2026-06-05 · [PyPI](https://pypi.org/project/scikit-fem/) · [source](https://github.com/kinnala/scikit-fem)

<details><summary>README extract</summary>

`scikit-fem` is a pure Python 3.10+ library for performing finite element
assembly. Its main
purpose is the transformation of bilinear forms into sparse matrices and linear
forms into vectors.

The library

- has minimal dependencies
- contains no compiled code ...

Example:
```python
from skfem import *
from skfem.helpers import dot, grad

# create the mesh
mesh = MeshTri().refined(4)
# or, with your own points and elements:
# mesh = MeshTri(points, elements)

basis = Basis(mesh, ElementTriP1())

@BilinearForm
def laplace(u, v, _):
    return dot(grad(u), grad(v))

@LinearForm
def rhs(v, _):
    return 1. * v

...
```

...

</details>

### sphinx-autoapi

Sphinx API documentation generator

`pip install sphinx-autoapi` · installs (wheel) · licence: MIT License · rank 5218 · last release 2026-10-31 · [PyPI](https://pypi.org/project/sphinx-autoapi/) · [docs](https://sphinx-autoapi.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Sphinx AutoAPI is a Sphinx extension for generating complete API documentation
without needing to load, run, or import the project being documented.

In contrast to the traditional Sphinx autodoc,
which requires manual authoring and uses code imports,
AutoAPI finds and generates documentation by parsing source code. ...

Sections: Sphinx AutoAPI, Getting Started, Running the tests, Code Style, Versioning

</details>

### shot-scraper

A CLI utility for taking screenshots of websites, recording video demos and scraping sites using JavaScript

`pip install shot-scraper` · installs (wheel) · licence: Apache-2.0 · rank 5295 · last release 2026-09-14 · [PyPI](https://pypi.org/project/shot-scraper/)

<details><summary>README extract</summary>

A CLI utility for taking screenshots of websites, recording video demos and scraping sites using JavaScript

For background on this project see shot-scraper: automated screenshots for documentation, built on Playwright.

- Full documentation for shot-scraper
- Tutorial: Automating screenshots for the Datasette documentation using shot-scraper ...

Sections: shot-scraper, Documentation, Get started with GitHub Actions, Taking your first screenshot, Examples

</details>

### streamlit-autorefresh

Simple way to autorefresh your Streamlit apps

`pip install streamlit-autorefresh` · installs (wheel) · licence: not stated · rank 5299 · last release 2023-06-25 · [PyPI](https://pypi.org/project/streamlit-autorefresh/)

### starlark-pyo3

Wraps starlark-rust into Python

`pip install starlark-pyo3` · installs (wheel) · licence: not stated · rank 5351 · last release 2026-10-19 · [PyPI](https://pypi.org/project/starlark-pyo3/) · [docs](https://documen.tician.de/starlark-pyo3/) · [source](https://github.com/inducer/starlark-pyo3)

<details><summary>README extract</summary>

This package provides a sandboxed/restricted Python-like environment
by exposing the
starlark-rust
interpreter for the
Starlark
Python-like language to Python via PyO3.

Starlark claims the following

- Deterministic evaluation. Executing the same code twice will give the
 same results.
- Hermetic execution. ...

Sections: Starlark-PyO3: Python bindings for starlark-rust, Links

</details>

### SALib

Tools for global sensitivity analysis. Contains Sobol', Morris, FAST, DGSM, PAWN, HDMR, Moment Independent and fractional factorial methods

`pip install SALib` · installs (wheel) · licence: MIT · rank 5394 · last release 2026-09-19 · [PyPI](https://pypi.org/project/SALib/) · [docs](https://salib.readthedocs.io) · [source](https://github.com/SALib/SALib)

<details><summary>README extract</summary>

Python implementations of commonly used sensitivity analysis methods.
Useful in systems modeling to calculate the effects of model inputs or
exogenous factors on outputs of interest.

Documentation: ReadTheDocs

Requirements: NumPy,
SciPy,
matplotlib,
pandas,
Python 3 (from SALib v1.2 onwards SALib does not officially support Python 2) ...

Example:
```python
from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
import numpy as np

problem = {
  'num_vars': 3,
  'names': ['x1', 'x2', 'x3'],
  'bounds': [[-np.pi, np.pi]]*3
}

# Generate samples
param_values = saltelli.sample(problem, 1024)

# Run model (example)
Y = Ishigami.evaluate(param_values)

...
```

...

</details>

### sgl-deep-ep

(no summary)

`pip install sgl-deep-ep` · does not install on CPython 3.14 · licence: not stated · rank 5409 · last release 2026-10-03 · [PyPI](https://pypi.org/project/sgl-deep-ep/)

<details><summary>README extract</summary>

`sgl-deep-ep` is SGLang's binary distribution of
DeepEP. The distribution name is
`sgl-deep-ep`, while the Python import remains compatible with DeepEP:

Example:
```python
import deep_ep
```

Sections: sgl-deep-ep, Host prerequisites

</details>

### sgl-deep-gemm

SGLang fork of DeepGemm

`pip install sgl-deep-gemm` · installs (wheel) · licence: Apache-2.0 · rank 5422 · last release 2026-11-07 · [PyPI](https://pypi.org/project/sgl-deep-gemm/) · [source](https://github.com/sgl-project/DeepGEMM/tree/release)

<details><summary>README extract</summary>

sgl-deep-gemm is a pypi package built from SGLang's customized branch of DeepGemm. Comparing with origina DeepGemm, it supports the following features to better support SGLang:
1. ...

Sections: Introduction, Usage

</details>

### swapper

The unofficial Django swappable models API.

`pip install swapper` · installs (wheel) · licence: MIT License · rank 5428 · last release 2026-09-01 · [PyPI](https://pypi.org/project/swapper/)

<details><summary>README extract</summary>

Swapper is an unofficial API for the [undocumented] but very powerful Django
feature: swappable models. Swapper facilitates implementing
arbitrary swappable models in your own reusable apps.

- Python 3.10 or later
- Django 4.2 or later

Example:
```python
from django.db import models
class Parent(models.Model):
    name = models.TextField()

class Child(models.Model):
    name = models.TextField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
```

Sections: Swapper, Django Swappable Models - No longer only for auth.User!, Requirements, Motivation, Real-World Examples, Creating a Reusable App, Loading Swapped Models, Migration Scripts, End User Documentation, API Documentation

</details>

### singleton-decorator

A testable singleton decorator

`pip install singleton-decorator` · installs from source (sdist only) · licence: GPLv3 · rank 5482 · last release 2017-08-10 · [PyPI](https://pypi.org/project/singleton-decorator/)

_README extract left out: share-alike licence._

### schematics

Python Data Structures for Humans

`pip install schematics` · installs (wheel) · licence: BSD License · rank 5492 · last release 2021-08-17 · [PyPI](https://pypi.org/project/schematics/)

### sqlmesh

Next-generation data transformation framework

`pip install sqlmesh` · installs (wheel) · licence: Apache Software License · rank 5515 · last release 2026-10-22 · [PyPI](https://pypi.org/project/sqlmesh/) · [docs](https://sqlmesh.readthedocs.io/en/stable/) · [source](https://github.com/SQLMesh/sqlmesh)

<details><summary>README extract</summary>

SQLMesh is a project of the Linux Foundation.

SQLMesh is a next-generation data transformation framework designed to ship data quickly, efficiently, and without error. Data teams can run and deploy data transformations written in SQL or Python with visibility and control at any size.

It is more than just a dbt alternative. ...

Sections: Core Features, Getting Started

</details>

### smolagents

🤗 smolagents: a barebones library for agents. Agents write python code to call tools or orchestrate other agents.

`pip install smolagents` · installs (wheel) · licence: not stated · rank 5534 · last release 2026-05-29 · [PyPI](https://pypi.org/project/smolagents/)

<details><summary>README extract</summary>

Agents that think in code!

`smolagents` is a library that enables you to run powerful agents in a few lines of code. It offers:

✨ Simplicity: the logic for agents fits in ~1,000 lines of code (see agents.py). We kept abstractions to their minimal shape above raw code!

🧑‍💻 First-class support for Code Agents. ...

Example:
```python
from smolagents import CodeAgent, WebSearchTool, InferenceClientModel

model = InferenceClientModel()
agent = CodeAgent(tools=[WebSearchTool()], model=model, stream_outputs=True)

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
```

Sections: Quick demo, CLI, How do Code agents work?, How smol is this library?, How strong are open models for agentic workflows?

</details>

### sklearn-crfsuite

CRFsuite (python-crfsuite) wrapper which provides interface simlar to scikit-learn

`pip install sklearn-crfsuite` · installs (wheel) · licence: MIT License · rank 5567 · last release 2024-06-18 · [PyPI](https://pypi.org/project/sklearn-crfsuite/)

<details><summary>README extract</summary>

sklearn-crfsuite is a thin CRFsuite (python-crfsuite) wrapper which provides
interface simlar to scikit-learn. `sklearn_crfsuite.CRF` is a scikit-learn
compatible estimator: you can use e.g. scikit-learn model
selection utilities (cross-validation, hyperparameter optimization) with it,
or save/load CRF models using joblib.

License is MIT. ...

Sections: sklearn-crfsuite, Changes, 0.5.0 (2024-06-18), 0.4.0 (2024-06-18), 0.3.6 (2017-06-22), 0.3.5 (2017-03-21), 0.3.4 (2016-11-17), 0.3.3 (2016-03-15), 0.3.2 (2015-12-18), 0.3.1 (2015-12-17), 0.3 (2015-12-17), 0.2 (2015-12-11), 0.1 (2015-11-27)

</details>

### scim2-models

SCIM2 models serialization and validation with pydantic

`pip install scim2-models` · installs (wheel) · licence: Apache-2.0 · rank 5576 · last release 2026-10-29 · [PyPI](https://pypi.org/project/scim2-models/) · [docs](https://scim2-models.readthedocs.io) · [source](https://github.com/python-scim/scim2-models)

<details><summary>README extract</summary>

Pydantic models for the SCIM 2.0 schemas and protocol.
It parses and produces SCIM payloads as native Python objects, and serves as a basis for SCIM
servers and clients.

Features:
- Models for the resources and messages of RFC 7643 and RFC 7644: `User`, `Group`,
 `EnterpriseUser`, `Schema`, `ResourceType`, `ServiceProviderConfig`, `ListResponse`,
 `SearchRequest`, `PatchOp` and `Error` ...

Example:
```python
from scim2_models import User
import datetime

payload = {
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "2819c223-7f76-453a-919d-413861904646",
    "userName": "bjensen@example.com",
    "meta": {
        "resourceType": "User",
        "created": "2010-01-23T04:56:22Z",
        "lastModified": "2011-05-13T04:42:34Z",
...
```

...

</details>

### soundex

Soundex algorith implementation for English and Indian languages

`pip install soundex` · installs from source (sdist only) · licence: DFSG approved; GNU Lesser General Public License v2 or later (LGPLv2+) · rank 5578 · last release 2014-06-01 · [PyPI](https://pypi.org/project/soundex/)

_README extract left out: share-alike licence._

### silpa_common

Common functions for SILPA and related modules

`pip install silpa_common` · installs from source (sdist only) · licence: DFSG approved; GNU Lesser General Public License v2 or later (LGPLv2+) · rank 5581 · last release 2014-05-03 · [PyPI](https://pypi.org/project/silpa_common/)

_README extract left out: share-alike licence._

### sqlalchemy-cockroachdb

CockroachDB dialect for SQLAlchemy

`pip install sqlalchemy-cockroachdb` · installs (wheel) · licence: Apache Software License · rank 5622 · last release 2026-04-23 · [PyPI](https://pypi.org/project/sqlalchemy-cockroachdb/) · [docs](https://github.com/cockroachdb/sqlalchemy-cockroachdb/wiki) · [source](https://github.com/cockroachdb/sqlalchemy-cockroachdb)

<details><summary>README extract</summary>

A database driver (DBAPI layer) is required to work with this dialect.

For psycopg2 support you must install either:

* psycopg2, which has some
 prerequisites of
 its own, or

* psycopg2-binary

(The binary package is a practical choice for development and testing but in
production it is advised to use the package built from sources.)

Sections: CockroachDB dialect for SQLAlchemy, Prerequisites, psycopg2, asyncpg, psycopg

</details>

### s2sphere

Python implementation of the S2 Geometry Library

`pip install s2sphere` · installs (wheel) · licence: MIT License · rank 5652 · last release 2017-11-16 · [PyPI](https://pypi.org/project/s2sphere/)

<details><summary>README extract</summary>

Python implementation of a part of the C++ S2 geometry library.

Links: Documentation,
GitHub,
Issue Tracker

Install with:

Quick set up for development (see the Developing section in the docs for more details):

</details>

### selenium-wire

Extends Selenium to give you the ability to inspect requests made by the browser.

`pip install selenium-wire` · installs (wheel) · licence: MIT License · rank 5682 · last release 2022-10-15 · [PyPI](https://pypi.org/project/selenium-wire/)

<details><summary>README extract</summary>

Selenium Wire extends Selenium's Python bindings to give you access to the underlying requests made by the browser. You author your code in the same way as you do with Selenium, but you get extra APIs for inspecting requests and responses and making changes to them on the fly.

Features:
* Pure Python, user-friendly API
* HTTP and HTTPS requests captured
* Intercept requests and responses
* Modify headers, parameters, body content on the fly
* Capture websocket messages
* HAR format supported
* Proxy server support

Example:
```python
from seleniumwire import webdriver  # Import from seleniumwire

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Go to the Google home page
driver.get('

# Access requests via the `requests` attribute
...

</details>

### sha256

sha256 library with midstate

`pip install sha256` · installs from source (sdist only) · licence: MIT License · rank 5691 · last release 2024-01-03 · [PyPI](https://pypi.org/project/sha256/) · [source](https://github.com/cloudtools/sha256)

<details><summary>README extract</summary>

This is a SHA-256 implementation that allows for setting and getting
the mid-state information. This was needed to enable repeated hashing
against a (potentially large) fixed prefix.

The original version of this was written in Python. ...

Sections: Performance, Cythonize

</details>

### semver4

Semantic versioning module enriched by hotfix version

`pip install semver4` · installs (wheel) · licence: MIT License · rank 5697 · last release 2024-03-24 · [PyPI](https://pypi.org/project/semver4/)

<details><summary>README extract</summary>

Features:
A python module to deal with modified semantic versioning.

Example:
```python
from semver4 import Version

version = Version4('2.4.4.0-alpha+123')
print(version)
# '2.4.4-alpha+123'

version = Version4(major=2, minor=4, patch=4, prerelease='beta', build='12346')
print(version)
# '2.4.4-beta+12346'
print(version.minor, version.fix)
# 4 0
print(version.core)
# '2.4.4'

print(version > Version('0.4.2.4'))
# True
...
```

Sections: Overview, Motivation, Fix version part, Usage

</details>

### symspellpy

Python SymSpell

`pip install symspellpy` · installs (wheel) · licence: MIT License · rank 5700 · last release 2026-11-07 · [PyPI](https://pypi.org/project/symspellpy/) · [docs](https://symspellpy.readthedocs.io/en/latest) · [source](https://github.com/mammothb/symspellpy)

<details><summary>README extract</summary>

symspellpy

========

symspellpy is a Python port of SymSpell v6.7.2, which provides much higher speed and lower memory consumption. Unit tests
from the original project are implemented to ensure the accuracy of the port.

Please note that the port has not been optimized for speed.

v6.7.2: Implemented fast distance comparer with editdistpy. ...

Sections: Notable Changes, Usage

</details>

### stim

A fast library for analyzing with quantum stabilizer circuits.

`pip install stim` · installs (wheel) · licence: Apache 2 · rank 5749 · last release 2026-05-22 · [PyPI](https://pypi.org/project/stim/)

<details><summary>README extract</summary>

Stim is a fast simulator for quantum stabilizer circuits.

API references are available on the stim github wiki:

Stim can be installed into a python 3 environment using pip:

Once stim is installed, you can `import stim` and use it.
There are three supported use cases:

1. Interactive simulation with `stim.TableauSimulator`.
2. ...

Example:
```python
import stim

s = stim.TableauSimulator()

# Create a GHZ state.
s.h(0)
s.cnot(0, 1)
s.cnot(0, 2)

# Look at the simulator state re-inverted to be forwards:
t = s.current_inverse_tableau()
print(t**-1)
# prints:
# +-xz-xz-xz-
# | ++ ++ ++
# | ZX _Z _Z
# | _X XZ __
# | _X __ XZ

# Measure the GHZ state.
print(s.measure_many(0, 1, 2))
...
```

Sections: Stim, Interactive Simulation, High Speed Sampling, Independent Exploration

</details>

### session-info

session_info outputs version information for modules loaded in the current session, Python, and the OS.

`pip install session-info` · installs (wheel) · licence: BSD-3 · rank 5775 · last release 2025-04-11 · [PyPI](https://pypi.org/project/session-info/)

<details><summary>README extract</summary>

`session_info` outputs version information for modules loaded in the current session,
Python, the OS, and the CPU. It is designed as a minimum measure to increase
reproducibility and provides similar information as `sessionInfo` and
`devtools::session_info` in R. ...

Example:
```python
import math

import natsort
import pandas
import session_info

session_info.show()
```

Sections: session_info, Motivation, Usage, Background

</details>

### symfc

This is the symfc module.

`pip install symfc` · installs (wheel) · licence: not stated · rank 5791 · last release 2026-11-06 · [PyPI](https://pypi.org/project/symfc/)

<details><summary>README extract</summary>

Atomic vibrations in crystals are often conveniently described using the phonon
model. In this model, the crystal potential is expanded into a Taylor series
with respect to atomic displacements from their equilibrium positions, and the
expansion coefficients are referred to as force constants. ...

Sections: symfc, What does symfc do?

</details>

### SocketSwap

SocketSwap is a python package that allows to proxy any third-party libraries traffic through a local TCP Proxy

`pip install SocketSwap` · installs (wheel) · licence: MIT License · rank 5850 · last release 2023-09-29 · [PyPI](https://pypi.org/project/SocketSwap/)

<details><summary>README extract</summary>

SocketSwap is a tool that allows to proxy any third-party libraries traffic through a TCP SOCKS5 Proxy.

Some Python libaries support proxing out of the box like requests.
For all other libaries especially ones not natively written in python, you can use SocketSwap to redirect traffic via a proxy.

Example:
```python
import socket
from SocketSwap import ProxySwapContext

def socket_factory():
    target_host = "localhost"
    target_port = 5432
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((target_host, target_port))
    return remote_socket

def main():

...
```

Sections: SocketSwap, Usage, Context Manager, Logging and Debugging

</details>

### sphinx-gallery

A Sphinx extension that builds an HTML gallery of examples from any set of Python scripts.

`pip install sphinx-gallery` · installs (wheel) · licence: 3-clause BSD · rank 5864 · last release 2026-09-18 · [PyPI](https://pypi.org/project/sphinx-gallery/) · [docs](https://sphinx-gallery.github.io) · [source](https://github.com/sphinx-gallery/sphinx-gallery)

<details><summary>README extract</summary>

A Sphinx extension that builds an
HTML gallery of examples from any set of Python scripts.
Check out the documentation for introductions on how to use it and more...

Sections: Sphinx-Gallery, Quickstart, Add examples to your docs, Who uses Sphinx-Gallery

</details>

### Secweb

Secweb is a pack of security middlewares for fastApi and starlette servers it includes CSP, HSTS, and many more

`pip install Secweb` · installs (wheel) · licence: MPL-2.0 · rank 5880 · last release 2026-07-30 · [PyPI](https://pypi.org/project/Secweb/) · [docs](https://github.com/tmotagam/Secweb#readme) · [source](https://github.com/tmotagam/Secweb.git)

<details><summary>README extract</summary>

Secweb helps in setting security headers for FastApi and Starlette

Secweb is the pack of security headers for fastapi and can also be used for any framework created on starlette. It has 16 security headers for your websites/APIs.

Features:
- 🔒 Secure Headers: Automatically apply headers like `Strict-Transport-Security`, `Content-Security-Policy`, and more.

- 🛠️ Customizable Policies: Flexibly build your own security policies. ...

Example:
```python
from Secweb import SecWeb

SecWeb(app=app) # The app is the ASGIapp required by the Starlette/FastApi to give access to the different methods to the class
```

Sections: Features, Requirements, Usage, SecWeb class, Middleware Classes, Nonce Processor, For FastApi server, For Starlette server, Origin Agent Cluster, Referrer Policy

</details>

### setuptools-scm-git-archive

setuptools_scm plugin for git archives

`pip install setuptools-scm-git-archive` · installs (wheel) · licence: MIT · rank 5913 · last release 2023-09-21 · [PyPI](https://pypi.org/project/setuptools-scm-git-archive/)

<details><summary>README extract</summary>

This plugin is obsolete. ``setuptools_scm >= 7.0.0`` supports Git archives by itself.

Migration guide

Change the contents of the ``.git_archival.txt`` file in the root directory of your repository from::

 ref-names: $Format:%D$

to:: ...

</details>

### serpyco-rs

(no summary)

`pip install serpyco-rs` · installs (wheel) · licence: MIT License · rank 5926 · last release 2026-09-22 · [PyPI](https://pypi.org/project/serpyco-rs/)

### sspilib

SSPI API bindings for Python

`pip install sspilib` · installs (wheel) · licence: MIT · rank 5963 · last release 2026-08-24 · [PyPI](https://pypi.org/project/sspilib/)

<details><summary>README extract</summary>

This library provides Python functions that wraps the Windows SSPI API.
It is designed to be both a high and low level interface that other libraries can easily leverage to use with SSPI integration.
The high level interface is under the `sspilib` namespace whereas the low-level interface is under the `sspilib.raw` interface.

* Python 3.10+ ...

Example:
```python
import sspilib

cred = sspilib.UserCredential(
    "username@DOMAIN.COM",
    "password",
)

ctx = sspilib.ClientSecurityContext(
    credential=cred,
    target_name="host/server.domain.com",
)

in_token = None
while not ctx.complete:
    out_token = ctx.step(in_token)
    if not out_token:
        break

...
```

...

</details>

### syncer

Async to sync converter

`pip install syncer` · installs from source (sdist only) · licence: MIT License · rank 5970 · last release 2023-05-08 · [PyPI](https://pypi.org/project/syncer/)

<details><summary>README extract</summary>

Syncer is an async-to-sync converter for python.

Features:
Sometimes (mainly in test) we need to convert asynchronous functions to normal,
synchronous functions and run them synchronously. It can be done by
`ayncio.get_event_loop().run_until_complete()`, but it's quite long... ...

Example:
```python
from syncer import sync
async def async_fun():
    ...
    return 1
b = sync(async_fun)  # now b is synchronous
assert 1 == b()
```

Sections: Syncer, Features, Usage

</details>

### snuggs

Snuggs are s-expressions for Numpy

`pip install snuggs` · installs (wheel) · licence: MIT · rank 5978 · last release 2019-09-18 · [PyPI](https://pypi.org/project/snuggs/)

<details><summary>README extract</summary>

Snuggs are s-expressions for Numpy

Snuggs wraps Numpy in expressions with the following syntax:

Example:
```python
>>> snuggs.eval("(+ (asarray 1 1) (asarray 2 2))")
array([3, 3])
```

Sections: snuggs, Syntax, Examples, Addition of two numbers, Multiplication of a number and an array, Evaluation context, Functions and operators, Higher-order functions, Performance notes

</details>

### smartystreets-python-sdk

An official library to help Python developers easily access the SmartyStreets APIs

`pip install smartystreets-python-sdk` · installs (wheel) · licence: Apache Software License · rank 6005 · last release 2026-10-30 · [PyPI](https://pypi.org/project/smartystreets-python-sdk/)

### segment-anything

(no summary)

`pip install segment-anything` · installs (wheel) · licence: not stated · rank 6034 · last release 2023-04-06 · [PyPI](https://pypi.org/project/segment-anything/)

### segmentation-models-pytorch

Image segmentation models with pre-trained backbones. PyTorch.

`pip install segmentation-models-pytorch` · installs (wheel) · licence: MIT · rank 6049 · last release 2026-10-26 · [PyPI](https://pypi.org/project/segmentation-models-pytorch/)

<details><summary>README extract</summary>

**Python library with Neural Networks for Image Semantic
Segmentation based on PyTorch.**

The main features of the library are:

 - Super simple high-level API (just two lines to create a neural network)
 - 12 encoder-decoder model architectures (Unet, Unet++, Segformer, DPT, ...)
 - 800+ pretrained convolution- and transform-based encoders, ...

Example:
```python
import segmentation_models_pytorch as smp

model = smp.Unet(
    encoder_name="resnet34",        # choose encoder, e.g. mobilenet_v2 or efficientnet-b7
    encoder_weights="imagenet",     # use `imagenet` pre-trained weights for encoder initialization
...
```

...

</details>

### srptools

Tools to implement Secure Remote Password (SRP) authentication

`pip install srptools` · installs (wheel) · licence: BSD-3-Clause · rank 6069 · last release 2026-10-26 · [PyPI](https://pypi.org/project/srptools/) · [docs](https://srptools.readthedocs.io/)

<details><summary>README extract</summary>

*Tools to implement Secure Remote Password (SRP) authentication*

SRP is a secure password-based authentication and key-exchange protocol —
a password-authenticated key agreement protocol (PAKE).

!!! note
 This package contains protocol implementation for Python 3.
 The last version with Python 2 support is `1.0.1`. ...

Sections: srptools, Description, Documentation, Quickstart

</details>

### snac

Multi-Scale Neural Audio Codec

`pip install snac` · installs (wheel) · licence: not stated · rank 6106 · last release 2024-09-11 · [PyPI](https://pypi.org/project/snac/)

<details><summary>README extract</summary>

Multi-Scale Neural Audio Codec (SNAC) compresses audio into discrete codes at a low bitrate.

| 🎸 Music samples | 🗣️ Speech samples |

| <video src=' | <video src=' |

🎧 More audio samples available at

Features:
SNAC encodes audio into hierarchical tokens similarly to SoundStream, EnCodec, and DAC (see the image
on the left). However, SNAC introduces a simple change where coarse tokens are sampled less frequently,
covering a broader time span (see the image ...

Example:
```python
import torch
from snac import SNAC

model = SNAC.from_pretrained("hubertsiuzdak/snac_32khz").eval().cuda()
audio = torch.randn(1, 1, 32000).cuda()  # placeholder for actual audio with shape (B, 1, T)

with torch.inference_mode():
    codes = model.encode(audio)
    audio_hat = model.decode(codes)
```

...

</details>

### scrapbook

A library for recording and reading data in Jupyter and nteract Notebooks

`pip install scrapbook` · installs (wheel) · licence: BSD License · rank 6108 · last release 2021-01-06 · [PyPI](https://pypi.org/project/scrapbook/) · [docs](https://nteract-scrapbook.readthedocs.io) · [source](https://github.com/nteract/scrapbook/)

<details><summary>README extract</summary>

The scrapbook library records a notebook’s data values and generated visual
content as "scraps". Recorded scraps can be read at a future time.

See the scrapbook documentation for
more information on how to use scrapbook.

Notebook users may wish to record data produced during a notebook's execution. ...

Example:
```python
"""glue example for recording data values"""
import scrapbook as sb

sb.glue("hello", "world")
sb.glue("number", 123)
sb.glue("some_list", [1, 3, 5])
sb.glue("some_dict", {"a": 1, "b": 2})
sb.glue("non_json", df, 'arrow')
```

...

</details>

### seqeval

Testing framework for sequence labeling

`pip install seqeval` · installs from source (sdist only) · licence: MIT License · rank 6204 · last release 2020-10-24 · [PyPI](https://pypi.org/project/seqeval/)

<details><summary>README extract</summary>

seqeval is a Python framework for sequence labeling evaluation.
seqeval can evaluate the performance of chunking tasks such as named-entity recognition, part-of-speech tagging, semantic role labeling and so on. ...

Example:
```python
>>> from seqeval.metrics import accuracy_score
>>> from seqeval.metrics import classification_report
>>> from seqeval.metrics import f1_score
>>> y_true = [['O', 'O', 'O', 'B-MISC', 'I-MISC', 'I-MISC', 'O'], ['B-PER', 'I-PER', 'O']]
>>> y_pred = [['O', 'O', 'B-MISC', 'I-MISC', 'I-MISC', 'I-MISC', 'O'], ['B-PER', 'I-PER', 'O']]
...
```

Sections: seqeval, Usage

</details>

### slacker

Slack API client

`pip install slacker` · installs from source (sdist only) · licence: Apache Software License · rank 6272 · last release 2020-02-15 · [PyPI](https://pypi.org/project/slacker/)

<details><summary>README extract</summary>

Slacker is a full-featured Python interface for the Slack API.

Example:
```python
from slacker import Slacker

slack = Slacker('<your-slack-api-token-goes-here>')

# Send a message to #general channel
slack.chat.post_message('#general', 'Hello fellow slackers!')

# Get users list
response = slack.users.list()
users = response.body['members']

# Upload a file
slack.files.upload('hello.txt')

# If you need to proxy the requests
...
```

Sections: Slacker, About, Examples, Documentation

</details>

### schemdraw

Electrical circuit schematic drawing

`pip install schemdraw` · installs (wheel) · licence: MIT · rank 6330 · last release 2026-05-29 · [PyPI](https://pypi.org/project/schemdraw/) · [docs](https://schemdraw.readthedocs.io) · [source](https://github.com/cdelker/schemdraw)

<details><summary>README extract</summary>

Schemdraw is a python package for producing high-quality electrical circuit schematic diagrams. Typical usage:

Included are symbols for basic electrical components (resistors, capacitors, diodes, transistors, etc.), opamps and signal processing elements. ...

Example:
```python
import schemdraw
import schemdraw.elements as elm
with schemdraw.Drawing(file='schematic.svg') as d:
    elm.Resistor().label('100KΩ')
    elm.Capacitor().down().label('0.1μF', loc='bottom')
    elm.Line().left()
    elm.Ground()
    elm.SourceV().up().label('10V')
```

</details>

### sagemaker-feature-store-pyspark-3.3

Amazon SageMaker FeatureStore PySpark Bindings

`pip install sagemaker-feature-store-pyspark-3.3` · installs from source (sdist only) · licence: Apache License 2.0 · rank 6332 · last release 2025-02-06 · [PyPI](https://pypi.org/project/sagemaker-feature-store-pyspark-3.3/)

<details><summary>README extract</summary>

Features:
SageMaker FeatureStore Spark is a connector library for Amazon SageMaker FeatureStore.

With this spark connector, you can easily ingest data to FeatureGroup's online and offline store from Spark `DataFrame`. ...

Sections: Overview, Getting Started

</details>

### slicerator

A lazy-loading, fancy-sliceable iterable.

`pip install slicerator` · installs (wheel) · licence: BSD · rank 6368 · last release 2022-04-07 · [PyPI](https://pypi.org/project/slicerator/)

<details><summary>README extract</summary>

a lazy-loading, fancy-slicable iterable

Think of it like a generator that is "reusable" and has a length.

Please see the documentation for examples and an API reference.

Installation

On any platform, use pip or conda.

`pip install slicerator`


`conda install -c conda-forge slicerator`

Example

Example:
```python
from slicerator import Slicerator

@Slicerator.from_class
class MyLazyLoader:
    def getitem(self, i):
        # this method will be wrapped by Slicerator, so that it accepts slices,
        # lists of integers, or boolean masks. Code below will only be executed
        # when an integer is used.

        # load thing number i
...
```

</details>

### simplepyble

Python bindings for the cross-platform SimpleBLE Bluetooth Low Energy library, for Windows, macOS, and Linux. Free for non-commercial use; commercial use requires a license.

`pip install simplepyble` · installs (wheel) · licence: BUSL-1.1 · rank 6376 · last release 2026-11-03 · [PyPI](https://pypi.org/project/simplepyble/)

<details><summary>README extract</summary>

Build Bluetooth once. Ship it everywhere.

SimplePyBLE brings SimpleBLE to Python
on Windows, macOS, and Linux. Discover and connect Bluetooth peripherals, read
and write GATT values, subscribe to notifications, and host local GATT services
through one API, with type hints and an asyncio module included.

Features:
- One cross-platform API: Keep your Bluetooth scripts, tools, and services the same on Windows, macOS, and Linux.
- Native underneath: Use WinRT, CoreBluetooth, and BlueZ through one maintained stack. ...

Example:
```python
import simplepyble

adapter = simplepyble.Adapter.get_adapters()[0]

adapter.set_callback_on_scan_found(
    lambda peripheral: print(f"{peripheral.identifier()} [{peripheral.address()}] {peripheral.rssi()} dBm")
)
adapter.scan_for(5000)
```

...

</details>

### shillelagh

Making it easy to query APIs via SQL

`pip install shillelagh` · installs (wheel) · licence: MIT License · rank 6392 · last release 2026-07-30 · [PyPI](https://pypi.org/project/shillelagh/) · [docs](https://shillelagh.readthedocs.io/)

<details><summary>README extract</summary>

Shillelagh (ʃɪˈleɪlɪ) is a Python library and CLI that allows you to query many resources (APIs, files, in memory objects) using SQL. It's both user and developer friendly, making it trivial to access resources and easy to add support for new ones.

Learn more on the documentation. ...

Features:
Sharks have been around for a long time. They're older than trees and the rings of Saturn, actually! The reason they haven't changed that much in hundreds of millions of years is because they're really good at what they do. ...

Example:
```python
from shillelagh.backends.apsw.db import connect

connection = connect(":memory:")
cursor = connection.cursor()

query = "SELECT * FROM a_table"
for row in cursor.execute(query):
    print(row)
```

...

</details>

### schemachange

A Database Change Management tool for Snowflake

`pip install schemachange` · installs (wheel) · licence: Apache Software License · rank 6396 · last release 2026-10-23 · [PyPI](https://pypi.org/project/schemachange/) · [source](https://github.com/Snowflake-Labs/schemachange)

<details><summary>README extract</summary>

*Looking for snowchange? You've found the right spot. snowchange has been renamed to schemachange.*

Features:
schemachange is a simple python based tool to manage all of your Snowflake objects. It
follows an Imperative-style approach to Database Change Management (DCM) and was inspired by
the Flyway database migration tool. ...

Example:
```python
Examples:
- `myorg-myaccount`
- `acme-production`

How to find your account identifier:
1. Log into Snowflake Web UI
2. Look at the URL or account locator in your profile
3. Or run: `SELECT CURRENT_ACCOUNT_NAME();` in Snowflake

Important: Do NOT include `snowflakecomputing.com` in the account identifier when configuring schemachange.

...
```

...

</details>

### slack-discovery-sdk

The Slack Discovery API SDK for Python

`pip install slack-discovery-sdk` · installs (wheel) · licence: not stated · rank 6404 · last release 2023-08-15 · [PyPI](https://pypi.org/project/slack-discovery-sdk/)

<details><summary>README extract</summary>

[][pypi-url]
[][pypi-url]

👋🏼 Welcome to the Python-Slack-Discovery-SDK! This project aims to make using the Slack Discovery APIs easier.

> 🚨 Note: This SDK is only accessible to customer developers with access to the Discovery API (Enterprise accounts) or partners who have been onboarded to the Security and Compliance partner program. ...

Example:
```python
from slack_discovery_sdk import DiscoveryClient
```

Sections: Python-Slack-Discovery-SDK, Prerequisites For Using the SDK, Using the SDK, 👨🏻‍💻 Understanding the Setup Script 👩🏻‍💻, 👨🏻‍💻 Adding Env Variables to Setup Script 👩🏻‍💻, 👩🏻‍💻 Run the Setup Script 👨🏻‍💻, Running the Examples, Considerations, Running tests, Feedback, Issues and Troubleshooting

</details>

### structlog-config

A comprehensive structlog configuration with sensible defaults for development and production environments, featuring context management, exception formatting, and path prettification.

`pip install structlog-config` · installs (wheel) · licence: not stated · rank 6450 · last release 2026-08-25 · [PyPI](https://pypi.org/project/structlog-config/) · [source](https://github.com/iloveitaly/structlog-config)

<details><summary>README extract</summary>

Logging is really important. Getting logging to work well in python feels like black magic: there's a ton of configuration
across structlog, warnings, std loggers, fastapi + celery context, JSON logging in production, etc that requires lots of
fiddling and testing to get working. ...

Features:
- Captures stdout, stderr, and exception tracebacks for failing tests
- Only creates output for failing tests by default (keeps directories clean)
- Separate files for each output type (stdout.txt, stderr.txt, exception.txt) ...

Example:
```python
from structlog_config import configure_logger

log = configure_logger()

log.info("the log", key="value")

# named logger just like stdlib
import structlog
custom_named_logger = structlog.get_logger(logger_name="test")
```

...

</details>

### simplejpeg

A simple package for fast JPEG encoding and decoding.

`pip install simplejpeg` · installs (wheel) · licence: MIT · rank 6476 · last release 2025-10-10 · [PyPI](https://pypi.org/project/simplejpeg/) · [docs](https://github.com/jfolz/simplejpeg/blob/master/README.rst) · [source](https://github.com/jfolz/simplejpeg)

<details><summary>README extract</summary>

This project is in no way affiliated with the
libjpeg-turbo
project.

simplejpeg is a simple package based on recent versions
of libturbojpeg for fast JPEG encoding and decoding.

Features:
Pillow and OpenCV are excellent options for handling JPEG
images and a variety of other formats.

If all you want is to read or write a couple of images and
don't worry about the details, this package is not for you. ...

Example:
```python
decode_jpeg_header(
    data: Any,
    min_height: SupportsInt=0,
    min_width: SupportsInt=0,
    min_factor: SupportsFloat=1,
    strict: bool=True,
) -> (SupportsInt, SupportsInt, Text, Text)
```

...

</details>

### sanitize-filename

A permissive filename sanitizer.

`pip install sanitize-filename` · installs (wheel) · licence: MIT License · rank 6479 · last release 2026-10-29 · [PyPI](https://pypi.org/project/sanitize-filename/)

<details><summary>README extract</summary>

A simple, dependency-free, blacklist-based filename sanitizer, for when you want to keep the original filename.

Note that a blacklist based sanitizer will _never_ be as safe as a whitelist based one. In most cases, your best option is to create a safe filename yourself. ...

Example:
```python
from sanitize_filename import sanitize

filename = input("Enter a file name:")
filename = sanitize(filename)
```

</details>

### sybil

Automated testing for the examples in your code and documentation.

`pip install sybil` · installs (wheel) · licence: MIT License · rank 6480 · last release 2026-06-13 · [PyPI](https://pypi.org/project/sybil/) · [docs](https://sybil.readthedocs.org/en/latest/) · [source](https://github.com/simplistix/sybil)

<details><summary>README extract</summary>

This library provides a way to check examples in your code and documentation by parsing
them from their source and evaluating the parsed examples as part of
your normal test run. Integration is provided for the main Python test
runners.

The documentation is the best place to start.

</details>

### samplomatic

Serving all of your circuit sampling needs since 2025.

`pip install samplomatic` · installs (wheel) · licence: Apache-2.0 · rank 6585 · last release 2026-08-25 · [PyPI](https://pypi.org/project/samplomatic/)

<details><summary>README extract</summary>

_Serving all of your circuit sampling needs since 2025._

> [!NOTE]
> This library is in a beta stage of development where things are changing fast and in breaking ways.
> Although each version of this library is well-tested, while the major version is `0`, please expect breaking changes between minor versions and pin your dependencies ...

Example:
```python
from samplomatic import build, Twirl
from qiskit.circuit import QuantumCircuit, Parameter
import numpy as np

circuit = QuantumCircuit(5)

with circuit.box([Twirl()]):
    # twirled boxes are always "dressed": putting your single-qubit gates into
    # the boxes will result in them being composed into the "dressing" layer
...
```

Sections: Documentation, Hello World, Citing this package

</details>

### scrapeops-scrapy-proxy-sdk

Scrapeops Scrapy Proxy SDK, simple integration to use the Scrapeops Proxy API with your Scrapy Spiders.

`pip install scrapeops-scrapy-proxy-sdk` · installs from source (sdist only) · licence: BSD License · rank 6602 · last release 2026-06-25 · [PyPI](https://pypi.org/project/scrapeops-scrapy-proxy-sdk/)

<details><summary>README extract</summary>

Scrapeops Scrapy Proxy SDK, simple integration to use the Scrapeops Proxy API with your Scrapy Spiders.

</details>

### sccache

Sccache is a ccache-like tool. It is used as a compiler wrapper and avoids compilation when possible. Sccache has the capability to utilize caching in remote storage environments, including various cloud storage options, or alternatively, in local storage.

`pip install sccache` · installs (wheel) · licence: Apache-2.0 · rank 6626 · last release 2026-06-22 · [PyPI](https://pypi.org/project/sccache/) · [source](https://github.com/mozilla/sccache/)

<details><summary>README extract</summary>

sccache is a ccache-like compiler caching tool. It is used as a compiler wrapper and avoids compilation when possible, storing cached results either on local disk or in one of several cloud storage backends. Multi-level caching with automatic backfill is supported for hierarchical cache architectures (see Multi-Level Cache). ...

Sections: sccache - Shared Compilation Cache, macOS, Windows, Via cargo, With Nix, Building portable binaries, Linux, General, Rust, C++20 Modules, User Agent

</details>

### smmap2

A mirror package for smmap

`pip install smmap2` · installs (wheel) · licence: not stated · rank 6690 · last release 2020-02-23 · [PyPI](https://pypi.org/project/smmap2/)

<details><summary>README extract</summary>

This is a mirror package for `smmap < Consider installing it directly instead.

</details>

### static-ffmpeg

Cross platform ffmpeg to work on various systems.

`pip install static-ffmpeg` · installs (wheel) · licence: MIT License · rank 6724 · last release 2026-01-16 · [PyPI](https://pypi.org/project/static-ffmpeg/)

<details><summary>README extract</summary>

The easiest way to get ffmpeg v8 installed through python.

Example:
```python
import static_ffmpeg
# ffmpeg installed on first call to add_paths(), threadsafe.
static_ffmpeg.add_paths()  # blocks until files are downloaded
# or static_ffmpeg.add_paths(weak=True) to only add if ffmpeg/ffprobe not already on path
# Now ffmpeg and ffprobe will use static_ffmpeg versions.
os.system("ffmpeg -i myfile.mp4 ...")
```

Sections: static-ffmpeg, Usage, About, Without this library..., Api, Virtual Environment (optional), Binary source, Version

</details>

### stackprinter

Debug-friendly stack traces, with variable values and semantic highlighting

`pip install stackprinter` · installs (wheel) · licence: MIT License · rank 6751 · last release 2026-04-17 · [PyPI](https://pypi.org/project/stackprinter/)

<details><summary>README extract</summary>

This is a more helpful version of Python's built-in exception message: It shows more code context and the current values of nearby variables. That answers many of the questions I'd ask an interactive debugger: Where in the code was the crash, what's in the relevant variables, and why was _that_ function called with _those_ arguments. ...

Example:
```python
Traceback (most recent call last):
  File "demo.py", line 12, in
    dangerous_function(somelist + anotherlist)
  File "demo.py", line 6, in dangerous_function
    return sorted(blub, key=lambda xs: sum(xs))
  File "demo.py", line 6, in
    return sorted(blub, key=lambda xs: sum(xs))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

...

</details>

### shiny

A web development framework for Python.

`pip install shiny` · installs (wheel) · licence: MIT · rank 6785 · last release 2026-10-29 · [PyPI](https://pypi.org/project/shiny/) · [docs](https://shiny.posit.co/py/) · [source](https://github.com/posit-dev/py-shiny)

<details><summary>README extract</summary>

Shiny for Python is the best way to build fast, beautiful web applications in Python. You can build quickly with Shiny and create simple interactive visualizations and prototype applications in an afternoon. But unlike other frameworks targeted at data scientists, Shiny does not limit your app's growth. ...

Sections: Shiny for Python, Join the conversation, Getting started, Agent Skills

</details>

### snakemake-interface-common

Common functions and classes for Snakemake and its plugins

`pip install snakemake-interface-common` · installs (wheel) · licence: not stated · rank 6823 · last release 2026-11-06 · [PyPI](https://pypi.org/project/snakemake-interface-common/)

<details><summary>README extract</summary>

Common functions and classes for Snakemake and its plugins.

</details>

### secure-smtplib

Secure SMTP subclasses for Python 2

`pip install secure-smtplib` · installs (wheel) · licence: UNKNOWN · rank 6829 · last release 2015-04-07 · [PyPI](https://pypi.org/project/secure-smtplib/)

<details><summary>README extract</summary>

Secure SMTP subclasses for Python 2

- First version of secure-smtplib that can be installed from PyPI

Sections: secure-smtplib, Changes, 0.1.0 (2015-04-07)

</details>

### sphinx-togglebutton

Toggle page content and collapse admonitions in Sphinx.

`pip install sphinx-togglebutton` · installs (wheel) · licence: MIT License · rank 6847 · last release 2026-03-27 · [PyPI](https://pypi.org/project/sphinx-togglebutton/)

<details><summary>README extract</summary>

A small sphinx extension to make it possible to add a "toggle button" to
sections of your page. This allows you to:

- Collapse Sphinx admonitions (notes, warnings, etc) so that their content is hidden
 until users click a toggle button.
- Collapse arbitrary chunks of content on your page with a `collapse` directive.

Sections: sphinx-togglebutton, Usage, Internationalization (i18n)

</details>

### spotipy

A light weight Python library for the Spotify Web API

`pip install spotipy` · installs (wheel) · licence: MIT · rank 6855 · last release 2026-03-03 · [PyPI](https://pypi.org/project/spotipy/) · [source](https://github.com/plamere/spotipy)

<details><summary>README extract</summary>

Features:
Spotipy supports all of the features of the Spotify Web API including access to all end points, and support for user authorization. For details on the capabilities you are encouraged to review the Spotify Web API documentation.

Example:
```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results'tracks'):
...
```

Sections: Spotipy, Features, Quick Start, Example without user authentication, Example with user authentication, Reporting Issues

</details>

### simhash

A Python implementation of Simhash Algorithm

`pip install simhash` · installs (wheel) · licence: MIT License · rank 6873 · last release 2022-03-03 · [PyPI](https://pypi.org/project/simhash/) · [source](https://github.com/1e0ng/simhash)

### sensai-utils

Utilities from sensAI, the Python library for sensible AI

`pip install sensai-utils` · installs (wheel) · licence: MIT License · rank 6899 · last release 2025-10-20 · [PyPI](https://pypi.org/project/sensai-utils/)

### snakemake-interface-storage-plugins

This package provides a stable interface for interactions between Snakemake and its storage plugins.

`pip install snakemake-interface-storage-plugins` · installs (wheel) · licence: not stated · rank 6903 · last release 2026-03-16 · [PyPI](https://pypi.org/project/snakemake-interface-storage-plugins/)

<details><summary>README extract</summary>

This package provides a stable interface for interactions between Snakemake and its storage plugins.

Plugins should implement the following skeleton to comply with this interface.
It is recommended to use Snakedeploy to set up the skeleton (and automated testing) within a python package.

Example:
```python
from dataclasses import dataclass, field
from typing import Any, Iterable, Optional, List
from snakemake_interface_storage_plugins.settings import StorageProviderSettingsBase
from snakemake_interface_storage_plugins.storage_provider import (
    StorageProviderBase,
    StorageQueryValidationResult,
    ExampleQuery,
    Operation,
)
...
```

</details>

### semantic-kernel

Semantic Kernel Python SDK

`pip install semantic-kernel` · installs (wheel) · licence: MIT License · rank 6907 · last release 2026-11-05 · [PyPI](https://pypi.org/project/semantic-kernel/) · [source](https://github.com/microsoft/semantic-kernel/tree/main/python)

<details><summary>README extract</summary>

> [!IMPORTANT]
> Semantic Kernel is now Microsoft Agent Framework! Microsoft Agent Framework (MAF) is the enterprise‑ready successor to Semantic Kernel. Microsoft Agent Framework is now available at version 1.0 as a production-ready release: stable APIs, and a commitment to long-term support. ...

Example:
```python
chat_service = AzureChatCompletion(
    api_key=...,
    endpoint=...,
    deployment_name=...,
    api_version=...,
)
```

Sections: Get Started with Semantic Kernel Python, 1. Setup API Keys, 2. Use the Kernel for Prompt Engineering, 3. Directly Use AI Services (No Kernel Required), 4. Build an Agent with Plugins and Tools, 5. Multi-Agent Orchestration, More Examples & Notebooks, Semantic Kernel Documentation

</details>

### semantic-text-splitter

Split text into semantic chunks, up to a desired chunk size. Supports calculating length by characters and tokens, and is callable from Rust and Python.

`pip install semantic-text-splitter` · installs (wheel) · licence: MIT · rank 6938 · last release 2026-10-25 · [PyPI](https://pypi.org/project/semantic-text-splitter/) · [source](https://github.com/benbrandt/text-splitter)

<details><summary>README extract</summary>

Large language models (LLMs) can be used for many tasks, but often have a limited context size that can be smaller than documents you might want to use. To use documents of larger length, you often have to split your text into chunks to fit within this context size. ...

Example:
```python
from semantic_text_splitter import TextSplitter

# Maximum number of characters in a chunk
max_characters = 1000
# Optionally can also have the splitter not trim whitespace for you
splitter = TextSplitter(max_characters)
# splitter = TextSplitter(max_characters, trim=False)

chunks = splitter.chunks("your document text")
```

...

</details>

### seedir

Package for creating, editing, and reading folder tree diagrams.

`pip install seedir` · installs (wheel) · licence: MIT · rank 6950 · last release 2025-06-04 · [PyPI](https://pypi.org/project/seedir/)

<details><summary>README extract</summary>

A Python package for creating, editing, and reading folder tree diagrams.

*Photo by Adam Kring.*

Example:
```python
>>> import seedir as sd
>>> sd.seedir(style='lines', itemlimit=10, depthlimit=2, exclude_folders='.git')
seedir/
├─.gitattributes
├─.gitignore
├─.ipynb_checkpoints/
│ └─examples-checkpoint.ipynb
├─build/
│ ├─bdist.win-amd64/
│ └─lib/
├─CHANGELOG.md
├─dist/
│ └─seedir-0.1.4-py3-none-any.whl
├─docs/
│ ├─exampledir/
│ ├─gettingstarted.md
│ ├─seedir/
...
```

Sections: seedir, Usage

</details>

### simplesat

Prototype for SAT-based dependency handling. This is a work in progress, do not expect any API not to change at this point.

`pip install simplesat` · installs (wheel) · licence: BSD-3-Clause · rank 7012 · last release 2025-04-03 · [PyPI](https://pypi.org/project/simplesat/)

<details><summary>README extract</summary>

Prototype for SAT-based dependency handling. This is a work in progress,
do not expect any API not to change at this point.

Features:
* new upgrade job kind, to update every installed package to the latest (#253)
* new solver method solve_with_hint for a more human-readable message for
 unsatisfiable problems (#254)

Sections: Example usage, Usage from the CLI, Comparing with php's composer, Bibliography, Version 0.9.2, Version 0.9.1, Version 0.9.0, Version 0.8.2, Internals, Version 0.8.1, Bug fixes, Version 0.8.0, Features

</details>

### sprites-py

Python SDK for Fly.io Sprites: computers for agents. Sprite management, remote command execution, filesystems, checkpoints, services, and network policy from Python.

`pip install sprites-py` · installs (wheel) · licence: MIT · rank 7014 · last release 2026-10-06 · [PyPI](https://pypi.org/project/sprites-py/) · [docs](https://fly.io/sprites/) · [source](https://github.com/superfly/sprites-py)

<details><summary>README extract</summary>

Python SDK for Sprites, providing sprite management,
remote command execution, filesystem access, checkpoints, services, and network
policy controls.

Example:
```python
import os

from sprites import SpritesClient

client = SpritesClient(token=os.environ["SPRITE_TOKEN"])
sprite = client.create_sprite(os.environ["SPRITE_NAME"])

# Run a command
result = sprite.run("echo", "hello", capture_output=True)
print(result.stdout.decode())  # "hello\n"

# Or use the Go-style API
cmd = sprite.command("ls", "-la")
...
```

Sections: Sprites Python SDK, Quick Start, API Overview, Async API, SpritesClient, Sprite, Filesystem, Checkpoints, Services, Network Policy, Client signals, Integrations, Requirements

</details>

### spark-expectations

This project helps us to run Data Quality Rules in flight while spark job is being run

`pip install spark-expectations` · does not install on CPython 3.14 · licence: not stated · rank 7026 · last release 2026-06-27 · [PyPI](https://pypi.org/project/spark-expectations/)

<details><summary>README extract</summary>

Spark Expectations is a specialized tool designed with the primary goal of maintaining data integrity within your processing pipeline.
By identifying and preventing malformed or incorrect data from reaching the target destination, it ensues that only quality data is
passed through. ...

Features:
Please find the spark-expectations flow and feature diagrams below

Example:
```python
from spark_expectations.config.user_config import Constants as user_config

se_user_conf = {
    user_config.se_notifications_enable_email: False,
    user_config.se_notifications_email_smtp_host: "mailhost.nike.com",
    user_config.se_notifications_email_smtp_port: 25,
    user_config.se_enable_obs_dq_report_result: True,
...
```

...

</details>

### streamlit-option-menu

streamlit-option-menu is a simple Streamlit component that allows users to select a single item from a list of options in a menu.

`pip install streamlit-option-menu` · installs (wheel) · licence: not stated · rank 7043 · last release 2024-10-09 · [PyPI](https://pypi.org/project/streamlit-option-menu/)

<details><summary>README extract</summary>

streamlit-option-menu is a simple Streamlit component that allows users to select a single item from a list of options in a menu.
It is similar in function to st.selectbox(), except that:
- It uses a simple static list to display the options instead of a dropdown
- It has configurable icons for each option item and the menu title ...

Example:
```python
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'],
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected

# horizontal Menu
selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
...
```

Sections: Parameters, Example

</details>

### security

The security toolkit for the Python community

`pip install security` · installs (wheel) · licence: not stated · rank 7088 · last release 2024-06-28 · [PyPI](https://pypi.org/project/security/) · [source](https://github.com/pixee/python-security)

### spsdk-mcu-link

SPSDK MCU-Link. A debugger probe plugin for SPSDK supporting LPC-Link/MCU-Link from NXP.

`pip install spsdk-mcu-link` · installs (wheel) · licence: BSD License · rank 7120 · last release 2026-10-13 · [PyPI](https://pypi.org/project/spsdk-mcu-link/)

<details><summary>README extract</summary>

SPSDK MCU-Link
 ==============

 NXP SPSDK MCU-Link debug probe support plugin for NXP LPC-Link/MCU-Link hardware debug probes. This plugin enables seamless integration with NXP's debug hardware.

 * Free software: BSD-3-Clause

 Features ...

</details>

### splinter

browser abstraction for web acceptance testing

`pip install splinter` · installs (wheel) · licence: BSD License · rank 7146 · last release 2024-01-16 · [PyPI](https://pypi.org/project/splinter/) · [docs](https://splinter.readthedocs.io/) · [source](https://github.com/cobrateam/splinter/)

<details><summary>README extract</summary>

Splinter is a Python framework that provides a simple and consistent interface for web application automation.

* Documentation

* Changelog

Key features:

- Easy to learn: The API is designed to be intuitive and quick to pick up.
- Faster to code: Automate browser interactions quickly and reliably without fighting the tool. ...

Example:
```python
from splinter import Browser

browser = Browser('firefox')
browser.visit('
browser.find_by_name('q').fill('splinter - python acceptance testing for web applications')
browser.find_by_name('btnK').click()

if browser.is_text_present('splinter.readthedocs.io'):
    print("Yes, the official website was found!")
else:
...
```

Sections: splinter, Example, Getting Started, Pytest Plugins, Page Objects

</details>

### sparse-dot-topn

This package boosts a sparse matrix multiplication followed by selecting the top-n multiplication

`pip install sparse-dot-topn` · installs (wheel) · licence: Apache Software License · rank 7193 · last release 2025-12-16 · [PyPI](https://pypi.org/project/sparse-dot-topn/)

<details><summary>README extract</summary>

sparse\_dot\_topn provides a fast way to performing a sparse matrix multiplication followed by top-n multiplication result selection.

Comparing very large feature vectors and picking the best matches, in practice often results in performing a sparse matrix multiplication followed by selecting the top-n multiplication results. ...

Example:
```python
import scipy.sparse as sparse
from sparse_dot_topn import sp_matmul, sp_matmul_topn

A = sparse.random(1000, 100, density=0.1, format="csr")
B = sparse.random(100, 2000, density=0.1, format="csr")

# Compute C and retain the top 10 values per row
C = sp_matmul_topn(A, B, top_n=10)

# or paralleslised matrix multiplication without top-n selection
...
```

...

</details>

### streamsets

A Python SDK for StreamSets

`pip install streamsets` · installs (wheel) · licence: not stated · rank 7204 · last release 2026-06-29 · [PyPI](https://pypi.org/project/streamsets/)

<details><summary>README extract</summary>

The StreamSets SDK allows users to interact with StreamSets products programmatically using Python, including Control Hub, Data Collector, Transformer, and Transformer for Snowflake.

Versions 4.0.0 and higher of the StreamSets SDK for Python support the StreamSets Platform.
Versions below 4.0.0 support our Legacy products. ...

Sections: StreamSets SDK for Python, Notices, Documentation, More Resources, Getting Help

</details>

### streamlit-pdf-viewer

Streamlit component for PDF visualisation and manipulation

`pip install streamlit-pdf-viewer` · installs (wheel) · licence: not stated · rank 7206 · last release 2026-07-20 · [PyPI](https://pypi.org/project/streamlit-pdf-viewer/)

<details><summary>README extract</summary>

Streamlit component that allows the visualisation and enrichment of PDF documents.
You can see an application in
action here.

Features:
- Show PDF files in a Streamlit application with a simple command
- Based on the pdf.js library
- Visualize annotations on top of the PDF documents
- Render text on top of the PDF document, allowing copy-paste ...

Example:
```python
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

pdf_viewer("str, path or bytes")
```

Sections: streamlit-pdf-viewer, Features, Limitations, Caveats, Streamlit compatibility, 107 for details and the bisect, Getting started, Params, Annotation format, Custom callback for clicking on annotations, Environment, Integrate into a streamlit application

</details>

### sepaxml

Python SEPA XML implementations

`pip install sepaxml` · installs (wheel) · licence: MIT License · rank 7208 · last release 2025-09-02 · [PyPI](https://pypi.org/project/sepaxml/)

<details><summary>README extract</summary>

This is a python implementation to generate SEPA XML files.

Supported standards:

* SEPA PAIN.001.001.03
* SEPA PAIN.001.001.09
* SEPA PAIN.001.001.10
* SEPA PAIN.001.001.11
* SEPA PAIN.008.001.02
* SEPA PAIN.008.001.08
* SEPA PAIN.008.001.09
* SEPA PAIN.008.001.10

Example:
```python
from sepaxml import SepaDD
import datetime, uuid

config = {
    "name": "Test von Testenstein",
    "IBAN": "NL50BANK1234567890",
    "BIC": "BANKNL2A",
    "batch": True,
    "creditor_id": "DE26ZZZ00000000000",  # supplied by your bank or financial authority
    "currency": "EUR",  # ISO 4217
...
```

Sections: SEPA XML Generator, Limitations, Usage, Direct debit, Credit transfer

</details>

### streamlit-javascript

component to run javascript code in streamlit application

`pip install streamlit-javascript` · installs (wheel) · licence: MIT License · rank 7251 · last release 2022-05-13 · [PyPI](https://pypi.org/project/streamlit-javascript/)

<details><summary>README extract</summary>

[][github_link] [][pypi_link]

Sections: Streamlit javascript execution, Getting started, Demo

</details>

### streamlit-agraph

Interactive Graph Vis for Streamlit.

`pip install streamlit-agraph` · installs (wheel) · licence: not stated · rank 7257 · last release 2023-01-28 · [PyPI](https://pypi.org/project/streamlit-agraph/)

<details><summary>README extract</summary>

Based on react-graph-vis

Example:
```python
import streamlit
from streamlit_agraph import agraph, Node, Edge, Config

nodes = []
edges = []
nodes.append( Node(id="Spiderman",
                   label="Peter Parker",
                   size=25,
                   shape="circularImage",
                   image="
            ) # includes **kwargs
nodes.append( Node(id="Captain_Marvel",
...
```

Sections: Example App, Basic Usage, Config Bilder, TripleStore

</details>

### sanic-ext

Extend your Sanic installation with some core functionality.

`pip install sanic-ext` · installs (wheel) · licence: MIT License · rank 7276 · last release 2026-01-20 · [PyPI](https://pypi.org/project/sanic-ext/)

<details><summary>README extract</summary>

Sanic strives to be "Unopinionated and flexible":
But what happens when you want all the goodies? Sanic Extensions is an officially supported Sanic plugin to provide application developers with additional tools and features.

Features:
- Auto create HEAD, OPTIONS, and TRACE endpoints
- CORS protection
- Predefined, endpoint-specific response serializers
- Argument injection into route handlers
- OpenAPI documentation with Redoc and/or Swagger ...

Example:
```python
from sanic import Sanic

app = Sanic("MyHelloWorldApp")
```

Sections: Sanic Extensions, Features, Getting started, Learn more

</details>

### speedtest-cli

Command line interface for testing internet bandwidth using speedtest.net

`pip install speedtest-cli` · installs (wheel) · licence: Apache Software License · rank 7330 · last release 2021-04-08 · [PyPI](https://pypi.org/project/speedtest-cli/)

<details><summary>README extract</summary>

Command line interface for testing internet bandwidth using
speedtest.net

speedtest-cli works with Python 2.4-3.7

Sections: speedtest-cli, Versions, Github, Just download (Like the way it used to be), Usage, Python API, Inconsistency

</details>

### scc-firewall-manager-sdk

Cisco Security Cloud Control Firewall Manager API

`pip install scc-firewall-manager-sdk` · installs (wheel) · licence: not stated · rank 7336 · last release 2026-11-07 · [PyPI](https://pypi.org/project/scc-firewall-manager-sdk/) · [docs](https://scc-firewall-manager-sdk.readthedocs.io/)

<details><summary>README extract</summary>

Use the documentation to explore the endpoints Security Cloud Control Firewall Manager has to offer

</details>

### sseclient

Python client library for reading Server Sent Event streams.

`pip install sseclient` · installs from source (sdist only) · licence: MIT License · rank 7401 · last release 2020-09-25 · [PyPI](https://pypi.org/project/sseclient/)

<details><summary>README extract</summary>

This is a Python client library for iterating over http Server Sent Event (SSE)
streams (also known as EventSource, after the name of the Javascript interface
inside browsers). The SSEClient class accepts a url on init, and is then an
iterator over messages coming from the server.

Example:
```python
from sseclient import SSEClient

messages = SSEClient('
for msg in messages:
    do_something_useful(msg)
```

Sections: Python SSE Client, Usage, Additional Resources

</details>

### spsdk-pyocd

PyOCD SW Debugger. A debugger probe plugin for SPSDK.

`pip install spsdk-pyocd` · installs (wheel) · licence: BSD License · rank 7434 · last release 2026-10-13 · [PyPI](https://pypi.org/project/spsdk-pyocd/)

<details><summary>README extract</summary>

* Free software: BSD-3-Clause

Features

* Allow SPSDK to use PyOCD as an interface for debugger probes.

Installation

* Activate virtual env, where you have SPSDK
 - to install spsdk run: `pip install spsdk`
* Install the package
 - `pip install spsdk-pyocd`
* If you want to use P&E Micro debugger probes install the `pemicro` extra
 - `pip ...

</details>

### sanic-testing

Core testing clients for Sanic

`pip install sanic-testing` · installs (wheel) · licence: MIT License · rank 7451 · last release 2024-06-30 · [PyPI](https://pypi.org/project/sanic-testing/)

<details><summary>README extract</summary>

This package is meant to be the core testing utility and clients for testing Sanic applications. It is mainly derived from `sanic.testing` which has (or will be) removed from the main Sanic repository in the future.

Documentation

Example:
```python
from sanic import Sanic
from sanic_testing import TestManager

sanic_app = Sanic(name)
TestManager(sanic_app)
```

Sections: Sanic Core Test, Getting Started, Writing a sync test, Writing an async test

</details>

### sagemaker-inference

Open source toolkit for helping create serving containers to run on Amazon SageMaker.

`pip install sagemaker-inference` · installs from source (sdist only) · licence: Apache Software License · rank 7509 · last release 2023-10-25 · [PyPI](https://pypi.org/project/sagemaker-inference/)

<details><summary>README extract</summary>

Serve machine learning models within a Docker container using Amazon
SageMaker.

Amazon SageMaker is a fully managed service for data science and machine learning (ML) workflows.
You can use Amazon SageMaker to simplify the process of building, training, and deploying ML models. ...

Example:
```python
from sagemaker_inference import content_types, decoder, default_inference_handler, encoder, errors

class DefaultPytorchInferenceHandler(default_inference_handler.DefaultInferenceHandler):

    def default_model_fn(self, model_dir, context=None):
        """Loads a model. For PyTorch, a default function to load a model cannot be provided.
...
```

Sections: SageMaker Inference Toolkit, books: Background, computer: Usage, Implementation Steps, Complete Example

</details>

### snowflake-code-unit-registry

SCAI state management library for database migrations

`pip install snowflake-code-unit-registry` · installs (wheel) · licence: Apache Software License · rank 7529 · last release 2026-11-03 · [PyPI](https://pypi.org/project/snowflake-code-unit-registry/)

<details><summary>README extract</summary>

SCAI state management library for database migrations.

Example:
```python
from scai_state import CodeUnitRegistry
from scai_state.types import CodeUnit, SourceMetadata, TargetMetadata, ObjectType, Kind

# Initialize a new registry
registry = CodeUnitRegistry.init("/path/to/repo")

# Or open an existing registry
registry = CodeUnitRegistry.open("/path/to/existing/repo")

# Create a code unit
code_unit = CodeUnit(
...
```

Sections: scai-state, Usage, Building from Source

</details>

### semantic-router

Super fast semantic router for AI decision making

`pip install semantic-router` · does not install on CPython 3.14 · licence: MIT · rank 7545 · last release 2026-10-22 · [PyPI](https://pypi.org/project/semantic-router/)

<details><summary>README extract</summary>

Semantic Router is a superfast decision-making layer for your LLMs and agents. Rather than waiting for slow LLM generations to make tool-use decisions, it decides in milliseconds: it compares the _semantic_ meaning of a request against your routes in vector space, or asks a small decision model in a single fast call. ...

Example:
```python
from semantic_router import Route

# we could use this as a guide for our chatbot to avoid political conversations
politics = Route(
    name="politics",
    utterances=[
        "isn't politics the best thing ever",
        "why don't you tell me about your political opinions",
        "don't you just love the president",
...
```

Sections: Read the Docs, Versions, Quickstart

</details>

### streamingjson

A streamlined, user-friendly JSON streaming preprocessor, crafted in Python.

`pip install streamingjson` · installs (wheel) · licence: MIT License · rank 7583 · last release 2024-09-20 · [PyPI](https://pypi.org/project/streamingjson/)

<details><summary>README extract</summary>

Welcome to streaming-json-py, a groundbreaking library designed to revolutionize the way we handle stream JSON parsing.

In an era dominated by LLMs (Large Language Models), the ability to efficiently parse JSON streams is more critical than ever. ...

Features:
- Real-Time JSON Parsing: With streaming-json-py, you no longer need to wait for the entire JSON data to be generated. This library allows for the parsing of JSON as it is being streamed (this means JSON stream can stops at any position), ...

Example:
```python
# init, @NOTE: We need to assign a new lexer for each JSON stream.
lexer = streamingjson.Lexer()

# append your JSON segment
lexer.append_string('{"a":')

# complete the JSON
print(lexer.complete_json()) # will print `{"a":null}`

# append more JSON segment
...

</details>

### scipy-openblas32

Provides OpenBLAS for python packaging

`pip install scipy-openblas32` · installs (wheel) · licence: BSD License · rank 7598 · last release 2026-11-02 · [PyPI](https://pypi.org/project/scipy-openblas32/)

<details><summary>README extract</summary>

1. The primary purposes of the scipy-openblas32 and scipy-openblas64 wheels are:
 - (a) to use them as build and runtime dependencies in CI and local development for NumPy and SciPy
 - (b) to be vendored into NumPy and SciPy wheels
 - (c) possibly, in the future, being used as runtime dependencies for NumPy
 and/or SciPy.
2. ...

Sections: Wheels containing OpenBLAS, OpenBLAS library build process, Buildtime, Runtime

</details>

### sentry-cli

A command line utility to work with Sentry.

`pip install sentry-cli` · installs (wheel) · licence: FSL-1.1-MIT · rank 7600 · last release 2026-10-22 · [PyPI](https://pypi.org/project/sentry-cli/)

<details><summary>README extract</summary>

> [!IMPORTANT]
> This repository is no longer under active development, as our new CLI will soon be replacing this one.
> We are therefore no longer accepting feature requests for this repo. Also, we will generally only fix bugs in this repo when there is a concrete reason preventing adoption of the new CLI. ...

Sections: Sentry CLI, Compatibility, Self-Hosted Sentry, Versioning, Compiling, Internal docs

</details>

### socketdev

Socket Security Python SDK

`pip install socketdev` · installs (wheel) · licence: not stated · rank 7603 · last release 2026-11-03 · [PyPI](https://pypi.org/project/socketdev/)

<details><summary>README extract</summary>

Example:
```python
from socketdev import socketdev
socket = socketdev(token="REPLACE_ME", timeout=30)
```

Sections: socketdev, Purpose, Initializing the module, export.cdx_bom(org_slug, id, query_params), export.spdx_bom(org_slug, id, query_params), export.openvex_bom(org_slug, id, query_params), fullscans.get(org_slug, params), fullscans.post(files, params), fullscans.delete(org_slug, full_scan_id), fullscans.stream(org_slug, full_scan_id, use_types=False), fullscans.metadata(org_slug, full_scan_id, use_types=False), fullscans.gfm(org_slug, before, after), basics.get_config(org_slug, use_types), dependencies.get(limit, offset)

</details>

### streamlit-folium

Render Folium objects in Streamlit

`pip install streamlit-folium` · installs (wheel) · licence: not stated · rank 7605 · last release 2026-08-03 · [PyPI](https://pypi.org/project/streamlit-folium/)

<details><summary>README extract</summary>

streamlit-folium integrates two great open-source projects in the Python ecosystem: Streamlit and Folium!

Sections: streamlit-folium: geospatial made easy in Streamlit!, Usage, Example

</details>

### stac-pydantic

Pydantic data models for the STAC spec

`pip install stac-pydantic` · installs (wheel) · licence: MIT License · rank 7676 · last release 2026-11-03 · [PyPI](https://pypi.org/project/stac-pydantic/) · [source](https://github.com/stac-utils/stac-pydantic.git)

<details><summary>README extract</summary>

Pydantic models for STAC Catalogs, Collections, Items, and the STAC API spec.
Initially developed by arturo-ai.

The main purpose of this library is to provide reusable request/response models for tools such as fastapi.
For more comprehensive schema validation and robust extension support, use pystac.

Example:
```python
from stac_pydantic import Catalog

stac_catalog = {
  "type": "Catalog",
  "stac_version": "1.0.0",
  "id": "sample",
  "description": "This is a very basic sample catalog.",
  "links": [
    {
      "href": "item.json",
      "rel": "item"
    }
  ]
}

catalog = Catalog(**stac_catalog)
assert catalog.id == "sample"
...
```

Sections: stac-pydantic, Usage, Loading Models, Extensions, Vendor Extensions, STAC API, Exporting Models, Required keys, CLI

</details>

### strands-agents-evals

Evaluation framework for Strands

`pip install strands-agents-evals` · installs (wheel) · licence: Apache-2.0 · rank 7708 · last release 2026-11-04 · [PyPI](https://pypi.org/project/strands-agents-evals/)

<details><summary>README extract</summary>

Documentation
 ◆ Samples
 ◆ CLI
 ◆ MCP Server

 Harness (Python, TypeScript)
 ◆ SDK (Python, TypeScript)
 ◆ Box
 ◆ Shell
 ◆ Evals
 ◆ Labs

Strands Evaluation is a powerful framework for evaluating AI agents and LLM applications. ...

Features:
- Multiple Evaluation Types: Output evaluation, trajectory analysis, tool usage assessment, and interaction evaluation
- Multimodal Evaluation: MLLM-as-a-Judge evaluators for image-to-text tasks with built-in rubrics ...

Example:
```python
from strands import Agent
from strands_evals import Case, Experiment
from strands_evals.evaluators import OutputEvaluator

# Create test cases
test_cases =
    Case[str, str
]

# Create evaluators with custom rubric
evaluators = [
    OutputEvaluator(
        rubric="""
        Evaluate based on:
...

</details>

### shiv

A command line utility for building fully self contained Python zipapps.

`pip install shiv` · installs (wheel) · licence: BSD License · rank 7727 · last release 2024-11-01 · [PyPI](https://pypi.org/project/shiv/)

<details><summary>README extract</summary>

shiv is a command line utility for building fully self-contained Python zipapps as outlined in PEP 441, but with all their dependencies included!

shiv's primary goal is making distributing Python applications fast & easy.

📗 Full documentation can be found here.

- python3.8+
- linux/osx/windows

Sections: shiv, sys requirements, quickstart, simple cli example, gotchas

</details>

### sanic-jwt

JWT oauth flow for Sanic

`pip install sanic-jwt` · installs (wheel) · licence: MIT License · rank 7732 · last release 2022-06-28 · [PyPI](https://pypi.org/project/sanic-jwt/)

<details><summary>README extract</summary>

Sanic JWT adds authentication protection and endpoints to [Sanic].

It is both easy to get up and running, and extensible for the
developer. It can act to protect endpoints and also provide authentication scoping, all wrapped into a nice [JWT].

Read the documentation | View the source code

What do I do? ...

Example:
```python
from sanic import Sanic
from sanic_jwt import Initialize

def my_authenticate(request, *args, **kwargs):
    ...

app = Sanic()
Initialize(
    app,
    authenticate=my_authenticate
)
```

</details>

### slipcover

Near Zero-Overhead Python Code Coverage

`pip install slipcover` · installs (wheel) · licence: Apache Software License · rank 7749 · last release 2026-08-13 · [PyPI](https://pypi.org/project/slipcover/) · [source](https://github.com/plasma-umass/slipcover)

<details><summary>README extract</summary>

by Juan Altmayer Pizzorno and Emery Berger
at UMass Amherst's PLASMA lab.

SlipCover is a fast code coverage tool.
It tracks a Python program as it runs and reports on the parts that executed and
those that didn't.
That can help guide your testing (showing code that isn't being tested), debugging,
fuzzing or to find "dead" code. ...

Sections: SlipCover: Near Zero-Overhead Python Code Coverage, About Slipcover, How it works, Performance, Accuracy, Getting started, Using it with a test harness, Configuration via `pyproject.toml`, Usage example, Command-line options, Platforms, Technical Information

</details>

### sagemaker-training

Open source library for creating containers to run on Amazon SageMaker.

`pip install sagemaker-training` · installs from source (sdist only) · licence: Apache Software License · rank 7779 · last release 2026-10-23 · [PyPI](https://pypi.org/project/sagemaker-training/)

<details><summary>README extract</summary>

Train machine learning models within a Docker container using Amazon SageMaker.

Amazon SageMaker is a fully managed service for data science and machine learning (ML) workflows.
You can use Amazon SageMaker to simplify the process of building, training, and deploying ML models. ...

Example:
```python
from sagemaker.estimator import Estimator

estimator = Estimator(image_name="custom-training-container",
                      role="SageMakerRole",
                      train_instance_count=1,
                      train_instance_type="local")

estimator.fit()
```

...

</details>

### streamlit-plotly-events

Plotly chart component for Streamlit that also allows for events to bubble back up to Streamlit.

`pip install streamlit-plotly-events` · installs (wheel) · licence: not stated · rank 7787 · last release 2021-04-26 · [PyPI](https://pypi.org/project/streamlit-plotly-events/)

<details><summary>README extract</summary>

Plotly chart component for Streamlit that also allows for events to bubble back up to Streamlit.

</details>

### salamandra

Framework for netlist manipulation

`pip install salamandra` · installs (wheel) · licence: Apache Software License · rank 7795 · last release 2021-04-13 · [PyPI](https://pypi.org/project/salamandra/)

<details><summary>README extract</summary>

Salamandra is an extensible Pythonic
infrastructure for loading, analyzing, generating and storing of netlists.
Salamandra is under development and evolving so documentation of the latest features is missing and expected to be added
soon. ...

Example:
```python
import salamandra as slm
nmos = slm.Component('nmos')
nmos.add_pin(slm.Pin('source'))
nmos.add_pin(slm.Pin('drain'))
nmos.add_pin(slm.Pin('gate'))
nmos.add_pin(slm.Pin('body'))
```

Sections: Project Salamandra, Getting Salamandra, Basic Commands, Other Commands, Export Netlist, Import Netlist, Publication

</details>

### socketsecurity

Socket Security CLI for CI/CD

`pip install socketsecurity` · installs (wheel) · licence: not stated · rank 7797 · last release 2026-11-06 · [PyPI](https://pypi.org/project/socketsecurity/)

<details><summary>README extract</summary>

Sections: Quick start, 2) Authenticate, 3) Run a basic scan, Common use cases, Basic policy scan (no SARIF), GitLab dependency-scanning report, PR scan diffed against the merge base, SARIF use cases, Full-scope reachable SARIF (grouped alerts), Diff-scope reachable SARIF (PR/CI gating), Full-scope SARIF (instance-level detail), Choose your mode, Config files (`--config`), CI/CD examples

</details>

### simple-equ

An open source library containing multiple known STEM equations in a functional form.

`pip install simple-equ` · does not install on CPython 3.14 · licence: not stated · rank 7799 · last release 2026-04-20 · [PyPI](https://pypi.org/project/simple-equ/)

<details><summary>README extract</summary>

An open source library containing multiple known STEM equations in a functional form.

</details>

### schema-salad

Schema Annotations for Linked Avro Data (SALAD)

`pip install schema-salad` · installs (wheel) · licence: Apache-2.0 · rank 7821 · last release 2026-11-06 · [PyPI](https://pypi.org/project/schema-salad/) · [docs](https://schema-salad.readthedocs.io/) · [source](https://github.com/common-workflow-language/schema_salad/)

<details><summary>README extract</summary>

Salad is a schema language for describing JSON or YAML structured
linked data documents. Salad schema describes rules for
preprocessing, structural validation, and hyperlink checking for
documents described by a Salad schema. ...

Example:
```python
$ schema-salad-tool
usage: schema-salad-tool [-h] [--rdf-serializer RDF_SERIALIZER] [--skip-schemas]
                      [--strict-foreign-properties] [--version]
                      [--print-jsonld-context  --print-avro |
                           --print-rdf  --print-index
...
```

Sections: Schema Salad, Commands, Codegen Examples, Quick Start, Documentation, Rationale

</details>

### sphinx-autodoc2

Analyse a python project and create documentation for it.

`pip install sphinx-autodoc2` · installs (wheel) · licence: MIT License · rank 7837 · last release 2023-11-27 · [PyPI](https://pypi.org/project/sphinx-autodoc2/)

### synqly

SDK for Synqly APIs

`pip install synqly` · installs (wheel) · licence: not stated · rank 7857 · last release 2026-11-04 · [PyPI](https://pypi.org/project/synqly/)

<details><summary>README extract</summary>

This repository contains the `SynqlyPythonClient` SDK package, which can be used to integrate a Python application with Synqly APIs. All Synqly SDKs require a valid Synqly Organization token to use.

If you aren't yet a Synqly customer, please feel free to Schedule a Demo. ...

Example:
```python
from synqly import engine
from synqly import management as mgmt
```

Sections: Synqly Python SDK, Import the SDK

</details>

### sudachidict-small

Sudachi Dictionary for SudachiPy - Small Edition

`pip install sudachidict-small` · installs (wheel) · licence: Apache-2.0 · rank 7888 · last release 2026-10-15 · [PyPI](https://pypi.org/project/sudachidict-small/)

<details><summary>README extract</summary>

- WorksApplications/SudachiDict
- WorksApplications/SudachiPy

Managing the dictionary resources as Python packages.

- SudachiDict-small · PyPI
- SudachiDict-core · PyPI
- SudachiDict-full · PyPI

The dictionary files are not included in the packages; It will be downloaded upon installation (the procedure in `setup.py`). ...

Sections: Sudachi Dictionary for SudachiPy, Commands to download and set the dictionaries, Dictionary option in SudachiPy before v0.5.2

</details>

### snaptrade-python-sdk

Client for SnapTrade

`pip install snaptrade-python-sdk` · installs (wheel) · licence: MIT License · rank 7923 · last release 2026-11-06 · [PyPI](https://pypi.org/project/snaptrade-python-sdk/)

<details><summary>README extract</summary>

Connect brokerage accounts to your app for live positions and trading.

Two limits apply to requests signed with your `clientId`. The stricter one
wins, and exceeding either returns `429 Too Many Requests`.

- Customer-level — 250 requests/minute by default, scoped to your
 `clientId` and applied across all endpoints. ...

Example:
```python
# Commercial API key example: registers a SnapTrade user and uses userId/userSecret.
import os
import uuid
from pprint import pprint
from typing import List

from snaptrade_client import SnapTrade, SnapTradeAuth

# 1) Initialize a client with your clientID and consumerKey.
snaptrade = SnapTrade(
    auth=SnapTradeAuth.commercial_api_key(
...
```

...

</details>

### sphinx-jinja

includes jinja templates in a documentation

`pip install sphinx-jinja` · installs (wheel) · licence: MIT License · rank 7929 · last release 2022-07-05 · [PyPI](https://pypi.org/project/sphinx-jinja/) · [source](https://github.com/tardyp/sphinx-jinja)

<details><summary>README extract</summary>

A sphinx extension to include jinja based templates based documentation into a sphinx doc

Example:
```python
jinja_env_kwargs = {
    'lstrip_blocks': True,
}

jinja_filters = {
    'bold': lambda value: f'{value}',
}

jinja_tests = {
    'instanceof': lambda value, type: isinstance(value, type),
}

jinja_globals = {
    'list': list,
}

jinja_policies = {
    'compiler.ascii_str': False,
}
```

Sections: sphinx-jinja, Usage, Available options, Running tests

</details>

### sarif-tools

SARIF tools

`pip install sarif-tools` · installs (wheel) · licence: MIT License · rank 7943 · last release 2025-07-17 · [PyPI](https://pypi.org/project/sarif-tools/)

<details><summary>README extract</summary>

A set of command line tools and Python library for working with SARIF files.

Read more about the SARIF format here:
sarifweb.azurewebsites.net.

Example:
```python
from sarif import loader

sarif_data = loader.load_sarif_file(path_to_sarif_file)
report = sarif_data.get_report()
error_histogram = report.get_issue_type_histogram_for_severity("error")
```

Sections: SARIF Tools, Prerequisites, File format variations, Command Line Usage, Commands, blame, codeclimate, copy, csv, diff, emacs, html, info, ls

</details>

### selfies

SELFIES (SELF-referencIng Embedded Strings) is a general-purpose, sequence-based, robust representation of semantically constrained graphs.

`pip install selfies` · installs (wheel) · licence: Apache Software License · rank 7986 · last release 2025-01-15 · [PyPI](https://pypi.org/project/selfies/)

<details><summary>README extract</summary>

Self-Referencing Embedded Strings (SELFIES): A 100% robust molecular string representation\
_Mario Krenn, Florian Haese, AkshatKumar Nigam, Pascal Friederich, Alan Aspuru-Guzik\
*Machine Learning: Science and Technology* 1, 045024 (2020), extensive blog post January 2021.\
Talk on youtube about SELFIES.\
A community paper with 31 authors on ...

Features:
Please refer to the documentation in our code-paper,
which contains a thorough tutorial for getting started with ``selfies``
and detailed descriptions of the functions
that ``selfies`` provides. We summarize some key functions below. ...

Example:
```python
import selfies as sf

benzene = "c1ccccc1"

# SMILES -> SELFIES -> SMILES translation
try:
    benzene_sf = sf.encoder(benzene)  # CCCRing1
...

</details>

### squarify

Pure Python implementation of the squarify treemap layout algorithm

`pip install squarify` · installs (wheel) · licence: Apache License 2.0 · rank 7993 · last release 2026-09-11 · [PyPI](https://pypi.org/project/squarify/)

### spin

Developer tool for scientific Python libraries

`pip install spin` · installs (wheel) · licence: BSD-3-Clause · rank 8006 · last release 2026-10-29 · [PyPI](https://pypi.org/project/spin/)

<details><summary>README extract</summary>

Example:
```python
from spin import util

@click.command()
def example():
    """Command that accesses `pyproject.toml` configuration"""
    config = util.get_config()
    print(config["tool.spin"])
```

Sections: 💫 Scientific Python INcantations (`spin`), Configuration, Command sections, Running, Built-in commands, Meson, Build (PEP 517 builder), Meta (commands that operate on commands), 🧪 Custom commands, Argument overrides, Advanced: adding arguments to built-in commands, Advanced: override Meson CLI, Auto-completion

</details>

### sib-api-v3-sdk

SendinBlue API

`pip install sib-api-v3-sdk` · installs from source (sdist only) · licence: not stated · rank 8033 · last release 2023-03-20 · [PyPI](https://pypi.org/project/sib-api-v3-sdk/)

<details><summary>README extract</summary>

SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to : - Manage your campaigns and get the statistics - Manage your contacts - Send transactional Emails and SMS - and much more... ...

</details>

### s3pypi

CLI for creating a Python Package Repository in an S3 bucket

`pip install s3pypi` · installs (wheel) · licence: not stated · rank 8041 · last release 2024-01-14 · [PyPI](https://pypi.org/project/s3pypi/)

### smp

Simple Management Protocol (SMP) for remotely managing MCU firmware

`pip install smp` · installs (wheel) · licence: Apache-2.0 · rank 8059 · last release 2026-09-22 · [PyPI](https://pypi.org/project/smp/) · [docs](https://jphutchins.github.io/smp/) · [source](https://github.com/JPHutchins/smp)

<details><summary>README extract</summary>

Sections: User Documentation, Create the venv, Verify Your Setup, Enable the githooks

</details>

### snakemake-storage-plugin-s3

A Snakemake storage plugin for S3 API storage (AWS S3, MinIO, etc.)

`pip install snakemake-storage-plugin-s3` · installs (wheel) · licence: MIT License · rank 8114 · last release 2025-09-11 · [PyPI](https://pypi.org/project/snakemake-storage-plugin-s3/) · [docs](https://snakemake.github.io/snakemake-plugin-catalog/plugins/storage/s3.html) · [source](https://github.com/snakemake/snakemake-storage-plugin-s3)

<details><summary>README extract</summary>

A Snakemake storage plugin for S3 API storage (AWS S3, MinIO, etc.).
For documentation and usage instructions, see the Snakemake plugin catalog.

</details>

### sshfs

SSH Filesystem -- Async SSH/SFTP backend for fsspec

`pip install sshfs` · installs (wheel) · licence: Apache-2.0 · rank 8138 · last release 2026-08-07 · [PyPI](https://pypi.org/project/sshfs/) · [source](https://github.com/fsspec/sshfs)

<details><summary>README extract</summary>

sshfs is an implementation of fsspec for
the SFTP protocol using asyncssh.

Features:
- A complete implementation of the fsspec protocol through SFTP
- Supports features outside of the SFTP (e.g server side copy through SSH command execution)
- Quite fast (compared to alternatives like paramiko)
- Builtin Channel Management ...

Example:
```python
from fsspec import open

with open('ssh://[user@]host[:port]/path/to/file', "w") as file:
    file.write("Hello World!")

with open('ssh://[user@]host[:port]/path/to/file', "r") as file:
    print(file.read())
```

Sections: sshfs, Features, Tutorial

</details>

### scikit-learn-stubs

scikit-learn stubs from the Microsoft python-type-stubs repository

`pip install scikit-learn-stubs` · installs (wheel) · licence: MIT License · rank 8140 · last release 2025-08-28 · [PyPI](https://pypi.org/project/scikit-learn-stubs/)

<details><summary>README extract</summary>

This repository simply publishes the stubs from Microsoft's Python Type Stubs repository to PyPI.

I made this package because of a specific issue at work, in general you can simply install the stubs by following the instructions given in the Microsoft repository.

</details>

### spiffe

Python library for SPIFFE support

`pip install spiffe` · installs (wheel) · licence: Apache-2.0 · rank 8194 · last release 2026-10-29 · [PyPI](https://pypi.org/project/spiffe/) · [source](https://github.com/HewlettPackard/py-spiffe)

<details><summary>README extract</summary>

Features:
The `spiffe` package, part of the py-spiffe library,
provides SPIFFE support and essential
tools for interacting with
the SPIFFE Workload API. ...

Example:
```python
from spiffe import WorkloadApiClient

# Fetch X.509 and JWT SVIDs
with WorkloadApiClient() as client:
    x509_svid = client.fetch_x509_svid()
    print(f'SPIFFE ID: {x509_svid.spiffe_id}')

    jwt_svid = client.fetch_jwt_svid(audience={"test"})
    print(f'SPIFFE ID: {jwt_svid.spiffe_id}')
```

Sections: `spiffe` package, Overview, Features, Prerequisites, Usage, WorkloadApiClient, X509Source, JwtSource

</details>

### sf-hamilton

This package has moved to apache-hamilton. Install apache-hamilton instead.

`pip install sf-hamilton` · installs (wheel) · licence: Apache-2.0 · rank 8228 · last release 2026-04-25 · [PyPI](https://pypi.org/project/sf-hamilton/) · [docs](https://hamilton.apache.org/)

<details><summary>README extract</summary>

<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements. See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership. ...

Sections: sf-hamilton has moved to apache-hamilton, Migration

</details>

### smooth-py

(no summary)

`pip install smooth-py` · installs (wheel) · licence: not stated · rank 8277 · last release 2026-06-15 · [PyPI](https://pypi.org/project/smooth-py/)

<details><summary>README extract</summary>

TL;DR: Smooth is an AI browser automation SDK and CLI that can act and extract information from the web. It's powered by our browser agent which controls the browser with mouse and keyboard to carry out tasks autonomously on the web.

Discord · Documentation · Get API Key

Features:
Autonomous agents like Claude Code are amazing at meaningful work—but they're mostly stuck in the CLI. Meanwhile, most valuable human work happens in the browser. ...

Example:
```python
from smooth import SmoothClient

smooth_client = SmoothClient(api_key="cmzr-YOUR_API_KEY")
task = smooth_client.run("Go to google flights and find the cheapest flight from London to Paris today")

print(f"Live URL: {task.live_url()}")
print(f"Agent response: {task.result()}")
```

...

</details>

### statistics

A Python 2.* port of 3.4 Statistics Module

`pip install statistics` · installs from source (sdist only) · licence: Apache License 2.0 · rank 8311 · last release 2014-10-16 · [PyPI](https://pypi.org/project/statistics/)

<details><summary>README extract</summary>

A port of Python 3.4 statistics module to Python 2.*, initially done through the 3to2 tool.

This module provides functions for calculating mathematical statistics of numeric (Real-valued) data.

Relevant links:

Make a version for Python 3.0 -> 3.2 (

Sections: statistics - Mathematical statistics functions, Sources, TODO

</details>

### scrapy-impersonate

Scrapy download handler that can impersonate browser fingerprints

`pip install scrapy-impersonate` · installs (wheel) · licence: MIT License · rank 8312 · last release 2026-10-29 · [PyPI](https://pypi.org/project/scrapy-impersonate/)

<details><summary>README extract</summary>

`scrapy-impersonate` is a Scrapy download handler. This project integrates curl_cffi to perform HTTP requests, so it can impersonate browsers' TLS signatures or JA3 fingerprints.

Example:
```python
import scrapy

class ImpersonateSpider(scrapy.Spider):
    name = "impersonate_spider"
    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "USER_AGENT": "",
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_impersonate.ImpersonateDownloadHandler",
...
```

Sections: scrapy-impersonate, Activation, Usage, impersonate-args, curl-options, Thanks

</details>

### surt

Sort-friendly URI Reordering Transform (SURT) python package.

`pip install surt` · installs from source (sdist only) · licence: GNU Affero General Public License v3 · rank 8321 · last release 2019-08-22 · [PyPI](https://pypi.org/project/surt/)

_README extract left out: share-alike licence._

### stac-fastapi-types

Core API for stac-fastapi modules.

`pip install stac-fastapi-types` · installs (wheel) · licence: MIT · rank 8333 · last release 2026-11-02 · [PyPI](https://pypi.org/project/stac-fastapi-types/)

### stac-fastapi-api

An implementation of STAC API based on the FastAPI framework.

`pip install stac-fastapi-api` · installs (wheel) · licence: MIT · rank 8345 · last release 2026-11-02 · [PyPI](https://pypi.org/project/stac-fastapi-api/)

### stac-fastapi-extensions

Extensions for stac-fastapi apis.

`pip install stac-fastapi-extensions` · installs (wheel) · licence: MIT · rank 8355 · last release 2026-11-02 · [PyPI](https://pypi.org/project/stac-fastapi-extensions/)

### survey

A simple library for creating beautiful interactive prompts.

`pip install survey` · installs (wheel) · licence: MIT · rank 8365 · last release 2024-10-21 · [PyPI](https://pypi.org/project/survey/)

<details><summary>README extract</summary>

✨ A simple library for creating beautiful interactive prompts.

Features:
- Pythonic: Friendly interface built around simple functions.
- Lightweight: No external depencencies for any operating system.
- Adaptable: Works with any string formatting and window size. ...

Sections: Features, Links

</details>

### sortedcollections

Python Sorted Collections

`pip install sortedcollections` · installs (wheel) · licence: Apache Software License · rank 8370 · last release 2021-01-18 · [PyPI](https://pypi.org/project/sortedcollections/)

<details><summary>README extract</summary>

Sorted Collections is an Apache2 licensed Python sorted collections library.

Features:
- Pure-Python
- Depends on the Sorted Containers module.
- ValueSortedDict - Dictionary with (key, value) item pairs sorted by value.
- ItemSortedDict - Dictionary with key-function support for item pairs. ...

Example:
```python
>>> from sortedcollections import ValueSortedDict
>>> help(ValueSortedDict)  # doctest: +SKIP
```

Sections: Python Sorted Collections, Features, Quickstart, Recipes, Reference and Indices

</details>

### soynlp

Unsupervised Korean Natural Language Processing Toolkits

`pip install soynlp` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 8394 · last release 2019-08-25 · [PyPI](https://pypi.org/project/soynlp/)

_README extract left out: share-alike licence._

### shinychat

An AI Chat interface for Shiny apps.

`pip install shinychat` · installs (wheel) · licence: MIT · rank 8412 · last release 2026-09-18 · [PyPI](https://pypi.org/project/shinychat/) · [docs](https://posit-dev.github.io/shinychat/py/) · [source](https://github.com/posit-dev/shinychat)

<details><summary>README extract</summary>

Chat UI component for Shiny for Python.

Note: shinychat is automatically installed with Shiny for Python and available as `shiny.ui.Chat` and `shiny.express.ui.Chat`. For complete instructions about creating chatbots please see the Shiny for Python documentation.

Sections: shinychat, Example

</details>

### sslpsk-pmd3

sslpsk fork for pymobiledevice3

`pip install sslpsk-pmd3` · installs (wheel) · licence: not stated · rank 8461 · last release 2026-11-02 · [PyPI](https://pypi.org/project/sslpsk-pmd3/)

<details><summary>README extract</summary>

TLS-PSK for Python's `ssl` module. Fork of sslpsk with support for the latest Python versions.

`SSLPSKContext` provides Python 3.13's `set_psk_client_callback()`/`set_psk_server_callback()` on every
supported version (on 3.13+ they are the native implementation): ...

Example:
```python
import ssl
from sslpsk_pmd3 import SSLPSKContext

client = SSLPSKContext(ssl.PROTOCOL_TLS_CLIENT)
client.check_hostname = False
client.verify_mode = ssl.CERT_NONE
client.set_ciphers("PSK")
client.set_psk_client_callback(lambda hint: ("client-identity", b"secret"))

server = SSLPSKContext(ssl.PROTOCOL_TLS_SERVER)
server.set_ciphers("PSK")
...
```

</details>

### sqlalchemy-easy-softdelete

Easily add soft-deletion to your SQLAlchemy Models.

`pip install sqlalchemy-easy-softdelete` · installs (wheel) · licence: BSD-3-Clause · rank 8475 · last release 2026-11-07 · [PyPI](https://pypi.org/project/sqlalchemy-easy-softdelete/) · [source](https://github.com/flipbit03/sqlalchemy-easy-softdelete)

<details><summary>README extract</summary>

Easily add soft-deletion to your SQLAlchemy Models and automatically filter out soft-deleted objects from your queries and relationships.

This package can generate a tailor-made SQLAlchemy Mixin that can be added to your SQLAlchemy Models, making them contain a field that, when set, will mark the entity as being soft-deleted. ...

Example:
```python
from sqlalchemy_easy_softdelete.mixin import generate_soft_delete_mixin_class
from sqlalchemy_easy_softdelete.hook import IgnoredTable
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer
from datetime import datetime

# Create a Class that inherits from our class builder
class SoftDeleteMixin(
...
```

Sections: SQLAlchemy Easy Soft-Delete, How to use, Example Usage, Rewrite cache

</details>

### sphinx-substitution-extensions

Extensions for Sphinx which allow for substitutions.

`pip install sphinx-substitution-extensions` · installs (wheel) · licence: MIT · rank 8479 · last release 2026-10-09 · [PyPI](https://pypi.org/project/sphinx-substitution-extensions/) · [source](https://github.com/adamtheturtle/sphinx-substitution-extensions)

<details><summary>README extract</summary>

Extensions for Sphinx which allow substitutions within code blocks.

Sections: Sphinx Substitution Extensions, rST setup, Using substitutions in rST documents, `code-block`, Inline `:substitution-code:`, `substitution-download`, External hyperlinks, `literalinclude`, `include`, `image`, MyST Markdown setup, Enabling substitutions by default, Using substitutions in MyST Markdown

</details>

### stac-fastapi-pgstac

An implementation of STAC API based on the FastAPI framework and using the pgstac backend.

`pip install stac-fastapi-pgstac` · installs (wheel) · licence: MIT · rank 8487 · last release 2026-11-02 · [PyPI](https://pypi.org/project/stac-fastapi-pgstac/)

<details><summary>README extract</summary>

PgSTAC backend for stac-fastapi, the FastAPI implementation of the STAC API spec

Features:
stac-fastapi-pgstac is an HTTP interface built in FastAPI.
It validates requests and data sent to a PgSTAC backend, and adds links to the returned data. ...

Sections: stac-fastapi-pgstac, Overview, `PgSTAC` version, Usage, Sorting, Hydration, Multi-Tenant Catalogs Extension, Poly-Hierarchy Links, Migrations, Quick Start, Running the API Locally, Running with Nginx Proxy, Loading Demo Data, Running Tests

</details>

### sap-cloud-sdk

SAP Cloud SDK for Python

`pip install sap-cloud-sdk` · installs (wheel) · licence: Apache-2.0 · rank 8557 · last release 2026-11-06 · [PyPI](https://pypi.org/project/sap-cloud-sdk/)

<details><summary>README extract</summary>

This SDK provides consistent interfaces for interacting with foundational services such as object storage, destination management, audit logging, data anonymization, data privacy integration, telemetry, and secure credential handling. ...

Features:
- Agent Decorators
- Agent Gateway
- Agent Memory
- AI Core Integration
- Audit Log Service
- Audit Log NG
- Destination Service
- Document Management Service
- Extensibility
- IAS (Identity and Access Service)
- ObjectStore Service ...

Sections: SAP Cloud SDK for Python, About this project, Key Features, Requirements and Setup, uv, Poetry, pip, Environment Configuration, Usage Guides, Licensing

</details>

### sexpdata

S-expression parser for Python

`pip install sexpdata` · installs (wheel) · licence: BSD License · rank 8597 · last release 2024-01-09 · [PyPI](https://pypi.org/project/sexpdata/)

<details><summary>README extract</summary>

`sexpdata` is a simple S-expression parser/serializer. It has
simple `load` and `dump` functions like `pickle`, `json` or `PyYAML`
module.

>>> from sexpdata import loads, dumps
>>> loads('("a" "b")')
['a', 'b']
>>> print(dumps(['a', 'b']))
("a" "b")

You can install `sexpdata` from PyPI:
Links: ...

</details>

### streamlit-extras

A community-driven collection of useful Streamlit components and utilities that extend Streamlit's functionality.

`pip install streamlit-extras` · installs (wheel) · licence: Apache-2.0 · rank 8599 · last release 2026-05-15 · [PyPI](https://pypi.org/project/streamlit-extras/)

<details><summary>README extract</summary>

A Python library with useful Streamlit extras

`streamlit-extras` is a Python library putting together useful Streamlit bits of code (extras).

Features:
- 📙 Discover: Visit our documentation to discover all extras.
- ⬇️ Install: `streamlit-extras` is a PyPI package with all extras included. Get them all using pip!
- 🫴 Share: Go ahead and share your own extras, it's just a PR away!

Example:
```python
from streamlit_extras.stoggle import stoggle

stoggle(
    "Click me!",
    """🥷 Surprise! Here's some additional content""",
)
```

Sections: 🪢 streamlit-extras, Highlights, Getting Started, Usage, Documentation

</details>

### simple-icd-10-cm

A simple python library for ICD-10-CM codes

`pip install simple-icd-10-cm` · installs (wheel) · licence: MIT License · rank 8606 · last release 2026-02-02 · [PyPI](https://pypi.org/project/simple-icd-10-cm/)

<details><summary>README extract</summary>

A simple python library for ICD-10-CM codes

* Release notes
* Introduction
* Setup
 * Using other ICD-10-CM releases
* The format of the codes
* About the file "Instructional Notations.md"
* Blocks containing only one category
* About the special seventh character
* Documentation
 * is_valid_item(code)
 * is_category_or_subcategory(code)
 * ...

Example:
```python
cm.is_block("B99")
# True
cm.is_category("B99")
# True
```

Sections: simple_icd_10_cm, Index, Introduction, Setup, The format of the codes, About the file "Instructional Notations.md", Blocks containing only one category, About the special seventh character, Documentation, is_valid_item(code), is_category_or_subcategory(code), is_chapter_or_block(code), is_chapter(code), is_block(code)

</details>

### sphinx-rtd-dark-mode

Dark mode for the Sphinx Read the Docs theme.

`pip install sphinx-rtd-dark-mode` · installs (wheel) · licence: MIT License · rank 8640 · last release 2023-09-19 · [PyPI](https://pypi.org/project/sphinx-rtd-dark-mode/)

<details><summary>README extract</summary>

This Sphinx extension adds a toggleable dark mode to the Read the Docs theme.
A little icon is added in the bottom right hand corner which allows the user
to switch between light or dark mode.

Sections: Sphinx RTD Theme Dark Mode, Using the Extension, Config, Default Dark Mode

</details>

### sphinx-inline-tabs

Add inline tabbed content to your Sphinx documentation.

`pip install sphinx-inline-tabs` · installs (wheel) · licence: MIT · rank 8692 · last release 2025-12-21 · [PyPI](https://pypi.org/project/sphinx-inline-tabs/) · [docs](https://sphinx-inline-tabs.readthedocs.io)

<details><summary>README extract</summary>

<!-- start-include-here -->

Add inline tabbed content to your Sphinx documentation.

Features:
- Elegant design: Small footprint in the markup and generated website, while looking good.
- Configurable: All the colors can be configured using CSS variables.
- Synchronisation: Tabs with the same label all switch with a single click. ...

Sections: Sphinx Inline Tabs, Features

</details>

### sqlalchemy-dremio

A SQLAlchemy dialect for Dremio via the Flight interface.

`pip install sqlalchemy-dremio` · installs from source (sdist only) · licence: Apache Software License · rank 8763 · last release 2026-03-12 · [PyPI](https://pypi.org/project/sqlalchemy-dremio/)

<details><summary>README extract</summary>

A SQLAlchemy dialect for Dremio via ODBC and Flight interfaces.

<!--ts-->
 * Installation
 * Usage
 * Testing
 * Superset Integration
<!--te-->

Installation

From pip:

`pip install sqlalchemy_dremio`

Or from conda:

`conda install sqlalchemy-dremio`

To install from source:
`python setup.py install`

Usage

Connection String example: ...

</details>

### starpulse

StarPulse visualizes the workflows runs adapters read, lifecycle machines and the agents moving through them

`pip install starpulse` · installs (wheel) · licence: MIT · rank 8788 · last release 2026-10-24 · [PyPI](https://pypi.org/project/starpulse/)

<details><summary>README extract</summary>

Every task, workflow run and agent in flight, on one live page.

 Live demo ·
 Configure ·
 Sources ·
 Agent CLI ·
 Adapters ·
 Consumers ·
 Security ·
 Compatibility ·
 Development loop ·
 Contributing

Features:
I wanted to see where my agents were in their sessions and which skills they
were using. Then I watched a video that mapped agent actions onto state
machines, and I wanted to map the whole agent lifecycle and pair it with the
Dagu workflows I ...

Sections: StarPulse, What it is and why, Quick start, Working with AI agents, Working without AI agents, Views, Feedback

</details>

### simple-di

simple dependency injection library

`pip install simple-di` · installs (wheel) · licence: Apache License 2.0 · rank 8816 · last release 2022-02-22 · [PyPI](https://pypi.org/project/simple-di/)

<details><summary>README extract</summary>

A simple, strictly typed dependency injection library.

- Install
- Usage
- API

Example:
```python
from simple_di import inject, Provide, Provider, container
from simple_di.providers import Static, Factory, Configuration

@container
class OptionsClass(container):
    cpu: Provider[int] = Static(2)
    worker: Provider[int] = Factory(lambda c: 2 * int(c) + 1, c=cpu)

Options = OptionsClass()

@inject
...
```

Sections: simple-di, Usage, API, inject

</details>

### sglang-router

High-performance Rust-based load balancer for SGLang with multiple routing algorithms and prefill-decode disaggregation support

`pip install sglang-router` · installs (wheel) · licence: Apache-2.0 · rank 8829 · last release 2026-01-15 · [PyPI](https://pypi.org/project/sglang-router/)

<details><summary>README extract</summary>

High-performance model routing control and data plane for large-scale LLM deployments. The gateway orchestrates fleets of workers, balances traffic across HTTP and gRPC backends, and exposes OpenAI-compatible APIs with pluggable history storage and tool integrations—while remaining deeply optimized for the SGLang serving runtime.

Features:
- Unified control plane for registering, monitoring, and orchestrating prefill, decode, and regular workers across heterogeneous model fleets. ...

Sections: SGLang Model Gateway, Overview, Architecture at a Glance, Feature Highlights, Documentation, Docker, Prerequisites, Rust Binary, Python Package, Checking Version, Quick Start, Regular HTTP Routing, Prefill/Decode Disaggregation (PD), Multi-Model Inference Gateway

</details>

### sec-downloader

Useful extensions for sec-edgar-downloader.

`pip install sec-downloader` · installs (wheel) · licence: MIT License · rank 8838 · last release 2025-05-20 · [PyPI](https://pypi.org/project/sec-downloader/)

<details><summary>README extract</summary>

A better version of `sec-edgar-downloader`. Includes an alternative
implementation (a wrapper instead of a fork), to keep compatibility with
new `sec-edgar-downloader` releases. This library partially uses
nbdev.

Features:
Advantages over `sec-edgar-downloader`:

Flexibility in Download Process

- Tailored for choosing *what*, *where*, and *how* to download.
- Files stored in memory for faster operations and no unnecessary disk
 clutter. ...

Example:
```python
from sec_downloader import Downloader

dl = Downloader("MyCompanyName", "email@example.com")
```

Sections: sec-downloader, Features, How to use, Download the metadata, Download the HTML files, Alternative implementation: Wrapper, Frequently Asked Questions (FAQ)

</details>

### semantic-link

Semantic link for Microsoft Fabric

`pip install semantic-link` · installs (wheel) · licence: Other/Proprietary License · rank 8844 · last release 2026-10-22 · [PyPI](https://pypi.org/project/semantic-link/)

<details><summary>README extract</summary>

Semantic link is a feature that allows you to establish a connection between Power BI datasets and Synapse Data Science in Microsoft Fabric.

The primary goals of semantic link are to facilitate data connectivity, enable the propagation of semantic information, and seamlessly integrate with established tools used by data scientists, such as ...

Sections: Getting started, Prerequisites, About the semantic link packages, Key concepts, 0.14.3, 0.14.2, 0.14.1, 0.14.0, 0.13.0, 0.12.3, 0.12.2, 0.12.1, 0.12.0, 0.11.2

</details>

### spaces

Utilities for Hugging Face Spaces

`pip install spaces` · installs (wheel) · licence: Apache-2.0 · rank 8874 · last release 2026-08-31 · [PyPI](https://pypi.org/project/spaces/) · [source](https://github.com/huggingface/huggingface_hub)

### sqlalchemy-postgres-copy

Utilities for using PostgreSQL COPY with SQLAlchemy

`pip install sqlalchemy-postgres-copy` · installs (wheel) · licence: Copyright 2016 Joshua Carp · rank 8879 · last release 2017-04-07 · [PyPI](https://pypi.org/project/sqlalchemy-postgres-copy/)

<details><summary>README extract</summary>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit ...

</details>

### simple-pid

A simple, easy to use PID controller

`pip install simple-pid` · installs (wheel) · licence: MIT License · rank 8905 · last release 2024-07-21 · [PyPI](https://pypi.org/project/simple-pid/) · [docs](https://simple-pid.readthedocs.io/)

<details><summary>README extract</summary>

A simple and easy to use PID controller in Python. If you want a PID controller without external dependencies that just works, this is for you! The PID was designed to be robust with help from Brett Beauregards guide.

Usage is very simple:

Example:
```python
from simple_pid import PID
pid = PID(1, 0.1, 0.05, setpoint=1)

# Assume we have a system we want to control in controlled_system
v = controlled_system.update(0)

while True:
    # Compute new output from the PID according to the systems current value
    control = pid(v)

    # Feed the PID output to the system and get its current value
...
```

Sections: simple-pid, Documentation, Tests

</details>

### sphinx-llm

(no summary)

`pip install sphinx-llm` · installs (wheel) · licence: not stated · rank 8925 · last release 2026-09-21 · [PyPI](https://pypi.org/project/sphinx-llm/) · [docs](https://github.com/NVIDIA/sphinx-llm#readme) · [source](https://github.com/NVIDIA/sphinx-llm)

<details><summary>README extract</summary>

The `sphinx-llm` package includes a collection of
Sphinx extensions for working with LLMs.

There are two categories of tools in this package:

- Enabling LLMs and agents to consume your docs - Produces additional build
 output for consumption by LLMs and agents. ...

Sections: sphinx-llm, Extensions, HTML discovery metadata, Configuration, Generated page summaries, Custom `llms.txt` override, Docref, Docref styling, Building the docs, Alternatives

</details>

### sqruff

A SQL linter written in rust.

`pip install sqruff` · installs (wheel) · licence: not stated · rank 8928 · last release 2026-10-30 · [PyPI](https://pypi.org/project/sqruff/)

<details><summary>README extract</summary>

`sqruff` is a SQL linter and formatter written in Rust.

- Linting: advanced, configurable SQL linting
- Formatting: automated, configurable formatting
- Speed: fast and efficient
- Portability: easy to integrate into dev workflows

Try it in the browser:

Sections: sqruff, Quickstart, Lint a project, Configure a project, Editor integrations, Documentation

</details>

### semantic-link-functions-holidays

Semantic link functions for holidays package. Enables enrichment of FabricDataFrame with public holidays.

`pip install semantic-link-functions-holidays` · installs (wheel) · licence: MIT License · rank 8940 · last release 2026-10-22 · [PyPI](https://pypi.org/project/semantic-link-functions-holidays/)

<details><summary>README extract</summary>

FabricDataFrames dynamically expose semantic functions based on logic defined by each function. For example, the is_holiday function shows up in the autocomplete suggestions when you're working on a FabricDataFrame containing both a datetime column and a country column. ...

Example:
```python
from sempy.fabric import FabricDataFrame

df = FabricDataFrame(
    {"country": ["US", "AT"], "date": ["2023-01-06", "2023-01-06"]},
    column_metadata={"country": {"data_category": "Country"}},
)

df["date"] = pd.to_datetime(df["date"])

holiday_series = df.is_holiday(date_col="date", country_col="country")
```

</details>

### semantic-link-functions-geopandas

Semantic link functions for Geopandas. Enables conversion of a FabricDataFrame to a GeoDataFrame.

`pip install semantic-link-functions-geopandas` · installs (wheel) · licence: MIT License · rank 8943 · last release 2026-10-22 · [PyPI](https://pypi.org/project/semantic-link-functions-geopandas/)

<details><summary>README extract</summary>

FabricDataFrames dynamically expose semantic functions based on logic defined by each function. For example, the is_holiday function shows up in the autocomplete suggestions when you're working on a FabricDataFrame containing both a datetime column and a country column. ...

Example:
```python
from sempy.fabric import FabricDataFrame

df = FabricDataFrame(
    {"country": ["US", "AT"],
        "lat": [40.7128, 47.8095],
        "long": [-74.0060, 13.0550]},
    column_metadata={"lat": {"data_category": "Latitude"}, "long": {"data_category": "Longitude"}},
)

df_geo = df.to_geopandas(lat_col="lat", long_col="long")
```

</details>

### semantic-link-functions-meteostat

Semantic link functions for meteostat package. Enables enrichment of FabricDataFrame with historical weather data.

`pip install semantic-link-functions-meteostat` · installs (wheel) · licence: MIT License · rank 8945 · last release 2026-10-22 · [PyPI](https://pypi.org/project/semantic-link-functions-meteostat/)

<details><summary>README extract</summary>

FabricDataFrames dynamically expose semantic functions based on logic defined by each function. For example, the is_holiday function shows up in the autocomplete suggestions when you're working on a FabricDataFrame containing both a datetime column and a country column. ...

Example:
```python
from sempy.fabric import FabricDataFrame

df = FabricDataFrame({
        "lat": [40.7128, 47.8095, 47.8095, 47.8095],
        "long": [-74.0060, 13.0550, 13.0550, 13.0550],
        "date": ["2023-01-06", "2023-01-06", "2023-01-07", "2023-01-10"]
    },
...
```

</details>

### semantic-link-functions-phonenumbers

Semantic link functions for phonenumbers package. Enables validation of phone numbers in FabricDataFrames.

`pip install semantic-link-functions-phonenumbers` · installs (wheel) · licence: MIT License · rank 8947 · last release 2026-10-22 · [PyPI](https://pypi.org/project/semantic-link-functions-phonenumbers/)

<details><summary>README extract</summary>

FabricDataFrames dynamically expose semantic functions based on logic defined by each function. For example, the is_holiday function shows up in the autocomplete suggestions when you're working on a FabricDataFrame containing both a datetime column and a country column. ...

Example:
```python
from sempy.fabric import FabricDataFrame

df = FabricDataFrame(
    {"num": ["+442083661177", "ABC000-0000", "abc"], "country": ["US", "AT", "Unknown"]},
    column_metadata={"country": {"data_category": "Country"}},
)

is_phone_series = df.is_phonenumber(col_num="num", col_country="country")
```

</details>

### semantic-link-functions-validators

Semantic link functions for validators package. Enables validation of email addresses, credit card numbers, ... in FabricDataFrames.

`pip install semantic-link-functions-validators` · installs (wheel) · licence: MIT License · rank 8948 · last release 2026-10-22 · [PyPI](https://pypi.org/project/semantic-link-functions-validators/)

<details><summary>README extract</summary>

FabricDataFrames dynamically expose semantic functions based on logic defined by each function. For example, the is_holiday function shows up in the autocomplete suggestions when you're working on a FabricDataFrame containing both a datetime column and a country column. ...

Example:
```python
from sempy.fabric import FabricDataFrame

df = FabricDataFrame(
        {"contact_email": ["a@b.com", "d.com"],
         "amex": ["378282246310005", "4242424242424242"],
         "iban": ["DE29100500001061045672", "123456"],
         "es_nie": ["X0095892M", "X0095892X"]}
    )

df["contact_email"].validators.is_email()
```

</details>

### socks

This package was automatically generated with 'register_pypi' and should be deleted soon!

`pip install socks` · installs from source (sdist only) · licence: not stated · rank 8963 · last release 2019-09-20 · [PyPI](https://pypi.org/project/socks/)

### staticmap

A small, python-based library for creating map images with lines and markers.

`pip install staticmap` · installs (wheel) · licence: not stated · rank 8966 · last release 2023-08-01 · [PyPI](https://pypi.org/project/staticmap/)

### sagemaker-feature-store-pyspark

Amazon SageMaker FeatureStore PySpark Bindings

`pip install sagemaker-feature-store-pyspark` · installs (wheel) · licence: Apache-2.0 · rank 8996 · last release 2026-10-13 · [PyPI](https://pypi.org/project/sagemaker-feature-store-pyspark/)

<details><summary>README extract</summary>

SageMaker FeatureStore Spark is an open source Spark library for
Amazon SageMaker FeatureStore.
With this connector, you can easily ingest data to FeatureGroup's online and
offline store from Spark `DataFrame`. This package provides the Python (PySpark)
interface. ...

Example:
```python
from feature_store_pyspark.FeatureStoreManager import FeatureStoreManager

feature_group_arn = "arn:aws:sagemaker:...:feature-group/your-feature-group"
feature_store_manager = FeatureStoreManager()
feature_store_manager.ingest_data(
    input_data_frame=df,
    feature_group_arn=feature_group_arn,
    target_stores=["OfflineStore"]
)
```

...

</details>

### simple-settings

A simple way to manage your project settings.

`pip install simple-settings` · installs (wheel) · licence: MIT License · rank 9015 · last release 2021-12-30 · [PyPI](https://pypi.org/project/simple-settings/) · [source](https://github.com/drgarcia1986/simple-settings)

### siwe

A Python implementation of Sign-In with Ethereum (EIP-4361).

`pip install siwe` · installs (wheel) · licence: Other/Proprietary License · rank 9017 · last release 2024-10-11 · [PyPI](https://pypi.org/project/siwe/) · [source](https://github.com/spruceid/siwe-py)

<details><summary>README extract</summary>

This package provides a Python implementation of EIP-4361: Sign In With Ethereum.

Example:
```python
try:
    message: SiweMessage = SiweMessage(message=eip_4361_string)
    message.verify(signature, nonce="abcdef", domain="example.com"):
except siwe.ValueError:
    # Invalid message
    print("Authentication attempt rejected.")
except siwe.ExpiredMessage:
    print("Authentication attempt rejected.")
except siwe.DomainMismatch:
...
```

Sections: Sign-In with Ethereum, Usage, Parsing a SIWE Message, Verifying and Authenticating a SIWE Message, Serialization of a SIWE Message, Example, See Also, Disclaimer

</details>

### sgl-flash-mla

FlashMLA attention kernels for SGLang

`pip install sgl-flash-mla` · installs (wheel) · licence: MIT License · rank 9063 · last release 2026-11-06 · [PyPI](https://pypi.org/project/sgl-flash-mla/)

<details><summary>README extract</summary>

A fork of deepseek-ai/FlashMLA, packaged as a standalone wheel for SGLang.

It differs from upstream in three ways:

- Upstream's current kernels are carried verbatim. `csrc/` is a byte-for-byte copy of upstream's NVIDIA sources, so syncing is a directory replacement rather than a merge. The Huawei Ascend NPU target is not carried. ...

Sections: FlashMLA (SGLang fork), Requirements, Tests

</details>

### sybil-extras

Additions to Sybil, the documentation testing tool.

`pip install sybil-extras` · installs (wheel) · licence: MIT · rank 9067 · last release 2026-10-09 · [PyPI](https://pypi.org/project/sybil-extras/) · [docs](https://adamtheturtle.github.io/sybil-extras/) · [source](https://github.com/adamtheturtle/sybil-extras)

<details><summary>README extract</summary>

Add ons for Sybil.

Example:
```python
"""Use MultiEvaluator to run multiple evaluators on the same parser."""

from sybil import Example, Sybil
from sybil.evaluators.python import PythonEvaluator
from sybil.parsers.rest.codeblock import CodeBlockParser
from sybil.typing import Evaluator

from sybil_extras.evaluators.multi import MultiEvaluator

...
```

Sections: sybil-extras, Evaluators, MultiEvaluator, ShellCommandEvaluator, BlockAccumulatorEvaluator, NoOpEvaluator, CodeBlockWriterEvaluator, Parsers, CustomDirectiveSkipParser, ThreadSafeSkipParser, GroupedSourceParser, GroupAllParser, AttributeGroupedSourceParser, SphinxJinja2Parser

</details>

### slither-analyzer

Slither is a Solidity and Vyper static analysis framework written in Python 3.

`pip install slither-analyzer` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 9093 · last release 2026-07-28 · [PyPI](https://pypi.org/project/slither-analyzer/)

_README extract left out: share-alike licence._

### schedulefree

Schedule Free Learning in PyTorch

`pip install schedulefree` · installs (wheel) · licence: Apache Software License · rank 9096 · last release 2025-03-24 · [PyPI](https://pypi.org/project/schedulefree/) · [source](https://github.com/facebookresearch/schedule_free)

<details><summary>README extract</summary>

Schedule-Free Optimizers in PyTorch.

Preprint: The Road Less Scheduled

Authors: Aaron Defazio, Xingyu (Alice) Yang, Harsh Mehta, Konstantin Mishchenko, Ahmed Khaled, Ashok Cutkosky

TLDR Faster training without schedules - no need to specify the stopping time/steps in advance! ...

Example:
```python
This will replace the `training_mean`/`training_var` cache (which is updated in each forward pass when in model.train() mode) with values calculated at $x$ instead of $y$. Using PreciseBN will also avoid this issue.

...
```

</details>

### sinter

Samples stim circuits and decodes them using pymatching.

`pip install sinter` · installs from source (sdist only) · licence: Apache 2 · rank 9169 · last release 2026-05-22 · [PyPI](https://pypi.org/project/sinter/)

<details><summary>README extract</summary>

Sinter is a software tool/library for doing fast monte carlo sampling of
quantum error correction circuits.

- How it works
- How to install
- How to use: Python API
 - Sinter Python API Reference
- How to use: Linux Command Line
 - Sinter Command Line Reference
- The csv format for sample statistics ...

Example:
```python
import stim
import sinter
import matplotlib.pyplot as plt

# Generates surface code circuit tasks using Stim's circuit generation.
def generate_example_tasks():
    for p in [0.001, 0.005, 0.01]:
        for d in [3, 5]:
            yield sinter.Task(
                circuit=stim.Circuit.generated(
                    rounds=d,
...
```

...

</details>

### sqlite-migrate

Compatibility package for sqlite-utils migrations

`pip install sqlite-migrate` · installs (wheel) · licence: Apache-2.0 · rank 9264 · last release 2026-07-07 · [PyPI](https://pypi.org/project/sqlite-migrate/)

<details><summary>README extract</summary>

Deprecated compatibility package for `sqlite-utils` migrations.

Migration support is now built into `sqlite-utils` 4. Install and use `sqlite-utils` directly for new projects:

New code should import `Migrations` from `sqlite_utils`: ...

Example:
```python
from sqlite_utils import Migrations
```

</details>

### shazamio

An asynchronous framework for the reverse engineered Shazam API, written in Python with asyncio and aiohttp.

`pip install shazamio` · installs (wheel) · licence: MIT · rank 9267 · last release 2026-10-26 · [PyPI](https://pypi.org/project/shazamio/) · [source](https://github.com/shazamio/ShazamIO)

<details><summary>README extract</summary>

🎵 Is a FREE asynchronous library from reverse engineered Shazam API written in Python 3.10+ with asyncio and aiohttp. Recognizes a song from a file or from bytes, reads a track, and returns every chart Shazam publishes.

Example:
```python
import asyncio
from shazamio import Serialize, Shazam

async def main():
    async with Shazam() as shazam:
        out = await shazam.recognize("Gloria.ogg")

        print(out)  # dict
        print(Serialize.full_track(out).track.title)  # I Will Survive

asyncio.run(main())
```

Sections: 💻 Example, 🔌 Closing what you open, 🎯 When a match may be wrong, 📊 What the chart methods return, 🔧 What data serialization gives you

</details>

### sphinx-multitoc-numbering

Supporting continuous HTML section numbering

`pip install sphinx-multitoc-numbering` · installs (wheel) · licence: MIT · rank 9291 · last release 2021-03-15 · [PyPI](https://pypi.org/project/sphinx-multitoc-numbering/)

### scalecodec

Python SCALE Codec Library

`pip install scalecodec` · installs (wheel) · licence: Apache Software License · rank 9323 · last release 2025-10-16 · [PyPI](https://pypi.org/project/scalecodec/)

<details><summary>README extract</summary>

Substrate uses a lightweight and efficient encoding and decoding program to optimize how data is sent and received over the network. The program used to serialize and deserialize data is called the SCALE codec, with SCALE being an acronym for Simple Concatenated Aggregate Little-Endian.

Sections: Python SCALE Codec, Description, Documentation, Examples of different types

</details>

### strip-markdown

Converts markdown to plain text

`pip install strip-markdown` · installs (wheel) · licence: MIT License · rank 9343 · last release 2022-04-23 · [PyPI](https://pypi.org/project/strip-markdown/)

<details><summary>README extract</summary>

Example:
```python
>>> import strip_markdown
>>>
>>> TXT: str = strip_markdown.strip_markdown(MD: str)
>>> strip_markdown.strip_markdown_file(MD_fn: str, TXT_fn: Optional[str])
```

Sections: strip_markdown, Example, Markdown, Title, Section, Markdown source, Text, Usage, Command line, Library

</details>

### slackweb

slack bot for incomming webhook

`pip install slackweb` · installs from source (sdist only) · licence: MIT License · rank 9354 · last release 2015-06-23 · [PyPI](https://pypi.org/project/slackweb/)

### sssom-schema

SSSOM is a Simple Standard for Sharing Ontology Mappings.

`pip install sssom-schema` · installs (wheel) · licence: MIT License · rank 9366 · last release 2024-08-09 · [PyPI](https://pypi.org/project/sssom-schema/)

<details><summary>README extract</summary>

SSSOM is a Simple Standard for Sharing Ontological Mappings, providing

1. a TSV-based representation for ontology term mappings
1. a comprehensive set of standard metadata elements to describe mappings and
1. a standard translation between the TSV and the Web Ontology Language (OWL). ...

Sections: A Simple Standard for Sharing Ontological Mappings (SSSOM), Copying

</details>

### shazamio-core

Audio fingerprinting for Shazam, written in Rust and exposed to Python

`pip install shazamio-core` · installs (wheel) · licence: not stated · rank 9401 · last release 2026-10-11 · [PyPI](https://pypi.org/project/shazamio-core/) · [source](https://github.com/shazamio/shazamio-core)

<details><summary>README extract</summary>

Audio fingerprinting for Shazam, written in Rust and exposed to Python.

It turns an audio file, or its bytes, into the signature Shazam's endpoint accepts. It does not talk to Shazam itself: ShazamIO is the client that sends the signature and reads the answer back.

Example:
```python
import asyncio
from pathlib import Path

from shazamio_core import Recognizer

async def main() -> None:
    recognizer = Recognizer()

    from_path = await recognizer.recognize_path("track.mp3")
    from_bytes = await recognizer.recognize_bytes(Path("track.mp3").read_bytes())

    print(from_path.signature.uri == from_bytes.signature.uri)

...
```

Sections: shazamio-core, Usage, What comes back, How much audio is analysed, Errors, Formats

</details>

### suntime

Simple sunset and sunrise time calculation python library

`pip install suntime` · installs (wheel) · licence: LGPLv3 · rank 9408 · last release 2026-08-31 · [PyPI](https://pypi.org/project/suntime/)

_README extract left out: share-alike licence._

### simple-lama-inpainting

(no summary)

`pip install simple-lama-inpainting` · installs (wheel) · licence: not stated · rank 9433 · last release 2023-07-28 · [PyPI](https://pypi.org/project/simple-lama-inpainting/)

<details><summary>README extract</summary>

Simple pip package for LaMa[1] inpainting.

Example:
```python
from simple_lama_inpainting import SimpleLama
from PIL import Image

simple_lama = SimpleLama()

img_path = "image.png"
mask_path = "mask.png"

image = Image.open(img_path)
mask = Image.open(mask_path)

result = simple_lama(image, mask)
result.save("inpainted.png")
```

Sections: simple-lama-inpainting, Usage, CLI, Integration to Your Code, Sources

</details>

### spanishconjugator

A python library to conjugate spanish words with parameters tense, mood and pronoun

`pip install spanishconjugator` · installs (wheel) · licence: MIT License · rank 9468 · last release 2024-12-09 · [PyPI](https://pypi.org/project/spanishconjugator/)

<details><summary>README extract</summary>

A class Conjugator containing a function conjugate which conjugates spanish verbs by tense, mood and pronoun.

Example:
```python
from spanishconjugator import Conjugator
imperfect_conjugation = Conjugator().conjugate('hablar','imperfect','indicative','yo')
print(imperfect_conjugation)
>>> hablaba
```

Sections: Spanish Conjugator 🇪🇸, Example usage, Tenses, Moods and Pronouns implemented

</details>

### slugify

A generic slugifier.

`pip install slugify` · installs from source (sdist only) · licence: UNKNOWN · rank 9484 · last release 2010-12-07 · [PyPI](https://pypi.org/project/slugify/)

### sssom

Operations on SSSOM mapping tables

`pip install sssom` · installs (wheel) · licence: MIT · rank 9493 · last release 2026-10-29 · [PyPI](https://pypi.org/project/sssom/)

<details><summary>README extract</summary>

A Python library and command line interface (CLI) for working with
SSSOM (Simple Standard for Sharing Ontology Mappings).

Example:
```python
import sssom

# other SSSOM files can be found on
url = "

# TSV can be parsed into a mapping set dataframe object,
# which includes a pandas DataFrame, a curies.Converter,
# and metadata
msdf = sssom.parse_tsv(url)

# SSSOM comes with several "write" functions
sssom.write_tsv(msdf, "test.tsv")
sssom.write_json(msdf, "test.json")
...
```

Sections: Python Utilities for SSSOM, Getting Started, Documentation, Deploy documentation, Schema, Harvard Medical School

</details>

### serena-agent

A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities - the IDE for your agent

`pip install serena-agent` · installs (wheel) · licence: GPL-3.0-or-later · rank 9567 · last release 2026-10-19 · [PyPI](https://pypi.org/project/serena-agent/)

_README extract left out: share-alike licence._

### scikit-fuzzy

Fuzzy logic toolkit for SciPy

`pip install scikit-fuzzy` · installs (wheel) · licence: not stated · rank 9607 · last release 2024-08-22 · [PyPI](https://pypi.org/project/scikit-fuzzy/)

<details><summary>README extract</summary>

`scikit-fuzzy` is a fuzzy logic toolkit for SciPy.

The goals of scikit-fuzzy are:
* To provide the community with a robust toolkit of independently developed and
 implemented fuzzy logic algorithms
* To increase the attractiveness of scientific Python as a valid alternative to
 closed-source options.

Please cite
if you find scikit-fuzzy useful. ...

</details>

### simple-dwd-weatherforecast

A simple tool to retrieve a weather forecast from DWD OpenData

`pip install simple-dwd-weatherforecast` · installs (wheel) · licence: MIT License · rank 9727 · last release 2026-10-24 · [PyPI](https://pypi.org/project/simple-dwd-weatherforecast/)

<details><summary>README extract</summary>

[][buymecoffee]

DISCLAIMER: This project is a private open source project and doesn't have any connection with Deutscher Wetterdienst.

If you like my work, I would be really happy if you buy me some coffee: Buy Me A Coffee

This is a python package for simple access to hourly forecast data for the next 10 days. ...

Example:
```python
from simple_dwd_weatherforecast import dwdforecast
from datetime import datetime, timedelta, timezone

# Find nearest Station-ID automatically
# id = dwdforecast.get_nearest_station_id(50.1109221, 8.6821267)

dwd_weather = dwdforecast.Weather("10385") # Station-ID For BERLIN-SCHOENEFELD
time_now = datetime.now(timezone.utc)
...
```

...

</details>

### snowfakery

Snowfakery is a tool for generating fake data that has relations between tables. Every row is faked data, but also unique and random, like a snowflake.

`pip install snowfakery` · installs (wheel) · licence: BSD License · rank 9728 · last release 2026-01-09 · [PyPI](https://pypi.org/project/snowfakery/)

<details><summary>README extract</summary>

Snowfakery is a tool for generating fake data that has relations between tables. Every row is faked data, but also unique and random, like a snowflake.

To tell Snowfakery what data you want to generate, you need to write a Recipe file in YAML.

Snowfakery can write its output to stdout, or any database accessible to SQLAlchemy. ...

Sections: Snowfakery Documentation, Updating Dependencies

</details>

### shamir-mnemonic

SLIP-39 Shamir Mnemonics

`pip install shamir-mnemonic` · installs (wheel) · licence: MIT License · rank 9731 · last release 2024-05-16 · [PyPI](https://pypi.org/project/shamir-mnemonic/)

<details><summary>README extract</summary>

Reference implementation of SLIP-0039: Shamir's Secret-Sharing for Mnemonic
Codes

This SLIP describes a standard and interoperable implementation of Shamir's
secret sharing (SSS). ...

Sections: python-shamir-mnemonic, Abstract, Specification, CLI usage, Test vectors, 0.3.0 - 2024-05-15, Incompatible, Added, Changed, Removed, 0.2.2 - 2021-12-07, 0.2.1 - 2021-02-03, Fixed

</details>

### svql

Query SystemVerilog modules with SQL.

`pip install svql` · installs (wheel) · licence: MIT · rank 9775 · last release 2025-03-06 · [PyPI](https://pypi.org/project/svql/)

<details><summary>README extract</summary>

A Python tool for parsing and analyzing SystemVerilog modules using SQL queries.

Features:
svql provides a simple interface to extract and query information from SystemVerilog modules. It parses module parameters, ports, and their connections, storing them in SQL-queryable DataFrames.

Example:
```python
from svql import Module

# Parse a SystemVerilog module
module = Module("path/to/your/module.sv")

print(f"All parameters that have not been changed from default for {module.header}:")
print(module.query("SELECT * FROM params WHERE override_value IS NULL"), "\n")

# Expected Output:
...
```

Sections: svql: SystemVerilog Module Analysis Tool, Overview, Usage, Example 1: Query Parameters Not Changed from Default, Example 2: Query Input Ports

</details>

### searoute

A python package for generating the shortest sea route between two points on Earth.

`pip install searoute` · installs from source (sdist only) · licence: Apache Software License · rank 9782 · last release 2026-05-17 · [PyPI](https://pypi.org/project/searoute/) · [docs](https://github.com/genthalili/searoute-py/blob/main/README.md) · [source](https://github.com/genthalili/searoute-py)

<details><summary>README extract</summary>

A python package for generating the shortest sea route between two points on Earth.

If points are on land, the function will attempt to find the nearest point on the sea and calculate the route from there. ...

Example:
```python
sr.searoute(..., backend = "igraph")  # build the network with igraph

m = Marnet()                          # defaults to networkx
m = Marnet(backend="networkx")        # explicit networkx
m = Marnet(backend="igraph")          # igraph (if installed)
```

Sections: Searoute py, Usage, Define origin and destination points, > Returns a GeoJSON LineString Feature, show route distance with unit, Graph backend, Bring your network, Nodes and Edges, Nodes, Edges, Example with more parameters, Using all parameters, wil include ports as well, Preferred Ports

</details>

### sandbox-fusion

Client package of Sandbox Fusion service

`pip install sandbox-fusion` · installs (wheel) · licence: Apache Software License · rank 9885 · last release 2025-01-06 · [PyPI](https://pypi.org/project/sandbox-fusion/)

### spec-kitty-events

Event log library with Lamport clocks and systematic error tracking

`pip install spec-kitty-events` · installs (wheel) · licence: MIT License · rank 9952 · last release 2026-10-27 · [PyPI](https://pypi.org/project/spec-kitty-events/)

<details><summary>README extract</summary>

Package Version: `11.3.0` | Envelope Schema Version: `3.0.0` | Python: `>=3.10`

The event contracts of Spec Kitty: the canonical vocabulary the Spec Kitty CLI and
runtime emit as a Mission moves through its lifecycle. This repository is the
event-contract surface of the Build Kitty
product line — the free CLI and its extension surface. ...

Example:
```python
import uuid
from datetime import datetime, timezone

from spec_kitty_events import Event

event = Event(
    event_id="01ARZ3NDEKTSV4RRFFQ69G5FAV",
    event_type="WPStatusChanged",
    aggregate_id="mission/WP01",
    payload={
        "mission_slug": "mission-001",
        "wp_id": "WP01",
        "from_lane": "planned",
...
```

...

</details>

### sagemaker-containers

Open source library for creating containers to run on Amazon SageMaker.

`pip install sagemaker-containers` · installs from source (sdist only) · licence: Apache Software License · rank 9954 · last release 2020-06-22 · [PyPI](https://pypi.org/project/sagemaker-containers/)

<details><summary>README extract</summary>

SageMaker Containers gives you tools to create SageMaker-compatible Docker containers, and has additional tools for letting you create Frameworks
(SageMaker-compatible Docker containers that can run arbitrary Python or shell scripts).

Currently, this library is used by the SageMaker Scikit-learn containers.

Example:
```python
import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
...
```

...

</details>

### sftpretty

Pretty secure file transfer made easy.

`pip install sftpretty` · installs (wheel) · licence: BSD License · rank 10048 · last release 2026-09-25 · [PyPI](https://pypi.org/project/sftpretty/) · [docs](https://docs.sftpretty.com) · [source](https://github.com/byteskeptical/sftpretty)

<details><summary>README extract</summary>

A pretty quick and simple interface to paramiko SFTP. Provides multi-threaded
routines with progress notifications for reliable, asynchronous transfers. A
Python3 optimized fork of pysftp with additional features & improvements. ...

Example:
```python
from sftpretty import CnOpts, Connection

# Basic

with Connection('hostname', username='me', password='secret') as sftp:
    # Temporarily chdir to public/.
    with sftp.cd('public'):
        # Upload file to public/ on remote.
        sftp.put('/my/local/filename')
        # Download a remote file from public/.
        sftp.get('remote_file')

...
```

Sections: sftpretty, Example, Additional Information, Requirements

</details>

### subprocess.run

The subprocess module extension to run processes.

`pip install subprocess.run` · installs from source (sdist only) · licence: BSD License · rank 10070 · last release 2013-11-16 · [PyPI](https://pypi.org/project/subprocess.run/)

<details><summary>README extract</summary>

The subprocess extension to run processes.

To use pipe from the shell.

Example:
```python
>>> from subprocess import run

>>> run('uname -r').stdout
3.7.0-7-generic

>>> run('uname -a').status
0

>>> print run('rm not_existing_directory').stderr
rm: cannot remove `not_existing_directory': No such file or directory

>>> print run('ls -la', 'wc -l')
14
```

Sections: from subprocess import run, Tests

</details>

### spec-kitty-tracker

Universal tracker interface, connector SDK, and sync engine for Spec Kitty

`pip install spec-kitty-tracker` · installs (wheel) · licence: MIT License · rank 10079 · last release 2026-09-01 · [PyPI](https://pypi.org/project/spec-kitty-tracker/)

<details><summary>README extract</summary>

Shared task-tracker abstraction layer for Spec Kitty CLI and SaaS.

1. Canonical issue model (`CanonicalIssue`, `ExternalRef`, `CanonicalLink`)
2. Tracker connector protocol with capability negotiation
3. Doctrine-style source-of-truth ownership policies
4. Conflict resolution and deterministic sync engine
5. ...

Example:
```python
import asyncio
from spec_kitty_tracker import (
    create_hosted_connector,
    HostedConnectorRequest,
    LinearHostedParams,
    NangoConnectionContext,
    InMemoryIssueStore,
    OwnershipPolicy,
    OwnershipMode,
    SyncEngine,
)

async def main() -> None:
    # SaaS host provides identity context per operation
...
```

...

</details>

### snaptime

Transform timestamps with a simple DSL

`pip install snaptime` · installs from source (sdist only) · licence: UNKNOWN · rank 10083 · last release 2017-06-15 · [PyPI](https://pypi.org/project/snaptime/)

### sb3-contrib

Contrib package of Stable Baselines3, experimental code.

`pip install sb3-contrib` · installs (wheel) · licence: MIT · rank 10115 · last release 2026-10-26 · [PyPI](https://pypi.org/project/sb3-contrib/) · [docs](https://sb3-contrib.readthedocs.io/) · [source](https://github.com/Stable-Baselines-Team/stable-baselines3-contrib)

<details><summary>README extract</summary>

Contrib package for Stable-Baselines3 - Experimental reinforcement learning (RL) code.
"sb3-contrib" for short.

A place for RL algorithms and tools that are considered experimental, e.g. implementations of the latest publications. Goal is to keep the simplicity, documentation and style of stable-baselines3 but for less matured implementations.

Features:
Over the span of stable-baselines and stable-baselines3, the community has been eager to contribute in form of better logging utilities, environment wrappers, extended support (e.g. different action spaces) and learning algorithms. ...

Sections: Stable-Baselines3 - Contrib (SB3-Contrib), What is SB3-Contrib?, Why create this repository?, Features, Documentation

</details>

### savepagenow

A simple Python wrapper and command-line interface for archive.org’s "Save Page Now" capturing service

`pip install savepagenow` · installs (wheel) · licence: MIT License · rank 10152 · last release 2026-01-19 · [PyPI](https://pypi.org/project/savepagenow/) · [docs](http://palewi.re/docs/savepagenow) · [source](https://github.com/palewire/savepagenow)

<details><summary>README extract</summary>

- Documentation: palewi.re/docs/savepagenow/
- Save Page Now at archive.org: archive.org/web
- Code: github.com/palewire/savepagenow
- Issues: github.com/palewire/savepagenow/issues
- Packaging: pypi.org/project/savepagenow

</details>

### sarj-standards

Compatibility bridge to the renamed code-standards distribution.

`pip install sarj-standards` · installs (wheel) · licence: MIT · rank 10157 · last release 2026-11-08 · [PyPI](https://pypi.org/project/sarj-standards/) · [docs](https://code-standards.sarj.ai/cli/) · [source](https://github.com/sarj-ai/code-standards)

<details><summary>README extract</summary>

<!-- Generated by `code-standards maintain docs sync`; do not edit. -->

Compatibility bridge to the renamed code-standards distribution.

Compatibility bridge for existing exact launchers after the distribution was renamed to `code-standards`. New installations should use `code-standards` directly.

Documentation · Source

</details>

### syntaqlite

Python API for libsyntaqlite: parse, format, and statically analyze SQLite SQL

`pip install syntaqlite` · installs (wheel) · licence: Apache-2.0 · rank 10166 · last release 2026-11-05 · [PyPI](https://pypi.org/project/syntaqlite/) · [docs](https://docs.syntaqlite.com)

<details><summary>README extract</summary>

libsyntaqlite is a fast, embeddable parser, formatter, and static analyzer for SQLite SQL. The `syntaqlite` package provides its Python API.

Docs · Playground · GitHub

The package requires Python 3.10 or later. Wheels are available for Linux
(x86_64, aarch64), macOS (x86_64, arm64), and Windows (x86_64). ...

Example:
```python
import syntaqlite

with syntaqlite.Syntaqlite() as sq:
    print(sq.format_sql("select 1"))
```

Sections: libsyntaqlite for Python, API, Formatting, Parsing, Tokenizing, Analysis, Column lineage, CLI

</details>

### sumtypes

Algebraic types for Python (notably providing Sum Types, aka Tagged Unions)

`pip install sumtypes` · installs (wheel) · licence: MIT License · rank 10179 · last release 2021-11-30 · [PyPI](https://pypi.org/project/sumtypes/)

<details><summary>README extract</summary>

sumtypes provides Algebraic Data Types for Python. The main benefit is the
implementation of Sum Types (aka Tagged Unions), which Python doesn't have
any native representation for. Product Types are just objects with multiple
attributes.

Documentation is at ...

Example:
```python
import attr
from sumtypes import sumtype, constructor, match

@sumtype
class MyType(object):
    # constructors specify names for their arguments
    MyConstructor = constructor('x')
    AnotherConstructor = constructor('x', 'y')

    # You can also make use of any feature of the attrs
    # package by using attr.ib in constructors
...
```

Sections: sumtypes, Example, See Also

</details>

### seqlog

SeqLog enables logging from Python to Seq.

`pip install seqlog` · installs (wheel) · licence: MIT License · rank 10180 · last release 2025-08-26 · [PyPI](https://pypi.org/project/seqlog/)

<details><summary>README extract</summary>

SeqLog enables logging from Python to Seq.

It also adds support for logging with named format arguments (via keyword arguments) in the same way `"{arg1}".format(arg1="foo")` does.

* Free software: MIT license

Sections: SeqLog, 0.4.3 (2025-07-26), 0.4.2 (2025-07-26), 0.4.1 (2025-05-11), 0.4.0 (2024-12-08), 0.3.31 (2024-04-27), 0.3.30 (2023-10-28), 0.3.29 (2023-08-24), 0.3.28 (2023-08-13), 0.3.27 (2023-08-03), 0.3.26 (2023-04-20), 0.3.25 (2023-04-18), 0.3.24 (2023-04-14), 0.3.22 (TBA)

</details>

### standardjson

JSON encoder that aims to be fully compliant with specifications ECMA-262 and ECMA-404.

`pip install standardjson` · installs (wheel) · licence: BSD License · rank 10211 · last release 2014-05-21 · [PyPI](https://pypi.org/project/standardjson/)

<details><summary>README extract</summary>

JSON encoder fully compliant with the ECMA-262 and ECMA-404 specifications.

* Free software: BSD license

Features:
Support for all objects that the Python stdlib's `json.JSONEncoder` can encode, plus:

* `datetime.datetime`
* `datetime.date`
* `datetime.time`
* `decimal.Decimal`

Works on Python 2.6, 2.7, 3.3. ...

Example:
```python
>>> import datetime
>>> import json
>>> from standardjson import StandardJSONEncoder

>>> json.dumps({'day': datetime.date(2010, 2, 17)}, cls=StandardJSONEncoder)
'{"day": "2010-02-17"}'
```

Sections: standardjson, Features, Quickstart, 0.3.1 (2014-05-21), 0.3.0 (2014-05-21), 0.2.0 (2014-05-20), 0.1.0 (2014-05-18)

</details>

### sip

A Python bindings generator for C/C++ libraries

`pip install sip` · installs (wheel) · licence: BSD-2-Clause · rank 10246 · last release 2026-10-26 · [PyPI](https://pypi.org/project/sip/)

<details><summary>README extract</summary>

One of the features of Python that makes it so powerful is the ability to take
existing libraries, written in C or C++, and make them available as Python
extension modules. Such extension modules are often called bindings for the
library.

SIP is a collection of tools that makes it very easy to create Python bindings
for C and C++ libraries. ...

Sections: SIP - A Python Bindings Generator for C and C++ Libraries, Documentation, Creating Packages for Distribution, Building the Documentation

</details>

### surya-ocr

OCR, layout, reading order, and table recognition in 90+ languages.

`pip install surya-ocr` · installs (wheel) · licence: Apache-2.0 · rank 10269 · last release 2026-10-29 · [PyPI](https://pypi.org/project/surya-ocr/) · [source](https://github.com/datalab-to/surya)

<details><summary>README extract</summary>

State of the Art models for Document Intelligence

Surya is a 689M param OCR model with these features:

- Accuracy - scores 85.9 on OmniParseBench, the highest of the open models under 1B parameters we have scored, and 83.7% on olmOCR-bench
- Speed - throughput of 4.5 pages/s on one H100 at 192 DPI, 1.7x Surya 2 with MTP (see Throughput) ...

Example:
```python
# v2
from surya.inference import SuryaInferenceManager
from surya.recognition import RecognitionPredictor

manager = SuryaInferenceManager()              # auto-spawns vllm or llama-server
rec = RecognitionPredictor(manager)
predictions = rec([image])
```

...

</details>

### soda-core-duckdb

(no summary)

`pip install soda-core-duckdb` · installs (wheel) · licence: not stated · rank 10276 · last release 2025-09-24 · [PyPI](https://pypi.org/project/soda-core-duckdb/)

### swagger-ui-py

Swagger UI for Python web framework, such as Tornado, Flask, Quart, Sanic and Falcon.

`pip install swagger-ui-py` · installs (wheel) · licence: Apache License 2.0 · rank 10280 · last release 2025-07-01 · [PyPI](https://pypi.org/project/swagger-ui-py/)

<details><summary>README extract</summary>

Project Page

Swagger UI for Python web framework, such Tornado, Flask, Quart, aiohttp, Sanic and Falcon.

Only support Python3.

Example:
```python
from swagger_ui import api_doc
api_doc(app, config_path='./config/test.yaml', url_prefix='/api/doc', title='API doc')
```

Sections: swagger-ui-py, Usage, SwaggerUI Configuration, OAuth2 Configuration, Swagger UI, Swagger Editor, Update

</details>

### streamlit-authenticator

A secure authentication module to manage user access in a Streamlit application.

`pip install streamlit-authenticator` · installs (wheel) · licence: MIT License · rank 10323 · last release 2025-03-01 · [PyPI](https://pypi.org/project/streamlit-authenticator/)

<details><summary>README extract</summary>

A secure authentication module to manage user access in a Streamlit application

> [!TIP]
> Looking for enterprise support for your Streamlit apps? Check out the Ploomber platform!

Example:
```python
import yaml
from yaml.loader import SafeLoader

with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# stauth.Hasher.hash_passwords(config['credentials'])

authenticator = stauth.Authenticate(
    config['credentials'],
    config'cookie',
    config'cookie',
...
```

...

</details>

### streamlit-antd-components

streamlit customer components of Antd Design and Mantine

`pip install streamlit-antd-components` · installs (wheel) · licence: not stated · rank 10329 · last release 2024-01-19 · [PyPI](https://pypi.org/project/streamlit-antd-components/)

<details><summary>README extract</summary>

[][share_link]
[][github_link]
[][pypi_link]
[][download_link]

A Streamlit custom component to implement Antd-Design and Mantine widgets.

Check out the Demo App for more example.

This library now provides component blow:

- `buttons` A group of buttons component.
- `divider` A divider line separates different content ...

Example:
```python
import streamlit as st
import streamlit_antd_components as sac

btn = sac.buttons(
    items=['button1', 'button2', 'button3'],
    index=0,
    format_func='title',
    align='center',
    direction='horizontal',
    radius='lg',
    return_index=False,
)
st.write(f'The selected button label is: {btn}')
```

Sections: Streamlit-Antd-Components, Quickstart, Todo

</details>

### slack-types

Slack API Types in Python

`pip install slack-types` · installs (wheel) · licence: MIT · rank 10356 · last release 2026-07-27 · [PyPI](https://pypi.org/project/slack-types/)

<details><summary>README extract</summary>

Pydantic v2 type definitions for the Slack APIs:

- Web API (`slack_types.web_api`)
- Events API (`slack_types.events_api`)
- Real Time Messaging API (`slack_types.rtm_api`)
- App backend payloads (`slack_types.app_backend.{dialogs,interactive_components,slash_commands,views}`)
- Audit Logs API (`slack_types.audit_api.v1`) ...

Example:
```python
from typing import Callable

from slack_bolt.async_app import AsyncApp
from slack_sdk.web.async_client import AsyncWebClient
from slack_types.events_api.app_mention_payload import Event as AppMentionEvent

app = AsyncApp()

@app.event("app_mention")
async def handle_mentions(event: dict, client: AsyncWebClient, say: Callable):
...
```

Sections: slack-types, Use, How types are generated

</details>

### semsql

(no summary)

`pip install semsql` · installs (wheel) · licence: not stated · rank 10452 · last release 2025-02-05 · [PyPI](https://pypi.org/project/semsql/)

<details><summary>README extract</summary>

This project provides a standard collection of SQL tables/views for ontologies, such that you can make queries like this,
to find all terms starting with `Abnormality` in HPO.

|stanza|subject|predicate|object|value|datatype|language| ...

Example:
```python
engine = create_engine(f"sqlite:////path/to/go.db")
SessionClass = sessionmaker(bind=engine)
session = SessionClass()
q = session.query(RdfsSubclassOfStatement)
q = q.add_entity(OwlSomeValuesFrom)
q = q.join(OwlSomeValuesFrom, RdfsSubclassOfStatement.object == OwlSomeValuesFrom.id)

lines = []
for ax, ex in q.all():
...
```

...

</details>

### suntimes

For a given place (longitude, latitude and altitude) and a given day, returns the time of sunrise and the time of sunset (in UTC and in local time). Create and save a json or csv file with the timetables for a whole year. Calculations valid beyond the polar circles; returns Polar Day or Polar Night if needed.

`pip install suntimes` · installs (wheel) · licence: MIT License · rank 10464 · last release 2022-07-01 · [PyPI](https://pypi.org/project/suntimes/)

<details><summary>README extract</summary>

Calculation of sunrise and sunset time for a location (longitude, latitude, altitude) with python. Calculations valid beyond the polar circles ; returns Polar Day or Polar Night if necessary. Sunrise and sunset times also available for an entire year as a json or csv file. ...

Example:
```python
A place is characterized by longitude, latitude, altitude
- longitude: float between -180 and 180 ; negative for west longitudes, positive for east longitudes
- latitude: float between -90 and 90 ; positive if north, negative if south
- altitude: float, in meters; greater than or equal to zero. Default = 0.

# Methods
...
```

...

</details>

### specify-cli

Specify CLI, part of GitHub Spec Kit. A tool to bootstrap your projects for Spec-Driven Development (SDD).

`pip install specify-cli` · installs (wheel) · licence: not stated · rank 10473 · last release 2026-11-06 · [PyPI](https://pypi.org/project/specify-cli/)

<details><summary>README extract</summary>

English ·
 简体中文 ·
 日本語 ·
 한국어

Spec Kit is an open source toolkit that gives AI coding agents structured
processes, reusable templates, and documented outcomes. Start with a ready-made
process, customize it, or bring your own.

| What you need | Process | Outcome | ...

Features:
Spec Kit combines ready-to-use processes with composable mechanisms:

| Capability | Spec Kit mechanism |

| Connect to or switch between coding agents | Integration |
| Add a command, quality gate, or complete process | Extension |
| Connect a ...

Sections: 🌱 Spec Kit, Choose your process, Capabilities, Get started, Bug fixing, Idea assessment, Customize or bring your own process, Documentation, In the news

</details>

### sphinx-remove-toctrees

Reduce your documentation build size by selectively removing toctrees from pages.

`pip install sphinx-remove-toctrees` · installs (wheel) · licence: MIT License · rank 10475 · last release 2024-03-22 · [PyPI](https://pypi.org/project/sphinx-remove-toctrees/)

<details><summary>README extract</summary>

Sections: Who is this for?, Use, Try it with this documentation, How this works

</details>

### stepfunctions

Open source library for developing data science workflows on AWS Step Functions.

`pip install stepfunctions` · installs from source (sdist only) · licence: Apache Software License · rank 10481 · last release 2022-01-24 · [PyPI](https://pypi.org/project/stepfunctions/)

<details><summary>README extract</summary>

The AWS Step Functions Data Science SDK is an open-source library that allows data
scientists to easily create workflows that process and publish machine learning
models using Amazon SageMaker and AWS Step Functions. ...

Features:
The AWS Step Functions Data Science SDK provides a Python API that enables you to
create data science and machine learning workflows using AWS Step Functions and
SageMaker directly in your Python code and Jupyter notebooks.

Using this SDK you can: ...

Example:
```python
start_pass_state = Pass(
    state_id="MyPassState"
)
```

...

</details>

### slip10

A reference implementation of the SLIP-0010 specification, which generalizes the BIP-0032 derivation scheme for private and public key pairs in hierarchical deterministic wallets for the curves secp256k1, NIST P-256, ed25519 and curve25519.

`pip install slip10` · installs (wheel) · licence: BSD-3-Clause AND MIT · rank 10501 · last release 2026-02-02 · [PyPI](https://pypi.org/project/slip10/) · [source](https://github.com/trezor/python-slip10)

<details><summary>README extract</summary>

A reference implementation of the SLIP-0010 specification, which generalizes the BIP-0032 derivation scheme for private and public key pairs in hierarchical deterministic wallets for the curves secp256k1, NIST P-256, ed25519 and curve25519.

Example:
```python
>>> from slip10 import SLIP10, HARDENED_INDEX
>>> slip10 = SLIP10.from_seed(bytes.fromhex("01"))
# Specify the derivation path as a list ...
>>> slip10.get_xpriv_from_path([1, HARDENED_INDEX, 9998])
'xprv9y4sBgCuub5x2DtbdNBDDCZ3btybk8YZZaTvzV5rmYd3PbU63XLo2QEj6cUt4JAqpF8gJiRKFUW8Vm7thPkccW2DpUvBxASycypEHxmZzts'
# ... Or in usual m/the/path/
...
```

...

</details>

### smtpapi

Simple wrapper to use SendGrid SMTP API

`pip install smtpapi` · installs (wheel) · licence: MIT License · rank 10513 · last release 2022-03-09 · [PyPI](https://pypi.org/project/smtpapi/)

<details><summary>README extract</summary>

This module helps build SendGrid's SMTP API headers.

Learn more about the SMTP API at SendGrid documentation.

The default branch name for this repository has been changed to `main` as of 07/27/2020.

All the updates to this module are documented in our CHANGELOG.

Example:
```python
from smtpapi import SMTPAPIHeader

header = SMTPAPIHeader()
header.add_to('email@email.com')
print(header.json_string())
```

Sections: Announcements, Prerequisites, Setup Environment Variables, Quick Start, Usage, Local Setup of the Project, About

</details>

### st-annotated-text

A simple component to display annotated text in Streamlit apps.

`pip install st-annotated-text` · installs (wheel) · licence: Apache Software License · rank 10564 · last release 2025-01-23 · [PyPI](https://pypi.org/project/st-annotated-text/)

<details><summary>README extract</summary>

A simple component to display annotated text in Streamlit apps. For example:

Or, even better, check out our demo app here:

Example:
```python
import streamlit as st
from annotated_text import annotated_text

annotated_text(
    "This ",
    ("is", "verb"),
    " some ",
    ("annotated", "adj"),
    ("text", "noun"),
    " for those of ",
    ("you", "pronoun"),
    " who ",
    ("like", "verb"),
    " this sort of ",
    ("thing", "noun"),
    "."
)
```

Sections: Annotated Text Component for Streamlit, Example, Parameters

</details>

### serialx

Serial library with native sync and async support for Windows, Linux, macOS, and other platforms

`pip install serialx` · installs (wheel) · licence: Apache-2.0 · rank 10568 · last release 2026-10-27 · [PyPI](https://pypi.org/project/serialx/) · [docs](https://puddly.github.io/serialx/) · [source](https://github.com/puddly/serialx)

<details><summary>README extract</summary>

Serialx is a no-compromise serial communication library for Python targeting common
platforms such as Linux (POSIX), macOS, and Windows. It provides both synchronous and
native asynchronous APIs for all platforms.

For more information, visit serialx's documentation:

Example:
```python
import serialx

with serialx.serial_for_url("/dev/serial/by-id/port", baudrate=115200) as serial:
    data = serial.readexactly(5)
    serial.write(b"test")

    serial.set_modem_pins(rts=True, dtr=True)
    pins = serial.get_modem_pins()
    assert pins.rts is serialx.PinState.HIGH
    assert pins.dtr is serialx.PinState.HIGH
```

Sections: Introduction, Usage, ESPHome serial proxy

</details>

### scarf-sdk

Python bindings for Scarf telemetry

`pip install scarf-sdk` · installs (wheel) · licence: not stated · rank 10576 · last release 2025-12-31 · [PyPI](https://pypi.org/project/scarf-sdk/)

<details><summary>README extract</summary>

A Python client for sending telemetry events to Scarf using JSON payloads.

Features:
- Simple API for sending telemetry events
- JSON payloads (supports nested data)
- Environment variable configuration
- Configurable timeouts (default: 3 seconds)
- Respects user Do Not Track settings
- Verbose logging mode for debugging

Example:
```python
from scarf import ScarfEventLogger

# Initialize with required endpoint URL
logger = ScarfEventLogger(
    endpoint_url="
    timeout=5.0  # Optional: Set default timeout in seconds (default: 3.0)
)

# Send an event with properties
success = logger.log_event({
    "event": "package_download",
    "package": "scarf",
    "details": {
...
```

Sections: scarf-py, Usage, Configuration, Features, Publishing

</details>

### spire-xls

A 100% standalone Excel Python API for Processing Excel Files

`pip install spire-xls` · installs (wheel) · licence: Free To Use But Restricted; Other/Proprietary License · rank 10603 · last release 2026-08-25 · [PyPI](https://pypi.org/project/spire-xls/)

<details><summary>README extract</summary>

Product Page | Documentation | Examples | Forum | Temporary License | Customized Demo

Spire.XLS for Python is a powerful Python Excel API that can be used to create, read, write, and convert Excel spreadsheets in any type of Python applications without installing Microsoft Office. ...

Example:
```python
from spire.xls.common import *
from spire.xls import *

outputFile = "CreateAnExcelWithFiveSheet.xlsx"

# Create an object of Workbook class
workbook = Workbook()

# Add five sheets to this file
workbook.CreateEmptySheets(5)

# Loop through the added worksheets
for i in range(0, 5):
    sheet = workbook.Worksheets[i]
...
```

...

</details>

### substrate-interface

Library for interfacing with a Substrate node

`pip install substrate-interface` · installs (wheel) · licence: Apache Software License · rank 10618 · last release 2026-01-20 · [PyPI](https://pypi.org/project/substrate-interface/)

<details><summary>README extract</summary>

This library specializes in interfacing with a Substrate node; querying storage, composing extrinsics,
SCALE encoding/decoding and providing additional convenience methods to deal with the features and metadata of
the Substrate runtime.

* Library documentation
* Metadata documentation for Polkadot and Kusama ecosystem runtimes

Example:
```python
substrate = SubstrateInterface(chainspec="polkadot_asset_hub", relay_chainspecs=["polkadot"])
```

Sections: Python Substrate Interface, Description, Documentation, Initialization, Quick usage, Balance information of an account, Create balance transfer extrinsic

</details>

### soft-webauthn

Python webauthn software authenticator

`pip install soft-webauthn` · installs (wheel) · licence: MIT License · rank 10757 · last release 2022-07-08 · [PyPI](https://pypi.org/project/soft-webauthn/)

<details><summary>README extract</summary>

Package is used for testing webauthn enabled web applications. The use-case is
authenticator and browser emulation during web application development
continuous integration.

`SoftWebauthnDevice` class interface exports basic navigator interface used for
webauthn features: ...

Sections: Python software webauthn token, References

</details>

### spatial_image

A multi-dimensional spatial image data structure for scientific Python.

`pip install spatial_image` · installs (wheel) · licence: MIT License · rank 10766 · last release 2025-08-08 · [PyPI](https://pypi.org/project/spatial_image/)

<details><summary>README extract</summary>

A multi-dimensional spatial image data structure for scientific Python.

To facilitate:

- Multi-scale processing and analysis
- Registration
- Resampling
- Subregion parallel processing
- Coupling with meshes, point sets, and annotations ...

Sections: spatial-image, Definitions, Data Dimensions, Axis attributes, Coordinates, Motivational Notes

</details>

### spatialdata

Spatial data format.

`pip install spatialdata` · installs (wheel) · licence: not stated · rank 10807 · last release 2026-07-02 · [PyPI](https://pypi.org/project/spatialdata/) · [docs](https://spatialdata.scverse.org/en/latest) · [source](https://github.com/scverse/spatialdata.git)

<details><summary>README extract</summary>

[][link-tests]

[][link-pypi]

SpatialData is a data framework, a schema and a serialization format for uni- and multi-modal spatial omics datasets. It is supported by a growing suite of software libraries for performant access, manipulation and analysis in multiple languages, including Python, R and JavaScript. ...

Sections: Getting started, Limitations, Contact

</details>

### sphinx-comments

Add comments and annotation to your documentation.

`pip install sphinx-comments` · installs (wheel) · licence: MIT License · rank 10842 · last release 2020-08-12 · [PyPI](https://pypi.org/project/sphinx-comments/)

<details><summary>README extract</summary>

Add comments and annotation functionality to your Sphinx website.

Currently, these commenting engines are supported:

- Hypothes.is provides a web overlay that allows you to annotate and comment collaboratively.
- utteranc.es is a web commenting system that uses GitHub Issues to store and manage comments. ...

Sections: Sphinx Comments, Repository structure

</details>

### smplx

PyTorch module for loading the SMPLX body model

`pip install smplx` · installs (wheel) · licence: not stated · rank 10855 · last release 2021-05-26 · [PyPI](https://pypi.org/project/smplx/)

<details><summary>README extract</summary>

[Paper Page] [Paper]
[Supp. Mat.]

Sections: Disclaimer, Description, News, Downloading the model, Loading SMPL-X, SMPL+H and SMPL, SMPL and SMPL+H setup, Model loading, MANO and FLAME correspondences, Example, Modifying the global pose of the model, Facial Contour, Contact

</details>

### sqlalchemy-risingwave

RisingWave dialect for SQLAlchemy

`pip install sqlalchemy-risingwave` · installs (wheel) · licence: Apache Software License · rank 10900 · last release 2026-06-18 · [PyPI](https://pypi.org/project/sqlalchemy-risingwave/) · [source](https://github.com/risingwavelabs/sqlalchemy-risingwave)

<details><summary>README extract</summary>

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

RisingWave is a cloud-native streaming database that uses SQL as the interface language. It is designed to reduce the complexity and cost of building real-time applications. ...

Sections: RisingWave dialect for SQLAlchemy, Prerequisites, Usage, SQLAlchemy compatibility, Safe fallbacks the dialect applies, User-declared invariants the dialect does NOT silently drop, Read-after-write, Where this fits in CI, Test, Ref

</details>

### saxoncee

Official Saxonica python package for the SaxonC-EE 13.1.1 processor: for XSLT 3.0, XQuery 3.1, XPath 3.1 and XML Schema processing.

`pip install saxoncee` · installs (wheel) · licence: not stated · rank 10945 · last release 2026-10-27 · [PyPI](https://pypi.org/project/saxoncee/) · [docs](https://www.saxonica.com/saxon-c/documentation13/index.html)

<details><summary>README extract</summary>

This is the official Saxonica Python wheel package for
Saxon, an XML document processor. SaxonC
provides APIs to run XSLT 3.0 transformations, XQuery 3.1 queries, XPath 3.1, and
XML Schema validation.

Features:
The main reason for using SaxonC in preference to other XML
tools available for Python is that it supports all the latest W3C
standards: XSLT 3.0, XPath 3.1, XQuery 3.1, and XSD 1.1.

Example:
```python
from saxoncee import *
```

Sections: Welcome to SaxonC-EE, SaxonC-EE, Why choose SaxonC?, What's new in this version?, About SaxonC, About Saxonica, Getting started, Example: Running a transformation, Using `pylint` on a project which uses `saxoncee`

</details>

### streamlit-code-editor

React-ace editor customized for Streamlit

`pip install streamlit-code-editor` · installs (wheel) · licence: not stated · rank 10952 · last release 2024-12-29 · [PyPI](https://pypi.org/project/streamlit-code-editor/)

<details><summary>README extract</summary>

A code editor component for streamlit.io apps, built on top of react-ace, with custom themes and customizable interface elements.

Example:
```python
import streamlit as st
from code_editor import code_editor

response_dict = code_editor(your_code_string)
```

Sections: streamlit code editor, Usage, Docs, Demo

</details>

### starlette-cramjam

Cramjam integration for Starlette ASGI framework.

`pip install starlette-cramjam` · installs (wheel) · licence: MIT License · rank 10978 · last release 2026-04-27 · [PyPI](https://pypi.org/project/starlette-cramjam/) · [source](https://github.com/developmentseed/starlette-cramjam)

<details><summary>README extract</summary>

Cramjam integration for Starlette ASGI framework.

Source Code:

The `starlette-cramjam` middleware aims to provide a unique Compression middleware to support Brotli, GZip, Deflate and ZSTD compression algorithms with a minimal requirement. ...

Example:
```python
import uvicorn

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import PlainTextResponse
from starlette.routing import Route

from starlette_cramjam.middleware import CompressionMiddleware

def index(request):
    return PlainTextResponse("Hello World")

app = Starlette(
...
```

Sections: starlette-cramjam, Usage, Minimal (defaults) example, Using options, Performance, Changes

</details>

### sphinx-jupyterbook-latex

Latex specific features for jupyter book

`pip install sphinx-jupyterbook-latex` · installs (wheel) · licence: BSD License · rank 11018 · last release 2023-12-11 · [PyPI](https://pypi.org/project/sphinx-jupyterbook-latex/)

<details><summary>README extract</summary>

Sphinx extension to support LaTeX infrastructure for Jupyter Book.

This repository is a development project to improve LaTeX support
in `Jupyter Book`.

To get started with `sphinx-jupyterbook-latex`, first install it through `pip`:

then, add `sphinx_jupyterbook_latex` to your extensions,
in a Sphinx `conf.py`: ...

Sections: sphinx-jupyterbook-latex, Get started, Extension Details

</details>

### sqlalchemy-serializer

Mixin for SQLAlchemy models serialization without pain

`pip install sqlalchemy-serializer` · installs (wheel) · licence: MIT License · rank 11026 · last release 2026-04-18 · [PyPI](https://pypi.org/project/sqlalchemy-serializer/) · [source](https://github.com/n0nSmoker/SQLAlchemy-serializer)

<details><summary>README extract</summary>

Mixin for SQLAlchemy models serialization without pain.

If you want to serialize SQLAlchemy model instances with only one line of code,
and tools like `marshmallow` seem to be redundant and too complex for such a simple task,
this mixin definitely suits you.

Contents
- Installation
- Usage
- Advanced usage
- Custom formats
- Custom types ...

Example:
```python
from sqlalchemy_serializer import SerializerMixin

class SomeModel(db.Model, SerializerMixin):
    ...
```

Sections: SQLAlchemy-serializer, Usage, Modern SQLAlchemy 2.0 Style, Advanced usage, Recursive models and trees, Custom formats, Custom types, Timezones, Helpers, serialize_collection, Troubleshooting, Max recursion, Controversial rules, Negative rules in ONLY section

</details>

### substrait-protobuf

Generated Substrait Protocol Buffer Code

`pip install substrait-protobuf` · installs (wheel) · licence: Apache-2.0 · rank 11057 · last release 2026-11-01 · [PyPI](https://pypi.org/project/substrait-protobuf/) · [source](https://github.com/substrait-io/substrait-packaging)

<details><summary>README extract</summary>

Generated Python protobuf bindings for the Substrait specification.

The protobuf definitions from which the code is generated can be found here.

Versions of this package correspond to Substrait releases. `vx.y.z` of substrait-protobuf will contain code generated from `vx.y.z` of the substrait repository.

Example:
```python
import substrait.algebra_pb2
import substrait.plan_pb2
import substrait.type_pb2
```

Sections: substrait-protobuf, Package Usage, Generation and Publishing, Local Generation

</details>

### spire-doc

A 100% standalone Word Python API for Processing Word Files

`pip install spire-doc` · installs (wheel) · licence: Free To Use But Restricted; Other/Proprietary License · rank 11076 · last release 2026-09-29 · [PyPI](https://pypi.org/project/spire-doc/)

<details><summary>README extract</summary>

Product Page | Documentation | Examples | Forum | Temporary License | Customized Demo

Spire.Doc for Python is a powerful and easy-to-use Word document processing library. It empowers developers to create, read, modify, and convert Word documents in Python applications without the need for Microsoft Word or any other third-party software.

Features:
Spire.Doc for Python provides a comprehensive set of features for working with various Word formats including DOC, DOCX, DOCM, DOT, DOTX, DOTM, and more.

The following list shows some key features offered by Spire.Doc for Python:
1. ...

Example:
```python
from spire.doc import *
from spire.doc.common import *

# Create a Document object
doc = Document()

# Add a section
section = doc.AddSection()

# Set the page margins
...

</details>

### shipyard-python-sdk

Shipyard Python SDK is an agent sandbox sdk

`pip install shipyard-python-sdk` · installs (wheel) · licence: not stated · rank 11094 · last release 2026-01-13 · [PyPI](https://pypi.org/project/shipyard-python-sdk/)

<details><summary>README extract</summary>

A Python SDK for interacting with Shipyard containerized execution environments.

Example:
```python
import asyncio
from shipyard_python_sdk import ShipyardClient, Spec, create_session_ship

async def main():
    # Option 1: Using client directly
    client = ShipyardClient(
        endpoint_url="
        access_token="your-token"
    )

    ship = await client.create_ship(
        ttl=3600,  # 1 hour
        spec=Spec(cpus=1.0, memory="512m"),
...
```

Sections: Shipyard Python SDK, Quick Start, File Structure, Components, ShipyardClient, SessionShip, Spec, Environment Variables, Error Handling, Examples

</details>

### strip-ansi

Strip ANSI escape sequences from a string

`pip install strip-ansi` · installs (wheel) · licence: not stated · rank 11102 · last release 2020-06-20 · [PyPI](https://pypi.org/project/strip-ansi/) · [source](https://github.com/ewen-lbh/python-strip-ansi)

<details><summary>README extract</summary>

Strip ANSI escape sequences from a string

Example:
```python
>>> from strip_ansi import strip_ansi
>>> strip_ansi("\033[38mLorem ipsum\033[0m")
"Lorem ipsum"
```

Sections: strip-ansi, Usage

</details>

### shipyard-neo-sdk

Python SDK for Shipyard Neo (Bay API)

`pip install shipyard-neo-sdk` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 11129 · last release 2026-03-05 · [PyPI](https://pypi.org/project/shipyard-neo-sdk/) · [source](https://github.com/AstrBotDevs/shipyard-neo)

_README extract left out: share-alike licence._

### subprocess-multitee

A small `tee` function for splitting stdout/stderr in subprocess, and a `subprocess.Popen` convenience wrapper

`pip install subprocess-multitee` · installs (wheel) · licence: not stated · rank 11154 · last release 2025-12-14 · [PyPI](https://pypi.org/project/subprocess-multitee/)

<details><summary>README extract</summary>

Multiplex subprocess stdout/stderr to multiple destinations simultaneously.

Features:
Standard `subprocess` forces a choice: either capture output (`stdout=PIPE`) or display it (`stdout=sys.stdout`). This library lets you do both—plus log to files, discard with `DEVNULL`, or any combination. ...

Example:
```python
from subprocess_multitee import Popen, tee, PIPE
import sys

# Capture output AND print to terminal in real-time
proc = Popen(['make'], stdout=tee(PIPE, sys.stdout))
output = proc.stdout.read()
proc.wait()
```

...

</details>

### streamlit-ace

Ace editor component for Streamlit.

`pip install streamlit-ace` · installs (wheel) · licence: MIT · rank 11180 · last release 2021-12-07 · [PyPI](https://pypi.org/project/streamlit-ace/)

<details><summary>README extract</summary>

[][github_link] [][pypi_link]

Example:
```python
import streamlit as st

from streamlit_ace import st_ace

# Spawn a new Ace editor
content = st_ace()

# Display editor's content as you type
content
```

Sections: 📝 Streamlit Ace, Getting started, Demo

</details>

### serverless-wsgi

Amazon AWS API Gateway WSGI wrapper

`pip install serverless-wsgi` · installs (wheel) · licence: MIT License · rank 11229 · last release 2025-06-11 · [PyPI](https://pypi.org/project/serverless-wsgi/)

<details><summary>README extract</summary>

A Serverless Framework plugin to build your deploy Python WSGI applications using Serverless. Compatible
WSGI application frameworks include Flask, Django and Pyramid - for a complete list, see:

Features:
- Transparently converts API Gateway and ALB requests to and from standard WSGI requests
- Supports anything you'd expect from WSGI such as redirects, cookies, file uploads etc. ...

Example:
```python
import app  # Replace with your actual application
import serverless_wsgi

# If you need to send additional content types as text, add then directly
# to the whitelist:

# serverless_wsgi.TEXT_MIME_TYPES.append("application/custom+json")

def handler(event, context):
    return serverless_wsgi.handle_request(app.app, event, context)
```

...

</details>

### signedjson

Sign JSON with Ed25519 signatures

`pip install signedjson` · installs (wheel) · licence: not stated · rank 11258 · last release 2022-03-29 · [PyPI](https://pypi.org/project/signedjson/)

<details><summary>README extract</summary>

Signs JSON objects with ED25519 signatures.

Features:
* More than one entity can sign the same object.
* Each entity can sign the object with more than one key making it easier to
 rotate keys
* ED25519 can be replaced with a different algorithm. ...

Example:
```python
from signedjson.key import generate_signing_key, get_verify_key
from signedjson.sign import (
    sign_json, verify_signed_json, SignatureVerifyException
)

signing_key = generate_signing_key('zxcvb')
signed_json = sign_json({'my_key': 'my_data'}, 'Alice', signing_key)

verify_key = get_verify_key(signing_key)

try:
...
```

Sections: Signed JSON, Features, Using, Format

</details>

### sqlbuild

Typed, test-first SQL pipelines with local E2E testing

`pip install sqlbuild` · installs (wheel) · licence: not stated · rank 11265 · last release 2026-11-08 · [PyPI](https://pypi.org/project/sqlbuild/)

<details><summary>README extract</summary>

The refactorable warehouse. Verify early, test properly, and refactor safely.

 Website ·
 Docs ·
 Quickstart ·
 Roadmap

Change your warehouse as often as your code. SQLBuild brings compile-time checks, end-to-end tests
and safe renames to your SQL, so change stops being risky. ...

Example:
```python
# models/marts/_sqlbuild/_macros/python/currency.py
def cents_to_dollars(column: str) -> str:
    """Convert a cents integer column to a dollars decimal with two decimal places."""
    return f"ROUND(({column}) / 100.0, 2)"
```

...

</details>

### signalrcore

Python SignalR Core full client (transports and encodings). Compatible with azure / serverless functions. Also with automatic reconnect and manually reconnect.

`pip install signalrcore` · installs (wheel) · licence: MIT · rank 11271 · last release 2026-11-03 · [PyPI](https://pypi.org/project/signalrcore/) · [docs](https://mandrewcito.github.io/signalrcore/) · [source](https://github.com/mandrewcito/signalrcore)

<details><summary>README extract</summary>

Python signalr core client library, made by a guy born in Vilalba (Lugo).

Feature list:
* All kind of communications with the server (streaming, sending messages)
* All transports implemented (sse, long polling and web sockets)
* All encodings (text, binary - msgpack)
* Authentication
* Automatic reconnection with different strategies
* Custom ...

Example:
```python
import logging
import sys
from signalrcore.hub_connection_builder import HubConnectionBuilder

def input_with_default(input_text, default_value):
    value = input(input_text.format(default_value))
    return default_value if value is None or value.strip() == "" else value

...
```

...

</details>

### simplegmail

A simple Python API client for Gmail.

`pip install simplegmail` · installs (wheel) · licence: MIT · rank 11296 · last release 2026-08-17 · [PyPI](https://pypi.org/project/simplegmail/)

<details><summary>README extract</summary>

A small Python client for sending, retrieving, and modifying messages through
the Gmail API.

simplegmail supports:

- plain-text and HTML messages;
- file attachments, Cc, Bcc, aliases, and Gmail signatures;
- standard-library `EmailMessage` objects, drafts, and threaded replies;
- Gmail search queries and common inbox filters; ...

Example:
```python
from simplegmail import Gmail

gmail = Gmail()
```

Sections: simplegmail, Google OAuth setup, Sending messages, Standard-library EmailMessage, Threaded replies, Drafts, Retrieving messages, Labels and message state, Attachments, Search queries, Errors and resource cleanup, Upgrading to 5.0

</details>

### setuptools-markdown

[Deprecated] Use Markdown for your project description

`pip install setuptools-markdown` · installs (wheel) · licence: MIT · rank 11298 · last release 2019-08-14 · [PyPI](https://pypi.org/project/setuptools-markdown/)

<details><summary>README extract</summary>

Use Markdown for your
project description

**Instead of using this, you should use the built-in functionality of
setuptools and PyPI.**

See this page
for details.

Example:
```python
# !/usr/bin/env python
# setup.py

from setuptools import setup

setup(
    ...
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',
    ...
)
```

Sections: setuptools-markdown, This project is deprecated., Use

</details>

### sentry-protos

Generated python code for sentry-protos

`pip install sentry-protos` · installs (wheel) · licence: not stated · rank 11306 · last release 2026-11-06 · [PyPI](https://pypi.org/project/sentry-protos/) · [source](https://github.com/getsentry/sentry-protos)

<details><summary>README extract</summary>

This package contains the generated code from the sentry-protos project for python.

:warning: All code within `py/sentry_protos` is generated by tooling in the containing project and should not be modified by hand. :warning:

</details>

### sxtwl

sxtwl_cpp warpper for python

`pip install sxtwl` · installs from source (sdist only) · licence: BSD · rank 11387 · last release 2024-09-06 · [PyPI](https://pypi.org/project/sxtwl/)

<details><summary>README extract</summary>

sxtwl_cpp是参考寿星天文历并使用C++实现日历库。因为其依据天文历法算法实现，故其可查询范围广(BC722年以后与实历相符，支持1800年以前及2200年以后的日历查询)。支持Android、IOS、Windows、MacOS、Linux等平台。使用swig暴露接口给python,lua,java等语言使用。

旧工程代码兼容
如果有已使用V1.x版本的工程，想兼容代码
或者在requirements.txt里修改

具体使用方法参考：

本项目 GitHub / Gitee（码云）。

<font color='red'> 注:因为pip上传后不能二次修改，参考事例可能会有错误无法修改，如果发现下面例子不能用，请以为准: 传送门 </font>

1. ...

Example:
```python
import  sxtwl

# 从公历年月日获取一天的信息
day = sxtwl.fromSolar(2021, 11, 7)

# 从农历年月日获取一天的信息
day = sxtwl.fromLunar(2020, 12, 1)
```

Sections: 介绍, 安装方法, 使用方法, 联系作者及广告

</details>

### sphinx-automodapi

Sphinx extension for auto-generating API documentation for entire modules

`pip install sphinx-automodapi` · installs (wheel) · licence: BSD-3-Clause · rank 11414 · last release 2026-10-15 · [PyPI](https://pypi.org/project/sphinx-automodapi/)

<details><summary>README extract</summary>

This is a Sphinx extension to automatically generate API pages for whole
modules. It was originally developed for the Astropy project but is now
available as a standalone package since it can be used for any other
package. The documentation can be found on
ReadTheDocs.

To run the tests, you can either do:
or if you have tox installed:

Sections: About, Running tests

</details>

### sklearn-pandas

Pandas integration with sklearn

`pip install sklearn-pandas` · installs (wheel) · licence: MIT License · rank 11459 · last release 2021-05-08 · [PyPI](https://pypi.org/project/sklearn-pandas/)

### splines

Splines in Euclidean Space and Beyond

`pip install splines` · installs (wheel) · licence: MIT License · rank 11524 · last release 2025-06-25 · [PyPI](https://pypi.org/project/splines/) · [docs](https://splines.readthedocs.io/) · [source](https://github.com/AudioSceneDescriptionFormat/splines/)

<details><summary>README extract</summary>

... with focus on univariate, non-uniform piecewise cubic polynomial curves
in one, two and three spatial dimensions, as well as rotation splines.

Installation
 `python -m pip install splines`

Online documentation

Documentation notebooks on Binder

Source code repository (and issue tracker)

DOI ...

</details>

### somacore

Python-language API specification and base utilities for implementation of the SOMA system.

`pip install somacore` · installs (wheel) · licence: MIT License · rank 11535 · last release 2026-04-17 · [PyPI](https://pypi.org/project/somacore/) · [source](https://github.com/single-cell-data/SOMA.git)

<details><summary>README extract</summary>

`somacore` is the Python interpretation of the abstract SOMA specification.
If you’re using SOMA to store or retrive data, you probably want to install a SOMA implementation instead, and not this package directly:

- tiledbsoma (source code)

This core pacakge contains base interfaces, shared types, and other cross-implementation code. ...

</details>

### superdoc-sdk

SuperDoc SDK (CLI-backed)

`pip install superdoc-sdk` · installs (wheel) · licence: AGPL-3.0 · rank 11567 · last release 2026-11-03 · [PyPI](https://pypi.org/project/superdoc-sdk/)

_README extract left out: share-alike licence._

### shinywidgets

Render ipywidgets in Shiny applications

`pip install shinywidgets` · installs (wheel) · licence: MIT License · rank 11569 · last release 2026-10-15 · [PyPI](https://pypi.org/project/shinywidgets/) · [docs](https://github.com/rstudio/py-shinywidgets/) · [source](https://github.com/rstudio/py-shinywidgets/)

<details><summary>README extract</summary>

Render ipywidgets inside a
Shiny (for Python) app.

See the Jupyter Widgets article on the Shiny for Python website for more details.

</details>

### snakemake-interface-executor-plugins

This package provides a stable interface for interactions between Snakemake and its executor plugins.

`pip install snakemake-interface-executor-plugins` · installs (wheel) · licence: MIT License · rank 11579 · last release 2026-03-08 · [PyPI](https://pypi.org/project/snakemake-interface-executor-plugins/)

<details><summary>README extract</summary>

This package provides a stable interface for interactions between Snakemake and its executor plugins.

Plugins should implement the following skeleton to comply with this interface.
It is recommended to use Snakedeploy to set up the skeleton (and automated testing) within a python package.

Example:
```python
from dataclasses import dataclass, field
from typing import List, Generator, Optional
from snakemake_interface_executor_plugins.executors.base import SubmittedJobInfo
from snakemake_interface_executor_plugins.executors.remote import RemoteExecutor
from snakemake_interface_executor_plugins.settings import (
    ExecutorSettingsBase, CommonSettings
...
```

</details>

### sqlbag

various snippets of SQL-related boilerplate

`pip install sqlbag` · installs (wheel) · licence: not stated · rank 11632 · last release 2021-04-01 · [PyPI](https://pypi.org/project/sqlbag/)

<details><summary>README extract</summary>

This is just a collection of handy code for doing database things.

Connections, flask setup, SQLAlchemy ORM helpers, temporary database setup and teardown (handy for integration tests).

Sections: sqlbag: various sql boilerplate, What is in the box

</details>

### sqlalchemy-vertica-python

Vertica dialect for sqlalchemy using vertica_python

`pip install sqlalchemy-vertica-python` · installs (wheel) · licence: MIT License · rank 11641 · last release 2023-06-05 · [PyPI](https://pypi.org/project/sqlalchemy-vertica-python/)

<details><summary>README extract</summary>

Vertica dialect for sqlalchemy. Forked from the Vertica ODBC dialect, written by James Casbon.

This module implements a Vertica dialect for SQLAlchemy using the pure-Python DB-API driver vertica-python, as adapted by Luke Emery-Fertitta.

It is currently maintained by BlueLabs - PRs are welcome!

Engine creation:

Example:
```python
import sqlalchemy as sa
sa.create_engine('vertica+vertica_python://user:pwd@host:port/database')
```

Sections: sqlalchemy-vertica-python, Usage

</details>

### streamlit-card

A streamlit component, to make UI cards

`pip install streamlit-card` · installs (wheel) · licence: MIT License · rank 11661 · last release 2024-05-10 · [PyPI](https://pypi.org/project/streamlit-card/)

<details><summary>README extract</summary>

Streamlit Component, for a UI card

authors - @gamcoh @Pernod Ricard

Example:
```python
from streamlit_card import card

res = card(
    title="Streamlit Card",
    text="This is a test card",
    image="
    styles={
        "card": {
            "width": "500px",
            "height": "500px",
            "border-radius": "60px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            ...
        },
        "text": {
...
```

Sections: st-card, Customizations, Multiple descriptions

</details>

### seahorse

(no summary)

`pip install seahorse` · installs (wheel) · licence: BSD-3-Clause · rank 11669 · last release 2026-08-30 · [PyPI](https://pypi.org/project/seahorse/) · [docs](https://github.com/corail-research/seahorse#readme) · [source](https://github.com/corail-research/seahorse)

<details><summary>README extract</summary>

Developing a game environnement for autonomous agents is complex.
Seahorse is a lightweight Python framework for building turn‑based adversarial games and running matches with AI agents.
This package is battle-tested and tailored to educational use cases

- Define your own game – describe the states, rules, possible moves, and winning condition. ...

Sections: A handy package for kickstarting AI game environments., ✨ Why Seahorse?, 📖 Documentation & Examples

</details>

### svn

Intuitive Subversion wrapper.

`pip install svn` · installs from source (sdist only) · licence: GPL 2 · rank 11694 · last release 2020-02-01 · [PyPI](https://pypi.org/project/svn/)

_README extract left out: share-alike licence._

### sgl-kernel

Kernel Library for SGLang

`pip install sgl-kernel` · installs (wheel) · licence: Apache Software License · rank 11739 · last release 2026-01-15 · [PyPI](https://pypi.org/project/sgl-kernel/)

<details><summary>README extract</summary>

Kernel Library for LLM inference engines

sgl-kernel provides optimized compute primitives for LLM inference engines, enabling efficient inference for large language models and vision-language models through custom kernel operations. It has been used by LightLLM, SGLang and so on.

Sections: sgl-kernel, Building from Source, Use Makefile to build sgl-kernel, Limit build resource usage (CPU / parallelism), Steps to add a new kernel, Adapting C++ Native Types for Torch Compatibility, Kernel Size Analysis, FAQ

</details>

### shotgun-api3

Flow Production Tracking Python API

`pip install shotgun-api3` · installs (wheel) · licence: not stated · rank 11784 · last release 2026-08-06 · [PyPI](https://pypi.org/project/shotgun-api3/)

<details><summary>README extract</summary>

Autodesk provides a simple Python-based API for accessing Flow Production Tracking and integrating with other tools. This is the official API that is maintained by Autodesk (

The latest version can always be found at

Tutorials and detailed documentation about the Python API are available at

Some useful direct links: ...

Sections: Flow Production Tracking Python API, Documentation, Tests

</details>

### snakemake-interface-report-plugins

The interface for Snakemake report plugins.

`pip install snakemake-interface-report-plugins` · installs (wheel) · licence: not stated · rank 11807 · last release 2026-03-09 · [PyPI](https://pypi.org/project/snakemake-interface-report-plugins/)

<details><summary>README extract</summary>

This package defines the interface between Snakemake and its report plugins.

Plugins should implement the following skeleton to comply with this interface.
It is recommended to use Snakedeploy to set up the skeleton (and automated testing) within a python package.

Example:
```python
from dataclasses import dataclass, field

from snakemake_interface_common.exceptions import WorkflowError
from snakemake_interface_report_plugins.reporter import ReporterBase
from snakemake_interface_report_plugins.settings import ReportSettingsBase

# Optional:
# Define additional settings for your reporter.
...
```

</details>

### substrait-extensions

Packaged Substrait Extension Files

`pip install substrait-extensions` · installs (wheel) · licence: Apache-2.0 · rank 11834 · last release 2026-11-01 · [PyPI](https://pypi.org/project/substrait-extensions/) · [source](https://github.com/substrait-io/substrait-packaging)

<details><summary>README extract</summary>

Packages Substrait extensions files, along with associated tests and dialects.

Provides datamodel-code-generator bindings to extensions and dialects.

Example:
```python
from importlib.resources import files

# Access extension files
arithmetic_extensions = files("substrait_extensions.extensions").joinpath("functions_arithmetic.yaml").read_text()
extension_schema_file = files("substrait_extensions.extensions").joinpath("simple_extensions_schema.yaml").read_text()

...
```

Sections: substrait-extensions, Usage

</details>

### superdoc-sdk-cli-linux-x64

SuperDoc CLI runtime for Linux x64

`pip install superdoc-sdk-cli-linux-x64` · installs (wheel) · licence: AGPL-3.0-only AND LicenseRef-SuperDoc-Document-Engine · rank 11859 · last release 2026-11-03 · [PyPI](https://pypi.org/project/superdoc-sdk-cli-linux-x64/)

_README extract left out: share-alike licence._

### spatial-access

(no summary)

`pip install spatial-access` · installs from source (sdist only) · licence: BSD · rank 11875 · last release 2022-01-11 · [PyPI](https://pypi.org/project/spatial-access/)

<details><summary>README extract</summary>

Compute travel times and spatial access measures at scale (millions of origin-destination pairs in minutes).
Travel times for three modes: walking, biking, driving.
Spatial access measures: provider-to-people ratio, avg. time to nearest provider, count/attribute sum of nearby providers, weighted access scores and floating catchment areas. ...

Example:
```python
from spatial_access.p2p import TransitMatrix
from spatial_access.Configs import Configs
custom_config = Configs()
# set fields of custom_cofig
tm = TransitMatrix(..., configs=custom_config)
# continue with computation
```

Sections: Overwriting default configuration values, PyPi Maintenance, Questions/Feedback?

</details>

### streamlit-vertical-slider

Creates a customizable vertical slider

`pip install streamlit-vertical-slider` · installs (wheel) · licence: not stated · rank 11898 · last release 2023-12-22 · [PyPI](https://pypi.org/project/streamlit-vertical-slider/)

<details><summary>README extract</summary>

Creates a constinuous vertical slider with color customizations.

- Fixed issue where default value was not been sent back to Streamlit
- Refactor label into a tooltip reducing the width of the widget by 30%
- Adjusted default size of track, rail and thumb to match Streamlit's native slider. ...

Example:
```python
import streamlit as st
from  streamlit_vertical_slider import vertical_slider

vertical_slider(
    label = "Your widget label",  #Optional
    key = "vert_01" ,
    height = 300, #Optional - Defaults to 300
    thumb_shape = "square", #Optional - Defaults to "circle"
    step = 1, #Optional - Defaults to 1
...
```

Sections: streamlit-vertical-slider, Update ⚠️, Version 2.5, Version 2.0, Usage

</details>

### streamlit-toggle-switch

Creates a customizable toggle

`pip install streamlit-toggle-switch` · installs (wheel) · licence: not stated · rank 11941 · last release 2022-10-25 · [PyPI](https://pypi.org/project/streamlit-toggle-switch/)

### stable-ts

Modifies OpenAI's Whisper to produce more reliable timestamps.

`pip install stable-ts` · installs from source (sdist only) · licence: MIT · rank 11958 · last release 2025-08-16 · [PyPI](https://pypi.org/project/stable-ts/)

<details><summary>README extract</summary>

This library modifies Whisper to produce more reliable timestamps and extends its functionality.

* Setup
* Usage
 * Transcribe
 * Output
 * Alignment
 * Adjustments
 * Refinement
 * Regrouping Words
 * Editing
 * Locating Words
 * Silence Suppression
 * Gap Adjustment
 * Tips
 * Visualizing Suppression
 * Encode Comparison
 * Use with any ASR
* ...

Example:
```python
import stable_whisper
model = stable_whisper.load_model('base')
result = model.transcribe('audio.mp3')
result.to_srt_vtt('audio.srt')
```

Sections: Stabilizing Timestamps for Whisper, Setup, Usage, Transcribe, Output, JSON, Alignment, Adjustments, Refinement, Regrouping Words, Regrouping Methods, Custom Method, Editing, Locating Words

</details>

### streamlit-faker

streamlit-faker is a library to very easily fake Streamlit commands

`pip install streamlit-faker` · installs (wheel) · licence: not stated · rank 11986 · last release 2025-07-01 · [PyPI](https://pypi.org/project/streamlit-faker/)

<details><summary>README extract</summary>

This repository introduces `streamlit-faker`, a library to very easily fake Streamlit commands. You can use it to quickly draft a user interface or as a QA tool... or maybe something more (let us know!). It is built upon the great joke2k/faker project!

The package is available on PyPI!

Call any Streamlit command (see Streamlit docs e.g. ...

Example:
```python
# streamlit_app.py
from streamlit_faker import get_streamlit_faker

st_faker = get_streamlit_faker()
st_faker.subheader()
st_faker.markdown()
st_faker.selectbox()
st_faker.slider()
st_faker.map()
```

Sections: streamlit-faker, Get started, Introduction

</details>

### streamlit-embedcode

Streamlit component for embedded code snippets

`pip install streamlit-embedcode` · installs (wheel) · licence: not stated · rank 11990 · last release 2021-05-17 · [PyPI](https://pypi.org/project/streamlit-embedcode/)

<details><summary>README extract</summary>

Streamlit component for embedded code snippets

</details>

### streamlit-camera-input-live

Alternative version of st.camera_input which returns the webcam images live, without any button press needed

`pip install streamlit-camera-input-live` · installs (wheel) · licence: not stated · rank 11997 · last release 2022-09-27 · [PyPI](https://pypi.org/project/streamlit-camera-input-live/)

<details><summary>README extract</summary>

Alternative version of st.camera_input which returns the webcam images live, without any button press needed

Example:
```python
import streamlit as st

from camera_input_live import camera_input_live

image = camera_input_live()

st.image(value)
```

Sections: streamlit-camera-input-live, Usage instructions

</details>

### stagehand-py

Python SDK for Stagehand

`pip install stagehand-py` · installs (wheel) · licence: MIT License · rank 11998 · last release 2026-10-07 · [PyPI](https://pypi.org/project/stagehand-py/) · [source](https://github.com/browserbase/stagehand)

<details><summary>README extract</summary>

> [!WARNING]
> stagehand-py is deprecated. The Python SDK is now published as
> `stagehand`: `pip install stagehand`.
> Source:

 The AI Browser Automation Framework

 Read the Docs

 NOTE: This is a Python SDK for Stagehand. The original implementation is in TypeScript and is available here. ...

Features:
Stagehand adds determinism to otherwise unpredictable agents.

While there's no limit to what you could instruct Stagehand to do, our primitives allow you to control how much you want to leave to an AI. ...

Example:
```python
import os
from stagehand.sync import Stagehand
from stagehand import StagehandConfig
from stagehand.schemas import AgentConfig, AgentExecuteOptions, AgentProvider
from dotenv import load_dotenv

load_dotenv()

def main():
    # Configure Stagehand
...

</details>

### snakemake-interface-logger-plugins

Logger plugin interface for snakemake

`pip install snakemake-interface-logger-plugins` · installs (wheel) · licence: not stated · rank 12080 · last release 2026-05-20 · [PyPI](https://pypi.org/project/snakemake-interface-logger-plugins/)

<details><summary>README extract</summary>

This package provides a stable interface for interactions between Snakemake and its logger plugins.

Plugins should implement the following skeleton to comply with this interface.
It is recommended to use Snakemake's poetry plugin to set up this skeleton (and automated testing) within a python package, see

Example:
```python
from snakemake_interface_logger_plugins.base import LogHandlerBase
from snakemake_interface_logger_plugins.settings import LogHandlerSettingsBase

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class LogHandlerSettings(LogHandlerSettingsBase):
    myparam: Optional[int] = field(
        default=None,
...
```

...

</details>

### seeq

The Seeq SDK for Python

`pip install seeq` · installs (wheel) · licence: Other/Proprietary License · rank 12144 · last release 2026-11-06 · [PyPI](https://pypi.org/project/seeq/) · [docs](https://python-docs.seeq.com/)

<details><summary>README extract</summary>

The seeq Python module is used to interface with Seeq Server API (

Documentation can be found at

IMPORTANT:

This module mirrors the versioning of Seeq Server, such that the version of this module reflects the version
of the Seeq Server from which the Seeq SDK was generated. ...

Example:
```python
import seeq
import getpass

api_client = seeq.sdk.ApiClient('

# Change this to False if you're getting errors related to SSL
seeq.sdk.Configuration().verify_ssl = True

auth_api = seeq.sdk.AuthApi(api_client)
auth_input = seeq.sdk.AuthInputV1()

# Use raw_input() instead of input() if you're using Python 2
...
```

Sections: Upgrade Considerations, When using Seeq Data lab, Older than R60, When NOT using Seeq Data Lab, seeq.spy, seeq.sdk

</details>

### sigil-sdk

Grafana Sigil Python SDK

`pip install sigil-sdk` · installs (wheel) · licence: not stated · rank 12165 · last release 2026-07-13 · [PyPI](https://pypi.org/project/sigil-sdk/)

<details><summary>README extract</summary>

`sigil-sdk` records normalized LLM generation and tool-execution telemetry. It exports normalized generations to Sigil ingest and uses your OpenTelemetry tracer/meter setup for traces and metrics.

Use this package when you want:

- A provider-agnostic generation record (same schema for OpenAI, Anthropic, Gemini, or custom adapters). ...

Example:
```python
from sigil_sdk import (
    Client,
    GenerationStart,
    ModelRef,
    assistant_text_message,
    user_text_message,
)

client = Client()  # reads SIGIL* env vars

with client.start_generation(
    GenerationStart(
        conversation_id="conv-1",
        agent_name="my-service",
        agent_version="1.0.0",
...
```

...

</details>

### scanspec

Specify step and flyscan paths in a serializable, efficient and Pythonic way

`pip install scanspec` · installs (wheel) · licence: Apache Software License · rank 12166 · last release 2026-04-28 · [PyPI](https://pypi.org/project/scanspec/) · [source](https://github.com/bluesky/scanspec)

<details><summary>README extract</summary>

Specify step and flyscan paths in a serializable, efficient and Pythonic way using combinations of:
- Specs like Line or Spiral
- Optionally Snaking
- Zip, Product and Concat to compose

Serialize the Spec rather than the expanded Path and reconstruct it on the
server. ...

Example:
```python
from scanspec.specs import Ellipse, Fly

spec = Fly(0.4 @ Ellipse(x, 1, 1, 1/9, y, 2.8, y_step=1.7/11, snake=True))
```

</details>

### slack

a DI container

`pip install slack` · does not install on CPython 3.14 · licence: MIT License · rank 12190 · last release ? · [PyPI](https://pypi.org/project/slack/)

<details><summary>README extract</summary>

a DI Container

Example:
```python
from slack import Container

c = Container()

class Component:
    def init(self):
        pass

c.register('component', Component)

c1 = c.provide('component')
c2 = c.provide('component')  # c1 is c2
```

Sections: slack, register and provide, dependency inject, partial inject, using decorator, apply, groups and reset

</details>

### scrapy-zyte-api

Client library to process URLs through Zyte API

`pip install scrapy-zyte-api` · installs (wheel) · licence: BSD-3-Clause · rank 12214 · last release 2026-11-06 · [PyPI](https://pypi.org/project/scrapy-zyte-api/) · [docs](https://scrapy-zyte-api.readthedocs.io/en/latest/) · [source](https://github.com/scrapy-plugins/scrapy-zyte-api)

<details><summary>README extract</summary>

Scrapy plugin for seamless Zyte API integration.

* License: BSD 3-clause

</details>

### shippo

Shipping API Python library (USPS, FedEx, UPS and more)

`pip install shippo` · installs (wheel) · licence: MIT License · rank 12263 · last release 2024-11-26 · [PyPI](https://pypi.org/project/shippo/)

<details><summary>README extract</summary>

Shippo is a shipping API that connects you with multiple shipping carriers (such as USPS, UPS, DHL, Canada Post, Australia Post, and many others) through one interface.

You must register for a Shippo account to use our API. It's free to sign up. Only pay to print a live label, test labels are free.

To use the API, you must generate an API Token. ...

Example:
```python
import shippo

shippo_sdk = shippo.Shippo(
    api_key_header="",
    # the API version can be globally set, though this is normally not required
    # shippo_api_version='',
)

address_list = shippo_sdk.addresses.list()

if address_list is not None:
    # handle response
    pass
```

...

</details>

### snowflake-cli-labs

Snowflake CLI

`pip install snowflake-cli-labs` · installs (wheel) · licence: not stated · rank 12324 · last release 2026-11-02 · [PyPI](https://pypi.org/project/snowflake-cli-labs/) · [source](https://github.com/snowflakedb/snowflake-cli)

<details><summary>README extract</summary>

<!--
 Copyright (c) 2024 Snowflake Inc.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at ...

</details>

### scim2-client

Pythonically build SCIM requests and parse SCIM responses

`pip install scim2-client` · installs (wheel) · licence: Apache Software License · rank 12338 · last release 2026-10-29 · [PyPI](https://pypi.org/project/scim2-client/) · [docs](https://scim2-client.readthedocs.io) · [source](https://github.com/python-scim/scim2-client)

<details><summary>README extract</summary>

A SCIM client Python library built upon scim2-models ,
that pythonically build requests and parse responses,
following the RFC7643 and RFC7644 specifications.
You can use whatever request engine you prefer to perform network requests, but scim2-client comes with httpx2 support. ...

Features:
- CRUD Operations: `create`, `query`, `replace`, `delete` methods for SCIM resources
- PATCH Support: Partial resource modifications with `add`, `remove` and `replace` operations ...

Example:
```python
import datetime
from httpx2 import Client
from scim2_client.engines.httpx2 import SyncSCIMClient
from scim2_models import SCIMException

client = Client(
    base_url=" headers={"Authorization": "Bearer foobar"}
)
scim = SyncSCIMClient(client)
scim.discover()
User = scim.get_resource_model("User")

...

</details>

### sonic-client

python client for sonic search backend

`pip install sonic-client` · installs (wheel) · licence: Apache Software License · rank 12340 · last release 2023-06-01 · [PyPI](https://pypi.org/project/sonic-client/)

<details><summary>README extract</summary>

Python client for sonic search backend.

Example:
```python
from sonic import IngestClient

with IngestClient("127.0.0.1", 1491, "password") as ingestcl:
    print(ingestcl.ping())
    print(ingestcl.protocol)
    print(ingestcl.bufsize)
    ingestcl.push("wiki", "articles", "article-1", "for the love of god hell")
    ingestcl.push("wiki", "articles", "article-2", "for the love of satan heaven")
...
```

Sections: python-sonic-client, Examples, Ingest, Search, Control, API reference, Difference from asonic

</details>

### slangpy

Easily call Slang functions and integrate with PyTorch auto diff directly from Python.

`pip install slangpy` · installs (wheel) · licence: Apache-2.0 · rank 12349 · last release 2026-07-16 · [PyPI](https://pypi.org/project/slangpy/) · [docs](https://slangpy.shader-slang.org/en/latest/) · [source](https://github.com/shader-slang/slangpy)

<details><summary>README extract</summary>

[][2] [][4] [][6]

SlangPy is a cross-platform library designed to make calling GPU code written in Slang extremely simple and easy. It's core objectives are to:
- Make it quick and simple to call Slang functions on the GPU from Python
- Eradicate the boilerplate and bugs associated with writing compute kernels ...

Sections: SlangPy, Introduction, Documentation

</details>

### shuffle-sdk

The SDK used for Shuffle

`pip install shuffle-sdk` · installs (wheel) · licence: MIT License · rank 12385 · last release 2026-08-31 · [PyPI](https://pypi.org/project/shuffle-sdk/)

<details><summary>README extract</summary>

This is the SDK used for app development, testing and production of ALL apps in Shuffle. Works with manual runs, Docker, k8s, cloud serverless.

Released under Python pip for usage outside of Shuffle

Python apps:
All apps:

Example:
```python
from shuffle_sdk import AppBase

class Example(AppBase):
    def sample_function(self, paramname):
        return f"Hello {paramname}"

if name == "main":
    Example.run()
```

Sections: Shuffle SDK, Usage with Shuffle, Build, Download, Usage, Building a fully functional Shuffle App, Adding new Liquid filters

</details>

### spatialmath-python

Provides spatial maths capability for Python.

`pip install spatialmath-python` · installs (wheel) · licence: MIT License · rank 12415 · last release 2026-11-05 · [PyPI](https://pypi.org/project/spatialmath-python/) · [docs](https://rai-opensource.github.io/spatialmath-python/) · [source](https://github.com/rai-opensource/spatialmath-python)

<details><summary>README extract</summary>

A Python implementation of the Spatial Math Toolbox for MATLAB®

- GitHub repository

- Documentation

- Recent changes

- Wiki (examples and details)

- Installation

Spatial mathematics capability underpins all of robotics and robotic vision where we need to describe the position, orientation or pose of objects in 2D or 3D spaces.

Features:
The package provides classes to represent pose and orientation in 3D and 2D
space:

| Represents | in 3D | in 2D |

| pose | ``SE3`` ``Twist3`` ``UnitDualQuaternion`` | ``SE2`` ``Twist2`` |
| orientation | ``SO3`` ``UnitQuaternion`` | ``SO2`` | ...

Example:
```python
>>> from spatialmath import SO3, SE3
>>> R1 = SO3.Rx(0.3)
>>> R1
   1         0         0
   0         0.955336 -0.29552
   0         0.29552   0.955336
```

...

</details>

### soldr

Instant tools. Instant builds. One command.

`pip install soldr` · installs (wheel) · licence: AGPL-3.0-only · rank 12443 · last release 2026-11-07 · [PyPI](https://pypi.org/project/soldr/) · [source](https://github.com/zackees/soldr)

_README extract left out: share-alike licence._

### schemainspect

Schema inspection for PostgreSQL (and possibly others)

`pip install schemainspect` · installs (wheel) · licence: Other/Proprietary License · rank 12492 · last release 2022-09-19 · [PyPI](https://pypi.org/project/schemainspect/) · [source](https://github.com/djrobstep/schemainspect)

<details><summary>README extract</summary>

Schema inspection for PostgreSQL (and potentially others in the future).

Inspects tables, views, materialized views, constraints, indexes, sequences, enums, functions, and extensions. Handles table partitioning and inheritance.

Limitations: Function inspection only confirmed to work with SQL/PLPGSQL languages so far.

Sections: `schemainspect`: SQL Schema Inspection, Basic Usage, Documentation

</details>

### soda-core-snowflake

(no summary)

`pip install soda-core-snowflake` · installs (wheel) · licence: not stated · rank 12516 · last release 2025-09-24 · [PyPI](https://pypi.org/project/soda-core-snowflake/)

### shortid

Short id generator

`pip install shortid` · installs from source (sdist only) · licence: MIT · rank 12572 · last release 2017-03-27 · [PyPI](https://pypi.org/project/shortid/)

### snakemake-interface-scheduler-plugins

Scheduler plugin interface for snakemake

`pip install snakemake-interface-scheduler-plugins` · installs (wheel) · licence: not stated · rank 12586 · last release 2025-10-20 · [PyPI](https://pypi.org/project/snakemake-interface-scheduler-plugins/)

<details><summary>README extract</summary>

This package provides a stable interface for interactions between Snakemake and its scheduler plugins.

Plugins should implement the following skeleton to comply with this interface.
It is recommended to use Snakedeploy to set up the skeleton (and automated testing) within a python package.

In any case, a plugin implementing this interface ...

Example:
```python
from typing import Dict, Mapping, Optional, Union, Sequence
from dataclasses import dataclass

from snakemake_interface_scheduler_plugins.settings import SchedulerSettingsBase
from snakemake_interface_scheduler_plugins.base import SchedulerBase
from snakemake_interface_scheduler_plugins.interfaces.dag import SchedulerDAGInterface
...
```

</details>

### slumber

A library that makes consuming a REST API easier and more convenient

`pip install slumber` · installs from source (sdist only) · licence: UNKNOWN · rank 12613 · last release 2015-05-14 · [PyPI](https://pypi.org/project/slumber/)

<details><summary>README extract</summary>

Slumber is a Python library that provides a convenient yet powerful
object-oriented interface to ReSTful APIs. It acts as a wrapper around the
excellent requests library and abstracts away the handling of URLs, serialization,
and request processing. ...

Sections: Slumber, Getting Help, QuickStart, Requirements, 0.7.1, 0.6.2, 0.6.1, 0.6.0, 0.5.2, 0.4.2, 0.4.1, 0.4.0, 0.3.1, 0.3.0

</details>

### serper-mcp-server

A MCP server for Serper

`pip install serper-mcp-server` · installs (wheel) · licence: not stated · rank 12615 · last release 2025-11-10 · [PyPI](https://pypi.org/project/serper-mcp-server/)

<details><summary>README extract</summary>

A Model Context Protocol server that provides Google Search via Serper. This server enables LLMs to get search result information from Google.

- `google_search` - Set all the parameters
- `google_search_images` - Set all the parameters
- `google_search_videos` - Set all the parameters
- `google_search_places` - Set all the parameters ...

Sections: Serper MCP Server, Available Tools, Usage, Using `uv` (recommended), Using `pip` for project, Using `pip` for globally usage, Debugging

</details>

### shadowcopy

A project for shadowcopy

`pip install shadowcopy` · installs (wheel) · licence: MIT License · rank 12632 · last release 2023-07-08 · [PyPI](https://pypi.org/project/shadowcopy/) · [docs](https://csm10495.github.io/shadowcopy) · [source](https://github.com/csm10495/shadowcopy)

<details><summary>README extract</summary>

shadowcopy is a module for performing file copies from 'shadows' on Windows. Shadow copies are typically used to copy files that are locked for usage by other processes.

More info on shadow copies in Windows can be found here

Creating/Deleting shadow copies requires admin access.

Example:
```python
from shadowcopy import shadow_copy

# Internally this creates a shadow copy instance via WMI, copies the file, then deletes the shadow copy.
shadow_copy("source.txt", "destination.txt")
```

Sections: shadowcopy, Example

</details>

### skyfield-data

Data package for Skyfield

`pip install skyfield-data` · installs (wheel) · licence: MIT License · rank 12640 · last release 2025-08-26 · [PyPI](https://pypi.org/project/skyfield-data/)

<details><summary>README extract</summary>

Skyfield is a Python library for astronomical computations. It depends on various data files to accurately compute moon phases, planet positions, etc.

Several issues are raised by these data files:

* If they're not found in the path of the ``Loader``, they're downloaded at runtime. ...

Example:
```python
from skyfield_data import get_skyfield_data_path
from skyfield.api import Loader
load = Loader(get_skyfield_data_path())
planets = load('de421.bsp')  # this command won't download this file
ts = load.timescale(builtin=False)  # this command won't download the IERS file
```

...

</details>

### sagemaker-feature-store-pyspark-3.1

Amazon SageMaker FeatureStore PySpark Bindings

`pip install sagemaker-feature-store-pyspark-3.1` · installs from source (sdist only) · licence: Apache License 2.0 · rank 12644 · last release 2025-02-06 · [PyPI](https://pypi.org/project/sagemaker-feature-store-pyspark-3.1/)

<details><summary>README extract</summary>

Features:
SageMaker FeatureStore Spark is a connector library for Amazon SageMaker FeatureStore.

With this spark connector, you can easily ingest data to FeatureGroup's online and offline store from Spark `DataFrame`. ...

Sections: Overview, Getting Started

</details>

### ssh-import-id

Authorize SSH public keys from trusted online identities

`pip install ssh-import-id` · installs (wheel) · licence: GPLv3 · rank 12657 · last release 2026-02-16 · [PyPI](https://pypi.org/project/ssh-import-id/)

_README extract left out: share-alike licence._

### stac-geoparquet

(no summary)

`pip install stac-geoparquet` · installs (wheel) · licence: MIT License · rank 12663 · last release 2026-10-21 · [PyPI](https://pypi.org/project/stac-geoparquet/)

<details><summary>README extract</summary>

Convert STAC items between JSON, GeoParquet, pgstac, and Delta Lake.

The STAC spec defines a JSON-based schema.
But it can be hard to manage and search through many millions of STAC items in JSON format.
For one, JSON is very large on disk. ...

Sections: STAC-GeoParquet, Purpose, Documentation, Releasing

</details>

### sqlvalidator

SQL queries formatting, syntactic and semantic validation

`pip install sqlvalidator` · installs (wheel) · licence: MIT · rank 12684 · last release 2022-12-25 · [PyPI](https://pypi.org/project/sqlvalidator/)

<details><summary>README extract</summary>

SQL queries formatting, syntactic and semantic validation

Only supports SELECT statements

Example:
```python
def fun():
    return "select col1, column2 from table"
```

Sections: sqlvalidator, Command line usage, SQL Formatting, Check SQL format, SQL Validation, API / Python code usage, Details about SQL Validation, SQL Syntax, Use with pre-commit, Internals, Run tests, Publishing

</details>

### small-gicp

Efficient and parallelized algorithms for fine point cloud registration

`pip install small-gicp` · installs (wheel) · licence: MIT · rank 12742 · last release 2026-06-13 · [PyPI](https://pypi.org/project/small-gicp/)

<details><summary>README extract</summary>

small_gicp is a header-only C++ library providing efficient and parallelized algorithms for fine point cloud registration (ICP, Point-to-Plane ICP, GICP, VGICP, etc.). It is a refined and optimized version of its predecessor, fast_gicp, re-written from scratch with the following features. ...

Example:
```python
# Align two point clouds using various ICP-like algorithms.

# Parameters
# ----------
# target_points : NDArray[np.float64]
# Nx3 or Nx4 matrix representing the target point cloud.
# source_points : NDArray[np.float64]
# Nx3 or Nx4 matrix representing the source point cloud.
# init_T_target_source : np.ndarray[np.float64]
...
```

...

</details>

### splunk-opentelemetry

(no summary)

`pip install splunk-opentelemetry` · installs (wheel) · licence: Apache-2.0 · rank 12791 · last release 2026-10-29 · [PyPI](https://pypi.org/project/splunk-opentelemetry/) · [docs](https://github.com/signalfx/splunk-otel-python#readme) · [source](https://github.com/signalfx/splunk-otel-python)

<details><summary>README extract</summary>

The Splunk Distribution of OpenTelemetry Python extends
OpenTelemetry Python to automatically instrument Python
applications and export traces, metrics, and logs to Splunk Observability Cloud. It patches supported libraries at
runtime with OpenTelemetry-compatible instrumentation and provides Splunk-specific configuration defaults. ...

Sections: Splunk Distribution of OpenTelemetry Python, Requirements, Get started, Experimental PostgreSQL trace correlation, Declarative configuration, Profiling, Optional: Cisco SecureApp, Fleet management with OpAMP

</details>

### sphinx-multiversion

Add support for multiple versions to sphinx

`pip install sphinx-multiversion` · installs (wheel) · licence: BSD License · rank 12821 · last release 2024-10-03 · [PyPI](https://pypi.org/project/sphinx-multiversion/)

<details><summary>README extract</summary>

Sphinx extension for building self-hosted versioned docs.

This extension aims to provide a clean implementation that tries to avoid
messing with Sphinx internals as much as possible.

Documentation can be found at:

</details>

### Selenium-Screenshot

This package is used to Clipped Images of Html Elements of Selenium Webdriver

`pip install Selenium-Screenshot` · installs (wheel) · licence: MIT License · rank 12826 · last release 2025-05-04 · [PyPI](https://pypi.org/project/Selenium-Screenshot/)

<details><summary>README extract</summary>

Selenium Screenshot:

The Selenium Screenshot is used to clip Html pages and elements using Selenium.

Installation:

`pip install Selenium-Screenshot`

This package supports Python 3.6+ only.

How to Use:

For Full Page Screenshot:

For Html Element Clipping:

Contact Information:

Email:py.wizard.org@gmail.com

Donation: ...

Example:
```python
from selenium import webdriver
from Screenshot import Screenshot

driver = webdriver.Chrome()
driver.get("

ss = Screenshot(driver)

# Example: hide sticky header + specific table
table_to_hide = driver.find_element("css selector", "#p-search")

ss.capture_full_page(
    output_path="python_wiki.png",
...
```

</details>

### surrogate

A Python micro-lib to create stubs for non-existing modules.

`pip install surrogate` · installs from source (sdist only) · licence: not stated · rank 12829 · last release 2019-04-11 · [PyPI](https://pypi.org/project/surrogate/)

### strongtyping

Decorator which checks whether the function is called with the correct type of parameters

`pip install strongtyping` · installs (wheel) · licence: MIT License · rank 12959 · last release 2026-10-25 · [PyPI](https://pypi.org/project/strongtyping/) · [docs](https://strongtyping.readthedocs.io/en/latest/) · [source](https://github.com/FelixTheC/strongtyping)

<details><summary>README extract</summary>

Decorator which checks at Runtime whether the function is called with the correct type of parameters.

And raises TypeMisMatch if the used parameters in a function call where invalid.

Example:
```python
from strongtyping.astrong_typing import a_match_typing
import asyncio

@a_match_typing
async def add(left: int, right: int) -> int:
    return left + right

async def main() -> None:
    result = await add(1, 2)  # 3
    await add(1, "2")  # raises TypeMismatch

asyncio.run(main())
```

Sections: Strong Typing, Performance boost with mypyc, Async functions, 🤖 AI Agent Ready, Docs are available on 'readthedocs'

</details>

### slippers

Build reusable components in Django without writing a single line of Python.

`pip install slippers` · installs (wheel) · licence: MIT · rank 12993 · last release 2026-08-13 · [PyPI](https://pypi.org/project/slippers/) · [docs](https://mitchel.me/slippers) · [source](https://github.com/mixxorz/slippers)

<details><summary>README extract</summary>

Build reusable components in Django without writing a single line of Python.

Sections: What is Slippers?, Documentation

</details>

### sd-jwt

The reference implementation of the IETF SD-JWT specification.

`pip install sd-jwt` · installs (wheel) · licence: not stated · rank 13065 · last release 2024-02-16 · [PyPI](https://pypi.org/project/sd-jwt/)

<details><summary>README extract</summary>

This is the reference implementation of the IETF SD-JWT specification written in Python.

This implementation is used to generate the examples in the IETF SD-JWT specification and it can also be used in other projects for implementing SD-JWT. ...

Sections: SD-JWT Reference Implementation, Setup, sd-jwt-generate, specification.yml for Test Cases and Examples, Input data: `user_claims`, Holder Behavior: `holder_disclosed_claims`, Verifier Output: `expect_verified_user_claims`, Other Properties

</details>

### setuptools-odoo

A library to help package Odoo addons with setuptools

`pip install setuptools-odoo` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 13137 · last release 2026-02-09 · [PyPI](https://pypi.org/project/setuptools-odoo/)

_README extract left out: share-alike licence._

### seletools

Helpful tools for Selenium on Python

`pip install seletools` · installs (wheel) · licence: MIT License · rank 13191 · last release 2024-05-12 · [PyPI](https://pypi.org/project/seletools/)

<details><summary>README extract</summary>

Current package is called Selenium Tools for a reason - it contains useful helpers that are not included into Selenium natively.

Contributions are very welcome!

Example:
```python
from seletools.actions import drag_and_drop

driver = webdriver.Chrome()
source = driver.find_element(By.CSS_SELECTOR, "...")
target = driver.find_element(By.CSS_SELECTOR, "...")
drag_and_drop(driver, source, target)
```

Sections: Selenium Tools, About package, Drag & Drop, Scroll, Getting webdriver's wait values, Interaction with IndexedDB, Setup - Selenium 3, Setup - Selenium 4, Interaction with Local Storage, Notes

</details>

