# Unclassified / O

[Index](README.md) · 419 packages in this topic, by downloads.

### opentelemetry-api

OpenTelemetry Python API

`pip install opentelemetry-api` · installs (wheel) · licence: Apache-2.0 · rank 41 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-api/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

Sections: OpenTelemetry Python API, References

</details>

### openpyxl

A Python library to read/write Excel 2010 xlsx/xlsm files

`pip install openpyxl` · installs (wheel) · licence: MIT License · rank 103 · last release 2024-06-28 · [PyPI](https://pypi.org/project/openpyxl/) · [docs](https://openpyxl.readthedocs.io/en/stable/) · [source](https://foss.heptapod.net/openpyxl/openpyxl)

<details><summary>README extract</summary>

openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.

It was born from lack of existing library to read/write natively from Python
the Office Open XML format.

All kudos to the PHPExcel team as openpyxl was initially based on PHPExcel.

Example:
```python
from openpyxl import Workbook
wb = Workbook()

# grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells
ws['A1'] = 42

# Rows can also be appended
ws.append([1, 2, 3])

# Python types will automatically be converted
import datetime
ws['A2'] = datetime.datetime.now()

# Save the file
wb.save("sample.xlsx")
```

Sections: Introduction, Mailing List, Documentation

</details>

### opentelemetry-semantic-conventions

OpenTelemetry Semantic Conventions

`pip install opentelemetry-semantic-conventions` · installs (wheel) · licence: Apache-2.0 · rank 107 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-semantic-conventions/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This library contains generated code for the semantic conventions defined by the OpenTelemetry specification.

Sections: OpenTelemetry Semantic Conventions, Code Generation, References

</details>

### opentelemetry-sdk

OpenTelemetry Python SDK

`pip install opentelemetry-sdk` · installs (wheel) · licence: Apache-2.0 · rank 109 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-sdk/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

Sections: OpenTelemetry Python SDK, References

</details>

### opentelemetry-proto

OpenTelemetry Python Proto

`pip install opentelemetry-proto` · installs (wheel) · licence: Apache-2.0 · rank 128 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-proto/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This library contains the generated code for OpenTelemetry protobuf data model. The code in the current
package was generated using the v1.10.0 release of opentelemetry-proto.

Sections: OpenTelemetry Python Proto, Code Generation, References

</details>

### opentelemetry-exporter-otlp-proto-common

OpenTelemetry Protobuf encoding

`pip install opentelemetry-exporter-otlp-proto-common` · installs (wheel) · licence: Apache-2.0 · rank 137 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-exporter-otlp-proto-common/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This library is provided as a convenience to encode to Protobuf. Currently used by:

* opentelemetry-exporter-otlp-proto-grpc
* opentelemetry-exporter-otlp-proto-http

Sections: OpenTelemetry Protobuf Encoding, References

</details>

### opentelemetry-exporter-otlp-proto-http

OpenTelemetry Collector Protobuf over HTTP Exporter

`pip install opentelemetry-exporter-otlp-proto-http` · installs (wheel) · licence: Apache-2.0 · rank 148 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-exporter-otlp-proto-http/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This library allows to export data to the OpenTelemetry Collector using the OpenTelemetry Protocol using Protobuf over HTTP.

Sections: OpenTelemetry Collector Protobuf over HTTP Exporter, References

</details>

### orjson

Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy

`pip install orjson` · installs (wheel) · licence: MPL-2.0 AND (Apache-2.0 OR MIT) · rank 152 · last release 2026-10-07 · [PyPI](https://pypi.org/project/orjson/) · [docs](https://github.com/ijl/orjson) · [source](https://github.com/ijl/orjson)

<details><summary>README extract</summary>

orjson is a fast, correct JSON library for Python. It
benchmarks as the fastest Python
library for JSON and is more correct than the standard json library or other
third-party libraries. It serializes
dataclass,
datetime,
numpy, and
UUID instances natively. ...

Example:
```python
>>> import orjson, datetime, numpy
>>> data = {
    "type": "job",
    "created_at": datetime.datetime(1970, 1, 1),
    "status": "🆗",
    "payload": numpy.array([[1, 2], [3, 4]]),
}
>>> orjson.dumps(data, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
...
```

Sections: orjson, Usage, Quickstart, Migrating, Serialize, default, option, OPT_APPEND_NEWLINE, OPT_INDENT_2, OPT_NAIVE_UTC, OPT_NON_STR_KEYS, OPT_OMIT_MICROSECONDS, OPT_PASSTHROUGH_DATACLASS, OPT_PASSTHROUGH_DATETIME

</details>

### opentelemetry-instrumentation

Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python

`pip install opentelemetry-instrumentation` · installs (wheel) · licence: Apache-2.0 · rank 190 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Example:
```python
from opentelemetry.instrumentation import auto_instrumentation
auto_instrumentation.initialize()
```

Sections: OpenTelemetry Instrumentation, opentelemetry-bootstrap, opentelemetry-instrument, Examples, Programmatic Auto-instrumentation, References

</details>

### opentelemetry-util-http

Web util for OpenTelemetry

`pip install opentelemetry-util-http` · installs (wheel) · licence: Apache-2.0 · rank 246 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-util-http/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library provides ASGI, WSGI middleware and other HTTP-related
functionality that is common to instrumented web frameworks (such as Django,
Starlette, FastAPI, etc.) to track requests timing through OpenTelemetry.

Example:
```python
from quart import Quart
from opentelemetry.instrumentation.asgi import OpenTelemetryMiddleware

app = Quart(name)
app.asgi_app = OpenTelemetryMiddleware(app.asgi_app)

@app.route("/")
async def hello():
    return "Hello!"

if name == "main":
    app.run(debug=True)
```

Sections: OpenTelemetry Util HTTP, Usage (Quart), Usage (Django 3.0), Usage (Raw ASGI), References

</details>

### opentelemetry-exporter-otlp-proto-grpc

OpenTelemetry Collector Protobuf over gRPC Exporter

`pip install opentelemetry-exporter-otlp-proto-grpc` · installs (wheel) · licence: Apache-2.0 · rank 256 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-exporter-otlp-proto-grpc/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This library allows to export data to the OpenTelemetry Collector using the OpenTelemetry Protocol using Protobuf over gRPC.

Sections: OpenTelemetry Collector Protobuf over gRPC Exporter, References

</details>

### opentelemetry-instrumentation-asgi

ASGI instrumentation for OpenTelemetry

`pip install opentelemetry-instrumentation-asgi` · installs (wheel) · licence: Apache-2.0 · rank 329 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-asgi/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library provides a ASGI middleware that can be used on any ASGI framework
(such as Django, Starlette, FastAPI or Quart) to track requests timing through OpenTelemetry.

Sections: OpenTelemetry ASGI Instrumentation, References

</details>

### opentelemetry-instrumentation-fastapi

OpenTelemetry FastAPI Instrumentation

`pip install opentelemetry-instrumentation-fastapi` · installs (wheel) · licence: Apache-2.0 · rank 332 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-fastapi/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library provides automatic and manual instrumentation of FastAPI web frameworks,
instrumenting http requests served by applications utilizing the framework.

auto-instrumentation using the opentelemetry-instrumentation package is also supported.

Sections: OpenTelemetry FastAPI Instrumentation, References

</details>

### opentelemetry-instrumentation-requests

OpenTelemetry requests instrumentation

`pip install opentelemetry-instrumentation-requests` · installs (wheel) · licence: Apache-2.0 · rank 357 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-requests/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing HTTP requests made by the
requests library.

Sections: OpenTelemetry Requests Instrumentation, Configuration, Exclude lists, References

</details>

### opentelemetry-exporter-otlp-common

OpenTelemetry OTLP HTTP export utilities

`pip install opentelemetry-exporter-otlp-common` · installs (wheel) · licence: Apache-2.0 · rank 380 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-exporter-otlp-common/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

OpenTelemetry OTLP export utilities.

This package is intended to be used by OpenTelemetry signal exporters (traces, metrics,
logs) that send telemetry with OTLP. Currently, all functionality in this package
is marked as internal and is not intended for use directly by application developers.

Sections: OpenTelemetry OTLP Utilities, References

</details>

### opentelemetry-exporter-otlp

OpenTelemetry Collector Exporters

`pip install opentelemetry-exporter-otlp` · installs (wheel) · licence: Apache-2.0 · rank 382 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-exporter-otlp/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This library is provided as a convenience to install all supported OpenTelemetry Collector Exporters. Currently it installs:

* opentelemetry-exporter-otlp-proto-grpc
* opentelemetry-exporter-otlp-proto-http

In the future, additional packages will be available:
* opentelemetry-exporter-otlp-json-http ...

Sections: OpenTelemetry Collector Exporters, References

</details>

### opentelemetry-instrumentation-httpx

OpenTelemetry HTTPX Instrumentation

`pip install opentelemetry-instrumentation-httpx` · installs (wheel) · licence: Apache-2.0 · rank 401 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-httpx/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing HTTP requests made by the
httpx and
httpx2 libraries.

If both libraries are installed, use `HTTPXClientInstrumentor` for
`httpx` clients and `HTTPX2ClientInstrumentor` for `httpx2` clients.
The instrumentors can be enabled independently.

Example:
```python
import httpx
import asyncio
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor

url = "
HTTPXClientInstrumentor().instrument()

with httpx.Client() as client:
    response = client.get(url)

async def get(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

asyncio.run(get(url))
```

...

</details>

### opentelemetry-exporter-http-transport

OpenTelemetry Exporters HTTP transport

`pip install opentelemetry-exporter-http-transport` · installs (wheel) · licence: Apache-2.0 · rank 412 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-exporter-http-transport/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This package provides shared HTTP transport abstractions used by OpenTelemetry exporters.

The package has no required dependencies. The `requests` and `urllib3`
transports are available as optional extras.

Sections: OpenTelemetry Exporters HTTP Transport, References

</details>

### ormsgpack

Fast, correct Python msgpack library supporting dataclasses, datetimes, and numpy

`pip install ormsgpack` · installs (wheel) · licence: Apache-2.0 OR MIT · rank 440 · last release 2026-10-15 · [PyPI](https://pypi.org/project/ormsgpack/)

<details><summary>README extract</summary>

ormsgpack is a fast MessagePack serialization library for Python
derived from orjson, with native support for various
Python types.

ormsgpack follows semantic versioning and supports CPython, PyPy and GraalPy.

Links:

- Repository
- Documentation

Example:
```python
>>> import ormsgpack, datetime, numpy
>>> event = {
...     "type": "put",
...     "time": datetime.datetime(1970, 1, 1),
...     "uid": 1,
...     "data": numpy.array([1, 2]),
... }
>>> ormsgpack.packb(event, option=ormsgpack.OPT_SERIALIZE_NUMPY)
b'\x84\xa4type\xa3put\xa4time\xb31970-01-01T00:00:00\xa3uid\x01\xa4data\x92\x01\x02'
...
```

Sections: ormsgpack, Quickstart

</details>

### opentelemetry-instrumentation-threading

Thread context propagation support for OpenTelemetry

`pip install opentelemetry-instrumentation-threading` · installs (wheel) · licence: Apache-2.0 · rank 515 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-threading/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library provides instrumentation for the `threading` module to ensure that
the OpenTelemetry context is propagated across threads. It is important to note
that this instrumentation does not produce any telemetry data on its own. It
merely ensures that the context is correctly propagated when threads are used.

Sections: OpenTelemetry threading Instrumentation, References

</details>

### opensearch-py

Python client for OpenSearch

`pip install opensearch-py` · installs (wheel) · licence: Apache Software License · rank 555 · last release 2026-04-27 · [PyPI](https://pypi.org/project/opensearch-py/) · [docs](https://opensearch.org/docs/clients/python) · [source](https://github.com/opensearch-project/opensearch-py)

<details><summary>README extract</summary>

OpenSearch Python Client

- Welcome!
- User Guide
- API Doc
- Compatibility with OpenSearch
- Project Resources
- Code of Conduct
- License
- Copyright

opensearch-py is a community-driven, open source fork
of elasticsearch-py licensed under the Apache v2.0 License.
For more information, see opensearch.org and the API Doc. ...

Sections: Welcome!, User Guide, Compatibility with OpenSearch, Project Resources, Copyright

</details>

### outcome

Capture the outcome of Python function calls.

`pip install outcome` · installs (wheel) · licence: Apache Software License; MIT License · rank 577 · last release 2023-10-26 · [PyPI](https://pypi.org/project/outcome/) · [docs](https://outcome.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Welcome to outcome!

Capture the outcome of Python function calls. Extracted from the
Trio project.

License: Your choice of MIT or Apache License 2.0

</details>

### opentelemetry-instrumentation-dbapi

OpenTelemetry Database API instrumentation

`pip install opentelemetry-instrumentation-dbapi` · installs (wheel) · licence: Apache-2.0 · rank 585 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-dbapi/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry Database API instrumentation, References

</details>

### opentelemetry-instrumentation-sqlalchemy

OpenTelemetry SQLAlchemy instrumentation

`pip install opentelemetry-instrumentation-sqlalchemy` · installs (wheel) · licence: Apache-2.0 · rank 593 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-sqlalchemy/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing requests made by the SQLAlchemy library.

Sections: OpenTelemetry SQLAlchemy Instrumentation, References

</details>

### omegaconf

A flexible configuration library

`pip install omegaconf` · installs (wheel) · licence: BSD License · rank 599 · last release 2026-10-09 · [PyPI](https://pypi.org/project/omegaconf/)

<details><summary>README extract</summary>

> [!IMPORTANT]
> OmegaConf project transition: OmegaConf moved from the `omry` GitHub account
> to `hydra-ecosystem`. The repository moved
> with its history, issues, and pull requests intact. OmegaConf remains BSD
> 3-Clause licensed. No action is required from OmegaConf users. ...

Sections: OmegaConf, Optional subprojects, Stable (2.4), Previous stable (2.3)

</details>

### opentelemetry-instrumentation-logging

OpenTelemetry Logging instrumentation

`pip install opentelemetry-instrumentation-logging` · installs (wheel) · licence: Apache-2.0 · rank 603 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-logging/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry logging integration, References

</details>

### opentelemetry-instrumentation-wsgi

WSGI Middleware for OpenTelemetry

`pip install opentelemetry-instrumentation-wsgi` · installs (wheel) · licence: Apache-2.0 · rank 647 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-wsgi/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library provides a WSGI middleware that can be used on any WSGI framework
(such as Django / Flask) to track requests timing through OpenTelemetry.

Sections: OpenTelemetry WSGI Middleware, References

</details>

### overrides

A decorator to automatically detect mismatch when overriding a method.

`pip install overrides` · installs (wheel) · licence: Apache License, Version 2.0 · rank 649 · last release 2024-01-27 · [PyPI](https://pypi.org/project/overrides/)

<details><summary>README extract</summary>

A decorator `@override` that verifies that a method that should override an inherited method actually does it.

Copies the docstring of the inherited method to the overridden method. ...

Example:
```python
from overrides import override

class SuperClass:

    def foo(self):
        """This docstring will be inherited by any method that overrides this!"""
        return 1

    def bar(self, x) -> str:
        return x

class SubClass(SuperClass):

    @override
    def foo(self):
        return 2

    @override
...
```

Sections: overrides, Motivation, Usage, Flags of control

</details>

### opentelemetry-instrumentation-psycopg2

OpenTelemetry psycopg2 instrumentation

`pip install opentelemetry-instrumentation-psycopg2` · installs (wheel) · licence: Apache-2.0 · rank 660 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-psycopg2/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry Psycopg2 Instrumentation, References

</details>

### opentelemetry-instrumentation-urllib3

OpenTelemetry urllib3 instrumentation

`pip install opentelemetry-instrumentation-urllib3` · installs (wheel) · licence: Apache-2.0 · rank 664 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-urllib3/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing HTTP requests made by the
urllib3 library.

Example:
```python
import urllib3
from opentelemetry.instrumentation.urllib3 import URLLib3Instrumentor

def strip_query_params(url: str) -> str:
    return url.split("?")[0]

URLLib3Instrumentor().instrument(
    # Remove all query params from the URL attribute on the span.
    url_filter=strip_query_params,
)

http = urllib3.PoolManager()
...
```

Sections: OpenTelemetry urllib3 Instrumentation, Usage, Configuration, Request/Response hooks, Exclude lists, References

</details>

### opentelemetry-instrumentation-django

OpenTelemetry Instrumentation for Django

`pip install opentelemetry-instrumentation-django` · installs (wheel) · licence: Apache-2.0 · rank 679 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-django/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing requests for Django applications.

Sections: OpenTelemetry Django Tracing, References

</details>

### opentelemetry-instrumentation-flask

Flask instrumentation for OpenTelemetry

`pip install opentelemetry-instrumentation-flask` · installs (wheel) · licence: Apache-2.0 · rank 711 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-flask/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library builds on the OpenTelemetry WSGI middleware to track web requests
in Flask applications.

Sections: OpenTelemetry Flask Tracing, References

</details>

### ordered-set

An OrderedSet is a custom MutableSet that remembers its order, so that every

`pip install ordered-set` · installs (wheel) · licence: MIT License · rank 718 · last release 2022-01-26 · [PyPI](https://pypi.org/project/ordered-set/)

<details><summary>README extract</summary>

An OrderedSet is a mutable data structure that is a hybrid of a list and a set.
It remembers the order of its entries, and every entry has an index number that
can be looked up.

Sections: Usage examples, OrderedSet in data science applications, Comparisons

</details>

### opentelemetry-instrumentation-urllib

OpenTelemetry urllib instrumentation

`pip install opentelemetry-instrumentation-urllib` · installs (wheel) · licence: Apache-2.0 · rank 723 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-urllib/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing HTTP requests made by the
urllib library.

Example:
```python
from opentelemetry.instrumentation.urllib import URLLibInstrumentor

# `request_obj` is an instance of urllib.request.Request
def request_hook(span, request_obj):
    pass

# `request_obj` is an instance of urllib.request.Request
# `response` is an instance of http.client.HTTPResponse
def response_hook(span, request_obj, response):
    pass

...
```

Sections: OpenTelemetry urllib Instrumentation, Configuration, Request/Response hooks, Exclude lists, References

</details>

### opentelemetry-instrumentation-aiohttp-client

OpenTelemetry aiohttp client instrumentation

`pip install opentelemetry-instrumentation-aiohttp-client` · installs (wheel) · licence: Apache-2.0 · rank 736 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-aiohttp-client/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing HTTP requests made by the
aiohttp client library.

Sections: OpenTelemetry aiohttp client Integration, References

</details>

### opentelemetry-instrumentation-redis

OpenTelemetry Redis instrumentation

`pip install opentelemetry-instrumentation-redis` · installs (wheel) · licence: Apache-2.0 · rank 746 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-redis/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing requests made by the Redis library.

Sections: OpenTelemetry Redis Instrumentation, References

</details>

### opentelemetry-distro

OpenTelemetry Python Distro

`pip install opentelemetry-distro` · installs (wheel) · licence: Apache-2.0 · rank 879 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-distro/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

### opentelemetry-exporter-prometheus

Prometheus Metric Exporter for OpenTelemetry

`pip install opentelemetry-exporter-prometheus` · installs (wheel) · licence: Apache-2.0 · rank 918 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-exporter-prometheus/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This library allows to export metrics data to Prometheus.

Sections: OpenTelemetry Prometheus Exporter, Limitations, References

</details>

### opentelemetry-instrumentation-grpc

OpenTelemetry gRPC instrumentation

`pip install opentelemetry-instrumentation-grpc` · installs (wheel) · licence: Apache-2.0 · rank 951 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-grpc/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Client and server interceptors for gRPC Python.

Sections: OpenTelemetry gRPC Integration, References

</details>

### onnx

Open Neural Network Exchange

`pip install onnx` · installs (wheel) · licence: Apache-2.0 · rank 956 · last release 2026-10-06 · [PyPI](https://pypi.org/project/onnx/) · [source](https://github.com/onnx/onnx)

<details><summary>README extract</summary>

Open Neural Network Exchange (ONNX) is an open ecosystem that empowers AI developers
to choose the right tools as their project evolves. ONNX provides an open source format for AI models, both deep learning and traditional ML. It defines an extensible computation graph model, as well as definitions of built-in operators and standard
data types. ...

Features:
A fixed build timestamp removes one known source of nondeterminism. When
independent builds use the same controlled inputs, their artifacts can be
compared byte for byte, with cryptographic digests providing a practical
shortcut. ...

Sections: Use ONNX, Learn about the ONNX spec, Programming utilities for working with ONNX Graphs, Discuss, Follow Us, Roadmap, Python ABI3 Compatibility, Why this matters, Trademark

</details>

### opentelemetry-resourcedetector-gcp

Google Cloud Resource Detector for OpenTelemetry

`pip install opentelemetry-resourcedetector-gcp` · installs (wheel) · licence: Apache-2.0 · rank 979 · last release 2026-07-24 · [PyPI](https://pypi.org/project/opentelemetry-resourcedetector-gcp/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library provides support for detecting GCP resources like GCE, GKE, etc.

Sections: OpenTelemetry Google Cloud Resource Detector, Usage, References

</details>

### opentelemetry-instrumentation-botocore

OpenTelemetry Botocore instrumentation

`pip install opentelemetry-instrumentation-botocore` · installs (wheel) · licence: Apache-2.0 · rank 991 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-botocore/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

### oss2

Aliyun OSS (Object Storage Service) SDK

`pip install oss2` · installs from source (sdist only) · licence: MIT License · rank 1011 · last release 2024-10-25 · [PyPI](https://pypi.org/project/oss2/)

<details><summary>README extract</summary>

`README of Chinese <

Features:
Alibaba Cloud Object Storage Python SDK 2.x. This version is not compatible with the previous version (Version 0.x). The package name is `oss2` to avoid conflict with previous versions. ...

Example:
```python
# -*- coding: utf-8 -*-

import oss2

endpoint = ' # Suppose that your bucket is in the Hangzhou region.

auth = oss2.Auth('<Your AccessKeyID>', '<Your AccessKeySecret>')
bucket = oss2.Bucket(auth, endpoint, '<your bucket name>')

# The object key in the bucket is story.txt
key = 'story.txt'

# Upload
...
```

Sections: Alibaba Cloud OSS SDK for Python, Overview, Running environment, Getting started, Handling errors, Setup Logging, More resources, Contacting us

</details>

### opentelemetry-semantic-conventions-ai

OpenTelemetry Semantic Conventions Extension for Large Language Models

`pip install opentelemetry-semantic-conventions-ai` · installs (wheel) · licence: Apache-2.0 · rank 1029 · last release 2026-03-26 · [PyPI](https://pypi.org/project/opentelemetry-semantic-conventions-ai/)

<details><summary>README extract</summary>

This is an extension of the standard OpenTelemetry Semantic Conventions for gen AI applications. It defines additional attributes for spans that are useful for debugging and monitoring prompts, completions, token usage, etc.

</details>

### opentelemetry-resource-detector-azure

Azure Resource Detector for OpenTelemetry

`pip install opentelemetry-resource-detector-azure` · installs (wheel) · licence: Apache-2.0 · rank 1041 · last release 2026-09-29 · [PyPI](https://pypi.org/project/opentelemetry-resource-detector-azure/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library contains OpenTelemetry Resource Detectors for the following Azure resources:
 * Azure Kubernetes Service
 * Azure App Service
 * Azure Virtual Machines
 * Azure Functions (Experimental)

Sections: OpenTelemetry Resource detectors for Azure, Mappings, References

</details>

### opentelemetry-propagator-aws-xray

AWS X-Ray Propagator for OpenTelemetry

`pip install opentelemetry-propagator-aws-xray` · installs (wheel) · licence: Apache Software License · rank 1044 · last release 2024-08-05 · [PyPI](https://pypi.org/project/opentelemetry-propagator-aws-xray/)

<details><summary>README extract</summary>

This library provides the propagator necessary to inject or extract a tracing
context across AWS services.

Example:
```python
from opentelemetry.propagate import set_global_textmap
from opentelemetry.propagators.aws import AwsXRayPropagator

set_global_textmap(AwsXRayPropagator())
```

Sections: OpenTelemetry Propagator for AWS X-Ray Service, Usage (AWS X-Ray Propagator), References

</details>

### opencensus-context

OpenCensus Runtime Context

`pip install opencensus-context` · installs (wheel) · licence: Apache Software License · rank 1046 · last release 2022-08-03 · [PyPI](https://pypi.org/project/opencensus-context/)

<details><summary>README extract</summary>

The OpenCensus Runtime Context provides in-process context propagation.
By default, `thread local storage` is used for Python 2.7, 3.4 and 3.5;
`contextvars` is used for Python >= 3.6, which provides `asyncio` support.

Example:
```python
from threading import Thread
from opencensus.common.runtime_context import RuntimeContext

def work(name):
    # here you will get the context from the parent thread
    print(RuntimeContext)

thread = Thread(
    # propagate context explicitly
    target=RuntimeContext.with_current_context(work),
    args=('foobar',),
)
thread.start()
...
```

Sections: OpenCensus Runtime Context, Usage, Explicit Thread Creation, Thread Pool, References

</details>

### opencensus

A stats collection and distributed tracing framework

`pip install opencensus` · installs (wheel) · licence: Apache Software License · rank 1049 · last release 2024-01-03 · [PyPI](https://pypi.org/project/opencensus/)

<details><summary>README extract</summary>

OpenCensus for Python. OpenCensus provides a framework to measure a
server's resource usage and collect performance stats. This repository
contains Python related utilities and supporting software needed by
OpenCensus.

- API Documentation

Example:
```python
from opencensus.trace.tracer import Tracer
from opencensus.trace.samplers import AlwaysOnSampler

# Initialize a tracer, by default using the `PrintExporter`
tracer = Tracer(sampler=AlwaysOnSampler())

# Example for creating nested spans
with tracer.span(name='span1'):
    do_something_to_trace()
    with tracer.span(name='span1_child1'):
...
```

Sections: Tracing, Usage, Customization, Extensions, Integration, Log Exporter, Metrics Exporter, Stats Exporter, Trace Exporter, Versioning

</details>

### ollama

The official Python client for Ollama.

`pip install ollama` · installs (wheel) · licence: MIT · rank 1073 · last release 2026-09-29 · [PyPI](https://pypi.org/project/ollama/) · [source](https://github.com/ollama/ollama-python)

<details><summary>README extract</summary>

The Ollama Python library provides the easiest way to integrate Python 3.8+ projects with Ollama.

- Ollama should be installed and running
- Pull a model to use with the library: `ollama pull <model>` e.g. `ollama pull gemma4`
 - See Ollama.com for more information on the models available.

Example:
```python
from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(
  model='gemma4',
  messages=[
    {
      'role': 'user',
      'content': 'Why is the sky blue?',
    },
  ],
)
print(response'message')
# or access fields directly from the response object
print(response.message.content)
```

...

</details>

### opentelemetry-instrumentation-asyncpg

OpenTelemetry instrumentation for AsyncPG

`pip install opentelemetry-instrumentation-asyncpg` · installs (wheel) · licence: Apache-2.0 · rank 1086 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-asyncpg/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing PostgreSQL queries made by the
asyncpg library.

Sections: OpenTelemetry asyncpg Instrumentation, References

</details>

### opensearch-protobufs

Protocol Buffer definitions for OpenSearch gRPC APIs

`pip install opensearch-protobufs` · installs (wheel) · licence: Apache Software License · rank 1096 · last release 2026-08-14 · [PyPI](https://pypi.org/project/opensearch-protobufs/) · [docs](https://github.com/opensearch-project/opensearch-protobufs/blob/main/README.md) · [source](https://github.com/opensearch-project/opensearch-protobufs)

<details><summary>README extract</summary>

This repository stores the Protobufs and generated code used for client <> server GRPC APIs.

The opensearch-api-specification repo will continue to be the source of truth, and these protobufs will mostly be a downstream consumer of the spec. ...

Example:
```python
from opensearch.protobufs.schemas import SearchRequest, BulkRequest, IndexDocumentRequest
from opensearch.protobufs.services import SearchServiceStub

# Use generated message types
request = SearchRequest()
request.query = "elasticsearch"
request.size = 10

# Use generated gRPC clients
client = SearchServiceStub(channel)
...
```

Sections: opensearch-protobufs, Using Raw Proto Files, Generated Code Usage, Go, Java, Python, Generated Code Locations, Intended usage of the repo, CI/CD

</details>

### opentelemetry-instrumentation-celery

OpenTelemetry Celery Instrumentation

`pip install opentelemetry-instrumentation-celery` · installs (wheel) · licence: Apache-2.0 · rank 1170 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-celery/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Instrumentation for Celery.

Sections: OpenTelemetry Celery Instrumentation, References

</details>

### opentelemetry-instrumentation-system-metrics

OpenTelemetry System Metrics Instrumentation

`pip install opentelemetry-instrumentation-system-metrics` · installs (wheel) · licence: Apache-2.0 · rank 1177 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-system-metrics/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Instrumentation to collect system performance metrics.

Sections: OpenTelemetry System Metrics Instrumentation, References

</details>

### openinference-semantic-conventions

OpenInference Semantic Conventions

`pip install openinference-semantic-conventions` · installs (wheel) · licence: Apache-2.0 · rank 1179 · last release 2026-10-29 · [PyPI](https://pypi.org/project/openinference-semantic-conventions/)

<details><summary>README extract</summary>

This library contains code for the OpenInference Semantic Conventions defined by the OpenInference specification.

</details>

### openinference-instrumentation

OpenInference instrumentation utilities

`pip install openinference-instrumentation` · installs (wheel) · licence: Apache-2.0 · rank 1212 · last release 2026-10-31 · [PyPI](https://pypi.org/project/openinference-instrumentation/)

<details><summary>README extract</summary>

Utility functions for OpenInference instrumentation.

Example:
```python
from openinference.instrumentation import (
    Annotation,
    get_annotation_attributes,
    get_evaluation_attributes,
)

span_annotations = get_annotation_attributes(
    annotations=[
        Annotation(
            name="hallucination",
            label="factual",
...
```

Sections: OpenInference Instrumentation, Annotation and Evaluation Attributes, Customizing Spans, Suppressing Tracing, Tracing Configuration

</details>

### opentelemetry-instrumentation-psycopg

OpenTelemetry psycopg instrumentation

`pip install opentelemetry-instrumentation-psycopg` · installs (wheel) · licence: Apache-2.0 · rank 1326 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-psycopg/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry Psycopg Instrumentation, References

</details>

### opentelemetry-exporter-gcp-trace

Google Cloud Trace exporter for OpenTelemetry

`pip install opentelemetry-exporter-gcp-trace` · installs (wheel) · licence: Apache Software License · rank 1397 · last release 2026-08-19 · [PyPI](https://pypi.org/project/opentelemetry-exporter-gcp-trace/)

<details><summary>README extract</summary>

This library provides support for exporting traces to Google Cloud Trace.

To get started with instrumentation in Google Cloud, see Generate traces and metrics with
Python.

To learn more about instrumentation and observability, including opinionated recommendations
for Google Cloud Observability, visit Instrumentation and observability. ...

Example:
```python
from opentelemetry import trace
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    SimpleSpanProcessor,
)

trace.set_tracer_provider(TracerProvider())

cloud_trace_exporter = CloudTraceSpanExporter(
...
```

Sections: OpenTelemetry Google Cloud Integration, Usage, References

</details>

### openai-harmony

OpenAI's response format for its open-weight model series gpt-oss

`pip install openai-harmony` · installs (wheel) · licence: not stated · rank 1437 · last release 2025-11-05 · [PyPI](https://pypi.org/project/openai-harmony/)

<details><summary>README extract</summary>

OpenAI's response format for its open-weight model series gpt-oss

Try gpt-oss | Learn more | Model card

The gpt-oss models were trained on the harmony response format for defining conversation structures, generating reasoning output and structuring function calls. ...

Example:
```python
from openai_harmony import (
    load_harmony_encoding,
    HarmonyEncodingName,
    Role,
    Message,
    Conversation,
    DeveloperContent,
    SystemContent,
)
enc = load_harmony_encoding(HarmonyEncodingName.HARMONY_GPT_OSS)
convo = Conversation.from_messages([
    Message.from_role_and_content(
        Role.SYSTEM,
...
```

...

</details>

### opentelemetry-sdk-extension-aws

AWS SDK extension for OpenTelemetry

`pip install opentelemetry-sdk-extension-aws` · installs (wheel) · licence: Apache Software License · rank 1598 · last release 2024-12-24 · [PyPI](https://pypi.org/project/opentelemetry-sdk-extension-aws/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library provides components necessary to configure the OpenTelemetry SDK
for tracing with AWS X-Ray.

Example:
```python
import opentelemetry.trace as trace
from opentelemetry.sdk.extension.aws.trace import AwsXRayIdGenerator
from opentelemetry.sdk.trace import TracerProvider

trace.set_tracer_provider(
    TracerProvider(id_generator=AwsXRayIdGenerator())
)
```

Sections: OpenTelemetry SDK Extension for AWS X-Ray Compatibility, Usage (AWS X-Ray IDs Generator), Usage (AWS Resource Detectors), References

</details>

### openai-whisper

Robust Speech Recognition via Large-Scale Weak Supervision

`pip install openai-whisper` · installs from source (sdist only) · licence: MIT · rank 1606 · last release 2025-06-26 · [PyPI](https://pypi.org/project/openai-whisper/)

<details><summary>README extract</summary>

[[Blog]](
[[Paper]](
[[Model card]](
[[Colab example]](

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification. ...

Example:
```python
import whisper

model = whisper.load_model("turbo")
result = model.transcribe("audio.mp3")
print(result["text"])
```

Sections: Whisper, Approach, Setup, Available models and languages, Command-line usage, Python usage, More examples

</details>

### osqp

OSQP: The Operator Splitting QP Solver

`pip install osqp` · installs (wheel) · licence: Apache-2.0 · rank 1640 · last release 2026-06-12 · [PyPI](https://pypi.org/project/osqp/)

<details><summary>README extract</summary>

Python wrapper for OSQP: The Operator Splitting QP solver.

The OSQP (Operator Splitting Quadratic Program) solver is a numerical
optimization package for solving problems in the form

$$\begin{array}{ll}
 \mbox{minimize} & \frac{1}{2} x^T P x + q^T x \\
 \mbox{subject to} & l \le A x \le u
\end{array} ...

Sections: OSQP Python, Documentation

</details>

### opentelemetry-instrumentation-kafka-python

OpenTelemetry Kafka-Python instrumentation

`pip install opentelemetry-instrumentation-kafka-python` · installs (wheel) · licence: Apache-2.0 · rank 1649 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-kafka-python/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry kafka-python integration, References

</details>

### opentelemetry-instrumentation-asyncio

OpenTelemetry instrumentation for asyncio

`pip install opentelemetry-instrumentation-asyncio` · installs (wheel) · licence: Apache-2.0 · rank 1668 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-asyncio/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

AsyncioInstrumentor: Tracing Requests Made by the Asyncio Library

The opentelemetry-instrumentation-asyncio package allows tracing asyncio applications.
It also includes metrics for duration and counts of coroutines and futures. Metrics are generated even if coroutines are not traced.

Example:
```python
# export OTEL_PYTHON_ASYNCIO_COROUTINE_NAMES_TO_TRACE=sleep

import asyncio
from opentelemetry.instrumentation.asyncio import AsyncioInstrumentor

AsyncioInstrumentor().instrument()

async def main():
    await asyncio.create_task(asyncio.sleep(0.1))

asyncio.run(main())
```

Sections: OpenTelemetry asyncio Instrumentation, Set the names of coroutines you want to trace., Run instrumented application, 1. coroutine, 2. future, 3. to_thread, asyncio metric types, API, References

</details>

### opentelemetry-instrumentation-starlette

OpenTelemetry Starlette Instrumentation

`pip install opentelemetry-instrumentation-starlette` · installs (wheel) · licence: Apache-2.0 · rank 1677 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-starlette/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library provides automatic and manual instrumentation of Starlette web frameworks,
instrumenting http requests served by applications utilizing the framework.

auto-instrumentation using the opentelemetry-instrumentation package is also supported.

Sections: OpenTelemetry Starlette Instrumentation, References

</details>

### opentelemetry-instrumentation-pymongo

OpenTelemetry pymongo instrumentation

`pip install opentelemetry-instrumentation-pymongo` · installs (wheel) · licence: Apache-2.0 · rank 1721 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-pymongo/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry pymongo Instrumentation, References

</details>

### oldest-supported-numpy

Meta-package that provides the oldest NumPy that supports a given Python version and platform. If wheels for the platform became available on PyPI only for a more recent NumPy version, then that NumPy version is specified.

`pip install oldest-supported-numpy` · installs (wheel) · licence: BSD · rank 1727 · last release 2023-12-21 · [PyPI](https://pypi.org/project/oldest-supported-numpy/)

<details><summary>README extract</summary>

This is a meta-package which can be used in `pyproject.toml` files
to automatically provide as a build-time dependency the oldest version
of NumPy that supports the given Python version and platform. In case
of platforms for which NumPy has prebuilt wheels, the provided version
also has a prebuilt NumPy wheel. ...

Features:
The NumPy version pinnings are defined inside the `setup.cfg` file as
`install_requires` dependencies, rather than as build-time dependencies
inside `pyproject.toml`. ...

Sections: About, Q&A, What about having a catchier name for this package?

</details>

### opencensus-ext-azure

OpenCensus Azure Monitor Exporter

`pip install opencensus-ext-azure` · installs (wheel) · licence: Apache Software License · rank 1773 · last release 2025-06-03 · [PyPI](https://pypi.org/project/opencensus-ext-azure/)

<details><summary>README extract</summary>

OpenCensus Azure Monitor exporters are on the path to deprecation. They will be officially unsupported by September 2024. Please migrate to the Azure Monitor OpenTelemetry Distro for the recommended "one-stop-shop" solution or the Azure Monitor OpenTelemetry exporters for the more hand-on, configurable solution based on OpenTelemetry. ...

Example:
```python
import logging

from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(name)
logger.addHandler(AzureLogHandler(connection_string='InstrumentationKey=<your-instrumentation_key-here>'))
logger.warning('Hello, World!')
```

...

</details>

### opentelemetry-instrumentation-sqlite3

OpenTelemetry SQLite3 instrumentation

`pip install opentelemetry-instrumentation-sqlite3` · installs (wheel) · licence: Apache-2.0 · rank 1775 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-sqlite3/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry SQLite3 Instrumentation, References

</details>

### oci

Oracle Cloud Infrastructure Python SDK

`pip install oci` · installs (wheel) · licence: Apache Software License; Universal Permissive License (UPL) · rank 1807 · last release 2026-11-03 · [PyPI](https://pypi.org/project/oci/)

<details><summary>README extract</summary>

This is the Python SDK for Oracle Cloud Infrastructure. Supported Python versions are mentioned here.


The project is open source and maintained by Oracle Corp. The home page for the project is here.


Example:
```python
>>> import oci
# Set up config
>>> config = oci.config.from_file(
...     "~/.oci/config",
...     "DEFAULT")
# Create a service client
>>> identity = oci.identity.IdentityClient(config)
# Get the current user
>>> user = identity.get_user(config["user"]).data
>>> print(user)
{
  "compartment_id": "ocid1.tenancy.oc1...",
...
```

Sections: Oracle Cloud Infrastructure Python SDK, About, Examples, Documentation, Help, Changes, Known Issues, Survey

</details>

### opentelemetry-processor-baggage

OpenTelemetry Baggage Span Processor

`pip install opentelemetry-processor-baggage` · installs (wheel) · licence: Apache-2.0 · rank 1878 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-processor-baggage/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

The BaggageSpanProcessor reads entries stored in Baggage
from the parent context and adds the baggage entries' keys and
values to the span as attributes on span start.

Example:
```python
from opentelemetry.processor.baggage import BaggageSpanProcessor, ALLOW_ALL_BAGGAGE_KEYS

tracer_provider = TracerProvider()
tracer_provider.add_span_processor(BaggageSpanProcessor(ALLOW_ALL_BAGGAGE_KEYS))
```

Sections: OpenTelemetry Baggage Span Processor, Usage, BaggageLogProcessor, References

</details>

### opentelemetry-exporter-gcp-monitoring

Google Cloud Monitoring exporter for OpenTelemetry

`pip install opentelemetry-exporter-gcp-monitoring` · installs (wheel) · licence: Apache Software License · rank 1894 · last release 2026-08-19 · [PyPI](https://pypi.org/project/opentelemetry-exporter-gcp-monitoring/)

<details><summary>README extract</summary>

This library provides support for exporting metrics to Google Cloud
Monitoring.

To get started with instrumentation in Google Cloud, see Generate traces and metrics with
Python.

To learn more about instrumentation and observability, including opinionated recommendations
for Google Cloud Observability, visit Instrumentation and observability. ...

Example:
```python
import time

from opentelemetry import metrics
from opentelemetry.exporter.cloud_monitoring import (
    CloudMonitoringMetricsExporter,
)
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource

metrics.set_meter_provider(
...
```

Sections: OpenTelemetry Google Cloud Monitoring Exporter, Usage, References

</details>

### opentelemetry-instrumentation-aiokafka

OpenTelemetry aiokafka instrumentation

`pip install opentelemetry-instrumentation-aiokafka` · installs (wheel) · licence: Apache-2.0 · rank 1940 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-aiokafka/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry aiokafka instrumentation, References

</details>

### opentelemetry-util-genai

OpenTelemetry GenAI Utils

`pip install opentelemetry-util-genai` · installs (wheel) · licence: Apache-2.0 · rank 1953 · last release 2026-10-23 · [PyPI](https://pypi.org/project/opentelemetry-util-genai/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

The GenAI Utils package provides boilerplate and helpers to standardize instrumentation for Generative AI.
It offers APIs to minimize the work needed to instrument GenAI libraries,
while providing standardization for generating spans, metrics, and events.

- `TelemetryHandler` -- manages LLM invocation lifecycles (spans, metrics, events) ...

Example:
```python
from opentelemetry import context
from opentelemetry.util.genai.invocation import (
    CLIENT_INFERENCE_CONTEXT_KEY,
    InferenceData,
)

data = InferenceData()
token = context.attach(context.set_value(CLIENT_INFERENCE_CONTEXT_KEY, data))
try:
    # Inner instrumented call detects data on context, suppresses its span,
...
```

...

</details>

### opentelemetry-instrumentation-jinja2

OpenTelemetry jinja2 instrumentation

`pip install opentelemetry-instrumentation-jinja2` · installs (wheel) · licence: Apache-2.0 · rank 1984 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-jinja2/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry jinja2 integration, References

</details>

### opentelemetry-instrumentation-boto3sqs

Boto3 SQS service tracing for OpenTelemetry

`pip install opentelemetry-instrumentation-boto3sqs` · installs (wheel) · licence: Apache-2.0 · rank 1993 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-boto3sqs/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing requests made by the Boto3 library to the SQS service.

Sections: OpenTelemetry Boto3 SQS Instrumentation, References

</details>

### openhands-sdk

OpenHands SDK - Core functionality for building AI agents

`pip install openhands-sdk` · installs (wheel) · licence: not stated · rank 1995 · last release 2026-11-06 · [PyPI](https://pypi.org/project/openhands-sdk/) · [docs](https://docs.openhands.dev/sdk) · [source](https://github.com/OpenHands/software-agent-sdk)

### opentelemetry-exporter-gcp-logging

Google Cloud Logging exporter for OpenTelemetry

`pip install opentelemetry-exporter-gcp-logging` · installs (wheel) · licence: Apache Software License · rank 1996 · last release 2026-08-19 · [PyPI](https://pypi.org/project/opentelemetry-exporter-gcp-logging/)

<details><summary>README extract</summary>

This library provides support for exporting logs to Google Cloud
Logging.

To get started with instrumentation in Google Cloud, see Generate traces and metrics with
Python.

To learn more about instrumentation and observability, including opinionated recommendations
for Google Cloud Observability, visit Instrumentation and observability. ...

Example:
```python
import logging
from opentelemetry.exporter.cloud_logging import (
    CloudLoggingExporter,
)
from opentelemetry.sdk.resources import Resource
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor

...
```

Sections: OpenTelemetry Google Cloud Logging Exporter, Usage, References

</details>

### openhands-tools

OpenHands Tools - Runtime tools for AI agents

`pip install openhands-tools` · installs (wheel) · licence: not stated · rank 2021 · last release 2026-11-06 · [PyPI](https://pypi.org/project/openhands-tools/) · [docs](https://docs.openhands.dev/sdk) · [source](https://github.com/OpenHands/software-agent-sdk)

### opentelemetry-instrumentation-langchain

OpenTelemetry Langchain instrumentation

`pip install opentelemetry-instrumentation-langchain` · installs (wheel) · licence: Apache-2.0 · rank 2066 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-langchain/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-langchain)

<details><summary>README extract</summary>

This library allows tracing complete LLM applications built with Langchain.

Example:
```python
from opentelemetry.instrumentation.langchain import LangchainInstrumentor

LangchainInstrumentor().instrument()
```

Sections: OpenTelemetry Langchain Instrumentation, Example usage, Privacy

</details>

### openlineage-python

OpenLineage Python Client

`pip install openlineage-python` · installs (wheel) · licence: Apache-2.0 · rank 2077 · last release 2026-10-29 · [PyPI](https://pypi.org/project/openlineage-python/)

<details><summary>README extract</summary>

Python client for OpenLineage.

Refer to the documentation for details.

</details>

### opentelemetry-instrumentation-tortoiseorm

OpenTelemetry Instrumentation for Tortoise ORM

`pip install opentelemetry-instrumentation-tortoiseorm` · installs (wheel) · licence: Apache-2.0 · rank 2092 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-tortoiseorm/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing queries made by tortoise ORM backends, mysql, postgres and sqlite.

Sections: OpenTelemetry Tortoise ORM Instrumentation, References

</details>

### onepassword-sdk

The 1Password Python SDK offers programmatic read access to your secrets in 1Password in an interface native to Python.

`pip install onepassword-sdk` · installs from source (sdist only) · licence: MIT License · rank 2099 · last release 2026-10-22 · [PyPI](https://pypi.org/project/onepassword-sdk/)

<details><summary>README extract</summary>

Documentation | Examples

The 1Password Python SDK is compatible with:

- `python` 3.9 or later
- `libssl` 3
- `glibc` 2.32 or later

If you're running a Linux distribution that still uses `libssl` version 1.1.1, such as Debian 11 or Ubuntu 20.04, you'll need to update to a later version of Linux or install the required dependencies.

Example:
```python
import asyncio
import os
from onepassword.client import Client, DesktopAuth

async def main():
    # Connects to 1Password. Fill in your own integration name and version.
    client = await Client.authenticate(
    auth=DesktopAuth(
        # TODO: Set to your 1Password account name.
        account_name="your-account-name"
    ),
...
```

...

</details>

### opentelemetry-propagator-b3

OpenTelemetry B3 Propagator

`pip install opentelemetry-propagator-b3` · installs (wheel) · licence: Apache-2.0 · rank 2101 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-propagator-b3/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This library provides a propagator for the B3 format

Sections: OpenTelemetry B3 Propagator, References

</details>

### opentelemetry-instrumentation-tornado

Tornado instrumentation for OpenTelemetry

`pip install opentelemetry-instrumentation-tornado` · installs (wheel) · licence: Apache-2.0 · rank 2116 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-tornado/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library builds on the OpenTelemetry WSGI middleware to track web requests
in Tornado applications.

Sections: OpenTelemetry Tornado Instrumentation, References

</details>

### ossdata

Scalable SWE datasets

`pip install ossdata` · installs (wheel) · licence: MIT License · rank 2122 · last release 2026-04-20 · [PyPI](https://pypi.org/project/ossdata/)

### opentelemetry-instrumentation-aws-lambda

OpenTelemetry AWS Lambda instrumentation

`pip install opentelemetry-instrumentation-aws-lambda` · installs (wheel) · licence: Apache-2.0 · rank 2131 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-aws-lambda/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library provides an Instrumentor used to trace requests made by the Lambda
functions on the AWS Lambda service.

It also provides scripts used by AWS Lambda Layers to automatically initialize
the OpenTelemetry SDK. Learn more on the AWS Distro for OpenTelemetry (ADOT)
documentation for the Python Lambda Layer.

Sections: OpenTelemetry AWS Lambda Tracing, References

</details>

### openfeature-sdk

Standardizing Feature Flagging for Everyone

`pip install openfeature-sdk` · installs (wheel) · licence: Apache-2.0 · rank 2145 · last release 2026-06-01 · [PyPI](https://pypi.org/project/openfeature-sdk/)

<details><summary>README extract</summary>

=3.10-blue.svg" />

OpenFeature is an open specification that provides a vendor-agnostic, community-driven API for feature flagging that works with your favorite feature flag management tool.

Example:
```python
from openfeature import api
from openfeature.provider.in_memory_provider import InMemoryFlag, InMemoryProvider

# flags defined in memory
my_flags = {
  "v2_enabled": InMemoryFlag("on", {"on": True, "off": False})
}

# configure a provider
api.set_provider(InMemoryProvider(my_flags))

# create a client
client = api.get_client()

...
```

Sections: OpenFeature Python SDK, 🚀 Quick start, Requirements, requirements.txt, Usage, 🌟 Features, Providers, Targeting, Hooks, Tracking, Logging, Logging Hook, Domains, Eventing

</details>

### opentelemetry-instrumentation-pika

OpenTelemetry pika instrumentation

`pip install opentelemetry-instrumentation-pika` · installs (wheel) · licence: Apache-2.0 · rank 2254 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-pika/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing requests made by the pika library.

Sections: OpenTelemetry pika Instrumentation, References

</details>

### opentelemetry-instrumentation-pymysql

OpenTelemetry PyMySQL instrumentation

`pip install opentelemetry-instrumentation-pymysql` · installs (wheel) · licence: Apache-2.0 · rank 2263 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-pymysql/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry PyMySQL Instrumentation, References

</details>

### opentelemetry-instrumentation-falcon

Falcon instrumentation for OpenTelemetry

`pip install opentelemetry-instrumentation-falcon` · installs (wheel) · licence: Apache-2.0 · rank 2265 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-falcon/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library builds on the OpenTelemetry WSGI middleware to track web requests
in Falcon applications.

Example:
```python
import falcon
from opentelemetry.instrumentation.falcon import FalconInstrumentor

FalconInstrumentor().instrument()

app = falcon.App()

class HelloWorldResource(object):
    def on_get(self, req, resp):
        resp.text = 'Hello World'

app.add_route('/hello', HelloWorldResource())
```

Sections: OpenTelemetry Falcon Tracing, Configuration, Exclude lists, Request attributes, Usage, Request/Response hooks, References

</details>

### opentelemetry-instrumentation-aio-pika

OpenTelemetry Aio-pika instrumentation

`pip install opentelemetry-instrumentation-aio-pika` · installs (wheel) · licence: Apache-2.0 · rank 2266 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-aio-pika/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing requests made by the Aio-pika library.

Sections: OpenTelemetry Aio-pika Instrumentation, References

</details>

### opentelemetry-instrumentation-confluent-kafka

OpenTelemetry Confluent Kafka instrumentation

`pip install opentelemetry-instrumentation-confluent-kafka` · installs (wheel) · licence: Apache-2.0 · rank 2268 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-confluent-kafka/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing requests made by the confluent-kafka library.

Sections: OpenTelemetry confluent-kafka Instrumentation, References

</details>

### opentelemetry-instrumentation-pyramid

OpenTelemetry Pyramid instrumentation

`pip install opentelemetry-instrumentation-pyramid` · installs (wheel) · licence: Apache-2.0 · rank 2280 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-pyramid/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry Pyramid Instrumentation, References

</details>

### opentelemetry-instrumentation-openai

OpenTelemetry OpenAI instrumentation

`pip install opentelemetry-instrumentation-openai` · installs (wheel) · licence: Apache-2.0 · rank 2281 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-openai/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-openai)

<details><summary>README extract</summary>

This library allows tracing OpenAI prompts and completions sent with the official OpenAI library.

Example:
```python
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

OpenAIInstrumentor().instrument()
```

Sections: OpenTelemetry OpenAI Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-anthropic

OpenTelemetry Anthropic instrumentation

`pip install opentelemetry-instrumentation-anthropic` · installs (wheel) · licence: Apache-2.0 · rank 2288 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-anthropic/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-anthropic)

<details><summary>README extract</summary>

This library allows tracing Anthropic prompts and completions sent with the official Anthropic library.

Example:
```python
from opentelemetry.instrumentation.anthropic import AnthropicInstrumentor

AnthropicInstrumentor().instrument()
```

Sections: OpenTelemetry Anthropic Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-mysqlclient

OpenTelemetry mysqlclient instrumentation

`pip install opentelemetry-instrumentation-mysqlclient` · installs (wheel) · licence: Apache-2.0 · rank 2293 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-mysqlclient/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry mysqlclient Instrumentation, References

</details>

### openinference-instrumentation-langchain

OpenInference LangChain Instrumentation

`pip install openinference-instrumentation-langchain` · installs (wheel) · licence: Apache-2.0 · rank 2299 · last release 2026-11-04 · [PyPI](https://pypi.org/project/openinference-instrumentation-langchain/)

<details><summary>README extract</summary>

Python auto-instrumentation library for LangChain.

These traces are fully OpenTelemetry compatible and can be sent to an OpenTelemetry collector for viewing, such as Arize Phoenix or Arize AX.

This instrumentation works with:
- LangChain 1.x (`langchain>=1.0.0`): Modern agent framework built on LangGraph ...

Example:
```python
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from openinference.instrumentation.langchain import LangChainInstrumentor
from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
...
```

...

</details>

### opentelemetry-instrumentation-mysql

OpenTelemetry MySQL instrumentation

`pip install opentelemetry-instrumentation-mysql` · installs (wheel) · licence: Apache-2.0 · rank 2373 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-mysql/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Instrumentation with MySQL that supports the mysql-connector library and is
specified to trace_integration using 'MySQL'.

Sections: OpenTelemetry MySQL Instrumentation, References

</details>

### onnx-ir

Efficient in-memory representation for ONNX

`pip install onnx-ir` · installs (wheel) · licence: Apache-2.0 · rank 2395 · last release 2026-10-20 · [PyPI](https://pypi.org/project/onnx-ir/) · [source](https://github.com/onnx/ir-py)

<details><summary>README extract</summary>

An in-memory IR that supports the full ONNX spec, designed for graph construction, analysis and transformation.

Features:
- Full ONNX spec support: all valid models representable by ONNX protobuf, and a subset of invalid models (so you can load and fix them). ...

Sections: Getting Started, Features ✨, Concept Diagram, Code Organization 🗺️

</details>

### opentelemetry-instrumentation-pymemcache

OpenTelemetry pymemcache instrumentation

`pip install opentelemetry-instrumentation-pymemcache` · installs (wheel) · licence: Apache-2.0 · rank 2399 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-pymemcache/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry pymemcache Instrumentation, References

</details>

### onnxscript

Naturally author ONNX functions and models using a subset of Python

`pip install onnxscript` · installs (wheel) · licence: MIT License · rank 2412 · last release 2026-09-09 · [PyPI](https://pypi.org/project/onnxscript/) · [source](https://github.com/microsoft/onnxscript)

<details><summary>README extract</summary>

ONNX Script enables developers to naturally author ONNX functions and
models using a subset of Python. ONNX Script is:

* Expressive: enables the authoring of all ONNX functions.
* Simple and concise: function code is natural and simple. ...

Example:
```python
import numpy as np

v = np.array([[0, 1], [2, 3]], dtype=np.float32)
result = Hardmax(v)
```

Sections: ONNX Script, Design Overview, Run Unit Tests, Example, Eager Mode Evaluation, ONNX Script Tools, ONNX Optimizer, ONNX Rewriter, Pattern-based rewriting, Coding Style, Licensing Guidelines, Trademarks

</details>

### opentelemetry-instrumentation-cassandra

OpenTelemetry Cassandra instrumentation

`pip install opentelemetry-instrumentation-cassandra` · installs (wheel) · licence: Apache-2.0 · rank 2420 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-cassandra/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Instrumentation for Cassandra (cassandra-driver and scylla-driver libraries).

Sections: OpenTelemetry Cassandra Instrumentation, References

</details>

### opentelemetry-instrumentation-aiopg

OpenTelemetry aiopg instrumentation

`pip install opentelemetry-instrumentation-aiopg` · installs (wheel) · licence: Apache-2.0 · rank 2426 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-aiopg/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry aiopg instrumentation, References

</details>

### opentelemetry-instrumentation-remoulade

OpenTelemetry Remoulade instrumentation

`pip install opentelemetry-instrumentation-remoulade` · installs (wheel) · licence: Apache-2.0 · rank 2432 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-remoulade/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing requests made by the Remoulade library.

Sections: OpenTelemetry Remoulade Instrumentation, References

</details>

### openinference-instrumentation-openai

OpenInference OpenAI Instrumentation

`pip install openinference-instrumentation-openai` · installs (wheel) · licence: Apache-2.0 · rank 2518 · last release 2026-10-31 · [PyPI](https://pypi.org/project/openinference-instrumentation-openai/)

<details><summary>README extract</summary>

Python auto-instrumentation library for OpenAI's python SDK.

The traces emitted by this instrumentation are fully OpenTelemetry compatible and can be sent to an OpenTelemetry collector for viewing, such as Arize Phoenix or Arize AX.

Example:
```python
import openai
from openinference.instrumentation.openai import OpenAIInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

endpoint = "
...
```

Sections: OpenInference OpenAI Instrumentation, SDK compatibility, Decisions API, Quickstart, FAQ, More Info

</details>

### opentelemetry-propagator-jaeger

OpenTelemetry Jaeger Propagator

`pip install opentelemetry-propagator-jaeger` · installs (wheel) · licence: Apache-2.0 · rank 2547 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-propagator-jaeger/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This library provides a propagator for the Jaeger format

Sections: OpenTelemetry Jaeger Propagator, References

</details>

### openlineage-integration-common

OpenLineage common python library for integrations

`pip install openlineage-integration-common` · installs (wheel) · licence: Apache Software License · rank 2567 · last release 2026-10-29 · [PyPI](https://pypi.org/project/openlineage-integration-common/) · [source](https://github.com/OpenLineage/OpenLineage/tree/main/integration/common)

<details><summary>README extract</summary>

Common modules for OpenLineage integrations.

For setting up a development environment, see the Python development setup guide.

Integrations can pass their active database and schema to qualify unqualified
tables and input column origins:

Explicit SQL qualifiers and dialect-specific `USE` statements take precedence
over the supplied defaults. ...

Example:
```python
from openlineage.common.sql import parse

metadata = parse(
    "INSERT INTO target SELECT id FROM source",
    dialect="postgres",
    default_schema="public",
    default_database="mydb",
)
```

Sections: OpenLineage Integration Common, SQL parser defaults

</details>

### openlineage-sql

Python interface for the Rust OpenLineage lineage extraction library

`pip install openlineage-sql` · installs (wheel) · licence: not stated · rank 2584 · last release 2026-10-29 · [PyPI](https://pypi.org/project/openlineage-sql/)

<details><summary>README extract</summary>

Refer to the GitHub for details. This package is not meant to be used alone by end-user.

</details>

### opentelemetry-propagator-ot-trace

OT Trace Propagator for OpenTelemetry

`pip install opentelemetry-propagator-ot-trace` · installs (wheel) · licence: Apache-2.0 · rank 2593 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-propagator-ot-trace/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry OT Trace Propagator, OTTrace Format, Interop and trace ids, References

</details>

### oyaml

Ordered YAML: drop-in replacement for PyYAML which preserves dict ordering

`pip install oyaml` · installs (wheel) · licence: MIT · rank 2608 · last release 2020-08-18 · [PyPI](https://pypi.org/project/oyaml/)

<details><summary>README extract</summary>

oyaml is a drop-in replacement for PyYAML which preserves dict ordering. Both Python 2 and Python 3 are supported. Just `pip install oyaml`, and import as shown below:

You'll no longer be annoyed by screwed-up mappings when dumping/loading.

Example:
```python
import oyaml as yaml
```

</details>

### o365

O365 - Microsoft Graph and Office 365 API made easy

`pip install o365` · installs (wheel) · licence: Apache Software License · rank 2679 · last release 2026-09-09 · [PyPI](https://pypi.org/project/o365/)

<details><summary>README extract</summary>

This project aims to make interacting with the Microsoft api, and related apis, easy to do in a Pythonic way.
Access to Email, Calendar, Contacts, OneDrive, Sharepoint, etc. Are easy to do in a way that feel easy and straight forward to beginners and feels just right to seasoned python programmer. ...

Features:
- Almost Full Support for MsGraph Rest Api.
- Good Abstraction layer for the Api.
- Full oauth support with automatic handling of refresh tokens.
- Automatic handling between local datetimes and server datetimes. ...

Example:
```python
from O365 import Account

credentials = ('client_id', 'client_secret')

account = Account(credentials)
m = account.new_message()
m.to.add('to_example@example.com')
m.subject = 'Testing!'
...

</details>

### openmed

Local-first SDK for clinical extraction and de-identification workflows on hardware you control.

`pip install openmed` · installs (wheel) · licence: Apache-2.0 · rank 2762 · last release 2026-11-03 · [PyPI](https://pypi.org/project/openmed/)

<details><summary>README extract</summary>

Turn clinical text into structured, de-identified insight on hardware you control.

OpenMed's core local runtime performs extraction and de-identification after required model artifacts are available. ...

Features:
| Deployment consideration | OpenMed SDK boundary |

| Core runtime | Processes locally after required artifacts are available |
| Optional network paths | Downloads, remote adapters, telemetry-enabled paths, and user integrations may use a network ...

Example:
```python
from openmed import analyze_text

result = analyze_text(
    "Patient started on imatinib for chronic myeloid leukemia.",
    model_name="disease_detection_superclinical",
)

for entity in result.entities:
    print(f"{entity.label:<12} {entity.text:<28} {entity.confidence:.2f}")
...

</details>

### opentelemetry-instrumentation-openai-v2

OpenTelemetry Official OpenAI instrumentation

`pip install opentelemetry-instrumentation-openai-v2` · installs (wheel) · licence: Apache-2.0 · rank 2778 · last release 2026-05-01 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-openai-v2/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing LLM requests and logging of messages made by the
OpenAI Python API library. It also captures
the duration of the operations and the number of tokens used as metrics.

Many LLM platforms support the OpenAI SDK. This means systems such as the following are observable with this instrumentation when accessed using it:

Example:
```python
from opentelemetry.instrumentation.openai_v2 import OpenAIInstrumentor

OpenAIInstrumentor().instrument()

client = OpenAI()
# Chat completion example
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Write a short poem on open telemetry."},
    ],
)

# Embeddings example
...
```

...

</details>

### openai-codex-cli-bin

Pinned Codex CLI runtime for the Python SDK

`pip install openai-codex-cli-bin` · installs (wheel) · licence: Apache Software License · rank 2803 · last release 2026-11-06 · [PyPI](https://pypi.org/project/openai-codex-cli-bin/) · [source](https://github.com/openai/codex)

<details><summary>README extract</summary>

Platform-specific runtime package consumed by the published `openai-codex`.

This package is staged during release so the SDK can pin an exact Codex CLI
version without checking platform binaries into the repo.

`openai-codex-cli-bin` is intentionally wheel-only. Do not build or publish an
sdist for this package.

</details>

### opik

Comet tool for logging and evaluating LLM traces

`pip install opik` · installs (wheel) · licence: Apache Software License · rank 2806 · last release 2026-11-06 · [PyPI](https://pypi.org/project/opik/) · [source](https://github.com/comet-ml/opik)

<details><summary>README extract</summary>

English | 简体中文 | Español | Français | Deutsch | 日本語

 Opik: Open-Source LLM Observability, Evaluation & AI Agent Tracing

Opik is the open-source LLM observability and evaluation platform for AI agent tracing, LLM evaluation, prompt management, and production monitoring. Built by Comet. ...

Example:
```python
from opik import track

@track
def my_function(input: str) -> str:
    return input
```

...

</details>

### owlrl

A simple implementation of the OWL2 RL Profile, as well as a basic RDFS inference, on top of RDFLib. Based mechanical forward chaining.

`pip install owlrl` · installs (wheel) · licence: OSI Approved · rank 2822 · last release 2026-07-08 · [PyPI](https://pypi.org/project/owlrl/) · [source](https://github.com/RDFLib/OWL-RL)

<details><summary>README extract</summary>

* Installation
* Use
* License
* Support & Contacts
* Development

A simple implementation of the OWL2 RL Profile, as well as a basic RDFS inference, on top of RDFLib, based on forward-chaining.

Sections: OWL-RL, Use, Scripts, Oxigraph store (optional), Changes

</details>

### opentelemetry-instrumentation-vertexai

OpenTelemetry Vertex AI instrumentation

`pip install opentelemetry-instrumentation-vertexai` · installs (wheel) · licence: Apache-2.0 · rank 2833 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-vertexai/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-vertexai)

<details><summary>README extract</summary>

This library allows tracing VertexAI prompts and completions sent with the official VertexAI library.

Example:
```python
from opentelemetry.instrumentation.vertexai import VertexAIInstrumentor

VertexAIInstrumentor().instrument()
```

Sections: OpenTelemetry VertexAI Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-google-generativeai

OpenTelemetry Google Generative AI instrumentation

`pip install opentelemetry-instrumentation-google-generativeai` · installs (wheel) · licence: Apache-2.0 · rank 2861 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-google-generativeai/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-google-generativeai)

<details><summary>README extract</summary>

This library allows tracing Google Gemini prompts and completions sent with the official Google Generative AI library.

Example:
```python
from opentelemetry.instrumentation.google_generativeai import GoogleGenerativeAiInstrumentor

GoogleGenerativeAiInstrumentor().instrument()
```

Sections: OpenTelemetry Google Generative AI Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-bedrock

OpenTelemetry Bedrock instrumentation

`pip install opentelemetry-instrumentation-bedrock` · installs (wheel) · licence: Apache-2.0 · rank 2869 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-bedrock/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-bedrock)

<details><summary>README extract</summary>

This library allows tracing any of AWS Bedrock's models prompts and completions sent with Boto3 to Bedrock.

Example:
```python
from opentelemetry.instrumentation.bedrock import BedrockInstrumentor

BedrockInstrumentor().instrument()
```

Sections: OpenTelemetry Bedrock Instrumentation, Example usage, Privacy

</details>

### openrouter

Official Python Client SDK for OpenRouter.

`pip install openrouter` · installs (wheel) · licence: Apache-2.0 · rank 2894 · last release 2026-11-08 · [PyPI](https://pypi.org/project/openrouter/) · [source](https://github.com/OpenRouterTeam/python-sdk.git)

<details><summary>README extract</summary>

The OpenRouter SDK is a Python toolkit designed to help you build AI-powered features and solutions. Giving you easy access to 400+ models across providers in an easy and type-safe way.

The OpenRouter Python SDK is stable as of v1.0.

To learn more about how to use the OpenRouter SDK, check out our API Reference and Documentation. ...

Example:
```python
# !/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
# "openrouter",
# ]
# ///

from openrouter import OpenRouter

sdk = OpenRouter(
  # SDK arguments
)

# Rest of script here...
```

Sections: OpenRouter SDK, uv, PIP, Poetry, Shell and script usage with `uv`, Requirements, PyCharm, SDK Usage, Web Search, Pagination, File uploads, Resource Management, Debugging, Running Tests

</details>

### opentelemetry-instrumentation-crewai

OpenTelemetry crewAI instrumentation

`pip install opentelemetry-instrumentation-crewai` · installs (wheel) · licence: Apache-2.0 · rank 2934 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-crewai/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-crewai)

<details><summary>README extract</summary>

This library allows tracing agentic workflows implemented with crewAI framework crewAI library.

Example:
```python
from opentelemetry.instrumentation.crewai import CrewAIInstrumentor

CrewAIInstrumentor().instrument()
```

Sections: OpenTelemetry CrewAI Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-qdrant

OpenTelemetry Qdrant instrumentation

`pip install opentelemetry-instrumentation-qdrant` · installs (wheel) · licence: Apache-2.0 · rank 2940 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-qdrant/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-qdrant)

<details><summary>README extract</summary>

This library allows tracing client-side calls to Qdrant vector DB sent with the official Qdrant client library.

Example:
```python
from opentelemetry.instrumentation.qdrant import QdrantInstrumentor

QdrantInstrumentor().instrument()
```

Sections: OpenTelemetry Qdrant Instrumentation, Example usage

</details>

### opentelemetry-instrumentation-cohere

OpenTelemetry Cohere instrumentation

`pip install opentelemetry-instrumentation-cohere` · installs (wheel) · licence: Apache-2.0 · rank 2971 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-cohere/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-cohere)

<details><summary>README extract</summary>

This library allows tracing calls to any of Cohere's endpoints sent with the official Cohere library.

Example:
```python
from opentelemetry.instrumentation.cohere import CohereInstrumentor

CohereInstrumentor().instrument()
```

Sections: OpenTelemetry Cohere Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-llamaindex

OpenTelemetry LlamaIndex instrumentation

`pip install opentelemetry-instrumentation-llamaindex` · installs (wheel) · licence: Apache-2.0 · rank 2981 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-llamaindex/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-llamaindex)

<details><summary>README extract</summary>

This library allows tracing complete LLM applications built with LlamaIndex.

Example:
```python
from opentelemetry.instrumentation.llamaindex import LlamaIndexInstrumentor

LlamaIndexInstrumentor().instrument()
```

Sections: OpenTelemetry LlamaIndex Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-ollama

OpenTelemetry Ollama instrumentation

`pip install opentelemetry-instrumentation-ollama` · installs (wheel) · licence: Apache-2.0 · rank 2999 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-ollama/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-ollama)

<details><summary>README extract</summary>

This library allows tracing calls to any of Ollama's endpoints sent with the official Ollama Python Library.

Example:
```python
from opentelemetry.instrumentation.ollama import OllamaInstrumentor

OllamaInstrumentor().instrument()
```

Sections: OpenTelemetry Ollama Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-transformers

OpenTelemetry transformers instrumentation

`pip install opentelemetry-instrumentation-transformers` · installs (wheel) · licence: Apache-2.0 · rank 3005 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-transformers/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-transformers)

<details><summary>README extract</summary>

This library allows tracing texte generation calls sent with the official HuggingFace Transformers library.

Example:
```python
from opentelemetry.instrumentation.transformers import TransformersInstrumentor

TransformersInstrumentor().instrument()
```

Sections: OpenTelemetry HuggingFace Transformers Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-replicate

OpenTelemetry Replicate instrumentation

`pip install opentelemetry-instrumentation-replicate` · installs (wheel) · licence: Apache-2.0 · rank 3013 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-replicate/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-replicate)

<details><summary>README extract</summary>

This library allows tracing Replicate prompts and image generation sent with the official replicate library.

Example:
```python
from opentelemetry.instrumentation.replicate import ReplicateInstrumentor

ReplicateInstrumentor().instrument()
```

Sections: OpenTelemetry Replicate Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-weaviate

OpenTelemetry Weaviate instrumentation

`pip install opentelemetry-instrumentation-weaviate` · installs (wheel) · licence: Apache-2.0 · rank 3014 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-weaviate/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-weaviate)

<details><summary>README extract</summary>

This library allows tracing client-side calls to Weaviate vector DB sent with the official Weaviate library.

Example:
```python
from opentelemetry.instrumentation.weaviate import WeaviateInstrumentor

WeaviateInstrumentor().instrument()
```

Sections: OpenTelemetry Weaviate Instrumentation, Example usage

</details>

### opentelemetry-instrumentation-mcp

OpenTelemetry mcp instrumentation

`pip install opentelemetry-instrumentation-mcp` · installs (wheel) · licence: Apache-2.0 · rank 3015 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-mcp/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-mcp)

<details><summary>README extract</summary>

OpenTelemetry MCP Instrumentation

This library allows tracing of agentic workflows implemented with MCP framework mcp python sdk.

Example:
```python
from opentelemetry.instrumentation.mcp import McpInstrumentor

McpInstrumentor().instrument()
```

Sections: Example usage, Privacy, Diagnostics

</details>

### opentelemetry-instrumentation-watsonx

OpenTelemetry IBM Watsonx Instrumentation

`pip install opentelemetry-instrumentation-watsonx` · installs (wheel) · licence: Apache-2.0 · rank 3017 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-watsonx/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-watsonx)

<details><summary>README extract</summary>

This library allows tracing IBM Watsonx prompts and completions sent with the official IBM Watson Machine Learning library and IBM watsonx.ai library.

Example:
```python
from opentelemetry.instrumentation.watsonx import WatsonxInstrumentor

WatsonxInstrumentor().instrument()
```

Sections: OpenTelemetry IBM Watsonx Instrumentation, Example usage, Privacy, SSL Issue

</details>

### opentelemetry-instrumentation-mistralai

OpenTelemetry Mistral AI instrumentation

`pip install opentelemetry-instrumentation-mistralai` · installs (wheel) · licence: Apache-2.0 · rank 3019 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-mistralai/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-mistralai)

<details><summary>README extract</summary>

This library allows tracing calls to any of mistralai's endpoints sent with the official Mistral AI library.

Example:
```python
from opentelemetry.instrumentation.mistralai import MistralAiInstrumentor

MistralAiInstrumentor().instrument()
```

Sections: OpenTelemetry Mistral AI Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-chromadb

OpenTelemetry Chroma DB instrumentation

`pip install opentelemetry-instrumentation-chromadb` · installs (wheel) · licence: Apache-2.0 · rank 3020 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-chromadb/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-chromadb)

<details><summary>README extract</summary>

This library allows tracing client-side calls to Chroma vector DB sent with the official Chroma library.

Example:
```python
from opentelemetry.instrumentation.chromadb import ChromaInstrumentor

ChromaInstrumentor().instrument()
```

Sections: OpenTelemetry Chroma Instrumentation, Example usage

</details>

### opentelemetry-instrumentation-together

OpenTelemetry Together AI instrumentation

`pip install opentelemetry-instrumentation-together` · installs (wheel) · licence: Apache-2.0 · rank 3021 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-together/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-together)

<details><summary>README extract</summary>

This library allows tracing calls to any of Together AI's endpoints sent with the official Together AI Library.

Example:
```python
from opentelemetry.instrumentation.together import TogetherAiInstrumentor

TogetherAiInstrumentor().instrument()
```

Sections: OpenTelemetry Together AI Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-sagemaker

OpenTelemetry SageMaker instrumentation

`pip install opentelemetry-instrumentation-sagemaker` · installs (wheel) · licence: Apache-2.0 · rank 3023 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-sagemaker/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-sagemaker)

<details><summary>README extract</summary>

This library allows tracing of any models deployed on Amazon SageMaker and invoked with Boto3 to SageMaker.

Example:
```python
from opentelemetry.instrumentation.sagemaker import SageMakerInstrumentor

SageMakerInstrumentor().instrument()
```

Sections: OpenTelemetry SageMaker Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-milvus

OpenTelemetry Milvus instrumentation

`pip install opentelemetry-instrumentation-milvus` · installs (wheel) · licence: Apache-2.0 · rank 3025 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-milvus/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-milvus)

<details><summary>README extract</summary>

This library allows tracing client-side calls to Milvus vector DB sent with the official Milvus library.

Example:
```python
from opentelemetry.instrumentation.milvus import MilvusInstrumentor

MilvusInstrumentor().instrument()
```

Sections: OpenTelemetry Milvus Instrumentation, Example usage

</details>

### opentelemetry-instrumentation-alephalpha

OpenTelemetry Aleph Alpha instrumentation

`pip install opentelemetry-instrumentation-alephalpha` · installs (wheel) · licence: Apache-2.0 · rank 3028 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-alephalpha/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-alephalpha)

<details><summary>README extract</summary>

This library allows tracing calls to any of Aleph Alpha's endpoints sent with the official Aleph Alpha Client.

Example:
```python
from opentelemetry.instrumentation.alephalpha import AlephAlphaInstrumentor

AlephAlphaInstrumentor().instrument()
```

Sections: OpenTelemetry Aleph Alpha Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-pinecone

OpenTelemetry Pinecone instrumentation

`pip install opentelemetry-instrumentation-pinecone` · installs (wheel) · licence: Apache-2.0 · rank 3031 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-pinecone/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-pinecone)

<details><summary>README extract</summary>

This library allows tracing client-side calls to Pinecone vector DB sent with the official Pinecone library.

Example:
```python
from opentelemetry.instrumentation.pinecone import PineconeInstrumentor

PineconeInstrumentor().instrument()
```

Sections: OpenTelemetry Pinecone Instrumentation, Example usage

</details>

### opentelemetry-instrumentation-lancedb

OpenTelemetry Lancedb instrumentation

`pip install opentelemetry-instrumentation-lancedb` · installs (wheel) · licence: Apache-2.0 · rank 3034 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-lancedb/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-lancedb)

<details><summary>README extract</summary>

This library allows tracing client-side calls to LanceDB sent with the official LanceDB library.

Example:
```python
from opentelemetry.instrumentation.lancedb import LanceInstrumentor

LanceInstrumentor().instrument()
```

Sections: OpenTelemetry LanceDB Instrumentation, Example usage

</details>

### opentelemetry-instrumentation-marqo

OpenTelemetry Marqo instrumentation

`pip install opentelemetry-instrumentation-marqo` · installs (wheel) · licence: Apache-2.0 · rank 3036 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-marqo/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-marqo)

<details><summary>README extract</summary>

This library allows tracing client-side calls to Marqo vector DB sent with the official Marqo library.

Example:
```python
from opentelemetry.instrumentation.marqo import MarqoInstrumentor

MarqoInstrumentor().instrument()
```

Sections: OpenTelemetry Marqo Instrumentation, Example usage

</details>

### opentelemetry-instrumentation-haystack

OpenTelemetry Haystack instrumentation

`pip install opentelemetry-instrumentation-haystack` · installs (wheel) · licence: Apache-2.0 · rank 3052 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-haystack/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-haystack)

<details><summary>README extract</summary>

This library allows tracing complete LLM applications built with Haystack.

Example:
```python
from opentelemetry.instrumentation.haystack import HaystackInstrumentor

HaystackInstrumentor().instrument()
```

Sections: OpenTelemetry Haystack Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-groq

OpenTelemetry Groq instrumentation

`pip install opentelemetry-instrumentation-groq` · installs (wheel) · licence: Apache-2.0 · rank 3062 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-groq/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-groq)

<details><summary>README extract</summary>

This library allows tracing Groq prompts and completions sent with the official Groq SDK.

Example:
```python
from opentelemetry.instrumentation.groq import GroqInstrumentor

GroqInstrumentor().instrument()
```

Sections: OpenTelemetry Groq Instrumentation, Example usage, Privacy

</details>

### openfga-sdk

A high performance and flexible authorization/permission engine built for developers and inspired by Google Zanzibar.

`pip install openfga-sdk` · installs (wheel) · licence: Apache-2.0 · rank 3066 · last release 2026-09-29 · [PyPI](https://pypi.org/project/openfga-sdk/) · [source](https://github.com/openfga/python-sdk.git)

<details><summary>README extract</summary>

<!-- x-release-please-version -->

This is an autogenerated python SDK for OpenFGA. It provides a wrapper around the OpenFGA API definition.

Example:
```python
# Call a custom endpoint using path parameters
response = await fga_client.execute_api_request(
    operation_name="CustomEndpoint",        # For telemetry/logging
    method="POST",
    path="/stores/{store_id}/custom-endpoint",
    path_params={"store_id": FGA_STORE_ID},
    body={
        "user": "user:bob",
        "action": "custom_action",
...
```

Sections: Python SDK for OpenFGA, About, Resources, PyPI, GitHub, Setuptools, Getting Started, Initializing the API Client, No Credentials, API Token, Client Credentials, OAuth2 Client Credentials (Standard OAuth2), Custom Headers, Default Headers

</details>

### opentelemetry-propagator-gcp

Google Cloud propagator for OpenTelemetry

`pip install opentelemetry-propagator-gcp` · installs (wheel) · licence: Apache Software License · rank 3102 · last release 2026-08-19 · [PyPI](https://pypi.org/project/opentelemetry-propagator-gcp/)

<details><summary>README extract</summary>

This library provides support for propagating trace context in the Google
Cloud `X-Cloud-Trace-Context` format.

To get started with instrumentation in Google Cloud, see Generate traces and metrics with
Python. ...

Example:
```python
from opentelemetry.propagate import set_global_textmap
from opentelemetry.propagators.composite import CompositePropagator
from opentelemetry.propagators.cloud_trace_propagator import (
    CloudTraceOneWayPropagator,
)
set_global_textmap(
    CompositePropagator([
        CloudTraceOneWayPropagator(),
        propagate.get_global_textmap(),
...
```

Sections: OpenTelemetry Google Cloud Propagator, Usage, References

</details>

### opentelemetry-instrumentation-openai-agents

OpenTelemetry OpenAI Agents instrumentation

`pip install opentelemetry-instrumentation-openai-agents` · installs (wheel) · licence: Apache-2.0 · rank 3148 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-openai-agents/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-openai-agents)

<details><summary>README extract</summary>

This library enables tracing of agentic workflows implemented using the OpenAI Agents framework, allowing visibility into agent reasoning, tool usage, and decision-making steps.

Example:
```python
from opentelemetry.instrumentation.openai_agents import OpenAIAgentsInstrumentor

OpenAIAgentsInstrumentor().instrument()
```

Sections: OpenTelemetry OpenAI Agents Instrumentation, Example usage, Privacy

</details>

### onnxconverter-common

ONNX Converter and Optimization Tools

`pip install onnxconverter-common` · installs (wheel) · licence: MIT License · rank 3150 · last release 2025-08-28 · [PyPI](https://pypi.org/project/onnxconverter-common/) · [source](https://github.com/microsoft/onnxconverter-common)

<details><summary>README extract</summary>

| Linux | Windows |

| | |

The onnxconverter-common package provides common functions and utilities for use in converters from various AI frameworks to ONNX. It also enables the different converters to work together to convert a model from mixed frameworks, like a scikit-learn pipeline embedding a xgboost model.

Sections: Introduction, Document

</details>

### opentelemetry-instrumentation-elasticsearch

OpenTelemetry elasticsearch instrumentation

`pip install opentelemetry-instrumentation-elasticsearch` · installs (wheel) · licence: Apache-2.0 · rank 3166 · last release 2026-06-24 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-elasticsearch/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing elasticsearch made by the
elasticsearch library.

Sections: OpenTelemetry elasticsearch Integration, References

</details>

### opentelemetry-instrumentation-writer

OpenTelemetry Writer instrumentation

`pip install opentelemetry-instrumentation-writer` · installs (wheel) · licence: Apache-2.0 · rank 3244 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-writer/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-writer)

<details><summary>README extract</summary>

This library allows tracing calls to any of Writer's endpoints sent with the official Writer Python Library.

Example:
```python
from opentelemetry.instrumentation.writer import WriterInstrumentor

WriterInstrumentor().instrument()
```

Sections: OpenTelemetry Writer Instrumentation, Example usage, Privacy

</details>

### opentelemetry-instrumentation-agno

OpenTelemetry Agno instrumentation

`pip install opentelemetry-instrumentation-agno` · installs (wheel) · licence: Apache-2.0 · rank 3268 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-agno/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-agno)

<details><summary>README extract</summary>

This library provides automatic instrumentation for the Agno framework.

Example:
```python
from opentelemetry.instrumentation.agno import AgnoInstrumentor

AgnoInstrumentor().instrument()
```

Sections: OpenTelemetry Agno Instrumentation, Usage, Links

</details>

### opentelemetry-instrumentation-voyageai

OpenTelemetry Voyage AI instrumentation

`pip install opentelemetry-instrumentation-voyageai` · installs (wheel) · licence: Apache-2.0 · rank 3281 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-voyageai/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-voyageai)

<details><summary>README extract</summary>

This library allows tracing Voyage AI API calls with OpenTelemetry.

Example:
```python
from opentelemetry.instrumentation.voyageai import VoyageAIInstrumentor

VoyageAIInstrumentor().instrument()

# Now use Voyage AI as usual
import voyageai

client = voyageai.Client()

# Embeddings
result = client.embed(texts=["Hello, world!"], model="voyage-3")

# Reranking
result = client.rerank(
    query="What is the capital of France?",
...
```

Sections: OpenTelemetry Voyage AI Instrumentation, Usage, Semantic Conventions

</details>

### opsgenie-sdk

Python SDK for Opsgenie REST API

`pip install opsgenie-sdk` · installs (wheel) · licence: Apache Software License · rank 3311 · last release 2021-08-02 · [PyPI](https://pypi.org/project/opsgenie-sdk/) · [docs](https://docs.opsgenie.com/docs/opsgenie-python-api) · [source](https://github.com/opsgenie/opsgenie-python-sdk)

<details><summary>README extract</summary>

This Python package is automatically generated by the OpenAPI Generator project:

- API version: 2.0.0
- Package version: 2.1.5
- Build package: com.atlassian.opsgenie.codegen.geniepy.GeniepyGenerator

For more information, please visit

Python 2.7 and 3.4+

Example:
```python
from future import print_function
import time
import opsgenie_sdk
from opsgenie_sdk.rest import ApiException
from pprint import pprint

configuration = opsgenie_sdk.Configuration()
# Configure API key authorization: GenieKey
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# create an instance of the API class
...
```

Sections: Python SDK for Opsgenie REST API, Requirements., Setuptools, Getting Started, Documentation for API Endpoints, Documentation For Models, GenieKey

</details>

### opentelemetry-instrumentation-google-genai

OpenTelemetry

`pip install opentelemetry-instrumentation-google-genai` · installs (wheel) · licence: Apache-2.0 · rank 3387 · last release 2026-10-23 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-google-genai/) · [source](https://github.com/open-telemetry/opentelemetry-python-genai)

<details><summary>README extract</summary>

This library adds instrumentation to the Google GenAI SDK library
to emit telemetry data following Semantic Conventions for GenAI systems.
It adds trace spans for GenAI operations, events/logs for recording prompts/responses, and emits metrics that describe the
GenAI operations in aggregate. ...

Example:
```python
from opentelemetry.instrumentation.google_genai import GoogleGenAiSdkInstrumentor
from google.genai import Client

GoogleGenAiSdkInstrumentor().instrument()

client = Client()
response = client.models.generate_content(
    model="gemini-1.5-flash-002",
    contents="Write a short poem on OpenTelemetry."
)
```

...

</details>

### openai-mcp-extensions

OpenAI extensions for MCP Python servers.

`pip install openai-mcp-extensions` · installs (wheel) · licence: Apache-2.0 · rank 3507 · last release 2026-10-21 · [PyPI](https://pypi.org/project/openai-mcp-extensions/) · [source](https://github.com/openai/mcp-extensions)

<details><summary>README extract</summary>

The Python SDK provides server-side OpenAI extensions for the official MCP Python SDK. Use `@openai/mcp-extensions/app` for MCP App extensions.

Example:
```python
from mcp.server.apps import Apps
from mcp.server.mcpserver import MCPServer

from openai_mcp_extensions import OpenAIExtensions

apps = Apps()
openai_extensions = OpenAIExtensions()
```

Sections: OpenAI MCP Extensions for Python, Server Setup, Structured Settings, UI Entrypoints, Filesystem Access, Composer Mentions, Multi-round-trip Requests, Suggested Values, Resource Selection

</details>

### opentelemetry-instrumentation-openai-agents-v2

OpenTelemetry OpenAI Agents instrumentation (barebones)

`pip install opentelemetry-instrumentation-openai-agents-v2` · installs (wheel) · licence: Apache-2.0 · rank 3527 · last release 2025-10-15 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-openai-agents-v2/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

### opentelemetry-instrumentation-aiohttp-server

Aiohttp server instrumentation for OpenTelemetry

`pip install opentelemetry-instrumentation-aiohttp-server` · installs (wheel) · licence: Apache-2.0 · rank 3542 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-aiohttp-server/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing HTTP requests made by the
aiohttp server library.

Sections: OpenTelemetry aiohttp server Integration, References

</details>

### opentelemetry-instrumentation-boto

OpenTelemetry Boto instrumentation

`pip install opentelemetry-instrumentation-boto` · installs (wheel) · licence: Apache-2.0 · rank 3567 · last release 2026-03-04 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-boto/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing requests made by the Boto library.

Sections: OpenTelemetry Boto Tracing, References

</details>

### openinference-instrumentation-openai-agents

OpenInference OpenAI Agents Instrumentation

`pip install openinference-instrumentation-openai-agents` · installs (wheel) · licence: Apache-2.0 · rank 3606 · last release 2026-11-04 · [PyPI](https://pypi.org/project/openinference-instrumentation-openai-agents/)

<details><summary>README extract</summary>

Python auto-instrumentation library for OpenAI Agents python SDK.

The traces emitted by this instrumentation are fully OpenTelemetry compatible and can be sent to an OpenTelemetry collector for viewing, such as Arize Phoenix or Arize AX.

| `openinference-instrumentation-openai-agents` | `openai-agents` | Python | ...

Example:
```python
from agents import Agent, Runner
from openinference.instrumentation.openai_agents import OpenAIAgentsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

endpoint = "
...
```

...

</details>

### objprint

A library that can print Python objects in human readable format

`pip install objprint` · installs (wheel) · licence: Apache Software License · rank 3614 · last release 2024-11-09 · [PyPI](https://pypi.org/project/objprint/)

<details><summary>README extract</summary>

A library that can print Python objects in human readable format

Example:
```python
from objprint import op

class Position:
    def init(self, x, y):
        self.x = x
        self.y = y

class Player:
    def init(self):
        self.name = "Alice"
        self.age = 18
        self.items = ["axe", "armor"]
        self.coins = {"gold": 1, "silver": 33, "bronze": 57}
        self.position = Position(3, 5)

op(Player())
```

Sections: objprint, Usage, op, add_objprint, This will print the same thing as above, Register Custom Type Formatter, config, Now you can use op() in any file, This is the same, You can specify a name for objprint()

</details>

### opentelemetry-instrumentation-click

Click instrumentation for OpenTelemetry

`pip install opentelemetry-instrumentation-click` · installs (wheel) · licence: Apache-2.0 · rank 3639 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-click/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing requests made by the click library.

Sections: OpenTelemetry click Instrumentation, References

</details>

### os-service-types

Python library for consuming OpenStack sevice-types-authority data

`pip install os-service-types` · installs (wheel) · licence: Apache-2.0 · rank 3685 · last release 2026-08-04 · [PyPI](https://pypi.org/project/os-service-types/) · [source](https://opendev.org/openstack/os-service-types/)

<details><summary>README extract</summary>

Python library for consuming OpenStack sevice-types-authority data

The OpenStack Service Types Authority contains information about official
OpenStack services and their historical `service-type` aliases.

The data is in JSON and the latest data should always be used. ...

</details>

### opentelemetry-resourcedetector-docker

An OpenTelemetry package to populates Resource attributes from Docker containers

`pip install opentelemetry-resourcedetector-docker` · installs (wheel) · licence: MIT License · rank 3763 · last release 2022-09-18 · [PyPI](https://pypi.org/project/opentelemetry-resourcedetector-docker/)

<details><summary>README extract</summary>

An OpenTelemetry package to populates Resource attributes from Docker containers.

Example:
```python
from opentelemetry.sdk.resources import get_aggregated_resources
from opentelemetry_resourcedetector_docker import DockerResourceDetector

...

resource = get_aggregated_resources([
    DockerResourceDetector(),
    SomeOtherResourceDetector()
])

... pass the returned `resource` to a TracerProvder, for example ...
```

Sections: opentelemetry-resourcedetector-docker, Usage

</details>

### opentelemetry-resourcedetector-kubernetes

An OpenTelemetry package to populates Resource attributes for Kubernetes pods

`pip install opentelemetry-resourcedetector-kubernetes` · installs (wheel) · licence: MIT License · rank 3774 · last release 2022-09-18 · [PyPI](https://pypi.org/project/opentelemetry-resourcedetector-kubernetes/)

<details><summary>README extract</summary>

An OpenTelemetry package to populates Resource attributes for Kubernetes pods.

Example:
```python
from opentelemetry.sdk.resources import get_aggregated_resources
from opentelemetry_resourcedetector_kubernetes import KubernetesResourceDetector

...

resource = get_aggregated_resources([
    KubernetesResourceDetector(),
    SomeOtherResourceDetector()
])

... pass the returned `resource` to a TracerProvder, for example ...
```

Sections: opentelemetry-resourcedetector-kubernetes, Usage, Detecting more attributes with The "Downward API", KubernetesDownwardAPIEnvironmentResourceDetector, KubernetesDownwardAPIVolumeResourceDetector

</details>

### openevals

Open-source evaluators for LLM applications

`pip install openevals` · installs (wheel) · licence: MIT · rank 3786 · last release 2026-10-22 · [PyPI](https://pypi.org/project/openevals/)

<details><summary>README extract</summary>

Much like tests in traditional software, evals are an important part of bringing LLM applications to production.
The goal of this package is to help provide a starting point for you to write evals for your LLM applications, from which
you can write more custom evals specific to your application. ...

Example:
```python
from openevals.llm import create_llm_as_judge
from openevals.prompts import CONCISENESS_PROMPT

conciseness_evaluator = create_llm_as_judge(
    # CONCISENESS_PROMPT is just an f-string
    prompt=CONCISENESS_PROMPT,
    model="openai:gpt-5.6-sol",
)

inputs = "How is the weather in San Francisco?"
...
```

...

</details>

### OpenEXR

Python bindings for the OpenEXR image file format

`pip install OpenEXR` · installs (wheel) · licence: not stated · rank 3858 · last release 2026-10-31 · [PyPI](https://pypi.org/project/OpenEXR/) · [source](https://github.com/AcademySoftwareFoundation/OpenEXR)

<details><summary>README extract</summary>

<!-- SPDX-License-Identifier: BSD-3-Clause -->
<!-- Copyright (c) Contributors to the OpenEXR Project -->

OpenEXR provides the specification and reference implementation of the
EXR file format, the professional-grade image storage format of the
motion picture industry. ...

Sections: OpenEXR, OpenEXR Project Mission, Python Module, Project Governance, Quick Start, Resources

</details>

### ocpsvg

(no summary)

`pip install ocpsvg` · installs (wheel) · licence: not stated · rank 3882 · last release 2026-09-12 · [PyPI](https://pypi.org/project/ocpsvg/)

<details><summary>README extract</summary>

- works at the `OCP` level

 - convert SVG path strings to and from `TopoDS_Edge`, `TopoDS_Wire`, and `TopoDS_Face` objects
 - import `TopoDS_Wire` and `TopoDS_Face` objects from an SVG document
- can be used to add SVG functionality (import and export) to higher level API

</details>

### oslo.utils

Oslo Utility library

`pip install oslo.utils` · installs (wheel) · licence: Apache-2.0 · rank 3902 · last release 2026-08-24 · [PyPI](https://pypi.org/project/oslo.utils/) · [source](https://opendev.org/openstack/oslo.utils)

<details><summary>README extract</summary>

The oslo.utils library provides support for common utility type functions,
such as encoding, exception handling, string manipulation, and time handling.

* Free software: Apache license

</details>

### openinference-instrumentation-claude-agent-sdk

OpenInference Claude Agent SDK Instrumentation

`pip install openinference-instrumentation-claude-agent-sdk` · installs (wheel) · licence: Apache-2.0 · rank 3978 · last release 2026-11-04 · [PyPI](https://pypi.org/project/openinference-instrumentation-claude-agent-sdk/)

<details><summary>README extract</summary>

Python auto-instrumentation for the Claude Agent SDK (Python). Traces `query()` and `ClaudeSDKClient` as OpenInference AGENT spans with prompt input, result output, session/model metadata, token counts, and tool child spans via hook injection.

- `query()` – One span per call (one-off sessions). ...

Example:
```python
import asyncio
import os
from claude_agent_sdk import query, ClaudeAgentOptions
from openinference.instrumentation.claude_agent_sdk import ClaudeAgentSDKInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
...
```

Sections: OpenInference Claude Agent SDK Instrumentation, Quickstart, Examples, What is instrumented, More Info

</details>

### oslo.i18n

Oslo i18n library

`pip install oslo.i18n` · installs (wheel) · licence: Apache-2.0 · rank 4009 · last release 2026-07-10 · [PyPI](https://pypi.org/project/oslo.i18n/) · [source](https://opendev.org/openstack/oslo.i18n)

<details><summary>README extract</summary>

The oslo.i18n library contain utilities for working with
internationalization (i18n) features, especially translation for text
strings in an application or library.

* Free software: Apache license

</details>

### openstacksdk

An SDK for building applications to work with OpenStack

`pip install openstacksdk` · installs (wheel) · licence: Apache-2.0 · rank 4037 · last release 2026-10-22 · [PyPI](https://pypi.org/project/openstacksdk/) · [source](https://opendev.org/openstack/openstacksdk/)

<details><summary>README extract</summary>

openstacksdk is a client library for building applications to work
with OpenStack clouds. The project aims to provide a consistent and
complete set of interactions with OpenStack's many services, along with
complete documentation, examples, and tools.

It also contains an abstraction interface layer. ...

Example:
```python
import openstack

# Initialize connection from a clouds.yaml by passing a cloud name
conn_from_cloud_name = openstack.connect(cloud='mordred')

# Initialize connection from a clouds.yaml using the OS_CLOUD envvar
conn_from_os_cloud = openstack.connect()

# Initialize connection from environment variables
...
```

Sections: openstacksdk, Getting started, Configuration, Links

</details>

### oslo.config

Oslo Configuration API

`pip install oslo.config` · installs (wheel) · licence: Apache-2.0 · rank 4089 · last release 2026-10-28 · [PyPI](https://pypi.org/project/oslo.config/) · [source](https://opendev.org/openstack/oslo.config)

<details><summary>README extract</summary>

The Oslo configuration API supports parsing command line arguments and
.ini style configuration files.

* License: Apache License, Version 2.0

</details>

### open-data-contract-standard

The Pydantic Model of the Open Data Contract Standard

`pip install open-data-contract-standard` · installs (wheel) · licence: MIT License · rank 4101 · last release 2026-09-02 · [PyPI](https://pypi.org/project/open-data-contract-standard/)

<details><summary>README extract</summary>

The pip module `open-data-contract-standard` to read and write YAML files using the Open Data Contract Standard. The pip module was extracted from the Data Contract CLI, which is its primary user.

The version number of the pip module corresponds to the version of the Open Data Contract Standard it supports. ...

Example:
```python
from open_data_contract_standard.model import OpenDataContractStandard

# Load a data contract specification from a file
data_contract = OpenDataContractStandard.from_file('path/to/your/data_contract.yaml')
# Print the data contract specification as a YAML string
print(data_contract.to_yaml())
```

Sections: Open Data Contract Standard (Python), Version Mapping, Usage

</details>

### omnibase-compat

Thin shared structural package for cross-repo enums, wire DTOs, event envelopes, primitives, and experimental schemas.

`pip install omnibase-compat` · installs (wheel) · licence: not stated · rank 4102 · last release 2026-09-03 · [PyPI](https://pypi.org/project/omnibase-compat/)

<details><summary>README extract</summary>

`omnibase_compat` is the thin shared structural package for cross-repo enums,
wire DTOs, event envelopes, concurrency helpers, and compatibility primitives.

It has zero OmniNode upstream runtime dependencies. Runtime dependencies are
limited to third-party structural support packages listed in `pyproject.toml`. ...

Features:
- Zero dependency on `omnibase_core`, `omnibase_spi`, or `omnibase_infra` (CI-enforced)
- Experimental artifact registry with lifecycle governance (`ticket` + `review_milestone` required) ...

Example:
```python
from omnibase_compat.enums.enum_message_category import EnumMessageCategory
from omnibase_compat.enums.enum_node_kind import EnumNodeKind
from omnibase_compat.models.event_envelope import EventEnvelopeV1Minimal
```

...

</details>

### objgraph

Draws Python object reference graphs with graphviz

`pip install objgraph` · installs (wheel) · licence: MIT · rank 4113 · last release 2026-10-16 · [PyPI](https://pypi.org/project/objgraph/) · [source](https://github.com/mgedmin/objgraph)

<details><summary>README extract</summary>

`objgraph` is a module that lets you visually explore Python object graphs.

You'll need graphviz if you want to draw
the pretty graphs.

I recommend xdot for interactive use.
`pip install xdot` should suffice; objgraph will automatically look for it
in your `PATH`.

Sections: Python Object Graphs, Changes, 3.7.0 (2026-10-16), 3.6.2 (2024-10-10), 3.6.1 (2024-02-26), 3.6.0 (2023-06-16), 3.5.0 (2020-10-11), 3.4.1 (2019-04-23), 3.4.0 (2018-02-13), 3.3.0 (2017-12-28), 3.2.0 (2017-12-20), 3.1.2 (2017-11-27), 3.1.1 (2017-10-30), 3.1.0 (2016-12-07)

</details>

### openinference-instrumentation-anthropic

OpenInference Anthropic Instrumentation

`pip install openinference-instrumentation-anthropic` · installs (wheel) · licence: Apache-2.0 · rank 4121 · last release 2026-11-05 · [PyPI](https://pypi.org/project/openinference-instrumentation-anthropic/)

<details><summary>README extract</summary>

Python autoinstrumentation library for the Anthropic package

This package implements the following Anthropic clients:
- `Messages` (`create`, `stream`, `parse`, `count_tokens`)
- `AsyncMessages`
- Beta `Messages` and `AsyncMessages`, including those of the Bedrock and Vertex AI clients ...

Example:
```python
import os
from anthropic import Anthropic
from openinference.instrumentation.anthropic import AnthropicInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

...
```

Sections: OpenInference Anthropic Instrumentation, Compatibility, Spans of the Anthropic SDK, Quickstart, More Info

</details>

### openinference-instrumentation-litellm

OpenInference liteLLM Instrumentation

`pip install openinference-instrumentation-litellm` · installs (wheel) · licence: Apache-2.0 · rank 4133 · last release 2026-11-05 · [PyPI](https://pypi.org/project/openinference-instrumentation-litellm/)

<details><summary>README extract</summary>

LiteLLM allows developers to call all LLM APIs using the openAI format. LiteLLM Proxy is a proxy server to call 100+ LLMs in OpenAI format. Both are supported by this auto-instrumentation.

This package implements OpenInference tracing for the following LiteLLM functions:
- completion()
- acompletion()
- completion_with_retries()
- embedding() ...

Example:
```python
import litellm
import phoenix as px

from openinference.instrumentation.litellm import LiteLLMInstrumentor

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
```

Sections: OpenInference LiteLLM Instrumentation, Quickstart, More Info

</details>

### openvino-telemetry

OpenVINO™ Telemetry package for sending statistics with user's consent, used in combination with other OpenVINO™ packages.

`pip install openvino-telemetry` · installs (wheel) · licence: Apache Software License · rank 4230 · last release 2025-07-07 · [PyPI](https://pypi.org/project/openvino-telemetry/)

<details><summary>README extract</summary>

The implementation of the Python 3 library to send the telemetry data from the OpenVINO™ toolkit components.

To send the data to Google Analytics, use the following three variables: `category`, `action`, and `label`.

- In the `category`, use only the name of the tool. ...

</details>

### oci-cli

Oracle Cloud Infrastructure CLI

`pip install oci-cli` · installs (wheel) · licence: Apache Software License; Universal Permissive License (UPL) · rank 4245 · last release 2026-11-03 · [PyPI](https://pypi.org/project/oci-cli/)

<details><summary>README extract</summary>

This is the command line interface for Oracle Cloud Infrastructure.

The project is open source and maintained by Oracle Corp. The home page for the project is here.


Example:
```python
powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('
```

Sections: Oracle Cloud Infrastructure CLI, About, Announcements, Interactive Features, Container Image, Mac OS X, Linux, Oracle Linux 7, Fedora Linux, Windows, Usage, Examples, Documentation, Help

</details>

### openvino

OpenVINO(TM) Runtime

`pip install openvino` · installs (wheel) · licence: Apache-2.0 · rank 4267 · last release 2026-10-01 · [PyPI](https://pypi.org/project/openvino/)

<details><summary>README extract</summary>

Documentation • Blog • Key Features • Tutorials • Integrations • Benchmarks • Generative AI

- Inference Optimization: Boost deep learning performance in computer vision, automatic speech recognition, generative AI, natural language processing with large and small language models, and many other common tasks. ...

Example:
```python
import openvino as ov
import torch
import torchvision

# load PyTorch model into memory
model = torch.hub.load("pytorch/vision", "shufflenet_v2_x1_0", weights="DEFAULT")

# convert the model into OpenVINO model
example = torch.randn(1, 3, 224, 224)
ov_model = ov.convert_model(model, example_input=(example,))

# compile the model for CPU device
...
```

...

</details>

### oslo.serialization

Oslo Serialization library

`pip install oslo.serialization` · installs (wheel) · licence: Apache-2.0 · rank 4268 · last release 2026-07-10 · [PyPI](https://pypi.org/project/oslo.serialization/) · [source](https://opendev.org/openstack/oslo.serialization)

<details><summary>README extract</summary>

The oslo.serialization library provides support for representing objects
in transmittable and storable formats, such as Base64, JSON and MessagePack.

* Free software: Apache license

</details>

### openhands-agent-server

OpenHands Agent Server - REST/WebSocket interface for OpenHands AI Agent

`pip install openhands-agent-server` · installs (wheel) · licence: not stated · rank 4287 · last release 2026-11-06 · [PyPI](https://pypi.org/project/openhands-agent-server/) · [docs](https://docs.openhands.dev/sdk) · [source](https://github.com/OpenHands/software-agent-sdk)

### openapi-generator-cli

CLI for openapi generator

`pip install openapi-generator-cli` · installs (wheel) · licence: Apache Software License · rank 4399 · last release 2026-11-03 · [PyPI](https://pypi.org/project/openapi-generator-cli/) · [docs](https://github.com/OpenAPITools/openapi-generator#3---usage) · [source](https://github.com/OpenAPITools/openapi-generator)

<details><summary>README extract</summary>

Sections: Further Documentation, Like the package?, Have suggestions or feedback?

</details>

### openinference-instrumentation-google-genai

OpenInference Google GenAI Instrumentation

`pip install openinference-instrumentation-google-genai` · installs (wheel) · licence: Apache-2.0 · rank 4586 · last release 2026-11-05 · [PyPI](https://pypi.org/project/openinference-instrumentation-google-genai/)

<details><summary>README extract</summary>

Python auto-instrumentation library for GenAI SDK. Traces are fully OpenTelemetry compatible and can be sent to any OpenTelemetry collector for viewing, such as Arize Phoenix or Arize AX.

Example:
```python
from openinference.instrumentation.google_genai import GoogleGenAIInstrumentor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

endpoint = "
tracer_provider = TracerProvider()
...
```

Sections: OpenInference Google GenAI Instrumentation, Quickstart, Progress, More Info

</details>

### opentelemetry-instrumentation-litellm

OpenTelemetry LiteLLM instrumentation

`pip install opentelemetry-instrumentation-litellm` · installs (wheel) · licence: Apache-2.0 · rank 4698 · last release 2026-11-05 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-litellm/) · [source](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-litellm)

<details><summary>README extract</summary>

This library allows tracing LLM prompts and completions sent with LiteLLM. Because LiteLLM normalizes every provider's reply into an OpenAI-style `ModelResponse` — including custom providers registered via `litellm.CustomLLM` — a single set of wrappers produces consistent `gen_ai.*` spans and metrics across all back-ends.

Example:
```python
from opentelemetry.instrumentation.litellm import LiteLLMInstrumentor

LiteLLMInstrumentor().instrument()
```

Sections: OpenTelemetry LiteLLM Instrumentation, Example usage, Privacy

</details>

### opentelemetry-resourcedetector-process

An OpenTelemetry package to populates Resource attributes from the running process

`pip install opentelemetry-resourcedetector-process` · installs (wheel) · licence: MIT License · rank 4699 · last release 2022-09-18 · [PyPI](https://pypi.org/project/opentelemetry-resourcedetector-process/)

<details><summary>README extract</summary>

An OpenTelemetry package to populates Resource attributes from the running process.

Example:
```python
from opentelemetry.sdk.resources import get_aggregated_resources
from opentelemetry_resourcedetector_process import ProcessResourceDetector

...

resource = get_aggregated_resources([
    ProcessResourceDetector(),
    SomeOtherResourceDetector()
])

... pass the returned `resource` to a TracerProvder, for example ...
```

Sections: opentelemetry-resourcedetector-process, Usage

</details>

### opentelemetry-container-distro

An OpenTelemetry distro which automatically discovers container attributes

`pip install opentelemetry-container-distro` · installs (wheel) · licence: MIT License · rank 4701 · last release 2022-09-18 · [PyPI](https://pypi.org/project/opentelemetry-container-distro/)

<details><summary>README extract</summary>

An OpenTelemetry distro which automatically discovers container attributes.

This distro expands the standard `opentelemetry-distro` to automatically bring in
additional resource detectors for container environments.

* opentelemetry-resourcedetector-docker
* opentelemetry-resourcedetector-kubernetes
* opentelemetry-resourcedetector-process ...

</details>

### openinference-instrumentation-agno

OpenInference Agno Instrumentation

`pip install openinference-instrumentation-agno` · installs (wheel) · licence: Apache-2.0 · rank 4806 · last release 2026-11-05 · [PyPI](https://pypi.org/project/openinference-instrumentation-agno/)

<details><summary>README extract</summary>

Python auto-instrumentation library for Agno Agents

The following instrumentation is fully OpenTelemetry-compatible and can be sent to an OpenTelemetry collector for monitoring, such as Arize Phoenix, Arize AX, or Langfuse.

Sections: OpenInference Agno Instrumentation, Quickstart, More Info

</details>

### openinference-instrumentation-google-adk

OpenInference Google ADK Instrumentation

`pip install openinference-instrumentation-google-adk` · installs (wheel) · licence: Apache-2.0 · rank 4930 · last release 2026-11-05 · [PyPI](https://pypi.org/project/openinference-instrumentation-google-adk/)

<details><summary>README extract</summary>

Python auto-instrumentation library for Google ADK.

The traces emitted by this instrumentation are fully OpenTelemetry compatible and can be sent to an OpenTelemetry collector for viewing, such as Arize Phoenix or Arize AX.

Example:
```python
import asyncio

from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.genai import types

from openinference.instrumentation.google_adk import GoogleADKInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
...
```

Sections: OpenInference Google ADK Instrumentation, Quickstart, More Info

</details>

### openapi-schema-pydantic

OpenAPI (v3) specification schema as pydantic class

`pip install openapi-schema-pydantic` · installs (wheel) · licence: MIT License · rank 5035 · last release 2022-06-29 · [PyPI](https://pypi.org/project/openapi-schema-pydantic/)

<details><summary>README extract</summary>

OpenAPI (v3) specification schema as Pydantic classes.

The naming of the classes follows the schema in
OpenAPI specification.

Example:
```python
from openapi_schema_pydantic import OpenAPI, Info, PathItem, Operation, Response

# Construct OpenAPI by pydantic objects
open_api = OpenAPI(
    info=Info(
        title="My own API",
        version="v0.0.1",
    ),
    paths={
        "/ping": PathItem(
            get=Operation(
                responses={
                    "200": Response(
...
```

Sections: openapi-schema-pydantic, Try me, Take advantage of Pydantic, Use Pydantic classes as schema, Notes, Use of OpenAPI.json() / OpenAPI.dict(), Non-pydantic schema types, Use OpenAPI 3.0.3 instead of 3.1.0

</details>

### opt-einsum-fx

Einsum optimization using opt_einsum and PyTorch FX

`pip install opt-einsum-fx` · installs (wheel) · licence: MIT License · rank 5055 · last release 2021-11-07 · [PyPI](https://pypi.org/project/opt-einsum-fx/)

<details><summary>README extract</summary>

Optimizing einsums and functions involving them using `opt_einsum` and PyTorch FX compute graphs.

Issues, questions, PRs, and any thoughts about further optimizing these kinds of operations are welcome!

For more information please see the docs.

Example:
```python
import torch
import torch.fx
import opt_einsum_fx

def einmatvecmul(a, b, vec):
    """Batched matrix-matrix-vector product using einsum"""
    return torch.einsum("zij,zjk,zk->zi", a, b, vec)

graph_mod = torch.fx.symbolic_trace(einmatvecmul)
print("Original code:\n", graph_mod.code)
graph_opt = opt_einsum_fx.optimize_einsums_full(
...
```

Sections: opt_einsum_fx, PyPI, Source, Minimal example

</details>

### openhands-aci

An Agent-Computer Interface (ACI) designed for software development agents OpenHands.

`pip install openhands-aci` · installs (wheel) · licence: MIT License · rank 5088 · last release 2026-02-27 · [PyPI](https://pypi.org/project/openhands-aci/)

<details><summary>README extract</summary>

> ⚠️ DEPRECATION NOTICE: This repository is now archived. The file editor tool has been migrated to the OpenHands Agent SDK under `openhands/tools/str_replace_editor`.

An Agent-Computer Interface (ACI) designed for software development agents OpenHands. ...

Features:
- Code Editor Interface: Sophisticated editing capabilities through the `editor` module
 - File creation and modification
 - Code editing
 - Configuration management ...

Sections: Agent-Computer Interface (ACI) for OpenHands, Features, Project Structure

</details>

### oss-harmony

Response format library for the gpt-oss open-weight model series (fork of openai-harmony)

`pip install oss-harmony` · installs (wheel) · licence: not stated · rank 5120 · last release 2026-10-29 · [PyPI](https://pypi.org/project/oss-harmony/)

<details><summary>README extract</summary>

Response format library for the gpt-oss open-weight model series (fork of openai-harmony)

The gpt-oss models were trained on the harmony response format for defining conversation structures, generating reasoning output and structuring function calls. ...

Example:
```python
from openai_harmony import (
    load_harmony_encoding,
    HarmonyEncodingName,
    Role,
    Message,
    Conversation,
    DeveloperContent,
    SystemContent,
)
enc = load_harmony_encoding(HarmonyEncodingName.HARMONY_GPT_OSS)
convo = Conversation.from_messages([
    Message.from_role_and_content(
        Role.SYSTEM,
...
```

Sections: Harmony, Using Harmony, Python, Example, Rust

</details>

### onnxmltools

Converts Machine Learning models to ONNX

`pip install onnxmltools` · installs (wheel) · licence: Apache-2.0 · rank 5149 · last release 2026-01-30 · [PyPI](https://pypi.org/project/onnxmltools/) · [source](https://github.com/onnx/onnxmltools)

<details><summary>README extract</summary>

<!--- SPDX-License-Identifier: Apache-2.0 -->

ONNXMLTools enables you to convert models from different machine learning toolkits into ONNX. Currently the following toolkits are supported: ...

Example:
```python
import onnxmltools
from keras.layers import Input, Dense, Add
from keras.models import Model

# N: batch size, C: sub-model input dimension, D: final model's input dimension
N, C, D = 2, 3, 3

# Define a sub-model, it will become a part of our final model
sub_input1 = Input(shape=(C,))
sub_mapped1 = Dense(D)(sub_input1)
...
```

Sections: Introduction, Dependencies, Examples, Keras to ONNX Conversion, CoreML to ONNX Conversion, H2O to ONNX Conversion, Test all existing converters, Add a new converter

</details>

### openhands-ai

OpenHands: Code Less, Make More

`pip install openhands-ai` · does not install on CPython 3.14 · licence: MIT · rank 5197 · last release 2026-07-09 · [PyPI](https://pypi.org/project/openhands-ai/) · [source](https://github.com/OpenHands/OpenHands)

<details><summary>README extract</summary>

The self-hosted developer control center for coding agents and automations.

 Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends.

 Quickstart |
 Docs |
 Self-Hosting |
 ACP Agents |
 Automations |
 Slack ...

Sections: Quickstart, Option 1: Without a Sandbox, Option 2: With a Docker Sandbox, Option 3: From Source, Architecture, More documentation

</details>

### oai-statsig-python-core

Statsig Python bindings for the Statsig Core SDK.

`pip install oai-statsig-python-core` · installs (wheel) · licence: ISC · rank 5352 · last release 2026-11-05 · [PyPI](https://pypi.org/project/oai-statsig-python-core/) · [docs](https://docs.statsig.com/server-core/python-core) · [source](https://github.com/statsig-io/statsig-server-core/tree/main/statsig-pyo3)

<details><summary>README extract</summary>

Statsig

Statsig helps you move faster with feature gates (feature flags), and/or dynamic configs. It also allows you to run A/B/n tests to validate your new features and understand their impact on your KPIs. If you're new to Statsig, check out our product and create an account at statsig.com.

Example:
```python
def is_read_only(self) -> bool:
    return not self.is_leader
```

Sections: Getting Started, ID-list file routing and fallback, Read-only data stores, Remote SDK telemetry control, Packages

</details>

### oslo.context

Oslo Context library

`pip install oslo.context` · installs (wheel) · licence: Apache-2.0 · rank 5354 · last release 2026-07-10 · [PyPI](https://pypi.org/project/oslo.context/) · [source](https://opendev.org/openstack/oslo.context)

<details><summary>README extract</summary>

The oslo.context library has helpers to maintain useful information
about a request context. The request context is usually populated in
the WSGI pipeline and used by various modules such as logging.

* License: Apache License, Version 2.0

</details>

### oslo.log

oslo.log library

`pip install oslo.log` · installs (wheel) · licence: Apache-2.0 · rank 5388 · last release 2026-09-10 · [PyPI](https://pypi.org/project/oslo.log/) · [source](https://opendev.org/openstack/oslo.log)

<details><summary>README extract</summary>

The oslo.log (logging) configuration library provides standardized
configuration for all openstack projects. It also provides custom
formatters, handlers and support for context specific
logging (like resource id's etc).

* Free software: Apache license

</details>

### oslex

OS-independent wrapper for shlex and mslex

`pip install oslex` · installs (wheel) · licence: MIT License · rank 5439 · last release 2026-05-10 · [PyPI](https://pypi.org/project/oslex/)

<details><summary>README extract</summary>

`oslex` is an OS-independent wrapper for `shlex` and `mslex`.

Its main purpose is to provide functions similar in functionality to `shlex.quote()`, `shlex.split()` and `shlex.join()` on both Windows and POSIX-compatible platforms. ...

Sections: oslex, Reference, `oslex.join()`, `oslex.quote()`, `oslex.split()`, `oslex.join_ms()`, `oslex.quote_ms()`, `oslex.split_ms()`, `oslex.join_sh()`, `oslex.quote_sh()`, `oslex.split_sh()`, Licensing

</details>

### opensearch-dsl

Python client for OpenSearch

`pip install opensearch-dsl` · installs (wheel) · licence: Apache Software License · rank 5444 · last release 2023-03-21 · [PyPI](https://pypi.org/project/opensearch-dsl/)

<details><summary>README extract</summary>

> Warning
>The OpenSearch high-level Python client (opensearch-dsl-py) will be deprecated after version 2.1.0. We recommend switching to the OpenSearch Python client (opensearch-py), which now includes the functionality of opensearch-dsl-py.

OpenSearch DSL Python Client

- Welcome!
- Getting Started
- Compatibility with OpenSearch ...

Sections: Welcome!, Getting Started, Compatibility with OpenSearch, Project Resources, Copyright

</details>

### odxtools

Utilities to work with the ODX standard for automotive diagnostics

`pip install odxtools` · installs (wheel) · licence: MIT License · rank 5583 · last release 2026-10-20 · [PyPI](https://pypi.org/project/odxtools/) · [source](https://github.com/mercedes-benz/odxtools)

<details><summary>README extract</summary>

<!-- SPDX-License-Identifier: MIT -->

`odxtools` is a set of utilities for working with diagnostic
descriptions of automotive electronic control units using the data
model and the associated technologies of the ODX standard. ...

Example:
```python
import odxtools

db = odxtools.load_pdx_file("somersault.pdx")
```

Sections: odxtools, Use Cases, Usage Examples, Python snippets, Using the non-strict mode, Interactive Usage, Python REPL, Command line usage, Generic parameters, The `list` subcommand, The `browse` subcommand, The `snoop` subcommand, The `find` subcommand, The `decode` subcommand

</details>

### omninode-memory

OmniNode memory primitives — models, protocols, and storage adapters for Qdrant, Memgraph, and PostgreSQL backends.

`pip install omninode-memory` · does not install on CPython 3.14 · licence: MIT · rank 5586 · last release 2026-11-08 · [PyPI](https://pypi.org/project/omninode-memory/) · [docs](https://github.com/OmniNode-ai/knowledge_base) · [source](https://github.com/OmniNode-ai/omnimemory)

<details><summary>README extract</summary>

OmniMemory provides document ingestion, semantic retrieval, and storage primitives for OmniNode.
Documentation: public knowledge base.

</details>

### opentelemetry-test-utils

Test utilities for OpenTelemetry unit tests

`pip install opentelemetry-test-utils` · installs (wheel) · licence: Apache-2.0 · rank 5620 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-test-utils/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This package provides internal testing utilities for the OpenTelemetry Python project and provides no stability or quality guarantees.
Please do not use it for anything other than writing or running tests for the OpenTelemetry Python project (github.com/open-telemetry/opentelemetry-python).

* OpenTelemetry Project

Sections: OpenTelemetry Test Utilities, References

</details>

### osc-lib

OpenStackClient Library

`pip install osc-lib` · installs (wheel) · licence: Apache-2.0 · rank 5648 · last release 2026-07-10 · [PyPI](https://pypi.org/project/osc-lib/) · [source](https://opendev.org/openstack/osc-lib/)

<details><summary>README extract</summary>

OpenStackClient (aka OSC) is a command-line client for OpenStack. osc-lib
is a package of common support modules for writing OSC plugins.

* PyPi - package installation
* Online Documentation
* Launchpad project - part of OpenStackClient
* Bugs - issue tracking
* Source
* `Developer` - getting started as a developer
* `Contributing` - contributing ...

Sections: osc-lib, Getting Started, Transition From OpenStackclient

</details>

### onecache

Python cache for sync and async code

`pip install onecache` · installs (wheel) · licence: MIT · rank 5673 · last release 2026-10-12 · [PyPI](https://pypi.org/project/onecache/)

<details><summary>README extract</summary>

Python cache for sync and async code.

Cache uses an LRU algorithm and can optionally set TTLs per entry.

On CPython the cache core is a compiled Cython extension (prebuilt wheels for Linux, macOS and Windows on x86_64 and ARM64). On PyPy, or on platforms without a prebuilt wheel, it falls back to an equivalent pure Python implementation. ...

Example:
```python
from onecache import CacheDecorator
from onecache import AsyncCacheDecorator

class Counter:
    def init(self, count=0):
        self.count = count

@pytest.mark.asyncio
async def test_async_cache_counter():
    """Test async cache, counter case."""
    counter = Counter()

    @AsyncCacheDecorator()
    async def mycoro(counter: Counter):
...
```

Sections: OneCache, Usage, Performance, Releasing

</details>

### opentelemetry-instrumentation-pymssql

OpenTelemetry pymssql instrumentation

`pip install opentelemetry-instrumentation-pymssql` · installs (wheel) · licence: Apache-2.0 · rank 5817 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-pymssql/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry pymssql Instrumentation, References

</details>

### opentelemetry-instrumentation-exceptions

OpenTelemetry unhandled exceptions instrumentation

`pip install opentelemetry-instrumentation-exceptions` · installs (wheel) · licence: Apache-2.0 · rank 5821 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-exceptions/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Example:
```python
from opentelemetry.instrumentation.exceptions import (
    UnhandledExceptionInstrumentor,
)

UnhandledExceptionInstrumentor().instrument()
```

Sections: OpenTelemetry unhandled exceptions instrumentation, Usage, References

</details>

### opentelemetry-exporter-prometheus-remote-write

Prometheus Remote Write Metrics Exporter for OpenTelemetry

`pip install opentelemetry-exporter-prometheus-remote-write` · installs (wheel) · licence: Apache-2.0 · rank 5828 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-exporter-prometheus-remote-write/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This package contains an exporter to send metrics from the OpenTelemetry Python SDK directly to a Prometheus Remote Write integrated backend
(such as Cortex or Thanos) without having to run an instance of the Prometheus server.

Sections: OpenTelemetry Prometheus Remote Write Exporter, References

</details>

### opentelemetry-instrumentation-asyncclick

Async Click instrumentation for OpenTelemetry

`pip install opentelemetry-instrumentation-asyncclick` · installs (wheel) · licence: Apache-2.0 · rank 5892 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-asyncclick/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library allows tracing requests made by the asyncclick fork of the click library.

Sections: OpenTelemetry asyncclick Instrumentation, References

</details>

### ops

The Python library behind great charms

`pip install ops` · installs (wheel) · licence: Apache-2.0 · rank 5903 · last release 2026-10-08 · [PyPI](https://pypi.org/project/ops/) · [docs](https://canonical.com/juju/docs/ops/latest/) · [source](https://github.com/canonical/operator)

<details><summary>README extract</summary>

The `ops` library is a Python framework for developing and testing Kubernetes and machine charms. While charms can be written in any language, `ops` defines the latest standard, and charmers are encouraged to use Python with `ops` for all charms. The library is an official component of the Charm SDK, itself a part of the Juju universe. ...

Example:
```python
import ops

class OpsExampleCharm(ops.CharmBase):
    """Charm the service."""

    def init(self, *args):
        super().init(*args)
        self.framework.observe(self.on['httpbin'].pebble_ready, self._on_httpbin_pebble_ready)
        self.framework.observe(self.on.config_changed, self._on_config_changed)

...
```

Sections: The `ops` library, Give it a try, Set up, Write your charm, Clean up, Next steps

</details>

### openinference-instrumentation-pydantic-ai

OpenInference PydanticAI Instrumentation

`pip install openinference-instrumentation-pydantic-ai` · installs (wheel) · licence: Apache-2.0 · rank 5919 · last release 2026-11-04 · [PyPI](https://pypi.org/project/openinference-instrumentation-pydantic-ai/)

<details><summary>README extract</summary>

Python auto-instrumentation library for PydanticAI. These traces are fully OpenTelemetry compatible and can be sent to an OpenTelemetry collector for viewing, such as Arize Phoenix or Arize AX.

Example:
```python
import os
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.instrumented import InstrumentationSettings
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from opentelemetry import trace
...
```

Sections: OpenInference PydanticAI, Quickstart, More Info

</details>

### openfeature-provider-flagd

OpenFeature provider for the flagd flag evaluation engine

`pip install openfeature-provider-flagd` · installs (wheel) · licence: Apache-2.0 · rank 5933 · last release 2026-10-22 · [PyPI](https://pypi.org/project/openfeature-provider-flagd/)

<details><summary>README extract</summary>

This provider is designed to use flagd's evaluation protocol, or locally evaluate flags defined in a flagd flag definition via the OpenFeature Python SDK.

Example:
```python
from openfeature import api
from openfeature.contrib.provider.flagd import FlagdProvider

api.set_provider(FlagdProvider())
```

Sections: flagd Provider for OpenFeature, Configuration and Usage, Remote resolver (RPC), In-process resolver, Sync-metadata, File mode, Configuration options, Custom channel credentials, Selector Handling (In-Process Mode Only), Current Implementation, Backward Compatibility, Reconnection, Deadlines, Deadlines with Remote resolver (RPC)

</details>

### openai-chatkit

A ChatKit backend SDK.

`pip install openai-chatkit` · installs (wheel) · licence: not stated · rank 5943 · last release 2026-05-19 · [PyPI](https://pypi.org/project/openai-chatkit/)

### oso-cloud

Oso Cloud Python client

`pip install oso-cloud` · installs (wheel) · licence: Apache-2.0 · rank 6008 · last release 2026-03-30 · [PyPI](https://pypi.org/project/oso-cloud/) · [docs](https://www.osohq.com/docs)

<details><summary>README extract</summary>

[][badge-slack-link]

The Oso Cloud client for Python provides a convenient wrapper around the Oso
Cloud HTTP API for applications and services written in Python.

Oso Cloud is authorization-as-a-service. ...

Sections: Oso Cloud Client for Python, What is Oso Cloud?, Documentation

</details>

### okta-jwt-verifier

A Python library for OKTA JWT tokens validation

`pip install okta-jwt-verifier` · installs (wheel) · licence: Apache Software License · rank 6097 · last release 2026-05-12 · [PyPI](https://pypi.org/project/okta-jwt-verifier/)

<details><summary>README extract</summary>

[](

- Release Status
- Need help?
- Getting Started
- Usage Guide
- Exceptions
- Contributing

This library helps you verify tokens that have been issued by Okta. To learn more about verification cases and Okta's tokens please read Working With OAuth 2.0 Tokens

> Requires Python version 3.6.0 or higher.

Example:
```python
import asyncio

from okta_jwt_verifier import BaseJWTVerifier

async def main():
    jwt_verifier = BaseJWTVerifier(issuer='{ISSUER}', audience='api://default')
    await jwt_verifier.verify_access_token('{JWT}')
    print('Token validated successfully.')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

Sections: Okta JWT Verifier for Python, Need help?, Getting started, Usage guide, Exceptions

</details>

### omnibase_infra

ONEX Infrastructure - Service integration and database infrastructure tools

`pip install omnibase_infra` · installs (wheel) · licence: MIT · rank 6135 · last release 2026-10-23 · [PyPI](https://pypi.org/project/omnibase_infra/)

<details><summary>README extract</summary>

omnibase_infra provides ONEX infrastructure implementations, service integrations, and runtime tooling.

Documentation: knowledge_base.

</details>

### openfeature-provider-flagsmith

Openfeature provider for Flagsmith

`pip install openfeature-provider-flagsmith` · installs (wheel) · licence: not stated · rank 6143 · last release 2026-08-07 · [PyPI](https://pypi.org/project/openfeature-provider-flagsmith/)

<details><summary>README extract</summary>

The Flagsmith provider allows you to connect to your Flagsmith instance through the OpenFeature SDK

Example:
```python
from flagsmith import Flagsmith
from openfeature_flagsmith.provider import FlagsmithProvider

provider = FlagsmithProvider(
    # Provide an instance of the Flagsmith python client.
    # Required: True
    client=Flagsmith(...),

    # By enabling the use_flagsmith_defaults setting, you can instruct the OpenFeature SDK to use
...
```

Sections: flagsmith-openfeature-provider-python, Python SDK usage, Using the Flagsmith Provider with the OpenFeature SDK, Tracking and experimentation, Recording exposures, Custom events, Caveats, Evaluation Context

</details>

### openai-clip

(no summary)

`pip install openai-clip` · installs from source (sdist only) · licence: not stated · rank 6199 · last release 2022-07-19 · [PyPI](https://pypi.org/project/openai-clip/)

### onyx-devtools

Developer utilities for working on onyx.app

`pip install onyx-devtools` · installs (wheel) · licence: MIT License · rank 6216 · last release 2026-10-28 · [PyPI](https://pypi.org/project/onyx-devtools/) · [source](https://github.com/onyx-dot-app/onyx)

<details><summary>README extract</summary>

Sections: Prerequisites, zsh, bash, Commands, `compose` - Launch Docker Containers, `logs` - View Docker Container Logs, `pull` - Pull Docker Images, `backend` - Run Backend Services, `stack` - Run the Local Dev Stack of a Worktree, `web` - Run Frontend Scripts, `test` - Run Go tests, `coverage` - Measure Go Coverage Against a Baseline, Comparing against the base, Raising the baseline

</details>

### openinference-instrumentation-llama-index

OpenInference LlamaIndex Instrumentation

`pip install openinference-instrumentation-llama-index` · installs (wheel) · licence: Apache-2.0 · rank 6223 · last release 2026-11-05 · [PyPI](https://pypi.org/project/openinference-instrumentation-llama-index/)

<details><summary>README extract</summary>

Python auto-instrumentation library for LlamaIndex.

These traces are fully OpenTelemetry compatible and can be sent to an OpenTelemetry collector for viewing, such as Arize Phoenix or Arize AX.

Example:
```python
from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

endpoint = "
tracer_provider = trace_sdk.TracerProvider()
...
```

Sections: OpenInference LlamaIndex Instrumentation, Compatibility, Quickstart, More Info

</details>

### ovld

Overloading Python functions

`pip install ovld` · installs (wheel) · licence: MIT · rank 6239 · last release 2026-09-19 · [PyPI](https://pypi.org/project/ovld/) · [docs](https://ovld.readthedocs.io/en/latest/) · [source](https://github.com/breuleux/ovld)

<details><summary>README extract</summary>

Fast multiple dispatch in Python, with many extra features.

📋 Documentation

With ovld, you can write a version of the same function for every type signature using annotations instead of writing an awkward sequence of `isinstance` statements. Unlike Python's `singledispatch`, it works for multiple arguments. ...

Example:
```python
from ovld import ovld
from ovld.dependent import Regexp
from typing import Literal

@ovld
def f(x: str):
    return f"The string {x!r}"

@ovld
def f(x: int):
    return f"The number {x}"

@ovld
def f(x: int, y: int):
    return "Two numbers!"

@ovld
def f(x: Literal[0]):
    return "zero"

@ovld
def f(x: Regexp[r"^X"]):
...
```

...

</details>

### oauth2

library for OAuth version 1.9

`pip install oauth2` · installs (wheel) · licence: MIT License · rank 6287 · last release 2015-09-12 · [PyPI](https://pypi.org/project/oauth2/)

### OpenMM

Python wrapper for OpenMM (a C++ MD package)

`pip install OpenMM` · installs (wheel) · licence: Python Software Foundation License (BSD-like) · rank 6354 · last release 2026-09-24 · [PyPI](https://pypi.org/project/OpenMM/)

<details><summary>README extract</summary>

OpenMM is a toolkit for molecular simulation. It can be used either as a
 stand-alone application for running simulations, or as a library you call
 from your own code. It provides a combination of extreme flexibility
 (through custom forces and integrators), openness, and high performance
 (especially on recent GPUs) that make it truly unique ...

</details>

### openinference-instrumentation-haystack

OpenInference Haystack Instrumentation

`pip install openinference-instrumentation-haystack` · installs (wheel) · licence: Apache-2.0 · rank 6386 · last release 2026-11-04 · [PyPI](https://pypi.org/project/openinference-instrumentation-haystack/)

<details><summary>README extract</summary>

Python auto-instrumentation library for LLM applications implemented with Haystack.

Haystack Pipelines and Components (ex. PromptBuilder, OpenAIGenerator, etc.) are fully OpenTelemetry-compatible and can be sent to an OpenTelemetry collector for monitoring, such as Arize Phoenix or Arize AX.

Example:
```python
from openinference.instrumentation.haystack import HaystackInstrumentor
from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
import os

# Set your OpenAI API key
...
```

Sections: OpenInference Haystack Instrumentation, Quickstart, More Info

</details>

### optimizely-sdk

Python SDK for Optimizely Feature Experimentation, Optimizely Full Stack (legacy), and Optimizely Rollouts.

`pip install optimizely-sdk` · installs (wheel) · licence: Apache Software License · rank 6412 · last release 2026-11-02 · [PyPI](https://pypi.org/project/optimizely-sdk/)

<details><summary>README extract</summary>

Optimizely Feature Experimentation is A/B testing and feature management for product development teams. Experiment in any application. Make every feature on your roadmap an opportunity to learn. Learn more at or see our documentation at # Optimizely Python SDK ...

Features:
To access the Feature Management configuration in the Optimizely
dashboard, please contact your Optimizely customer success manager.

Example:
```python
notification_center.add_notification_listener(NotificationTypes.OPTIMIZELY_CONFIG_UPDATE, update_callback)
```

...

</details>

### ocsf-lib

Tools for working with the OCSF schema

`pip install ocsf-lib` · installs (wheel) · licence: Apache Software License · rank 6471 · last release 2025-07-07 · [PyPI](https://pypi.org/project/ocsf-lib/)

<details><summary>README extract</summary>

Tools for building Python scripts and applications leveraging the OCSF.

Example:
```python
schema = get_schema("1.1.0")
schema = get_schema("./1.3.0-dev.json")
schema = get_schema("path/to/ocsf-schema")
```

Sections: OCSF Library for Python, Quick Start, About, ocsf.util: The utilities package, ocsf.schema: The Schema Package, ocsf.repository: The Repository Package, ocsf.compile: An OCSF Compiler, ocsf.api: The API Package, ocsf.compare: The Compare Package, ocsf.validate.framework: The Validation Framework Package, Getting Started, PyPI, From Source, Type Checking

</details>

### opack2

Python library for parsing the opack format

`pip install opack2` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6562 · last release 2026-10-28 · [PyPI](https://pypi.org/project/opack2/)

_README extract left out: share-alike licence._

### openupgradelib

A library with support functions to be called from Odoo migration scripts.

`pip install openupgradelib` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 6630 · last release 2026-08-25 · [PyPI](https://pypi.org/project/openupgradelib/)

_README extract left out: share-alike licence._

### openfeature-flagd-core

OpenFeature flagd evaluator core implementation

`pip install openfeature-flagd-core` · installs (wheel) · licence: Apache Software License · rank 6655 · last release 2026-10-15 · [PyPI](https://pypi.org/project/openfeature-flagd-core/)

<details><summary>README extract</summary>

Reference implementation of the flagd evaluator -- flag parsing, targeting rules (JSON logic), and custom operators (fractional, sem_ver, starts_with, ends_with). Mirrors the Java `flagd-core` module.

It is part of the OpenFeature Python SDK contrib project.

Example:
```python
from openfeature.contrib.tools.flagd.core import FlagdCore

core = FlagdCore()
core.set_flags(
    '{"flags": {"my-flag": {"state": "ENABLED", "variants": {"on": true}, "defaultVariant": "on"}}}'
)
result = core.resolve_boolean_value("my-flag", False)
```

Sections: OpenFeature flagd Core, Usage

</details>

### openfeature-flagd-api

OpenFeature flagd evaluator API definition

`pip install openfeature-flagd-api` · installs (wheel) · licence: Apache Software License · rank 6664 · last release 2026-04-30 · [PyPI](https://pypi.org/project/openfeature-flagd-api/)

<details><summary>README extract</summary>

This package defines the pure API/contract (Python Protocol) for the flagd evaluator, allowing others to provide their own evaluator implementations.

It is part of the OpenFeature Python SDK contrib project and mirrors the Java `flagd-api` module.

Example:
```python
from openfeature.contrib.tools.flagd.api import Evaluator, FlagStoreException
```

Sections: OpenFeature flagd Evaluator API, Usage

</details>

### oslo.concurrency

Oslo Concurrency library

`pip install oslo.concurrency` · installs (wheel) · licence: Apache-2.0 · rank 6691 · last release 2026-07-16 · [PyPI](https://pypi.org/project/oslo.concurrency/) · [source](https://opendev.org/openstack/oslo.concurrency)

<details><summary>README extract</summary>

The oslo.concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

* Free software: Apache license

</details>

### openpyxl-stubs

Type stubs for openpyxl

`pip install openpyxl-stubs` · installs (wheel) · licence: MIT license · rank 6710 · last release 2023-01-12 · [PyPI](https://pypi.org/project/openpyxl-stubs/)

<details><summary>README extract</summary>

Add types for openpyxl for mypy.

Example:
```python
from typing import Optional
from flask_httpauth import HTTPAuth, Authorization

def foo(bar: HTTPAuth) -> Optional[Authorization]:
    return bar.get_auth()
```

Sections: openpyxl-stubs, Usage

</details>

### openlit

OpenTelemetry-native Auto instrumentation library for monitoring LLM Applications and GPUs, facilitating the integration of observability into your GenAI-driven projects

`pip install openlit` · installs (wheel) · licence: Apache Software License · rank 6713 · last release 2026-08-03 · [PyPI](https://pypi.org/project/openlit/) · [source](https://github.com/openlit/openlit/tree/main/openlit/python)

<details><summary>README extract</summary>

Documentation | Quickstart | Roadmap | Feature Request | Report a Bug

OpenLIT SDK is a monitoring framework built on top of OpenTelemetry that gives your complete Observability for your AI stack, from LLMs to vector databases and GPUs, with just one line of code with tracing and metrics. ...

Example:
```python
import openlit

openlit.init(
  otlp_endpoint="YOUR_OTEL_ENDPOINT",
  otlp_headers ="YOUR_OTEL_ENDPOINT_AUTH"
)
```

...

</details>

### openwakeword

An open-source audio wake word (or phrase) detection framework with a focus on performance and simplicity

`pip install openwakeword` · installs (wheel) · licence: Apache Software License · rank 6746 · last release 2024-02-11 · [PyPI](https://pypi.org/project/openwakeword/)

<details><summary>README extract</summary>

openWakeWord is an open-source wakeword library that can be used to create voice-enabled applications and interfaces. It includes pre-trained models for common words & phrases that work well in real-world environments.

Quick Links
- Installation
- Training New Models
- FAQ

2024/02/11
- v0.6.0 of openWakeWord released. ...

Example:
```python
import openwakeword
from openwakeword.model import Model

# One-time download of all pre-trained models (or only select models)
openwakeword.utils.download_models()

# Instantiate the model(s)
model = Model(
    wakeword_models=["path/to/model.tflite"],  # can also leave this argument empty to load all of the included pre-trained models
)

...
```

...

</details>

### opentelemetry-exporter-jaeger-thrift

Jaeger Thrift Exporter for OpenTelemetry

`pip install opentelemetry-exporter-jaeger-thrift` · installs (wheel) · licence: Apache Software License · rank 6747 · last release 2023-11-07 · [PyPI](https://pypi.org/project/opentelemetry-exporter-jaeger-thrift/)

<details><summary>README extract</summary>

This library allows to export tracing data to Jaeger using Thrift.

Sections: OpenTelemetry Jaeger Thrift Exporter, Configuration, References

</details>

### office365

A wrapper around O365 offering subclasses with additional utility methods.

`pip install office365` · installs (wheel) · licence: MIT · rank 6754 · last release 2020-12-15 · [PyPI](https://pypi.org/project/office365/)

<details><summary>README extract</summary>

This library is currently still under development. The API will likely undergo significant changes that may break any code you write with it.
The documentation will fall out of sync with the updates regularly until development slows down. Use it at your own risk.

Features:
A wrapper around the incredible O365 library ( for using Outlook and People services (for now). Provides a config class for handling credentials and persisting them to the drive, a query interface similar to SQLAlchemy, and subclasses of many O365 ...

Sections: PLEASE NOTE, Overview, Usage

</details>

### openfeature-provider-ofrep

OpenFeature provider for the OpenFeature Remote Evaluation Protocol (OFREP)

`pip install openfeature-provider-ofrep` · installs (wheel) · licence: Apache-2.0 · rank 6765 · last release 2026-05-07 · [PyPI](https://pypi.org/project/openfeature-provider-ofrep/)

<details><summary>README extract</summary>

This provider is designed to use the OpenFeature Remote Evaluation Protocol (OFREP).

Example:
```python
from openfeature import api
from openfeature.contrib.provider.ofrep import OFREPProvider

api.set_provider(OFREPProvider())
```

Sections: OFREP Provider for OpenFeature, Configuration and Usage, Configuration options

</details>

### opentelemetry-contrib-instrumentations

OpenTelemetry Contrib Instrumentation Packages

`pip install opentelemetry-contrib-instrumentations` · installs (wheel) · licence: Apache-2.0 · rank 6830 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-contrib-instrumentations/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry Instrumentation, References

</details>

### onyx-devtools-audit

Vulnerability auditor for onyx-devtools

`pip install onyx-devtools-audit` · installs (wheel) · licence: MIT License · rank 6854 · last release 2026-10-28 · [PyPI](https://pypi.org/project/onyx-devtools-audit/) · [source](https://github.com/onyx-dot-app/onyx)

<details><summary>README extract</summary>

`ods-audit` is the vulnerability auditor of `ods`, the
onyx.app devtools utility script.

It scans lockfiles, container images, open Dependabot alerts, and the GitHub
Actions pinned in `.github` against OSV.dev, and it gates
deploys on the result.

It ships as its own wheel because its scanner is about 50 MB, most of the size
of a combined binary. ...

</details>

### openhands-workspace

OpenHands Workspace - Docker and container-based workspace implementations

`pip install openhands-workspace` · installs (wheel) · licence: not stated · rank 6878 · last release 2026-11-06 · [PyPI](https://pypi.org/project/openhands-workspace/) · [docs](https://docs.openhands.dev/sdk) · [source](https://github.com/OpenHands/software-agent-sdk)

### opencensus-ext-logging

OpenCensus logging Integration

`pip install opencensus-ext-logging` · installs (wheel) · licence: Apache Software License · rank 6911 · last release 2021-10-05 · [PyPI](https://pypi.org/project/opencensus-ext-logging/)

<details><summary>README extract</summary>

The logging integration enriches the log records with trace ID, span ID and sampling flag.
The following attributes will be added to `LogRecord`:

 * traceId
 * spanId
 * traceSampled

Note that this only takes effect for loggers created after the integration.

Example:
```python
import logging

from opencensus.trace import config_integration
from opencensus.trace.samplers import AlwaysOnSampler
from opencensus.trace.tracer import Tracer

config_integration.trace_integrations(['logging'])
logging.basicConfig(format='%(asctime)s traceId=%(traceId)s spanId=%(spanId)s %(message)s')
tracer = Tracer(sampler=AlwaysOnSampler())

...
```

Sections: OpenCensus logging Integration, Usage, References

</details>

### openinference-instrumentation-bedrock

OpenInference Bedrock Instrumentation

`pip install openinference-instrumentation-bedrock` · installs (wheel) · licence: Apache-2.0 · rank 6920 · last release 2026-11-04 · [PyPI](https://pypi.org/project/openinference-instrumentation-bedrock/)

<details><summary>README extract</summary>

Python autoinstrumentation library for AWS Bedrock calls made using `boto3` (sync) and `aioboto3` (async).

This package implements OpenInference tracing for `invoke_model`, `invoke_agent` and `converse` calls made using the `bedrock-runtime` and `bedrock-agent-runtime` clients from both `boto3` (sync) and `aioboto3` (async). ...

Example:
```python
session = boto3.session.Session()
client = session.client("bedrock-runtime")
prompt = b'{"prompt": "Human: Hello there, how are you? Assistant:", "max_tokens_to_sample": 1024}'
response = client.invoke_model(modelId="anthropic.claude-v2", body=prompt)
response_body = json.loads(response.get("body").read())
print(response_body["completion"])
```

...

</details>

### openseespy

OpenSeesPy — Python interpreter for OpenSees

`pip install openseespy` · installs (wheel) · licence: LICENSE.md · rank 6954 · last release 2026-03-18 · [PyPI](https://pypi.org/project/openseespy/)

<details><summary>README extract</summary>

Pip package for OpenSeesPy — the Python interpreter for OpenSees.

This is a meta-package that automatically installs the correct platform-specific
package for your operating system.

Example:
```python
import openseespy.opensees as ops
```

Sections: OpenSeesPy, Import, Upgrade, Documentation, Issues

</details>

### okonomiyaki

Self-contained library to deal with metadata in Enthought-specific egg and runtime archives

`pip install okonomiyaki` · installs (wheel) · licence: BSD-3-Clause · rank 6991 · last release 2025-02-14 · [PyPI](https://pypi.org/project/okonomiyaki/)

<details><summary>README extract</summary>

Okonomiyaki is an experimental library aimed at consolidating a lot of our
low-level code used for Enthought's eggs.

The library contains code for the following:

* producing EDM and enpkg-compatible egg from a tree + metadata
* object models for eggs metadata, as well as versions and platform
 representations ...

Example:
```python
from okonomiyaki.versions import EnpkgVersion
# Every Version class has a from_string constructor
v1 = EnpkgVersion.from_string("1.3.3-1")
v2 = EnpkgVersion.from_string("1.3.2-3")

assert v1 > v2
```

Sections: Note, Examples, Version parsing, Platform parsing, Egg metadata, 2025-02-13 3.0.0, 2024-08-23 2.0.0, 2023-06-29 1.4.0, 2021-07-01 1.3.2, 2021-06-29 1.3.1, 2021-03-21 1.3.0, 2019-11-08 1.2.0, 2019-09-20 1.1.1, 2019-09-19 1.1.0

</details>

### openseespylinux

A OpenSeesPy Linux package

`pip install openseespylinux` · installs (wheel) · licence: LICENSE.md · rank 7018 · last release 2026-03-18 · [PyPI](https://pypi.org/project/openseespylinux/)

<details><summary>README extract</summary>

Pip Package for OpenSeesPy Linux

Example:
```python
import openseespylinux as ops
```

Sections: OpenSeesPy Linux, Import, Documentation, Issues

</details>

### opentelemetry-python-contrib-external-valkey

OpenTelemetry Valkey instrumentation

`pip install opentelemetry-python-contrib-external-valkey` · installs (wheel) · licence: Apache-2.0 · rank 7103 · last release 2026-10-07 · [PyPI](https://pypi.org/project/opentelemetry-python-contrib-external-valkey/)

<details><summary>README extract</summary>

OpenTelemetry instrumentation for the Valkey Python Client.

Features:
`opentelemetry-instrumentation-redis` instruments the `redis` module and has multiple `isinstance` checks for classes from it. Since the Valkey Python Client is a fork of the Redis Python Client, any instrumentation through ...

Example:
```python
from opentelemetry.instrumentation.valkey import ValkeyInstrumentor

ValkeyInstrumentor().instrument()
```

Sections: opentelemetry-python-contrib-external-valkey, How do I use it?, Why is this needed?, How does it work?

</details>

### openequivariance

A fast GPU JIT kernel generator for the Clebsch-Gordon Tensor Product

`pip install openequivariance` · installs from source (sdist only) · licence: BSD-3-Clause · rank 7130 · last release 2026-11-01 · [PyPI](https://pypi.org/project/openequivariance/) · [source](https://github.com/PASSIONLab/OpenEquivariance)

<details><summary>README extract</summary>

[[PyTorch Examples]](#pytorch-examples)
[[JAX Examples]](#jax-examples)
[[Citation and Acknowledgements]](#citation-and-acknowledgements)

OpenEquivariance is a CUDA and HIP kernel generator for the Clebsch-Gordon tensor product,
a key kernel in rotation-equivariant deep neural networks. ...

Example:
```python
import torch
import e3nn.o3 as o3

gen = torch.Generator(device='cuda')

batch_size = 1000
X_ir, Y_ir, Z_ir = o3.Irreps("1x2e"), o3.Irreps("1x3e"), o3.Irreps("1x2e")
X = torch.rand(batch_size, X_ir.dim, device='cuda', generator=gen)
Y = torch.rand(batch_size, Y_ir.dim, device='cuda', generator=gen)

instructions=[(0, 0, 0, "uvu", True)]

...
```

Sections: OpenEquivariance, PyTorch Examples, JAX Examples, Copyright

</details>

### opentelemetry-exporter-zipkin-json

Zipkin Span JSON Exporter for OpenTelemetry

`pip install opentelemetry-exporter-zipkin-json` · installs (wheel) · licence: Apache-2.0 · rank 7138 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-exporter-zipkin-json/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This library allows export of tracing data to Zipkin using JSON
for serialization.

Sections: OpenTelemetry Zipkin JSON Exporter, References

</details>

### opensearch-mcp-server-py

OpenSearch MCP Server

`pip install opensearch-mcp-server-py` · installs (wheel) · licence: Apache-2.0 · rank 7225 · last release 2026-09-17 · [PyPI](https://pypi.org/project/opensearch-mcp-server-py/) · [docs](https://github.com/opensearch-project/opensearch-mcp-server-py/blob/main/USER_GUIDE.md) · [source](https://github.com/opensearch-project/opensearch-mcp-server-py.git)

<details><summary>README extract</summary>

- OpenSearch MCP Server
- Installing opensearch-mcp-server-py
- Available tools
- User Guide
- Agent Memory
- Contributing
- Code of Conduct
- License
- Copyright

opensearch-mcp-server-py is a Model Context Protocol (MCP) server for OpenSearch that enables AI assistants to interact with OpenSearch clusters. ...

Sections: OpenSearch MCP Server, Zero-Config Setup, Available Tools, Core Tools (Enabled by Default), Additional Tools (Disabled by Default), Agentic Memory Tools (Disabled by Default), Observability Tools (Disabled by Default), Search Relevance Workbench Tools (Disabled by Default), Skills Tools (Disabled by Default), Memory Tools (Opt-in), Tool Parameters, User Guide, Agent Memory, Choosing the right approach

</details>

### onnx-graphsurgeon

ONNX GraphSurgeon

`pip install onnx-graphsurgeon` · installs (wheel) · licence: Apache 2.0 · rank 7277 · last release 2026-04-08 · [PyPI](https://pypi.org/project/onnx-graphsurgeon/)

<details><summary>README extract</summary>

Example:
```python
graph = gs.import_onnx(onnx.load("model.onnx"))
```

Sections: ONNX GraphSurgeon, Introduction, Using Prebuilt Wheels, Building From Source, Using Make Targets, Building Manually, Examples, Understanding The Basics, Importers, IR, Tensor, Node, A Note On Modifying Inputs And Outputs, Graph

</details>

### onigurumacffi

python cffi bindings for the oniguruma regex engine

`pip install onigurumacffi` · installs (wheel) · licence: MIT · rank 7303 · last release 2026-01-25 · [PyPI](https://pypi.org/project/onigurumacffi/)

<details><summary>README extract</summary>

python cffi bindings for the oniguruma regex engine

Example:
```python
class OnigSearchOption(enum.IntEnum):
    NONE = ...
    NOTBOL = ...
    NOTEOL = ...
    POSIX_REGION = ...
    CHECK_VALIDITY_OF_STRING = ...
    NOT_BEGIN_STRING = ...
    NOT_BEGIN_POSITION = ...
```

Sections: onigurumacffi, api, `compile(pattern: str) -> _Pattern`, `compile_regset(*patterns: str) -> _RegSet`, `OnigSearchOption`, `_Pattern.number_of_captures() -> int`, `_Match.group(n: int = 0) -> str`, `_Match[n: int] -> str`, `_Match.start(n: int = 0) -> int`, `_Match.end(n: int = 0) -> int`, `_Match.span(n: int = 0) -> int`, `_Match.expand(s: str) -> str`

</details>

### openapi-codec

An OpenAPI codec for Core API.

`pip install openapi-codec` · installs from source (sdist only) · licence: BSD License · rank 7405 · last release 2017-07-19 · [PyPI](https://pypi.org/project/openapi-codec/)

### ocp-tessellate

Tessellate OCP (https://github.com/cadquery/OCP) objects to use with threejs

`pip install ocp-tessellate` · installs (wheel) · licence: Apache-2.0 · rank 7409 · last release 2026-10-18 · [PyPI](https://pypi.org/project/ocp-tessellate/)

<details><summary>README extract</summary>

Tessellate OCP (Python bindings for OpenCascade) shapes into a JSON-friendly format suitable for three-cad-viewer and downstream tooling such as ocp_vscode.

It accepts geometry from CadQuery, build123d, and raw `TopoDS*` shapes of OCP or nanocct, walks the structure, computes triangulations / discretized edges, and emits a hierarchical group of ...

Example:
```python
from build123d import Box, Sphere, Compound
from ocp_tessellate.convert import to_ocpgroup, tessellate_group

box = Box(1, 2, 3)
sphere = Sphere(0.5)
sphere.label = "ball"
assembly = Compound(label="root", children=[box, sphere])

# Step 1: convert to an OcpGroup hierarchy + instance list
group, instances = to_ocpgroup(assembly)

...
```

...

</details>

### onnx-weekly

Open Neural Network Exchange

`pip install onnx-weekly` · installs (wheel) · licence: Apache-2.0 · rank 7429 · last release 2026-11-02 · [PyPI](https://pypi.org/project/onnx-weekly/) · [source](https://github.com/onnx/onnx)

<details><summary>README extract</summary>

Open Neural Network Exchange (ONNX) is an open ecosystem that empowers AI developers
to choose the right tools as their project evolves. ONNX provides an open source format for AI models, both deep learning and traditional ML. It defines an extensible computation graph model, as well as definitions of built-in operators and standard
data types. ...

Features:
A fixed build timestamp removes one known source of nondeterminism. When
independent builds use the same controlled inputs, their artifacts can be
compared byte for byte, with cryptographic digests providing a practical
shortcut. ...

Sections: Use ONNX, Learn about the ONNX spec, Programming utilities for working with ONNX Graphs, Discuss, Follow Us, Roadmap, Python ABI3 Compatibility, Why this matters, Trademark

</details>

### openmeteo-sdk

Open-Meteo Python SDK

`pip install openmeteo-sdk` · installs (wheel) · licence: MIT License · rank 7442 · last release 2026-10-30 · [PyPI](https://pypi.org/project/openmeteo-sdk/) · [docs](https://github.com/open-meteo/sdk/tree/main#readme) · [source](https://github.com/open-meteo/sdk)

<details><summary>README extract</summary>

`pip install openmeteo-sdk`

`VariableWithValues.ValuesInt64AsNumpy()` returns raw Unix timestamps in seconds for `sunrise`, `sunset`, `moonrise`, and `moonset`. When an event does not occur during the local calendar day, the value is the missing timestamp sentinel `INT64_MAX` (`9223372036854775807`). ...

Example:
```python
import numpy as np
import pandas as pd

missing_int64 = np.iinfo(np.int64).max

raw = variable.ValuesInt64AsNumpy()
timestamps = pd.to_datetime(
    pd.Series(raw).mask(raw == missing_int64),
    unit="s",
    utc=True,
)
```

Sections: Open-Meteo Python SDK, Missing sunrise, sunset, moonrise, and moonset timestamps

</details>

### oslo.db

Oslo Database library

`pip install oslo.db` · installs (wheel) · licence: Apache-2.0 · rank 7461 · last release 2026-08-24 · [PyPI](https://pypi.org/project/oslo.db/) · [source](https://opendev.org/openstack/oslo.db)

<details><summary>README extract</summary>

The oslo db (database) handling library, provides database
connectivity to different database backends and various other helper
utils.

* Free software: Apache license

</details>

### overloading

Function overloading for Python 3

`pip install overloading` · installs (wheel) · licence: MIT License · rank 7473 · last release 2016-04-15 · [PyPI](https://pypi.org/project/overloading/)

<details><summary>README extract</summary>

`overloading` is a module that provides function and method dispatching
based on the types and number of runtime arguments.

When an overloaded function is invoked, the dispatcher compares the supplied
arguments to available signatures and calls the implementation providing the
most accurate match:

Features:
* Function validation during registration and comprehensive resolution rules
 guarantee a well-defined outcome at invocation time.
* Supports the typing module introduced in Python 3.5.
* Supports optional parameters. ...

Example:
```python
@overload
def biggest(items: Iterable[int]):
    return max(items)

@overload
def biggest(items: Iterable[str]):
    return max(items, key=len)
```

Sections: Features, Documentation

</details>

### ordereddict

A drop-in substitute for Py2.7's new collections.OrderedDict that works in Python 2.4-2.6.

`pip install ordereddict` · installs from source (sdist only) · licence: MIT License · rank 7488 · last release 2010-10-28 · [PyPI](https://pypi.org/project/ordereddict/)

<details><summary>README extract</summary>

Drop-in substitute for Py2.7's new collections.OrderedDict. The recipe has big-oh
performance that matches regular dictionaries (amortized O(1)
insertion/deletion/lookup and O(n) iteration/repr/copy/equality_testing).

Originally based on

</details>

### oslo.messaging

Oslo Messaging API

`pip install oslo.messaging` · installs (wheel) · licence: Apache Software License · rank 7492 · last release 2026-10-19 · [PyPI](https://pypi.org/project/oslo.messaging/) · [source](https://opendev.org/openstack/oslo.messaging)

<details><summary>README extract</summary>

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

* License: Apache License, Version 2.0

</details>

### oslo.policy

Oslo Policy library

`pip install oslo.policy` · installs (wheel) · licence: Apache-2.0 · rank 7515 · last release 2026-08-24 · [PyPI](https://pypi.org/project/oslo.policy/) · [source](https://opendev.org/openstack/oslo.policy)

<details><summary>README extract</summary>

The Oslo Policy library provides support for RBAC policy enforcement across
all OpenStack services.

* Free software: Apache license

</details>

### opendal

Apache OpenDAL™ Python Binding

`pip install opendal` · installs (wheel) · licence: Apache-2.0 · rank 7534 · last release 2026-10-18 · [PyPI](https://pypi.org/project/opendal/) · [docs](https://opendal.apache.org/docs/python/index.html) · [source](https://github.com/apache/opendal)

<details><summary>README extract</summary>

This package provides a native Python binding for Apache OpenDAL™, a data access
layer that allows you to access various storage services in a unified way.

We release the OpenDAL Python binding independently of the
`opendal` crate (Rust core). For updates
and compatibility, use the Python binding version instead of the `opendal` crate
version. ...

Example:
```python
import opendal

# Configure a service, then build an operator from it.
op = opendal.Operator("fs", root="/tmp")

# The same verbs work on every service.
op.write("test.txt", b"Hello World")
print(op.read("test.txt"))
print(op.stat("test.txt").content_length)
```

Sections: Apache OpenDAL™ Python Binding, Useful Links, Quickstart, Used By, Third-party software

</details>

### osprofiler

OpenStack Profiler Library

`pip install osprofiler` · installs (wheel) · licence: Apache Software License · rank 7617 · last release 2026-05-05 · [PyPI](https://pypi.org/project/osprofiler/) · [source](https://opendev.org/openstack/osprofiler)

<details><summary>README extract</summary>

OSProfiler provides a tiny but powerful library that is used by
most (soon to be all) OpenStack projects and their python clients. It
provides functionality to be able to generate 1 trace per request, that goes
through all involved services. ...

</details>

### oslo.middleware

Oslo Middleware library

`pip install oslo.middleware` · installs (wheel) · licence: Apache-2.0 · rank 7662 · last release 2026-07-10 · [PyPI](https://pypi.org/project/oslo.middleware/) · [source](https://opendev.org/openstack/oslo.middleware)

<details><summary>README extract</summary>

Oslo middleware library includes components that can be injected into
wsgi pipelines to intercept request/response flows. The base class can be
enhanced with functionality like add/delete/modification of http headers
and support for limiting size/connection etc.

* Free software: Apache license

</details>

### onnx2torch

ONNX to PyTorch converter

`pip install onnx2torch` · installs (wheel) · licence: Apache Software License · rank 7667 · last release 2024-08-07 · [PyPI](https://pypi.org/project/onnx2torch/) · [source](https://github.com/ENOT-AutoDL/onnx2torch)

<details><summary>README extract</summary>

onnx2torch is an ONNX to PyTorch converter.
Our converter:

- Is easy to use – Convert the ONNX model with the function call `convert`;
- Is easy to extend – Write your own custom layer in PyTorch and register it with `@add_converter`;
- Convert back to ONNX – You can convert the model back to ONNX using the `torch.onnx.export` function. ...

Example:
```python
import onnx
import torch
from onnx2torch import convert

# Path to ONNX model
onnx_model_path = "/some/path/mobile_net_v2.onnx"
# You can pass the path to the onnx model to convert it or...
torch_model_1 = convert(onnx_model_path)

# Or you can load a regular onnx model and pass it to the converter
onnx_model = onnx.load(onnx_model_path)
...
```

...

</details>

### openpi-client

Runs openpi policy interface by websocket connection to a server.

`pip install openpi-client` · installs (wheel) · licence: not stated · rank 7729 · last release 2026-03-30 · [PyPI](https://pypi.org/project/openpi-client/)

<details><summary>README extract</summary>

Runs openpi policy interface by websocket connection to a server.

</details>

### oslo.service

oslo.service library

`pip install oslo.service` · installs (wheel) · licence: Apache Software License · rank 7736 · last release 2026-07-31 · [PyPI](https://pypi.org/project/oslo.service/) · [source](https://opendev.org/openstack/oslo.service)

<details><summary>README extract</summary>

oslo.service provides a framework for defining new long-running
services using the patterns established by other OpenStack
applications. It also includes utilities long-running applications
might need for working with SSL or WSGI, performing periodic
operations, interacting with systemd, etc.

* Free software: Apache license

</details>

### openmeteo-requests

Open-Meteo Python Library

`pip install openmeteo-requests` · installs (wheel) · licence: MIT License · rank 7800 · last release 2026-01-19 · [PyPI](https://pypi.org/project/openmeteo-requests/) · [docs](https://github.com/open-meteo/python-requests/tree/main#readme) · [source](https://github.com/open-meteo/python-requests)

<details><summary>README extract</summary>

This API client provides access to weather data from Open-Meteo Weather API based on the Python library `niquests` and compatible with the `requests` library.

A key feature is its use of FlatBuffers instead of JSON for data transfer. FlatBuffers are particularly efficient when dealing with large volumes of time-series data. ...

Example:
```python
# pip install openmeteo-requests

import openmeteo_requests

openmeteo = openmeteo_requests.Client()

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "
params = {
    "latitude": 52.52,
    "longitude": 13.41,
...
```

Sections: Open-Meteo API Python Client, Basic Usage, NumPy, Pandas, Polars, Caching Data, Multiple Locations / Models, TODO

</details>

### orion-py-client

Python Client for Orion Feature Store to push/produce Model Features and get features' metadata

`pip install orion-py-client` · installs (wheel) · licence: Apache Software License · rank 7804 · last release 2026-09-01 · [PyPI](https://pypi.org/project/orion-py-client/) · [source](https://github.com/meesho/orion/orion_py_client)

<details><summary>README extract</summary>

A lightweight Python client for interacting with Orion Feature Store. This client provides functionality for feature metadata retrieval, protobuf serialization, and Kafka integration. 🚀

This client helps in pushing ML model's features stored in offline sources (like tables, Cloud storage objects in parquet/delta format, etc) to Orion Feature Store

Features:
- Feature metadata retrieval
- Protobuf serialization of feature values and produce to Apache Kafka

 - Scalar types (FP32, FP64, Int32, Int64, UInt32, UInt64, String, Bool)
 - Vector types (Vectors of each of the above Scalar Types) ...

Example:
```python
from orion_py_client import OrionPyClient

# Initialize the client
client = OrionPyClient(
    features_metadata_source_url="your_features_metadata_source_url",
...

</details>

### obspec

Object storage interface definitions for Python.

`pip install obspec` · installs (wheel) · licence: MIT · rank 7952 · last release 2025-06-25 · [PyPI](https://pypi.org/project/obspec/) · [docs](https://developmentseed.org/obspec/latest/) · [source](https://github.com/developmentseed/obspec)

<details><summary>README extract</summary>

A Python protocol for interfacing with object storage.

Read the release post.

It's designed to abstract away the complexities of different object storage providers while acknowledging that object storage is _not a filesystem. The Python protocols present more similarities to HTTP requests than Python file objects. ...

Sections: obspec, Implementations, Utilities

</details>

### opentelemetry-instrumentation-structlog

OpenTelemetry structlog instrumentation

`pip install opentelemetry-instrumentation-structlog` · installs (wheel) · licence: Apache-2.0 · rank 7960 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-structlog/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry structlog integration, References

</details>

### oslo.metrics

Oslo Metrics library

`pip install oslo.metrics` · installs (wheel) · licence: Apache-2.0 · rank 8002 · last release 2026-08-24 · [PyPI](https://pypi.org/project/oslo.metrics/) · [source](https://opendev.org/openstack/oslo.metrics)

<details><summary>README extract</summary>

This Oslo metrics API supports collecting metrics data from other Oslo
libraries and exposing the metrics data to monitoring system.

</details>

### onnx2torch-py313

ONNX to PyTorch converter

`pip install onnx2torch-py313` · installs (wheel) · licence: Apache Software License · rank 8050 · last release 2025-04-11 · [PyPI](https://pypi.org/project/onnx2torch-py313/) · [source](https://github.com/ENOT-AutoDL/onnx2torch)

<details><summary>README extract</summary>

onnx2torch is an ONNX to PyTorch converter.
Our converter:

- Is easy to use – Convert the ONNX model with the function call `convert`;
- Is easy to extend – Write your own custom layer in PyTorch and register it with `@add_converter`;
- Convert back to ONNX – You can convert the model back to ONNX using the `torch.onnx.export` function. ...

Example:
```python
import onnx
import torch
from onnx2torch import convert

# Path to ONNX model
onnx_model_path = "/some/path/mobile_net_v2.onnx"
# You can pass the path to the onnx model to convert it or...
torch_model_1 = convert(onnx_model_path)

# Or you can load a regular onnx model and pass it to the converter
onnx_model = onnx.load(onnx_model_path)
...
```

...

</details>

### opentelemetry-exporter-jaeger-proto-grpc

Jaeger Protobuf Exporter for OpenTelemetry

`pip install opentelemetry-exporter-jaeger-proto-grpc` · installs (wheel) · licence: Apache Software License · rank 8132 · last release 2023-11-07 · [PyPI](https://pypi.org/project/opentelemetry-exporter-jaeger-proto-grpc/)

<details><summary>README extract</summary>

This library allows to export tracing data to Jaeger.

Sections: OpenTelemetry Jaeger Protobuf Exporter, Configuration, References

</details>

### odoo-test-helper

Our Odoo project tools

`pip install odoo-test-helper` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 8179 · last release 2026-02-20 · [PyPI](https://pypi.org/project/odoo-test-helper/) · [docs](https://github.com/oca/odoo-test-helper) · [source](https://github.com/oca/odoo-test-helper)

_README extract left out: share-alike licence._

### opentelemetry-exporter-jaeger

Jaeger Exporters for OpenTelemetry

`pip install opentelemetry-exporter-jaeger` · installs (wheel) · licence: Apache Software License · rank 8188 · last release 2023-11-07 · [PyPI](https://pypi.org/project/opentelemetry-exporter-jaeger/)

<details><summary>README extract</summary>

This library is provided as a convenience to install all supported Jaeger Exporters. Currently it installs:
* opentelemetry-exporter-jaeger-proto-grpc
* opentelemetry-exporter-jaeger-thrift

To avoid unnecessary dependencies, users should install the specific package once they've determined their
preferred serialization method.

Sections: OpenTelemetry Jaeger Exporter, References

</details>

### oslo.cache

Cache storage for OpenStack projects.

`pip install oslo.cache` · installs (wheel) · licence: Apache-2.0 · rank 8195 · last release 2026-07-10 · [PyPI](https://pypi.org/project/oslo.cache/) · [source](https://opendev.org/openstack/oslo.cache)

<details><summary>README extract</summary>

`oslo.cache` aims to provide a generic caching mechanism for OpenStack projects
by wrapping the dogpile.cache library. The dogpile.cache
library provides support memoization, key value storage and interfaces to common
caching backends such as Memcached.

* Free software: Apache license

</details>

### onnxoptimizer

ONNX Optimizer

`pip install onnxoptimizer` · installs (wheel) · licence: Apache-2.0 · rank 8231 · last release 2026-01-07 · [PyPI](https://pypi.org/project/onnxoptimizer/)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: ONNX Project Contributors

SPDX-License-Identifier: Apache-2.0

ONNX provides a C++ library for performing arbitrary optimizations on ONNX models, as well as a growing list of prepackaged optimization passes.

The primary motivation is to share work between the many ONNX backend implementations. ...

Sections: ONNX Optimizer, Introduction, Command-line API, Roadmap, Relevant tools

</details>

### ocifs

Convenient filesystem interface over Oracle Cloud's Object Storage

`pip install ocifs` · installs (wheel) · licence: Universal Permissive License (UPL) · rank 8328 · last release 2025-11-06 · [PyPI](https://pypi.org/project/ocifs/) · [docs](https://ocifs.readthedocs.io/en/latest/index.html) · [source](https://github.com/oracle/ocifs)

<details><summary>README extract</summary>

The Oracle Cloud Infrastructure Object Storage service is an internet-scale, high-performance storage platform that offers reliable and cost-efficient data durability. With Object Storage, you can safely and securely store or retrieve data directly from the internet or from within the cloud platform. ...

Example:
```python
from ocifs import OCIFileSystem

fs = OCIFilesystem("~/.oci/config")
# 1.Create empty file or truncate in OCI objectstorage bucket
 fs.touch("oci://<my_bucket>@<my_namespace>/<my_prefix>/hello.txt", truncate=True, data=b"Writing to Object Storage!")
 # 2.Fetch(potentially multiple paths' contents
...
```

...

</details>

### optuna-dashboard

Real-time dashboard for Optuna

`pip install optuna-dashboard` · installs (wheel) · licence: MIT License · rank 8393 · last release 2026-09-10 · [PyPI](https://pypi.org/project/optuna-dashboard/)

<details><summary>README extract</summary>

:link: Website
| :page_with_curl: Docs
| :gear: Install Guide
| :pencil: Tutorial
| :bulb: Examples

Real-time dashboard for Optuna.
Code files were originally taken from Goptuna.

Example:
```python
import optuna

def objective(trial):
    x = trial.suggest_float("x", -100, 100)
    y = trial.suggest_categorical("y", [-1, 0, 1])
    return x**2 + y

if name == "main":
    study = optuna.create_study(
        storage="sqlite:///db.sqlite3",  # Specify the storage URL here.
        study_name="quadratic-simple"
    )
...
```

Sections: optuna-dashboard, Getting Started, Using an official Docker image, Jupyter Lab Extension (Experimental), Browser-only version (Experimental), VS Code and code-server Extension (Experimental), Submitting patches

</details>

### onvif-zeep

Python Client for ONVIF Camera

`pip install onvif-zeep` · installs from source (sdist only) · licence: MIT · rank 8442 · last release 2018-08-20 · [PyPI](https://pypi.org/project/onvif-zeep/)

<details><summary>README extract</summary>

python-onvif-zeep

ONVIF Client Implementation in Python

zeep >= 3.0.0

Example:
```python
from onvif import ONVIFCamera
mycam = ONVIFCamera('192.168.0.2', 80, 'user', 'passwd', '/etc/onvif/wsdl/')
```

Sections: Dependencies, Getting Started, Initialize an ONVIFCamera instance, Get information from your camera, Configure (Control) your camera, Use other services, ONVIF CLI, Single command example, Interactive mode, Batch mode, References

</details>

### oslo.upgradecheck

Common code for writing OpenStack upgrade checks

`pip install oslo.upgradecheck` · installs (wheel) · licence: Apache-2.0 · rank 8446 · last release 2026-07-10 · [PyPI](https://pypi.org/project/oslo.upgradecheck/) · [source](https://opendev.org/openstack/oslo.upgradecheck)

<details><summary>README extract</summary>

Common code for writing OpenStack upgrade checks

This project contains the common code necessary for writing upgrade checks
in OpenStack projects. It includes a module (oslo_upgradecheck.upgradecheck)
for the common code as well as an example (oslo_upgradecheck.main) of
integrating that code into a project.

* Free software: Apache license

</details>

### openmetadata-ingestion

Ingestion Framework for OpenMetadata

`pip install openmetadata-ingestion` · installs (wheel) · licence: not stated · rank 8456 · last release 2026-10-30 · [PyPI](https://pypi.org/project/openmetadata-ingestion/) · [docs](https://docs.open-metadata.org/) · [source](https://github.com/open-metadata/OpenMetadata)

<details><summary>README extract</summary>

This guide will help you setup the Ingestion framework and connectors

OpenMetadata Ingestion is a simple framework to build connectors and ingest metadata of various systems through OpenMetadata APIs. It could be used in an orchestration framework(e.g. Apache Airflow) to ingest metadata.
Prerequisites

- Python >= 3.9.x ...

Sections: Docs, TopologyRunner

</details>

### ob-metaflow-stubs

Metaflow Stubs: Stubs for the metaflow package

`pip install ob-metaflow-stubs` · installs (wheel) · licence: Apache License 2.0 · rank 8523 · last release 2026-10-30 · [PyPI](https://pypi.org/project/ob-metaflow-stubs/)

<details><summary>README extract</summary>

This package contains stub files for `metaflow` and thus offers type hints for various editors (such as `VSCode`) and language servers (such as `Pylance`).

</details>

### oauth-cli-kit

Reusable OAuth 2.0 + PKCE helpers for CLI applications

`pip install oauth-cli-kit` · installs (wheel) · licence: MIT License · rank 8566 · last release 2026-06-30 · [PyPI](https://pypi.org/project/oauth-cli-kit/)

### openinference-instrumentation-dspy

OpenInference DSPy Instrumentation

`pip install openinference-instrumentation-dspy` · installs (wheel) · licence: Apache-2.0 · rank 8608 · last release 2026-11-04 · [PyPI](https://pypi.org/project/openinference-instrumentation-dspy/)

<details><summary>README extract</summary>

Python auto-instrumentation library for DSPy.

These traces are fully OpenTelemetry-compatible and can be sent to an OpenTelemetry collector for viewing, such as Arize Phoenix or Arize AX.

Example:
```python
from openinference.instrumentation.dspy import DSPyInstrumentor
from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

endpoint = "
...
```

Sections: OpenInference DSPy Instrumentation, Quickstart, More Info

</details>

### outerbounds

More Data Science, Less Administration

`pip install outerbounds` · installs (wheel) · licence: Other/Proprietary License · rank 8624 · last release 2026-10-30 · [PyPI](https://pypi.org/project/outerbounds/) · [docs](https://docs.metaflow.org)

### openresponses-types

Python SDK for OpenResponses specification

`pip install openresponses-types` · installs (wheel) · licence: Apache-2.0 · rank 8660 · last release 2026-08-05 · [PyPI](https://pypi.org/project/openresponses-types/) · [docs](https://github.com/mozilla-ai/openresponses-python#readme) · [source](https://github.com/mozilla-ai/openresponses-python)

<details><summary>README extract</summary>

Python SDK providing Pydantic models for the OpenResponses API specification.

Sections: OpenResponses Types, Setup, Generate Types, Versioning, Links

</details>

### openlineage-dbt

OpenLineage integration with dbt

`pip install openlineage-dbt` · installs (wheel) · licence: not stated · rank 8760 · last release 2026-10-29 · [PyPI](https://pypi.org/project/openlineage-dbt/)

<details><summary>README extract</summary>

Wrapper script for automatic metadata collection from dbt

Features:
Metadata

* Model run lifecycle
* Model inputs / outputs

Sections: OpenLineage dbt integration, Features, Requirements, Configuration, Transport, Logging, Usage, dbt Core v2, Upgrading from dbt Core v1

</details>

### ocpp

Python package implementing the JSON version of the Open Charge Point Protocol (OCPP).

`pip install ocpp` · installs (wheel) · licence: MIT License · rank 8798 · last release 2025-07-16 · [PyPI](https://pypi.org/project/ocpp/) · [docs](https://ocpp.readthedocs.io/en/latest/) · [source](https://github.com/mobilityhouse/ocpp)

<details><summary>README extract</summary>

Python package implementing the JSON version of the Open Charge Point Protocol
(OCPP). Currently OCPP 1.6 (errata v4), OCPP 2.0.1 (Edition 2 FINAL, 2022-12-15 and Edition 3 errata 2024-11)
are supported.

Sections: OCPP, Documentation, Aknowledgements

</details>

### os-testr

A testr wrapper to provide functionality for OpenStack projects

`pip install os-testr` · installs (wheel) · licence: Apache Software License · rank 8887 · last release 2022-04-04 · [PyPI](https://pypi.org/project/os-testr/)

<details><summary>README extract</summary>

A testr wrapper to provide functionality for OpenStack projects.

* Free software: Apache license

Features:
* `subunit-trace`: an output filter for a subunit stream which provides
 useful information about the run
* `subunit2html`: generates a test results html page from a subunit stream
* `generate-subunit`: generate a subunit stream for a single test

Sections: os-testr, Features

</details>

### openlineage-airflow

OpenLineage integration with Airflow

`pip install openlineage-airflow` · installs (wheel) · licence: Apache Software License · rank 8922 · last release 2025-12-11 · [PyPI](https://pypi.org/project/openlineage-airflow/) · [source](https://github.com/OpenLineage/OpenLineage/tree/main/integration/airflow)

<details><summary>README extract</summary>

Features:
Metadata

* Task lifecycle
* Task parameters
* Task runs linked to versioned code
* Task inputs / outputs

Lineage

* Track inter-DAG dependencies

Built-in

* SQL parser
* Link to code builder (ex: GitHub)
* Metadata extractors

Example:
```python
SparkSubmitOperator(
    task_id="my_task",
    application="/script.py",
    conf={
      # separated components
      "spark.openlineage.parentJobNamespace": "{{ macros.OpenLineagePlugin.lineage_job_namespace() }}",
      "spark.openlineage.parentJobName": "{{ macros.OpenLineagePlugin.lineage_job_name(task_instance) }}",
...
```

...

</details>

### onnxruntime_extensions

ONNXRuntime Extensions

`pip install onnxruntime_extensions` · does not install on CPython 3.14 · licence: MIT License · rank 9158 · last release 2026-02-04 · [PyPI](https://pypi.org/project/onnxruntime_extensions/)

<details><summary>README extract</summary>

Introduction: ONNXRuntime-Extensions is a C/C++ library that extends the capability of the ONNX models and inference with ONNX Runtime, via ONNX Runtime Custom Operator ABIs. It includes a set of ONNX Runtime Custom Operator to support the common pre- and post-processing operators for vision, text, and nlp models. ...

Example:
```python
help(onnxruntime_extensions.gen_processing_models)
```

Sections: ONNXRuntime-Extensions, What's ONNXRuntime-Extensions, Quickstart, Usage, 1. Generation of Pre-/Post-Processing ONNX Model, NOTE, 2. Using Extensions for ONNX Runtime inference, Python, C++, Java, C

</details>

### once-py

Utility for initialization ensuring functions are called only once

`pip install once-py` · installs (wheel) · licence: MIT · rank 9382 · last release 2025-12-02 · [PyPI](https://pypi.org/project/once-py/)

<details><summary>README extract</summary>

This library provides functionality to ensure a function is called exactly
once in Python, heavily inspired by `std::call_once`.

During initialization, we often want to ensure code is run exactly once.
But thinking about all the different ways this constraint can be violated can
be time-consuming and complex. ...

Example:
```python
import once

@once.once
def my_expensive_object():
    load_expensive_resource()
    load_more_expensive_resources()
    return ObjectSingletonUsingLotsOfMemory()

def caller_one():
    my_expensive_object().use_it()

def caller_two_from_a_separate_thread():
    my_expensive_object().use_it()

def optional_init_function_to_prewarm():
...
```

Sections: Once, Use with methods, Options, `per_thread`, `allow_reset`, `retry_exceptions`

</details>

### ome-types

Python dataclasses for the OME data model

`pip install ome-types` · installs (wheel) · licence: MIT · rank 9537 · last release 2026-10-16 · [PyPI](https://pypi.org/project/ome-types/) · [docs](https://ome-types.readthedocs.io/en/latest/) · [source](https://github.com/imaging-formats/ome-types)

<details><summary>README extract</summary>

`ome_types` provides a set of python dataclasses and utility functions for
parsing the OME-XML
format into
fully-typed python objects for interactive or programmatic access in python. It
can also take these python objects and output them into valid OME-XML.
`ome_types` is a pure python library and does not require a Java virtual
machine. ...

Example:
```python
from ome_types import from_xml

ome = from_xml("tests/data/hcs.ome.xml")
```

...

</details>

### opendataloader-pdf

A Python wrapper for the opendataloader-pdf Java CLI.

`pip install opendataloader-pdf` · installs (wheel) · licence: Apache-2.0 · rank 9554 · last release 2026-11-06 · [PyPI](https://pypi.org/project/opendataloader-pdf/)

<details><summary>README extract</summary>

PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.

🔍 PDF parser for AI data extraction — Extract Markdown, JSON (with bounding boxes), and HTML from any PDF. #1 in benchmarks (0.907 overall). Deterministic local mode + AI hybrid mode for complex pages. ...

Features:
MPL 2.0 requires file-level copyleft, which often triggers legal review before enterprise adoption. Apache 2.0 is fully permissive — no copyleft obligations, easier to integrate into commercial projects. ...

Example:
```python
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="markdown,json"
)
```

...

</details>

### openmim

MIM Installs OpenMMLab packages

`pip install openmim` · installs (wheel) · licence: not stated · rank 9779 · last release 2023-06-28 · [PyPI](https://pypi.org/project/openmim/)

<details><summary>README extract</summary>

Example:
```python
from mim import install

# install mmcv
install('mmcv-full')

# install mmcls will automatically install mmcv if it is not installed
install('mmcls')

# install extension based on OpenMMLab
install('git+
```

Sections: Major Features, Customization, Build custom projects with MIM, Command, Projects in OpenMMLab

</details>

### openinference-instrumentation-instructor

OpenInference Instructor Instrumentation

`pip install openinference-instrumentation-instructor` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 9840 · last release 2026-11-04 · [PyPI](https://pypi.org/project/openinference-instrumentation-instructor/)

<details><summary>README extract</summary>

Python auto-instrumentation library for the Instructor library.

These traces are fully OpenTelemetry compatible and can be sent to an OpenTelemetry collector for viewing, such as Arize Phoenix or Arize AX.

Example:
```python
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

endpoint = "
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter(endpoint)))
...
```

Sections: OpenInference Instructor Instrumentation, Quickstart, More Info

</details>

### os-client-config

OpenStack Client Configuation Library

`pip install os-client-config` · installs (wheel) · licence: Apache Software License · rank 9883 · last release 2025-07-08 · [PyPI](https://pypi.org/project/os-client-config/)

<details><summary>README extract</summary>

`os-client-config` is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want to
put in a config file. ...

Sections: os-client-config, Source

</details>

### ob-metaflow

Metaflow: More AI and ML, Less Engineering

`pip install ob-metaflow` · installs (wheel) · licence: Apache License 2.0 · rank 9993 · last release 2026-10-30 · [PyPI](https://pypi.org/project/ob-metaflow/)

<details><summary>README extract</summary>

Metaflow is a human-centric framework designed to help scientists and engineers build and manage real-life AI and ML systems. Serving teams of all sizes and scale, Metaflow streamlines the entire development lifecycle—from rapid prototyping in notebooks to reliable, maintainable production deployments—enabling teams to iterate quickly and deliver ...

Sections: Metaflow, From prototype to production (and back), Getting started, Deploying infrastructure for Metaflow in your cloud, Get in touch

</details>

### orq-ai-sdk

Python Client SDK for the Orq API.

`pip install orq-ai-sdk` · installs (wheel) · licence: not stated · rank 10006 · last release 2026-11-06 · [PyPI](https://pypi.org/project/orq-ai-sdk/) · [source](https://github.com/orq-ai/orq-python.git)

<details><summary>README extract</summary>

Developer-friendly & type-safe Python SDK specifically catered to leverage *orq-ai-sdk* API.

orq.ai API: orq.ai API documentation

For more information about the API: orq.ai Documentation

Example:
```python
# !/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
# "orq-ai-sdk",
# ]
# ///

from orq_ai_sdk import Orq

sdk = Orq(
  # SDK arguments
)

# Rest of script here...
```

Sections: orq-ai-sdk, Summary, uv, PIP, Poetry, Shell and script usage with `uv`, PyCharm, SDK Example Usage, Example, Authentication, Available Resources and Operations, Agents, Agents.External, ~~Agents.Responses~~

</details>

### ob-metaflow-extensions

Outerbounds Platform Extensions for Metaflow

`pip install ob-metaflow-extensions` · installs (wheel) · licence: Commercial · rank 10031 · last release 2026-10-29 · [PyPI](https://pypi.org/project/ob-metaflow-extensions/)

<details><summary>README extract</summary>

This package installs client side packages for Outerbounds platform. See Outerbounds platform documentation and Metaflow documentation for more info on how to use it.

</details>

### openviking-sdk

Lightweight Python HTTP SDK for OpenViking

`pip install openviking-sdk` · installs (wheel) · licence: not stated · rank 10110 · last release 2026-11-02 · [PyPI](https://pypi.org/project/openviking-sdk/)

<details><summary>README extract</summary>

Lightweight Python HTTP SDK for OpenViking.

`openviking-sdk` is the small package for users who only need to call an existing OpenViking server over HTTP. It avoids the heavier local-runtime, server, and CLI dependencies from the main `openviking` package.

Example:
```python
from openviking_sdk import SyncHTTPClient

client = SyncHTTPClient(
    url="
    api_key="your-user-key",
)
client.initialize()

healthy = client.health()
print("health:", healthy)

session = client.create_session(session_id="demo-session")
print("session:", session)

client.session(session_id="demo-session").add_message(
    role="user",
...
```

...

</details>

### ob-project-utils

Utilities for Outerbounds projects

`pip install ob-project-utils` · installs (wheel) · licence: not stated · rank 10234 · last release 2026-10-22 · [PyPI](https://pypi.org/project/ob-project-utils/)

<details><summary>README extract</summary>

- `deploy` - CI/CD deployment script for obprojects
- `src-html` - Svelte source for highlight and table (eval) cards
- `metaflow-extensions` - the highlight card backend & `card(type='highlight')`
- `highlight_card` - highlight card mutator, i.e. the user-facing `@highlight`
- `obproject` - `ProjectFlow` base flow and supporting modules

</details>

### openinference-instrumentation-mcp

OpenInference MCP Instrumentation

`pip install openinference-instrumentation-mcp` · installs (wheel) · licence: Apache-2.0 · rank 10271 · last release 2026-11-04 · [PyPI](https://pypi.org/project/openinference-instrumentation-mcp/)

<details><summary>README extract</summary>

Python auto-instrumentation library for MCP's python SDK. Currently, it only enables context propagation so that the span active
when making an MCP tool call can be connected to those generated when executing it. It does not generate any telemetry.

Sections: OpenInference MCP Instrumentation, More Info

</details>

### ontoportal_client

A client to BioPortal and other OntoPortal instances

`pip install ontoportal_client` · installs (wheel) · licence: MIT · rank 10296 · last release 2026-04-14 · [PyPI](https://pypi.org/project/ontoportal_client/) · [docs](https://ontoportal_client.readthedocs.io) · [source](https://github.com/cthoyt/ontoportal-client.git)

<details><summary>README extract</summary>

A client to BioPortal and other OntoPortal instances.

Example:
```python
from ontoportal_client import BioPortalClient

bioportal_client = BioPortalClient()
ontologies = bioportal_client.get_ontologies()
```

Sections: OntoPortal Client, 💪 Getting Started, ⚙️ Configuration, 👋 Attribution, 🍪 Cookiecutter, 📖 Building the Documentation, Initial Configuration, Configuring ReadTheDocs, Configuring Archival on Zenodo, Registering with the Python Package Index (PyPI), Configuring your machine's connection to PyPI, Uploading to PyPI, Releasing on GitHub, Updating Package Boilerplate

</details>

### oaklib

Ontology Access Kit: Python library for common ontology operations over a variety of backends

`pip install oaklib` · installs (wheel) · licence: Apache-2.0 · rank 10301 · last release 2026-08-03 · [PyPI](https://pypi.org/project/oaklib/)

<details><summary>README extract</summary>

Python lib for common ontology operations over a variety of backends.

OAK provides a collection of interfaces for various ontology operations, including:

 - look up basic features of an ontology element, such as its label, definition, relationships, or aliases
 - search an ontology for a term
 - validate an ontology
 - modify or delete terms
 - ...

Example:
```python
from oaklib import get_adapter

# connect to the CL sqlite database adapter
# (will first download if not already downloaded)
adapter = get_adapter("sqlite:obo:cl")

NEURON = "CL:0000540"

print('## Basic info')
print(f'ID: {NEURON}')
print(f'Label: {adapter.label(NEURON)}')

for alias in adapter.entity_aliases(NEURON):
...
```

...

</details>

### onfido-python

Python library for the Onfido API

`pip install onfido-python` · installs (wheel) · licence: MIT · rank 10315 · last release 2026-11-06 · [PyPI](https://pypi.org/project/onfido-python/) · [source](https://github.com/onfido/onfido-python)

<details><summary>README extract</summary>

The official Python library for integrating with the Onfido API.

Documentation is available at <

This version uses Onfido API v3.6. Refer to our API versioning guide for details. It explains which client library versions use which versions of the API.

Example:
```python
import onfido

import urllib3
from os import environ

configuration = onfido.Configuration(
    api_token=environ['ONFIDO_API_TOKEN'],
    region=onfido.configuration.Region.EU,     # Supports `EU`, `US` and `CA`
    timeout=urllib3.util.Timeout(connect=60.0, read=60.0)
  )

with onfido.ApiClient(configuration) as api_client:
...
```

...

</details>

### openmeter

Client for OpenMeter: Real-Time and Scalable Usage Metering

`pip install openmeter` · installs (wheel) · licence: Apache Software License · rank 10336 · last release 2026-10-09 · [PyPI](https://pypi.org/project/openmeter/) · [source](https://github.com/openmeter/openmeter)

<details><summary>README extract</summary>

On PyPI

This package is generated by `@typespec/http-client-python` with Typespec.

- Python 3.9 or later is required to use this package.

Features:
| Namespace | Operation | Method | Description |

| Events | | | Track usage by ingesting events |
| | Create | `client.events.ingest_event(event)` | Ingest a single event |
| | Create | `client.events.ingest_events(events)` | Ingest batch of events ...

Example:
```python
from openmeter import Client

client = Client(
    endpoint="
    token="your-api-token",
)
```

Sections: OpenMeter Python SDK, Prerequisites, Examples, Setup, Synchronous Client, Async Client, Ingest an Event, Synchronous, Async, Query Meter, Client API Reference, Overview

</details>

### openfeature-hooks-opentelemetry

OpenTelemetry hooks for the OpenFeature Python SDK

`pip install openfeature-hooks-opentelemetry` · installs (wheel) · licence: Apache-2.0 · rank 10394 · last release 2026-02-17 · [PyPI](https://pypi.org/project/openfeature-hooks-opentelemetry/)

<details><summary>README extract</summary>

The OpenTelemetry tracing hook for OpenFeature provides a spec compliant way to automatically add a feature flag evaluation to a span as a span event. Since feature flags are dynamic and affect runtime behavior, it’s important to collect relevant feature flag telemetry signals. ...

Example:
```python
from openfeature import api
from openfeature.contrib.hook.opentelemetry import TracingHook

api.add_hooks([TracingHook()])
```

Sections: OpenTelemetry Hook, Usage, Register Globally, Register Per Client

</details>

### ols-client

A client to the EBI Ontology Lookup Service

`pip install ols-client` · installs (wheel) · licence: MIT License · rank 10434 · last release 2025-08-04 · [PyPI](https://pypi.org/project/ols-client/) · [docs](https://ols_client.readthedocs.io) · [source](https://github.com/cthoyt/ols-client.git)

<details><summary>README extract</summary>

A client to the EBI Ontology Lookup Service.

Example:
```python
from ols_client import EBIClient

ebi_client = EBIClient()
ontologies = ebi_client.get_ontologies()
```

Sections: OLS Client, 💪 Getting Started, 👋 Attribution, Related, 🍪 Cookiecutter, 📖 Building the Documentation, Initial Configuration, Configuring ReadTheDocs, Configuring Archival on Zenodo, Registering with the Python Package Index (PyPI), Configuring your machine's connection to PyPI, Uploading to PyPI, Releasing on GitHub, Updating Package Boilerplate

</details>

### omnidoc

OmniDoc: world-leading AI office suite. Any-format conversion, layout-preserving translation in 38 languages, structured content extraction, native AI MCP for every document. Website: https://omnidoc.top/

`pip install omnidoc` · installs (wheel) · licence: not stated · rank 10439 · last release 2026-11-05 · [PyPI](https://pypi.org/project/omnidoc/) · [docs](https://docs.omnidoc.top/)

<details><summary>README extract</summary>

One app. One API. Your layout stays exactly where it was.

Stop re-typing translated PDFs. OmniDoc translates PDF, Word, PowerPoint, LaTeX and 11 more formats into 38 languages and puts every table, formula and footnote back in place. ...

Features:
The world's most powerful AI document engine, all in one app.

The first product to put PDF layout reconstruction, interactive dynamic documents and AI-native office work into one app: translated PDFs keep their layout, documents become web pages, ...

Example:
```python
from omnidoc import OmniDocClient

client = OmniDocClient()  # reads OMNIDOC_API_KEY
files = client.translate_file("report.docx", "en", output_dir="out")
print(files)
```

...

</details>

### onesignal-python-api

OneSignal

`pip install onesignal-python-api` · installs (wheel) · licence: not stated · rank 10572 · last release 2026-10-15 · [PyPI](https://pypi.org/project/onesignal-python-api/)

<details><summary>README extract</summary>

A powerful way to send personalized messages at scale and build effective customer engagement strategies. Learn more at onesignal.com # noqa: E501

</details>

### oslo.versionedobjects

Oslo Versioned Objects library

`pip install oslo.versionedobjects` · installs (wheel) · licence: Apache Software License · rank 10585 · last release 2026-08-24 · [PyPI](https://pypi.org/project/oslo.versionedobjects/) · [source](https://opendev.org/openstack/oslo.versionedobjects)

<details><summary>README extract</summary>

The oslo.versionedobjects library provides a generic versioned object model
that is RPC-friendly, with inbuilt serialization, field typing, and remotable
method calls. It can be used to define a data model within a project
independent of external APIs or database schema for the purposes of providing
upgrade compatibility across distributed ...

</details>

### opencensus-ext-requests

OpenCensus Requests Integration

`pip install opencensus-ext-requests` · installs (wheel) · licence: Apache Software License · rank 10596 · last release 2022-08-03 · [PyPI](https://pypi.org/project/opencensus-ext-requests/)

<details><summary>README extract</summary>

OpenCensus can trace HTTP requests made with the requests package. The request URL,
method, and status will be collected.

You can enable requests integration by specifying `'requests'` to `trace_integrations`.

It's possible to configure a list of URL you don't want traced. By default the request to exporter
won't be traced. ...

Example:
```python
import requests
from opencensus.trace import config_integration
from opencensus.trace.tracer import Tracer

if name == 'main':
    config_integration.trace_integrations(['requests'])
    tracer = Tracer()
    with tracer.span(name='parent'):
        response = requests.get(url='
```

Sections: OpenCensus requests Integration, Usage, References

</details>

### opentelemetry-proto-json

OpenTelemetry Python Json Proto

`pip install opentelemetry-proto-json` · installs (wheel) · licence: Apache-2.0 · rank 10642 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-proto-json/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This library contains the generated code for OpenTelemetry protobuf data model with JSON encoding support. The code in the current package was generated using the v1.10.0 release of opentelemetry-proto and includes definitions for the OpenTelemetry JSON Protobuf encoding specification.

Sections: OpenTelemetry Python Proto JSON, Code Generation, References

</details>

### opentelemetry-exporter-otlp-json-common

OpenTelemetry JSON encoding

`pip install opentelemetry-exporter-otlp-json-common` · installs (wheel) · licence: Apache-2.0 · rank 10652 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-exporter-otlp-json-common/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This library is provided as a convenience to encode to OTLP JSON.

Sections: OpenTelemetry JSON Encoding, References

</details>

### openbb-core

OpenBB package with core functionality.

`pip install openbb-core` · installs (wheel) · licence: Apache-2.0 · rank 10692 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-core/)

<details><summary>README extract</summary>

`openbb-core` is the runtime that turns a collection of installed Python
packages into the OpenBB Platform. By itself it ships **no data, no providers,
and no commands**. Its job is to:

1. Discover provider, command, and result-type extensions installed in the
 current Python environment via setuptools entry points.
2. ...

Example:
```python
result = obb.equity.price.historical("AAPL")
result.charting.to_chart()  # accessor registered by openbb_charting
```

Sections: openbb-core, Entry points, `openbb_core_extension`, `openbb_provider_extension`, `openbb_obbject_extension`, Console script: `openbb-build`, What lives inside the package, Prerequisites, Running the REST API, Bugs

</details>

### overpy

Python Wrapper to access the OpenStreepMap Overpass API

`pip install overpy` · installs (wheel) · licence: MIT License · rank 10882 · last release 2023-12-04 · [PyPI](https://pypi.org/project/overpy/) · [docs](https://python-overpy.readthedocs.io/) · [source](https://github.com/DinoTools/python-overpy)

<details><summary>README extract</summary>

A Python Wrapper to access the Overpass API.

Have a look at the documentation to find additional information.

Features:
* Query Overpass API
* Parse JSON and XML response data
* Additional helper functions

Example:
```python
import overpy

api = overpy.Overpass()

# fetch all ways and nodes
result = api.query("""
    way(50.746,7.154,50.748,7.157) ["highway"];
    (._;>;);
    out body;
    """)

for way in result.ways:
    print("Name: %s" % way.tags.get("name", "n/a"))
    print("  Highway: %s" % way.tags.get("highway", "n/a"))
    print("  Nodes:")
...
```

Sections: Python Overpass Wrapper, Features, Examples, Helper

</details>

### openskill

Multiplayer Rating System. No Friction.

`pip install openskill` · installs (wheel) · licence: MIT · rank 10915 · last release 2026-01-11 · [PyPI](https://pypi.org/project/openskill/) · [docs](https://openskill.me/en/stable) · [source](https://github.com/vivekjoshy/openskill.py)

<details><summary>README extract</summary>

A faster and open license asymmetric multi-team, multiplayer rating system comparable to TrueSkill.

In the multifaceted world of online gaming, an accurate multiplayer rating system plays a crucial role. ...

Example:
```python
>>> from openskill.models import PlackettLuce
>>> model = PlackettLuce()
>>> model.rating()
PlackettLuceRating(mu=25.0, sigma=8.333333333333334)
>>> r = model.rating
>>> [[a, b], [x, y]] = [[r(), r()], [r(), r()]]
>>> [[a, b], [x, y]] = model.rate([[a, b], [x, y]])
>>> a
PlackettLuceRating(mu=26.964294621803063, sigma=8.177962604389991)
>>> x
...
```

Sections: Description, Usage, Limited Example, References, Implementations in other Languages

</details>

### openweathermap

openweathermap

`pip install openweathermap` · installs (wheel) · licence: MIT License · rank 10991 · last release 2022-09-07 · [PyPI](https://pypi.org/project/openweathermap/)

<details><summary>README extract</summary>

get weather json from openweathermap

add this to your django settings:

OPENWEATHERMAP_TOKEN = 'YOUR TOKEN'

</details>

### ophyd

Bluesky hardware abstraction with an emphasis on EPICS

`pip install ophyd` · installs (wheel) · licence: BSD License · rank 11010 · last release 2026-06-04 · [PyPI](https://pypi.org/project/ophyd/)

<details><summary>README extract</summary>

Ophyd is a Python library for interfacing with hardware. It provides an
abstraction layer that enables experiment orchestration and data acquisition
code to operate above the specifics of particular devices and control systems.

Ophyd is typically used with the Bluesky Run Engine for experiment
orchestration and data acquisition. ...

</details>

### officeparserpy

A Python library to parse text out of any office file. Currently supports docx, pptx, xlsx, odt, odp, ods, pdf files.

`pip install officeparserpy` · installs (wheel) · licence: MIT License · rank 11157 · last release 2024-02-11 · [PyPI](https://pypi.org/project/officeparserpy/)

<details><summary>README extract</summary>

A Python library to parse text out of any office file.

Example:
```python
from officeparserpy import parse_office

# USING FILE BUFFERS
# instead of file path, you can also pass file buffers of one of the supported files
# on parse_office function.

# get file buffers
file_buffers = open("/path/to/officeFile", "rb").read()
# get parsed text from officeparserpy
...
```

Sections: officeparserpy, Library Usage, Configuration Object: OfficeParserConfig, Exception Types, Known Bugs

</details>

### OpenMM-CUDA-12

CUDA platform for OpenMM

`pip install OpenMM-CUDA-12` · installs (wheel) · licence: not stated · rank 11347 · last release 2026-09-11 · [PyPI](https://pypi.org/project/OpenMM-CUDA-12/)

### openinference-instrumentation-crewai

OpenInference Crewai Instrumentation

`pip install openinference-instrumentation-crewai` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 11382 · last release 2026-11-04 · [PyPI](https://pypi.org/project/openinference-instrumentation-crewai/)

<details><summary>README extract</summary>

Python auto-instrumentation library for LLM agents implemented with CrewAI

Crews are fully OpenTelemetry-compatible and can be sent to an OpenTelemetry collector for monitoring, such as Arize Phoenix or Arize AX.

Example:
```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from openinference.instrumentation.crewai import CrewAIInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
...
```

Sections: OpenInference crewAI Instrumentation, Quickstart, Event Listener Mode, More Info

</details>

### openapi-python-generator

Openapi Python Generator

`pip install openapi-python-generator` · installs (wheel) · licence: MIT License · rank 11400 · last release 2025-09-29 · [PyPI](https://pypi.org/project/openapi-python-generator/) · [docs](https://openapi-python-generator.readthedocs.io) · [source](https://github.com/MarcoMuellner/openapi-python-generator)

<details><summary>README extract</summary>

[][pypi]
[][status]
[][python version]
[][license]

[][documentation]
[][tests]
[][codecov]

[][pre-commit]
[][black]

Documentation: here

Features:
- Ease of use. Provide input, output and the library, and the generator will do the rest.
- Type safety and type hinting. OpenAPI python generator makes heavy use of pydantic models to provide type-safe data structures. ...

Sections: Openapi Python Generator, Features, Requirements, Usage, Roadmap, Issues

</details>

### ordered-enum

A small library for adding total orderings to enums

`pip install ordered-enum` · installs (wheel) · licence: not stated · rank 11463 · last release 2025-06-23 · [PyPI](https://pypi.org/project/ordered-enum/) · [source](https://github.com/woodruffw/ordered_enum)

<details><summary>README extract</summary>

ordered_enum is a small library for adding (total) orderings to `enum.Enum`s.

It provides two ordering behaviors:

* `ordered_enum.OrderedEnum`: total ordering by definition
* `ordered_enum.ValueOrderedEnum`: "total" ordering by member values

Example:
```python
from ordered_enum import OrderedEnum

class State(OrderedEnum):
    Disabled = 4
    Loaded = 3
    Waiting = 2
    Running = 1
    Dead = 0

assert(State.Disabled < State.Loaded)
assert(sorted([State.Dead, State.Waiting]) == [State.Waiting, State.Dead])
```

Sections: ordered_enum, Usage, Caveats

</details>

### openstep-parser

OpenStep plist reader into python objects

`pip install openstep-parser` · installs (wheel) · licence: MIT · rank 11556 · last release 2025-10-10 · [PyPI](https://pypi.org/project/openstep-parser/)

<details><summary>README extract</summary>

Parse Xcode projects directly using python. It doesn't require system command utilities.

</details>

### ome-zarr-models

A minimal Python package for reading OME-Zarr (meta)data

`pip install ome-zarr-models` · installs (wheel) · licence: MIT License · rank 11692 · last release 2026-09-02 · [PyPI](https://pypi.org/project/ome-zarr-models/) · [docs](https://ome-zarr-models-py.readthedocs.io) · [source](https://github.com/ome-zarr-models/ome-zarr-models-py)

<details><summary>README extract</summary>

A minimal Python package for reading OME-Zarr (meta)data.

See the docs for more info:

</details>

### oslo.reports

oslo.reports library

`pip install oslo.reports` · installs (wheel) · licence: Apache-2.0 · rank 11728 · last release 2026-07-10 · [PyPI](https://pypi.org/project/oslo.reports/) · [source](https://opendev.org/openstack/oslo.reports)

<details><summary>README extract</summary>

When things go wrong in (production) deployments of OpenStack collecting debug
data is a key first step in the process of triaging & ultimately resolving the
problem. Projects like Nova has extensively used logging capabilities which
produce a vast amount of data. ...

</details>

### openlocationcode

Python library for Open Location Code (Plus Codes)

`pip install openlocationcode` · installs from source (sdist only) · licence: Apache 2.0 · rank 11731 · last release 2019-07-20 · [PyPI](https://pypi.org/project/openlocationcode/)

### optopsy

A nimble backtesting and statistics library for options strategies

`pip install optopsy` · does not install on CPython 3.14 · licence: AGPL-3.0-or-later · rank 11736 · last release 2026-03-04 · [PyPI](https://pypi.org/project/optopsy/)

_README extract left out: share-alike licence._

### onepasswordconnectsdk

Python SDK for 1Password Connect

`pip install onepasswordconnectsdk` · installs (wheel) · licence: MIT License · rank 11760 · last release 2026-10-21 · [PyPI](https://pypi.org/project/onepasswordconnectsdk/) · [source](https://github.com/1Password/connect-sdk-python)

<details><summary>README extract</summary>

Access your 1Password items in your Python applications through your self-hosted 1Password Connect server.

The 1Password Connect SDK provides access to 1Password via 1Password Connect hosted in your infrastructure. The library is intended to be used by Python applications to simplify accessing items in 1Password vaults. ...

Example:
```python
from onepasswordconnectsdk.client import (
    Client,
    new_client_from_environment,
)

connect_client: Client = new_client_from_environment()

client.get_item("{item_id}", "{vault_id}")
```

Sections: 1Password Connect SDK for Python, 🪄 See it in action, ✨ Get started

</details>

### opentelemetry-resource-detector-containerid

Container Resource Detector for OpenTelemetry

`pip install opentelemetry-resource-detector-containerid` · installs (wheel) · licence: Apache-2.0 · rank 11771 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-resource-detector-containerid/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library provides custom resource detector for container platforms

Sections: OpenTelemetry Resource detectors for containers, References

</details>

### ophyd-async

Asynchronous Bluesky hardware abstraction code, compatible with control systems like EPICS and Tango

`pip install ophyd-async` · installs (wheel) · licence: BSD License · rank 11782 · last release 2026-09-23 · [PyPI](https://pypi.org/project/ophyd-async/) · [source](https://github.com/bluesky/ophyd-async)

<details><summary>README extract</summary>

Ophyd-async is a Python library for asynchronously interfacing with hardware, intended to be used as an abstraction layer that enables experiment orchestration and data acquisition code to operate above the specifics of particular devices and control systems.

What | Where ...

</details>

### os-traits

A library containing standardized trait strings

`pip install os-traits` · installs (wheel) · licence: Apache Software License · rank 11816 · last release 2026-08-21 · [PyPI](https://pypi.org/project/os-traits/)

<details><summary>README extract</summary>

`os-traits` is an OpenStack library containing standardized trait strings.

Traits are strings that represent a feature of a resource provider hosted by
the Placement service. This library contains the catalog of constants that
have been standardized in the OpenStack community to refer to a particular
hardware, virtualization, storage, network, or ...

</details>

### openenv-core

A unified framework for reinforcement learning environments

`pip install openenv-core` · installs (wheel) · licence: not stated · rank 11891 · last release 2026-05-11 · [PyPI](https://pypi.org/project/openenv-core/)

<details><summary>README extract</summary>

An e2e framework for creating, deploying and using isolated execution environments for agentic RL training, built using Gymnasium style simple APIs.

🚀 Featured Example: Train LLMs to play BlackJack using torchforge (PyTorch's agentic RL framework): `examples/grpo_blackjack/` ...

Features:
OpenEnv provides a standard for interacting with agentic execution environments via simple Gymnasium style APIs - `step()`, `reset()`, `state()`. ...

Example:
```python
import asyncio
from echo_env import CallToolAction, EchoEnv

async def main():
    # Connect to a running Space (async context manager)
    async with EchoEnv(base_url=" as client:
        # Reset the environment
        result = await client.reset()
        print(result.observation.echoed_message)  # "Echo environment ready!"

...
```
...

</details>

### os-ken

A component-based software defined networking framework for OpenStack

`pip install os-ken` · installs (wheel) · licence: Apache Software License · rank 11913 · last release 2026-08-20 · [PyPI](https://pypi.org/project/os-ken/) · [docs](https://docs.openstack.org/os-ken/latest/) · [source](https://opendev.org/openstack/os-ken)

<details><summary>README extract</summary>

A component-based software defined networking framework in OpenStack.

This is a fork of the Ryu library tailored for OpenStack Neutron.

* License: Apache License, Version 2.0

</details>

### openfile

A convenience function that delegates to the appropriate standard library function.

`pip install openfile` · installs (wheel) · licence: MIT License · rank 12019 · last release 2018-09-26 · [PyPI](https://pypi.org/project/openfile/)

<details><summary>README extract</summary>

`openfile` is a trivial Python module that implements a single convenience
function `openfile(filename, mode="rt", **kwargs)` wich delegates the real
work to one of the following standard library functions:

- `gzip.open(filename, mode, **kwargs)` if the file ends with suffix `.gz`; ...

</details>

### openbb-yfinance

yfinance extension for OpenBB

`pip install openbb-yfinance` · installs (wheel) · licence: AGPL-3.0-only · rank 12091 · last release 2026-11-01 · [PyPI](https://pypi.org/project/openbb-yfinance/) · [source](https://github.com/deeleeramone/openbb-danglewood)

_README extract left out: share-alike licence._

### ovsdbapp

A library for creating OVSDB applications

`pip install ovsdbapp` · installs (wheel) · licence: Apache Software License · rank 12167 · last release 2026-10-19 · [PyPI](https://pypi.org/project/ovsdbapp/) · [source](https://opendev.org/openstack/ovsdbapp)

<details><summary>README extract</summary>

A library for creating OVSDB applications

The ovsdbapp library is useful for creating applications that communicate
via Open_vSwitch's OVSDB protocol ( It
wraps the Python `ovs` package and adds an event loop and friendly
transactions. ovsdbapp targets Unix-like systems where Open vSwitch and
`python-ovs` are supported. ...

</details>

### oxylabs

Official Python library for Oxylabs Scraper APIs

`pip install oxylabs` · installs (wheel) · licence: MIT · rank 12262 · last release 2026-03-09 · [PyPI](https://pypi.org/project/oxylabs/)

<details><summary>README extract</summary>

The official Python library for the Oxylabs Scraper APIs.

Collect public data at scale with industry-leading web scraping solutions and the world's largest ethical proxy network.
Documentation can be found at

</details>

### orffinder

Open Reading Frame finder natively coded in Python.

`pip install orffinder` · installs (wheel) · licence: MIT License · rank 12305 · last release 2021-09-14 · [PyPI](https://pypi.org/project/orffinder/)

<details><summary>README extract</summary>

ORFFinder in Python. Inspired by NCBI's version:

Finds the open reading frame (6-frame scan) on a given 5' to 3' nucleotide.

Example:
```python
from Bio import SeqIO
from orffinder import orffinder

sequence = SeqIO.read("gene.fasta", "fasta")
orffinder.getORFs(sequence, minimum_length=75, remove_nested=True)
```

Sections: ORFFinder, Terminal Usage, API Usage, Documentation, Dependencies

</details>

### openhands

OpenHands CLI - Terminal User Interface for OpenHands AI Agent

`pip install openhands` · does not install on CPython 3.14 · licence: MIT · rank 12315 · last release 2026-05-08 · [PyPI](https://pypi.org/project/openhands/)

<details><summary>README extract</summary>

Deutsch |
 Español |
 français |
 日本語 |
 한국어 |
 Português |
 Русский |

Run OpenHands agent inside your terminal, favorite IDE, CI pipelines, local browser, or secure OpenHands Cloud sandboxes.

Sections: OpenHands V1 CLI, (Powered by OpenHands Software Agent SDK), Using uv (Recommended), Executable Binary, Usage, Quick Start, Configuration, Running Modes, Features, MCP Servers, Confirmation Modes, Cloud Conversations, Headless Mode, Resume Conversations

</details>

### oboros

A fast, Rust-powered CLI tool that detects circular imports in Python projects

`pip install oboros` · installs (wheel) · licence: not stated · rank 12337 · last release 2026-08-20 · [PyPI](https://pypi.org/project/oboros/)

### oslo.privsep

OpenStack library for privilege separation

`pip install oslo.privsep` · installs (wheel) · licence: Apache-2.0 · rank 12406 · last release 2026-07-10 · [PyPI](https://pypi.org/project/oslo.privsep/) · [source](https://opendev.org/openstack/oslo.privsep)

<details><summary>README extract</summary>

OpenStack library for privilege separation

This library helps applications perform actions which require more or
less privileges than they were started with in a safe, easy to code
and easy to use manner. ...

</details>

### obspec-utils

Utilities for interacting with object storage, based on obspec

`pip install obspec-utils` · installs (wheel) · licence: Apache-2.0 · rank 12416 · last release 2026-01-28 · [PyPI](https://pypi.org/project/obspec-utils/) · [docs](https://obspec-utils.readthedocs.io) · [source](https://github.com/virtual-zarr/obspec-utils)

### opentelemetry-instrumentation-sklearn

OpenTelemetry sklearn instrumentation

`pip install opentelemetry-instrumentation-sklearn` · installs (wheel) · licence: Apache Software License · rank 12425 · last release 2024-05-31 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-sklearn/)

<details><summary>README extract</summary>

This library allows tracing HTTP requests made by the
scikit-learn library.

Sections: OpenTelemetry Scikit-Learn Instrumentation, References

</details>

### oslo.rootwrap

Oslo Rootwrap

`pip install oslo.rootwrap` · installs (wheel) · licence: Apache-2.0 · rank 12432 · last release 2026-07-10 · [PyPI](https://pypi.org/project/oslo.rootwrap/) · [source](https://opendev.org/openstack/oslo.rootwrap)

<details><summary>README extract</summary>

oslo.rootwrap allows fine-grained filtering of shell commands to run
as `root` from OpenStack services.

* License: Apache License, Version 2.0

</details>

### overturemaps

Python tools for interacting with Overture Maps (overturemaps.org) data.

`pip install overturemaps` · installs (wheel) · licence: MIT · rank 12522 · last release 2026-11-06 · [PyPI](https://pypi.org/project/overturemaps/) · [source](https://github.com/OvertureMaps/overturemaps-py)

<details><summary>README extract</summary>

Official Python command-line tool of the Overture Maps Foundation.

Overture provides free and open geospatial map data, from many different sources and normalized to a
common schema. This tool helps to download Overture data
within a region of interest and converts it to a few different file formats. ...

Sections: overturemaps-py, Quick Start, Commands, Documentation

</details>

### omniverseclient

Omniverse ClientLibrary Python bindings

`pip install omniverseclient` · does not install on CPython 3.14 · licence: not stated · rank 12524 · last release 2026-10-02 · [PyPI](https://pypi.org/project/omniverseclient/) · [docs](https://docs.omniverse.nvidia.com/kit/docs/client_library/latest/index.html)

<details><summary>README extract</summary>

Python bindings for the NVIDIA Omniverse Client Library, which Omniverse applications use to access files on Omniverse Nucleus servers, local disk, and HTTP(S) endpoints through a single URL-based API.

See the Client Library documentation for usage and API reference.

Example:
```python
import omni.client
```

</details>

### openbb-news

RSS news feeds extension for OpenBB

`pip install openbb-news` · installs (wheel) · licence: Apache-2.0 · rank 12553 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-news/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

RSS news feeds for the OpenBB Platform — one Workspace Newsfeed widget backed by
a registry of 500+ vetted feeds (Benzinga, GlobeNewswire by full ICB industry
breakdown + subject/event-type breakdown — earnings, M&A, dividends, IPOs, etc.,
PR Newswire regional + category, Axios, Yahoo Finance, Fortune, BBC, Fox News,
Drudge Report, Drugs.com, ...

Sections: openbb-news, Endpoints, Pluggable feeds — `openbb.toml`, 1. Add or replace feeds — `[news.rss_feeds]`, 2. Pretty provider names — `[news.rss_providers]`, 3. Keep the bundled defaults — `[news] merge_defaults`, Full example, Tests

</details>

### opentelemetry-instrumentation-genai-openai

OpenTelemetry Official OpenAI instrumentation

`pip install opentelemetry-instrumentation-genai-openai` · installs (wheel) · licence: Apache-2.0 · rank 12555 · last release 2026-10-23 · [PyPI](https://pypi.org/project/opentelemetry-instrumentation-genai-openai/) · [source](https://github.com/open-telemetry/opentelemetry-python-genai)

<details><summary>README extract</summary>

This library allows tracing LLM requests and logging of messages made by the
OpenAI Python API library. It also captures
the duration of the operations and the number of tokens used as metrics, and for
streaming chat completions the time to the first chunk and the time between output
chunks.

Many LLM platforms support the OpenAI SDK. ...

Example:
```python
from opentelemetry.instrumentation.genai.openai import OpenAIInstrumentor

OpenAIInstrumentor().instrument()

client = OpenAI()
# Chat completion example
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Write a short poem on open telemetry."},
    ],
)

...
```

...

</details>

### optionlab

Python library for evaluating options trading strategies

`pip install optionlab` · installs (wheel) · licence: not stated · rank 12645 · last release 2026-11-07 · [PyPI](https://pypi.org/project/optionlab/)

<details><summary>README extract</summary>

This package is a lightweight library designed to provide quick evaluation of options trading
strategies. It produces various outputs:

- the profit/loss profile of the strategy on a user-defined target date

- the range of stock prices for which the strategy is profitable (i.e., generating a return of
at least \$0.01) ...

Sections: OptionLab, Contact, Documentation, Disclaimer

</details>

### openbb-fred

FRED provider extension for OpenBB Platform.

`pip install openbb-fred` · installs (wheel) · licence: Apache-2.0 · rank 12673 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-fred/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

`openbb-fred` integrates Federal Reserve Economic Data, the database maintained by the
Research division of the Federal Reserve Bank of St. Louis, into the Open Data Platform by
OpenBB. It reads three St. Louis Fed APIs:

- FRED v1 — ` — series metadata and observations,
 series and release search, and the published release tables. ...

Example:
```python
from openbb import obb

obb.economy.fred_search(
    query="retail sales",
    search_type="full_text",
    order_by="observation_end",
    sort_order="desc",
    limit=25,
    provider="fred",
).to_df()
```

...

</details>

### openbb-sec

SEC provider extension for OpenBB Platform.

`pip install openbb-sec` · installs (wheel) · licence: Apache-2.0 · rank 12781 · last release 2026-09-29 · [PyPI](https://pypi.org/project/openbb-sec/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

Free, key-less access to U.S. SEC EDGAR data for the OpenBB Platform — filings, financial statements, fund holdings, ownership, and full-text search, with a built-in OpenBB Workspace backend.

No credentials or API key required. Responses are persisted to a local disk cache so repeated queries are fast and offline-friendly.

Example:
```python
from openbb import obb

# Resolve identifiers
obb.sec.cik_map(symbol="AAPL")
obb.sec.symbol_map(query="0000320193")

# Filings and full-text search
obb.sec.company_filings(symbol="AAPL", form_type="10-K")
obb.sec.full_text_search(query="climate change", form_type="8-K")

# 10-K / 10-Q content (defaults to the latest filing)
...
```

Sections: OpenBB SEC Provider, Quick start, Coverage, Basic usage, OpenBB Workspace, Cache management, Documentation

</details>

### openenv

A unified framework for reinforcement learning environments

`pip install openenv` · installs (wheel) · licence: BSD-3-Clause · rank 12862 · last release 2026-11-05 · [PyPI](https://pypi.org/project/openenv/)

<details><summary>README extract</summary>

An end-to-end framework for creating, deploying and using isolated execution environments for agentic RL, with a simple Gymnasium-style API.

- One API for every environment. `reset()`, `step()` and `state()`, sync or async, over a WebSocket.
- Isolated, deployable environments. ...

Example:
```python
import asyncio
from echo_env import CallToolAction, EchoEnv

async def main():
    # Connect to a running Space (async context manager)
    async with EchoEnv(base_url=" as client:
        # Reset the environment
        result = await client.reset()
        print(result.observation.metadata["message"])  # "Echo environment ready!"

...
```

...

</details>

### openbb-equity

Equity extension for OpenBB

`pip install openbb-equity` · installs (wheel) · licence: Apache-2.0 · rank 12868 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-equity/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

This extension provides equity market data tools for the OpenBB Platform.

Features of the Equity extension include:

- Access to various equity market data sources

 - `calendar` for equity-specific events
 - `compare` for peer analysis
 - `darkpool` for dark pool shorts data
 - `discovery` for equity discovery
 - `estimates` for analyst ...

</details>

### ompl

The Open Motion Planning Library

`pip install ompl` · does not install on CPython 3.14 · licence: BSD-3-Clause · rank 12918 · last release 2026-06-23 · [PyPI](https://pypi.org/project/ompl/)

<details><summary>README extract</summary>

Example:
```python
m.attr("ATLAS_STATE_SPACE_SAMPLES") = nb::cast(ompl::magic::ATLAS_STATE_SPACE_SAMPLES);
m.attr("ATLAS_STATE_SPACE_EPSILON") = nb::cast(0.05);
m.attr("ATLAS_STATE_SPACE_RHO_MULTIPLIER") = nb::cast(5);
m.attr("ATLAS_STATE_SPACE_ALPHA") = nb::cast(boost::math::constants::pi<double>() / 8.0);
m.attr("ATLAS_STATE_SPACE_EXPLORATION") = nb::cast(0.75);
...
```

Sections: OMPL Python Bindings, How to use Python binding, How is Nanobind organized?, Adding new bindings, General Instructions, Binding "OMPL::Magic" constants, Note on ARM platforms

</details>

### openbb-platform-api

OpenBB Platform API: launcher and widgets builder for the Open Data Platform REST API and OpenBB Workspace custom-backend connector.

`pip install openbb-platform-api` · installs (wheel) · licence: Apache-2.0 · rank 12936 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-platform-api/) · [docs](https://docs.openbb.co/odp/python/extensions/interface/openbb-api) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

Launcher and widgets builder for the OpenBB Workspace custom backend. Wraps any FastAPI application with the metadata, exception handling, and `widgets.json` generation that OpenBB Workspace expects — so a regular FastAPI app becomes a Workspace data source with no glue code. ...

Example:
```python
from fastapi import FastAPI
from openbb_platform_api.response_models import (
    Data,
    MetricResponseModel,
    OmniWidgetResponseModel,
    PdfResponseModel,
)

app = FastAPI()

# Markdown — return a string
@app.get("/hello")
async def hello() -> str:
    """Tooltip from the docstring."""
    return "Hello, OpenBB!"

...
```

...

</details>

### ogbench

OGBench: Benchmarking Offline Goal-Conditioned RL

`pip install ogbench` · installs (wheel) · licence: MIT License · rank 12977 · last release 2026-10-26 · [PyPI](https://pypi.org/project/ogbench/)

### openapi

Python OpenAPI 2.0 (Swagger) object model

`pip install openapi` · installs (wheel) · licence: not stated · rank 13024 · last release 2024-06-17 · [PyPI](https://pypi.org/project/openapi/)

### OpenGeode-core

Open source framework for representing and manipulating geometric models

`pip install OpenGeode-core` · installs (wheel) · licence: MIT · rank 13032 · last release 2026-11-08 · [PyPI](https://pypi.org/project/OpenGeode-core/)

<details><summary>README extract</summary>

OpenGeode is an open source framework for representing and manipulating geometric models, from simple meshes to complex boundary representations. The framework is easy to use thanks to its readable API and its Python bindings for quick prototyping. It is the industrialization of a 5-year research prototype platform RINGMesh.

Sections: OpenGeodeby Geode-solutions, Introduction, Ecosystem, Documentation, Questions

</details>

### openinference-instrumentation-vertexai

OpenInference VertexAI Instrumentation

`pip install openinference-instrumentation-vertexai` · installs (wheel) · licence: Apache-2.0 · rank 13066 · last release 2026-11-04 · [PyPI](https://pypi.org/project/openinference-instrumentation-vertexai/)

<details><summary>README extract</summary>

Python auto-instrumentation library for VertexAI SDK and the Google Cloud AI Platform. Traces are fully OpenTelemetry compatible and can be sent to any OpenTelemetry collector for viewing, such as Arize Phoenix or Arize AX.

Example:
```python
from openinference.instrumentation.vertexai import VertexAIInstrumentor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

endpoint = "
tracer_provider = TracerProvider()
...
```

Sections: OpenInference Google VertexAI Instrumentation, Quickstart, More Info

</details>

### openstep-plist

ASCII plist parser written in Cython

`pip install openstep-plist` · installs (wheel) · licence: MIT · rank 13118 · last release 2026-03-11 · [PyPI](https://pypi.org/project/openstep-plist/)

<details><summary>README extract</summary>

A parser for the "old style" OpenStep property list format (also known as ASCII
plist), written in Cython.
Largely based on the CoreFoundation implementation found here:

</details>

### OMPython

OpenModelica-Python API Interface

`pip install OMPython` · installs (wheel) · licence: not stated · rank 13173 · last release 2026-09-01 · [PyPI](https://pypi.org/project/OMPython/) · [docs](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/ompython.html) · [source](https://github.com/OpenModelica/OMPython)

<details><summary>README extract</summary>

OMPython is a Python interface that uses ZeroMQ to communicate with OpenModelica.

 - Python >= 3.10; Python >= 3.12 for `OMPath` functionality (handle file system access via OMC using a `pathlib.Path` compatible abstraction layer)
 - Additional packages: numpy, psutil, pyparsing and pyzmq

Example:
```python
import OMPython
help(OMPython)
```

Sections: OMPython, Dependencies, Via pip, Via conda, Via source, Usage, Bug Reports, Contact

</details>

### openbb-bls

BLS provider extension for OpenBB Platform.

`pip install openbb-bls` · installs (wheel) · licence: Apache-2.0 · rank 13319 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-bls/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

`openbb-bls` integrates the U.S. Bureau of Labor Statistics into the OpenBB
Platform. It combines three data paths:

- BLS Public Data API v2 — point-in-time time series by series ID (the only
 endpoint that can use an API key). ...

Example:
```python
from openbb import obb

# Latest CPI-U expenditure-category table (no key required)
obb.bls.cpi.t1_expenditure_category(provider="bls").to_df()

# A specific time series from the BLS Public Data API
obb.bls.series(symbol="CUUR0000SA0", provider="bls").to_df()

# Find series in the local catalog, then chart one
...
```

...

</details>

### os-resource-classes

Resource Classes for OpenStack

`pip install os-resource-classes` · installs (wheel) · licence: Apache Software License · rank 13325 · last release 2021-07-15 · [PyPI](https://pypi.org/project/os-resource-classes/)

<details><summary>README extract</summary>

A list of standardized resource classes for OpenStack.

A resource class is a distinct type of inventory that exists in
a cloud environment, for example `VCPU`, `DISK_GB`. They are
upper case with underscores. They often include a unit in their
name. ...

</details>

### od

Shorthand syntax for building OrderedDicts

`pip install od` · installs (wheel) · licence: MIT · rank 13424 · last release 2022-02-07 · [PyPI](https://pypi.org/project/od/)

<details><summary>README extract</summary>

The `od` package adds a shorthand syntax to create instances of OrderedDict
You can also use it like the regular constructor for `OrderedDict`:
Install this package using pip:

Example:
```python
>>> import od
>>>
>>> od["cat": "fish", "mouse": "cheese"]
OrderedDict([('cat', 'fish'), ('mouse', 'cheese')])
>>> od["mouse": "cheese", "cat": "fish"]
OrderedDict([('mouse', 'cheese'), ('cat', 'fish')])
```

</details>

### os-vif

A library for plugging and unplugging virtual interfaces in OpenStack.

`pip install os-vif` · installs (wheel) · licence: Apache Software License · rank 13478 · last release 2026-10-09 · [PyPI](https://pypi.org/project/os-vif/) · [source](https://opendev.org/openstack/os_vif)

<details><summary>README extract</summary>

A library for plugging and unplugging virtual interfaces in OpenStack.

* License: Apache License, Version 2.0

</details>

### openbb-economy

Economy extension for OpenBB

`pip install openbb-economy` · installs (wheel) · licence: Apache-2.0 · rank 13482 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-economy/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

The Economy extension provides global macroeconomic data access for the OpenBB Platform.

</details>

### opencensus-ext-sqlalchemy

OpenCensus SQLAlchemy Integration

`pip install opencensus-ext-sqlalchemy` · installs (wheel) · licence: Apache Software License · rank 13490 · last release 2021-10-05 · [PyPI](https://pypi.org/project/opencensus-ext-sqlalchemy/)

<details><summary>README extract</summary>

You can trace usage of the sqlalchemy package, regardless of the underlying
database, by specifying `'sqlalchemy'` to `trace_integrations`.

Example:
```python
from opencensus.trace import config_integration

config_integration.trace_integrations(['sqlalchemy'])
```

Sections: OpenCensus SQLAlchemy Integration, Usage, References

</details>

### openbb-federal-reserve

US Federal Reserve provider extension for OpenBB. Data, documents, indicators, and research from the Federal Reserve System, FOMC, FRB, and twelve regional districts.

`pip install openbb-federal-reserve` · installs (wheel) · licence: Apache-2.0 · rank 13544 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-federal-reserve/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

This extension integrates Federal Reserve data into the OpenBB Platform: Federal Reserve Board statistics not published to FRED, research and survey data from the twelve regional Reserve Banks, and FFIEC bank-supervision and regulatory reports. No authorization is required for access. ...

Sections: OpenBB Federal Reserve Provider, Quick Start, Start Server, Add to Workspace, Coverage, Apps, Endpoints

</details>

### openbb-oecd

OECD provider extension for OpenBB Platform.

`pip install openbb-oecd` · installs (wheel) · licence: Apache-2.0 · rank 13563 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-oecd/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

This package adds the `openbb-oecd` provider extension to the Open Data Platform by OpenBB.

It provides everything you need — endpoints, tools, and metadata — to access and explore the entirety of
< without any previous experience working with it.

Example:
```python
from openbb import obb

# List all available OECD indicators to find what you need
indicators = obb.economy.available_indicators(provider="oecd", query="GDP")
print(indicators.to_df())

# Fetch real GDP growth for the US, UK, and Germany
data = obb.economy.indicators(
    provider="oecd",
    symbol="DF_QNA::B1GQ",
    country="USA,GBR,DEU",
...
```

...

</details>

### openbb-imf

IMF provider extension for OpenBB Platform.

`pip install openbb-imf` · installs (wheel) · licence: Apache-2.0 · rank 13621 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-imf/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

This package adds the `openbb-imf` provider extension to the Open Data Platform by OpenBB.

It provides everything you need - endpoints, tools, and metadata - to access and explore the entirety of
< without any previous experience working with it.

Example:
```python
from openbb import obb

indicators = obb.economy.available_indicators(provider="imf", dataflows="CPI,PI")

print(indicators.to_dict("records"))
```

Sections: OpenBB IMF Provider Extension, Quick Start, Start Server, Add to Workspace, Click to Open App, Implementation Details, Indicators, Presentation Tables, Symbology, Coverage, Endpoints

</details>

### openbb

Investment research for everyone, anywhere.

`pip install openbb` · installs (wheel) · licence: Apache-2.0 · rank 13648 · last release 2026-09-29 · [PyPI](https://pypi.org/project/openbb/) · [docs](https://docs.openbb.co) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

The OpenBB Platform is a set of Python packages that turn financial and economic data sources into one typed Python client (`from openbb import obb`), a FastAPI REST API, and an MCP server.

`openbb-core` is the runtime. ...

Example:
```python
from openbb import obb

output = obb.equity.price.historical("AAPL", provider="cboe")
df = output.to_dataframe()
```

Sections: OpenBB Platform, Repository layout, Packages, Core and tooling, Routers, Providers, OBBject extensions, Python, Credentials, REST API, MCP server

</details>

### otree-core

(no summary)

`pip install otree-core` · installs from source (sdist only) · licence: MIT · rank 13717 · last release 2020-10-07 · [PyPI](https://pypi.org/project/otree-core/)

### openinference-instrumentation-smolagents

OpenInference smolagents Instrumentation

`pip install openinference-instrumentation-smolagents` · installs (wheel) · licence: Apache-2.0 · rank 13799 · last release 2026-11-04 · [PyPI](https://pypi.org/project/openinference-instrumentation-smolagents/)

<details><summary>README extract</summary>

Python auto-instrumentation library for LLM agents implemented with smolagents

Crews are fully OpenTelemetry-compatible and can be sent to an OpenTelemetry collector for monitoring, such as Arize Phoenix or Arize AX.

Example:
```python
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
```

Sections: OpenInference smolagents Instrumentation, Quickstart, Manual instrumentation, More Info

</details>

### openbb-cftc

CFTC and DTCC Public Price Dissemination data integration for OpenBB Platform.

`pip install openbb-cftc` · installs (wheel) · licence: Apache-2.0 · rank 13806 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-cftc/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

This package provides full access to the CFTC Commitment of Traders database.
Reports are fetched by CFTC Code (e.g. `13874+`) and returns the full history of the contract.

It also exposes the swap transaction and pricing data published by DTCC's Public Price
Dissemination service — the swap data repository for CFTC-jurisdiction trades — ...

Features:
`spread` is disseminated, so it is surfaced — raw, as reported. But reading it as "the CDS
spread" is wrong twice over.

First, the spec makes it a conditional alternative, not a price: it is required only when
there is no fixed rate and no upfront. ...

Example:
```python
from openbb import obb

search_results = obb.cftc.cot_search(query="gold")

print(search_results.to_df())
```

...

</details>

### openbb-crypto

Crypto extension for OpenBB

`pip install openbb-crypto` · installs (wheel) · licence: Apache-2.0 · rank 13836 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-crypto/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

This extension provides a set of commands for crypto data retrieval.

</details>

### openbb-government-us

US Government data extensions for OpenBB Platform, one provider per agency.

`pip install openbb-government-us` · installs (wheel) · licence: Apache-2.0 · rank 13843 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-government-us/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

This package integrates US Government data sources into the OpenBB Platform, organized as one provider per federal agency. A single install:

registers three providers - `congress_gov`, `us_treasury`, and `usda` - plus two API routers, `obb.uscongress` and `obb.ustreasury`. ...

Example:
```python
from openbb import obb

bills = obb.uscongress.bills(congress=118, bill_type="s", provider="congress_gov")
```

Sections: OpenBB US Government Provider Extensions, Congress, Treasury, USDA, Usage

</details>

### openbb-us-eia

U.S. Energy Information Administration (EIA) provider extension for OpenBB Platform.

`pip install openbb-us-eia` · installs (wheel) · licence: Apache-2.0 · rank 13848 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-us-eia/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

This module integrates the EIA data provider into the OpenBB Platform,
exposing the EIA Open Data APIv2 as a set of typed router
endpoints under `obb.eia`, plus the Weekly Petroleum Status Report and Short Term Energy
Outlook models.

Example:
```python
from openbb import obb

obb.user.credentials.eia_api_key = "REPLACE_WITH_YOUR_KEY"
```

Sections: OpenBB EIA Provider Extension, PyPI, From Source, `user_settings.json`, Current Python Session, Coverage, API Dataset Endpoints, Discovery Endpoints, Reports, The Metadata Cache and Generated Models

</details>

### openbb-currency

Currency extension for OpenBB

`pip install openbb-currency` · installs (wheel) · licence: Apache-2.0 · rank 13892 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-currency/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

This extension provides currency exchange related data for the OpenBB Platform.

</details>

### onelogin

OneLogin API Python SDK

`pip install onelogin` · installs (wheel) · licence: NoLicense · rank 13941 · last release 2026-07-02 · [PyPI](https://pypi.org/project/onelogin/) · [source](https://github.com/onelogin/onelogin-python-sdk)

<details><summary>README extract</summary>

Official Python SDK for the OneLogin API. Manage users, roles, groups, apps, and authentication programmatically.

API reference: OneLogin API Documentation.
Per-endpoint docs: see `docs/` in this repo.

Example:
```python
import os
import onelogin
from pprint import pprint

configuration = onelogin.Configuration(
    host="
    username=os.environ["ONELOGIN_CLIENT_ID"],
    password=os.environ["ONELOGIN_CLIENT_SECRET"],
)

with onelogin.ApiClient(configuration) as api_client:
    # Exchange client credentials for an access token.
...
```

Sections: onelogin-python-sdk, Requirements, Getting Started, Authentication, Tests, Troubleshooting

</details>

### os-brick

OpenStack Cinder brick library for managing local volume attaches

`pip install os-brick` · installs (wheel) · licence: Apache Software License · rank 13953 · last release 2026-08-24 · [PyPI](https://pypi.org/project/os-brick/) · [source](https://opendev.org/openstack/os-brick)

<details><summary>README extract</summary>

OpenStack Cinder brick library for managing local volume attaches

Features:
* Discovery of volumes being attached to a host for many transport protocols.
* Removal of volumes from a host.

Sections: Team and repository tags, brick, Features, Hacking

</details>

### openapi3

Client and Validator of OpenAPI 3 Specifications

`pip install openapi3` · installs (wheel) · licence: BSD 3-Clause License · rank 13997 · last release 2023-08-29 · [PyPI](https://pypi.org/project/openapi3/)

<details><summary>README extract</summary>

A Python OpenAPI 3 Specification client and validator for Python 3.

This module can be run against a spec file to validate it like so:

Example:
```python
from openapi3 import OpenAPI
import yaml

# load the spec file and read the yaml
with open('openapi.yaml') as f:
    spec = yaml.safe_load(f.read())

# parse the spec into python - this will raise if the spec is invalid
api = OpenAPI(spec)

# call operations and receive result models
regions = api.call_getRegions()

...
```

Sections: openapi3, Validation Mode, Usage as a Client, Running Tests, Roadmap

</details>

### omniopt2

Automatic highly parallelized hyperparameter optimizer based on Ax/Botorch

`pip install omniopt2` · installs (wheel) · licence: not stated · rank 14008 · last release 2026-11-04 · [PyPI](https://pypi.org/project/omniopt2/)

<details><summary>README extract</summary>

OmniOpt2 is a highly parallel hyperparameter optimizer for Linux, SLURM
clusters, and local workstations. It explores a parameter search space, runs
your program with the proposed parameters, reads a result from its output, and
uses Ax/BoTorch, Optuna, or other generators to decide what to try next. ...

Features:
- GUI and CLI: build a complete `omniopt` command in the browser or use the
 CLI directly.
- SLURM and local execution: workers run as SLURM jobs when `sbatch` is
 available, otherwise locally through submitit's local executor. ...

...

</details>

### opentelemetry-exporter-otlp-json-file

OpenTelemetry JSON File Exporter

`pip install opentelemetry-exporter-otlp-json-file` · installs (wheel) · licence: Apache-2.0 · rank 14032 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-exporter-otlp-json-file/) · [source](https://github.com/open-telemetry/opentelemetry-python)

<details><summary>README extract</summary>

This library exports telemetry as OTLP JSON to a file-like text stream, such
as a file or stdout.

The exporter writes newline delimited OTLP JSON records for file-based
collection workflows.

Sections: OpenTelemetry JSON File Exporter, References

</details>

### otel-instrumentation-nats

OpenTelemetry auto-instrumentation for nats-py

`pip install otel-instrumentation-nats` · installs (wheel) · licence: not stated · rank 14053 · last release 2026-04-07 · [PyPI](https://pypi.org/project/otel-instrumentation-nats/) · [source](https://github.com/tintty1/otel-instrumentation-nats)

<details><summary>README extract</summary>

OpenTelemetry auto-instrumentation for nats-py.

Automatically creates spans for NATS publish, subscribe, request-reply, and JetStream operations with distributed trace context propagation through message headers.

Example:
```python
import asyncio
import nats
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

from otel_instrumentation_nats import NatsInstrumentor

async def main():
    # Set up OpenTelemetry
    provider = TracerProvider()
...
```

...

</details>

### openbb-benzinga

Benzinga extension for OpenBB

`pip install openbb-benzinga` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 14108 · last release 2026-05-26 · [PyPI](https://pypi.org/project/openbb-benzinga/)

_README extract left out: share-alike licence._

### ovs-dbg

OVS Debug contains scripts and libraries that help debug OVS and OVN

`pip install ovs-dbg` · installs (wheel) · licence: Apache Software License · rank 14110 · last release 2023-07-17 · [PyPI](https://pypi.org/project/ovs-dbg/) · [source](https://github.com/amorenoz/ovs-dbg)

<details><summary>README extract</summary>

Scripts to help debug OVS and OVN

Full documentation here:

Sections: ovs-dbg, Available tools, ovs-ofparse, ovs-lgrep, ovs-offline

</details>

### opentelemetry-exporter-credential-provider-gcp

GCP OTLP Exporter Credential Provider for OpenTelemetry

`pip install opentelemetry-exporter-credential-provider-gcp` · installs (wheel) · licence: Apache-2.0 · rank 14124 · last release 2026-10-29 · [PyPI](https://pypi.org/project/opentelemetry-exporter-credential-provider-gcp/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

This library provides support for supplying your machine's Application Default Credentials (
to the OTLP Exporters created automatically by OpenTelemetry Python's auto instrumentation.
These credentials authorize OTLP traces to be sent to `telemetry.googleapis.com`. ...

Sections: OpenTelemetry GCP Credential Provider for OTLP Exporters, Usage, References

</details>

### OpenGeode-IO

Implementation of input and output formats for OpenGeode

`pip install OpenGeode-IO` · installs (wheel) · licence: MIT · rank 14162 · last release 2026-10-31 · [PyPI](https://pypi.org/project/OpenGeode-IO/)

<details><summary>README extract</summary>

OpenGeode-IO provides input and output formats for [OpenGeode] models and meshes.

Sections: OpenGeode-IOby Geode-solutions, Input/Output formats for OpenGeode, Introduction, Documentation, Questions

</details>

### oathtool

One-time password generator

`pip install oathtool` · installs (wheel) · licence: MIT · rank 14187 · last release 2025-05-03 · [PyPI](https://pypi.org/project/oathtool/) · [source](https://github.com/jaraco/oathtool)

<details><summary>README extract</summary>

TOTP code generator based on oathtool.

Example:
```python
>>> oathtool.generate_otp(key)
```

</details>

### onnx-tool

A tool for parsing, editing, optimizing, and profiling ONNX models.

`pip install onnx-tool` · installs (wheel) · licence: MIT · rank 14192 · last release 2026-04-19 · [PyPI](https://pypi.org/project/onnx-tool/)

<details><summary>README extract</summary>

📄 简体中文 | ✨ New Project: AI-Enhancement-Filter (powered by onnx-tool)

A comprehensive toolkit for analyzing, optimizing, and transforming ONNX models with advanced capabilities for LLMs, diffusion models, and computer vision architectures.

- LLM Optimization: Build and profile large language models with KV cache analysis (example) ...

Example:
```python
from onnx_tool import Model

model = Model('model.onnx')          # Load any ONNX file
graph = model.graph                  # Access computation graph
node = graph.nodemap['Conv_0']       # Modify operator attributes
tensor = graph.tensormap['weight']   # Edit tensor data/types
model.save_model('modified.onnx')    # Persist changes
```

...

</details>

### openfeed

Barchart Openfeed Example Client for Python

`pip install openfeed` · installs (wheel) · licence: MIT · rank 14241 · last release 2023-09-20 · [PyPI](https://pypi.org/project/openfeed/)

<details><summary>README extract</summary>

This SDK encapuslates the openfeed proto objects and faciliates client connections to openfeed servers.

Example:
```python
import openfeed

# new client with credentials
of_client = openfeed.OpenfeedClient("username", "password")

# optional state handlers
of_client.on_error = lambda x: print("Error:", x)
of_client.on_connected = lambda x: print("Connected")
of_client.on_disconnected = lambda x: print("Disconnected")

# attach a global message handler
...
```

Sections: Openfeed SDK for Python, Example Usage, Expected Output, Openfeed Documentation, Subscription Types, OHLC

</details>

### opset

A library for simplifying the configuration of Python applications at all stages of deployment.

`pip install opset` · installs (wheel) · licence: Apache-2.0 · rank 14295 · last release 2026-02-27 · [PyPI](https://pypi.org/project/opset/)

<details><summary>README extract</summary>

A library for simplifying the configuration of Python applications at all stages of deployment.

Opset is a config manager that let you manage your configuration via YAML file or environment variables. ...

Example:
```python
from opset import OpsetSettingsMainModel, Config

class MyConfig(OpsetSettingsMainModel):
    host: str
    port: int = 8080

config = Config("my-app", MyConfig, "my_app.config").config
```

Sections: Opset, Lexicon, Architecture Overview, Usage Guide, Making the difference between null and empty, Controlling your entry points, Opset + Google Cloud Secret Manager, Determining the project automatically, Combined secrets, Project Mapping, Example Configuration file, local.yml, Example Logging Configuration values, Log Processors

</details>

### openbb-etf

ETF extension for OpenBB

`pip install openbb-etf` · installs (wheel) · licence: Apache-2.0 · rank 14305 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-etf/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

This extension provides a set of commands for ETF data retrieval.

</details>

### openbb-derivatives

Derivatives extension for OpenBB

`pip install openbb-derivatives` · installs (wheel) · licence: Apache-2.0 · rank 14310 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-derivatives/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

This extension provides derivatives data for the OpenBB Platform.

</details>

### openbb-index

Index extension for OpenBB

`pip install openbb-index` · installs (wheel) · licence: Apache-2.0 · rank 14311 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-index/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

The Index extension provides global and european index data access for the OpenBB Platform.

</details>

### openbb-fixedincome

Fixed income extension for OpenBB

`pip install openbb-fixedincome` · installs (wheel) · licence: Apache-2.0 · rank 14319 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-fixedincome/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

This extension provides fixed income data for the OpenBB Platform.

Features of the Fixed Income extension include information on government bonds and central bank rates.

</details>

### openbb-fmp

FMP extension for OpenBB

`pip install openbb-fmp` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 14330 · last release 2026-05-26 · [PyPI](https://pypi.org/project/openbb-fmp/)

_README extract left out: share-alike licence._

### openbb-commodity

Commodity extension for OpenBB

`pip install openbb-commodity` · installs (wheel) · licence: Apache-2.0 · rank 14543 · last release 2026-09-28 · [PyPI](https://pypi.org/project/openbb-commodity/) · [source](https://github.com/OpenBB-finance/OpenBB)

<details><summary>README extract</summary>

This extension provides a set of commands for commodity-related data.

</details>

### openbb-regulators

Markets and Agency Regulators extension for OpenBB

`pip install openbb-regulators` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 14566 · last release 2026-05-26 · [PyPI](https://pypi.org/project/openbb-regulators/)

_README extract left out: share-alike licence._

### openbb-intrinio

Intrinio extension for OpenBB

`pip install openbb-intrinio` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 14567 · last release 2026-05-26 · [PyPI](https://pypi.org/project/openbb-intrinio/)

_README extract left out: share-alike licence._

### openbb-tiingo

Tiingo extension for OpenBB

`pip install openbb-tiingo` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 14576 · last release 2026-05-26 · [PyPI](https://pypi.org/project/openbb-tiingo/)

_README extract left out: share-alike licence._

### openbb-tradingeconomics

Trading Economics extension for OpenBB

`pip install openbb-tradingeconomics` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 14587 · last release 2026-05-26 · [PyPI](https://pypi.org/project/openbb-tradingeconomics/)

_README extract left out: share-alike licence._

### open-terminal

A remote computer API.

`pip install open-terminal` · installs (wheel) · licence: MIT · rank 14628 · last release 2026-11-08 · [PyPI](https://pypi.org/project/open-terminal/)

<details><summary>README extract</summary>

A computer for your AI agents. Run commands, search and manage files, execute code, and work with browsers and desktops through a self-hosted REST API. Connect it to Open WebUI, or use it with your own tools.

Documentation · Changelog · Report an issue

Sections: Open Terminal, Docker, Python, Private local IPC, Connect to Open WebUI, Configuration, Coding agents in chat, Server settings, Multi-user deployments

</details>

### openbb-econdb

EconDB extension for OpenBB

`pip install openbb-econdb` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 14698 · last release 2026-05-26 · [PyPI](https://pypi.org/project/openbb-econdb/)

_README extract left out: share-alike licence._

### openfermionpyscf

A plugin allowing OpenFermion to interface with PySCF.

`pip install openfermionpyscf` · installs (wheel) · licence: Apache 2 · rank 14711 · last release 2020-12-22 · [PyPI](https://pypi.org/project/openfermionpyscf/)

<details><summary>README extract</summary>

OpenFermion is an open source library (licensed under Apache 2) for compiling and analyzing quantum algorithms which simulate fermionic systems.
This plugin library allows the electronic structure package PySCF (licensed under BSD-2-Clause) to interface with OpenFermion.

Sections: OpenFermion-PySCF, Disclaimer

</details>

### opencensus-ext-flask

OpenCensus Flask Integration

`pip install opencensus-ext-flask` · installs (wheel) · licence: Apache Software License · rank 14762 · last release 2023-03-10 · [PyPI](https://pypi.org/project/opencensus-ext-flask/)

<details><summary>README extract</summary>

Example:
```python
from flask import Flask
from opencensus.ext.flask.flask_middleware import FlaskMiddleware

app = Flask(name)
middleware = FlaskMiddleware(app, excludelist_paths=['_ah/health'])

@app.route('/')
def hello():
    return 'Hello World!'

if name == 'main':
    import logging
    logger = logging.getLogger('werkzeug')
    logger.setLevel(logging.ERROR)
...
```

Sections: OpenCensus Flask Integration, Usage, References

</details>

### opening_hours_py

A parser for the opening_hours fields from OpenStreetMap.

`pip install opening_hours_py` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 14786 · last release 2026-11-04 · [PyPI](https://pypi.org/project/opening_hours_py/)

<details><summary>README extract</summary>

[][pypi]
[][docs]
[][pypi]
[][codecov]
[][demo-website]

Features:
- 📝 Parsing for OSM opening hours
- 🧮 Evaluation of state and next change
- ⏳ Lazy infinite iterator
- 🌅 Accurate sun events
- 📅 Embedded public holidays database for many countries (from [nager])
- 🌍 Timezone support ...

Example:
```python
from opening_hours import OpeningHours

oh = OpeningHours("Mo-Fr 10:00-18:00; Sa-Su 10:00-12:00")
print("Current status is", oh.state())
print("This will change at", oh.next_change())

# You can also attach a timezone to your expression. If you use timezone-aware
# dates, they will be converted to local time before any computation is done.
...
```

Sections: Python bindings for OSM Opening Hours, Usage, Features, Limitations

</details>

### OpenGeode-GeosciencesIO

Input/Output formats for OpenGeode-Geosciences

`pip install OpenGeode-GeosciencesIO` · installs (wheel) · licence: MIT · rank 14818 · last release 2026-11-08 · [PyPI](https://pypi.org/project/OpenGeode-GeosciencesIO/)

<details><summary>README extract</summary>

OpenGeode-GeosciencesIO provides input and output formats for [OpenGeode-Geosciences] objects.

Sections: OpenGeode-GeosciencesIOby Geode-solutions, Input/Output formats for OpenGeode-Geosciences, Introduction, Documentation, Questions

</details>

### oslo.limit

Limit enforcement library to assist with quota calculation.

`pip install oslo.limit` · installs (wheel) · licence: Apache-2.0 · rank 14828 · last release 2026-07-10 · [PyPI](https://pypi.org/project/oslo.limit/) · [source](https://opendev.org/openstack/oslo.limit)

<details><summary>README extract</summary>

Oslo.limit is the limit enforcement library to assist with quota calculation.
It aims to provide support for quota enforcement across all OpenStack services.

* Free software: Apache license

</details>

### osc-placement

OpenStackClient plugin for the Placement service

`pip install osc-placement` · installs (wheel) · licence: Apache Software License · rank 14841 · last release 2026-08-28 · [PyPI](https://pypi.org/project/osc-placement/)

<details><summary>README extract</summary>

OpenStackClient plugin for the Placement service

This is an OpenStackClient plugin, that provides CLI for the Placement service.
Python API binding is not implemented - Placement API consumers are encouraged
to use the REST API directly, CLI is provided only for convenience of users.

* Free software: Apache license

</details>

### ovos-config

ovos-core configuration module

`pip install ovos-config` · installs (wheel) · licence: Apache-2.0 · rank 14878 · last release 2025-06-18 · [PyPI](https://pypi.org/project/ovos-config/)

<details><summary>README extract</summary>

helper package to interact with mycroft config

Sections: OVOS-config, Command Line usage

</details>

### oslo.vmware

Oslo VMware library

`pip install oslo.vmware` · installs (wheel) · licence: Apache Software License · rank 14879 · last release 2026-08-24 · [PyPI](https://pypi.org/project/oslo.vmware/) · [source](https://opendev.org/openstack/oslo.vmware)

### opendp

Python bindings for the OpenDP Library

`pip install opendp` · installs (wheel) · licence: MIT · rank 14883 · last release 2026-10-06 · [PyPI](https://pypi.org/project/opendp/) · [docs](https://docs.opendp.org/) · [source](https://github.com/opendp/opendp)

<details><summary>README extract</summary>

The OpenDP Library is a modular collection of statistical algorithms that adhere to the definition of
differential privacy.
It can be used to build applications of privacy-preserving computations, using a number of different models of privacy.
OpenDP is implemented in Rust, with bindings for easy use from Python and R. ...

Sections: Documentation, Getting Help

</details>

### openbb-congress-gov

Congress.gov Provider Extension for the OpenBB Platform

`pip install openbb-congress-gov` · installs (wheel) · licence: not stated · rank 14884 · last release 2026-05-26 · [PyPI](https://pypi.org/project/openbb-congress-gov/)

<details><summary>README extract</summary>

This provider integrates with the Congress.gov API to provide access to U.S. legislative data and text.

Example:
```python
from openbb import obb

obb.user.credentials.congress_gov_api_key = "YOUR KEY"
```

Sections: Congress.gov Provider, Features, Congress Bills, Bill Summaries & Metadata, Bill Text URLs and Downloads, OpenBB Workspace Application, Configuration, Congress.gov API Key, Entering Credentials, Coverage, Bill Text, Usage Examples, Fetching Recent Bills, Getting Bill Summaries

</details>

### OpenGeode-Inspector

Open source framework for inspecting the validity of geometric models

`pip install OpenGeode-Inspector` · installs (wheel) · licence: MIT · rank 14919 · last release 2026-11-08 · [PyPI](https://pypi.org/project/OpenGeode-Inspector/)

<details><summary>README extract</summary>

OpenGeode-Inspector is a module of [OpenGeode] providing ways of inspecting your meshes and models and verifying their validity.

Sections: OpenGeode-Inspectorby Geode-solutions, OpenGeode module for inspecting meshes and models, Introduction, Documentation, Usage, Questions

</details>

### opentelemetry-opamp-client

OpenTelemetry OpAMP client

`pip install opentelemetry-opamp-client` · installs (wheel) · licence: Apache-2.0 · rank 14973 · last release 2026-10-26 · [PyPI](https://pypi.org/project/opentelemetry-opamp-client/) · [source](https://github.com/open-telemetry/opentelemetry-python-contrib)

<details><summary>README extract</summary>

Sections: OpenTelemetry OpAMP Client, References

</details>

### ovos-utils

collection of simple utilities for use across the openvoiceos ecosystem

`pip install ovos-utils` · installs (wheel) · licence: Apache-2.0 · rank 14974 · last release 2026-03-11 · [PyPI](https://pypi.org/project/ovos-utils/) · [source](https://github.com/OpenVoiceOS/ovos_utils)

<details><summary>README extract</summary>

collection of simple utilities for use across the mycroft ecosystem

Sections: OVOS-utils, Commandline scripts, ovos-logs

</details>

### openreview-py

OpenReview API Python client library

`pip install openreview-py` · installs (wheel) · licence: MIT · rank 14996 · last release 2026-11-05 · [PyPI](https://pypi.org/project/openreview-py/)

<details><summary>README extract</summary>

Prerequisites

Python 3.9 or newer is required to use openreview-py.

Installation

There are two ways to install the OpenReview python library.

Using `pip`:

From the repository:

> Note: Depending on your Python installation you may need to use the command `pip3` instead of `pip`.

Sections: OpenReview Python library, Updating Dependencies, Interactive Shell, Branch Selection, Keeping Infrastructure Between Runs, Configuration, Cleanup, Test Setup, Running Tests

</details>

