# Unclassified / P (part 3 of 3)

[Index](README.md) · 979 packages in this topic, by downloads.

[part 1](unclassified-p.md) · [part 2](unclassified-p-2.md) · part 3

### py-topping

simplify functions from other libraries functions in 1-2 lines

`pip install py-topping` · installs from source (sdist only) · licence: MIT License · rank 14603 · last release 2026-02-09 · [PyPI](https://pypi.org/project/py-topping/)

<details><summary>README extract</summary>

PyPi Project Page :

To Install the Stable Version

To Install the Newest Version

This library will *NOT auto install dependencies for you but you could see the list of dependencies in sample links

You could see samples of how to use this library inside the samples folder in github


Sections: py_topping, a topping on great libraries, This library focus on "simplify" (& laziness :P), database, sharepoint, gcp, socket, data_preparation, general_use, opc, run_pipeline

</details>

### pygridsynth

Python version gridsynth program computes approximations of Z-rotations over the Clifford+T gate set

`pip install pygridsynth` · installs (wheel) · licence: MIT License · rank 14617 · last release 2026-01-09 · [PyPI](https://pypi.org/project/pygridsynth/)

<details><summary>README extract</summary>

`pygridsynth` is a Python library for approximating arbitrary Z-rotations using the Clifford+T gate set, based on a given angle `θ` and tolerance `ε`. It is particularly useful for addressing approximate gate synthesis problems in quantum computing and algorithm research.

Features:
- Inspired by Established Work: This library is based on P. Selinger's gridsynth program (newsynth), adapted for Python with additional functionality.
- High Precision: Utilizes the `mpmath` library to support high-precision calculations. ...

Example:
```python
import mpmath

from pygridsynth.gridsynth import gridsynth_gates

mpmath.mp.dps = 128
theta = mpmath.mpf("0.5")
epsilon = mpmath.mpf("1e-10")
gates = gridsynth_gates(theta=theta, epsilon=epsilon)
print(gates)

mpmath.mp.dps = 128
...

</details>

### pyctcdecode

CTC beam search decoder for speech recognition.

`pip install pyctcdecode` · installs (wheel) · licence: not stated · rank 14623 · last release 2023-01-20 · [PyPI](https://pypi.org/project/pyctcdecode/) · [source](https://github.com/kensho-technologies/pyctcdecode)

<details><summary>README extract</summary>

A fast and feature-rich CTC beam search decoder for speech recognition written in Python, providing n-gram (kenlm) language model support similar to PaddlePaddle's decoder, but incorporating many new features such as byte pair encoding and real-time decoding to support models like Nvidia's Conformer-CTC or Facebook's Wav2Vec2.

Features:
In scientific computing, there’s often a tension between a language’s performance and its ease of use for prototyping and experimentation. Although C++ is the conventional choice for CTC decoders, we decided to try building one in Python. ...

Example:
```python
from pyctcdecode import build_ctcdecoder

# specify alphabet labels as they appear in logits
labels = [
    " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
...

</details>

### pygohcl

Python bindings for Hashicorp HCL2 Go library

`pip install pygohcl` · installs (wheel) · licence: MIT License · rank 14629 · last release 2026-09-17 · [PyPI](https://pypi.org/project/pygohcl/)

<details><summary>README extract</summary>

Python wrapper for hashicorp/hcl (v2).

The following versions are supported - 3.10, 3.11, 3.12, 3.13, 3.14, 3.15.

Example:
```python
>>> import pygohcl
>>> pygohcl.loads("""variable "docker_ports" {
...   type = list(object({
...     internal = number
...     external = number
...     protocol = string
...   }))
...   default = [
...     {
...       internal = 8300
...       external = 8300
...       protocol = "tcp"
...     }
...   ]
... }""")
...
```

Sections: pygohcl, Requirements, Setup, Usage, Building locally

</details>

### python-amazon-ad-api

Python wrapper for the Amazon Advertising API

`pip install python-amazon-ad-api` · installs (wheel) · licence: MIT License · rank 14653 · last release 2026-11-05 · [PyPI](https://pypi.org/project/python-amazon-ad-api/)

<details><summary>README extract</summary>

A python 3 wrapper to access Amazon's Advertising API with an easy-to-use interface.

Features:
You need obtain your own credentials with Amazon that may include an amazon developer account and access as seller or vendor. Please view the checklist of Amazon Ads API onboarding overview

Example:
```python
from ad_api.api import v1

result = v1.Campaigns(credentials=credentials, debug=True).query_campaigns(
    body={
        "adProductFilter": {"include": ["SPONSORED_PRODUCTS"]},
        "stateFilter": {"include": ["ENABLED"]},
        "maxResults": 100,
    }
)

campaigns = result.payload.get("campaigns")
...
```

...

</details>

### pyspark-extension

A library that provides useful extensions to Apache Spark.

`pip install pyspark-extension` · installs (wheel) · licence: Apache Software License · rank 14675 · last release 2026-09-10 · [PyPI](https://pypi.org/project/pyspark-extension/)

<details><summary>README extract</summary>

This project provides extensions to the Apache Spark project in Scala and Python:

Diff: A `diff` transformation and application for `Dataset`s that computes the differences between
two datasets, i.e. which rows to _add_, _delete_ or _change_ to get from one dataset to the other. ...

Example:
```python
# noinspection PyUnresolvedReferences
from gresearch.spark import *

# using PIP
spark.install_pip_package("pandas==1.4.3", "pyarrow")
spark.install_pip_package("-r", "requirements.txt")

# using Poetry
spark.install_poetry_project("../my-poetry-project/", poetry_python="../venv-poetry/bin/python")
```

Sections: Spark Extension, Using Spark Extension, PyPi package (local Spark cluster only), PySpark API, PySpark REPL, PySpark `spark-submit`, Your favorite Data Science notebook

</details>

### pygrabber

Module for grabbing live video images using DirectShow

`pip install pygrabber` · installs (wheel) · licence: MIT · rank 14701 · last release 2023-10-20 · [PyPI](https://pypi.org/project/pygrabber/)

<details><summary>README extract</summary>

This is a Python library that enables you to use video cameras from Python on Windows. It is based on DirectShow.
In particular, it allows to:
 * Capture photos from a video camera
 * View installed cameras on a system
 * Set the camera options
 * Save a vide captured from a camera

The library is available on PyPI:

Example:
```python
# This code lists the cameras connected to your PC:

from pygrabber.dshow_graph import FilterGraph

graph = FilterGraph()
print(graph.get_input_devices())
```

Sections: python_grabber, Basic example, Save images example, View live video example, Sample GUI application

</details>

### python-zaqarclient

Client Library for OpenStack Zaqar Messaging API

`pip install python-zaqarclient` · installs (wheel) · licence: Apache Software License · rank 14726 · last release 2026-08-27 · [PyPI](https://pypi.org/project/python-zaqarclient/)

<details><summary>README extract</summary>

:Wiki: Zaqar Wiki
:Launchpad: Zaqar Launchpad
:Review: Code Review
:Design: Client Wiki
:IRC: #openstack-zaqar @ OFTC

Welcome to the Zaqar Python Client project!

Sections: Python Zaqar Client, What's in the box, How to use, Python client, Command line interface

</details>

### pydantic-scim

Pydantic types for SCIM

`pip install pydantic-scim` · installs (wheel) · licence: not stated · rank 14798 · last release 2023-10-26 · [PyPI](https://pypi.org/project/pydantic-scim/)

<details><summary>README extract</summary>

Largely generated by running `datamodel-codegen` on the files in schema/,
and then cleaned up by hand.

</details>

### pymochow

Python SDK for mochow

`pip install pymochow` · installs (wheel) · licence: Apache License 2.0 · rank 14833 · last release 2026-05-09 · [PyPI](https://pypi.org/project/pymochow/)

### python-magic-bin

File type identification using libmagic binary package

`pip install python-magic-bin` · does not install on CPython 3.14 · licence: MIT License · rank 14854 · last release 2017-10-02 · [PyPI](https://pypi.org/project/python-magic-bin/)

<details><summary>README extract</summary>

This module uses ctypes to access the libmagic file type
identification library. It makes use of the local magic database and
supports both textual and MIME-type output.

</details>

### proxycurl-py

(no summary)

`pip install proxycurl-py` · installs (wheel) · licence: not stated · rank 14898 · last release 2024-09-27 · [PyPI](https://pypi.org/project/proxycurl-py/)

<details><summary>README extract</summary>

* What is Proxycurl?
* Before you install
* Installation and supported Python versions
* Initializing `proxycurl-py` with an API Key
* Usage with examples
 + Enrich a Person Profile
 + Enrich a Company Profile
 + Lookup a person
 + Lookup a company
 + Lookup a LinkedIn Profile URL from a work email address
 + Enrich LinkedIn member profiles in ...

Example:
```python
from proxycurl.asyncio import Proxycurl, do_bulk
import asyncio
import csv

proxycurl = Proxycurl()
person = asyncio.run(proxycurl.linkedin.person.get(
    url='
))
print('Person Result:', person)
```

...

</details>

### pcmflux

A performant audio capture pipeline that encodes raw PCM to Opus, skipping silence.

`pip install pcmflux` · installs (wheel) · licence: MPL-2.0 · rank 14910 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pcmflux/)

<details><summary>README extract</summary>

Part of

pcmflux is a high-performance audio capture and encoding module for Python.

It is designed to capture system audio using PulseAudio, encode it into the Opus format, and stream it with low latency. ...

Example:
```python
from pcmflux import AudioCapture, AudioCaptureSettings

def on_chunk(frame):
    # Silence-gated chunks are never delivered (the callback is skipped for
    # them), so there's no empty/"silence" frame to filter out here.
    data = bytes(frame)          # copy out (header+Opus, or raw Opus per settings)
...
```

Sections: pcmflux, Building from source, Core Features, Usage, API notes, Example Usage, Ogg Opus Output Socket

</details>

### pypistats

Python interface to PyPI Stats API https://pypistats.org/api

`pip install pypistats` · installs (wheel) · licence: MIT · rank 14922 · last release 2026-06-30 · [PyPI](https://pypi.org/project/pypistats/) · [source](https://github.com/hugovk/pypistats)

<details><summary>README extract</summary>

Python interface to PyPI Stats API to get aggregate
download statistics on Python packages on the Python Package Index without having to
execute queries directly against Google BigQuery.

Data is available for the last 180 days. (For longer
time periods, pypinfo can help, you'll need an API
key and get free quota.)

Example:
```python
import pypistats
from pprint import pprint

# Call the API
print(pypistats.recent("pillow"))
print(pypistats.recent("pillow", "day", format="markdown"))
print(pypistats.recent("pillow", "week", format="rst"))
print(pypistats.recent("pillow", "month", format="html"))
pprint(pypistats.recent("pillow", "week", format="json"))
...
```

Sections: pypistats, From PyPI, From source, Example command-line use, Example programmatic use, NumPy and pandas, See also

</details>

### python-zunclient

Client Library for Zun

`pip install python-zunclient` · installs (wheel) · licence: Apache Software License · rank 14960 · last release 2026-08-28 · [PyPI](https://pypi.org/project/python-zunclient/)

<details><summary>README extract</summary>

This is a client library for Zun built on the Zun API.
It provides a Python API (the zunclient module)
and a command-line tool (zun).

* License: Apache License, Version 2.0
* PyPi - package installation
* Online Documentation
* Launchpad project - release management
* Blueprints - feature specifications
* Bugs - issue tracking
* Source
* How to ...

Sections: Team and repository tags, Python bindings to the OpenStack Container API

</details>

### pycardano

A Cardano library in Python

`pip install pycardano` · installs (wheel) · licence: MIT License · rank 14987 · last release 2026-03-01 · [PyPI](https://pypi.org/project/pycardano/) · [docs](https://pycardano.readthedocs.io/en/latest/) · [source](https://github.com/Python-Cardano/pycardano)

<details><summary>README extract</summary>

PyCardano is a Cardano library written in Python. It allows users to create and sign transactions without
depending on third-party Cardano serialization tools, such as
cardano-cli and
cardano-serialization-lib, making it a lightweight library, which
is simple and fast to set up in all types of environments. ...

Features:
- [x] Shelly address
- [x] Transaction builder
- [x] Transaction signing
- [x] Multi-asset
- [X] Chain backend integration
- [X] Fee calculation
- [X] UTxO selection
- [X] Native script
- [X] Native token
- [X] Metadata
- [X] Plutus script ...

Example:
```python
"""Build a transaction using transaction builder"""

from blockfrost import ApiUrls
from pycardano import *

# Use testnet
network = Network.TESTNET

# Read keys to memory
...

</details>

### plone.app.layout

Layout mechanisms for Plone

`pip install plone.app.layout` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 14998 · last release 2026-06-23 · [PyPI](https://pypi.org/project/plone.app.layout/)

_README extract left out: share-alike licence._

