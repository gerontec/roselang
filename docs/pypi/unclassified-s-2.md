# Unclassified / S (part 2 of 2)

[Index](README.md) · 537 packages in this topic, by downloads.

[part 1](unclassified-s.md) · part 2

### surge-api

Surge Python SDK

`pip install surge-api` · installs (wheel) · licence: MIT · rank 13212 · last release 2026-11-06 · [PyPI](https://pypi.org/project/surge-api/)

<details><summary>README extract</summary>

The Surge Python SDK provides convenient access to the Surge API from applications written in the Python language.

Example:
```python
import surge
surge.api_key = "YOUR API KEY"
```

Sections: Surge Python SDK, Requirements, Usage, Authentication, Downloading project results, Creating projects, Creating tasks

</details>

### sarif-pydantic

(no summary)

`pip install sarif-pydantic` · installs (wheel) · licence: not stated · rank 13261 · last release 2025-11-04 · [PyPI](https://pypi.org/project/sarif-pydantic/)

<details><summary>README extract</summary>

An implementation of the SARIF (Static Analysis Results Interchange Format) format using Pydantic.

Features:
This library provides Pydantic models for working with the SARIF specification (version 2.1.0). It enables Python developers to:

- Create, validate, and manipulate SARIF data
- Parse existing SARIF files into typed Python objects ...

Example:
```python
from sarif_pydantic import (
    ArtifactLocation,
    Invocation,
    Level,
    Location,
    Message,
    PhysicalLocation,
    Region,
    Result,
    Run,
    Sarif,
    Tool,
    ToolDriver
)

# Create a tool driver
tool_driver = ToolDriver(
    name="Example Analyzer",
    version="1.0.0",
)

# Create a tool with the driver
...
```

...

</details>

### saltext.vault

Salt Extension for interacting with Vault (or OpenBao)

`pip install saltext.vault` · installs (wheel) · licence: Apache Software License · rank 13277 · last release 2026-08-09 · [PyPI](https://pypi.org/project/saltext.vault/) · [docs](https://salt-extensions.github.io/saltext-vault/) · [source](https://github.com/salt-extensions/saltext-vault)

<details><summary>README extract</summary>

Salt Extension for interacting with Vault (or OpenBao)

Sections: Salt Extension for HashiCorp Vault, User Documentation, Quickstart, Automatic, Manual, Pull request

</details>

### structlog-pretty

A collection of structlog processors for prettier output

`pip install structlog-pretty` · installs (wheel) · licence: MIT License · rank 13316 · last release 2024-07-15 · [PyPI](https://pypi.org/project/structlog-pretty/)

<details><summary>README extract</summary>

A collection of structlog processors for prettier output: a code syntax
highlighter, JSON and XML prettifiers, a multiline string printer, and
a numeric value rounder.

Example:
```python
import structlog
import structlog_pretty

structlog.configure(
    # ...
    processors=[
        structlog.stdlib.add_log_level,
        structlog_pretty.NumericRounder(digits=2, only_fields=['timing'])
        structlog.processors.JSONRenderer(),
    ],
)
```

Sections: structlog-pretty, Usage

</details>

### streamlit-js-eval

A custom Streamlit component to evaluate arbitrary Javascript expressions.

`pip install streamlit-js-eval` · installs (wheel) · licence: not stated · rank 13337 · last release 2026-01-09 · [PyPI](https://pypi.org/project/streamlit-js-eval/)

<details><summary>README extract</summary>

SJE is a custom Streamlit component, built to evaluate arbitrary Javascript expressions and return the result. It can become useful in doing certain functionalities which are _simple_ things in JavaScript, but unavailable or difficult to do in Streamlit. Examples include cookie management, writing to clipboard, getting device width (e.g. ...

Example:
```python
st.write(f"Screen width is {streamlit_js_eval(js_expressions='screen.width', key = 'SCR')}")
```

Sections: Streamlit-JS-Eval, Example, Common JavaScript functionalities, Handling Geolocation Errors, Known Limitations

</details>

### sendgrid-python

SendGrid client

`pip install sendgrid-python` · installs from source (sdist only) · licence: LICENSE.txt · rank 13399 · last release 2012-06-28 · [PyPI](https://pypi.org/project/sendgrid-python/)

### seeq-spy

Easy-to-use Python interface for Seeq

`pip install seeq-spy` · installs (wheel) · licence: Other/Proprietary License · rank 13468 · last release 2026-11-04 · [PyPI](https://pypi.org/project/seeq-spy/) · [docs](https://python-docs.seeq.com/)

<details><summary>README extract</summary>

The seeq-spy Python module is the recommended programming interface for interacting with the Seeq Server.

Use of this module requires a
Seeq Data Lab license.

Documentation can be found at

The Seeq SPy module is a friendly set of functions that are optimized for use with
Jupyter, Pandas and NumPy. ...

Example:
```python
from seeq import spy
spy.docs.copy()
```

</details>

### smooch

Smooch

`pip install smooch` · installs (wheel) · licence: not stated · rank 13576 · last release 2021-03-04 · [PyPI](https://pypi.org/project/smooch/)

<details><summary>README extract</summary>

The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our official documentation.

</details>

### stackit-core

Core functionality for the STACKIT SDK for Python

`pip install stackit-core` · installs (wheel) · licence: Apache Software License · rank 13612 · last release 2026-11-05 · [PyPI](https://pypi.org/project/stackit-core/)

<details><summary>README extract</summary>

> ⓘ INFO: The STACKIT Python SDK is in beta and in active development.

The STACKIT Python core package consists of core functionality which is needed
to use the STACKIT Python SDK.

Sections: STACKIT Python SDK Core, Introduction, Usage

</details>

### sdp-transform

A simple Python parser and writer of SDP.

`pip install sdp-transform` · installs (wheel) · licence: MIT License · rank 13615 · last release 2024-05-06 · [PyPI](https://pypi.org/project/sdp-transform/)

### storage

Libraries to interact with Enterprise Storage Arrays, FC Switches and Servers.

`pip install storage` · installs from source (sdist only) · licence: LICENSE.txt · rank 13639 · last release 2013-05-20 · [PyPI](https://pypi.org/project/storage/)

<details><summary>README extract</summary>

Storage library provides python classes/functions to interact with Enterprise Storage Arrays, FC Switches and Servers.

Visit to view documentation, report bugs and obtain help.

Sections: Storage, Documentation

</details>

### strictdoc

StrictDoc is open-source software for technical documentation and requirements management.

`pip install strictdoc` · installs (wheel) · licence: Apache-2.0 · rank 13655 · last release 2026-10-22 · [PyPI](https://pypi.org/project/strictdoc/) · [source](https://github.com/strictdoc-project/strictdoc)

<details><summary>README extract</summary>

StrictDoc is open-source software for technical documentation and requirements
management.

The main StrictDoc documentation is hosted on Read the Docs:

The documentation is hosted on Read the Docs:
StrictDoc documentation.

For a quick visual overview, see the
StrictDoc project slide deck.

Sections: StrictDoc, Documentation, Quick start, Project links

</details>

### solara-ui

(no summary)

`pip install solara-ui` · installs (wheel) · licence: MIT License · rank 13670 · last release 2026-11-07 · [PyPI](https://pypi.org/project/solara-ui/) · [docs](https://solara.dev)

<details><summary>README extract</summary>

A Pure Python, React-style Framework for Scaling Your Jupyter and Web Apps

Come chat with us on Discord to ask questions or share your thoughts or creations!

While there are many Python web frameworks out there, most are designed for small data apps or use paradigms unproven for larger scale. ...

Example:
```python
import solara

# Declare reactive variables at the top level. Components using these variables
# will be re-executed when their values change.
sentence = solara.reactive("Solara makes our team more productive.")
word_limit = solara.reactive(10)

@solara.component
def Page():
...
```

Sections: Introducing Solara, First script, Demo, Running in solara-server, Running in Jupyter, Resources

</details>

### Shimmy

An API conversion tool providing Gymnasium and PettingZoo bindings for popular external reinforcement learning environments.

`pip install Shimmy` · installs (wheel) · licence: MIT License · rank 13683 · last release 2026-04-10 · [PyPI](https://pypi.org/project/Shimmy/)

<details><summary>README extract</summary>

Shimmy is an API conversion tool providing Gymnasium and PettingZoo bindings for popular external reinforcement learning environments.

The documentation website is at shimmy.farama.org and we have a public discord server (which we also use to coordinate development work) that you can join here:

</details>

### stdeb

Python to Debian source package conversion utility

`pip install stdeb` · installs (wheel) · licence: MIT License · rank 13693 · last release 2025-09-12 · [PyPI](https://pypi.org/project/stdeb/)

<details><summary>README extract</summary>

stdeb produces Debian source
packages from Python packages via a new distutils command,
`sdist_dsc`. Automatic defaults are provided for the Debian package,
but many aspects of the resulting package can be customized (see the
customizing section, below). An additional command, `bdist_deb`,
creates a Debian binary package, a .deb file. ...

Features:
* Create a package for all Python versions supported by
 python-support. (Limiting this range is possible with the
 `XS-Python-Version:` config option.)

* Automatic conversion of Python package names into valid Debian
 package names. ...

...

</details>

### sagemaker-experiments

Open source library for Experiment Tracking in SageMaker Jobs and Notebooks

`pip install sagemaker-experiments` · installs (wheel) · licence: Apache Software License · rank 13695 · last release 2023-05-17 · [PyPI](https://pypi.org/project/sagemaker-experiments/)

<details><summary>README extract</summary>

NOTE: Use the SageMaker SDK to use SageMaker Experiments. This repository will not be up to date with the latest product improvements. Link to developer guide.

Experiment tracking in SageMaker Training Jobs, Processing Jobs, and Notebooks.

Features:
SageMaker Experiments is an AWS service for tracking machine learning Experiments. The SageMaker Experiments Python SDK is a high-level interface to this service that helps you track Experiment information using Python. ...

Example:
```python
import boto3
import pickle, gzip, numpy, json, os
import io
import numpy as np
import sagemaker.amazon.common as smac
import sagemaker
from sagemaker import get_execution_role
from sagemaker import analytics
from smexperiments import experiment

# Specify training container
...

</details>

### stjames

structured JSON atom/molecule encoding scheme

`pip install stjames` · installs (wheel) · licence: MIT · rank 13699 · last release 2026-10-28 · [PyPI](https://pypi.org/project/stjames/)

<details><summary>README extract</summary>

This is the Rowan schema for passing molecule/calculation data back and forth between different parts of the software.

This is not intended to be run as a standalone library: it's basically just a big composite Pydantic model which does some validation and intelligent default selection. ...

Sections: stjames, STructured JSON Atom/Molecule Encoding Scheme

</details>

### sqlframe

Turning PySpark Into a Universal DataFrame API

`pip install sqlframe` · installs (wheel) · licence: MIT License · rank 13744 · last release 2026-11-05 · [PyPI](https://pypi.org/project/sqlframe/)

<details><summary>README extract</summary>

Run the PySpark DataFrame API directly on your database.
No Spark cluster required.

 Quickstart ·
 Documentation ·
 Report an issue

Features:
- Familiar API. Write transformations with PySpark DataFrame operations, joins, and window functions.
- Direct execution. Run your transformations on your database engine.
- Visible SQL. ...

Example:
```python
from sqlframe.duckdb import DuckDBSession

session = DuckDBSession()
df = session.createDataFrame(
    [("US", 120), ("UK", 80), ("US", 30)],
    ["country", "revenue"],
)
df.groupBy("country").sum("revenue").orderBy("country").show()
```

Sections: Your PySpark code. Your database., Why SQLFrame?, Try it locally, Choose your engine, Already using PySpark?, Keep exploring

</details>

### style

🌈 Terminal string styling

`pip install style` · installs (wheel) · licence: MIT License · rank 13781 · last release 2019-03-08 · [PyPI](https://pypi.org/project/style/)

<details><summary>README extract</summary>

style is a simple terminal string styling package. Its API is a port of the popular
chalk package for javascript.

Example:
```python
import style

print(style.red('Hello', style.bold('world') + '!'))
```

Sections: style, Usage, API, style.\ `style*.style`, style.\ `enabled`, Styles

</details>

### sumologic-sdk

Sumo Logic Python SDK

`pip install sumologic-sdk` · installs (wheel) · licence: not stated · rank 13810 · last release 2026-09-02 · [PyPI](https://pypi.org/project/sumologic-sdk/)

<details><summary>README extract</summary>

Community-supported Python interface to the Sumo Logic REST API. The idea is to make it easier to
hit the API in Python code. Sample scripts available in the `scripts` folder. Please submit issues
here via Github. Do not submit customer issues to Sumo Logic support (but REST API issues are of
course supported). ...

Sections: Sumo Logic Python SDK, TLS 1.2 Requirement, How to use / examples

</details>

### sonora

A WSGI and ASGI compatible grpc-web implementation.

`pip install sonora` · installs (wheel) · licence: Apache Software License · rank 13814 · last release 2023-08-23 · [PyPI](https://pypi.org/project/sonora/)

### stdiomask

A cross-platform Python module for entering passwords to a stdio terminal and displaying a **** mask, which getpass cannot do.

`pip install stdiomask` · installs from source (sdist only) · licence: GNU General Public License v3 or later (GPLv3+) · rank 13846 · last release 2020-10-11 · [PyPI](https://pypi.org/project/stdiomask/)

_README extract left out: share-alike licence._

### stubs

Tools for setting up stubs and mocks.

`pip install stubs` · installs (wheel) · licence: Apache Software License · rank 13932 · last release 2016-10-31 · [PyPI](https://pypi.org/project/stubs/)

### solara

(no summary)

`pip install solara` · installs (wheel) · licence: MIT License · rank 13938 · last release 2026-11-07 · [PyPI](https://pypi.org/project/solara/) · [docs](https://solara.dev)

<details><summary>README extract</summary>

A Pure Python, React-style Framework for Scaling Your Jupyter and Web Apps

Come chat with us on Discord to ask questions or share your thoughts or creations!

While there are many Python web frameworks out there, most are designed for small data apps or use paradigms unproven for larger scale. ...

Example:
```python
import solara

# Declare reactive variables at the top level. Components using these variables
# will be re-executed when their values change.
sentence = solara.reactive("Solara makes our team more productive.")
word_limit = solara.reactive(10)

@solara.component
def Page():
...
```

Sections: Introducing Solara, First script, Demo, Running in solara-server, Running in Jupyter, Resources

</details>

### scrublet

Doublet prediction in single-cell RNA-sequencing data

`pip install scrublet` · installs (wheel) · licence: not stated · rank 13946 · last release 2020-12-29 · [PyPI](https://pypi.org/project/scrublet/)

<details><summary>README extract</summary>

Single-Cell Remover of Doublets

Python code for identifying doublets in single-cell RNA-seq data. For details and validation of the method, see our paper in Cell Systems or the preprint on bioRxiv.

Example:
```python
import scrublet as scr
scrub = scr.Scrublet(counts_matrix)
doublet_scores, predicted_doublets = scrub.scrub_doublets()
```

Sections: Scrublet, Quick start, Best practices, Old versions, Other doublet detection tools

</details>

### sqlalchemy-migrate

Database schema migration for SQLAlchemy

`pip install sqlalchemy-migrate` · installs (wheel) · licence: Apache Software License · rank 13992 · last release 2019-10-22 · [PyPI](https://pypi.org/project/sqlalchemy-migrate/)

<details><summary>README extract</summary>

Fork from to get it working with
SQLAlchemy 0.8.

Inspired by Ruby on Rails' migrations, Migrate provides a way to deal with
database schema changes in SQLAlchemy projects.

Migrate extends SQLAlchemy to have database changeset handling. ...

Sections: SQLAlchemy Migrate, Help, Tests and Bugs

</details>

### syntok

Text tokenization and sentence segmentation (segtok v2).

`pip install syntok` · installs (wheel) · licence: MIT License · rank 14002 · last release 2022-03-12 · [PyPI](https://pypi.org/project/syntok/)

<details><summary>README extract</summary>

(a.k.a. segtok v2)

The syntok package provides two modules, `syntok.segmenter` and `syntok.tokenizer`.
The tokenizer provides functionality for splitting (Indo-European) text into words and symbols (collectively called *tokens*). ...

Example:
```python
from syntok.tokenizer import Tokenizer

document = open('README.rst').read()
tok = Tokenizer()  # optional: keep "n't" contractions and "-", "_" inside words as tokens

for token in tok.tokenize(document):
    print(repr(token))
```

Sections: syntok, Sentence segmentation and word tokenization, `segtok`, Usage, Command-line, `syntok.tokenizer`, `syntok.segmenter`, Legal

</details>

### spatialdata-plot

Static plotting for spatial data.

`pip install spatialdata-plot` · installs (wheel) · licence: not stated · rank 14019 · last release 2026-10-09 · [PyPI](https://pypi.org/project/spatialdata-plot/) · [docs](https://spatialdata.scverse.org/projects/plot/en/latest/index.html) · [source](https://github.com/scverse/spatialdata-plot.git)

<details><summary>README extract</summary>

[][link-tests]
[][link-docs]
[][link-codecov]
[][link-pypi]

The `spatialdata-plot` package extends `spatialdata` with a declarative plotting API that enables to quickly visualize `spatialdata` objects and their respective elements (i.e. `images`, `labels`, `points` and `shapes`). ...

Sections: Getting started, Contact

</details>

### sdmetrics

Metrics for Synthetic Data Generation Projects

`pip install sdmetrics` · installs (wheel) · licence: MIT · rank 14020 · last release 2026-10-29 · [PyPI](https://pypi.org/project/sdmetrics/) · [source](https://github.com/sdv-dev/SDMetrics)

<details><summary>README extract</summary>

This repository is part of The Synthetic Data Vault Project, a project from DataCebo.

Features:
The SDMetrics library evaluates synthetic data by comparing it to the real data that you're trying to mimic. It includes a variety of metrics to capture different aspects of the data, for example quality and privacy. ...

Example:
```python
from sdmetrics import load_demo
from sdmetrics.reports.single_table import QualityReport

real_data, synthetic_data, metadata = load_demo(modality='single_table')

my_report = QualityReport()
my_report.generate(real_data, synthetic_data, metadata)
```

Sections: Overview, Usage, What's next?

</details>

### starknet-py

A python SDK for Starknet

`pip install starknet-py` · installs from source (sdist only) · licence: MIT · rank 14042 · last release 2026-04-16 · [PyPI](https://pypi.org/project/starknet-py/) · [docs](https://starknetpy.rtfd.io/) · [source](https://github.com/software-mansion/starknet.py)

<details><summary>README extract</summary>

- Installation
- Quickstart
- Guide
- API
- Migration guide

Example:
```python
from starknet_py.net.full_node_client import FullNodeClient

node_url = "
client = FullNodeClient(node_url=node_url)

call_result = await client.get_block(block_number=1)
```

Sections: Starknet SDK for Python, 📘 Documentation, 💨 Quickstart, Using FullNodeClient, Creating Account, Using Account, Using Contract

</details>

### stackit-iaas

IaaS-API

`pip install stackit-iaas` · installs (wheel) · licence: Apache Software License · rank 14046 · last release 2026-11-03 · [PyPI](https://pypi.org/project/stackit-iaas/)

<details><summary>README extract</summary>

This API allows you to create and modify IaaS resources.

For more information, please visit

This package is part of the STACKIT Python SDK. For additional information, please visit the GitHub repository of the SDK.

Sections: stackit.iaas, Getting Started

</details>

### stackit-resourcemanager

Resource Manager API

`pip install stackit-resourcemanager` · installs (wheel) · licence: Apache Software License · rank 14054 · last release 2026-11-03 · [PyPI](https://pypi.org/project/stackit-resourcemanager/)

<details><summary>README extract</summary>

API v2 to manage resource containers - organizations, folders, projects incl. labels

STACKIT resource management handles the terms _Organization_, _Folder_, _Project_, _Label_, and the hierarchical structure between them. Technically, organizations,
folders, and projects are _Resource Containers to which a _Label_ can be attached to. ...

Sections: stackit.resourcemanager, Resource Management, Organizations, Projects, Label, Getting Started

</details>

### shutils

Tools for python development.

`pip install shutils` · installs from source (sdist only) · licence: MIT · rank 14103 · last release 2020-05-01 · [PyPI](https://pypi.org/project/shutils/)

### stackit-objectstorage

STACKIT Object Storage API

`pip install stackit-objectstorage` · installs (wheel) · licence: Apache Software License · rank 14122 · last release 2026-11-03 · [PyPI](https://pypi.org/project/stackit-objectstorage/)

<details><summary>README extract</summary>

STACKIT API to manage the Object Storage

This package is part of the STACKIT Python SDK. For additional information, please visit the GitHub repository of the SDK.

Sections: stackit.objectstorage, Getting Started

</details>

### sleipnirgroup-jormungandr

Reverse mode autodiff library and NLP solver DSL

`pip install sleipnirgroup-jormungandr` · installs (wheel) · licence: BSD-3-Clause · rank 14144 · last release 2026-09-05 · [PyPI](https://pypi.org/project/sleipnirgroup-jormungandr/) · [docs](https://sleipnirgroup.github.io/Sleipnir/)

<details><summary>README extract</summary>

Sleipnir is a reverse mode autodiff library, interior-point method, and NLP solver DSL for C++23 and Python. The DSL automatically chooses the best solver based on the problem structure. ...

Example:
```python
# !/usr/bin/env python

from sleipnir.optimization import Problem

def main():
    # Find the x, y pair with the largest product for which x + 3y = 36
    problem = Problem()

    x, y = problem.decision_variable(2)

    problem.maximize(x * y)
    problem.subject_to(x + 3 * y == 36)
    problem.solve()

    # x = 18.0, y = 6.0
...
```

Sections: Sleipnir, Docs, Examples, Benchmarks

</details>

### sample-helper-aws-appconfig

Sample helper library for AWS AppConfig

`pip install sample-helper-aws-appconfig` · installs (wheel) · licence: OSI Approved; Other/Proprietary License · rank 14149 · last release 2026-05-18 · [PyPI](https://pypi.org/project/sample-helper-aws-appconfig/) · [source](https://github.com/aws-samples/sample-python-helper-aws-appconfig)

<details><summary>README extract</summary>

A sample helper Python library for AWS AppConfig which makes rolling configuration updates out easier.

Features:
* Configurable update interval: you can ask the library to update your configuration as often as needed, but it will only call the AWS AppConfig API at the configured interval (in seconds). ...

Example:
```python
from appconfig_helper import AppConfigHelper
from fastapi import FastAPI

appconfig = AppConfigHelper(
    "MyAppConfigApp",
    "MyAppConfigEnvironment",
    "MyAppConfigProfile",
    45  # minimum interval between update checks
)

app = FastAPI()

@app.get("/some-url")
def index():
    if appconfig.update_config():
...
```

Sections: Sample AWS AppConfig Helper, Features, Example, Usage, Initialising, Reading the configuration, Use in AWS Lambda

</details>

### simplekv

A key-value storage for binary data, support many backends.

`pip install simplekv` · installs (wheel) · licence: MIT · rank 14175 · last release 2020-04-09 · [PyPI](https://pypi.org/project/simplekv/)

<details><summary>README extract</summary>

*simplekv* is an API for very basic key-value stores used for small, frequently
accessed data or large binary blobs. Its basic interface is easy to implement
and it supports a number of backends, including the filesystem, SQLAlchemy,
MongoDB, Redis and Amazon S3/Google Storage.

Sections: simple key-value storage api, Documentation

</details>

### spgci

SPGCI is an API Client for the S&P Commodity Insights REST API

`pip install spgci` · installs (wheel) · licence: Apache Software License · rank 14195 · last release 2026-10-28 · [PyPI](https://pypi.org/project/spgci/) · [docs](https://developer.spglobal.com/commodityinsights/tools/notebooks) · [source](https://github.com/spgi-ci/spgci-python)

<details><summary>README extract</summary>

Python Client for the S&P Global Commodity Insights API.

Looking for more examples? Check out our Notebook Gallery.

Features:
- Automatically generates token prior to making request.
- Returns data as a pandas DataFrame (set `raw=False` to get the raw `request.response` object). ...

Example:
```python
import spgci as ci

ci.set_credentials(<username>, <password>)
mdd = ci.MarketData()

symbols = ["PCAAS00", "PCAAT00"]
mdd.get_assessments_by_symbol_current(symbol=symbols)
```

Sections: SPGCI Python Library, Getting Started, #, Features, Market Data, Forward Curves, Energy Price Forecast, EWindow Market Data, World Oil Supply, World Refinery Database, Insights, Global Integrated Energy Model (Deprecated), Refining Margins & Crude Arbitrage, LNG Global Analytics

</details>

### sogen

Sogen Windows user-space emulator bindings

`pip install sogen` · installs from source (sdist only) · licence: GNU General Public License v2 (GPLv2) · rank 14263 · last release 2026-11-08 · [PyPI](https://pypi.org/project/sogen/)

_README extract left out: share-alike licence._

### sceptre

An AWS Cloud Provisioning Tool

`pip install sceptre` · installs (wheel) · licence: Apache Software License · rank 14278 · last release 2026-05-22 · [PyPI](https://pypi.org/project/sceptre/) · [docs](https://docs.sceptre-project.org) · [source](https://github.com/Sceptre/sceptre)

<details><summary>README extract</summary>

Sceptre is a tool to drive
AWS CloudFormation. It automates the
mundane, repetitive and error-prone tasks, enabling you to concentrate on
building better infrastructure.

Features:
- Code reuse by separating a Stack's template and its configuration
- Support for templates written in JSON, YAML, Jinja2 or Python DSLs such as
 Troposphere
- Dependency resolution by passing of Stack outputs to parameters of dependent
 Stacks ...

Example:
```python
from sceptre.context import SceptreContext
from sceptre.plan.plan import SceptrePlan

context = SceptreContext("/path/to/project", "command_path")
plan = SceptrePlan(context)
plan.launch()
```

...

</details>

### secscanner2junit

Convert Security Scanner Output to JUnit Format

`pip install secscanner2junit` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 14314 · last release 2025-02-08 · [PyPI](https://pypi.org/project/secscanner2junit/) · [source](https://github.com/logchange/SecScanner2JUnit)

_README extract left out: share-alike licence._

### st-attn

Sliding Tile Atteniton Kernel Used in FastVideo

`pip install st-attn` · does not install on CPython 3.14 · licence: Apache Software License · rank 14318 · last release 2025-11-13 · [PyPI](https://pypi.org/project/st-attn/)

### streamlit-tour

Streamlit component that implement the wonderful Driver.js library. It allows you to start a tour that takes the user through the component that you want

`pip install streamlit-tour` · installs (wheel) · licence: BSD-3-Clause · rank 14360 · last release 2026-04-09 · [PyPI](https://pypi.org/project/streamlit-tour/) · [source](https://github.com/mp-mech-ai/streamlit_tour)

<details><summary>README extract</summary>

A Driver.js integration for Streamlit - add beautiful, interactive guided tours to your Streamlit apps with a single Python call.

<!-- Replace the line below with your actual GIF -->

Features:
- :link: Bind tour steps to any Streamlit widget by its `key`
- :window: Element-free info steps - show contextual popups not anchored to any component ...

Example:
```python
import streamlit as st
from streamlit_tour import Tour

st.title("My App")
st.text_input("Name", key="name_input")

tour = Tour(
    steps=[
        Tour.bind("name_input", title="Your Name", desc="Enter your name here."),
        Tour.info(title="That's it!", desc="You're ready to go."),
    ]
)

tour.start()
```

...

</details>

### stonefish-license-manager

(no summary)

`pip install stonefish-license-manager` · installs (wheel) · licence: LicenseRef-MIT-no-modify · rank 14366 · last release 2026-11-02 · [PyPI](https://pypi.org/project/stonefish-license-manager/)

### snakefmt

The uncompromising Snakemake code formatter

`pip install snakefmt` · installs (wheel) · licence: MIT · rank 14387 · last release 2026-10-14 · [PyPI](https://pypi.org/project/snakefmt/) · [docs](https://github.com/snakemake/snakefmt/blob/master/README.md) · [source](https://github.com/snakemake/snakefmt)

<details><summary>README extract</summary>

This repository provides formatting for Snakemake files. It follows the
design and specifications of Black.

> [!WARNING]
> `snakefmt` modifies files in-place by default, thus we strongly
> recommend ensuring your files are under version control before doing any formatting. ...

Example:
```python
from snakemake.utils import min_version
min_version("5.14.0")
configfile: "config.yaml" # snakemake keywords are treated like classes i.e. 2 newlines
SAMPLES = ['s1', 's2'] # strings are normalised
CONDITIONS = ["a", "b", "longlonglonglonglonglonglonglonglonglonglonglonglonglonglonglong"] # long lines are wrapped
...
```

...

</details>

### stemming

(no summary)

`pip install stemming` · installs from source (sdist only) · licence: not stated · rank 14416 · last release 2010-12-20 · [PyPI](https://pypi.org/project/stemming/)

### selectors2

Back-ported, durable, and portable selectors

`pip install selectors2` · installs (wheel) · licence: MIT License; Python Software Foundation License · rank 14433 · last release 2020-07-21 · [PyPI](https://pypi.org/project/selectors2/)

<details><summary>README extract</summary>

Backported, durable, and portable selectors designed to replace
the standard library selectors module.

Features:
* Support for all major platforms. (Linux, Mac OS, Windows)
* Support for Python 2.6 or later and Jython.
* Support many different selectors
 * `select.kqueue` (BSD, Mac OS)
 * `select.devpoll` (Solaris)
 * `select.epoll` (Linux 2.5.44+)
 * ...

Example:
```python
import sys
import selectors2 as selectors

# Use DefaultSelector, it picks the best
# selector available for your platform! :)
s = selectors.DefaultSelector()

import socket

# We're going to use Google as an example.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.google.com", 80))

...
```

...

</details>

### sid-sdk

Context-management primitives for rendering search results and tracking document spans shown to language models

`pip install sid-sdk` · installs (wheel) · licence: MIT · rank 14522 · last release 2026-10-08 · [PyPI](https://pypi.org/project/sid-sdk/) · [docs](https://github.com/sidhq/sid-python#readme) · [source](https://github.com/sidhq/sid-python)

<details><summary>README extract</summary>

`sid-sdk` turns search results into compact, model-facing document views. It
assigns stable short IDs, selects relevant snippets, tracks the exact character
ranges already shown, masks repeated text, and renders SID's `<doc>` format. ...

Example:
```python
from sid import DocumentCache

cache = DocumentCache(language="english")
cache.add_document(
    "database-id",
    {"title": "Example", "content": "The complete document text ..."},
)
view = cache.apply_snippet(
    "database-id",
    snippet_field="content",
    query="complete document",
)
print(view.render_xml())
cache.update_seen(view)
```

Sections: SID SDK, Basic use, Model-facing IDs, Character ranges, Rendering and forks

</details>

### SocksiPy-branch

A Python SOCKS module

`pip install SocksiPy-branch` · installs from source (sdist only) · licence: BSD · rank 14526 · last release 2010-05-26 · [PyPI](https://pypi.org/project/SocksiPy-branch/)

<details><summary>README extract</summary>

This Python module allows you to create TCP connections through a SOCKS proxy
without any special effort.

</details>

### smoldot-light

Python bindings for the smoldot_light Rust crate.

`pip install smoldot-light` · installs (wheel) · licence: not stated · rank 14536 · last release 2026-01-14 · [PyPI](https://pypi.org/project/smoldot-light/)

<details><summary>README extract</summary>

Python bindings for the `smoldot_light` Rust crate using PyO3. The goal is to run a lightweight
Polkadot client in Python and connect it to `py-polkadot-sdk`.

Features:
- Rust core: `smoldot_light` provides the light client implementation.
- Python API: `SmoldotClient` exposes JSON-RPC request/response plumbing.
- Build system: `maturin` builds and installs the extension module.

Example:
```python
from smoldot_light import SmoldotClient

client = SmoldotClient()

# Load a chain spec JSON string (Polkadot, Kusama, or a local chain).
with open("polkadot.json", "r", encoding="utf-8") as f:
    chain_spec = f.read()

relay_chain_id = client.add_chain(chain_spec)

# If you are connecting a parachain, pass the relay chain id(s).
...
```

...

</details>

### snyk-agent-scan

Agent supply chain security scanner.

`pip install snyk-agent-scan` · installs (wheel) · licence: Apache-2.0 · rank 14570 · last release 2026-11-06 · [PyPI](https://pypi.org/project/snyk-agent-scan/)

<details><summary>README extract</summary>

Discover and scan agent components on your machine for prompt injections

 and vulnerabilities (including agents, MCP servers, skills).

> Note: We don't publish an npm package for Agent Scan. Install it via `uvx` or as a standalone binary. ...

Features:
- Auto-discover MCP configurations, agent tools, skills
- Scanning of Claude, Cursor, GitHub Copilot, Windsurf, Gemini CLI, Amp, Amazon Q, and other agents.

Sections: Snyk Agent Scan, Agent Scan v0.5.x output, Agent Scan v0.6 and later output, Quick Start, Run with `uvx`, Agent Scan v0.5.x, Agent Scan v0.6 and later, Run with a standalone binary, Highlights, Detection coverage by scope, Verifying Standalone Binaries, Step-by-Step Verification Guide

</details>

### sqs-extended-client

AWS SQS extended client functionality from amazon-sqs-java-extended-client-lib

`pip install sqs-extended-client` · installs (wheel) · licence: Apache Software License · rank 14573 · last release 2023-11-17 · [PyPI](https://pypi.org/project/sqs-extended-client/)

<details><summary>README extract</summary>

Features:
sqs-extended-client allows for sending large messages through SQS via S3. This is the same mechanism that the Amazon library
amazon-sqs-java-extended-client-lib provides. This library is
interoperable with that library. ...

Example:
```python
import boto3
from botocore.config import Config
import sqs_extended_client

# Low level client
sqs = boto3.client('sqs')
sqs.large_payload_support = 'my-bucket-name'
sqs.s3 = boto3.resource(
  's3',
  config=Config(
    signature_version='s3v4',
    s3={
      "use_accelerate_endpoint": True
    }
  )
)

# boto resource
...
```

Sections: sqs-extended-client, Overview, Usage, Note, Setting a custom S3 resource

</details>

### stm32loader

Flash firmware to STM32 microcontrollers using Python.

`pip install stm32loader` · installs (wheel) · licence: GPL-3.0-or-later · rank 14579 · last release 2026-11-06 · [PyPI](https://pypi.org/project/stm32loader/)

_README extract left out: share-alike licence._

### solara-server

(no summary)

`pip install solara-server` · installs (wheel) · licence: MIT License · rank 14582 · last release 2026-11-07 · [PyPI](https://pypi.org/project/solara-server/) · [docs](https://solara.dev)

<details><summary>README extract</summary>

The solara server enables running ipywidgets based applications without a real Jupyter kernel, allowing multiple "Virtual kernels" to share the same process for better performance and scalability.

See for more details.

</details>

### sail-sdk

Deprecated: use the sail package instead. Compatibility release of the Sail Python SDK.

`pip install sail-sdk` · installs (wheel) · licence: not stated · rank 14583 · last release 2026-10-29 · [PyPI](https://pypi.org/project/sail-sdk/)

<details><summary>README extract</summary>

`sail-sdk` has been renamed to `sail`. Install
the canonical package instead:

This `sail-sdk` release is a thin redirect: it installs the matching `sail`
release for you, so you get the exact same `import sail` package and `sail` CLI. ...

Sections: sail-sdk (deprecated), Migrating

</details>

### sysrsync

Simple and safe python wrapper for calling system rsync

`pip install sysrsync` · installs (wheel) · licence: not stated · rank 14670 · last release 2023-04-24 · [PyPI](https://pypi.org/project/sysrsync/)

<details><summary>README extract</summary>

Simple and safe native rsync wrapper for Python 3

* rsync
* python 3.6+

development:

* poetry (be sure to have both poetry and pip upgraded to the latest version)

Example:
```python
import sysrsync

sysrsync.run(source='/home/user/foo.txt',
             destination='/home/server/bar')
# runs 'rsync /home/users/foo.txt /home/server/files'
```

Sections: sysrsync, Requirements, Basic rules, Usage, API

</details>

### sumolib

Python helper modules to read networks, parse output data and do other useful stuff related to the traffic simulation Eclipse SUMO

`pip install sumolib` · installs (wheel) · licence: EPL-2.0 OR GPL-2.0-or-later · rank 14681 · last release 2026-10-08 · [PyPI](https://pypi.org/project/sumolib/) · [docs](https://sumo.dlr.de/docs/) · [source](https://github.com/eclipse-sumo/sumo)

_README extract left out: share-alike licence._

### ssm-parameter-store

Add your description here

`pip install ssm-parameter-store` · installs (wheel) · licence: not stated · rank 14700 · last release 2026-08-30 · [PyPI](https://pypi.org/project/ssm-parameter-store/)

<details><summary>README extract</summary>

This is a simple Python wrapper for getting values from AWS Systems Manager
Parameter Store.

The module supports getting a single parameter, multiple parameters or all parameters matching a particular path.

All parameters are returned as a Python `dict`.

Example:
```python
from ssm_parameter_store import EC2ParameterStore

store = EC2ParameterStore()
```

Sections: SSM Parameter Store, Description, Usage, Examples, Populating Environment Variables, Related Projects

</details>

### soda-duckdb

Soda DuckDB V4

`pip install soda-duckdb` · installs (wheel) · licence: Proprietary · rank 14743 · last release 2026-11-05 · [PyPI](https://pypi.org/project/soda-duckdb/)

### streamlit-cookies-controller

Streamlit cookies controller

`pip install streamlit-cookies-controller` · installs (wheel) · licence: MIT License · rank 14756 · last release 2024-04-10 · [PyPI](https://pypi.org/project/streamlit-cookies-controller/)

<details><summary>README extract</summary>

[][pypi_link]
[][pypi_link]
[][github_link]
[][license_link]
[][issue_link]
[][pull_link]

Control client browser cookie for the site.

`streamlit-cookies-controller` let you

- get cookie(s)
- set cookie
- remove cookie

from/to the client browser.
It use universal-cookie package to access the cookies.

Example:
```python
import streamlit as st
from streamlit_cookies_controller import CookieController

st.set_page_config('Cookie QuickStart', '🍪', layout='wide')

controller = CookieController()

# Set a cookie
controller.set('cookie_name', 'testing')
st.write(st.session_state)

# Get all cookies
cookies = controller.getAll()
st.write(cookies)

# Get a cookie
...
```

...

</details>

### stigg-api-client-v2

(no summary)

`pip install stigg-api-client-v2` · installs (wheel) · licence: Other/Proprietary License · rank 14761 · last release 2026-11-05 · [PyPI](https://pypi.org/project/stigg-api-client-v2/)

<details><summary>README extract</summary>

This library provides a Python wrapper to Stigg's GraphQL API based on
the operations that are in use by the Stigg's Node.js SDK.

The ariadne-codegen code generator is used to generate a typesafe Python API client.

TBD

Example:
```python
import os
from stigg import Stigg

api_key = os.environ.get("STIGG_SERVER_API_KEY")

client = Stigg.create_async_client(api_key)
```

Sections: stigg-api-client-v2, Documentation, Usage

</details>

### stackit-ske

SKE-API

`pip install stackit-ske` · installs (wheel) · licence: Apache Software License · rank 14813 · last release 2026-11-03 · [PyPI](https://pypi.org/project/stackit-ske/)

<details><summary>README extract</summary>

The SKE API provides endpoints to create, update, delete clusters within STACKIT portal projects and to trigger further cluster management tasks.

For more information, please visit

This package is part of the STACKIT Python SDK. For additional information, please visit the GitHub repository of the SDK.

Sections: stackit.ske, Getting Started

</details>

### sphinxcontrib-drawio

Sphinx Extension to include draw.io files

`pip install sphinxcontrib-drawio` · installs (wheel) · licence: MIT License · rank 14849 · last release 2023-09-12 · [PyPI](https://pypi.org/project/sphinxcontrib-drawio/)

<details><summary>README extract</summary>

Sphinx Extension adding the `drawio-image` and `drawio-figure` directives.
These are equivalent to the standard `image` and `figure` directives, but
accept the path to a `.drawio` file and additional options to control
exporting of the diagram to a suitable image format. ...

Sections: sphinxcontrib-drawio, Options, Binary Path, Headless Mode, Default Output Format, Default Export Scale, Default Transparency, Disable Verbose Electron, Disable Shared Memory Usage, Disable GPU, No Sandbox, Usage, Format, Page Index

</details>

### synapse-s3-storage-provider

A storage provider which can fetch and store media in Amazon S3.

`pip install synapse-s3-storage-provider` · installs (wheel) · licence: Apache Software License · rank 14862 · last release 2026-08-18 · [PyPI](https://pypi.org/project/synapse-s3-storage-provider/)

<details><summary>README extract</summary>

This module can be used by synapse as a storage provider, allowing it to fetch
and store media in Amazon S3.

Usage

The `s3_storage_provider.py` should be on the PYTHONPATH when starting
synapse.

Example of entry in synapse config:

This module uses `boto3`, and so the credentials should be specified as
described here.

Regular cleanup job ...

</details>

### safeIO

Safely make I/O operations to files in Python even from multiple threads... and more!

`pip install safeIO` · installs from source (sdist only) · licence: MIT License · rank 14900 · last release 2021-02-23 · [PyPI](https://pypi.org/project/safeIO/)

<details><summary>README extract</summary>

> Safely make I/O operations to files in Python even from multiple threads... and more!

1. safeIO
2. Table of Content
3. What is it?
4. Installation
5. Objects
 - TextFile()
 - BinaryFile()
 - JSONFile()
6. Tips ...

Example:
```python
from safeIO import TextFile

f = TextFile("example.txt", blocking=False)
print(f.read()) # prints "None"
with f:
    print(f.read()) # prints the content of example.txt
with f as reading_file:
    print(reading_file.read()) # prints the content of example.txt
```

Sections: safeIO, Table of Content, What is it?, Objects, TextFile(filepath, encoding="utf-8", blocking=True), isfile, delete, rename, move, name, fileno, read, write, append

</details>

### serpy

ridiculously fast object serialization

`pip install serpy` · installs (wheel) · licence: MIT License · rank 14950 · last release 2017-11-28 · [PyPI](https://pypi.org/project/serpy/)

<details><summary>README extract</summary>

.. image::
 :target:
 :alt: Coveralls

 .. image::
 :target:
 :alt: Documentation Status

 .. image::
 :target:
 :alt: Downloads

serpy is a super simple object serialization framework built for speed.
serpy serializes complex datatypes (Django Models, custom classes, ...) to
simple native types (dicts, lists, strings, ...). ...

Example:
```python
import serpy

class Foo(object):
    """The object to be serialized."""
    y = 'hello'
    z = 9.5

    def init(self, x):
        self.x = x

class FooSerializer(serpy.Serializer):
    """The serializer schema definition."""
    # Use a Field subclass like IntField if you need more validation.
    x = serpy.IntField()
    y = serpy.Field()
...
```

...

</details>

### snownlp

Python library for processing Chinese text

`pip install snownlp` · installs from source (sdist only) · licence: MIT License · rank 14956 · last release 2015-09-27 · [PyPI](https://pypi.org/project/snownlp/)

<details><summary>README extract</summary>

SnowNLP是一个python写的类库，可以方便的处理中文文本内容，是受到了TextBlob的启发而写的，由于现在大部分的自然语言处理库基本都是针对英文的，于是写了一个方便处理中文的类库，并且和TextBlob不同的是，这里没有用NLTK，所有的算法都是自己实现的，并且自带了一些训练好的字典。注意本程序都是处理的unicode编码，所以使用时请自行decode成unicode。

~~~~{python}
from snownlp import SnowNLP

s = SnowNLP(u'这个东西真心很赞')

s.words # [u'这个', u'东西', u'真心',
 # u'很', u'赞'] ...

Features:
* 中文分词（Character-Based Generative Model）
* 词性标注（TnT 3-gram 隐马）
* 情感分析（现在训练数据主要是买卖东西时的评价，所以对其他的一些可能效果不是很好，待解决）
* 文本分类（Naive Bayes）
* 转换成拼音（Trie树实现的最大匹配）
* 繁体转简体（Trie树实现的最大匹配）
* 提取文本关键词（TextRank算法）
* 提取文本摘要（TextRank算法）
* tf，idf
* Tokenization（分割成句子）
* ...

...

</details>

### scimschema

A validator for System for Cross domain Identity Management (SCIM) responses given predefine schemas

`pip install scimschema` · installs (wheel) · licence: MIT License · rank 14957 · last release 2021-06-21 · [PyPI](https://pypi.org/project/scimschema/) · [source](https://github.com/GordonSo/scimschema)

<details><summary>README extract</summary>

Validate JSon content given a predefined set of SCIM Schemas (in JSON representation format) as specified in SCIM (supporting Python 3+).

Features:
Support for SCIM 2.0,
 - Validate SCIM Schema definition
 - Validate Model (schema) Id, Name, description, attributes
 - Validate Attribute (schema) Name, Type, Required, Canonical Values, Mutability, Returned, Uniqueness ...

Example:
```python
from scimschema import validate
from . import extension # <- this is the custom schemas define by your: see  for example

# A sample schema, like what we'd get from response.get(<scim entity url>).json()
content = {
    "schemas": ["urn:ietf:params:scim:schemas:core2:2.0:Group", "urn:huddle:params:scim:schemas:extension:2.0:SimpleAccount"],
...
```

...

</details>

### slangtorch

A package for calling Slang modules from Python and PyTorch.

`pip install slangtorch` · installs (wheel) · licence: MIT License · rank 14959 · last release 2026-07-31 · [PyPI](https://pypi.org/project/slangtorch/)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: 2024-2026 The Khronos Group, Inc.
SPDX-License-Identifier: CC-BY-4.0

This package allows you to use Slang as a language to write
PyTorch kernels.

Slang user guide:

`slangtorch` documentation:

Sections: Slang-Torch Package, Building Wheels Locally

</details>

### sockjs-tornado

SockJS python server implementation on top of Tornado framework

`pip install sockjs-tornado` · installs from source (sdist only) · licence: MIT License · rank 14983 · last release 2020-04-24 · [PyPI](https://pypi.org/project/sockjs-tornado/)

<details><summary>README extract</summary>

SockJS-tornado is a Python server side counterpart of SockJS-client browser library
running on top of Tornado framework.

Simplified echo SockJS server could look more or less like:
(Take look at examples for a complete version).

Subscribe to SockJS mailing list for discussions and support.

Example:
```python
from tornado import web, ioloop
from sockjs.tornado import SockJSRouter, SockJSConnection

class EchoConnection(SockJSConnection):
    def on_message(self, msg):
        self.send(msg)

if name == 'main':
    EchoRouter = SockJSRouter(EchoConnection, '/echo')

    app = web.Application(EchoRouter.urls)
    app.listen(9999)
...
```

Sections: SockJS-tornado server, SockJS-tornado API, Settings, Deployment, 1.0.7, 1.0.6, 1.0.2, 1.0.1, 1.0.0, 0.0.5, 0.0.4, 0.0.3, 0.0.2, 0.0.1

</details>

### soda-databricks

Soda Databricks V4

`pip install soda-databricks` · installs (wheel) · licence: Proprietary · rank 14999 · last release 2026-11-05 · [PyPI](https://pypi.org/project/soda-databricks/)

