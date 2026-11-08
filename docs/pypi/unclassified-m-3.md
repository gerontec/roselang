# Unclassified / M (part 3 of 3)

[Index](README.md) · 770 packages in this topic, by downloads.

[part 1](unclassified-m.md) · [part 2](unclassified-m-2.md) · part 3

### multiformats-config

Pre-loading configuration module for the 'multiformats' package.

`pip install multiformats-config` · installs (wheel) · licence: not stated · rank 12376 · last release 2023-12-18 · [PyPI](https://pypi.org/project/multiformats-config/)

<details><summary>README extract</summary>

This module provides configuration and table information for the multiformats library.

</details>

### memoized-property

A simple python decorator for defining properties that only run their fget function once

`pip install memoized-property` · installs from source (sdist only) · licence: BSD License · rank 12401 · last release 2016-09-29 · [PyPI](https://pypi.org/project/memoized-property/)

<details><summary>README extract</summary>

A simple python decorator for defining properties that only run their fget function once.

* Free software: BSD license

A Python property that only calls its `fget` function one time. How many times have you written
this code (or similar)?

I've written it just enough times to be annoyed enough to capture this module. The result is this:

Features:
I couldn't find a pre-existing version of this on PyPI. I found one other on GitHub,
 but it was not published to PyPI.

Example:
```python
def class C(object):

    @property
    def name(self):
        if not hasattr(self, '_name'):
            self._name = some_expensive_load()
        return self._name
```

Sections: memoized_property, What?, Why?, 1.0.3 (2016-09-28), 1.0.2 (2014-05-02), 1.0.1 (2014-01-01), 1.0.0 (2013-12-26)

</details>

### marker-pdf

Convert documents to markdown with high speed and accuracy.

`pip install marker-pdf` · installs (wheel) · licence: Apache-2.0 · rank 12418 · last release 2026-10-29 · [PyPI](https://pypi.org/project/marker-pdf/) · [source](https://github.com/datalab-to/marker)

<details><summary>README extract</summary>

State of the Art models for Document Intelligence

Marker converts documents to markdown, JSON, chunks, and HTML quickly and accurately.

- Converts PDF, image, PPTX, DOCX, XLSX, HTML, EPUB files in all languages
- Formats tables, forms, equations, inline math, links, references, and code blocks
- Extracts and saves images ...

Example:
```python
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

converter = PdfConverter(
    artifact_dict=create_model_dict(),
)
rendered = converter("FILEPATH")
text, _, images = text_from_rendered(rendered)
```

...

</details>

### msads

A library to make working with the Bing Ads APIs and bulk services easy

`pip install msads` · installs from source (sdist only) · licence: MIT License · rank 12451 · last release 2026-10-14 · [PyPI](https://pypi.org/project/msads/)

<details><summary>README extract</summary>

.. image:: :target:

The Bing Ads Python Software Development Kit (SDK) Version 13.0 enhances the experience of developing Bing Ads applications
with the Python programming language.
The SDK includes classes for all Bing Ads REST API web services and abstracts the low level details of authentication with OAuth. ...

Sections: Bing Ads Python SDK, Getting Started, External Dependencies

</details>

### moondream

Official Python interface for Moondream Cloud and Photon local inference.

`pip install moondream` · installs (wheel) · licence: not stated · rank 12456 · last release 2026-09-30 · [PyPI](https://pypi.org/project/moondream/)

<details><summary>README extract</summary>

Official Python interface for Moondream Cloud and Photon local inference on NVIDIA GPUs, Apple Silicon Macs, or CPUs where the selected model supports them.

Features:
Photon exposes each selected model's capabilities through one model-bound client:

| Method | Description |

| `caption` | Generate descriptive captions for images |
| `query` | Ask questions about image content |
| `chat` | Continue multi-turn ...

Example:
```python
import moondream as md
from PIL import Image

# Initialize with Moondream Cloud
model = md.vl(api_key="<your-api-key>")

# Or initialize Photon local inference on a device supported by the model
model = md.photon("moondream3.1-9B-A2B")

# Load an image
image = Image.open("path/to/image.jpg")

# Generate a caption
...
```

...

</details>

### marshmallow-mongoengine

Mongoengine integration with the marshmallow (de)serialization library

`pip install marshmallow-mongoengine` · installs (wheel) · licence: MIT License · rank 12564 · last release 2023-03-14 · [PyPI](https://pypi.org/project/marshmallow-mongoengine/)

<details><summary>README extract</summary>

Mongoengine integration with the marshmallow (de)serialization library.

See documentation at

Example:
```python
import mongoengine as me

class Author(me.Document):
    id = me.IntField(primary_key=True, default=1)
    name = me.StringField()
    books = me.ListField(me.ReferenceField('Book'))

    def repr(self):
        return '<Author(name={self.name!r})>'.format(self=self)

class Book(me.Document):
    title = me.StringField()
```

Sections: marshmallow-mongoengine, Declare your models, Generate marshmallow schemas, (De)serialize your data, Get it now

</details>

### mattermostdriver

A Python Mattermost Driver

`pip install mattermostdriver` · installs (wheel) · licence: MIT · rank 12595 · last release 2022-01-21 · [PyPI](https://pypi.org/project/mattermostdriver/)

<details><summary>README extract</summary>

The repository will try to keep up with the master of

If something changes, it is most likely to change because the official mattermost api changed.

Python 3.5 or later is required.

Example:
```python
from mattermostdriver import Driver

foo = Driver({
    """
    Required options

    Instead of the login/password, you can also use a personal access token.
    If you have a token, you don't need to pass login/pass.
    It is also possible to use 'auth' to pass a auth header in directly,
    for an example, see:

    """
...
```

Sections: Python Mattermost Driver (APIv4), Info, Documentation, Usage

</details>

### mitmproxy-windows

(no summary)

`pip install mitmproxy-windows` · installs (wheel) · licence: LGPL-3.0-or-later · rank 12621 · last release 2026-10-22 · [PyPI](https://pypi.org/project/mitmproxy-windows/) · [source](https://github.com/mitmproxy/mitmproxy-rs)

_README extract left out: share-alike licence._

### mt5linux

MetaTrader5 for linux users

`pip install mt5linux` · installs (wheel) · licence: MIT · rank 12648 · last release 2026-08-04 · [PyPI](https://pypi.org/project/mt5linux/)

<details><summary>README extract</summary>

<!-- final pipeline test -->

A package that uses Wine, RPyC, and mt5server.exe (a standalone binary with all dependencies) to run MetaTrader5 on Linux.

For an explanation of who should use mt5linux and why, see Motivation and Use Cases.

Example:
```python
from mt5linux import MetaTrader5

mt5 = MetaTrader5(
    host="localhost",
    mt5_login=12345678,
    mt5_password="your_password",
    mt5_server="Broker-Server",
    engine="auto",        # 'auto', 'docker', or 'udocker'
    image_tag="latest",   # Docker image tag
    ui_port=8080,         # noVNC http port (auto-selected if None)
...
```

Sections: MetaTrader 5 for Linux, Docker, Usage, Option 2: Manual Docker, Option 3: Standalone Server (Linux with Wine), Accessing Container Properties, Thanks

</details>

### mflux

MLX native implementations of state-of-the-art generative image models.

`pip install mflux` · installs (wheel) · licence: not stated · rank 12651 · last release 2026-10-27 · [PyPI](https://pypi.org/project/mflux/)

<details><summary>README extract</summary>

Run the latest state-of-the-art generative image models locally on your Mac in native MLX!

Sections: About, 💡 Philosophy, 🎨 Models, ✨ Features, 🌱 Related projects, Build a UI under `mflux.web`, Extras under `mflux.extras`

</details>

### mailersend

The official MailerLite Python SDK

`pip install mailersend` · installs (wheel) · licence: not stated · rank 12710 · last release 2026-10-26 · [PyPI](https://pypi.org/project/mailersend/)

### mocksftp

Mock SFTP server for testing purposes

`pip install mocksftp` · installs (wheel) · licence: MIT License · rank 12716 · last release 2018-03-21 · [PyPI](https://pypi.org/project/mocksftp/)

<details><summary>README extract</summary>

In-process SFTP server for testing your SFTP related client code.

Example:
```python
from contextlib import closing
import py.path

def test_open_file(sftp_server, sftp_client):
    # Write directly in the server root.
    root_path = py.path.local(sftp_server.root)
    root_path.join('file.txt').write('content')

    # Access the folder via the client
    sftp = sftp_client.open_sftp()
    assert sftp.listdir('.') == ['file.txt']
...
```

Sections: mocksftp - Easily test your sftp client code, Usage example, Alternatives

</details>

### markdown-code-runner

Automatically execute code blocks within a Markdown file and update the output in-place

`pip install markdown-code-runner` · installs (wheel) · licence: MIT License · rank 12737 · last release 2026-01-24 · [PyPI](https://pypi.org/project/markdown-code-runner/) · [docs](https://markdown-code-runner.nijho.lt)

<details><summary>README extract</summary>

`markdown-code-runner` is a Python package that automatically executes code blocks within a Markdown file, including hidden code blocks, and updates the output in-place.
This package is particularly useful for maintaining Markdown files with embedded code snippets, ensuring that the output displayed is up-to-date and accurate. ...

Features:
- Automatically execute code blocks, including hidden code blocks, within a Markdown file
- Allows hidden code blocks (i.e., code blocks that are not displayed in the Markdown file) to generate content like tables, plots, etc. ...

Example:
```python
from markdown_code_runner import update_markdown_file

update_markdown_file("path/to/your/markdown_file.md")
```

...

</details>

### mock-firestore

In-memory implementation of Google Cloud Firestore for use in tests

`pip install mock-firestore` · installs (wheel) · licence: MIT License · rank 12783 · last release 2022-01-24 · [PyPI](https://pypi.org/project/mock-firestore/)

<details><summary>README extract</summary>

An in-memory implementation of the Python client library for Google Cloud Firestore, intended for use in tests to replace the real thing. This project is in early stages and is only a partial implementation of the real client library.

To install:

`pip install mock-firestore`

Python 3.6+ is required for it to work.

Example:
```python
db = firestore.Client()
mock_db = MockFirestore()

# Can be used in the same way as a firestore.Client() object would be, e.g.:
db.collection('users').get()
mock_db.collection('users').get()
```

Sections: Python Mock Firestore, Usage, Running the tests

</details>

### meltano

Meltano is your CLI for ELT+: Open Source, Flexible, and Scalable. Move, transform, and test your data with confidence using a streamlined data engineering workflow you’ll love.

`pip install meltano` · installs (wheel) · licence: MIT · rank 12798 · last release 2026-10-07 · [PyPI](https://pypi.org/project/meltano/) · [docs](https://docs.meltano.com) · [source](https://github.com/meltano/meltano)

<details><summary>README extract</summary>

Unlock 600+ APIs and DBs and realize your wildest data and ML-powered product ideas.

Meltano Hub is the single source of truth to find any Meltano plugins as well as Singer taps and targets. Users are also able to add more plugins to the Hub and have them immediately discoverable and usable within Meltano. ...

Sections: The declarative code-first data integration engine, Integrations, Docker Images, Documentation, Responsible Disclosure Policy

</details>

### macwinnie-enhanced-logging

Batteries-included logging for Python applications.

`pip install macwinnie-enhanced-logging` · installs (wheel) · licence: not stated · rank 12804 · last release 2026-03-06 · [PyPI](https://pypi.org/project/macwinnie-enhanced-logging/)

<details><summary>README extract</summary>

Last built version: `v0.1.3`

Batteries-included logging for Python applications.

`macwinnie-enhanced-logging` provides a clean, consistent logging setup built on top of:

- Python’s built-in `logging` module (so third-party libraries keep working normally)
- `structlog` (so *your* logs are structured, predictable, and easy to analyze) ...

Features:
- Works with standard Python logging
- Structured logging with structlog
- Human-friendly console output for development
- JSON output for log pipelines and observability stacks
- Optional callsite information (file/function/line) ...

Example:
```python
from enhanced_logging import configure_logging, LogConfig

configure_logging(
    LogConfig(
        format="json",
        level="INFO",
        app_name="my-service"
    )
)
```

...

</details>

### macwinnie-py-pushover-client

Pushover client for Python projects.

`pip install macwinnie-py-pushover-client` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+); Other/Proprietary Licen · rank 12914 · last release 2026-04-22 · [PyPI](https://pypi.org/project/macwinnie-py-pushover-client/) · [source](https://github.com/macwinnie/python-pushover/)

_README extract left out: share-alike licence._

### mitmproxy-macos

(no summary)

`pip install mitmproxy-macos` · installs (wheel) · licence: MIT · rank 12917 · last release 2026-10-22 · [PyPI](https://pypi.org/project/mitmproxy-macos/) · [source](https://github.com/mitmproxy/mitmproxy-rs)

<details><summary>README extract</summary>

This package contains the following precompiled binaries for macOS:

 - `macos-certificate-truster.app`: A helper app written in Rust to mark the mitmproxy CA as trusted.
 - `Mitmproxy Redirector.app`: The app bundle that sets up and hosts the network extension for redirecting traffic.

</details>

### macwinnie-sqlite3

Pushover client for Python projects.

`pip install macwinnie-sqlite3` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 12921 · last release 2026-04-22 · [PyPI](https://pypi.org/project/macwinnie-sqlite3/)

_README extract left out: share-alike licence._

### ms-swift

Swift: Scalable lightWeight Infrastructure for Fine-Tuning

`pip install ms-swift` · installs (wheel) · licence: Apache Software License · rank 12952 · last release 2026-10-13 · [PyPI](https://pypi.org/project/ms-swift/)

<details><summary>README extract</summary>

ModelScope Community Website

 中文 ｜ English

 Paper ｜ English Documentation ｜ 中文文档

Example:
```python
from peft import LoraConfig, get_peft_model
from swift import get_model_processor, get_template, load_dataset, EncodePreprocessor
from swift.trainers import Seq2SeqTrainer, Seq2SeqTrainingArguments
# Retrieve the model and template, and add a trainable LoRA module
model, tokenizer = get_model_processor(model_id_or_path, ...)
...
```

Sections: SWIFT (Scalable lightWeight Infrastructure for Fine-Tuning), ☎ Groups, 📝 Introduction, 🎉 News, 🚀 Quick Start, Command Line Interface (Recommended), Web-UI, Using Python, ✨ Usage, Training, Megatron-SWIFT, Reinforcement Learning, Inference, Interface Inference

</details>

### multimodars

A Rust-powered cardiac multi-image modality fusion package

`pip install multimodars` · installs (wheel) · licence: MIT License · rank 12970 · last release 2026-11-06 · [PyPI](https://pypi.org/project/multimodars/)

<details><summary>README extract</summary>

"One package to fuse them all."

 — The Lord of the Rings (probably)

> A high‑performance, Rust‑accelerated toolkit for multi‑modality cardiac image fusion and registration ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ.

Features:
`multimoda-rs` aligns and fuses diverse cardiac imaging modalities — IVUS, OCT and CCTA — into unified high-resolution 3D models. ...

Example:
```python
import multimodars as mm
import numpy as np

# Align four intravascular phases (rest-dia, rest-sys, stress-dia, stress-sys)
rest, stress, dia, sys, _ = mm.from_file_full(
    "examples/data/ivus_rest",    # input_path_ab
    "examples/data/ivus_stress",  # input_path_cd
    write_obj=True,
    output_path_ab="output/rest",
...
```

Sections: Overview, Key Features, Quick Example, Pipeline, Documentation

</details>

### music-assistant-client

Music Assistant Client

`pip install music-assistant-client` · installs (wheel) · licence: Apache-2.0 · rank 13002 · last release 2026-11-07 · [PyPI](https://pypi.org/project/music-assistant-client/) · [source](https://github.com/music-assistant/client)

<details><summary>README extract</summary>

Python client to interact with the Music Assistant Server API

Example:
```python
import asyncio
from music_assistant_client import MusicAssistantClient, login_with_token

async def main():
    # Get a token (do this once and save it)
    user, token = await login_with_token(
        "
        "admin",
        "password"
    )

    # Connect to the server
    async with MusicAssistantClient(" None, token=token) as client:
...
```

Sections: Music Assistant Client, Authentication, 1. Using a Long-Lived Token (Recommended), 2. Manual Token Management, 3. Using Username and Password Directly, Backward Compatibility, API Reference, Client Class, Example Usage, Error Handling

</details>

### monocle-apptrace

package with monocle genAI tracing

`pip install monocle-apptrace` · installs (wheel) · licence: Apache Software License · rank 13098 · last release 2026-10-30 · [PyPI](https://pypi.org/project/monocle-apptrace/)

<details><summary>README extract</summary>

Monocle helps developers and platform engineers building or managing GenAI apps monitor these in prod by making it easy to instrument their code to capture traces that are compliant with open-source cloud-native observability ecosystem. ...

Example:
```python
from monocle_apptrace.instrumentor import setup_monocle_telemetry
```

Sections: Monocle Apptrace, Use Monocle, Claude Code Instrumentation, Codex CLI Instrumentation, GitHub Copilot Instrumentation

</details>

### mathruler

(no summary)

`pip install mathruler` · installs (wheel) · licence: not stated · rank 13133 · last release 2025-02-22 · [PyPI](https://pypi.org/project/mathruler/)

### mkdocs-htmlproofer-plugin

A MkDocs plugin that validates URL in rendered HTML files

`pip install mkdocs-htmlproofer-plugin` · installs (wheel) · licence: MIT License · rank 13207 · last release 2026-09-28 · [PyPI](https://pypi.org/project/mkdocs-htmlproofer-plugin/)

<details><summary>README extract</summary>

*A MkDocs plugin that validates URLs, including anchors, in rendered html files*.

> [!NOTE]
> MkDocs 1.6+ supports native validation of anchors.

Sections: mkdocs-htmlproofer-plugin, Configuring, `enabled`, `raise_error`, `raise_error_after_finish`, `raise_error_excludes`, `ignore_urls`, `warn_on_ignored_urls`, `ignore_pages`, `validate_external_urls`, `validate_rendered_template`, `strict_anchors`, `skip_downloads`, `retry_max_times`

</details>

### momwire

A pure-Python method-of-moments antenna simulator with optional C++ accelerators

`pip install momwire` · installs (wheel) · licence: MIT License · rank 13268 · last release 2026-11-06 · [PyPI](https://pypi.org/project/momwire/)

<details><summary>README extract</summary>

A pure-Python method-of-moments antenna simulator with optional C++ accelerators (pybind11).

Extracted from antenna_designer.

`BSplineSolver` (degree-d Galerkin, default d=1/2) is the default solver;
`HMatrixSolver` and `ArrayBlockSolver` are structural accelerators built on
top of it. ...

Example:
```python
sol = solver.compute_port_solution()  # one fill, one factorisation
sol.y  # (n_ports, n_ports) short-circuit Y
sol.coeffs  # (n_dof, n_ports) — column j is the
# solution for 1 V at port j
sol.port_currents  # the same matrix as `y`, asserted
```

...

</details>

### mysql-mimic

A python implementation of the mysql server protocol

`pip install mysql-mimic` · installs (wheel) · licence: MIT · rank 13274 · last release 2026-10-07 · [PyPI](https://pypi.org/project/mysql-mimic/)

<details><summary>README extract</summary>

Pure-python implementation of the MySQL server wire protocol.

This can be used to create applications that act as a MySQL server.

Example:
```python
import asyncio

from mysql_mimic import MysqlServer, Session

class MySession(Session):
    async def query(self, expression, sql, attrs):
        print(f"Parsed abstract syntax tree: {expression}")
        print(f"Original SQL string: {sql}")
        print(f"Query attributes: {sql}")
        print(f"Currently authenticated user: {self.username}")
...
```

Sections: MySQL-Mimic, Usage, Authentication, Performance, Options

</details>

### MonthDelta

date computations with months

`pip install MonthDelta` · installs from source (sdist only) · licence: Python Software Foundation License · rank 13281 · last release 2009-04-23 · [PyPI](https://pypi.org/project/MonthDelta/)

### mkdocs-markdownextradata-plugin

A MkDocs plugin that injects the mkdocs.yml extra variables into the markdown template

`pip install mkdocs-markdownextradata-plugin` · installs (wheel) · licence: MIT License · rank 13297 · last release 2024-08-22 · [PyPI](https://pypi.org/project/mkdocs-markdownextradata-plugin/)

<details><summary>README extract</summary>

*A MkDocs plugin that injects the mkdocs.yml extra variables into the markdown template*

usecase

Sections: mkdocs-markdownextradata-plugin, Features, Use Extra Variables in your markdown files, Using external data files, Jinja2 Template Engine Configuration

</details>

### MultiMapping

Special MultiMapping objects used in Zope.

`pip install MultiMapping` · installs (wheel) · licence: ZPL-2.1 · rank 13391 · last release 2026-01-23 · [PyPI](https://pypi.org/project/MultiMapping/) · [source](https://github.com/zopefoundation/MultiMapping)

<details><summary>README extract</summary>

Features:
MultiMapping provides special objects used in some Zope internals like ZRDB.

Sections: Overview, 5.1 (2026-01-23), 5.0 (2023-02-09), 4.1 (2018-10-05), 4.0 (2017-05-17), 3.1 (2017-04-26), 3.0 (2016-04-03), 2.13.0 (2010-03-30)

</details>

### mecab-ko-dic

mecab-ko-dic packaged for Python

`pip install mecab-ko-dic` · installs from source (sdist only) · licence: not stated · rank 13406 · last release 2021-02-19 · [PyPI](https://pypi.org/project/mecab-ko-dic/)

<details><summary>README extract</summary>

This is a Korean dictionary for the MeCab tokenizer, packaged for use in Python
with mecab-python3 or
fugashi.

We (at Luminoso) think this is probably a better way to find tokens in Korean
words than just splitting the text on spaces would be. We also know that MeCab
wasn't designed for Korean. ...

Sections: mecab-ko-dic, Should you use this?, Usage

</details>

### mongo-tooling-metrics

A slim library which leverages Pydantic to reliably collect type enforced metrics and store them to MongoDB.

`pip install mongo-tooling-metrics` · installs (wheel) · licence: not stated · rank 13441 · last release 2023-06-01 · [PyPI](https://pypi.org/project/mongo-tooling-metrics/)

### msldap

Python library to play with MS LDAP

`pip install msldap` · installs (wheel) · licence: MIT License · rank 13448 · last release 2025-05-25 · [PyPI](https://pypi.org/project/msldap/)

### motmetrics

Metrics for multiple object tracker benchmarking.

`pip install motmetrics` · installs (wheel) · licence: MIT · rank 13486 · last release 2022-12-26 · [PyPI](https://pypi.org/project/motmetrics/)

<details><summary>README extract</summary>

The py-motmetrics library provides a Python implementation of metrics for benchmarking multiple object trackers (MOT).

While benchmarking single object trackers is rather straightforward, measuring the performance of multiple object trackers needs careful design as multiple correspondence constellations can arise (see image below). ...

Features:
- _Variety of metrics

 Provides MOTA, MOTP, track quality measures, global ID measures and more. The results are comparable with the popular MOTChallenge benchmarks (\*1).
- _Distance agnostic ...

Example:
```python
import motmetrics as mm
# List all default metrics
mh = mm.metrics.create()
print(mh.list_metrics_markdown())
```

...

</details>

### marshmallow-jsonapi

JSON API 1.0 (https://jsonapi.org) formatting with marshmallow

`pip install marshmallow-jsonapi` · installs (wheel) · licence: MIT License · rank 13527 · last release 2020-12-27 · [PyPI](https://pypi.org/project/marshmallow-jsonapi/)

<details><summary>README extract</summary>

Homepage:

JSON API 1.0 ( formatting with marshmallow.

marshmallow-jsonapi provides a simple way to produce JSON API-compliant data in any Python web framework.

Example:
```python
from marshmallow_jsonapi import Schema, fields

class PostSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str()

    author = fields.Relationship(
        "/authors/{author_id}", related_url_kwargs={"author_id": "<author.id>"}
    )

    comments = fields.Relationship(
        "/posts/{post_id}/comments",
...
```

Sections: marshmallow-jsonapi, Documentation, Requirements, Project Links

</details>

### modelscan

The modelscan package is a cli tool for detecting unsafe operations in model files across various model serialization formats.

`pip install modelscan` · does not install on CPython 3.14 · licence: Apache Software License · rank 13531 · last release 2026-02-18 · [PyPI](https://pypi.org/project/modelscan/)

<details><summary>README extract</summary>

Machine Learning (ML) models are shared publicly over the internet, within teams and across teams. The rise of Foundation Models have resulted in public ML models being increasingly consumed for further training/fine tuning. ML Models are increasingly used to make critical decisions and power mission-critical applications. ...

Features:
Models are often created from automated pipelines, others may come from a data scientist’s laptop. In either case the model needs to move from one machine to another before it is used. That process of saving a model to disk is called serialization. ...

Example:
```python
from modelscan.modelscan import ModelScan
from modelscan.settings import DEFAULT_SETTINGS

# Initialize ModelScan with default settings
scanner = ModelScan(settings=DEFAULT_SETTINGS)

...

</details>

### mistralai-vibe-harness

Mistral Vibe Harness runtime & bindings

`pip install mistralai-vibe-harness` · installs (wheel) · licence: Other/Proprietary License · rank 13562 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mistralai-vibe-harness/)

### mobsfscan

mobsfscan is a static analysis tool that can find insecure code patterns in your Android and iOS source code. Supports Java, Kotlin, Swift, and Objective C Code.

`pip install mobsfscan` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 13590 · last release 2026-10-27 · [PyPI](https://pypi.org/project/mobsfscan/)

_README extract left out: share-alike licence._

### multiregex

Quickly match many regexes against a string. Provides 2-10x speedups over naïve regex matching.

`pip install multiregex` · installs (wheel) · licence: BSD-3-Clause · rank 13598 · last release 2026-05-20 · [PyPI](https://pypi.org/project/multiregex/) · [source](https://github.com/quantco/multiregex)

<details><summary>README extract</summary>

Quickly match many regexes against a string. Provides 2-10x speedups over naïve regex matching.

See this introductory blog post.

Example:
```python
import multiregex

# Create matcher from multiple regexes.
my_patterns = [r"\w+@\w+\.com", r"\w\.com"]
matcher = multiregex.RegexMatcher(my_patterns)

# Run `re.search` for all regexes.
# Returns a set of matches as (re.Pattern, re.Match) tuples.
matcher.search("john.doe@example.com")
...
```

Sections: multiregex, Introduction, Usage, Custom prematchers, Disabling prematchers, Profiling prematchers

</details>

### mineru-llama-cpp

In-process llama.cpp VLM inference engine for MinerU

`pip install mineru-llama-cpp` · installs (wheel) · licence: not stated · rank 13626 · last release 2026-10-22 · [PyPI](https://pypi.org/project/mineru-llama-cpp/) · [source](https://github.com/opendatalab/mineru-llama-cpp)

<details><summary>README extract</summary>

In-process llama.cpp VLM inference engine for MinerU, exposing a single
`Engine` class with synchronous and asynchronous generate/stream methods.
Wraps a pinned build of llama.cpp
(no HTTP layer, no subprocess) via the CPython Limited API. ...

Example:
```python
from mineru_llama_cpp import Engine, SamplingParams

with Engine("/path/to/model.gguf", "/path/to/mmproj.gguf") as engine:
    result = engine.generate([{"role": "user", "content": "hello"}])
    print(result.content)

    for chunk in engine.stream([{"role": "user", "content": "hello"}]):
        print(chunk.delta, end="", flush=True)
```

...

</details>

### mockredispy

Mock for redis-py

`pip install mockredispy` · installs from source (sdist only) · licence: Apache2 · rank 13656 · last release 2016-04-18 · [PyPI](https://pypi.org/project/mockredispy/)

### mkdocs-render-swagger-plugin

MKDocs plugin for rendering swagger & openapi files.

`pip install mkdocs-render-swagger-plugin` · installs (wheel) · licence: MIT License · rank 13665 · last release 2024-05-26 · [PyPI](https://pypi.org/project/mkdocs-render-swagger-plugin/)

<details><summary>README extract</summary>

This is the Mkdocs plugin for rendering swagger &amp; openapi schemas using Swagger UI. It is written in Python.

Sections: mkdocs-render-swagger-plugin, Usage, Example, Referencing a local json, Referencing an external json, Explicit declaration of the Swagger JS library, MkDocs plugins and Swagger api

</details>

### microversion-parse

OpenStack microversion header parser

`pip install microversion-parse` · installs (wheel) · licence: Apache Software License · rank 13689 · last release 2025-12-04 · [PyPI](https://pypi.org/project/microversion-parse/) · [source](https://opendev.org/openstack/microversion-parse)

<details><summary>README extract</summary>

A small set of functions to manage OpenStack microversion headers that can
be used in middleware, application handlers and decorators to effectively
manage microversions.

Also included, in the `middleware` module, is a `MicroversionMiddleware`
that will process incoming microversion headers. ...

Example:
```python
import microversion_parse

# headers is a dict of headers with folded (comma-separated
# values) or a list of header, value tuples
version = microversion_parse.get_version(
    headers, service_type='compute',
    legacy_headers=['x-openstack-nova-api-version'])

# If headers are not already available, a dict of headers
...
```

Sections: microversion_parse, get_version, parse_version_string, extract_version, MicroversionMiddleware

</details>

### migra

Like `diff` but for PostgreSQL schemas

`pip install migra` · installs (wheel) · licence: Other/Proprietary License · rank 13705 · last release 2022-09-18 · [PyPI](https://pypi.org/project/migra/) · [source](https://github.com/djrobstep/migra)

<details><summary>README extract</summary>

- ## compare schemas
- ## autogenerate migration scripts
- ## autosync your development database from your application models
- ## make your schema changes testable, robust, and (mostly) automatic

`migra` is a schema diff tool for PostgreSQL, written in Python. Use it in your python scripts, or from the command line like this: ...

Sections: migra: Like diff but for Postgres schemas, THE DOCS, Folks, schemas are good

</details>

### martian-linguafranca

LLM API format converter with Rust core and Python bindings

`pip install martian-linguafranca` · installs (wheel) · licence: MIT License · rank 13707 · last release 2026-10-29 · [PyPI](https://pypi.org/project/martian-linguafranca/) · [source](https://github.com/withmartian/linguafranca)

<details><summary>README extract</summary>

LLM API format converter with a Rust core and Python bindings.

Converts requests, responses, and streaming events between:
- OpenAI Chat Completions
- Anthropic Messages
- Open Responses

Also supports within-format conversions: collect a stream into a single
response, or decompose a response into stream events.

Example:
```python
import linguafranca as lf

# Convert a Chat Completions request to Anthropic Messages
result = lf.convert_request_json(
    {"model": "gpt-4.1-mini", "messages": [{"role": "user", "content": "hello"}]},
    source_format=lf.FormatName.OPENAI_CHAT_COMPLETIONS,
    target_format=lf.FormatName.ANTHROPIC_MESSAGES,
)

result.value     # converted dict
...
```

...

</details>

### millify

Convert long numbers into a human-readable format in Python

`pip install millify` · installs from source (sdist only) · licence: not stated · rank 13774 · last release 2018-01-15 · [PyPI](https://pypi.org/project/millify/)

### minisaml

Minimal SAML2 client

`pip install minisaml` · installs (wheel) · licence: Apache Software License · rank 13786 · last release 2026-01-27 · [PyPI](https://pypi.org/project/minisaml/) · [docs](https://minisaml.readthedocs.io) · [source](https://github.com/HENNGE/minisaml)

<details><summary>README extract</summary>

Absolutely minimalistic SAML 2 client. Does not support the full SAML 2 specification, on purpose.
It only supports requests via HTTP Redirect and responses via HTTP POST.

Example:
```python
from minisaml.request import get_request_redirect_url

url = get_request_redirect_url(
    saml_endpoint="
    expected_audience="Your SAML Issuer",
    acs_url="
)

# This line depends on your web framework/server
redirect_user_to_url(url)
```

Sections: MiniSAML, Usage, Create a SAML Request, Validate and parse the SAML Response

</details>

### maigret

🕵️‍♂️ Collect a dossier on a person by username from thousands of sites.

`pip install maigret` · installs (wheel) · licence: MIT License · rank 13880 · last release 2026-09-18 · [PyPI](https://pypi.org/project/maigret/) · [docs](https://maigret.readthedocs.io) · [source](https://github.com/soxoj/maigret)

<details><summary>README extract</summary>

English · 简体中文 · Français

 📖 Documentation

Maigret collects a dossier on a person by username only, checking for accounts on a huge number of sites and gathering all the available information from web pages. No API keys required. AI profiling (demo).

Sections: Maigret, In one minute, Main features, Used by, Demo, Video, Reports, Windows, Cloud Shells, Snap (Linux), From source, Docker, Troubleshooting, Usage

</details>

### memory-tempfile

Helper functions to identify and use paths on the OS (Linux-only for now) where RAM-based tempfiles can be created.

`pip install memory-tempfile` · installs (wheel) · licence: MIT License · rank 13906 · last release 2020-03-11 · [PyPI](https://pypi.org/project/memory-tempfile/) · [source](https://github.com/mbello/memory-tempfile)

<details><summary>README extract</summary>

Features:
Often there is a need to temporarily save a file to 'disk' for the consumption of external tools. Or maybe you can pipe some input info to an external tool
but has no way of forcing such external tool to pipe its output straight to your software: it ...

Sections: Overview, API, The constructor, Requirements, Usage, Example 1, Example 2

</details>

### maibot-dashboard

MaiBot WebUI static assets

`pip install maibot-dashboard` · installs (wheel) · licence: not stated · rank 13927 · last release 2026-11-07 · [PyPI](https://pypi.org/project/maibot-dashboard/)

### memcache-hybrid

Python bindings for memcache_hybrid implemented with pybind11

`pip install memcache-hybrid` · does not install on CPython 3.14 · licence: Mulan PSL v2 · rank 13963 · last release 2026-10-27 · [PyPI](https://pypi.org/project/memcache-hybrid/)

<details><summary>README extract</summary>

- [2026/06] MemCache使能推理PrefixCache加速案例实践，请关注wiki主页案例库获取最新案例
- [2025/12] MemCache已作为vllm-ascend backend使能大模型推理加速，详情查看vllm-ascend开源社区，使用示例

- [2025/11] MemCache项目于2025年11月开源，开源社区地址为：

MemCache roadmap详见：Roadmap
MemCache 分支发布策略：分支发布策略

Sections: High-performance distributed key-value cache, 🔄Latest News, 🔜 Roadmap&发布策略, 🎉概述, 🧩核心组件, 📁项目结构导览, 🔥性能表现, 🚀快速入门, 📑学习教程, 📦软件硬件配套说明, 📌FAQ, 📝相关信息, 说明

</details>

### matrix-common

Common utilities for Synapse, Sydent and Sygnal

`pip install matrix-common` · installs (wheel) · licence: Apache Software License · rank 14005 · last release 2022-09-13 · [PyPI](https://pypi.org/project/matrix-common/)

<details><summary>README extract</summary>

Common utilities for Synapse, Sydent and Sygnal.

Example:
```python
import matrix_common
```

Sections: matrix-python-common, Usage, Releasing

</details>

### mailsuite

A Python package for retrieving, parsing, and sending emails

`pip install mailsuite` · installs (wheel) · licence: Apache-2.0 · rank 14104 · last release 2026-10-30 · [PyPI](https://pypi.org/project/mailsuite/) · [docs](https://seanthegeek.net/mailsuite/)

<details><summary>README extract</summary>

A Python package for retrieving, parsing, and sending emails.

Features:
- Simplified IMAP client (`mailsuite.imap.IMAPClient`) — usable on its own,
 and the engine behind the mailbox abstraction's IMAP backend
 - Automatic reconnection and retries after dropped connections and timeouts
 - Watch a folder for new messages ...

Example:
```python
MSGraphConnection(..., graph_url="
```

Sections: mailsuite, Features, Microsoft Graph notes, Microsoft Graph permissions

</details>

### milksnake

A python library that extends setuptools for binary extensions.

`pip install milksnake` · installs (wheel) · licence: Apache Software License · rank 14115 · last release 2023-10-12 · [PyPI](https://pypi.org/project/milksnake/)

<details><summary>README extract</summary>

Milksnake is an extension for setuptools that allows you to distribute
dynamic linked libraries in Python wheels in the most portable way imaginable.

It gives you a hook to invoke your own build process and to then take the
resulting dynamic linked library.

Features:
There are already other projects that make Python and native libraries play
along but this one is different. Unlike other projects that build Python
extension modules the goal of this project is to build regular native libraries
that are then loaded ...

Example:
```python
from setuptools import setup

def build_native(spec):
    # build an example rust library
    build = spec.add_external_build(
        cmd=['cargo', 'build', '--release'],
        path='./rust'
    )

    spec.add_cffi_module(
...

</details>

### metaflow-stubs

Metaflow Stubs: Stubs for the metaflow package

`pip install metaflow-stubs` · installs (wheel) · licence: Apache Software License · rank 14158 · last release 2026-11-06 · [PyPI](https://pypi.org/project/metaflow-stubs/) · [docs](https://docs.metaflow.org) · [source](https://github.com/Netflix/metaflow)

<details><summary>README extract</summary>

This package contains stub files for `metaflow` and thus offers type hints for various editors (such as `VSCode`) and language servers (such as `Pylance`).

</details>

### mailer

A module to send email simply in Python

`pip install mailer` · installs from source (sdist only) · licence: MIT License · rank 14179 · last release 2015-04-22 · [PyPI](https://pypi.org/project/mailer/)

<details><summary>README extract</summary>

Here are some of the features:

* Single class to send plain text, HTML email, and attachments
* Auto detects attachment types
* Support for internationalized headers

Changes in version 0.3

The API for Mailer.To is changed. Use a string to specify a single recipient,
and an iterable to specify more than one.

Changes in version 0.4 ...

</details>

### mknotebooks

Plugin for mkdocs to generate markdown documents from jupyter notebooks.

`pip install mknotebooks` · installs (wheel) · licence: MIT License · rank 14200 · last release 2023-08-07 · [PyPI](https://pypi.org/project/mknotebooks/)

<details><summary>README extract</summary>

mknotebooks is a plugin for MkDocs enabling you to include Jupyter notebooks directly in your project documentation.

Sections: mknotebooks, Usage, Options, Styling, Syntax highlighting, Binder, Examples, Inspecting generated markdown

</details>

### meteomatics

Meteomatics API connector

`pip install meteomatics` · installs (wheel) · licence: MIT License · rank 14226 · last release 2026-04-29 · [PyPI](https://pypi.org/project/meteomatics/)

<details><summary>README extract</summary>

Meteomatics provides a REST-style API to retrieve historic, current, and forecast data globally. This includes model data and observational data in time series and areal formats. Areal formats are also offered through a WMS/WFS-compatible interface. Geographic and time series data can be combined in certain file formats, such as NetCDF. ...

</details>

### mup

Maximal Update Parametrization

`pip install mup` · installs from source (sdist only) · licence: MIT License · rank 14268 · last release 2022-03-08 · [PyPI](https://pypi.org/project/mup/)

<details><summary>README extract</summary>

In *Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer*, we show that hyperparameters become stable across neural network sizes when we parametrize the model in maximal update parametrization (μP). ...

Example:
```python
from mup import MuReadout, make_base_shapes, set_base_shapes, MuSGD, MuAdam

class MyModel(nn.Module):
    def init(self, width, ...):
        ...
        ### In model definition, replace output layer with MuReadout
        # readout = nn.Linear(width, d_out)
        readout = MuReadout(width, d_out)
...
```

...

</details>

### mattersim

MatterSim: A Deep Learning Atomistic Model Across Elements, Temperatures and Pressures.

`pip install mattersim` · installs from source (sdist only) · licence: MIT License · rank 14379 · last release 2026-05-28 · [PyPI](https://pypi.org/project/mattersim/)

<details><summary>README extract</summary>

MatterSim is a deep learning atomistic model across elements, temperatures and pressures.

This README provides a quick start guide. For more comprehensive information, please refer to the MatterSim documentation.

Example:
```python
import torch
from loguru import logger
from ase.build import bulk
from ase.units import GPa
from mattersim.forcefield import MatterSimCalculator

device = "cuda" if torch.cuda.is_available() else "cpu"
logger.info(f"Running MatterSim on {device}")

si = bulk("Si", "diamond", a=5.43)
si.calc = MatterSimCalculator(device=device)
...
```

Sections: Documentation, Prerequisite, Pre-trained Models, Usage, A minimal test, Finetune, A minimal finetune example, Reference, Limitations, Trademarks, Responsible AI Transparency Documentation

</details>

### meshtastic

Python API & client shell for talking to Meshtastic devices

`pip install meshtastic` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 14389 · last release 2026-07-17 · [PyPI](https://pypi.org/project/meshtastic/)

_README extract left out: share-alike licence._

### mollie-api-py

Python Client SDK Generated by Speakeasy.

`pip install mollie-api-py` · installs (wheel) · licence: not stated · rank 14408 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mollie-api-py/) · [source](https://github.com/mollie/mollie-api-py.git)

<details><summary>README extract</summary>

> Mollie is transitioning to new, automatically generated SDKs.
> As a part of this transition, new features will be developed exclusively for the new Python SDK. We encourage you to migrate to this version by 23 October 2026, after which the legacy SDK will enter maintenance mode and receive no further updates. ...

Features:
* list - List capabilities

Example:
```python
# !/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
# "mollie-api-py",
# ]
# ///

from mollie import ClientSDK

sdk = ClientSDK(
  # SDK arguments
)

# Rest of script here...
```

...

</details>

### monday

A Python client library for Monday.com

`pip install monday` · installs (wheel) · licence: BSD · rank 14457 · last release 2026-05-01 · [PyPI](https://pypi.org/project/monday/)

<details><summary>README extract</summary>

A monday.com Python Client Library

For an overview of the Monday API, click here.

- Python >= 3.11
- urllib3 >= 2.6.0

Example:
```python
from monday import MondayClient

monday = MondayClient('your token')

monday.items.create_item(board_id='12345678', group_id='today', item_name='Do a thing')
```

Sections: monday, Requirements, Getting started, Additional Resources and Code Samples

</details>

### miceforest

Multiple Imputation by Chained Equations with LightGBM

`pip install miceforest` · installs (wheel) · licence: MIT · rank 14489 · last release 2025-10-27 · [PyPI](https://pypi.org/project/miceforest/)

<details><summary>README extract</summary>

Fast, memory efficient Multiple Imputation by Chained Equations (MICE)
with lightgbm. The R version of this package may be found
here.

`miceforest` was designed to be:

 - Fast
 - Uses lightgbm as a backend
 - Has efficient mean matching solutions. ...

Example:
```python
import miceforest as mf
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

# Load data and introduce missing values
iris = pd.concat(load_iris(as_frame=True,return_X_y=True),axis=1)
iris.rename({"target": "species"}, inplace=True, axis=1)
iris['species'] = iris['species'].astype('category')
...
```

...

</details>

### matrx-seo

Provider-neutral SEO collection contracts and canonical persistence.

`pip install matrx-seo` · installs (wheel) · licence: not stated · rank 14557 · last release 2026-10-30 · [PyPI](https://pypi.org/project/matrx-seo/)

<details><summary>README extract</summary>

Provider-neutral SEO provider clients, collection contracts, normalization, replay
fixtures, and live `seo.*` persistence for Matrx. The standalone FastAPI
service exposes collection, cache, operation-catalog, and exact request/response evidence
routes over the same package code used by aidream. See
`matrx_seo/FEATURE.md` for the current contract.

</details>

### myskoda

Library for interaction with the MySkoda APIs.

`pip install myskoda` · installs (wheel) · licence: not stated · rank 14571 · last release 2026-10-09 · [PyPI](https://pypi.org/project/myskoda/)

<details><summary>README extract</summary>

MySkoda is an async Python library to interact with the Skoda API.

This library will stop working in October 2026.

Škoda has released a new and official public API. A new Python client library for this API is expected to be release soon as well. ...

Example:
```python
import asyncio
from aiohttp import ClientSession
from myskoda import MySkoda

USERNAME = "my.user@domain.com"
PASSWORD = "my_password"

async def main():
    async with ClientSession() as session:
        myskoda = MySkoda(session)
        await myskoda.connect(USERNAME, PASSWORD)
        for vin in await myskoda.list_vehicle_vins():
...
```

Sections: MySkoda, warning: END OF LIFE ANNOUNCEMENT :warning, Get In Touch, Quick Start, Basic example, Documentation, As Library, As CLI, Disclaimer

</details>

### medspacy

Library for clinical NLP with spaCy.

`pip install medspacy` · installs from source (sdist only) · licence: MIT License · rank 14649 · last release 2024-11-21 · [PyPI](https://pypi.org/project/medspacy/) · [source](https://github.com/medspacy/medspacy)

<details><summary>README extract</summary>

Library for clinical NLP with spaCy.

MedSpaCy is currently in beta.

Features:
MedSpaCy is a library of tools for performing clinical NLP and text processing tasks with the popular spaCy
framework. The `medspacy` package brings together a number of other packages, each of which implements specific
functionality for common ...

Example:
```python
import medspacy
from medspacy.ner import TargetRule
from medspacy.visualization import visualize_ent

# Load medspacy model
nlp = medspacy.load()
print(nlp.pipe_names)

text = """
Past Medical History:
1. Atrial fibrillation
2. Type II Diabetes Mellitus

Assessment and Plan:
...
```

Sections: medspacy, Overview, Usage, Requirements, Basic Usage, Citing medspaCy, Made with medSpaCy

</details>

### mani-skill

ManiSkill3: A Unified Benchmark for Generalizable Manipulation Skills

`pip install mani-skill` · installs (wheel) · licence: not stated · rank 14729 · last release 2026-04-21 · [PyPI](https://pypi.org/project/mani-skill/)

<details><summary>README extract</summary>

Sample of environments/robots rendered with ray-tracing. Scene datasets sourced from AI2THOR and ReplicaCAD

ManiSkill is an open-source framework for robot simulation and training powered by SAPIEN, with a strong focus on manipulation skills. Among its features include:
- GPU parallelized visual data collection system. ...

Sections: ManiSkill 3, Getting Started

</details>

### marin-rigging

(no summary)

`pip install marin-rigging` · does not install on CPython 3.14 · licence: not stated · rank 14735 · last release 2026-11-07 · [PyPI](https://pypi.org/project/marin-rigging/)

### matrx-files

All things files: cloud storage, media management, conversion, PDF, sharing — the platform's independent file service.

`pip install matrx-files` · installs (wheel) · licence: MIT License · rank 14752 · last release 2026-10-30 · [PyPI](https://pypi.org/project/matrx-files/) · [source](https://github.com/AI-Matrix-Engine/aidream-current)

<details><summary>README extract</summary>

All things files: cloud storage, media management, conversion, PDF, sharing — the platform's independent file service.

Contract: INDEPENDENCE.md.

Cross-repo system-of-record: `/Users/armanisadeghi/code/common-docs/systems/files/file-service/STATE.md`
— read it before touching this feature in ANY repo. ...

</details>

### moonraker-api

Async websocket API client for Moonraker

`pip install moonraker-api` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 14780 · last release 2026-06-10 · [PyPI](https://pypi.org/project/moonraker-api/)

_README extract left out: share-alike licence._

### markupever

The fast, most optimal, and correct HTML & XML parsing library.

`pip install markupever` · installs (wheel) · licence: MIT License · rank 14789 · last release 2026-11-05 · [PyPI](https://pypi.org/project/markupever/)

<details><summary>README extract</summary>

_MarkupEver is a modern, fast (high-performance), XML & HTML languages parsing library written in Rust._

KEY FEATURES:

- 🚀 Fast: Very high performance and fast (thanks to html5ever and selectors).
- 🔥 Easy: Designed to be easy to use and learn. Completion everywhere.
- ✨ Low-Memory: Written in Rust. Uses low memory. ...

Example:
```python
import markupever

dom = markupever.parse_file("file.html", "html")
# Or parse a HTML content directly:
# dom = markupever.parse("... content ...", "html")

for element in dom.select("div.section > p:child-nth(1)"):
    print(element.text())
```

Sections: Example, Parse, Create DOM

</details>

### mozjpeg-lossless-optimization

Optimize JPEGs losslessly using MozJPEG

`pip install mozjpeg-lossless-optimization` · installs (wheel) · licence: BSD-3-Clause · rank 14821 · last release 2025-10-30 · [PyPI](https://pypi.org/project/mozjpeg-lossless-optimization/) · [docs](https://github.com/wanadev/mozjpeg-lossless-optimization#usage) · [source](https://github.com/wanadev/mozjpeg-lossless-optimization)

<details><summary>README extract</summary>

This library optimizes JPEGs losslessly using MozJPEG.

To reduce the file sizes,

* the Huffman table of the JPEGs is optimized,
* the baseline JPEGs are converted to progressive JPEGs,
* and any metadata and ICC profiles are removed. ...

Example:
```python
import mozjpeg_lossless_optimization

with open("./image.jpg", "rb") as input_jpeg_file:
    input_jpeg_bytes = input_jpeg_file.read()

output_jpeg_bytes = mozjpeg_lossless_optimization.optimize(input_jpeg_bytes)

with open("./out.jpg", "wb") as output_jpeg_file:
    output_jpeg_file.write(output_jpeg_bytes)
```

Sections: MozJPEG Lossless Optimization, Usage, From PyPI, From Sources, Hacking

</details>

### molmospaces-resources

Resource manager for MolmoSpaces

`pip install molmospaces-resources` · installs (wheel) · licence: Apache-2.0 · rank 14864 · last release 2026-08-12 · [PyPI](https://pypi.org/project/molmospaces-resources/) · [source](https://github.com/allenai/molmospaces-resources)

<details><summary>README extract</summary>

Resource manager for MolmoSpaces. Downloads, caches, and symlinks versioned data archives from remote buckets.

- Versioned, read-only download cache with symlink-based install directories
- Eager or on-demand archive extraction with parallel downloads
- Pluggable archive indexing for fast asset lookup ...

Example:
```python
import os
from molmospaces_resources import HFRemoteStorage, setup_resource_manager

source = HFRemoteStorage("allenai/molmospaces", repo_prefix="mujoco", token=os.environ["HF_TOKEN"])
mgr = setup_resource_manager(
  source,
  symlink_dir=SYMLINK_DIR,
  versions=ASSETS_VERSIONS,
  cache_dir=CACHE_DIR,
)
```

Sections: MolmoSpaces-resources, Setup example, Logging, FAQ

</details>

### monday-api-python-sdk

A Python SDK for interacting with Monday's GraphQL API.

`pip install monday-api-python-sdk` · installs (wheel) · licence: not stated · rank 14921 · last release 2026-08-03 · [PyPI](https://pypi.org/project/monday-api-python-sdk/)

<details><summary>README extract</summary>

A Python SDK for interacting with Monday"s GraphQL API.

Example:
```python
from monday_sdk import MondayClient

client = MondayClient(token="your_token")

column_values = {
    "status_column_id": "In Progress",  # Replace with your actual status column ID and value
    "date_column_id": "2025-01-06",    # Replace with your actual date column ID and date (YYYY-MM-DD format)
...
```

Sections: monday-api-python-sdk, Authentication, Examples, Example 1: Create a new item, Example 2: Create an Update and Update Column Values, Response Types, Available Types, Example Usage

</details>

### mypy-boto3-agent-registry-control

Type annotations for boto3 AgentRegistryControl 1.43.125 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-agent-registry-control` · installs (wheel) · licence: MIT · rank 14930 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mypy-boto3-agent-registry-control/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_agent_registry_control/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 AgentRegistryControl 1.43.125
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-agent-registry-control docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### meilisearch-mcp

MCP server for Meilisearch

`pip install meilisearch-mcp` · installs (wheel) · licence: not stated · rank 14934 · last release 2026-08-24 · [PyPI](https://pypi.org/project/meilisearch-mcp/)

### mypy-boto3-agent-registry

Type annotations for boto3 AgentRegistry 1.43.106 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-agent-registry` · installs (wheel) · licence: MIT · rank 14966 · last release 2026-09-30 · [PyPI](https://pypi.org/project/mypy-boto3-agent-registry/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_agent_registry/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 AgentRegistry 1.43.106 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-agent-registry docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### meshagent-api

Python Server API for Meshagent

`pip install meshagent-api` · installs (wheel) · licence: Apache-2.0 · rank 14988 · last release 2026-10-31 · [PyPI](https://pypi.org/project/meshagent-api/) · [docs](https://docs.meshagent.com) · [source](https://www.meshagent.com)

<details><summary>README extract</summary>

The ``meshagent.api`` is the foundation that all other packages build on. It includes foundational protocols, JWT authentication, room management, document sync, and more.

 MeshAgent uses JSON Web Tokens (JWTs) to authenticate participants. ...

Sections: Meshagent, MeshAgent API, JWT Authentication, RoomClient, Document Runtime and Schemas, WebhookServer, ServiceHost

</details>

