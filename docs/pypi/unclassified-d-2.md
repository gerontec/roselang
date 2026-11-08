# Unclassified / D (part 2 of 2)

[Index](README.md) · 552 packages in this topic, by downloads.

[part 1](unclassified-d.md) · part 2

### diptest

Hartigan's diptest.

`pip install diptest` · installs (wheel) · licence: GPLv2+ · rank 13049 · last release 2026-10-18 · [PyPI](https://pypi.org/project/diptest/) · [docs](https://github.com/RUrlus/diptest#readme) · [source](https://github.com/RUrlus/diptest)

_README extract left out: share-alike licence._

### django-jsonfield

JSONField for django models

`pip install django-jsonfield` · installs (wheel) · licence: BSD License · rank 13055 · last release 2020-10-28 · [PyPI](https://pypi.org/project/django-jsonfield/)

<details><summary>README extract</summary>

Maintenance mode only: It is not recommended you use this library on new
projects. Django 3.1 includes a cross-database `JSONField` implementation -
see its release notes.
You can use that field on older versions of Django with the
django-jsonfield-backport
package. See the (long) History section below for more information. ...

Sections: django-jsonfield, Notes, Extras, jsonify templatetag, 1.4.0 (2019-12-18), 1.3.1 (2019-08-19), 1.3.0 (2019-08-18), 1.2.0 (2019-04-28), 1.1.0 (2019-03-16), 1.0.1 (2016-07-21), 1.0.0 (2016-06-02), 0.7.1, 0.7

</details>

### dvclive

Experiments logger for ML projects.

`pip install dvclive` · installs (wheel) · licence: Apache-2.0 · rank 13106 · last release 2026-06-05 · [PyPI](https://pypi.org/project/dvclive/) · [docs](https://dvc.org/doc/dvclive) · [source](https://github.com/iterative/dvclive)

<details><summary>README extract</summary>

DVCLive is a Python library for logging machine learning metrics and other
metadata in simple file formats, which is fully compatible with DVC.

- Get Started
- How it Works
- API Reference
- Integrations

______________

Example:
```python
import time
import random

from dvclive import Live

params = {"learning_rate": 0.002, "optimizer": "Adam", "epochs": 20}

with Live() as live:

    # log a parameters
    for param in params:
        live.log_param(param, params[param])

    # simulate training
    offset = random.uniform(0.2, 0.1)
    for epoch in range(1, params["epochs"]):
...
```

Sections: DVCLive, Documentation, Quickstart, Initialize DVC Repository, Example code, Running, Comparing, DVC CLI, DVC Extension for VS Code, DVC Studio, Comparison to related technologies

</details>

### datetype

A type wrapper for the standard library `datetime` that supplies stricter checks, such as making 'datetime' not substitutable for 'date', and separating out Naive and Aware datetimes into separate, mutually-incompatible types.

`pip install datetype` · installs (wheel) · licence: not stated · rank 13184 · last release 2025-12-01 · [PyPI](https://pypi.org/project/datetype/) · [docs](https://datetype.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

DateType is a workaround for this
bug to demonstrate that we could
have a type-checking-time wrapper for `datetime` that doesn't change (or almost
doesn't change) the implementation, but fixes up two very annoying behaviors of
the stdlib `datetime` module:

1. ...

Sections: DateType, A Workaround

</details>

### dargs

Process arguments for the deep modeling project.

`pip install dargs` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 13195 · last release 2026-08-31 · [PyPI](https://pypi.org/project/dargs/) · [docs](https://docs.deepmodeling.com/projects/dargs) · [source](https://github.com/deepmodeling/dargs)

_README extract left out: share-alike licence._

### daikin-onecta

Async Python client for the Daikin Onecta cloud API

`pip install daikin-onecta` · installs (wheel) · licence: MIT · rank 13271 · last release 2026-11-01 · [PyPI](https://pypi.org/project/daikin-onecta/) · [source](https://github.com/jwillemsen/daikin-onecta)

<details><summary>README extract</summary>

Async Python client for the Daikin Onecta cloud API.

This library contains the Daikin-specific API layer used by the Home Assistant
Daikin Onecta integration. It deliberately has no dependency on Home Assistant.

Example:
```python
import aiohttp

from daikin_onecta import OnectaClient

async def token_provider() -> str:
    return "access-token"

async with aiohttp.ClientSession() as session:
    client = OnectaClient(session, token_provider)
    devices = await client.get_gateway_devices()
```

Sections: daikin-onecta, Usage, Errors

</details>

### deepface

A Lightweight Face Recognition and Facial Attribute Analysis Framework (Age, Gender, Emotion, Race) for Python

`pip install deepface` · installs (wheel) · licence: MIT License · rank 13289 · last release 2026-11-04 · [PyPI](https://pypi.org/project/deepface/)

<details><summary>README extract</summary>

DeepFace is a lightweight face recognition and facial attribute analysis (age, gender, emotion and race) framework for python. It is a hybrid face recognition framework wrapping state-of-the-art models: `VGG-Face`, `FaceNet`, `OpenFace`, `DeepFace`, `DeepID`, `ArcFace`, `Dlib`, `SFace`, `GhostFaceNet`, `Buffalo_L`. ...

Sections: deepface, Extended Applications

</details>

### duckdb-extension-vss

Duckdb vss extension

`pip install duckdb-extension-vss` · installs (wheel) · licence: MIT License · rank 13292 · last release 2026-11-01 · [PyPI](https://pypi.org/project/duckdb-extension-vss/) · [docs](https://github.com/santosh-d3vpl3x/duckdb_extensions#readme) · [source](https://github.com/santosh-d3vpl3x/duckdb_extensions)

### django-pgbulk

Native Postgres update, upsert, and copy operations.

`pip install django-pgbulk` · installs (wheel) · licence: BSD License · rank 13295 · last release 2025-11-30 · [PyPI](https://pypi.org/project/django-pgbulk/) · [docs](https://django-pgbulk.readthedocs.io) · [source](https://github.com/AmbitionEng/django-pgbulk)

<details><summary>README extract</summary>

`django-pgbulk` provides functions for doing native Postgres bulk upserts (i.e. UPDATE ON CONFLICT), bulk updates, and COPY FROM.

Bulk upserts can distinguish between updated/created rows and ignore unchanged updates. ...

Example:
```python
import pgbulk

pgbulk.upsert(
    MyModel,
    [
        MyModel(int_field=1, some_attr="some_val1"),
        MyModel(int_field=2, some_attr="some_val2"),
    ],
    # These are the fields that identify the uniqueness constraint.
    ["int_field"],
    # These are the fields that will be updated if the row already
...
```

Sections: django-pgbulk, Quick Start, Examples, Update or insert rows, Bulk update rows, Copy rows into a table, Advanced Features, Documentation, Compatibility, Creators

</details>

### dask-kubernetes

Native Kubernetes integration for Dask

`pip install dask-kubernetes` · installs (wheel) · licence: not stated · rank 13376 · last release 2026-03-02 · [PyPI](https://pypi.org/project/dask-kubernetes/)

### duckdb-extension-fts

Duckdb fts extension

`pip install duckdb-extension-fts` · installs (wheel) · licence: MIT License · rank 13378 · last release 2026-11-01 · [PyPI](https://pypi.org/project/duckdb-extension-fts/) · [docs](https://github.com/santosh-d3vpl3x/duckdb_extensions#readme) · [source](https://github.com/santosh-d3vpl3x/duckdb_extensions)

### docraptor

DocRaptor

`pip install docraptor` · installs (wheel) · licence: MIT · rank 13404 · last release 2023-09-27 · [PyPI](https://pypi.org/project/docraptor/)

<details><summary>README extract</summary>

A native client library for the DocRaptor HTML to PDF/XLS service. # noqa: E501

</details>

### dagster-duckdb-pandas

Package for storing Pandas DataFrames in DuckDB.

`pip install dagster-duckdb-pandas` · installs (wheel) · licence: Apache-2.0 · rank 13460 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-duckdb-pandas/)

### dbt-fabricspark

A Microsoft Fabric Spark adapter plugin for dbt

`pip install dbt-fabricspark` · does not install on CPython 3.14 · licence: MIT · rank 13540 · last release 2026-11-06 · [PyPI](https://pypi.org/project/dbt-fabricspark/)

<details><summary>README extract</summary>

dbt adapter for Fabric Spark supporting SQL models.

 dbt Docs
 Fabric Lakehouse with Spark
 Fabric Lakehouse Livy API

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. ...

Features:
- Livy session management with session reuse and robust connectivity across dbt runs
- Lakehouse with schema support — auto-detects schema-enabled lakehouses and uses three-part naming (`lakehouse.schema.table`) ...

...

</details>

### datedelta

Like datetime.timedelta, for date arithmetic.

`pip install datedelta` · installs (wheel) · licence: BSD License · rank 13564 · last release 2022-01-01 · [PyPI](https://pypi.org/project/datedelta/) · [source](https://github.com/aaugustin/datedelta)

<details><summary>README extract</summary>

`datedelta.datedelta` is `datetime.timedelta` for date arithmetic.

It accounts for oddities of the Gregorian calendar.

It's convenient for computing yearly, monthly, or weekly subscriptions periods.

It guarantees consistent results on arithmetic operations that it supports.

Example:
```python
>>> import datetime
>>> import datedelta

>>> datetime.date(2025, 4, 22) + 2 * datedelta.WEEK
datetime.date(2025, 5, 6)

>>> datetime.date(2025, 4, 22) + 3 * datedelta.MONTH
datetime.date(2025, 7, 22)
```

Sections: datedelta, Behavior, Usage, Basic intervals, Arbitrary intervals, Other operations, Limitations, Alternatives, 1.3, 1.2, 1.1, 1.0

</details>

### django-statsd-mozilla

Django interface with statsd

`pip install django-statsd-mozilla` · installs (wheel) · licence: BSD · rank 13570 · last release 2017-09-01 · [PyPI](https://pypi.org/project/django-statsd-mozilla/)

### django-modeladmin-reorder

Custom ordering for the apps and models in the admin app.

`pip install django-modeladmin-reorder` · installs from source (sdist only) · licence: BSD License · rank 13572 · last release 2018-04-25 · [PyPI](https://pypi.org/project/django-modeladmin-reorder/)

<details><summary>README extract</summary>

Custom ordering for the apps and models in the admin app. You can also rename, cross link or exclude models from the app list.

Features:
* Reorder apps in admin index - this will allow you to position most used apps in top of the page, instead of listing apps alphabetically. e.g. `sites` app before the `auth` app ...

Sections: django-modeladmin-reorder, Features, Documentation, Configuration, 0.1.0 (2014-08-01)

</details>

### duckdb-extension-httpfs

Duckdb httpfs extension

`pip install duckdb-extension-httpfs` · installs (wheel) · licence: MIT License · rank 13580 · last release 2026-11-01 · [PyPI](https://pypi.org/project/duckdb-extension-httpfs/) · [docs](https://github.com/santosh-d3vpl3x/duckdb_extensions#readme) · [source](https://github.com/santosh-d3vpl3x/duckdb_extensions)

### dapr-ext-fastapi

Dapr FastAPI Extension for the Dapr Python SDK.

`pip install dapr-ext-fastapi` · installs (wheel) · licence: Apache Software License · rank 13608 · last release 2026-07-15 · [PyPI](https://pypi.org/project/dapr-ext-fastapi/) · [docs](https://github.com/dapr/docs) · [source](https://github.com/dapr/python-sdk)

<details><summary>README extract</summary>

This FastAPI extension is used for FastAPI http server.

Sections: dapr-ext-fastapi extension, References

</details>

### distro-info

(no summary)

`pip install distro-info` · installs (wheel) · licence: not stated · rank 13678 · last release 2021-10-27 · [PyPI](https://pypi.org/project/distro-info/)

### dbx

DataBricks CLI eXtensions aka dbx

`pip install dbx` · installs (wheel) · licence: not stated · rank 13686 · last release 2024-07-02 · [PyPI](https://pypi.org/project/dbx/)

<details><summary>README extract</summary>

🧱Databricks CLI eXtensions - aka dbx is a CLI tool for development and advanced Databricks workflows management.

`dbx` simplifies Databricks workflows development, deployment and launch across multiple
environments. It also helps to package your project and deliver it to
your Databricks environment in a versioned fashion. ...

Sections: dbx by Databricks Labs, Concept, Requirements, Documentation, Interface versioning, Legal Information, Feedback

</details>

### dirsql

Ephemeral SQL index over a local directory

`pip install dirsql` · installs (wheel) · licence: MIT · rank 13698 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dirsql/)

<details><summary>README extract</summary>

Ephemeral SQL index over a local directory. `dirsql` watches a filesystem, ingests structured files into an in-memory SQLite database, and exposes a SQL query interface -- the filesystem is always the source of truth.

Documentation

Also available as `dirsql` on crates.io and `dirsql` on npm.

Example:
```python
import asyncio
import json
from dirsql import DirSQL, Table

async def main():
    db = DirSQL(
        "./my-blog",
        tables=[
            Table(
                ddl="CREATE TABLE posts (title TEXT, author TEXT)",
                glob="posts/*.json",
                extract=lambda path: [json.loads(open(path, encoding="utf-8").read())],
...
```

...

</details>

### django-settings-holder

Object that allows settings to be accessed with attributes.

`pip install django-settings-holder` · installs (wheel) · licence: MIT · rank 13724 · last release 2026-10-09 · [PyPI](https://pypi.org/project/django-settings-holder/) · [docs](https://mrthearman.github.io/django-settings-holder) · [source](https://github.com/MrThearMan/django-settings-holder)

<details><summary>README extract</summary>

[][coverage]
[][status]
[][pypi]
[][licence]
[][repo]
[][issues]
[][pypi]

[][pypi]
[][pypi]

Documentation:

Source Code:

Contributing:

This library provides utilities for Django extensions that want to define their own settings dictionaries.
Settings can be included in a SettingsHolder that allows them to be accessed via attributes. ...

</details>

### django-http-compression

Django middleware for compressing HTTP responses with Zstandard, Brotli, or Gzip.

`pip install django-http-compression` · installs (wheel) · licence: MIT · rank 13756 · last release 2026-04-08 · [PyPI](https://pypi.org/project/django-http-compression/) · [source](https://github.com/adamchainz/django-http-compression)

<details><summary>README extract</summary>

Django middleware for compressing HTTP responses with Zstandard, Brotli, or Gzip.

For a bit of background, see the introductory blog post.

Work smarter and faster with my book Boost Your Django DX which covers many ways to improve your development experience.

Python 3.10 to 3.14 supported.

Django 4.2 to 6.0 supported. ...

Sections: django-http-compression, Requirements, API

</details>

### dbt-colibri

A column lineage parser and dashboarding tool

`pip install dbt-colibri` · installs (wheel) · licence: MIT · rank 13783 · last release 2026-10-05 · [PyPI](https://pypi.org/project/dbt-colibri/)

<details><summary>README extract</summary>

A lightweight, developer-friendly CLI tool and self-hostable dashboard for extracting and visualizing column-level lineage from your dbt projects.

Built for data teams who want transparent, flexible lineage tracking without vendor lock-in or complex enterprise tooling.

Features:
- 🔍 Complete visibility: Easy UI, track how every column flows through your dbt transformations
- ⚡ Fast & lightweight: Generate reports in seconds from your existing dbt artifacts ...

Sections: Why dbt-colibri?, Quick Start, Basic Usage, Documentation, CLI Commands, `colibri generate`, Output Files, Project Structure, Advanced Usage, CI/CD Integration, General idea, Technical Details, Requirements, dbt Compatibility

</details>

### droid-sdk

Python asyncio SDK for Factory Droid

`pip install droid-sdk` · installs (wheel) · licence: Apache-2.0 · rank 13796 · last release 2026-09-24 · [PyPI](https://pypi.org/project/droid-sdk/)

<details><summary>README extract</summary>

Async Python 3.10+ SDK for local Factory Droid sessions.

Example:
```python
import asyncio
from droid_sdk import run

async def main() -> None:
    result = await run("Summarize this repository.", timeout=60)
    print(result.text if result.success else result.subtype)

asyncio.run(main())
```

Sections: Factory Droid SDK for Python, One turn or a conversation, Results, errors, and typing, Structured output and attachments, Discover available models, Interactions and controls, SDK attribution, Custom system prompts, Resume and replacement ownership, MCP and custom runtime, Saved sessions and examples, Limitations

</details>

### dvsim

DV system

`pip install dvsim` · installs (wheel) · licence: Apache-2.0 · rank 13857 · last release 2026-10-28 · [PyPI](https://pypi.org/project/dvsim/)

<details><summary>README extract</summary>

<!--

Sections: DVSim, About the project, About this repository, Using nix and direnv, Using uv direct, macOS and Linux, Windows (Powershell), Using DVSim, Documentation, Other related documents, Licensing, Bugs

</details>

### datalayer-reactor

FastAPI + pluggy extension reactor for modular SaaS applications

`pip install datalayer-reactor` · installs (wheel) · licence: BSD-3-Clause · rank 13944 · last release 2026-11-07 · [PyPI](https://pypi.org/project/datalayer-reactor/)

<details><summary>README extract</summary>

Application builders hit a wall when a feature spans the browser and the
server: frontend and backend plugin systems usually disagree about discovery,
dependencies, lifecycle, compatibility, and enablement. ...

Sections: ⚛️ Reactor, 📖 Documentation, 🎵 The music store, running in the page, Repository layout

</details>

### duckdb-extensions

DuckDB extensions as python package

`pip install duckdb-extensions` · installs (wheel) · licence: MIT License · rank 13959 · last release 2026-11-01 · [PyPI](https://pypi.org/project/duckdb-extensions/) · [docs](https://github.com/santosh-d3vpl3x/duckdb_extensions#readme) · [source](https://github.com/santosh-d3vpl3x/duckdb_extensions)

<details><summary>README extract</summary>

Sections: Available extensions, Project scope, Artifact integrity checks, Licensing

</details>

### django-log-formatter-asim

Formats Django logs in ASIM format.

`pip install django-log-formatter-asim` · installs (wheel) · licence: MIT License · rank 14021 · last release 2026-08-24 · [PyPI](https://pypi.org/project/django-log-formatter-asim/)

<details><summary>README extract</summary>

The library formats Django logs in ASIM format.

Mapping to the format may not be complete, but best effort has been made to create logical field mappings.

Example:
```python
from django_log_formatter_asim import ASIMFormatter

LOGGING = {
    ...
    "formatters": {
        "asim_formatter": {
            "()": ASIMFormatter,
        },
    },
    'handlers': {
        'asim': {
            'formatter': 'asim_formatter',
            ...
        },
    },
    "root": {
        "handlers": ["asim"],
        ...
    }
...
```

...

</details>

### django-socio-grpc

Fork of django-grpc-framework with more feature maintained by the socio team. Make GRPC with django easy.

`pip install django-socio-grpc` · installs (wheel) · licence: not stated · rank 14025 · last release 2025-09-24 · [PyPI](https://pypi.org/project/django-socio-grpc/)

### django-elasticsearch-dsl-drf

Integrate Elasticsearch DSL with Django REST framework.

`pip install django-elasticsearch-dsl-drf` · installs (wheel) · licence: GNU General Public License v2 (GPLv2); GNU Lesser General Public License v2 or l · rank 14027 · last release 2022-07-03 · [PyPI](https://pypi.org/project/django-elasticsearch-dsl-drf/) · [docs](https://django-elasticsearch-dsl-drf.readthedocs.io/) · [source](https://github.com/barseghyanartur/django-elasticsearch-dsl-drf)

_README extract left out: share-alike licence._

### dash-renderer

Front-end component renderer for Dash

`pip install dash-renderer` · installs from source (sdist only) · licence: MIT · rank 14030 · last release 2021-04-08 · [PyPI](https://pypi.org/project/dash-renderer/)

### django-deprecated-field

Util for marking Django DB fields as deprecated, enabling migration consistency with rolling deploys

`pip install django-deprecated-field` · installs (wheel) · licence: MIT License · rank 14068 · last release 2025-12-09 · [PyPI](https://pypi.org/project/django-deprecated-field/)

<details><summary>README extract</summary>

A Django field util that allows you to mark model fields as deprecated. This will enable you to have migration consistency when using rolling deploy.

When you have multiple instances of Django running, for redundancy, you typically deploy new versions in a rolling manner. ...

Features:
When a field is deprecated, we:
- Ensure that is is nullable, which is necessary for cross-version compatibility for `INSERT`s
- Omit the field from `SELECT`s and other queries, ensuring cross-version compatibility for `SELECT`s, etc ...

Example:
```python
from django.db import models
from django_deprecated_field import deprecated

class MyClass(models.Model):

    my_field = deprecated(
        models.CharField(...)
    )
```

...

</details>

### dragonfly-energy

Dragonfly extension for energy simulation.

`pip install dragonfly-energy` · installs (wheel) · licence: AGPL-3.0 · rank 14106 · last release 2026-11-06 · [PyPI](https://pypi.org/project/dragonfly-energy/)

_README extract left out: share-alike licence._

### django-salesforce

a Salesforce backend for Django's ORM

`pip install django-salesforce` · installs (wheel) · licence: MIT (or AGPL) · rank 14148 · last release 2026-04-09 · [PyPI](https://pypi.org/project/django-salesforce/)

_README extract left out: share-alike licence._

### dash-mp-components

Dash components for the Materials Project. Version is managed by Git tags in CI/CD

`pip install dash-mp-components` · installs (wheel) · licence: BSD · rank 14156 · last release 2026-06-09 · [PyPI](https://pypi.org/project/dash-mp-components/)

### dna-features-viewer

Plot features from DNA sequences (e.g. Genbank) with Python

`pip install dna-features-viewer` · installs (wheel) · licence: MIT · rank 14231 · last release 2025-05-09 · [PyPI](https://pypi.org/project/dna-features-viewer/)

<details><summary>README extract</summary>

DNA Features Viewer is a Python library to visualize DNA features, e.g. from GenBank or Gff files:

DNA Features Viewer can plot sequence maps linearly or circularly, with or without nucleotide sequence and amino-acid sequences. The plotter automatically produces clear plots even for sequences with many overlapping features and long labels. ...

Sections: DNA Features Viewer, Infos, More biology software

</details>

### databricks-labs-pylint

Plugin for PyLint to support Databricks specific code patterns and best practices.

`pip install databricks-labs-pylint` · installs (wheel) · licence: Other/Proprietary License · rank 14249 · last release 2024-10-03 · [PyPI](https://pypi.org/project/databricks-labs-pylint/) · [source](https://github.com/databrickslabs/pylint-plugin)

<details><summary>README extract</summary>

<!-- FOR CONTRIBUTORS: Edit this file in Visual Studio Code with the recommended extensions, so that we update the table of contents automatically -->


PyLint serves as a valuable tool for developers by performing various checks on code quality. ...

Features:
Even though Ruff is 10x+ faster
than PyLint, it doesn't have a plugin system yet, nor does it have
a feature parity with PyLint yet. Other
projects use MyPy,
Ruff, and PyLint together to achieve
the most comprehensive code analysis. ...

...

</details>

### django-reversion-compare

Add compare view to django-reversion for comparing two versions of a reversion model.

`pip install django-reversion-compare` · installs (wheel) · licence: GPL-3.0-or-later · rank 14251 · last release 2026-10-06 · [PyPI](https://pypi.org/project/django-reversion-compare/) · [docs](https://codeberg.org/jedie/django-reversion-compare) · [source](https://codeberg.org/jedie/django-reversion-compare)

_README extract left out: share-alike licence._

### debug-mgr

Simple debug manager for use of C++ Python extensions

`pip install debug-mgr` · installs (wheel) · licence: Apache 2.0 · rank 14267 · last release 2026-08-30 · [PyPI](https://pypi.org/project/debug-mgr/)

<details><summary>README extract</summary>

Simple debug manager for use of C++ Python extensions

</details>

### dhanhq

The official Python client for communicating with the DhanHQ API

`pip install dhanhq` · installs (wheel) · licence: MIT LICENSE · rank 14279 · last release 2026-10-08 · [PyPI](https://pypi.org/project/dhanhq/)

<details><summary>README extract</summary>

> v2.3.0 is the latest stable release. You can install the previous stable version by using the below code:

The official Python client for communicating with the Dhan API

DhanHQ-py Rest API is used to automate investing and trading. ...

Features:
* Order Management
The order management APIs lets you place a new order, cancel or modify the pending order, retrieve the order status, trade status, order book & tradebook. ...

Example:
```python
from dhanhq import DhanContext, MarketFeed

# Define and use your dhan_context if you haven't already done so like below:
dhan_context = DhanContext("client_id","access_token")

# Structure for subscribing is (exchange_segment, "security_id", subscription_type)

instruments = [(MarketFeed.NSE, "1333", MarketFeed.Ticker),   # Ticker - Ticker Data
...
...

</details>

### dreamscale

Cloud robot policy inference — one function call.

`pip install dreamscale` · installs (wheel) · licence: Apache-2.0 · rank 14306 · last release 2026-11-07 · [PyPI](https://pypi.org/project/dreamscale/) · [docs](https://docs.dreamscalelabs.com)

<details><summary>README extract</summary>

Cloud robot policy inference — one function call.

> Pre-alpha SDK. Model access and deployment readiness are separate from package installation.
> Formerly `dropbear`. Existing `dropbear` projects keep working unchanged: the
> `dropbear` package now installs `dreamscale` and keeps the old import and command.

Example:
```python
import dreamscale

result = dreamscale.agents.run_yam(
    model="gpt-6-astra",
    instruction="Open both grippers",
)
```

...

</details>

### django-datatables-view

Django datatables view

`pip install django-datatables-view` · installs (wheel) · licence: MIT License · rank 14339 · last release 2022-04-05 · [PyPI](https://pypi.org/project/django-datatables-view/)

<details><summary>README extract</summary>

django-datatables-view is a base view for handling server side processing for the awesome datatables 1.9.x,
1.10.x (

django-datatables-view simplifies handling of sorting, filtering and creating JSON output, as defined
at:

Example:
```python
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape

class OrderListJson(BaseDatatableView):
    order_columns = ['number', 'user', 'state']

    def get_initial_queryset(self):
        # return queryset used as base for further sorting/filtering
...
```

Sections: About, Example, Usage, 2. Edit views.py, 3. Edit urls.py, 4. Define HTML + JavaScript, Another example of views.py customisation, Yet another example of views.py customisation

</details>

### django-oscar

A domain-driven e-commerce framework for Django

`pip install django-oscar` · installs (wheel) · licence: BSD License · rank 14348 · last release 2026-09-29 · [PyPI](https://pypi.org/project/django-oscar/)

<details><summary>README extract</summary>

Oscar is an e-commerce framework for Django designed for building domain-driven
sites. It is structured such that any part of the core functionality can be
customised to suit the needs of your project. ...

Sections: Domain-driven e-commerce for Django, Screenshots, Sandbox, Extensions, Videos, Our Pledge, Our Standards, Our Responsibilities, Enforcement, Case studies

</details>

### devicecheck

Apple DeviceCheck API. Reduce fraudulent use of your services by managing device state and asserting app integrity.

`pip install devicecheck` · installs (wheel) · licence: MIT License · rank 14383 · last release 2024-05-03 · [PyPI](https://pypi.org/project/devicecheck/) · [source](https://github.com/Kylmakalle/devicecheck)

<details><summary>README extract</summary>

<!-- -->

Accessing and Modifying Per-Device Data

Use a token from your app to validate requests, query and modify two per-device binary digits stored on Apple servers.

Features:
- Prevent API & Content abuse with validating requests via Apple device token
- Query and modify two bits of data to achieve up to four remote states saved on Apple servers
- Easy to use configuration
- Examples ...

Example:
```python
from devicecheck import DeviceCheck

device_check = DeviceCheck(
    team_id="XX7AN23E0Z",  #
    bundle_id="com.akentev.app",
    key_id="JSAD983ENA",  # Generated at
    private_key="/path/to/AuthKey_JSAD983ENA.p8",
    # Generated file at
    dev_environment=True,  # True if using development Apple environment, False if using in production.
...
```

...

</details>

### django-threadlocals

Contains utils for storing and retreiving values from threadlocals, and middleware for placing the current Django request in threadlocal storage.

`pip install django-threadlocals` · installs (wheel) · licence: BSD License · rank 14412 · last release 2019-01-31 · [PyPI](https://pypi.org/project/django-threadlocals/)

<details><summary>README extract</summary>

Example:
```python
from threadlocals.threadlocals import get_current_request

request = get_current_request()
```

Sections: Setup/Usage, Caveat Emptor

</details>

### dukascopy-python

Download and stream historical price data for variety of financial instruments (Forex, Commodities and Indices) from Dukascopy Bank SA.

`pip install dukascopy-python` · installs (wheel) · licence: MIT License · rank 14429 · last release 2026-10-28 · [PyPI](https://pypi.org/project/dukascopy-python/)

<details><summary>README extract</summary>

Download historical financial market data from Dukascopy Bank SA, including tick-level prices and OHLCV candles for Forex, commodities, indices, and other financial instruments.

Supports multiple data feed versions, configurable HTTP sessions, optional logging, and Pandas integration.

Example:
```python
from datetime import datetime, timezone

import dukascopy_python.compat as duka
from dukascopy_python.compat.instruments import (
    INSTRUMENT_FX_MAJORS_EUR_USD,
)

df = duka.fetch(
    INSTRUMENT_FX_MAJORS_EUR_USD,
    duka.INTERVAL_MIN_1,
    duka.OFFER_SIDE_BID,
    datetime(2025, 1, 1, tzinfo=timezone.utc),
...
```

...

</details>

### dbt-copilot-python

Helper functions to run Django and Flask applications in AWS Copilot/ECS.

`pip install dbt-copilot-python` · installs (wheel) · licence: not stated · rank 14443 · last release 2026-02-16 · [PyPI](https://pypi.org/project/dbt-copilot-python/)

<details><summary>README extract</summary>

A set of utility functions for running Django & Flask apps in AWS ECS via AWS Copilot.

Example:
```python
from dbt_copilot_python.network import setup_allowed_hosts

ALLOWED_HOSTS = [...]

ALLOWED_HOSTS = setup_allowed_hosts(ALLOWED_HOSTS)
```

Sections: DBT Copilot Python, Using `dbt-copilot-python`, With celery, With error tracking, Usage, `ALLOWED_HOSTS` setting, Celery health check, `DATABASES` setting, Error tracking, Requirements, Run the tests, Publishing

</details>

### django-quill-editor

Integrate Quill editor with Django project.

`pip install django-quill-editor` · installs (wheel) · licence: MIT · rank 14475 · last release 2024-09-20 · [PyPI](https://pypi.org/project/django-quill-editor/)

<details><summary>README extract</summary>

django-quill-editor makes Quill.js easy to use on Django Forms and admin sites

- No configuration required for static files!
- The entire code for inserting WYSIWYG editor is less than 30 lines
- It can be used in both admin and Django views ...

Example:
```python
# models.py
from django.db import models
from django_quill.fields import QuillField

class QuillPost(models.Model):
    content = QuillField()
```

Sections: django-quill-editor, Live Demo, Documentation, QuickStart, Setup, Making Model, Using in admin, Running the Live Demo project in local, Distribution tips (for owners), Sphinx docs, Local, docker-compose up

</details>

### django-db-file-storage

Custom FILE_STORAGE for Django. Saves files in your database instead of your file system.

`pip install django-db-file-storage` · installs (wheel) · licence: MIT License · rank 14477 · last release 2024-01-30 · [PyPI](https://pypi.org/project/django-db-file-storage/)

<details><summary>README extract</summary>

Django DB File Storage is a custom
file storage system
for Django. Use it to save files in your database instead of your file system.

Supports Python versions `2.7`, `3.5`, `3.6+`, and Django versions `1.11`, `2.2` & `3.0+`.

Dependencies scanned by PyUp.io

The project docs can be found here (RTD).

In order to run the demo project, just

Sections: django-db-file-storage, Documentation, Demo, . download the project and `cd` into it,, . `cd` into the `demo_and_tests` directory,, . visit in your browser.

</details>

### django-admin-confirm

Adds confirmation to Django Admin changes, additions and actions

`pip install django-admin-confirm` · installs (wheel) · licence: Apache 2.0 · rank 14492 · last release 2026-10-01 · [PyPI](https://pypi.org/project/django-admin-confirm/)

<details><summary>README extract</summary>

AdminConfirmMixin is a mixin for ModelAdmin to add confirmations to change, add and actions.

It can be configured to add a confirmation page on ModelAdmin upon:

- saving changes
- adding new instances
- performing actions

Typical Usage:

Example:
```python
from admin_confirm import AdminConfirmMixin

class MyModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['field1', 'field2']
```

Sections: Django Admin Confirm, Disclaimer, Configuration Options, Usage

</details>

### dash-svg

SVG support library for Plotly/Dash

`pip install dash-svg` · installs (wheel) · licence: MIT · rank 14494 · last release 2023-02-27 · [PyPI](https://pypi.org/project/dash-svg/)

<details><summary>README extract</summary>

Scalable Vector Graphics (SVG) library for Plotly/Dash

Dash clone of the ubiquitous *create-react-app* default project,

Example:
```python
import dash
from dash import html
from dash_svg import Svg, G, Path, Circle

app = dash.Dash(name)

app.layout = html.Div([
    html.Header([
        Svg([
            G([
                Path(d='...'),
                Circle(cx="420.9", cy="296.5", r='45.7'),
                Path(d='M520.5 78.1z')
            ], fill='#61DAFB')
...
```

Sections: dash-svg, Documentation

</details>

### django-scopes

Scope queries in multi-tenant django applications

`pip install django-scopes` · installs (wheel) · licence: Apache-2.0 · rank 14498 · last release 2026-07-24 · [PyPI](https://pypi.org/project/django-scopes/)

<details><summary>README extract</summary>

Motivation

Many of us use Django to build multi-tenant applications where every user only ever
gets access to a small, separated fraction of the data in our application, while
at the same time having *some* global functionality that makes separate databases per
client infeasible. ...

Example:
```python
from django.db import models

class Site(models.Model):
    name = models.CharField(…)

class Post(models.Model):
    site = models.ForeignKey(Site, …)
    title = models.CharField(…)

class Comment(models.Model):
    post = models.ForeignKey(Post, …)
    text = models.CharField(…)
```

Sections: django-scopes, Activate scopes in contexts, Custom manager classes, Scoping the User model, Locking, Admin, ModelForms, django-filter, Uniqueness, Further reading

</details>

### darwin-py

Library and command line interface for darwin.v7labs.com

`pip install darwin-py` · does not install on CPython 3.14 · licence: MIT License · rank 14499 · last release 2026-11-06 · [PyPI](https://pypi.org/project/darwin-py/) · [docs](https://darwin-py-sdk.v7labs.com/index.html) · [source](https://github.com/v7labs/darwin-py)

<details><summary>README extract</summary>

⚡️ Official library to annotate, manage datasets, and models on
V7's Darwin Training Data Platform. ⚡️

Darwin-py can both be used from the command line and as a python library.

<hr/>

Main functions are (but not limited to):

- Client authentication
- Listing local and remote datasets
- Create/remove datasets ...

Example:
```python
from darwin.client import Client

client = Client.local() # use the configuration in ~/.darwin/config.yaml
dataset = client.get_remote_dataset("example-team/test")
dataset.pull() # downloads annotations and images for the latest exported version
```

...

</details>

### django-ltree

Django app to support ltree postgres extension

`pip install django-ltree` · installs (wheel) · licence: not stated · rank 14504 · last release 2026-08-26 · [PyPI](https://pypi.org/project/django-ltree/) · [source](https://github.com/mariocesar/django_ltree)

<details><summary>README extract</summary>

A Django implementation for PostgreSQL's ltree extension, providing efficient storage and querying of hierarchical tree-like data.

See PostgreSQL's ltree documentation to learn
more about it.

The main benefits of `ltree`:

- Efficient path queries (ancestors, descendants, pattern matching)
- Index-friendly hierarchical storage ...

Features:
- Django model fields for ltree data types
- Query utilities for common tree operations
- Migration support for ltree extension installation
- Compatibility with Django's ORM and query syntax

Example:
```python
class Meta(TreeModel.Meta):
```

...

</details>

### djc-core

Core library for django-components written in Rust.

`pip install djc-core` · installs (wheel) · licence: MIT · rank 14510 · last release 2026-06-25 · [PyPI](https://pypi.org/project/djc-core/)

<details><summary>README extract</summary>

Rust-based parsers and toolings used by django-components. Exposed as a Python package with maturin.

Example:
```python
from djc_core.safe_eval import safe_eval

# Compile an expression
compiled = safe_eval("my_var + 1")

# Evaluate with a context
result = compiled({"my_var": 5})
print(result)  # 6
```

Sections: djc-core, Packages, Safe eval, HTML transfomer, Architecture, Crate structure, Design philosophy, Deployment, Creating new crates, 1. Create Rust-side code, 2. Expose Rust code to Python, 3. Define Python-side code

</details>

### django-pattern-library

A module for Django that allows to build pattern libraries for your projects.

`pip install django-pattern-library` · installs (wheel) · licence: BSD License · rank 14542 · last release 2026-07-24 · [PyPI](https://pypi.org/project/django-pattern-library/) · [docs](https://torchbox.github.io/django-pattern-library/) · [source](https://github.com/torchbox/django-pattern-library)

<details><summary>README extract</summary>

> UI pattern libraries for Django templates. Try our online demo.

Features:
This package automates the maintenance of UI pattern libraries or styleguides for Django projects, and allows developers to experiment with Django templates without having to create Django views and models. ...

Sections: django-pattern-library, Features, Why you need this, Online demo, Documentation, Nightly builds

</details>

### datarobot-asgi-middleware

A FastAPI/ASGI middleware to simplify development of FastAPI apps on DataRobot

`pip install datarobot-asgi-middleware` · installs (wheel) · licence: not stated · rank 14562 · last release 2025-06-17 · [PyPI](https://pypi.org/project/datarobot-asgi-middleware/)

<details><summary>README extract</summary>

A middleware to simplify front-proxy handling and health checks in
DataRobot.

Example:
```python
from fastapi import FastAPI

from datarobot_asgi_middleware import DataRobotASGIMiddleware

app = FastAPI()
app.add_middleware(DataRobotASGIMiddleware)

@app.get("/")
async def root():
    return {"message": "hello"}
```

Sections: DataRobot ASGI Middleware, Usage

</details>

### datadog-serverless-compat

Datadog Serverless Compatibility Layer for Python

`pip install datadog-serverless-compat` · installs (wheel) · licence: Apache Software License · rank 14569 · last release 2026-11-02 · [PyPI](https://pypi.org/project/datadog-serverless-compat/) · [source](https://github.com/DataDog/datadog-serverless-compat-py)

<details><summary>README extract</summary>

Datadog library for Python to enable tracing and custom metric submission from Azure Functions and Google Cloud Run Functions (1st gen).

Sections: Datadog Serverless Compatibility Layer for Python, Getting Started

</details>

### django-bmemcached

A Django cache backend to use bmemcached module which supports memcached binary protocol with authentication.

`pip install django-bmemcached` · installs from source (sdist only) · licence: MIT License · rank 14575 · last release 2020-01-09 · [PyPI](https://pypi.org/project/django-bmemcached/)

### dagster-iceberg

Package for PyIceberg-specific Dagster framework op and resource components.

`pip install dagster-iceberg` · installs (wheel) · licence: Apache Software License · rank 14581 · last release 2026-05-27 · [PyPI](https://pypi.org/project/dagster-iceberg/)

<details><summary>README extract</summary>

> ⚠️ This project has preview status

Dagster IO manager for managing Iceberg tables with PyIceberg.

Features:
Available features can be found here.

Sections: Examples, Documentation, Features

</details>

### dbmate-bin

A thin wrapper to distribute https://github.com/amacneil/dbmate via pip.

`pip install dbmate-bin` · installs (wheel) · licence: MIT · rank 14646 · last release 2026-10-21 · [PyPI](https://pypi.org/project/dbmate-bin/) · [source](https://github.com/justin-yan/pybin)

<details><summary>README extract</summary>

This project is part of the pybin family of packages, which are generally
permissively-licensed binary tools that have been re-packaged to be distributable via python's PyPI infrastructure using
`pip install $TOOLNAME-bin`. ...

Sections: dbmate-bin, Packaging Details

</details>

### dash-testing-stub

Package installed with dash[testing] for optional loading of pytest dash plugin.

`pip install dash-testing-stub` · installs (wheel) · licence: MIT License · rank 14671 · last release 2023-02-09 · [PyPI](https://pypi.org/project/dash-testing-stub/)

### docent-python

Renamed to 'docent'. This package is a redirect that depends on 'docent'.

`pip install docent-python` · installs (wheel) · licence: Apache-2.0 · rank 14719 · last release 2026-10-06 · [PyPI](https://pypi.org/project/docent-python/) · [docs](https://transluce.mintlify.app)

<details><summary>README extract</summary>

This package has been renamed to `docent`.

`docent-python` is now a thin redirect that depends on `docent`. Installing it
will install `docent` automatically, and `import docent` continues to work
without any code changes.

Replace `docent-python` with `docent` in your project's dependencies:

The import path is unchanged:

Example:
```python
import docent
```

Sections: docent-python, Migrating, Source

</details>

### dagster-ssh

Package for ssh Dagster framework components.

`pip install dagster-ssh` · installs (wheel) · licence: Apache-2.0 · rank 14730 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dagster-ssh/)

### dwave-samplers

Ocean-compatible collection of solvers/samplers.

`pip install dwave-samplers` · installs (wheel) · licence: Apache Software License · rank 14763 · last release 2026-06-18 · [PyPI](https://pypi.org/project/dwave-samplers/) · [docs](https://docs.dwavequantum.com) · [source](https://github.com/dwavesystems/dwave-samplers)

<details><summary>README extract</summary>

Ocean software provides a variety of quantum, classical, and quantum-classical
hybrid dimod
samplers
that run either remotely (for example, in the
Leap service) or locally on your CPU.

Sections: dwave-samplers, Planar, Random, Simulated Annealing, Simulated Quantum Annealing, Steepest Descent, Tabu, Tree Decomposition

</details>

### demoparser2

(no summary)

`pip install demoparser2` · installs (wheel) · licence: not stated · rank 14773 · last release 2026-10-29 · [PyPI](https://pypi.org/project/demoparser2/)

### django-mass-edit

Make bulk changes in the Django admin interface

`pip install django-mass-edit` · installs (wheel) · licence: BSD License · rank 14802 · last release 2023-08-22 · [PyPI](https://pypi.org/project/django-mass-edit/)

### django-iam-dbauth

Django database backends to use AWS Database IAM Authentication

`pip install django-iam-dbauth` · installs (wheel) · licence: MIT License · rank 14811 · last release 2024-09-12 · [PyPI](https://pypi.org/project/django-iam-dbauth/)

<details><summary>README extract</summary>

<!-- start-no-pypi -->

<!-- end-no-pypi -->

Sections: Django IAM database backends, Usage, SSL and PostgreSQL, SSL and MySQL, CNAME considerations

</details>

### datasetsforecast

Datasets for Time series forecasting

`pip install datasetsforecast` · installs (wheel) · licence: MIT License · rank 14826 · last release 2026-10-27 · [PyPI](https://pypi.org/project/datasetsforecast/) · [docs](https://nixtlaverse.nixtla.io/datasetsforecast/) · [source](https://github.com/Nixtla/datasetsforecast)

<details><summary>README extract</summary>

> Datasets for time series forecasting

Example:
```python
from datasetsforecast.phm2008 import PHM2008
```

Sections: datasetsforecast, Datasets, How to use

</details>

### Dijkstar

Dijkstra/A*

`pip install Dijkstar` · installs (wheel) · licence: MIT License · rank 14831 · last release 2021-03-30 · [PyPI](https://pypi.org/project/Dijkstar/)

<details><summary>README extract</summary>

Dijkstar is an implementation of Dijkstra's single-source shortest-paths
algorithm. If a destination node is given, the algorithm halts when that
node is reached; otherwise it continues until paths from the source node
to all other nodes are found.

Accepts an optional cost (or "weight") function that will be called on
every iteration. ...

Example:
```python
>>> from dijkstar import Graph, find_path
>>> graph = Graph()
>>> graph.add_edge(1, 2, 110)
>>> graph.add_edge(2, 3, 125)
>>> graph.add_edge(3, 4, 108)
>>> find_path(graph, 1, 4)
PathInfo(
    nodes=[1, 2, 3, 4],
    edges=[110, 125, 108],
    costs=[110, 125, 108],
    total_cost=343)
```

Sections: Dijkstar, Graph Export & Import

</details>

### django-rest-framework-condition

Decorators @condition, @last_modified and @etag for Django Rest Framework

`pip install django-rest-framework-condition` · installs (wheel) · licence: not stated · rank 14859 · last release 2019-04-08 · [PyPI](https://pypi.org/project/django-rest-framework-condition/)

<details><summary>README extract</summary>

This package allows you to use `@condition` decorator from Django on ViewSet or
APIView from Django Rest Framework. In other words, you can use http headers
ETag and Last-modified with you APIs. ...

Example:
```python
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_condition import last_modified

class LastModifiedApiView(APIView):
    @last_modified(lambda _: datetime(2019, 1, 1))
    def get(self, request):
        return Response({'data': 'I have Last-Modified header!'})
```

</details>

### deepcomparer

Deep compare python structures like dictionaries, lists and iterables.

`pip install deepcomparer` · installs (wheel) · licence: MIT License · rank 14868 · last release 2023-01-01 · [PyPI](https://pypi.org/project/deepcomparer/)

<details><summary>README extract</summary>

Deep compare python objects and structures like dictionaries, lists and iterables.

Example:
```python
from deepcomparer import deep_compare

class Pokemon:
    def init(self, name):
        self.name = name

user: dict = {
    'name': 'ash',
    'links': {
        'pokehub': '@ash'
    },
    'pokemons': [Pokemon('pikachu')]
}

user2: dict = {
    'name': 'ash',
    'links': {
        'pokehub': '@ash'
    },
    'pokemons': [Pokemon('geodude')]
}
...
```

Sections: Deepcomparer, Getting Started, Usage

</details>

### django-admin-data-views

Add custom data views to django admin panel.

`pip install django-admin-data-views` · installs (wheel) · licence: MIT · rank 14892 · last release 2026-10-09 · [PyPI](https://pypi.org/project/django-admin-data-views/) · [docs](https://mrthearman.github.io/django-admin-data-views) · [source](https://github.com/MrThearMan/django-admin-data-views)

<details><summary>README extract</summary>

[][coverage]
[][status]
[][pypi]
[][licence]
[][repo]
[][issues]
[][pypi]

[][pypi]
[][pypi]

Documentation:

Source Code:

Contributing:

Django Admin Data Views enables you to easily add non-model data to the django admin panel.
Data from an API or file can be shown in similar table and item views than regular models.

</details>

### datetime-truncate

Truncate datetime objects to a set level of precision

`pip install datetime-truncate` · installs (wheel) · licence: BSD License · rank 14896 · last release 2020-08-06 · [PyPI](https://pypi.org/project/datetime-truncate/)

<details><summary>README extract</summary>

This module truncates a datetime object to the level of precision that
you specify, making everything higher than that zero (or one for day
and month).

It is based on PostgreSQL's DATE_TRUNC.

Documentation available on Read the Docs.

Example:
```python
>>> from datetime_truncate import truncate
>>> truncate(datetime(2012, 2, 4, 12, 24, 50, 234), 'second')
datetime(2012, 2, 4, 12, 24, 50)
>>> truncate(datetime(2012, 2, 4, 12, 24, 50), 'minute')
datetime(2012, 2, 4, 12, 24)
>>> truncate(datetime(2012, 2, 4, 12, 24), 'hour')
datetime(2012, 2, 4, 12)
>>> truncate(datetime(2012, 2, 4, 12, 24), 'day')
...
```

Sections: datetime_truncate, Usage

</details>

### dump-env

A utility tool to create .env files

`pip install dump-env` · installs (wheel) · licence: MIT License · rank 14912 · last release 2026-09-01 · [PyPI](https://pypi.org/project/dump-env/) · [source](https://github.com/wemake-services/dump-env)

<details><summary>README extract</summary>

`dump-env` takes an `.env.template` file and some optional environmental variables to create a new `.env` file from these two sources. No external dependencies are used.

Features:
Why do we need such a tool? Well, this tool is very helpful when your CI is building `docker` (or other) images.
Previously we had some complex logic of encrypting and decrypting files, importing secret keys and so on. ...

Sections: A utility tool to create ``.env`` files, Why?, Quickstart, Advanced Usage, Multiple prefixes, Strict env variables, Source templates, Strict Source, Unquoted values, Interpolation, Creating secret variables in some CIs, Real-world usages, Related

</details>

### django-bleach

Easily use bleach with Django models and templates

`pip install django-bleach` · installs (wheel) · licence: MIT License · rank 14976 · last release 2023-08-05 · [PyPI](https://pypi.org/project/django-bleach/) · [docs](https://django-bleach.readthedocs.io/) · [source](https://github.com/marksweb/django-bleach)

<details><summary>README extract</summary>

Bleach is a Python module that takes any HTML input, and returns
valid, sanitised HTML that contains only an allowed subset of HTML tags,
attributes and styles. `django-bleach` is a Django app that makes using
`bleach` extremely easy.

Read the documentation here.

1. Install `django-bleach` via `pip`:
2. ...

Example:
```python
# in app/models.py

from django import models
from django_bleach.models import BleachField

class Post(models.Model):

    title = models.CharField()
    content = BleachField()

    # ...
```

Sections: django-bleach - Bleach and sanitise user HTML, Setup, Usage, In your models, In your forms, In your templates

</details>

### dictknife

utility set of handling dict

`pip install dictknife` · installs (wheel) · licence: MIT · rank 14994 · last release 2025-07-05 · [PyPI](https://pypi.org/project/dictknife/) · [docs](http://dictknife.readthedocs.io) · [source](https://github.com/podhmo/dictknife)

<details><summary>README extract</summary>

swiss army knife for handling dict.

Sections: dictknife, examples, doc

</details>

