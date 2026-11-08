# Scientific/Engineering (part 2 of 2)

[Index](README.md) · 726 packages in this topic, 124 more listed under another topic, by downloads.

[part 1](scientific-engineering.md) · part 2

### pynrrd

Pure python module for reading and writing NRRD files.

`pip install pynrrd` · installs (wheel) · licence: MIT License · rank 10828 · last release 2025-01-23 · [PyPI](https://pypi.org/project/pynrrd/) · [docs](https://pynrrd.readthedocs.io/en/stable)

<details><summary>README extract</summary>

pynrrd is a pure-Python module for reading and writing NRRD files into and
from numpy arrays.

* numpy
* typing_extensions

v1.0+ requires Python 3.7 or above. If you have an older Python version, please install a v0.x release instead.

Example:
```python
import numpy as np
import nrrd

# Some sample numpy data
data = np.zeros((5,4,3,2))
filename = 'testdata.nrrd'

# Write to a NRRD file
nrrd.write(filename, data)

# Read the data back from file
readdata, header = nrrd.read(filename)
print(readdata.shape)
print(header)
```

Sections: pynrrd, Requirements, Example usage, Next Steps

</details>

### alchemlyb

the simple alchemistry library

`pip install alchemlyb` · installs (wheel) · licence: BSD-3-Clause · rank 10840 · last release 2025-10-22 · [PyPI](https://pypi.org/project/alchemlyb/) · [docs](https://alchemlyb.readthedocs.io/) · [source](https://github.com/alchemistry/alchemlyb)

<details><summary>README extract</summary>

alchemlyb makes alchemical free energy calculations easier to do by leveraging the full power and flexibility of the PyData stack Wu2024. It includes:

1. Parsers for extracting raw data from output files of common molecular dynamics engines such as GROMACS, AMBER, NAMD and other simulation codes.

2. ...

Sections: alchemlyb: the simple alchemistry library, Documentation, Getting involved, References

</details>

### p4p

Python interface to PVAccess protocol client

`pip install p4p` · installs (wheel) · licence: BSD · rank 10870 · last release 2026-09-29 · [PyPI](https://pypi.org/project/p4p/)

<details><summary>README extract</summary>

Python bindings for the PVAccess network client and server.

 python -m virtualenv p4ptest
 . p4ptest/bin/activate
 python -m pip install -U pip
 python -m pip install p4p
 python -m nose2 p4p

See documentation

Source

CI results

</details>

### tippecanoe

Builds vector tilesets from large (or small) collections of GeoJSON, FlatGeobuf, or CSV features

`pip install tippecanoe` · installs (wheel) · licence: BSD License · rank 10879 · last release 2024-12-10 · [PyPI](https://pypi.org/project/tippecanoe/) · [source](https://github.com/felt/tippecanoe)

<details><summary>README extract</summary>

A project that packages tippecanoe as a Python package, enabling `tippecanoe` to be installed from PyPI:

or used as part of `build-system.requires` in a pyproject.toml file:

After installation, the Python bin directory for console scripts may need to be added to your path (or if installing in a venv, activate the venv). ...

Sections: tippecanoe Python Distributions, Using with pipx, Using with pyproject.toml

</details>

### genai-perf

GenAI Perf Analyzer CLI - CLI tool to simplify profiling LLMs and Generative AI models with Perf Analyzer

`pip install genai-perf` · installs (wheel) · licence: BSD · rank 10881 · last release 2025-08-26 · [PyPI](https://pypi.org/project/genai-perf/)

<details><summary>README extract</summary>

<!--
Copyright (c) 2024-2025, NVIDIA CORPORATION & AFFILIATES. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
 * Redistributions of source code must retain the above copyright
 notice, this list of conditions and the following ...

Example:
```python
# Hypothetical integration with the inference engine
import InferenceEngine  # Assume this exists

engine = InferenceEngine()
logger = Logger("mooncake_traffic.jsonl")

def process_request(prompt: str):
    result = engine.infer(prompt)
    logger.log_request({
        "input_length": len(engine.tokenize(prompt)),
...
```

...

</details>

### tmtools

Python bindings around the TM-align code for structural alignment of proteins

`pip install tmtools` · installs from source (sdist only) · licence: GNU General Public License v3 (GPLv3) · rank 10890 · last release 2025-11-09 · [PyPI](https://pypi.org/project/tmtools/)

_README extract left out: share-alike licence._

### scikit-learn-extra

A set of tools for scikit-learn.

`pip install scikit-learn-extra` · installs from source (sdist only) · licence: OSI Approved · rank 10895 · last release 2023-03-27 · [PyPI](https://pypi.org/project/scikit-learn-extra/)

<details><summary>README extract</summary>

scikit-learn-extra is a Python module for machine learning that extends scikit-learn. It includes algorithms that are useful but do not satisfy the scikit-learn inclusion criteria, for instance due to their novelty or lower citation number.

</details>

### igwn-segments

Representations of semi-open intervals

`pip install igwn-segments` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 10925 · last release 2026-01-19 · [PyPI](https://pypi.org/project/igwn-segments/)

_README extract left out: share-alike licence._

### spark-sklearn

Integration tools for running scikit-learn on Spark

`pip install spark-sklearn` · installs from source (sdist only) · licence: Apache Software License · rank 10932 · last release 2019-01-30 · [PyPI](https://pypi.org/project/spark-sklearn/)

<details><summary>README extract</summary>

This package contains some tools to integrate the Spark computing framework
with the popular scikit-learn machine library. Among other things, it can:

- train and evaluate multiple scikit-learn models in parallel. It is a distributed analog to the
 multicore implementation included by default in `scikit-learn` ...

Example:
```python
from sklearn import svm, datasets
from spark_sklearn import GridSearchCV
iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svr = svm.SVC(gamma='auto')
clf = GridSearchCV(sc, svr, parameters)
clf.fit(iris.data, iris.target)
```

Sections: Scikit-learn integration package for Apache Spark, Example, Documentation

</details>

### suffix-trees

Suffix trees, generalized suffix trees and string processing methods

`pip install suffix-trees` · installs (wheel) · licence: MIT · rank 10958 · last release 2026-08-31 · [PyPI](https://pypi.org/project/suffix-trees/)

<details><summary>README extract</summary>

Python implementation of Suffix Trees and Generalized Suffix Trees. Also provided methods with typical applications of STrees and GSTrees.

Example:
```python
from suffix_trees import STree

# Suffix-Tree example.
st = STree.STree("abcdefghab")
print(st.find("abc"))  # 0
print(st.find_all("ab"))  # {0, 8}

# Generalized Suffix-Tree example.
a = ["xxxabcxxx", "adsaabc", "ytysabcrew", "qqqabcqw", "aaabc"]
st = STree.STree(a)
print(st.lcs())  # "abc"

...
```

Sections: suffix_trees, Usage

</details>

### fasttext-numpy2-wheel

fasttext Python bindings

`pip install fasttext-numpy2-wheel` · installs from source (sdist only) · licence: MIT License · rank 10963 · last release 2024-11-05 · [PyPI](https://pypi.org/project/fasttext-numpy2-wheel/)

<details><summary>README extract</summary>

fastText is a library for efficient learning
of word representations and sentence classification.

In this document we present how to use fastText in python.

Example:
```python
+>>> import fasttext
+>>> help(fasttext.FastText)

Help on module fasttext.FastText in fasttext:

NAME
    fasttext.FastText

DESCRIPTION
    # Copyright (c) 2017-present, Facebook, Inc.
    # All rights reserved.
    #
    # This source code is licensed under the MIT license found in the
...
```

...

</details>

### rainflow

Implementation of ASTM E1049-85 rainflow cycle counting algorithm

`pip install rainflow` · installs (wheel) · licence: MIT License · rank 10988 · last release 2023-04-17 · [PyPI](https://pypi.org/project/rainflow/) · [source](https://github.com/iamlikeme/rainflow)

<details><summary>README extract</summary>

`rainflow` is a Python implementation of the ASTM E1049-85 rainflow cycle counting
algorythm for fatigue analysis.

Installation

`rainflow` is available on PyPI:

and on conda-forge:

Usage

See release notes in `CHANGELOG.md`.

Let's generate a sample time series. ...

Example:
```python
from math import sin, cos

time = [4.0 * i / 200 for i in range(200 + 1)]
signal = [0.2 + 0.5 * sin(t) + 0.2 * cos(10*t) + 0.2 * sin(4*t) for t in time]
```

</details>

### pycuda

Python wrapper for Nvidia CUDA

`pip install pycuda` · installs from source (sdist only) · licence: MIT License · rank 10993 · last release 2026-01-15 · [PyPI](https://pypi.org/project/pycuda/) · [source](https://github.com/inducer/pycuda)

<details><summary>README extract</summary>

PyCUDA lets you access Nvidia's CUDA parallel computation API from Python.
Several wrappers of the CUDA API already exist-so what's so special
about PyCUDA?

* Object cleanup tied to lifetime of objects. This idiom, often
 called
 RAII
 in C++, makes it much easier to write correct, leak- and
 crash-free code. ...

</details>

### fxpmath

A python library for fractional fixed-point (base 2) arithmetic and binary manipulation with Numpy compatibility.

`pip install fxpmath` · installs (wheel) · licence: MIT · rank 11021 · last release 2026-03-24 · [PyPI](https://pypi.org/project/fxpmath/) · [source](https://github.com/francof2a/fxpmath)

<details><summary>README extract</summary>

A python library for fractional fixed-point (base 2) arithmetic and binary manipulation with Numpy compatibility.

Some key features:

* Fixed-point signed and unsigned numbers representation.
* Arbitrary word and fractional sizes. Auto sizing capability. Extended precision capability.
* Arithmetic and logical (bitwise) operations supported. ...

Example:
```python
from fxpmath import Fxp

x = Fxp(-7.25)      # create fxp variable with value 7.25
x.info()
```

Sections: Table of content, quick start, creation, Representations, changing values, changing size, indexing, arithmetic, logical (bitwise) operators, Comparisons, behaviors, overflow / underflow, rounding, inaccuracy

</details>

### litert-converter

LiteRT is for mobile and embedded devices.

`pip install litert-converter` · installs (wheel) · licence: Apache Software License · rank 11041 · last release 2026-10-12 · [PyPI](https://pypi.org/project/litert-converter/)

<details><summary>README extract</summary>

LiteRT is the official solution for running machine learning models on mobile
and embedded devices. It enables on-device machine learning inference with low
latency and a small binary size on Android, iOS, and other operating systems.

</details>

### maketables

Publication-ready tables from regression results (pyfixest, statsmodels, linearmodels, lifelines, Stata, or any package via a plug-in interface), descriptive statistics, and balance tables, with output to LaTeX, Word, Typst, and HTML (via Great Tables)

`pip install maketables` · installs (wheel) · licence: MIT License · rank 11044 · last release 2026-10-19 · [PyPI](https://pypi.org/project/maketables/) · [docs](https://py-econometrics.github.io/maketables/) · [source](https://github.com/py-econometrics/maketables)

<details><summary>README extract</summary>

Docs ·
Function & API Reference ·
Report Bugs & Request Features ·
Adding Support for new Model Classes

A Python package for creating publication-ready tables from regression results
(`statsmodels`, `pyfixest`, `linearmodels`), descriptive statistics, and balance tables
with output to *LaTeX*, *Word*, *Typst* and *HTML* (HTML tables are created ...

Features:
MakeTables provides a unified interface for generating tables such as:

- Regression tables from Statsmodels,
 PyFixest,
 Linearmodels and
 Stata
- Descriptive statistics
- Balance tables

The package supports multiple output formats including: ...

Example:
```python
import pandas as pd
import maketables as mt

# Load your data (here using a sample Stata dataset with the import_dta function that also stores variable labels)
...

</details>

### fdt

Flattened Device Tree Python Module

`pip install fdt` · installs (wheel) · licence: Apache Software License · rank 11123 · last release 2022-07-08 · [PyPI](https://pypi.org/project/fdt/)

<details><summary>README extract</summary>

This python module is usable for manipulation with Device Tree Data and primary was
created for imxsb tool

> Some parts in this module have been inspired from: project.

Example:
```python
import fdt

#-----------------------------------------------
# convert *.dtb to *.dts
# ----------------------------------------------
with open("example.dtb", "rb") as f:
    dtb_data = f.read()

dt1 = fdt.parse_dtb(dtb_data)

with open("example.dts", "w") as f:
    f.write(dt1.to_dts())

#-----------------------------------------------
...
```

Sections: Flattened Device Tree Python Module, Usage, [ pydtc ] Tool, $ pydtc unpack [-h] [-s TAB_SIZE] [-o DTS_FILE] dtb_file, optional arguments, Example

</details>

### xpresslibs

FICO Xpress Optimizer libraries

`pip install xpresslibs` · installs (wheel) · licence: LicenseRef-FICO-Shrinkwrap-License · rank 11132 · last release 2026-10-29 · [PyPI](https://pypi.org/project/xpresslibs/)

<details><summary>README extract</summary>

This package provides the FICO&#174; Xpress Solver native libraries only. To develop optimization models in Python, install the `xpress` package, which depends on this package.

Licensing

The Xpress software is governed by the Xpress Shrinkwrap License Agreement. When downloading the package, you accept the license terms. ...

</details>

### itk-core

ITK is an open-source toolkit for multidimensional image analysis

`pip install itk-core` · installs (wheel) · licence: Apache Software License · rank 11143 · last release 2026-08-07 · [PyPI](https://pypi.org/project/itk-core/) · [source](https://github.com/InsightSoftwareConsortium/ITK)

<details><summary>README extract</summary>

| | C++ | Python |

| Linux | | |
| Windows | | |
| macOS | | |
| macOS (Apple Silicon)| | |
| Linux (Code coverage)| | |

Links

* Homepage
* Download
* Documentation
* Discussion
* Software Guide
* Examples
* Issue tracking
* Submit a patch ...

Sections: ITK: The Insight Toolkit, The papers, The books, Specific software version

</details>

### keras-tuner

A Hyperparameter Tuning Library for Keras

`pip install keras-tuner` · installs (wheel) · licence: Apache License 2.0 · rank 11152 · last release 2025-11-11 · [PyPI](https://pypi.org/project/keras-tuner/)

<details><summary>README extract</summary>

KerasTuner is an easy-to-use, scalable hyperparameter optimization framework
that solves the pain points of hyperparameter search. Easily configure your
search space with a define-by-run syntax, then leverage one of the available
search algorithms to find the best hyperparameter values for your models. ...

Example:
```python
import keras_tuner
from tensorflow import keras
```

Sections: KerasTuner, Quick links, Quick introduction, Citing KerasTuner

</details>

### pandas-profiling

Deprecated 'pandas-profiling' package, use 'ydata-profiling' instead

`pip install pandas-profiling` · does not install on CPython 3.14 · licence: MIT License · rank 11163 · last release 2023-01-31 · [PyPI](https://pypi.org/project/pandas-profiling/)

<details><summary>README extract</summary>

⚠️ `pandas-profiling` package naming was changed. To continue profiling data use `ydata-profiling` instead!

This repo implements the brownout strategy for deprecating the pandas-profiling package on PyPI.⚠️

> Thank you for using and following ``pandas-profiling`` developments. ...

Sections: pandas-profiling, 🎊 New year, new face, more functionalities!, How to fix the error for the main use cases, Schedule for deprecation, About pandas-profiling

</details>

### pyresample

Geospatial image resampling in Python

`pip install pyresample` · installs (wheel) · licence: LGPL-3.0-or-later · rank 11199 · last release 2025-12-02 · [PyPI](https://pypi.org/project/pyresample/)

_README extract left out: share-alike licence._

### islpy

Wrapper around isl, an integer set library

`pip install islpy` · installs (wheel) · licence: MIT · rank 11215 · last release 2026-09-10 · [PyPI](https://pypi.org/project/islpy/) · [docs](https://documen.tician.de/islpy) · [source](https://github.com/inducer/islpy)

<details><summary>README extract</summary>

islpy is a Python wrapper around Sven Verdoolaege's isl, a library for manipulating sets and
relations of integer points bounded by linear constraints.

Supported operations on sets include ...

</details>

### tensorflow-data-validation

A library for exploring and validating machine learning data.

`pip install tensorflow-data-validation` · does not install on CPython 3.14 · licence: Apache Software License · rank 11254 · last release 2026-06-11 · [PyPI](https://pypi.org/project/tensorflow-data-validation/)

<details><summary>README extract</summary>

<!-- See: www.tensorflow.org/tfx/data_validation/ -->

*TensorFlow Data Validation* (TFDV) is a library for exploring and validating
machine learning data. It is designed to be highly scalable
and to work well with TensorFlow and TensorFlow Extended (TFX).

TF Data Validation includes: ...

Sections: TensorFlow Data Validation, Nightly Packages, Build with Docker, 2. Clone the TFDV repository, 3. Build the pip package, Build from source, 1. Prerequisites, Notable Dependencies, Compatible versions, Questions, Links

</details>

### itk-filtering

ITK is an open-source toolkit for multidimensional image analysis

`pip install itk-filtering` · installs (wheel) · licence: Apache Software License · rank 11259 · last release 2026-08-07 · [PyPI](https://pypi.org/project/itk-filtering/) · [source](https://github.com/InsightSoftwareConsortium/ITK)

<details><summary>README extract</summary>

| | C++ | Python |

| Linux | | |
| Windows | | |
| macOS | | |
| macOS (Apple Silicon)| | |
| Linux (Code coverage)| | |

Links

* Homepage
* Download
* Documentation
* Discussion
* Software Guide
* Examples
* Issue tracking
* Submit a patch ...

Sections: ITK: The Insight Toolkit, The papers, The books, Specific software version

</details>

### bittensor-drand

Rust-backed Python library for generating timelock-encrypted weight commitments for Bittensor's commit-reveal mechanism using drand randomness.

`pip install bittensor-drand` · installs (wheel) · licence: MIT License · rank 11262 · last release 2026-06-18 · [PyPI](https://pypi.org/project/bittensor-drand/) · [source](https://github.com/opentensor/bittensor-drand)

<details><summary>README extract</summary>

Drand timelock encryption for Bittensor commit-reveal weights and general-purpose commitments. Rust core with Python bindings via PyO3.

- `get_encrypted_commit` is replaced by `get_encrypted_commit_v2`. The old modulo-based epoch math (`(block + netuid + 1) / (tempo + 1)`) is gone. ...

Example:
```python
from bittensor_drand import get_encrypted_commit_v2
```

Sections: bittensor-drand, What's new in 2.0, Quick start, Usage: commit-reveal weights, Using the SDK (recommended), Using `bittensor_drand` directly, General-purpose encryption, Encrypt a string for N blocks into the future, Encrypt / decrypt binary data (round-trip), Encrypt for a specific Drand round, Batch decryption with a pre-fetched signature, ML-KEM-768 encryption, API reference, Build & test

</details>

### pyopenjtalk-plus

A Python wrapper for OpenJTalk with additional improvements

`pip install pyopenjtalk-plus` · installs (wheel) · licence: MIT · rank 11266 · last release 2026-10-21 · [PyPI](https://pypi.org/project/pyopenjtalk-plus/)

<details><summary>README extract</summary>

pyopenjtalk-plus は、各フォークでの改善を一つのコードベースにまとめ、さらなる改善を加えることを目的とした、pyopenjtalk の派生ライブラリです。

- パッケージ名を `pyopenjtalk-plus` に変更
 - ライブラリ名は `pyopenjtalk` から変更されておらず、pyopenjtalk 本家同様に `import pyopenjtalk` でインポートできる
 - pyopenjtalk 本家のドロップイン代替として利用できる ...

Example:
```python
In [1]: import pyopenjtalk

In [2]: from scipy.io import wavfile

In [3]: x, sr = pyopenjtalk.tts("おめでとうございます")

In [4]: wavfile.write("test.wav", sr, x.astype(np.int16))
```

Sections: pyopenjtalk-plus, Changes in this fork, pyopenjtalk, Notice, Build requirements, Quick demo, TTS, Run text processing frontend only, Grapheme-to-phoeneme (G2P), Create/Apply user dictionary, About `run_marine` option

</details>

### itk-numerics

ITK is an open-source toolkit for multidimensional image analysis

`pip install itk-numerics` · installs (wheel) · licence: Apache Software License · rank 11276 · last release 2026-08-07 · [PyPI](https://pypi.org/project/itk-numerics/) · [source](https://github.com/InsightSoftwareConsortium/ITK)

<details><summary>README extract</summary>

| | C++ | Python |

| Linux | | |
| Windows | | |
| macOS | | |
| macOS (Apple Silicon)| | |
| Linux (Code coverage)| | |

Links

* Homepage
* Download
* Documentation
* Discussion
* Software Guide
* Examples
* Issue tracking
* Submit a patch ...

Sections: ITK: The Insight Toolkit, The papers, The books, Specific software version

</details>

### woodwork

a data typing library for machine learning

`pip install woodwork` · installs (wheel) · licence: not stated · rank 11291 · last release 2024-05-14 · [PyPI](https://pypi.org/project/woodwork/) · [docs](https://woodwork.alteryx.com) · [source](https://github.com/alteryx/woodwork/)

<details><summary>README extract</summary>

Woodwork provides a common typing namespace for using your existing DataFrames in Featuretools, EvalML, and general ML. A Woodwork
DataFrame stores the physical, logical, and semantic data types present in the data. In addition, it can store metadata about the data, allowing you to store specific information you might need for your application.

Example:
```python
import pandas as pd
import woodwork as ww

df = pd.read_csv("
df.ww.init(name='retail')
df.ww.set_types(logical_types={
    'quantity': 'Integer',
    'customer_name': 'PersonFullName',
    'country': 'Categorical',
    'order_id': 'Categorical',
    'description': 'NaturalLanguage',
})
df.ww
```

Sections: Add-ons, Example, Built at Alteryx

</details>

### featuretools

a framework for automated feature engineering

`pip install featuretools` · installs (wheel) · licence: BSD 3-clause · rank 11299 · last release 2024-05-14 · [PyPI](https://pypi.org/project/featuretools/) · [docs](https://featuretools.alteryx.com) · [source](https://github.com/alteryx/featuretools/)

<details><summary>README extract</summary>

"One of the holy grails of machine learning is to automate more and more of the feature engineering process." ― Pedro Domingos, A Few Useful Things to Know about Machine Learning

Featuretools is a python library for automated feature engineering. See the documentation for more information.

Example:
```python
>> import featuretools as ft
>> es = ft.demo.load_mock_customer(return_entityset=True)
>> es.plot()
```

Sections: Add-ons, Example, Demos, Citing Featuretools, Built at Alteryx

</details>

### turboquant-py

Python implementation of the TurboQuant and QJL vector quantization algorithms

`pip install turboquant-py` · installs (wheel) · licence: Apache-2.0 · rank 11330 · last release 2026-03-27 · [PyPI](https://pypi.org/project/turboquant-py/) · [source](https://github.com/msilverblatt/turboquant-py)

<details><summary>README extract</summary>

Python implementation of the TurboQuant and QJL vector quantization algorithms.

turboquant-py implements the TurboQuant and QJL vector quantization algorithms from Google Research (ICLR 2026 / AISTATS 2026). ...

Example:
```python
import numpy as np
from turboquant import TurboQuant

vectors = np.random.randn(1000, 384)  # 1000 vectors, dim=384
tq = TurboQuant(dim=384, bit_width=2, mode="mse", seed=42)

compressed = tq.quantize(vectors)
reconstructed = tq.dequantize(compressed)

mse = float(np.mean((vectors - reconstructed) ** 2))
print(f"Reconstruction MSE: {mse:.6f}")

...
```

...

</details>

### forestci

Confidence intervals for scikit-learn forest algorithms

`pip install forestci` · installs (wheel) · licence: MIT · rank 11344 · last release 2026-10-03 · [PyPI](https://pypi.org/project/forestci/) · [docs](https://contrib.scikit-learn.org/forest-confidence-interval/) · [source](https://github.com/scikit-learn-contrib/forest-confidence-interval)

<details><summary>README extract</summary>

Forest algorithms are powerful ensemble methods for classification and regression.
However, predictions from these algorithms do contain some amount of error.
Prediction variability can illustrate how influential
the training set is for producing the observed random forest predictions. ...

Sections: `forestci`: confidence intervals for Forest algorithms, Examples, Rebuilding and publishing the documentation

</details>

### kubeflow

Kubeflow Python SDK to manage ML workloads and to interact with Kubeflow APIs.

`pip install kubeflow` · installs (wheel) · licence: Apache-2.0 · rank 11352 · last release 2026-08-10 · [PyPI](https://pypi.org/project/kubeflow/) · [docs](https://www.kubeflow.org/docs/components) · [source](https://github.com/kubeflow/sdk)

<details><summary>README extract</summary>

Latest News 🔥

- [2026/03] The Kubeflow SDK v0.4 is officially released with `SparkClient` and `ModelRegistryClient`
 support. Check out the announcement blog post.
- [2026/01] We have our official documentation here at Kubeflow SDK Documentation
- [2025/11] Please fill this survey
 to shape the future of Kubeflow SDK. ...

Features:
The Kubeflow SDK is a set of unified Pythonic APIs that let you run any AI workload at any scale –
without the need to learn Kubernetes. ...

Example:
```python
from kubeflow.trainer import TrainerClient, CustomTrainer, TrainJobTemplate

def get_torch_dist(learning_rate: str, num_epochs: str):
    import os
    import torch
    import torch.distributed as dist

    dist.init_process_group(backend="gloo")
    print("PyTorch Distributed Environment")
...

</details>

### scikit-bio

Data structures, algorithms and educational resources for bioinformatics.

`pip install scikit-bio` · installs (wheel) · licence: BSD-3-Clause · rank 11365 · last release 2026-09-21 · [PyPI](https://pypi.org/project/scikit-bio/) · [docs](https://scikit.bio/docs/latest/) · [source](https://github.com/scikit-bio/scikit-bio)

<details><summary>README extract</summary>

*scikit-bio is an open-source, BSD-licensed Python 3 package providing data structures, algorithms and educational resources for bioinformatics.*

Visit the scikit-bio website: to learn more about this project.

Sections: Adoption, Team, Collaboration, Branding

</details>

### mjlab

Isaac Lab API, powered by MuJoCo-Warp, for RL and robotics research.

`pip install mjlab` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 11366 · last release 2026-08-09 · [PyPI](https://pypi.org/project/mjlab/) · [source](https://github.com/mujocolab/mjlab)

<details><summary>README extract</summary>

mjlab combines Isaac Lab's manager-based API with MuJoCo Warp, a GPU-accelerated version of MuJoCo.
The framework provides composable building blocks for environment design,
with minimal dependencies and direct access to native MuJoCo data structures.

Sections: mjlab, Getting Started, Training Examples, 1. Velocity Tracking, 2. Motion Imitation, 3. Sanity-check with Dummy Agents, Documentation, Third-Party Code

</details>

### igwn-ligolw

Python LIGO Light-Weight XML I/O Library

`pip install igwn-ligolw` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 11394 · last release 2026-01-19 · [PyPI](https://pypi.org/project/igwn-ligolw/)

_README extract left out: share-alike licence._

### dipy

Diffusion MRI Imaging in Python

`pip install dipy` · installs (wheel) · licence: BSD License · rank 11401 · last release 2026-04-23 · [PyPI](https://pypi.org/project/dipy/) · [docs](https://docs.dipy.org/stable/) · [source](https://github.com/dipy/dipy)

<details><summary>README extract</summary>

DIPY [DIPYREF]_ is a python library for the analysis of MR diffusion imaging.

DIPY is for research only; please contact admins@dipy.org if you plan to deploy
in clinical settings.

Current information can always be found from the DIPY website -

Please see the DIPY community list at

Please see the users' forum at

Sections: Website, Mailing Lists, Code, Python versions and dependencies, Reference

</details>

### pyvcd

Value change dump (VCD) file support for Python

`pip install pyvcd` · installs (wheel) · licence: MIT · rank 11411 · last release 2026-10-19 · [PyPI](https://pypi.org/project/pyvcd/) · [source](https://github.com/SanDisk-Open-Source/pyvcd)

<details><summary>README extract</summary>

The PyVCD package writes and reads Value Change Dump (VCD) files as
specified in clause 21.7 of IEEE 1800-2023, which supersedes IEEE
1364-2005 without changing the VCD format.

Read the documentation.

Visit PyVCD on GitHub.

Example:
```python
>>> import sys
>>> from vcd import VCDWriter
>>> with VCDWriter(sys.stdout, timescale='1 ns', date='today') as writer:
...     counter_var = writer.register_var('a.b.c', 'counter', 'integer', size=8)
...     real_var = writer.register_var('a.b.c', 'x', 'real', init=1.23)
...     for timestamp, value in enumerate(range(10, 20, 2)):
...
```

Sections: PyVCD, Quick Start, PyVCD and the waveform ecosystem

</details>

### zhinst-core

Python API for Zurich Instruments Devices

`pip install zhinst-core` · installs (wheel) · licence: MIT · rank 11415 · last release 2026-10-29 · [PyPI](https://pypi.org/project/zhinst-core/) · [docs](https://docs.zhinst.com/labone_api_user_manual)

<details><summary>README extract</summary>

The `zhinst-core` package allows communication with Zurich Instruments devices from
the Python programming language. It's the native Python API of LabOne&reg;, the
Zurich Instruments control software.

The documentation for the `zhinst.core` binary extension can be accessed online or via the built-in `help` command: ...

Example:
```python
import zhinst.core
help(zhinst.core)
```

</details>

### pdb-tools

A swiss army knife for PDB files.

`pip install pdb-tools` · installs (wheel) · licence: Apache Software License, version 2 · rank 11436 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pdb-tools/) · [source](https://github.com/haddocking/pdb-tools)

<details><summary>README extract</summary>

A swiss army knife for manipulating and editing PDB files.

The Harms lab maintains a set of tools also called `pdbtools`, which perform a
slightly different set of functions. You can find them here.

Manipulating PDB files is often painful. ...

Sections: pdb-tools, Looking for the _other_ pdb-tools?, About, What can I do with them?, What _can't I do with them?, Requirements

</details>

### lightly

A deep learning package for self-supervised learning and world models

`pip install lightly` · installs (wheel) · licence: MIT License · rank 11444 · last release 2026-10-26 · [PyPI](https://pypi.org/project/lightly/) · [docs](https://docs.lightly.ai) · [source](https://github.com/lightly-ai/lightly)

<details><summary>README extract</summary>

LightlySSL is a computer vision framework for self-supervised learning and latent world models.

- Documentation
- Github
- Discord

For a commercial version with more features, including Docker support and pretraining
models for embedding, classification, detection, and segmentation tasks with
a single command, please contact sales@lightly.ai. ...

Features:
This self-supervised learning framework offers the following features:

- Modular framework, which exposes low-level building blocks such as loss functions and
 model heads.
- Easy to use and written in a PyTorch-like style. ...

Example:
```python
import torch
import torchvision

from lightly import loss
from lightly import transforms
from lightly.data import LightlyDataset
from lightly.models.modules import heads

...

</details>

### spm-calculator

Calculate Supplemental Poverty Measure thresholds and conditional forecasts

`pip install spm-calculator` · installs (wheel) · licence: MIT · rank 11447 · last release 2026-11-02 · [PyPI](https://pypi.org/project/spm-calculator/) · [docs](https://policyengine-docs.vercel.app/spm-calculator/) · [source](https://github.com/PolicyEngine/spm-calculator)

<details><summary>README extract</summary>

Calculate Supplemental Poverty Measure (SPM) thresholds with published national
inputs and conditional CE/ACS rolling forecasts. The package works offline for
standalone calculations and supplies the same forecast artifact to optional
PolicyEngine, Microcosm Frame and actual Axiom core integrations.

Install the package from
PyPI. ...

Example:
```python
from spm_calculator import SPMUnit, load_forecast

forecast = load_forecast()
result = forecast.calculate_unit(
    SPMUnit(
        unit_id="example-family",
        num_adults=2,
        num_children=2,
        tenure="renter",
        year=2025,
        geography_kind="national",
        resources=40_000,
    )
)
...
```

...

</details>

### gplearn

Genetic Programming in Python, with a scikit-learn inspired API

`pip install gplearn` · installs (wheel) · licence: BSD-3-Clause · rank 11458 · last release 2026-01-07 · [PyPI](https://pypi.org/project/gplearn/) · [source](https://github.com/trevorstephens/gplearn)

<details><summary>README extract</summary>

`gplearn` implements Genetic Programming in Python, with a scikit-learn inspired and compatible API.

While Genetic Programming (GP) can be used to perform a very wide variety of tasks, gplearn is purposefully constrained to solving symbolic regression problems. ...

</details>

### modelcif

Package for handling ModelCIF mmCIF and BinaryCIF files

`pip install modelcif` · installs (wheel) · licence: MIT · rank 11460 · last release 2026-08-18 · [PyPI](https://pypi.org/project/modelcif/) · [docs](https://python-modelcif.readthedocs.io/) · [source](https://github.com/ihmwg/python-modelcif)

<details><summary>README extract</summary>

This is a Python package to assist in handling mmCIF
and BinaryCIF files compliant with the
ModelCIF
extension. It works with Python 3.6 or later.

Please see the documentation or some
worked examples
for more details.

</details>

### pvanalytics

PVAnalytics is a python library for the analysis of photovoltaic system-level data.

`pip install pvanalytics` · installs (wheel) · licence: MIT · rank 11470 · last release 2024-11-27 · [PyPI](https://pypi.org/project/pvanalytics/)

<details><summary>README extract</summary>

PVAnalytics is a collection of functions for working with data
from photovoltaic power systems. The library includes functions for
general data quality tests such as outlier detection, validation that
data is physically plausible, filtering data for specific conditions,
and labeling specific features in the data.

Documentation:

Source code:

</details>

### pyxcp

Universal Calibration Protocol for Python

`pip install pyxcp` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 11489 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pyxcp/)

_README extract left out: share-alike licence._

### ihm

Package for handling IHM mmCIF and BinaryCIF files

`pip install ihm` · installs from source (sdist only) · licence: MIT · rank 11525 · last release 2026-10-07 · [PyPI](https://pypi.org/project/ihm/)

<details><summary>README extract</summary>

This is a Python package to assist in handling mmCIF
and BinaryCIF files compliant with the
integrative/hybrid modeling (IHM)
extension. It works with Python 3.6 or later.

To handle non-integrative theoretical models (for example, homology models),
see the python-modelcif package
which supports files compliant with the
ModelCIF
extension. ...

</details>

### neo

Neo is a package for representing electrophysiology data in Python, together with support for reading a wide range of neurophysiology file formats

`pip install neo` · installs (wheel) · licence: BSD-3-Clause · rank 11540 · last release 2026-10-15 · [PyPI](https://pypi.org/project/neo/) · [docs](http://neo.readthedocs.io/) · [source](https://github.com/NeuralEnsemble/python-neo)

<details><summary>README extract</summary>

Neo is a Python package for working with electrophysiology data in Python, together
with support for reading a wide range of neurophysiology file formats, including
Spike2, NeuroExplorer, AlphaOmega, Axon, Blackrock, Plexon, Tdt, and support for
writing to a subset of these formats plus non-proprietary formats including HDF5. ...

Sections: Neo, More information

</details>

### pyts

A python package for time series classification

`pip install pyts` · installs (wheel) · licence: BSD-3-Clause · rank 11592 · last release 2026-10-21 · [PyPI](https://pypi.org/project/pyts/) · [docs](https://pyts.readthedocs.io/) · [source](https://github.com/johannfaouzi/pyts)

<details><summary>README extract</summary>

pyts is a Python package for time series classification. It
aims to make time series classification easily accessible by providing
preprocessing and utility tools, and implementations of
state-of-the-art algorithms. Most of these algorithms transform time series,
thus pyts provides several tools to perform these transformations.

Sections: pyts: a Python package for time series classification, Dependencies, Documentation, Implemented features

</details>

### ViennaRNA

A library for the prediction and comparison of RNA secondary structures.

`pip install ViennaRNA` · installs (wheel) · licence: not stated · rank 11599 · last release 2026-11-06 · [PyPI](https://pypi.org/project/ViennaRNA/) · [docs](https://www.tbi.univie.ac.at/RNA)

<details><summary>README extract</summary>

A C code library and several stand-alone programs for the prediction and comparison of RNA secondary structures.

Amongst other things, our implementations allow you to:

- predict minimum free energy secondary structures
- calculate the partition function for the ensemble of structures
- compute various equilibrium probabilities ...

Sections: ViennaRNA Package, Availability, Documentation, Quick Start, Binary packages, Bioconda, Python interface only, Building a Python 3 sdist or wheel package, References, Contact

</details>

### ouster-sdk

Ouster Sensor SDK

`pip install ouster-sdk` · installs (wheel) · licence: BSD-3-Clause AND Ouster-Freeware-EULA (See project links) · rank 11606 · last release 2026-08-13 · [PyPI](https://pypi.org/project/ouster-sdk/) · [source](https://github.com/ouster-lidar/ouster-sdk)

<details><summary>README extract</summary>

The Ouster Sensor SDK provides developers with a comprehensive set of interfaces for interacting with Ouster sensor hardware.
The SDK includes a suite of tools, libraries, and APIs to access the full range of sensor features and generate recorded sensor data. ...

Sections: Ouster Python SDK, Licensing

</details>

### tensorflow-intel

TensorFlow is an open source machine learning framework for everyone.

`pip install tensorflow-intel` · does not install on CPython 3.14 · licence: Apache Software License · rank 11640 · last release 2024-10-25 · [PyPI](https://pypi.org/project/tensorflow-intel/)

<details><summary>README extract</summary>

TensorFlow is an open source software library for high performance numerical computation. Its flexible architecture allows easy deployment of computation across a variety of platforms, and from desktops to clusters of servers to mobile and edge devices. ...

</details>

### ydf

YDF (short for Yggdrasil Decision Forests) is a library for training, serving, evaluating and analyzing decision forest models such as Random Forest and Gradient Boosted Trees.

`pip install ydf` · installs (wheel) · licence: Apache Software License · rank 11652 · last release 2026-11-02 · [PyPI](https://pypi.org/project/ydf/) · [docs](https://ydf.readthedocs.io/) · [source](https://github.com/google/yggdrasil-decision-forests.git)

<details><summary>README extract</summary>

YDF is a library for training, serving, and interpreting decision forest
models. It acts as a lightweight, efficient wrapper around the C++
Yggdrasil Decision Forests
library.

It provides fast access to core methods along with advanced features for model
import/export, evaluation, and inspection. ...

Example:
```python
import ydf
import pandas as pd

# Load dataset
ds_path = "
train_ds = pd.read_csv(f"{ds_path}/adult_train.csv")
test_ds = pd.read_csv(f"{ds_path}/adult_test.csv")

# Train a Gradient Boosted Trees model
model = ydf.GradientBoostedTreesLearner(label="income").train(train_ds)

# Evaluate the model
print(model.evaluate(test_ds))

# Save the model
...
```

Sections: YDF - Yggdrasil Decision Forests for Python, Usage Example, Documentation

</details>

### flytekitplugins-ray

This package holds the Ray plugins for flytekit

`pip install flytekitplugins-ray` · installs (wheel) · licence: Apache Software License · rank 11698 · last release 2026-11-03 · [PyPI](https://pypi.org/project/flytekitplugins-ray/)

### trackers

A unified library for object tracking featuring clean room re-implementations of leading multi-object tracking algorithms

`pip install trackers` · installs (wheel) · licence: Apache Software License · rank 11724 · last release 2026-11-05 · [PyPI](https://pypi.org/project/trackers/)

<details><summary>README extract</summary>

Plug-and-play object tracking in Python (multi-object) for any detection model.

`trackers` is an object tracking library for Python. It gives you clean-room, benchmarked implementations of SORT, ByteTrack, OC-SORT, BoT-SORT, C-BIoU, and McByte — so occlusions, fast motion, and moving cameras stop being your problem to solve from scratch. ...

Features:
- Clean-room implementations. Every algorithm is re-implemented from the original paper — not vendored or wrapped. You can read it, understand it, and modify it.
- Apache 2.0, no copyleft. ...

Example:
```python
import cv2
import supervision as sv
from inference import get_model
from trackers import ByteTrackTracker

model = get_model(model_id="rfdetr-medium")
tracker = ByteTrackTracker()

cap = cv2.VideoCapture("video.mp4")
...

</details>

### PySpice

Simulate electronic circuit using Python and the Ngspice / Xyce simulators

`pip install PySpice` · installs (wheel) · licence: GNU General Public License (GPL) · rank 11738 · last release 2021-05-15 · [PyPI](https://pypi.org/project/PySpice/) · [docs](https://pyspice.fabrice-salvaire.fr) · [source](https://github.com/FabriceSalvaire/PySpice)

_README extract left out: share-alike licence._

### lithops

Run unmodified Python code at massive scale on any cloud, with no servers to manage

`pip install lithops` · installs (wheel) · licence: Apache-2.0 · rank 11762 · last release 2026-10-30 · [PyPI](https://pypi.org/project/lithops/) · [docs](https://lithops-cloud.github.io/docs/) · [source](https://github.com/lithops-cloud/lithops)

### itk

ITK is an open-source toolkit for multidimensional image analysis

`pip install itk` · installs (wheel) · licence: Apache Software License · rank 11775 · last release 2026-08-07 · [PyPI](https://pypi.org/project/itk/) · [source](https://github.com/InsightSoftwareConsortium/ITK)

<details><summary>README extract</summary>

| | C++ | Python |

| Linux | | |
| Windows | | |
| macOS | | |
| macOS (Apple Silicon)| | |
| Linux (Code coverage)| | |

Links

* Homepage
* Download
* Documentation
* Discussion
* Software Guide
* Examples
* Issue tracking
* Submit a patch ...

Sections: ITK: The Insight Toolkit, The papers, The books, Specific software version

</details>

### nvidia-matmul-heuristics

NVIDIA Matmul Heuristics

`pip install nvidia-matmul-heuristics` · installs (wheel) · licence: not stated · rank 11826 · last release 2025-08-25 · [PyPI](https://pypi.org/project/nvidia-matmul-heuristics/) · [docs](https://docs.nvidia.com/cuda/nvidia-matmul-heuristics/)

<details><summary>README extract</summary>

NVIDIA Matmul Heuristics is a module that provides heuristics for GEMM kernel meta-parameter selection and auto-tuning.

</details>

### quantecon

Import the main names to top level.

`pip install quantecon` · installs (wheel) · licence: not stated · rank 11829 · last release 2026-10-17 · [PyPI](https://pypi.org/project/quantecon/) · [docs](http://quanteconpy.readthedocs.org/en/latest/) · [source](https://github.com/quantecon/QuantEcon.py)

<details><summary>README extract</summary>

A high performance, open source Python code library for economics

Example:
```python
import quantecon as qe
```

Sections: QuantEcon.py, Usage, Examples and Sample Code, Downloading the `quantecon` Repository

</details>

### factor-analyzer

A Factor Analysis tool written in Python

`pip install factor-analyzer` · installs from source (sdist only) · licence: not stated · rank 11836 · last release 2024-02-08 · [PyPI](https://pypi.org/project/factor-analyzer/)

<details><summary>README extract</summary>

This is a Python module to perform exploratory and factor analysis (EFA), with several
optional rotations. It also includes a class to perform confirmatory factor
analysis (CFA), with certain pre-defined constraints. In exploratory factor analysis,
factor extraction can be performed using a variety of estimation techniques. ...

Example:
```python
In [1]: import pandas as pd
   ...: from factor_analyzer import FactorAnalyzer

In [2]: df_features = pd.read_csv('tests/data/test02.csv')

In [3]: fa = FactorAnalyzer(rotation=None)

In [4]: fa.fit(df_features)
Out[4]:
FactorAnalyzer(bounds=(0.005, 1), impute='median', is_corr_matrix=False,
...
```

Sections: FactorAnalyzer, Description, Examples, Requirements

</details>

### skan

Skeleton analysis in Python

`pip install skan` · installs (wheel) · licence: BSD License · rank 11854 · last release 2026-02-06 · [PyPI](https://pypi.org/project/skan/) · [docs](https://skeleton-analysis.org/stable/) · [source](https://github.com/jni/skan)

<details><summary>README extract</summary>

Python module to analyse skeleton (thin object) images

See the documentation at

</details>

### itk-io

ITK is an open-source toolkit for multidimensional image analysis

`pip install itk-io` · installs (wheel) · licence: Apache Software License · rank 11862 · last release 2026-08-07 · [PyPI](https://pypi.org/project/itk-io/) · [source](https://github.com/InsightSoftwareConsortium/ITK)

<details><summary>README extract</summary>

| | C++ | Python |

| Linux | | |
| Windows | | |
| macOS | | |
| macOS (Apple Silicon)| | |
| Linux (Code coverage)| | |

Links

* Homepage
* Download
* Documentation
* Discussion
* Software Guide
* Examples
* Issue tracking
* Submit a patch ...

Sections: ITK: The Insight Toolkit, The papers, The books, Specific software version

</details>

### fill-voids

Fill voids in 3D binary images fast.

`pip install fill-voids` · installs (wheel) · licence: LGPL-3.0-or-later · rank 11876 · last release 2026-04-30 · [PyPI](https://pypi.org/project/fill-voids/)

_README extract left out: share-alike licence._

### Pint-Pandas

Extend Pandas Dataframe with Physical quantities module

`pip install Pint-Pandas` · installs (wheel) · licence: BSD License · rank 11877 · last release 2026-03-20 · [PyPI](https://pypi.org/project/Pint-Pandas/)

<details><summary>README extract</summary>

Pandas support for pint

Example:
```python
>>> import pandas as pd
>>> import pint_pandas
```

Sections: Pint-Pandas, Documentation

</details>

### scitokens

SciToken reference implementation library

`pip install scitokens` · installs (wheel) · licence: Apache Software License · rank 11894 · last release 2026-03-13 · [PyPI](https://pypi.org/project/scitokens/) · [docs](https://scitokens.readthedocs.io/) · [source](https://github.com/scitokens/scitokens)

<details><summary>README extract</summary>

This library aims to be a reference implementation of the SciTokens'
JSON Web Token (JWT) token format.

SciTokens is built on top of the
PyJWT and
cryptography libraries. We aim
to provide a safe, high-level interface for token manipulation, avoiding
common pitfalls of using the underling libraries directly. ...

Example:
```python
>>> import scitokens
>>> token = scitokens.SciToken() # Create token and generate a new private key
>>> token2 = scitokens.SciToken(key=private_key) # Create token using existing key
```

Sections: SciTokens Library, Generating Tokens, Token Serialization, Validating Tokens, Enforcing SciTokens Logic, Creating Sample Tokens, Decorator, Configuration

</details>

### gmr

Gaussian Mixture Regression

`pip install gmr` · installs (wheel) · licence: BSD-3-Clause · rank 11904 · last release 2026-01-12 · [PyPI](https://pypi.org/project/gmr/)

<details><summary>README extract</summary>

> Gaussian Mixture Models (GMMs) for clustering and regression in Python.

(Source code of example)

* License: New BSD / BSD 3-clause

* API documentation

Example:
```python
import numpy as np
from gmr import GMM

# Your dataset as a NumPy array of shape (n_samples, n_features):
X = np.random.randn(100, 2)

gmm = GMM(n_components=3, random_state=0)
gmm.from_samples(X)

# Estimate GMM with expectation maximization:
X_sampled = gmm.sample(100)

# Make predictions with known values for the first feature:
...
```

Sections: gmr, Documentation, Example, How Does It Compare to scikit-learn?, Gallery, Saving a Model, API Documentation, Generate Documentation, Related Publications

</details>

### suitesparse-graphblas

SuiteSparse:GraphBLAS Python bindings.

`pip install suitesparse-graphblas` · installs (wheel) · licence: Apache-2.0 · rank 11954 · last release 2026-10-28 · [PyPI](https://pypi.org/project/suitesparse-graphblas/) · [source](https://github.com/GraphBLAS/python-suitesparse-graphblas)

<details><summary>README extract</summary>

Python CFFI Binding around
SuiteSparse:GraphBLAS

This is a base package that exposes only the low level CFFI API
bindings and symbols. This package is shared by the syntax bindings
pygraphblas and
python-graphblas.

Example:
```python
import micropip
await micropip.install("suitesparse-graphblas")
```

Sections: python-suitesparse-graphblas, In the browser (Pyodide)

</details>

### tabpfn-client

API access for TabPFN: Foundation model for tabular data

`pip install tabpfn-client` · installs (wheel) · licence: Apache Software License · rank 11975 · last release 2026-11-02 · [PyPI](https://pypi.org/project/tabpfn-client/) · [docs](https://priorlabs.ai/docs) · [source](https://github.com/priorlabs/tabpfn-client)

### opacus

Train PyTorch models with Differential Privacy

`pip install opacus` · installs (wheel) · licence: Apache Software License · rank 11987 · last release 2026-05-05 · [PyPI](https://pypi.org/project/opacus/) · [docs](https://opacus.ai/api) · [source](https://github.com/pytorch/opacus)

<details><summary>README extract</summary>

Opacus is a library that enables training PyTorch models
with differential privacy. It supports training with minimal code changes
required on the client, has little impact on training performance, and allows
the client to online track the privacy budget expended at any given moment.

This code release is aimed at two target audiences:

1. ...

Example:
```python
# define your components as usual
model = Net()
optimizer = SGD(model.parameters(), lr=0.05)
data_loader = torch.utils.data.DataLoader(dataset, batch_size=1024)

# enter PrivacyEngine
privacy_engine = PrivacyEngine()
model, optimizer, data_loader = privacy_engine.make_private(
    module=model,
    optimizer=optimizer,
    data_loader=data_loader,
...
```

...

</details>

### skorch

scikit-learn compatible neural network library for pytorch

`pip install skorch` · installs (wheel) · licence: not stated · rank 11991 · last release 2026-05-14 · [PyPI](https://pypi.org/project/skorch/)

<details><summary>README extract</summary>

A scikit-learn compatible neural network library that wraps PyTorch.

- Documentation
- Source Code
- Installation

Example:
```python
import numpy as np
from sklearn.datasets import make_classification
from torch import nn
from skorch import NeuralNetClassifier

X, y = make_classification(1000, 20, n_informative=10, random_state=0)
X = X.astype(np.float32)
y = y.astype(np.int64)

class MyModule(nn.Module):
    def init(self, num_units=10, nonlin=nn.ReLU()):
...
```

Sections: Resources, Examples, From source, Using conda, Using pip, PyTorch, External resources, Communication

</details>

### igwn-auth-utils

Authorisation utilities for IGWN

`pip install igwn-auth-utils` · installs (wheel) · licence: BSD License · rank 12020 · last release 2025-05-30 · [PyPI](https://pypi.org/project/igwn-auth-utils/) · [docs](https://igwn-auth-utils.readthedocs.io) · [source](https://git.ligo.org/computing/igwn-auth-utils.git)

<details><summary>README extract</summary>

Python library functions to simplify using IGWN authorisation credentials.


This project is primarily aimed at discovering X.509 credentials and
SciTokens for use with HTTP(S) requests to IGWN-operated services.

Example:
```python
>>> from igwn_auth_utils import find_x509_credentials
>>> print(find_x509_credentials())
('/tmp/x509up_u1000', '/tmp/x509up_u1000')
```

Sections: `igwn-auth-utils`, Basic usage

</details>

### qcodes

Python-based data acquisition framework developed by the Copenhagen / Delft / Sydney / Microsoft quantum computing consortium

`pip install qcodes` · installs (wheel) · licence: MIT · rank 12024 · last release 2026-10-26 · [PyPI](https://pypi.org/project/qcodes/) · [docs](https://microsoft.github.io/Qcodes/) · [source](https://github.com/microsoft/qcodes)

<details><summary>README extract</summary>

QCoDeS is a Python-based data acquisition framework developed by the
Copenhagen / Delft / Sydney / Microsoft quantum computing consortium.
While it has been developed to serve the needs of nanoelectronic device
experiments, it is not inherently limited to such experiments, and can
be used anywhere a system with many degrees of freedom is ...

Sections: QCoDeS, Default branch is now main, Docs, QCoDeS Loop, Trademarks

</details>

### pybamm

Python Battery Mathematical Modelling

`pip install pybamm` · installs (wheel) · licence: BSD License · rank 12033 · last release 2026-10-20 · [PyPI](https://pypi.org/project/pybamm/) · [docs](https://docs.pybamm.org) · [source](https://github.com/pybamm-team/PyBaMM)

<details><summary>README extract</summary>

PyBaMM (Python Battery Mathematical Modelling) is an open-source battery simulation package
written in Python. Our mission is to accelerate battery modelling research by
providing open-source tools for multi-institutional, interdisciplinary collaboration. ...

Example:
```python
import pybamm

model = pybamm.lithium_ion.DFN()  # Doyle-Fuller-Newman model
sim = pybamm.Simulation(model)
sim.solve([0, 3600])  # solve for 1 hour
sim.plot()
```

Sections: PyBaMM, 💻 Using PyBaMM, Versioning, Using pip, Using conda, Optional solvers, Model zoo, 📖 Citing PyBaMM, 📫 Get in touch

</details>

### qiskit-algorithms

Qiskit Algorithms: A library of quantum computing algorithms

`pip install qiskit-algorithms` · installs (wheel) · licence: Apache Software License · rank 12050 · last release 2025-08-29 · [PyPI](https://pypi.org/project/qiskit-algorithms/) · [docs](https://qiskit-community.github.io/qiskit-algorithms/) · [source](https://github.com/qiskit-community/qiskit-algorithms)

<details><summary>README extract</summary>

> [!WARNING]
> Qiskit Algorithms is no longer officially supported by IBM.
> Like any other Apache 2 licensed code, you are free to use it or/and extend it, but please be aware that it is under your own risk.

</details>

### itk-segmentation

ITK is an open-source toolkit for multidimensional image analysis

`pip install itk-segmentation` · installs (wheel) · licence: Apache Software License · rank 12063 · last release 2026-08-07 · [PyPI](https://pypi.org/project/itk-segmentation/) · [source](https://github.com/InsightSoftwareConsortium/ITK)

<details><summary>README extract</summary>

| | C++ | Python |

| Linux | | |
| Windows | | |
| macOS | | |
| macOS (Apple Silicon)| | |
| Linux (Code coverage)| | |

Links

* Homepage
* Download
* Documentation
* Discussion
* Software Guide
* Examples
* Issue tracking
* Submit a patch ...

Sections: ITK: The Insight Toolkit, The papers, The books, Specific software version

</details>

### lightly-utils

A utility package for lightly

`pip install lightly-utils` · installs (wheel) · licence: MIT License · rank 12064 · last release 2021-07-08 · [PyPI](https://pypi.org/project/lightly-utils/) · [docs](https://docs.lightly.ai) · [source](https://github.com/lightly-ai/lightly)

### nvidia-nvfatbin-cu12

NVIDIA compiler library for fatbin interaction

`pip install nvidia-nvfatbin-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 12090 · last release 2025-06-05 · [PyPI](https://pypi.org/project/nvidia-nvfatbin-cu12/)

<details><summary>README extract</summary>

NVIDIA compiler library for fatbin interaction

</details>

### skforecast

Python library for time series forecasting using scikit-learn compatible models, statistical methods, and foundation models.

`pip install skforecast` · installs (wheel) · licence: BSD-3-Clause · rank 12108 · last release 2026-10-08 · [PyPI](https://pypi.org/project/skforecast/) · [docs](https://skforecast.org) · [source](https://github.com/skforecast/skforecast)

<details><summary>README extract</summary>

| | |

| Package | |
| Meta | |
| Testing | |
| Community | |

Time series forecasting, from prototype to production. Skforecast is a Python library for time series forecasting using scikit-learn compatible models, statistical methods, and foundation models. ...

Example:
```python
from lightgbm import LGBMRegressor
from skforecast.recursive import ForecasterRecursive
from skforecast.datasets import load_demo_dataset

# Download demo dataset
y = load_demo_dataset()

# Create and fit the forecaster using the last 15 observations as features
forecaster = ForecasterRecursive(
...
```

Sections: About skforecast, Quick example, Features, One API for every kind of model, Built for production, Forecasters, Documentation, AI and tools

</details>

### tesseract

Tesselation based Recovery of Amorphous halo Concentrations

`pip install tesseract` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 12128 · last release 2015-07-13 · [PyPI](https://pypi.org/project/tesseract/)

_README extract left out: share-alike licence._

### semopy

Structural Equation Modeling Optimization in Python.

`pip install semopy` · installs from source (sdist only) · licence: MIT License · rank 12130 · last release 2024-01-04 · [PyPI](https://pypi.org/project/semopy/)

<details><summary>README extract</summary>

Visit our website for a detailed introduction

semopy is a Python package that includes numerous Structural Equation Modelling (SEM) techniques.

Features:
- Write down a model description in a user-friendly syntax
 - Estimate model's parameters using a variety of objective functions
 - Estimate models with population structure via random effects
 - Restricted Maximum Likelihood
 - Integration with ...

Sections: semopy, Features, Syntax, Quickstart, The first step, The second step, The third step, Would you like to know more?, Requirements

</details>

### tensorflow-recommenders

Tensorflow Recommenders, a TensorFlow library for recommender systems.

`pip install tensorflow-recommenders` · installs (wheel) · licence: Apache Software License · rank 12131 · last release 2026-01-23 · [PyPI](https://pypi.org/project/tensorflow-recommenders/)

<details><summary>README extract</summary>

TensorFlow Recommenders is a library for building recommender system models
using TensorFlow.

It helps with the full workflow of building a recommender system: data
preparation, model formulation, training, evaluation, and deployment. ...

Example:
```python
from typing import Dict, Text

import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_recommenders as tfrs

# Ratings data.
ratings = tfds.load('movielens/100k-ratings', split="train")
# Features of all the available movies.
movies = tfds.load('movielens/100k-movies', split="train")

# Select the basic features.
...
```

Sections: TensorFlow Recommenders, Documentation, Quick start

</details>

### skrl

Modular and flexible library for reinforcement learning on PyTorch, JAX and NVIDIA Warp

`pip install skrl` · installs (wheel) · licence: MIT License · rank 12160 · last release 2026-10-21 · [PyPI](https://pypi.org/project/skrl/) · [docs](https://skrl.readthedocs.io) · [source](https://github.com/Toni-SM/skrl)

<details><summary>README extract</summary>

[](

Documentation:

Description: ``skrl`` is an open-source modular library for Reinforcement Learning written in Python
(implemented in PyTorch, JAX and NVIDIA Warp)
and designed with a focus on modularity, readability, simplicity, and transparency of algorithm implementation. ...

Sections: SKRL - Reinforcement Learning library, Refer to the documentation for details and examples, Citing this library

</details>

### msgpack-numpy-opentensor

Numpy data serialization using msgpack

`pip install msgpack-numpy-opentensor` · installs (wheel) · licence: BSD License · rank 12182 · last release 2023-10-02 · [PyPI](https://pypi.org/project/msgpack-numpy-opentensor/)

<details><summary>README extract</summary>

Package Description

This package provides encoding and decoding routines that enable the
serialization and deserialization of numerical and array data types provided by
numpy using the highly efficient
msgpack format. Serialization of Python's
native complex data types is also supported.

Installation ...

</details>

### pyroots

Pure python single variable function solvers

`pip install pyroots` · installs (wheel) · licence: BSD License · rank 12184 · last release 2020-06-17 · [PyPI](https://pypi.org/project/pyroots/) · [docs](https://github.com/pmav99/pyroots) · [source](https://github.com/pmav99/pyroots)

<details><summary>README extract</summary>

Abstract

A Python library implementing various root finding methods for
single-variable functions.

Currently the following methods have been implemented:

- The bisect method.
- The ridder method.
- The brent method. ...

Example:
```python
# define the function whose root you are searching
def f(x, a):
    return x ** 2 - a + 1

# Create the Solver object (instead of Brentq you could also import Brenth/Ridder/Bisect)
from pyroots import Brentq
brent = Brentq(epsilon=1e-5)

# solve the function in `[-3, 0]` while `a` is equal to 2
result = brent(f, -3, 0, a=2)
print(result)
```

Sections: pyroots, Function

</details>

### ridgeplot

Beautiful ridgeline plots in python

`pip install ridgeplot` · installs (wheel) · licence: MIT License · rank 12232 · last release 2026-04-07 · [PyPI](https://pypi.org/project/ridgeplot/) · [docs](https://ridgeplot.readthedocs.io/en/stable/) · [source](https://github.com/tpvasconcelos/ridgeplot)

<details><summary>README extract</summary>

`ridgeplot` is a Python package that provides a simple interface for plotting beautiful and interactive ridgeline plots within the extensive Plotly ecosystem.

Example:
```python
import numpy as np
from ridgeplot import ridgeplot

my_samples = [np.random.normal(n, size=900) for n in range(6, 0, -2)]
fig = ridgeplot(samples=my_samples)
fig.show()
```

Sections: ridgeplot: beautiful ridgeline plots in Python, Getting started, Basic example, Flexible configuration, More examples

</details>

### itk-registration

ITK is an open-source toolkit for multidimensional image analysis

`pip install itk-registration` · installs (wheel) · licence: Apache Software License · rank 12235 · last release 2026-08-07 · [PyPI](https://pypi.org/project/itk-registration/) · [source](https://github.com/InsightSoftwareConsortium/ITK)

<details><summary>README extract</summary>

| | C++ | Python |

| Linux | | |
| Windows | | |
| macOS | | |
| macOS (Apple Silicon)| | |
| Linux (Code coverage)| | |

Links

* Homepage
* Download
* Documentation
* Discussion
* Software Guide
* Examples
* Issue tracking
* Submit a patch ...

Sections: ITK: The Insight Toolkit, The papers, The books, Specific software version

</details>

### pyproject2conda

A script to convert a Python project declared on a pyproject.toml to a conda environment.

`pip install pyproject2conda` · installs (wheel) · licence: NIST-PD · rank 12249 · last release 2026-08-19 · [PyPI](https://pypi.org/project/pyproject2conda/) · [docs](https://pages.nist.gov/pyproject2conda/)

<details><summary>README extract</summary>

<!-- markdownlint-disable MD041 -->

<!-- prettier-ignore-start -->
[][repo-link]
[][docs-link]
[][license-link]
[][pypi-link]
[][conda-link]
[][ruff-link]
[][uv-link]

<!--
 For more badges, see


<!-- other links -->

<!-- prettier-ignore-end -->

A script to convert `pyproject.toml` dependencies to `environment.yaml` files.

Features:
The main goal of `pyproject2conda` is to provide a means to keep all basic
dependency information, for both `pip` based and `conda` based environments, in
`pyproject.toml`. ...

Example:
```python
>>> from pyproject2conda.requirements import RequirementsConfig
>>> p = RequirementsConfig.from_path("./tests/data/test-pyproject.toml")

# Basic environment
>>> print(p.to_conda_yaml(python_include="infer").strip())
dependencies:
  - python<3.11,>=3.8
...

</details>

### tensorflow-cpu-aws

TensorFlow is an open source machine learning framework for everyone.

`pip install tensorflow-cpu-aws` · does not install on CPython 3.14 · licence: Apache Software License · rank 12297 · last release 2024-03-14 · [PyPI](https://pypi.org/project/tensorflow-cpu-aws/)

<details><summary>README extract</summary>

TensorFlow is an open source software library for high performance numerical
computation. Its flexible architecture allows easy deployment of computation
across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters
of servers to mobile and edge devices. ...

</details>

### trx-python

A community-oriented file format for tractography

`pip install trx-python` · installs (wheel) · licence: BSD License · rank 12299 · last release 2026-09-18 · [PyPI](https://pypi.org/project/trx-python/) · [docs](https://tee-ar-ex.github.io/trx-python/) · [source](https://github.com/tee-ar-ex/trx-python)

<details><summary>README extract</summary>

A Python implementation of the TRX file format for tractography data.

For details, please visit the documentation.

Example:
```python
from trx.io import load, save

# Load a tractogram (supports .trx, .trk, .tck, .vtk, .fib, .dpy)
trx = load("tractogram.trx")

# Save to a different format
save(trx, "output.trk")
```

Sections: trx-python, From PyPI, From Source, Quick Start, Loading and Saving Tractograms, Command-Line Interface, First-Time Setup, Common Commands, Code Quality, Pre-commit Hooks, Temporary Directory, Troubleshooting, Documentation

</details>

### pygeos

GEOS wrapped in numpy ufuncs

`pip install pygeos` · installs from source (sdist only) · licence: BSD 3-Clause · rank 12300 · last release 2022-12-12 · [PyPI](https://pypi.org/project/pygeos/)

<details><summary>README extract</summary>

PyGEOS is a C/Python library with vectorized geometry functions. The geometry
operations are done in the open-source geometry library GEOS. PyGEOS wraps
these operations in NumPy ufuncs providing a performance improvement when
operating on arrays of geometries. ...

Example:
```python
>>> geoms = points(*np.indices((4, 4)))
>>> polygon = box(0, 0, 2, 2)

>>> contains(polygon, geoms)

  array([[False, False, False, False],
         [False,  True, False, False],
         [False, False, False, False],
         [False, False, False, False]])
```

Sections: PyGEOS, What is a ufunc?, Multithreading, Examples, References

</details>

### mltable

Contains MLTable loading and authoring apis for the mltable package.

`pip install mltable` · does not install on CPython 3.14 · licence: Other/Proprietary License · rank 12303 · last release 2026-08-07 · [PyPI](https://pypi.org/project/mltable/)

<details><summary>README extract</summary>

MLTable is a Python package that provides fast, flexible data loading functions designed to make accessing "tabular" data easy and intuitive. MLTable will help you to abstract the schema definition for tabular data so that it is easier to materialize the table into a Pandas dataframe. ...

Features:
- added authrization support
- `MLTable.save()` bug fixes

Sections: mltable: machine learning table data toolkit, Main Features, Getting started, Documentation, 1.6.3 (2025-09-08), Bugs Fixed, 1.6.2 (2025-08-27), 1.6.1 (2024-01-24), Features Added, 1.5.0 (2023-08-14), 1.4.1 (2023-06-19)

</details>

### pyepics

Epics Channel Access for Python

`pip install pyepics` · installs (wheel) · licence: not stated · rank 12306 · last release 2026-05-20 · [PyPI](https://pypi.org/project/pyepics/) · [docs](https://pyepics.github.io/pyepics/)

<details><summary>README extract</summary>

PyEpics is a Python interface to the EPICS Channel Access (CA) library
for the EPICS control system.

The PyEpics module includes both low-level (C-like) and higher-level access
(with Python objects) to the EPICS Channnel Access (CA) protocol. ...

Features:
Pyepics provides two principle modules: ca, and pv, and functions
caget(), caput(), and cainfo() for the simplest of interaction with EPICS. ...

Example:
```python
 ~> python
 >>> from epics import caget, caput, cainfo
 >>> print(caget('XXX:m1.VAL'))
1.200
>>> caput('XXX:m1.VAL',2.30)
1
>>> cainfo('XXX.m1.VAL')
== XXX:m1.VAL  (double) ==
   value      = 2.3
   char_value = 2.3000
   count      = 1
   units      = mm
   precision  = 4
   host       = xxx.aps.anl.gov:5064
   access     = read/write
...
```

...

</details>

### slycot

A wrapper for the SLICOT control and systems library

`pip install slycot` · installs (wheel) · licence: GPL-2.0 AND BSD-3-Clause AND GPL-3.0-with-GCC-exception AND BSD-2-Clause · rank 12329 · last release 2026-10-17 · [PyPI](https://pypi.org/project/slycot/)

_README extract left out: share-alike licence._

### nipype

Neuroimaging in Python: Pipelines and Interfaces

`pip install nipype` · installs (wheel) · licence: Apache-2.0 · rank 12371 · last release 2026-08-25 · [PyPI](https://pypi.org/project/nipype/) · [docs](http://nipy.org/nipype) · [source](http://github.com/nipy/nipype)

<details><summary>README extract</summary>

Current neuroimaging software offer users an incredible opportunity to
analyze data using a variety of different algorithms. However, this has
resulted in a heterogeneous collection of specialized applications
without transparent interoperability or a uniform operating interface. ...

Sections: Documentation, Python 2 Statement

</details>

### flytekitplugins-spark

Spark 3 plugin for flytekit

`pip install flytekitplugins-spark` · installs (wheel) · licence: Apache Software License · rank 12375 · last release 2026-11-03 · [PyPI](https://pypi.org/project/flytekitplugins-spark/)

### pyjoulescope-driver

Joulescope™ driver

`pip install pyjoulescope-driver` · installs (wheel) · licence: Apache-2.0 · rank 12394 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pyjoulescope-driver/) · [source](https://github.com/jetperch/joulescope_driver/)

<details><summary>README extract</summary>

<!--

Sections: SPDX-FileCopyrightText: Copyright 2014-2026 Jetperch LLC, Joulescope Driver, Building, Windows, macOS, Ubuntu, Common, Build python bindings

</details>

### broadbean

Package for easily generating and manipulating signal pulses.

`pip install broadbean` · installs (wheel) · licence: MIT License · rank 12404 · last release 2026-05-11 · [PyPI](https://pypi.org/project/broadbean/)

<details><summary>README extract</summary>

A library for making pulses that can be leveraged with QCoDeS (in
particular with Tektronix 5000/7000 series AWG drivers),
but also works as standalone.

Usage examples can be found in broadbean's documentation here.

Short description: The broadbean module lets the user compose and
manipulate pulse sequences. ...

Sections: Broadbean aka QCoDeS Pulse Builder, Formal requirements

</details>

### sectionproperties

A python package for the analysis of arbitrary cross-sections using the finite element method.

`pip install sectionproperties` · installs (wheel) · licence: MIT License · rank 12468 · last release 2026-01-24 · [PyPI](https://pypi.org/project/sectionproperties/) · [docs](https://sectionproperties.readthedocs.io) · [source](https://github.com/robbievanleeuwen/section-properties)

<details><summary>README extract</summary>

[][pypi]
[][status]
[][python version]
[][license]
[][read the docs]
[][uv]
[][ruff]
[][pre-commit]
[][tests]
[][codecov]
[][joss]

`sectionproperties` is a python package for the analysis of arbitrary cross-sections
using the finite element method. ...

Features:
See the complete list of `sectionproperties` features
here.

Sections: Documentation, Features, Disclaimer

</details>

### cytriangle

Object-oriented Cython wrapper of Shewchuk's Triangle Library

`pip install cytriangle` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3); Other/Proprietary License · rank 12480 · last release 2026-01-22 · [PyPI](https://pypi.org/project/cytriangle/) · [source](https://github.com/m-clare/cytriangle)

_README extract left out: share-alike licence._

### hepunits

Units and constants in the HEP system of units

`pip install hepunits` · installs (wheel) · licence: BSD-3-Clause · rank 12486 · last release 2026-10-01 · [PyPI](https://pypi.org/project/hepunits/)

<details><summary>README extract</summary>

|GitHub Actions Status: CICode Coverage|

`hepunits` collects the most commonly used units and constants in the
HEP System of Units, as derived from the basic units originally defined by the CLHEP project,
which are *not* the same as the SI system of units: ...

Example:
```python
>>> from hepunits.constants import c_light
>>> from hepunits.units import picosecond, micrometer
>>> tau_Bs = 1.5 * picosecond  # a particle lifetime, say the Bs meson's
>>> ctau_Bs = c_light * tau_Bs  # ctau of the particle, ~450 microns
>>> print(ctau_Bs)  # result in HEP units, so mm
0.449688687
...
```

Sections: `hepunits`: units and constants in the HEP system of units, Getting started, Fancier usage, Pint integration

</details>

### virtualizarr

Create virtual Zarr stores from archival data using xarray API

`pip install virtualizarr` · installs (wheel) · licence: Apache-2.0 · rank 12512 · last release 2026-10-14 · [PyPI](https://pypi.org/project/virtualizarr/) · [docs](https://github.com/zarr-developers/VirtualiZarr/blob/main/README.md)

<details><summary>README extract</summary>

The best way to distribute large scientific datasets is via the Cloud, in Cloud-Optimized formats [^1]. But often this data is stuck in archival pre-Cloud file formats such as netCDF. ...

Features:
* Create virtual references pointing to bytes inside an archival file with `open_virtual_dataset`.
* Supports a range of archival file formats, including netCDF4 and HDF5, and has a pluggable system for supporting new formats. ...

Sections: VirtualiZarr, Features, Inspired by Kerchunk, Articles, Talks and Presentations, References

</details>

### prefetch-generator

a simple tool to compute arbitrary generator in a background thread

`pip install prefetch-generator` · installs from source (sdist only) · licence: The Unlicense (Unlicense) · rank 12519 · last release 2022-11-19 · [PyPI](https://pypi.org/project/prefetch-generator/)

<details><summary>README extract</summary>

Based on

This is a single-function package that makes it possible to transform any generator into a `BackgroundGenerator` which computes any number of elements from the generator ahead, in a background thread.

It is quite lightweight, but not entirely weightless. ...

Sections: for item in BackgroundGenerator(my_generator), do_stuff(item), @prefetch(), def my_generator(some_param), while True, X = read_heavy_file(), y = wget_from_cornhub(), do_pretty_much_anything(some_param), yield X, y

</details>

### roc-validator

A Python package to validate RO-Crates

`pip install roc-validator` · installs (wheel) · licence: Apache Software License · rank 12527 · last release 2026-10-29 · [PyPI](https://pypi.org/project/roc-validator/) · [docs](https://github.com/crs4/rocrate-validator) · [source](https://github.com/crs4/rocrate-validator)

<details><summary>README extract</summary>

`rocrate-validator` (available as `roc-validator` on PyPI) is a Python package to validate RO-Crates
against different profiles, including the base RO-Crate profile and various extensions.

Features:
- Validates RO-Crates against the profiles they declare to conform to.
 Currently, validation for the following profiles is implemented:
 - RO-Crate 1.3 *(base profile, used by default)*
 - RO-Crate 1.2 *(base profile)*
 - RO-Crate 1.1 *(base ...

Example:
```python
# Import the `services` and `models` module from the rocrate_validator package
from rocrate_validator import services, models

# Create an instance of `ValidationSettings` class to configure the validation
settings = services.ValidationSettings(
    # Set the path to the RO-Crate root directory
    rocrate_uri='/path/to/ro-crate',
...

</details>

### ai-dynamo-runtime

Dynamo Inference Framework Runtime

`pip install ai-dynamo-runtime` · installs (wheel) · licence: Apache Software License · rank 12562 · last release 2026-11-05 · [PyPI](https://pypi.org/project/ai-dynamo-runtime/)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2024-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at ...

Sections: Dynamo Python Bindings, 🚀 Quick Start, Run Examples, Prerequisite, Hello World Example, Performance

</details>

### pyorbital

Scheduling satellite passes in Python

`pip install pyorbital` · installs (wheel) · licence: Apache-2.0 · rank 12563 · last release 2026-10-12 · [PyPI](https://pypi.org/project/pyorbital/) · [docs](https://pyorbital.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

This is the Pyorbital, a Python package for computing orbital parameters from TLE
files, and making various astronomical computations.

It is part of the Pytroll project:

</details>

### qiskit-ionq

Qiskit provider for IonQ backends

`pip install qiskit-ionq` · installs (wheel) · licence: Apache Software License · rank 12565 · last release 2026-06-05 · [PyPI](https://pypi.org/project/qiskit-ionq/) · [source](https://github.com/qiskit-community/qiskit-ionq)

<details><summary>README extract</summary>

Qiskit is an open-source SDK for working with quantum computers at the level of circuits, algorithms, and application modules.

This project contains a provider that allows access to [IonQ] ion trap quantum
systems.

The example python notebook (in `/example`) should help you understand basic usage. ...

Example:
```python
from qiskit_ionq import IonQProvider

provider = IonQProvider("token")
```

Sections: Qiskit IonQ Provider, API Access, Provider Setup, Credential Environment Variables, Submitting a Circuit, Compilation as a service (`dry_run`), Per-shot memory (`memory`), Mid-circuit measurements, Basis gates and transpilation, Running Tests, Fixtures, SSL certificate issues, Documentation

</details>

### netron

Viewer for neural network, deep learning and machine learning models.

`pip install netron` · installs (wheel) · licence: MIT · rank 12566 · last release 2026-11-06 · [PyPI](https://pypi.org/project/netron/)

<details><summary>README extract</summary>

Netron is a viewer for neural network, deep learning and machine learning models.

Netron supports ONNX, TensorFlow Lite, PyTorch, torch.export, ExecuTorch, TorchScript, TensorFlow, Core ML, OpenVINO, Keras, Caffe, Darknet, Safetensors and NumPy.

Netron has experimental support for MLIR, JAX, GGUF, RKNN, ncnn, MNN, PaddlePaddle and scikit-learn.

</details>

### torch-npu

NPU bridge for PyTorch

`pip install torch-npu` · installs (wheel) · licence: BSD License · rank 12614 · last release 2026-10-15 · [PyPI](https://pypi.org/project/torch-npu/)

<details><summary>README extract</summary>

PyTorch Adapter Plugin for Ascend NPU

 English | 简体中文

 Supported Versions ·
 Installation ·
 Quick Start ·
 Compatibility ·
 Support ·
 Contributing ·
 Docs ·
 Community

Features:
As the core component of the Ascend for PyTorch community, TorchNPU is a deep learning adapter plugin built by Ascend for PyTorch, enabling the PyTorch framework to directly invoke Ascend NPU and providing developers with the powerful compute ...

Example:
```python
import torch
import torch_npu

x = torch.randn(2, 2).npu()
y = torch.randn(2, 2).npu()
z = x.mm(y)
print(z)
```

Sections: TorchNPU, Overview, Key Features, Latest News, From Binary, From Source, Quick Start, Initialize Environment, Run Example, Disclaimer

</details>

### zhinst-toolkit

Zurich Instruments Toolkit High Level API

`pip install zhinst-toolkit` · installs (wheel) · licence: MIT License · rank 12631 · last release 2026-11-05 · [PyPI](https://pypi.org/project/zhinst-toolkit/)

<details><summary>README extract</summary>

The Zurich Instruments Toolkit (zhinst-toolkit) is a high level driver package
that allows communication with Zurich Instruments devices from the Python
programming language. It is based on top of the native
Python API (``zhinst.core``) of LabOne®,
the Zurich Instruments control software. ...

Sections: Zurich Instruments Toolkit (zhinst-toolkit), LabOne software, Documentation

</details>

### particle

Extended PDG particle data and MC identification codes

`pip install particle` · installs (wheel) · licence: BSD-3-Clause · rank 12652 · last release 2026-10-29 · [PyPI](https://pypi.org/project/particle/)

<details><summary>README extract</summary>

Particle provides a pythonic interface to the Particle Data Group (PDG)
particle data tables and particle identification codes,
with extended particle information and extra goodies.

The PDG defines the standard particle identification (ID) numbering scheme.
The package provides the `PDGID` class implementing queries on those PDG IDs. ...

Example:
```python
>>> from particle import PDGID
>>>
>>> pid = PDGID(211)
>>> pid

>>> pid.is_meson
True
>>> pid = PDGID(99999999)
>>> pid
```

...

</details>

### mne-bids

MNE-BIDS: Organizing MEG, EEG, and iEEG data according to the BIDS specification and facilitating their analysis with MNE-Python

`pip install mne-bids` · installs (wheel) · licence: OSI Approved · rank 12679 · last release 2026-09-29 · [PyPI](https://pypi.org/project/mne-bids/) · [docs](https://mne.tools/mne-bids) · [source](https://github.com/mne-tools/mne-bids)

<details><summary>README extract</summary>

MNE-BIDS is a Python package that allows you to read and write
BIDS-compatible datasets with the help of
MNE-Python.

Why?

MNE-BIDS links BIDS and MNE-Python with the goal to make your analyses faster to code and more robust,
and to facilitate data and code sharing with co-workers and collaborators. ...

</details>

### geomloss

Geometric loss functions between point clouds, images and volumes.

`pip install geomloss` · installs (wheel) · licence: MIT · rank 12740 · last release 2026-05-05 · [PyPI](https://pypi.org/project/geomloss/)

### qiskit-terra

Software for developing quantum computing programs

`pip install qiskit-terra` · installs (wheel) · licence: Apache Software License · rank 12748 · last release 2024-09-27 · [PyPI](https://pypi.org/project/qiskit-terra/) · [docs](https://docs.quantum.ibm.com) · [source](https://github.com/Qiskit/qiskit)

<details><summary>README extract</summary>

> [!IMPORTANT]
> The package `qiskit-terra` is not going to be updated after August 15th, 2024. Since Qiskit 0.44 (released on July 27th, 2023), the `qiskit` meta-package only contains `qiskit-terra`. In Qiskit 1.0 and beyond, the meta-package architecture is removed. ...

Example:
```python
import numpy as np
from qiskit import QuantumCircuit

# 1. A quantum circuit for preparing the quantum state |000> + i |111>
qc_example = QuantumCircuit(3)
qc_example.h(0)          # generate superpostion
qc_example.p(np.pi/2,0)  # add quantum phase
qc_example.cx(0,1)       # 0th-qubit-Controlled-NOT gate on 1st qubit
...
```

Sections: Qiskit, Create your first quantum program in Qiskit, Executing your code on real quantum hardware

</details>

### fysom

pYthOn Finite State Machine

`pip install fysom` · installs from source (sdist only) · licence: MIT License · rank 12759 · last release 2021-09-10 · [PyPI](https://pypi.org/project/fysom/)

### doppler-dsp

Practical, portable, performant digital signal processing.

`pip install doppler-dsp` · installs (wheel) · licence: MIT License · rank 12779 · last release 2026-11-08 · [PyPI](https://pypi.org/project/doppler-dsp/) · [docs](https://doppler-dsp.github.io/doppler/) · [source](https://github.com/doppler-dsp/doppler)

<details><summary>README extract</summary>

Practical, portable, performant digital signal processing.

doppler is a C99 DSP library — NCO, FIR, FFT, polyphase resampling, DDC,
AGC, carrier and burst acquisition, DSSS receivers, convolutional and
Reed-Solomon coding, CCSDS framing and more — with file, buffer, and
NATS-based streaming, and a
scenario-driven waveform generator (`wfmgen`) ...

Features:
Every algorithm lives in C exactly once. The Python layer is type conversion
and lifetime bridging — a few hundred lines of glue, not a reimplementation. ...

Example:
```python
from doppler.spectral import FFT
import numpy as np

x = np.random.randn(1024).astype(np.complex64)
X = FFT(1024).execute_cf32(x)
print(f"FFT: {len(x)} samples in -> {X.shape[0]} complex64 bins out")
```

...

</details>

### pysoem

Cython wrapper for the SOEM Library

`pip install pysoem` · installs (wheel) · licence: MIT License · rank 12787 · last release 2026-01-11 · [PyPI](https://pypi.org/project/pysoem/) · [docs](https://pysoem.readthedocs.io)

<details><summary>README extract</summary>

PySOEM is a Cython wrapper for the Simple Open EtherCAT Master Library (

PySOEM enables basic system testing of EtherCAT slave devices with Python.

Features

* input process data read and output process data write
* SDO read and write
* EEPROM read and write
* FoE read and write

Todo

* EoE ...

Sections: PySOEM, Introduction, Requirements, Linux, Windows, macOS (new with PySOEM 1.1.5), Usage, Changes, v1.1.13, v1.1.12, v1.1.11, v1.1.10, v1.1.9, v1.1.8

</details>

### MAVProxy

MAVProxy MAVLink ground station

`pip install MAVProxy` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 12789 · last release 2026-09-24 · [PyPI](https://pypi.org/project/MAVProxy/)

_README extract left out: share-alike licence._

### pycausalimpact

Python version of Google's Causal Impact model

`pip install pycausalimpact` · installs (wheel) · licence: Apache Software License · rank 12801 · last release 2020-05-11 · [PyPI](https://pypi.org/project/pycausalimpact/)

<details><summary>README extract</summary>

Python causal impact (or causal inference) implementation of Google's model with all functionalities fully ported and tested.

The main goal of the algorithm is to infer the expected effect a given intervention (or any action) had on some response variable by analyzing differences between expected and observed time series data. ...

Example:
```python
import numpy as np
import pandas as pd
from statsmodels.tsa.arima_process import ArmaProcess
from causalimpact import CausalImpact

np.random.seed(12345)
ar = np.r[1, 0.9]
ma = np.array([1])
arma_process = ArmaProcess(ar, ma)
X = 100 + arma_process.generate_sample(nsample=100)
y = 1.2 * X + np.random.normal(size=100)
y[70:] += 5

...
```

...

</details>

### pointblank

Find out if your data is what you think it is.

`pip install pointblank` · installs (wheel) · licence: MIT License · rank 12816 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pointblank/)

<details><summary>README extract</summary>

> [!TIP]
> 📖 Pointblank: The Complete Guide: A comprehensive (and free!) book on data validation with Pointblank is now being written. Follow along and learn everything from first steps to advanced validation patterns and AI-assisted workflows.

📊 Book chapter progress

Overall: 31% complete — 14 of 37 chapters have content

Foundations ...

Features:
- Works with your existing stack: Seamlessly integrates with Polars, Pandas, DuckDB, MySQL, PostgreSQL, SQLite, Parquet, PySpark, Snowflake, and more! ...

Example:
```python
import pointblank as pb

# Load your data
data = pb.load_dataset("game_revenue")              # A sample dataset

# Use DraftValidation to generate a validation plan
pb.DraftValidation(data=data, model="anthropic:claude-opus-4-6")
```

...

</details>

### pyvrp

A state-of-the-art vehicle routing problem solver.

`pip install pyvrp` · installs (wheel) · licence: MIT · rank 12850 · last release 2026-10-16 · [PyPI](https://pypi.org/project/pyvrp/) · [docs](https://pyvrp.org/) · [source](https://github.com/PyVRP/PyVRP)

<details><summary>README extract</summary>

PyVRP is an open-source, state-of-the-art vehicle routing problem (VRP) solver developed by Applied Routing.
It currently supports VRPs with:
- Pickups and deliveries (capacitated VRP, VRP with simultaneous pickup and delivery, VRP with backhaul, pickup and delivery VRP); ...

Sections: Tutorials, Getting help

</details>

### kerchunk

Functions to make reference descriptions for ReferenceFileSystem

`pip install kerchunk` · installs (wheel) · licence: MIT License · rank 12873 · last release 2026-03-30 · [PyPI](https://pypi.org/project/kerchunk/) · [docs](https://fsspec.github.io/kerchunk)

<details><summary>README extract</summary>

Cloud-friendly access to archival data

Kerchunk is a library that provides a unified way to represent a variety of chunked, compressed
data formats (e.g. NetCDF, HDF5, GRIB),
allowing efficient access to the data from traditional file systems or cloud object storage.
It also provides a flexible way to create
virtual datasets from multiple files. ...

</details>

### anastruct

Finite element analysis of 2D structures

`pip install anastruct` · installs (wheel) · licence: GNU General Public License v3 (GPLv3); GNU General Public License v3 or later (G · rank 12888 · last release 2026-10-31 · [PyPI](https://pypi.org/project/anastruct/) · [docs](http://anastruct-docs.readthedocs.io) · [source](https://github.com/ritchie46/anaStruct)

_README extract left out: share-alike licence._

### quantile-forest

Quantile regression forests compatible with scikit-learn.

`pip install quantile-forest` · installs (wheel) · licence: Apache-2.0 · rank 12890 · last release 2026-11-07 · [PyPI](https://pypi.org/project/quantile-forest/) · [docs](https://zillow.github.io/quantile-forest) · [source](https://github.com/zillow/quantile-forest)

<details><summary>README extract</summary>

quantile-forest offers a Python implementation of quantile regression forests compatible with scikit-learn.

Quantile regression forests (QRF) are a non-parametric, tree-based ensemble method for estimating conditional quantiles, with application to high-dimensional data and uncertainty estimation [[1]](#1). ...

Example:
```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from quantile_forest import RandomForestQuantileRegressor

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
qrf = RandomForestQuantileRegressor().fit(X_train, y_train)
...
```

</details>

### edt

Multi-Label Anisotropic Euclidean Distance Transform 3D

`pip install edt` · installs (wheel) · licence: LGPL-3.0-or-later · rank 12894 · last release 2026-07-02 · [PyPI](https://pypi.org/project/edt/)

_README extract left out: share-alike licence._

### tensorflow-transform

A library for data preprocessing with TensorFlow

`pip install tensorflow-transform` · installs (wheel) · licence: Apache Software License · rank 12902 · last release 2026-06-11 · [PyPI](https://pypi.org/project/tensorflow-transform/)

<details><summary>README extract</summary>

<!-- See: www.tensorflow.org/tfx/transform/ -->

*TensorFlow Transform* is a library for preprocessing data with TensorFlow.
`tf.Transform` is useful for data that requires a full-pass, such as:

* Normalize an input value by mean and standard deviation.
* Convert strings to integers by generating a vocabulary over all input values. ...

Sections: TensorFlow Transform, Build TFT from source, Nightly Packages, Running Tests, Notable Dependencies, Compatible versions, Questions

</details>

### vrplib

Python library for reading and writing VRP instances.

`pip install vrplib` · installs (wheel) · licence: MIT · rank 12920 · last release 2026-04-06 · [PyPI](https://pypi.org/project/vrplib/) · [source](https://github.com/PyVRP/VRPLIB)

<details><summary>README extract</summary>

`vrplib` is a Python package for working with Vehicle Routing Problem (VRP) instances. The main features are:
- reading VRPLIB and Solomon instances and solutions, and
- writing VRPLIB-style instances and solutions.

- Installation
- Example usage
- Documentation

Example:
```python
import vrplib

# Read VRPLIB formatted instances (default)
instance = vrplib.read_instance("/path/to/X-n101-k25.vrp")
solution = vrplib.read_solution("/path/to/X-n101-k25.sol")

# Read Solomon formatted instances
instance = vrplib.read_instance("/path/to/C101.txt", instance_format="solomon")
...
```

...

</details>

### latch

The Latch SDK

`pip install latch` · installs (wheel) · licence: not stated · rank 12960 · last release 2026-10-28 · [PyPI](https://pypi.org/project/latch/) · [docs](https://latch.wiki) · [source](https://github.com/latchbio/latch)

<details><summary>README extract</summary>

The Latch SDK is a framework to build and deploy bioinformatics workflows, and
dynamically generate associated interfaces, with a handful of python functions.

It is built directly on Flyte for all the benefits that the Kubernetes-native
workflow orchestration framework provides - task-level type-safety and
containerization, independent task ...

Sections: Latch SDK, Quickstart, Examples

</details>

### geneva

Geneva - Multimodal Data Lake for AI

`pip install geneva` · does not install on CPython 3.14 · licence: LicenseRef-Proprietary · rank 12966 · last release 2026-11-04 · [PyPI](https://pypi.org/project/geneva/)

<details><summary>README extract</summary>

Geneva is a petabyte-scale multimodal feature engineering and data management platform built on LanceDB.

- `src/` - Geneva client library and core runtime
- `src/tests/` - unit test suites
- `src/integ_tests/` - integration test suites
- `src/stress_tests/` - stress and load tests ...

Sections: Geneva - Multimodal Data Platform, What lives in this repo, Configuration

</details>

### negspacy

A spaCy pipeline component for negating concepts in text (NegEx).

`pip install negspacy` · installs (wheel) · licence: MIT License · rank 13052 · last release 2026-04-20 · [PyPI](https://pypi.org/project/negspacy/)

<details><summary>README extract</summary>

spaCy pipeline object for negating concepts in text. Based on the NegEx algorithm.

***NegEx - A Simple Algorithm for Identifying Negated Findings and Diseases in Discharge Summaries
Chapman, Bridewell, Hanbury, Cooper, Buchanan*** ...

Example:
```python
from negspacy.negation import Negex
from negspacy.termsets import termset

ts = termset("en")

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe(
    "negex",
    config={
        "neg_termset":ts.get_patterns()
    }
)
```

Sections: negspacy: negation for spaCy, What's new, NegEx Patterns, Termsets, Additional Functionality, Change patterns or view patterns in use, Negations with Spans, Negations in noun chunks, Other libraries

</details>

### arxiv-mcp-server

A flexible arXiv search and analysis service with MCP protocol support

`pip install arxiv-mcp-server` · installs (wheel) · licence: Apache-2.0 · rank 13060 · last release 2026-10-08 · [PyPI](https://pypi.org/project/arxiv-mcp-server/) · [docs](https://github.com/blazickjp/arxiv-mcp-server#readme) · [source](https://github.com/blazickjp/arxiv-mcp-server)

<details><summary>README extract</summary>

<!-- mcp-name: io.github.blazickjp/arxiv-mcp-server -->

A local MCP server for agent literature work. The differentiator is original-LaTeX section reads, BibTeX from arXiv metadata, and topic watches. Papers stay on disk. The working loop is paper ID → outline → one section → citations. Search is optional.

Features:
Search, source retrieval, citation graphs, and downloads call their respective external services. What stays local is the literature loop: read author-submitted LaTeX one section at a time, export BibTeX from authoritative arXiv metadata, and keep ...

...

</details>

### stravalib

A Python package that makes it easy to access and download data from the Strava V3 REST API.

`pip install stravalib` · installs (wheel) · licence: Apache-2.0 · rank 13063 · last release 2026-08-27 · [PyPI](https://pypi.org/project/stravalib/) · [docs](https://stravalib.readthedocs.io) · [source](https://github.com/stravalib/stravalib)

<details><summary>README extract</summary>

The stravalib Python package provides easy-to-use tools for accessing and
downloading Strava data from the Strava V3 API. Stravalib provides a `Client` class that supports:

- Authenticating with stravalib
- Managing your authentication to ensure it's current (if you have your environment setup) ...

Sections: Welcome to stravalib, Dependencies, Get started using Stravalib, Building from source, Pull Requests and tests, Still reading?

</details>

### cmweather

A library of useful colormaps when visualizing weather and climate data, with numerous color vision deficiency friendly options

`pip install cmweather` · installs (wheel) · licence: MIT License · rank 13073 · last release 2024-01-04 · [PyPI](https://pypi.org/project/cmweather/) · [docs](https://github.com/openradar/cmweather) · [source](https://github.com/openradar/cmweather)

<details><summary>README extract</summary>

The motivation for this package is to contain weather maps relevant to the weather and climate community. There are many colormaps that are unique to the weather/climate community that are not included in core libraries such as matplotlib. This is also meant to be a community collaboration, across multiple domain-specific packages (ex. ...

Sections: cmweather, Motivation

</details>

### hugr

Quantinuum's common representation for quantum programs

`pip install hugr` · installs (wheel) · licence: Apache Software License · rank 13090 · last release 2026-10-06 · [PyPI](https://pypi.org/project/hugr/) · [source](https://github.com/quantinuum/hugr/tree/main/hugr-py)

<details><summary>README extract</summary>

The Hierarchical Unified Graph Representation (HUGR, pronounced _hugger_) is the
common representation of quantum programs and operations in the Quantinuum
ecosystem.

This library provides a pure-python implementation of the HUGR data model, and
a low-level API for constructing HUGR objects.

The API documentation for this package is here. ...

</details>

### fortranformat

Mimics Fortran textual IO in Python.

`pip install fortranformat` · installs (wheel) · licence: MIT License · rank 13100 · last release 2025-04-08 · [PyPI](https://pypi.org/project/fortranformat/) · [source](https://github.com/brendanarnold/py-fortranformat)

### xradar

Xradar includes all the tools to get your weather radar into the xarray data model.

`pip install xradar` · installs (wheel) · licence: MIT · rank 13126 · last release 2026-10-21 · [PyPI](https://pypi.org/project/xradar/) · [docs](https://docs.openradarscience.org/projects/xradar/) · [source](https://github.com/openradar/xradar)

<details><summary>README extract</summary>

Xradar includes all the tools to get your weather radar into the xarray data model.

* Code: MIT license
* Documentation: CC-BY-SA-4.0

Sections: xradar, About, Features, Import/Export Capabilities, Import-Only Capabilities, Data Transformation and Alignment, 0.13.0 (2026-10-21), 0.12.0 (2026-04-21), 0.11.1 (2026-02-03), 0.11.0 (2026-01-12), 0.10.0 (2025-07-11), 0.9.0 (2025-02-07), 0.8.0 (2024-11-04), 0.7.0 (2024-10-26)

</details>

### pyranges

GenomicRanges for Python.

`pip install pyranges` · installs (wheel) · licence: MIT License · rank 13141 · last release 2026-10-26 · [PyPI](https://pypi.org/project/pyranges/)

<details><summary>README extract</summary>

This repo currently hosts the "version 0" of pyranges. A redesigned, faster version 1 is available at
Version 1 will soon replace version 0. We encourage existing v0 users to migrate to v1 (see guide at and new users to directly adopt v1. Read about v1 in our preprint at

Version 0.1.6 supports pandas 3 (pandas 1.5 and 2.x are still supported). ...

Features:
- fast
 - memory-efficient
 - featureful
 - pythonic/pandastic
 - supports chaining with a terse syntax
 - uses Pandas DataFrames, so the whole Python data science stack works on PyRanges

Sections: pyranges0, Deprecation note!, Recent changes, Introduction, Documentation, Features, Asking for help

</details>

### floret

floret Python bindings

`pip install floret` · installs from source (sdist only) · licence: MIT License · rank 13197 · last release 2023-11-04 · [PyPI](https://pypi.org/project/floret/)

<details><summary>README extract</summary>

floret is an extended version of fastText that can
produce word representations for any word from a compact vector table. It
combines:

- fastText's subwords to provide embeddings for any word
- Bloom embeddings ("hashing trick") for a compact vector table

Example:
```python
import floret

# train vectors
model = floret.train_unsupervised(
    "data.txt",
    model="cbow",
    mode="floret",
    hashCount=2,
    bucket=50000,
    minn=3,
    maxn=6,
)

# query vector
model.get_word_vector("broccoli")

# save full model
model.save_model("vectors.bin")

# export standard word-only vector table
...
```

Sections: Usage, Use floret vectors in spaCy, Notes

</details>

### pymatreader

Convenient reader for Matlab mat files

`pip install pymatreader` · installs (wheel) · licence: BSD License · rank 13217 · last release 2026-09-28 · [PyPI](https://pypi.org/project/pymatreader/)

<details><summary>README extract</summary>

A Python module to read Matlab files. This module works with both the old (< 7.3) and the new (>= 7.3) HDF5 based format. The output should be the same for both kinds of files.

Example:
```python
from pymatreader import read_mat

data = read_mat(filename)
```

Sections: pymatreader, How to use, Documentation, Code

</details>

### pyserq

serQ in Python: compile a program to its IR and run it, in process

`pip install pyserq` · installs (wheel) · licence: Apache-2.0 · rank 13221 · last release 2026-10-15 · [PyPI](https://pypi.org/project/pyserq/) · [docs](https://servingq.github.io/serQ/python/)

<details><summary>README extract</summary>

serQ in Python. serQ is a language in which an LLM serving deployment is a
program; pyserq compiles a program to its IR and runs it, in process, and
gives what the `serq` CLI gives. ...

Example:
```python
import pyserq
p = pyserq.compile("mg1.sq", workload="workloads/mg1.sq",
                   sets={"lam": 0.8}, seed=10, horizon=250000, warmup=25000)
r = pyserq.run(p)            # the GIL is released while it runs
r.json()                     # what `serq run --json` prints
o = r.client["response"]      # o.mean, o.ci, o.samples, o.times
...
```

</details>

### fparser

Python implementation of a Fortran parser

`pip install fparser` · installs (wheel) · licence: BSD-3-Clause · rank 13229 · last release 2026-09-01 · [PyPI](https://pypi.org/project/fparser/)

<details><summary>README extract</summary>

* 01/09/2026 Version 0.2.5 released (extensions for omitting a comma before/
 after character edit descriptors in a format specification and for using
 INQUIRY to test for directories) plus finalised support for all F2008
 intrinsic functions.
 * 26/06/2026 Version 0.2.4 released (bug fix for importing F2008 without
 F2003. ...

Sections: News, Introduction, Obtaining, Documentation, Code Metrics, See also

</details>

### daal4py

daal4py is a Convenient Python API to the Intel® oneAPI Data Analytics Library (oneDAL)

`pip install daal4py` · installs (wheel) · licence: Apache Software License · rank 13246 · last release 2024-09-17 · [PyPI](https://pypi.org/project/daal4py/) · [docs](https://intelpython.github.io/daal4py/) · [source](https://github.com/IntelPython/daal4py)

<details><summary>README extract</summary>

A simplified API to Intel(R) oneAPI Data Analytics Library that allows for fast usage of the framework suited for Data Scientists or Machine Learning users. Built to help provide an abstraction to Intel(R) oneAPI Data Analytics Library for either direct usage or integration into one's own framework. ...

Sections: 👀 Follow us on Medium, 🔗 Important links, 📦 PyPi channel, 📦 Anaconda Cloud: Conda-Forge channel, 📦 Anaconda Cloud: Intel channel, ⚠️ Scikit-learn patching

</details>

### swiglpk

swiglpk - Simple swig bindings for the GNU Linear Programming Kit

`pip install swiglpk` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 13286 · last release 2026-02-05 · [PyPI](https://pypi.org/project/swiglpk/)

_README extract left out: share-alike licence._

### nemo-gym

NeMo Gym is a library for building reinforcement learning environments

`pip install nemo-gym` · installs (wheel) · licence: Apache Software License · rank 13288 · last release 2026-10-12 · [PyPI](https://pypi.org/project/nemo-gym/)

<details><summary>README extract</summary>

Requirements • Quick Start • Environment Tutorials • Available Environments • Documentation & Resources • Community & Support • Citations

NeMo Gym is a library for evaluating and improving models and agents using environments. ...

Sections: NeMo Gym, 🎯 When to Use NeMo Gym, 🏆 What NeMo Gym Provides, 🌎 Ecosystem, 📣 News, 📋 Requirements, 🚀 Quick Start, Run Evaluation, Next Steps, 🧭 Environment Tutorials, 📦 Available Environments, 📖 Documentation & Resources, ⚠️ Notice and Disclaimer

</details>

### PeakUtils

Peak detection utilities for 1D data

`pip install PeakUtils` · installs (wheel) · licence: MIT License · rank 13304 · last release 2024-06-27 · [PyPI](https://pypi.org/project/PeakUtils/)

<details><summary>README extract</summary>

This package provides utilities related to the detection of peaks on 1D data.
Includes functions to estimate baselines, finding the indexes of peaks in the data
and performing Gaussian fitting or centroid computation to further increase the
resolution of the peak detection.

The documentation is available at .

</details>

### genpy

AST-based generation of Python source code

`pip install genpy` · installs from source (sdist only) · licence: MIT License · rank 13335 · last release 2022-08-15 · [PyPI](https://pypi.org/project/genpy/)

<details><summary>README extract</summary>

genpy offers a simple abstract syntax tree for Python to allow structured code
generation from Python.

Places on the web related to genpy:

* Python package index (download releases)
* Documentation (read how things work)
* Github (get latest source code, file bugs) ...

</details>

### nc-time-axis

Provides support for a cftime axis in matplotlib

`pip install nc-time-axis` · installs (wheel) · licence: BSD License · rank 13343 · last release 2022-04-20 · [PyPI](https://pypi.org/project/nc-time-axis/) · [source](https://github.com/SciTools/nc-time-axis)

### persista

library for persisting and caching data

`pip install persista` · installs (wheel) · licence: BSD-3-Clause · rank 13356 · last release 2026-07-31 · [PyPI](https://pypi.org/project/persista/) · [docs](https://durandtibo.github.io/persista/) · [source](https://github.com/durandtibo/persista)

<details><summary>README extract</summary>

Features:
`persista` is a lightweight Python library that provides simple, consistent building blocks for
persisting and caching data. It offers a uniform key-value store interface backed by multiple
storage engines (in-memory, SQLite, DuckDB, LMDB, Redis, ...

Example:
```python
>>> from persista.store import InMemoryStore
>>> with InMemoryStore() as store:
...     store.set("user:1", {"name": "Alice"})
...     store.get("user:1")
...
{'name': 'Alice'}
```

Sections: persista, Overview, Why persista?, Features, 🗄️ Key-Value Stores, ⏱️ TTL Caching, 🌐 HTTP Utilities, Using uv (recommended), Using pip, Requirements, API Stability

</details>

### lume-pyat

pyAT-specific implementation of LUMEModel classes for virtual accelerators

`pip install lume-pyat` · installs (wheel) · licence: Apache-2.0 · rank 13381 · last release 2026-09-17 · [PyPI](https://pypi.org/project/lume-pyat/) · [docs](https://github.com/als-apg/lume-pyat) · [source](https://github.com/als-apg/lume-pyat)

<details><summary>README extract</summary>

pyAT-specific implementation of LUME model
classes for virtual accelerators.

`lume-pyat` sits between lume-base
and pyAT. You build the lattice, 4D or 6D;
this package wraps it in a `PyATSimulator`, binds free-form variable names to
element attributes — or to the ring energy — in native pyAT units, and exposes
the result as a lume-base ...

Example:
```python
import at
import numpy as np

from lume_pyat import (
    LUMEPyATModel,
    PyATReadOnlyScalarVariable,
    PyATSimulator,
    PyATWritableScalarVariable,
)

# 1. Build a lattice. lume-pyat never builds one for you -- this is a small
# FODO ring, but any 4D-canonical at.Lattice works.
N_CELLS = 8
elements = []
for cell in range(1, N_CELLS + 1):
...
```

...

</details>

### tensorly

Tensor learning in Python.

`pip install tensorly` · installs (wheel) · licence: BSD-3-Clause · rank 13414 · last release 2026-10-05 · [PyPI](https://pypi.org/project/tensorly/)

<details><summary>README extract</summary>

TensorLy is a Python library that aims at making tensor learning simple and accessible. It allows to easily perform tensor decomposition, tensor learning and tensor algebra. Its backend system allows to seamlessly perform computation with NumPy, PyTorch, JAX, TensorFlow, CuPy or Paddle, and run methods at scale on CPU or GPU.

Example:
```python
import tensorly as tl
import numpy as np

tensor = tl.tensor(np.arange(24).reshape((3, 4, 2)), dtype=tl.float64)
unfolded = tl.unfold(tensor, mode=0)
tl.fold(unfolded, mode=0, shape=tensor.shape)
```

Sections: TensorLy, Quickstart, Creating tensors, Setting the backend, Tensor decomposition, Next steps, Running the tests, Citing

</details>

### flwr

Flower: A Friendly Federated AI Framework

`pip install flwr` · installs (wheel) · licence: Apache-2.0 · rank 13422 · last release 2026-11-04 · [PyPI](https://pypi.org/project/flwr/) · [docs](https://flower.ai) · [source](https://github.com/flwrlabs/flower)

<details><summary>README extract</summary>

Website |
 Blog |
 Docs |
 Slack

Flower (`flwr`) is a framework for building federated AI systems. The
design of Flower is based on a few guiding principles:

- Customizable: Federated learning systems vary wildly from one use case to
 another. ...

Sections: Flower: A Friendly Federated AI Framework, Federated Learning Tutorial, Documentation, Flower Baselines, Flower Usage Examples

</details>

### roboto-mcap-codec

Decodes one channel of an MCAP file (ROS, DDS/IDL, JSON or MessagePack messages) into Apache Arrow, and single messages into Python objects.

`pip install roboto-mcap-codec` · installs (wheel) · licence: MPL-2.0 · rank 13432 · last release 2026-11-06 · [PyPI](https://pypi.org/project/roboto-mcap-codec/)

<details><summary>README extract</summary>

Decodes one channel of an MCAP file into Apache Arrow, and single messages into
Python objects. `open_mcap_file` reads the file through a byte-range reader you
supply: its footer and summary, then only the chunks that hold the channel's
messages within the requested row range and, for a window on log time, overlap
that window. ...

Example:
```python
import os

import mcap_codec

path = "recording.mcap"
with open(path, "rb") as file:

    # Called for each byte range the cursor reads; return exactly `length` bytes.
    def read_bytes(offset: int, length: int) -> bytes:
        file.seek(offset)
        return file.read(length)

    with mcap_codec.open_mcap_file(
        read_bytes,
...
```

Sections: roboto-mcap-codec, Quick start, Decoding single messages, Changes from 0.1

</details>

### gwdatafind

The GWDataFind data discovery client

`pip install gwdatafind` · installs (wheel) · licence: MIT License · rank 13456 · last release 2025-10-31 · [PyPI](https://pypi.org/project/gwdatafind/) · [docs](https://gwdatafind.readthedocs.io) · [source](https://git.ligo.org/gwdatafind/gwdatafind.git)

<details><summary>README extract</summary>

The GWDataFind data discovery client.

The GWDataFind service allows users to query for the location of
Gravitational-Wave Frame (GWF) files containing data from the current
gravitational-wave detectors.

Example:
```python
>>> from gwdatafind import find_urls
>>> find_urls('H', 'H1_R', 1198800018, 1198800618)
```

Sections: GWDataFind, Basic Usage

</details>

### meshioplusplus

meshio++: I/O for many mesh formats (C++20 core + Python bindings)

`pip install meshioplusplus` · installs (wheel) · licence: MIT AND MPL-2.0 · rank 13464 · last release 2026-11-07 · [PyPI](https://pypi.org/project/meshioplusplus/) · [source](https://github.com/loumalouomega/meshioplusplus)

<details><summary>README extract</summary>

I/O for mesh files.

[][c++standard]

There are various mesh formats available for representing unstructured meshes. meshio++ can read and write all of the following and smoothly converts between them: ...

Example:
```python
import meshioplusplus

mesh = meshioplusplus.read(
    filename,  # string, os.PathLike, or a buffer/open file
    # file_format="stl",  # optional if filename is a path; inferred from extension
    # see meshioplusplus convert --help for all possible formats
)
# mesh.points, mesh.cells, mesh.cells_dict, ...

# mesh.vtk.read() is also possible
```

...

</details>

### ragged

Ragged array library, complying with Python API specification.

`pip install ragged` · installs (wheel) · licence: BSD License · rank 13470 · last release 2026-06-03 · [PyPI](https://pypi.org/project/ragged/)

<details><summary>README extract</summary>

[][actions-link]
[][pypi-link]
[][pypi-link]
[][github-discussions-link]

Ragged is a library for manipulating ragged arrays as though they were
NumPy or CuPy arrays, following the
Array API specification.

For example, this is a
ragged/jagged array:

The values are all floating-point numbers, so `a.dtype` is `float64`, ...

Example:
```python
>>> import ragged
>>> a = ragged.array([[[1.1, 2.2, 3.3], []], [[4.4]], [], [[5.5, 6.6, 7.7, 8.8], [9.9]]])
>>> a
ragged.array([
    [[1.1, 2.2, 3.3], []],
    [[4.4]],
    [],
    [[5.5, 6.6, 7.7, 8.8], [9.9]]
])
```

Sections: Introduction, Implementation

</details>

### pyfqmr

cython wrapper around C++ library for fast triangular mesh reduction

`pip install pyfqmr` · installs (wheel) · licence: MIT License · rank 13471 · last release 2025-08-23 · [PyPI](https://pypi.org/project/pyfqmr/)

<details><summary>README extract</summary>

Cython wrapper around sp4acerat's quadrics mesh reduction
algorithm.

- *Numpy*
- *Cython* (only for compilation, but not needed if installed from PyPI)

Example:
```python
>>> # We assume you have a numpy based mesh processing software
>>> # Where you can get the vertices and faces of the mesh as numpy arrays.
>>> # For example Trimesh or meshio
>>> import pyfqmr
>>> import trimesh as tr
>>> bunny = tr.load_mesh('example/Stanford_Bunny_sample.stl')
>>> # Simplify object
>>> mesh_simplifier = pyfqmr.Simplify()
...
```

Sections: pyfqmr : Python Fast Quadric Mesh Reduction, Requirements, Compilation, Usage, Controlling the reduction algorithm, Controlling the lossless reduction algorithm, Note, More information is to be found on Sp4cerat's repository

</details>

### openpmd-beamphysics

Tools for analyzing and viewing particle data in the openPMD standard, extension beamphysics.

`pip install openpmd-beamphysics` · installs (wheel) · licence: not stated · rank 13511 · last release 2026-10-28 · [PyPI](https://pypi.org/project/openpmd-beamphysics/)

<details><summary>README extract</summary>

| `Documentation` |

| |

Tools for analyzing and viewing particle data in the openPMD standard, extension beamphysics.

</details>

### xtgeo

XTGeo is a Python library for 3D grids, surfaces, wells, etc

`pip install xtgeo` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 13530 · last release 2026-10-14 · [PyPI](https://pypi.org/project/xtgeo/) · [docs](https://xtgeo.readthedocs.io) · [source](https://github.com/equinor/xtgeo)

_README extract left out: share-alike licence._

### nmrglue

A module for working with NMR data in Python

`pip install nmrglue` · installs (wheel) · licence: BSD License · rank 13545 · last release 2026-08-16 · [PyPI](https://pypi.org/project/nmrglue/)

<details><summary>README extract</summary>

nmrglue is a module for working with NMR data in Python. When used with the
numpy, scipy, and matplotlib packages nmrglue provides a robust interpreted
environment for processing, analyzing, and inspecting NMR data.

Sections: nmrglue, What is nmrglue?, Important Links, What can nmrglue do?, Citing nmrglue

</details>

### qiskit-connector

Quantum Computing Qiskit Connector For Quantum Backend Use In Realtime

`pip install qiskit-connector` · installs (wheel) · licence: Apache Software License · rank 13583 · last release 2026-01-07 · [PyPI](https://pypi.org/project/qiskit-connector/) · [source](https://github.com/schijioke-uche/pypi-qiskit-connector)

<details><summary>README extract</summary>

🖥️ Qiskit Connector® - Seamless Real-Time Connector for IBM Quantum Computing QPU

Qiskit Connector® is quantum computing open-source SDK extension. The Qiskit Connector® transforms how quantum developers connect to IBM Quantum backends by automating every step of the authentication, plan detection, and backend selection process. ...

Example:
```python
from qiskit_connector import QConnectorV2 as connector
from qiskit_connector import QPlanV2 as plan
```

Sections: Quantum Computing Qiskit Connector, 📋 Built-in classes & functions, 🗂️ Variable Setup, 👤 Usage - With Qiskit 2.x Code Sample, 📦 For Open or Paid Plans, Output Sample, 📜 Rights

</details>

### aisimulate

AISimulate: GPU-free inference simulation and deployment configuration

`pip install aisimulate` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 13600 · last release 2026-10-21 · [PyPI](https://pypi.org/project/aisimulate/) · [source](https://github.com/ai-dynamo/aisimulate)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

AISimulate predicts LLM serving behavior and searches for deployment
configurations offline, without bringing up a GPU serving cluster. ...

Sections: AISimulate, Predict one deployment, Search for a deployment, Documentation and coverage, Legacy CLI compatibility

</details>

### tensorflow-gpu

Removed: please install "tensorflow" instead.

`pip install tensorflow-gpu` · installs from source (sdist only) · licence: Apache Software License · rank 13637 · last release 2023-01-24 · [PyPI](https://pypi.org/project/tensorflow-gpu/)

<details><summary>README extract</summary>

tensorflow-gpu has been removed. Please install tensorflow instead.
The tensorflow package supports GPU accelerated operations via Nvidia CUDA.

tensorflow and tensorflow-gpu have been the same package since TensorFlow
2.1, released in September 2019. ...

Sections: Removal Information, About this package

</details>

### hankel

Hankel Transformations using method of Ogata 2005

`pip install hankel` · installs (wheel) · licence: MIT License · rank 13652 · last release 2023-07-27 · [PyPI](https://pypi.org/project/hankel/) · [docs](https://hankel.readthedocs.io) · [source](https://github.com/steven-murray/hankel)

<details><summary>README extract</summary>

Perform simple and accurate Hankel transformations using the method of
Ogata 2005.

Hankel transforms and integrals are commonplace in any area in which
Fourier Transforms are required over fields that
are radially symmetric (see
Wikipedia for a
thorough description). ...

Features:
- Accurate and fast solutions to many Hankel integrals
- Easy to use and re-use
- Arbitrary order transforms
- Built-in support for radially symmetric Fourier Transforms
- Thoroughly tested.
- only Python 3 compatible.

Sections: hankel, Features, Quick links, References

</details>

### ncls

A fast interval tree-like implementation in C, wrapped for the Python ecosystem.

`pip install ncls` · installs from source (sdist only) · licence: MIT License · rank 13674 · last release 2026-10-26 · [PyPI](https://pypi.org/project/ncls/)

<details><summary>README extract</summary>

While I'll continue maintaining this library I suggest you change to ruranges which is a more lightweight and faster library with many more operations than NCLS.

The Nested Containment List is a datastructure for interval overlap queries,
like the interval tree. ...

Example:
```python
from ncls import NCLS

import pandas as pd

starts = pd.Series(range(0, 5))
ends = starts + 100
ids = starts

subject_df = pd.DataFrame({"Start": starts, "End": ends}, index=ids)

print(subject_df)
# Start  End
# 0      0  100
# 1      1  101
# 2      2  102
# 3      3  103
# 4      4  104

ncls = NCLS(starts.values, ends.values, ids.values)

...
```

Sections: Nested containment list, Deprecation notice, NCLS, Usage, Benchmark, Original paper

</details>

### repo2rocrate

Generate RO-Crates from workflow repositories

`pip install repo2rocrate` · installs (wheel) · licence: Apache Software License · rank 13677 · last release 2023-05-03 · [PyPI](https://pypi.org/project/repo2rocrate/)

<details><summary>README extract</summary>

Generate a Workflow Testing RO-Crate from a "best-practices" workflow repository. In this context, "best-practices" means the set of guidelines, especially regarding repository structure and metadata, put together by the workflow language community. ...

Sections: repo2rocrate, Usage

</details>

### azureml-fsspec

Access datastore uri with fsspec

`pip install azureml-fsspec` · does not install on CPython 3.14 · licence: Other/Proprietary License · rank 13725 · last release 2026-07-31 · [PyPI](https://pypi.org/project/azureml-fsspec/)

<details><summary>README extract</summary>

Features:
- added support for python 3.12 and 3.13

Example:
```python
# load parquet file to pandas
import pandas
df = pandas.read_parquet('azureml://subscriptions/{sub_id}/resourcegroups/{rs_group}/workspaces/{ws}
                          /datastores/workspaceblobstore/paths/myfolder/mydata.parquet')

# load csv file to pandas
import pandas
...
```

Sections: Filesystem interface to Azure Machine Learning defined URIs, Getting started, Examples, 1.4.0 (04-16-2026), Features Added, Bugs Fixed, 1.3.1 (02-05-2024), 1.3.0 (01-17-2024), 1.2.0 (08-14-2023), 1.1.0 (06-01-2023)

</details>

### pya2ldb

A2L for Python

`pip install pya2ldb` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 13729 · last release 2026-10-16 · [PyPI](https://pypi.org/project/pya2ldb/)

_README extract left out: share-alike licence._

### docculus

Library for LangChain documents

`pip install docculus` · installs (wheel) · licence: BSD-3-Clause · rank 13731 · last release 2026-08-01 · [PyPI](https://pypi.org/project/docculus/) · [docs](https://durandtibo.github.io/docculus/) · [source](https://github.com/durandtibo/docculus)

<details><summary>README extract</summary>

Features:
`docculus` is a lightweight Python library that makes it easy to analyze, transform, hash, and
validate
`langchain_core.documents.Document`
objects.

Quick Links:

- Documentation
- Installation
- Features
- Contributing
- License

Example:
```python
>>> from langchain_core.documents import Document
>>> from docculus.transform import deduplicate_documents, format_documents
>>> docs = [
...     Document(id="1", page_content="The cat sat on the mat."),
...     Document(id="2", page_content="The cat sat on the mat."),
...     Document(id="3", page_content="The dog chased the ball."),
... ]
...
```

...

</details>

### gstools

GSTools: A geostatistical toolbox.

`pip install gstools` · installs (wheel) · licence: LGPL-3.0 · rank 13735 · last release 2025-04-28 · [PyPI](https://pypi.org/project/gstools/) · [docs](https://gstools.readthedocs.io) · [source](https://github.com/GeoStat-Framework/GSTools)

_README extract left out: share-alike licence._

### dlib-bin

A toolkit for making real world machine learning and data analysis applications

`pip install dlib-bin` · installs (wheel) · licence: Boost Software License · rank 13752 · last release 2026-10-02 · [PyPI](https://pypi.org/project/dlib-bin/)

### ggplot

ggplot for python

`pip install ggplot` · installs (wheel) · licence: BSD · rank 13753 · last release 2016-09-29 · [PyPI](https://pypi.org/project/ggplot/)

<details><summary>README extract</summary>

`ggplot` is a Python implementation of the grammar of graphics. It is
not intended to be a feature-for-feature port of
ggplot(diamonds, aes(x='price', color='clarity')) + \
 geom_density() + \
 scale_color_brewer(type='div', palette=7) + \
 facet_wrap('cut')
$ pip install -U ggplot

Sections: ggplot, What is it?, or

</details>

### trollimage

Pytroll imaging library

`pip install trollimage` · installs (wheel) · licence: Apache-2.0 · rank 13760 · last release 2026-10-13 · [PyPI](https://pypi.org/project/trollimage/)

<details><summary>README extract</summary>

Imaging package for pytroll packages like
SatPy.

</details>

### executorch

On-device AI across mobile, embedded and edge for PyTorch

`pip install executorch` · installs (wheel) · licence: BSD-3-Clause · rank 13802 · last release 2026-11-04 · [PyPI](https://pypi.org/project/executorch/) · [source](https://github.com/pytorch/executorch)

<details><summary>README extract</summary>

ExecuTorch is a PyTorch platform that provides
infrastructure to run PyTorch programs everywhere from AR/VR wearables to
standard on-device iOS and Android mobile deployments. One of the main goals for
ExecuTorch is to enable wider customization and deployment capabilities of the
PyTorch programs. ...

</details>

### pybids

bids: interface with datasets conforming to BIDS

`pip install pybids` · installs (wheel) · licence: MIT License · rank 13833 · last release 2026-03-12 · [PyPI](https://pypi.org/project/pybids/)

<details><summary>README extract</summary>

PyBIDS is a Python library to centralize interactions with datasets conforming
BIDS (Brain Imaging Data Structure) format. For more information about BIDS
visit

PyBIDS currently supports Python 3 on POSIX operating systems (including Mac OS). Windows is not officially supported, though most PyBIDS functionality will probably work fine.

Sections: PyBIDS, Dependencies, Usage

</details>

### pypemicro

Python tool to control PEMicro Debug probes

`pip install pypemicro` · installs (wheel) · licence: BSD License · rank 13866 · last release 2023-02-23 · [PyPI](https://pypi.org/project/pypemicro/)

### tket-exts

Python interface for hugr extensions offered by tket

`pip install tket-exts` · installs (wheel) · licence: Apache Software License · rank 13872 · last release 2026-09-30 · [PyPI](https://pypi.org/project/tket-exts/) · [source](https://github.com/quantinuum/tket2/tree/main/tket/tket-exts)

<details><summary>README extract</summary>

[](
[](
[](

This is an auxiliary Python package containing HUGR extension definitions for `tket`
operations and types.

This package is intended to be used as an internal dependency for `tket`.
See < for the main package.

</details>

### ai-dynamo

Distributed Inference Framework

`pip install ai-dynamo` · installs (wheel) · licence: Apache Software License · rank 13878 · last release 2026-11-05 · [PyPI](https://pypi.org/project/ai-dynamo/) · [source](https://github.com/ai-dynamo/dynamo.git)

<details><summary>README extract</summary>

| Docs | Roadmap | Recipes | Examples | Containers | Digest | Design Proposals | How to Contribute | Slack |

The open-source, datacenter-scale inference stack. Dynamo is the orchestration layer above inference engines — it doesn't replace SGLang, TensorRT-LLM, or vLLM, it turns them into a coordinated multi-node inference system. ...

Sections: Dynamo, When to use Dynamo, Key Results, What Dynamo Does, Core Capabilities, New in 1.0, Request Routing Topologies, Quick Start, Option A: Container (fastest), vLLM, SGLang, Option C: Kubernetes (recommended)

</details>

### bluesky-tiled-plugins

Integrations for using Tiled with Bluesky

`pip install bluesky-tiled-plugins` · installs (wheel) · licence: BSD-3-Clause · rank 13888 · last release 2026-11-02 · [PyPI](https://pypi.org/project/bluesky-tiled-plugins/)

<details><summary>README extract</summary>

[][actions-link]

[][pypi-link]
[][conda-link]
[][pypi-link]

<!-- SPHINX-START -->

<!-- prettier-ignore-start -->

<!-- prettier-ignore-end -->

<!-- README only content. Anything below this line won't be included in index.md -->

See for more detailed
documentation.

</details>

### bids-validator

Validator for the Brain Imaging Data Structure

`pip install bids-validator` · installs (wheel) · licence: MIT License · rank 13893 · last release 2024-08-06 · [PyPI](https://pypi.org/project/bids-validator/)

<details><summary>README extract</summary>

- BIDS-Validator
 - Quickstart
 - Support
 - Maintainers and Contributors
 - Use
 - API
 - .bidsignore
 - Configuration
 - In the Browser
 - On the Server
 - Through Command Line
 - Docker image
 - Python Library
 - Example
 - Development
 - Running Locally in a Browser
 - Testing
 - Publishing
 - Acknowledgments

Example:
```python
from bids_validator import BIDSValidator
validator = BIDSValidator()
filepaths = ["/sub-01/anat/sub-01_rec-CSD_T1w.nii.gz", "/sub-01/anat/sub-01_acq-23_rec-CSD_T1w.exe"]
for filepath in filepaths:
    print(validator.is_bids(filepath))  # will print True, and then False
```

...

</details>

### spacy-lookups-data

Additional lookup tables and data resources for spaCy

`pip install spacy-lookups-data` · installs (wheel) · licence: MIT License · rank 13919 · last release 2023-07-28 · [PyPI](https://pypi.org/project/spacy-lookups-data/)

<details><summary>README extract</summary>

This repository contains additional data files to be used with
spaCy v2.2+. When it's installed in the same environment as
spaCy, this package makes the resources for each language available as an entry
point, which spaCy checks when setting up the `Vocab` and `Lookups`.

Feel free to submit pull requests to update the data. ...

Features:
The main purpose of this package is to make the default spaCy installation
smaller and not force every user to download large data files for _all_
languages by default. ...

Sections: spaCy lookups data, FAQ, Why does this exist?, Is this package only for lemmatization?, Running tests, Bug reports and other issues

</details>

### dtwalign

Comprehensive DTW package which enables partial mathing and has various constraint options

`pip install dtwalign` · installs (wheel) · licence: MIT · rank 13962 · last release 2022-12-30 · [PyPI](https://pypi.org/project/dtwalign/)

<details><summary>README extract</summary>

Comprehensive dynamic time warping module for python.

Features:
* Fast computation by Numba
* Local constraint (step pattern)
* Global constraint (windowing)
* Alignment path visualization

Sections: DTW (Dynamic Time Warping), Features, Reference

</details>

### pyocd-pemicro

PyOCD debug probe plugin for PEMicro debug probes

`pip install pyocd-pemicro` · installs (wheel) · licence: BSD License · rank 13970 · last release 2023-02-23 · [PyPI](https://pypi.org/project/pyocd-pemicro/) · [docs](https://pyocd.io/docs)

### lytekit

Latch fork of Flyte SDK for Python

`pip install lytekit` · installs (wheel) · licence: Apache Software License · rank 13979 · last release 2026-06-30 · [PyPI](https://pypi.org/project/lytekit/)

<details><summary>README extract</summary>

Flytekit Python is the Python SDK built on top of Flyte

 Contribution Guide

Flytekit Python is the Python Library for easily authoring, testing, deploying, and interacting with Flyte tasks, workflows, and launch plans.

If you haven't explored Flyte yet, please refer to:
 - Flyte homepage
 - Flyte core repository

Example:
```python
from flytekit import task, workflow

@task(cache=True, cache_version="1", retries=3)
def sum(x: int, y: int) -> int:
    return x + y

@task(cache=True, cache_version="1", retries=3)
def square(z: int) -> int:
    return z*z

@workflow
def my_workflow(x: int, y: int) -> int:
    return sum(x=square(z=x), y=square(z=y))
```

Sections: Flytekit Python, Plugins, 🚀 Quick Start, A Simple Example, 📦 Resources, Code Structure, 🐞 File an Issue, 🔌 Flytekit Plugins

</details>

### SeismoStats

A Python Package for Statistical Seismology.

`pip install SeismoStats` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 13982 · last release 2025-12-11 · [PyPI](https://pypi.org/project/SeismoStats/) · [docs](https://seismostats.readthedocs.io/) · [source](https://github.com/swiss-seismological-service/SeismoStats)

_README extract left out: share-alike licence._

### scipp

Multi-dimensional data arrays with labeled dimensions

`pip install scipp` · installs (wheel) · licence: BSD-3-Clause · rank 14000 · last release 2026-09-22 · [PyPI](https://pypi.org/project/scipp/) · [docs](https://scipp.github.io/) · [source](https://github.com/scipp/scipp)

<details><summary>README extract</summary>

See for project context and how to use and install the scipp Python module.

Bug reports or feature requests should be submitted by opening an issue.
For general discussions, or questions about how to achieve something with Scipp, start a new discussion.

Sections: Scipp, Links

</details>

### interpax

Interpolation and function approximation with JAX

`pip install interpax` · installs (wheel) · licence: MIT · rank 14040 · last release 2026-10-22 · [PyPI](https://pypi.org/project/interpax/) · [docs](https://interpax.readthedocs.io/) · [source](https://github.com/f0uriest/interpax/)

<details><summary>README extract</summary>

interpax is a library for interpolation and function approximation using JAX.

Includes methods for nearest neighbor, linear, and several cubic interpolation schemes
in 1d, 2d, and 3d, as well as Fourier interpolation for periodic functions in
1d and 2d. Also includes a scipy-like RBFInterpolator and smoothing splines for noisy data. ...

Example:
```python
import jax.numpy as jnp
import numpy as np
from interpax import interp1d

xp = jnp.linspace(0, 2 * np.pi, 100)
xq = jnp.linspace(0, 2 * np.pi, 10000)
f = lambda x: jnp.sin(x)
fp = f(xp)

fq = interp1d(xq, xp, fp, method="cubic")
np.testing.assert_allclose(fq, f(xq), rtol=1e-6, atol=1e-5)
```

Sections: interpax, Usage

</details>

### SMACT

Semiconducting Materials by Analogy and Chemical Theory

`pip install SMACT` · does not install on CPython 3.14 · licence: MIT · rank 14041 · last release 2026-09-24 · [PyPI](https://pypi.org/project/SMACT/) · [docs](https://smact.readthedocs.io/en/latest/) · [source](https://github.com/WMD-group/SMACT)

<details><summary>README extract</summary>

Semiconducting Materials by Analogy and Chemical Theory (SMACT) is a collection of rapid screening and informatics tools that uses data about chemical elements.

- Documentation: <
- Examples: <

_If you torture the data enough, nature will always confess - Roland Coase (from 'How should economists choose?') ...

Sections: SMACT, Statement of need, Getting started, Code features, Package structure, List of modules, Requirements, Bugs, features and questions, Tests, References

</details>

### inference-sdk

With no prior knowledge of machine learning or device-specific deployment, you can deploy a computer vision model to a range of devices and environments using Roboflow Inference.

`pip install inference-sdk` · does not install on CPython 3.14 · licence: Apache Software License · rank 14044 · last release 2026-10-30 · [PyPI](https://pypi.org/project/inference-sdk/)

<details><summary>README extract</summary>

notebooks | supervision | autodistill | maestro

Inference turns any computer or edge device into a command center for your computer vision projects.

* 🛠️ Self-host your own fine-tuned models
* 🧠 Access the latest and greatest foundation models (like Florence-2, CLIP, and SAM2)
* 🤝 Use Workflows to track, count, time, measure, and visualize
* 👁️ ...

Example:
```python
from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url=" # use local inference server
    # api_key="" # optional to access your private data and models
)

result = client.run_workflow(
    workspace_name="roboflow-docs",
    workflow_id="model-comparison",
    images={
        "image": "
    },
    parameters={
...
```

...

</details>

### kditransform

Kernel density integral transformation

`pip install kditransform` · installs (wheel) · licence: OSI Approved · rank 14061 · last release 2025-10-23 · [PyPI](https://pypi.org/project/kditransform/)

<details><summary>README extract</summary>

The kernel-density integral transformation (McCarter, 2023, TMLR), like min-max scaling and quantile transformation, maps continuous features to the range `[0, 1]`.
It achieves a happy balance between these two transforms, preserving the shape of the input distribution like min-max scaling, while nonlinearly attenuating the effect of outliers like ...

Example:
```python
import numpy as np
from kditransform import KDITransformer
X = np.random.uniform(size=(500, 1))
kdt = KDITransformer(alpha=1.)
Y = kdt.fit_transform(X)
```

Sections: kditransform, Usage, Citing this method, Usage with TabPFN

</details>

### opensearch-py-ml

Python Client and Toolkit for DataFrames, Big Data, Machine Learning and ETL in OpenSearch

`pip install opensearch-py-ml` · installs (wheel) · licence: Apache Software License · rank 14066 · last release 2025-09-16 · [PyPI](https://pypi.org/project/opensearch-py-ml/) · [source](https://github.com/opensearch-project/opensearch-py-ml)

<details><summary>README extract</summary>

OpenSearch-py-ml

- Welcome!
- Getting Started
- Compatibility with OpenSearch
- Project Resources
- Code of Conduct
- License
- Copyright

opensearch-py-ml is a Python client that provides a suite of data analytics and machine learning tools for OpenSearch. ...

Sections: Welcome!, Copyright

</details>

### konlpy

Python package for Korean natural language processing.

`pip install konlpy` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 14075 · last release 2022-01-02 · [PyPI](https://pypi.org/project/konlpy/)

_README extract left out: share-alike licence._

### scikit-fmm

An extension module implementing the fast marching method

`pip install scikit-fmm` · installs from source (sdist only) · licence: BSD License · rank 14109 · last release 2025-06-23 · [PyPI](https://pypi.org/project/scikit-fmm/)

<details><summary>README extract</summary>

`scikit-fmm` is a Python extension module which implements the fast marching method.
The fast marching method is used to model the evolution of boundaries
and interfaces in a variety of application areas. ...

Example:
```python
import skfmm
import numpy as np
phi = np.ones((3, 3))
phi[1, 1] = -1
skfmm.distance(phi)
```

Sections: scikit-fmm: the fast marching method for Python, Documentation, PyPI, Requirements, Running Tests, Building documentation, Publications using scikit-fmm

</details>

### dimos-viewer

Interactive Rerun viewer for DimOS with click-to-navigate support

`pip install dimos-viewer` · installs (wheel) · licence: Apache Software License; MIT License · rank 14128 · last release 2026-10-08 · [PyPI](https://pypi.org/project/dimos-viewer/) · [source](https://github.com/dimensionalOS/dimos-viewer)

<details><summary>README extract</summary>

Advanced example showing how to control an external application from the Rerun viewer, by extending the viewer UI.

> [!NOTE]
> #2337: In order to spawn a web viewer with these customizations applied, you have to build the web viewer of the version yourself. This is currently not supported outside of the Rerun repository.

Features:
This example is divided into two parts:

- Viewer (`src/viewer.rs`): Wraps the Rerun viewer inside an `eframe` app.
- App (`src/app.rs`): The application that uses the Rerun SDK. ...

Sections: Overview, Usage, Relationship with Viewer callbacks

</details>

### doroutes

Advanced Routing for GDSFactory

`pip install doroutes` · installs (wheel) · licence: Other/Proprietary License · rank 14140 · last release 2026-10-30 · [PyPI](https://pypi.org/project/doroutes/)

### gradio-pdf

Easily display PDFs in Gradio

`pip install gradio-pdf` · installs (wheel) · licence: Apache-2.0 · rank 14161 · last release 2025-11-26 · [PyPI](https://pypi.org/project/gradio-pdf/) · [source](https://github.com/freddyaboulton/gradio-pdf)

<details><summary>README extract</summary>

Easily display PDFs in Gradio

Example:
```python
import gradio as gr
from _app import demo as app
import os

...
```

Sections: `gradio_pdf`, Usage, `PDF`, Initialization, Events, User function

</details>

### cf-units

Units of measure as required by the Climate and Forecast (CF) metadata conventions

`pip install cf-units` · installs (wheel) · licence: BSD-3-Clause · rank 14172 · last release 2026-01-16 · [PyPI](https://pypi.org/project/cf-units/) · [docs](https://cf-units.readthedocs.io) · [source](https://github.com/SciTools/cf-units)

<details><summary>README extract</summary>

| | |

| ⚙️ CI | |
| 💬 Community | |
| 📖 Documentation | |
| 📈 Health | |
| ✨ Meta | |
| 📦 Package | |
| 🧰 Repo | |
| | |

Features:
Units of measure as required by the Climate and Forecast (CF) metadata
conventions.

Provision of a wrapper class to support Unidata/UCAR UDUNITS-2 library, and the
cftime calendar functionality.

Documentation can be found at <

Sections: cf-units, Overview, Example, Get in Touch

</details>

### CyRK

Runge-Kutta ODE Integrator Implemented in Cython and Numba.

`pip install CyRK` · installs (wheel) · licence: Apache-2.0 · rank 14189 · last release 2026-10-10 · [PyPI](https://pypi.org/project/CyRK/) · [docs](https://cyrk.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Documentation | GitHub

Runge-Kutta ODE Integrator Implemented in Cython and Numba

CyRK provides fast integration tools to solve systems of ODEs using an adaptive time stepping scheme. CyRK can accept differential equations that are written in pure Python, njited numba, or cython-based cdef. ...

Sections: CyRK, Overview, Additional Features, Limitations, Using CyRK, Citing CyRK, Projects using CyRK

</details>

### pydsdl

Cyphal DSDL processing frontend

`pip install pydsdl` · installs (wheel) · licence: MIT License · rank 14232 · last release 2026-07-28 · [PyPI](https://pypi.org/project/pydsdl/)

<details><summary>README extract</summary>

PyDSDL is a Cyphal DSDL compiler front-end implemented in Python.
It accepts a DSDL namespace at the input and produces a well-annotated abstract syntax tree (AST) at the output,
evaluating all constant expressions in the process.
All DSDL features defined in the Cyphal Specification are supported. ...

Example:
```python
import pydsdl
try:
    types = pydsdl.read_namespace(target_directory, lookup_directories)
except pydsdl.InvalidDefinitionError as ex:
    print(f'{ex.path}:{ex.line}: Invalid DSDL: {ex.text}', file=sys.stderr)
    exit(1)
else:
    for t in types:
        print(t)  # Process the type -- generate code, analyze, etc.
```

</details>

### gstools-cython

Cython backend for GSTools.

`pip install gstools-cython` · installs (wheel) · licence: LGPL-3.0-or-later · rank 14240 · last release 2025-12-26 · [PyPI](https://pypi.org/project/gstools-cython/) · [docs](https://gstools.readthedocs.io) · [source](https://github.com/GeoStat-Framework/GSTools-Cython)

_README extract left out: share-alike licence._

### lytekitplugins-pods

Flytekit plugin to support K8s Pod tasks

`pip install lytekitplugins-pods` · installs (wheel) · licence: Apache Software License · rank 14245 · last release 2025-02-20 · [PyPI](https://pypi.org/project/lytekitplugins-pods/)

### egobox

(no summary)

`pip install egobox` · installs (wheel) · licence: Apache Software License · rank 14271 · last release 2026-11-06 · [PyPI](https://pypi.org/project/egobox/)

<details><summary>README extract</summary>

`egobox` package is the Python binding of the optimizer named `Egor` (and its multi-objective counterpart `Belfegor`) and the surrogate model `Gpx`, mixture of Gaussian processes, from the EGObox libraries written in Rust.

Example:
```python
import numpy as np
import egobox as egx

# Objective function
def f_obj(x: np.ndarray) -> np.ndarray:
    return (x - 3.5) * np.sin((x - 3.5) / (np.pi))

# Minimize f_opt in [0, 25]
optim = egx.Egor([[0.0, 25.0]]).minimize(f_obj, max_iters=20, seed=42)
print(
    f"Optimization f={optim.result.y_opt} at {optim.result.x_opt}"
...
```

Sections: EGObox - Efficient Global Optimization toolbox, Egor optimizer, Belfegor multi-objective optimizer (experimental), Gpx surrogate model

</details>

### pystempel

Polish stemmer.

`pip install pystempel` · installs (wheel) · licence: Other/Proprietary License · rank 14285 · last release 2024-07-10 · [PyPI](https://pypi.org/project/pystempel/)

<details><summary>README extract</summary>

Python port of Stempel, an algorithmic stemmer for the Polish language, originally written in Java.

The original stemmer has been implemented as part of Egothor Project, taken virtually unchanged to
Stempel Stemmer Java library by Andrzej Białecki and next included as part of Apache Lucene,
a free and open-source search engine library. ...

Example:
```python
from pystempel import Stemmer
```

Sections: Stempel Stemmer, How to use, Choosing stemming table, Choosing between port and wrapper, Options, Licensing, Alternatives

</details>

### zhinst-comms

Zurich Instruments internal python bindings for Capnp

`pip install zhinst-comms` · installs (wheel) · licence: MIT License; Other/Proprietary License · rank 14290 · last release 2026-11-02 · [PyPI](https://pypi.org/project/zhinst-comms/)

<details><summary>README extract</summary>

The `zhinst-comms` package bundles the protocol stack required to talk to a
server (e.g. LabOne data server). It is not tailored to a specific server or protocol but aims to provide a generic API that can be customized to all needs.

> ⚠️ This package is not intended to be used directly..
> It is utilized in the `labone` package. ...

</details>

### trollsift

String parser/formatter

`pip install trollsift` · installs (wheel) · licence: Apache-2.0 · rank 14291 · last release 2026-10-13 · [PyPI](https://pypi.org/project/trollsift/)

<details><summary>README extract</summary>

Trollsift is a collection of modules that assist with formatting,
parsing and filtering satellite granule file names.

For documentation, see

</details>

### btclib-secp256k1

Simple python bindings to libsecp256k1

`pip install btclib-secp256k1` · installs (wheel) · licence: MIT · rank 14297 · last release 2026-11-01 · [PyPI](https://pypi.org/project/btclib-secp256k1/) · [docs](https://btclib-secp256k1.readthedocs.io) · [source](https://github.com/btclib-org/btclib-secp256k1)

<details><summary>README extract</summary>

<!-- The badges are what the reader decides with, in groups: what the
software is and whether it can be used, whether it works, and what the
OpenSSF makes of it.

Inside the second group the gates come first, in the order a commit meets
them, and the sentinels follow in the order section 10 of the organization
standard schedules them -- the badge ...

Example:
```python
>>> import hashlib
>>> from btclib_secp256k1 import dsa, keys, ssa, xonly

>>> # BIP340 test vector 1; yours comes from os.urandom or a wallet
>>> prvkey = 0xB7E151628AED2A6ABF7158809CF4F3C762E7160F38B4DA56A784D9045190CFEF
>>> pubkey = keys.pubkey_from_prvkey(prvkey)
>>> msg = hashlib.sha256(b"hello").digest()
```

...

</details>

### tskit

The tree sequence toolkit.

`pip install tskit` · installs (wheel) · licence: MIT · rank 14325 · last release 2026-10-30 · [PyPI](https://pypi.org/project/tskit/) · [docs](https://tskit.dev/tskit/docs/stable) · [source](https://github.com/tskit-dev/tskit/)

<details><summary>README extract</summary>

The tree sequence toolkit.

Tskit is a cross-platform library for the storage and analysis of large-scale
genetic genealogy and variation data.
Please see the documentation
for further details.

Tskit is highly portable, and provides a number of
installation options.

</details>

### PyKrige

Kriging Toolkit for Python.

`pip install PyKrige` · installs (wheel) · licence: BSD-3-Clause · rank 14344 · last release 2025-10-16 · [PyPI](https://pypi.org/project/PyKrige/) · [docs](https://pykrige.readthedocs.io) · [source](https://github.com/GeoStat-Framework/PyKrige)

<details><summary>README extract</summary>

Kriging Toolkit for Python.

The code supports 2D and 3D ordinary and universal kriging. Standard
variogram models (linear, power, spherical, gaussian, exponential) are
built in, but custom variogram models can also be used. ...

Sections: PyKrige, Purpose, Features, Kriging algorithms, Wrappers, Tools, Kriging Parameters Tuning, Regression Kriging, Classification Kriging

</details>

### nunavut

Generate code from DSDL using Jinja2 templates.

`pip install nunavut` · installs (wheel) · licence: MIT · rank 14351 · last release 2026-10-25 · [PyPI](https://pypi.org/project/nunavut/) · [source](https://github.com/OpenCyphal/nunavut)

<details><summary>README extract</summary>

+--------------------------------+-----------------------------------+
| nox build (main) ...

Sections: Nunavut: DSDL transpiler, Examples, Generate C headers using the command-line tool, Generate Python packages using the command-line tool, Use custom templates, More examples, Extras, Bundled third-party software, Documentation

</details>

### torchio

Tools for medical image processing with PyTorch

`pip install torchio` · installs (wheel) · licence: Apache-2.0 · rank 14375 · last release 2026-06-02 · [PyPI](https://pypi.org/project/torchio/) · [docs](https://docs.torchio.org) · [source](https://github.com/TorchIO-project/torchio)

<details><summary>README extract</summary>

> *Tools like TorchIO are a symptom of the maturation of medical AI research using deep learning techniques*.

Jack Clark, Policy Director
at OpenAI (link).

 Package


 Code

 Tutorials

 Community

 Original

 Random blur

 Random flip

 Random noise

 Random affine transformation

 Random elastic transformation

 Random bias field artifact ...

</details>

### properscoring

Proper scoring rules in Python

`pip install properscoring` · installs (wheel) · licence: Apache Software License · rank 14381 · last release 2015-11-12 · [PyPI](https://pypi.org/project/properscoring/)

<details><summary>README extract</summary>

Proper scoring rules for evaluating probabilistic forecasts in Python.
Evaluation methods that are "strictly proper" cannot be artificially improved
through hedging, which makes them fair methods for accessing the accuracy of
probabilistic forecasts. In particular, these rules are often used for
evaluating weather forecasts. ...

Example:
```python
import numpy as np
import properscoring as ps
from scipy.stats import norm
```

Sections: properscoring, Example: five ways to calculate CRPS, API

</details>

### cppcheck

Package cppcheck as a python wheel.

`pip install cppcheck` · installs (wheel) · licence: Apache Software License · rank 14407 · last release 2026-10-07 · [PyPI](https://pypi.org/project/cppcheck/)

<details><summary>README extract</summary>

<!-- SPHINX-START -->

Package cppcheck as a python wheel.

<!-- writes more things here -->

</details>

### earthkit-utils

Utilities for the Earthkit ecosystem

`pip install earthkit-utils` · installs (wheel) · licence: Apache-2.0 · rank 14415 · last release 2026-11-04 · [PyPI](https://pypi.org/project/earthkit-utils/) · [docs](https://earthkit-utils.readthedocs.io/) · [source](https://github.com/ecmwf/earthkit-utils/)

<details><summary>README extract</summary>

> [!IMPORTANT]
> This software is Graduated and subject to ECMWF's guidelines on Software Maturity.

Utilities for the earthkit ecosystem.

 Installation
 Documentation

</details>

### regionmask

create masks of geospatial regions for arbitrary grids

`pip install regionmask` · installs (wheel) · licence: MIT License · rank 14441 · last release 2024-12-03 · [PyPI](https://pypi.org/project/regionmask/)

<details><summary>README extract</summary>

When working with gridded data such as climate model output or reanalysis data it is
often important to create regional averages, e.g., over countries, continents or
regions defined in the literature. To do so we need to know for each grid point to which
region it belongs to.

regionmask is a python package that: ...

Sections: create *masks* of geospatial *regions* for arbitrary grids, Documentation, Get in touch

</details>

### lume-base

Base classes and architecture for LUME Python projects

`pip install lume-base` · installs (wheel) · licence: Apache-2.0 · rank 14461 · last release 2026-09-14 · [PyPI](https://pypi.org/project/lume-base/) · [docs](https://slaclab.github.io/lume-base) · [source](https://github.com/slaclab/lume-base)

<details><summary>README extract</summary>

Base classes and architecture for LUME Python projects

Sections: lume-base, Linting and Formatting, Building Documentation

</details>

### TotalSegmentator

Robust segmentation of 117 classes in CT images.

`pip install TotalSegmentator` · installs (wheel) · licence: Apache 2.0 · rank 14481 · last release 2026-08-12 · [PyPI](https://pypi.org/project/TotalSegmentator/)

### arm-pyart

Py-ART: Python ARM Radar Toolkit

`pip install arm-pyart` · installs (wheel) · licence: BSD-3-Clause · rank 14484 · last release 2026-09-17 · [PyPI](https://pypi.org/project/arm-pyart/)

<details><summary>README extract</summary>

a growing collection of weather radar algorithms and utilities build on top of
the Scientific Python stack and distributed under the 3-Clause BSD license.
Py-ART is used by the Atmospheric Radiation Measurement (ARM) User
Facility for working with data from a number of precipitation and cloud radars,
but has been designed so that it can be used by ...

</details>

### ert

Ensemble based Reservoir Tool (ERT)

`pip install ert` · installs (wheel) · licence: GPL-3.0-only · rank 14493 · last release 2026-11-06 · [PyPI](https://pypi.org/project/ert/) · [source](https://github.com/equinor/ert)

_README extract left out: share-alike licence._

### boxmot

BoxMOT: pluggable SOTA tracking modules for segmentation, object detection and pose estimation models

`pip install boxmot` · does not install on CPython 3.14 · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 14574 · last release 2026-10-27 · [PyPI](https://pypi.org/project/boxmot/)

_README extract left out: share-alike licence._

### u8darts

⚠️ DEPRECATED - Use 'darts' package instead. This legacy compatibility package redirects to 'darts'.

`pip install u8darts` · installs (wheel) · licence: Apache-2.0 · rank 14593 · last release 2026-02-10 · [PyPI](https://pypi.org/project/u8darts/) · [docs](https://unit8co.github.io/darts/) · [source](https://github.com/unit8co/darts)

<details><summary>README extract</summary>

⚠️⚠️⚠️ As of version `0.41.0`: The `u8darts` PyPI package is deprecated use `darts` instead ⚠️⚠️⚠️

- use `pip install "darts[option]>=0.41.0"` rather than `pip install "u8darts[option]"` (e.g. `pip install "darts[all]>=0.41.0"`) ...

Features:
* Forecasting Models: A large collection of forecasting models for regression as well as classification tasks; from statistical models (such as
 ARIMA) to deep learning models (such as N-BEATS). See the forecasting models below. ...

Example:
```python
import pandas as pd
from darts import TimeSeries

# Read a pandas DataFrame
df = pd.read_csv("AirPassengers.csv", delimiter=",")

# Create a TimeSeries, specifying the time and value columns
series = TimeSeries.from_dataframe(df, "Month", "#Passengers")

...

</details>

### satpy

Python package for earth-observing satellite data processing

`pip install satpy` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 14600 · last release 2026-03-04 · [PyPI](https://pypi.org/project/satpy/) · [docs](https://satpy.readthedocs.io/en/stable/) · [source](https://github.com/pytroll/satpy)

_README extract left out: share-alike licence._

### cutensor-cu13

NVIDIA cuTENSOR

`pip install cutensor-cu13` · installs (wheel) · licence: NVIDIA Proprietary Software · rank 14684 · last release 2026-09-21 · [PyPI](https://pypi.org/project/cutensor-cu13/)

<details><summary>README extract</summary>

cuTENSOR is a high-performance CUDA library for tensor primitives.

Features:
* FP64 inputs with FP32 compute.
 * FP32 inputs with FP16, BF16, or TF32 compute.
 * Complex-times-real operations.
 * Conjugate (without transpose) support.

* Support for up to 64-dimensional tensors.
* Arbitrary data layouts. ...

Sections: Key Features, Documentation

</details>

### medspacy-unqlite

Fast Python bindings for the UnQLite embedded NoSQL database.

`pip install medspacy-unqlite` · installs from source (sdist only) · licence: MIT License · rank 14697 · last release 2025-05-16 · [PyPI](https://pypi.org/project/medspacy-unqlite/) · [source](https://github.com/medspacy/medspacy-unqlite)

<details><summary>README extract</summary>

Fast Python bindings for UnQLite, a lightweight, embedded NoSQL database and JSON document store.

This is a forked version from coleifer/unqlite-python for better handling installation issues. ...

Features:
UnQLite features:

* Embedded, zero-conf database
* Transactional (ACID)
* Single file or in-memory database
* Key/value store
* Cursor support and linear record traversal
* JSON document store
* Thread-safe
* Terabyte-sized databases ...

Example:
```python
>>> from unqlite import UnQLite
>>> db = UnQLite()  # Create an in-memory database.
```

Sections: Please note, Features, Basic usage, Key/value features, Cursors, Document store features, Collections, Transactions

</details>

### crackle-codec

Crackle 3D dense segmentation compression codec.

`pip install crackle-codec` · installs (wheel) · licence: BSD-3-Clause · rank 14708 · last release 2026-11-06 · [PyPI](https://pypi.org/project/crackle-codec/)

<details><summary>README extract</summary>

*This repository is currently Beta. It works and the format is reasonably fixed. There may be some improvements down the line (such as 3d compression of crack codes, 2d chunking), but they will be a new format version number if necessary to retain backwards compatibility.*

Crackle is a compression codec for 3D dense segmentation (labeled) images. ...

Example:
```python
import pyarrow.parquet as pq
table = pq.read_table("myfile.ckl.meta.parquet")
print(table)
```

...

</details>

### libnvforest-cu12

nvForest

`pip install libnvforest-cu12` · installs (wheel) · licence: Apache-2.0 · rank 14714 · last release 2026-10-08 · [PyPI](https://pypi.org/project/libnvforest-cu12/)

<details><summary>README extract</summary>

nvForest is a highly-optimized and lightweight RAPIDS library that enables fast inference for decision tree models on NVIDIA GPUs and CPUs. It does not train models; it runs inference on models trained elsewhere (e.g., XGBoost, LightGBM, scikit-learn, or cuML).

nvForest uses Treelite as the common format for importing tree models. ...

Example:
```python
import nvforest

# Load XGBoost model for GPU inference
fm = nvforest.load_model("/path/to/xgboost_model.ubj", device="gpu",
                         model_type="xgboost_ubj")

# Run inference (X can be a NumPy array or CuPy array)
pred = fm.predict(X)
```

Sections: nvForest - Highly Optimized Decision Tree Inference, Inference Modes, Contact, Open GPU Data Science

</details>

### rapid-pe

RapidPE: The original low-latency gravitational wave parameter estimation code.

`pip install rapid-pe` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 14715 · last release 2023-10-25 · [PyPI](https://pypi.org/project/rapid-pe/) · [source](https://git.ligo.org/rapidpe-rift/rapidpe/)

_README extract left out: share-alike licence._

### qiskit-nature

Qiskit Nature: A library of quantum computing chemistry/physics experiments

`pip install qiskit-nature` · installs (wheel) · licence: Apache Software License · rank 14746 · last release 2026-06-01 · [PyPI](https://pypi.org/project/qiskit-nature/) · [docs](https://qiskit-community.github.io/qiskit-nature/) · [source](https://github.com/Qiskit/qiskit-nature)

<details><summary>README extract</summary>

Qiskit Nature is an open-source framework which supports solving quantum mechanical natural
science problems using quantum computing algorithms. This includes finding ground and excited
states of electronic and vibrational structure problems, measuring the dipole moments of molecular
systems, solving the Ising and Fermi-Hubbard models on lattices, ...

Sections: Qiskit Nature, Further examples

</details>

### sorted-nearest

Find nearest intervals.

`pip install sorted-nearest` · installs from source (sdist only) · licence: MIT License · rank 14747 · last release 2026-10-27 · [PyPI](https://pypi.org/project/sorted-nearest/)

### metatensor-core

Python bindings for metatensor

`pip install metatensor-core` · installs (wheel) · licence: BSD-3-Clause · rank 14771 · last release 2026-10-06 · [PyPI](https://pypi.org/project/metatensor-core/) · [docs](https://docs.metatensor.org/latest/) · [source](https://github.com/metatensor/metatensor)

<details><summary>README extract</summary>

This package contains the Python bindings to the core C API of metatensor. Most
users will want to use the `metatensor` meta package instead, which also
includes function to operate on the data.

</details>

### miss-hit-core

Code formatting and code metrics for programs written in the MATLAB/Simulink and Octave languages.

`pip install miss-hit-core` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 14796 · last release 2024-09-02 · [PyPI](https://pypi.org/project/miss-hit-core/) · [docs](https://florianschanda.github.io/miss_hit/) · [source](https://github.com/florianschanda/miss_hit)

_README extract left out: share-alike licence._

### scikit-surprise

An easy-to-use library for recommender systems.

`pip install scikit-surprise` · installs (wheel) · licence: BSD License · rank 14809 · last release 2026-05-30 · [PyPI](https://pypi.org/project/scikit-surprise/) · [source](https://github.com/NicolasHug/Surprise)

<details><summary>README extract</summary>

Overview

Surprise is a Python
scikit for building and analyzing
recommender systems that deal with explicit rating data.

Surprise **was designed with the
following purposes in mind**:

- Give users perfect control over their experiments. ...

Example:
```python
from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate

# Load the movielens-100k dataset (download it if needed).
data = Dataset.load_builtin('ml-100k')

# Use the famous SVD algorithm.
algo = SVD()

# Run 5-fold cross-validation and print results.
...
```

</details>

### dask-geopandas

Parallel GeoPandas with Dask

`pip install dask-geopandas` · installs (wheel) · licence: BSD License · rank 14817 · last release 2025-06-02 · [PyPI](https://pypi.org/project/dask-geopandas/) · [docs](https://dask-geopandas.readthedocs.io/) · [source](https://github.com/geopandas/dask-geopandas)

<details><summary>README extract</summary>

Parallel GeoPandas with Dask

Dask-GeoPandas is a project merging the geospatial capabilities of GeoPandas
and scalability of Dask. GeoPandas is an open source project designed to make working with geospatial data in Python easier. GeoPandas extends the datatypes used by pandas to allow spatial operations on geometric types. ...

Example:
```python
import geopandas
df = geopandas.read_file('...')
```

Sections: dask-geopandas, Documentation, Example

</details>

### scikit-spatial

Spatial objects and computations based on NumPy arrays.

`pip install scikit-spatial` · installs (wheel) · licence: BSD License · rank 14830 · last release 2026-11-08 · [PyPI](https://pypi.org/project/scikit-spatial/) · [docs](https://scikit-spatial.readthedocs.io) · [source](https://github.com/ajhynes7/scikit-spatial)

<details><summary>README extract</summary>

This package provides spatial objects based on NumPy arrays, as well as
computations using these objects. The package includes computations for
2D, 3D, and higher-dimensional space.

The following spatial objects are provided:

- Point
- Points
- Vector
- Line
- LineSegment
- Plane
- Circle
- Sphere
- Triangle
- Cylinder ...

Features:
This package has little to no overlap with the functionality of
`scipy.spatial`. It can be viewed as an object-oriented extension. ...

Example:
```python
>>> from skspatial.objects import Vector

>>> vector = Vector([2, 0, 0])
```

Sections: Introduction, Why this instead of `scipy.spatial` or `sympy.geometry`?, Example Usage, Measurement, Comparison, Projection, Intersection, Fitting, Transformation

</details>

### pytango

Python bindings for the cppTango library; part of the Tango Distributed Control System toolkit

`pip install pytango` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 14875 · last release 2026-07-20 · [PyPI](https://pypi.org/project/pytango/) · [docs](https://pytango.readthedocs.io) · [source](https://gitlab.com/tango-controls/pytango.git)

_README extract left out: share-alike licence._

### pyvista-frd-reader

Read CalculiX FRD result files into PyVista, backed by a C++ core with a C ABI.

`pip install pyvista-frd-reader` · installs (wheel) · licence: MIT · rank 14885 · last release 2026-10-09 · [PyPI](https://pypi.org/project/pyvista-frd-reader/)

<details><summary>README extract</summary>

Read and write CalculiX FRD files with PyVista. The Python API returns a
`pyvista.UnstructuredGrid`; the C API exposes the same parser without a
Python dependency.

Example:
```python
import pyvista_frd

mesh = pyvista_frd.read("result.frd")
mesh.plot(scalars="STRESS_Mises")
```

Sections: pyvista-frd-reader, Read time steps, Read node and element sets, Named surfaces, Write and convert files, Relationship to PyVista, C API, Documentation, Credit

</details>

### saleae

Library to control a Saleae

`pip install saleae` · installs from source (sdist only) · licence: MIT License · rank 14895 · last release 2021-02-06 · [PyPI](https://pypi.org/project/saleae/)

<details><summary>README extract</summary>

This library implements the control protocol for the
Saleae Logic Analyzer. It is based off of the
documentation and example here:

IMPORTANT: You must enable the 'Remote Scripting Server' in Saleae. Click
on "Options" in the top-right, the "Developer" tab, and check "Enable scripting
socket server". This should not require a restart. ...

Example:
```python
import saleae
s = saleae.Saleae()
s.capture_to_file('/tmp/test.logicdata')
```

Sections: python-saleae, Usage

</details>

### vowpalwabbit

Vowpal Wabbit Python package

`pip install vowpalwabbit` · installs (wheel) · licence: BSD License · rank 14901 · last release 2026-09-27 · [PyPI](https://pypi.org/project/vowpalwabbit/)

<details><summary>README extract</summary>

Vowpal Wabbit is a fast machine learning library for online learning, and this is the python wrapper for the project.

Python Version: 3.10, 3.11, 3.12, or 3.13

Pre-built wheels are available on PyPI for:

* Linux (x86_64, aarch64)
* macOS (x86_64, arm64)
* Windows (x86_64) ...

Example:
```python
>>> import vowpalwabbit
>>> vw = vowpalwabbit.Workspace(quiet=True)
>>> ex = vw.example('1 | a b c')
>>> vw.learn(ex)
>>> vw.predict(ex)
```

Sections: Vowpal Wabbit Python Wrapper, Requirements, Usage, Troubleshooting

</details>

### dss-python

Python interface (bindings and tools) for OpenDSS. Based on the AltDSS/DSS C-API project, the alternative OpenDSS implementation from DSS-Extensions.org. Multiplatform, API-compatible/drop-in replacement for the COM version of OpenDSS.

`pip install dss-python` · installs (wheel) · licence: BSD License · rank 14907 · last release 2024-03-29 · [PyPI](https://pypi.org/project/dss-python/) · [docs](https://dss-extensions.org/DSS-Python) · [source](https://github.com/dss-extensions/DSS-Python.git)

<details><summary>README extract</summary>

Python bindings and misc tools for using our to our customized/alternative implementation of OpenDSS, AltDSS/DSS C-API library. OpenDSS is an open-source electric power distribution system simulator distributed by EPRI. ...

Example:
```python
import win32com.client
dss_engine = win32com.client.gencache.EnsureDispatch("OpenDSSEngine.DSS")
```

Sections: Missing features and limitations, Extra features, Building, Documentation, Example usage, Roadmap: docs and interactive features, Questions?

</details>

### wigglystuff

Collection of Anywidget Widgets

`pip install wigglystuff` · installs (wheel) · licence: MIT License · rank 14925 · last release 2026-10-19 · [PyPI](https://pypi.org/project/wigglystuff/)

<details><summary>README extract</summary>

> "A collection of creative AnyWidgets for Python notebook environments."

The project uses anywidget under the hood so our tools should work in marimo, Jupyter, Shiny for Python, VSCode, Colab, Solara, etc. Because of the anywidget integration you should also be able interact with ipywidgets natively.

Sections: wigglystuff, Widget Gallery, 3rd party widgets

</details>

### pygad

PyGAD: A Python Library for Building the Genetic Algorithm and Training Machine Learning Algoithms (Keras & PyTorch).

`pip install pygad` · installs (wheel) · licence: not stated · rank 14932 · last release 2026-10-16 · [PyPI](https://pypi.org/project/pygad/) · [docs](https://pygad.readthedocs.io)

<details><summary>README extract</summary>

PyGAD is an open-source, easy-to-use Python 3 library for building the genetic algorithm and optimizing machine learning algorithms. It supports Keras and PyTorch, and it can optimize both single-objective and multi-objective problems.

> Try Vilvik, a free cloud-based tool powered by PyGAD. ...

Example:
```python
import pygad
import numpy

"""
Given the following function:
    y = f(w1:w6) = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + w6x6
    where (x1,x2,x3,x4,x5,x6)=(4,-2,3.5,5,-11,-4.7) and y=44
What are the best values for the 6 weights (w1 to w6)? We are going to use the genetic algorithm to optimize this function.
"""

...
```

...

</details>

### crowd-kit

Computational Quality Control for Crowdsourcing

`pip install crowd-kit` · installs (wheel) · licence: Apache-2.0 · rank 14935 · last release 2025-10-13 · [PyPI](https://pypi.org/project/crowd-kit/) · [docs](https://crowd-kit.readthedocs.io/) · [source](https://github.com/Toloka/crowd-kit)

<details><summary>README extract</summary>

[][pypi_link]
[][github_tests_link]
[][codecov_link]
[][docs_link]
[][paper_link]

Crowd-Kit is a powerful Python library that implements commonly-used aggregation methods for crowdsourced annotation and offers the relevant metrics and datasets. We strive to implement functionality that simplifies working with crowdsourced data. ...

Sections: Crowd-Kit: Computational Quality Control for Crowdsourcing, Getting Started, Implemented Aggregation Methods, Categorical Responses, Multi-Label Responses, Textual Responses, Image Segmentation, Pairwise Comparisons, Learning from Crowds

</details>

### tensorflow-io-nightly

TensorFlow IO

`pip install tensorflow-io-nightly` · does not install on CPython 3.14 · licence: Apache Software License · rank 14955 · last release 2023-03-09 · [PyPI](https://pypi.org/project/tensorflow-io-nightly/) · [docs](https://tensorflow.org/io) · [source](https://github.com/tensorflow/io)

<details><summary>README extract</summary>

TensorFlow I/O is a collection of file systems and file formats that are not
available in TensorFlow's built-in support. A full list of supported file systems
and file formats by TensorFlow I/O can be found here.

The use of tensorflow-io is straightforward with keras. ...

Example:
```python
import tensorflow as tf
import tensorflow_io as tfio

# Read the MNIST data into the IODataset.
dataset_url = "
d_train = tfio.IODataset.from_mnist(
    dataset_url + "train-images-idx3-ubyte.gz",
    dataset_url + "train-labels-idx1-ubyte.gz",
)

# Shuffle the elements of the dataset.
d_train = d_train.shuffle(buffer_size=1024)

...
```

Sections: TensorFlow I/O, Python Package, Docker Images, R Package, TensorFlow Version Compatibility, Performance Benchmarking, Additional Information

</details>

### mnn

C methods for MNN Package

`pip install mnn` · installs (wheel) · licence: BSD License · rank 14963 · last release 2026-10-29 · [PyPI](https://pypi.org/project/mnn/)

<details><summary>README extract</summary>

This is a python package for MNN

Sections: MNN Python Package, Dependencies

</details>

### qiskit-ibm-experiment

Qiskit IBM Experiment service for accessing the quantum experiment interface at IBM

`pip install qiskit-ibm-experiment` · installs (wheel) · licence: Apache Software License · rank 14968 · last release 2024-09-05 · [PyPI](https://pypi.org/project/qiskit-ibm-experiment/) · [docs](https://qiskit-extensions.github.io/qiskit-ibm-experiment) · [source](https://github.com/Qiskit/qiskit-ibm-experiment)

<details><summary>README extract</summary>

Qiskit is an open-source SDK for working with quantum computers at the level of circuits, algorithms, and application modules.

This project contains a service that allows accessing the [IBM Quantum]
experiment database.

Example:
```python
from qiskit_ibm_experiment import IBMExperimentService
IBMExperimentService.save_account(token='MY_API_TOKEN')
```

Sections: Qiskit IBM Experiment service, Provider Setup

</details>

### returnn

The RWTH extensible training framework for universal recurrent neural networks

`pip install returnn` · installs (wheel) · licence: Other/Proprietary License · rank 14984 · last release 2026-11-06 · [PyPI](https://pypi.org/project/returnn/)

<details><summary>README extract</summary>

GitHub repository.
RETURNN paper 2016,
RETURNN paper 2018.

RETURNN - RWTH extensible training framework for universal recurrent neural networks,
is a PyTorch/TensorFlow-based implementation of modern recurrent neural network architectures.
It is optimized for fast and reliable training of recurrent neural networks in a multi-GPU environment. ...

Sections: Welcome to RETURNN, Dependencies

</details>

### pyhdf

Python interface to the NCSA HDF4 library

`pip install pyhdf` · installs (wheel) · licence: OSI Approved · rank 14993 · last release 2026-07-11 · [PyPI](https://pypi.org/project/pyhdf/)

<details><summary>README extract</summary>

pyhdf is a python wrapper around the NCSA HDF version 4 library.
The SD (Scientific Dataset), VS (Vdata) and V (Vgroup) API's
are currently implemented. NetCDF files can also be
read and modified. It supports both Python 2 and Python 3.

*Note:* The sourceforge pyhdf
website and
project are out-of-date. ...

Sections: pyhdf, Documentation, Examples

</details>

## Also in this topic

- [duckdb](database.md#duckdb) - DuckDB in-process database
- [statsmodels](office-business-financial.md#statsmodels) - Statistical computations and models for Python
- [h5py](database.md#h5py) - Read and write HDF5 files from Python
- [pandas-gbq](internet.md#pandas-gbq) - Google BigQuery connector for pandas
- [trimesh](multimedia-graphics.md#trimesh) - Import, export, process, analyze and view triangular meshes.
- [soxr](multimedia-sound-audio.md#soxr) - High quality, one-dimensional sample-rate conversion library
- [rq](internet.md#rq) - RQ is a simple, lightweight, library for creating background jobs, and processing them.
- [ortools](office-business-scheduling.md#ortools) - Google OR-Tools python libraries and modules
- [bokeh](office-business.md#bokeh) - Interactive plots and applications in the browser from Python
- [firecrawl-py](internet.md#firecrawl-py) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [vtk](multimedia-graphics.md#vtk) - VTK is an open-source toolkit for 3D computer graphics, image processing, and visualization
- [cuda-python](education.md#cuda-python) - CUDA Python: Performance meets Productivity
- [ndg-httpsclient](internet.md#ndg-httpsclient) - Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
- [cuda-core](education.md#cuda-core) - cuda.core: pythonic CUDA module
- [chdb](database.md#chdb) - chDB is an in-process OLAP SQL Engine powered by ClickHouse
- [ibis-framework](database-front-ends.md#ibis-framework) - The portable Python dataframe library
- [chdb-core](database.md#chdb-core) - chDB is an in-process OLAP SQL Engine powered by ClickHouse
- [pyloudnorm](multimedia-sound-audio.md#pyloudnorm) - Implementation of ITU-R BS.1770-4 loudness algorithm in Python.
- [julius](multimedia-sound-audio.md#julius) - Nice DSP sweets: resampling, FFT Convolutions. All with PyTorch, differentiable and with CUDA support.
- [nvtx](database.md#nvtx) - Python NVTX - Python code annotation library
- [uncertainties](education.md#uncertainties) - calculations with values with uncertainties, error propagation
- [nccl4py](education.md#nccl4py) - NCCL4Py: Python bindings for NCCL
- [cadquery](internet.md#cadquery) - CadQuery is a parametric scripting language for creating and traversing CAD models
- [PubChemPy](database-front-ends.md#pubchempy) - A simple Python wrapper around the PubChem PUG REST API.
- [open3d](education.md#open3d) - Open3D: A Modern Library for 3D Data Processing.
- [svgpathtools](multimedia-graphics.md#svgpathtools) - A collection of tools for manipulating and analyzing SVG Path objects and Bezier curves.
- [seleniumbase](internet.md#seleniumbase) - SeleniumBase is a framework for web crawling, scraping, and testing. Supports pytest. CDP Mode adds stealth. Includes many tools.
- [torch-audiomentations](multimedia.md#torch-audiomentations) - A Pytorch library for audio data augmentation. Inspired by audiomentations. Useful for deep learning.
- [panel](office-business.md#panel) - The powerful data exploration & web app framework for Python.
- [supervision](multimedia-graphics.md#supervision) - A set of easy-to-use utils that will come in handy in any Computer Vision project
- [lap](education.md#lap) - Linear Assignment Problem solver (LAPJV/LAPMOD).
- [graphframes-py](database-front-ends.md#graphframes-py) - GraphFrames: Graph Processing Framework for Apache Spark
- [sigfig](education.md#sigfig) - Python library for rounding numbers (with expected results)
- [cascadio](multimedia-graphics.md#cascadio) - Convert STEP files to GLB using OpenCASCADE
- [django-rq](internet.md#django-rq) - An app that provides django integration for RQ (Redis Queue)
- [QuantLib](office-business-financial.md#quantlib) - Python bindings for the QuantLib library
- [firecrawl](internet.md#firecrawl) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [flameprof](internet.md#flameprof) - cProfile flamegraph generator
- [bd-materials](multimedia-graphics.md#bd-materials) - Typical-values engineering materials for build123d -- with finishes and three.js PBR looks
- [scikit-rf](communications-ham-radio.md#scikit-rf) - Object Oriented Microwave Engineering
- [nautilus-trader](office-business-financial.md#nautilus-trader) - Production-grade Rust-native trading engine with deterministic event-driven architecture
- [maggma](database-front-ends.md#maggma) - Framework to develop datapipelines from files on disk to full dissemenation API
- [sbvirtualdisplay](internet.md#sbvirtualdisplay) - A customized pyvirtualdisplay for SeleniumBase.
- [jobflow](database-front-ends.md#jobflow) - jobflow is a library for writing computational workflows
- [mycdp](internet.md#mycdp) - Autogenerated CDP utilities for Python
- [selenium-stealth](internet.md#selenium-stealth) - Trying to make python selenium more stealthy.
- [quantities](education.md#quantities) - Support for physical quantities with units, based on numpy
- [rapids-logger](database.md#rapids-logger) - Logging framework for RAPIDS built around spdlog
- [lapx](education.md#lapx) - Linear assignment problem solvers, including single and batch solvers.
- [pandas-ta](office-business-financial.md#pandas-ta) - A Comprehensive Python 3 Technical Analysis Library with Pandas Dataframe Extension for Quantitative Researchers, Traders, and Investors.
- [vortex-data](database.md#vortex-data) - Python bindings for Vortex, an Apache Arrow-compatible toolkit for working with compressed array data.
- [clickhouse-cityhash](internet.md#clickhouse-cityhash) - Python-bindings for CityHash, a fast non-cryptographic hash algorithm
- [tika](database-front-ends.md#tika) - Apache Tika Python library
- [gerbonara](artistic-software.md#gerbonara) - Tools to handle Gerber and Excellon files in Python
- [pymatgen-analysis-defects](other-nonlisted-topic.md#pymatgen-analysis-defects) - Pymatgen extension for defects analysis
- [quantstats](office-business-financial.md#quantstats) - Portfolio analytics for quants
- [mp-pyrho](other-nonlisted-topic.md#mp-pyrho) - Tools for re-griding periodic volumetric quantum chemistry data for machine-learning purposes.
- [audiomentations](multimedia.md#audiomentations) - A Python library for audio data augmentation. Inspired by albumentations. Useful for machine learning.
- [numpy-rms](multimedia-sound-audio.md#numpy-rms) - A fast python library for calculating the RMS of a NumPy array
- [numpy-minmax](multimedia-sound-audio.md#numpy-minmax) - A fast python library for finding both min and max value in a NumPy array
- [rq-dashboard](internet.md#rq-dashboard) - rq-dashboard is a general purpose, lightweight, web interface to monitor your RQ queues, jobs, and workers in realtime.
- [noisereduce](education.md#noisereduce) - Noise reduction using Spectral Gating in Python
- [libcudf-cu12](database.md#libcudf-cu12) - cuDF - GPU Dataframe (C++)
- [samplerate](multimedia-sound-audio.md#samplerate) - Monolithic python wrapper for libsamplerate based on pybind11 and NumPy
- [onnx-asr](multimedia-sound-audio.md#onnx-asr) - A lightweight Python package for Automatic Speech Recognition using ONNX models
- [bitmath](communications-file-sharing.md#bitmath) - Pythonic module for representing and manipulating file sizes with different prefix notations (file size unit conversion)
- [librmm-cu12](database.md#librmm-cu12) - Library for CUDA memory management
- [cudf-cu12](database.md#cudf-cu12) - cuDF - GPU Dataframe
- [rmm-cu12](database.md#rmm-cu12) - Library for CUDA memory management
- [pylibcudf-cu12](database.md#pylibcudf-cu12) - pylibcudf - Python bindings for libcudf
- [libkvikio-cu12](database.md#libkvikio-cu12) - KvikIO - GPUDirect Storage (C++)
- [imgui-bundle](artistic-software.md#imgui-bundle) - Dear ImGui for Python and C++, batteries included: real-time GUIs, plots and live data, on the desktop and in the browser, with no server.
- [pyrealsense2](multimedia-video.md#pyrealsense2) - Python Wrapper for Realsense SDK 2.0.
- [geoip2fast](internet.md#geoip2fast) - GeoIP2Fast is the fastest GeoIP2 country/city/asn lookup library that supports IPv4 and IPv6. A search takes less than 0.00003 seconds. It has its own data file updated twice a week with Maxmind-Geolite2-CSV, supports IPv4/IPv6 and is Pure Python!
- [pandas-ta-classic](office-business-financial.md#pandas-ta-classic) - Technical Analysis Indicators - Pandas TA Classic is an easy to use Python 3 Pandas Extension with a comprehensive collection of indicators and TA-Lib patterns.
- [pyFFTW](multimedia-sound-audio.md#pyfftw) - A pythonic wrapper around FFTW, the FFT library, presenting a unified interface for all the supported transforms.
- [manim](multimedia-graphics.md#manim) - Animation engine for explanatory math videos.
- [py2neo-history](database.md#py2neo-history) - Python client library and toolkit for Neo4j
- [solcast](internet.md#solcast) - a simple Python SDK for the Solcast API
- [pyamg](education.md#pyamg) - PyAMG: Algebraic Multigrid Solvers in Python
- [questdb](database-front-ends.md#questdb) - QuestDB client library for Python
- [duckdb-cli](database.md#duckdb-cli) - The DuckDB CLI
- [pydap](internet-www-http.md#pydap) - A pure python implementation of the Data Access Protocol.
- [pytricia](internet-log-analysis.md#pytricia) - An efficient IP address storage and lookup module for Python.
- [ipfshttpclient](internet.md#ipfshttpclient) - Python IPFS HTTP CLIENT library
- [jina](database-database-engines-servers.md#jina) - Multimodal AI services & pipelines with cloud-native stack: gRPC, Kubernetes, Docker, OpenTelemetry, Prometheus, Jaeger, etc.
- [cwl-utils](file-formats.md#cwl-utils) - 
- [torchreid](education.md#torchreid) - Torchreid-Pip: Deep learning person re-identification in PyTorch.
- [grafana-client](communications.md#grafana-client) - A client library for accessing the Grafana HTTP API, written in Python
- [minimalmodbus](communications.md#minimalmodbus) - Easy-to-use Modbus RTU and Modbus ASCII implementation for Python
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
- [clip-interrogator](education.md#clip-interrogator) - Generate a prompt from an image
- [dask-cuda](database.md#dask-cuda) - Utilities for Dask and CUDA interactions
- [times](internet.md#times) - Times is a small, minimalistic, Python library for dealing with time conversions between universal time and arbitrary timezones.
- [py-vollib-vectorized](office-business-financial.md#py-vollib-vectorized) - A fast, vectorized approach to calculating Implied Volatility and Greeks using the Black, Black-Scholes and Black-Scholes-Merton pricing.
- [blackjax](education.md#blackjax) - Flexible and fast sampling in Python
- [pypylon](multimedia-graphics.md#pypylon) - The official Python language binding for the Basler pylon C++ APIs.
- [librmm-cu13](database.md#librmm-cu13) - Library for CUDA memory management
- [rmm-cu13](database.md#rmm-cu13) - Library for CUDA memory management
- [docplex](other-nonlisted-topic.md#docplex) - The IBM Decision Optimization CPLEX Modeling for Python
- [scikit-video](multimedia-video.md#scikit-video) - Video Processing in Python
- [nbtoolbelt](education.md#nbtoolbelt) - Tools to work with Jupyter notebooks
- [docarray](database-database-engines-servers.md#docarray) - The data structure for multimodal data
- [gravis](multimedia-graphics.md#gravis) - Interactive graph visualizations with Python and HTML/CSS/JS.
- [pyDOE3](education.md#pydoe3) - Design of experiments for Python
- [ft-pandas-ta](office-business-financial.md#ft-pandas-ta) - An easy to use Python 3 Pandas Extension with 130+ Technical Analysis Indicators. Can be called from a Pandas DataFrame or standalone like TA-Lib. Correlation tested with TA-Lib.
- [cloudml-hypertune](internet.md#cloudml-hypertune) - A library to report Google CloudML Engine HyperTune metrics.
- [xlcalculator](office-business-financial.md#xlcalculator) - Converts MS Excel formulas to Python and evaluates them.
- [gooddata-sdk](database.md#gooddata-sdk) - GoodData Cloud Python SDK
- [py2neo](database.md#py2neo) - Python client library and toolkit for Neo4j
- [ovrtx](multimedia-graphics.md#ovrtx) - Omniverse RTX
- [klepto](database.md#klepto) - persistent caching to memory, disk, or database
- [sphinxcontrib-katex](documentation.md#sphinxcontrib-katex) - A Sphinx extension for rendering math in HTML pages
- [graphdatascience](database.md#graphdatascience) - A Python client for the Neo4j Graph Data Science (GDS) library
- [atomate2](other-nonlisted-topic.md#atomate2) - atomate2 is a library of materials science workflows
- [pybboxes](education.md#pybboxes) - Light Weight Toolkit for Bounding Boxes
- [hdf5storage](database.md#hdf5storage) - Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files.
- [matminer](other-nonlisted-topic.md#matminer) - matminer is a library that contains tools for data mining in Materials Science
- [stftpitchshift](artistic-software.md#stftpitchshift) - STFT based pitch and timbre shifting
- [open3d-cpu](education.md#open3d-cpu) - Open3D: A Modern Library for 3D Data Processing.
- [covalent](adaptive-technologies.md#covalent) - Covalent Workflow Tool
- [pymetis](multimedia-graphics.md#pymetis) - A graph partitioning package
- [pyxnat](internet-www-http-2.md#pyxnat) - XNAT in Python
- [vulkan](multimedia-graphics.md#vulkan) - Ultimate Python binding for Vulkan API
