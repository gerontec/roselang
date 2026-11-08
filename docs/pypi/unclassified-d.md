# Unclassified / D (part 1 of 2)

[Index](README.md) · 552 packages in this topic, by downloads.

part 1 · [part 2](unclassified-d-2.md)

### databricks-sdk

Databricks SDK for Python (Beta)

`pip install databricks-sdk` · installs (wheel) · licence: Apache Software License · rank 317 · last release 2026-11-05 · [PyPI](https://pypi.org/project/databricks-sdk/) · [docs](https://databricks-sdk-py.readthedocs.io)

<details><summary>README extract</summary>

> This repository is a read-only mirror, published from Databricks'
> internal repository with each release. Pull requests are reviewed
> here but merged internally (see CONTRIBUTING.md).

Beta: This SDK is supported for production use cases,
but we do expect future releases to have some interface changes; see Interface stability. ...

Example:
```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
for c in w.clusters.list():
    print(c.cluster_name)
```

...

</details>

### durationpy

Module for converting between datetime.timedelta and Go's Duration strings.

`pip install durationpy` · installs (wheel) · licence: MIT · rank 388 · last release 2026-08-26 · [PyPI](https://pypi.org/project/durationpy/)

### datadog

The Datadog Python library

`pip install datadog` · installs (wheel) · licence: BSD License · rank 428 · last release 2026-11-04 · [PyPI](https://pypi.org/project/datadog/) · [docs](https://datadogpy.readthedocs.io/en/latest/) · [source](https://github.com/DataDog/datadogpy)

<details><summary>README extract</summary>

The Datadog Python Library is a collection of tools suitable for inclusion in existing Python projects or for the development of standalone scripts. It provides an abstraction on top of Datadog's raw HTTP interface and the Agent's DogStatsD metrics aggregation server, to interact with Datadog and efficiently report events and metrics. ...

Example:
```python
from datadog import initialize, api

options = {
    "api_key": "<YOUR_API_KEY>",
    "app_key": "<YOUR_APP_KEY>",
}

initialize(**options)

title = "Something big happened!"
text = "And let me tell you all about it here!"
tags = ["version:1", "application:web"]

api.Event.create(title=title, text=text, tags=tags)
```

...

</details>

### dataclasses-json

Easily serialize dataclasses to and from JSON.

`pip install dataclasses-json` · installs (wheel) · licence: MIT License · rank 460 · last release 2024-06-09 · [PyPI](https://pypi.org/project/dataclasses-json/) · [docs](https://lidatong.github.io/dataclasses-json/) · [source](https://github.com/lidatong/dataclasses-json)

<details><summary>README extract</summary>

This library provides a simple API for encoding and decoding dataclasses to and from JSON.

It's very easy to get started.

README / Documentation website. Features a navigation bar and search functionality, and should mirror this README exactly -- take a look!

Example:
```python
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Person:
    name: str

person = Person(name='lidatong')
person.to_json()  # '{"name": "lidatong"}' <- this is a string
person.to_dict()  # {'name': 'lidatong'} <- this is a dict
Person.from_json('{"name": "lidatong"}')  # Person(1)
...
```

...

</details>

### ddtrace

Datadog APM client library

`pip install ddtrace` · installs (wheel) · licence: LICENSE.BSD3 · rank 486 · last release 2026-11-04 · [PyPI](https://pypi.org/project/ddtrace/) · [docs](https://ddtrace.readthedocs.io/en/stable/) · [source](https://github.com/DataDog/dd-trace-py/)

<details><summary>README extract</summary>

This library powers Distributed Tracing,
 Continuous Profiling,
 Error Tracking,
 Test Optimization,
 Deployment Tracking,
 Code Hotspots,
 Dynamic Instrumentation,
 and more.

To get started with tracing, check out the product documentation or the glossary.

For advanced usage and configuration information, check out the library documentation. ...

</details>

### dateparser

Date parsing library designed to parse dates from HTML pages

`pip install dateparser` · installs (wheel) · licence: BSD-3-Clause · rank 528 · last release 2026-11-04 · [PyPI](https://pypi.org/project/dateparser/) · [source](https://github.com/scrapinghub/dateparser)

<details><summary>README extract</summary>

Python parser for human readable dates

Features:
- Support for almost every existing date format: absolute dates,
 relative dates (`"two weeks ago"` or `"tomorrow"`), timestamps,
 etc.
- Support for more than 200 language
 locales.
- Language autodetection ...

Example:
```python
>>> import dateparser

>>> dateparser.parse('Fri, 12 Dec 2014 10:55:50')
datetime.datetime(2014, 12, 12, 10, 55, 50)

>>> dateparser.parse('1991-05-17')
datetime.datetime(1991, 5, 17, 0, 0)

>>> dateparser.parse('In two months')  # today is 1st Aug 2020
datetime.datetime(2020, 10, 1, 11, 12, 27, 764201)

...
```

...

</details>

### databricks-sql-connector

Databricks SQL Connector for Python

`pip install databricks-sql-connector` · installs (wheel) · licence: Apache Software License · rank 549 · last release 2026-11-04 · [PyPI](https://pypi.org/project/databricks-sql-connector/)

<details><summary>README extract</summary>

The Databricks SQL Connector for Python allows you to develop Python applications that connect to Databricks clusters and SQL warehouses. It is a Thrift-based client with no dependencies on ODBC or JDBC. It conforms to the Python DB API 2.0 specification.

This connector uses Arrow as the data-exchange format, and supports APIs (e.g. ...

Sections: Databricks SQL Connector for Python, Requirements, Documentation, Quickstart, SQLAlchemy, Quick SQLAlchemy guide

</details>

### diskcache

Disk Cache -- Disk and file backed persistent cache.

`pip install diskcache` · installs (wheel) · licence: Apache Software License · rank 716 · last release 2023-08-31 · [PyPI](https://pypi.org/project/diskcache/) · [docs](http://www.grantjenks.com/docs/diskcache/) · [source](https://github.com/grantjenks/python-diskcache)

<details><summary>README extract</summary>

DiskCache is an Apache2 licensed disk and file backed cache library, written
in pure-Python, and compatible with Django.

The cloud-based computing of 2023 puts a premium on memory. Gigabytes of empty
space is left on disks as processes vie for memory. Among these processes is
Memcached (and sometimes Redis) which is used as a cache. ...

Features:
- Pure-Python
- Fully Documented
- Benchmark comparisons (alternatives, Django cache backends)
- 100% test coverage
- Hours of stress testing
- Performance matters
- Django compatible API
- Thread-safe and process-safe ...

Example:
```python
>>> import diskcache
>>> help(diskcache)                             # doctest: +SKIP
```

Sections: DiskCache: Disk Backed Cache, Testimonials, Features, Quickstart, User Guide, Comparisons, Reference

</details>

### dbt-adapters

The set of adapter protocols and base functionality that supports integration with dbt-core

`pip install dbt-adapters` · installs (wheel) · licence: Apache Software License · rank 728 · last release 2026-07-15 · [PyPI](https://pypi.org/project/dbt-adapters/) · [docs](https://docs.getdbt.com) · [source](https://github.com/dbt-labs/dbt-adapters.git#subdirectory=dbt-adapters)

<details><summary>README extract</summary>

There are two major adapter types: base and sql.

`BaseAdapter` defines the base functionality an adapter is required to implement in order to function with `dbt-core`.
There are several methods which have default implementations as well as methods that require the concrete adapter to implement them. ...

Sections: Adapters, `base`, `sql`, Components, Connections, Files, Dialect, Relation caching, Integration with `dbt-core`

</details>

### dbt-common

The shared common utilities that dbt-core and adapter implementations use

`pip install dbt-common` · installs (wheel) · licence: Apache-2.0 · rank 733 · last release 2026-08-11 · [PyPI](https://pypi.org/project/dbt-common/) · [source](https://github.com/dbt-labs/dbt-common.git)

<details><summary>README extract</summary>

The shared common utilities for dbt-core and adapter implementations use

To release a new version of dbt-common to pypi, you'll need to:
1. Run the release workflow to bump the version, generate changelogs and release to pypi
4. ...

Sections: dbt-common, Releasing dbt-common, Getting started

</details>

### dbt-core

With dbt, data analysts and engineers can build analytics the way engineers build applications.

`pip install dbt-core` · installs (wheel) · licence: Apache-2.0 · rank 752 · last release 2026-10-14 · [PyPI](https://pypi.org/project/dbt-core/) · [source](https://github.com/dbt-labs/dbt-core.git)

<details><summary>README extract</summary>

> Note: v2 of the dbt engine is now available, and ships as two distributions:
> - `pip install dbt` (recommended) - installs the default distribution with the full feature set
> - `pip install dbt-oss` - installs the subset distribution, with only Apache 2 open source code
> With v2, you no longer need to install adapters separately, so you can ...

Sections: Understanding dbt, Getting started

</details>

### django-cors-headers

django-cors-headers is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).

`pip install django-cors-headers` · installs (wheel) · licence: MIT · rank 781 · last release 2025-09-18 · [PyPI](https://pypi.org/project/django-cors-headers/) · [source](https://github.com/adamchainz/django-cors-headers)

<details><summary>README extract</summary>

A Django App that adds Cross-Origin Resource Sharing (CORS) headers to
responses. This allows in-browser requests to your Django application from
other origins.

Improve your Django and Git skills with my books.

Adding CORS headers allows your resources to be accessed on other domains. ...

Example:
```python
from corsheaders.defaults import default_methods

CORS_ALLOW_METHODS = (
    *default_methods,
    "POKE",
)
```

...

</details>

### dbt-extractor

A tool to analyze and extract information from Jinja used in dbt projects.

`pip install dbt-extractor` · installs (wheel) · licence: Apache Software License · rank 805 · last release 2025-04-07 · [PyPI](https://pypi.org/project/dbt-extractor/) · [source](https://github.com/dbt-labs/dbt-parser-generator/)

<details><summary>README extract</summary>

This repository contains a tool that processes the most common jinja value templates in dbt model files. The tool depends on tree-sitter and the tree-sitter-jinja2 library.

Sections: dbt extractor, Understanding dbt-extractor, Getting started, Strategy, Architecture

</details>

### datadog-api-client

Collection of all Datadog Public endpoints

`pip install datadog-api-client` · installs (wheel) · licence: Apache Software License · rank 825 · last release 2026-10-13 · [PyPI](https://pypi.org/project/datadog-api-client/) · [docs](https://docs.datadoghq.com/api/) · [source](https://github.com/DataDog/datadog-api-client-python)

<details><summary>README extract</summary>

This repository contains the autogenerated Python client for the Datadog API. The client code, feature files, and test data are generated from Datadog's public OpenAPI specifications by internal tooling.

We welcome contributions that expand or improve the client's capabilities. ...

Example:
```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="example",
    type=MonitorType("log alert"),
...
```

...

</details>

### dbt-protos

Public proto bindings for dbt

`pip install dbt-protos` · installs (wheel) · licence: Apache Software License · rank 837 · last release 2026-10-23 · [PyPI](https://pypi.org/project/dbt-protos/)

<details><summary>README extract</summary>

Central public protos repository for use in dbt.

This repository and library are 100% generated.

</details>

### django-filter

Django-filter is a reusable Django application for allowing users to filter querysets dynamically.

`pip install django-filter` · installs (wheel) · licence: BSD License · rank 966 · last release 2026-10-03 · [PyPI](https://pypi.org/project/django-filter/) · [docs](https://django-filter.readthedocs.io/en/main/) · [source](https://github.com/carltongibson/django-filter)

<details><summary>README extract</summary>

Django-filter is a reusable Django application allowing users to declaratively
add dynamic `QuerySet` filtering from URL parameters.

Full documentation on read the docs.

Django-Filter is a mature and stable package. It uses a two-part CalVer
versioning scheme, such as `21.1`. The first number is the year. ...

Example:
```python
import django_filters

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name', 'price', 'manufacturer']
```

Sections: Django Filter, Versioning and stability policy, Usage, Usage with Django REST Framework

</details>

### datamodel-code-generator

Datamodel Code Generator

`pip install datamodel-code-generator` · installs (wheel) · licence: MIT · rank 972 · last release 2026-11-07 · [PyPI](https://pypi.org/project/datamodel-code-generator/) · [source](https://github.com/datamodel-code-generator/datamodel-code-generator)

<details><summary>README extract</summary>

🚀 Generate Python data models from schema definitions in seconds.

📚 Documentation ·
🧪 Playground ·
💼 Lead maintainer available for work

> [!NOTE]
> Playground privacy: Generation runs locally in your browser with Pyodide. Your schema and options are not sent to a
> backend. ...

Example:
```python
# generated by datamodel-codegen:
# filename:  schema.json

from future import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

class Species(StrEnum):
    dog = 'dog'
    cat = 'cat'
    bird = 'bird'
    fish = 'fish'

class Pet(BaseModel):
    model_config = ConfigDict(
...
```

...

</details>

### databricks-labs-blueprint

Common libraries for Databricks Labs

`pip install databricks-labs-blueprint` · installs (wheel) · licence: Other/Proprietary License · rank 998 · last release 2026-11-03 · [PyPI](https://pypi.org/project/databricks-labs-blueprint/) · [source](https://github.com/databrickslabs/blueprint)

<details><summary>README extract</summary>

<!-- FOR CONTRIBUTORS: Edit this file in Visual Studio Code with the recommended extensions, so that we update the table of contents automatically -->


Baseline for Databricks Labs projects written in Python. Sources are validated with `mypy` and `pylint`. See Contributing instructions if you would like to improve this project. ...

Example:
```python
from databricks.sdk import WorkspaceClient
from databricks.labs.blueprint.paths import WorkspacePath

name = 'some-folder'
ws = WorkspaceClient()
wsp = WorkspacePath(ws, f"~/{name}/foo/bar/baz")
assert not wsp.is_absolute()

wsp.absolute()  # raises NotImplementedError

with_user = wsp.expanduser()
with_user.mkdir()

...
```

...

</details>

### django-stubs-ext

Monkey-patching and extensions for django-stubs

`pip install django-stubs-ext` · installs (wheel) · licence: MIT · rank 1012 · last release 2026-10-05 · [PyPI](https://pypi.org/project/django-stubs-ext/)

<details><summary>README extract</summary>

This package contains extensions and monkey-patching functions for the django-stubs package. Certain features of django-stubs (i.e. generic django classes that don't define the `class_getitem` method) require runtime monkey-patching, which can't be done with type stubs. ...

Example:
```python
import django_stubs_ext

django_stubs_ext.monkeypatch()
```

Sections: Extensions and monkey-patching for django-stubs, Usage, Version compatibility, To get help

</details>

### django-storages

Support for many storage backends in Django

`pip install django-storages` · installs (wheel) · licence: BSD License · rank 1019 · last release 2025-04-02 · [PyPI](https://pypi.org/project/django-storages/)

<details><summary>README extract</summary>

Sections: About, Found a Bug?, Documentation, . Check for open issues at the project, . Bug me until I can merge your pull request.

</details>

### detect-installer

Detect how a Python package was installed and get the correct upgrade command

`pip install detect-installer` · installs (wheel) · licence: 0BSD · rank 1025 · last release 2026-09-02 · [PyPI](https://pypi.org/project/detect-installer/)

<details><summary>README extract</summary>

Example:
```python
from detect_installer import detect_installer

info = detect_installer("rich")

if info is None:
    print("Package is not installed")
else:
    print(info.installer)    # e.g. Installer.PIP
    print(info.upgrade_cmd)  # e.g. "pip install -U rich"
```

Sections: Usage, Vendoring

</details>

### dbt-semantic-interfaces

The shared semantic layer definitions that dbt-core and MetricFlow use

`pip install dbt-semantic-interfaces` · installs (wheel) · licence: Apache-2.0 · rank 1075 · last release 2026-02-10 · [PyPI](https://pypi.org/project/dbt-semantic-interfaces/)

<details><summary>README extract</summary>

This repo contains the shared semantic classes, default validation, and tests designed to be used by both the dbt-core and MetricFlow projects. By centralizing these shared resources, we aim to maintain consistency and reduce code duplication across both projects.

Features:
- Protocols for shared semantic classes: Define the interfaces and common attributes that must be implemented by the objects in both projects.
- Validation: Ensure that the objects comply with the expected structure and constraints. ...

Sections: dbt-semantic-interfaces, Features

</details>

### django-stubs

Mypy stubs for Django

`pip install django-stubs` · installs (wheel) · licence: MIT · rank 1087 · last release 2026-10-05 · [PyPI](https://pypi.org/project/django-stubs/)

<details><summary>README extract</summary>

This package contains type stubs and a custom mypy plugin to provide more precise static types and type inference for Django framework. Django uses some Python "magic" that makes having precise types for some code patterns problematic. This is why we need this project. The final goal is to be able to get precise types for most common patterns.

Example:
```python
try:
    from .local_settings import *
except Exception:
    pass
```

...

</details>

### dunamai

Dynamic version generation

`pip install dunamai` · installs (wheel) · licence: MIT License · rank 1173 · last release 2026-11-07 · [PyPI](https://pypi.org/project/dunamai/) · [source](https://github.com/mtkennerly/dunamai)

<details><summary>README extract</summary>

Dunamai is a Python 3.5+ library and command line tool for producing dynamic,
standards-compliant version strings, derived from tags in your version control system.
This facilitates uniquely identifying nightly or per-commit builds in continuous integration
and releasing new versions of your software simply by creating a tag. ...

Features:
* Git (2.7.0+ is recommended, but versions as old as 1.8.2.3 will work with some reduced functionality)
 * Mercurial
 * Darcs
 * Subversion
 * Bazaar
 * Fossil
 * Pijul ...

Example:
```python
from dunamai import Version, Style

# Let's say you're on commit g644252b, which is tagged as v0.1.0.
version = Version.from_git()
assert version.serialize() == "0.1.0"

# Let's say there was a v0.1.0rc5 tag 44 commits ago
# and you have some uncommitted changes.
...

</details>

### DateTime

This package provides a DateTime data type, as known from Zope. Unless you need to communicate with Zope APIs, you're probably better off using Python's built-in datetime module.

`pip install DateTime` · installs (wheel) · licence: Zope Public License · rank 1190 · last release 2025-11-25 · [PyPI](https://pypi.org/project/DateTime/)

<details><summary>README extract</summary>

This package provides a DateTime data type, as known from Zope.

Unless you need to communicate with Zope APIs, you're probably better
off using Python's built-in datetime module.

For further documentation, please have a look at `src/DateTime/DateTime.txt`.

Encapsulation of date/time values.

Returns the list of recognized timezone names: ...

Sections: DateTime, The DateTime package, Function Timezones(), Class DateTime, Constructor for DateTime, Instance Methods for DateTime (IDateTime interface), Conversion and comparison methods, Component access, strftime(), General formats from previous DateTime, New formats, Deprecated API, General Services Provided by DateTime, Numeric Services Provided by DateTime

</details>

### dagster-pipes

Toolkit for Dagster integrations with transform logic outside of Dagster

`pip install dagster-pipes` · installs (wheel) · licence: Apache-2.0 · rank 1254 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-pipes/)

### ddtrace-internal

Stub internal Datadog Python package (ddtrace-internal).

`pip install ddtrace-internal` · installs (wheel) · licence: BSD-3-Clause OR Apache-2.0 · rank 1272 · last release 2026-10-30 · [PyPI](https://pypi.org/project/ddtrace-internal/) · [source](https://github.com/DataDog/datadog-apm-python)

<details><summary>README extract</summary>

Stub Python distribution for code used by multiple products in dd-trace-py

Sections: ddtrace-internal, Running tests, Layout

</details>

### deltalake

Native Delta Lake Python binding based on delta-rs with Pandas integration

`pip install deltalake` · installs (wheel) · licence: Apache Software License · rank 1286 · last release 2026-09-24 · [PyPI](https://pypi.org/project/deltalake/) · [docs](https://delta-io.github.io/delta-rs/) · [source](https://github.com/delta-io/delta-rs/tree/main/python/)

<details><summary>README extract</summary>

Native Delta Lake Python binding based on
delta-rs with
Pandas integration.

Example:
```python
from deltalake import DeltaTable
dt = DeltaTable("../rust/tests/data/delta-0.2.0")
dt.version()
3
dt.file_uris()
['s3://bucket/table/part-00000-cb6b150b-30b8-4662-ad28-ff32ddab96d2-c000.snappy.parquet',
 's3://bucket/table/part-00000-7c2deba3-1994-4fb8-bc07-d46c948aa415-c000.snappy.parquet',
...
```

Sections: Deltalake-python, Example, Tracing and Observability, Basic Example, Build custom wheels, Cross compilation

</details>

### dagster-shared

Shared code between dagster and dagster-dg-core.

`pip install dagster-shared` · installs (wheel) · licence: Apache-2.0 · rank 1314 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-shared/)

### dirhash

Python module and CLI for hashing of file system directories.

`pip install dirhash` · installs (wheel) · licence: MIT · rank 1343 · last release 2024-08-03 · [PyPI](https://pypi.org/project/dirhash/)

<details><summary>README extract</summary>

A lightweight python module and CLI for computing the hash of any
directory based on its files' structure and content.

- Supports all hashing algorithms of Python's built-in `hashlib` module.
- Glob/wildcard (".gitignore style") path matching for expressive filtering of files to include/exclude.
- Multiprocessing for up to 6x speed-up ...

Features:
If you (or your application) need to verify the integrity of a set of files as well
as their name and location, you might find this useful. ...

Example:
```python
from dirhash import dirhash

dirpath = "path/to/directory"
dir_md5 = dirhash(dirpath, "md5")
pyfiles_md5 = dirhash(dirpath, "md5", match=["*.py"])
no_hidden_sha1 = dirhash(dirpath, "sha1", ignore=[".*", ".*/"])
```

Sections: dirhash, Usage, Why?, Performance, Documentation

</details>

### dotenv

Deprecated package

`pip install dotenv` · installs (wheel) · licence: not stated · rank 1357 · last release 2025-02-19 · [PyPI](https://pypi.org/project/dotenv/)

### daytona_api_client_async

Daytona

`pip install daytona_api_client_async` · installs (wheel) · licence: Apache-2.0 · rank 1394 · last release 2026-11-07 · [PyPI](https://pypi.org/project/daytona_api_client_async/) · [source](https://github.com/daytona/clients)

### daytona_api_client

Daytona

`pip install daytona_api_client` · installs (wheel) · licence: Apache-2.0 · rank 1396 · last release 2026-11-07 · [PyPI](https://pypi.org/project/daytona_api_client/) · [source](https://github.com/daytona/clients)

### daytona_toolbox_api_client_async

Daytona Toolbox API

`pip install daytona_toolbox_api_client_async` · installs (wheel) · licence: Apache-2.0 · rank 1402 · last release 2026-11-07 · [PyPI](https://pypi.org/project/daytona_toolbox_api_client_async/) · [source](https://github.com/daytona/clients)

### daytona_toolbox_api_client

Daytona Toolbox API

`pip install daytona_toolbox_api_client` · installs (wheel) · licence: Apache-2.0 · rank 1404 · last release 2026-11-07 · [PyPI](https://pypi.org/project/daytona_toolbox_api_client/) · [source](https://github.com/daytona/clients)

<details><summary>README extract</summary>

Daytona Daemon Toolbox API for file operations, process execution, git operations, LSP, computer use, and more.

This Python package is automatically generated by the OpenAPI Generator project:

- API version: v0.0.0-dev
- Package version: 0.0.0-dev
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

Example:
```python
import daytona_toolbox_api_client
from daytona_toolbox_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to
# See configuration.py for a list of all supported configuration parameters.
configuration = daytona_toolbox_api_client.Configuration(
    host = "
)

...
```

...

</details>

### daytona

Python SDK for Daytona

`pip install daytona` · installs (wheel) · licence: Apache-2.0 · rank 1441 · last release 2026-11-07 · [PyPI](https://pypi.org/project/daytona/)

<details><summary>README extract</summary>

The official Python SDK for Daytona, a secure and elastic infrastructure for running AI-generated code. Daytona provides full composable computers — sandboxes — that you can manage programmatically using the Daytona SDK. ...

Example:
```python
from daytona import Daytona, DaytonaConfig

# Initialize with environment variables
daytona = Daytona()

# Initialize with configuration object
config = DaytonaConfig(
    api_key="YOUR_API_KEY",
    api_url="YOUR_API_URL",
    target="us"
)
```

...

</details>

### databricks-cli

A command line interface for Databricks

`pip install databricks-cli` · installs (wheel) · licence: Apache Software License · rank 1449 · last release 2023-10-05 · [PyPI](https://pypi.org/project/databricks-cli/)

<details><summary>README extract</summary>

Note

 Databricks recommends that you use newer Databricks CLI versions 0.200 and above instead of legacy Databricks CLI versions 0.17 and below (located in this repository). You can find the new CLI at ...

Sections: databricks-cli, Requirements, Known Issues, Using Docker, Documentation

</details>

### dagster-graphql

The GraphQL API for Dagster.

`pip install dagster-graphql` · installs (wheel) · licence: Apache-2.0 · rank 1478 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-graphql/)

### deepmerge

A toolset for deeply merging Python dictionaries.

`pip install deepmerge` · installs (wheel) · licence: MIT License · rank 1485 · last release 2026-10-25 · [PyPI](https://pypi.org/project/deepmerge/) · [source](https://github.com/toumorokoshi/deepmerge)

<details><summary>README extract</summary>

A tool to handle merging of nested data structures in Python.

Example:
```python
from deepmerge import always_merger

base = {"foo": ["bar"]}
next = {"foo": ["baz"]}

expected_result = {'foo': ['bar', 'baz']}
result = always_merger.merge(base, next)

assert expected_result == result
```

Sections: deepmerge, Example

</details>

### dagster-webserver

Web UI for dagster.

`pip install dagster-webserver` · installs (wheel) · licence: Apache-2.0 · rank 1536 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-webserver/)

### djangorestframework-stubs

PEP-484 stubs for django-rest-framework

`pip install djangorestframework-stubs` · installs (wheel) · licence: MIT · rank 1580 · last release 2026-11-02 · [PyPI](https://pypi.org/project/djangorestframework-stubs/)

<details><summary>README extract</summary>

Mypy stubs for Django REST Framework.
Supports Python 3.11 and up.

Example:
```python
class MyModelSerializer(serializers.ModelSerializer[MyModel]):
    class Meta:
        model = MyModel
        fields = ("id", "example")
```

Sections: pep484 stubs for Django REST framework, FAQ, To get help

</details>

### dbt-snowflake

The Snowflake adapter plugin for dbt

`pip install dbt-snowflake` · installs (wheel) · licence: Apache Software License · rank 1641 · last release 2026-11-04 · [PyPI](https://pypi.org/project/dbt-snowflake/) · [docs](https://docs.getdbt.com) · [source](https://github.com/dbt-labs/dbt-adapters.git#subdirectory=dbt-snowflake)

<details><summary>README extract</summary>

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

`dbt-snowflake` enables dbt to work with Snowflake. ...

Sections: dbt, dbt-snowflake, Getting started

</details>

### databricks-connect

Databricks Connect Client

`pip install databricks-connect` · does not install on CPython 3.14 · licence: Other/Proprietary License · rank 1651 · last release 2026-10-23 · [PyPI](https://pypi.org/project/databricks-connect/)

<details><summary>README extract</summary>

Databricks Connect allows you to connect popular IDEs such as Visual Studio Code, PyCharm, IntelliJ IDEA,
notebook servers, and other custom applications to Databricks clusters.

Databricks Connect is a client library for the Databricks Runtime. ...

</details>

### dagster-postgres

A Dagster integration for postgres

`pip install dagster-postgres` · installs (wheel) · licence: Apache-2.0 · rank 1661 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-postgres/)

### daytona_analytics_api_client_async

Daytona Analytics API

`pip install daytona_analytics_api_client_async` · installs (wheel) · licence: not stated · rank 1672 · last release 2026-11-07 · [PyPI](https://pypi.org/project/daytona_analytics_api_client_async/) · [source](https://github.com/daytona/clients)

### daytona_analytics_api_client

Daytona Analytics API

`pip install daytona_analytics_api_client` · installs (wheel) · licence: not stated · rank 1673 · last release 2026-11-07 · [PyPI](https://pypi.org/project/daytona_analytics_api_client/) · [source](https://github.com/daytona/clients)

### dspy

DSPy

`pip install dspy` · installs (wheel) · licence: not stated · rank 1725 · last release 2026-10-12 · [PyPI](https://pypi.org/project/dspy/)

<details><summary>README extract</summary>

Documentation: DSPy Docs

DSPy is the framework for _programming—rather than prompting—language models. It allows you to iterate fast on building modular AI systems and offers algorithms for optimizing their prompts and weights, whether you're building simple classifiers, sophisticated RAG pipelines, or Agent loops. ...

Sections: DSPy: _Programming_—not prompting—Foundation Models, Documentation: dspy.ai

</details>

### disposable-email-domains

A set of disposable email domains

`pip install disposable-email-domains` · installs (wheel) · licence: MIT · rank 1732 · last release 2026-11-05 · [PyPI](https://pypi.org/project/disposable-email-domains/)

<details><summary>README extract</summary>

This module provides a set of known disposable email domains.

Example:
```python
>>> from disposable_email_domains import blocklist
>>> 'bearsarefuzzy.com' in blocklist
True
```

Sections: Disposable Email Domains, Usage, Source

</details>

### docx2txt

A pure python-based utility to extract text and images from docx files.

`pip install docx2txt` · installs (wheel) · licence: not stated · rank 1737 · last release 2025-03-24 · [PyPI](https://pypi.org/project/docx2txt/)

### django-simple-history

Store model history and view/revert changes from admin site.

`pip install django-simple-history` · installs (wheel) · licence: BSD License · rank 1743 · last release 2026-07-22 · [PyPI](https://pypi.org/project/django-simple-history/) · [docs](https://django-simple-history.readthedocs.io/en/stable/) · [source](https://github.com/django-commons/django-simple-history)

<details><summary>README extract</summary>

`django-simple-history` stores Django model state on every create/update/delete.

This app supports the following combinations of Django and Python:

========== ========================
 Django Python
========== ========================
5.2 3.10, 3.11, 3.12, 3.13, 3.14
6.0 3.12, 3.13, 3.14
6.1 3.12, 3.13, 3.14
main 3.12, 3.13, 3.14
========== ...

Sections: Getting Help, 3.13.0 (2026-07-22), 3.12.0 (2026-06-22), 3.11.0 (2025-12-09), 3.10.1 (2025-06-20), 3.10.0 (2025-06-20), 3.9.0 (2025-01-26), 3.8.0 (2025-01-23), 3.7.0 (2024-05-29), 3.6.0 (2024-05-26), 3.5.0 (2024-02-19), 3.4.0 (2023-08-18), 3.3.0 (2023-03-08), 3.2.0 (2022-09-28)

</details>

### dependency-groups

A tool for resolving PEP 735 Dependency Group data

`pip install dependency-groups` · installs (wheel) · licence: MIT · rank 1783 · last release 2026-08-22 · [PyPI](https://pypi.org/project/dependency-groups/) · [docs](https://dependency-groups.readthedocs.io/) · [source](https://github.com/pypa/dependency-groups)

<details><summary>README extract</summary>

An implementation of Dependency Groups (PEP 735).

This is a library which is able to parse dependency groups, following includes, and provide that data as output.

`dependency-groups` provides the following:

- A `DependencyGroupResolver` which implements efficient resolution of
 dependency groups ...

Sections: Dependency Groups, Interfaces, Documentation

</details>

### dbt-postgres

The set of adapter protocols and base functionality that supports integration with dbt-core

`pip install dbt-postgres` · installs (wheel) · licence: Apache Software License · rank 1786 · last release 2026-07-16 · [PyPI](https://pypi.org/project/dbt-postgres/) · [docs](https://docs.getdbt.com) · [source](https://github.com/dbt-labs/dbt-adapters.git#subdirectory=dbt-postgres)

<details><summary>README extract</summary>

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

`dbt-postgres` enables dbt to work with Postgres. ...

Sections: dbt, dbt-postgres, Getting started, psycopg2-binary vs. psycopg2

</details>

### django-model-utils

Django model mixins and utilities

`pip install django-model-utils` · installs (wheel) · licence: BSD License · rank 1795 · last release 2024-09-04 · [PyPI](https://pypi.org/project/django-model-utils/)

<details><summary>README extract</summary>

Django model mixins and utilities.

`django-model-utils` supports Django 3.2+.

This app is available on PyPI.

Documentation for django-model-utils is available

Sections: django-model-utils, Getting Help, 5.0.0 (2024-09-01), 4.5.1 (2024-05-02), 4.5.0 (2024-04-01), 4.4.0 (2024-02-10), 4.3.1 (2022-11-15), 4.3.0, 4.2.0 (2021-10-11), 4.1.1 (2020-12-01), 4.1.0 (2020-11-29), 4.0.0 (2019-12-11), 3.2.0 (2019.06.21), 3.1.2 (2018.05.09)

</details>

### dbt-spark

The Apache Spark adapter plugin for dbt

`pip install dbt-spark` · installs (wheel) · licence: Apache Software License · rank 1916 · last release 2026-07-16 · [PyPI](https://pypi.org/project/dbt-spark/) · [docs](https://docs.getdbt.com) · [source](https://github.com/dbt-labs/dbt-adapters.git#subdirectory=dbt-spark)

<details><summary>README extract</summary>

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

`dbt-spark` enables dbt to work with Apache Spark. ...

Sections: dbt, dbt-spark, Getting started, Running locally, Additional Configuration for MacOS

</details>

### dagster-cloud-cli

(no summary)

`pip install dagster-cloud-cli` · installs (wheel) · licence: Apache-2.0 · rank 1919 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-cloud-cli/)

### docling-parse

Simple package to extract text with coordinates from programmatic PDFs

`pip install docling-parse` · installs (wheel) · licence: MIT · rank 1959 · last release 2026-10-29 · [PyPI](https://pypi.org/project/docling-parse/) · [source](https://github.com/docling-project/docling-parse)

<details><summary>README extract</summary>

Simple package to extract text, paths and bitmap images with coordinates from programmatic PDFs. This package is used in the Docling PDF conversion. Below, we show a few output of the latest parser with char, word and line level output for text, in addition to the extracted paths and bitmap resources. ...

Example:
```python
from docling_core.types.doc.page import TextCellUnit
from docling_parse.pdf_parser import (
    ContentConfig,
    ContentLevel,
    DecodeConfig,
    DoclingPdfParser,
)

parser = DoclingPdfParser(loglevel="fatal")

pdf_doc = parser.load(
    path_or_stream="",
    decode_config=DecodeConfig(
        do_sanitization=True,
...
```

...

</details>

### dbt-bigquery

The BigQuery adapter plugin for dbt

`pip install dbt-bigquery` · installs (wheel) · licence: Apache Software License · rank 1982 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dbt-bigquery/) · [docs](https://docs.getdbt.com) · [source](https://github.com/dbt-labs/dbt-adapters.git#subdirectory=dbt-bigquery)

<details><summary>README extract</summary>

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

`dbt-bigquery` enables dbt to work with Google BigQuery. ...

Sections: dbt, dbt-bigquery, Getting started

</details>

### dagster-aws

Package for AWS-specific Dagster framework solid and resource components.

`pip install dagster-aws` · installs (wheel) · licence: Apache-2.0 · rank 2019 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-aws/)

### docxtpl

Python docx template engine

`pip install docxtpl` · installs (wheel) · licence: LGPL-2.1-only · rank 2035 · last release 2025-11-13 · [PyPI](https://pypi.org/project/docxtpl/) · [source](https://github.com/elapouya/python-docx-template.git)

_README extract left out: share-alike licence._

### decli

Minimal, easy-to-use, declarative cli tool

`pip install decli` · installs (wheel) · licence: MIT License · rank 2042 · last release 2025-06-01 · [PyPI](https://pypi.org/project/decli/)

<details><summary>README extract</summary>

Minimal declarative cli tool.

Example:
```python
from decli import cli

data = {
    "prog": "myapp",
    "description": "Process some integers.",
    "arguments": [
        {
            "name": "integers",
            "metavar": "N",
            "type": int,
            "nargs": "+",
            "help": "an integer for the accumulator",
        },
        {
            "name": "--sum",
...
```

Sections: Decli, About, Usage, Main cli, Arguments, Subcommands, Func, Groups, Exclusive Groups, Groups and Exclusive groups, Parents, Recipes, Minimal

</details>

### django-migration-linter

Detect backward incompatible migrations for your django project

`pip install django-migration-linter` · installs (wheel) · licence: Apache-2.0 · rank 2044 · last release 2026-01-04 · [PyPI](https://pypi.org/project/django-migration-linter/) · [source](https://github.com/3YOURMIND/django-migration-linter)

<details><summary>README extract</summary>

Detect backward incompatible migrations for your Django project.
It will save you time by making sure migrations will not break with a older codebase.

Sections: Django migration linter, Usage example, Integration, More information, Blog post, They talk about the linter, Related, Maintained by David Wobrock

</details>

### ddsketch

Distributed quantile sketches

`pip install ddsketch` · installs (wheel) · licence: Apache Software License · rank 2059 · last release 2024-04-01 · [PyPI](https://pypi.org/project/ddsketch/)

<details><summary>README extract</summary>

This repo contains the Python implementation of the distributed quantile sketch
algorithm DDSketch [1]. DDSketch has relative-error guarantees for any quantile
q in [0, 1]. That is if the true value of the qth-quantile is `x` then DDSketch
returns a value `y` such that `|x-y| / x < e` where `e` is the relative error
parameter. ...

Example:
```python
from ddsketch import DDSketch

sketch = DDSketch()
```

Sections: ddsketch, Usage, Formatting, Type-checking, Protobuf, Releasing, References

</details>

### dbt-databricks

The Databricks adapter plugin for dbt

`pip install dbt-databricks` · installs (wheel) · licence: Apache-2.0 · rank 2075 · last release 2026-10-29 · [PyPI](https://pypi.org/project/dbt-databricks/) · [docs](https://docs.getdbt.com/reference/resource-configs/databricks-configs) · [source](https://github.com/databricks/dbt-databricks)

<details><summary>README extract</summary>

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

The Databricks Lakehouse provides one simple platform to unify all your data, analytics and AI workloads.

The `dbt-databricks` adapter contains all of the code enabling dbt to work with Databricks. ...

Example:
```python
def model(dbt, session):
    dbt.config(
      http_path="sql/protocolv1/..."
    )
```

Sections: dbt-databricks, Choosing between dbt-databricks and dbt-spark, Getting started, Profile Setup, Documentation, Quick Starts, Compatibility, Tips and Tricks, Choosing compute for a Python model, Python models and ANSI mode

</details>

### dagster-k8s

A Dagster integration for k8s

`pip install dagster-k8s` · installs (wheel) · licence: Apache-2.0 · rank 2095 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-k8s/)

### databricks-agents

Mosaic AI Agent Framework SDK

`pip install databricks-agents` · installs (wheel) · licence: Other/Proprietary License · rank 2146 · last release 2026-10-21 · [PyPI](https://pypi.org/project/databricks-agents/)

<details><summary>README extract</summary>

The software and other materials included in this library are subject to the DB license.

</details>

### djangorestframework-csv

CSV Tools for Django REST Framework

`pip install djangorestframework-csv` · installs (wheel) · licence: BSD License · rank 2148 · last release 2023-12-12 · [PyPI](https://pypi.org/project/djangorestframework-csv/)

<details><summary>README extract</summary>

CSV Tools for Django REST Framework

Sections: djangorestframework-csv, Compatibility, Running the tests, 3.0.2, 3.0.1, 3.0.0, 2.1.1, 2.1.0, 2.0.0, 1.4.0/1.4.1, 1.3.4, 1.3.2/1.3.3, 1.3.1, 1.3.0

</details>

### databricks-pypi1

(no summary)

`pip install databricks-pypi1` · installs (wheel) · licence: not stated · rank 2269 · last release 2018-11-13 · [PyPI](https://pypi.org/project/databricks-pypi1/)

### deepeval

The LLM Evaluation Framework

`pip install deepeval` · installs (wheel) · licence: Apache Software License · rank 2325 · last release 2026-11-04 · [PyPI](https://pypi.org/project/deepeval/) · [docs](https://deepeval.com) · [source](https://github.com/confident-ai/deepeval)

<details><summary>README extract</summary>

Documentation |
 Metrics and Features |
 Getting Started |
 Integrations |
 Confident AI

 Deutsch |
 Español |
 français |
 日本語 |
 한국어 |
 Português |
 Русский |

DeepEval is a simple-to-use, open-source LLM evaluation framework, for evaluating large-language model systems. It is similar to Pytest but specialized for unit testing LLM apps. ...

Example:
```python
import pytest
from deepeval import assert_test
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams

def test_case():
    correctness_metric = GEval(
        name="Correctness",
        criteria="Determine if the 'actual output' is correct based on the 'expected output'.",
...
```

...

</details>

### django-linear-migrations

Ensure your migrations are linear.

`pip install django-linear-migrations` · installs (wheel) · licence: MIT · rank 2336 · last release 2025-09-18 · [PyPI](https://pypi.org/project/django-linear-migrations/) · [source](https://github.com/adamchainz/django-linear-migrations)

<details><summary>README extract</summary>

Ensure your migration history is linear.

For a bit of background, see the introductory blog post.

Work smarter and faster with my book Boost Your Django DX which covers django-linear-migrations and many other tools to improve your development experience.

Python 3.9 to 3.14 supported.

Django 4.2 to 6.0 supported.

Example:
```python
# myapp/management/commands/makemigrations.py
from django_linear_migrations.management.commands.makemigrations import (
    Command as BaseCommand,
)

class Command(BaseCommand): ...
```

...

</details>

### dparse

A parser for Python dependency files

`pip install dparse` · installs (wheel) · licence: MIT License · rank 2367 · last release 2024-11-08 · [PyPI](https://pypi.org/project/dparse/)

<details><summary>README extract</summary>

A parser for Python dependency files

Example:
```python
from dparse import parse, filetypes

content = """
South==1.0.1 --hash=sha256:abcdefghijklmno
pycrypto>=2.6
"""

df = parse(content, file_type=filetypes.requirements_txt)

print(df.json())

{
  "file_type": "requirements.txt",
  "content": "\nSouth==1.0.1 --hash=sha256:abcdefghijklmno\npycrypto>=2.6\n",
  "path": null,
  "sha": null,
...
```

Sections: Dependency Parser, Usage, Python 2.7

</details>

### databricks-labs-lsql

Lightweight stateless SQL execution for Databricks with minimal dependencies

`pip install databricks-labs-lsql` · installs (wheel) · licence: Other/Proprietary License · rank 2390 · last release 2026-11-03 · [PyPI](https://pypi.org/project/databricks-labs-lsql/) · [docs](https://github.com/databrickslabs/lsql#readme) · [source](https://github.com/databrickslabs/lsql)

<details><summary>README extract</summary>

Lightweight execution of SQL queries through Databricks SDK for Python.

<!-- TOC -->
* Databricks Labs LSQL
* Installation
* Executing SQL
 * Iterating over results
 * Executing without iterating
 * Fetching one record
 * Fetching one value
 * Parameters
* SQL backend abstraction
* Project Support
<!-- TOC -->

Example:
```python
from databricks.sdk import WorkspaceClient
from databricks.labs.lsql.core import StatementExecutionExt
w = WorkspaceClient()
see = StatementExecutionExt(w)
for (pickup_zip, dropoff_zip) in see('SELECT pickup_zip, dropoff_zip FROM samples.nyctaxi.trips LIMIT 10'):
    print(f'pickup_zip={pickup_zip}, dropoff_zip={dropoff_zip}')
```

...

</details>

### dagster-dg-cli

(no summary)

`pip install dagster-dg-cli` · installs (wheel) · licence: Apache-2.0 · rank 2394 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-dg-cli/)

### dagster-dg-core

(no summary)

`pip install dagster-dg-core` · installs (wheel) · licence: Apache-2.0 · rank 2401 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-dg-core/)

### dagster-slack

A Slack client resource for posting to Slack

`pip install dagster-slack` · installs (wheel) · licence: Apache-2.0 · rank 2408 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-slack/)

### databricks-sqlalchemy

Databricks SQLAlchemy plugin for Python

`pip install databricks-sqlalchemy` · installs (wheel) · licence: Apache Software License · rank 2419 · last release 2026-07-02 · [PyPI](https://pypi.org/project/databricks-sqlalchemy/)

<details><summary>README extract</summary>

The Databricks dialect for SQLAlchemy serves as bridge between SQLAlchemy and the Databricks SQL Python driver. A working example demonstrating usage can be found in `sqlalchemy_example.py`.

Example:
```python
import os
from sqlalchemy import create_engine

host = os.getenv("DATABRICKS_SERVER_HOSTNAME")
http_path = os.getenv("DATABRICKS_HTTP_PATH")
access_token = os.getenv("DATABRICKS_TOKEN")
catalog = os.getenv("DATABRICKS_CATALOG")
schema = os.getenv("DATABRICKS_SCHEMA")

engine = create_engine(
...
```

...

</details>

### django-hijack

Enable users to hijack (=login as) and work on behalf of another user.

`pip install django-hijack` · installs (wheel) · licence: MIT License · rank 2476 · last release 2026-10-10 · [PyPI](https://pypi.org/project/django-hijack/) · [docs](https://django-hijack.rtfd.io/) · [source](https://github.com/django-hijack/django-hijack)

<details><summary>README extract</summary>

With Django Hijack, admins can impersonate and work on behalf of other users without having to know their credentials.

Sections: Django Hijack, Docs, Versions, Testimonials

</details>

### dbt-duckdb

The duckdb adapter plugin for dbt (data build tool)

`pip install dbt-duckdb` · installs (wheel) · licence: Apache Software License · rank 2481 · last release 2026-10-26 · [PyPI](https://pypi.org/project/dbt-duckdb/)

<details><summary>README extract</summary>

DuckDB is an embedded database, similar to SQLite, but designed for OLAP-style analytics.
It is crazy fast and allows you to read and write data stored in CSV, JSON, and Parquet files directly, without requiring you to load
them into the database first. ...

Example:
```python
default:
  outputs:
    dev:
      type: duckdb
      path: /tmp/dbt.duckdb
      extensions:
        - httpfs
        - parquet
      secrets:
        - type: s3
          region: my-aws-region
          key_id: "{{ env_var('S3_ACCESS_KEY_ID') }}"
          secret: "{{ env_var('S3_SECRET_ACCESS_KEY') }}"
  target: dev
```

...

</details>

### databricks-pypi2

(no summary)

`pip install databricks-pypi2` · installs (wheel) · licence: not stated · rank 2492 · last release 2018-11-13 · [PyPI](https://pypi.org/project/databricks-pypi2/)

### depyf

Decompile python functions, from bytecode to source code!

`pip install depyf` · installs (wheel) · licence: MIT · rank 2585 · last release 2025-10-13 · [PyPI](https://pypi.org/project/depyf/)

<details><summary>README extract</summary>

> `depyf` is proud to be a PyTorch ecosystem project. Check out the announcement blog for more details.

Have you ever felt overwhelmed by the complexities of `torch.compile`? Diving into its workings can feel like black magic, with bytecode and Python internal details that many users fail to understand, hindering them from understanding and ...

Features:
If you want to understand bytecode generated by `torch.compile`, then `depyf` might be the only choice for you. Below we tested several existing decompilers, they struggle to decompile simple Python bytecode across versions, and have poor support ...

Example:
```python
import torch
from torch import _dynamo as torchdynamo
from typing import List

@torch.compile
def toy_example(a, b):
    x = a / (torch.abs(a) + 1)
    if b.sum() < 0:
...

</details>

### dlinfo

Python wrapper for libc's dlinfo and dyld_find on Mac

`pip install dlinfo` · installs (wheel) · licence: MIT · rank 2686 · last release 2025-01-16 · [PyPI](https://pypi.org/project/dlinfo/)

<details><summary>README extract</summary>

Python wrapper for libc's dlinfo

Example:
```python
>>> from dlinfo import DLInfo
>>> lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
>>> dlinfo = DLInfo(lib)
>>> dlinfo.path
'/lib/x86_64-linux-gnu/libc.so.6'
```

Sections: python-dlinfo, Usage

</details>

### datadog_lambda

The Datadog AWS Lambda Library

`pip install datadog_lambda` · installs (wheel) · licence: Apache Software License · rank 2700 · last release 2026-10-21 · [PyPI](https://pypi.org/project/datadog_lambda/) · [source](https://github.com/DataDog/datadog-lambda-python)

<details><summary>README extract</summary>

Datadog Lambda Library for Python (3.8, 3.9, 3.10, 3.11, 3.12, 3.13, and 3.14) enables enhanced Lambda metrics, distributed tracing, and custom metric submission from AWS Lambda functions.

Sections: datadog-lambda-python, Configuration, Opening Issues, Lambda Profiling Beta, Major Version Notes, 6.x / Layer version 95+, 5.x / Layer version 86+, 4.x / Layer version 61+

</details>

### dashscope

dashscope client sdk library

`pip install dashscope` · installs (wheel) · licence: Apache Software License · rank 2741 · last release 2026-11-06 · [PyPI](https://pypi.org/project/dashscope/)

<details><summary>README extract</summary>

> English | 中文

The DashScope Python SDK is the official client for Alibaba Cloud Model Studio (Bailian), covering text generation, multi-modal understanding, embeddings, reranking, image/video generation, speech synthesis & recognition, fine-tuning, agentic RL, applications and more. ...

Features:
Every capability is a resource on the client. Sync and async clients expose the same surface (async methods are `await`ed) — with one exception: the duplex WebSocket audio sessions are sync-only by design, as noted below. ...

Example:
```python
import dashscope

completion = dashscope.chat("qwen-plus", "Tell me a joke")
print(completion.output_text)
```

...

</details>

### django-pydantic-field

Type-Safe Pydantic Schemas for Django JSONFields

`pip install django-pydantic-field` · installs (wheel) · licence: MIT · rank 2753 · last release 2026-10-30 · [PyPI](https://pypi.org/project/django-pydantic-field/) · [docs](https://github.com/surenkov/django-pydantic-field) · [source](https://github.com/surenkov/django-pydantic-field)

<details><summary>README extract</summary>

`django-pydantic-field` provides a way to use Pydantic models as schemas for Django's `JSONField`.
It offers full support for Pydantic v1 and v2, type safety and integration with Django's ecosystem, including Forms and Django REST Framework.

Features:
- Unified API: Transparent support for Pydantic v1 and v2 through the `SchemaAdapter`s.
- Type-Safe: Support for static type checking (ty/mypy/pyright) with type inference for models and annotations. ...

Example:
```python
import pydantic
import typing

from django.db import models
from django_pydantic_field import SchemaField

class Foo(pydantic.BaseModel):
    count: int
    slug: str = "default"

class MyModel(models.Model):
    # Django-like style (explicit schema)
    bar = SchemaField(Foo, default={"count": 5})

...

</details>

### duckdb-engine

SQLAlchemy driver for duckdb

`pip install duckdb-engine` · installs (wheel) · licence: MIT License · rank 2758 · last release 2025-03-29 · [PyPI](https://pypi.org/project/duckdb-engine/) · [source](https://github.com/Mause/duckdb_engine)

<details><summary>README extract</summary>

Basic SQLAlchemy driver for DuckDB

<!--ts-->
- duckdb\_engine
 - Installation
 - Usage
 - Usage in IPython/Jupyter
 - Configuration
 - How to register a pandas DataFrame
 - Things to keep in mind
 - Auto-incrementing ID columns
 - Pandas `read_sql()` chunksize
 - Unsigned integer support
 - Alembic Integration
 - Preloading extensions ...

Example:
```python
from sqlalchemy import Column, Integer, Sequence, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session

Base = declarative_base()

class FakeModel(Base):  # type: ignore
    tablename = "fake"

    id = Column(Integer, Sequence("fakemodel_id_sequence"), primary_key=True)
...
```

...

</details>

### django-reversion

An extension to the Django web framework that provides version control for model instances.

`pip install django-reversion` · installs (wheel) · licence: BSD License · rank 2768 · last release 2026-11-02 · [PyPI](https://pypi.org/project/django-reversion/)

<details><summary>README extract</summary>

django-reversion is an extension to the Django web framework that provides
version control for model instances.

- Python 3.11 or later
- Django 5.2 or later

Features:
- Roll back to any point in a model instance's history.
- Recover deleted model instances.
- Simple admin integration.

Sections: django-reversion, Requirements, Features, Documentation, Upgrading

</details>

### datacompy

Dataframe comparisons in Python

`pip install datacompy` · installs (wheel) · licence: Apache Software License · rank 2780 · last release 2026-10-27 · [PyPI](https://pypi.org/project/datacompy/) · [docs](https://capitalone.github.io/datacompy/) · [source](https://github.com/capitalone/datacompy.git)

<details><summary>README extract</summary>

DataComPy is a package to compare two DataFrames (or tables) such as Pandas, Spark, Polars, and
even Snowflake. Originally it was created to be something of a replacement
for SAS's ``PROC COMPARE`` for Pandas DataFrames with some more functionality than
just ``Pandas.DataFrame.equals(Pandas.DataFrame)`` (in that it prints out some stats,
and lets ...

Example:
```python
import pandas as pd
from datacompy import PandasCompare

df1 = pd.DataFrame({"id": [1, 2, 3], "val": [10, 20, 30]})
df2 = pd.DataFrame({"id": [1, 2, 3], "val": [10, 99, 30]})

compare = PandasCompare(df1, df2, join_columns="id")

# Access structured data directly
data = compare.build_report_data()
print(data.row_summary.unequal_rows)  # 1
...
```

Sections: DataComPy, Command Line Interface, Programmatic Report Access

</details>

### dotmap

ordered, dynamically-expandable dot-access dictionary

`pip install dotmap` · installs (wheel) · licence: MIT · rank 2805 · last release 2022-04-06 · [PyPI](https://pypi.org/project/dotmap/)

<details><summary>README extract</summary>

Features:
`DotMap` is a dot-access `dict` subclass that

- has dynamic hierarchy creation (autovivification)
- can be initialized with keys
- easily initializes from `dict`
- easily converts to `dict`
- is ordered by insertion ...

Example:
```python
from dotmap import DotMap
m = DotMap()
m.name = 'Joe'
print('Hello ' + m.name)
# Hello Joe
```

Sections: DotMap, Upgrade, Features

</details>

### docopt-ng

Jazzband-maintained fork of docopt, the humane command line arguments parser.

`pip install docopt-ng` · installs (wheel) · licence: MIT License · rank 2841 · last release 2023-05-30 · [PyPI](https://pypi.org/project/docopt-ng/) · [source](https://github.com/jazzband/docopt-ng)

<details><summary>README extract</summary>

docopt-ng is a fork of the original docopt, now maintained by the
jazzband project. Now with maintenance, typehints, and complete test coverage!

docopt-ng helps you create beautiful command-line interfaces:

results in:

Beat that! The option parser is generated based on the docstring above
that is passed to `docopt` function. ...

Example:
```python
"""Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
  naval_fate.py (-h | --help)
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
...
```

...

</details>

### dash-bootstrap-components

Bootstrap themed components for use in Plotly Dash

`pip install dash-bootstrap-components` · installs (wheel) · licence: Apache Software License · rank 2842 · last release 2025-08-20 · [PyPI](https://pypi.org/project/dash-bootstrap-components/) · [source](https://github.com/dbc-team/dash-bootstrap-components/)

<details><summary>README extract</summary>

Bootstrap components for Plotly Dash

 Explore the documentation
 Report a bug
 Request a feature

_dash-bootstrap-components is a library of Bootstrap
components for use with Plotly Dash, that makes it easier to
build consistently styled Dash apps with complex, responsive layouts.

Example:
```python
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
```

Sections: Dash Bootstrap Components, PyPI, Anaconda, Quick start, Linking a stylesheet, Build the layout

</details>

### django-object-actions

A Django app for adding object tools for models in the admin

`pip install django-object-actions` · installs (wheel) · licence: Apache Software License · rank 2897 · last release 2026-05-28 · [PyPI](https://pypi.org/project/django-object-actions/)

<details><summary>README extract</summary>

If you've ever tried making admin object tools you may have thought, "why can't
this be as easy as making Django Admin Actions?" Well now they can be.

Install Django Object Actions:

Add `django_object_actions` to your `INSTALLED_APPS` so Django can find
our templates.

In your admin.py:

Example:
```python
from django_object_actions import DjangoObjectActions

class MyModelAdmin(DjangoObjectActions, admin.ModelAdmin):
    @action(
        label="This will be the label of the button",  # optional
        description="This will be the tooltip of the button" # optional
    )
    def toolfunc(self, request, obj):
        pass

...
```

...

</details>

### dify-plugin

Dify Plugin SDK

`pip install dify-plugin` · installs (wheel) · licence: Apache-2.0 · rank 2903 · last release 2026-11-02 · [PyPI](https://pypi.org/project/dify-plugin/) · [source](https://github.com/langgenius/dify-plugin-sdks)

<details><summary>README extract</summary>

The Python SDK for building Dify plugins: tools, model providers, agent strategies, HTTP extensions, datasources, and triggers.

Plugin development guide · Schema reference · Releases

Sections: Dify Plugin SDK, Getting Started, Production Plugin Examples, OpenAI-Compatible Embeddings, Blocking LLM Replay, OpenAI-Compatible Completion Input, OpenAI-Compatible Usage Estimates, OpenAI-Compatible Streaming, Version Management, For SDK Users, Manifest Version Reference, Meta.Version Reference, Meta.MinimumDifyVersion Reference, Literal Stop Sequences

</details>

### dagster-docker

A Dagster integration for docker

`pip install dagster-docker` · installs (wheel) · licence: Apache-2.0 · rank 2924 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-docker/)

### dbt-redshift

The Redshift adapter plugin for dbt

`pip install dbt-redshift` · installs (wheel) · licence: Apache Software License · rank 2986 · last release 2026-11-04 · [PyPI](https://pypi.org/project/dbt-redshift/) · [docs](https://docs.getdbt.com) · [source](https://github.com/dbt-labs/dbt-adapters.git#subdirectory=dbt-redshift)

<details><summary>README extract</summary>

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

`dbt-redshift` enables dbt to work with Amazon Redshift. ...

Sections: dbt, dbt-redshift, Getting started

</details>

### dataclass-wizard

A wizard-like JSON serialization library for Python dataclasses

`pip install dataclass-wizard` · installs (wheel) · licence: Apache Software License · rank 3007 · last release 2026-07-03 · [PyPI](https://pypi.org/project/dataclass-wizard/) · [docs](https://dcw.ritviknag.com) · [source](https://github.com/rnag/dataclass-wizard)

<details><summary>README extract</summary>

Simple, elegant wizarding tools for Python’s `dataclasses`.

📘 Docs → dcw.ritviknag.com

Dataclass Wizard is a fast, well-tested serialization library for Python dataclasses with automatic type conversion and support for JSON, YAML, TOML, and environment variables.

Behold, the power of Dataclass Wizard:

Features:
Dataclass Wizard helps you turn Python dataclasses into robust,
high-performance serialization schemas with minimal effort.

- 🚀 Fast — code-generated loaders and dumpers
- 🪶 Lightweight — pure Python, minimal dependencies ...

Example:
```python
from dataclasses import dataclass
from dataclass_wizard import JSONWizard

@dataclass
class Data(JSONWizard):
    value: int

data = Data.from_dict({"value": "123"})
assert data.value == 123
print(data.to_json())
```

...

</details>

### django-pgactivity

Monitor, kill, and analyze Postgres queries.

`pip install django-pgactivity` · installs (wheel) · licence: BSD License · rank 3038 · last release 2025-11-30 · [PyPI](https://pypi.org/project/django-pgactivity/) · [docs](https://django-pgactivity.readthedocs.io) · [source](https://github.com/AmbitionEng/django-pgactivity)

<details><summary>README extract</summary>

`django-pgactivity` makes it easy to view, filter, and kill active Postgres queries.

Some of the features at a glance:

* The `PGActivity` proxy model and `pgactivity` management command for querying and filtering the Postgres pg_stat_activity view. ...

Example:
```python
import pgactivity

@pgactivity.timeout(0.5)
def my_operation():
    # Any queries in this operation that take over 500 milliseconds will throw
    # django.db.utils.OperationalError.
```

Sections: django-pgactivity, Quick Start, Basic Command Usage, Attaching Context, Proxy Model, Setting the Statement Timeout, Compatibility, Documentation, Creators

</details>

### django-pglock

Postgres locking routines and lock table access.

`pip install django-pglock` · installs (wheel) · licence: BSD License · rank 3059 · last release 2025-11-30 · [PyPI](https://pypi.org/project/django-pglock/) · [docs](https://django-pglock.readthedocs.io) · [source](https://github.com/AmbitionEng/django-pglock)

<details><summary>README extract</summary>

`django-pglock` performs advisory locks, table locks, and helps manage blocking locks.
Here's some of the functionality at a glance:

* `pglock.advisory` for application-level locking, for example, ensuring that tasks don't overlap.
* `pglock.model` for locking an entire model. ...

Example:
```python
import pglock

with pglock.advisory("my_lock_id"):
    # This code blocks until the "my_lock_id" lock is available
```

Sections: django-pglock, Quickstart, Advisory Locks, Model Locks, Prioritizing Blocked Code, Setting the Lock Timeout, Querying Locks, Compatibility, Documentation, Creators

</details>

### dogpile.cache

A caching front-end based on the Dogpile lock.

`pip install dogpile.cache` · installs (wheel) · licence: MIT · rank 3061 · last release 2025-10-11 · [PyPI](https://pypi.org/project/dogpile.cache/) · [docs](https://dogpilecache.sqlalchemy.org)

<details><summary>README extract</summary>

Dogpile consists of two subsystems, one building on top of the other.

`dogpile` provides the concept of a "dogpile lock", a control structure
which allows a single thread of execution to be selected as the "creator" of
some resource, while allowing other threads of execution to refer to the previous
version of this resource as the creation ...

Features:
* A succinct API which encourages up-front configuration of pre-defined
 "regions", each one defining a set of caching characteristics including
 storage backend, configuration options, and default expiration time. ...

Sections: dogpile, Documentation, Features, The SQLAlchemy Project

</details>

### django-safedelete

Mask your objects instead of deleting them from your database.

`pip install django-safedelete` · installs (wheel) · licence: BSD License · rank 3073 · last release 2026-08-17 · [PyPI](https://pypi.org/project/django-safedelete/)

<details><summary>README extract</summary>

For various reasons, you may want to avoid deleting objects from your database.

This Django application provides an abstract model, that allows you to transparently retrieve or delete your objects,
without having them deleted from your database. ...

Example:
```python
# imports
from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE

# Models

# We create a new model, with the given policy : Objects will be hard-deleted, or soft deleted if other objects would have been deleted too.
class Article(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE_NOCASCADE

...
```

...

</details>

### django-countries

Provides a country field for Django models.

`pip install django-countries` · installs (wheel) · licence: MIT License · rank 3076 · last release 2026-09-10 · [PyPI](https://pypi.org/project/django-countries/) · [source](https://github.com/SmileyChris/django-countries)

<details><summary>README extract</summary>

A Django application that provides country choices for use with forms, flag icons static files, and a country field for models.

📚 Read the full documentation

Features:
- Country Field: Django model field with all ISO 3166-1 countries
- Translated Names: Country names translated using Django's i18n system
- Flag Icons: Static flag image files for all countries ...

Example:
```python
from django_countries.fields import CountryField

class Person(models.Model):
    country = CountryField()
```

Sections: Django Countries, Documentation, Quick Start, Features, Translations

</details>

### dagster-dbt

A Dagster integration for dbt

`pip install dagster-dbt` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 3091 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-dbt/)

### dicttoxml

Converts a Python dictionary or other native data type into a valid XML string.

`pip install dicttoxml` · installs (wheel) · licence: not stated · rank 3159 · last release 2022-12-23 · [PyPI](https://pypi.org/project/dicttoxml/)

<details><summary>README extract</summary>

Converts a Python dictionary or other native data type into a valid XML string.

Supports item (`int`, `float`, `long`, `decimal.Decimal`, `bool`, `str`, `unicode`, `datetime`, `none` and other number-like objects) and collection (`list`, `set`, `tuple` and `dict`, as well as iterable and dict-like objects) data types, with arbitrary nesting for ...

Sections: Summary, Details, Basic Usage, JSON to XML, XML Snippet, Custom Root, Omit XML Declaration, Disable Type Attributes, Change or Suppress XML Encoding Attribute, Unique ID Attributes, Dict-Like and Iterable Objects, Define Custom Item Names, CDATA, Return a String

</details>

### django-rest-polymorphic

Polymorphic serializers for Django REST Framework.

`pip install django-rest-polymorphic` · installs (wheel) · licence: MIT License · rank 3178 · last release 2022-07-17 · [PyPI](https://pypi.org/project/django-rest-polymorphic/)

<details><summary>README extract</summary>

Polymorphic serializers for Django REST Framework.

Features:
`django-rest-polymorphic` allows you to easily define serializers for your inherited models that you have created using `django-polymorphic` library.

Example:
```python
# models.py
from django.db import models
from polymorphic.models import PolymorphicModel

class Project(PolymorphicModel):
    topic = models.CharField(max_length=30)

class ArtProject(Project):
    artist = models.CharField(max_length=30)

class ResearchProject(Project):
    supervisor = models.CharField(max_length=30)
```

Sections: Django REST Polymorphic, Overview, Usage, Customize resource type

</details>

### django-postgres-copy

Quickly import and export delimited data with Django support for PostgreSQL's COPY command

`pip install django-postgres-copy` · installs (wheel) · licence: MIT · rank 3190 · last release 2025-06-22 · [PyPI](https://pypi.org/project/django-postgres-copy/) · [docs](https://palewi.re/docs/django-postgres-copy/) · [source](https://github.com/palewire/django-postgres-copy)

<details><summary>README extract</summary>

- Documentation: palewi.re/docs/django-postgres-copy/
- Issues: github.com/palewire/django-postgres-copy/issues
- Packaging: pypi.python.org/pypi/django-postgres-copy
- Testing: github.com/palewire/django-postgres-copy/actions

</details>

### dynamodb-json

A DynamoDB json util from and to python objects

`pip install dynamodb-json` · installs (wheel) · licence: Mozilla · rank 3207 · last release 2024-05-18 · [PyPI](https://pypi.org/project/dynamodb-json/)

<details><summary>README extract</summary>

DynamoDB json util to load and dump strings of Dynamodb json format to python object and vise-versa

Example:
```python
import time
import uuid
from datetime import datetime
from decimal import Decimal

from dynamodb_json import json_util as json

json = {"MyString": "a",
         "num": 4,
         "MyBool": False,
         "my_dict": {"my_date": datetime.utcnow()},
         "MyNone": None,
         "MyZero": 0,
...
```

Sections: DynamoDB Json, Use

</details>

### docxcompose

Compose .docx documents

`pip install docxcompose` · installs (wheel) · licence: MIT License · rank 3213 · last release 2026-06-02 · [PyPI](https://pypi.org/project/docxcompose/)

<details><summary>README extract</summary>

*docxcompose* is a Python library for concatenating/appending Microsoft
Word (.docx) files.

Example:
```python
from docxcompose.composer import Composer
from docx import Document
master = Document("master.docx")
composer = Composer(master)
doc1 = Document("doc1.docx")
composer.append(doc1)
composer.save("combined.docx")
```

Sections: Example usage, The docxcompose console script, Docker container, Options, Preserving styles, Headers and footers

</details>

### dvc

Git for data scientists - manage your code and data together

`pip install dvc` · installs (wheel) · licence: Apache-2.0 · rank 3219 · last release 2026-03-31 · [PyPI](https://pypi.org/project/dvc/) · [docs](https://dvc.org/doc) · [source](https://github.com/treeverse/dvc)

<details><summary>README extract</summary>

Website
• Docs
• Blog
• Tutorial
• Related Technologies
• How DVC works
• VS Code Extension
• Installation
• Contributing
• Community and Support


Data Version Control or DVC is a command line tool and VS Code Extension to help you develop reproducible machine learning projects: ...

Sections: . Version your data and models., . Iterate fast with lightweight pipelines., Quick start, How DVC works, VS Code Extension, Snapcraft (Linux), Chocolatey (Windows), Brew (mac OS), Anaconda (Any platform), PyPI (Python), Package (Platform-specific), Ubuntu / Debian (deb), Fedora / CentOS (rpm), Copyright

</details>

### dbl-tempo

Tempo is timeseries manipulation for Spark. This project builds upon the capabilities of PySpark to provide a suite of abstractions and functions that make operations on timeseries data easier and highly scalable.

`pip install dbl-tempo` · installs (wheel) · licence: MIT · rank 3228 · last release 2025-09-15 · [PyPI](https://pypi.org/project/dbl-tempo/) · [docs](https://databrickslabs.github.io/tempo/) · [source](https://github.com/databrickslabs/tempo)

<details><summary>README extract</summary>

The purpose of this project is to make time series manipulation with Spark simpler. Operations covered under this package include AS OF joins, rolling statistics with user-specified window lengths, featurization of time series using lagged values, and Delta Lake optimization on time and partition fields.

Example:
```python
# ts_col = timestamp column on which to sort fact and source table
# partition_cols - columns to use for partitioning the TSDF into more granular time series for windowing and sorting

resampled_sdf = phone_accel_tsdf.resample(freq='min', func='floor')
resampled_pdf = resampled_sdf.df.filter(col('event_ts').cast("date") == "2015-02-23").toPandas()
...
```

...

</details>

### dvc-data

DVC's data management subsystem

`pip install dvc-data` · installs (wheel) · licence: Apache-2.0 · rank 3248 · last release 2026-02-27 · [PyPI](https://pypi.org/project/dvc-data/) · [source](https://github.com/iterative/dvc-data)

<details><summary>README extract</summary>

Features:
* TODO

Example:
```python
from dvc_data.hashfile import HashFile

obj = HashFile("/path/to/file", fs, HashInfo("md5", "36eba1e1e343279857ea7f69a597324e")
```

Sections: DVC data, Features, Requirements, Usage, HashFile, HashFileDB, Index, Storage, Issues

</details>

### dvc-objects

dvc objects - filesystem and object-db level abstractions to use in dvc and dvc-data

`pip install dvc-objects` · installs (wheel) · licence: Apache-2.0 · rank 3260 · last release 2026-11-06 · [PyPI](https://pypi.org/project/dvc-objects/) · [source](https://github.com/treeverse/dvc-objects)

<details><summary>README extract</summary>

Features:
* serverless
* supports multiple storages (local, s3, gs, gdrive, ssh/sftp, etc)
* based on fsspec

Sections: DVC objects, Features, Requirements, Usage, Issues

</details>

### dvc-studio-client

Small library to post data from DVC/DVCLive to Iterative Studio

`pip install dvc-studio-client` · installs (wheel) · licence: Apache-2.0 · rank 3261 · last release 2026-06-01 · [PyPI](https://pypi.org/project/dvc-studio-client/) · [source](https://github.com/iterative/dvc-studio-client)

<details><summary>README extract</summary>

Client to interact with DVC Studio.

Features:
- Model Registry
 - get_download_uris: Return download URIs for the specified model.

- Live Experiments
 - post_live_metrics: Post updates to `api/live`. ...

Sections: dvc-studio-client, Features, Issues

</details>

### databricks-dlt

Databricks DLT Library

`pip install databricks-dlt` · installs (wheel) · licence: Databricks Proprietary License · rank 3264 · last release 2024-11-27 · [PyPI](https://pypi.org/project/databricks-dlt/)

<details><summary>README extract</summary>

The Databricks Delta Live Tables (DLT) Python stub makes local development of DLT pipelines easier by:
* Providing API specs and docstring references for autocomplete features in IDEs.
* Providing Python data type hints to the library to enable type checking for DLT projects.

Sections: Python stub for Delta Live Tables, Getting Started, Documentation

</details>

### django-taggit

django-taggit is a reusable Django application for simple tagging.

`pip install django-taggit` · installs (wheel) · licence: BSD License · rank 3270 · last release 2026-11-02 · [PyPI](https://pypi.org/project/django-taggit/) · [docs](https://django-taggit.readthedocs.io) · [source](https://github.com/jazzband/django-taggit)

<details><summary>README extract</summary>

This is a Jazzband project. By contributing you agree
to abide by the Contributor Code of Conduct and follow the guidelines.

`django-taggit` a simpler approach to tagging with Django. Add `"taggit"` to your
`INSTALLED_APPS` then just add a TaggableManager to your model and go:

Then you can use the API like so: ...

Example:
```python
from django.db import models

from taggit.managers import TaggableManager

class Food(models.Model):
    # ... fields here

    tags = TaggableManager()
```

</details>

### django-unfold

Modern Django Admin

`pip install django-unfold` · installs (wheel) · licence: MIT · rank 3275 · last release 2026-11-01 · [PyPI](https://pypi.org/project/django-unfold/) · [docs](https://unfoldadmin.com/docs/) · [source](https://github.com/unfoldadmin/django-unfold)

<details><summary>README extract</summary>

A modern Django admin theme for building dashboards, internal tools, and business applications

 Live demo ·
 Documentation ·
 Discord ·
 PyPI

Features:
- Django native - Built on `django.contrib.admin`, preserving familiar models, permissions, and conventions.
- Incremental adoption - Introduce Unfold gradually without rebuilding your existing admin. ...

Example:
```python
from django.contrib import admin
from unfold.admin import ModelAdmin

@admin.register(MyModel)
class MyModelAdmin(ModelAdmin):
    pass
```

Sections: Unfold - Modern Django admin, Quickstart, Why Unfold?, Features

</details>

### dagster-celery

Package for using Celery as Dagster's execution engine.

`pip install dagster-celery` · installs (wheel) · licence: Apache-2.0 · rank 3296 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-celery/)

### dvc-render

Dvc Render

`pip install dvc-render` · installs (wheel) · licence: Apache-2.0 · rank 3309 · last release 2024-04-10 · [PyPI](https://pypi.org/project/dvc-render/) · [source](https://github.com/iterative/dvc-render)

<details><summary>README extract</summary>

dvc-render is a library for rendering data stored in DVC plots format into different output formats, like Vega. It can also generate HTML and MarkDown reports containing multiple plots.

It is used internally by DVC, DVCLive, and Studio.

Features:
* Renderers

Take data stored in DVC plots format alongside plot properties in order to render a plot in different formats.

* Reports

Take multiple renderers and build an HTML or MarkDown report.

* Templates ...

Example:
```python
from dvc_render import VegaRenderer
properties = {"template": "confusion", "x": "predicted", "y": "actual"}
 datapoints = [
     {"predicted": "B", "actual": "A"},
     {"predicted": "A", "actual": "A"},
 ]

renderer = VegaRenderer(datapoints, "foo", **properties)
plot_content = renderer.get_filled_template()
```

...

</details>

### django-libsass

A django-compressor filter to compile SASS files using libsass

`pip install django-libsass` · installs (wheel) · licence: BSD License · rank 3313 · last release 2021-07-08 · [PyPI](https://pypi.org/project/django-libsass/)

<details><summary>README extract</summary>

A django-compressor filter to compile Sass files using libsass.

Features:
We wanted to use Sass in a Django project without introducing any external (non pip-installable)
dependencies. (Actually, we wanted to use Less, but the same arguments apply...) There are a few
pure Python implementations of Sass and Less, but we ...

Example:
```python
@import "../variables.scss";
```

Sections: django-libsass, Imports, Settings, Custom functions, Why django-libsass?, Reporting bugs

</details>

### dataset

Toolkit for Python-based database access.

`pip install dataset` · installs (wheel) · licence: MIT License · rank 3315 · last release 2026-04-12 · [PyPI](https://pypi.org/project/dataset/) · [docs](https://dataset.readthedocs.io/) · [source](https://github.com/pudo/dataset)

<details><summary>README extract</summary>

In short, dataset makes reading and writing data in databases as simple as reading and writing JSON files.

Read the docs

To install dataset, fetch it with ``pip``:

Note: as of version 1.0, dataset is split into two packages, with the
data export features now extracted into a stand-alone package, datafreeze.
See the relevant repository here.

</details>

### django-htmx

Extensions for using Django with htmx.

`pip install django-htmx` · installs (wheel) · licence: MIT · rank 3319 · last release 2026-08-05 · [PyPI](https://pypi.org/project/django-htmx/) · [docs](https://django-htmx.readthedocs.io/) · [source](https://github.com/adamchainz/django-htmx)

<details><summary>README extract</summary>

Extensions for using Django with htmx.

Please see

Sections: django-htmx, Documentation

</details>

### dvc-task

Extensible task queue used in DVC.

`pip install dvc-task` · installs (wheel) · licence: Apache-2.0 · rank 3324 · last release 2024-10-08 · [PyPI](https://pypi.org/project/dvc-task/) · [source](https://github.com/iterative/dvc-task)

<details><summary>README extract</summary>

dvc-task is a library for queuing, running and managing background jobs
(processes) from standalone Python applications. dvc-task is built on Celery,
but does not require a full AMQP messaging server (or any other "heavy" servers
which are traditionally used as Celery brokers).

Features:
* `dvc_task.proc` module for running and managing background processes in
 Celery tasks
* Preconfigured Celery app intended for use in standalone desktop
 applications ...

Example:
```python
from dvc_task.proc import ProcessManager

@app.task
def my_task():
    manager = ProcessManager(wdir=".")
    manager.run(["echo", "hello world"], name="foo").delay()
```

...

</details>

### ddapm-test-agent

Test agent for Datadog APM client libraries

`pip install ddapm-test-agent` · installs (wheel) · licence: BSD 3 · rank 3325 · last release 2026-10-26 · [PyPI](https://pypi.org/project/ddapm-test-agent/)

<details><summary>README extract</summary>

The APM test agent is an application which emulates the APM endpoints of the Datadog agent which can be used for testing Datadog APM client libraries.

See the Features section for the complete list of functionalities provided.

See the HTTP API section for the endpoints available. ...

Example:
```python
from openai import OpenAI

client = OpenAI(base_url="
```

Sections: Datadog APM test agent, Features, Trace invariant checks, Returning data, Helpful logging, Proxy, LLM Observability Proxy, Claude Code Hooks, Snapshot output, OTLP trace snapshots, Web UI, Recording 3rd party API requests, Custom 3rd Party Providers, Ignoring Headers in Recorded Cassettes

</details>

### dvc-http

http plugin for dvc

`pip install dvc-http` · installs (wheel) · licence: Apache License 2.0 · rank 3331 · last release 2023-12-13 · [PyPI](https://pypi.org/project/dvc-http/) · [docs](https://dvc.org/doc) · [source](https://github.com/iterative/dvc-http)

### django-loginas

An app to add a "Log in as user" button in the Django user admin page.

`pip install django-loginas` · installs (wheel) · licence: BSD · rank 3341 · last release 2026-01-06 · [PyPI](https://pypi.org/project/django-loginas/)

<details><summary>README extract</summary>

About

"Login as user" for the Django admin.

`loginas` supports Python 3 only, as of version 0.4. If you're on 2, use
0.3.6.

Installing django-loginas

* Add `loginas` to your Python path, or install using pip: `pip install django-loginas`

* If you're using a custom User model, you'll need to add the template to it so the button shows up: ...

Example:
```python
# urls.py
urlpatterns = [
    # from Django 3.2 on, make sure to add loginas urls before the admin site urls, i.e.:
    path('admin/', include('loginas.urls')),
    path('admin/', admin.site.urls),
]
```

Sections: django-loginas, Existing logout view?, Template awareness

</details>

### dbt-clickhouse

The Clickhouse plugin for dbt (data build tool)

`pip install dbt-clickhouse` · installs (wheel) · licence: Apache-2.0 · rank 3381 · last release 2026-09-15 · [PyPI](https://pypi.org/project/dbt-clickhouse/) · [docs](https://github.com/ClickHouse/dbt-clickhouse#documentation) · [source](https://github.com/ClickHouse/dbt-clickhouse)

<details><summary>README extract</summary>

This plugin ports dbt functionality to Clickhouse.

See the ClickHouse website for the full documentation entry.
The documentation source is maintained in `docs`.

Sections: dbt-clickhouse, Documentation

</details>

### django-pgmigrate

Avoid costly downtime during Postgres migrations.

`pip install django-pgmigrate` · installs (wheel) · licence: BSD License · rank 3388 · last release 2025-11-30 · [PyPI](https://pypi.org/project/django-pgmigrate/) · [docs](https://django-pgmigrate.readthedocs.io) · [source](https://github.com/AmbitionEng/django-pgmigrate)

<details><summary>README extract</summary>

`django-pgmigrate` helps you avoid costly downtime with Postgres migrations.

Imagine the following happens:

1. A long-running task queries a model in a transaction and keeps the transaction open.
2. `python manage.py migrate` tries to change a field on the model. ...

Sections: django-pgmigrate, Quick Start, Compatibility, Documentation, Creators

</details>

### drf-exceptions-hog

Standardized and easy-to-parse API error responses for DRF.

`pip install drf-exceptions-hog` · installs (wheel) · licence: MIT License · rank 3390 · last release 2023-05-08 · [PyPI](https://pypi.org/project/drf-exceptions-hog/)

<details><summary>README extract</summary>

Standardized and easy-to-parse API error responses for Django REST Framework.

After reusing similar code in multiple projects, we realized this might actually help others. The problem we're trying to solve is that DRF exceptions tend to vary in format and therefore require complex parsing logic on the frontend, which generally needs to be ...

Sections: DRF Exceptions Hog, 🔌 Usage, 📑 Documentation, Response structure, Multiple exceptions, Error types, 🧱 Requirements

</details>

### django-fernet-fields-v2

Fernet-encrypted model fields for Django

`pip install django-fernet-fields-v2` · installs (wheel) · licence: MIT License · rank 3392 · last release 2023-08-15 · [PyPI](https://pypi.org/project/django-fernet-fields-v2/)

<details><summary>README extract</summary>

django-fernet-fields-v2

 Fernet symmetric encryption for Django model fields, using the
 cryptography library and supports Django \>=3.2 .
 `django-fernet-fields-v2` supports Django 3.2 and later on Python 3.8, 3.9, 3.10 and 3.11
 Only PostgreSQL, SQLite, and MySQL are tested, but any Django database backend
 with support for `BinaryField` should ...

</details>

### django-auditlog

Audit log app for Django

`pip install django-auditlog` · installs (wheel) · licence: MIT License · rank 3394 · last release 2025-12-18 · [PyPI](https://pypi.org/project/django-auditlog/) · [docs](https://django-auditlog.readthedocs.io) · [source](https://github.com/jazzband/django-auditlog)

<details><summary>README extract</summary>

Migrate to V3

Check the Upgrading to version 3 doc before upgrading to V3.

</details>

### django-types

Type stubs for Django

`pip install django-types` · installs (wheel) · licence: MIT · rank 3413 · last release 2026-04-22 · [PyPI](https://pypi.org/project/django-types/) · [source](https://github.com/sbdchd/django-types)

<details><summary>README extract</summary>

Type stubs for Django.

> Note: this project was forked from
> < with the goal of removing the
> `mypy` plugin dependency so that `mypy`
> can't crash due to Django
> config, and that
> non-`mypy` type checkers like
> `pyright` will work better with
> Django.

Example:
```python
import django_stubs_ext

django_stubs_ext.monkeypatch()
```

Sections: django-types, I cannot use QuerySet or Manager with type annotations, usage, `id Field`, `HttpRequest`'s `user` property, related, Releasing a new version

</details>

### databricks

(no summary)

`pip install databricks` · installs (wheel) · licence: not stated · rank 3419 · last release 2018-11-15 · [PyPI](https://pypi.org/project/databricks/)

### deltalite

Streaming partition upsert for Delta tables, replacing delta-rs SQL MERGE

`pip install deltalite` · installs (wheel) · licence: MIT · rank 3435 · last release 2026-11-05 · [PyPI](https://pypi.org/project/deltalite/) · [source](https://github.com/PostHog/posthog)

<details><summary>README extract</summary>

Streaming, partition-level upsert for Delta Lake tables
that replaces delta-rs's SQL `MERGE` with a bounded-memory merge engine. Memory
is bounded by the size of the incoming batch and a few concurrency knobs —
never by the size of the target table. ...

Features:
delta-rs `MERGE` executes a DataFusion hash join whose memory scales with the
*scanned target*, and it can deadlock under a bounded memory pool
(delta-io/delta-rs#4614). ...

Example:
```python
import pyarrow as pa
import deltalite

table = deltalite.DeltaLiteTable.open(
    "s3://bucket/events",
    storage_options={
        "AWS_REGION": "us-east-1",
        "AWS_ACCESS_KEY_ID": "...",
        "AWS_SECRET_ACCESS_KEY": "...",
    },
)

batch = pa.table({
    "id":  [1, 2, 3],
...

</details>

### dataclasses-json-speakeasy

Easily serialize dataclasses to and from JSON.

`pip install dataclasses-json-speakeasy` · installs (wheel) · licence: MIT License · rank 3453 · last release 2024-02-01 · [PyPI](https://pypi.org/project/dataclasses-json-speakeasy/) · [docs](https://lidatong.github.io/dataclasses-json/) · [source](https://github.com/lidatong/dataclasses-json)

<details><summary>README extract</summary>

This library provides a simple API for encoding and decoding dataclasses to and from JSON.

It's very easy to get started.

README / Documentation website. Features a navigation bar and search functionality, and should mirror this README exactly -- take a look!

Example:
```python
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Person:
    name: str

person = Person(name='lidatong')
person.to_json()  # '{"name": "lidatong"}' <- this is a string
person.to_dict()  # {'name': 'lidatong'} <- this is a dict
Person.from_json('{"name": "lidatong"}')  # Person(1)
...
```

...

</details>

### databricks-ai-search

Databricks AI Search Client (formerly Vector Search)

`pip install databricks-ai-search` · installs (wheel) · licence: not stated · rank 3457 · last release 2026-11-07 · [PyPI](https://pypi.org/project/databricks-ai-search/)

<details><summary>README extract</summary>

The Python SDK for Databricks AI Search, the fully managed vector and keyword search service in the Databricks platform. AI Search is the new name for the product previously known as Databricks Vector Search.

Example:
```python
from databricks.ai_search.client import AISearchClient

# Initialize the client (auto-detects credentials in Databricks notebooks)
client = AISearchClient()

# Create an endpoint and index
endpoint = client.create_endpoint(name="my-endpoint", endpoint_type="STANDARD")
index = client.create_delta_sync_index(
    endpoint_name="my-endpoint",
...
```

Sections: Databricks AI Search Python SDK, Usage, Authentication, Use with AI coding agents

</details>

### datefinder

Extract datetime objects from natural language text

`pip install datefinder` · installs (wheel) · licence: MIT License · rank 3519 · last release 2026-03-25 · [PyPI](https://pypi.org/project/datefinder/)

<details><summary>README extract</summary>

A python module for locating dates inside text. Use this package to extract date-like
strings from documents and turn them into useful datetime/temporal objects.

As of `1.0.0`, `find_dates(...)` defaults to the v2 compatibility engine.
The original engine remains available as `find_dates_legacy(...)`.

Example:
```python
In [1]: string_with_dates = """
   ...: ...
   ...: entries are due by January 4th, 2017 at 8:00pm
   ...: ...
   ...: created 01/15/2005 by ACME Inc. and associates.
   ...: ...
   ...: """

In [2]: import datefinder

In [3]: matches = datefinder.find_dates(string_with_dates)

In [4]: for match in matches:
   ...:     print(match)
   ...:
...
```

...

</details>

### django-pgtrigger

Postgres trigger support integrated with Django models.

`pip install django-pgtrigger` · installs (wheel) · licence: BSD License · rank 3523 · last release 2025-12-04 · [PyPI](https://pypi.org/project/django-pgtrigger/) · [docs](https://django-pgtrigger.readthedocs.io) · [source](https://github.com/AmbitionEng/django-pgtrigger)

<details><summary>README extract</summary>

`django-pgtrigger` helps you write Postgres triggers for your Django models.

Features:
Triggers can solve a variety of complex problems more reliably, performantly, and succinctly than application code.
For example,

* Protecting operations on rows or columns (`pgtrigger.Protect`). ...

Example:
```python
import pgtrigger

class ProtectedModel(models.Model):
    """This model cannot be deleted!"""

    class Meta:
        triggers = [
            pgtrigger.Protect(name="protect_deletes", operation=pgtrigger.Delete)
        ]
```

Sections: django-pgtrigger, Why should I use triggers?, Quick start, Compatibility, Documentation, Other Material, Creators

</details>

### django-nested-admin

Django admin classes that allow for nested inlines

`pip install django-nested-admin` · installs (wheel) · licence: BSD · rank 3525 · last release 2025-10-23 · [PyPI](https://pypi.org/project/django-nested-admin/)

<details><summary>README extract</summary>

django-nested-admin is a project that makes it possible to nest
admin inlines (that is, to define inlines on InlineModelAdmin classes).
It is compatible with Django 3.2+ and Python 3.7+ and works with or
without Grappelli. When Grappelli is not installed it allows
Grappelli-like drag-and-drop functionality.

Example:
```python
# An example admin.py for a Table of Contents app

from django.contrib import admin
import nested_admin

from .models import TableOfContents, TocArticle, TocSection

class TocArticleInline(nested_admin.NestedStackedInline):
    model = TocArticle
    sortable_field_name = "position"

class TocSectionInline(nested_admin.NestedStackedInline):
...
```

Sections: Configuration, Example Usage

</details>

### dep-logic

Python dependency specifications supporting logical operations

`pip install dep-logic` · installs (wheel) · licence: Apache Software License · rank 3581 · last release 2026-08-28 · [PyPI](https://pypi.org/project/dep-logic/)

<details><summary>README extract</summary>

Python dependency specifications supporting logical operations

Example:
```python
>>> from dep_logic.specifiers import parse_version_specifier
>>>
>>> a = parse_version_specifier(">=1.0.0")
>>> b = parse_version_specifier("<2.0.0")
>>> print(a & b)
>=1.0.0,<2.0.0
>>> a = parse_version_specifier(">=1.0.0,<2.0.0")
>>> b = parse_version_specifier(">1.5")
>>> print(a | b)
>=1.0.0
```

Sections: Dep-Logic, What does it do?, About the project, Caveats

</details>

### django-vite

Integration of Vite in a Django project.

`pip install django-vite` · installs (wheel) · licence: Apache Software License · rank 3586 · last release 2026-09-14 · [PyPI](https://pypi.org/project/django-vite/)

<details><summary>README extract</summary>

Integration of ViteJS in a Django project.

- Installation
 - Django
 - ViteJS
 - Assets
- Usage
 - Configuration
 - Dev Mode
 - Template tags
 - Custom attributes
 - Loading assets from a CDN
- Vite Legacy Plugin
- Multi-app configuration ...

Example:
```python
# myapp/django_vite_s3.py
import json
import boto3
from django_vite.core.asset_loader import ManifestClient, DjangoViteAppClient

class S3ManifestClient(ManifestClient):
    def load_manifest(self):
        s3 = boto3.client("s3")
        res = s3.get_object(Bucket='django-vite-public-example', Key='manifest.json')
...
```

...

</details>

### dpkt

fast, simple packet creation / parsing, with definitions for the basic TCP/IP protocols

`pip install dpkt` · installs (wheel) · licence: BSD License · rank 3621 · last release 2022-08-18 · [PyPI](https://pypi.org/project/dpkt/)

<details><summary>README extract</summary>

The dpkt project is a python module for fast, simple packet parsing, with definitions for the basic TCP/IP protocols.

Sections: dpkt, Examples and Documentation

</details>

### databricks-feature-engineering

Databricks Feature Engineering Client

`pip install databricks-feature-engineering` · installs (wheel) · licence: Databricks Proprietary License · rank 3648 · last release 2026-11-03 · [PyPI](https://pypi.org/project/databricks-feature-engineering/)

<details><summary>README extract</summary>

The Databricks Feature Engineering client is used to:
* Create, read, and write feature tables
* Train models on feature data
* Publish feature tables to online stores for real-time serving
* Upgrade workspace feature table metadata to Unity Catalog

Documentation can be found per-cloud at:
- AWS
- Azure
- GCP

For release notes, see
- AWS ...

Sections: Documentation, Limitations

</details>

### databricks-api

Databricks API client auto-generated from the official databricks-cli package

`pip install databricks-api` · installs (wheel) · licence: MIT License · rank 3660 · last release 2023-06-08 · [PyPI](https://pypi.org/project/databricks-api/) · [source](https://github.com/crflynn/databricks-api)

<details><summary>README extract</summary>

Please switch to the official Databricks SDK for Python ( by running the following command:

*[This documentation is auto-generated]*

This package provides a simplified interface for the Databricks REST API.
The interface is autogenerated on instantiation using the underlying client
library used in the official `databricks-cli` python package. ...

Example:
```python
from databricks_api import DatabricksAPI

# Provide a host and token
db = DatabricksAPI(
    host="example.cloud.databricks.com",
    token="dpapi123..."
)

# OR a host and user and password
db = DatabricksAPI(
    host="example.cloud.databricks.com",
    user="me@example.com",
    password="password"
)

# Full init signature
db = DatabricksAPI(
...
```

...

</details>

### databricks-vectorsearch

Databricks Vector Search Client

`pip install databricks-vectorsearch` · installs (wheel) · licence: not stated · rank 3670 · last release 2026-10-30 · [PyPI](https://pypi.org/project/databricks-vectorsearch/)

### dateutils

Various utilities for working with date and datetime objects

`pip install dateutils` · installs (wheel) · licence: BSD License · rank 3673 · last release 2020-10-23 · [PyPI](https://pypi.org/project/dateutils/)

<details><summary>README extract</summary>

The main purpose of this package is to provide more complex arithmetic
operations on dates/times. Heavy use is made of the relativedelta type from
Labix's dateutil library. Much of this package is just a light wrapper on top
of this with some added features such as range generation and business day
calculation.

Installation ...

</details>

### dbt-athena

The athena adapter plugin for dbt (data build tool)

`pip install dbt-athena` · installs (wheel) · licence: Apache Software License · rank 3697 · last release 2026-09-07 · [PyPI](https://pypi.org/project/dbt-athena/) · [docs](https://docs.getdbt.com) · [source](https://github.com/dbt-labs/dbt-adapters.git#subdirectory=dbt-athena)

<details><summary>README extract</summary>

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

`dbt-athena` enables dbt to work with Amazon Athena. ...

Features:
- Supports dbt version `1.7.*`
- Support for Python
- Supports seeds
- Correctly detects views and their columns
- Supports table materialization
 - Iceberg tables are supported only with Athena Engine v3 and a unique table location
 (see table ...

Example:
```python
import pandas as pd

def model(dbt, session):
    dbt.config(materialized="table")

    model_df = pd.DataFrame({"A": [1, 2, 3, 4]})

    return model_df
```

...

</details>

### databento-dbn

Python bindings for encoding and decoding Databento Binary Encoding (DBN)

`pip install databento-dbn` · installs (wheel) · licence: Apache-2.0 · rank 3698 · last release 2026-10-27 · [PyPI](https://pypi.org/project/databento-dbn/) · [docs](https://databento.com/docs) · [source](https://github.com/databento/dbn)

<details><summary>README extract</summary>

Python bindings for the `dbn` Rust library, used by the Databento Python client library.
For more information about the encoding, read our introduction to DBN.

Using this library is for advanced users and is not fully documented or supported.

Sections: databento-dbn, Usage and documentation, Building

</details>

### docformatter

Formats docstrings to follow PEP 257

`pip install docformatter` · installs (wheel) · licence: MIT License; Other/Proprietary License · rank 3702 · last release 2026-04-28 · [PyPI](https://pypi.org/project/docformatter/) · [docs](https://docformatter.readthedocs.io/en/latest/) · [source](https://github.com/PyCQA/docformatter)

<details><summary>README extract</summary>

+----------------+----------------------------------------------------------+
| Code + +
+----------------+----------------------------------------------------------+
| Docstrings + +
+----------------+----------------------------------------------------------+
| GitHub + ...

Features:
`docformatter` automatically formats docstrings to follow a subset of the PEP
257 conventions. Below are the relevant items quoted from PEP 257.

- For consistency, always use triple double quotes around docstrings. ...

Example:
```python
"""   Here are some examples.

    This module docstring should be dedented."""

def factorial(x):
    '''

    Return x factorial.

    This uses math.factorial.

    '''
    import math
    return math.factorial(x)

def print_factorial(x):
    """Print x factorial"""
...

</details>

### django-json-widget

Django json widget is an alternative widget that makes it easy to edit the jsonfield field of django.

`pip install django-json-widget` · installs (wheel) · licence: BSD License · rank 3706 · last release 2025-12-12 · [PyPI](https://pypi.org/project/django-json-widget/)

<details><summary>README extract</summary>

An alternative widget that makes it easy to edit the new Django's field JSONField (PostgreSQL specific model fields)

Example:
```python
from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget
from .models import YourModel

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
```

Sections: django-json-widget, Quickstart, Configuration, Accessing JsonEditor Instance, JSONEditorWidget widget, 2.1.1 (2025-12-12), 2.1.0 (2025-10-24), 2.0.4 (2025-10-11), 2.0.3 (2025-07-29), 2.0.2 (2025-07-28), 2.0.0 (2024-03-24), 1.1.1 (2021-02-17), 1.1.0 (2021-02-05), 1.0.1 (2020-04-17)

</details>

### deepspeed

DeepSpeed library

`pip install deepspeed` · installs from source (sdist only) · licence: Apache Software License 2.0 · rank 3737 · last release 2026-10-29 · [PyPI](https://pypi.org/project/deepspeed/) · [docs](https://deepspeed.readthedocs.io) · [source](https://github.com/deepspeedai/DeepSpeed)

<details><summary>README extract</summary>

English · 简体中文

DeepSpeed hosts regular office hours on the last Tuesday of each month at 12:00 America/New_York to discuss development plans, features, etc. This meeting is public for anyone to join and ask questions.
The meeting is hosted on Zoom and can be joined here.

* [2026/05] Using Muon Optimizer with DeepSpeed ...

Sections: Office Hours, Latest News, Extreme Speed and Scale for DL Training, DeepSpeed Adoption, Requirements, PyPI, Windows, Further Reading, Publications, Videos

</details>

### decord

Decord Video Loader

`pip install decord` · installs (wheel) · licence: Apache Software License · rank 3754 · last release 2021-06-14 · [PyPI](https://pypi.org/project/decord/)

### dagster-pandas

Utilities and examples for working with pandas and dagster, an opinionated framework for expressing data pipelines

`pip install dagster-pandas` · installs (wheel) · licence: Apache-2.0 · rank 3765 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-pandas/)

### dagster-gcp

Package for GCP-specific Dagster framework op and resource components.

`pip install dagster-gcp` · installs (wheel) · licence: Apache-2.0 · rank 3850 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-gcp/)

### dydantic

Dynamically generate pydantic models from JSON schema.

`pip install dydantic` · installs (wheel) · licence: MIT License · rank 3870 · last release 2025-01-29 · [PyPI](https://pypi.org/project/dydantic/)

<details><summary>README extract</summary>

Dydantic is a Python library for dynamically generating Pydantic models from JSON schemas. It provides a convenient way to create Pydantic models on-the-fly based on the structure defined in a JSON schema.

Features:
- Automatically generate Pydantic models from JSON schemas
- Support for nested objects and referenced definitions
- Customizable model configurations, base classes, and validators
- Handle various JSON schema types and formats ...

Example:
```python
from dydantic import create_model_from_schema

json_schema = {
    "title": "Person",
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
    },
    "required": ["name"],
}

Person = create_model_from_schema(json_schema)

person = Person(name="John", age=30)
...
```

...

</details>

### datasketches

The Apache DataSketches Library for Python

`pip install datasketches` · installs from source (sdist only) · licence: Apache License 2.0 · rank 3893 · last release 2025-03-01 · [PyPI](https://pypi.org/project/datasketches/)

<details><summary>README extract</summary>

This is the official version of the Apache DataSketches Python library.

In the analysis of big data there are often problem queries that don’t scale because they require huge compute resources and time to generate exact results. Examples include count distinct, quantiles, most-frequent items, joins, matrix computations, and graph analysis. ...

Sections: The Apache DataSketches Library for Python, Usage, Available Sketch Classes, Known Differences from C++, Unit tests

</details>

### docusign-esign

Docusign eSignature REST API

`pip install docusign-esign` · installs (wheel) · licence: not stated · rank 3914 · last release 2026-03-13 · [PyPI](https://pypi.org/project/docusign-esign/)

<details><summary>README extract</summary>

[][pypi-url]

The Docusign SDK makes integrating Docusign into your apps and websites a seamless experience.

Sections: The Official Docusign eSignature Python Client SDK, Introduction, Version Information, Requirements, Compatibility, Path setup, SDK Dependencies, API Reference, Code examples, OAuth implementations, Additional resources

</details>

### dagster-rest-resources

(no summary)

`pip install dagster-rest-resources` · installs (wheel) · licence: Apache-2.0 · rank 3929 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-rest-resources/)

### django-deprecate-fields

This package allows deprecating model fields and allows removing them in a backwards compatible manner.

`pip install django-deprecate-fields` · installs (wheel) · licence: Apache License 2.0 · rank 3960 · last release 2026-01-20 · [PyPI](https://pypi.org/project/django-deprecate-fields/)

<details><summary>README extract</summary>

Example:
```python
from django.db import models

class MyModel(models.Model):
    field1 = models.CharField()
    field2 = models.CharField()
```

Sections: Django - Deprecate Field, Usage, Custom django commands

</details>

### django-mptt

Utilities for implementing Modified Preorder Tree Traversal with your Django Models and working with trees of Model instances.

`pip install django-mptt` · installs (wheel) · licence: MIT License · rank 4002 · last release 2026-11-03 · [PyPI](https://pypi.org/project/django-mptt/)

<details><summary>README extract</summary>

django-mptt works by storing pre-computed left/right/level/tree_id values
alongside each row. This makes reads very fast, but it means that every
insert, move, or delete must update a potentially large number of sibling and
ancestor rows. ...

Features:
* Simple registration of models - fields required for tree structure will be
 added automatically.

* The tree structure is automatically updated when you create or delete
 model instances, or change an instance's parent. ...

Sections: This project is currently unmaintained, django-mptt, What is Modified Preorder Tree Traversal?, What is `django-mptt`?, Requirements, Feature overview

</details>

### databricks-bundles

Python support for Declarative Automation Bundles

`pip install databricks-bundles` · installs (wheel) · licence: not stated · rank 4067 · last release 2026-11-04 · [PyPI](https://pypi.org/project/databricks-bundles/)

<details><summary>README extract</summary>

Python for Declarative Automation Bundles extends Declarative Automation Bundles so that you can:
- Define jobs and pipelines as Python code. These jobs can coexist with jobs defined in YAML.
- Dynamically create jobs and pipelines using metadata.
- Modify jobs and pipelines defined in YAML or Python during bundle deployment. ...

Sections: databricks-bundles, Getting started, Privacy Notice

</details>

### dash-core-components

Core component suite for Dash

`pip install dash-core-components` · installs (wheel) · licence: MIT · rank 4085 · last release 2022-03-02 · [PyPI](https://pypi.org/project/dash-core-components/)

<details><summary>README extract</summary>

As of Dash 2, the development of dash-core-components has been moved to the main Dash repo

This package exists for backward compatibility

This package provides the core React component suite for Dash.

Sections: Notice, Dash Core Components, Code quality and tests, To run integration tests (test_integration.py), Publishing, Dash Component Boilerplate, Big Thanks

</details>

### databricks-ai-bridge

Official Python library for Databricks AI support

`pip install databricks-ai-bridge` · installs (wheel) · licence: not stated · rank 4103 · last release 2026-09-18 · [PyPI](https://pypi.org/project/databricks-ai-bridge/)

<details><summary>README extract</summary>

The Databricks AI Bridge library provides a shared layer of APIs to interact with Databricks AI features, such as Databricks AI/BI Genie and Vector Search. Use these packages to help author agents with Agent Framework on Databricks. ...

Sections: Databricks AI Bridge library, Integration Packages

</details>

### dash-html-components

Vanilla HTML components for Dash

`pip install dash-html-components` · installs (wheel) · licence: MIT · rank 4110 · last release 2022-03-02 · [PyPI](https://pypi.org/project/dash-html-components/)

<details><summary>README extract</summary>

As of Dash 2, the development of dash-html-components has been moved to the main Dash repo

This package exists for backward compatibility

Vanilla HTML components for Dash

Sections: Notice, dash-html-components, Generating HTML Components, Create a production build and publish

</details>

### dash-table

Dash table

`pip install dash-table` · installs (wheel) · licence: MIT · rank 4116 · last release 2022-03-02 · [PyPI](https://pypi.org/project/dash-table/)

<details><summary>README extract</summary>

As of Dash 2, the development of Dash Table has been moved to the main Dash repo

This package exists for backward compatibility

An interactive `DataTable` for Dash.

:point_right: Documentation

Example:
```python
import dash
import dash_table
import pandas as pd

df = pd.read_csv('

app = dash.Dash(name)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if name == 'main':
    app.run_server(debug=True)
```

Sections: Notice, Dash Table, Quickstart, Background

</details>

### drawsvg

A Python 3 library for programmatically generating SVG (vector) images and animations. Drawsvg can also render to PNG, MP4, and display your drawings in Jupyter notebook and Jupyter lab.

`pip install drawsvg` · installs (wheel) · licence: MIT License · rank 4139 · last release 2026-08-12 · [PyPI](https://pypi.org/project/drawsvg/)

<details><summary>README extract</summary>

A Python 3 library for programmatically generating SVG images and animations that can render and display your drawings in a Jupyter notebook or Jupyter lab.

Most common SVG tags are supported and others can easily be added by writing a small subclass of `DrawableBasicElement` or `DrawableParentElement`. ...

Example:
```python
import drawsvg as draw

d = draw.Drawing(200, 100, origin='center')

# Draw an irregular polygon
d.append(draw.Lines(-80, 45,
                     70, 49,
                     95, -49,
                    -90, -40,
                    close=False,
            fill='#eeee00',
            stroke='black'))

# Draw a rectangle
...
```

...

</details>

### datacontract-specification

The Pydantic Model of the Data Contract Specification

`pip install datacontract-specification` · installs (wheel) · licence: MIT License · rank 4175 · last release 2025-09-25 · [PyPI](https://pypi.org/project/datacontract-specification/)

<details><summary>README extract</summary>

The pip module `datacontract-specification` to read and write YAML files using the Data Contract Specification. The pip module was extracted from the Data Contract CLI, which is its primary user.

The version number of the pip module corresponds to the version of the Data Contract Specification it supports. ...

Example:
```python
from datacontract_specification.model import DataContractSpecification

# Load a data contract specification from a file
data_contract = DataContractSpecification.from_file('path/to/your/data_contract.yaml')
# Print the data contract specification as a YAML string
print(data_contract.to_yaml())
```

Sections: Data Contract Specification (Python), Version Mapping, Usage

</details>

### daytona_sdk

Deprecated: please migrate to the 'daytona' package. This alias is being phased out.

`pip install daytona_sdk` · installs (wheel) · licence: Apache-2.0 · rank 4188 · last release 2026-11-07 · [PyPI](https://pypi.org/project/daytona_sdk/)

<details><summary>README extract</summary>

This package is deprecated. Please migrate to the `daytona` package.

Then update your imports:

`daytona_sdk` currently ships the same code as `daytona` and will continue to
receive updates for a transition period so existing installs keep working.
However, it is being phased out and will eventually be discontinued. ...

Example:
```python
import daytona  # instead of: import daytona_sdk
```

</details>

### detect-test-pollution

a tool to detect test pollution

`pip install detect-test-pollution` · installs (wheel) · licence: MIT License · rank 4190 · last release 2023-09-28 · [PyPI](https://pypi.org/project/detect-test-pollution/)

<details><summary>README extract</summary>

a tool to detect test pollution

Example:
```python
k = 1

def test_k():
    assert k == 1

def test_k2():
    global k

    k = 2
    assert k == 2
```

Sections: detect-test-pollution, what is test pollution?, usage, fuzzing

</details>

### debtcollector

A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner.

`pip install debtcollector` · installs (wheel) · licence: Apache Software License · rank 4203 · last release 2026-03-24 · [PyPI](https://pypi.org/project/debtcollector/) · [source](https://opendev.org/openstack/debtcollector/)

<details><summary>README extract</summary>

A collection of Python deprecation patterns and strategies that help you
collect your technical debt in a non-destructive manner. The goal of this
library is to provide well documented developer facing deprecation
patterns that start of with a basic set and can expand into a larger
set of patterns as time goes on. ...

</details>

### django-allow-cidr

A Django Middleware to enable use of CIDR IP ranges in ALLOWED_HOSTS.

`pip install django-allow-cidr` · installs (wheel) · licence: Apache Software License · rank 4258 · last release 2025-04-08 · [PyPI](https://pypi.org/project/django-allow-cidr/)

<details><summary>README extract</summary>

A Django Middleware to enable use of CIDR IP ranges in ALLOWED_HOSTS.

Features:
* The normal `ALLOWED_HOSTS` values will also work as intended. This Middleware is intended to augment,
 not replace, the normal Django function. ...

Sections: Django Allow CIDR, Quickstart, Features, Running Tests, Pushing to PyPI, 0.8.0 (2025-04-08), 0.7.1 (2023-07-10), 0.7.0 (2023-07-10), 0.6.0 (2023-01-05), 0.5.0 (2022-07-09), 0.4.1 (2022-06-13), 0.4.0 (2022-02-22), 0.3.1 (2018-07-31), 0.3.0 (2018-02-21)

</details>

### dbfread

Read DBF Files with Python

`pip install dbfread` · installs (wheel) · licence: MIT · rank 4289 · last release 2016-11-25 · [PyPI](https://pypi.org/project/dbfread/)

<details><summary>README extract</summary>

DBF is a file format used by databases such dBase, Visual FoxPro, and
FoxBase+. This library reads DBF files and returns the data as native
Python data types for further processing. It is primarily intended for
batch jobs and one-off scripts.

By default records are streamed directly from the file. ...

Example:
```python
>>> from dbfread import DBF
>>> for record in DBF('people.dbf'):
...     print(record)
OrderedDict([('NAME', 'Alice'), ('BIRTHDATE', datetime.date(1987, 3, 1))])
OrderedDict([('NAME', 'Bob'), ('BIRTHDATE', datetime.date(1980, 11, 12))])
```

Sections: dbfread - Read DBF Files with Python, Main Features, Source code, API Changes, Contact

</details>

### draccus

A slightly opinionated framework for simple dataclass-based configurations based on Pyrallis.

`pip install draccus` · installs (wheel) · licence: MIT · rank 4328 · last release 2026-06-12 · [PyPI](https://pypi.org/project/draccus/) · [source](https://github.com/dlwh/draccus)

<details><summary>README extract</summary>

> Draccus: "A large herbivorous reptilian creature, known for their ability to breathe fire."

Draccus is a fork of the excellent Pyrallis library, but with
a few changes to make it more suitable for more complex use cases. The main changes are: ...

Features:
We support everything in Pyrallis (see their examples), but also support subtyping and including config files within
config files. We try to maintain the original repository's simple, clean approach. ...

Example:
```python
from dataclasses import dataclass
import draccus

@dataclass
class TrainConfig:
    """Training Config for Machine Learning"""
    workers: int = 8               # The number of workers for training
    exp_name: str = 'default_exp'  # The experiment name

@draccus.wrap()
def main(cfg: TrainConfig):
...
```

...

</details>

### databricks-mcp

MCP helpers for Databricks

`pip install databricks-mcp` · installs (wheel) · licence: Apache-2.0 · rank 4385 · last release 2026-07-31 · [PyPI](https://pypi.org/project/databricks-mcp/)

<details><summary>README extract</summary>

The `databricks-mcp` package provides useful helpers to integrate MCP Servers in Databricks

Features:
- OAuth Provider: Enables authentication across Databricks Notebooks, Model Serving, and local environments using the Databricks CLI.

Sections: Databricks MCP Library, From PyPI, From Source, Key Features

</details>

### dvc-s3

s3 plugin for dvc

`pip install dvc-s3` · installs (wheel) · licence: Apache-2.0 · rank 4431 · last release 2026-01-16 · [PyPI](https://pypi.org/project/dvc-s3/) · [docs](https://dvc.org/doc) · [source](https://github.com/iterative/dvc-s3)

<details><summary>README extract</summary>

s3 plugin for dvc

By default tests will be run against moto.
To run against real S3, set `DVC_TEST_AWS_REPO_BUCKET` with an AWS bucket name.

Sections: dvc-s3, Tests

</details>

### django-modeltranslation

Translates Django models using a registration approach.

`pip install django-modeltranslation` · installs (wheel) · licence: BSD-3-Clause · rank 4441 · last release 2026-09-07 · [PyPI](https://pypi.org/project/django-modeltranslation/) · [docs](https://django-modeltranslation.readthedocs.org/en/latest) · [source](https://github.com/deschler/django-modeltranslation)

<details><summary>README extract</summary>

The modeltranslation application is used to translate dynamic content of
existing Django models to an arbitrary number of languages without having to
change the original model classes. ...

Features:
- Add translations without changing existing models or views
- Translation fields are stored in the same table (no expensive joins)
- Supports inherited models (abstract and multi-table inheritance)
- Handle more than just text fields ...

Sections: Modeltranslation, Features

</details>

### darkdetect

Detect OS Dark Mode from Python

`pip install darkdetect` · installs (wheel) · licence: BSD License · rank 4455 · last release 2022-12-16 · [PyPI](https://pypi.org/project/darkdetect/)

<details><summary>README extract</summary>

This package allows to detect if the user is using Dark Mode on:

- macOS 10.14+
- Windows 10 1607+
- Linux with a dark GTK theme.

The main application of this package is to detect the Dark mode from your GUI Python application (Tkinter/wx/pyqt/qt for python (pyside)/...) and apply the needed adjustments to your interface. ...

Example:
```python
import darkdetect

>>> darkdetect.theme()
'Dark'

>>> darkdetect.isDark()
True

>>> darkdetect.isLight()
False
```

Sections: Darkdetect, Usage, Notes

</details>

### defusedcsv

Drop-in replacement for Python's CSV library that tries to mitigate CSV injection attacks

`pip install defusedcsv` · installs (wheel) · licence: Apache Software License · rank 4582 · last release 2025-09-02 · [PyPI](https://pypi.org/project/defusedcsv/)

<details><summary>README extract</summary>

If your Python application offers CSV export of user-generated data, that user-generated data might contain malicious
payloads that might trigger vulnerabilities in the spreadsheet software of the user that downloads the file (i.e. MS
Excel or LibreOffice). ...

Sections: defusedcsv, Usage, Useful Links

</details>

### diagrams

Diagram as Code

`pip install diagrams` · installs (wheel) · licence: MIT License · rank 4631 · last release 2025-11-22 · [PyPI](https://pypi.org/project/diagrams/) · [source](https://github.com/mingrammer/diagrams)

<details><summary>README extract</summary>

Diagram as Code.

Diagrams lets you draw the cloud system architecture in Python code. It was born for prototyping a new system architecture design without any design tools. You can also describe or visualize the existing system architecture as well. ...

Sections: Diagrams, Providers, Getting Started, Examples, Who uses it?, Other languages

</details>

### databricks-labs-remorph

SQL code converter and data reconcilation tool for accelerating data onboarding to Databricks from EDW, CDW and other ETL sources.

`pip install databricks-labs-remorph` · installs (wheel) · licence: not stated · rank 4636 · last release 2025-06-08 · [PyPI](https://pypi.org/project/databricks-labs-remorph/) · [docs](https://github.com/databrickslabs/remorph) · [source](https://github.com/databrickslabs/remorph)

<details><summary>README extract</summary>

Databricks Labs Remorph

> No further updates, bug fixes, or support will be provided for Remorph, please use Lakebridge instead.

</details>

### django-browser-reload

Automatically refresh your browser on changes to Python code, templates, or static files.

`pip install django-browser-reload` · installs (wheel) · licence: MIT · rank 4645 · last release 2025-09-22 · [PyPI](https://pypi.org/project/django-browser-reload/) · [source](https://github.com/adamchainz/django-browser-reload)

<details><summary>README extract</summary>

Automatically refresh your browser on changes to Python code, templates, or static files.

Work smarter and faster with my book Boost Your Django DX which covers django-browser-reload and many other tools.
I wrote django-browser-reload whilst working on the book!

Python 3.9 to 3.14 supported.

Django 4.2 to 6.0 supported. ...

Example:
```python
# myproject/jinja2.py
from jinja2 import Environment
from django_browser_reload.jinja import django_browser_reload_script

def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            # ...
            "django_browser_reload_script": django_browser_reload_script,
        }
    )
    return env
```

Sections: django-browser-reload, Requirements, Usage, Template tag, Example project, How it works

</details>

### dbt-fabric

A Microsoft Fabric Synapse Data Warehouse adapter plugin for dbt

`pip install dbt-fabric` · does not install on CPython 3.14 · licence: MIT · rank 4688 · last release 2026-10-26 · [PyPI](https://pypi.org/project/dbt-fabric/) · [source](https://github.com/microsoft/dbt-fabric)

<details><summary>README extract</summary>

dbt adapter for Microsoft Fabric Synapse Data Warehouse.

The 1.12.x adapter series requires dbt-core 1.12 or newer.
Adapter minor versions follow the corresponding dbt-core minor version.

We've bundled all documentation on the dbt docs site
* Profile setup & authentication
* Adapter documentation, usage and important notes

Sections: dbt-fabric, Documentation, dbt package compatibility, dbt_artifacts upstream dependency, dbt_constraints limitations, Performance guidance for large projects

</details>

### dingtalk-stream

A Python library for sending messages to DingTalk chatbot

`pip install dingtalk-stream` · installs (wheel) · licence: MIT License · rank 4710 · last release 2025-10-24 · [PyPI](https://pypi.org/project/dingtalk-stream/)

<details><summary>README extract</summary>

Python SDK for DingTalk Stream Mode API, Compared with the webhook mode, it is easier to access the DingTalk chatbot

钉钉支持 Stream 模式接入事件推送、机器人收消息以及卡片回调，该 SDK 实现了 Stream 模式。相比 Webhook 模式，Stream 模式可以更简单的接入各类事件和回调。

1. 安装 SDK

2. 开发一个 Stream 机器人

以下示例注册一个加法处理会调，可以实现一个加法机器人（给机器人发送1+1，回复2）

Example:
```python
# !/usr/bin/env python

import argparse
import logging
from dingtalk_stream import AckMessage
import dingtalk_stream

def setup_logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter('%(asctime)s %(name)-8s %(levelname)-8s %(message)s [%(filename)s:%(lineno)d]'))
...
```

Sections: DingTalk Stream Mode 介绍, 快速指南, 高阶使用方法, 开发教程, 特别说明, 参考资料

</details>

### djangorestframework-camel-case

Camel case JSON support for Django REST framework.

`pip install djangorestframework-camel-case` · installs from source (sdist only) · licence: BSD License · rank 4725 · last release 2023-02-13 · [PyPI](https://pypi.org/project/djangorestframework-camel-case/)

<details><summary>README extract</summary>

Camel case JSON support for Django REST framework.

Example:
```python
from djangorestframework_camel_case.parser import CamelCaseJSONParser
from rest_framework.generics import CreateAPIView

class NoUnderscoreBeforeNumberCamelCaseJSONParser(CamelCaseJSONParser):
    json_underscoreize = {'no_underscore_before_number': True}

class MyView(CreateAPIView):
    queryset = MyModel.objects.all()
...
```

Sections: Django REST Framework JSON CamelCase, Swapping Renderer, Ignore Fields, Ignore Keys, Running Tests, 1.4.2 (2023-02-13), 1.4.1 (2023-02-13), 1.4.0 (2023-02-09), 1.3.0 (2021-11-14), 1.2.0 (2020-06-16), 1.1.2 (2019-10-22), 1.1.1 (2019-09-09), 1.1.0 (2019-09-09), 0.1.0 (2013-12-20)

</details>

### django-money

Adds support for using money and currency fields in django models and forms. Uses py-moneyed as the money implementation.

`pip install django-money` · installs (wheel) · licence: BSD · rank 4735 · last release 2026-10-14 · [PyPI](https://pypi.org/project/django-money/)

<details><summary>README extract</summary>

A little Django app that uses py-moneyed to add support for Money
fields in your models and forms.

* Django versions supported: 4.2, 5.0, 5.1, 5.2
* Python versions supported: 3.10, 3.11, 3.12, 3.13
* PyPy versions supported: PyPy3 ...

Example:
```python
from djmoney.models.fields import MoneyField
from django.db import models

class BankAccount(models.Model):
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
```

Sections: django-money, Model usage, Callable defaults, Configuring currency choices, Field validation, Constructing form data, Adding a new Currency, Important note on model managers, Note on serialization, Format localization, Working with Exchange Rates, Usage with Django REST Framework, Customization, Background

</details>

### django-pghistory

History tracking for Django and Postgres

`pip install django-pghistory` · installs (wheel) · licence: BSD License · rank 4743 · last release 2026-02-17 · [PyPI](https://pypi.org/project/django-pghistory/) · [docs](https://django-pghistory.readthedocs.io) · [source](https://github.com/AmbitionEng/django-pghistory)

<details><summary>README extract</summary>

Example:
```python
import pghistory

@pghistory.track()
class TrackedModel(models.Model):
    int_field = models.IntegerField()
    text_field = models.TextField()
```

Sections: Quick Start, Compatibility, Documentation, Other Material, Creator

</details>

### djangorestframework-types

Type stubs for Django Rest Framework

`pip install djangorestframework-types` · installs (wheel) · licence: MIT License · rank 4756 · last release 2024-10-10 · [PyPI](https://pypi.org/project/djangorestframework-types/) · [source](https://github.com/sbdchd/djangorestframework-types)

<details><summary>README extract</summary>

Type stubs for Django Rest Framework.

> Note: this project was forked from
> < with the goal of
> removing the `mypy` plugin dependency so
> that `mypy` can't crash due to Django
> config, and that
> non-`mypy` type checkers like
> `pyright` will work better with
> Django Rest Framework.

Sections: djangorestframework-types, related

</details>

### datafusion

Build and run queries against data

`pip install datafusion` · installs (wheel) · licence: OSI Approved; Apache Software License · rank 4819 · last release 2026-10-12 · [PyPI](https://pypi.org/project/datafusion/) · [docs](https://datafusion.apache.org/python) · [source](https://github.com/apache/datafusion-python)

<details><summary>README extract</summary>

<!---
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements. See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership. ...

Features:
- Execute queries using SQL or DataFrames against CSV, Parquet, and JSON data sources.
- Queries are optimized using DataFusion's query optimizer.
- Execute user-defined Python code from SQL. ...

Example:
```python
from datafusion import SessionContext

# Create a DataFusion context
ctx = SessionContext()

# Register table with context
ctx.register_parquet('taxi', 'yellow_tripdata_2021-01.parquet')

# Execute SQL
df = ctx.sql("select passenger_count, count(*) "
             "from taxi "
             "where passenger_count is not null "
...
```

...

</details>

### docx-revisions

Track changes (revisions) support for python-docx: read, write and manipulate <w:ins> and <w:del> elements

`pip install docx-revisions` · installs (wheel) · licence: MIT · rank 4845 · last release 2026-04-14 · [PyPI](https://pypi.org/project/docx-revisions/) · [docs](https://balalofernandez.github.io/docx-revisions) · [source](https://github.com/balalofernandez/docx-revisions)

<details><summary>README extract</summary>

Read and write track changes in Word documents (.docx) with Python. docx-revisions extends python-docx to support document revision tracking, change tracking, and OOXML revision markup (insertions `` and deletions ``) so you can programmatically accept text, list revisions with author and date, and apply insertions, deletions, or replacements with ...

Example:
```python
from docx_revisions import RevisionDocument

rdoc = RevisionDocument("tracked_changes.docx")
for para in rdoc.paragraphs:
    if para.has_track_changes:
        for change in para.track_changes:
            print(f"{type(change).name}: '{change.text}' by {change.author}")
        print(f"Accepted: {para.accepted_text}")
...
```

...

</details>

### django-multiselectfield

Django multiple select field

`pip install django-multiselectfield` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 4860 · last release 2025-06-12 · [PyPI](https://pypi.org/project/django-multiselectfield/)

_README extract left out: share-alike licence._

### daqp

DAQP: A dual active-set QP solver

`pip install daqp` · installs (wheel) · licence: MIT · rank 4875 · last release 2026-11-02 · [PyPI](https://pypi.org/project/daqp/)

<details><summary>README extract</summary>

DAQP is a dual active-set solver that solves convex quadratic programs of the form
Binary constraints of the form $A x \in \lbrace b_l, b_u \rbrace$ are also supported, allowing for mixed-integer quadratic programs to be solved.

The code is written in C and is *library free*. DAQP can be interfaced to C, Julia, MATLAB, and Python. ...

Sections: DAQP, Citing DAQP

</details>

### dukpy

Simple JavaScript interpreter for Python

`pip install dukpy` · installs (wheel) · licence: MIT · rank 4880 · last release 2026-07-23 · [PyPI](https://pypi.org/project/dukpy/)

<details><summary>README extract</summary>

DukPy is a simple JavaScript interpreter for Python **without any external
runtime dependency**.

The name comes from DukPy's original Duktape-based implementation and is kept
for package compatibility.

It comes with a bunch of common transpilers built-in for convenience:

 - *TypeScript*
 - *JSX*
 - *LESS* ...

Example:
```python
>>> import dukpy
>>> dukpy.typescript_compile('''
... class Greeter {
...     constructor(public greeting: string) { }
...     greet() {
...         return "
# " + this.greeting + "
";
...     }
... };
...
... var greeter = new Greeter("Hello, world!");
... ''')
...
```

...

</details>

### django-annoying

This is a django application that tries to eliminate annoying things in the Django framework.

`pip install django-annoying` · installs (wheel) · licence: BSD License · rank 4927 · last release 2025-04-03 · [PyPI](https://pypi.org/project/django-annoying/)

<details><summary>README extract</summary>

Features:

 - render_to decorator - Reduce typing in django views.
 - signals decorator - Allow using signals as decorators.
 - ajax_request decorator - Returns JsonResponse with dict as content.
 - autostrip decorator - Strip form text fields before validation. ...

</details>

### dapr

The official release of Dapr Python SDK.

`pip install dapr` · installs (wheel) · licence: Apache Software License · rank 4967 · last release 2026-10-22 · [PyPI](https://pypi.org/project/dapr/) · [docs](https://github.com/dapr/docs) · [source](https://github.com/dapr/python-sdk)

<details><summary>README extract</summary>

<!-- IGNORE_LINKS -->

<!-- END_IGNORE -->

Dapr is a portable, event-driven, serverless runtime for building distributed applications across cloud and edge.

Dapr SDK for Python allows you to implement the Virtual Actor model, based on the actor design pattern. This SDK can run locally, in a container and in any distributed systems environment. ...

Sections: Dapr SDK for Python, Getting started, Prerequisites, Try out examples, Build and test, Documentation, Generate gRPC Protobuf client, Help & Feedback

</details>

### delta-kernel-rust-sharing-wrapper

(no summary)

`pip install delta-kernel-rust-sharing-wrapper` · installs (wheel) · licence: Apache-2.0 · rank 4976 · last release 2026-10-28 · [PyPI](https://pypi.org/project/delta-kernel-rust-sharing-wrapper/)

<details><summary>README extract</summary>

This adds a thin python bindings via maturin and pyo3 for delta-kernel-rust.

Sections: Delta Kernel Rust Sharing Wrapper, usage

</details>

### DafnyRuntimePython

Dafny runtime for Python

`pip install DafnyRuntimePython` · installs (wheel) · licence: MIT License · rank 4999 · last release 2025-08-25 · [PyPI](https://pypi.org/project/DafnyRuntimePython/)

### dash-ag-grid

Dash wrapper around AG Grid, the best interactive data grid for the web.

`pip install dash-ag-grid` · installs (wheel) · licence: MIT License · rank 5029 · last release 2026-07-15 · [PyPI](https://pypi.org/project/dash-ag-grid/) · [docs](https://dash.plotly.com/dash-ag-grid) · [source](https://github.com/plotly/dash-ag-grid)

<details><summary>README extract</summary>

Dash AG Grid is a Dash component wrapper for the AG Grid JavaScript package, enabling you to display AG Grid components natively in your Dash app.

The underlying AG Grid JavaScript package is a third-party software component developed by AG Grid Ltd. Many features are available for free in the AG Grid Community version. ...

Example:
```python
import dash_ag_grid as dag
from dash import Dash
import pandas as pd

app = Dash()

df = pd.read_csv("

app.layout = dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
)

app.run(debug=True)
```

Sections: Dash AG Grid, Documentation, Quick Start, AG Grid Enterprise features

</details>

### dbt-trino

The trino adapter plugin for dbt (data build tool)

`pip install dbt-trino` · installs (wheel) · licence: Apache Software License · rank 5079 · last release 2026-10-26 · [PyPI](https://pypi.org/project/dbt-trino/)

<details><summary>README extract</summary>

dbt is a data transformation workflow tool that lets teams quickly and collaboratively deploy analytics code, following software engineering best practices like modularity, CI/CD, testing, and documentation. It enables anyone who knows SQL to build production-grade data pipelines. ...

Sections: dbt-trino, Introduction, Compatibility, Setup & Configuration, Trino- and Starburst-specific configuration, Query routing, User-defined functions (SQL UDFs), Backport process

</details>

### django-modelcluster

Django extension to allow working with 'clusters' of models as a single unit, independently of the database

`pip install django-modelcluster` · installs (wheel) · licence: BSD-3-Clause · rank 5121 · last release 2026-05-01 · [PyPI](https://pypi.org/project/django-modelcluster/)

<details><summary>README extract</summary>

If you had a data model like this:

wouldn't it be nice if you could construct bundles of objects like this, independently of the database:

Unfortunately, you can't. Objects need to exist in the database for foreign key relations to work: ...

Example:
```python
class Band(models.Model):
    name = models.CharField(max_length=255)

class BandMember(models.Model):
    band = models.ForeignKey('Band', related_name='members', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
```

Sections: django-modelcluster, Many-to-many relations, Introspection

</details>

### django-zeal

Detect N+1s in your Django app

`pip install django-zeal` · installs (wheel) · licence: not stated · rank 5137 · last release 2026-10-14 · [PyPI](https://pypi.org/project/django-zeal/)

<details><summary>README extract</summary>

Catch N+1 queries in your Django project.

🔥 Battle-tested at Cinder

Features:
- Detects N+1s from missing prefetches and from use of `.defer()`/`.only()`/`.get()`
- Friendly error messages like `N+1 detected on social.User.followers at myapp/views.py:25 in get_user`
- Configurable thresholds
- Allow-list
- Well-tested ...

Example:
```python
from celery.signals import task_prerun, task_postrun
from zeal import setup, teardown
from django.conf import settings

@task_prerun.connect()
def setup_zeal(*args, **kwargs):
    setup()

@task_postrun.connect()
def teardown_zeal(*args, **kwargs):
    teardown()
```

Sections: django-zeal, Features, Celery, Tests, Generic setup, Configuration, Debugging N+1s, Comparison to nplusone

</details>

### dictor

an elegant dictionary and JSON handler

`pip install dictor` · installs from source (sdist only) · licence: MIT · rank 5157 · last release 2023-09-15 · [PyPI](https://pypi.org/project/dictor/)

<details><summary>README extract</summary>

ATTENTION: Dictor version 0.1.13 and up will be dropping support for Python 2

Dictor is a Python JSON and Dictionary (Hash, Map) handler.

Dictor takes a dictionary or JSON data and returns value for a specific key. ...

Features:
using the built-in dict.get() does not parse the full body of a dict.

This method works if parsing a simple key=value structure, for example:

 data = {"name": "Joe"} ...

Example:
```python
from dictor import dictor

with open('sample.json') as data:
    data = json.load(data)

print(dictor(data, 'characters'))

...
```

...

</details>

### django-webpack-loader

Transparently use webpack with django

`pip install django-webpack-loader` · installs (wheel) · licence: MIT License · rank 5174 · last release 2026-05-13 · [PyPI](https://pypi.org/project/django-webpack-loader/)

<details><summary>README extract</summary>

Integrate Webpack bundles in Django templates by using a simple template tag:

Behind the scenes, Django Webpack Loader consumes a stats file generated by webpack-bundle-tracker and lets you use the generated bundles in Django.

A changelog is available.

Example:
```python
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'webpack_bundles/',
        'CACHE': not DEBUG,
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
    }
}
```

...

</details>

### docx

The docx module creates, reads and writes Microsoft Office Word 2007 docx files

`pip install docx` · installs from source (sdist only) · licence: UNKNOWN · rank 5207 · last release 2014-02-06 · [PyPI](https://pypi.org/project/docx/)

<details><summary>README extract</summary>

The docx module creates, reads and writes Microsoft Office Word 2007 docx
files.

These are referred to as 'WordML', 'Office Open XML' and 'Open XML' by
Microsoft.

These documents can be opened in Microsoft Office 2007 / 2010, Microsoft Mac
Office 2008, Google Docs, OpenOffice.org 3, and Apple iWork 08.

They also validate as well formed XML. ...

Sections: Python docx, Introduction, Making documents, Editing documents, Getting started, Making and Modifying Documents, Extracting Text from a Document, Ideas & To Do List, We love forks, changes and pull requests!, Want to talk? Need help?

</details>

### django-watchfiles

Make Django’s autoreloader more efficient by watching for changes with watchfiles.

`pip install django-watchfiles` · installs (wheel) · licence: MIT · rank 5245 · last release 2025-09-22 · [PyPI](https://pypi.org/project/django-watchfiles/) · [source](https://github.com/adamchainz/django-watchfiles)

<details><summary>README extract</summary>

Make Django’s autoreloader more efficient by watching for changes with watchfiles.

Improve your Django and Git skills with my books.

Python 3.9 to 3.14 supported.

Django 4.2 to 6.0 supported.

Sections: django-watchfiles, Requirements, Usage

</details>

### dbt-athena-community

The athena adapter plugin for dbt (data build tool)

`pip install dbt-athena-community` · installs (wheel) · licence: Apache Software License · rank 5271 · last release 2026-09-07 · [PyPI](https://pypi.org/project/dbt-athena-community/) · [docs](https://docs.getdbt.com) · [source](https://github.com/dbt-labs/dbt-adapters.git#subdirectory=dbt-athena)

<details><summary>README extract</summary>

- Features
 - Quick start
 - Installation
 - Prerequisites
 - Credentials
 - Configuring your profile
 - Additional information
 - Models
 - Table configuration
 - Table location
 - Incremental models
 - On schema change
 - Iceberg
 - Highly available table (HA)
 - HA known issues
 - Update glue data catalog
 - Snapshots
 - Timestamp strategy
 - ...

Features:
- Supports dbt version `1.7.*`
- Support for Python
- Supports seeds
- Correctly detects views and their columns
- Supports table materialization
 - Iceberg tables are supported only with Athena Engine v3 and a unique table location
 (see table ...

Example:
```python
import pandas as pd

def model(dbt, session):
    dbt.config(materialized="table")

    model_df = pd.DataFrame({"A": [1, 2, 3, 4]})

    return model_df
```

...

</details>

### decord2

Decord2 is a high-performance, efficient video decoding and loading library for deep learning research, featuring smart shuffling, random frame access, GPU acceleration, and seamless integration with popular frameworks.

`pip install decord2` · installs (wheel) · licence: Apache-2.0 · rank 5302 · last release 2026-05-30 · [PyPI](https://pypi.org/project/decord2/)

### django-permissionedforms

Django extension for creating forms that vary according to user permissions

`pip install django-permissionedforms` · installs (wheel) · licence: BSD License · rank 5358 · last release 2022-02-28 · [PyPI](https://pypi.org/project/django-permissionedforms/)

<details><summary>README extract</summary>

`django-permissionedforms` is an extension to Django's forms framework, allowing you to define forms where certain fields are shown or omitted according to the user's permissions.

Installation

Run: `pip install django-permissionedforms`

Usage ...

Example:
```python
from permissionedforms import PermissionedForm

class PersonForm(PermissionedForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        field_permissions = {
            'last_name': 'myapp.change_last_name'
        }
```

</details>

### dbt-sqlserver

A Microsoft SQL Server adapter plugin for dbt

`pip install dbt-sqlserver` · installs (wheel) · licence: MIT License · rank 5364 · last release 2026-11-03 · [PyPI](https://pypi.org/project/dbt-sqlserver/) · [source](https://github.com/dbt-msft/dbt-sqlserver)

<details><summary>README extract</summary>

dbt adapter for Microsoft SQL Server and Azure SQL services.

The adapter supports dbt-core 1.12 or newer and follows the same versioning scheme.
E.g. version 1.12.x of the adapter is compatible with dbt-core 1.12.x.

Sections: dbt-sqlserver, Documentation, Backend requirements at a glance, `pyodbc` backend, `mssql-python` backend, `adbc` backend *(experimental), Configuration, `dbt_sqlserver_use_default_schema_concat`, `backend`, `dbt_sqlserver_enable_safe_type_expansion`, `pre_hook_transaction_scope`, `dbt_sqlserver_use_dbt_transactions`, `dbt_sqlserver_use_native_string_types`, `xact_abort`

</details>

### django-log-request-id

Django middleware and log filter to attach a unique ID to every log message generated as part of a request

`pip install django-log-request-id` · installs (wheel) · licence: BSD-3-Clause · rank 5372 · last release 2026-03-12 · [PyPI](https://pypi.org/project/django-log-request-id/) · [source](https://github.com/dabapps/django-log-request-id/)

<details><summary>README extract</summary>

Django middleware and log filter to attach a unique ID to every log message generated as part of a request.

Author: Jamie Matthews, @j4mie

Example

Why?

So you can grep (or otherwise search) a set of logs for a high-traffic application to isolate all messages associated with a single request.

How?

The request ID is stored in a `ContextVar`. ...

Example:
```python
import logging
logger = logging.getLogger(name)
logger.debug("A wild log message appears!")
```

</details>

### diskcache-weave

Disk Cache -- Disk and file backed persistent cache.

`pip install diskcache-weave` · installs (wheel) · licence: Apache Software License · rank 5476 · last release 2026-03-19 · [PyPI](https://pypi.org/project/diskcache-weave/) · [docs](http://www.grantjenks.com/docs/diskcache/) · [source](https://github.com/grantjenks/python-diskcache)

<details><summary>README extract</summary>

DiskCache is an Apache2 licensed disk and file backed cache library, written
in pure-Python, and compatible with Django.

The cloud-based computing of 2023 puts a premium on memory. Gigabytes of empty
space is left on disks as processes vie for memory. Among these processes is
Memcached (and sometimes Redis) which is used as a cache. ...

Features:
- Pure-Python
- Fully Documented
- Benchmark comparisons (alternatives, Django cache backends)
- 100% test coverage
- Hours of stress testing
- Performance matters
- Django compatible API
- Thread-safe and process-safe ...

Example:
```python
>>> import diskcache
>>> help(diskcache)                             # doctest: +SKIP
```

Sections: DiskCache: Disk Backed Cache, Testimonials, Features, Quickstart, User Guide, Comparisons, Reference

</details>

### django-ordered-model

Allows Django models to be ordered and provides a simple admin interface for reordering them.

`pip install django-ordered-model` · installs (wheel) · licence: BSD License · rank 5489 · last release 2023-03-17 · [PyPI](https://pypi.org/project/django-ordered-model/)

<details><summary>README extract</summary>

django-ordered-model allows models to be ordered and provides a simple admin
interface for reordering them.

Based on and

See our compatability notes for the appropriate version to use with older Django and Python releases.

Installation

Please install using Pip:

Or if you have checked out the repository: ...

Example:
```python
from django.db import models
from ordered_model.models import OrderedModel

class Item(OrderedModel):
    name = models.CharField(max_length=100)
```

Sections: django-ordered-model, Swap positions, Move position up on position, Move to arbitrary position, Move object above or below reference, Move to top of stack, Move to bottom of stack, Updating fields that would be updated during save(), Get the previous or next objects, Subset Ordering

</details>

### databricks-langchain

Support for Databricks AI support in LangChain

`pip install databricks-langchain` · installs (wheel) · licence: Apache-2.0 · rank 5497 · last release 2026-10-27 · [PyPI](https://pypi.org/project/databricks-langchain/)

<details><summary>README extract</summary>

The `databricks-langchain` package provides seamless integration of Databricks AI features into LangChain applications. This repository is now the central hub for all Databricks-related LangChain components, consolidating previous packages such as `langchain-databricks` and `langchain-community`.

Features:
- LLMs Integration: Use Databricks-hosted large language models (LLMs) like Llama and Mixtral through `ChatDatabricks`.
- Vector Search: Store and query vector representations using `DatabricksVectorSearch`. ...

Example:
```python
from databricks_langchain import ChatDatabricks

llm = ChatDatabricks(endpoint="databricks-meta-llama-3-1-70b-instruct")
```

...

</details>

### django-upgrade

Automatically upgrade your Django project code.

`pip install django-upgrade` · installs (wheel) · licence: MIT · rank 5556 · last release 2026-10-02 · [PyPI](https://pypi.org/project/django-upgrade/) · [docs](https://django-upgrade.readthedocs.io/) · [source](https://github.com/adamchainz/django-upgrade)

<details><summary>README extract</summary>

Automatically upgrade your Django project code.

Please see

Sections: django-upgrade, Documentation

</details>

### dbt-state

dbt plugin that skips redundant model executions by caching results from previous runs

`pip install dbt-state` · installs (wheel) · licence: not stated · rank 5602 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dbt-state/)

<details><summary>README extract</summary>

dbt plugin that skips redundant model executions by caching results from previous runs. Learn more at state.dbt.com.

</details>

### drf-standardized-errors

Standardize your API error responses.

`pip install drf-standardized-errors` · installs (wheel) · licence: MIT License · rank 5612 · last release 2026-04-29 · [PyPI](https://pypi.org/project/drf-standardized-errors/) · [docs](https://drf-standardized-errors.readthedocs.io/en/latest/) · [source](https://github.com/ghazi-git/drf-standardized-errors)

<details><summary>README extract</summary>

Standardize your DRF API error responses.

By default, the package will convert all API error responses (4xx and 5xx) to the following standardized format:

Features:
- Highly customizable: gives you flexibility to define your own standardized error responses and override
specific aspects the exception handling process without having to rewrite everything.
- Supports nested serializers and ListSerializer errors ...

Sections: DRF Standardized Errors, Features, Requirements, Quickstart, Notes, Integration with DRF spectacular, Links

</details>

### djangoql

DjangoQL: Advanced search language for Django

`pip install djangoql` · installs (wheel) · licence: MIT License · rank 5680 · last release 2026-01-27 · [PyPI](https://pypi.org/project/djangoql/)

<details><summary>README extract</summary>

Advanced search language for Django, with auto-completion. Supports logical
operators, parenthesis, table joins, and works with any Django model. Tested on
Python 2.7, 3.6–3.14, Django 1.8–6.0. The auto-completion feature has been
tested in Chrome, Firefox, Safari, IE9+.

See a video: DjangoQL demo

DjangoQL is used by: ...

Example:
```python
from django.contrib import admin

from djangoql.admin import DjangoQLSearchMixin

from .models import Book

@admin.register(Book)
class BookAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    pass
```

Sections: DjangoQL, Add it to your Django admin, Using DjangoQL with the standard Django admin search, Language reference, DjangoQL Schema, Custom search fields

</details>

### dapr-ext-workflow

Dapr Workflow Authoring Extension for the Dapr Python SDK.

`pip install dapr-ext-workflow` · installs (wheel) · licence: Apache Software License · rank 5693 · last release 2026-07-15 · [PyPI](https://pypi.org/project/dapr-ext-workflow/) · [docs](https://github.com/dapr/docs) · [source](https://github.com/dapr/python-sdk)

<details><summary>README extract</summary>

This is the workflow authoring extension for Dapr Workflow

Sections: dapr-ext-workflow extension, References

</details>

### django-fernet-encrypted-fields

Symmetrically encrypted model fields for Django

`pip install django-fernet-encrypted-fields` · installs (wheel) · licence: not stated · rank 5724 · last release 2026-04-14 · [PyPI](https://pypi.org/project/django-fernet-encrypted-fields/)

<details><summary>README extract</summary>

This package was created as a successor to django-encrypted-fields.

Example:
```python
from encrypted_fields.fields import EncryptedTextField

class MyModel(models.Model):
    text_field = EncryptedTextField()
```

Sections: Django Fernet Encrypted Fields, Getting Started, Rotating SALT keys, Rotating SECRET_KEY, Available Fields, Compatible Django Version

</details>

### django-permissions-policy

Set the Permissions-Policy HTTP header on your Django app.

`pip install django-permissions-policy` · installs (wheel) · licence: MIT · rank 5734 · last release 2026-09-16 · [PyPI](https://pypi.org/project/django-permissions-policy/) · [source](https://github.com/adamchainz/django-permissions-policy)

<details><summary>README extract</summary>

Set the `Permissions-Policy` HTTP header on your Django app.

Work smarter and faster with my book Boost Your Django DX which covers many ways to improve your development experience.

Python 3.10 to 3.15 supported.

Django 5.2 to 6.1 supported.

Example:
```python
from django.shortcuts import render
from django_permissions_policy.decorators import permissions_policy_override

@permissions_policy_override(
    {
        "geolocation": [],
    }
)
def puppy_park_view(request):
    return render(request, "puppies/park.html")
```

Sections: django-permissions-policy, Requirements, Settings, Middleware arguments, Examples, Decorators, `permissions_policy_override(config)`, `permissions_policy_report_only_override(config)`

</details>

### dagster-spark

Package for Spark Dagster framework components.

`pip install dagster-spark` · installs (wheel) · licence: Apache-2.0 · rank 5763 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-spark/)

### dagster-pyspark

Package for PySpark Dagster framework components.

`pip install dagster-pyspark` · installs (wheel) · licence: Apache-2.0 · rank 5802 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-pyspark/)

### django-choices-field

Django field that set/get django's new TextChoices/IntegerChoices enum.

`pip install django-choices-field` · installs (wheel) · licence: MIT License · rank 5853 · last release 2025-12-27 · [PyPI](https://pypi.org/project/django-choices-field/) · [docs](https://django-choices-field.readthedocs.io) · [source](https://github.com/bellini666/django-choices-field)

<details><summary>README extract</summary>

Django field that set/get django's new TextChoices/IntegerChoices enum.

Example:
```python
import enum

from django.db import models
from django_choices_field import TextChoicesField, IntegerChoicesField, IntegerChoicesFlag

class MyModel(models.Model):
    class TextEnum(models.TextChoices):
        FOO = "foo", "Foo Description"
        BAR = "bar", "Bar Description"

    class IntegerEnum(models.IntegerChoices):
...
```

Sections: django-choices-field, Usage

</details>

### django-pg-zero-downtime-migrations

Django postgresql backend that apply migrations with respect to database locks

`pip install django-pg-zero-downtime-migrations` · installs (wheel) · licence: MIT · rank 5941 · last release 2026-08-26 · [PyPI](https://pypi.org/project/django-pg-zero-downtime-migrations/) · [source](https://github.com/tbicr/django-pg-zero-downtime-migrations)

<details><summary>README extract</summary>

Django postgresql backend that apply migrations with respect to database locks.

Sections: django-pg-zero-downtime-migrations, Usage, Differences with standard django backend, Deployment flow, Settings, ZERO_DOWNTIME_MIGRATIONS_LOCK_TIMEOUT, ZERO_DOWNTIME_MIGRATIONS_STATEMENT_TIMEOUT, ZERO_DOWNTIME_MIGRATIONS_FLEXIBLE_STATEMENT_TIMEOUT, ZERO_DOWNTIME_MIGRATIONS_RAISE_FOR_UNSAFE, ZERO_DOWNTIME_DEFERRED_SQL, ZERO_DOWNTIME_MIGRATIONS_IDEMPOTENT_SQL, ZERO_DOWNTIME_MIGRATIONS_EXPLICIT_CONSTRAINTS_DROP, ZERO_DOWNTIME_MIGRATIONS_KEEP_DEFAULT, PgBouncer and timeouts

</details>

### dagster-databricks

Package for Databricks-specific Dagster framework op and resource components.

`pip install dagster-databricks` · installs (wheel) · licence: Apache-2.0 · rank 5969 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-databricks/)

### dvc-gs

gs plugin for dvc

`pip install dvc-gs` · installs (wheel) · licence: Apache-2.0 · rank 5981 · last release 2026-06-09 · [PyPI](https://pypi.org/project/dvc-gs/) · [docs](https://dvc.org/doc) · [source](https://github.com/iterative/dvc-gs)

### daft

Distributed Dataframes for Multimodal Data

`pip install daft` · installs (wheel) · licence: not stated · rank 5988 · last release 2026-10-06 · [PyPI](https://pypi.org/project/daft/) · [source](https://github.com/Eventual-Inc/Daft)

<details><summary>README extract</summary>

Website • Docs • Installation • Daft Quickstart • Community and Support

Daft is a high-performance data engine for AI and multimodal workloads. Process images, audio, video, and structured data at any scale. ...

Sections: Getting Started, Quickstart, More Resources, Benchmarks, Telemetry, Related Projects

</details>

### dagster-snowflake

Package for Snowflake Dagster framework components.

`pip install dagster-snowflake` · installs (wheel) · licence: Apache-2.0 · rank 5990 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-snowflake/)

### delta

Human friendly context aware duration parsing library

`pip install delta` · installs from source (sdist only) · licence: MIT · rank 5991 · last release 2016-08-06 · [PyPI](https://pypi.org/project/delta/)

### django-solo

Django Solo helps working with singletons

`pip install django-solo` · installs (wheel) · licence: CC-BY-3.0 · rank 5999 · last release 2026-11-04 · [PyPI](https://pypi.org/project/django-solo/) · [source](https://github.com/lazybird/django-solo/)

<details><summary>README extract</summary>

+---------------------------+
 | |
 | |
 | \ | Django Solo helps working with singletons:
 | /\ | database tables that only have one row.
 | >=)'> | Singletons are useful for things like global
 | \/ | settings that you want to edit from the admin
 | / | instead of having them in Django settings.py.
 | |
 | |
 +---------------------------+ ...

Example:
```python
# models.py

from django.db import models
from solo.models import SingletonModel

class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default="Site Name")
    maintenance_mode = models.BooleanField(default=False)

    def str(self):
        return "Site Configuration"

    class Meta:
...
```

...

</details>

### ddddocr

带带弟弟OCR

`pip install ddddocr` · installs (wheel) · licence: MIT License · rank 6015 · last release 2026-03-11 · [PyPI](https://pypi.org/project/ddddocr/)

<details><summary>README extract</summary>

一个简单易用的通用验证码识别Python库

- 赞助合作商
- 项目介绍
- 环境支持
- 安装方法
- 功能概览
- 初始化参数详解
 - 参数详细说明
 - 功能组合与冲突
 - 模型选择指南
 - 性能优化参数
- 详细使用说明
 - 文字识别功能
 - 基础OCR识别
 - OCR概率输出
 - 自定义字符范围
 - 颜色过滤功能
 - 目标检测功能
 - 滑块验证码处理
 - 算法1：边缘匹配
 - 算法2：图像差异比较
 - 自定义模型导入
- 高级用法
 - 批量处理
 - 多线程优化
 - 验证码预处理 ...

Example:
```python
ddddocr.DdddOcr(
    ocr=True,           # 是否启用OCR功能
    det=False,          # 是否启用目标检测功能
    old=False,          # 是否使用旧版OCR模型
    beta=False,         # 是否使用Beta版OCR模型（新模型）
    use_gpu=False,      # 是否使用GPU加速
    device_id=0,        # 使用的GPU设备ID
    show_ad=True,       # 是否显示广告信息
    import_onnx_path="", # 自定义模型路径
...
```

Sections: DdddOcr - 通用验证码识别SDK, 目录, 赞助合作商, 项目介绍, 环境支持, 安装方法, 从PyPI安装（推荐）, 从源码安装, 安装 API 依赖（可选）, 功能概览, 初始化参数详解, 参数详细说明, 功能组合与冲突, 模型选择指南

</details>

### dnfile

Parse .NET executable files.

`pip install dnfile` · installs (wheel) · licence: MIT License · rank 6024 · last release 2026-01-31 · [PyPI](https://pypi.org/project/dnfile/) · [source](https://github.com/malwarefrank/dnfile)

<details><summary>README extract</summary>

Parse .NET executable files.

* Free software: MIT license

Features:
* Parse as much as we can, even if the file is partially malformed.
* Easy to use. Developed with IDE autocompletion in mind.

Example:
```python
import sys
import dnfile

filepath = sys.argv[1]

pe = dnfile.dnPE(filepath)
pe.print_info()
```

Sections: dnfile, Features, Quick Start, TODO, 0.18.0 (2026), 0.17.0 (2025), 0.16.0 (2025), 0.15.1 (2024), 0.15.0 (2024), 0.14.1 (2023), 0.14.0 (2023), 0.13.0 (2022), 0.12.0 (2022), 0.11.0 (2022)

</details>

### django-sendgrid-v5

An implementation of Django's EmailBackend compatible with sendgrid-python v5+

`pip install django-sendgrid-v5` · installs (wheel) · licence: MIT License · rank 6033 · last release 2026-01-05 · [PyPI](https://pypi.org/project/django-sendgrid-v5/)

<details><summary>README extract</summary>

This package implements an email backend for Django that relies on sendgrid's REST API for message delivery.

It is under active development, and pull requests are more than welcome\! ...

Example:
```python
from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```

Sections: django-sendgrid-v5, Other settings, Usage, Simple, Dynamic Template with JSON Data, Webhook Helpers, FAQ, Examples, Stargazers over time

</details>

### deno

Python redistribution of Deno binaries

`pip install deno` · installs (wheel) · licence: MIT · rank 6071 · last release 2026-10-21 · [PyPI](https://pypi.org/project/deno/) · [docs](https://docs.deno.com)

<details><summary>README extract</summary>

The easiest way to install and use Deno — the modern JavaScript and TypeScript runtime — in your Python projects.

Deno is a secure runtime for JavaScript and TypeScript that's built on V8, Rust, and Tokio. It features:

- 🔒 Secure by default - No file, network, or environment access unless explicitly enabled ...

Features:
- ✅ Easy integration - Install Deno alongside Python dependencies
- ✅ Version pinning - Lock Deno versions in `requirements.txt` or `pyproject.toml`
- ✅ No manual downloads - Automatic binary management ...

Example:
```python
import deno
import subprocess
import tempfile
import os

# Create a temporary TypeScript file
ts_code = """
console.log("Hello from Deno!");
const data = { message: "TypeScript works!" };
console.log(JSON.stringify(data));
"""

...

</details>

### databricks-openai

Support for Databricks AI support with OpenAI

`pip install databricks-openai` · installs (wheel) · licence: Apache-2.0 · rank 6087 · last release 2026-10-27 · [PyPI](https://pypi.org/project/databricks-openai/)

<details><summary>README extract</summary>

The `databricks-openai` package provides seamless integration of Databricks AI features into OpenAI applications.

Features:
- Vector Search: Store and query vector representations using `VectorSearchRetrieverTool`.
- Sandbox: Run an OpenAI Agents SDK agent's shell and filesystem tools inside a Databricks sandbox with `DatabricksSandboxClient` (install ...

Example:
```python
# Step 1: call model with VectorSearchRetrieverTool defined
dbvs_tool = VectorSearchRetrieverTool(index_name="catalog.schema.my_index_name")
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {
        "role": "user",
        "content": "Using the Databricks documentation, answer what is Spark?"
    }
]
...
```

...

</details>

### dsnparse

parse dsn urls

`pip install dsnparse` · installs (wheel) · licence: MIT · rank 6127 · last release 2025-10-13 · [PyPI](https://pypi.org/project/dsnparse/) · [source](https://github.com/Jaymon/dsnparse)

<details><summary>README extract</summary>

Parse dsn connection url strings. Responsible for parsing dsn strings in projects like prom and morp.

This is a generic version of dj-database-url.

So, now you can create dsns like this:

 scheme://user:pass@host:port/path?query=query_val#fragment

For example, let's look at a prom dsn: ...

Example:
```python
import dsnparse

dsn = "prom.interface.postgres.Interface://testuser:testpw@localhost:1234/testdb"
r = dsnparse.parse(dsn)

print(r.scheme) # prom.interface.postgres.Interface
print(r.username) # testuser
print(r.password) # testpw
print(r.host) # localhost
print(r.port) # 1234
print(r.hostloc) # localhost:1234
print(r.paths) # ['testdb']
```

Sections: dsnparse, Customizing

</details>

### dbt-metricflow

Execute commands against the MetricFlow semantic layer with dbt.

`pip install dbt-metricflow` · installs (wheel) · licence: Apache-2.0 · rank 6186 · last release 2026-09-10 · [PyPI](https://pypi.org/project/dbt-metricflow/) · [source](https://github.com/dbt-labs/metricflow/tree/main/dbt-metricflow)

<details><summary>README extract</summary>

This repo encapsulates the dbt-core, MetricFlow, and supported dbt-adapters packages. This package will manage the versioning between these packages such that they are compatible with each other.

- dbt-core and MetricFlow both depend on dbt-semantic-interfaces, which includes the schemas and interfaces for objects related to the semantic layer. ...

Sections: Welcome to dbt-metricflow, Repo use cases

</details>

### django-pgviews-redux

Create and manage Postgres SQL Views in Django

`pip install django-pgviews-redux` · installs (wheel) · licence: not stated · rank 6228 · last release 2026-10-21 · [PyPI](https://pypi.org/project/django-pgviews-redux/) · [source](https://github.com/xelixdev/django-pgviews-redux)

<details><summary>README extract</summary>

Adds first-class support for PostgreSQL Views in the Django ORM.
Fork of the original django-pgviews by mypebble with support for later Djangos, Pythons, and new features.

Example:
```python
from django.db import models

from django_pgviews import view as pg

class Customer(models.Model):
    name = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    is_preferred = models.BooleanField(default=False)

class PreferredCustomer(pg.View):
    name = models.CharField(max_length=100)
...
```

Sections: SQL Views for Postgres, Basic example, Usage, Define Fields, Define Projection, Migrations, Autodetector, Changing upstream fields, Features, Configuration, Updating Views, Dependencies, Materialized Views, Concurrent refresh

</details>

### detect_agent

Detect if code is running in an AI agent or automated development environment

`pip install detect_agent` · installs (wheel) · licence: not stated · rank 6245 · last release 2026-08-12 · [PyPI](https://pypi.org/project/detect_agent/) · [source](https://github.com/togethercomputer/detect_agent)

<details><summary>README extract</summary>

> This is a Python port of Vercel's `detect-agent` package.

A lightweight utility for detecting if code is being executed by an AI agent or automated development environment.

Example:
```python
from detect_agent import determine_agent

result = determine_agent()

if result["is_agent"]:
    agent = result["agent"]
    print(f"Running in {agent['name']} environment")
    # Adapt behavior for AI agent context
```

Sections: detect_agent, Usage, Agent Definitions, The AI_AGENT Standard, Recommended Naming Convention, Use Cases, Adaptive Behavior, Telemetry and Analytics, Feature Toggles, Links

</details>

### databricks-pypi-extras

(no summary)

`pip install databricks-pypi-extras` · installs (wheel) · licence: not stated · rank 6267 · last release 2019-02-14 · [PyPI](https://pypi.org/project/databricks-pypi-extras/)

### diskcache-stubs

diskcache stubs

`pip install diskcache-stubs` · installs (wheel) · licence: Apache Software License · rank 6311 · last release 2024-08-18 · [PyPI](https://pypi.org/project/diskcache-stubs/) · [source](https://github.com/phi-friday/diskcache-stubs)

<details><summary>README extract</summary>

Warning: This library provides type hints only.
If you need the runtime package,
you can find it `python-diskcache`.

Sections: diskcache-stubs, TODO

</details>

### deepseek-harness-runtime-bin

Bundled dsh CLI runtime for the DeepSeek Harness Python SDK

`pip install deepseek-harness-runtime-bin` · installs (wheel) · licence: MIT · rank 6338 · last release 2026-10-17 · [PyPI](https://pypi.org/project/deepseek-harness-runtime-bin/) · [docs](https://github.com/deepseek-ai/deepseek-harness/blob/master/python/sdk-runtime/README.md) · [source](https://github.com/deepseek-ai/deepseek-harness)

<details><summary>README extract</summary>

English | 中文

Platform runtime wheel for the DeepSeek Harness Python SDK. It packages the normal `dsh` CLI and its closed Node dependency tree into a native executable, so SDK use requires no system Node.js. This package publishes wheels only.

Sections: deepseek-harness-runtime-bin, Python module API, Packaged profile resolution, Build and distribution

</details>

### docx2python

Extract content from docx files

`pip install docx2python` · installs (wheel) · licence: MIT · rank 6339 · last release 2026-10-28 · [PyPI](https://pypi.org/project/docx2python/)

<details><summary>README extract</summary>

* Better type hints for DocxOutput properties. You should never get an "or" or "Any" type hint for the nested lists returned by Docx2Python.
* Support for "strict" namespaces. Word uses a superset of the standard Open Office XML format. Work can restrict itself to the standard by saving with the "strict" namespace. This is now supported. ...

Example:
```python
from docx2python import docx2python

# extract docx content
with docx2python('path/to/file.docx') as docx_content:
    print(docx_content.text)

docx_content = docx2python('path/to/file.docx')
print(docx_content.text)
docx_content.close()

# extract docx content, write images to image_directory
...
```

...

</details>

### dspy-ai

DSPy

`pip install dspy-ai` · installs (wheel) · licence: MIT License · rank 6355 · last release 2026-10-12 · [PyPI](https://pypi.org/project/dspy-ai/)

<details><summary>README extract</summary>

`dspy-ai` is a compatibility alias for the dspy package. Install `dspy` instead: `pip install dspy`.

</details>

### django-hosts

Dynamic and static host resolving for Django. Maps hostnames to URLconfs.

`pip install django-hosts` · installs (wheel) · licence: BSD License · rank 6370 · last release 2025-06-19 · [PyPI](https://pypi.org/project/django-hosts/) · [source](https://github.com/jazzband/django-hosts)

<details><summary>README extract</summary>

This Django app routes requests for specific hosts to different URL schemes
defined in modules called "hostconfs".

For example, if you own `example.com` but want to serve specific content
at `api.example.com` and `beta.example.com`, add the following to a
`hosts.py` file: ...

Example:
```python
from django_hosts import patterns, host

host_patterns = patterns('path.to',
    host(r'api', 'api.urls', name='api'),
    host(r'beta', 'beta.urls', name='beta'),
)
```

Sections: django-hosts, . Set the `ROOT_HOSTCONF` setting to the dotted Python

</details>

### django-cotton

Enabling Modern UI Composition in Django.

`pip install django-cotton` · installs (wheel) · licence: MIT License · rank 6373 · last release 2026-10-14 · [PyPI](https://pypi.org/project/django-cotton/)

<details><summary>README extract</summary>

Bringing component-based design to Django templates.

- Docs site + demos: django-cotton.com
- Discord community (new)

Features:
Cotton aims to overcome certain limitations that exist in the django template system that hold us back when we want to apply modern practices to compose UIs in a modular and reusable way.

Example:
```python
# views.py
from django.http import HttpResponse
from django_cotton import render_component

def user_deleted(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponse(
        render_component(request, "notification",
            message=f"{user.name} deleted",
            type="success"
        )
    )
```

...

</details>

### daiquiri

Library to configure Python logging easily

`pip install daiquiri` · installs (wheel) · licence: Apache Software License · rank 6416 · last release 2025-09-04 · [PyPI](https://pypi.org/project/daiquiri/)

<details><summary>README extract</summary>

The daiquiri library provides an easy way to configure logging. It also
provides some custom formatters and handlers.

You can read the whole documentation at

* Free software: Apache license

</details>

### django-sslserver

An SSL-enabled development server for Django

`pip install django-sslserver` · installs (wheel) · licence: MIT License · rank 6457 · last release 2019-12-10 · [PyPI](https://pypi.org/project/django-sslserver/)

### dagster-dlt

Package for performing ETL/ELT tasks with dlt in Dagster.

`pip install dagster-dlt` · installs (wheel) · licence: Apache-2.0 · rank 6505 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-dlt/)

### dm-control

Continuous control environments and MuJoCo Python bindings.

`pip install dm-control` · installs (wheel) · licence: Apache-2.0 · rank 6519 · last release 2026-11-06 · [PyPI](https://pypi.org/project/dm-control/)

<details><summary>README extract</summary>

DeepMind's software stack for physics-based simulation and Reinforcement
Learning environments, using MuJoCo physics.

An introductory tutorial for this package is available as a Colaboratory
notebook: Open In Google Colab.

</details>

### dbtlabs-vortex

Python client for Vortex

`pip install dbtlabs-vortex` · installs (wheel) · licence: not stated · rank 6533 · last release 2026-06-18 · [PyPI](https://pypi.org/project/dbtlabs-vortex/)

<details><summary>README extract</summary>

A Python client for sending data to the Vortex.

Features:
This client provides an easy way to send properly formatted messages to Kafka topics that will be consumed by the Vortex service and written to Iceberg tables.

The client:
- Accepts arbitrary protobufs onto a buffer via `log_proto` ...

Example:
```python
from dbtlabs_vortex.producer import log_proto, shutdown

# Send JSON data
log_proto(... proto ...)

# Wait for all messages to be delivered
shutdown(timeout_seconds=0.500)
```

Sections: Vortex Python Client, Overview, Prerequisites, Setup, Quick Start, Examples, Error Handling

</details>

### dask-image

Distributed image processing

`pip install dask-image` · installs (wheel) · licence: BSD License · rank 6560 · last release 2026-05-27 · [PyPI](https://pypi.org/project/dask-image/) · [source](https://github.com/dask/dask-image)

<details><summary>README extract</summary>

Distributed image processing

* Free software: BSD 3-Clause

</details>

### databricks-zerobus-ingest-sdk

Databricks Zerobus Ingest SDK for Python

`pip install databricks-zerobus-ingest-sdk` · installs (wheel) · licence: not stated · rank 6581 · last release 2026-11-02 · [PyPI](https://pypi.org/project/databricks-zerobus-ingest-sdk/)

<details><summary>README extract</summary>

A high-performance Python client for streaming data ingestion into Databricks Delta tables using the Zerobus service.

Features:
The Zerobus Python SDK is a thin wrapper around the Zerobus Rust SDK, built using PyO3 bindings. It delivers native performance with a Python-friendly API supporting both synchronous and asynchronous usage. ...

Example:
```python
from zerobus.sdk.sync import ZerobusSdk
from zerobus.sdk.shared import TableProperties

server_endpoint = "
workspace_url = "

sdk = ZerobusSdk(server_endpoint, workspace_url)
table_properties = TableProperties("main.default.air_quality")
stream = sdk.create_stream(client_id, client_secret, table_properties)

try:
    for i in range(100):
...
```

...

</details>

### developer-disk-image

Download DeveloperDiskImage ans Personalized images from GitHub

`pip install developer-disk-image` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6608 · last release 2026-08-07 · [PyPI](https://pypi.org/project/developer-disk-image/)

_README extract left out: share-alike licence._

### dagster-azure

Package for Azure-specific Dagster framework op and resource components.

`pip install dagster-azure` · installs (wheel) · licence: Apache-2.0 · rank 6618 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-azure/)

### djoser

REST implementation of Django authentication system.

`pip install djoser` · installs (wheel) · licence: MIT License · rank 6643 · last release 2026-10-12 · [PyPI](https://pypi.org/project/djoser/) · [docs](https://djoser.readthedocs.io/) · [source](https://github.com/sunscrapers/djoser)

<details><summary>README extract</summary>

REST implementation of Django authentication
system. djoser library provides a set of Django Rest Framework
views to handle basic actions such as registration, login, logout, password
reset and account activation. It works with
custom user model.

Supported features include:

- Token-based authentication
- JWT authentication ...

Sections: djoser, Requirements, Documentation, Without uv, Example project, Commiting your code, Similar projects

</details>

### djhtml

Django/Jinja template indenter

`pip install djhtml` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6650 · last release 2026-03-26 · [PyPI](https://pypi.org/project/djhtml/)

_README extract left out: share-alike licence._

### durabletask

A Durable Task Client SDK for Python

`pip install durabletask` · installs (wheel) · licence: MIT License · rank 6679 · last release 2026-11-02 · [PyPI](https://pypi.org/project/durabletask/) · [source](https://github.com/microsoft/durabletask-python)

<details><summary>README extract</summary>

This repository contains Python SDKs for building durable orchestrations with
Azure Durable Task Scheduler
and Azure Durable Functions:

- `durabletask` is the core orchestration SDK.
- `durabletask.azuremanaged` is the Azure Durable
 Task Scheduler provider. ...

Example:
```python
from durabletask.client import OrchestrationQuery

query = OrchestrationQuery(task_hub_names=["orders", "billing"])
```

Sections: Durable Task SDK for Python, Python Requirements, References, Optional Features, Task Hub Query Filters, Set Serialization, Entity IDs, Large Payload Externalization, Failure Details Properties, Trademarks

</details>

### dask-labextension

A JupyterLab extension for Dask.

`pip install dask-labextension` · installs (wheel) · licence: BSD License · rank 6740 · last release 2023-08-04 · [PyPI](https://pypi.org/project/dask-labextension/) · [source](https://github.com/dask/dask-labextension)

<details><summary>README extract</summary>

This package provides a JupyterLab extension to manage Dask clusters,
as well as embed Dask's dashboard plots directly into JupyterLab panes.

JupyterLab >= 1.0
distributed >= 1.24.1

Sections: Dask JupyterLab Extension, Explanatory Video (5 minutes), Requirements, JupyterLab 4.x, JupyterLab 3.x, JupyterLab 2.x, Configuration of Dask cluster management, Configuring a default layout, Publishing, Handling Javascript package version conflicts

</details>

### dtschema

DeviceTree validation schema and tools

`pip install dtschema` · installs (wheel) · licence: BSD License · rank 6767 · last release 2026-09-18 · [PyPI](https://pypi.org/project/dtschema/) · [source](https://github.com/devicetree-org/dt-schema)

<details><summary>README extract</summary>

The dtschema module contains tools and schema data for Devicetree
schema validation using the
json-schema vocabulary.
The tools validate Devicetree files using DT binding schema files. The
tools also validate the DT binding schema files. Schema files are
written in a JSON compatible subset of YAML to be both human and machine
readable. ...

Sections: Devicetree Schema Tools, Data Model, Devicetree Schemas, Devicetree Meta-Schemas, Usage, Dependencies

</details>

### dtlpymetrics

Scoring and metrics app

`pip install dtlpymetrics` · installs (wheel) · licence: not stated · rank 6773 · last release 2026-02-26 · [PyPI](https://pypi.org/project/dtlpymetrics/)

<details><summary>README extract</summary>

This app improves the efficiency of annotating data by improving annotation quality while reducing the time required to
produce them.

The components of this app are:

1. Functions to calculate scores for quality tasks and model predictions.
2. ...

Sections: Scoring and metrics app, Description, Quality Flows, Score Types, 1) Raw annotation scores, 2) Annotation overall, 3) User confusion score, 4) Label confusion score, 5) Item overall score, Confusion Example, Functions

</details>

### durabletask.azuremanaged

Durable Task Python SDK provider implementation for the Azure Durable Task Scheduler

`pip install durabletask.azuremanaged` · installs (wheel) · licence: MIT License · rank 6779 · last release 2026-11-02 · [PyPI](https://pypi.org/project/durabletask.azuremanaged/) · [source](https://github.com/microsoft/durabletask-python)

### dataproc-spark-connect

Dataproc client library for Spark Connect

`pip install dataproc-spark-connect` · installs (wheel) · licence: Apache 2.0 · rank 6807 · last release 2026-04-07 · [PyPI](https://pypi.org/project/dataproc-spark-connect/)

<details><summary>README extract</summary>

A wrapper of the Apache Spark Connect
client with additional functionalities that allow applications to communicate
with a remote Dataproc Spark Session using the Spark Connect protocol without
requiring additional steps.

Example:
```python
from google.cloud.dataproc_spark_connect import DataprocSparkSession
spark = DataprocSparkSession.builder.getOrCreate()
```

Sections: Dataproc Spark Connect Client, Setup, Usage, Builder Configuration, Reusing Named Sessions Across Notebooks, Using Spark SQL Magic Commands (Jupyter Notebooks), Code reviews

</details>

### django-sesame

Frictionless authentication with "Magic Links" for your Django project.

`pip install django-sesame` · installs (wheel) · licence: BSD License · rank 6850 · last release 2026-10-02 · [PyPI](https://pypi.org/project/django-sesame/) · [docs](https://django-sesame.readthedocs.io/) · [source](https://github.com/aaugustin/django-sesame)

<details><summary>README extract</summary>

django-sesame provides frictionless authentication with "Magic Links" for
your Django project.

It generates URLs containing authentication tokens such as:

Then it authenticates users based on tokens found in URLs.

More broadly, it supports a wide range of use cases for
stateless, token-based authentication. ...

Example:
```python
from django.urls import path
from sesame.views import LoginView

urlpatterns = [
    ...,
    path("sesame/login/", LoginView.as_view(), name="sesame-login"),
    ...,
]
```

Sections: Requirements, Getting started, Quick example, Use cases

</details>

### dash-mantine-components

Plotly Dash Components based on Mantine

`pip install dash-mantine-components` · installs (wheel) · licence: MIT · rank 6852 · last release 2026-10-30 · [PyPI](https://pypi.org/project/dash-mantine-components/)

<details><summary>README extract</summary>

Dash Mantine Components is an extensive (90+) Dash components library based on Mantine React Components Library. It makes it easier to create good quality dashboards with very well designed components out of the box.

Example:
```python
import dash
from dash import Dash, Input, Output, callback, html, no_update

import dash_mantine_components as dmc

app = Dash()

app.layout = dmc.MantineProvider(
    [
        dmc.DatePickerInput(
            id="date-picker",
            label="Start Date",
            description="You can also provide a description",
...
```

Sections: Quickstart, 📚 Documentation

</details>

### dropbox-sign

Dropbox Sign API

`pip install dropbox-sign` · installs (wheel) · licence: MIT · rank 6867 · last release 2026-10-21 · [PyPI](https://pypi.org/project/dropbox-sign/) · [source](https://github.com/hellosign/dropbox-sign-python)

<details><summary>README extract</summary>

Dropbox Sign v3 API

Version 2.0.0 is generated with OpenAPI Generator 7.26.0. Existing code keeps working, with these changes:

- Python 3.10 or later is required. Python 3.8 and 3.9 are no longer supported; pip keeps installing 1.x on those versions.
- Dependencies: `urllib3 >= 2.8.0` and `pydantic >= 2.11`. ...

Example:
```python
import json
from datetime import date, datetime
from pprint import pprint

from dropbox_sign import ApiClient, ApiException, Configuration, api, models

configuration = Configuration(
    username="YOUR_API_KEY",
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
...
```

...

</details>

### drjax

DrJAX - Scalable and Differentiable MapReduce Primitives in JAX.

`pip install drjax` · installs (wheel) · licence: Apache Software License · rank 6880 · last release 2026-08-31 · [PyPI](https://pypi.org/project/drjax/) · [source](https://github.com/google/drjax)

<details><summary>README extract</summary>

DrJAX is a library designed to embed a MapReduce programming model into JAX. DrJAX has
multiple objectives.

1. Create a simple JAX-based authoring surface for MapReduce computations.
1. Leverage JAX's sharding mechanisms to enable highly optimized execution of
 MapReduce computations, especially in large-scale datacenter settings.
1. ...

Sections: DrJAX - Differentiable MapReduce Primitives in JAX, System design, Disclaimers

</details>

### delayed-assert

Delayed/soft assertions for python

`pip install delayed-assert` · installs (wheel) · licence: not stated · rank 6893 · last release 2025-12-07 · [PyPI](https://pypi.org/project/delayed-assert/)

<details><summary>README extract</summary>

Delayed aka. Soft asserts for python

Few features:

 - No Dependenices on any other framework/library.
 - Should work with any testing framework.
 - Can be use as decorator or context manager.

Example:
```python
expect(lambda: self.assertListEqual([4,5,6,2,5],[7,8]))
```

Sections: Python-Delayed-Assert, Uses, Using assertion library with lambda, Current possible uses, Color Output Control, Disable Colors via Environment Variable, Disable Colors Programmatically, Caller Stack Verification

</details>

### django-better-admin-arrayfield

Better ArrayField widget for admin

`pip install django-better-admin-arrayfield` · installs (wheel) · licence: BSD License · rank 6908 · last release 2020-12-08 · [PyPI](https://pypi.org/project/django-better-admin-arrayfield/)

<details><summary>README extract</summary>

Better ArrayField widget for admin

Supported Python versions:

Supported Django versions: 2.0, 2.1, 2.2, 3.0, 3.1

might work with different django/python versions as well but I did not test that.

It changes comma separated widget to list based in admin panel.

Before:

After:

Example:
```python
from django_better_admin_arrayfield.models.fields import ArrayField
```

Sections: Django better admin ArrayField, Quickstart, Usage, Custom subwidget, Running Tests, Pre-commit hooks, 1.4.2 (2020-12-08), 1.4.1 (2020-12-08), 1.4.0 (2020-10-04), 1.3.0 (2020-07-09), 1.2.1 (2020-07-09), 1.2.0 (2020-07-09), 1.1.0 (2020-04-28), 1.0.7 (2020-04-27)

</details>

### django-mcp-server

Django MCP Server is a Django extensions to easily enable AI Agents to interact with Django Apps through the Model Context Protocol it works equally well on WSGI and ASGI

`pip install django-mcp-server` · installs (wheel) · licence: MIT License · rank 6917 · last release 2025-10-10 · [PyPI](https://pypi.org/project/django-mcp-server/)

<details><summary>README extract</summary>

Django MCP Server is an implementation of the Model Context Protocol (MCP) extension for Django. This module allows MCP Clients and AI agents to interact with any Django application seamlessly.

🚀 Django-Style declarative style tools to allow AI Agents and MCP clients tool to interact with Django. ...

Features:
- Expose Django models and logic as MCP tools.
- Serve an MCP endpoint inside your Django app.
- Easily integrate with AI agents, MCP Clients, or tools like Google ADK.

Example:
```python
from django.urls import path, include

urlpatterns = [
    # your urls...
    path("", include('mcp_server.urls')),
]
```

...

</details>

### django-hashid-field

A Hashids obfuscated Django Model Field

`pip install django-hashid-field` · installs (wheel) · licence: MIT License · rank 6923 · last release 2024-05-03 · [PyPI](https://pypi.org/project/django-hashid-field/)

<details><summary>README extract</summary>

This library has been retired. It is no longer recommended for new projects. Existing projects do not require
changes, but should consider migrating to a different library. See the
RETIRED
document for more information.

A custom Model Field that uses the Hashids library
to obfuscate an IntegerField or AutoField. ...

Features:
* Stores IDs as integers in the database
* Allows lookups and filtering by hashid string or Hashid object and (optionally) integer. ...

Example:
```python
>>> b = Book()
>>> b.reference_id = 123
>>> b.reference_id
Hashid(123): OwLxW8D
```

...

</details>

### django-elasticsearch-dsl

Wrapper around elasticsearch-dsl-py for django models

`pip install django-elasticsearch-dsl` · installs (wheel) · licence: BSD License · rank 6927 · last release 2025-07-23 · [PyPI](https://pypi.org/project/django-elasticsearch-dsl/)

<details><summary>README extract</summary>

Django Elasticsearch DSL is a package that allows indexing of django models in elasticsearch.
It is built as a thin wrapper around elasticsearch-py
so you can use all the features developed by the elasticsearch-py team.

You can view the full documentation at

Features:
- Based on elasticsearch-py so you can make queries with the Search class.
- Django signal receivers on save and delete for keeping Elasticsearch in sync.
- Management commands for creating, deleting, rebuilding and populating indices. ...

Sections: Django Elasticsearch DSL, Features, 7.1.4 (2020-07-05), 7.1.1 (2019-12-26), 7.1.0 (2019-10-29), 7.0.0 (2019-08-11), 6.4.2 (2019-07-26), 6.4.1 (2019-06-14), 6.4.0 (2019-06-01), 0.5.1 (2018-11-07), 0.5.0 (2018-04-22), Breaking Change, 0.4.5 (2018-04-22), 0.4.4 (2017-12-13)

</details>

### django-sequences

Generate gapless sequences of integer values.

`pip install django-sequences` · installs (wheel) · licence: BSD License · rank 6939 · last release 2026-10-02 · [PyPI](https://pypi.org/project/django-sequences/) · [source](https://github.com/aaugustin/django-sequences)

<details><summary>README extract</summary>

By default, Django gives each model an auto-incrementing integer primary key.
These primary keys look like they generate a continuous sequence of integers.

However, this behavior isn't guaranteed. ...

Example:
```python
from django.db import transaction
from sequences import get_next_value
from invoices.models import Invoice

with transaction.atomic():
    Invoice.objects.create(number=get_next_value("invoice_numbers"))
```

Sections: django-sequences, Getting started, API, `get_next_value`, `get_next_values`, `get_last_value`, `delete`, `Sequence`, Examples, Per-date sequences, Multiple databases, Isolation levels, Releasing, Running test databases

</details>

### datadog-logger

Python logging handler for DataDog events

`pip install datadog-logger` · installs (wheel) · licence: MIT · rank 6960 · last release 2026-07-27 · [PyPI](https://pypi.org/project/datadog-logger/)

<details><summary>README extract</summary>

Note: This library does not send logs to Datadog's Log Management product. See
Datadog's documentation for how to configure log collection. See

A Python `logging.Handler` for sending log messages to DataDog as Events in
the Events Explorer.

Example:
```python
import datadog
from datadog_logger import log_error_events
import logging

# Authenticate with DataDog
datadog.initialize(api_key="api-key", app_key="app-key")

# Note, a normal STDOUT handler will not be configured if this is not
# called first
logging.basicConfig()

...
```

Sections: DataDog Logger, Usage, Details

</details>

### dumb-init

Simple wrapper script which proxies signals to a child

`pip install dumb-init` · installs (wheel) · licence: not stated · rank 7011 · last release 2022-04-26 · [PyPI](https://pypi.org/project/dumb-init/)

### dash-extensions

Extensions for Plotly Dash.

`pip install dash-extensions` · installs (wheel) · licence: MIT · rank 7017 · last release 2026-07-16 · [PyPI](https://pypi.org/project/dash-extensions/) · [source](https://github.com/emilhe/dash-extensions)

<details><summary>README extract</summary>

The `dash-extensions` package is a collection of utility functions, syntax extensions, and Dash components that aim to improve the Dash development experience. Here is a brief overview,

- The `enrich` module, which contains various enriched versions of Dash components
- A number of custom components, e.g. ...

</details>

### django-grappelli

A jazzy skin for the Django Admin-Interface.

`pip install django-grappelli` · installs (wheel) · licence: BSD License · rank 7102 · last release 2026-10-16 · [PyPI](https://pypi.org/project/django-grappelli/) · [source](https://github.com/sehmaschine/django-grappelli)

<details><summary>README extract</summary>

A jazzy skin for the Django admin interface.

Grappelli is a grid-based alternative/extension to the Django administration interface.

Sections: Django Grappelli, Code, Website, Documentation, Compatibility

</details>

### django-template-partials

Reusable named inline-partials for the Django Template Language

`pip install django-template-partials` · installs (wheel) · licence: MIT License · rank 7110 · last release 2025-11-14 · [PyPI](https://pypi.org/project/django-template-partials/) · [docs](https://github.com/carltongibson/django-template-partials?tab=readme-ov-file#basic-usage) · [source](https://github.com/carltongibson/django-template-partials/)

<details><summary>README extract</summary>

Reusable named inline partials for the Django Template Language.

Template Partials were added to Django in version 6.0. You should use that in new projects:

Check out the Migration Guide if you're updating to the Django version.

I introduced `django-template-partials` in my DjangoCon Europe 2023 talk in Edinburgh. ...

Example:
```python
from template_partials.apps import wrap_loaders

TEMPLATES = [
    ...,
    {
        "BACKEND": "...",
        "NAME": "myname",
        "OPTIONS": {
           ...,
        },
    },
    ...,
]

wrap_loaders("myname")
```

...

</details>

### dagster-datadog

Package for datadog Dagster framework components.

`pip install dagster-datadog` · installs (wheel) · licence: Apache-2.0 · rank 7159 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-datadog/)

### dagit

Web UI for dagster.

`pip install dagit` · installs (wheel) · licence: Apache-2.0 · rank 7179 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagit/)

### django-zen-queries

Explicit control over query execution in Django applications.

`pip install django-zen-queries` · installs (wheel) · licence: BSD · rank 7269 · last release 2021-07-27 · [PyPI](https://pypi.org/project/django-zen-queries/)

<details><summary>README extract</summary>

Gives you control over which parts of your code are allowed to run queries, and which aren't.

Tested against Django 2.2 - 3.1 on Python 3.6 - 3.9.

> Explicit is better than implicit

(The Zen Of Python)

The greatest strength of Django's ORM is also its greatest weakness. ...

Example:
```python
class Topping(models.Model):
    name = models.CharField(max_length=100)

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    toppings = models.ManyToManyField(Topping)
```

Sections: django-zen-queries, Motivation, Example, Instructions, Decorator, Extra tools, Render shortcut, TemplateResponse subclass, Django REST framework Serializer and View mixins, Escape hatch, Template Tags, Permissions gotcha, How does it work?

</details>

### docker-compose

Multi-container orchestration for Docker

`pip install docker-compose` · installs (wheel) · licence: Apache Software License · rank 7293 · last release 2021-05-10 · [PyPI](https://pypi.org/project/docker-compose/) · [docs](https://docs.docker.com/compose/overview) · [source](https://github.com/docker/compose)

<details><summary>README extract</summary>

Docker Compose is a tool for running multi-container applications on Docker
defined using the Compose file format.
A Compose file is used to define how the one or more containers that make up
your application are configured.
Once you have a Compose file, you can create and start your application with a
single command: `docker-compose up`. ...

Sections: Docker Compose, Windows and macOS, Linux, Using pip

</details>

### django-google-sso

Easily add Google Authentication to your Django Projects

`pip install django-google-sso` · installs (wheel) · licence: MIT · rank 7313 · last release 2026-06-17 · [PyPI](https://pypi.org/project/django-google-sso/) · [docs](https://megalus.github.io/django-google-sso/) · [source](https://github.com/megalus/django-google-sso)

<details><summary>README extract</summary>

Easily integrate Google Authentication into your Django projects

This library simplifies the process of authenticating users with Google in Django projects. It adds a customizable "Login with Google" button to your Django Admin login page with minimal configuration.

Features:
- Simplicity: Adds Google authentication with minimal setup and no template modifications
- Admin Integration: Seamlessly integrates with the Django Admin interface ...

Example:
```python
# urls.py

from django.urls import include, path

urlpatterns = [
    # other urlpatterns...
    path(
        "google_sso/", include("django_google_sso.urls", namespace="django_google_sso")
    ),
]
```

Sections: Welcome to Django Google SSO, Why use Django Google SSO?, Quick Start, Configuration, Example project, Documentation

</details>

### drf-orjson-renderer

Django RestFramework JSON Renderer Backed by orjson

`pip install drf-orjson-renderer` · installs (wheel) · licence: MIT License · rank 7322 · last release 2025-12-17 · [PyPI](https://pypi.org/project/drf-orjson-renderer/) · [source](https://github.com/brianjbuck/drf_orjson_renderer)

<details><summary>README extract</summary>

`drf_orjson_renderer` is JSON renderer and parser for Django Rest Framework
using the orjson library. Backed by
Rust, orjson is safe, correct and _fast_. ⚡️

In addition, unlike some performance optimized DRF renderers, It also renders
pretty printed JSON when requests are made via RestFramework's BrowsableAPI.

You get:
- The safety of Rust ...

Example:
```python
from rest_framework.views import APIView
from rest_framework.response import Response

class MyView(APIView):
    def default(self, obj):
        if isinstance(obj, MyComplexData):
            return dict(obj)

    def get_renderer_context(self):
        renderer_context = super().get_renderer_context()
...
```

Sections: Django Rest Framework ORJSON Renderer, Passing Your Own `default` Function, Numpy, Benchmarks

</details>

### dynamic-yaml

Enables self referential yaml entries

`pip install dynamic-yaml` · installs (wheel) · licence: MIT License · rank 7328 · last release 2024-04-09 · [PyPI](https://pypi.org/project/dynamic-yaml/)

<details><summary>README extract</summary>

Dynamic YAML is a couple of classes and functions that add extra functionality to YAML that turns it into a great configuration language for Python. If you prefer JSON, then see dynamic-json.

YAML already provides: ...

Example:
```python
import dynamic_yaml

with open('/path/to/file.yaml') as fileobj:
    cfg = dynamic_yaml.load(fileobj)
    assert cfg.dirs.venv == '/home/user/venvs/hello-world'
    assert cfg.dirs.output == '/home/user/venvs/hello-world/data/output-a-b'
```

</details>

### deskew

Skew detection and correction in images containing text

`pip install deskew` · installs (wheel) · licence: MIT · rank 7411 · last release 2026-06-03 · [PyPI](https://pypi.org/project/deskew/) · [source](https://github.com/sbrunner/deskew)

<details><summary>README extract</summary>

Note: Skew is measured in degrees. Deskewing is a process whereby skew is removed by rotating an image by the same amount as its skew but in the opposite direction. This results in a horizontally and vertically aligned image where the text runs across the page rather than at an angle. ...

Example:
```python
import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import rotate

from deskew import determine_skew

image = io.imread('input.png')
grayscale = rgb2gray(image)
angle = determine_skew(grayscale)
rotated = rotate(image, angle, resize=True) * 255
io.imsave('output.png', rotated.astype(np.uint8))
```

Sections: Deskew, Skew detection and correction in images containing text, Cli usage, Lib usage, Debug images

</details>

### drf-flex-fields

Flexible, dynamic fields and nested resources for Django REST Framework serializers.

`pip install drf-flex-fields` · installs from source (sdist only) · licence: MIT License · rank 7430 · last release 2023-03-11 · [PyPI](https://pypi.org/project/drf-flex-fields/)

<details><summary>README extract</summary>

Flexible, dynamic fields and nested models for Django REST Framework serializers.

Features:
FlexFields (DRF-FF) for Django REST Framework is a package designed to provide a common baseline of functionality for dynamically setting fields and nested models within DRF serializers. ...

Example:
```python
from rest_flex_fields import FlexFieldsModelSerializer

class StateSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'name')

class CountrySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'population', 'states')
...
```

...

</details>

### django-sortedm2m

Drop-in replacement for Django's many to many field with sorted relations.

`pip install django-sortedm2m` · installs (wheel) · licence: BSD License · rank 7459 · last release 2026-11-07 · [PyPI](https://pypi.org/project/django-sortedm2m/)

<details><summary>README extract</summary>

`sortedm2m` is a drop-in replacement for django's own `ManyToManyField`.
The provided `SortedManyToManyField` behaves like the original one but
remembers the order of added relations.

Imagine that you have a gallery model and a photo model. ...

Example:
```python
from django.db import models
from sortedm2m.fields import SortedManyToManyField

class Photo(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='...')

class Gallery(models.Model):
    name = models.CharField(max_length=50)
    photos = SortedManyToManyField(Photo)
```

Sections: django-sortedm2m, Use Cases, Requirements, Usage, `SortedManyToManyField`, `sorted`, `sort_value_field_name`, `base_class`, Admin, Running the tests, Code Quality, 4.1.0, 4.0.0, 3.1.1

</details>

### django-cache-url

Use Cache URLs in your Django application.

`pip install django-cache-url` · installs (wheel) · licence: MIT License · rank 7520 · last release 2026-01-24 · [PyPI](https://pypi.org/project/django-cache-url/)

<details><summary>README extract</summary>

django-cache-url
~~~~~~~~~~~~~~~~

This simple Django utility allows you to utilize the
`12factor < inspired
``CACHE_URL`` environment variable to configure your Django application.

Usage

Configure your cache in ``settings.py``::

 CACHES={'default': django_cache_url.config()}

Nice and simple.

</details>

### databricks-feature-store

Databricks Feature Store Client

`pip install databricks-feature-store` · installs (wheel) · licence: Databricks Proprietary License · rank 7537 · last release 2024-01-09 · [PyPI](https://pypi.org/project/databricks-feature-store/)

<details><summary>README extract</summary>

Starting with v0.17.0, the `databricks-feature-store` package is *deprecated*. Use `databricks-feature-engineering`
 instead.

- Use `pip install databricks-feature-engineering` to replace `pip install databricks-feature-store`. ...

</details>

### django-contrib-comments

The code formerly known as django.contrib.comments.

`pip install django-contrib-comments` · installs (wheel) · licence: BSD License · rank 7554 · last release 2022-01-31 · [PyPI](https://pypi.org/project/django-contrib-comments/)

<details><summary>README extract</summary>

Django used to include a comments framework; since Django 1.6 it's been
separated to a separate project. This is that project.

This framework can be used to attach comments to any model, so you can use it
for comments on blog entries, photos, book chapters, or anything else.

For details, consult the documentation.


Sections: Django "excontrib" Comments, 2.2.0 (2022-01-31), 2.1.0 (2021-03-03), 2.0.0 (2020-12-20), 1.9.2 (2019-12-03), 1.9.1 (2019-02-20), 1.9.0 (2018-08-04), 1.8.0 (2017-02-03), 1.7.3 (2016-09-13), 1.7.2 (2016-08-04), 1.7.1 (2016-05-03), 1.7.0 (2016-03-29), 1.6.2 (2016-12-10), 1.6.1 (2016-05-08)

</details>

### django-dramatiq

A Django app for Dramatiq.

`pip install django-dramatiq` · installs (wheel) · licence: not stated · rank 7591 · last release 2025-11-13 · [PyPI](https://pypi.org/project/django-dramatiq/)

### django-filter-stubs

PEP-484 stubs for django-filter

`pip install django-filter-stubs` · installs (wheel) · licence: MIT License · rank 7645 · last release 2023-03-28 · [PyPI](https://pypi.org/project/django-filter-stubs/)

<details><summary>README extract</summary>

This package contains type subs to provide more precise static types for Django Filters.

</details>

### deepseek-harness-sdk

Python SDK for DeepSeek Harness

`pip install deepseek-harness-sdk` · installs (wheel) · licence: MIT · rank 7710 · last release 2026-10-17 · [PyPI](https://pypi.org/project/deepseek-harness-sdk/) · [docs](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/python-sdk.md) · [source](https://github.com/deepseek-ai/deepseek-harness)

<details><summary>README extract</summary>

English | 中文

Python subprocess SDK for driving DeepSeek Harness over newline-delimited JSON-RPC on stdio. Install `deepseek-harness-sdk`; it installs the exact same-version `deepseek-harness-runtime-bin` wheel for the current platform. ...

Example:
```python
from deepseek_harness_runtime import download_office
from deepseek_harness.office import convert, recalculate, render_images

download_office()
pdf = convert("report.docx", "report.pdf")
workbook = recalculate("forecast.xlsx", "calculated.xlsx")
preview = render_images("report.docx", "report-preview", pages=[1])
```

Sections: DeepSeek Harness Python SDK, Optional Office operations, Start a runtime, Customize plugins, Results and notifications

</details>

### duo-client

Reference client for Duo Security APIs

`pip install duo-client` · installs (wheel) · licence: BSD License · rank 7741 · last release 2026-08-20 · [PyPI](https://pypi.org/project/duo-client/)

<details><summary>README extract</summary>

Features:
Auth -

Admin -

Accounts -

Activity - The activity endpoint is in public preview and subject to change

Sections: Overview, Tested Against Python Versions, Requirements, Using, Linting

</details>

### dataframely

A declarative, polars-native data frame validation library

`pip install dataframely` · installs (wheel) · licence: not stated · rank 7763 · last release 2026-09-20 · [PyPI](https://pypi.org/project/dataframely/) · [docs](https://dataframely.readthedocs.io/) · [source](https://github.com/quantco/dataframely)

<details><summary>README extract</summary>

Example:
```python
import dataframely as dy
import polars as pl

class HouseSchema(dy.Schema):
    zip_code = dy.String(nullable=False, min_length=3)
    num_bedrooms = dy.UInt8(nullable=False)
    num_bathrooms = dy.UInt8(nullable=False)
    price = dy.Float64(nullable=False)

    @dy.rule()
    def reasonable_bathroom_to_bedroom_ratio(cls) -> pl.Expr:
...
```

Sections: 📖 Introduction, 🎯 Usage, Defining a data frame schema, Validating data against schema

</details>

### dagster-airbyte

Package for integrating Airbyte with Dagster.

`pip install dagster-airbyte` · installs (wheel) · licence: Apache-2.0 · rank 7812 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-airbyte/)

### django-flags

Feature flags for Django projects

`pip install django-flags` · installs (wheel) · licence: CC0-1.0 · rank 7855 · last release 2026-02-10 · [PyPI](https://pypi.org/project/django-flags/) · [source](https://github.com/cfpb/django-flags)

<details><summary>README extract</summary>

Feature flags allow you to toggle functionality in both Django code and the Django templates based on configurable conditions. Flags can be useful for staging feature deployments, for A/B testing, or for any time you need an on/off switch for blocks of code. ...

Sections: Django-Flags, Dependencies, Documentation, Getting help, Getting involved, Licensing

</details>

### django-recurrence

Django utility wrapping dateutil.rrule

`pip install django-recurrence` · installs (wheel) · licence: BSD License · rank 7859 · last release 2025-12-19 · [PyPI](https://pypi.org/project/django-recurrence/)

<details><summary>README extract</summary>

django-recurrence is a utility for working with recurring dates in Django.

* Recurrence/Rule objects using a subset of rfc2445
 (wraps `dateutil.rrule`) for specifying recurring date/times,
* `RecurrenceField` for storing recurring datetimes in the database, and
* JavaScript widget. ...

Example:
```python
import recurrence.fields

class Course(models.Model):
    title = models.CharField(max_length=200)
    start = models.TimeField()
    end = models.TimeField()
    recurrences = recurrence.fields.RecurrenceField()
```

Sections: django-recurrence, Functionality, Documentation, Issues

</details>

### django-pgtransaction

A context manager/decorator which extends Django's atomic function with the ability to set isolation level and retries for a given transaction.

`pip install django-pgtransaction` · installs (wheel) · licence: BSD License · rank 7896 · last release 2025-11-30 · [PyPI](https://pypi.org/project/django-pgtransaction/) · [docs](https://django-pgtransaction.readthedocs.io) · [source](https://github.com/AmbitionEng/django-pgtransaction)

<details><summary>README extract</summary>

django-pgtransaction offers a drop-in replacement for the default `django.db.transaction` module which, when used on top of a PostgreSQL database, extends the functionality of that module with Postgres-specific features. ...

Example:
```python
import pgtransaction

with pgtransaction.atomic(isolation_level=pgtransaction.SERIALIZABLE):
    # Do queries with SERIALIZABLE isolation...
```

Sections: django-pgtransaction, Quickstart, Isolation Levels, Read-Only Transactions, Deferrable Transactions, Retries for Concurrent Updates, Nested Usage, Compatibility, Documentation, Creators

</details>

### django-jsoneditor

Django JSON Editor

`pip install django-jsoneditor` · installs (wheel) · licence: not stated · rank 7898 · last release 2023-02-15 · [PyPI](https://pypi.org/project/django-jsoneditor/)

<details><summary>README extract</summary>

Django-JSONEditor is an online structured JSON input widget for Django appropriate for various JSONField's provided for Django.

Code of the javascript JSONEditor online editor has been got from the

See the latest versions of the javascript online JSON Editor here:

Sample views:

</details>

### django-upload-validator

A simple Django file type validator using python-magic

`pip install django-upload-validator` · installs (wheel) · licence: MIT · rank 7941 · last release 2022-02-12 · [PyPI](https://pypi.org/project/django-upload-validator/)

<details><summary>README extract</summary>

Django Upload Validator is a simple utility for validating file types and extensions using `python-magic` library.

Example:
```python
from upload_validator import FileTypeValidator

validator = FileTypeValidator(
    allowed_types=['application/msword'],
    allowed_extensions=['.doc', '.docx']
)

file_resource = open('sample.doc')

# ValidationError will be raised in case of invalid type or extension
validator(file_resource)
```

Sections: Django Upload Validator, Usage, Running Tests

</details>

### deadcode

Find and remove dead code.

`pip install deadcode` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 7988 · last release 2026-11-07 · [PyPI](https://pypi.org/project/deadcode/) · [docs](https://deadcode.readthedocs.io/)

_README extract left out: share-alike licence._

### dagster-duckdb

Package for DuckDB-specific Dagster framework op and resource components.

`pip install dagster-duckdb` · installs (wheel) · licence: Apache-2.0 · rank 8003 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-duckdb/)

### django-tenants-smart-executor

Executors for django-tenants which check whether any migrations need running before running them, making it faster.

`pip install django-tenants-smart-executor` · installs (wheel) · licence: MIT · rank 8016 · last release 2026-08-27 · [PyPI](https://pypi.org/project/django-tenants-smart-executor/) · [source](https://github.com/xelixdev/django-tenants-smart-executor)

<details><summary>README extract</summary>

When using django-tenants, running migrations becomes quite a problem time-wise, especially as your list of tenants grows and the number of your apps and models increases.
This is the case even if there are actually no migrations to run.

This package provides two methods of speeding up migrations for `django-tenants`.

1. ...

Example:
```python
SMART_EXECUTOR_LIMIT_STATE_TO_SCHEMA = "full"
SMART_EXECUTOR_LIMIT_STATE_EXCEPTIONS_MAP: dict[bool, set[str]] = {
    True: {  # in tenant schema, do migrate these public apps
        "account",
    },
    False: set(),  # in public schema, there are no exceptions for any tenant apps
}
```

Sections: Django Tenants Smart Executor, Skipping schema migration if there are no migrations to run, Skipping state migration on schema, When to use this

</details>

### dynamixel-sdk

Dynamixel SDK 4. python package

`pip install dynamixel-sdk` · installs (wheel) · licence: Apache 2.0 · rank 8068 · last release 2026-09-14 · [PyPI](https://pypi.org/project/dynamixel-sdk/)

### dataforseo-client

DataForSEO API documentation

`pip install dataforseo-client` · installs (wheel) · licence: not stated · rank 8071 · last release 2026-10-26 · [PyPI](https://pypi.org/project/dataforseo-client/)

<details><summary>README extract</summary>

Features:
This is a Python client providing you, as a developer, with a tool for obtaining the necessary data from DataForSEO APIs. You don't have to figure out how to make a request and process a response - all that is readily available in this client. ...

Example:
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.serp_google_organic_live_advanced_request_info import SerpGoogleOrganicLiveAdvancedRequestInfo
from pprint import pprint

...
```

Sections: OVERVIEW, YAML Spec, Documentation, Code generation, Examples of usage

</details>

### dagger-io

A client package for running Dagger pipelines in Python.

`pip install dagger-io` · installs (wheel) · licence: Apache Software License · rank 8078 · last release 2026-10-21 · [PyPI](https://pypi.org/project/dagger-io/) · [docs](https://docs.dagger.io/sdk/python) · [source](https://github.com/dagger/dagger/tree/main/sdk/python)

<details><summary>README extract</summary>

A client package for running Dagger pipelines.

The Dagger Python SDK contains everything you need to develop CI/CD pipelines in Python, and run them on any OCI-compatible container runtime.

- Python 3.10 or later
- Docker, or another OCI-compatible container runtime ...

Example:
```python
import sys

import anyio
import dagger
from dagger import dag

async def main(args: list[str]):
    async with dagger.connection():
        # build container with cowsay entrypoint
        ctr = (
            dag.container()
            .from("python:alpine")
            .with_exec(["pip", "install", "cowsay"])
        )

...
```

Sections: Dagger Python SDK, What is the Dagger Python SDK?, Requirements, Example, Learn more, Common tasks

</details>

### django-custom-commands

A Django package which allows specifying custom paths to load managenent commands from.

`pip install django-custom-commands` · installs (wheel) · licence: MIT License; Public Domain · rank 8089 · last release 2024-10-30 · [PyPI](https://pypi.org/project/django-custom-commands/) · [source](https://github.com/mikicz/django-custom-commands)

<details><summary>README extract</summary>

A Django package which allows specifying custom paths to load managenent commands from. This allows loading management commands which are not in Django apps.

Sections: Django Custom Commands, Usage, Running tests

</details>

### django-extra-views

Extra class-based views for Django

`pip install django-extra-views` · installs (wheel) · licence: MIT License · rank 8109 · last release 2025-04-22 · [PyPI](https://pypi.org/project/django-extra-views/)

<details><summary>README extract</summary>

Django-extra-views is a Django package which introduces additional class-based views
in order to simplify common design patterns such as those found in the Django
admin interface.

Supported Python and Django versions: Python 3.6+, Django 2.2-5.1,
see tox.ini for an up-to-date list.

Full documentation is available at read the docs.

Features:
- `FormSet` and `ModelFormSet` views - The formset equivalents of
 `FormView` and `ModelFormView`.
- `InlineFormSetView` - Lets you edit a formset related to a model (using
 Django's `inlineformset_factory`). ...

Example:
```python
from extra_views import FormSetView
from my_forms import AddressForm

class AddressFormSet(FormSetView):
    form_class = AddressForm
    template_name = 'address_formset.html'
```

...

</details>

### datalab-python-sdk

SDK for the Datalab document intelligence API

`pip install datalab-python-sdk` · installs (wheel) · licence: MIT · rank 8111 · last release 2026-11-06 · [PyPI](https://pypi.org/project/datalab-python-sdk/) · [docs](https://documentation.datalab.to) · [source](https://github.com/datalab-to/sdk)

<details><summary>README extract</summary>

A Python SDK for the Datalab API - it turns documents into verifiable knowledge your agents act on. Datalab is the team behind Chandra, marker, surya, and lift.

See the full documentation at

Example:
```python
from datalab_sdk import DatalabClient

client = DatalabClient() # use env var from above, or pass api_key="your_api_key_here"

# Convert PDF to markdown
result = client.convert("document.pdf")
print(result.markdown)
```

Sections: Datalab SDK, Quick Start, Authentication, Basic Usage, Progress callbacks, Conversion options, Structured extraction, Redaction, Other endpoints, Inputs, polling and errors, Workflows, CLI Usage

</details>

### django-memoized-prefetch

A memoized prefetch for Django.

`pip install django-memoized-prefetch` · installs (wheel) · licence: MIT · rank 8115 · last release 2025-11-10 · [PyPI](https://pypi.org/project/django-memoized-prefetch/) · [source](https://github.com/xelixdev/django-memoized-prefetch)

<details><summary>README extract</summary>

A Django package that provides efficient memoized prefetching for processing data in chunks, reducing database queries through intelligent caching.
In some cases it can be useful even when not processing data in chunks, for example, when there are multiple foreign keys to the same table.

Features:
`django-memoized-prefetch` optimizes Django ORM queries when processing large datasets by:
- Reusing previously fetched objects across chunks
- Memoizing prefetched objects using LRU (Least Recently Used) cache ...

Example:
```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

...

</details>

### django-datadog-logger

Django Datadog Logger integration package.

`pip install django-datadog-logger` · installs (wheel) · licence: MIT · rank 8143 · last release 2026-10-17 · [PyPI](https://pypi.org/project/django-datadog-logger/)

<details><summary>README extract</summary>

Django Datadog Logger integration package.

- Free software: MIT license
- Documentation: <

Example:
```python
API_LOG_ROOT = env.str("API_LOG_ROOT")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {"format": "{levelname} {message}", "style": "{"},
        "json": {"()": "django_datadog_logger.formatters.datadog.DatadogJSONFormatter"},
    },
    "handlers": {
...
```

Sections: Django Datadog Logger, Quick start, ddtrace

</details>

### django-lifecycle

Declarative model lifecycle hooks.

`pip install django-lifecycle` · installs (wheel) · licence: MIT License · rank 8185 · last release 2026-06-14 · [PyPI](https://pypi.org/project/django-lifecycle/) · [docs](https://rsinger86.github.io/django-lifecycle/) · [source](https://github.com/rsinger86/django-lifecycle)

<details><summary>README extract</summary>

This project provides a `@hook` decorator as well as a base model and mixin to add lifecycle hooks to your Django models. Django's built-in approach to offering lifecycle hooks is Signals. However, my team often finds that Signals introduce unnecessary indirection and are at odds with Django's "fat models" approach. ...

Example:
```python
from django_lifecycle import LifecycleModel, hook, BEFORE_UPDATE, AFTER_UPDATE
from django_lifecycle.conditions import WhenFieldValueIs, WhenFieldValueWas, WhenFieldHasChanged

class Article(LifecycleModel):
    contents = models.TextField()
    updated_at = models.DateTimeField(null=True)
...
```

</details>

### dbl-discoverx

DiscoverX - Map and Search your Lakehouse

`pip install dbl-discoverx` · installs (wheel) · licence: Other/Proprietary License · rank 8232 · last release 2025-05-02 · [PyPI](https://pypi.org/project/dbl-discoverx/)

<details><summary>README extract</summary>

Your Swiss-Army-knife for Lakehouse administration.

DiscoverX automates administration tasks that require inspecting or applying operations to a large number of Lakehouse assets.

You can execute a SQL template against multiple tables with ...

Example:
```python
from discoverx import DX
dx = DX(locale="US")
```

Sections: DiscoverX, Multi-table operations with SQL templates, A more advanced SQL example, Multi-table operations with python functions, Example Notebooks, Getting started, Available functionality, from_tables Actions, Requirements

</details>

### django-etc

Tiny stuff for Django that won't fit into separate apps.

`pip install django-etc` · installs (wheel) · licence: BSD License · rank 8248 · last release 2022-10-06 · [PyPI](https://pypi.org/project/django-etc/)

<details><summary>README extract</summary>

*Tiny stuff for Django that won't fit into separate apps.*

* etc.toolbox.get_site_url does its best to provide you with a site URL whether request object is available or not.

* etc.toolbox.import_app_module imports and returns a module from a specific app by its name. ...

Sections: django-etc, Description, Utils, Models, Admin, Forms, Template tags, Documentation

</details>

### django-rich

Extensions for using Rich with Django.

`pip install django-rich` · installs (wheel) · licence: MIT · rank 8294 · last release 2025-09-18 · [PyPI](https://pypi.org/project/django-rich/) · [source](https://github.com/adamchainz/django-rich)

<details><summary>README extract</summary>

Extensions for using Rich with Django.

Work smarter and faster with my book Boost Your Django DX which covers many ways to improve your development experience.
I wrote django-rich whilst working on the book!

Python 3.9 to 3.14 supported.

Django 4.2 to 6.0 supported.

Example:
```python
from time import sleep

from django_rich.management import RichCommand

class Command(RichCommand):
    def handle(self, *args, **options):
        self.console.print("[bold blue]Frobnicating widgets:[/bold blue]")

        with self.console.status("Starting...") as status:
            for i in range(1, 11):
...
```

Sections: django-rich, Requirements, Reference, `shell` command integration, `django_rich.management.RichCommand`, `django_rich.test.RichRunner`, Output Width on CI

</details>

### discord-webhook

Easily send Discord webhooks with Python

`pip install discord-webhook` · installs (wheel) · licence: MIT License · rank 8316 · last release 2025-03-05 · [PyPI](https://pypi.org/project/discord-webhook/) · [source](https://github.com/lovvskillz/python-discord-webhook)

<details><summary>README extract</summary>

Easily send Discord webhooks with Python (also has async support)

Example:
```python
from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url="your webhook url", content="Webhook Message")
response = webhook.execute()
```

Sections: Python Discord webhook, Examples, Basic Webhook, Create multiple instances, Get Webhook by ID, Send Webhook to a thread, Manage being Rate Limited, Webhook with Embedded Content, Edit Webhook Messages, Delete Webhook Messages, Send Files, Remove Embeds and Files, Allowed Mentions, Use Message Flags

</details>

### darker

Apply Black formatting only in regions changed since last commit

`pip install darker` · installs (wheel) · licence: BSD · rank 8401 · last release 2025-09-01 · [PyPI](https://pypi.org/project/darker/) · [source](https://github.com/akaihola/darker)

<details><summary>README extract</summary>

This utility reformats Python source code files.
However, when run in a Git repository, it compares an old revision of the source tree
to a newer revision (or the working tree). It then only applies reformatting
in regions which have changed in the Git working tree between the two revisions.

The reformatters supported are: ...

Features:
You want to start unifying code style in your project
using Black or the Ruff formatter.
Maybe you also like to standardize on how to order your imports,
or convert string formatting to use f-strings. ...

Example:
```python
if True: print('hi')
print()
if False: print('there')
```

...

</details>

### duet

A simple future-based async library for python.

`pip install duet` · installs (wheel) · licence: Apache 2 · rank 8470 · last release 2023-07-26 · [PyPI](https://pypi.org/project/duet/)

<details><summary>README extract</summary>

A simple future-based async library for python

Duet takes inspiration from the amazing trio
library and the structured concurrency
approach to async programming that it uses.
However, duet differs from trio in two major ways: ...

Sections: duet, Note

</details>

### drjit

Dr.Jit: A Just-In-Time Compiler for Differentiable Rendering

`pip install drjit` · installs (wheel) · licence: BSD License · rank 8474 · last release 2026-08-07 · [PyPI](https://pypi.org/project/drjit/)

<details><summary>README extract</summary>

Dr.Jit is a *just-in-time* (JIT) compiler for ordinary and differentiable
computation. It was originally created as the numerical foundation of Mitsuba
3, a differentiable Monte
Carlo renderer. However,
*Dr.Jit* is a general-purpose tool that can also help with various other types
of embarrassingly parallel computation. ...

Sections: About this project, Difference to machine learning frameworks, Cloning, Documentation

</details>

### deepseek-recipe

Python bindings for deepseek-recipe components

`pip install deepseek-recipe` · installs (wheel) · licence: MIT · rank 8504 · last release 2026-10-20 · [PyPI](https://pypi.org/project/deepseek-recipe/) · [docs](https://github.com/deepseek-ai/deepseek-recipe/tree/main/docs) · [source](https://github.com/deepseek-ai/deepseek-recipe)

<details><summary>README extract</summary>

Python bindings for deepseek-recipe: conversion of Messages, Chat Completions,
and Responses requests, rendering of DeepSeek V4/V4.1 conversations into
prompts, encoding of conversations into token IDs with an attached tokenizer,
image preprocessing, and response streaming. ...

Example:
```python
from deepseek_recipe import ChatCompletionRequest, ConversionOptions, DeepseekV41Encoding

request = ChatCompletionRequest({
    "model": "DeepSeek-V4.1-Flash",
    "messages": [{"role": "user", "content": "Hello"}],
})
converted = request.convert(ConversionOptions())
rendered = DeepseekV41Encoding().render_conversation(converted.conversation)
...
```

Sections: deepseek-recipe-python, Example

</details>

### dash-iconify

Iconify for Plotly Dash

`pip install dash-iconify` · installs (wheel) · licence: MIT · rank 8524 · last release 2022-04-21 · [PyPI](https://pypi.org/project/dash-iconify/)

<details><summary>README extract</summary>

Dash Iconify based on Iconify is a Dash component library which brings over 100,000 vector icons.

Example:
```python
from dash_iconify import DashIconify
from dash import Dash

app = Dash(name)

app.layout = DashIconify(
    icon="ion:logo-github",
    width=30,
    height=30,
    rotate=1,
    flip="horizontal",
)

if name == "main":
    app.run_server(debug=True)
```

Sections: Dash Iconify, Quickstart, Using with dmc, Keyword Arguments

</details>

### django-click

Build Django management commands using the click CLI package.

`pip install django-click` · installs (wheel) · licence: MIT · rank 8526 · last release 2026-01-10 · [PyPI](https://pypi.org/project/django-click/)

<details><summary>README extract</summary>

Project information:

Automated code metrics:

`django-click` is a library to easily write Django management commands using the
`click` command line library.

* Free software: MIT license

* Compatible with Django 4.2, 5.2 and 6.0 running on Python 3.10, 3.11, 3.12, 3.13 and 3.14 ...

Example:
```python
import djclick as click

@click.command()
@click.argument('name')
def command(name):
    click.secho(f'Hello, {name}', fg='red')
```

Sections: Django Click, Example

</details>

### django-snowflake

Django backend for Snowflake

`pip install django-snowflake` · installs (wheel) · licence: MIT License · rank 8536 · last release 2026-08-19 · [PyPI](https://pypi.org/project/django-snowflake/) · [source](https://github.com/Snowflake-Labs/django-snowflake)

<details><summary>README extract</summary>

Example:
```python
>>> JSONModel.objects.filter(value__k={"l": "m"})
```

Sections: Snowflake backend for Django, Persistent connections, Snowpark Container Services (SPCS) connections, Notes on Django fields, Notes on Django QuerySets, Known issues and limitations, Troubleshooting, Debug logging

</details>

### datadog-cdk-constructs-v2

CDK Construct Library to automatically instrument Python and Node Lambda functions with Datadog using AWS CDK v2

`pip install datadog-cdk-constructs-v2` · installs (wheel) · licence: OSI Approved · rank 8549 · last release 2026-11-03 · [PyPI](https://pypi.org/project/datadog-cdk-constructs-v2/) · [source](https://github.com/DataDog/datadog-cdk-constructs)

<details><summary>README extract</summary>

Use this Datadog CDK Construct Library to deploy serverless applications using AWS CDK.

For more information on the DatadogECSFargate construct, see here.

For more information on the DatadogECSManagedInstances construct, see here. ...

Example:
```python
import { DatadogLambda, DatadogDefaultLayerVersions } from "datadog-cdk-constructs-v2";

const datadogLambda = new DatadogLambda(this, "datadogLambda", {
  // Lambda library layer versions are optional; they default to the latest
  // version bundled with this construct. Set them to pin a specific version.
  addLayers: <BOOLEAN>,
...
```

Sections: Datadog CDK Constructs, Lambda, npm, PyPI, Note, Go, Maven (Java), Usage, AWS CDK, TypeScript, Python, Java, Source Code Integration

</details>

### darkgraylib

Common supporting code for Darker and Graylint

`pip install darkgraylib` · installs (wheel) · licence: BSD-3-Clause · rank 8577 · last release 2025-11-02 · [PyPI](https://pypi.org/project/darkgraylib/) · [source](https://github.com/akaihola/darkgraylib)

<details><summary>README extract</summary>

This package is a placeholder for common supporting code for Darker and Graylint.

Such pieces of code have been moved from Darker to this new package.

Features:
Darker and Graylint originate from the same original Darker code base. In February
2023, linter support was decided to be moved out from Darker. Obviously, the two tools
are still very similar and share a lot of under-the-hood functionality. ...

Sections: darkgraylib, What?, Why?, GitHub stars trend

</details>

### django-safemigrate

Safely run migrations before deployment

`pip install django-safemigrate` · installs (wheel) · licence: MIT · rank 8584 · last release 2025-06-03 · [PyPI](https://pypi.org/project/django-safemigrate/) · [source](https://github.com/ryanhiebert/django-safemigrate)

<details><summary>README extract</summary>

django-safemigrate adds a `safemigrate` command to Django
to allow for safely running a migration command when deploying.

Example:
```python
from django_safemigrate import Safe

class Migration(migrations.Migration):
    safe = Safe.before_deploy
```

Sections: django-safemigrate: Safely run migrations before deployment, Usage, Safety Options, Pre-commit Hook, Nonstrict Mode, Disabled Mode

</details>

### dbt-glue

dbt adapter for AWS Glue

`pip install dbt-glue` · installs (wheel) · licence: Apache Software License · rank 8596 · last release 2026-09-10 · [PyPI](https://pypi.org/project/dbt-glue/)

<details><summary>README extract</summary>

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.
dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis. ...

Example:
```python
def model(dbt, spark):
    # Configure the model
    dbt.config(materialized='python_model', file_format='iceberg')

    # Create your DataFrame using Spark
    data = [
        (1, 'Alice', 100),
        (2, 'Bob', 200),
        (3, 'Charlie', 300)
    ]
    columns = ['id', 'name', 'value']

    # Return a Spark DataFrame
...
```

...

</details>

### dockerfile

Parse a dockerfile into a high-level representation using the official go parser.

`pip install dockerfile` · installs (wheel) · licence: MIT License · rank 8618 · last release 2025-01-04 · [PyPI](https://pypi.org/project/dockerfile/)

<details><summary>README extract</summary>

The goal of this repository is to provide a wrapper around
docker/docker's parser for dockerfiles.

Example:
```python
>>> dockerfile.all_cmds()
('add', 'arg', 'cmd', 'copy', 'entrypoint', 'env', 'expose', 'from', 'healthcheck', 'label', 'maintainer', 'onbuild', 'run', 'shell', 'stopsignal', 'user', 'volume', 'workdir')
```

Sections: dockerfile, python library, Usage, `dockerfile.all_cmds()`, `dockerfile.parse_file(filename)`, `dockerfile.parse_string(s)`, go library

</details>

### devcycle-python-server-sdk

DevCycle Python SDK

`pip install devcycle-python-server-sdk` · installs (wheel) · licence: not stated · rank 8676 · last release 2026-10-08 · [PyPI](https://pypi.org/project/devcycle-python-server-sdk/)

<details><summary>README extract</summary>

The DevCycle Python SDK used for feature management.

</details>

### dagster-gcp-pandas

Package for storing Pandas DataFrames in GCP.

`pip install dagster-gcp-pandas` · installs (wheel) · licence: Apache-2.0 · rank 8687 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-gcp-pandas/)

### django-hashids

Non-intrusive hashids library for Django

`pip install django-hashids` · installs (wheel) · licence: MIT License · rank 8711 · last release 2025-11-12 · [PyPI](https://pypi.org/project/django-hashids/) · [source](https://github.com/ericls/django-hashids)

<details><summary>README extract</summary>

django-hashids is a simple and non-intrusive hashids library for Django. It acts as a model field, but it does not touch the database or change the model.

Features:
- Proxy the internal model `pk` field without storing the value in the database.
- Allows lookups and filtering by hashid string.
- Can be used as sort key
- Allows specifying a salt, min_length and alphabet globally ...

Example:
```python
from django_hashids import HashidsField

class TestModel(Model):
    hashid = HashidsField(real_field_name="id")
```

Sections: Django Hashids, Features, Usage, Examples, Using with URLs, Config

</details>

### deno-sandbox

Deno Sandbox Python SDK

`pip install deno-sandbox` · installs (wheel) · licence: not stated · rank 8793 · last release 2026-07-22 · [PyPI](https://pypi.org/project/deno-sandbox/) · [source](https://github.com/denoland/sandbox-py)

<details><summary>README extract</summary>

The official Python SDK for Deno Sandboxes - isolated, secure environments running in lightweight Linux microVMs. Create on-demand sandboxes to execute untrusted code, run shell commands, build AI agents with code execution capabilities, or provide interactive development environments.

Features:
- Secure Isolation - Each sandbox runs in its own microVM with full process and filesystem isolation
- Sync & Async APIs - First-class support for both synchronous and asynchronous Python code ...

Example:
```python
from deno_sandbox import DenoDeploy

sdk = DenoDeploy()

with sdk.sandbox.create() as sb:
    # Run a shell command
    process = sb.spawn("echo", args=["Hello from the sandbox!"])
    process.wait()

    # Write and read files
...

</details>

### dbt-fusion-package-tools

Add your description here

`pip install dbt-fusion-package-tools` · does not install on CPython 3.14 · licence: not stated · rank 8800 · last release 2026-09-09 · [PyPI](https://pypi.org/project/dbt-fusion-package-tools/)

<details><summary>README extract</summary>

This directory contains code used by the `packages` option in the CLI that upgrades packages in a project to a Fusion-compatible version. The code is centered on four classes:
* DbtPackageFile: represents a file (currently packages.yml or dependencies.yml) that contains package dependencies for a project
* DbtPackage: represents a package that is ...

Sections: Package Management, How the CLI works, Scripts, TODO

</details>

### diastatic-malt

A library for Python operator overloading

`pip install diastatic-malt` · installs (wheel) · licence: Apache Software License · rank 8801 · last release 2026-03-09 · [PyPI](https://pypi.org/project/diastatic-malt/)

<details><summary>README extract</summary>

DiastaticMalt is a tool for source-to-source transformations and operator
overloading in Python, including the overloading built-in Python keywords.
It can be utilized to transform regular Python code into a new form better
suited for specific purposes, such as program capture. ...

</details>

### django-statici18n

A Django app that compiles i18n JavaScript catalogs to static files.

`pip install django-statici18n` · installs (wheel) · licence: BSD License · rank 8803 · last release 2026-09-02 · [PyPI](https://pypi.org/project/django-statici18n/) · [source](https://github.com/zyegfryed/django-statici18n)

<details><summary>README extract</summary>

Features:
When dealing with internationalization in JavaScript code, Django provides
the JSONCatalog view which sends out a JavaScript code library with
functions that mimic the gettext interface, plus an array of translation
strings. ...

Sections: django-statici18n, Overview

</details>

### dbt-autofix

CLI to autofix deprecations in dbt projects

`pip install dbt-autofix` · does not install on CPython 3.14 · licence: not stated · rank 8804 · last release 2026-09-09 · [PyPI](https://pypi.org/project/dbt-autofix/)

<details><summary>README extract</summary>

dbt-autofix automatically scans your dbt project for deprecated configurations and updates them to align with the latest best practices. This makes it easier to resolve deprecation warnings introduced in dbt v1.10 as well as prepare for migration to the dbt v2 engine. ...

Sections: dbt-autofix, Deprecation Coverage - Project Files, Deprecation Coverage - CLI Commands, In dbt Studio, From PyPi, With uv (recommended), With pip, From the source repo, Usage, `deprecations` - the main one, `packages` - the new one, `jobs`, Using `AGENTS.md`, Pre-commit Hooks

</details>

### django-impersonate

Django app to allow superusers to impersonate other users.

`pip install django-impersonate` · installs from source (sdist only) · licence: BSD License · rank 8824 · last release 2025-04-05 · [PyPI](https://pypi.org/project/django-impersonate/)

<details><summary>README extract</summary>

Simple application to allow superusers to "impersonate" other
non-superuser accounts.

Version: 1.9.5

Project Links:
Issues
- Mailing
List -
Contributing

Author: Peter Sanchez (

Example:
```python
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^impersonate/', include('impersonate.urls')),
    ... (all your other urls here) ...
)
```

Sections: django-impersonate, Dependencies, Use, Functionality, Signals, Settings, Copyright & Warranty

</details>

### django-apscheduler

APScheduler for Django

`pip install django-apscheduler` · installs (wheel) · licence: MIT License · rank 8875 · last release 2024-09-28 · [PyPI](https://pypi.org/project/django-apscheduler/)

<details><summary>README extract</summary>

APScheduler for Django.

This is a Django app that adds a lightweight wrapper around APScheduler. It enables storing persistent jobs in the
database using Django's ORM.

django-apscheduler is a great choice for quickly and easily adding basic scheduling features to your Django applications
with minimal dependencies and very little additional ...

Example:
```python
# runapscheduler.py
import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
...
```

</details>

### discord

A mirror package for discord.py. Please install that instead.

`pip install discord` · installs (wheel) · licence: not stated · rank 8881 · last release 2023-08-10 · [PyPI](https://pypi.org/project/discord/)

<details><summary>README extract</summary>

It is recommended to install `discord.py` instead.

</details>

### dataframe-image

Embed pandas DataFrames as images in pdf and markdown files when converting from Jupyter Notebooks

`pip install dataframe-image` · installs (wheel) · licence: MIT License · rank 8906 · last release 2025-01-30 · [PyPI](https://pypi.org/project/dataframe-image/)

<details><summary>README extract</summary>

A package to convert pandas DataFrames as images.

Also convert Jupyter Notebooks to PDF and/or Markdown embedding dataframe as image into it.

dataframe_image has the ability to export both normal and styled DataFrames as images from within a Python script. ...

Example:
```python
>>> import dataframe_image as dfi
>>> dfi.export(df_styled, 'df_styled.png')
```

Sections: dataframe_image, Exporting individual DataFrames, Export Jupyter Notebook, Usage, Configuration, table_conversion, Browser backend, Other parameters, PDF Conversion - LaTeX vs Chrome Browser, More features, As a Python Library, From the Command Line, Finding Google Chrome, In Google Colab

</details>

### django-templated-mail

Send emails using Django template system.

`pip install django-templated-mail` · installs (wheel) · licence: MIT License · rank 8911 · last release 2018-02-01 · [PyPI](https://pypi.org/project/django-templated-mail/)

<details><summary>README extract</summary>

A simple wrapper for `django.core.mail.EmailMultiAlternatives` which makes
use of Django template system to store email content in separate file.

Developed by SUNSCRAPERS with passion & patience.

Sections: django-templated-mail, Documentation

</details>

### django-pandas

Tools for working with pydata.pandas in your Django projects

`pip install django-pandas` · installs (wheel) · licence: BSD License · rank 9000 · last release 2024-04-03 · [PyPI](https://pypi.org/project/django-pandas/)

<details><summary>README extract</summary>

Tools for working with pandas in your Django
projects

Example:
```python
class MyModel(models.Model):

    full_name = models.CharField(max_length=25)
    age = models.IntegerField()
    department = models.CharField(max_length=3)
    wage = models.FloatField()
```

Sections: Django Pandas, What's New, Dependencies, Usage, IO Module, read_frame, Examples, DataFrameManager, to_dataframe, to_timeseries, to_pivot_table, CHANGES

</details>

### dbt-sqlite

A SQLite adapter plugin for dbt (data build tool)

`pip install dbt-sqlite` · installs (wheel) · licence: Apache Software License · rank 9044 · last release 2025-06-27 · [PyPI](https://pypi.org/project/dbt-sqlite/)

<details><summary>README extract</summary>

Please see the github repository for detailed information

</details>

### dbt-score

Linter for dbt metadata.

`pip install dbt-score` · installs (wheel) · licence: MIT License · rank 9094 · last release 2026-10-07 · [PyPI](https://pypi.org/project/dbt-score/)

<details><summary>README extract</summary>

**A comprehensive linter for dbt metadata that helps maintain high-quality data
models at scale.**

Features:
- 🔍 Comprehensive Linting: Evaluates dbt entities against configurable
 rules for documentation, tests, naming, and structure
- 📊 Scoring System: Provides numerical scores (0-10) for individual models
 and overall project health ...

Example:
```python
from dbt_score import Model, rule, RuleViolation

@rule
def model_has_business_owner(model: Model) -> RuleViolation:
    if model.meta.get("business_owner") is None:
        return RuleViolation("Model lacks a business owner.")
```

...

</details>

### duplocloud-client

Command line Client for interacting with Duplocloud portals.

`pip install duplocloud-client` · installs (wheel) · licence: MIT License · rank 9150 · last release 2026-07-20 · [PyPI](https://pypi.org/project/duplocloud-client/) · [docs](https://cli.duplocloud.com/) · [source](https://github.com/duplocloud/duploctl)

<details><summary>README extract</summary>

CLI and Python SDK for managing DuploCloud infrastructure. Works as a standalone command-line tool or as a Python module in your own scripts and CI/CD pipelines.

- 30+ resource types -- tenants, services, infrastructure, hosts, RDS, S3, Lambda, ECS, Batch, Argo Workflows, and more ...

Example:
```python
from duplocloud.controller import DuploCtl

# Reads DUPLO_HOST, DUPLO_TOKEN, DUPLO_TENANT from env
duplo, args = DuploCtl.from_env()

# Callable interface (like CLI syntax)
services = duplo("service", "list")
tenant = duplo("tenant", "find", "mytenant")
```

Sections: duploctl, Quick Start, Configuration, CLI Usage, Cloud Access (JIT), Resource Management, Python Module, From Environment Variables, From Explicit Credentials, Create Resources, Docker, CI/CD, Resources

</details>

### dagster-polars

Dagster integration library for Polars

`pip install dagster-polars` · installs (wheel) · licence: Apache Software License · rank 9224 · last release 2026-05-22 · [PyPI](https://pypi.org/project/dagster-polars/) · [source](https://github.com/dagster-io/community-integrations/tree/main/libraries/dagster-polars)

<details><summary>README extract</summary>

This library provides Dagster integration with Polars.
It allows using Polars DataFrames as inputs and outputs with Dagster's `@asset` and `@op`.
Type annotations are used to control whether to load an eager or lazy DataFrame, or other types supported by `dagster-polars`. ...

</details>

### dateformat

Parse and format dates quickly

`pip install dateformat` · installs from source (sdist only) · licence: MIT · rank 9235 · last release 2019-04-04 · [PyPI](https://pypi.org/project/dateformat/)

<details><summary>README extract</summary>

`dateformat` does two things: turn `datetime` objects into strings, and turn strings into `datetime` objects.
 It's goal is to do these things simply and well, and to satisfy the following criteria: ...

Example:
```python
>>> from dateformat import DateFormat

>>> date_format = DateFormat("YYYY-MM-DD hh:mm:ss.SSSS+HH:MM")
```

</details>

### doccmd

Run commands against code blocks in reStructuredText and Markdown files.

`pip install doccmd` · installs (wheel) · licence: MIT · rank 9262 · last release 2026-09-16 · [PyPI](https://pypi.org/project/doccmd/) · [docs](https://adamtheturtle.github.io/doccmd/) · [source](https://github.com/adamtheturtle/doccmd)

<details><summary>README extract</summary>

A command line tool for running commands against code blocks in documentation files.
This allows you to run linters, formatters, and other tools against the code blocks in your documentation files.

Example:
```python
"""Example function which is used in a future code block."""

def my_function() -> None:
    """Do nothing."""
```

Sections: doccmd, With `pip`, With Homebrew (macOS, Linux, WSL), With winget (Windows), Pre-built Linux (x86) binaries, Pre-built macOS (ARM) binaries, Pre-built Windows binaries, With Docker, With Nix, Using `doccmd` as a pre-commit hook, Usage example, What does it work on?, Formatters and padding, pycon code blocks

</details>

### delegator.py

Subprocesses for Humans 2.0.

`pip install delegator.py` · installs (wheel) · licence: MIT · rank 9395 · last release 2018-09-17 · [PyPI](https://pypi.org/project/delegator.py/)

<details><summary>README extract</summary>

Delegator.py — Subprocesses for Humans 2.0

Delegator.py is a simple library for dealing with subprocesses, inspired
by both envoy and pexpect (in fact, it depends on it!).

This module features two main functions `delegator.run()` and `delegator.chain()`. ...

Example:
```python
>>> c = delegator.run('ls')
>>> print c.out
README.rst   delegator.py

>>> c = delegator.run('long-running-process', block=False)
>>> c.pid
35199
>>> c.block()
>>> c.return_code
0
```

</details>

### drafthorse

Python ZUGFeRD XML implementation

`pip install drafthorse` · installs (wheel) · licence: Apache Software License · rank 9436 · last release 2025-09-15 · [PyPI](https://pypi.org/project/drafthorse/)

<details><summary>README extract</summary>

This is a low-level python implementation of the ZUGFeRD XML format. ZUGFeRD is a German
format for sending digital invoices. ZUGFeRD XML files are to be attached to a PDF
file. This library can be used to generate or parse the contents of this XML file as well as
attach it to a PDF. We do not support parsing PDF files (for now). ...

Example:
```python
from drafthorse.models.document import Document
samplexml = open("sample.xml", "rb").read()
doc = Document.parse(samplexml)
print(doc.trade.agreement.seller.name)
```

Sections: drafthorse -- Basic ZUGFeRD implementation in Python, Maintenance note, Usage

</details>

### django-ace

django-ace provides of ACE editor with Django

`pip install django-ace` · installs (wheel) · licence: BSD-2-Clause · rank 9467 · last release 2026-05-14 · [PyPI](https://pypi.org/project/django-ace/)

<details><summary>README extract</summary>

Example:
```python
from django import forms
from django_ace import AceWidget

class EditorForm(forms.Form):
    text = forms.CharField(widget=AceWidget(width=None, height=None))
```

Sections: django-ace, Usage, Example Project, v1.44.0, v1.43.5, v1.43.3, v1.42.0, v1.39.1, v1.38.0, v1.37.5, v1.36.2, v1.32.4, v1.32.3, v1.32.0

</details>

### dbstream

A meta package to be connected to several databases

`pip install dbstream` · installs from source (sdist only) · licence: MIT License · rank 9515 · last release 2024-10-15 · [PyPI](https://pypi.org/project/dbstream/)

### databricksapi

Python Databricks API wrapper using requests module

`pip install databricksapi` · installs from source (sdist only) · licence: MIT License · rank 9548 · last release 2020-04-03 · [PyPI](https://pypi.org/project/databricksapi/)

<details><summary>README extract</summary>

*This package is a Python Implementation of the Databricks API for structured and programmatic use. This Python implementation requires that your Databricks API Token be saved as an environment variable in your system:* `export DATABRICKS_TOKEN=MY_DATABRICKS_TOKEN` in OSX / Linux. ...

Example:
```python
from databricksapi import Workspace
url = '
token = 'dapiXXXXXXXXXXXXX'
ws = Workspace(url, token)
```

Sections: Databricks API Documentation, UPDATE, APIs Included, Imports, Token API, Methods, createToken(*lifetime_seconds*, *comment*), listTokens(), revokeToken(*token_id*), Secrets API, createSecretScope(*scope*, *initial_manage_princial*), deleteSecretScope(*scope*), listSecretScopes()

</details>

### discord-markdown-py

(no summary)

`pip install discord-markdown-py` · installs (wheel) · licence: not stated · rank 9697 · last release 2026-11-04 · [PyPI](https://pypi.org/project/discord-markdown-py/)

### django-request-logging

Django middleware that logs http request body.

`pip install django-request-logging` · installs (wheel) · licence: MIT · rank 9707 · last release 2022-02-23 · [PyPI](https://pypi.org/project/django-request-logging/)

<details><summary>README extract</summary>

Plug django-request-logging into your Django project and you will have intuitive and color coded request/response payload logging, for both web requests and API requests. Supports Django 1.8+.

Sections: django-request-logging, Details, Django settings, REQUEST_LOGGING_DATA_LOG_LEVEL, REQUEST_LOGGING_ENABLE_COLORIZE, REQUEST_LOGGING_DISABLE_COLORIZE (Deprecated), REQUEST_LOGGING_MAX_BODY_LENGTH, REQUEST_LOGGING_HTTP_4XX_LOG_LEVEL, REQUEST_LOGGING_SENSITIVE_HEADERS, DJANGO_REQUEST_LOGGING_LOGGER_NAME, DJANGO_REQUEST_LOGGING_NO_LOGGING_DEFAULT_VALUE, DJANGO_REQUEST_LOGGING_LOG_HEADERS_DEFAULT_VALUE = True, DJANGO_REQUEST_LOGGING_LOG_BODY_DEFAULT_VALUE = True, DJANGO_REQUEST_LOGGING_LOG_RESPONSE_DEFAULT_VALUE = True

</details>

### dimod

A shared API for binary quadratic model samplers.

`pip install dimod` · installs (wheel) · licence: Apache-2.0 · rank 9776 · last release 2026-10-22 · [PyPI](https://pypi.org/project/dimod/) · [docs](https://docs.dwavequantum.com) · [source](https://github.com/dwavesystems/dimod)

<details><summary>README extract</summary>

`dimod` is a shared API for samplers. It provides:

* Classes for quadratic models---such as the binary quadratic model (BQM)
 class that contains Ising and QUBO models used by samplers such as the
 D-Wave quantum computer---and higher-order (non-quadratic) models.
* Reference examples of samplers and composed samplers. ...

</details>

### dagster-snowflake-pandas

Package for integrating Snowflake and Pandas with Dagster.

`pip install dagster-snowflake-pandas` · installs (wheel) · licence: Apache-2.0 · rank 9778 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-snowflake-pandas/)

### devpi-common

Utilities jointly used by devpi-server, devpi-client and others.

`pip install devpi-common` · installs (wheel) · licence: MIT License · rank 9789 · last release 2026-10-27 · [PyPI](https://pypi.org/project/devpi-common/) · [source](https://github.com/devpi/devpi)

<details><summary>README extract</summary>

This package contains utility functions used by devpi-server and devpi-client.

See for more information.

Sections: 4.1.2 (2026-10-26), Bug Fixes, 4.1.1 (2026-02-09), 4.1.0 (2025-05-18), Other Changes, 4.0.4 (2024-04-20), 4.0.3 (2023-11-23)

</details>

### django-concurrency

Optimistic lock implementation for Django. Prevents users from doing concurrent editing

`pip install django-concurrency` · installs (wheel) · licence: MIT · rank 9823 · last release 2026-04-08 · [PyPI](https://pypi.org/project/django-concurrency/)

<details><summary>README extract</summary>

django-concurrency is an optimistic lock implementation for Django.

It prevents users from doing concurrent editing in Django both from UI and from a
django command.

How it works

Now if you try::

you will get a ``RecordModifiedError`` on ``b.save()``

Similar projects ...

Example:
```python
from django.db import models
from concurrency.fields import IntegerVersionField

class ConcurrentModel( models.Model ):
    version = IntegerVersionField( )
    name = models.CharField(max_length=100)
```

</details>

### dowhy

DoWhy is a Python library for causal inference that supports explicit modeling and testing of causal assumptions

`pip install dowhy` · does not install on CPython 3.14 · licence: MIT License · rank 9887 · last release 2025-11-08 · [PyPI](https://pypi.org/project/dowhy/) · [docs](https://py-why.github.io/dowhy) · [source](https://github.com/py-why/dowhy)

<details><summary>README extract</summary>

- The documentation, user guide, sample notebooks and other information are available at

- DoWhy is part of the PyWhy Ecosystem. For more tools and libraries related to causality, checkout the PyWhy GitHub organization!
- For any questions, comments, or discussions about specific use cases, join our community on Discord () ...

Features:
DoWhy supports the following causal tasks:

- Effect estimation (identification, average causal effect, conditional average causal effect, instrumental variables and more) ...

Example:
```python
from dowhy import CausalModel
import dowhy.datasets

# Load some sample data
data = dowhy.datasets.linear_dataset(
    beta=10,
    num_common_causes=5,
    num_instruments=2,
    num_samples=10000,
    treatment_is_binary=True)
```

...

</details>

### DeepFriedMarshmallow

A plug-and-play JIT implementation for Marshmallow to speed up data serialization and deserialization

`pip install DeepFriedMarshmallow` · installs (wheel) · licence: Apache Software License · rank 9891 · last release 2025-09-03 · [PyPI](https://pypi.org/project/DeepFriedMarshmallow/)

<details><summary>README extract</summary>

I need to be honest with you — I have no idea how to compare the speed of a
marshmallow and the speed of a chicken nugget. I really liked that headline,
though, so let's just assume that a nugget is indeed faster than a
marshmallow. So is this project, Deep-Fried Marshmallow, faster than
vanilla Marshmallow. ...

Example:
```python
from marshmallow import Schema, fields

class ArtistSchema(Schema):
    name = fields.Str()

class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())

schema = AlbumSchema()
```

Sections: Plugin System, Per-schema Controls, Enabling Deep-Fried Marshmallow, Auto-patching all Marshmallow schemas, Custom Schema classes, Patcher functions, How it works, Special thanks to

</details>

### django-utils-six

Forward compatibility django.utils.six for Django 3

`pip install django-utils-six` · installs (wheel) · licence: BSD License · rank 9901 · last release 2020-06-17 · [PyPI](https://pypi.org/project/django-utils-six/) · [source](https://github.com/whtsky/django-utils-six)

<details><summary>README extract</summary>

Forward compatibility django.utils.six for Django 3

Code is taken from Django 2.2

Features:
I found `django.utils.six` is solely responsible for plenty of libraries' incompatibility with Django 3.

Sections: django-utils-six, Why?

</details>

### databind

Databind is a library inspired by jackson-databind to de-/serialize Python dataclasses. The `databind` package will install the full suite of databind packages. Compatible with Python 3.8 and newer.

`pip install databind` · installs (wheel) · licence: MIT · rank 9957 · last release 2026-05-22 · [PyPI](https://pypi.org/project/databind/) · [docs](https://niklasrosenstein.github.io/python-databind/) · [source](https://github.com/NiklasRosenstein/python-databind)

<details><summary>README extract</summary>

The `databind` package provides a (de)serialization framework that understands most native Python types as well as
dataclasses, as well as an implementation for serialize to/from JSON-like nested data structures.

Databind is intended mostly for flexible and easy to use configuration loading. ...

Features:
* Support for a plethora of builtin types, including `Enum`, `Decimal`, `UUID`, `Path`, `datetime`, `date`,
 `time`, `timedelta`
* Support for multiple union serialization modes (nested, flat, keyed, `typing.Literal`)
* Support for generic types, ...

Example:
```python
@dataclass
class Server:
    host: str
    port: int

@dataclass
class Config:
    server: Server

from databind.json import dump, load

dict_payload = {"server": {"host": "localhost", "port": 8080}}
...

</details>

### django-sql-utils

Improved API for aggregating using Subquery

`pip install django-sql-utils` · installs (wheel) · licence: MIT License · rank 9962 · last release 2023-09-28 · [PyPI](https://pypi.org/project/django-sql-utils/)

<details><summary>README extract</summary>

This package provides utilities for working with Django querysets so that
you can generate the SQL that you want, with an API you enjoy.

The `Count` aggregation in Django:
generates SQL like the following:
In many cases, this is not as performant as doing the count in a SUBQUERY
instead of with a JOIN:
Django allows us to generate this SQL using ...

Example:
```python
Parent.objects.annotate(child_count=Count('child'))
```

Sections: Django SQL Utils, Subquery Aggregates, Easier API for Exists

</details>

### dataclass-factory

An utility class for creating instances of dataclasses

`pip install dataclass-factory` · installs (wheel) · licence: Apache Software License · rank 9976 · last release 2022-07-20 · [PyPI](https://pypi.org/project/dataclass-factory/)

<details><summary>README extract</summary>

dataclass_factory is a modern way to convert dataclasses or other objects to and from more common types like dicts

See documentation for more details.

Install

Use

Example:
```python
from dataclasses import dataclass
import dataclass_factory

@dataclass
class Book:
    title: str
    price: int
    author: str = "Unknown author"

data = {
    "title": "Fahrenheit 451",
    "price": 100,
}

factory = dataclass_factory.Factory()
book: Book = factory.load(data, Book)  # Same as Book(title="Fahrenheit 451", price=100)
...
```

Sections: dataclass_factory, Help, TL;DR, Requirements, Advantages

</details>

### django-watchman

django-watchman exposes a status endpoint for your backing services

`pip install django-watchman` · installs (wheel) · licence: BSD-3-Clause · rank 9988 · last release 2026-11-02 · [PyPI](https://pypi.org/project/django-watchman/) · [docs](https://django-watchman.readthedocs.io) · [source](https://github.com/mwarkentin/django-watchman)

<details><summary>README extract</summary>

django-watchman exposes a status endpoint for your backing services like
databases, caches, etc.

Features:
- Status endpoint -- JSON response with the health of all backing services
- Human-friendly dashboard -- HTML dashboard at `/watchman/dashboard/`
- Built-in checks -- Databases, caches, storage, and email out of the box ...

Example:
```python
re_path(r'^watchman/', include('watchman.urls')),
```

Sections: django-watchman, Features, Endpoints, Built-in Checks, Documentation, Used By, Testimonials, Quickstart, Configuration Highlights

</details>

### django-cursor-pagination

Cursor based pagination for Django

`pip install django-cursor-pagination` · installs (wheel) · licence: BSD License · rank 10001 · last release 2024-07-01 · [PyPI](https://pypi.org/project/django-cursor-pagination/)

<details><summary>README extract</summary>

A cursor based pagination system for Django. Instead of refering to specific
pages by number, we give every item in the queryset a cursor based on its
ordering values. We then ask for subsequent records by asking for records
*after* the cursor of the last item we currently have. ...

Example:
```python
from cursor_pagination import CursorPaginator

from myapp.models import Post

def posts_api(request, after=None):
    qs = Post.objects.all()
    page_size = 10
    paginator = CursorPaginator(qs, ordering=('-created', '-id'))
    page = paginator.page(first=page_size, after=after)
    data = {
        'objects': [serialize_page(p) for p in page],
...
```

</details>

### datarobot-genai

Generic helpers for GenAI

`pip install datarobot-genai` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 10021 · last release 2026-11-02 · [PyPI](https://pypi.org/project/datarobot-genai/)

<details><summary>README extract</summary>

Homepage
 PyPI
 Support

A toolkit for building agents on DataRobot.

- Unified LLM layer (DataRobot-compatible)—one `get_llm()` entry point per integration (LangGraph, LlamaIndex, CrewAI, NAT), all backed by the same LiteLLM-based routing to the DataRobot LLM Gateway, LLM deployments, NIM, or external providers. ...

Sections: DataRobot GenAI Library, Use, Prerequisites, Credentials, Standalone end-to-end examples, In-depth documentation, Semantic versioning, TestPyPI, Excluded upstream dependencies, Troubleshooting, Next steps, Publishing, Links

</details>

### ddtrace-api

The public API of the dd-trace libraries

`pip install ddtrace-api` · installs (wheel) · licence: not stated · rank 10063 · last release 2025-03-31 · [PyPI](https://pypi.org/project/ddtrace-api/) · [source](https://github.com/DataDog/dd-trace-py-api/)

### django-data-browser

Interactive user-friendly database explorer.

`pip install django-data-browser` · installs (wheel) · licence: MIT License · rank 10088 · last release 2026-10-19 · [PyPI](https://pypi.org/project/django-data-browser/)

<details><summary>README extract</summary>

Interactive, user-friendly database explorer.

There is a live demo site available here

Because it's hosted on Heroku free tier it might take a while to respond to the first page load.

The Django project is a small e-commerce site selling microservices.

Source:

Admin:

Features:
* Zero config, if it's in the admin it's in the browser.
* Select fields (including calculated fields), aggregate, filter, sort and pivot.
* Automatically follow OneToOneFields and ForeignKeys.
* Respects per user admin permissions. ...

Example:
```python
from django.db.models import Aggregate

class Percentile(Aggregate):
    arity = 1
    function = "percentile_cont"
    template = "%(function)s(%(percentile)s) WITHIN GROUP (ORDER BY %(expressions)s)"
    name = "Percentile"

...

</details>

### django-opensearch-dsl

Wrapper around opensearch-py for django models

`pip install django-opensearch-dsl` · installs from source (sdist only) · licence: Apache Software License · rank 10121 · last release 2025-11-24 · [PyPI](https://pypi.org/project/django-opensearch-dsl/)

<details><summary>README extract</summary>

Django Opensearch DSL is a package that allows the indexing of Django models in opensearch. It is built as a thin
wrapper around `opensearch-py`
so you can use all the features developed by the `opensearch-py` team.

You can view the full documentation

Features:
- Based on `opensearch-py` so you can make queries with
 the `Search`
 object.
- Management commands for creating, deleting, and populating indices and documents.
- Opensearch auto mapping from Django models fields. ...

Example:
```python
# models.py

class Car(models.Model):
    name = models.CharField()
    color = models.CharField()
    description = models.TextField()
    type = models.IntegerField(choices=[
        (1, "Sedan"),
        (2, "Truck"),
        (4, "SUV"),
    ])
```

...

</details>

### databind.json

De-/serialize Python dataclasses to or from JSON payloads. Compatible with Python 3.8 and newer. Deprecated, use `databind` module instead.

`pip install databind.json` · installs (wheel) · licence: MIT · rank 10145 · last release 2026-05-22 · [PyPI](https://pypi.org/project/databind.json/) · [docs](https://niklasrosenstein.github.io/python-databind/) · [source](https://github.com/NiklasRosenstein/python-databind)

<details><summary>README extract</summary>

Deprecated since v4.5.0. This is a proxy for depending on `databind`. Do not
depend on this package directly anymore.

</details>

### databind.core

Databind is a library inspired by jackson-databind to de-/serialize Python dataclasses. Compatible with Python 3.8 and newer. Deprecated, use `databind` package.

`pip install databind.core` · installs (wheel) · licence: MIT · rank 10151 · last release 2026-05-22 · [PyPI](https://pypi.org/project/databind.core/) · [docs](https://niklasrosenstein.github.io/python-databind/) · [source](https://github.com/NiklasRosenstein/python-databind)

<details><summary>README extract</summary>

Deprecated since v4.5.0. This is a proxy for depending on `databind`. Do not
depend on this package directly anymore.

</details>

### django-compat

For- and backwards compatibility layer for Django 1.4, 1.7, 1.8, 1.9, 1.10, and 1.11

`pip install django-compat` · installs from source (sdist only) · licence: MIT License · rank 10158 · last release 2017-12-04 · [PyPI](https://pypi.org/project/django-compat/)

<details><summary>README extract</summary>

Forward and backwards compatibility layer for Django ~~1.4~~, ~~1.7~~, 1.8, 1.9, 1.10 and 1.11

~~Consider django-compat as an experiment based on the discussion on reddit. Let's see where it goes.~~

What started as an experiment based on this discussion on reddit has proven to be true in real life.

django-compat is under active development. ...

Features:
* Be able to use the LTS versions of Django and support newer versions in your app
* Use features from newer Django versions in an old one
* Manage and master the gap between different framework versions

...

</details>

### databend-sqlalchemy

Sqlalchemy adapter for Databend

`pip install databend-sqlalchemy` · installs (wheel) · licence: Apache Software License; MIT License · rank 10193 · last release 2026-02-28 · [PyPI](https://pypi.org/project/databend-sqlalchemy/)

<details><summary>README extract</summary>

Databend dialect for SQLAlchemy.

Installation

The package is installable through PIP::

 pip install databend-sqlalchemy

Usage

The DSN format is similar to that of regular Postgres:: ...

</details>

### docspec

Docspec is a JSON object specification for representing API documentation of programming languages.

`pip install docspec` · installs (wheel) · licence: not stated · rank 10195 · last release 2025-05-06 · [PyPI](https://pypi.org/project/docspec/)

<details><summary>README extract</summary>

This Python packages provides

* A library to (de-) serialize Docspec conformat JSON payloads
* A CLI to validate and introspect such payloads

Example:

The `docspec` Python module requires Python 3.5 or newer.

Copyright © 2020, Niklas Rosenstein

Example:
```python
import docspec, sys
for module in docspec.load_modules(sys.stdin):
  module.members = [member for member in module.members if member.docstring]
  docspec.dump_module(sys.stdout)
```

</details>

### django-dynamic-preferences

Dynamic global and instance settings for your django project

`pip install django-dynamic-preferences` · installs (wheel) · licence: BSD License · rank 10205 · last release 2025-01-10 · [PyPI](https://pypi.org/project/django-dynamic-preferences/)

<details><summary>README extract</summary>

Dynamic-preferences is a Django app, BSD-licensed, designed to help you manage your project settings. While most of the time,
a `settings.py` file is sufficient, there are some situations where you need something more flexible such as:

* per-user settings (or, generally speaking, per instance settings)
* settings change without server restart ...

Features:
* Simple to setup
* Admin integration
* Forms integration
* Bundled with global and per-user preferences
* Can be extended to other models if need (e.g. per-site preferences)
* Integrates with django caching mechanisms to improve performance

Sections: django-dynamic-preferences, Features, Documentation

</details>

### dagster-pandera

Integration layer for dagster and pandera.

`pip install dagster-pandera` · installs (wheel) · licence: Apache-2.0 · rank 10229 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-pandera/)

### docspec-python

A parser based on lib2to3 producing docspec data from Python source code.

`pip install docspec-python` · installs (wheel) · licence: not stated · rank 10258 · last release 2025-05-06 · [PyPI](https://pypi.org/project/docspec-python/)

<details><summary>README extract</summary>

A parser based on `lib2to3` procuding docspec data from Python source code.

Example:

Copyright © 2020, Niklas Rosenstein

Example:
```python
from docspec_python import parse_python_module
import docspec, sys
docspec.dump_module(parse_python_module(sys.stdin, print_function=False), sys.stdout)
```

</details>

### dash-daq

DAQ components for Dash

`pip install dash-daq` · installs (wheel) · licence: MIT License · rank 10272 · last release 2025-03-11 · [PyPI](https://pypi.org/project/dash-daq/)

<details><summary>README extract</summary>

DAQ components for Dash.

Docs:

Sections: dash_daq, Documentation, Demo server, Code quality and tests, To run lint and unit tests, Demo applications

</details>

### django-ranged-response

Modified Django FileResponse that adds Content-Range headers.

`pip install django-ranged-response` · installs from source (sdist only) · licence: MIT · rank 10295 · last release 2017-07-18 · [PyPI](https://pypi.org/project/django-ranged-response/)

### django-currentuser

Conveniently store reference to request user on thread/db level.

`pip install django-currentuser` · installs (wheel) · licence: BSD License · rank 10344 · last release 2026-01-21 · [PyPI](https://pypi.org/project/django-currentuser/)

<details><summary>README extract</summary>

Example:
```python
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

# As model field:
from django_currentuser.db.models import CurrentUserField
class Foo(models.Model):
    created_by = CurrentUserField()
    updated_by = CurrentUserField(on_update=True)
```

Sections: django-currentuser, Quickstart, Differences to django-cuser, Reporting issues/improvements, Pull Requests, Setting up all Python versions

</details>

### django-prettyjson

Enables pretty JSON viewer in Django forms, admin, or templates

`pip install django-prettyjson` · installs (wheel) · licence: BSD License · rank 10350 · last release 2018-08-07 · [PyPI](https://pypi.org/project/django-prettyjson/)

<details><summary>README extract</summary>

Enables pretty JSON viewer in Django forms, admin, or templates. The viewer is adapted from jQuery JSONView. It is compatible with almost anything: JSON stored in a string, a jsonfield (using django.contrib.postgres or django-jsonfield), or any python object that can be serialized to JSON (using standardjson).

See

Example:
```python
from prettyjson import PrettyJSONWidget

class JsonForm(forms.ModelForm):
  class Meta:
    model = Test
    fields = 'all'
    widgets = {
      'myjsonfield': PrettyJSONWidget(),
    }

class JsonAdmin(admin.ModelAdmin):
  form = JsonForm
```

Sections: django-prettyjson, Demo, Configuration, Usage, Configure Rendering, Running Tests

</details>

### dynamic-network-architectures

none

`pip install dynamic-network-architectures` · installs (wheel) · licence: not stated · rank 10372 · last release 2026-06-07 · [PyPI](https://pypi.org/project/dynamic-network-architectures/)

### django-test-plus

django-test-plus provides useful additions to Django's default TestCase

`pip install django-test-plus` · installs (wheel) · licence: BSD License · rank 10488 · last release 2026-10-13 · [PyPI](https://pypi.org/project/django-test-plus/) · [docs](https://django-test-plus.readthedocs.io)

<details><summary>README extract</summary>

Useful additions to Django's default TestCase from REVSYS

Let's face it, writing tests isn't always fun. Part of the reason for
that is all of the boilerplate you end up writing. django-test-plus is
an attempt to cut down on some of that when writing Django tests. ...

Example:
```python
from test_plus.test import TestCase

class MyViewTests(TestCase):
    ...
```

Sections: django-test-plus, Rationale, Usage, Documentation, To run all tests, Keep in touch!

</details>

### devpi-client

devpi upload/install/... workflow commands for Python developers

`pip install devpi-client` · installs (wheel) · licence: MIT License · rank 10520 · last release 2026-04-30 · [PyPI](https://pypi.org/project/devpi-client/) · [docs](https://doc.devpi.net) · [source](https://github.com/devpi/devpi)

<details><summary>README extract</summary>

Features:
- Allow `patchjson` to read from stdin with `-` as JSON filename.

Sections: 7.3.0 (2026-04-30), Features, 7.2.1 (2026-03-17), Bug Fixes, 7.2.0 (2024-10-16), 7.1.0 (2024-07-17), 7.0.3 (2024-04-20)

</details>

### dask-jobqueue

Deploy Dask on job queuing systems like PBS, Slurm, SGE or LSF

`pip install dask-jobqueue` · installs (wheel) · licence: BSD 3-Clause · rank 10535 · last release 2024-08-22 · [PyPI](https://pypi.org/project/dask-jobqueue/)

<details><summary>README extract</summary>

Easy deployment of Dask Distributed on job queuing systems such as PBS, Slurm,
or SGE. See documentation for more information.

</details>

### django-components

A way to create simple reusable template components in Django.

`pip install django-components` · installs (wheel) · licence: MIT · rank 10581 · last release 2026-08-22 · [PyPI](https://pypi.org/project/django-components/) · [docs](https://django-components.github.io/django-components/)

<details><summary>README extract</summary>

`django-components` is a modular and extensible UI framework for Django.

It combines Django's templating system with the modularity seen
in modern frontend frameworks like Vue or React.

With `django-components` you can support Django projects small and large without leaving the Django ecosystem. ...

Example:
```python
# components/product_card/product_card.py
from django_components import Component, register

@register("product_card")
class ProductCard(Component):
    template_file = "product_card.html"
    js_file = "product_card.js"
    css_file = "product_card.css"

    class Kwargs:
        product_id: int
        show_price: bool = True
...
```

...

</details>

### decomp2dbg

Symbol syncing framework for decompilers and debuggers

`pip install decomp2dbg` · installs (wheel) · licence: BSD-2-Clause · rank 10614 · last release 2026-07-14 · [PyPI](https://pypi.org/project/decomp2dbg/)

<details><summary>README extract</summary>

Reverse engineering involves both static (decompiler) and dynamic (debugger) analysis, yet we often
use these analyses without sharing knowledge between the two. In the case of reversing static binaries,
context switching between debugger assembly and the symbols you have reversed in decompilation can be inefficient. ...

Features:
- [X] Auto-updating decompilation context view
- [X] Auto-syncing function names
- [X] Breakable/Inspectable symbols
- [X] Auto-syncing stack variable names
- [ ] Auto-syncing structs
- [ ] Online DWARF Creation
- [ ] Function Type Syncing ...

Sections: decomp2dbg, Decompilers, Debuggers, Usage, Decompilation View, Functions and Global Vars, Stack Vars, Register Vars, Func Args, Advanced Usage, Shared Libraries, Features

</details>

### django-heroku

This is a Django library for Heroku apps.

`pip install django-heroku` · installs (wheel) · licence: MIT License · rank 10670 · last release 2018-03-01 · [PyPI](https://pypi.org/project/django-heroku/)

<details><summary>README extract</summary>

This is a Django library for Heroku applications that ensures a seamless deployment and development experience.

This library provides:

- Settings configuration (Static files / WhiteNoise).
- Logging configuration.
- Test runner (important for Heroku CI).

Django 2.0 is targeted, but older versions of Django should be compatible. ...

Example:
```python
…
# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
```

Sections: Django-Heroku (Python Library), Usage of Django-Heroku

</details>

### django-softdelete

Soft delete support for Django ORM, with undelete.

`pip install django-softdelete` · installs (wheel) · licence: BSD License · rank 10688 · last release 2025-04-10 · [PyPI](https://pypi.org/project/django-softdelete/)

### data-platform-helpers

(no summary)

`pip install data-platform-helpers` · installs (wheel) · licence: Apache-2.0 · rank 10689 · last release 2026-08-27 · [PyPI](https://pypi.org/project/data-platform-helpers/)

<details><summary>README extract</summary>

PIP Package for a variety of Data Platform Helpers

Table of Contents:

1. Version Checker

used to determine if a relevant version attribute across related applications are valid.

There are many potential applications for this. Here are a few examples:

1. ...

Example:
```python
from data_platform_helpers.version_check import CrossAppVersionChecker
...
self.version_checker = self.CrossAppVersionChecker(
    self,
    version=x, # can be a revision of a charm, version of a snap, version of a workload, etc
    relations_to_check=[x,y,z],
    # only use if the version doesn't not need to exactly match our current version
...
```

Sections: 1. Version Checker, Purpose, How to use, 3. Interfaces

</details>

### dune-client

A simple framework for interacting with Dune Analytics official API service.

`pip install dune-client` · installs (wheel) · licence: Apache Software License · rank 10726 · last release 2026-10-26 · [PyPI](https://pypi.org/project/dune-client/) · [source](https://github.com/duneanalytics/dune-client)

<details><summary>README extract</summary>

A python framework for interacting with Dune Analytics' officially supported API
service.

Example:
```python
from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import QueryBase

query = QueryBase(
    name="Sample Query",
    query_id=1215383,
    params=[
        QueryParameter.text_type(name="TextField", value="Word"),
        QueryParameter.number_type(name="NumberField", value=3.1415926535),
...
```

Sections: Dune Client, Using uv (recommended), Using pip, Example Usage, Quickstart: run_query, Further Examples, Get Latest Results, Paid Subscription Features, CRUD Operations, Setup, Makefile Shortcuts, Format, Lint & Types, Deployment

</details>

### dagster-managed-elements

Package for Managed elements with Dagster.

`pip install dagster-managed-elements` · installs (wheel) · licence: Apache-2.0 · rank 10762 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-managed-elements/)

### dbt-package-tools

Add your description here

`pip install dbt-package-tools` · does not install on CPython 3.14 · licence: not stated · rank 10790 · last release 2026-09-09 · [PyPI](https://pypi.org/project/dbt-package-tools/)

<details><summary>README extract</summary>

This directory contains code used by the `packages` option in the CLI that upgrades packages in a project to a Fusion-compatible version. The code is centered on four classes:
* DbtPackageFile: represents a file (currently packages.yml or dependencies.yml) that contains package dependencies for a project
* DbtPackage: represents a package that is ...

Sections: Package Management, How the CLI works, Scripts, TODO

</details>

### demisto-sdk

"A Python library for the Demisto SDK"

`pip install demisto-sdk` · installs (wheel) · licence: MIT License · rank 10796 · last release 2026-10-20 · [PyPI](https://pypi.org/project/demisto-sdk/)

<details><summary>README extract</summary>

The Demisto SDK is a Python library designed to aid the development process, both to validate entities being developed and to assist in the interaction between your development setup and Cortex XSOAR or Cortex XSIAM.

Requirements:

- Python 3.10, 3.11, 3.12, 3.13, or 3.14.
- git installed.
- A linux, mac or WSL2 machine. ...

Sections: Demisto SDK, Usage, Environment Variable Setup, For Cortex XSOAR 6.x Only, For Cortex XSIAM or Cortex XSOAR 8.x and above, CLI usage, Content path, Version Check, Run using Docker image, Commands, Logs, Customizable command configuration, Internet Connection, Docker Usage

</details>

### dnstwist

Domain name permutation engine for detecting homograph phishing attacks, typo squatting, and brand impersonation

`pip install dnstwist` · installs (wheel) · licence: Apache Software License · rank 10859 · last release 2025-01-30 · [PyPI](https://pypi.org/project/dnstwist/)

### datarobot-predict

DataRobot Prediction Library

`pip install datarobot-predict` · installs (wheel) · licence: Apache Software License · rank 10862 · last release 2025-12-24 · [PyPI](https://pypi.org/project/datarobot-predict/)

<details><summary>README extract</summary>

DataRobot Prediction Library is a Python library for making predictions using various prediction methods supported by DataRobot.
The intention is to provide a common interface for making predictions, making it easy to swap out the underlying implementation.

For more info, see the official documentation.

</details>

### datastar-py

Helper functions and classes for the Datastar library (https://data-star.dev/)

`pip install datastar-py` · installs (wheel) · licence: MIT · rank 10904 · last release 2026-09-27 · [PyPI](https://pypi.org/project/datastar-py/) · [docs](https://github.com/starfederation/datastar-python/blob/develop/README.md) · [source](https://github.com/starfederation/datastar-python)

<details><summary>README extract</summary>

The `datastar-py` package provides a Python SDK for working with Datastar.

Datastar sends responses back to the browser using SSE. This allows the backend to
send any number of events, from zero to infinity in response to a single request. ...

Example:
```python
import asyncio
from datetime import datetime

from datastar_py import ServerSentEventGenerator as SSE, attribute_generator as data
from datastar_py.quart import datastar_response, read_signals
from quart import Quart

app = Quart(name)

# Import frontend library via Content Distribution Network, create targets for Server Sent Events
...
```

Sections: Datastar Python SDK, Event Generation Helpers, Response Helpers, Response Decorator, Signal Helpers, Attribute Generation Helper, Action Generation Helper

</details>

### django-organizations

Group accounts for Django

`pip install django-organizations` · installs (wheel) · licence: BSD License · rank 10908 · last release 2026-07-03 · [PyPI](https://pypi.org/project/django-organizations/) · [docs](https://django-organizations.readthedocs.io/en/latest/) · [source](https://github.com/bennylope/django-organizations)

<details><summary>README extract</summary>

Separate individual user identity from accounts, subscriptions, etc..
Django Organizations adds user-managed, multi-user groups to your Django project.
Use Django Organizations whether your site needs organizations that function like
social groups or multi-user account objects to provide account and subscription
functionality beyond the individual ...

Example:
```python
>>> from organizations.utils import create_organization
>>> chris = User.objects.get(username="chris")
>>> soundgarden = create_organization(chris, "Soundgarden", org_user_defaults={'is_admin': True})
>>> soundgarden.is_member(chris)
True
>>> soundgarden.is_admin(chris)
True
>>> soundgarden.owner.organization_user
<OrganizationUser: Chris Cornell>
...
```

...

</details>

### django-read-only

Disable Django database writes.

`pip install django-read-only` · installs (wheel) · licence: MIT · rank 10909 · last release 2025-09-18 · [PyPI](https://pypi.org/project/django-read-only/) · [source](https://github.com/adamchainz/django-read-only)

<details><summary>README extract</summary>

Disable Django database writes.

Work smarter and faster with my book Boost Your Django DX which covers django-read-only, IPython, and many other tools.

Python 3.9 to 3.14 supported.

Django 4.2 to 6.0 supported.

Example:
```python
>>> import django_read_only
>>> django_read_only.enable_writes()
```

Sections: django-read-only, Requirements, Usage, Recommended Setup, IPython Extension, How it Works

</details>

### datetime-quarter

Simple and lightweight quarter support for python datetime

`pip install datetime-quarter` · installs (wheel) · licence: MIT License · rank 10920 · last release 2020-02-09 · [PyPI](https://pypi.org/project/datetime-quarter/)

<details><summary>README extract</summary>

Simple quarter support for python `datetime.date`

1. Install via pip (`pip install datetime-quarter`)
2. or via git (`git clone "
3. Check availability in your project like below

Example:
```python
from datequarter import DateQuarter

sample = DateQuarter(2019, 4)
print(sample)  # 2019 4Q
```

Sections: datetime-quarter, Setup, Operations, 1. Creation, 2. Adding or sub quarter, 3. Getting distance, 4. Comparison of `DateQuarter`, 5. Comparison of `datetime.date`, 6. Getting start and end date, 7. Iterate over containing date, 8. Iterate between `DateQuarter`

</details>

### dub

Python Client SDK Generated by Speakeasy

`pip install dub` · installs (wheel) · licence: not stated · rank 10923 · last release 2026-10-28 · [PyPI](https://pypi.org/project/dub/) · [source](https://github.com/dubinc/dub-python.git)

<details><summary>README extract</summary>

Learn more about the Dub.co Python SDK in the official documentation.

Dub API: Dub is the modern link attribution platform for short links, conversion tracking, and affiliate programs.

Example:
```python
# !/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
# "dub",
# ]
# ///

from dub import Dub

sdk = Dub(
  # SDK arguments
)

# Rest of script here...
```

Sections: Dub.co Python SDK, Summary, uv, PIP, Poetry, Shell and script usage with `uv`, SDK Example Usage, Example 1, Example 2, Available Resources and Operations, Analytics, Bounties, Commissions, Customers

</details>

### docutils-stubs

PEP 561 type stubs for docutils

`pip install docutils-stubs` · installs (wheel) · licence: The Unlicense (Unlicense) · rank 10968 · last release 2022-01-02 · [PyPI](https://pypi.org/project/docutils-stubs/)

### django-markdownify

Markdown template filter for Django.

`pip install django-markdownify` · installs (wheel) · licence: MIT · rank 10986 · last release 2026-05-18 · [PyPI](https://pypi.org/project/django-markdownify/)

<details><summary>README extract</summary>

Django Markdownify is a template filter to convert Markdown to HTML in Django. Markdown is converted to HTML and sanitized.

Read the full documentation on Read the docs or check out the package on pypi.

> [!WARNING]
> The old settings are removed in release 0.9.4! Please update to the new settings as soon as possible.

Sections: Django Markdownify - A Django Markdown filter, Usage, Example, Documentation

</details>

### dbt-coverage

One-stop-shop for docs and test coverage of dbt projects

`pip install dbt-coverage` · installs (wheel) · licence: MIT License · rank 11078 · last release 2026-10-07 · [PyPI](https://pypi.org/project/dbt-coverage/) · [docs](https://github.com/slidoapp/dbt-coverage) · [source](https://github.com/slidoapp/dbt-coverage)

<details><summary>README extract</summary>

_One-stop-shop for docs and test coverage of `dbt` projects._

Optimized for dbt 1.0, see full support matrix.

Features:
_`dbt-coverage` is to `dbt` what `coverage.py` and `interrogate` are to Python._

It is a single CLI tool which checks your `dbt` project for missing documentation and tests. ...

Sections: dbt-coverage, Why do I need something like this?, Demo, Usage, Compute, Markdown output with `--cov-format`, Custom run artifacts path with `--run-artifacts-dir`, Compare, Combined use-case, Related packages

</details>

### dbt-dremio

The Dremio adapter plugin for dbt

`pip install dbt-dremio` · installs (wheel) · licence: Apache Software License · rank 11080 · last release 2026-09-11 · [PyPI](https://pypi.org/project/dbt-dremio/)

<details><summary>README extract</summary>

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

- Dremio docs for our dbt adapter ...

Sections: Documentation, dbt-dremio version 1.11.0, Getting started

</details>

### dparse2

A parser for Python dependency files

`pip install dparse2` · installs (wheel) · licence: MIT License · rank 11141 · last release 2022-12-23 · [PyPI](https://pypi.org/project/dparse2/)

<details><summary>README extract</summary>

A parser for Python manifests and dependency files now at

Originally at

This is a maintained fork by some of the contributors since upstream stopped
updating this.

Example:
```python
from dparse2 import parse
from dparse2 import filetypes

content = """
South==1.0.1 --hash=sha256:abcdefghijklmno
pycrypto>=2.6
"""

df = parse(content, file_type=filetypes.requirements_txt)

print(df.json())

{
  "file_type": "requirements.txt",
  "content": "\nSouth==1.0.1 --hash=sha256:abcdefghijklmno\npycrypto>=2.6\n",
  "path": null,
...
```

Sections: Dependency Parser, Usage, 0.7.0, 0.6.1, 0.6.0, 0.5.1 (2020-04-26), 0.5.0 (2020-03-14), 0.4.1 (2018-04-06), 0.4.0 (2018-04-06), 0.3.0 (2018-03-01), 0.2.1 (2017-07-19), 0.2.0 (2017-07-19), 0.1.1 (2017-07-14), 0.1.0 (2017-07-11)

</details>

### django-authlib

Authentication utils for Django

`pip install django-authlib` · installs (wheel) · licence: MIT License · rank 11149 · last release 2026-10-28 · [PyPI](https://pypi.org/project/django-authlib/)

<details><summary>README extract</summary>

authlib is a collection of authentication utilities for implementing
passwordless authentication. This is achieved by either sending
cryptographically signed links by email, or by fetching the email
address from third party providers such as Google, Facebook and Twitter. ...

Example:
```python
from django.urls import path
from authlib import views
from authlib.facebook import FacebookOAuth2Client
from authlib.google import GoogleOAuth2Client
from authlib.microsoft import MicrosoftOAuth2Client
from authlib.twitter import TwitterOAuthClient

urlpatterns = [
    path("login/", views.login, name="login"),
    path(
...
```

...

</details>

### descriptastorus

Descriptor creation, storage and molecular file indexing

`pip install descriptastorus` · installs (wheel) · licence: not stated · rank 11159 · last release 2024-10-26 · [PyPI](https://pypi.org/project/descriptastorus/)

### demisto-py

"A Python library for the Demisto API"

`pip install demisto-py` · installs (wheel) · licence: Apache Software License · rank 11169 · last release 2026-05-11 · [PyPI](https://pypi.org/project/demisto-py/)

<details><summary>README extract</summary>

A Python library for the Demisto API.

Version 2.x is compatible with Demisto server version 4.5 and later.

Example:
```python
import demisto_client

# Also possible to set env variables: DEMISTO_API_KEY and DEMISTO_BASE_URL
api_key = 'YOUR_API_KEY'
host = '

api_instance = demisto_client.configure(base_url=host, api_key=api_key)
```

Sections: Demisto Client for Python, Demisto for Python Usage, 1. Get a Demisto API Key, 3. Create incidents, API Documentation, Troubleshooting, API Key, Dev Environment Setup, Running unit-tests using Pytest, Code Generation

</details>

### databaas-utils

Lakekeeper/Iceberg lakehouse access for Databaas: catalog, remote-signed object storage, and Airflow integration.

`pip install databaas-utils` · installs (wheel) · licence: Apache-2.0 · rank 11246 · last release 2026-10-08 · [PyPI](https://pypi.org/project/databaas-utils/)

<details><summary>README extract</summary>

Lakekeeper/Iceberg lakehouse access for Databaas: catalog, remote-signed object storage,
an Airflow integration, and user access from notebooks — in JupyterHub or on a laptop.

`databaas_utils.user` authenticates as the person running the code and picks how by
itself (`databaas_utils.notebook`, its former name, still works): ...

Example:
```python
from databaas_utils import LakehouseSettings, rest_catalog

settings = LakehouseSettings.from_profile()  # picks up the login from `databaas login`
catalog = rest_catalog(settings)
catalog.list_namespaces()
```

Sections: databaas-utils, Notebooks, Local (analyst) quickstart, Deploying DAGs, Documentation

</details>

### django-perf-rec

Keep detailed records of the performance of your Django code.

`pip install django-perf-rec` · installs (wheel) · licence: MIT · rank 11251 · last release 2025-09-18 · [PyPI](https://pypi.org/project/django-perf-rec/) · [source](https://github.com/adamchainz/django-perf-rec)

<details><summary>README extract</summary>

Keep detailed records of the performance of your Django code.

Note (2025-08-01):
My new package inline-snapshot-django is a faster and more convenient alternative to django-perf-rec.
As a consequence, django-perf-rec is now in maintenance mode, and will not receive significant new features. ...

Example:
```python
def test_home(self):
    with django_perf_rec.record():
        self.client.get("/")
```

Sections: django-perf-rec, Requirements, API, `TestCaseMixin`, `get_perf_path(file_path)`, `get_record_name(test_name, class_name=None)`, Settings, `HIDE_COLUMNS`, `MODE`, Usage in Pytest

</details>

### dj-datatables-view

Django datatables view fork from django-datatables-view

`pip install dj-datatables-view` · installs (wheel) · licence: MIT License · rank 11272 · last release 2022-02-24 · [PyPI](https://pypi.org/project/dj-datatables-view/) · [source](https://gitlab.com/longbowou/django-datatables-view)

<details><summary>README extract</summary>

Fork from django-datatables-view
Compatible with Django 2+ 3+ 4+

dj-datatables-view is a base view for handling server side
processing for the awesome datatables 1.9.*, 1.10.*, 1.11.*

dj-datatables-view simplifies handling of sorting, filtering and
creating JSON output, as defined at:

Example:
```python
from dj-datatables-view.base_datatable_view import BaseDatatableView
from django.utils.html import escape

class OrderListJson(BaseDatatableView):
    order_columns = ['number', 'user', 'state']

    def get_initial_queryset(self):
        # return queryset used as base for futher sorting/filtering
...
```

Sections: About, Usage, 2. Edit views.py, 3. Edit urls.py, 4. Define HTML + JavaScript, Another example of views.py customisation, Yet another example of views.py customisation

</details>

### dagster-celery-k8s

A Dagster integration for celery-k8s-executor

`pip install dagster-celery-k8s` · installs (wheel) · licence: Apache-2.0 · rank 11281 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-celery-k8s/)

### deeplake

Data Lake for Multi-Modal AI Search

`pip install deeplake` · does not install on CPython 3.14 · licence: not stated · rank 11297 · last release 2026-08-25 · [PyPI](https://pypi.org/project/deeplake/) · [docs](https://docs.deeplake.ai/) · [source](https://github.com/activeloopai/deeplake)

<details><summary>README extract</summary>

Get Started •
 API Reference •
 LangChain & VectorDBs Course •
 Blog •
 Whitepaper •
 Slack •
 Twitter

Deep Lake is a Database for AI powered by a storage format optimized for deep-learning applications. Deep Lake can be used for:

1. Storing and searching data plus vectors while building LLM applications
2. ...

Sections: Deep Lake: Database for AI, Docs •, What is Deep Lake?, Deep Lake includes the following features, 🧠 Deep Lake Code Examples by Application, Vector Store Applications, - Vector Store Quickstart, - Vector Store Tutorials, - LangChain Integration, - LlamaIndex Integration, - Image Similarity Search with Deep Lake, Deep Learning Applications, - Deep Learning Quickstart, - Tutorials for Training Models

</details>

### django-navhelper

Django template tags designed to help the navigation rendering

`pip install django-navhelper` · installs (wheel) · licence: MIT · rank 11309 · last release 2023-06-19 · [PyPI](https://pypi.org/project/django-navhelper/)

<details><summary>README extract</summary>

Django template tags to add active class on navigation menus

- Django 4.2
- Python 3.10

Sections: Django navhelper, Prerequisites, Template tags, navactive, renavactive, Settings, Run test suite

</details>

### dataclass-csv

Map CSV data into dataclasses

`pip install dataclass-csv` · installs (wheel) · licence: BSD License · rank 11313 · last release 2026-02-01 · [PyPI](https://pypi.org/project/dataclass-csv/)

<details><summary>README extract</summary>

Dataclass CSV makes working with CSV files easier and much better than working with Dicts. It uses Python's Dataclasses to store data of every row on the CSV file and also uses type annotations which enables proper type checking and validation.

- Use `dataclasses` instead of dictionaries to represent the rows in the CSV file. ...

Example:
```python
from dataclasses import dataclass

from dataclass_csv import DataclassReader
```

Sections: Dataclass CSV, Main features, Thanks, Getting started, Using the DataclassReader, Error handling, Default values, Mapping dataclass fields to columns, Fields metadata, Handling values with empty spaces, User-defined types, Using the DataclassWriter, Modifying the CSV header

</details>

### dbt-bouncer

Configure and enforce conventions for your dbt project.

`pip install dbt-bouncer` · installs (wheel) · licence: MIT · rank 11314 · last release 2026-11-03 · [PyPI](https://pypi.org/project/dbt-bouncer/) · [docs](https://godatadriven.github.io/dbt-bouncer/) · [source](https://github.com/godatadriven/dbt-bouncer)

<details><summary>README extract</summary>

All documentation can be found on `dbt-bouncer` documentation website.

Features:
- Presets — start with a bundled `minimal`, `standard` or `strict` config, with no config file to write. Run `dbt-bouncer run --preset strict`.
- Baselines — adopt strict checks on an existing project and fail only on *new* failures. ...

Sections: dbt-bouncer, Configure and enforce conventions for your dbt project., Documentation, Aims, Features, TLDR

</details>

### django-slack

Provides easy-to-use integration between Django projects and the Slack group chat and IM tool.

`pip install django-slack` · installs (wheel) · licence: BSD-3-Clause · rank 11327 · last release 2023-03-02 · [PyPI](https://pypi.org/project/django-slack/)

### dbt-core-interface

Dbt Core Interface

`pip install dbt-core-interface` · does not install on CPython 3.14 · licence: MIT · rank 11368 · last release 2026-01-11 · [PyPI](https://pypi.org/project/dbt-core-interface/) · [docs](https://dbt-core-interface.readthedocs.io) · [source](https://github.com/z3z1ma/dbt-core-interface)

<details><summary>README extract</summary>

Lightweight, thread-safe, multi-project Python interface to dbt-core

Built with the tools and technologies:

Features:
`dbt-core-interface` is a lightweight, high-performance Python interface for working directly with `dbt-core` (v1.8+). It allows developers to manage and run dbt projects entirely in memory using an intuitive Python API—enabling runtime SQL ...

Example:
```python
from dbt_core_interface.client import DbtInterfaceClient, ServerError

client = DbtInterfaceClient(
    project_dir="/path/to/project",
    profiles_dir="/path/to/profiles.yml",
    target="dev",
    base_url="
    timeout=(5.0, 15.0)
)

# Health & heartbeat
print(client.health_check())  # {'status': 'ok', ...}
...
```

...

</details>

### dvc-azure

azure plugin for dvc

`pip install dvc-azure` · installs (wheel) · licence: Apache-2.0 · rank 11376 · last release 2026-06-10 · [PyPI](https://pypi.org/project/dvc-azure/) · [docs](https://dvc.org/doc) · [source](https://github.com/iterative/dvc-azure)

### duckduckgo-mcp-server

MCP Server for searching via DuckDuckGo

`pip install duckduckgo-mcp-server` · installs (wheel) · licence: MIT License · rank 11397 · last release 2026-09-04 · [PyPI](https://pypi.org/project/duckduckgo-mcp-server/)

<details><summary>README extract</summary>

A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing.

Features:
- Web Search: Search DuckDuckGo with advanced rate limiting and result formatting
- Content Fetching: Retrieve and parse webpage content with intelligent text extraction ...

Example:
```python
async def search(query: str, max_results: int = 10, region: str = "") -> str
```

Sections: DuckDuckGo Search MCP Server, Quick Start, Features, Usage, Running with Claude Desktop, Running with Claude Code, Running with SSE or Streamable HTTP, Running behind a reverse proxy or in Docker, Running behind a TLS-intercepting proxy, Backends (bypassing bot detection), Search backend, Available Tools, 1. Search Tool, 2. Content Fetching Tool

</details>

### django-wkhtmltopdf

Converts HTML to PDF using wkhtmltopdf.

`pip install django-wkhtmltopdf` · installs (wheel) · licence: MIT License · rank 11403 · last release 2022-02-24 · [PyPI](https://pypi.org/project/django-wkhtmltopdf/)

<details><summary>README extract</summary>

Provides Django views to wrap the HTML to PDF conversion of the wkhtmltopdf binary.

Install the wkhtmltopdf static binary.

This requires libfontconfig (on Ubuntu: `sudo aptitude install libfontconfig`).

Python 2.6+ and 3.3+ are supported.

Sections: django-wkhtmltopdf, Converts HTML to PDF, Requirements, Documentation

</details>

### django-js-reverse

Javascript url handling for Django that doesn't hurt.

`pip install django-js-reverse` · installs (wheel) · licence: MIT · rank 11404 · last release 2026-05-22 · [PyPI](https://pypi.org/project/django-js-reverse/) · [source](https://github.com/vintasoftware/django-js-reverse)

<details><summary>README extract</summary>

Javascript url handling for Django that doesn’t hurt.

This package is now maintained by Vinta Software but it was originally created by @ierror. Many thanks to you, Bernhard.

Features:
Django JS Reverse is a small django app that makes url handling of
named urls in javascript easy and non-annoying..

For example you can retrieve a named url:

urls.py:

in javascript like:

Result:

Example:
```python
from django.urls import path
from django_js_reverse.views import urls_json

urlpatterns = [
    path("jsreverse.json", urls_json, name="js_reverse"),
]
```

...

</details>

### docvortex

A fast, multi-format document parsing and conversion engine

`pip install docvortex` · installs (wheel) · licence: MIT AND Apache-2.0 AND BSD-3-Clause · rank 11429 · last release 2026-11-07 · [PyPI](https://pypi.org/project/docvortex/) · [source](https://github.com/myhloli/DocVortex)

<details><summary>README extract</summary>

Native document parsing. One structure, many outputs.

English · 简体中文

Performance · Quick start · Formats · Documentation

DocVortex is a standalone Python engine for parsing and converting documents.
It reads native text and document structure into a unified representation,
then exports the result in the formats your workflow needs. ...

Example:
```python
import docvortex

result = docvortex.parse("report.pdf")
result.export("output/report.md", output_format="markdown")
result.export("output/report.docx", output_format="docx")
```

Sections: DocVortex, Documents in. Possibilities out., PDF performance, Quick start, Command line, Python, Native inputs · 20 formats, Outputs · 7 formats, Save now, export later, Choose the right workflow, Documentation

</details>

### drf-access-policy

Declarative access policies/permissions modeled after AWS' IAM policies.

`pip install drf-access-policy` · installs from source (sdist only) · licence: MIT License · rank 11439 · last release 2023-03-02 · [PyPI](https://pypi.org/project/drf-access-policy/)

<details><summary>README extract</summary>

This project brings a declaritive, organized approach to managing access control in Django REST Framework projects. Each ViewSet or function-based view can be assigned an explicit policy for the exposed resource(s). ...

Example:
```python
class ArticleAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": "*",
            "effect": "allow"
        },
        {
            "action": ["publish", "unpublish"],
            "principal": ["group:editor"],
            "effect": "allow"
        }
    ]
```

...

</details>

### deepfilterlib

(no summary)

`pip install deepfilterlib` · installs from source (sdist only) · licence: not stated · rank 11480 · last release 2023-08-31 · [PyPI](https://pypi.org/project/deepfilterlib/)

### django-admin-env-notice

Visually distinguish environments in Django Admin

`pip install django-admin-env-notice` · installs (wheel) · licence: BSD License · rank 11487 · last release 2024-10-19 · [PyPI](https://pypi.org/project/django-admin-env-notice/)

<details><summary>README extract</summary>

Visually distinguish environments in Django Admin. Based on great advice from post: 5 ways to make Django Admin safer by hakibenita.

- Python 2.7, 3.4+
- Django 1.9+

Sections: django-admin-env-notice, Requirements, Quickstart, Screenshots, Running Tests

</details>

### djfernet

(no summary)

`pip install djfernet` · installs from source (sdist only) · licence: MIT · rank 11496 · last release 2022-02-13 · [PyPI](https://pypi.org/project/djfernet/)

<details><summary>README extract</summary>

Maintained fork of github.com/orcasgit/django-fernet-fields used by
yourlabs.io/oss/djwebdapp

Fernet symmetric encryption for Django model fields, using the
cryptography library.

`djfernet` supports Django 4.0 and later on Python 3. ...

Sections: djfernet, Getting Help

</details>

### dbt-sl-sdk

A client for dbt's Semantic Layer

`pip install dbt-sl-sdk` · does not install on CPython 3.14 · licence: not stated · rank 11527 · last release 2026-05-27 · [PyPI](https://pypi.org/project/dbt-sl-sdk/)

<details><summary>README extract</summary>

A library for easily accessing dbt's Semantic Layer via Python.

Example:
```python
from dbtsl import SemanticLayerClient

client = SemanticLayerClient(
    environment_id=123,
    auth_token="<your-semantic-layer-api-token>",
    host="semantic-layer.cloud.getdbt.com",
)

# query the first metric by `metric_time`
def main():
    with client.session():
        metrics = client.metrics()
        table = client.query(
...
```

Sections: dbt Semantic Layer SDK for Python, Usage, asyncio, Integrating with dataframe libraries, Lazy loading, More examples, Disabling telemetry

</details>

### django-clickhouse-backend

Django clickHouse database backend

`pip install django-clickhouse-backend` · installs (wheel) · licence: MIT License · rank 11572 · last release 2026-08-09 · [PyPI](https://pypi.org/project/django-clickhouse-backend/)

<details><summary>README extract</summary>

Django clickhouse backend is a django database backend for
clickhouse database. This project allows using django ORM to interact with
clickhouse, the goal of the project is to operate clickhouse like operating mysql, postgresql in django.

Thanks to clickhouse driver, django clickhouse backend use it as DBAPI. ...

Example:
```python
# dbrouters.py
from clickhouse_backend.models import ClickhouseModel

def get_subclasses(class):
    classes = class.subclasses()

    index = 0
    while index < len(classes):
        classes.extend(classes[index].subclasses())
        index += 1

    return list(set(classes))

class ClickHouseRouter:
    def init(self):
...
```

...

</details>

### datarobot-moderations

DataRobot Monitoring and Moderation framework

`pip install datarobot-moderations` · does not install on CPython 3.14 · licence: DataRobot Tool and Utility Agreement · rank 11631 · last release 2026-10-27 · [PyPI](https://pypi.org/project/datarobot-moderations/)

<details><summary>README extract</summary>

This library enforces the intervention in the prompt and response texts as per the
guard configuration set by the user.

The library accepts the guard configuration in the yaml format and the input prompts
and outputs the dataframe with the details like:
- should the prompt be blocked
- should the completion be blocked ...

Example:
```python
import json
from datarobot_dome.api import ModerationPipeline

pipeline = ModerationPipeline.from_yaml("docs/examples/agent_goal_accuracy_config.yaml")

task = "Book a flight from NYC to London"

# chat_completion is the object returned by the DataRobot agent SDK.
# `pipeline_interactions` is attached when the agent has tool calls / multi-turn
...
```

...

</details>

### dgl

Deep Graph Library

`pip install dgl` · does not install on CPython 3.14 · licence: Apache Software License · rank 11700 · last release 2024-05-13 · [PyPI](https://pypi.org/project/dgl/)

### django-nine

Version checking library.

`pip install django-nine` · installs (wheel) · licence: GNU General Public License v2 (GPLv2); GNU Lesser General Public License v2 or l · rank 11788 · last release 2022-12-05 · [PyPI](https://pypi.org/project/django-nine/) · [docs](https://django-nine.readthedocs.io/) · [source](https://github.com/barseghyanartur/django-nine)

_README extract left out: share-alike licence._

### django-reverse-admin

(no summary)

`pip install django-reverse-admin` · installs from source (sdist only) · licence: BSD License · rank 11802 · last release 2021-03-27 · [PyPI](https://pypi.org/project/django-reverse-admin/)

<details><summary>README extract</summary>

Module that makes django admin handle OneToOneFields in a better way. A common use case for one-to-one relationships is to "embed" a model inside another one. For example, a Person may have multiple foreign keys pointing to an Address entity, one home address, one business address and so on. ...

Example:
```python
from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

class Person(models.Model):
    name = models.CharField(max_length=255)
...
```

Sections: Django Reverse Admin, Requirements, Usage, Demo, Contribtion, Packaging

</details>

### dbt-loom

A dbt-core plugin to import public nodes in multi-project deployments.

`pip install dbt-loom` · installs (wheel) · licence: not stated · rank 11804 · last release 2026-09-06 · [PyPI](https://pypi.org/project/dbt-loom/)

<details><summary>README extract</summary>

dbt-loom is a dbt Core plugin that weaves together multi-project deployments. dbt-loom works by fetching public model definitions from your dbt artifacts, and injecting those models into your dbt project.

dbt-loom currently supports obtaining model definitions from:

- Local manifest files
- Remote manifest files via http(s) ...

Sections: dbt-loom, Getting Started, How does it work?, Advanced Features, Configuring artifact sources, Object storage, `dbt-core` hosting providers, Data Warehouses, Using environment variables, Example, Gzipped files, Exclude nested packages, Include only specific packages, Optional manifests

</details>

### deepteam

The LLM Red Teaming Framework

`pip install deepteam` · does not install on CPython 3.14 · licence: Apache Software License · rank 11810 · last release 2026-10-16 · [PyPI](https://pypi.org/project/deepteam/) · [docs](https://trydeepteam.com) · [source](https://github.com/confident-ai/deepteam)

<details><summary>README extract</summary>

Documentation |
 Vulnerabilities, Attacks, and Features |
 Getting Started |
 Confident AI

 Deutsch |
 Español |
 français |
 日本語 |
 한국어 |
 Português |
 Русский |

DeepTeam is a simple-to-use, open-source red teaming framework for LLM systems. Think of it as penetration testing, but for LLMs. ...

Example:
```python
from deepteam import red_team
from deepteam.vulnerabilities import Bias
from deepteam.attacks.single_turn import PromptInjection

async def model_callback(input: str) -> str:
    # Replace this with your LLM application
    return f"I'm sorry but I can't answer this: {input}"

risk_assessment = red_team(
    model_callback=model_callback,
...
```

...

</details>

### django-cid

Correlation IDs in Django for debugging requests

`pip install django-cid` · installs (wheel) · licence: BSD License · rank 11827 · last release 2024-05-14 · [PyPI](https://pypi.org/project/django-cid/) · [docs](https://django-correlation-id.readthedocs.io/) · [source](https://github.com/Polyconseil/django-cid)

<details><summary>README extract</summary>

Logging is important. Anyone who has had a call at 3am to say the site
is down knows this. Without quality logging it is almost impossible to
work out what on earth is happening.

The more you log, the harder it is to track down exactly what the
effects of a particular request are. Enter Django Correlation ID. ...

</details>

### django-settings-export

This Django app allows you to export certain settings to your templates.

`pip install django-settings-export` · installs from source (sdist only) · licence: BSD · rank 11884 · last release 2016-11-06 · [PyPI](https://pypi.org/project/django-settings-export/)

<details><summary>README extract</summary>

Often it is needed to make some of your Django project's settings
accessible from within templates. This app provides a simple mechanism
for doing just that.

Principles:

* *Explicit is better than implicit:* Only explicitly listed
 settings keys are exported to templates. ...

Sections: `django-settings-export`, Usage, Changing the `settings` variable name, Exceptions, Demo & Tests, Contact

</details>

### dagster-async-executor

Async Support for Dagster

`pip install dagster-async-executor` · installs (wheel) · licence: not stated · rank 11929 · last release 2026-06-29 · [PyPI](https://pypi.org/project/dagster-async-executor/)

<details><summary>README extract</summary>

An executor for Dagster that adds native `asyncio` support for ops and assets.

`dagster-async-executor` lets you:

- Run `async def` ops without manually managing event loops or thread pools.
- Mix sync and async ops in the same job.
- Use dynamic / fan-out graphs with async upstream and downstream dependencies. ...

Example:
```python
import anyio
import dagster as dg
from dagster_async_executor import async_executor

NUM_FANOUTS = 300
SLEEP_SECONDS = 3

@dg.op(out=dg.DynamicOut())
async def create_dynamic_outputs():
    """Creates a dynamic number of outputs."""
    for i in range(NUM_FANOUTS):
        yield dg.DynamicOutput(value=f"item{i}", mapping_key=f"key{i}")

@dg.op
...
```

...

</details>

### django-s3-storage

Django Amazon S3 file storage.

`pip install django-s3-storage` · installs (wheel) · licence: BSD License · rank 11950 · last release 2023-11-04 · [PyPI](https://pypi.org/project/django-s3-storage/)

### dbnomics

DBnomics Python client

`pip install dbnomics` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 11996 · last release 2025-06-18 · [PyPI](https://pypi.org/project/dbnomics/)

_README extract left out: share-alike licence._

### django-rusty-templates-agentic

An agentic fork of Django Rusty Templates with a compatible Python API

`pip install django-rusty-templates-agentic` · installs (wheel) · licence: not stated · rank 12001 · last release 2026-11-08 · [PyPI](https://pypi.org/project/django-rusty-templates-agentic/) · [source](https://github.com/jefftriplett/django-rusty-templates-agentic)

<details><summary>README extract</summary>

Django Rusty Templates (Agentic) is a fork of Lily's Django Rusty Templates library, an experimental reimplementation of Django's templating language in Rust. This fork began as an agentic attempt to try out the idea, exploring compatibility, performance, and shared server/browser templates. ...

Example:
```python
@register.tag("card")
def compile_card(parser, token):
    body = parser.parse(("endcard",))
    parser.delete_first_token()
    return CardNode(body)

compile_card.rusty_isolated_compiler = True
```

Sections: Django Rusty Templates (Agentic), Goals, Versioning, Usage, What is ported, Django contrib apps, WebAssembly for JavaScript clients, Benchmarks, Inspecting templates, Isolating custom tag compilers

</details>

### devicetree

Python libraries for devicetree

`pip install devicetree` · installs (wheel) · licence: Apache Software License · rank 12081 · last release 2022-04-27 · [PyPI](https://pypi.org/project/devicetree/)

<details><summary>README extract</summary>

This is just a placeholder for moving Zephyr's devicetree libraries
to PyPI.

</details>

### djangorestframework-guardian

django-guardian support for Django REST Framework

`pip install djangorestframework-guardian` · installs (wheel) · licence: BSD-3-Clause · rank 12157 · last release 2025-07-01 · [PyPI](https://pypi.org/project/djangorestframework-guardian/) · [source](https://github.com/rpkilby/django-rest-framework-guardian)

<details><summary>README extract</summary>

django-rest-framework-guardian provides django-guardian integrations for Django REST Framework.

Example:
```python
from rest_framework import permissions

class CustomObjectPermissions(permissions.DjangoObjectPermissions):
    """
    Similar to `DjangoObjectPermissions`, but adding 'view' permissions.
    """
    perms_map = {
        'GET': ['%(app_label)s.view%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view%(model_name)s'],
...
```

Sections: django-rest-framework-guardian, ObjectPermissionsFilter, ObjectPermissionsAssignmentMixin

</details>

### drf-dynamic-fields

Dynamically return subset of Django REST Framework serializer fields

`pip install drf-dynamic-fields` · installs (wheel) · licence: MIT License · rank 12228 · last release 2022-04-05 · [PyPI](https://pypi.org/project/drf-dynamic-fields/)

<details><summary>README extract</summary>

This package provides a mixin that allows the user to dynamically select only a
subset of fields per resource.

Official version support:

- Django 2.2 LTS, 3.2 LTS, 4.0
- Supported REST Framework versions: 3.8, 3.9
- Python 3.7+

This library is about filtering fields based on individual requests. ...

Features:
Example serializer:

A regular request returns all fields:

`GET /identities`

A query with the `fields` parameter on the other hand returns only a subset of
the fields:

`GET /identities/?fields=id,data` ...

Example:
```python
from drf_dynamic_fields import DynamicFieldsMixin

class IdentitySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Identity
        fields = ('id', 'url', 'type', 'data')
```

...

</details>

### dtaidistance

Distance measures for time series (Dynamic Time Warping, fast C implementation)

`pip install dtaidistance` · installs (wheel) · licence: Apache-2.0 · rank 12267 · last release 2026-09-11 · [PyPI](https://pypi.org/project/dtaidistance/) · [docs](https://http://dtaidistance.readthedocs.io) · [source](https://github.com/wannesm/dtaidistance)

<details><summary>README extract</summary>

Library for time series distances (e.g. Dynamic Time Warping) used in the
DTAI Research Group. The library offers a pure
Python implementation and a fast implementation in C. The C implementation
has only Cython as a dependency. It is compatible with Numpy and Pandas and
implemented such that unnecessary data copy operations are avoided. ...

Sections: Time Series Distances, Citing this work, Usage, Dynamic Time Warping (DTW) Distance Measure, DTW Distance Measure Between Two Series, Dynamic Subsequence Warping to explain (dis)similarities, DTW Distance Measure all warping paths, DTW Distance Measures Between Set of Series, Clustering, Subsequence search, Motif Discovery, Dependencies, Contact, References

</details>

### django-dbconn-retry

Patch Django to retry a database connection first before failing.

`pip install django-dbconn-retry` · installs (wheel) · licence: BSD-3-Clause · rank 12279 · last release 2026-10-30 · [PyPI](https://pypi.org/project/django-dbconn-retry/)

<details><summary>README extract</summary>

This library monkeypatches `django.db.backends.base.BaseDatabaseWrapper` so
that when a database operation fails because the underlying TCP connection was
already closed, it first tries to reconnect, instead of immediately raising
an `OperationException`.

Features:
I use HAProxy as a load-balancer in front of my PostgreSQL databases all
the time, sometimes in addition to `pgbouncer`. Even though you can mostly
prevent surprises by enabling TCP keep-alive packets through tcpka,
clitcpka and srvtcpka, I still ...

Sections: Django Database Connection Autoreconnect, Why is this useful?, Signals, Settings

</details>

### django-sqids

Non-intrusive sqids library for Django

`pip install django-sqids` · installs (wheel) · licence: MIT License · rank 12321 · last release 2025-07-09 · [PyPI](https://pypi.org/project/django-sqids/) · [source](https://github.com/julianwachholz/django-sqids)

<details><summary>README extract</summary>

django-sqids is a simple and non-intrusive sqids library for Django. It acts as a model field, but it does not touch the database or change the model.

The project was forked from django-hashids to provide the same functionality with the newer Sqids library.

Features:
- Proxy the internal model `pk` field without storing the value in the database.
- Allows lookups and filtering by sqid string.
- Can be used as sort key.
- Allows specifying a min_length and alphabet globally. ...

Example:
```python
from django_sqids import SqidsField

class TestModel(Model):
    sqid = SqidsField(real_field_name="id")
```

Sections: Django Sqids, Features, Usage, Examples, Using with URLs, Using with Django Admin, Config, Where did the Salt go?

</details>

### dlt-meta

DLT-META Framework (Compatibility wrapper - please migrate to databricks-labs-sdp-meta)

`pip install dlt-meta` · does not install on CPython 3.14 · licence: Databricks License · rank 12335 · last release 2026-08-31 · [PyPI](https://pypi.org/project/dlt-meta/) · [docs](https://databrickslabs.github.io/sdp-meta/) · [source](https://github.com/databrickslabs/sdp-meta)

<details><summary>README extract</summary>

DEPRECATED: This package is a compatibility wrapper for
databricks-labs-sdp-meta
(DLT-META is now SDP-META). Installing it pulls in the new package and keeps
existing `dlt_meta` / `src.*` imports working unchanged.

Replace:

With:

And migrate imports when convenient:

All functionality is identical. ...

Example:
```python
# old (still works via this wrapper)
from src.dataflow_pipeline import DataflowPipeline
# new
from databricks.labs.sdp_meta.dataflow_pipeline import DataflowPipeline
```

Sections: DLT-META Compatibility Package, Migration

</details>

### durations

UNKNOWN

`pip install durations` · installs from source (sdist only) · licence: MIT · rank 12348 · last release 2014-01-10 · [PyPI](https://pypi.org/project/durations/)

### django-cprofile-middleware

Easily add cProfile profiling to django views.

`pip install django-cprofile-middleware` · installs from source (sdist only) · licence: MIT · rank 12407 · last release 2020-02-20 · [PyPI](https://pypi.org/project/django-cprofile-middleware/)

<details><summary>README extract</summary>

[![pypi-version]][pypi]

This is a simple profiling middleware for Django applications. I wrote it because I got tired of printing "start" "stop" "stop 2" in my programs to find the bottlenecks.

I found a simple example on @dcramer's slideshare and modified it to support sorting.

Sections: django-cprofile-middleware, Running & Sorting Results, Enjoy!

</details>

### dagster-sling

Package for performing ETL/ELT tasks with Sling in Dagster.

`pip install dagster-sling` · installs (wheel) · licence: Apache-2.0 · rank 12420 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-sling/)

### dagster-prometheus

A Dagster integration for prometheus

`pip install dagster-prometheus` · installs (wheel) · licence: Apache-2.0 · rank 12423 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-prometheus/)

### django-role-permissions

A django app for role based permissions.

`pip install django-role-permissions` · installs (wheel) · licence: MIT License · rank 12427 · last release 2023-06-09 · [PyPI](https://pypi.org/project/django-role-permissions/)

### docker-squash

Docker layer squashing tool

`pip install docker-squash` · installs from source (sdist only) · licence: MIT · rank 12439 · last release 2024-11-13 · [PyPI](https://pypi.org/project/docker-squash/)

<details><summary>README extract</summary>

Docker creates many layers while building the image. Sometimes it's not necessary or desireable
to have them in the image. For example a Dockerfile `ADD` instruction creates a single layer
with files you want to make available in the image. ...

Features:
- Can squash last n layers from an image
- Can squash from a selected layer to the end (not always possible, depends on the image)
- Support for Docker 1.9 or newer (older releases may run perfectly fine too, try it!) ...

Sections: `docker-squash`, The problem, Features, Usage, Examples

</details>

### django-fake-model

Simple library for creating fake models in the unit tests.

`pip install django-fake-model` · installs (wheel) · licence: BSD License · rank 12464 · last release 2016-02-08 · [PyPI](https://pypi.org/project/django-fake-model/)

<details><summary>README extract</summary>

Simple library for creating fake models in the unit tests.

This simple library allows to create fake models in your test without migrations, test apps and test tables in your base. All tables that you need will created/removed during the test.

Example:
```python
from django_fake_model import models as f
from django.db import models
from django.test import TestCase, TransactionTestCase

class MyFakeModel(f.FakeModel):

    name = models.CharField(max_length=100)

@MyFakeModel.fake_me
class MyFakeModelTests(TestCase):

    def test_create_model(self):
        MyFakeModel.objects.create(name='123')
...
```

...

</details>

### dol

Base builtin tools make and transform data object layers (dols).

`pip install dol` · installs (wheel) · licence: Apache-2.0 · rank 12502 · last release 2026-11-03 · [PyPI](https://pypi.org/project/dol/)

<details><summary>README extract</summary>

Base builtin tools make and transform data object layers (dols).

The main idea comes in many names such as
Data Access Object (DAO),
Repository Pattern,
Hexagonal architecture, or ports and adapters architecture
for data. ...

Features:
- because it's short
- because it's cute
- because it reminds one of "russian dolls" (one way to think of wrappers)
- because we can come up with an acronym the contains "Data Object" in it.

Example:
```python
import pickle

src_backend = {
    "file_1.pkl": pickle.dumps([["A", "B", "C"], ["one", "two", "three"]]),
    "file_2.pkl": pickle.dumps([["apple", "pie"], ["one", "two"], ["hot", "cold"]]),
}
targ_backend = dict()
```

...

</details>

### dict-hash

Python package to hash dictionaries using default hash, md5, sha256 and more.

`pip install dict-hash` · installs from source (sdist only) · licence: MIT License · rank 12517 · last release 2025-11-10 · [PyPI](https://pypi.org/project/dict-hash/)

<details><summary>README extract</summary>

Python package to hash dictionaries using both default hash and sha256.
It comes with full support for hashing Pandas & Polars DataFrame/Series objects, Numba objects and Numpy arrays.
It supports both objects from Pandas 1.x and 2.x and Numpy 1.x and 2.x.

Furthermore, the library supports objects that can be recursively hashed. ...

Features:
In Python, dictionaries just aren't hashable. This is because they are mutable objects, and as such, they cannot be hashed.
If you were to try and run `hash({})`, you would get a `TypeError` exception.

Example:
```python
from dict_hash import dict_hash
from random_dict import random_dict
from random import randint

d = random_dict(randint(1, 10), randint(1, 10))
my_hash = dict_hash(d)
```

...

</details>

### django-watson

Full-text multi-table search application for Django. Easy to install and use, with good performance.

`pip install django-watson` · installs (wheel) · licence: BSD License · rank 12538 · last release 2023-01-14 · [PyPI](https://pypi.org/project/django-watson/)

<details><summary>README extract</summary>

django-watson is a fast multi-model full-text search plugin for Django.

It is easy to install and use, and provides high quality search results.

Features

* Search across multiple models.
* Order results by relevance.
* No need to install additional third-party modules or services.
* Fast and scaleable enough for most use cases. ...

</details>

### deflate-dict

Package to deflate and inflate dictionaries.

`pip install deflate-dict` · installs from source (sdist only) · licence: MIT License · rank 12592 · last release 2024-10-26 · [PyPI](https://pypi.org/project/deflate-dict/)

<details><summary>README extract</summary>

Python package to deflate 🌵 and re-inflate 🎈 nested dictionaries.

Example:
```python
from deflate_dict import deflate
D = {
    "a": [
        {
            "b": (0, 1, 2)
        },
        {
            "c": [1, 2, 3]
        }
    ]
}
result = deflate(D, sep="_")

# {'str(a)_listIndex(0)_str(b)': (0, 1, 2), 'str(a)_listIndex(1)_str(c)': [1, 2, 3]}
```

Sections: 🎈🌵 Deflate Dict, Deflating a dictionary, Inflate a dictionary, Handling and restoring mixed types

</details>

### do-mpc

(no summary)

`pip install do-mpc` · installs (wheel) · licence: GNU Lesser General Public License version 3 · rank 12619 · last release 2026-09-03 · [PyPI](https://pypi.org/project/do-mpc/)

_README extract left out: share-alike licence._

### dataengine

General purpose data engineering python package.

`pip install dataengine` · installs (wheel) · licence: not stated · rank 12636 · last release 2025-04-17 · [PyPI](https://pypi.org/project/dataengine/)

<details><summary>README extract</summary>

Data Engine is a general purpose python package for data engineering that leverages python, pandas, Apache Spark, and public cloud services.

Sections: Data Engine, Usage Guide, Adding to Your Project's Requirements, How to use the package, Setup Instructions

</details>

### dbt-oracle

dbt (data build tool) adapter for Oracle Autonomous Database

`pip install dbt-oracle` · installs (wheel) · licence: Apache-2.0 · rank 12738 · last release 2026-08-06 · [PyPI](https://pypi.org/project/dbt-oracle/) · [docs](https://docs.getdbt.com/reference/warehouse-profiles/oracle-profile) · [source](https://github.com/oracle/dbt-oracle)

<details><summary>README extract</summary>

[][4]

`dbt-oracle` implements dbt (data build tool) functionalities for Oracle Autonomous Database.

> Prior to version 1.0.0, dbt-oracle was created and maintained by Indicium on their GitHub repo. Contributors in this repo are credited for laying the groundwork and maintaining the adapter till version 0.4.3. ...

Sections: dbt-oracle, Documentation, Help, Sample project

</details>

### dagster-pagerduty

Package for pagerduty Dagster framework components.

`pip install dagster-pagerduty` · installs (wheel) · licence: Apache-2.0 · rank 12753 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-pagerduty/)

### docstring-inheritance

Avoid writing and maintaining duplicated docstrings.

`pip install docstring-inheritance` · installs (wheel) · licence: MIT · rank 12771 · last release 2025-12-11 · [PyPI](https://pypi.org/project/docstring-inheritance/) · [docs](https://antoined.github.io/docstring-inheritance) · [source](https://github.com/AntoineD/docstring-inheritance)

<details><summary>README extract</summary>

<!--
 Copyright 2021 Antoine DECHAUME

 This work is licensed under the Creative Commons Attribution 4.0
 International License. To view a copy of this license, visit
 or send a letter to Creative
 Commons, PO Box 1866, Mountain View, CA 94042, USA. ...

Features:
- By default, the metaclasses and functions in this package do nothing, so they have virtually no performance impact.
- When building documentation, enable the inheritance of the docstrings by defining the environment variable ...

Example:
```python
from docstring_inheritance import NumpyDocstringInheritanceMeta

class Parent(metaclass=NumpyDocstringInheritanceMeta):
  def method(self, x, y=None):
    """Parent summary.

    Parameters

    x:
       Description for x.
    y:
       Description for y.

    Notes

...

</details>

### django-google-cloud-tasks

Async Tasks with HTTP endpoints

`pip install django-google-cloud-tasks` · installs (wheel) · licence: not stated · rank 12848 · last release 2025-05-15 · [PyPI](https://pypi.org/project/django-google-cloud-tasks/)

<details><summary>README extract</summary>

Powered by GCP Pilot.

Example:
```python
from django_cloud_tasks.tasks import Task

class MyTask(Task):
    def run(self, x, y):
        # computation goes here
        print(x**y)

MyTask.asap(x=10, y=3)  # run async (another instance will execute and print)
MyTask.sync(x=10, y=5)  # run sync (the print happens right now)
```

Sections: Django Cloud Tasks, APIs, IAM, Configuration, On Demand Task, Queue, Troubleshooting, Cleanup, Task Enqueuing Retry Policy, Global Configuration, Task-Specific Configuration, How It Works, Periodic Task, Publisher

</details>

### django-choices

Sanity for the django choices functionality.

`pip install django-choices` · installs (wheel) · licence: MIT License · rank 12915 · last release 2023-07-24 · [PyPI](https://pypi.org/project/django-choices/)

<details><summary>README extract</summary>

DISCLAIMER

New projects should not use this package. Existing users can follow the migration guide
in the documentation.

Note: Django 3.0 added enumeration types.
This feature mostly replaces the need for Django-Choices.
See also Adam Johnson's post on using them.

Introduction ...

Sections: Django-Choices, Order and sanity for django model choices., Source Code

</details>

### django-logentry-admin

Show all LogEntry objects in the Django admin site.

`pip install django-logentry-admin` · installs (wheel) · licence: ISC · rank 12929 · last release 2026-10-31 · [PyPI](https://pypi.org/project/django-logentry-admin/)

<details><summary>README extract</summary>

Show all LogEntry objects in the Django admin site.

Django records every addition, change and deletion made through the
admin, but only shows each user their own last few actions. This app
adds the whole log to the admin: ...

Sections: django-logentry-admin, v1.2.0 - 31/10/2026, v1.1.0 - 25/05/2021, v1.0.6 - 23/04/2020, v1.0.5 - 30/07/2019, v1.0.4 - 17/06/2018, v1.0.3 - 14/12/2017, v1.0.2 - 12/08/2016, v1.0.1 - 24/07/2016, v0.1.5 - 17/02/2015, v0.1.4 - 28/09/2014, v0.1.3 - 02/06/2014, v0.1.2 - 26/08/2013, v0.1.1 - 28/12/2011

</details>

### dyntastic

A DynamoDB library on top of Pydantic and boto3.

`pip install dyntastic` · installs (wheel) · licence: MIT · rank 12953 · last release 2025-04-06 · [PyPI](https://pypi.org/project/dyntastic/)

<details><summary>README extract</summary>

A DynamoDB library on top of Pydantic and boto3.

Example:
```python
import uuid
from datetime import datetime
from typing import Optional

from dyntastic import Dyntastic
from pydantic import Field

class Product(Dyntastic):
    table_name = "products"
    hash_key = "product_id"

    product_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: Optional[str] = None
...
```

Sections: dyntastic, Usage, Inserting into DynamoDB, Getting Items from DynamoDB, Querying Items in DynamoDB, Scanning Items in DynamoDB, Updating Items in DynamoDB, Batch Reads, Batch Writes, Transactions, Create a DynamoDB Table, Dynamic table names, 0.18.0 2025-04-05, 0.17.0 2025-02-25

</details>

### drf-kit

DRF Toolkit

`pip install drf-kit` · installs (wheel) · licence: not stated · rank 12958 · last release 2025-08-14 · [PyPI](https://pypi.org/project/drf-kit/)

<details><summary>README extract</summary>

A comprehensive toolkit that extends Django REST Framework with enhanced functionality and common patterns.

📚 Full Documentation

Features:
DRF Toolkit provides a comprehensive set of tools and utilities for Django REST Framework:

- Models: Enhanced model functionality with diff tracking, soft delete, and more
- Serializers: Advanced serialization with automatic field handling ...

Sections: Django REST Framework Toolkit, Quick Start, Requirements, Features, Setup

</details>

### dagio

A python package for running directed acyclic graphs of asynchronous I/O operations

`pip install dagio` · installs (wheel) · licence: MIT License · rank 12990 · last release 2021-10-18 · [PyPI](https://pypi.org/project/dagio/)

<details><summary>README extract</summary>

`dagio` is an embarassingly simple Python package for running directed acyclic
graphs of asynchronous I/O operations. It is built using and to be used with
Python's built-in `asyncio`
module, and provides a _veeeery_ thin layer of functionality on top of it.
:sweat_smile:

Features:
It's for making DAGs of IO operations. DAG IO. Technically it's _asynchronous_
DAG-based I/O, and the name `adagio` would have been siiiick, but it was
already taken! :sob:

Example:
```python
import asyncio

class MyDag:

    async def task_a(self):
        # does task a stuff...

    async def task_b(self):
        # does task b stuff...

    async def task_c(self):
        # does task c stuff...

    async def task_d(self):
        # does task d stuff...

    async def task_e(self):
...

</details>

### dagster-fivetran

Package for integrating Fivetran with Dagster.

`pip install dagster-fivetran` · installs (wheel) · licence: Apache-2.0 · rank 13001 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-fivetran/)

### django-oauth-toolkit-dcr

An extension to django oauth toolkit to support Dynamic Client Registration RFC7591

`pip install django-oauth-toolkit-dcr` · installs (wheel) · licence: MIT License · rank 13029 · last release 2025-06-07 · [PyPI](https://pypi.org/project/django-oauth-toolkit-dcr/)

<details><summary>README extract</summary>

An extension to Django OAuth Toolkit that adds support for OAuth 2.0 Dynamic Client Registration as defined in RFC 7591.

Features:
- ✅ RFC 7591 Compliant: Full implementation of OAuth 2.0 Dynamic Client Registration
- ✅ Open Registration Mode: No authentication required for client registration ...

Example:
```python
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

@method_decorator(ratelimit(key='ip', rate='10/h', method='POST'), name='post')
class RateLimitedDCRView(DynamicClientRegistrationView):
    pass
```

...

</details>

### djade

A Django template formatter.

`pip install djade` · installs (wheel) · licence: MIT · rank 13043 · last release 2026-10-15 · [PyPI](https://pypi.org/project/djade/) · [source](https://github.com/adamchainz/djade)

<details><summary>README extract</summary>

A Django template formatter.

 You can have any colour you like, as long as it’s [d]jade.

Djade formats Django template syntax with a style based on the template style guide in Django’s documentation.
It does not format HTML or other templated languages.

Djade is fast because it is built in Rust: benchmarked taking 20ms to format 377 templates. ...

Sections: Djade, pre-commit hook, Usage, Options, `--target-version`, `--check`, Formatting, Fixers, Django 4.2+: `length_is` -> `length`, Django 4.1+: empty ID `json_script` fixer, Django 3.1+: `ifequal` and `ifnotequal` -> `if`, Django 2.1+: `admin_static` and `staticfiles` -> `static`, Django 1.3+: legacy variable assignment syntax

</details>

