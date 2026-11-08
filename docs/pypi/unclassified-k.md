# Unclassified / K

[Index](README.md) · 69 packages in this topic, by downloads.

### kiwisolver

A fast implementation of the Cassowary constraint solver

`pip install kiwisolver` · installs (wheel) · licence: BSD License · rank 186 · last release 2026-08-28 · [PyPI](https://pypi.org/project/kiwisolver/) · [docs](https://kiwisolver.readthedocs.io/en/latest/) · [source](https://github.com/nucleic/kiwi)

### keyring

Store and access your passwords safely.

`pip install keyring` · installs (wheel) · licence: MIT · rank 205 · last release 2025-11-16 · [PyPI](https://pypi.org/project/keyring/) · [source](https://github.com/jaraco/keyring)

<details><summary>README extract</summary>

The Python keyring library provides an easy way to access the
system keyring service from python. It can be used in any
application that needs safe password storage.

These recommended keyring backends are supported: ...

Example:
```python
>>> import keyring
>>> keyring.set_password("system", "username", "password")
>>> keyring.get_password("system", "username")
'password'
```

Sections: Compatibility - macOS, 525 for details., Using Keyring, Command-line Utility, Tab Completion, Configuring, Config file path, Config file content, Third-Party Backends, Runtime Configuration, Disabling Keyring, Altering Keyring Behavior, Using Keyring on Ubuntu 16.04, Using Keyring on headless Linux systems

</details>

### keyrings.google-artifactregistry-auth

Keyring backend for Google Auth tokens

`pip install keyrings.google-artifactregistry-auth` · installs (wheel) · licence: Apache Software License · rank 1072 · last release 2023-03-01 · [PyPI](https://pypi.org/project/keyrings.google-artifactregistry-auth/)

<details><summary>README extract</summary>

This repository contains an alternate keyring backend implementation to help with interacting with Python repositories hosted on Artifact Registry.

`keyrings.google-artifactregistry-auth` is a Python package which allows you to configure keyring to interact with Python repositories stored in Artifact Registry. ...

Sections: Artifact Registry tools for Python, Authentication, Usage with other tools, Usage with `tox`

</details>

### kaleido

Plotly graph export library

`pip install kaleido` · installs (wheel) · licence: not stated · rank 1259 · last release 2026-10-06 · [PyPI](https://pypi.org/project/kaleido/) · [source](https://github.com/plotly/kaleido)

<details><summary>README extract</summary>

Features:
Kaleido is a cross-platform Python library for generating static images
(e.g. png, svg, pdf, etc.) for Plotly.js, to be used by Plotly.py.

Example:
```python
import asyncio
import kaleido
import plotly.express as px

async def main():
    # n is number of processes
    async with kaleido.Kaleido(n=4, timeout=90) as k:
        # fig is a plotly figure object
        fig = px.scatter(x=[1, 2, 3, 4], y=[2, 1, 4, 3])
        await k.write_fig(fig, path="./", opts={"format": "jpg"})

...
```

Sections: Overview, Migrating from v0 to v1, Usage examples, PageGenerators

</details>

### kestra

Kestra is an infinitely scalable orchestration and scheduling platform, creating, running, scheduling, and monitoring millions of complex pipelines.

`pip install kestra` · installs (wheel) · licence: Apache Software License · rank 1854 · last release 2026-09-07 · [PyPI](https://pypi.org/project/kestra/) · [source](https://github.com/kestra-io/libs)

<details><summary>README extract</summary>

This Python client provides functionality to interact with the Kestra server for sending metrics, outputs, and logs, as well as executing/polling flows.

Example:
```python
from kestra import Flow
flow = Flow()
flow.execute('mynamespace', 'myflow', {'param': 'value'})
```

Sections: Kestra Python Client, Kestra Class, Methods, Flow Class, Initialization, Usage Examples, Error Handling, Logging, Outputs, Counters, Timers, Gauges

</details>

### knack

A Command-Line Interface framework

`pip install knack` · installs (wheel) · licence: MIT License · rank 2214 · last release 2026-05-14 · [PyPI](https://pypi.org/project/knack/)

<details><summary>README extract</summary>

pip install -r requirements.txt
pip install -e .
pip install tox
tox

</details>

### kfp-pipeline-spec

Kubeflow Pipelines pipeline spec

`pip install kfp-pipeline-spec` · installs (wheel) · licence: Apache 2.0 · rank 2697 · last release 2026-10-28 · [PyPI](https://pypi.org/project/kfp-pipeline-spec/)

### keyrings.codeartifact

Automatically retrieve credentials for AWS CodeArtifact.

`pip install keyrings.codeartifact` · installs (wheel) · licence: not stated · rank 2703 · last release 2025-07-01 · [PyPI](https://pypi.org/project/keyrings.codeartifact/) · [source](https://github.com/jmkeyes/keyrings.codeartifact.git)

<details><summary>README extract</summary>

The `keyrings.codeartifact` package provides authentication for publishing and consuming packages within a private
PyPi repository hosted on AWS CodeArtifact; it contains an extension to the
keyring library that will automatically inject a time-limited access token.

Installation ...

Sections: AWS CodeArtifact Keyring Backend, Single Section Configuration, Multiple Section Configuration (EXPERIMENTAL)

</details>

### kfp-server-api

Kubeflow Pipelines API

`pip install kfp-server-api` · installs from source (sdist only) · licence: Apache 2.0 · rank 2750 · last release 2026-10-28 · [PyPI](https://pypi.org/project/kfp-server-api/)

<details><summary>README extract</summary>

This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition. # noqa: E501

</details>

### keyrings.alt

Alternate keyring implementations

`pip install keyrings.alt` · installs (wheel) · licence: MIT License · rank 2815 · last release 2024-08-14 · [PyPI](https://pypi.org/project/keyrings.alt/) · [source](https://github.com/jaraco/keyrings.alt)

<details><summary>README extract</summary>

Alternate keyring backend implementations for use with the
keyring package.

Keyrings in this package may have security risks or other implications. These
backends were extracted from the main keyring project to
make them available for those who wish to employ them, but are
discouraged for general production use. ...

</details>

### kagglesdk

Bindings to access kaggle's external-facing APIs

`pip install kagglesdk` · installs (wheel) · licence: Apache Software License · rank 3077 · last release 2026-10-21 · [PyPI](https://pypi.org/project/kagglesdk/)

<details><summary>README extract</summary>

Basic python bindings for Kaggle's external-facing endpoints.

These are automatically-generated, so external contributor PRs will only be accepted on documentation. Please feel free to file issues in this repository.

Kaggle maintainers: regeneration is documented in the internal `kapigen` tooling.

</details>

### kagglehub

Access Kaggle resources anywhere

`pip install kagglehub` · installs (wheel) · licence: Apache Software License · rank 3125 · last release 2026-10-21 · [PyPI](https://pypi.org/project/kagglehub/)

<details><summary>README extract</summary>

The `kagglehub` library provides a simple way to interact with Kaggle resources such as datasets, models, notebook outputs in Python.

This library also integrates natively with the Kaggle notebook environment. This means the behavior differs when you download a Kaggle resource with `kagglehub` in the Kaggle notebook environment: ...

Example:
```python
import kagglehub

kagglehub.login()
```

Sections: kagglehub, Usage, Authenticate, Option 1: kagglehub.login(), Option 2: Environment variable, Option 3: API token file, Option 4: Google Colab secret, Option 5: Legacy API credentials file, Download Model, Upload Model, Load Dataset, `KaggleDatasetAdapter.PANDAS`, `KaggleDatasetAdapter.HUGGING_FACE`, `KaggleDatasetAdapter.POLARS`

</details>

### kernels

Download compute kernels

`pip install kernels` · installs (wheel) · licence: Apache-2.0 · rank 3229 · last release 2026-11-02 · [PyPI](https://pypi.org/project/kernels/)

<details><summary>README extract</summary>

The Kernel Hub allows Python libraries and applications to load compute
kernels directly from the Hub. To support this kind
of dynamic loading, Hub kernels differ from traditional Python kernel
packages in that they are made to be:

- Portable: a kernel can be loaded from paths outside `PYTHONPATH`. ...

Example:
```python
import torch

from kernels import get_kernel

# Download optimized kernels from the Hugging Face hub
activation = get_kernel("kernels-community/activation", version=1)

# Random tensor
x = torch.randn((10, 10), dtype=torch.float16, device="cuda")

# Run the kernel
y = torch.empty_like(x)
activation.gelu_fast(y, x)

print(y)
```

Sections: kernels, 🚀 Quick Start, 📚 Documentation, Test coverage

</details>

### kedro

Kedro helps you build production-ready data and analytics pipelines

`pip install kedro` · installs (wheel) · licence: Apache Software License (Apache 2.0) · rank 3346 · last release 2026-09-28 · [PyPI](https://pypi.org/project/kedro/) · [docs](https://docs.kedro.org) · [source](https://github.com/kedro-org/kedro)

<details><summary>README extract</summary>

Kedro is a toolbox for production-ready data engineering and data science pipelines. It uses software engineering best practices to help you create data engineering and data science pipelines that are reproducible, maintainable, and modular. You can find out more at kedro.org. ...

Features:
Kedro is built upon our collective best-practice (and mistakes) trying to deliver real-world ML applications that have vast amounts of raw unvetted data. We developed Kedro to achieve the following: ...

Sections: What is Kedro?, What are the main features of Kedro?, How do I use Kedro?, Why does Kedro exist?, The humans behind Kedro, Where can I learn more?, ☕️ Kedro Coffee Chat 🔶

</details>

### keystoneauth1

Authentication Library for OpenStack Identity

`pip install keystoneauth1` · installs (wheel) · licence: Apache-2.0 · rank 3543 · last release 2026-10-12 · [PyPI](https://pypi.org/project/keystoneauth1/) · [docs](https://docs.openstack.org/keystoneauth/latest/) · [source](https://opendev.org/openstack/keystoneauth/)

<details><summary>README extract</summary>

This package contains tools for authenticating to an OpenStack-based cloud.
These tools include:

* Authentication plugins (password, token, and federation based)
* Discovery mechanisms to determine API version support
* A session that is used to maintain client settings across requests (based on
 the requests Python library) ...

</details>

### kokoro-onnx

TTS with kokoro and onnx runtime

`pip install kokoro-onnx` · does not install on CPython 3.14 · licence: not stated · rank 3651 · last release 2026-08-19 · [PyPI](https://pypi.org/project/kokoro-onnx/) · [source](https://github.com/thewh1teagle/kokoro-onnx)

<details><summary>README extract</summary>

TTS with onnx runtime based on Kokoro-TTS

🚀 Version 1.0 models are out now! 🎉


Features:
- Supports multiple languages
- Fast performance near real-time on macOS M1
- Offer multiple voices
- Lightweight: ~300MB (quantized: ~80MB)

Sections: kokoro-onnx, Features, Setup, Examples, Voices

</details>

### k8s-agent-sandbox

A client library to interact with the Agentic Sandbox on Kubernetes.

`pip install k8s-agent-sandbox` · installs (wheel) · licence: Apache Software License · rank 3658 · last release 2026-11-06 · [PyPI](https://pypi.org/project/k8s-agent-sandbox/)

<details><summary>README extract</summary>

This Python client provides a simple, high-level interface for creating and interacting with
sandboxes managed by the Agent Sandbox controller. It's designed to be used as a context manager,
ensuring that sandbox resources are properly created and cleaned up. ...

Example:
```python
from k8s_agent_sandbox import SandboxClient
from k8s_agent_sandbox.models import SandboxGatewayConnectionConfig

# Connect via the GKE Gateway
client = SandboxClient(
    connection_config=SandboxGatewayConnectionConfig(
        gateway_name="external-http-gateway",  # Name of the Gateway resource
    )
)

...
```

...

</details>

### kedro-datasets

Kedro-Datasets is where you can find all of Kedro's data connectors.

`pip install kedro-datasets` · installs (wheel) · licence: Apache Software License (Apache 2.0) · rank 3672 · last release 2026-11-03 · [PyPI](https://pypi.org/project/kedro-datasets/) · [docs](https://docs.kedro.org) · [source](https://github.com/kedro-org/kedro-plugins/tree/main/kedro-datasets)

<details><summary>README extract</summary>

<!-- Note that the contents of this file are also used in the documentation, see docs/source/index.md -->

Welcome to `kedro_datasets`, the home of Kedro's data connectors. Here you will find `AbstractDataset` implementations powering Kedro's DataCatalog created by QuantumBlack and external contributors.

Sections: Kedro-Datasets, How can I create my own `AbstractDataset` implementation?

</details>

### kernels-data

Kernels data structures (Python bindings)

`pip install kernels-data` · installs (wheel) · licence: not stated · rank 3751 · last release 2026-09-15 · [PyPI](https://pypi.org/project/kernels-data/)

### kedro-viz

Kedro-Viz helps visualise Kedro data and analytics pipelines

`pip install kedro-viz` · installs (wheel) · licence: Apache Software License (Apache 2.0) · rank 4071 · last release 2026-11-06 · [PyPI](https://pypi.org/project/kedro-viz/) · [docs](https://docs.kedro.org/projects/kedro-viz) · [source](https://github.com/kedro-org/kedro-viz)

<details><summary>README extract</summary>

✨ Data Science Pipelines. Beautifully Designed ✨

Live Demo:

Kedro-Viz is an interactive development tool for building data science pipelines with Kedro.

Features:
- ✨ Complete visualisation of a Kedro project and its pipelines
- 🎨 Supports light & dark themes out of the box
- 🚀 Scales to big pipelines with hundreds of nodes
- 🔎 Highly interactive, filterable and searchable ...

Sections: Kedro-Viz, Introduction, Features, Usage, Compatibility with Kedro and Kedro-datasets, CLI Usage, Standalone React component usage, Kedro-Viz in Visual Studio Code Extension, Feature Flags

</details>

### kr8s

A Kubernetes API library

`pip install kr8s` · installs (wheel) · licence: BSD-3-Clause · rank 4185 · last release 2026-01-16 · [PyPI](https://pypi.org/project/kr8s/) · [docs](https://docs.kr8s.org/en/stable) · [source](https://github.com/kr8s-org/kr8s.git)

<details><summary>README extract</summary>

A simple, extensible Python client library for Kubernetes that feels familiar for folks who already know how to use `kubectl`.

Features:
- API inspired by `kubectl` for a shallow learning curve.
- Sensible defaults to reduce boiler plate.
- No swagger generated code, human readable code only.
- Has both a standard and an async API that can be used with `asyncio` and `trio`. ...

Example:
```python
import kr8s

for node in kr8s.get("nodes"):
    print(node.name)
```

Sections: Highlights, Quickstart, Examples, List Nodes, Create a Pod, Scale a Deployment, List Pods by label selector, Add a label to a Pod, Generate a Pod, Cordon a Node, Pod Exec, Port forward a Pod

</details>

### krb5

Kerberos API bindings for Python

`pip install krb5` · installs from source (sdist only) · licence: MIT · rank 4409 · last release 2026-08-24 · [PyPI](https://pypi.org/project/krb5/)

<details><summary>README extract</summary>

This library provides Python functions that wraps the Kerberos 5 C API.
Due to the complex nature of this API it is highly recommended to use something like python-gssapi which exposes the Kerberos authentication details through GSSAPI. ...

Example:
```python
import krb5

if not hasattr(krb5, "kt_dup"):
    raise Exception("Current implementation does not support krb5_kt_dup")
```

Sections: Python Kerberos 5 Library, Requirements, Structure, Python Free-Threading (PEP 779)

</details>

### kaggle

Access Kaggle resources anywhere

`pip install kaggle` · installs (wheel) · licence: Apache Software License · rank 4809 · last release 2026-10-22 · [PyPI](https://pypi.org/project/kaggle/)

<details><summary>README extract</summary>

The official CLI to interact with Kaggle.

User documentation

Features:
Some of the key features are:

* List competitions, download competition data, submit to a competition.
* List, create, update, download or delete datasets.
* List, create, update, download or delete models & model variations. ...

Sections: Kaggle CLI, Key Features, Quick start, Hosting a competition, `kagglesdk` Updates, Prerequisites, Run `kaggle` from source, Option 1: Execute a one-liner of code from the command line, Option 2: Run many commands in a shell, Lint / Format, Tests, Integration Tests, Code Coverage, Editor Integration

</details>

### k8

Kubernetes Python Models

`pip install k8` · installs (wheel) · licence: MIT License · rank 4951 · last release 2024-05-23 · [PyPI](https://pypi.org/project/k8/)

<details><summary>README extract</summary>

K8 Models for Python

Regenerate with ./refresh.sh

</details>

### kedro-telemetry

Kedro-Telemetry

`pip install kedro-telemetry` · installs (wheel) · licence: Apache Software License (Apache 2.0) · rank 5019 · last release 2026-09-03 · [PyPI](https://pypi.org/project/kedro-telemetry/) · [docs](https://github.com/kedro-org/kedro-plugins/blob/main/kedro-telemetry/README.md) · [source](https://github.com/kedro-org/kedro-plugins/tree/main/kedro-telemetry)

<details><summary>README extract</summary>

Kedro-Telemetry is a plugin
that gathers anonymised and aggregated usage analytics
to help the Kedro team
understand how Kedro is used and prioritise improvements to the product accordingly.

Read our Telemetry documentation
for further information on the intent of the data collection and what data is collected. ...

Sections: Kedro-Telemetry, What is kedro-telemetry?, What data is being collected?, How is the data collected, Events sent by other Kedro plugins, How do I withdraw consent?, What happens when I withdraw consent?

</details>

### kylinpy

Apache Kylin Python Client Library

`pip install kylinpy` · installs from source (sdist only) · licence: MIT License · rank 5072 · last release 2020-08-11 · [PyPI](https://pypi.org/project/kylinpy/)

<details><summary>README extract</summary>

Apache Kylin Python Client Library is a python-based Apache Kylin client.

Any application that uses SQLAlchemy can now query Apache Kylin with this Apache Kylin dialect installed.

Example:
```python
$ python
>>> import sqlalchemy as sa
>>> kylin_engine = sa.create_engine('kylin://ADMIN:KYLIN@sandbox/learn_kylin?timeout=60&is_debug=1')
>>> results = kylin_engine.execute('SELECT count(*) FROM KYLIN_SALES')
>>> [e for e in results]
[(4953,)]
>>> kylin_engine.table_names()
[u'KYLIN_ACCOUNT',
 u'KYLIN_CAL_DT',
 u'KYLIN_CATEGORY_GROUPINGS',
...
```

Sections: Apache Kylin Python Client Library, Apache Kylin dialect for SQLAlchemy, From SQLAlchemy access Apache Kylin, From Pandas access Apache Kylin, From Superset access Apache Kylin

</details>

### keyrings.cryptfile

Encrypted file keyring backend

`pip install keyrings.cryptfile` · installs from source (sdist only) · licence: MIT License · rank 5405 · last release 2022-11-20 · [PyPI](https://pypi.org/project/keyrings.cryptfile/)

<details><summary>README extract</summary>

Summary

Encrypted plain file keyring backend for use with the
keyring package.

Description

The project is mainly targeted on a sufficiently secure storage for plain text
passwords (keyring) in a simple portable file, where the default keyring storage
implementation of a usual desktop environment doesn't fit.

Cryptography ...

Example:
```python
(env) $ python3
Python 3.4.5 (default, Jul 03 2016, 12:57:15) [GCC] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from keyrings.cryptfile.cryptfile import CryptFileKeyring
>>> kr = CryptFileKeyring()
>>> kr.set_password("service", "user", "secret")
Please set a password for your new keyring: **
...
```

</details>

### kubernetes-stubs-elephant-fork

Type stubs for the Kubernetes Python API client

`pip install kubernetes-stubs-elephant-fork` · installs (wheel) · licence: Apache Software License · rank 5513 · last release 2026-11-06 · [PyPI](https://pypi.org/project/kubernetes-stubs-elephant-fork/)

<details><summary>README extract</summary>

fork of kubernetes-stubs

This library is deprecated.

The official Kubernetes Python client has supported typing since version 37.0.0,
making `kubernetes-stubs-elephant-fork` obsolete.

Thank you to everyone who installed and used `kubernetes-stubs-elephant-fork` over the past few years. ...

Features:
kubernetes-stubs has not provided stubs for kubernetes >= 23.0 yet (2023-05-30).

`kubernetes-stubs-elephant-fork` provides stubs for all releases after 7.0 of kubernetes,
even includes any release in the future automatically. ...

Sections: kubernetes-stubs-elephant-fork, deprecated, why fork?

</details>

### koalas

Koalas: pandas API on Apache Spark

`pip install koalas` · does not install on CPython 3.14 · licence: http://www.apache.org/licenses/LICENSE-2.0 · rank 5593 · last release 2021-10-19 · [PyPI](https://pypi.org/project/koalas/) · [docs](https://koalas.readthedocs.io/) · [source](https://github.com/databricks/koalas)

<details><summary>README extract</summary>

NOTE: Koalas supports Apache Spark 3.1 and below as it will be officially included to PySpark in the upcoming Apache Spark 3.2. This repository is now in maintenance mode. For Apache Spark 3.2 and above, please use PySpark directly.

 pandas API on Apache Spark

 Explore Koalas docs »

 Live notebook
 Issues
 Mailing list ...

Example:
```python
import databricks.koalas as ks
import pandas as pd

pdf = pd.DataFrame({'x':range(3), 'y':['a','b','b'], 'z':['a','b','b']})

# Create a Koalas DataFrame from pandas DataFrame
df = ks.from_pandas(pdf)

# Rename the columns
df.columns = ['x', 'y', 'z1']

# Do some operations in place:
df['x2'] = df.x * df.x
```

Sections: Getting Started, FAQ, Best Practices, Koalas Talks and Blogs

</details>

### kubernetes-stubs

Type stubs for the Kubernetes Python API client

`pip install kubernetes-stubs` · installs (wheel) · licence: Apache Software License · rank 5790 · last release 2022-04-20 · [PyPI](https://pypi.org/project/kubernetes-stubs/)

<details><summary>README extract</summary>

Python type stubs for the Kubernetes API client.
The version numbers of this package track upstream's. PRs to fix bugs are
welcomed.

Sections: kubernetes-stubs, Usage

</details>

### kokoro

TTS

`pip install kokoro` · does not install on CPython 3.14 · licence: Apache Software License · rank 5803 · last release 2025-04-05 · [PyPI](https://pypi.org/project/kokoro/) · [source](https://github.com/hexgrad/kokoro)

<details><summary>README extract</summary>

An inference library for Kokoro-82M. You can `pip install kokoro`.

> Kokoro is an open-weight TTS model with 82 million parameters. Despite its lightweight architecture, it delivers comparable quality to larger models while being significantly faster and more cost-efficient. ...

Example:
```python
!pip install -q kokoro>=0.9.4 soundfile
!apt-get -qq -y install espeak-ng > /dev/null 2>&1
from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import torch
pipeline = KPipeline(lang_code='a')
text = '''
...
```

Sections: kokoro, Usage, Advanced Usage, Conda Environment

</details>

### keplergl

Kepler.gl Jupyter Widget

`pip install keplergl` · installs (wheel) · licence: MIT · rank 6177 · last release 2026-10-26 · [PyPI](https://pypi.org/project/keplergl/)

<details><summary>README extract</summary>

This is the kepler.gl Jupyter widget, an advanced geospatial visualization tool for rendering large-scale interactive maps in Jupyter Notebook and JupyterLab.

Features:
- Multiple data formats: Load CSV, GeoJSON, Pandas DataFrame, and GeoPandas GeoDataFrame
- GeoArrow support: Use `use_arrow=True` for faster data loading and rendering with large datasets ...

Example:
```python
from keplergl import KeplerGl

# Create a map
map = KeplerGl(height=400)

# Add data
map.add_data(data=df, name='my_data')

# Display the map
map
```

Sections: kepler.gl for Jupyter, Prerequisites, Quick Start, Features, Documentation, AI Assistant Skill Setup

</details>

### kuzu

Highly scalable, extremely fast, easy-to-use embeddable graph database

`pip install kuzu` · installs (wheel) · licence: MIT · rank 6203 · last release 2025-10-10 · [PyPI](https://pypi.org/project/kuzu/) · [docs](https://docs.kuzudb.com/) · [source](https://github.com/kuzudb/kuzu)

<details><summary>README extract</summary>

> [!NOTE]
> Kuzu is working on something new!
> We are archiving the KuzuDB project here:
> For those using Kuzu currently, prior Kuzu releases will continue to be usable in the same way without modifications to your code.
> If you are also using extensions, moving forward you have two options:
> 1. ...

Sections: Kuzu, Docs and Blog, Getting Started, Extensions, Host your own extension server, Build from Source

</details>

### klaviyo-api

Klaviyo Python SDK

`pip install klaviyo-api` · installs (wheel) · licence: MIT License · rank 6619 · last release 2026-10-15 · [PyPI](https://pypi.org/project/klaviyo-api/)

<details><summary>README extract</summary>

- SDK version: 25.0.0
- API revision: 2026-10-15

Example:
```python
klaviyo.Metrics.get_metrics()
```

Sections: Klaviyo Python SDK, Helpful Resources, Design & Approach, Organization, Usage Example, To instantiate the client, Example request, Use Case Examples, How to filter based on datetime, How to use pagination and the page[size] param, Uploading Image From File, Error Handling, Important Notes, Comprehensive List of Operations & Parameters

</details>

### kbcstorage

Client for Keboola Storage API

`pip install kbcstorage` · installs (wheel) · licence: MIT License · rank 7065 · last release 2026-10-08 · [PyPI](https://pypi.org/project/kbcstorage/)

<details><summary>README extract</summary>

Client for using Keboola Connection Storage API. This API client provides client methods to get data from KBC and store data in KBC. The endpoints
for working with buckets, tables and workspaces are covered.

Example:
```python
from kbcstorage.client import Client, StorageApiToken

client = Client(' StorageApiToken('your-token'))

# get table data into local file
client.tables.export_to_file(table_id='in.c-demo.some-table', path_name='/data/')

# save data
client.tables.create(name='some-table-2', bucket_id='in.c-demo', file_path='/data/some-table')

# list buckets
...
```

Sections: Python client for the Keboola Storage API, Client Class Usage, Authentication, Breaking change in 0.11.0, Endpoint Classes Usage, Local environment, Editor setup, Checks, Tests

</details>

### kfactory

KLayout API implementation of gdsfactory

`pip install kfactory` · installs (wheel) · licence: not stated · rank 7226 · last release 2026-10-16 · [PyPI](https://pypi.org/project/kfactory/)

<details><summary>README extract</summary>

KFactory is a Python framework for photonic and electronic chip layout, built on KLayout's C++ geometry engine.
It provides parametric cells with caching, optical and electrical routing, enclosures via Minkowski sums, and schematic-driven design with LVS.

Features:
- Cell caching — the `@kf.cell` decorator deduplicates identical components automatically
- Routing — optical and electrical bundle routing, Manhattan primitives, all-angle routing, and path-length matching ...

Sections: KFactory 3.5.0, Key Features, Getting Started, Ecosystem, Documentation

</details>

### konoha

Add your description here

`pip install konoha` · installs (wheel) · licence: MIT · rank 7531 · last release 2026-10-25 · [PyPI](https://pypi.org/project/konoha/)

<details><summary>README extract</summary>

`Konoha` is a Python library for providing easy-to-use integrated interface of various Japanese tokenizers,
which enables you to switch a tokenizer and boost your pre-processing.

Example:
```python
from konoha import WordTokenizer

sentence = '自然言語処理を勉強しています'

tokenizer = WordTokenizer('MeCab')
print(tokenizer.tokenize(sentence))
# => [自然, 言語, 処理, を, 勉強, し, て, い, ます]

tokenizer = WordTokenizer('Sentencepiece', model_path="data/model.spm")
print(tokenizer.tokenize(sentence))
# => [▁, 自然, 言語, 処理, を, 勉強, し, ています]
```

Sections: 🌿 Konoha: Simple wrapper of Japanese Tokenizers, Quick Start with Docker, Example, Word level tokenization, Remote files, Sentence level tokenization, Test, Article

</details>

### keystonemiddleware

Middleware for OpenStack Identity

`pip install keystonemiddleware` · installs (wheel) · licence: Apache Software License · rank 8094 · last release 2026-11-02 · [PyPI](https://pypi.org/project/keystonemiddleware/)

<details><summary>README extract</summary>

This package contains middleware modules designed to provide authentication and
authorization features to web services other than `Keystone
< The most prominent module is
`keystonemiddleware.auth_token`. This package does not expose any CLI or
Python API features.

For information on contributing, see `CONTRIBUTING.rst`. ...

</details>

### keysymdef

X11 keysym data for Python

`pip install keysymdef` · installs (wheel) · licence: X11 · rank 8112 · last release 2023-02-25 · [PyPI](https://pypi.org/project/keysymdef/)

<details><summary>README extract</summary>

This Python package contains the X11 and XF86 keysym definitions as lists of tuples:
The elements of each tuple are:

1. The mnemonic name (`str`)
2. The integer value (`int`)
3. The unicode code point, if any (`int` or `None`)

This data is hard-coded; consequently this package has no dependencies (on `python-xlib` or others).

Example:
```python
>>> from keysymdef import keysymdef, xf86keysym
>>> print(keysymdef[1])
('BackSpace', 65288, None)
>>> print(xf86keysym[1])
('MonBrightnessUp', 269025026, None)
```

</details>

### kombo

The official Python SDK for the Kombo Unified API

`pip install kombo` · installs (wheel) · licence: not stated · rank 8193 · last release 2026-09-23 · [PyPI](https://pypi.org/project/kombo/) · [source](https://github.com/kombohq/python-sdk.git)

<details><summary>README extract</summary>

Developer-friendly & type-safe Python SDK for the Kombo Unified API.

> [!NOTE]
> The Kombo Python SDK is currently in beta. The core API structure, methods, and input/output objects are considered stable. ...

Example:
```python
# !/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
# "kombo",
# ]
# ///

from kombo import Kombo

sdk = Kombo(
  # SDK arguments
)

# Rest of script here...
```

Sections: Kombo Python SDK, uv, PIP, Poetry, Shell and script usage with `uv`, SDK Example Usage, Specifying an integration ID, Region Selection, Example, Available Resources and Operations, Assessment, Ats, Connect, General

</details>

### kml2geojson

A Python library to convert KML files to GeoJSON files

`pip install kml2geojson` · installs (wheel) · licence: MIT · rank 8272 · last release 2026-07-06 · [PyPI](https://pypi.org/project/kml2geojson/) · [docs](https://araichev.codeberg.page/kml2geojson_docs)

<details><summary>README extract</summary>

Tests:

kml2geojson is a Python package to convert KML files to GeoJSON files.
It's a lightweight, dependency-minimal, web-output-focused alternative to GDAL.
Most of its code is a translation into Python of the Node.js package togeojson, but kml2geojson also adds the following features.

- Preserve KML object styling, such as color and opacity ...

Sections: kml2geojson, Usage, Documentation, Notes, Changes, 6.0.0, 2026-07-06, 5.1.1, 2026-03-12, 5.1.0, 2022-04-29, 5.0.1, 2021-10-11, 5.0.0, 2021-10-07, 4.0.0, 2016-11-24, 3.0.4, 2015-10-15, 3.0.3, 2015-10-13, 3.0.2, 2015-10-12

</details>

### koyeb-sdk

Koyeb python sdk

`pip install koyeb-sdk` · installs (wheel) · licence: Apache-2.0 · rank 8576 · last release 2026-10-27 · [PyPI](https://pypi.org/project/koyeb-sdk/) · [source](https://github.com/koyeb/koyeb-python-sdk)

<details><summary>README extract</summary>

This is the official Python SDK for Koyeb, a platform that allows you to deploy and manage applications and services in the cloud.

- `koyeb.api`: Contains the synchronous API client and methods to interact with Koyeb's REST API. Documentation ...

Sections: Koyeb python sdk, Modules, Koyeb Sanboxes, Set the Koyeb API token, Example sandbox code, Run the code, The Koyeb Sandbox Python module

</details>

### kafka-schema-registry

Kafka and schema registry integration

`pip install kafka-schema-registry` · installs (wheel) · licence: MIT · rank 8583 · last release 2022-07-13 · [PyPI](https://pypi.org/project/kafka-schema-registry/) · [source](https://github.com/flix-tech/kafka-schema-registry)

<details><summary>README extract</summary>

This library allows you to create topics on Kafka topics, associated with a
Confluent Schema Registry, and publish messages on them.

It takes care of:
* creating the topic
* publishing the associated schema (or updating an existing one)
* serializing and publishing messages to Kafka ...

Example:
```python
from kafka_schema_registry import prepare_producer

SAMPLE_SCHEMA = {
    "type": "record",
    "name": "TestType",
    "fields" : [
        {"name": "age", "type": "int"},
        {"name": "name", "type": ["null", "string"]}
    ]
}

producer = prepare_producer(
        ['localhost:9092'],
        f'
        topic_name,
        1,
        1,
...
```

Sections: kafka-schema-registry, Usage, Running the tests

</details>

### kaldi-python-io

A pure python IO interface for data accessing in kaldi

`pip install kaldi-python-io` · installs from source (sdist only) · licence: Apache V2.0 · rank 9225 · last release 2021-03-18 · [PyPI](https://pypi.org/project/kaldi-python-io/)

<details><summary>README extract</summary>

A python (3.6+) wrapper for Kaldi's data accessing.

Example:
```python
# allow only sequential index
ark_reader = ArchiveReader("copy-feats ark:foo.ark ark:- |")
for key, _ in ark_reader:
    print(key)
ali_reader = AlignArchiveReader("gunzip -c foo.ali.gz |")
for key, _ in ark_reader:
    print(key)
```

Sections: Kaldi Python IO, Usage

</details>

### kantoku

Circus is a program that will let you run and watch multiple processes and sockets.

`pip install kantoku` · installs (wheel) · licence: Apache Software License · rank 9319 · last release 2025-03-11 · [PyPI](https://pypi.org/project/kantoku/) · [docs](https://circus.readthedocs.io) · [source](https://github.com/bentoml/kantoku)

<details><summary>README extract</summary>

Circus is a program that runs and watches processes and sockets.
Circus can be used as a library or through the command line.

- Full Documentation
- How to Contribute
- IRC: Freenode, channel #mozilla-circus

Sections: Circus, Links

</details>

### kanaries-track

kanaries_track: track to kanaries data infra

`pip install kanaries-track` · installs (wheel) · licence: Apache Software License · rank 9357 · last release 2024-05-13 · [PyPI](https://pypi.org/project/kanaries-track/) · [source](https://github.com/Kanaries/kanaries-track)

<details><summary>README extract</summary>

Example:
```python
import kanaries_track

kanaries_track.config.auth_token = "your_project_key"
kanaries_track.track({"xxx": "xxx"}) # any map
```

Sections: kanaries-track, Quick Start

</details>

### kenlm

(no summary)

`pip install kenlm` · installs from source (sdist only) · licence: not stated · rank 9388 · last release 2025-04-07 · [PyPI](https://pypi.org/project/kenlm/)

### Kivy-Garden

(no summary)

`pip install Kivy-Garden` · installs (wheel) · licence: MIT · rank 10032 · last release 2022-03-23 · [PyPI](https://pypi.org/project/Kivy-Garden/)

### kcl-rs

Rust-powered Python bindings for the Amazon Kinesis Client Library

`pip install kcl-rs` · installs (wheel) · licence: Apache-2.0 · rank 10188 · last release 2026-07-21 · [PyPI](https://pypi.org/project/kcl-rs/)

<details><summary>README extract</summary>

A Rust port of the Amazon Kinesis Client Library (KCL)
with native Python bindings — the KCL v3 consumer framework without a JVM and
without the MultiLangDaemon.

Like the Java KCL, this is the framework that turns "read from a Kinesis
stream" into a production consumer fleet: it coordinates shard leases
between workers through a DynamoDB table, ...

Example:
```python
from kcl_rs import RecordProcessorBase, Scheduler, CheckpointError

class MyProcessor(RecordProcessorBase):
    def initialize(self, initialize_input):
        print(f"starting on shard {initialize_input.shard_id}")

    def process_records(self, process_records_input):
        for record in process_records_input.records:
...
```

...

</details>

### kubernetes-validate

validates kubernetes resource definitions against schemas

`pip install kubernetes-validate` · installs (wheel) · licence: Apache · rank 10252 · last release 2026-10-11 · [PyPI](https://pypi.org/project/kubernetes-validate/)

<details><summary>README extract</summary>

kubernetes-validate validates Kubernetes resource definitions against the
declared Kubernetes schemas.

Based on Gareth Rushgrove's excellent work providing a basis for turning Kubernetes
Swagger API definitions into JSONSchema definitions, kubernetes-validate will report
on mismatches between schema defnition and resource definition ...

Example:
```python
from future import print_function
import kubernetes_validate
import yaml

try:
    data = yaml.load(open('resource.yaml').read())
    kubernetes_validate.validate(data, '1.22', strict=True)
except kubernetes_validate.ValidationError as e:
    print(''. join(e.path), e.message)
```

Sections: kubernetes-validate, Usage, Command line, Python, Examples

</details>

### keboola.vcr

VCR recording, sanitization, and validation for Keboola component HTTP interactions

`pip install keboola.vcr` · installs (wheel) · licence: MIT License · rank 10260 · last release 2026-11-04 · [PyPI](https://pypi.org/project/keboola.vcr/) · [source](https://github.com/keboola/python-vcr-tests)

<details><summary>README extract</summary>

VCR recording, sanitization, and validation for Keboola component HTTP interactions.

Features:
- Recording: Captures real HTTP interactions via vcrpy and stores them as JSON cassettes
- Sanitization: Redacts secrets, tokens, and sensitive fields before saving cassettes ...

Example:
```python
from keboola.vcr.recorder import VCRRecorder
from keboola.vcr.sanitizers import DefaultSanitizer

recorder = VCRRecorder(
    cassette_dir="tests/cassettes/my_test",
    secrets={"api_key": "secret"},
)
```

Sections: keboola.vcr, Usage, Features, Sanitizing data before the component reads it, Recording proxy (PHP and other non-Python components)

</details>

### kgcl-schema

Schema for the KGCL project.

`pip install kgcl-schema` · installs (wheel) · licence: MIT License · rank 10405 · last release 2024-11-14 · [PyPI](https://pypi.org/project/kgcl-schema/)

<details><summary>README extract</summary>

KGCL is a standard datamodel for representing changes in ontologies and knowledge graphs.

This repository houses:

- The KGCL schema/standard
- The Python implementation of the standard (LinkML model, LARK grammar)

The following URIs will resolve to the KGCL standard:

Read more here.

Sections: KGCL: Knowledge Graph Change Language, Documentation

</details>

### kgcl-rdflib

Schema for the KGCL project.

`pip install kgcl-rdflib` · installs (wheel) · licence: MIT License · rank 10469 · last release 2023-05-11 · [PyPI](https://pypi.org/project/kgcl-rdflib/)

<details><summary>README extract</summary>

An engine that applies changes or diffs specified in KGCL to an RDF graph stored using rdflib

KGCL (Knowledge Graph Change Language) is a datamodel and language for representing changes in ontologies and knowledge graphs

The core KGCL repo is here:

 This kgcl-rdflib repo applies the KGCL model to rdflib graphs.

Sections: kgcl-rdflib, KGCL

</details>

### kcli

Provisioner/Manager for Libvirt/Vsphere/Aws/Gcp/Hcloud/Kubevirt/Ovirt/Openstack/IBM Cloud and containers

`pip install kcli` · installs (wheel) · licence: ASL · rank 10476 · last release 2026-11-06 · [PyPI](https://pypi.org/project/kcli/)

<details><summary>README extract</summary>

Provisioner/Manager for Libvirt/Vsphere/Aws/Gcp/Hcloud/Kubevirt/Ovirt/Openstack/IBM Cloud and containers

</details>

### kyrax

A fast excel file reader and writer for Python, written in Rust

`pip install kyrax` · installs (wheel) · licence: MIT License · rank 10496 · last release 2026-08-17 · [PyPI](https://pypi.org/project/kyrax/) · [source](https://github.com/AdityaVishwakarmaIN/kyrax)

<details><summary>README extract</summary>

A fast excel file reader for Python and Rust.

Docs:
 * Python (local: `make doc-serve`)
 * Rust (local: `cargo doc --open -p kyrax`)

The Python library is considered production-ready. The API is mostly stable, and we avoid breaking changes as much as
possible.

> ⚠️ The free-threaded build is still considered experimental ...

Features:
- Zero-copy data exchange via Arrow PyCapsule Interface
- High-speed Turbo engine - selective XLSX feature reading (`read_excel_turbo`), declarative writing (`write_excel_turbo`), and streaming (`write_excel_turbo_stream`) ...

Example:
```python
import kyrax

# Load an Excel file
reader = kyrax.read_excel("data.xlsx")
sheet = reader.load_sheet(0)  # Load first sheet

# Use with Polars (zero-copy, no pyarrow needed)
import polars as pl
...

</details>

### kiss-icp

Simple yet effective 3D LiDAR-Odometry registration pipeline

`pip install kiss-icp` · installs from source (sdist only) · licence: MIT License · rank 10690 · last release 2026-04-26 · [PyPI](https://pypi.org/project/kiss-icp/)

<details><summary>README extract</summary>

Demo
 Install
 ROS 2
 ROS Demo
 Paper
 Contact Us

KISS-ICP is a LiDAR Odometry pipeline that just works on most of the cases withouth tunning any parameter.

Sections: KISS-ICP, Running the system, Config

</details>

### koreanize-matplotlib

matplotlib의 폰트 설정을 자동으로 한국어화

`pip install koreanize-matplotlib` · installs (wheel) · licence: MIT License · rank 10795 · last release 2022-12-27 · [PyPI](https://pypi.org/project/koreanize-matplotlib/)

<details><summary>README extract</summary>

matplotlib를 한국어 표시에 대응시킵니다.

matplotlib를 import한 후 koreanize_matplotlib를 import합니다.


Example:
```python
import matplotlib.pyplot as plt
import koreanize_matplotlib

plt.plot([-1, 0, 1, 2])
plt.title('그래프 제목', fontweight="bold")
plt.xlabel('간단한 그래프')
plt.show()
```

Sections: koreanize-matplotlib, 사용법, 설치, 사용한 폰트

</details>

### kumoai

AI on the Modern Data Stack

`pip install kumoai` · installs (wheel) · licence: MIT · rank 10871 · last release 2026-05-11 · [PyPI](https://pypi.org/project/kumoai/) · [docs](https://kumo.ai/docs)

<details><summary>README extract</summary>

______________

The Kumo SDK implements a pythonic interface for users to programmatically
interact with the Kumo machine learning platform
(documentation).

</details>

### kfp-kubernetes

Kubernetes platform configuration library and generated protos.

`pip install kfp-kubernetes` · installs (wheel) · licence: Apache 2.0 · rank 11064 · last release 2026-10-28 · [PyPI](https://pypi.org/project/kfp-kubernetes/) · [docs](https://kfp-kubernetes.readthedocs.io/) · [source](https://github.com/kubeflow/pipelines/tree/master/kubernetes_platform/python)

<details><summary>README extract</summary>

The Kubeflow Pipelines SDK kfp-kubernetes python library (part of the Kubeflow Pipelines project) is an addon to the Kubeflow Pipelines SDK that enables authoring Kubeflow pipelines with Kubernetes-specific features and concepts, such as: ...

Example:
```python
from kfp import dsl
from kfp import kubernetes

@dsl.component
def print_secret():
    import os
    print(os.environ['SECRET_VAR'])

@dsl.pipeline
def pipeline():
    task = print_secret()
    kubernetes.use_secret_as_env(task,
                                 secret_name='my-secret',
...
```

...

</details>

### kappa

A CLI tool for AWS Lambda developers

`pip install kappa` · installs from source (sdist only) · licence: Apache Software License · rank 12014 · last release 2017-02-13 · [PyPI](https://pypi.org/project/kappa/)

<details><summary>README extract</summary>

Kappa is a command line tool that (hopefully) makes it easier to
deploy, update, and test functions for AWS Lambda.

There are quite a few steps involved in developing a Lambda function.
You have to: ...

Sections: kappa, Quick Start, Policies

</details>

### kr-sentence

Light-weight sentence tokenizer for Korean.

`pip install kr-sentence` · installs (wheel) · licence: Apache Software License · rank 12274 · last release 2021-10-28 · [PyPI](https://pypi.org/project/kr-sentence/)

<details><summary>README extract</summary>

A light-weight sentence tokenizer for Korean.

Half-width punctuation is generally used in Korean, but this tokenizer also supports full-width punctuation. (For details about full-width punctuation in Korean, please see

Sample Code:

from kr_sentence.tokenizer import tokenize

paragraph_str = "저는 미국인이에요. 만나서 반갑습니다." ...

</details>

### kt-legacy

Legacy import names for Keras Tuner

`pip install kt-legacy` · installs (wheel) · licence: Apache License 2.0 · rank 12588 · last release 2023-04-12 · [PyPI](https://pypi.org/project/kt-legacy/)

### kingfisher-bin

Kingfisher secret scanning CLI (packaged binary)

`pip install kingfisher-bin` · installs (wheel) · licence: Apache Software License · rank 12596 · last release 2026-11-05 · [PyPI](https://pypi.org/project/kingfisher-bin/) · [source](https://github.com/mongodb/kingfisher)

<details><summary>README extract</summary>

This package ships the Kingfisher CLI as a platform-specific Python wheel.
The `kingfisher` console script executes the bundled binary for your
OS/architecture.

Sections: Kingfisher (Python wheel), Usage

</details>

### kornia-moons

Conversions between kornia and other computer vision libraries formats

`pip install kornia-moons` · installs (wheel) · licence: Apache Software License · rank 12646 · last release 2026-08-07 · [PyPI](https://pypi.org/project/kornia-moons/) · [docs](https://ducha-aiki.github.io/kornia_moons/) · [source](https://github.com/ducha-aiki/kornia_moons)

<details><summary>README extract</summary>

Conversions between kornia and other computer vision libraries formats, mainly OpenCV.

Documentation:

- Keypoint / LAF conversions — OpenCV `cv2.KeyPoint` ↔ kornia local affine frames (LAFs), handling the differing scale and orientation conventions (`mrSize=6.0` for SIFT, `1.0` for ORB): `laf_from_opencv_SIFT_kpts`, `opencv_ORB_kpts_from_laf`, ...

Example:
```python
import matplotlib.pyplot as plt
import cv2
from kornia.image import image_to_tensor

from kornia_moons.feature import laf_from_opencv_ORB_kpts, opencv_ORB_kpts_from_laf
from kornia_moons.viz import visualize_LAF

img = cv2.cvtColor(cv2.imread('data/strahov.png'), cv2.COLOR_BGR2RGB)

det = cv2.ORB_create(500)
...
```

...

</details>

### kosong

The LLM abstraction layer for modern AI agent applications.

`pip install kosong` · installs (wheel) · licence: not stated · rank 12813 · last release 2026-08-03 · [PyPI](https://pypi.org/project/kosong/)

<details><summary>README extract</summary>

Kosong is an LLM abstraction layer designed for modern AI agent applications. It unifies message structures, asynchronous tool orchestration, and pluggable chat providers so you can build agents with ease and avoid vendor lock-in.

> Kosong means "empty" in Malay and Indonesian.

Example:
```python
import asyncio

import kosong
from kosong.chat_provider.kimi import Kimi
from kosong.message import Message

async def main() -> None:
    kimi = Kimi(
        base_url="
        api_key="your_kimi_api_key_here",
        model="kimi-k2-turbo-preview",
    )

    history = [
        Message(role="user", content="Who are you?"),
    ]

...
```

Sections: Kosong, Examples, Simple chat completion, Streaming output, Tool calling with `kosong.step`, Builtin Demo

</details>

### kimi-cli

[Archived] Legacy Python Kimi CLI, no longer maintained. Use Kimi Code CLI instead: https://github.com/MoonshotAI/kimi-code

`pip install kimi-cli` · installs (wheel) · licence: not stated · rank 12861 · last release 2026-09-22 · [PyPI](https://pypi.org/project/kimi-cli/) · [source](https://github.com/MoonshotAI/kimi-cli)

<details><summary>README extract</summary>

Kimi Code CLI | Migration Guide | 迁移指南 | Legacy Docs

> [!CAUTION]
> This project has been archived and is no longer maintained. Kimi CLI (Python) has been replaced by Kimi Code CLI, the next-generation terminal AI agent from the same team.
> - This repository is read-only. There will be no further releases, bug fixes, or security updates. ...

Sections: Kimi CLI (Archived), Migrate to Kimi Code CLI, Packages in this repository, Getting Started, Key Features, Shell command mode, VS Code extension, IDE integration via ACP, Zsh integration, More

</details>

### keystone

OpenStack Identity

`pip install keystone` · installs (wheel) · licence: Apache Software License · rank 13075 · last release 2026-09-30 · [PyPI](https://pypi.org/project/keystone/) · [source](https://opendev.org/openstack/keystone)

<details><summary>README extract</summary>

OpenStack Keystone provides authentication, authorization and service discovery
mechanisms via HTTP primarily for use by projects in the OpenStack family. It
is most commonly deployed as an HTTP interface to existing identity systems,
such as LDAP.

Developer documentation, the source of which is in `doc/source/`, is
published at: ...

</details>

### krakenex

kraken.com cryptocurrency exchange API

`pip install krakenex` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 13222 · last release 2024-07-01 · [PyPI](https://pypi.org/project/krakenex/)

_README extract left out: share-alike licence._

### kfnetlist

Standalone Netlist schema for kfactory and netlist tooling

`pip install kfnetlist` · installs (wheel) · licence: not stated · rank 13231 · last release 2026-09-14 · [PyPI](https://pypi.org/project/kfnetlist/)

