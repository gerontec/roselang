# Internet

[Index](README.md) · 328 packages in this topic, 34 more listed under another topic, by downloads.

### pydantic

Data validation using Python type hints

`pip install pydantic` · installs (wheel) · licence: MIT · rank 18 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pydantic/) · [docs](https://pydantic.dev/docs/validation/latest/get-started/) · [source](https://github.com/pydantic/pydantic)

<details><summary>README extract</summary>

Data validation using Python type hints.

Fast and extensible, Pydantic plays nicely with your linters/IDE/brain.
Define how data should be in pure, canonical Python 3.10+; validate it with Pydantic.

We've launched Pydantic Logfire to help you monitor your applications.
Learn more ...

Example:
```python
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: list[int] = []

external_data = {'id': '123', 'signup_ts': '2017-06-01 12:22', 'friends': [1, '2', b'3']}
user = User(**external_data)
...
```

...

</details>

### annotated-doc

Document parameters, class attributes, return types, and variables inline, with Annotated.

`pip install annotated-doc` · installs (wheel) · licence: MIT · rank 63 · last release 2026-07-28 · [PyPI](https://pypi.org/project/annotated-doc/) · [docs](https://github.com/fastapi/annotated-doc) · [source](https://github.com/fastapi/annotated-doc)

<details><summary>README extract</summary>

Document parameters, class attributes, return types, and variables inline, with `Annotated`.

Example:
```python
from typing import Annotated

from annotated_doc import Doc

def hi(name: Annotated[str, Doc("Who to say hi to")]) -> None:
    print(f"Hi, {name}!")
```

Sections: Annotated Doc, Usage, Who Uses This, Reasons not to use `annotated-doc`, Reasons to use `annotated-doc`

</details>

### fastapi

FastAPI framework, high performance, easy to learn, fast to code, ready for production

`pip install fastapi` · installs (wheel) · licence: MIT · rank 65 · last release 2026-11-07 · [PyPI](https://pypi.org/project/fastapi/) · [docs](https://fastapi.tiangolo.com/) · [source](https://github.com/fastapi/fastapi)

<details><summary>README extract</summary>

FastAPI framework, high performance, easy to learn, fast to code, ready for production

Documentation:

Source Code:

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

The key features are: ...

Example:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

Sections: Opinions, FastAPI mini documentary, Typer, the FastAPI of CLIs, Requirements, Example, Create it, Run it, Check it, Interactive API docs, Alternative API docs, Example upgrade, Interactive API docs upgrade, Alternative API docs upgrade, Recap

</details>

### googleapis-common-protos

Common protobufs used in Google APIs

`pip install googleapis-common-protos` · installs (wheel) · licence: Apache-2.0 · rank 66 · last release 2026-10-22 · [PyPI](https://pypi.org/project/googleapis-common-protos/) · [source](https://github.com/googleapis/google-cloud-python/tree/main/packages/googleapis-common-protos)

<details><summary>README extract</summary>

- Client Library Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Service Config, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### pydantic-settings

Settings management using Pydantic

`pip install pydantic-settings` · installs (wheel) · licence: MIT · rank 74 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pydantic-settings/) · [docs](https://docs.pydantic.dev/dev-v2/concepts/pydantic_settings/) · [source](https://github.com/pydantic/pydantic-settings)

<details><summary>README extract</summary>

Settings management using Pydantic.

See documentation for more details.

The Pydantic Stack is everything you need to ship production-grade AI agents:

- Pydantic AI - Type-safe agent framework
- Pydantic Logfire - AI-first, full-stack observability
- Logfire AI Gateway - Unified LLM proxy

Sections: pydantic-settings, Part of the Pydantic Stack

</details>

### google-api-core

Google API client core library

`pip install google-api-core` · installs (wheel) · licence: Apache Software License · rank 102 · last release 2026-11-05 · [PyPI](https://pypi.org/project/google-api-core/) · [docs](https://googleapis.dev/python/google-api-core/latest/) · [source](https://github.com/googleapis/google-cloud-python)

<details><summary>README extract</summary>

This library is not meant to stand-alone. Instead it defines
common helpers used by all Google API clients. For more information, see the
documentation.

</details>

### isodate

An ISO 8601 date/time/duration parser and formatter

`pip install isodate` · installs (wheel) · licence: BSD License · rank 161 · last release 2024-10-08 · [PyPI](https://pypi.org/project/isodate/)

<details><summary>README extract</summary>

This module implements ISO 8601 date, time and duration parsing.
The implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is not
mentioned there, then it is treated as non existent, and not as an allowed
option.

For instance, ISO8601:2004 never mentions 2 digit years. ...

Sections: ISO 8601 date/time parser, Documentation, Limitations, Further information, CHANGES, 0.7.2 (2024-10-08), Potentially breaking changes, 0.6.1 (2021-12-13), 0.6.0 (2017-10-13), 0.5.4 (2015-08-06), 0.5.1 (2014-11-07), 0.5.0 (2014-02-23), 0.4.9 (2012-10-30), 0.4.8 (2012-05-04)

</details>

### google-cloud-core

Google Cloud API client core library

`pip install google-cloud-core` · installs (wheel) · licence: Apache Software License · rank 178 · last release 2026-09-29 · [PyPI](https://pypi.org/project/google-cloud-core/)

<details><summary>README extract</summary>

This library is not meant to stand-alone. Instead it defines
common helpers (e.g. base `Client` classes) used by all of the
`google-cloud-*` packages.

- Documentation

Sections: Core Helpers for Google Cloud Python Client Library, Quick Start

</details>

### websocket-client

WebSocket client for Python with low level API options

`pip install websocket-client` · installs (wheel) · licence: Apache-2.0 · rank 180 · last release 2026-08-31 · [PyPI](https://pypi.org/project/websocket-client/) · [docs](https://websocket-client.readthedocs.io/) · [source](https://github.com/websocket-client/websocket-client/)

<details><summary>README extract</summary>

websocket-client is a WebSocket client for Python. It provides access
to low level APIs for WebSockets. websocket-client implements version
hybi-13
of the WebSocket protocol. This client does not currently support the
permessage-deflate extension from
RFC 7692.

This project's documentation can be found at

Example:
```python
import websocket
import _thread
import time
import rel

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

if name == "main":
    websocket.enableTrace(True)
...
```

Sections: websocket-client, Documentation, Usage Tips, Performance, Examples, Long-lived Connection, Short-lived Connection

</details>

### google-cloud-storage

Google Cloud Storage API client library

`pip install google-cloud-storage` · installs (wheel) · licence: Apache Software License · rank 191 · last release 2026-10-15 · [PyPI](https://pypi.org/project/google-cloud-storage/)

<details><summary>README extract</summary>

Google Cloud Storage is a managed service for storing unstructured data. Cloud Storage
allows worldwide storage and retrieval of any amount of data at any time. You can use
Cloud Storage for a range of scenarios including serving website content, storing data
for archival and disaster recovery, or distributing large data objects to users via ...

Example:
```python
# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = "my-new-bucket"

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)

print(f"Bucket {bucket.name} created.")
```

...

</details>

### google-cloud-bigquery

Google BigQuery API client library

`pip install google-cloud-bigquery` · installs (wheel) · licence: Apache 2.0 · rank 192 · last release 2026-10-29 · [PyPI](https://pypi.org/project/google-cloud-bigquery/) · [source](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigquery)

<details><summary>README extract</summary>

Querying massive datasets can be time consuming and expensive without the
right hardware and infrastructure. Google BigQuery solves this problem by
enabling super-fast, SQL queries against append-mostly tables, using the
processing power of Google's infrastructure.

- Client Library Documentation
- Product Documentation ...

Example:
```python
from google.cloud import bigquery

client = bigquery.Client()

# Perform a query.
QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)
```

...

</details>

### google-resumable-media

Utilities for Google Media Downloads and Resumable Uploads

`pip install google-resumable-media` · installs (wheel) · licence: Apache Software License · rank 202 · last release 2026-09-29 · [PyPI](https://pypi.org/project/google-resumable-media/)

<details><summary>README extract</summary>

Utilities for Google Media Downloads and Resumable Uploads

See the docs for examples and usage.

</details>

### google-genai

GenAI Python SDK

`pip install google-genai` · installs (wheel) · licence: Apache-2.0 · rank 203 · last release 2026-11-06 · [PyPI](https://pypi.org/project/google-genai/)

<details><summary>README extract</summary>

Documentation:

Google Gen AI Python SDK provides an interface for developers to integrate
Google's generative models into their Python applications. It supports
the Gemini Developer API and
Gemini Enterprise Agent Platform
APIs. ...

Example:
```python
from google import genai
from google.genai import types
```

Sections: Google Gen AI SDK, Agent Skills, Imports, Create a client, Using types, Close a client, Client context managers, API Selection, HTTP client option: httpx, Faster async client option: Aiohttp, Proxy, Custom base url, Types, Models

</details>

### gunicorn

WSGI HTTP Server for UNIX

`pip install gunicorn` · installs (wheel) · licence: MIT · rank 263 · last release 2026-08-24 · [PyPI](https://pypi.org/project/gunicorn/) · [docs](https://gunicorn.org) · [source](https://github.com/benoitc/gunicorn)

<details><summary>README extract</summary>

Gunicorn is maintained by volunteers. If it powers your production, please consider supporting us:

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork
worker model ported from Ruby's Unicorn project. ...

Features:
- WSGI support for Django, Flask, Pyramid, and any WSGI framework
- ASGI support for FastAPI, Starlette, Quart
- HTTP/2 support (beta) with multiplexed streams
- Dirty Arbiters (beta) for heavy workloads (ML models, long-running tasks) ...

Sections: Gunicorn, Quick Start, Features, Documentation

</details>

### grpc-google-iam-v1

IAM API client library

`pip install grpc-google-iam-v1` · installs (wheel) · licence: Apache Software License · rank 266 · last release 2026-10-22 · [PyPI](https://pypi.org/project/grpc-google-iam-v1/) · [source](https://github.com/googleapis/google-cloud-python)

<details><summary>README extract</summary>

IAM Meta: Manages access control for Google Cloud Platform resources.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for IAM Meta, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### paramiko

SSH2 protocol library

`pip install paramiko` · installs (wheel) · licence: LGPL-2.1 · rank 271 · last release 2026-10-18 · [PyPI](https://pypi.org/project/paramiko/) · [docs](https://docs.paramiko.org) · [source](https://github.com/paramiko/paramiko)

_README extract left out: share-alike licence._

### google-cloud-aiplatform

Vertex AI API client library

`pip install google-cloud-aiplatform` · installs (wheel) · licence: Apache 2.0 · rank 299 · last release 2026-10-28 · [PyPI](https://pypi.org/project/google-cloud-aiplatform/)

<details><summary>README extract</summary>

Gemini Enterprise Agent Platform: Gemini Enterprise Agent Platform is Google Cloud's comprehensive platform for developers to build, scale, govern and optimize agents.

- Client Library Documentation
- Product Documentation

Example:
```python
import vertexai
from vertexai import types

# Instantiate GenAI client from Vertex SDK
# Replace with your project ID and location
client = vertexai.Client(project='my-project', location='us-central1')
```

...

</details>

### pydantic-extra-types

Extra Pydantic types.

`pip install pydantic-extra-types` · installs (wheel) · licence: MIT · rank 400 · last release 2026-03-16 · [PyPI](https://pypi.org/project/pydantic-extra-types/) · [docs](https://docs.pydantic.dev/latest/) · [source](https://github.com/pydantic/pydantic-extra-types)

<details><summary>README extract</summary>

A place for pydantic types that probably shouldn't exist in the main pydantic lib.

See pydantic/pydantic#5012 for more info.

</details>

### google-cloud-secret-manager

Google Cloud Secret Manager API client library

`pip install google-cloud-secret-manager` · installs (wheel) · licence: Apache Software License · rank 407 · last release 2026-11-05 · [PyPI](https://pypi.org/project/google-cloud-secret-manager/)

<details><summary>README extract</summary>

Secret Manager: Stores sensitive data such as API keys, passwords, and certificates.
Provides convenience while improving security.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Secret Manager, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-resource-manager

Google Cloud Resource Manager API client library

`pip install google-cloud-resource-manager` · installs (wheel) · licence: Apache Software License · rank 457 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-resource-manager/)

<details><summary>README extract</summary>

Cloud Resource Manager: Creates, reads, and updates metadata for Google Cloud Platform resource
containers.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Resource Manager, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### fqdn

Validates fully-qualified domain names against RFC 1123, so that they are acceptable to modern browsers

`pip install fqdn` · installs (wheel) · licence: MPL-2.0 · rank 496 · last release 2026-09-28 · [PyPI](https://pypi.org/project/fqdn/) · [source](https://github.com/ypcrts/fqdn)

<details><summary>README extract</summary>

This package validates Fully Qualified Domain Names (FQDNs) conforming to the
Internet Engineering Task Force specification (see
IETF Specification). The design intent is to validate
that a string would be traditionally acceptable as a public Internet hostname
to RFC-conforming software, which is a strict subset of the logic in modern web
browsers ...

Example:
```python
>>> from fqdn import FQDN
>>> domain = 'bbc.co.uk'
>>> bbc_fqdn = FQDN(domain)
>>> bbc_fqdn.is_valid
True
>>> bbc_fqdn.absolute
'bbc.co.uk.'
>>> bbc_fqdn.relative
'bbc.co.uk'
```

Sections: Python FQDN — Fully-Qualified Domain Names, Notes, Standards Conformance, IETF Specification, Commentary

</details>

### google-cloud-pubsub

Google Cloud Pub/Sub API client library

`pip install google-cloud-pubsub` · installs (wheel) · licence: Apache Software License · rank 504 · last release 2026-10-15 · [PyPI](https://pypi.org/project/google-cloud-pubsub/)

<details><summary>README extract</summary>

Cloud Pub/Sub: Provides reliable, many-to-many, asynchronous messaging between
applications.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Pub/Sub, Quick Start, Code samples and snippets, Mac/Linux, Windows, Example Usage, Publishing, Subscribing, Authentication, Versioning, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples

</details>

### google-cloud-appengine-logging

Google Cloud Appengine Logging API client library

`pip install google-cloud-appengine-logging` · installs (wheel) · licence: Apache Software License · rank 575 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-appengine-logging/)

<details><summary>README extract</summary>

AppEngine Logging:

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for AppEngine Logging, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-firestore

Google Cloud Firestore API client library

`pip install google-cloud-firestore` · installs (wheel) · licence: Apache Software License · rank 584 · last release 2026-10-08 · [PyPI](https://pypi.org/project/google-cloud-firestore/)

<details><summary>README extract</summary>

Cloud Firestore: Accesses the NoSQL document database built for automatic scaling, high
performance, and ease of application development.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Firestore, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-logging

Google Cloud Logging API client library

`pip install google-cloud-logging` · installs (wheel) · licence: Apache Software License · rank 588 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-logging/)

<details><summary>README extract</summary>

Cloud Logging: Writes log entries and manages your Cloud Logging configuration.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Logging, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### genai-prices

Calculate prices for calling LLM inference APIs.

`pip install genai-prices` · installs (wheel) · licence: MIT · rank 622 · last release 2026-10-30 · [PyPI](https://pypi.org/project/genai-prices/) · [source](https://github.com/pydantic/genai-prices)

<details><summary>README extract</summary>

Python package for github.com/pydantic/genai-prices.

Example:
```python
from genai_prices import extract_usage

response_data = {
    'model': 'claude-sonnet-4-20250514',
    'usage': {
        'input_tokens': 504,
        'cache_creation_input_tokens': 123,
        'cache_read_input_tokens': 0,
        'output_tokens': 97,
    },
}
extracted_usage = extract_usage(response_data, provider_id='anthropic')
...
```

Sections: genai-prices, Warning: these prices will not be 100% accurate, Usage, `calc_price`, Request pricing context, Batch API, Perplexity web search, Cached input tokens, `extract_usage`, `UpdatePrices`, CLI Usage, Further Documentation, Fractional usage values

</details>

### pydantic-ai-slim

AI Agent Framework, the Pydantic way, slim package

`pip install pydantic-ai-slim` · installs (wheel) · licence: MIT · rank 633 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pydantic-ai-slim/) · [docs](https://pydantic.dev/docs/ai/overview/install/#slim-install) · [source](https://github.com/pydantic/pydantic-ai/tree/main/pydantic_ai_slim)

<details><summary>README extract</summary>

Pydantic AI core logic with minimal required dependencies.

For more information on how to use this package see pydantic.dev/docs/ai/overview/install.

</details>

### pydantic-graph

Graph and state machine library

`pip install pydantic-graph` · installs (wheel) · licence: MIT · rank 636 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pydantic-graph/) · [docs](https://pydantic.dev/docs/ai/graph/graph/) · [source](https://github.com/pydantic/pydantic-ai)

<details><summary>README extract</summary>

Graph and finite state machine library.

This library is developed as part of Pydantic AI, however it has no dependency
on `pydantic-ai` or related packages and can be considered as a pure graph-based state machine library. You may find it useful whether or not you're using Pydantic AI or even building with GenAI. ...

</details>

### gevent

Coroutine-based network library

`pip install gevent` · installs (wheel) · licence: MIT · rank 687 · last release 2026-09-16 · [PyPI](https://pypi.org/project/gevent/) · [docs](http://www.gevent.org) · [source](https://github.com/gevent/gevent/)

<details><summary>README extract</summary>

gevent is a coroutine -based Python networking library that uses
greenlet to provide a high-level synchronous API on top of the libev
or libuv event loop.

Features include:

* Fast event loop based on libev or libuv.
* Lightweight execution units based on greenlets. ...

Sections: gevent, Older Versions of Python, Extra Dependencies

</details>

### retrying

Retrying

`pip install retrying` · installs (wheel) · licence: Apache-2.0 · rank 744 · last release 2025-08-03 · [PyPI](https://pypi.org/project/retrying/) · [source](https://github.com/groodt/retrying)

<details><summary>README extract</summary>

Retrying is an Apache 2.0 licensed general-purpose retrying library, written in
Python, to simplify the task of adding retry behavior to just about anything.

The simplest use case is retrying a flaky function whenever an Exception occurs
until a value is returned.

Features:
- Generic Decorator API
- Specify stop condition (i.e. limit by number of attempts)
- Specify wait condition (i.e. exponential backoff sleeping between attempts)
- Customize retrying on Exceptions
- Customize retrying on expected returned result

Example:
```python
@retry
def never_give_up_never_surrender():
    print("Retry forever ignoring Exceptions, don't wait between retries")
```

Sections: Retrying, Features, Examples

</details>

### google-cloud-monitoring

Google Cloud Monitoring API client library

`pip install google-cloud-monitoring` · installs (wheel) · licence: Apache Software License · rank 747 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-monitoring/)

<details><summary>README extract</summary>

Cloud Monitoring: Manages your Cloud Monitoring data and configurations.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Monitoring, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-bigquery-storage

Google Cloud Bigquery Storage API client library

`pip install google-cloud-bigquery-storage` · installs (wheel) · licence: Apache Software License · rank 757 · last release 2026-10-15 · [PyPI](https://pypi.org/project/google-cloud-bigquery-storage/)

<details><summary>README extract</summary>

BigQuery Storage:

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for BigQuery Storage, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### maxminddb

Reader for the MaxMind DB format

`pip install maxminddb` · installs (wheel) · licence: Apache-2.0 · rank 834 · last release 2026-09-10 · [PyPI](https://pypi.org/project/maxminddb/) · [docs](https://maxminddb.readthedocs.io/en/latest/) · [source](https://github.com/maxmind/MaxMind-DB-Reader-python)

<details><summary>README extract</summary>

This is a Python module for reading MaxMind DB files. The module includes both
a pure Python reader and an optional C extension.

MaxMind DB is a binary file format that stores data indexed by IP address
subnets (IPv4 or IPv6).

Example:
```python
>>> import maxminddb
>>>
>>> with maxminddb.open_database('GeoLite2-City.mmdb') as reader:
>>>
>>>     reader.get('152.216.7.110')
{'country': ... }
>>>
>>>     reader.get_with_prefix_len('152.216.7.110')
({'country': ... }, 24)
>>>
>>>     for network, record in reader:
>>>         ...
```

Sections: MaxMind DB Python Module, Description, Usage, Example, Exceptions, Thread Safety, Versioning

</details>

### tld

Extract the top-level domain (TLD) from the URL given.

`pip install tld` · installs (wheel) · licence: MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-or-later · rank 855 · last release 2026-03-06 · [PyPI](https://pypi.org/project/tld/) · [docs](https://tld.readthedocs.io/) · [source](https://github.com/barseghyanartur/tld/)

_README extract left out: share-alike licence._

### pandas-gbq

Google BigQuery connector for pandas

`pip install pandas-gbq` · installs (wheel) · licence: BSD License · rank 861 · last release 2026-10-23 · [PyPI](https://pypi.org/project/pandas-gbq/)

<details><summary>README extract</summary>

pandas-gbq is a package providing an interface to the Google BigQuery API from pandas.

- Library Documentation
- Product Documentation

Example:
```python
import pandas_gbq

# If running in your local environment or Colab, use the code below and specify your GCP project ID
# result_dataframe = pandas_gbq.read_gbq("SELECT * FROM bigquery-public-data.usa_names.usa_1910_2013 LIMIT 10", project_id="your-project-id")

...
```

Sections: pandas-gbq, Usage, Perform a query, Upload a dataframe, More samples

</details>

### logfire

Pydantic Logfire Python SDK and command-line interface

`pip install logfire` · installs (wheel) · licence: MIT · rank 885 · last release 2026-11-07 · [PyPI](https://pypi.org/project/logfire/) · [docs](https://pydantic.dev/docs/logfire/) · [source](https://github.com/pydantic/logfire)

<details><summary>README extract</summary>

Pydantic Logfire helps you understand what your
Python application is doing through traces, logs, and metrics.

Import Logfire in your application:

See the Logfire documentation to get
started.

Example:
```python
import logfire
```

</details>

### google-cloud-kms

Google Cloud Kms API client library

`pip install google-cloud-kms` · installs (wheel) · licence: Apache Software License · rank 913 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-kms/)

<details><summary>README extract</summary>

Cloud Key Management Service (KMS): Manages keys and performs cryptographic operations in a central cloud
service, for direct use by other cloud resources and applications.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Key Management Service (KMS), Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-spanner

Google Cloud Spanner API client library

`pip install google-cloud-spanner` · installs (wheel) · licence: Apache Software License · rank 931 · last release 2026-09-03 · [PyPI](https://pypi.org/project/google-cloud-spanner/)

<details><summary>README extract</summary>

Cloud Spanner: Cloud Spanner is a managed, mission-critical, globally consistent and
scalable relational database service.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Spanner, Quick Start, Code samples and snippets, Mac/Linux, Windows, Example Usage, Executing Arbitrary SQL in a Transaction, Select records using a Transaction, Insert records using Mutations with a Transaction, Update records using Mutations with a Transaction, Connection API, Aborted Transactions Retry Mechanism, Next Steps, Logging

</details>

### google-cloud-tasks

Google Cloud Tasks API client library

`pip install google-cloud-tasks` · installs (wheel) · licence: Apache Software License · rank 996 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-tasks/)

<details><summary>README extract</summary>

Cloud Tasks: Manages the execution of large numbers of distributed requests.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Tasks, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### asyncssh

AsyncSSH: Asynchronous SSHv2 client and server library

`pip install asyncssh` · installs (wheel) · licence: OSI Approved · rank 1020 · last release 2026-10-04 · [PyPI](https://pypi.org/project/asyncssh/) · [docs](https://asyncssh.readthedocs.io) · [source](https://github.com/ronf/asyncssh)

<details><summary>README extract</summary>

AsyncSSH is a Python package which provides an asynchronous client and
server implementation of the SSHv2 protocol on top of the Python 3.10+
asyncio framework.

Check out the examples to get started!


Features:
* Full support for SSHv2, SFTP, and SCP client and server functions

 * Shell, command, and subsystem channels
 * Environment variables, terminal type, and window size
 * Direct and forwarded TCP/IP channels
 * OpenSSH-compatible direct and ...

Example:
```python
import asyncio, asyncssh, sys

async def run_client():
    async with asyncssh.connect('localhost') as conn:
        result = await conn.run('echo "Hello!"', check=True)
        print(result.stdout, end='')

try:
    asyncio.get_event_loop().run_until_complete(run_client())
except (OSError, asyncssh.Error) as exc:
...
...

</details>

### google-cloud-speech

Google Cloud Speech API client library

`pip install google-cloud-speech` · installs (wheel) · licence: Apache Software License · rank 1036 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-speech/)

<details><summary>README extract</summary>

Cloud Speech-to-Text: Converts audio to text by applying powerful neural network models.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Speech-to-Text, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### pyRFC3339

Generate and parse RFC 3339 timestamps

`pip install pyRFC3339` · installs (wheel) · licence: MIT · rank 1050 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pyRFC3339/) · [docs](https://pyrfc3339.readthedocs.io/) · [source](https://github.com/kurtraschke/pyRFC3339.git)

<details><summary>README extract</summary>

pyRFC3339 parses and generates :RFC:`3339`-compliant timestamps using Python datetime.datetime objects.

>>> from pyrfc3339 import generate, parse
>>> from datetime import UTC, datetime
>>> generate(datetime.now(UTC)) #doctest:+ELLIPSIS
'...T...Z'
>>> parse('2009-01-01T10:01:02Z')
datetime.datetime(2009, 1, 1, 10, 1, 2, ...

</details>

### google-cloud-bigtable

Google Cloud Bigtable API client library

`pip install google-cloud-bigtable` · installs (wheel) · licence: Apache Software License · rank 1058 · last release 2026-10-22 · [PyPI](https://pypi.org/project/google-cloud-bigtable/)

<details><summary>README extract</summary>

Cloud Bigtable: API for reading and writing the contents of Bigtable tables associated with
a Google Cloud project.

- Client Library Documentation
- Product Documentation

v2.23.0 includes a release of the new BigtableDataClientAsync client, accessible at the import path
google.cloud.bigtable.data. ...

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Bigtable, Async Data Client, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-run

Google Cloud Run API client library

`pip install google-cloud-run` · installs (wheel) · licence: Apache Software License · rank 1059 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-run/)

<details><summary>README extract</summary>

Cloud Run Admin: Deploy and manage user provided container images that scale automatically
based on incoming requests. The Cloud Run Admin API v1 follows the Knative
Serving API specification, while v2 is aligned with Google Cloud AIP-based
API standards, as described in

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Run Admin, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-dataproc

Google Cloud Dataproc API client library

`pip install google-cloud-dataproc` · installs (wheel) · licence: Apache Software License · rank 1070 · last release 2026-10-15 · [PyPI](https://pypi.org/project/google-cloud-dataproc/)

<details><summary>README extract</summary>

Cloud Dataproc: Manages Hadoop-based clusters and jobs on Google Cloud Platform.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Dataproc, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### gcloud-aio-auth

Python Client for Google Cloud Auth

`pip install gcloud-aio-auth` · installs (wheel) · licence: MIT License · rank 1080 · last release 2026-11-04 · [PyPI](https://pypi.org/project/gcloud-aio-auth/) · [source](https://github.com/talkiq/gcloud-aio)

<details><summary>README extract</summary>

This is a shared codebase for `gcloud-aio-auth` and `gcloud-rest-auth`

This library implements an `IamClient` class, which can be used to interact
with GCP public keys and URL sign blobs.

It also implements an `IapToken` class which is used for authorizing against
an Identity-Aware Proxy (IAP) secured GCP service. ...

Sections: (Asyncio OR Threadsafe) Python Client for Google Cloud Auth, Usage

</details>

### geoip2

MaxMind GeoIP API

`pip install geoip2` · installs (wheel) · licence: Apache-2.0 · rank 1094 · last release 2026-07-16 · [PyPI](https://pypi.org/project/geoip2/) · [docs](https://geoip2.readthedocs.io/en/latest/) · [source](https://github.com/maxmind/GeoIP2-python)

<details><summary>README extract</summary>

This package provides an API for the GeoIP and GeoLite web services and databases.

Example:
```python
>>> import geoip2.webservice
>>>
>>> # This creates a Client object that can be reused across requests.
>>> # Replace "42" with your account ID and "license_key" with your license
>>> # key. Set the "host" keyword argument to "geolite.info" to use the
>>> # GeoLite web service instead of the GeoIP web service. Set the
...
```

Sections: MaxMind GeoIP Python API, Description, Database Reader Extension, IP Geolocation Usage, Web Service Usage, Sync Web Service Example, Async Web Service Example, Web Service Client Exceptions, Database Usage, Database Example, City Database, Anonymous IP Database, Anonymous Plus Database, ASN Database

</details>

### gcloud-aio-storage

Python Client for Google Cloud Storage

`pip install gcloud-aio-storage` · installs (wheel) · licence: MIT License · rank 1101 · last release 2026-10-02 · [PyPI](https://pypi.org/project/gcloud-aio-storage/) · [source](https://github.com/talkiq/gcloud-aio)

<details><summary>README extract</summary>

This is a shared codebase for `gcloud-aio-storage` and
 `gcloud-rest-storage`

</details>

### google-cloud-storage-control

Google Cloud Storage Control API client library

`pip install google-cloud-storage-control` · installs (wheel) · licence: Apache Software License · rank 1114 · last release 2026-10-22 · [PyPI](https://pypi.org/project/google-cloud-storage-control/)

<details><summary>README extract</summary>

Storage Control: The Storage Control API lets you perform metadata-specific, control plane,
and long-running operations.

The Storage Control API creates one space to perform metadata-specific,
control plane, and long-running operations apart from the Storage API. ...

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Storage Control, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### rq

RQ is a simple, lightweight, library for creating background jobs, and processing them.

`pip install rq` · installs (wheel) · licence: BSD-2-Clause · rank 1120 · last release 2026-10-28 · [PyPI](https://pypi.org/project/rq/) · [docs](https://python-rq.org/docs/) · [source](https://github.com/rq/rq/)

<details><summary>README extract</summary>

RQ (_Redis Queue) is a simple Python library for queueing jobs and processing
them in the background with workers. It is backed by Redis/Valkey and is designed
to have a low barrier to entry while scaling incredibly well for large applications. ...

Example:
```python
import requests

def count_words_at_url(url):
    """Just an example function that's called async."""
    resp = requests.get(url)
    return len(resp.text.split())
```

Sections: Getting started, Job Prioritization, 1. Enqueue at the front, 2. Use multiple queues, Scheduling Jobs, Repeating Jobs, Unique Jobs, Rate Limiting, Retrying Failed Jobs, Webhooks, Interval and Cron Job Scheduling

</details>

### obstore

(no summary)

`pip install obstore` · installs (wheel) · licence: MIT License · rank 1129 · last release 2026-10-27 · [PyPI](https://pypi.org/project/obstore/)

<details><summary>README extract</summary>

[][pypi_link]
[][conda_version]
[][pypi-link]

The simplest, highest-throughput [^1] Python interface to Amazon S3, Google Cloud Storage, Azure Storage, & other S3-compliant APIs, powered by Rust.

- One interface for all backends with no required Python dependencies.
- Sync and async API with full type hinting. ...

Sections: obstore, Documentation

</details>

### google-cloud-vision

Google Cloud Vision API client library

`pip install google-cloud-vision` · installs (wheel) · licence: Apache Software License · rank 1146 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-vision/)

<details><summary>README extract</summary>

Cloud Vision: Integrates Google Vision features, including image labeling, face, logo,
and landmark detection, optical character recognition (OCR), and detection
of explicit content, into applications.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Vision, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-compute

Google Cloud Compute API client library

`pip install google-cloud-compute` · installs (wheel) · licence: Apache Software License · rank 1151 · last release 2026-11-05 · [PyPI](https://pypi.org/project/google-cloud-compute/)

<details><summary>README extract</summary>

Compute Engine: Compute Engine is an infrastructure as a service (IaaS) product that offers self-managed virtual machine (VM) instances and bare metal instances.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Compute Engine, Quick Start, PyCharm/JetBrains IDEs, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### python-snappy

Python library for the snappy compression library from Google

`pip install python-snappy` · installs (wheel) · licence: BSD License · rank 1161 · last release 2024-08-29 · [PyPI](https://pypi.org/project/python-snappy/)

<details><summary>README extract</summary>

Python bindings for the snappy compression library from Google.

More details about Snappy library:

</details>

### google-cloud-texttospeech

Google Cloud Texttospeech API client library

`pip install google-cloud-texttospeech` · installs (wheel) · licence: Apache Software License · rank 1232 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-texttospeech/)

<details><summary>README extract</summary>

Cloud Text-to-Speech: Synthesizes natural-sounding speech by applying powerful neural network
models.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Text-to-Speech, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-dlp

Google Cloud Dlp API client library

`pip install google-cloud-dlp` · installs (wheel) · licence: Apache Software License · rank 1235 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-dlp/)

<details><summary>README extract</summary>

Sensitive Data Protection (DLP): Discover and protect your sensitive data. A fully managed service designed
to help you discover, classify, and protect your valuable data assets with
ease.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Sensitive Data Protection (DLP), Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### pydantic-evals

Framework for evaluating stochastic code execution, especially code making use of LLMs

`pip install pydantic-evals` · installs (wheel) · licence: MIT · rank 1240 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pydantic-evals/) · [docs](https://pydantic.dev/docs/ai/evals/evals/) · [source](https://github.com/pydantic/pydantic-ai)

<details><summary>README extract</summary>

This is a library for evaluating non-deterministic (or "stochastic") functions in Python. It provides a simple,
Pythonic interface for defining and running stochastic functions, and analyzing the results of running those functions. ...

Example:
```python
from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import Evaluator, EvaluatorContext, IsInstance

# Define a test case with inputs and expected output
case = Case(
    name='capital_question',
    inputs='What is the capital of France?',
    expected_output='Paris',
)

# Define a custom evaluator
...
```

Sections: Pydantic Evals, Example, Logfire Integration

</details>

### google-cloud-translate

Google Cloud Translate API client library

`pip install google-cloud-translate` · installs (wheel) · licence: Apache Software License · rank 1247 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-translate/)

<details><summary>README extract</summary>

Cloud Translation: Integrates text translation into your website or application.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Translation, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-ai-generativelanguage

Google Ai Generativelanguage API client library

`pip install google-ai-generativelanguage` · installs (wheel) · licence: Apache Software License · rank 1252 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-ai-generativelanguage/)

<details><summary>README extract</summary>

Generative Language: The Gemini API allows developers to build generative AI applications using
Gemini models. Gemini is our most capable model, built from the ground up
to be multimodal. It can generalize and seamlessly understand, operate
across, and combine different types of information including language,
images, audio, video, and code. ...

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

...

</details>

### scp

scp module for paramiko

`pip install scp` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 1303 · last release 2026-10-06 · [PyPI](https://pypi.org/project/scp/)

_README extract left out: share-alike licence._

### google-cloud-dataplex

Google Cloud Dataplex API client library

`pip install google-cloud-dataplex` · installs (wheel) · licence: Apache Software License · rank 1316 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-dataplex/)

<details><summary>README extract</summary>

Cloud Dataplex: A unified, intelligent governance solution for data and AI assets.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Dataplex, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-trace

Google Cloud Trace API client library

`pip install google-cloud-trace` · installs (wheel) · licence: Apache Software License · rank 1355 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-trace/)

<details><summary>README extract</summary>

Cloud Trace: Sends application trace data to Stackdriver Trace for viewing. Trace data
is collected for all App Engine applications by default. Trace data from
other applications can be provided using this API. This library is used to
interact with the Trace API directly. ...

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Trace, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-language

Google Cloud Language API client library

`pip install google-cloud-language` · installs (wheel) · licence: Apache Software License · rank 1363 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-language/)

<details><summary>README extract</summary>

Cloud Natural Language: Provides natural language understanding technologies, such as sentiment
analysis, entity recognition, entity sentiment analysis, and other text
annotations, to developers.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Natural Language, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-build

Google Cloud Build API client library

`pip install google-cloud-build` · installs (wheel) · licence: Apache Software License · rank 1380 · last release 2026-11-05 · [PyPI](https://pypi.org/project/google-cloud-build/)

<details><summary>README extract</summary>

Cloud Build: Creates and manages builds on Google Cloud Platform.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Build, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### atlassian-python-api

Python Atlassian REST API Wrapper

`pip install atlassian-python-api` · installs (wheel) · licence: Apache Software License · rank 1389 · last release 2026-09-14 · [PyPI](https://pypi.org/project/atlassian-python-api/)

<details><summary>README extract</summary>

What is it?
___
The atlassian-python-api library provides a simple and convenient way to interact with Atlassian products
(such as Jira Service management, Jira Software, Confluence, Bitbucket and apps Insight, X-Ray) using Python. ...

Example:
```python
from atlassian import Confluence
import requests
# If you want to use a session, you can create it like this:
session =  requests.Session()
# and pass it to the Confluence constructor
confluence = Confluence(
    url='
    username='admin',
    password='admin',
    session=session,)

status = confluence.create_page(
    space='DEMO',
...
```

</details>

### google-cloud-container

Google Cloud Container API client library

`pip install google-cloud-container` · installs (wheel) · licence: Apache Software License · rank 1393 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-container/)

<details><summary>README extract</summary>

Kubernetes Engine: Builds and manages container-based applications, powered by the open source
Kubernetes technology.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Kubernetes Engine, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-videointelligence

Google Cloud Videointelligence API client library

`pip install google-cloud-videointelligence` · installs (wheel) · licence: Apache Software License · rank 1395 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-videointelligence/)

<details><summary>README extract</summary>

Cloud Video Intelligence: Detects objects, explicit content, and scene changes in videos. It also
specifies the region for annotation and transcribes speech to text.
Supports both asynchronous API and streaming API.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Video Intelligence, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### asyncer

Asyncer, async and await, focused on developer experience.

`pip install asyncer` · installs (wheel) · licence: MIT · rank 1405 · last release 2026-06-25 · [PyPI](https://pypi.org/project/asyncer/) · [docs](https://asyncer.tiangolo.com) · [source](https://github.com/fastapi/asyncer)

<details><summary>README extract</summary>

Asyncer, async and await, focused on developer experience.

Documentation:

Source Code:

Asyncer is a small library built on top of AnyIO.

Asyncer has a small number of utility functions that allow working with `async`, `await`, and concurrent code in a more convenient way under my (@tiangolo - Sebastián Ramírez) very opinionated and subjective ...

Example:
```python
import time

import anyio
from asyncer import asyncify

def do_sync_work(name: str):
    time.sleep(1)
    return f"Hello, {name}"

async def main():
    message = await asyncify(do_sync_work)(name="World")
    print(message)

anyio.run(main)
```

Sections: Can I Use It?, Requirements, How to Use

</details>

### cssutils

A CSS Cascading Style Sheets library for Python

`pip install cssutils` · installs (wheel) · licence: LGPL-3.0-or-later · rank 1406 · last release 2026-04-27 · [PyPI](https://pypi.org/project/cssutils/) · [source](https://github.com/jaraco/cssutils)

_README extract left out: share-alike licence._

### google-cloud-bigquery-datatransfer

Google Cloud Bigquery Datatransfer API client library

`pip install google-cloud-bigquery-datatransfer` · installs (wheel) · licence: Apache Software License · rank 1427 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-bigquery-datatransfer/)

<details><summary>README extract</summary>

BigQuery Data Transfer: Schedule queries or transfer external data from SaaS applications to Google
BigQuery on a regular basis.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for BigQuery Data Transfer, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-dataform

Google Cloud Dataform API client library

`pip install google-cloud-dataform` · installs (wheel) · licence: Apache Software License · rank 1451 · last release 2026-11-05 · [PyPI](https://pypi.org/project/google-cloud-dataform/)

<details><summary>README extract</summary>

Dataform: Service to develop, version control, and operationalize SQL pipelines in
BigQuery.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Dataform, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-iam

Google Cloud Iam API client library

`pip install google-cloud-iam` · installs (wheel) · licence: Apache Software License · rank 1474 · last release 2026-11-05 · [PyPI](https://pypi.org/project/google-cloud-iam/)

<details><summary>README extract</summary>

Identity and Access Management (IAM): Manages identity and access control for Google Cloud resources, including
the creation of service accounts, which you can use to authenticate to
Google and make API calls. Enabling this API also enables the IAM Service
Account Credentials API (iamcredentials.googleapis.com). ...

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

...

</details>

### gcloud-aio-bigquery

Python Client for Google Cloud BigQuery

`pip install gcloud-aio-bigquery` · installs (wheel) · licence: MIT License · rank 1479 · last release 2026-11-04 · [PyPI](https://pypi.org/project/gcloud-aio-bigquery/) · [source](https://github.com/talkiq/gcloud-aio)

<details><summary>README extract</summary>

This is a shared codebase for `gcloud-aio-bigquery` and
 `gcloud-rest-bigquery`

</details>

### google-cloud-workflows

Google Cloud Workflows API client library

`pip install google-cloud-workflows` · installs (wheel) · licence: Apache Software License · rank 1483 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-workflows/)

<details><summary>README extract</summary>

Workflows: Manage workflow definitions. To execute workflows and manage executions,
see the Workflows Executions API.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Workflows, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-storage-transfer

Google Cloud Storage Transfer API client library

`pip install google-cloud-storage-transfer` · installs (wheel) · licence: Apache Software License · rank 1490 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-storage-transfer/)

<details><summary>README extract</summary>

Storage Transfer: Transfers data from external data sources to a Google Cloud Storage bucket
or between Google Cloud Storage buckets.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Storage Transfer, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-redis

Google Cloud Redis API client library

`pip install google-cloud-redis` · installs (wheel) · licence: Apache Software License · rank 1497 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-redis/)

<details><summary>README extract</summary>

Google Cloud Memorystore for Redis: Creates and manages Redis instances on the Google Cloud Platform.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Google Cloud Memorystore for Redis, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### aws-sam-translator

AWS SAM Translator is a library that transform SAM templates into AWS CloudFormation templates

`pip install aws-sam-translator` · installs (wheel) · licence: Apache Software License · rank 1502 · last release 2026-10-30 · [PyPI](https://pypi.org/project/aws-sam-translator/)

<details><summary>README extract</summary>

The AWS Serverless Application Model (AWS SAM) transform is a AWS CloudFormation macro that transforms SAM templates into CloudFormation templates.

To use the SAM transform, add `AWS::Serverless-2016-10-31` to the `Transform` section of your CloudFormation template.

Benefits of using the SAM transform include: ...

Sections: AWS SAM transform, Getting started, Getting help, Learn more, Workshops and tutorials, Documentation

</details>

### google-cloud-datacatalog

Google Cloud Datacatalog API client library

`pip install google-cloud-datacatalog` · installs (wheel) · licence: Apache Software License · rank 1533 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-datacatalog/)

<details><summary>README extract</summary>

Google Cloud Data Catalog: A fully managed and highly scalable data discovery and metadata management
service.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Google Cloud Data Catalog, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-batch

Google Cloud Batch API client library

`pip install google-cloud-batch` · installs (wheel) · licence: Apache Software License · rank 1535 · last release 2026-11-05 · [PyPI](https://pypi.org/project/google-cloud-batch/)

<details><summary>README extract</summary>

Batch: An API to manage the running of Batch resources on Google Cloud Platform.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Batch, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### aiormq

Pure python AMQP asynchronous client library

`pip install aiormq` · installs (wheel) · licence: Apache-2.0 · rank 1538 · last release 2026-11-01 · [PyPI](https://pypi.org/project/aiormq/) · [docs](https://github.com/mosquito/aiormq/blob/master/README.md) · [source](https://github.com/mosquito/aiormq)

<details><summary>README extract</summary>

aiormq is a pure python AMQP client library.

Features:
* Connecting by URL

 * amqp example: amqp://user:password@server.host/vhost
 * secure amqp example: amqps://user:password@server.host/vhost?cafile=ca.pem&keyfile=key.pem&certfile=cert.pem&no_verify_ssl=0 ...

Example:
```python
import asyncio
import aiormq

async def on_message(message):
    """
    on_message doesn't necessarily have to be defined as async.
    Here it is to show that it's possible.
    """
    print(f" [x] Received message {message!r}")
    print(f"Message body is: {message.body!r}")
    print("Before sleep!")
...
```

...

</details>

### aio-pika

Wrapper around the aiormq for asyncio and humans

`pip install aio-pika` · installs (wheel) · licence: Apache-2.0 · rank 1539 · last release 2026-11-02 · [PyPI](https://pypi.org/project/aio-pika/) · [docs](https://docs.aio-pika.com/) · [source](https://github.com/mosquito/aio-pika)

<details><summary>README extract</summary>

A wrapper around aiormq for asyncio and humans.

Check out the examples and the tutorial in the documentation.

If you are a newcomer to RabbitMQ, please start with the adopted official RabbitMQ tutorial.

> Note: Since version `5.0.0` this library doesn't use `pika` as AMQP connector. ...

Features:
* Completely asynchronous API.
* Object oriented API.
* Transparent auto-reconnects with complete state recovery with `connect_robust`
 (e.g. declared queues or exchanges, consuming state and bindings).
* Python 3.11+ compatible. ...

Example:
```python
import asyncio
import aio_pika
import aio_pika.abc

async def main(loop):
    # Connecting with the given parameters is also possible.
    # aio_pika.connect_robust(host="host", login="login", password="password")
...

</details>

### pydantic-ai

AI Agent Framework, the Pydantic way

`pip install pydantic-ai` · installs (wheel) · licence: MIT · rank 1583 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pydantic-ai/) · [docs](https://pydantic.dev/docs/ai/) · [source](https://github.com/pydantic/pydantic-ai)

<details><summary>README extract</summary>

Agents, realtime voice, image generation, embeddings. Every model, every interface, typed end to end.

Pydantic AI is the Python AI SDK: a typed, extensible agent loop with every model a string swap away, and another one to fall back to when a provider fails. ...

Features:
- Any model, one Python API. Virtually every model and provider (OpenAI, Anthropic, Google, Bedrock, Azure AI Foundry, Groq, Mistral, xAI, Ollama, and dozens more), swappable with a string, or through the Pydantic AI Gateway: one key for all of ...

Example:
```python
from pydantic_ai import Agent
from pydantic_ai.capabilities import WebSearch
from pydantic_ai_harness import Advisor, Coder

agent = Agent(
    'anthropic:claude-fable-5-1',
    capabilities=[
...

</details>

### google-cloud-orchestration-airflow

Google Cloud Orchestration Airflow API client library

`pip install google-cloud-orchestration-airflow` · installs (wheel) · licence: Apache Software License · rank 1590 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-orchestration-airflow/)

<details><summary>README extract</summary>

Cloud Composer: Manages Apache Airflow environments on Google Cloud Platform.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Composer, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-automl

Google Cloud Automl API client library

`pip install google-cloud-automl` · installs (wheel) · licence: Apache Software License · rank 1591 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-automl/)

<details><summary>README extract</summary>

Cloud AutoML: Train high-quality custom machine learning models with minimum effort and
machine learning expertise.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud AutoML, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-memcache

Google Cloud Memcache API client library

`pip install google-cloud-memcache` · installs (wheel) · licence: Apache Software License · rank 1594 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-memcache/)

<details><summary>README extract</summary>

Cloud Memorystore for Memcached: Google Cloud Memorystore for Memcached API is used for creating and
managing Memcached instances in GCP.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Memorystore for Memcached, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-os-login

Google Cloud Os Login API client library

`pip install google-cloud-os-login` · installs (wheel) · licence: Apache Software License · rank 1597 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-os-login/)

<details><summary>README extract</summary>

Cloud OS Login: You can use OS Login to manage access to your VM instances using IAM roles.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud OS Login, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### django-allauth

Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

`pip install django-allauth` · installs (wheel) · licence: MIT License · rank 1602 · last release 2026-10-30 · [PyPI](https://pypi.org/project/django-allauth/) · [docs](https://docs.allauth.org/en/latest/) · [source](https://codeberg.org/allauth/django-allauth)

<details><summary>README extract</summary>

Integrated set of Django applications addressing authentication,
registration, account management as well as 3rd party (social) account
authentication.

Home page

Source code

Issue Tracker

Documentation

Stack Overflow

Demo
 and

Translations ...

Features:
🔑 Comprehensive account functionality
 Supports multiple authentication
 schemes (e.g. login by user name, or by email), as well as multiple
 strategies for account verification (ranging from none to mandatory email
 verification). ...

Sections: Welcome to django-allauth!, Rationale, Features

</details>

### google-cloud-dataflow-client

Google Cloud Dataflow Client API client library

`pip install google-cloud-dataflow-client` · installs (wheel) · licence: Apache Software License · rank 1609 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-dataflow-client/)

<details><summary>README extract</summary>

Dataflow: Manages Google Cloud Dataflow projects on Google Cloud Platform.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Dataflow, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-dataproc-metastore

Google Cloud Dataproc Metastore API client library

`pip install google-cloud-dataproc-metastore` · installs (wheel) · licence: Apache Software License · rank 1611 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-dataproc-metastore/)

<details><summary>README extract</summary>

Dataproc Metastore: The Dataproc Metastore API is used to manage the lifecycle and
configuration of metastore services.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Dataproc Metastore, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### selectolax

A fast HTML5 parser with CSS selectors, written in Cython, using the Lexbor engine.

`pip install selectolax` · installs (wheel) · licence: MIT · rank 1659 · last release 2026-10-22 · [PyPI](https://pypi.org/project/selectolax/) · [docs](https://selectolax.readthedocs.io/en/latest/lexbor.html) · [source](https://github.com/rushter/selectolax)

<details><summary>README extract</summary>

A fast HTML5 parser with CSS selectors, written in Cython, using the Lexbor engine.

Example:
```python
from selectolax.lexbor import LexborHTMLParser

html = """

# Hi there

Lorem Ipsum is simply dummy text of the printing and typesetting industry.

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

"""
tree = LexborHTMLParser(html)

print(tree.css_first('h1#title').text())
# 'Hi there'

print(tree.css_first('h1#title').attributes)
...
```

Sections: Basic examples, Using advanced CSS selectors, Using `lexbor-contains` CSS pseudo-class to match text, Simple Benchmark, Links

</details>

### discord.py

A Python wrapper for the Discord API

`pip install discord.py` · installs (wheel) · licence: MIT License · rank 1686 · last release 2026-03-03 · [PyPI](https://pypi.org/project/discord.py/) · [docs](https://discordpy.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

A modern, easy to use, feature-rich, and async ready API wrapper for Discord written in Python.

Features:
- Modern Pythonic API using `async` and `await`.
- Proper rate limit handling.
- Optimised in both speed and memory.

Example:
```python
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

...
```

Sections: discord.py, Key Features, Optional Packages, Quick Example, Bot Example, Links

</details>

### social-auth-core

Python social authentication made simple.

`pip install social-auth-core` · installs (wheel) · licence: BSD-3-Clause · rank 1698 · last release 2026-10-20 · [PyPI](https://pypi.org/project/social-auth-core/)

<details><summary>README extract</summary>

Python Social Auth is an easy to setup social authentication/registration
mechanism with support for several frameworks and auth providers.

This is the core component of the python-social-auth ecosystem, it
implements the common interface to define new authentication backends
to third parties services, implement integrations with web ...

Sections: Python Social Auth - Core, Description, Documentation, Setup, Versioning

</details>

### firecrawl-py

Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)

`pip install firecrawl-py` · installs (wheel) · licence: MIT License · rank 1710 · last release 2026-11-04 · [PyPI](https://pypi.org/project/firecrawl-py/) · [docs](https://docs.firecrawl.dev) · [source](https://github.com/firecrawl/firecrawl)

<details><summary>README extract</summary>

The Firecrawl Python SDK is the Python client for Firecrawl, the context API for AI agents. Search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and get back clean Markdown or structured data your agents can ship with.

Example:
```python
from firecrawl import Firecrawl
from firecrawl.types import ScrapeOptions

firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

# Scrape a website (v2):
data = firecrawl.scrape(
  '
  formats=['markdown', 'html']
)
print(data)

# Crawl a website (v2 waiter):
crawl_status = firecrawl.crawl(
  '
  limit=100,
...
```

...

</details>

### google-analytics-admin

Google Analytics Admin API client library

`pip install google-analytics-admin` · installs (wheel) · licence: Apache Software License · rank 1714 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-analytics-admin/)

<details><summary>README extract</summary>

Google Analytics Admin: Manage properties in Google Analytics. Warning: Creating multiple Customer
Applications, Accounts, or Projects to simulate or act as a single
Customer Application, Account, or Project (respectively) or to circumvent
Service-specific usage limits or quotas is a direct violation of Google
Cloud Platform Terms of Service as ...

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

...

</details>

### social-auth-app-django

Python Social Authentication, Django integration.

`pip install social-auth-app-django` · installs (wheel) · licence: BSD-3-Clause · rank 1744 · last release 2026-10-20 · [PyPI](https://pypi.org/project/social-auth-app-django/)

<details><summary>README extract</summary>

Python Social Auth is an easy to setup social authentication/registration
mechanism with support for several frameworks and auth providers.

This is the Django component of the
python-social-auth ecosystem,
it implements the needed functionality to integrate
social-auth-core
in a Django based project. ...

Sections: Python Social Auth - Django, Description, Django version, Documentation, Setup, Versioning

</details>

### google-cloud-discoveryengine

Google Cloud Discoveryengine API client library

`pip install google-cloud-discoveryengine` · installs (wheel) · licence: Apache Software License · rank 1746 · last release 2026-11-05 · [PyPI](https://pypi.org/project/google-cloud-discoveryengine/)

<details><summary>README extract</summary>

Discovery Engine: Discovery Engine API.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Discovery Engine, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### rfc3987

Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)

`pip install rfc3987` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 1772 · last release 2018-07-29 · [PyPI](https://pypi.org/project/rfc3987/)

_README extract left out: share-alike licence._

### ndg-httpsclient

Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL

`pip install ndg-httpsclient` · installs (wheel) · licence: BSD License · rank 1811 · last release 2018-07-23 · [PyPI](https://pypi.org/project/ndg-httpsclient/)

<details><summary>README extract</summary>

A HTTPS client implementation for
 * `httplib` (Python 2), `http.client` (Python 3) and
 * `urllib2` (Python 2) and `urllib` (Python 3)

... based on PyOpenSSL. PyOpenSSL provides a more fully featured SSL implementation
over the default provided with Python and importantly enables full verification
of the SSL peer using `pyasn1`.

Sections: 0.5.1, 0.5.0, 0.4.4, 0.4.3, 0.4.2, 0.4.1, 0.4.0, 0.3.3, 0.3.2, 0.3.1, 0.3.0, 0.2.0, 0.1.0, Prerequisites

</details>

### google-analytics-data

Google Analytics Data API client library

`pip install google-analytics-data` · installs (wheel) · licence: Apache Software License · rank 1845 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-analytics-data/)

<details><summary>README extract</summary>

Google Analytics Data: Accesses report data in Google Analytics. Warning: Creating multiple
Customer Applications, Accounts, or Projects to simulate or act as a
single Customer Application, Account, or Project (respectively) or to
circumvent Service-specific usage limits or quotas is a direct violation
of Google Cloud Platform Terms of Service as ...

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

...

</details>

### pymsteams

Format messages and post to Microsoft Teams.

`pip install pymsteams` · installs (wheel) · licence: Apache Software License · rank 1869 · last release 2025-01-07 · [PyPI](https://pypi.org/project/pymsteams/)

<details><summary>README extract</summary>

Example:
```python
import pymsteams

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard("<Microsoft Webhook URL>")

# Add text to the message.
myTeamsMessage.text("this is my text")

# send the message.
myTeamsMessage.send()
```

Sections: pymsteams, Usage, Creating ConnectorCard Messages, Creating CreatorCard Messages to send via async loop, Optional Formatting Methods for Cards, Add a title, Add a link button, Change URL, Set Color Theme, Preview your object, Adding sections to the Connector Card Message, Adding potential actions to the Connector Card Message, Troubleshooting HTTP response, Exceptions

</details>

### django-ninja

Django Ninja - Fast Django REST framework

`pip install django-ninja` · installs (wheel) · licence: MIT License · rank 1883 · last release 2026-10-29 · [PyPI](https://pypi.org/project/django-ninja/) · [docs](https://django-ninja.dev) · [source](https://github.com/vitalik/django-ninja)

<details><summary>README extract</summary>

^ Please read ^

 Fast to learn, fast to code, fast to run

Django Ninja is a web framework for building APIs with Django and Python 3.6+ type hints.

 Key features:

 - Easy: Designed to be easy to use and intuitive.
 - FAST execution: Very high performance thanks to Pydantic and async support. ...

Example:
```python
from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
```

Sections: Django Ninja - Fast Django REST Framework, Usage, Interactive API docs, What next?

</details>

### arq

Job queues in python with asyncio and redis

`pip install arq` · installs (wheel) · licence: MIT License · rank 1903 · last release 2026-04-16 · [PyPI](https://pypi.org/project/arq/) · [docs](https://arq-docs.helpmanual.io) · [source](https://github.com/python-arq/arq)

<details><summary>README extract</summary>

In maintenance only mode: arq is in maintenance only mode, see #510.

Job queues in python with asyncio and redis.

See documentation for more details.

</details>

### google-cloud-datastore

Google Cloud Datastore API client library

`pip install google-cloud-datastore` · installs (wheel) · licence: Apache Software License · rank 1922 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-datastore/)

<details><summary>README extract</summary>

Cloud Datastore: Accesses the schemaless NoSQL database to provide fully managed, robust,
scalable storage for your application.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Datastore, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### boto

Amazon Web Services Library

`pip install boto` · installs (wheel) · licence: MIT License · rank 1988 · last release 2018-07-11 · [PyPI](https://pypi.org/project/boto/)

<details><summary>README extract</summary>

boto 2.49.0

Released: 11-July-2018

Boto3, the next version of Boto, is now
stable and recommended for general use. It can be used side-by-side with Boto
in the same project, so it is easy to start using Boto3 in your existing
projects as well as new projects. Going forward, API updates and all new
feature work will be focused on Boto3. ...

Sections: boto, Boto 3, Introduction, Services, Finding Out More About Boto, Getting Started with Boto

</details>

### google-cloud-vectorsearch

Google Cloud Vectorsearch API client library

`pip install google-cloud-vectorsearch` · installs (wheel) · licence: Apache Software License · rank 1998 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-vectorsearch/)

<details><summary>README extract</summary>

Vector Search: The Vector Search API provides a fully-managed, highly performant, and
scalable vector database designed to power next-generation search,
recommendation, and generative AI applications. It allows you to store,
index, and query your data and its corresponding vector embeddings through
a simple, intuitive interface. ...

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

...

</details>

### pydantic-monty

Monty, the Python sandbox: bindings plus the worker binary

`pip install pydantic-monty` · installs (wheel) · licence: MIT · rank 2006 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pydantic-monty/) · [source](https://github.com/pydantic/monty)

<details><summary>README extract</summary>

Python bindings for Monty, a sandbox for Python code written by AI.

Execution always happens in a pool of `monty` worker subprocesses: a monty
process can never be made fully crash-proof against memory errors (stack
overflows, allocator aborts) triggered by adversarial input, so crash
isolation is built in. ...

Example:
```python
from pydantic_monty import Monty

with Monty() as pool:
    with pool.checkout() as session:
        print(session.feed_run('1 + 2'))
        #> 3
```

Sections: pydantic-monty, CLI, Usage, Basic execution, Async, Input variables and external lookup, Host modules, Host objects and classes, Snapshots: pausing and resuming execution, Resource limits, Clock, sleeping and entropy, Type checking, Crash/failure isolation, Observability

</details>

### googlemaps

Python client library for Google Maps Platform

`pip install googlemaps` · installs from source (sdist only) · licence: Apache Software License · rank 2124 · last release 2023-01-26 · [PyPI](https://pypi.org/project/googlemaps/)

<details><summary>README extract</summary>

Use Python? Want to geocode something? Looking for directions?
Maybe matrices of directions? This library brings the Google Maps Platform Web
Services to your Python application.

The Python Client for Google Maps Services is a Python Client library for the following Google Maps
APIs: ...

Example:
```python
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='Add Your Key here')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

...
```

...

</details>

### cadwyn

Production-ready community-driven modern Stripe-like API versioning in FastAPI

`pip install cadwyn` · installs (wheel) · licence: MIT · rank 2130 · last release 2026-11-01 · [PyPI](https://pypi.org/project/cadwyn/) · [docs](https://docs.cadwyn.dev) · [source](https://github.com/zmievsa/cadwyn)

<details><summary>README extract</summary>

Production-ready community-driven modern Stripe-like API versioning in FastAPI

Cadwyn allows you to maintain the implementation just for your newest API version and get all the older versions generated automatically. ...

Sections: Cadwyn, Who is this for?, Get started

</details>

### fido2

FIDO2/WebAuthn library for implementing clients and servers.

`pip install fido2` · installs (wheel) · licence: Apache Software License; BSD License; Mozilla Public License 2.0 (MPL 2.0) · rank 2149 · last release 2026-06-29 · [PyPI](https://pypi.org/project/fido2/)

<details><summary>README extract</summary>

== python-fido2
image: actions build", link="

Provides library functionality for communicating with a FIDO device over USB as
well as verifying attestation and assertion signatures.

NOTE: Version 2.0 is now released. For help with migration from version 1.x, see
link:doc/Migration_1-2.adoc[the migration guide]. ...

</details>

### google-cloud-artifact-registry

Google Cloud Artifact Registry API client library

`pip install google-cloud-artifact-registry` · installs (wheel) · licence: Apache Software License · rank 2162 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-artifact-registry/)

<details><summary>README extract</summary>

Artifact Registry: Store and manage build artifacts in a scalable and integrated service built
on Google infrastructure.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Artifact Registry, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### connexion

Connexion - API first applications with OpenAPI/Swagger

`pip install connexion` · installs (wheel) · licence: Apache Software License · rank 2184 · last release 2025-10-13 · [PyPI](https://pypi.org/project/connexion/) · [source](https://github.com/spec-first/connexion)

<details><summary>README extract</summary>

Explore the docs »

Connexion is a modern Python web framework that makes spec-first and api-first development easy.
You describe your API in an OpenAPI (or Swagger) specification with as much
detail as you want and Connexion will guarantee that it works as you specified. ...

Example:
```python
from connexion import AsyncApp

app = AsyncApp(name)
```

Sections: ✨ Features, 🪤 Why Connexion, ⚒️ How to Use, Creating your application, Registering an API, Running your application, 📜 Changes, 🙏 Thanks, 📚 Recommended Resources

</details>

### google-cloud-alloydb

Google Cloud Alloydb API client library

`pip install google-cloud-alloydb` · installs (wheel) · licence: Apache Software License · rank 2191 · last release 2026-10-15 · [PyPI](https://pypi.org/project/google-cloud-alloydb/)

<details><summary>README extract</summary>

AlloyDB: AlloyDB for PostgreSQL is an open source-compatible database service that
provides a powerful option for migrating, modernizing, or building
commercial-grade applications. ...

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for AlloyDB, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-documentai

Google Cloud Documentai API client library

`pip install google-cloud-documentai` · installs (wheel) · licence: Apache Software License · rank 2210 · last release 2026-10-29 · [PyPI](https://pypi.org/project/google-cloud-documentai/)

<details><summary>README extract</summary>

Cloud Document AI: Service to parse structured information from unstructured or
semi-structured documents using state-of-the-art Google AI such as natural
language, computer vision, translation, and AutoML.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Document AI, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### txtorcon

Twisted-based Tor controller client, with state-tracking and configuration abstractions. https://txtorcon.readthedocs.org https://github.com/meejah/txtorcon

`pip install txtorcon` · installs (wheel) · licence: MIT License · rank 2212 · last release 2026-06-01 · [PyPI](https://pypi.org/project/txtorcon/)

<details><summary>README extract</summary>

- docs: or

- `torsocks git clone git://fjblvrw2jrxnhtg67qpbzi45r7ofojaoo3orzykesly2j3c2m3htapid.onion/txtorcon.git`
- MIT-licensed;
- Python 3.8+, PyPy 7.3.7+;
- depends on
 Twisted,
 Automat

txtorcon is an implementation of the control-spec
for Tor using the Twisted
networking library for Python. ...

Example:
```python
from twisted.internet.task import react
from twisted.internet.defer import inlineCallbacks, ensureDeferred
from twisted.internet.endpoints import UNIXClientEndpoint

import treq
import txtorcon

async def main(reactor):
    tor = await txtorcon.connect(
        reactor,
        UNIXClientEndpoint(reactor, "/var/run/tor/control")
    )

...
```

Sections: txtorcon, Ten Thousand Feet, Some Possibly Motivational Example Code, Try It Now On Debian/Ubuntu, Read More

</details>

### devtools

Python's missing debug print command, and more.

`pip install devtools` · installs (wheel) · licence: MIT · rank 2324 · last release 2026-10-11 · [PyPI](https://pypi.org/project/devtools/) · [docs](https://python-devtools.helpmanual.io) · [source](https://github.com/samuelcolvin/python-devtools)

<details><summary>README extract</summary>

Python's missing debug print command and other development tools.

For more information, see documentation.

Example:
```python
from devtools import debug

whatever = [1, 2, 3]
debug(whatever)
```

Sections: python devtools, Usage, Usage without Import

</details>

### dirty-equals

Doing dirty (but extremely useful) things with equals.

`pip install dirty-equals` · installs (wheel) · licence: MIT · rank 2369 · last release 2025-11-17 · [PyPI](https://pypi.org/project/dirty-equals/) · [docs](https://dirty-equals.helpmanual.io) · [source](https://github.com/samuelcolvin/dirty-equals)

<details><summary>README extract</summary>

Doing dirty (but extremely useful) things with equals.

Documentation: dirty-equals.helpmanual.io

Source Code: github.com/samuelcolvin/dirty-equals

dirty-equals is a python library that (mis)uses the `eq` method to make python code (generally unit tests)
more declarative and therefore easier to read and write. ...

Example:
```python
from dirty_equals import IsPositive

assert 1 == IsPositive
assert -2 == IsPositive  # this will fail!
```

</details>

### pydantic-monty-client

Python client for the Monty sandbox

`pip install pydantic-monty-client` · installs (wheel) · licence: MIT License · rank 2384 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pydantic-monty-client/) · [source](https://github.com/pydantic/monty)

<details><summary>README extract</summary>

Python client for the Monty sandbox.

Most users want `pydantic-monty`
instead, which pulls in this package plus
`pydantic-monty-runtime` and
is documented in full on its PyPI page.

Install this package directly to use the remote client alone,
or if you're installing the `monty` binary another way.

Example:
```python
from pydantic_monty import Monty

with Monty() as pool:
    with pool.checkout(limits={'max_suspensions': 100}) as session:
        print(session.feed_run('1 + 2'))
        #> 3
```

Sections: pydantic-monty-client, Usage with a remote monty server, Host decode budget, Usage with a local monty worker, Where a snapshot stopped, Tracing snapshot handlers, Restoring snapshots, Working directory, Execution time

</details>

### google-cloud

API Client library for Google Cloud

`pip install google-cloud` · installs (wheel) · licence: Apache Software License · rank 2418 · last release 2018-07-30 · [PyPI](https://pypi.org/project/google-cloud/)

<details><summary>README extract</summary>

Python idiomatic client for Google Cloud Platform services.

 WARNING: The google-cloud Python package is deprecated. On June 18, 2018,
 this package will no longer install any other packages. Please install the
 product-specific google-cloud-* packages needed for your application.

- Homepage
- API Documentation
- Read The Docs Documentation

</details>

### google-cloud-managedkafka

Google Cloud Managedkafka API client library

`pip install google-cloud-managedkafka` · installs (wheel) · licence: Apache Software License · rank 2470 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-managedkafka/)

<details><summary>README extract</summary>

Managed Service for Apache Kafka: Manage Apache Kafka clusters and resources.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Managed Service for Apache Kafka, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### suds-community

Lightweight SOAP client (community fork)

`pip install suds-community` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 2497 · last release 2024-08-24 · [PyPI](https://pypi.org/project/suds-community/)

_README extract left out: share-alike licence._

### google-cloud-pubsublite

Google Cloud Pubsublite API client library

`pip install google-cloud-pubsublite` · installs (wheel) · licence: Apache Software License · rank 2603 · last release 2025-12-16 · [PyPI](https://pypi.org/project/google-cloud-pubsublite/)

<details><summary>README extract</summary>

Pub/Sub Lite API: is designed to provide reliable,
many-to-many, asynchronous messaging between applications. Publisher
applications can send messages to a topic and other applications can
subscribe to that topic to receive the messages. ...

Sections: Python Client for Pub/Sub Lite API, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps

</details>

### starlette-context

Middleware for Starlette that allows you to store and access the context data of a request. Can be used with logging so logs automatically use request headers such as x-request-id or x-correlation-id.

`pip install starlette-context` · installs (wheel) · licence: MIT · rank 2819 · last release 2026-02-28 · [PyPI](https://pypi.org/project/starlette-context/) · [docs](https://starlette-context.readthedocs.io/) · [source](https://github.com/tomwojcik/starlette-context)

<details><summary>README extract</summary>

Middleware for Starlette that allows you to store and access the context data of a request. Can be used with logging so logs automatically use request headers such as x-request-id or x-correlation-id.

Example:
```python
import uvicorn

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from starlette_context import context, plugins
from starlette_context.middleware import ContextMiddleware

...
```

Sections: starlette-context, Resources, Dependencies, Example

</details>

### cadquery

CadQuery is a parametric scripting language for creating and traversing CAD models

`pip install cadquery` · installs (wheel) · licence: Apache Software License · rank 2867 · last release 2026-06-21 · [PyPI](https://pypi.org/project/cadquery/)

<details><summary>README extract</summary>

*Documentation* | *Cheatsheet* | *GitHub Discussions* | *Google Group* | *GUI Editor*

CadQuery is an intuitive, easy-to-use Python module for building parametric 3D CAD models. Using CadQuery, you can write short, simple scripts that produce high quality CAD models. ...

Features:
* Build 3D models with scripts that are as close as possible to how you would describe the object to a human.
* Create parametric models that can be very easily customized by end users. ...

Example:
```python
apptainer run oras://ghcr.io/cadquery/cadquery-apptainer:master ipython -i -c"from cadquery.func import *; from cadquery.vis import show; show(box(1,1,1))"
```

...

</details>

### google-cloud-recaptcha-enterprise

Google Cloud Recaptcha Enterprise API client library

`pip install google-cloud-recaptcha-enterprise` · installs (wheel) · licence: Apache Software License · rank 2873 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-recaptcha-enterprise/)

<details><summary>README extract</summary>

reCAPTCHA Enterprise: Help protect your website from fraudulent activity, spam, and abuse without
creating friction.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for reCAPTCHA Enterprise, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### eventlet

Highly concurrent networking library

`pip install eventlet` · installs (wheel) · licence: MIT License · rank 2874 · last release 2026-10-19 · [PyPI](https://pypi.org/project/eventlet/) · [docs](https://eventlet.readthedocs.io/) · [source](https://github.com/eventlet/eventlet)

<details><summary>README extract</summary>

**New usages of eventlet are now heavily discouraged! Please read the
following.**

Eventlet was created almost 18 years ago, at a time where async
features were absent from the CPython stdlib. ...

Sections: Warning, Eventlet, Getting Eventlet, Building the Docs Locally

</details>

### pytube

Python 3 library for downloading YouTube Videos.

`pip install pytube` · installs (wheel) · licence: The Unlicense (Unlicense) · rank 2900 · last release 2023-05-07 · [PyPI](https://pypi.org/project/pytube/)

<details><summary>README extract</summary>

Features:
- Support for both progressive & DASH streams
- Support for downloading the complete playlist
- Easily register ``on_download_progress`` & ``on_download_complete`` callbacks
- Command-line interfaced included
- Caption track support ...

Example:
```python
>>> from pytube import YouTube
>>> YouTube('
>>> yt = YouTube('
>>> yt.streams
 ... .filter(progressive=True, file_extension='mp4')
 ... .order_by('resolution')
 ... .desc()
 ... .first()
 ... .download()
```

Sections: pytube, Documentation, Description, Features, Quickstart, Using pytube in a Python script, Using the command-line interface

</details>

### scim2-filter-parser

A customizable parser/transpiler for SCIM2.0 filters.

`pip install scim2-filter-parser` · installs (wheel) · licence: MIT License · rank 2958 · last release 2024-07-20 · [PyPI](https://pypi.org/project/scim2-filter-parser/) · [docs](https://scim2-filter-parser.readthedocs.io/en/stable/) · [source](https://github.com/15five/scim2-filter-parser)

<details><summary>README extract</summary>

SCIM 2.0 defines queries that look like this:
These can be hard to work with and covert into SQL to run against a database.

That's where SCIM 2.0 Filter Parser (SFP) can help.

SFP is broken up into four modules, each handling a different part of
translating a SCIM call into a SQL query. ...

Example:
```python
sfp-lexer 'emails[type eq "work" and value co "@example.com"] or ims[type eq "xmpp" and value co "@foo.com"]'

Token(type='ATTRNAME', value='emails', lineno=1, index=0)
Token(type='LBRACKET', value='[', lineno=1, index=6)
Token(type='ATTRNAME', value='type', lineno=1, index=7)
Token(type='EQ', value='eq', lineno=1, index=12)
...
```

Sections: SCIM 2.0 Filter Parser, Description, Use, Django, Speed, Tests

</details>

### google-cloud-recommendations-ai

Google Cloud Recommendations Ai API client library

`pip install google-cloud-recommendations-ai` · installs (wheel) · licence: Apache Software License · rank 3035 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-recommendations-ai/)

<details><summary>README extract</summary>

Recommendations AI: Recommendations AI service enables customers to build end-to-end
personalized recommendation systems without requiring a high level of
expertise in machine learning, recommendation system, or Google Cloud.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Recommendations AI, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### geocoder

Geocoder is a simple and consistent geocoding library.

`pip install geocoder` · installs (wheel) · licence: Apache Software License · rank 3081 · last release 2018-04-04 · [PyPI](https://pypi.org/project/geocoder/)

<details><summary>README extract</summary>

Python Geocoder

Table of content

- Overview
- A glimpse at the API
 - Forward
 - Multiple results
 - Reverse
 - House Addresses
 - IP Addresses
 - Bounding Box
- Command Line Interface
- Providers
- Installation
 - PyPi Install
 - GitHub Install
 - Snap Install
- Feedback
- Contribution
 - Documenting
 - Coding
- ChangeLog

Features:
Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different
JSON responses between each other. ...

Example:
```python
>>> import requests
>>> url = '
>>> params = {'sensor': 'false', 'address': 'Mountain View, CA'}
>>> r = requests.get(url, params=params)
>>> results = r.json()['results']
>>> location = results0['location']
>>> location['lat'], location['lng']
...

</details>

### django-scim2

A partial implementation of the SCIM 2.0 provider specification for use with Django.

`pip install django-scim2` · installs (wheel) · licence: MIT License · rank 3110 · last release 2026-08-12 · [PyPI](https://pypi.org/project/django-scim2/) · [docs](https://django-scim2.readthedocs.io/en/stable/) · [source](https://github.com/15five/django-scim2)

<details><summary>README extract</summary>

This is a provider-side implementation of the SCIM 2.0 [1]_
specification for use in Django.

Note that currently the only supported database is Postgres.

Sections: django-scim2, PyPI, Source, Documentation, Tests, Coverage, Extensibility

</details>

### google-cloud-scheduler

Google Cloud Scheduler API client library

`pip install google-cloud-scheduler` · installs (wheel) · licence: Apache Software License · rank 3131 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-scheduler/)

<details><summary>README extract</summary>

Cloud Scheduler: Creates and manages jobs run on a regular recurring schedule.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Scheduler, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### Pysher

Pusher websocket client for python, based on Erik Kulyk's PythonPusherClient

`pip install Pysher` · installs from source (sdist only) · licence: MIT License · rank 3193 · last release 2022-10-10 · [PyPI](https://pypi.org/project/Pysher/)

<details><summary>README extract</summary>

`pysher` is a python module for handling pusher websockets. It is based on @ekulyk's `PythonPusherClient`.
 A key difference is the dropped support for pre-3.5 Python versions.

This fork is meant as a continuation of the project, and is currently in maintenance mode. ...

Example:
```python
import pysher

# Add a logging handler so we can see the raw communication data
import logging

root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
root.addHandler(ch)

pusher = pysher.Pusher(appkey)

def my_func(*args, **kwargs):
 print("processing Args:", args)
 print("processing Kwargs:", kwargs)

...
```

Sections: Pysher, Example, Performance, Thanks, Copyright, Version 1.0.6, Fixed, Version 1.0.5, Version 1.0.4, Version 1.0.2, Version 1.0.0

</details>

### google-cloud-modelarmor

Google Cloud Modelarmor API client library

`pip install google-cloud-modelarmor` · installs (wheel) · licence: Apache Software License · rank 3194 · last release 2026-11-05 · [PyPI](https://pypi.org/project/google-cloud-modelarmor/)

<details><summary>README extract</summary>

Model Armor: Model Armor helps you protect against risks like prompt injection, harmful
content, and data leakage in generative AI applications by letting you
define policies that filter user prompts and model responses.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Model Armor, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### pytest-pretty

pytest plugin for printing summary data as I want it

`pip install pytest-pretty` · installs (wheel) · licence: MIT · rank 3215 · last release 2025-06-04 · [PyPI](https://pypi.org/project/pytest-pretty/) · [source](https://github.com/samuelcolvin/pytest-pretty)

<details><summary>README extract</summary>

Opinionated pytest plugin to make output slightly easier to read and errors easy to find and fix.

pytest-pretty's only dependencies are rich and pytest itself.

One-line info on which test has failed while tests are running:

A rich table of failures with both test line number and error line number: ...

Sections: pytest-pretty, Realtime error summary, Table of failures, Prettier Summary of a Test Run, Usage with GitHub Actions, `pytester_pretty` fixture

</details>

### litestar

Litestar - A production-ready, highly performant, extensible ASGI API Framework

`pip install litestar` · installs (wheel) · licence: MIT License · rank 3378 · last release 2026-10-18 · [PyPI](https://pypi.org/project/litestar/) · [docs](https://docs.litestar.dev/) · [source](https://github.com/litestar-org/litestar)

<details><summary>README extract</summary>

| Project | | Status |

| CI/CD | | |
| Quality | | |
| Package | | |
| Community | | |
| Meta | | |

Litestar is a powerful, flexible yet opinionated ASGI framework, focused on
building APIs. ...

Example:
```python
from litestar import Litestar, get
from litestar.di import Provide

async def my_dependency() -> str: ...

@get("/")
async def index(injected: str) -> str:
    return injected

app = Litestar([index], dependencies={"injected": Provide(my_dependency)})
```

Sections: Quick Start, Core Features, Example Applications, Features, Class-based Controllers, Data Parsing, Type Hints, and Msgspec, OpenAPI, ReDoc, Swagger-UI and Stoplight Elements API Documentation, Dependency Injection, Middleware, Route Guards, Request Life Cycle Hooks, Performance

</details>

### seleniumbase

SeleniumBase is a framework for web crawling, scraping, and testing. Supports pytest. CDP Mode adds stealth. Includes many tools.

`pip install seleniumbase` · installs (wheel) · licence: MIT · rank 3401 · last release 2026-11-05 · [PyPI](https://pypi.org/project/seleniumbase/) · [docs](https://seleniumbase.io/) · [source](https://github.com/seleniumbase/SeleniumBase)

<details><summary>README extract</summary>

Example:
```python
from seleniumbase import BaseCase
BaseCase.main(name, file)

class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.goto("
        self.type("#user-name", "standard_user")
        self.type("#password", "secret_sauce\n")
        self.assert_element("div.inventory_list")
        self.assert_exact_text("Products", "span.title")
...
```

Sections: ⚙️ Stealthy architecture flowchart, Set up Python & Git, 🔵 Downloading webdrivers, Basic Example / Usage, Here are some common SeleniumBase methods, Fun Facts / Learn More, Demo Mode / Debugging, 🔵 Command-line Options, Directory Configuration, Log files from failed tests, SeleniumBase Dashboard, Generating Test Reports, 🔵 pytest HTML Reports, 🔵 pynose Reports

</details>

### stpyv8

Python Wrapper for Google V8 Engine

`pip install stpyv8` · installs (wheel) · licence: Apache Software License · rank 3406 · last release 2025-11-03 · [PyPI](https://pypi.org/project/stpyv8/)

<details><summary>README extract</summary>

STPyV8 allows interoperability between Python 3 and JavaScript running Google V8 engine.
Use STPyV8 to embed JavaScript code directly into your Python project, or to call Python
code from JavaScript.

STPyV8 is a fork of the original PyV8 project,
with code changed to work with the latest Google V8 engine and Python 3. ...

Example:
```python
# simple.py
import STPyV8

with STPyV8.JSContext() as ctxt:
  upcase = ctxt.eval("""
    ( (lowerString) => {
        return lowerString.toUpperCase();
    })
  """)
  print(upcase("hello world!"))
```

Sections: STPyV8, Usage Examples, Using Python in V8, Using JavaScript in Python, Building, Build Examples, Ubuntu/Debian, MacOS, Windows, Building Boost, Building STPyV8, How does this work?, Is STPyV8 fast?, What can I use this for?

</details>

### litestar-htmx

HTMX Integration for Litestar

`pip install litestar-htmx` · installs (wheel) · licence: MIT License · rank 3422 · last release 2025-06-11 · [PyPI](https://pypi.org/project/litestar-htmx/)

### google-cloud-os-config

Google Cloud Os Config API client library

`pip install google-cloud-os-config` · installs (wheel) · licence: Apache Software License · rank 3444 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-os-config/)

<details><summary>README extract</summary>

OS Config: OS management tools that can be used for patch management, patch
compliance, and configuration management on VM instances.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for OS Config, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-org-policy

Google Cloud Org Policy API client library

`pip install google-cloud-org-policy` · installs (wheel) · licence: Apache Software License · rank 3450 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-org-policy/)

<details><summary>README extract</summary>

Organization Policy: The Organization Policy API allows users to configure governance rules on
their Google Cloud resources across the resource hierarchy.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Organization Policy, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### swagger-ui-bundle

Swagger UI bundled for usage with Python

`pip install swagger-ui-bundle` · installs (wheel) · licence: Apache Software License · rank 3456 · last release 2023-11-01 · [PyPI](https://pypi.org/project/swagger-ui-bundle/) · [source](https://github.com/spec-first/swagger_ui_bundle)

<details><summary>README extract</summary>

This package contains the static files for swagger-ui as a python package.

Basic configuration options are templated with the Jinja2 templating language.

This package is intended to be webserver-agnostic, so it only includes the
static files, and some very basic configuration.

Example:
```python
from swagger_ui_bundle import swagger_ui_path
```

Sections: swagger_ui_bundle, Getting Started

</details>

### google-cloud-asset

Google Cloud Asset API client library

`pip install google-cloud-asset` · installs (wheel) · licence: Apache Software License · rank 3461 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-asset/)

<details><summary>README extract</summary>

Cloud Asset: The Cloud Asset API manages the history and inventory of Google Cloud
resources.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Asset, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-access-context-manager

Google Cloud Access Context Manager Protobufs

`pip install google-cloud-access-context-manager` · installs (wheel) · licence: Apache Software License · rank 3464 · last release 2026-10-22 · [PyPI](https://pypi.org/project/google-cloud-access-context-manager/)

<details><summary>README extract</summary>

Access Context Manager: An API for setting attribute based access control to requests to GCP
services.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Access Context Manager, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-video-transcoder

Google Cloud Video Transcoder API client library

`pip install google-cloud-video-transcoder` · installs (wheel) · licence: Apache Software License · rank 3545 · last release 2026-10-29 · [PyPI](https://pypi.org/project/google-cloud-video-transcoder/)

<details><summary>README extract</summary>

Transcoder: This API converts video files into formats suitable for consumer
distribution.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Transcoder, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### rpyc

Remote Python Call (RPyC) is a transparent and symmetric distributed computing library

`pip install rpyc` · installs (wheel) · licence: MIT License · rank 3657 · last release 2025-04-18 · [PyPI](https://pypi.org/project/rpyc/) · [source](https://github.com/tomerfiliba-org/rpyc)

<details><summary>README extract</summary>

RPyC (pronounced like *are-pie-see*), or *Remote Python Call*, is a
transparent library for symmetrical remote procedure calls,
clustering, and distributed-computing. RPyC makes use of object-proxying,
a technique that employs python's dynamic nature, to overcome the physical
boundaries between processes and computers, so that remote objects can ...

</details>

### telnetlib3

Python Telnet server and client CLI and Protocol library

`pip install telnetlib3` · installs (wheel) · licence: ISC · rank 3662 · last release 2026-11-04 · [PyPI](https://pypi.org/project/telnetlib3/) · [docs](https://telnetlib3.readthedocs.io) · [source](https://github.com/jquast/telnetlib3)

<details><summary>README extract</summary>

`telnetlib3` is a feature-rich Telnet Server, Client, and Protocol library
for Python 3.9 and newer.

This library supports both modern asyncio *and* legacy Blocking API.

The python telnetlib.py module removed by Python 3.13 is also re-distributed as-is, as a backport. ...

Features:
The following RFC specifications are implemented:

* rfc-727, "Telnet Logout Option," Apr 1977.
* rfc-779, "Telnet Send-Location Option", Apr 1981.
* rfc-854, "Telnet Protocol Specification", May 1983. ...

Example:
```python
import asyncio
import telnetlib3

async def shell(reader, writer):
    writer.write('\r\nWould you like to play a game? ')
    inp = await reader.readline()
    if inp:
        writer.echo(inp)
        writer.write('\r\nThey say the only way to win '
...

</details>

### rtoml

A TOML library for python implemented in rust.

`pip install rtoml` · installs (wheel) · licence: MIT License · rank 3705 · last release 2026-10-12 · [PyPI](https://pypi.org/project/rtoml/) · [source](https://github.com/samuelcolvin/rtoml)

<details><summary>README extract</summary>

A TOML library for python implemented in rust.

Features:
* Correctness: rtoml is based on the widely used and very stable toml
rust crate, it passes all the standard TOML tests for TOML 1.1 as well as
having 100% coverage on python code. ...

Example:
```python
from datetime import datetime, timezone, timedelta
import rtoml

obj = {
    'title': 'TOML Example',
    'owner': {
        'dob': datetime(1979, 5, 27, 7, 32, tzinfo=timezone(timedelta(hours=-8))),
        'name': 'Tom Preston-Werner',
    },
    'database': {
        'connection_max': 5000,
        'enabled': True,
...
```

Sections: rtoml, Why Use rtoml, Usage, load, loads, dumps, dump, Examples

</details>

### webdavclient3

WebDAV client, based on original package https://github.com/designerror/webdav-client-python but uses requests instead of PyCURL

`pip install webdavclient3` · installs (wheel) · licence: MIT · rank 3842 · last release 2026-02-06 · [PyPI](https://pypi.org/project/webdavclient3/) · [source](https://github.com/ezhov-evgeny/webdav-client-python-3)

<details><summary>README extract</summary>

Package webdavclient3 based on but uses `requests` instead of `PyCURL`.
It provides easy way to work with WebDAV-servers.

Installation

Sample Usage

Example:
```python
from webdav3.client import Client
options = {
 'webdav_hostname': "
 'webdav_login':    "login",
 'webdav_password': "password"
}
client = Client(options)
client.verify = False # To not check SSL certificates (Default = True)
client.session.proxies(...) # To set proxy directly into the session (Optional)
...
```

Sections: Python WebDAV Client 3, Webdav API, Resource API, Code convention, Run tests, Prepare a Pull Request, Releasing

</details>

### aws-sam-cli

AWS SAM CLI is a CLI tool for local development and testing of Serverless applications

`pip install aws-sam-cli` · installs (wheel) · licence: Apache-2.0 · rank 3854 · last release 2026-10-29 · [PyPI](https://pypi.org/project/aws-sam-cli/)

<details><summary>README extract</summary>

Installation | Blogs | Videos | AWS Docs | Roadmap | Try It Out

The AWS Serverless Application Model (SAM) CLI is an open-source CLI tool that helps you develop serverless applications containing Lambda functions, Step Functions, API Gateway, EventBridge, SQS, SNS and more. Some of the features it provides are: ...

Sections: AWS SAM CLI, Recent blogposts and workshops, Get Started, What is this Github repository? 💻, Related Repositories and Resources

</details>

### aws-lambda-builders

Python library to compile, build & package AWS Lambda functions for several runtimes & frameworks.

`pip install aws-lambda-builders` · installs (wheel) · licence: Apache Software License · rank 3888 · last release 2026-10-26 · [PyPI](https://pypi.org/project/aws-lambda-builders/)

<details><summary>README extract</summary>

Lambda Builders is a Python library to compile, build and package AWS Lambda functions for several runtimes &
frameworks.

Lambda Builders currently contains the following workflows ...

Sections: Lambda Builders, Integrating with Lambda Builders

</details>

### google-cloud-parametermanager

Google Cloud Parametermanager API client library

`pip install google-cloud-parametermanager` · installs (wheel) · licence: Apache Software License · rank 3975 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-parametermanager/)

<details><summary>README extract</summary>

Parameter Manager: Parameter Manager is a single source of truth to store, access and manage
the lifecycle of your workload parameters. Parameter Manager aims to make
management of sensitive application parameters effortless for customers
without diminishing focus on security.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

...

</details>

### asynciolimiter

Rate limiter for Async IO

`pip install asynciolimiter` · installs (wheel) · licence: MIT License · rank 4069 · last release 2025-03-18 · [PyPI](https://pypi.org/project/asynciolimiter/) · [docs](https://asynciolimiter.readthedocs.io/en/latest/) · [source](https://github.com/bharel/asynciolimiter)

<details><summary>README extract</summary>

A simple yet efficient Python AsyncIO rate limiter.

Example:
```python
# Limit to 10 requests per 5 second (equiv to 2 requests per second)
>>> limiter = asynciolimiter.Limiter(10/5)
>>> async def main():
...     await limiter.wait() # Wait for a slot to be available.
...     pass # do stuff

>>> limiter = Limiter(1/3)
>>> async def request():
...     await limiter.wait()
...     print("Request")  # Do stuff
...
...
```

Sections: asynciolimiter, Sample Usage, Available Limiter flavors, Documentation

</details>

### rfc3339

Format dates according to the RFC 3339.

`pip install rfc3339` · installs (wheel) · licence: ISCL · rank 4173 · last release 2019-09-24 · [PyPI](https://pypi.org/project/rfc3339/)

<details><summary>README extract</summary>

Formats dates according to the :RFC:`3339`.

Report bugs and feature requests on Sourcehut

Source availabe on this Mercurial repository:

.. _Sourcehut:

</details>

### proxy.py

\u26a1 Fast \u2022 \U0001fab6 Lightweight \u2022 \U0001f51f Dependency \u2022 \U0001f50c Pluggable \u2022 \U0001f608 TLS interception \u2022 \U0001f512 DNS-over-HTTPS \u2022 \U0001f525 Poor Mans VPN \u2022 \u23ea Reverse & \u23e9 Forward \u2022 \U0001f46e\U0001f3ff Proxy Server framework \u2022 \U0001f310 Web Server framework \u2022 \u27b5 \u27b6 \u27b7 \u27a0 PubSub framework \u2022 \U0001f477 Work acceptor & executor framework.

`pip install proxy.py` · installs (wheel) · licence: BSD License · rank 4349 · last release 2025-02-18 · [PyPI](https://pypi.org/project/proxy.py/)

<details><summary>README extract</summary>

Features:
- A drop-in alternative to `ngrok`
- Fast & Scalable

 - Scale up by using all available cores on the system

 - Threadless executions using asyncio

 - Made to handle `tens-of-thousands` connections / sec ...

Example:
```python
gen_private_key(
    key_path: str,
    password: str,
    bits: int = 2048,
    timeout: int = 10) -> bool
```

Sections: Features, Using PIP, Stable Version with PIP, Using Docker, Stable Version from Docker Hub, Using HomeBrew, Stable Version with HomeBrew, Start proxy.py, Run it, Understanding logs, Enable DEBUG logging, From command line using repo source, Docker image, Customize startup flags

</details>

### google-cloud-sql

Google Cloud Sql API client library

`pip install google-cloud-sql` · installs (wheel) · licence: Apache Software License · rank 4408 · last release 2026-11-05 · [PyPI](https://pypi.org/project/google-cloud-sql/)

<details><summary>README extract</summary>

Cloud SQL Admin: Cloud SQL Admin API

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud SQL Admin, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### python-memcached

Pure python memcached client

`pip install python-memcached` · installs (wheel) · licence: Python Software Foundation License · rank 4442 · last release 2024-01-14 · [PyPI](https://pypi.org/project/python-memcached/)

<details><summary>README extract</summary>

Features:
This software is a 100% Python interface to the memcached memory cache
daemon. It is the client side software which allows storing values
in one or more, possibly remote, memcached servers. Search google for
memcached for more information. ...

</details>

### fastapi-utils

Reusable utilities for FastAPI

`pip install fastapi-utils` · installs (wheel) · licence: MIT License · rank 4453 · last release 2024-11-11 · [PyPI](https://pypi.org/project/fastapi-utils/) · [docs](https://fastapiutils.github.io/fastapi-utils/) · [source](https://github.com/dmontagu/fastapi-utils)

<details><summary>README extract</summary>

Quicker FastApi developing tools

Documentation:

Source Code:

FastAPI is a modern, fast web framework for building APIs with Python 3.8+.

But if you're here, you probably already knew that!

Features:
This package includes a number of utilities to help reduce boilerplate and reuse common functionality across projects:

* Resource Class: Create CRUD with ease the OOP way with `Resource` base class that lets you implement methods quick. ...

Sections: Features, Requirements

</details>

### django-rq

An app that provides django integration for RQ (Redis Queue)

`pip install django-rq` · installs (wheel) · licence: MIT · rank 4555 · last release 2026-08-30 · [PyPI](https://pypi.org/project/django-rq/) · [source](https://github.com/rq/django-rq)

<details><summary>README extract</summary>

Django integration with RQ, a Redis based Python queuing library. Django-RQ is a simple app that allows you to configure your queues in Django's `settings.py` and easily use them in your project.

Example:
```python
# urls.py
urlpatterns += [
    path('django-rq/', include('django_rq.urls'))
]
```

Sections: Django-RQ, Requirements, Admin Integration, Standalone URLs (Alternative), Template URL Resolution, Usage, Putting jobs in the queue, `@job` decorator, Running workers, Suspending and Resuming Workers, Queue Statistics, Configuring Prometheus, Configuring Logging, Custom Queue Classes

</details>

### fnvhash

Pure Python FNV hash implementation.

`pip install fnvhash` · installs (wheel) · licence: MIT License · rank 4594 · last release 2025-05-05 · [PyPI](https://pypi.org/project/fnvhash/)

<details><summary>README extract</summary>

Pure Python implementation of the FNV hash family with 100% test coverage.
Take a look at pyhash for use cases where performance is more important than
portability.

Example:
```python
>>> from fnvhash import fnv1a_32
>>> hex(fnv1a_32(b'foo'))
'0xa9f37ed7'
```

Sections: Pure Python FNV hash implementation, Usage

</details>

### logfire-sdk

The best Python observability tool! 🪵🔥

`pip install logfire-sdk` · installs (wheel) · licence: MIT · rank 4611 · last release 2026-11-07 · [PyPI](https://pypi.org/project/logfire-sdk/) · [docs](https://pydantic.dev/docs/logfire/) · [source](https://github.com/pydantic/logfire)

<details><summary>README extract</summary>

This distribution contains the Python software development kit (SDK) for
Pydantic Logfire.

Most users should install `logfire`, which includes this SDK and the Logfire
command-line interface:

Install `logfire-sdk` directly when the command-line interface is not needed or
is unavailable in the target runtime: ...

</details>

### google-cloud-functions

Google Cloud Functions API client library

`pip install google-cloud-functions` · installs (wheel) · licence: Apache Software License · rank 4613 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-functions/)

<details><summary>README extract</summary>

Cloud Functions: Manages lightweight user-provided functions executed in response to events.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Functions, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-geo-type

Google Geo Type API client library

`pip install google-geo-type` · installs (wheel) · licence: Apache Software License · rank 4786 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-geo-type/)

<details><summary>README extract</summary>

Common Geo Types: Defines common types for Google Geo APIs.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Common Geo Types, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### sharepy

Simple SharePoint Online authentication for Python

`pip install sharepy` · installs from source (sdist only) · licence: GNU General Public License v3 (GPLv3) · rank 4808 · last release 2022-02-05 · [PyPI](https://pypi.org/project/sharepy/)

_README extract left out: share-alike licence._

### google-cloud-dialogflow-cx

Google Cloud Dialogflow Cx API client library

`pip install google-cloud-dialogflow-cx` · installs (wheel) · licence: Apache Software License · rank 4818 · last release 2026-10-08 · [PyPI](https://pypi.org/project/google-cloud-dialogflow-cx/)

<details><summary>README extract</summary>

Dialogflow: Builds conversational interfaces (for example, chatbots, and voice-powered
apps and devices).

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Dialogflow, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### jsonasobj

JSON as python objects

`pip install jsonasobj` · installs (wheel) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication · rank 4823 · last release 2021-02-08 · [PyPI](https://pypi.org/project/jsonasobj/)

<details><summary>README extract</summary>

an extension to the core python json library that treats name/value pairs
as first class attributes whenever possible

</details>

### firecrawl

Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)

`pip install firecrawl` · installs (wheel) · licence: MIT License · rank 4863 · last release 2026-11-04 · [PyPI](https://pypi.org/project/firecrawl/) · [docs](https://docs.firecrawl.dev) · [source](https://github.com/firecrawl/firecrawl)

<details><summary>README extract</summary>

The Firecrawl Python SDK is the Python client for Firecrawl, the context API for AI agents. Search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and get back clean Markdown or structured data your agents can ship with.

Example:
```python
from firecrawl import Firecrawl
from firecrawl.types import ScrapeOptions

firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

# Scrape a website (v2):
data = firecrawl.scrape(
  '
  formats=['markdown', 'html']
)
print(data)

# Crawl a website (v2 waiter):
crawl_status = firecrawl.crawl(
  '
  limit=100,
...
```

...

</details>

### google-cloud-error-reporting

Google Cloud Error Reporting API client library

`pip install google-cloud-error-reporting` · installs (wheel) · licence: Apache Software License · rank 4865 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-error-reporting/)

<details><summary>README extract</summary>

Error Reporting: Groups and counts similar errors from cloud services and applications,
reports new errors, and provides access to error groups and their
associated errors.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Error Reporting, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### flameprof

cProfile flamegraph generator

`pip install flameprof` · installs from source (sdist only) · licence: MIT License · rank 4964 · last release 2018-12-25 · [PyPI](https://pypi.org/project/flameprof/)

<details><summary>README extract</summary>

Flamegraph generator for python's cProfile stats.

Flamegraphs allow to
visualize relations between functions in a very compact and understandable
manner.

`Flameprof` solves main problems of built-in cProfile reporting and can replace
gprof2dot because later outputs
very huge graphs with a lot of noise. ...

Sections: Native svg (--format=svg), Svg generated with flamegraph.pl (--format=log)

</details>

### lomond

Websocket Client Library

`pip install lomond` · installs (wheel) · licence: BSD License · rank 5077 · last release 2026-09-18 · [PyPI](https://pypi.org/project/lomond/)

<details><summary>README extract</summary>

Tranquil WebSockets for Python.

Lomond is a Websocket client which turns a websocket connection in to
an orderly stream of _events_. No threads or callbacks necessary.

- Documentation

- GitHub Repository

- Blog

Example:
```python
from lomond import WebSocket

websocket = WebSocket('wss://echo.websocket.org')

for event in websocket:
    if event.name == 'poll':
        websocket.send_text('Hello, World')
    elif event.name == 'text':
        print(event.text)
```

Sections: Dataplicity Lomond, How to Use, TLS and Debugging, PyPI Trusted Publisher (TPM), Example, Events

</details>

### suds

Lightweight SOAP client (community fork)

`pip install suds` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 5107 · last release 2024-08-24 · [PyPI](https://pypi.org/project/suds/)

_README extract left out: share-alike licence._

### ipaddr

Google's IP address manipulation library

`pip install ipaddr` · installs from source (sdist only) · licence: Apache Software License · rank 5180 · last release 2017-09-15 · [PyPI](https://pypi.org/project/ipaddr/)

<details><summary>README extract</summary>

ipaddr.py is a library for working with IP addresses, both IPv4 and IPv6.

It has been superseded by ipaddress from the Python 3 standard library, and its
Python 2 backport.

</details>

### ibm-watsonx-ai

IBM watsonx.ai API Client

`pip install ibm-watsonx-ai` · installs (wheel) · licence: BSD License · rank 5210 · last release 2026-11-05 · [PyPI](https://pypi.org/project/ibm-watsonx-ai/) · [docs](https://ibm.github.io/watsonx-ai-python-sdk)

<details><summary>README extract</summary>

Enterprise-grade Python client for building, tuning and deploying AI models with IBM watsonx.ai

🚀 Quick Start •
📘 Documentation •
📓 Examples

`ibm-watsonx-ai` is the official Python SDK for IBM watsonx.ai, an enterprise-grade AI platform for building, training, tuning, deploying, and operating AI models at scale. ...

Example:
```python
from ibm_watsonx_ai import Credentials, APIClient

credentials = Credentials(
    url="
    api_key=""
)

# Initialize APIClient using a space ID (you can also use a project ID)
api_client = APIClient(credentials, space_id="")
```

...

</details>

### PyPAC

Proxy auto-config and auto-discovery for Python.

`pip install PyPAC` · installs (wheel) · licence: Apache Software License · rank 5274 · last release 2026-08-07 · [PyPI](https://pypi.org/project/PyPAC/)

<details><summary>README extract</summary>

PyPAC is a Python library for finding proxy auto-config (PAC) files and making HTTP requests
that respect them. PAC files are often used in organizations that need fine-grained and centralized control
of proxy settings.

PyPAC can find PAC files according to the DNS portion of the Web Proxy Auto-Discovery (WPAD) protocol. ...

Features:
* The same Requests API that you already know and love
* Honour PAC setting from Windows Internet Options and macOS System Preferences
* Follow DNS Web Proxy Auto-Discovery protocol
* Proxy authentication pass-through
* Proxy failover and load ...

Example:
```python
>>> from pypac import PACSession
>>> session = PACSession()
>>> session.get('
...
```

...

</details>

### google-cloud-dns

Google Cloud DNS API client library

`pip install google-cloud-dns` · installs (wheel) · licence: Apache Software License · rank 5438 · last release 2026-09-29 · [PyPI](https://pypi.org/project/google-cloud-dns/)

<details><summary>README extract</summary>

Cloud DNS API: provides methods that you can use to manage DNS for your applications.

- Client Library Documentation
- Product Documentation

Sections: Python Client for Cloud DNS API, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps

</details>

### sbvirtualdisplay

A customized pyvirtualdisplay for SeleniumBase.

`pip install sbvirtualdisplay` · installs (wheel) · licence: MIT License · rank 5458 · last release 2024-12-16 · [PyPI](https://pypi.org/project/sbvirtualdisplay/) · [source](https://github.com/mdmintz/sbVirtualDisplay)

<details><summary>README extract</summary>

A customized pyvirtualdisplay for use with SeleniumBase automation.

Example:
```python
from sbvirtualdisplay import Display

display = Display(visible=0, size=(1440, 1880))
display.start()

# Run browser tests in a headless environment

display.stop()
```

Sections: sbVirtualDisplay (💻), Usage example, Or as a context manager, When to use, More info

</details>

### mycdp

Autogenerated CDP utilities for Python

`pip install mycdp` · installs (wheel) · licence: MIT · rank 5559 · last release 2026-06-13 · [PyPI](https://pypi.org/project/mycdp/) · [source](https://github.com/mdmintz/MyCDP)

### gcloud-aio-pubsub

Python Client for Google Cloud Pub/Sub

`pip install gcloud-aio-pubsub` · installs (wheel) · licence: MIT License · rank 5634 · last release 2026-10-16 · [PyPI](https://pypi.org/project/gcloud-aio-pubsub/) · [source](https://github.com/talkiq/gcloud-aio)

<details><summary>README extract</summary>

This is a shared codebase for `gcloud-aio-pubsub` and
 `gcloud-rest-pubsub`

</details>

### PyLD

Python implementation of the JSON-LD API

`pip install PyLD` · installs (wheel) · licence: BSD License · rank 5674 · last release 2026-09-02 · [PyPI](https://pypi.org/project/PyLD/)

<details><summary>README extract</summary>

Documentation |
Installation | Usage | Advanced
Topics | Contributing |
Changelog

This library is an implementation of the JSON-LD specification in
Python.

JSON, as specified in RFC7159, is a simple
language for representing objects on the Web. Linked Data is a way of describing
content across different documents or Web sites. ...

Features:
This library aims to conform with the following W3C Recommendations:

| Standard | Status |

| JSON-LD 1.1 | W3C Recommendation |
| JSON-LD 1.1 Processing Algorithms and API | W3C Recommendation |
| JSON-LD 1.1 Framing | W3C Recommendation |
| RDF ...

Example:
```python
from pyld import jsonld
from pyld.identifier_issuer import IdentifierIssuer
import json

doc = {
    " "Manu Sporny",
    " {"@id": "
    " {"@id": "
}

context = {
    "name": "
...

</details>

### ipwhois

Retrieve and parse whois data for IPv4 and IPv6 addresses.

`pip install ipwhois` · installs (wheel) · licence: BSD License · rank 5716 · last release 2024-10-15 · [PyPI](https://pypi.org/project/ipwhois/)

<details><summary>README extract</summary>

ipwhois is a Python package focused on retrieving and parsing whois data
for IPv4 and IPv6 addresses.

Features:
* Parses a majority of whois fields in to a standard dictionary
* IPv4 and IPv6 support

* Proxy support for RDAP queries
* Supports legacy whois protocol queries
* Referral whois support for legacy whois protocol
* Recursive network parsing for IPs ...

Sections: ipwhois, Summary, Features, Links, Documentation, GitHub latest, GitHub dev, Examples, Github, Pypi, Changes, Upgrade Notes, Dependencies, Firewall Ports

</details>

### google-events

Google Cloudevents library

`pip install google-events` · installs (wheel) · licence: Apache Software License · rank 5736 · last release 2024-12-05 · [PyPI](https://pypi.org/project/google-events/)

<details><summary>README extract</summary>

This library provides classes of common event types used with Google services,
as defined in the Google Cloudevents repository.

</details>

### google-cloud-ndb

NDB library for Google Cloud Datastore

`pip install google-cloud-ndb` · installs (wheel) · licence: Apache Software License · rank 5747 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-ndb/) · [docs](https://googleapis.dev/python/python-ndb/latest)

<details><summary>README extract</summary>

This is an updated version of the `ndb` client library for use with
Google Cloud Datastore.

* Client Library Documentation
* Product Documentation

The original Python 2 version of `ndb` was designed specifically for the
Google App Engine `python27` runtime and can be found at
 This version of
`ndb` is designed for the Google App Engine Python 3 ...

Sections: Google Cloud Datastore `ndb` Client Library, Introduction

</details>

### google-cloud-eventarc-publishing

Google Cloud Eventarc Publishing API client library

`pip install google-cloud-eventarc-publishing` · installs (wheel) · licence: Apache Software License · rank 5750 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-eventarc-publishing/)

<details><summary>README extract</summary>

Eventarc Publishing: Processes events generated by an event provider and delivers them to a
subscriber.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Eventarc Publishing, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-maps-places

Google Maps Places API client library

`pip install google-maps-places` · installs (wheel) · licence: Apache Software License · rank 5776 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-maps-places/)

<details><summary>README extract</summary>

Places API (New): The Places API allows developers to access a variety of search and
retrieval endpoints for a Place.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Places API (New), Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### gcloud

API Client library for Google Cloud

`pip install gcloud` · installs from source (sdist only) · licence: Apache Software License · rank 5778 · last release 2016-09-23 · [PyPI](https://pypi.org/project/gcloud/)

<details><summary>README extract</summary>

Python idiomatic client for Google Cloud Platform services.

Warning: This package has moved. It has been renamed to
google-cloud on PyPI. No new releases will be made for
`gcloud`.

Features:
- Homepage
- API Documentation

This client supports the following Google Cloud Platform services:

- Google Cloud Datastore
- Google Cloud Storage
- Google Cloud Pub/Sub
- Google BigQuery
- Google Cloud Resource Manager ...

Example:
```python
from gcloud import datastore
# Create, populate and persist an entity
entity = datastore.Entity(key=datastore.Key('EntityKind'))
entity.update({
    'foo': u'bar',
    'baz': 1337,
    'qux': False,
})
# Then query for entities
query = datastore.Query(kind='EntityKind')
for result in query.fetch():
    print result
```

...

</details>

### selenium-stealth

Trying to make python selenium more stealthy.

`pip install selenium-stealth` · installs (wheel) · licence: MIT License · rank 5800 · last release 2020-11-05 · [PyPI](https://pypi.org/project/selenium-stealth/)

<details><summary>README extract</summary>

A python package selenium-stealth to prevent detection. This programme is trying to make python selenium more stealthy.

As of now selenium-stealth only support Selenium Chrome.

After using selenium-stealth you can prevent almost all selenium detections. ...

Example:
```python
from selenium import webdriver
from selenium_stealth import stealth
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
...
```

Sections: selenium-stealth, Usage, Args, Test results (red is bad), Selenium without selenium-stealth 😢, Selenium with selenium-stealth 💯

</details>

### google-ads-admanager

Google Ads Admanager API client library

`pip install google-ads-admanager` · installs (wheel) · licence: Apache Software License · rank 5951 · last release 2026-10-08 · [PyPI](https://pypi.org/project/google-ads-admanager/)

<details><summary>README extract</summary>

Google Ad Manager: Manage your Ad Manager inventory, run reports and more.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Google Ad Manager, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### spider-client

Python SDK for Spider Cloud API

`pip install spider-client` · installs (wheel) · licence: MIT · rank 5996 · last release 2026-07-18 · [PyPI](https://pypi.org/project/spider-client/)

<details><summary>README extract</summary>

The Spider Cloud Python SDK offers a toolkit for straightforward website scraping, crawling at scale, and other utilities like extracting links and taking screenshots, enabling you to collect data formatted for compatibility with language models (LLMs). It features a user-friendly interface for seamless integration with the Spider Cloud API.

Example:
```python
from spider import Spider

# Initialize the Spider with your API key
app = Spider(api_key='your_api_key')

# Scrape a single URL
url = '
scraped_data = app.scrape_url(url)

# Crawl a website
crawler_params = {
    'limit': 1,
    'proxy_enabled': True,
    'metadata': False,
    'request': 'http'
}
...
```

...

</details>

### django-ninja-extra

Django Ninja Extra - Class Based Utility and more for Django Ninja(Fast Django REST framework)

`pip install django-ninja-extra` · installs (wheel) · licence: MIT License · rank 6026 · last release 2026-08-17 · [PyPI](https://pypi.org/project/django-ninja-extra/) · [docs](https://eadwincode.github.io/django-ninja-extra/)

<details><summary>README extract</summary>

Django Ninja Extra is a powerful extension for Django Ninja that enhances your Django REST API development experience. It introduces class-based views and advanced features while maintaining the high performance and simplicity of Django Ninja. ...

Example:
```python
from ninja_extra import NinjaExtraAPI, api_controller, http_get

api = NinjaExtraAPI()

# Function-based endpoint example
@api.get("/hello", tags=['Basic'])
def hello(request, name: str = "World"):
    return {"message": f"Hello, {name}!"}

# Class-based controller example
@api_controller('/math', tags=['Math'])
class MathController:
...
```

...

</details>

### google-cloud-billing

Google Cloud Billing API client library

`pip install google-cloud-billing` · installs (wheel) · licence: Apache Software License · rank 6063 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-billing/)

<details><summary>README extract</summary>

Cloud Billing: Allows developers to manage billing for their Google Cloud Platform
projects programmatically.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Billing, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### py-cord

A Python wrapper for the Discord API

`pip install py-cord` · installs (wheel) · licence: MIT · rank 6103 · last release 2026-07-25 · [PyPI](https://pypi.org/project/py-cord/) · [docs](https://docs.pycord.dev) · [source](https://github.com/Pycord-Development/pycord)

<details><summary>README extract</summary>

Pycord is a modern, easy to use, feature-rich, and async ready API wrapper for Discord written in Python.

Pycord supports Python `3.10` - `3.14`

Features:
- Modern Pythonic API using `async` and `await`.
- Proper rate limit handling.
- Optimised for both speed and memory usage.
- Full application API support.

Example:
```python
import discord

bot = discord.Bot()

@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")

@bot.user_command(name="Say Hello")
async def hi(ctx, user):
    await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

bot.run("token")
```

Sections: Note, Key Features, Optional Packages, Quick Example, Traditional Commands Example, Useful Links, Translations

</details>

### google-cloud-bigquery-logging

Google Cloud Bigquery Logging API client library

`pip install google-cloud-bigquery-logging` · installs (wheel) · licence: Apache Software License · rank 6248 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-bigquery-logging/)

<details><summary>README extract</summary>

BigQuery Logging:

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for BigQuery Logging, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### localstack

The LocalStack Command Line Interface

`pip install localstack` · installs (wheel) · licence: Apache-2.0 · rank 6264 · last release 2026-09-28 · [PyPI](https://pypi.org/project/localstack/) · [docs](https://docs.localstack.cloud) · [source](https://github.com/localstack/localstack.git)

<details><summary>README extract</summary>

The command-line interface for LocalStack, a cloud service emulator that runs on your laptop or in your CI environment.

> [!WARNING]
> The `localstack` CLI is deprecated and will no longer receive updates. Please use the new `lstk` CLI instead. You don't need to uninstall this one. ...

Sections: LocalStack CLI, Usage, Releasing, Documentation

</details>

### clickhouse-cityhash

Python-bindings for CityHash, a fast non-cryptographic hash algorithm

`pip install clickhouse-cityhash` · installs (wheel) · licence: MIT License · rank 6306 · last release 2026-07-14 · [PyPI](https://pypi.org/project/clickhouse-cityhash/)

<details><summary>README extract</summary>

A fork of Python wrapper around CityHash
with downgraded version of algorithm. This fork used as 3-rd party library
for hashing data in ClickHouse protocol. Unfortunately ClickHouse
server comes with built-in old version of this algorithm.

Please use original python-cityhash
package for other purposes.

Sections: CityHash, Getting Started, See Also

</details>

### google-maps-addressvalidation

Google Maps Addressvalidation API client library

`pip install google-maps-addressvalidation` · installs (wheel) · licence: Apache Software License · rank 6349 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-maps-addressvalidation/)

<details><summary>README extract</summary>

Address Validation: The Address Validation API allows developers to verify the accuracy of
addresses. Given an address, it returns information about the correctness
of the components of the parsed address, a geocode, and a verdict on the
deliverability of the parsed address.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

...

</details>

### repath

Generate regular expressions form ExpressJS path patterns

`pip install repath` · installs (wheel) · licence: MIT License · rank 6579 · last release 2019-10-08 · [PyPI](https://pypi.org/project/repath/)

<details><summary>README extract</summary>

A port of the pathToRegexp node module to Python. Parses express-style paths to PCRE regular expression patterns, taking advantage of Python's named capture groups.

</details>

### google-cloud-bigquery-connection

Google Cloud Bigquery Connection API client library

`pip install google-cloud-bigquery-connection` · installs (wheel) · licence: Apache Software License · rank 6601 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-bigquery-connection/)

<details><summary>README extract</summary>

BigQuery Connection: Allows users to manage BigQuery connections to external data sources.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for BigQuery Connection, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### pymisp

Python API for MISP.

`pip install pymisp` · installs (wheel) · licence: BSD-2-Clause · rank 6656 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pymisp/) · [docs](https://pymisp.readthedocs.io) · [source](https://github.com/MISP/PyMISP)

<details><summary>README extract</summary>

PyMISP is a Python library to access MISP platforms via their REST API.

PyMISP allows you to fetch events, add or update events/attributes, add or update samples or search for attributes.

Example:
```python
import logging
logger = logging.getLogger('pymisp')

# Configure it as you wish, for example, enable DEBUG mode:
logger.setLevel(logging.DEBUG)
```

Sections: PyMISP - Python Library to access MISP, Running the tests, Samples and how to use PyMISP, Debugging, Test cases, Documentation, Jupyter notebook, Everything is a Mutable Mapping, MISP Objects

</details>

### gcloud-rest-auth

Python Client for Google Cloud Auth

`pip install gcloud-rest-auth` · installs (wheel) · licence: MIT License · rank 6726 · last release 2026-11-04 · [PyPI](https://pypi.org/project/gcloud-rest-auth/) · [source](https://github.com/talkiq/gcloud-aio)

<details><summary>README extract</summary>

This is a shared codebase for `gcloud-rest-auth` and `gcloud-rest-auth`

This library implements an `IamClient` class, which can be used to interact
with GCP public keys and URL sign blobs.

It also implements an `IapToken` class which is used for authorizing against
an Identity-Aware Proxy (IAP) secured GCP service. ...

Sections: (Asyncio OR Threadsafe) Python Client for Google Cloud Auth, Usage

</details>

### google-cloud-common

Google Cloud Common API client library

`pip install google-cloud-common` · installs (wheel) · licence: Apache Software License · rank 6735 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-common/)

<details><summary>README extract</summary>

Common Operation Metadata type: Provides common protobuf definitions for APIs.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Common Operation Metadata type, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-tpu

Google Cloud Tpu API client library

`pip install google-cloud-tpu` · installs (wheel) · licence: Apache Software License · rank 6775 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-tpu/)

<details><summary>README extract</summary>

Cloud TPU: TPU API provides customers with access to Google TPU technology.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud TPU, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### rq-dashboard

rq-dashboard is a general purpose, lightweight, web interface to monitor your RQ queues, jobs, and workers in realtime.

`pip install rq-dashboard` · installs (wheel) · licence: BSD License · rank 6799 · last release 2026-11-06 · [PyPI](https://pypi.org/project/rq-dashboard/)

<details><summary>README extract</summary>

`rq-dashboard` is a general purpose, lightweight,
Flask-based web front-end to monitor your
RQ queues, jobs, and workers in realtime.

Maturity notes

The RQ dashboard is currently being developed and is in beta stage.
How migrate to version 1.0 you can find here

You can find help in the discussion page in github or join our discord server ...

Features:
The upstream project exposes only a Flask blueprint. The application factory in
`rq_dashboard/app.py` wraps that blueprint so that: ...

Sections: Introduction, Why `rq_dashboard/app.py` exists, Dockerfile, Compose service, Reverse proxy (Caddy example)

</details>

### saq

Distributed Python job queue with asyncio and redis

`pip install saq` · installs (wheel) · licence: MIT License · rank 6889 · last release 2026-10-29 · [PyPI](https://pypi.org/project/saq/)

<details><summary>README extract</summary>

SAQ (Simple Async Queue) is a simple and performant job queueing framework built on top of asyncio and redis or postgres. It can be used for processing background jobs with workers. For example, you could use SAQ to schedule emails, execute long queries, or do expensive data analysis.

Documentation

It uses redis-py >= 4.2. ...

Example:
```python
import asyncio

from saq import CronJob, Queue

class DBHelper:
    """Helper class for demo purposes"""

    async def disconnect(self):
        print("Disconnecting from the database")

    async def connect(self):
        print("Connectiong...")

    def str(self):
        return "Your DBHelper at work"

...
```

Sections: SAQ, Usage, Example, Demo, Comparison to ARQ

</details>

### fastapi-debug-toolbar

A debug toolbar for FastAPI.

`pip install fastapi-debug-toolbar` · installs (wheel) · licence: BSD License · rank 6998 · last release 2024-05-04 · [PyPI](https://pypi.org/project/fastapi-debug-toolbar/) · [docs](https://fastapi-debug-toolbar.domake.io) · [source](https://github.com/mongkok/fastapi-debug-toolbar)

<details><summary>README extract</summary>

🐞A debug toolbar for FastAPI based on the original django-debug-toolbar.🐞

Swagger UI & GraphQL are supported.

Documentation:

Example:
```python
from debug_toolbar.middleware import DebugToolbarMiddleware
from fastapi import FastAPI

app = FastAPI(debug=True)
app.add_middleware(DebugToolbarMiddleware)
```

Sections: Debug Toolbar, Quickstart, SQLAlchemy, Tortoise ORM

</details>

### google-cloud-securitycenter

Google Cloud Securitycenter API client library

`pip install google-cloud-securitycenter` · installs (wheel) · licence: Apache Software License · rank 7046 · last release 2026-10-15 · [PyPI](https://pypi.org/project/google-cloud-securitycenter/)

<details><summary>README extract</summary>

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-filestore

Google Cloud Filestore API client library

`pip install google-cloud-filestore` · installs (wheel) · licence: Apache Software License · rank 7048 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-filestore/)

<details><summary>README extract</summary>

Cloud Filestore: The Cloud Filestore API is used for creating and managing cloud file
servers.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Filestore, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-iamconnectorcredentials

Google Cloud Iamconnectorcredentials API client library

`pip install google-cloud-iamconnectorcredentials` · installs (wheel) · licence: Apache Software License · rank 7077 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-iamconnectorcredentials/)

<details><summary>README extract</summary>

iamconnectorcredentials.googleapis.com: iamconnectorcredentials.googleapis.com API.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for iamconnectorcredentials.googleapis.com, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### toml-fmt-common

Common logic to the TOML formatter.

`pip install toml-fmt-common` · installs (wheel) · licence: MIT · rank 7158 · last release 2026-05-29 · [PyPI](https://pypi.org/project/toml-fmt-common/) · [docs](https://github.com/tox-dev/toml-fmt/tree/main/toml-fmt-common#toml-fmt-common) · [source](https://github.com/tox-dev/toml-fmt/tree/main/toml-fmt-common)

<details><summary>README extract</summary>

Contains Python code common to all formatters under the `toml-fmt` umbrella (meant to only be used by that project).

</details>

### scrapfly-sdk

Scrapfly SDK for Scrapfly

`pip install scrapfly-sdk` · installs (wheel) · licence: BSD · rank 7185 · last release 2026-09-08 · [PyPI](https://pypi.org/project/scrapfly-sdk/) · [docs](https://scrapfly.io/docs) · [source](https://github.com/scrapfly/python-sdk)

<details><summary>README extract</summary>

Example:
```python
import os

from llama_index.readers.web import ScrapflyReader
from llama_index.core import VectorStoreIndex

# Initiate ScrapflyReader with your Scrapfly API key
scrapfly_reader = ScrapflyReader(
    api_key="Your Scrapfly API key",  # Get your API key from
    ignore_scrape_failures=True,  # Ignore unprocessable web pages and log their exceptions
...
```

Sections: Scrapfly SDK, Unblocker, `asp` is the deprecated alias, Integrations, LlamaIndex, Usage, LangChain, Get Your API Key, Migration, Migrate from 0.7.x to 0.8, What's new, 0.8.x

</details>

### cloudsmith-cli

Cloudsmith Command-Line Interface (CLI)

`pip install cloudsmith-cli` · installs (wheel) · licence: Apache-2.0 · rank 7267 · last release 2026-10-28 · [PyPI](https://pypi.org/project/cloudsmith-cli/)

<details><summary>README extract</summary>

The Cloudsmith Command Line Interface (CLI) is a Python 3 text-based interface to the API. This allows users, machines and other services to access and integrate smoothly with Cloudsmith without requiring explicit plugins or tools. Be awesome. Automate Everything.

The following asciinema video demonstrates some of the CLI commands: ...

Features:
The CLI currently supports the following commands (and sub-commands):

- `authenticate`|`auth`: Authenticate the CLI against an organization's SAML configuration.
- `check`: Check rate limits and service status. ...

Example:
```python
gpg --import cloudsmith-cli-release-key.asc
gpg --verify cloudsmith-<version>-linux-x86_64-gnu.tar.gz.sig cloudsmith-<version>-linux-x86_64-gnu.tar.gz
```

...

</details>

### pytubefix

Python3 library for downloading YouTube Videos.

`pip install pytubefix` · installs (wheel) · licence: MIT · rank 7334 · last release 2026-10-16 · [PyPI](https://pypi.org/project/pytubefix/)

<details><summary>README extract</summary>

Example:
```python
import asyncio
from pytubefix import AsyncYouTube

URL = "YOUR_VIDEO_URL"

async def main():
    # Initialize AsyncYouTube with OAuth to handle age-restricted content
    yt = AsyncYouTube(URL, use_oauth=True, allow_oauth_cache=True)

    # Fetch all available streams asynchronously
    streams = await yt.streams()
    print("Available Streams:")
...
```

Sections: Python3 Library for Downloading YouTube Videos, Quickstart, Download MP4 Video in Highest Resolution, Download Audio-Only (.m4a), Download a Complete Playlist, Use OAuth Authentication, Specify Output Directory for Downloads, Working with Subtitles/Caption Tracks, View Available Subtitles, Print Subtitle Tracks, Save Subtitles to a Text File, Using Channels, Get Channel Name, Download All Videos from a Channel

</details>

### grafana-api

Yet another Python library for Grafana API

`pip install grafana-api` · installs (wheel) · licence: MIT License · rank 7340 · last release 2020-08-16 · [PyPI](https://pypi.org/project/grafana-api/) · [source](https://github.com/m0nhawk/grafana_api/)

<details><summary>README extract</summary>

Yet another Grafana API library for Python. Support Python 3 only.

You need Python 3 and only the `requests` library installed.

Example:
```python
from grafana_api.grafana_face import GrafanaFace

grafana_api = GrafanaFace(auth='abcde....', host='api.my-grafana-host.com')

# Search dashboards based on tag
grafana_api.search.search_dashboards(tag='applications')

# Find a user by email
user = grafana_api.users.find_user('test@test.com')

# Add user to team 2
...
```

Sections: grafana_api, What is this library for?, Requirements, Quick start, Authentication, Issue tracker

</details>

### instaloader

Download pictures (or videos) along with their captions and other metadata from Instagram.

`pip install instaloader` · installs (wheel) · licence: MIT License · rank 7427 · last release 2026-10-26 · [PyPI](https://pypi.org/project/instaloader/)

<details><summary>README extract</summary>

Instaloader

- downloads **public and private profiles, hashtags, user stories,
 feeds and saved media**,

- downloads comments, geotags and captions of each post,

- automatically detects profile name changes and renames the target
 directory accordingly,

- allows fine-grained customization of filters and where to store
 downloaded media, ...

Sections: How to Automatically Download Pictures from Instagram, Disclaimer

</details>

### jsonrpcserver

Process incoming JSON-RPC 2.0 requests in Python

`pip install jsonrpcserver` · installs (wheel) · licence: MIT · rank 7454 · last release 2026-11-06 · [PyPI](https://pypi.org/project/jsonrpcserver/) · [docs](https://bensynapse.github.io/jsonrpcserver/) · [source](https://github.com/bensynapse/jsonrpcserver)

<details><summary>README extract</summary>

Process incoming JSON-RPC 2.0 requests in Python

 Documentation |
 API reference |
 Examples |
 Changelog |
 Migration

jsonrpcserver takes a JSON-RPC 2.0
request, calls your Python function and gives you the response to send back.
It leaves the networking to you, so it fits into whatever server you already
have.

Features:
- Works with any framework or transport. The docs have tested examples for
 http.server, Flask, Werkzeug, Django, FastAPI, aiohttp, Sanic, Tornado,
 websockets, ZeroMQ and Socket.IO.
- Sync and async: `dispatch` and `async_dispatch`. ...

Example:
```python
from jsonrpcserver import Result, Success, method, serve

@method
def ping() -> Result:
    return Success("pong")

if name == "main":
    serve("localhost", 8000)
```

...

</details>

### google-cloud-service-usage

Google Cloud Service Usage API client library

`pip install google-cloud-service-usage` · installs (wheel) · licence: Apache Software License · rank 7501 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-service-usage/)

<details><summary>README extract</summary>

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Service Usage, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### django-graphql-jwt

JSON Web Token for Django GraphQL.

`pip install django-graphql-jwt` · installs (wheel) · licence: MIT License · rank 7506 · last release 2023-08-04 · [PyPI](https://pypi.org/project/django-graphql-jwt/) · [docs](https://django-graphql-jwt.domake.io) · [source](https://github.com/flavors/django-graphql-jwt)

<details><summary>README extract</summary>

JSON Web Token authentication for Django GraphQL.

Fantastic documentation is available at

Example:
```python
import graphene
import graphql_jwt

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(mutation=Mutation)
```

</details>

### google-cloud-datacatalog-lineage

Google Cloud Datacatalog Lineage API client library

`pip install google-cloud-datacatalog-lineage` · installs (wheel) · licence: Apache Software License · rank 7527 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-datacatalog-lineage/)

<details><summary>README extract</summary>

Data Lineage: Data lineage is a visual map that tracks the entire lifecycle of your data. It shows you where your data comes from (the origin), where it travels (the destinations), and all the changes or transformations that happen along the way.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Data Lineage, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-bigquery-reservation

Google Cloud Bigquery Reservation API client library

`pip install google-cloud-bigquery-reservation` · installs (wheel) · licence: Apache Software License · rank 7593 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-bigquery-reservation/)

<details><summary>README extract</summary>

BigQuery Reservation: A service to modify your BigQuery reservations.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for BigQuery Reservation, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-oauth

OAuth2 for Google APIs

`pip install google-oauth` · does not install on CPython 3.14 · licence: MIT License · rank 7594 · last release ? · [PyPI](https://pypi.org/project/google-oauth/)

<details><summary>README extract</summary>

`google-oauth` aims to implement Google OAuth2.

Sections: Google OAuth Service, Usage, OAuth2 for service accounts, Documentation, TODO

</details>

### google-cloud-appengine-admin

Google Cloud Appengine Admin API client library

`pip install google-cloud-appengine-admin` · installs (wheel) · licence: Apache Software License · rank 7620 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-appengine-admin/)

<details><summary>README extract</summary>

App Engine Admin: Provisions and manages developers' App Engine applications.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for App Engine Admin, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### td-client

Treasure Data API library for Python

`pip install td-client` · installs (wheel) · licence: Apache Software License · rank 7765 · last release 2026-01-29 · [PyPI](https://pypi.org/project/td-client/)

<details><summary>README extract</summary>

Treasure Data API library for Python

`td-client` supports the following versions of Python.

* Python 3.10+
* PyPy

Example:
```python
import tdclient

with tdclient.Client() as td:
    for job in td.jobs():
        print(job.job_id)
```

Sections: Treasure Data API library for Python, Requirements, Examples, Listing jobs, Running jobs, Running jobs via DBAPI2, Importing data, Bulk import, Changing how CSV and TSV columns are read, Type Hints, Running tests, Linting and type checking, Running tests (tox)

</details>

### bigframes

BigQuery DataFrames -- scalable analytics and machine learning with BigQuery

`pip install bigframes` · installs (wheel) · licence: Apache Software License · rank 7841 · last release 2026-11-04 · [PyPI](https://pypi.org/project/bigframes/) · [source](https://github.com/google/bigframes)

<details><summary>README extract</summary>

BigQuery DataFrames (also known as BigFrames) provides a Pythonic DataFrame
and machine learning (ML) API powered by the BigQuery engine. It provides modules
for many use cases, including:

* bigframes.pandas
 is a pandas API for analytics. Many workloads can be
 migrated from pandas to bigframes by just changing a few imports. ...

Features:
BigQuery DataFrames eliminates the "data movement bottleneck." Instead of downloading large datasets to a local environment, BigFrames translates your Python code into optimized SQL executed across BigQuery's distributed compute engine. ...

Example:
```python
import bigframes.pandas as bpd

bpd.options.bigquery.project = your_gcp_project_id  # Optional in BQ Studio.
bpd.options.bigquery.ordering_mode = "partial"  # Recommended for performance.
...

</details>

### google-apps-meet

Google Apps Meet API client library

`pip install google-apps-meet` · installs (wheel) · licence: Apache Software License · rank 7897 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-apps-meet/)

<details><summary>README extract</summary>

Google Meet: Create and manage meetings in Google Meet.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Google Meet, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### scour

Scour SVG Optimizer

`pip install scour` · installs from source (sdist only) · licence: Apache Software License · rank 7957 · last release 2020-11-22 · [PyPI](https://pypi.org/project/scour/)

<details><summary>README extract</summary>

Scour is an SVG optimizer/cleaner that reduces the size of scalable
vector graphics by optimizing structure and removing unnecessary data.

It can be used to create streamlined vector graphics suitable for web
deployment, publishing/sharing or further processing. ...

</details>

### geoip2fast

GeoIP2Fast is the fastest GeoIP2 country/city/asn lookup library that supports IPv4 and IPv6. A search takes less than 0.00003 seconds. It has its own data file updated twice a week with Maxmind-Geolite2-CSV, supports IPv4/IPv6 and is Pure Python!

`pip install geoip2fast` · installs from source (sdist only) · licence: MIT License · rank 7959 · last release 2024-06-21 · [PyPI](https://pypi.org/project/geoip2fast/) · [source](https://github.com/rabuchaim/geoip2fast)

<details><summary>README extract</summary>

GeoIP2Fast is the fastest GeoIP2 country/city/asn lookup library. A search takes less than 0.00003 seconds. It has its own data file updated with Maxmind-Geolite2-CSV, supports IPv4 and IPv6, works on Python3, Pypy3 and is Pure Python! ...

Example:
```python
>>> from geoip2fast import GeoIP2Fast
>>> geoip = GeoIP2Fast(geoip2fast_data_file="/my_data_files_path/geoip2fast-city-asn-ipv6.dat.gz",verbose=True)
GeoIP2Fast v1.2.1 is ready! geoip2fast-city-asn-ipv6.dat.gz loaded with 4.488.721 networks in 0.54506 seconds and using 426.28 MiB.
>>> print(geoip.lookup("191.251.128.1").pp_json())
{
...
```

...

</details>

### google-cloud-bigquery-biglake

Google Cloud Bigquery Biglake API client library

`pip install google-cloud-bigquery-biglake` · installs (wheel) · licence: Apache Software License · rank 7983 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-bigquery-biglake/)

<details><summary>README extract</summary>

BigLake: The BigLake API provides access to BigLake Metastore, a serverless, fully
managed, and highly available metastore for open-source data that can be
used for querying Apache Iceberg tables in BigQuery.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for BigLake, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### django-ninja-jwt

Django Ninja JWT - JSON Web Token for Django-Ninja

`pip install django-ninja-jwt` · installs (wheel) · licence: MIT License · rank 8025 · last release 2026-07-21 · [PyPI](https://pypi.org/project/django-ninja-jwt/) · [docs](https://github.com/eadwinCode/django-ninja-jwt) · [source](https://github.com/eadwinCode/django-ninja-jwt)

<details><summary>README extract</summary>

Ninja JWT is a JSON Web Token (JWT) plugin for Django-Ninja.
This library is a fork of Simple JWT by Jazzband,
a widely-used JWT plugin for the Django REST Framework.

This library does not address any issues present in the original SIMPLE JWT.
It only adds support for Django-Ninja and removes dependencies on DRF. ...

Sections: Ninja JWT, Abstract, Notice, Requirements, Example, Using Ninja Router, Usage

</details>

### google-cloud-monitoring-dashboards

Google Cloud Monitoring Dashboards API client library

`pip install google-cloud-monitoring-dashboards` · installs (wheel) · licence: Apache Software License · rank 8096 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-monitoring-dashboards/)

<details><summary>README extract</summary>

Cloud Monitoring: Manages your Cloud Monitoring data and configurations.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Monitoring, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### django-render-block

Render a particular block from a template to a string.

`pip install django-render-block` · installs (wheel) · licence: ISC License (ISCL) · rank 8098 · last release 2025-05-13 · [PyPI](https://pypi.org/project/django-render-block/) · [docs](https://github.com/clokep/django-render-block/blob/main/README.rst) · [source](https://github.com/clokep/django-render-block)

<details><summary>README extract</summary>

Render the content of a specific block tag from a Django template. Works for
arbitrary template inheritance, even if a block is defined in the child template
but not in the parent. Generally it works like `render_to_string` from Django,
but allows you to specify a block to render.

Features:
* Render a specific block from a template
* Fully supports the Django templating engine
* Partially supports the Jinja2 engine: it does
 not currently process the `extends` tag.

Example:
```python
>>> from render_block import render_block_to_string
>>> print(render_block_to_string('test2.html', 'block1'))
'block1 from test2'
>>> print(render_block_to_string('test2.html', 'block2'))
'block2 from test1'
```

...

</details>

### arcp

arcp (Archive and Package) URI parser and generator

`pip install arcp` · installs (wheel) · licence: Apache License, Version 2.0 · rank 8187 · last release 2020-02-12 · [PyPI](https://pypi.org/project/arcp/)

<details><summary>README extract</summary>

Create/parse arcp (Archive and Package) URIs.

`arcp` provides functions for creating arcp URIs,
which can be used for identifying or parsing hypermedia
files packaged in an archive or package, like a ZIP file. ...

Example:
```python
>>> css = arcp.arcp_name("app.example.com", "css/style.css")
>>> urllib.parse.urljoin(css, "../fonts/foo.woff")
'arcp://name,app.example.com/fonts/foo.woff'
```

Sections: arcp-py, Introduction, Usage

</details>

### google-cloud-agentidentitycredentials

Google Cloud Agentidentitycredentials API client library

`pip install google-cloud-agentidentitycredentials` · installs (wheel) · licence: Apache Software License · rank 8199 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-agentidentitycredentials/)

<details><summary>README extract</summary>

agentidentitycredentials.googleapis.com: agentidentitycredentials.googleapis.com API.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for agentidentitycredentials.googleapis.com, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### fastapi-restful

Quicker FastApi developing tools

`pip install fastapi-restful` · installs (wheel) · licence: MIT License · rank 8222 · last release 2024-05-07 · [PyPI](https://pypi.org/project/fastapi-restful/) · [docs](https://fastapi-restful.netlify.app) · [source](https://github.com/yuval9313/FastApi-RESTful)

<details><summary>README extract</summary>

Quicker FastApi developing tools

Documentation:

Source Code:

Base on:

FastAPI is a modern, fast web framework for building APIs with Python 3.7+.

But if you're here, you probably already knew that!

Features:
This package includes a number of utilities to help reduce boilerplate and reuse common functionality across projects:

* Resource Class: Create CRUD with ease the OOP way with `Resource` base class that lets you implement methods quick. ...

Sections: Features, Requirements

</details>

### buildpg

Query building for the postgresql prepared statements and asyncpg.

`pip install buildpg` · installs (wheel) · licence: MIT License · rank 8224 · last release 2022-03-01 · [PyPI](https://pypi.org/project/buildpg/)

<details><summary>README extract</summary>

Query building for the postgresql prepared statements and asyncpg.

Lots of more powerful features, including full clause construction, multiple values, logic functions,
query pretty-printing and different variable substitution - below is just a very quick summary.
Please check the code and tests for examples.

Simple variable substitution: ...

Example:
```python
from buildpg import render

render('select * from mytable where x=:foo and y=:bar', foo=123, bar='whatever')
>> 'select * from mytable where x=$1 and y=$2', [123, 'whatever']
```

Sections: buildpg, Building Queries, With asyncpg, Operators, Functions

</details>

### fasta2a

Convert an AI Agent into a A2A server! ✨

`pip install fasta2a` · installs (wheel) · licence: MIT · rank 8254 · last release 2026-10-05 · [PyPI](https://pypi.org/project/fasta2a/) · [docs](https://pydantic.github.io/fasta2a) · [source](https://github.com/pydantic/fasta2a)

<details><summary>README extract</summary>

FastA2A is an agentic framework agnostic implementation of the A2A protocol in Python.
The library is designed to be used with any agentic framework, and is not exclusive to Pydantic AI.

Example:
```python
import uuid
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

from fasta2a import FastA2A, Worker
from fasta2a.broker import InMemoryBroker
from fasta2a.schema import Artifact, Message, TaskIdParams, TaskSendParams, TextPart
from fasta2a.storage import InMemoryStorage

...
```

Sections: FastA2A, Usage, Using Pydantic AI, Streaming, Extensions, Output modes, Design, Tasks and Context, Storage

</details>

### rocrate

RO-Crate metadata generator/parser

`pip install rocrate` · installs (wheel) · licence: Apache-2.0 · rank 8351 · last release 2026-10-06 · [PyPI](https://pypi.org/project/rocrate/)

<details><summary>README extract</summary>

ro-crate-py is a Python library to create and consume Research Object Crates. It supports the current RO-Crate 1.3 specification as well as the older RO-Crate 1.2, RO-Crate 1.1 and RO-Crate 1.0.

Example:
```python
from rocrate.rocrate import ROCrate

crate = ROCrate()
paper = crate.add_file("exp/paper.pdf", properties={
    "name": "manuscript",
    "encodingFormat": "application/pdf"
})
table = crate.add_file("exp/results.csv", properties={
    "name": "experimental data",
    "encodingFormat": "text/csv"
})
...
```

...

</details>

### localstack-ext

Extensions for LocalStack

`pip install localstack-ext` · does not install on CPython 3.14 · licence: LicenseRef-All-Rights-Reserved · rank 8375 · last release 2026-03-23 · [PyPI](https://pypi.org/project/localstack-ext/) · [docs](https://docs.localstack.cloud)

### solcast

a simple Python SDK for the Solcast API

`pip install solcast` · installs (wheel) · licence: Apache-2.0 · rank 8377 · last release 2026-10-01 · [PyPI](https://pypi.org/project/solcast/) · [docs](https://solcast.github.io/solcast-api-python-sdk) · [source](https://github.com/Solcast/solcast-api-python-sdk)

<details><summary>README extract</summary>

Python SDK to access the Solcast API

Documentation:

Example:
```python
from solcast import live

res = live.radiation_and_weather(
    latitude=-33.856784,
    longitude=151.215297,
    output_parameters=['air_temp', 'dni', 'ghi']
)
res.to_dict()
res.to_pandas()  # requires optional pandas installation
```

Sections: Solcast API Python SDK, Basic Usage, Docs, Formatters and Linters

</details>

### fastapi-problem

FastAPI support for RFC9457 problems.

`pip install fastapi-problem` · installs (wheel) · licence: Apache-2.0 · rank 8448 · last release 2026-02-10 · [PyPI](https://pypi.org/project/fastapi-problem/) · [docs](https://nrwldev.github.io/fastapi-problem/)

<details><summary>README extract</summary>

`fastapi_problem` is a set of exceptions and handlers for use in fastapi
applications to support easy error management and responses.

Each exception easily marshals to JSON based on the
RFC9457 spec for use in api
errors.

Check the docs for more details. ...

Example:
```python
import fastapi
from fastapi_problem.handler import add_exception_handler, new_exception_handler

app = fastapi.FastAPI()
eh = new_exception_handler()
add_exception_handler(app, eh)

@app.get("/user")
async def get_user():
    raise UserNotFoundError("No user found.")
```

Sections: FastAPI Problems, Custom Errors, Usage

</details>

### rfc9457

Implementation of RFC9457 problems.

`pip install rfc9457` · installs (wheel) · licence: Apache-2.0 · rank 8452 · last release 2026-02-10 · [PyPI](https://pypi.org/project/rfc9457/)

<details><summary>README extract</summary>

`rfc9457` is a set of exceptions to support easy error management and responses
in web based apis.

Each exception easily marshals to JSON based on the
RFC9457 spec for use in api
errors.

This library is currently used to support problem details in both Starlette and FastAPI.

starlette-problem
fastapi-problem ...

Example:
```python
from rfc9457 import NotFoundProblem

class UserNotFoundError(NotFoundProblem):
    title = "User not found."

UserNotFoundError(
    detail="details",
    custom_key="value",
).marshal()
```

Sections: RFC9457 implementation for Python, Custom Errors

</details>

### starlette-problem

Starlette support for RFC9457 problems.

`pip install starlette-problem` · installs (wheel) · licence: Apache-2.0 · rank 8462 · last release 2026-02-10 · [PyPI](https://pypi.org/project/starlette-problem/) · [docs](https://nrwldev.github.io/starlette-problem/)

<details><summary>README extract</summary>

`starlette_problem` is a set of exceptions and handlers for use in starlette
applications to support easy error management and responses.

Each exception easily marshals to JSON based on the
RFC9457 spec for use in api
errors.

Check the docs for more details. ...

Example:
```python
import starlette.applications
from starlette_problem.handler import add_exception_handler

app = starlette.applications.Starlette()
add_exception_handler(app)

@app.get("/user")
async def get_user():
    raise UserNotFoundError("No user found.")
```

Sections: Starlette Problems, Custom Errors, Usage

</details>

### mechanize

Stateful, programmatic web browsing

`pip install mechanize` · installs (wheel) · licence: BSD License · rank 8561 · last release 2024-04-26 · [PyPI](https://pypi.org/project/mechanize/)

<details><summary>README extract</summary>

Stateful programmatic web browsing in Python

- The browser class `mechanize.Browser` implements the
 interface of `urllib2.OpenerDirector`, so any URL can
 be opened not just `http`.

- Easy HTML form filling.

- Convenient link parsing and following.

- Browser history (`.back()` and `.reload()` methods). ...

Sections: mechanize - Automate interaction with HTTP web servers, Major features, Documentation

</details>

### fastapi-decorators

Create decorators for your endpoints using FastAPI dependencies.

`pip install fastapi-decorators` · installs (wheel) · licence: MIT License · rank 8575 · last release 2026-03-30 · [PyPI](https://pypi.org/project/fastapi-decorators/) · [docs](https://github.com/Minibrams/fastapi-decorators) · [source](https://github.com/Minibrams/fastapi-decorators)

<details><summary>README extract</summary>

Example:
```python
from fastapi_decorators import depends
from fastapi import Depends, Header

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != "expected-api-key":
        raise HTTPException(status_code=403, detail="Forbidden")

@app.get("/secure-data")
@depends(Depends(verify_api_key))
def get_secure_data():
    ...
```

Sections: Usage examples, Using `depends()` directly, Simple decorator, Decorator factory, Logging decorator, Custom Response Header decorator, Rate Limiting decorator, Caching decorator, Error Handling decorator, Combining Multiple decorators, Dependency injection with parameters, Satisfying type checkers

</details>

### localstack-core

The core library and runtime of LocalStack

`pip install localstack-core` · installs (wheel) · licence: Apache-2.0 · rank 8839 · last release 2026-03-23 · [PyPI](https://pypi.org/project/localstack-core/) · [docs](https://docs.localstack.cloud)

### ipfshttpclient

Python IPFS HTTP CLIENT library

`pip install ipfshttpclient` · installs (wheel) · licence: MIT License · rank 8866 · last release 2021-03-15 · [PyPI](https://pypi.org/project/ipfshttpclient/) · [docs](https://ipfs.io/ipns/12D3KooWEqnTdgqHnkkwarSrJjeMP2ZJiADWLYADaNvUb6SQNyPF/docs/)

<details><summary>README extract</summary>

Check out the HTTP Client reference for the full command reference.

Note: The `ipfsapi` PIP package and Python module have both been renamed to `ipfshttpclient`!
See the relevant section of the CHANGELOG for details. ...

Example:
```python
>>> import ipfshttpclient
>>> client = ipfshttpclient.connect()  # Connects to: /dns/localhost/tcp/5001/http
>>> res = client.add('test.txt')
>>> res
{'Hash': 'QmWxS5aNTFEc9XbMX1ASvLET1zrqEaTssqt33rVZQCQb22', 'Name': 'test.txt'}
>>> client.cat(res['Hash'])
'fdsafkljdskafjaksdjf\n'
```

Sections: py-ipfs-http-client, Usage, Documentation, Migrating from `0.4.x` to `0.6.0`, Featured Projects, Easy Tasks, Bug reports, Pull requests, Chat with Us (IRC/Matrix)

</details>

### websocket

Websocket implementation for gevent

`pip install websocket` · installs from source (sdist only) · licence: MIT License · rank 8891 · last release 2010-12-03 · [PyPI](https://pypi.org/project/websocket/)

### turbohtml

A fast, fully typed HTML toolkit for Python, powered by a C-accelerated core.

`pip install turbohtml` · installs (wheel) · licence: MIT · rank 8901 · last release 2026-11-07 · [PyPI](https://pypi.org/project/turbohtml/) · [docs](https://turbohtml.readthedocs.io) · [source](https://github.com/tox-dev/turbohtml)

<details><summary>README extract</summary>

A fast, fully typed HTML toolkit for Python with a C-accelerated core: tokenize, parse, query, edit, serialize, and
extract HTML several times faster than the pure-Python alternatives, with free-threading support. The hot path is C; a
thin typed facade is the only Python you touch. It is not a drop-in for the libraries it replaces.

Features:
| Task | API |

| Escape / unescape | `escape`, `unescape` — byte-for-byte with `html.escape`/`html.unescape` |
| Tokenize | `tokenize`, `Tokenizer` — WHATWG streaming tokenizer with incremental `feed`/`close` |
| Parse | `parse`, `parse_fragment`, ...

Example:
```python
import turbohtml
from turbohtml import Formatter, Html

doc = turbohtml.parse("
# Tea
café & cake
")
print([h.text for h in doc.find_all("h1")])  # ['Tea']
...

</details>

### wait-for-it

Wait for service(s) to be available before executing a command.

`pip install wait-for-it` · installs (wheel) · licence: MIT License · rank 9045 · last release 2024-10-13 · [PyPI](https://pypi.org/project/wait-for-it/)

<details><summary>README extract</summary>

> [!IMPORTANT]
> The wait-for-it project has a new home at by now.

Wait for service(s) to be available before executing a command.

`wait-for-it` is a script that will wait on the availability of one or more TCP services (i.e. `host:port`) before executing a user-defined command. ...

Sections: wait-for-it, Demo, Usage, Examples, Related

</details>

### gcloud-aio-datastore

Python Client for Google Cloud Datastore

`pip install gcloud-aio-datastore` · installs (wheel) · licence: MIT License · rank 9097 · last release 2026-11-06 · [PyPI](https://pypi.org/project/gcloud-aio-datastore/) · [source](https://github.com/talkiq/gcloud-aio)

<details><summary>README extract</summary>

This is a shared codebase for `gcloud-aio-datastore` and
 `gcloud-rest-datastore`

</details>

### google-cloud-geminidataanalytics

Google Cloud Geminidataanalytics API client library

`pip install google-cloud-geminidataanalytics` · installs (wheel) · licence: Apache Software License · rank 9214 · last release 2026-10-29 · [PyPI](https://pypi.org/project/google-cloud-geminidataanalytics/)

<details><summary>README extract</summary>

Data Analytics API with Gemini: The Gemini Data Analytics API enables developers to build intelligent data
analytics applications. Leverage AI-powered chat interfaces to allow users
to interact with and analyze structured data using natural language.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Data Analytics API with Gemini, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### centrifuge-python

WebSocket SDK for Centrifugo (and any Centrifuge-based server) on top of Python asyncio library

`pip install centrifuge-python` · installs (wheel) · licence: MIT · rank 9268 · last release 2026-10-20 · [PyPI](https://pypi.org/project/centrifuge-python/)

<details><summary>README extract</summary>

This is a WebSocket real-time SDK for Centrifugo server (and any Centrifuge-based server) on top of Python asyncio library.

> [!TIP]
> If you are looking for Centrifugo server API client – check out pycent instead. ...

Example:
```python
import ssl

ssl_ctx = ssl.create_default_context(cafile="/path/to/ca.pem")

client = Client(
    "wss://localhost:8000/connection/websocket",
    ssl_context=ssl_ctx,
)
```

Sections: centrifuge-python, Custom TLS configuration, Connecting through a proxy, Callbacks should not block, Callbacks should not raise, Run example, Run tests

</details>

### obstore-databaas

(no summary)

`pip install obstore-databaas` · installs (wheel) · licence: MIT License · rank 9326 · last release 2026-08-19 · [PyPI](https://pypi.org/project/obstore-databaas/)

<details><summary>README extract</summary>

[][pypi_link]
[][conda_version]
[][pypi-link]

The simplest, highest-throughput [^1] Python interface to Amazon S3, Google Cloud Storage, Azure Storage, & other S3-compliant APIs, powered by Rust.

- One interface for all backends with no required Python dependencies.
- Sync and async API with full type hinting. ...

Sections: obstore, Documentation

</details>

### google-cloud-datastream

Google Cloud Datastream API client library

`pip install google-cloud-datastream` · installs (wheel) · licence: Apache Software License · rank 9336 · last release 2026-10-15 · [PyPI](https://pypi.org/project/google-cloud-datastream/)

<details><summary>README extract</summary>

Datastream: Datastream is a serverless and easy-to-use change data capture (CDC) and replication service that lets you synchronize data reliably, and with minimal latency.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Datastream, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### gcloud-aio-taskqueue

Python Client for Google Cloud Task Queue

`pip install gcloud-aio-taskqueue` · installs (wheel) · licence: MIT License · rank 9359 · last release 2026-10-02 · [PyPI](https://pypi.org/project/gcloud-aio-taskqueue/) · [source](https://github.com/talkiq/gcloud-aio)

### aiopenapi3

client and validator for OpenAPI3 3.0, OpenAPI 3.1, OpenAPI 3.2, Swagger 2.0

`pip install aiopenapi3` · installs (wheel) · licence: BSD License · rank 9507 · last release 2026-09-26 · [PyPI](https://pypi.org/project/aiopenapi3/) · [docs](https://aiopenapi3.readthedocs.io/) · [source](https://github.com/commonism/aiopenapi3)

<details><summary>README extract</summary>

A Python OpenAPI 3 Specification client and validator for Python 3.

This project is a fork of Dorthu/openapi3.

Features:
* implements …
 * Swagger 2.0
 * OpenAPI 3.0.3
 * OpenAPI 3.1.0
 * OpenAPI 3.2.0
 * description document parsing via pydantic
 * recursive schemas (A.a -> A)
 * request body model creation via pydantic
 * pydantic compatible "format"-type coercion ...

Sections: aiopenapi3, Features, Documentation, Running Tests

</details>

### google-cloud-privilegedaccessmanager

Google Cloud Privilegedaccessmanager API client library

`pip install google-cloud-privilegedaccessmanager` · installs (wheel) · licence: Apache Software License · rank 9547 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-privilegedaccessmanager/)

<details><summary>README extract</summary>

Privileged Access Manager: Privileged Access Manager (PAM) helps you on your journey towards least
privilege and helps mitigate risks tied to privileged access misuse or
abuse. PAM allows you to shift from always-on standing privileges towards
on-demand access with just-in-time, time-bound, and approval-based access
elevations. ...

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

...

</details>

### gcloud-rest-bigquery

Python Client for Google Cloud BigQuery

`pip install gcloud-rest-bigquery` · installs (wheel) · licence: MIT License · rank 9580 · last release 2026-11-04 · [PyPI](https://pypi.org/project/gcloud-rest-bigquery/) · [source](https://github.com/talkiq/gcloud-aio)

<details><summary>README extract</summary>

This is a shared codebase for `gcloud-rest-bigquery` and
 `gcloud-rest-bigquery`

</details>

### iptools

Python utilites for manipulating IPv4 and IPv6 addresses

`pip install iptools` · installs (wheel) · licence: BSD License · rank 9587 · last release 2019-01-07 · [PyPI](https://pypi.org/project/iptools/)

<details><summary>README extract</summary>

Utilities for manipulating IPv4 and IPv6 addresses including a
class that can be used to include CIDR network blocks in Django's
INTERNAL_IPS setting.

Full documentation at

</details>

### google-shopping-type

Google Shopping Type API client library

`pip install google-shopping-type` · installs (wheel) · licence: Apache Software License · rank 9747 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-shopping-type/)

<details><summary>README extract</summary>

Shopping Common Types:

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Shopping Common Types, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### gcloud-rest-taskqueue

Python Client for Google Cloud Task Queue

`pip install gcloud-rest-taskqueue` · installs (wheel) · licence: MIT License · rank 9757 · last release 2026-10-02 · [PyPI](https://pypi.org/project/gcloud-rest-taskqueue/) · [source](https://github.com/talkiq/gcloud-aio)

### python-status

HTTP Status for Humans

`pip install python-status` · installs from source (sdist only) · licence: BSD License · rank 9806 · last release 2015-10-17 · [PyPI](https://pypi.org/project/python-status/)

<details><summary>README extract</summary>

Features:
For every project I was creating a `status.py` file in the root directory. So I thought it's better to release this as a package on PyPi and use it.

Sections: Usage, Why?

</details>

### gcloud-rest-datastore

Python Client for Google Cloud Datastore

`pip install gcloud-rest-datastore` · installs (wheel) · licence: MIT License · rank 9888 · last release 2026-11-06 · [PyPI](https://pypi.org/project/gcloud-rest-datastore/) · [source](https://github.com/talkiq/gcloud-aio)

<details><summary>README extract</summary>

This is a shared codebase for `gcloud-rest-datastore` and
 `gcloud-rest-datastore`

</details>

### aioaws

Asyncio SDK for some AWS services.

`pip install aioaws` · installs (wheel) · licence: MIT License · rank 9999 · last release 2024-08-16 · [PyPI](https://pypi.org/project/aioaws/) · [source](https://github.com/samuelcolvin/aioaws)

<details><summary>README extract</summary>

Asyncio SDK for some AWS services.

This library does not depend on boto, boto3 or any of the other bloated, opaque and mind thumbing AWS SDKs. Instead, it
is written from scratch to provide clean, secure and easily debuggable access to AWS services I want to use. ...

Example:
```python
import asyncio
from aioaws.s3 import S3Client, S3Config
from httpx import AsyncClient

# requires `pip install devtools`
from devtools import debug

async def s3_demo(client: AsyncClient):
    s3 = S3Client(client, S3Config('<access key>', '<secret key>', '<region>', 'my_bucket_name.com'))

    # upload a file:
...
```

Sections: aioaws, S3 Usage, SES, SNS

</details>

### executor

Programmer friendly subprocess wrapper

`pip install executor` · installs (wheel) · licence: MIT License · rank 10051 · last release 2020-11-19 · [PyPI](https://pypi.org/project/executor/)

<details><summary>README extract</summary>

The `executor` package is a simple wrapper for Python's subprocess module
that makes it very easy to handle subprocesses on UNIX systems with proper
escaping of arguments and error checking:

- An object oriented interface is used to execute commands using sane but
 customizable (and well documented) defaults. ...

Sections: executor: Programmer friendly subprocess wrapper, Usage, Command line, Python API, Providing input, Getting output, Running commands as root, Enabling logging, Running remote commands, Running remote commands concurrently, Contact

</details>

### aiomisc

aiomisc - miscellaneous utils for asyncio

`pip install aiomisc` · installs (wheel) · licence: MIT · rank 10117 · last release 2026-10-23 · [PyPI](https://pypi.org/project/aiomisc/) · [docs](https://docs.aiomisc.com/) · [source](https://github.com/aiokitchen/aiomisc)

<details><summary>README extract</summary>

Miscellaneous utils for asyncio.

As a programmer, you are no stranger to the challenges that come with building
and maintaining software applications. One area that can be particularly
difficult is designing the architecture of software that uses asynchronous I/O.

This is where aiomisc comes in. ...

Features:
Problem: Production asyncio applications require significant boilerplate
for logging, graceful shutdown, thread pools, and error handling.

Solution: aiomisc handles infrastructure so you can focus on business logic. ...

Example:
```python
import asyncio
import logging

import aiomisc

log = logging.getLogger(name)

async def main():
    log.info('Starting')
    await asyncio.sleep(3)
    log.info('Exiting')

if name == 'main':
...

</details>

### fastapi-cors

Simple env support of CORS settings for Fastapi applications

`pip install fastapi-cors` · installs (wheel) · licence: MIT License · rank 10259 · last release 2023-07-12 · [PyPI](https://pypi.org/project/fastapi-cors/)

<details><summary>README extract</summary>

A simply scoped abstraction to provide CORS settings via environment variables to a Fastapi application.

Example:
```python
from fastapi import FastAPI

# during this next line `fastapi_cors.env` will read environment variables from .env
from fastapi_cors import CORS

app = FastAPI()

CORS(app)
```

Sections: fastapi-cors, Usage, Opinions, Config, Example Env

</details>

### wafw00f

The Web Application Firewall Fingerprinting Toolkit

`pip install wafw00f` · installs (wheel) · licence: BSD-3-Clause · rank 10281 · last release 2026-01-26 · [PyPI](https://pypi.org/project/wafw00f/) · [docs](https://github.com/EnableSecurity/wafw00f/wiki) · [source](https://github.com/EnableSecurity/wafw00f/tree/master)

<details><summary>README extract</summary>

WAFW00F

 The Web Application Firewall Fingerprinting Tool.

 — From Enable Security

To do its magic, WAFW00F does the following:

- Sends a _normal_ HTTP request and analyses the response; this identifies a
 number of WAF solutions. ...

Example:
```python
$ wafw00f -l

                  ?              ,.   (   .      )        .      "
          __        ??          ("     )  )'     ,'        )  . (`     '`
    (___()'`;   ???          .; )  ' (( (" )    ;(,     ((  (  ;)  "  )")
    /,___ /`                 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( ' )
    \\   \\                 |__||||||||__|

...
```

Sections: How does it work?, What does it detect?, How do I use it?, Via Docker, From source, Final Words

</details>

### google-maps-routing

Google Maps Routing API client library

`pip install google-maps-routing` · installs (wheel) · licence: Apache Software License · rank 10346 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-maps-routing/)

<details><summary>README extract</summary>

Routes: routes.googleapis.com API.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Routes, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### times

Times is a small, minimalistic, Python library for dealing with time conversions between universal time and arbitrary timezones.

`pip install times` · installs (wheel) · licence: BSD License · rank 10395 · last release 2014-08-24 · [PyPI](https://pypi.org/project/times/)

<details><summary>README extract</summary>

NOTE:
This library will not be maintained any further. **You probably want to use
the excellent Arrow library.**

> “There should be one—and preferably only one—obvious way to do it.”

In fact, version 0.7 of times has been rewritten to be implemented on top of
Arrow, so it still provides the Times interface, but you'll already be using
Arrow. ...

Sections: Times, Accepting time, Date Strings, POSIX timestamps, Current time, Presenting times

</details>

### google-shopping-merchant-products

Google Shopping Merchant Products API client library

`pip install google-shopping-merchant-products` · installs (wheel) · licence: Apache Software License · rank 10426 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-shopping-merchant-products/)

<details><summary>README extract</summary>

Shopping Merchant Products: Programmatically manage your Merchant Center Accounts.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Shopping Merchant Products, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-api-keys

Google Cloud Api Keys API client library

`pip install google-cloud-api-keys` · installs (wheel) · licence: Apache Software License · rank 10547 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-api-keys/)

<details><summary>README extract</summary>

API Keys: Manages the API keys associated with developer projects.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for API Keys, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### django-graphiql-debug-toolbar

Django Debug Toolbar for GraphiQL IDE.

`pip install django-graphiql-debug-toolbar` · installs (wheel) · licence: MIT License · rank 10610 · last release 2021-08-28 · [PyPI](https://pypi.org/project/django-graphiql-debug-toolbar/) · [source](https://github.com/flavors/django-graphiql-debug-toolbar)

<details><summary>README extract</summary>

Django Debug Toolbar for GraphiQL IDE.

* Python ≥ 3.6
* Django ≥ 2.2

Sections: Django GraphiQL Debug Toolbar, Dependencies

</details>

### jsonrpcclient

Create JSON-RPC 2.0 requests and parse responses in Python

`pip install jsonrpcclient` · installs (wheel) · licence: MIT · rank 10639 · last release 2026-11-06 · [PyPI](https://pypi.org/project/jsonrpcclient/) · [docs](https://bensynapse.github.io/jsonrpcclient/) · [source](https://github.com/bensynapse/jsonrpcclient)

<details><summary>README extract</summary>

Create JSON-RPC 2.0 requests and parse responses in Python

 Documentation |
 API reference |
 Examples |
 Changelog |
 Migration

jsonrpcclient builds JSON-RPC 2.0
requests and parses the responses. It doesn't send anything, so it works with
any transport: HTTP, websockets, ZeroMQ, or something of your own.

Features:
- Builds requests for any transport. You send them with the library you
 already use.
- No dependencies outside the standard library.
- Typed, with a `py.typed` marker. The package passes mypy and pyright in
 strict mode. ...

Example:
```python
import requests

from jsonrpcclient import Error, Ok, parse, request

url = "
response = requests.post(url, json=request("ping"), timeout=10)
response.raise_for_status()
parsed = parse(response.json())
if isinstance(parsed, Ok):
...

</details>

### pymediawiki

Wikipedia and MediaWiki API wrapper for Python

`pip install pymediawiki` · installs (wheel) · licence: OSI Approved; MIT License · rank 10704 · last release 2024-12-20 · [PyPI](https://pypi.org/project/pymediawiki/)

<details><summary>README extract</summary>

*mediawiki* is a python wrapper and parser for the MediaWiki API. The goal
is to allow users to quickly and efficiently pull data from the MediaWiki site
of their choice instead of worrying about dealing directly with the API. As
such, it does not force the use of a particular MediaWiki site. ...

Example:
```python
>>> from mediawiki import MediaWiki
>>> wikipedia = MediaWiki()
>>> wikipedia.search('washington')
```

Sections: MediaWiki, Documentation, Automated Tests, Quickstart

</details>

### google-cloud-bigquery-analyticshub

Google Cloud Bigquery Analyticshub API client library

`pip install google-cloud-bigquery-analyticshub` · installs (wheel) · licence: Apache Software License · rank 10712 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-bigquery-analyticshub/)

<details><summary>README extract</summary>

Analytics Hub: Exchange data and analytics assets securely and efficiently.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Analytics Hub, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### ecologits

EcoLogits tracks and estimates the energy consumption and environmental impacts of using generative AI models through APIs.

`pip install ecologits` · installs (wheel) · licence: MPL-2.0 · rank 10722 · last release 2026-10-14 · [PyPI](https://pypi.org/project/ecologits/)

<details><summary>README extract</summary>

🌱 EcoLogits tracks the energy consumption and environmental impacts of using generative AI models through APIs.

Read the full documentation on ecologits.ai.

EcoLogits is part of the Code Carbon non-profit — built by volunteers and supported by sponsors. Chat with us on Discord.

> Local compute? Use CodeCarbon. ...

Example:
```python
from ecologits import EcoLogits
from openai import OpenAI

# Initialize EcoLogits
EcoLogits.init(providers=["openai"])

client = OpenAI(api_key="")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Tell me a funny joke!"}
    ]
)

...
```

Sections: 🚀 Usage, Related tools

</details>

### minfraud

MaxMind minFraud API

`pip install minfraud` · installs (wheel) · licence: Apache-2.0 · rank 10818 · last release 2026-07-21 · [PyPI](https://pypi.org/project/minfraud/) · [docs](https://minfraud.readthedocs.io/en/latest/) · [source](https://github.com/maxmind/minfraud-api-python)

<details><summary>README extract</summary>

This package provides an API for the MaxMind minFraud Score, Insights, and
Factors web services as well as the
Report Transaction web service.

Example:
```python
>>> client = Client(42, 'licensekey')
>>> async_client = AsyncClient(42, 'licensekey')
```

Sections: minFraud Python API, Description, Documentation, Usage, Score, Insights and Factors Usage, Report Transactions Usage, Request Validation (for all request methods), Errors, Examples, Score, Insights and Factors Example, Report Transactions Example, Versioning

</details>

### analytics-mcp

MCP server for Google Analytics

`pip install analytics-mcp` · installs (wheel) · licence: Apache-2.0 · rank 10865 · last release 2026-11-06 · [PyPI](https://pypi.org/project/analytics-mcp/) · [source](https://github.com/googleanalytics/google-analytics-mcp.git)

<details><summary>README extract</summary>

This repo contains the source code for running a local or remote multi-tenant
MCP server that interacts with APIs for
Google Analytics.

Join the discussion and ask questions in the
🤖-analytics-mcp channel
on Discord.

The server uses the
Google Analytics Admin API
and
Google Analytics Data API
to provide several
Tools for use with LLMs. ...

Sections: Google Analytics MCP Server, Tools 🛠️, Retrieve account and property information 🟠, Run core reports 📙, Run realtime reports ⏳, Setup instructions 🔧, Configure Python 🐍, Enable APIs in your project ✅, Configure credentials 🔑, Configure Gemini, Configure Claude Code, Multi-tenant HTTP & End-User OAuth 🌐, Deploy with Docker & Google Cloud Run 🐳, Try it out 🥼

</details>

### adaptix

An extremely flexible and configurable data model conversion library

`pip install adaptix` · installs (wheel) · licence: Apache-2.0 · rank 10891 · last release 2026-04-04 · [PyPI](https://pypi.org/project/adaptix/) · [docs](https://adaptix.readthedocs.io/en/latest/) · [source](https://github.com/reagento/adaptix/)

<details><summary>README extract</summary>

An extremely flexible and configurable data model conversion library.

> [!IMPORTANT]
> Adaptix is ready for production!
> The beta version only means there may be some backward incompatible changes, so you need to pin a specific version.

📚 Documentation

Install

Use for model loading and dumping.

Use for converting one model to another.

Example:
```python
from dataclasses import dataclass

from adaptix import Retort

@dataclass
class Book:
    title: str
    price: int

data = {
    "title": "Fahrenheit 451",
    "price": 100,
}

# Retort is meant to be global constant or just one-time created
retort = Retort()

book = retort.load(data, Book)
assert book == Book(title="Fahrenheit 451", price=100)
...
```

Sections: TL;DR, Use cases, Advantages

</details>

### cidr-trie

Store/search CIDR prefixes in a trie structure.

`pip install cidr-trie` · installs (wheel) · licence: MIT License · rank 10914 · last release 2019-07-05 · [PyPI](https://pypi.org/project/cidr-trie/)

<details><summary>README extract</summary>

Store CIDR IP addresses (both v4 and v6) in a trie for easy lookup.

Read the documentation here.

Example:
```python
from cidr_trie import PatriciaTrie

# --- supports IPv4 ---
trie = PatriciaTrie()
trie.insert("0.0.0.0/0", "Internet")
trie.insert("32.0.0.0/9", "RIR-A")
trie.insert("32.128.0.0/9", "RIR-B")
trie.insert("32.32.0.0/16", "another")
trie.insert("32.32.32.0/24", "third")
trie.insert("32.32.32.32/32", "you")
...
```

Sections: cidr-trie, Usage

</details>

### google-compute-engine

Google Compute Engine

`pip install google-compute-engine` · installs from source (sdist only) · licence: Apache Software License · rank 11022 · last release 2019-01-24 · [PyPI](https://pypi.org/project/google-compute-engine/)

### google-cloud-documentai-toolbox

(no summary)

`pip install google-cloud-documentai-toolbox` · installs (wheel) · licence: Apache 2.0 · rank 11146 · last release 2026-10-22 · [PyPI](https://pypi.org/project/google-cloud-documentai-toolbox/)

<details><summary>README extract</summary>

Document AI Toolbox: Document AI Toolbox aims to reduce the friction of managing, manipulating, and extracting information from outputs of Document AI `BatchProcessDocuments()` (JSON files written to user-managed GCS buckets) and `ProcessDocument()` methods, programmatically.

Disclaimer

The Document AI Toolbox is in an experimental state. ...

Sections: Document AI Toolbox, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps

</details>

### google-cloud-notebooks

Google Cloud Notebooks API client library

`pip install google-cloud-notebooks` · installs (wheel) · licence: Apache Software License · rank 11210 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-notebooks/)

<details><summary>README extract</summary>

Notebooks: Notebooks API is used to manage notebook resources in Google Cloud.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Notebooks, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-retail

Google Cloud Retail API client library

`pip install google-cloud-retail` · installs (wheel) · licence: Apache Software License · rank 11230 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-retail/)

<details><summary>README extract</summary>

Vertex AI Search for commerce: AI Commerce Search API is made up of Search, Browse and
Recommendations. These discovery AI solutions help you implement
personalized search, browse and recommendations, based on machine learning
models, across your websites and mobile applications.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

...

</details>

### discord-protos

Discord user settings protobufs.

`pip install discord-protos` · installs (wheel) · licence: MIT License · rank 11305 · last release 2026-11-07 · [PyPI](https://pypi.org/project/discord-protos/)

<details><summary>README extract</summary>

Example:
```python
import base64

from google.protobuf.json_format import ParseDict
from discord_protos import PreloadedUserSettings

settings = PreloadedUserSettings()
payload = ParseDict({
    'status': {
        'status': 'online',
        'custom_status': {
            'text': 'Hello World',
        },
    },
}, settings).SerializeToString()

...
```

Sections: Usage, Example

</details>

### aiocoap

Python CoAP library

`pip install aiocoap` · installs (wheel) · licence: MIT AND BSD-3-Clause · rank 11464 · last release 2025-11-05 · [PyPI](https://pypi.org/project/aiocoap/) · [docs](https://aiocoap.readthedocs.org/) · [source](https://codeberg.org/aiocoap/aiocoap)

<details><summary>README extract</summary>

The aiocoap package is an implementation of CoAP, the Constrained Application
Protocol. It facilitates writing applications that talk to
network enabled embedded ("IoT" / "Internet of Things") devices.

It is written in Python 3 using its native asyncio methods to facilitate
concurrent operations while maintaining an easy to use interface.

Features:
This library supports the following standards in full or partially:

* RFC7252 (CoAP): Supported for clients and servers. Multicast is supported on
 the server side, and partially for clients. ...

Sections: aiocoap – The Python CoAP library, Usage, Features / Standards, Dependencies, Relevant URLs, Licensing

</details>

### google-cloud-bigquery-datapolicies

Google Cloud Bigquery Datapolicies API client library

`pip install google-cloud-bigquery-datapolicies` · installs (wheel) · licence: Apache Software License · rank 11478 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-bigquery-datapolicies/)

<details><summary>README extract</summary>

BigQuery Data Policy: Allows users to manage BigQuery data policies.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for BigQuery Data Policy, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### h2o-authn

H2O Python Clients Authentication Helpers

`pip install h2o-authn` · installs (wheel) · licence: Apache-2.0 · rank 11595 · last release 2026-11-04 · [PyPI](https://pypi.org/project/h2o-authn/) · [docs](https://github.com/h2oai/authn-py#readme) · [source](https://github.com/h2oai/authn-py)

<details><summary>README extract</summary>

H2O Python Clients Authentication Helpers.

Example:
```python
provider = h2o_authn.TokenProvider(...)
aprovider = h2o_authn.AsyncTokenProvider(...)

# Calling the providers directly makes sure that a fresh access token is available
# and returns it.
access_token = provider()
access_token = await aprovider()

# Calling the token() returns h2o_authn.token.Token instance.
token = provider.token()
...
```

Sections: `h2o-authn`, Usage, Examples, Example: Use with H2O.ai MLOps Python CLient, Example: Use with H2O.ai Enterprise Steam Python Client

</details>

### google-cloud-quotas

Google Cloud Quotas API client library

`pip install google-cloud-quotas` · installs (wheel) · licence: Apache Software License · rank 11718 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-quotas/)

<details><summary>README extract</summary>

Cloud Quotas: Cloud Quotas API provides Google Cloud service consumers with management
and observability for resource usage, quotas, and restrictions of the
services they consume.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Quotas, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### tensorizer

A tool for fast PyTorch module, model, and tensor serialization + deserialization.

`pip install tensorizer` · installs (wheel) · licence: MIT License · rank 11781 · last release 2026-04-21 · [PyPI](https://pypi.org/project/tensorizer/) · [source](https://github.com/coreweave/tensorizer)

<details><summary>README extract</summary>

Module, Model, and Tensor Serialization/Deserialization

Extremely fast model loads from HTTP/HTTPS, Redis, and S3 endpoints.
GPT-J (`20GB`) loads at wire-speed (`~5GB/s`) on a 40GbE network, and
is only bottlenecked by the Linux kernel TCP stack.

CoreWeave and our customers use KNative to deploy models as serverless
functions. ...

Example:
```python
import torch
from tensorizer import TensorSerializer
from transformers import AutoModelForCausalLM

model_ref = "EleutherAI/gpt-j-6B"
# For less intensive requirements, swap above with the line below:
# model_ref = "EleutherAI/gpt-neo-125M"
model_name = model_ref.split("/")[-1]
# Change this to your S3 bucket.
s3_bucket = "bucket"
...
```

...

</details>

### sphinx-bootstrap-theme

Sphinx Bootstrap Theme.

`pip install sphinx-bootstrap-theme` · installs (wheel) · licence: MIT License · rank 11796 · last release 2022-02-03 · [PyPI](https://pypi.org/project/sphinx-bootstrap-theme/)

<details><summary>README extract</summary>

This Sphinx theme integrates the Bootstrap CSS / JavaScript
framework with various layout options, hierarchical menu navigation,
and mobile-friendly responsive design. It is configurable, extensible,
and can use any number of different Bootswatch CSS themes.

The theme is introduced and discussed in the following posts: ...

Example:
```python
{# Import the theme's layout. #}
{% extends "!layout.html" %}

{# Add some extra stuff before and use existing with 'super()' call. #}
{% block footer %}

# My footer of awesomeness.

  {{ super() }}
{% endblock %}
```

Sections: Sphinx Bootstrap Theme, Introduction and Demos, Customization, Theme Options, Bootstrap Versions, Extending "layout.html", Adding Custom CSS, Theme Notes, Sphinx, Bootstrap, Packaging

</details>

### google-cloud-certificate-manager

Google Cloud Certificate Manager API client library

`pip install google-cloud-certificate-manager` · installs (wheel) · licence: Apache Software License · rank 11800 · last release 2026-10-22 · [PyPI](https://pypi.org/project/google-cloud-certificate-manager/)

<details><summary>README extract</summary>

Certificate Manager: Certificate Manager simplifies the acquisition, deployment, and management of Transport Layer Security (TLS) certificates.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Certificate Manager, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### whoisdomain

Python package for retrieving WHOIS information of domains.

`pip install whoisdomain` · installs (wheel) · licence: MIT · rank 11823 · last release 2026-08-06 · [PyPI](https://pypi.org/project/whoisdomain/) · [source](https://github.com/mboot-github/WhoisDomain/)

<details><summary>README extract</summary>

- A Python package for retrieving WHOIS information of DOMAIN'S ONLY.
- Python >=3.10

 - whodap>=0.1.16 .
 - tld>=0.13.2 .
 - redis (optional) .
- v1 uses only whois and has been be moved to maintenance only
- v2 will use whodap to first retrieve info with rdap, if no data is available try the classic whois approach. ...

Features:
* See: Features

Sections: whoisdomain, Notes, A), Versioning, Features, Dependencies, Notes for Mac users, Issues, Usage example, Updates, 2.20260709.1, 2.20260805.1, 2.20260805.2

</details>

### google-apps-card

Google Apps Card API client library

`pip install google-apps-card` · installs (wheel) · licence: Apache Software License · rank 11843 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-apps-card/)

<details><summary>README extract</summary>

Google Apps Card: Card interface displayed in a Google Chat message or Google Workspace Add-on.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Google Apps Card, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-ads-datamanager

Google Ads Datamanager API client library

`pip install google-ads-datamanager` · installs (wheel) · licence: Apache Software License · rank 11844 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-ads-datamanager/)

<details><summary>README extract</summary>

Data Manager: A unified ingestion API for data partners, agencies and advertisers to
connect first-party data across Google advertising products.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Data Manager, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### twitter-ads

A Twitter supported and maintained Ads API SDK for Python.

`pip install twitter-ads` · installs (wheel) · licence: MIT License · rank 11874 · last release 2022-05-27 · [PyPI](https://pypi.org/project/twitter-ads/)

### ai

AI Agent Framework for Python

`pip install ai` · installs (wheel) · licence: Apache-2.0 · rank 11955 · last release 2026-11-04 · [PyPI](https://pypi.org/project/ai/) · [source](https://github.com/vercel-labs/ai-python)

<details><summary>README extract</summary>

A toolkit for building LLM-powered applications and agent loops.

> [!NOTE]
> The AI SDK for Python is in public beta.

Example:
```python
import asyncio
import ai

@ai.tool
async def contact_mothership(query: str) -> str:
    """Contact the mothership for important decisions."""
    return "Soon."

async def main() -> None:
    model = ai.get_model("anthropic/claude-sonnet-4")
    agent = ai.Agent(tools=[contact_mothership])

    messages = [
        ai.system_message(
...
```

Sections: AI SDK for Python, Quick Start, Models, Agents, Hooks, Examples

</details>

### google-maps-routeoptimization

Google Maps Routeoptimization API client library

`pip install google-maps-routeoptimization` · installs (wheel) · licence: Apache Software License · rank 12013 · last release 2026-11-05 · [PyPI](https://pypi.org/project/google-maps-routeoptimization/)

<details><summary>README extract</summary>

Route Optimization: The Route Optimization API assigns tasks and routes to a vehicle fleet,
optimizing against the objectives and constraints that you supply for your
transportation goals.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Route Optimization, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### safe-netrc

Safe netrc file parser

`pip install safe-netrc` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 12076 · last release 2022-11-29 · [PyPI](https://pypi.org/project/safe-netrc/) · [source](https://git.ligo.org/computing/safe-netrc)

_README extract left out: share-alike licence._

### google-apps-chat

Google Apps Chat API client library

`pip install google-apps-chat` · installs (wheel) · licence: Apache Software License · rank 12366 · last release 2026-11-05 · [PyPI](https://pypi.org/project/google-apps-chat/)

<details><summary>README extract</summary>

Google Chat: The Google Chat API lets you build Chat apps to integrate your services
with Google Chat and manage Chat resources such as spaces, members, and
messages.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Google Chat, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### cloudml-hypertune

A library to report Google CloudML Engine HyperTune metrics.

`pip install cloudml-hypertune` · installs from source (sdist only) · licence: Apache Software License · rank 12445 · last release 2019-12-18 · [PyPI](https://pypi.org/project/cloudml-hypertune/)

<details><summary>README extract</summary>

Helper Functions for CloudML Engine Hypertune Services.

- Google CloudML Engine Overview.

- Google CloudML Engine Hyperparameter Tuning
 Overview.

Example:
```python
import hypertune

hpt = hypertune.HyperTune()
hpt.report_hyperparameter_tuning_metric(
    hyperparameter_metric_tag='my_metric_tag',
    metric_value=0.987,
    global_step=1000)
```

Sections: Metric Reporting Python Package for CloudML Hypertune, Prerequisites, Usage, Licensing

</details>

### news-please

news-please is an open source easy-to-use news extractor that just works.

`pip install news-please` · installs (wheel) · licence: Apache Software License · rank 12541 · last release 2025-09-21 · [PyPI](https://pypi.org/project/news-please/)

<details><summary>README extract</summary>

news-please is an open source, easy-to-use news crawler that extracts structured information from almost any news website. It can follow recursively internal hyperlinks and read RSS feeds to fetch both most recent and also old, archived articles. You only need to provide the root URL of the news website. ...

</details>

### google-maps-geocode

Google Maps Geocode API client library

`pip install google-maps-geocode` · installs (wheel) · licence: Apache Software License · rank 12573 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-maps-geocode/)

<details><summary>README extract</summary>

Geocoding: Convert addresses into geographic coordinates (geocoding), which you can
use to place markers or position the map. This API also allows you to
convert geographic coordinates into an address (reverse geocoding).

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Geocoding, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-shopping-merchant-datasources

Google Shopping Merchant Datasources API client library

`pip install google-shopping-merchant-datasources` · installs (wheel) · licence: Apache Software License · rank 12649 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-shopping-merchant-datasources/)

<details><summary>README extract</summary>

Shopping Merchant Data Sources: Programmatically manage your Merchant Center Accounts.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Shopping Merchant Data Sources, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### grafeas

Grafeas API client library

`pip install grafeas` · installs (wheel) · licence: Apache Software License · rank 12659 · last release 2026-10-01 · [PyPI](https://pypi.org/project/grafeas/)

<details><summary>README extract</summary>

Container Analysis: An implementation of the Grafeas API, which stores, and enables querying and
retrieval of critical metadata about all of your software artifacts.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Container Analysis, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### status

HTTP status code reporting for GET and POST requests

`pip install status` · installs (wheel) · licence: MIT License · rank 12764 · last release 2015-01-07 · [PyPI](https://pypi.org/project/status/)

### pylast

A Python interface to Last.fm and Libre.fm

`pip install pylast` · installs (wheel) · licence: Apache-2.0 · rank 12870 · last release 2026-09-29 · [PyPI](https://pypi.org/project/pylast/) · [source](https://github.com/pylast/pylast)

<details><summary>README extract</summary>

A Python interface to Last.fm and other API-compatible websites
such as Libre.fm.

Use the pydoc utility for help on usage or see tests/ for examples.

Features:
- Simple public interface.
- Access to all the data exposed by the Last.fm web services.
- Scrobbling support.
- Full object-oriented design.
- Proxy support.
- Internal caching support for some web services calls (disabled by default). ...

Example:
```python
import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from  for Last.fm
API_KEY = "b25b959554ed76058ac220b7b2e0a026"  # this is a sample key
API_SECRET = "425b55975eed76058ac220b7b4e8a054"

# In order to perform a write operation you need to authenticate yourself
username = "your_user_name"
...
```

...

</details>

### google-cloud-recommender

Google Cloud Recommender API client library

`pip install google-cloud-recommender` · installs (wheel) · licence: Apache Software License · rank 12883 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-recommender/)

<details><summary>README extract</summary>

Recommender: Recommenders generate recommendations that fall into six value categories that can help you optimize your cloud in a variety of ways.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Recommender, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-containeranalysis

Google Cloud Containeranalysis API client library

`pip install google-cloud-containeranalysis` · installs (wheel) · licence: Apache Software License · rank 12954 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-containeranalysis/)

<details><summary>README extract</summary>

Container Analysis: This API is a prerequisite for leveraging Artifact Analysis
scanning capabilities in both Artifact Registry and with Advanced
Vulnerability Insights (runtime scanning) in GKE. ...

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Container Analysis, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### google-cloud-deploy

Google Cloud Deploy API client library

`pip install google-cloud-deploy` · installs (wheel) · licence: Apache Software License · rank 13061 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-deploy/)

<details><summary>README extract</summary>

Cloud Deploy: Cloud Deploy is a service that automates delivery of your applications to a series of target environments in a defined sequence.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Cloud Deploy, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### bigquery-magics

Google BigQuery magics for Jupyter and IPython

`pip install bigquery-magics` · installs (wheel) · licence: Apache Software License · rank 13193 · last release 2026-10-23 · [PyPI](https://pypi.org/project/bigquery-magics/)

<details><summary>README extract</summary>

Querying massive datasets can be time consuming and expensive without the
right hardware and infrastructure. Google BigQuery solves this problem by
enabling super-fast, SQL queries against append-mostly tables, using the
processing power of Google's infrastructure.

- Library Documentation
- Product Documentation

Example:
```python
%%bigquery
SELECT name, SUM(number) as count
FROM 'bigquery-public-data.usa_names.usa_1910_current'
GROUP BY name
ORDER BY count DESC
LIMIT 3
```

Sections: IPython Magics for BigQuery, Quick Start, Mac/Linux, Windows, Example Usage, Perform a query

</details>

### apitally

Simple API monitoring & analytics for REST APIs built with FastAPI, Flask, Django, Starlette, Litestar and BlackSheep.

`pip install apitally` · installs (wheel) · licence: MIT License · rank 13213 · last release 2026-10-21 · [PyPI](https://pypi.org/project/apitally/) · [docs](https://docs.apitally.io) · [source](https://github.com/apitally/apitally-py)

<details><summary>README extract</summary>

API monitoring & analytics made simple

Metrics, logs, traces, and alerts for your APIs — with just a few lines of code.

Apitally is a simple API monitoring and analytics tool that makes it easy to understand API usage, monitor performance, and troubleshoot issues.
Get started in minutes by just adding a few lines of code. ...

Features:
- API analytics: Traffic, error and performance metrics for your API, each endpoint, and per API consumer. Drill down from metrics to individual API requests. ...

Example:
```python
import apitally
from fastapi import FastAPI

app = FastAPI()
apitally.init(app, write_token="your-write-token", env="dev")
```

...

</details>

### google-shopping-merchant-accounts

Google Shopping Merchant Accounts API client library

`pip install google-shopping-merchant-accounts` · installs (wheel) · licence: Apache Software License · rank 13420 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-shopping-merchant-accounts/)

<details><summary>README extract</summary>

Shopping Merchant Accounts: Programmatically manage your Merchant Center Accounts.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Shopping Merchant Accounts, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### trendspy

A Python library for accessing Google Trends data

`pip install trendspy` · installs (wheel) · licence: MIT License · rank 13458 · last release 2024-12-25 · [PyPI](https://pypi.org/project/trendspy/) · [source](https://github.com/sdil87/trendspy.git)

<details><summary>README extract</summary>

Python library for accessing Google Trends data.

Features:
Explore
- Track popularity over time (`interest_over_time`)
- Analyze geographic distribution (`interest_by_region`)
- Compare interest across different timeframes and regions (multirange support) ...

Example:
```python
from trendspy import Trends
tr = Trends()
df = tr.interest_over_time(['python', 'javascript'])
df.plot(title='Python vs JavaScript Interest Over Time',
        figsize=(12, 6))
```

Sections: TrendsPy, Key Features, Basic Usage, Advanced Features, Search Categories and Locations, Real-time Trending Searches and News, Independent Historical Data for Multiple Keywords, Geographic Analysis, Timeframe Formats, Multirange Interest Over Time, Documentation, Disclaimer

</details>

### discord.py-self

A Python wrapper for the Discord user API

`pip install discord.py-self` · installs (wheel) · licence: MIT License · rank 13515 · last release 2026-01-18 · [PyPI](https://pypi.org/project/discord.py-self/) · [docs](https://discordpy-self.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

A modern, easy-to-use, feature-rich, and async-ready API wrapper for Discord's user API written in Python.

| Note:
| Automating user accounts is against the Discord ToS. This library is a proof of concept and I cannot recommend using it. Do so at your own risk.

| Credits:

- Rapptz for the original library this fork is based on. ...

Features:
- Modern Pythonic API using `async` and `await`.
- Proper rate limit handling.
- Optimised in both speed and memory.
- Mostly compatible with the upstream `discord.py`.
- Prevents user account automation detection. ...

Example:
```python
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # only respond to ourselves
...

</details>

### django-queryable-properties

Write Django model properties that can be used in database queries.

`pip install django-queryable-properties` · installs (wheel) · licence: BSD License · rank 13587 · last release 2026-08-06 · [PyPI](https://pypi.org/project/django-queryable-properties/)

<details><summary>README extract</summary>

*django-queryable-properties* is a Django extension that allows to implement model properties which can be used
in database queries performed via Django's ORM.

Further information, including supported Python and Django versions as well as installation instructions, can be found
in the documentation hosted by readthedocs.

Sections: django-queryable-properties, 1.13.0 (2026-08-06), 1.12.1 (2025-12-04), 1.12.0 (2025-08-07), 1.11.0 (2025-05-13), 1.10.1 (2025-04-02), 1.10.0 (2025-01-28), 1.9.3 (2024-08-08), 1.9.2 (2024-03-06), 1.9.1 (2024-01-09), 1.9.0 (2023-12-05), 1.8.5 (2023-11-13), 1.8.4 (2023-04-05), 1.8.3 (2022-08-06)

</details>

### fastapi-slim

FastAPI framework, high performance, easy to learn, fast to code, ready for production

`pip install fastapi-slim` · installs (wheel) · licence: MIT · rank 13641 · last release 2026-02-21 · [PyPI](https://pypi.org/project/fastapi-slim/) · [docs](https://fastapi.tiangolo.com/) · [source](https://github.com/fastapi/fastapi)

<details><summary>README extract</summary>

FastAPI framework, high performance, easy to learn, fast to code, ready for production

Documentation:

Source Code:

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

⚠️ Do not install this package. ⚠️ ...

</details>

### flask-prometheus-metrics

Prometheus Metrics for Flask Web App

`pip install flask-prometheus-metrics` · installs (wheel) · licence: MIT License · rank 13710 · last release 2019-06-06 · [PyPI](https://pypi.org/project/flask-prometheus-metrics/)

<details><summary>README extract</summary>

Prometheus metrics exporter for Flask web applications.

``flask_prometheus_metrics`` uses official Prometheus Python Client
providing basic metrics about process resource usage, app's requests metrics and information.

Example:
```python
from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

app = Flask(name)

@app.route("/")
def index():
    return "Test"

...
```

...

</details>

### google-cloud-api-gateway

Google Cloud Api Gateway API client library

`pip install google-cloud-api-gateway` · installs (wheel) · licence: Apache Software License · rank 13740 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-api-gateway/)

<details><summary>README extract</summary>

API Gateway: API Gateway enables you to provide secure access to your backend services through a well-defined REST API that is consistent across all of your services, regardless of the service implementation.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for API Gateway, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### aioauth

Asynchronous OAuth 2.0 framework for Python 3.

`pip install aioauth` · installs (wheel) · licence: MIT License · rank 13877 · last release 2026-07-26 · [PyPI](https://pypi.org/project/aioauth/)

<details><summary>README extract</summary>

`aioauth` implements OAuth 2.0 protocol and can be used in asynchronous frameworks like FastAPI / Starlette, aiohttp. It can work with any databases like `MongoDB`, `PostgreSQL`, `MySQL` and ORMs like gino, sqlalchemy or databases over simple BaseStorage interface.

Features:
There are few great OAuth frameworks for Python like oauthlib and authlib, but they do not support asyncio and rewriting these libraries to asyncio is a significant challenge (see issues here and here).

Sections: Asynchronous OAuth 2.0 framework for Python 3, Why this project exists?, Examples, API Reference and User Guide

</details>

### google-cloud-runtimeconfig

Google Cloud RuntimeConfig API client library

`pip install google-cloud-runtimeconfig` · installs (wheel) · licence: Apache Software License · rank 14034 · last release 2026-09-29 · [PyPI](https://pypi.org/project/google-cloud-runtimeconfig/)

<details><summary>README extract</summary>

Google Cloud Runtime Configurator API:

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Google Cloud Runtime Configurator API, Quick Start, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### httplib2shim

A wrapper over urllib3 that matches httplib2's interface

`pip install httplib2shim` · installs from source (sdist only) · licence: Apache Software License · rank 14065 · last release 2017-06-26 · [PyPI](https://pypi.org/project/httplib2shim/)

<details><summary>README extract</summary>

`httplib2shim` is a wrapper over `httplib2` that uses `urllib3` to perform HTTP requests. This library is intended to help existing legacy libraries (and their users) to migrate away from `httplib2`. It is not intended to be a general purpose replacement for `httplib2`. ...

Example:
```python
import httplib2shim
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()
http = httplib2shim.Http()
credentials.authorize(http)

# http is now authorized with OAuth2 credentials and uses urllib3 under
# the covers.
```

Sections: httplib2shim, Usage, Licensing

</details>

### google-cloud-bigquery-data-exchange

Google Cloud Bigquery Data Exchange API client library

`pip install google-cloud-bigquery-data-exchange` · installs (wheel) · licence: Apache Software License · rank 14164 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-bigquery-data-exchange/)

<details><summary>README extract</summary>

Analytics Hub: Exchange data and analytics assets securely and efficiently.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Analytics Hub, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### PyLink

Universal communication interface using File-Like API

`pip install PyLink` · installs from source (sdist only) · licence: BSD License · rank 14284 · last release 2017-11-29 · [PyPI](https://pypi.org/project/PyLink/)

<details><summary>README extract</summary>

Pylink offers a universal communication interface using File-Like API.
For now, only the TCP, UDP, Serial and GSM interfaces are
supported.

The aim of this project is to allow any type of communication.
It is best suited for projects that have various ways of communicating
including IP remote or local serial communication.

Example:
```python
>>> from pylink import TCPLink, link_from_url
>>> link = TCPLink('localhost', 7) # conntect to echo tcp service
>>> link.write('Hello')
2012-06-05 12:44:06,211 INFO: new <TCPLink tcp:127.0.0.1:7> was initialized
2012-06-05 12:44:06,211 INFO: Write : <b'hello'>
>>> link.read() == 'Hello'
2012-06-05 12:44:06,312 INFO: Read : <'hello'>
True
```

...

</details>

### django-invitations

Generic invitations app with support for django-allauth

`pip install django-invitations` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 14358 · last release 2023-11-22 · [PyPI](https://pypi.org/project/django-invitations/) · [docs](https://django-invitations.readthedocs.io/en/latest/) · [source](https://github.com/jazzband/django-invitations/)

_README extract left out: share-alike licence._

### google-cloud-webrisk

Google Cloud Webrisk API client library

`pip install google-cloud-webrisk` · installs (wheel) · licence: Apache Software License · rank 14369 · last release 2026-10-01 · [PyPI](https://pypi.org/project/google-cloud-webrisk/)

<details><summary>README extract</summary>

Web Risk: Web Risk is an enterprise security product that lets your client applications check URLs against Google's constantly updated lists of unsafe web resources.

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Web Risk, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

### ministack

Free, open-source local AWS emulator — drop-in LocalStack replacement

`pip install ministack` · installs (wheel) · licence: MIT License · rank 14615 · last release 2026-11-05 · [PyPI](https://pypi.org/project/ministack/) · [source](https://github.com/ministackorg/ministack)

<details><summary>README extract</summary>

Free, open-source local AWS emulator. Free forever.

60+ AWS services on a single port · Multi-account & multi-region · Terraform compatible · Real databases · MIT licensed

 Ministack.org · Docker Hub · LinkedIn

Features:
LocalStack recently moved its core services behind a paid plan. If you relied on LocalStack Community for local development and CI/CD pipelines, MiniStack is your free alternative.

- 60+ AWS services emulated on a single port (4566) ...

Example:
```python
boto3.client("s3",
    endpoint_url="
    aws_access_key_id="048408301323",
    aws_secret_access_key="test",
)
```

...

</details>

### PyCampbellCR1000

Communication tools for Campbell CR1000-type Dataloggers

`pip install PyCampbellCR1000` · installs from source (sdist only) · licence: GNU General Public License v3 (GPLv3) · rank 14643 · last release 2017-11-29 · [PyPI](https://pypi.org/project/PyCampbellCR1000/)

_README extract left out: share-alike licence._

### distconfig3

Library to manage configuration using Zookeeper, Etcd, Consul

`pip install distconfig3` · installs (wheel) · licence: Apache Software License · rank 14703 · last release 2020-11-12 · [PyPI](https://pypi.org/project/distconfig3/)

<details><summary>README extract</summary>

This is a fork of distconfig removing Python 2.7 support as well as six
and ujson dependencies.

Library to manage distributed configuration using either ZooKeeper or
Etcd or Consul. ...

Example:
```python
from kazoo import client

from distconfig import Proxy

client = client.KazooClient()
# The user must call `KazooClient.start()` before using this particular
# backend
client.start()

proxy = Proxy.configure(
    'distconfig.backends.zookeeper.ZooKeeperBackend',
    client=client,
)

# config is a read only mapping-like object.
...
```

Sections: distconfig3, Rational, Usage, TODO

</details>

### google-cloud-dialogflow

Google Cloud Dialogflow API client library

`pip install google-cloud-dialogflow` · installs (wheel) · licence: Apache Software License · rank 14725 · last release 2026-10-22 · [PyPI](https://pypi.org/project/google-cloud-dialogflow/)

<details><summary>README extract</summary>

Dialogflow: Builds conversational interfaces (for example, chatbots, and voice-powered
apps and devices).

- Client Library Documentation
- Product Documentation

Example:
```python
import logging

from google.cloud import library_v1

base_logger = logging.getLogger("google")
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
```

Sections: Python Client for Dialogflow, Quick Start, Code samples and snippets, Mac/Linux, Windows, Next Steps, Logging, Simple, environment-based configuration, Environment-Based Examples, Advanced, code-based configuration, Code-Based Examples, Logging details

</details>

## Also in this topic

- [sqlmodel](database.md#sqlmodel) - SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness.
- [pika](communications.md#pika) - Pika Python AMQP Client Library
- [paho-mqtt](communications.md#paho-mqtt) - MQTT version 5.0/3.1.1 client class
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [autobahn](communications.md#autobahn) - WebSocket client & server library, WAMP real-time framework
- [python-telegram-bot](communications-chat.md#python-telegram-bot) - We have made you a wrapper you can't refuse
- [pamqp](communications.md#pamqp) - RabbitMQ Focused AMQP low-level library
- [dbos](database.md#dbos) - Ultra-lightweight durable execution in Python
- [python-ldap](database.md#python-ldap) - Python modules for implementing LDAP clients
- [mleap](communications-chat.md#mleap) - MLeap Python API
- [IMAPClient](communications-email.md#imapclient) - Easy-to-use, Pythonic and complete IMAP client library
- [IPy](communications.md#ipy) - Class and tools for handling of IPv4 and IPv6 addresses and networks
- [TgCrypto](communications.md#tgcrypto) - Fast and Portable Cryptography Extension Library for Pyrogram
- [aioimaplib](communications-email.md#aioimaplib) - Python asyncio IMAP4rev1 client library
- [Pyrogram](communications.md#pyrogram) - Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots
- [feedgen](communications.md#feedgen) - Feed Generator (ATOM, RSS, Podcasts)
- [AMQPStorm](communications.md#amqpstorm) - Thread-safe Python3 RabbitMQ Client & Management library.
- [bitmath](communications-file-sharing.md#bitmath) - Pythonic module for representing and manipulating file sizes with different prefix notations (file size unit conversion)
- [pyfcm](communications.md#pyfcm) - Python client for FCM - Firebase Cloud Messaging (Android, iOS and Web)
- [ciscoconfparse](communications.md#ciscoconfparse) - Parse, Audit, Query, Build, and Modify Cisco IOS-style and JunOS-style configs
- [grafana-client](communications.md#grafana-client) - A client library for accessing the Grafana HTTP API, written in Python
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
- [sumy](education.md#sumy) - Module for automatic summarization of text documents and HTML pages.
- [censys](documentation-sphinx.md#censys) - An easy-to-use and lightweight API wrapper for Censys APIs (censys.io).
- [python-twitter](communications-chat.md#python-twitter) - A Python wrapper around the Twitter API
- [tb-paho-mqtt-client](communications.md#tb-paho-mqtt-client) - MQTT version 5.0/3.1.1 client class
- [Hydrogram](communications.md#hydrogram) - Sleek, advanced, and asynchronous Telegram MTProto API framework in Python, designed for fluid user and bot interactions.
- [createsend](communications.md#createsend) - A library which implements the complete functionality of the Campaign Monitor API.
- [twython](communications-chat.md#twython) - Actively maintained, pure Python wrapper for the Twitter API. Supports both normal and streaming Twitter APIs
- [amqtt](communications.md#amqtt) - Python's asyncio-native MQTT broker and client.
- [Kurigram](communications.md#kurigram) - Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots
- [email-normalize](communications.md#email-normalize) - Return a normalized email-address stripping ISP specific behaviors
- [odmantic](database.md#odmantic) - ODMantic, an AsyncIO MongoDB Object Document Mapper for Python using type hints
- [cose](communications.md#cose) - CBOR Object Signing and Encryption (COSE) implementation
