# Unclassified / Q

[Index](README.md) · 36 packages in this topic, by downloads.

### qdrant-client

Client library for the Qdrant vector search engine

`pip install qdrant-client` · installs (wheel) · licence: Apache Software License · rank 1030 · last release 2026-10-22 · [PyPI](https://pypi.org/project/qdrant-client/) · [source](https://github.com/qdrant/qdrant-client)

<details><summary>README extract</summary>

Python Client library for the Qdrant vector search engine.

Client library and SDK for the Qdrant vector search engine.

Library contains type definitions for all Qdrant API and allows to make both Sync and Async requests.

Client allows calls for all Qdrant API methods directly. ...

Features:
- Type hints for all API methods
- Local mode - use same API without running server
- REST and gRPC support
- Minimal dependencies
- Extensive Test Coverage

Example:
```python
from qdrant_client.models import Distance, VectorParams

client.create_collection(
    collection_name="my_collection",
    vectors_config=VectorParams(size=100, distance=Distance.COSINE),
)
```

...

</details>

### quack-kernels

(no summary)

`pip install quack-kernels` · installs (wheel) · licence: not stated · rank 2186 · last release 2026-09-11 · [PyPI](https://pypi.org/project/quack-kernels/)

### qdldl

QDLDL, a free LDL factorization routine.

`pip install qdldl` · installs (wheel) · licence: Apache 2.0 · rank 2413 · last release 2026-02-19 · [PyPI](https://pypi.org/project/qdldl/)

<details><summary>README extract</summary>

Python interface to the QDLDL
free LDL factorization routine for quasi-definite linear systems: `Ax =
b`.

Example:
```python
import qdldl
F = qdldl.Solver(A)
```

Sections: qdldl-python, Usage

</details>

### queuelib

Collection of persistent (disk-based) and non-persistent (memory-based) queues

`pip install queuelib` · installs (wheel) · licence: BSD-3-Clause · rank 2478 · last release 2026-08-24 · [PyPI](https://pypi.org/project/queuelib/) · [docs](https://github.com/scrapy/queuelib/blob/master/README.rst) · [source](https://github.com/scrapy/queuelib)

<details><summary>README extract</summary>

Queuelib is a Python library that implements object collections which are stored
in memory or persisted to disk, provide a simple API, and run fast.

Queuelib provides collections for queues (FIFO), stacks (LIFO), queues
sorted by priority and queues that are emptied in a round-robin fashion.

Queuelib supports Python 3.10+ and has no dependencies.

Example:
```python
>>> from queuelib import FifoDiskQueue
>>> q = FifoDiskQueue("queuefile")
>>> q.push(b'a')
>>> q.push(b'b')
>>> q.push(b'c')
>>> q.pop()
b'a'
>>> q.close()
>>> q = FifoDiskQueue("queuefile")
>>> q.pop()
b'b'
>>> q.pop()
b'c'
>>> q.pop()
>>>
```

...

</details>

### quickjs

Wrapping the quickjs C library.

`pip install quickjs` · installs from source (sdist only) · licence: not stated · rank 2670 · last release 2023-11-19 · [PyPI](https://pypi.org/project/quickjs/)

<details><summary>README extract</summary>

Python wrapper around .

Translates types like `str`, `float`, `bool`, `list`, `dict` and combinations
thereof to and from Javascript.

QuickJS is currently thread-hostile, so this wrapper makes sure that all calls
to the same JS runtime comes from the same thead.

</details>

### querystring-parser

QueryString parser for Python/Django that correctly handles nested dictionaries

`pip install querystring-parser` · installs (wheel) · licence: MIT License · rank 2845 · last release 2020-10-21 · [PyPI](https://pypi.org/project/querystring-parser/)

### qtconsole

Jupyter Qt console

`pip install qtconsole` · installs (wheel) · licence: BSD License · rank 3109 · last release 2026-03-25 · [PyPI](https://pypi.org/project/qtconsole/)

<details><summary>README extract</summary>

A rich Qt-based console for working with Jupyter kernels,
supporting rich media output, session export, and more.

The Qtconsole is a very lightweight application that largely feels like a terminal, but
provides a number of enhancements only possible in a GUI, such as inline
figures, proper multiline editing with syntax highlighting, graphical ...

Sections: Jupyter QtConsole, Usage, Resources

</details>

### query-cache-common

Common code for Query Cache shared across client and server

`pip install query-cache-common` · installs (wheel) · licence: not stated · rank 5187 · last release 2026-10-15 · [PyPI](https://pypi.org/project/query-cache-common/)

### query-cache-protobuf

Generated protobuf code for Query Cache

`pip install query-cache-protobuf` · installs (wheel) · licence: not stated · rank 5189 · last release 2026-10-15 · [PyPI](https://pypi.org/project/query-cache-protobuf/)

### qiskit-qasm3-import

Importer for parsing OpenQASM 3 strings into Qiskit circuits

`pip install qiskit-qasm3-import` · installs (wheel) · licence: Apache 2.0 License · rank 5863 · last release 2025-06-10 · [PyPI](https://pypi.org/project/qiskit-qasm3-import/) · [docs](https://qiskit.github.io/qiskit-qasm3-import) · [source](https://github.com/Qiskit/qiskit-qasm3-import)

<details><summary>README extract</summary>

This repository provides the Python package `qiskit_qasm3_import`, which is a
basic and temporary importer from OpenQASM 3 into Qiskit's `QuantumCircuit`.

Qiskit itself accepts this package as an optional dependency if it is installed. ...

Example:
```python
from qiskit_qasm3_import import parse
circuit = parse(program)
```

Sections: Importer from OpenQASM 3 to Qiskit, Example, Building documentation, Code style and linting

</details>

### qudida

QUick and DIrty Domain Adaptation

`pip install qudida` · installs (wheel) · licence: not stated · rank 6253 · last release 2021-08-09 · [PyPI](https://pypi.org/project/qudida/)

<details><summary>README extract</summary>

QuDiDA is a micro library for very naive though quick pixel level image domain adaptation via `scikit-learn` transformers.
Is assumed to be used as image augmentation technique, while was not tested in public benchmarks.

Example:
```python
import cv2

from sklearn.decomposition import PCA
from qudida import DomainAdapter

adapter = DomainAdapter(transformer=PCA(n_components=1), ref_img=cv2.imread('target.png'))
source = cv2.imread('source.png')
result = adapter(source)
cv2.imwrite('../result.png', result)
```

Sections: QuDiDA (QUick and DIrty Domain Adaptation), Usage, Example

</details>

### quinn

Pyspark helper methods to maximize developer efficiency

`pip install quinn` · installs (wheel) · licence: Apache Software License · rank 6258 · last release 2024-02-13 · [PyPI](https://pypi.org/project/quinn/)

<details><summary>README extract</summary>

Pyspark helper methods to maximize developer productivity.

Quinn provides DataFrame validation functions, useful column functions / DataFrame transformations, and performant helper functions.

Quinn is uploaded to PyPi and can be installed with this command:

Example:
```python
import quinn
```

Sections: Quinn, Setup, Quinn Helper Functions, DataFrame Validations, Functions, Transformations, DataFrame Helpers, Schema Helpers, Pyspark Core Class Extensions, Column Extensions, Code Style

</details>

### quests

Quick Uncertainty and Entropy from STructural Similarity

`pip install quests` · installs (wheel) · licence: not stated · rank 7055 · last release 2026-02-22 · [PyPI](https://pypi.org/project/quests/)

<details><summary>README extract</summary>

QUESTS provides model-free uncertainty and entropy estimation methods for interatomic potentials.
Among the methods, we propose a structural descriptor and information-theoretical strategy that:

1. Is fast to compute, as it uses only distances between atoms within an environment. ...

Example:
```python
from ase.io import read
from quests.descriptor import get_descriptors
from quests.entropy import entropy, diversity

dset = read("dataset.xyz", index=":")
x = get_descriptors(dset, k=32, cutoff=5.0)
h = 0.015
batch_size = 10000
H = entropy(x, h=h, batch_size=batch_size)
D = diversity(x, h=h, batch_size=batch_size)
```

...

</details>

### qwen-tts

Qwen-TTS python package

`pip install qwen-tts` · installs (wheel) · licence: Apache-2.0 · rank 7222 · last release 2026-02-06 · [PyPI](https://pypi.org/project/qwen-tts/) · [source](https://github.com/Qwen/Qwen3-TTS)

<details><summary>README extract</summary>

🤗 Hugging Face | 🤖 ModelScope | 📑 Blog | 📑 Paper

🖥️ Hugging Face Demo | 🖥️ ModelScope Demo | 💬 WeChat (微信) | 🫨 Discord | 📑 API

We release Qwen3-TTS, a series of powerful speech generation capabilities developed by Qwen, offering comprehensive support for voice clone, voice design, ultra-high-quality human-like speech generation, and natural ...

Example:
```python
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice",
    device_map="cuda:0",
    dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
)

# single inference
wavs, sr = model.generate_custom_voice(
...
```

...

</details>

### qrcode_terminal

Python QRCode Terminal

`pip install qrcode_terminal` · installs from source (sdist only) · licence: MIT · rank 8136 · last release 2017-12-05 · [PyPI](https://pypi.org/project/qrcode_terminal/)

### qdk

Quantum Development Kit Python Package

`pip install qdk` · installs (wheel) · licence: MIT License · rank 8465 · last release 2026-10-08 · [PyPI](https://pypi.org/project/qdk/)

<details><summary>README extract</summary>

The Quantum Development Kit (QDK) provides a single, cohesive Python entry point for compiling, simulating, and estimating resources for quantum programs (Q# and OpenQASM), with optional extras for visualization, cloud workflows, and interoperability with Qiskit and Cirq.

Example:
```python
from qdk import qsharp

result = qsharp.run("{ use q = Qubit(); H(q); return MResetZ(q); }", shots=100)
print(result)
```

Sections: qdk, Quick Start, OpenQASM parsing and analysis, Public API Surface, Error Correction Preview, Submodules, Top level exports, Configuration Map, Telemetry

</details>

### qds-sdk

Python SDK for coding to the Qubole Data Service API

`pip install qds-sdk` · installs (wheel) · licence: Apache Software License · rank 9011 · last release 2025-03-06 · [PyPI](https://pypi.org/project/qds-sdk/)

<details><summary>README extract</summary>

A Python module that provides the tools you need to authenticate with,
and use the Qubole Data Service API.

Example:
```python
from qds_sdk.qubole import Qubole

Qubole.configure(api_token='ksbdvcwdkjn123423')

# or

Qubole.configure(api_token='ksbdvcwdkjn123423', api_url='
```

Sections: Qubole Data Service Python SDK, From PyPI, From source, CLI, SDK API

</details>

### qase-api-client

Qase TestOps API V1 client for Python

`pip install qase-api-client` · installs (wheel) · licence: not stated · rank 9279 · last release 2026-08-25 · [PyPI](https://pypi.org/project/qase-api-client/)

<details><summary>README extract</summary>

Qase TestOps API v1 Specification.

This Python package is automatically generated by the OpenAPI Generator project:

- API version: 1.0.0
- Generator version: 7.15.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit

Python 3.9+

Example:
```python
import qase.api_client_v1
from qase.api_client_v1.rest import ApiException
from pprint import pprint
import certifi

# Defining the host is optional and defaults to
# See configuration.py for a list of all supported configuration parameters.
configuration = qase.api_client_v1.Configuration(
    host = "
)

...
```

Sections: qase-api-client, Requirements, Setuptools, Tests, Getting Started, Documentation for API Endpoints, Documentation For Models, TokenAuth

</details>

### qase-api-v2-client

Qase TestOps API V2 client for Python

`pip install qase-api-v2-client` · installs (wheel) · licence: not stated · rank 9373 · last release 2026-08-25 · [PyPI](https://pypi.org/project/qase-api-v2-client/)

<details><summary>README extract</summary>

Qase TestOps API v2 Specification.

This Python package is automatically generated by the OpenAPI Generator project:

- API version: 2.0.0
- Generator version: 7.15.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
 For more information, please visit

Python 3.9+

Example:
```python
from qase.api_client_v2.rest import ApiException
from pprint import pprint
import certifi

# Defining the host is optional and defaults to
# See configuration.py for a list of all supported configuration parameters.
configuration = qase.api_client_v2.Configuration(
    host="
)

configuration.ssl_ca_cert = certifi.where()

...
```

Sections: qase, Requirements, Setuptools, Tests, Getting Started, Documentation for API Endpoints, Documentation For Models, TokenAuth

</details>

### qontract-reconcile

Collection of tools to reconcile services with their desired state as defined in the app-interface DB.

`pip install qontract-reconcile` · installs (wheel) · licence: Apache 2.0 · rank 9447 · last release 2024-12-10 · [PyPI](https://pypi.org/project/qontract-reconcile/) · [docs](https://github.com/app-sre/qontract-reconcile) · [source](https://github.com/app-sre/qontract-reconcile)

<details><summary>README extract</summary>

[][pypi-link]
[][pypi-link]

A tool to reconcile services with their desired state as defined in app-interface.
Additional tools that use the libraries created by the reconciliations are also hosted here.

Sections: qontract-reconcile, Usage, OpenShift usage, Available Integrations, Tools, Image build, Prepare config.toml, Run qontract-server, Trigger integration, Query Classes, Workflow, Troubleshooting, Code style guide

</details>

### qwen-asr

Qwen-ASR python package

`pip install qwen-asr` · installs (wheel) · licence: Apache-2.0 · rank 9804 · last release 2026-01-30 · [PyPI](https://pypi.org/project/qwen-asr/) · [source](https://github.com/Qwen/Qwen3-ASR)

<details><summary>README extract</summary>

🤗 Hugging Face | 🤖 ModelScope | 📑 Blog | 📑 Paper

🖥️ Hugging Face Demo | 🖥️ ModelScope Demo | 💬 WeChat (微信) | 🫨 Discord | 📑 API

We release Qwen3-ASR, a family that includes two powerful all-in-one speech recognition models that support language identification and ASR for 52 languages and dialects, as well as a novel non-autoregressive speech ...

Example:
```python
import torch
from qwen_asr import Qwen3ForcedAligner

model = Qwen3ForcedAligner.from_pretrained(
    "Qwen/Qwen3-ForcedAligner-0.6B",
    dtype=torch.bfloat16,
    device_map="cuda:0",
    # attn_implementation="flash_attention_2",
)

results = model.align(
    audio="
    text="甚至出现交易几乎停滞的情况。",
    language="Chinese",
)

print(results[0])
...
```

...

</details>

### quantconnect-stubs

Type stubs for QuantConnect's Lean

`pip install quantconnect-stubs` · installs (wheel) · licence: Apache Software License · rank 10510 · last release 2026-11-06 · [PyPI](https://pypi.org/project/quantconnect-stubs/)

<details><summary>README extract</summary>

This package contains type stubs for QuantConnect's Lean algorithmic trading engine and for parts of the .NET library that are used by Lean.

These stubs can be used by editors to provide type-aware features like autocomplete and auto-imports in QuantConnect strategies written in Python. ...

Example:
```python
from AlgorithmImports import *
```

</details>

### qsAPI

qsAPI - a client for Qlik Sense QPS and QRS interfaces

`pip install qsAPI` · installs (wheel) · licence: MIT License · rank 11020 · last release 2020-10-22 · [PyPI](https://pypi.org/project/qsAPI/)

<details><summary>README extract</summary>

qsAPI is a client for Qlik Sense QPS and QRS interfaces written in python that provides an environment for managing a Qlik Sense site via programming or interactive console. The module provides a set of commands for viewing and editing configuration settings, as well as managing tasks and other features available through APIs.

Example:
```python
>>> qrs=qsAPI.QRS(proxy='hostname', certificate='path\\client.pem')
```

Sections: About, Usage, Connecting with certificates, Connecting with windows credentials (NTLM), Examples, Count users using a filter, Duplicate an application in the server, Export an application, Export all published applications to directories, Retrieve a list of sessions for a user, More examples, Command Line, TODO

</details>

### Quandl

Package for quandl API access

`pip install Quandl` · installs (wheel) · licence: MIT License · rank 11093 · last release 2021-11-11 · [PyPI](https://pypi.org/project/Quandl/)

<details><summary>README extract</summary>

A Python library for Quandl's RESTful API.

You can install this package by using the pip tool and installing:

 $ pip install quandl

Or:

 $ easy_install quandl

Sections: Official Quandl API Client for Python, Setup, Usage

</details>

### qwasm

WebAssembly decoder & disassembler

`pip install qwasm` · installs (wheel) · licence: MIT · rank 11488 · last release 2022-10-05 · [PyPI](https://pypi.org/project/qwasm/)

### quarto

Python Interface to 'Quarto' Markdown Publishing System

`pip install quarto` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 11552 · last release 2021-02-03 · [PyPI](https://pypi.org/project/quarto/)

_README extract left out: share-alike licence._

### quixstreams

Python library for building stream processing applications with Apache Kafka

`pip install quixstreams` · installs (wheel) · licence: Apache Software License · rank 12206 · last release 2026-10-15 · [PyPI](https://pypi.org/project/quixstreams/)

<details><summary>README extract</summary>

Quix Streams is an end-to-end framework for real-time Python data engineering, operational analytics and machine learning on Apache Kafka data streams. Extract, transform and load data reliably in fewer lines of code using your favourite Python libraries. ...

Features:
Quix Streams provides the following features to make your life easier:

- Pure Python, meaning no wrappers around Java and no cross-language debugging.
- Streaming DataFrame API for building tabular data processing pipelines. ...

Example:
```python
from quixstreams import Application

# A minimal application reading temperature data in Celsius from the Kafka topic,
# converting it to Fahrenheit and producing alerts to another topic.

# Define an application that will connect to Kafka
app = Application(
...

</details>

### qwen-agent

Qwen-Agent: Enhancing LLMs with Agent Workflows, RAG, Function Calling, and Code Interpreter.

`pip install qwen-agent` · installs (wheel) · licence: not stated · rank 12709 · last release 2026-02-16 · [PyPI](https://pypi.org/project/qwen-agent/)

<details><summary>README extract</summary>

中文 ｜ English

 💜 Qwen Chat | 🤗 Hugging Face | 🤖 ModelScope | 📑 Blog ｜ 📖 Documentation

📊 Benchmark | 💬 WeChat (微信) | 🫨 Discord

Qwen-Agent is a framework for developing LLM applications based on the instruction following, tool usage, planning, and
memory capabilities of Qwen. ...

Sections: News, Getting Started, Preparation: Model Service, FAQ, How to Use the Code Interpreter Tool?, How to Use MCP?, Do you have function calling (aka tool calling)?, How to pass LLM parameters to the Agent?, Application: BrowserQwen, Disclaimer

</details>

### quarto-cli

Open-source scientific and technical publishing system built on Pandoc.

`pip install quarto-cli` · installs from source (sdist only) · licence: MIT License · rank 13165 · last release 2026-11-02 · [PyPI](https://pypi.org/project/quarto-cli/) · [source](https://www.github.com/quarto-dev/quarto-cli)

<details><summary>README extract</summary>

<!-- -*- mode: gfm -*- -->

Quarto is an open-source scientific and technical publishing system built on Pandoc. Quarto documents are authored using markdown, an easy to write plain text format.

In addition to the core capabilities of Pandoc, Quarto includes:

1. ...

</details>

### qm-saas

QM Simulator as a Service is a client library to launch simulator instances for QUA programs.

`pip install qm-saas` · installs (wheel) · licence: BSD License · rank 13658 · last release 2026-09-30 · [PyPI](https://pypi.org/project/qm-saas/)

<details><summary>README extract</summary>

Run Quantum Machines' QUA simulator instances at scale.

This package provides a client to use the QM OPX simulator cloud service. It allows you to run QUA programs and retrieve the results on several instances in the cloud.

To learn how to use this package, please visit the documentation website at:

</details>

### qm-octave

SDK to control an Octave with QUA

`pip install qm-octave` · does not install on CPython 3.14 · licence: BSD License · rank 13829 · last release 2025-07-01 · [PyPI](https://pypi.org/project/qm-octave/)

<details><summary>README extract</summary>

Quantum machine's Octave sdk

Versions

Version Number | Description |

1.0.0 | Initial release |
1.0.3 | Bugfix release |
1.1.0 | Stable release |
1.2.0 | Release compatible with new calibration API released |
 | as part of QUA SDK version 1.1.5 |

</details>

### qrbill

A library to generate Swiss QR-bill payment slips.

`pip install qrbill` · installs (wheel) · licence: MIT · rank 14024 · last release 2025-11-05 · [PyPI](https://pypi.org/project/qrbill/)

<details><summary>README extract</summary>

From 2020, Swiss payment slips will progressively be converted to the
QR-bill format.
Specifications can be found on

This library is aimed to produce properly-formatted QR-bills as SVG files
either from command line input or by using the `QRBill` class.

Example:
```python
>>> from qrbill import QRBill
>>> my_bill = QRBill(
        account='CH5800791123000889012',
        creditor={
            'name': 'Jane', 'pcode': '1000', 'city': 'Lausanne', 'country': 'CH',
        },
        amount='22.45',
    )
>>> my_bill.as_svg('/tmp/my_bill.svg')
```

Sections: Python library to generate Swiss QR-bills, Command line usage example, Python usage example, Outputting as PDF or bitmap, Running tests

</details>

### quartz-cron-checker

Simple Python library to check if a Quartz cron expression is valid.

`pip install quartz-cron-checker` · installs (wheel) · licence: not stated · rank 14076 · last release 2026-10-29 · [PyPI](https://pypi.org/project/quartz-cron-checker/)

<details><summary>README extract</summary>

quartz-cron-checker is a lightweight (zero dependencies!), strict validator for Quartz-style cron expressions in Python.

It ensures all parts of the cron string conform to the Quartz cron spec—including support for special characters, named values, and mutual exclusivity of day-of-month and day-of-week.

Features:
- ✅ Full support for 6- or 7-field Quartz cron expressions (`second minute hour day-of-month month day-of-week [year]`)
- ✅ Literal handling (`*`, `?`, `L`, `W`, `#`)
- ✅ Named months (`JAN`, `FEB`, etc.) and days (`MON`, `TUE`, etc.) ...

Example:
```python
from quartz_cron_checker import QuartzCronChecker

# Parse and validate a cron string
cron = QuartzCronChecker.from_cron_string("0 0 12 ? * MON-FRI")
cron.validate()  # Raises if invalid

...

</details>

### qt-material

Material inspired stylesheet for PySide6 and PyQt6.

`pip install qt-material` · installs (wheel) · licence: BSD License · rank 14208 · last release 2025-04-21 · [PyPI](https://pypi.org/project/qt-material/) · [docs](https://qt-material.readthedocs.io/en/latest/) · [source](https://github.com/dunderlab/qt-material.git)

<details><summary>README extract</summary>

This is another stylesheet for PySide6, and PyQt6, which looks like Material Design (close enough).

There is some custom dark themes:

And light:

 * Install
 * Usage
 * Themes
 * Custom colors
 * Usage
 * Light themes
 * Environ variables
 * Alternative QPushButtons and custom fonts
 * Custom stylesheets
 * Run examples
 * New themes
 * Change ...

Example:
```python
import sys
from PySide6 import QtWidgets
# from PySide2 import QtWidgets
# from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
apply_stylesheet(app, theme='dark_teal.xml')

# run
window.show()
...
```

...

</details>

### quicksectx

Quicksect is a fast python / cython implementation of interval search.

`pip install quicksectx` · installs from source (sdist only) · licence: MIT License · rank 14399 · last release 2025-08-25 · [PyPI](https://pypi.org/project/quicksectx/) · [source](https://github.com/jianlins/quicksectx)

<details><summary>README extract</summary>

Quicksect is a fast python / cython implementation of interval search based on the pure python version in
bx-python
I pulled it out, optimized and converted to cython and James Taylor has incoporated it back into bx-python
with his improvements. ...

Sections: Quicksect, Description, Use, Test, Low-Level, For Dev

</details>

### quartodoc

Generate API documentation with Quarto.

`pip install quartodoc` · installs (wheel) · licence: MIT License · rank 14517 · last release 2025-06-10 · [PyPI](https://pypi.org/project/quartodoc/) · [source](https://github.com/machow/quartodoc)

<details><summary>README extract</summary>

Features:
quartodoc lets you quickly generate Python package API reference
documentation using Markdown and Quarto. quartodoc
is designed as an alternative to
Sphinx. ...

Sections: Overview, Basic use, Rebuilding site, Looking up objects, Learning more

</details>

